import datetime

AUTHOR = 'Frogboots'
SITENAME = 'Mr Trashcan'
SITEURL = ""
PATH = "content"
DELETE_OUTPUT_DIRECTORY = True
SUMMARY_MAX_PARAGRAPHS = 1
DEFAULT_PAGINATION = 5

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'nest'
SITESUBTITLE = u'Where the truth goes on vacation...'

NEST_CSS_MINIFY = False

# Add items to top menu before pages
MENUITEMS = [('Home', '/'),
             ('Categories','/categories.html'),
             ('Authors','/authors.html'),
             ('About','/pages/about.html')]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = '' # 'header.png'
NEST_HEADER_LOGO = '/images/mtc_trans.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Recent', '/'),
                     ('Archives', '/archives.html'),
                     ('Categories','/categories.html'),
                     ('Authors','/authors.html')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'
year = str(datetime.datetime.now().year)
NEST_COPYRIGHT = u'<br>Copyright &copy; ' + year + ' Frogboots'
# Footer optional
NEST_FOOTER_HTML = ''
# index.html
NEST_INDEX_HEAD_TITLE = u'Mr Trashcan'
NEST_INDEX_HEADER_TITLE = u'Where the truth goes on vacation...'
NEST_INDEX_HEADER_SUBTITLE = u''
NEST_INDEX_CONTENT_TITLE = u'Recent Posts'
# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archives for all posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# article.html
NEST_ARTICLE_HEADER_BY = u'By'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = u'Posts archives'
NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u"Who's to blame"
NEST_AUTHORS_HEAD_DESCRIPTION = u"Who's to blame"
NEST_AUTHORS_HEADER_TITLE = u"Who's to blame"
NEST_AUTHORS_HEADER_SUBTITLE = u'Articles listed by author'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Articles listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Articles listed by category'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Category Archive'
NEST_CATEGORY_HEADER_TITLE = u'Category'
NEST_CATEGORY_HEADER_SUBTITLE = u'Category Archive'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archives'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archives'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
#    ("Pelican", "https://getpelican.com/"),
#    ("Python.org", "https://www.python.org/"),
#    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
)

STATIC_PATHS = ["images", "extra/favicon.ico", "extra/utilities.js"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/utilities.js": {"path": "utilities.js"},
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
