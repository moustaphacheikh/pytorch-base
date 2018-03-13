
import logging

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s.%(funcName)s : %(message)s',
                              datefmt = '%m/%d/%Y %I:%M:%S %p')

def create_logger(name='__name__', level='DEBUG'):
    """Creates a Root-Level logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger

def get_console_handler(level='DEBUG', formatter=formatter):
    """Creates a Handler for outputting messages to the console
    """
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(level)

    return handler

def get_file_handler(filename, level='DEBUG', formatter):
    """Creates a Handler for outputting messages to a file
    """
    handler = logging.FileHandler(filename)
    handler.setFormatter(formatter)
    handler.setLevel(level)

    return handler
