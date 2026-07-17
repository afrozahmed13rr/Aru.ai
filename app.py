from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import g4f

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; background: #fff; }
        .header { display: flex; align-items: center; padding: 15px; border-bottom: 1px solid #eee; }
        .header img { width: 40px; height: 40px; margin-right: 12px; }
        #chat { flex: 1; overflow-y: auto; padding: 15px; display: flex; flex-direction: column; }
        .msg { padding: 12px 16px; margin: 6px 0; border-radius: 18px; max-width: 75%; font-size: 15px; }
        .user { align-self: flex-end; background: #007bff; color: white; border-bottom-right-radius: 4px; }
        .bot { align-self: flex-start; background: #f1f0f0; color: black; border-bottom-left-radius: 4px; }
        .input-area { display: flex; padding: 15px; background: #fff; border-top: 1px solid #eee; position: sticky; bottom: 0; }
        input { flex: 1; padding: 14px; border: 1px solid #ddd; border-radius: 25px; outline: none; }
        button { padding: 12px 20px; border: none; background: #007bff; color: white; border-radius: 25px; margin-left: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="header">
        <img src="https://cdn-icons-png.flaticon.com/512/3069/3069176.png" alt="Aru">
        <h2>Aru.ai</h2>
    </div>
    <div id="chat"></div>
    <div class="input-area">
        <input type="text" id="userInput" placeholder="Message...">
        <button onclick="sendMessage()">Send</button>
    </div>
    <script>
        async function sendMessage() {
            let input = document.getElementById('userInput');
            let chat = document.getElementById('chat');
            let text = input.value.trim();
            if (text === "") return;
            
            chat.innerHTML += '<div class="msg user">' + text + '</div>';
            input.value = '';
            chat.scrollTop = chat.scrollHeight;
            
            let res = await fetch('/get_reply?msg=' + encodeURIComponent(text));
            let data = await res.json();
            
            chat.innerHTML += '<div class="msg bot">' + data.reply + '</div>';
            chat.scrollTop = chat.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(content=html_content)

@app.get("/get_reply")
async def get_reply(msg: str):
    try:
        # G4F se AI response mang rahe hain
        response = g4f.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": msg}],
        )
        return {"reply": response}
    except Exception as e:
        return {"reply": "Aru abhi connect nahi ho pa rahi... Check logs!"}
