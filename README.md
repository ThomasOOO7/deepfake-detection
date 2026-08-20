# 🕵️ DeepFake Detection System

An AI-powered web application that detects whether an uploaded **image or video is REAL or FAKE** using a deepfake detection model exposed through an API.

> 🔍 Upload → 🤖 Analyze → 📊 Get Detection Result

---

## 🌟 Overview

With the rapid growth of generative AI, manipulated images and videos have become increasingly difficult to distinguish from authentic media.

**DeepFake Detection System** provides a simple web-based platform where users can upload images or videos and receive an AI-generated prediction indicating whether the media is likely to be **real or manipulated**.

The application separates the **web interface** from the **AI detection model**, allowing the model to be independently developed, updated, or deployed.

---

## ✨ Features

* 📷 Image deepfake detection
* 🎥 Video deepfake detection
* 🤖 AI/ML-based classification
* 🔌 REST API model integration
* 📊 Prediction and confidence score
* ⚡ Simple and responsive interface
* 🔒 File type and upload validation
* 🧩 Modular architecture
* 🚀 Easy local deployment
* 🔄 Extendable for future detection models

---

## 🖥️ Demo

### Home Page
<img width="817" height="558" alt="image" src="https://github.com/user-attachments/assets/98dcbb17-fced-4ee3-a952-35535ade1cf3" />



### Detection Result
<img width="705" height="562" alt="image" src="https://github.com/user-attachments/assets/7461ad77-208b-4b86-bcff-d5baffbead4d" />

<img width="608" height="550" alt="image" src="https://github.com/user-attachments/assets/3c3e7def-4a9b-4dca-b4fe-b6d1ead0bb4e" />


---

## 🏗️ Architecture

```text
<img width="791" height="439" alt="image" src="https://github.com/user-attachments/assets/c6de68f2-d600-4b44-b43f-e70a95b2a63e" />

<img width="998" height="600" alt="image" src="https://github.com/user-attachments/assets/dc75dc5f-c1f3-4840-8968-f8ff44884aab" />

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript


### Backend

* Python
* Flask
* REST API
* Requests

### Machine Learning

* PyTorch
* Hugging Face Transformers
* OpenCV
* NumPy
* Pillow

> The exact ML libraries depend on the model being integrated.

---

## 📂 Project Structure

```text
deepfake-detection/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── uploads/
│
├── model_api/
│   ├── api.py
│   └── model.py
│
└── docs/
    └── screenshots/
```

---

## ⚙️ How It Works

### Image Detection

```text
Image
  ↓
Upload
  ↓
Backend
  ↓
Detection API
  ↓
Image Preprocessing
  ↓
AI Model
  ↓
Prediction
  ↓
REAL / FAKE
```

### Video Detection

```text
Video
  ↓
Upload
  ↓
Backend
  ↓
Frame Extraction
  ↓
Face Detection
  ↓
Frame Analysis
  ↓
AI Model
  ↓
Prediction Aggregation
  ↓
REAL / FAKE
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/ThomasOOO7/deepfake-detection.git
```

```bash
cd deepfake-detection
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---



## 4. Start the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🔌 API

The detection model can expose an endpoint such as:

```http
POST /api/detect
```

### Request

```text
multipart/form-data
```

with:

```text
file = image/video
```

### Example Response

```json
{
  "prediction": "FAKE",
  "confidence": 0.94
}
```

Possible predictions:

```text
REAL
FAKE
```

---

# 📊 Detection Result

The interface can display:

```text
┌──────────────────────────────┐
│      Detection Result        │
├──────────────────────────────┤
│                              │
│        ⚠️ FAKE               │
│                              │
│     Confidence: 94%          │
│                              │
└──────────────────────────────┘
```

The confidence score represents the model's confidence in its prediction and should not be interpreted as absolute proof of authenticity.

---

# 🧠 Model

The website is model-agnostic. The detection model can be replaced without significantly changing the frontend.

Possible architecture:

```text
Uploaded Media
      ↓
Preprocessing
      ↓
Feature Extraction
      ↓
DeepFake Detection Model
      ↓
Classification
      ↓
Prediction + Confidence
```

Depending on the implementation, the system may use technologies such as:

* Vision Transformers
* CNN-based models
* Transformer-based architectures
* OpenCV
* Face detection
* Frame-level analysis

---

# 🔐 Security

For production deployment, the following protections should be implemented:

* Validate uploaded file types
* Restrict maximum file size
* Generate unique filenames
* Never execute uploaded files
* Store temporary uploads securely
* Delete files after processing
* Protect API endpoints
* Add request rate limiting
* Disable Flask debug mode in production
* Keep API credentials in environment variables

---

# 🧪 Testing

The system should be evaluated using both authentic and manipulated media.

### Real Media

* Original photographs
* Original videos
* Different resolutions
* Different lighting conditions
* Different face orientations

### Fake Media

* Face-swapped images
* Face-swapped videos
* AI-generated faces
* Re-encoded manipulated videos
* Different compression levels

---

# 📈 Future Improvements

* [ ] Frame-by-frame video analysis
* [ ] Advanced confidence visualization
* [ ] Face detection and localization
* [ ] Detection heatmaps
* [ ] Explainable AI
* [ ] Audio deepfake detection
* [ ] AI-generated image detection
* [ ] Detection history
* [ ] User authentication
* [ ] Cloud deployment
* [ ] GPU acceleration
* [ ] Mobile-responsive interface
* [ ] Public API
* [ ] Detailed downloadable reports

---

# ⚠️ Limitations

Deepfake detection is an evolving research problem.

Detection accuracy can be affected by:

* Video/image quality
* Compression
* Lighting
* Face orientation
* Manipulation technique
* Training dataset
* Unseen deepfake generation methods

Therefore, the result should be considered an **AI-assisted prediction**, not definitive proof that media is authentic or manipulated.

---

# 🎯 Objectives

The project aims to:

1. Develop an accessible deepfake detection platform.
2. Support both images and videos.
3. Integrate an AI detection model through an API.
4. Provide understandable detection results.
5. Create a modular architecture for future model improvements.
6. Demonstrate a practical application of AI for digital media verification.

---

# 🌍 Potential Applications

The system can be useful for:

* 📰 Digital journalism
* 🛡️ Cybersecurity research
* 🔎 Digital media verification
* 📱 Social media moderation
* 🧪 Academic research
* 🎓 Educational demonstrations
* 🖥️ Content verification

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/your-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature/your-feature
```

5. Open a Pull Request.

---

# 📜 License

This project is intended for **educational and research purposes**.

A suitable open-source license can be added after verifying the licenses of all datasets, pretrained models, and third-party libraries used in the project.

---

# 👨‍💻 Author

**Omkar Dattatray Ghorpade**

Computer Science & Engineering

Karmaveer Bhaurao Patil College of Engineering, Satara

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## ⚠️ Disclaimer

This project is developed for educational and research purposes. Deepfake detection models can produce incorrect predictions, particularly when encountering manipulation techniques or data distributions that were not represented during training.

The system should **not be used as the sole basis for legal, financial, journalistic, or other high-stakes decisions.**
