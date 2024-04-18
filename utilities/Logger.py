import logging
import inspect

class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)   #### loging tu logger ko leke ayo
        logfile = logging.FileHandler("C:\\Users\\nikhi\\PycharmProjects\\CredeKart_Pytest_Project\\Logs\\CredKart.log")
        log_format = logging.Formatter("%(asctime)s : %(name)s : %(funcName)s : %(lineno)s :%(message)s : %(levelname)s")
        logfile.setFormatter(log_format)       #### FoRAMT
        logger.addHandler(logfile)     ### ACTIVITY ADD  FILE


        logger.setLevel(logging.INFO)     # when select then start from
        # logger.setLevel(logging.CRITICAL)
        return logger

######## Level Of Logs

#Debug
#Info
#warning
#error
#Critical
