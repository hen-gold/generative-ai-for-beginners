# Contributing to Generative AI for Beginners

Thank you for your interest in contributing to this course! This guide will help you get started.

## Ways to Contribute

### 🐛 Report Issues
Found a bug or error? [Open an issue](https://github.com/microsoft/generative-ai-for-beginners/issues/new)

### 📝 Improve Documentation
Fix typos, clarify explanations, or add examples

### 💻 Submit Code
Improve code examples or fix bugs

### 🌐 Translate Content
Help make the course available in more languages

### 💡 Share Ideas
Suggest new lessons or improvements

## Getting Started

### 1. Fork the Repository

1. Visit [github.com/microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)
2. Click **Fork** button
3. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/generative-ai-for-beginners.git
   cd generative-ai-for-beginners
   ```

### 2. Create a Branch

```bash
git checkout -b fix/lesson-06-typo
# or
git checkout -b feature/add-rust-examples
```

**Branch naming:**
- `fix/` - Bug fixes
- `feature/` - New features
- `docs/` - Documentation changes
- `translation/` - Translation work

### 3. Make Your Changes

Follow the guidelines below based on what you're contributing.

## Contribution Guidelines

### Code Contributions

#### Python Code Style
- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints where appropriate
- Include docstrings for functions
- Keep examples simple and educational

```python
def generate_recipe(ingredients: list[str], dietary: str = None) -> str:
    """
    Generate a recipe based on ingredients.
    
    Args:
        ingredients: List of available ingredients
        dietary: Optional dietary restrictions
        
    Returns:
        Generated recipe as a string
    """
    # Implementation
```

#### TypeScript Code Style
- Use TypeScript with proper types
- Follow existing code formatting
- Include JSDoc comments
- Use async/await for promises

```typescript
/**
 * Generate a recipe based on ingredients
 * @param ingredients - List of available ingredients
 * @param dietary - Optional dietary restrictions
 * @returns Generated recipe
 */
async function generateRecipe(
  ingredients: string[],
  dietary?: string
): Promise<string> {
  // Implementation
}
```

#### Testing Your Code
```bash
# Python
python your_script.py

# TypeScript
npm run build
npm start
```

### Documentation Contributions

#### Markdown Style

✅ **Good:**
```markdown
Check out [Azure OpenAI](https://aka.ms/azure-openai?WT.mc_id=academic-105485-koreyst)
```

❌ **Bad:**
```markdown
Check out [Azure OpenAI](https://learn.microsoft.com/en-us/azure/openai)
```

**Rules:**
- All URLs must be in `[text](url)` format
- Microsoft URLs must include tracking ID: `?WT.mc_id=academic-105485-koreyst`
- No country-specific locales (`/en-us/` → `/`)
- Use relative links for internal pages: `./lesson-01/README.md`
- Start relative links with `./` or `../`

#### Adding Images
- Store in lesson's `images/` folder
- Use descriptive names: `setup-complete-screenshot.png`
- Optimize for web (< 500KB when possible)
- Include alt text: `![Setup complete dialog](./images/setup-complete.png)`

### Translation Contributions

**Important:** Translations are automated via GitHub Actions!

- **Do not** submit manual translations
- Translations are generated from English source
- Updates propagate automatically
- Translation issues? [Open an issue](https://github.com/microsoft/generative-ai-for-beginners/issues)

For adding a new language, contact the maintainers.

## Pull Request Process

### 1. Commit Your Changes

```bash
git add .
git commit -m "Fix typo in lesson 06 README"
```

**Commit message format:**
- Use present tense: "Add feature" not "Added feature"
- Be specific: "Fix API key validation in lesson 06"
- Reference issues: "Fixes #123"

### 2. Push to Your Fork

```bash
git push origin fix/lesson-06-typo
```

### 3. Create Pull Request

1. Go to your fork on GitHub
2. Click **New Pull Request**
3. Select your branch
4. Fill out the PR template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
How did you test your changes?

## Related Issues
Closes #123
```

### 4. Pass CI Checks

The automated checks validate:
- ✅ Markdown link format
- ✅ Tracking IDs on Microsoft URLs
- ✅ No country-specific locales
- ✅ Valid relative links

### 5. Respond to Feedback

Maintainers may request changes. To update your PR:

```bash
# Make changes
git add .
git commit -m "Address review feedback"
git push origin fix/lesson-06-typo
```

## Code of Conduct

This project follows the [Microsoft Open Source Code of Conduct](../CODE_OF_CONDUCT.md).

**Expected behavior:**
- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community

## Development Setup

### Prerequisites
- Git
- Python 3.9+
- Node.js (for TypeScript examples)
- VS Code (recommended)

### Environment Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.copy .env
# Add your API keys to .env
```

## Recognition

Contributors are recognized in several ways:
- Listed in GitHub contributors
- Mentioned in release notes for significant contributions
- Community recognition in Discord

## Questions?

- 💬 Ask in [Discord](https://aka.ms/genai-discord)
- 📧 Email the maintainers
- 💭 [Start a discussion](https://github.com/microsoft/generative-ai-for-beginners/discussions)

## Resources

- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [How to Write Good Commit Messages](https://chris.beams.io/posts/git-commit/)
- [Markdown Guide](https://www.markdownguide.org/)

---

Thank you for contributing to Generative AI education! 🚀

[Back to Home](./Home)
