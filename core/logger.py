# -*- coding: utf-8 -*-
# @Author    : Evescn
# @time      : 2020/11/18 10:06
# @File      : logger.py
# @Software  : PyCharm

import logging
from conf import setting


def logger(log_type):

    logger = logging.getLogger(log_type)
    logger.setLevel(setting.LOG_LEVEL)

    ch = logging.StreamHandler()
    ch.setLevel(setting.LOG_LEVEL)

    # log_file = "%s/log/%s" % (setting.BASE_DIR, setting.LOG_TYPES[log_type])
    # fh = logging.StreamHandler(log_file)
    # fh.setLevel(setting.Log_LEVEL)

    # create file handler and set level to warning
    log_file = "%s/log/%s" % (setting.BASE_DIR, setting.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(setting.LOG_LEVEL)



    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # logger.addHandler(ch)
    logger.addHandler(fh)

    return logger