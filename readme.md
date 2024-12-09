# Preliminary

## This repository is tested fine under following enviroment settings:

### Hardware

* #### NVIDIA GeForce RTX 3060 12G
* #### 12th Gen Intel(R) Core(TM) i7-12700

### OS Settings

* #### Ubuntu 22.04 LTS
* #### CUDA 11.7

### Virtual Enviroments Settings (conda)
* ``` pip install ultralytic ``` 

### Resource
* [Pretrained Weight](https://drive.google.com/file/d/1UexfSHYXq6nkm3d0ILm1GKqgJ8pPhGFB/view?usp=sharing)
* [Dataset](https://drive.google.com/drive/folders/1FCTkbf6wC6T-gBGs22uvkfbtqpuJS8L9?usp=sharing)

### Edit the data yaml file (MND_NightVision_YOLOv8s-seg-cftv3/ultralytics/dataset/dataset.yaml)


```yaml
train: path/to/dataset/train           # Path to your training dataset

val: path/to/dataset/(val/test)      # Path to your validation/testing dataset, for example, if you want to train/calculate on val set, then this line should be "val: path/to/dataset/test", same if test set.

nc: 6                                  # Number of classes (adjust based on your dataset)

names:
  0: person
  1: motorcycle
  2: bicycle
  3: car
  4: truck
  5: bus
```

# Train

* ## From pretrained:
  ```python train-seg.py --model <path/to/pretrained/model> --data <path/to/data/yaml>```

* ## From scratch:
  ```python train-seg.py --model <path/to/model/yaml> --data <path/to/data/yaml>```

# Validate
```python train-seg.py --model <path/to/trained/model> --data <path/to/data/yaml>```

# Inference
```python predict-seg.py --model <path/to/pretrained/model> --data <path/to/testing/data>```
