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

## Go and DDIA reading collections

Go lives under `src/go/` in Languages; Designing Data-Intensive Applications lives
under `src/ddia/` in Systems. Both have landing cards, overview pages, chapter
navigation, section tables of contents, full-text search, highlighted code, tables,
and original SVG concept diagrams. The Go source includes chapters 2–6; DDIA includes
the preface and chapters 1–14. No other Go chapters exist in the source snapshot.

All 20 imported chapter Markdown files are byte-for-byte preserved from
[FAANG_BOOKS](https://github.com/harshityadav95/FAANG_BOOKS) at
`e17be94c728cd6ae755bf5d87a5a45b1a9f0dfbb`. Provenance, source byte counts, and SHA-256
hashes are recorded in `scripts/book-import.json` and verified with
`python scripts/check_books.py`. Original book figure files are absent upstream;
source captions/descriptions remain intact, and the clearly labeled Notex SVGs
provide additional conceptual overviews. Original text retains its respective rights.
