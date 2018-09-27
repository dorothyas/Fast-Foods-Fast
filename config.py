class Config(object):

    class DevelopmentConfig(Config):
        DEBUG = True


    class ProductionConfig(Config):

        DEBUG = False
        TESTING = False

    class TestingConfig(Config):

        DEBUG = True
        TESTING = True