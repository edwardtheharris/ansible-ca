"""Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

# pylint: disable=invalid-name,redefined-builtin

from pathlib import Path
import version_query


def get_release():
    """Query the current release for the project."""
    repo_path = Path(".")
    ret_value = version_query.git_query.query_git_repo(repo_path).to_str()
    return ret_value


author = "Xander Harris"
autoyaml_depth = "10"
autoyaml_root = "."
autoyaml_safe_loader = False

project_copyright = "2024-%Y, Xander Harris. All rights reserved."

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".venv/*",
    ".tmp/*",
    ".pytest_cache/*",
    ".venv/",
]

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    # "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.duration",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.autoyaml",
]

favicons = [
    {
        "sizes": "16x16",
        "href": "img/ansible-16x16.png",
    },
    {
        "sizes": "32x32",
        "href": "img/ansible-32x32.png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "img/ansible-180x180.png",  # use a local file in _static
    },
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = "_static/img/ansible-16x16.png"
html_logo = "_static/img/ansible.png"
html_static_path = ["_static"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/edwardtheharris/ansible-k8s-nodes",
}
myst_dmath_double_inline = True
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_title_to_header = True
project = "Ansible CA"
release = "0.0.3"
rst_epilog = """
   .. topic:: <SUDO>
      
      <SUDO>
   .. sectionauthor:: Xander Harris <xandertheharris@gmail.com>
"""
show_authors = True
source_suffix = {".md": "markdown", ".rst": "restructuredText"}
templates_path = ["_templates"]
