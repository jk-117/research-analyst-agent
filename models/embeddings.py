from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embedding(text):
    """
    Generates a vector embedding for input text.
    """
    return embedding_model.encode(text).tolist()  # convert numpy array to list for serialization

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
        i += max_length - overlap  # move forward with overlap
    return chunks

if __name__ == "__main__":
    sample_text = " ".join(["This is sentence."] * 50)  # long sample

    # Test chunking
    chunks = chunk_text(sample_text, max_length=20, overlap=5)
    for idx, c in enumerate(chunks):
        print(f"\nChunk {idx+1}:\n{c}")

    # Test embedding
    sample_text = "The quick brown fox jumps over the lazy dog."
    embedding = generate_embedding(sample_text)
    print(f"\nEmbedding length: {len(embedding)}")
