# Jinjalume

Server-rendered Tailwind UI components for Flask, Jinja, and Python web apps.

Jinjalume is an open-source, HTML-first component kit for developers who want reusable UI in Jinja templates without adopting a frontend SPA framework.

> Early MVP: the API and visual language will evolve. Feedback and contributions are welcome.

## What is included

- A small Flask extension that makes Jinjalume templates available to your app
- Reusable Jinja macros for buttons, badges, alerts, cards, inputs, textareas, avatars, spinners, and dialogs
- Tailwind CSS v4 build setup
- A working Flask demo
- Contributor documentation, issue templates, and continuous integration

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"

npm install
npm run build:css
flask --app demo.app run --debug
```

Open <http://127.0.0.1:5000>.

Browse the component gallery at <https://phcodesage.github.io/jinjalume/>.

## Use in a Flask app

```python
from flask import Flask

from jinjalume import Jinjalume

app = Flask(__name__)
Jinjalume(app)
```

Then import a component in a Jinja template:

```jinja
{% from "jinjalume/components/button.html" import button %}

{{ button("Save changes", variant="primary", type="submit") }}
```

The extension only registers Jinjalume's templates. Your application remains responsible for building and serving its Tailwind CSS file.

## Available components

Import the macros you need from `jinjalume/components/`:

- `button.html` — primary, secondary, and danger actions
- `badge.html` — compact status labels
- `alert.html` — informational, success, warning, and danger messages
- `card.html` — content containers with a caller block
- `input.html` and `textarea.html` — labeled fields with help and error states
- `avatar.html` — image or initials avatar
- `spinner.html` — accessible loading indicator
- `modal.html` — native HTML dialog markup for progressive enhancement

All components are plain Jinja macros. They do not require a JavaScript framework, and interactive behavior can be progressively enhanced with native browser APIs, HTMX, or Alpine.js.

## Development

```bash
make install
make test
make lint
make css
```

Run the CSS watcher and Flask in separate terminals while developing:

```bash
npm run dev:css
flask --app demo.app run --debug
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Roadmap

- WTForms helpers and validation states
- More accessible interactive components using progressive enhancement
- Optional HTMX and Alpine.js integrations
- Theme tokens, dark mode, and RTL examples
- Component documentation site and visual regression tests

## License

Jinjalume is available under the [MIT License](LICENSE).
