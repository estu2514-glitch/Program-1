# Aplikasi Game Secret Number - Versi Advanced

import random

def main_game():
    secret_number = 234
    attempts = 0
    max_attempts = 10
    score = 100
    
    print("=" * 50)
    print("🎮 SELAMAT DATANG DI GAME TEBAK ANGKA 🎮")
    print("=" * 50)
    print(f"⚠️  Anda punya {max_attempts} kesempatan untuk menebak!")
    print("Petunjuk: Angka yang dicari adalah angka 3 digit")
    print("=" * 50 + "\n")
    
    while attempts < max_attempts:
        try:
            guess_number = int(input(f"[Percobaan {attempts + 1}/{max_attempts}] Masukkan Tebak Angka: "))
            
            # Validasi input
            if guess_number < 0 or guess_number > 999:
                print("❌ Masukkan angka antara 0-999!\n")
                continue
            
            attempts += 1
            score -= 10
            
            if guess_number == secret_number:
                print("\n" + "=" * 50)
                print("🎉 SELAMAT.. !!, TEBAKAN ANDA BENAR!! 🎉")
                print("=" * 50)
                print(f"✨ Angka rahasia: {secret_number}")
                print(f"📊 Jumlah percobaan: {attempts}")
                print(f"⭐ Skor akhir: {score} poin")
                print("=" * 50 + "\n")
                return True
            
            elif guess_number > secret_number:
                print(f"📍 Tebakan terlalu TINGGI! Coba angka yang lebih kecil.")
                print(f"   Sisa percobaan: {max_attempts - attempts}\n")
            
            else:
                print(f"📍 Tebakan terlalu RENDAH! Coba angka yang lebih besar.")
                print(f"   Sisa percobaan: {max_attempts - attempts}\n")
        
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka saja.\n")
            continue
    
    # Game Over
    print("\n" + "=" * 50)
    print("💀 GAME OVER! KESEMPATAN HABIS!")
    print("=" * 50)
    print(f"😢 Angka rahasia yang benar adalah: {secret_number}")
    print("=" * 50 + "\n")
    return False

# Main Program
if __name__ == "__main__":
    menang = main_game()
    
    while True:
        main_lagi = input("Apakah ingin bermain lagi? (y/n): ").lower()
        if main_lagi == 'y':
            print("\n")
            menang = main_game()
        elif main_lagi == 'n':
            print("\n👋 Terima kasih telah bermain! Sampai jumpa lagi!")
            break
        else:
            print("⚠️  Masukkan 'y' atau 'n'!\n")
