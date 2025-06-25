# Personal Website - Dra. Alejandra Tabares Pozos

![Website Preview](https://img.shields.io/badge/Status-Live-brightgreen)
![Jekyll Version](https://img.shields.io/badge/Jekyll-4.0+-blue)
![Bootstrap Version](https://img.shields.io/badge/Bootstrap-5.3.0-blue)

Personal academic website of Dra. Alejandra Tabares Pozos, Assistant Professor at Universidad de los Andes. This website showcases research, publications, teaching experience, and professional achievements in the field of AI-driven energy systems and optimization.

**🌐 Live Site:** [https://pozost.github.io/MyWebSite](https://pozost.github.io/MyWebSite)

## 🌟 Features

- **Modern Design**: Professional and responsive design using Bootstrap 5
- **Academic Focus**: Optimized for academic content and research presentation
- **SEO Optimized**: Built-in search engine optimization
- **Fast Loading**: Optimized for performance and user experience
- **Mobile Responsive**: Perfect viewing on all devices
- **GitHub Pages Ready**: Configured for easy deployment

## 🚀 Quick Start

### Prerequisites

- Ruby 3.2 or higher
- Jekyll 4.0+
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/PozosT/MyWebSite.git
   cd MyWebSite
   ```

2. **Install dependencies**
   ```bash
   bundle install
   ```

3. **Run locally**
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site**
   Open your browser and go to `http://localhost:4000/MyWebSite`

## 📦 Deployment to GitHub Pages

### Automatic Deployment (Already Configured)

The site is automatically deployed to GitHub Pages when you push to the main branch. The workflow is configured in `.github/workflows/jekyll.yml`.

1. **Push changes to GitHub**
   ```bash
   git add .
   git commit -m "Update website"
   git push origin main
   ```

2. **Check deployment**
   - Go to the [Actions tab](https://github.com/PozosT/MyWebSite/actions) to monitor deployment
   - Your site will be available at [https://pozost.github.io/MyWebSite](https://pozost.github.io/MyWebSite)

### Manual Deployment

1. **Build the site**
   ```bash
   bundle exec jekyll build
   ```

2. **Deploy to GitHub Pages**
   ```bash
   bundle exec jekyll build --baseurl "/MyWebSite"
   ```

## ⚙️ Configuration

### Update Personal Information

Edit `_config.yml` to customize your information:

```yaml
title: Dra. Alejandra Tabares Pozos
email: a.tabaresp@uniandes.edu.co
url: "https://pozost.github.io"
baseurl: "/MyWebSite"
```

### Update Navigation

Modify the navigation menu in `_config.yml`:

```yaml
nav_pages:
  - name: about
  - name: publications
  - name: research
  - name: education
  - name: talks
  - name: volunteering
```

### Add Publications

1. Create new files in `_publications/` directory
2. Use the existing publication format as template
3. Update `_data/publist.yml` to include new publications

### Add Team Members

1. Add photos to `images/team/`
2. Update `_data/team_members.yml`

## 📁 Project Structure

```
├── _config.yml              # Site configuration
├── _data/                   # Data files (publications, team, etc.)
├── _includes/               # Reusable HTML components
├── _layouts/                # Page layouts
├── _pages/                  # Main pages
├── _publications/           # Publication files
├── _sass/                   # SCSS stylesheets
├── css/                     # Compiled CSS
├── images/                  # Images and logos
├── js/                      # JavaScript files
├── .github/workflows/       # GitHub Actions workflows
└── Gemfile                  # Ruby dependencies
```

## 🎨 Customization

### Colors

The color scheme can be customized in `css/main.scss`:

```scss
$primary-color: #2c3e50;
$secondary-color: #3498db;
$accent-color: #e74c3c;
```

### Fonts

The site uses Google Fonts (Inter and Source Sans Pro). To change fonts, update the font imports in `_includes/head.html`.

### Layouts

Customize page layouts by modifying files in the `_layouts/` directory.

## 🔧 Troubleshooting

### Common Issues

1. **Build Errors**
   - Ensure Ruby version is 3.2+
   - Run `bundle update` to update dependencies
   - Check for syntax errors in YAML files

2. **Images Not Loading**
   - Verify image paths are correct
   - Ensure images are in the `images/` directory
   - Check file permissions

3. **GitHub Pages Not Updating**
   - Wait a few minutes for deployment
   - Check GitHub Actions for build errors
   - Verify the repository is public

### Performance Optimization

- Optimize images before uploading
- Minimize external dependencies
- Use CDN links for external resources

## 📝 Content Management

### Adding New Pages

1. Create a new `.md` file in `_pages/`
2. Add front matter with layout and metadata
3. Update navigation if needed

### Adding Publications

1. Create a new file in `_publications/`
2. Use the existing format as template
3. Update `_data/publist.yml`

### Adding News

1. Edit `_data/news.yml`
2. Add new entries with date, title, and content

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Jekyll](https://jekyllrb.com/)
- Styled with [Bootstrap 5](https://getbootstrap.com/)
- Icons from [Font Awesome](https://fontawesome.com/)
- Academic icons from [Academicons](https://jpswalsh.github.io/academicons/)

## 📞 Contact

For questions or support, please contact:
- Email: a.tabaresp@uniandes.edu.co
- Website: [https://pozost.github.io/MyWebSite](https://pozost.github.io/MyWebSite)
- GitHub: [https://github.com/PozosT/MyWebSite](https://github.com/PozosT/MyWebSite)

---

**Repository:** [https://github.com/PozosT/MyWebSite](https://github.com/PozosT/MyWebSite)  
**Live Site:** [https://pozost.github.io/MyWebSite](https://pozost.github.io/MyWebSite)
