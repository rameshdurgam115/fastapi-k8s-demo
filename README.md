# fastapi-k8s-demo

A simple three-container Kubernetes demo app, built with FastAPI, PostgreSQL, and Nginx.

## 📖 Overview

This project shows how to:

1. **Write** a FastAPI app that returns your Postgres version  
2. **Containerize** it with Docker  
3. **Deploy** to Kubernetes (Minikube) with three services:
   - **Postgres** (database)  
   - **FastAPI** (backend)  
   - **Nginx** (reverse-proxy)  
4. **Test** via port-forwarding and Swagger UI

---

## 🚀 Prerequisites

- **Git**  
- **Docker** (and Docker Desktop if on Windows/macOS)  
- **kubectl** CLI  
- **Minikube** or **Kind**  
- **Python 3.8+** (for local dev, optional once Dockerized)

---
