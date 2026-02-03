# 🚀 Quick Start - 5 Minute Setup

Get your AI Code Review educational website live in 5 minutes!

## ⚡ Absolute Fastest Way (2 minutes)

### Using GitHub Pages:

```bash
# 1. Copy all files to a new GitHub repo
# 2. Go to Settings → Pages
# 3. Select "Deploy from a branch" → "main"
# 4. Your site is live at: https://YOUR_USERNAME.github.io/ai-code-review-learn
```

**That's it! Your site is live.**

---

## 💻 Local Testing (Before Publishing)

### On Mac/Linux:

```bash
# Navigate to the folder
cd path/to/ai-code-review-learn

# Start server
python3 app.py

# Open browser: http://localhost:8000
```

### On Windows:

```bash
# Navigate to the folder
cd path\to\ai-code-review-learn

# Start server
python app.py

# Open browser: http://localhost:8000
```

### Alternative (No Python needed):

```bash
# If you have Python 3
python3 -m http.server 8000

# If you have PHP
php -S localhost:8000

# If you have Node.js
npx http-server
```

---

## 📦 What You Get

```
ai-code-review-learn/
├── index.html           ← Main website (all content here)
├── styles.css          ← Styling
├── app.py              ← Local server (optional)
├── README.md           ← Documentation
├── LICENSE             ← MIT License (free to use)
└── DEPLOYMENT.md       ← Detailed deployment guide
```

---

## 🌍 Publishing Platforms (Choose One)

### Option 1: GitHub Pages (Free, Recommended)
1. Create GitHub account
2. New public repository
3. Upload all files
4. Settings → Pages → Deploy from branch (main)
5. **Done!** Site live at `https://username.github.io/ai-code-review-learn`

### Option 2: Netlify (Free, Super Easy)
1. Go to netlify.com
2. Drag & drop the folder
3. **Done!** Site live immediately

### Option 3: Vercel (Free, Very Fast)
1. Go to vercel.com
2. Connect GitHub repo
3. Click Deploy
4. **Done!**

### Option 4: Your Own Server
See DEPLOYMENT.md for VPS setup instructions

---

## ✅ Verification Checklist

After deploying, verify:

- [ ] Site opens without errors
- [ ] All text visible and readable
- [ ] Navigation links work
- [ ] Responsive on mobile
- [ ] Images (if any) load correctly
- [ ] CSS styling applied (not broken)

---

## 🎨 Customization (Optional)

### Change Colors
Edit `styles.css` line 8-14:
```css
:root {
    --primary-color: #2563eb;      /* Change these values */
    --secondary-color: #7c3aed;
```

### Add More Content
Edit `index.html` - it's all in one file, easy to modify

### Update Title/Meta
In `index.html` `<head>` section:
```html
<title>Your Custom Title</title>
<meta name="description" content="Your description">
```

---

## 📱 Test on Mobile

1. Deploy your site
2. Visit on phone/tablet
3. Check layout looks good
4. Test navigation

---

## 🔗 Share Your Site

Once live, share:
- **Twitter/X**: "Just published free educational guide on AI code review tools: [URL]"
- **LinkedIn**: Post with educational content
- **Reddit**: r/learnprogramming, r/webdev
- **Dev.to**: Write article with link
- **Product Hunt**: Submit for visibility

---

## 🆘 Problems?

### Site not loading?
- Check all files uploaded
- Verify `index.html` is in root
- Wait 1-2 minutes for GitHub Pages to update
- Clear browser cache (Ctrl+Shift+Delete)

### CSS looks broken?
- Make sure `styles.css` is uploaded
- Check in same folder as `index.html`
- Hard refresh: Ctrl+Shift+R (Cmd+Shift+R on Mac)

### Local server won't start?
- Make sure you have Python 3 installed
- Check you're in the correct directory
- Try: `python3 -m http.server 8000`

### Still stuck?
- Read DEPLOYMENT.md (detailed guide)
- Check platform documentation
- Google "[platform] + your issue"

---

## 📚 File Descriptions

| File | Purpose |
|------|---------|
| `index.html` | Entire website in one file - Edit for content |
| `styles.css` | All styling - Edit for colors/fonts |
| `app.py` | Optional local server - Run with `python3 app.py` |
| `README.md` | Full documentation |
| `DEPLOYMENT.md` | Detailed deployment guide |
| `LICENSE` | MIT License - Free to use/modify |
| `QUICKSTART.md` | This file |

---

## 🎯 Next Steps

1. **Test Locally**: Run `python3 app.py` and visit `http://localhost:8000`
2. **Deploy**: Choose GitHub Pages or Netlify (easiest)
3. **Customize**: Update colors, text, content if desired
4. **Share**: Post link to social media
5. **Enjoy**: You've published a free educational resource!

---

## ⏱️ Timeline

- **5 min**: Upload files to GitHub
- **1 min**: Enable GitHub Pages
- **1-2 min**: GitHub Pages generates your URL
- **TOTAL: ~10 minutes to live deployment**

---

**You're all set! Deploy now and share with the world.** 🌍

Questions? Check DEPLOYMENT.md for detailed instructions for each platform.
