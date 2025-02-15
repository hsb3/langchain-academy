import os
import logging
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_env_file(start_path):
    """
    Searches for a .env file starting from the given directory path.

    Args:
        start_path (str): The directory path to start searching from.

    Returns:
        Path or None: The path to the .env file if found, otherwise None.

    Logs:
        Info: When the search starts and if the .env file is found.
        Warning: If no .env file is found.
    """
    logging.info(f"Searching for .env file starting from {start_path}")
    for root, dirs, files in os.walk(start_path):
        if ".env" in files:
            env_path = Path(root) / ".env"
            logging.info(f".env file found at {env_path}")
            return env_path
    logging.warning("No .env file found")
    return None

def set_env_variables(env_file_path):
    """
    Loads environment variables from a specified .env file and sets them in the OS environment.

    Args:
        env_file_path (str): The path to the .env file.

    Logs:
        - Info: When the .env file is being loaded and when each environment variable is set.
        - Error: If the .env file fails to load.
        - Warning: If a line in the .env file is invalid or skipped.

    Raises:
        None
    """
    logging.info(f"Loading .env file from {env_file_path}")
    if not load_dotenv(env_file_path):
        logging.error(f"Failed to load .env file from {env_file_path}")
        return

    with open(env_file_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' not in line:
                logging.warning(f"Skipping invalid line: {line}")
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.split('#', 1)[0].strip()  # Ignore inline comments
            if key and value:
                os.environ[key] = value
                logging.info(f"Set {key}={os.getenv(key)}")
            else:
                logging.warning(f"Skipping invalid line: {line}")

if __name__ == "__main__":
    start_path = Path.cwd()  # Starting from the current working directory
    env_file_path = find_env_file(start_path)
    if env_file_path:
        set_env_variables(env_file_path)
    else:
        logging.warning("No .env file found")