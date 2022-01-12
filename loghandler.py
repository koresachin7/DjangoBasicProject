import logging

logger = logging

# logging basic config method and saving log files
logger.basicConfig(filename='addressbook.log', level=logging.INFO,
                   format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger.basicConfig(filename='addressbook.log', level=logging.ERROR,
                   format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)s')