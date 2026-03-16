from typing import List, Optional
from sentence_transformers import SentenceTransformer
import chromadb

from app.config import(EMBEDDING_MODEL_NAME, CHROMA_PERSIST_DIR, COLLECTION_NAME, RETRIEVAL_K)
from app.config import Document

class VectorStore:
    def __init__(self):
        print("loading model...")
        self.embedder =SentenceTransformer(EMBEDDING_MODEL_NAME)
        print("model loaded")

        self.client = chromadb.PersistentClient(path=str(CHROMA_PERSIST_DIR))
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME, metadata={"hnsw:space": "cosine"})

    def add_documents(self, documents: List[Document]) -> int:
        if not documents:
            return 0
        
        texts = [doc.content for doc in documents]
        metadata = [doc.metadata for doc in documents]

        ids = [f"doc_{i}_{doc.metadata['source']}" for i, doc in enumerate(documents)]

        embeddings = self.embedder.encode(texts).tolist()

        self.collection.add(ids = ids, embeddings=embeddings, documents=texts, metadata=metadata)
        return len(documents)

    def search(self, query: str, k: int = RETRIEVAL_K)-> List[Document]:
        query_embedding = self.embedder.encode(query).tolist()

        results = self.collection.query(query_embeddings =[query_embedding], n_results = k)

        documents = []
        for i in range(len(results["ids"][0])):
            doc = Document(content=results['documents'][0][i], metadata=results['metadata'][0][i])
            documents.append(doc)
        return documents

    def clear(self):
        self.client.delete_collection(name=COLLECTION_NAME)
        self.collection = self.client.get_or_create_collection(name=COLLECTION_NAME, metadata={"hnsw:space": "cosine"})

    
