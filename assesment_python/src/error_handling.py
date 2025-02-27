import logging
def log_error(error_code: str, message: str):
    """Logs an error message with a specific error code."""
    logging.error(f"{error_code}: {message}")



