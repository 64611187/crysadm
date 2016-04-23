#! /usr/bin/env python3.4
# -*- coding: utf-8 -*-
# config.py - configration for crysadm web and redis server
__author__ = 'powergx'

# Redis����������
class RedisConfig():
    def __init__(self, host, port, db, password=None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password

# Crysadm ����
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    SESSION_TYPE = 'memcached'
    SECRET_KEY = '1TZCbwsA-pk58-wvSU-IQbL-36IQj0o2GgoV'
    REDIS_CONF = RedisConfig(host='127.0.0.1', port=6379, db=0)
    PASSWORD_PREFIX = "08b3db21-d510-11e4-9ttd-10ddb199c373"
    ENCRYPT_PWD_URL = None
    SERVER_IP = '127.0.0.1'
    SERVER_PORT = 5036

# ��������ʱ����
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

# ����������ģʽ
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

# ����ģʽ
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
