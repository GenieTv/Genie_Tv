import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,base64,sys,xbmcvfs
import urlresolver
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2,urllib, glob, traceback
import re
import extract
import downloader
import plugintools
import zipfile
import time
import ntpath
import cookielib
import Parse, CNF_Studio_Indexer
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup, BeautifulSOAP
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
Decode = base64.decodestring
MyBuild = ADDON.getSetting('Build')
MyLocal = ADDON.getSetting('Local')
RemoteM3u = ADDON.getSetting('Remote')
LocalM3u = ADDON.getSetting('LocalM3u')
U = ADDON.getSetting('User')
dialog = xbmcgui.Dialog()
HOME = xbmc.translatePath('special://home/')
FANART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png',FANART,''))
ART = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
VERSION = "2.0.8"
DBPATH = xbmc.translatePath('special://database')
TNPATH = xbmc.translatePath('special://thumbnails');
PATH = "GenieTv"            
BASEURL = "http://architects.x10host.com"
H = 'http://'
localizedString = ADDON.getLocalizedString
cookieJar = CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
urlOpener.addheaders = [('User-Agent', 'Mozilla/5.0')]
addon_handle = int(sys.argv[1])

def INDEX():
    addDir('[COLORgreen]WIZARD[/COLOR]',BASEURL,4001,ART+'MB.png',FANART,'')
    addDir('[COLORgreen]STREAMS[/COLOR]',BASEURL,4002,ART+'streams.png',FANART,'')
    addDir('[COLORgreen]MUSIC[/COLOR]',BASEURL,4003,ART+'MUSIC.png',FANART,'')
    addDir('[COLORgreen]KODI FX SKINS[/COLOR]',BASEURL,8030,ART+'FX.png',FANART,'')
    addDir('[COLORgreen]BUILDERS TOOLBOX[/COLOR]',BASEURL,32,ART+'builderstoolbox.png',FANART,'')
    addDir('[COLORgreen]SOURCE LIST[/COLOR]',BASEURL,46,ART+'sources.png',FANART,'')
    addDir('[COLORgreen]MAINTENANCE[/COLOR]',BASEURL,3,ART+'MAIN6.png',FANART,'')
    addDir('[COLORgreen]GenieTv RSS Feed[/COLOR]',BASEURL,39,ART+'RSS.png',FANART,'')
    addDir('[COLORgreen]APK TOOL[/COLOR]',BASEURL,2,ART+'APK.png',FANART,'')
    addDir('[COLORgreen]ADDONS[/COLOR]',(Decode('aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv')),2030,ART+'ADDONS.png',FANART,'')
    addDir('[COLORgreen]ADDONS PACKS[/COLOR]',BASEURL,30,ART+'ADDONP.png',FANART,'')
    setView('movies', 'MAIN')

def MenWish():
    addDir('[COLORgreen]RESTORE MY BUILD[/COLOR]',BASEURL,49,ART+'MB.png',FANART,'')
    addDir('[COLORgreen]WIPE GENIE[/COLOR]',BASEURL,41,ART+'wipegenie.png',FANART,'')
    addDir('[COLORgreen]WISHES PC[/COLOR]',BASEURL,1,ART+'WISHESPC.png',FANART,'')
    addDir('[COLORgreen]WISHES ANDROID[/COLOR]',BASEURL,44,ART+'WISHESAN.png',FANART,'')
    setView('movies', 'MAIN')
def MenStream():
#    addDir('[COLORgreen]DOCUMENTARIES[/COLOR]',BASEURL,8040,ART+'soaps.png',FANART,'')
    addDir('[COLORgreen]Soaps Catch Up[/COLOR]',BASEURL,8000,ART+'soaps.png',FANART,'')
    addDir('[COLORgreen]GenieTv SCRAPED LIVE TV[/COLOR]',BASEURL,7030,ART+'origin.png',FANART,'')
#    addDir('[COLORgreen]GenieTv SCRAPED TV VOD[/COLOR]',BASEURL,7001,ART+'VOD.png',FANART,'')
    addDir('[COLORgreen]SCRAPED MOVIES VOD[/COLOR]',BASEURL,7018,ART+'MOVIESv.png',FANART,'')
    addDir('[COLORgreen]GenieTv VOD[/COLOR]',BASEURL,1005,ART+'VOD.png',FANART,'')
    addDir('[COLORgreen]GenieTv STREAMS[/COLOR]',BASEURL,1008,ART+'streams.png',FANART,'')
    addDir('[COLORgreen]THE REAPER[/COLOR]',BASEURL,1016,ART+'reap.png',FANART,'')
    addDir('[COLORgreen]SCOOBY STREAMS[/COLOR]',BASEURL,1026,ART+'scoob.png',FANART,'')
    addDir('[COLORgreen]GenieTv ANIME --PLEASE USE PLAYER 3 WHILE WE ATTEMPT TO CORRECT THE ISSUE--[/COLOR]',BASEURL,1001,ART+'anime.png',FANART,'PLEASE USE PLAYER 3 WHILE WE ATTEMPT TO CORRECT THE ISSUE')
    addDir('[COLORgreen]PLAYLIST LOADER[/COLOR]',BASEURL,3000,ART+'loader.png',FANART,'')
#    addDir('[COLORgreen]GenieTv EPG[/COLOR]',BASEURL,1014,ART+'VOD.png',FANART,'')
    setView('movies', 'MAIN')

def MenMusic():
    addDir('[COLORgreen]GenieTv RADIO[/COLOR]',BASEURL,1013,ART+'radio.png',FANART,'')
#    addDir('[COLORgreen]GenieTv MUSIC SCRAPE[/COLOR]',BASEURL,1010,ART+'VOD.png',FANART,'')
    setView('movies', 'MAIN')

def MAINTENANCE():
    addDir2('DELETE CACHE','url',14,ART+'MAIN5.png',FANART,'')
    addDir2('DELETE PACKAGES','url',6,ART+'MAIN4.png',FANART,'')
    addDir2('FORCE REFRESH','url',10,ART+'MAIN3.png',FANART,'Force Refresh All Repos')
#    addDir('LAST RESORT FIX EMPTY REPOS','url',9,ART+'1.jpg',FANART,'Fix Corrupt Database')
    addDir2('CHECK MY IP','url',12,ART+'MAIN2.png',FANART,'')
    addDir2('ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER','url',13,ART+'MAIN1.png',FANART,'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db')
    addDir('[COLORgreen]ADVANCED SETTINGS XML[/COLOR]',BASEURL,4,ART+'XML.png',FANART,'')
    addDir('[COLORgreen]URL FIXES[/COLOR]',BASEURL,20,ART+'URLFIX.png',FANART,'')
    setView('movies', 'MAIN')


def ADDONS():
    addDir('[COLORgreen]REPOS[/COLOR]',(Decode('aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv')),2030,ART+'repos.png',FANART,'')
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
      
def FXSKIN(url):
    link = OPEN_URL(Decode('aHR0cDovL2RsLmRyb3Bib3h1c2VyY29udGVudC5jb20vcy9kejYwd2FqMGhmcnV2aDgvQlVJTERTLnR4dD9kbD0w')).replace('\n','').replace('\r','')
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
    
def APK():
    html=OPEN_CAT(Decode('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vYXBrL2Fway5waHA='))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,2031,ART+'APK.png')
    
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
    link = OPEN_URL(Decode('aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==')).replace('\n','').replace('\r','')
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
    link = OPEN_URL(Decode('aHR0cDovL2dlbmlldHYuYXJjaGl0ZWN0cy54MTBob3N0LmNvbS90ZXN0L3doLnR4dA==')).replace('\n','').replace('\r','')
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
    dialog.ok("GenieTv", "Press ok to finish install","[COLOR yellow]Brought To You By Architects@Work[/COLOR]")
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
#------------------------------RADIO-----------------------------------------------------------------------
def RADIO():
    html=OPEN_CAT(Decode('aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw='))
    match = re.compile('<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="(.+?)">',re.DOTALL).findall(html)
    for name,url in match:
			    addDir4(name,url,222,ART+'radio.png')
#------------------------------DOCUMENTARIES---------------------------------------------------------------------#------------------------------RADIO-----------------------------------------------------------------------
def DOC1():
    html=OPEN_CAT(Decode('aHR0cDovL3RvcGRvY3VtZW50YXJ5ZmlsbXMuY29tLw=='))
    match = re.compile('<a href="(.+?)" >(.+?)</a></li><li>').findall(html)
    for url,name in match:
			    addDir3('[COLORgreen]'+name+'[/COLOR]',url,8041,ART+'radio.png')
def DOC2(url):
    html=OPEN_CAT(url)
    match = re.compile('<h2><a href="(.+?)" title="(.+?)">.+?</a></h2>.+?src="(.+?)"',re.DOTALL).findall(html)
    match2 = re.compile('class="inactive">.+?</a><a href="(.+?)">Next</a></div>',re.DOTALL).findall(html)
    for url,name,img in match:
			    addDir3('[COLORgreen]'+name+'[/COLOR]',url,8042,img)
    for url in match2:
			    addDir3('[COLORgreen]NEXT PAGE[/COLOR]',url,8041,ART+'radio.png')
def DOC3(url):
    html=OPEN_CAT(url)
    match = re.compile('<meta itemprop="name" content="(.+?)".+?<meta itemprop="thumbnailUrl" content="(.+?)".+?<meta itemprop="embedUrl" content="(.+?)".+?<meta itemprop="description" content="(.+?)" />',re.DOTALL).findall(html)
    for name,img,url,disc in match:
			    addDir2('[COLORgreen]'+name+'[/COLOR]',url.replace('https://www.youtube.com/embed/','http://youtube.com/watch?v='),222,img,'',disc)
#------------------------------EPG---------------------------------------------------------------------#------------------------------RADIO-----------------------------------------------------------------------
def EPG():
    html=OPEN_CAT(Decode('aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw=='))
    match = re.compile('<a href="(.+?)"  qt-title=".+?" qt-text=".+?<br> .+?" title="(.+?)".+?class=".+? src="(.+?)" alt=".+?" /></a>',re.DOTALL).findall(html)
    for url,name,img in match:
			    addDir4('[COLORgreen]'+name+'[/COLOR]',url,8002,img)
def EPG2(url):
    html=OPEN_CAT(url)
    match = re.compile('<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="(.+?)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>',re.DOTALL).findall(html)
    for img,time,url,name,disc in match:
			    addDir('%s %s'%('[COLORgreen]'+name+'[/COLOR]',time),url,1015,img,disc)
#------------------------------SOAPS------------------------------------------------------------------------
def Soap_TV():

    addDir3('Coronation Street','',8001,'')   
    addDir3('Eastenders','',8002,'')
    addDir3('Emmerdale','',8003,'')
    addDir3('Hollyoaks','',8004,'')
    addDir3('Im a Celebrity','',8005,'')



    
def Hollyoaks():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Holly' in name:
            img = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
            if 'huge' in url:
			    addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE_IGNORE_THE);

def Eastenders():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'East' in name:
            img = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
            if 'huge' in url:
    			addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def Emmerdale():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Emmer' in name:
            img = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
            if 'huge' in url:
                addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def CoronationStreet():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)".+?target=_blank>(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Coro' in name:
            img = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
            if 'huge' in url:
    			addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass

    xbmcplugin.addSortMethod(addon_handle, xbmcplugin.SORT_METHOD_TITLE);

def ImACeleb():
    HTML = OPEN_URL('http://uksoapshare.blogspot.co.uk/')
    match = re.compile('<a href="(.+?)" target="_blank">(.+?)</a>').findall(HTML)
    for url,name in match:
        if 'Celeb' in name:
            img = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
            if 'huge' in url:
    			addDir4((name).replace('.HDTV.x264-SS.mp4','').replace('_HDTV.x264','').replace('-SS.mp4','').replace('_720p.HDTV.x264.',' ').replace('_720p',''),url.replace('\\/','/'),8006,img)
            else:
                pass
				
def SOAPPLAYER(name,url):
        validate_URL = urlresolver.HostedMediaFile(url).valid_url()
        if validate_URL:
                resolved_URL = urlresolver.HostedMediaFile(url).resolve()
        else:
                html = open_url(url)
                url=re.compile('src="(.+?)"></iframe>').findall(html)[0]
                url=url.split('?autoplay')[0]
                html = open_url(url)
                resurl = re.compile('mp4","url":"(.+?)"').findall(html)[-1]
                resolved_URL=resurl.replace('\\/','/')
        liz = xbmcgui.ListItem(name,'','')
        liz.setPath(resolved_URL)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

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
    match = re.compile('"id":".+?","name":"(.+?)","img":"(.+?)","stream_url3":".+?","cat_id":"(.+?)","stream_url2":".+?","stream_url":".+?"}',re.DOTALL).findall(html)
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
    match = re.compile('"id":".+?","name":"'+Search_Name+'","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}',re.DOTALL).findall(html)
    match = re.compile('"id":".+?","name":"'+Search_Name+'","img":"(.+?)","stream_url3":"(.+?)","cat_id":".+?","stream_url2":"(.+?)","stream_url":"(.+?)"}',re.DOTALL).findall(html)
    for img,url,url2,url3 in match:
		Image = Decode ('aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv') + (img).replace('\\','')
		addDir4(Search_Name + ': Link 1',(url).replace('\\',''),222,Image)
		addDir4(Search_Name + ': Link 2',(url2).replace('\\',''),222,Image)
		addDir4(Search_Name + ': Link 3',(url3).replace('\\',''),222,Image)
		
#------------------------------SCRAPE---------------------------------------------------------------------
def cnfTV():
    html=OPEN_URL('http://tvshows.cnfstudio.com/')
    match = re.compile('<a href="http://tvshows.cnfstudio.com/genre/(.+?)">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3(name,'http://tvshows.cnfstudio.com/genre/' + url,7010,ART+'icon.png')
        print '>>>>>>>>>>' + url

def cnfTVCat(url):
    html=OPEN_URL(url)
    match = re.compile('<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>',re.DOTALL).findall(html)
    prev = re.compile("<link rel='prev' href='(.+?)'/>").findall(html)
    next = re.compile("<link rel='next' href='(.+?)'/>").findall(html)
    for img,url,name in match:
        addDir3((name).replace('&#038;','').replace('&#8216;','').replace('&#8217;','').replace('&#8211;',''),url,7011,img)
    prev=prev
    for url in prev:
        addDir3('Prev',url,7010,'')
    next=next
    for url in next:
        addDir3('Next',url,7010,'')

def cnfTVPlay(url):
    html=OPEN_URL(url)
    match = re.compile('<li>.+?<a href="(.+?)" target="_blank">.+?<span class="datex">(.+?)</span>.+?</b>(.+?)</span>.+?</li>',re.DOTALL).findall(html)
    for url,episode,name in match:
        addDir4(('Season') + episode + ('  ') + name,url,7004,ART+'icon.png')

def cnfTVPlay1(url):

    html=OPEN_URL(url)
    match = re.compile('<div id="play-1".+?src="(.+?)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>',re.DOTALL).findall(html)
    for url,name in match:
        addDir3(name,(url + '&fv=&sou=').replace('player','watch'),7000,ART+'icon.png')

def Get_Page(name, url, img):
    HTML = OPEN_URL(url)
    Page_Link = re.compile('<iframe class="playerframe" src="(.+?)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>',re.DOTALL).findall(HTML)
    No_PageLinks = len(Page_Link)
    
    
    if No_PageLinks == 1:
        for PageLink in Page_Link:
            PageLink = PageLink.replace('player','watch')
            Resolve_Link = PageLink + '&fv=&sou='
            Resolve_Page = OPEN_URL(Resolve_Link)
            Resolved = re.compile('<source src="(.+?)" type=".+?">',re.DOTALL).findall(Resolve_Page)
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
		
dialog = xbmcgui.Dialog()
		
		
def cnfCat(url):
    html=OPEN_URL(url)
    match = re.compile('<div class="movie">.+?<img src="(.+?)" alt=".+?" />.+?<a href="(.+?)"><span class="player"></span></a>.+?<h2>(.+?)</h2>',re.DOTALL).findall(html)
    prev = re.compile("<link rel='next' href='(.+?)'/>").findall(html)
    for img,url,name in match:
		addDir4((name).replace('&#038;','').replace('&#8216;','').replace('&#8217;','').replace('&#8211;',''),url,7004,img)
    prev=prev
    for url in prev:
		addDir3('Next Page',url,7003,'')

def cnfMovie(url):

    html=OPEN_URL(url)
    match = re.compile('<div id="play-1" class="player-content"><iframe class="playerframe" src="(.+?)" scrolling="no".+?</div>',re.DOTALL).findall(html)
    for url in match:
        link = url + '&fv=&sou='
        link = link.replace('player','watch')
        Play_URL = cnfPlay1(link)
        ResolvePlayURL = cnfPlay1(url)


def cnfPlay1(url):

    html=OPEN_URL(url)
    match = re.compile('<video id=".+?<source src="(.+?)" type="video/mp4">',re.DOTALL).findall(html)
    for url in match:
        RESOLVE(url,'')

#------------------------------PLAYLIST LOADER----------------------------------------------------------------
def LOADER():
    addDir('[COLORgreen]Local M3u[/COLOR]',LocalM3u,2001,ART+'loader.png',FANART,'')
    addDir('[COLORgreen]Remote M3u[/COLOR]',RemoteM3u,1009,ART+'loader.png',FANART,'')
	
def LocalM3UPLAY(url):
    match = re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall
    for var,name,url in match:
        addDir4(name,url,222,ART+'streams.png')

#------------------------------SCOOBY STREAMS---------------------------------------------------------------------
def SCOOBY():
    html=OPEN_CAT(Decode('aHR0cDovL3Njb29ieXN0cmVhbXMueDEwaG9zdC5jb20vc2Nvb2J5L3R2Y2F0cy5waHA='))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1027,image)
		
def SCOOBY2(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1028,image)
def SCOOBY3(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,333,image)
def SCOOBY4(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir4(name,url,404,image)
#------------------------------THE REAPER---------------------------------------------------------------------
def REAPER():
    html=OPEN_CAT(Decode('aHR0cDovL3RoZXJlYXBlci54MTBob3N0LmNvbS9UaGVfUmVhcGVycy9tYWluLnBocA=='))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1017,image)
		
def REAPER2(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1018,image)
def REAPER3(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,333,image)
def REAPER4(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir4(name,url,404,image)
#-----------------------------VOD----------------------------------------------------------------------
def TESTCATS2():
    html=OPEN_CAT(Decode('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA=='))
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3(name,url,1007,image)
def TESTCATS3(url):
    html=OPEN_CAT(url)
    match = re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(html)
    for url,image,name in match:
        addDir3('[COLORgreen]'+name+'[/COLOR]',url,1006,image)

def TestPlayUrl(name, url, iconimage=None):
	print '--- Playing "{0}". {1}'.format(name, url)
	listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
	listitem.setInfo(type="Video", infoLabels={ "Title": name })
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
		
#-----------------------------MUSIC-SCRAPE---------------------------------------------------------------------
def MUSIC1():
    html=OPEN_CAT(Decode('aHR0cDovL2ZyZWVtdXNpY2FyY2hpdmUub3JnLw=='))
    match = re.compile('<a href="(.+?)" style="background-color:.+?">(.+?)</a>').findall(html)
    for url,name in match:
        addDir3('[COLORgreen]'+name+'[/COLOR]',url,1011,ART+'streams.png')
def MUSIC2(url):
    html=OPEN_CAT(url)
    match = re.compile('<span class="ptxt-artist">\n.+?<b>\n.+?<a href=".+?">(.+?)</a>\n.+?</b>\n.+?</span>\n.+?<span class="ptxt-track"><a href=".+?"><b>"(.+?)"</b></a></span>\n.+?<span class="playicn">\n.+?<a href="(.+?)" class="icn-arrow" title="Download"></a>',re.DOTALL).findall(html)
    match2 = re.compile('.+?<a href="(.+?)">NEXT').findall(html)
    for artist,name,url in match:
        addDir4('%s %s'%('[COLORgold]'+artist+'[/COLOR]', '[COLORgreen]'+name+'[/COLOR]'),url,222,ART+'streams.png')
    match2=match2
    for url2 in match2:
        addDir3('[COLORgold]NEXT[/COLOR] [COLORgreen]PAGE[/COLOR]',url2,1011,ART+'streams.png')
def MUSIC3(url):
    html=OPEN_CAT(url)
    match = re.compile('<div class="full-poster">.+?<img src="(.+?)".+?title=.+?alt="Watch(.+?)Online" />.+?<div class="clear"></div>(.+?)..+?</div>.+?<iframe.+?scrolling="no" frameborder="0" src="(.+?)" allowFullScreen></iframe>',re.DOTALL).findall(html)
    for image,name,desc,url in match:
        addDir(name,url,222,'http://www.movietubenow.biz%s'%image,'',desc)

#################################
#######  GenieTv Streams ########
#################################
    
def TESTCATS():
    html=OPEN_CAT(Decode('aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24='))
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
        match=re.compile('<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /></a><br><b>(.+?)</b>').findall(link)
        for url,image,name in match:
                addDir4('%s'%(name).replace('GenieTv','[COLOR green]GenieTV[/COLOR]').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),222,image)
def RESOLVE(url,name): 
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
        RESOLVE(url,name)

elif mode==333:
        Live_VOD(url)


elif mode==1001:
        TESTCATS()

elif mode==1005:
        TESTCATS2()

elif mode==1007:
        TESTCATS3(url)

elif mode==1010:
        MUSIC1()

elif mode==1011:
        MUSIC2(url)

elif mode==1012:
        MUSIC3(url)

elif mode==1006:
        Parse.ParseURL(url)

elif mode==2030:
        Parse.addonParseURL(url)

elif mode==2031:
        Parse.apkParseURL(url)

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
        
elif mode==2001:
        LocalM3UPLAY(url)

elif mode==1013:
        RADIO()

elif mode==1014:
        EPG()

elif mode==1015:
        EPG2(url)

elif mode==1016:
        REAPER()

elif mode==1017:
        REAPER2(url)

elif mode==1018:
        REAPER3(url)

elif mode==1019:
        REAPER4(url)

elif mode==1026:
        SCOOBY()

elif mode==1027:
        SCOOBY2(url)

elif mode==1028:
        SCOOBY3(url)

elif mode==1029:
        SCOOBY4(url)

elif mode==4001:
        MenWish()

elif mode==4002:
        MenStream()

elif mode==4003:
        MenMusic()

elif mode==3000:
        LOADER()
       
elif mode == 404: 
        TestPlayUrl(name,url,iconimage)

elif mode == 7030:
        LiveTVFullCat()

elif mode == 7021:
        List_LiveTVFull(name)

elif mode == 7022:
        LiveTVFull(name)

elif mode == 7000:
		Get_Page(name, url, img)
		
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
elif mode == 8040:
		DOC1()
elif mode == 8041:
		DOC2(url)
elif mode == 8042:
		DOC3(url)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
