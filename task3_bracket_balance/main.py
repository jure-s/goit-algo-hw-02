from bracket_balance import is_balanced

def main():
    print("📋 Перевірка збалансованості дужок")
    print("Введіть вираз для перевірки. Для виходу введіть 'exit'.\n")

    while True:
        expression = input("👉 Введіть вираз: ")
        if expression.lower() == 'exit':
            print("🚪 Вихід із програми.")
            break

        if is_balanced(expression):
            print("✅ Вираз збалансований!")
        else:
            print("❌ Вираз не збалансований!")

if __name__ == "__main__":
    main()
