import logging
def log_error(error_code: str, message: str):
    """Logs an error message with a specific error code """
    logging.error(f"{error_code}: {message}")

def log_info(message:str):
    """Logs an information message """
    logging.info(message)

def log_warning(message:str):
    """Logs a warning message """
    logging.warning(message)

