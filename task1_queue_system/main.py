from queue_system import QueueSystem
import time
import random

def main():
    system = QueueSystem()

    print("📥 Система обробки заявок запущена.")
    print("Натисніть Ctrl+C, щоб зупинити програму.")

    try:
        while True:
            # Імітуємо генерацію нових заявок частіше, ніж обробку
            for _ in range(random.randint(1, 3)):  # Генеруємо 1-3 заявки
                system.generate_request()
            
            time.sleep(2)  # Затримка для імітації надходження заявок
            
            # Обробляємо заявки
            for _ in range(random.randint(1, 2)):  # Обробляємо 1-2 заявки
                system.process_request()

            print(f"📊 Поточний розмір черги: {system.queue_size()}")
            time.sleep(2)  # Затримка для імітації роботи
            
    except KeyboardInterrupt:
        print("\n🚪 Система завершила роботу.")
        system.show_log()
        system.save_log_to_file()

if __name__ == "__main__":
    main()
