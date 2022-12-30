"""A lightweight theme for JupyterHub."""
import os
from pathlib import Path
from sphinx.util import logging

__version__ = "0.0.1"

THEME_PATH = (Path(__file__).parent / "theme" / "jupyterhub-sphinx-theme").resolve()

logger = logging.getLogger(__name__)

def set_config_defaults(app, config):
    theme = config.html_theme_options
    if not theme:
        theme = {}

    # Default jupyter favicon
    if not config.html_favicon:
        config.__dict__["html_favicon"] = (
            "https://github.com/jupyter/design/raw/master/logos/Favicon/favicon.png"
        )

    # Navigation bar
    if "navbar_align" not in theme:
        theme["navbar_align"] = "left"

    icon_links = [] if "icon_links" not in theme else theme["icon_links"]
    icon_links.extend(
        [
            {
                "name": "Discourse",
                "url": "https://discourse.jupyter.org/",
                "icon": "fa-brands fa-discourse",
                "type": "fontawesome",
            },
            {
                "name": "Team Compass",
                "url": "https://jupyterhub-team-compass.readthedocs.io/en/latest/",
                "icon": "fa-solid fa-compass",
                "type": "fontawesome",
            },
        ]
    )
    theme["icon_links"] = icon_links

    # Default logo
    logo = {} if "logo" not in theme else theme["logo"]
    if not logo:
        logo = {}
    if "image_dark" not in logo:
        logo["image_dark"] = "images/hub-rectangle-dark.svg"
    if "image_light" not in logo:
        logo["image_light"] = "images/hub-rectangle.svg"
    theme["logo"] = logo

    # Update the HTML theme config
    config.__dict__["html_theme_options"] = theme

    # Sphinxext Opengraph add URL based on ReadTheDocs variables
    # auto-generate this so that we don't have to manually add it in each documentation.
    # it should be addable via the environment variables.
    env = os.environ
    if "GITHUB_ACTION" in env:
        site_url = f"https://{env['GITHUB_REPOSITORY_OWNER']}.github.io/{env['GITHUB_REPOSITORY']}"
    elif "READTHEDOCS" in env:
        site_url = f"https://{env['READTHEDOCS_PROJECT']}.readthedocs.io/{env['READTHEDOCS_LANGUAGE']}/{env['READTHEDOCS_VERSION_NAME']}"
    else:
        # Don't do anything automatic if we aren't in RTD or GHP
        site_url = None
    if site_url and not hasattr(config, "ogp_site_url"):
        logger.info("Setting `ogp_site_url` via CI/CD environment variables...")
        config.__dict__["ogp_site_url"] = site_url

def setup(app):
    app.add_html_theme("jupyterhub_sphinx_theme", THEME_PATH)
    app.config.html_static_path.append(str(THEME_PATH / "static"))
    app.connect("config-inited", set_config_defaults)

    # Activate extensions
    for extension in ["sphinx_copybutton", "sphinxext.opengraph"]:
        app.setup_extension(extension)
