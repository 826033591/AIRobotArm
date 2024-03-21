import logging
import os
import settings

# 检查并创建日志文件目录
log_directory = os.path.dirname(settings.LOGGING['filename'])
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# 配置日志系统
logging.basicConfig(level=getattr(logging, settings.LOGGING['level']),
                    format=settings.LOGGING['format'],
                    datefmt=settings.LOGGING['datefmt'],
                    filename=settings.LOGGING['filename'],
                    filemode=settings.LOGGING['filemode'],
                    encoding='utf-8')

def get_logger(name):
    """
    提供一个获取已配置日志记录器的函数。
    """
    return logging.getLogger(name)
if __name__ == '__main__':
    logger = get_logger('test_logger')
    logger.debug('这是一条debug信息')
    logger.info('这是一条info信息')
    logger.warning('这是一条warning信息')
    logger.error('这是一条error信息')
    logger.critical('这是一条critical信息')