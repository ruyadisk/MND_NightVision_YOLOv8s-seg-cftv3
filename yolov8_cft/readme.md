## You should edit the path of your config file and model weight to use the training/val/inf code.

Weight[[url](https://drive.google.com/file/d/1UexfSHYXq6nkm3d0ILm1GKqgJ8pPhGFB/view?usp=sharing)]  
Dataset[[url](https://drive.google.com/drive/folders/1FCTkbf6wC6T-gBGs22uvkfbtqpuJS8L9?usp=sharing)]


## Calculate Validation/Testing Set Score

### Step 1: Edit the YAML File
1. Open the YAML configuration file for your dataset.
2. To calculate the score of the test set, make the following changes:

```yaml
train: path/to/dataset/train           # Path to your training dataset
val: path/to/dataset/(val/test)        # Path to your validation/testing dataset, for example, if you want to calculate testing set, then this line should be "val: path/to/dataset/test".
nc: 6                                  # Number of classes (adjust based on your dataset)
names:
  0: person
  1: motorcycle
  2: bicycle
  3: car
  4: truck
  5: bus
```
### Step 2: Edit val-seg.py
#### 1. Open the val-seg.py script in your code editor.
#### 2. Locate the part of the script that references the model and YAML file paths.
#### 3. Replace these paths with the correct paths to your trained model and YAML file:
    Set the path to your model.
    Set the path to the modified YAML file from Step 1.

### Step 3: Run val-seg.py
