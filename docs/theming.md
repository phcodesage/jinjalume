# Jinjalume theming proposal

## Decision

Jinjalume uses semantic CSS custom properties for component colors and opts into dark mode with a root `data-theme` attribute:

```html
<html data-theme="light">
```

Set `data-theme="dark"` on the document root to opt in. Light mode remains the default. This avoids forcing an application to follow the user's system preference and works with server-rendered HTML before any JavaScript runs.

The reference token definitions live in `static/src/input.css`:

```css
:root {
  --jl-surface: #ffffff;
  --jl-text: #0f172a;
  --jl-border: #e2e8f0;
}

[data-theme="dark"] {
  --jl-surface: #1e293b;
  --jl-text: #f8fafc;
  --jl-border: #475569;
}
```

Components consume these semantic tokens through Tailwind arbitrary-value utilities such as `bg-[var(--jl-surface)]` and `text-[var(--jl-text)]`. The token names are stable; their values are application-owned.

## Why this shape

- It preserves the current light appearance while allowing a complete theme swap at one root element.
- It keeps component templates independent of a JavaScript framework.
- It lets applications choose server-side, user-preference, or client-side theme selection without changing macros.
- It avoids publishing a second CSS framework or requiring consumers to adopt a global class naming convention.
- Semantic tokens make future brand themes, high-contrast themes, and RTL examples additive rather than a rewrite of every component.

## Application integration

The Python package intentionally does not ship compiled CSS. An application using Tailwind should scan its installed Jinjalume templates and copy the token layer into its CSS entry point. The demo already does this through `static/src/input.css`.

The demo's theme toggle is a few lines of vanilla JavaScript and stores the choice in `localStorage`. Applications may replace it with a server-side preference, a cookie, or their own control. No toggle is required for the theme contract: setting `data-theme="dark"` is enough.

## Initial token groups

The first implementation covers page/surface/text/border, primary and danger actions, focus color, info/success/warning/danger feedback, neutral badges, and the avatar/spinner accent. All four required component groups—buttons, alerts, cards, and form fields—consume these tokens.
