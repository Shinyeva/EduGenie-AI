from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1 style='text-align:center;color:#7c3aed;margin-top:100px'>
    🎓 EduGenie-AI is LIVE!</h1>
    <p style='text-align:center'>Your AI Learning Assistant Ready for Demo!</p>
    """
