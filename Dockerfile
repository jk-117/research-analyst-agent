# Use official Python image
FROM python:3.10

# Set work directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Upgrade pip to latest (important for large dependencies)
RUN pip install --upgrade pip

# Install dependencies with increased timeout to avoid ReadTimeoutError
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
