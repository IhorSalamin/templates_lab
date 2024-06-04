import sys
import os
import pandas as pd
import configparser
from abc import ABC, abstractmethod

# Визначення стратегій виводу
class OutputStrategy(ABC):
    @abstractmethod
    def output(self, data):
        pass

class ConsoleOutputStrategy(OutputStrategy):
    def output(self, data):
        print(data)

class KafkaOutputStrategy(OutputStrategy):
    def output(self, data):
        # Тут додайте код для виводу у Kafka
        print("Outputting to Kafka (mock implementation):")
        print(data)

# Функція для зчитування даних з CSV файлу
def read_data_from_csv(file_path):
    df = pd.read_csv(file_path, header=None)  # Читання CSV без заголовків
    return df

# Функція для отримання стратегії виводу з конфігураційного файлу
def get_output_strategy(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    output_type = config['OUTPUT']['Type']
    
    if output_type == 'console':
        return ConsoleOutputStrategy()
    elif output_type == 'kafka':
        return KafkaOutputStrategy()
    else:
        raise ValueError(f"Unknown output type: {output_type}")

# Функція для обробки і виводу даних
def process_and_output_data(file_path, output_strategy: OutputStrategy):
    data = read_data_from_csv(file_path)
    output_strategy.output(data)

# Головна функція
def main():
    file_path = 'backend/data.csv'
    output_strategy = get_output_strategy()
    process_and_output_data(file_path, output_strategy)

if __name__ == "__main__":
    main()
