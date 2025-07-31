# Engineering Portfolio Website

![Portfolio Screenshot](./screenshot.png)

A modern, responsive portfolio website for engineers featuring dark mode, project showcase, and contact functionality.

## Features

- **Dark/Light Mode Toggle** - User preference persists across sessions
- **Responsive Design** - Works on all device sizes
- **Project Showcase** - Filterable project gallery
- **Contact Form** - Direct email integration
- **Resume Download** - Google Drive integration
- **Interactive UI** - Smooth animations and transitions

## Technologies Used

- HTML5
- CSS3 (with CSS Variables)
- JavaScript (ES6)
- Bootstrap 5
- Font Awesome 6

## File Structure
portfolio/
├── index.html # Main website file
├── README.md # This documentation
├── images/ # All image assets
│ ├── heroimg.jpg # Profile picture (800x800px)
│ ├── aboutimg.jpg # About section image
│ └── projects/ # Project screenshots
├── css/
│ └── styles.css # Custom styles
└── js/
└── main.js # Custom JavaScript

text

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/engineering-portfolio.git
   cd engineering-portfolio
Add your images:

Place your profile photo at images/heroimg.jpg (800×800 recommended)

Add about section image at images/aboutimg.jpg

Customize content:

Open index.html and edit:

Your name (line 420)

Contact email (line 650)

Resume link (line 800)

Project details (lines 500-600)

Test locally:

Open index.html in your browser

Deployment
Option 1: GitHub Pages
Create a new repository

Push your files

Go to Settings → Pages → Select main branch

Option 2: Netlify
Drag and drop your folder to Netlify Drop

Follow the deployment prompts

Customization Guide
Change Colors
Edit the CSS variables at the top of styles.css:

css
:root {
  --primary: #2563eb;       /* Main brand color */
  --secondary: #0f172a;     /* Dark accent */
  --accent: #10b981;        /* Highlight color */
}
Add Projects
Add new project cards in the projects section:

html
<div class="col-md-6 col-lg-4">
  <div class="project-card">
    <img src="images/projects/project1.jpg" class="project-img">
    <div class="project-content">
      <h3>Project Title</h3>
      <p class="project-tech">React, Node.js</p>
      <p>Project description...</p>
      <div class="project-links">
        <a href="#"><i class="fab fa-github"></i> Code</a>
        <a href="#"><i class="fas fa-external-link-alt"></i> Live Demo</a>
      </div>
    </div>
  </div>
</div>
Troubleshooting
Image not loading?

Verify correct file path in src attribute

Check filename capitalization matches exactly

Ensure image is in the right directory

Dark mode not working?

Check browser console for JavaScript errors

Verify localStorage is enabled

Contact form issues?

Test with a real email client installed

Check spam folder if emails aren't arriving

License
MIT License - Free for personal and commercial use

