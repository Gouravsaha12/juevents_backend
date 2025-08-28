# JUEVENTS Backend

FastAPI-based backend for managing events, registrations, and users.  
Built with **FastAPI**, **SQLAlchemy**, **Alembic**, and **PostgreSQL**.

---

## 🚀 Features
- User authentication (JWT based)
- Create, update, delete events
- Register/unregister for events
- Cascade delete (events → registrations)
- Filter events by type/location
- Separate past, current, and upcoming events

---

## 🛠 Tech Stack
- **FastAPI** (backend framework)
- **SQLAlchemy + Alembic** (ORM + migrations)
- **PostgreSQL** (database)
- **Pydantic** (data validation)

---

## 📦 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/juevents.git
   cd juevents/backend
