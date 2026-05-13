# Drowsiness Detection Web App

This mini-project streams webcam video in the browser, sends sampled frames to a Flask backend, and uses MediaPipe Face Mesh plus Eye Aspect Ratio (EAR) to detect blinks and prolonged eye closure.

## Features

- Browser webcam access with no API keys
- Flask backend API for frame analysis
- MediaPipe Face Mesh landmark detection
- EAR-based blink counting and drowsiness detection
- Browser alarm that stays active until the user is awake
- Minimal responsive UI with start/stop controls and live metrics

## Project Structure

```text
.
|-- app.py
|-- config.py
|-- requirements.txt
|-- services/
|   `-- drowsiness_detector.py
|-- static/
|   |-- css/
|   |   `-- styles.css
|   `-- js/
|       `-- app.js
`-- templates/
    `-- index.html
```

## Local Setup

```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in a browser and allow camera access.

## Tuning

Thresholds live in `config.py`:

- `EAR_THRESHOLD`: lower values make eye-closed detection less sensitive
- `CLOSED_EYES_FRAME_THRESHOLD`: number of consecutive analyzed frames before drowsy status is triggered
- `ANALYZE_INTERVAL_MS`: how often the browser sends frames to the backend

## Deployment Notes

- For production, run the Flask app with Waitress:

```powershell
waitress-serve --host=0.0.0.0 --port=5000 wsgi:app
```

- Keep HTTPS enabled in deployment so browsers allow camera access.
