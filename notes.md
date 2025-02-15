

1. (Optional) Install JupyterLab for an alternative interfact
    ```bash
    brew install jupyterlab
    ```   
2. (pip) Create a virtual environment, activate, install requirements:

    ```bash
    ENV_NAME=lc-academy-env && python3 -m venv $ENV_NAME && source $ENV_NAME/bin/activate && pip install -r requirements.txt
    ```
3. add .env file with necessary API keys 
4. run load_env.py 
    ```python 
    python3 load_env.py
    ```
