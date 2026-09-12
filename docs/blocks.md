# Jinjalume UI blocks

UI blocks are composition-level templates for common application screens. They use the same server-rendered macros as the component gallery and do not require Flowbite, a JavaScript framework, or a client-side router.

The demo previews these blocks at `/blocks`:

- `/login` — login form with email, password, remember-me, forgot-password, and validation states
- `/signup` — account creation form with password confirmation, terms consent, and validation states
- `/admin` — responsive admin dashboard with sidebar navigation, mobile details menu, KPI cards, an order table, and activity timeline

## Authentication shell

```jinja
{% from "jinjalume/blocks/auth.html" import auth_shell, login_form %}

{% call auth_shell(
    "Welcome back",
    description="Sign in to continue to your workspace.",
    eyebrow="Sign in",
    alternate_label="New here?",
    alternate_href="/signup",
    alternate_text="Create an account"
) %}
  {{ login_form(action="/login", forgot_href="/forgot-password") }}
{% endcall %}
```

Signature: `auth_shell(title, description=None, eyebrow="Welcome", alternate_label=None, alternate_href=None, alternate_text=None, class_name="")`

The caller block contains the form or other authentication content. The shell supplies a responsive split layout, a branded desktop panel, a mobile brand link, and an alternate-action footer.

## Login and signup forms

```jinja
{% from "jinjalume/blocks/auth.html" import login_form, signup_form %}

{{ login_form(
    action="/login",
    email="person@example.com",
    email_error="Use your work email.",
    password_error="Enter your password."
) }}

{{ signup_form(
    action="/signup",
    name="Taylor Morgan",
    email="taylor@example.com",
    password_error="Use at least 8 characters."
) }}
```

Signatures:

- `login_form(action="", method="post", email="", remember=False, email_error=None, password_error=None, form_error=None, forgot_href="#", submit_label="Sign in", class_name="")`
- `signup_form(action="", method="post", name="", email="", name_error=None, email_error=None, password_error=None, confirmation_error=None, terms_error=None, form_error=None, terms_href="#", submit_label="Create account", class_name="")`

Both forms use the existing input and button primitives, so errors are exposed through `aria-invalid` and linked descriptions. The forms submit normally with `POST`; validation and authentication remain the consuming application's responsibility.

## Dashboard shell

```jinja
{% from "jinjalume/blocks/dashboard.html" import dashboard_shell, stat_card %}

{% call dashboard_shell(
    title="Overview",
    description="Monitor your workspace performance.",
    nav_items=[
        {"label": "Overview", "href": "/admin"},
        {"label": "Customers", "href": "/customers", "badge": "24"}
    ],
    active_item="Overview",
    user_name="Alex Morgan",
    user_email="alex@example.com"
) %}
  <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
    {{ stat_card("Total revenue", "$48,294", change="+12.8%", icon="$") }}
    {{ stat_card("Open tickets", "18", change="-4.5%", trend="down", icon="!") }}
  </div>
{% endcall %}
```

Signatures:

- `dashboard_nav(nav_items=[], active_item="Overview", class_name="")`
- `stat_card(label, value, change=None, trend="up", note=None, icon=None, class_name="")`
- `dashboard_shell(title="Overview", description=None, nav_items=[], active_item="Overview", user_name="Alex Morgan", user_email="alex@example.com", class_name="")`

`nav_items` accepts mappings with `label`, `href`, optional `badge`, and optional `active` keys. The dashboard shell renders a desktop sidebar and a native `<details>` mobile menu. Put tables, charts, filters, or other application-specific content in the caller block.
