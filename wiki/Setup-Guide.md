# Complete Setup Guide

This comprehensive guide will help you set up your environment for the Generative AI for Beginners course.

## Choose Your Setup Method

### 🌐 Option 1: GitHub Codespaces (Recommended)
Best for quick start, no local installation needed.

### 💻 Option 2: Local Development
Best for offline work and full control.

### ☁️ Option 3: Azure Cloud Shell
Best for Azure-focused development.

## GitHub Codespaces Setup

### Step 1: Fork the Repository

1. Visit the [course repository](https://github.com/microsoft/generative-ai-for-beginners)
2. Click **Fork** in the top-right corner
3. Create fork in your personal account

### Step 2: Create Codespace

1. In your fork, click **Code** button
2. Select **Codespaces** tab
3. Click **Create codespace on main**
4. Wait for environment to build (2-5 minutes)

### Step 3: Configure API Keys

#### Method A: Codespace Secrets (Recommended)

1. Click gear icon ⚙️ in bottom-left
2. Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
3. Type "Codespaces: Manage User Secrets"
4. Add secrets:
   - `OPENAI_API_KEY`
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_ENDPOINT`
   - `GITHUB_TOKEN`

#### Method B: Environment File

1. Copy `.env.copy` to `.env`
2. Edit `.env` with your API keys
3. Never commit `.env` to git

### Step 4: Verify Setup

```bash
# Test Python
python --version

# Test pip packages
pip list | grep openai

# Test Node.js (optional)
node --version
```

## Local Development Setup

### Prerequisites

- **Git**: [Download](https://git-scm.com/downloads)
- **Python 3.9+**: [Download](https://www.python.org/downloads/)
- **Node.js** (optional): [Download](https://nodejs.org/)
- **VS Code**: [Download](https://code.visualstudio.com/)

### Step 1: Clone Repository

```bash
# Fork first on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/generative-ai-for-beginners.git
cd generative-ai-for-beginners
```

### Step 2: Python Environment

#### Windows

```cmd
# Create virtual environment
python -m venv venv

# Activate
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### macOS/Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Node.js Setup (Optional)

```bash
# Install global packages
npm install -g npm@latest

# For TypeScript lessons, navigate to specific lesson
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Step 4: Configure Environment Variables

```bash
# Copy template
cp .env.copy .env

# Edit .env with your favorite editor
code .env  # VS Code
nano .env  # Terminal editor
```

Add your credentials:

```env
# OpenAI
OPENAI_API_KEY=sk-...

# Azure OpenAI
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=https://....openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-35-turbo
AZURE_OPENAI_API_VERSION=2024-02-01

# GitHub Models (optional)
GITHUB_TOKEN=ghp_...
```

### Step 5: Test Your Setup

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Run test script
python -c "import openai; print('✓ OpenAI installed')"
python -c "from dotenv import load_dotenv; print('✓ dotenv installed')"
```

## API Provider Setup

### OpenAI API

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to **API Keys**
4. Click **Create new secret key**
5. Copy key and save securely
6. Add to `.env` as `OPENAI_API_KEY`

**Pricing**: Pay-as-you-go, starts at $0.002/1K tokens

### Azure OpenAI Service

1. Have an Azure subscription ([free trial](https://azure.microsoft.com/free/))
2. Request access to [Azure OpenAI](https://aka.ms/oai/access)
3. Create Azure OpenAI resource:
   ```bash
   az cognitiveservices account create \
     --name my-openai \
     --resource-group my-rg \
     --kind OpenAI \
     --sku S0 \
     --location eastus
   ```
4. Deploy a model (gpt-35-turbo or gpt-4)
5. Get keys and endpoint from Azure Portal
6. Add to `.env`

### GitHub Models (Free Tier)

1. Have a GitHub account
2. Visit [GitHub Models](https://github.com/marketplace/models)
3. Generate Personal Access Token:
   - Settings → Developer settings → Personal access tokens
   - Generate new token (classic)
   - Select scopes: `repo`, `read:org`
4. Add token to `.env` as `GITHUB_TOKEN`

## IDE Configuration

### VS Code Extensions

Install these extensions for the best experience:

- **Python** (ms-python.python)
- **Jupyter** (ms-toolsai.jupyter)
- **TypeScript** (ms-vscode.typescript)
- **ESLint** (dbaeumer.vscode-eslint)
- **GitLens** (eamodio.gitlens)

### Jupyter Notebooks

```bash
# Install Jupyter
pip install jupyter

# Start Jupyter
jupyter notebook

# Or use VS Code's built-in notebook support
```

## Troubleshooting

### Python Command Not Found

**Windows**: Install from [python.org](https://www.python.org/downloads/), ensure "Add to PATH" is checked

**macOS**: 
```bash
brew install python3
```

**Linux**:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Virtual Environment Issues

```bash
# Deactivate and recreate
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Module Not Found Errors

```bash
# Ensure virtual environment is activated
which python  # Should show venv path

# Reinstall requirements
pip install -r requirements.txt
```

### API Authentication Errors

- Verify API key is correct (no extra spaces)
- Check key hasn't expired
- Ensure sufficient credits/quota
- Confirm endpoint URL is correct (Azure)

### Codespace Build Stuck

1. Cancel the build
2. Delete the codespace
3. Create a new one
4. If problem persists, try "Rebuild Container"

## Next Steps

Once your environment is ready:

1. ✅ Test with [Lesson 00](./Lesson-00-Course-Setup)
2. ✅ Start learning with [Lesson 01](./Lesson-01-Introduction-to-GenAI)
3. ✅ Join the [Discord community](https://aka.ms/genai-discord)

## Additional Resources

- [GitHub Codespaces Docs](https://docs.github.com/en/codespaces)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [OpenAI Quickstart](https://platform.openai.com/docs/quickstart)
- [Azure OpenAI Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart)

---
[Back to Home](./Home)
