import os
import subprocess

def run_task(task_number):
    """Запускає обране завдання."""
    tasks = {
        "1": "task1_queue_system/main.py",
        "2": "task2_palindrome_check/main.py",
        "3": "task3_bracket_balance/main.py"
    }
    if task_number in tasks:
        try:
            subprocess.run(f"python {tasks[task_number]}", shell=True, check=True)
        except KeyboardInterrupt:
            print("\n⏹ Завдання перервано користувачем.")
    else:
        print("❌ Невірний номер завдання. Введіть 1, 2 або 3.")

def main():
    print("📋 Запуск завдань")
    print("1: Система обробки заявок")
    print("2: Перевірка паліндромів")
    print("3: Перевірка збалансованості дужок")
    print("exit: Вийти з програми")

    while True:
        try:
            choice = input("\n👉 Виберіть завдання (1, 2, 3) або 'exit': ")
            if choice.lower() == "exit":
                print("🚪 Вихід із програми.")
                break
            run_task(choice)
        except KeyboardInterrupt:
            print("\n🚪 Вихід із програми.")
            break

if __name__ == "__main__":
    main()
