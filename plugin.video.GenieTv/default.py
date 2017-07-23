# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata , socket
import urlresolver
from imports import cloudflare , googleplus , client , cleantitle
from imports import yt
import xml . etree . ElementTree as ElementTree
import httplib
import liveresolver
import requests
import urlparse
import shutil
import binascii
import subprocess
import urllib2 , urllib , glob , traceback
import re
from imports import extract
from imports import downloader
import plugintools
import zipfile
import time
import ntpath
import cookielib
from imports import Parse , CNF_Studio_Indexer , speedtest , uservar , tools
try :
 import StorageServer
except :
 import storageserverdummy as StorageServer
oo000 = StorageServer . StorageServer ( "plugin.video.GenieTv" , 24 )
try :
 import json
except :
 import simplejson as json
from threading import Thread
from datetime import date , datetime , timedelta
from urllib2 import urlopen
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup , BeautifulSOAP
from cookielib import CookieJar
from addon . common . addon import Addon
from addon . common . net import Net
from imports . tvGuide import gui
import webbrowser
import SimpleDownloader
if 9 - 9: Ii . o0o00Oo0O - iI11I1II1I1I
if 71 - 71: ii
iIIii1IIi = ''
def o0OO00 ( i , t1 , t2 = [ ] ) :
 oo = iIIii1IIi
 for i1iII1IiiIiI1 in t1 :
  oo += chr ( i1iII1IiiIiI1 )
  i += 1
  if i > 1 :
   oo = oo [ : - 1 ]
   i = 0
 for i1iII1IiiIiI1 in t2 :
  oo += chr ( i1iII1IiiIiI1 )
  i += 1
  if i > 1 :
   oo = oo [ : - 1 ]
   i = 0
 return oo
 if 40 - 40: ooOoO0O00 * IIiIiII11i
 if 51 - 51: oOo0O0Ooo * I1ii11iIi11i
 if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = "3.5.7"
IiII = 'plugin.video.GenieTv'
iI1Ii11111iIi = xbmc . translatePath ( 'special://home/addons/repository.GenieTv' )
i1i1II = xbmc . translatePath ( 'special://home/addons/' )
O0oo0OO0 = xbmc . translatePath ( 'special://home/addonsbroke/' )
I1i1iiI1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
iiIIIII1i1iI = 'plugin.video.GenieTv'
o0oO0 = [ 'plugin.video.GenieTv' , 'script.module.addon.common' , 'repository.GenieTv' ]
oo00 = xbmcaddon . Addon ( id = iiIIIII1i1iI )
o00 = xbmc . translatePath ( 'special://home/media' )
Oo0oO0ooo = 'plugin.video.GenieTv'
o0oOoO00o = xbmcgui . DialogProgress ( )
i1 = '[COLORsteelblue]GenieTv[/COLOR]'
oOOoo00O0O = base64 . b64decode ( 'aHR0cDovL2dlbmlldHYuY28udWsvc3BlZWR0ZXN0LnR4dA==' )
i1111 = uservar . CONTACT
i11 = base64 . decodestring
I11 = xbmcaddon . Addon ( ) . setSetting
Oo0o0000o0o0 = ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIv' ) )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
oO0o0o0ooO0oO = os . path . join ( oOo0oooo00o , 'userdata' )
oo0o0O00 = os . path . join ( oO0o0o0ooO0oO , 'addon_data' , IiII )
oO = os . path . join ( oo0o0O00 , 'wizard.log' )
i1iiIIiiI111 = uservar . ADDONTITLE
oooOOOOO = xbmc . translatePath ( 'special://profile/' )
i1iiIII111ii = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
i1i1II = os . path . join ( oOo0oooo00o , 'addons' )
i1iIIi1 = os . path . join ( i1i1II , 'packages' )
ii11iIi1I = os . path . join ( i1i1II , 'HUB' )
iI111I11I1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYXBrLnR4dA==' ) )
OOooO0OOoo = Net ( )
iIii1 = xbmcgui . Dialog ( )
oOOoO0 = oo00 . getSetting ( 'Build' )
O0OoO000O0OO = oo00 . getSetting ( 'Local' )
iiI1IiI = oo00 . getSetting ( 'Remote' )
II = oo00 . getSetting ( 'LocalM3u' )
ooOoOoo0O = oo00 . getSetting ( 'TEXTCOL' )
OooO0 = oo00 . getSetting ( 'Downloads' )
II11iiii1Ii = xbmc . translatePath ( 'special://logpath/' )
OO0o = oo00 . getSetting ( 'User' )
Ooo = oo00 . getSetting ( 'Pass' )
O0o0Oo = oo00 . getSetting ( 'AdultPass' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
Oo00OOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'fanart.jpg' ) )
O0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'icon.png' ) )
O00o0OO = ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
I11i1 = xbmc . translatePath ( 'special://database' )
iIi1ii1I1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
o0 = xbmc . translatePath ( 'special://thumbnails' ) ;
I11II1i = "GenieTv"
IIIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
ooooooO0oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
IIiiiiiiIi1I1 = 'http://'
I1IIIii = datetime . now ( )
oOoOooOo0o0 = base64 . decodestring ( 'LnBocA==' )
OOOO = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
OOO00 = [ ]
iiiiiIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
O000OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
I11iii1Ii = oo00 . getLocalizedString
I1IIiiIiii = CookieJar ( )
O000oo0O = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( I1IIiiIiii ) )
O000oo0O . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
OOOOi11i1 = int ( sys . argv [ 1 ] )
IIIii1II1II = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
i1I1iI = os . path . join ( iIi1ii1I1 , 'favorites' )
oo0OooOOo0 = iIi1ii1I1 + '/addons.ini'
oO0o0o0ooO0oO = xbmc . translatePath ( 'special://home/userdata/' )
o0O = xbmc . translatePath ( 'special://home/userdatabroke/' )
O00oO = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
I11i1I1I = xbmc . translatePath ( 'special://home/userdata/addon_data' )
oO0Oo = I11i1I1I + 'GenieTvWatched'
oOOoo0Oo = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYw==' ) )
o00OO00OoO = [ 'daclips' , 'filehoot' , 'allmyvideos' , 'vidspot' , 'vodlocker' , 'vidto' ]
if not os . path . exists ( oO0Oo ) :
 os . makedirs ( oO0Oo )
OOOO0OOoO0O0 = oO0Oo + 'watched.txt'
if not os . path . exists ( OOOO0OOoO0O0 ) :
 open ( OOOO0OOoO0O0 , 'w+' )
O0Oo000ooO00 = open ( OOOO0OOoO0O0 ) . read ( )
oO0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlNvbGQv' ) )
Ii1iIiII1ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
ooOooo000oOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
Oo0oOOo = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
Oo0OoO00oOO0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
OOO00O = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( i1I1iI ) == True :
 OOoOO0oo0ooO = open ( i1I1iI ) . read ( )
else : OOoOO0oo0ooO = [ ]
O0o0O00Oo0o0 = oo00 . getSetting ( 'debug' )
if os . path . exists ( iIi1ii1I1 ) == False :
 os . makedirs ( iIi1ii1I1 )
def O00O0oOO00O00 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = ''
 iiI111I1iIiI = ''
 try :
  i1i = urllib2 . urlopen ( i1Oo00 )
  iiI111I1iIiI = i1i . read ( )
  i1i . close ( )
 except : pass
 if iiI111I1iIiI != '' :
  return iiI111I1iIiI
 else :
  iiI111I1iIiI = 'Failed'
  return iiI111I1iIiI
  if 41 - 41: i1i1I1IIii1II . oooOo0oo0oo - Iii * o0ii1I / IiI1i11I % III1iiIii
O0OOO = [ ]
II11iIiIIIiI = O00O0oOO00O00 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if II11iIiIIIiI != 'Failed' :
 O0OOO . append ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not II11iIiIIIiI != 'Failed' :
 o0o = O00O0oOO00O00 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if o0o != 'Failed' :
  O0OOO . append ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not o0o != 'Failed' :
  o00OooOO000 = O00O0oOO00O00 ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if o00OooOO000 != 'Failed' :
   O0OOO . append ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not o00OooOO000 != 'Failed' :
   OOoOoo = O00O0oOO00O00 ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if OOoOoo != 'Failed' :
    O0OOO . append ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
oO0000OOo00 = ( str ( O0OOO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
iiIi1IIiIi = oO0000OOo00 + 'GenieArt/NEW/'
if 75 - 75: i1IiiiI1iI + i1iIi
if 68 - 68: Ii % Ii1I + Ii
def iii ( ) :
 if not os . path . exists ( iI1Ii11111iIi ) :
  iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  II1I = 'genie tv repo not being installed '
  O0 ( )
 else :
  i1II1Iiii1I11 ( )
  if 9 - 9: Ii1I / I1ii11iIi11i - oOo0O0Ooo / ii / iI11I1II1I1I - I11i
def i1II1Iiii1I11 ( ) :
 if 91 - 91: IiI1i11I % ooOoO0O00 % iI11I1II1I1I
 IIi1I11I1II = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 ii11IIII11I = open ( Oo0OoO00oOO0o ) . read ( )
 OOooo = open ( OOO00O ) . read ( )
 if 90 - 90: I11i % ooOoO0O00 / oO0o
 IIi = re . compile ( 'version="([^"]*)" provider' ) . findall ( ii11IIII11I )
 i1Iii1i1I = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( OOooo )
 OOoO00 = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( IIi1I11I1II )
 IiI111111IIII = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( IIi1I11I1II )
 for i1Ii in IIi :
  ii111iI1iIi1 = i1Ii
  for OOO in OOoO00 :
   if not OOO == ii111iI1iIi1 :
    o0oOoO00o . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    oo0OOo0 ( )
   if OOO == ii111iI1iIi1 :
    I11IiI
 for O0ooO0Oo00o in i1Iii1i1I :
  ooO0oOOooOo0 = O0ooO0Oo00o
  for i1I1ii11i1Iii in IiI111111IIII :
   if not i1I1ii11i1Iii == ooO0oOOooOo0 :
    o0oOoO00o . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    O0 ( )
   if i1I1ii11i1Iii == ooO0oOOooOo0 :
    xbmc . sleep ( 100 )
    I11IiI
def I1IiiiiI ( ) :
 if not os . path . exists ( ooooooO0oo ) :
  o0OIiII ( 'Change Log 23/7/17 - v3.5.7' , '[COLORorangered]Welcoming SUPREMACY Addon To GenieTv[/COLOR],[COLORsteelblue]Now In Streams Section[/COLOR],[CR][COLORorangered]The Return Of Bamf [COLORsteelblue]With Back In Time Section Now In Streams[/COLOR],[CR][COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
  os . makedirs ( ooooooO0oo )
def ii1iII1II ( ) :
 o0OIiII ( 'Change Log 23/7/17 - v3.5.7' , '[COLORorangered]Welcoming SUPREMACY Addon To GenieTv[/COLOR],[COLORsteelblue]Now In Streams Section[/COLOR],[CR][COLORorangered]The Return Of Bamf [COLORsteelblue]With Back In Time Section Now In Streams[/COLOR],[CR][COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
def Iii1I1I11iiI1 ( ) :
 iii ( )
 I1IiiiiI ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  I1I1i1I ( )
 else :
  if 30 - 30: ii
  if 5 - 5: i1iIi - IIiIiII11i - ii % o0ii1I + oOo0O0Ooo * iI11I1II1I1I
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 4009 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
   if 8 - 8: I11i % o0o00Oo0O / oOo0O0Ooo - i1i1I1IIii1II
  if oo00 . getSetting ( 'Music' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'tools.png' , Oo00OOOOO , '' )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , iiIi1IIiIi + 'settings.png' , Oo00OOOOO , '' )
  if OO ( ) == 'android' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , str ( oO0000OOo00 ) , 30039 , iiIi1IIiIi + 'APKpng' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   Ii1I1i ( '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' , str ( oO0000OOo00 ) , 46 , iiIi1IIiIi + 'SoruceList.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '' , 10050 , iiIi1IIiIi + 'Addons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , str ( oO0000OOo00 ) , 39 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def I1I1i1I ( ) :
 if 57 - 57: i1IiiiI1iI % o0ii1I + I11i - I1ii11iIi11i
 if 65 - 65: Iii . OOooOOo
 if 39 - 39: IIiIiII11i / i1iIi + i1IiiiI1iI / OOooOOo
 if 13 - 13: III1iiIii + o0o00Oo0O + IiI1i11I % oOo0O0Ooo / I11i . III1iiIii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 40099 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
  if 86 - 86: i1i1I1IIii1II * I11i % ooOoO0O00 . o0ii1I . Ii
 if oo00 . getSetting ( 'Music' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def tools ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']Change Log[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONTACT US[/COLOR]' , '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  ii1iII1II ( )
 if O0O00Oo == 1 :
  oo0OOo0 ( )
 if O0O00Oo == 2 :
  oooooo0O000o ( )
 if O0O00Oo == 3 :
  OoO ( )
 if O0O00Oo == 4 :
  ooO0O0O0ooOOO ( oOOo0O00o )
 if O0O00Oo == 5 :
  iIii1 . ok ( i1 , i1111 )
 if O0O00Oo == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if O0O00Oo == 7 :
  iIiIi11 ( )
  if 87 - 87: I1ii11iIi11i . oOo0O0Ooo - IIiIiII11i + o0o00Oo0O / I1ii11iIi11i / i1i1I1IIii1II
def IiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIIii1I :
  Ii1I1i ( iIIIiIi , url , 21009 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  if 100 - 100: oOo0O0Ooo / I11i % IIiIiII11i % I1ii11iIi11i % oooOo0oo0oo
def O00oO000O0O ( url ) :
 url = url
 I1i1i1iii = OO ( )
 if I1i1i1iii ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif I1i1i1iii ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 16 - 16: o0ii1I + III1iiIii * o0o00Oo0O % ooOoO0O00 . oOo0O0Ooo
  if 67 - 67: ii / oOo0O0Ooo * o0ii1I + Iii
def OooOo0ooo ( ) :
 oOOo0O00o = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( oOOo0O00o , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 ooO0O00Oo0o ( oOOo0O00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOOOo0o00OO0000 ( )
def I1i ( ) :
 O00Oooo = i11I ( )
 o00Oo0oooooo = O00Oooo . replace ( II11iiii1Ii , "" )
 if os . path . exists ( O00Oooo ) or not O00Oooo == False :
  O0oO0 = open ( O00Oooo , mode = 'r' ) ; iII11 = O0oO0 . read ( ) ; O0oO0 . close ( )
  o0OIiII ( "%s - %s" % ( i1 , o00Oo0oooooo ) , iII11 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OooOo0ooo ( ) :
 oOOo0O00o = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( oOOo0O00o , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 ooO0O00Oo0o ( oOOo0O00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOOOo0o00OO0000 ( )
def iiIiii1IIIII ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Todays Games[/COLOR]' , str ( oO0000OOo00 ) , 90030 , iiIi1IIiIi + 'tgames.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Tommys Replays[/COLOR]' , str ( oO0000OOo00 ) , 900300 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 67 - 67: o0ii1I / III1iiIii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 9 - 9: o0o00Oo0O % o0o00Oo0O - I11i
def OoOiiI1IIIi ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match eng prem[/COLOR]' , 'http://ourmatch.net/videos/england/premier-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match la liga[/COLOR]' , 'http://ourmatch.net/videos/spain/la-liga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match serie a[/COLOR]' , 'http://ourmatch.net/videos/italy/serie-a-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match bund[/COLOR]' , 'http://ourmatch.net/videos/germany/bundesliga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match ligue 1[/COLOR]' , 'http://ourmatch.net/videos/france/ligue-1-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']our match uefa champ[/COLOR]' , 'http://ourmatch.net/videos/europe/uefa-champions-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
iiIi1IIiIi + 'tommysreplays.png'
def II11IiIi11 ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOAL OF THE MONTH[/COLOR]' , 'http://ourmatch.net/goal-of-the-month/' , 900302 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIOOO0O00O0OOOO = re . compile ( 'href="([^"]*)".+?<img src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iiii1I = re . compile ( 'class=\'current\'>.+?</span><a class=.+? href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIOOO0O00O0OOOO :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 900302 , ooO0OO , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for OOo0 in I1iiii1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , OOo0 , 900301 , iiIi1IIiIi + 'NEXT.png' , '' , '' )
def oO00ooooO0o ( url ) :
 oo0o = OooOoooOo ( url )
 IIOOO0O00O0OOOO = re . compile ( "<source src=\"(.+?)\"></video>',.+?'type':'([^']*)'," , re . DOTALL ) . findall ( oo0o )
 o0oO0oooOoo = re . compile ( "embed:'<iframe src=\"(.+?)\" width=.+? 'type':'([^']*)'," , re . DOTALL ) . findall ( oo0o )
 for url , iIIIiIi in IIOOO0O00O0OOOO :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for url , iIIIiIi in o0oO0oooOoo :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
def I1III1111iIi ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIi = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for OooOo0oo0O0o00O , I1i11 in IIi :
  o0OIiII ( '[COLOR' + ooOoOoo0O + ']Tommys List[/COLOR]  ' + OooOo0oo0O0o00O , I1i11 )
def IiIi1I1 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIi = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
def IiIIi1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , ooO0OO , Oo00OOOOO , '' )
 for url in next :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , iiIi1IIiIi + 'NEXT.png' , Oo00OOOOO , '' )
def IIIIiii1IIii ( url ) :
 I1i111I = OooOoooOo ( url )
 II1i11I = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 ii1I1IIii11 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for iIIIiIi , url in i1Iii1i1I :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for iIIIiIi , url in ii1I1IIii11 :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for url in II1i11I :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
  if 67 - 67: IiI1i11I + Iii / I11i . i1i1I1IIii1II + oooOo0oo0oo
def ooOoOo0 ( url ) :
 if 'drive' in url :
  I11iiiiI1i ( url )
 else :
  I1i111I = OooOoooOo ( url )
  IIi = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( I1i111I )
  for url in IIi :
   I11iiiiI1i ( url )
def iI1i11 ( url ) :
 OoOOoooOO0O = liveresolver . resolve ( url )
 ooo00Ooo = xbmcgui . ListItem ( path = OoOOoooOO0O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo00Ooo )
def Oo0o0O00 ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 ii1 = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1 )
def i11I ( ) :
 I1i11OO = False
 if os . path . exists ( os . path . join ( II11iiii1Ii , 'xbmc.log' ) ) :
  I1i11OO = os . path . join ( II11iiii1Ii , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'kodi.log' ) ) :
  I1i11OO = os . path . join ( II11iiii1Ii , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'spmc.log' ) ) :
  I1i11OO = os . path . join ( II11iiii1Ii , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'tvmc.log' ) ) :
  I1i11OO = os . path . join ( II11iiii1Ii , 'tvmc.log' )
 return I1i11OO
 if 84 - 84: i1iIi % o0ii1I + Ii
def II1I1Ii ( url ) :
 if url == 'http://' : return False
 try :
  i1Oo00 = urllib2 . Request ( url )
  i1Oo00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1i = urllib2 . urlopen ( i1Oo00 )
  i1i . close ( )
 except Exception , Ooo0O0oooo :
  return Ooo0O0oooo
 return True
def iiI ( ) :
 if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
 if 39 - 39: o0o00Oo0O + i1IiiiI1iI
 if 91 - 91: ii - iI11I1II1I1I + OOooOOo / oO0o . OOooOOo + o0o00Oo0O
 if 26 - 26: Ii1I - ii
 if 11 - 11: oOo0O0Ooo * i1i1I1IIii1II
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def o000oo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Wizard[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   o00o0 ( )
  if O0O00Oo == 1 :
   II1III1I1I1Ii ( )
  if O0O00Oo == 2 :
   OOOOoO00o0O ( I1I1I1IIi1III )
  if O0O00Oo == 3 :
   II11IiiIII ( oOOo0O00o )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 10060 , iiIi1IIiIi + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 49 , iiIi1IIiIi + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , str ( oO0000OOo00 ) , 41 , iiIi1IIiIi + 'WipeGenie.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' , str ( oO0000OOo00 ) , 44 , iiIi1IIiIi + 'GenieBuilds.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 58 - 58: o0ii1I + I11i - oOo0O0Ooo
def i1i1ii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if 46 - 46: OOooOOo + oO0o
  if 70 - 70: IiI1i11I / iI11I1II1I1I
  if oo00 . getSetting ( 'Search' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 9000 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Streams[/COLOR]' , '' , 10025 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , iiIi1IIiIi + 'bamf.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Supremacy[/COLOR]' , '' , 1131000 , iiIi1IIiIi + 'supremacy.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiIi1IIiIi + 'zone.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']STREAM CATEGORIES[/COLOR]' , str ( oO0000OOo00 ) , 90002 , iiIi1IIiIi + 'cats.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
   if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
   if 96 - 96: ii + i1i1I1IIii1II
   if 44 - 44: i1i1I1IIii1II
 else :
  if 20 - 20: Iii + o0ii1I / o0o00Oo0O % iI11I1II1I1I
  if 88 - 88: OOooOOo / IIiIiII11i
  if oo00 . getSetting ( 'Search' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 9000 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Streams[/COLOR]' , '' , 10025 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Back In Time[/COLOR]' , 'http://genietvcunts.co.uk/bamffff/BAMF.xml' , 90036 , iiIi1IIiIi + 'bamf.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Supremacy[/COLOR]' , '' , 1131000 , iiIi1IIiIi + 'supremacy.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiIi1IIiIi + 'zone.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
   if 87 - 87: Ii1I - Ii1I - IiI1i11I + i1i1I1IIii1II
   if 82 - 82: i1i1I1IIii1II / iI11I1II1I1I . oOo0O0Ooo . oooOo0oo0oo / I11i
   if 42 - 42: I1ii11iIi11i
   if 19 - 19: i1i1I1IIii1II % Ii1I * iI11I1II1I1I + oOo0O0Ooo
   if 46 - 46: I1ii11iIi11i
   if 1 - 1: IiI1i11I
   if 97 - 97: oooOo0oo0oo + IiI1i11I + o0o00Oo0O + Ii
   if 77 - 77: I11i / ii
   if 46 - 46: I11i % iI11I1II1I1I . IiI1i11I % IiI1i11I + Ii
   if 72 - 72: iI11I1II1I1I * o0ii1I % i1iIi / oO0o
   if 35 - 35: i1iIi + ooOoO0O00 % Ii1I % Iii + i1i1I1IIii1II
   if 17 - 17: ooOoO0O00
   if 21 - 21: I1ii11iIi11i
   if 29 - 29: Iii / IIiIiII11i / i1iIi * oooOo0oo0oo
   if 10 - 10: i1IiiiI1iI % III1iiIii * III1iiIii . Iii / o0ii1I % oooOo0oo0oo
   if 49 - 49: oO0o / i1i1I1IIii1II + o0o00Oo0O * I11i
   if 28 - 28: i1iIi + Ii / Iii % OOooOOo % I1ii11iIi11i - o0o00Oo0O
   if 54 - 54: ooOoO0O00 + IIiIiII11i
   if 83 - 83: Ii1I - oOo0O0Ooo + oooOo0oo0oo
   if 5 - 5: o0ii1I
   if 46 - 46: III1iiIii
   if 45 - 45: i1iIi
   if 21 - 21: i1i1I1IIii1II . i1IiiiI1iI . oooOo0oo0oo / I1ii11iIi11i / i1IiiiI1iI
   if 17 - 17: oooOo0oo0oo / oooOo0oo0oo / Iii
   if 1 - 1: ooOoO0O00 . Ii % oooOo0oo0oo
   if 82 - 82: iI11I1II1I1I + I1ii11iIi11i . iI11I1II1I1I % III1iiIii / o0ii1I . o0ii1I
   if 14 - 14: I11i . oooOo0oo0oo . Iii + ii - oooOo0oo0oo + III1iiIii
   if 9 - 9: o0ii1I
 I1iI1ii1II ( 'movies' , 'MAIN' )
def oooooOOO000Oo ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  Ooo00OoOOO ( )
 if O0O00Oo == 1 :
  Oo0OO0000oooo ( )
 if O0O00Oo == 2 :
  IIII1iII ( )
 if O0O00Oo == 3 :
  ii1III11 ( )
 if O0O00Oo == 4 :
  I1iiIIIi11 ( )
 if O0O00Oo == 5 :
  Ii1I11ii1i ( )
  if 89 - 89: IiI1i11I . o0o00Oo0O / Ii1I % OOooOOo . I1ii11iIi11i
  if 50 - 50: IIiIiII11i + Ii1I . ooOoO0O00 % I11i
def IIIi ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   O00OoO0o ( )
  if O0O00Oo == 1 :
   i1i111iI ( )
  if O0O00Oo == 2 :
   IIiiI ( oOOo0O00o )
  if O0O00Oo == 3 :
   III1i11 ( )
  if O0O00Oo == 4 :
   iiI111 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0O00Oo == 5 :
   I1iIiIi11i11 ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 9001 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 10200 , iiIi1IIiIi + 'rated.png' , Oo00OOOOO , '' )
  if 52 - 52: i1iIi + o0o00Oo0O . IiI1i11I . Ii1I . oO0o
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , str ( oO0000OOo00 ) , 7061 , iiIi1IIiIi + 'PopcornBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Desi Flix[/COLOR]' , '' , 80005 , iiIi1IIiIi + 'Desi.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiIi1IIiIi + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiIi1IIiIi + 'ClassicMovies.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def oo000ii ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 78 - 78: ii . oO0o + i1iIi - ooOoO0O00
 if 31 - 31: ii . oooOo0oo0oo
 if 83 - 83: IiI1i11I . o0o00Oo0O / I1ii11iIi11i / oooOo0oo0oo - IIiIiII11i
 if 100 - 100: oO0o
 if 46 - 46: OOooOOo / iI11I1II1I1I % IiI1i11I . iI11I1II1I1I * IiI1i11I
def IIi1ii1Ii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   OoOoO ( )
  if O0O00Oo == 1 :
   o0ii1i ( )
  if O0O00Oo == 2 :
   oOOoo ( )
  if O0O00Oo == 3 :
   iII1111III1I ( )
  if O0O00Oo == 4 :
   ii11i ( )
  if O0O00Oo == 5 :
   O00oOo00o0o ( )
  if O0O00Oo == 6 :
   O00oO0 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , str ( oO0000OOo00 ) , 9002 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  if 70 - 70: Iii . Ii1I * ii - III1iiIii * oOo0O0Ooo + OOooOOo
  if 10 - 10: I11i / Ii
  if 92 - 92: Iii . i1IiiiI1iI
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiIi1IIiIi + 'iWatchSeries.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , str ( oO0000OOo00 ) , 10095 , iiIi1IIiIi + 'RD.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , str ( oO0000OOo00 ) , 8064 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiIi1IIiIi + 'TVShowTrailers.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def oOO00O0Ooooo00 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   O000 = '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]'
   if 79 - 79: ii - oOo0O0Ooo
   if 69 - 69: Iii
   if 95 - 95: i1iIi + Ii * i1IiiiI1iI - ooOoO0O00 * i1IiiiI1iI - iI11I1II1I1I
   if 75 - 75: ii * III1iiIii
  oOOoo00O00o = [ O000 , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I1Iiiiiii ( )
  if O0O00Oo == 1 :
   I1IIIiI1I1ii1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , iiiI1I1iIIIi1 , iIIIiIi )
  if O0O00Oo == 2 :
   IiiI1iiiiI1iI ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if O0O00Oo == 3 :
   I1IIIiI1I1ii1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , iiiI1I1iIIIi1 , iIIIiIi )
 else :
  if 43 - 43: i1i1I1IIii1II - ii
  if 3 - 3: o0o00Oo0O / IiI1i11I
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 31 - 31: oooOo0oo0oo + I11i . ii
  if 89 - 89: IIiIiII11i + ooOoO0O00 + IIiIiII11i
  if 7 - 7: o0o00Oo0O % I11i + Ii1I * IiI1i11I - IiI1i11I
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  if 42 - 42: OOooOOo * OOooOOo * i1IiiiI1iI . Iii
  if 51 - 51: oooOo0oo0oo % iI11I1II1I1I - ii % i1iIi * iI11I1II1I1I % oO0o
  if 99 - 99: i1i1I1IIii1II * IIiIiII11i * i1IiiiI1iI
  if 92 - 92: I1ii11iIi11i
  if 40 - 40: OOooOOo / III1iiIii
  if 79 - 79: oO0o - iI11I1II1I1I + o0ii1I - i1IiiiI1iI
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 61 - 61: IIiIiII11i
def Ii1ii111i1 ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def IiiI1iiiiI1iI ( url ) :
 I1i111I = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 ii1I1IIii11 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 for iIIIiIi , ooO0OO , url in IIi :
  if '247ch' in url :
   oOoo000 ( iIIIiIi , url , 10190 , ooO0OO )
  elif '.m3u' in url :
   oOoo000 ( iIIIiIi , url , 1019 , ooO0OO )
  elif '.xml' in url :
   oOoo000 ( iIIIiIi , url , 1018 , ooO0OO )
  else :
   OooOo00o ( iIIIiIi , url , 222 , ooO0OO )
 for iIIIiIi , url , ooO0OO in i1Iii1i1I :
  if '.xml' in url :
   oOoo000 ( iIIIiIi , url , 1018 , ooO0OO )
  elif '.m3u' in url :
   oOoo000 ( iIIIiIi , url , 1019 , ooO0OO )
  else :
   OooOo00o ( iIIIiIi , url , 222 , ooO0OO )
 for iIIIiIi , url , ooO0OO in ii1I1IIii11 :
  OooOo00o ( iIIIiIi , url , 8043 , ooO0OO )
def IiI11i1IIiiI ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def OoOo00o0OO ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url , ooO0OO in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , ooO0OO )
  if 1 - 1: oOo0O0Ooo % i1iIi
def oOoO00 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 40 - 40: I11i
def OOOooo ( url ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url , O0oOOo0Oo , o000O000 , IIo0o0O0O00oOOo , O000OOO in IIi :
  if o000O000 == '123' :
   o000O000 = iiIi1IIiIi + 'appstreams.png'
  if IIo0o0O0O00oOOo == '123' :
   IIo0o0O0O00oOOo = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   I1I1II1I11 ( iIIIiIi , url , 100010 , o000O000 , IIo0o0O0O00oOOo , O000OOO )
  elif 'playlist' in url :
   I1I1II1I11 ( iIIIiIi , url , 100007 , o000O000 , IIo0o0O0O00oOOo , O000OOO )
  elif 'watchseries' in url :
   I1I1II1I11 ( iIIIiIi , url , 100100 , o000O000 , IIo0o0O0O00oOOo , O000OOO )
  elif not 'http' in url :
   ii1oOoO0o0ooo ( iIIIiIi , url , 100009 , o000O000 , IIo0o0O0O00oOOo , O000OOO , '' )
  else :
   ii1oOoO0o0ooo ( iIIIiIi , url , 100005 , o000O000 , IIo0o0O0O00oOOo , O000OOO , '' )
   if 86 - 86: Ii1I * o0o00Oo0O * III1iiIii
def Ooo0oo ( url ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIIii1I :
  if ooO0OO == '123' :
   ooO0OO = iiIi1IIiIi + 'appstreams.png'
  if IIo0o0O0O00oOOo == '123' :
   IIo0o0O0O00oOOo = Oo00OOOOO
  if 'php' in url :
   I1I1II1I11 ( iIIIiIi , url , 100004 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  elif 'playlist' in url :
   I1I1II1I11 ( iIIIiIi , url , 100007 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  elif 'watchseries' in url :
   I1I1II1I11 ( iIIIiIi , url , 100100 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  elif not 'http' in url :
   ii1oOoO0o0ooo ( iIIIiIi , url , 100009 , ooO0OO , IIo0o0O0O00oOOo , O000OOO , '' )
  else :
   ii1oOoO0o0ooo ( iIIIiIi , url , 100005 , ooO0OO , IIo0o0O0O00oOOo , O000OOO , '' )
   if 41 - 41: OOooOOo * Iii / OOooOOo % i1i1I1IIii1II
def IioO0oOOO0Ooo ( url ) :
 if 38 - 38: oOo0O0Ooo
 II11iIiIIIiI = Oo00oo0000OO ( url )
 oOo0OoOOo0 = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1i1i1I in oOo0OoOOo0 :
  o000O000 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( i1i1i1I ) )
  for o000O000 in o000O000 :
   o000O000 = o000O000
  iIIIiIi = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( i1i1i1I ) )
  for iIIIiIi in iIIIiIi :
   if 'elete' in iIIIiIi :
    pass
   elif 'rivate Vid' in iIIIiIi :
    pass
   else :
    iIIIiIi = ( iIIIiIi ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  iII11I1Ii1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( i1i1i1I ) )
  for iII11I1Ii1 in iII11I1Ii1 :
   iII11I1Ii1 = iII11I1Ii1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( i1i1i1I ) )
  for url in url :
   url = url
  ii1oOoO0o0ooo ( '[COLORred]' + str ( iII11I1Ii1 ) + '[/COLOR] : ' + str ( iIIIiIi ) , str ( url ) , 100009 , str ( o000O000 ) , Oo00OOOOO , '' , '' )
  I1iI1ii1II ( 'movies' , '' )
  if 92 - 92: Iii / Iii . Ii1I
  if 17 - 17: Ii - IIiIiII11i * I11i
  if 5 - 5: oooOo0oo0oo - oooOo0oo0oo . I1ii11iIi11i + OOooOOo - oooOo0oo0oo . i1i1I1IIii1II
  if 31 - 31: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I % Iii
def iiiI1ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIIii1I :
  if '.php' in url :
   I1I1II1I11 ( iIIIiIi , url , 100210 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  else :
   Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
   if 50 - 50: oOo0O0Ooo * Ii
   if 68 - 68: oooOo0oo0oo * o0o00Oo0O . Iii - IIiIiII11i . i1iIi / IIiIiII11i
   if 47 - 47: ii
def ii1i1i1IiII ( iconimage , url , extra ) :
 o000O000 = ' '
 O0o = ' '
 IIo0o0O0O00oOOo = ' '
 II11I = ' '
 oo0oOO00oO = Oo00oo0000OO ( url )
 o000O000 = re . compile ( '<img src="(.+?)">' ) . findall ( oo0oOO00oO )
 for o000O000 in o000O000 :
  o000O000 = o000O000
 i11i1iIiii = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( oo0oOO00oO )
 for IIo0o0O0O00oOOo in i11i1iIiii :
  IIo0o0O0O00oOOo = IIo0o0O0O00oOOo
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( oo0oOO00oO )
 for url , II11I in IIi :
  II11I = 'S' + ( II11I ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  OOO00OO0oOo ( ( II11I ) . replace ( '  ' , '' ) , url , 100101 , o000O000 , IIo0o0O0O00oOOo , O0o , '' )
  I1iI1ii1II ( 'Movies' , 'info' )
  if 35 - 35: IiI1i11I + i1iIi - i1i1I1IIii1II . IiI1i11I . III1iiIii
def oo0ooOO ( url , name , fanart , extra , iconimage ) :
 iI1IiIIiIIi = extra
 II11I = name
 oo0oOO00oO = Oo00oo0000OO ( url )
 o000O000 = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( oo0oOO00oO )
 for url , name , IiIi11Iii in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  IiIi11Iii = IiIi11Iii
  III1i1iI1 = name + ' - [COLORred]' + IiIi11Iii + '[/COLOR]'
  OOO00OO0oOo ( III1i1iI1 , url , 100102 , o000O000 , fanart , 'Aired : ' + IiIi11Iii , III1i1iI1 )
  if 97 - 97: Iii - Ii
def i1iIi1II11 ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = Oo00oo0000OO ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , name in IIi :
  for ooo00Ooo in o00OO00OoO :
   if ooo00Ooo in oOOo0O00o :
    URL = 'http://www.watchseriesgo.to/link/' + oOOo0O00o
    ii1oOoO0o0ooo ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  OOO00OO0oOo ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 11 - 11: IiI1i11I * o0ii1I - OOooOOo
  if 66 - 66: OOooOOo . Ii - IiI1i11I * I11i + ii * Ii1I
def oO0OO0 ( url , name ) :
 O00Oo = name
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  Ii1111IiIi ( url , O00Oo )
 for url in i1Iii1i1I :
  Ii1111IiIi ( url , O00Oo )
 for url in ii1I1IIii11 :
  Ii1111IiIi ( url , O00Oo )
  if 35 - 35: oooOo0oo0oo * I11i * oOo0O0Ooo % I1ii11iIi11i . OOooOOo
def Ii1111IiIi ( url , season_name ) :
 if 'daclips.in' in url :
  O00o00O ( url , season_name )
 elif 'filehoot.com' in url :
  ii1iii11i1 ( url , season_name )
 elif 'allmyvideos.net' in url :
  I11Oo00oO0O ( url , season_name )
 elif 'vidspot.net' in url :
  OOooO ( url , season_name )
 elif 'vodlocker' in url :
  O00O0OO00oo ( url , season_name )
 elif 'vidto' in url :
  oOOO ( url , season_name )
  if 56 - 56: Ii1I
  if 26 - 26: ii % ii
def oOOO ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII , iIIIiIi in IIi :
  oooO ( iIIIII1iiiiII , season_name )
  if 22 - 22: i1iIi - i1iIi % oooOo0oo0oo . i1IiiiI1iI + i1i1I1IIii1II
  if 63 - 63: oOo0O0Ooo % i1IiiiI1iI * I11i + i1IiiiI1iI / I1ii11iIi11i % IiI1i11I
def I11Oo00oO0O ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII , iIIIiIi in IIi :
  oooO ( iIIIII1iiiiII , season_name )
  if 45 - 45: III1iiIii
def OOooO ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII , iIIIiIi in IIi :
  oooO ( iIIIII1iiiiII , season_name )
  if 20 - 20: ii * I11i * o0o00Oo0O . oooOo0oo0oo
def O00O0OO00oo ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII in IIi :
  oooO ( iIIIII1iiiiII , season_name )
  if 78 - 78: iI11I1II1I1I + Iii - o0ii1I * i1IiiiI1iI - ii % OOooOOo
def O00o00O ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII in IIi :
  oooO ( iIIIII1iiiiII , season_name )
  if 34 - 34: o0o00Oo0O
def ii1iii11i1 ( url , season_name ) :
 II11iIiIIIiI = Oo00oo0000OO ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIII1iiiiII in IIi :
  oooO ( iIIIII1iiiiII , season_name )
  if 80 - 80: ooOoO0O00 - I1ii11iIi11i / oO0o - Ii
def oooO ( Link , season_name ) :
 if 'http:/' in Link :
  OO0O0o0o0 ( Link )
  if 31 - 31: o0ii1I
def iIIiI1I1i ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 O0O0OOooOO0 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in O0O0OOooOO0 :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 31 - 31: oOo0O0Ooo * i1i1I1IIii1II + ii - IiI1i11I / ii
def OOO00OO0oOo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  if 31 - 31: i1i1I1IIii1II / III1iiIii * I11i . IIiIiII11i
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
 if 89 - 89: o0o00Oo0O
 if 2 - 2: Ii1I . Ii1I + Ii1I * I11i
def ii1oOoO0o0ooo ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
 if 100 - 100: I1ii11iIi11i % o0ii1I / Iii
def iIII11Ii ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 52 - 52: i1IiiiI1iI / i1iIi - Iii
def iIiI ( url ) :
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iIIIi1i1I11i . play ( url ) . strip ( )
 except : pass
 if 87 - 87: i1i1I1IIii1II + iI11I1II1I1I - ii
def OO0O0o0o0 ( url ) :
 iIIIi1i1I11i = xbmc . Player ( )
 import urlresolver
 try : iIIIi1i1I11i . play ( url )
 except : pass
 if 8 - 8: ii / Iii + ooOoO0O00 . IiI1i11I
def Oo00oo0000OO ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = ''
 iiI111I1iIiI = ''
 try :
  i1i = urllib2 . urlopen ( i1Oo00 )
  iiI111I1iIiI = i1i . read ( )
  i1i . close ( )
 except : pass
 if iiI111I1iIiI != '' :
  return iiI111I1iIiI
 else :
  iiI111I1iIiI = 'Opened'
  return iiI111I1iIiI
  if 73 - 73: ooOoO0O00 + IiI1i11I . Ii
  if 5 - 5: i1i1I1IIii1II . Ii1I . IIiIiII11i . ii
  if 96 - 96: Ii - oooOo0oo0oo % o0o00Oo0O / oO0o
def Oo0OO0000oooo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   O0O0 ( )
  if O0O00Oo == 1 :
   oo0OOOoOo ( )
  if O0O00Oo == 2 :
   IIiiIIi1 ( )
  if O0O00Oo == 3 :
   ooO000O ( )
  if O0O00Oo == 4 :
   oOIII111iiIi1 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'SearchCartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( oO0000OOo00 ) , 21004 , iiIi1IIiIi + 'watchcartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '' , 10001 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '' , 20000 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , iiIi1IIiIi + 'anime.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def ii1III11 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iiIi1IIiIi + 'Fitness.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Go Fishing[/COLOR]' , str ( oO0000OOo00 ) , 8090 , iiIi1IIiIi + 'GoFishing.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , iiIi1IIiIi + 'GenieTVKitchen.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 29 - 29: ii + o0ii1I % iI11I1II1I1I - oooOo0oo0oo . oOo0O0Ooo % I1ii11iIi11i
 if 16 - 16: III1iiIii / I1ii11iIi11i + oooOo0oo0oo / o0ii1I
 if 42 - 42: I1ii11iIi11i + IIiIiII11i - oOo0O0Ooo / Iii % III1iiIii
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   O0ooOOO = ( II1I ) . replace ( 'special://home/addons/' , '' )
   o0OIiII ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + O0ooOOO + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0O00Oo = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0O00Oo == 0 :
    O0oiIiiiiI1II1I1 ( II1I )
    OOOOo0o00OO0000 ( )
   elif O0O00Oo == 1 :
    OoO0ooO ( II1I )
  else :
   pass
   if 52 - 52: Ii / ooOoO0O00
def OoO0ooO ( addon ) :
 O0ooOOO = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 1 - 1: i1iIi
def O0oiIiiiiI1II1I1 ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 oOO0oo = os . path . join ( IIIII , 'default.py' )
 II1iIi1IiIii = open ( oOO0oo , "w+" )
 if 30 - 30: i1iIi % IiI1i11I * oooOo0oo0oo - Ii1I * o0ii1I % i1iIi
 II1iIi1IiIii . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 II1iIi1IiIii . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 II1iIi1IiIii . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 46 - 46: Ii - o0o00Oo0O . i1i1I1IIii1II
 if 100 - 100: oOo0O0Ooo / I11i * IiI1i11I . o0o00Oo0O / oooOo0oo0oo
 if 83 - 83: i1IiiiI1iI
 if 48 - 48: IIiIiII11i * oooOo0oo0oo * i1IiiiI1iI
def i1iiiIii11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OOoOOO000O0 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oOo0 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 II1i11I = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 II1i11I1 = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url , iiIiIiII , IIo0o0O0O00oOOo , O000OOO in OOoOOO000O0 :
  if 'php' in url :
   I1I1II1I11 ( iIIIiIi , url , 90037 , iiIiIiII , IIo0o0O0O00oOOo , O000OOO )
  elif iIIIiIi == 'Search' :
   I1I1II1I11 ( 'Search' , url , 90038 , iiIiIiII , IIo0o0O0O00oOOo , O000OOO )
  else :
   Ii1I1i ( iIIIiIi , url , 222 , iiIiIiII , IIo0o0O0O00oOOo , O000OOO )
 for iIIIiIi , ooO0OO , url , i1I1 in oOo0 :
  I1I1II1I11 ( iIIIiIi , url , 90037 , ooO0OO , i1I1 , '' )
 for iIIIiIi , ooO0OO , url , i1I1 in IIi :
  I1I1II1I11 ( iIIIiIi , url , 90037 , ooO0OO , i1I1 , '' )
 for iIIIiIi , url , ooO0OO , i1I1 in i1Iii1i1I :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , i1I1 , '' )
 for iIIIiIi , url , ooO0OO , i1I1 in ii1I1IIii11 :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , i1I1 , '' )
 for iIIIiIi , url , ooO0OO , i1I1 in II1i11I :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , i1I1 , '' )
 for iIIIiIi , url , ooO0OO in II1i11I1 :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , '' , '' )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
def iIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , ooO0OO , url , i1I1 in IIi :
  I1I1II1I11 ( iIIIiIi , url , 90037 , ooO0OO , i1I1 , '' )
 for iIIIiIi , url , ooO0OO , i1I1 in i1Iii1i1I :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , i1I1 , '' )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
  if 10 - 10: oO0o / I1ii11iIi11i
def I1iII11iIII1i1I ( ) :
 oOO0ooIiIIi1I1I11Ii = [ 'serialsearch' , 'moviesearch' ]
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 if Oo == '' :
  pass
 else :
  for iiIiI in oOO0ooIiIIi1I1I11Ii :
   o0Ooo0O00 = Oo0o0000o0o0 + iiIiI + '.php'
   oo0oOO00oO = OooOoooOo ( o0Ooo0O00 )
   if oo0oOO00oO != 'Opened' :
    IIIii1I = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( oo0oOO00oO )
    for iIIIiIi , oOOo0O00o , iiIiIiII , IIo0o0O0O00oOOo , O000OOO in IIIii1I :
     if Oo in iIIIiIi . lower ( ) :
      ii1o0oooO = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for ooo00Ooo in ii1o0oooO :
       if ooo00Ooo == oOOo0O00o :
        iIIIiIi = '[COLORred]* [/COLOR]' + ( iIIIiIi ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        ooOo = open ( OOOO0OOoO0O0 , "a" )
        ooOo . write ( 'item="' + iIIIiIi + '"\n' )
        ooOo . close
      if 'php' in oOOo0O00o :
       I1I1II1I11 ( iIIIiIi , oOOo0O00o , 90037 , iiIiIiII , IIo0o0O0O00oOOo , O000OOO )
      else :
       Ii1I1i ( iIIIiIi , oOOo0O00o , 222 , iiIiIiII , IIo0o0O0O00oOOo , O000OOO )
       if 84 - 84: oooOo0oo0oo
   I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
   if 87 - 87: i1iIi + I11i
def i1iIIIIIIiII1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://www.tvcatchup.com/channels/' )
 o0o = OooOoooOo ( 'http://www.djing.com/' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img style="" src="([^"]*)" alt="([^"]*)"/>.+?<br/>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iii11 = re . compile ( 'title="([^"]*)".+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( o0o )
 for oOOo0O00o , ooO0OO , i1oO , iIIIiIi in IIi :
  OooOo00o ( ( '[COLORgold]' + i1oO + '[/COLOR][COLORwhite] - [COLORsteelblue]' + iIIIiIi + '[/COLOR]' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' ) , 'http://www.tvcatchup.com' + oOOo0O00o , 90024 , ooO0OO )
 for I1IIIii , oOOo0O00o , ooO0OO in iii11 :
  OooOo00o ( I1IIIii , 'http://www.tvcatchup.com' + oOOo0O00o , 90024 , ooO0OO )
 for oOOo0O00o , ooO0OO , iIIIiIi in i1Iii1i1I :
  if 'Submit' in iIIIiIi :
   pass
  elif '&lt;' in iIIIiIi :
   pass
  else :
   Ii1I1i ( '[COLORgold]DJing  [/COLOR][COLORwhite]- [COLORsteelblue]' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 90025 , 'http://www.djing.com' + ooO0OO , Oo00OOOOO , '' )
  I1iI1ii1II ( 'movies' , 'MAIN' )
def iI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 42 - 42: ii + I1ii11iIi11i % IIiIiII11i + oO0o
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiiiI1i ( url )
def I11i11I1iiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  IiiI ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 19 - 19: IIiIiII11i
def i1i111iI ( ) :
 if 72 - 72: ii / oOo0O0Ooo + o0ii1I / OOooOOo * o0ii1I
 if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + IiI1i11I * iI11I1II1I1I % o0ii1I
 if 25 - 25: Iii + OOooOOo . I11i % OOooOOo * oooOo0oo0oo
 if 32 - 32: Ii - i1IiiiI1iI
 if 53 - 53: ii - III1iiIii
 if 87 - 87: i1i1I1IIii1II . oOo0O0Ooo
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'yr' in oOOo0O00o :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + oOOo0O00o , 10201 , iiIi1IIiIi + 'rated.png' )
   if 17 - 17: o0ii1I . Ii
def IIIiiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO00oo00 , url , iIIIiIi in IIi :
  if 'id' in url :
   oOoo000 ( ( '[COLORred]RANK [COLORblue]' + OoO00oo00 + '[COLORred] - [COLORblue]' + iIIIiIi + '[/COLOR]' ) , iIIIiIi , 10202 , iiIi1IIiIi + 'rated.png' )
   if 76 - 76: ii + I1ii11iIi11i % III1iiIii . oO0o + IIiIiII11i
def oO0oOooooOoO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 i1oOOOOOOOoO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0OO = ( url )
 Oo = o0OO . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( o0OO ) . replace ( ' ' , '+' )
 I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 IIiI = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 O0oOOo0o = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 I1III11iiii11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 ooOo0OoO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1iiIIi1I = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o0OO
 iiI1I1IIi11i1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 i1II1iii1i = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 83 - 83: Ii1I / i1IiiiI1iI - Ii . iI11I1II1I1I + I1ii11iIi11i
 ooO0000o00O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 O0Ooo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 78 - 78: oO0o % III1iiIii * ooOoO0O00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( I1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( IIiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( O0oOOo0o )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 O0iI = O00O0oOO00O00 ( I1III11iiii11i1 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 Ii1IIiiIiiIi = O00O0oOO00O00 ( i1iiIIi1I )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 i1iiIIIi = O00O0oOO00O00 ( iiI1I1IIi11i1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 Oo0o = O00O0oOO00O00 ( i1II1iii1i )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 93 - 93: oooOo0oo0oo
 if 43 - 43: Ii1I / oOo0O0Ooo . i1iIi
 Ooo0oO0 = O00O0oOO00O00 ( ooO0000o00O )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 o0Oo0oOooOoOo = O00O0oOO00O00 ( O0Ooo )
 if 49 - 49: oooOo0oo0oo . Ii1I . Ii - IIiIiII11i / o0ii1I
 if 62 - 62: oooOo0oo0oo
 if 1 - 1: III1iiIii / III1iiIii - Ii
 if 87 - 87: I1ii11iIi11i / o0o00Oo0O * III1iiIii / I11i
 if 19 - 19: i1IiiiI1iI + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
 if 16 - 16: i1i1I1IIii1II + i1iIi / I11i
 if 82 - 82: III1iiIii * Ii % IIiIiII11i - ii
 if 90 - 90: I1ii11iIi11i . i1i1I1IIii1II * ooOoO0O00 - ooOoO0O00
 if 16 - 16: oOo0O0Ooo * ooOoO0O00 - I11i . III1iiIii % Iii / I11i
 if 14 - 14: iI11I1II1I1I * i1IiiiI1iI * Ii1I / iI11I1II1I1I * III1iiIii / Iii
 if 77 - 77: oO0o + i1IiiiI1iI + i1IiiiI1iI * o0ii1I / ii . o0ii1I
 if 62 - 62: ooOoO0O00 - ooOoO0O00
 if 69 - 69: OOooOOo % i1i1I1IIii1II - Iii
 if Oo0o != 'Failed' :
  Iiii1ii = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oo0o )
  for url , iIIIiIi in Iiii1ii :
   I1i111IiIiIi1 = O00O0oOO00O00 ( url )
   i1II11II1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1i111IiIiIi1 )
   for II1IIIii , iIIIiIi1I1i in i1II11II1 :
    iIIIiIi1I1i = ( iIIIiIi1I1i . replace ( '.' , ' ' ) )
    if Oo in iIIIiIi1I1i . lower ( ) :
     if '.mkv' in II1IIIii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + II1IIIii , 222 , '' , '' , '' )
     elif '.mp4' in II1IIIii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + II1IIIii , 222 , '' , '' , '' )
     elif '.avi' in II1IIIii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + II1IIIii , 222 , '' , '' , '' )
     elif '.wav' in II1IIIii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + II1IIIii , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + II1IIIii , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 78 - 78: iI11I1II1I1I % OOooOOo + Ii1I / ooOoO0O00 % IIiIiII11i + oooOo0oo0oo
      I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in i1Iii1i1I :
   if o0OO in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 91 - 91: iI11I1II1I1I % oO0o . I11i + o0ii1I + I11i
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 95 - 95: o0ii1I + Ii1I * oooOo0oo0oo
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for I1Ii , iIIIiIi in ii1I1IIii11 :
   if o0OO in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IIiI + I1Ii ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in II1i11I :
   if o0OO in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 77 - 77: iI11I1II1I1I - ooOoO0O00 . i1i1I1IIii1II
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if O0iI != 'Failed' :
  iIi1iIIIiIiI = [ ]
  II1i11I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0iI )
  for url , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in II1i11I1 :
   if o0OO in iIIIiIi . lower ( ) :
    if iIIIiIi in iIi1iIIIiIiI :
     pass
    else :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
     iIi1iIIIiIiI . append ( iIIIiIi )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if Ii1IIiiIiiIi != 'Failed' :
  OooOo000o0o = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( Ii1IIiiIiiIi )
  for url , ooO0OO , iIIIiIi in OooOo000o0o :
   if o0OO in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , ooO0OO )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 42 - 42: i1i1I1IIii1II % oooOo0oo0oo
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 60 - 60: OOooOOo / i1IiiiI1iI - IIiIiII11i . I1ii11iIi11i + o0o00Oo0O
    if 43 - 43: iI11I1II1I1I / IIiIiII11i % I11i - oooOo0oo0oo
    if 62 - 62: Iii
    if 63 - 63: oooOo0oo0oo + i1iIi * i1i1I1IIii1II / I11i / I1ii11iIi11i * iI11I1II1I1I
    if 57 - 57: OOooOOo - i1i1I1IIii1II / i1iIi % Ii
    if 3 - 3: IiI1i11I . i1iIi % oOo0O0Ooo + Ii1I
    if 64 - 64: ooOoO0O00
    if 29 - 29: I11i / Ii / oOo0O0Ooo % i1i1I1IIii1II % Ii
    if 18 - 18: oooOo0oo0oo + i1IiiiI1iI
    if 80 - 80: i1i1I1IIii1II + I11i * o0ii1I + oO0o
    if 75 - 75: Iii / I11i / oooOo0oo0oo / III1iiIii % i1iIi + IIiIiII11i
    if 4 - 4: IiI1i11I - I1ii11iIi11i - III1iiIii - Iii % Ii / oO0o
    if 50 - 50: i1iIi + ooOoO0O00
    if 31 - 31: o0ii1I
    if 78 - 78: Ii + I11i + i1IiiiI1iI / I11i % iI11I1II1I1I % III1iiIii
    if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % i1IiiiI1iI . Ii1I % o0o00Oo0O
    if 47 - 47: I11i
    if 66 - 66: oOo0O0Ooo - III1iiIii
 if Ooo0oO0 != 'Failed' :
  iiIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ooo0oO0 )
  for url , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in iiIii :
   if o0OO in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 28 - 28: i1i1I1IIii1II
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 52 - 52: oOo0O0Ooo + iI11I1II1I1I
    if 71 - 71: o0o00Oo0O / i1i1I1IIii1II
    if 34 - 34: OOooOOo . iI11I1II1I1I % o0o00Oo0O
    if 43 - 43: Ii1I - IiI1i11I
    if 70 - 70: IiI1i11I / oooOo0oo0oo % i1iIi - o0ii1I
    if 47 - 47: IiI1i11I
    if 92 - 92: oooOo0oo0oo + OOooOOo % ooOoO0O00
    if 23 - 23: i1IiiiI1iI - oooOo0oo0oo + o0ii1I - OOooOOo * OOooOOo . I1ii11iIi11i
    if 47 - 47: i1i1I1IIii1II % iI11I1II1I1I
    if 11 - 11: oOo0O0Ooo % o0ii1I - oO0o - i1i1I1IIii1II + I11i
 o0O0O0 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 55 - 55: o0o00Oo0O - i1IiiiI1iI
 for iiIiI in o0O0O0 :
  o0Ooo0O00 = oO0 + iiIiI + oOoOooOo0o0
  Oo0o = O00O0oOO00O00 ( o0Ooo0O00 )
  if Oo0o != 'Failed' :
   Iiii1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0o )
   for url , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in Iiii1ii :
    if o0OO in iIIIiIi . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 58 - 58: OOooOOo - IiI1i11I - ii
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 96 - 96: iI11I1II1I1I
 o0O0O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 82 - 82: OOooOOo + o0o00Oo0O - III1iiIii % i1i1I1IIii1II * Ii
 if 15 - 15: I11i
 for iiIiI in o0O0O0 :
  o0Ooo0O00 = i1oOOOOOOOoO + iiIiI
  I1iI = O00O0oOO00O00 ( o0Ooo0O00 )
  if I1iI != 'Failed' :
   oO0Ooo0OooOOo = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( I1iI )
   for I1Ii , iIIIiIi in oO0Ooo0OooOOo :
    if o0OO in iIIIiIi . lower ( ) :
     OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( i1oOOOOOOOoO + iiIiI + I1Ii ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 71 - 71: III1iiIii + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 55 - 55: ii + i1IiiiI1iI + ii * i1iIi
def ii11i ( ) :
 oOoo000 ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 oOoo000 ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 oOoo000 ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 oOoo000 ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 68 - 68: o0o00Oo0O
def II1iIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , II11I , OoOOOOo , IiIi11Iii , OoOOOO0O0oO0 in IIi :
  oOoo000 ( ( '[COLORblue]' + iIIIiIi + '[/COLOR] [COLORred]Season[/COLOR]-' + II11I + ' [COLORred]Returns [/COLOR]- ' + OoOOOO0O0oO0 + ' ' + IiIi11Iii ) , iIIIiIi , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 15 - 15: i1iIi * OOooOOo % III1iiIii . OOooOOo . Iii
def o0ooO0OOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , II11I , OoOOOOo in IIi :
  oOoo000 ( ( '[COLORblue]' + iIIIiIi + '[/COLOR] [COLORred]Season[/COLOR]-' + II11I + ' [COLORred] Status Unknown[/COLOR] ' ) , iIIIiIi , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 74 - 74: o0ii1I * Ii / i1IiiiI1iI
def OoOoo00O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , II11I , OoOOOOo , IiIi11Iii in IIi :
  oOoo000 ( ( '[COLORblue]' + iIIIiIi + ' [COLORred] Cancelled On[/COLOR] ' + IiIi11Iii ) , iIIIiIi , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 29 - 29: I11i
def oo0 ( url ) :
 o0OO = ( url )
 Oo = o0OO . lower ( )
 if 2 - 2: ii
 if 60 - 60: oO0o
 II1IIIii = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( o0OO ) . replace ( ' ' , '+' )
 I1 = 'http://onlinemovies.tube/?s=' + ( o0OO ) . replace ( ' ' , '+' )
 IIiI = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 O0oOOo0o = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 ooOo0OoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 81 - 81: OOooOOo % o0ii1I
 iiI1I1IIi11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 i1II1iii1i = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 oo0i1iIIi1II1iiI = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 31 - 31: I11i % Iii + iI11I1II1I1I + Ii * i1IiiiI1iI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 45 - 45: oooOo0oo0oo * i1IiiiI1iI . i1iIi - i1IiiiI1iI + III1iiIii
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 34 - 34: oooOo0oo0oo . I1ii11iIi11i
 if 78 - 78: Ii1I % oOo0O0Ooo / ii % oooOo0oo0oo - IiI1i11I
 oo0o = O00O0oOO00O00 ( II1IIIii )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( I1 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( IIiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( O0oOOo0o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 I1iI = O00O0oOO00O00 ( ooOo0OoO )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 2 - 2: iI11I1II1I1I
 if 45 - 45: ii / Ii
 i1iiIIIi = O00O0oOO00O00 ( iiI1I1IIi11i1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 Oo0o = O00O0oOO00O00 ( i1II1iii1i )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 I11I1i1iI = O00O0oOO00O00 ( oo0i1iIIi1II1iiI )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 90 - 90: III1iiIii * IIiIiII11i % i1IiiiI1iI + i1i1I1IIii1II
 if Oo0o != 'Failed' :
  Iiii1ii = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oo0o )
  for url , iIIIiIi in Iiii1ii :
   I1i111IiIiIi1 = O00O0oOO00O00 ( url )
   i1II11II1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1i111IiIiIi1 )
   for II1IIIii , iIIIiIi1I1i in i1II11II1 :
    if Oo in iIIIiIi1I1i . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + II1IIIii , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 93 - 93: i1IiiiI1iI + o0ii1I
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if i1iiIIIi != 'Failed' :
  i1i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iiIIIi )
  for url , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in i1i1 :
   if Oo in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 27 - 27: i1IiiiI1iI + ii - OOooOOo
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 15 - 15: i1i1I1IIii1II / Iii * o0o00Oo0O . IIiIiII11i - oO0o
    if 90 - 90: i1i1I1IIii1II
    if 94 - 94: Iii / Ii1I * i1IiiiI1iI - OOooOOo
    if 44 - 44: o0ii1I % Ii - IiI1i11I * Ii1I + I1ii11iIi11i * oooOo0oo0oo
    if 41 - 41: o0o00Oo0O * i1iIi - OOooOOo . o0ii1I
    if 65 - 65: I1ii11iIi11i . ii
    if 70 - 70: I1ii11iIi11i - i1i1I1IIii1II . iI11I1II1I1I % Iii / OOooOOo - o0o00Oo0O
    if 55 - 55: IiI1i11I - oO0o
    if 100 - 100: o0o00Oo0O
    if 79 - 79: iI11I1II1I1I
    if 81 - 81: oooOo0oo0oo + iI11I1II1I1I * i1IiiiI1iI - iI11I1II1I1I . oooOo0oo0oo
 if I11I1i1iI != 'Failed' :
  I1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11I1i1iI )
  for url , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in I1ii :
   if Oo in iIIIiIi . lower ( ) :
    oOoo000 ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , iiiI1I1iIIIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 80 - 80: Ii1I / iI11I1II1I1I % OOooOOo
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  oO000o0Oo00 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , ooO0OO , iIIIiIi , OooO0O in i1Iii1i1I :
   if Oo in iIIIiIi . lower ( ) :
    if 'season' in OooO0O :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , ooO0OO , ooO0OO , '' )
    if 'episodes' in OooO0O :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , ooO0OO , ooO0OO , '' )
  for url in oO000o0Oo00 :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 44 - 44: o0o00Oo0O . i1i1I1IIii1II * Ii % Ii + o0o00Oo0O / oooOo0oo0oo
   I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  oOo0 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( oo0o )
  for url , iIIIiIi , ooO0OO in oOo0 :
   if Oo in iIIIiIi . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( iIIIiIi ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , ooO0OO , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 89 - 89: o0ii1I % ooOoO0O00 % i1i1I1IIii1II
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 53 - 53: i1i1I1IIii1II * ii . OOooOOo
    if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
    if 37 - 37: ooOoO0O00 - oooOo0oo0oo % ii / oooOo0oo0oo % i1iIi
    if 48 - 48: Ii % i1i1I1IIii1II
    if 29 - 29: IiI1i11I + Ii % Iii
    if 93 - 93: OOooOOo % iI11I1II1I1I
    if 90 - 90: oOo0O0Ooo - oooOo0oo0oo / o0ii1I / o0o00Oo0O / Iii
    if 87 - 87: OOooOOo / III1iiIii + iI11I1II1I1I
    if 93 - 93: iI11I1II1I1I + i1i1I1IIii1II % i1iIi
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for iIIIiIi in ii1I1IIii11 :
   if Oo in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( IIiI + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 21 - 21: oooOo0oo0oo
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for iIIIiIi in II1i11I :
   if Oo in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( O0oOOo0o + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 6 - 6: III1iiIii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if I1iI != 'Failed' :
  oO0Ooo0OooOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1iI )
  for url , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in oO0Ooo0OooOOo :
   if Oo in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 46 - 46: III1iiIii + i1i1I1IIii1II
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 79 - 79: ii - III1iiIii * III1iiIii . OOooOOo
 Oo00ooO0OoOo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for iiIiI in Oo00ooO0OoOo :
  o0Ooo0O00 = oO0 + iiIiI + oOoOooOo0o0
  Ooo0oO0 = O00O0oOO00O00 ( o0Ooo0O00 )
  if Ooo0oO0 != 'Failed' :
   iiIii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Ooo0oO0 )
   for iIIIiIi , O000OOO , url , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in iiIii :
    if Oo in iIIIiIi . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , url , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 99 - 99: OOooOOo
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 77 - 77: I11i
     if 48 - 48: OOooOOo % Ii1I / Iii . iI11I1II1I1I * IIiIiII11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 65 - 65: OOooOOo
def I1iI11I1III1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( ( iIIIiIi ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + oOOo0O00o , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + oOOo0O00o )
def IiIi1 ( url ) :
 Oo00o000oOO = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( Oo00o000oOO )
 sys . exit ( 1 )
 if 37 - 37: o0o00Oo0O - Iii
def IiI1 ( ) :
 if 59 - 59: Iii / I1ii11iIi11i / oooOo0oo0oo / o0o00Oo0O / OOooOOo + I11i
 if 13 - 13: I11i % i1i1I1IIii1II / i1IiiiI1iI % i1IiiiI1iI % o0o00Oo0O
 if 90 - 90: III1iiIii . i1iIi / iI11I1II1I1I
 if 28 - 28: III1iiIii + i1i1I1IIii1II - i1iIi / iI11I1II1I1I - oOo0O0Ooo
 if 45 - 45: o0o00Oo0O / ooOoO0O00 * i1i1I1IIii1II * oO0o
 if 35 - 35: Ii1I / IiI1i11I % oOo0O0Ooo + iI11I1II1I1I
 if 79 - 79: OOooOOo / i1iIi
 if 77 - 77: I1ii11iIi11i
 if 46 - 46: i1IiiiI1iI
 if 72 - 72: IiI1i11I * oooOo0oo0oo
 if 67 - 67: ooOoO0O00
 oOoo000 ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 oOoo000 ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 oOoo000 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 5 - 5: IIiIiII11i . ii
def oOOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , IIiIii in IIi :
  oOoo000 ( ( iIIIiIi + ' - ' + IIiIii ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 74 - 74: Iii / IIiIiII11i + i1iIi * iI11I1II1I1I - i1IiiiI1iI - oO0o
def OoOoO0OooOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 94 - 94: I11i . oO0o
def oooO00Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  oOoo000 ( iIIIiIi , url , 90054 , ooO0OO )
 for url in next :
  oOoo000 ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 86 - 86: IIiIiII11i + i1iIi + III1iiIii
def I11i11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for ooO0OO , IIiIii , url , iIIIiIi , oooO00o00 in IIi :
  I1I1II1I11 ( IIiIii + ' - ' + iIIIiIi + ' - ' + oooO00o00 , url , 90044 , ooO0OO , ooO0OO , '' )
 for ooO0OO , iIIIiIi , url in i1Iii1i1I :
  oOoo000 ( iIIIiIi , url , 90044 , ooO0OO , ooO0OO , '' )
 for url in next :
  oOoo000 ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 9 - 9: oO0o * Iii - o0ii1I
def iIi11i ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://onlinemovies.tube/?s=' + ( o0OO ) . replace ( ' ' , '+' )
 Oo = ooIII1II1iii1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( Oo )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi , OooO0O in IIi :
  if 'season' in OooO0O :
   oOoo000 ( iIIIiIi , oOOo0O00o , 90054 , ooO0OO , ooO0OO , '' )
  if 'episodes' in OooO0O :
   oOoo000 ( iIIIiIi , oOOo0O00o , 90044 , ooO0OO , ooO0OO , '' )
 for oOOo0O00o in next :
  oOoo000 ( 'NEXT' , oOOo0O00o , 90053 , iiIi1IIiIi + 'Next.png' )
  if 75 - 75: III1iiIii - OOooOOo - iI11I1II1I1I % I11i
def OooooO ( ) :
 if 92 - 92: I11i / I11i * o0ii1I
 if 19 - 19: o0ii1I
 if 55 - 55: oooOo0oo0oo % oooOo0oo0oo / o0o00Oo0O % IiI1i11I - I11i . I1ii11iIi11i
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
 if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
 if 8 - 8: OOooOOo * I1ii11iIi11i / III1iiIii % o0ii1I - oOo0O0Ooo
 if 71 - 71: IiI1i11I
 if 23 - 23: ooOoO0O00 . iI11I1II1I1I . oooOo0oo0oo . o0o00Oo0O % o0ii1I % Ii
 if 11 - 11: o0o00Oo0O - IIiIiII11i . oooOo0oo0oo . o0ii1I % i1IiiiI1iI
 if 21 - 21: I1ii11iIi11i / IiI1i11I . i1IiiiI1iI * ii + Iii - ooOoO0O00
 oOoo000 ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 oOoo000 ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 oOoo000 ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 oOoo000 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 58 - 58: Ii1I
def ii1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , IIiIii in IIi :
  if 'genre' in url :
   oOoo000 ( ( iIIIiIi + ' - ' + IIiIii ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 98 - 98: ooOoO0O00
def OOO0oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'release' in url :
   oOoo000 ( iIIIiIi , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 38 - 38: iI11I1II1I1I / i1iIi
def i11oooOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , oo0oo0O0 , url , O000OOO in IIi :
  I1I1II1I11 ( iIIIiIi + ' ' + oo0oo0O0 , url , 90044 , ooO0OO , ooO0OO , O000OOO )
 for ooO0OO , iIIIiIi , OooO0O , url , IiIIiiI , O000OOO in i1Iii1i1I :
  if 'movies' in OooO0O :
   I1I1II1I11 ( iIIIiIi + ' - ' + IiIIiiI , url , 90044 , ooO0OO , ooO0OO , O000OOO )
 for url in next :
  oOoo000 ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 60 - 60: i1IiiiI1iI
def oOO0o00o0Oo0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iIIi1iiII ( 'http:' + url )
  if 14 - 14: o0o00Oo0O
def iIIi1iiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  OooOo00o ( ( iIIIiIi ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def II1iIii111iII ( ) :
 if 27 - 27: I11i * Ii * oO0o
 if 92 - 92: I1ii11iIi11i / Ii + Ii1I
 if 87 - 87: OOooOOo % iI11I1II1I1I
 if 72 - 72: oooOo0oo0oo . oooOo0oo0oo - Ii1I
 if 48 - 48: I1ii11iIi11i - i1iIi + I1ii11iIi11i - oOo0O0Ooo * Ii . IiI1i11I
 if 35 - 35: III1iiIii . o0o00Oo0O + I1ii11iIi11i + oooOo0oo0oo + ooOoO0O00
 if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
 if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
 if 58 - 58: oooOo0oo0oo . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
 if 50 - 50: IiI1i11I % IIiIiII11i - i1iIi . ooOoO0O00 + o0o00Oo0O % IiI1i11I
 if 10 - 10: IiI1i11I . ooOoO0O00 + o0ii1I
 if 66 - 66: oO0o % I11i
 if 21 - 21: OOooOOo - ii % Ii
 if 71 - 71: ooOoO0O00 - Iii * i1IiiiI1iI + i1i1I1IIii1II - oO0o % Ii1I
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://onlinemovies.tube/?s=' + ( o0OO ) . replace ( ' ' , '+' )
 Oo = ooIII1II1iii1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( Oo )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi , Ooo0oO in IIi :
  if 'movies' in Ooo0oO :
   oOoo000 ( Ooo0oO + '-' + iIIIiIi , oOOo0O00o , 90044 , ooO0OO )
 for oOOo0O00o in next :
  i11oooOo ( oOOo0O00o )
  if 32 - 32: ooOoO0O00 . IiI1i11I + IIiIiII11i - oO0o - iI11I1II1I1I
def III1i11 ( ) :
 oOoo000 ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 80006 , iiIi1IIiIi + 'Desi.png' )
def iIIIIiiii1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  OooOo00o ( iIIIiIi , url , 80007 , ooO0OO )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def IIi1iI11IIIi1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  I11iiiiI1i ( url )
def o00O0o0oo0oOO0oO ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://www.join4films.com/?s=' + ( o0OO ) . replace ( ' ' , '+' ) + '&search_type=1'
 Oo = ooIII1II1iii1i . lower ( )
 iIIIIiiii1I ( Oo )
 if 15 - 15: oO0o * IIiIiII11i
 if 59 - 59: i1IiiiI1iI + oO0o / oooOo0oo0oo
 if 97 - 97: I1ii11iIi11i * IiI1i11I % i1iIi . IiI1i11I - i1IiiiI1iI - oooOo0oo0oo
 if 79 - 79: oOo0O0Ooo - i1iIi
 if 37 - 37: III1iiIii . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
 if 83 - 83: III1iiIii / i1IiiiI1iI
 if 64 - 64: oO0o % III1iiIii . i1IiiiI1iI % oO0o + Iii * III1iiIii
 if 83 - 83: I11i % i1i1I1IIii1II + Iii % Ii + o0o00Oo0O
 if 65 - 65: iI11I1II1I1I % i1i1I1IIii1II + o0o00Oo0O / ii
 if 52 - 52: o0ii1I % oooOo0oo0oo * oOo0O0Ooo % Iii + oooOo0oo0oo / IiI1i11I
 if 80 - 80: ii + III1iiIii
 if 95 - 95: i1IiiiI1iI / i1i1I1IIii1II * i1IiiiI1iI - ii * ii % oO0o
 if 43 - 43: I1ii11iIi11i . i1IiiiI1iI
 if 12 - 12: i1IiiiI1iI + oooOo0oo0oo + Iii . III1iiIii / o0ii1I
 if 29 - 29: III1iiIii . i1iIi - IIiIiII11i
 if 68 - 68: iI11I1II1I1I + IIiIiII11i / i1i1I1IIii1II
 if 91 - 91: OOooOOo % iI11I1II1I1I . oOo0O0Ooo
def O00ooooo00 ( ) :
 I1I1II1I11 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 94 - 94: Iii - IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + Ii1I * Ii1I
def I1iiIiiii1111 ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://imoviemax.se/?s=' + ( o0OO ) . replace ( ' ' , '+' )
 Oo = ooIII1II1iii1i . lower ( )
 I1ii1i11i ( Oo )
def Oooooo0O00o ( url ) :
 II11ii1 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ii1II1II in IIi :
  if iIIIiIi in II11ii1 :
   pass
  else :
   I1I1II1I11 ( iIIIiIi + ' - ' + ii1II1II + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   II11ii1 . append ( iIIIiIi )
   if 42 - 42: o0ii1I
def O0o00oo0OO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , oO0o000OooOoo in IIi :
  I1I1II1I11 ( iIIIiIi + ' - Views:' + oO0o000OooOoo , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 8 - 8: I1ii11iIi11i + i1iIi / o0o00Oo0O * ii * IIiIiII11i % o0ii1I
  if 66 - 66: OOooOOo
def I1ii1i11i ( url ) :
 I1iI1 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  I1I1II1I11 ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  I1I1II1I11 ( iIIIiIi , url , 10075 , ooO0OO , ooO0OO , '' )
  I1iI1 . append ( iIIIiIi )
  if 52 - 52: OOooOOo * oO0o - o0ii1I
def OOoOOo0 ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for iIiI1Iii1 , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  Ooooo = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + Ooooo
  iIiiiIiIi = ( iIiI1Iii1 ) . replace ( 'play-' , 'Server ' )
  Ii1I1i ( iIiiiIiIi , Ooooo , 10076 , img , img , '' )
  if 19 - 19: III1iiIii . Ii1I / OOooOOo
def O00oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for I1 in IIi :
  if '=m' in I1 :
   OoOoooO000OO ( I1 )
  elif 'php' in I1 :
   O00oo ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( I1 )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for IIiI in IIi :
    OoOoooO000OO ( I1 )
    if 62 - 62: oooOo0oo0oo + I1ii11iIi11i % iI11I1II1I1I / iI11I1II1I1I . i1iIi . III1iiIii
    if 21 - 21: oO0o - o0ii1I - oOo0O0Ooo / OOooOOo
    if 48 - 48: ii
def II1IiI1iiI111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OoOOOO00 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11Iii , IIii1III in OoOOOO00 :
  print 'there ><><><><><><><><><><><><'
  IiIi11Iii = IiIi11Iii
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIii1III ) )
  for iIIIiIi , ooooOoo0OO in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + IiIi11Iii + '[/COLOR] - ' + iIIIiIi + ' - [COLOR' + ooOoOoo0O + ']' + ooooOoo0OO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 i1i1i1I = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi11Iii , Oo0 in i1i1i1I :
  print 'there ><><><><><><><><><><><><'
  IiIi11Iii = IiIi11Iii
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Oo0 ) )
  for iIIIiIi , ooooOoo0OO in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + IiIi11Iii + '[/COLOR] - ' + iIIIiIi + ' - [COLOR' + ooOoOoo0O + ']' + ooooOoo0OO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 96 - 96: Iii % o0ii1I % i1i1I1IIii1II * Iii / oooOo0oo0oo
   if 13 - 13: iI11I1II1I1I - oO0o
   if 100 - 100: Ii / Ii
def O00oO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1i1i1I in i1i1i1I :
  iIIIiIi = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
  for iIIIiIi in iIIIiIi :
   iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1i1i1I ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  o000O000 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
  for o000O000 in o000O000 :
   o000O000 = 'http:' + o000O000
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , '' , '' )
  if 89 - 89: IiI1i11I . Ii * o0o00Oo0O
  if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + III1iiIii
  if 27 - 27: oooOo0oo0oo
  if 52 - 52: i1IiiiI1iI % OOooOOo + iI11I1II1I1I * i1i1I1IIii1II . o0ii1I
def iiI111 ( url ) :
 if 95 - 95: iI11I1II1I1I . III1iiIii - ii * oO0o / I11i
 oOo0OO0o0 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1 , ooO0OO , iIIIiIi , II1I1I in IIi :
  iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( I1 )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for O0O0OOooOO0 , O0o in i1Iii1i1I :
   III11I = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( O0o ) )
   for O000OOO in III11I :
    if iIIIiIi in oOo0OO0o0 :
     pass
    else :
     Ii1I1i ( iIIIiIi , O0O0OOooOO0 , 8043 , ooO0OO , ooO0OO , O000OOO )
     I1iI1ii1II ( 'movies' , 'INFO' )
     oOo0OO0o0 . append ( iIIIiIi )
     if 3 - 3: Ii
     if 81 - 81: oOo0O0Ooo . ii * o0ii1I . i1i1I1IIii1II - o0o00Oo0O * i1i1I1IIii1II
def OoO0Oo00 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , iiiI1I1iIIIi1 , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
  I1I1II1I11 ( iIIIiIi , url , 10065 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O000OOO )
 I1iI1ii1II ( 'movies' , 'INFO' )
 if 1 - 1: i1IiiiI1iI - Iii
def i1I111Ii ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'https://www.youtube.com/results?search_query=' + ( o0OO ) . replace ( ' ' , '+' )
 Oo = ooIII1II1iii1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( Oo )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in next :
  oOOo0O00o = 'https://www.youtube.com' + oOOo0O00o
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , oOOo0O00o , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for ooO0OO , oOOo0O00o , iIIIiIi , i11i1i , O0o in IIi :
  OOO00 . append ( iIIIiIi )
  I1iI1ii1II ( 'tvshows' , 'INFO' )
  o000O000 = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + o000O000
  oOOo0O00o = 'http://www.youtube.com' + oOOo0O00o
  Ii1I1i ( '[COLORred]' + i11i1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , o000O000 , O0o )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for ooO0OO , oOOo0O00o , iIIIiIi , i11i1i in IIi :
   print 'im doing it'
   I1iI1ii1II ( 'tvshows' , 'INFO' )
   o000O000 = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
   oOOo0O00o = 'http://www.youtube.com' + oOOo0O00o
   if '&' in oOOo0O00o :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( oOOo0O00o )
    i1i1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for i1i1i1I in i1i1i1I :
     iIIIiIi = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for iIIIiIi in iIIIiIi :
      iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oOOo0O00o = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1i1i1I ) )
     for oOOo0O00o in oOOo0O00o :
      oOOo0O00o = 'https://www.youtube.com/w' + oOOo0O00o
     o000O000 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for o000O000 in o000O000 :
      o000O000 = 'http:' + o000O000
     Ii1I1i ( '[COLORred]' + i11i1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , Oo00OOOOO , '' )
   elif iIIIiIi in OOO00 :
    pass
   elif 'user' in oOOo0O00o or 'elete' in iIIIiIi :
    pass
   elif 'hannel' in oOOo0O00o :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oOOo0O00o
    II11iIiIIIiI = OooOoooOo ( oOOo0O00o )
    I1ii1Ii1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for ooO0OO , oOOo0O00o , iIIIiIi in I1ii1Ii1 :
     if 'outube' in oOOo0O00o or 'list' in oOOo0O00o :
      pass
     elif 'atch' in oOOo0O00o :
      oOOo0O00o = ( oOOo0O00o ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + i11i1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ooO0OO , 'http:' + ooO0OO , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + i11i1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , o000O000 , '' )
    if 73 - 73: o0o00Oo0O . i1i1I1IIii1II + Ii + iI11I1II1I1I - Iii / OOooOOo
def OO0OOOOo0000O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for ooO0OO , url , iIIIiIi , i11i1i , O0o in IIi :
  OOO00 . append ( iIIIiIi )
  I1iI1ii1II ( 'tvshows' , 'INFO' )
  o000O000 = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + o000O000
  url = 'http://www.youtube.com' + url
  Ii1I1i ( '[COLORred]' + i11i1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , o000O000 , O0o )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for ooO0OO , url , iIIIiIi , i11i1i in IIi :
   I1iI1ii1II ( 'tvshows' , 'INFO' )
   o000O000 = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    i1i1i1I = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for i1i1i1I in i1i1i1I :
     iIIIiIi = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for iIIIiIi in iIIIiIi :
      iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( i1i1i1I ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     o000O000 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( i1i1i1I ) )
     for o000O000 in o000O000 :
      o000O000 = 'http:' + o000O000
     Ii1I1i ( '[COLORred]' + i11i1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , Oo00OOOOO , '' )
   elif iIIIiIi in OOO00 :
    pass
   elif 'user' in url or 'elete' in iIIIiIi :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    I1ii1Ii1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for ooO0OO , url , iIIIiIi in I1ii1Ii1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + i11i1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ooO0OO , 'http:' + ooO0OO , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + i11i1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 , o000O000 , '' )
    if 25 - 25: IiI1i11I - I1ii11iIi11i
    if 10 - 10: o0o00Oo0O % III1iiIii . oO0o + I11i + Ii1I
    if 52 - 52: OOooOOo / oO0o + i1IiiiI1iI
def Iii1i11iiI1 ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 95 - 95: i1i1I1IIii1II * iI11I1II1I1I + Ii1I
def i1iI1i ( ) :
 ivuesetup . iVueInt ( )
 if 59 - 59: III1iiIii
def oOoO0OOO00O ( ) :
 OOOOO0o0OOo ( )
 return
 if 40 - 40: III1iiIii * i1i1I1IIii1II % Iii * Ii1I
def OOOOO0o0OOo ( ) :
 if 80 - 80: iI11I1II1I1I - ii - Ii1I - Ii1I . ii
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 I1iI11I = II1I . getSetting ( id = 'User' )
 Oo0oOO = II1I . getSetting ( id = 'Pass' )
 ooooo = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 iIiIi = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 iiIiI1 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 iII1IiiIIII = "http://piesustv.net:8000/get.php?username=" + I1iI11I + "&password=" + Oo0oOO + "&type=m3u_plus&output=ts"
 I11iI = "http://piesustv.net:8000/xmltv.php?username=" + I1iI11I + "&password=" + Oo0oOO + "&type=m3u_plus&output=ts"
 if 79 - 79: o0o00Oo0O + i1i1I1IIii1II
 xbmc . executeJSONRPC ( ooooo )
 xbmc . executeJSONRPC ( iIiIi )
 xbmc . executeJSONRPC ( iiIiI1 )
 if 21 - 21: i1iIi + I11i % i1IiiiI1iI + Ii + IiI1i11I + IIiIiII11i
 oOO0OOOOOo0Oo = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 oOO0OOOOOo0Oo . setSetting ( id = 'm3uUrl' , value = iII1IiiIIII )
 oOO0OOOOOo0Oo . setSetting ( id = 'epgUrl' , value = I11iI )
 oOO0OOOOOo0Oo . setSetting ( id = 'm3uCache' , value = "false" )
 oOO0OOOOOo0Oo . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def iIiIi1Ii1Ii1IIIi ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 70 - 70: OOooOOo . oooOo0oo0oo * III1iiIii + Iii
if 77 - 77: i1i1I1IIii1II % Ii . oooOo0oo0oo % oooOo0oo0oo
if 36 - 36: I1ii11iIi11i % o0ii1I / Ii % i1IiiiI1iI + oO0o
def i1IiI ( ) :
 if 31 - 31: OOooOOo / IIiIiII11i + Iii * ii / IiI1i11I
 if 40 - 40: OOooOOo - oooOo0oo0oo - oooOo0oo0oo - o0o00Oo0O - o0o00Oo0O . IIiIiII11i
 if 57 - 57: o0ii1I - ii
 if 68 - 68: I11i % Ii1I / i1IiiiI1iI + i1IiiiI1iI - i1IiiiI1iI . oO0o
 if 100 - 100: OOooOOo % I1ii11iIi11i
 if 76 - 76: IIiIiII11i / oO0o + ii . Ii1I . Iii . i1iIi
 if 43 - 43: ooOoO0O00
 if 17 - 17: o0o00Oo0O - OOooOOo
 if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
 if 34 - 34: o0ii1I * o0ii1I - Ii1I - o0o00Oo0O . Ii
 if 32 - 32: iI11I1II1I1I . oO0o * i1i1I1IIii1II / oooOo0oo0oo . IIiIiII11i - I1ii11iIi11i
 if 10 - 10: Ii1I / Ii - o0ii1I + i1i1I1IIii1II * oOo0O0Ooo
 if OO0o == "insert_username" :
  OoooOo0 = IiI1Ii1ii ( )
  Ii11iiIIiI1 = I1Iii11I111I ( )
  I11 ( 'User' , OoooOo0 )
  I11 ( 'Pass' , Ii11iiIIiI1 )
  xbmc . executebuiltin ( 'Container.Refresh' )
  IIIiI1iiiiiIi = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( OoooOo0 , Ii11iiIIiI1 )
  IIIiI1iiiiiIi = OooOoooOo ( IIIiI1iiiiiIi )
  if IIIiI1iiiiiIi == "" :
   O0oo0 = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   iii1iiii11I = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   o0oO0o0oo0O0 = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , O0oo0 , iii1iiii11I , o0oO0o0oo0O0 )
   i1IiI ( )
  else :
   O0oo0 = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   iii1iiii11I = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   o0oO0o0oo0O0 = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % OoooOo0 )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , O0oo0 , iii1iiii11I , o0oO0o0oo0O0 )
   xbmc . executebuiltin ( 'Container.Refresh' )
   O0oo00oOOO0o ( )
 else :
  O0oo00oOOO0o ( )
def IiI1Ii1ii ( ) :
 II1i = xbmc . Keyboard ( '' , 'heading' , True )
 II1i . setHeading ( 'Enter Username' )
 II1i . setHiddenInput ( False )
 II1i . doModal ( )
 if ( II1i . isConfirmed ( ) ) :
  I111iiIIiI1I = II1i . getText ( )
  return I111iiIIiI1I
 else :
  return False
  if 51 - 51: oOo0O0Ooo + oooOo0oo0oo + Iii
  if 50 - 50: i1IiiiI1iI + Ii1I
def I1Iii11I111I ( ) :
 II1i = xbmc . Keyboard ( '' , 'heading' , True )
 II1i . setHeading ( 'Enter Password' )
 II1i . setHiddenInput ( False )
 II1i . doModal ( )
 if ( II1i . isConfirmed ( ) ) :
  I111iiIIiI1I = II1i . getText ( )
  return I111iiIIiI1I
 else :
  return False
def i1IiOOOooOOOOOOOO ( ) :
 iII1IiiIIII = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  oooOOo = urllib2 . urlopen ( iII1IiiIIII )
  print oooOOo . getcode ( )
  oooOOo . close ( )
  if 85 - 85: o0ii1I - o0o00Oo0O * Ii . ooOoO0O00
  pass
  if 20 - 20: IiI1i11I / oooOo0oo0oo
 except urllib2 . HTTPError , Ooo0O0oooo :
  print Ooo0O0oooo . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def O0oo00oOOO0o ( ) :
 iii ( )
 if 28 - 28: i1iIi * Iii % Ii * IiI1i11I / o0ii1I
 if 41 - 41: oooOo0oo0oo - I11i + o0ii1I
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 15 - 15: Iii / I11i + o0ii1I
 if 76 - 76: o0ii1I + ii / oooOo0oo0oo % oO0o / Ii1I
 if 38 - 38: i1IiiiI1iI . IiI1i11I . oOo0O0Ooo * oO0o
 if 69 - 69: I11i % Ii / o0ii1I
def ooOOO00oOOooO ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 IiIIii1iiI = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 ii1IiiII = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 IIIiI1iiiiiIi = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 IIIiI1iiiiiIi = OooOoooOo ( IIIiI1iiiiiIi )
 if not IIIiI1iiiiiIi == "" :
  IiiI1II1II1i = 'https://tinyurl.com/create.php?source=indexpage&url=' + IiIIii1iiI + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( IiiI1II1II1i ) )
  iIO0OO0o0O00oO = 'https://tinyurl.com/create.php?source=indexpage&url=' + ii1IiiII + '&submit=Make+TinyURL%21&alias='
  IiIIii1iiI = OooOoooOo ( IiiI1II1II1i )
  ii1IiiII = OooOoooOo ( iIO0OO0o0O00oO )
  xbmc . log ( str ( ii1IiiII ) )
  o00O = oO0o0oOo ( IiIIii1iiI , '<div class="indent"><b>' , '</b>' )
  OoO0O0oo0o = oO0o0oOo ( ii1IiiII , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % o00O , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % OoO0O0oo0o )
 else :
  return
def iIi11I11 ( ) :
 i1IiOOOooOOOOOOOO ( )
 i1ioO ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , I11iiI + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( i1iIii1i111 )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  I1I1II1I11 ( ( '[COLORsteelblue]' + iIIIiIi + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOOo0O00o , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def OOooo000OooO ( url ) :
 open = OooOoooOo ( o0o0 + url )
 OoOo = IiI1iiIiII ( open , '<channel>' , '</channel>' )
 for IIiiiI1iI in OoOo :
  if '<playlist_url>' in open :
   iIIIiIi = oO0o0oOo ( IIiiiI1iI , '<title>' , '</title>' )
   II1IIIii = oO0o0oOo ( IIiiiI1iI , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   I1I1II1I11 ( str ( base64 . b64decode ( iIIIiIi ) ) . replace ( '?' , '' ) , II1IIIii , 3 , icon , IIo0o0O0O00oOOo , '' )
  else :
   iIIIiIi = oO0o0oOo ( IIiiiI1iI , '<title>' , '</title>' )
   iIIIiIi = base64 . b64decode ( iIIIiIi )
   O0O0O0oO0o0OOOOOO = oO0o0oOo ( IIiiiI1iI , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = oO0o0oOo ( IIiiiI1iI , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   O000OOO = oO0o0oOo ( IIiiiI1iI , '<description>' , '</description>' )
   O000OOO = base64 . b64decode ( O000OOO )
   IiI1i11IiIiii = oO0o0oOo ( O000OOO , 'PLOT:' , '\n' )
   I11iiI1I1 = oO0o0oOo ( O000OOO , 'CAST:' , '\n' )
   o0i1Ii11II = oO0o0oOo ( O000OOO , 'RATING:' , '\n' )
   i1iiiiI11ii = oO0o0oOo ( O000OOO , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   i1iiiiI11ii = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( i1iiiiI11ii )
   oooooOOo0o = oO0o0oOo ( O000OOO , 'DURATION_SECS:' , '\n' )
   oOO0 = oO0o0oOo ( O000OOO , 'GENRE:' , '\n' )
   OoO000Oo0oO ( str ( iIIIiIi ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , O0O0O0oO0o0OOOOOO , IIo0o0O0O00oOOo , IiI1i11IiIiii , str ( i1iiiiI11ii ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( I11iiI1I1 ) . split ( ) , o0i1Ii11II , oooooOOo0o , oOO0 )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 46 - 46: o0o00Oo0O - OOooOOo . ii
i1I111II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
Oo0OOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 44 - 44: Iii * I11i
def II11ii1I11 ( ) :
 iII1IiiIIII = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  oooOOo = urllib2 . urlopen ( iII1IiiIIII )
  print oooOOo . getcode ( )
  oooOOo . close ( )
  if 65 - 65: oooOo0oo0oo + IIiIiII11i
  pass
  if 61 - 61: Ii * i1i1I1IIii1II % I1ii11iIi11i * i1IiiiI1iI - ii - oO0o
 except urllib2 . HTTPError , Ooo0O0oooo :
  print Ooo0O0oooo . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 83 - 83: i1iIi / oooOo0oo0oo
 oOOo0O00o = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 i11iI1 ( oOOo0O00o , Oo0OOo + "uide.xml" )
 if 35 - 35: Iii
 O0oO0 = open ( i1I111II , 'r+' )
 input = open ( i1I111II ) . read ( ) . decode ( 'UTF-8' )
 o00oo = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 O0oO0 . write ( o00oo )
 O0oO0 . truncate ( )
 O0oO0 . close ( )
 O0oO0oo0O ( )
 if 82 - 82: ii . o0ii1I
def O0oO0oo0O ( ) :
 open = OooOoooOo ( III1ii )
 all = IiI1iiIiII ( open , '{"num' , 'direct' )
 for IIiiiI1iI in all :
  if '"tv_archive":1' in IIiiiI1iI :
   iIIIiIi = oO0o0oOo ( IIiiiI1iI , '"epg_channel_id":"' , '"' )
   O0O0O0oO0o0OOOOOO = oO0o0oOo ( IIiiiI1iI , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = oO0o0oOo ( IIiiiI1iI , 'stream_id":"' , '"' )
   iIIIiIi = iIIIiIi . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   I1I1II1I11 ( iIIIiIi , id , 90027 , O0O0O0oO0o0OOOOOO , IIo0o0O0O00oOOo , iIIIiIi )
   if 38 - 38: Ii1I + OOooOOo
   if 68 - 68: o0o00Oo0O
def o0oOoO00 ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 oOO000 = open ( i1I111II )
 OoOooO = ElementTree . parse ( oOO000 )
 OoO0o00OOOOO = "apples"
 import datetime as dt
 from datetime import time
 I1iIi1iIIIIiI = datetime . now ( ) - timedelta ( days = 5 )
 IiIi11Iii = str ( I1iIi1iIIIIiI )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 O000oooOO0Oo0 = OoOooO . findall ( "programme" )
 for I1iIiIii in O000oooOO0Oo0 :
  if name in I1iIiIii . attrib . get ( 'channel' ) :
   OO0 = I1iIiIii . attrib . get ( 'start' )
   I1iiI1iiI1i1 , OOOO00OOO00 , ii1OO0 = OO0 . partition ( ' +' )
   IiIi11Iii = str ( IiIi11Iii ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   i1iiiiI11ii , OoOoO00OOoOOOo0 , OoOOOO0O0oO0 = OO0 . partition ( '2017' )
   oOoO00O = I1iIiIii . find ( 'title' ) . text + OO0
   OoOOOO0O0oO0 = OoOOOO0O0oO0 [ : - 6 ]
   if I1iiI1iiI1i1 > IiIi11Iii :
    if I1iiI1iiI1i1 < I1IIIii :
     I11I1I1i1i = I1iiI1iiI1i1
     I11I1I1i1i = I11I1I1i1i [ : 4 ] + '/' + I11I1I1i1i [ 4 : ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : 4 ] + '-' + I1iiI1iiI1i1 [ 4 : ]
     I11I1I1i1i = I11I1I1i1i [ : 7 ] + '/' + I11I1I1i1i [ 7 : ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : 7 ] + '-' + I1iiI1iiI1i1 [ 7 : ]
     I11I1I1i1i = I11I1I1i1i [ : 10 ] + ' - ' + I11I1I1i1i [ 10 : ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : 10 ] + ':' + I1iiI1iiI1i1 [ 10 : ]
     I11I1I1i1i = I11I1I1i1i [ : 15 ] + ':' + I11I1I1i1i [ 15 : ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : 13 ] + '-' + I1iiI1iiI1i1 [ 13 : ]
     I11I1I1i1i = I11I1I1i1i [ : - 2 ]
     I1iiI1iiI1i1 = I1iiI1iiI1i1 [ : - 2 ]
     Oo0oOO0O00 = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( I1iiI1iiI1i1 ) + "&duration=240" + "&stream=%s" ) % ( OO0o , Ooo , id )
     OoO0o00OOOOO = Oo0oOO0O00 + str ( I1iiI1iiI1i1 ) + "&duration=240"
     I11I1I1i1i = '[COLOR blue]%s - [/COLOR]' % I11I1I1i1i
     oOoO00O = str ( I11I1I1i1i ) + I1iIiIii . find ( 'title' ) . text
     O000OOO = I1iIiIii . find ( 'desc' ) . text
     Ii1I1i ( oOoO00O , Oo0oOO0O00 , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , O000OOO )
def o00OOo0o0O ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OO0o ) . replace ( 'PASSWORD' , Ooo )
 iiIIIiIii = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 iiIIIiIii . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 iiIIIiIii . setProperty ( 'IsPlayable' , 'true' )
 iiIIIiIii . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiIIIiIii )
def i11iI1 ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 I111Iii1 = time . time ( )
 urllib . urlretrieve ( url , dest , lambda i11i , O0o0O00o0o , II1IIiiI1 : O00O00 ( i11i , O0o0O00o0o , II1IIiiI1 , o0oOoO00o , I111Iii1 ) )
def O00O00 ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  oOooO0OoO = min ( numblocks * blocksize * 100 / filesize , 100 )
  o0oOOOOoo0 = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  ooOO0OOO00o = numblocks * blocksize / ( time . time ( ) - start_time )
  if ooOO0OOO00o > 0 :
   OoOoO0ooooO0 = ( filesize - numblocks * blocksize ) / ooOO0OOO00o
  else :
   OoOoO0ooooO0 = 0
  ooOO0OOO00o = ooOO0OOO00o / 1024
  IIII1ii1 = ooOO0OOO00o / 1024
  OOO0O0OOo = float ( filesize ) / ( 1024 * 1024 )
  Iii1 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( o0oOOOOoo0 )
  Ooo0O0oooo = '[COLOR white]Speed:  %.02f Mb/s ' % IIII1ii1 + '[/COLOR]'
  dp . update ( oOooO0OoO , Iii1 , Ooo0O0oooo )
 except :
  oOooO0OoO = 100
  dp . update ( oOooO0OoO )
 if dp . iscanceled ( ) :
  OOoO = xbmcgui . Dialog ( )
  OOoO . ok ( "GenieTv" , 'The download was cancelled.' )
  if 8 - 8: i1IiiiI1iI + oO0o
  sys . exit ( )
  dp . close ( )
  if 9 - 9: oooOo0oo0oo + I11i
def I1iII1IIi1IiI ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  iIioo0ooO ( )
  if 97 - 97: i1IiiiI1iI . Iii / oOo0O0Ooo
  if 83 - 83: Iii - Ii1I * i1i1I1IIii1II
  if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
  if 75 - 75: Ii1I - OOooOOo * Ii . ii - I1ii11iIi11i . Iii
  if 6 - 6: Iii * i1i1I1IIii1II / ii % o0ii1I * I11i
  if 28 - 28: III1iiIii * oOo0O0Ooo % III1iiIii
  if 95 - 95: o0o00Oo0O / Iii . i1IiiiI1iI
  if 17 - 17: Iii
def iIioo0ooO ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for oOOo0O00o in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def o0OO0OO000OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 O00o0000OO = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 oOo0 = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 ii1I1IIii11 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 II1i11I = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 II1i11I1 = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 oO0Ooo0OooOOo = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 OooOo000o0o = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 O0Ooo0O0OO = iiI1iiii1Iii ( )
 OoOOOOOoOo0 = iIioOo ( )
 for url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in O00o0000OO :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in oOo0 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in II1i11I :
  dt = datetime . fromtimestamp ( float ( II1i11I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   OooOo00o ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in ii1I1IIii11 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in II1i11I1 :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in oO0Ooo0OooOOo :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OooOo000o0o :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + O0Ooo0O0OO , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + OoOOOOOoOo0 , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 66 - 66: IIiIiII11i + oO0o
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 19 - 19: oO0o . ii * oO0o + III1iiIii + ii
def i11iiI ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 oO00o00 ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 51 - 51: I1ii11iIi11i * iI11I1II1I1I . ii . o0ii1I - oooOo0oo0oo / oOo0O0Ooo
def OoO0ooOI1i1i111Ii1I ( data ) :
 oo0oooOoOoOO = len ( data ) % 4
 if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
 if 5 - 5: Iii
 if 22 - 22: iI11I1II1I1I * i1IiiiI1iI / I1ii11iIi11i
 if 31 - 31: Ii
 if 56 - 56: Iii / o0ii1I + I1ii11iIi11i - ooOoO0O00 - III1iiIii + iI11I1II1I1I
 if 75 - 75: Ii1I
 if oo0oooOoOoOO != 0 :
  data += b'=' * ( 4 - oo0oooOoOoOO )
 return base64 . decodestring ( data )
def oO0o0oOo ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : O00o = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : O00o = ''
 else :
  try : O00o = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : O00o = ''
 return O00o
 if 55 - 55: i1iIi % Iii / Ii
 if 20 - 20: III1iiIii / i1IiiiI1iI * III1iiIii * oO0o
def IiI1iiIiII ( text , start_with , end_with ) :
 O00o = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return O00o
def iiI1iiii1Iii ( ) :
 OOOOoO = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 OOOOoO . connect ( ( '8.8.8.8' , 0 ) )
 OOOOoO = OOOOoO . getsockname ( ) [ 0 ]
 return OOOOoO
 if 80 - 80: I1ii11iIi11i % III1iiIii % ii * I1ii11iIi11i % o0ii1I
def iIioOo ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 O0Ooo0O0OO = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( O0Ooo0O0OO . group ( ) )
I11iiI = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
III1ii = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
iii1 = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
O0Ooo0O = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
iii1oOo0OoOOOo0 = '&action=get_live_categories'
OOoo00 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
i1iIii1i111 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 22 - 22: i1iIi / i1iIi - o0ii1I % Iii . oooOo0oo0oo + III1iiIii
o0o0 = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
OooO00oo0O0 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
i1iI = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
Ooiiii11iI1 = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 81 - 81: Ii + o0ii1I % Ii - ooOoO0O00
def ii11i1I1i ( ) :
 i1IiOOOooOOOOOOOO ( )
 open = OooOoooOo ( i1iI )
 OoOo = IiI1iiIiII ( open , '<channel>' , '</channel>' )
 for IIiiiI1iI in OoOo :
  iIIIiIi = oO0o0oOo ( IIiiiI1iI , '<title>' , '</title>' )
  iIIIiIi = base64 . b64decode ( iIIIiIi )
  II1IIIii = oO0o0oOo ( IIiiiI1iI , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  I1I1II1I11 ( '[COLORsteelblue]' + iIIIiIi + '[/COLOR]' , II1IIIii , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 49 - 49: ii + ii / oooOo0oo0oo . i1i1I1IIii1II
def IiIooOoOo0O00oo ( url ) :
 open = OooOoooOo ( Ooiiii11iI1 + url )
 OoOo = IiI1iiIiII ( open , '<channel>' , '</channel>' )
 for IIiiiI1iI in OoOo :
  iIIIiIi = oO0o0oOo ( IIiiiI1iI , '<title>' , '</title>' )
  iIIIiIi = base64 . b64decode ( iIIIiIi )
  xbmc . log ( str ( iIIIiIi ) )
  O0O0O0oO0o0OOOOOO = oO0o0oOo ( IIiiiI1iI , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  II1IIIii = oO0o0oOo ( IIiiiI1iI , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  O000OOO = oO0o0oOo ( IIiiiI1iI , '<description>' , '</description>' )
  O000OOO = base64 . b64decode ( O000OOO )
  iIIi111IiII1i = '('
  oOo0O000oo0 = ')'
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , II1IIIii , 222 , O0O0O0oO0o0OOOOOO , IIo0o0O0O00oOOo , ( '[COLOR' + ooOoOoo0O + ']' + O000OOO + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( oOo0O000oo0 , '[COLORsteelblue]' ) . replace ( iIIi111IiII1i , '[COLORorangered]' ) )
  if 15 - 15: I1ii11iIi11i / o0ii1I % o0o00Oo0O + Ii1I
def o0oi1I1I1I ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( OOoo00 + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , type , I1 , iiIiIiII in IIi :
  IIiI = ( O0Ooo0O + I1 + '.m3u8' ) . strip ( )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , IIiI , 222 , ( iiIiIiII ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
def iII1III ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi1I1i , O0oo0oO00o in IIi :
  if name == iIIIiIi1I1i :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) + O0oo0oO00o , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def I1ii111i1ii1 ( name ) :
 o0Ii11iIiiI = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , ooO0OO , oOOo0O00o in IIi :
  oOOo0O00o = ( oOOo0O00o ) . replace ( '.ts' , '.m3u8' )
  Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oOOo0O00o ) . strip ( ) , 222 , ooO0OO , ooO0OO , '' )
 else :
  Ii1I1i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 82 - 82: ii
  if 75 - 75: IIiIiII11i % oOo0O0Ooo + oooOo0oo0oo % ii / III1iiIii
  if 4 - 4: Ii - oooOo0oo0oo % Ii1I * i1IiiiI1iI % I11i
  if 71 - 71: i1iIi . i1iIi - iI11I1II1I1I
  if 22 - 22: ii / Ii1I % IiI1i11I * OOooOOo
  if 32 - 32: ii % i1i1I1IIii1II % iI11I1II1I1I / o0o00Oo0O
  if 61 - 61: IIiIiII11i . o0o00Oo0O - o0ii1I - Ii1I / Ii - IIiIiII11i
  if 98 - 98: o0ii1I - oOo0O0Ooo . Ii * I1ii11iIi11i
  if 29 - 29: o0ii1I / i1iIi % Iii
  if 10 - 10: iI11I1II1I1I % ii % Ii1I
  if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * Iii
  if 89 - 89: o0ii1I - i1iIi . Iii - i1IiiiI1iI - oOo0O0Ooo
def o00o0 ( ) :
 I1I1II1I11 ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  I1I1II1I11 ( 'Backup Genie Favourites' , oOOo0O00o , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  I1I1II1I11 ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  I1I1II1I11 ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 79 - 79: III1iiIii + III1iiIii + o0ii1I
  if 39 - 39: o0o00Oo0O - ii
  if 63 - 63: iI11I1II1I1I % I11i * i1iIi
zip = oo00 . getSetting ( 'zip' )
oo0iii1iI = xbmc . translatePath ( os . path . join ( zip ) )
def IiiIi1I11 ( ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 13 - 13: i1iIi * oooOo0oo0oo + I11i
  if 27 - 27: i1i1I1IIii1II % Iii - IiI1i11I / III1iiIii . ii / I1ii11iIi11i
  if 8 - 8: o0o00Oo0O + i1i1I1IIii1II + i1IiiiI1iI
def i111iii1I1 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  IiiIi1I11 ( )
  iiIiII1 = open ( url ) . read ( )
  ii111iI = os . path . join ( oo0iii1iI , description . split ( 'Your ' ) [ 1 ] )
  O0oO0 = open ( ii111iI , mode = 'w' )
  O0oO0 . write ( iiIiII1 )
  O0oO0 . close ( )
 else :
  if 'guisettings.xml' in description :
   IIiiiI1iI = open ( os . path . join ( oo0iii1iI , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O00o = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( O00o ) . findall ( IIiiiI1iI )
   for type , ii11I1 , I1I in IIi :
    I1I = I1I . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , ii11I1 , I1I ) )
  else :
   ii111iI = os . path . join ( url )
   iiIiII1 = open ( os . path . join ( oo0iii1iI , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O0oO0 = open ( ii111iI , mode = 'w' )
   O0oO0 . write ( iiIiII1 )
   O0oO0 . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 76 - 76: oOo0O0Ooo
 if 42 - 42: ii % I1ii11iIi11i % oooOo0oo0oo
 if 39 - 39: o0ii1I
 if 60 - 60: oooOo0oo0oo
def o000ooOo0o0OO ( ) :
 iiI1ii1IIiI = 1
 IiiIi1I11 ( )
 IIi1i1I11IIII = xbmc . translatePath ( os . path . join ( oo0iii1iI , 'Build Backup' , 'Full Backup' , '' ) )
 OooOoOOO00O = xbmc . translatePath ( os . path . join ( oo0iii1iI , 'Build Backup' , 'my_full_backup.zip' ) )
 I111iIIII11iI = xbmc . translatePath ( os . path . join ( oo0iii1iI , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( IIi1i1I11IIII ) :
  os . makedirs ( IIi1i1I11IIII )
 oOoOO = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not oOoOO ) : return False , 0
 i11I1iIii1i11 = oOoOO
 iIiiI11II11i = xbmc . translatePath ( os . path . join ( IIi1i1I11IIII , i11I1iIii1i11 + '.zip' ) )
 o00OoO0o0 = [ 'plugin.video.GenieTv' ]
 o0OOOoO0ooOOOo0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 o0oOOO = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 IIi11 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 O0OOOiii1iII1I = "Creating full backup of existing build"
 i1Ii11ii = "Creating Community Build"
 Ii11IIIi1 = "Archiving..."
 ooooooo00oO0OO = ""
 IIIii11 = "Please Wait"
 i1i11I1I1 ( oOo0oooo00o , iIiiI11II11i , i1Ii11ii , Ii11IIIi1 , ooooooo00oO0OO , IIIii11 , o0oOOO , IIi11 )
 time . sleep ( 1 )
 OOOOOoooO = xbmc . translatePath ( os . path . join ( IIi1i1I11IIII , i11I1iIii1i11 + '_guisettings.zip' ) )
 oO0Oooo0OoO = zipfile . ZipFile ( OOOOOoooO , mode = 'w' )
 try :
  oO0Oooo0OoO . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oO0Oooo0OoO . close ( )
 if iiI1ii1IIiI == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + OooOoOOO00O , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + iIiiI11II11i + '[/COLOR]' )
  if 38 - 38: oOo0O0Ooo . oOo0O0Ooo . o0ii1I + Ii1I * I1ii11iIi11i
def i1i11I1I1 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 OoOO0 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 Iii1I = len ( sourcefile )
 ooo = [ ]
 II111 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for I11iIi , Ii1IIiII1I , OOOii in os . walk ( sourcefile ) :
  for file in OOOii :
   II111 . append ( file )
 Iii1I11 = len ( II111 )
 for I11iIi , Ii1IIiII1I , OOOii in os . walk ( sourcefile ) :
  Ii1IIiII1I [ : ] = [ O0o0o for O0o0o in Ii1IIiII1I if O0o0o not in exclude_dirs ]
  OOOii [ : ] = [ O0oO0 for O0oO0 in OOOii if O0oO0 not in exclude_files ]
  for file in OOOii :
   ooo . append ( file )
   IiiiIi1111I = len ( ooo ) / float ( Iii1I11 ) * 100
   o0oOoO00o . update ( int ( IiiiIi1111I ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iII1i1ii = os . path . join ( I11iIi , file )
   if not 'temp' in Ii1IIiII1I :
    if not 'plugin.program.originwizard' in Ii1IIiII1I :
     import time
     i1I1ii1i = '01/01/1980'
     iiiiII11iIi = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iII1i1ii ) ) )
     if iiiiII11iIi > i1I1ii1i :
      OoOO0 . write ( iII1i1ii , iII1i1ii [ Iii1I : ] )
 OoOO0 . close ( )
 o0oOoO00o . close ( )
 if 51 - 51: I1ii11iIi11i / III1iiIii * o0ii1I - IIiIiII11i / oOo0O0Ooo . III1iiIii
 if 65 - 65: III1iiIii
def oooOOo0oOoOO ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 6 - 6: i1i1I1IIii1II . Iii
 if 43 - 43: Ii1I + I11i
def iI1iiiiiii ( ) :
 iii ( )
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  O00OoO0o ( )
 if O0O00Oo == 1 :
  OoOoO ( )
 if O0O00Oo == 2 :
  O0O0 ( )
 if O0O00Oo == 3 :
  i1I111Ii ( )
  if 63 - 63: iI11I1II1I1I + III1iiIii % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
  if 60 - 60: I11i . OOooOOo % i1IiiiI1iI / oOo0O0Ooo / o0o00Oo0O
  if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / oooOo0oo0oo . Ii1I * i1iIi
  if 59 - 59: iI11I1II1I1I / Ii1I % i1iIi
  if 84 - 84: iI11I1II1I1I / oOo0O0Ooo . OOooOOo % Iii
  if 99 - 99: I1ii11iIi11i + Ii
  if 36 - 36: o0ii1I * i1IiiiI1iI * iI11I1II1I1I - Iii % Ii
  if 98 - 98: iI11I1II1I1I - ooOoO0O00 + i1iIi % Iii + i1iIi / i1i1I1IIii1II
  if 97 - 97: III1iiIii % i1iIi + IIiIiII11i - III1iiIii % oO0o + i1iIi
def iIIII11i ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   i1iiiIii11 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if O0O00Oo == 1 :
   i1iiiIii11 ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if O0O00Oo == 2 :
   oOo0OOoo0o ( )
  if O0O00Oo == 3 :
   iiiIIiiIi ( )
  if O0O00Oo == 4 :
   Oooo0oOooOO ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0O00Oo == 5 :
   O0ooooO ( )
  if O0O00Oo == 6 :
   o0ooOooO ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0O00Oo == 7 :
   O0OoOo ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0O00Oo == 8 :
   OOOOoO0 ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0O00Oo == 9 :
   IiiIiIIi1 ( )
  if O0O00Oo == 10 :
   i1oo ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 90037 , iiIi1IIiIi + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 90037 , iiIi1IIiIi + 'Quicksilver.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '' , 70001 , iiIi1IIiIi + 'RadioNomy.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30031 , iiIi1IIiIi + 'MusicChannels.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iiIi1IIiIi + 'UKRadio.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , str ( oO0000OOo00 ) , 1013 , iiIi1IIiIi + 'WorldRadio.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iiIi1IIiIi + 'Concerts.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) , 1030 , iiIi1IIiIi + 'MUSIC.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iiIi1IIiIi + 'MusicVideos.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 1111 , iiIi1IIiIi + 'MusicSearch.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , iiIi1IIiIi + 'KodibleAudioBooks.png' , Oo00OOOOO , '' )
  if 83 - 83: o0o00Oo0O + OOooOOo / o0o00Oo0O / Iii
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 68 - 68: ooOoO0O00 . Iii . ooOoO0O00 + III1iiIii % oOo0O0Ooo
def IIoO ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   iI1I ( )
  if O0O00Oo == 1 :
   iiI ( )
  if O0O00Oo == 2 :
   I1i ( )
  if O0O00Oo == 3 :
   i111I1 ( oOOo0O00o )
  if O0O00Oo == 4 :
   OOOo0Oo0O ( oOOo0O00o )
  if O0O00Oo == 5 :
   OOOOo0o00OO0000 ( )
  if O0O00Oo == 6 :
   i1I1I1iIIi ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0O00Oo == 7 :
   IiOo00O0o0O ( )
 else :
  Ii1I1i ( 'CLLEANUP' , 'url' , 9666 , iiIi1IIiIi + 'MAIN5.png' , Oo00OOOOO , '' )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '' , 80000 , iiIi1IIiIi + 'KillKodi.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '' , 50004 , iiIi1IIiIi + 'Speedtest.png' , Oo00OOOOO , '' )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , iiIi1IIiIi + 'View-Log-File.png' , Oo00OOOOO , '' )
  Ii1I1i ( 'DELETE CACHE' , 'url' , 14 , iiIi1IIiIi + 'DeleteCache.png' , Oo00OOOOO , '' )
  Ii1I1i ( 'DELETE PACKAGES' , 'url' , 6 , iiIi1IIiIi + 'DeletePackages.png' , Oo00OOOOO , '' )
  Ii1I1i ( 'FORCE REFRESH' , 'url' , 10 , iiIi1IIiIi + 'ForceRefresh.png' , Oo00OOOOO , 'Force Refresh All Repos' )
  I1I1II1I11 ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , iiIi1IIiIi + '1.jpg' , Oo00OOOOO , 'Fix Corrupt Database' )
  Ii1I1i ( 'CHECK MY IP' , 'url' , 12 , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
  Ii1I1i ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , iiIi1IIiIi + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Oo00OOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 86 - 86: Iii + o0o00Oo0O + I1ii11iIi11i - Iii
  if 34 - 34: IIiIiII11i % oOo0O0Ooo % i1IiiiI1iI + I1ii11iIi11i - OOooOOo
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 66 - 66: o0ii1I * iI11I1II1I1I - i1iIi / oOo0O0Ooo
 if 62 - 62: III1iiIii . o0o00Oo0O . iI11I1II1I1I
def i1i1II ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iiIi1IIiIi + 'repos.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEW[/COLOR]' , str ( oO0000OOo00 ) , 22 , iiIi1IIiIi + 'NEW.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']IPTV[/COLOR]' , str ( oO0000OOo00 ) , 23 , iiIi1IIiIi + 'IPTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']VIDEO[/COLOR]' , str ( oO0000OOo00 ) , 24 , iiIi1IIiIi + 'VIDEO.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SPORTS[/COLOR]' , str ( oO0000OOo00 ) , 25 , iiIi1IIiIi + 'SPORTS.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 26 , iiIi1IIiIi + 'KIDS.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) , 27 , iiIi1IIiIi + 'MUSIC.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']PROGRAMS[/COLOR]' , str ( oO0000OOo00 ) , 28 , iiIi1IIiIi + 'PROGRAMS.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']XXX[/COLOR]' , 'URL' , 29 , iiIi1IIiIi + 'XXX.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 94 - 94: i1iIi % Iii % ooOoO0O00
 if 90 - 90: o0ii1I * oO0o
def I1iO0o0O0OooOoo ( ) :
 iii ( )
 Ii1I1i ( 'CHECK ADVANCED XML' , str ( oO0000OOo00 ) , 8 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'MUCKYS XML' , str ( oO0000OOo00 ) + '/wizard/muckys.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( '0CACHE XML' , str ( oO0000OOo00 ) + '/wizard/0cache.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'MIKEY1234 XML' , str ( oO0000OOo00 ) + '/wizard/mikey.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'TUXENS XML' , str ( oO0000OOo00 ) + '/wizard/tuxens.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'P2P RECOMMENDED XML1' , str ( oO0000OOo00 ) + '/wizard/p2p1.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'P2P RECOMMENDED XML2' , str ( oO0000OOo00 ) + '/wizard/p2p2.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'DELETE XML' , str ( oO0000OOo00 ) , 11 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 17 - 17: ii % i1i1I1IIii1II - ooOoO0O00 % III1iiIii % I1ii11iIi11i
def II1III1I1I1Ii ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 41 - 41: ii . i1IiiiI1iI % OOooOOo - IiI1i11I
def oOOooO ( ) :
 iii ( )
 Ii1I1i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 38 - 38: o0o00Oo0O
 if 79 - 79: ooOoO0O00 . i1i1I1IIii1II
 if 34 - 34: i1IiiiI1iI * IIiIiII11i
def o0oO00OOo0oO ( ) :
 iii ( )
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  oOiiI11I1ii11 ( )
 if O0O00Oo == 0 :
  O0OoO0oooOO ( oOOo0O00o )
 if O0O00Oo == 0 :
  i1ii11I111Ii ( oOOo0O00o )
  if 77 - 77: oO0o + oO0o . i1iIi * ii + oO0o
  if 6 - 6: ooOoO0O00 - Iii
  if 89 - 89: i1iIi - Iii . o0o00Oo0O % ii . Ii
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 35 - 35: IIiIiII11i / OOooOOo - o0o00Oo0O . IIiIiII11i
def oO0o000oOO ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for ooO0OO , iIIIiIi in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , ooO0OO , ooO0OO , '' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 27 - 27: o0o00Oo0O - Iii * IIiIiII11i - iI11I1II1I1I / i1iIi
def II1iOOoOooO0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( I1IiiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 6 - 6: oOo0O0Ooo - Ii
def oOiiI11I1ii11 ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 61 - 61: i1IiiiI1iI * Ii1I % oOo0O0Ooo % oO0o % Iii + Iii
def i1111I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OoO00oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 96 - 96: ooOoO0O00
def oOOO00 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + ooooOOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 49 - 49: o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . IIiIiII11i % III1iiIii
def IIii1Ii1i1ii1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOOoOOooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 42 - 42: iI11I1II1I1I * o0ii1I / oO0o + oooOo0oo0oo
def Iii11iI1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 79 - 79: oOo0O0Ooo - IiI1i11I / Iii . I1ii11iIi11i
def O0OoO0oooOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o0III11IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 40 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 53 - 53: IiI1i11I / ooOoO0O00 / ooOoO0O00
def o0oo00O ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IIIIII1iI1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 14 - 14: oOo0O0Ooo / o0o00Oo0O
def oooooo0O000o ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  II111iii ( )
 if O0O00Oo == 1 :
  OooO00o000 ( )
 if O0O00Oo == 2 :
  i1i11II1 ( )
  if 5 - 5: oO0o + oO0o + IIiIiII11i * iI11I1II1I1I + ii
  if 77 - 77: o0o00Oo0O * Ii1I * i1i1I1IIii1II + oO0o + Ii1I - i1IiiiI1iI
  if 10 - 10: Ii1I + III1iiIii
  if 58 - 58: oOo0O0Ooo + ii / IiI1i11I . i1iIi % I11i / Ii1I
def OooO00o000 ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , oooO0 in IIi :
  oOoo000 ( 'Android Apps' + oooO0 , 'https://www.apkfiles.com' + oOOo0O00o , 30035 , iiIi1IIiIi + 'apps.png' )
 for oOOo0O00o , oooO0 in i1Iii1i1I :
  oOoo000 ( 'Android Games' + oooO0 , 'https://www.apkfiles.com' + oOOo0O00o , 30035 , iiIi1IIiIi + 'GAMES.png' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def I11Iii11i11I1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '/cat' in url :
   oOoo000 ( ( iIIIiIi ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def IiOO0oo00OOo ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '/app' in url :
   oOoo000 ( ( iIIIiIi ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def OoOo00oOoO ( url ) :
 I1i111I = OooOoooOo ( url )
 II1IIIii = url
 if "page=" in str ( url ) :
  II1IIIii = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  if 'apk' in url :
   Ii1I1i ( ( iIIIiIi ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + ooO0OO )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 Ii1I1i ( 'Next Page' , II1IIIii + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def Oo0O00o0O0 ( name , url ) :
 I1i111I = oOOo000oOoO0 ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( I1i111I )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  IiIii11ii111 ( name , url , 'Brackets' )
def i1i11II1 ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'https://www.apkfiles.com/search?q=' + ( o0OO ) . replace ( ' ' , '+' ) + '&search_type=1'
 Oo = ooIII1II1iii1i . lower ( )
 OoOo00oOoO ( Oo )
 if 75 - 75: o0o00Oo0O
def oOoO ( url ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( OOooooO , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I11ii1IIiIi = os . path . join ( o00oo0 , iIIIiIi + '.apk' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 80 - 80: OOooOOo + iI11I1II1I1I . III1iiIii
def ooOoOoo000O0O ( url ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I11ii1IIiIi = os . path . join ( o00oo0 , iIIIiIi + '.mp4' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 42 - 42: I11i / III1iiIii
 if 79 - 79: o0ii1I
def iII1i1 ( name , url , description ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I11ii1IIiIi = os . path . join ( o00oo0 , name )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 IIIii = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print IIIii
 print '======================================='
 extract . all ( I11ii1IIiIi , IIIii , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 63 - 63: oOo0O0Ooo - Ii - IiI1i11I % Iii . o0ii1I * Ii1I
 if 66 - 66: ii + I11i . ooOoO0O00 * IiI1i11I
 if 92 - 92: Iii / i1IiiiI1iI
 if 4 - 4: i1IiiiI1iI
 if 11 - 11: ii + ooOoO0O00 / o0ii1I
def II111iii ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , oOOo0O00o , iiIiIiII , IIo0o0O0O00oOOo , i1I in IIi :
  Ii1I1i ( iIIIiIi , oOOo0O00o , 80003 , iiIiIiII , iiIi1IIiIi + 'APKToolsB.png' , i1I )
def Iii11 ( apk , ret = None ) :
 if apk == "kodi" :
  iIi11iIiiIi = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( iIi11iIiiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   iIIii = IIi [ 0 ] [ 0 ]
   i11I1iIii1i11 = IIi [ 0 ] [ 1 ]
   O0OooOO = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( iIIii , i11I1iIii1i11 )
  if ret == 'version' : return iIIii
  else : return O0OooOO
 elif apk == "spmc" :
  Ii1 = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  iIIii = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  O0OooOO = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( iIIii , iIIii )
  if ret == 'version' : return iIIii
  else : return O0OooOO
def IiIii11ii111 ( name , url , Brackets ) :
 if OO ( ) == 'android' :
  iIIi11 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not iIIi11 : iIiiII1Ii1ii ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  iIIi1 = name
  if iIIi11 :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not II1I1Ii ( url ) == True : iIiiII1Ii1ii ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iIIi1 , '' , 'Please Wait' )
   I11ii1IIiIi = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( I11ii1IIiIi )
   except : pass
   downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    oO0Oooo0OoO = zipfile . ZipFile ( I11ii1IIiIi )
    for file in oO0Oooo0OoO . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as O0oO0 :
       OoOo0O00 = file . split ( '/' ) [ 1 ]
       O0oO0 . write ( oO0Oooo0OoO . read ( file ) )
       xbmc . sleep ( 500 )
       O0oO0 . close ( )
       try :
        os . remove ( I11ii1IIiIi )
       except :
        pass
       I11ii1IIiIi = os . path . join ( i1iIIi1 , OoOo0O00 )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I11ii1IIiIi + '")' )
  else : iIiiII1Ii1ii ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIiiII1Ii1ii ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 9 - 9: oooOo0oo0oo
 if 38 - 38: Iii . oO0o . Ii * ii + IiI1i11I
 if 49 - 49: I1ii11iIi11i - oO0o / i1IiiiI1iI / I11i % i1i1I1IIii1II
 if 38 - 38: I11i . i1i1I1IIii1II / I11i % IIiIiII11i
def I11iI1iIii1ii ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOOo0O00o = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oOOo0O00o )
  OoOoOo0o00OoOO ( ( iIIIiIi ) . replace ( '_' , ' ' ) , oOOo0O00o )
  if 26 - 26: o0o00Oo0O - Iii . IIiIiII11i / iI11I1II1I1I
def OoOoOo0o00OoOO ( name , url ) :
 if OO ( ) == 'android' :
  iIIi11 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not iIIi11 : iIiiII1Ii1ii ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  iIIi1 = name
  if iIIi11 :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not II1I1Ii ( url ) == True : iIiiII1Ii1ii ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % iIIi1 , '' , 'Please Wait' )
   I11ii1IIiIi = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( I11ii1IIiIi )
   except : pass
   downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I11ii1IIiIi + '")' )
  else : iIiiII1Ii1ii ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIiiII1Ii1ii ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 80 - 80: oOo0O0Ooo % Ii1I % IiI1i11I / III1iiIii
 if 67 - 67: o0ii1I / o0o00Oo0O * IiI1i11I
def ii1iIIIiIiII ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'INFO' )
 if 39 - 39: I11i / III1iiIii - IiI1i11I
 if 96 - 96: Iii * Ii1I * o0ii1I + Ii1I % oOo0O0Ooo + Ii
def II11IiiIII ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 30015 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 37 - 37: Iii % Ii1I / i1iIi
def o0oO ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 Ooooo = url
 ooO0OO = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for I1 , iIIIiIi in IIi :
  if '.mp4' in iIIIiIi :
   Ii1I1i ( 'Watch VIDEO' , url + '/' + I1 , 222 , ooO0OO , fanart , '' )
  if 'description' in iIIIiIi :
   Ii1I1i ( 'Read Description' , url + '/' + I1 , 30017 , ooO0OO , fanart , '' )
  if 'images' in iIIIiIi :
   I1I1II1I11 ( 'View Images' , url + '/' + I1 , 30018 , ooO0OO , fanart , '' )
  if 'url' in iIIIiIi :
   Ii1I1i ( 'Install Build On Android' , url + '/' + I1 , 30016 , ooO0OO , fanart , '' )
  if 'url' in iIIIiIi :
   Ii1I1i ( 'Install Build On Pc' , url + '/' + I1 , 30019 , ooO0OO , fanart , '' )
 I1iI1ii1II ( 'movies' , 'INFO' )
 if 53 - 53: oOo0O0Ooo
def i1Iii ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  iiI11111II ( url )
  if 48 - 48: IiI1i11I % Ii . ii * III1iiIii % oO0o . IiI1i11I
def IiOOo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  o0O0O0O00o ( url )
  if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
def Ooi1IIii1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for I111iiIIiI1I in IIi :
  o0OIiII ( 'Description:' , I111iiIIiI1I )
  if 60 - 60: o0ii1I % I1ii11iIi11i / Iii . IiI1i11I / i1IiiiI1iI - ii
def o0iii1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for I1 , iIIIiIi in IIi :
  if 'png' in iIIIiIi :
   Ii1I1i ( 'image' , '' , '' , url + '/' + I1 , url + '/' + I1 , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - IiI1i11I - Ii
def oo0O00o0 ( name , url , description ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , name + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOOOo0o00OO0000 ( )
 if 51 - 51: o0o00Oo0O % IIiIiII11i % Ii + oooOo0oo0oo . ii
 if 14 - 14: I1ii11iIi11i + Ii - i1i1I1IIii1II % III1iiIii
def o0O0O0O00o ( url ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 ooO0O00Oo0o ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iI1I ( )
 if 1 - 1: i1i1I1IIii1II + i1IiiiI1iI . oOo0O0Ooo
def iiI11111II ( url ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 ooO0O00Oo0o ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iI1I ( )
 if 47 - 47: IiI1i11I . OOooOOo
def o0oOO0 ( name , url , description ) :
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 I11ii1IIiIi = os . path . join ( O0OoO000O0OO )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iI1I ( )
 if 31 - 31: o0ii1I * I11i * o0ii1I + oO0o * I11i . i1IiiiI1iI
def OO ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def O00Oooo ( log ) :
 xbmc . log ( "[%s]: %s" % ( i1iiIIiiI111 , log ) )
 if not os . path . exists ( oo0o0O00 ) : os . makedirs ( oo0o0O00 )
 if not os . path . exists ( oO ) : O0oO0 = open ( oO , 'w' ) ; O0oO0 . close ( )
 with open ( oO , 'a' ) as O0oO0 :
  Oo00oo00o00Oo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  O0oO0 . write ( Oo00oo00o00Oo . rstrip ( '\r\n' ) + '\n' )
def iI1I ( ) :
 O0O00Oo = iIii1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if O0O00Oo == 0 : return
 elif O0O00Oo == 1 : pass
 I1i1i1iii = OO ( )
 O00Oooo ( "Platform: " + str ( I1i1i1iii ) )
 os . _exit ( 1 )
 O00Oooo ( "Force close failed!  Trying alternate methods." )
 if I1i1i1iii == 'osx' :
  O00Oooo ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1i1i1iii == 'linux' :
  O00Oooo ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1i1i1iii == 'android' :
  O00Oooo ( "############ try android force close #################" )
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop com.gadgetcity.itvmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill com.gadgetcity.itvmc' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.com.gadgetcity.itvmc());' )
  except : pass
  iIii1 . ok ( i1iiIIiiI111 , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif I1i1i1iii == 'windows' :
  O00Oooo ( "############ try windows force close #################" )
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill XBMC.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill Kodi.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im Kodi.exe /f' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im XBMC.exe /f' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  O00Oooo ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  O00Oooo ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 1 - 1: III1iiIii
  if 31 - 31: ooOoO0O00
  if 21 - 21: ooOoO0O00
def i1ii11I111Ii ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OOOO00 , Ii1IIiII1I , OOOii in os . walk ( url ) :
  for file in OOOii :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    IIiiiI1iI = open ( ( os . path . join ( OOOO00 , file ) ) ) . read ( )
    O00oo0o0000 = IIiiiI1iI . replace ( oOo0oooo00o , 'special://home/' )
    O0oO0 = open ( ( os . path . join ( OOOO00 , file ) ) , mode = 'w' )
    O0oO0 . write ( str ( O00oo0o0000 ) )
    O0oO0 . close ( )
 iI1I ( )
 if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
def oOo0OOoo0o ( ) :
 oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 61 - 61: oOo0O0Ooo + i1i1I1IIii1II % i1IiiiI1iI % iI11I1II1I1I - ii
def iIIiI1 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def Ii11Ii1 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def IiiIIII1I1i ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , ooO0OO , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , ooO0OO )
def I1IIIIII1 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( I1i111I )
 for url in IIi :
  I11iiiiI1i ( url )
def O0oO0O ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO
 IIiiiII11i = 'https://www.radionomy.com/en/search/index?query=' + ( o0OO ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( IIiiiII11i )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oOOo0O00o , 70005 , ooO0OO )
  if 34 - 34: I11i % ii
  if 36 - 36: oOo0O0Ooo
def O0ooooO ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.listenlive.eu/' + oOOo0O00o , 10111113 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def Oooo0oOooOO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . Iii
 if 64 - 64: i1iIi / ooOoO0O00 % IiI1i11I
 IIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , OOoOo0O0 , url , I1o0 in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' [COLORorangered] ' + I1o0 + '[/COLOR]' , url , 222225 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[CR]' + OOoOo0O0 + '[CR]' + I1o0 + '[/COLOR]' )
  if 26 - 26: IiI1i11I * iI11I1II1I1I + IIiIiII11i / oOo0O0Ooo
def O0OO ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.toonjet.com/' + oOOo0O00o , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o0O00oOo ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( I1i111I )
 for url , ooO0OO in IIi :
  if 'ol.gif' in ooO0OO :
   pass
  elif 'link_block_' in ooO0OO :
   pass
  elif '.png' in ooO0OO :
   pass
  else :
   oOoo000 ( ( ooO0OO ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1ii ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I1i111I )
 for url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 2 - 2: IIiIiII11i . Iii
  if 83 - 83: oOo0O0Ooo - i1IiiiI1iI + oOo0O0Ooo . oOo0O0Ooo
def i1oo ( ) :
 i1ioO ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 i1ioO ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 45 - 45: ooOoO0O00 % oooOo0oo0oo % IIiIiII11i
def IIIIi1Iii1iIi ( ) :
 i1ioO ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 i1ioO ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 i1ioO ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 36 - 36: Ii * Ii1I * OOooOOo
def II1iIii11II1IIiI ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oOOo0O00o , I1iII1II1I1ii in IIi :
  if 'Parent' in iIIIiIi :
   pass
  elif '2' in I1iII1II1I1ii :
   i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 54 - 54: ii + I1ii11iIi11i * oooOo0oo0oo
def oOoO0O00o ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oOOo0O00o , I1iII1II1I1ii in IIi :
  if o0OO in iIIIiIi . lower ( ) :
   if '1' in I1iII1II1I1ii :
    i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in I1iII1II1I1ii :
    i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in I1iII1II1I1ii :
    i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 25 - 25: o0o00Oo0O + Iii + oooOo0oo0oo * Ii1I
    if 87 - 87: I1ii11iIi11i . ii * i1IiiiI1iI * IIiIiII11i / ooOoO0O00 * OOooOOo
def I11IiIi1iI1ii ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oOOo0O00o , I1iII1II1I1ii in IIi :
  if '1' in I1iII1II1I1ii :
   i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in I1iII1II1I1ii :
   i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in I1iII1II1I1ii :
   i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 68 - 68: III1iiIii * oO0o . Iii / o0ii1I . I11i - Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: I1ii11iIi11i / o0ii1I % Iii + i1i1I1IIii1II - oO0o
def i11ii ( url ) :
 I1 = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in i1Iii1i1I :
  if 'mp3' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I1 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in iIIIiIi :
   i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1 + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 42 - 42: o0ii1I * o0o00Oo0O / i1i1I1IIii1II
   if 8 - 8: ooOoO0O00 + IIiIiII11i / o0ii1I + Ii1I % o0ii1I - iI11I1II1I1I
   if 29 - 29: I1ii11iIi11i + IIiIiII11i
def oOOo00ooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1 = url
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'Parent' in iIIIiIi :
   pass
  elif '.db' in iIIIiIi :
   pass
  elif '.jpg' in iIIIiIi :
   pass
  elif '.html' in iIIIiIi :
   pass
  elif '.doc' in iIIIiIi :
   pass
  elif 'mp3' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1 + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I1 + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 64 - 64: ooOoO0O00
   if 31 - 31: Iii / i1iIi % i1i1I1IIii1II + ii
def iiI1IiIi1i1I ( ) :
 i1ioO ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 i1ioO ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 i1ioO ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 31 - 31: o0ii1I / o0ii1I
def o00000O ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oOOo0O00o + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in ooO0OO :
   pass
  else :
   i1ioO ( ooO0OO , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oOOo0O00o ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + ooO0OO + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 23 - 23: I1ii11iIi11i - o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: Ii1I
 if 54 - 54: i1iIi * Ii1I . IIiIiII11i / oooOo0oo0oo % oooOo0oo0oo
def IiIIii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if '</a>' in iIIIiIi :
   pass
  elif '(' in iIIIiIi :
   i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 7 - 7: o0o00Oo0O - Ii1I / OOooOOo - o0ii1I - i1i1I1IIii1II / ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: ii
def oOO0o00 ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if o0OO in iIIIiIi . lower ( ) :
   if '</a>' in iIIIiIi :
    pass
   elif '(' in iIIIiIi :
    i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 20 - 20: OOooOOo - o0ii1I . OOooOOo - I11i / I11i
    if 96 - 96: ooOoO0O00 * IIiIiII11i
def o00Oo0O ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if '</a>' in iIIIiIi :
   pass
  elif '(' in iIIIiIi :
   i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 17 - 17: oO0o
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: i1i1I1IIii1II + ii - o0ii1I % I11i / I11i / iI11I1II1I1I
 if 31 - 31: ii - o0ii1I . III1iiIii % i1i1I1IIii1II
def II11i1I1iiII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I1 = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( I1 )
  if 45 - 45: oO0o + oO0o % i1iIi
def I1i1i1iIi1iIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  if '<p align' in iIIIiIi :
   pass
  elif '&nbsp;' in iIIIiIi :
   pass
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 22 - 22: iI11I1II1I1I * oOo0O0Ooo / Iii + OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: oooOo0oo0oo
 if 69 - 69: IIiIiII11i + I1ii11iIi11i - i1i1I1IIii1II . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
def oo0OOOoOo ( ) :
 II11iIiIIIiI = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'ongoing' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'CartoonShows.png' , '' , '' )
  if 'disney' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'Disney.png' , '' , '' )
  if 'genre' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'Genre.png' , '' , '' )
  if 'years' in oOOo0O00o :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 21005 , iiIi1IIiIi + 'Years.png' , '' , '' )
def oOooooooO0o ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oOO0 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , ooO0OO , ooO0OO , iIIIiIi )
 for url , iIIIiIi in oOO0 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def o0Ii11I1iIIi ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIIIi1i1I11i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0ooO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 iIOO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in O0ooO :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , iIIIiIi in iIIIi1i1I11i :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def I1III1I11I1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 85 - 85: i1IiiiI1iI
def ooO000O ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if '9cart' in oOOo0O00o :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 62 - 62: o0ii1I % IIiIiII11i + III1iiIii + oooOo0oo0oo % i1i1I1IIii1II . oOo0O0Ooo
def OOoOo0ooOoo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , iIIIiIi in ii1I1IIii11 :
  if '9cart' in url :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 68 - 68: oooOo0oo0oo + o0ii1I
def o0o0oooO00O0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 20003 , ooO0OO )
 for url , iIIIiIi in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 33 - 33: ooOoO0O00 / oOo0O0Ooo
def iiIi1I1II11II ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   oOoo000 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 40 - 40: IiI1i11I + o0o00Oo0O
def Ii1iII1ii1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 80 - 80: iI11I1II1I1I / Ii + IiI1i11I
def I11I1i ( url ) :
 url = cloudflare . source ( url )
 OoOoooO000OO ( url )
 if 100 - 100: i1i1I1IIii1II
def iiIiiiIii11i1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  OoOoooO000OO ( url )
  if 87 - 87: oO0o + ii . i1iIi * Iii
  if 82 - 82: iI11I1II1I1I * ii
def IIiiIIi1 ( ) :
 if 50 - 50: i1IiiiI1iI - IIiIiII11i
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 33 - 33: III1iiIii / III1iiIii . Ii * Ii1I + I11i
def O0O0 ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 16 - 16: III1iiIii
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 10 - 10: OOooOOo . III1iiIii * iI11I1II1I1I - i1i1I1IIii1II - OOooOOo / i1IiiiI1iI
 for oOOo0O00o , iIIIiIi in IIi :
  if o0OO in iIIIiIi . lower ( ) :
   if 'Dad!' in iIIIiIi :
    pass
   elif 'Family Guy' in iIIIiIi :
    pass
   elif '2 Stupid' in iIIIiIi :
    pass
   elif 'The Zelfs' in iIIIiIi :
    pass
   elif 'A Clone' in iIIIiIi :
    pass
   elif 'A.T.O.M' in iIIIiIi :
    pass
   elif 'Almost Naked' in iIIIiIi :
    pass
   elif 'Angry Kid' in iIIIiIi :
    pass
   elif 'Annoying Orange' in iIIIiIi :
    pass
   elif 'Aqua Teen' in iIIIiIi :
    pass
   elif 'Assy Mcgee' in iIIIiIi :
    pass
   elif 'Astroblast' in iIIIiIi :
    pass
   elif 'Atomic Betty' in iIIIiIi :
    pass
   elif 'Axe Cop' in iIIIiIi :
    pass
   elif 'Baby Playpen' in iIIIiIi :
    pass
   elif 'Beavis and Butt' in iIIIiIi :
    pass
   elif 'Celebrity Deathmatch' in iIIIiIi :
    pass
   elif 'Clerks The' in iIIIiIi :
    pass
   elif 'Crapston Villas' in iIIIiIi :
    pass
   elif 'Duckman:' in iIIIiIi :
    pass
   elif 'Stripperella' in iIIIiIi :
    pass
   elif 'Vixen' in iIIIiIi :
    pass
   else :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
    if 13 - 13: i1i1I1IIii1II + OOooOOo % III1iiIii % ii
    if 22 - 22: i1IiiiI1iI
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 23 - 23: o0o00Oo0O
def oOIII111iiIi1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if 'Dad!' in iIIIiIi :
   pass
  elif 'Family Guy' in iIIIiIi :
   pass
  elif '2 Stupid' in iIIIiIi :
   pass
  elif 'The Zelfs' in iIIIiIi :
   pass
  elif 'A Clone' in iIIIiIi :
   pass
  elif 'A.T.O.M' in iIIIiIi :
   pass
  elif 'Almost Naked' in iIIIiIi :
   pass
  elif 'Angry Kid' in iIIIiIi :
   pass
  elif 'Annoying Orange' in iIIIiIi :
   pass
  elif 'Aqua Teen' in iIIIiIi :
   pass
  elif 'Assy Mcgee' in iIIIiIi :
   pass
  elif 'Astroblast' in iIIIiIi :
   pass
  elif 'Atomic Betty' in iIIIiIi :
   pass
  elif 'Axe Cop' in iIIIiIi :
   pass
  elif 'Baby Playpen' in iIIIiIi :
   pass
  elif 'Beavis and Butt' in iIIIiIi :
   pass
  elif 'Celebrity Deathmatch' in iIIIiIi :
   pass
  elif 'Clerks The' in iIIIiIi :
   pass
  elif 'Crapston Villas' in iIIIiIi :
   pass
  elif 'Duckman:' in iIIIiIi :
   pass
  elif 'Stripperella' in iIIIiIi :
   pass
  elif 'Vixen' in iIIIiIi :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: ooOoO0O00 . oooOo0oo0oo / i1iIi / I11i % III1iiIii - o0ii1I
def iI1i1Iiii ( url ) :
 I1i111I = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i111I )
 for ooO0OO in i1Iii1i1I :
  iiiIIII1IIi = ooO0OO
 ii1I1IIii11 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1i111I )
 for url in ii1I1IIii11 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10007 , iiiIIII1IIi )
  if 63 - 63: IIiIiII11i . i1IiiiI1iI % III1iiIii + IIiIiII11i
  if 81 - 81: oooOo0oo0oo - oOo0O0Ooo % I11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: i1iIi - ooOoO0O00 . OOooOOo
def I1iI1II11i1ii ( url , IMAGE ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  print iIIIiIi + '     ' + url
  if 'easy' in url :
   oo0O0Oo0O ( url )
   if 38 - 38: ii
   if 64 - 64: o0ii1I * i1IiiiI1iI . III1iiIii - IIiIiII11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 96 - 96: i1IiiiI1iI / III1iiIii * iI11I1II1I1I + Ii * Ii1I / oOo0O0Ooo
def oo0O0Oo0O ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I1i111I )
 for url in IIi :
  I11iiiiI1i ( url )
  if 93 - 93: o0o00Oo0O * iI11I1II1I1I + o0ii1I % IiI1i11I
  if 96 - 96: i1i1I1IIii1II % I1ii11iIi11i
  if 20 - 20: i1iIi . III1iiIii / Iii . ii * oooOo0oo0oo + o0ii1I
def iiIII ( ) :
 if 30 - 30: Iii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 46 - 46: i1iIi
def o0O0o ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  if 'elete' in iIIIiIi :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 222 , ooO0OO )
   if 47 - 47: oooOo0oo0oo * o0ii1I % iI11I1II1I1I / i1iIi
def O0O00O ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0ooOIii1iIIIi11I1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , IIII11Ii1I11I , i1iII1IiiIiI1 in O0ooOIii1iIIIi11I1 :
  for o0OO in IIII11Ii1I11I :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   I11II1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oOOo0O00o , iIIIiIi in I11II1 :
    if 'tube' in oOOo0O00o :
     pass
    elif 'stage' in oOOo0O00o :
     OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + IIII11Ii1I11I + '   -   ' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ooO0OO , )
    elif 'vee' in oOOo0O00o :
     pass
     if 82 - 82: oooOo0oo0oo % Ii1I . i1IiiiI1iI . o0o00Oo0O
def O0o0O0oOoO ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0ooOIii1iIIIi11I1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , IIII11Ii1I11I , i1iII1IiiIiI1 in O0ooOIii1iIIIi11I1 :
  I11II1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oOOo0O00o , iIIIiIi in I11II1 :
   if 'tube' in oOOo0O00o :
    pass
   elif 'stage' in oOOo0O00o :
    OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + IIII11Ii1I11I + '   -   ' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ooO0OO )
   elif 'vee' in oOOo0O00o :
    pass
    if 100 - 100: ooOoO0O00 % o0ii1I
    if 55 - 55: oOo0O0Ooo + IiI1i11I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: i1i1I1IIii1II + IiI1i11I % IiI1i11I / Iii . oOo0O0Ooo - OOooOOo
def iIIiI1I1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O0O0OOooOO0 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( O0O0OOooOO0 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in O0O0OOooOO0 :
  IiiI ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 19 - 19: Iii / IiI1i11I + III1iiIii
  if 76 - 76: iI11I1II1I1I / i1IiiiI1iI - Ii1I % I11i % oooOo0oo0oo + ii
  if 10 - 10: oO0o * Iii / I1ii11iIi11i - i1IiiiI1iI
  if 11 - 11: III1iiIii % Ii1I / i1iIi . Ii + oooOo0oo0oo - IIiIiII11i
  if 50 - 50: ooOoO0O00 * i1i1I1IIii1II / Ii / Ii / i1i1I1IIii1II
  if 84 - 84: Ii1I - IiI1i11I + Ii1I
  if 63 - 63: Iii * i1iIi % IIiIiII11i % i1IiiiI1iI + oOo0O0Ooo * I1ii11iIi11i
def I1Iiiiiii ( ) :
 if 96 - 96: III1iiIii
 oo00OOo0 ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 oo00OOo0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 61 - 61: i1i1I1IIii1II % i1iIi - Ii1I + i1i1I1IIii1II . OOooOOo
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 44 - 44: Ii1I / o0o00Oo0O - III1iiIii + oooOo0oo0oo . Iii . Ii1I
def OO000oOO0o ( ) :
 oo00OOo0 ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 oo00OOo0 ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 57 - 57: iI11I1II1I1I * oooOo0oo0oo - Ii / Iii - iI11I1II1I1I + i1iIi
 I1iI1ii1II ( 'movies' , 'MAIN' )
def O0oO0ooOOo ( ) :
 if 9 - 9: i1IiiiI1iI - oO0o + iI11I1II1I1I % o0o00Oo0O + Iii + III1iiIii
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 o0O0O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 50 - 50: ooOoO0O00 + i1iIi
 for iiIiI in o0O0O0 :
  o0Ooo0O00 = oO0 + iiIiI + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( o0Ooo0O00 )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
   if o0OO in iIIIiIi . lower ( ) :
    oOoO0oOo0Oo ( iIIIiIi , oOOo0O00o , 222 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O000OOO )
    if 39 - 39: i1IiiiI1iI
    I1iI1ii1II ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 57 - 57: ii * ii - oOo0O0Ooo / i1IiiiI1iI * Ii1I - III1iiIii
    if 71 - 71: iI11I1II1I1I / Ii % I11i . i1IiiiI1iI * oOo0O0Ooo % IIiIiII11i
def i1II1111 ( ) :
 if 55 - 55: iI11I1II1I1I + oOo0O0Ooo - I1ii11iIi11i
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 o0O0O0 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 24 - 24: oO0o / i1IiiiI1iI + IiI1i11I * Iii * IiI1i11I
 for iiIiI in o0O0O0 :
  IiIIIIIii = oO0 + iiIiI + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( IiIIIIIii )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIIIiIi , O000OOO , oOOo0O00o , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in IIi :
   if o0OO in iIIIiIi . lower ( ) :
    oo00OOo0 ( iIIIiIi , oOOo0O00o , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
    if 45 - 45: oO0o * oO0o
    I1iI1ii1II ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 9 - 9: iI11I1II1I1I
    if 57 - 57: i1iIi / o0ii1I % I11i % Ii
def o0OO0Oooo ( ) :
 if 97 - 97: IiI1i11I
 I1i111I = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , O000OOO , oOOo0O00o , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in IIi :
  oo00OOo0 ( iIIIiIi , oOOo0O00o , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  I1iI1ii1II ( 'movies' , 'MAIN' )
def OoO00o00 ( url ) :
 if 72 - 72: ooOoO0O00
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1Iii11111I1iii = ( '%s%s' % ( OO0Oo00 , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in IIi :
  ii1o0oooO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for ooo00Ooo in ii1o0oooO :
   if ooo00Ooo == url :
    iIIIiIi = ( '[COLORred]Watched - [/COLOR]' + iIIIiIi ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  oOoO0oOo0Oo ( iIIIiIi , url , 222 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
  if 28 - 28: oO0o + i1IiiiI1iI / OOooOOo % i1i1I1IIii1II - I1ii11iIi11i
  I1iI1ii1II ( 'movies' , 'MAIN' )
  if 70 - 70: ooOoO0O00 - iI11I1II1I1I - i1IiiiI1iI
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 49 - 49: i1IiiiI1iI / IIiIiII11i
  if 69 - 69: I11i + Ii1I / iI11I1II1I1I . III1iiIii % Ii1I * OOooOOo
def Iii1i11 ( url ) :
 if 25 - 25: iI11I1II1I1I + Ii - o0ii1I * ii
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , O000OOO , url , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in IIi :
  oo00OOo0 ( iIIIiIi , url , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  if 22 - 22: i1IiiiI1iI - oOo0O0Ooo
  I1iI1ii1II ( 'movies' , 'MAIN' )
  if 96 - 96: ooOoO0O00 + I1ii11iIi11i - IIiIiII11i . ii . oooOo0oo0oo / oO0o
  if 88 - 88: ooOoO0O00
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 53 - 53: i1iIi . oooOo0oo0oo . I11i + i1i1I1IIii1II
def oOoO0oOo0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + o0ii1I % ooOoO0O00 . i1i1I1IIii1II
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
 if 57 - 57: i1i1I1IIii1II
def oo00OOo0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 92 - 92: IIiIiII11i - oO0o - oooOo0oo0oo % oOo0O0Ooo - OOooOOo * i1IiiiI1iI
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
if 16 - 16: iI11I1II1I1I + ii - i1iIi * III1iiIii
if 37 - 37: IiI1i11I
if 15 - 15: I11i % oO0o / IiI1i11I
if 36 - 36: oO0o + oO0o % I1ii11iIi11i + I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
if 20 - 20: oooOo0oo0oo * i1i1I1IIii1II
if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . oooOo0oo0oo
if 31 - 31: i1i1I1IIii1II % ooOoO0O00 . ii - I11i + ii
if 45 - 45: oooOo0oo0oo + Iii / ii - o0ii1I + ii
if 42 - 42: iI11I1II1I1I * oOo0O0Ooo * i1IiiiI1iI
if 62 - 62: oooOo0oo0oo * o0o00Oo0O % III1iiIii . III1iiIii . oOo0O0Ooo
if 91 - 91: ooOoO0O00 . IiI1i11I
if 37 - 37: IiI1i11I - Iii + iI11I1II1I1I / i1IiiiI1iI - oO0o . I11i
if 62 - 62: Ii1I
if 47 - 47: i1IiiiI1iI % oooOo0oo0oo * oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
if 2 - 2: i1IiiiI1iI % ii - i1iIi * Ii1I * III1iiIii
def Ooi11 ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 67 - 67: Iii / o0o00Oo0O * o0ii1I - III1iiIii . ii + III1iiIii
def i1I1iiiI ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 i1IiIi1I1i = [ ]
 try :
  if 39 - 39: Ii + oooOo0oo0oo % IiI1i11I + o0ii1I * oOo0O0Ooo + i1IiiiI1iI
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  Ooi11 ( 'Making Favorites File' )
  i1IiIi1I1i . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  IIiiiI1iI = open ( i1I1iI , "w" )
  IIiiiI1iI . write ( json . dumps ( i1IiIi1I1i ) )
  IIiiiI1iI . close ( )
 else :
  Ooi11 ( 'Appending Favorites' )
  IIiiiI1iI = open ( i1I1iI ) . read ( )
  Oo00oOo = json . loads ( IIiiiI1iI )
  Oo00oOo . append ( ( name , url , iconimage , fanart , mode ) )
  O00oo0o0000 = open ( i1I1iI , "w" )
  O00oo0o0000 . write ( json . dumps ( Oo00oOo ) )
  O00oo0o0000 . close ( )
  if 51 - 51: IiI1i11I
  if 81 - 81: o0o00Oo0O
def i11ii11IiI1 ( ) :
 if os . path . exists ( i1I1iI ) == False :
  i1IiIi1I1i = [ ]
  Ooi11 ( 'Making Favorites File' )
  i1IiIi1I1i . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  IIiiiI1iI = open ( i1I1iI , "w" )
  IIiiiI1iI . write ( json . dumps ( i1IiIi1I1i ) )
  IIiiiI1iI . close ( )
 else :
  Iii1i1ii1i1 = json . loads ( open ( i1I1iI ) . read ( ) )
  OOO0O0OOo = len ( Iii1i1ii1i1 )
  for iio0Oo in Iii1i1ii1i1 :
   iIIIiIi = iio0Oo [ 0 ]
   oOOo0O00o = iio0Oo [ 1 ]
   iiiI1I1iIIIi1 = iio0Oo [ 2 ]
   try :
    IiiiiiiI111i = iio0Oo [ 3 ]
    if IiiiiiiI111i == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     IiiiiiiI111i = iiiI1I1iIIIi1
    else :
     IiiiiiiI111i = IIo0o0O0O00oOOo
   try : iiIIIIiI11II1 = iio0Oo [ 5 ]
   except : iiIIIIiI11II1 = None
   try : IiI1i11i1iI = iio0Oo [ 6 ]
   except : IiI1i11i1iI = None
   if 92 - 92: oooOo0oo0oo % IIiIiII11i . IiI1i11I
   if iio0Oo [ 4 ] == 0 :
    I1I1II1I11 ( iIIIiIi , oOOo0O00o , '' , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , '' , 'fav' )
   else :
    I1I1II1I11 ( iIIIiIi , oOOo0O00o , iio0Oo [ 4 ] , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , '' , 'fav' )
    if 46 - 46: OOooOOo + oOo0O0Ooo % ii * Ii - I1ii11iIi11i
def i11I1Ii1Iiii1 ( name ) :
 Oo00oOo = json . loads ( open ( i1I1iI ) . read ( ) )
 for o0oooOoOoOo in range ( len ( Oo00oOo ) ) :
  if Oo00oOo [ o0oooOoOoOo ] [ 0 ] == name :
   del Oo00oOo [ o0oooOoOoOo ]
   O00oo0o0000 = open ( i1I1iI , "w" )
   O00oo0o0000 . write ( json . dumps ( Oo00oOo ) )
   O00oo0o0000 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 96 - 96: OOooOOo / oO0o % ii * i1iIi
 if 6 - 6: oOo0O0Ooo . IIiIiII11i + i1IiiiI1iI / oO0o % oOo0O0Ooo . ii
def oO00o00 ( ) :
 Oooo000 = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 IIii1i1 = open ( Oooo000 , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 IIii1i1 . write ( r'[' + IiII + ']' + '\n' )
 for iIIIiIi , ooO0OO , OOooooO0 , oOOo0O00o in IIi :
  oOOo0O00o = ( oOOo0O00o + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  I1II = ( iIIIiIi + '=plugin://' + IiII + '/?url=' + oOOo0O00o + '&mode=10012&name=' + ( iIIIiIi ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( ooO0OO ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( ooO0OO ) . replace ( ' ' , '' ) + '+&amp;description=' )
  IIii1i1 . write ( I1II + '\n' )
  if 2 - 2: o0ii1I . o0o00Oo0O - i1i1I1IIii1II + III1iiIii
  if 96 - 96: o0ii1I + o0ii1I
def iiiIi1Iiii1I ( ) :
 I1i111I = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o in IIi :
  oOoo000 ( '24/7' , oOOo0O00o , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 54 - 54: i1iIi - iI11I1II1I1I - Iii % o0ii1I / IIiIiII11i
def oooooO0oO0o ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def iiiIIiiIi ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def IIII1iII ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def O0ooo0Ooo ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def oOOo0OOOOo0o ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  Ii1I1i ( iIIIiIi , oOOo0O00o , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 29 - 29: III1iiIii - Iii . o0o00Oo0O . o0o00Oo0O
  if 16 - 16: ooOoO0O00 * i1iIi % oO0o + o0ii1I
def IIIi11Ii ( ) :
 if 92 - 92: i1i1I1IIii1II / Ii1I
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 6 - 6: Ii / ooOoO0O00 / III1iiIii . oOo0O0Ooo - oooOo0oo0oo % Ii
def o0OoOoOo0O ( ) :
 if 37 - 37: ooOoO0O00 . i1IiiiI1iI - IIiIiII11i % I11i - ooOoO0O00 . i1i1I1IIii1II
 I1i111I = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi , ooooOoo0OO in IIi :
  I1I1II1I11 ( iIIIiIi + '  -  ' + ( ooooOoo0OO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOOo0O00o , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 34 - 34: iI11I1II1I1I / IIiIiII11i
  if 3 - 3: I11i - ii + IiI1i11I . Iii
  if 88 - 88: Iii - IiI1i11I
def OOoOO0oOooo ( ) :
 if 34 - 34: Iii % I1ii11iIi11i + o0ii1I
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Action[/COLOR]' , 'Aksiyon' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Adventure[/COLOR]' , 'Macera' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Animation[/COLOR]' , 'Animasyon' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Anime[/COLOR]' , 'Anime' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Biography[/COLOR]' , 'Biyografi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Comedy[/COLOR]' , 'Komedi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Drama[/COLOR]' , 'Dram' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Family[/COLOR]' , 'Aile' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']History[/COLOR]' , 'Tarih' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Horror[/COLOR]' , 'Korku' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Mystery[/COLOR]' , 'Gizem' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Romance[/COLOR]' , 'Romantik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Sport[/COLOR]' , 'Spor' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Western[/COLOR]' , 'Tarih' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 93 - 93: o0ii1I - i1IiiiI1iI % o0o00Oo0O
def iiiI ( url ) :
 Ooooo = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( Ooooo )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 73 - 73: I1ii11iIi11i . i1iIi - I1ii11iIi11i % oooOo0oo0oo / Ii / iI11I1II1I1I
  if 15 - 15: i1iIi * iI11I1II1I1I * i1i1I1IIii1II
  if 96 - 96: i1IiiiI1iI * iI11I1II1I1I / OOooOOo % oooOo0oo0oo * IIiIiII11i
  if 3 - 3: oooOo0oo0oo . I1ii11iIi11i / Ii + oO0o
def i1O00oo00o000o ( ) :
 if 57 - 57: Iii - Iii % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 oOOo0O00o = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o0OO ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( oOOo0O00o )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  if o0OO in iIIIiIi . lower ( ) :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - o0ii1I * iI11I1II1I1I
   if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / i1i1I1IIii1II * I11i + oooOo0oo0oo
   if 89 - 89: i1iIi * oOo0O0Ooo . i1i1I1IIii1II
def O000O000 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1 , II11I , OoO0000O , iIIIiIi in IIi :
  I1I1iI = ( OoO0000O ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  III = ( II11I ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Oo0O = 'Season ' + III + 'Episode ' + I1I1iI + iIIIiIi
  i1iIi1iiii1ii ( Oo0O , I1 )
  if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 21 - 21: OOooOOo - Ii - OOooOOo
  if 4 - 4: Iii . III1iiIii
def i1iIi1iiii1ii ( name , url ) :
 I1 = url
 I1IIiiI1II = name
 o0o = cloudflare . source ( I1 )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for O0O0OOooOO0 , I1I1i1ii11 in i1Iii1i1I :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + I1IIiiI1II + I1I1i1ii11 + '[/COLOR]' , O0O0OOooOO0 , 222 , iiIi1IIiIi + 'dtv.png' )
  if 22 - 22: iI11I1II1I1I . o0ii1I * i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: oooOo0oo0oo + i1IiiiI1iI + Ii - Ii1I
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
def o0ii1i ( ) :
 if 11 - 11: IiI1i11I
 if 20 - 20: o0ii1I . i1IiiiI1iI % o0ii1I
 if 5 - 5: oooOo0oo0oo + IiI1i11I
 if 23 - 23: i1IiiiI1iI % iI11I1II1I1I . Iii
 if 95 - 95: I1ii11iIi11i + Ii % oooOo0oo0oo - i1i1I1IIii1II
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
 if 95 - 95: i1IiiiI1iI + III1iiIii * iI11I1II1I1I
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / o0ii1I
def iiii1ii1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 Ii1i111iI = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + ooO0OO , '' , '' )
 for url in Ii1i111iI :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 48 - 48: I1ii11iIi11i
def OooO0oO0Oo0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 Ii1i111iI = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  ooO0OO = 'http://watchepisodes.cc/' + ooO0OO
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10093 , ooO0OO , ooO0OO , '' )
 for url in Ii1i111iI :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 84 - 84: IIiIiII11i / oO0o . III1iiIii
def o0OO00oO00 ( url , iconimage ) :
 ooO0OO = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoO0000O , url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + OoO0000O + ' - ' + iIIIiIi + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , ooO0OO , '' , '' )
  if 65 - 65: Ii1I . o0ii1I / Ii + o0o00Oo0O . III1iiIii
def III11i ( url , iconimage ) :
 ooO0OO = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  if 'player' in iIIIiIi :
   pass
  elif 'vod' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , ooO0OO , '' , '' )
   if 54 - 54: i1IiiiI1iI / I11i
   if 39 - 39: oooOo0oo0oo % i1i1I1IIii1II * Ii1I - o0o00Oo0O + oOo0O0Ooo + I11i
   if 64 - 64: IIiIiII11i / IIiIiII11i
   if 52 - 52: i1IiiiI1iI * Ii1I
   if 35 - 35: I11i % oO0o
   if 27 - 27: o0ii1I - iI11I1II1I1I * o0ii1I
def oOOoo ( ) :
 if 30 - 30: I11i + o0ii1I / ii - III1iiIii % i1i1I1IIii1II
 if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
 if 15 - 15: i1iIi / i1iIi % ii . i1IiiiI1iI
 if 93 - 93: Ii1I * Ii1I / ii
 if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
 if 19 - 19: o0o00Oo0O % IIiIiII11i * I11i
 if 27 - 27: oooOo0oo0oo * III1iiIii / Ii - i1i1I1IIii1II + IIiIiII11i
 if 43 - 43: Ii1I - IIiIiII11i
 if 56 - 56: Ii1I . ooOoO0O00 / IiI1i11I % i1i1I1IIii1II / o0o00Oo0O * Iii
 if 98 - 98: o0o00Oo0O + IiI1i11I
 if 23 - 23: ii . iI11I1II1I1I / ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / Iii . oO0o
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - III1iiIii
 if 50 - 50: oOo0O0Ooo - i1i1I1IIii1II + i1i1I1IIii1II * Iii + i1i1I1IIii1II
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
 if 30 - 30: OOooOOo - Ii
def oO0OOOO00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( i1i1i1I ) )
 for url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 26 - 26: i1iIi + OOooOOo
def II111I1i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 10 - 10: o0o00Oo0O . OOooOOo * III1iiIii / i1IiiiI1iI / ooOoO0O00
def IiiIOoO00o0o0oo0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'episode' in url :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 13 - 13: Iii % i1IiiiI1iI . ooOoO0O00
  if 1 - 1: I11i % I11i . iI11I1II1I1I . ii . III1iiIii . IiI1i11I
def oooo ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOi1IIII11II1 = 'http://www.watchseriesgo.to/search/' + o0OO . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( OOi1IIII11II1 )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , oOOo0O00o , iIIIiIi in IIi :
  if 'watch online' in iIIIiIi :
   pass
  else :
   print oOOo0O00o
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.watchseriesgo.to' + oOOo0O00o , 10044 , ooO0OO , '' , '' )
   if 75 - 75: oO0o - OOooOOo - ooOoO0O00 % I1ii11iIi11i - IIiIiII11i
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 61 - 61: I1ii11iIi11i + ii / Ii
def I11OoooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , OoO0000O , O000OOO in IIi :
  O00Oo = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( OoO0000O ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + O00Oo + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , ooO0OO , '' , O000OOO )
  if 49 - 49: III1iiIii + oO0o + o0o00Oo0O
def OooOOOOOOOO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  O00Oo = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + O00Oo + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 48 - 48: i1IiiiI1iI / i1iIi . iI11I1II1I1I
def ooo0OOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , ooO0OO , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 52 - 52: oO0o
def I1O0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1i1i1I = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for II11I , O0ooOIii1iIIIi11I1 in i1i1i1I :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( O0ooOIii1iIIIi11I1 ) )
  for url , iIIIiIi in IIi :
   O00Oo = ( II11I ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + O00Oo + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 94 - 94: oO0o - IIiIiII11i % iI11I1II1I1I
class oOoo0o ( ) :
 if 57 - 57: ii % IIiIiII11i - i1IiiiI1iI
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 1 - 1: III1iiIii
  O00Oo = name
  self . Get_Sources ( oOOo0O00o , O00Oo )
  if 27 - 27: OOooOOo . i1IiiiI1iI * OOooOOo
  if 8 - 8: i1i1I1IIii1II * III1iiIii * i1iIi
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iIIIiIi in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + oOOo0O00o
   self . Get_site_link ( URL , season_name )
   if 26 - 26: IiI1i11I * oooOo0oo0oo / oooOo0oo0oo - IiI1i11I
 def Get_site_link ( self , url , season_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  i1Iii1i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  ii1I1IIii11 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for url in IIi :
   self . main ( url , season_name )
  for url in i1Iii1i1I :
   self . main ( url , season_name )
  for url in ii1I1IIii11 :
   self . main ( url , season_name )
   if 59 - 59: o0ii1I % IiI1i11I / IIiIiII11i + oOo0O0Ooo * i1iIi
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   o0o0O0o0O = 'DACLIPS'
   if o0o0O0o0O in oOoo0o . source_list :
    pass
   else :
    self . daclips ( url , season_name , o0o0O0o0O )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    o0o0O0o0O = 'THEVIDEO'
    if o0o0O0o0O in oOoo0o . source_list :
     pass
    else :
     self . thevideo ( url , season_name , o0o0O0o0O )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     o0o0O0o0O = 'ALLMYVIDEOS'
     if o0o0O0o0O in oOoo0o . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , o0o0O0o0O )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      o0o0O0o0O = 'VIDSPOT'
      if o0o0O0o0O in oOoo0o . source_list :
       pass
      else :
       self . vidspot ( url , season_name , o0o0O0o0O )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       o0o0O0o0O = 'VODLOCKER'
       if o0o0O0o0O in oOoo0o . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , o0o0O0o0O )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        o0o0O0o0O = 'VIDTO'
        if o0o0O0o0O in oOoo0o . source_list :
         pass
        else :
         self . vidto ( url , season_name , o0o0O0o0O )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 16 - 16: I11i
       else :
        if 'youwatch' in url :
         o0o0O0o0O = 'YouWatch'
         if o0o0O0o0O in oOoo0o . source_list :
          pass
         else :
          self . youwatch ( url , season_name , o0o0O0o0O )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 37 - 37: oOo0O0Ooo + ii . i1IiiiI1iI + oOo0O0Ooo . III1iiIii
          if 44 - 44: OOooOOo . i1IiiiI1iI . ooOoO0O00 . OOooOOo * i1iIi
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII , iIIIiIi in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 59 - 59: IIiIiII11i * ii - ii
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII , iIIIiIi in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 33 - 33: o0o00Oo0O . Ii % I11i
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 50 - 50: i1iIi
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * oooOo0oo0oo
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 83 - 83: Ii - oOo0O0Ooo * Ii
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . youplay ( iIIIII1iiiiII , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for iIIIII1iiiiII in IIi :
   self . Printer ( iIIIII1iiiiII , season_name , source_name )
   if 59 - 59: IiI1i11I - ii / i1iIi + Ii1I . I11i - IiI1i11I
 def Printer ( self , Link , season_name , source_name ) :
  if 29 - 29: i1i1I1IIii1II
  if Link in oOoo0o . List :
   pass
  elif source_name in oOoo0o . source_list :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   oOoo0o . List . append ( Link )
   oOoo0o . source_list . append ( source_name )
   if 26 - 26: o0o00Oo0O % oooOo0oo0oo - III1iiIii . oooOo0oo0oo
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 70 - 70: I11i + Iii / IiI1i11I + i1iIi / oOo0O0Ooo
   if 33 - 33: ii . o0o00Oo0O
   if 59 - 59: iI11I1II1I1I
   if 45 - 45: o0o00Oo0O
   if 78 - 78: Iii - iI11I1II1I1I + i1IiiiI1iI - Ii1I - i1IiiiI1iI
def Ooo00OoOOO ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 21 - 21: ii . o0o00Oo0O / Ii
def oOOOoo0 ( url ) :
 iI1i11II1i1i = '20'
 O0O0O00OoO0O = [ ]
 i1II11III = '                                                    '
 O0OO0oo = '        '
 I1I1II1I11 ( i1II11III + 'pl' + O0OO0oo + 'w' + O0OO0oo + 'd' + O0OO0oo + 'l' + O0OO0oo + 'f' + O0OO0oo + 'a' + O0OO0oo + 'pts' , '' , '' , '' , '' , '' )
 I1i111I = Oo00oo0000OO ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( I1i111I )
 for II111IiiIIi , o0oo , oOOO00o0OOO00 , O0o0o , oo0oOooo0 , O0oO0 , IIiiiI1iI , oo0oO0oo , o0O0ooo0o in IIi :
  O0Oo = O0oOo00Oo0oo0 ( o0oo )
  i111 = O0oOo00Oo0oo0 ( oOOO00o0OOO00 )
  O0oOO0o00OO = O0oOo00Oo0oo0 ( O0o0o )
  II1i11i1iI1I = O0oOo00Oo0oo0 ( oo0oOooo0 )
  oooOoO00O = O0oOo00Oo0oo0 ( O0oO0 )
  I1i1IIiiI11II = O0oOo00Oo0oo0 ( IIiiiI1iI )
  O0O0O00OoO0O . append ( II111IiiIIi [ 0 ] )
  Ii1i1 = len ( O0O0O00OoO0O )
  iiiIiIIiIiiii = int ( len ( i1II11III ) - len ( II111IiiIIi ) - 2 )
  if len ( O0O0O00OoO0O ) >= 10 :
   iiiIiIIiIiiii = iiiIiIIiIiiii - 1
  if len ( O0O0O00OoO0O ) <= int ( iI1i11II1i1i ) :
   Ii1I1i ( str ( Ii1i1 ) + ' ' + II111IiiIIi + i1II11III [ 0 : iiiIiIIiIiiii ] + o0oo + O0Oo + oOOO00o0OOO00 + i111 + O0o0o + O0oOO0o00OO + oo0oOooo0 + II1i11i1iI1I + O0oO0 + oooOoO00O + IIiiiI1iI + I1i1IIiiI11II + ' ' + o0O0ooo0o , '' , '' , '' , '' , '' )
   if 99 - 99: III1iiIii % i1IiiiI1iI
   if 61 - 61: o0o00Oo0O + oOo0O0Ooo / ii * IiI1i11I / IIiIiII11i / IiI1i11I
def O0oOo00Oo0oo0 ( space ) :
 if len ( space ) > 1 :
  ii1II1II = len ( '        ' ) - len ( space ) + 1
  space = int ( ii1II1II ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 56 - 56: IiI1i11I * Ii1I - IIiIiII11i % Ii1I
def Ii1IIiii1Ii ( ) :
 if 48 - 48: I11i + Ii1I / Ii1I
 if 80 - 80: ii
 if 65 - 65: i1i1I1IIii1II * ooOoO0O00 . ii % i1iIi
 if 87 - 87: Ii * IIiIiII11i - o0ii1I % ii
 if 55 - 55: ooOoO0O00
 if 67 - 67: oOo0O0Ooo - oO0o
 if 60 - 60: ooOoO0O00 / iI11I1II1I1I * i1i1I1IIii1II + i1iIi + ii + IIiIiII11i
 if 13 - 13: iI11I1II1I1I - oooOo0oo0oo
 if 14 - 14: i1iIi
 if 75 - 75: iI11I1II1I1I % i1iIi / oooOo0oo0oo - IiI1i11I % Ii
 if 11 - 11: Iii . o0ii1I
 if 87 - 87: oooOo0oo0oo + oooOo0oo0oo
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
 if 87 - 87: OOooOOo - oO0o * oO0o / o0ii1I . Iii * I11i
 if 21 - 21: IIiIiII11i
 if 29 - 29: OOooOOo % o0ii1I
 if 7 - 7: ooOoO0O00 / III1iiIii / IiI1i11I
 if 97 - 97: oO0o + iI11I1II1I1I
 if 79 - 79: i1iIi + i1i1I1IIii1II - IIiIiII11i . I1ii11iIi11i
 if 26 - 26: III1iiIii
 if 52 - 52: o0o00Oo0O + i1iIi
 if 11 - 11: ooOoO0O00 / i1IiiiI1iI * Ii1I * i1IiiiI1iI * i1iIi - Ii
 if 96 - 96: Ii1I % Ii1I
 if 1 - 1: oOo0O0Ooo . o0ii1I
 if 26 - 26: i1i1I1IIii1II - i1iIi % I1ii11iIi11i - i1i1I1IIii1II + III1iiIii
 if 33 - 33: o0ii1I + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * III1iiIii
 if 21 - 21: o0o00Oo0O * i1iIi % oO0o
 if 14 - 14: o0o00Oo0O / i1IiiiI1iI / i1iIi + III1iiIii - III1iiIii
 if 10 - 10: o0o00Oo0O - Ii1I / i1IiiiI1iI % OOooOOo / ii / o0ii1I
 if 73 - 73: i1iIi + III1iiIii % I11i . Ii1I / oooOo0oo0oo . i1IiiiI1iI
 if 76 - 76: Iii . Ii1I * ii % IiI1i11I
 if 24 - 24: ii
 if 83 - 83: o0o00Oo0O / oO0o
 if 62 - 62: Iii
 if 73 - 73: o0ii1I % oO0o * oooOo0oo0oo
 if 84 - 84: I1ii11iIi11i
 if 18 - 18: ii
 if 85 - 85: ii . oO0o . oO0o
 if 70 - 70: Iii
 if 72 - 72: i1IiiiI1iI - i1iIi - oOo0O0Ooo - IiI1i11I + oooOo0oo0oo - ooOoO0O00
 if 45 - 45: oO0o * oOo0O0Ooo
 if 61 - 61: IiI1i11I % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
 if 74 - 74: Ii1I * i1i1I1IIii1II + IiI1i11I % o0o00Oo0O
 if 18 - 18: ooOoO0O00 % III1iiIii . o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - IIiIiII11i
 if 55 - 55: OOooOOo . iI11I1II1I1I * oooOo0oo0oo % iI11I1II1I1I . oO0o
 if 43 - 43: o0ii1I . oooOo0oo0oo + oOo0O0Ooo * Ii
 if 2 - 2: oooOo0oo0oo
 if 3 - 3: oOo0O0Ooo . IiI1i11I % o0o00Oo0O - i1iIi / o0o00Oo0O
 if 79 - 79: o0ii1I + i1i1I1IIii1II % i1iIi % oOo0O0Ooo
 if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
 if 53 - 53: IiI1i11I . i1i1I1IIii1II / I1ii11iIi11i . oO0o . Ii
 if 60 - 60: IIiIiII11i
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 if 57 - 57: IIiIiII11i . ooOoO0O00
 if 33 - 33: IiI1i11I + I1ii11iIi11i % Iii . i1i1I1IIii1II
 if 6 - 6: III1iiIii + Ii1I
 if 62 - 62: i1i1I1IIii1II . i1IiiiI1iI - ii * IIiIiII11i . Ii
 if 13 - 13: iI11I1II1I1I * I11i - Ii
 if 63 - 63: ii * i1IiiiI1iI
 if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . i1i1I1IIii1II % IIiIiII11i
 if 18 - 18: Iii % ii + oO0o / Iii
 if 37 - 37: ooOoO0O00 - o0ii1I / III1iiIii . IIiIiII11i % i1iIi
 if 39 - 39: o0ii1I % Ii * oO0o
 if 23 - 23: oooOo0oo0oo + i1iIi / Ii * I1ii11iIi11i . oO0o
 if 28 - 28: IiI1i11I - I11i
 if 92 - 92: I1ii11iIi11i % I11i - i1iIi / i1iIi / OOooOOo
 if 84 - 84: oooOo0oo0oo
 if 4 - 4: III1iiIii . i1IiiiI1iI / o0ii1I / IiI1i11I + IIiIiII11i
 if 32 - 32: ooOoO0O00 + iI11I1II1I1I . Ii1I . Iii - o0ii1I
 if 55 - 55: Ii1I / ii - oO0o / oOo0O0Ooo
 if 23 - 23: Iii * i1IiiiI1iI * I11i - oOo0O0Ooo % OOooOOo + I11i
 if 41 - 41: III1iiIii * ii . i1iIi % Ii
 if 11 - 11: iI11I1II1I1I . i1IiiiI1iI - I1ii11iIi11i / Iii + IIiIiII11i
 if 29 - 29: Iii . Ii + ooOoO0O00 - o0ii1I + o0o00Oo0O . oOo0O0Ooo
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOOo0O00o , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooO0OO , Oo00OOOOO , '' )
  if 8 - 8: I11i
def ooOO0O0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1i1i1I in i1i1i1I :
  OoOOOO0O0oO0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( i1i1i1I ) )
  for IIIiIIIi111iI in OoOOOO0O0oO0 :
   IIIiIIIi111iI = IIIiIIIi111iI
  II1IIII1i1i = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
  for IiIiI1i1ii , ooO0OO , time , i1oO in II1IIII1i1i :
   I1ii1Ii1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( i1oO )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IIIiIIIi111iI + ' - ' + IiIiI1i1ii + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + ooO0OO , Oo00OOOOO , ( str ( I1ii1Ii1 ) ) )
   if 46 - 46: o0o00Oo0O % ii
 I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if 22 - 22: IiI1i11I + ii - OOooOOo - oO0o * i1IiiiI1iI - i1i1I1IIii1II
def O0ooOOOo000OOoOO ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 if 13 - 13: I1ii11iIi11i
def oO0OooO00Oo ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  oO0OO00O0 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIIIiIi :
   pass
  else :
   oO0OO00O0 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + oO0OO00O0 + '[/COLOR]' , url , 10013 , ooO0OO )
 for url , ooO0OO , iIIIiIi in i1Iii1i1I :
  oO0OO00O0 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIIIiIi :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + oO0OO00O0 + '[/COLOR]' , url , 10013 , ooO0OO )
def O000oOo0OO ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 57 - 57: Ii1I
 if 30 - 30: Ii1I * III1iiIii % III1iiIii * IiI1i11I . IiI1i11I
 if 23 - 23: oO0o % i1iIi - i1i1I1IIii1II . Ii1I . ii
 if 65 - 65: III1iiIii + ii - ooOoO0O00
 if 57 - 57: i1i1I1IIii1II / oooOo0oo0oo / oooOo0oo0oo * I11i * Ii1I - Ii
 if 82 - 82: oOo0O0Ooo . oO0o
 if 67 - 67: Ii1I * Ii + o0ii1I % o0ii1I + iI11I1II1I1I - oooOo0oo0oo
 for url , ooO0OO , iIIIiIi in i1Iii1i1I :
  oO0OO00O0 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIIIiIi :
   pass
  else :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + oO0OO00O0 + '[/COLOR]' , url , 10013 , ooO0OO )
   if 10 - 10: oOo0O0Ooo - i1IiiiI1iI - Ii1I / IiI1i11I
def I11iI1i11IiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for O0O0OOooOO0 in IIi :
  O000o = ( O0O0OOooOO0 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  IiiI ( 'http:' + O000o )
  if 76 - 76: oooOo0oo0oo
  if 52 - 52: I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
  if 9 - 9: IiI1i11I - IiI1i11I
  if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + i1i1I1IIii1II
def IIi1iii ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  OooOo00o ( iIIIiIi , url , 8046 , ooO0OO )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def ii1Ii ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  IiiI ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 41 - 41: Ii1I % Ii1I + III1iiIii . IiI1i11I % i1IiiiI1iI * i1iIi
def O0Ii1iIii1I1 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I1i111I )
 for url in IIi :
  yt . PlayVideo ( url )
  if 21 - 21: OOooOOo + OOooOOo * i1iIi / oooOo0oo0oo * ii . I1ii11iIi11i
def I1iiIIIi11 ( ) :
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 oOoo000 ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1iII1IiI1I ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + ooO0OO )
 for url in next :
  oOoo000 ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 31 - 31: ii % Ii - IIiIiII11i * Ii
  if 82 - 82: o0o00Oo0O / oooOo0oo0oo + IiI1i11I
def I11II1i1I11I1 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i111I )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def i1iI1I1I ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , '' )
  if 24 - 24: III1iiIii % III1iiIii - IiI1i11I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Iii11I1I11I1I1 ( name , url ) :
 ii1IiIi1iIi = 0
 name = name
 url = url
 oOOoo00O00o = [ '144' , '240' , '380' , '480' , '720' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  I11iiiiI1i ( url )
  if 16 - 16: oooOo0oo0oo % oOo0O0Ooo . i1IiiiI1iI * oO0o % o0o00Oo0O . oooOo0oo0oo
  if 94 - 94: Ii1I
  if 33 - 33: Ii1I + Ii1I . o0ii1I
  if 27 - 27: IIiIiII11i - Ii - ii
  if 90 - 90: oOo0O0Ooo
  if 4 - 4: oooOo0oo0oo % i1iIi - oooOo0oo0oo - I11i
  if 30 - 30: III1iiIii
  if 34 - 34: i1i1I1IIii1II - IIiIiII11i - I11i + IiI1i11I + i1IiiiI1iI
def oo0OOo ( ) :
 I1i111I = oOOo000oOoO0 ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  if 'genre' in oOOo0O00o :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oOOo0O00o , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOIiI1IIIiI1I1i ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , ooO0OO )
 for url in next :
  oOoo000 ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 84 - 84: OOooOOo - Iii
def OoO00O00O0 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( I1i111I )
 for url in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  i1iI1I1I ( url )
  if 76 - 76: oOo0O0Ooo % Ii + oooOo0oo0oo
def I11iIIi1Iii ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ooIII1II1iii1i = 'http://documentarylovers.com/?s=' + ( o0OO ) . replace ( ' ' , '+' )
 Oo = ooIII1II1iii1i . lower ( )
 OOIiI1IIIiI1I1i ( Oo )
 if 96 - 96: IiI1i11I % IiI1i11I % i1IiiiI1iI / i1IiiiI1iI - Ii1I
def i11i1 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if 'films' in url :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def O0O0I1II ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  if 'films' in url :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + ooO0OO )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def o0o0OoOO00Oo ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1i111I )
 for url in IIi :
  if 'rtd' in url :
   i1iiIi1II1 ( url )
   if 12 - 12: Ii + Iii - Ii1I
def i1iiIi1II1 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( I1i111I )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  I11iiiiI1i ( url )
  if 27 - 27: IiI1i11I
  if 22 - 22: OOooOOo / oOo0O0Ooo
def iI11I1IiI1 ( ) :
 II11iIiIIIiI = oOOo000oOoO0 ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi , iIIIiIi1I1i in IIi :
  oOoo000 ( ( iIIIiIi + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi1I1i + '[/COLOR]' ) , oOOo0O00o , 8086 , ooO0OO )
  if 5 - 5: IiI1i11I / i1i1I1IIii1II % i1iIi . Ii % OOooOOo + i1i1I1IIii1II
def oOo0oOoo0 ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 8087 , ooO0OO )
  if 53 - 53: ii + oOo0O0Ooo . IiI1i11I % o0o00Oo0O + o0ii1I / I11i
def oooOOO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  OO00o0 ( url , iIIIiIi )
  if 62 - 62: i1iIi . i1IiiiI1iI
def OO00o0 ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 97 - 97: oOo0O0Ooo + III1iiIii . Ii * I1ii11iIi11i % ooOoO0O00
def oo00000ooOooO ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oOOo0O00o , 3002 , 'http://www.solie.org/alibrary/' + ooO0OO )
def oo0o0OO00oOO ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ooO0OO )
def IiiII1iIi ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 OoO00oooo0o = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I1i111I )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , iIIIiIi in OoO00oooo0o :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']Season- ' + iIIIiIi + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , ooO0OO , iIIIiIi in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ooO0OO )
def iiiiii ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i111I )
 for url in IIi :
  ooII1 ( url )
def ooII1 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I1i111I )
 for url in IIi :
  I11iiiiI1i ( url )
  if 90 - 90: Iii / i1i1I1IIii1II + OOooOOo
def I1iIiIi11i11 ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOOo0O00o , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def IiII11I1I1IIi ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( I1i111I )
 for url in IIi :
  OoOoooO000OO ( url )
  if 44 - 44: OOooOOo
def O00oOo00o0o ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOOo0O00o , 8065 , iiIi1IIiIi + 'classictv.png' )
def I111 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  if 'mp4' in url :
   I11iiiiI1i ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 66 - 66: i1IiiiI1iI * ii / Ii1I - Iii - i1iIi * Iii
def OOoOooO0o ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oOOo0O00o , 8071 , iiIi1IIiIi + 'streams.png' )
def OOoOI1i1i1Iii1 ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  if '(Free Access)' in iIIIiIi :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def OoO00Ooooo ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , ooO0OO , IIo0o0O0O00oOOo , '' )
  if 25 - 25: I11i + iI11I1II1I1I + III1iiIii + Ii1I / i1IiiiI1iI - ooOoO0O00
def Ii1I11Ii1iI ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  OOOOOo00OOoO ( 'http://watchxxxfree.com/categories' )
 if O0O00Oo == 1 :
  i111iii1I11I ( 'http://www.perfectgirls.net' )
 if O0O00Oo == 2 :
  iii111iiI11I ( 'http://www.xvideos.com/best' )
 if O0O00Oo == 3 :
  iII1i ( 'http://www.xvideos.com/best' )
 if O0O00Oo == 4 :
  iii111iiI11I ( 'http://www.xvideos.com/best' )
 if O0O00Oo == 5 :
  iii111iiI11I ( 'http://www.xvideos.com/verified/videos' )
 if O0O00Oo == 6 :
  oOii1iiiiii ( 'http://www.xvideos.com/tags' )
 if O0O00Oo == 7 :
  OOOoO0o ( 'http://www.xvideos.com/porn' )
 if O0O00Oo == 8 :
  iiioO000oO0oO ( )
  if 44 - 44: oooOo0oo0oo - III1iiIii + IiI1i11I
  if 78 - 78: o0ii1I
  if 29 - 29: IIiIiII11i
  if 79 - 79: iI11I1II1I1I - Ii + i1iIi - IIiIiII11i . iI11I1II1I1I
  if 84 - 84: I1ii11iIi11i % Iii * o0o00Oo0O * Iii
  if 66 - 66: oooOo0oo0oo / iI11I1II1I1I - OOooOOo % o0o00Oo0O . i1iIi
  if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
  if 37 - 37: ooOoO0O00 * Ii
  if 95 - 95: Ii % i1IiiiI1iI * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
def II1iiiiI1Ii11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'ch' in url :
   i1ioO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def O0oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for iIIIiIi , url in III1II1iiI11 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def iiIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   ooO00Oo ( url )
def IIiI1iiIII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiiiI1i ( url )
def OOOOOo00OOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , ii1II1II in IIi :
  if 'category' in url :
   i1ioO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORorange]   ' + ii1II1II + '[/COLOR]' , url , 90006 , ooO0OO , iiIi1IIiIi + 'Jizbox.png' , '' )
def oo0OooOoOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , ooO0OO , '' , '' )
 for url in III1II1iiI11 :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def iIIii1i1iIiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   ooO00Oo ( url )
def ooO00Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiiiI1i ( url )
def i111iii1I11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ii1II1II in IIi :
  if 'category' in url :
   i1ioO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORorange]' + ii1II1II + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def oOooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1 = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , ooO0OO , '' , '' )
 for url in III1II1iiI11 :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , I1 + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iI1iII1 ( 'http://www.perfectgirls.net' + url )
def iI1iII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  IiiI ( 'http://' + url )
def OOOoO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ii1II1II in IIi :
  i1ioO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - No of Videos : [COLORorange]' + ii1II1II + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def oOii1iiiiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 III1II1iiI11 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in III1II1iiI11 :
  i1ioO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ii1II1II in IIi :
  i1ioO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - No of Videos : [COLORorange]' + ( ii1II1II + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 70 - 70: i1iIi . oO0o + oOo0O0Ooo
def I1iIIiiiIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 III1II1iiI11 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in III1II1iiI11 :
  i1ioO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , oooO0 in IIi :
  i1ioO ( iIIIiIi + '--' + ( oooO0 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( ooO0OO ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 95 - 95: Iii
  if 76 - 76: IIiIiII11i - ooOoO0O00 . o0o00Oo0O * Ii % I11i - IiI1i11I
def iii111iiI11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , i11i1i , I1II1IIiI11 in IIi :
  i1ioO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - Porn Quality : [COLORorange]' + I1II1IIiI11 + ' - [COLORred]' + i11i1i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , ooO0OO , ooO0OO , I1II1IIiI11 + ' - ' + i11i1i )
 IIIiiiiiiii1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in IIIiiiiiiii1 :
  i1ioO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 97 - 97: Ii1I - i1iIi * Ii + i1IiiiI1iI % ii
def iII1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1i1I = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 III1II1iiI11 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in III1II1iiI11 :
  i1ioO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( i1i1i1I ) )
 for url , iIIIiIi in IIi :
  if '/c/' in url :
   i1ioO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . oooOo0oo0oo
   if 3 - 3: o0o00Oo0O - i1IiiiI1iI * o0ii1I * oooOo0oo0oo / o0ii1I
def iiioO000oO0oO ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Ooo000OO00 = ( o0OO ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 Oo = O0Ooo000OO00 . lower ( )
 IIiiiII11i = 'http://www.xvideos.com/?k=' + Oo
 print IIiiiII11i + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( IIiiiII11i )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , oOOo0O00o , iIIIiIi , i11i1i , I1II1IIiI11 in IIi :
  i1ioO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - Porn Quality : [COLORorange]' + I1II1IIiI11 + ' - [COLORred]' + i11i1i + '[/COLOR]' , 'http://www.xvideos.com' + oOOo0O00o , 10108 , ooO0OO , ooO0OO , I1II1IIiI11 + ' - ' + i11i1i )
 IIIiiiiiiii1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in IIIiiiiiiii1 :
  i1ioO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oOOo0O00o , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 51 - 51: i1iIi * III1iiIii * iI11I1II1I1I / OOooOOo % III1iiIii
if 36 - 36: Ii1I * I11i + Ii + ii
if 82 - 82: OOooOOo . OOooOOo
if 10 - 10: I1ii11iIi11i * Ii1I . i1i1I1IIii1II . ii . oooOo0oo0oo * Ii1I
if 80 - 80: i1IiiiI1iI + Iii . i1IiiiI1iI + oooOo0oo0oo
if 85 - 85: Ii . Iii + o0ii1I / o0ii1I
if 43 - 43: III1iiIii . ii - IIiIiII11i
if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * oooOo0oo0oo * i1i1I1IIii1II
if 19 - 19: i1IiiiI1iI * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
if 15 - 15: o0ii1I + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
if 54 - 54: III1iiIii - IIiIiII11i . i1iIi + o0ii1I
if 45 - 45: i1i1I1IIii1II + IIiIiII11i . IiI1i11I / Ii1I
if 76 - 76: o0ii1I + IiI1i11I - III1iiIii * iI11I1II1I1I % ooOoO0O00
if 72 - 72: i1iIi + IIiIiII11i . o0o00Oo0O - IiI1i11I / ii . i1IiiiI1iI
if 28 - 28: iI11I1II1I1I . o0o00Oo0O
if 32 - 32: ii
if 29 - 29: Ii1I
if 41 - 41: o0ii1I
if 49 - 49: o0ii1I % IIiIiII11i . o0ii1I - I11i - Iii * III1iiIii
if 47 - 47: o0o00Oo0O . I11i / o0ii1I * IiI1i11I
if 63 - 63: i1IiiiI1iI - i1i1I1IIii1II - IiI1i11I - i1iIi / i1i1I1IIii1II + oO0o
if 94 - 94: III1iiIii / oOo0O0Ooo . IIiIiII11i
if 32 - 32: i1i1I1IIii1II . oooOo0oo0oo % oooOo0oo0oo . OOooOOo
if 37 - 37: oooOo0oo0oo + o0o00Oo0O + oooOo0oo0oo . IiI1i11I . I11i
if 78 - 78: oOo0O0Ooo / Iii + I11i . I1ii11iIi11i / o0o00Oo0O
if 49 - 49: Ii1I
if 66 - 66: I11i . Ii1I
if 18 - 18: I1ii11iIi11i + III1iiIii
if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % o0ii1I . oOo0O0Ooo
if 43 - 43: oOo0O0Ooo % Ii1I * o0ii1I
if 31 - 31: o0ii1I / IiI1i11I
if 3 - 3: III1iiIii
if 37 - 37: o0ii1I * ii * Iii + I1ii11iIi11i . oOo0O0Ooo
if 61 - 61: oooOo0oo0oo . oooOo0oo0oo
def ii11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in ii1I1IIii11 :
  if 'http' in url :
   OooOo00o ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 43 - 43: OOooOOo % o0ii1I + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
def OOOOo00oOOO00 ( url ) :
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 try : iIIIi1i1I11i . play ( url )
 except : pass
 if 13 - 13: Ii1I / oO0o * Ii % oO0o % oO0o * IIiIiII11i
 if 17 - 17: Iii . o0o00Oo0O * ooOoO0O00 - OOooOOo % ooOoO0O00
def I1iI1I ( ) :
 if 37 - 37: oOo0O0Ooo - iI11I1II1I1I
 if 56 - 56: III1iiIii - o0ii1I + Ii * oO0o % oOo0O0Ooo
 if 37 - 37: iI11I1II1I1I + III1iiIii / i1IiiiI1iI . ii
 if 72 - 72: i1i1I1IIii1II % i1iIi % oooOo0oo0oo
 if 63 - 63: oO0o . o0ii1I % IIiIiII11i / Iii - OOooOOo
 if 4 - 4: I1ii11iIi11i - o0o00Oo0O / Iii + o0o00Oo0O - i1i1I1IIii1II * I1ii11iIi11i
 if 25 - 25: oOo0O0Ooo
 if 64 - 64: i1i1I1IIii1II
 if 80 - 80: I11i % iI11I1II1I1I
 if 63 - 63: III1iiIii * Ii
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 8091 , iiIi1IIiIi + 'gofish.png' )
def O0O0OOo00Oo ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 8092 , ooO0OO )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def IiI1iIIiIi1Ii ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0oOoOOO000 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO in O0oOoOOO000 :
  ooO0OO = ooO0OO
 for url , iIIIiIi in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 8092 , ooO0OO )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 57 - 57: I11i - III1iiIii . oooOo0oo0oo
def IIiIi ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 45 - 45: I1ii11iIi11i
  if 4 - 4: Iii
  if 60 - 60: IIiIiII11i + i1IiiiI1iI / i1i1I1IIii1II % ii - ooOoO0O00
  if 57 - 57: i1iIi
OO00O0O = '{PQ},' ; o0oo0oo0 = '{SC},' ; IIi1II = '{XG},' ; OOOoooO0o0o = '{JP},' ; OOoOoOO00 = '{HW},' ; o0O00 = '{RT},'
def O00OoO0o ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 i1oOOOOOOOoO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 oOOo0O00o = 'http://onlinemovies.tube/?s=' + ( o0OO ) . replace ( ' ' , '+' )
 I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 IIiI = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 O0oOOo0o = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 I1III11iiii11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 ooOo0OoO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1iiIIi1I = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o0OO
 iiI1I1IIi11i1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 i1II1iii1i = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 4 - 4: Ii % IiI1i11I
 ooO0000o00O = ( i11 ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 O0Ooo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 41 - 41: IiI1i11I + i1IiiiI1iI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 o0o = O00O0oOO00O00 ( I1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source Technica " )
 i1iiIIIi = O00O0oOO00O00 ( I1 )
 o0oOoO00o . update ( 32 , "" , "Checking Source Pandoras Box " )
 o00OooOO000 = O00O0oOO00O00 ( IIiI )
 o0oOoO00o . update ( 59 , "" , "Checking Source Lazy List " )
 OOoOoo = O00O0oOO00O00 ( O0oOOo0o )
 o0oOoO00o . update ( 72 , "" , "Checking Source RaizTv " )
 Oo0o = O00O0oOO00O00 ( i1II1iii1i )
 o0oOoO00o . update ( 91 , "" , "Checking WebSpace " )
 if 96 - 96: o0o00Oo0O + oooOo0oo0oo . i1iIi + oooOo0oo0oo
 if 43 - 43: Ii
 if 65 - 65: o0o00Oo0O / IiI1i11I . ooOoO0O00 * IiI1i11I / iI11I1II1I1I - i1i1I1IIii1II
 if 93 - 93: OOooOOo % Ii - o0ii1I % oO0o
 if 55 - 55: I11i . Ii1I
 if 63 - 63: i1i1I1IIii1II
 if 79 - 79: Ii1I - i1i1I1IIii1II - I11i . oooOo0oo0oo
 if 65 - 65: Ii . oO0o % IiI1i11I + III1iiIii - Ii
 o0Oo0oOooOoOo = O00O0oOO00O00 ( O0Ooo )
 if 60 - 60: i1IiiiI1iI
 if Oo0o != 'Failed' :
  Iiii1ii = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oo0o )
  for oOOo0O00o , iIIIiIi in Iiii1ii :
   I1i111IiIiIi1 = O00O0oOO00O00 ( oOOo0O00o )
   i1II11II1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1i111IiIiIi1 )
   for II1IIIii , iIIIiIi1I1i in i1II11II1 :
    iIIIiIi1I1i = ( iIIIiIi1I1i . replace ( '.' , ' ' ) )
    if Oo in iIIIiIi1I1i . lower ( ) :
     if '.mkv' in II1IIIii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + II1IIIii , 222 , '' , '' , '' )
     elif '.mp4' in II1IIIii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + II1IIIii , 222 , '' , '' , '' )
     elif '.avi' in II1IIIii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + II1IIIii , 222 , '' , '' , '' )
     elif '.wav' in II1IIIii :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + II1IIIii , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + II1IIIii , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting WebSpace Links" )
      if 14 - 14: I1ii11iIi11i % i1i1I1IIii1II * IiI1i11I - Ii / Ii1I * Ii
      I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in i1Iii1i1I :
   if o0OO in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source Technica[/COLOR]' ) , oOOo0O00o , 222 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * Iii + oooOo0oo0oo
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 14 - 14: o0ii1I - o0o00Oo0O
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for I1Ii , iIIIiIi in ii1I1IIii11 :
   if o0OO in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IIiI + I1Ii ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Lazy List Links" )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in II1i11I :
   if o0OO in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source RaizTv[/COLOR]' ) , oOOo0O00o , 222 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: i1IiiiI1iI * Iii / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
    if 49 - 49: o0ii1I / IiI1i11I . IiI1i11I . IiI1i11I + Ii % Iii
    if 7 - 7: III1iiIii * i1iIi + OOooOOo
    if 22 - 22: IiI1i11I
    if 48 - 48: Ii1I . oOo0O0Ooo
    if 73 - 73: o0o00Oo0O . i1IiiiI1iI - ii % Iii % ooOoO0O00
    if 14 - 14: i1IiiiI1iI + o0ii1I * I1ii11iIi11i
    if 49 - 49: I1ii11iIi11i
    if 57 - 57: o0o00Oo0O * i1iIi - IiI1i11I - iI11I1II1I1I * IiI1i11I
    if 9 - 9: III1iiIii . Iii
    if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
    if 96 - 96: i1iIi % o0o00Oo0O
    if 51 - 51: oOo0O0Ooo - IiI1i11I / Ii1I . Ii1I + Ii1I
    if 87 - 87: IIiIiII11i . o0ii1I * oO0o
    if 74 - 74: I11i % OOooOOo . IiI1i11I % i1IiiiI1iI . o0o00Oo0O % IIiIiII11i
    if 5 - 5: i1i1I1IIii1II - ii / OOooOOo
    if 30 - 30: Iii % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
    if 55 - 55: oO0o
    if 20 - 20: i1iIi * i1IiiiI1iI * I11i - i1iIi
    if 32 - 32: o0ii1I * i1i1I1IIii1II
    if 85 - 85: Ii . oO0o + oO0o
    if 28 - 28: I1ii11iIi11i
    if 62 - 62: I1ii11iIi11i + ii / IiI1i11I
    if 60 - 60: o0ii1I / OOooOOo . Iii % oooOo0oo0oo
    if 61 - 61: o0o00Oo0O . o0ii1I . o0o00Oo0O * Ii * IIiIiII11i / i1IiiiI1iI
    if 69 - 69: Iii
    if 17 - 17: Iii
    if 38 - 38: i1IiiiI1iI % oooOo0oo0oo
    if 9 - 9: o0o00Oo0O . iI11I1II1I1I
    if 44 - 44: Ii1I % III1iiIii
    if 6 - 6: oO0o
    if 82 - 82: iI11I1II1I1I . Iii / III1iiIii / oooOo0oo0oo * IIiIiII11i % i1i1I1IIii1II
    if 62 - 62: IIiIiII11i
    if 96 - 96: Iii % OOooOOo * Ii1I
    if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . i1iIi
    if 63 - 63: Ii % Ii1I % oOo0O0Ooo . III1iiIii * I11i + oooOo0oo0oo
    if 77 - 77: I11i
    if 63 - 63: i1iIi * i1i1I1IIii1II + i1iIi * o0ii1I + I1ii11iIi11i / Ii1I
    if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
    if 65 - 65: i1IiiiI1iI + o0o00Oo0O % I11i
 o0O0O0 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 72 - 72: oooOo0oo0oo . OOooOOo / IIiIiII11i
 for iiIiI in o0O0O0 :
  o0Ooo0O00 = oO0 + iiIiI + oOoOooOo0o0
  Oo0o = O00O0oOO00O00 ( o0Ooo0O00 )
  if Oo0o != 'Failed' :
   Iiii1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0o )
   for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in Iiii1ii :
    if o0OO in iIIIiIi . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , oOOo0O00o , 222 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 69 - 69: oooOo0oo0oo * IIiIiII11i - i1iIi - ooOoO0O00 + Ii
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 50 - 50: ii * ooOoO0O00 / i1i1I1IIii1II
 o0O0O0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 83 - 83: ooOoO0O00
 if 38 - 38: ii * iI11I1II1I1I
 for iiIiI in o0O0O0 :
  o0Ooo0O00 = i1oOOOOOOOoO + iiIiI
  I1iI = O00O0oOO00O00 ( o0Ooo0O00 )
  if I1iI != 'Failed' :
   oO0Ooo0OooOOo = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( I1iI )
   for I1Ii , iIIIiIi in oO0Ooo0OooOOo :
    if o0OO in iIIIiIi . lower ( ) :
     OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( i1oOOOOOOOoO + iiIiI + I1Ii ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 54 - 54: ii . i1IiiiI1iI
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: o0ii1I
def OoOoO ( ) :
 if 31 - 31: Iii . Ii . oO0o * I1ii11iIi11i % o0ii1I . I11i
 if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
 if 93 - 93: i1iIi % i1IiiiI1iI
 if 46 - 46: Ii1I * OOooOOo * III1iiIii * Ii1I . Ii1I
 if 43 - 43: i1iIi . ooOoO0O00
 if 68 - 68: III1iiIii % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
 if 45 - 45: oOo0O0Ooo
 if 17 - 17: ii - i1iIi + o0ii1I . ii % I1ii11iIi11i
 if 92 - 92: i1IiiiI1iI - oooOo0oo0oo % oO0o - I11i % ooOoO0O00
 if 38 - 38: Ii1I . Iii / OOooOOo % Iii
 if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / IiI1i11I
 if 61 - 61: I1ii11iIi11i - i1IiiiI1iI
 if 51 - 51: IiI1i11I * i1iIi / o0o00Oo0O / o0o00Oo0O
 if 52 - 52: ii % o0o00Oo0O
 if 56 - 56: i1i1I1IIii1II - ooOoO0O00 * ii - IIiIiII11i
 if 28 - 28: ooOoO0O00 / Iii . I11i
 if 11 - 11: I1ii11iIi11i * ii - Ii
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 if 13 - 13: Ii . o0o00Oo0O / oooOo0oo0oo * ooOoO0O00
 if 14 - 14: III1iiIii + III1iiIii . Iii / o0ii1I . iI11I1II1I1I
 II1IIIii = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( o0OO ) . replace ( ' ' , '+' )
 I1 = 'http://onlinemovies.tube/?s=' + ( o0OO ) . replace ( ' ' , '+' )
 IIiI = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 O0oOOo0o = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 ooOo0OoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 10 - 10: IIiIiII11i . oooOo0oo0oo / IiI1i11I
 iiI1I1IIi11i1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 i1II1iii1i = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 35 - 35: IiI1i11I / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 3 - 3: Ii1I
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 42 - 42: Iii % I1ii11iIi11i + III1iiIii - Iii . iI11I1II1I1I - o0ii1I
 if 27 - 27: IiI1i11I % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
 oo0o = O00O0oOO00O00 ( II1IIIii )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( I1 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( IIiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( O0oOOo0o )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 I1iI = O00O0oOO00O00 ( ooOo0OoO )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 37 - 37: IiI1i11I + i1IiiiI1iI * o0ii1I + III1iiIii
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + o0ii1I / IIiIiII11i
 i1iiIIIi = O00O0oOO00O00 ( iiI1I1IIi11i1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 Oo0o = O00O0oOO00O00 ( i1II1iii1i )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 66 - 66: i1iIi + i1i1I1IIii1II % ii
 if 23 - 23: i1i1I1IIii1II . OOooOOo + iI11I1II1I1I
 if Oo0o != 'Failed' :
  Iiii1ii = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( Oo0o )
  for oOOo0O00o , iIIIiIi in Iiii1ii :
   I1i111IiIiIi1 = O00O0oOO00O00 ( oOOo0O00o )
   i1II11II1 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( I1i111IiIiIi1 )
   for II1IIIii , iIIIiIi1I1i in i1II11II1 :
    if Oo in iIIIiIi1I1i . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + iIIIiIi1I1i + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + II1IIIii , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 17 - 17: III1iiIii
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if i1iiIIIi != 'Failed' :
  i1i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iiIIIi )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in i1i1 :
   if Oo in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source HeroVision[/COLOR]' ) , oOOo0O00o , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 12 - 12: ooOoO0O00 . oO0o
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 14 - 14: oooOo0oo0oo + IIiIiII11i % oooOo0oo0oo . i1i1I1IIii1II * i1iIi
    if 54 - 54: i1iIi * Iii - i1IiiiI1iI
    if 15 - 15: IiI1i11I / o0o00Oo0O
    if 61 - 61: ooOoO0O00 / ooOoO0O00 + i1iIi . i1IiiiI1iI * i1iIi
    if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
    if 82 - 82: o0o00Oo0O / IiI1i11I * oO0o - Iii + I1ii11iIi11i
    if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + o0ii1I * IIiIiII11i
    if 78 - 78: i1IiiiI1iI - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
    if 97 - 97: ooOoO0O00
    if 29 - 29: oOo0O0Ooo
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  oO000o0Oo00 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for oOOo0O00o , ooO0OO , iIIIiIi , OooO0O in i1Iii1i1I :
   if Oo in iIIIiIi . lower ( ) :
    if 'season' in OooO0O :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOOo0O00o , 90054 , ooO0OO , ooO0OO , '' )
    if 'episodes' in OooO0O :
     oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOOo0O00o , 90044 , ooO0OO , ooO0OO , '' )
  for oOOo0O00o in oO000o0Oo00 :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oOOo0O00o , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 37 - 37: Ii1I * i1IiiiI1iI * oOo0O0Ooo * o0o00Oo0O
   I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  oOo0 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( oo0o )
  for oOOo0O00o , iIIIiIi , ooO0OO in oOo0 :
   if Oo in iIIIiIi . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( iIIIiIi ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oOOo0O00o , 8022 , ooO0OO , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 35 - 35: oOo0O0Ooo - Ii1I * IiI1i11I + III1iiIii / ooOoO0O00
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 46 - 46: I1ii11iIi11i . i1iIi % I1ii11iIi11i / IIiIiII11i * i1iIi * oooOo0oo0oo
    if 59 - 59: i1IiiiI1iI * IiI1i11I
    if 31 - 31: Iii / o0o00Oo0O
    if 57 - 57: ooOoO0O00 % i1iIi
    if 69 - 69: I11i
    if 69 - 69: i1IiiiI1iI
    if 83 - 83: iI11I1II1I1I . I11i + i1IiiiI1iI . ii / i1iIi + IIiIiII11i
    if 90 - 90: o0ii1I * IiI1i11I / oooOo0oo0oo
    if 68 - 68: OOooOOo
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for iIIIiIi in ii1I1IIii11 :
   if Oo in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( IIiI + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 65 - 65: i1i1I1IIii1II
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for iIIIiIi in II1i11I :
   if Oo in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( O0oOOo0o + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 82 - 82: I11i
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if I1iI != 'Failed' :
  oO0Ooo0OooOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1iI )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in oO0Ooo0OooOOo :
   if Oo in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] Source Scooby[/COLOR]' ) , oOOo0O00o , 1016 , iiiI1I1iIIIi1 , i11i1iIiii , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + i1IiiiI1iI
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 65 - 65: o0ii1I
 Oo00ooO0OoOo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for iiIiI in Oo00ooO0OoOo :
  o0Ooo0O00 = oO0 + iiIiI + oOoOooOo0o0
  Ooo0oO0 = O00O0oOO00O00 ( o0Ooo0O00 )
  if Ooo0oO0 != 'Failed' :
   iiIii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Ooo0oO0 )
   for iIIIiIi , O000OOO , oOOo0O00o , ooO0OO , IIo0o0O0O00oOOo , O0oOOo0Oo in iiIii :
    if Oo in iIIIiIi . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , oOOo0O00o , O0oOOo0Oo , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 71 - 71: i1IiiiI1iI % i1IiiiI1iI . i1i1I1IIii1II + Ii - Ii
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / i1IiiiI1iI - Ii . i1iIi / oooOo0oo0oo
     if 13 - 13: I11i % o0o00Oo0O - i1IiiiI1iI * ii / I1ii11iIi11i - ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOo000O00O ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo0O00o = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( o0OO ) . replace ( ' ' , '+' )
 if 90 - 90: ooOoO0O00 / i1i1I1IIii1II / oO0o % oooOo0oo0oo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( oOOo0O00o )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 20 - 20: Ii - OOooOOo + III1iiIii % IiI1i11I
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iIIIiIi in i1Iii1i1I :
   if o0OO in iIIIiIi . lower ( ) :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oOOo0O00o ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 79 - 79: oO0o / I11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
oo0i1iIi1IiI = '{ZH},' ; i11i11Iii = '{IX},' ; OO0o00Oo0oo0 = '{LM},'
if 22 - 22: i1iIi . I11i * o0ii1I - i1iIi / oOo0O0Ooo
def O0O00o0O ( url ) :
 I1iI1i11I = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( I1iI1i11I )
 for url , II11I , ooooOoo0OO , iIIIiIi in IIi :
  oOoo000 ( ( II11I ) . replace ( 'Sezon' , ' Season ' ) + ( ooooOoo0OO ) . replace ( 'Bölüm' , ' Episode ' ) + iIIIiIi , url , 8063 , '' )
  if 80 - 80: i1i1I1IIii1II
  if 54 - 54: OOooOOo % iI11I1II1I1I
  if 24 - 24: III1iiIii / o0ii1I * oooOo0oo0oo
  if 33 - 33: oooOo0oo0oo
def ii1Ii1 ( url ) :
 I1iI1i11I = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( I1iI1i11I )
 for url , iIIIiIi in IIi :
  OooOo00o ( iIIIiIi , url , 222 , '' )
  if 48 - 48: Iii . Ii % oOo0O0Ooo
  if 57 - 57: oooOo0oo0oo * oO0o + o0o00Oo0O % i1IiiiI1iI - oOo0O0Ooo
  if 43 - 43: i1IiiiI1iI
  if 10 - 10: ooOoO0O00 - I11i / ii + Ii + iI11I1II1I1I
def iiIooo0O0O0OO ( ) :
 if 65 - 65: I11i - ii / OOooOOo
 I1iI1i11I = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1iI1i11I )
 for oOOo0O00o , ooO0OO , iIIIiIi , ooooOoo0OO in IIi :
  oOoo000 ( iIIIiIi + '  -  ' + ( ooooOoo0OO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOOo0O00o , 8063 , ooO0OO )
  if 49 - 49: i1i1I1IIii1II
def o0o000OOO ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi , ooO0OO in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 8002 , ooO0OO )
def I1111iii1ii11 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , time , url , iIIIiIi , i1I in IIi :
  I1I1II1I11 ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , time ) , url , 1015 , ooO0OO , i1I )
  if 79 - 79: iI11I1II1I1I / iI11I1II1I1I . IiI1i11I . o0ii1I
def iII1I1iIIIiII ( ) :
 if 41 - 41: i1IiiiI1iI - o0o00Oo0O * I1ii11iIi11i % oOo0O0Ooo
 oOoo000 ( 'Coronation Street' , '' , 8001 , '' )
 oOoo000 ( 'Eastenders' , '' , 8002 , '' )
 oOoo000 ( 'Emmerdale' , '' , 8003 , '' )
 oOoo000 ( 'Hollyoaks' , '' , 8004 , '' )
 oOoo000 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 70 - 70: III1iiIii
 if 4 - 4: oooOo0oo0oo + Ii + Iii
 if 98 - 98: i1iIi - iI11I1II1I1I + oooOo0oo0oo - iI11I1II1I1I
 if 70 - 70: oooOo0oo0oo / Ii1I
def oooOoo ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Holly' in iIIIiIi :
   ooO0OO = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 99 - 99: i1IiiiI1iI - Ii1I - oOo0O0Ooo - i1IiiiI1iI + oO0o + IIiIiII11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 34 - 34: i1IiiiI1iI * Iii
def i1oO0o00oOo00oO ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'East' in iIIIiIi :
   ooO0OO = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 68 - 68: iI11I1II1I1I - oOo0O0Ooo . i1i1I1IIii1II + OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: I11i % I11i % IIiIiII11i * iI11I1II1I1I / III1iiIii . Ii1I
def IIiIiI1III1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Emmer' in iIIIiIi :
   ooO0OO = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 13 - 13: IIiIiII11i . oO0o
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: i1i1I1IIii1II . IiI1i11I - Iii . iI11I1II1I1I + Iii . OOooOOo
def OOoOO00O ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Coro' in iIIIiIi :
   ooO0OO = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 44 - 44: i1i1I1IIii1II * IIiIiII11i * IIiIiII11i + oOo0O0Ooo / I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: I1ii11iIi11i - III1iiIii
def ii1i1iIiIIi ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Celeb' in iIIIiIi :
   ooO0OO = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oOOo0O00o :
    OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 24 - 24: I11i - IiI1i11I % I1ii11iIi11i
def O0O0Oo00o0oO ( name , url ) :
 Iiooo000o0OoOo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if Iiooo000o0OoOo :
  O0oo0OoooO0 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I1i111I = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( I1i111I ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I1i111I = open_url ( url )
  IiiIIII1i1iII1 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( I1i111I ) [ - 1 ]
  O0oo0OoooO0 = IiiIIII1i1iII1 . replace ( '\\/' , '/' )
 iiIIIiIii = xbmcgui . ListItem ( name , '' , '' )
 iiIIIiIii . setPath ( O0oo0OoooO0 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiIIIiIii )
 if 32 - 32: IIiIiII11i . o0o00Oo0O + ii * Ii1I / IiI1i11I % ii
 if 3 - 3: o0ii1I * Ii
def o0000oOoo0o0o ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oOOo0O00o , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for oOOo0O00o , iIIIiIi in i1Iii1i1I :
  oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oOOo0O00o , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 82 - 82: IIiIiII11i * OOooOOo * iI11I1II1I1I % i1i1I1IIii1II * oooOo0oo0oo
def i1IOO ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Movies' in iIIIiIi :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( oOOo0O00o ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def Oo0OO0ooO0O0O ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ooO0OO )
 for url in i1Iii1i1I :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 76 - 76: I11i / Iii
  if 95 - 95: OOooOOo - o0o00Oo0O % ii
def IIiiI ( url ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url , ooO0OO in IIi :
  if '{{' in iIIIiIi :
   pass
  else :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , ooO0OO )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
iIo0O00o00o0 = '{UJ},' ; o00OOOOoOO = '{WE},' ; OooOoOoo0ooo0 = '{WP},' ; oO000oOo0oO0 = '{PP},'
def IIIiiii1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url , ooO0OO in IIi :
  if '{{' in iIIIiIi :
   pass
  else :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ooO0OO )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOO0o0OO ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  oo0Oooo0O ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo0Oooo0O ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: I1ii11iIi11i
 if 16 - 16: oOo0O0Ooo * IiI1i11I . iI11I1II1I1I
 if 66 - 66: ii * o0o00Oo0O / i1iIi * o0ii1I
def i11II ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '(cooltvseries.com)' in iIIIiIi :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , iIIIiIi in i1Iii1i1I :
  if '(cooltvseries.com)' in iIIIiIi :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def II1OoOOoOOOoooO0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I1i111I )
 for url in IIi :
  IiiI ( ( url ) . replace ( ' ' , '%20' ) )
i11i1i1i = '{XX},' ; OoO00O = '{UD},' ; O0oo0ooO = '{YT},' ; ii1i1 = '{JS},' ; IIII1I11Ii11 = '{PF},'
if 78 - 78: oO0o
def iI1Iiiii ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi , ooO0OO in IIi :
  OooOo00o ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oOOo0O00o ) ) , 222 , ooO0OO )
  if 62 - 62: iI11I1II1I1I % i1IiiiI1iI % Ii1I * III1iiIii
def o0ooOooO ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  if 'youtu' in url :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + ooO0OO )
 for url in next :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 87 - 87: III1iiIii
def II1i1i ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 17 - 17: I11i . III1iiIii . Ii + ii % Ii
def IIiI1iIiii ( url ) :
 I1i111I = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , ooO0OO )
  if 53 - 53: i1IiiiI1iI % Ii1I
  if 17 - 17: ii % o0ii1I % o0o00Oo0O
  if 46 - 46: IiI1i11I + i1IiiiI1iI % ii * Ii1I
  if 89 - 89: III1iiIii - III1iiIii % IiI1i11I / Iii + i1i1I1IIii1II - III1iiIii
  if 97 - 97: o0ii1I % OOooOOo / Ii1I / iI11I1II1I1I * ii * oooOo0oo0oo
def oOoOOo00oO ( ) :
 if 71 - 71: Ii * OOooOOo * oooOo0oo0oo + i1i1I1IIii1II + I1ii11iIi11i
 oOoo000 ( 'All Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Entertainment' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Movies' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Music' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'News' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Sports' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Documentary' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Kids' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Food' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Religious' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'USA Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 oOoo000 ( 'Other' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 if 59 - 59: III1iiIii
 if 54 - 54: oooOo0oo0oo
def IIIIIIi1I ( Cat_Name ) :
 if 86 - 86: IIiIiII11i - ii - i1iIi % IiI1i11I
 i1IIi1 = False
 ooOO0 = '0'
 if Cat_Name == 'All Channels' : i1IIi1 = True
 if Cat_Name == 'Entertainment' : ooOO0 = '1'
 if Cat_Name == 'Movies' : ooOO0 = '2'
 if Cat_Name == 'Music' : ooOO0 = '3'
 if Cat_Name == 'News' : ooOO0 = '4'
 if Cat_Name == 'Sports' : ooOO0 = '5'
 if Cat_Name == 'Documentary' : ooOO0 = '6'
 if Cat_Name == 'Kids' : ooOO0 = '7'
 if Cat_Name == 'Food' : ooOO0 = '8'
 if Cat_Name == 'Religious' : ooOO0 = '9'
 if Cat_Name == 'USA Channels' : ooOO0 = '10'
 if Cat_Name == 'Other' : ooOO0 = '11'
 if 17 - 17: oooOo0oo0oo - i1i1I1IIii1II
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I1i111I )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for iIIIiIi , ooO0OO , ii1ii in IIi :
  II1iII = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ooO0OO ) . replace ( '\\' , '' )
  if ii1ii == ooOO0 :
   oOoo000 ( iIIIiIi , '' , 7022 , II1iII )
  elif i1IIi1 == True :
   oOoo000 ( iIIIiIi , '' , 7022 , II1iII )
  else : pass
  if 49 - 49: Ii1I - oooOo0oo0oo / I1ii11iIi11i / i1i1I1IIii1II
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 58 - 58: I11i . IiI1i11I % IiI1i11I
def iI1II ( Search_Name ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , oOOo0O00o , I1 , IIiI in IIi :
  II1iII = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ooO0OO ) . replace ( '\\' , '' )
  OooOo00o ( Search_Name + ': Link 1' , ( oOOo0O00o ) . replace ( '\\' , '' ) , 222 , II1iII )
  OooOo00o ( Search_Name + ': Link 2' , ( I1 ) . replace ( '\\' , '' ) , 222 , II1iII )
  OooOo00o ( Search_Name + ': Link 3' , ( IIiI ) . replace ( '\\' , '' ) , 222 , II1iII )
  if 59 - 59: I1ii11iIi11i . I11i % oOo0O0Ooo / ii % i1i1I1IIii1II
def Oo00o ( ) :
 I1i111I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  OooOo00o ( iIIIiIi , ( oOOo0O00o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def iiIi1i ( ) :
 I1i111I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  OooOo00o ( iIIIiIi , ( oOOo0O00o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def o0o0OoOo ( ) :
 I1i111I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  OooOo00o ( iIIIiIi , ( oOOo0O00o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 49 - 49: ooOoO0O00 - OOooOOo - Iii * oOo0O0Ooo . i1iIi
def i11ii111II1II ( url ) :
 url
 ooo00Ooo = xbmcgui . ListItem ( iIIIiIi , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo00Ooo )
 return
 if 2 - 2: IIiIiII11i + o0ii1I - oO0o / IiI1i11I - oO0o * Ii1I
 if 51 - 51: Ii % OOooOOo . oO0o
def o0Oo0o0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( I1i111I )
 for url , O000OOO , ooO0OO , iIIIiIi in IIi :
  I1I1II1I11 ( iIIIiIi , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + ooO0OO , '' , ( O000OOO ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  oOoo000 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 14 - 14: OOooOOo . i1iIi - i1IiiiI1iI - IiI1i11I
def iioOOOoOo0oOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , O000OOO , ooO0OO in IIi :
  Ii1I1i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + ooO0OO , '' , O000OOO )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 O0ooOIii1iIIIi11I1 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OoOOOO0 in O0ooOIii1iIIIi11I1 :
  I1i11 = ( OoOOOO0 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1I1II1I11 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + ooO0OO , '' , I1i11 )
  if 33 - 33: oOo0O0Ooo - IiI1i11I . ooOoO0O00 / Ii
def O0oo0oOO00o0O0O ( INFO ) :
 o0OIiII ( 'info for workout' , INFO )
 if 64 - 64: o0ii1I . I11i - ooOoO0O00
 if 35 - 35: Ii1I % ii
 if 59 - 59: oOo0O0Ooo % Iii
def iiIiiIi1iiiIi ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( ( iIIIiIi ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def IIiII11i1 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , url , 9032 , iiIi1IIiIi + 'icon.png' )
def i1IiioOOooo ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  if '=' in iIIIiIi :
   pass
  else :
   OooOo00o ( ( iIIIiIi ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def IiI11IiIIi ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  if '=' in iIIIiIi :
   pass
  else :
   OooOo00o ( iIIIiIi , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 92 - 92: o0ii1I
   if 48 - 48: IiI1i11I . oOo0O0Ooo + o0o00Oo0O
   if 19 - 19: oOo0O0Ooo / i1IiiiI1iI - Iii
def IiIiIIi1 ( url ) :
 OOO00OO0oOo ( '[COLORblue][B]BAMFS MOVIES[/B][/COLOR]' , 'http://onlinemoviescinema.com/movies/' , 1000111 , '' , '' , '' , '' )
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<link>.+?</link>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , ooO0OO , url in IIi :
  if 'music' in url :
   OOO00OO0oOo ( iIIIiIi , url , 90036 , ooO0OO , ooO0OO , '' , '' )
  elif 'bl' in url :
   pass
  elif '247' in url :
   pass
  else :
   OOO00OO0oOo ( iIIIiIi , url , 90039 , ooO0OO , ooO0OO , '' , '' )
def IIi1Iii ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<item>\n<title>(.+?)</title>\n<utube>(.+?)</utube>\n<thumbnail>(.+?)</thumbnail>\n<fanart></fanart>\n</item>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url , ooO0OO in IIi :
  ii1oOoO0o0ooo ( iIIIiIi , url , 100009 , ooO0OO , ooO0OO , '' , '' )
  if 21 - 21: Ii1I - i1i1I1IIii1II * oO0o
def oO00oOOOO ( url ) :
 OOO00OO0oOo ( '[COLORblue][B]MOVIES BY GENRE[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]MOVIES BY YEAR[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png' , '' , '' , '' )
 I1i111I = requests . get ( url ) . text
 OOo0 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I1i111I )
 i1i1i1I = re . compile ( "Archives: Movies </h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 for url , ooO0OO , iIIIiIi in IIi :
  o0o0OOO0ooo00 = requests . get ( url ) . text
  I11III111i1I = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( o0o0OOO0ooo00 )
  for O0ooOO0O00 in I11III111i1I :
   OOO0O = requests . get ( O0ooOO0O00 ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OOO0O )
   for IIiiiI1iI , O00oo0o0000 , i1iII1IiiIiI1 , O0o0o , iiI111I1iIiI in IIi :
    if IIiiiI1iI == 'xyz' :
     iIi11 = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( iIIIiIi , iIi11 , 1001111 , ooO0OO , ooO0OO , '' , '' )
    else :
     iIi11 = 'http://' + O0o0o + '.' + i1iII1IiiIiI1 + '.' + O00oo0o0000 + '.' + IIiiiI1iI + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( iIIIiIi , iIi11 , 1001111 , ooO0OO , ooO0OO , '' , '' )
 for I1iiii1I in OOo0 :
  OOO00OO0oOo ( '[COLORblue][B]NEXT[/B][/COLOR]' , I1iiii1I , 1000111 , '' , '' , '' , '' )
  if 82 - 82: ooOoO0O00 % III1iiIii + I1ii11iIi11i - o0o00Oo0O - Iii
  if 64 - 64: o0ii1I - IiI1i11I
  if 12 - 12: ooOoO0O00
def oo0O0o0O ( ) :
 OOO00OO0oOo ( '[COLORblue][B] ACTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/action/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] ADVENTURE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/adventure/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] ANIMATION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/animation/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] COMEDY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/comedy/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] CRIME[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] DOCUMENTARY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/documentary/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] DRAMA[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/drama/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] FAMILY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre//family' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] FANTASY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/fantasy/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] FOREIGN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/foreign/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] HISTORY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/history/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] HORROR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/horror/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] MUSIC[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/music/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] MYSTERY[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/mystery/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] ROMANCE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/romance/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] SCIENCE FICTION[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/science-fiction/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] SPORTS[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/sports/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] THRILLER[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/thriller/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] TV MOVIE[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/tv-movie/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] WAR[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/war/' , 1003111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B] WESTERN[/B][/COLOR]' , 'http://onlinemoviescinema.com/genre/western/' , 1003111 , '' , '' , '' , '' )
 if 87 - 87: IiI1i11I - oO0o * I1ii11iIi11i - III1iiIii . Ii1I * ooOoO0O00
 if 79 - 79: IiI1i11I
def I1I111i1i1i ( url , name ) :
 OOO00OO0oOo ( name , '' , '' , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]BACK TO GENRES[/B][/COLOR]' , '' , 1002111 , 'http://2.bp.blogspot.com/_s8fgo2oOrGA/TJniXdGtoJI/AAAAAAAAAHM/EE43v4CdIU4/s1600/5803926-movie-poster-of-film-genres-vintage-background.jpg' , '' , '' , '' )
 I1i111I = requests . get ( url ) . text
 OOo0 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I1i111I )
 i1i1i1I = re . compile ( "<h3>Movie Genre.+?</h3>.+?<div class=\"item-img\">(.+?)<ul class=\"pagination\"><li>" , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 for url , ooO0OO , name in IIi :
  o0o0OOO0ooo00 = requests . get ( url ) . text
  I11III111i1I = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( o0o0OOO0ooo00 )
  for O0ooOO0O00 in I11III111i1I :
   OOO0O = requests . get ( O0ooOO0O00 ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OOO0O )
   for IIiiiI1iI , O00oo0o0000 , i1iII1IiiIiI1 , O0o0o , iiI111I1iIiI in IIi :
    if IIiiiI1iI == 'xyz' :
     iIi11 = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( name , iIi11 , 1001111 , ooO0OO , ooO0OO , '' , '' )
    else :
     iIi11 = 'http://' + O0o0o + '.' + i1iII1IiiIiI1 + '.' + O00oo0o0000 + '.' + IIiiiI1iI + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( name , iIi11 , 1001111 , ooO0OO , ooO0OO , '' , '' )
     if 25 - 25: i1iIi . III1iiIii - oOo0O0Ooo * i1i1I1IIii1II
 for I1iiii1I in OOo0 :
  OOO00OO0oOo ( '[COLORblue][B]NEXT[/B][/COLOR]' , I1iiii1I , 1003111 , '' , '' , '' , '' )
  if 32 - 32: Iii
  if 5 - 5: I11i
def O0oo0o0ooO00 ( ) :
 OOO00OO0oOo ( '[COLORblue][B]2017[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2017-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2016[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2016-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2015[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2015-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2014[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2014-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2013[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2013-movies/' , 1005 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2012[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2012-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2011[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2011-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2010[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2010-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2009[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2009-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2008[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2008-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2007[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2007-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2006[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2006-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2005[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2005-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2004[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2004-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2003[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2003-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2002[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2002-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2001[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2001-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]2000[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-2000-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1999[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1999-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1998[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1998-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1997[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1997-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1996[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1996-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1995[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1995-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1994[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1994-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1993[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1993-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1992[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1992-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1991[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1991-movies/' , 1005111 , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]1990[/B][/COLOR]' , 'http://onlinemoviescinema.com/watch-1990-movies/' , 1005111 , '' , '' , '' , '' )
 if 50 - 50: i1IiiiI1iI + oooOo0oo0oo . I11i
 if 60 - 60: ooOoO0O00 / Iii - I11i - i1iIi
 if 98 - 98: I1ii11iIi11i + OOooOOo * oooOo0oo0oo / IiI1i11I * OOooOOo / ii
def IiIoOo ( url , name ) :
 OOO00OO0oOo ( name , '' , '' , '' , '' , '' , '' )
 OOO00OO0oOo ( '[COLORblue][B]BACK TO YEARS[/B][/COLOR]' , '' , 1004111 , 'https://e.snmc.io/lk/l/s/5b799d8ed01a5bbcfa9dd2bb0290b642/5942704.png ' , '' , '' , '' )
 I1i111I = requests . get ( url ) . text
 OOo0 = re . compile ( '<li><a class="next page-numbers" href="(.+?)">Next .+?</a>' , re . DOTALL ) . findall ( I1i111I )
 i1i1i1I = re . compile ( '<h3>Movies of:.+?</h3>(.+?)<ul class="pagination"><li>' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<div class="col-sm-4 col-xs-6 item responsive-height">.+?<a href="(.+?)"><img width=.+?src="(.+?)" class=.+?alt="(.+?)"' , re . DOTALL ) . findall ( str ( i1i1i1I ) )
 for url , ooO0OO , name in IIi :
  o0o0OOO0ooo00 = requests . get ( url ) . text
  I11III111i1I = re . compile ( '<div class="player.+?">.+?<IFRAME SRC="(.+?)" FRAMEBORDER' , re . DOTALL ) . findall ( o0o0OOO0ooo00 )
  for O0ooOO0O00 in I11III111i1I :
   OOO0O = requests . get ( O0ooOO0O00 ) . text
   IIi = re . compile ( '\|vvad\|(.+?)\|(.+?)\|(.+?)\|(.+?)\|.+?var\|100\|(.+?)\|' , re . DOTALL ) . findall ( OOO0O )
   for IIiiiI1iI , O00oo0o0000 , i1iII1IiiIiI1 , O0o0o , iiI111I1iIiI in IIi :
    if IIiiiI1iI == 'xyz' :
     iIi11 = 'http://xyz.streamjunkie.tv/hls/' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( name , iIi11 , 1001111 , ooO0OO , ooO0OO , '' , '' )
    else :
     iIi11 = 'http://' + O0o0o + '.' + i1iII1IiiIiI1 + '.' + O00oo0o0000 + '.' + IIiiiI1iI + '/hls/,' + iiI111I1iIiI + ',.urlset/master.m3u8'
     ii1oOoO0o0ooo ( name , iIi11 , 1001111 , ooO0OO , ooO0OO , '' , '' )
     if 49 - 49: I11i * o0ii1I + I1ii11iIi11i
 for I1iiii1I in OOo0 :
  OOO00OO0oOo ( '[COLORblue][B]NEXT[/B][/COLOR]' , I1iiii1I , 1005111 , '' , '' , '' , '' )
def IIIiioo ( name , url ) :
 import urlresolver
 try :
  oOoO00Oo00o0O = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( oOoO00Oo00o0O , xbmcgui . ListItem ( name ) )
 except :
  xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( name ) )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 14 - 14: iI11I1II1I1I . oO0o + I11i * i1i1I1IIii1II . OOooOOo % I11i
 if 58 - 58: i1IiiiI1iI % Ii1I - OOooOOo . IIiIiII11i
 if 76 - 76: i1i1I1IIii1II * Ii % I11i / IIiIiII11i % OOooOOo - IIiIiII11i
def I11OoOO0o000000 ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Daily' in iIIIiIi :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 9008 , O0O )
def O0oooOOoOOO ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def OoO0 ( url ) :
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 OooOo00o ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  OooOo00o ( ( iIIIiIi ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 45 - 45: Iii . i1i1I1IIii1II - i1iIi . IiI1i11I / III1iiIii
def oooiIi11 ( ) :
 I1i111I = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if '.m3u' in oOOo0O00o :
   oOoo000 ( ( iIIIiIi ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oOOo0O00o ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def OOo0oo ( url ) :
 I1i111I = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  OooOo00o ( ( iIIIiIi ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 70 - 70: IIiIiII11i * ii - o0ii1I + i1i1I1IIii1II * o0o00Oo0O
def Ii1I11ii1i ( ) :
 I1i111I = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'category' in oOOo0O00o :
   oOoo000 ( iIIIiIi , 'http://www.disclose.tv/' + oOOo0O00o , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 49 - 49: i1i1I1IIii1II . o0ii1I . OOooOOo - Ii1I
   if 74 - 74: i1iIi % Ii1I * ooOoO0O00
def iiiii1I ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  oOoo000 ( iIIIiIi , 'http://www.disclose.tv/' + url , 7011 , ooO0OO )
 for url in next :
  oOoo000 ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 22 - 22: IiI1i11I . ii . I1ii11iIi11i
  if 44 - 44: OOooOOo / I1ii11iIi11i . ii % ii * Ii
def O0OooOoOOoooO00oO ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I1i111I )
 ii1I1IIii11 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  if 'http' in url :
   OooOo00o ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , iIIIiIi in i1Iii1i1I :
  OooOo00o ( iIIIiIi , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in ii1I1IIii11 :
  OooOo00o ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 62 - 62: o0ii1I
  if 4 - 4: iI11I1II1I1I . I1ii11iIi11i - Ii
def OOoo0o000 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 80 - 80: ii . i1iIi % Ii + ooOoO0O00 / i1iIi . IiI1i11I
def o0ooOoOoO0o ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OOo00OoOoo = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o0Oi1i1i11IIii = len ( OOo00OoOoo )
 if 11 - 11: i1iIi . i1IiiiI1iI - IiI1i11I . I11i
 if 41 - 41: i1i1I1IIii1II / oO0o - oO0o + i1iIi * oooOo0oo0oo
 if o0Oi1i1i11IIii == 1 :
  for i1IiIi1II11ii in OOo00OoOoo :
   i1IiIi1II11ii = i1IiIi1II11ii . replace ( 'player' , 'watch' )
   IIiI111iI1iiii = i1IiIi1II11ii + '&fv=&sou='
   O0ooo = OooOoooOo ( IIiI111iI1iiii )
   oo0oo = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( O0ooo )
   for iIIIII1iiiiII in oo0oo :
    I1ii1ii = False
    Resolve ( iIIIII1iiiiII )
    if 22 - 22: Ii
 elif o0Oi1i1i11IIii > 1 :
  if 52 - 52: Iii / oO0o
  for i1IiIi1II11ii in OOo00OoOoo :
   iIOoo0o00O0O0oO = OooOoooOo ( i1IiIi1II11ii )
   OO000OOO = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iIOoo0o00O0O0oO )
   o000OOooo000O = OO000OOO
   o000OOooo000O = ( str ( o000OOooo000O ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + o000OOooo000O
   OooOo00o ( 'DOUBLE LINK' , o000OOooo000O , 424 , '' )
   if 69 - 69: o0o00Oo0O . IiI1i11I
   for url in OO000OOO :
    oOoo000 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I1 = Google . resolve ( url )
    except :
     pass
    try :
     o0oOoO00oo0oOo = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I1 ) )
     for iiOO00O , iiO0OoO0OOO00 in o0oOoO00oo0oOo :
      if 15 - 15: I11i . o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . i1i1I1IIii1II * ii
      HD_URLS . append ( iiOO00O )
      SD_URLS . append ( iiO0OoO0OOO00 )
    except :
     pass
 else :
  pass
  if 32 - 32: i1iIi / IIiIiII11i . o0o00Oo0O . i1iIi % oOo0O0Ooo - I11i
def O00OoO0oo ( ) :
 if 47 - 47: oO0o . Ii
 if 9 - 9: OOooOOo - Iii . ii % i1iIi
 oOoo000 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 13 - 13: oO0o * iI11I1II1I1I + IIiIiII11i - I1ii11iIi11i - OOooOOo
 oOoo000 ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 43 - 43: IiI1i11I / i1IiiiI1iI * oOo0O0Ooo % i1iIi % oOo0O0Ooo
 if 18 - 18: oO0o
def O0oOo ( ) :
 I1i111I = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , 'http://cnfstudio.com/genre/' + oOOo0O00o , 7003 , iiIi1IIiIi + 'icon.png' )
  if 1 - 1: i1i1I1IIii1II % Iii / OOooOOo
iIii1 = xbmcgui . Dialog ( )
if 15 - 15: oO0o - OOooOOo
i11iI1I1I11II = '{UN},' ; oo0O00O0oO = '{IG},' ; IIIIi1iII = '{PL},' ; ii1oO0Oo = '{LO},' ; iIi1IIIi1Ii = '{LP},' ; Ii1IiIIIi1i = '{HA},' ; II111Ii1I1I = '{XD},' ; o00oo0oOo0o0 = '{TA},' ; i1Ii1 = '{DP},' ; i1I1ii1iI1 = '{JT},' ; OoI1Ii = '{JJ},' ; IIIII1iII1 = '{MM},' ; OO0oOoO0O0 = '{FQ},' ; iiiI1i = '{HH},'
if 93 - 93: IiI1i11I % Ii - OOooOOo . o0ii1I
def ooo0oO0o000O0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I1i111I )
 iiIi11i1I1 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , ooO0OO )
 iiIi11i1I1 = iiIi11i1I1
 for url in iiIi11i1I1 :
  oOoo000 ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 72 - 72: III1iiIii + Ii - oooOo0oo0oo
def oo00o0Oo0O0 ( url ) :
 if 56 - 56: oooOo0oo0oo / IiI1i11I . I1ii11iIi11i % oooOo0oo0oo + IiI1i11I / i1IiiiI1iI
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  Iii1111Ii1iI = O00o000O0 ( iiI111I1iIiI )
  oOoo00O00ooo = O00o000O0 ( url )
  if 37 - 37: OOooOOo
  if 37 - 37: I1ii11iIi11i - Iii / oooOo0oo0oo / III1iiIii * ooOoO0O00
def O00o000O0 ( url ) :
 if 55 - 55: oOo0O0Ooo
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  OoOoooO000OO ( url )
  if 83 - 83: OOooOOo / i1iIi / IiI1i11I + oO0o - oOo0O0Ooo * ooOoO0O00
  if 34 - 34: iI11I1II1I1I * o0o00Oo0O - OOooOOo + iI11I1II1I1I % Ii1I
def oOo ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 86 - 86: IiI1i11I % ooOoO0O00 + ii + o0ii1I
def I1IIiIIii1II1 ( ) :
 if os . path . exists ( II ) :
  o0O0oOooooO00 = open ( II , 'r' )
  for ooo00Ooo in o0O0oOooooO00 :
   oooOo0O = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( ooo00Ooo )
   for iIIIiIi , oOOo0O00o in oooOo0O :
    OooOo00o ( iIIIiIi , oOOo0O00o , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 53 - 53: ii * oOo0O0Ooo - oO0o . Ii / I1ii11iIi11i - ooOoO0O00
def iiI11IIiIiI1 ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = oOOo000oOoO0 ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIIIiIi , url in IIi :
   url = ( url ) . strip ( )
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 84 - 84: oooOo0oo0oo + IIiIiII11i . I11i * I1ii11iIi11i
  if 68 - 68: o0ii1I % o0ii1I
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in IIi :
  oOOo0O00o = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oOOo0O00o
 iIIIiIi = 'plugin.video.GenieTv'
 if 26 - 26: I11i . o0ii1I * OOooOOo
 Oo0OoooOoO0O0 ( oOOo0O00o , iIIIiIi )
 if 50 - 50: oO0o / Iii . Ii
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in IIi :
  oOOo0O00o = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oOOo0O00o
 iIIIiIi = 'repository.GenieTv'
 if 84 - 84: ii . oO0o / OOooOOo * ooOoO0O00
 Oo0OoooOoO0O0 ( oOOo0O00o , iIIIiIi )
 if 6 - 6: iI11I1II1I1I * iI11I1II1I1I
 if 77 - 77: oooOo0oo0oo % i1i1I1IIii1II + iI11I1II1I1I * o0ii1I . III1iiIii . I1ii11iIi11i
def OoO ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  IIiiiI ( )
 if O0O00Oo == 1 :
  ooooO0OOo0o0 ( )
  if 27 - 27: I11i . OOooOOo * o0ii1I * IiI1i11I * o0o00Oo0O
  if 93 - 93: III1iiIii % i1IiiiI1iI % IIiIiII11i
  if 20 - 20: ii * i1IiiiI1iI
  if 38 - 38: IiI1i11I . ii
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
i1iiI11ii1II1 = 'https://addons.tvaddons.ag/'
if 33 - 33: i1i1I1IIii1II / Iii . OOooOOo * o0o00Oo0O - III1iiIii
def ooooO0OOo0o0 ( ) :
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 IIiiiII11i = 'https://addons.tvaddons.ag/search/?keyword=' + Oo
 II11iIiIIIiI = OooOoooOo ( IIiiiII11i )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , o000O000 , iIIIiIi in IIi :
  I1I1II1I11 ( iIIIiIi , oOOo0O00o , 10054 , 'https://addons.tvaddons.ag/' + o000O000 , Oo00OOOOO , '' )
  if 12 - 12: Ii + Ii1I * oO0o
  if 13 - 13: I1ii11iIi11i + ii / III1iiIii
def IIiiiI ( ) :
 II11iIiIIIiI = OooOoooOo ( i1iiI11ii1II1 )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  if 'Repositories' in iIIIiIi :
   pass
  elif 'Services' in iIIIiIi :
   pass
  elif 'International' in iIIIiIi :
   pass
  else :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 10053 , 'https://addons.tvaddons.ag/' + ooO0OO , Oo00OOOOO , '' )
   if 56 - 56: Ii1I * IIiIiII11i
   if 75 - 75: Iii . I11i - Ii / Iii
def Addon ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OOo0 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  if 'Please' in iIIIiIi :
   pass
  else :
   Ii1I1i ( iIIIiIi , url , 10054 , 'https://addons.tvaddons.ag/' + ooO0OO , Oo00OOOOO , '' )
 for url in OOo0 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
  if 100 - 100: Ii * Ii . iI11I1II1I1I % IiI1i11I * Ii1I
  if 17 - 17: o0ii1I * III1iiIii * Ii / Ii1I / Ii
def IiiiiI ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   I11ii1IIiIi = os . path . join ( o00oo0 , name + '.zip' )
   try :
    os . remove ( I11ii1IIiIi )
   except :
    pass
   downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
   OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OoOOo0OOoO
   print '======================================='
   extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
   OOOOo0o00OO0000 ( )
   if 5 - 5: IiI1i11I * i1iIi + III1iiIii . oOo0O0Ooo / oOo0O0Ooo
def Oo0OoooOoO0O0 ( url , name ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 I11ii1IIiIi = os . path . join ( o00oo0 , name + '.zip' )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 OoOOo0OOoO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoOOo0OOoO
 print '======================================='
 extract . all ( I11ii1IIiIi , OoOOo0OOoO , o0oOoO00o )
 OOOOo0o00OO0000 ( )
 if 72 - 72: oO0o / Ii1I - oooOo0oo0oo - ii / ii % ii
def OOOOo0o00OO0000 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 85 - 85: oO0o . I11i . oOo0O0Ooo
 if 75 - 75: iI11I1II1I1I - o0ii1I % o0o00Oo0O % III1iiIii
def II1II1iiIiI ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , o000O000 , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , url , 1007 , o000O000 )
def i1IOO0O0ooOo ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , o000O000 , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 1006 , o000O000 )
  if 23 - 23: oO0o / III1iiIii * IIiIiII11i
def I1ii111I ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
  IIIi1ii1i1 ( iIIIiIi , 100109 , oOOo0O00o , image = iiiI1I1iIIIi1 , isFolder = True )
  if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
def iII1IiI1I11i ( url ) :
 import random
 Ii1i11I11i = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 Ii1i11I11i . clear ( )
 oO0oooo = [ ]
 OOOoO0 = [ ]
 oO0OO00O0 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1 , iiiI1I1iIIIi1 , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
  oO0oooo . append ( [ I1 , iIIIiIi ] )
  if len ( oO0oooo ) == len ( IIi ) :
   for ooo00Ooo in oO0oooo :
    O0OO0 = random . randint ( 1 , len ( oO0oooo ) )
    try :
     OO0oO0o0oOO = oO0oooo [ int ( O0OO0 ) ]
    except :
     pass
    if len ( OOOoO0 ) <= 20 :
     if OO0oO0o0oOO [ 1 ] not in oO0OO00O0 :
      o0o = OooOoooOo ( OO0oO0o0oOO [ 0 ] )
      ii1I1IIii11 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for Iii1OO , iI1III11IIi11Ii11 in ii1I1IIii11 :
       OOoOoo = OooOoooOo ( Iii1OO )
       II1i11I = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for iII1I , iiI111I1iIiI in II1i11I :
        if 'panda' in iiI111I1iIiI :
         O0iI = OooOoooOo ( iiI111I1iIiI )
         II1i11I1 = re . compile ( "url: '(.+?)'" ) . findall ( O0iI )
         for oOoOo0O00Oo in II1i11I1 :
          if 'http' in oOoOo0O00Oo :
           iiIIIiIii = xbmcgui . ListItem ( OO0oO0o0oOO [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : OO0oO0o0oOO [ 1 ] } )
           iiIIIiIii . setProperty ( "IsPlayable" , "true" )
           Ii1i11I11i . add ( oOoOo0O00Oo , iiIIIiIii )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiIIIiIii )
           if 7 - 7: Ii - o0o00Oo0O / o0o00Oo0O % I1ii11iIi11i / i1i1I1IIii1II / iI11I1II1I1I
def IIIi1ii1i1 ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 I111IIiii1Ii = sys . argv [ 0 ]
 I111IIiii1Ii += '?mode=' + str ( mode )
 I111IIiii1Ii += '&title=' + urllib . quote_plus ( name )
 I111IIiii1Ii += '&image=' + urllib . quote_plus ( image )
 I111IIiii1Ii += '&page=' + str ( page )
 if url != '' :
  I111IIiii1Ii += '&url=' + urllib . quote_plus ( url )
 if keyword :
  I111IIiii1Ii += '&keyword=' + urllib . quote_plus ( keyword )
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  iiIIIiIii . addContextMenuItems ( contextMenu )
 if infoLabels :
  iiIIIiIii . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  iiIIIiIii . setProperty ( "IsPlayable" , "true" )
 iiIIIiIii . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = isFolder )
 if 30 - 30: Ii1I . Ii + Ii
 if 97 - 97: OOooOOo . I1ii11iIi11i . i1IiiiI1iI + IiI1i11I % i1iIi . III1iiIii
def I1IIIiI1I1ii1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , iconimage , O000OOO , IIo0o0O0O00oOOo , name in IIi :
  if 'http' in url :
   if '.php' in url :
    ii1o0oooO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for ooo00Ooo in ii1o0oooO :
     if ooo00Ooo == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    oo00OOo0 ( name , url , 1016 , iconimage , IIo0o0O0O00oOOo , O000OOO )
   else :
    if 'youtube' in url :
     ii1o0oooO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for ooo00Ooo in ii1o0oooO :
      if ooo00Ooo == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     oOoO0oOo0Oo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , IIo0o0O0O00oOOo , O000OOO )
    else :
     ii1o0oooO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for ooo00Ooo in ii1o0oooO :
      if ooo00Ooo == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     oOoO0oOo0Oo ( name , url , 222 , iconimage , IIo0o0O0O00oOOo , O000OOO )
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
  else :
   i1iIiiii ( url , iconimage , name )
   if 83 - 83: oooOo0oo0oo * III1iiIii / oO0o / Ii
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
  for url , o000O000 , name in IIi :
   if 'http' in url :
    if '.php' in url :
     oOoo000 ( name , url , 1016 , o000O000 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OooOo00o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , o000O000 )
     else :
      ii1o0oooO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for ooo00Ooo in ii1o0oooO :
       if ooo00Ooo == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OooOo00o ( name , url , 222 , o000O000 )
      I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
   else :
    i1iIiiii ( url , o000O000 , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 94 - 94: o0o00Oo0O / iI11I1II1I1I + o0o00Oo0O / oOo0O0Ooo
def i1iIiiii ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oooO0OOO0o0o = ( url ) . replace ( i11i11Iii , 'http' ) . replace ( OoO00O , '.com' ) ;
 iiiIiiIII = ( oooO0OOO0o0o ) . replace ( OO0o00Oo0oo0 , 'a' ) . replace ( IIi1II , 'b' ) . replace ( OOOoooO0o0o , 'c' ) . replace ( o00OOOOoOO , 'd' ) . replace ( IIIIi1iII , 'e' ) . replace ( i1I1ii1iI1 , 'f' ) ;
 OOooo0o = ( iiiIiiIII ) . replace ( i11i1i1i , 'g' ) . replace ( Ii1IiIIIi1i , 'h' ) . replace ( O0oo0ooO , 'i' ) . replace ( IIII1I11Ii11 , 'j' ) . replace ( OOoOoOO00 , 'k' ) . replace ( o0O00 , 'l' ) ;
 iiIiI11IIiI = ( OOooo0o ) . replace ( o0Oo0oOo0oO0 , 'm' ) . replace ( IiIII1I1iIiiI , 'n' ) . replace ( IiIiIi1I , 'o' ) . replace ( o0OoOOO , 'p' ) . replace ( o00oOO0Oo , 'q' ) . replace ( OoO0oOOOooO0o , 'r' ) ;
 oO0O0Ooo = ( iiIiI11IIiI ) . replace ( I1iIIiI , 's' ) . replace ( OooOoOoo0ooo0 , 't' ) . replace ( OOO0o , 'u' ) . replace ( i1I1I1IIIi11 , 'v' ) . replace ( ooOo000 , 'w' ) . replace ( OO0o0oo , 'x' ) ;
 o00I11II1iI = ( oO0O0Ooo ) . replace ( i1Ooo0O0OO0OOo , 'y' ) . replace ( i111ii11I1 , 'z' ) . replace ( i11iI1I1I11II , '.' ) . replace ( oo0O00O0oO , '(' ) . replace ( ii1oO0Oo , ')' ) . replace ( iIi1IIIi1Ii , '/' ) ;
 iii1I1 = ( o00I11II1iI ) . replace ( oo0i1iIi1IiI , '1' ) . replace ( oO000oOo0oO0 , '2' ) . replace ( O00 , '3' ) . replace ( o00oo0oOo0o0 , '4' ) . replace ( i1Ii1 , '5' ) . replace ( ii1i1 , '6' ) ;
 Iii1IIiIi = ( iii1I1 ) . replace ( OoI1Ii , '7' ) . replace ( IIIII1iII1 , '8' ) . replace ( OO0oOoO0O0 , '9' ) . replace ( iiiI1i , '0' ) . replace ( OO00O0O , ':' ) . replace ( o0oo0oo0 , '%' ) ;
 url = ( Iii1IIiIi ) . replace ( iIo0O00o00o0 , '-' ) . replace ( II111Ii1I1I , '_' ) ;
 OooOo00o ( name , url , 222 , iconimage ) ;
 if 62 - 62: Ii + i1i1I1IIii1II / i1iIi . i1IiiiI1iI / Iii
 if 28 - 28: oooOo0oo0oo % oooOo0oo0oo % o0o00Oo0O % iI11I1II1I1I % OOooOOo
def o0ooo0O00 ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for oOOo0O00o , o000O000 , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 1007 , o000O000 )
def oo00O0Ooo ( url ) :
 if 94 - 94: o0o00Oo0O . ii - Ii - ooOoO0O00 * I11i
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , o000O000 , iIIIiIi in IIi :
  oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 1006 , o000O000 )
  if 54 - 54: i1iIi * ii . ii . i1IiiiI1iI
def O00o0OooOOO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 ii1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 ii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1 )
 if 57 - 57: IIiIiII11i + I11i . Ii1I + iI11I1II1I1I
 if 60 - 60: ii * I1ii11iIi11i + Ii . Ii . OOooOOo - i1i1I1IIii1II
def OOOOoO0 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  if '-dir-' in iIIIiIi :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , ooO0OO )
  else :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 1006 , ooO0OO )
   if 81 - 81: oooOo0oo0oo + IIiIiII11i * IiI1i11I / oooOo0oo0oo + oOo0O0Ooo - I11i
def oooOoOOOoo0 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 oo0O = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '[To Parent Directory]' in iIIIiIi :
   iIIIiIi = 'HOME'
   pass
  elif 'HOME' in iIIIiIi :
   pass
  elif '.m3u' in iIIIiIi :
   oOoo000 ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , oo0O + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in iIIIiIi :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , oo0O + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in iIIIiIi :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , oo0O + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) , oo0O + url , 1012 , iiIi1IIiIi + 'music.png' )
def IiI1i1iIi1 ( url ) :
 II11iIiIIIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 69 - 69: I1ii11iIi11i
def ooOOO000 ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 oo0O = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '.mp3' in iIIIiIi :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '/' , '' ) , oo0O + url , 1011 , iiIi1IIiIi + 'music.png' )
def O0OoO ( ) :
 I1i111I = oOOo000oOoO0 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , ( 'http://www.cyn.net/music/' + oOOo0O00o ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + ooO0OO ) . replace ( ' ' , '%20' ) )
def oOo0O00 ( url , img ) :
 I1i111I = oOOo000oOoO0 ( url )
 I1 = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( I1 + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 24 - 24: oO0o
def O0OoOo ( url ) :
 I1i111I = oOOo000oOoO0 ( url )
 I1 = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for type , url , iIIIiIi in IIi :
  if '[VID]' in type :
   OooOo00o ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , I1 + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   O0OoOo ( I1 + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: oO0o * iI11I1II1I1I - Ii1I - i1IiiiI1iI + III1iiIii
 if 91 - 91: o0o00Oo0O
def IiiIiIIi1 ( ) :
 i1oOOOOOOOoO = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 o0OO = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo = o0OO . lower ( )
 oOOo0O00o = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 II1IIIii = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I1 = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 26 - 26: ii + i1i1I1IIii1II + oO0o . o0o00Oo0O
 II11iIiIIIiI = O00O0oOO00O00 ( oOOo0O00o )
 oo0o = O00O0oOO00O00 ( II1IIIii )
 o0o = O00O0oOO00O00 ( I1 )
 if 46 - 46: ii - I1ii11iIi11i * i1IiiiI1iI * oooOo0oo0oo * i1IiiiI1iI . i1i1I1IIii1II
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iiiI1I1iIIIi1 , O000OOO , i11i1iIiii , iIIIiIi in IIi :
   if o0OO in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oOOo0O00o , 1016 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O000OOO )
    if 96 - 96: o0ii1I / III1iiIii % I11i + Iii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  oOo0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oo0o )
  for oOOo0O00o , iIIIiIi in oOo0 :
   if o0OO in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oOOo0O00o ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 46 - 46: oO0o * oOo0O0Ooo
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for oOOo0O00o , iIIIiIi in i1Iii1i1I :
   if o0OO in iIIIiIi . lower ( ) :
    oOoo000 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oOOo0O00o ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 25 - 25: i1IiiiI1iI . III1iiIii % o0o00Oo0O % ooOoO0O00
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 53 - 53: o0o00Oo0O % i1iIi
    if 41 - 41: III1iiIii
    if 29 - 29: i1iIi
    if 70 - 70: i1i1I1IIii1II . o0o00Oo0O % Iii % III1iiIii - Iii * Ii1I
    if 22 - 22: ooOoO0O00
    if 82 - 82: i1i1I1IIii1II . iI11I1II1I1I - Ii1I
o0Oo0oOo0oO0 = '{SF},' ; IiIII1I1iIiiI = '{IF},' ; IiIiIi1I = '{PW},' ; O00 = '{AM},' ; o0OoOOO = '{GF},' ; o00oOO0Oo = '{DD},' ; OoO0oOOOooO0o = '{UO},' ; I1iIIiI = '{LE},' ; OOO0o = '{ZY},' ; i1I1I1IIIi11 = '{UE},' ; ooOo000 = '{PE},' ; OO0o0oo = '{JE},' ; i1Ooo0O0OO0OOo = '{TH},' ; i111ii11I1 = '{LK},'
if 55 - 55: I1ii11iIi11i % o0ii1I . iI11I1II1I1I * i1IiiiI1iI
if 33 - 33: o0o00Oo0O - oOo0O0Ooo / Ii1I / oO0o + IiI1i11I - i1i1I1IIii1II
def iII1111III1I ( ) :
 I1i111I = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 8021 , iiIi1IIiIi + 'iwatch.png' )
  I1iI1ii1II ( 'movies' , 'MAIN' )
def I1I111 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I1i111I )
 for url , iIIIiIi , i11I1iIii1i11 in IIi :
  oOoo000 ( iIIIiIi + i11I1iIii1i11 , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def oOO0oOo0OOoOO ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1i111I )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  o0O00oo0Ooo ( url )
def o0O00oo0Ooo ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1i111I )
 ii1I1IIii11 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I1i111I )
 II1i11I = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  OooOo00o ( 'VidSpot - ' + iIIIiIi , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  OooOo00o ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , iIIIiIi in II1i11I :
  OooOo00o ( 'VidUp' + iIIIiIi , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for iIIIiIi , url in ii1I1IIii11 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OooOo00o ( 'TheVideo - ' + iIIIiIi , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 23 - 23: ii
def ooOOOo ( ) :
 I1i111I = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 1021 , iiIi1IIiIi + 'anime.png' )
  if 100 - 100: o0o00Oo0O / oooOo0oo0oo - i1iIi
  if 15 - 15: IiI1i11I - o0o00Oo0O - ii
def iiiiIIiiII1Iii1 ( ) :
 I1i111I = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , oOOo0O00o , 1002 , iiIi1IIiIi + 'anime.png' )
  if 93 - 93: OOooOOo % o0ii1I / o0ii1I - i1iIi - III1iiIii % i1iIi
  if 9 - 9: ii * oOo0O0Ooo - I1ii11iIi11i / Ii * IiI1i11I
  if 56 - 56: oOo0O0Ooo . Iii % IiI1i11I
def I1I1i ( url ) :
 I1i111I = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i111I )
 for ooO0OO in i1Iii1i1I :
  iiiIIII1IIi = ooO0OO
 ii1I1IIii11 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1i111I )
 for url in ii1I1IIii11 :
  oOoo000 ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOoo000 ( iIIIiIi , url , 1003 , iiiIIII1IIi )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOii ( url , IMAGE ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  print iIIIiIi + '     ' + url
  if 'easy' in url :
   o0ooo ( url )
  elif 'playpanda' in url :
   o0ooo ( url )
   if 77 - 77: I11i % IiI1i11I / ooOoO0O00 . I1ii11iIi11i
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0ooo ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I1i111I )
 for url in IIi :
  OooOo00o ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 77 - 77: Ii % i1IiiiI1iI - I1ii11iIi11i - i1i1I1IIii1II * oooOo0oo0oo
  if 3 - 3: ii - i1i1I1IIii1II / oOo0O0Ooo
def o0ooo0ooo0 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 30 - 30: I11i - o0ii1I . Ii + i1i1I1IIii1II % i1iIi + Ii1I
def oOOo000oOoO0 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 5 - 5: oooOo0oo0oo . IiI1i11I . i1i1I1IIii1II % III1iiIii * o0o00Oo0O
def IIiiiiIii ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I1Iii11111I1iii = ( '%s%s' % ( OO0Oo00 , url ) )
 iiI111I1iIiI = oOOo000oOoO0 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , o000O000 , iIIIiIi in IIi :
  OooOo00o ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , o000O000 )
  if 60 - 60: OOooOOo / i1iIi % iI11I1II1I1I
def IiIi1i1 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  o0000o0o ( url , iIIIiIi )
 else :
  I11iiiiI1i ( url )
def I11iiiiI1i ( url ) :
 import urlresolver
 try :
  oOoO00Oo00o0O = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( oOoO00Oo00o0O , xbmcgui . ListItem ( iIIIiIi ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( iIIIiIi ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def OoOoooO000OO ( url ) :
 if 75 - 75: Iii - oO0o - IiI1i11I % iI11I1II1I1I * oO0o
 ooOo = open ( OOOO0OOoO0O0 , "a" )
 ooOo . write ( 'url="' + url + '"\n' )
 ooOo . close
 if 25 - 25: i1IiiiI1iI - i1iIi + I1ii11iIi11i . oOo0O0Ooo % iI11I1II1I1I
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 try : iIIIi1i1I11i . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iIIIiIi ) )
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iIIIi1i1I11i . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def o0000o0o ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  I1iII1II1I1ii = '.mp4'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   IiIIi1I ( url , name , I1iII1II1I1ii )
 elif '.mkv' in url :
  I1iII1II1I1ii = '.mkv'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   IiIIi1I ( url , name , I1iII1II1I1ii )
 elif '.mp3' in url :
  I1iII1II1I1ii = '.mp3'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   IiIIi1I ( url , name , I1iII1II1I1ii )
 elif '.avi' in url :
  I1iII1II1I1ii = '.avi'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   IiIIi1I ( url , name , I1iII1II1I1ii )
 elif '.mov' in url :
  I1iII1II1I1ii = '.mov'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   IiIIi1I ( url , name , I1iII1II1I1ii )
 elif '.mpeg' in url :
  I1iII1II1I1ii = '.mpeg'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   IiIIi1I ( url , name , I1iII1II1I1ii )
 elif '.mpg' in url :
  I1iII1II1I1ii = '.mpg'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   IiIIi1I ( url , name , I1iII1II1I1ii )
 elif '.flv' in url :
  I1iII1II1I1ii = '.flv'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   IiIIi1I ( url , name , I1iII1II1I1ii )
 elif '.wmv' in url :
  I1iII1II1I1ii = '.wmv'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   IiIIi1I ( url , name , I1iII1II1I1ii )
 else :
  I11iiiiI1i ( url )
def IiIIi1I ( url , name , cat ) :
 iii11iI ( )
 o00oo0 = xbmc . translatePath ( os . path . join ( OooO0 ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 I11ii1IIiIi = os . path . join ( o00oo0 , file )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def iii11iI ( ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def ii1II1i1 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iIIIiIi )
 xbmc . sleep ( 1 )
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 o0oOoO00o . update ( 100 , '%s' % iIIIiIi )
 xbmc . sleep ( 1 )
 iIIIi1i1I11i . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 64 - 64: iI11I1II1I1I
def IiiI ( url ) :
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iIIIi1i1I11i . play ( url ) . strip ( )
 except : pass
 if 61 - 61: o0ii1I % I1ii11iIi11i + OOooOOo
def oOoiIi1I1Iii1 ( url ) :
 iIIIi1i1I11i = xbmc . Player ( oOO0OO0OO ( ) )
 import urlresolver
 Oo0ooOoo = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 iIIIi1i1I11i . play ( Oo0ooOoo )
 xbmc . sleep ( 1 )
 iIIIi1i1I11i . play ( url )
 if 57 - 57: oOo0O0Ooo - ooOoO0O00 + IiI1i11I * I1ii11iIi11i % oO0o
 if 87 - 87: iI11I1II1I1I % OOooOOo + oO0o / Ii
def oOO0OO0OO ( ) :
 try :
  o0oOOo0oO0o = getSet ( "core-player" )
  if ( o0oOOo0oO0o == 'DVDPLAYER' ) : IIiiI1 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0oOOo0oO0o == 'MPLAYER' ) : IIiiI1 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0oOOo0oO0o == 'PAPLAYER' ) : IIiiI1 = xbmc . PLAYER_CORE_PAPLAYER
  else : IIiiI1 = xbmc . PLAYER_CORE_AUTO
 except : IIiiI1 = xbmc . PLAYER_CORE_AUTO
 return IIiiI1
 return True
 if 64 - 64: OOooOOo
def oOoo000 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
 if 10 - 10: oO0o + iI11I1II1I1I . IIiIiII11i
def i1ioO ( name , url , mode , iconimage , fanart , description ) :
 if 8 - 8: oO0o / IIiIiII11i
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
 if 71 - 71: I1ii11iIi11i % IiI1i11I . i1iIi % o0o00Oo0O + iI11I1II1I1I % i1IiiiI1iI
def OooOo00o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1i11II = [ ]
  I1i11II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
 if 8 - 8: Ii1I - i1iIi + IiI1i11I * oO0o
 if 22 - 22: Ii1I * ii
 if 33 - 33: oooOo0oo0oo / I11i + oooOo0oo0oo . Ii
 if 19 - 19: OOooOOo % OOooOOo
 if 74 - 74: Ii / Ii1I - i1i1I1IIii1II . oO0o
 if 25 - 25: oooOo0oo0oo % i1i1I1IIii1II
def II1i1i1111IIIii ( url , heading , announce ) :
 class ii11IiiiIi1iI ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   self . image = xbmcgui . ControlImage ( 800 , 600 , 1200 , 450 , url , aspectRatio = 2 )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . addControl ( self . image )
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : O0oO0 = open ( announce ) ; I111iiIIiI1I = O0oO0 . read ( )
   except : I111iiIIiI1I = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I111iiIIiI1I ) )
   return
 ii11IiiiIi1iI ( )
 ii11IiiiIi1iI ( )
def o0OIiII ( heading , announce ) :
 class ii11IiiiIi1iI ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : O0oO0 = open ( announce ) ; I111iiIIiI1I = O0oO0 . read ( )
   except : I111iiIIiI1I = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I111iiIIiI1I ) )
   return
 ii11IiiiIi1iI ( )
 ii11IiiiIi1iI ( )
def iIiIi11 ( ) :
 II1i1i1111IIIii ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 23 - 23: IIiIiII11i - IIiIiII11i / i1i1I1IIii1II - III1iiIii - Ii
 if 68 - 68: o0o00Oo0O / IiI1i11I
 if 70 - 70: I1ii11iIi11i
 if 92 - 92: oooOo0oo0oo + ooOoO0O00 - i1iIi
 if 13 - 13: IiI1i11I
def OOOOo0o00OO0000 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 79 - 79: ii / oO0o % o0ii1I - OOooOOo * ooOoO0O00 + i1IiiiI1iI
 if 42 - 42: Ii % i1IiiiI1iI + Ii % Ii % Ii1I
 if 6 - 6: i1i1I1IIii1II . I11i / oOo0O0Ooo
 if 64 - 64: IiI1i11I
 if 65 - 65: o0o00Oo0O / IIiIiII11i * III1iiIii % o0ii1I + I11i
 if 43 - 43: i1IiiiI1iI + oO0o * ii
 if 85 - 85: IiI1i11I + oooOo0oo0oo
 if 36 - 36: oO0o % IIiIiII11i * o0o00Oo0O + IIiIiII11i - i1i1I1IIii1II - ooOoO0O00
 if 53 - 53: o0ii1I - oooOo0oo0oo
 if 75 - 75: IiI1i11I % o0o00Oo0O - Iii - Ii1I + oOo0O0Ooo - oOo0O0Ooo
 if 87 - 87: ooOoO0O00 % o0ii1I % ooOoO0O00 + iI11I1II1I1I
 if 23 - 23: iI11I1II1I1I * Iii . i1IiiiI1iI - I11i
 if 66 - 66: oOo0O0Ooo * i1IiiiI1iI / Ii / oooOo0oo0oo
 if 19 - 19: i1iIi % iI11I1II1I1I * ii
 if 60 - 60: i1IiiiI1iI * IiI1i11I / ii * I1ii11iIi11i
 if 47 - 47: IiI1i11I + I11i % iI11I1II1I1I * OOooOOo
 if 65 - 65: oooOo0oo0oo . IIiIiII11i * Ii + oooOo0oo0oo
 if 99 - 99: Ii1I % I1ii11iIi11i
 if 31 - 31: I11i - IIiIiII11i * oooOo0oo0oo . oooOo0oo0oo - i1i1I1IIii1II
 if 57 - 57: oooOo0oo0oo / Ii / i1IiiiI1iI - I1ii11iIi11i . iI11I1II1I1I
 if 84 - 84: III1iiIii
 if 42 - 42: o0o00Oo0O . i1IiiiI1iI / Iii
 if 69 - 69: OOooOOo / i1IiiiI1iI * oOo0O0Ooo
 if 76 - 76: o0o00Oo0O + IIiIiII11i * oO0o
def iI1IIi1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + ii11iOoo0oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 100 - 100: o0ii1I
def O0O0OoO0o0OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 61 - 61: ooOoO0O00 % Ii % i1i1I1IIii1II % OOooOOo % IiI1i11I + IiI1i11I
def oOoooOooooo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + II1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 64 - 64: Ii / oOo0O0Ooo
def OOiiI1iii1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o0oooiIIIII1iiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 43 - 43: I11i * ii
def I1iI111iIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oO0OO00oOO0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 45 - 45: ii + oooOo0oo0oo - oooOo0oo0oo - i1iIi + I11i
def OOooOOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiIii1iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 51 - 51: III1iiIii * oooOo0oo0oo / Ii - IiI1i11I
def o00OO0O00O0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiiI11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 63 - 63: OOooOOo
def IiIiII ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Oo0ooOOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 96 - 96: ii + oooOo0oo0oo - i1IiiiI1iI / i1i1I1IIii1II % i1i1I1IIii1II
def iIiI1III1Ii1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oO00ooOoOoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 61 - 61: Iii / oooOo0oo0oo
def ooO0O0O0ooOOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOo0oOOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0o in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , O0o )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 79 - 79: ii * oO0o + oO0o % o0ii1I % oooOo0oo0oo * III1iiIii
 if 11 - 11: oooOo0oo0oo - o0ii1I
 if 44 - 44: i1i1I1IIii1II + i1i1I1IIii1II - Iii % Iii - Ii / I1ii11iIi11i
 if 51 - 51: oOo0O0Ooo * oOo0O0Ooo
 if 49 - 49: i1IiiiI1iI
 if 11 - 11: ooOoO0O00
 if 65 - 65: oO0o . i1iIi
 if 12 - 12: i1IiiiI1iI + o0o00Oo0O - i1i1I1IIii1II . III1iiIii
 if 46 - 46: III1iiIii . i1iIi / IiI1i11I
def IiOo00O0o0O ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OOOO00 , Ii1IIiII1I , OOOii in os . walk ( o0 ) :
     oo0Oo000 = 0
     oo0Oo000 += len ( OOOii )
     if oo0Oo000 > 0 :
      for O0oO0 in OOOii :
       os . unlink ( os . path . join ( OOOO00 , O0oO0 ) )
  I1iiiiiII1I1I = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( I1iiiiiII1I1I )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 71 - 71: i1IiiiI1iI
 if 67 - 67: I11i / o0ii1I * Ii / Ii1I
 if 9 - 9: oooOo0oo0oo * i1iIi - ii / o0o00Oo0O
 if 86 - 86: oOo0O0Ooo . I11i % o0ii1I - OOooOOo . ooOoO0O00
 if 30 - 30: IIiIiII11i + iI11I1II1I1I / Iii
 if 58 - 58: i1IiiiI1iI - Iii + i1i1I1IIii1II * oO0o
 if 45 - 45: III1iiIii * oooOo0oo0oo . oO0o
 if 56 - 56: III1iiIii * o0ii1I . IIiIiII11i / OOooOOo
def iIiiII1Ii1ii ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 70 - 70: Ii1I
def i111I1 ( url ) :
 oOo0O0o = os . path . join ( oooOOOOO , 'addon_data' )
 I11ii1I11III1 = [
 ( oOo0O0o ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( oOo0O0o , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOo0O0o , 'plugin.video.itv' , 'Images' ) ) ]
 if 12 - 12: OOooOOo + Iii . oO0o * Ii * Iii * i1IiiiI1iI
 Ii1i11iIi1iII = 0
 if 23 - 23: Iii + III1iiIii . i1i1I1IIii1II
 for ooo00Ooo in I11ii1I11III1 :
  if os . path . exists ( ooo00Ooo ) and not ooo00Ooo in [ oo0o0O00 , oOo0O0o ] :
   for OOOO00 , Ii1IIiII1I , OOOii in os . walk ( ooo00Ooo ) :
    oo0Oo000 = 0
    oo0Oo000 += len ( OOOii )
    if oo0Oo000 > 0 :
     for O0oO0 in OOOii :
      if not O0oO0 in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( OOOO00 , O0oO0 ) )
       except :
        pass
      else : O00Oooo ( 'Ignore Log File: %s' % O0oO0 )
     for O0o0o in Ii1IIiII1I :
      try :
       shutil . rmtree ( os . path . join ( OOOO00 , O0o0o ) )
       Ii1i11iIi1iII += 1
       O00Oooo ( "[Success] cleared %s files from %s" % ( str ( oo0Oo000 ) , os . path . join ( ooo00Ooo , O0o0o ) ) )
      except :
       O00Oooo ( "[Failed] to wipe cache in: %s" % os . path . join ( ooo00Ooo , O0o0o ) )
  else :
   for OOOO00 , Ii1IIiII1I , OOOii in os . walk ( ooo00Ooo ) :
    for O0o0o in Ii1IIiII1I :
     if 'cache' in O0o0o . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( OOOO00 , O0o0o ) )
       Ii1i11iIi1iII += 1
       O00Oooo ( "[Success] wiped %s " % os . path . join ( ooo00Ooo , O0o0o ) )
      except :
       O00Oooo ( "[Failed] to wipe cache in: %s" % os . path . join ( ooo00Ooo , O0o0o ) )
       if 33 - 33: oO0o / Ii / ooOoO0O00 . III1iiIii
 iIiiII1Ii1ii ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % Ii1i11iIi1iII )
 if 7 - 7: I1ii11iIi11i + III1iiIii
 if 15 - 15: iI11I1II1I1I % OOooOOo + ooOoO0O00 . o0ii1I - I1ii11iIi11i
 if 91 - 91: oOo0O0Ooo - ii - ii
 if 69 - 69: IiI1i11I * Ii / ooOoO0O00
 if 86 - 86: oOo0O0Ooo % Iii * o0o00Oo0O + ooOoO0O00 % i1IiiiI1iI
 if 97 - 97: IIiIiII11i * OOooOOo - i1IiiiI1iI / Ii / OOooOOo
 if 25 - 25: I1ii11iIi11i / I1ii11iIi11i
def OOOo0Oo0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oo0ooo0OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOOO00 , Ii1IIiII1I , OOOii in os . walk ( oo0ooo0OOO ) :
   oo0Oo000 = 0
   oo0Oo000 += len ( OOOii )
   if 32 - 32: III1iiIii
   if 1 - 1: oOo0O0Ooo
   if oo0Oo000 > 0 :
    if 25 - 25: o0o00Oo0O + oooOo0oo0oo / IiI1i11I
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( oo0Oo000 ) + " files found" , "Do you want to delete them?" ) :
     if 51 - 51: Iii
     for O0oO0 in OOOii :
      os . unlink ( os . path . join ( OOOO00 , O0oO0 ) )
     for O0o0o in Ii1IIiII1I :
      shutil . rmtree ( os . path . join ( OOOO00 , O0o0o ) )
     iIii1 = xbmcgui . Dialog ( )
     iIii1 . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    iIii1 = xbmcgui . Dialog ( )
    iIii1 . ok ( i1 , "       No Packages to DELETE" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 return
 if 54 - 54: ooOoO0O00 . o0o00Oo0O . ooOoO0O00 . oO0o + i1IiiiI1iI - Ii
 if 80 - 80: OOooOOo
 if 5 - 5: oOo0O0Ooo - oOo0O0Ooo / o0o00Oo0O + oooOo0oo0oo - Ii
 if 87 - 87: ooOoO0O00 - o0o00Oo0O % ii * Ii % Ii
 if 19 - 19: i1iIi
 if 44 - 44: i1IiiiI1iI - Ii * oOo0O0Ooo
 if 84 - 84: o0o00Oo0O % o0ii1I
 if 3 - 3: oOo0O0Ooo . Iii / Ii1I
 if 2 - 2: III1iiIii + Iii / iI11I1II1I1I . Ii . ooOoO0O00 * i1iIi
def ooO0O00Oo0o ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oo0ooo0OOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OOOO00 , Ii1IIiII1I , OOOii in os . walk ( oo0ooo0OOO ) :
   oo0Oo000 = 0
   oo0Oo000 += len ( OOOii )
   if 14 - 14: I1ii11iIi11i . o0o00Oo0O - i1i1I1IIii1II - Ii
   if 8 - 8: oOo0O0Ooo / iI11I1II1I1I / ii / I1ii11iIi11i / i1iIi
   if oo0Oo000 > 0 :
    if 80 - 80: Iii
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( oo0Oo000 ) + " files found" , "Do you want to delete them?" ) :
     if 26 - 26: IIiIiII11i + oOo0O0Ooo . IIiIiII11i - i1i1I1IIii1II % oO0o
     for O0oO0 in OOOii :
      os . unlink ( os . path . join ( OOOO00 , O0oO0 ) )
     for O0o0o in Ii1IIiII1I :
      shutil . rmtree ( os . path . join ( OOOO00 , O0o0o ) )
     iIii1 = xbmcgui . Dialog ( )
     iIii1 . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    iIii1 = xbmcgui . Dialog ( )
    iIii1 . ok ( i1 , "       No Packages to DELETE" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 i111I1 ( url )
 return
 if 1 - 1: oO0o - IIiIiII11i
 if 75 - 75: I1ii11iIi11i - OOooOOo + i1i1I1IIii1II % ooOoO0O00 * oooOo0oo0oo
 if 56 - 56: OOooOOo / oO0o / oOo0O0Ooo % ii
 if 39 - 39: oOo0O0Ooo + IIiIiII11i * I1ii11iIi11i % o0ii1I . I11i * i1i1I1IIii1II
 if 42 - 42: o0ii1I / I1ii11iIi11i
 if 25 - 25: ii % o0ii1I * i1IiiiI1iI * Iii + oOo0O0Ooo % Ii1I
 if 70 - 70: o0ii1I + Ii1I * Iii * ooOoO0O00 . i1IiiiI1iI
 if 76 - 76: ii * OOooOOo . ii
 if 46 - 46: i1iIi * I11i % IIiIiII11i / i1IiiiI1iI
 if 29 - 29: oO0o - Ii % I1ii11iIi11i % I11i
def iI111ii11 ( url , name ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oOoOoo0OOOo0 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 iIII1Ii1 = os . path . join ( o00oo0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( iIII1Ii1 ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   oOoOoo0OOOo0 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
   try :
    os . remove ( oOoOoo0OOOo0 )
    print '=== GenieTv - REMOVING    ' + str ( oOoOoo0OOOo0 ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   IIiiiI1iI = open ( oOoOoo0OOOo0 , "w" )
   IIiiiI1iI . write ( iiI111I1iIiI )
   IIiiiI1iI . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( oOoOoo0OOOo0 ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  oOoOoo0OOOo0 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
  try :
   os . remove ( oOoOoo0OOOo0 )
   print '=== GenieTv - REMOVING    ' + str ( oOoOoo0OOOo0 ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  IIiiiI1iI = open ( oOoOoo0OOOo0 , "w" )
  IIiiiI1iI . write ( iiI111I1iIiI )
  IIiiiI1iI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oOoOoo0OOOo0 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 58 - 58: i1iIi
def o00OI11II1II1iii ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oOoOoo0OOOo0 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
 try :
  IIiiiI1iI = open ( oOoOoo0OOOo0 ) . read ( )
  if 'zero' in IIiiiI1iI :
   name = '0CACHE'
  elif 'tuxen' in IIiiiI1iI :
   name = 'TUXENS'
  elif 'muckys' in IIiiiI1iI :
   name = 'MUCKYS'
  elif 'p2p1' in IIiiiI1iI :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in IIiiiI1iI :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in IIiiiI1iI :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 94 - 94: III1iiIii - I1ii11iIi11i . I11i - i1iIi - i1i1I1IIii1II . Iii
def iII1I1i ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oOoOoo0OOOo0 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
 try :
  os . remove ( oOoOoo0OOOo0 )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( oOoOoo0OOOo0 ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 33 - 33: i1iIi . oOo0O0Ooo . Ii % oO0o
 if 72 - 72: Ii1I / o0o00Oo0O % IIiIiII11i / IIiIiII11i
 if 48 - 48: oooOo0oo0oo % oooOo0oo0oo / iI11I1II1I1I - Ii
 if 57 - 57: Iii / III1iiIii * ooOoO0O00 + IIiIiII11i . I11i
 if 11 - 11: IIiIiII11i
 if 66 - 66: o0ii1I - oOo0O0Ooo . ii * i1IiiiI1iI
 if 16 - 16: III1iiIii * oO0o * Ii - i1iIi
 if 88 - 88: iI11I1II1I1I / o0ii1I * III1iiIii / i1IiiiI1iI
 if 31 - 31: o0o00Oo0O . oOo0O0Ooo
 if 8 - 8: OOooOOo
def i1I1I1iIIi ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for O0Ooo0O0OO , o0o0Oo0o0oOo , Ii1ii11i , OoooO0ooO00 in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % O0Ooo0O0OO , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % Ii1ii11i , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OoooO0ooO00 )
  inc = inc + 1
  if 61 - 61: I11i + IIiIiII11i + i1i1I1IIii1II + o0ii1I / i1IiiiI1iI . OOooOOo
  if 62 - 62: i1iIi
  if 13 - 13: ooOoO0O00 / oOo0O0Ooo . o0o00Oo0O * ooOoO0O00
  if 93 - 93: Ii1I . oO0o
  if 67 - 67: IIiIiII11i + ii + oOo0O0Ooo
  if 76 - 76: o0o00Oo0O / I1ii11iIi11i . OOooOOo
  if 81 - 81: I11i + IIiIiII11i % i1IiiiI1iI - i1i1I1IIii1II + i1iIi - Ii1I
  if 99 - 99: iI11I1II1I1I
  if 100 - 100: OOooOOo + i1IiiiI1iI * I1ii11iIi11i / III1iiIii - III1iiIii
def IiIoo0OOo ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  o00oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oOoOoo0OOOo0 = os . path . join ( o00oo0 , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  IIiiiI1iI = open ( oOoOoo0OOOo0 , "w" )
  IIiiiI1iI . write ( iiI111I1iIiI )
  IIiiiI1iI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oOoOoo0OOOo0 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 86 - 86: IiI1i11I / IiI1i11I . i1iIi - oO0o
def iI11iI1II1 ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  o00oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oOoOoo0OOOo0 = os . path . join ( o00oo0 , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  IIiiiI1iI = open ( oOoOoo0OOOo0 , "w" )
  IIiiiI1iI . write ( iiI111I1iIiI )
  IIiiiI1iI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oOoOoo0OOOo0 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 99 - 99: iI11I1II1I1I . OOooOOo . I11i / I1ii11iIi11i . o0ii1I
 if 17 - 17: ii - Ii1I
def I1IIIIi ( ) :
 try :
  iiIiI111Ii1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iiIiI111Ii1 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    o00oOO0o0oO0O = os . path . join ( iiIiI111Ii1 , "source.db" )
    os . unlink ( o00oOO0o0oO0O )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 49 - 49: OOooOOo - iI11I1II1I1I / III1iiIii - oOo0O0Ooo . i1IiiiI1iI - Iii
 if 33 - 33: III1iiIii - iI11I1II1I1I
 if 77 - 77: oooOo0oo0oo . Ii1I / IIiIiII11i % iI11I1II1I1I * Ii
 if 9 - 9: i1i1I1IIii1II - ooOoO0O00 . i1iIi + Ii1I
 if 72 - 72: i1iIi
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 47 - 47: iI11I1II1I1I . oooOo0oo0oo / Iii % IIiIiII11i
 if 92 - 92: Ii1I % Ii
 if 82 - 82: i1IiiiI1iI * Ii1I % o0ii1I / I11i
 if 28 - 28: IiI1i11I % oO0o - oooOo0oo0oo - I1ii11iIi11i
 if 16 - 16: Ii - Ii . OOooOOo / ooOoO0O00
 if 76 - 76: o0o00Oo0O * oO0o / o0o00Oo0O
 if 23 - 23: Ii1I . iI11I1II1I1I - Ii / IIiIiII11i
def OOOOoO00o0O ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; iI1ii1I1i = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iI1ii1I1i :
  oo00o = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; oo00o = xbmc . translatePath ( oo00o ) ;
  iioO0OoOoo00 = os . path . join ( oo00o , ".." , ".." ) ; iioO0OoOoo00 = os . path . abspath ( iioO0OoOoo00 ) ; pluginlog ( "freshstart.main_list xbmcPath=" + iioO0OoOoo00 ) ; IIiiIi1i = False
  try :
   for OOOO00 , Ii1IIiII1I , OOOii in os . walk ( iioO0OoOoo00 , topdown = True ) :
    Ii1IIiII1I [ : ] = [ O0o0o for O0o0o in Ii1IIiII1I if O0o0o not in o0oO0 ]
    for iIIIiIi in OOOii :
     try : os . remove ( os . path . join ( OOOO00 , iIIIiIi ) )
     except :
      if iIIIiIi not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIiiIi1i = True
      pluginlog ( "Error removing " + OOOO00 + " " + iIIIiIi )
    for iIIIiIi in Ii1IIiII1I :
     try : os . rmdir ( os . path . join ( OOOO00 , iIIIiIi ) )
     except :
      if iIIIiIi not in [ "Database" , "userdata" ] : IIiiIi1i = True
      pluginlog ( "Error removing " + OOOO00 + " " + iIIIiIi )
   if not IIiiIi1i : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 iI1I ( )
 if 15 - 15: IIiIiII11i % ooOoO0O00 / i1i1I1IIii1II . iI11I1II1I1I * I1ii11iIi11i
 if 5 - 5: IiI1i11I
 if 61 - 61: oooOo0oo0oo * oO0o - o0o00Oo0O
def iiiI1IiiIII1ii ( ) :
 iiOo00ooO0 = [ ]
 IiIIIIiIi = sys . argv [ 2 ]
 if len ( IiIIIIiIi ) >= 2 :
  I1I1I1IIi1III = sys . argv [ 2 ]
  oo0IIII1 = I1I1I1IIi1III . replace ( '?' , '' )
  if ( I1I1I1IIi1III [ len ( I1I1I1IIi1III ) - 1 ] == '/' ) :
   I1I1I1IIi1III = I1I1I1IIi1III [ 0 : len ( I1I1I1IIi1III ) - 2 ]
  II1ii111 = oo0IIII1 . split ( '&' )
  iiOo00ooO0 = { }
  for iio0Oo in range ( len ( II1ii111 ) ) :
   iII1Iiii11I1i = { }
   iII1Iiii11I1i = II1ii111 [ iio0Oo ] . split ( '=' )
   if ( len ( iII1Iiii11I1i ) ) == 2 :
    iiOo00ooO0 [ iII1Iiii11I1i [ 0 ] ] = iII1Iiii11I1i [ 1 ]
    if 30 - 30: i1i1I1IIii1II / i1IiiiI1iI * i1iIi % oO0o + oO0o
 return iiOo00ooO0
 if 6 - 6: III1iiIii + oO0o
Ii1Ii1iii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
OOooooO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
iIIi111IiII1i = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
i1iIIIIi = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I1IiiiI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iIii1IiI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
ii11iOoo0oO0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
Iiii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
IiIIi = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
II1II = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
o0oooiIIIII1iiI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
oO0OO00oOO0o0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
IiIii1iII = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
IiiI11I = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
Oo0ooOOO0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
oO00ooOoOoOO = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
IIIIII1iI1II = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iII1ii1iiIII = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o0III11IiI = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OoO00oo0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
ooooOOO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oOOoOOooO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
OOo0oOOO0 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OO0Oo00 = base64 . decodestring ( 'Q1VOVA==' )
def OoO000Oo0oO ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 iiIIIiIii . setProperty ( 'fanart_image' , fanart )
 iiIIIiIii . setProperty ( "IsPlayable" , "true" )
 II1oo0OO0OoO = [ ]
 II1oo0OO0OoO . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 II1oo0OO0OoO . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 iiIIIiIii . addContextMenuItems ( II1oo0OO0OoO , replaceItems = True )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
def I1I1II1I11 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = True )
 return II1
 if 5 - 5: IIiIiII11i
def Ii1I1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I111IIiii1Ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 II1 = True
 iiIIIiIii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiIIIiIii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iiIIIiIii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1i11II = [ ]
  if showcontext == 'fav' :
   I1i11II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   I1i11II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiIIIiIii . addContextMenuItems ( I1i11II )
 II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I111IIiii1Ii , listitem = iiIIIiIii , isFolder = False )
 return II1
 if 88 - 88: ii % IIiIiII11i + III1iiIii + III1iiIii * I1ii11iIi11i
 if 81 - 81: oOo0O0Ooo * i1iIi + i1IiiiI1iI
I1I1I1IIi1III = iiiI1IiiIII1ii ( )
oOOo0O00o = None
iIIIiIi = None
O0oOOo0Oo = None
iiiI1I1iIIIi1 = None
IIo0o0O0O00oOOo = None
O0o = None
Ii1I1iIiIi = None
O0oOooOoOo = None
if 54 - 54: IiI1i11I . oO0o . iI11I1II1I1I
if 45 - 45: Ii1I + oOo0O0Ooo / Ii
try :
 O0oOooOoOo = int ( I1I1I1IIi1III [ "fav_mode" ] )
except :
 pass
 if 45 - 45: III1iiIii / o0o00Oo0O * oOo0O0Ooo - oooOo0oo0oo * i1IiiiI1iI
try :
 oOOo0O00o = urllib . unquote_plus ( I1I1I1IIi1III [ "url" ] )
except :
 pass
try :
 iIIIiIi = urllib . unquote_plus ( I1I1I1IIi1III [ "name" ] )
except :
 pass
try :
 iiiI1I1iIIIi1 = urllib . unquote_plus ( I1I1I1IIi1III [ "iconimage" ] )
except :
 pass
try :
 O0oOOo0Oo = int ( I1I1I1IIi1III [ "mode" ] )
except :
 pass
try :
 IIo0o0O0O00oOOo = urllib . unquote_plus ( I1I1I1IIi1III [ "fanart" ] )
except :
 pass
try :
 O0o = urllib . unquote_plus ( I1I1I1IIi1III [ "description" ] )
except :
 pass
 if 19 - 19: OOooOOo / III1iiIii - oooOo0oo0oo * Ii % i1IiiiI1iI
 if 98 - 98: III1iiIii + III1iiIii + oooOo0oo0oo / ooOoO0O00 + i1i1I1IIii1II
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( O0oOOo0Oo )
print "URL: " + str ( oOOo0O00o )
print "Name: " + str ( iIIIiIi )
print "IconImage: " + str ( iiiI1I1iIIIi1 )
if 53 - 53: OOooOOo
if 69 - 69: iI11I1II1I1I * oO0o / ii % Ii1I . oOo0O0Ooo % Iii
def I1iI1ii1II ( content , viewType ) :
 if 40 - 40: Ii % i1i1I1IIii1II / oooOo0oo0oo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 85 - 85: oO0o % o0o00Oo0O . o0ii1I . IiI1i11I . IiI1i11I
if iiiI1I1iIIIi1 == None : iiiI1I1iIIIi1 = O0O
if IIo0o0O0O00oOOo == None : IIo0o0O0O00oOOo = Oo00OOOOO
if O0oOOo0Oo == None :
 Iii1I1I11iiI1 ( )
 if 90 - 90: I11i - I1ii11iIi11i / i1iIi / ooOoO0O00 - o0ii1I
elif O0oOOo0Oo == 1 :
 ii1iIIIiIiII ( oOOo0O00o )
 if 43 - 43: Ii - ii % i1iIi
elif O0oOOo0Oo == 44 :
 II11IiiIII ( oOOo0O00o )
 if 55 - 55: i1i1I1IIii1II % I1ii11iIi11i % III1iiIii
elif O0oOOo0Oo == 2 :
 OooO00o000 ( )
 if 65 - 65: III1iiIii * III1iiIii
elif O0oOOo0Oo == 3 :
 IIoO ( )
 if 60 - 60: i1iIi
elif O0oOOo0Oo == 21 :
 i1i1II ( )
 if 92 - 92: o0o00Oo0O % III1iiIii
elif O0oOOo0Oo == 4 :
 I1iO0o0O0OooOoo ( )
 if 15 - 15: o0o00Oo0O % ooOoO0O00 - oooOo0oo0oo . III1iiIii
elif O0oOOo0Oo == 5 :
 o0O0O0O00o ( oOOo0O00o )
 if 1 - 1: oOo0O0Ooo
elif O0oOOo0Oo == 6 :
 OOOo0Oo0O ( oOOo0O00o )
 if 40 - 40: I11i % Iii % o0o00Oo0O
elif O0oOOo0Oo == 7 :
 iI111ii11 ( oOOo0O00o , iIIIiIi )
 if 88 - 88: I11i - i1i1I1IIii1II
elif O0oOOo0Oo == 8 :
 o00OI11II1II1iii ( oOOo0O00o , iIIIiIi )
 if 73 - 73: IIiIiII11i
elif O0oOOo0Oo == 9 :
 FIXREPOSADDONS ( oOOo0O00o )
 if 7 - 7: o0o00Oo0O / oO0o
elif O0oOOo0Oo == 10 :
 OOOOo0o00OO0000 ( )
 if 90 - 90: IiI1i11I % i1i1I1IIii1II / iI11I1II1I1I
elif O0oOOo0Oo == 11 :
 iII1I1i ( oOOo0O00o )
 if 52 - 52: oOo0O0Ooo / I11i
elif O0oOOo0Oo == 12 :
 i1I1I1iIIi ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 20 - 20: i1IiiiI1iI . oOo0O0Ooo - iI11I1II1I1I / IiI1i11I
elif O0oOOo0Oo == 13 :
 IiOo00O0o0O ( )
 if 46 - 46: i1IiiiI1iI . Ii
elif O0oOOo0Oo == 14 :
 i111I1 ( oOOo0O00o )
 if 89 - 89: oO0o - oooOo0oo0oo - ooOoO0O00 - oO0o % iI11I1II1I1I
elif O0oOOo0Oo == 15 :
 oOOooO ( )
 if 52 - 52: I11i * o0o00Oo0O + Ii1I
elif O0oOOo0Oo == 16 :
 IiIoo0OOo ( oOOo0O00o , iIIIiIi )
 if 83 - 83: Iii + oooOo0oo0oo - ii
elif O0oOOo0Oo == 17 :
 iI11iI1II1 ( oOOo0O00o , iIIIiIi )
 if 7 - 7: III1iiIii % i1iIi / ii / I11i + oO0o - oO0o
elif O0oOOo0Oo == 18 :
 I1IIIIi ( )
 if 15 - 15: ooOoO0O00 + oooOo0oo0oo / o0ii1I
elif O0oOOo0Oo == 19 :
 oOoO ( oOOo0O00o )
 if 51 - 51: oooOo0oo0oo + o0o00Oo0O
elif O0oOOo0Oo == 40 :
 iII1i1 ( iIIIiIi , oOOo0O00o , O0o )
 if 91 - 91: Ii + I11i % oO0o / i1i1I1IIii1II - ooOoO0O00
elif O0oOOo0Oo == 42 :
 oo0O00o0 ( iIIIiIi , oOOo0O00o , O0o )
 if 82 - 82: o0ii1I . ii + ii % oO0o % Ii1I
elif O0oOOo0Oo == 43 :
 iiI11111II ( oOOo0O00o )
 if 65 - 65: I1ii11iIi11i . Iii
elif O0oOOo0Oo == 20 :
 II1iOOoOooO0o ( oOOo0O00o )
 if 7 - 7: I1ii11iIi11i * IIiIiII11i
elif O0oOOo0Oo == 22 :
 iI1IIi1I ( oOOo0O00o )
 if 11 - 11: OOooOOo % ii
elif O0oOOo0Oo == 23 :
 O0O0OoO0o0OO ( oOOo0O00o )
 if 92 - 92: OOooOOo - IiI1i11I * o0ii1I - ooOoO0O00
elif O0oOOo0Oo == 24 :
 oOoooOooooo0 ( oOOo0O00o )
 if 87 - 87: o0ii1I * i1IiiiI1iI + iI11I1II1I1I * I11i * iI11I1II1I1I . Iii
elif O0oOOo0Oo == 25 :
 OOiiI1iii1I ( oOOo0O00o )
 if 66 - 66: o0ii1I / oO0o . o0o00Oo0O . Iii % ii / oooOo0oo0oo
elif O0oOOo0Oo == 26 :
 I1iI111iIi ( oOOo0O00o )
 if 49 - 49: oOo0O0Ooo * IiI1i11I - oO0o % o0ii1I + o0ii1I * i1IiiiI1iI
elif O0oOOo0Oo == 27 :
 OOooOOO ( oOOo0O00o )
 if 94 - 94: OOooOOo - Iii + o0ii1I + OOooOOo + IIiIiII11i
elif O0oOOo0Oo == 28 :
 o00OO0O00O0 ( oOOo0O00o )
 if 61 - 61: III1iiIii + o0ii1I / i1i1I1IIii1II . ii + IiI1i11I
elif O0oOOo0Oo == 29 :
 IiIiII ( oOOo0O00o )
 if 29 - 29: oooOo0oo0oo
elif O0oOOo0Oo == 30 :
 o0oo00O ( oOOo0O00o )
 if 69 - 69: i1i1I1IIii1II % ii * IiI1i11I
elif O0oOOo0Oo == 31 :
 iIiI1III1Ii1 ( oOOo0O00o )
 if 58 - 58: i1i1I1IIii1II / Ii . OOooOOo % o0o00Oo0O / iI11I1II1I1I
elif O0oOOo0Oo == 32 :
 o0oO00OOo0oO ( )
 if 50 - 50: i1IiiiI1iI . Iii / o0o00Oo0O . Iii
elif O0oOOo0Oo == 33 :
 oOiiI11I1ii11 ( )
 if 91 - 91: Ii . Ii1I + Iii
elif O0oOOo0Oo == 35 :
 i1ii11I111Ii ( oOOo0O00o )
 if 67 - 67: Ii1I * i1IiiiI1iI * oOo0O0Ooo / Iii - III1iiIii + i1i1I1IIii1II
elif O0oOOo0Oo == 34 :
 O0OoO0oooOO ( oOOo0O00o )
 if 11 - 11: o0o00Oo0O + ooOoO0O00 / I11i * oO0o
elif O0oOOo0Oo == 36 :
 i1111I ( oOOo0O00o )
 if 64 - 64: ooOoO0O00 % III1iiIii . i1iIi . iI11I1II1I1I + oO0o - iI11I1II1I1I
elif O0oOOo0Oo == 37 :
 oOOO00 ( oOOo0O00o )
 if 52 - 52: IIiIiII11i - III1iiIii
elif O0oOOo0Oo == 38 :
 IIii1Ii1i1ii1 ( oOOo0O00o )
 if 91 - 91: iI11I1II1I1I + IiI1i11I . Iii % Ii - Ii + oOo0O0Ooo
elif O0oOOo0Oo == 41 :
 OOOOoO00o0O ( I1I1I1IIi1III )
 if 75 - 75: Ii1I / oOo0O0Ooo - iI11I1II1I1I / oO0o * oooOo0oo0oo
elif O0oOOo0Oo == 39 :
 ooO0O0O0ooOOO ( oOOo0O00o )
 if 73 - 73: ii % III1iiIii / i1IiiiI1iI * Iii + ooOoO0O00 % Ii
elif O0oOOo0Oo == 45 :
 TEXTS ( )
 if 91 - 91: Ii
elif O0oOOo0Oo == 46 :
 iIiIi11 ( )
 if 6 - 6: o0o00Oo0O - iI11I1II1I1I + i1IiiiI1iI . I11i * Ii
elif O0oOOo0Oo == 47 :
 GEVID ( )
 if 53 - 53: oooOo0oo0oo / oOo0O0Ooo / i1i1I1IIii1II * oooOo0oo0oo / ooOoO0O00 - i1IiiiI1iI
elif O0oOOo0Oo == 48 :
 o0oOO0 ( iIIIiIi , oOOo0O00o , O0o )
 if 71 - 71: o0o00Oo0O + I1ii11iIi11i % i1i1I1IIii1II - I11i
elif O0oOOo0Oo == 49 :
 II1III1I1I1Ii ( )
 if 82 - 82: iI11I1II1I1I
elif O0oOOo0Oo == 22222 :
 OoOoooO000OO ( oOOo0O00o )
 if 64 - 64: i1iIi + oOo0O0Ooo % oooOo0oo0oo + IIiIiII11i
elif O0oOOo0Oo == 222225 :
 OO0O0o0o0 ( oOOo0O00o )
 if 46 - 46: oOo0O0Ooo
elif O0oOOo0Oo == 222 :
 IiIi1i1 ( oOOo0O00o )
 if 72 - 72: IiI1i11I
elif O0oOOo0Oo == 2222222 :
 I11iiiiI1i ( oOOo0O00o )
 if 100 - 100: oOo0O0Ooo
elif O0oOOo0Oo == 222222 :
 o0000o0o ( oOOo0O00o , iIIIiIi )
 if 55 - 55: ooOoO0O00 % III1iiIii
elif O0oOOo0Oo == 333 :
 IIiiiiIii ( oOOo0O00o )
 if 44 - 44: i1i1I1IIii1II - iI11I1II1I1I / i1iIi - iI11I1II1I1I % ooOoO0O00 + i1iIi
 if 74 - 74: Iii . OOooOOo + OOooOOo
elif O0oOOo0Oo == 1020 :
 ooOOOo ( )
 if 87 - 87: III1iiIii + I11i . ooOoO0O00 % i1IiiiI1iI
elif O0oOOo0Oo == 1021 :
 ANIMEEP ( )
 if 44 - 44: I1ii11iIi11i - oooOo0oo0oo . o0ii1I * ii
elif O0oOOo0Oo == 1022 :
 ANIMEPLAY ( oOOo0O00o )
 if 93 - 93: oO0o . oO0o
elif O0oOOo0Oo == 1001 :
 iiiiIIiiII1Iii1 ( )
 if 52 - 52: oooOo0oo0oo . i1i1I1IIii1II / I1ii11iIi11i . ii % Ii1I
elif O0oOOo0Oo == 1005 :
 o0ooo0O00 ( )
 if 65 - 65: i1iIi % IIiIiII11i . IiI1i11I - iI11I1II1I1I - oOo0O0Ooo
elif O0oOOo0Oo == 1007 :
 oo00O0Ooo ( oOOo0O00o )
 if 63 - 63: oOo0O0Ooo . OOooOOo - IIiIiII11i
elif O0oOOo0Oo == 1010 :
 OOOOoO0 ( oOOo0O00o )
 if 55 - 55: i1iIi - I11i
elif O0oOOo0Oo == 1011 :
 ooOOO000 ( oOOo0O00o )
 if 32 - 32: i1IiiiI1iI * o0ii1I / i1IiiiI1iI . OOooOOo + Ii1I - i1iIi
elif O0oOOo0Oo == 1012 :
 oooOoOOOoo0 ( oOOo0O00o )
 if 14 - 14: III1iiIii * o0o00Oo0O + o0o00Oo0O - i1iIi . Ii - III1iiIii
elif O0oOOo0Oo == 1030 :
 O0OoO ( )
 if 37 - 37: Iii
elif O0oOOo0Oo == 1031 :
 oOo0O00 ( oOOo0O00o , iiiI1I1iIIIi1 )
 if 19 - 19: ii % i1IiiiI1iI
elif O0oOOo0Oo == 1032 :
 O0OoOo ( oOOo0O00o )
 if 57 - 57: OOooOOo + ooOoO0O00 . iI11I1II1I1I . iI11I1II1I1I / iI11I1II1I1I % i1i1I1IIii1II
elif O0oOOo0Oo == 1006 :
 Parse . ParseURL ( oOOo0O00o )
 if 7 - 7: Ii * Ii1I / oO0o * i1i1I1IIii1II
elif O0oOOo0Oo == 2030 :
 Parse . addonParseURL ( oOOo0O00o )
 if 35 - 35: III1iiIii . ooOoO0O00 + Ii1I . III1iiIii + i1iIi . i1i1I1IIii1II
elif O0oOOo0Oo == 2031 :
 Parse . apkParseURL ( oOOo0O00o )
 if 2 - 2: IIiIiII11i
elif O0oOOo0Oo == 2032 :
 Parse . ParseBOSS ( oOOo0O00o )
 if 18 - 18: iI11I1II1I1I % Ii1I % I1ii11iIi11i
elif O0oOOo0Oo == 1002 :
 I1I1i ( oOOo0O00o )
 if 47 - 47: i1iIi - oOo0O0Ooo % oooOo0oo0oo * o0ii1I % oOo0O0Ooo
elif O0oOOo0Oo == 1003 :
 OOii ( oOOo0O00o , iiiI1I1iIIIi1 )
 if 95 - 95: oO0o + OOooOOo % I1ii11iIi11i . o0ii1I * oOo0O0Ooo + i1IiiiI1iI
elif O0oOOo0Oo == 1004 :
 o0ooo ( oOOo0O00o )
 if 22 - 22: I1ii11iIi11i . oO0o
elif O0oOOo0Oo == 1008 :
 iI1Iiiii ( )
 if 55 - 55: I1ii11iIi11i % ii * IIiIiII11i % ii
elif O0oOOo0Oo == 1009 :
 iiI11IIiIiI1 ( oOOo0O00o )
 if 30 - 30: i1IiiiI1iI / I11i + ii + OOooOOo + oO0o
elif O0oOOo0Oo == 2001 :
 I1IIiIIii1II1 ( )
 if 40 - 40: ii / III1iiIii
elif O0oOOo0Oo == 2002 :
 IiI1i1iIi1 ( oOOo0O00o )
 if 82 - 82: Ii - i1i1I1IIii1II - ooOoO0O00
elif O0oOOo0Oo == 1013 :
 O0ooooO ( )
elif O0oOOo0Oo == 10111113 :
 Oooo0oOooOO ( oOOo0O00o )
 if 78 - 78: i1i1I1IIii1II % IiI1i11I / ooOoO0O00 / i1iIi
elif O0oOOo0Oo == 1014 :
 o0o000OOO ( )
 if 44 - 44: I11i + o0ii1I + oOo0O0Ooo % o0o00Oo0O
elif O0oOOo0Oo == 1015 :
 I1111iii1ii11 ( oOOo0O00o )
 if 100 - 100: ii
elif O0oOOo0Oo == 1016 :
 I1IIIiI1I1ii1 ( oOOo0O00o , iiiI1I1iIIIi1 , iIIIiIi )
 if 27 - 27: Ii % IIiIiII11i + i1IiiiI1iI
elif O0oOOo0Oo == 1017 :
 oOoO00 ( )
 if 76 - 76: oooOo0oo0oo - i1IiiiI1iI + iI11I1II1I1I + oOo0O0Ooo * i1i1I1IIii1II
elif O0oOOo0Oo == 1018 :
 IiiI1iiiiI1iI ( oOOo0O00o )
 if 93 - 93: Ii * Ii - oOo0O0Ooo + iI11I1II1I1I * Ii
elif O0oOOo0Oo == 1019 :
 IiI11i1IIiiI ( oOOo0O00o )
elif O0oOOo0Oo == 10190 :
 OoOo00o0OO ( oOOo0O00o )
 if 14 - 14: i1iIi . ii . oOo0O0Ooo - III1iiIii + iI11I1II1I1I
elif O0oOOo0Oo == 1023 :
 oooOOo0oOoOO ( )
 if 47 - 47: oooOo0oo0oo % ooOoO0O00
elif O0oOOo0Oo == 1024 :
 II1II1iiIiI ( oOOo0O00o )
 if 23 - 23: o0ii1I * o0ii1I / Iii
elif O0oOOo0Oo == 1025 :
 i1IOO0O0ooOo ( oOOo0O00o )
 if 11 - 11: oooOo0oo0oo
elif O0oOOo0Oo == 4001 :
 o000oo ( )
 if 58 - 58: oO0o * ii
elif O0oOOo0Oo == 4002 :
 i1i1ii ( )
 if 47 - 47: IiI1i11I - I1ii11iIi11i
elif O0oOOo0Oo == 4003 :
 iIIII11i ( )
 if 19 - 19: o0o00Oo0O . ooOoO0O00 + Iii / IIiIiII11i + i1iIi
elif O0oOOo0Oo == 4004 :
 IIIi ( )
 if 26 - 26: o0ii1I * i1i1I1IIii1II % oOo0O0Ooo - oooOo0oo0oo . i1IiiiI1iI
elif O0oOOo0Oo == 4005 :
 IIi1ii1Ii ( )
 if 35 - 35: ooOoO0O00 % Ii + o0ii1I
elif O0oOOo0Oo == 4006 :
 oOO00O0Ooooo00 ( )
 if 14 - 14: oO0o * ii
elif O0oOOo0Oo == 4007 :
 Oo0OO0000oooo ( )
 if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . OOooOOo
elif O0oOOo0Oo == 4008 :
 ii1III11 ( )
 if 97 - 97: Iii % IIiIiII11i % o0ii1I . IIiIiII11i . iI11I1II1I1I
elif O0oOOo0Oo == 40099 : i1IiI ( )
elif O0oOOo0Oo == 4009 : O0oo00oOOO0o ( )
elif O0oOOo0Oo == 4010 : i11iiI ( )
elif O0oOOo0Oo == 3000 :
 oOo ( )
 if 98 - 98: Ii + o0o00Oo0O - o0o00Oo0O - IiI1i11I
elif O0oOOo0Oo == 3001 :
 oo00000ooOooO ( )
 if 25 - 25: i1i1I1IIii1II / o0o00Oo0O + i1IiiiI1iI % Ii / oOo0O0Ooo
elif O0oOOo0Oo == 3002 :
 oo0o0OO00oOO ( oOOo0O00o )
 if 62 - 62: IiI1i11I . Iii * ooOoO0O00 + IiI1i11I
elif O0oOOo0Oo == 3003 :
 IiiII1iIi ( oOOo0O00o )
 if 95 - 95: o0ii1I / I11i % i1iIi - oOo0O0Ooo / oooOo0oo0oo * oooOo0oo0oo
elif O0oOOo0Oo == 3004 :
 iiiiii ( oOOo0O00o )
 if 6 - 6: oO0o % III1iiIii + iI11I1II1I1I
elif O0oOOo0Oo == 404 :
 O00o0OooOOO ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 )
 if 18 - 18: IIiIiII11i . o0ii1I + OOooOOo + o0o00Oo0O - Iii
elif O0oOOo0Oo == 405 :
 ii1II1i1 ( oOOo0O00o )
 if 30 - 30: IIiIiII11i
elif O0oOOo0Oo == 7030 :
 oOoOOo00oO ( )
 if 26 - 26: Iii - ooOoO0O00 - I1ii11iIi11i * o0o00Oo0O * oooOo0oo0oo . ii
elif O0oOOo0Oo == 7021 :
 IIIIIIi1I ( iIIIiIi )
 if 99 - 99: i1i1I1IIii1II . oO0o / oooOo0oo0oo
elif O0oOOo0Oo == 7022 :
 iI1II ( iIIIiIi )
 if 12 - 12: iI11I1II1I1I + i1iIi * i1IiiiI1iI % ii / iI11I1II1I1I
elif O0oOOo0Oo == 7000 :
 o0ooOoOoO0o ( iIIIiIi , oOOo0O00o , img )
 if 43 - 43: o0o00Oo0O . ooOoO0O00 - ii - ooOoO0O00 - Ii1I
elif O0oOOo0Oo == 7050 :
 o0ooOooO ( oOOo0O00o )
 if 8 - 8: OOooOOo / o0ii1I
elif O0oOOo0Oo == 7051 :
 II1i1i ( oOOo0O00o )
 if 12 - 12: iI11I1II1I1I
elif O0oOOo0Oo == 7052 :
 i11II ( oOOo0O00o )
 if 52 - 52: i1i1I1IIii1II . Ii1I + i1i1I1IIii1II
elif O0oOOo0Oo == 7053 :
 II1OoOOoOOOoooO0 ( oOOo0O00o )
 if 73 - 73: IIiIiII11i / Ii / i1iIi
elif O0oOOo0Oo == 7054 :
 CoolPlay ( oOOo0O00o )
 if 1 - 1: IiI1i11I + OOooOOo / III1iiIii - oOo0O0Ooo % oOo0O0Ooo
elif O0oOOo0Oo == 7060 :
 i1IOO ( )
 if 6 - 6: OOooOOo - ooOoO0O00 + IIiIiII11i % i1i1I1IIii1II
elif O0oOOo0Oo == 7061 :
 IIiiI ( oOOo0O00o )
 if 72 - 72: oooOo0oo0oo + oooOo0oo0oo
elif O0oOOo0Oo == 7063 :
 Oo0OO0ooO0O0O ( oOOo0O00o )
 if 30 - 30: Iii
elif O0oOOo0Oo == 7062 :
 IIIiiii1 ( oOOo0O00o )
 if 15 - 15: o0o00Oo0O - ooOoO0O00 . iI11I1II1I1I - Ii / o0ii1I
elif O0oOOo0Oo == 7064 :
 NATatozcat ( )
 if 11 - 11: iI11I1II1I1I + oOo0O0Ooo
elif O0oOOo0Oo == 7067 :
 oOO0o0OO ( oOOo0O00o )
 if 15 - 15: I11i
elif O0oOOo0Oo == 7066 :
 NATatozA ( oOOo0O00o )
 if 55 - 55: Ii / ii - Iii
elif O0oOOo0Oo == 7065 :
 oo0Oooo0O ( oOOo0O00o )
 if 89 - 89: Iii - ooOoO0O00 - ooOoO0O00 * oooOo0oo0oo - o0o00Oo0O
elif O0oOOo0Oo == 7070 :
 o0000oOoo0o0o ( )
 if 94 - 94: I1ii11iIi11i / Iii . Ii1I
elif O0oOOo0Oo == 7071 :
 DIZIlist ( oOOo0O00o )
 if 31 - 31: Ii + iI11I1II1I1I . IIiIiII11i
elif O0oOOo0Oo == 7072 :
 DIZIpull ( oOOo0O00o )
 if 72 - 72: i1IiiiI1iI * oO0o + I1ii11iIi11i / o0ii1I % oooOo0oo0oo
elif O0oOOo0Oo == 7073 :
 WATCHDIZI ( oOOo0O00o )
 if 84 - 84: OOooOOo / I11i
elif O0oOOo0Oo == 7002 :
 O0oOo ( )
 if 9 - 9: o0ii1I
elif O0oOOo0Oo == 7003 :
 ooo0oO0o000O0 ( oOOo0O00o )
 if 76 - 76: oOo0O0Ooo % I1ii11iIi11i / iI11I1II1I1I - I1ii11iIi11i
elif O0oOOo0Oo == 7004 :
 oo00o0Oo0O0 ( oOOo0O00o )
 if 34 - 34: OOooOOo - ooOoO0O00 + oooOo0oo0oo + o0ii1I . I11i
elif O0oOOo0Oo == 7020 :
 O00o000O0 ( oOOo0O00o )
 if 42 - 42: oO0o
elif O0oOOo0Oo == 7001 :
 Ii1I11ii1i ( )
 if 59 - 59: oO0o . i1IiiiI1iI % oO0o
elif O0oOOo0Oo == 7010 :
 iiiii1I ( oOOo0O00o )
 if 22 - 22: I1ii11iIi11i
elif O0oOOo0Oo == 7011 :
 O0OooOoOOoooO00oO ( oOOo0O00o )
 if 21 - 21: I11i
elif O0oOOo0Oo == 7012 :
 OOoo0o000 ( oOOo0O00o )
 if 86 - 86: i1iIi / iI11I1II1I1I . oooOo0oo0oo
elif O0oOOo0Oo == 7013 :
 cnfTVPlay2 ( oOOo0O00o )
elif O0oOOo0Oo == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oOOo0O00o )
elif O0oOOo0Oo == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oOOo0O00o )
elif O0oOOo0Oo == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif O0oOOo0Oo == 7018 :
 O00OoO0oo ( )
elif O0oOOo0Oo == 7019 :
 CNF_Studio_Indexer . List_Movies ( oOOo0O00o )
elif O0oOOo0Oo == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oOOo0O00o )
elif O0oOOo0Oo == 7024 :
 CNF_Studio_Indexer . Box_Office ( oOOo0O00o )
 if 93 - 93: I1ii11iIi11i / IIiIiII11i . I1ii11iIi11i + ooOoO0O00 + ooOoO0O00
elif O0oOOo0Oo == 8000 :
 iII1I1iIIIiII ( )
elif O0oOOo0Oo == 8001 :
 OOoOO00O ( )
elif O0oOOo0Oo == 8002 :
 i1oO0o00oOo00oO ( )
elif O0oOOo0Oo == 8003 :
 IIiIiI1III1 ( )
elif O0oOOo0Oo == 8004 :
 oooOoo ( )
elif O0oOOo0Oo == 8005 :
 ii1i1iIiIIi ( )
elif O0oOOo0Oo == 8006 :
 O0O0Oo00o0oO ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 8030 :
 Iii11iI1I ( oOOo0O00o )
elif O0oOOo0Oo == 8045 :
 IIi1iii ( oOOo0O00o )
elif O0oOOo0Oo == 8046 :
 ii1Ii ( oOOo0O00o )
elif O0oOOo0Oo == 8047 :
 O0Ii1iIii1I1 ( oOOo0O00o )
elif O0oOOo0Oo == 8048 :
 i11i1 ( oOOo0O00o )
elif O0oOOo0Oo == 8049 :
 O0O0I1II ( oOOo0O00o )
elif O0oOOo0Oo == 804900 :
 o0o0OoOO00Oo ( oOOo0O00o )
elif O0oOOo0Oo == 8020 :
 iII1111III1I ( )
elif O0oOOo0Oo == 8021 :
 I1I111 ( oOOo0O00o )
elif O0oOOo0Oo == 8022 :
 oOO0oOo0OOoOO ( oOOo0O00o )
elif O0oOOo0Oo == 8023 :
 o0O00oo0Ooo ( oOOo0O00o )
elif O0oOOo0Oo == 8040 :
 I1iiIIIi11 ( )
elif O0oOOo0Oo == 8041 :
 i1iII1IiI1I ( oOOo0O00o )
elif O0oOOo0Oo == 8042 :
 I11II1i1I11I1 ( oOOo0O00o )
elif O0oOOo0Oo == 8043 :
 yt . PlayVideo ( oOOo0O00o )
elif O0oOOo0Oo == 8044 :
 i1iI1I1I ( oOOo0O00o )
elif O0oOOo0Oo == 8060 :
 I1iIiIi11i11 ( )
elif O0oOOo0Oo == 8061 :
 IiII11I1I1IIi ( oOOo0O00o )
elif O0oOOo0Oo == 8064 :
 O00oOo00o0o ( )
elif O0oOOo0Oo == 8065 :
 I111 ( oOOo0O00o )
elif O0oOOo0Oo == 8070 :
 OOoOooO0o ( )
elif O0oOOo0Oo == 8071 :
 OOoOI1i1i1Iii1 ( oOOo0O00o )
elif O0oOOo0Oo == 7080 :
 OoO00Ooooo ( oOOo0O00o )
elif O0oOOo0Oo == 8090 :
 I1iI1I ( )
elif O0oOOo0Oo == 8091 :
 O0O0OOo00Oo ( oOOo0O00o )
elif O0oOOo0Oo == 8092 :
 IIiIi ( oOOo0O00o )
elif O0oOOo0Oo == 8093 :
 IiI1iIIiIi1Ii ( oOOo0O00o )
elif O0oOOo0Oo == 8081 :
 iiIooo0O0O0OO ( )
elif O0oOOo0Oo == 8062 :
 O0O00o0O ( oOOo0O00o )
elif O0oOOo0Oo == 8063 :
 ii1Ii1 ( oOOo0O00o )
elif O0oOOo0Oo == 8050 :
 O0OO ( )
elif O0oOOo0Oo == 8051 :
 o0o0O00oOo ( oOOo0O00o )
elif O0oOOo0Oo == 8052 :
 iI1ii ( oOOo0O00o )
elif O0oOOo0Oo == 8085 :
 iI11I1IiI1 ( )
elif O0oOOo0Oo == 8086 :
 oOo0oOoo0 ( oOOo0O00o )
elif O0oOOo0Oo == 8087 :
 oooOOO0 ( oOOo0O00o )
elif O0oOOo0Oo == 8088 :
 OO00o0 ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 9000 :
 iI1iiiiiii ( )
elif O0oOOo0Oo == 1111 :
 IiiIiIIi1 ( )
elif O0oOOo0Oo == 9001 :
 O00OoO0o ( )
elif O0oOOo0Oo == 9002 :
 OoOoO ( )
elif O0oOOo0Oo == 9003 :
 oOo000O00O ( )
elif O0oOOo0Oo == 9004 :
 World1 ( )
elif O0oOOo0Oo == 9005 :
 World2 ( oOOo0O00o )
elif O0oOOo0Oo == 9006 :
 World3 ( oOOo0O00o )
elif O0oOOo0Oo == 9007 :
 I11OoOO0o000000 ( )
elif O0oOOo0Oo == 9008 :
 O0oooOOoOOO ( oOOo0O00o )
elif O0oOOo0Oo == 9009 :
 OoO0 ( oOOo0O00o )
elif O0oOOo0Oo == 9010 :
 oooiIi11 ( )
elif O0oOOo0Oo == 9011 :
 OOo0oo ( oOOo0O00o )
elif O0oOOo0Oo == 50 :
 ooOoOoo000O0O ( oOOo0O00o )
elif O0oOOo0Oo == 9020 :
 champlist ( )
elif O0oOOo0Oo == 9021 :
 Oo00o ( )
elif O0oOOo0Oo == 9022 :
 iiIi1i ( )
elif O0oOOo0Oo == 9023 :
 o0o0OoOo ( )
elif O0oOOo0Oo == 9024 :
 i11ii111II1II ( oOOo0O00o )
elif O0oOOo0Oo == 9030 :
 iiIiiIi1iiiIi ( oOOo0O00o )
elif O0oOOo0Oo == 9031 :
 IIiII11i1 ( oOOo0O00o )
elif O0oOOo0Oo == 9032 :
 i1IiioOOooo ( oOOo0O00o )
elif O0oOOo0Oo == 9033 :
 IiI11IiIIi ( oOOo0O00o )
elif O0oOOo0Oo == 9034 :
 oo000ii ( )
elif O0oOOo0Oo == 7085 :
 o0Oo0o0 ( oOOo0O00o )
elif O0oOOo0Oo == 7086 :
 iioOOOoOo0oOoo ( oOOo0O00o )
elif O0oOOo0Oo == 7087 :
 O0oo0oOO00o0O0O ( O0o )
elif O0oOOo0Oo == 9666 :
 ooO0O00Oo0o ( oOOo0O00o )
elif O0oOOo0Oo == 10100 : Ii1I11Ii1iI ( )
elif O0oOOo0Oo == 101001 : OOOoO0o ( oOOo0O00o )
elif O0oOOo0Oo == 10105 : iii111iiI11I ( oOOo0O00o )
elif O0oOOo0Oo == 10106 : iII1i ( oOOo0O00o )
elif O0oOOo0Oo == 10104 : I1iIIiiiIII ( oOOo0O00o )
elif O0oOOo0Oo == 10107 : iiioO000oO0oO ( )
elif O0oOOo0Oo == 10103 : oOii1iiiiii ( oOOo0O00o )
elif O0oOOo0Oo == 10108 : ii11 ( oOOo0O00o )
elif O0oOOo0Oo == 10000 : Origin_Menu ( )
elif O0oOOo0Oo == 10001 : IIiiIIi1 ( )
elif O0oOOo0Oo == 10002 : Ooo00OoOOO ( )
elif O0oOOo0Oo == 10003 : iiIII ( )
elif O0oOOo0Oo == 10004 : oOIII111iiIi1 ( oOOo0O00o )
elif O0oOOo0Oo == 10005 : O0O0 ( )
elif O0oOOo0Oo == 10006 : iI1i1Iiii ( oOOo0O00o )
elif O0oOOo0Oo == 10007 : I1iI1II11i1ii ( oOOo0O00o , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 10008 : O0ooOOOo000OOoOO ( )
elif O0oOOo0Oo == 10009 : Ii1IIiii1Ii ( )
elif O0oOOo0Oo == 10010 : ooOO0O0O ( oOOo0O00o )
elif O0oOOo0Oo == 10011 : oO0OooO00Oo ( oOOo0O00o )
elif O0oOOo0Oo == 10012 : I11iiiiI1i ( oOOo0O00o )
elif O0oOOo0Oo == 10113 : GRABG ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 10109 : oOoiIi1I1Iii1 ( oOOo0O00o )
elif O0oOOo0Oo == 10013 : I11iI1i11IiI ( oOOo0O00o )
elif O0oOOo0Oo == 10014 : O0o0O0oOoO ( )
elif O0oOOo0Oo == 10015 : O0O00O ( )
elif O0oOOo0Oo == 10016 : iIIiI1I1i ( oOOo0O00o )
elif O0oOOo0Oo == 10017 : o0O0o ( )
elif O0oOOo0Oo == 10018 : IIIi11Ii ( )
elif O0oOOo0Oo == 10019 : o0OoOoOo0O ( )
elif O0oOOo0Oo == 10020 : OOoOO0oOooo ( )
elif O0oOOo0Oo == 10021 : i1O00oo00o000o ( )
elif O0oOOo0Oo == 10022 : O000O000 ( oOOo0O00o )
elif O0oOOo0Oo == 10023 : i1iIi1iiii1ii ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 10024 : iiiI ( oOOo0O00o )
elif O0oOOo0Oo == 10025 : I1Iiiiiii ( )
elif O0oOOo0Oo == 10026 : OO000oOO0o ( )
elif O0oOOo0Oo == 10027 : O0oO0ooOOo ( )
elif O0oOOo0Oo == 10028 : i1II1111 ( )
elif O0oOOo0Oo == 10029 : o0OO0Oooo ( )
elif O0oOOo0Oo == 423 : Iii1i11 ( oOOo0O00o )
elif O0oOOo0Oo == 426 : OoO00o00 ( oOOo0O00o )
elif O0oOOo0Oo == 10030 : Izle_Films ( )
elif O0oOOo0Oo == 10031 : Latest_Izle_Movies ( )
elif O0oOOo0Oo == 10032 : Izle_Genres ( )
elif O0oOOo0Oo == 10033 : Izle_Pop_Movies ( )
elif O0oOOo0Oo == 10034 : Izle_Boxsets ( )
elif O0oOOo0Oo == 10035 : Izle_Search ( )
elif O0oOOo0Oo == 10036 : Izle_Genres_Movie ( oOOo0O00o )
elif O0oOOo0Oo == 10037 : Izle_Boxset_single ( oOOo0O00o )
elif O0oOOo0Oo == 10038 : Izle_IFRAME ( )
elif O0oOOo0Oo == 10039 : Izle_Boxsets_Next ( oOOo0O00o )
elif O0oOOo0Oo == 10040 : oOOoo ( )
elif O0oOOo0Oo == 10041 : ooo0OOoo ( oOOo0O00o )
elif O0oOOo0Oo == 10042 : I11OoooO ( oOOo0O00o )
elif O0oOOo0Oo == 10043 : oooo ( )
elif O0oOOo0Oo == 10044 : I1O0 ( oOOo0O00o )
elif O0oOOo0Oo == 10045 : oOoo0o ( iIIIiIi )
elif O0oOOo0Oo == 10046 : OooOOOOOOOO00 ( oOOo0O00o )
elif O0oOOo0Oo == 10047 : oO0OOOO00o ( oOOo0O00o )
elif O0oOOo0Oo == 10048 : II111I1i1 ( oOOo0O00o )
elif O0oOOo0Oo == 10049 : IiiIOoO00o0o0oo0o ( oOOo0O00o )
elif O0oOOo0Oo == 10050 : OoO ( )
elif O0oOOo0Oo == 10051 : IIiiiI ( )
elif O0oOOo0Oo == 10052 : ooooO0OOo0o0 ( )
elif O0oOOo0Oo == 10053 : Addon ( oOOo0O00o )
elif O0oOOo0Oo == 10054 : IiiiiI ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 10055 :
 Ooi11 ( "addFavorite" )
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 i1I1iiiI ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0oOooOoOo )
elif O0oOOo0Oo == 10056 :
 Ooi11 ( "rmFavorite" )
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 i11I1Ii1Iiii1 ( iIIIiIi )
elif O0oOOo0Oo == 10057 :
 Ooi11 ( "getFavorites" )
 i11ii11IiI1 ( )
elif O0oOOo0Oo == 10058 : I1iII1IIi1IiI ( )
elif O0oOOo0Oo == 10059 : Donators_Guide ( )
elif O0oOOo0Oo == 10060 : o00o0 ( )
elif O0oOOo0Oo == 10061 : o000ooOo0o0OO ( )
elif O0oOOo0Oo == 10062 : i111iii1I1 ( iIIIiIi , oOOo0O00o , O0o )
elif O0oOOo0Oo == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif O0oOOo0Oo == 10064 : i1I111Ii ( )
elif O0oOOo0Oo == 10065 : OO0OOOOo0000O ( oOOo0O00o )
elif O0oOOo0Oo == 10066 : OoO0Oo00 ( oOOo0O00o )
elif O0oOOo0Oo == 10068 : iiI111 ( oOOo0O00o )
elif O0oOOo0Oo == 10069 : O00oO0 ( oOOo0O00o )
elif O0oOOo0Oo == 10070 : II1IiI1iiI111 ( oOOo0O00o )
elif O0oOOo0Oo == 10071 : Genie_Watch ( )
elif O0oOOo0Oo == 10072 : O00ooooo00 ( )
elif O0oOOo0Oo == 10073 : Oooooo0O00o ( oOOo0O00o )
elif O0oOOo0Oo == 10074 : I1ii1i11i ( oOOo0O00o )
elif O0oOOo0Oo == 10075 : OOoOOo0 ( iiiI1I1iIIIi1 , iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 10076 : O00oo ( oOOo0O00o )
elif O0oOOo0Oo == 10077 : O0o00oo0OO0 ( oOOo0O00o )
elif O0oOOo0Oo == 10078 : I1iiIiiii1111 ( )
elif O0oOOo0Oo == 10079 : Genie_Watch_Tv_Shows ( )
elif O0oOOo0Oo == 10080 : Genie_Watch_Tv_Genre ( oOOo0O00o )
elif O0oOOo0Oo == 10081 : Genie_Watch_TV_PlayRun ( oOOo0O00o )
elif O0oOOo0Oo == 10082 : Genie_Watch_TV_Episodes ( oOOo0O00o , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 10083 : Genie_Watch_Tv_Recent ( oOOo0O00o )
elif O0oOOo0Oo == 10084 : Ii1ii111i1 ( )
elif O0oOOo0Oo == 10085 : oo0OOo0 ( )
elif O0oOOo0Oo == 10086 : O0 ( )
elif O0oOOo0Oo == 20000 : ooO000O ( )
elif O0oOOo0Oo == 20001 : OOoOo0ooOoo ( oOOo0O00o )
elif O0oOOo0Oo == 20002 : o0o0oooO00O0 ( oOOo0O00o )
elif O0oOOo0Oo == 20003 : iiIi1I1II11II ( oOOo0O00o )
elif O0oOOo0Oo == 20004 : Ii1iII1ii1 ( oOOo0O00o )
elif O0oOOo0Oo == 20005 : I11I1i ( oOOo0O00o )
elif O0oOOo0Oo == 21004 : oo0OOOoOo ( )
elif O0oOOo0Oo == 21005 : oOooooooO0o ( oOOo0O00o )
elif O0oOOo0Oo == 21006 : o0Ii11I1iIIi ( oOOo0O00o )
elif O0oOOo0Oo == 21007 : I1III1I11I1 ( oOOo0O00o )
elif O0oOOo0Oo == 21008 : IiI ( oOOo0O00o )
elif O0oOOo0Oo == 21009 : O00oO000O0O ( oOOo0O00o )
elif O0oOOo0Oo == 30000 : i1oo ( )
elif O0oOOo0Oo == 30001 : I11IiIi1iI1ii ( )
elif O0oOOo0Oo == 100121 : Resolve ( oOOo0O00o )
elif O0oOOo0Oo == 30003 : o00Oo0O ( )
elif O0oOOo0Oo == 30004 : II11i1I1iiII1 ( oOOo0O00o )
elif O0oOOo0Oo == 30005 : I1i1i1iIi1iIi ( oOOo0O00o )
elif O0oOOo0Oo == 30006 : iiI1IiIi1i1I ( )
elif O0oOOo0Oo == 30007 : o00000O ( )
elif O0oOOo0Oo == 30008 : IiIIii1 ( oOOo0O00o )
elif O0oOOo0Oo == 30009 : i11ii ( oOOo0O00o )
elif O0oOOo0Oo == 30010 : oOOo00ooO ( oOOo0O00o )
elif O0oOOo0Oo == 30011 : IIIIi1Iii1iIi ( )
elif O0oOOo0Oo == 30012 : II1iIii11II1IIiI ( )
elif O0oOOo0Oo == 30013 : oOoO0O00o ( )
elif O0oOOo0Oo == 30014 : oOO0o00 ( )
elif O0oOOo0Oo == 30015 : o0oO ( oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo )
elif O0oOOo0Oo == 30016 : i1Iii ( oOOo0O00o )
elif O0oOOo0Oo == 30019 : IiOOo0 ( oOOo0O00o )
elif O0oOOo0Oo == 30017 : Ooi1IIii1i ( oOOo0O00o )
elif O0oOOo0Oo == 30018 : o0iii1i ( oOOo0O00o )
elif O0oOOo0Oo == 30030 : oooooO0oO0o ( )
elif O0oOOo0Oo == 30031 : iiiIIiiIi ( )
elif O0oOOo0Oo == 30032 : IIII1iII ( )
elif O0oOOo0Oo == 30033 : O0ooo0Ooo ( )
elif O0oOOo0Oo == 30034 : oOOo0OOOOo0o ( )
elif O0oOOo0Oo == 30035 : I11Iii11i11I1 ( oOOo0O00o )
elif O0oOOo0Oo == 30036 : IiOO0oo00OOo ( oOOo0O00o )
elif O0oOOo0Oo == 30037 : OoOo00oOoO ( oOOo0O00o )
elif O0oOOo0Oo == 30038 : i1i11II1 ( )
elif O0oOOo0Oo == 30039 : oooooo0O000o ( )
elif O0oOOo0Oo == 50000 : I1i ( )
elif O0oOOo0Oo == 50001 : oO0o000oOO ( )
elif O0oOOo0Oo == 50002 : oOOOoo0 ( oOOo0O00o )
elif O0oOOo0Oo == 50003 : Table_Menu ( O0o )
elif O0oOOo0Oo == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif O0oOOo0Oo == 60001 : ii11i1I1i ( )
elif O0oOOo0Oo == 60002 : I1ii111i1ii1 ( iIIIiIi )
elif O0oOOo0Oo == 60003 : IiIooOoOo0O00oo ( oOOo0O00o )
elif O0oOOo0Oo == 600033 : o0oi1I1I1I ( oOOo0O00o )
elif O0oOOo0Oo == 60004 : o0OO0OO000OO ( oOOo0O00o )
elif O0oOOo0Oo == 50004 : iiI ( )
elif O0oOOo0Oo == 50005 : speedtest . runtest ( oOOo0O00o )
elif O0oOOo0Oo == 70001 : oOo0OOoo0o ( )
elif O0oOOo0Oo == 70002 : iIIiI1 ( oOOo0O00o )
elif O0oOOo0Oo == 70003 : Ii11Ii1 ( oOOo0O00o )
elif O0oOOo0Oo == 70004 : IiiIIII1I1i ( oOOo0O00o )
elif O0oOOo0Oo == 70005 : I1IIIIII1 ( oOOo0O00o )
elif O0oOOo0Oo == 70006 : O0oO0O ( )
elif O0oOOo0Oo == 50006 : o0OIiII ( i1 , i1111 )
elif O0oOOo0Oo == 80000 : iI1I ( )
elif O0oOOo0Oo == 80001 : resolvefilmon ( oOOo0O00o )
elif O0oOOo0Oo == 80002 : II111iii ( )
elif O0oOOo0Oo == 80003 : IiIii11ii111 ( iIIIiIi , oOOo0O00o , "None" )
elif O0oOOo0Oo == 80004 : Oo0O00o0O0 ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 80005 : III1i11 ( )
elif O0oOOo0Oo == 80006 : iIIIIiiii1I ( oOOo0O00o )
elif O0oOOo0Oo == 80007 : IIi1iI11IIIi1 ( oOOo0O00o )
elif O0oOOo0Oo == 80008 : o00O0o0oo0oOO0oO ( )
elif O0oOOo0Oo == 80009 : oo0OOo ( )
elif O0oOOo0Oo == 80010 : OOIiI1IIIiI1I1i ( oOOo0O00o )
elif O0oOOo0Oo == 80011 : OoO00O00O0 ( oOOo0O00o )
elif O0oOOo0Oo == 80012 : I11iIIi1Iii ( )
elif O0oOOo0Oo == 90000 : Iii11I1I11I1I1 ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 90001 : tools ( )
elif O0oOOo0Oo == 90002 : oooooOOO000Oo ( )
elif O0oOOo0Oo == 90003 : oOooooo ( oOOo0O00o )
elif O0oOOo0Oo == 90004 : OO00 ( oOOo0O00o )
elif O0oOOo0Oo == 90005 : iI1iII1 ( oOOo0O00o )
elif O0oOOo0Oo == 90006 : oo0OooOoOo ( oOOo0O00o )
elif O0oOOo0Oo == 90007 : iIIii1i1iIiI ( oOOo0O00o )
elif O0oOOo0Oo == 90008 : O0oo ( oOOo0O00o )
elif O0oOOo0Oo == 90009 : iiIi ( oOOo0O00o )
elif O0oOOo0Oo == 90010 : iiIiii1IIIII ( )
elif O0oOOo0Oo == 90020 : iiiIi1Iiii1I ( )
elif O0oOOo0Oo == 90021 : hellyeah2 ( oOOo0O00o )
elif O0oOOo0Oo == 90022 : hellyeah3 ( oOOo0O00o )
elif O0oOOo0Oo == 90023 : i1iIIIIIIiII1 ( )
elif O0oOOo0Oo == 90024 : iI ( oOOo0O00o )
elif O0oOOo0Oo == 90025 : I11i11I1iiII ( oOOo0O00o )
if 30 - 30: OOooOOo . oooOo0oo0oo % oooOo0oo0oo / IIiIiII11i + ooOoO0O00
elif O0oOOo0Oo == 90026 : II11ii1I11 ( )
elif O0oOOo0Oo == 90027 : o0oOoO00 ( iIIIiIi , oOOo0O00o , O0o )
elif O0oOOo0Oo == 90028 : o00OOo0o0O ( oOOo0O00o )
if 61 - 61: ooOoO0O00 % IIiIiII11i * IIiIiII11i . I11i / Ii1I - i1IiiiI1iI
elif O0oOOo0Oo == 900300 : OoOiiI1IIIi ( )
elif O0oOOo0Oo == 900301 : II11IiIi11 ( oOOo0O00o )
elif O0oOOo0Oo == 900302 : oO00ooooO0o ( oOOo0O00o )
elif O0oOOo0Oo == 90030 : I1III1111iIi ( )
elif O0oOOo0Oo == 90031 : IiIi1I1 ( )
elif O0oOOo0Oo == 90032 : IiIIi1 ( oOOo0O00o )
elif O0oOOo0Oo == 90033 : IIIIiii1IIii ( oOOo0O00o )
elif O0oOOo0Oo == 90034 : ooOoOo0 ( oOOo0O00o )
elif O0oOOo0Oo == 90035 : iI1i11 ( oOOo0O00o )
elif O0oOOo0Oo == 90036 : IiIiIIi1 ( oOOo0O00o )
elif O0oOOo0Oo == 90039 : IIi1Iii ( oOOo0O00o )
elif O0oOOo0Oo == 90037 : i1iiiIii11 ( oOOo0O00o )
elif O0oOOo0Oo == 900377 : iIi ( oOOo0O00o )
elif O0oOOo0Oo == 90038 : I1iII11iIII1i1I ( )
if 93 - 93: o0ii1I - ooOoO0O00
elif O0oOOo0Oo == 10090 : o0ii1i ( )
elif O0oOOo0Oo == 10091 : iiii1ii1 ( oOOo0O00o )
elif O0oOOo0Oo == 10092 : OooO0oO0Oo0 ( oOOo0O00o )
elif O0oOOo0Oo == 10093 : o0OO00oO00 ( oOOo0O00o , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 10094 : III11i ( oOOo0O00o , iiiI1I1iIIIi1 )
if 3 - 3: i1i1I1IIii1II + oO0o - IiI1i11I / o0ii1I
elif O0oOOo0Oo == 10095 : ii11i ( )
elif O0oOOo0Oo == 10096 : II1iIII ( oOOo0O00o )
elif O0oOOo0Oo == 10097 : o0ooO0OOO ( oOOo0O00o )
elif O0oOOo0Oo == 10098 : OoOoo00O ( oOOo0O00o )
elif O0oOOo0Oo == 10099 : oo0 ( oOOo0O00o )
if 58 - 58: o0ii1I * Iii
elif O0oOOo0Oo == 10200 : i1i111iI ( )
elif O0oOOo0Oo == 10201 : IIIiiiI ( oOOo0O00o )
elif O0oOOo0Oo == 10202 : oO0oOooooOoO ( oOOo0O00o )
elif O0oOOo0Oo == 10203 : RT4 ( oOOo0O00o )
if 95 - 95: i1i1I1IIii1II
elif O0oOOo0Oo == 90040 : OooooO ( )
elif O0oOOo0Oo == 90041 : ii1I ( oOOo0O00o )
elif O0oOOo0Oo == 90042 : OOO0oO ( oOOo0O00o )
elif O0oOOo0Oo == 90043 : i11oooOo ( oOOo0O00o )
elif O0oOOo0Oo == 90044 : oOO0o00o0Oo0O ( oOOo0O00o )
elif O0oOOo0Oo == 90045 : II1iIii111iII ( )
elif O0oOOo0Oo == 90046 : iIIi1iiII ( oOOo0O00o )
elif O0oOOo0Oo == 90050 : IiI1 ( )
elif O0oOOo0Oo == 90051 : oOOOo ( oOOo0O00o )
elif O0oOOo0Oo == 90052 : OoOoO0OooOOo ( oOOo0O00o )
elif O0oOOo0Oo == 90053 : oooO00Oo ( oOOo0O00o )
elif O0oOOo0Oo == 90054 : I11i11I ( oOOo0O00o )
elif O0oOOo0Oo == 90055 : iIi11i ( )
if 49 - 49: oOo0O0Ooo
elif O0oOOo0Oo == 100001 : Stand_up ( )
if 23 - 23: i1IiiiI1iI
elif O0oOOo0Oo == 100003 : iIIiI1I1i ( oOOo0O00o )
elif O0oOOo0Oo == 100004 : Ooo0oo ( oOOo0O00o )
elif O0oOOo0Oo == 100005 : Resolve ( oOOo0O00o )
elif O0oOOo0Oo == 100008 : Search ( )
elif O0oOOo0Oo == 100007 : IioO0oOOO0Ooo ( oOOo0O00o )
elif O0oOOo0Oo == 100009 : yt . PlayVideo ( oOOo0O00o )
elif O0oOOo0Oo == 100010 : OOOooo ( oOOo0O00o )
elif O0oOOo0Oo == 100100 : ii1i1i1IiII ( iiiI1I1iIIIi1 , oOOo0O00o , Ii1I1iIiIi )
elif O0oOOo0Oo == 100101 : oo0ooOO ( oOOo0O00o , iIIIiIi , IIo0o0O0O00oOOo , Ii1I1iIiIi , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 100102 : i1iIi1II11 ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo )
elif O0oOOo0Oo == 100106 : oO0OO0 ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 100107 : iIII11Ii ( )
elif O0oOOo0Oo == 100108 : I1ii111I ( )
elif O0oOOo0Oo == 100109 : iII1IiI1I11i ( oOOo0O00o )
elif O0oOOo0Oo == 40000 : iIi11I11 ( )
elif O0oOOo0Oo == 40001 : OOooo000OooO ( oOOo0O00o )
elif O0oOOo0Oo == 100110 : I1iI11I1III1 ( )
elif O0oOOo0Oo == 100111 : IiIi1 ( oOOo0O00o )
elif O0oOOo0Oo == 100110 : I1iI11I1III1 ( )
elif O0oOOo0Oo == 100210 : iiiI1ii ( oOOo0O00o )
elif O0oOOo0Oo == 100211 : Iii1i11iiI1 ( )
elif O0oOOo0Oo == 100212 : oOoO0OOO00O ( )
elif O0oOOo0Oo == 100213 : iIiIi1Ii1Ii1IIIi ( )
elif O0oOOo0Oo == 100214 : ooOOO00oOOooO ( )
elif O0oOOo0Oo == 1000111 :
 oO00oOOOO ( oOOo0O00o )
 if 5 - 5: Ii1I % OOooOOo . ii . I11i + Ii
elif O0oOOo0Oo == 1001111 :
 IIIiioo ( iIIIiIi , oOOo0O00o )
 if 54 - 54: i1iIi - o0o00Oo0O + IiI1i11I
elif O0oOOo0Oo == 1002111 :
 oo0O0o0O ( )
 if 34 - 34: o0ii1I - oooOo0oo0oo % IiI1i11I
elif O0oOOo0Oo == 1003111 :
 I1I111i1i1i ( oOOo0O00o , iIIIiIi )
 if 48 - 48: i1i1I1IIii1II - o0o00Oo0O
elif O0oOOo0Oo == 1004111 :
 O0oo0o0ooO00 ( )
 if 17 - 17: iI11I1II1I1I . III1iiIii / i1iIi % Iii + I11i - iI11I1II1I1I
elif O0oOOo0Oo == 1005111 :
 IiIoOo ( oOOo0O00o , iIIIiIi )
elif O0oOOo0Oo == 1100 : from imports . pyramid import pyramid ; pyramid . SKindex ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1101000 : from imports . pyramid import pyramid ; pyramid . getData ( oOOo0O00o , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1102000 : from imports . pyramid import pyramid ; pyramid . getChannelItems ( iIIIiIi , oOOo0O00o , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1103000 : from imports . pyramid import pyramid ; pyramid . getSubChannelItems ( iIIIiIi , oOOo0O00o , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1104000 : from imports . pyramid import pyramid ; pyramid . getFavorites ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1105000 :
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . addFavorite ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo , O0oOooOoOo )
elif O0oOOo0Oo == 1106000 :
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 from imports . pyramid import pyramid ; pyramid . rmFavorite ( iIIIiIi )
elif O0oOOo0Oo == 1107000 : from imports . pyramid import pyramid ; pyramid . addSource ( oOOo0O00o )
elif O0oOOo0Oo == 1108000 : from imports . pyramid import pyramid ; pyramid . rmSource ( iIIIiIi )
elif O0oOOo0Oo == 1109000 : from imports . pyramid import pyramid ; pyramid . download_file ( iIIIiIi , oOOo0O00o )
elif O0oOOo0Oo == 1110000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( )
elif O0oOOo0Oo == 1111000 : from imports . pyramid import pyramid ; pyramid . addSource ( oOOo0O00o )
elif O0oOOo0Oo == 1112000 :
 from imports . pyramid import pyramid
 if 'google' in oOOo0O00o :
  import urlresolver
  OoOOoooOO0O = urlresolver . resolve ( oOOo0O00o )
  ooo00Ooo = xbmcgui . ListItem ( path = OoOOoooOO0O )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo00Ooo )
 elif not oOOo0O00o . startswith ( "plugin://plugin" ) or not any ( x in oOOo0O00o for x in pyramid . g_ignoreSetResolved ) :
  ooo00Ooo = xbmcgui . ListItem ( path = oOOo0O00o )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo00Ooo )
 else :
  print 'Not setting setResolvedUrl'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + oOOo0O00o + ')' )
elif O0oOOo0Oo == 1113000 : from imports . pyramid import pyramid ; pyramid . play_playlist ( iIIIiIi , playlist )
elif O0oOOo0Oo == 1114000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1115000 : from imports . pyramid import pyramid ; pyramid . get_xml_database ( oOOo0O00o , True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1116000 : from imports . pyramid import pyramid ; pyramid . getCommunitySources ( True ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1117000 :
 oOOo0O00o , OOO000O = getRegexParsed ( regexs , oOOo0O00o )
 if oOOo0O00o :
  from imports . pyramid import pyramid ; pyramid . playsetresolved ( oOOo0O00o , iIIIiIi , iiiI1I1iIIIi1 , OOO000O )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid ,Failed to extract regex. - " + "this" + ",4000," + icon + ")" )
elif O0oOOo0Oo == 1118000 :
 try :
  from imports . pyramid import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(ThePyramid,Please [COLOR yellow]install the Youtube Addon[/COLOR] module ,10000," ")" )
 IiI1i11iIIi1Ii1 = youtubedl . single_YD ( oOOo0O00o )
 from imports . pyramid import pyramid ; pyramid . playsetresolved ( IiI1i11iIIi1Ii1 , iIIIiIi , iiiI1I1iIIIi1 )
elif O0oOOo0Oo == 1119000 : from imports . pyramid import pyramid ; pyramid . playsetresolved ( pyramid . urlsolver ( oOOo0O00o ) , iIIIiIi , iiiI1I1iIIIi1 , True )
elif O0oOOo0Oo == 1121000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( '' , iIIIiIi , 'video' )
elif O0oOOo0Oo == 1123000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( oOOo0O00o , iIIIiIi , 'video' )
elif O0oOOo0Oo == 1124000 : from imports . pyramid import pyramid ; pyramid . ytdl_download ( oOOo0O00o , iIIIiIi , 'audio' )
elif O0oOOo0Oo == 1125000 : from imports . pyramid import pyramid ; pyramid . search ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1126000 :
 iIIIiIi = iIIIiIi . split ( ':' )
 from imports . pyramid import pyramid ; pyramid . search ( oOOo0O00o , search_term = iIIIiIi [ 1 ] )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1127000 :
 from imports . pyramid import pyramid ; pyramid . pulsarIMDB = search ( oOOo0O00o )
 xbmc . Player ( ) . play ( pulsarIMDB )
elif O0oOOo0Oo == 1128 : from imports . pyramid import pyramid ; pyramid . SKindex_Joker ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1129 : from imports . pyramid import pyramid ; pyramid . SKindex_Oblivion ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1130000 : from imports . pyramid import pyramid ; pyramid . GetSublinks ( iIIIiIi , oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo )
elif O0oOOo0Oo == 1131000 : from imports . pyramid import pyramid ; pyramid . SKindex_Supremacy ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1132000 : from imports . pyramid import pyramid ; pyramid . SKindex_BAMF ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1133 : from imports . pyramid import pyramid ; pyramid . SKindex_Quicksilver ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1134 : from imports . pyramid import pyramid ; pyramid . SKindex_Silent ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1135000 : from imports . pyramid import pyramid ; pyramid . WizHDMenu ( oOOo0O00o , iiiI1I1iIIIi1 , IIo0o0O0O00oOOo ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1136000 : from imports . pyramid import pyramid ; pyramid . Wiz_Get_url ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1137 : from imports . pyramid import pyramid ; pyramid . scrape ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1138 : from imports . pyramid import pyramid ; pyramid . scrape_link ( iIIIiIi , oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1139 : from imports . pyramid import pyramid ; pyramid . SKindex_deliverance ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1140 : from imports . pyramid import pyramid ; pyramid . SearchChannels ( ) ; pyramid . SetViewThumbnail ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1141 : from imports . pyramid import pyramid ; pyramid . Search_input ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1142000 : from imports . pyramid import pyramid ; pyramid . RESOLVE ( oOOo0O00o )
elif O0oOOo0Oo == 1143 : from imports . pyramid import pyramid ; pyramid . SKindex_TigensWorld ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1144000 : from imports . pyramid import pyramid ; pyramid . queueItem ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1145 : from imports . pyramid import pyramid ; pyramid . SKindex_Ultra ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1146 : from imports . pyramid import pyramid ; pyramid . SKindex_Fido ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1147 : from imports . pyramid import pyramid ; pyramid . SKindex_Rays ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1153000 : from imports . pyramid import pyramid ; pyramid . pluginquerybyJSON ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1154000 : from imports . pyramid import pyramid ; pyramid . get_random ( oOOo0O00o ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif O0oOOo0Oo == 1156 : from imports . pyramid import pyramid ; pyramid . SKindex_Midnight ( ) ; xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
