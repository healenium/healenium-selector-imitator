FROM python:3.7-slim-stretch

RUN pip install --upgrade pip==23.3

COPY ./ ./

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]