import logging

# Set name of log
logging.getLogger("PyNhatNghe")

# Setup log
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d: %(message)s"
)

# Ghi log
logging.info("Hello info log")
logging.debug("Debug log")
logging.warning("Warning log")
logging.error("Eror log")
logging.critical("CRITICAL log")
