from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; background: #fff; }
        .header { display: flex; align-items: center; padding: 15px; border-bottom: 1px solid #eee; }
        .header img { width: 40px; height: 40px; margin-right: 12px; }
        #chat { flex: 1; overflow-y: auto; padding: 15px; display: flex; flex-direction: column; }
        .msg { padding: 12px 16px; margin: 6px 0; border-radius: 18px; max-width: 75%; font-size: 15px; }
        .user { align-self: flex-end; background: #007bff; color: white; border-bottom-right-radius: 4px; }
        .bot { align-self: flex-start; background: #f1f0f0; color: black; border-bottom-left-radius: 4px; }
        
        /* Input area fix: Thoda upar aur bada */
        .input-area { 
            display: flex; padding: 15px; background: #fff; 
            border-top: 1px solid #eee; align-items: center;
            position: sticky; bottom: 0; z-index: 10;
        }
        input { flex: 1; padding: 14px; border: 1px solid #ddd; border-radius: 25px; outline: none; font-size: 16px; }
        button { padding: 12px 20px; border: none; background: #007bff; color: white; border-radius: 25px; margin-left: 10px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>
    <div class="header">
        <img src="https://cdn-icons-png.flaticon.com/512/3069/3069176.png" alt="Aru">
        <h2>Aru.ai</h2>
    </div>
    <div id="chat"></div>
    <div class="input-area">
        <input type="text" id="userInput" placeholder="Message..." onkeypress="handleEnter(event)">
        <button onclick="sendMessage()">Send</button>
    </div>
    <script>
        function sendMessage() {
            let input = document.getElementById('userInput');
            let chat = document.getElementById('chat');
            if (input.value.trim() === "") return;
            chat.innerHTML += '<div class="msg user">' + input.value + '</div>';
            input.value = '';
            chat.scrollTop = chat.scrollHeight;
            
            // Bot simulation reply
            setTimeout(() => {
                chat.innerHTML += '<div class="msg bot">Main abhi seekh rahi hoon! ✨</div>';
                chat.scrollTop = chat.scrollHeight;
            }, 600);
        }
        function handleEnter(e) { if (e.key === 'Enter') sendMessage(); }
    </script>
</body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(content=html_content)
