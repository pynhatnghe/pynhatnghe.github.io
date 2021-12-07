import logging
from datetime import datetime

# Set name of log
logging.getLogger("PyNhatNghe")

# Setup log
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d: %(message)s",
    filename='app_{:%Y_%m_%d}.log'.format(datetime.utcnow())
)

# Ghi log
logging.debug("Debug log")
logging.info("Hello info log")
logging.warning("Warning log A")
logging.error("Eror log")
logging.critical("CRITICAL log")
