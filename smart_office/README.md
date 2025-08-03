# 🧠 Smart Office Object Detection with YOLOv5

This project trains a custom YOLOv5 model to detect common office objects such as `person`, `chair`, `cup`, and `phone`. It uses a merged dataset (Roboflow + COCO-style), and results are visualized through a Streamlit dashboard.

---

## 📁 Project Structure


---

## 🚀 Features

- YOLOv5s fine-tuned on custom-labeled office data
- Streamlit app for image upload and live detection
- High accuracy with fast inference
- Dataset: Roboflow + custom merged images

---

## 🗃️ Dataset Info

- 📦 Source: [Roboflow Office Object Dataset v1](https://universe.roboflow.com/jeongcj-zi66f/office-object-k7u5n/dataset/1)
- 🏷 Classes: `person`, `chair`, `cup`, `phone`
- 🖼 Format: YOLO (images + labels)
- 🧪 ~600+ images in total (train/val/test split)

---

## 🏋️‍♂️ Model Training

```bash
# 1. Install YOLOv5 dependencies

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


📊 Evaluation
python val.py \
  --weights runs/train/smart_office_combined/weights/best.pt \
  --data ../data/office_object_dataset/data.yaml \
  --img 640

✅ mAP@0.5: 89.4%

✅ mAP@0.5:0.95: 69.2%

✅ Precision: 82.3%

✅ Recall: 90.8%

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
| Classes    | 5 (keyboard, laptop, monitor, person, smartphone) |
