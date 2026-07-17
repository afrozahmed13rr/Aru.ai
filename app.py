from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: sans-serif; background-color: #fff; margin: 0; display: flex; justify-content: center; }
        .header { position: fixed; top: 0; width: 100%; max-width: 400px; background-color: #fafafa; border-bottom: 1px solid #dbdbdb; display: flex; align-items: center; padding: 10px 15px; }
        .header img { width: 40px; height: 40px; border-radius: 50%; margin-right: 10px; border: 2px solid #ff8a8a; }
        #chat { padding-top: 70px; padding-bottom: 80px; width: 100%; max-width: 400px; }
        .message { margin: 10px 15px; padding: 10px 15px; border-radius: 20px; font-size: 14px; max-width: 70%; }
        .aru-message { background-color: #efefef; align-self: flex-start; }
        .user-message { background: #007bff; color: #fff; align-self: flex-end; margin-left: auto; }
        .input-area { position: fixed; bottom: 0; width: 100%; max-width: 400px; background-color: #fff; border-top: 1px solid #dbdbdb; padding: 10px; display: flex; }
        input { flex-grow: 1; padding: 10px; border-radius: 20px; border: 1px solid #dbdbdb; outline: none; }
        button { background: none; border: none; color: #0095f6; font-weight: bold; margin-left: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="header">
        <img src="https://i.imgur.com/8KQ383X.png" alt="Aru">
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
                chat.innerHTML += '<div class="message user-message">' + input.value + '</div>';
                chat.innerHTML += '<div class="message aru-message">Aru abhi online ho rahi hai... ✨</div>';
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
