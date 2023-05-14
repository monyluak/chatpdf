# ChatPDF

Chat with your PDF


## Prerequisites
1. [Python 3.6 or later](https://www.python.org/downloads/)
2. [OpenAI API Key](https://platform.openai.com/signup)
3. [LangChain library](https://python.langchain.com/en/latest/index.html)
4. [Faiss VectorDB](https://github.com/facebookresearch/faiss)

## Installation

Create a virtual environment
```
python3 -m venv venv
```

Activate the virtual environment
```
source venv/bin/activate
```

Install packages
```
pip install -r requirements.txt
```

## Usage

1. Make sure you have an OpenAI API key. You can get one by signing up for OpenAI at https://platform.openai.com/signup

2. Load your OpenAI API key in a `.env` file in the root directory of your project using the following format:

```
OPENAI_API_KEY=<your_api_key>
```

3. Replace the file path in `loader` with the path to the PDF document i.e `loader = PyPDFLoader("data/resume.pdf")
` The pdf will be used for the question answering system.

4. Run the script and input a question to get an answer from the PDF document.

```
python3 app.py
```

## How it works

1. Import necessary libraries and load the OpenAI API key from a `.env` file.
```
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```

2. Import necessary classes from the LangChain library, including `PyPDFLoader`, `OpenAIEmbeddings`, `FAISS`, `OpenAI`, and `RetrievalQA` These classes are used to load a PDF document, convert the text into embeddings, create a vector store, and set up the question-answering model.

```
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from langchain import OpenAI
from langchain.chains import RetrievalQA
```

3. These lines create an instance of `PyPDFLoader` to load a PDF document, split it into pages, create an instance of `OpenAIEmbeddings` to convert the text into embeddings, create an instance of `FAISS` to create a vector store, and create an instance of `RetrievalQA` to set up the question-answering model.

```
loader = PyPDFLoader("data/resume.pdf")
pages = loader.load_and_split()

embeddings = OpenAIEmbeddings()

index = FAISS.from_documents(pages, embeddings)
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=index.as_retriever(),
)
```

4. These lines prompt the user to input a question, pass the question to the `RetrievalQA` model, and print the answer to the console.
```
query = input("Ask me anything? ")
print(qa.run(query))
```

## Conclusion 

In conclusion, this code demonstrates how to build a question answering system for PDF documents using natural language processing and machine learning techniques. By using OpenAI's powerful language model and FAISS for efficient indexing and retrieval, we can provide users with quick and accurate answers to their questions about PDF documents.

**Note**
To use OpenAI's GPT-3 language model and API, you'll need an API key, which can be obtained by signing up for their API program. You should take care to keep your API key secure and not share it publicly.

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).
