from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="gemma2-9b-it", groq_api_key = groq_api_key)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","Translate the following into {language}"),
        ("user","{text}")
    ]
)

parser = StrOutputParser()

chain = prompt|model|parser


app = FastAPI(title = 'Langchain Server', 
              version = "1.0",
              description = "Simple API server using Langchain runnable interface")

add_routes(
    app,
    chain,
    path="/doodoo"
)

if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)