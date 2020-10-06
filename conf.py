# -*- coding: utf-8 -*-
#
# How to in AIMMS documentation build configuration file, created by
# sphinx-quickstart on Wed Dec 13 15:09:51 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
if os.name == 'nt':
	import ssl
	import urllib
	
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
	  'sphinx.builders.linkcheck',
    'sphinx.ext.intersphinx',
    'sphinx_aimms_theme']

intersphinx_mapping = {'functionreference': ('https://documentation.aimms.com/functionreference/',
                                  (None,'objects-functionreference.inv'))}
	
if os.name != 'nt':

#Import spelling extension
    extensions.append('sphinx_sitemap')
    extensions.append('sphinx_last_updated_by_git')
        
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'AIMMS Documentation'
copyright = u'2018-2020, AIMMS'
author = u'AIMMS'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = u'1'
# The full version, including alpha/beta/rc tags.
# release = u'0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_aimms_theme'

if os.name == 'nt':
   
   Display_edit_on_gitlab = True
   # if builds locally (a windows machine), do not displays external extensions (Google Analytics, Community Embeddable, Algolia search, etc.)
   Display_3rd_Party_Extensions = False
else:

   # if builds on GitLab (a Linux machine), force "Edit on Gitlab" not to be shown, and displays external extensions (Google Analytics, Community Embeddable, Algolia search, etc.)
   Display_edit_on_gitlab = False
   Display_3rd_Party_Extensions = True

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {


    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
 #   'includehidden': True,
    'titles_only': True,
    'doc_title' : 'Documentation',
    'home_page_title': 'AIMMS Documentation',
    'home_page_description': "AIMMS Documentation is a help resource containing detailed product documentation and other reference materials including user guide, function list, modeling manual, language reference.",
    'display_community_embeddable' : Display_3rd_Party_Extensions,
    'google_analytics_id': 'UA-1290545-13',
    'generate_google_analytics' : Display_3rd_Party_Extensions,
    'display_algolia_search' : Display_3rd_Party_Extensions,
    'algolia_appid': 'BH4D9OD16A', 
    'algolia_appkey': 'f7e44f5b57ababa5c5ceb1e1087ae3b1', 
    'algolia_indexname': 'aimms',
}

# rst_epilog = ``` ``` 

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Add any variable here that you will be able to call in your templates   
html_context = {
    #'css_files': ['_static/aimms_2019_10_25.css'],
    "display_gitlab": Display_edit_on_gitlab, # Integrate Gitlab
    "gitlab_user": "aimms", # Username
    "gitlab_repo": "documentation", # Repo name
    "gitlab_version": "master", # Version
#    "conf_py_path": "", # Path in the checkout to the docs root
    "suffix": ".rst",
    "Display_3rd_Party_Extensions": Display_3rd_Party_Extensions
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        #'about.html',
        #'navigation.html',
        #'localtoc.html',
        #'relations.html',  # needs 'show_related': True theme option to display
        #'sourcelink.html',
        #'searchbox.html'
    ]
}

rst_prolog = """
:tocdepth: 2
"""

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'AIMMSdoc'
html_show_sourcelink = False

# index page for your site
html_baseurl = 'https://documentation.aimms.com/'

# adding path to non-rst files that go to the build
html_extra_path = ['robots.txt', 'meta-index-file.txt']

# -- Options for LaTeX output ---------------------------------------------

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
    (master_doc, 'AIMMS-doc.tex', u'AIMMS Documentation',
     u'AIMMS', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'aimmsdoc', u'AIMMS Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'AimmsDoc', u'AIMMS Documentation',
     author, 'AimmsDoc', 'AIMMS Documentation',
     'Miscellaneous'),
]

#import the one and only spelling exception central file 
# if os.name == 'nt':
	# context = ssl._create_unverified_context()
	# urllib.urlretrieve("https://gitlab.aimms.com/Arthur/unified-spelling_word_list_filename/raw/master/spelling_wordlist.txt", "spelling_wordlist.txt", context=context)

#spelling_word_list_filename = ''
		   
highlight_language = 'aimms'

