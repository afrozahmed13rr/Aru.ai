from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { font-family: -apple-system, sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; background: #fff; }
        .header { display: flex; align-items: center; padding: 10px; border-bottom: 1px solid #eee; }
        .header img { width: 40px; height: 40px; border-radius: 50%; margin-right: 10px; }
        #chat { flex: 1; overflow-y: auto; padding: 10px; }
        .input-area { display: flex; padding: 10px; border-top: 1px solid #eee; background: #fff; }
        input { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 20px; outline: none; }
        button { margin-left: 10px; border: none; background: none; color: #0095f6; font-weight: bold; }
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
        function sendMessage() {
            const input = document.getElementById('userInput');
            const chat = document.getElementById('chat');
            if (input.value.trim() !== "") {
                chat.innerHTML += '<div style="margin:5px; text-align:right;">' + input.value + '</div>';
                input.value = '';
                chat.scrollTop = chat.scrollHeight;
            }
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(content=html_content)
