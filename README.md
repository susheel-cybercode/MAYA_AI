# NOAH LLM - Uncensored Local Transformer

A completely uncensored, self-hosted language model trained on coding, cybersecurity, psychology, body language, and computer vision domains.

## Features

- **Fully Local**: Runs offline, no API keys needed
- **Uncensored**: No hardcoded safety filters
- **Domain Expertise**: Trained on coding, cybersec, psychology, body language, computer vision
- **Multiple Sizes**: Small (7M), Medium (40M), Large (150M) parameters
- **BPE Tokenizer**: 16K vocab trained on your data
- **Ollama-style CLI**: `noah pull`, `noah run`, `noah list`

## Quick Start

### Train on Kaggle (Free GPU)
```python
# In Kaggle notebook with GPU T4 x2
!git clone https://github.com/susheel-cybercode/MAYA_AI.git
%cd MAYA_AI
!pip install -q -r requirements.txt tokenizers
!python train_bpe_tokenizer.py
!python maya_bpe.py --train --size small --epochs 3 --batch-size 16
```

### Train Locally (CPU)
```bash
cd /home/susheel/Desktop/MAYA\ AI
source venv/bin/activate
python train_bpe_tokenizer.py
python maya_bpe.py --train --size small --epochs 1 --batch-size 2
```

### Chat with Trained Model
```bash
python maya_bpe.py --size small
```

### Ollama-style CLI
```bash
./noah pull small
./noah run small
./noah run small "What is SQL injection?"
./noah list
```

## Model Sizes

| Size | Params | VRAM (train) | VRAM (infer) | Use Case |
|------|--------|--------------|--------------|----------|
| Small | ~7M | 2GB | 1GB | Phone, testing |
| Medium | ~40M | 8GB | 4GB | Laptop, balanced |
| Large | ~150M | 24GB | 12GB | Server, quality |

## Integration with Apple of Eden

Run NOAH as OpenAI-compatible API server:
```bash
# Terminal 1: Start API server
python maya_api_server.py

# Terminal 2: Configure Eden
cd /home/susheel/Desktop/theappleofeden
python -c "
from eden.core.config import Config
cfg = Config()
cfg.ai_provider = 'custom_local'
cfg.custom_llm_url = 'http://localhost:8000'
cfg.custom_model = 'noah'
cfg.save()
"

# Terminal 3: Run Eden
python eden_core.py --chat
```

## Training Data

Add `.txt` files to `training_data/` and re-run:
```bash
python train_bpe_tokenizer.py
python maya_bpe.py --train --size small --epochs 3 --batch-size 8
```

## License

MIT License