import logging
import os
from datetime import datetime

def generate_logs():
    logs_dir = "logs"      #This defines the folder name where all your log files will be stored.
    os.makedirs(logs_dir, exist_ok=True)#This creates the "logs" directory if it doesn’t already exist.exist_ok=True prevents errors if the folder already exists

    log_filename = f"EcommerceSiteAutomation_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    log_filepath = os.path.join(logs_dir, log_filename) #This creates the full path to your log file.

    logger = logging.getLogger("automation_logger") #A named logger is useful in large projects or frameworks because it:Can be reused across files.Can be configured independently of other loggers (like the root logger).
    logger.setLevel(logging.INFO) #This sets the minimum level of log messages the logger will handle.

    # Avoid duplicate logs
    if not logger.handlers:  #“If this logger doesn't already have any handlers, then add one.”
        file_handler = logging.FileHandler(log_filepath, mode='a')#This creates a file handler, which writes log messages to a file.
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)  #Tells the handler: “Use this format when writing logs to the file.”
        logger.addHandler(file_handler) #Attaches the file_handler to the logger.

    return logger






















