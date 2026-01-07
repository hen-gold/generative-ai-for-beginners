# Lesson 06: Building Text Generation Applications

**Type:** Build  
**Full Lesson:** [View in Repository](https://github.com/microsoft/generative-ai-for-beginners/tree/main/06-text-generation-apps)  
**Video:** [Watch on YouTube](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

## Overview

Learn to build your first text generation application using Azure OpenAI or OpenAI API. This hands-on lesson covers setting up the API, making calls, and building a practical recipe generator app.

## Learning Objectives

- Set up and authenticate with OpenAI APIs
- Make your first API calls in Python and TypeScript
- Build a complete text generation application
- Handle errors and implement best practices

## What You'll Build

A **Recipe Generator App** that:
- Takes ingredients as input
- Generates creative recipes
- Provides cooking instructions
- Handles various dietary restrictions

## Prerequisites

- Completed [Lesson 00: Course Setup](./Lesson-00-Course-Setup)
- API key for OpenAI or Azure OpenAI
- Python 3.9+ or Node.js installed

## Getting Started

### Python Setup

```python
# Install required packages
pip install openai python-dotenv

# Import libraries
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
```

### TypeScript Setup

```typescript
// Install packages
npm install openai dotenv

// Import libraries
import OpenAI from 'openai';
import * as dotenv from 'dotenv';

// Load environment variables
dotenv.config();
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});
```

## Basic API Call

### Python Example

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is generative AI?"}
    ],
    temperature=0.7,
    max_tokens=150
)

print(response.choices[0].message.content)
```

### TypeScript Example

```typescript
const response = await client.chat.completions.create({
  model: "gpt-3.5-turbo",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "What is generative AI?" }
  ],
  temperature: 0.7,
  max_tokens: 150
});

console.log(response.choices[0].message.content);
```

## Building the Recipe Generator

### Step 1: Define the System Prompt

```python
system_prompt = """
You are a creative chef assistant. Generate delicious recipes 
based on the ingredients provided. Include:
- Recipe name
- Cooking time
- Difficulty level
- Ingredients list
- Step-by-step instructions
- Nutritional tips
"""
```

### Step 2: Create the User Input Function

```python
def get_recipe(ingredients: str, dietary_restrictions: str = None):
    user_message = f"Create a recipe using: {ingredients}"
    
    if dietary_restrictions:
        user_message += f"\nDietary restrictions: {dietary_restrictions}"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.8,  # Higher for creativity
        max_tokens=500
    )
    
    return response.choices[0].message.content
```

### Step 3: Add Error Handling

```python
from openai import OpenAIError

try:
    recipe = get_recipe("chicken, tomatoes, garlic", "gluten-free")
    print(recipe)
except OpenAIError as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

### Step 4: Implement Token Counting

```python
import tiktoken

def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

# Check before making API call
tokens = count_tokens(user_message)
print(f"Using approximately {tokens} tokens")
```

## Advanced Features

### Streaming Responses

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

### Conversation History

```python
conversation_history = [
    {"role": "system", "content": system_prompt}
]

def chat(user_input: str):
    conversation_history.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )
    
    assistant_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message
```

### Response Formatting

```python
def get_structured_recipe(ingredients: str):
    user_message = f"""
    Create a recipe using: {ingredients}
    
    Format your response as JSON:
    {{
        "name": "Recipe name",
        "time": "Cooking time",
        "difficulty": "Easy/Medium/Hard",
        "ingredients": ["item 1", "item 2"],
        "instructions": ["step 1", "step 2"]
    }}
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
        response_format={"type": "json_object"}
    )
    
    return json.loads(response.choices[0].message.content)
```

## Best Practices

✅ **API Key Security**
- Never commit API keys to git
- Use environment variables
- Rotate keys regularly

✅ **Cost Optimization**
- Count tokens before API calls
- Use appropriate model (GPT-3.5 vs GPT-4)
- Implement caching for repeated queries

✅ **Error Handling**
- Handle rate limits
- Implement retry logic
- Validate inputs

✅ **User Experience**
- Show loading indicators
- Stream responses for better UX
- Provide clear error messages

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| `401 Unauthorized` | Check API key is correct |
| `429 Rate Limit` | Implement exponential backoff |
| `Timeout` | Reduce max_tokens or increase timeout |
| Inconsistent outputs | Lower temperature for consistency |

## Testing Your Application

```python
# Test cases
test_cases = [
    ("pasta, tomatoes, basil", "vegetarian"),
    ("chicken, rice, curry powder", None),
    ("chocolate, flour, eggs", "gluten-free")
]

for ingredients, restrictions in test_cases:
    print(f"\nTest: {ingredients}, {restrictions}")
    try:
        recipe = get_recipe(ingredients, restrictions)
        print("✓ Success")
    except Exception as e:
        print(f"✗ Failed: {e}")
```

## Next Steps

- **[Lesson 07: Building Chat Applications](./Lesson-07-Building-Chat-Applications)**
- Explore the complete code examples in the repository
- Try building your own text generation app

## Additional Resources

- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Code Examples](https://github.com/microsoft/generative-ai-for-beginners/tree/main/06-text-generation-apps)

---
[← Previous: Advanced Prompts](./Lesson-05-Advanced-Prompts) | [Back to Home](./Home) | [Next Lesson: Chat Applications →](./Lesson-07-Building-Chat-Applications)
