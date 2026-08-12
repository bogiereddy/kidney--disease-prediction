kidney disease prediction
# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/bogiereddy/kidney--disease-prediction.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```






## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI ="https://dagshub.com/bogiereddy/kidney--disease-prediction.mlflow"\

MLFLOW_TRACKING_USERNAME"="bogiereddy"\
MLFLOW_TRACKING_PASSWORD="dee8b528330ba44c9e45edb01be1684f171a697b"\
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/bogiereddy/kidney--disease-prediction.mlflow

export MLFLOW_TRACKING_USERNAME=bogiereddy 

export MLFLOW_TRACKING_PASSWORD=dee8b528330ba44c9e45edb01be1684f171a697b

```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app



#####
# 🩺 Kidney Disease Classification using VGG16 | MLflow | DVC | MLOps

A Deep Learning-based Kidney Disease Classification system that detects whether a CT scan image belongs to **Normal** or **Tumor** classes using **Transfer Learning (VGG16)**. The project follows an end-to-end MLOps pipeline with **DVC**, **MLflow**, and a modular Python architecture.

---

## 📌 Project Overview

This project uses a pretrained **VGG16** model with Transfer Learning to classify kidney CT scan images into:

- ✅ Normal
- ✅ Tumor

The project is designed following production-level MLOps practices including:

- Modular code architecture
- Configuration management
- Data Version Control (DVC)
- Experiment Tracking (MLflow)
- Logging
- Pipeline-based execution

---

## 🚀 Features

- End-to-End Deep Learning Pipeline
- Transfer Learning using VGG16
- Image Data Augmentation
- Model Training & Evaluation
- MLflow Experiment Tracking
- DVC Data Versioning
- Config-driven Development
- Modular Project Structure
- Logging Support

---

## 🧠 Model

- Base Model: VGG16
- Weights: ImageNet
- Include Top: False
- Custom Classification Head
- Output Classes: 2

---

## 📂 Dataset

Original Dataset contains four classes:

- Normal
- Tumor
- Cyst
- Stone

For this project only the following classes are used:

- Normal
- Tumor

The unwanted classes are automatically removed during the data ingestion stage.

---

## 🛠️ Technologies Used

### Programming

- Python 3.12

### Deep Learning

- TensorFlow
- Keras

### MLOps

- MLflow
- DVC

### Utilities

- YAML
- Logging
- pathlib
- gdown

---

## 📁 Project Structure

```
Kidney-Disease-Classification/
│
├── config/
│   └── config.yaml
│
├── artifacts/
│
├── src/
│   └── Cnnclassifier/
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       ├── utils/
│
├── params.yaml
├── main.py
├── dvc.yaml
├── requirements.txt
└── README.md
```

---

## ⚙️ Project Pipeline

### Stage 1

Data Ingestion

- Download dataset
- Extract dataset
- Remove unwanted classes

### Stage 2

Prepare Base Model

- Load pretrained VGG16
- Freeze convolution layers
- Add custom Dense layer

### Stage 3

Model Training

- Data augmentation
- Train model
- Save trained model

### Stage 4

Model Evaluation

- Evaluate model
- Save metrics
- Log experiment to MLflow

---

## 📈 MLflow

This project logs:

- Parameters
- Accuracy
- Loss
- Trained Model

Example metrics:

```
Accuracy : 95%

Loss : 0.12
```

---

## 📦 DVC

DVC is used for

- Dataset versioning
- Pipeline management
- Reproducibility

Run pipeline

```bash
dvc repro
```

---

## ▶️ Installation

Clone repository

```bash
git clone https://github.com/yourusername/Kidney-Disease-Classification.git
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

```bash
python main.py
```

---

## 📊 Model Summary

- Input Size: 224 × 224 × 3
- Base Model: VGG16
- Transfer Learning
- Flatten Layer
- Dense(2, Softmax)

---

## 📁 Configuration

Parameters are managed through

```
config/config.yaml
```

and

```
params.yaml
```

No hardcoded values are used.

---

## 📌 Future Improvements

- FastAPI Deployment
- Docker Support
- GitHub Actions CI/CD
- Kubernetes Deployment
- Model Monitoring
- Explainable AI (Grad-CAM)

---

## 👨‍💻 Author

**Bogireddy Obulreddy**

Aspiring AI & Machine Learning Engineer

Skills:

- Python
- Machine Learning
- Deep Learning
- TensorFlow
- MLOps
- MLflow
- DVC
- Git
- Docker

---

## ⭐ If you found this project useful, don't forget to give it a Star!
'''