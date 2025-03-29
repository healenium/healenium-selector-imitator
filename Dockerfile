FROM python:alpine

RUN pip install --upgrade pip

COPY ./ ./

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]