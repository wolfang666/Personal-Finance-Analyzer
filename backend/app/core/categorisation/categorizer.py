import numpy as np
from app.core.categorisation.vectorizer import (
    load_vectorizer,
    load_ref_vectors,
    load_ref_labels
)
from app.core.categorisation.cosine import compute_cosine_similarity

_vectorizer = load_vectorizer()
_ref_vectors = load_ref_vectors()
_ref_labels = load_ref_labels()

def categorize(text, threshold=0.4):
    vec = _vectorizer.transform([text])

    similarity = compute_cosine_similarity(vec, _ref_vectors)

    similarity = similarity.flatten()

    idx = int(similarity.argmax())
    score = float(similarity[idx])

    if score >= threshold:
        cat, subcat = _ref_labels[idx]
        return cat, subcat, round(score, 3)

    return "Others", None, round(score, 3)
