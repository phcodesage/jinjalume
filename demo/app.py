from flask import Flask, render_template, request

from jinjalume import Jinjalume

app = Flask(__name__)
Jinjalume(app)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/blocks")
def blocks():
    return render_template("blocks.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    email = request.form.get("email", "").strip()
    errors = {}
    form_error = None
    success_message = None

    if request.method == "POST":
        if not email:
            errors["email"] = "Enter your email address."
        if not request.form.get("password"):
            errors["password"] = "Enter your password."
        if errors:
            form_error = "Review the fields below and try again."
        else:
            success_message = "Demo sign-in accepted. No account was created."

    return render_template(
        "login.html",
        email=email,
        remember=bool(request.form.get("remember")),
        email_error=errors.get("email"),
        password_error=errors.get("password"),
        form_error=form_error,
        success_message=success_message,
    )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    errors = {}
    form_error = None
    success_message = None

    if request.method == "POST":
        password = request.form.get("password", "")
        confirmation = request.form.get("password_confirmation", "")
        if not name:
            errors["name"] = "Enter your full name."
        if not email:
            errors["email"] = "Enter your email address."
        if len(password) < 8:
            errors["password"] = "Use at least 8 characters."
        if password != confirmation:
            errors["confirmation"] = "Passwords must match."
        if not request.form.get("terms"):
            errors["terms"] = "Accept the terms to continue."
        if errors:
            form_error = "Review the fields below and try again."
        else:
            success_message = "Demo account created. No data was saved."

    return render_template(
        "signup.html",
        name=name,
        email=email,
        name_error=errors.get("name"),
        email_error=errors.get("email"),
        password_error=errors.get("password"),
        confirmation_error=errors.get("confirmation"),
        terms_error=errors.get("terms"),
        form_error=form_error,
        success_message=success_message,
    )


@app.get("/admin")
def admin():
    return render_template(
        "admin.html",
        nav_items=[
            {"label": "Overview", "href": "/admin"},
            {"label": "Customers", "href": "#customers", "badge": "24"},
            {"label": "Orders", "href": "#orders"},
            {"label": "Analytics", "href": "#analytics"},
            {"label": "Settings", "href": "#settings"},
        ],
        metrics=[
            {
                "label": "Total revenue",
                "value": "$48,294",
                "change": "+12.8%",
                "note": "Compared with last month",
                "icon": "$",
            },
            {
                "label": "Active customers",
                "value": "2,431",
                "change": "+8.2%",
                "note": "Across all workspaces",
                "icon": "↗",
            },
            {
                "label": "Open tickets",
                "value": "18",
                "change": "-4.5%",
                "trend": "down",
                "note": "Compared with last week",
                "icon": "!",
            },
            {
                "label": "Conversion rate",
                "value": "6.24%",
                "change": "+1.4%",
                "note": "From 38,910 sessions",
                "icon": "%",
            },
        ],
        orders=[
            {
                "customer": "Olivia Martin",
                "email": "olivia@example.com",
                "amount": "$1,240.00",
                "status": "Paid",
                "date": "Sep 12, 2026",
            },
            {
                "customer": "Phoenix Baker",
                "email": "phoenix@example.com",
                "amount": "$860.00",
                "status": "Processing",
                "date": "Sep 11, 2026",
            },
            {
                "customer": "Lana Byrd",
                "email": "lana@example.com",
                "amount": "$540.00",
                "status": "Paid",
                "date": "Sep 11, 2026",
            },
            {
                "customer": "Demi Wilkinson",
                "email": "demi@example.com",
                "amount": "$320.00",
                "status": "Refunded",
                "date": "Sep 10, 2026",
            },
        ],
        activity=[
            {
                "label": "New workspace created",
                "detail": "Acme Inc. joined the Pro plan",
                "time": "12 minutes ago",
            },
            {
                "label": "Invoice paid",
                "detail": "Olivia Martin paid invoice #1048",
                "time": "48 minutes ago",
            },
            {
                "label": "Support ticket resolved",
                "detail": "Ticket #284 was closed by Maya",
                "time": "2 hours ago",
            },
        ],
    )


@app.route("/htmx", methods=["GET", "POST"])
def htmx_demo():
    """Show an optional HTMX enhancement with a plain form fallback."""

    submitted = request.method == "POST"
    message = request.form.get("message", "").strip()

    if submitted and message:
        result_variant = "success"
        result_title = "Server response"
        result_message = f"Received: {message}"
    elif submitted:
        result_variant = "danger"
        result_title = "Message required"
        result_message = "Enter a message before submitting the form."
    else:
        result_variant = None
        result_title = None
        result_message = None

    if request.headers.get("HX-Request") == "true":
        return render_template(
            "partials/htmx_result.html",
            result_variant=result_variant,
            result_title=result_title,
            result_message=result_message,
        )

    return render_template(
        "htmx.html",
        submitted=submitted,
        result_variant=result_variant,
        result_title=result_title,
        result_message=result_message,
    )
