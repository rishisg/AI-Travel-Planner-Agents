# ✅ memory/memory_store.py (Vector Memory using FAISS)

import faiss
import numpy as np

class MemoryStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(512)  # 512-dimensional vector space
        self.data = []  # Stores raw user inputs
    
    def store_user_trip(self, user_inputs):
        embedding_vector = np.random.rand(512).astype('float32')  # Simulated embedding
        self.index.add(np.array([embedding_vector]))  # Add to FAISS index
        self.data.append(user_inputs)  # Store raw input
    
    def retrieve_similar_trips(self):
        if not self.data:
            return None
        
        query_vector = np.random.rand(512).astype('float32')  # Example search vector
        distances, indices = self.index.search(np.array([query_vector]), 3)  # Retrieve top 3 closest trips
        
        similar_trips = [self.data[idx] for idx in indices[0] if distances[0][idx] < 0.3]  # Filter highly relevant trips
        return similar_trips if similar_trips else None
