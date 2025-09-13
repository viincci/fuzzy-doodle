# Heritage Road Map Foundation - Plant Blog

🌿 A Next.js blog platform dedicated to South African botanical heritage, research, and conservation.

## About HRMF

The Heritage Road Map Foundation (HRMF) is committed to preserving and documenting South Africa's extraordinary plant diversity through research, education, and community engagement. This blog serves as our digital platform for sharing botanical discoveries, conservation efforts, and educational content about South African flora.

## Features

- **Modern Blog Platform**: Built with Next.js 12 and Tailwind CSS
- **FastAPI Integration**: Ready for backend integration with FastAPI
- **Responsive Design**: Mobile-first design optimized for all devices
- **SEO Optimized**: Built-in SEO optimization with meta tags and structured data
- **Search & Filtering**: Advanced search and filtering capabilities for articles
- **Species Database**: Integration-ready for comprehensive plant species data
- **Conservation Projects**: Showcase ongoing conservation initiatives
- **Multi-author Support**: Support for multiple researchers and contributors
- **Image Optimization**: Optimized image handling and responsive images
- **Newsletter Integration**: Built-in newsletter subscription functionality
- **Comments System**: Integrated commenting system with Giscus
- **Analytics Ready**: Integration with Google Analytics and other providers

## Tech Stack

- **Frontend**: Next.js 12, React 17, Tailwind CSS
- **Backend**: FastAPI (integration ready)
- **Database**: PostgreSQL (recommended for FastAPI backend)
- **Styling**: Tailwind CSS with custom plant-themed design
- **Image Handling**: Next.js Image Optimization
- **Comments**: Giscus (GitHub-based commenting)
- **Newsletter**: EmailOctopus integration
- **Deployment**: Vercel (recommended)

## Quick Start

### Prerequisites

- Node.js 16.x or later
- npm or yarn
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hrmf-plant-blog.git
   cd hrmf-plant-blog
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env.local
   ```
   Edit `.env.local` with your configuration values.

4. **Start development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

5. **Open in browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## Project Structure

```
📦 hrmf-plant-blog/
├── 🗂️ components/          # React components
│   ├── 🗂️ blog/           # Blog-specific components
│   ├── 🗂️ species/        # Species database components
│   ├── 🗂️ ui/             # Reusable UI components
│   └── 🗂️ layout/         # Layout components
├── 🗂️ data/               # Static data and content
│   ├── 🗂️ authors/        # Author profiles
│   ├── 🗂️ blog/           # Blog posts (MDX format)
│   └── 🗂️ species/        # Species data files
├── 🗂️ lib/                # Utility libraries
│   ├── 📄 api.js           # API integration utilities
│   ├── 📄 mdx.js           # MDX processing
│   └── 📄 utils.js         # General utilities
├── 🗂️ pages/              # Next.js pages
│   ├── 🗂️ api/            # API routes
│   ├── 🗂️ blog/           # Blog pages
│   ├── 🗂️ species/        # Species pages
│   └── 🗂️ projects/       # Project pages
├── 🗂️ public/             # Static assets
│   └── 🗂️ static/         # Images and media
├── 🗂️ styles/             # CSS and styling
└── 🗂️ layouts/            # Page layout templates
```

## Configuration

### Site Metadata

Edit `data/siteMetadata.js` to customize:
- Site title and description
- Author information
- Social media links
- Analytics configuration
- Newsletter settings

### Navigation

Modify `data/headerNavLinks.js` to customize navigation:
- Menu items
- External links
- Category pages

### Content Types

The platform supports several content types:

1. **Blog Articles** (`/blog`)
   - Research papers
   - Conservation stories
   - Field reports
   - Educational content

2. **Species Database** (`/species`)
   - Taxonomic information
   - Conservation status
   - Distribution maps
   - Images and descriptions

3. **Conservation Projects** (`/projects`)
   - Active projects
   - Project outcomes
   - Funding information
   - Team members

4. **Regional Guides** (`/regions`)
   - Biome descriptions
   - Endemic species
   - Conservation priorities

## Content Management

### Adding Blog Posts

1. Create a new MDX file in `data/blog/`
2. Use the following frontmatter structure:

```yaml
---
title: 'Your Article Title'
date: '2025-01-15'
tags: ['conservation', 'fynbos', 'endemic-species']
draft: false
summary: 'Brief article summary for listings'
authors: ['default']
images: ['/static/images/article-image.jpg']
---

Your article content here...
```

### Adding Species Data

Species data can be added as:
1. MDX files in `data/species/`
2. JSON data for API integration
3. Database entries (when FastAPI backend is implemented)

## API Integration

The platform is designed to work with a FastAPI backend. Key integration points:

### Blog API Endpoints
- `GET /api/v1/articles` - List articles with pagination
- `GET /api/v1/articles/{slug}` - Get single article
- `GET /api/v1/categories` - List categories
- `GET /api/v1/tags` - List tags

### Species API Endpoints
- `GET /api/v1/species` - List species with filtering
- `GET /api/v1/species/{id}` - Get single species
- `GET /api/v1/families` - List plant families

### Project API Endpoints
- `GET /api/v1/projects` - List conservation projects
- `GET /api/v1/projects/{id}` - Get single project

See `lib/api.js` for complete API integration utilities.

## Customization

### Styling

The site uses Tailwind CSS with a custom configuration optimized for botanical content:

- **Colors**: Green-focused palette reflecting South African flora
- **Typography**: Clear, readable fonts for scientific content
- **Components**: Custom components for species cards, project displays
- **Responsive**: Mobile-first design with desktop enhancements

### Adding New Content Types

1. Create new page templates in `layouts/`
2. Add corresponding pages in `pages/`
3. Update navigation in `data/headerNavLinks.js`
4. Add API integration in `lib/api.js`

## SEO and Performance

- **Next.js Image Optimization**: Automatic image optimization
- **Meta Tags**: Dynamic meta tags for articles and pages
- **Structured Data**: JSON-LD for botanical content
- **Sitemap**: Automatic sitemap generation
- **Performance**: Optimized for Core Web Vitals

## Deployment

### Vercel (Recommended)

1. Connect your GitHub repository to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy automatically on push to main branch

### Other Platforms

The site can be deployed to:
- Netlify
- GitHub Pages
- AWS Amplify
- Custom servers

## FastAPI Backend Setup

When ready to implement the FastAPI backend:

1. **Create FastAPI project structure**
2. **Set up PostgreSQL database**
3. **Implement API endpoints** (see `lib/api.js` for expected structure)
4. **Configure CORS** for frontend domain
5. **Update environment variables**

## Contributing

We welcome contributions from the botanical community:

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

### Content Contributions

- Research articles
- Species descriptions
- Conservation project updates
- Regional guides
- Image contributions

### Code Contributions

- Bug fixes
- Feature enhancements
- Performance improvements
- Documentation updates

## Community

- **Website**: [https://hrmf.org.za](https://hrmf.org.za)
- **Email**: info@hrmf.org.za
- **Twitter**: [@hrmf_sa](https://twitter.com/hrmf_sa)
- **GitHub**: [github.com/hrmf](https://github.com/hrmf)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Based on the excellent [Tailwind Nextjs Starter Blog](https://github.com/timlrx/tailwind-nextjs-starter-blog)
- South African National Biodiversity Institute (SANBI)
- Botanical Society of South Africa
- All contributing researchers and botanists

## Roadmap

- [ ] FastAPI backend implementation
- [ ] Advanced search with Algolia
- [ ] Interactive species maps
- [ ] Mobile app companion
- [ ] Citizen science integration
- [ ] Multi-language support (Afrikaans, Zulu, Xhosa)
- [ ] Advanced image recognition for species identification
- [ ] Integration with iNaturalist and other platforms

---

*Preserving South Africa's botanical heritage for future generations* 🌿
