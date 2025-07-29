from ultralytics import YOLO

MODEL_PATH = "yolov8n.pt" 
DATA_PATH =  "DatasetRoboflow/data.yaml"
NUM_EPOCHS = 40
NUM_WORKERS = 3

if __name__ == "__main__":
    # Load the model
    model = YOLO(MODEL_PATH)

    # Train
    model.train(data=DATA_PATH, epochs=NUM_EPOCHS, imgsz=640, batch=16, name="TRILOGIS-BOXESv", device="gpu", workers=NUM_WORKERS) # Remove workers for CPU usage