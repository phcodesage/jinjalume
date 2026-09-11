from flask import Flask, render_template_string

from jinjalume import Jinjalume


def test_extension_registers_package_templates():
    app = Flask(__name__)
    extension = Jinjalume(app)

    with app.app_context():
        rendered = render_template_string(
            '{% from "jinjalume/components/button.html" import button %}'
            '{{ button("Save", variant="primary") }}'
        )

    assert app.extensions["jinjalume"] is extension
    assert '<button type="button"' in rendered
    assert "Save" in rendered
    assert "bg-slate-900" in rendered


def test_extension_preserves_application_templates(tmp_path):
    templates = tmp_path / "templates"
    templates.mkdir()
    (templates / "custom.html").write_text("Custom template", encoding="utf-8")

    app = Flask(__name__, template_folder=str(templates))
    Jinjalume(app)

    with app.app_context():
        rendered = render_template_string('{% include "custom.html" %}')

    assert rendered == "Custom template"


def test_extended_components_render():
    app = Flask(__name__)
    Jinjalume(app)

    template = """
    {% from "jinjalume/components/avatar.html" import avatar %}
    {% from "jinjalume/components/modal.html" import modal %}
    {% from "jinjalume/components/spinner.html" import spinner %}
    {% from "jinjalume/components/textarea.html" import textarea_field %}
    {{ avatar("Jinjalume") }}
    {{ spinner("Saving") }}
    {{ textarea_field("message", label="Message", required=True) }}
    {% call modal("example", "Example dialog") %}Dialog content{% endcall %}
    """

    with app.app_context():
        rendered = render_template_string(template)

    assert 'aria-label="Jinjalume"' in rendered
    assert 'aria-label="Saving"' in rendered
    assert 'id="message"' in rendered
    assert 'id="example"' in rendered
    assert "Dialog content" in rendered


def test_component_markup_exposes_accessible_semantics():
    app = Flask(__name__)
    Jinjalume(app)

    template = """
    {% from "jinjalume/components/alert.html" import alert %}
    {% from "jinjalume/components/avatar.html" import avatar %}
    {% from "jinjalume/components/button.html" import button %}
    {% from "jinjalume/components/input.html" import input_field %}
    {% from "jinjalume/components/modal.html" import modal %}
    {% from "jinjalume/components/spinner.html" import spinner %}
    {% from "jinjalume/components/textarea.html" import textarea_field %}
    {{ button("Save", disabled=True) }}
    {{ input_field("email", label="Email", error="Enter an email address") }}
    {{ textarea_field("message", label="Message", error="Enter a message") }}
    {{ alert("Changes were saved", title="Saved") }}
    {{ avatar("Jinjalume", src="/avatar.png") }}
    {{ spinner("Saving") }}
    {% call modal("confirm", "Confirm changes") %}Review your changes.{% endcall %}
    """

    with app.app_context():
        rendered = render_template_string(template)

    assert '<button type="button"' in rendered
    assert "disabled>Save</button>" in rendered
    assert '<label for="email"' in rendered
    assert 'id="email"' in rendered
    assert 'aria-describedby="email-error"' in rendered
    assert 'id="email-error"' in rendered
    assert '<label for="message"' in rendered
    assert 'id="message"' in rendered
    assert 'aria-describedby="message-error"' in rendered
    assert 'id="message-error"' in rendered
    assert 'role="alert"' in rendered
    assert "Changes were saved" in rendered
    assert '<img src="/avatar.png" alt="Jinjalume"' in rendered
    assert 'role="status" aria-label="Saving"' in rendered
    assert '<dialog id="confirm" aria-labelledby="confirm-title"' in rendered
    assert '<h2 id="confirm-title"' in rendered
    assert '<button type="submit" aria-label="Close dialog"' in rendered
