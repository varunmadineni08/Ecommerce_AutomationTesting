import logging
import os
from datetime import datetime

def generate_logs():
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)

    log_filename = f"EcommerceSiteAutomation_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    log_filepath = os.path.join(logs_dir, log_filename)

    logger = logging.getLogger("automation_logger")
    logger.setLevel(logging.INFO)

    # Avoid duplicate logs
    if not logger.handlers:
        file_handler = logging.FileHandler(log_filepath, mode='a')
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger






















