import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def compute_cosine_similarity(vec, ref_vectors) -> np.ndarray:
    return cosine_similarity(vec, ref_vectors)[0]