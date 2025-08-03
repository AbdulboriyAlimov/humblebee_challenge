# 🧠 Smart Office Object Detection with YOLOv5

This project trains a custom YOLOv5 model to detect common office objects such as keyboard, laptop, monitor, person and smartphone. It uses a merged dataset (Roboflow + COCO-style), and results are visualized through a Streamlit dashboard.

---

## 🚀 Features

- YOLOv5s fine-tuned on custom-labeled office data
- Streamlit app for image upload and live detection
- High accuracy with fast inference
- Dataset: Roboflow + custom merged images

---

## 🗃️ Dataset Info

This project uses the COCO128 dataset for training and validation. It is a small subset of the COCO dataset commonly used for quick experiments and model prototyping.

COCO128 YAML file used: data/coco128.yaml

It includes 128 training and validation images with 80 common object classes.

There is no need to download this dataset just write the command below and it will be downloaded automatically

python train.py --data coco128.yaml --weights yolov5s.pt --epochs 100 --batch-size 16
---

## 🏋️‍♂️ Model Training

```bash
# 1. Clone YOLOv5 and install dependencies
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

# 2. Train
python train.py \
  --img 640 \
  --batch 16 \
  --epochs 99 \
  --data ../data/merged/data.yaml \
  --weights yolov5s.pt \
  --name smart_office_combined

✅ Best model saved: runs/train/smart_office_combined/weights/best.pt

Current best model is saved in best_model folder


📊 Evaluation
python val.py \
  --weights runs/train/smart_office_combined/weights/best.pt \
  --data ../data/office_object_dataset/data.yaml \
  --img 640

✅ mAP@0.5: 90.4%

✅ mAP@0.5:0.95: 68.2%

✅ Precision: 90.7%

✅ Recall: 83.1%

📷 Streamlit App
# Run Streamlit dashboard
streamlit run streamlit_app.py

Upload image

See bounding boxes and confidence

Model auto-loads best.pt

🧠 Technical Summary

| Setting    | Value                         |
| ---------- | ----------------------------- |
| Model      | YOLOv5s (pretrained)          |
| Epochs     | 99                            |
| Batch size | 16                            |
| GPU Used   | RTX 3090                      |
