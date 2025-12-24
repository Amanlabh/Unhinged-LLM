# Model Notes

## Unrestricted System Prompt

The system prompt has been configured to be unrestricted and open. However, note that:

1. **Model-Level Restrictions**: Some Ollama models have built-in safety features that are part of the model weights themselves. These cannot be overridden by system prompts alone.

2. **Uncensored Models**: If you want truly unrestricted responses, consider using uncensored/community models:
   ```bash
   # Examples of models that may be less restricted:
   ollama pull llama3.2
   ollama pull mistral
   ollama pull codellama
   
   # Or search for community uncensored variants on:
   # https://ollama.ai/library
   ```

3. **Custom Models**: You can also fine-tune or use custom models that have fewer restrictions.

4. **System Prompt Location**: The system prompt is defined in `cyber_knowledge.py` in the `get_cyber_context()` function. You can modify it directly to change the assistant's behavior.

## Changing the Model

You can change the model by:
- Setting `OLLAMA_MODEL` in `.env` file
- Using the `models` command in the assistant to see available models
- Modifying `DEFAULT_MODEL` in `config.py`

## Technical Note

The system prompt is sent with every request to Ollama. However, the model's training and built-in safety mechanisms may still apply regardless of the system prompt. For maximum flexibility, use models specifically trained without safety restrictions.



