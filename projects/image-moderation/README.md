# Image Moderation with Open Source LLM Vision Models 🔍

## Overview

This project demonstrates how to use open-source LLM Vision models for cost-effective image moderation. While state-of-the-art models like GPT-4o offer excellent results, their cost ($3.50/1000 images) can be prohibitive for many applications.

This implementation uses the `mistralai/pixtral-12b` model via [OpenRouter](https://openrouter.ai/mistralai/pixtral-12b), reducing costs to approximately $0.14/1000 images while maintaining good moderation capabilities.

⚠️ **Note**: This is a proof-of-concept implementation intended for experimentation. Additional prompt engineering and testing would be needed for production use.

## Model Comparison

| Model | Cost per 1000 images | Availability |
|-------|---------------------|--------------|
| GPT-4o | $3.50 | Closed Source |
| Pixtral-12B | $0.14 | Open Source |

## Implementation Options

### 1. Local Inference with MLX (MacOS)
Run the model locally using Apple's MLX framework. The model (~12GB) will be downloaded from Hugging Face.

Requirements:
- [uv package manager](https://docs.astral.sh/uv/getting-started/installation/)

```bash
uv run src/app_mlx.py
```

### 2. OpenRouter API Integration
Use the hosted version of Pixtral-12B through OpenRouter's API.

Setup:
1. Copy the environment configuration:
   ```bash
   cp .env.example .env
   ```
2. Add your OpenRouter API key to `.env`
3. Run the application:
   ```bash
   uv run src/app_openrouter.py
   ```

## Performance Considerations

- Local inference requires ~12GB storage for the model
- MLX implementation optimized for Apple Silicon
- API version suitable for quick testing and lower setup overhead
- Response times may vary between local and API implementations

## Future Improvements

- [ ] Enhanced prompt engineering for better accuracy
- [ ] Support for batch processing
- [ ] Performance benchmarks
- [ ] Error handling and edge cases

## Connect With Me

<div>
    <a href="https://twitter.com/maledorak">
        <img src="https://img.shields.io/badge/X/Twitter-000000?style=for-the-badge&logo=x&logoColor=black&color=white" />
    </a>
    <a href="https://bsky.app/profile/maledorak.bsky.social">
        <img src="https://img.shields.io/badge/Bluesky-000000?style=for-the-badge&logo=bluesky&logoColor=black&color=white" />
    </a>
    <a href="https://github.com/maledorak">
        <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=black&color=white" />
    </a>
    <a href="https://www.linkedin.com/in/mariuszkorzekwa/">
        <img src="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&logo=linkedin&logoColor=black&color=white" />
    </a>
</div>
