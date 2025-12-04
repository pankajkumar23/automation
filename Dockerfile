# 1. Use a lightweight Linux system with Python installed
FROM python:3.9-slim

# 2. Create a working folder inside the container
WORKDIR /app

# 3. Copy all files from your laptop to the container's folder
COPY . .

# 4. The command to run when the container starts
CMD ["python", "main.py"]