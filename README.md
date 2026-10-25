# Notex

An open library of programming notes, code snippets, system design references,
Python notebooks, and handwritten computer science notes by [Harshit Yadav](https://harshityadav.in).

The landing page follows the current Fanout composition: rotating hero, floating
reading material, three marquee rows, thirteen topic cards, preview rows, a learning
folder, eight navigation tiles, three free-access cards, study section, FAQ, and footer.
The full collection lives at `library/`, with sidebar readers for every note.
The Cloud & infrastructure section at `#cloud` adds Cloudflare, Azure, and Kubernetes
path previews with original generated notebook artwork and links to official guides.
It uses the reference pale palette, compact navigation, grotesk and monospaced typography. Notex
retains its own content and branding; proprietary Fanout artwork is not bundled.

## Local development

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python scripts/check.py
.venv/bin/python scripts/check_books.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory docs
```

Open [localhost:4173](http://localhost:4173). Rebuild after editing source files.

- `src/`: original Markdown, PDFs, images, and notebooks.
- `web/assets/`: CSS, browser JavaScript, self-hosted fonts and font licenses.
- `scripts/build.py`: renders every Markdown page, copies attachments, and builds the search index.
- `scripts/cloud.py`: cloud-path cards and accessible topic-preview dialogs.
- `docs/`: generated, deployable static site. All URLs support the `/Notex/` project prefix.

## GitHub Pages

In repository **Settings → Pages → Source**, choose **GitHub Actions**. Pushes to
`master` or `main` build, check, and deploy the site with the included workflow.
No personal token, backend, analytics, external font CDN, or paid service is required.
The generated `docs/` directory also supports the classic branch `/docs` Pages setup.

Search runs locally in the browser. Saved notes use localStorage on the current
device. Handwritten PDFs are served locally; notebooks open in GitHub's renderer.

## License

Website code: [MIT](LICENSE). Bundled fonts: Overused Grotesk (SIL OFL 1.1) and
Departure Mono (MIT). Original references and attachments retain their respective
licenses. External links and embedded remote images in legacy notes may need an
internet connection. No claim is made over third-party material.

## Go and DDIA learning paths

The Go and DDIA overviews follow the Fanout course composition: compact navigation,
a course syllabus, module directory, numbered lesson rows, reading/practice filters,
and list/grid layouts. Go has 5 modules and 119 lessons; DDIA has 15 modules and
202 lessons. Long chapters split at natural headings; publishing notices and scraped
navigation are omitted from guided lessons. Original code, exercises, and technical
explanations remain intact. Each lesson links to the complete chapter and references.
Progress, saved notes, and the last visited lesson stay in browser localStorage.

`scripts/curriculum.py` derives modules and lessons from the imported chapters;
`scripts/books.py` renders course navigation and overview pages. Generated routes
under `docs/go/lessons`, `docs/go/modules`, `docs/ddia/lessons`, and `docs/ddia/modules`
are rebuilt on each build. Edit source chapters rather than generated lesson HTML.
The two new notebook covers are original generated PNGs with transparent backgrounds;
art direction and prompts are documented in `web/assets/books/README.md`.

All 20 imported chapter Markdown files are byte-for-byte preserved from
[FAANG_BOOKS](https://github.com/harshityadav95/FAANG_BOOKS) at
`e17be94c728cd6ae755bf5d87a5a45b1a9f0dfbb`. Provenance, source byte counts, and SHA-256
hashes are recorded in `scripts/book-import.json`. `python scripts/check_books.py`
verifies original files and confirms every code block survives lesson extraction and
HTML rendering. Go source contains chapters 2–6 only; DDIA includes the preface and
chapters 1–14. Original book figure files are absent upstream; captions and descriptions
remain in the notes. Original text retains its respective rights.
