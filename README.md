# YOLO MODEL TRAINING PROJECT
This project was made to fine-tune a YOLOv8n model with a custom dataset

## FOLDERS
- `DatasetRoboflow` contains the dataset downloaded from [roboflow](https://universe.roboflow.com/myworkspace-fgx5u/trilogis-boxes)
- `onnxModels` will contain the exported onnx model
- `runs` is a folder created by ultralytics whenever a train session ends, containing the model and some data of the training session, and the prediction results
- `sampleImages` is a folder containing some images that are used to test the models
- `scripts` contains all the scripts

## SCRIPTS
- `exportModelOnnx.py` exports the model to .onnx format, to then be imported into the unity project
- `testModel.py` executes a test session, using the selected model to predict the image inside the `sampleImages` folder
- `trainModel.py` starts a training session, you can select the base model,the path where the dataset is located, the number of epochs to train your model for and the workers used for the training session (only for GPU usage, 3 is the max value before the program to stop. For CPU usage remove workers from the parameters)

## REQUIREMENTS
These scripts all use `python 3.10.0`, you can download it [here](https://www.python.org/downloads/release/python-3100/).

You can quickly install the requirements using this command
>  **⚠️ WARNING**<br>
The training script uses the GPU device, in order to have it working you have to install NVIDIA CUDA 12.8 [here](https://developer.nvidia.com/cuda-12-8-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local)<br>
Otherwise you can run the command for CPU usage and in the `training.py` script change the `device` value from <span style="color:#E88B43">"gpu"</span> to <span style="color:#E88B43">"cpu"</span> and remove the `workers` parameter
>
### GPU INSTALL
```bash
pip install -r requirements.txt
```
### CPU INSTALL
```bash
pip install -r requirementsCPU.txt
```
---
### Here's the list of the GPU requirements
- `ultralytics`: 8.3.168  
- `torch`: 2.7.1+cu128  
- `torchvision`: 0.22.1+cu128  
- `torchaudio`: 2.7.1+cu128  
- `opencv-python`: 4.12.0.88  
- `PyYAML`: 6.0.2  
- `numpy`: 2.2.6  
- `tqdm`: 4.67.1  
- `requests`: 2.32.4  

### Here's the list of the CPU requirements
- `ultralytics`: 8.3.168  
- `torch`: 2.7.1
- `torchvision`: 0.22.1
- `torchaudio`: 2.7.1
- `opencv-python`: 4.12.0.88  
- `PyYAML`: 6.0.2  
- `numpy`: 2.2.6  
- `tqdm`: 4.67.1  
- `requests`: 2.32.4  