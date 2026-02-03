from llama_cpp import Llama
from app.config import (
    MODEL_PATH,
    LLM_CONTEXT_SIZE,
    LLM_GPU_LAYERS
)

def load_llm():
    return Llama(
        model_path = str(MODEL_PATH),
        n_ctx = LLM_CONTEXT_SIZE,
        n_gpu_layers = LLM_GPU_LAYERS,
        verbose=True
    )