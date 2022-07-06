import logging
import time
from logging.handlers import RotatingFileHandler


def create_rotating_log(path):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    # add a rotating handler
    handler = RotatingFileHandler(
        path,
        maxBytes=20, # file log tối đa 20bytes
        backupCount=5 # Ngoài file log đang chạy lấy 5 file log gần nhất
    )
    logger.addHandler(handler)

    for i in range(10):
        logger.info("This is test log line %s" % i)
        time.sleep(1.5)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "test.log"
    create_rotating_log(log_file)