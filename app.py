from flask import Flask, jsonify, render_template, request

from config import AppConfig
from services.drowsiness_detector import DrowsinessDetector


app = Flask(__name__)
app.config.from_object(AppConfig)

detector = None


def get_detector():
    """Initialize the detector lazily so import-time backend issues do not crash Flask."""
    global detector
    if detector is None:
        detector = DrowsinessDetector(app.config)
    return detector


@app.get("/")
def index():
    """Render the main dashboard."""
    return render_template("index.html", config=app.config)


@app.post("/analyze")
def analyze():
    """Analyze one webcam frame and return drowsiness metrics."""
    payload = request.get_json(silent=True) or {}
    frame_data = payload.get("frame")

    if not frame_data:
        return jsonify({"error": "Missing frame payload."}), 400

    try:
        result = get_detector().process_frame(frame_data)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except RuntimeError as exc:
        return jsonify({"error": str(exc)}), 500

    return jsonify(result)


@app.post("/reset")
def reset():
    """Reset counters when the browser stops detection."""
    if detector is not None:
        detector.reset()
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False, threaded=True)
