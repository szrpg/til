# -*- config; utf-8 -*-
from logging import getLogger
from logging.config import fileConfig
import os

#fileConfig('logging_config.ini', disable_existing_loggers=False)
#fileConfig(os.path.join(os.getcwd(), 'logging_config.ini'))
fileConfig('logging_config.ini')
logger = getLogger('simpleExample')
logger.debug('TEST')
logger.info('TEST INFO')
