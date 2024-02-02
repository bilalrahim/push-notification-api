# Push Notification API

## Introduction

Push Notification API is a Django-based application that utilizes Firebase Admin SDK and Confluent Kafka for handling push notifications in real-time.

## Tech Stack

- Django
- Django REST Framework
- Firebase Admin SDK
- Confluent Kafka
- Gunicorn (for serving Django application)
- Docker
- Kubernetes

## Deployment Steps

### Prerequisites

- Docker installed
- Kubernetes cluster set up (if deploying on Kubernetes)

### Local Deployment

1. Clone the repository:

```bash
   git clone https://github.com/your-username/your-repository.git
```

2. 
```bash 
    cd your-repository
    docker-compose up
```
4. Kubernetes deployment: 
```bash
    kubectl apply -f deployment-django.yml
```bash
    kubectl apply -f deployment-kafka.yml
```

5. Apply Kubernetes Service file: 
```bash
  kubectl apply -f service-django.yml
  kubectl apply -f service-kafka.yml
```

6. Monitor pod status: 
```bash
   kubectl get pods
```


### Future Improvements
- Implement user authentication
- Add data validation for API endpoints
- Improve error handling
- Integrate with additional notification services
- Use secrets manager to store credentials.

## Side Note:
The container runs successfully without kubernetes but when I deploy it using kubernetes I get the following error.

```bash
exec: "gunicorn": executable file not found in $PATH: unknown
```

Plus since currently we do not have any device tokens from Firebase, because this is a demo project, so the firebase sdk throws an exception.