import os
from pathlib import Path

BASE_DIR =  Path(__file__).parent.parent
DATA_DIR = BASE_DIR/ "data"
DEMO_DIR = BASE_DIR / "demo"
CHROMA_DIR = BASE_DIR / "chroma_db"


EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDING_DIMENSION = 384

# Chunking configuration
CHUNK_SIZE = 750  
CHUNK_OVERLAP = 100  

RETRIEVAL_K = 4  # number of chunks to retrieve per query
COLLECTION_NAME = "documents"

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
LLM_MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 1024
TEMPERATURE = 0.3

FILE_TYPES = ["pdf" "txt"]

DEMO_Q = [ "What is this document acout?", "what is the main topic of this document", "Summarize this document", "What are the most imprtant concepts mentioned"]


# System prompt for the LLM
SYSTEM_PROMPT = """You are a helpful assistant that answers questions based on the provided document context.

Instructions:
1. Answer ONLY using information from the provided context
2. If the context doesn't contain the answer, say "I don't have enough information to answer this"
3. Cite your sources using [Source: filename, chunk X] format
4. Be concise but thorough"""

# Template for QA
QA_PROMPT_TEMPLATE = """Context from documents:
{context}

Question: {question}

Answer based on the context above, with citations:"""