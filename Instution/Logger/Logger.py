import logging
logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
logger.setLevel(logging.WARNING)

file_handler = logging.FileHandler("gpr.log")
file_handler.setFormatter('%(asctime)s %(levelname)s %(message)s')
logger.addHandler(file_handler)

# try
# execept
# logger.WARNING(messhae e)