import logging
from datetime import datetime

# Config
logging.basicConfig(
    level=logging.DEBUG,
    # filename="applog.log"
    filename='applog_{:%Y-%m-%d}.log'.format(datetime.now()),
    format='%(asctime)s %(filename)s line %(lineno)d %(message)s'

)
LOGGER = logging.getLogger("PyNhatNghe")

# Ghi log
LOGGER.info('This is INFO')
LOGGER.debug('This is DEBUG')
LOGGER.warning('This is WARNING')
LOGGER.error('This is ERROR')
LOGGER.critical('This is CRITICAL')
try:
    x = 2 / 0
except Exception as ex:
    LOGGER.error(ex)