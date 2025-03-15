import cv2
from ultralytics import YOLO
from flask import Flask, Response, request
import threading
import os
import time

print("DEBUG: detect.py loaded!")  # Confirms this file is running

# Attempt to load YOLO model
try:
    model = YOLO('yolov8n.pt')
    print("DEBUG: YOLO model loaded successfully!")
except Exception as e:
    print(f"DEBUG: Error loading YOLO model: {e}")

app = Flask(__name__)

output_frame = None
lock = threading.Lock()
is_running = False
current_video = None

def detect_objects():
    """
    Reads the video file frame-by-frame, runs YOLO detection,
    counts vehicles, draws bounding boxes, and syncs playback 
    to the video’s original FPS for near real-time matching.
    """
    global output_frame, lock, is_running, current_video

    if not current_video:
        print("DEBUG: No video file set in current_video!")
        return

    print(f"DEBUG: Starting detection on {current_video}")

    cap = cv2.VideoCapture(current_video)
    print(f"DEBUG: cap.isOpened() returned {cap.isOpened()}")

    if not cap.isOpened():
        print(f"DEBUG: Could not open video: {current_video}")
        return

    # Read the video's original FPS
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"DEBUG: Video FPS = {video_fps}")
    if video_fps <= 0:
        # Fallback if FPS is invalid
        video_fps = 30.0

    is_running = True

    while cap.isOpened() and is_running:
        start_time = time.time()  # measure how long detection takes per frame

        ret, frame = cap.read()
        print(f"DEBUG: ret={ret}")

        if not ret:
            print("DEBUG: No more frames or error reading frame.")
            break

        # Run YOLO detection
        results = model(frame)
        print(f"DEBUG: Frame processed, {len(results)} results found.")

        # Count vehicles in this frame
        vehicle_count = 0

        # Draw bounding boxes & increment count
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                # If the class is one of the "vehicle" types (car=2, motorcycle=3, bus=5, truck=7)
                if class_id in [2, 3, 5, 7]:
                    vehicle_count += 1
                    x1, y1, x2, y2 = box.xyxy[0]
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)),
                                  (0, 255, 0), 2)
                    cv2.putText(frame, 'Vehicle', (int(x1), int(y1) - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Draw the vehicle count on the top-left corner
        cv2.putText(frame,
                    f"Vehicle Count: {vehicle_count}",
                    (20, 40),  # position
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,       # font scale
                    (0, 255, 0),
                    2)         # thickness

        # Store the processed frame for streaming
        with lock:
            output_frame = frame.copy()

        # Sync to the video’s original FPS
        frame_time = 1.0 / video_fps  # target time per frame
        elapsed = time.time() - start_time
        sleep_time = frame_time - elapsed
        if sleep_time > 0:
            time.sleep(sleep_time)

    cap.release()
    is_running = False
    print("DEBUG: Detection stopped, cap released.")

@app.route('/test')
def test_route():
    """
    A quick debug route to confirm Flask is running.
    http://127.0.0.1:5000/test
    """
    print("DEBUG: /test route called.")
    return "Test route is working!"

@app.route('/video_feed')
def video_feed():
    """
    Streams out the processed frames in MJPEG format.
    """
    print("DEBUG: /video_feed route called.")

    def generate():
        global output_frame, lock
        while True:
            with lock:
                if output_frame is None:
                    # No frames yet, skip
                    continue

                # Encode frame as JPEG
                _, buffer = cv2.imencode('.jpg', output_frame)
                frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Receives a video file via POST, saves it, then starts detection.
    """
    global current_video, is_running

    print("DEBUG: /upload route called.")

    if is_running:
        print("DEBUG: Attempted to upload while detection is running.")
        return 'Detection already running', 400

    if 'videoFile' not in request.files:
        print("DEBUG: No 'videoFile' in request.")
        return 'No file uploaded', 400

    file = request.files['videoFile']
    if file.filename == '':
        print("DEBUG: File selected has empty filename.")
        return 'No file selected', 400

    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    current_video = file_path

    print(f"DEBUG: Video file uploaded -> {file_path}")

    # Start YOLO detection in a new thread
    threading.Thread(target=detect_objects).start()

    return 'File uploaded and detection started', 200

@app.route('/stop', methods=['POST'])
def stop_detection():
    """
    Sets is_running to False, stopping detect_objects loop.
    """
    global is_running
    print("DEBUG: /stop route called.")
    is_running = False
    return 'Detection stopped', 200

if __name__ == '__main__':
    print("DEBUG: Flask app starting on 0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000)
