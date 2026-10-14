# Huihui Li — Academic Homepage

- Home: https://hhuili.github.io/
- Publications: https://hhuili.github.io/publications/

Two static pages adapted from [Yaoyao Liu's public personal website template](https://github.com/yaoyao-liu/personal-website). The site uses a black navigation bar and the Source Sans 3 / Montserrat font combination from the reference lab website. The original template license and self-hosted font licenses are retained. GitHub Pages publishes `docs/` from `main`.

## Edit and publish

The editable sources are:

| Source | What it changes |
| --- | --- |
| `content/home.html` | Introduction, research interests, software and contact |
| `content/news.json` | News, newest first; entries beyond four get a Show more button |
| `content/publications.json` | Publications, figures and resource links |
| `templates/hero.html` | Portrait, name, affiliation and profile links shared by both pages |
| `templates/header.html` | Shared top navigation |
| `templates/base.html` | Page head, shared structure and footer |
| `docs/styles.css` | Personal style overrides |
| `docs/assets/huihui-li.jpg` | Original portrait |
| `docs/assets/Huihui-Li-CV.pdf` | Downloadable CV |

After editing content or templates, regenerate the pages with standard Python:

```bash
python3 scripts/build_site.py
```

The generated files are `docs/index.html` and `docs/publications/index.html`. You can edit those files directly, but a later regeneration will replace direct edits. Commit and push both source changes and generated pages to `main`; GitHub Pages will publish them automatically. No package installation or Jekyll build is required.

## Local preview

```bash
python3 -m http.server 4173 --directory docs
```

Open http://localhost:4173 and refresh after editing.

## Extending the website

The header, personal profile and page shell are shared templates. To add a future Group, Research, or Contact page, add its content, render it with `build_page` in `scripts/build_site.py`, and add its link in `templates/header.html`. The current navigation contains only Home and Publications.

## CV source

`cv/Huihui-Li-CV.md` is an editable text reference. The PDF generator `cv/build_cv.py` currently contains its own text; editing the Markdown alone does not regenerate the PDF. To rebuild, update the generator, install `reportlab` and `pypdf` in a Python environment, then run:

```bash
python3 cv/build_cv.py
```

Alternatively, replace `docs/assets/Huihui-Li-CV.pdf` with a prepared PDF.

## Provenance and licenses

See `SOURCES.md`, `TEMPLATE-LICENSE`, and `docs/assets/fonts/`. No additional license is granted here for personal photographs or CV content.

The earlier Sites website remains at https://hhuili.sweet-birch-1196.chatgpt.site/. It is a separate publication and is not updated by GitHub commits.
