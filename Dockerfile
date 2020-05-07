FROM python:3-alpine

LABEL email="yevhen.trofimenko@gmail.com"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "run_all_templates.py"]