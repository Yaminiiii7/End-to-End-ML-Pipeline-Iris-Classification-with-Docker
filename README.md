# Iris Flower Classification Using KNN in Python – MLOps Project (FastAPI + Docker + K8s)


This project helps you learn **Building and Deploying an ML Model** using a simple and real-world use case end-to-end machine learning workflow: predicting flower species are predicted based on sepal and petal measurements.

- ✅ Model Training
- ✅ Building the Model locally
- ✅ API Deployment with FastAPI
- ✅ Dockerization
- ✅ Kubernetes Deployment

---

## 📊 Problem Statement

Predict if a person is diabetic based on:
- sepal_length
- sepal_width
- petal_length
- petal_width

We use a K-Nearest Neighbor Classifier trained on the **Iris Dataset**.

---

## 🚀 Quick Start

## Install EC2 dependencies

1.  **Update System Packages:**
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

2.  **Install Git, Docker, and Docker Compose:**
    ```bash
    sudo apt install git docker.io docker-compose-v2 -y
    ```

3.  **Start and Enable Docker:**
    ```bash
    sudo systemctl start docker
    sudo systemctl enable docker
    ```

4.  **Add User to Docker Group (to run docker without sudo):**
    ```bash
    sudo usermod -aG docker $USER
    newgrp docker
    ```
5) **Install k3s**
  ```bash
  curl -sfL https://get.k3s.io | sh -
  ```

6) **Verify cluster + set kubectl access**
  k3s installs kubectl as k3s kubectl. You can use either:
  ```bash
  sudo k3s kubectl get nodes
  sudo k3s kubectl get pods -A
  ```

7) **Allow your user to read kubeconfig**
  ```bash
  sudo chmod 644 /etc/rancher/k3s/k3s.yaml
  export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
  echo 'export KUBECONFIG=/etc/rancher/k3s/k3s.yaml' >> ~/.bashrcsource ~/.bashrc
  kubectl get nodes
  ```


### 1. Clone the Repo

```bash
git clone https://github.com/Yaminiiii7/End-to-End-ML-Pipeline-Iris-Classification-with-Docker.git
cd End-to-End-ML-Pipeline-Iris-Classification-with-Docker
```
### 2.Install Python and pip

```bash
sudo apt install python3 python3-pip python3-venv -y
```

### 3. Create Virtual Environment

```
python3 -m venv .mlops
.venv/Scripts/Activate
```

### 4. Install Dependencies

```
pip install -r requirements.txt
```

## 5. Train the Model

```
python train.py
```

## 6. Run the API Locally

```
uvicorn main:app --reload
```

### 7. Sample Input for /predict

```
/predict?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2
```

## Dockerize the API

### 8. Build the Docker Image

```bash
  docker build -t iris-prediction-model .
```

### 9. Run the Container

```bash
  docker run -p 8000:8000 iris-prediction-model
```

### 10. Deploy to Kubernetes

```bash
  kubectl apply -f iris-prediction-model-deployment.yml
```
### 11. Check pods availability

```
    kubectl get pods -w
```

## 11. Access 
```
  http://<publicIPofEC2>:8000
```

