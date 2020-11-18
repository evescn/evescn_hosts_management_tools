# -*- coding: utf-8 -*-
# @Author    : Evescn
# @time      : 2020/11/17 15:29
# @File      : setting.py
# @Software  : PyCharm

import os
import logging
from core import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_LEVEL = logging.INFO

# LOG_TYPES

LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

# transaction logger
trans_logger = logger.logger('transaction')

# access logger
access_logger = logger.logger('access')

