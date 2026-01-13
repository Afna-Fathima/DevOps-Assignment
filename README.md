# DevOps Assignment - Complete Setup Guide

## Project Structure

```
DevOps-Assignment/
├── monolith-app/
│   ├── app.py                    (Single app with all routes)
│   ├── Dockerfile                (Docker image config)
│   └── .github/workflows/ci.yml   (CI/CD pipeline)
│
├── microservices/
│   ├── user-service/
│   │   ├── app.py               (Port 5001)
│   │   ├── Dockerfile
│   │   └── .github/workflows/ci.yml
│   │
│   ├── product-service/
│   │   ├── app.py               (Port 5002)
│   │   ├── Dockerfile
│   │   └── .github/workflows/ci.yml
│   │
│   └── order-service/
│       ├── app.py               (Port 5003)
│       ├── Dockerfile
│       └── .github/workflows/ci.yml
│
└── api-gateway/
    ├── app.py                   (Port 8000, routes to all services)
    ├── Dockerfile
    └── .github/workflows/ci.yml
```

## What You Have

### 1. MONOLITHIC APPLICATION (All-in-one)
- **Purpose**: Single application with all features
- **Port**: 5000
- **Routes**: 
  - `/users` → returns User module
  - `/products` → returns Product module
  - `/orders` → returns Order module

### 2. MICROSERVICES (Independent services)
- **User Service** (Port 5001): Handles `/users` endpoint
- **Product Service** (Port 5002): Handles `/products` endpoint
- **Order Service** (Port 5003): Handles `/orders` endpoint
- Each service is completely independent with its own container

### 3. API GATEWAY (Single entry point)
- **Purpose**: Routes all requests to correct microservices
- **Port**: 8000
- **Routes**:
  - Client → Gateway → User Service
  - Client → Gateway → Product Service
  - Client → Gateway → Order Service

## LOCAL TESTING (Step by Step)

### Prerequisites
- Docker installed
- Command Prompt or PowerShell

### Test 1: Monolithic Application

```bash
cd C:\Users\agust\Downloads\DevOps-Assignment\monolith-app

# Build the Docker image
docker build -t monolith-app .

# Run the container
docker run -p 5000:5000 monolith-app

# In another terminal, test endpoints:
curl http://localhost:5000/users
curl http://localhost:5000/products
curl http://localhost:5000/orders
```

### Test 2: Microservices (All 3 services)

Run each in a separate terminal:

**Terminal 1 - User Service:**
```bash
cd C:\Users\agust\Downloads\DevOps-Assignment\microservices\user-service
docker build -t user-service .
docker run -p 5001:5001 user-service
```

**Terminal 2 - Product Service:**
```bash
cd C:\Users\agust\Downloads\DevOps-Assignment\microservices\product-service
docker build -t product-service .
docker run -p 5002:5002 product-service
```

**Terminal 3 - Order Service:**
```bash
cd C:\Users\agust\Downloads\DevOps-Assignment\microservices\order-service
docker build -t order-service .
docker run -p 5003:5003 order-service
```

**Terminal 4 - Test each service:**
```bash
curl http://localhost:5001/users
curl http://localhost:5002/products
curl http://localhost:5003/orders
```

### Test 3: API Gateway (With all services running)

**Terminal 5 - API Gateway:**
```bash
cd C:\Users\agust\Downloads\DevOps-Assignment\api-gateway
docker build -t api-gateway .
docker run -p 8000:8000 api-gateway
```

**Terminal 6 - Test through Gateway:**
```bash
curl http://localhost:8000/users
curl http://localhost:8000/products
curl http://localhost:8000/orders
```

## CI/CD Pipelines (GitHub Actions)

Each component has a `.github/workflows/ci.yml` file that:
1. Triggers on every `git push`
2. Automatically builds the Docker image
3. Can be viewed in GitHub Actions tab

### How to Use GitHub Actions:
1. Push code to GitHub: `git push`
2. Go to GitHub repository → Actions tab
3. Watch the pipeline run automatically
4. See build status (✓ passed or ✗ failed)

## Key Concepts

| Aspect | Monolithic | Microservices |
|--------|-----------|---------------|
| **Codebase** | Single | Multiple |
| **Deployment** | All or nothing | Independent |
| **Scaling** | Entire app | Per service |
| **Failure** | Full outage | Isolated |
| **CI/CD** | One pipeline | One per service |

## Submission Checklist

- [ ] Local execution working (screenshots)
- [ ] GitHub repository created
- [ ] All 3 components deployed
- [ ] CI/CD pipelines triggered (show GitHub Actions)
- [ ] Document with Name, Register Number, Date
- [ ] Proof of local testing

## Common Commands

```bash
# Build a Docker image
docker build -t image-name .

# Run a container with port mapping
docker run -p host-port:container-port image-name

# List running containers
docker ps

# Stop a container
docker stop container-id

# Remove an image
docker rmi image-name
```

---
Created: January 13, 2026
