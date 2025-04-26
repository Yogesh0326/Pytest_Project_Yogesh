import logging

class Log_Maker:
    @staticmethod
    def log_gen():   # below line add path of file inside which we want to store the logs with date and time format
        logging.basicConfig(filename=".\\logs\\testcases.log", format="%(asctime)s - %(levelname)s - %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S", force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)   # set the level of logger as INFO
        return logger