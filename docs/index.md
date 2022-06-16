# The JupyterHub documentation theme

A lightweight theme built on the PyData Sphinx Theme, for use by the JupyterHub community.
It makes minimal changes to the `pydata-sphinx-theme` in order to standardize styles and a top-bar that can be shared across all JupyterHub documentation.

## Theme build system

This theme uses the [`sphinx-theme-builder` tool](https://github.com/pradyunsg/sphinx-theme-builder), which is a helper tool for automatically compiling Sphinx theme assets.
This will download a local copy of NodeJS and build the theme's assets with the environment specified in `package.json`.

## Theme structure

This theme follows the [`sphinx-theme-builder` filesystem layout](https://sphinx-theme-builder.readthedocs.io/en/latest/reference/filesystem-layout/).

## Use this theme in a repository

To use this theme in the repository, follow these steps:

- Add this theme to the `pip` install requirements of the repo. For now, point it to the `main` branch like so:

  ```
  # in requirements.txt
  git+https://github.com/jupyterhub/jupyterhub-sphinx-theme
  ```
  
  or to install locally
  
  ```console
  $ pip install git+https://github.com/jupyterhub/jupyterhub-sphinx-theme
  ```
- Configure the Sphinx docs to use the theme by editing `conf.py`

  ```python
  html_theme = "jupyterhub_sphinx_theme"
  ```
  
- Make any customizations that you wish, following the [pydata sphinx theme documenation](https://pydata-sphinx-theme.readthedocs.io/en/stable/).

## Build the theme locally

You can build the documentation for this theme to preview it.
The easiest way to build the documentation in this repository is to use [the `nox` automation tool](https://nox.thea.codes/), a tool for quickly building environments and running commands within them.
This ensures that your environment has all the dependencies needed to build the documentation.

To do so, follow these steps:

1. Install `nox`

   ```console
   $ pip install nox
   ```
2. Build the documentation:

   ```console
   $ nox -s docs
   ```

This should create a local environment in a `.nox` folder, build the documentation (as specified in the `noxfile.py` configuration), and the output will be in `docs/_build/html`.

To build live documentation that updates when you update local files, run the following command:

```console
$ nox -s docs-live
```

## Examples

See the kitchen sink for some example pages.

```{toctree}
:maxdepth: 3
:glob:
reference/kitchen-sink/*
```
