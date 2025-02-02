from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status":True,"message": "Systemn is up and running"}