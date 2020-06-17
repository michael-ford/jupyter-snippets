# Import packages
import os
from src import common
import logbook

# Setup log
common.initialize_logger(log_file_path='', overwrite=True)

log = logbook.Logger('Logbook')

# Set Globals
USE_CACHE = True    # if False reproduces all needed data files
ENV = ''  # conda environment being used 