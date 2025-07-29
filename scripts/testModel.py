from ultralytics import YOLO

TEST_PATH = "sampleImages"
MODEL_PATH = 'runs/detect/TRILOGIS-BOXESv8/weights/best.pt'

model = YOLO(MODEL_PATH)

results = model.predict(source=TEST_PATH, imgsz=640, conf=0.60, save=True)