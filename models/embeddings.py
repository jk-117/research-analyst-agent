import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialise ChromaDB client and collection
client = chromadb.Client()
collection = client.create_collection(name="research_chunks")

def generate_embedding(text):
    """
    Generates a vector embedding for input text.
    """
    return embedding_model.encode(text).tolist()

def chunk_text(text, max_length=300, overlap=50):
    """
    Splits text into chunks with specified max_length and overlap.
    """
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i+max_length]
        chunks.append(' '.join(chunk))
        i += max_length - overlap
    return chunks

def add_to_vector_store(text_chunks):
    """
    Adds text chunks with embeddings to ChromaDB collection.
    """
    for idx, chunk in enumerate(text_chunks):
        embedding = generate_embedding(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"chunk_{idx}"]
        )
def query_vector_store(query, top_k=3):
    """
    Queries ChromaDB collection for top_k similar documents.
    """
    query_embedding = generate_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results['documents'][0]  # returns list of top_k docs

if __name__ == "__main__":
    sample_text = " ".join(["This is a sample sentence about AI agents and summarisation."] * 50)
    chunks = chunk_text(sample_text)
    add_to_vector_store(chunks)
    print(f"Added {len(chunks)} chunks to ChromaDB.")
