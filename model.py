from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pydantic import SecretStr

load_dotenv()

def openrouterllm()->ChatOpenAI:
    OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
    BASE_URL = os.environ.get("BASE_URL")


    llm=ChatOpenAI(
        model="nvidia/nemotron-nano-9b-v2:free",
        api_key=SecretStr(OPENROUTER_API_KEY) if OPENROUTER_API_KEY else None,
        base_url=BASE_URL,
        temperature=0.6
    )
    return llm

def local_llm()->ChatOpenAI:
    LMSTUDIO_API_KEY = os.environ.get("LMSTUDIO_API_KEY")
    LOCAL_BASE_URL = os.environ.get("LOCAL_BASE_URL")
    print("LMSTUDIO_API_KEY :",LMSTUDIO_API_KEY)
    print("LOCAL_BASE_URL",LOCAL_BASE_URL)
    gemma="gemma-3-12b-it"
    minicpm="huihui-minicpm-v-4_5-abliterated"
    llm=ChatOpenAI(    
        model=gemma,
        api_key=SecretStr(LMSTUDIO_API_KEY) if LMSTUDIO_API_KEY else None,
        base_url=LOCAL_BASE_URL,
        temperature=0.7,
        )
    return llm