\# IRS — Face Recognition System



A Python-based face recognition application that identifies registered individuals from a live camera feed using deep learning-based face embeddings and MongoDB for student information.



\## 📌 Overview



IRS (Identification and Recognition System) is a computer vision project developed to demonstrate real-time face detection and recognition.



The application:



\* Captures video from a webcam

\* Detects faces from the video stream

\* Generates face encodings using a pre-trained FaceNet-based model

\* Compares detected faces against registered face encodings

\* Identifies recognized individuals

\* Retrieves/stores student information using MongoDB

\* Provides a web interface using Flask



\## 🛠️ Technologies Used



\* \*\*Python\*\*

\* \*\*OpenCV\*\* — Computer vision and video processing

\* \*\*TensorFlow / Keras\*\* — Deep learning model execution

\* \*\*FaceNet\*\* — Face embedding / recognition model

\* \*\*dlib\*\* — Facial landmark processing

\* \*\*Flask\*\* — Web application framework

\* \*\*MongoDB / PyMongo\*\* — Student information storage

\* \*\*NumPy\*\*

\* \*\*SciPy\*\*

\* \*\*imutils\*\*



\## 🧠 System Architecture



```text

&#x20;               ┌──────────────────┐

&#x20;               │   Webcam / Video │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │   Face Detection │

&#x20;               │     OpenCV       │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │ Face Preprocessing│

&#x20;               │  \& Alignment     │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │ Face Embedding   │

&#x20;               │ FaceNet / Keras  │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │ Similarity /     │

&#x20;               │ Distance Check   │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                   ┌────┴────┐

&#x20;                   │         │

&#x20;                 Match     Unknown

&#x20;                   │

&#x20;                   ▼

&#x20;            ┌───────────────┐

&#x20;            │    MongoDB    │

&#x20;            │ Student Data  │

&#x20;            └───────────────┘

```



\## 📂 Project Structure



```text

IRS/

│

├── haarcascades/

│   └── haarcascade\_frontalface\_default.xml

│

├── static/

│   └── templatepic.jpg

│

├── templates/

│   └── ...

│

├── webapp2.0.py

├── fr\_utils.py

├── inception\_blocks\_v2.py

├── requirements.txt

├── README.md

├── INSTRUCTIONS.txt

└── ...

```



> \*\*Note:\*\* Large model files and the face-image dataset are intentionally excluded from this repository. See the setup section below.



\## 📦 Required Model Files



The application requires the following model files locally:



```text

shape\_predictor\_68\_face\_landmarks.dat

nn4.small2.v1.h5

```



These files are not included in this repository because of their size.



You must obtain/place the required model files in the project root before running the application.



The application also expects a local face dataset in:



```text

images/

```



The dataset is intentionally excluded from the public repository.



\## 🗄️ MongoDB Configuration



The application uses MongoDB to store student information.



The MongoDB connection should \*\*not\*\* be hard-coded into the source code.



Set your MongoDB connection string through an environment variable:



```text

MONGO\_URI=your\_mongodb\_connection\_string

```



For example, when using a `.env` file:



```text

MONGO\_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true\&w=majority

```



Never commit real database credentials, passwords, API keys, or other secrets to GitHub.



\## ⚙️ Installation



\### 1. Clone the repository



```bash

git clone https://github.com/Aj-Chaudhary/IRS.git

cd IRS

```



\### 2. Create a virtual environment



Windows:



```powershell

python -m venv venv

venv\\Scripts\\activate

```



Linux/macOS:



```bash

python3 -m venv venv

source venv/bin/activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Add the required model files



Place:



```text

shape\_predictor\_68\_face\_landmarks.dat

nn4.small2.v1.h5

```



in the appropriate project location.



\### 5. Configure MongoDB



Create a `.env` file:



```text

MONGO\_URI=your\_mongodb\_connection\_string

```



Make sure `.env` is included in `.gitignore`.



\### 6. Add a local face dataset



Create:



```text

images/

```



and organize registered faces by identity.



Example:



```text

images/

├── Person1/

│   ├── image1.jpg

│   ├── image2.jpg

│   └── image3.jpg

│

└── Person2/

&#x20;   ├── image1.jpg

&#x20;   └── image2.jpg

```



\### 7. Run the application



```bash

python webapp2.0.py

```



\## 🔍 Recognition Process



The recognition pipeline follows these general steps:



1\. Capture a frame from the camera.

2\. Detect faces in the frame.

3\. Process and align detected faces.

4\. Generate numerical face embeddings.

5\. Compare the embedding with registered identities.

6\. Apply the configured recognition threshold.

7\. Identify the closest matching registered person.

8\. Retrieve relevant student information from MongoDB.



\## 🎯 Project Purpose



This project was developed as a practical exploration of:



\* Computer vision

\* Face recognition

\* Deep learning

\* Python application development

\* Flask web applications

\* MongoDB integration

\* Real-time video processing



It demonstrates how multiple technologies can be combined to build an end-to-end identification system.



\## ⚠️ Limitations



\* Recognition performance depends on lighting, camera quality, pose, and image quality.

\* The pre-trained model is relatively lightweight and may not provide state-of-the-art recognition performance.

\* The application requires the appropriate model files and local face dataset.

\* MongoDB configuration is required for student information functionality.

\* This project is intended primarily for educational and demonstration purposes.



\## 🔐 Privacy \& Responsible Use



Face recognition involves sensitive biometric information.



If adapting this project for real-world use:



\* Obtain appropriate consent before collecting facial data.

\* Protect stored biometric information.

\* Never publish private face datasets publicly.

\* Secure database credentials and access controls.

\* Follow applicable privacy and data-protection laws.

\* Provide appropriate mechanisms for data deletion and access where required.



\## 🚀 Future Improvements



Possible improvements include:



\* Modern face detection models

\* Improved face alignment

\* More robust recognition under different lighting conditions

\* Role-based authentication

\* Secure REST APIs

\* Better database architecture

\* Attendance management

\* Recognition confidence visualization

\* Docker deployment

\* Cloud deployment

\* Automated testing

\* Improved frontend UI

\* Privacy-preserving biometric storage



\## 👨‍💻 Author



\*\*Ajay Kumar Chaudhary\*\*



Computer Science \& Engineering

Interested in Software Engineering, Artificial Intelligence, Machine Learning, Computer Vision, and intelligent systems.



GitHub:

https://github.com/Aj-Chaudhary



\## 📄 License



This project can be used for educational and research purposes. Check the licenses of all third-party models, datasets, libraries, and dependencies before redistributing or deploying the project commercially.



