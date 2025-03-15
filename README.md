# 🚗 Vehicle Detection and Counting System

This project is a **Vehicle Detection and Counting System** using **YOLO v8** with a Flask backend for YOLO inference and a Node.js-based frontend. It allows users to upload videos for real-time vehicle detection and counting.

---

## 📌 **Features**
✅ Real-time vehicle detection using YOLO v8  
✅ Vehicle counting and bounding box visualization  
✅ Flask backend for YOLO inference  
✅ Node.js frontend for live streaming  
✅ Supports MJPEG video stream  
✅ REST endpoints for video upload and control  

---

## 🛠️ **Tech Stack**
- **Backend:** Flask (Python)  
- **Model:** YOLO v8 (ultralytics)  
- **Frontend:** Node.js, Express.js  
- **Libraries:** OpenCV, TensorFlow, Flask, Socket.io  

---

## 📸 **Screenshots**
### 🚀 Live Detection Example:
![Live Detection](./screenshots/live_detection.png)

### 📊 Counting Example:
![Counting](./screenshots/counting.png)

---

## 📂 **Folder Structure**
```
├── models/                # YOLO model files
├── public/                # Frontend files
│   ├── index.html         # Main HTML file
│   ├── styles.css         # Styling
│   └── script.js          # Frontend logic
├── uploads/               # Uploaded video files
├── detect.py              # Flask backend with YOLO detection
├── server.js              # Node.js server
├── requirements.txt       # Python dependencies
├── package.json           # Node.js dependencies
├── README.md              # Project documentation
```

---

## 🚀 **Setup and Installation**
### ✅ **1. Clone the repository**:
```bash
git clone https://github.com/akashprajapaticse/Vehicle_Detection_Counting.git
```

### ✅ **2. Set up Python Backend**
1. Navigate to the project folder:
```bash
cd Vehicle_Detection_Counting
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux/MacOS
.\venv\Scripts\activate   # Windows
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Start Flask backend:
```bash
python detect.py
```

---

### ✅ **3. Set up Node.js Frontend**
1. Open a new terminal in the same project folder.
2. Install Node.js dependencies:
```bash
npm install
```

3. Start the Node.js server:
```bash
node server.js
```

---

### ✅ **4. Access the Application**
- Flask API (YOLO detection) → `http://localhost:5000/test`  
- Node.js frontend → `http://localhost:3001`  
- Video feed → `http://localhost:5000/video_feed`  

---

## 🎯 **API Endpoints**
### 🔹 **Upload a Video**  
`POST` → `/upload`  
- Accepts a video file  
- Saves it to `/uploads`  
- Starts YOLO detection in a separate thread  

### 🔹 **Stop Detection**  
`POST` → `/stop`  
- Stops the YOLO detection loop  

### 🔹 **Stream Video Feed**  
`GET` → `/video_feed`  
- Returns processed frames as MJPEG stream  

### 🔹 **Test Route**  
`GET` → `/test`  
- Confirms Flask backend is running  

---

## 🚦 **How It Works**
1. User uploads a video from the frontend  
2. Flask backend starts YOLO detection using `threading`  
3. YOLO detects vehicles in each frame and counts them  
4. The processed frames are sent to the frontend using Flask’s `Response` object  
5. Frontend updates in real-time using the video feed  

---

## ⚠️ **Troubleshooting**
❗ **YOLO model load failure**  
- Ensure that `yolov8n.pt` is present in the root folder.  
- Run the following command to install `ultralytics`:  
```bash
pip install ultralytics
```

❗ **Port conflict**  
- Make sure that Flask is using port `5000` and Node.js is using port `3001`.  

---

## 📜 **License**
This project is licensed under the **MIT License**.

---

## 🙌 **Contributors**
👤 **Akash Prajapati** - [GitHub](https://github.com/akashprajapaticse)  

---

## ⭐ **Show Your Support**
If you like this project, give it a ⭐ on GitHub!
