
# 🗑️ Waste Classification using Machine Learning

This project is a **Flask web application** that classifies waste images into categories such as cardboard, compost, glass, metal, paper, plastic, and trash. It uses a **TensorFlow Lite model** for lightweight, efficient inference and is deployed on **Render**.  

🌍 **Live Demo:** [Waste Classification App](https://waste-classification-3.onrender.com)  

---

## 📌 Features
- Upload an image of waste and get a predicted category.  
- Displays prediction confidence.  
- Built with **Flask**, **TensorFlow Lite**, and **NumPy**.  
- Frontend built using **HTML, CSS, and JavaScript**.  
- Deployed on **Render** (free tier).  

---

## 📂 Dataset
We use the **[Multi-class Garbage Classification Dataset](https://www.kaggle.com/datasets/vishallazrus/multi-class-garbage-classification-dataset?utm_source=chatgpt.com)** from Kaggle.  

- The dataset contains images organized in folders by class.  
- Classes include: `cardboard`, `compost`, `glass`, `metal`, `paper`, `plastic`, and `trash`.  

---

## ⚙️ Tech Stack
- **Backend:** Flask (Python)  
- **Model:** TensorFlow Lite (pre-trained CNN model)  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Render (Python Web Service)  

---

## 🚀 Installation & Setup (Local)
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/waste-classification.git
   cd waste-classification


2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

5. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

---

## 🌐 Deployment (Render)

1. Push your project to GitHub.
2. On [Render](https://render.com/):

   * Create a new **Web Service**.
   * Connect your GitHub repo.
   * Build command:

     ```bash
     pip install -r requirements.txt
     ```
   * Start command:

     ```bash
     ./start.sh
     ```
3. Add a `runtime.txt` file to specify Python version:

   ```
   python-3.11.8
   ```

---

## 📊 Example Prediction

* Upload an image of a **plastic bottle**.
* Model predicts: **Plastic** with **0.92 confidence**.

---

## 📜 License

This project is released under the MIT License.

---

## 👩‍💻 Author

Developed by **\[Fathimath Rizwana]**.
Contributions are welcome! 🚀

```

---
<img width="1920" height="859" alt="ecosort1" src="https://github.com/user-attachments/assets/8d7e9e87-2874-4f9c-ad73-f2f0c10882d8" />
<img width="1920" height="859" alt="ecosort2" src="https://github.com/user-attachments/assets/e807e799-dbd1-448d-b333-279cb9a39502" />

```
