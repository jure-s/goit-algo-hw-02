from queue import Queue
import random
import time
import csv


class QueueSystem:
    def __init__(self, log_file="processed_requests.csv"):
        """Ініціалізація черги, журналу та файлу для збереження."""
        self.queue = Queue()
        self.processed_requests = []  # Журнал оброблених заявок
        self.log_file = log_file
        self.initialize_log_file()

    def initialize_log_file(self):
        """Ініціалізує файл журналу, якщо він не існує."""
        with open(self.log_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["ID заявки", "Час обробки"])  # Заголовки

    def generate_request(self):
        """Генерація нової заявки з унікальним ідентифікатором."""
        request_id = f"REQ-{random.randint(1000, 9999)}"
        self.queue.put(request_id)
        print(f"🔹 Заявка {request_id} додана до черги.")

    def process_request(self):
        """Обробка заявки з черги."""
        if not self.queue.empty():
            request_id = self.queue.get()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            self.processed_requests.append({
                "id": request_id,
                "time": timestamp
            })
            print(f"✅ Заявка {request_id} оброблена.")
        else:
            print("⚠️ Черга пуста.")

    def is_empty(self):
        """Перевіряє, чи пуста черга."""
        return self.queue.empty()

    def queue_size(self):
        """Повертає розмір черги."""
        return self.queue.qsize()

    def show_log(self):
        """Виводить журнал оброблених заявок."""
        print("\n📜 Журнал оброблених заявок:")
        for record in self.processed_requests:
            print(f"  - Заявка {record['id']} оброблена о {record['time']}")

    def save_log_to_file(self):
        """Зберігає журнал оброблених заявок у файл."""
        with open(self.log_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for record in self.processed_requests:
                writer.writerow([record['id'], record['time']])
        print(f"\n💾 Журнал збережено у файл: {self.log_file}")
