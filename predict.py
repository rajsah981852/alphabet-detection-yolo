import os
from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Path to test images folder
image_folder = "test_images"

# Loop through all images
for image_name in os.listdir(image_folder):

    image_path = os.path.join(image_folder, image_name)

    # Run prediction
    results = model(image_path, conf=0.25, iou=0.5)

    characters = []

    for r in results:
        boxes = r.boxes

        if boxes is None:
            continue

        for box in boxes:
            conf = float(box.conf[0])

            if conf < 0.25:
                continue

            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            x1 = box.xyxy[0][0].item()

            characters.append((x1, label, conf))

    # Sort left → right
    characters = sorted(characters, key=lambda x: x[0])

    # ✅ FIXED: inside loop
    filtered = []

    for char in characters:
        if not filtered:
            filtered.append(char)
            continue

        prev = filtered[-1]

        if abs(char[0] - prev[0]) < 15:
            if char[2] > prev[2]:
                filtered[-1] = char
        else:
            filtered.append(char)

    # Final text
    final_text = "".join([char[1] for char in filtered])

    # ✅ print per image
    print(f"{image_name} → {final_text}")