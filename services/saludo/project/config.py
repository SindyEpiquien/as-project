# services/users/project/config.py

class BaseConfig:
    """Configuracion base"""
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Configuracion de desarrollo"""
    pass


class TestingConfig(BaseConfig):
    """Configuracion de prueba"""
    pass 


class ProductionConfig(BaseConfig):
    """Configuracion de produccion"""
    pass


