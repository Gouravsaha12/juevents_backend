# STEP 1: Define the base image
FROM python:3.12-slim

# STEP 2: Set the working directory inside the container
WORKDIR /app

# STEP 3: Copy and install requirements
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# STEP 4: Copy your application code into the container
COPY . .

# STEP 5: Define the command to run your app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]