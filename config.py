class Config(object):
    TESTING = False
    DEBUG = False

class DevelopmentConfig(Config):
        DEBUG = True


class ProductionConfig(Config):

    DEBUG = False
    TESTING = False

class TestingConfig(Config):

    DEBUG = True
    TESTING = True

        