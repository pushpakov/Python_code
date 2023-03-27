import logging

# Some of the commonly used parameters for basicConfig() are the following:
# level: The root logger will be set to the specified severity level.
# filename: This specifies the file.
# filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
# format: This is the format of the log message.

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')



# The defined levels, in order of increasing severity, are the following:

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')



# formatting the output
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')

