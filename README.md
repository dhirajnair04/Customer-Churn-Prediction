# 📊 Customer Churn Prediction App

This is a FastAPI-based web application that predicts customer churn using a trained machine learning model.

## 🚀 Features
- Web interface for input using `index.html`
- Predicts churn probability using a pre-trained `churn_model.pkl`
- Built with FastAPI for a fast and scalable backend
- Docker support for easy deployment

## 🛠️ Setup & Installation

### 1️⃣ Clone the repository
```sh
git clone https://github.com/dhirajnair04/Customer-Churn-Prediction.git
cd churn-prediction-app
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run the application
```
uvicorn app:app --reload
```
Then, open http://127.0.0.1:8000 in your browser.

### 🐳 Run with Docker (Optional)
```
docker build -t churn-app .
docker run -p 8000:8000 churn-app
```

### Deployment on AWS EC2 (Optional)
1. Launch an EC2 Instance
2. Install Docker & Git
   ```
   sudo apt update && sudo apt install -y docker.io git
   ```
3. Clone the Repository on EC2
   ```
   git clone https://github.com/your-username/Customer-Churn-Prediction.git
   ```
4. Build and Run Docker Container
   ```
   docker build -t churn-prediction .
   docker run -p 8000:8000 churn-prediction
   ```
## API Endpoints
Home Page (HTML Form for Input)
```
GET /
```

Prediction API (Submit Form Data)
```
POST /predict
```

## Contributing
Feel free to contribute by submitting issues or pull requests!

## Author
Dhiraj, Jeet, Palak, Taral
