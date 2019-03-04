class BasicConfig:
    SECRET_KEY = 'dev'


class ProdConfig(BasicConfig):
    SECRET_KEY = 'skj123'
