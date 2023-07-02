# 
FROM python:3.9

# 
WORKDIR /code

# Install necessary system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./patch.py /usr/local/lib/python3.9/site-packages/easyocr/utils.py
 
COPY ./app /code/app

COPY ./data /code/data

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
