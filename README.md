```markdown
# 🚗 Vehicle Detection and Counting using YOLOv8 (Flask-Based)

This project performs **vehicle detection and counting** from a video file using **YOLOv8** and **Flask**. It uses OpenCV to read frames, perform object detection with YOLOv8, and count detected vehicles in real-time. The detection results are visualized with bounding boxes.

---

## ✅ Features
- Vehicle detection using YOLOv8
- Real-time counting from video files
- Uses Flask for simple backend execution
- Efficient processing with OpenCV

---

## 🛠 Tech Stack
- **Language**: Python  
- **Framework**: Flask  
- **Model**: YOLOv8 (`yolov8n.pt`)  
- **Libraries**: OpenCV, Ultralytics, Flask

---

## 📁 Folder Structure
```
├── uploads/               # Folder containing input video(s)
│   └── test_file.mp4      # Sample video file
├── yolov8n.pt             # YOLOv8n model file
├── detect.py              # Main script for detection and counting
├── requirements.txt       # Python dependencies
├── screenshot.png         # (Optional) Screenshot of output
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/akashprajapaticse/Vehicle_Detection_Counting.git
cd Vehicle_Detection_Counting
```

### 2. Set up a Python virtual environment
```bash
python -m venv venv
source venv/bin/activate   # For macOS/Linux
.\venv\Scripts\activate    # For Windows
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python detect.py
```

---

## 📝 Notes
- Make sure `yolov8n.pt` is present in the project directory.
- Place your input video inside the `uploads/` folder before running the script.
- Adjust the video file name/path in `detect.py` if needed.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🙌 Author
**Akash Prajapati** – [GitHub](https://github.com/akashprajapaticse)
```