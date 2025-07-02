# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# -- Project information -----------------------------------------------------

project = 'cosmotic'
copyright = '2025, Bonolo Mphahlele'
author = 'Bonolo Mphahlele'


# -- Path setup --------------------------------------------------------------

# Add the project root directory to sys.path (adjust '..' if your docs folder is not at project root)
sys.path.insert(0, os.path.abspath('..'))

# Set the Django settings module environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'cosmotic.settings'

# Setup Django
django.setup()


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',     # Automatically generate documentation from docstrings
    'sphinx.ext.napoleon',    # Support for Google style docstrings
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']