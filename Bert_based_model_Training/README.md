# 🎭 Sentiment Analysis on IMDb using BERT

This project applies a **BERT-based transformer model** to classify IMDb movie reviews as **positive** or **negative** using Hugging Face Transformers.

---

## 🧠 Overview

- Uses pretrained `bert-base-uncased` or `roberta-base` models
- Fine-tunes on the IMDb dataset (binary sentiment classification)
- Achieves ~89.9% accuracy on validation
- Built with 🤗 Transformers and PyTorch (or TensorFlow)

---

## 📦 Dependencies

- `transformers`
- `datasets`
- `torch` or `tensorflow`
- `scikit-learn`
- `matplotlib` (optional)

Install with:
```bash
pip install transformers datasets scikit-learn matplotlib

