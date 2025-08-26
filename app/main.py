from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"status": "ok", "message": "arc_micro_plan placeholder running"}
