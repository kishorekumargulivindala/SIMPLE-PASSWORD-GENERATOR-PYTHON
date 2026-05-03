import random
import string

print("=== 🔐 PASSWORD GENERATOR ===")

length = int(input("Enter length: "))

print("\nSelect options (y/n):")
use_letters = input("Letters? (y/n): ").lower()
use_digits = input("Digits? (y/n): ").lower()
use_symbols = input("Symbols? (y/n): ").lower()

pool = ""

if use_letters == "y":
    pool += string.ascii_letters
if use_digits == "y":
    pool += string.digits
if use_symbols == "y":
    pool += string.punctuation

if pool == "":
    print("❌ Select at least one option!")
    exit()

password = "".join(random.choice(pool) for _ in range(length))

print("\n✅ Password:", password)