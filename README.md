# Classification of 3D CAD Models
<hr>

The purpose of this project is to explore methods of classification of geometries in 3D CAD model files, such as STEP or BREP formats. Unlike point-cloud or mesh data typically used in computer vision and robotics, CAD models are parametric and dimensionally accurate boundary representations, making them the foundation of engineering design and manufacturing. By investigating machine learning approaches tailored to CAD data, we aim to understand how best to represent and classify these models and to propose benchmark methodologies for future research.

## Authors
- Ross Matheny
- Usman Siddiqui
- Shemar Allen

## Dataset Overview
- **Primary Dataset:** 700 B-rep models across 7 classes  
  (Cone, Cube, Cylinder, Pipe, Rectangular Plate, Round Plate, Sphere)  
- Each model includes parametric variations (e.g., diameter, height, thickness).  
- B-rep files were converted into numerical matrices/vectors encoding curve and surface parameters.

**Additional datasets (used for comparison):**
- **TraceParts subset**  
- **Randomized synthetic dataset** (same structure as primary)

## Methods
- Direct B-rep feature extraction (surfaces, curves, parametric blocks)
- Neural network classifier (dense Keras model)
- Support Vector Machine (SVM)
- Gaussian Naive Bayes
- Fixed-length sequence preprocessing (padding, label encoding)
- Evaluation using accuracy, precision/recall/F1, confusion matrices


## Results
PERFORMANCE METRICS

Dataset                | Accuracy | Macro Precision | Macro Recall | Macro F1
-----------------------|----------|-----------------|--------------|----------
NN_models.ipynb        | 1.00     | 1.00            | 1.00         | 1.00
NN_models_randomized   | 1.00     | 1.00            | 1.00         | 1.00
NN_traceparts          | 0.95     | 0.96            | 0.96         | 0.95

COMPUTATIONAL METRICS

Dataset                | Training Time (sec) | Inference Time (sec) | Trainable Params | Total Params
-----------------------|---------------------|----------------------|------------------|--------------
NN_models.ipynb        | 0.3339              | 0.0400               | 132,103          | 396,311
NN_models_randomized   | 0.3339              | 0.0400               | 132,103          | 396,311
NN_traceparts          | 0.5233              | 0.0523               | 139,846          | 416,540

## Getting Started

1. Execute the following commands in your terminal: 
    ```
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
