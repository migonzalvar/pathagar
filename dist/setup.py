#!/usr/bin/env python

from distutils.core import setup

# all the specifics are selected in setup.cfg
setup(name='pathagar',
	packages = ['pathagar',
		'pathagar.books',
		'pathagar.books.management',
		'pathagar.books.management.commands'
		],
	package_dir = {'pathagar':''},
	package_data = {'pathagar':[
		'static_media/style/*.css',
		'static_media/style/blueprint/*.css',
#		'static_media/style/blueprint/plugins/rtl/*.txt',
#		'static_media/style/blueprint/plugins/rtl/*.css',
		'static_media/style/blueprint/plugins/rtl/*.txt',
		'static_media/style/blueprint/plugins/link-icons/*.{txt,css}',
		'static_media/style/blueprint/plugins/link-icons/*.txt',
		'static_media/style/blueprint/plugins/link-icons/icons/*',
		'static_media/style/blueprint/plugins/fancy-type/*',
		'static_media/style/blueprint/plugins/buttons/*.txt',
		'static_media/style/blueprint/plugins/buttons/*.css',
		'static_media/style/blueprint/plugins/buttons/icons/*',
		'templates/*.html',
		'templates/registration/*',
		'templates/admin/*',
		'templates/books/*',
		'AUTHORS',
		'COPYING',
		'README.mkd',
		'requirements.pip',
		'settings.*',
		'setup.*',
		'books/fixtures/*',
		'books/templates/*',
		'books/static/images/*',
		'books/static/js/*',
		]}
	)

