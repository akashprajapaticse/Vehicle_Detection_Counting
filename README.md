### **README.md** for Vehicle Detection and Counting

```markdown
# 🚗 Vehicle Detection and Counting System

This project is a **Vehicle Detection and Counting System** using **YOLO v11** in a Node.js-based web application. The system detects and counts vehicles from a live camera feed or video input, providing real-time results.

---

## 📌 **Features**
✅ Real-time vehicle detection using YOLO v11  
✅ Vehicle counting and classification  
✅ Supports live video feeds and video files  
✅ Web-based interface using Node.js  
✅ Performance-optimized using TensorFlow and OpenCV  

---

## 🛠️ **Tech Stack**
- **Backend:** Node.js, Express.js  
- **Machine Learning:** YOLO v11 (ONNX model)  
- **Frontend:** HTML, CSS, JavaScript  
- **Libraries:** TensorFlow.js, OpenCV.js, Socket.io  

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
├── server.js              # Node.js server
├── package.json           # Dependencies
└── README.md              # Project documentation
```

---

## 🚀 **Setup and Installation**
1. **Clone the repository**:
```bash
git clone https://github.com/akashprajapaticse/vehicle-detection-counting.git
```

2. **Navigate to the project folder**:
```bash
cd vehicle-detection-counting
```

3. **Install dependencies**:
```bash
npm install
```

4. **Start the server**:
```bash
node server.js
```

5. **Access the app**:  
Open your browser and visit:
```
http://localhost:3001
```

---

## 🎯 **How It Works**
1. Load the YOLO model using TensorFlow.js  
2. Capture live feed using `getUserMedia()`  
3. Preprocess the video frames  
4. Run YOLO object detection model  
5. Count and display vehicle types in real-time  
6. Display statistics and FPS  

---

## ⚠️ **Troubleshooting**
❗ **ONNX Model Error**:  
If the model fails to load, verify the path in `server.js`:
```javascript
const modelPath = './models/yolov11.onnx';
```

❗ **Permission Error**:  
Allow camera and microphone access in browser settings.

---

## 📜 **License**
This project is licensed under the MIT License.

---

## 🙌 **Contributors**
👤 **Akash Prajapati** - [GitHub](https://github.com/akashprajapaticse)  

---

## ⭐ **Show Your Support**
If you like this project, give it a ⭐ on GitHub!
```

---

Let me know if you want to modify or add anything! 😎
