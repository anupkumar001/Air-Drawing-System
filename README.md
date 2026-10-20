# 🚀 Movie-Style Air UI — Gesture-Controlled Desktop Launcher

Control desktop applications using hand gestures and your webcam! This project uses Python, OpenCV, and MediaPipe Hands to track your fingers, highlight on-screen application cards, and launch applications with a pinch gesture.

> **Project Status:** Beginner prototype. The interface appears inside an OpenCV camera window. It is a simulated futuristic interface, not a real hologram.

## ✨ Features

- 🖐️ Real-time hand tracking using MediaPipe
- 🟩 Highlights application cards when pointing at them
- 🤏 Uses a pinch gesture to trigger an application
- 📝 Opens Notepad on Windows
- 🧮 Opens Calculator on Windows
- 📁 Opens File Explorer on Windows
- ⌨️ Press `Esc` to exit the application

## 🧰 Tech Stack

- Python 3.11
- OpenCV
- MediaPipe Hands
- NumPy

## 📁 Project Structure

```text
Movie-Style-Air-UI/
├── air_ui.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Install Python

Install Python 3.11 and ensure Python is available on your system.

### 2. Clone the Repository

```bash
git clone https://github.com/anupkumar001/Air-Drawing-System.git
cd Air-Drawing-System
```

### 3. Install Dependencies

```bash
py -3.11 -m pip install -r requirements.txt
```

### 4. Run the Project

```bash
py -3.11 air_ui.py
```

Allow camera access if prompted and ensure your hand is clearly visible.

## 🖐️ How to Use

1. Run the Python script.
2. Show one hand to your webcam.
3. Move your index fingertip over one of the application cards.
4. Bring your thumb and index finger close together to perform a pinch gesture.
5. The selected application should open.
6. Press `Esc` to close the camera window.

## 🖥️ Default Application Cards

| Card | Application |
|---|---|
| FILE 1 | Notepad |
| FILE 2 | Calculator |
| FILE 3 | File Explorer |

## ⚠️ Notes

- This project is designed to run locally on a computer with Python installed.
- GitHub Pages cannot directly run this Python webcam application.
- A working webcam and compatible Python packages are required.
- The current code uses fixed coordinates for application cards.
- The application-launching command may need adjustment for your operating system.

## 🔮 Future Improvements

- Futuristic neon interface and visual effects
- Custom application cards
- Improved gesture recognition
- Drag-and-drop interaction using hand gestures
- Better layout scaling and error handling

## 👨‍💻 Author

**Anup Kumar**

Suggestions and feedback are welcome!

---
⭐ If you find this project interesting, consider giving the repository a star.
