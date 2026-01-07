# Troubleshooting Guide

Common issues and their solutions when working with the Generative AI for Beginners course.

## Setup Issues

### Codespace Won't Start

**Symptoms:**
- Codespace creation hangs
- Build fails after 10+ minutes
- Container won't start

**Solutions:**

1. **Clear browser cache and cookies**
   ```
   Chrome: Settings → Privacy → Clear browsing data
   Firefox: Settings → Privacy → Clear Data
   ```

2. **Try a different browser**
   - Chrome/Edge (Chromium-based recommended)
   - Clear extensions that might interfere

3. **Delete and recreate Codespace**
   ```
   1. Go to your fork
   2. Code → Codespaces → Click "..."
   3. Delete codespace
   4. Create new codespace
   ```

4. **Rebuild container**
   - Open Command Palette (Ctrl/Cmd + Shift + P)
   - Select "Codespaces: Rebuild Container"

5. **Check GitHub Status**
   - Visit [githubstatus.com](https://www.githubstatus.com/)

### Local Clone Issues

**Problem: `git clone` fails**

```bash
# Use HTTPS instead of SSH if SSH fails
git clone https://github.com/YOUR_USERNAME/generative-ai-for-beginners.git

# If behind proxy
git config --global http.proxy http://proxyserver:port
```

**Problem: Large repository, slow download**

```bash
# Shallow clone (faster, less history)
git clone --depth 1 https://github.com/YOUR_USERNAME/generative-ai-for-beginners.git
```

## Python Issues

### Python Not Found

**Windows:**
```cmd
# Check if Python is installed
python --version
# or
py --version

# Not installed? Download from python.org
# During install, check "Add Python to PATH"
```

**macOS:**
```bash
# Install using Homebrew
brew install python3

# Or download from python.org
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Fedora
sudo dnf install python3 python3-pip
```

### Virtual Environment Issues

**Problem: `venv` module not found**

```bash
# Ubuntu/Debian
sudo apt install python3-venv

# macOS (use system Python or Homebrew)
python3 -m pip install virtualenv
```

**Problem: Activation script not found**

```bash
# Recreate venv
rm -rf venv
python3 -m venv venv

# Activate
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

**Problem: Wrong Python version in venv**

```bash
# Specify Python version explicitly
python3.9 -m venv venv
# or
python3.11 -m venv venv
```

### Package Installation Issues

**Problem: `pip install` fails**

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install with verbose output to see errors
pip install -r requirements.txt -v

# Clear cache and reinstall
pip cache purge
pip install -r requirements.txt
```

**Problem: Permission denied**

```bash
# Don't use sudo! Use virtual environment instead
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Problem: SSL certificate errors**

```bash
# Temporary workaround (not recommended for production)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Better: Update certificates
# macOS: Install Certificates.command in Python folder
# Windows: Update via Windows Update
```

### Import Errors

**Problem: `ModuleNotFoundError: No module named 'openai'`**

```bash
# Ensure venv is activated
which python  # Should show venv path

# If not in venv, activate
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

## Node.js / TypeScript Issues

### Node/npm Not Found

```bash
# Install Node.js from nodejs.org
# or use nvm (Node Version Manager)

# Check installation
node --version
npm --version
```

### npm Install Failures

```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install

# Try with legacy peer deps if still failing
npm install --legacy-peer-deps
```

### TypeScript Compilation Errors

```bash
# Install TypeScript globally
npm install -g typescript

# Check version
tsc --version

# Compile with verbose output
npm run build -- --verbose
```

## API Issues

### Authentication Errors (401)

**OpenAI:**
```python
# Check API key format
# Should start with "sk-"
# Example: sk-proj-xxxxx

# Verify key works
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

**Azure OpenAI:**
```bash
# Check all required variables
echo $AZURE_OPENAI_API_KEY
echo $AZURE_OPENAI_ENDPOINT
echo $AZURE_OPENAI_DEPLOYMENT

# Endpoint should be like:
# https://YOUR_RESOURCE.openai.azure.com/
```

**Common mistakes:**
- ❌ Extra spaces in API key
- ❌ Wrong environment variable name
- ❌ API key expired or revoked
- ❌ `.env` file not loaded
- ❌ Wrong .env location

### Rate Limit Errors (429)

**Solution:**
```python
import time
from openai import OpenAI, RateLimitError

client = OpenAI()

def call_with_retry(prompt, max_retries=3):
    for i in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response
        except RateLimitError:
            if i < max_retries - 1:
                wait_time = (2 ** i) * 1  # Exponential backoff
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
```

**Also check:**
- API quota/credits remaining
- Upgrade plan if needed
- Reduce request frequency

### Timeout Errors

```python
# Increase timeout
from openai import OpenAI

client = OpenAI(timeout=60.0)  # 60 seconds

# Or reduce max_tokens to get faster response
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...],
    max_tokens=500  # Lower than default
)
```

### Connection Errors

```bash
# Check internet connection
ping api.openai.com

# Check if behind firewall/proxy
# Configure proxy if needed
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port
```

## Jupyter Notebook Issues

### Kernel Not Found

**In VS Code:**
1. Open Command Palette (Ctrl/Cmd + Shift + P)
2. "Jupyter: Select Interpreter"
3. Choose Python from your venv

**In Jupyter:**
```bash
# Install ipykernel
pip install ipykernel

# Add kernel
python -m ipykernel install --user --name=venv

# Select kernel in Jupyter notebook
```

### Notebook Won't Start

```bash
# Reinstall Jupyter
pip uninstall jupyter
pip install jupyter

# Start with verbose output
jupyter notebook --debug
```

### Cell Execution Hangs

- Click "Interrupt Kernel" button
- Restart kernel: Kernel → Restart
- Check for infinite loops in code

## Environment Variable Issues

### `.env` File Not Working

**Check file location:**
```bash
# Should be in repository root
ls -la .env

# If not there, create it
cp .env.copy .env
```

**Verify format:**
```bash
# Correct format (no quotes, spaces, or comments on same line)
OPENAI_API_KEY=sk-xxxxx
AZURE_OPENAI_ENDPOINT=https://xxx.openai.azure.com/

# Wrong formats
OPENAI_API_KEY = "sk-xxxxx"  # No quotes, no spaces around =
OPENAI_API_KEY=sk-xxxxx # comment  # Comment on new line
```

**Load in Python:**
```python
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Verify loaded
print("API Key loaded:", bool(os.getenv("OPENAI_API_KEY")))
```

### Codespace Secrets Not Working

1. **Set secret**: Gear icon → Command Palette → "Codespaces: Manage User Secrets"
2. **Restart Codespace** after adding secrets
3. **Check in terminal**:
   ```bash
   echo $OPENAI_API_KEY
   ```

## Git Issues

### Merge Conflicts

```bash
# Pull latest changes
git pull origin main

# If conflicts occur
# 1. Open conflicted files
# 2. Resolve conflicts (remove <<<, ===, >>> markers)
# 3. Stage and commit
git add .
git commit -m "Resolve merge conflicts"
```

### Accidental Commits

```bash
# Undo last commit (keep changes)
git reset HEAD~1

# Undo last commit (discard changes) - CAREFUL!
git reset --hard HEAD~1

# Remove file from git but keep locally
git rm --cached .env
```

### Large Files

```bash
# If accidentally committed large files
# Add to .gitignore
echo "large_file.bin" >> .gitignore

# Remove from git
git rm --cached large_file.bin
git commit -m "Remove large file"
```

## Performance Issues

### Slow Response Times

**Use faster model:**
```python
# Instead of gpt-4
model="gpt-3.5-turbo"  # Much faster

# Or use streaming
for chunk in client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...],
    stream=True
):
    print(chunk.choices[0].delta.content, end="")
```

**Reduce tokens:**
```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...],
    max_tokens=150  # Limit response length
)
```

### High API Costs

**Monitor usage:**
- OpenAI: https://platform.openai.com/usage
- Azure: Portal → Your Resource → Metrics

**Reduce costs:**
1. Use GPT-3.5 instead of GPT-4 when possible
2. Implement caching for repeated queries
3. Reduce max_tokens
4. Lower temperature for deterministic tasks
5. Use prompt compression techniques

## Still Having Issues?

### Get Help

1. **Search existing issues**: [GitHub Issues](https://github.com/microsoft/generative-ai-for-beginners/issues)
2. **Ask in Discord**: [Join community](https://aka.ms/genai-discord)
3. **Open new issue**: Include:
   - Operating system
   - Python/Node version
   - Error messages (full stack trace)
   - Steps to reproduce

### Provide Useful Information

When asking for help, include:

```bash
# System info
uname -a  # macOS/Linux
systeminfo  # Windows

# Python info
python --version
pip list

# Node info (if applicable)
node --version
npm --version

# Environment
echo $OPENAI_API_KEY | head -c 10  # First 10 chars only!
```

---
[Back to Home](./Home)
