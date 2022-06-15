FROM python:3.7

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD streamlit run --server.port 8080 app.py