# coding=utf-8
import logging

# 定义并配置log变量
log = logging.getLogger('vehicle')
log.setLevel(logging.DEBUG)
hdr = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')
hdr.setFormatter(formatter)
log.addHandler(hdr)
