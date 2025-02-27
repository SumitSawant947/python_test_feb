import logging
import os
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging
logging.basicConfig(
    filename=os.path.join(log_dir, "errors.log"),
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_error(error_code, message):
    error_message = f"ERROR {error_code}: {message}"
    print(error_message)
    logging.error(error_message)