import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
app_mode = os.getenv("APP_MODE", "development")
logging.info("Application mode: %s", app_mode)
