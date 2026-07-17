from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #fce4ec; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .chat-container { background: #ffffff; padding: 25px; border-radius: 30px; box-shadow: 0 10px 20px rgba(255, 182, 193, 0.5); width: 90%; max-width: 400px; text-align: center; border: 2px solid #ffb6c1; }
        .angel-icon { width: 150px; height: 150px; border-radius: 50%; border: 4px solid #ffb6c1; margin-bottom: 15px; object-fit: cover; }
        h2 { color: #d81b60; margin-bottom: 20px; font-family: cursive; }
        #chat { height: 200px; overflow-y: auto; border: 1px solid #f8bbd0; padding: 15px; margin-bottom: 15px; border-radius: 15px; text-align: left; background-color: #fff5f7; }
        input { width: 65%; padding: 12px; border-radius: 20px; border: 2px solid #ffb6c1; outline: none; }
        button { padding: 12px 20px; background: #ffb6c1; border: none; border-radius: 20px; color: white; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="chat-container">
        <img src="https://i.imgur.com/rCXGGG6.jpeg" class="angel-icon" alt="Aru Angel">
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
