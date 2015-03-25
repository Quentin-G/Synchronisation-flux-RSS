#-*- coding: utf-8 -*-
from distutils.core import setup

setup(
	name = 'FeedSynchronizer',
	packages = ['FeedSynchronizer'],
	version = '1.0.0',
	description = 'Synchronizing a RSS feed to social networks',
	author = 'Florent Desnous, Quentin Girod, Thomas Marçais',
	author_email = 'florent.desnous@gmail.com',
	url = 'https://github.com/Quentin-G/Synchronisation-flux-RSS',
	install_requires = [
		'pytumblr',
		'facebook',
		'linkedin',
		'TwitterAPI',
		'feedparser',
		'flup']
)