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
