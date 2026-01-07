# Lesson 01: Introduction to Generative AI and LLMs

**Type:** Learn  
**Full Lesson:** [View in Repository](https://github.com/microsoft/generative-ai-for-beginners/tree/main/01-introduction-to-genai)  
**Video:** [Watch on YouTube](https://aka.ms/gen-ai-lesson-1-gh?WT.mc_id=academic-105485-koreyst)

## Overview

This lesson introduces you to Generative AI and Large Language Models (LLMs). You'll learn what makes generative AI different from previous AI approaches, how LLMs work, and what they can be used for.

## Learning Objectives

After completing this lesson, you will understand:

- What Generative AI is and its capabilities
- How Large Language Models (LLMs) work
- The evolution from traditional AI to modern Generative AI
- Key concepts: tokens, embeddings, transformers
- Practical use cases for LLMs in education and beyond

## Key Concepts

### What is Generative AI?

Generative AI is artificial intelligence capable of generating text, images, and other types of content. Unlike traditional AI that classifies or analyzes data, generative AI creates new content based on patterns learned during training.

**Key characteristics:**
- Creates original content
- Works with natural language prompts
- Accessible to everyone (no coding required for basic use)
- Can handle multiple types of content (text, images, code, etc.)

### The Evolution of AI

**1960s-1990s:** Rule-based chatbots with hardcoded knowledge bases

**1990s:** Statistical approach and machine learning
- Models learn patterns from data
- Text classification and sentiment analysis

**2000s-2010s:** Neural networks and virtual assistants
- Recurrent Neural Networks (RNNs)
- Better natural language understanding
- Context-aware responses

**Present:** Generative AI and Transformers
- Transformer architecture (attention mechanism)
- Large Language Models trained on massive datasets
- Ability to generate coherent, creative text

### How LLMs Work

#### 1. Tokenization
Text is converted to numbers (tokens) that the model can process:
```
"Hello world" → [15496, 995] → Model processes → [2534] → "!"
```

#### 2. Prediction
- Model predicts the next token based on input
- Uses probability distribution across all possible tokens
- Adds randomness for creativity (controlled by "temperature")

#### 3. Generation
- Predicted token is added to input
- Process repeats in a loop
- Creates coherent, multi-sentence responses

### Transformer Architecture

The breakthrough that enabled modern LLMs:

- **Attention mechanism**: Model focuses on relevant parts of input
- **Parallel processing**: Faster training on large datasets
- **Context understanding**: Handles long text sequences
- **Transfer learning**: Pre-trained models can be fine-tuned

## Our Educational Startup Scenario

Throughout this course, we'll explore how a fictional startup uses Generative AI to:

- Improve accessibility in learning globally
- Provide personalized learning experiences
- Offer 24/7 virtual teaching assistance
- Help teachers with assessment and feedback

## Practical Applications

### In Education:
- Personalized tutoring and explanations
- Automated grading and feedback
- Content generation for learning materials
- Language translation for global access

### General Use Cases:
- Content creation and writing assistance
- Code generation and debugging
- Question answering and research
- Creative brainstorming

## Key Takeaways

✅ Generative AI democratizes AI - anyone can use it with natural language  
✅ LLMs work by predicting tokens and generating text probabilistically  
✅ Transformer architecture enables modern LLM capabilities  
✅ Applications span education, business, creative work, and more  

## Hands-On Activities

1. Try ChatGPT or Bing Chat to see generative AI in action
2. Experiment with different prompts and observe the responses
3. Notice how the same prompt can yield different results

## Next Steps

Continue your learning journey:
- **[Lesson 02: Exploring and Comparing Different LLMs](./Lesson-02-Exploring-and-Comparing-LLMs)**

## Additional Resources

- [Microsoft Learn: Introduction to Azure OpenAI Service](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)
- [Attention Is All You Need - Original Transformer Paper](https://arxiv.org/abs/1706.03762)
- [OpenAI GPT Documentation](https://platform.openai.com/docs/models)

---
[← Previous: Course Setup](./Lesson-00-Course-Setup) | [Back to Home](./Home) | [Next Lesson: Exploring LLMs →](./Lesson-02-Exploring-and-Comparing-LLMs)
