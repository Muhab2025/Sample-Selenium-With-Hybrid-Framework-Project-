import logging

def generate_logs():
    logger = logging.getLogger()
    file_handler = logging.FileHandler(".\\logs\\sample_selenium_hybrid.log", mode='w')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger