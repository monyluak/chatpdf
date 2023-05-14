import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from langchain import OpenAI
from langchain.chains import RetrievalQA


loader = PyPDFLoader("data/resume.pdf")
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()

index = FAISS.from_documents(pages, embeddings)
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=index.as_retriever(),
)
query = input("Ask me anything? ")
print(qa.run(query))
