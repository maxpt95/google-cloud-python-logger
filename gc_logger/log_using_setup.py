"""Sample of writing in log before and after setup"""
import logging

import write_in_all_severities
from config import setup_log

logger = logging.getLogger(__name__)
setup_log.setup_cloud_logging(logger)

if __name__ == "__main__":
    logger.debug("Writing before setup")
    setup_log.setup_logging()
    logger.debug("Writing after setup")
    write_in_all_severities.write()
