from palindrome_check import is_palindrome

def main():
    print("📋 Перевірка паліндромів")
    print("Введіть рядки для перевірки. Для виходу введіть 'exit'.\n")

    while True:
        user_input = input("👉 Введіть рядок: ")
        if user_input.lower() == 'exit':
            print("🚪 Вихід із програми.")
            break
        
        if is_palindrome(user_input):
            print("✅ Цей рядок є паліндромом!")
        else:
            print("❌ Цей рядок не є паліндромом.")

if __name__ == "__main__":
    main()
