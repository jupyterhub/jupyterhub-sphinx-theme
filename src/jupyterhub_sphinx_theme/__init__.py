"""A lightweight theme for JupyterHub."""
import os
from pathlib import Path

__version__ = "0.0.1"

THEME_PATH = (Path(__file__).parent / "theme" / "jupyterhub-sphinx-theme").resolve()


def set_config_defaults(app, config):
    theme = config.html_theme_options
    BREAK

    # Navigation bar
    if "navbar_align" not in theme:
        theme["theme_navbar_align"] = "left"


def set_html_defaults(app, pagename, templatename, context, doctree):
    theme = app.config.html_theme_options
    if not theme:
        theme = {}

    # Navigation bar
    if "navbar_align" not in theme:
        context["theme_navbar_align"] = "left"

    icon_links = [] if "icon_links" not in theme else theme["icon_links"]
    icon_links.extend(
        [
            {
                "name": "Discourse",
                "url": "https://discourse.jupyter.org/",
                "icon": "fab fa-discourse",
                "type": "fontawesome",
            },
            {
                "name": "jupyter.org",
                "url": "https://jupyter.org/",
                "icon": "https://github.com/jupyter/design/raw/master/logos/Favicon/favicon.png",
                "type": "url",
            },
            {
                "name": "Twitter",
                "url": "https://twitter.com/ProjectJupyter",
                "icon": "fab fa-twitter",
                "type": "fontawesome",
            },
        ]
    )
    context["theme_icon_links"] = icon_links

    # Default logo
    logo = {} if "logo" not in theme else theme["logo"]
    if not logo:
        logo = {}
    if "image_dark" not in logo:
        logo["image_dark"] = "images/hub-rectangle-dark.svg"
    if "image_light" not in logo:
        logo["image_light"] = "images/hub-rectangle.svg"
    context["theme_logo"] = logo


def setup(app):
    app.add_html_theme("jupyterhub_sphinx_theme", THEME_PATH)
    app.setup_extension("sphinx_copybutton")
    app.config.html_static_path.append(str(THEME_PATH / "static"))
    app.config.html_favicon = (
        "https://github.com/jupyter/design/raw/master/logos/Favicon/favicon.png"
    )
    app.connect("html-page-context", set_html_defaults)
    app.connect("config-inited", set_config_defaults)
