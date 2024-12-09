# yolo-based-object-detection-azure-pipeline

This project provides an advanced YOLO (You Only Look Once) based object detection pipeline. It uses the YOLOv5 model to perform object detection on images. The project exposes a REST API (using FastAPI) for inference, includes training scripts to fine-tune the model, and has guidelines for deploying to Azure. It also demonstrates object-oriented principles, design patterns, and a modular architecture.

## Features

- **YOLOv5 Object Detection**: Pretrained model for quick inference and capability to fine-tune with custom data.
- **REST API Endpoints**: Easy inference using FastAPI endpoints.
- **Azure Deployment**: Instructions and service utilities for deploying to Azure Web Apps or Azure Container Instances.
- **Training Service**: Train/fine-tune the YOLO model on custom datasets.
- **Modular and Scalable Codebase**: OOP principles, design patterns, and clean architecture.
- **Logging and Configuration**: Centralized configuration management and logging utilities.

## Technologies and Concepts Used

- **Python 3.11.3**
- **YOLOv5 (ultralytics)** for object detection
- **PyTorch** for deep learning
- **FastAPI** for REST API
- **Uvicorn** for ASGI server
- **Pydantic** for configuration management
- **Azure CLI and Azure SDK** (for deployment)
- **Object-Oriented Design**: Base classes, abstract classes, and concrete implementations.
- **Design Patterns**: Strategy pattern for handling different detectors.
- **Logging and Utilities**: Well-structured logging and utility functions.

## Directory Structure

```bash
yolo-based-object-detection-azure-pipeline/
├─ README.md
├─ requirements.txt
├─ .env
├─ src/
│  ├─ main.py
│  ├─ config.py
│  ├─ detectors/
│  │   ├─ base_detector.py
│  │   ├─ yolo_detector.py
│  │
│  ├─ services/
│  │   ├─ inference_service.py
│  │   ├─ training_service.py
│  │   ├─ azure_deployment_service.py
│  │
│  ├─ utils/
│  │   ├─ image_utils.py
│  │   ├─ logging_utils.py
│  │
│  ├─ models/
│  │   └─ yolo/
│  │       └─ yolov5s.pt   # Pretrained YOLOv5s model weights (downloaded)
│  │
│  ├─ tests/
│  │   ├─ test_inference.py
│  │
│  └─ data/
│      ├─ samples/
│      │   ├─ sample_image.jpg  # Sample image for testing inference
│      ├─ training_data/
│      │   ├─ images/           # training images
│      │   ├─ labels/           # YOLO format labels
│      │   └─ dataset.yaml      # YOLO dataset configuration file for training
│
└─ .env
```

## Testing the Application

- **Installation of Libraries**:

```bash
pip install -r requirements.txt
```

**Creation of YOLO labels**:

- Use https://annotate.pixlab.io/ to create annotation .json file for the input image file.
- Run src/data/training_data/labels/convert_json_to_yolo/convert_json_to_yolo.py code for converting .json to YOLO format .txt file.

**Training Directory Checklist**:

```bash
training_data/
   ├─ images/
   │    ├─ train/
   │    │    ├─ img1.jpg
   │    │    ├─ img2.jpg
   │    ├─ val/
   │         ├─ img3.jpg
   │
   ├─ labels/
   │    ├─ train/
   │    │    ├─ img1.txt
   │    │    ├─ img2.txt
   │    ├─ val/
   │         ├─ img3.txt
   │
   └─ dataset.yaml
```

**Verify Labels**:

```bash
labels/
   ├─ train/
   │    ├─ img1.txt
   │    ├─ img2.txt
   │    └─ ...
   ├─ val/
   │    ├─ img3.txt
   │    └─ ...
```

The .txt file will contain lines in the YOLO format:

```bash
<class_id> <x_center> <y_center> <width> <height>
```

**Training the YOLO Model**:

```bash
python -m src.services.training_service
```

**Test the Training**:

Once training is complete, evaluate the results:

- Check the runs/train/exp/ folder for metrics and trained weights.
- Use the trained model to test predictions: Replace config.MODEL_PATH in the code with the new weights file:

```bash
runs\detect\train5\weights\best.pt
```

Now, you’ve successfully generated labels for your dataset, trained the YOLO model, and can test it with new images!

## Running the Application Locally

- **Run the Application**:

```bash
uvicorn src.main:app --host 127.0.0.1 --port 8000
```

This will start the FastAPI application on http://127.0.0.1:8000

**Test Inference Endpoint**:

Send a POST request with an image file to the /infer endpoint.

```bash
curl -X POST "http://127.0.0.1:8000/infer" -F "file=@src/data/samples/sample_image.jpg"
```

You should see a JSON response with detected objects.

**Run Unit Tests**:

```bash
pytest src/tests/
```

**Further Training (Fine-Tuning)**:

To train or fine-tune the model on your custom dataset:
- Place your dataset images and labels in src/data/training_data/.
- Update dataset.yaml with paths to your images and labels.
- Run the training script:

```bash
python src/services/training_service.py
```

This will load the YOLO model, update it with your data, and produce new weights in src/models/yolo/runs/train/exp/weights/best.pt.

**Deploying to Azure**:

- **Build a Docker image**:

```bash
docker build -t myregistry.azurecr.io/yolo-app:latest .
docker push myregistry.azurecr.io/yolo-app:latest
```

- **Azure Web App Deployment**:

```bash
az login
az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name myyolowebapp --deployment-container-image-name myregistry.azurecr.io/yolo-app:latest
```

- **Configure Environment Variables in Azure**:

```bash
az webapp config appsettings set --resource-group myResourceGroup --name myyolowebapp --settings MODEL_PATH="src/models/yolo/yolov5s.pt"
```

- **Access web app**:

Open https://myyolowebapp.azurewebsites.net/docs in your browser for the API docs.

## License

*This project is licensed under the MIT License.*
