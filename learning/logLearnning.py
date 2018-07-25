import logging
import os
import time

# create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 创建一个handler记录日志
rq = time.strftime('%Y%m%d%h%M', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/logs/'
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_name = log_path+ rq + '.log'
log_file = log_name
fh = logging.FileHandler(log_file,mode='w')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.debug("debug")
logger.info('info')
logger.warning("warning")
logger.error("error")
logger.critical("critical")
