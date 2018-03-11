# -*- coding: cp1252 -*-
import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs,unicodedata,socket,random
import urlresolver
from imports import cloudflare,googleplus,client,cleantitle
from imports import yt
import xml.etree.ElementTree as ElementTree
import httplib
import liveresolver
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2,urllib, glob, traceback
import re
from imports import extract
from imports import downloader
import plugintools
import zipfile
import time
import ntpath
import cookielib
from imports.jsunpack import unpack as packets
from imports.common import random_agent
from imports import Parse, CNF_Studio_Indexer, speedtest, uservar, tools
try:
  import StorageServer
except:
  import storageserverdummy as StorageServer
cache = StorageServer.StorageServer("plugin.video.GenieTv", 24)
try:
    import json
except:
    import simplejson as json
from threading import Thread
from datetime import date, datetime, timedelta
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup, BeautifulSOAP
from cookielib import CookieJar
from addon.common.addon import Addon
from addon.common.net import Net
from imports.tvGuide import gui
import webbrowser
import SimpleDownloader

#################
ooOOOoo = ''
def ttTTtt(i, t1, t2=[]):
 t = ooOOOoo
 for c in t1:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1] 	
   i = 0  
 for c in t2:
  t += chr(c)
  i += 1
  if i > 1:
   t = t[:-1]
   i = 0
 return t
 

###THANK YOU TO THE PEOPLE THAT ORIGINALY WROTE SOME OF THIS CODE "STUART DENTON, PIPCAN, MIKEY1234, WHUFCLEE" TO NAME A FEW, WITHOUT YOU I STILL PROBABLY WOULDNT HAVE A CLUE WHERE TO START###
VERSION = "3.6.6"
ADDON_ID='plugin.video.GenieTv'
repo_path = xbmc.translatePath('special://home/addons/repository.GenieTv')
ADDONS = xbmc.translatePath('special://home/addons/')
Addons = xbmc.translatePath('special://home/addonsbroke/')
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
addon_id = 'plugin.video.GenieTv'
EXCLUDES     = ['plugin.video.GenieTv','script.module.addon.common','repository.GenieTv']
ADDON = xbmcaddon.Addon(id=addon_id)
MEDIA = xbmc.translatePath('special://home/media')
AddonID='plugin.video.GenieTv'
dp =  xbmcgui.DialogProgress()
AddonTitle='[COLORsteelblue]GenieTv[/COLOR]' 
SPEEDFILE = base64.b64decode('aHR0cDovL2dlbmlldHYuY28udWsvc3BlZWR0ZXN0LnR4dA==')
CONTACT = uservar.CONTACT
Decode = base64.decodestring
setSetting = xbmcaddon.Addon().setSetting
Base_reap = (Decode('aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIv'))
HOME           = xbmc.translatePath('special://home/')
USERDATA       = os.path.join(HOME,      'userdata')
ADDONDATA      = os.path.join(USERDATA,  'addon_data', ADDON_ID)
WIZLOG         = os.path.join(ADDONDATA, 'wizard.log')
ADDONTITLE     = uservar.ADDONTITLE
PROFILE        = xbmc.translatePath('special://profile/')
LOGFILES       = ['xbmc.log', 'xbmc.old.log', 'kodi.log', 'kodi.old.log', 'spmc.log', 'spmc.old.log', 'tvmc.log', 'tvmc.old.log']
ADDONS         = os.path.join(HOME,     'addons')
PACKAGES       = os.path.join(ADDONS,   'packages')
THUMBS         = os.path.join(USERDATA,  'Thumbnails')
DATABASE       = os.path.join(USERDATA,  'Database')
HUB       = os.path.join(ADDONS,   'HUB')
APKFILE      = (Decode('aHR0cDovL2dlbmlldHYuY28udWsvYXBrLnR4dA=='))
net = Net()
Dialog = xbmcgui.Dialog()
MyBuild = ADDON.getSetting('Build')
MyLocal = ADDON.getSetting('Local')
RemoteM3u = ADDON.getSetting('Remote')
LocalM3u = ADDON.getSetting('LocalM3u')
TEXTCOL = ADDON.getSetting('TEXTCOL')
DOWNCONT = ADDON.getSetting('Downloads')
LOG = xbmc.translatePath('special://logpath/')
U = ADDON.getSetting('User')
Pass = ADDON.getSetting('Pass')
DNS = ADDON.getSetting('DNS')
if DNS == 'Option 1':                                           
	DDNS = '.net'                                                   
if DNS == 'Option 2':                                           
	DDNS = '.eu'                                                   
if DNS == 'Option 3':                                           
	DDNS = '.com'
Adult_Pass = ADDON.getSetting('AdultPass')
Dialog = xbmcgui.Dialog()
HOME = xbmc.translatePath('special://home/')
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
ORIGIN_IMAGE = (Decode('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw=='))
DBPATH = xbmc.translatePath('special://database')
favorites_folder = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.GenieTV')
TNPATH = xbmc.translatePath('special://thumbnails');
PATH = "GenieTv"        
WIPE_ADDON 	 =  xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv'))
Change_Log_Path = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv/Change_Log_Temp'))
H = 'http://'
ART = base64.decodestring('aHR0cDovL2dlbmlldHYuY28udWsvZ2VuaWV0dl9hcnQvYmVuc19hcnQv')
now = datetime.now()
CAT = base64.decodestring('LnBocA==')
BASEK = base64.decodestring('aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=')
youtube_list =[]
reset_database = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py'))
start_guide = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py'))
localizedString = ADDON.getLocalizedString
cookieJar = CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
urlOpener.addheaders = [('User-Agent', 'Mozilla/5.0')]
addon_handle = int(sys.argv[1])
profile = xbmc.translatePath(ADDON.getAddonInfo('profile').decode('utf-8'))
favorites = os.path.join(favorites_folder, 'favorites')
Addons_ini = favorites_folder + '/addons.ini'
USERDATA = xbmc.translatePath('special://home/userdata/')
userdata = xbmc.translatePath('special://home/userdatabroke/')
ADDON_PATH = xbmc.translatePath('special://home/addons/plugin.video.GenieTv') 
USERDATA_PATH = xbmc.translatePath('special://home/userdata/addon_data')     
ADDON_DATA = USERDATA_PATH + 'GenieTvWatched' 
Main 		= (Decode('aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYw=='))
Sources = ['daclips','filehoot','allmyvideos','vidspot','vodlocker','vidto']	                                                                                     
watched = ADDON_DATA + 'watched.txt'                                       
if not os.path.exists(ADDON_DATA):                                           
    os.makedirs(ADDON_DATA)                                                   
watched = ADDON_DATA + 'watched.txt'                                       
if not os.path.exists(watched):                                             
    open(watched,'w+')                                                       
watched_read = open(watched).read()
Base_Pand = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv'))
IVUE 		 =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/script.ivueguide/master.db'))
FAVS         =  xbmc.translatePath(os.path.join('special://home/userdata','favourites.xml'))
GENIE_FAVS	 =  xbmc.translatePath(os.path.join('special://home/userdata/addon_data/plugin.video.GenieTv/favorites'))
GENIE_ADDON_XML = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv/addon.xml'))
Repo_Addon_Xml = xbmc.translatePath(os.path.join('special://home/addons/repository.GenieTv/addon.xml'))  
if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
else: FAV = []
debug = ADDON.getSetting('debug')
if os.path.exists(favorites_folder)==False:
    os.makedirs(favorites_folder)
def OPEN_Search(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = ''
        link = ''
        try: 
            response = urllib2.urlopen(req)
            link=response.read()
            response.close()
        except: pass
        if link != '':
            return link
        else:
            link = 'Failed'
            return link

BASEURL_List = []
HTML = OPEN_Search(Decode('aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8='))
if HTML != 'Failed':
	BASEURL_List.append(Decode('aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8='))
if not HTML != 'Failed':
    HTML2 = OPEN_Search(Decode('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v'))
    if HTML2 != 'Failed':
		BASEURL_List.append(Decode('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v'))
    if not HTML2 != 'Failed':
        HTML3 = OPEN_Search(Decode('aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v'))
        if HTML3 != 'Failed':
            BASEURL_List.append(Decode('aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v'))
        if not HTML3 != 'Failed':
            HTML4 = OPEN_Search(Decode('aHR0cDovLzUuMTM1LjEuNDYvcmVkby8='))
            if HTML4 != 'Failed':
                BASEURL_List.append(Decode('aHR0cDovLzUuMTM1LjEuNDYvcmVkby8='))
else:
    pass
BASEURL = (str(BASEURL_List)).replace('[\'','').replace('\']','')	

	
	
def Repo_Check():
    if not os.path.exists(repo_path):
        Dialog.ok("[COLOR=white]Incompatible[/COLOR]", "Unfortunately GenieTv will only work with",'its official repo please install from trusted source','')
        addon = 'genie tv repo not being installed '
    	Force_Repo_Download()
    else:		
        Version_Checker()

def Version_Checker():			

    Correct_Versions = OPEN_URL(Decode('aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0'))
    Version_Check = open(GENIE_ADDON_XML).read()
    Repo_Version_Check = open(Repo_Addon_Xml).read()

    match = re.compile('version="([^"]*)" provider').findall(Version_Check)
    match2 = re.compile('version="([^"]*)" provider-name').findall(Repo_Version_Check)
    correct_match_addon = re.compile('GENIE TV ADDON - Version = &quot;(.+?)&quot;').findall(Correct_Versions)
    correct_match_repo = re.compile('GENIE TV REPO - Version = &quot;(.+?)&quot;').findall(Correct_Versions)
    for version in match:
        result1 = version
        for correct_addon in correct_match_addon:
            if not correct_addon == result1:
                dp.create('Incorrect Addon Version','Downloading Correct Version',)
                xbmc.sleep(1000)
                dp.close
                Force_Addon_Download()
            if correct_addon == result1:
                addon_check			
    for repo_version in match2:
        result2 = repo_version
        for correct_repo in correct_match_repo:
            if not correct_repo == result2:
                dp.create('Incorrect Repo Installed','Installing Correct Version','')
                xbmc.sleep(1000)
                dp.close
                Force_Repo_Download()
            if correct_repo == result2:
                xbmc.sleep(100)
                addon_check 
def Change_Log():
    if not os.path.exists(Change_Log_Path):
        TextBox('Change Log 11/03/2018 - v3.6.6','[COLORsteelblue]Pandoras Box Returns,[CR][COLORsteelblue]Add URLResolve,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section Gets A Massive Revamp[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]')
        os.makedirs(Change_Log_Path)
def Change_Log2():
    TextBox('Change Log 11/03/2018 - v3.6.6','[COLORsteelblue]Pandoras Box Returns,[CR]Tommys Sports Makes A Massive Return[/COLOR],[CR][COLORsteelblue]Sports Replays Updated[/COLOR],[CR][COLORsteelblue]G.O.D.S Returns Updated With All Your Latest Goddies[/COLOR],[CR][COLORsteelblue]Apprentice Returns With An All New Super Movies Section[/COLOR],[CR][COLORsteelblue]Cozy Corner Updated Stories Section Gets A Massive Revamp[/COLOR],[CR][COLORsteelblue]Dead Sections Repaired Or Removed[/COLOR],[CR][COLORsteelblue]Tweaks And Fixes Throughout[/COLOR]')
def DDNS_Log():
	TextBox(DDNS,DDNS)
def TextBox(title, msg):
	class TextBoxes(xbmcgui.WindowXMLDialog):
		def onInit(self):
			self.title      = 101
			self.msg        = 102
			self.scrollbar  = 103
			self.okbutton   = 201
			self.showdialog()

		def showdialog(self):
			self.getControl(self.title).setLabel(title)
			self.getControl(self.msg).setText(msg)
			self.setFocusId(self.scrollbar)
			
		def onClick(self, controlId):
			if (controlId == self.okbutton):
				self.close()
		
		def onAction(self, action):
			if   action == ACTION_PREVIOUS_MENU: self.close()
			elif action == ACTION_NAV_BACK: self.close()
			
	tb = TextBoxes( "Textbox.xml" , ADDON.getAddonInfo('path'), 'DefaultSkin', title=title, msg=msg)
	tb.doModal()
	del tb

def INDEX():
    Repo_Check()
    Change_Log()
    if ADDON.getSetting('Simplify')=='true':
        INDEXsimp()
    else:
#        if ADDON.getSetting('My Build')=='true':
#            addDir('[COLOR'+TEXTCOL+']WIZARD[/COLOR]',str(BASEURL),4001,ART+'Wizard.png',FANART,'')
#        addDir('[COLOR'+TEXTCOL+']TEST[/COLOR]','',219999989,ART+'GTV.png',FANART,'')
        addDir('[COLOR'+TEXTCOL+']G-Tv Live List[/COLOR]','',4009,ART+'GTV.png',FANART,'')
        addDir('[COLOR'+TEXTCOL+']Tommys Sports[/COLOR]','',90010,ART + 'tommys.png',FANART,'')
        if ADDON.getSetting('Streams')=='true':
            addDir('[COLOR'+TEXTCOL+']STREAMS[/COLOR]',str(BASEURL),4002,ART+'Streams.png',FANART,'')
#        addDir('[COLOR'+TEXTCOL+']GENIE STORE[/COLOR]','http://genietv.co.uk/store.php',21008,ART+'store.png',FANART,'Direct Access To The GenieTv Store')
#        if ADDON.getSetting('Music')=='true':
#            addDir('[COLOR'+TEXTCOL+']Music[/COLOR]',str(BASEURL),4003,ART+'Music.png',FANART,'')
#        if Adult_Pass == '5knuckleshuffle':
#            addDir('[COLORorangered]Adult Content[/COLOR]','',19999999,ART+'AG.png',FANART,'')
        addDir('[COLOR'+TEXTCOL+']TOOLS[/COLOR]','',90001,ART+'tools.png',FANART,'')
        addDir2('[COLOR'+TEXTCOL+']OPEN SETTINGS[/COLOR]','',60000,ART+'settings.png',FANART,'')
        if platform() == 'android':
            addDir('[COLOR'+TEXTCOL+']APK TOOL[/COLOR]',str(BASEURL),30039,ART+'APKpng',FANART,'')
#        if ADDON.getSetting('Source List')=='true':
#            addDir2('[COLOR'+TEXTCOL+']SOURCE LIST[/COLOR]',str(BASEURL),46,ART+'SourceList.png',FANART,'')
        if ADDON.getSetting('Maintainance')=='true':
            addDir('[COLOR'+TEXTCOL+']MAINTENANCE[/COLOR]',str(BASEURL),3,ART+'Maintenance.png',FANART,'')
#        if ADDON.getSetting('Addons')=='true':
#            addDir('[COLOR'+TEXTCOL+']ADDONS[/COLOR]','',10050,ART+'Addons.png',FANART,'')
#        if ADDON.getSetting('Rss Feed')=='true':
#            addDir('[COLOR'+TEXTCOL+']GenieTv RSS Feed[/COLOR]',str(BASEURL),39,ART+'GenieTVRSSFeed.png',FANART,'')
    setView('movies', 'MAIN')         
def INDEXsimp():
#    addDir('[COLOR'+TEXTCOL+']TEST[/COLOR]','',100110,ART + 'tommys.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']Random Play[/COLOR]','',100108,ART + 'tommys.png',FANART,'')
#    if ADDON.getSetting('My Build')=='true':
#        addDir('[COLOR'+TEXTCOL+']WIZARD[/COLOR]',str(BASEURL),4001,ART+'Wizard.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']FightNight[/COLOR]','',1999990,ART+'GTV.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']G-Tv Live List[/COLOR]','',40099,ART+'GTV.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Tommys Sports[/COLOR]','',90010,ART + 'tommys.png',FANART,'')
    if ADDON.getSetting('Streams')=='true':
        addDir('[COLOR'+TEXTCOL+']STREAMS[/COLOR]',str(BASEURL),4002,ART+'Streams.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']GENIE STORE[/COLOR]','http://genietv.co.uk/store.php',21008,ART+'store.png',FANART,'')
#    if ADDON.getSetting('Music')=='true':
#        addDir('[COLOR'+TEXTCOL+']Music[/COLOR]',str(BASEURL),4003,ART+'Music.png',FANART,'')
#    if Adult_Pass == '5knuckleshuffle':
#        addDir('[COLORorangered]Adult Content[/COLOR]','',19999999,ART+'AG.png',FANART,'')
    if ADDON.getSetting('Maintainance')=='true':
        addDir('[COLOR'+TEXTCOL+']MAINTENANCE[/COLOR]',str(BASEURL),3,ART+'Maintenance.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']TOOLS[/COLOR]','',90001,ART+'png',FANART,'')
    setView('movies', 'MAIN') 
def tools():
	choices = ['[COLOR'+TEXTCOL+']Change Log[/COLOR]','[COLOR'+TEXTCOL+']Force Genie Update Kodi[/COLOR]','[COLOR'+TEXTCOL+']APK TOOL[/COLOR]','[COLOR'+TEXTCOL+']GenieTv RSS Feed[/COLOR]','[COLOR'+TEXTCOL+']CONTACT US[/COLOR]','[COLOR'+TEXTCOL+']OPEN SETTINGS[/COLOR]','[COLOR'+TEXTCOL+']SOURCE LIST[/COLOR]']
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']TOOLS[/COLOR]', choices)
	if choice==0:
		Change_Log2()
	if choice==1:
		Force_Addon_Download()
	if choice==2:
		APKSECTION()
	if choice==3:
		RSS(url)
	if choice==4:
		Dialog.ok(AddonTitle, CONTACT)
	if choice==5:
		ADDON.openSettings(sys.argv[0])
	if choice==6:
		SOURCES()
#--------------COZY CORNER-----------------------------------------------------
def COZY():
    addDir('Stories','http://etc.usf.edu/lit2go/books/',21999995,'http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg','http://www.virtual-fireplace.net/files/theme/fireplace-stories.jpg','')
    addDir('Virtual FirePlaces','http://www.virtual-fireplace.net/fireplaces.html',21999991,'http://www.virtual-fireplace.net/files/theme/burning-log.gif','http://www.virtual-fireplace.net/files/theme/burning-log1.gif','')
    addDir('Nature Sounds','http://www.virtual-fireplace.net/sounds.html',21999993,'http://www.virtual-fireplace.net/files/theme/sound.gif','http://www.virtual-fireplace.net/files/theme/sound-bw.gif','')
def COZYfire1(url):
    HTML = OPEN_URL(url)
    Regex = re.compile('<div><a href="([^"]*)" target="someFrame"><img src="([^"]*)".+?/></a>(.+?)</div>',re.DOTALL).findall(HTML)
    for url,img,name in Regex:
        addDir2(name,url,21999992,'http://www.virtual-fireplace.net/'+img,'http://www.virtual-fireplace.net/'+img,name)
def COZYfire2(url):
    HTML = OPEN_URL(url)
    Regex = re.compile('rel="canonical" href="([^"]*)">',re.DOTALL).findall(HTML)
    for url in Regex:
        url = (url).replace('//www.youtube.com/embed/','').replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=','')
        yt.PlayVideo(url)
def COZYsound1(url):
    addDir('Rain And Thunder','http://www.virtual-fireplace.net/rain-and-thunder.html',21999994,'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg','http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/1556918_orig.jpg','')
    addDir('Water And Forests','http://www.virtual-fireplace.net/water-and-forest.html',21999994,'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg','http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/9341182_orig.jpg','')
    addDir('Beach And Ocean','http://www.virtual-fireplace.net/rain-and-thunder.html',21999994,'http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg','http://www.virtual-fireplace.net/uploads/1/6/2/8/16283378/2924407_orig.jpg','')
def COZYsound2(url,iconimage):
    img = iconimage
    HTML = OPEN_URL(url)
    Regex = re.compile('<h2 class="wsite-content-title".+?">Nature Sounds:(.+?)<br /><.+?src="([^"]*)"',re.DOTALL).findall(HTML)
    for name,url in Regex:
        addDir2(name,'http:'+url,21999992,img,img,'')
def COZYstorie(url):
    HTML = OPEN_URL(url)
    Regex = re.compile('data-src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">.+?<figcaption class="author">.+?<figcaption class="abstract">(.+?)</figcaption>',re.DOTALL).findall(HTML)
    for img,name,url,desc in Regex:
        addDir(name,url,21999996,img,img,(desc).replace('&ldquo;','"').replace('&rdquo;','"').replace('&#8230','').replace('&mdash;','-').replace('&ndash;','-').replace('&quot;','"').replace('&rsquo;','').replace('&#39;','').replace('&quo','').replace('<br />','').replace('<p>','').replace('</p>',''))
def COZYstorie1(url,iconimage):
    img = iconimage
    desc = 'desc'
    HTML = OPEN_URL(url)
    Regex = re.compile('<dt>.+?<a href="([^"]*)">(.+?)</a>.+?<dd(.+?)</dd>',re.DOTALL).findall(HTML)
    for url,name,story in Regex:
        addDir2('[COLOR'+TEXTCOL+']'+name+'[/COLOR] - Audio',url,21999997,img,img,(story).replace('&#8230','').replace('&mdash;','-').replace('&ndash;','-').replace('&quot;','"').replace('&rsquo;','').replace('&#39;','').replace('&quo','').replace('<br />','').replace('<p>','').replace('</p>',''),(story).replace('&#8230','').replace('&mdash;','-').replace('&ndash;','-').replace('&quot;','"').replace('&rsquo;','').replace('&#39;','').replace('&quo','').replace('<br />','').replace('<p>','').replace('</p>',''))
        addDir2('[COLOR'+TEXTCOL+']'+name+'[/COLOR] - Text',url,21999998,img,img,(story).replace('&#8230','').replace('&mdash;','-').replace('&ndash;','-').replace('&quot;','"').replace('&rsquo;','').replace('&#39;','').replace('&quo','').replace('<br />','').replace('<p>','').replace('</p>',''),(story).replace('&#8230','').replace('&mdash;','-').replace('&ndash;','-').replace('&quot;','"').replace('&rsquo;','').replace('&#39;','').replace('&quo','').replace('<br />','').replace('<p>','').replace('</p>',''))
def COZYstorie2(url,iconimage):
    img = iconimage
    HTML = OPEN_URL(url)
    Regex = re.compile('<a href="([^"]*)">Audio</a>').findall(HTML)
    for url in Regex:
        RESOLVEtest(url)
def COZYstorie3(name,url,iconimage):
    img = iconimage
    HTML = OPEN_URL(url)
    Regex = re.compile('</audio>(.+?)</div>',re.DOTALL).findall(HTML)
    for story in Regex:
        TextBox((name).replace(' - Text',''),(story).replace('&ldquo;','"').replace('&rdquo;','"').replace('&#8230','').replace('&mdash;','-').replace('&ndash;','-').replace('&quot;','"').replace('&rsquo;','').replace('&#39;','').replace('&quo','').replace('<br />','').replace('<p>','').replace('</p>',''))

#--------------COZY CORNER END-----------------------------------------------------
def store(url):
    HTML = OPEN_URL(url)
    Regex = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML)
    for url,img,desc,fanart,name in Regex:
        addDir2(name,url,21009,img,fanart,desc)

def store2(url):
	url = url
	myplatform = platform()
	if myplatform() == 'android':
		try:
			xbmc.executebuiltin('StartAndroidActivity(com.android.browser,android.intent.action.VIEW,'+url+')')
		except:
			pass
		else:
			xbmc.executebuiltin('StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,'+url+')')
	elif myplatform() == 'windows':
		webbrowser.open_new(url)


def guideskins():
    url = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("GenieTv","Downloading Awesomeness",'', 'Please Wait')
    lib=os.path.join(path, 'GuideSkins'+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv/resources/skins'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    CLEANUP(url)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "Your skins are now downloaded, Enjoy","[COLOR yellow]Brought To You By GenieTv[/COLOR]")
    UPDATEREPO()
def viewLogFile():
	log     = log_check()
	logtype = log.replace(LOG,"")
	if os.path.exists(log) or not log == False:
		f = open(log,mode='r'); msg = f.read(); f.close()
		TextBox("%s - %s" % (AddonTitle, logtype), msg)
	else: 
		LogNotify('View Log', 'No Log File Found!')
def errorChecking(log=None, count=None, all=None):
	if log == None:
		mainlog = Grab_Log(True)
		oldlog  = Grab_Log(True, True)
		if not oldlog == False and not mainlog == False:
			which = Dialog.select(ADDONTITLE, ["View %s: %s error(s)" % (mainlog.replace(LOG, ""), errorChecking(mainlog, True, True)), "View %s: %s error(s)" % (oldlog.replace(LOG, ""), errorChecking(oldlog, True, True))])
			if which == -1: LogNotify('[COLOR %s]View Log[/COLOR]' % COLOR1, '[COLOR %s]View Log Cancelled![/COLOR]' % COLOR2); return
		elif mainlog == False and oldlog == False:
			LogNotify('[COLOR %s]View Log[/COLOR]' % COLOR1, '[COLOR %s]No Log File Found![/COLOR]' % COLOR2)
			return
		elif not mainlog == False: which = 0
		elif not oldlog == False: which = 1
		log = mainlog if which == 0 else oldlog
	if log == False:
		if count == None:
			LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Log File not Found[/COLOR]" % COLOR2)
			return False
		else: 
			return 0
	else:
		if os.path.exists(log):
			f = open(log,mode='r'); a = f.read().replace('\n', '').replace('\r', ''); f.close()
			match = re.compile("-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--").findall(a)
			if not count == None:
				if all == None: 
					x = 0
					for item in match:
						if ADDON_ID in item: x += 1
					return x
				else: return len(match)
			if len(match) > 0:
				x = 0; msg = ""
				for item in match:
					if all == None and not ADDON_ID in item: continue
					else: 
						x += 1
						msg += "[COLOR red]Error Number %s[/COLOR]\n(PythonToCppException) : -->Python callback/script returned the following error<--%s-->End of Python script error report<--\n\n" % (x, item.replace('                                          ', '\n').replace('\\\\','\\').replace(HOME, ''))
				if x > 0:
					TextBox(ADDONTITLE, msg)
				else: LogNotify(ADDONTITLE, "No Errors Found in Log")
			else: LogNotify(ADDONTITLE, "No Errors Found in Log")
		else: LogNotify(ADDONTITLE, "Log File not Found")
def Grab_Log(file=False, old=False, wizard=False):
	if wizard == True:
		if not os.path.exists(WIZLOG): return False
		else:
			if file == True:
				return WIZLOG
			else:
				filename    = open(WIZLOG, 'r')
				logtext     = filename.read()
				filename.close()
				return logtext
	finalfile   = 0
	logfilepath = os.listdir(LOG)
	logsfound   = []

	for item in logfilepath:
		if old == True and item.endswith('.old.log'): logsfound.append(os.path.join(LOG, item))
		elif old == False and item.endswith('.log') and not item.endswith('.old.log'): logsfound.append(os.path.join(LOG, item))

	if len(logsfound) > 0:
		logsfound.sort(key=lambda f: os.path.getmtime(f))
		if file == True: return logsfound[-1]
		else:
			filename    = open(logsfound[-1], 'r')
			logtext     = filename.read()
			filename.close()
			return logtext
	else: 
		return False

def guideskins():
    url = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("GenieTv","Downloading Awesomeness",'', 'Please Wait')
    lib=os.path.join(path, 'GuideSkins'+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv/resources/skins'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    CLEANUP(url)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "Your skins are now downloaded, Enjoy","[COLOR yellow]Brought To You By GenieTv[/COLOR]")
    UPDATEREPO()
def tommyslist():
        Menu_1('[COLOR'+TEXTCOL+']Todays Games[/COLOR]','',90030,ART+'tgames.png',FANART,'','')
        addDir('[COLOR'+TEXTCOL+']Live Sport On G-Tv[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=')),7080,ART + 'Sport.png',FANART,'')
        addDir('[COLOR'+TEXTCOL+']Tommys Replays[/COLOR]','http://www.replaymatches.com/',900300,ART+'tommysreplays.png',FANART,'')
#        addDir('[COLOR'+TEXTCOL+']Tommys Replays[/COLOR]',str(BASEURL),90031,ART+'tommysreplays.png',FANART,'')
#        addDir('[COLOR'+TEXTCOL+']Premier League Table[/COLOR]','http://www.sportinglife.com/football/premier-league/table',50002,ART + 'PremiereLeague.png',FANART,'')
#        addDir2('[COLOR'+TEXTCOL+']TEST Filmon[/COLOR]','http://www.filmon.tv/tv/channel/export?channel_id=27&affid=223489Mv',222,ART + 'PremiereLeague.png',FANART,'')
def Tgamesnew():
	List = ['Premier League','La Liga','Serie A','Bundesliga','Liguel','UEFA','FIFA']
	html = requests.get(url).content
	match = re.compile("<ul class='shnav simple-mainmenu'>(.+?)</nav>",re.DOTALL).findall(html)
	block = re.compile("<li>.+?href='(.+?)'.+?itemprop='name'>(.+?)<",re.DOTALL).findall(str(match))
	for link, name in block:
		if not name == 'Home':
			pass
			Link = 'http://www.replaymatches.com/'+link
			if name in List:
				addDir('[COLORred]'+name+'[/COLOR]',Link,900301,ART+'tommysreplays.png','','')
			else:
				addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',Link,900301,ART+'tommysreplays.png','','')

'''
    addDir('[COLOR'+TEXTCOL+']our match eng prem[/COLOR]','http://ourmatch.net/videos/england/premier-league-highlights/',900301,ART+'tommysreplays.png','','')
    addDir('[COLOR'+TEXTCOL+']our match la liga[/COLOR]','http://ourmatch.net/videos/spain/la-liga-highlights/',900301,ART+'tommysreplays.png','','')
    addDir('[COLOR'+TEXTCOL+']our match serie a[/COLOR]','http://ourmatch.net/videos/italy/serie-a-highlights/',900301,ART+'tommysreplays.png','','')
    addDir('[COLOR'+TEXTCOL+']our match bund[/COLOR]','http://ourmatch.net/videos/germany/bundesliga-highlights/',900301,ART+'tommysreplays.png','','')
    addDir('[COLOR'+TEXTCOL+']our match ligue 1[/COLOR]','http://ourmatch.net/videos/france/ligue-1-highlights/',900301,ART+'tommysreplays.png','','')
    addDir('[COLOR'+TEXTCOL+']our match uefa champ[/COLOR]','http://ourmatch.net/videos/europe/uefa-champions-league-highlights/',900301,ART+'tommysreplays.png','','')
ART+'tommysreplays.png'     
'''   
def Treplaysnew(url):
    #addDir('[COLOR'+TEXTCOL+']GOAL OF THE MONTH[/COLOR]','http://ourmatch.net/goal-of-the-month/',900302,ART+'tommysreplays.png',ART+'tommysreplays.png','')
    HTML = OPEN_URL(url)
    regex = re.compile("<h2 class='post-title entry-title'>.+?href='(.+?)'.+?title='(.+?)'.+?content='(.+?)'>",re.DOTALL).findall(HTML)
    nxt = re.compile("<a class='blog-pager-older-link'.+?href='(.+?)'").findall(HTML)
    for url,name,img in regex:
        addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,900302,img,ART+'tommysreplays.png','')
    for Next in nxt:
        addDir('[COLOR'+TEXTCOL+']NEXT PAGE[/COLOR]',Next,900301,ART+'NEXT.png','','')
def Tplay(url):
	html = requests.get(url).content
	match = re.compile('<a class="link-iframe".+?href="(.+?)".+?src="(.+?)"',re.DOTALL).findall(html)
	for link, img in match:
		if 'Highlight' in img:
			name = 'HighLights'
		elif '1st' in img:
			name = '1st Half'
		elif '2nd' in img:
			name = '2nd Half'
		Play_1('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',link,1001111,img,ART+'tommysreplays.png','','')
def Tgames():
	html= requests.get(Decode('aHR0cDovL2dlbmlldHYuY28udWsvZm9vdGJhbGw=')).content
	match = re.compile('<div class="entry-content">.+?<h1 class="entry-title">(.+?)</h1>(.+?)<div style="clear:both;"></div>',re.DOTALL).findall(html)
	for INFO, rest in match:
		Menu_1('[COLORred]'+INFO+'[/COLOR]','','',ART+'tommysreplays.png',ART+'tommysreplays.png','','')
		match1 = re.compile("<div style='float.+?<span style=.+?>(.+?)<.+?<img src=\"(.+?)\"",re.DOTALL).findall(str(rest))
		for game,im in match1:
			Menu_1('[COLOR'+TEXTCOL+']'+game+'[/COLOR]','','',im,ART+'tommysreplays.png','','')

'''
def Treplays():
    addDir('[COLOR'+TEXTCOL+']Last Highlight | Football Highlights[/COLOR]',(Decode('aHR0cDovL2xhc3RobC5jb20v')),90032,ART+'tommysreplays.png',FANART,'')
    html=OPEN_URL(Decode('aHR0cDovL2xhc3RobC5jb20v'))
    match = re.compile('menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>',re.DOTALL).findall(html)
    for url,name in match:
        addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,90032,ART+'tommysreplays.png',FANART,'')
def Treplays2(url):
    html=OPEN_URL(url)
    match = re.compile('<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ',re.DOTALL).findall(html)
    next = re.compile('<link rel="next" href="([^"]*)" />',re.DOTALL).findall(html)
    for url,name,img in match:
        addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8211;','-').replace('&#038;','&'),url,90033,img,FANART,'')
    for url in next:
        addDir(('[COLOR'+TEXTCOL+']NEXT[/COLOR]').replace('&#038;','&'),url,90032,ART+'NEXT.png',FANART,'')
def Treplays3(url):
    html=OPEN_URL(url)
    match4 = re.compile('"file":"([^"]*)"',re.DOTALL).findall(html)
    match3 = re.compile('<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"',re.DOTALL).findall(html)
    match2 = re.compile('<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"',re.DOTALL).findall(html)
    match = re.compile('id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"',re.DOTALL).findall(html)
    for name,url in match:
        addDir2(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('pane-0-0','HighLights').replace('pane-0-1','First Half').replace('pane-0-2','Second Half'),'http:'+url,90034,ART+'tommysreplays.png',FANART,'')
    for name,url in match2:
        addDir2(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('pane-0-0','HighLights').replace('pane-0-1','First Half').replace('pane-0-2','Second Half'),'http:'+url,90034,ART+'tommysreplays.png',FANART,'')
    for name,url in match3:
        addDir2(('[COLOR'+TEXTCOL+']Full Show[/COLOR]').replace('pane-0-0','HighLights').replace('pane-0-1','First Half').replace('pane-0-2','Second Half'),'http:'+url,90034,ART+'tommysreplays.png',FANART,'')
    for url in match4:
        addDir2(('[COLOR'+TEXTCOL+']Play[/COLOR]').replace('pane-0-0','HighLights').replace('pane-0-1','First Half').replace('pane-0-2','Second Half'),url,222,ART+'tommysreplays.png',FANART,'')

def Treplays4(url):
    if 'drive' in url:
        RESOLVEtest(url)
    else:
        html=OPEN_URL(url)
        match = re.compile('sources:.+?file:"([^"]*)"').findall(html)
        for url in match:
            RESOLVEtest(url)
'''
def playFilmon(url):
	resolved = liveresolver.resolve(url)
	item     = xbmcgui.ListItem(path=resolved)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
def play_FilmOn_url(url):
    _log("play_resolved_url ["+url+"]")
    listitem = xbmcgui.ListItem(path=url)
    return xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
def log_check():
	ret = False
	if os.path.exists(os.path.join(LOG,'xbmc.log')):
		ret = os.path.join(LOG,'xbmc.log')
	elif os.path.exists(os.path.join(LOG,'kodi.log')):
		ret = os.path.join(LOG,'kodi.log')
	elif os.path.exists(os.path.join(LOG,'spmc.log')):
		ret = os.path.join(LOG,'spmc.log')
	elif os.path.exists(os.path.join(LOG,'tvmc.log')):
		ret = os.path.join(LOG,'tvmc.log')
	return ret

def workingURL(url):
	if url == 'http://': return False
	try: 
		req = urllib2.Request(url)
		req.add_header('User-Agent', USER_AGENT)
		response = urllib2.urlopen(req)
		response.close()
	except Exception, e:
		return e
	return True
'''
def testurls(url)
    test = OPEN_URL(url)
    if not test == True:
'''	
def speedMenu():
	xbmc.executebuiltin('Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")')
def MenWish():
	Repo_Check()
	if ADDON.getSetting('Simplify')=='true':
		choices = ['[COLOR'+TEXTCOL+']BACKUP MY BUILD[/COLOR]','[COLOR'+TEXTCOL+']RESTORE MY BUILD[/COLOR]','[COLOR'+TEXTCOL+']WIPE GENIE[/COLOR]','[COLOR'+TEXTCOL+']Genie BUILDS[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Wizard[/COLOR]', choices)
		if choice==0:
			BackUp_My_Build()
		if choice==1:
			RES()
		if choice==2:
			FRESHSTART(params)
		if choice==3:
			WISHES(url)
	else:
		addDir('[COLOR'+TEXTCOL+']BACKUP MY BUILD[/COLOR]',str(BASEURL),10060,ART+'BackupMyBuild.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']RESTORE MY BUILD[/COLOR]',str(BASEURL),49,ART+'RestoreMyBuild.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']WIPE GENIE[/COLOR]',str(BASEURL),41,ART+'WipeGenie.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']Genie BUILDS[/COLOR]',str(BASEURL),44,ART+'GenieBuilds.png',FANART,'')
	setView('movies', 'MAIN')

def MenStream():
	Repo_Check()
	if ADDON.getSetting('Simplify')=='true':
#		if ADDON.getSetting('Favourites')=='true':
#			addDir('[COLOR'+TEXTCOL+']FAVOURITES[/COLOR]',str(BASEURL),10057,ART+'Favourites.png',FANART,'')
		if ADDON.getSetting('Search')=='true':
			addDir('[COLOR'+TEXTCOL+']SEARCH[/COLOR]',str(BASEURL),9000,ART+'Search.png',FANART,'')
		if ADDON.getSetting('HeroVision')=='true':
			addDir('[COLOR'+TEXTCOL+']APPRENTICE[/COLOR]','',1017,ART+'appstreams.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']TECHNICA STREAMS[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=')),1016,ART+'Technica-Streams.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']PANDORAS BOX[/COLOR]',str(BASEURL),10025,ART+'PandorasBox.png',FANART,'')	
		addDir('[COLOR'+TEXTCOL+']Genie On Demand Streams[/COLOR]',(Decode('aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3NoYWthL0dPRFMucGhw')),1016,ART+'gods.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']Back In Time[/COLOR]','http://genietvcunts.co.uk/bamffff/BAMF.xml',90036,ART+'Bamf.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']BOSS DOCS[/COLOR]',Decode('aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw=='),2032,ART+'boss.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']Supremacy[/COLOR]','',1131000,ART+'supremacy.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']MOVIES[/COLOR]',str(BASEURL),4004,ART+'Movies.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']TV SHOWS[/COLOR]',str(BASEURL),4005,ART+'TVShows.png',FANART,'')
		#addDir('[COLOR'+TEXTCOL+']24/7 STREAMS[/COLOR]','',9050000,ART+'247Streams.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']KIDS[/COLOR]',str(BASEURL),10001,ART+'Kids.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']STREAM CATEGORIES[/COLOR]',str(BASEURL),90002,ART+'cats.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']FREEVIEW[/COLOR]',str(BASEURL),90023,ART+'freeview.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']COMEDY ZONE[/COLOR]',Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA=='),1016,ART+'zone.png',FANART,'')
#		if ADDON.getSetting('Fitness')=='true':
#			addDir('[COLOR'+TEXTCOL+']FITNESS[/COLOR]','',7084,ART+'Fitness.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']STREAM TEAM[/COLOR]',str(BASEURL),4006,ART+'StreamTeam.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']Genie On Demand Series[/COLOR]',(Decode('aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3BsZXgvZG93bmxvYWRzL0cuTy5ELlMvZ29kcy5waHA=')),100210,ART+'gods.png',FANART,'')
	else:
#		if ADDON.getSetting('Favourites')=='true':
#			addDir('[COLOR'+TEXTCOL+']FAVOURITES[/COLOR]',str(BASEURL),10057,ART+'Favourites.png',FANART,'')
		if ADDON.getSetting('Search')=='true':
			addDir('[COLOR'+TEXTCOL+']SEARCH[/COLOR]',str(BASEURL),9000,ART+'Search.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']TECHNICA STREAMS[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=')),1016,ART+'Technica-Streams.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']PANDORAS BOX[/COLOR]',str(BASEURL),10025,ART+'PandorasBox.png',FANART,'')	
		addDir('[COLOR'+TEXTCOL+']Genie On Demand Streams[/COLOR]',(Decode('aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3NoYWthL0dPRFMucGhw')),1016,ART+'gods.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']Back In Time[/COLOR]','http://genietvcunts.co.uk/bamffff/BAMF.xml',90036,ART+'Bamf.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']Supremacy[/COLOR]','',1131000,ART+'supremacy.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']BOSS DOCS[/COLOR]',Decode('aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw=='),2032,ART+'boss.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']APPRENTICE[/COLOR]','',1017,ART+'appstreams.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']MOVIES[/COLOR]',str(BASEURL),4004,ART+'Movies.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']TV SHOWS[/COLOR]',str(BASEURL),4005,ART+'TVShows.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']KIDS[/COLOR]',str(BASEURL),10001,ART+'Kids.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']COZY CORNER[/COLOR]',Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA=='),21999990,ART+'zone.png',FANART,'')
#		if ADDON.getSetting('Football')=='true':
#			addDir('[COLOR'+TEXTCOL+']FOOTBALL[/COLOR]','',10002,ART+'Football.png',FANART,'')
		#addDir('[COLOR'+TEXTCOL+']24/7 STREAMS[/COLOR]','',9050000,ART+'247Streams.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']COMEDY ZONE[/COLOR]',Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA=='),1016,ART+'zone.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']FREEVIEW[/COLOR]',str(BASEURL),90023,ART+'freeview.png',FANART,'')
#		if ADDON.getSetting('Fitness')=='true':
#			addDir('[COLOR'+TEXTCOL+']FITNESS[/COLOR]','',7084,ART+'Fitness.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']STREAM TEAM[/COLOR]',str(BASEURL),4006,ART+'StreamTeam.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']Genie On Demand Series[/COLOR]',(Decode('aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L3BsZXgvZG93bmxvYWRzL0cuTy5ELlMvZ29kcy5waHA=')),100210,ART+'gods.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']NEWS[/COLOR]',str(BASEURL),30032,ART+'News.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']HOBBIES[/COLOR]',str(BASEURL),4008,ART+'Hobbies.png',FANART,'')
#		if ADDON.getSetting('Documentaries')=='true':
#			addDir('[COLOR'+TEXTCOL+']DOCUMENTARIES[/COLOR]',str(BASEURL),8040,ART+'documentaries.png',FANART,'')
#		if ADDON.getSetting('Disclose')=='true':
#			addDir('[COLOR'+TEXTCOL+']DISCLOSE TV[/COLOR]',str(BASEURL),7001,ART+'DiscloseTV.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']24/7 STREAMS[/COLOR]','',30030,ART+'247Streams.png',FANART,'')
#		if ADDON.getSetting('TV GUIDE')=='true':
#			addDir2('[COLOR'+TEXTCOL+']TV GUIDE[/COLOR]','',10063,ART+'TvGuide.png',FANART,'')
#		if ADDON.getSetting('CLASSICS')=='true':
#			addDir('[COLOR'+TEXTCOL+']CLASSICS[/COLOR]',str(BASEURL),3001,ART+'loader.png',FANART,'')
#    if ADDON.getSetting('Playlist Loader')=='true':
#        addDir('[COLOR'+TEXTCOL+']PLAYLIST LOADER[/COLOR]',str(BASEURL),3000,ART+'PlaylistLoader.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']The Channel List[/COLOR]','',50001,ART+'TvGuide.png',FANART,'')
#    if ADDON.getSetting('M3u Streams')=='true':
#        addDir('[COLOR'+TEXTCOL+']M3U STREAMS[/COLOR]',BASEURL+'/m3ustreams/UKTV.m3u',8071,ART+'streams.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']KISS CARTOONS[/COLOR]',str(BASEURL),20000,ART+'anime.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']Origin[/COLOR]','',10000,ART + 'ORIGIN.png',FANART,'')	
#    addDir('[COLOR'+TEXTCOL+']EPG[/COLOR]',str(BASEURL),1014,ART+'vod.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']SCRAPED IPTV[/COLOR]',(Decode('aHR0cDovL2lwdHYuZmlsbW92ZXIuY29tLw==')),9030,ART+'streams.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']SOAPS CATCH UP[/COLOR]',str(BASEURL),8000,ART+'soaps.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']STREAMS[/COLOR]',str(BASEURL),1008,ART+'streams.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']IZLE FILMS[/COLOR]','',10030,ART+'IZLEFILMS.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']CHAMPION IPTV[/COLOR]',str(BASEURL),9020,ART+'UKiptvandvod.png',FANART,'UK IPTV AND HD VOD')
#    addDir('[COLOR'+TEXTCOL+']Genie Vision[/COLOR]','',10072,ART+'genievision.png',FANART,'')
	setView('movies', 'MAIN')
def streamcats():
	choices = ['[COLOR'+TEXTCOL+']FOOTBALL[/COLOR]','[COLOR'+TEXTCOL+']KIDS[/COLOR]','[COLOR'+TEXTCOL+']NEWS[/COLOR]','[COLOR'+TEXTCOL+']HOBBIES[/COLOR]','[COLOR'+TEXTCOL+']DOCUMENTARIES[/COLOR]','[COLOR'+TEXTCOL+']DISCLOSE TV[/COLOR]']
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']CATEGORIES[/COLOR]', choices)
	if choice==0:
		Origin_Football()
	if choice==1:
		MenStreamkids()
	if choice==2:
		ARCONAI3()
	if choice==3:
		MenStreamhob()
	if choice==4:
		DOC1()
	if choice==5:
		cnfTV()
		
	
def MenStreammov():
	Repo_Check()
	if ADDON.getSetting('Simplify')=='true':
		choices = ['[COLOR'+TEXTCOL+']SEARCH MOVIES[/COLOR]','[COLOR'+TEXTCOL+']TOP RATED MOVIES[/COLOR]','[COLOR'+TEXTCOL+']DESI FLIX[/COLOR]','[COLOR'+TEXTCOL+']FILM TRAILERS[/COLOR]','[COLOR'+TEXTCOL+']CLASSIC MOVIES[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']MOVIES[/COLOR]', choices)
		if choice==0:
			Search_Films_Lists()
		if choice==1:
			RT1()
		if choice==2:
			MOVnew()
		if choice==3:
			Film_Trailers(Decode('aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl'))
		if choice==4:
			classic_TV()
	else:
		addDir('[COLOR'+TEXTCOL+']SEARCH MOVIES[/COLOR]',str(BASEURL),9001,ART+'Search.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']TOP RATED MOVIES[/COLOR]',str(BASEURL),10200,ART+'rated.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']Desi Flix[/COLOR]','',80005,ART+'Desi.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']Film Trailers[/COLOR]',Decode('aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl'),10068,ART+'FilmTrailers.png',FANART,'')
		if ADDON.getSetting('CLASSIC MOVIES')=='true':
			addDir('[COLOR'+TEXTCOL+']CLASSIC MOVIES[/COLOR]','',8060,ART+'ClassicMovies.png',FANART,'')
	setView('movies', 'MAIN')
def IPTVMENU():
    addDir('[COLOR'+TEXTCOL+']DAILY LISTS[/COLOR]','',9007,ICON,FANART,'')
    addDir('[COLOR'+TEXTCOL+']WEB LISTS[/COLOR]','http://iptvsatlinks.blogspot.co.uk/',9030,ICON,FANART,'')
#    addDir('[COLOR'+TEXTCOL+']Find Me A Stream[/COLOR]','',9003,ART + 'Sport.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']World IPTV[/COLOR]','',9004,ART + 'Sport.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']Iptv Lists[/COLOR]','',9010,ART + 'Sport.png',FANART,'')

	
def MenStreamtv():
	Repo_Check()
	if ADDON.getSetting('Simplify')=='true':
		choices = ['[COLOR'+TEXTCOL+']SEARCH SERIES[/COLOR]','[COLOR'+TEXTCOL+']Dans Scrapes[/COLOR]','[COLOR'+TEXTCOL+']THE SOURCE[/COLOR]','[COLOR'+TEXTCOL+']RETURN DATES[/COLOR]','[COLOR'+TEXTCOL+']CLASSIC TV[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']TV SHOWS[/COLOR]', choices)
		if choice==0:
			Search_Tv_Lists()
		if choice==1:
			show_main('http://www.tvmaze.com/shows')
		if choice==2:
			Home_Menu_Episodes()
		if choice==3:
			RD1()
		if choice==4:
			classic_TVshows()
	else:
		addDir('[COLOR'+TEXTCOL+']SEARCH SERIES[/COLOR]',str(BASEURL),9002,ART+'Search.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']Dans Scrapes[/COLOR]','http://www.tvmaze.com/shows',9110001,ART+'ClassicTV.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']RETURN DATES[/COLOR]',str(BASEURL),10095,ART+'RD.png',FANART,'')
		if ADDON.getSetting('CLASSIC TV')=='true':
			addDir('[COLOR'+TEXTCOL+']CLASSIC TV[/COLOR]',str(BASEURL),8064,ART+'ClassicTV.png',FANART,'')
	setView('movies', 'MAIN')
def MenStreamteam():
	Repo_Check()
	if ADDON.getSetting('Simplify')=='true':
		if ADDON.getSetting('Pandoras Box')=='true':
			pan = '[COLOR'+TEXTCOL+']Murrays Mints[/COLOR]'
#		if ADDON.getSetting('Scooby Streams')=='true':
#			scoob = '[COLOR'+TEXTCOL+']SCOOBY STREAMS[/COLOR]'
		#if ADDON.getSetting('HeroVision')=='true':
			#hero = '[COLOR'+TEXTCOL+']APPRENTICE[/COLOR]'
		choices = [pan,'[COLOR'+TEXTCOL+']TECHNICA STREAMS[/COLOR]','[COLOR'+TEXTCOL+']BAMF TV[/COLOR]','[COLOR'+TEXTCOL+']PIRATE MOVIES[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']StreamTeam[/COLOR]', choices)
		if choice==0:
			Pand_Home_Menu()
		if choice==1:
			HEROVISION()
		if choice==2:
			BAMFTV((Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s')))
		if choice==3:
			REAPER((Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=')),iconimage,name)
	else:
#		if ADDON.getSetting('The Reaper')=='true':
#			addDir('[COLOR'+TEXTCOL+']THE REAPER[/COLOR]',(Decode('aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvbWFpbm1lbnUucGhw')),90037,ART+'TheReaper.png',FANART,'')
		if ADDON.getSetting('Pandoras Box')=='true':
			addDir('[COLOR'+TEXTCOL+']Murrays Mints[/COLOR]',str(BASEURL),10025,ART+'PandorasBox.png',FANART,'')	
		addDir('[COLOR'+TEXTCOL+']TECHNICA STREAMS[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=')),1016,ART+'Technica-Streams.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']ROADRUNNER STREAMS[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw')),1016,ART+'Roadrunner-Streams.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']RAIZ TV[/COLOR]',(Decode('aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0')),90037,ART+'raiztv.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']SUPREMACY[/COLOR]',(Decode('aHR0cDovL3N0ZXBoZW4tYnVpbGRzLnVrL3N1cHJlbWFjeS9ob21lLnR4dA==')),900377,ART+'raiztv.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']BAMF TV[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s')),1018,ART+'bamftv.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']PIRATE MOVIES[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=')),1016,ART+'pirate.png',FANART,'')
		#if ADDON.getSetting('HeroVision')=='true':
			#addDir('[COLOR'+TEXTCOL+']APPRENTICE[/COLOR]','',1017,ART+'appstreams.png',FANART,'')
#		if ADDON.getSetting('Scooby Streams')=='true':
#			addDir('[COLOR'+TEXTCOL+']SCOOBY STREAMS[/COLOR]',str(BASEURL),1023,ART+'ScoobyStreams.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']ITV[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==')),1016,ART+'ITVStreams.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']Test[/COLOR]',(Decode('aHR0cDovL2dlbmlldHYuY28udWsvdGVzdC5waHA=')),1016,(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9pdHZzdHJlYW1zLnBuZw==')),FANART,'')
	setView('movies', 'MAIN')
	
def MenSilentHunter():
    Repo_Check()
    addDir2('[COLOR'+TEXTCOL+']SILENT HUNTER[/COLOR]',(Decode('aHR0cDovLzUuMTM1LjIwNy45Ni8=')),1006,ART+'SilentHunter.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']SERVER 1[/COLOR]',(Decode('aHR0cDovLzUuMTM1LjIwNy45Ni8=')),1018,ART+'SilentHunter.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']SERVER 2[/COLOR]',(Decode('aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==')),1018,ART+'SilentHunter.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']SCRAPES[/COLOR]',(Decode('aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw')),1016,ART+'SilentHunter.png',FANART,'')
def BAMFTV(url):
    html=OPEN_URL(url)
    block = re.compile('<item>(.+?)</item>',re.DOTALL).findall(html)
    match = re.compile('<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>',re.DOTALL).findall(str(block))
    match2 = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>',re.DOTALL).findall(str(block))
    match3 = re.compile('<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>',re.DOTALL).findall(str(block))
    for name,img,url in match:
        if '247ch' in url:
            addDir3(name,url,10190,img)
        elif '.m3u' in url:
            addDir3(name,url,1019,img)
        elif '.xml' in url:
            addDir3(name,url,1018,img)
        else:
            addDir4(name,url,222,img)
    for name,url,img in match2:
        if '.xml' in url:
            addDir3(name,url,1018,img)
        elif '.m3u' in url:
            addDir3(name,url,1019,img)
        else:
            addDir4(name,url,222,img)
    for name,url,img in match3:
        addDir4(name,url,8043,img)
def Get_BAMF_playlinks(url):
    HTML = OPEN_CAT(url)
    match = re.compile('EXTINF:.+?,(.+?)\n(.+?)\n#',re.DOTALL).findall(HTML)
    for name,url in match:
        addDir4('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,222,ART+'BAMFTV.png')
def Get_BAMF247_playlinks(url):
    HTML = OPEN_CAT(url)
    match = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>',re.DOTALL).findall(HTML)
    for name,url,img in match:
        addDir4('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,222,img)

def HEROVISION():
    #addDir('[COLOR'+TEXTCOL+']APPRENTICE[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==')),1016,ART+'appstreams.png',FANART,'')
    Menu_1('[COLOR'+TEXTCOL+']All Movies[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==')),9110013,ART+'scraped.png',FANART,'','')
    Menu_1('[COLOR'+TEXTCOL+']Movies By Genre[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=')),9110013,ART+'scraped.png',FANART,'','')
    Menu_1('[COLOR'+TEXTCOL+']Movies By A - Z[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==')),9110013,ART+'scraped.png',FANART,'','')
    Menu_1('[COLOR'+TEXTCOL+']Search[/COLOR]','',9110015,ART+'Search.png',FANART,'','')
    #addDir('[COLORred]****[/COLOR][COLOR'+TEXTCOL+']Newly Added Magic[/COLOR][COLORred]****[/COLOR]',(Decode('aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw')),100004,ART+'newaddmagic.png',FANART,'')
    #addDir('[COLOR'+TEXTCOL+']Sitcoms[/COLOR]',(Decode('aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=')),100010,ART+'newaddsit.png',FANART,'')
    #addDir('[COLORred]****[/COLOR][COLOR'+TEXTCOL+']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]',(Decode('aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw')),100010,ART+'newaddsit.png',FANART,'')
#----------------dans additions -------------------------------------------------------------
def reg_nan(url):
    html = requests.get(url).text
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>',re.DOTALL).findall(html)
    for title, mode,sub, im, plot, year,fanart in match:
        if fanart == ' ':
            fanart = FANART
        if im == ' ':
            im = ICON
        plot = plot.replace('\\n',' ')
        if mode == 'Movie Search':
            Play_1(title,year,9110014,im,fanart,plot,'')
        elif mode == 'Menu':
            Menu_1(title,sub,9110013,im,fanart,plot,'')

def send_to_movie_search_pyramid(name,url):
    from imports import Scrape_Nan
    name = str(name)
    year = str(url)
    dp =  xbmcgui.DialogProgress()
    dp.create('Checking for stream')
    Scrape_Nan.scrape_movie(name,year,'')

def nanmovsearch():
    Dialog = xbmcgui.Dialog()
    Search_Name = Dialog.input('Search your moive', type=xbmcgui.INPUT_ALPHANUM)
    List = ['aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9mdWxsLnR4dA==','aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9HZW5yZS9HZW5yZS50eHQ=','aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL21vdmllcy9BLVovQS1aLnR4dA==']
    for url in List:
        html = requests.get(Decode(url)).content
        match = re.compile('<item>.+?<title>(.+?)</title>.+?<link>(.+?)</link>.+?<sublink>(.+?)</sublink>.+?<thumbnail>(.+?)</thumbnail>.+?<plot>(.+?)</plot>.+?<year>(.+?)</year>.+?<fanart>(.+?)</fanart>.+?</item>',re.DOTALL).findall(html)
        for title, mode,sub, im, plot, year,fanart in match:
            if fanart == ' ':
                fanart = FANART
            if im == ' ':
                im = ICON
            plot = plot.replace('\\n',' ')
            if mode == 'Movie Search':
                if Search_Name.lower() in title.lower():
                    Play_1(title,year,9110014,im,fanart,plot,'')
def Regex_com(url):
    HTML = OPEN_URL_1(url)
    match = re.compile('<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"').findall(HTML)
    for name,url,mode,image,fanart,desc in match:
        if image == '123':
            image = ART+'appstreams.png'
        if fanart == '123':
            fanart = ART+'appstreams.png'
        if 'php' in url:
            addDir(name,url,100010,image,fanart,desc)
        elif 'playlist' in url:
            addDir(name,url,100007,image,fanart,desc)
        elif 'watchseries' in url:
            addDir(name,url,100100,image,fanart,desc)
        elif not 'http' in url:
            Play_1(name,url,100009,image,fanart,desc,'')
        else:
            Play_1(name,url,100005,image,fanart,desc,'')

def Regex_magic(url):
    HTML = OPEN_URL_1(url)
    Regex = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML)
    for url,img,desc,fanart,name in Regex:
        if img == '123':
            img = ART+'appstreams.png'
        if fanart == '123':
            fanart = FANART
        if 'php' in url:
            addDir(name,url,100004,img,fanart,desc)
        elif 'playlist' in url:
            addDir(name,url,100007,img,fanart,desc)
        elif 'watchseries' in url:
            addDir(name,url,100100,img,fanart,desc)
        elif not 'http' in url:
            Play_1(name,url,100009,img,fanart,desc,'')
        else:
            Play_1(name,url,100005,img,fanart,desc,'')

def grab_youtube_playlist(url):

    HTML = OPEN_URL_1(url)
    block_set = re.compile('<tr class="pl-video yt-uix-tile(.+?)</tr>',re.DOTALL).findall(HTML)
    for block in block_set:
        image = re.compile('data-thumb="(.+?)"').findall(str(block))
        for image in image:
            image = image
        name = re.compile('data-title="(.+?)"').findall(str(block))
        for name in name:
            if 'elete' in name:
                pass
            elif 'rivate Vid' in name:
                pass
            else:
    			name = (name).replace('&quot;','').replace('&#39;','\'').replace('&amp;','&')
        duration = re.compile('<div class="timestamp"><span aria-label=".+?">(.+?)</span>').findall(str(block))
        for duration in duration:
            duration = duration
        url = re.compile('data-video-ids="(.+?)"').findall(str(block))
        for url in url:
            url = url
        Play_1('[COLORred]'+str(duration)+'[/COLOR] : '+str(name),str(url),100009,str(image),FANART,'','' )
        setView('movies', '')
###################################tv shows dan###################################
def nantvsearch():
	Search_Name = Dialog.input('Search Dans Scrapes', type=xbmcgui.INPUT_ALPHANUM)
	Search_Clean_Name = 'http://www.tvmaze.com/search?q='+(Search_Name).replace(' ','+')
	Search_Title = Search_Clean_Name.lower()
	HTML = OPEN_URL(Search_Title)
	match = re.compile('<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>',re.DOTALL).findall(HTML)
	for url, img, name in match:
		url2 = 'http://www.tvmaze.com'+url.replace('"','')
		html2 = requests.get(url2).content
		match = re.compile('<article>.+?<p>(.+?)</p>',re.DOTALL).findall(html2)
		for desc in match:
			if not '<div>' in desc:
				des = desc.replace('<b>','').replace('</b>','').replace('<i>','').replace('</i>','')
			img = 'http:'+img
			name = name.replace('&#039;','')
			if name == '':
				get = re.compile('/shows/.+?/([^"]*)"').findall(str(url))
				for name in get:
					name = name.replace('-',' ')
		Menu_1(name,url2,9110002,img,FANART,des,'')
###################################tv shows dan###################################
def show_main(url):
    addDir3('[COLORsteelblue]SEARCH[/COLOR]','',9110004,ART+'Search.png',FANART,'')
    html = requests.get(url).content
    match = re.compile('<figure class="image small-12 cell">.+?href="([^>]*)><img src="([^"]*)" alt="([^"]*)"></a>',re.DOTALL).findall(html)
    Next = re.compile('<li class="next"><a href="(.+?)"').findall(html)
    for url, img, name in match:
        url2 = 'http://www.tvmaze.com'+url.replace('"','')
        #Menu_1(url2,'',9110002,img,FANART,name,'')
        html2 = requests.get(url2).content
        match = re.compile('<article>.+?<p>(.+?)</p>',re.DOTALL).findall(html2)
        for desc in match:
            if not '<div>' in desc:
                des = desc.replace('<b>','').replace('</b>','').replace('<i>','').replace('</i>','')
            img = 'http:'+img
            name = name.replace('&#039;','').replace('&amp;','&')
            if name == '':
                get = re.compile('/shows/.+?/([^"]*)"').findall(str(url))
                for name in get:
                    name = name.replace('-',' ').replace('&#039;','').replace('&amp;','&')
        Menu_1(name,url2,9110002,img,FANART,des,'')

    for nxt in Next:
        url = 'http://www.tvmaze.com'+nxt
        Menu_1('NEXT',url,9110001,img,FANART,'','')
def get_desc(url):
	html = requests.get(url).content
	match = re.compile('<article>.+?<p>(.+?)</p>',re.DOTALL).findall(html)
	for desc in match:
		des = desc.replace('<b>','').replace('</b>','')
	return des
def get_eps(url,name,iconimage):
    title = name.replace('&#039;','').replace('&amp;','&')
    img = iconimage
    html = requests.get(url+'/episodes').content
    html2 = requests.get(url).content
    block = re.compile("<h2 data-magellan-target='(.+?)'.+?<tbody>(.+?)</tbody>",re.DOTALL).findall(html)
    match = re.compile('<span id="year">\((.+?)-',re.DOTALL).findall(html2)
    for show_year in match:
        show_year = show_year.replace(' ','')   
    for seas , rest in block:
        if not 'special' in seas.lower():
            seas = seas.replace('S','').replace('s','')
        eps = re.compile('<tr data-key=".+?"><td>(.+?)</td><td>.+?,(.+?)</td>.+?href=".+?">(.+?)</a>',re.DOTALL).findall(str(rest))
        for ep, ep_year, ep_name in eps:
            if not 'special' in ep.lower():
                Menu_1(title+' - SEASON -'+seas+'- EPISODE-'+ep+'-'+show_year,'',9110003,img,FANART,'',title)
				
				
				
def send_to_search2(name,extra):
    #xbmc.log('name:'+(str(extra)),xbmc.LOGNOTICE)
    dp =  xbmcgui.DialogProgress()
    dp.create('Checking for stream')
    from imports import Scrape_Nan
    name_splitter = name + '<>'
    name_split = re.compile('(.+?)- SEASON -(.+?)- EPISODE-(.+?)-(.+?)<>').findall(str(name_splitter))
    for title,season,episode,show_year in name_split:
        title = title
        season = season
        episode = episode
        tvdb = ''
        Scrape_Nan.scrape_episode(title,show_year,'',season,episode,'')

'''		
def movie_search(description,extra):
	#xbmc.log('title:'+title+'# year:'+year,xbmc.LOGNOTICE)
	year = (str(description))
	title = (str(extra))
	xbmc.log('title:'+title+'# year:'+year,xbmc.LOGNOTICE)
	from imports import Scrape_Nan
	Scrape_Nan.scrape_movie(title,year,'')
'''

def ac247():
    Menu_1('Featured 24/7','',9070000,ART+'arconai/feat.png',FANART,'','')
    Menu_1('24/7 Tv Thows','',9080000,ART+'arconai/247shows.png',FANART,'','')
    Menu_1('24/7 Movies','',9090000,ART+'arconai/247movies.png',FANART,'','')
    Menu_1('24/7 Cable','',9100000,ART+'arconai/247cable.png',FANART,'','')
    Menu_1('24/7 Random Stream','',9110000,ART+'arconai/random.png',FANART,'','')

def actvshows():
    url = 'http://arconaitv.me/'
    index = 'index.php#shows'
    html = BeautifulSoup(requests.get(url+index).content)
    conts = html.findAll('div', attrs= {'class':'stream-nav shows'})
    for cont in conts:
        links = cont.findAll('div', attrs= {'class':'stream-initial'})
        for link in links:
            inis = link.text
        links2 = cont.findAll('a')
        for link in links2:
            if link.has_key('href'):
                href = url+link['href']
            if link.has_key('title'):
                name = link['title']
            heads = {'User-Agent': random_agent()}
            html3 = requests.get(href,headers=heads).content
            pp = packets(html3)

            match = re.compile("'https:(.+?)'").findall(pp)
            for plink in match:
                plink = plink.replace('\\','').replace('m3u8/','m3u8')
                src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
                Play_1(name, src ,9060000,ART+'247Streams.png',FANART,'','')


def actvmovies():
    url = 'http://arconaitv.me/'
    index = 'index.php#movies'
    html = BeautifulSoup(requests.get(url+index).content)
    conts = html.findAll('div', attrs= {'class':'stream-nav movies'})
    for cont in conts:
        links = cont.findAll('div', attrs= {'class':'stream-initial'})
        for link in links:
            inis = link.text
        links2 = cont.findAll('a')
        for link in links2:
            if link.has_key('href'):
                href = url+link['href']
            if link.has_key('title'):
                name = link['title']
            heads = {'User-Agent': random_agent()}
            html3 = requests.get(href,headers=heads).content
            pp = packets(html3)

            match = re.compile("'https:(.+?)'").findall(pp)
            for plink in match:
                plink = plink.replace('\\','').replace('m3u8/','m3u8')
                src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
                Play_1(name, src ,9060000,ART+'247Streams.png',FANART,'','')
            

def actvcable():
    url = 'http://arconaitv.me/'
    index = 'index.php#cable'
    html = BeautifulSoup(requests.get(url+index).content)
    conts = html.findAll('div', attrs= {'class':'stream-nav cable'})
    for cont in conts:
        links = cont.findAll('div', attrs= {'class':'stream-initial'})
        for link in links:
            inis = link.text
        links2 = cont.findAll('a')
        for link in links2:
            if link.has_key('href'):
                href = url+link['href']
            if link.has_key('title'):
                name = link['title']
            heads = {'User-Agent': random_agent()}
            html3 = requests.get(href,headers=heads).content
            pp = packets(html3)

            match = re.compile("'https:(.+?)'").findall(pp)
            for plink in match:
                plink = plink.replace('\\','').replace('m3u8/','m3u8')
                src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
                Play_1(name, src ,9060000,ART+'247Streams.png',FANART,'','')

def actvrand():
    html2 = 'http://arconaitv.me/stream.php?id=random'
    heads = {'User-Agent': random_agent()}
    html3 = requests.get(html2,headers=heads).content
    pp = packets(html3)

    match = re.compile("'https:(.+?)'").findall(pp)
    for plink in match:
        plink = plink.replace('\\','').replace('m3u8/','m3u8')
        src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
        Play_1('Random Pick', src ,9060000,ART+'247Streams.png',FANART,'','')

def arcontv():
    url = 'http://arconaitv.me/'
    index = 'index.php#shows'

    html = BeautifulSoup(requests.get(url+index).content)
    conts = html.findAll('div', attrs= {'class':'box-content'})
    for cont in conts:
        links = cont.findAll('a')
        for link in links:
            if link.has_key('href'):
                href = url+link['href']
            if link.has_key('title'):
                name = link['title']
            pics = link.findAll('img')
            for pic in pics:
                img = url+pic['src']
                heads = {'User-Agent': random_agent()}
                html3 = requests.get(href,headers=heads).content
                pp = packets(html3)

                match = re.compile("'https:(.+?)'").findall(pp)
                for plink in match:
                    plink = plink.replace('\\','').replace('m3u8/','m3u8')
                    src = 'https:'+plink+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
                    Play_1(name, src ,9060000,img,img,'','')

def Big_Resolve(name,url):
    import urlresolver
    try:
        resolved_url = urlresolver.resolve(url)
        xbmc.Player().play(resolved_url, xbmcgui.ListItem(name))
    except:
        xbmc.Player().play(url, xbmcgui.ListItem(name))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
	
########################### G.O.D.S ##########################################
def GODS(url):
    HTML = OPEN_URL(url)
    Regex = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>').findall(HTML)
    for url,img,desc,fanart,name in Regex:
        if '.php' in url:
		    addDir(name,url,100210,img,fanart,desc)
        else:
            addDir2(name,url,222,img,fanart,desc)

###########################Watch series Grab##########################################

def Grab_Season(iconimage,url,extra):
    image = ' '
    description = ' '
    fanart = ' '
    season = ' '
    OPEN = OPEN_URL_1(url)
    image = re.compile('<img src="(.+?)">').findall(OPEN)
    for image in image:
        image = image
    background = re.compile('style="background-image: url\((.+?)\)">').findall(OPEN)
    for fanart in background:
        fanart = fanart	
    match = re.compile('itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>',re.DOTALL).findall(OPEN)
    for url,season in match:
        season = 'S'+(season).replace('  ','').replace('\n','').replace('    ','').replace('	','')
        url = Main + url
        Menu_1((season).replace('  ',''),url,100101,image,fanart,description,'')
        setView('Movies', 'info')
	
def Grab_Episode(url,name,fanart,extra,iconimage):
    main_name = extra 
    season = name
    OPEN = OPEN_URL_1(url)
    image = iconimage
    match = re.compile('<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>',re.DOTALL).findall(OPEN)
    for url,name,date in match:
        name = (name).replace('&nbsp;','-').replace('---',' - ').replace('&#039;','\'').replace('&amp;','&').replace('&quot;','"')
        url = Main+url
        date = date
        full_name = name+' - [COLORred]'+date+'[/COLOR]'
        Menu_1(full_name,url,100102,image,fanart,'Aired : '+date,full_name)

def Get_Sources(name,URL,iconimage,fanart):
    HTML = OPEN_URL_1(URL)
    match = re.compile('<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n',re.DOTALL).findall(HTML)
    for url,name in match:
        for item in Sources:
            if item in url:
                URL = 'http://www.watchseriesgo.to/link/' + url
                Play_1(name,URL,100106,ART+'appstreams.png',FANART,'','')
    if len(match)<=0:
        Menu_1('[COLORred]NO STREAMS AVAILABLE[/COLOR]','','','','','','')
		
		
def Get_site_link(url,name):
    season_name = name
    HTML = OPEN_URL_1(url)
    match = re.compile('<iframe style=.+?" src="(.+?)"').findall(HTML)
    match2 = re.compile('<IFRAME SRC="(.+?)"').findall(HTML)
    match3 = re.compile('<IFRAME style=".+?" SRC="(.+?)"').findall(HTML)
    for url in match:
        main_1(url,season_name)
    for url in match2:
        main_1(url,season_name)
    for url in match3:
        main_1(url,season_name)

def main_1(url,season_name):
    if 'daclips.in' in url:
        daclips_1(url,season_name)
    elif 'filehoot.com' in url:
        filehoot_1(url,season_name)
    elif 'allmyvideos.net' in url:
        allmyvid_1(url,season_name)
    elif 'vidspot.net' in url:
        vidspot_1(url,season_name)
    elif 'vodlocker' in url:
        vodlocker_1(url,season_name)	
    elif 'vidto' in url:
        vidto_1(url,season_name)	


def vidto_1(url,season_name):
    HTML = OPEN_URL_1(url)
    match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"',re.DOTALL).findall(HTML)
    for Link,name in match:
        Printer_1(Link,season_name)

												
def allmyvid_1(url,season_name):
    HTML = OPEN_URL_1(url)
    match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"',re.DOTALL).findall(HTML)
    for Link,name in match:
        Printer_1(Link,season_name)

def vidspot_1(url,season_name):
    HTML = OPEN_URL_1(url)
    match = re.compile('"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"').findall(HTML)
    for Link,name in match:
        Printer_1(Link,season_name)

def vodlocker_1(url,season_name):
    HTML = OPEN_URL_1(url)
    match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
    for Link in match:
        Printer_1(Link,season_name)

def daclips_1(url,season_name):
    HTML = OPEN_URL_1(url)
    match = re.compile('{ file: "(.+?)", type:"video" }').findall(HTML)
    for Link in match:
        Printer_1(Link,season_name)

def filehoot_1(url,season_name):
    HTML = OPEN_URL_1(url)
    match = re.compile('file: "(.+?)",.+?skin',re.DOTALL).findall(HTML)
    for Link in match:
        Printer_1(Link,season_name)

def Printer_1(Link,season_name):
    if 'http:/' in Link:
        Resolve_2(Link)

#--------------menus and paly-----------------------------------------------------
def Play_Stage(url):
    HTML = OPEN_URL_1(url)
    playlink = re.compile("url\[.+?\] = '(.+?)';").findall(HTML)
    for url in playlink:
        Resolve_2((url).replace('[','').replace(']','').replace('\'',''))

def Menu_1(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

		
def Play_1(name,url,mode,iconimage,fanart,description,extra,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=100107)' % sys.argv[0]))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def queueItem():
    return xbmc.executebuiltin('Action(Queue)')
	
def RESOLVE_1(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    url = (url).strip()
    try: play.play(url).strip()
    except: pass

def Resolve_2(url): 
    play=xbmc.Player()
    import urlresolver
    try: play.play(url)
    except: pass

def OPEN_URL_1(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = ''
    link = ''
    try: 
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    except: pass
    if link != '':
        return link
    else:
        link = 'Opened'
        return link
#----------------dans additions end-------------------------------------------------------------


def MenStreamkids():
	Repo_Check()
	if ADDON.getSetting('Simplify')=='true':
		choices = ['[COLOR'+TEXTCOL+']CARTOONS[/COLOR]']
		#choices = ['[COLOR'+TEXTCOL+']SEARCH CARTOONS[/COLOR]','[COLOR'+TEXTCOL+']WATCH CARTOONS ONLINE[/COLOR]','[COLOR'+TEXTCOL+']CARTOONS[/COLOR]','[COLOR'+TEXTCOL+']MORE CARTOONS[/COLOR]','[COLOR'+TEXTCOL+']ANIME LAND[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Kids[/COLOR]', choices)
		#if choice==0:
			#Origin_Cart_Search()
		#if choice==1:
			#WCO_CATS()
		if choice==0:
			Origin_cartoons()
		#if choice==3:
			#KISS_CATS()
		#if choice==4:
			#Origin_Cart((Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==')))
	else:
		#addDir('[COLOR'+TEXTCOL+']SEARCH CARTOONS[/COLOR]','',10005,ART + 'SearchCartoons.png',FANART,'')
		#if ADDON.getSetting('WCO')=='true':
			#addDir('[COLOR'+TEXTCOL+']WATCH CARTOONS ONLINE[/COLOR]',str(BASEURL),21004,ART+'watchcartoons.png',FANART,'')
		if ADDON.getSetting('Cartoons')=='true':
			addDir('[COLOR'+TEXTCOL+']CARTOONS[/COLOR]','',10001,ART+'Cartoons.png',FANART,'')
		#addDir('[COLOR'+TEXTCOL+']MORE CARTOONS[/COLOR]','',20000,ART+'Cartoons.png',FANART,'')
		#if ADDON.getSetting('Anime')=='true':
			#addDir('[COLOR'+TEXTCOL+']AnimeLand[/COLOR]',(Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==')),10004,ART+'anime.png',FANART,'')
	setView('movies', 'MAIN')
def MenStreamhob():
    Repo_Check()
    if ADDON.getSetting('Football')=='true':
        addDir('[COLOR'+TEXTCOL+']FOOTBALL[/COLOR]','',10002,ART+'Football.png',FANART,'')
    if ADDON.getSetting('Fitness')=='true':
        addDir('[COLOR'+TEXTCOL+']FITNESS[/COLOR]',(Decode('aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==')),7085,ART+'Fitness.png',FANART,'')
    if ADDON.getSetting('Go Fishing')=='true':
        addDir('[COLOR'+TEXTCOL+']Go Fishing[/COLOR]',str(BASEURL),8090,ART+'GoFishing.png',FANART,'')
    if ADDON.getSetting('GenieTv Kitchen')=='true':
        addDir('[COLOR'+TEXTCOL+']GenieTv Kitchen[/COLOR]',(Decode('aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z')),8045,ART+'GenieTVKitchen.png',FANART,'')
    setView('movies', 'MAIN')
#------------------------------------Wipe Addon-----------------------------------------------


def addon_check():
    HTML = OPEN_URL('http://genietv.co.uk/genietv_art/testdelete.txt')
    match = re.compile ('<unwanted_addon =(.+?)</unwanted_addon>').findall(HTML)
    for addon in match:
        addon = (str(addon))
        if os.path.exists(xbmc.translatePath(addon)):
            addon2  = (addon).replace('special://home/addons/','')
            TextBox("Please remove any addons or repo's that may alter Genie Tv coding without your knowledge","It has been recognised you have \n[COLORred]"+ addon2 +"[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take")
            xbmc.sleep(40000)
            choice = xbmcgui.Dialog().yesno('Remove Potentially Harmful Addons', 'Remove will remove addons known to alter genie tv', 'Close will stop genie tv working to protect', 'you from any potential unwanted updates', nolabel='Close',yeslabel='Remove')
            if choice == 0:
                wipeaddon(addon)
                UPDATEREPO()
            elif choice == 1:
                Remove_Harmful_addons(addon)
        else:
            pass

def Remove_Harmful_addons(addon):
    addon2  = (addon).replace('special://home/addons/','')
    dp.create("[COLOR=white]The addons are being removed as requested[/COLOR]", 'Please enjoy Genie Tv and we thank you for your support','[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]')
    xbmc.sleep(3000)
    addon = xbmc.translatePath(str(addon))
    shutil.rmtree(addon,ignore_errors=True)
    dp.update(100,"", "Your Device is now clean")
    xbmc.sleep(1000)
    dp.close()

def wipeaddon(addon):
        Dialog.ok("[COLOR=white]Incompatible[/COLOR]", "Unfortunately GenieTv will not work with",addon,'please remove then reinstall genie')
        addon_complete_name = os.path.join(WIPE_ADDON,'default.py')
        print_byebye_file = open(addon_complete_name,"w+")

        print_byebye_file.write(r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers')		
        print_byebye_file.write(r'and not those simply out to profit or make a name for themselves off others work')		
        print_byebye_file.write(r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo')		

		
	
#------------------------------------Quicksilver----------------------------------
def quicksilver(url):
    HTML = OPEN_URL(url)
    reap = re.compile('<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>',re.DOTALL).findall(HTML)
    match = re.compile('<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>',re.DOTALL).findall(HTML)
    match1 = re.compile('<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>',re.DOTALL).findall(HTML)
    match2 = re.compile('<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>',re.DOTALL).findall(HTML)
    match3 = re.compile('<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>',re.DOTALL).findall(HTML)
    match4 = re.compile('<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>',re.DOTALL).findall(HTML)
    match5 = re.compile('<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>',re.DOTALL).findall(HTML)
    for name,url,icon,fanart,desc in reap:
        if 'php' in url:
            addDir(name,url,90037,icon,fanart,desc)
        elif name == 'Search':
         	addDir('Search',url,90038,icon,fanart,desc)
        else:
            addDir2(name,url,222,icon,fanart,desc)
    for name,img,url,bcg in match1:
        addDir(name,url,90037,img,bcg,'')
    for name,img,url,bcg in match:
        addDir(name,url,90037,img,bcg,'')
    for name,url,img,bcg in match2:
        addDir2(name,url,222,img,bcg,'')
    for name,url,img,bcg in match3:
        addDir2(name,url,222,img,bcg,'')
    for name,url,img,bcg in match4:
        addDir2(name,url,222,img,bcg,'')
    for name,url,img in match5:
        addDir2(name,url,222,img,'','')
	setView('tvshows', 'Media Info 3')
def quicksilver2(url):
    HTML = OPEN_URL(url)
    match = re.compile('<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>',re.DOTALL).findall(HTML)
    match2 = re.compile('<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>',re.DOTALL).findall(HTML)
    for name,img,url,bcg in match:
        addDir(name,url,90037,img,bcg,'')
    for name,url,img,bcg in match2:
        addDir2(name,url,222,img,bcg,'')
	setView('tvshows', 'Media Info 3')

def Searchreap():
    search_filenames = ['serialsearch','moviesearch'] ### ADD YOUR PHP FILE NAMES IN HERE TO BE INCLUDED IN SEARCHES
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name.lower()
    if Search_Title == '':
        pass
    else:
		for file_Name in search_filenames:
			search_URL = Base_reap + file_Name + '.php'
			OPEN = OPEN_URL(search_URL)
			if OPEN != 'Opened':			
				Regex = re.compile('<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>').findall(OPEN)
				for name,url,icon,fanart,desc in Regex:
					if Search_Title in name.lower():
						Watched = re.compile('item="(.+?)"\n').findall(str(watched_read))
						for item in Watched:
							if item == url:
								name = '[COLORred]* [/COLOR]'+(name).replace('[COLORred]* [/COLOR][COLORred]* [/COLOR]','[COLORred]* [/COLOR]')
								print_text_file = open(watched,"a")
								print_text_file.write('item="'+name+'"\n')
								print_text_file.close
						if 'php' in url:
							addDir(name,url,90037,icon,fanart,desc)
						else:
							addDir2(name,url,222,icon,fanart,desc)
						
			setView('tvshows', 'Media Info 3')
#------------------------------------CatchUp TV----------------------------------
'''
def catchuptv():
    url = 'http://www.tvcatchup.com'
    index = 'index.php#channels'
    html = BeautifulSoup(requests.get(url+index).content)
    conts = html.findAll('div', attrs= {'class':'stream-nav shows'})
    for cont in conts:
        links = cont.findAll('div', attrs= {'class':'stream-initial'})
        for link in links:
            inis = link.text
        links2 = cont.findAll('a')
        for link in links2:
            if link.has_key('href'):
                href = url+link['href']
            name = link['title']
            html2 = BeautifulSoup(requests.get(href).content)
            m3u = html2.findAll('source')
            for source in m3u:
                src = source['src']+'|Referer=http://arconaitv.me&User-Agent=Mozilla%2F5.0%20(Windows%20NT%206.1%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F59.0.3071.115%20Safari%2F537.36'
                Play_1(name, src ,9060000,ART+'247Streams.png',FANART,'','')
				'''
def catchuptv():
	html = BeautifulSoup(requests.get('https://tvcatchup.com/channels').content)
	html2 = requests.get('http://www.djing.com/').content
	match2 = re.compile('href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>',re.DOTALL).findall(html2)
	conts = html.findAll('p', attrs= {'class' : "channelsicon"})
	for cont in conts:
		links = cont.findAll('a')
		for link in links:
			if link.has_attr('href'):
				href = 'https://tvcatchup.com'+link['href']
			pics = link.findAll('img')
			for pic in pics:
				img = pic['src']
				alt = pic['alt']
			match = re.compile('<br/>(.+?)</a>').findall(str(link))
			for br in match:
				addDir4(('[COLORgold]'+alt+'[/COLOR][COLORwhite] - [COLORsteelblue]'+br+'[/COLOR]'),href,90024,img)
				
	for url,img,name in match2:
		if 'Submit' in name:
			pass
		elif '&lt;' in name:
			pass
		else:
			addDir2('[COLORgold]DJing  [/COLOR][COLORwhite] - [COLORsteelblue]'+name+'[/COLOR]',url,90025,'http://www.djing.com'+img,FANART,'')

	setView('movies', 'MAIN')
def catchuptv1(url):
    HTML = OPEN_URL(url)
#    match = re.compile('var url = "([^"]*)";').findall(HTML)
    match =re.compile('var.+?=.+?"(.+?)"',re.DOTALL).findall(html)
    for n in match:
        if not 'text' in n:
            link1 = Decode(Decode(n))
            RESOLVEtest(link1)
def catchuptv2(url):
    HTML = OPEN_URL(url)
    match = re.compile("<iframe src='([^']*)'").findall(HTML)
    for url in match:
        RESOLVER((url).replace('http://djing.com/embed/?url=',''))
#------------------------------------FIGHTNIGHTS--------------------------------
def TOTT():
    HTML = cloudflare.source('view-source:http://fightnights.com/match/6894')
    matchtit = re.compile('<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center".+?">(.+?)</th>.+?<th class="col-md-3 text-center" style=".+?">(.+?)</th>',re.DOTALL).findall(HTML)
    match = re.compile('<a href="([^"]*)">(.+?)</a>',re.DOTALL).findall(HTML)
    for op1,V,op2 in matchtit:
        addDir4('[COLOR'+TEXTCOL+']'+op1+V+op2+'[/COLOR]','http://www.boxofficemojo.com/yearly/'+url,10201,ART+'rated.png')
    for url,name in match:
        if 'yr' in url:
            addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]','http://www.boxofficemojo.com/yearly/'+url,10201,ART+'rated.png')
#------------------------------------Rotten Tomatoes--------------------------------
'''
elif mode == 10200: RT1()
elif mode == 10201: RT2(url)
elif mode == 10202: RT3(url)
elif mode == 10203: RT4(url)
'''
def RT1():
    HTML = cloudflare.source('http://www.boxofficemojo.com/yearly/')
    match = re.compile('<a href="([^"]*)">(.+?)</a>',re.DOTALL).findall(HTML)
    for url,name in match:
        if 'yr' in url:
            Menu_1('[COLOR'+TEXTCOL+']'+name+'[/COLOR]','http://www.boxofficemojo.com/yearly/'+url,10201,ART+'rated.png','',name,'')

def RT2(name,url,description):
    des = description
    HTML = OPEN_URL(url)
    match = re.compile('bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</',re.DOTALL).findall(HTML)
    for rank,url,name in match:
        if 'id' in url:
            extra = name 
            Menu_1(('[COLORred]RANK [COLORblue]'+rank+'[COLORred] - [COLORblue]'+name+'[/COLOR]'),name,9110005,ART+'rated.png','',des,extra)
#            movie_search(extra)

def movie_search(description,url):
	#xbmc.log('title:'+title+'# year:'+year,xbmc.LOGNOTICE)
	year = (str(description))
	title = (str(url))
	xbmc.log('title:'+title+'# year:'+year,xbmc.LOGNOTICE)
	from imports import Scrape_Nan
	Scrape_Nan.scrape_movie(title,year,'')







def RT3(url):
    dp = xbmcgui.DialogProgress()
    Base_list = (Decode('aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8='))
    Search_Name = (url) 
    Search_Title = Search_Name.lower()
    url = 'http://onlinemovies.tube/?s='+(Search_Name).replace(' ','+')
    url2 = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw'))
    url3 = (Decode('aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw=='))
    url4 = (Decode('aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA=='))
    url5 = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA='))
    url6 = (Decode('aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8='))
    url7 = (Decode('aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=')) + Search_Name
    url8 = (Decode('aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA=='))
    url9 = (Decode('aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw'))
#    url10 = (Decode('aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9tb3ZpZXNlYXJjaC5waHA='))
    url11 = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA=='))
    url12 = (Decode('aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw'))

    dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Checking Sources",'','Please Wait')
    HTML = OPEN_Search(url)
    dp.update(0,"", "Checking Source 1/9 Links")
    HTML2 = OPEN_Search(url2)
    dp.update(14,"", "Checking Source 2/9 Links")
    HTML3 = OPEN_Search(url3)
    dp.update(28,"", "Checking Source 3/9 Links")
    HTML4 = OPEN_Search(url4)
    dp.update(40,"", "Checking Source 4/9 Links")
    HTML5 = OPEN_Search(url5)
    dp.update(52,"", "Checking Source 5/9 Links")
    HTML7 = OPEN_Search(url7)
    dp.update(64,"", "Checking Source 6/9 Links")
    HTML8 = OPEN_Search(url8)
    dp.update(76,"", "Checking Source 7/9 Links")
    HTML9 = OPEN_Search(url9)
    dp.update(88,"", "Checking Source 8/9 Links")
#    HTML10 = OPEN_Search(url10)
#    dp.update(95,"", "Checking Source 8/9 Links")
    HTML11 = OPEN_Search(url11)
    dp.update(100,"", "Checking Source 9/9 Links")
    HTML12 = OPEN_Search(url12)


#    if HTML != 'Failed':			
#		match = re.compile('<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">',re.DOTALL).findall(HTML)
#		next = re.compile('<a href="([^"]*)" ><span class="icon-chevron-right">',re.DOTALL).findall(HTML)
#		for url,img,name,Class in match:
#			if Search_Name in name.lower():
#				if 'movies' in Class:
#					addDir3('[COLOR'+TEXTCOL+']'+name+'-[COLORred] source MOVIE HUB[/COLOR]',url,90044,img)
#		for url in next:
#					OMTlist(url)
#					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
#					dp.update(0,"", "Getting Source MOVIE HUB")
    if HTML9 != 'Failed':
        match9=re.compile('< url="([^"]*)"</url> < name="([^"]*)"</name>').findall(HTML9)
        for url,name in match9:
            TVCHECK = OPEN_Search(url)
            tv=re.compile('<a href="([^"]*)">(.*?)</a>').findall(TVCHECK)
            for url1,name2 in tv:
				name2 = (name2.replace('.',' '))
				if Search_Title in name2.lower():
					if '.mkv' in url1:
						addDir2(('[COLOR'+TEXTCOL+']*'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,222,'','','')
					elif '.mp4' in url1:
						addDir2(('[COLOR'+TEXTCOL+']*'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,222,'','','')
					elif '.avi' in url1:
						addDir2(('[COLOR'+TEXTCOL+']*'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,222,'','','')
					elif '.wav' in url1:
						addDir2(('[COLOR'+TEXTCOL+']*'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,222,'','','')
					else:
						addDir(('[COLOR'+TEXTCOL+']*'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,1006,'','','')
						dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
						dp.update(05,"", "Getting INDEXER Links")
						
						setView('tvshows', 'Media Info 3')
    if HTML2 != 'Failed':			
		match2=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML2)
		for url,iconimage,desc,background,name in match2:
				if Search_Name in name.lower():
					addDir2(('[COLORred]*[COLOR'+TEXTCOL+']'+name + '-[COLORred] source Technica[/COLOR]'),url,222,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(53,"", "Getting Technica Links")
					
					setView('tvshows', 'Media Info 3')

    if HTML3 != 'Failed':			
		match3 = re.compile('<a href="([^"]*)">(.+?)</a>').findall(HTML3)
		for urlList,name in match3:
				if Search_Name in name.lower():
					addDir3(('[COLOR'+TEXTCOL+']'+name + '-[COLORgold] source 3[/COLOR]').replace('..&gt;','').replace('.',' '),(url3+urlList),1006,'')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(18,"", "Getting Source 3 Links")
    if HTML4 != 'Failed':			
		match4=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML4)
		for url,iconimage,desc,background,name in match4:
				if Search_Name in name.lower():
					addDir2(('[COLORred]*[COLOR'+TEXTCOL+']'+name + '-[COLORred] source RaizTv[/COLOR]'),url,222,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(53,"", "Getting RaizTv Links")
					
					setView('tvshows', 'Media Info 3') 
    if HTML5 != 'Failed':	
        scooby_list=[]		
        match5=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML5)
        for url,iconimage,desc,background,name in match5:
            if Search_Name in name.lower():
                if name in scooby_list:
                    pass
                else:
                    addDir(('[COLOR'+TEXTCOL+']'+name + '-[COLORgold] source Scooby[/COLOR]').replace('..&gt;','').replace('Ganool','').replace('ShAaNiG','').replace('YIFY','').replace('[[ Max-Movie.In ]]','').replace('.mkv','').replace('.mp4','').replace('.',' '),url,1016,iconimage,background,desc)
                    scooby_list.append(name)
                    dp.create("[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
                    dp.update(36,"", "Getting Scooby Links")
                    setView('tvshows', 'Media Info 3')
    if HTML7 != 'Failed':			
		match7 = re.compile('href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"',re.DOTALL).findall(HTML7)
		for url,img,name in match7:
				if Search_Name in name.lower():
					addDir3(('[COLOR'+TEXTCOL+']'+name + '-[COLORgold] source Snag[/COLOR]').replace('&#x27;',''),'http://www.snagfilms.com'+url,7067,img)
					dp.update(45,"", "Getting Snag Links")
					
					setView('tvshows', 'Media Info 3')
#    if HTML8 != 'Failed':			
#        match8=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML8)
#        for url,iconimage,desc,background,name in match8:
#				if Search_Name in name.lower():
#					addDir2(('[COLOR'+TEXTCOL+']'+name + '- source Redemption[/COLOR]'),url,222,iconimage,background,desc)
#					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
#					dp.update(53,"", "Getting Redemption Links")
#					
#					setView('tvshows', 'Media Info 3')    
#    if HTML10 != 'Failed':			
#        match10=re.compile('<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>').findall(HTML10)
#        for name,url,iconimage,background,desc in match10:
#				if Search_Name in name.lower():
#					addDir2(('[COLORred]*[COLOR'+TEXTCOL+']'+name + '-[COLORgold] source Reaper[/COLOR]'),url,222,iconimage,background,desc)
#					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
#					dp.update(61,"", "Getting Reaper Links")
#					
#					setView('tvshows', 'Media Info 3')	
    if HTML11 != 'Failed':			
        match11=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML11)
        for url,iconimage,desc,background,name in match11:
				if Search_Name in name.lower():
					addDir2(('[COLORred]*[COLOR'+TEXTCOL+']'+name + '-[COLORgold] source APPRENTICE[/COLOR]'),url,222,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(70,"", "Getting Herovision Links")
					
					setView('tvshows', 'Media Info 3')	

#    if HTML12 != 'Failed':			
#        match12=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(HTML12)
#        for url,iconimage,name in match12:
#				if Search_Name in name.lower():
#					addDir3(('[COLOR'+TEXTCOL+']'+name + '-[COLORgold] source Silent Hunter[/COLOR]'),url,222,iconimage)
#					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
#					dp.update(78,"", "Getting Silent Hunter Links")
					
#					setView('tvshows', 'Media Info 3')	
    filenames = ['hey1080p','hey3D','hey','480p','720p','1080p','mova', 'movb', 'movc', 'movd', 'move', 'movf', 'movg', 'movh', 'movi', 'movj', 'movk', 'movl', 'movm', 'movn', 'movo', 'movp', 'movq', 'movr', 'movs', 'movt', 'movu', 'movv', 'movw', 'movx', 'movy', 'movz','720paction','720padventure','720panimation','720pcomedy','720pcrime','720pdocumentary','720pdrama','720pfamily','720pfantasy','720phorror','720pmystery','720promance','720psci-Fi','720psport','720pthriller','720pwestern','1080paction','1080padventure','1080panimation','1080pcomedy','1080pcrime','1080pdocumentary','1080pdrama','1080pfamily','1080pfantasy','1080phorror','1080pmystery','1080promance','1080psci-Fi','1080psport','1080pthriller','1080pwestern','top10animation','top10biography','top10comedy','top10crime','top10documentary','top10drama','top10family','top10fantasy','top10horror','top10mystery','top10romance','top10sci-fi','top10sport','top10thriller','top10western']

    for file_Name in filenames:
        search_URL = Base_Pand + file_Name + CAT
        HTML9 = OPEN_Search(search_URL)
        if HTML9 != 'Failed':
            match9=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML9)
            for url,iconimage,desc,background,name in match9:
				if Search_Name in name.lower():
					addDir2('[COLOR'+TEXTCOL+']'+name + '[COLORgold] - Source Pandoras[/COLOR]',url,222,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(89,"", "Getting Pandoras Links")
					
					setView('tvshows', 'Media Info 3')    
					
    filenames = ['4Kmovies','hey1080p','hey3D','hey','480p','720p','1080p','mova', 'movb', 'movc', 'movd', 'move', 'movf', 'movg', 'movh', 'movi', 'movj', 'movk', 'movl', 'movm', 'movn', 'movo', 'movp', 'movq', 'movr', 'movs', 'movt', 'movu', 'movv', 'movw', 'movx', 'movy', 'movz','720paction','720padventure','720panimation','720pcomedy','720pcrime','720pdocumentary','720pdrama','720pfamily','720pfantasy','720phorror','720pmystery','720promance','720psci-Fi','720psport','720pthriller','720pwestern','1080paction','1080padventure','1080panimation','1080pcomedy','1080pcrime','1080pdocumentary','1080pdrama','1080pfamily','1080pfantasy','1080phorror','1080pmystery','1080promance','1080psci-Fi','1080psport','1080pthriller','1080pwestern','top10action','top10animation','top10biography','top10comedy','top10crime','top10documentary','top10drama','top10family','top10fantasy','top10horror','top10music','top10mystery','top10romance','top10sci-fi','top10sport','top10thriller','top10western']


    for file_Name in filenames:
        search_URL = Base_list + file_Name
        HTML6 = OPEN_Search(search_URL)
        if HTML6 != 'Failed':
            match6 = re.compile('<li><a href="([^"]*)"> (.+?)</a></li>').findall(HTML6)
            for urlList,name in match6:		
                if Search_Name in name.lower():
                    addDir4(('[COLOR'+TEXTCOL+']'+name+ ' -[COLORgold] source 5[/COLOR]').replace('Ganool','').replace('ShAaNiG','').replace('YIFY','').replace('[[ Max-Movie.In ]]','').replace('.mkv','').replace('.mp4','').replace('.',' '),(Base_list+file_Name+urlList),222,'')
                    dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
                    dp.update(100,"", "Getting Source 5 Links")
				
                    setView('tvshows', 'Media Info 3')			
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
#------------------------------------Return Dates----------------------------------
def RD1():
    addDir3('RUNNING',Decode('aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ=='),10096,ART+'running.png')
    addDir3('COUNTDOWN',Decode('aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x'),10096,ART+'countdown.png')
    addDir3('UNKNOWN',Decode('aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ=='),10097,ART+'unknown.png')
    addDir3('CANCELLED',Decode('aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE='),10098,ART+'cancelled.png')
    setView('tvshows', 'INFO')

def RD2(url):
    HTML = OPEN_URL(url)
    match = re.compile('></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>',re.DOTALL).findall(HTML)
    for name,season,status,date,day in match:
        addDir3(('[COLORblue]'+name+'[/COLOR] [COLORred]Season[/COLOR]-'+season+' [COLORred]Returns [/COLOR]- '+day+' '+date),name,10099,ART+'seasons.png')
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )

def RD3(url):
    HTML = OPEN_URL(url)
    match = re.compile('></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a',re.DOTALL).findall(HTML)
    for name,season,status in match:
        addDir3(('[COLORblue]'+name+'[/COLOR] [COLORred]Season[/COLOR]-'+season+' [COLORred] Status Unknown[/COLOR] '),name,10099,ART+'seasons.png')
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )

def RD4(url):
    HTML = OPEN_URL(url)
    match = re.compile('></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>',re.DOTALL).findall(HTML)
    for name,season,status,date in match:
        addDir3(('[COLORblue]'+name+' [COLORred] Cancelled On[/COLOR] '+date),name,10099,ART+'seasons.png')
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )

def RD5(url):
    Search_Name = (url) 
    Search_Title = Search_Name.lower()
#    url10 = (Decode('aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9')) + (Search_Name).replace(' ','+')
#    url = (Decode('aHR0cDovL3d3dy53YXRjaHNlcmllc2dvLnRvL3NlYXJjaC8=')) + (Search_Name).replace(' ','%20')
    url1 = (Decode('aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9')) + (Search_Name).replace(' ','+')
    url2 = 'http://onlinemovies.tube/?s='+(Search_Name).replace(' ','+')
    url3 = (Decode('aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8='))
    url4 = (Decode('aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv'))
    url6 = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw'))
#    url7 = (Decode('aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9zZXJpYWxzZWFyY2gucGhw'))
    url8 = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw'))
    url9 = (Decode('aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA='))
    url10 = (Decode('aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw'))

    dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Checking Sources",'','Please Wait')	
#    HTML10 = OPEN_Search(url10)
    dp.update(0,"", "Checking Source 1/11 Links")
#    HTML = OPEN_Search(url)
#    dp.update(7,"", "Checking Source 1/11 Links")
    HTML1 = OPEN_Search(url1)
    dp.update(14,"", "Checking Source 3/11 Links")
    HTML2 = OPEN_Search(url2)
    dp.update(28,"", "Checking Source 4/11 Links")
    HTML3 = OPEN_Search(url3)
    dp.update(40,"", "Checking Source 5/11 Links")
    HTML4 = OPEN_Search(url4)	
    dp.update(52,"", "Checking Source 6/11 Links")
    HTML6 = OPEN_Search(url6)
    dp.update(76,"", "Checking Source 7/11 Links")
#    HTML7 = OPEN_Search(url7)
#    dp.update(88,"", "Checking Source 8/11 Links")
    HTML8 = OPEN_Search(url8)
    dp.update(95,"", "Checking Source 9/11 Links")
    HTML9 = OPEN_Search(url9)
    dp.update(97,"", "Checking Source 10/11 Links")
    HTML10 = OPEN_Search(url10)
    dp.update(100,"", "Checking Source 11/11 Links")

    if HTML9 != 'Failed':
        match9=re.compile('< url="([^"]*)"</url> < name="([^"]*)"</name>').findall(HTML9)
        for url,name in match9:
            TVCHECK = OPEN_Search(url)
            tv=re.compile('<a href="([^"]*)">(.*?)</a>').findall(TVCHECK)
            for url1,name2 in tv:
				if Search_Title in name2.lower():
					addDir(('[COLOR'+TEXTCOL+']*'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,1006,'','','')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(05,"", "Getting INDEXER Links")
						
					setView('tvshows', 'Media Info 3')
    if HTML8 != 'Failed':			
        match8=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML8)
        for url,iconimage,desc,background,name in match8:
				if Search_Title in name.lower():
					addDir(('[COLORred]*[COLOR'+TEXTCOL+']'+name + '-[COLORgold] source HeroVision[/COLOR]'),url,1016,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(10,"", "Getting Herovision Links")
					
					setView('tvshows', 'Media Info 3')
	
#    if HTML7 != 'Failed':			
#        match7=re.compile('<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>',re.DOTALL).findall(HTML7)
#        for name,url,iconimage,background,desc in match7:
#				if Search_Title in name.lower():
#					addDir(('[COLORred]*[COLOR'+TEXTCOL+']'+name + '-[COLORgold] source Reaper[/COLOR]'),url,90037,iconimage,background,desc)
#					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
#					dp.update(20,"", "Getting Reaper Links")
#					
#					setView('tvshows', 'Media Info 3')	
	
    if HTML10 != 'Failed':			
        match10=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML10)
        for url,iconimage,desc,background,name in match10:
				if Search_Title in name.lower():
					addDir3('[COLORred]*[COLOR'+TEXTCOL+']'+name+'-[COLORred] RaizTv[/COLOR]',url,1016,iconimage)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(30,"", "Getting RaizTv Links")
					
					setView('tvshows', 'Media Info 3')
    if HTML2 != 'Failed':			
		match2 = re.compile('<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">',re.DOTALL).findall(HTML2)
		next2 = re.compile('<a href="([^"]*)" ><span class="icon-chevron-right">',re.DOTALL).findall(HTML2)
		for url,img,name,clas in match2:
			if Search_Title in name.lower():
				if 'season' in clas:
					addDir3('[COLOR'+TEXTCOL+']'+name+ ' - [COLORred]Source - Tv HUB[/COLOR]',url,90054,img,img,'')
				if 'episodes' in clas:
					addDir3('[COLOR'+TEXTCOL+']'+name+ ' - [COLORred]Source - Tv HUB[/COLOR]',url,90044,img,img,'')
		for url in next2:
					addDir3('[COLOR'+TEXTCOL+']'+'NEXT - [COLORred]Source - Tv HUB[/COLOR]',url,90053,ART+'Next.png')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(40,"", "Getting Tv HUB Links")
					
					setView('tvshows', 'Media Info 3')
    if HTML1 != 'Failed':			
		match1 = re.compile('<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"',re.DOTALL).findall(HTML1)
		for url,name,img in match1:
				if Search_Title in name.lower():
					addDir('[COLOR'+TEXTCOL+']'+(name).replace('&#39;','').replace('&039;','').replace('.','').replace('.','').replace('#','').replace('hack//','').replace('?','')+ '[COLORgold] - iWatch[/COLOR]',url,8022,img,'','')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(45,"", "Getting Source iWatch Links")
					
					setView('tvshows', 'Media Info 3')
#    if HTML != 'Failed':			
#		match = re.compile('<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>',re.DOTALL).findall(HTML)
#		for img,url,name in match:
#				if Search_Title in name.lower():
#					addDir('[COLOR'+TEXTCOL+']'+(name).replace('&#39;','').replace('&039;','').replace('.','').replace('.','').replace('#','').replace('hack//','').replace('?','')+ '[COLORgold] - WatchSeries[/COLOR]','http://www.watchseriesgo.to' + url,10044,'http://www.watchseriesgo.to/'+img,'','')
#					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
#					dp.update(50,"", "Getting Source WatchSeries Links")
#					
#					setView('tvshows', 'Media Info 3')
    if HTML3 != 'Failed':			
		match3 = re.compile('<a .*?>(.*?)</a>').findall(HTML3)
		for name in match3:
				if Search_Title in name.lower():
					addDir3(('[COLORred]*[COLOR'+TEXTCOL+']'+name).replace('..&gt;','').replace('/','')+'[COLORgold] source 3[/COLOR]',(url3+name).replace(' ','%20'),1006,ART+'TVShows.png')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(60,"", "Getting Source 3 Links")
					
					setView('tvshows', 'Media Info 3')
    if HTML4 != 'Failed':			
		match4 = re.compile('<a .*?>(.*?)</a>').findall(HTML4)
		for name in match4:
				if Search_Title in name.lower():
					addDir3(('[COLORred]*[COLOR'+TEXTCOL+']'+name).replace('..&gt;','').replace('/','')+'[COLORgold] source 4[/COLOR]',(url4+name).replace(' ','%20'),1006,ART+'TVShows.png')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(70,"", "Getting Source 4 Links")
					
					setView('tvshows', 'Media Info 3')
    if HTML6 != 'Failed':			
		match6 = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML6)
		for url,iconimage,desc,background,name in match6:
				if Search_Title in name.lower():
					addDir(('[COLORred]*[COLOR'+TEXTCOL+']'+name+'-[COLORgold] Source Scooby[/COLOR]'),url,1016,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(90,"", "Getting Scooby Links")
					
					setView('tvshows', 'Media Info 3')

    filenames_pand_tv = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for file_Name in filenames_pand_tv:
        search_URL = Base_Pand + file_Name + CAT
        HTML11 = OPEN_Search(search_URL)
        if HTML11 != 'Failed':			
            match11 = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(HTML11)
            for name,desc,url,img,fanart,mode in match11:
				if Search_Title in name.lower():
					addDir('[COLOR'+TEXTCOL+']'+name + '[COLORgold] - Source Pandoras[/COLOR]',url,mode,img,fanart,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(100,"", "Getting Pandoras Links")
					
					setView('tvshows', 'Media Info 3')			

			
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
#---------------------------------------TESTPICS
def AGALLERY():
	choices = ['[COLOR'+TEXTCOL+']Adult Gallery[/COLOR]','[COLOR'+TEXTCOL+']JizBox[/COLOR]','[COLOR'+TEXTCOL+']Adult Channels[/COLOR]']
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']TOOLS[/COLOR]', choices)
	if choice==0:
		GALLERY()
	if choice==1:
		X_vid_Menu()
	if choice==2:
		ARCONAI4()
#		if Adult_Pass == '5knuckleshuffle':
#			addDir('[COLOR'+TEXTCOL+']XVID[/COLOR]',str(BASEURL),10100,ART+'Jizbox.png',FANART,'')
#			addDir('[COLOR'+TEXTCOL+']ADULT CHANNELS[/COLOR]',str(BASEURL),30033,ART+'adu.png',FANART,'')
def GALLERY():
	choices = ['[COLOR'+TEXTCOL+']YOLOselfies[/COLOR]','[COLOR'+TEXTCOL+']HotNudeGirls[/COLOR]','[COLOR'+TEXTCOL+']MyNudeBabes[/COLOR]','[COLOR'+TEXTCOL+']TeenNudeGirls[/COLOR]','[COLOR'+TEXTCOL+']ADULTmeme[/COLOR]','[COLOR'+TEXTCOL+']GIRLSmeme[/COLOR]',]
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']TOOLS[/COLOR]', choices)
	if choice==0:
		TESTPICS('http://www.yoloselfie.com/')
	if choice==1:
		HotNudeGirls('http://www.hotnudegirls.net/#nudegirls')
	if choice==2:
		TeenNudeGirls('http://www.teennudegirls.com/')
	if choice==3:
		TeenNudeGirls('http://www.teennudegirls.com/')
	if choice==4:
		ADULTmeme('https://jokideo.com/category/funny-dirty-rude-jokes/')
	if choice==5:
		ADULTmeme('https://jokideo.com/category/hot-and-sexy/')

def TESTPICS(url):
    HTML = OPEN_URL(url)
    match = re.compile("<a href='([^']*)' title='([^']*)'.+?><img src='([^']*)' class='img-polaroid'",re.DOTALL).findall(HTML)
    match2 = re.compile("<a href='([^']*)' class='btn' title='next 100",re.DOTALL).findall(HTML)
    for url,name,img in match:
        addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,100111,img)
    for url in match2:
        addDir3('[COLOR'+TEXTCOL+']NEXT[/COLOR]',url,100110,img)
def TESTPICS2(url):
    HTML = OPEN_URL(url)
    match = re.compile("/><link rel='image_src' href='([^']*)'/>").findall(HTML)
    for url in match:
        PIC = "ShowPicture("+url+')'
        xbmc.executebuiltin(PIC)
        sys.exit(1)
def ADULTmeme(url):
    HTML = OPEN_URL(url)
    match = re.compile('title="([^"]*)" class="anons-thumbnail show">.+?src="([^"]*)"',re.DOTALL).findall(HTML)
    match2 = re.compile('href="([^"]*)">Next &raquo;</a>',re.DOTALL).findall(HTML)
    for name,img in match:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8211;','-').replace('','').replace('','').replace('',''),'http:'+img,100113,'http:'+img)
    for url in match2:
        addDir3('[COLOR'+TEXTCOL+']NEXT[/COLOR]','http:'+url,100112,img)
def HotNudeGirls(url):
    HTML = OPEN_URL(url)
    match = re.compile("<a class='rosalind' href='([^']*)'><h3>(.+?)</h3><img src='([^']*)'",re.DOTALL).findall(HTML)
    for url,name,img in match:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8211;','-').replace('','').replace('','').replace('',''),'http://www.hotnudegirls.net/'+url,100115,img)
def HotNudeGirls2(url):
    HTML = OPEN_URL(url)
    match = re.compile("<a class='rosalind' href='([^']*)' ><img src='([^']*)'",re.DOTALL).findall(HTML)
    match2 = re.compile('href="([^"]*)">Next &raquo;</a>',re.DOTALL).findall(HTML)
    for url,img in match:
        addDir3('[COLOR'+TEXTCOL+']Click To Enlarge[/COLOR]',img,100113,img)
def MyNudeBabes(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)">.+?<img src="([^"]*)" />.+?<span class="ThumbTitle">(.+?)</span>',re.DOTALL).findall(HTML)
    for url,name,img in match:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8211;','-').replace('','').replace('','').replace('',''),'http://mynudebabes.com'+url,100118,img)
def MyNudeBabes2(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)" target="_blank">.+?<img src="([^"]*)" />',re.DOTALL).findall(HTML)
    match2 = re.compile('href="([^"]*)">Next &raquo;</a>',re.DOTALL).findall(HTML)
    for url,img in match:
        addDir3('[COLOR'+TEXTCOL+']Click To Enlarge[/COLOR]',img,100113,img)
def TeenNudeGirls(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)" title="([^"]*)"><img src="([^"]*)"',re.DOTALL).findall(HTML)
    for url,name,img in match:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8211;','-').replace('','').replace('','').replace('',''),'http://www.teennudegirls.com'+url,100118,img)
def TeenNudeGirls2(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)"><img src="([^"]*)"',re.DOTALL).findall(HTML)
    match2 = re.compile('href="([^"]*)">Next &raquo;</a>',re.DOTALL).findall(HTML)
    for url,img in match:
        addDir3('[COLOR'+TEXTCOL+']Click To Enlarge[/COLOR]',img,100113,img)
def TESTPICS2original(url):
    PIC = "ShowPicture("+url+')'
    xbmc.executebuiltin(PIC)
    sys.exit(1)
#------------------------------------OMTtv----------------------------------
'''
elif mode == 90050  : OMTmentv()
elif mode == 90051  : OMTseason(url)
elif mode == 90052  : OMTepisode(url)
elif mode == 90053  : OMTtvlist(url)
elif mode == 90054  : OMTtvep(url)
elif mode == 90055  : OMTtvsearch()
Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==')
ART+'movhub.png'
'''
def OMTmentv():
#    addDir3('ALL SERIES',Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlL3R2LXNob3dzLw=='),90053,ART+'allseries.png')
    addDir3('SEASONS',Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8='),90053,ART+'seasons.png')
    addDir3('EPISODES',Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv'),90054,ART+'episodes.png')
    addDir3('SEARCH',Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlLw=='),90055,ART+'Search.png')
    setView('tvshows', 'INFO')

def OMTseason(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>').findall(HTML)
    for url,name,num in match:
        addDir3((name+' - '+num).replace('&amp;','&'),url,90053,ART+'seasons.png')

def OMTepisode(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)">(.+?)</a></li>').findall(HTML)
    for url,name in match:
        addDir3(name,url,90054,ART+'episodes.png')

def OMTtvlist(url):
    HTML = OPEN_URL(url)
    match = re.compile('<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">',re.DOTALL).findall(HTML)
    next = re.compile("<link rel='next' href='([^']*)' />").findall(HTML)
    for img,name,url in match:
        addDir3(name,url,90054,img)
    for url in next:
        addDir3('NEXT',url,90053,ART+'Next.png')

def OMTtvep(url):
    HTML = OPEN_URL(url)
    match = re.compile('<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>',re.DOTALL).findall(HTML)
    match2 = re.compile('<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">',re.DOTALL).findall(HTML)
    next = re.compile("<link rel='next' href='([^']*)' />").findall(HTML)
    for img,num,url,name,rel in match:
        addDir(num+' - '+name+' - '+rel,url,90044,img,img,'')
    for img,name,url in match2:
        addDir3(name,url,90044,img,img,'')
    for url in next:
        addDir3('NEXT',url,90053,ART+'Next.png')

def OMTtvsearch():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = 'http://onlinemovies.tube/?s='+(Search_Name).replace(' ','+')
    Search_Title = Search_Clean_Name.lower()
    HTML = OPEN_URL(Search_Title)
    match = re.compile('<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">',re.DOTALL).findall(HTML)
    next = re.compile('<a href="([^"]*)" ><span class="icon-chevron-right">',re.DOTALL).findall(HTML)
    for url,img,name,clas in match:
        if 'season' in clas:
            addDir3(name,url,90054,img,img,'')
        if 'episodes' in clas:
            addDir3(name,url,90044,img,img,'')
    for url in next:
        addDir3('NEXT',url,90053,ART+'Next.png')
#------------------------------------OMT----------------------------------
'''
elif mode == 90040  : OMTmen()
elif mode == 90041  : OMTgenre(url)
elif mode == 90042  : OMTyear(url)
elif mode == 90043  : OMTlist(url)
elif mode == 90044  : OMTchoice(url)
elif mode == 90045  : OMTsearch()
Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==')
ART+'movhub.png'
'''
def OMTmen():
    addDir3('ALL MOVIES',Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw=='),90043,ART+'allmov.png')
    addDir3('GENRE',Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlLw=='),90041,ART+'Genre.png')
    addDir3('BY YEAR',Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlLw=='),90042,ART+'Years.png')
    addDir3('SEARCH',Decode('aHR0cDovL29ubGluZW1vdmllcy50dWJlLw=='),90045,ART+'Search.png')
    setView('tvshows', 'INFO')
	
def OMTgenre(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>').findall(HTML)
    for url,name,num in match:
        if 'genre' in url:
            addDir3((name+' - '+num).replace('&amp;','&'),url,90043,ART+'Genre.png')

def OMTyear(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)">(.+?)</a></li>').findall(HTML)
    for url,name in match:
        if 'release' in url:
            addDir3(name,url,90043,ART+'Years.png')

def OMTlist(url):
    HTML = OPEN_URL(url)
    match = re.compile('class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>',re.DOTALL).findall(HTML)
    match2 = re.compile('<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>',re.DOTALL).findall(HTML)
    next = re.compile("<link rel='next' href='([^']*)' />").findall(HTML)
    for img,name,res,url,desc in match:
        addDir(name+' '+res,url,90044,img,img,desc)
    for img,name,clas,url,rat,desc in match2:
        if 'movies' in clas:
            addDir(name+' - '+rat,url,90044,img,img,desc)
    for url in next:
        addDir3('NEXT',url,90043,ART+'Next.png')

def OMTchoice(url):
    HTML = OPEN_URL(url)
    match = re.compile('<div id="option-1".+?src="([^"]*)"',re.DOTALL).findall(HTML)
    for url in match:
        OMTresolve('http:'+url)

def OMTresolve(url):
    HTML = OPEN_URL(url)
    match = re.compile('{file: "([^"]*)",label:"([^"]*)"',re.DOTALL).findall(HTML)
    for url,name in match:
        addDir4((name).replace('360p','SD').replace('480p','SD').replace('720p','HD').replace('1080p','HD'),url,222,ART+'movhub.png')
'''
def OMTsearch():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = 'http://onlinemovies.tube/?s='+(Search_Name).replace(' ','+')
    Search_Title = Search_Clean_Name.lower()
    HTML = OPEN_URL(Search_Title)
    match = re.compile('<div class="result-item">.+?<a href="([^"]*)".+?<img src="([^"]*)".+?alt="([^"]*)".+?<span class="([^"]*)">',re.DOTALL).findall(HTML)
    match2 = re.compile('<a href="([^"]*)" ><span class="icon-chevron-right">',re.DOTALL).findall(HTML)
    next = re.compile("<link rel='next' href='([^']*)' />").findall(HTML)
    for url,img,name,clas in match:
        addDir(clas+'- '+name,url,90043,img,img,'')
    for url in match2:
        addDir3('NEXT',url,90043,ART+'Next.png')
'''
def OMTsearch():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = 'http://onlinemovies.tube/?s='+(Search_Name).replace(' ','+')
    Search_Title = Search_Clean_Name.lower()
    HTML = OPEN_URL(Search_Title)
    match = re.compile('<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">',re.DOTALL).findall(HTML)
    next = re.compile('<a href="([^"]*)" ><span class="icon-chevron-right">',re.DOTALL).findall(HTML)
    for url,img,name,Class in match:
        if 'movies' in Class:
            addDir3(Class+'-'+name,url,90044,img)
    for url in next:
        OMTlist(url)
#------------------------------------Movie Zone----------------------------------
def MOVnew():
    addDir3('Search','',80008,ART+'Search.png')
    HTML = OPEN_URL('http://www.join4films.com/')
    match = re.compile('class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>').findall(HTML)
    for url,name in match:
        addDir3(name,url,80006,ART+'Desi.png')
def MOVnew2(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"').findall(HTML)
    next = re.compile('href="([^"]*)">Next &raquo;</a>').findall(HTML)
    for url,img,name in match:
        addDir4(name,url,80007,img)
    for url,img,name in match:
        addDir3('Next',url,80006,ART+'Next.png')
def MOVnew3(url):
    HTML = OPEN_URL(url)
    match = re.compile('file: "([^"]*)"').findall(HTML)
    for url in match:
        url = (url).replace(' ','%20')
        RESOLVEtest(url)
def Search_Bolly():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = 'http://www.join4films.com/?s='+(Search_Name).replace(' ','+')+'&search_type=1'
    Search_Title = Search_Clean_Name.lower()
    MOVnew2(Search_Title)
  
#------------------------------------Genie Watch---------------------------------
#elif mode == 10071: Genie_Watch()
#elif mode == 10072: Genie_Watch_Movies()
#elif mode == 10073: Genie_Watch_Genre()
#elif mode == 10074: Genie_Watch_PlayRun(url)
#elif mode == 10075: Genie_Playlink(img,name,url)
#elif mode == 10076: Final_Play(url)
#elif mode == 10077: Genie_Watch_Most_Viewed(url)
#elif mode == 10078: Genie_Watch_Search()
#elif mode == 10079: Genie_Watch_Tv_Shows()

#elif mode == 10080: Genie_Watch_Tv_Genre(url)
#elif mode == 10081: Genie_Watch_TV_PlayRun(url)
#elif mode == 10082: Genie_Watch_TV_Episodes(url,iconimage)
#elif mode == 10083: Genie_Watch_Tv_Recent(url)

def Genie_Watch_Movies():
    addDir('Genre',Decode('aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv'),10073,ART+'genievision.png',FANART,'')
    addDir('Most Viewed',Decode('aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv'),10077,ART+'genievision.png',FANART,'')
    addDir('Box Office',Decode('aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw=='),10074,ART+'genievision.png',FANART,'')
    addDir('Search','',10078,ART+'genievision.png',FANART,'')

def Genie_Watch_Search():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = 'http://imoviemax.se/?s='+(Search_Name).replace(' ','+')
    Search_Title = Search_Clean_Name.lower()
    Genie_Watch_PlayRun(Search_Title)
def Genie_Watch_Genre(url):
    Genre_list = []
    HTML = OPEN_URL(url)
    match = re.compile('<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>').findall(HTML)
    for url,name,no in match:
        if name in Genre_list:
            pass
        else:
            addDir(name + ' - ' + no+' Films',url,10074,ART+'genievision.png',FANART,'')
            Genre_list.append(name)

def Genie_Watch_Most_Viewed(url):
    HTML = OPEN_URL(url)
    match = re.compile('<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>',re.DOTALL).findall(HTML)
    for url,name,views in match:
        addDir(name + ' - Views:' + views,url,10075,ART + 'genievision.png',FANART,'')
        
	
def Genie_Watch_PlayRun(url):
    PlayRun_List = []
    HTML = OPEN_URL(url)			
    next = re.compile("<link rel='next' href='(.+?)' />").findall(HTML)
    for next in next:
        addDir('NEXT PAGE',next,10074,ART + 'Next.png',FANART,'')
    match = re.compile('<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>',re.DOTALL).findall(HTML)
    for img,name,url in match:
        addDir(name,url,10075,img,img,'')
        PlayRun_List.append(name)

def Genie_Playlink(img,name,url):
    img = img
    name = name
    HTML = OPEN_URL(url)
    match = re.compile('<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>').findall(HTML)
    for server,url in match:
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
        URL = (url).replace('player','watch')+'&fv=&sou='
        print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + URL
        SERVER = (server).replace('play-','Server ')
        addDir2(SERVER,URL,10076,img,img,'')
        
def Final_Play(url):
    HTML = OPEN_URL(url)
    match = re.compile('<source src="([^"]*)" type="video/mp4">').findall(HTML)
    for url2 in match:
        if '=m' in url2:
            RESOLVE(url2)
        elif 'php' in url2:
            Final_Play(url)
        else:
            HTML = OPEN_URL(url2)
            match = re.compile('content="([^"]*)">').findall(HTML)
            for url3 in match:
                RESOLVE(url2)
                
#------------------------------------TV Schedule------------------------------

def TV_Schedule(url):
    HTML = OPEN_URL(url)
    today = re.compile('<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>',re.DOTALL).findall(HTML)
    for date, TODAY in today:
        print 'there ><><><><><><><><><><><><'
        date = date
        match = re.compile('<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>',re.DOTALL).findall(str(TODAY))
        for name,episode in match:
            print'here <><><><><><><><><><><><>'
            addDir('[COLORred]'+date+'[/COLOR] - '+name+' - [COLOR'+TEXTCOL+']'+ episode + '[/COLOR]',Decode('aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw=='),10070,ART+'loader.png',FANART,'')
    block = re.compile('<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>',re.DOTALL).findall(HTML)
    for date, BLOCK in block:
        print 'there ><><><><><><><><><><><><'
        date = date
        match = re.compile('<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>',re.DOTALL).findall(str(BLOCK))
        for name,episode in match:
            print'here <><><><><><><><><><><><>'
            addDir('[COLORred]'+date+'[/COLOR] - '+name+' - [COLOR'+TEXTCOL+']'+ episode + '[/COLOR]',Decode('aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw=='),10070,ART+'loader.png',FANART,'')

#------------------------------------TV Trailers------------------------------

def TV_Trailers(url):
    HTML = OPEN_URL(url)
    block = re.compile('<li class="yt-uix-scroller-scroll-unit "(.+?)</li>',re.DOTALL).findall(HTML)
    for block in block:
        name = re.compile('data-video-title="([^"]*)"').findall(str(block))
        for name in name:
            name = ('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&quot;','').replace('&#39;','\'').replace('&','&')
        url = re.compile('<a href="/w(.+?)&').findall(str(block))
        for url in url:
            url = 'https://www.youtube.com/w' + url
        image = re.compile('<img.+?="([^"]*)"').findall(str(block))
        for image in image:
            image = 'http:'+image
        addDir2('[COLOR'+TEXTCOL+']'+name +'[/COLOR]',(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,image,'','')

	
#-------------------------------------Film Trailers----------------------------

def Film_Trailers(url):

    film_list=[]
    HTML = OPEN_URL(url)
    match = re.compile('<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>',re.DOTALL).findall(HTML)	
    for url2,img,name,added in match:
        name = ('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#039;','\'').replace('&','&').replace('&quot;','"')
        HTML2 = OPEN_URL(url2)
        match2 = re.compile('<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>',re.DOTALL).findall(HTML2)
        for playlink, description in match2:
            match_description = re.compile('<p>(.+?)</p>',re.DOTALL).findall(str(description))
            for desc in match_description:
                if name in film_list:
                    pass
                else:
                    addDir2(name,playlink,8043,img,img,desc)
                    setView('movies', 'INFO')
                    film_list.append(name)
#-------------------------------------Youtube-----------------------------------
#elif mode == 10064: Youtube_search()
def REQUESTS(url):
    html=OPEN_CAT(url)
    match=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(html)
    for url,iconimage,desc,fanart,name in match:
        addDir(name,url,10065,iconimage,fanart,desc)
    setView('movies', 'INFO')

def Youtube_search():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = 'https://www.youtube.com/results?search_query=' + (Search_Name).replace(' ','+')
    Search_Title = Search_Clean_Name.lower()
    HTML = OPEN_URL(Search_Title)
    match = re.compile('<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>',re.DOTALL).findall(HTML)
    next = re.compile('<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>').findall(HTML)
    for url in next:
        url = 'https://www.youtube.com' + url
        addDir('[COLOR'+TEXTCOL+'] NEXT [/COLOR]',url,10065,ART + 'Next.png',FANART,'')
    for img,url,name,length,description in match:
        youtube_list.append(name)    
        setView('tvshows', 'INFO')
        image = 'http:' + (img).replace('https:','')
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + image
        url = 'http://www.youtube.com' + url
        addDir2('[COLORred]'+length +'[/COLOR]'+'[COLOR'+TEXTCOL+']'+name +'[/COLOR]',(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,image,image,description)
    else:
        match = re.compile('<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>',re.DOTALL).findall(HTML)
        for img,url,name,length in match:
            print 'im doing it'		
            setView('tvshows', 'INFO')
            image = 'http:' + (img).replace('https:','')
            url = 'http://www.youtube.com' + url
            if '&' in url:
				print ' i got here'
				HTML = OPEN_URL(url)
				block = re.compile('<li class="yt-uix-scroller-scroll-unit "(.+?)</li>',re.DOTALL).findall(HTML)
				for block in block:
					name = re.compile('data-video-title="([^"]*)"').findall(str(block))
					for name in name:
						name = ('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&quot;','').replace('&#39;','\'').replace('&','&')
					url = re.compile('<a href="/w(.+?)&').findall(str(block))
					for url in url:
						url = 'https://www.youtube.com/w' + url
					image = re.compile('<img.+?="([^"]*)"').findall(str(block))
					for image in image:
						image = 'http:'+image
					addDir2('[COLORred]'+length +'[/COLOR]'+'[COLOR'+TEXTCOL+']'+name +'[/COLOR]',(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,image,FANART,'')
            elif name in youtube_list:
                pass
            elif 'user' in url  or 'elete' in name:
                pass
            elif 'hannel' in url:
				print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
				HTML = OPEN_URL(url)
				channel = re.compile('data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>',re.DOTALL).findall(HTML)
				for img,url,name in channel:
					if 'outube' in url or 'list' in url:
						pass
					elif 'atch' in url:
						url = (url).replace('/watch?v=','')
						addDir2('[COLORred]'+length +'[/COLOR]'+'[COLOR'+TEXTCOL+']'+name +'[/COLOR]',(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,'http:'+img,'http:'+img,'')					
					else:
						pass
            else:
				addDir2('[COLORred]'+length +'[/COLOR]'+'[COLOR'+TEXTCOL+']'+name +'[/COLOR]',(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,image,image,'')

def youtube_next(url):
    HTML = OPEN_URL(url)
    match = re.compile('<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>',re.DOTALL).findall(HTML)
    next = re.compile('<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>').findall(HTML)
    for url in next:
        url = 'https://www.youtube.com' + url
        addDir('[COLOR'+TEXTCOL+'] NEXT [/COLOR]',url,10065,ART + 'Next.png',FANART,'')
    for img,url,name,length,description in match:
        youtube_list.append(name)    
        setView('tvshows', 'INFO')
        image = 'http:' + (img).replace('https:','')
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + image
        url = 'http://www.youtube.com' + url
        addDir2('[COLORred]'+length +'[/COLOR]'+'[COLOR'+TEXTCOL+']'+name +'[/COLOR]',(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,image,image,description)
    else:
        match = re.compile('<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>',re.DOTALL).findall(HTML)
        for img,url,name,length in match:    
            setView('tvshows', 'INFO')
            image = 'http:' + (img).replace('https:','')
            url = 'http://www.youtube.com' + url
            if '&' in url:
				HTML = OPEN_URL(url)
				block = re.compile('<li class="yt-uix-scroller-scroll-unit "(.+?)</li>',re.DOTALL).findall(HTML)
				for block in block:
					name = re.compile('data-video-title="([^"]*)"').findall(str(block))
					for name in name:
						name = ('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&quot;','').replace('&#39;','\'').replace('&','&')
					url = re.compile('<a href="/w(.+?)&').findall(str(block))
					for url in url:
						url = 'https://www.youtube.com/w' + url
					image = re.compile('<img.+?="([^"]*)"').findall(str(block))
					for image in image:
						image = 'http:'+image
					addDir2('[COLORred]'+length +'[/COLOR]'+'[COLOR'+TEXTCOL+']'+name +'[/COLOR]',(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,image,FANART,'')
            elif name in youtube_list:  
                pass
            elif 'user' in url  or 'elete' in name:
                pass
            elif 'hannel' in url:
				print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
				HTML = OPEN_URL(url)
				channel = re.compile('data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>',re.DOTALL).findall(HTML)
				for img,url,name in channel:
					if 'outube' in url or 'list' in url:
						pass
					elif 'atch' in url:
						url = (url).replace('/watch?v=','')
						addDir2('[COLORred]'+length +'[/COLOR]'+'[COLOR'+TEXTCOL+']'+name +'[/COLOR]',(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,'http:'+img,'http:'+img,'')					
					else:
						pass
            else:
				addDir2('[COLORred]'+length +'[/COLOR]'+'[COLOR'+TEXTCOL+']'+name +'[/COLOR]',(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,image,image,'')
###########################################################
##########################################################

def guidemenu():
	addDir2('[COLOR'+TEXTCOL+']Setup Tv Guide[/COLOR]','',100212,ART + 'linkchannels.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']Open Guide[/COLOR]','',100213,ART + 'TvGuide.png',FANART,'')

def ivueint():
	ivuesetup.iVueInt()
	
def pvrsetup():
	correctPVR()
	return
	
def correctPVR():

	addon = xbmcaddon.Addon('plugin.video.GenieTv')
	username_text = addon.getSetting(id='User')
	password_text = addon.getSetting(id='Pass')
	jsonSetPVR = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
	IPTVon 	   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
	nulldemo   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
	loginurl   = "http://piesustv"+DDNS+":8000/get.php?username=" + username_text + "&password=" + password_text + "&type=m3u_plus&output=ts"
	EPGurl     = "http://piesustv"+DDNS+":8000/xmltv.php?username=" + username_text + "&password=" + password_text + "&type=m3u_plus&output=ts"

	xbmc.executeJSONRPC(jsonSetPVR)
	xbmc.executeJSONRPC(IPTVon)
	xbmc.executeJSONRPC(nulldemo)
	
	moist = xbmcaddon.Addon('pvr.iptvsimple')
	moist.setSetting(id='m3uUrl', value=loginurl)
	moist.setSetting(id='epgUrl', value=EPGurl)
	moist.setSetting(id='m3uCache', value="false")
	moist.setSetting(id='epgCache', value="false")
	xbmc.executebuiltin("Container.Refresh")
def tvguide22():
	xbmc.executebuiltin('ActivateWindow(TVGuide)')

'''
	if xbmc.getCondVisibility('System.HasAddon(pvr.iptvsimple)') and xbmc.getCondVisibility('System.HasAddon(script.ivueguide)'):
		dialog = xbmcgui.Dialog().select('Select a TV Guide', ['PVR TV Guide','iVue TV Guide'])
		if dialog==0:
			xbmc.executebuiltin('ActivateWindow(TVGuide)')
		elif dialog==1:
			xbmc.executebuiltin('RunAddon(script.ivueguide)')
	elif not xbmc.getCondVisibility('System.HasAddon(pvr.iptvsimple)') and xbmc.getCondVisibility('System.HasAddon(script.ivueguide)'):
		xbmc.executebuiltin('RunAddon(script.ivueguide)')
	elif xbmc.getCondVisibility('System.HasAddon(pvr.iptvsimple)') and not xbmc.getCondVisibility('System.HasAddon(script.ivueguide)'):
		xbmc.executebuiltin('ActivateWindow(TVGuide)')
'''
##########################################################
#########################################################
def start():
	if U=="insert_username":
		user = userpopup()
		passw= passpopup()
		setSetting('User',user)
		setSetting('Pass',passw)
		xbmc.executebuiltin('Container.Refresh')
		auth = 'http://piesustv'+DDNS+':8000/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(user,passw)
		auth = OPEN_URL(auth)
		if auth == "":
			line1 = "[COLOR "+TEXTCOL+"]Incorrect Login Details[/COLOR]"
			line2 = "[COLOR "+TEXTCOL+"]Please Re-enter[/COLOR]" 
			line3 = "" 
			xbmcgui.Dialog().ok('Attention', line1, line2, line3)
			start()
		else:
			line1 = "[COLOR "+TEXTCOL+"]Login Successful[/COLOR]"
			line2 = "[COLOR "+TEXTCOL+"]Welcome to GenieTv[/COLOR]"
			line3 = ('[COLOR '+TEXTCOL+']%s[/COLOR]'%user)
			xbmcgui.Dialog().ok('GenieTv', line1, line2, line3)
			xbmc.executebuiltin('Container.Refresh')
			MenLiveTV()	
	else:
		MenLiveTV()
def userpopup():
	kb =xbmc.Keyboard ('', 'heading', True)
	kb.setHeading('Enter Username')
	kb.setHiddenInput(False)
	kb.doModal()
	if (kb.isConfirmed()):
		text = kb.getText()
		return text
	else:
		return False

		
def passpopup():
	kb =xbmc.Keyboard ('', 'heading', True)
	kb.setHeading('Enter Password')
	kb.setHiddenInput(False)
	kb.doModal()
	if (kb.isConfirmed()):
		text = kb.getText()
		return text
	else:
		return False
def checkexp():
    loginurl   = "http://piesustv"+DDNS+":8000//get.php?username=" + U + "&password=" + Pass + "&type=m3u_plus&output=ts"
    try:
        connection = urllib2.urlopen(loginurl)
        print connection.getcode()
        connection.close()
        #playlist found, user active & login correct, proceed to addon
        pass
        
    except urllib2.HTTPError, e:
        print e.getcode()
        Dialog.ok("[COLORorangered]Expired Account[/COLOR]",'[COLOR '+TEXTCOL+']You cannot use this service with an expired account[/COLOR]',' ','[COLOR '+TEXTCOL+']Please check your account information[/COLOR]')
        sys.exit(1)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
def MenLiveTV():
    Repo_Check()
#    if ADDON.getSetting('G-tv')=='true':
#        addDir('[COLOR'+TEXTCOL+']G-Tv PRIVATE LIST[/COLOR]','',10058,ART+'GTVIPTV.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']My Account[/COLOR]','http://piesustv'+DDNS+':8000/panel_api.php?username='+U+'&password='+Pass,60004,ART + 'Sport.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']G-Tv Channels[/COLOR]',(Decode('aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=')),60001,ART+'GTV.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Live Sport On G-Tv[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=')),7080,ART + 'Sport.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Guide Menu[/COLOR]','',100211,ART + 'TvGuide.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']CatchUp Tv[/COLOR]','',90026,ART + 'Sport.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']VOD Lists[/COLOR]','',40000,ART+'Vod_Lists.png',FANART,'')
#    if ADDON.getSetting('TV GUIDE')=='true':
#        addDir2('[COLOR'+TEXTCOL+']TV GUIDE[/COLOR]','',10063,ART+'TvGuide.png',FANART,'')
#    addDir2('[COLOR'+TEXTCOL+']Link GTV to Guide[/COLOR]','',4010,ART+'linkchannels.png',FANART,'')

def GetTiny():
	xbmc.executebuiltin("ActivateWindow(busydialog)")
	m3u  = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D'+U+'%26password%3D'+Pass+'%26type%3Dm3u_plus%26output%3Dts'
	epg  = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D'+U+'%26password%3D'+Pass
	auth = 'http://piesustv'+DDNS+':8000/enigma2.php?username='+U+'&password='+Pass+'&type=get_vod_categories'
	auth = OPEN_URL(auth)
	if not auth=="":
		request  = 'https://tinyurl.com/create.php?source=indexpage&url='+m3u+'&submit=Make+TinyURL%21&alias='
		xbmc.log(str(request))
		request2 = 'https://tinyurl.com/create.php?source=indexpage&url='+epg+'&submit=Make+TinyURL%21&alias='
		m3u = OPEN_URL(request)
		epg = OPEN_URL(request2)
		xbmc.log(str(epg))
		shortm3u = regex_from_to(m3u,'<div class="indent"><b>','</b>')
		shortepg = regex_from_to(epg,'<div class="indent"><b>','</b>')
		xbmc.executebuiltin("Dialog.Close(busydialog)")
		xbmcgui.Dialog().ok('[COLOR'+TEXTCOL+']GenieTv[/COLOR]','[COLORsteelblue]PLAYLIST URL: [/COLOR]%s'%shortm3u,'','[COLORsteelblue]EPG URL: [/COLOR]%s'%shortepg)
	else:
		return
def VOD_Menu():
	checkexp()
	addDirFolder(('[COLORsteelblue]All Vod[/COLOR]').replace('\/',' - '),APIkey+'&action=get_vod_streams',40001,ART+'Vod_Lists.png',FANART,'')
	HTML = OPEN_URL(VODcats)
	match = re.compile('"category_id":"([^"]*)","category_name":"([^"]*)"',re.DOTALL).findall(HTML)
	for url,name in match:
		addDir(('[COLORsteelblue]'+name+'[/COLOR]').replace('\/',' - '),url,40001,ART+'Vod_Lists.png',FANART,'')
def Get_VOD_playlinks(url):
	open = OPEN_URL(VODlist+url)
	all_cats = regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		if '<playlist_url>' in open:
			name = regex_from_to(a,'<title>','</title>')
			url1  = regex_from_to(a,'<playlist_url>','</playlist_url>').replace('<![CDATA[','').replace(']]>','')
			addDir(str(base64.b64decode(name)).replace('?',''),url1,40001,icon,fanart,'')
		else:
			if xbmcaddon.Addon().getSetting('meta') == 'true':
				try:
					name = regex_from_to(a,'<title>','</title>')
					name = base64.b64decode(name)
					thumb= regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
					url  = regex_from_to(a,'<stream_url>','</stream_url>').replace('<![CDATA[','').replace(']]>','')
					desc = regex_from_to(a,'<description>','</description>')
					desc = base64.b64decode(desc)
					plot = regex_from_to(desc,'PLOT:','\n')
					cast = regex_from_to(desc,'CAST:','\n')
					ratin= regex_from_to(desc,'RATING:','\n')
					year = regex_from_to(desc,'RELEASEDATE:','\n').replace(' ','-')
					year = re.compile('-.*?-.*?-(.*?)-',re.DOTALL).findall(year)
					runt = regex_from_to(desc,'DURATION_SECS:','\n')
					genre= regex_from_to(desc,'GENRE:','\n')
					addDirMeta(str(name).replace('[/COLOR].','.[/COLOR]'),url,222,thumb,fanart,plot,str(year).replace("['","").replace("']",""),str(cast).split(),ratin,runt,genre)
				except:pass
				xbmcplugin.setContent(int(sys.argv[1]), 'movies')
			else:
				name = regex_from_to(a,'<title>','</title>')
				name = base64.b64decode(name)
				thumb= regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
				url  = regex_from_to(a,'<stream_url>','</stream_url>').replace('<![CDATA[','').replace(']]>','')
				desc = regex_from_to(a,'<description>','</description>')
				addDir2(name,url,222,thumb,fanart,base64.b64decode(desc))
##########################################
Guide = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv/resources/catchup', 'guide.xml'))
GuideLoc = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv/resources/catchup', 'g'))

def catchup2():
    loginurl   = "http://piesustv"+DDNS+":8000/get.php?username=" + U + "&password=" + Pass + "&type=m3u_plus&output=ts"
    try:
        connection = urllib2.urlopen(loginurl)
        print connection.getcode()
        connection.close()
        #playlist found, user active & login correct, proceed to addon
        pass
        
    except urllib2.HTTPError, e:
        print e.getcode()
        Dialog.ok("[COLOR white]Expired Account[/COLOR]",'[COLOR white]You cannot use this service with an expired account[/COLOR]',' ','[COLOR white]Please check your account information[/COLOR]')
        sys.exit(1)
        xbmc.executebuiltin("Dialog.Close(busydialog)")

    url = "http://piesustv"+DDNS+":8000/xmltv.php?username=%s&password=%s"%(U,Pass)
    DownloaderClass(url,GuideLoc + "uide.xml")
    
    f = open(Guide, 'r+')
    input = open(Guide).read().decode('UTF-8')
    output = unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')
    f.write(output)
    f.truncate()
    f.close()
    listcatchup()
		
def listcatchup():
	open = OPEN_URL(panel_api)
	all  = regex_get_all(open,'{"num','direct')
	for a in all:
		if '"tv_archive":1' in a:
			name = regex_from_to(a,'"epg_channel_id":"','"')
			thumb= regex_from_to(a,'"stream_icon":"','"').replace('\/','/')
			id   = regex_from_to(a,'stream_id":"','"')
			name = name.replace('ENT:','[COLOR blue]ENT:[/COLOR]').replace('DOC:','[COLOR blue]DOC:[/COLOR]').replace('MOV:','[COLOR blue]MOV:[/COLOR]').replace('SSS:','[COLOR blue]SSS[/COLOR]').replace('BTS:','[COLOR blue]BTS:[/COLOR]').replace('TEST','[COLOR blue]TEST[/COLOR]').replace('Install','[COLOR blue]Install[/COLOR]').replace('24/7','[COLOR blue]24/7[/COLOR]').replace('INT:','[COLOR blue]INT:[/COLOR]').replace('DE:','[COLOR blue]DE:[/COLOR]').replace('FR:','[COLOR blue]FR:[/COLOR]').replace('PL:','[COLOR blue]PL:[/COLOR]').replace('AR:','[COLOR blue]AR:[/COLOR]').replace('LIVE:','[COLOR blue]LIVE:[/COLOR]').replace('ES:','[COLOR blue]ES:[/COLOR]').replace('IN:','[COLOR blue]IN:[/COLOR]').replace('PK:','[COLOR blue]PK:[/COLOR]')
			addDir(name,id,90027,thumb,fanart,name)
			

def tvarchive(name,url,description):
    id = url
    name = str(name.replace('[COLOR blue]ENT:[/COLOR]','ENT:').replace('[COLOR blue]DOC:[/COLOR]','DOC:').replace('[COLOR blue]MOV:[/COLOR]','MOV').replace('[COLOR blue]SSSS[/COLOR]','SSS:').replace('[COLOR blue]BTS:[/COLOR]','BTS:').replace('[COLOR blue]INT:[/COLOR]','INT:').replace('[COLOR blue]DE:[/COLOR]','DE:').replace('[COLOR blue]FR:[/COLOR]','FR:').replace('[COLOR blue]PL:[/COLOR]','PL:').replace('[COLOR blue]AR:[/COLOR]','AR:').replace('[COLOR blue]LIVE:[/COLOR]','LIVE:').replace('[COLOR blue]ES:[/COLOR]','ES:').replace('[COLOR blue]IN:[/COLOR]','IN:').replace('[COLOR blue]PK:[/COLOR]','PK'))
    filename = open(Guide)
    tree = ElementTree.parse(filename)
    pony = "apples"
    import datetime as dt
    from datetime import time
    date3 = datetime.now() - timedelta(days=5)
    date = str(date3)
    now = str(datetime.now()).replace('-','').replace(':','').replace(' ','')
    programmes = tree.findall("programme")
    for programme in programmes:
        if name in programme.attrib.get('channel'):
            showtime = programme.attrib.get('start')
            head, sep, tail = showtime.partition(' +')
            date = str(date).replace('-','').replace(':','').replace(' ','')
            year, month, day = showtime.partition('2017')
            kanalinimi = programme.find('title').text + showtime
            day = day[:-6]
            if head > date:
                if head < now:
                    head2 = head
                    head2 = head2[:4] + '/' + head2[4:]
                    head = head[:4] + '-' + head[4:]
                    head2 = head2[:7] + '/' + head2[7:]
                    head = head[:7] + '-' + head[7:]
                    head2 = head2[:10] + ' - ' + head2[10:]
                    head = head[:10] + ':' + head[10:]
                    head2 = head2[:15] + ':' + head2[15:]
                    head = head[:13] + '-' + head[13:]
                    head2 = head2[:-2]
                    head = head[:-2]
                    poo1 = ("http://piesustv"+DDNS+":8000/streaming/timeshift.php?username=%s&password=%s&start="+ str(head)+"&duration=240"+"&stream=%s")%(U,Pass,id)
                    pony = poo1 + str(head) + "&duration=240"
                    head2 = '[COLOR blue]%s - [/COLOR]'%head2 
                    kanalinimi = str(head2)+ programme.find('title').text
                    desc  = programme.find('desc').text
                    addDir2(kanalinimi,poo1,222,ART+'GTV.png',FANART,desc)
def stream_video(url):
	url = str(url).replace('USERNAME',U).replace('PASSWORD',Pass)
	liz = xbmcgui.ListItem('', iconImage='DefaultVideo.png', thumbnailImage=ICON)
	liz.setInfo(type='Video', infoLabels={'Title': '', 'Plot': ''})
	liz.setProperty('IsPlayable','true')
	liz.setPath(str(url))
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)	
def DownloaderClass(url, dest):
    dp = xbmcgui.DialogProgress()
    dp.create('Fetching latest Catch Up',"Fetching latest Catch Up...",' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            mbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % (currently_downloaded)
            e = '[COLOR white]Speed:  %.02f Mb/s ' % mbps_speed  + '[/COLOR]'
            dp.update(percent, mbs, e)
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled():
            dialog = xbmcgui.Dialog()
            dialog.ok("GenieTv", 'The download was cancelled.')
				
            sys.exit()
            dp.close()
########################
def Check_Donator_Password():
    if Pass == 'insert_password':
        Dialog.ok('[COLOR'+TEXTCOL+']G-Tv Login[/COLOR]','You need to set username and password to access this','These are unique and provided upon purchase','from [COLOR'+TEXTCOL+']http://GenieTv.co.uk[/COLOR]')        
        ADDON.openSettings(sys.argv[0])
    else:
        CHECKAccDetails()
#        check_password = open(Addons_ini)
#        match = re.compile('plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F').findall(str(check_password))
#        for username,password in match:
#            if username == 'needs replacing' or password == 'needs replacing':
#                print_addons_ini()	
#    	addDir('[COLOR'+TEXTCOL+']G-Tv PRIVATE LIST[/COLOR]',(Decode('aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdG5ldy5tM3U=')),7080,ART+'PrivateList.png',FANART,'')
#        addDir('[COLOR'+TEXTCOL+']My Account[/COLOR]','http://piesustv'+DDNS+':8000/panel_api.php?username='+U+'&password='+Pass,60004,ART + 'Sport.png',FANART,'')
#        addDir('[COLOR'+TEXTCOL+']G-Tv Channels[/COLOR]',(Decode('aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=')),60001,ART+'GTV.png',FANART,'')
def CHECKAccDetails():
        link = OPEN_URL('http://piesustv'+DDNS+':8000/panel_api.php?username='+U+'&password='+Pass)
        match=re.compile('"exp_date":"(.+?)"').findall(link)
        for url in match:
                dt = datetime.fromtimestamp(float(match[0]))
                dt.strftime('%Y-%m-%d %H:%M:%S')
                if now <= dt <= now + timedelta(hours=24):
                    Dialog.ok('[COLORred]Your Account Expires Today[/COLOR]','[COLOR'+TEXTCOL+']If You Wish To Continue With Your Subscription[/COLOR]','','[COLOR'+TEXTCOL+']Please Visit [COLORred]GenieTv.co.uk[COLOR'+TEXTCOL+'] To Purchase A licence[/COLOR]')        
def MyAccDetails(url):
        link = OPEN_URL(url)
        match=re.compile('"username":"(.+?)"').findall(link)
        matchp=re.compile('"password":"(.+?)"').findall(link)
        match1=re.compile('"status":"(.+?)"').findall(link)
        match2=re.compile('"exp_date":"(.+?)"').findall(link) 	
        match3=re.compile('"active_cons":"(.+?)"').findall(link)
        match4=re.compile('"created_at":"(.+?)"').findall(link)
        match5=re.compile('"max_connections":"(.+?)"').findall(link)
        match6=re.compile('"is_trial":"1"').findall(link)
        match7=re.compile('"is_trial":"0"').findall(link)
        ip        = getlocalip()
        extip     = getexternalip()
        for url in match:
                addDir4('[COLOR'+TEXTCOL+']My GTV Account Information[/COLOR]','','',ART +'MyAcc.png')
                addDir4('[COLOR'+TEXTCOL+']Username:[/COLOR]  %s'%(url),'','',ART + 'MyAcc.png')
        for url in matchp:
                addDir4('[COLOR'+TEXTCOL+']Password:[/COLOR]  %s'%(url),'','',ART + 'MyAcc.png')
        for url in match1:
                addDir4('[COLOR'+TEXTCOL+']Status:[/COLOR]  %s'%(url),'','',ART + 'MyAcc.png')
        for url in match4:
                dt = datetime.fromtimestamp(float(match4[0]))
                dt.strftime('%Y-%m-%d %H:%M:%S')
                addDir4('[COLOR'+TEXTCOL+']Created:[/COLOR]  %s'%(dt),'','',ART +'MyAcc.png')
        for url in match2:
                dt = datetime.fromtimestamp(float(match2[0]))
                dt.strftime('%Y-%m-%d %H:%M:%S')
                if now <= dt <= now + timedelta(hours=24):
                    addDir4('[COLORred]Expires Today[/COLOR]','','',ART +'MyAcc.png')
                addDir4('[COLOR'+TEXTCOL+']Expires:[/COLOR]  %s'%(dt),'','',ART +'MyAcc.png')
        for url in match3:
                addDir4('[COLOR'+TEXTCOL+']Active Connection:[/COLOR]  %s'%(url),'','',ART +'MyAcc.png')
        for url in match5:
                addDir4('[COLOR'+TEXTCOL+']Max Connection:[/COLOR]  %s'%(url),'','',ART +'MyAcc.png') 
        for url in match6:
                addDir4('[COLOR'+TEXTCOL+']Trial:[/COLOR] Yes','','',ART +'MyAcc.png')
        for url in match7:
                addDir4('[COLOR'+TEXTCOL+']Trial:[/COLOR] No','','',ART +'MyAcc.png')
        addDir2('[COLOR'+TEXTCOL+']Get Short Links[/COLOR]','',100214,ART+'shortlinks.png',FANART,'')
        addDir('[COLOR'+TEXTCOL+']Local IP Address:[/COLOR] '+ip,'','',ART+'CheckMyIP.png',FANART,'')
        addDir('[COLOR'+TEXTCOL+']External IP Address:[/COLOR] '+extip,'','',ART+'CheckMyIP.png',FANART,'')

        addDir4('[COLOR'+TEXTCOL+']Sign up[/COLOR]','',50006,'')

def ReCreate_Addon_ini():
    Dialog.ok('[COLOR=white]ReCreate Addons.ini[/COLOR]','If it doesnt work ensure login details are correct and retry','','This will allow access to streams in guide without linking to favourites')        
    xbmc.executebuiltin("XBMC.RunScript("+reset_database+")")
    print_addons_ini()
    Dialog.ok('[COLOR=yellow]Done[/COLOR]','Done','Easy as that','Now Go to guide and it should link your GTV streams')
##########################################################################################################################################
def decode_base6422(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)
def regex_from_to(text, from_string, to_string, excluding=True):
	if excluding:
		try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
		except: r = ''
	else:
		try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
		except: r = ''
	return r


def regex_get_all(text, start_with, end_with):
	r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
	return r
def getlocalip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 0))
	s = s.getsockname()[0]
	return s
			
def getexternalip():
	open = OPEN_URL('http://canyouseeme.org/')
	ip = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',open)
	return str(ip.group())
APIkey= 'http://piesustv'+DDNS+':8000/player_api.php?username=%s&password=%s'%(U,Pass)
panel_api    = 'http://piesustv'+DDNS+':8000/panel_api.php?username=%s&password=%s'%(U,Pass)
PlayMov= 'http://piesustv'+DDNS+':8000/movie/%s/%s/'%(U,Pass)
PlayLive= 'http://piesustv'+DDNS+':8000/live/%s/%s/'%(U,Pass)
StreamCats= '&action=get_live_categories'
Streams= 'http://piesustv'+DDNS+':8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id='%(U,Pass)
VODcats= 'http://piesustv'+DDNS+':8000/player_api.php?username=%s&password=%s&action=get_vod_categories'%(U,Pass)
#VODcats= 'http://piesustv'+DDNS+':8000/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(U,Pass)
VODlist= 'http://piesustv'+DDNS+':8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id='%(U,Pass)
nandn= 'http://piesustv'+DDNS+':8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id='%(U,Pass)
livcat= 'http://piesustv'+DDNS+':8000/enigma2.php?username=%s&password=%s&type=get_live_categories'%(U,Pass)
EPGURL = "http://piesustv"+DDNS+":8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id="%(U,Pass)
		
def Streams_Menu():
	checkexp()
	open = OPEN_URL(livcat)
	all_cats = regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		name = regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		url1  = regex_from_to(a,'<playlist_url>','</playlist_url>').replace('<![CDATA[','').replace(']]>','')
		addDir('[COLORsteelblue]'+name+'[/COLOR]',url1,60003,ART+'GTV.png',FANART,'')

def Get_Ultimate_playlinks_data(url):
	open = OPEN_URL(EPGURL+url)
	all_cats = regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		name = regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		xbmc.log(str(name))
		thumb= regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
		url1  = regex_from_to(a,'<stream_url>','</stream_url>').replace('<![CDATA[','').replace(']]>','')
		desc = regex_from_to(a,'<description>','</description>')
		desc = base64.b64decode(desc)
		T='('
		TT=')'
		addDir2(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('min','min[COLORsteelblue]').replace('+','[COLORorangered]+'),url1,222,thumb,fanart,('[COLOR'+TEXTCOL+']'+desc+'[/COLOR]').replace('<','').replace(TT,'[COLORsteelblue]').replace(T,'[COLORorangered]'))

def Get_Ultimate_playlinks(url):
    url=url
    HTML = OPEN_URL(Streams+url)
    match = re.compile('"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg',re.DOTALL).findall(HTML)
    for name,type,url2,icon in match:
        url3 = (PlayLive+url2+'.m3u8').strip()
        addDir2('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url3,222,(icon).replace('\/','/')+'jpg',FANART,type)
        setView('tvshows', 'Media Info 3')	
def GRABDATA(url,name,img):
	img = img
	name = name
	url = url
	HTML = OPEN_URL('http://piesustv'+DDNS+':8000/xmltv.php?username='+U+'&password='+Pass)
	match = re.compile('channel="([^"]*)">.+?<title>(.+?)</title>',re.DOTALL).findall(HTML)
	for name2,show in match:
		if name == name2:
			addDir2((''+name+'').replace('_',' ')+show,(url).strip(),222,img,img,'')
		else:
			addDir2((''+name+'').replace('_',' '),(url).strip(),222,img,img,'')
def Live_Events(name):
    seperator = name
    HTML = OPEN_URL('http://piesustv'+DDNS+':8000/get.php?username='+U+'&password='+Pass+'&type=m3u_plus&output=mpegts')
    match = re.compile('#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n').findall(HTML)
    for name,img,url in match:
        url = (url).replace('.ts','.m3u8')
        addDir2((''+name+'').replace('_',' '),(url).strip(),222,img,img,'')
    else:
        addDir2('[COLORred]Streams will appear here for live events when available[/COLOR]','',222,'','','')
#def TvGuide():
#	try:
#		w = gui.TVGuide()
#		w.doModal()
#		del w
#
#	except:
#		import sys
#		import traceback as tb
#		(etype, value, traceback) = sys.exc_info()
#		tb.print_exception(etype, value, traceback)

def BackUp_My_Build():
    addDir('Full Backup','',10061,ART + 'FullBackUp.png',FANART,'Back Up Your Full System')
    if os.path.exists(GENIE_FAVS):
        addDir('Backup Genie Favourites',url,10062,ART + 'BackupGenieFavourites.png',FANART,'Back Up Your favourites')	    
    if os.path.exists(IVUE):
        addDir('Backup Ivue Config',IVUE,10062,ART + 'BackUpIvueConfig.png',FANART,'Back Up Your master.db')	    
    if os.path.exists(FAVS):
        addDir('Backup Kodi Favourites',FAVS,10062,ART + 'BackKodiFavourites.png',FANART,'Back Up Your favourites.xml')
#---------------------------------------------------------------------------------------------------
#Function to restore a zip file

zip =  ADDON.getSetting('zip')
USB =  xbmc.translatePath(os.path.join(zip))
def Check_Download_Path():
    path = xbmc.translatePath(os.path.join(zip,'testCBFolder'))
    if not os.path.exists(zip):
        Dialog.ok('[COLOR=white]GenieTv[/COLOR]','The download location you have stored does not exist .\nPlease update the addon settings and try again.','','')        
        ADDON.openSettings(sys.argv[0])

#---------------------------------------------------------------------------------------------------
#Function to restore a backup xml file (guisettings, sources, RSS)
def Restore_Backup_XML(name,url,description):
    if 'Backup' in name:
        if 'Genie' in name:
		    url = GENIE_FAVS
        elif 'Ivue' in name:
		    url = IVUE
        elif 'Kodi' in name:
		    url = FAVS
        Check_Download_Path()
        TO_READ   = open(url).read()
        TO_WRITE  = os.path.join(USB,description.split('Your ')[1])
        f = open(TO_WRITE, mode='w')
        f.write(TO_READ)
        f.close() 
    else:
        if 'guisettings.xml' in description:
            a = open(os.path.join(USB,description.split('Your ')[1])).read()
            r='<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>'% skin
            match=re.compile(r).findall(a)
            for type,string,setting in match:
                setting=setting.replace('&quot;','') .replace('&','&') 
                xbmc.executebuiltin("Skin.Se	t%s(%s,%s)"%(type.title(),string,setting))  
        else:    
            TO_WRITE   = os.path.join(url)
            TO_READ  = open(os.path.join(USB,description.split('Your ')[1])).read()
            f = open(TO_WRITE, mode='w')
            f.write(TO_READ)
            f.close()  
    Dialog.ok("[COLOR=white]GenieTv[/COLOR]", "", 'All Done !','')
		
		
#---------------------------------------------------------------------------------------------------
#Create a community (universal) backup - this renames paths to special:// and removes unwanted folders
def Community_Backup():
    guisuccess=1
    Check_Download_Path()
    fullbackuppath = xbmc.translatePath(os.path.join(USB,'Build Backup','Full Backup',''))
    myfullbackup = xbmc.translatePath(os.path.join(USB,'Build Backup','my_full_backup.zip'))
    myfullbackupGUI = xbmc.translatePath(os.path.join(USB,'Build Backup','my_full_backup_GUI_Settings.zip'))
    if not os.path.exists(fullbackuppath):
        os.makedirs(fullbackuppath)
    vq = Dialog.input('Enter a name for this backup', type=xbmcgui.INPUT_ALPHANUM)
    if ( not vq ): return False, 0
    title = vq
    backup_zip = xbmc.translatePath(os.path.join(fullbackuppath,title+'.zip'))
    exclude_dirs_full =  ['plugin.video.GenieTv']
    exclude_files_full = ["xbmc.log","xbmc.old.log","kodi.log","kodi.old.log",'.DS_Store','.setup_complete','XBMCHelper.conf']
    exclude_dirs =  ['plugin.video.GenieTv', 'repository.origin','cache', 'system', 'Thumbnails', "peripheral_data",'library','keymaps']
    exclude_files = ["xbmc.log","xbmc.old.log","kodi.log","kodi.old.log","Textures13.db",'.DS_Store','.setup_complete','XBMCHelper.conf', 'advancedsettings.xml']
    message_header = "Creating full backup of existing build"
    message_header2 = "Creating Community Build"
    message1 = "Archiving..."
    message2 = ""
    message3 = "Please Wait"
    Archive_Tree(HOME, backup_zip, message_header2, message1, message2, message3, exclude_dirs, exclude_files)  
    time.sleep(1)
    GUIname = xbmc.translatePath(os.path.join(fullbackuppath, title+'_guisettings.zip'))
    zf = zipfile.ZipFile(GUIname, mode='w')
    try:
        zf.write(xbmc.translatePath(os.path.join(HOME,'userdata','profiles.xml')), 'profiles.xml', zipfile.ZIP_DEFLATED) #Copy profiles.xml
    except: pass
    zf.close()
    if guisuccess == 0:
        Dialog.ok("FAILED!", 'The guisettings.xml file could not be found on your', 'system, please reboot and try again.', '')
    else:
        Dialog.ok("SUCCESS!", 'You Are Now Backed Up. If you\'d like to share this build with', 'the community please post details on the forum at', '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]')
        Dialog.ok("Build Locations", 'Full Backup (only used to restore on this device): [COLOR=yellow]'+myfullbackup, '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]'+backup_zip+'[/COLOR]')

def Archive_Tree(sourcefile, destfile, message_header, message1, message2, message3, exclude_dirs, exclude_files):
    zipobj = zipfile.ZipFile(destfile , 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(sourcefile)
    for_progress = []
    ITEM =[]
    dp.create(message_header, message1, message2, message3)
    for base, dirs, files in os.walk(sourcefile):
        for file in files:
            ITEM.append(file)
    N_ITEM =len(ITEM)
    for base, dirs, files in os.walk(sourcefile):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        files[:] = [f for f in files if f not in exclude_files]
        for file in files:
            for_progress.append(file) 
            progress = len(for_progress) / float(N_ITEM) * 100  
            dp.update(int(progress),"Backing Up",'[COLOR yellow]%s[/COLOR]'%file, 'Please Wait')
            fn = os.path.join(base, file)
            if not 'temp' in dirs:
                if not 'plugin.program.originwizard' in dirs:
                   import time
                   FORCE= '01/01/1980'
                   FILE_DATE=time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(fn)))
                   if FILE_DATE > FORCE:
                       zipobj.write(fn, fn[rootlen:])  
    zipobj.close()
    dp.close()
		
	
def SCOOBYCATS():
    Repo_Check()
    addDir('[COLOR'+TEXTCOL+']SCOOBY STREAMS[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==')),1016,ART+'scoob.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']SCOOBY SCRAPES[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==')),1024,ART+'scoob.png',FANART,'')

	
def Search_Lists():
	Repo_Check()
	choices = ['[COLOR'+TEXTCOL+']SEARCH MOVIES[/COLOR]','[COLOR'+TEXTCOL+']SEARCH SERIES[/COLOR]','[COLOR'+TEXTCOL+']SEARCH CARTOONS[/COLOR]','[COLOR'+TEXTCOL+']SEARCH YOUTUBE[/COLOR]']
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Search Genie[/COLOR]', choices)
	if choice==0:
		Search_Films_Lists()
	if choice==1:
		Search_Tv_Lists()
	if choice==2:
		Origin_Cart_Search()
	if choice==3:
		Youtube_search()
#    if ADDON.getSetting('YOUTUBE')=='true':
#        addDir('[COLOR'+TEXTCOL+']SEARCH YOUTUBE[/COLOR]',str(BASEURL),10064,ART+'SeachYouTube.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']SEARCH MOVIES[/COLOR]',str(BASEURL),9001,ART+'MOVIESv.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']SEARCH SERIES[/COLOR]',str(BASEURL),9002,ART+'TVSHOWSv.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']SEARCH CARTOONS[/COLOR]','',10005,ART + 'ORIGINCARTOON',FANART,'')

	#    addDir('[COLOR'+TEXTCOL+']SEARCH LiveTv[/COLOR]',str(BASEURL),9003,ART+'livetv.png',FANART,'')


def MenMusic():
	Repo_Check()
	if ADDON.getSetting('Simplify')=='true':
		choices = ['[COLOR'+TEXTCOL+']RaysRavers Radio[/COLOR]','[COLOR'+TEXTCOL+']ThunderStruck[/COLOR]','[COLOR'+TEXTCOL+']RadioNomy[/COLOR]','[COLOR'+TEXTCOL+']MUSIC CHANNELS[/COLOR]','[COLOR'+TEXTCOL+']UK RADIO[/COLOR]','[COLOR'+TEXTCOL+']WORLD RADIO[/COLOR]','[COLOR'+TEXTCOL+']CONCERTS[/COLOR]','[COLOR'+TEXTCOL+']MUSIC VIDEOS[/COLOR]','[COLOR'+TEXTCOL+']MUSIC[/COLOR]','[COLOR'+TEXTCOL+']MUSIC SEARCH[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Music[/COLOR]', choices)
		if choice==0:
			from imports.pyramid import pyramid;pyramid.SKindex_Raiz();xbmcplugin.endOfDirectory(int(sys.argv[1]))
		if choice==1:
			from imports.pyramid import pyramid;pyramid.SKindex_thunderstruck();xbmcplugin.endOfDirectory(int(sys.argv[1]))
		if choice==2:
			RadioNomy()
		if choice==3:
			ARCONAI2()
		if choice==4:
			RADIO2((Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=')))
		if choice==5:
			RADIO()
		if choice==6:
			WATCHCATS((Decode('aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=')))
		if choice==7:
			MUSICVIDS((Decode('aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==')))
		if choice==8:
			MUSIC1(str(BASEURL)+(Decode('L3ZvZC91cmxzL211c2ljLnBocA==')))
		if choice==9:
			Search_Music_Lists()
	else:
		addDir('[COLOR'+TEXTCOL+']RaysRavers Radio[/COLOR]',(Decode('aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=')),1125,ART+'Rays-Ravers.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']ThunderStruck[/COLOR]',(Decode('aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=')),1127,ART+'Thunder.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']RadioNomy[/COLOR]','',70001,ART+'RadioNomy.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']MUSIC CHANNELS[/COLOR]',str(BASEURL),30031,ART+'MusicChannels.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']UK RADIO[/COLOR]',(Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=')),10111113,ART+'UKRadio.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']WORLD RADIO[/COLOR]',str(BASEURL),1013,ART+'WorldRadio.png',FANART,'')
		if ADDON.getSetting('CONCERTS')=='true':
			addDir('[COLOR'+TEXTCOL+']CONCERTS[/COLOR]',(Decode('aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=')),7050,ART+'Concerts.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']MUSIC[/COLOR]',str(BASEURL),1030,ART+'MUSIC.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']MUSIC VIDEOS[/COLOR]',(Decode('aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==')),1032,ART+'MusicVideos.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']MUSIC[/COLOR]',str(BASEURL)+(Decode('L3ZvZC91cmxzL211c2ljLnBocA==')),1010,ART+'Music.png',FANART,'')
		addDir('[COLOR'+TEXTCOL+']MUSIC SEARCH[/COLOR]',str(BASEURL),1111,ART+'MusicSearch.png',FANART,'')
#		addDir('[COLOR'+TEXTCOL+']KODIBLE AUDIO BOOKS[/COLOR]','http://doremisa.com/audiobooks/',30000,ART+'KodibleAudioBooks.png',FANART,'')
#addDir('[COLOR'+TEXTCOL+']GenieTv MUSIC SCRAPE[/COLOR]',str(BASEURL),1010,ART+'vod.png',FANART,'')
	setView('movies', 'MAIN')
COLOR1         = 'white'
COLOR2         = 'gold'
def MAINTENANCE():
	Repo_Check()
	if Grab_Log(True) == False: kodilog = 0
	else: kodilog = errorChecking(Grab_Log(True), True, True)
	if Grab_Log(True, True) == False: kodioldlog = 0
	else: kodioldlog = errorChecking(Grab_Log(True,True), True, True)
	errorsinlog = int(kodilog) + int(kodioldlog)
	errorsfound = str(errorsinlog) + ' Error(s) Found' if errorsinlog > 0 else 'None Found'
	wizlogsize = ': [COLORsteelblue]Not Found[/COLOR]' if not os.path.exists(WIZLOG) else ": [COLORorangered]%s[/COLOR]" % convertSize(os.path.getsize(WIZLOG))
	sizepack   = getSize(PACKAGES)
	sizethumb  = getSize(THUMBS)
	sizecache  = getCacheSize()
	totalsize  = sizepack+sizethumb+sizecache
	ip        = getlocalip()
	extip     = getexternalip()
	addDir2('[COLOR'+TEXTCOL+']CLEAN UP:[COLORorangered] [B]%s[/B][/COLOR]' % convertSize(totalsize),'url',9666,ART+'MAIN5.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']KILL KODI[/COLOR]','',80000,ART+'KillKodi.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']SPEEDTEST[/COLOR]','',50004,ART+'Speedtest.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']VIEW LOG Errors:[COLORorangered] %s[/COLOR]' % (errorsfound),'',219999990,ART+'View-Log-File.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']VIEW LOG FILE[/COLOR]','',50000,ART+'View-Log-File.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']CLEAR LOG FILES: [COLORorangered]'+wizlogsize+'[/COLOR]','',219999991,ART+'View-Log-File.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']DELETE CACHE:[COLORorangered] [B]%s[/B][/COLOR]' % convertSize(sizecache),'url',14,ART+'DeleteCache.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']DELETE PACKAGES:[COLORorangered] [B]%s[/B][/COLOR]' % convertSize(sizepack),'url',6,ART+'DeletePackages.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']FORCE REFRESH[/COLOR]','url',10,ART+'ForceRefresh.png',FANART,'Force Refresh All Repos')
	addDir2('[COLOR'+TEXTCOL+']LAST RESORT FIX EMPTY REPOS[/COLOR]','url',9,ART+'1.jpg',FANART,'Fix Corrupt Database')
	addDir2('[COLOR'+TEXTCOL+']CLEAR THUBMNAILS:[COLORorangered] [B]%s[/B][/COLOR]' % convertSize(sizethumb),'url',219999992,ART+'DeleteTextureAndThumbnailFolderAndroidOnly.png',FANART,'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db')
	addDir2('[COLOR'+TEXTCOL+']Local IP Address:[COLORorangered] '+ip+'[/COLOR] ','','',ART+'CheckMyIP.png',FANART,'')
	addDir2('[COLOR'+TEXTCOL+']External IP Address:[COLORorangered] '+extip+'[/COLOR] ','','',ART+'CheckMyIP.png',FANART,'')
#	addDir('[COLOR'+TEXTCOL+']ADVANCED SETTINGS XML[/COLOR]',str(BASEURL),4,ART+'AdvancedSettingXML.png',FANART,'')
#	addDir('[COLOR'+TEXTCOL+']URL FIXES[/COLOR]',str(BASEURL),20,ART+'URLFixes.png',FANART,'')
	setView('movies', 'MAIN')
def ebi(proc):
	xbmc.executebuiltin(proc)

def refresh():
	ebi('Container.Refresh()')
def clearlogfiles():
	f = open(WIZLOG, 'w'); f.close(); LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Wizard Log Cleared![/COLOR]" % COLOR2)
	refresh()
##################################################################################################
def clearThumbs(type=None):
	latest = latestDB('Textures')
	if not type == None: choice = 1
	else: choice = Dialog.yesno(ADDONTITLE, '[COLOR %s]Would you like to delete the %s and Thumbnails folder?' % (COLOR2, latest), "They will repopulate on the next startup[/COLOR]", nolabel='[B][COLOR red]Don\'t Delete[/COLOR][/B]', yeslabel='[B][COLOR green]Delete Thumbs[/COLOR][/B]')
	if choice == 1:
		try: removeFile(os.join(DATABASE, latest))
		except: log2('Failed to delete, Purging DB.'); purgeDb(latest)
		removeFolder(THUMBS)
		#if not type == 'total': killxbmc()
	else: log2('Clear thumbnames cancelled')
	redoThumbs()
	
	
def redoThumbs():
	if not os.path.exists(THUMBS): os.makedirs(THUMBS)
	thumbfolders = '0123456789abcdef'
	videos = os.path.join(THUMBS, 'Video', 'Bookmarks')
	for item in thumbfolders:
		foldname = os.path.join(THUMBS, item)
		if not os.path.exists(foldname): os.makedirs(foldname)
	if not os.path.exists(videos): os.makedirs(videos)
	
def latestDB(DB):
	if DB in ['Addons', 'ADSP', 'Epg', 'MyMusic', 'MyVideos', 'Textures', 'TV', 'ViewModes']:
		match = glob.glob(os.path.join(DATABASE,'%s*.db' % DB))
		comp = '%s(.+?).db' % DB[1:]
		highest = 0
		for file in match :
			try: check = int(re.compile(comp).findall(file)[0])
			except: check = 0
			if highest < check :
				highest = check
		return '%s%s.db' % (DB, highest)
	else: return False
	
def removeFolder(path):
	log2("Deleting Folder: %s" % path, xbmc.LOGNOTICE)
	try: shutil.rmtree(path,ignore_errors=True, onerror=None)
	except: return False
	
def purgeDb(name):
	#dbfile = name.replace('.db','').translate(None, digits)
	#if dbfile not in ['Addons', 'ADSP', 'Epg', 'MyMusic', 'MyVideos', 'Textures', 'TV', 'ViewModes']: return False
	#textfile = os.path.join(DATABASE, name)
	log2('Purging DB %s.' % name, xbmc.LOGNOTICE)
	if os.path.exists(name):
		try:
			textdb = database.connect(name)
			textexe = textdb.cursor()
		except Exception, e:
			log2("DB Connection Error: %s" % str(e), xbmc.LOGERROR)
			return False
	else: log2('%s not found.' % name, xbmc.LOGERROR); return False
	textexe.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
	for table in textexe.fetchall():
		if table[0] == 'version': 
			log2('Data from table `%s` skipped.' % table[0], xbmc.LOGDEBUG)
		else:
			try:
				textexe.execute("DELETE FROM %s" % table[0])
				textdb.commit()
				log2('Data from table `%s` cleared.' % table[0], xbmc.LOGDEBUG)
			except Exception, e: log2("DB Remove Table `%s` Error: %s" % (table[0], str(e)), xbmc.LOGERROR)
	textexe.close()
	log2('%s DB Purging Complete.' % name, xbmc.LOGNOTICE)
	show = name.replace('\\', '/').split('/')
	LogNotify("[COLOR %s]Purge Database[/COLOR]" % COLOR1, "[COLOR %s]%s Complete[/COLOR]" % (COLOR2, show[len(show)-1]))
	
def removeFile(path):
	log2("Deleting File: %s" % path, xbmc.LOGNOTICE)
	try:    os.remove(path)
	except: return False

####################################################################################################################
def getCacheSize():
	PROFILEADDONDATA = os.path.join(PROFILE,'addon_data')
	dbfiles   = [
		(os.path.join(ADDONDATA, 'plugin.video.phstreams', 'cache.db')),
		(os.path.join(ADDONDATA, 'plugin.video.bob', 'cache.db')),
		(os.path.join(ADDONDATA, 'plugin.video.specto', 'cache.db')),
		(os.path.join(ADDONDATA, 'plugin.video.genesis', 'cache.db')),
		(os.path.join(ADDONDATA, 'plugin.video.exodus', 'cache.db')),
		(os.path.join(DATABASE,  'onechannelcache.db')),
		(os.path.join(DATABASE,  'saltscache.db')),
		(os.path.join(DATABASE,  'saltshd.lite.db'))]
	cachelist = [
		(PROFILEADDONDATA),
		(ADDONDATA),
		(os.path.join(HOME,'cache')),
		(os.path.join(HOME,'temp')),
		(os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')),
		(os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')),
		(os.path.join(ADDONDATA,'script.module.simple.downloader')),
		(os.path.join(ADDONDATA,'plugin.video.itv','Images')),
		(os.path.join(PROFILEADDONDATA,'script.module.simple.downloader')),
		(os.path.join(PROFILEADDONDATA,'plugin.video.itv','Images'))]
		
	totalsize = 0

	for item in cachelist:
		if os.path.exists(item) and not item in [ADDONDATA, PROFILEADDONDATA]:
			totalsize = getSize(item, totalsize)
		else:
			for root, dirs, files in os.walk(item):
				for d in dirs:
					if 'cache' in d.lower() and not d.lower() == 'meta_cache': totalsize = getSize(os.path.join(root, d), totalsize)
	
	return totalsize
def getSize(path, total=0):
	for dirpath, dirnames, filenames in os.walk(path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total += os.path.getsize(fp)
	return total
def convertSize(num, suffix='B'):
	for unit in ['', 'K', 'M', 'G']:
		if abs(num) < 1024.0:
			return "%3.02f %s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.02f %s%s" % (num, 'G', suffix)

def ADDONS():
    Repo_Check()
    addDir('[COLOR'+TEXTCOL+']REPOS[/COLOR]',(Decode('aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv')),2030,ART+'repos.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']NEW[/COLOR]',str(BASEURL),22,ART+'NEW.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']IPTV[/COLOR]',str(BASEURL),23,ART+'IPTV.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']VIDEO[/COLOR]',str(BASEURL),24,ART+'VIDEO.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']SPORTS[/COLOR]',str(BASEURL),25,ART+'SPORTS.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']KIDS[/COLOR]',str(BASEURL),26,ART+'KIDS.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']MUSIC[/COLOR]',str(BASEURL),27,ART+'MUSIC.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']PROGRAMS[/COLOR]',str(BASEURL),28,ART+'PROGRAMS.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']XXX[/COLOR]','URL',29,ART+'XXX.png',FANART,'')
    setView('movies', 'MAIN')


def ADVANCEDXML():
    Repo_Check()
    addDir2('CHECK ADVANCED XML',str(BASEURL),8,ART+'XML.png',FANART,'')
    addDir2('MUCKYS XML',str(BASEURL)+'/wizard/muckys.xml',7,ART+'XML.png',FANART,'')
    addDir2('0CACHE XML',str(BASEURL)+'/wizard/0cache.xml',7,ART+'XML.png',FANART,'')
    addDir2('MIKEY1234 XML',str(BASEURL)+'/wizard/mikey.xml',7,ART+'XML.png',FANART,'')
    addDir2('TUXENS XML',str(BASEURL)+'/wizard/tuxens.xml',7,ART+'XML.png',FANART,'')
    addDir2('P2P RECOMMENDED XML1',str(BASEURL)+'/wizard/p2p1.xml',7,ART+'XML.png',FANART,'')
    addDir2('P2P RECOMMENDED XML2',str(BASEURL)+'/wizard/p2p2.xml',7,ART+'XML.png',FANART,'')
    addDir2('DELETE XML',str(BASEURL),11,ART+'XML.png',FANART,'')
    setView('movies', 'MAIN')
	
def RES():
    Repo_Check()
    addDir2('[COLOR'+TEXTCOL+']My Local Zip[/COLOR]',MyLocal,48,ART+'MyLocalZIP.png',FANART,'')
    addDir2('[COLOR'+TEXTCOL+']My Online Zip[/COLOR]',MyBuild,43,ART+'MyOnlineZip.png',FANART,'')

def CUSTOMFTV():
    Repo_Check()
    addDir2('INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED',str(BASEURL)+'/wizard/customftv/ftvguide-addons.zip',5,ART+'FTV4.png',FANART,'')
    addDir2('FTV GUIDE FIRST RUN SETTINGS',str(BASEURL)+'/wizard/customftv/settings.xml',17,ART+'FTV3.png',FANART,'')
    addDir2('FTV GUIDE ADDONS2.INI UPDATE DAILY','http://ren.byethost12.com/addons2.ini',16,ART+'FTV1.png',FANART,'')
    addDir2('RESET FTV DATABASE','url',18,ART+'FTV2.png',FANART,'')
    


def BUILD():
	Repo_Check()
	choices = ['[COLOR'+TEXTCOL+']SKINS[/COLOR]','[COLOR'+TEXTCOL+']ARTWORK PACKS[/COLOR]','[COLOR'+TEXTCOL+']CREATE UNIVERSAL PATHS[/COLOR]']
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']TOOLS[/COLOR]', choices)
	if choice==0:
		SKINS()
	if choice==0:
		ARTWORK(url)
	if choice==0:
		Fix_Paths(url)
#    addDir('[COLOR'+TEXTCOL+']SKINS[/COLOR]',str(BASEURL),33,ART+'Skins.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']ARTWORK PACKS[/COLOR]',str(BASEURL),34,ART+'ArtworkPacks.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']CREATE UNIVERSAL PATHS[/COLOR]',HOME,35,ART+'CreateUniversalPath.png',FANART,'')
	setView('movies', 'MAIN')

def thelist():
    link = OPEN_URL (Decode('aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2'))
    match = re.compile(' src="([^"]*)".+?><br />(.+?)</span></li>',re.DOTALL).findall(link)
    for img,name in match:
            addDir2(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&amp;','&').replace('<br />','').replace('&nbsp;',' ').replace('</span><span style="margin: 0px; padding: 0px;">',' '),'','',img,img,'')
    setView('tvshows', 'INFO')

def URLFIX(url):
    link = OPEN_URL(F).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def SKINS():
    Repo_Check()
    addDir('[COLOR'+TEXTCOL+']GOTHAM SKINS[/COLOR]',str(BASEURL),36,ART+'GothamSkins.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']HELIX SKINS[/COLOR]',str(BASEURL),37,ART+'HelixSkins.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']ISENGAARD SKINS[/COLOR]',HOME,38,ART+'IsengaardSkins.png',FANART,'')
    setView('movies', 'MAIN')
    
def GSKIN(url):
    link = OPEN_URL(str(BASEURL)+V).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def HSKIN(url):
    link = OPEN_URL(str(BASEURL)+W).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def ISKIN(url):
    link = OPEN_URL(str(BASEURL)+X).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
      
def FXSKIN(url):
    link = OPEN_URL(Decode('aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==')).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def ARTWORK(url):
    link = OPEN_URL(str(BASEURL)+R).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,40,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def ADDONSP(url):
    link = OPEN_URL(str(BASEURL)+P).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')

def APKSECTION():
	choices = ['[COLOR'+TEXTCOL+']GenieTv Apps[/COLOR]','[COLOR'+TEXTCOL+']APK Factory[/COLOR]','[COLOR'+TEXTCOL+']APK Search[/COLOR]']
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']APK TOOL[/COLOR]', choices)
	if choice==0:
		apkmasterMenu()
	if choice==1:
		APK()
	if choice==2:
		APKSearch()
#    addDir('[COLOR'+TEXTCOL+']GenieTv Apps[/COLOR]','',80002,ART+'APKAndroidOnly.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']APK Factory[/COLOR]',str(BASEURL),2,ART+'APKAndroidOnly.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']APK Search[/COLOR]',str(BASEURL),30038,ART+'APKSearch.png',FANART,'')
     
def APK():
    html=OPEN_CAT(Decode('aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw=='))
    match = re.compile('href="([^"]*)">Applications(.+?)</a>').findall(html)
    match2 = re.compile('href="([^"]*)">Games(.+?)</a>').findall(html)
    for url,count in match:
        addDir3('Android Apps'+count,'https://www.apkfiles.com'+url,30035,ART+'apps.png')
    for url,count in match2:
        addDir3('Android Games'+count,'https://www.apkfiles.com'+url,30035,ART+'GAMES.png')
    setView('movies', 'MAIN')
def APKGAME(url):
    html=OPEN_URL(url)
    match = re.compile('<a href="([^"]*)" >(.+?)</a>').findall(html)
    for url,name in match:
        if '/cat' in url:
            addDir3((name).replace('&amp;',' - '),'https://www.apkfiles.com'+url,30037,ART+'APK.png')
def APKAPP(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="([^"]*)" >(.+?)</a>').findall(html)
    for url,name in match:
        if '/app' in url:
            addDir3((name).replace('&amp;',' - '),'https://www.apkfiles.com'+url,30037,ART+'APK.png')
def APKSELECT2(url):
	html=OPEN_URL(url)
	url1 = url
	if "page=" in str(url):
		url1 = url.split('?')[0]
	match = re.compile('<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"',re.DOTALL).findall(html)
	match2 = re.compile('class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>').findall(html)
	for url,img,name in match:
		if 'apk' in url:
			addDir2((name).replace('&#39;','').replace('&amp;',' - ').replace('&#174;:',': ').replace('&#174;',' '),'https://www.apkfiles.com'+url,80004,'http:'+img)
	if len(match2) > 1:
		match2 = str(match2[len(match2) - 1])
	addDir2('Next Page',url1+str(match2),30037,ART+'Next.png')
def APKGRAB(name,url):
    html=OPEN_CAT(url)
    name=name
    match = re.compile('href="([^"]*)" class="yellow_button"  title=').findall(html)
    for url in match:
        url = 'https://www.apkfiles.com'+url
        apkInstaller(name,url,'Brackets')
def APKSearch():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = 'https://www.apkfiles.com/search?q='+(Search_Name).replace(' ','+')+'&search_type=1'
    Search_Title = Search_Clean_Name.lower()
    APKSELECT2(Search_Title)
    
def APKTOOL(url):
    path = xbmc.translatePath(os.path.join(A,'Download'))
    dp = xbmcgui.DialogProgress()
    dp.create("Your App Is Downloading","Why not check out our website",'', 'Http://GenieTv.co.uk')
    lib=os.path.join(path, name+'.apk')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]","[COLORblue]Tool Brought To You By GenieTv[/COLOR]")
    
def DOWNLOAD(url):
    path = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.GenieTv/resources/downloads'))
    dp = xbmcgui.DialogProgress()
    dp.create("Your fILM Is Downloading","Why not check out our website",'', 'Http://GenieTv.co.uk')
    lib=os.path.join(path, name+'.mp4')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]","[COLORblue]Tool Brought To You By GenieTv[/COLOR]")
    
    
def ARTTOOL(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Your Art Pack Is Downloading","Why not check out our website",'', 'Http://GenieTv.co.uk')
    lib=os.path.join(path, name)
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    artfolder = xbmc.translatePath(os.path.join(MEDIA))
    time.sleep(2)
    dp.update(0,"", "Placing Your Art Please Wait")
    print '======================================='
    print artfolder
    print '======================================='
    extract.all(lib,artfolder,dp)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]")

####################################
##########APK Installer#############
####################################

def apkmasterMenu():
	link = OPEN_URL(APKFILE).replace('\n','').replace('\r','').replace('\t','')
	match = re.compile('name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
	for name, url, icon, fanart, disc in match:
		addDir2(name,url,80003,icon,ART+'APKToolsB.png',disc)
def latestApk(apk, ret=None):
	if apk == "kodi":
		kodi  = "https://kodi.tv/download/"
		link  = OPEN_URL(kodi).replace('\n','').replace('\r','').replace('\t','')
		match = re.compile("<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>").findall(link)
		if len(match) == 1:
			ver    = match[0][0]
			title  = match[0][1]
			apkurl = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % (ver, title)
		if ret == 'version': return ver
		else:                return apkurl
	elif apk == "spmc":
		spmc  = 'https://github.com/koying/SPMC/releases/latest/'
		link  = OPEN_URL(spmc).replace('\n','').replace('\r','').replace('\t','')
		match = re.compile(".+?class=\"release-title\">(.+?)</h1>.+?").findall(link)
		ver   = re.sub('<[^<]+?>', '', match[0]).replace(' ', '')
		apkurl = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % (ver, ver)
		if ret == 'version': return ver
		else:                return apkurl
def apkInstaller(name, url, Brackets):
	if platform() == 'android':
		yes=Dialog.yesno(ADDONTITLE, "Would you like to download and install:", "%s" % name)
		if not yes: LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] Install Cancelled'); return
		display = name
		if yes:
			if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
			if not workingURL(url) == True: LogNotify(ADDONTITLE, 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]'); return
			dp.create(ADDONTITLE,'Downloading %s' % display,'', 'Please Wait')
			lib=os.path.join(PACKAGES, "%s.apk" % name)
			try: os.remove(lib)
			except: pass
			downloader.download(url, lib, dp)
			xbmc.sleep(500)
			dp.close()
			if "Brackets" in Brackets:
				zf = zipfile.ZipFile(lib)
				for file in  zf.namelist():
					if file.endswith('.apk'):
						with open(os.path.join(PACKAGES,os.path.basename(file)), 'wb') as f:
							file2 = file.split('/')[1]
							f.write(zf.read(file))
							xbmc.sleep(500)
							f.close()
							try:
								os.remove(lib)
							except:
								pass
							lib = os.path.join(PACKAGES, file2)
			Dialog.ok(ADDONTITLE, "Launching the APK to be installed", "Follow the install process to complete.")
			xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:'+lib+'")')
		else: LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] Install Cancelled')
	else: LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] None Android Device')

###########################
#######THE HUB#############
###########################
def THEHUB():
	if not os.path.exists(HUB): os.makedirs(HUB)
	link = OPEN_URL(Decode('aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw=='))
	match = re.compile('<a href="([^"]*)">(.+?).apk</a></td>').findall(link)
	for url,name in match:
		url = ((Decode('aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw=='))+url)
		THEHUB2((name).replace('_',' '), url)

def THEHUB2(name, url):
	if platform() == 'android':
		yes=Dialog.yesno(ADDONTITLE, "Would you like to download and install:", "%s" % name)
		if not yes: LogNotify(ADDONTITLE, '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day'); return
		display = name
		if yes:
			if not os.path.exists(HUB): os.makedirs(HUB)
			if not workingURL(url) == True: LogNotify(ADDONTITLE, 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]'); return
			dp.create(ADDONTITLE,'Downloading %s' % display,'', 'Please Wait')
			lib=os.path.join(HUB, "%s.apk" % name)
			try: os.remove(lib)
			except: pass
			downloader.download(url, lib, dp)
			xbmc.sleep(500)
			dp.close()
			Dialog.ok(ADDONTITLE, "Launching the APK to be installed", "Follow the install process to complete.")
			xbmc.executebuiltin('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:'+lib+'")')
		else: LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] Install Cancelled')
	else: LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] None Android Device')

###########################
def WISHESPC(url):
    link = OPEN_URL (BASEURL+(Decode('L0dlbmllVHYvdGVzdC93aC50eHQ='))).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'INFO')


def WISHES(url):
    link = OPEN_URL (BASEURL+(Decode('L0dlbmllVHYvdGVzdC8='))).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,30015,iconimage,fanart,description)
    setView('movies', 'MAIN')

def THEWIZ(url,iconimage,fanart):
	link = OPEN_URL (url)
	URL = url
	img = iconimage
	fanart = fanart
	match = re.compile('href="([^"]*)">(.+?)</a>').findall(link)
	for url2,name in match:
		if '.mp4' in name:
			addDir2('Watch VIDEO',url+'/'+url2,222,img,fanart,'')
		if 'description' in name:
			addDir2('Read Description',url+'/'+url2,30017,img,fanart,'')
		if 'images' in name:
			addDir('View Images',url+'/'+url2,30018,img,fanart,'')
		if 'url' in name:
			addDir2('Install Build On Android',url+'/'+url2,30016,img,fanart,'')
		if 'url' in name:
			addDir2('Install Build On Pc',url+'/'+url2,30019,img,fanart,'')
	setView('movies', 'INFO')

def THEWIZINSTALL(url):
	link = OPEN_URL (url)
	match = re.compile('url="([^"]*)"').findall(link)
	for url in match:
		WIZARDAN(url)

def THEWIZINSTALLPC(url):
	link = OPEN_URL (url)
	match = re.compile('url="([^"]*)"').findall(link)
	for url in match:
		WIZARD(url)

def THEWIZDESC(url):
	link = OPEN_URL (url)
	match = re.compile('desc="([^"]*)"').findall(link)
	for text in match:
		TextBox('Description:',text)

def THEWIZimage(url):
	link = OPEN_URL (url)
	url = url
	match = re.compile('<a href="([^"]*)">(.+?)</a>').findall(link)
	for url2,name in match:
		if 'png' in name:
			addDir2('image','','',url+'/'+url2,url+'/'+url2,'')
	setView('movies', 'MAIN')

def ADDSKIN(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("GenieTv","Downloading Content",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://home','addons'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "Press ok to finish install","[COLOR yellow]Brought To You By GenieTv[/COLOR]")
    UPDATEREPO()


def WIZARD(url):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("GenieTv","Downloading ",'', 'Please Wait')
    lib=os.path.join(path, 'plugin.program.GenieTv.install'+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    CLEANUP(url)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager","[COLOR yellow]Brought To You By GenieTv[/COLOR]")
    killxbmc()

def WIZARDAN(url):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("GenieTv","Downloading ",'', 'Please Wait')
    lib=os.path.join(path, 'plugin.program.GenieTv.install'+'.zip')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    CLEANUP(url)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. ","[COLOR yellow]Brought To You By GenieTv[/COLOR]")
    killxbmc()

def LOCALZIP(name,url,description):
    addonfolder = xbmc.translatePath(os.path.join('special://','home'))
    dp = xbmcgui.DialogProgress()
    lib=os.path.join(MyLocal)
    time.sleep(2)
    dp.create("GenieTv","Restoring",'', 'Please Wait')
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. ","[COLOR yellow]Brought To You By GenieTv[/COLOR]")
    killxbmc()
       
def platform():
	if xbmc.getCondVisibility('system.platform.android'):   return 'android'
	elif xbmc.getCondVisibility('system.platform.linux'):   return 'linux'
	elif xbmc.getCondVisibility('system.platform.windows'): return 'windows'
	elif xbmc.getCondVisibility('system.platform.osx'):	    return 'osx'
	elif xbmc.getCondVisibility('system.platform.atv2'):    return 'atv2'
	elif xbmc.getCondVisibility('system.platform.ios'):	    return 'ios'
def log(log):
	xbmc.log("[%s]: %s" % (ADDONTITLE, log))
	if not os.path.exists(ADDONDATA): os.makedirs(ADDONDATA)
	if not os.path.exists(WIZLOG): f = open(WIZLOG, 'w'); f.close()
	with open(WIZLOG, 'a') as f:
		line = "[%s %s] %s" % (datetime.now().date(), str(datetime.now().time())[:8], log)
		f.write(line.rstrip('\r\n')+'\n')
def log2(msg, level=xbmc.LOGDEBUG):
	if not os.path.exists(ADDONDATA): os.makedirs(ADDONDATA)
	if not os.path.exists(WIZLOG): f = open(WIZLOG, 'w'); f.close()
	if WIZDEBUGGING == 'false': return False
	if DEBUGLEVEL == '0': return False
	if DEBUGLEVEL == '1' and not level in [xbmc.LOGNOTICE, xbmc.LOGERROR, xbmc.LOGSEVERE, xbmc.LOGFATAL]: return False
	if DEBUGLEVEL == '2': level = xbmc.LOGNOTICE
	try:
		if isinstance(msg, unicode):
			msg = '%s' % (msg.encode('utf-8'))
		xbmc.log('%s: %s' % (ADDONTITLE, msg), level)
	except Exception as e:
		try: xbmc.log('Logging Failure: %s' % (e), level)
		except: pass
	if ENABLEWIZLOG == 'true':
		lastcheck = getS('nextcleandate') if not getS('nextcleandate') == '' else str(TODAY)
		if CLEANWIZLOG == 'true' and lastcheck <= str(TODAY): checkLog()
		with open(WIZLOG, 'a') as f:
			line = "[%s %s] %s" % (datetime.now().date(), str(datetime.now().time())[:8], msg)
			f.write(line.rstrip('\r\n')+'\n')
def killxbmc():
	choice = Dialog.yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
	if choice == 0: return
	elif choice == 1: pass
	myplatform = platform()
	log("Platform: " + str(myplatform))
	os._exit(1)
	log("Force close failed!  Trying alternate methods.")
	if myplatform == 'osx': # OSX
		log("############ try osx force close #################")
		try: os.system('killall -9 XBMC')
		except: pass
		try: os.system('killall -9 Kodi')
		except: pass
		Dialog.ok("[COLOR=red][B]WARNING !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
	elif myplatform == 'linux': #Linux
		log("############ try linux force close #################")
		try: os.system('killall XBMC')
		except: pass
		try: os.system('killall Kodi')
		except: pass
		try: os.system('killall -9 xbmc.bin')
		except: pass
		try: os.system('killall -9 kodi.bin')
		except: pass
		Dialog.ok("[COLOR=red][B]WARNING !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
	elif myplatform == 'android': # Android 
		log("############ try android force close #################")
		try: os.system('adb shell am force-stop org.xbmc.kodi')
		except: pass
		try: os.system('adb shell am force-stop org.kodi')
		except: pass
		try: os.system('adb shell am force-stop org.xbmc.xbmc')
		except: pass
		try: os.system('adb shell am force-stop org.xbmc')
		except: pass		
		try: os.system('adb shell am force-stop com.gadgetcity.itvmc')
		except: pass		
		try: os.system('adb shell kill org.xbmc.kodi')
		except: pass
		try: os.system('adb shell kill org.kodi')
		except: pass
		try: os.system('adb shell kill org.xbmc.xbmc')
		except: pass
		try: os.system('adb shell kill org.xbmc')
		except: pass
		try: os.system('adb shell kill com.gadgetcity.itvmc')
		except: pass
		try: os.system('Process.killProcess(android.os.Process.org.xbmc,kodi());')
		except: pass
		try: os.system('Process.killProcess(android.os.Process.org.kodi());')
		except: pass
		try: os.system('Process.killProcess(android.os.Process.org.xbmc.xbmc());')
		except: pass
		try: os.system('Process.killProcess(android.os.Process.org.xbmc());')
		except: pass
		try: os.system('Process.killProcess(android.os.Process.com.gadgetcity.itvmc());')
		except: pass
		Dialog.ok(ADDONTITLE, "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI")
	elif myplatform == 'windows': # Windows
		log("############ try windows force close #################")
		try:
			os.system('@ECHO off')
			os.system('tskill XBMC.exe')
		except: pass
		try:
			os.system('@ECHO off')
			os.system('tskill Kodi.exe')
		except: pass
		try:
			os.system('@ECHO off')
			os.system('TASKKILL /im Kodi.exe /f')
		except: pass
		try:
			os.system('@ECHO off')
			os.system('TASKKILL /im XBMC.exe /f')
		except: pass
		Dialog.ok("[COLOR=red][B]WARNING !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
	else: #ATV
		log("############ try atv force close #################")
		try: os.system('killall AppleTV')
		except: pass
		log("############ try raspbmc force close #################") #OSMC / Raspbmc
		try: os.system('sudo initctl stop kodi')
		except: pass
		try: os.system('sudo initctl stop xbmc')
		except: pass
		Dialog.ok("[COLOR=red][B]WARNING !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.","iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo.")


#Convert physical paths to special paths
def Fix_Paths(url):
    dp.create("[COLOR=green]GenieTv[/COLOR]","Renaming paths...",'', 'Please Wait')
    for root, dirs, files in os.walk(url):  #Search all xml files and replace physical with special
        for file in files:
            if file.endswith(".xml"):
                 dp.update(0,"Fixing",file, 'Please Wait')
                 a=open((os.path.join(root, file))).read()
                 b=a.replace(HOME, 'special://home/')
                 f = open((os.path.join(root, file)), mode='w')
                 f.write(str(b))
                 f.close()
    killxbmc()
#------------------------------RADIONOMY-----------------------------------------------------------------------
def RadioNomy():
    addDir3(('[COLOR'+TEXTCOL+']GENRE[/COLOR]'),(Decode('aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==')),70002,ART+'RadioNomy.png')
    addDir3(('[COLOR'+TEXTCOL+']SORT BY[/COLOR]'),(Decode('aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==')),70003,ART+'RadioNomy.png')
    addDir3(('[COLOR'+TEXTCOL+']SEARCH[/COLOR]'),'',70006,ART+'RadioNomy.png')

def RadioNomygenre(url):
    html=OPEN_CAT(url)
    match = re.compile('<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]'),(Decode('aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ=='))+url,70004,ART+'RadioNomy.png')
def RadioNomysort(url):
    html=OPEN_CAT(url)
    match = re.compile('<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]'),(Decode('aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ=='))+url,70004,ART+'RadioNomy.png')
def RadioNomylist(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"',re.DOTALL).findall(html)
    match2 = re.compile('data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>').findall(html)
    for url,name in match2:
        addDir3(('[COLOR'+TEXTCOL+']Filter - '+name+'[/COLOR]'),(Decode('aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ=='))+url,70004,ART+'RadioNomy.png')
    for url,img,name in match:
        addDir4(('[COLOR'+TEXTCOL+']Stream - '+name+'[/COLOR]'),(Decode('aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ=='))+url,70005,img)
def RadioNomyplay(url):
    html=OPEN_CAT(url)
    match = re.compile('<li><a class="download" href="([^"]*)').findall(html)
    for url in match:
        RESOLVEtest(url)
def RadioNomysearch():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name
    Search_URL = 'https://www.radionomy.com/en/search/index?query=' + (Search_Name).replace(' ','+')
    HTML = OPEN_URL(Search_URL)
    match = re.compile('<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"',re.DOTALL).findall(HTML)
    for url,img,name in match:
        addDir4(('[COLOR'+TEXTCOL+']Stream - '+name+'[/COLOR]'),(Decode('aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ=='))+url,70005,img)

#------------------------------RADIO-----------------------------------------------------------------------
def RADIO():
    html=OPEN_CAT(Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw=='))
    match = re.compile('<a href="([^"]*)">(.+?)</a></td></tr>').findall(html)
    for url,name in match:
			    addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]','http://www.listenlive.eu/'+url,10111113,ART+'WorldRadio.png',ART+'WorldRadio.png','Radio Stations From Around The World.')
def RADIO2(url):
    html=OPEN_CAT(url)
#    match = re.compile('<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">',re.DOTALL).findall(html)
#    for name,url in match:
    match = re.compile('<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>',re.DOTALL).findall(html)
    for name,reg,url,what in match:
			    addDir2('[COLOR'+TEXTCOL+']'+name+' [COLORorangered] '+what+'[/COLOR]',url,222225,ART+'WorldRadio.png',ART+'WorldRadio.png','[COLOR'+TEXTCOL+']'+name+'[CR]'+reg+'[CR]'+what+'[/COLOR]')
#------------------------------CARTOONS---------------------------------------------------------------------
def TOON1():
    html=OPEN_CAT(Decode('aHR0cDovL3d3dy50b29uamV0LmNvbS8='))
    match = re.compile('<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>').findall(html)
    for url,name in match:
			    addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]','http://www.toonjet.com/'+url,8051,ART+'classictoons.png')
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
def TOON2(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="([^"]*)"><img src="([^"]*)"').findall(html)
    match2 = re.compile('<a href="([^"]*)">.+?</a></td></tr></table>').findall(html)
    for url,img in match:
        if 'ol.gif' in img:
            pass
        elif 'link_block_' in img:
            pass
        elif '.png' in img:
            pass
        else:
			    addDir3((img).replace('http://www.toonjet.com/images/icons/','').replace('images/icons/','').replace('.jpg','').replace('_icon','').replace('_',' '),'http://www.toonjet.com/'+url,8052,ART+'vod.png')
    for url in match2:
        addDir3('NEXT PAGE','http://www.toonjet.com/'+url,8051,ART + 'Next.png')
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
def TOON3(url):
    html=OPEN_CAT(url)
    match = re.compile('<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>').findall(html)
    for url in match:
			    addDir4('[COLOR'+TEXTCOL+']PLAY[/COLOR]',(url).replace('http://www.youtube.com/embed/','').replace('?autoplay=0',''),8043,ART+'classictoons.png')

#--------------------------------KODIBLE--------------------------------------------------------------------------
def Home_Menu():
    addDirFolder('Audio Books','',30011,ART + 'AudioBooks.png',ART + 'AudioBooks.png','')
    addDirFolder('Kids Audio Books','',30006,ART + 'KidsAudioBooks.png',ART + 'KidsAudioBooks.png','')

def Audio_Menu():	
    addDirFolder('All','',30001,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
    addDirFolder('Popular','',30012,ART + 'POPULARv.png',ART + 'POPULARv.png','')
    addDirFolder('Search','',30013,ART + 'Search.png',ART + 'Search.png','')

def Popular():
    HTML = OPEN_URL(BASEK + 'books' + CAT)
    match = re.compile('<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>').findall(HTML)
    for name,url,cat in match:
        if 'Parent' in name:
            pass
        elif '2' in cat:
            addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('.mp3',''),url,30010,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
			
def Search_Audio():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    HTML = OPEN_URL(BASEK + 'books' + CAT)
    match = re.compile('<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>').findall(HTML)
    for name,url,cat in match:
        if Search_Name in name.lower():
            if '1' in cat:
                addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('.mp3',''),url,30010,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
            elif '2' in cat:
                addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('.mp3',''),url,30010,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
            elif '3' in cat:	
                addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('.mp3',''),url,30009,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')

	
def Audio():
    HTML = OPEN_URL(BASEK + 'books' + CAT)
    match = re.compile('<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>').findall(HTML)
    for name,url,cat in match:
        if '1' in cat:
            addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('.mp3',''),url,3010,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
        elif '2' in cat:
            addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('.mp3',''),url,30010,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
        elif '3' in cat:	
            addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('.mp3',''),url,30009,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def Match(url):
    url2 = url
    HTML = OPEN_URL(url)
    match2 = re.compile('<a href="([^"]*)">(.+?)</a>').findall(HTML)
    for url,name in match2:
        if 'mp3' in name:
            addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' '),url2+url,222,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
        if 'wma' in name:
            addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' '),url2+url,222,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
        if 'm4b' in name:
            addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' '),url2+url,222,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
        elif '/' in name:
            addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('/','').replace('.mp3',''),url2+url,30009,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
	
	
		
def Match2(url):
    HTML = OPEN_URL(url)
    url2 = url
    match = re.compile('<li><a href="([^"]*)">(.+?)</a></li>').findall(HTML)
    for url,name in match:
        if 'Parent' in name:
            pass
        elif '.db' in name:
		    pass
        elif '.jpg' in name:
		    pass
        elif '.html' in name:
		    pass
        elif '.doc' in name:
		    pass
        elif 'mp3' in name:
            addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('/','').replace('.mp3',''),url2+url,222,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
        elif 'm4a' in name:
            addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('/','').replace('.mp3',''),url2+url,222,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
        else:
            addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('%20',' ').replace('/','').replace('.mp3',''),url2+url,30010,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')

   
def Kids_Menu():
    addDirFolder('A-Z','',30007,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
    addDirFolder('All','',30003,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
    addDirFolder('Search','',30014,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')

def Kids_AZ():
    HTML = OPEN_URL(Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ=='))
    match = re.compile('<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>',re.DOTALL).findall(HTML)
    for url,img in match:
        print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'+url+'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        if '-x' in img:
            pass
        else:
            addDirFolder(img,(Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=')) + (url).replace('colour_it','books_audio/audio_books_a'),30008,(Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==')) + img + '.gif',ART + 'KodibleAudioBooks.png','')

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

			
def Kids_AZ_Audio(url):   
    HTML = OPEN_URL(url)
    match = re.compile('<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>',re.DOTALL).findall(HTML)
    for url,name in match:
        if '</a>' in name:
            pass
        elif '(' in name:
            addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;','').replace('  ','').replace('.mp3',''),Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=') + url,30005,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
        else:
            addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;','').replace('  ','').replace('.mp3',''),Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=') + url,30004,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);		
	
def Search_Kids():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    HTML = OPEN_URL(Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ=='))
    match = re.compile('<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>',re.DOTALL).findall(HTML)
    for url,name in match:
        if Search_Name in name.lower():			
            if '</a>' in name:
                pass
            elif '(' in name:
                addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;','').replace('  ','').replace('+','').replace('.mp3',''),Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=') + url,30005,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
            else:
                addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;','').replace('  ','').replace('+','').replace('.mp3',''),Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=') + url,30004,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
	
	
def Kids_Audio():   
    HTML = OPEN_URL(Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ=='))
    match = re.compile('<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>',re.DOTALL).findall(HTML)
    for url,name in match:
        if '</a>' in name:
            pass
        elif '(' in name:
            addDirFolder(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;','').replace('  ','').replace('+','').replace('.mp3',''),Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=') + url,30005,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')
        else:
            addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;','').replace('  ','').replace('+','').replace('.mp3',''),Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=') + url,30004,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
			

def Kids_Play(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)">Download</a></b></td>').findall(HTML)
    for url in match:
        url2 = (Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=')) + url
        Resolve(url2)

def Kids_Play_Multi(url):
    HTML = OPEN_URL(url)
    match = re.compile('<td width="247">(.*?)</td>.*?<a href="([^"]*)">',re.DOTALL).findall(HTML)
    for name,url in match:
        if '<p align' in name:
            pass
        elif '&nbsp;' in name:
            pass
        else:
            addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;',''),Decode('aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=') + url,222,ART + 'KodibleAudioBooks.png',ART + 'KodibleAudioBooks.png','')

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
#--------------------------------WATCH CARTOONS--------------------------------------------------------------------------

def WCO_CATS():
    HTML = cloudflare.source(Decode('aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv'))
    match = re.compile('class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>',re.DOTALL).findall(HTML)
    for url,name in match:
        if 'ongoing' in url:
            addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,21005,ART + 'OnGoing.png','','')
        if 'cartoon-series' in url:
            addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,21005,ART + 'CartoonShows.png','','')
        if 'disney' in url:
            addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,21005,ART + 'Disney.png','','')
        if 'genre' in url:
            addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,21005,ART + 'Genre.png','','')
        if 'years' in url:
            addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,21005,ART + 'Years.png','','')
def WCO_SHOWS(url):
    HTML = cloudflare.source(url)
    match = re.compile('<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"',re.DOTALL).findall(HTML)
    genre = re.compile('<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>').findall(HTML)
    next = re.compile('<link rel="next" href="([^"]*)" />').findall(HTML)
    for url,name,img in match:
        addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8211;','-'),url,21006,img,img,name)
    for url,name in genre:
        addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,21005,ART + 'watchcartoons.png','','')
    for url in next:
        addDir('[COLOR'+TEXTCOL+']NEXT[/COLOR]',url,21005,ART + 'Next.png','','')
def WCO_EP(url):
    HTML = cloudflare.source(url)
    match = re.compile('<li><a href="([^"]*)" target=_blank>(.+?)</a></li>',re.DOTALL).findall(HTML)
    play = re.compile('file:"([^"]*)",type:"mp4",label:"([^"]*)"',re.DOTALL).findall(HTML)
    play2 = re.compile('src="([^"]*)" frameborder=').findall(HTML)
    playdirect = re.compile('<iframe src="([^"]*)"').findall(HTML)
    for url,name in match:
        addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8211;','-').replace('&#8217;',''),url,21007,ART + 'watchcartoons.png','','')
    for url in play2:
        addDir('[COLOR'+TEXTCOL+']PLAY[/COLOR]','http:'+url,222,ART + 'watchcartoons.png','','')
    for url,name in play:
        addDir2('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,222,ART + 'watchcartoons.png','','')
    else:
        addDir('[COLOR'+TEXTCOL+']NO STREAMS AVAILABLE[/COLOR]',url,21005,ART + 'watchcartoons.png','','')
def WCO_PLAY(url):
    HTML = cloudflare.source(url)
    match = re.compile('file:"([^"]*)",type:"mp4",label:"([^"]*)"',re.DOTALL).findall(HTML)
    for url,name in match:
        addDir2('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,222,ART + 'watchcartoons.png','','')
#--------------------------------KISS CARTOONS--------------------------------------------------------------------------
def KISS_CATS():
    HTML = cloudflare.source('http://9cartoon.me/CartoonList')
    match = re.compile('<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>',re.DOTALL).findall(HTML)
    for url,name in match:
        if '9cart' in url:
            addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,20001,ART +'ORIGINCARTOON.png')

def KISS_CATS2(url):
    HTML = cloudflare.source(url)
    match = re.compile('href="([^"]*)" rel="all" class="active">All</a>',re.DOTALL).findall(HTML)
    match2 = re.compile('<a href="([^"]*)" rel="0" class="">#</a>',re.DOTALL).findall(HTML)
    match3 = re.compile('<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>',re.DOTALL).findall(HTML)
    for url in match:
        if '9cart' in url:
            addDir3('[COLOR'+TEXTCOL+']ALL[/COLOR]',url,20002,ART +'ORIGINCARTOON.png')
    for url in match2:
        if '9cart' in url:
            addDir3('[COLOR'+TEXTCOL+']123[/COLOR]',url,20002,ART +'ORIGINCARTOON.png')
    for url,name in match3:
        if '9cart' in url:
            addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,20002,ART +'ORIGINCARTOON.png')
	
def KISS_NAME(url):
    HTML = cloudflare.source(url)
    match = re.compile('<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>',re.DOTALL).findall(HTML)
    match2 = re.compile('<a href="([^"]*)"><span>(.+?)</span>',re.DOTALL).findall(HTML)
    for img,url,name in match:
        addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,20003,img)
    for url,name in match2:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&raquo;','Next'),url,20002,ART +'ORIGINCARTOON.png')

def KISS_GENRE(url):
    HTML = cloudflare.source(url)
    match = re.compile('<a href="([^"]*)">').findall(HTML)
    for url in match:
         if 'Watch' in url:
            addDir3((url).replace('http://9cartoon.me/Watch/','').replace('/',' ').replace('-',' '),url,20004,ART +'ORIGINCARTOON.png')

def KISS_SHOW(url):
    HTML = cloudflare.source(url)
    match = re.compile('href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>',re.DOTALL).findall(HTML)
    for url,name in match:
        addDir4('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,20005,ART +'ORIGINCARTOON.png')

def KISS_EP(url):
    url = cloudflare.source(url)
    RESOLVE(url)

def kissplay(url):
    HTML = cloudflare.source(url)
    match = re.recompile ('src="([^"]*)"')
    for url in match:
        RESOLVE(url)
#--------------------------------CARTOONS EXTRA--------------------------------------------------------------------------

def Random_Play_Cartoon(url,name):
    url = url;name = name
    Playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    Playlist.clear()
    episode_full_count = []
    Ep_Name_List = []
    html2 = OPEN_URL(url) 
    match2 = re.compile('<img src="(.+?)" id="series_image" width="250" height="370" alt=".+?" />').findall(html2) 
    for img in match2: 
        IMAGE = img 
    match3 = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(html2) 
    for Playlink_url,Ep_name in match3: 
        episode_full_count.append([Playlink_url,Ep_name]) 
        if len(episode_full_count)==len(match3):
            for item in episode_full_count:
                get_random_ep=random.randint(1,len(episode_full_count))
                try:									
                    next_url_to_use=episode_full_count[int(get_random_ep)]
                    if next_url_to_use[1] not in Ep_Name_List:
                        Ep_Name_List.append(next_url_to_use[1])
                        html3 = OPEN_URL(next_url_to_use[0])
                        match4 = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html3)
                        for ignore,final_playlink_get in match4:
                            if 'easy' in final_playlink_get:
                                html4 = OPEN_URL(final_playlink_get)
                                match5 = re.compile('file: "(.+?)"').findall(html4)
                                for finally_got_there_phew in match5:
                                    if 'http' in finally_got_there_phew:
                                        liz = xbmcgui.ListItem(next_url_to_use[1], iconImage=IMAGE, thumbnailImage=IMAGE)
                                        liz.setInfo( type="Video", infoLabels={"Title": next_url_to_use[1]})
                                        liz.setProperty("IsPlayable","true")
                                        Playlist.add(finally_got_there_phew, liz)
                                        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
                                    else:
                                        pass
                            else:
                                pass
                    else:
                        pass
                except:
                    pass
        else:
            pass
                    
def Random_Cartoon(url):
    Playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    Playlist.clear()
    Counter = []
    full_count = []
    Prog_Name = [] 
    html=OPEN_URL(url) 
    match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(html) 
    for url,name in match: 
        full_count.append([url,name]) 
        if len(full_count) == len(match): 
            for item in full_count: 
                get_random=random.randint(1,len(full_count)) 
                try: 
                    url_to_add = full_count[int(get_random)] 
                except: 
                    pass 
                if url_to_add[1] not in Prog_Name:
                    Prog_Name.append(url_to_add[1]) 
                    if int(len(Counter)) < 1:
                        Counter.append(url_to_add[1][0])
                        Random_Play_Cartoon(url_to_add[0],url_to_add[1])
                    else:
                        pass
                else:
                    pass
        else:
            pass
			
def Random_play(name, mode, url='', image=None, isFolder=True, page=1, keyword=None, infoLabels=None, contextMenu=None):
    if not image:
        image = ICON
    u  = sys.argv[0] 
    u += '?mode='  + str(mode)
    u += '&title=' + urllib.quote_plus(name)
    u += '&image=' + urllib.quote_plus(image)
    u += '&page='  + str(page)
    if url != '':     
        u += '&url='   + urllib.quote_plus(url) 
    if keyword:
        u += '&keyword=' + urllib.quote_plus(keyword) 
    liz = xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
    if contextMenu:
        liz.addContextMenuItems(contextMenu)
    if infoLabels:
        liz.setInfo(type="Video", infoLabels=infoLabels)
    if not isFolder:
        liz.setProperty("IsPlayable","true")
    liz.setProperty('Fanart_Image', FANART)     
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def twenty47_select():
    BASE = Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=')
    html=OPEN_URL(BASE)
    match = re.compile('<td><a href="(.+?)">(.+?)</a></td>').findall(html)
    for url,name in match:
        Random_play(name,9110012,url=url,image=ICON,isFolder=False)
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def Origin_cartoons():
    BASE = Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=')
    addDir('[COLOR'+TEXTCOL+']Cartoons[/COLOR]','',10004,ART+'Kids.png',FANART,'')
    Menu_1('[COLOR'+TEXTCOL+']24/7 Select Cartoon[/COLOR]','',9110011,ART+'Kids.png',FANART,'','')
    Random_play('[COLOR'+TEXTCOL+']24/7 Random Cartoon[/COLOR]',9110010,url=BASE,image=ART+'Kids.png',isFolder=False)
    addDir('[COLOR'+TEXTCOL+']Search Cartoons[/COLOR]','',10005,ART+'Kids.png',FANART,'')
	
def Origin_Cart_Search():
    BASE = Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=')
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name.lower()
    HTML = OPEN_URL(BASE)
#    HTML2 = OPEN_URL(Decode('aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUvP3M9'))
    match = re.compile('<td><a href="([^"]*)">(.+)</a></td>').findall(HTML)
#    match2 = re.compile('<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"',re.DOTALL).findall(HTML2)
    for url,name in match:
        if Search_Name in name.lower():
            if 'Dad!' in name:
                pass
            elif 'Family Guy' in name:
                pass
            elif '2 Stupid' in name:
                pass
            elif 'The Zelfs' in name:
                pass
            elif 'A Clone' in name:
                pass
            elif 'A.T.O.M' in name:
                pass
            elif 'Almost Naked' in name:
                pass
            elif 'Angry Kid' in name:
                pass
            elif 'Annoying Orange' in name:
                pass
            elif 'Aqua Teen' in name:
                pass
            elif 'Assy Mcgee' in name:
                pass
            elif 'Astroblast' in name:
                pass
            elif 'Atomic Betty' in name:
                pass
            elif 'Axe Cop' in name:
                pass
            elif 'Baby Playpen' in name:
                pass
            elif 'Beavis and Butt' in name:
                pass
            elif 'Celebrity Deathmatch' in name:
                pass
            elif 'Clerks The' in name:
                pass
            elif 'Crapston Villas' in name:
                pass
            elif 'Duckman:' in name:
                pass
            elif 'Stripperella' in name:
                pass
            elif 'Vixen' in name:
                pass
            else:
                addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,10006,ART+'Kids.png',FANART,'')
#	for url,name,img in match2:
#		addDir(('[COLOR'+TEXTCOL+']'+name+' -WCO[/COLOR]').replace('&#8211;','-'),url,21006,img,img,name)

	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def Origin_Cart(url):
    BASE = Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=')
    html=OPEN_URL(BASE)
    match = re.compile('<td><a href="([^"]*)">(.+)</a></td>').findall(html)
    for url,name in match:
            if 'Dad!' in name:
                pass
            elif 'Family Guy' in name:
                pass
            elif '2 Stupid' in name:
                pass
            elif 'The Zelfs' in name:
                pass
            elif 'A Clone' in name:
                pass
            elif 'A.T.O.M' in name:
                pass
            elif 'Almost Naked' in name:
                pass
            elif 'Angry Kid' in name:
                pass
            elif 'Annoying Orange' in name:
                pass
            elif 'Aqua Teen' in name:
                pass
            elif 'Assy Mcgee' in name:
                pass
            elif 'Astroblast' in name:
                pass
            elif 'Atomic Betty' in name:
                pass
            elif 'Axe Cop' in name:
                pass
            elif 'Baby Playpen' in name:
                pass
            elif 'Beavis and Butt' in name:
                pass
            elif 'Celebrity Deathmatch' in name:
                pass
            elif 'Clerks The' in name:
                pass
            elif 'Crapston Villas' in name:
                pass
            elif 'Duckman:' in name:
                pass
            elif 'Stripperella' in name:
                pass
            elif 'Vixen' in name:
                pass
            else:
                addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,10006,ART+'Kids.png',FANART,'')
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
    
def Origin_Cartoon_Lists(url):
    html=OPEN_URL(url)
    match2 = re.compile('<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />').findall(html)
    for img in match2:
        IMAGE = img
    match3 = re.compile('<li><a href="([^"]*)">Next</a></li>').findall(html)
    for url in match3:
	    addDir('[COLOR'+TEXTCOL+']NEXT PAGE[/COLOR]',url,10006,ART + 'Next.png',FANART,'')
    match = re.compile('&nbsp;<a href="([^"]*)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir4('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,10007,IMAGE)
	

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def Origin_Cartoon_Lists2(url,IMAGE):
    sources = []
    html=OPEN_URL(url)
    match = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html)
    for name,url2 in match:
        if 'panda' in url2:
            HTML = OPEN_URL(url2)
            match2 = re.compile("url: '(.+?)'").findall(HTML)
            for url3 in match2:
                if 'http' in url3:
					sources.append({'source': 'playpanda', 'quality': 'SD', 'url': url3})
        elif 'easy' in url2:
            HTML2 = OPEN_URL(url2)
            match3 = re.compile('file: "(.+?)"').findall(HTML2)
            for url3 in match3:
                if 'http' in url3:
					sources.append({'source': 'easyvideo', 'quality': 'SD', 'url': url3})
        elif 'zoo' in url2:
            HTML3 = OPEN_URL(url2)
            match4 = re.compile('src: "(.+?)"').findall(HTML3)
            for url3 in match4:
                if 'http' in url3:
					sources.append({'source': 'videozoo', 'quality': 'SD', 'url': url3})
    if len(sources)>=3:
    	choice = Dialog.select('Select Playlink',
	                                [link["source"] + " - " + " (" + link["quality"] + ")"
	                                for link in sources])
        if choice != -1:
            url = sources[choice]['url']
            isFolder=False
            xbmc.Player().play(url)
        

	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);			

def Origin_Cartoon_Lists3(url):
    html=OPEN_URL(url)
    match = re.compile("url: '(.+?)',").findall(html)
    for url in match:
        RESOLVEtest(url)
    
#---------------------------Origin Stand up------------------------------------------------------------

def Stand_Up_Home_Menu():

    addDir('[COLOR'+TEXTCOL+']Stand Up[/COLOR]','',10014,ART + 'StandUp.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Search Comedian[/COLOR]','',10015,ART + 'SearchComedian.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Others[/COLOR]','',10017,ART + 'Others.png',FANART,'')
	
def My_list():
    HTML = OPEN_URL((Decode('aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=')))
    match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(HTML)
    for url,img,name in match:
        if 'elete' in name:
            pass
        else:
            addDir4('[COLOR'+TEXTCOL+']' + name + '[/COLOR]',url,222,img)
	
def Search_Stand_Up():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name.lower()
    HTML = OPEN_URL((Decode('aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=')))
    Block = re.compile('<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>',re.DOTALL).findall(HTML)
    for img, comic, c in Block:
        for Search_Name in comic:
            print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
            find_URL = re.compile('<a href="([^"]*)">(.+?)</a>',re.DOTALL).findall(c)
            for url, name in find_URL:
                if 'tube' in url:
                    pass
                elif 'stage' in url:
                    addDir4('[COLOR'+TEXTCOL+']' + comic + '   -   ' + name + '[/COLOR]',(url).replace('" target="_blank',''),10016,'http://couchtripper.com/'+img,)
                elif 'vee' in url:
			        pass
				
def Origin_StandUp():
    HTML = OPEN_URL((Decode('aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=')))
    Block = re.compile('<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>',re.DOTALL).findall(HTML)
    for img, comic, c in Block:
	find_URL = re.compile('<a href="([^"]*)">(.+?)</a>',re.DOTALL).findall(c)
        for url, name in find_URL:
            if 'tube' in url:
                pass
            elif 'stage' in url:
				addDir4('[COLOR'+TEXTCOL+']' + comic + '   -   ' + name + '[/COLOR]',(url).replace('" target="_blank',''),10016,'http://couchtripper.com/'+img)
            elif 'vee' in url:
                pass
			    

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

def Play_Stage(url):
    HTML = OPEN_URL(url)
    print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
    playlink = re.compile("url\[.+?\] = '(.+?)';").findall(HTML)
    print '>>>>>>>>>>>>>>>>>>>>>>>' + (str(playlink)) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    for url in playlink:
        RESOLVER((url).replace('[','').replace(']','').replace('\'',''))

############################################################### PANDORAS SECTION ######################################################################################################

	
	
#elif mode == 423 	: open_Menu(url)
#elif mode == 426 	: Pandora_Menu(url)
def Pand_Home_Menu():
    
    addDirPand2('[COLOR darkgoldenrod]By Category[/COLOR]','',10029,'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q',FANART,'')
    addDirPand2('[COLOR darkgoldenrod]Search[/COLOR]','',10026,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png',FANART,'')

    setView('movies', 'MAIN')

def Pand_Search_Menu():
    addDirPand2('Search Films','',10027,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png',FANART,'')
    addDirPand2('Search TV','',10028,'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png',FANART,'')

    setView('movies', 'MAIN')
def Search_Pandoras_Films():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    filenames = ['#','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for file_Name in filenames:
        search_URL = Base_Pand + '/Movies/a.to.z/' +file_Name + '.php'
        HTML = OPEN_Search(search_URL)
        match=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML)
        for url,iconimage,desc,background,name in match:
            if Search_Name in name.lower():
                if '.php' in url:
                    name = '[COLORsteelblue]'+name+'[/COLOR]'    
                    addDir(name,url,426,iconimage,background,desc)
                else:
                    name = '[COLORsteelblue]'+name+'[/COLOR]'    
                    addDirPand(name,url,222,iconimage,background,desc)
				
                    setView('movies', 'MAIN')
                    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
				
def Search_Pandoras_TV():
    
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) # what you type in
    Search_Title = Search_Name.lower()
    filenames = ['#','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for file_Name in filenames:
        search_URL2 = Base_Pand + 'TV/Index/A-Z/' + file_Name + '.php'
        HTML = OPEN_Search(search_URL2)
        match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>',re.DOTALL).findall(HTML)
        for url,iconimage,desc,background,name in match:
            if Search_Name in name.lower():
                if '.php' in url:
                    name = '[COLORsteelblue]'+name+'[/COLOR]'    
                    addDir(name,url,426,iconimage,background,desc)
                else:
                    name = '[COLORsteelblue]'+name+'[/COLOR]'    
                    addDirPand(name,url,222,iconimage,background,desc)
				
                    setView('movies', 'MAIN')
                    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

	
def Pandoras_Box():

    html=OPEN_URL(Base_Pand +'spongemain.php')
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
        addDirPand2(name,url,mode,img,fanart,desc)
        setView('movies', 'MAIN')
def Pandora_Menu(url):
        
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,desc,background,name in match:
            if '.php' in url:
                Watched = re.compile('url="([^"]*)"\n').findall(str(watched_read))   
                for item in Watched:											   
                    if item == url:												   
                        name = ('[COLORred]Watched - [/COLOR]'+name).replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]')                 
                addDir(name,url,426,iconimage,background,desc)
            else:
                Watched = re.compile('url="([^"]*)"\n').findall(str(watched_read))   
                for item in Watched:											   
                    if item == url:												   
                        name = ('[COLORred]Watched - [/COLOR]'+name).replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]')                 
                addDirPand(name,url,222,iconimage,background,desc)

                setView('movies', 'MAIN')			
			
                xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

			
def PANDS_open_Menu(url):

    html=OPEN_URL(url)
    match = re.compile('<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>',re.DOTALL).findall(html)
    for name,desc,url,img,fanart,mode in match:
            addDirPand2(name,url,mode,img,fanart,desc)

            setView('movies', 'MAIN')			

			
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def addDirPand(name,url,mode,iconimage,fanart,description,showcontext=True,allinfo={}):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=100107)' % sys.argv[0]))
            if showcontext == 'fav':
                contextMenu.append(('Remove from Genie TV Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Genie TV Favorites','XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDirPand2(name,url,mode,iconimage,fanart,description,showcontext=True,allinfo={}):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=100107)' % sys.argv[0]))
            if showcontext == 'fav':
                contextMenu.append(('Remove from Genie TV Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Genie TV Favorites','XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
	
	
############################################################### PANDORAS SECTION END ######################################################################################################	

#===============================Favourites------------------------------------------


'''
            if not name in FAV:
                contextMenu.append(('Add to Genie TV Favorites','XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
'''

def addon_log(string):
    if debug == 'true':
        xbmc.log("[addon.live.GenieTV-%s]: %s" %(addon_version, string))

def addFavorite(name,url,iconimage,fanart,mode,playlist=None,regexs=None):
        favList = []
        try:
            # seems that after
            name = name.encode('utf-8', 'ignore')
        except:
            pass
        if os.path.exists(favorites)==False:
            addon_log('Making Favorites File')
            favList.append((name,url,iconimage,fanart,mode,playlist,regexs))
            a = open(favorites, "w")
            a.write(json.dumps(favList))
            a.close()
        else:
            addon_log('Appending Favorites')
            a = open(favorites).read()
            data = json.loads(a)
            data.append((name,url,iconimage,fanart,mode))
            b = open(favorites, "w")
            b.write(json.dumps(data))
            b.close()
		

def getFavorites():
        if os.path.exists(favorites)==False:
            favList = []
            addon_log('Making Favorites File')
            favList.append(('Genie Tv Favourites Section','','','','','',''))
            a = open(favorites, "w")
            a.write(json.dumps(favList))
            a.close()        
        else:
			items = json.loads(open(favorites).read())
			total = len(items)
			for i in items:
				name = i[0]
				url = i[1]
				iconimage = i[2]
				try:
					fanArt = i[3]
					if fanArt == None:
						raise
				except:
					if ADDON.getSetting('use_thumb') == "true":
						fanArt = iconimage
					else:
						fanArt = fanart
				try: playlist = i[5]
				except: playlist = None
				try: regexs = i[6]
				except: regexs = None

				if i[4] == 0:
					addDir(name,url,'',iconimage,fanart,'','fav')
				else:
					addDir(name,url,i[4],iconimage,fanart,'','fav')

def rmFavorite(name):
        data = json.loads(open(favorites).read())
        for index in range(len(data)):
            if data[index][0]==name:
                del data[index]
                b = open(favorites, "w")
                b.write(json.dumps(data))
                b.close()
                break
        xbmc.executebuiltin("XBMC.Container.Refresh")
#-----------------------------------Print Addons.ini------------------------------------------------

def print_addons_ini():
        py_complete_name = os.path.join(favorites_folder,'addons.ini')
        print_default_file = open(py_complete_name,"w+")
        HTML = OPEN_URL('http://piesustv'+DDNS+':8000/get.php?username='+U+'&password='+Pass+'&type=m3u_plus&output=mpegts')
        match = re.compile('#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts').findall(HTML)
        print_default_file.write(r'['+ADDON_ID+']' +'\n')
        for name,img,group,url in match:
            url = (url+'.m3u8').replace(':','%3A').replace('/','%2F')
            final_name = (name+'=plugin://'+ADDON_ID+'/?url='+url+'&mode=10012&name='+(name).replace(' ','+')+'&amp;iconimage='+(img).replace(' ','')+'+&amp;fanart='+(img).replace(' ','')+'+&amp;description=')
            print_default_file.write(final_name+'\n')
 
#------------------------------------HELL YEAH 24/7 -----------------------------------------------------
def hellyeah():
    html=cloudflare.source(Decode('aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8='))
    match = re.compile('src="([^"]*)" type="application/x-mpegurl"/></video>',re.DOTALL).findall(html)
    for url in match:
        addDir3('24/7',url,90021,ART+'247Streams.png')
#------------------------------------ARCONAI-----------------------------------------------------
def ARCONAI():
    html=OPEN_URL(Decode('aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ=='))
    match = re.compile('EXTINF:.+?,(.+?)\n(.+?)\n#',re.DOTALL).findall(html)
    for name,url in match:
        addDir2(name,(url).strip(),222,ART+'247Streams.png',ART+'247Streams.png','')
def ARCONAI2():
    html=OPEN_URL(Decode('aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1'))
    match = re.compile('EXTINF:.+?,(.+?)\n(.+?)\n#',re.DOTALL).findall(html)
    for name,url in match:
        addDir2(name,(url).strip(),222,ART+'musicch.png',ART+'musicch.png','')
def ARCONAI3():
    html=OPEN_URL(Decode('aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U='))
    match = re.compile('EXTINF:.+?,(.+?)\n(.+?)\n#',re.DOTALL).findall(html)
    for name,url in match:
        addDir2(name,(url).strip(),222,ART+'NEWS.png',ART+'NEWS.png','')
def ARCONAI4():
    html=OPEN_URL(Decode('aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1'))
    match = re.compile('EXTINF:.+?,(.+?)\n(.+?)\n#',re.DOTALL).findall(html)
    for name,url in match:
        addDir2(name,(url).strip(),222,ART+'adult.png',ART+'adult.png','')
def TUTS():
    html=OPEN_URL(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw'))
    match = re.compile('href="/watch?v=(.+?)">(.+?)</a>',re.DOTALL).findall(html)
    for url,name in match:
        addDir2(name,url,1016,ART+'TUTS.png',ART+'TUTS.png','')
#-------------------------------------Dizzy TV-------------------------------------------------------------

def Dizzy_Menu():

    addDir('[COLOR'+TEXTCOL+']Recent Episodes[/COLOR]','',10019,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Genres[/COLOR]','',10020,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Search[/COLOR]','',10021,ART+'dtv.png',FANART,'')
#------------------------------------Dizzy Recent-----------------------------------------------------
def Recent_Scraped_Dizzy():

    html=cloudflare.source(Decode('aHR0cDovL2RpemlsYWIuY29t'))
    match = re.compile('<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>',re.DOTALL).findall(html)
    for url,img,name,episode in match:
        addDir(name + '  -  ' + (episode).replace('sezon','Season').replace('bölüm','Episode'),url,10023,ART+'dtv.png',FANART,'')

#------------------------------------Dizzy Genres----------------------------------------------------

def Dizzy_Genres():

    addDir('[COLOR'+TEXTCOL+']Action[/COLOR]','Aksiyon',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Adventure[/COLOR]','Macera',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Animation[/COLOR]','Animasyon',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Anime[/COLOR]','Anime',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Biography[/COLOR]','Biyografi',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Comedy[/COLOR]','Komedi',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Crime[/COLOR]','Su%C3%A7',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Documentary[/COLOR]','Belgesel',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Drama[/COLOR]','Dram',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Family[/COLOR]','Aile',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Fantasy[/COLOR]','Fantastik',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']History[/COLOR]','Tarih',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Horror[/COLOR]','Korku',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Mini-Series[/COLOR]','Mini%20Dizi',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Musical[/COLOR]','M%C3%BCzikal',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Mystery[/COLOR]','Gizem',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Romance[/COLOR]','Romantik',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Science Fiction[/COLOR]','Bilim%20Kurgu',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Sport[/COLOR]','Spor',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Thriller[/COLOR]','Gerilim',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']War[/COLOR]','Sava%C5%9F',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Western[/COLOR]','Tarih',10024,ART+'dtv.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Youth[/COLOR]','Gen%C3%A7lik',10024,ART+'dtv.png',FANART,'')

def Dizzy_Genre_Menu(url):
    URL = 'http://dizilab.com/arsiv?limit=100&tur='+url+'&orderby=&ulke=&order=&yil=&dizi_adi='
    HTML = cloudflare.source(URL)
    match = re.compile('<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>',re.DOTALL).findall(HTML)
    for url, img, name in match:
        addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,10022,ART+'dtv.png',FANART,'')
	

#------------------------------------Dizzy Search----------------------------------------------------

def Dizzy_Search():

    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) 
    Search_Title = Search_Name.lower()
    url = (Decode('aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' )) + (Search_Name).replace(' ','+')
    HTML = cloudflare.source(url)		
    match = re.compile('<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>').findall(HTML)    
    for url,img,name in match:
		if Search_Name in name.lower():
			addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,10022,ART+'dtv.png')
			
#------------------------------------Dizzy play ---------------------------

def Get_Dizzy_Episode(url):
    HTML = cloudflare.source(url)
    match = re.compile ('<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>',re.DOTALL).findall(HTML)
    for url2,season,ep,name in match:
        EP = (ep).replace('Sezon','').replace('bölüm','').replace('Bölüm','').replace('BÃ¶lÃ¼m','').replace('.','')
        SEASON = (season).replace('bölüm','').replace('Sezon','').replace('Bölüm','').replace('BÃ¶lÃ¼m','').replace('.','')
        NAME2 = 'Season ' + SEASON + 'Episode ' + EP + name
        Play_Dizzy_link(NAME2,url2)

        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
	
		
def Play_Dizzy_link(name,url):
    url2 = url
    NAME = name
    HTML2 = cloudflare.source(url2)
    match2 = re.compile('file: "([^"]*)",.+?label: "([^"]*)",',re.DOTALL).findall(HTML2)
    for playlink,pixel in match2:
        addDir4('[COLOR'+TEXTCOL+']' + NAME + pixel+'[/COLOR]',playlink,222,ART+'dtv.png')

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	

#-----------------------Watch EPISODES----------------------------------------------------------
'''
elif mode == 10090: Home_Menu_Episodes()
elif mode == 10091: A_Z_epi(url)
elif mode == 10092: A_Z_ser(url)
elif mode == 10093: A_Z_list(url,iconimage)
elif mode == 10094: A_Z_source(url,iconimage)
'''
def Home_Menu_Episodes():
    addDir('[COLOR'+TEXTCOL+']LATEST EPISODES[/COLOR]','http://watchepisodes.cc/',10091,ART+'WATCHSERIES.png','','')               
    addDir('[COLOR'+TEXTCOL+']A-Z[/COLOR]','http://watchepisodes.cc/series/',10092,ART+'WATCHSERIES.png','','')               
    addDir('[COLOR'+TEXTCOL+']POPULAR[/COLOR]','http://watchepisodes.cc/popular-series/',10092,ART+'WATCHSERIES.png','','')               
    addDir('[COLOR'+TEXTCOL+']SEARCH[/COLOR]','',10091,ART+'WATCHSERIES.png','','')               

def A_Z_epi(url):	
    HTML = cloudflare.source(url)
    match = re.compile('<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>',re.DOTALL).findall(HTML)
    NEXT = re.compile('([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>').findall(HTML)
    for img,url,name in match:
		addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,10094,'http://watchepisodes.cc/'+img,'','')               
    for url in NEXT:
		addDir('[COLOR'+TEXTCOL+']'+'NEXT'+'[/COLOR]',url,10091,ART + 'Next.png','','')               

def A_Z_ser(url):	
    HTML = cloudflare.source(url)
    match = re.compile('<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>',re.DOTALL).findall(HTML)
    NEXT = re.compile('([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>').findall(HTML)
    for img,url,name in match:
        img = 'http://watchepisodes.cc/'+img
        addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,10093,img,img,'')               
    for url in NEXT:
		addDir('[COLOR'+TEXTCOL+']'+'NEXT'+'[/COLOR]',url,10092,ART + 'Next.png','','')               

def A_Z_list(url,iconimage):
    img = iconimage
    HTML = cloudflare.source(url)
    match = re.compile("<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>",re.DOTALL).findall(HTML)
    for ep,url,name in match:
		addDir('[COLOR'+TEXTCOL+']'+ep+' - '+name+'[/COLOR]','http://watchepisodes.cc/'+url,10094,img,'','')               

def A_Z_source(url,iconimage):
    img = iconimage
    HTML = cloudflare.source(url)
    match = re.compile('<td>(.+?)</td>.+?<a href="([^"]*)"',re.DOTALL).findall(HTML)
    for name,url in match:
        if 'player' in name:
            pass
        elif 'vod' in name:
		    addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.','').replace('www','').replace('com','').replace(' ',''),url,10045,img,'','')               





#-----------------------Origin Watch Series ----------------------------------------------------------
'''
elif mode == 10041: Get_Watchseries_program(url)
elif mode == 10042: Get_Watchseries_Popular(url)
elif mode == 10043: Search_Watchseries()
elif mode == 10044: Get_Watchseries_Episode(url)
elif mode == 10045: Worker(url)
elif mode == 10046: Get_Watchseries_Newest(url)
elif mode == 10047: A_Z_watch(url)
elif mode == 10048: Watch_series_genres(url)
elif mode == 10049: Get_Watchseries_Prog(url)
ART+'WatchSeries.png'
'''
def Home_Menu_Watchseries():

#    addDir('[COLOR'+TEXTCOL+']A-Z[/COLOR]','http://www.watchseriesgo.to/letters/',10047,ART+'WATCHSERIES.png','','')               
    addDir('[COLOR'+TEXTCOL+']Newest Episodes Added[/COLOR]','http://www.watchseriesgo.to/latest',10046,ART+'latest.png',ART+'WatchSeries.png','')               
    addDir('[COLOR'+TEXTCOL+']This Week\'s Popular Episodes[/COLOR]','http://www.watchseriesgo.to/new',10042,ART+'popular.png',ART+'WatchSeries.png','')               
    addDir('[COLOR'+TEXTCOL+']Genres[/COLOR]','http://www.watchseriesgo.to/series',10048,ART+'Genre.png',ART+'WatchSeries.png','')                   
    addDir('[COLOR'+TEXTCOL+']Series[/COLOR]','http://www.watchseriesgo.to/series',10041,ART+'series.png',ART+'WatchSeries.png','')               
    addDir('[COLOR'+TEXTCOL+']Search Program[/COLOR]','',10043,ART+'Search.png',ART+'WatchSeries.png','')               

	
def A_Z_watch(url):	
    HTML = OPEN_URL(url)
    block = re.compile('<ul class="pagination">(.+?)</ul>',re.DOTALL).findall(HTML)
    match = re.compile('<li><a href="/letters/(.+?)">(.+?)</a></li>').findall(str(block))
    for url, name in match:
			addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]','http://www.watchseriesgo.to/letters/'+url,10049,ART+'WATCHSERIES.png','','')               
	    
def Watch_series_genres(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)" class="sr-header">(.+?)</a>').findall(HTML)
    for url,name in match:
			addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]','http://www.watchseriesgo.to/'+url,10049,ART+'WATCHSERIES.png','','')               

def Get_Watchseries_Prog(url):
    HTML = OPEN_URL(url)
    match = re.compile('<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>',re.DOTALL).findall(HTML)
    match2 = re.compile('<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div',re.DOTALL).findall(HTML)
    for url,name in match:
        if 'episode' in url:
            addDir('[COLOR'+TEXTCOL+']'+('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;',' ').replace('&','&').replace('&#039;','\'')+'[/COLOR]','http://www.watchseriesgo.to' + url,10045,ART+'WATCHSERIES.png','','')              
        else:
            addDir('[COLOR'+TEXTCOL+']'+('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;',' ').replace('&','&').replace('&#039;','\'')+'[/COLOR]','http://www.watchseriesgo.to' + url,10044,ART+'WATCHSERIES.png','','')              
    for url in match2:
         addDir('[COLOR'+TEXTCOL+']'+'NEXT'+'[/COLOR]','http://www.watchseriesgo.to' + url,10049,ART + 'Next.png','','')              
			
	
def Search_Watchseries():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) 
    Search_name = 'http://www.watchseriesgo.to/search/' + Search_Name.replace(' ','%20')
    HTML = OPEN_URL(Search_name)
    match = re.compile('<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>',re.DOTALL).findall(HTML)
    for img,url,name in match:
        if 'watch online' in name:
                pass
        else:
            print url
            addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]','http://www.watchseriesgo.to' + url,10044,img,'','')              

            xbmcplugin.setContent(addon_handle, 'movies')

def Get_Watchseries_Popular(url):			
    HTML = OPEN_URL(url)
    match = re.compile('<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>',re.DOTALL).findall(HTML)
    for img,url,name,ep,desc in match:
        season_name = ('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;',' ').replace('&','&').replace('&#039;','\'') + ' - ' + (ep).replace('&','&').replace('&#039;','\'')
        addDir('[COLOR'+TEXTCOL+']'+ season_name +'[/COLOR]','http://www.watchseriesgo.to' + url,10045,img,'',desc)              
	
def Get_Watchseries_Newest(url):
    HTML = OPEN_URL(url)
    match = re.compile('<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>',re.DOTALL).findall(HTML)
    match2 = re.compile('&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>',re.DOTALL).findall(HTML)
    for url,name in match:
        season_name = ('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;',' ').replace('&','&').replace('&#039;','\'')
        addDir('[COLOR'+TEXTCOL+']'+ season_name +'[/COLOR]','http://www.watchseriesgo.to' + url,10045,ART+'WATCHSERIES.png','','')              
    for url in match2:
         addDir('[COLOR'+TEXTCOL+']'+'NEXT'+'[/COLOR]','http://www.watchseriesgo.to' + url,10046,ART + 'Next.png','','')              

def Get_Watchseries_program(url):
    HTML = OPEN_URL(url)
    match = re.compile('<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"',re.DOTALL).findall(HTML)
    match2 = re.compile('&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>',re.DOTALL).findall(HTML)
    for url,name,img in match:
         addDir('[COLOR'+TEXTCOL+']'+('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;',' ').replace('&','&').replace('&#039;','\'')+'[/COLOR]','http://www.watchseriesgo.to' + url,10044,img,'','')              
    for url in match2:
         addDir('[COLOR'+TEXTCOL+']'+'NEXT'+'[/COLOR]','http://www.watchseriesgo.to' + url,10041,ART + 'Next.png','','')              

def Get_Watchseries_Episode(url):
    HTML = OPEN_URL(url)
    match = re.compile('<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">',re.DOTALL).findall(HTML)
    block = re.compile('<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>',re.DOTALL).findall(HTML)
    for season, Block in block:
        match = re.compile('<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n',re.DOTALL).findall(str(Block))
        for url,name in match:
            season_name = (season).replace('  ','') + ' ' + ('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&nbsp;',' ').replace('&#039;','\'').replace('  ','')		   
            addDir('[COLOR'+TEXTCOL+']'+ season_name +'[/COLOR]','http://www.watchseriesgo.to' + url,10045,ART+'WATCHSERIES.png','','')               
    match2 = re.compile('&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>',re.DOTALL).findall(HTML)
    for name,url in match:
         addDir(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('/episode/','').replace('_',' ').replace('.html',''),'http://www.watchseriesgo.to' + url,10045,ART+'WATCHSERIES.png','','')
    for url in match2:
         addDir('[COLOR'+TEXTCOL+']'+'NEXT'+'[/COLOR]','http://www.watchseriesgo.to' + url,10044,ART + 'Next.png','','')
         xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

class Watchseries():

        List = []
        source_list = []        
        def __init__(self,name):

            season_name = name
            self.Get_Sources(url,season_name)
			

        def Get_Sources(self,URL,season_name):
            dp = xbmcgui.DialogProgress()
            HTML = OPEN_URL(URL)
            match = re.compile('<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"',re.DOTALL).findall(HTML)
            for url,name in match:
                URL = 'http://www.watchseriesgo.to/link/' + url
                self.Get_site_link(URL,season_name)

        def Get_site_link(self,url,season_name):
            HTML = OPEN_URL(url)
            match = re.compile('<iframe.+? src="([^"]*)"',re.DOTALL).findall(HTML)
            match2 = re.compile('<IFRAME SRC="([^"]*)"').findall(HTML)
            match3 = re.compile('<IFRAME style=".+?" SRC="([^"]*)"').findall(HTML)
            for url in match:
                self.main(url,season_name)
            for url in match2:
                self.main(url,season_name)
            for url in match3:
                self.main(url,season_name)

        def main(self,url,season_name):
                dp.create("[COLORwhite]GenieTv[/COLOR]","Getting Sources",'','Please Wait')
                if 'daclips.in' in url:
                    source_name = 'DACLIPS'
                    if source_name in Watchseries.source_list:
					    pass
                    else:
                        self.daclips(url,season_name,source_name)
                        dp.update(0,"", "Getting Daclips Links")
                else:
                    if 'thevideo.me' in url:
                        source_name = 'THEVIDEO'
                        if source_name in Watchseries.source_list:
					        pass					        
                        else:                           
                            self.thevideo(url,season_name,source_name)
                            dp.update(0,"", "Getting Thevideo Links")
                    else:
                        if 'allmyvideos.net' in url:
                            source_name = 'ALLMYVIDEOS'
                            if source_name in Watchseries.source_list:
                                pass                    
                            else:							
                                self.allmyvid(url,season_name,source_name)
                                dp.update(0,"", "Getting Allmyvideo Links")
                        else:
                            if 'vidspot.net' in url:
                                source_name = 'VIDSPOT'
                                if source_name in Watchseries.source_list:
					                pass                            
                                else:
                                    self.vidspot(url,season_name,source_name)
                                    dp.update(0,"", "Getting Vidspot Links")
                            else:
                                if 'vodlocker' in url:
                                    source_name = 'VODLOCKER'
                                    if source_name in Watchseries.source_list:
					                    pass                                
                                    else:
                                        self.vodlocker(url,season_name,source_name)
                                        dp.update(0,"", "Getting Vodlocker Links")
                                else:
                                    if 'vidto' in url:
                                        source_name = 'VIDTO'
                                        if source_name in Watchseries.source_list:
					                        pass                                
                                        else:
                                            self.vidto(url,season_name,source_name)
                                            dp.update(0,"", "Getting Vidto Links")
                        
                                    else:
                                        if 'youwatch' in url:
                                            source_name = 'YouWatch'
                                            if source_name in Watchseries.source_list:
					                            pass                                
                                            else:
                                                self.youwatch(url,season_name,source_name)
                                                dp.update(0,"", "Getting YouWatch Links")
                        
                   
        def allmyvid(self,url,season_name,source_name):
            HTML = OPEN_URL(url)
            match = re.compile('"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"',re.DOTALL).findall(HTML)
            for Link,name in match:
                    self.Printer(Link,season_name,source_name)

        def vidspot(self,url,season_name,source_name):
            HTML = OPEN_URL(url)
            match = re.compile('"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"').findall(HTML)
            for Link,name in match:
                    self.Printer(Link,season_name,source_name)

        def thevideo(self,url,season_name,source_name):
            HTML = OPEN_URL(url)
            match = re.compile('{"file":"([^"]*)"').findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)

        def vodlocker(self,url,season_name,source_name):
            HTML = OPEN_URL(url)
            match = re.compile('file: "([^"]*)"').findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)

        def daclips(self,url,season_name,source_name):
            HTML = OPEN_URL(url)
            match = re.compile('{ file: "([^"]*)", type:"video" }').findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)

        def filehoot(self,url,season_name,source_name):
            HTML = OPEN_URL(url)
            match = re.compile('file: "([^"]*)"').findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)
        def vidto(self,url,season_name,source_name):
            HTML = OPEN_URL(url)
            match = re.compile('file: "([^"]*)"').findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)
        def youwatch(self,url,season_name,source_name):
            HTML = OPEN_URL(url)
            match = re.compile('<iframe src="([^"]*)"').findall(HTML)
            for Link in match:
                    self.youplay(Link,season_name,source_name)
        def youplay(self,url,season_name,source_name):
            HTML = OPEN_URL(url)
            match = re.compile('file: "([^"]*)"').findall(HTML)
            for Link in match:
                    self.Printer(Link,season_name,source_name)

        def Printer(self,Link,season_name,source_name):

                if Link in Watchseries.List:
                    pass
                elif source_name in Watchseries.source_list:
				    pass
                else:
                    addDir4('[COLOR'+TEXTCOL+']'+source_name+'[/COLOR]',Link,222,ART+'WATCHSERIES.png')
                    dp.update(100,"", "Got Source")
                    Watchseries.List.append(Link)                    
                    Watchseries.source_list.append(source_name)
					
		    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	



#---------------------Origin Football------------------------------------------------------------------

def Origin_Football():
    addDir('[COLOR'+TEXTCOL+']Highlights[/COLOR]','',10008,ART + 'Highlights.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Fixtures[/COLOR]','',10009,ART + 'Fixtures.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Live Sport On G-Tv[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=')),7080,ART + 'Sport.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Premier League Table[/COLOR]','http://www.bbc.co.uk/sport/football/premier-league/table',50002,ART + 'PremiereLeague.png',FANART,'')

def premtable(url):
    team_total='20'
    results = []
    sp1 = '                                                    '
    sp2 = '        '
    addDir(sp1+'pl'+sp2+'w'+sp2+'d'+sp2+'l'+sp2+'f'+sp2+'a'+sp2+'pts','','','','','')
    html=OPEN_URL_1(url)
    match = re.compile('<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>',re.DOTALL).findall(html)
    for team,pl,w,d,l,f,a,dif,pts in match:
        pl_sp = clean_space(pl)
        w_sp = clean_space(w)
        d_sp = clean_space(d)
        l_sp = clean_space(l)
        f_sp = clean_space(f)
        a_sp = clean_space(a)
        results.append(team[0])
        pos = len(results)
        sp_no = int(len(sp1)-len(team)-2)
        if len(results)>=10:
            sp_no = sp_no - 1
        if len(results)<=int(team_total):
			addDir2(str(pos)+' '+team+sp1[0:sp_no]+pl+pl_sp+w+w_sp+d+d_sp+l+l_sp+f+f_sp+a+a_sp+' '+pts,'','','','','')
            
#str(pos)+' '+team+sp1[0:sp_no]+pl+pl_sp+w+w_sp+d+d_sp+l+l_sp+f+f_sp+a+a_sp+' '+pts
def clean_space(space):
    if len(space)>1:
        no = len('        ')-len(space)+1
        space = int(no)*' '
    elif len(space)==1:
        space = '        '
    return space

'''
def premtable(url):
    addDir('[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]','','','','','')
    html=OPEN_URL(url)
    match = re.compile('<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>',re.DOTALL).findall(html)
    for pos,url,team,pl,w,d,l,f,a,pts,dif in match:
        team = team
        if 'Arsenal' in team:
            image = ART+'arsenal-logo.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                                  '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Bournemouth' in team:
            image = ART+'afc-bournemouth.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                       '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Burnley' in team:
            image = ART+'KEGnQWW.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                                   '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Chelsea' in team:
            image = ART+'chelsea.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                                  '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Crystal' in team:
            image = ART+'CrystalPalace.0.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                       '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Everton' in team:
            image = ART+'Everton.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                                   '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Hull' in team:
            image = ART+'hull-city-afc.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                                 '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Leicester' in team:
            image = ART+'leicester-city-fc-hd-logo.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                       '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Liverpool' in team:
            image = ART+'liverpool-logo.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                               '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Manchester City' in team:
            image = ART+'city-logo.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'               '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Manchester United' in team:
            image = ART+'91.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'          '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Middlesbrough' in team:
            image = ART+'middlesbrough-fc-hd-logo.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                 '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Southampton' in team:
            image = ART+'southampton-fc-logo.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                   '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Stoke City' in team:
            image = ART+'stoke-city.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                          '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Sunderland' in team:
            image = ART+'sunderland-logo.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                        '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Swansea' in team:
            image = ART+'swansea-city-afc.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                    '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Tottenham' in team:
            image = ART+'tottenham-hotspur_zps4e3ed7c1.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'        '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Watford' in team:
            image = ART+'watford-fc-hd-logo.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'                              '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'Bromwich' in team:
            image = ART+'west-bromwich-albion-logo.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'   '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        elif 'West Ham' in team:
            image = ART+'west-ham.png'
            name = '[COLOR'+TEXTCOL+']'+pos+' - '+team+'             '+pl+'        '+w+'        '+d+'        '+l+'        '+f+'        '+a+'        '+pts+'[/COLOR]'
        addDir(str(name),(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=')),50003,image,image,team)

def Table_Menu(description):
    team = description
    url = ('http://www.fullmatchesandshows.com/?s='+team).replace(' ','%20')
    get_All_Rows2(url)
'''			
def FootballFixturesDay():
    html=OPEN_URL(Decode('aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s'))
    match = re.compile('<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"',re.DOTALL).findall(html)
    for url,img,name in match:
        addDir('[COLOR'+TEXTCOL+']'+('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('amp;','')+'[/COLOR]',Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + url,10010,Decode('aHR0cDovL2xpdmVvbnNhdC5jb20v') + img,FANART,'')
	
def FootballFixturesGame(url):
    HTML = OPEN_URL(url)
    block = re.compile('AndClearL.+?><h2.+?head>(.*?)float',re.DOTALL).findall(HTML)
    for block in block:
        day = re.compile('(.*?)</h2>').findall(str(block))
        for Day in day:
            Day = Day
        game = re.compile('comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->',re.DOTALL).findall(str(block))
        for comp,img,time,chan in game:
            channel = re.compile(",CAPTION, '(.+?)&nbsp").findall(chan)
            addDir('[COLOR'+TEXTCOL+']' + Day + ' - ' + comp + ' - ' + time + '[/COLOR]','',10010,Decode('aHR0cDovL2xpdmVvbnNhdC5jb20=') + img,FANART,(str(channel)))

    setView('tvshows', 'Media Info 3')

def Football_Highlights():
    addDir('[COLOR'+TEXTCOL+']Latest[/COLOR]','http://www.fullmatchesandshows.com',10011,'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']EURO 2016[/COLOR]','http://www.fullmatchesandshows.com/euro-2016/',10011,'http://football.mywapblog.com/files/uefa-euro-2016-logo.png',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']Shows[/COLOR]','http://www.fullmatchesandshows.com/category/show/',10011,'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']Premier League[/COLOR]','http://www.fullmatchesandshows.com/premier-league/',10011,'https://footballseasons.files.wordpress.com/2013/05/premier-league.png',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']La Liga[/COLOR]','http://www.fullmatchesandshows.com/la-liga/',10011,'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']Bundesliga[/COLOR]','http://www.fullmatchesandshows.com/bundesliga/',10011,'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']Champions League[/COLOR]','http://www.fullmatchesandshows.com/champions-league/',10011,'http://www.ecursuri.ro/images/teste/test-champions-league.jpg',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']Serie A[/COLOR]','http://www.fullmatchesandshows.com/category/serie-a/',10011,'http://files.jcriccione.it/200000223-2484526782/serie%20a.png',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']Ligue 1[/COLOR]','http://www.fullmatchesandshows.com/category/ligue-1/',10011,'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']Copa America 2015[/COLOR]','http://www.fullmatchesandshows.com/copa-america-2015/',10011,'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']CONCACAF[/COLOR]','http://www.fullmatchesandshows.com/category/concacaf/',10011,'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png',ART + 'fanart.jpg','')
    addDir('[COLOR'+TEXTCOL+']Women World Cup[/COLOR]','http://www.fullmatchesandshows.com/category/women-world-cup/',10011,'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png',ART + 'fanart.jpg','' )

def get_All_Rows(url):
    addDir('[COLOR'+TEXTCOL+']Live On G-Tv[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=')),7080,ART + 'TodaysMacthes.png',FANART,'')
    HTML = OPEN_URL(url)
    match = re.compile('class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>',re.DOTALL).findall(HTML)
    match2 = re.compile('<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>',re.DOTALL).findall(HTML)
    for img,url,name in match:
        Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
        if 'Highlights &' in name:
		    pass
        else:
            Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
            addDir4('[COLOR'+TEXTCOL+']'+Name+'[/COLOR]',url,10013,img)
    for url,img,name in match2:
        Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
        if 'Highlights &' in name:
		    pass
        else:
            addDir4('[COLOR'+TEXTCOL+']'+Name+'[/COLOR]',url,10013,img)
def get_All_Rows2(url):
    addDir('[COLOR'+TEXTCOL+']Live On G-Tv[/COLOR]',(Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=')),7080,ART + 'TodaysMacthes.png',FANART,'')
    HTML = OPEN_URL(url)
    match = re.compile('class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>',re.DOTALL).findall(HTML)
    match2 = re.compile('<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>',re.DOTALL).findall(HTML)
#    for img,url,name in match:
#        Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
#        if 'Highlights &' in name:
#		    pass
#        else:
#            Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
#            addDir4('[COLOR'+TEXTCOL+']'+Name+'[/COLOR]',url,10013,img)
    for url,img,name in match2:
        Name = name.replace('&#8211;', '-').replace('&#038;', '&').replace('&#8217;', '')
        if 'Highlights &' in name:
		    pass
        else:
            addDir4('[COLOR'+TEXTCOL+']'+Name+'[/COLOR]',url,10013,img)

def get_PLAYlink(url):
    HTML = OPEN_URL(url)
    match = re.compile('<script data-config="([^"]*)" data-height').findall(HTML)
    for playlink in match:
        Playlink = (playlink).replace('/v2', '').replace('zeus.json', 'video-sd.mp4?hosting_id=21772').replace('config.playwire.com', 'cdn.video.playwire.com')
        RESOLVER('http:'+Playlink)
		

				
#------------------------------GenieTv Kitchen---------------------------------------------------------------------
def DOCjl1(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"',re.DOTALL).findall(html)
    match2 = re.compile("<a rel='next' href=([^=]*)=",re.DOTALL).findall(html)
    for url,name,img in match:
                addDir4(name,url,8046,img)
    for url in match2:
        addDir3('NEXT PAGE',(url).replace(' class',''),8045,ART + 'Next.png')
def DOCjl2(url):
    html=OPEN_CAT(url)
    match = re.compile("__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)',",re.DOTALL).findall(html)
    for url,img,name in match:
        RESOLVER('http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/'+url)

def DOCjl3(url):
    html=OPEN_CAT(url)
    match = re.compile("src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>").findall(html)
    for url in match:
        yt.PlayVideo(url)
#------------------------------DOCUMENTARIES---------------------------------------------------------------------
def DOC1():
    addDir3('[COLOR'+TEXTCOL+']Documentary Lovers[/COLOR]','http://documentarylovers.com/',80009,ART+'documentary.png')
    addDir3('[COLOR'+TEXTCOL+']RTD Documentaries[/COLOR]','https://rtd.rt.com/',8048,ART+'documentary.png')
    addDir3('[COLOR'+TEXTCOL+']Search Docs[/COLOR]','',80012,ART+'Search.png')
    html=OPEN_CAT(Decode('aHR0cDovL2RvY3VyLmNvLw=='))
    match = re.compile('<a href="([^"]*)" class=.+? title="([^"]*)">').findall(html)
    for url,name in match:
        addDir3(name,url,8041,ART+'documentary.png')
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
def DOC2(url):
    html=OPEN_CAT(url)
    match = re.compile('<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>').findall(html)
    next = re.compile('<a href="([^"]*)" rel=next>',re.DOTALL).findall(html)
    for img,url,name in match:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#039;s',''),'http://docur.co'+url,8042,'http://docur.co'+img)                
    for url in next:
        addDir3('NEXT PAGE',url,8041,ART + 'Next.png')
 
	
def DOC3(url):
    html=OPEN_CAT(url)
    match = re.compile('<iframe.+?src="([^"]*)"').findall(html)
    match2 = re.compile('<iframe.+?src="([^"]*)"').findall(html)
    for url in match:
        if 'youtube' in url:
            url = (url).replace('https://www.youtube.com/embed/','')
            addDir4('[COLOR'+TEXTCOL+']YouTube[/COLOR]',url,8043,ART+'documentary.png')
        else:
            addDir3('[COLOR'+TEXTCOL+']doclist[/COLOR]','http:'+url,8044,'')
def DOCLIST(url):
    html=OPEN_CAT(url)
    match = re.compile('}],"([^"]*)":.+?,"url":"([^"]*)"',re.DOTALL).findall(html)
    for name,url in match:
        url = (url).replace('\/','/')
        addDir4('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,222,'')	
		
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
def addCONTEXT(name,url):
	menuTotal=0
	name = name
	url=url
	choices = ['144','240','380','480','720']
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Resolution[/COLOR]', choices)
	if choice==0:
		RESOLVEtest(url)
#	url = url
#	name = name
#	menuTotal=0
#
#	if menuTotal==0: MenuItem = xbmcgui.Dialog().select('[COLOR cyan]'+name+'[/COLOR]', ['[COLOR cyan]Launch[/COLOR]','[COLOR ghostwhite]No Preview Video[/COLOR]','[COLOR tomato]Uninstall[/COLOR]'])
#	if MenuItem==0:
#		RESOLVEtest(url)

def LOVERS():
    html=OPEN_CAT('http://documentarylovers.com/')
    match = re.compile('title="([^"]*)" href="([^"]*)"').findall(html)
    for name,url in match:
        if 'genre' in url:
            addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#038;','and').replace('&amp;','and'),url,80010,ART+'documentary.png')
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
def LOVERS2(url):
    html=OPEN_CAT(url)
    match = re.compile('href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"',re.DOTALL).findall(html)
    next = re.compile('rel="next" href="([^"]*)"').findall(html)
    for url,name,img in match:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8217;','').replace('&#038;','and').replace('&amp;','and'),url,80011,img)
    for url in next:
        addDir3('NEXT PAGE',url,80010,ART + 'Next.png')

def LOVERS3(url):
    html=OPEN_CAT(url)
    match = re.compile('data-video="youtube" data-src="([^"]*)"><div').findall(html)
    match2 = re.compile('itemprop="embedURL" content="([^"]*)"><meta').findall(html)
    for url in match:
        addDir4('[COLOR'+TEXTCOL+']YouTube[/COLOR]',url,8043,ART+'documentary.png')
    for url in match2:
        DOCLIST(url)

def searchLOVERS():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = 'http://documentarylovers.com/?s='+(Search_Name).replace(' ','+')
    Search_Title = Search_Clean_Name.lower()
    LOVERS2(Search_Title)

def rtd(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="([^"]*)" title="([^"]*)">',re.DOTALL).findall(html)
    match2 = re.compile('rel="next" href="([^"]*)">»</a>').findall(html)
    for url,name in match:
        if 'films' in url:
            addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#038;','and').replace('&#8217;','and'),'https://rtd.rt.com'+url,8049,ART+'documentary.png')
def rtd2(url):
    html=OPEN_CAT(url)
    match = re.compile('<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>',re.DOTALL).findall(html)
    match2 = re.compile('rel="next" href="([^"]*)">»</a>').findall(html)
    for img,url,name in match:
        if 'films' in url:
            addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#038;','and').replace('&#8217;','and'),'https://rtd.rt.com'+url,804900,'https://rtd.rt.com'+img)
    for url in match2:
        addDir3('NEXT',url,8049,ART+'Next.png')
def rtd3(url):
    html=OPEN_CAT(url)
    match = re.compile('src="([^"]*)" frameborder=').findall(html)
    for url in match:
        if 'rtd' in url:
            rtdPlay(url)

def rtdPlay(url):
    html=OPEN_CAT(url)
    match = re.compile("{file: '([^']*)' + '([^']*)'}").findall(html)
    for link,file in match:
        url = ('https://rtd.rt.com'+link+file)
        RESOLVEtest(url)

#------------------------------WORLD TV---------------------------------------------------------------------
def get_Country():
    HTML = OPEN_CAT('http://www.stream2watch.co/live-tv')
    match = re.compile('<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>',re.DOTALL).findall(HTML)
    for url,img,name,name2 in match:
        addDir3((name+'[COLOR'+TEXTCOL+']'+name2+'[/COLOR]'),url,8086,img)

def get_Channel(url):
    HTML = OPEN_CAT(url)
    match = re.compile('<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>',re.DOTALL).findall(HTML)
    for url,img,name in match:
        addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,8087,img)

def get_Part_1_Link(url):
    HTML = OPEN_URL(url)
    match = re.compile('a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>',re.DOTALL).findall(HTML)
    for url,name in match:
        Get_Playlink(url,name)
	
def Get_Playlink(url,name):
    HTML = OPEN_URL(url)
    match = re.compile("playStream\('.+?', '(.+?)'\);",re.DOTALL).findall(HTML)
    for url in match:
        print url
        addDir4('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,222,'')
#------------------------------CLASSICS---------------------------------------------------------------------
def CLASSICS1():
    html=OPEN_CAT(Decode('aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA=='))
    match = re.compile('<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>',re.DOTALL).findall(html)
    for url,img,name in match:
			    addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('</TD>','').replace('<BR>',' ').replace('</H3>','').replace('/<br>',' ').replace('</a>','').replace('<br>','').replace('<H3>',''),'http://www.solie.org/alibrary/'+url,3002,'http://www.solie.org/alibrary/'+img)
def CLASSICS2(url):
    html=OPEN_CAT(url)
    match = re.compile('<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>',re.DOTALL).findall(html)
    for url,img,name in match:
			    addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('</TD>','').replace('<BR>',' ').replace('</H3>','').replace('/<br>',' ').replace('</a>','').replace('<br>','').replace('<H3>',''),'http://www.solie.org/alibrary/'+url,3003,'http://www.solie.org/alibrary/'+img)
def CLASSICS3(url):
    html=OPEN_CAT(url)
    match = re.compile('<br><a href="([^"]*)">(.+?)</a>').findall(html)
    series = re.compile('href="([^"]*)">Season(.+?)</a>').findall(html)
    next = re.compile('<a href="([^"]*)">Episodes</a>').findall(html)
    match2 = re.compile('<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>',re.DOTALL).findall(html)
    for url,name in match:
			    addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('</TD>','').replace('<BR>',' ').replace('</H3>','').replace('/<br>',' ').replace('</a>','').replace('<br>','').replace('<H3>',''),'http://www.solie.org/alibrary/'+url,3004,ART+'classicmovies.png')
    for url,name in series:
                addDir3('[COLOR'+TEXTCOL+']Season- '+name+'[/COLOR]','http://www.solie.org/alibrary/'+url,3003,ART+'classicmovies.png')
    for url in next:
			    addDir3('[COLOR'+TEXTCOL+']NEXT[/COLOR]','http://www.solie.org/alibrary/'+url,3003,ART + 'Next.png')
    for url,img,name in match2:
			    addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('</TD>','').replace('<BR>',' ').replace('</H3>','').replace('/<br>',' ').replace('</a>','').replace('<br>','').replace('<H3>',''),'http://www.solie.org/alibrary/'+url,3003,'http://www.solie.org/alibrary/'+img)
def CLASSICS4(url):
    html=OPEN_CAT(url)
    match = re.compile('<iframe.+?src="([^"]*)"').findall(html)
    for url in match:
			    CLASSICSPLAY(url)
def CLASSICSPLAY(url):
    html=OPEN_CAT(url)
    match = re.compile('<meta property="og:video" content="([^"]*)"/>').findall(html)
    for url in match:
			    RESOLVEtest(url)
#------------------------------Classic Movies---------------------------------------------------------------------
def classic_TV():
    html=OPEN_CAT(Decode('aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8='))
    match = re.compile('<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>').findall(html)
    for url,name in match:
			    addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8211;',':'),url,8065,ART+'classicmovies.png')
def classic_TV2(url):
    html=OPEN_CAT(url)
    match = re.compile("v.src = '([^']*)';").findall(html)
    for url in match:
			    RESOLVE(url)
#------------------------------Classic Tv---------------------------------------------------------------------
def classic_TVshows():
    html=OPEN_CAT(Decode('aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv'))
    match = re.compile('<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>').findall(html)
    for url,name in match:
			    addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#8211;',':'),url,8065,ART+'classictv.png')
def classic_TVshows2(url):
    html=OPEN_CAT(url)
    match = re.compile('href="([^"]*)">',re.DOTALL).findall(html)
    match2 = re.compile("videoId: '([^']*)'",re.DOTALL).findall(html)
    for url in match:
        if 'mp4' in url:
			RESOLVEtest(url)
    for url in match2:
		yt.PlayVideo(url)
#------------------------------M3U SCRAPE---------------------------------------------------------------------
def Get_m3u_links():
    HTML = OPEN_URL(Decode('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw=='))
    match = re.compile('<li><a href="([^"]*)"> (.+?).m3u</a></li>').findall(HTML)
    for url,name in match:
        addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('-',' ').replace('_',' '),(Decode('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8='))+url,8071,ART + 'streams.png')  	
def Get_m3u_playlinks(url):
    HTML = OPEN_CAT(url)
    match = re.compile('EXTINF:.+?,(.+?)\n(.+?)\n#',re.DOTALL).findall(HTML)
    for name,url in match:
		if '(Free Access)' in name:
			url = (url).strip()
		else:
			url = ((Decode('aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv'))+U+'/'+Pass+url).strip()
		addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('_',' ').replace('(Free Access)','[COLORwhite] - Free Access[/COLOR]'),url,222,ART + 'streams.png')
def Get_List_playlinks(url):
    HTML = OPEN_CAT(url)
    match = re.compile('EXTINF:(.+?),(.+?)\n(.+?)\n#',re.DOTALL).findall(HTML)
    for img,name,url in match:
        url = ((Decode('aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv'))+U+'/'+Pass+url).strip()
        addDir2(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('_',' '),url,222,img,fanart,'')
#------------------------------Xvid SCRAPE---------------------------------------------------------------------
def X_vid_Menu():
	choices = ['[COLOR'+TEXTCOL+']XXX Vids[/COLOR]','[COLOR'+TEXTCOL+']Perfect Girls[/COLOR]','[COLOR'+TEXTCOL+']Best Videos[/COLOR]','[COLOR'+TEXTCOL+']Genres[/COLOR]','[COLOR'+TEXTCOL+']Recently Uploaded[/COLOR]','[COLOR'+TEXTCOL+']100% Verified[/COLOR]','[COLOR'+TEXTCOL+']Tags[/COLOR]','[COLOR'+TEXTCOL+']In Your Language[/COLOR]','[COLOR'+TEXTCOL+']Search[/COLOR]']
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']TOOLS[/COLOR]', choices)
	if choice==0:
		XXXHD('http://watchxxxfree.com/categories')
	if choice==1:
		Xperfect('http://www.perfectgirls.net')
	if choice==2:
		XNew_Videos('http://www.xvideos.com/best')
	if choice==3:
		XGenres('http://www.xvideos.com/best')
	if choice==4:
		XNew_Videos('http://www.xvideos.com/best')
	if choice==5:
		XNew_Videos('http://www.xvideos.com/verified/videos')
	if choice==6:
		Xtags('http://www.xvideos.com/tags')
	if choice==7:
		X_vid_Lang('http://www.xvideos.com/porn')
	if choice==8:
		XSearch_X()
#    addDirFolder('[COLOR'+TEXTCOL+']Best Videos[/COLOR]','http://www.xvideos.com/best',10105,ART+'Jizbox.png','','')
#    addDirFolder('[COLOR'+TEXTCOL+']Genres[/COLOR]','http://www.xvideos.com',10106,ART+'Jizbox.png','','')
#    addDirFolder('[COLOR'+TEXTCOL+']Recently Uploaded[/COLOR]','http://xvideos.com',10105,ART+'Jizbox.png','','')
#    addDirFolder('[COLOR'+TEXTCOL+']100% Verified[/COLOR]','http://www.xvideos.com/verified/videos',10105,ART+'Jizbox.png','','')
#    addDirFolder('[COLOR'+TEXTCOL+']Tags[/COLOR]','http://www.xvideos.com/tags',10103,ART+'Jizbox.png','','')
#    addDirFolder('[COLOR'+TEXTCOL+']PornStars[/COLOR]','http://www.xvideos.com/pornstars',10104,ART+'Jizbox.png','','')
#    addDirFolder('[COLOR'+TEXTCOL+']In Your Language[/COLOR]','http://www.xvideos.com/porn',101001,ART+'Jizbox.png','','')
#    addDirFolder('[COLOR'+TEXTCOL+']Search[/COLOR]','',10107,ART+'Jizbox.png','','',)
	
def wetsex(url):
    HTML = OPEN_URL(url)
    match = re.compile("<a target='_blank' href='([^']*)'><span>(.+?)</span>").findall(HTML)
    for url,name in match:
        if 'ch' in url:
            addDirFolder('[COLOR'+TEXTCOL+']'+name + '[COLORorange]   Videos[/COLOR]','http://www.wetsextube.com'+url,90008,ART+'Jizbox.png',ART+'Jizbox.png','')	
def wetsex2(url):
    HTML = OPEN_URL(url)
    match = re.compile("<a class=.+?href='([^']*)' rel=.+? title='([^']*)'",re.DOTALL).findall(HTML)
    next_button = re.compile('class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">').findall(HTML)
    for url,name in match:
        addDir2(('[COLOR'+TEXTCOL+']'+name + '[/COLOR]').replace('&#8211;','-').replace('&#039;',''),'http://www.wetsextube.com'+url,90009,ART+'Jizbox.png','','')	
    for name,url in next_button:
        addDir('[COLOR'+TEXTCOL+']'+name + '[/COLOR]','http://www.wetsextube.com'+url,90008,ART+'Next.png','','')
def wetsex3(url):
    HTML = OPEN_URL(url)
    match = re.compile('data-lazy-src="([^"]*)" frameborder=',re.DOTALL).findall(HTML)
    for url in match:
        if 'jetload' in url:
            XXXHDPLAY(url)	
def wetsexPLAY(url):
    HTML = OPEN_URL(url)
    match = re.compile('file: "([^"]*)",').findall(HTML)
    for url in match:
        RESOLVEtest(url)
def XXXHD(url):
    HTML = OPEN_URL(url)
    match = re.compile('data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>',re.DOTALL).findall(HTML)
    for img,url,name,no in match:
        if 'category' in url:
            addDirFolder('[COLOR'+TEXTCOL+']'+name + '[COLORorange]   ' +no+'[/COLOR]',url,90006,img,ART+'Jizbox.png','')	
def XXXHD2(url):
    HTML = OPEN_URL(url)
    match = re.compile('data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">',re.DOTALL).findall(HTML)
    next_button = re.compile('<link rel="next" href="([^"]*)"/>').findall(HTML)
    for img,url,name in match:
        addDir2(('[COLOR'+TEXTCOL+']'+name + '[/COLOR]').replace('&#8211;','-'),url,90007,img,'','')	
    for url in next_button:
        addDir('[COLORred]NEXT[/COLOR]',url,90006,ART+'Next.png','','')
def XXXHD3(url):
    HTML = OPEN_URL(url)
    match = re.compile('data-lazy-src="([^"]*)" frameborder=',re.DOTALL).findall(HTML)
    for url in match:
        if 'jetload' in url:
            XXXHDPLAY(url)	
def XXXHDPLAY(url):
    HTML = OPEN_URL(url)
    match = re.compile('file: "([^"]*)",').findall(HTML)
    for url in match:
        RESOLVEtest(url)
def Xperfect(url):
    HTML = OPEN_URL(url)
    match = re.compile('<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>',re.DOTALL).findall(HTML)
    for url,name,no in match:
        if 'category' in url:
            addDirFolder('[COLOR'+TEXTCOL+']'+name + '[COLORorange]' +no+'[/COLOR]','http://www.perfectgirls.net'+url,90003,ART+'Jizbox.png','','')	
def Xperfect2(url):
    HTML = OPEN_URL(url)
    url2 = url
    match = re.compile('<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"',re.DOTALL).findall(HTML)
    next_button = re.compile('rel="next" href="([^"]*)">Next &raquo;</a>').findall(HTML)
    for url,name,img in match:
        addDir2('[COLOR'+TEXTCOL+']'+name + '[/COLOR]','http://www.perfectgirls.net'+url,90004,img,'','')	
    for url in next_button:
        addDir('[COLORred]NEXT[/COLOR]',url2+'/'+url,90003,ART+'Next.png','','')	
def Xperfect3(url):
    HTML = OPEN_URL(url)
    match = re.compile('get\("(.*)", function').findall(HTML)
    for url in match:
        Xperfectplayer('http://www.perfectgirls.net'+url)	
def Xperfectplayer(url):
    HTML = OPEN_URL(url)
    match = re.compile('http://(.+?)\n').findall(HTML)
    for url in match:
        RESOLVER('http://'+url)	
def X_vid_Lang(url):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>').findall(HTML)
    for url,name,no in match:
        addDirFolder('[COLOR'+TEXTCOL+']'+name + '[COLORgreen] - No of Videos : [COLORorange]' +no+'[/COLOR]','http://www.xvideos.com'+url,10105,ART+'Jizbox.png','','')	
def Xtags(url):
    HTML = OPEN_URL(url)
    next_button = re.compile('<li><a class=".+?".+?href="([^"]*)">Next</a></li>').findall(HTML)
    for url in next_button:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,10103,ART+'Jizbox.png','','')	
    match = re.compile('<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>').findall(HTML)
    for url,name,no in match:
        addDirFolder(('[COLOR'+TEXTCOL+']'+name + '[COLORgreen] - No of Videos : [COLORorange]' + (no+'[/COLOR]')).replace('"></span>',' ').replace('<span class="flag-small flag-','').replace('>',''),'http://www.xvideos.com'+url,10105,ART+'Jizbox.png','','')

def XPornstars(url):
    HTML = OPEN_URL(url)
    next_button = re.compile('<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>').findall(HTML)
    for url in next_button:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,10104,ART + 'Next.png','','')
    match = re.compile(':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n',re.DOTALL).findall(HTML)
    for img,url,name,count in match:
        addDirFolder(name+'--'+(count).replace('&nbsp;','').replace('			',''),'http://www.xvideos.com'+url+'#_tabVideos,videos-best',10105,(img).replace('http:\/\/','http://'),'','')        
		
	  
def XNew_Videos(url):
    HTML = OPEN_URL(url)
    match = re.compile('data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="mobile-hide">(.+?)<.+?class="duration">(.+?)<',re.DOTALL).findall(HTML)
    match2 = re.compile('data-src="([^"]*)" .+? href="([^"]*)" title="([^"]*)">.+?class="duration">(.+?)<',re.DOTALL).findall(HTML)
    for img,url,name,views,length in match:
        addDirFolder('[COLORorangered]'+name + '[COLORgreen] - Porn Quality : [COLORorange]' + views + ' - [COLORred]' + length+'[/COLOR]','http://www.xvideos.com'+url,10108,img,img,views + ' - ' + length)	
    next_button2 = re.compile('<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>').findall(HTML)
    for img,url,name,length in match2:
        addDirFolder('[COLORorangered]'+name + '[COLORgreen] - Porn Quality : [COLORorange]' + length+'[/COLOR]','http://www.xvideos.com'+url,10108,img,img,length)	
    next_button2 = re.compile('<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>').findall(HTML)
    for url in next_button2:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,10105,ART + 'Next.png','','')

    
def XGenres(url):
    HTML = OPEN_URL(url)
    block = re.compile('<div class="main-categories">(.+?)</div>',re.DOTALL).findall(HTML)
    next_button = re.compile('<li><a class=".+?".+?href="([^"]*)">Next</a></li>').findall(HTML)
    for url in next_button:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,10106,ART + 'Next.png','','')
    match = re.compile('<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>').findall(str(block))
    for url,name in match:
        if '/c/' in url:
	        addDirFolder('[COLOR'+TEXTCOL+']'+name+'[/COLOR]','http://www.xvideos.com'+url,10105,ART+'Jizbox.png','','')

		
def XSearch_X():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean = (Search_Name).replace(' ','+').replace('&','&')
    Search_Title = Search_Clean.lower()
    Search_URL = 'http://www.xvideos.com/?k=' + Search_Title
    print Search_URL + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
    HTML = OPEN_URL(Search_URL)
    match = re.compile('<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<',re.DOTALL).findall(HTML)
    for img,url,name,length,rating in match:
        addDirFolder('[COLOR'+TEXTCOL+']'+name + '[COLORgreen] - Porn Quality : [COLORorange]' + rating + ' - [COLORred]' + length+'[/COLOR]','http://www.xvideos.com'+url,10108,img,img,rating + ' - ' + length)	
    next_button2 = re.compile('<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>').findall(HTML)
    for url in next_button2:
        addDirFolder('[COLORred]NEXT[/COLOR]','http://www.xvideos.com'+url,10105,ART + 'Next.png','','')
'''
def XSearch_X():
  
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) 
    Search_Title = Search_Name.lower()
    url = 'http://www.xvideos.com/?k=' + Search_Title
    url2 = 'http://www.perfectgirls.net/search/' + Search_Title + '/'

    dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Checking Sources",'','Please Wait')	
    HTML = OPEN_Search(url)
    dp.update(0,"", "Checking Source XVID Links")
    HTML2 = OPEN_Search(url2)
    dp.update(100,"", "Checking Source PERFECT GIRLS Links")

    if HTML != 'Failed':			
        match=re.compile('<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<').findall(HTML)
        for img,url,name,length,rating in match:
				if Search_Title in name.lower():
					addDirFolder('[COLOR'+TEXTCOL+']'+name + '[COLORgreen] - Porn Quality : [COLORorange]' + rating + ' - [COLORred]' + length+'[/COLOR]','http://www.xvideos.com'+url,10108,img,img,rating + ' - ' + length)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(50,"", "Getting XVID Links")
					
					setView('tvshows', 'Media Info 3')
	
    if HTML2 != 'Failed':			
        match2=re.compile('<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"',re.DOTALL).findall(HTML2)
        for url,name,img in match2:
				if Search_Title in name.lower():
					('[COLOR'+TEXTCOL+']'+name + '[/COLOR]','http://www.perfectgirls.net'+url,90004,img,'','')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(100,"", "Getting PERFECT GIRLS Links")
					
					setView('tvshows', 'Media Info 3')	
'''

def XPlayLink(url):
    HTML = OPEN_URL(url)
    match = re.compile("setVideoUrlLow.+?'([^']*)'").findall(HTML)
    match2 = re.compile("setVideoUrlHigh.+?'([^']*)'").findall(HTML)
    match3 = re.compile("setVideoHLS.+?'([^']*)'").findall(HTML)
    for url in match:
        if 'http' in url:
            addDir4('[COLOR'+TEXTCOL+']Quality = [COLORred]SQUINT[/COLOR]',url,222,ART+'Jizbox.png')
    for url in match2:
        if 'http' in url:
            addDir4('[COLOR'+TEXTCOL+']Quality = [COLORyellow]ENJOY[/COLOR]',url,222,ART+'Jizbox.png')
    for url in match3:
        if 'http' in url:
            addDir4('[COLOR'+TEXTCOL+']Quality = [COLORgreen]GO BLIND[/COLOR]',url,222,ART+'Jizbox.png')
		
def XResolveTwo(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass

#------------------------------Go Fishing SCRAPE---------------------------------------------------------------------
'''
elif mode == 8090:
		Get_XNXX_CATS()
elif mode == 8091:
		Get_XNXX_VIDS(url)
elif mode == 8092:
		Get_XNXX_playlinks(url)
elif mode == 8093:
		Get_XNXX_next(url)
'''
def Get_XNXX_CATS():
    HTML = OPEN_URL(Decode('aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw=='))
    match = re.compile('<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>',re.DOTALL).findall(HTML)
    for url,name in match:
        addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,8091,ART+'gofish.png')  	
def Get_XNXX_VIDS(url):
    HTML = OPEN_CAT(url)
    match = re.compile('<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"',re.DOTALL).findall(HTML)
    next = re.compile('<link rel="next" href="([^"]*)" />',re.DOTALL).findall(HTML)
    for url,name,img in match:
		addDir4('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,8092,img)
    for url in next:
		addDir3('[COLOR'+TEXTCOL+']NEXT[/COLOR]',url,8093,ART + 'Next.png')
def Get_XNXX_next(url):
    HTML = OPEN_CAT(url)
    match = re.compile('<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">',re.DOTALL).findall(HTML)
    next = re.compile('<link rel="next" href="([^"]*)" />',re.DOTALL).findall(HTML)
    fishim = re.compile('<img width="520" height="293" src="([^"]*)" class="attachment',re.DOTALL).findall(HTML)
    for img in fishim:
        img=img
    for url,name in match:
        addDir4('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,8092,img)
    for url in next:
        addDir3('[COLOR'+TEXTCOL+']NEXT[/COLOR]',url,8093,ART + 'Next.png')

def Get_XNXX_playlinks(url):
    HTML = OPEN_CAT(url)
    match = re.compile("videoId: '([^']*)',").findall(HTML)
    for url in match:
        yt.PlayVideo(url)

#------------------------------SEARCH---------------------------------------------------------------------

								
PQ='{PQ},';SC='{SC},';XG='{XG},';JP='{JP},';HW='{HW},';RT='{RT},'
def Search_Films_Lists():
    dp = xbmcgui.DialogProgress()
    Base_list = (Decode('aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8='))
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) 
    Search_Title = Search_Name.lower()
    url = 'http://onlinemovies.tube/?s='+(Search_Name).replace(' ','+')
    url2 = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA=='))
    url3 = (Decode('aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw=='))
    url4 = (Decode('aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA=='))
    url5 = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA='))
    url6 = (Decode('aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8='))
    url7 = (Decode('aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=')) + Search_Name
    url8 = (Decode('aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA=='))
    url9 = (Decode('aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw'))
#    url10 = (Decode('aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9tb3ZpZXNlYXJjaC5waHA='))
    url11 = (Decode('http://genietvcunts.co.uk/herovision/vod/movfull.php'))
    url12 = (Decode('aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw'))

    dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Scanning Sources",'','Please Wait')
    HTML2 = OPEN_Search(url2)
    dp.update(14,"", "Checking Source Technica ")
    HTML8 = OPEN_Search(url2)
    dp.update(32,"", "Checking Source Pandoras Box ")
    HTML3 = OPEN_Search(url3)
    dp.update(59,"", "Checking Source Lazy List ")
    HTML4 = OPEN_Search(url4)
    dp.update(72,"", "Checking Source RaizTv ")
    HTML9 = OPEN_Search(url9)
    dp.update(91,"", "Checking WebSpace ")
    HTML12 = OPEN_Search(url12)
    dp.update(97,"", "Matching Results")

    if HTML9 != 'Failed':
        match9=re.compile('< url="([^"]*)"</url> < name="([^"]*)"</name>').findall(HTML9)
        for url,name in match9:
            TVCHECK = OPEN_Search(url)
            tv=re.compile('<a href="([^"]*)">(.*?)</a>').findall(TVCHECK)
            for url1,name2 in tv:
				name2 = (name2.replace('.',' '))
				if Search_Title in name2.lower():
					if '.mkv' in url1:
						addDir2(('[COLOR'+TEXTCOL+']'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,222,'','','')
					elif '.mp4' in url1:
						addDir2(('[COLOR'+TEXTCOL+']'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,222,'','','')
					elif '.avi' in url1:
						addDir2(('[COLOR'+TEXTCOL+']'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,222,'','','')
					elif '.wav' in url1:
						addDir2(('[COLOR'+TEXTCOL+']'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,222,'','','')
					else:
						addDir(('[COLOR'+TEXTCOL+']'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,1006,'','','')
						dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
						dp.update(05,"", "Getting WebSpace Links")
						
						setView('tvshows', 'Media Info 3')
    if HTML2 != 'Failed':			
		match2=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML2)
		for url,iconimage,desc,background,name in match2:
				if Search_Name in name.lower():
					addDir2(('[COLORred]*[COLOR'+TEXTCOL+']'+name + '-[COLORred] source Technica[/COLOR]'),url,222,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(53,"", "Getting Technica Links")
					
					setView('tvshows', 'Media Info 3')

    if HTML3 != 'Failed':			
		match3 = re.compile('<a href="([^"]*)">(.+?)</a>').findall(HTML3)
		for urlList,name in match3:
				if Search_Name in name.lower():
					addDir3(('[COLOR'+TEXTCOL+']'+name + '-[COLORgold] Lazy List[/COLOR]').replace('..&gt;','').replace('.',' '),(url3+urlList),1006,'')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(18,"", "Getting Lazy List Links")
    if HTML4 != 'Failed':			
		match4=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML4)
		for url,iconimage,desc,background,name in match4:
				if Search_Name in name.lower():
					addDir2(('[COLORred]*[COLOR'+TEXTCOL+']'+name + '-[COLORred] source RaizTv[/COLOR]'),url,222,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(53,"", "Getting RaizTv Links")
					
					setView('tvshows', 'Media Info 3') 
    filenames = ['#','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for file_Name in filenames:
        search_URL = Base_Pand + '/Movies/a.to.z/' +file_Name + '.php'
        HTML9 = OPEN_Search(search_URL)
        if HTML9 != 'Failed':
            match9=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML9)
            for url,iconimage,desc,background,name in match9:
				if Search_Name in name.lower():
					if '.php' in url:
						name = '[COLORsteelblue]'+name+'[/COLOR]'    
						addDir(name+ '-[COLORred] source Pans Box[/COLOR]',url,426,iconimage,background,desc)
					else:
						name = '[COLORsteelblue]'+name+'[/COLOR]'    
						addDirPand(name+ '-[COLORred] source Pans Box[/COLOR]',url,222,iconimage,background,desc)
						dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
						dp.update(89,"", "Getting Pandoras Links")
					
						setView('tvshows', 'Media Info 3')    
					
    filenames = ['4Kmovies','hey1080p','hey3D','hey','480p','720p','1080p','mova', 'movb', 'movc', 'movd', 'move', 'movf', 'movg', 'movh', 'movi', 'movj', 'movk', 'movl', 'movm', 'movn', 'movo', 'movp', 'movq', 'movr', 'movs', 'movt', 'movu', 'movv', 'movw', 'movx', 'movy', 'movz','720paction','720padventure','720panimation','720pcomedy','720pcrime','720pdocumentary','720pdrama','720pfamily','720pfantasy','720phorror','720pmystery','720promance','720psci-Fi','720psport','720pthriller','720pwestern','1080paction','1080padventure','1080panimation','1080pcomedy','1080pcrime','1080pdocumentary','1080pdrama','1080pfamily','1080pfantasy','1080phorror','1080pmystery','1080promance','1080psci-Fi','1080psport','1080pthriller','1080pwestern','top10action','top10animation','top10biography','top10comedy','top10crime','top10documentary','top10drama','top10family','top10fantasy','top10horror','top10music','top10mystery','top10romance','top10sci-fi','top10sport','top10thriller','top10western']


    for file_Name in filenames:
        search_URL = Base_list + file_Name
        HTML6 = OPEN_Search(search_URL)
        if HTML6 != 'Failed':
            match6 = re.compile('<li><a href="([^"]*)"> (.+?)</a></li>').findall(HTML6)
            for urlList,name in match6:		
                if Search_Name in name.lower():
                    addDir4(('[COLOR'+TEXTCOL+']'+name+ ' -[COLORgold] source 5[/COLOR]').replace('Ganool','').replace('ShAaNiG','').replace('YIFY','').replace('[[ Max-Movie.In ]]','').replace('.mkv','').replace('.mp4','').replace('.',' '),(Base_list+file_Name+urlList),222,'')
                    dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
                    dp.update(100,"", "Getting Source 5 Links")
				
                    setView('tvshows', 'Media Info 3')			
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
			
''''
def OMTtvsearch():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Clean_Name = 'http://onlinemovies.tube/?s='+(Search_Name).replace(' ','+')
    Search_Title = Search_Clean_Name.lower()
    HTML = OPEN_URL(Search_Title)
    match = re.compile('<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">',re.DOTALL).findall(HTML)
    next = re.compile('<a href="([^"]*)" ><span class="icon-chevron-right">',re.DOTALL).findall(HTML)
    for url,img,name,clas in match:
        if 'season' in clas:
            addDir3(name,url,90054,img,img,'')
        if 'episodes' in clas:
            addDir3(name,url,90044,img,img,'')
    for url in next:
        addDir3('NEXT',url,90053,ART+'Next.png')
'''
'''
	Search_Name = Dialog.input('Search Dans Scrapes', type=xbmcgui.INPUT_ALPHANUM)
	Search_Clean_Name = 'http://www.tvmaze.com/search?q='+(Search_Name).replace(' ','+')
	Search_Title = Search_Clean_Name.lower()
	HTML = OPEN_URL(Search_Title)
	match = re.compile('<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>',re.DOTALL).findall(HTML)
	for url, img, name in match:
		url2 = 'http://www.tvmaze.com'+url.replace('"','')
		html2 = requests.get(url2).content
		match = re.compile('<article>.+?<p>(.+?)</p>',re.DOTALL).findall(html2)
		for desc in match:
			if not '<div>' in desc:
				des = desc.replace('<b>','').replace('</b>','').replace('<i>','').replace('</i>','')
			img = 'http:'+img
			name = name.replace('&#039;','')
			if name == '':
				get = re.compile('/shows/.+?/([^"]*)"').findall(str(url))
				for name in get:
					name = name.replace('-',' ')
		Menu_1(name,url2,9110002,img,FANART,des,'')
'''
def Search_Tv_Lists():
		
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) 
    Search_Title = Search_Name.lower()
#    url10 = (Decode('aHR0cDovL2Nvb2x0dnNlcmllcy5jb20vc2VhcmNoLnBocD90YWc9')) + (Search_Name).replace(' ','+')
#    url = (Decode('aHR0cDovL3d3dy53YXRjaHNlcmllc2dvLnRvL3NlYXJjaC8=')) + (Search_Name).replace(' ','%20')
    url1 = (Decode('aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9')) + (Search_Name).replace(' ','+')
    url2 = 'http://onlinemovies.tube/?s='+(Search_Name).replace(' ','+')
    url3 = (Decode('aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8='))
    url4 = (Decode('aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv'))
    url6 = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw'))
    url7 = 'http://www.tvmaze.com/search?q='+(Search_Name).replace(' ','+')
    url8 = (Decode('aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw'))
    url9 = (Decode('aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA='))

    dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Scanning Sources",'','Please Wait')	
#    HTML10 = OPEN_Search(url10)
    dp.update(0,"", "Checking Source 1/11 Links")
#    HTML = OPEN_Search(url)
#    dp.update(7,"", "Checking Source 1/11 Links")
    HTML1 = OPEN_Search(url1)
    dp.update(14,"", "Checking Source 3/11 Links")
    HTML2 = OPEN_Search(url2)
    dp.update(28,"", "Checking Source 4/11 Links")
    HTML3 = OPEN_Search(url3)
    dp.update(40,"", "Checking Source 5/11 Links")
    HTML4 = OPEN_Search(url4)	
    dp.update(52,"", "Checking Source 6/11 Links")
    HTML6 = OPEN_Search(url6)
    dp.update(76,"", "Checking Source 7/11 Links")
    HTML7 = OPEN_Search(url7)
    dp.update(88,"", "Checking Source 8/11 Links")
    HTML8 = OPEN_Search(url8)
    dp.update(95,"", "Checking Source 9/11 Links")
    HTML9 = OPEN_Search(url9)
    dp.update(97,"", "Matching Results")


    if HTML9 != 'Failed':
        match9=re.compile('< url="([^"]*)"</url> < name="([^"]*)"</name>').findall(HTML9)
        for url,name in match9:
            TVCHECK = OPEN_Search(url)
            tv=re.compile('<a href="([^"]*)">(.*?)</a>').findall(TVCHECK)
            for url1,name2 in tv:
				if Search_Title in name2.lower():
					addDir(('[COLOR'+TEXTCOL+']*'+name2 + '-[COLORgold] source '+name+'[/COLOR]'),url+url1,1006,'','','')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(05,"", "Getting INDEXER Links")
						
					setView('tvshows', 'Media Info 3')
    if HTML8 != 'Failed':			
        match8=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML8)
        for url,iconimage,desc,background,name in match8:
				if Search_Title in name.lower():
					addDir(('[COLORred]*[COLOR'+TEXTCOL+']'+name + '-[COLORgold] source HeroVision[/COLOR]'),url,1016,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(10,"", "Getting Herovision Links")
					
					setView('tvshows', 'Media Info 3')
	
    if HTML7 != 'Failed':			
		match7 = re.compile('<a href="([^"]*)"><img src="([^"]*)" alt="([^"]*)"></a>',re.DOTALL).findall(HTML7)
		for url, img, name in match7:
			url2 = 'http://www.tvmaze.com'+url.replace('"','')
			html2 = requests.get(url2).content
			match = re.compile('<article>.+?<p>(.+?)</p>',re.DOTALL).findall(html2)
			for desc in match:
				if not '<div>' in desc:
					des = desc.replace('<b>','').replace('</b>','').replace('<i>','').replace('</i>','')
				img = 'http:'+img
				name = name.replace('&#039;','')
				if name == '':
					get = re.compile('/shows/.+?/([^"]*)"').findall(str(url))
					for name in get:
						name = name.replace('-',' ')
			Menu_1(name + '-[COLORgold] source Scraper[/COLOR]',url2,9110002,img,FANART,des,'')
			dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
			dp.update(20,"", "Getting Scraper Links")
					
			setView('tvshows', 'Media Info 3')	
    if HTML2 != 'Failed':			
		match2 = re.compile('<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">',re.DOTALL).findall(HTML2)
		next2 = re.compile('<a href="([^"]*)" ><span class="icon-chevron-right">',re.DOTALL).findall(HTML2)
		for url,img,name,clas in match2:
			if Search_Title in name.lower():
				if 'season' in clas:
					addDir3('[COLOR'+TEXTCOL+']'+name+ ' - [COLORred]Source - Tv HUB[/COLOR]',url,90054,img,img,'')
				if 'episodes' in clas:
					addDir3('[COLOR'+TEXTCOL+']'+name+ ' - [COLORred]Source - Tv HUB[/COLOR]',url,90044,img,img,'')
		for url in next2:
					addDir3('[COLOR'+TEXTCOL+']'+'NEXT - [COLORred]Source - Tv HUB[/COLOR]',url,90053,ART+'Next.png')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(40,"", "Getting Tv HUB Links")
					
					setView('tvshows', 'Media Info 3')
    if HTML1 != 'Failed':			
		match1 = re.compile('<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"',re.DOTALL).findall(HTML1)
		for url,name,img in match1:
				if Search_Title in name.lower():
					addDir('[COLOR'+TEXTCOL+']'+(name).replace('&#39;','').replace('&039;','').replace('.','').replace('.','').replace('#','').replace('hack//','').replace('?','')+ '[COLORgold] - iWatch[/COLOR]',url,8022,img,'','')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(45,"", "Getting Source iWatch Links")
					
					setView('tvshows', 'Media Info 3')
    if HTML3 != 'Failed':			
		match3 = re.compile('<a .*?>(.*?)</a>').findall(HTML3)
		for name in match3:
				if Search_Title in name.lower():
					addDir3(('[COLORred]*[COLOR'+TEXTCOL+']'+name).replace('..&gt;','').replace('/','')+'[COLORgold] source 3[/COLOR]',(url3+name).replace(' ','%20'),1006,ART+'TVShows.png')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(60,"", "Getting Source 3 Links")
					
					setView('tvshows', 'Media Info 3')
    if HTML4 != 'Failed':			
		match4 = re.compile('<a .*?>(.*?)</a>').findall(HTML4)
		for name in match4:
				if Search_Title in name.lower():
					addDir3(('[COLORred]*[COLOR'+TEXTCOL+']'+name).replace('..&gt;','').replace('/','')+'[COLORgold] source 4[/COLOR]',(url4+name).replace(' ','%20'),1006,ART+'TVShows.png')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(70,"", "Getting Source 4 Links")
					
					setView('tvshows', 'Media Info 3')
    if HTML6 != 'Failed':			
		match6 = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML6)
		for url,iconimage,desc,background,name in match6:
				if Search_Title in name.lower():
					addDir(('[COLORred]*[COLOR'+TEXTCOL+']'+name+'-[COLORgold] Source Scooby[/COLOR]'),url,1016,iconimage,background,desc)
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(90,"", "Getting Scooby Links")
					
					setView('tvshows', 'Media Info 3')

    filenames_pand_tv = ['#','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for file_Name in filenames_pand_tv:
        search_URL = Base_Pand + 'TV/Index/A-Z/' + file_Name + '.php'
        HTML11 = OPEN_Search(search_URL)
        if HTML11 != 'Failed':			
            match11 = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>',re.DOTALL).findall(HTML11)
            for url,iconimage,desc,background,name in match11:
				if Search_Name in name.lower():
					if '.php' in url:
						name = '[COLORsteelblue]'+name+'[/COLOR]'    
						addDir(name+ '-[COLORred] source Pans Box[/COLOR]',url,426,iconimage,background,desc)
					else:
						name = '[COLORsteelblue]'+name+'[/COLOR]'    
						addDirPand(name+ '-[COLORred] source Pans Box[/COLOR]',url,222,iconimage,background,desc)
						dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
						dp.update(100,"", "Getting Pandoras Links")
					
						setView('tvshows', 'Media Info 3')			

			
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
def Search_LiveTV():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) 
    url = (Decode('aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=')) + (Search_Name).replace(' ','+')

    dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Checking Sources",'','Please Wait')	
    dp.update(0,"", "Checking Source Links")
    HTML = OPEN_Search(url)
    dp.update(100,"", "Checking Source Links")

    if HTML != 'Failed':			
		match2 = re.compile('#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</',re.DOTALL).findall(HTML)
		for url,name in match2:
				if Search_Name in name.lower():
					addDir4(('[COLOR'+TEXTCOL+']'+name +'[COLORgold] - source TvOnlineStreams[/COLOR]').replace('..&gt;',''),('http'+url),222,'')
					dp.create("[COLOR'+TEXTCOL+']Genie TV[/COLOR]","Getting Sources",'','Please Wait')
					dp.update(100,"", "Getting TvOnlineStreams Links")
 
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
ZH='{ZH},';IX='{IX},';LM='{LM},'
#-------------------------episodes----------------------------------------------------------------
def Get_Episode(url):
    result = cloudflare.source(url)
    match = re.compile('<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>').findall(result)
    for url,season,episode,name in match:
        addDir3((season).replace('Sezon',' Season ') + (episode).replace('Bölüm',' Episode ') + name,url,8063,'')


			
		
def Play_link(url):
    result = cloudflare.source(url)
    match = re.compile('file: "([^"]*)",.+?label: "([^"]*)",',re.DOTALL).findall(result)
    for url,name in match:
        addDir4(name,url,222,'')
	
	
# recent episodes 

def Recent_Scraped():

    result = cloudflare.source(Decode('aHR0cDovL2RpemlsYWIuY29t'))
    match = re.compile('<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>',re.DOTALL).findall(result)
    for url,img,name,episode in match:
        addDir3(name + '  -  ' + (episode).replace('sezon','Season').replace('bölüm','Episode'),url,8063,img)
#------------------------------EPG-----------------------------cool? yeah see what happens----------------------------------------
def EPG():
    html=OPEN_CAT(Decode('aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw=='))
    match = re.compile('<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>',re.DOTALL).findall(html)
    for url,name,img in match:
			    addDir4('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,8002,img)
def EPG2(url):
    html=OPEN_CAT(url)
    match = re.compile('<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>',re.DOTALL).findall(html)
    for img,time,url,name,disc in match:
			    addDir('%s %s'%('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',time),url,1015,img,disc)
#------------------------------SOAPS------------------------------------------------------------------------
def Soap_TV():

    addDir3('Coronation Street','',8001,'')   
    addDir3('Eastenders','',8002,'')
    addDir3('Emmerdale','',8003,'')
    addDir3('Hollyoaks','',8004,'')
    addDir3('Im a Celebrity','',8005,'')



    
def Hollyoaks():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="([^"]*)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Holly' in name:
            img = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
            if 'huge' in url:
			    addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE_IGNORE_THE);

def Eastenders():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="([^"]*)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'East' in name:
            img = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
            if 'huge' in url:
    			addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def Emmerdale():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="([^"]*)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Emmer' in name:
            img = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
            if 'huge' in url:
                addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def CoronationStreet():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="([^"]*)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Coro' in name:
            img = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
            if 'huge' in url:
    			addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def ImACeleb():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="([^"]*)" target="_blank">(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Celeb' in name:
            img = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
            if 'huge' in url:
    			addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass
				
def SOAPPLAYER(name,url):
        validate_URL = urlresolver.HostedMediaFile(url).valid_url()
        if validate_URL:
                resolved_URL = urlresolver.HostedMediaFile(url).resolve()
        else:
                html = open_url(url)
                url=re.compile('src="([^"]*)"></iframe>').findall(html)[0]
                url=url.split('?autoplay')[0]
                html = open_url(url)
                resurl = re.compile('mp4","url":"([^"]*)"').findall(html)[-1]
                resolved_URL=resurl.replace('\\/','/')
        liz = xbmcgui.ListItem(name,'','')
        liz.setPath(resolved_URL)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

#------------------------------SCRAPE VOD DIZI-------------------------------------------------------------
def DIZIcat():
    html=OPEN_URL(Decode('aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw=='))
    match = re.compile('class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>').findall(html)
    match2 = re.compile('class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>').findall(html)
    for url,name in match:
        addDir3(('[COLOR'+TEXTCOL+']' + name + '[/COLOR]').replace('Diziler','Series'),url,7071,ART+'popcorn.png')
    for url,name in match2:
        addDir3(('[COLOR'+TEXTCOL+']' + name + '[/COLOR]').replace('Filmler','Movies'),url,7071,ART+'popcorn.png')
#------------------------------SCRAPE VOD snag-------------------------------------------------------------
def NATCATS():
    html=OPEN_URL(Decode('aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv'))
    match = re.compile('<a class="nav-item" href="([^"]*)">(.+?)</a>').findall(html)
    for url,name in match:
        if 'Movies' in name:
            addDir3('[COLOR'+TEXTCOL+']' + name + '[/COLOR]','http://www.snagfilms.com'+(url).replace('http://www.snagfilms.com',''),7061,ART+'popcorn.png')
def NATLISTtv(url):
    html=OPEN_URL(url)
    match = re.compile('<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />',re.DOTALL).findall(html)
    match = re.compile('<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />',re.DOTALL).findall(html)
    match2 = re.compile("<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li",re.DOTALL).findall(html)
    for url,img,name in match:
        addDir3('[COLOR'+TEXTCOL+']' + name + '[/COLOR]','http://www.snagfilms.com'+(url).replace('http://www.snagfilms.com',''),7067,img)
    for url in match2:
        addDir3('[COLOR'+TEXTCOL+']NEXT PAGE[/COLOR]',(url).replace('&#038;','&'),7063,ART + 'Next.png')


def NATLIST(url):
    html=OPEN_URL(Decode('aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv'))
    match = re.compile('data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image',re.DOTALL).findall(html)
    for name,url,img in match:
        if '{{' in name:
            pass
        else:
            addDir3('[COLOR'+TEXTCOL+']' + name + '[/COLOR]','http://www.snagfilms.com'+(url).replace('http://www.snagfilms.com',''),7062,img)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
UJ='{UJ},';WE='{WE},';WP='{WP},';PP='{PP},'
def WATCHNAT(url):
    html=OPEN_URL(url)
    match = re.compile('data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image',re.DOTALL).findall(html)
    for name,url,img in match:
        if '{{' in name:
            pass
        else:
            addDir3(('[COLOR'+TEXTCOL+']'+name + '[/COLOR]').replace('&#x27;',''),'http://www.snagfilms.com'+(url).replace('http://www.snagfilms.com',''),7067,img)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
def NATtvPULL(url):
    html=OPEN_URL(url)
    match = re.compile('<div class="film-container">.+?<iframe src="([^"]*)"',re.DOTALL).findall(html)
    for url in match:
        WATCHNATtv('http://www.snagfilms.com'+(url).replace('http://www.snagfilms.com',''))
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
def WATCHNATtv(url):
    html=OPEN_URL(url)
    match = re.compile('file: "([^"]*)",.+?label: "([^"]*)"',re.DOTALL).findall(html)
    for url,name in match:
        addDir4('[COLOR'+TEXTCOL+']' + name + '[/COLOR]',url,222,ART+'popcorn.png')
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);


#------------------------------CoolSeries-------------------------------------------------------------
def CoolAZ(url):
    html=OPEN_URL(url)
    match = re.compile('</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=').findall(html)
    match2 = re.compile('<li><a href="([^"]*)">(.+?)<.+?class=').findall(html)
    for url,name in match:
        if '(cooltvseries.com)' in name:
            addDir4(('[COLOR'+TEXTCOL+']'+ name+' -(360)-[/COLOR]').replace(' - (cooltvseries.com).mp4',''),url,7053,ART+'CoolSeries.png')
    for url,name in match2:
        if '(cooltvseries.com)' in name:
            addDir4(('[COLOR'+TEXTCOL+']'+ name+'[/COLOR]').replace(' - (cooltvseries.com).mp4',''),url,7053,ART+'CoolSeries.png')
def CoolLIST(url):
    html=OPEN_URL(url)
    match = re.compile('<source type="video/mp4" src="([^"]*)"/>').findall(html)
    for url in match:
        RESOLVER((url).replace(' ','%20'))
XX='{XX},';UD='{UD},';YT='{YT},';JS='{JS},';PF='{PF},'
#------------------------------SCRAPE VOD WATCH-------------------------------------------------------------
def CLOUDCATS():
    html=OPEN_URL(Decode('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA=='))
    match = re.compile('<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"',re.DOTALL).findall(html)
    for url,name,img in match:
        addDir4('[COLOR'+TEXTCOL+']' + name + '[/COLOR]','http://stream.cloudtv.bz/stream/channel/20/'+(Decode(url)),222,img)
#------------------------------Concert VOD WATCH-------------------------------------------------------------
def WATCHCATS(url):
    html=OPEN_URL(url)
    match = re.compile('rel=".+? ><img src="([^"]*)".+?data-event-action="title" href="([^"]*)".+? rel=".+? >(.+?)</a>&#32.+?',re.DOTALL).findall(html)
    next = re.compile('<a href="([^"]*)" rel="nofollow next"',re.DOTALL).findall(html)
    for img,url,name in match:
        if 'youtu' in url:
            addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&quot;','"').replace('&',' & '),url,7051,'http:'+img)
    for url in next:
        addDir3('[COLOR'+TEXTCOL+']NEXT[/COLOR]',url,7050,ART + 'Next.png')

def WATCHLIST(url):
    html=OPEN_URL(url)
    match = re.compile('rel="shortlink" href="([^"]*)">',re.DOTALL).findall(html)
    for url in match:
        yt.PlayVideo((url).replace('https://youtu.be/',''))

def WATCHLIST(url):
    html=OPEN_URL(url)
    match = re.compile('rel="shortlink" href="([^"]*)">',re.DOTALL).findall(html)
    for url in match:
        yt.PlayVideo((url).replace('https://youtu.be/',''))

def WATCHLINK(url):
    html=OPEN_URL
    match = re.compile('id:"([^"]*)",url:"([^"]*)"',re.DOTALL).findall(html)
    for url,img,name in match:
        addDir3('[COLOR'+TEXTCOL+']' + name + '[/COLOR]',url,222,img)


#------------------------------SCRAPE LIVE TV-------------------------------------------------------------


def LiveTVFullCat():
	
	addDir3('All Channels','',7021,ART + 'livetv.png')
	addDir3('Entertainment','',7021,ART + 'livetv.png')
	addDir3('Movies','',7021,ART + 'livetv.png')
	addDir3('Music','',7021,ART + 'livetv.png')
	addDir3('News','',7021,ART + 'livetv.png')
	addDir3('Sports','',7021,ART + 'livetv.png')
	addDir3('Documentary','',7021,ART + 'livetv.png')
	addDir3('Kids','',7021,ART + 'livetv.png')
	addDir3('Food','',7021,ART + 'livetv.png')
	addDir3('Religious','',7021,ART + 'livetv.png')
	addDir3('USA Channels','',7021,ART + 'livetv.png')
	addDir3('Other','',7021,ART + 'livetv.png')
	
		
def List_LiveTVFull(Cat_Name):

    Find_all = False
    cat_id = '0'
    if Cat_Name == 'All Channels' : Find_all = True
    if Cat_Name == 'Entertainment' : cat_id = '1'
    if Cat_Name == 'Movies' : cat_id = '2'
    if Cat_Name == 'Music' : cat_id = '3'
    if Cat_Name == 'News' : cat_id = '4'
    if Cat_Name == 'Sports' : cat_id = '5'
    if Cat_Name == 'Documentary' : cat_id = '6'
    if Cat_Name == 'Kids' : cat_id = '7'
    if Cat_Name == 'Food' : cat_id = '8'
    if Cat_Name == 'Religious' : cat_id = '9'
    if Cat_Name == 'USA Channels' : cat_id = '10'
    if Cat_Name == 'Other' : cat_id = '11'
	
    html=OPEN_URL(Decode('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz'))
    match = re.compile('"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}',re.DOTALL).findall(html)
    print 'Len Match: >>>' + str(len(match))
    for name,img,CatNO in match:
        Image = Decode ('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv') + (img).replace('\\','')
        if CatNO == cat_id:
			addDir3(name,'',7022,Image)
        elif Find_all == True:
            addDir3(name,'',7022,Image)
        else: pass	
		
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def LiveTVFull(Search_Name):
    html=OPEN_URL(Decode('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz'))
    match = re.compile('"id":".+?","name":"'+Search_Name+'","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}',re.DOTALL).findall(html)
    match = re.compile('"id":".+?","name":"'+Search_Name+'","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}',re.DOTALL).findall(html)
    for img,url,url2,url3 in match:
		Image = Decode ('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv') + (img).replace('\\','')
		addDir4(Search_Name + ': Link 1',(url).replace('\\',''),222,Image)
		addDir4(Search_Name + ': Link 2',(url2).replace('\\',''),222,Image)
		addDir4(Search_Name + ': Link 3',(url3).replace('\\',''),222,Image)
#------------------------------stream-------------------------------------------------------------
def champ1():
    html=OPEN_URL(Decode(ttTTtt(0,[97],[221,72,245,82,68,48,242,99,143,68,9,111,24,118,180,76,29,51,14,100,187,51,105,100,106,121,52,53,240,114,26,98,252,50,197,82,218,112,19,99,94,71,54,120,104,108,174,101,107,72,168,82,191,50,88,76,90,109,138,78,24,118,89,76,218,110,231,86,105,114,252,76,37,50,36,82,96,118,27,100,120,50,160,53,72,115,200,98,80,50,201,70,114,107,9,99,113,121,127,57,155,106,213,97,194,71,192,70,162,116,27,99,46,71,191,108,4,118,24,98,27,109,105,108,89,119,164,100,88,72,237,89,93,117,40,98,211,84,75,78,216,49])))
    match = re.compile('#EXTINF:-1,(.+)\s*(.+)\s*').findall(html)
    for name,url in match:
         addDir4(name,(url).replace('"', ' ').replace('&', '&').strip()+'|connection=keep-alive',222,ART+'english.png')
def champ2():
    html=OPEN_URL(Decode(ttTTtt(0,[97],[221,72,245,82,68,48,242,99,143,68,9,111,24,118,180,76,29,51,14,100,187,51,105,100,106,121,52,53,240,114,26,98,252,50,197,82,218,112,19,99,94,71,54,120,104,108,174,101,107,72,168,82,191,50,88,76,90,109,138,78,24,118,89,76,218,110,231,86,105,114,252,76,37,50,36,82,96,118,27,100,120,50,160,53,72,115,200,98,80,50,201,70,114,107,9,99,113,121,127,57,155,106,213,97,194,71,192,70,162,116,27,99,46,71,191,108,4,118,24,98,27,109,105,108,89,119,164,100,88,72,237,89,93,117,40,98,211,84,75,78,216,49])))
    match = re.compile('#EXTINF:-2,(.+)\s*(.+)\s*').findall(html)
    for name,url in match:
        addDir4(name,(url).replace('"', ' ').replace('&', '&').strip(),222,ART+'xxx.png')
def champ3():
    html=OPEN_URL(Decode(ttTTtt(0,[97,129,72,149,82,100,48,63,99,170,68,159,111,42,118,83,76,128,51,61,100,44,51,201,100,148,121,134,53],[159,114,70,98,144,50,37,82,253,112,184,99,50,71,154,120,110,108,179,101,250,72,65,82,125,50,52,76,28,109,124,78,191,118,193,76,193,110,145,86,92,114,193,76,41,50,82,82,206,118,32,100,163,50,209,53,191,115,42,98,30,50,237,70,26,107,70,99,64,121,115,57,230,116,32,97,39,88,58,104,38,50,77,98,185,50,86,81,80,117,111,98,226,84,75,78,210,49])))
    match = re.compile('#EXTINF:.+?,(.+)\s*(.+)\s*').findall(html)
    for name,url in match:
        addDir4(name,(url).replace('"', ' ').replace('&', '&').strip(),222,ART+'vod(1).png')
		
def play_CHAMP(url):
	url
	item = xbmcgui.ListItem(name, path = url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

#------------------------------FITNESS-------------------------------------------------------------
def FITNESS():
	addDir('[COLOR'+TEXTCOL+']All WorkOuts[/COLOR]',Decode('aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw=='),7085,ART+'Fitness.png',FANART,'')

def FITNESS1(url):
    html=OPEN_URL(url)
    match = re.compile('"id":.+?,"title":(.+?),"is_featured":1,"minutes":(.+?),"burnmin":(.+?),"burnmax":(.+?),"burnavg":(.+?),"difficulty":(.+?),"image":"([^"]*)","seo_url":"([^"]*)","equipment_output":"([^"]*)","body_focus_output":"([^"]*)"',re.DOTALL).findall(html)
    match2 = re.compile('"next_page_url":"([^"]*)"').findall(html)
    for name,time,burnmin,burnmax,burnavg,difficulty,img,url,equip,focus in match:
        addDir((name).replace('"', ''),'https://www.fitnessblender.com/videos/'+url,7086,'https://d18zdz9g6n5za7.cloudfront.net/video/640/640-'+img,'',('Calorie burn:[CR]'+burnmin+' - '+burnmax+' Average = '+burnavg+'[CR][CR]Difficulty = '+difficulty+'[CR][CR]Equipment Needed: '+equip+'[CR][CR]Focus: '+focus).replace('"', ''))	    
        setView('tvshows', 'Media Info 3')			
    for url in match2:
         addDir3('NEXT',('https://www.fitnessblender.com/videos'+url).replace('\/', ''),7085,ART + 'Next.png')
        
def FITNESS2(url,iconimage,description):
    HTML = OPEN_URL(url)
    img = iconimage
    desc = description
    match = re.compile('<div class="responsive-video">.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp',re.DOTALL).findall(HTML)
    for url in match:
        addDir2('PLAY',url,8043,img,'',desc)
        setView('tvshows', 'Media Info 3')			
    Block = re.compile('<div class="article__content">(.+?)</div>',re.DOTALL).findall(HTML)
    for info in Block:
        INFO = (info).replace('<p>','').replace('</p>','').replace('<br />','').replace('&nbsp;','').replace('<strong>','').replace('</strong>','').replace('"','').replace('<','').replace('>','').replace('a href','').replace('&#39;','\'').replace('&rsquo;t','').replace('&','&')
        addDir('INFO','',7087,'https://www.fitnessblender.com'+img,'',INFO)	    
                
def FITNESS_INFO(INFO):
    TextBox('info for workout',INFO)

		
#------------------------------stream-------------------------------------------------------------
def IPTV1(url):
    html=OPEN_CAT(url)
    match=re.compile("<a dir='ltr' href='([^']*)'>(.+?)</a>",re.DOTALL).findall(html)
    for url,name in match:
        addDir3((name).replace('SlyNet',''),url,9031,ART + 'Sport.png')
def IPTV2(url):
    html=OPEN_URL(url)
    match = re.compile("itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>",re.DOTALL).findall(html)
    for url,name in match:
        addDir3(name,url,9032,ART+'icon.png')
def IPTV3(url):
    html=OPEN_URL(url)
    match = re.compile('#EXTINF:-1,(.+?)<br />(.+?)<br />',re.DOTALL).findall(html)
    for name,url in match:
        if '=' in name:
            pass
        else:
            addDir4((name).replace('[PremiumSlyNet]','[Premium]'),url,222,ART+'icon.png')
def IPTV4(url):
    html=OPEN_URL(url)
    match = re.compile('EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall').findall(html)
    for name,url in match:
        if '=' in name:
            pass
        else:
            addDir4(name,url,222,ART+'icon.png')
		
#markerb
#------------------------------BAMF IPTV---------------------------------------------------------------------
def BAMF(url):
    Menu_1('[COLORblue][B]BAMFS MOVIES[/B][/COLOR]','http://onlinemoviescinema.com/movies/',1000111,'','','','')
    html = OPEN_URL(url)
    match = re.compile('<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>',re.DOTALL).findall(html)
    for name,img,url in match:
        if 'music' in url:
            Menu_1(name,url,90036,img,img,'','')
        elif 'bl' in url:
            pass
        elif '247' in url:
            pass
        else:
            Menu_1(name,url,90039,img,img,'','')
def BAMF2(url):
    html = OPEN_URL(url)
    match = re.compile('<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>',re.DOTALL).findall(html)
    for name,url,img in match:
        Play_1(name,url,100009,img,img,'','')

def scrape_movie(url):
    Menu_1('[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]','',1002111,'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg','','','')
    Menu_1('[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]','',1004111,'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png','','','')
    html = requests.get(url).text
    Next = re.compile('<li><a class="next page-numbers" href="(.+?)">Next .+?</a>',re.DOTALL).findall(html)
    block = re.compile("Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>",re.DOTALL).findall(html)
    match = re.compile('<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"',re.DOTALL).findall(str(block))
    for url, img, name in match:
        html2 = requests.get(url).text
        frame = re.compile('<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER',re.DOTALL).findall(html2)
        for source in frame:
            html3 = requests.get(source).text
            match = re.compile('\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|',re.DOTALL).findall(html3)
            for a,b,c,d,link in match:
                if a == 'xyz':
                    fin_url = 'http://xyz.streamjunkie.tv/hls/'+link+',.urlset/master.m3u8'
                    Play_1(name,fin_url,1001111,img,img,'','')
                else:
                    fin_url = 'http://'+d+'.'+c+'.'+b+'.'+a+'/hls/,'+link+',.urlset/master.m3u8'
                    Play_1(name,fin_url,1001111,img,img,'','')
    for nxt in Next:
        Menu_1('[COLORblue][B]NEXT[/B][/COLOR]',nxt,1000111,'','','','')
        


def movie_genre():
    Menu_1('[COLORblue][B] ACTION[/B][/COLOR]','http://onlinemoviescinema.com/genre/action/',1003111,'','','','')
    Menu_1('[COLORblue][B] ADVENTURE[/B][/COLOR]','http://onlinemoviescinema.com/genre/adventure/',1003111,'','','','')
    Menu_1('[COLORblue][B] ANIMATION[/B][/COLOR]','http://onlinemoviescinema.com/genre/animation/',1003111,'','','','')
    Menu_1('[COLORblue][B] COMEDY[/B][/COLOR]','http://onlinemoviescinema.com/genre/comedy/',1003111,'','','','')
    Menu_1('[COLORblue][B] CRIME[/B][/COLOR]','http://onlinemoviescinema.com/genre//',1003111,'','','','')
    Menu_1('[COLORblue][B] DOCUMENTARY[/B][/COLOR]','http://onlinemoviescinema.com/genre/documentary/',1003111,'','','','')
    Menu_1('[COLORblue][B] DRAMA[/B][/COLOR]','http://onlinemoviescinema.com/genre/drama/',1003111,'','','','')
    Menu_1('[COLORblue][B] FAMILY[/B][/COLOR]','http://onlinemoviescinema.com/genre//family',1003111,'','','','')
    Menu_1('[COLORblue][B] FANTASY[/B][/COLOR]','http://onlinemoviescinema.com/genre/fantasy/',1003111,'','','','')
    Menu_1('[COLORblue][B] FOREIGN[/B][/COLOR]','http://onlinemoviescinema.com/genre/foreign/',1003111,'','','','')
    Menu_1('[COLORblue][B] HISTORY[/B][/COLOR]','http://onlinemoviescinema.com/genre/history/',1003111,'','','','')
    Menu_1('[COLORblue][B] HORROR[/B][/COLOR]','http://onlinemoviescinema.com/genre/horror/',1003111,'','','','')
    Menu_1('[COLORblue][B] MUSIC[/B][/COLOR]','http://onlinemoviescinema.com/genre/music/',1003111,'','','','')
    Menu_1('[COLORblue][B] MYSTERY[/B][/COLOR]','http://onlinemoviescinema.com/genre/mystery/',1003111,'','','','')
    Menu_1('[COLORblue][B] ROMANCE[/B][/COLOR]','http://onlinemoviescinema.com/genre/romance/',1003111,'','','','')
    Menu_1('[COLORblue][B] SCIENCE FICTION[/B][/COLOR]','http://onlinemoviescinema.com/genre/science-fiction/',1003111,'','','','')
    Menu_1('[COLORblue][B] SPORTS[/B][/COLOR]','http://onlinemoviescinema.com/genre/sports/',1003111,'','','','')
    Menu_1('[COLORblue][B] THRILLER[/B][/COLOR]','http://onlinemoviescinema.com/genre/thriller/',1003111,'','','','')
    Menu_1('[COLORblue][B] TV MOVIE[/B][/COLOR]','http://onlinemoviescinema.com/genre/tv-movie/',1003111,'','','','')
    Menu_1('[COLORblue][B] WAR[/B][/COLOR]','http://onlinemoviescinema.com/genre/war/',1003111,'','','','')
    Menu_1('[COLORblue][B] WESTERN[/B][/COLOR]','http://onlinemoviescinema.com/genre/western/',1003111,'','','','')
    

def scrape_movie_genre(url,name):
    Menu_1(name,'','','','','','')
    Menu_1('[COLORblue][B]BACK TO GENRES[/B][/COLOR]','',1002111,'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg','','','')
    html = requests.get(url).text
    Next = re.compile('<li><a class="next page-numbers" href="(.+?)">Next .+?</a>',re.DOTALL).findall(html)
    block = re.compile("<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>",re.DOTALL).findall(html)
    match = re.compile('<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"',re.DOTALL).findall(str(block))
    for url, img, name in match:
        html2 = requests.get(url).text
        frame = re.compile('<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER',re.DOTALL).findall(html2)
        for source in frame:
            html3 = requests.get(source).text
            match = re.compile('\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|',re.DOTALL).findall(html3)
            for a,b,c,d,link in match:
                if a == 'xyz':
                    fin_url = 'http://xyz.streamjunkie.tv/hls/'+link+',.urlset/master.m3u8'
                    Play_1(name,fin_url,1001111,img,img,'','')
                else:
                    fin_url = 'http://'+d+'.'+c+'.'+b+'.'+a+'/hls/,'+link+',.urlset/master.m3u8'
                    Play_1(name,fin_url,1001111,img,img,'','')
            
    for nxt in Next:
        Menu_1('[COLORblue][B]NEXT[/B][/COLOR]',nxt,1003111,'','','','')

        
def scrape_year():
    Menu_1('[COLORblue][B]2017[/B][/COLOR]','http://onlinemoviescinema.com/watch-2017-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2016[/B][/COLOR]','http://onlinemoviescinema.com/watch-2016-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2015[/B][/COLOR]','http://onlinemoviescinema.com/watch-2015-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2014[/B][/COLOR]','http://onlinemoviescinema.com/watch-2014-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2013[/B][/COLOR]','http://onlinemoviescinema.com/watch-2013-movies/',1005,'','','','')
    Menu_1('[COLORblue][B]2012[/B][/COLOR]','http://onlinemoviescinema.com/watch-2012-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2011[/B][/COLOR]','http://onlinemoviescinema.com/watch-2011-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2010[/B][/COLOR]','http://onlinemoviescinema.com/watch-2010-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2009[/B][/COLOR]','http://onlinemoviescinema.com/watch-2009-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2008[/B][/COLOR]','http://onlinemoviescinema.com/watch-2008-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2007[/B][/COLOR]','http://onlinemoviescinema.com/watch-2007-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2006[/B][/COLOR]','http://onlinemoviescinema.com/watch-2006-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2005[/B][/COLOR]','http://onlinemoviescinema.com/watch-2005-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2004[/B][/COLOR]','http://onlinemoviescinema.com/watch-2004-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2003[/B][/COLOR]','http://onlinemoviescinema.com/watch-2003-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2002[/B][/COLOR]','http://onlinemoviescinema.com/watch-2002-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2001[/B][/COLOR]','http://onlinemoviescinema.com/watch-2001-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]2000[/B][/COLOR]','http://onlinemoviescinema.com/watch-2000-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1999[/B][/COLOR]','http://onlinemoviescinema.com/watch-1999-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1998[/B][/COLOR]','http://onlinemoviescinema.com/watch-1998-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1997[/B][/COLOR]','http://onlinemoviescinema.com/watch-1997-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1996[/B][/COLOR]','http://onlinemoviescinema.com/watch-1996-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1995[/B][/COLOR]','http://onlinemoviescinema.com/watch-1995-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1994[/B][/COLOR]','http://onlinemoviescinema.com/watch-1994-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1993[/B][/COLOR]','http://onlinemoviescinema.com/watch-1993-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1992[/B][/COLOR]','http://onlinemoviescinema.com/watch-1992-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1991[/B][/COLOR]','http://onlinemoviescinema.com/watch-1991-movies/',1005111,'','','','')
    Menu_1('[COLORblue][B]1990[/B][/COLOR]','http://onlinemoviescinema.com/watch-1990-movies/',1005111,'','','','')
    
    
     
def scrape_movie_year(url,name):
    Menu_1(name,'','','','','','')
    Menu_1('[COLORblue][B]BACK TO YEARS[/B][/COLOR]','',1004111,'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ','','','')
    html = requests.get(url).text
    Next = re.compile('<li><a class="next page-numbers" href="(.+?)">Next .+?</a>',re.DOTALL).findall(html)
    block = re.compile('<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>',re.DOTALL).findall(html)
    match = re.compile('<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"',re.DOTALL).findall(str(block))    
    for url, img, name in match:
        html2 = requests.get(url).text
        frame = re.compile('<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER',re.DOTALL).findall(html2)
        for source in frame:
            html3 = requests.get(source).text
            match = re.compile('\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|',re.DOTALL).findall(html3)
            for a,b,c,d,link in match:
                if a == 'xyz':
                    fin_url = 'http://xyz.streamjunkie.tv/hls/'+link+',.urlset/master.m3u8'
                    Play_1(name,fin_url,1001111,img,img,'','')
                else:
                    fin_url = 'http://'+d+'.'+c+'.'+b+'.'+a+'/hls/,'+link+',.urlset/master.m3u8'
                    Play_1(name,fin_url,1001111,img,img,'','')
            
    for nxt in Next:
        Menu_1('[COLORblue][B]NEXT[/B][/COLOR]',nxt,1005111,'','','','')
def Big_Resolve(name,url):
	import urlresolver
	try:
		resolved_url = urlresolver.resolve(url)
		xbmc.Player().play(resolved_url, xbmcgui.ListItem(name))
	except:
		xbmc.Player().play(url, xbmcgui.ListItem(name))
	xbmcplugin.endOfDirectory(int(sys.argv[1]))
#------------------------------Film On---------------------------------------------------------------------

#------------------------------World IPTV2---------------------------------------------------------------------
def World11():
    html=OPEN_URL(Decode('aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8='))
    match = re.compile("<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>",re.DOTALL).findall(html)
    for url,name in match:
        if 'Daily' in name:
            addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,9008,ICON)
def World22(url):
    html=OPEN_URL(url)
    match = re.compile('>http(.+?)<br />',re.DOTALL).findall(html)
    for url in match:
        addDir3('[COLOR'+TEXTCOL+']NOT A GENIE LIST[/COLOR]',('http'+url).replace('amp;',''),9009,ICON)
def World33(url):
    addDir4('[COLOR'+TEXTCOL+']SOME WILL, SOME WONT[/COLOR]','','','')
    addDir4('[COLOR'+TEXTCOL+']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]','','','')
    addDir4('[COLOR'+TEXTCOL+']DONT BLAME US![/COLOR]','','','')
    html=OPEN_URL(url)
    match = re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n#').findall(html)
    for name,url in match:
        addDir4((name).replace('_',' '),url,222,ICON)
#------------------------------IPTV LISTS---------------------------------------------------------------------
def IPTVLISTS1():
    html=cloudflare.source(Decode('aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=')) 
    match = re.compile('<a href="([^"]*)">(.+?)</a>').findall(html)
    for url,name in match:
        if '.m3u' in url:
            addDir3((name).replace('_',' ').replace('.m3u',''),((Decode('aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8='))+url),9011,ART+'disclose.png')
def IPTVLISTS2(url):
    html=cloudflare.source(url)
    match = re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n#').findall(html)
    for name,url in match:
        addDir4((name).replace('_',' '),url,222,'')
#------------------------------DISCLOSE SCRAPE---------------------------------------------------------------------
def cnfTV():
    html=OPEN_URL('http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/')
    match = re.compile('<li><a href="([^"]*)">(.+?)</a></li>').findall(html)
    for url,name in match:
        if 'category' in url:
            addDir3(name,'http://www.disclose.tv/' + url,7010,ART+'disclose.png')


def cnfTVCat(url):
    html=OPEN_URL(url)
    match = re.compile('href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />',re.DOTALL).findall(html)
    next = re.compile('<link rel="next" href="([^"]*)" />').findall(html)
    for url,name,img in match:
        addDir3(name,'http://www.disclose.tv/' + url,7011,img)
    for url in next:
        addDir3('NEXT',url,7010,ART + 'Next.png')


def cnfTVPlay(url):
    html=OPEN_URL(url)
    match = re.compile('url: "([^"]*)",',re.DOTALL).findall(html)
    match2 = re.compile("src='([^']*)' type='([^']*)' />",re.DOTALL).findall(html)
    match3 = re.compile('<div class="youtube-player" data-id="([^"]*)">',re.DOTALL).findall(html)
    for url in match:
        if 'http' in url:
            addDir4('video/flv',url,222,ART+'disclose.png')
    for url,name in match2:
        addDir4(name,url,222,ART+'disclose.png')
    for url in match3:
        addDir4('YT Link',url,8043,ART+'disclose.png')

#------------------------------Classic Tv SCRAPE---------------------------------------------------------------------
def cnfTVPlay1(url):
    html=OPEN_URL(url)
    match = re.compile('<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>',re.DOTALL).findall(html)
    for url,name in match:
        addDir3(name,(url + '&fv=&sou=').replace('player','watch'),7000,ART+'icon.png')

def Get_Page(name, url, img):
    HTML = OPEN_URL(url)
    Page_Link = re.compile('<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>',re.DOTALL).findall(HTML)
    No_PageLinks = len(Page_Link)
    
    
    if No_PageLinks == 1:
        for PageLink in Page_Link:
            PageLink = PageLink.replace('player','watch')
            Resolve_Link = PageLink + '&fv=&sou='
            Resolve_Page = OPEN_URL(Resolve_Link)
            Resolved = re.compile('<source src="([^"]*)" type=".+?">',re.DOTALL).findall(Resolve_Page)
            for Link in Resolved:
                isFolder=False
                Resolve(Link)
    
    elif No_PageLinks > 1:
        
        for PageLink in Page_Link:
            Get_NextURL = OPEN_URL(PageLink)
            NextURL = re.compile('<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>',re.DOTALL).findall(Get_NextURL)
            RT_Link = NextURL
            RT_Link = (str(RT_Link)).replace('[\'', '').replace('\']', '');
            print 'Stripped url : ' + RT_Link
            addDir4('DOUBLE LINK',RT_Link,424,'')
			
            for url in NextURL:
					addDir3('DOUBLE LINK',url,424,'')
					try:
						url2 = Google.resolve(url)
					except:
						pass
					try:
						find_Links = re.findall(r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}", str(url2))
						for HD, SD in find_Links:
							
							HD_URLS.append(HD)
							SD_URLS.append(SD)
					except:
						pass
    else:
        pass

def MOVIES_TWO():
#    addDir3('Top 20 Most Viewed','http://cnfstudio.com',7014,ART+'Movies.png')
#    addDir3('Box Office','http://cnfstudio.com/category/box-office/',7024,ART+'Movies.png')
    addDir3('Genres','http://cnfstudio.com/movies/',7002,ART+'Movies.png')
#    addDir3('By Year','http://cnfstudio.com',7015,ART+'Movies.png')
    addDir3('Search Movies','',7017,ART+'Movies.png')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

		
def cnfHome():      
    html=OPEN_URL('http://cnfstudio.com/')
    match = re.compile('<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(name,'http://cnfstudio.com/genre/' + url,7003,ART+'icon.png')
		
Dialog = xbmcgui.Dialog()
		
UN='{UN},';IG='{IG},';PL='{PL},';LO='{LO},';LP='{LP},';HA='{HA},';XD='{XD},';TA='{TA},';DP='{DP},';JT='{JT},';JJ='{JJ},';MM='{MM},';FQ='{FQ},';HH='{HH},'
		
def cnfCat(url):
    html=OPEN_URL(url)
    match = re.compile('<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>',re.DOTALL).findall(html)
    prev = re.compile("<link rel='next' href='(.+?)'/>").findall(html)
    for img,url,name in match:
		addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('&#038;','').replace('&#8216;','').replace('&#8217;','').replace('&#8211;',''),url,7004,img)
    prev=prev
    for url in prev:
		addDir3('Next Page',url,7003,ART + 'Next.png')

def cnfMovie(url):

    html=OPEN_URL(url)
    match = re.compile('<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>',re.DOTALL).findall(html)
    for url in match:
        link = url + '&fv=&sou='
        link = link.replace('player','watch')
        Play_URL = cnfPlay1(link)
        ResolvePlayURL = cnfPlay1(url)


def cnfPlay1(url):

    html=OPEN_URL(url)
    match = re.compile('<video id=".+?<source src="([^"]*)" type="video/mp4">',re.DOTALL).findall(html)
    for url in match:
        RESOLVE(url)

#------------------------------PLAYLIST LOADER----------------------------------------------------------------
def LOADER():
    addDir('[COLOR'+TEXTCOL+']Local M3u[/COLOR]',LocalM3u,2001,ART+'LocalM3U.png',FANART,'')
    addDir('[COLOR'+TEXTCOL+']Remote M3u[/COLOR]',RemoteM3u,7080,ART+'RemoteM3U.png',FANART,'')
	
def LocalM3UPLAY():
    if os.path.exists(LocalM3u):
        open_file = open(LocalM3u,'r')
        for item in open_file:
            item_regex = re.compile(r'#EXTINF:.+?,(.+?)\n(.+?)\n#').findall(item)
            for name,url in item_regex:
                addDir4(name,url,222,ART + 'streams.png')
    else:
        Dialog.ok('Set m3u path','you need to set path to your m3u file')
        ADDON.openSettings(sys.argv[0])

def M3UPLAY(url):
	if os.path.exists(Remote):
		HTML = OPEN_CAT(url)
		match = re.compile('EXTINF:.+?,(.+?)\n(.+?)\n#',re.DOTALL).findall(HTML)
		for name,url in match:
			url = (url).strip()
			addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('_',' '),url,222,'')
	else:
		Dialog.ok('Set m3u path','you need to set path to your m3u file')
		ADDON.openSettings(sys.argv[0])
#--------------------------------------------------------------------------------------------------------
#Addon Installer
def Force_Addon_Download():
    HTML = OPEN_URL(Decode('aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY='))
    match = re.compile('<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>').findall(HTML)
    for url in match:
        url = Decode('aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==')+url
    name = 'plugin.video.GenieTv'
	
    Addon_Extract2(url,name)

def Force_Repo_Download():
    HTML = OPEN_URL(Decode('aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2'))
    match = re.compile('<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>').findall(HTML)
    for url in match:
        url = Decode('aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=')+url
    name = 'repository.GenieTv'
	
    Addon_Extract2(url,name)

	
def Addons_Menu():
	choices = ['[COLOR'+TEXTCOL+']CATAGORIES[/COLOR]','[COLOR'+TEXTCOL+']SEARCH[/COLOR]']
	choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']TOOLS[/COLOR]', choices)
	if choice==0:
		Addon_Cat()
	if choice==1:
		Search_Addons()
#    addDir('[COLOR'+TEXTCOL+']CATAGORIES[/COLOR]','',10051,ART+'Catagories.png',FANART,'')
#    addDir('[COLOR'+TEXTCOL+']SEARCH[/COLOR]','',10052,ART+'Search.png',FANART,'')


ADDON        =  xbmcaddon.Addon(id='plugin.video.GenieTv')
Dialog 		 =  xbmcgui.Dialog()
HOME         =  xbmc.translatePath('special://home/')
dp           =  xbmcgui.DialogProgress()
base_url 	 = 'https://addons.tvaddons.ag/'

def Search_Addons():
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM)
    Search_Title = Search_Name.lower()
    Search_URL = 'https://addons.tvaddons.ag/search/?keyword=' + Search_Title 
    HTML = OPEN_URL(Search_URL)
    match = re.compile('<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>').findall(HTML)
    for url,image,name in match:
            addDir(name,url,10054,'https://addons.tvaddons.ag/'+image,FANART,'')


def Addon_Cat():
    HTML = OPEN_URL(base_url)
    match = re.compile('<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>').findall(HTML)
    for url,img,name in match:
        if 'Repositories' in name:
            pass
        elif 'Services' in name:
            pass
        elif 'International' in name:
            pass
        else:
            addDir('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,10053,'https://addons.tvaddons.ag/'+img,FANART,'')


def Addon(url):
    HTML = OPEN_URL(url)
    Next = re.compile('<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>').findall(HTML)
    match = re.compile('<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>').findall(HTML)
    for url,img,name in match:
        if 'Please' in name:
            pass
        else:
            addDir2(name,url,10054,'https://addons.tvaddons.ag/'+img,FANART,'')
    for url in Next:
        addDir('[COLOR'+TEXTCOL+']NEXT PAGE[/COLOR]','https://addons.tvaddons.ag'+url,10053,ART + 'Next.png',FANART,'')


def Addon_Extract(url,name):
    HTML = OPEN_URL(url)
    match = re.compile('<a href="([^"]*)"').findall(HTML)
    for url in match:
        if 'plugin' in url:
            print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
            path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
            dp = xbmcgui.DialogProgress()
            dp.create("GenieTv","Downloading Content",'', 'Please Wait')
            lib=os.path.join(path, name+'.zip')
            try:
                os.remove(lib)
            except:
                pass
            downloader.download(url, lib, dp)
            addonfolder = xbmc.translatePath(os.path.join('special://home','addons'))
            time.sleep(2)
            dp.update(0,"", "Extracting Zip Please Wait")
            print '======================================='
            print addonfolder
            print '======================================='
            extract.all(lib,addonfolder,dp)
            UPDATEREPO()

def Addon_Extract2(url,name):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("GenieTv","Downloading Content",'', 'Please Wait')
    lib=os.path.join(path, name+'.zip')
    try:
        os.remove(lib)
    except:
        pass
    downloader.download(url, lib, dp)
    addonfolder = xbmc.translatePath(os.path.join('special://home','addons'))
    time.sleep(2)
    dp.update(0,"", "Extracting Zip Please Wait")
    print '======================================='
    print addonfolder
    print '======================================='
    extract.all(lib,addonfolder,dp)
    UPDATEREPO()

def UPDATEREPO():
    xbmc.executebuiltin( 'UpdateLocalAddons' )
    xbmc.executebuiltin( 'UpdateAddonRepos' )
    Dialog = xbmcgui.Dialog()
    Dialog.ok("Origin + Genie TV", '','                                 REFRESH SUCCESSFUL :)', "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]")
    return

#------------------------------SCOOBY STREAMS---------------------------------------------------------------------
def SCOOBYCATS1(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1007,image)
def SCOOBYCATS2(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,1006,image)
#------------------------RANDOM PLAY----------------------------------------------------------------
def random_list():
    html=OPEN_URL(Decode('aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw'))
    match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>',re.DOTALL).findall(html)
    for url,iconimage,desc,fanart,name in match:
        Random_play(name,100109,url,image=iconimage,isFolder=True)

def get_random(url):
	import random
	Playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
	Playlist.clear()
	Full_List = []
	Count = []
	Name = []
	HTML = OPEN_URL(url)
	match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>',re.DOTALL).findall(HTML)
	for url2,iconimage,desc,fanart,name in match:
		Full_List.append([url2,name])
		if len(Full_List)==len(match):
			for item in Full_List:
				random_movie=random.randint(1,len(Full_List))
				try:
					next_url = Full_List[int(random_movie)]
				except:
					pass
				if len(Count)<=20:
					if next_url[1] not in Name:
						HTML2 = OPEN_URL(next_url[0])
						match3 = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(HTML2) 
						for Playlink_url,Ep_name in match3: 
							HTML4 = OPEN_URL(Playlink_url)
							match4 = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(HTML4)
							for ignore,link in match4:
								if 'panda' in link:
									HTML5 = OPEN_URL(link)
									match5 = re.compile("url: '(.+?)'").findall(HTML5)
									for finally_got_there_phew in match5:
										if 'http' in finally_got_there_phew:
											liz = xbmcgui.ListItem(next_url[1], iconImage=IMAGES, thumbnailImage=IMAGES)
											liz.setInfo( type="Video", infoLabels={"Title": next_url[1]})
											liz.setProperty("IsPlayable","true")
											Playlist.add(finally_got_there_phew, liz)
											xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
			
def Random_play(name, mode, url='', image=None, isFolder=True, page=1, keyword=None, infoLabels=None, contextMenu=None):
    if not image:
        image = ICON
    u  = sys.argv[0] 
    u += '?mode='  + str(mode)
    u += '&title=' + urllib.quote_plus(name)
    u += '&image=' + urllib.quote_plus(image)
    u += '&page='  + str(page)
    if url != '':     
        u += '&url='   + urllib.quote_plus(url) 
    if keyword:
        u += '&keyword=' + urllib.quote_plus(keyword) 
    liz = xbmcgui.ListItem(name, iconImage=image, thumbnailImage=image)
    if contextMenu:
        liz.addContextMenuItems(contextMenu)
    if infoLabels:
        liz.setInfo(type="Video", infoLabels=infoLabels)
    if not isFolder:
        liz.setProperty("IsPlayable","true")
    liz.setProperty('Fanart_Image', FANART)     
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

#------------------------------THE REAPER---------------------------------------------------------------------
def REAPER(url,iconimage,name):
    from imports import cache
    cache = cache.get('', 0, url)
    html=OPEN_CAT(url)
    match=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(html)
    for url,iconimage,desc,fanart,name in match:
        if 'http' in url:
			if '.php' in url:
					Watched = re.compile('url="([^"]*)"\n').findall(str(watched_read))   
					for item in Watched:											   
						if item == url:												   
							name = ('[COLORred]Watched - [/COLOR]'+name).replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]')                 
					addDirPand2(name,url,1016,iconimage,fanart,desc)
			else:
				if 'youtube' in url:
					Watched = re.compile('url="([^"]*)"\n').findall(str(watched_read))   
					for item in Watched:											   
						if item == url:												   
							name = ('[COLORred]Watched - [/COLOR]'+name).replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]')                
					addDirPand(name,(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,iconimage,fanart,desc)     
				else:
					Watched = re.compile('url="([^"]*)"\n').findall(str(watched_read))   
					for item in Watched:											   
						if item == url:												   
							name = ('[COLORred]Watched - [/COLOR]'+name).replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]').replace('[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]','[COLORred]Watched - [/COLOR]')                 
					addDirPand(name,url,222,iconimage,fanart,desc)			
					setView('tvshows', 'Media Info 3')      
        else:
            Decrypt(url,iconimage,name)
            
    else:
        match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
        for url,image,name in match:
            if 'http' in url:
				if '.php' in url:
					addDir3(name,url,1016,image)
				else:
					if 'youtube' in url:
						print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
						addDir4(name,(url).replace('https://www.youtube.com/watch?v=','').replace('http://www.youtube.com/watch?v=',''),8043,image)
					else:
						Watched = re.compile('url="([^"]*)"\n').findall(str(watched_read))   
						for item in Watched:											   
							if item == url:												   
								name = '[COLORred]Watched - [/COLOR]'+name                 
						addDir4(name,url,222,image)
						setView('tvshows', 'Media Info 3')      
            else:
			    Decrypt(url,image,name)
        xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
    return cache
		
def Decrypt(url,iconimage,name):
    iconimage = iconimage
    name = name
    url = url
    DeCrypt_Multi = (url).replace(IX,'http').replace(UD,'.com');
    Decrypt1 = (DeCrypt_Multi).replace(LM,'a').replace(XG,'b').replace(JP,'c').replace(WE,'d').replace(PL,'e').replace(JT,'f');
    Decrypt2 = (Decrypt1).replace(XX,'g').replace(HA,'h').replace(YT,'i').replace(PF,'j').replace(HW,'k').replace(RT,'l');
    Decrypt3 = (Decrypt2).replace(SF,'m').replace(IF,'n').replace(PW,'o').replace(GF,'p').replace(DD,'q').replace(UO,'r');
    Decrypt4 = (Decrypt3).replace(LE,'s').replace(WP,'t').replace(ZY,'u').replace(UE,'v').replace(PE,'w').replace(JE,'x');
    Decrypt5 = (Decrypt4).replace(TH,'y').replace(LK,'z').replace(UN,'.').replace(IG,'(').replace(LO,')').replace(LP,'/');
    Decrypt6 = (Decrypt5).replace(ZH,'1').replace(PP,'2').replace(AM,'3').replace(TA,'4').replace(DP,'5').replace(JS,'6');
    Decrypt7 = (Decrypt6).replace(JJ,'7').replace(MM,'8').replace(FQ,'9').replace(HH,'0').replace(PQ,':').replace(SC,'%');
    url = (Decrypt7).replace(UJ,'-').replace(XD,'_');
    addDir4(name,url,222,iconimage);
	
#-----------------------------VOD----------------------------------------------------------------------
def TESTCATS2():
    html=OPEN_CAT(Decode('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA=='))
    match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1007,image)
def TESTCATS3(url):

    html=OPEN_CAT(url)
    match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,1006,image)

def TestPlayUrl(name, url, iconimage=None):
	print '--- Playing "{0}". {1}'.format(name, url)
	listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
	listitem.setInfo(type="Video", infoLabels={ "Title": name })
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		
#-----------------------------MUSIC-SCRAPE---------------------------------------------------------------------
def MUSIC1(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,img,name in match:
		if '-dir-' in name:
			addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('-dir-',''),url,1012,img)
		else:
			addDir3('[COLOR'+TEXTCOL+']'+name+'[/COLOR]',url,1006,img)
#marker
def MUSICDIR(url):
    html=OPEN_CAT(url)
    URL2 = ('http://afewbitsmore.com/')
    match = re.compile('<A HREF="([^"]*)">(.+?)</A><br>',re.DOTALL).findall(html)
    for url,name in match:
        if '[To Parent Directory]' in name: 
            name = 'HOME'
            pass
        elif 'HOME' in name:
            pass
        elif '.m3u' in name:
            addDir3('[COLOR'+TEXTCOL+']PLAY ALL[/COLOR]',URL2 + url,2002,ART+'music.png')
        elif '.mp3' in name:
            addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.mp3','').replace('amp;',''),URL2 + url,222,ART+'music.png')
        elif '.m4a' in name:
            addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.m4a','').replace('amp;',''),URL2 + url,222,ART+'music.png')
        else:
            addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]'),URL2 + url,1012,ART+'music.png')
def MusicM3UPLAY(url):
    HTML = OPEN_CAT(url)
    match = re.compile('EXTINF:(.+?),(.+?)\n(.+?)\n#',re.DOTALL).findall(HTML)
    for img,name,url in match:
        addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('_',' '),url,222,ART+'music.png')
			
def MUSIC2(url):
    html=OPEN_CAT(url)
    URL2 = url
    match = re.compile("<a href='(.+?)'>(.+?)</a>").findall(html)
    for url,name in match:
        if '.mp3' in name:
            print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
            addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.mp3','').replace('/',''),'http://hypem.com' + url,222,ART+'music.png')
        else:
            addDir3(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('/',''),URL2 + url,1011,ART+'music.png') 
def MUSIC3():
    html=OPEN_CAT(Decode('aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw=='))
    match = re.compile('<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>',re.DOTALL).findall(html)
    for url,img,name in match:
        addDir3(name,('http://www.cyn.net/music/' + url).replace(' ','%20'),1031,('http://www.cyn.net/music/' + img).replace(' ','%20'))
def MUSIC4(url,img):
    html=OPEN_CAT(url)
    url2 = url
    img = img
    match = re.compile('<a href="([^"]*)">(.+?)</a>',re.DOTALL).findall(html)
    for url,name in match:
        addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.mp3',''),(url2 +'/'+ url).replace(' ','%20'),222,img)

def MUSICVIDS(url):
    html=OPEN_CAT(url)
    url2 = url
    match = re.compile('alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>',re.DOTALL).findall(html)
    for type,url,name in match:
        if '[VID]' in type:
            addDir4(('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('.mp4','').replace('_H.264-AAC','').replace('(',' (').replace(')',') '),url2+url,222,ART+'music.png')
        if '[DIR]' in type:
            MUSICVIDS(url2+url)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);
		
		
def Search_Music_Lists():
    Base_list = (Decode('aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8='))
    Search_Name = Dialog.input('Search', type=xbmcgui.INPUT_ALPHANUM) 
    Search_Title = Search_Name.lower()
    url = (Decode('aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw'))
    url1 = (Decode('aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw=='))
    url2 = (Decode('aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv'))
	
    HTML = OPEN_Search(url)	
    HTML1 = OPEN_Search(url1)	
    HTML2 = OPEN_Search(url2)	

    if HTML != 'Failed':			
		match = re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>').findall(HTML)
		for url,iconimage,desc,background,name in match:
				if Search_Name in name.lower():
					addDir(('[COLOR'+TEXTCOL+']'+name+'[COLORgold] source RaysRavers[/COLOR]').replace('_',' '),url,1016,iconimage,fanart,desc)
					
					setView('tvshows', 'Media Info 3')			
    if HTML1 != 'Failed':			
		match1 = re.compile('<a href="([^"]*)">(.+?)</a>').findall(HTML1)
		for url,name in match1:
				if Search_Name in name.lower():
					addDir3(('[COLOR'+TEXTCOL+']'+name+'[COLORgold] source 1').replace('..&gt;','').replace('/','')+'[/COLOR]',((Decode('aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw=='))+url).replace(' ','%20'),1006,ART+'Music.png')
					
					setView('tvshows', 'Media Info 3')			
    if HTML2 != 'Failed':			
		match2 = re.compile('<td><a href="([^"]*)">(.+?)</a></td>').findall(HTML2)
		for url,name in match2:
				if Search_Name in name.lower():
					addDir3(('[COLOR'+TEXTCOL+']'+name+'[COLORgold] source 2').replace('..&gt;','').replace('/','')+'[/COLOR]',((Decode('aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv'))+url).replace(' ','%20'),1006,ART+'Music.png')
					
					setView('tvshows', 'Media Info 3')			
		

#################################
#######  GenieTv Streams ########
#################################

SF='{SF},';IF='{IF},';PW='{PW},';AM='{AM},';GF='{GF},';DD='{DD},';UO='{UO},';LE='{LE},';ZY='{ZY},';UE='{UE},';PE='{PE},';JE='{JE},';TH='{TH},';LK='{LK},'

#------------------------------------------iwatch series---------------------------------------------    
def iwatch1():
    html=OPEN_URL('http://www.iwatchseries.me/tv-list/')
    match = re.compile('<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>').findall(html)
    for url,name in match:
        addDir3(name,url,8021,ART+'iwatch.png')
        setView('movies', 'MAIN')
def iwatch2(url):
    html=OPEN_URL(url)
    match = re.compile('<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>').findall(html)
    for url,name,title in match:
        addDir3(name+title,url,8022,ART+'iwatch.png')
def iwatch3(url):
    html=OPEN_URL(url)
    match = re.compile('<iframe src="([^"]*)"').findall(html)
    for url in match:
        print '>>>>>>>>>>>>>>>>>>>>'+url
        iwatch4(url)
def iwatch4(url):
    html=OPEN_URL(url)
    match = re.compile('{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"',re.DOTALL).findall(html)
    match2 = re.compile('setup\(\{.+?file: "([^"]*)",.+?skin',re.DOTALL).findall(html)
    match3 = re.compile("{ label: '([^']*)', file:.+?'([^']*)' }").findall(html)
    match4 = re.compile('"file":"([^"]*)","label":"([^"]*)"').findall(html)
    for url,name in match:
        addDir4('VidSpot - '+name,url,222,ART+'iwatch.png')
    for url in match2:
        addDir4('VodLocker',url,222,ART+'iwatch.png')
    for url,name in match4:
        addDir4('VidUp'+name,url,222,ART+'iwatch.png')
    for name,url in match3:
        print '<><><><><><><><><><><> before   ' + url
        if 'hevideo' in url:
            print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
            addDir4('TheVideo - '+name,url,222,ART+'iwatch.png')
#------------------------------------------AnimeLand---------------------------------------------    
def ANIMELIST():
    html=cloudflare.source('http://www.animeland.me/anime-list')
    match = re.compile('letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>').findall(html)
    for url,name in match:
        addDir3(name,url,1021,ART+'anime.png')

#------------------------------------------AnimeToon---------------------------------------------    
def TESTCATS():
    html=OPEN_URL('http://www.animetoon.org/cartoon')
    match = re.compile('<td><a href="([^"]*)">(.+)</a></td>').findall(html)
    for url,name in match:
        addDir3(name,url,1002,ART+'anime.png')
	
		
		
def LISTS(url):
    html=OPEN_URL(url)
    match2 = re.compile('<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />').findall(html)
    for img in match2:
        IMAGE = img
    match3 = re.compile('<li><a href="([^"]*)">Next</a></li>').findall(html)
    for url in match3:
	    addDir3('NEXT PAGE',url,1002,ART + 'Next.png')
    match = re.compile('&nbsp;<a href="([^"]*)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(name,url,1003,IMAGE)
    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);	
def LISTS2(url,IMAGE):
    html=OPEN_URL(url)
    match = re.compile('"playlist">(.+?)</span></div><div><iframe src="([^"]*)"').findall(html)
    for name,url in match:
        print name + '     ' + url
        if 'easy' in url:
            LISTS3(url)
        elif 'playpanda' in url:
		    LISTS3(url)
        
	xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);			
def LISTS3(url):
    html=OPEN_URL(url)
    match = re.compile("url: '(.+?)',").findall(html)
    for url in match:
        addDir4('STREAM',url,222,ART+'anime.png')
		
        
def OPEN_Movie(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0")
        req.add_header('referer', url)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
        
def OPEN_CAT(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def Live_VOD(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_CAT(url)
        match=re.compile('<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(link)
        for url,image,name in match:
                addDir4('%s'%('[COLOR'+TEXTCOL+']'+name+'[/COLOR]').replace('GenieTv','[COLOR green]GenieTV[/COLOR]').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),222,image)
 
def RESOLVEchoice(url):
    if ADDON.getSetting('down')=='true':
        RESOLVEdown(url,name) 
    else:
        RESOLVEtest(url)
def RESOLVEtest(url):
	import urlresolver
	try:
		resolved_url = urlresolver.resolve(url).strip()
		xbmc.Player().play(resolved_url, xbmcgui.ListItem(name))
	except:
		try:
			xbmc.Player().play(url, xbmcgui.ListItem(name))
		except:
			xbmcgui.Dialog().notification("GenieTv", "unplayable stream")
			sys.exit() 
def RESOLVE(url): 
    
    print_text_file = open(watched,"a")                      
    print_text_file.write('url="'+url+'"\n')                 
    print_text_file.close                                    

    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('LOADING','Opening %s Now'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve() 
    if dp.iscanceled(): 
        print "[COLORred]STREAM CANCELLED[/COLOR]" # need to get this part working    
        Dialog = xbmcgui.Dialog()
        if Dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            Dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
	         return
    else:
        try: play.play(url)
        except: pass
        try: ADDON.resolve_url(url) 
        except: pass 
        dp.close()
def RESOLVEdown(url,name):
	url = url
	name = name
	if '.mp4' in url:
		cat = '.mp4'
		choices = ['[COLOR'+TEXTCOL+']PLAY[/COLOR]','[COLOR'+TEXTCOL+']DOWNLOAD[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Play/Download[/COLOR]', choices)
		if choice==0:
			RESOLVEtest(url)
		if choice==1:
			DownMov(url,name,cat)
	elif '.mkv' in url:
		cat = '.mkv'
		choices = ['[COLOR'+TEXTCOL+']PLAY[/COLOR]','[COLOR'+TEXTCOL+']DOWNLOAD[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Play/Download[/COLOR]', choices)
		if choice==0:
			RESOLVEtest(url)
		if choice==1:
			DownMov(url,name,cat)
	elif '.mp3' in url:
		cat = '.mp3'
		choices = ['[COLOR'+TEXTCOL+']PLAY[/COLOR]','[COLOR'+TEXTCOL+']DOWNLOAD[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Play/Download[/COLOR]', choices)
		if choice==0:
			RESOLVEtest(url)
		if choice==1:
			DownMov(url,name,cat)
	elif '.avi' in url:
		cat = '.avi'
		choices = ['[COLOR'+TEXTCOL+']PLAY[/COLOR]','[COLOR'+TEXTCOL+']DOWNLOAD[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Play/Download[/COLOR]', choices)
		if choice==0:
			RESOLVEtest(url)
		if choice==1:
			DownMov(url,name,cat)
	elif '.mov' in url:
		cat = '.mov'
		choices = ['[COLOR'+TEXTCOL+']PLAY[/COLOR]','[COLOR'+TEXTCOL+']DOWNLOAD[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Play/Download[/COLOR]', choices)
		if choice==0:
			RESOLVEtest(url)
		if choice==1:
			DownMov(url,name,cat)
	elif '.mpeg' in url:
		cat = '.mpeg'
		choices = ['[COLOR'+TEXTCOL+']PLAY[/COLOR]','[COLOR'+TEXTCOL+']DOWNLOAD[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Play/Download[/COLOR]', choices)
		if choice==0:
			RESOLVEtest(url)
		if choice==1:
			DownMov(url,name,cat)
	elif '.mpg' in url:
		cat = '.mpg'
		choices = ['[COLOR'+TEXTCOL+']PLAY[/COLOR]','[COLOR'+TEXTCOL+']DOWNLOAD[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Play/Download[/COLOR]', choices)
		if choice==0:
			RESOLVEtest(url)
		if choice==1:
			DownMov(url,name,cat)
	elif '.flv' in url:
		cat = '.flv'
		choices = ['[COLOR'+TEXTCOL+']PLAY[/COLOR]','[COLOR'+TEXTCOL+']DOWNLOAD[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Play/Download[/COLOR]', choices)
		if choice==0:
			RESOLVEtest(url)
		if choice==1:
			DownMov(url,name,cat)
	elif '.wmv' in url:
		cat = '.wmv'
		choices = ['[COLOR'+TEXTCOL+']PLAY[/COLOR]','[COLOR'+TEXTCOL+']DOWNLOAD[/COLOR]']
		choice = xbmcgui.Dialog().select('[COLOR'+TEXTCOL+']Play/Download[/COLOR]', choices)
		if choice==0:
			RESOLVEtest(url)
		if choice==1:
			DownMov(url,name,cat)
	else:
		RESOLVEtest(url)
def DownMov(url,name,cat):
    Check_Down_Path()
    path = xbmc.translatePath(os.path.join(DOWNCONT))
    name = (name).replace('blue','').replace('green','').replace('COLOR','').replace('[','').replace(']','').replace(' ','_').replace('/','')
    file = name+cat
    dp = xbmcgui.DialogProgress()
    dp.create("Your Item Is Downloading","Why not check out our website",'@', 'Http://GenieTv.co.uk')
    lib=os.path.join(path, file)
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]","[COLORblue]Tool Brought To You By GenieTv[/COLOR]")
def Check_Down_Path():
    path = xbmc.translatePath(os.path.join(DOWNCONT))
    if not os.path.exists(DOWNCONT):
        Dialog.ok('[COLOR=white]GenieTv[/COLOR]','The download location you have stored does not exist .\nPlease update the addon settings and try again.','','')        
        ADDON.openSettings(sys.argv[0])
def RESOLVEGTV(url):
        dp = xbmcgui.DialogProgress()
        dp.create('Fetching Your Video','Fetching Your Video')
        dp.update(0,'%s'%name)
        xbmc.sleep(1)
        play=xbmc.Player(GetPlayerCore())
        dp.update(100,'%s'%name)
        xbmc.sleep(1)
        play.play(url).strip()
        dp.close()

def RESOLVER(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    url = (url).strip()
    try: play.play(url).strip()
    except: pass
	
def RESOLVERtest(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    intro = 'http://genietv.co.uk/guide/intro.mp4'
    xbmc.sleep(10)
    play.play(intro)
    xbmc.sleep(1)
    play.play(url)

	
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 
	  
def addDir3(name,url,mode,iconimage,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        if showcontext:
            contextMenu = []
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=100107)' % sys.argv[0]))
            if showcontext == 'fav':
                contextMenu.append(('Remove from Genie TV Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Genie TV Favorites','XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
	
def addDirFolder(name,url,mode,iconimage,fanart,description):

        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    	
def addDir4(name,url,mode,iconimage,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        if showcontext:
            contextMenu = []
            contextMenu.append(('Queue Item', 'RunPlugin(%s?mode=100107)' % sys.argv[0]))
            if showcontext == 'fav':
                contextMenu.append(('Remove from Genie TV Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Genie TV Favorites','XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok        
              

#################################
####### POPUP TEXT BOXES ########
#################################

def TextBoxesImg(url,heading,announce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      self.image =xbmcgui.ControlImage (800, 600, 1200, 450,url, aspectRatio=2)
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.addControl(self.image)
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(announce); text=f.read()
      except: text=announce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()
  TextBox()
def TextBoxes(heading,announce):
  class TextBox():
    WINDOW=10147
    CONTROL_LABEL=1
    CONTROL_TEXTBOX=5
    def __init__(self,*args,**kwargs):
      xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
      self.win=xbmcgui.Window(self.WINDOW) # get window
      xbmc.sleep(500) # give window time to initialize
      self.setControls()
    def setControls(self):
      self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
      try: f=open(announce); text=f.read()
      except: text=announce
      self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
      return
  TextBox()
  TextBox()
def SOURCES():
    TextBoxesImg(ART+'genie.png','GenieTv Recomended Sources', '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]'  )

################################
###    FIX REPOS&ADDONS      ###
################################

def UPDATEREPO():
    xbmc.executebuiltin( 'UpdateLocalAddons' )
    xbmc.executebuiltin( 'UpdateAddonRepos' )
    Dialog = xbmcgui.Dialog()
    Dialog.ok("GenieTv", '','                                 REFRESH SUCCESSFUL :)', "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]")
    return
    
#def FIXREPOSADDONS(url):
#    print '###'+AddonTitle+' - DELETING ADDONS16.DB ###'
#    path = xbmc.translatePath(os.path.join('special://database',''))
#    advance=os.path.join(path, 'addons16.db')
#    try:
#        os.remove(advance)
#        Dialog = xbmcgui.Dialog()
#        print '=== GenieTv - DELETING    '+str(advance)+'    ==='
#        Dialog.ok(AddonTitle, "       Remove Addona16.db Sucessfull Please Reboot To Take Affect")
#    except:
#        Dialog = xbmcgui.Dialog()
#        Dialog.ok(AddonTitle, "       No File To Remove")
#    return

################################
###    End FIX REPOS&ADDONS  ###
################################


################################
###          ADDONS          ###
################################

def NEW(url):
    link = OPEN_URL(str(BASEURL)+D).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def IPTV(url):
    link = OPEN_URL(str(BASEURL)+E).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def VIDEO(url):
    link = OPEN_URL(str(BASEURL)+G).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def SPORTS(url):
    link = OPEN_URL(str(BASEURL)+I).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def KIDS(url):
    link = OPEN_URL(str(BASEURL)+J).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def MUSIC(url):
    link = OPEN_URL(str(BASEURL)+K).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def PROGRAMS(url):
    link = OPEN_URL(str(BASEURL)+L).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def XXX(url):
    link = OPEN_URL(str(BASEURL)+M).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def REPOS(url):
    link = OPEN_URL(str(BASEURL)+O).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def RSS(url):
    link = OPEN_URL(str(BASEURL)+Y).replace('\n','').replace('\r','')
    match = re.compile('name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,5,ART+'GenieTVRSSFeed.png',ART+'GenieTVRSSFeed.png',description)
    setView('movies', 'MAIN')
    
################################
###        End ADDONS        ###
################################

################################
###     DELETE THUMBS        ###
################################

def DELETETHUMBS():
    try:
        if os.path.exists(TNPATH)==True:
            Dialog = xbmcgui.Dialog()
            if Dialog.yesno("Delete Thumbnails", "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]", "This feature deletes your thumbnail folder and textures13.db", "Are you sure you want to do proceed? This Can NOT Be Undone"):
                for root, dirs, files in os.walk(TNPATH):
                    file_count = 0
                    file_count += len(files)
                    if file_count > 0:                
                        for f in files:
                            os.unlink(os.path.join(root, f))               
        text13 = os.path.join(DBPATH,"Textures13.db")               
        os.unlink(text13)
        Dialog.ok("Restart KODI", "Please restart KODI to rebuild thumbnail library")
    except: 
        Dialog = xbmcgui.Dialog()
        Dialog.ok(AddonTitle, "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook")
    return

################################
###     END DELETE THUMBS    ###
################################

################################
###       DELETE CACHE       ###
################################
def LogNotify(title,message,times=2000,icon=ICON):
	xbmc.executebuiltin('XBMC.Notification(%s, %s, %s, %s)' % (title , message , times, icon))

def DELETECACHE(url):
	PROFILEADDONDATA = os.path.join(PROFILE,'addon_data')
	cachelist = [
		(PROFILEADDONDATA),
		(ADDONDATA),
		(os.path.join(HOME,'cache')),
		(os.path.join(HOME,'temp')),
		(os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')),
		(os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')),
		(os.path.join(ADDONDATA,'script.module.simple.downloader')),
		(os.path.join(ADDONDATA,'plugin.video.itv','Images')),
		(os.path.join(PROFILEADDONDATA,'script.module.simple.downloader')),
		(os.path.join(PROFILEADDONDATA,'plugin.video.itv','Images'))]
		
	delfiles = 0

	for item in cachelist:
		if os.path.exists(item) and not item in [ADDONDATA, PROFILEADDONDATA]:
			for root, dirs, files in os.walk(item):
				file_count = 0
				file_count += len(files)
				if file_count > 0:
					for f in files:
						if not f in LOGFILES:
							try:
								os.unlink(os.path.join(root, f))
							except:
								pass
						else: log('Ignore Log File: %s' % f)
					for d in dirs:
						try:
							shutil.rmtree(os.path.join(root, d))
							delfiles += 1
							log("[Success] cleared %s files from %s" % (str(file_count), os.path.join(item,d)))
						except:
							log("[Failed] to wipe cache in: %s" % os.path.join(item,d))
		else:
			for root, dirs, files in os.walk(item):
				for d in dirs:
					if 'cache' in d.lower():
						try:
							shutil.rmtree(os.path.join(root, d))
							delfiles += 1
							log("[Success] wiped %s " % os.path.join(item,d))
						except:
							log("[Failed] to wipe cache in: %s" % os.path.join(item,d))

	LogNotify(ADDONTITLE,'Clear Cache: Removed %s Files' % delfiles)
################################
###     END DELETE CACHE     ###
################################

################################
###     DELETE PACKAGES      ###
################################
def DELETEPACKAGES(url):
    print '###'+AddonTitle+' - DELETING PACKAGES###'
    packages_cache_path = xbmc.translatePath(os.path.join('special://home/addons/packages', ''))
    try:    
        for root, dirs, files in os.walk(packages_cache_path):
            file_count = 0
            file_count += len(files)
            
        # Count files and give option to delete
            if file_count > 0:
    
                Dialog = xbmcgui.Dialog()
                if Dialog.yesno("Delete Package Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                            
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                    Dialog = xbmcgui.Dialog()
                    Dialog.ok(AddonTitle, "       Deleting Packages all done")
                else:
                        pass
            else:
                Dialog = xbmcgui.Dialog()
                Dialog.ok(AddonTitle, "       No Packages to DELETE")
    except: 
        Dialog = xbmcgui.Dialog()
        Dialog.ok(AddonTitle, "Error Deleting Packages please visit The Support Group, GenieTv on facebook")
    refresh()
    return

################################
###    End DELETE PACKAGES   ###
################################

################################
###          CLEANUP         ###
################################
    
def CLEANUP(url):
    print '###'+AddonTitle+' - DELETING PACKAGES###'
    packages_cache_path = xbmc.translatePath(os.path.join('special://home/addons/packages', ''))
    try:    
        for root, dirs, files in os.walk(packages_cache_path):
            file_count = 0
            file_count += len(files)
            
        # Count files and give option to delete
            if file_count > 0:
    
                Dialog = xbmcgui.Dialog()
                if Dialog.yesno("Delete Package Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                            
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                    Dialog = xbmcgui.Dialog()
                    Dialog.ok(AddonTitle, "       Deleting Packages all done")
                else:
                        pass
            else:
                Dialog = xbmcgui.Dialog()
                Dialog.ok(AddonTitle, "       No Packages to DELETE")
    except: 
        Dialog = xbmcgui.Dialog()
        Dialog.ok(AddonTitle, "Error Deleting Packages please visit The Support Group, GenieTv on facebook")
    DELETECACHE(url)
    return


################################
###       End CLEANUP        ###
################################

################################
###       Advanced XML       ###
################################ 
    
def AXML(url,name):
    path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    Dialog = xbmcgui.Dialog()
    bak=os.path.join(path, 'advancedsettings.xml.bak')
    if os.path.exists(bak)==False: 
        if Dialog.yesno("Back Up Original", 'Have You Backed Up Your Original?','', "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]"):
            print '###'+AddonTitle+' - ADVANCED XML###'
            path = xbmc.translatePath(os.path.join('special://home/userdata',''))
            advance=os.path.join(path, 'advancedsettings.xml')
            try:
                os.remove(advance)
                print '=== GenieTv - REMOVING    '+str(advance)+'    ==='
            except:
                pass
            link=net.http_GET(url).content
            a = open(advance,"w") 
            a.write(link)
            a.close()
            print '=== GenieTv - WRITING NEW    '+str(advance)+'    ==='
            Dialog = xbmcgui.Dialog()
            Dialog.ok(AddonTitle, "       Done Adding new Advanced XML")
    else: 
        print '###'+AddonTitle+' - ADVANCED XML###'
        path = xbmc.translatePath(os.path.join('special://home/userdata',''))
        advance=os.path.join(path, 'advancedsettings.xml')
        try:
            os.remove(advance)
            print '=== GenieTv - REMOVING    '+str(advance)+'    ==='
        except:
            pass
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== GenieTv - WRITING NEW    '+str(advance)+'    ==='
        Dialog = xbmcgui.Dialog()
        Dialog.ok(AddonTitle, "       Done Adding new Advanced XML")    
    return

def CHECKADVANCEDXML(url,name):
    print '###'+AddonTitle+' - CHECK ADVANCE XML###'
    path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    try:
        a=open(advance).read()
        if 'zero' in a:
            name='0CACHE'
        elif 'tuxen' in a:
            name='TUXENS'
        elif 'muckys' in a:
            name='MUCKYS'
        elif 'p2p1' in a:
            name='1st P2P RECOMMENDED'
        elif 'p2p2' in a:
            name='2nd P2P RECOMMENDED'
        elif 'mikey' in a:
            name='MIKEY1234'
    except:
        name="NO ADVANCED"
    Dialog = xbmcgui.Dialog()
    Dialog.ok(AddonTitle,"[COLOR yellow]YOU HAVE[/COLOR] "+ name+"[COLOR yellow] XML SETTINGS SETUP[/COLOR]")
    return

def DELETEADVANCEDXML(url):
    print '###'+AddonTitle+' - DELETING ADVANCE XML###'
    path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    try:
        os.remove(advance)
        Dialog = xbmcgui.Dialog()
        print '=== GenieTv - DELETING    '+str(advance)+'    ==='
        Dialog.ok(AddonTitle, "       Remove Advanced Settings Sucessfull")
    except:
        Dialog = xbmcgui.Dialog()
        Dialog.ok(AddonTitle, "       No Advanced Settings To Remove")
    return

################################
###     End Advanced XML     ###
################################

################################
###        CHECK IP          ###
################################
#Thanks to metalkettle for his work on the original IP checker addon        

def IPCHECK(url='http://www.iplocation.net/',inc=1):
    match=re.compile("<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>").findall(net.http_GET(url).content)
    for ip, region, country, isp in match:
        if inc <2: Dialog=xbmcgui.Dialog(); Dialog.ok('Check My IP',"[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ip, '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % country, '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % isp)
        inc=inc+1

#################################
###      END CHECK IP         ###
#################################

#################################
###       CUSTOM FTV          ###
#################################

def CUSTOMINI(url,name):
    Dialog = xbmcgui.Dialog()
    if Dialog.yesno("GenieTv", '                                    Install Latest .ini File'):
        print '###'+AddonTitle+' - CUSTOM FTV INI###'
        path = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/plugin.video.GenieTv',''))
        advance=os.path.join(path, 'addons2.ini')
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== GenieTv - WRITING NEW    '+str(advance)+'    ==='
        Dialog = xbmcgui.Dialog()
        Dialog.ok(AddonTitle, "                               Done Adding New .ini File")  
    return

def CUSTOMSET(url,name):
    Dialog = xbmcgui.Dialog()
    if Dialog.yesno("GenieTv", '                               Install Custom Settings'):
        print '###'+AddonTitle+' - CUSTOM FTV SETTINGS###'
        path = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/plugin.video.GenieTv',''))
        advance=os.path.join(path, 'settings.xml')
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== GenieTv - WRITING NEW    '+str(advance)+'    ==='
        Dialog = xbmcgui.Dialog()
        Dialog.ok(AddonTitle, "                               Done Adding New Settings")  
    return


def DELETEFTVDB():
    try:
        ftvpath = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/plugin.video.GenieTv',''))
        if os.path.exists(ftvpath)==True:
            Dialog = xbmcgui.Dialog()
            if Dialog.yesno("GenieTv", "                               Delete FTV Guide Database"):
                ftvsource = os.path.join(ftvpath,"source.db")               
                os.unlink(ftvsource)               
        Dialog.ok("GenieTv", "                                     FTV Database Reset")
    except: 
        Dialog = xbmcgui.Dialog()
        Dialog.ok(AddonTitle, "               Error Deleting Database No Database To Delete")
    return

#################################
###      END CUSTOM FTV       ###
#################################
        
def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link
    

		
############################
###FRESH START##############
####THANKS TO TVADDONS######

def FRESHSTART(params):
    pluginlog("freshstart.main_list "+repr(params)); yes_pressed=pluginmessage_yes_no(AddonTitle,"Do you wish to restore your","Kodi configuration to default settings?")
    if yes_pressed:
        addonPath=xbmcaddon.Addon(id=AddonID).getAddonInfo('path'); addonPath=xbmc.translatePath(addonPath); 
        xbmcPath=os.path.join(addonPath,"..",".."); xbmcPath=os.path.abspath(xbmcPath); pluginlog("freshstart.main_list xbmcPath="+xbmcPath); failed=False
        try:
            for root, dirs, files in os.walk(xbmcPath,topdown=True):
                dirs[:] = [d for d in dirs if d not in EXCLUDES]
                for name in files:
                    try: os.remove(os.path.join(root,name))
                    except:
                        if name not in ["Addons15.db","MyVideos75.db","Textures13.db","xbmc.log"]: failed=True
                        pluginlog("Error removing "+root+" "+name)
                for name in dirs:
                    try: os.rmdir(os.path.join(root,name))
                    except:
                        if name not in ["Database","userdata"]: failed=True
                        pluginlog("Error removing "+root+" "+name)
            if not failed: pluginlog("freshstart.main_list All user files removed, you now have a clean install"); pluginmessage(AddonTitle,"The process is complete, you're now back to a fresh Kodi configuration with GenieTv!","Please reboot your system or restart Kodi in order for the changes to be applied.")
            else: pluginlog("freshstart.main_list User files partially removed"); pluginmessage(AddonTitle,"The process is complete, you're now back to a fresh Kodi configuration with GenieTv","Please reboot your system or restart Kodi in order for the changes to be applied.")
        except: pluginmessage(AddonTitle,"Problem found","Your settings has not been changed"); import traceback; pluginlog(traceback.format_exc()); pluginlog("freshstart.main_list NOT removed")
        pluginadd_item(action="",title="Now Exit Kodi",folder=False)
    else: pluginmessage(AddonTitle,"Your settings","has not been changed"); pluginadd_item(action="",title="Done",folder=False)
    killxbmc()

          
        
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

N = base64.decodestring('aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==')
A = base64.decodestring('L3N0b3JhZ2UvZW11bGF0ZWQvMA==')
T = base64.decodestring('L2dlbmllLnR4dA==')
B = base64.decodestring('LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=')
F = base64.decodestring('aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=')
C = base64.decodestring('aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s')
D = base64.decodestring('L2FkZG9ucy9uZXcudHh0')
NVOD = base64.decodestring('aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==')
E = base64.decodestring('L2FkZG9ucy9pcHR2LnR4dA==')
G = base64.decodestring('L2FkZG9ucy92aWRlby50eHQ=')
I = base64.decodestring('L2FkZG9ucy9zcG9ydHMudHh0')
J = base64.decodestring('L2FkZG9ucy9raWRzLnR4dA==')
K = base64.decodestring('L2FkZG9ucy9tdXNpYy50eHQ=')
L = base64.decodestring('L2FkZG9ucy9wcm9ncmFtcy50eHQ=')
M = base64.decodestring('L2FkZG9ucy94eHgudHh0')
O = base64.decodestring('L2FkZG9ucy9yZXBvLnR4dA==')
P = base64.decodestring('L2FkZG9ucy9wYWNrcy50eHQ=')
Q = base64.decodestring('L2FkZG9ucy9za2lucy50eHQ=')
R = base64.decodestring('L2FkZG9ucy9hcnQudHh0')
V = base64.decodestring('L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=')
W = base64.decodestring('L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==')
X = base64.decodestring('L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==')
Y = base64.decodestring('L2FkZG9ucy9SU1MudHh0')
BASE = base64.decodestring('Q1VOVA==')
def addFile(display, mode=None, name=None, url=None, menu=None, description=ADDONTITLE, overwrite=True, fanart=FANART, icon=ICON, themeit=None):
	u = sys.argv[0]
	if not mode == None: u += "?mode=%s" % urllib.quote_plus(mode)
	if not name == None: u += "&name="+urllib.quote_plus(name)
	if not url == None: u += "&url="+urllib.quote_plus(url)
	ok=True
	if themeit: display = themeit % display
	liz=xbmcgui.ListItem(display, iconImage="DefaultFolder.png", thumbnailImage=icon)
	liz.setInfo( type="Video", infoLabels={ "Title": display, "Plot": description} )
	liz.setProperty( "Fanart_Image", fanart )
	if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok
def addDirMeta(name,url,mode,iconimage,fanart,description,year,cast,rating,runtime,genre):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description,"Rating":rating,"Year":year,"Duration":runtime,"Cast":cast,"Genre":genre})
	liz.setProperty('fanart_image', fanart)
	liz.setProperty("IsPlayable","true")
	cm = []
	cm.append(('Play Trailer','XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url='+str(name)+')'))
	cm.append(('Movie Information', 'XBMC.Action(Info)'))
	liz.addContextMenuItems(cm,replaceItems=True)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok
def addDir(name,url,mode,iconimage,fanart,description,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Genie TV Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Genie TV Favorites','XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
		
def addDir2(name,url,mode,iconimage,fanart,description,showcontext=True,allinfo={}):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if showcontext:
            contextMenu = []
            if showcontext == 'fav':
                contextMenu.append(('Remove from Genie TV Favorites','XBMC.RunPlugin(%s?mode=10056&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
            if not name in FAV:
                contextMenu.append(('Add to Genie TV Favorites','XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

                      
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None
extra=None
fav_mode=None


try:
    fav_mode=int(params["fav_mode"])
except:
    pass

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
        
        
print str(PATH)+': '+str(VERSION)
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )
        
if iconimage==None: iconimage = ICON
if fanart==None: fanart = FANART        
if mode==None:
        INDEX()

elif mode==1:
        WISHESPC(url)

elif mode==44:
        WISHES(url)

elif mode==2:
        APK()

elif mode==3:
        MAINTENANCE()

elif mode==21:
        ADDONS()

elif mode==4:
        ADVANCEDXML()

elif mode==5:
        WIZARD(url)

elif mode==6:
        DELETEPACKAGES(url)

elif mode==7:
        AXML(url,name)

elif mode==8:
        CHECKADVANCEDXML(url,name)

elif mode==9:
        FIXREPOSADDONS(url)

elif mode==10:
        UPDATEREPO()

elif mode==11:
        DELETEADVANCEDXML(url)

elif mode==12:
        IPCHECK(url='http://www.iplocation.net/',inc=1)

elif mode==13:
        DELETETHUMBS()

elif mode==14:
        DELETECACHE(url)

elif mode==15:
        CUSTOMFTV()

elif mode==16:
        CUSTOMINI(url,name)

elif mode==17:
        CUSTOMSET(url,name)

elif mode==18:
        DELETEFTVDB()

elif mode==19:
        APKTOOL(url)

elif mode==40:
        ARTTOOL(name,url,description)

elif mode==42:
        ADDSKIN(name,url,description)

elif mode==43:
        WIZARDAN(url)

elif mode==20:
        URLFIX(url)

elif mode==22:
        NEW(url)

elif mode==23:
        IPTV(url)

elif mode==24:
        VIDEO(url)

elif mode==25:
        SPORTS(url)

elif mode==26:
        KIDS(url)

elif mode==27:
        MUSIC(url)

elif mode==28:
        PROGRAMS(url)

elif mode==29:
        XXX(url)

elif mode==30:
        ADDONSP(url)

elif mode==31:
        REPOS(url)

elif mode==32:
        BUILD()

elif mode==33:
        SKINS()

elif mode==35:
        Fix_Paths(url)

elif mode==34:
        ARTWORK(url)

elif mode==36:
        GSKIN(url)

elif mode==37:
        HSKIN(url)

elif mode==38:
        ISKIN(url)

elif mode==41:        
        FRESHSTART(params)

elif mode==39:
        RSS(url)

elif mode==45:
        TEXTS()

elif mode==46:
        SOURCES()

elif mode==47:
        GEVID()

elif mode==48:
        LOCALZIP(name,url,description)

elif mode==49:
        RES()
       
elif mode==22222:
        RESOLVE(url)
       
elif mode==222225:
        Resolve_2(url)

elif mode==222:
        RESOLVEchoice(url)

elif mode==2222222:
        RESOLVEtest(url)

elif mode==222222:
        RESOLVEdown(url,name)

elif mode==333:
        Live_VOD(url)


elif mode==1020:
        ANIMELIST()

elif mode==1021:
        ANIMEEP()

elif mode==1022:
        ANIMEPLAY(url)

elif mode==1001:
        TESTCATS()

elif mode==1005:
        TESTCATS2()

elif mode==1007:
        TESTCATS3(url)

elif mode==1010:
        MUSIC1(url)

elif mode==1011:
        MUSIC2(url)

elif mode==1012:
        MUSICDIR(url)

elif mode==1030:
        MUSIC3()

elif mode==1031:
        MUSIC4(url,iconimage)

elif mode==1032:
        MUSICVIDS(url)

elif mode==1006:
        Parse.ParseURL(url)

elif mode==2030:
        Parse.addonParseURL(url)

elif mode==2031:
        Parse.apkParseURL(url)

elif mode==2032:
        Parse.ParseBOSS(url)

elif mode==1002:
        LISTS(url)

elif mode==1003:
        LISTS2(url,iconimage)
        
elif mode==1004:
        LISTS3(url)
        
elif mode==1008:
        CLOUDCATS()
        
elif mode==1009:
        M3UPLAY(url)
        
elif mode==2001:
        LocalM3UPLAY()
        
elif mode==2002:
        MusicM3UPLAY(url)

elif mode==1013:
        RADIO()
elif mode==10111113:
        RADIO2(url)

elif mode==1014:
        EPG()

elif mode==1015:
        EPG2(url)

elif mode==1016:
        REAPER(url,iconimage,name)

elif mode==1017:
        HEROVISION()

elif mode==1018:
        BAMFTV(url)

elif mode==1019:
        Get_BAMF_playlinks(url)
elif mode==10190:
        Get_BAMF247_playlinks(url)

elif mode==1023:
        SCOOBYCATS()

elif mode==1024:
        SCOOBYCATS1(url)

elif mode==1025:
        SCOOBYCATS2(url)

elif mode==4001:
        MenWish()

elif mode==4002:
        MenStream()

elif mode==4003:
        MenMusic()

elif mode==4004:
        MenStreammov()

elif mode==4005:
        MenStreamtv()

elif mode==4006:
        MenStreamteam()

elif mode==4007:
        MenStreamkids()

elif mode==4008:
        MenStreamhob()

elif mode == 40099: start()
elif mode == 4009: MenLiveTV()
elif mode == 4010: ReCreate_Addon_ini()
elif mode==3000:
        LOADER()
       
elif mode==3001:
        CLASSICS1()
       
elif mode==3002:
        CLASSICS2(url)
       
elif mode==3003:
        CLASSICS3(url)
       
elif mode==3004:
        CLASSICS4(url)
       
elif mode == 404: 
        TestPlayUrl(name,url,iconimage)
       
elif mode == 405: 
        RESOLVEGTV(url)

elif mode == 7030:
        LiveTVFullCat()

elif mode == 7021:
        List_LiveTVFull(name)

elif mode == 7022:
        LiveTVFull(name)

elif mode == 7000:
		Get_Page(name, url, img)
		
elif mode == 7050:
        WATCHCATS(url)

elif mode == 7051:
        WATCHLIST(url)

elif mode == 70511:
        WATCHLIST2(url)

elif mode == 7052:
        CoolAZ(url)

elif mode == 7053:
        CoolLIST(url)

elif mode == 7054:
        CoolPlay(url)

elif mode == 7060:
        NATCATS()

elif mode == 7061:
        NATLIST(url)

elif mode == 7063:
        NATLISTtv(url)

elif mode == 7062:
        WATCHNAT(url)

elif mode == 7064:
        NATatozcat()

elif mode == 7067:
        NATtvPULL(url)

elif mode == 7066:
        NATatozA(url)

elif mode == 7065:
        WATCHNATtv(url)

elif mode == 7070:
        DIZIcat()

elif mode == 7071:
        DIZIlist(url)

elif mode == 7072:
        DIZIpull(url)

elif mode == 7073:
        WATCHDIZI(url)

elif mode == 7002:
        cnfHome()

elif mode == 7003:
        cnfCat(url)

elif mode == 7004:
        cnfMovie(url)

elif mode == 7020:
        cnfPlay1(url)

elif mode == 7001:
        cnfTV()

elif mode == 7010:
        cnfTVCat(url)

elif mode == 7011:
        cnfTVPlay(url)

elif mode == 7012:
        cnfTVPlay1(url)

elif mode == 7013:
        cnfTVPlay2(url)
elif mode == 7014: 
		CNF_Studio_Indexer.MV_Movies(url)
elif mode == 7015:
		CNF_Studio_Indexer.Movie_ByYear(url)
elif mode == 7016:
		CNF_Studio_Indexer.Resolve_CNF_Link(name, url, iconimage)
elif mode == 7017:
		CNF_Studio_Indexer.Search_Movie()
elif mode == 7018:
		MOVIES_TWO()
elif mode == 7019: 
		CNF_Studio_Indexer.List_Movies(url)
elif mode == 7020: 
		CNF_Studio_Indexer.Get_Movie_Page(url)
elif mode == 7024: 
		CNF_Studio_Indexer.Box_Office(url)

elif mode == 8000:
		Soap_TV()
elif mode == 8001:
		CoronationStreet()
elif mode == 8002:
		Eastenders()
elif mode == 8003: 
		Emmerdale()
elif mode == 8004: 
		Hollyoaks()
elif mode == 8005: 
		ImACeleb()
elif mode == 8006:
		SOAPPLAYER(name,url)
elif mode == 8030:
		FXSKIN(url)
elif mode == 8045:
		DOCjl1(url)
elif mode == 8046:
		DOCjl2(url)
elif mode == 8047:
		DOCjl3(url)
elif mode == 8048:
		rtd(url)
elif mode == 8049:
		rtd2(url)
elif mode == 804900:
		rtd3(url)
elif mode == 8020:
		iwatch1()
elif mode == 8021:
		iwatch2(url)
elif mode == 8022:
		iwatch3(url)
elif mode == 8023:
		iwatch4(url)
elif mode == 8040:
		DOC1()
elif mode == 8041:
		DOC2(url)
elif mode == 8042:
		DOC3(url)
elif mode == 8043:
		yt.PlayVideo(url)
elif mode == 8044:
		DOCLIST(url)
elif mode == 8060:
		classic_TV()
elif mode == 8061:
		classic_TV2(url)
elif mode == 8064:
		classic_TVshows()
elif mode == 8065:
		classic_TVshows2(url)
elif mode == 8070:
		Get_m3u_links()
elif mode == 8071:
		Get_m3u_playlinks(url)
elif mode == 7080:
		Get_List_playlinks(url)
elif mode == 8090:
		Get_XNXX_CATS()
elif mode == 8091:
		Get_XNXX_VIDS(url)
elif mode == 8092:
		Get_XNXX_playlinks(url)
elif mode == 8093:
		Get_XNXX_next(url)
elif mode == 8081:
		Recent_Scraped()
elif mode == 8062:
		Get_Episode(url)
elif mode == 8063:
		Play_link(url)
elif mode == 8050:
		TOON1()
elif mode == 8051:
		TOON2(url)
elif mode == 8052:
		TOON3(url)
elif mode == 8085:
		get_Country()
elif mode == 8086:
		get_Channel(url)
elif mode == 8087:
		get_Part_1_Link(url)
elif mode == 8088:
		Get_Playlink(url,name)
elif mode == 9000:
		Search_Lists()
elif mode == 1111:
		Search_Music_Lists()
elif mode == 9001:
		Search_Films_Lists()
elif mode == 9002:
		Search_Tv_Lists()
elif mode == 9003:
		Search_LiveTV()
elif mode == 9004:
		World1()
elif mode == 9005:
		World2(url)
elif mode == 9006:
		World3(url)
elif mode == 9007:
		World11()
elif mode == 9008:
		World22(url)
elif mode == 9009:
		World33(url)
elif mode == 9010:
		IPTVLISTS1()
elif mode == 9011:
		IPTVLISTS2(url)
elif mode == 50:
		DOWNLOAD(url)
elif mode == 9020:
		champlist()
elif mode == 9021:
		champ1()
elif mode == 9022:
		champ2()
elif mode == 9023:
		champ3()
elif mode == 9024:
		play_CHAMP(url)
elif mode == 9030:
		IPTV1(url)
elif mode == 9031:
		IPTV2(url)
elif mode == 9032:
		IPTV3(url)
elif mode == 9033:
		IPTV4(url)
elif mode == 9034:
		IPTVMENU()
elif mode == 7084:
		FITNESS()
elif mode == 7085:
		FITNESS1(url)
elif mode == 7086:
		FITNESS2(url,iconimage,description)
elif mode == 7087:
        FITNESS_INFO(description)
elif mode == 9666:
        CLEANUP(url)
elif mode == 10100: X_vid_Menu()
elif mode == 101001: X_vid_Lang(url)
elif mode == 10105: XNew_Videos(url)
elif mode == 10106: XGenres(url)
elif mode == 10104: XPornstars(url)
elif mode == 10107: XSearch_X()
elif mode == 10103: Xtags(url)
elif mode == 10108: XPlayLink(url)
elif mode == 10000: Origin_Menu()
elif mode == 10001: Origin_cartoons()
elif mode == 10002: Origin_Football()
elif mode == 10003: Stand_Up_Home_Menu()
elif mode == 10004: Origin_Cart(url)
elif mode == 10005: Origin_Cart_Search()
elif mode == 10006: Origin_Cartoon_Lists(url)
elif mode == 10007: Origin_Cartoon_Lists2(url,iconimage)
elif mode == 10008: Football_Highlights()
elif mode == 10009: FootballFixturesDay()
elif mode == 10010: FootballFixturesGame(url)
elif mode == 10011: get_All_Rows(url)
elif mode == 10012: RESOLVEtest(url)
elif mode == 10113: GRABG(url,name)
elif mode == 10109: RESOLVERtest(url)
elif mode == 10013: get_PLAYlink(url)
elif mode == 10014 : Origin_StandUp()
elif mode == 10015 : Search_Stand_Up()
elif mode == 10016 : Play_Stage(url)
elif mode == 10017 : My_list()
elif mode == 10018 : Dizzy_Menu()
elif mode == 10019: Recent_Scraped_Dizzy()
elif mode == 10020: Dizzy_Genres()
elif mode == 10021: Dizzy_Search()
elif mode == 10022: Get_Dizzy_Episode(url)
elif mode == 10023: Play_Dizzy_link(name,url)
elif mode == 10024: Dizzy_Genre_Menu(url)
elif mode == 10025: Pand_Home_Menu()
elif mode == 10026: Pand_Search_Menu()
elif mode == 10027: Search_Pandoras_Films()
elif mode == 10028: Search_Pandoras_TV()
elif mode == 10029: Pandoras_Box()
elif mode == 423 	: PANDS_open_Menu(url)
elif mode == 426 	: Pandora_Menu(url)
elif mode == 10030: Izle_Films()
elif mode == 10031: Latest_Izle_Movies()
elif mode == 10032: Izle_Genres()
elif mode == 10033: Izle_Pop_Movies()
elif mode == 10034: Izle_Boxsets()
elif mode == 10035: Izle_Search()
elif mode == 10036: Izle_Genres_Movie(url)
elif mode == 10037: Izle_Boxset_single(url)
elif mode == 10038: Izle_IFRAME()
elif mode == 10039: Izle_Boxsets_Next(url)
elif mode == 10040: Home_Menu_Watchseries()
elif mode == 10041: Get_Watchseries_program(url)
elif mode == 10042: Get_Watchseries_Popular(url)
elif mode == 10043: Search_Watchseries()
elif mode == 10044: Get_Watchseries_Episode(url)
elif mode == 10045: Watchseries(name)
elif mode == 10046: Get_Watchseries_Newest(url)
elif mode == 10047: A_Z_watch(url)
elif mode == 10048: Watch_series_genres(url)
elif mode == 10049: Get_Watchseries_Prog(url)
elif mode == 10050: Addons_Menu()
elif mode == 10051: Addon_Cat()
elif mode == 10052: Search_Addons()
elif mode == 10053: Addon(url)
elif mode == 10054: Addon_Extract(url,name)
elif mode==10055:
    addon_log("addFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name,url,iconimage,fanart,fav_mode)
elif mode==10056:
    addon_log("rmFavorite")
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)
elif mode==10057:
    addon_log("getFavorites")
    getFavorites()
elif mode == 10058: Check_Donator_Password()
elif mode == 10059: Donators_Guide()
elif mode == 10060: BackUp_My_Build()
elif mode == 10061: Community_Backup()
elif mode == 10062: Restore_Backup_XML(name,url,description)
elif mode == 10063: xbmc.executebuiltin("XBMC.RunScript("+start_guide+")")
elif mode == 10064: Youtube_search()
elif mode == 10065: youtube_next(url)
elif mode == 10066: REQUESTS(url)
elif mode == 10068: Film_Trailers(url)
elif mode == 10069: TV_Trailers(url)
elif mode == 10070: TV_Schedule(url)
elif mode == 10071: Genie_Watch()
elif mode == 10072: Genie_Watch_Movies()
elif mode == 10073: Genie_Watch_Genre(url)
elif mode == 10074: Genie_Watch_PlayRun(url)
elif mode == 10075: Genie_Playlink(iconimage,name,url)
elif mode == 10076: Final_Play(url)
elif mode == 10077: Genie_Watch_Most_Viewed(url)
elif mode == 10078: Genie_Watch_Search()
elif mode == 10079: Genie_Watch_Tv_Shows()
elif mode == 10080: Genie_Watch_Tv_Genre(url)
elif mode == 10081: Genie_Watch_TV_PlayRun(url)
elif mode == 10082: Genie_Watch_TV_Episodes(url,iconimage)
elif mode == 10083: Genie_Watch_Tv_Recent(url)
elif mode == 10084: MenSilentHunter()
elif mode == 10085: Force_Addon_Download()
elif mode == 10086: Force_Repo_Download()
elif mode == 20000: KISS_CATS()
elif mode == 20001: KISS_CATS2(url)
elif mode == 20002: KISS_NAME(url)
elif mode == 20003: KISS_GENRE(url)
elif mode == 20004: KISS_SHOW(url)
elif mode == 20005: KISS_EP(url)
elif mode == 21004: WCO_CATS()
elif mode == 21005: WCO_SHOWS(url)
elif mode == 21006: WCO_EP(url)
elif mode == 21007: WCO_PLAY(url)
elif mode == 21008: store(url)
elif mode == 21009: store2(url)
elif mode == 30000     : Home_Menu()
elif mode == 30001 		: Audio()
elif mode == 100121    	: Resolve(url)
elif mode == 30003 		: Kids_Audio()
elif mode == 30004 		: Kids_Play(url)
elif mode == 30005 		: Kids_Play_Multi(url)
elif mode == 30006 		: Kids_Menu()
elif mode == 30007 		: Kids_AZ()
elif mode == 30008 		: Kids_AZ_Audio(url)
elif mode == 30009 		: Match(url)
elif mode == 30010 	: Match2(url)
elif mode == 30011 	: Audio_Menu()
elif mode == 30012 	: Popular()
elif mode == 30013 	: Search_Audio()
elif mode == 30014 	: Search_Kids()
elif mode == 30015 	: THEWIZ(url,iconimage,fanart)
elif mode == 30016 	: THEWIZINSTALL(url)
elif mode == 30019 	: THEWIZINSTALLPC(url)
elif mode == 30017 	: THEWIZDESC(url)
elif mode == 30018	: THEWIZimage(url)
elif mode == 30030	: ARCONAI()
elif mode == 30031	: ARCONAI2()
elif mode == 30032	: ARCONAI3()
elif mode == 30033	: ARCONAI4()
elif mode == 30034	: TUTS()
elif mode == 30035	: APKGAME(url)
elif mode == 30036	: APKAPP(url)
elif mode == 30037	: APKSELECT2(url)
elif mode == 30038	: APKSearch()
elif mode == 30039	: APKSECTION()
elif mode == 50000	: viewLogFile()
elif mode == 50001	: thelist()
elif mode == 50002	: premtable(url)
elif mode == 50003  : Table_Menu(description)
elif mode == 60000  : ADDON.openSettings(sys.argv[0])
elif mode == 60001  : Streams_Menu()
elif mode == 60002  : Live_Events(name)
elif mode == 60003  : Get_Ultimate_playlinks_data(url)
elif mode == 600033  : Get_Ultimate_playlinks(url)
elif mode == 60004  : MyAccDetails(url)
elif mode == 50004  : speedMenu()
elif mode == 50005  : speedtest.runtest(url)
elif mode == 70001  : RadioNomy()
elif mode == 70002  : RadioNomygenre(url)
elif mode == 70003  : RadioNomysort(url)
elif mode == 70004  : RadioNomylist(url)
elif mode == 70005  : RadioNomyplay(url)
elif mode == 70006  : RadioNomysearch()
elif mode == 50006  : TextBoxes(AddonTitle, CONTACT)
elif mode == 80000  : killxbmc()
elif mode == 80001  : resolvefilmon(url)
elif mode == 80002  : apkmasterMenu()
elif mode == 80003  : apkInstaller(name, url,"None")
elif mode == 80004  : APKGRAB(name,url)
elif mode == 80005  : MOVnew()
elif mode == 80006  : MOVnew2(url)
elif mode == 80007  : MOVnew3(url)
elif mode == 80008  : Search_Bolly()
elif mode == 80009  : LOVERS()
elif mode == 80010  : LOVERS2(url)
elif mode == 80011  : LOVERS3(url)
elif mode == 80012  : searchLOVERS()
elif mode == 90000  : addCONTEXT(name,url)
elif mode == 90001  : tools()
elif mode == 90002  : streamcats()
elif mode == 90003  : Xperfect2(url)
elif mode == 90004  : Xperfect3(url)
elif mode == 90005  : Xperfectplayer(url)
elif mode == 90006  : XXXHD2(url)
elif mode == 90007  : XXXHD3(url)
elif mode == 90008  : wetsex2(url)
elif mode == 90009  : wetsex3(url)
elif mode == 90010  : tommyslist()
elif mode == 90020  : hellyeah()
elif mode == 90021  : hellyeah2(url)
elif mode == 90022  : hellyeah3(url)
elif mode == 90023  : catchuptv()
elif mode == 90024  : catchuptv1(url)
elif mode == 90025  : catchuptv2(url)

elif mode == 90026  : catchup2()
elif mode == 90027  : tvarchive(name,url,description)
elif mode == 90028  : stream_video(url)

elif mode == 900300  : Tgamesnew()
elif mode == 900301  : Treplaysnew(url)
elif mode == 900302  : Tplay(url)
elif mode == 90030  : Tgames()
elif mode == 90031  : Treplays()
elif mode == 90032  : Treplays2(url)
elif mode == 90033  : Treplays3(url)
elif mode == 90034  : Treplays4(url)
elif mode == 90035  : playFilmon(url)
elif mode == 90036  : BAMF(url)
elif mode == 90039  : BAMF2(url)
elif mode == 90037  : quicksilver(url)
elif mode == 900377  : quicksilver2(url)
elif mode == 90038  : Searchreap()

elif mode == 10090: Home_Menu_Episodes()
elif mode == 10091: A_Z_epi(url)
elif mode == 10092: A_Z_ser(url)
elif mode == 10093: A_Z_list(url,iconimage)
elif mode == 10094: A_Z_source(url,iconimage)

elif mode == 10095: RD1()
elif mode == 10096: RD2(url)
elif mode == 10097: RD3(url)
elif mode == 10098: RD4(url)
elif mode == 10099: RD5(url)

elif mode == 10200: RT1()
elif mode == 10201: RT2(name,url,description)
elif mode == 10202: RT3(url)
elif mode == 10203: RT4(url)

elif mode == 90040  : OMTmen()
elif mode == 90041  : OMTgenre(url)
elif mode == 90042  : OMTyear(url)
elif mode == 90043  : OMTlist(url)
elif mode == 90044  : OMTchoice(url)
elif mode == 90045  : OMTsearch()
elif mode == 90046  : OMTresolve(url)
elif mode == 90050  : OMTmentv()
elif mode == 90051  : OMTseason(url)
elif mode == 90052  : OMTepisode(url)
elif mode == 90053  : OMTtvlist(url)
elif mode == 90054  : OMTtvep(url)
elif mode == 90055  : OMTtvsearch()
#if mode == None     : Main_Menu()
elif mode == 100001 : Stand_up()
#elif mode == 100002: Search()
elif mode == 100003: Play_Stage(url)
elif mode == 100004: Regex_magic(url)
elif mode == 100005: Resolve(url)
elif mode == 100008: Search()
elif mode == 100007: grab_youtube_playlist(url)
elif mode == 100009: yt.PlayVideo(url)
elif mode == 100010: Regex_com(url)
elif mode == 100100: Grab_Season(iconimage,url,extra)
elif mode == 100101: Grab_Episode(url,name,fanart,extra,iconimage)
elif mode == 100102: Get_Sources(name,url,iconimage,fanart)
elif mode == 100106: Get_site_link(url,name)
elif mode == 100107: queueItem()
elif mode == 100108: random_list()
elif mode == 100109: get_random(url)
elif mode == 40000: VOD_Menu()
elif mode == 40001: Get_VOD_playlinks(url)
elif mode == 100110: TESTPICS(url)
elif mode == 100111: TESTPICS2(url)
elif mode == 100112: ADULTmeme(url)
elif mode == 100113: TESTPICS2original(url)
elif mode == 100114: HotNudeGirls(url)
elif mode == 100115: HotNudeGirls2(url)
elif mode == 100117: TeenNudeGirls(url)
elif mode == 100118: TeenNudeGirls2(url)
elif mode == 100120: MyNudeBabes(url)
elif mode == 1001200: MyNudeBabes2(url)
elif mode == 100210: GODS(url)
elif mode == 100211: guidemenu()
elif mode == 100212: pvrsetup()
elif mode == 100213: tvguide22()
elif mode == 100214: GetTiny()
elif mode==1000111:
    scrape_movie(url)
    
elif mode==1001111:
    Big_Resolve(name,url)
    
elif mode==1002111:
    movie_genre()
    
elif mode==1003111:
    scrape_movie_genre(url,name)
    
elif mode==1004111:
    scrape_year()
    
elif mode==1005111:
    scrape_movie_year(url,name)
elif mode == 1100: from imports.pyramid import pyramid;pyramid.SKindex();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1101000:from imports.pyramid import pyramid;pyramid.getData(url,fanart);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1102000:from imports.pyramid import pyramid;pyramid.getChannelItems(name,url,fanart);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1103000:from imports.pyramid import pyramid;pyramid.getSubChannelItems(name,url,fanart);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1104000:from imports.pyramid import pyramid;pyramid.getFavorites();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1105000:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    from imports.pyramid import pyramid;pyramid.addFavorite(name,url,iconimage,fanart,fav_mode)
elif mode==1106000:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    from imports.pyramid import pyramid;pyramid.rmFavorite(name)
elif mode==1107000:from imports.pyramid import pyramid;pyramid.addSource(url)
elif mode==1108000:from imports.pyramid import pyramid;pyramid.rmSource(name)
elif mode==1109000:from imports.pyramid import pyramid;pyramid.download_file(name, url)
elif mode==1110000:from imports.pyramid import pyramid;pyramid.getCommunitySources()
elif mode==1111000:from imports.pyramid import pyramid;pyramid.addSource(url)
elif mode==1112000:
    from imports.pyramid import pyramid
    if 'google' in url:
        import urlresolver
        resolved = urlresolver.resolve(url)
        item = xbmcgui.ListItem(path=resolved)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    elif not url.startswith("plugin://plugin") or not any(x in url for x in pyramid.g_ignoreSetResolved):#not url.startswith("plugin://plugin.video.f4mTester") :
        item = xbmcgui.ListItem(path=url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
    else:
        print 'Not setting setResolvedUrl'
        xbmc.executebuiltin('XBMC.RunPlugin('+url+')')
elif mode==1113000:from imports.pyramid import pyramid;pyramid.play_playlist(name, playlist)
elif mode==1114000:from imports.pyramid import pyramid;pyramid.get_xml_database(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1115000:from imports.pyramid import pyramid;pyramid.get_xml_database(url, True);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1116000:from imports.pyramid import pyramid;pyramid.getCommunitySources(True);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1117000:
    url,setresolved = getRegexParsed(regexs, url)
    if url:
        from imports.pyramid import pyramid;pyramid.playsetresolved(url,name,iconimage,setresolved)
    else:
        xbmc.executebuiltin("XBMC.Notification(ThePyramid ,Failed to extract regex. - "+"this"+",4000,"+icon+")")
elif mode==1118000:
    try:
        from imports.pyramid import youtubedl
    except Exception:
        xbmc.executebuiltin("XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000,"")")
    stream_url=youtubedl.single_YD(url)
    from imports.pyramid import pyramid;pyramid.playsetresolved(stream_url,name,iconimage)
elif mode==1119000:from imports.pyramid import pyramid;pyramid.playsetresolved (pyramid.urlsolver(url),name,iconimage,True)
elif mode==1121000:from imports.pyramid import pyramid;pyramid.ytdl_download('',name,'video')
elif mode==1123000:from imports.pyramid import pyramid;pyramid.ytdl_download(url,name,'video')
elif mode==1124000:from imports.pyramid import pyramid;pyramid.ytdl_download(url,name,'audio')
elif mode==1125000:from imports.pyramid import pyramid;pyramid.search(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==1126000:
    name = name.split(':')
    from imports.pyramid import pyramid;pyramid.search(url,search_term=name[1])
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1127000:
    from imports.pyramid import pyramid;pyramid.pulsarIMDB=search(url)
    xbmc.Player().play(pulsarIMDB)
elif mode == 1124: from imports.pyramid import pyramid;pyramid.Search_Raiz()
elif mode == 1125: from imports.pyramid import pyramid;pyramid.SKindex_Raiz();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1126: from imports.pyramid import pyramid;pyramid.Search_Thunder()
elif mode == 1127: from imports.pyramid import pyramid;pyramid.SKindex_thunderstruck();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1128: from imports.pyramid import pyramid;pyramid.SKindex_Joker();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1129: from imports.pyramid import pyramid;pyramid.SKindex_Oblivion();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1130000: from imports.pyramid import pyramid;pyramid.GetSublinks(name,url,iconimage,fanart)
elif mode == 1131000: from imports.pyramid import pyramid;pyramid.SKindex_Supremacy();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1132000: from imports.pyramid import pyramid;pyramid.SKindex_BAMF();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1133: from imports.pyramid import pyramid;pyramid.SKindex_Quicksilver();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1134: from imports.pyramid import pyramid;pyramid.SKindex_Silent();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1135000: from imports.pyramid import pyramid;pyramid.WizHDMenu(url,iconimage,fanart);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1136000: from imports.pyramid import pyramid;pyramid.Wiz_Get_url(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1137: from imports.pyramid import pyramid;pyramid.scrape();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1138: from imports.pyramid import pyramid;pyramid.scrape_link(name,url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1139: from imports.pyramid import pyramid;pyramid.SKindex_deliverance();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1140: from imports.pyramid import pyramid;pyramid.SearchChannels();pyramid.SetViewThumbnail();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1141: from imports.pyramid import pyramid;pyramid.Search_input(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1142000: from imports.pyramid import pyramid;pyramid.RESOLVE(url)
elif mode == 1143: from imports.pyramid import pyramid;pyramid.SKindex_TigensWorld();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1144000: from imports.pyramid import pyramid;pyramid.queueItem();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1145: from imports.pyramid import pyramid;pyramid.SKindex_Ultra();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1146: from imports.pyramid import pyramid;pyramid.SKindex_Fido();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1147: from imports.pyramid import pyramid;pyramid.SKindex_Rays();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1153000: from imports.pyramid import pyramid;pyramid.pluginquerybyJSON(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1154000: from imports.pyramid import pyramid;pyramid.get_random(url);xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode == 1156: from imports.pyramid import pyramid;pyramid.SKindex_Midnight();xbmcplugin.endOfDirectory(int(sys.argv[1]))
elif mode==9050000: ac247()
elif mode==9060000: Big_Resolve(name,url)
elif mode==9080000: actvshows()
elif mode==9070000: arcontv()
elif mode==9090000: actvmovies()
elif mode==9100000: actvcable()
elif mode==9110000: actvrand()
elif mode==9110001: show_main(url)
elif mode==9110002: get_eps(url,name,iconimage) 
elif mode==9110003: send_to_search2(name,extra)  
elif mode==9110005: movie_search(description,url)  
elif mode==9110004: nantvsearch()
elif mode==9110010: Random_Cartoon(url)
elif mode==9110011: twenty47_select()
elif mode==9110012: Random_Play_Cartoon(url,name)
elif mode==9110013: reg_nan(url) 
elif mode==9110014: send_to_movie_search_pyramid(name,url)
elif mode==9110015: nanmovsearch() 
elif mode==9999999: GALLERY()    
elif mode==19999999: AGALLERY()    
elif mode==1999990: TOTT()    
elif mode==21999990: COZY()    
elif mode==21999991: COZYfire1(url)    
elif mode==21999992: COZYfire2(url)    
elif mode==21999993: COZYsound1(url)    
elif mode==21999994: COZYsound2(url,iconimage)    
elif mode==21999995: COZYstorie(url)    
elif mode==21999996: COZYstorie1(url,iconimage)    
elif mode==21999997: COZYstorie2(url,iconimage)    
elif mode==21999998: COZYstorie3(name,url,iconimage)    
elif mode==219999989: DDNS_Log()    
elif mode==219999990: errorChecking(all=True)   
elif mode==219999991: clearlogfiles()   
elif mode==219999992: clearThumbs()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
