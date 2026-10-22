# Notex

An open library of programming notes, code snippets, system design references,
Python notebooks, and handwritten computer science notes by [Harshit Yadav](https://harshityadav.in).

The landing page follows the current Fanout composition: rotating hero, floating
reading material, three marquee rows, eleven topic cards, preview rows, a learning
folder, eight navigation tiles, three free-access cards, study section, FAQ, and footer.
The full collection lives at `library/`, with sidebar readers for every note.
It uses the reference pale palette, compact navigation, grotesk and monospaced typography. Notex
retains its own content and branding; proprietary Fanout artwork is not bundled.

## Local development

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build.py
.venv/bin/python scripts/check.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory docs
```

Open [localhost:4173](http://localhost:4173). Rebuild after editing source files.

- `src/`: original Markdown, PDFs, images, and notebooks.
- `web/assets/`: CSS, browser JavaScript, self-hosted fonts and font licenses.
- `scripts/build.py`: renders every Markdown page, copies attachments, and builds the search index.
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
