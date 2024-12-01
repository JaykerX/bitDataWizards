import os

class Config:
    """Base configuration."""
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False