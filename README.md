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
- [✅ Verifying the Setup](#-verifying-the-setup)
- [🗄️ Connecting to the Database](#️-connecting-to-the-database-pgadmin)
- [🛠️ Common Development Commands](#️-common-development-commands)
- [🚢 Pushing to Docker Hub](#-pushing-to-docker-hub)

---

## ✨ Features

* **Modern API Framework**: Built with **FastAPI** for high performance and automatic interactive documentation.
* **Relational Database**: Uses **PostgreSQL** for reliable and persistent data storage.
* **Containerized Environment**: Uses **Docker** and **Docker Compose** to ensure a consistent and isolated development environment.
* **Scalable**: The container-based setup is ready for deployment to any cloud provider.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop)
* [Git](https://git-scm.com/downloads)

---

## 🚀 Getting Started

Follow these steps to get the application running on your local machine.

### 1. Clone the Repository

First, clone this repository to your local machine using Git.

```bash
git clone <your-repository-url>
cd juevents_backend
