import time
import os
import logging
from logging.handlers import TimedRotatingFileHandler

class SetLogs:
    def __init__(self) -> None:        
        # Установка пути к директории с лог-файлами
        logs_dir = os.path.join(os.path.curdir, 'logs')
        os.makedirs(logs_dir, exist_ok=True)

        # Определение текущей даты
        current_date = time.strftime("%Y-%m-%d", time.localtime())

        # Настройка формата записей лога
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
        date_format = "%Y-%m-%d %H:%M:%S"

        # Настройка файла для записи логов
        log_file = os.path.join(logs_dir, f"app_{current_date}.log")

        # Настройка уровня логирования
        log_level = logging.INFO # Выбор нужного уровня логирования (INFO, WARNING, ERROR, CRITICAL)

        # Создание и настройка объекта логирования
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        handler = TimedRotatingFileHandler(log_file, when="midnight")
        handler.setFormatter(logging.Formatter(log_format, datefmt=date_format))
        self.logger.addHandler(handler)