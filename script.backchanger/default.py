# -*- coding: utf-8 -*-
#------------------------------------------------------------
# KepaIPTV - XBMC Add-on by Kepa
# Version 2.1 (26.04.2021)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)



import os
import sys
import urllib
import urllib2
import re
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import requests
import base64

addon = xbmcaddon.Addon()
addonname = '[LOWERCASE][CAPITALIZE][COLOR white]kepa[COLOR white]Background Changer[/CAPITALIZE][/LOWERCASE][/COLOR]'
icon = addon.getAddonInfo('icon')
myaddon = xbmcaddon.Addon("script.backchanger")

def cambia_fondo():
	can_continue=True
	foto = xbmc.translatePath('special://home/addons/script.backchanger/fondo.jpg')
	
	try:
		f=open(foto,'r')
		f.close()

	except:
		url = 'https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/media/image/2018/11/superman-worlds-finest_1.jpg'
		try:
			r = requests.get(url, allow_redirects=True)
			f=open(foto, 'wb').write(r.content)
			f.close()
		except:
			can_continue=False
			xbmc.executebuiltin('Notification(Error accesing internet,There must be some problem with your internet conection, take a look to your proxy,8000')

	if  xbmc.getCondVisibility('Skin.String(CustomBackgroundPath)')==0 and can_continue:
		xbmc.executebuiltin('Skin.Reset(CustomBackgroundPath)')
		xbmc.executebuiltin('Skin.SetBool(UseCustomBackground,True)')
		xbmc.executebuiltin('Skin.SetString(CustomBackgroundPath,'+foto+')')
		xbmc.executebuiltin('ReloadSkin()')


cambia_fondo()