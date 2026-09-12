# Visual regression tests

The gallery is checked with Playwright at desktop (`1280x800`) and mobile (`390x844`) Chromium viewports, plus a desktop dark-theme snapshot. Reference PNGs live beside `gallery.spec.js` in its snapshot directory.

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
