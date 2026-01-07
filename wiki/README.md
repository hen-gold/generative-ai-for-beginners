# Wiki for Generative AI for Beginners

This directory contains the wiki content for the Generative AI for Beginners course.

## About This Wiki

The wiki provides:
- Easy navigation through all 21 lessons
- Quick reference guides and glossary
- Setup instructions and troubleshooting
- Community contribution guidelines
- FAQ for common questions

## Structure

### Core Pages
- **Home.md** - Main wiki landing page with course overview
- **_Sidebar.md** - Navigation sidebar for GitHub wiki

### Lesson Pages (Lesson-XX-*.md)
- One page for each of the 21 lessons
- Includes overview, learning objectives, key concepts
- Links to full lesson content in repository

### Resource Pages
- **Setup-Guide.md** - Comprehensive setup instructions
- **FAQ.md** - Frequently asked questions
- **Glossary.md** - Definitions of key terms
- **Contributing.md** - How to contribute to the course
- **Troubleshooting.md** - Common issues and solutions

## Using This Wiki on GitHub

### Method 1: Push to GitHub Wiki Repository

GitHub wikis are stored in a separate `.wiki` git repository. To publish this wiki:

```bash
# Clone the wiki repository (create wiki first in GitHub UI)
git clone https://github.com/hen-gold/generative-ai-for-beginners.wiki.git

# Copy wiki files
cp -r wiki/*.md generative-ai-for-beginners.wiki/

# Commit and push
cd generative-ai-for-beginners.wiki
git add .
git commit -m "Initialize wiki with all course content"
git push origin master
```

### Method 2: Manual Upload

1. Go to your repository on GitHub
2. Click "Wiki" tab
3. Click "Create the first page" or "New Page"
4. Copy content from `Home.md` to create home page
5. Repeat for other pages

### Method 3: Keep as Documentation

The wiki can also serve as additional documentation in the main repository:
- Reference from main README
- Use for internal documentation
- Include in GitHub Pages site

## Wiki Features

### Navigation
- **Home page** provides course overview and lesson index
- **Sidebar** (_Sidebar.md) enables quick navigation
- Each lesson links to previous/next and back to home

### Quick Links
- All lesson pages link to full content in repository
- Video links where available
- Additional resource links

### Search
GitHub wiki includes built-in search functionality across all pages.

## Maintenance

### Updating Wiki Content

1. Edit files in this directory
2. Test locally if desired
3. Push to GitHub wiki repository
4. Changes appear immediately

### Keeping in Sync

When lesson content is updated:
1. Review corresponding wiki page
2. Update key concepts/overview as needed
3. Maintain links to repository content

### Style Guidelines

- Use consistent formatting across pages
- Include navigation links at bottom of each page
- Keep content concise (detailed content in main lessons)
- Use emoji sparingly for visual organization
- Test all links before committing

## Contributing to Wiki

See [Contributing.md](./Contributing.md) for full guidelines.

**Quick tips:**
- Follow existing page structure
- Use relative links between wiki pages
- Include tracking IDs on Microsoft URLs
- Test all links
- Submit via pull request

## Questions?

- 💬 [Discord Community](https://aka.ms/genai-discord)
- 🐛 [GitHub Issues](https://github.com/microsoft/generative-ai-for-beginners/issues)
- 📧 Contact maintainers

---

**Ready to learn?** Start with [Home.md](./Home.md)!
