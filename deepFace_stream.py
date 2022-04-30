from deepface import DeepFace
# Options for model_name and detector_backend:
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']

# Source of the input stream, webcam is 0
source=0

DeepFace.stream(db_path = "database", model_name="Facenet", detector_backend="opencv", source= source)