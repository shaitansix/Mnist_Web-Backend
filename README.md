# 🤖 MNIST Neural Network Playground
*Interactive web interface for training neural networks on MNIST dataset using Keras (Django backend) and React frontend*

---
## 🚀 Quick Setup Guide

## Using docker

### 1. Download the Docker Hub image
```bash
docker pull shaitansix/mnist_web-api:1
```

### 2. Create a Docker container and then initialize it
```bash
docker run --name mnist_web-api -e SECRET_KEY="hhha2%kgyg_!f7(^h4@l^%wwc@7z^%^^ql7rt&d_aea)n3+3-j" -e CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:4173,http://127.0.0.1:4173 -e ALLOWED_HOSTS=localhost,127.0.0.1 -p 8000:8000 shaitansix/mnist_web-api:1
```

### 3. Create a superuser
**In another system console, run the following command:**
```bash
docker exec -it mnist_web-api python manage.py createsuperuser
```

*✔️ Backend available at: 
http://localhost:8000/admin/*

## Using Django

### 1. Create a folder for the project and open cmd in this folder

### 2. Clone the Repository
```bash
git clone https://github.com/shaitansix/Mnist_Web-Backend.git
cd Mnist_Web-Backend
```

### 3. Create and activate virtual environment
```bash
pip install virtualenv
virtualenv -p python3.9 venv
.\venv\Scripts\activate  # Windows
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Migrate the database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Generating static files
```bash
python manage.py collectstatic
```

### 7. Configure environment variables
**Create a file .env.dev in /server and add:**
```bash
SECRET_KEY=hhha2%kgyg_!f7(^h4@l^%wwc@7z^%^^ql7rt&d_aea)n3+3-j
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:4173,http://127.0.0.1:4173
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 8. Create a folder called "data" in the Mnist_Web-Backend folder and then inside that folder create another one called "keras_models"

### 9. Create a superuser
```bash
python manage.py createsuperuser
```

### 10. Run the Django server
```bash
python manage.py runserver
```

*✔️ Backend available at: 
http://localhost:8000/admin/*