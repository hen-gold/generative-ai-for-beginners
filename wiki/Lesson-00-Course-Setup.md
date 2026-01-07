# Lesson 00: Course Setup

**Type:** Learn  
**Full Lesson:** [View in Repository](https://github.com/microsoft/generative-ai-for-beginners/tree/main/00-course-setup)

## Overview

This lesson helps you set up your development environment to start learning and building with Generative AI. You'll learn how to configure your workspace, set up necessary tools, and prepare for the rest of the course.

## What You'll Learn

- How to fork and clone the repository
- Setting up GitHub Codespaces or local development environment
- Configuring API keys for OpenAI, Azure OpenAI, or GitHub Models
- Troubleshooting common setup issues

## Setup Options

### Option 1: GitHub Codespaces (Recommended)
GitHub Codespaces provides a cloud-based development environment with everything pre-configured:

1. Fork the repository to your GitHub account
2. Create a new Codespace from your fork
3. Add your API keys as Codespace secrets
4. Start coding!

**Benefits:**
- No local installation required
- Pre-configured environment
- Works from any device with a browser

### Option 2: Local Development
For those who prefer working on their local machine:

1. Fork and clone the repository
2. Install Python 3.9+ and/or Node.js
3. Set up a virtual environment (Python)
4. Install dependencies from `requirements.txt` (Python) or `package.json` (Node.js)
5. Configure `.env` file with your API keys

## Required Tools

- **Git** - Version control
- **Python 3.9+** (for Python examples)
- **Node.js** (for TypeScript examples)
- **VS Code** (recommended editor)
- **Jupyter** (for notebook examples)

## API Provider Options

You can use any of these providers throughout the course:

1. **Azure OpenAI Service** - Microsoft's enterprise-grade OpenAI service
2. **OpenAI API** - Direct access to OpenAI models
3. **GitHub Models** - Free tier for experimentation

See the [Providers Guide](https://github.com/microsoft/generative-ai-for-beginners/blob/main/00-course-setup/03-providers.md) for detailed setup instructions.

## Environment Variables

Create a `.env` file in the repository root with your API credentials:

```bash
# OpenAI
OPENAI_API_KEY=your_openai_key

# Azure OpenAI
AZURE_OPENAI_API_KEY=your_azure_key
AZURE_OPENAI_ENDPOINT=your_endpoint_url
AZURE_OPENAI_DEPLOYMENT=your_deployment_name
AZURE_OPENAI_API_VERSION=2024-02-01

# GitHub Models
GITHUB_TOKEN=your_github_token
```

## Common Issues

| Symptom | Fix |
|---------|-----|
| Container build stuck > 10 min | Rebuild Container in Codespaces |
| `python: command not found` | Create new terminal session |
| `401 Unauthorized` from OpenAI | Check API key is correct and not expired |
| Notebook kernel missing | Select Python 3 kernel from notebook menu |

## Next Steps

Once your environment is set up, continue to:
- **[Lesson 01: Introduction to Generative AI](./Lesson-01-Introduction-to-GenAI)**

## Additional Resources

- [Setup Local Guide](https://github.com/microsoft/generative-ai-for-beginners/blob/main/00-course-setup/02-setup-local.md)
- [Providers Guide](https://github.com/microsoft/generative-ai-for-beginners/blob/main/00-course-setup/03-providers.md)
- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)

---
[← Back to Home](./Home) | [Next Lesson: Introduction to GenAI →](./Lesson-01-Introduction-to-GenAI)
