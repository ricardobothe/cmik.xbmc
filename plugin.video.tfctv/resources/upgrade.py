# -*- coding: utf-8 -*-

'''
    Tfc.tv Add-on
    Copyright (C) 2018 cmik
'''

from resources.lib.libraries import control
from resources.lib.models import episodes
from resources.lib.models import shows
from resources.lib.models import library
logger = control.logger

def upgradeDB():

    # Load DB
    episodeDB = episodes.Episode(control.episodesFile)
    showDB = shows.Show(control.showsFile)
    libraryDB = library.Library(control.libraryFile)

    # DB upgrades per version
    if control.addonInfo('lastVersion') == '1.0.0-beta' and control.addonInfo('version') == '1.0.0':
    	control.showNotification('Upgrading databases...', control.lang(50002))
    	logger.logDebug(episodeDB.upgrade([
    		'ALTER TABLE `EPISODE` ADD COLUMN `TYPE` TEXT',
    		'UPDATE `EPISODE` SET TYPE = \'episode\' WHERE TYPE IS NULL']))
    	logger.logDebug(showDB.upgrade([
    		'ALTER TABLE `SHOW` ADD COLUMN `TYPE` TEXT',
    		'UPDATE `SHOW` SET TYPE = \'show\' WHERE TYPE IS NULL']))