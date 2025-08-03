import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'yolov5'))

from val import run as val_run

def evaluate_yolov5_model():
    weights_path = 'yolov5/runs/train/exp2/weights/best.pt'
    data_yaml = 'yolov5/data/coco128.yaml'  
    device = '0' 

    results = val_run(
        weights=weights_path,
        data=data_yaml,
        device=device,
        batch_size=16,
        verbose=True,
    )
    print(results)

if __name__ == "__main__":
    evaluate_yolov5_model()
