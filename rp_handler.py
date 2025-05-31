import runpod
import torch
from diffusers import FluxPipeline
import time

# Initialize models
def initialize_model():
    model_path = "/runpod-volume/flux1-dev"

    # Load FLUX pipeline
    pipe = FluxPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        use_safetensors=True
    )

    return pipe

# Load model at startup


def train_model(input_url):
    pipe = initialize_model()



# RunPod serverless handler
def handler(event):
    print("🚀 Worker start")
    input = event['input']

    input_url = input.get('input_url')
    test = input.get('test')

    print(f"📥 Input URL: {input_url}")

    try:
        result = train_model()
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

# Run as serverless function
if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
