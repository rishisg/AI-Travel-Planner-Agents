# Use Python official image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy only necessary files first (to optimize caching)
COPY requirements.txt /app/

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app/

# Ensure environment variables are loaded securely at runtime
CMD ["streamlit", "run", "app.py"]

# Expose Streamlit port
EXPOSE 8501
