# Use official Python 3.10 image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY src/ ./src/

# Install dependencies
RUN pip install --no-cache-dir coverage

# Set PYTHONPATH so tests can import main
ENV PYTHONPATH=/app/src

# Default command: run calculator interactively
CMD ["python", "src/main.py"]

# Optional: run tests with coverage
# docker build -t python-calculator .
# docker run --rm python-calculator coverage run -m unittest discover -s src -p "test_*.py"
# docker run --rm python-calculator coverage report
