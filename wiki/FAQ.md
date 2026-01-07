# Frequently Asked Questions (FAQ)

## General Questions

### Q: Who is this course for?

**A:** This course is designed for beginners who want to learn about Generative AI and build applications. Basic programming knowledge (Python or TypeScript) is helpful but not required.

### Q: Do I need to pay for API access?

**A:** You have several options:
- **GitHub Models**: Free tier available for experimentation
- **OpenAI**: Pay-as-you-go (typically $5-20 for the course)
- **Azure OpenAI**: Requires Azure subscription (free trial available)

### Q: How long does it take to complete the course?

**A:** At your own pace, 2-4 weeks if spending 5-10 hours per week. Each lesson takes 1-3 hours.

### Q: Can I get a certificate?

**A:** This is a free, self-paced course. While there's no official certificate, you can showcase your GitHub projects and learnings.

## Technical Questions

### Q: Which programming language should I use?

**A:** Most lessons provide examples in both **Python** and **TypeScript**. Choose based on your preference:
- **Python**: Recommended for beginners, widely used in AI
- **TypeScript**: Great for web developers

### Q: Do I need a powerful computer?

**A:** No! The models run on the cloud via APIs. You just need:
- Internet connection
- Modern browser (for Codespaces) OR
- Basic computer for local development

### Q: Can I use a different model provider?

**A:** Yes! The concepts apply to any LLM provider. You may need to adjust the code slightly for different APIs.

### Q: What if I'm completely new to programming?

**A:** We recommend learning Python basics first:
- [Python for Beginners](https://aka.ms/genai-beginners/python)
- [TypeScript Basics](https://aka.ms/genai-beginners/typescript)

## Setup Issues

### Q: My Codespace won't start

**A:** Try these steps:
1. Clear browser cache
2. Try a different browser
3. Delete and recreate the Codespace
4. Check GitHub status page

### Q: I get "401 Unauthorized" errors

**A:** This means your API key is invalid or expired:
- Verify the key is correct (no extra spaces)
- Check if you have credits/quota remaining
- Generate a new key if needed

### Q: Packages won't install

**A:** Common solutions:
```bash
# Upgrade pip
pip install --upgrade pip

# Clear cache
pip cache purge

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

### Q: I can't find my `.env` file

**A:** The `.env` file is hidden by default:
- **VS Code**: It should be visible in the file explorer
- **Terminal**: Use `ls -la` to see hidden files
- **Create it**: Copy from `.env.copy` if missing

## Cost & Billing

### Q: How much will this course cost?

**A:** Typical costs:
- **GitHub Models**: Free tier available
- **OpenAI GPT-3.5**: ~$5-10 for entire course
- **OpenAI GPT-4**: ~$15-30 for entire course
- **Azure**: Similar to OpenAI, free credits available

### Q: How do I monitor my API usage?

**A:** 
- **OpenAI**: Check [Usage Dashboard](https://platform.openai.com/usage)
- **Azure**: Monitor in Azure Portal
- Set up billing alerts to avoid surprises

### Q: Can I use free models?

**A:** Yes! Options include:
- GitHub Models (free tier)
- Hugging Face models (free, self-hosted)
- Local models (if you have GPU)

## Learning Path

### Q: Must I complete lessons in order?

**A:** We recommend following the order, especially for lessons 00-05 (foundations). Later lessons can be more flexible based on your interests.

### Q: Can I skip lessons?

**A:** Yes, but note dependencies:
- Lessons 00-05: Build foundational knowledge
- Lessons 06-11: Each teaches different application types
- Lessons 12-21: Advanced topics, more independent

### Q: Where can I find help?

**A:** Multiple support options:
- **Discord**: [Join our community](https://aka.ms/genai-discord)
- **GitHub Issues**: Report bugs or ask questions
- **Discussions**: Ask in GitHub Discussions
- **Microsoft Learn**: Additional resources

### Q: What should I build after finishing?

**A:** Ideas for projects:
- Personal chatbot with your data
- Study assistant for students
- Code documentation generator
- Content creation tool
- Custom search engine

## Advanced Topics

### Q: How do I fine-tune a model?

**A:** See [Lesson 18: Fine-Tuning](./Lesson-18-Fine-Tuning) for detailed guidance.

### Q: Can I use my own data?

**A:** Yes! [Lesson 15: RAG](./Lesson-15-RAG-and-Vector-Databases) covers this in detail.

### Q: What about using this in production?

**A:** Key considerations:
- Implement proper error handling
- Add content filtering
- Monitor costs and usage
- Follow security best practices (Lesson 13)
- Consider SLAs and reliability

### Q: How do I deploy my application?

**A:** Options include:
- **Azure**: App Service, Container Apps, Functions
- **Vercel/Netlify**: For web applications
- **AWS**: Lambda, ECS, Elastic Beanstalk
- **Google Cloud**: Cloud Run, App Engine

## Community & Contributing

### Q: How can I contribute?

**A:** See our [Contributing Guide](./Contributing):
- Report issues
- Fix bugs
- Improve documentation
- Add translations
- Share your projects

### Q: Can I translate the course?

**A:** Yes! We have automated translation workflows. Contact the team or submit a translation PR.

### Q: Is there a community?

**A:** Yes! Join our active community:
- [Discord Server](https://aka.ms/genai-discord)
- [GitHub Discussions](https://github.com/microsoft/generative-ai-for-beginners/discussions)
- Follow on social media

## Still Have Questions?

- 💬 [Ask on Discord](https://aka.ms/genai-discord)
- 🐛 [Open a GitHub Issue](https://github.com/microsoft/generative-ai-for-beginners/issues)
- 💡 [Start a Discussion](https://github.com/microsoft/generative-ai-for-beginners/discussions)

---
[Back to Home](./Home)
