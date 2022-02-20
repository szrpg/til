from logging import getLogger, Formatter, FileHandler, INFO

logger = getLogger(__name__)
logger.setLevel(INFO)
fh = FileHandler('test.log')
fmt = Formatter('%(asctime)s %(message)s')
fh.setFormatter(fmt)
fh.setLevel(INFO)
logger.addHandler(fh)


logger.info('test')
