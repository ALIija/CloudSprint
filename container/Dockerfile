# container/Dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN python -m pip install --no-cache-dir fastapi uvicorn
COPY <<EOF /app/main.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/") 
def root(): return {"status":"ok"}
EOF
EXPOSE 80
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]
