import os


class AppConfig:
    """Application defaults shared by the UI and backend detector."""

    SECRET_KEY = "dev-secret-key"
    FACE_MESH_MAX_FACES = 1
    EAR_THRESHOLD = 0.21
    CLOSED_EYES_FRAME_THRESHOLD = 8
    ANALYZE_INTERVAL_MS = 250
    MODEL_ASSET_PATH = os.path.join("models", "face_landmarker_v2.task")
