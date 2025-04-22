# import cv2
# import numpy as np
# import threading
# from ultralytics import YOLO
# import tkinter as tk
# from PIL import Image, ImageTk

# import torch
# from torch.serialization import add_safe_globals
# from ultralytics.nn.tasks import DetectionModel

# add_safe_globals({'ultralytics.nn.tasks.DetectionModel': DetectionModel})

# # Load the YOLOv8 model
# model = YOLO('yolov8n.pt')

# # Load video
# video_path = 'uploads/test_file.mp4'
# cap = cv2.VideoCapture(video_path)

# # Define rhombus ROI
# rhombus_roi = np.array([[80, 400], [240, 100], [400, 100], [550, 400]], np.int32).reshape((-1, 1, 2))

# # Create Tkinter window
# root = tk.Tk()
# root.title("Vehicle Detection")
# root.geometry("800x700")
# root.resizable(False, False)

# # Center the window on the screen
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# x = (screen_width // 2) - (800 // 2)
# y = (screen_height // 2) - (700 // 2)
# root.geometry(f"+{x}+{y}")

# # Add title
# title_label = tk.Label(root, text="Vehicle Detection and Counting", font=("Arial", 20, "bold"), pady=10)
# title_label.pack()

# # Frame to show video
# video_frame = tk.Label(root)
# video_frame.pack()

# # Stop flag
# stop_flag = False

# def stop_detection():
#     global stop_flag
#     stop_flag = True
#     root.quit()

# # Stop button
# stop_button = tk.Button(root, text="Stop Detection", command=stop_detection,
#                         font=("Arial", 14), bg="red", fg="white", pady=5, padx=10)
# stop_button.pack(pady=20)

# def update_frame():
#     global stop_flag
#     ret, frame = cap.read()
#     if not ret or stop_flag:
#         cap.release()
#         return

#     results = model(frame, "cuda")
#     vehicle_count = 0

#     # Draw rhombus
#     cv2.polylines(frame, [rhombus_roi], isClosed=True, color=(255, 0, 0), thickness=2)

#     for result in results:
#         for box in result.boxes:
#             cls = int(box.cls[0])
#             if cls in [2, 3, 5, 7]:  # Car, motorcycle, bus, truck
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 cx = int((x1 + x2) / 2)
#                 cy = int((y1 + y2) / 2)

#                 if cv2.pointPolygonTest(rhombus_roi, (cx, cy), False) >= 0:
#                     vehicle_count += 1
#                     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
#                     cv2.putText(frame, 'Vehicle', (x1, y1 - 5),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
#                     cv2.circle(frame, (cx, cy), 3, (0, 255, 255), -1)

#     # Display vehicle count
#     cv2.putText(frame, f"Vehicles: {vehicle_count}",
#                 (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

#     # Convert BGR to RGB for Tkinter
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     img = Image.fromarray(frame_rgb)
#     imgtk = ImageTk.PhotoImage(image=img)
#     video_frame.imgtk = imgtk
#     video_frame.configure(image=imgtk)

#     if not stop_flag:
#         video_frame.after(10, update_frame)

# # Start video thread
# threading.Thread(target=update_frame).start()

# # Start the GUI loop
# root.mainloop()


import cv2
import numpy as np
import threading
from ultralytics import YOLO
import tkinter as tk
from PIL import Image, ImageTk

import torch
from torch.serialization import add_safe_globals
from ultralytics.nn.tasks import DetectionModel

# Fix for PyTorch 2.6+: allow loading DetectionModel class safely
add_safe_globals({'ultralytics.nn.tasks.DetectionModel': DetectionModel})

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Load video
video_path = 'uploads/test_file.mp4'
cap = cv2.VideoCapture(video_path)

# Define rhombus ROI
rhombus_roi = np.array([[80, 400], [240, 100], [400, 100], [550, 400]], np.int32).reshape((-1, 1, 2))

# Create Tkinter window
root = tk.Tk()
root.title("Vehicle Detection")
root.geometry("800x700")
root.resizable(False, False)

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (800 // 2)
y = (screen_height // 2) - (700 // 2)
root.geometry(f"+{x}+{y}")

# Add title
title_label = tk.Label(root, text="Vehicle Detection and Counting", font=("Arial", 20, "bold"), pady=10)
title_label.pack()

# Frame to show video
video_frame = tk.Label(root)
video_frame.pack()

# Stop flag
stop_flag = False

def stop_detection():
    global stop_flag
    stop_flag = True
    root.quit()

# Stop button
stop_button = tk.Button(root, text="Stop Detection", command=stop_detection,
                        font=("Arial", 14), bg="red", fg="white", pady=5, padx=10)
stop_button.pack(pady=20)

def update_frame():
    global stop_flag
    ret, frame = cap.read()
    if not ret or stop_flag:
        cap.release()
        return

    results = model(frame, device="cuda")
    vehicle_count = 0

    # Draw rhombus
    cv2.polylines(frame, [rhombus_roi], isClosed=True, color=(255, 0, 0), thickness=2)

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            if cls in [2, 3, 5, 7]:  # Car, motorcycle, bus, truck
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)

                if cv2.pointPolygonTest(rhombus_roi, (cx, cy), False) >= 0:
                    vehicle_count += 1
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                    cv2.putText(frame, 'Vehicle', (x1, y1 - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                    cv2.circle(frame, (cx, cy), 3, (0, 255, 255), -1)

    # Display vehicle count
    cv2.putText(frame, f"Vehicles: {vehicle_count}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    # Convert BGR to RGB for Tkinter
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)
    video_frame.imgtk = imgtk
    video_frame.configure(image=imgtk)

    if not stop_flag:
        video_frame.after(10, update_frame)

# Start video thread
threading.Thread(target=update_frame).start()

# Start the GUI loop
root.mainloop()
