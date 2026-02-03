from pathlib import Path
import os

# Project Paths

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

DB_PATH = DATA_DIR / "finance.db"
MODEL_PATH = MODELS_DIR / "mistral-7b-instruct-v0.1.Q4_K_M.gguf"
VECTORIZER_PATH = MODELS_DIR / "tfidf_vectorizer.pkl"
REF_VECTORS_PATH = MODELS_DIR / "ref_vectors.pkl"
REF_LABELS_PATH = MODELS_DIR / "ref_labels.pkl"

# Environment

ENV = os.getenv("ENV","development")
DEBUG = ENV == "development"

# LLM Configuration

LLM_CONTEXT_SIZE = int(os.getenv("LLM_CONTEXT_SIZE",2048))
LLM_GPU_LAYERS = int(os.getenv("LLM_GPU_LAYERS",35))
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE",0.2))
LLM_TOP_P = float(os.getenv("LLM_TOP_P",0.9))
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS",300))

# Database Configuration

SQLITE_TIMEOUT = int(os.getenv("SQLITE_TIMEOUT",30))