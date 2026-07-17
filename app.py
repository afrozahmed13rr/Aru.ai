# app.py mein ye HTML wala section replace karo:
html_content = """
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; }
        #chat { flex: 1; overflow-y: auto; padding: 20px; padding-bottom: 80px; } /* Bottom padding zaroori hai */
        .msg { padding: 10px; margin: 5px; border-radius: 10px; background: #eee; }
        .input-area { 
            position: fixed; bottom: 0; width: 100%; padding: 15px; 
            background: white; border-top: 1px solid #ccc; display: flex; 
            box-sizing: border-box; /* Isse box screen se bahar nahi jayega */
        }
        input { flex: 1; padding: 10px; border-radius: 10px; border: 1px solid #ccc; }
        button { padding: 10px 20px; margin-left: 10px; background: #007bff; color: white; border: none; border-radius: 10px; }
    </style>
</head>
<body>
    <div id="chat"><p>Welcome Ruba! Aru is ready.</p></div>
    <div class="input-area">
        <input type="text" id="msg" placeholder="Message...">
        <button onclick="sendMsg('Ruba')">Send</button>
    </div>
    <script>
        async function sendMsg(user) {
            let m = document.getElementById('msg');
            let chat = document.getElementById('chat');
            if(m.value.trim() === "") return;
            
            chat.innerHTML += '<div class="msg">You: '+m.value+'</div>';
            let val = m.value;
            m.value = '';
            
            let res = await fetch('/get_reply?user='+user+'&msg='+encodeURIComponent(val));
            let data = await res.json();
            
            chat.innerHTML += '<div class="msg">Aru: '+data.reply+'</div>';
            chat.scrollTop = chat.scrollHeight; // Auto-scroll niche ke liye
        }
    </script>
</body>
</html>
"""
