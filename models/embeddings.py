import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialise ChromaDB client and collection
client = chromadb.Client()
collection = client.create_collection(name="research_chunks")

def generate_embedding(text):
    """
    Generates a vector embedding for the input text using the SentenceTransformer model.

    Args:
        text (str): The input text to embed.

    Returns:
        list: The embedding vector as a list of floats.
    """
    return embedding_model.encode(text).tolist()

def chunk_text(text, max_length=300, overlap=50):
    """
    Splits input text into chunks of up to max_length words with specified overlap.
    
    Args:
        text (str): Input long text to split.
        max_length (int): Maximum words per chunk.
        overlap (int): Number of overlapping words between chunks.
    
    Returns:
        list: List of text chunks as strings.
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
    Adds a list of text chunks to the specified vector store collection.

    Args:
        chunks (list): List of text chunks to index.
        collection_name (str): Name of the collection to store embeddings in.

    Returns:
        None
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
    Retrieves top matching text chunks from the vector store based on query similarity.

    Args:
        query (str): The input query text.
        collection_name (str): Name of the collection to query from.
        top_k (int): Number of top results to return.

    Returns:
        list: List of retrieved text chunks matching the query.
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
