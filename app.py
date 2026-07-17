from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# HTML chat interface
html_content = """
<!DOCTYPE html>
<html>
<head><title>Aru AI</title></head>
<body>
    <h1>Hi, I'm Aru! 🤖</h1>
    <div id="chat"></div>
    <input type="text" id="userInput" placeholder="Kuch bolo...">
    <button onclick="sendMessage()">Send</button>

    <script>
        function sendMessage() {
            const input = document.getElementById('userInput').value;
            document.getElementById('chat').innerHTML += '<p>You: ' + input + '</p>';
            // Yahan aage AI ka logic connect karenge
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(content=html_content)
