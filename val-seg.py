from ultralytics import YOLO
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--model" ,type=str, help="path to trained model")
    parser.add_argument("--data", type=str, help="path to validation data")

    args = parser.parse_args()    

    model = YOLO(args.model)

    metrics = model.val(data=args.data) # yaml
    metrics.box.map    # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps   # a list contains map50-95 of each category
