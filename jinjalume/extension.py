"""Flask integration for the Jinjalume Jinja component templates."""

from __future__ import annotations

from jinja2 import ChoiceLoader, PackageLoader


class Jinjalume:
    """Register Jinjalume's reusable templates with a Flask application.

    Jinjalume intentionally does not take over an application's static folder
    or Tailwind configuration. This keeps the extension compatible with an
    existing asset pipeline while making the component templates available.
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Attach Jinjalume to *app* and preserve the app's template loader."""

        package_loader = PackageLoader("jinjalume", "templates")
        application_loader = app.jinja_loader

        if application_loader is None:
            app.jinja_loader = package_loader
        elif not isinstance(application_loader, ChoiceLoader):
            app.jinja_loader = ChoiceLoader([package_loader, application_loader])
        else:
            app.jinja_loader = ChoiceLoader([package_loader, *application_loader.loaders])

        app.extensions["jinjalume"] = self
