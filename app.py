from fastapi import FastAPI
from pydantic import BaseModel
from main import AruBrain
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Web interface se connect karne ke liye CORS zaroori hai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

aru = AruBrain()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Aru AI Server is Online!"}

@app.post("/chat")
async def chat(req: ChatRequest):
    # Process cognition ka result return karega
    reply = aru.process_cognition(req.message)
    return {"reply": reply}