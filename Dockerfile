# 1. Use the official slim Python 3.10 image
FROM python:3.10-slim

# 2. Set /app as the working directory inside the container
WORKDIR /app

# 3. Copy all files (app/, Dockerfile, etc.) into /app
COPY . .

# 4. Install only the needed Python packages
RUN pip install --no-cache-dir fastapi uvicorn psycopg2-binary

# 5. Tell Docker that the container listens on port 8000
EXPOSE 8000

# 6. When the container starts, run Uvicorn pointing at our app
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
