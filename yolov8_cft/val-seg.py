from ultralytics import YOLO

# Load a model
model = YOLO('') # model

# Validate the model
metrics = model.val(data='') # yaml
metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category
