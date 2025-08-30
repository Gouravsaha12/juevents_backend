# JUEvents Backend

[![Made with FastAPI](https://img.shields.io/badge/Made%20with-FastAPI-green.svg)](https://fastapi.tiangolo.com/)
[![Python Version](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)](https://www.postgresql.org/)
[![Dockerized](https://img.shields.io/badge/Dockerized-Yes-blue.svg)](https://www.docker.com/)

A robust backend service for the JUEvents application, built with FastAPI and PostgreSQL, and fully containerized with Docker for easy setup and deployment.

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [📋 Prerequisites](#-prerequisites)
- [🚀 Getting Started](#-getting-started)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create the Configuration File (.env)](#2-create-the-configuration-file-env)
  - [3. Build and Run with Docker Compose](#3-build-and-run-with-docker-compose)
- [✅ Verifying the Setup](#-verifying-the-setup)
  
---

## ✨ Features

- **Modern API Framework**: Built with **FastAPI** for high performance and automatic interactive documentation.
- **Relational Database**: Uses **PostgreSQL** for reliable and persistent data storage.
- **Containerized Environment**: Uses **Docker** and **Docker Compose** to ensure a consistent and isolated development environment.
- **Scalable**: The container-based setup is ready for deployment to any cloud provider.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop)
- [Git](https://git-scm.com/downloads)

---

## 🚀 Getting Started

Follow these steps to get the application running on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd juevents_backend

### 2. Create the Configuration File (.env)

The application uses environment variables for configuration. Create a file named `.env` in the root of the `juevents_backend` directory.

Copy and paste the following template into the `.env` file, and modify the values as needed:

```env
# PostgreSQL Settings
POSTGRES_USER=juevents_user
POSTGRES_PASSWORD=your_strong_password_here
POSTGRES_DB=juevents_db
POSTGRES_HOST=db
POSTGRES_PORT=5432

# FastAPI Database Connection URL
# Note: The username, password, host, and db name must match the variables above.
DATABASE_URL="postgresql://juevents_user:your_strong_password_here@db:5432/juevents_db"

# Application Settings
SECRET_KEY=your_very_secret_key_for_jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

### 3. Build and Run with Docker Compose

From the root of the `juevents_backend` directory, run the following commands:

```bash
# Build the API image (use --no-cache for a completely fresh build)
docker-compose build

# Start the API and Database containers in the background
docker-compose up -d

## ✅ Verifying the Setup

After starting the containers, verify everything is running properly.

### ✅ Check Container Status

Run the following command to check the status of the running containers:

```bash
docker-compose ps

### 📜 View Logs

To view real-time logs from your services, run:

```bash
docker-compose logs -f
