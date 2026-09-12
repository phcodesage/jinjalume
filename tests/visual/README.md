# Visual regression tests

The static landing page, component gallery, and the login, signup, and admin dashboard blocks are checked with Playwright at desktop (`1280x800`) and mobile (`390x844`) Chromium viewports. The gallery also has a dark-theme snapshot. Reference PNGs live beside each visual spec in its snapshot directory.

Install the Python development environment and browser once:

```bash
python -m pip install -e ".[dev]"
npm ci
npx playwright install chromium
```

Run the suite with:

```bash
npm run test:visual
```

When a deliberate visual change is made, review the result and update references explicitly:

```bash
npx playwright test --update-snapshots
```

CI installs Chromium and runs the same command. Failed reports and screenshots are uploaded as workflow artifacts; generated artifacts are not committed.
