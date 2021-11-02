# -*- coding: utf-8 -*-
# Copyright 2020 SkyWater PDK Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import docutils
import os
import re
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'SkyWater SKY130 PDK'
copyright = '2020, SkyWater PDK Authors'
author = 'SkyWater PDK Authors'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinxcontrib_hdl_diagrams',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Enable github links when not on readthedocs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    html_context = {
        "display_github": True,         # Integrate GitHub
        "github_user": "google",        # Username
        "github_repo": "skywater-pdk",  # Repo name
        "github_version": "master",     # Version
        "conf_py_path": "/doc/",
    }
else:
    docs_dir = os.path.abspath(os.path.dirname(__file__))
    print("Docs dir is:", docs_dir)
    import subprocess
    subprocess.call('git fetch origin --unshallow', cwd=docs_dir, shell=True)
    subprocess.check_call('git fetch origin --tags', cwd=docs_dir, shell=True)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = re.sub('^v', '', os.popen('git describe ').read().strip())
# The short X.Y version.
version = release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'env',
    'Thumbs.db',
    '.DS_Store',
    # Files included in other rst files.
    'code-of-conduct.rst',
    'rules/periphery-rules.rst',
    'rules/device-details/*/index.rst',
    'rules/summary/*-key.rst',
    'rules/layers/*-key.rst',
    'rules/hv/*-key.rst',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# Prefix each section label with the name of the document it is in, followed by
# a colon. For example, index:Introduction for a section called Introduction
# that appears in document index.rst. Useful for avoiding ambiguity when the
# same section heading appears in different documents.
#autosectionlabel_prefix_document = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_symbiflow_theme"

html_logo = "_static/skywater-pdk-logo-top.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# https://sphinx-symbiflow-theme.readthedocs.io/en/latest/customization.html
html_theme_options = {
    'nav_title': 'SkyWater SKY130 PDK',

    'color_primary': 'light-green',
    'color_accent': 'teal',

    # Set the repo location to get a badge with stats
    'github_url': 'https://github.com/google/skywater-pdk',
    'repo_name': 'google/skywater-pdk',

    'globaltoc_depth': 4,

    # Hide the symbiflow links
    'hide_symbiflow_links': True,
    'license_url' : 'https://www.apache.org/licenses/LICENSE-2.0',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'skywater-pdk-doc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        # source start file
        master_doc,
        # target name
        'skywater-pdk.tex',
        # title
        'SkyWater SKY130 PDK Documentation',
        # author
        author,
        # document class
        'manual',
    ),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'skywater-pdk', 'SkyWater SKY130 PDK Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        # source start file
        master_doc,
        # target name
        'skywater-pdk',
        # title
        'SkyWater SKY130 PDK Documentation',
        # author
        author,
        # dir menu entry
        'SkyWater SKY130 PDK',
        # description
        'Documentation for open source PDK targetting SkyWater SKY130 process node.',
        # category
        'Miscellaneous',
    ),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# Enable the figures and numbers
numfig = True

# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


import re
from docutils.parsers.rst import directives, roles, nodes

LIB_REGEX = re.compile('sky130_(?P<lib_src>[^_\s]*)_(?P<lib_type>[^_\s]*)(_(?P<lib_name>[^_\s]*))?')
CELL_REGEX = re.compile('sky130_(?P<lib_src>[^_\s]*)_(?P<lib_type>[^_\s]*)(_(?P<lib_name>[^_\s]*))?__(?P<cell_name>[^\s]*)')

def lib_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Library name which gets colorized."""
    m = LIB_REGEX.match(text)
    if not m:
        msg = inliner.reporter.error("Malformed library name of "+repr(text), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    app = inliner.document.settings.env.app

    #lib_process_role = roles.role('lib_src', inliner.language, lineno, inliner.reporter)
    #lib_src_role = roles.role('lib_src', inliner.language, lineno, inliner.reporter)
    #lib_type_role = roles.role('lib_src', inliner.language, lineno, inliner.reporter)
    #lib_name_role = roles.role('lib_src', inliner.language, lineno, inliner.reporter)
    lib_process = 'sky130'
    lib_src = m.group('lib_src')
    lib_type = m.group('lib_type')
    lib_name = m.group('lib_name')

    r = [
        nodes.inline(lib_process, lib_process, classes=['lib-process']),
        nodes.inline('_', '_', options=options),
        nodes.inline(lib_src, lib_src, classes=['lib-src']),
        nodes.inline('_', '_', options=options),
        nodes.inline(lib_type, lib_type, classes=['lib-type']),
    ]
    if lib_name:
        r.append(nodes.inline('_', '_', options=options))
        r.append(nodes.inline(lib_name, lib_name, classes=['lib-name']))

    return r, []


def cell_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Cell name which gets colorized."""
    m = CELL_REGEX.match(text)
    if not m:
        msg = inliner.reporter.error("Malformed cell name of "+repr(text), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    app = inliner.document.settings.env.app

    #lib_process_role = roles.role('lib_src', inliner.language, lineno, inliner.reporter)
    #lib_src_role = roles.role('lib_src', inliner.language, lineno, inliner.reporter)
    #lib_type_role = roles.role('lib_src', inliner.language, lineno, inliner.reporter)
    #lib_name_role = roles.role('lib_src', inliner.language, lineno, inliner.reporter)
    lib_process = 'sky130'
    lib_src = m.group('lib_src')
    lib_type = m.group('lib_type')
    lib_name = m.group('lib_name')
    cell_name = m.group('cell_name')

    r = [
        nodes.inline(lib_process, lib_process, classes=['lib-process']),
        nodes.inline('_', '_', options=options),
        nodes.inline(lib_src, lib_src, classes=['lib-src']),
        nodes.inline('_', '_', options=options),
        nodes.inline(lib_type, lib_type, classes=['lib-type']),
    ]
    if lib_name:
        r.append(nodes.inline('_', '_', options=options))
        r.append(nodes.inline(lib_name, lib_name, classes=['lib-name']))
    r.append(nodes.inline('__', '__', options=options))
    r.append(nodes.inline(cell_name, cell_name, classes=['cell-name']))

    return r, []


def add_role(app, new_role_name):
    options = {
        'class': directives.class_option(new_role_name),
    }
    role = roles.CustomRole(new_role_name, roles.generic_custom_role, options, "")
    app.add_role(new_role_name, role)


def setup(app):
    app.add_css_file('extra.css')
    add_role(app, 'cell_name')
    add_role(app, 'lib_process')
    add_role(app, 'lib_src')
    add_role(app, 'lib_type')
    add_role(app, 'lib_name')
    add_role(app, 'drc_rule')
    add_role(app, 'drc_tag')
    add_role(app, 'drc_flag')
    add_role(app, 'layer')

    app.add_role('lib', lib_role)
    app.add_role('cell', cell_role)
    app.add_role('model', cell_role)
