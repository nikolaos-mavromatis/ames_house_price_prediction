FROM python:3.12.4-slim

WORKDIR /app

COPY /app/main.py /app/

RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port", "8501"]



# WORKDIR /api

# COPY . .

# RUN pip install -r requirements.txt

# EXPOSE 8000

# CMD ["fastapi", "run", "api/main.py", "--host", "0.0.0.0", "--port", "8000"]
