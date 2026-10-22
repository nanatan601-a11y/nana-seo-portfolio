# Nana Tan Remote SEO Portfolio

This is a static bilingual portfolio website for GitHub Pages. English pages live at the site root and Chinese pages live under `/zh/`, with self-referencing canonicals and reciprocal `hreflang` links.

This optimized version is written for SEO Strategist, Organic Growth, Technical SEO, E-commerce SEO, International SEO, and SEO/GEO roles. It emphasizes business impact, technical SEO with developer collaboration, AI search visibility, English communication, and cross-functional execution.

## Pages

- `index.html` — homepage
- `cases.html` — case overview
- `case-maggie.html` — Maggie Sun Real Estate case
- `case-wjs.html` — WJS Home case
- `case-mokafx.html` — Moka SFX case overview
- `case-moka-sfx-ads.html` — Moka SFX paid media efficiency deep dive
- `case-wjs-recovery.html` — WJS Home organic recovery deep dive
- `case-maggie-local-growth.html` — Maggie Sun Real Estate local growth deep dive
- `resume-copy-bilingual.md` — ready-to-use Chinese and English resume copy
- `case-sunsara.html` — Sunsara Beauty case
- `skills.html` — capabilities summary
- `zh/` — generated Chinese versions of every public page
- `assets/resume/` — downloadable English and Chinese resume PDFs
- `source/pages/` — bilingual source templates used to generate the public pages
- `sitemap.xml` and `robots.txt` — search discovery files

## Update bilingual pages

Edit the matching `source/pages/*.html.template` file, then regenerate and validate the public pages:

```text
python3 build_localized_site.py
python3 validate_site.py
```

Do not edit the generated root or `/zh/` HTML files directly; the next build will overwrite them.

## Publish with GitHub Pages

1. Create a GitHub repository, for example `nanatan-seo-portfolio`.
2. Upload all files in this folder to the repository root.
3. Go to **Settings → Pages**.
4. Select **Deploy from a branch**.
5. Choose `main` and `/root`.
6. Save and wait for GitHub to generate the live URL.

If you want a GitHub username website, create a repository named:

```text
your-github-username.github.io
```

Then upload these files to that repository root.
