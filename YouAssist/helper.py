# from langchain.document_loaders import YoutubeLoader
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings() 

def createVectorStoreFromYoutube(youtubeUrl: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(youtubeUrl)
    print(loader)
    transcript = loader.load()
    print(transcript)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    print(text_splitter)
    docs = text_splitter.split_documents(transcript)
    print(docs)

    db = FAISS.from_documents(docs, embeddings)
    print(db)
    return db

if __name__ == "__main__":
    createVectorStoreFromYoutube("https://www.youtube.com/watch?v=lG7Uxts9SXs")