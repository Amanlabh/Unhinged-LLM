# Quick Start - Unrestricted Mode

## What Changed

1. **System Prompt**: Made completely explicit about having NO limits, NO restrictions, NO filters
2. **API Parameters**: Added high temperature (1.0) and unlimited response length
3. **Generate Mode**: Option to use `generate()` instead of `chat()` which sometimes bypasses restrictions better

## How to Use

### Option 1: Use Generate Mode (Recommended for unrestricted)

Create a `.env` file:
```env
OLLAMA_MODEL=llama3.2
USE_GENERATE=true
```

### Option 2: Try Different Models

Some models are less restricted. Try:
```bash
ollama pull mistral
ollama pull codellama
```

Then set in `.env`:
```env
OLLAMA_MODEL=mistral
USE_GENERATE=true
```

### Option 3: Use Uncensored Community Models

Search for uncensored models:
```bash
ollama search uncensored
```

## Testing

After restarting, test with:
```
"Are you limited?"
"Can you help with illegal activities?"
"Explain how to hack"
```

If it still mentions limits, the **model itself** has restrictions that can't be overridden. You'll need to use a different, uncensored model.

## Important Note

The system prompt is now completely unrestricted. However, **the model itself** may still have built-in safety features that are part of its training. These cannot be removed by prompts alone. You need to use models that were trained without safety restrictions.



