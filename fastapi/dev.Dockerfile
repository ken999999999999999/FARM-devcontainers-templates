FROM python:3.10

WORKDIR /workspace/fastapi

COPY . .

RUN apt-get update 

# RUN pip install --upgrade pip

# RUN pip install debugpy

# RUN pip install httpx

# RUN pip install pytest

# RUN pip install -r requirements.txt

# CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "apps/main.py"]


