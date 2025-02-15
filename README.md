# Intro to LangGraph [2/14/25]


## Introduction

**Welcome to LangChain Academy!**

> In each module folder, you'll see:
>> - instructional Jupyter notebooks.
>> -  a `studio` subdirectory, with 
graphs to use with `LangGraph Studio/API`.

**Overview of module contents:**
- Module 0: basic setup
- Module 1: 

---

## Setup
### Python version

You need to run Python 3.11 or later. 
Check your version and upgrade if necessary.

**check**
```
python3 --version
```
**upgrade**



### Clone repo
```
git clone https://github.com/langchain-ai/langchain-academy.git
$ cd langchain-academy
```

### Create an environment and install dependencies
#### Mac/Linux/WSL
```
$ python3 -m venv lc-academy-env
$ source lc-academy-env/bin/activate
$ pip install -r requirements.txt
```


### Running notebooks
If you don't have Jupyter set up, follow installation instructions [here](https://jupyter.org/install).
```
$ jupyter notebook
```

### Setting up env variables
Briefly going over how to set up environment variables. You can also 
use a `.env` file with `python-dotenv` library.
#### Mac/Linux/WSL
```
$ export API_ENV_VAR="your-api-key-here"
```


### Set OpenAI API key
* If you don't have an OpenAI API key, you can sign up [here](https://openai.com/index/openai-api/).
*  Set `OPENAI_API_KEY` in your environment 

### Sign up and Set LangSmith API
* Sign up for LangSmith [here](https://smith.langchain.com/), find out more about LangSmith
* and how to use it within your workflow [here](https://www.langchain.com/langsmith), and relevant library [docs](https://docs.smith.langchain.com/)!
*  Set `LANGCHAIN_API_KEY`, `LANGCHAIN_TRACING_V2=true` in your environment 

### Set up Tavily API for web search

* Tavily Search API is a search engine optimized for LLMs and RAG, aimed at efficient, 
quick, and persistent search results. 
* You can sign up for an API key [here](https://tavily.com/). 
It's easy to sign up and offers a very generous free tier. Some lessons (in Module 4) will use Tavily. 

* Set `TAVILY_API_KEY` in your environment.

### Set up LangGraph Studio

* Currently, Studio only has macOS support and needs Docker Desktop running.
* Download the latest `.dmg` file [here](https://github.com/langchain-ai/langgraph-studio?tab=readme-ov-file#download)
* Install Docker desktop for Mac [here](https://docs.docker.com/engine/install/)

### Running Studio
Graphs for LangGraph Studio are in the `module-x/studio/` folders.

* To use Studio, you will need to create a .env file with the relevant API keys
* Run this from the command line to create these files for module 1 to 5, as an example:
```
for i in {1..6}; do
  cp module-$i/studio/.env.example module-$i/studio/.env
  echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\"" > module-$i/studio/.env
done
echo "TAVILY_API_KEY=\"$TAVILY_API_KEY\"" >> module-4/studio/.env
```

---
1. (Optional) Install JupyterLab for an alternative interfact
    ```bash
    brew install jupyterlab
    ``` 

> now you can exec `jupyter` commands like opening a notebook or lab


2. (pip) Create a virtual environment, activate, install requirements:

    ```bash
    ENV_NAME=lc-academy-env && python3 -m venv $ENV_NAME && source $ENV_NAME/bin/activate && pip install -r requirements.txt
    ```

3. add .env file with necessary API keys 

4. run load_env.py 
    ```python 
    python3 load_env.py
    ```
---