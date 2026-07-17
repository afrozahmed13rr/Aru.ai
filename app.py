from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: 'Arial', sans-serif; background-color: #fce4ec; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .chat-container { background: #ffffff; padding: 20px; border-radius: 30px; box-shadow: 0 10px 20px rgba(255, 182, 193, 0.5); width: 90%; max-width: 400px; text-align: center; border: 2px solid #ffb6c1; }
        .angel-icon { width: 120px; height: 120px; border-radius: 50%; border: 3px solid #ffb6c1; margin-bottom: 10px; }
        #chat { height: 200px; overflow-y: auto; border: 1px solid #f8bbd0; padding: 10px; margin-bottom: 10px; border-radius: 15px; text-align: left; background-color: #fff5f7; }
        input { width: 60%; padding: 10px; border-radius: 20px; border: 2px solid #ffb6c1; }
        button { padding: 10px 20px; background: #ffb6c1; border: none; border-radius: 20px; color: white; cursor: pointer; }
    </style>
</head>
<body>
    <div class="chat-container">
        <!-- Maine direct link use kiya hai jo kaam karega -->
        <img src="https://i.imgur.com/gK96eWJ.png" class="angel-icon" alt="Aru">
        <h2>Aru AI</h2>
        <div id="chat"></div>
        <input type="text" id="userInput" placeholder="Kuch likho...">
        <button onclick="sendMessage()">Send</button>
    </div>
    <script>
        function sendMessage() {
            let input = document.getElementById('userInput');
            let chat = document.getElementById('chat');
            if(input.value.trim() !== "") {
                chat.innerHTML += '<p><b>You:</b> ' + input.value + '</p>';
                chat.innerHTML += '<p><b>Aru:</b> Main abhi seekh rahi hoon! ✨</p>';
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
