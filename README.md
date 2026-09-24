# 🌱 Smart Vegetable & Plant Leaf Detection System

<p align="center">
  <img src="home.png" alt="Smart Vegetable & Plant Leaf Detection System" width="100%">
</p>

<h3 align="center">
  AI-Powered Vegetable & Plant Leaf Detection System
</h3>

<p align="center">
  A professional Django-based web application integrating CNN, YOLO, and Computer Vision for image, video, and real-time camera detection.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Django-Framework-green?style=for-the-badge&logo=django">
  <img src="https://img.shields.io/badge/CNN-Deep%20Learning-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/YOLO-Object%20Detection-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-blue?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap">
</p>

---

## 📌 Overview

**Smart Vegetable & Plant Leaf Detection System** is a Django-based Artificial Intelligence and Computer Vision application designed to detect and classify vegetables and plant leaves through different input sources.

The system integrates trained **CNN classification models** and **YOLO object detection models** into a Django web application. Users can perform detection using uploaded images, uploaded videos, or a live camera.

The application also provides a complete user authentication system. Registered users can create an account, log in, access their personal profile, and view their previous detection records.

The project combines:

* Artificial Intelligence
* Deep Learning
* Computer Vision
* Image Classification
* Object Detection
* Real-Time Detection
* Django Web Development

---

# ✨ Features

| Feature              | Description                                    |
| -------------------- | ---------------------------------------------- |
| 🏠 Home              | Project landing page and system overview       |
| 📖 About             | Information about the project and technologies |
| 📞 Contact           | Contact and communication interface            |
| 🖼️ Image Detection  | AI-based detection from uploaded images        |
| 🎥 Video Detection   | Detection from uploaded video files            |
| 📷 Camera Detection  | Real-time detection using a live camera        |
| 🔐 Registration      | New user account creation                      |
| 🔑 Login             | Secure user authentication                     |
| 👤 User Profile      | Personal user profile access                   |
| 📊 Detection History | View previous detection records                |
| 🤖 CNN               | Image classification                           |
| 🎯 YOLO              | Object detection                               |

---

# 🖥️ Application Interface

## 🏠 Home Page

The home page acts as the main entry point of the application and provides access to the system's major features.

<p align="center">
  <img width="1333" height="2882" alt="home" src="https://github.com/user-attachments/assets/1219e72f-07de-4d4f-b41d-c8819934a626" />
</p>

---

## 📖 About Page

The About page presents the purpose of the project, its AI technologies, and the overall functionality of the system.

<p align="center">
  <img width="1344" height="2072" alt="about_us" src="https://github.com/user-attachments/assets/98d9f078-0168-4174-bce4-8f9177bc5c38" />
</p>

---

## 📞 Contact Page

The Contact page provides a user-friendly interface for communication and project-related inquiries.

<p align="center">
  <img width="1347" height="1764" alt="contact" src="https://github.com/user-attachments/assets/ad357fb8-7f54-474f-ac4e-6a56394da575" />
</p>

---

## 📷 Camera Detection

The camera detection module performs **real-time AI detection** using a live camera stream.

<p align="center">
  <img width="1338" height="2286" alt="cam_detaction" src="https://github.com/user-attachments/assets/081848a2-4946-49fd-82f5-44f18236379a" />
</p>

### Detection Flow

```text
Live Camera
     ↓
Video Frames
     ↓
AI Model
     ↓
YOLO Detection
     ↓
Detection Result
```

---

## 🎥 Video Detection

The video detection module allows users to upload video files and process them using the trained AI detection model.

<p align="center">
  <img width="1332" height="2561" alt="video_detaction" src="https://github.com/user-attachments/assets/e7d1929b-bbfc-4e57-89a0-ebfdc921d9c1" />
</p>

### Detection Flow

```text
Video Upload
     ↓
Frame Extraction
     ↓
AI Processing
     ↓
YOLO Detection
     ↓
Detection Result
```

---

## 🖼️ Image Detection

The image detection module allows users to upload an image and perform AI-based classification and detection.

<p align="center">
  <img width="1320" height="2664" alt="image_detaction" src="https://github.com/user-attachments/assets/daa779f6-8fee-4589-9e39-2033073418ef" />
</p>

### Detection Flow

```text
Image Upload
     ↓
Image Preprocessing
     ↓
CNN / YOLO Model
     ↓
Prediction
     ↓
Detection Result
```

---

## 👤 User Profile

Registered users can access their personal profile and review their detection activities.

<p align="center">
  <img width="1341" height="3801" alt="profile44" src="https://github.com/user-attachments/assets/e973a3a0-8999-41d0-aa8f-8e3dde2c3aad" />
</p>

### Profile Features

* User registration
* User login/logout
* Personal profile
* Detection records
* Detection history
* User-specific information

---

# 🧠 AI & Machine Learning

The project uses two primary deep learning approaches.

## 🔬 CNN Classification

**Convolutional Neural Network (CNN)** models are used for image classification.

CNN models learn visual patterns and features from plant, leaf, fruit, and vegetable images and use those learned features to classify input images.

### CNN Components

```text
CNN_Classification_Dataset/
        ↓
Data Preprocessing
        ↓
CNN Training
        ↓
CNN_Models/
        ↓
Model Evaluation
        ↓
Final Testing
```

---

## 🎯 YOLO Object Detection

**YOLO (You Only Look Once)** is used for object detection and real-time detection tasks.

The YOLO models can process image frames from uploaded images, videos, and live camera streams.

### YOLO Components

```text
YOLO_Classification_Dataset/
        ↓
Data Preparation
        ↓
YOLO Training
        ↓
YOLO_Models/
        ↓
Model Evaluation
        ↓
Django Integration
        ↓
Live Detection
```

---

# 📂 AI / ML Directory Structure

The AI development workspace is organized inside `AI/notebooks/`.

```text
AI/
│
├── requirements.txt
│
└── notebooks/
    │
    ├── Cleaned_Dataset/
    │
    ├── CNN_Classification_Dataset/
    │
    ├── CNN_Models/
    │
    ├── CNN_Results/
    │
    ├── Final_Testing_Results/
    │
    ├── Model_Evaluation_Results/
    │
    ├── Preprocessed_Data/
    │
    ├── Preprocessed_Dataset/
    │
    ├── runs/
    │
    ├── YOLO_Classification_Dataset/
    │
    ├── YOLO_Models/
    │
    ├── 01_Dataset_Analysis.ipynb
    ├── 02_Data_Cleaning.ipynb
    ├── 03_Data_Preprocessing.ipynb
    ├── 04_Data_Visualization.ipynb
    ├── 05_Image_Preprocessing.ipynb
    ├── 06_YOLO_Training.ipynb
    ├── 07_CNN_Training.ipynb
    ├── 08_Model_Evaluation.ipynb
    └── 09_Final_Testing.ipynb
```

### AI Directory Description

| Directory / File               | Purpose                                 |
| ------------------------------ | --------------------------------------- |
| `Cleaned_Dataset/`             | Cleaned dataset files                   |
| `CNN_Classification_Dataset/`  | Dataset prepared for CNN classification |
| `CNN_Models/`                  | Trained CNN models                      |
| `CNN_Results/`                 | CNN training/results                    |
| `Final_Testing_Results/`       | Final model testing results             |
| `Model_Evaluation_Results/`    | Model evaluation outputs                |
| `Preprocessed_Data/`           | Processed metadata/data                 |
| `Preprocessed_Dataset/`        | Preprocessed image datasets             |
| `runs/`                        | YOLO training/inference outputs         |
| `YOLO_Classification_Dataset/` | Dataset prepared for YOLO               |
| `YOLO_Models/`                 | Trained YOLO models                     |
| `01_Dataset_Analysis.ipynb`    | Dataset analysis                        |
| `02_Data_Cleaning.ipynb`       | Data cleaning                           |
| `03_Data_Preprocessing.ipynb`  | Data preprocessing                      |
| `04_Data_Visualization.ipynb`  | Data visualization                      |
| `05_Image_Preprocessing.ipynb` | Image preprocessing                     |
| `06_YOLO_Training.ipynb`       | YOLO training                           |
| `07_CNN_Training.ipynb`        | CNN training                            |
| `08_Model_Evaluation.ipynb`    | Model evaluation                        |
| `09_Final_Testing.ipynb`       | Final testing                           |

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │        User         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Django Web App   │
                         └──────────┬──────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             │                      │                      │
             ▼                      ▼                      ▼
      Image Detection       Video Detection       Camera Detection
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    AI Processing    │
                         └──────────┬──────────┘
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                         ▼                     ▼
                    CNN Model             YOLO Model
                  Classification         Object Detection
                         │                     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │  Detection Result   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Detection Record    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   User Profile      │
                         │ Detection History   │
                         └─────────────────────┘
```

---

# 🔄 Complete AI Development Workflow

```text
Dataset Collection
        ↓
Dataset Analysis
        ↓
Data Cleaning
        ↓
Data Preprocessing
        ↓
Image Preprocessing
        ↓
 ┌──────┴──────┐
 ↓             ↓
CNN Training   YOLO Training
 ↓             ↓
CNN Models     YOLO Models
 └──────┬──────┘
        ↓
Model Evaluation
        ↓
Final Testing
        ↓
Django Integration
        ↓
Image / Video / Camera Detection
        ↓
Detection Records
        ↓
User Profile & History
```

---


# 🎨 Frontend Technologies

The frontend interface is developed using:

* **HTML5** — webpage structure and semantic content
* **CSS3** — custom styling and responsive UI
* **Bootstrap 5** — responsive layout and modern UI components
* **JavaScript** — client-side interaction and dynamic functionality
* **Django Templates** — dynamic HTML rendering and backend integration

---

# ⚙️ Backend Technologies

The backend is built with:

* **Python**
* **Django**
* **Django Authentication**
* **Django ORM**
* **Django Templates**
* **SQLite / Django-supported database**

---

# 👤 Authentication & User Management

The application provides a complete user authentication workflow:

```text
New User
   ↓
Registration
   ↓
Login
   ↓
Authenticated Session
   ↓
Dashboard
   ├── Image Detection
   ├── Video Detection
   ├── Camera Detection
   └── User Profile
             ↓
       Detection History
```

Each authenticated user can access their own profile and associated detection records.

---

# 📊 Detection Record Management

The system maintains detection information associated with users.

A detection record may contain information such as:

* Detection type
* Input media
* Prediction result
* Detection information
* Date and time
* Associated user

This provides users with a convenient way to review their previous detection activities.

---

# 📚 Datasets

The project uses publicly available datasets for training and developing the AI models.

## 🍎 Fruits-360

**Folder:**

```text
Fruits-360/
```

**Kaggle:**

[Fruits-360 Dataset](https://www.kaggle.com/moltean/fruits?utm_source=chatgpt.com)

Used for fruit image classification and visual recognition.

---

## 🌿 New Plant Diseases

**Folder:**

```text
New_Plant_Diseases/
```

**Kaggle:**

[New Plant Diseases Dataset](https://www.kaggle.com/vipoooool/new-plant-diseases-dataset?utm_source=chatgpt.com)

Used for plant leaf and disease classification tasks.

---

## 🌱 PlantDoc

**Folder:**

```text
PlantDoc/
```

**Kaggle:**

[PlantDoc Dataset](https://www.kaggle.com/abdulhasibuddin/plant-doc-dataset?utm_source=chatgpt.com)

Used for plant and plant disease detection/classification tasks.

---

## 🥕 Vegetable Image Dataset

**Folder:**

```text
Vegetable_Dataset/
```

**Kaggle:**

[Vegetable Image Dataset](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset?utm_source=chatgpt.com)

Used for vegetable image classification and recognition.

---

# 📋 Dataset Reference

| Dataset Name            | Local Folder          | Application                           |
| ----------------------- | --------------------- | ------------------------------------- |
| Fruits-360              | `Fruits-360/`         | Fruit Classification                  |
| New Plant Diseases      | `New_Plant_Diseases/` | Plant Disease Classification          |
| PlantDoc                | `PlantDoc/`           | Plant Detection & Disease Recognition |
| Vegetable Image Dataset | `Vegetable_Dataset/`  | Vegetable Classification              |

> **Note:** Large datasets and trained model files are excluded from the Git repository to keep the repository lightweight. Download the required datasets from their respective sources when reproducing the AI experiments.

---

# 🛠️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/LIMON-714/Smart_Agrivision.git
```

```bash
cd Smart_Agrivision
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r AI/requirements.txt
```

---

## 4. Environment Configuration

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
```

Keep the real `.env` file private and do not commit it to GitHub.

---

## 5. Database Setup

Run Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6. Create Admin User

```bash
python manage.py createsuperuser
```

Enter the required username, email, and password.

---

## 7. Start the Application

```bash
python manage.py runserver
```

Then open the local Django development server in your browser.

---

# 📦 Git & Large Files

The project uses `.gitignore` to prevent large generated AI/ML assets and sensitive files from being committed.

Examples include:

```text
CNN_Classification_Dataset/
CNN_Models/
YOLO_Classification_Dataset/
YOLO_Models/
Cleaned_Dataset/
Preprocessed_Data/
Preprocessed_Dataset/
CNN_Results/
Final_Testing_Results/
Model_Evaluation_Results/
runs/
*.pt
*.pth
*.keras
*.onnx
*.pkl
.env
db.sqlite3
```

This allows the source code, notebooks, configuration templates, and required project files to remain manageable in Git.

---

# 🔐 Security

Security considerations include:

* Sensitive environment variables are stored outside the repository.
* `.env` is excluded from Git.
* User authentication is handled through Django.
* User-specific detection records are associated with authenticated accounts.
* Large model files are excluded from the source repository.
* Database files containing local application data are excluded from Git.

---

# 🔮 Future Development

Potential future improvements include:

* 📱 Mobile application support
* ☁️ Cloud deployment
* 🌐 Production hosting
* 📈 Advanced analytics dashboard
* 🌿 Additional plant disease classes
* 🥬 More vegetable categories
* ⚡ Faster real-time inference
* 🔔 Detection notifications
* 🌍 Multi-language support
* 🧠 Further model optimization
* 📊 Advanced model performance monitoring

---

# 🧰 Technology Stack

```text
Frontend
│
├── HTML5
├── CSS3
├── Bootstrap 5
├── JavaScript
└── Django Templates

Backend
│
├── Python
└── Django

AI / ML
│
├── CNN
├── YOLO
├── Deep Learning
└── Computer Vision

Development
│
├── Jupyter Notebook
├── OpenCV
├── NumPy
└── Pandas
```

---

# 📌 Project Summary

**Smart Vegetable & Plant Leaf Detection System** brings together web development and Artificial Intelligence into a single integrated platform.

The system provides:

```text
                SMART AGRIVISION
                      │
        ┌─────────────┼─────────────┐
        │             │             │
     IMAGE          VIDEO         CAMERA
        │             │             │
        └─────────────┼─────────────┘
                      │
                 AI DETECTION
                      │
              ┌───────┴───────┐
              │               │
             CNN             YOLO
              │               │
              └───────┬───────┘
                      │
                RESULT / RECORD
                      │
                 USER PROFILE
                      │
               DETECTION HISTORY
```

The combination of **Django, CNN, YOLO, Computer Vision, and modern frontend technologies** provides the foundation for an integrated AI-powered plant and vegetable detection platform.

---

# 👨‍💻 Developer

### Smart Vegetable & Plant Leaf Detection System

Developed using:

**Python • Django • CNN • YOLO • OpenCV • HTML5 • CSS3 • Bootstrap 5 • JavaScript**

---

# 📜 License

This project is developed for educational, research, and software development purposes.

The external datasets used by this project are subject to their respective dataset licenses and terms of use. Please review the licensing conditions of each dataset before redistribution or commercial use.

---

# 🙏 Acknowledgements

Thanks to the creators and contributors of the publicly available datasets used during the development of this project.

### Dataset Sources

* Fruits-360 — Kaggle
* New Plant Diseases Dataset — Kaggle
* PlantDoc — Kaggle
* Vegetable Image Dataset — Kaggle

---

<p align="center">
  🌱 <strong>Smart Vegetable & Plant Leaf Detection System</strong> 🤖
</p>

<p align="center">
  Built with Python • Django • CNN • YOLO • Computer Vision
</p>
