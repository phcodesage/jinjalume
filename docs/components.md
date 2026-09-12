# Jinjalume component reference

The demo gallery at `/` renders every component in this reference. Start it with:

```bash
make css
flask --app demo.app run --debug
```

Every example assumes `Jinjalume(app)` has been initialized and imports the macro from its package template.

## Button

```jinja
{% from "jinjalume/components/button.html" import button %}

{{ button("Save changes", variant="primary", type="submit") }}
{{ button("Cancel", variant="secondary", href="/cancel") }}
{{ button("Delete", variant="danger", size="sm") }}
```

Signature: `button(label, variant="primary", size="md", type="button", href=None, class_name="", disabled=False)`

`variant` supports `primary`, `secondary`, and `danger`. `size` supports `sm`, `md`, and `lg`. With `href`, the macro emits an anchor; otherwise it emits a button. `disabled` is native for buttons and expressed with `aria-disabled` plus `tabindex=-1` for links.

Rendered shape:

```html
<button type="submit" class="...">Save changes</button>
```

## Badge

```jinja
{% from "jinjalume/components/badge.html" import badge %}

{{ badge("Draft") }}
{{ badge("Published", variant="success") }}
{{ badge("Needs review", variant="warning") }}
{{ badge("Failed", variant="danger") }}
```

Signature: `badge(label, variant="neutral", class_name="")`

`variant` supports `neutral`, `success`, `warning`, and `danger`.

Rendered shape:

```html
<span class="...">Published</span>
```

## Alert

```jinja
{% from "jinjalume/components/alert.html" import alert %}

{{ alert("Your profile was saved.", variant="success", title="Success") }}
{{ alert("Check the highlighted fields.", variant="warning") }}
```

Signature: `alert(message, variant="info", title=None, class_name="")`

`variant` supports `info`, `success`, `warning`, and `danger`. Alerts use `role="alert"` and accept plain text or already-rendered Jinja content according to the consuming application's autoescape policy.

Rendered shape:

```html
<div role="alert" class="...">
  <p class="font-semibold">Success</p>
  <p class="mt-1">Your profile was saved.</p>
</div>
```

## Card

Cards use a caller block for body content:

```jinja
{% from "jinjalume/components/card.html" import card %}

{% call card("Account", "Update your contact details.") %}
  <p>Your account is active.</p>
{% endcall %}
```

Signature: `card(title=None, description=None, class_name="")`

`title` and `description` are optional. The caller block is required and is rendered inside the card body.

Rendered shape:

```html
<section class="...">
  <h2>Account</h2>
  <p>Update your contact details.</p>
  <div>...</div>
</section>
```

## Input field

```jinja
{% from "jinjalume/components/input.html" import input_field %}

{{ input_field(
    "email",
    label="Email address",
    type="email",
    value="person@example.com",
    placeholder="you@example.com",
    help_text="We will never share your email.",
    required=True
) }}
```

Signature: `input_field(name, label=None, value="", type="text", placeholder="", help_text=None, error=None, required=False, class_name="", autocomplete=None)`

`type` is passed to the native input. When `error` is present, the control gets `aria-invalid="true"` and a linked error message. Help and error messages get deterministic IDs and are combined in `aria-describedby`.

Rendered shape:

```html
<label for="email">Email address</label>
<input id="email" name="email" type="email" aria-describedby="email-help">
<p id="email-help">We will never share your email.</p>
```

## Select field

```jinja
{% from "jinjalume/components/select.html" import select_field %}

{{ select_field(
    "status",
    label="Status",
    options=[
        {"value": "draft", "label": "Draft"},
        {"value": "published", "label": "Published"},
        {"value": "archived", "label": "Archived", "disabled": True}
    ],
    value="published",
    help_text="Choose the publication state.",
    required=True
) }}
```

Signature: `select_field(name, label=None, options=[], value="", help_text=None, error=None, required=False, class_name="")`

Each option may be a mapping with `value`, `label`, and optional `disabled` keys, or a two-item `(value, label)` pair. The option whose value matches `value` is selected. The macro emits a native `<select>` and uses the same label, help, error, required, and `aria-describedby` conventions as the other form fields.

Rendered shape:

```html
<select id="status" name="status" required aria-describedby="status-help">
  <option value="published" selected>Published</option>
</select>
```

## Textarea field

```jinja
{% from "jinjalume/components/textarea.html" import textarea_field %}

{{ textarea_field(
    "message",
    label="Message",
    value="Existing text",
    rows=5,
    placeholder="Write a message…",
    error="A message is required."
) }}
```

Signature: `textarea_field(name, label=None, value="", rows=4, placeholder="", help_text=None, error=None, required=False, class_name="")`

`rows` controls the native textarea height. Error and help messages use the same accessible relationship contract as `input_field` and `select_field`.

Rendered shape:

```html
<label for="message">Message</label>
<textarea id="message" name="message" rows="5" aria-invalid="true" aria-describedby="message-error">Existing text</textarea>
<p id="message-error">A message is required.</p>
```

## Avatar

```jinja
{% from "jinjalume/components/avatar.html" import avatar %}

{{ avatar("Jinjalume") }}
{{ avatar("Taylor Example", src="/static/taylor.jpg", size="lg") }}
```

Signature: `avatar(name, src=None, size="md", class_name="")`

`size` supports `sm`, `md`, and `lg`. Without `src`, the macro renders the first character of `name` with an accessible label. With `src`, it renders an image whose `alt` text is `name`.

Rendered shape without an image:

```html
<span role="img" aria-label="Jinjalume" class="...">J</span>
```

## Spinner

```jinja
{% from "jinjalume/components/spinner.html" import spinner %}

{{ spinner("Saving changes") }}
{{ spinner("Loading results", size="sm") }}
```

Signature: `spinner(label="Loading", size="md", class_name="")`

`size` supports `sm`, `md`, and `lg`. The wrapper has `role="status"` and an accessible label; the visible SVG is hidden from assistive technology.

Rendered shape:

```html
<span role="status" aria-label="Saving changes" class="...">...</span>
```

## Modal

Modals use a caller block and the browser's native `<dialog>` element:

```jinja
{% from "jinjalume/components/modal.html" import modal %}

<button type="button" onclick="document.getElementById('help').showModal()">
  Open help
</button>

{% call modal("help", "Help", description="About this form") %}
  <p>Use the close button or press Escape.</p>
{% endcall %}
```

Signature: `modal(id, title, description=None, class_name="")`

`id` must be unique in the document. The title is linked through `aria-labelledby`; when `description` is present it is also linked through `aria-describedby`. The close control submits a `method="dialog"` form, and no JavaScript framework is required.

Rendered shape:

```html
<dialog id="help" aria-labelledby="help-title" aria-describedby="help-description">...</dialog>
```

## Custom classes and CSS

All macros accept `class_name` for local composition. Jinjalume does not ship a compiled stylesheet: the consuming application owns its Tailwind build and must scan the Jinjalume template directory. The demo uses `static/src/input.css` and includes the token definitions described in [theming.md](theming.md).
