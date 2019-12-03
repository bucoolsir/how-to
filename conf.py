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
from sphinx.builders import html as builders
from sphinx.util import logging
#import pdb
import subprocess


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
    'sphinx.ext.intersphinx',
	  'sphinx.builders.linkcheck',
    'sphinx_aimms_theme']
  
intersphinx_mapping = {'functionreference': ('https://documentation.aimms.com/functionreference',
                                  (None,'objects-functionreference.inv'))}

if os.name != 'nt':

#Import spelling extension
    extensions.append('sphinx_sitemap')
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'ContentIndex'

title = 'AIMMS How-To'

# General information about the project.
project = title
copyright = u'2019, AIMMS'
author = u'AIMMS'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1'
# The full version, including alpha/beta/rc tags.
release = u'0'

# includes these texts at the end of all source .rsts, helpful for using repetitive replacements 

rst_epilog = """
.. |date| date:: %B, %Y

.. |time| date:: %H:%M

Last Updated: |date|
"""

# include these texts at the beginning of all source .rsts, use only for HTML builds to update last updated date. 

rst_prolog = """
:tocdepth: 2
"""
# Last Updated on |date|
# """

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
pygments_style = 'default'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

#html_theme_path = ["."]

html_theme = 'sphinx_aimms_theme'

html_title = title

html_use_index = True
html_show_sourcelink = False

# if builds locally (a windows machine), force "Edit on Gitlab" to be shown, and do not displays Thumbs and Insided Embeddable (extensions)
if os.name == 'nt':
   Display_edit_on_gitlab = True
   Display_3rd_Party_Extensions = False
else:

   # if builds on GitLab (a Linux machine), force "Edit on Gitlab" not to be shown, and displays Thumbs and Insided Embeddable (extensions)
   Display_edit_on_gitlab = False
   Display_3rd_Party_Extensions = True

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {
    'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
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
 #   'titles_only': False
    'doc_title' : 'How-To',
    'home_page_title': 'AIMMS How-To',
    'home_page_description': "AIMMS How-To is a support knowledge base for everyone involved in projects that use AIMMS. You'll find help tutorials, best practices, and practical guidance for using AIMMS software.",
    'display_community_embeddable' : Display_3rd_Party_Extensions,
 }


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# The following "context" is passed to templates in _templates folder
html_context = {
    'css_files': ['_static/aimms_how_to_2019_10_25.css'],
    "display_gitlab": Display_edit_on_gitlab, # Integrate Gitlab
    "gitlab_user": "aimms/customer-support", # Username
    "gitlab_repo": "aimms-how-to", # Repo name
    "gitlab_version": "master", # Version
    "conf_py_path": "", # Path in the checkout to the docs root
    "suffix": ".rst",
    "Display_3rd_Party_Extensions" : Display_3rd_Party_Extensions # display Thumbs and Insided Embeddable
    
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'localtoc.html',
#         #'relations.html',  # needs 'show_related': True theme option to display
#         #'sourcelink.html',
#         'searchbox.html'
#     ]
# }

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'HowToinAIMMSdoc'


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
    (master_doc, 'HowToinAIMMS.tex', title,
     u'AIMMS User Support Team', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'howtoinaimms', title,
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, title, title,
     author, title, 'One line description of project.',
     'Miscellaneous'),
]

# if builds on GitLab (a Linux machine), force todos not to be shown :)
if os.name == 'nt':
   nitpicky = True
else:
	#To check any broken links 
   todo_include_todos = False

# index page for your site (used by sitemap extension)
html_baseurl = 'https://how-to.aimms.com/'

# adding path to non-rst files that go to the build
html_extra_path = ['robots.txt']

#------------------------------------------------- Generate redirects from old URLs  ----------------------------------------------------------#

redirects_file = "WebSite_Redirection_Mapping/redirection_map.txt"

"""
    sphinxcontrib.redirects
    ~~~~~~~~~~~~~~~~~~~~~~~
    Generate redirects for moved pages when using the HTML builder.
    See the README file for details. https://github.com/sphinx-contrib/redirects/blob/master/sphinxcontrib/redirects/__init__.py
    :copyright: Copyright 2017 by Stephen Finucane <stephen@that.guru>
    :license: BSD, see LICENSE for details.
"""

TEMPLATE = """<html>
  <head><meta http-equiv="refresh" content="0; url=/%s"/></head>
</html>
"""

def generate_redirects(app):
    
    logger = logging.getLogger(__name__)
    
    #only if not on Linux (Gitlab computers)
    if os.name == 'nt':
        #Generates the mapping file out of Git logs by launching a batch script, Assuming you have git installed on your computer... 
        try:
            subprocess.call([r'WebSite_Redirection_Mapping\\Run_generate_redirection_map.bat'], stdout=open(os.devnull, 'wb'))
            logger.info("Redirection map file has been written in WebSite_Redirection_Mapping\\redirection_map_full.txt")
        except:
            logger.warning("Website Mapping file couldn't be generated. Please debug the generate_redirects() function in conf.py. Redirection mapping is ignored.")
            pass
            return
        
    #pdb.set_trace()
    path = os.path.join(app.srcdir, app.config.redirects_file)
    if not os.path.exists(path):
        app.info("Could not find redirects file at '%s'" % path)
        return

    in_suffix = app.config.source_suffix.keys()[0]

    # TODO(stephenfin): Add support for DirectoryHTMLBuilder
    if not type(app.builder) == builders.StandaloneHTMLBuilder:
        app.warn("The 'sphinxcontrib-redirects' plugin is only supported "
                 "by the 'html' builder. Skipping...")
        return
    
    
    logger.info("Redirection Generation has started..." )
    redirects_counter = 0
    with open(path) as redirects:
        for line in redirects.readlines():
            from_path, to_path = line.rstrip().split('\t')
            redirects_counter += 1
            #To have an overview of all the redirections generated, enable logs :)
            #logger.info("Redirecting '%s' to '%s'" % (from_path, to_path))
            
            from_path = from_path.replace(in_suffix, '.html')
            to_path_prefix = '..%s' % os.path.sep * (
                len(from_path.split(os.path.sep)) - 1)
            to_path = to_path_prefix + to_path.replace(in_suffix, '.html')

            redirected_filename = os.path.join(app.builder.outdir, from_path)
            redirected_directory = os.path.dirname(redirected_filename)
            if not os.path.exists(redirected_directory):
                os.makedirs(redirected_directory)

            with open(redirected_filename, 'w') as f:
                f.write(TEMPLATE % to_path)
                
    logger.info("Redirection Generation has finished successfully! With %i redirections" % redirects_counter )
    
# The setup function here is picked up by sphinx at each build. You may input any cool change here, like syntax highlighting or redirects
def setup(sphinx):
	
   #To handle redirections
   handle_redirections = False
   if handle_redirections or os.name != 'nt':
		sphinx.add_config_value('redirects_file', 'redirects', 'env')
		sphinx.connect('builder-inited', generate_redirects)   
 
highlight_language = 'aimms'