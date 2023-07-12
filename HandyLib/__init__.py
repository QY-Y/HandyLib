import time
import sys
import logging
import socket
import logging.handlers
name = "HandyLib"


def get_logger(level='info', test_flag=False,
               filename='',
               maxsize=1024*1024*3,
               backup_num=5, encoding='utf-8', print_to_cmd=False,file_logger=True):
    '''
    ruturns a logger, 
    if test_flag is True or level is set to logging.DEBUG,
    it will output to terminal
    '''
    level = level.upper()
    if level == 'INFO':
        level = logging.INFO
    elif level == 'WARNING' or level == 'WARN':
        level = logging.WARNING
    elif level == 'ERROR' or level == 'ERR':
        level = logging.ERROR
    elif level == 'DEBUG':
        level = logging.DEBUG
    else:
        print('unknown logging level:{level}')
    if filename == '':
        temp = sys.argv[0].split('.')
        temp = temp[:-1]
        filename = '.'.join(temp) + '.log'

    logger = logging.getLogger()
    f = logging.Formatter(
        "[%(asctime)s] [%(filename)s:%(lineno)s-%(funcName)s] [%(levelname)s] %(message)s")    # output format
    if file_logger:
        fh = logging.handlers.RotatingFileHandler(
            filename, maxBytes=maxsize, backupCount=backup_num, encoding=encoding)
        fh.setFormatter(f)
        logger.addHandler(fh)
    if print_to_cmd or level == logging.DEBUG:
    #     # output to standard output
        sh = logging.StreamHandler(stream=sys.stdout)
        sh.setFormatter(f)
        logger.addHandler(sh)
    logger.setLevel(level)
    return logger


def time_this(fn):
    def wrap(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        print('[{0}] took {1:.10f} seconds'.format(
            fn.__name__, time.time() - start))
    return wrap


def get_hostname():
    
    return socket.gethostname()
