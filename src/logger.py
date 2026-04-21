import logging
from datetime import datetime
import sys
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

class BotLogger:
    @staticmethod
    def get_logger(name="Bot"):
        logger = logging.getLogger(name)
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            log_dir_ = ROOT_DIR / "data" / "logs"
            filename_ = f"bot_{datetime.now().strftime('%Y-%m-%d')}.log"

            log_dir_.mkdir(parents=True, exist_ok=True)

            file_name = os.path.join(log_dir_, filename_) #f"data/logs/bot_{datetime.now().strftime('%Y-%m-%d')}.log"
            file_handler = logging.FileHandler(file_name, encoding='utf-8')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger