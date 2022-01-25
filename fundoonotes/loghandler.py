import logging

logger = logging

# logging basic config method and saving log files
logger.basicConfig(filename='fundoonotes.log', level=logging.INFO,filemode="w",
                   format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger.basicConfig(filename='fundoonotes.log', level=logging.ERROR,filemode="w",
                   format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineno)s')