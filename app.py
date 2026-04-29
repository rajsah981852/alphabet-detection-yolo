import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Load model
model = YOLO("runs/detect/train/weights/best.pt")

st.title("Alphabet Detection System")
st.write("Upload an image and get detected text")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_array = np.array(image)

    results = model(img_array)

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

    # Remove duplicates
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

    final_text = "".join([char[1] for char in filtered])

    st.success(f"Detected Text: {final_text}")