# How to Deploy the Wiki

This guide explains how to deploy the wiki content to GitHub's wiki feature.

## What Was Created

A comprehensive wiki with **30 pages**:

### Main Pages
- **Home.md** - Landing page with full course overview
- **_Sidebar.md** - Navigation sidebar

### Lesson Pages (22 pages)
- Lesson 00-21: One page per lesson with overview, objectives, and links

### Resource Pages (6 pages)
- **Setup-Guide.md** - Complete environment setup instructions
- **FAQ.md** - Frequently asked questions
- **Glossary.md** - Comprehensive terminology reference
- **Contributing.md** - Contribution guidelines
- **Troubleshooting.md** - Common issues and solutions
- **README.md** - Wiki documentation and usage guide

## Deployment Options

### Option 1: GitHub Wiki (Recommended)

GitHub provides a built-in wiki feature for each repository. To enable and populate it:

#### Step 1: Enable Wiki
1. Go to your repository: `https://github.com/hen-gold/generative-ai-for-beginners`
2. Click **Settings** tab
3. Scroll to **Features** section
4. Check **Wikis** checkbox

#### Step 2: Clone Wiki Repository
Each GitHub wiki is a separate git repository:

```bash
# Clone the wiki repo (after enabling wiki)
git clone https://github.com/hen-gold/generative-ai-for-beginners.wiki.git

# Navigate to wiki repo
cd generative-ai-for-beginners.wiki
```

#### Step 3: Copy Wiki Files
```bash
# Copy all wiki markdown files from your main repo
# Assuming you're in the wiki directory and main repo is ../generative-ai-for-beginners
cp ../generative-ai-for-beginners/wiki/*.md .

# Check what was copied
ls -la *.md
```

#### Step 4: Commit and Push
```bash
# Add all files
git add .

# Commit
git commit -m "Initialize wiki with complete course documentation"

# Push to wiki
git push origin master
```

#### Step 5: View Your Wiki
Visit: `https://github.com/hen-gold/generative-ai-for-beginners/wiki`

### Option 2: GitHub Pages

Use the wiki as part of a GitHub Pages site:

#### Create a docs site
```bash
# In your main repository
mkdir -p docs/wiki
cp wiki/*.md docs/wiki/

# Create index
cat > docs/index.md << 'EOF'
# Generative AI for Beginners

[View Wiki](./wiki/Home.md)
EOF

# Commit and push
git add docs/
git commit -m "Add wiki to docs folder"
git push
```

#### Enable GitHub Pages
1. Go to **Settings** → **Pages**
2. Source: Deploy from branch
3. Branch: `main` (or your branch)
4. Folder: `/docs`
5. Save

Your wiki will be at: `https://hen-gold.github.io/generative-ai-for-beginners/wiki/Home.html`

### Option 3: Keep in Repository

Simply use the wiki directory as documentation within the repository:

```markdown
# Add to main README.md
## 📖 Documentation

Check out our comprehensive [Wiki](./wiki/Home.md) for:
- Complete course guide
- Setup instructions
- Troubleshooting
- FAQ and glossary
```

## Wiki Navigation

The wiki includes built-in navigation:

### Sidebar Navigation
The `_Sidebar.md` file provides persistent navigation on GitHub wiki pages:
- Links to all lessons
- Quick access to resources
- Organized by course sections

### Page Navigation
Each lesson page includes:
- Link to previous lesson
- Link to next lesson  
- Link back to Home

Example footer:
```markdown
[← Previous: Lesson 05](./Lesson-05) | [Back to Home](./Home) | [Next: Lesson 07 →](./Lesson-07)
```

## Maintaining the Wiki

### Updating Content

When lesson content changes:

1. **Update wiki page** (in main repo)
   ```bash
   cd /path/to/generative-ai-for-beginners
   # Edit wiki/Lesson-XX-*.md
   git add wiki/
   git commit -m "Update wiki: lesson XX"
   git push
   ```

2. **Sync to GitHub wiki** (if using Option 1)
   ```bash
   cd /path/to/generative-ai-for-beginners.wiki
   cp ../generative-ai-for-beginners/wiki/*.md .
   git add .
   git commit -m "Update from main repository"
   git push origin master
   ```

### Adding New Pages

1. Create new `.md` file in wiki directory
2. Add link in `_Sidebar.md` for navigation
3. Add link in `Home.md` if appropriate
4. Follow existing page structure
5. Commit and sync to GitHub wiki

### Best Practices

✅ Keep wiki concise - detailed content in lessons  
✅ Update wiki when adding/changing lessons  
✅ Test all links before publishing  
✅ Use consistent formatting  
✅ Include navigation links  
✅ Sync regularly if using separate wiki repo  

## Customization

### Branding

Update these sections in `Home.md`:
- Course title and description
- Organization name
- Contact links
- Discord/community links

### Sidebar

Modify `_Sidebar.md` to:
- Add/remove sections
- Change groupings
- Adjust navigation structure

### Styling

GitHub wiki supports:
- Markdown formatting
- Emoji (use sparingly)
- Tables
- Code blocks
- Images (relative paths)

## Troubleshooting

### Wiki not showing up
- Ensure wiki feature is enabled in repository settings
- Check that Home.md exists (required as landing page)
- Verify file permissions

### Links not working
- Use relative links: `./Page-Name` not `Page-Name`
- File names are case-sensitive
- Spaces in filenames: use hyphens `-`

### Sidebar not appearing
- File must be named exactly `_Sidebar.md`
- Check file is in root of wiki repository
- Some GitHub UI locations don't show sidebar

### Images not loading
- Store images in repository, not wiki
- Use full URLs: `https://raw.githubusercontent.com/...`
- Or relative if using docs/ approach

## Testing

### Before Deployment

1. **Check all files exist**
   ```bash
   cd wiki/
   ls -la *.md | wc -l  # Should show 30
   ```

2. **Verify links**
   - Test all internal links
   - Check external URLs
   - Confirm lesson page links

3. **Preview locally**
   - Use VS Code markdown preview
   - Or GitHub preview in pull request

### After Deployment

1. Visit wiki home page
2. Click through navigation
3. Test sidebar links
4. Verify search works
5. Check on mobile

## Next Steps

Now that the wiki is created:

1. ✅ Review the wiki content
2. ✅ Choose deployment option
3. ✅ Deploy to GitHub wiki or Pages
4. ✅ Test navigation and links
5. ✅ Share with users!
6. ✅ Update main README to link to wiki

## Additional Features

### Search
GitHub wiki includes built-in search across all pages.

### History
Every wiki page tracks revision history.

### Collaboration
Multiple contributors can edit wiki pages directly on GitHub.

### Issues
Link to specific wiki pages from GitHub issues: `wiki/Page-Name`

---

**Questions?** Open an issue or check the [Wiki README](./wiki/README.md)
