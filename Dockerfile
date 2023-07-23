FROM python:3.8.10-slim

WORKDIR /myapi

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application files to the working directory
COPY . .

# Expose the port that the FastAPI application listens on
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
