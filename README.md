
# 🧠🎮 DSA Hand Gesture Game Hub

Welcome to **DSA Hand Gesture Game Hub**, an interactive collection of AI + DSA–powered mini-games that you can play **with your hand gestures** or your mouse.
This project combines **Computer Vision**, **Flask Web Interface**, and **Data Structures & Algorithms (DSA)** concepts into a fun and educational experience.

---

## 🚀 Features

* 🖐️ **Play with Hand Gestures** (via webcam using MediaPipe + OpenCV)
* 🧩 **Multiple DSA-based Mini Games**

  * 🪨✋✂️ Rock-Paper-Scissors *(Decision Tree logic)*
  * 🧠 Memory Graph (DFS)
  * 🔢 Sorting Challenge (QuickSort)
  * 🎯 Path Finder (BFS)
  * 🟦 Sudoku Solver (Backtracking)
* 🌐 **Web Interface** (Flask + HTML)
* ✨ **Modern Neon-Themed UI**
* 📊 **Time & Space Complexities** included in comments inside the code

---

## 🧰 Tech Stack

| Component       | Technology                                        |
| --------------- | ------------------------------------------------- |
| Language        | Python 3.x                                        |
| Framework       | Flask                                             |
| Computer Vision | OpenCV, MediaPipe                                 |
| Algorithms      | DFS, BFS, QuickSort, Backtracking, Decision Trees |
| Frontend        | HTML5, CSS3, JavaScript                           |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download the Repository

```bash
git clone https://github.com/yourusername/DSA-Hand-Gesture-GameHub.git
cd DSA-Hand-Gesture-GameHub
```

### 2️⃣ Install Required Libraries

```bash
pip install flask opencv-python mediapipe numpy
```

### 3️⃣ Project Structure

```
📁 DSA-Hand-Gesture-GameHub/
│
├── game_hub.py              # Main Python backend
├── templates/
│   └── index.html           # Web interface
└── README.md
```

### 4️⃣ Run the App

```bash
python game_hub.py
```

Then open your browser at:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🖐️ Hand Gesture Controls

| Gesture     | Hand Shape         | Game Action |
| ----------- | ------------------ | ----------- |
| ✊ Rock      | All fingers closed | Rock        |
| ✋ Paper     | All fingers open   | Paper       |
| ✌️ Scissors | Two fingers open   | Scissors    |

> Keep your hand steady for 2–3 seconds in front of the webcam for accurate recognition.

---

## 🧮 Algorithms & DSA Concepts Used

| Game                | Algorithm / Concept      | Time Complexity | Space Complexity |
| ------------------- | ------------------------ | --------------- | ---------------- |
| Rock-Paper-Scissors | Decision Tree            | O(1)            | O(1)             |
| Memory Graph        | DFS (Depth-First Search) | O(V+E)          | O(V)             |
| Sorting Challenge   | QuickSort                | O(n log n)      | O(log n)         |
| Path Finder         | BFS (Shortest Path)      | O(V+E)          | O(V)             |
| Sudoku Solver       | Backtracking             | O(9^(n²))       | O(n²)            |

---

## 🎨 UI Features

* Modern gradient background (blue–purple)
* Animated hover buttons
* Live gesture feedback (“Gesture: Rock / Paper / Scissors”)
* Clear game instructions
* Responsive layout

---

## 🧠 Educational Value

This project demonstrates how **core DSA algorithms** can be implemented in an **interactive, real-world AI environment**, helping you:

* Understand algorithm performance
* Integrate DSA with computer vision
* Learn how backend and frontend communicate using Flask + JSON

---

## 🔍 Troubleshooting

* If the webcam feed doesn’t open → check camera permissions.
* If gesture detection is unstable → ensure good lighting and background contrast.
* Press **Q** on the OpenCV window to stop the camera safely.
* Restart Flask after code changes.

---

## 🪴 Future Enhancements

* Add Leaderboard using file or database storage
* Add gesture-controlled menus for all 5 DSA games
* Integrate voice feedback (“You Win”, “Draw”, etc.)
* Include real-time performance graphs for algorithms

---

## 📝 Author

👨‍💻 **Pranav Machireddy**
📧 *Developed for academic demonstration of AI + DSA integration.*

---

## 🪪 License

This project is released under the **MIT License** — feel free to modify and share with proper credit.
