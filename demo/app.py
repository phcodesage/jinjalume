from flask import Flask, render_template, request

from jinjalume import Jinjalume

app = Flask(__name__)
Jinjalume(app)


@app.get("/")
def index():
    return render_template("index.html")


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
