from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import tensorflow as tf

# -----------------------
# Flask App
# -----------------------
app = Flask(__name__, template_folder="templates", static_folder="static")

# -----------------------
# Load TFLite Model
# -----------------------
MODEL_DIR = os.path.dirname(__file__)
MODEL_PATH_TFLITE = os.path.join(MODEL_DIR, "waste_classification.tflite")

if not os.path.exists(MODEL_PATH_TFLITE):
    raise FileNotFoundError("No TensorFlow Lite model found (waste_classification.tflite)")

interpreter = tf.lite.Interpreter(model_path=MODEL_PATH_TFLITE)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Define 7 classes from your training notebook
CLASS_NAMES = ["cardboard", "compost", "glass", "metal", "paper", "plastic", "trash"]

# -----------------------
# Routes
# -----------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/classify")
def classify_page():
    return render_template("classify.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Save uploaded file temporarily
    temp_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(temp_path)

    # Preprocess image
    img = image.load_img(temp_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype(np.float32) / 255.0

    # Run inference
    interpreter.set_tensor(input_details[0]['index'], img_array)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_details[0]['index'])[0]

    class_idx = int(np.argmax(preds))
    confidence = float(np.max(preds))

    # Debug
    print("Raw predictions:", preds)

    # Delete file after prediction
    os.remove(temp_path)

    return jsonify({
        "predicted_class": CLASS_NAMES[class_idx],
        "confidence": round(confidence, 4)
    })

# -----------------------
# Run Server
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)
