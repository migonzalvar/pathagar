import os

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
    
    # Book list:
    (r'^$', 'pathagar.books.views.latest', {}, 'latest'),
    (r'^by-title/$', 'pathagar.books.views.by_title', {}, 'by_title'),
    (r'^by-author/$', 'pathagar.books.views.by_author', {}, 'by_author'),
    (r'^tags/(?P<tag>[-\w]+)/$', 'pathagar.books.views.book_list_tag',
     {}, 'book_list_tag'),
    
    # Book list Atom:
    (r'^feed.atom', 'pathagar.books.views.latest',
     {'qtype': u'feed'}, 'latest_feed'),
    (r'^by-title.atom$', 'pathagar.books.views.by_title',
     {'qtype': u'feed'}, 'by_title_feed'),
    (r'^by-author.atom$', 'pathagar.books.views.by_author',
     {'qtype': u'feed'}, 'by_author_feed'),
    (r'^tags/(?P<tag>[-\w]+).atom$', 'pathagar.books.views.book_list_tag',
     {'qtype': u'feed'}, 'book_list_tag_feed'),
        
    # Add, view, edit and remove books:
    (r'^add/book/?$', 'pathagar.books.views.add_book'),
    (r'^view/book/(?P<book_id>\d+)/$', 'pathagar.books.views.book_detail'),
    (r'^edit/book/(?P<book_id>\d+)/?$', 'pathagar.books.views.edit_book'),
    (r'^remove/book/(?P<book_id>\d+)/?$', 'pathagar.books.views.remove_book'),
    
    
    # Add language:
    (r'^add/dc_language|language/?$', 'pathagar.books.views.add_language'),
    
    # Auth:
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    
    # Admin:
    (r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    from django.views.static import serve
    # Serve static media:
    urlpatterns += patterns('',
       url(r'^static_media/(?P<path>.*)$', serve,
           {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

       # Book files and covers:
       url(r'^books/(?P<path>.*)$', serve,
           {'document_root': os.path.join(settings.MEDIA_ROOT, 'books')}),
       url(r'^covers/(?P<path>.*)$', serve,
           {'document_root': os.path.join(settings.MEDIA_ROOT, 'covers')}),
    )
