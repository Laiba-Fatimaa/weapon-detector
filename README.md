# Gun Detection Security Feed

A simple real-time security camera prototype that watches a webcam feed and flags when a firearm-like object is detected. It uses OpenCV with a custom-trained **Haar cascade classifier** (`cascade.xml`) to scan each frame, draws a box around detections, and stops with an alert when one is found.

> **Note:** This is an educational computer-vision prototype. Haar cascades are a lightweight, older technique and can produce false positives and false negatives. It should **not** be relied on as a real safety or security system.

## Features

- Live webcam feed in a window titled "Security Feed"
- Haar cascade detection on grayscale frames
- Blue bounding box drawn around each detection
- Live date and time stamp overlaid on the video
- Prints `Guns detected` to the console and shows the detection frame when something is found
- Clear error messages if the cascade file or webcam can't be loaded
- Press `q` to quit at any time

## How It Works

1. The script loads `cascade.xml` and opens the webcam, exiting with a clear error if either fails.
2. Each frame is resized to 500 px wide for speed and converted to grayscale.
3. `detectMultiScale()` scans the frame with these settings:

   | Parameter | Value | Meaning |
   |-----------|-------|---------|
   | `scaleFactor` | `1.3` | How much the image is shrunk at each scan level (higher = faster, less accurate) |
   | `minNeighbors` | `20` | Overlapping hits needed to confirm a detection (higher = fewer false positives) |
   | `minSize` | `(100, 100)` | Ignores anything smaller than 100×100 pixels |

4. Detections get a blue rectangle, and a timestamp is drawn at the bottom-left of the frame.
5. On the first detection, the script prints `Guns detected`, releases the camera, and displays the detection frame with matplotlib. Otherwise the frame is shown live in the "Security Feed" window.

## Requirements

- Python 3.8+
- A working webcam
- A trained Haar cascade file named `cascade.xml` in the same folder as the script
- Python packages:
  - `opencv-python`
  - `imutils`
  - `matplotlib`

## Installation

```bash
git clone https://github.com/Laiba-Fatimaa/weapon-detector.git
cd weapon-detector

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install opencv-python imutils matplotlib
```

Make sure `cascade.xml` is in the project folder.

## Usage

```bash
python gun_detection.py
```

- A "Security Feed" window opens showing the live camera view.
- When a detection occurs, `Guns detected` is printed in the terminal and a window opens showing the frame with the detection box.
- Press `q` in the feed window to quit manually.

## Configuration

| Setting | Where | Default | Effect |
|---------|-------|---------|--------|
| Camera index | `cv2.VideoCapture(0)` | `0` | Use `1`, `2`, etc. for another camera |
| Frame width | `imutils.resize(frame, width=500)` | `500` | Smaller = faster, larger = more detail |
| `scaleFactor` | `detectMultiScale` | `1.3` | Lower (e.g. `1.1`) is more thorough but slower |
| `minNeighbors` | `detectMultiScale` | `20` | Raise to cut false alarms, lower to catch more |
| `minSize` | `detectMultiScale` | `(100, 100)` | Smallest object size to detect |

To keep monitoring after a detection instead of stopping, remove the `break` inside the `if len(guns) > 0:` block.

## Troubleshooting

**`FileNotFoundError: Could not load 'cascade.xml'`**
The cascade file is missing or in the wrong folder. Place it next to the script, or use its full path.

**`RuntimeError: Could not open the webcam`**
Close other apps using the camera, or try `cv2.VideoCapture(1)`.

**Too many false detections**
Increase `minNeighbors` or `minSize`, and use good, even lighting.

**Missing detections**
Lower `minNeighbors` or `scaleFactor`, or retrain the cascade with more varied images.

## Limitations

- Accuracy depends heavily on the training data, lighting, angle, and background.
- Haar cascades may mistake other objects for a firearm.
- The script stops at the first detection by default.

## Ideas for Future Improvements

- Replace the Haar cascade with a modern detector such as YOLO for better accuracy
- Save a snapshot and timestamp of each detection to disk
- Send an alert (email, SMS, or push notification) on detection
- Keep monitoring after a detection instead of exiting
- Add a confidence threshold and detection log

## Tech Stack

- [OpenCV](https://opencv.org/): video capture, Haar cascade detection, drawing
- [imutils](https://github.com/PyImageSearch/imutils): frame resizing helper
- [Matplotlib](https://matplotlib.org/): displaying the detection frame

## License

Add your license of choice here (for example, MIT).
