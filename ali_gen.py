import random
import os

def luhn_checksum(card_number):
    digits = [int(x) for x in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for d in even_digits:
        total += sum(divmod(d * 2, 10))
    return total % 10 == 0

def generate_cc(bin_format, count=1):
    generated = []
    for _ in range(count):
        card = bin_format.replace('x', '')
        while len(card) < 15:
            card += str(random.randint(0, 9))
        
        for i in range(10):
            if luhn_checksum(card + str(i)):
                full_card = card + str(i)
                cvv = str(random.randint(100, 999))
                month = str(random.randint(1, 12)).zfill(2)
                year = str(random.randint(2026, 2031))
                generated.append(f"{full_card}|{month}|{year}|{cvv}")
                break
    return generated

def main():
    os.system('clear')
    print("========================================")
    print("      ALI AHMED PRO CC GEN & CHECK      ")
    print("      (Github Ready Edition)            ")
    print("========================================\n")
    
    bin_input = input("Enter BIN (e.g. 515462) or Pattern: ")
    count = int(input("How many cards to generate? (e.g. 100): "))
    
    print("\n[+] Generating and Formatting...")
    cards = generate_cc(bin_input, count)
    
    file_name = "generated_cards.txt"
    with open(file_name, "w") as f:
        for c in cards:
            f.write(c + "\n")
            print(f"VALID FORMAT: {c}")
            
    print(f"\n[!] Success! {count} cards saved to {file_name}")
    print("[!] Use these cards in a Live Checker Gate.")

if __name__ == "__main__":
    main()
