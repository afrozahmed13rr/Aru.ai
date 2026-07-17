from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import g4f
import sqlite3

app = FastAPI()

# Database setup
def init_db():
    conn = sqlite3.connect("aru_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS history (user TEXT, chat TEXT)")
    conn.commit()
    conn.close()

init_db()

@app.get("/", response_class=HTMLResponse)
async def get():
    return """
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1.0"><style>
    body{font-family:sans-serif; text-align:center; padding-top:50px;}
    input{padding:10px; border-radius:10px; border:1px solid #ccc; width:80%;}
    button{padding:10px 20px; background:#007bff; color:white; border:none; border-radius:10px; margin-top:10px;}
    </style></head>
    <body>
        <h2>Login to Aru.ai</h2>
        <form method="post" action="/chat">
            <input type="text" name="username" placeholder="Apna naam likho..." required><br>
            <button type="submit">Login</button>
        </form>
    </body></html>
    """

@app.post("/chat", response_class=HTMLResponse)
async def chat_interface(username: str = Form(...)):
    return f"""
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{{font-family:sans-serif; margin:0; display:flex; flex-direction:column; height:100vh;}}
        #chat{{flex:1; overflow-y:auto; padding:20px;}}
        .msg{{padding:10px; margin:5px; border-radius:10px; background:#eee;}}
        .input-area{{padding:20px; border-top:1px solid #ccc; display:flex;}}
    </style></head>
    <body>
        <div id="chat"><p>Welcome {username}! Aru is ready.</p></div>
        <div class="input-area">
            <input type="text" id="msg" placeholder="Message...">
            <button onclick="sendMsg('{username}')">Send</button>
        </div>
        <script>
            async function sendMsg(user) {{
                let m = document.getElementById('msg').value;
                document.getElementById('chat').innerHTML += '<div class="msg">You: '+m+'</div>';
                let res = await fetch('/get_reply?user='+user+'&msg='+encodeURIComponent(m));
                let data = await res.json();
                document.getElementById('chat').innerHTML += '<div class="msg">Aru: '+data.reply+'</div>';
                document.getElementById('msg').value = '';
            }}
        </script>
    </body></html>
    """

@app.get("/get_reply")
async def get_reply(user: str, msg: str):
    # Data save in SQLite
    conn = sqlite3.connect("aru_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history VALUES (?, ?)", (user, msg))
    conn.commit()
    conn.close()
    
    # AI Logic
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "You are Aru, a helpful friend. Keep responses short."},
                      {"role": "user", "content": msg}]
        )
        return {"reply": response}
    except:
        return {"reply": "Aru abhi busy hai!"}
