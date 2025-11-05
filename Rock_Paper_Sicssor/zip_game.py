from flask import Flask, render_template, jsonify
import threading, cv2, mediapipe as mp, numpy as np, random, time

app = Flask(__name__)

gesture_data = {"gesture": "None"}
running = True

# ---------------- HAND GESTURE DETECTION ----------------
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

def count_fingers(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []
    if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)
    for id in range(1, 5):
        if hand_landmarks.landmark[tips[id]].y < hand_landmarks.landmark[tips[id]-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers.count(1)

def gesture_loop():
    global running, gesture_data
    cap = cv2.VideoCapture(0)
    prev_gesture = "None"
    stable_count = 0
    while running:
        success, frame = cap.read()
        if not success:
            continue
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)
        h, w, _ = frame.shape

        gesture = "None"
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
                count = count_fingers(handLms)
                if count == 0:
                    gesture = "Rock"
                elif count == 5:
                    gesture = "Paper"
                elif count == 2:
                    gesture = "Scissors"
                else:
                    gesture = "Unknown"

        if gesture == prev_gesture:
            stable_count += 1
        else:
            stable_count = 0
        prev_gesture = gesture
        if stable_count > 3:
            gesture_data["gesture"] = gesture

        cv2.putText(frame, f"Gesture: {gesture_data['gesture']}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("Hand Gesture Tracker (Press Q to quit)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

t = threading.Thread(target=gesture_loop, daemon=True)
t.start()

# ---------------- GAME LOGIC ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gesture")
def get_gesture():
    return jsonify(gesture_data)

@app.route("/rps")
def rock_paper_scissors():
    gestures = ["Rock", "Paper", "Scissors"]
    comp = random.choice(gestures)
    user = gesture_data["gesture"]
    result = "Waiting for valid gesture..."
    if user in gestures:
        if user == comp:
            result = "Draw!"
        elif (user == "Rock" and comp == "Scissors") or \
             (user == "Paper" and comp == "Rock") or \
             (user == "Scissors" and comp == "Paper"):
            result = "You Win!"
        else:
            result = "Computer Wins!"
    return jsonify({"you": user, "computer": comp, "result": result})

if __name__ == "__main__":
    try:
        app.run(debug=False, host="0.0.0.0", port=5000)
    finally:
        running = False
        t.join()
