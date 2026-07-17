from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; background: #fff; }
        .header { display: flex; align-items: center; padding: 15px; border-bottom: 1px solid #ddd; }
        .header img { width: 40px; height: 40px; margin-right: 10px; }
        #chat { flex: 1; overflow-y: auto; padding: 15px; display: flex; flex-direction: column; }
        .msg { padding: 10px; margin: 5px; border-radius: 15px; max-width: 80%; }
        .user { align-self: flex-end; background: #007bff; color: white; }
        .bot { align-self: flex-start; background: #eee; }
        .input-area { display: flex; padding: 10px; border-top: 1px solid #ddd; }
        input { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 20px; outline: none; }
        button { padding: 10px 20px; border: none; background: #007bff; color: white; border-radius: 20px; margin-left: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="header">
        <img src="https://cdn-icons-png.flaticon.com/512/3069/3069176.png" alt="Icon">
        <h2>Aru.ai</h2>
    </div>
    <div id="chat"></div>
    <div class="input-area">
        <input type="text" id="userInput" placeholder="Kuch likho...">
        <button onclick="sendMessage()">Send</button>
    </div>
    <script>
        function sendMessage() {
            let input = document.getElementById('userInput');
            let chat = document.getElementById('chat');
            if (input.value.trim() === "") return;
            
            // User message
            chat.innerHTML += '<div class="msg user">' + input.value + '</div>';
            
            // Bot reply
            setTimeout(() => {
                chat.innerHTML += '<div class="msg bot">Main abhi seekh rahi hoon! ✨</div>';
                chat.scrollTop = chat.scrollHeight;
            }, 500);
            
            input.value = '';
            chat.scrollTop = chat.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(content=html_content)
