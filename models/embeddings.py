from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embedding(text):
    """
    Generates a vector embedding for input text.
    """
    return embedding_model.encode(text).tolist()  # convert numpy array to list for serialization

if __name__ == "__main__":
    sample_text = "The quick brown fox jumps over the lazy dog."
    embedding = generate_embedding(sample_text)
    print(f"Embedding length: {len(embedding)}")
