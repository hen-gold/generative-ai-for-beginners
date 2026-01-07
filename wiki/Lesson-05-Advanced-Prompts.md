# Lesson 05: Creating Advanced Prompts

**Type:** Learn  
**Full Lesson:** [View in Repository](https://github.com/microsoft/generative-ai-for-beginners/tree/main/05-advanced-prompts)  
**Video:** [Watch on YouTube](https://aka.ms/gen-ai-lesson5-gh?WT.mc_id=academic-105485-koreyst)

## Overview

Take your prompt engineering skills to the next level with advanced techniques that improve the quality, consistency, and reliability of AI outputs.

## Learning Objectives

- Master advanced prompting techniques
- Implement complex prompt patterns
- Optimize prompts for specific outcomes
- Handle challenging scenarios

## Advanced Techniques

### 1. Chain-of-Thought (CoT) Prompting

Guides the model through step-by-step reasoning:

```
Question: If I have 15 apples and give away 3, then buy 7 more, 
then give half away, how many do I have?

Let's solve this step-by-step:
1. Start: 15 apples
2. Give away 3: 15 - 3 = 12 apples
3. Buy 7 more: 12 + 7 = 19 apples
4. Give half away: 19 / 2 = 9.5, so 9 apples (rounding down)

Answer: 9 apples
```

**Benefits:**
- Improved accuracy on complex problems
- Better reasoning transparency
- Easier to debug errors

### 2. Zero-Shot vs. Few-Shot vs. Many-Shot

**Zero-Shot** (no examples):
```
Classify the sentiment: "I love this product!"
```

**Few-Shot** (2-3 examples):
```
Classify sentiment:

Text: "Amazing service!"
Sentiment: Positive

Text: "Terrible experience"
Sentiment: Negative

Text: "It was okay"
Sentiment: Neutral

Text: "Best purchase ever!"
Sentiment: [Model completes]
```

**Many-Shot** (10+ examples): Best for complex patterns

### 3. Self-Consistency

Generate multiple responses and pick the most consistent:

```python
responses = []
for i in range(5):
    response = model.generate(prompt, temperature=0.7)
    responses.append(response)

# Choose most common answer
final_answer = most_common(responses)
```

### 4. Tree of Thoughts

Explore multiple reasoning paths:

```
Problem: Plan a 3-day trip to Paris

Approach 1: Budget-focused
- Day 1: Free museums, walk Champs-Élysées
- Day 2: Picnic at Eiffel Tower, explore Montmartre
- Day 3: Notre-Dame, Latin Quarter

Approach 2: Cultural immersion
- Day 1: Louvre full day
- Day 2: Musée d'Orsay, opera show
- Day 3: Versailles day trip

Approach 3: Food and experience
- Day 1: Cooking class, food market tour
- Day 2: Wine tasting, restaurant crawl
- Day 3: Pastry workshops, cafe hopping

Best approach for a young couple: Approach 3 (food-focused)
```

### 5. Program-Aided Language Models (PAL)

Combine natural language with code:

```
Question: Calculate compound interest for $1000 at 5% for 3 years

Let me write code to solve this:

```python
principal = 1000
rate = 0.05
time = 3
amount = principal * (1 + rate) ** time
interest = amount - principal
```

Result: $157.63 in interest, total amount $1157.63
```

### 6. ReAct (Reasoning + Acting)

Interleave reasoning and actions:

```
Task: Find the population of the capital of France

Thought: I need to first identify the capital of France
Action: Search "capital of France"
Observation: The capital is Paris

Thought: Now I need the population of Paris
Action: Search "population of Paris"
Observation: Paris has approximately 2.1 million people

Answer: The population of Paris (capital of France) is 
approximately 2.1 million people in the city proper.
```

### 7. Prompt Chaining

Break complex tasks into sequential prompts:

```python
# Step 1: Extract information
extract_prompt = "Extract key points from this article: ..."
key_points = model.generate(extract_prompt)

# Step 2: Analyze sentiment
analyze_prompt = f"Analyze the sentiment of these points: {key_points}"
sentiment = model.generate(analyze_prompt)

# Step 3: Generate summary
summary_prompt = f"Create a summary combining points: {key_points} 
with sentiment: {sentiment}"
final_summary = model.generate(summary_prompt)
```

## Advanced Patterns

### Constitutional AI

Add principles and safeguards:

```
You are a helpful assistant that follows these principles:
1. Always prioritize user safety
2. Admit when you don't know something
3. Avoid making assumptions about the user
4. Provide balanced perspectives on controversial topics
5. Cite sources when making factual claims

Now answer: [user question]
```

### Meta-Prompting

Prompt about prompting:

```
Generate an effective prompt to help someone learn Python.
The prompt should:
- Be clear and specific
- Include context about the learner (beginner)
- Suggest a learning path
- Encourage hands-on practice
```

### Prompt Compression

Reduce tokens while maintaining meaning:

```
Original (50 tokens):
"Please carefully analyze this customer feedback and provide 
a detailed summary of the main concerns, categorizing them by 
topic and including the frequency of each concern type."

Compressed (25 tokens):
"Analyze feedback. Summarize main concerns by topic with frequency counts."
```

## Optimization Techniques

### 1. A/B Testing Prompts

```python
prompt_a = "Explain [topic] simply"
prompt_b = "You are a teacher. Explain [topic] to a beginner"

# Test and measure which performs better
results_a = test_prompt(prompt_a, test_cases)
results_b = test_prompt(prompt_b, test_cases)
```

### 2. Prompt Templates

Create reusable structures:

```python
ANALYSIS_TEMPLATE = """
Context: {context}
Task: Analyze the following {data_type}
Focus on: {focus_areas}
Output format: {output_format}

Data: {data}

Analysis:
"""

# Use template
prompt = ANALYSIS_TEMPLATE.format(
    context="Customer feedback analysis",
    data_type="reviews",
    focus_areas="sentiment and key themes",
    output_format="bullet points",
    data=reviews
)
```

### 3. Dynamic Prompting

Adjust based on context:

```python
def create_prompt(user_level, topic):
    if user_level == "beginner":
        context = "You are a patient teacher for beginners"
    elif user_level == "advanced":
        context = "You are an expert providing advanced insights"
    
    return f"{context}\n\nExplain {topic}"
```

## Handling Edge Cases

### Dealing with Refusals

❌ Model refuses: "I can't help with that"

✅ Reframe:
```
Instead of: "How do I hack a website?"
Try: "Explain common website security vulnerabilities so I 
can protect my own website"
```

### Reducing Hallucinations

```
Answer based ONLY on the information below. If the answer isn't 
in the text, say "Information not available."

Context: [provided text]

Question: [question]
```

### Maintaining Consistency

```
Remember these key facts throughout our conversation:
- User's name: Alice
- Context: Project planning meeting
- Goal: Finalize Q1 roadmap

Now, let's begin...
```

## Practical Applications

### Code Review Prompt

```
Review this code for:
1. Security vulnerabilities
2. Performance issues  
3. Code style violations
4. Potential bugs

Provide specific line numbers and suggested fixes.

Code:
```python
[code here]
```
```

### Creative Writing Prompt

```
Write a short story with these constraints:
- Genre: Sci-fi mystery
- Setting: Mars colony, 2150
- Characters: 2 main, 3 supporting
- Tone: Suspenseful but hopeful
- Length: 500 words
- Must include: A hidden message, a red robot, oxygen shortage
```

## Best Practices for Advanced Prompting

✅ Test with diverse inputs  
✅ Measure performance objectively  
✅ Version control your prompts  
✅ Document what works and what doesn't  
✅ Combine techniques for best results  
✅ Monitor costs (complex prompts use more tokens)  
✅ Balance complexity with maintainability  

## Hands-On Exercises

1. Create a chain-of-thought prompt for a logic puzzle
2. Implement prompt chaining for a multi-step task
3. Build a self-consistency system for fact-checking
4. Design a ReAct prompt for research tasks

## Next Steps

- **[Lesson 06: Building Text Generation Applications](./Lesson-06-Text-Generation-Apps)**

## Additional Resources

- [Advanced Prompt Engineering](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)
- [Chain-of-Thought Paper](https://arxiv.org/abs/2201.11903)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

---
[← Previous: Prompt Engineering Fundamentals](./Lesson-04-Prompt-Engineering-Fundamentals) | [Back to Home](./Home) | [Next Lesson: Text Generation Apps →](./Lesson-06-Text-Generation-Apps)
