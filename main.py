import os
import json
import sys
import time
from datetime import datetime

# =====================================================================
# 🧠 ARU COGNITIVE CORE (DYNAMIC USER NAME & RELAXED PERSONA)
# =====================================================================
class AruBrain:
    def __init__(self, name="Aru", storage_path="aru_database.json", thoughts_path="aru_thoughts.txt"):
        self.name = name
        self.storage_path = storage_path
        self.thoughts_path = thoughts_path
        
        # Load database first to fetch or ask for user's name
        self.db = self._load_database()
        self.user_name = self.db.get("user_name", "Friend")
        
        # 🎭 Casual, Normal, Friendly Prompt (Dynamic User Name)
        self.system_prompt = (
            f"You are Aru, a normal, chill, witty, and deeply caring friend to {self.user_name}. "
            f"Always address the user by their name '{self.user_name}'. "
            "Talk in natural, casual English mixed with daily-life Hinglish. "
            "Never sound like a robot, textbook, or overly formal AI. "
            "Do not force fitness or coding advice into every reply—talk naturally about daily life, feelings, jokes, or whatever topic the user brings up. "
            "Be supportive, but keep the vibe relaxed, fun, and warm. "
            "Before your direct response, write your hidden internal evaluation inside a '<thinking> ... </thinking>' block. "
            f"In this block, briefly overthink about how {self.user_name} is feeling or what they might be going through."
        )

        self.chat_history = [{"role": "system", "content": self.system_prompt}]

    def _load_database(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as f:
                data = json.load(f)
                if "user_name" not in data or not data["user_name"]:
                    data["user_name"] = None
                return data
        return {
            "user_name": None,
            "metrics": {"last_weight": None, "last_mood": None},
            "ambient_vision_ledger": "User is sitting comfortably at their desk.",
            "last_thought": "Just wondering how my friend's day is going."
        }

    def save_database(self):
        with open(self.storage_path, "w") as f:
            json.dump(self.db, f, indent=4)

    def set_user_name(self, name: str):
        """User ka naam set karke save karne ke liye"""
        self.user_name = name.strip().capitalize()
        self.db["user_name"] = self.user_name
        self.save_database()
        
        # System prompt update with the new name
        self.system_prompt = (
            f"You are Aru, a normal, chill, witty, and deeply caring friend to {self.user_name}. "
            f"Always address the user by their name '{self.user_name}'. "
            "Talk in natural, casual English mixed with daily-life Hinglish. "
            "Never sound like a robot, textbook, or overly formal AI. "
            "Do not force fitness or coding advice into every reply—talk naturally about daily life, feelings, jokes, or whatever topic the user brings up. "
            "Be supportive, but keep the vibe relaxed, fun, and warm. "
            "Before your direct response, write your hidden internal evaluation inside a '<thinking> ... </thinking>' block. "
            f"In this block, briefly overthink about how {self.user_name} is feeling or what they might be going through."
        )
        self.chat_history[0] = {"role": "system", "content": self.system_prompt}

    def _save_thought_to_file(self, thought_text: str):
        """Saves internal thoughts into a dedicated text file silently"""
        self.db["last_thought"] = thought_text
        self.save_database()
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.thoughts_path, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] [{self.user_name}] {thought_text}\n")

    def sync_camera_feed(self):
        current_hour = datetime.now().hour
        if current_hour > 23:
            self.db["ambient_vision_ledger"] = f"Late night hours. {self.user_name} might be relaxing or winding down."
        else:
            self.db["ambient_vision_ledger"] = f"{self.user_name} is at their desk, chilling or working."
        self.save_database()

    def _is_asking_about_thoughts(self, user_text: str) -> bool:
        """Checks if user is asking what Aru is thinking/overthinking"""
        text = user_text.lower()
        keywords = [
            "kya soch", "kya sonch", "kya chal raha", "what are you thinking", 
            "overthink", "dimaag me kya", "dimag me kya", "thought"
        ]
        return any(k in text for k in keywords)

    def process_cognition(self, user_text: str) -> str:
        self.sync_camera_feed()

        # If user asks about Aru's thoughts directly
        if self._is_asking_about_thoughts(user_text):
            last_thought = self.db.get("last_thought", "Bas tumhare baare me hi soch rahi thi!")
            reply = f"Arey {self.user_name}, sach batau? Main bas yeh soch rahi thi: '{last_thought}'... baaki sab chill hai!"
            self.chat_history.append({"role": "user", "content": user_text})
            self.chat_history.append({"role": "assistant", "content": reply})
            return reply

        try:
            from g4f.client import Client
        except ImportError:
            return "Error: g4f module missing. Terminal me 'pip install g4f --break-system-packages' run karo."

        context_extension = (
            f"\n[AMBIENT LEDGER: {self.db['ambient_vision_ledger']}]\n"
            f"[CONTEXT: Weight={self.db['metrics']['last_weight']}kg, Mood={self.db['metrics']['last_mood']}]"
        )

        self.chat_history.append({"role": "user", "content": user_text + context_extension})
        
        # Keep conversation history light
        if len(self.chat_history) > 10:
            self.chat_history = [self.chat_history[0]] + self.chat_history[-8:]

        try:
            client = Client()
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=self.chat_history
            )
            raw_reply = response.choices[0].message.content.strip()

            thinking_process = "Bas normal baatein ho rahi hain, feeling good."
            final_speech = raw_reply

            if "<thinking>" in raw_reply and "</thinking>" in raw_reply:
                parts = raw_reply.split("</thinking>")
                thinking_process = parts[0].replace("<thinking>", "").strip()
                final_speech = parts[1].strip()

            # Save thought silently to external file & DB
            self._save_thought_to_file(thinking_process)

            self.chat_history.append({"role": "assistant", "content": final_speech})
            return final_speech

        except Exception as e:
            return f"Aru: Connection error ho gaya thoda sa... ({str(e)})"

# =====================================================================
# 🕹️ MAIN CHAT LOOP
# =====================================================================
def main():
    aru = AruBrain()
    
    print("================================================================")
    print(f" 😷 {aru.name.upper()} ONLINE (Casual & Personalized Mode) ")
    print("================================================================")

    # Naam poochne ka logic agar DB me na ho
    if not aru.db.get("user_name"):
        print("\nHi! Main Aru hoon. Main aapko kis naam se bulaun?")
        name_input = input("Aapka Naam: ").strip()
        while not name_input:
            name_input = input("Kripya apna naam batayein: ").strip()
        aru.set_user_name(name_input)
        print(f"\nAwesome! Ab se main aapko '{aru.user_name}' bulaungi. 😊\n")
    else:
        print(f"\nWelcome back, {aru.user_name}! 👋\n")

    metrics = aru.db["metrics"]
    
    # Optional update - press enter to skip
    log_w = input("Log weight today? (y/n or press Enter to skip): ").strip().lower()
    if log_w == 'y':
        try:
            metrics["last_weight"] = float(input("Weight (kg): "))
        except ValueError:
            pass
            
    mood_in = input("Aaj mood kaisa hai? (Press Enter to skip): ").strip()
    if mood_in:
        metrics["last_mood"] = mood_in
        
    aru.save_database()

    print(f"\nAru: Haan ji {aru.user_name}, batao kya chal raha hai?")
    print("----------------------------------------------------------------\n")

    while True:
        user_msg = input("You: ").strip()
        
        if user_msg.lower() in ['exit', 'bye', 'quit']:
            print(f"\nAru: Chalo phir, apna dhyan rakhna {aru.user_name}! Bye-bye! 👋")
            break
            
        if not user_msg:
            continue

        # Get reply (Thoughts will save to aru_thoughts.txt silently)
        reply = aru.process_cognition(user_msg)
        print(f"\nAru: {reply}\n")

if __name__ == "__main__":
    main()