import os
from dotenv import load_dotenv

from langchain.document_loaders import ReadTheDocLoader # helps build documentation for GitHub repo




load_dotenv()


def ingest_docs() -> None:
    loader = ReadTheDocLoader(path="/Users/morgan/Documents/04_Online_Courses/13_udemy_langchain/langchain-apps/langchain-docs/api.python.langchain.com/en/latest")
    raw_documents = loader.load()


if __name__ == "__main__":
    ingest_docs()