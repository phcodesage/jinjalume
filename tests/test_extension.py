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
