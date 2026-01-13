# DevOps Assignment: Complete Setup Guide

## Assignment Overview
This is a DevOps assignment requiring implementation of three architectures with CI/CD pipelines:
1. **Monolithic Application** - Single app with all features
2. **Microservices Architecture** - Independent services  
3. **API Gateway/Proxy** - Routing layer for microservices

## What You Already Have
Your project structure is partially set up:
- ✅ **Framework**: Python with Flask (lightweight, perfect for learning)
- ✅ **Services Running**: User Service (5001), Product Service (5002), Order Service (5003), API Gateway (8000)
- ✅ **Dockerfiles**: Each service has a Dockerfile for containerization
- ✅ **CI/CD Pipelines**: GitHub Actions workflows (`.github/workflows/ci.yml`)

## Quick Start Commands

### Run All Services Locally
```bash
# Terminal 1 - User Service
cd microservices\user-service && python app.py

# Terminal 2 - Product Service
cd microservices\product-service && python app.py

# Terminal 3 - Order Service
cd microservices\order-service && python app.py

# Terminal 4 - API Gateway
cd api-gateway && python app.py

# Terminal 5 - Test APIs
curl http://localhost:8000/users
curl http://localhost:8000/products
curl http://localhost:8000/orders
```

### Run with Docker (if Docker Desktop is installed)
```bash
# Build images
docker build -t user-service microservices\user-service
docker build -t product-service microservices\product-service
docker build -t order-service microservices\order-service
docker build -t api-gateway api-gateway

# Run containers
docker run -p 5001:5001 user-service
docker run -p 5002:5002 product-service
docker run -p 5003:5003 order-service
docker run -p 8000:8000 api-gateway
```

## Architecture Patterns in This Codebase

### Monolithic vs Microservices
| Aspect | Monolith | Microservices |
|--------|----------|---------------|
| **Location** | `monolith-app/` | `microservices/` (3 services) |
| **Database** | Single DB | Each service independent |
| **Deployment** | One docker image | Multiple docker images |
| **Scaling** | All or nothing | Per-service scaling |
| **Failure Impact** | Full outage | Isolated to service |

### Service Communication Pattern
- **API Gateway** acts as single entry point (port 8000)
- Forwards requests to specific microservices based on path
- Example: `GET /users` → routes to User Service on 5001

### CI/CD Workflow
Each service has `.github/workflows/ci.yml` that:
1. Triggers on `git push` to GitHub
2. Runs `docker build` automatically
3. Creates/updates Docker image
4. Can deploy to registry or cloud

## Critical Files to Know

- [microservices/user-service/app.py](microservices/user-service/app.py) - User Service endpoint
- [microservices/product-service/app.py](microservices/product-service/app.py) - Product Service endpoint
- [microservices/order-service/app.py](microservices/order-service/app.py) - Order Service endpoint
- [api-gateway/app.py](api-gateway/app.py) - Central routing logic
- [README.md](README.md) - Full documentation

## Assignment Submission Steps

### Step 1: Local Testing (REQUIRED)
1. Run all services from "Quick Start Commands" above
2. Test each endpoint and take **screenshots** showing:
   - Services running in terminals
   - curl/browser output showing responses
   - All three architectures working

### Step 2: GitHub Setup (REQUIRED)
1. Create GitHub repository
2. Push your code: `git push`
3. Go to GitHub → Actions tab
4. Watch CI/CD pipelines execute automatically
5. Take **screenshot** of successful pipeline run
6. Note: You may need to enable GitHub Actions in repo settings

### Step 3: Prepare Submission Document
Create a document with this format:
```
DevOps Assignment Submission

Name: [Your Name]
Register Number: [Your Register Number]
Date: [Submission Date]

Implemented:
✓ Monolithic Application with CI/CD
✓ Microservices with CI/CD  
✓ API Gateway with CI/CD

Verification:
✓ Local execution screenshots attached
✓ GitHub Actions pipelines executed (screenshot attached)
✓ GitHub repository link: [Your GitHub URL]

Architecture Summary:
- Monolith runs on port 5000
- Microservices: User (5001), Product (5002), Order (5003)
- Gateway: port 8000, routes to all microservices
```

## Key DevOps Concepts Demonstrated

### Docker
- Containerization - Each service in isolated container
- Images - Defined in each Dockerfile
- Port mapping - `-p host:container` binds ports

### CI/CD
- **Continuous Integration**: Auto-build on push via GitHub Actions
- **Continuous Deployment**: Pipeline defined in `.github/workflows/ci.yml`
- **Automated Testing**: Pipeline can run tests (not fully set up yet)

### Microservices
- **Service Independence**: Each service can run/update independently
- **API Gateway Pattern**: Single endpoint routes to services
- **Scalability**: Can scale each service separately

## Troubleshooting

### Services Won't Start
- Ensure Python 3.7+ is installed: `python --version`
- Install Flask if missing: `pip install flask requests`
- Check ports aren't in use: `netstat -ano` (Windows)

### Docker Commands Fail
- Docker Desktop must be running
- Check installation: `docker --version`
- On Windows: May need WSL 2 backend enabled

### Git Push Fails
- Install Git: `git --version`
- Configure Git:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```
- Create SSH key: `ssh-keygen -t ed25519`
- Add to GitHub → Settings → SSH Keys

## References
- Flask docs: https://flask.palletsprojects.com
- Docker docs: https://docs.docker.com
- GitHub Actions: https://docs.github.com/actions
- Microservices pattern: https://microservices.io

## Next Steps
1. ✅ Run local services (DONE)
2. ☐ Set up GitHub repository
3. ☐ Push code and trigger CI/CD
4. ☐ Take screenshots
5. ☐ Submit assignment
