## You should edit the path of your config file and model weight to use the training/val/inf code.

Weight[[url](https://drive.google.com/file/d/1UexfSHYXq6nkm3d0ILm1GKqgJ8pPhGFB/view?usp=sharing)]  
Dataset[[url](https://drive.google.com/drive/folders/1FCTkbf6wC6T-gBGs22uvkfbtqpuJS8L9?usp=sharing)]


## Calculate val/testint set score:
1. Edit your yaml file, for example, if you want to calculate score of testing set:
`train: path/to/dataset/train
val: path/to/dataset/val
#val: path/to/dataset/test
nc: 6
names: 
    0: person
    1: motorcycle
    2: bicycle
    3: car
    4: truck
    5: bus
`
2. Run val-seg.py ( need to edit the file, fill the path of model and yaml )
