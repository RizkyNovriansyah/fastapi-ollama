# Menggunakan image Python sebagai base image
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

RUN apt-get update && apt-get install -y iputils-ping

# Menyalin file requirements.txt (jika ada)
COPY requirements.txt /app/

# Install dependencies (FastAPI dan Uvicorn)
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file dari folder lokal ke container
COPY . /app/

# Menentukan port yang digunakan oleh aplikasi
EXPOSE 8000

# Menjalankan aplikasi FastAPI menggunakan Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
