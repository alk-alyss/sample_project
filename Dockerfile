FROM python:3.11
WORKDIR /server
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./ask3.py .
CMD ["uvicorn", "ask3:app", "--host", "0.0.0.0", "--port", "80"]