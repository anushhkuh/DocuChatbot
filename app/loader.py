from pathlib import Path
from typing import List, Dict, Any
from dataclasses import dataclass

@datclasses

class Document:
    """reprsnts a doc with its body and metadata - used in citations"""
    content: str
    metadata: Dict[str, Any]

class DocumentLoder:
    def __inti__(self, chunk_size: int =CHUNK_SIZE, chunk_overlap:int = CHUNK_OVERLAP):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap, separators=["\n\n", "\n", " ", ""])

        def load_pdf(self, file_path: Path) -> str:
            text = ""

            with pdfplumber.open(file_path) as pdf:
                for pafe in pdf.pages:
                    page_text  =page.extract_text() or ""
                    text += page_text + "\n"

                    return text.strip()

        def load_txt(self,file_path: Path)-> str:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read().strip()

        def load(self, file_path: str)-> List[Document]:
             path = Path(file_path)

             if not path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")

            extension  = path.suffix.lower().lstrip(".")

            if extention not in FILE_TYPES:
                raise ValueError(f"Unsupported file type: {extension}")
            
            if extension == "pdf":
                text = self.load_pdf(path)
            else:
                text = self.load_txt(path)

            chunks = self.text_splitter.split_text(text)

            documents = []

            for i, chunk in emumerate(chunks):
                doc = Document(content=chunk, metadata={"source": path.name, "chunk_index": i, "total_chunks": len(chunks)})
                documents.append(doc)

            return documents

