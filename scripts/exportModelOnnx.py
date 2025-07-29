from ultralytics import YOLO
import shutil
import os

PT_MODEL_PATH = "runs/detect/TRILOGIS-BOXESv7/weights/best.pt"
ONNX_MODEL_PATH = "onnxModels/trilois_boxes.onnx"

model = YOLO(PT_MODEL_PATH)

# Export the model to ONNX format
exported_path = model.export(format="onnx", opset=9)
if os.path.exists(exported_path):
    # Remove the existing ONNX model if it exists
    if os.path.exists(ONNX_MODEL_PATH):
        os.remove(ONNX_MODEL_PATH)
    # Copy the exported ONNX model to the desired path
    shutil.copyfile(exported_path, ONNX_MODEL_PATH)
    # Remove the temporary exported file
    os.remove(exported_path)