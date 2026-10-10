# Huihui Li — Academic Homepage

Website: https://hhuili.github.io/

A static academic homepage using the Minimal Light template. No JavaScript, package installation, or build step is needed. GitHub Pages publishes `docs/` from the `main` branch; a push to that branch triggers publication.

## Editing

- `docs/index.html`: biography, research interests, publications, software, and contact links.
- `docs/styles.css`: local styling, including portrait framing.
- `docs/assets/huihui-li.jpg`: portrait.
- `docs/assets/Huihui-Li-CV.pdf`: downloadable CV.
- `docs/assets/css/`: original template styles.

## Local preview

From the repository directory, run:

```bash
python3 -m http.server 4173 --directory docs
```

Open http://localhost:4173 and refresh after editing. Commit and push changes to `main` to update the public website.

## CV source

`cv/Huihui-Li-CV.md` is an editable text reference. The PDF generator `cv/build_cv.py` currently contains its own text; editing the Markdown alone does not regenerate the PDF. To rebuild, update the generator, install its `reportlab` and `pypdf` dependencies in a Python environment, then run:

```bash
python3 cv/build_cv.py
```

Alternatively, replace `docs/assets/Huihui-Li-CV.pdf` with a prepared PDF.

## Provenance and licenses

The webpage and all assets were copied unchanged from the existing Sites publication. The Sites website remains available at https://hhuili.sweet-birch-1196.chatgpt.site/; GitHub commits do not automatically update that separate publication.

See `SOURCES.md` for content provenance. Minimal Light and font licenses are retained under `docs/assets/fonts/`. No additional license is granted here for personal photographs or CV content.
