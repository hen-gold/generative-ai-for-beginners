# Lesson 04: Prompt Engineering Fundamentals

**Type:** Learn  
**Full Lesson:** [View in Repository](https://github.com/microsoft/generative-ai-for-beginners/tree/main/04-prompt-engineering-fundamentals)  
**Video:** [Watch on YouTube](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Overview

Master the art and science of prompt engineering - the key to getting the best results from Large Language Models. Learn techniques, patterns, and best practices for crafting effective prompts.

## Learning Objectives

- Understand what prompt engineering is and why it matters
- Learn fundamental prompting techniques
- Apply best practices for different use cases
- Avoid common prompting mistakes

## What is Prompt Engineering?

Prompt engineering is the practice of designing and refining inputs to get desired outputs from AI models. It's about communicating effectively with AI.

**Why it matters:**
- Same model, different results based on prompts
- Can dramatically improve output quality
- Cost-effective way to optimize AI performance
- No model retraining required

## Basic Prompt Structure

```
[Context] + [Instruction] + [Input Data] + [Output Format]
```

**Example:**
```
You are a helpful teacher. [Context]
Explain quantum computing [Instruction]
for a 10-year-old student [Input Data]
in 3 simple sentences. [Output Format]
```

## Core Techniques

### 1. **Be Clear and Specific**

❌ Poor: "Tell me about dogs"  
✅ Good: "List 5 key characteristics that make dogs good family pets, focusing on behavior and care requirements"

### 2. **Provide Context**

```
You are an expert Python developer with 10 years of experience.
Help me debug this code...
```

### 3. **Give Examples (Few-Shot Learning)**

```
Convert these sentences to positive tone:

Sentence: "This is terrible"
Positive: "This has room for improvement"

Sentence: "I hate waiting"
Positive: "I appreciate patience"

Sentence: "This is boring"
Positive: [Model completes]
```

### 4. **Specify Output Format**

```
List the benefits of exercise in JSON format:
{
  "benefits": [
    {"category": "physical", "description": "..."},
    {"category": "mental", "description": "..."}
  ]
}
```

### 5. **Break Down Complex Tasks**

Instead of one complex prompt, use a sequence:
1. First, extract key information
2. Then, analyze the information
3. Finally, generate recommendations

### 6. **Use Delimiters**

```
Summarize the text between triple quotes:

\"\"\"
[Long text here]
\"\"\"
```

### 7. **Assign a Role**

```
You are a cybersecurity expert.
You are a creative marketing professional.
You are a patient medical advisor.
```

## Prompting Patterns

### Chain of Thought

Encourage step-by-step reasoning:
```
Solve this problem step by step:
Problem: ...
Let's think through this carefully:
```

### Instructional

Clear, direct commands:
```
Write a product description.
Translate this to Spanish.
Summarize in 50 words.
```

### Conversational

Natural dialogue style:
```
I'm trying to learn Python.
Can you help me understand functions?
```

### Template-Based

Structured format with placeholders:
```
Product Name: [name]
Description: [description]
Target Audience: [audience]
Generate a marketing tagline.
```

## Advanced Techniques

### Temperature Control
- **Low (0.0-0.3)**: Factual, consistent, deterministic
- **Medium (0.7)**: Balanced creativity
- **High (1.0+)**: Creative, varied, exploratory

### System Messages
Set persistent behavior:
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant that speaks like Shakespeare"},
    {"role": "user", "content": "Tell me about AI"}
]
```

### Constraints
Add boundaries:
```
Answer in exactly 100 words.
Use only information from the provided document.
Do not make assumptions; if unsure, say "I don't know."
```

## Common Mistakes to Avoid

❌ **Too vague**: "Tell me something interesting"  
❌ **Multiple questions**: "What's AI and blockchain and how do they work together?"  
❌ **Assuming knowledge**: Referencing prior conversations without context  
❌ **No validation**: Accepting outputs without checking  
❌ **Overcomplicating**: 500-word prompts when 50 words suffice  

## Best Practices

✅ Start simple, iterate to improve  
✅ Test with multiple variations  
✅ Be specific about what you don't want  
✅ Use examples to guide the model  
✅ Specify the expertise level needed  
✅ Request citations when accuracy matters  
✅ Save successful prompts for reuse  

## Hands-On Exercises

1. **Exercise 1**: Improve this prompt
   ```
   Tell me about machine learning.
   ```

2. **Exercise 2**: Create a few-shot prompt for sentiment analysis

3. **Exercise 3**: Design a prompt that generates Python code with error handling

4. **Exercise 4**: Write a chain-of-thought prompt for a math problem

## Real-World Applications

### Customer Support
```
You are a customer support agent.
Help the user solve their problem professionally.
If you can't help, escalate to a human agent.
```

### Content Creation
```
Write a blog post outline about [topic]
Target audience: [audience]
Tone: [professional/casual/technical]
Include 5 main sections with bullet points.
```

### Code Generation
```
Generate a Python function that:
- Takes a list of numbers as input
- Returns the median value
- Handles edge cases (empty list, single element)
- Includes docstring and type hints
```

## Testing Your Prompts

1. **Clarity test**: Can someone else understand your prompt?
2. **Consistency test**: Same prompt, similar outputs?
3. **Edge cases**: How does it handle unusual inputs?
4. **Efficiency test**: Can you achieve the same result with fewer tokens?

## Next Steps

- **[Lesson 05: Creating Advanced Prompts](./Lesson-05-Advanced-Prompts)**

## Additional Resources

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Prompt Engineering Techniques](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)
- [Azure OpenAI Best Practices](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)

---
[← Previous: Using AI Responsibly](./Lesson-03-Using-GenAI-Responsibly) | [Back to Home](./Home) | [Next Lesson: Advanced Prompts →](./Lesson-05-Advanced-Prompts)
