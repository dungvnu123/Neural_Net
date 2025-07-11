# Virtual Keyboard with Hand Tracking

A **computer‑vision–based virtual keyboard** that lets you type in mid‑air using nothing but your webcam and your hand. It leverages **OpenCV**, **cvzone** (MediaPipe under the hood), and **pynput** to convert hand gestures into real keypresses on your computer.

https://user-images.githubusercontent.com/…/demo.gif <!-- Replace with your own GIF or screenshot -->

---

## Features

- **Real‑time hand tracking** (single‑hand) with fingertip landmark detection.  
- **On‑screen QWERTY keyboard** rendered with corner accents and translucent overlay.  
- **Pinch‑to‑press** interaction: bring your **index (8) & middle (12)** fingertips within 40 px to "click" the hovered key.  
- Sends **actual keypress events** via `pynput.Controller`, so it works in any application.  
- Built‑in **Backspace** (`<`) support, live text area, and *press “q”* to quit.  
- Fully **customisable layout & colours** – just edit the `keys` list or button styling.

## Prerequisites

| Package | Tested Version |
|---------|---------------|
| Python  | ≥ 3.8         |
| opencv‑python | 4.10.* |
| cvzone  | 1.6.1         |
| numpy   | 1.26.*        |
| pynput  | 1.7.*         |

> **Tip:** `cvzone` automatically installs `mediapipe`, which performs the hand‑landmark detection.

## Installation

```bash
# 1. Clone the repo
$ git clone https://github.com/your‑username/virtual‑keyboard.git
$ cd virtual‑keyboard

# 2. (Optional) Create and activate a virtual environment
$ python -m venv venv
$ source venv/bin/activate         # Windows: venv\Scripts\activate

# 3. Install dependencies
$ pip install -r requirements.txt
```

`requirements.txt` (for convenience):
```txt
opencv‑python
cvzone
numpy
pynput
```

## Usage

```bash
python virtual_keyboard.py
```

1. Ensure **only one hand** is visible to the webcam.  
2. Hover your **index fingertip** over a key – it lights up purple.  
3. **Pinch** index & middle fingers together to register the keystroke (key turns green).  
4. Press **q** on your physical keyboard (or close the window) to exit.

### Keyboard Layout

The layout is controlled by the nested `keys` list:
```python
keys = [
    ["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L",";"],
    ["Z","X","C","V","B","N","M",",",".","/","<"]
]
```
Change or localise it (e.g. Vietnamese VNI/TELEX) as you like. Buttons are auto‑generated with a fixed size of **70 × 70 px**.

## How It Works

1. **Frame capture** from OpenCV webcam.  
2. `cvzone.HandDetector` returns 21 hand landmarks.  
3. The **index fingertip (id 8)** coordinates determine hover state over a button.  
4. Distance between id 8 & id 12 (< 40 px) triggers a click.  
5. `pynput.keyboard.Controller` sends the character to the OS.  
6. The pressed key is appended to `finalText` and drawn on a grey text bar.

![diagram](docs/flowchart.svg) <!-- Optional architecture diagram -->

## Troubleshooting / FAQ

| Symptom | Possible Fix |
|---------|-------------|
| *Camera feed black* | Another app is using the webcam; close it or change `cap = cv2.VideoCapture(1)` |
| *Lag / low FPS* | Lower the **frame size** or raise the **detectionCon** threshold |
| *Inaccurate clicks* | Adjust the **distance threshold** in the `l < 40` condition |

## Roadmap

- [ ] Multihand support & two‑hand chords  
- [ ] **Shift / Caps Lock** modifier  
- [ ] Auto‑calibration of click distance based on hand size  
- [ ] Dark/light theme toggle  
- [ ] Export typed text to `.txt`

## Contributing

Pull requests are welcome! Feel free to open issues for bug reports or feature ideas.

## License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

## Acknowledgements

- [cvzone](https://github.com/cvzone/cvzone) by **Murtaza Hassan**  
- [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) by Google  
- [pynput](https://github.com/moses-palmer/pynput) for cross‑platform keyboard control  
- Inspired by various YouTube tutorials on "AI Virtual Keyboard".

---

> ❤ *Happy flying‑keyboard typing!*
