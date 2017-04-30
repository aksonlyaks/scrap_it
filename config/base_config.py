import os

# Generic Config Variables for Scrapping
class ApplicationConfig:
	environment = os.environ.get("ENV", 'debug')
	read_timeout = 30.0
	connect_timeout = 5.0