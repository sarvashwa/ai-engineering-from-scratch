import logging
import time

logger = logging.getLogger(__name__)

def background_log():
    
    time.sleep(5)

    logger.info("Finished background task.")