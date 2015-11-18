import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import urlresolver
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2,urllib, glob
import re
import extract
import downloader
import plugintools
import zipfile
import time
import ntpath
import cookielib
from urllib2 import urlopen
from cookielib import CookieJar
from addon.common.addon import Addon
from addon.common.net import Net
 

###THANK YOU TO THE PEOPLE THAT ORIGINALY WROTE SOME OF THIS CODE "STUART DENTON, PIPCAN, MIKEY1234, WHUFCLEE" TO NAME A FEW, WITHOUT YOU I STILL PROBABLY WOULDNT HAVE A CLUE WHERE TO START###


USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
addon_id = 'plugin.video.GenieTv'
EXCLUDES     = ['plugin.video.GenieTv','script.module.addon.common']
ADDON = xbmcaddon.Addon(id=addon_id)
MEDIA = xbmc.translatePath('special://home/media')
AddonID='plugin.video.GenieTv'
dp =  xbmcgui.DialogProgress()
AddonTitle="[COLORgreen]GenieTv[/COLOR]" 
net = Net()
MyBuild = ADDON.getSetting('Build')
MyLocal = ADDON.getSetting('Local')
U = ADDON.getSetting('User')
dialog = xbmcgui.Dialog()
HOME = xbmc.translatePath('special://home/')
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png',FANART,''))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
VERSION = "2.0.3"
DBPATH = xbmc.translatePath('special://database')
TNPATH = xbmc.translatePath('special://thumbnails');
PATH = "GenieTv"            
BASEURL = "http://architects.x10host.com"
H = 'http://'
localizedString = ADDON.getLocalizedString
cookieJar = CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
urlOpener.addheaders = [('User-Agent', 'Mozilla/5.0')]

def INDEX():
    addDir('[COLORgreen]MY BUILD[/COLOR]',BASEURL,49,ART+'MB.png',FANART,'')
    addDir('[COLORgreen]WISHES PC[/COLOR]',BASEURL,1,ART+'WISHESPC.png',FANART,'')
    addDir('[COLORgreen]WISHES ANDROID[/COLOR]',BASEURL,44,ART+'WISHESAN.png',FANART,'')
    addDir('[COLORgreen]GenieTv STREAMS[/COLOR]',BASEURL,1008,ART+'streams.png',FANART,'')
    addDir('[COLORgreen]GenieTv ANIME --PLEASE USE PLAYER 3 WHILE WE ATTEMPT TO CORRECT THE ISSUE--[/COLOR]',BASEURL,1001,ART+'anime.png',FANART,'PLEASE USE PLAYER 3 WHILE WE ATTEMPT TO CORRECT THE ISSUE')
    addDir('[COLORgreen]GenieTv VOD[/COLOR]',BASEURL,1005,ART+'VOD.png',FANART,'')
    addDir2('[COLORgreen]SOURCE LIST[/COLOR]',BASEURL,46,ART+'TUTS.png',FANART,'')
    addDir('[COLORgreen]WIPE GENIE[/COLOR]',BASEURL,41,ART+'wipegenie.png',FANART,'')
    addDir('[COLORgreen]GenieTv RSS Feed[/COLOR]',BASEURL,39,ART+'RSS.png',FANART,'')
    addDir('[COLORgreen]APK TOOL[/COLOR]',BASEURL,2,ART+'APK.png',FANART,'')
    addDir('[COLORgreen]ADDONS[/COLOR]',BASEURL,21,ART+'ADDONS.png',FANART,'')
    addDir('[COLORgreen]ADDONS PACKS[/COLOR]',BASEURL,30,ART+'ADDONP.png',FANART,'')
    addDir('[COLORgreen]URL FIXES[/COLOR]',BASEURL,20,ART+'URLFIX.png',FANART,'')
    addDir('[COLORgreen]BUILDERS TOOLBOX[/COLOR]',BASEURL,32,ART+'builderstoolbox.png',FANART,'')
    addDir('[COLORgreen]MAINTENANCE[/COLOR]',BASEURL,3,ART+'MAIN6.png',FANART,'')
    addDir('[COLORgreen]ADVANCED SETTINGS XML[/COLOR]',BASEURL,4,ART+'XML.png',FANART,'')
    setView('movies', 'MAIN')

def MAINTENANCE():
    addDir2('DELETE CACHE','url',14,ART+'MAIN5.png',FANART,'')
    addDir2('DELETE PACKAGES','url',6,ART+'MAIN4.png',FANART,'')
    addDir2('FORCE REFRESH','url',10,ART+'MAIN3.png',FANART,'Force Refresh All Repos')
#    addDir('LAST RESORT FIX EMPTY REPOS','url',9,ART+'1.jpg',FANART,'Fix Corrupt Database')
    addDir2('CHECK MY IP','url',12,ART+'MAIN2.png',FANART,'')
    addDir2('ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER','url',13,ART+'MAIN1.png',FANART,'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db')
    setView('movies', 'MAIN')


def ADDONS():
    addDir('[COLORgreen]REPOS[/COLOR]',BASEURL,31,ART+'repos.png',FANART,'')
    addDir('[COLORgreen]NEW[/COLOR]',BASEURL,22,ART+'NEW.png',FANART,'')
    addDir('[COLORgreen]IPTV[/COLOR]',BASEURL,23,ART+'IPTV.png',FANART,'')
    addDir('[COLORgreen]VIDEO[/COLOR]',BASEURL,24,ART+'VIDEO.png',FANART,'')
    addDir('[COLORgreen]SPORTS[/COLOR]',BASEURL,25,ART+'SPORTS.png',FANART,'')
    addDir('[COLORgreen]KIDS[/COLOR]',BASEURL,26,ART+'KIDS.png',FANART,'')
    addDir('[COLORgreen]MUSIC[/COLOR]',BASEURL,27,ART+'MUSIC.png',FANART,'')
    addDir('[COLORgreen]PROGRAMS[/COLOR]',BASEURL,28,ART+'PROGRAMS.png',FANART,'')
    addDir('[COLORgreen]XXX[/COLOR]','URL',29,ART+'XXX.png',FANART,'')
    setView('movies', 'MAIN')


def ADVANCEDXML():
    addDir2('CHECK ADVANCED XML',BASEURL,8,ART+'XML.png',FANART,'')
    addDir2('MUCKYS XML',BASEURL+'/wizard/muckys.xml',7,ART+'XML.png',FANART,'')
    addDir2('0CACHE XML',BASEURL+'/wizard/0cache.xml',7,ART+'XML.png',FANART,'')
    addDir2('MIKEY1234 XML',BASEURL+'/wizard/mikey.xml',7,ART+'XML.png',FANART,'')
    addDir2('TUXENS XML',BASEURL+'/wizard/tuxens.xml',7,ART+'XML.png',FANART,'')
    addDir2('P2P RECOMMENDED XML1',BASEURL+'/wizard/p2p1.xml',7,ART+'XML.png',FANART,'')
    addDir2('P2P RECOMMENDED XML2',BASEURL+'/wizard/p2p2.xml',7,ART+'XML.png',FANART,'')
    addDir2('DELETE XML',BASEURL,11,ART+'XML.png',FANART,'')
    setView('movies', 'MAIN')
	
def RES():
    addDir2('[COLORgreen]My Local Zip[/COLOR]',MyLocal,48,ART+'MB.png',FANART,'')
    addDir2('[COLORgreen]My Online Zip[/COLOR]',MyBuild,43,ART+'MB.png',FANART,'')

def CUSTOMFTV():
    addDir2('INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED',BASEURL+'/wizard/customftv/ftvguide-addons.zip',5,ART+'FTV4.png',FANART,'')
    addDir2('FTV GUIDE FIRST RUN SETTINGS',BASEURL+'/wizard/customftv/settings.xml',17,ART+'FTV3.png',FANART,'')
    addDir2('FTV GUIDE ADDONS2.INI UPDATE DAILY','http://ren.byethost12.com/addons2.ini',16,ART+'FTV1.png',FANART,'')
    addDir2('RESET FTV DATABASE','url',18,ART+'FTV2.png',FANART,'')
    


def BUILD():
    addDir('[COLORgreen]SKINS[/COLOR]',BASEURL,33,ART+'skinp.png',FANART,'')
    addDir('[COLORgreen]ARTWORK PACKS[/COLOR]',BASEURL,34,ART+'artp.png',FANART,'')
    addDir('[COLORgreen]CREATE UNIVERSAL PATHS[/COLOR]',HOME,35,ART+'GUI.png',FANART,'')
    setView('movies', 'MAIN')

def URLFIX(url):
    link = OPEN_URL(F).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def SKINS():
    addDir('[COLORgreen]GOTHAM SKINS[/COLOR]',BASEURL,36,ART+'GSKIN.png',FANART,'')
    addDir('[COLORgreen]HELIX SKINS[/COLOR]',BASEURL,37,ART+'HSKIN.png',FANART,'')
    addDir('[COLORgreen]ISENGAARD SKINS[/COLOR]',HOME,38,ART+'ISKIN.png',FANART,'')
    setView('movies', 'MAIN')
    
def GSKIN(url):
    link = OPEN_URL(BASEURL+V).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def HSKIN(url):
    link = OPEN_URL(BASEURL+W).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def ISKIN(url):
    link = OPEN_URL(BASEURL+X).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def ARTWORK(url):
    link = OPEN_URL(BASEURL+R).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,40,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def ADDONSP(url):
    link = OPEN_URL(BASEURL+P).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,5,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def APK(url):
    link = OPEN_URL(C).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,19,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def APKTOOL(name,url,description):
    path = xbmc.translatePath(os.path.join(A,'Download'))
    dp = xbmcgui.DialogProgress()
    dp.create("Your App Is Downloading","Why not check out our website",'', 'Http://architects.x10host.com')
    lib=os.path.join(path, name+'.apk')
    try:
       os.remove(lib)
    except:
       pass
    downloader.download(url, lib, dp)
    dialog = xbmcgui.Dialog()
    dialog.ok("GenieTv", "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]","[COLORblue]Tool Brought To You By Architects@Work[/COLOR]")
    
    
def ARTTOOL(name,url,description):
    path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
    dp = xbmcgui.DialogProgress()
    dp.create("Your Art Pack Is Downloading","Why not check out our website",'', 'Http://architects.x10host.com')
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
    dialog = xbmcgui.Dialog()
    dialog.ok("GenieTv", "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]")


def WISHESPC(url):
    link = OPEN_URL(H+U+B).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,5,iconimage,fanart,description)
    try:
        link = OPEN_URL(N+U+T).replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        for name,url,iconimage,fanart,description in match:
            addDir(name,url,5,iconimage,fanart,description)
    except: pass
    setView('movies', 'INFO')


def WISHES(url):
    link = OPEN_URL(H+U+B).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
        addDir(name,url,43,iconimage,fanart,description)
    try:
        link = OPEN_URL(N+U+T).replace('\n','').replace('\r','')
        match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
        for name,url,iconimage,fanart,description in match:
            addDir(name,url,43,iconimage,fanart,description)
    except: pass
    setView('movies', 'INFO')


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
    dialog = xbmcgui.Dialog()
    dialog.ok("GenieTv", "Press ok to force close kodi, if unsuccessful please disconnect the power, if using windows Please kill kodi via taskmanager","[COLOR yellow]Brought To You By Architects@Work[/COLOR]")
    UPDATEREPO()


def WIZARD(name,url,description):
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
    dialog = xbmcgui.Dialog()
    dialog.ok("GenieTv", "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager","[COLOR yellow]Brought To You By Architects@Work[/COLOR]")
    killxbmc()

def WIZARDAN(name,url,description):
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
    dialog = xbmcgui.Dialog()
    dialog.ok("GenieTv", "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN","[COLOR yellow]Brought To You By Architects@Work[/COLOR]")
        

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
    dialog = xbmcgui.Dialog()
    dialog.ok("GenieTv", "Please Disconnect The Power From Your Device. DO NOT EXIT CLEANLY VIA SHUTDOWN","[COLOR yellow]Brought To You By Architects@Work[/COLOR]")
        

def killxbmc():
    choice = xbmcgui.Dialog().yesno('Force Close Kodi', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    if choice == 0:
        return
    elif choice == 1:
        pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        try: os.system('adb shell am force-stop org.xbmc.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass        
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "Your system has been detected as Android, you ", "[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Pulling the power cable is the simplest method to force close.")
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
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
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.","Your platform could not be detected so just pull the power cable.")    

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'


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
#---------------------------------------------------------------------------------------------------
def M3UCATS():
    html=OPEN_CAT(URL2)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1009,image)
		
def M3UPLAY(url):
    html=OPEN_CAT(url)
    match = re.compile('#EXTINF:-1,(.+?) (.+?) ').findall(html)
    for name,url in match:
        addDir4(name,url,222,ART+'streams.png')
#---------------------------------------------------------------------------------------------------
def TESTCATS2():
    html=OPEN_CAT(URL1)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1007,image)
def TESTCATS3(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1006,image)

def AddTVSHOWDir(name, url, mode, iconimage, description="", isFolder=True, background=None):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)

	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
	if background:
		liz.setProperty('fanart_image', background)
	if mode == 1 or mode == 2:
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10008).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=22)'.format(sys.argv[0], urllib.quote_plus(url)))])
	elif mode == 404:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
	elif mode == 556:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10010).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=33&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
		
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def Add_Directory_Item(handle, url, listitem, isFolder):

    xbmcplugin.addDirectoryItem(handle, url, listitem, isFolder) 

def ParseURL(url): 
    response = urlOpener.open(url).read()
        
    try:
        Titles = re.findall(r'<a .*?>(.*?)</a>',response)
        Links = re.findall(r'<a.*?href="(.*?)">',response)
            
        for link in Links:
            if '.gif' in link:
                pass
            elif '..' in link:
                pass
            elif '.txt' in link:
                pass
            elif '.png' in link:
                pass
            elif '?C=N;O=D' in link:
                pass
            elif '?C=M;O=A' in link:
                pass
            elif '?C=S;O=A' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif 'Torrent' in link:
                pass
            elif 'exe' in link:
                pass
            elif 'public' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif 'pub' in link:
                pass
            elif 'install' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif '?C=D;O=A' in link:
                pass
            elif 'mpeg' in link:
                pass
            else:
                name = link
                if 'txt' in name:
                    pass
                if 'HDTV' in name:
                    name = name.replace ('HDTV', '')
                if 'XviD-LOL' in name:
                    name = name.replace ('XviD-LOL', '')
                if 'x264-LOL' in name:
                    name = name.replace ('x264-LOL', '')
                if 'X264-DIMENSION' in name:
                    name = name.replace ('X264-DIMENSION', '')
                if 'Farsimovie' in name:
                    name = name.replace ('Farsimovie', '')
                if 'avi' in name:
                    name = name.replace ('avi', '')
                if 'mp4' in name:
                    name = name.replace ('mp4', '')
                if 'mkv' in name:
                    name = name.replace ('mkv', '')
                if '%20' in name:
                    name = name.replace ('%20', ' ')
                if '%5bVTV%5d' in name:
                    name = name.replace ('%5bVTV%5d', ' ')
                if 'DeeJayAhmed' in name:
                    name = name.replace ('DeeJayAhmed', '')
                if '-' in name:
                    name = name.replace ('-', '')
                if '1Ch' in name:
                    name = name.replace ('1Ch', '')
                if 'BluRay' in name:
                    name = name.replace ('BluRay', '')
                if 'ReEnc' in name:
                    name = name.replace ('ReEnc', '')
                if '/' in name:
                    name = name.replace('/', ' ')
                if 'Film2Movie_ORG' in name:
                    name = name.replace('Film2Movie_ORG', ' ')
                if 'Film2Movie_INFO' in name:
                    name = name.replace('Film2Movie_INFO', ' ')
                if 'x265' in name:
                    name = name.replace('x265', ' ')
                if 'HEVC' in name:
                    name = name.replace('HEVC', ' ')
                if '&amp;' in name:
                    name = name.replace('&amp;', ' ')
                if '%5b2007%5d' in name:
                    name = name.replace('%5b2007%5d', ' ')
                if '%5b2006%5d%5b' in name:
                    name = name.replace('%5b2006%5d%5b', ' ')
                if '%5b' in name:
                    name = name.replace('%5b', ' ')
                if '%5d' in name:
                    name = name.replace('%5d', ' ')
                if 'x264' in name:
                    name = name.replace('x264', ' ')
                if 'CHD' in name:
                    name = name.replace('CHD', ' ')
                if 'sample' in name:
                    name = name.replace('sample', ' ')
                if 'DVDSCR' in name:
                    name = name.replace('DVDSCR', ' ')
                if 'DVDRip' in name:
                    name = name.replace('DVDRip', ' ')
                if '%d0' in name:
                    name = name.replace('%d0', ' ')
                if '%92' in name:
                    name = name.replace('%92', ' ')
                if '%b3' in name:
                    name = name.replace('%b3', ' ')
                if '%d1' in name:
                    name = name.replace('%d1', ' ')
                if '%be' in name:
                    name = name.replace('%be', ' ')
                if '%81' in name:
                    name = name.replace('%81', ' ')
                if '%82' in name:
                    name = name.replace('%82', ' ')
                if '%8f' in name:
                    name = name.replace('%8f', ' ')
                if '%94' in name:
                    name = name.replace('%94', ' ')
                if '%83' in name:
                    name = name.replace('%83', ' ')
                if '%85' in name:
                    name = name.replace('%85', ' ')
                if '%93' in name:
                    name = name.replace('%93', ' ')
                if '%80' in name:
                    name = name.replace('%80', ' ')
                if '%b4' in name:
                    name = name.replace('%b4', ' ')
                if '%bd' in name:
                    name = name.replace('%bd', ' ')
                if '%b0' in name:
                    name = name.replace('%b0', ' ')
                if '%9e' in name:
                    name = name.replace('%9e', ' ')
                if '%8b' in name:
                    name = name.replace('%8b', ' ')
                if '%84' in name:
                    name = name.replace('%84', ' ')
                if '%b8' in name:
                    name = name.replace('%b8', ' ')
                if '%bb' in name:
                    name = name.replace('%bb', ' ')
                if '%86' in name:
                    name = name.replace('%86', ' ')
                if '%8c' in name:
                    name = name.replace('%8c', ' ')
                if '%b9' in name:
                    name = name.replace('%b9', ' ')
                if '%ba' in name:
                    name = name.replace('%ba', ' ')
                if '%9a' in name:
                    name = name.replace('%9a', ' ')
                if '%9d' in name:
                    name = name.replace('%9d', ' ')
                if '.' in name:
                    name = name.replace('.', ' ')
                if '2012' in name:
                    name = name.replace('2012', ' ')
                if 'mp3' in name:
                    name = name.replace('mp3', ' ')
                if '(' in name:
                    name = name.replace('(', ' ')
                if ')' in name:
                    name = name.replace(')', ' ')
                if 'DivX' in name:
                    name = name.replace('DivX', ' ')
                if 'Filmiha' in name:
                    name = name.replace('Filmiha', ' ')
                if 'com' in name:
                    name = name.replace('com', ' ')
                if 'filmiha' in name:
                    name = name.replace('filmiha', ' ')
                if 'XViD' in name:
                    name = name.replace('XViD', ' ')
                if 'WEB' in name:
                    name = name.replace('WEB', ' ')
                if 'AC3MAJESTIC' in name:
                    name = name.replace('AC3MAJESTIC', ' ')
                if 'anoXmous_' in name:
                    name = name.replace('anoXmous', ' ')
                if 'juggs' in name:
                    name = name.replace('juggs', ' ')
                if 'GECKOS' in name:
                    name = name.replace('GECKOS', ' ')
                if 'AMIABLE' in name:
                    name = name.replace('AMIABLE', ' ')
                if 'tuvideo' in name:
                    name = name.replace('tuvideo', ' ')
                if 'matiasmx' in name:
                    name = name.replace('matiasmx', ' ')
                if 'REMUX' in name:
                    name = name.replace('REMUX', ' ')
                if 'DTSHD' in name:
                    name = name.replace('DTSHD', ' ')
                if 'MA' in name:
                    name = name.replace('MA', ' ')
                if '1PublicHD' in name:
                    name = name.replace('1PublicHD', ' ')
                if 'AC3EVE' in name:
                    name = name.replace('AC3EVE', ' ')
                if 'LTRG' in name:
                    name = name.replace('LTRG', ' ')
                if 'FarsiMovie' in name:
                    name = name.replace('FarsiMovie', ' ')
                if 'Net' in name:
                    name = name.replace('Net', ' ')
                if '%' in name:
                    name = name.replace('%', ' ')
                if 'png' in name:
                    name = name.replace('png', ' ')
                if 'wmv' in name:
                    name = name.replace('wmv', ' ')

                if '.mkv' in link or '.mp3' in link or '.mp4' in link or '.avi' in link or '.flv' in link or '.mpeg' in link or '.3gp' in link or '.divx' in link:
                    AddTVSHOWDir(name, url+link, 404, ART+'VOD.png', 'GenieTv does not host or distribute any of the content displayed by this addon. GenieTV does not have any affiliation with the content provider.', isFolder=False)
					
                else:
					AddTVSHOWDir(name, url+link, 1006, '', '', isFolder=True)
                    

                

    except Exception, e:
                print str(e)        



def TestPlayUrl(name, url, iconimage=None):
	print '--- Playing "{0}". {1}'.format(name, url)
	listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
	listitem.setInfo(type="Video", infoLabels={ "Title": name })
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		

#################################
#######  GenieTv Streams ########
#################################
    
def TESTCATS():
    html=OPEN_CAT(URL3)
    match = re.compile('<td><a href="(.+?)">(.+)</a></td>').findall(html)
    for url,name in match:
        addDir3(name,url,1002,ART+'VOD.png')

def LISTS(url):
    html=OPEN_CAT(url)
    match = re.compile('&nbsp;<a href="(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(name,url,1003,ART+'VOD.png')
		
def LISTS2(url):
    html=OPEN_CAT(url)
    match = re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(html)
    for name,url in match:
        addDir3(name,url,1004,ART+'VOD.png')
		
def LISTS3(url):
    html=OPEN_CAT(url)
    match = re.compile("url: '(.+?)',").findall(html)
    for url in match:
        addDir4('STREAM',url,222,ART+'VOD.png')
		
        
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
        match=re.compile('"playlist">(.+?)</span></div><div><iframe src="(.+?)"').findall(link)
        for name,url in match:
                addDir4('%s'%(name).replace('GenieTv','[COLOR green]GenieTV[/COLOR]').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),222,ART+'VOD.png')
def RESOLVE(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('[COLORlime]Architects@Work[/COLOR]','Opening %s Now'%(name))
    if dp.iscanceled(): 
        print "[COLORred]STREAM CANCELLED[/COLOR]" # need to get this part working    
        dp.update(100)
        dp.close()
        dialog = xbmcgui.Dialog()
        if dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
	         return
    else:
        try: play.play(url)
        except: pass
        try: ADDON.resolve_url(url) 
        except: pass 

       
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
	  
def addDir3(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir4(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
              

#################################
####### POPUP TEXT BOXES ########
#################################

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

def SOURCES():
    TextBoxes('These are the main Sources you should get into you XBMC', '[COLORwhite]http://architects.x10host.com[/COLOR]--- [CR]  [COLORred]http://repo.sharktech.co.uk[/COLOR]--- [CR]   [COLORwhite]http://fusion.tvaddons.ag[/COLOR]--- [CR]  [COLORred]http://i.totalxbmc.tv[/COLOR]--- [CR]   [COLORwhite]http://www.xunitytalk.com/xfinity[/COLOR]--- [CR]  [COLORred]http://srp.nu[/COLOR]--- [CR]   [COLORwhite]http://solved.no-issue.ca[/COLOR]--- [CR]  [COLORred]http://xbmc.aminhacasadigital.com[/COLOR]--- [CR]   [COLORwhite]http://xbmc.movieshd.co[/COLOR]--- [CR]  [COLORred]http://install.kaosbox.tv[/COLOR]--- [CR]   [COLORwhite]http://kodi-repo.com/mxr[/COLOR]--- [CR]  [COLORred]http://kodi.metalkettle.co[/COLOR]--- [CR]   [COLORwhite]http://prozone.getxbmc.com[/COLOR]--- [CR]  [COLORred]http://transform.mega-tron.tv[/COLOR]--- [CR]   [COLORwhite]http://muckys.kodimediaportal.ml[/COLOR]--- [CR]  [COLORred]http://jas0npc.pcriot.com[/COLOR]--- [CR]  [COLORwhite]Sports devil source[/COLOR]--- [CR]  [COLORred]http://iwillfolo.com/iwf[/COLOR]')

################################
###    FIX REPOS&ADDONS      ###
################################

def UPDATEREPO():
    xbmc.executebuiltin( 'UpdateLocalAddons' )
    xbmc.executebuiltin( 'UpdateAddonRepos' )
    dialog = xbmcgui.Dialog()
    dialog.ok("GenieTv", '','                                 REFRESH SUCCESSFUL :)', "                          [COLOR gold]Brought To You By WIZARD HELPER[/COLOR]")
    return
    
#def FIXREPOSADDONS(url):
#    print '###'+AddonTitle+' - DELETING ADDONS16.DB ###'
#    path = xbmc.translatePath(os.path.join('special://database',''))
#    advance=os.path.join(path, 'addons16.db')
#    try:
#        os.remove(advance)
#        dialog = xbmcgui.Dialog()
#        print '=== GenieTv - DELETING    '+str(advance)+'    ==='
#        dialog.ok(AddonTitle, "       Remove Addona16.db Sucessfull Please Reboot To Take Affect")
#    except:
#        dialog = xbmcgui.Dialog()
#        dialog.ok(AddonTitle, "       No File To Remove")
#    return

################################
###    End FIX REPOS&ADDONS  ###
################################


################################
###          ADDONS          ###
################################

def NEW(url):
    link = OPEN_URL(BASEURL+D).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def IPTV(url):
    link = OPEN_URL(BASEURL+E).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def VIDEO(url):
    link = OPEN_URL(BASEURL+G).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def SPORTS(url):
    link = OPEN_URL(BASEURL+I).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def KIDS(url):
    link = OPEN_URL(BASEURL+J).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def MUSIC(url):
    link = OPEN_URL(BASEURL+K).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def PROGRAMS(url):
    link = OPEN_URL(BASEURL+L).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def XXX(url):
    link = OPEN_URL(BASEURL+M).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def REPOS(url):
    link = OPEN_URL(BASEURL+O).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
    setView('movies', 'MAIN')
    
def RSS(url):
    link = OPEN_URL(BASEURL+Y).replace('\n','').replace('\r','')
    match = re.compile('name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
    for name,url,iconimage,fanart,description in match:
            addDir(name,url,42,iconimage,fanart,description)
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
            dialog = xbmcgui.Dialog()
            if dialog.yesno("Delete Thumbnails", "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]", "This feature deletes your thumbnail folder and textures13.db", "Are you sure you want to do proceed? This Can NOT Be Undone"):
                for root, dirs, files in os.walk(TNPATH):
                    file_count = 0
                    file_count += len(files)
                    if file_count > 0:                
                        for f in files:
                            os.unlink(os.path.join(root, f))               
        text13 = os.path.join(DBPATH,"Textures13.db")               
        os.unlink(text13)
        dialog.ok("Restart KODI", "Please restart KODI to rebuild thumbnail library")
    except: 
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "Error Deleting Thumbnails please visit WIZARD HELPER on facebook")
    return

################################
###     END DELETE THUMBS    ###
################################

################################
###       DELETE CACHE       ###
################################

def DELETECACHE(url):
    print '############################################################       DELETING STANDARD CACHE             ###############################################################'
    xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
    if os.path.exists(xbmc_cache_path)==True:    
        for root, dirs, files in os.walk(xbmc_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete KODI Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        try:
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
        
        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'Other'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
        
        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'LocalAndRental'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
              # Set path to Cydia Archives cache files
                             

    # Set path to What th Furk cache files
    wtf_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.whatthefurk/cache'), '')
    if os.path.exists(wtf_cache_path)==True:    
        for root, dirs, files in os.walk(wtf_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete WTF Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
                
                # Set path to 4oD cache files
    channel4_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.4od/cache'), '')
    if os.path.exists(channel4_cache_path)==True:    
        for root, dirs, files in os.walk(channel4_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete 4oD Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
                
                # Set path to BBC iPlayer cache files
    iplayer_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache'), '')
    if os.path.exists(iplayer_cache_path)==True:    
        for root, dirs, files in os.walk(iplayer_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete BBC iPlayer Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
                
                
                # Set path to Simple Downloader cache files
    downloader_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/script.module.simple.downloader'), '')
    if os.path.exists(downloader_cache_path)==True:    
        for root, dirs, files in os.walk(downloader_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Simple Downloader Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
                
                # Set path to ITV cache files
    itv_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.itv/Images'), '')
    if os.path.exists(itv_cache_path)==True:    
        for root, dirs, files in os.walk(itv_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ITV Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass

                # Set path to movies4me cache files
    m4me_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.movies4me/cache'), '')
    if os.path.exists(itv_cache_path)==True:    
        for root, dirs, files in os.walk(m4me_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Movies4me Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass

                    # Set path to phoenix cache files
    phoenix_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.phstreams/Cache'), '')
    if os.path.exists(itv_cache_path)==True:    
        for root, dirs, files in os.walk(phoenix_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Phoenix Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass

                    # Set path to youtube music cache files
    ytmusic_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.spotitube/cache'), '')
    if os.path.exists(itv_cache_path)==True:    
        for root, dirs, files in os.walk(ytmusic_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete YouTube Music Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass

                    # Set path to supercartoons cache files
    supercartoons_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.supercartoons/cache'), '')
    if os.path.exists(itv_cache_path)==True:    
        for root, dirs, files in os.walk(supercartoons_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete SuperCartoons Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass

                    # Set path to tvonline.cc cache files
    tvonline_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.tvonline.cc/cache'), '')
    if os.path.exists(itv_cache_path)==True:    
        for root, dirs, files in os.walk(tvonline_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete TVonline Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass

                    # Set path to youtube cache files
    youtube_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.youtube/kodion'), '')
    if os.path.exists(itv_cache_path)==True:    
        for root, dirs, files in os.walk(youtube_cache_path):
            file_count = 0
            file_count += len(files)
        
        # Count files and give option to delete
            if file_count > 0:
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete YouTube Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass

                    # Set path to genesis cache files
    
    genesis_cache_path = xbmc.translatePath('special://masterprofile/addon_data/plugin.video.genesis')
    dialog = xbmcgui.Dialog()
    try:
        if dialog.yesno("Delete Genesis Cache Files", "Do you want to delete cache"):
            genesiscache = os.path.join(genesis_cache_path,"cache.db")
            os.unlink(genesiscache)

    except:
        pass
    
    dialog = xbmcgui.Dialog()
    dialog.ok("GenieTv", "                               Finished Deleting Cache ", "                          [COLOR gold]Brought To You By GenieTv[/COLOR]")

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
    
                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete Package Cache Files", str(file_count) + " files found", "Do you want to delete them?"):
                            
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                    dialog = xbmcgui.Dialog()
                    dialog.ok(AddonTitle, "       Deleting Packages all done")
                else:
                        pass
            else:
                dialog = xbmcgui.Dialog()
                dialog.ok(AddonTitle, "       No Packages to DELETE")
    except: 
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "Error Deleting Packages please visit WIZARD HELPER on facebook")
    return

################################
###    End DELETE PACKAGES   ###
################################

################################
###       Advanced XML       ###
################################ 
    
def AXML(url,name):
    path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    dialog = xbmcgui.Dialog()
    bak=os.path.join(path, 'advancedsettings.xml.bak')
    if os.path.exists(bak)==False: 
        if dialog.yesno("Back Up Original", 'Have You Backed Up Your Original?','', "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]"):
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
            dialog = xbmcgui.Dialog()
            dialog.ok(AddonTitle, "       Done Adding new Advanced XML")
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
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "       Done Adding new Advanced XML")    
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
    dialog = xbmcgui.Dialog()
    dialog.ok(AddonTitle,"[COLOR yellow]YOU HAVE[/COLOR] "+ name+"[COLOR yellow] XML SETTINGS SETUP[/COLOR]")
    return

def DELETEADVANCEDXML(url):
    print '###'+AddonTitle+' - DELETING ADVANCE XML###'
    path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    try:
        os.remove(advance)
        dialog = xbmcgui.Dialog()
        print '=== GenieTv - DELETING    '+str(advance)+'    ==='
        dialog.ok(AddonTitle, "       Remove Advanced Settings Sucessfull")
    except:
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "       No Advanced Settings To Remove")
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
        if inc <2: dialog=xbmcgui.Dialog(); dialog.ok('Check My IP',"[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ip, '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % country, '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % isp)
        inc=inc+1

#################################
###      END CHECK IP         ###
#################################

#################################
###       CUSTOM FTV          ###
#################################

def CUSTOMINI(url,name):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("GenieTv", '                                    Install Latest .ini File'):
        print '###'+AddonTitle+' - CUSTOM FTV INI###'
        path = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/script.ftvguide',''))
        advance=os.path.join(path, 'addons2.ini')
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== GenieTv - WRITING NEW    '+str(advance)+'    ==='
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "                               Done Adding New .ini File")  
    return

def CUSTOMSET(url,name):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("GenieTv", '                               Install Custom Settings'):
        print '###'+AddonTitle+' - CUSTOM FTV SETTINGS###'
        path = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/script.ftvguide',''))
        advance=os.path.join(path, 'settings.xml')
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== GenieTv - WRITING NEW    '+str(advance)+'    ==='
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "                               Done Adding New Settings")  
    return


def DELETEFTVDB():
    try:
        ftvpath = xbmc.translatePath(os.path.join('special://masterprofile/addon_data/script.ftvguide',''))
        if os.path.exists(ftvpath)==True:
            dialog = xbmcgui.Dialog()
            if dialog.yesno("GenieTv", "                               Delete FTV Guide Database"):
                ftvsource = os.path.join(ftvpath,"source.db")               
                os.unlink(ftvsource)               
        dialog.ok("GenieTv", "                                     FTV Database Reset")
    except: 
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "               Error Deleting Database No Database To Delete")
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
    plugintools.log("freshstart.main_list "+repr(params)); yes_pressed=plugintools.message_yes_no(AddonTitle,"Do you wish to restore your","Kodi configuration to default settings?")
    if yes_pressed:
        addonPath=xbmcaddon.Addon(id=AddonID).getAddonInfo('path'); addonPath=xbmc.translatePath(addonPath); 
        xbmcPath=os.path.join(addonPath,"..",".."); xbmcPath=os.path.abspath(xbmcPath); plugintools.log("freshstart.main_list xbmcPath="+xbmcPath); failed=False
        try:
            for root, dirs, files in os.walk(xbmcPath,topdown=True):
                dirs[:] = [d for d in dirs if d not in EXCLUDES]
                for name in files:
                    try: os.remove(os.path.join(root,name))
                    except:
                        if name not in ["Addons15.db","MyVideos75.db","Textures13.db","xbmc.log"]: failed=True
                        plugintools.log("Error removing "+root+" "+name)
                for name in dirs:
                    try: os.rmdir(os.path.join(root,name))
                    except:
                        if name not in ["Database","userdata"]: failed=True
                        plugintools.log("Error removing "+root+" "+name)
            if not failed: plugintools.log("freshstart.main_list All user files removed, you now have a clean install"); plugintools.message(AddonTitle,"The process is complete, you're now back to a fresh Kodi configuration with GenieTv!","Please reboot your system or restart Kodi in order for the changes to be applied.")
            else: plugintools.log("freshstart.main_list User files partially removed"); plugintools.message(AddonTitle,"The process is complete, you're now back to a fresh Kodi configuration with GenieTv","Please reboot your system or restart Kodi in order for the changes to be applied.")
        except: plugintools.message(AddonTitle,"Problem found","Your settings has not been changed"); import traceback; plugintools.log(traceback.format_exc()); plugintools.log("freshstart.main_list NOT removed")
        plugintools.add_item(action="",title="Now Exit Kodi",folder=False)
    else: plugintools.message(AddonTitle,"Your settings","has not been changed"); plugintools.add_item(action="",title="Done",folder=False)
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

N = base64.decodestring('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v')
A = base64.decodestring('L3N0b3JhZ2UvZW11bGF0ZWQvMA==')
T = base64.decodestring('L2dlbmllLnR4dA==')
B = base64.decodestring('LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=')
F = base64.decodestring('aHR0cDovL2ZpeGVzLmFyY2hpdGVjdHMueDEwaG9zdC5jb20vZml4ZXMudHh0')
C = base64.decodestring('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBwcy9hcHBzLnhtbA==')
D = base64.decodestring('L2FkZG9ucy9uZXcudHh0')
NVOD = base64.decodestring('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3ZvZC5waHA=')
URL1 = base64.decodestring('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==')
URL2 = base64.decodestring('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvbTN1LnBocA==')
URL3 = base64.decodestring('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=')
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
def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==5 :
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir2(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

                      
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None


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
        
        
if mode==None or url==None or len(url)<1:
        INDEX()

elif mode==1:
        WISHESPC(url)

elif mode==44:
        WISHES(url)

elif mode==2:
        APK(url)

elif mode==3:
        MAINTENANCE()

elif mode==21:
        ADDONS()

elif mode==4:
        ADVANCEDXML()

elif mode==5:
        WIZARD(name,url,description)

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
        IPCHECK()

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
        APKTOOL(name,url,description)

elif mode==40:
        ARTTOOL(name,url,description)

elif mode==42:
        ADDSKIN(name,url,description)

elif mode==43:
        WIZARDAN(name,url,description)

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
       
elif mode==222:
        RESOLVE(url)

elif mode==333:
        Live_VOD(url)


elif mode==1001:
        TESTCATS()

elif mode==1005:
        TESTCATS2()

elif mode==1007:
        TESTCATS3(url)

elif mode==1006:
        ParseURL(url)

elif mode==1002:
        LISTS(url)

elif mode==1003:
        LISTS2(url)
        
elif mode==1004:
        LISTS3(url)
        
elif mode==1008:
        M3UCATS()
        
elif mode==1009:
        M3UPLAY(url)
        
elif mode == 404: 
        TestPlayUrl(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
