import joblib
from app.config import (
    VECTORIZER_PATH,
    REF_VECTORS_PATH,
    REF_LABELS_PATH
)

def load_vectorizer():
    return joblib.load(VECTORIZER_PATH)

def load_ref_vectors():
    return joblib.load(REF_VECTORS_PATH)

def load_ref_labels():
    return joblib.load(REF_LABELS_PATH)