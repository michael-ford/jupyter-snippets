# Import packages
import os
from src import common
from src.data import dvc_tools
import logbook
from IPython.display import Markdown as md       # Allows markdown output in code cells. See https://stackoverflow.com/a/57023238

# Setup log
common.initialize_logger(log_file_path='', overwrite=True)

log = logbook.Logger('Logbook')

# Set Globals
USE_CACHE = True    # if False reproduces all needed data files
ENV = ''  # conda environment being used 
