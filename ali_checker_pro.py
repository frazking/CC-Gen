import requests
import time
import os

# --- CC GEN | LIV BIN (PRO CHECKER) ---

def check_card(card_data, sk_key):
    try:
        p = card_data.split('|')
        if len(p) < 4: return f"⚠️ Format Error: {card_data}"
        
        num, mon, year, cvv = p[0], p[1], p[2], p[3]
        if len(year) == 2: year = "20" + year

        url = "https://api.stripe.com/v1/payment_methods"
        headers = {
            "Authorization": f"Bearer {sk_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "type": "card",
            "card[number]": num,
            "card[exp_month]": mon,
            "card[exp_year]": year,
            "card[cvc]": cvv,
        }

        response = requests.post(url, headers=headers, data=data).json()

        if "id" in response:
            return f"\033[92m✅ LIVE | {card_data} | ID: {response['id']}\033[0m"
        elif "error" in response:
            msg = response['error'].get('message', 'Declined')
            return f"\033[91m❌ DEAD | {card_data} | {msg}\033[0m"
        else:
            return f"\033[93m⚠️ UNKNOWN | {card_data}\033[0m"

    except Exception as e:
        return f"\033[91m🚫 ERROR | {str(e)}\033[0m"

def main():
    print("\033[94m" + "="*40)
    print("      CC GEN | LIV BIN - PRO CHECKER")
    print("="*40 + "\033[0m")
    
    # Key yahan input karni hogi, file mein save nahi hogi
    sk_input = input("[?] Enter your Secret Key (sk_live_...): ").strip()
    file_name = input("[?] Enter card list file (e.g., cards.txt): ").strip()
    
    if not os.path.exists(file_name):
        print("[-] File nahi mili!")
        return

    with open(file_name, 'r') as f:
        cards = f.read().splitlines()
    
    print(f"\n[!] Total Cards: {len(cards)}\n")
    
    for card in cards:
        if '|' in card:
            print(check_card(card, sk_input))
            time.sleep(1) # IP Safety

if __name__ == "__main__":
    main()
