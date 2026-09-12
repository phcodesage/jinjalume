# Contributing to Jinjalume

Everyone is welcome to contribute. You do not need prior approval to open an issue, improve documentation, fix a bug, or propose a component. Please read the [Code of Conduct](CODE_OF_CONDUCT.md) first.

## Local setup

```bash
git clone https://github.com/phcodesage/jinjalume.git
cd jinjalume
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
npm install
```

Run checks before submitting a pull request:

```bash
make test
make lint
npm run build:css
```

### Visual regression checks

The component gallery has Playwright snapshots for desktop, mobile, and the dark theme. Install Chromium once with `npx playwright install chromium`, then run `npm run test:visual`. When a UI change is intentional, inspect the screenshots locally and update them explicitly with `npx playwright test --update-snapshots`. Do not update snapshots to hide an unintended layout change. CI uploads failed reports and screenshots for review without committing generated artifacts.

## Adding a component

1. Add the component under `jinjalume/templates/jinjalume/components/`.
2. Prefer a small Jinja macro with explicit, documented arguments.
3. Use complete Tailwind class names so Tailwind can detect them at build time.
4. Include keyboard and screen-reader behavior in the initial markup.
5. Add or update a demo in `demo/templates/index.html`.
6. Add or update a rendering test in `tests/`.
7. Update the README or component documentation when the public API changes.

## Pull requests

- Keep pull requests focused and explain the user-facing change.
- Add tests for bug fixes and new behavior.
- Include screenshots or a short recording for visual changes when useful.
- Do not add generated files, secrets, or unrelated formatting changes.
- Be open to review suggestions; maintainers will explain requested changes.

If you are unsure where to start, look for issues labeled `good first issue` or open an issue describing the idea.
