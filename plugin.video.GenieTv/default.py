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
IiiIII111iI = "3.5.5"
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
  o0OIiII ( 'Change Log 7/7/17 - v3.5.5' , '[COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
  os . makedirs ( ooooooO0oo )
def ii1iII1II ( ) :
 o0OIiII ( 'Change Log 7/7/17 - v3.5.5' , '[COLORsteelblue]Gtv Live Lists now has 24hour catchup on over 30 channels[/COLOR],[CR][COLORsteelblue]Wizard Removed And Replaced With Standalone Addon[/COLOR],[CR][COLORsteelblue]GODS Has A Major Overhaul Merging With Pans Box[/COLOR],[CR][COLORsteelblue]Searches Back Online[/COLOR],[CR][COLORsteelblue]Boss Comedy Back Online[/COLOR],[CR]General Maintence' )
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
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
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
   if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Streams[/COLOR]' , '' , 10025 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  if 96 - 96: ii + i1i1I1IIii1II
  if 44 - 44: i1i1I1IIii1II
  if 20 - 20: Iii + o0ii1I / o0o00Oo0O % iI11I1II1I1I
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzLw==' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiIi1IIiIi + 'zone.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']STREAM CATEGORIES[/COLOR]' , str ( oO0000OOo00 ) , 90002 , iiIi1IIiIi + 'cats.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
 else :
  if 88 - 88: OOooOOo / IIiIiII11i
  if 87 - 87: Ii1I - Ii1I - IiI1i11I + i1i1I1IIii1II
  if oo00 . getSetting ( 'Search' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 9000 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Streams[/COLOR]' , '' , 10025 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  if 82 - 82: i1i1I1IIii1II / iI11I1II1I1I . oOo0O0Ooo . oooOo0oo0oo / I11i
  if 42 - 42: I1ii11iIi11i
  if 19 - 19: i1i1I1IIii1II % Ii1I * iI11I1II1I1I + oOo0O0Ooo
  if 46 - 46: I1ii11iIi11i
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
   if 59 - 59: oOo0O0Ooo * IIiIiII11i . o0o00Oo0O
   if 56 - 56: o0ii1I - IiI1i11I % oOo0O0Ooo - I11i
 I1iI1ii1II ( 'movies' , 'MAIN' )
def Oo00O ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  iI111i1II ( )
 if O0O00Oo == 1 :
  O0ooooo0OOOO0 ( )
 if O0O00Oo == 2 :
  IiiIi1III ( )
 if O0O00Oo == 3 :
  O0Oo ( )
 if O0O00Oo == 4 :
  ii11i11i1 ( )
 if O0O00Oo == 5 :
  Ooo0o00o0o ( )
  if 7 - 7: o0o00Oo0O - I1ii11iIi11i + Ii1I + IIiIiII11i + iI11I1II1I1I
  if 58 - 58: I11i / III1iiIii . OOooOOo / ii + i1IiiiI1iI
def O0OoO0ooOO0o ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   OoOo0oOooOoOO ( )
  if O0O00Oo == 1 :
   oo00ooOoO00 ( )
  if O0O00Oo == 2 :
   o00oOoOo0 ( oOOo0O00o )
  if O0O00Oo == 3 :
   o0O0O0ooo0oOO ( )
  if O0O00Oo == 4 :
   oo000ii ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if O0O00Oo == 5 :
   OoOIiiiii111i1ii ( )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 9001 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 10200 , iiIi1IIiIi + 'rated.png' , Oo00OOOOO , '' )
  if 25 - 25: oooOo0oo0oo - i1iIi / Ii
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , str ( oO0000OOo00 ) , 7061 , iiIi1IIiIi + 'PopcornBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Desi Flix[/COLOR]' , '' , 80005 , iiIi1IIiIi + 'Desi.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiIi1IIiIi + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiIi1IIiIi + 'ClassicMovies.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def iiI1ii11i1 ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 38 - 38: Ii1I - IiI1i11I / o0o00Oo0O . i1IiiiI1iI
 if 45 - 45: i1IiiiI1iI
 if 83 - 83: OOooOOo . ii
 if 58 - 58: Ii + ii % ii / III1iiIii / Ii
 if 62 - 62: oO0o / Ii1I
def ii1O000OOO0OOo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   i1i1I111iIi1 ( )
  if O0O00Oo == 1 :
   oo00O00oO000o ( )
  if O0O00Oo == 2 :
   OOo00OoO ( )
  if O0O00Oo == 3 :
   iIi1 ( )
  if O0O00Oo == 4 :
   i11iiI1111 ( )
  if O0O00Oo == 5 :
   oOoooo000Oo00 ( )
  if O0O00Oo == 6 :
   OOoo ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , str ( oO0000OOo00 ) , 9002 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  if 69 - 69: Iii
  if 95 - 95: i1iIi + Ii * i1IiiiI1iI - ooOoO0O00 * i1IiiiI1iI - iI11I1II1I1I
  if 75 - 75: ii * III1iiIii
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiIi1IIiIi + 'iWatchSeries.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , str ( oO0000OOo00 ) , 10095 , iiIi1IIiIi + 'RD.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , str ( oO0000OOo00 ) , 8064 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiIi1IIiIi + 'TVShowTrailers.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def I1Iiiiiii ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1IIIiI1I1ii1 = '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]'
   if 30 - 30: o0o00Oo0O * ii
   if 38 - 38: III1iiIii - Ii1I . OOooOOo - i1IiiiI1iI . ii
   if 89 - 89: iI11I1II1I1I
   if 21 - 21: Iii % Iii
  oOOoo00O00o = [ I1IIIiI1I1ii1 , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   iiI1 ( )
  if O0O00Oo == 1 :
   iiIIiii ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , iiIIIiIi1IIi , iIIIiIi )
  if O0O00Oo == 2 :
   ii11i ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if O0O00Oo == 3 :
   iiIIiii ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , iiIIIiIi1IIi , iIIIiIi )
 else :
  if 35 - 35: Ii1I * IiI1i11I - oO0o % I11i
  if 87 - 87: OOooOOo * i1IiiiI1iI . Iii
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Murrays Mints[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  if 51 - 51: oooOo0oo0oo % iI11I1II1I1I - ii % i1iIi * iI11I1II1I1I % oO0o
  if 99 - 99: i1i1I1IIii1II * IIiIiII11i * i1IiiiI1iI
  if 92 - 92: I1ii11iIi11i
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  if 40 - 40: OOooOOo / III1iiIii
  if 79 - 79: oO0o - iI11I1II1I1I + o0ii1I - i1IiiiI1iI
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
  if 61 - 61: IIiIiII11i
  if 15 - 15: Ii % oOo0O0Ooo * Iii / i1IiiiI1iI
  if 90 - 90: IiI1i11I
  if 31 - 31: oooOo0oo0oo + o0o00Oo0O
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 87 - 87: i1iIi
def IIIii ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def ii11i ( url ) :
 I1i111I = OooOoooOo ( url )
 O00OooOo00o = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
 ii1I1IIii11 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
 for iIIIiIi , ooO0OO , url in IIi :
  if '247ch' in url :
   IiI11i1IIiiI ( iIIIiIi , url , 10190 , ooO0OO )
  elif '.m3u' in url :
   IiI11i1IIiiI ( iIIIiIi , url , 1019 , ooO0OO )
  elif '.xml' in url :
   IiI11i1IIiiI ( iIIIiIi , url , 1018 , ooO0OO )
  else :
   oOOo000oOoO0 ( iIIIiIi , url , 222 , ooO0OO )
 for iIIIiIi , url , ooO0OO in i1Iii1i1I :
  if '.xml' in url :
   IiI11i1IIiiI ( iIIIiIi , url , 1018 , ooO0OO )
  elif '.m3u' in url :
   IiI11i1IIiiI ( iIIIiIi , url , 1019 , ooO0OO )
  else :
   oOOo000oOoO0 ( iIIIiIi , url , 222 , ooO0OO )
 for iIIIiIi , url , ooO0OO in ii1I1IIii11 :
  oOOo000oOoO0 ( iIIIiIi , url , 8043 , ooO0OO )
def OoOo00o0OO ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def iI1IIIii ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url , ooO0OO in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , ooO0OO )
  if 7 - 7: III1iiIii - Iii / IIiIiII11i * o0ii1I . IiI1i11I * IiI1i11I
def O0O0oOOo0O ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 19 - 19: I11i / i1IiiiI1iI % I11i % IiI1i11I * III1iiIii
def ii1oOoO0o0ooo ( url ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url , i1Ii11II , IioO0oOOO0Ooo , IIo0o0O0O00oOOo , O000OOO in IIi :
  if IioO0oOOO0Ooo == '123' :
   IioO0oOOO0Ooo = iiIi1IIiIi + 'appstreams.png'
  if IIo0o0O0O00oOOo == '123' :
   IIo0o0O0O00oOOo = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   I1I1II1I11 ( iIIIiIi , url , 100010 , IioO0oOOO0Ooo , IIo0o0O0O00oOOo , O000OOO )
  elif 'playlist' in url :
   I1I1II1I11 ( iIIIiIi , url , 100007 , IioO0oOOO0Ooo , IIo0o0O0O00oOOo , O000OOO )
  elif 'watchseries' in url :
   I1I1II1I11 ( iIIIiIi , url , 100100 , IioO0oOOO0Ooo , IIo0o0O0O00oOOo , O000OOO )
  elif not 'http' in url :
   i1i1I ( iIIIiIi , url , 100009 , IioO0oOOO0Ooo , IIo0o0O0O00oOOo , O000OOO , '' )
  else :
   i1i1I ( iIIIiIi , url , 100005 , IioO0oOOO0Ooo , IIo0o0O0O00oOOo , O000OOO , '' )
   if 25 - 25: iI11I1II1I1I + Ii1I + IiI1i11I / IIiIiII11i / Iii
def o0O0Oo00Oo0o ( url ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
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
   i1i1I ( iIIIiIi , url , 100009 , ooO0OO , IIo0o0O0O00oOOo , O000OOO , '' )
  else :
   i1i1I ( iIIIiIi , url , 100005 , ooO0OO , IIo0o0O0O00oOOo , O000OOO , '' )
   if 74 - 74: I1ii11iIi11i / Ii - IIiIiII11i * I11i
def IIi1IIIIi ( url ) :
 if 70 - 70: oooOo0oo0oo / IIiIiII11i - iI11I1II1I1I - IiI1i11I
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IiiiIi1i = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00OooOo00o in IiiiIi1i :
  IioO0oOOO0Ooo = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( O00OooOo00o ) )
  for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
   IioO0oOOO0Ooo = IioO0oOOO0Ooo
  iIIIiIi = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( O00OooOo00o ) )
  for iIIIiIi in iIIIiIi :
   if 'elete' in iIIIiIi :
    pass
   elif 'rivate Vid' in iIIIiIi :
    pass
   else :
    iIIIiIi = ( iIIIiIi ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  i1ii = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( O00OooOo00o ) )
  for i1ii in i1ii :
   i1ii = i1ii
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( O00OooOo00o ) )
  for url in url :
   url = url
  i1i1I ( '[COLORred]' + str ( i1ii ) + '[/COLOR] : ' + str ( iIIIiIi ) , str ( url ) , 100009 , str ( IioO0oOOO0Ooo ) , Oo00OOOOO , '' , '' )
  I1iI1ii1II ( 'movies' , '' )
  if 68 - 68: oooOo0oo0oo * o0o00Oo0O . Iii - IIiIiII11i . i1iIi / IIiIiII11i
  if 47 - 47: ii
  if 4 - 4: oOo0O0Ooo % Iii
  if 10 - 10: III1iiIii . ii - oO0o + III1iiIii - o0o00Oo0O
def o0oO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIIii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIIii1I :
  if '.php' in url :
   I1I1II1I11 ( iIIIiIi , url , 100210 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  else :
   Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
   if 65 - 65: oooOo0oo0oo . i1IiiiI1iI . oO0o . IiI1i11I - oooOo0oo0oo
   if 19 - 19: Ii + IiI1i11I % i1iIi
   if 14 - 14: oO0o . IIiIiII11i . Iii / o0ii1I % Ii1I - i1iIi
def o0oOoO0O ( iconimage , url , extra ) :
 IioO0oOOO0Ooo = ' '
 OoOo000oOo0oo = ' '
 IIo0o0O0O00oOOo = ' '
 oO0O = ' '
 oOO = oO0o0O0Ooo0o ( url )
 IioO0oOOO0Ooo = re . compile ( '<img src="(.+?)">' ) . findall ( oOO )
 for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
  IioO0oOOO0Ooo = IioO0oOOO0Ooo
 iiiIIiIi = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( oOO )
 for IIo0o0O0O00oOOo in iiiIIiIi :
  IIo0o0O0O00oOOo = IIo0o0O0O00oOOo
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( oOO )
 for url , oO0O in IIi :
  oO0O = 'S' + ( oO0O ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  OooOOO ( ( oO0O ) . replace ( '  ' , '' ) , url , 100101 , IioO0oOOO0Ooo , IIo0o0O0O00oOOo , OoOo000oOo0oo , '' )
  I1iI1ii1II ( 'Movies' , 'info' )
  if 48 - 48: iI11I1II1I1I % ooOoO0O00 % IiI1i11I + i1iIi
def Iiii11iIi1 ( url , name , fanart , extra , iconimage ) :
 i1iI11I1II1 = extra
 oO0O = name
 oOO = oO0o0O0Ooo0o ( url )
 IioO0oOOO0Ooo = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( oOO )
 for url , name , ii11II1i in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  ii11II1i = ii11II1i
  OOOO000o0 = name + ' - [COLORred]' + ii11II1i + '[/COLOR]'
  OooOOO ( OOOO000o0 , url , 100102 , IioO0oOOO0Ooo , fanart , 'Aired : ' + ii11II1i , OOOO000o0 )
  if 98 - 98: oO0o . Iii % IIiIiII11i
def O0OoOoO00O ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , name in IIi :
  for ooo00Ooo in o00OO00OoO :
   if ooo00Ooo in oOOo0O00o :
    URL = 'http://www.watchseriesgo.to/link/' + oOOo0O00o
    i1i1I ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  OooOOO ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 96 - 96: oOo0O0Ooo % I1ii11iIi11i . Ii1I + oooOo0oo0oo
  if 42 - 42: IIiIiII11i * IiI1i11I * Ii - oooOo0oo0oo . ii
def oo00o ( url , name ) :
 oo0000Oo00o = name
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  O00oOo ( url , oo0000Oo00o )
 for url in i1Iii1i1I :
  O00oOo ( url , oo0000Oo00o )
 for url in ii1I1IIii11 :
  O00oOo ( url , oo0000Oo00o )
  if 26 - 26: III1iiIii % i1IiiiI1iI % i1i1I1IIii1II % o0ii1I
def O00oOo ( url , season_name ) :
 if 'daclips.in' in url :
  O0oo0ooOOOO ( url , season_name )
 elif 'filehoot.com' in url :
  Ii1ii ( url , season_name )
 elif 'allmyvideos.net' in url :
  iIIIII1iiiiII ( url , season_name )
 elif 'vidspot.net' in url :
  oooO ( url , season_name )
 elif 'vodlocker' in url :
  I111i1I1 ( url , season_name )
 elif 'vidto' in url :
  O0o00OOo00O0O ( url , season_name )
  if 5 - 5: I11i / ii * I11i * o0o00Oo0O . o0ii1I % III1iiIii
  if 43 - 43: I11i
def O0o00OOo00O0O ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO00oOooo0O , iIIIiIi in IIi :
  oOOOo ( OO00oOooo0O , season_name )
  if 68 - 68: i1i1I1IIii1II - Ii1I % o0o00Oo0O % i1IiiiI1iI
  if 11 - 11: o0o00Oo0O / oO0o % oooOo0oo0oo + I11i + iI11I1II1I1I
def iIIIII1iiiiII ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO00oOooo0O , iIIIiIi in IIi :
  oOOOo ( OO00oOooo0O , season_name )
  if 40 - 40: i1iIi - oooOo0oo0oo . o0ii1I * I1ii11iIi11i % i1IiiiI1iI
def oooO ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for OO00oOooo0O , iIIIiIi in IIi :
  oOOOo ( OO00oOooo0O , season_name )
  if 56 - 56: Ii . I11i - oOo0O0Ooo * Iii
def I111i1I1 ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO00oOooo0O in IIi :
  oOOOo ( OO00oOooo0O , season_name )
  if 91 - 91: i1i1I1IIii1II + ii - ooOoO0O00
def O0oo0ooOOOO ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for OO00oOooo0O in IIi :
  oOOOo ( OO00oOooo0O , season_name )
  if 84 - 84: o0ii1I / III1iiIii
def Ii1ii ( url , season_name ) :
 II11iIiIIIiI = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OO00oOooo0O in IIi :
  oOOOo ( OO00oOooo0O , season_name )
  if 86 - 86: OOooOOo * IIiIiII11i - o0o00Oo0O . OOooOOo % iI11I1II1I1I / oooOo0oo0oo
def oOOOo ( Link , season_name ) :
 if 'http:/' in Link :
  IiIIiIIIiIii ( Link )
  if 23 - 23: IiI1i11I + Iii . OOooOOo * oOo0O0Ooo + Ii1I
def I1iIi1iiiIiI ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 III1I1Ii11iI = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in III1I1Ii11iI :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 52 - 52: oooOo0oo0oo - IiI1i11I * i1i1I1IIii1II
def OooOOO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1I11iIiII . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OO0OO0OO = [ ]
  if 61 - 61: ii . i1i1I1IIii1II . ii / I1ii11iIi11i
  if showcontext == 'fav' :
   OO0OO0OO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   OO0OO0OO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1I11iIiII . addContextMenuItems ( OO0OO0OO )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = True )
 return iiIii1I
 if 72 - 72: ooOoO0O00
 if 82 - 82: OOooOOo + ii / Ii * Ii1I . ii
def i1i1I ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1I11iIiII . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OO0OO0OO = [ ]
  OO0OO0OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OO0OO0OO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   OO0OO0OO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1I11iIiII . addContextMenuItems ( OO0OO0OO )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = False )
 return iiIii1I
 if 63 - 63: Ii1I
def i1II ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 2 - 2: IIiIiII11i - oO0o . III1iiIii * IiI1i11I / i1i1I1IIii1II
def OOo0iiIii1IIi ( url ) :
 ii1IiIiI1 = xbmc . Player ( OOOoOo00O ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : ii1IiIiI1 . play ( url ) . strip ( )
 except : pass
 if 59 - 59: oooOo0oo0oo % iI11I1II1I1I . ooOoO0O00 + IIiIiII11i * III1iiIii
def IiIIiIIIiIii ( url ) :
 ii1IiIiI1 = xbmc . Player ( )
 import urlresolver
 try : ii1IiIiI1 . play ( url )
 except : pass
 if 41 - 41: o0ii1I % Ii1I
def oO0o0O0Ooo0o ( url ) :
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
  if 12 - 12: oooOo0oo0oo
  if 69 - 69: ii + oooOo0oo0oo
  if 26 - 26: I1ii11iIi11i + oooOo0oo0oo / oO0o % OOooOOo % Ii1I + IIiIiII11i
def O0ooooo0OOOO0 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   i11I1I1iiI ( )
  if O0O00Oo == 1 :
   I1i1iii1Ii ( )
  if O0O00Oo == 2 :
   iI ( )
  if O0O00Oo == 3 :
   O0O00OOo ( )
  if O0O00Oo == 4 :
   OoOOo ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def O0Oo ( ) :
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
 if 17 - 17: ooOoO0O00
 if 1 - 1: i1iIi
 if 78 - 78: Ii1I + Iii - o0o00Oo0O
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   i1I1iIi1IiI = ( II1I ) . replace ( 'special://home/addons/' , '' )
   o0OIiII ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + i1I1iIi1IiI + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   O0O00Oo = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if O0O00Oo == 0 :
    i1111O0O000OOOo ( II1I )
    OOOOo0o00OO0000 ( )
   elif O0O00Oo == 1 :
    i11ii1Ii1 ( II1I )
  else :
   pass
   if 25 - 25: oooOo0oo0oo
def i11ii1Ii1 ( addon ) :
 i1I1iIi1IiI = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 83 - 83: i1IiiiI1iI
def i1111O0O000OOOo ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 ii111Ii11iii = os . path . join ( IIIII , 'default.py' )
 o00OOoOOO000O0 = open ( ii111Ii11iii , "w+" )
 if 92 - 92: Ii1I / o0o00Oo0O
 o00OOoOOO000O0 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 o00OOoOOO000O0 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 o00OOoOOO000O0 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 80 - 80: I11i - oooOo0oo0oo + ii
 if 98 - 98: oooOo0oo0oo + ooOoO0O00 . oOo0O0Ooo - IIiIiII11i - I11i
 if 24 - 24: I1ii11iIi11i - ooOoO0O00 + Iii
 if 38 - 38: ii / Ii1I . o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
def ooO00O00oOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIII1ii = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 II1i11I = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIIi1I1I11Ii = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url , o0OO , IIo0o0O0O00oOOo , O000OOO in I1 :
  if 'php' in url :
   I1I1II1I11 ( iIIIiIi , url , 90037 , o0OO , IIo0o0O0O00oOOo , O000OOO )
  elif iIIIiIi == 'Search' :
   I1I1II1I11 ( 'Search' , url , 90038 , o0OO , IIo0o0O0O00oOOo , O000OOO )
  else :
   Ii1I1i ( iIIIiIi , url , 222 , o0OO , IIo0o0O0O00oOOo , O000OOO )
 for iIIIiIi , ooO0OO , url , Oo in IIII1ii :
  I1I1II1I11 ( iIIIiIi , url , 90037 , ooO0OO , Oo , '' )
 for iIIIiIi , ooO0OO , url , Oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 90037 , ooO0OO , Oo , '' )
 for iIIIiIi , url , ooO0OO , Oo in i1Iii1i1I :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , Oo , '' )
 for iIIIiIi , url , ooO0OO , Oo in ii1I1IIii11 :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , Oo , '' )
 for iIIIiIi , url , ooO0OO , Oo in II1i11I :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , Oo , '' )
 for iIIIiIi , url , ooO0OO in IiIIi1I1I11Ii :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , '' , '' )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
def iiIiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , ooO0OO , url , Oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 90037 , ooO0OO , Oo , '' )
 for iIIIiIi , url , ooO0OO , Oo in i1Iii1i1I :
  Ii1I1i ( iIIIiIi , url , 222 , ooO0OO , Oo , '' )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
  if 87 - 87: i1iIi - ii + Ii
def O0oooo0OoO0oo ( ) :
 IiiiIi1iI1iI = [ 'serialsearch' , 'moviesearch' ]
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 if OOOOoOO0O == '' :
  pass
 else :
  for ii11I in IiiiIi1iI1iI :
   i1IiIiiiIIIIi = Oo0o0000o0o0 + ii11I + '.php'
   oOO = OooOoooOo ( i1IiIiiiIIIIi )
   if oOO != 'Opened' :
    IIIii1I = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( oOO )
    for iIIIiIi , oOOo0O00o , o0OO , IIo0o0O0O00oOOo , O000OOO in IIIii1I :
     if OOOOoOO0O in iIIIiIi . lower ( ) :
      ooOo00 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for ooo00Ooo in ooOo00 :
       if ooo00Ooo == oOOo0O00o :
        iIIIiIi = '[COLORred]* [/COLOR]' + ( iIIIiIi ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        O00O0 = open ( OOOO0OOoO0O0 , "a" )
        O00O0 . write ( 'item="' + iIIIiIi + '"\n' )
        O00O0 . close
      if 'php' in oOOo0O00o :
       I1I1II1I11 ( iIIIiIi , oOOo0O00o , 90037 , o0OO , IIo0o0O0O00oOOo , O000OOO )
      else :
       Ii1I1i ( iIIIiIi , oOOo0O00o , 222 , o0OO , IIo0o0O0O00oOOo , O000OOO )
       if 19 - 19: i1i1I1IIii1II - IIiIiII11i
   I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
   if 63 - 63: Ii . I11i
def i11ii ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://www.tvcatchup.com/channels/' )
 o0o = OooOoooOo ( 'http://www.djing.com/' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img style="" src="([^"]*)" alt="([^"]*)"/>.+?<br/>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i11I1 = re . compile ( 'title="([^"]*)".+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( o0o )
 for oOOo0O00o , ooO0OO , Ii1iIi111i1i1 , iIIIiIi in IIi :
  oOOo000oOoO0 ( ( '[COLORgold]' + Ii1iIi111i1i1 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + iIIIiIi + '[/COLOR]' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' ) , 'http://www.tvcatchup.com' + oOOo0O00o , 90024 , ooO0OO )
 for I1IIIii , oOOo0O00o , ooO0OO in i11I1 :
  oOOo000oOoO0 ( I1IIIii , 'http://www.tvcatchup.com' + oOOo0O00o , 90024 , ooO0OO )
 for oOOo0O00o , ooO0OO , iIIIiIi in i1Iii1i1I :
  if 'Submit' in iIIIiIi :
   pass
  elif '&lt;' in iIIIiIi :
   pass
  else :
   Ii1I1i ( '[COLORgold]DJing  [/COLOR][COLORwhite]- [COLORsteelblue]' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 90025 , 'http://www.djing.com' + ooO0OO , Oo00OOOOO , '' )
  I1iI1ii1II ( 'movies' , 'MAIN' )
def IIOO0ooOo0OoOo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 87 - 87: i1i1I1IIii1II . oOo0O0Ooo
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiiiI1i ( url )
def i1iIIIiiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OoO00oo00 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 76 - 76: ii + I1ii11iIi11i % III1iiIii . oO0o + IIiIiII11i
def oo00ooOoO00 ( ) :
 if 70 - 70: oOo0O0Ooo / Iii
 if 28 - 28: Ii1I * ii . IIiIiII11i / Ii + i1i1I1IIii1II
 if 38 - 38: III1iiIii . o0ii1I
 if 24 - 24: I11i - I11i + Ii1I + oOo0O0Ooo - i1i1I1IIii1II
 if 12 - 12: IiI1i11I . III1iiIii . OOooOOo / o0o00Oo0O
 if 58 - 58: I11i - IIiIiII11i % i1i1I1IIii1II + i1IiiiI1iI . OOooOOo / III1iiIii
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'yr' in oOOo0O00o :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + oOOo0O00o , 10201 , iiIi1IIiIi + 'rated.png' )
   if 8 - 8: Ii1I . oO0o * Iii + IIiIiII11i % Ii
def i1i1IiIiIi1Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0ooOO , url , iIIIiIi in IIi :
  if 'id' in url :
   IiI11i1IIiiI ( ( '[COLORred]RANK [COLORblue]' + oO0ooOO + '[COLORred] - [COLORblue]' + iIIIiIi + '[/COLOR]' ) , iIIIiIi , 10202 , iiIi1IIiIi + 'rated.png' )
   if 16 - 16: I1ii11iIi11i + i1iIi / I1ii11iIi11i / oO0o % i1i1I1IIii1II % Ii1I
def Ii1II11II1iii ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOO0ooOoO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OO00o = ( url )
 OOOOoOO0O = OO00o . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( OO00o ) . replace ( ' ' , '+' )
 ooO0000o00O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 O0Ooo = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 IIiIIIIii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 iIiI1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIiI1ii = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + OO00o
 oo0OOoOoo0O0O = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iiI11ii1111 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 2 - 2: OOooOOo . ooOoO0O00 . ooOoO0O00 - IIiIiII11i - OOooOOo
 ooOOooo0Oo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oo0O0o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 87 - 87: I1ii11iIi11i / o0o00Oo0O * III1iiIii / I11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( ooO0000o00O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( O0Ooo )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( oO00oOOo0Oo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 I1iiIII = O00O0oOO00O00 ( IIiIIIIii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iIi1I1 = O00O0oOO00O00 ( iIIiI1ii )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O0oOoo0OoO0O = O00O0oOO00O00 ( oo0OOoOoo0O0O )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 oo00IiI1 = O00O0oOO00O00 ( iiI11ii1111 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 87 - 87: I11i % iI11I1II1I1I
 if 100 - 100: i1IiiiI1iI . oOo0O0Ooo * i1IiiiI1iI - oOo0O0Ooo . Iii * o0ii1I
 oO000o = O00O0oOO00O00 ( ooOOooo0Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 o0Oo = O00O0oOO00O00 ( oo0O0o )
 if 57 - 57: oooOo0oo0oo / I1ii11iIi11i
 if 69 - 69: i1i1I1IIii1II - I1ii11iIi11i % III1iiIii
 if 50 - 50: ii
 if 4 - 4: IIiIiII11i . Iii + o0ii1I * i1IiiiI1iI . i1iIi
 if 87 - 87: OOooOOo / oO0o / Ii
 if 74 - 74: i1i1I1IIii1II / Ii1I % I11i
 if 88 - 88: OOooOOo - Ii % I11i * Iii + Ii1I
 if 52 - 52: IIiIiII11i . oOo0O0Ooo + OOooOOo % oO0o
 if 62 - 62: I11i
 if 15 - 15: Iii + o0ii1I . oooOo0oo0oo * oO0o . OOooOOo
 if 18 - 18: ooOoO0O00 % IIiIiII11i + i1IiiiI1iI % o0ii1I
 if 72 - 72: iI11I1II1I1I
 if 45 - 45: I1ii11iIi11i - I11i % i1IiiiI1iI
 if oo00IiI1 != 'Failed' :
  i1IIi1i1Ii1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oo00IiI1 )
  for url , iIIIiIi in i1IIi1i1Ii1 :
   Iiio0Oo0oO = O00O0oOO00O00 ( url )
   iIII1iiIi11 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Iiio0Oo0oO )
   for ooOo0O0O0oOO0 , iIiIIi in iIII1iiIi11 :
    iIiIIi = ( iIiIIi . replace ( '.' , ' ' ) )
    if OOOOoOO0O in iIiIIi . lower ( ) :
     if '.mkv' in ooOo0O0O0oOO0 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + ooOo0O0O0oOO0 , 222 , '' , '' , '' )
     elif '.mp4' in ooOo0O0O0oOO0 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + ooOo0O0O0oOO0 , 222 , '' , '' , '' )
     elif '.avi' in ooOo0O0O0oOO0 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + ooOo0O0O0oOO0 , 222 , '' , '' , '' )
     elif '.wav' in ooOo0O0O0oOO0 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']*' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + ooOo0O0O0oOO0 , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + ooOo0O0O0oOO0 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 14 - 14: I11i / oooOo0oo0oo - iI11I1II1I1I - i1i1I1IIii1II % i1iIi
      I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in i1Iii1i1I :
   if OO00o in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 49 - 49: i1iIi * i1i1I1IIii1II / I11i / I1ii11iIi11i * iI11I1II1I1I
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 57 - 57: OOooOOo - i1i1I1IIii1II / i1iIi % Ii
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for I11oOOooo , iIIIiIi in ii1I1IIii11 :
   if OO00o in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O0Ooo + I11oOOooo ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in II1i11I :
   if OO00o in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 80 - 80: oOo0O0Ooo - Ii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if I1iiIII != 'Failed' :
  oOoooO000O = [ ]
  IiIIi1I1I11Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1iiIII )
  for url , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in IiIIi1I1I11Ii :
   if OO00o in iIIIiIi . lower ( ) :
    if iIIIiIi in oOoooO000O :
     pass
    else :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
     oOoooO000O . append ( iIIIiIi )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if iIi1I1 != 'Failed' :
  III1I11i1iIi = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iIi1I1 )
  for url , ooO0OO , iIIIiIi in III1I11i1iIi :
   if OO00o in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , ooO0OO )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 69 - 69: I1ii11iIi11i * IIiIiII11i * i1iIi . IiI1i11I - Ii1I
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 39 - 39: o0ii1I * oOo0O0Ooo % oO0o . OOooOOo
    if 24 - 24: ooOoO0O00 * iI11I1II1I1I / o0ii1I
    if 78 - 78: Ii + I11i + i1IiiiI1iI / I11i % iI11I1II1I1I % III1iiIii
    if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % i1IiiiI1iI . Ii1I % o0o00Oo0O
    if 47 - 47: I11i
    if 66 - 66: oOo0O0Ooo - III1iiIii
    if 33 - 33: oOo0O0Ooo / oO0o
    if 12 - 12: IIiIiII11i
    if 2 - 2: ooOoO0O00 - oOo0O0Ooo + Iii . IIiIiII11i
    if 25 - 25: i1i1I1IIii1II
    if 34 - 34: OOooOOo . iI11I1II1I1I % o0o00Oo0O
    if 43 - 43: Ii1I - IiI1i11I
    if 70 - 70: IiI1i11I / oooOo0oo0oo % i1iIi - o0ii1I
    if 47 - 47: IiI1i11I
    if 92 - 92: oooOo0oo0oo + OOooOOo % ooOoO0O00
    if 23 - 23: i1IiiiI1iI - oooOo0oo0oo + o0ii1I - OOooOOo * OOooOOo . I1ii11iIi11i
    if 47 - 47: i1i1I1IIii1II % iI11I1II1I1I
    if 11 - 11: oOo0O0Ooo % o0ii1I - oO0o - i1i1I1IIii1II + I11i
 if oO000o != 'Failed' :
  o0O0O0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO000o )
  for url , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in o0O0O0 :
   if OO00o in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 55 - 55: o0o00Oo0O - i1IiiiI1iI
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 58 - 58: OOooOOo - IiI1i11I - ii
    if 96 - 96: iI11I1II1I1I
    if 82 - 82: OOooOOo + o0o00Oo0O - III1iiIii % i1i1I1IIii1II * Ii
    if 15 - 15: I11i
    if 39 - 39: oooOo0oo0oo / Ii1I / oOo0O0Ooo * i1IiiiI1iI
    if 44 - 44: o0o00Oo0O + i1iIi . iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - Iii
    if 83 - 83: III1iiIii * Iii / I1ii11iIi11i
    if 32 - 32: I11i + OOooOOo - ii
    if 39 - 39: ii * oooOo0oo0oo * o0o00Oo0O . Iii . oO0o + i1iIi
    if 9 - 9: OOooOOo + i1i1I1IIii1II % ii + I11i
 ooOO0o = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 51 - 51: I1ii11iIi11i - Ii1I * Iii
 for ii11I in ooOO0o :
  i1IiIiiiIIIIi = oO0 + ii11I + oOoOooOo0o0
  oo00IiI1 = O00O0oOO00O00 ( i1IiIiiiIIIIi )
  if oo00IiI1 != 'Failed' :
   i1IIi1i1Ii1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00IiI1 )
   for url , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in i1IIi1i1Ii1 :
    if OO00o in iIIIiIi . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 12 - 12: iI11I1II1I1I % i1iIi % i1iIi
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 78 - 78: III1iiIii . OOooOOo . Iii
 ooOO0o = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 97 - 97: i1i1I1IIii1II
 if 80 - 80: oOo0O0Ooo . o0ii1I
 for ii11I in ooOO0o :
  i1IiIiiiIIIIi = o0oOO0ooOoO + ii11I
  I1I11ii = O00O0oOO00O00 ( i1IiIiiiIIIIi )
  if I1I11ii != 'Failed' :
   OOoOoo00Oo = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( I1I11ii )
   for I11oOOooo , iIIIiIi in OOoOoo00Oo :
    if OO00o in iIIIiIi . lower ( ) :
     oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o0oOO0ooOoO + ii11I + I11oOOooo ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: oO0o . IIiIiII11i % OOooOOo % o0ii1I
def i11iiI1111 ( ) :
 IiI11i1IIiiI ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 IiI11i1IIiiI ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 IiI11i1IIiiI ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 IiI11i1IIiiI ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 87 - 87: iI11I1II1I1I . ii * OOooOOo
def OOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oO0O , o0ooOo00O , ii11II1i , Ii1i1I1 in IIi :
  IiI11i1IIiiI ( ( '[COLORblue]' + iIIIiIi + '[/COLOR] [COLORred]Season[/COLOR]-' + oO0O + ' [COLORred]Returns [/COLOR]- ' + Ii1i1I1 + ' ' + ii11II1i ) , iIIIiIi , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 97 - 97: i1IiiiI1iI . i1iIi - i1IiiiI1iI + oOo0O0Ooo * IIiIiII11i
def I111Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oO0O , o0ooOo00O in IIi :
  IiI11i1IIiiI ( ( '[COLORblue]' + iIIIiIi + '[/COLOR] [COLORred]Season[/COLOR]-' + oO0O + ' [COLORred] Status Unknown[/COLOR] ' ) , iIIIiIi , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 34 - 34: I11i / IiI1i11I % o0o00Oo0O . oO0o . ooOoO0O00
def iiO0O0o0oO0O00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oO0O , o0ooOo00O , ii11II1i in IIi :
  IiI11i1IIiiI ( ( '[COLORblue]' + iIIIiIi + ' [COLORred] Cancelled On[/COLOR] ' + ii11II1i ) , iIIIiIi , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 70 - 70: i1IiiiI1iI + i1i1I1IIii1II
def o00ooo0 ( url ) :
 OO00o = ( url )
 OOOOoOO0O = OO00o . lower ( )
 if 39 - 39: i1iIi . IIiIiII11i
 if 45 - 45: i1i1I1IIii1II * OOooOOo / iI11I1II1I1I
 ooOo0O0O0oOO0 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( OO00o ) . replace ( ' ' , '+' )
 ooO0000o00O = 'http://onlinemovies.tube/?s=' + ( OO00o ) . replace ( ' ' , '+' )
 O0Ooo = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 iIiI1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 77 - 77: i1IiiiI1iI - Iii
 oo0OOoOoo0O0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iiI11ii1111 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 iiI1iI1I = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 27 - 27: Ii1I * i1IiiiI1iI - oO0o + o0ii1I * o0ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 55 - 55: i1iIi
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 82 - 82: i1IiiiI1iI - oooOo0oo0oo + oO0o
 if 64 - 64: I11i . o0o00Oo0O * o0ii1I + ii - I1ii11iIi11i . ii
 oo0o = O00O0oOO00O00 ( ooOo0O0O0oOO0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( ooO0000o00O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( O0Ooo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( oO00oOOo0Oo )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 I1I11ii = O00O0oOO00O00 ( iIiI1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 70 - 70: I1ii11iIi11i - i1i1I1IIii1II . iI11I1II1I1I % Iii / OOooOOo - o0o00Oo0O
 if 55 - 55: IiI1i11I - oO0o
 O0oOoo0OoO0O = O00O0oOO00O00 ( oo0OOoOoo0O0O )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 oo00IiI1 = O00O0oOO00O00 ( iiI11ii1111 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 o0i1I11iI1iiI = O00O0oOO00O00 ( iiI1iI1I )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 48 - 48: Iii . ii . oOo0O0Ooo . OOooOOo % Ii1I / IiI1i11I
 if oo00IiI1 != 'Failed' :
  i1IIi1i1Ii1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oo00IiI1 )
  for url , iIIIiIi in i1IIi1i1Ii1 :
   Iiio0Oo0oO = O00O0oOO00O00 ( url )
   iIII1iiIi11 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Iiio0Oo0oO )
   for ooOo0O0O0oOO0 , iIiIIi in iIII1iiIi11 :
    if OOOOoOO0O in iIiIIi . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , url + ooOo0O0O0oOO0 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 11 - 11: ooOoO0O00 % oO0o % IiI1i11I
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if O0oOoo0OoO0O != 'Failed' :
  O0Oo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0oOoo0OoO0O )
  for url , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in O0Oo0 :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 80 - 80: oOo0O0Ooo - iI11I1II1I1I . oooOo0oo0oo + oO0o - i1IiiiI1iI
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 5 - 5: IiI1i11I
    if 62 - 62: OOooOOo . ii . oooOo0oo0oo . oO0o * IiI1i11I
    if 78 - 78: i1i1I1IIii1II / oO0o - i1i1I1IIii1II * ii . OOooOOo
    if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
    if 37 - 37: ooOoO0O00 - oooOo0oo0oo % ii / oooOo0oo0oo % i1iIi
    if 48 - 48: Ii % i1i1I1IIii1II
    if 29 - 29: IiI1i11I + Ii % Iii
    if 93 - 93: OOooOOo % iI11I1II1I1I
    if 90 - 90: oOo0O0Ooo - oooOo0oo0oo / o0ii1I / o0o00Oo0O / Iii
    if 87 - 87: OOooOOo / III1iiIii + iI11I1II1I1I
    if 93 - 93: iI11I1II1I1I + i1i1I1IIii1II % i1iIi
 if o0i1I11iI1iiI != 'Failed' :
  iii1IiI1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0i1I11iI1iiI )
  for url , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in iii1IiI1I1 :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , iiIIIiIi1IIi )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 64 - 64: i1iIi / o0o00Oo0O * OOooOOo * i1iIi
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  O00oo = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , ooO0OO , iIIIiIi , OoOo0oO0o in i1Iii1i1I :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    if 'season' in OoOo0oO0o :
     IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , ooO0OO , ooO0OO , '' )
    if 'episodes' in OoOo0oO0o :
     IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , ooO0OO , ooO0OO , '' )
  for url in O00oo :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 54 - 54: IiI1i11I % ooOoO0O00 + Ii1I
   I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  IIII1ii = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( oo0o )
  for url , iIIIiIi , ooO0OO in IIII1ii :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( iIIIiIi ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , ooO0OO , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 2 - 2: iI11I1II1I1I * i1i1I1IIii1II / OOooOOo . Iii / III1iiIii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 75 - 75: OOooOOo
    if 78 - 78: o0ii1I + OOooOOo + III1iiIii - III1iiIii . Ii / oO0o
    if 27 - 27: o0ii1I - o0o00Oo0O % Iii * i1IiiiI1iI . III1iiIii % iI11I1II1I1I
    if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % i1iIi
    if 24 - 24: OOooOOo
    if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + oooOo0oo0oo
    if 28 - 28: oOo0O0Ooo
    if 49 - 49: Iii . I11i % i1i1I1IIii1II / o0ii1I
    if 95 - 95: o0o00Oo0O * OOooOOo * III1iiIii . i1iIi / iI11I1II1I1I
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for iIIIiIi in ii1I1IIii11 :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( O0Ooo + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 28 - 28: III1iiIii + i1i1I1IIii1II - i1iIi / iI11I1II1I1I - oOo0O0Ooo
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for iIIIiIi in II1i11I :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( oO00oOOo0Oo + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 45 - 45: o0o00Oo0O / ooOoO0O00 * i1i1I1IIii1II * oO0o
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if I1I11ii != 'Failed' :
  OOoOoo00Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1I11ii )
  for url , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in OOoOoo00Oo :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 35 - 35: Ii1I / IiI1i11I % oOo0O0Ooo + iI11I1II1I1I
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 79 - 79: OOooOOo / i1iIi
 oOo00o = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for ii11I in oOo00o :
  i1IiIiiiIIIIi = oO0 + ii11I + oOoOooOo0o0
  oO000o = O00O0oOO00O00 ( i1IiIiiiIIIIi )
  if oO000o != 'Failed' :
   o0O0O0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO000o )
   for iIIIiIi , O000OOO , url , ooO0OO , IIo0o0O0O00oOOo , i1Ii11II in o0O0O0 :
    if OOOOoOO0O in iIIIiIi . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , url , i1Ii11II , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 98 - 98: oooOo0oo0oo % ooOoO0O00 . oOo0O0Ooo . IIiIiII11i . Ii1I / Ii
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 32 - 32: I11i + oOo0O0Ooo . i1IiiiI1iI
     if 41 - 41: OOooOOo . Ii / Iii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: OOooOOo % IIiIiII11i
def OoO0O000 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( iIIIiIi ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + oOOo0O00o , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + oOOo0O00o )
def II1Ii ( url ) :
 Ii1iiII1i = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( Ii1iiII1i )
 sys . exit ( 1 )
 if 52 - 52: i1i1I1IIii1II / i1IiiiI1iI
def o0Oi11i1I ( ) :
 if 100 - 100: IiI1i11I / oO0o * iI11I1II1I1I * o0o00Oo0O - ooOoO0O00
 if 48 - 48: o0o00Oo0O * o0ii1I * oO0o . oO0o * Iii - o0ii1I
 if 14 - 14: Ii1I + Ii
 if 83 - 83: Ii1I / Ii + IIiIiII11i . IiI1i11I * oooOo0oo0oo + III1iiIii
 if 42 - 42: ooOoO0O00 % IIiIiII11i . i1iIi
 if 7 - 7: Ii1I - i1i1I1IIii1II * oooOo0oo0oo + I11i . Ii1I
 if 85 - 85: o0o00Oo0O
 if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * o0ii1I
 if 19 - 19: o0ii1I
 if 55 - 55: oooOo0oo0oo % oooOo0oo0oo / o0o00Oo0O % IiI1i11I - I11i . I1ii11iIi11i
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
 IiI11i1IIiiI ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 IiI11i1IIiiI ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 IiI11i1IIiiI ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
def IIiI11I1I1i1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , oooo in IIi :
  IiI11i1IIiiI ( ( iIIIiIi + ' - ' + oooo ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 70 - 70: o0ii1I . Ii % o0ii1I . o0o00Oo0O - iI11I1II1I1I
def i111i1iIi1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 95 - 95: ii + Iii - Ii1I / Ii1I . ooOoO0O00 . ii
def I1iiI1II ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  IiI11i1IIiiI ( iIIIiIi , url , 90054 , ooO0OO )
 for url in next :
  IiI11i1IIiiI ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 44 - 44: I1ii11iIi11i / ooOoO0O00 + iI11I1II1I1I / iI11I1II1I1I * iI11I1II1I1I . o0ii1I
def Ooii1IIi1ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for ooO0OO , oooo , url , iIIIiIi , oo0OoOOooO in IIi :
  I1I1II1I11 ( oooo + ' - ' + iIIIiIi + ' - ' + oo0OoOOooO , url , 90044 , ooO0OO , ooO0OO , '' )
 for ooO0OO , iIIIiIi , url in i1Iii1i1I :
  IiI11i1IIiiI ( iIIIiIi , url , 90044 , ooO0OO , ooO0OO , '' )
 for url in next :
  IiI11i1IIiiI ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 60 - 60: i1IiiiI1iI
def oOO0o00o0Oo0O ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIi1iiII = 'http://onlinemovies.tube/?s=' + ( OO00o ) . replace ( ' ' , '+' )
 OOOOoOO0O = iIIi1iiII . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOOoOO0O )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi , OoOo0oO0o in IIi :
  if 'season' in OoOo0oO0o :
   IiI11i1IIiiI ( iIIIiIi , oOOo0O00o , 90054 , ooO0OO , ooO0OO , '' )
  if 'episodes' in OoOo0oO0o :
   IiI11i1IIiiI ( iIIIiIi , oOOo0O00o , 90044 , ooO0OO , ooO0OO , '' )
 for oOOo0O00o in next :
  IiI11i1IIiiI ( 'NEXT' , oOOo0O00o , 90053 , iiIi1IIiIi + 'Next.png' )
  if 14 - 14: o0o00Oo0O
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
 IiI11i1IIiiI ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 IiI11i1IIiiI ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 IiI11i1IIiiI ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 IiI11i1IIiiI ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 10 - 10: IiI1i11I . ooOoO0O00 + o0ii1I
def oOOoOOO0oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , oooo in IIi :
  if 'genre' in url :
   IiI11i1IIiiI ( ( iIIIiIi + ' - ' + oooo ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 87 - 87: i1iIi / OOooOOo % I11i * i1i1I1IIii1II
def oOOOoo0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'release' in url :
   IiI11i1IIiiI ( iIIIiIi , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 44 - 44: o0o00Oo0O % ooOoO0O00
def IiIIiii1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , ooooo0Oo0 , url , O000OOO in IIi :
  I1I1II1I11 ( iIIIiIi + ' ' + ooooo0Oo0 , url , 90044 , ooO0OO , ooO0OO , O000OOO )
 for ooO0OO , iIIIiIi , OoOo0oO0o , url , o0I1IIIi11ii11 , O000OOO in i1Iii1i1I :
  if 'movies' in OoOo0oO0o :
   I1I1II1I11 ( iIIIiIi + ' - ' + o0I1IIIi11ii11 , url , 90044 , ooO0OO , ooO0OO , O000OOO )
 for url in next :
  IiI11i1IIiiI ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 53 - 53: i1IiiiI1iI * III1iiIii / iI11I1II1I1I / oOo0O0Ooo % Ii1I
def IIii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  oOOO0 ( 'http:' + url )
  if 32 - 32: i1iIi % i1IiiiI1iI * I1ii11iIi11i
def oOOO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  oOOo000oOoO0 ( ( iIIIiIi ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def O0O000oOo0O ( ) :
 if 82 - 82: III1iiIii
 if 86 - 86: I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
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
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIi1iiII = 'http://onlinemovies.tube/?s=' + ( OO00o ) . replace ( ' ' , '+' )
 OOOOoOO0O = iIIi1iiII . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOOoOO0O )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi , O00ooooo00 in IIi :
  if 'movies' in O00ooooo00 :
   IiI11i1IIiiI ( O00ooooo00 + '-' + iIIIiIi , oOOo0O00o , 90044 , ooO0OO )
 for oOOo0O00o in next :
  IiIIiii1I ( oOOo0O00o )
  if 94 - 94: Iii - IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + Ii1I * Ii1I
def o0O0O0ooo0oOO ( ) :
 IiI11i1IIiiI ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , oOOo0O00o , 80006 , iiIi1IIiIi + 'Desi.png' )
def I1iiIiiii1111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  oOOo000oOoO0 ( iIIIiIi , url , 80007 , ooO0OO )
 for url , ooO0OO , iIIIiIi in IIi :
  IiI11i1IIiiI ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def I1ii1i11i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  I11iiiiI1i ( url )
def Oooooo0O00o ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIi1iiII = 'http://www.join4films.com/?s=' + ( OO00o ) . replace ( ' ' , '+' ) + '&search_type=1'
 OOOOoOO0O = iIIi1iiII . lower ( )
 I1iiIiiii1111 ( OOOOoOO0O )
 if 36 - 36: OOooOOo + III1iiIii * o0o00Oo0O . ii * ii
 if 51 - 51: Ii1I * Ii1I
 if 98 - 98: oO0o - o0ii1I . III1iiIii % Ii
 if 69 - 69: Ii1I + IiI1i11I * o0o00Oo0O . oooOo0oo0oo % OOooOOo
 if 96 - 96: i1iIi . i1iIi - Iii / Iii
 if 96 - 96: Ii / oOo0O0Ooo - o0o00Oo0O . i1iIi
 if 39 - 39: i1iIi / o0o00Oo0O * III1iiIii
 if 17 - 17: o0ii1I / iI11I1II1I1I - oO0o + oOo0O0Ooo % oooOo0oo0oo
 if 14 - 14: I11i % III1iiIii + Ii1I + oO0o
 if 76 - 76: oO0o - Ii + OOooOOo + oooOo0oo0oo / ii
 if 50 - 50: IIiIiII11i - i1IiiiI1iI + iI11I1II1I1I + iI11I1II1I1I
 if 91 - 91: IIiIiII11i - o0o00Oo0O . iI11I1II1I1I . o0o00Oo0O + Ii1I - IIiIiII11i
 if 26 - 26: I11i
 if 12 - 12: ii / o0o00Oo0O + IIiIiII11i * Ii1I
 if 46 - 46: IIiIiII11i - III1iiIii * ii / i1i1I1IIii1II % III1iiIii
 if 11 - 11: iI11I1II1I1I . OOooOOo / III1iiIii % i1iIi
 if 61 - 61: i1iIi - oooOo0oo0oo + oooOo0oo0oo
def iiiIiIIII1iiIIi ( ) :
 I1I1II1I11 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 17 - 17: Iii
def oOoO0ooO0000 ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIi1iiII = 'http://imoviemax.se/?s=' + ( OO00o ) . replace ( ' ' , '+' )
 OOOOoOO0O = iIIi1iiII . lower ( )
 OOOOO ( OOOOoOO0O )
def O0OOoo0 ( url ) :
 i1I1iii = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , i1IIOo0 in IIi :
  if iIIIiIi in i1I1iii :
   pass
  else :
   I1I1II1I11 ( iIIIiIi + ' - ' + i1IIOo0 + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   i1I1iii . append ( iIIIiIi )
   if 96 - 96: Iii % o0ii1I % i1i1I1IIii1II * Iii / oooOo0oo0oo
def iiI1iiii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , i1iiIIiiiII in IIi :
  I1I1II1I11 ( iIIIiIi + ' - Views:' + i1iiIIiiiII , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 5 - 5: ii / I11i % Iii % oO0o * IiI1i11I + iI11I1II1I1I
  if 11 - 11: i1IiiiI1iI % Ii % i1i1I1IIii1II . III1iiIii
def OOOOO ( url ) :
 oOO0o = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  I1I1II1I11 ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  I1I1II1I11 ( iIIIiIi , url , 10075 , ooO0OO , ooO0OO , '' )
  oOO0o . append ( iIIIiIi )
  if 65 - 65: IiI1i11I . oO0o + o0ii1I
def IIiI1I ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for oOo0OOO00Oo , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  i1ii1ii1II1 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + i1ii1ii1II1
  IIIiI1Ii11 = ( oOo0OOO00Oo ) . replace ( 'play-' , 'Server ' )
  Ii1I1i ( IIIiI1Ii11 , i1ii1ii1II1 , 10076 , img , img , '' )
  if 1 - 1: i1IiiiI1iI - Iii
def i1I111Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for ooO0000o00O in IIi :
  if '=m' in ooO0000o00O :
   i11i1i ( ooO0000o00O )
  elif 'php' in ooO0000o00O :
   i1I111Ii ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( ooO0000o00O )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for O0Ooo in IIi :
    i11i1i ( ooO0000o00O )
    if 10 - 10: o0ii1I - Ii . Ii1I % ooOoO0O00
    if 78 - 78: iI11I1II1I1I * I1ii11iIi11i . I1ii11iIi11i - oooOo0oo0oo . iI11I1II1I1I
    if 30 - 30: i1iIi + i1iIi % III1iiIii - I11i - Ii1I
def i111IiiI1Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OooOOOOOo = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ii11II1i , i1I11ii in OooOOOOOo :
  print 'there ><><><><><><><><><><><><'
  ii11II1i = ii11II1i
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1I11ii ) )
  for iIIIiIi , o0ooO00O0O in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + ii11II1i + '[/COLOR] - ' + iIIIiIi + ' - [COLOR' + ooOoOoo0O + ']' + o0ooO00O0O + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 O00OooOo00o = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ii11II1i , iiiI1iI1 in O00OooOo00o :
  print 'there ><><><><><><><><><><><><'
  ii11II1i = ii11II1i
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iiiI1iI1 ) )
  for iIIIiIi , o0ooO00O0O in IIi :
   print 'here <><><><><><><><><><><><>'
   I1I1II1I11 ( '[COLORred]' + ii11II1i + '[/COLOR] - ' + iIIIiIi + ' - [COLOR' + ooOoOoo0O + ']' + o0ooO00O0O + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 15 - 15: III1iiIii . ooOoO0O00 * OOooOOo % iI11I1II1I1I
   if 35 - 35: Ii1I + i1IiiiI1iI - OOooOOo % i1i1I1IIii1II % I11i % OOooOOo
   if 45 - 45: oOo0O0Ooo * oooOo0oo0oo % oO0o
def OOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00OooOo00o = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00OooOo00o in O00OooOo00o :
  iIIIiIi = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
  for iIIIiIi in iIIIiIi :
   iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00OooOo00o ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  IioO0oOOO0Ooo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
  for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
   IioO0oOOO0Ooo = 'http:' + IioO0oOOO0Ooo
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , '' , '' )
  if 24 - 24: i1iIi - Iii * i1i1I1IIii1II
  if 87 - 87: o0ii1I - Ii1I % Ii1I . i1i1I1IIii1II / Ii1I
  if 6 - 6: OOooOOo / iI11I1II1I1I * ii * Ii
  if 79 - 79: III1iiIii % oO0o
def oo000ii ( url ) :
 if 81 - 81: Ii + Ii * oO0o + III1iiIii
 iiiiiI = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0000o00O , ooO0OO , iIIIiIi , IiiIi in IIi :
  iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( ooO0000o00O )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for III1I1Ii11iI , OoOo000oOo0oo in i1Iii1i1I :
   i1ii1I = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( OoOo000oOo0oo ) )
   for O000OOO in i1ii1I :
    if iIIIiIi in iiiiiI :
     pass
    else :
     Ii1I1i ( iIIIiIi , III1I1Ii11iI , 8043 , ooO0OO , ooO0OO , O000OOO )
     I1iI1ii1II ( 'movies' , 'INFO' )
     iiiiiI . append ( iIIIiIi )
     if 50 - 50: iI11I1II1I1I + OOooOOo . OOooOOo + ooOoO0O00 + III1iiIii
     if 27 - 27: ooOoO0O00 % o0ii1I - oO0o / i1i1I1IIii1II . i1iIi / I1ii11iIi11i
def OO0OoO0o ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , iiIIIiIi1IIi , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
  I1I1II1I11 ( iIIIiIi , url , 10065 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , O000OOO )
 I1iI1ii1II ( 'movies' , 'INFO' )
 if 98 - 98: i1IiiiI1iI
def IIIIIIi1IiIi ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIi1iiII = 'https://www.youtube.com/results?search_query=' + ( OO00o ) . replace ( ' ' , '+' )
 OOOOoOO0O = iIIi1iiII . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOOoOO0O )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in next :
  oOOo0O00o = 'https://www.youtube.com' + oOOo0O00o
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , oOOo0O00o , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for ooO0OO , oOOo0O00o , iIIIiIi , III1i , OoOo000oOo0oo in IIi :
  OOO00 . append ( iIIIiIi )
  I1iI1ii1II ( 'tvshows' , 'INFO' )
  IioO0oOOO0Ooo = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IioO0oOOO0Ooo
  oOOo0O00o = 'http://www.youtube.com' + oOOo0O00o
  Ii1I1i ( '[COLORred]' + III1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , IioO0oOOO0Ooo , OoOo000oOo0oo )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for ooO0OO , oOOo0O00o , iIIIiIi , III1i in IIi :
   print 'im doing it'
   I1iI1ii1II ( 'tvshows' , 'INFO' )
   IioO0oOOO0Ooo = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
   oOOo0O00o = 'http://www.youtube.com' + oOOo0O00o
   if '&' in oOOo0O00o :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( oOOo0O00o )
    O00OooOo00o = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for O00OooOo00o in O00OooOo00o :
     iIIIiIi = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
     for iIIIiIi in iIIIiIi :
      iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oOOo0O00o = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00OooOo00o ) )
     for oOOo0O00o in oOOo0O00o :
      oOOo0O00o = 'https://www.youtube.com/w' + oOOo0O00o
     IioO0oOOO0Ooo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
     for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
      IioO0oOOO0Ooo = 'http:' + IioO0oOOO0Ooo
     Ii1I1i ( '[COLORred]' + III1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , Oo00OOOOO , '' )
   elif iIIIiIi in OOO00 :
    pass
   elif 'user' in oOOo0O00o or 'elete' in iIIIiIi :
    pass
   elif 'hannel' in oOOo0O00o :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oOOo0O00o
    II11iIiIIIiI = OooOoooOo ( oOOo0O00o )
    o0Oo0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for ooO0OO , oOOo0O00o , iIIIiIi in o0Oo0 :
     if 'outube' in oOOo0O00o or 'list' in oOOo0O00o :
      pass
     elif 'atch' in oOOo0O00o :
      oOOo0O00o = ( oOOo0O00o ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + III1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ooO0OO , 'http:' + ooO0OO , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + III1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , IioO0oOOO0Ooo , '' )
    if 35 - 35: Ii - i1i1I1IIii1II % Ii
def II111I1Iii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for ooO0OO , url , iIIIiIi , III1i , OoOo000oOo0oo in IIi :
  OOO00 . append ( iIIIiIi )
  I1iI1ii1II ( 'tvshows' , 'INFO' )
  IioO0oOOO0Ooo = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IioO0oOOO0Ooo
  url = 'http://www.youtube.com' + url
  Ii1I1i ( '[COLORred]' + III1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , IioO0oOOO0Ooo , OoOo000oOo0oo )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for ooO0OO , url , iIIIiIi , III1i in IIi :
   I1iI1ii1II ( 'tvshows' , 'INFO' )
   IioO0oOOO0Ooo = 'http:' + ( ooO0OO ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    O00OooOo00o = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for O00OooOo00o in O00OooOo00o :
     iIIIiIi = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
     for iIIIiIi in iIIIiIi :
      iIIIiIi = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00OooOo00o ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     IioO0oOOO0Ooo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00OooOo00o ) )
     for IioO0oOOO0Ooo in IioO0oOOO0Ooo :
      IioO0oOOO0Ooo = 'http:' + IioO0oOOO0Ooo
     Ii1I1i ( '[COLORred]' + III1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , Oo00OOOOO , '' )
   elif iIIIiIi in OOO00 :
    pass
   elif 'user' in url or 'elete' in iIIIiIi :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    o0Oo0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for ooO0OO , url , iIIIiIi in o0Oo0 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      Ii1I1i ( '[COLORred]' + III1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ooO0OO , 'http:' + ooO0OO , '' )
     else :
      pass
   else :
    Ii1I1i ( '[COLORred]' + III1i + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo , IioO0oOOO0Ooo , '' )
    if 84 - 84: I1ii11iIi11i % IiI1i11I % ii + oooOo0oo0oo % Ii
    if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * i1i1I1IIii1II . Iii / ooOoO0O00
    if 50 - 50: i1IiiiI1iI / ooOoO0O00 % ii
def oOOOOO0Ooooo ( ) :
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 57 - 57: o0ii1I - ii
def OOoOO0O0o0 ( ) :
 ivuesetup . iVueInt ( )
 if 44 - 44: oooOo0oo0oo / I1ii11iIi11i + III1iiIii % IIiIiII11i / oO0o + Ii
def ii11Iiii ( ) :
 II1 ( )
 return
 if 60 - 60: IIiIiII11i + ooOoO0O00 . o0o00Oo0O + oOo0O0Ooo
def II1 ( ) :
 if 80 - 80: i1i1I1IIii1II % i1i1I1IIii1II % o0o00Oo0O - Ii . IiI1i11I / o0o00Oo0O
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 IiIi1Ii = II1I . getSetting ( id = 'User' )
 iiIIiI11II1 = II1I . getSetting ( id = 'Pass' )
 oooOo = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 oOoO0Oo0 = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 i11i11i = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 iiI1iI = "http://piesustv.net:8000/get.php?username=" + IiIi1Ii + "&password=" + iiIIiI11II1 + "&type=m3u_plus&output=ts"
 Ooo00O0 = "http://piesustv.net:8000/xmltv.php?username=" + IiIi1Ii + "&password=" + iiIIiI11II1 + "&type=m3u_plus&output=ts"
 if 70 - 70: oOo0O0Ooo - i1iIi - oO0o - OOooOOo . Ii % ooOoO0O00
 xbmc . executeJSONRPC ( oooOo )
 xbmc . executeJSONRPC ( oOoO0Oo0 )
 xbmc . executeJSONRPC ( i11i11i )
 if 1 - 1: i1i1I1IIii1II / ooOoO0O00
 O0oo0 = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 O0oo0 . setSetting ( id = 'm3uUrl' , value = iiI1iI )
 O0oo0 . setSetting ( id = 'epgUrl' , value = Ooo00O0 )
 O0oo0 . setSetting ( id = 'm3uCache' , value = "false" )
 O0oo0 . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def iii1iiii11I ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
if 56 - 56: IiI1i11I . i1IiiiI1iI
if 3 - 3: o0ii1I + i1IiiiI1iI . ooOoO0O00 / oooOo0oo0oo % i1IiiiI1iI
if 98 - 98: III1iiIii * iI11I1II1I1I . o0ii1I * I1ii11iIi11i / Ii1I + i1iIi
def iiI1ii111 ( ) :
 if 97 - 97: o0o00Oo0O / oooOo0oo0oo + I11i . i1i1I1IIii1II % OOooOOo - OOooOOo
 if 33 - 33: Iii % IIiIiII11i + oO0o
 if 93 - 93: ooOoO0O00 . III1iiIii / oOo0O0Ooo + III1iiIii
 if 58 - 58: Ii1I + o0o00Oo0O . I1ii11iIi11i + OOooOOo - oO0o - OOooOOo
 if 41 - 41: I1ii11iIi11i / ooOoO0O00 / I1ii11iIi11i - IiI1i11I . I11i
 if 65 - 65: o0o00Oo0O * Ii . ii / oOo0O0Ooo / IiI1i11I
 if 69 - 69: i1iIi % i1iIi
 if 76 - 76: Ii * IiI1i11I / oO0o % Ii1I + oooOo0oo0oo
 if 48 - 48: iI11I1II1I1I % ooOoO0O00 + OOooOOo % I11i
 if 79 - 79: OOooOOo % oOo0O0Ooo % o0ii1I / ooOoO0O00 % oO0o
 if 56 - 56: iI11I1II1I1I - Ii * IiI1i11I
 if 84 - 84: oooOo0oo0oo + o0ii1I + I11i
 if OO0o == "insert_username" :
  i1i1iIII11i = IiIIoOo ( )
  oo0oIi = oOooOOo00ooO ( )
  I11 ( 'User' , i1i1iIII11i )
  I11 ( 'Pass' , oo0oIi )
  xbmc . executebuiltin ( 'Container.Refresh' )
  o0OO0oooo = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( i1i1iIII11i , oo0oIi )
  o0OO0oooo = OooOoooOo ( o0OO0oooo )
  if o0OO0oooo == "" :
   I11II1i1 = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   IiI1ii11I1 = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   I1i1iI = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , I11II1i1 , IiI1ii11I1 , I1i1iI )
   iiI1ii111 ( )
  else :
   I11II1i1 = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   IiI1ii11I1 = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   I1i1iI = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % i1i1iIII11i )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , I11II1i1 , IiI1ii11I1 , I1i1iI )
   xbmc . executebuiltin ( 'Container.Refresh' )
   I1iI1I1ii1 ( )
 else :
  I1iI1I1ii1 ( )
def IiIIoOo ( ) :
 iIIi1 = xbmc . Keyboard ( '' , 'heading' , True )
 iIIi1 . setHeading ( 'Enter Username' )
 iIIi1 . setHiddenInput ( False )
 iIIi1 . doModal ( )
 if ( iIIi1 . isConfirmed ( ) ) :
  o0Ooo0o0Oo = iIIi1 . getText ( )
  return o0Ooo0o0Oo
 else :
  return False
  if 55 - 55: iI11I1II1I1I * IiI1i11I
  if 85 - 85: iI11I1II1I1I . IIiIiII11i
def oOooOOo00ooO ( ) :
 iIIi1 = xbmc . Keyboard ( '' , 'heading' , True )
 iIIi1 . setHeading ( 'Enter Password' )
 iIIi1 . setHiddenInput ( False )
 iIIi1 . doModal ( )
 if ( iIIi1 . isConfirmed ( ) ) :
  o0Ooo0o0Oo = iIIi1 . getText ( )
  return o0Ooo0o0Oo
 else :
  return False
def o0ooo0o0 ( ) :
 iiI1iI = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  O00Oooo00 = urllib2 . urlopen ( iiI1iI )
  print O00Oooo00 . getcode ( )
  O00Oooo00 . close ( )
  if 93 - 93: o0o00Oo0O / i1iIi + oOo0O0Ooo
  pass
  if 20 - 20: III1iiIii / IiI1i11I % ii / iI11I1II1I1I + oOo0O0Ooo
 except urllib2 . HTTPError , Ooo0O0oooo :
  print Ooo0O0oooo . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def I1iI1I1ii1 ( ) :
 iii ( )
 if 57 - 57: I11i / i1IiiiI1iI
 if 13 - 13: ii + oO0o
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 32 - 32: o0o00Oo0O + i1i1I1IIii1II % I1ii11iIi11i
 if 7 - 7: Ii1I / i1iIi
 if 11 - 11: III1iiIii * i1iIi / i1iIi - oooOo0oo0oo
 if 68 - 68: oOo0O0Ooo % III1iiIii - III1iiIii / oOo0O0Ooo + Ii1I - I1ii11iIi11i
def o0oO0o00O ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 iiii1 = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 OooO0O0Ooo = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 o0OO0oooo = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 o0OO0oooo = OooOoooOo ( o0OO0oooo )
 if not o0OO0oooo == "" :
  oO0OIIIiIi1iiI = 'https://tinyurl.com/create.php?source=indexpage&url=' + iiii1 + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( oO0OIIIiIi1iiI ) )
  iI1 = 'https://tinyurl.com/create.php?source=indexpage&url=' + OooO0O0Ooo + '&submit=Make+TinyURL%21&alias='
  iiii1 = OooOoooOo ( oO0OIIIiIi1iiI )
  OooO0O0Ooo = OooOoooOo ( iI1 )
  xbmc . log ( str ( OooO0O0Ooo ) )
  o0Iiii = I1i1I ( iiii1 , '<div class="indent"><b>' , '</b>' )
  i1111iI1 = I1i1I ( OooO0O0Ooo , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % o0Iiii , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % i1111iI1 )
 else :
  return
def Oo0oOOOOo ( ) :
 o0ooo0o0 ( )
 iiiO000OOO ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , o0IIi1 + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( O00O00o )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  I1I1II1I11 ( ( '[COLORsteelblue]' + iIIIiIi + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOOo0O00o , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def I11IiI1iI ( url ) :
 open = OooOoooOo ( O0OO0OoO + url )
 o0OOo = IiI1Ii11Ii ( open , '<channel>' , '</channel>' )
 for OoO0oO0oo0O in o0OOo :
  if '<playlist_url>' in open :
   iIIIiIi = I1i1I ( OoO0oO0oo0O , '<title>' , '</title>' )
   ooOo0O0O0oOO0 = I1i1I ( OoO0oO0oo0O , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   I1I1II1I11 ( str ( base64 . b64decode ( iIIIiIi ) ) . replace ( '?' , '' ) , ooOo0O0O0oOO0 , 3 , icon , IIo0o0O0O00oOOo , '' )
  else :
   iIIIiIi = I1i1I ( OoO0oO0oo0O , '<title>' , '</title>' )
   iIIIiIi = base64 . b64decode ( iIIIiIi )
   oooOOO0ooOoOOO = I1i1I ( OoO0oO0oo0O , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = I1i1I ( OoO0oO0oo0O , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   O000OOO = I1i1I ( OoO0oO0oo0O , '<description>' , '</description>' )
   O000OOO = base64 . b64decode ( O000OOO )
   o0IiIiI111IIII1 = I1i1I ( O000OOO , 'PLOT:' , '\n' )
   OOOoOooO000oO = I1i1I ( O000OOO , 'CAST:' , '\n' )
   o0OOOOOo00 = I1i1I ( O000OOO , 'RATING:' , '\n' )
   oo0oOO = I1i1I ( O000OOO , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   oo0oOO = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( oo0oOO )
   IIO000oooOO0Oo0 = I1i1I ( O000OOO , 'DURATION_SECS:' , '\n' )
   I1iIiIii = I1i1I ( O000OOO , 'GENRE:' , '\n' )
   OO0 ( str ( iIIIiIi ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , oooOOO0ooOoOOO , IIo0o0O0O00oOOo , o0IiIiI111IIII1 , str ( oo0oOO ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( OOOoOooO000oO ) . split ( ) , o0OOOOOo00 , IIO000oooOO0Oo0 , I1iIiIii )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 17 - 17: o0ii1I * IIiIiII11i / III1iiIii + iI11I1II1I1I . Iii - o0o00Oo0O
O0OOO00OOO00o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
i11o00Ooo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 54 - 54: oOo0O0Ooo * oooOo0oo0oo + I11i % ooOoO0O00 - I11i + OOooOOo
def IIIIiI11Ii1i ( ) :
 iiI1iI = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  O00Oooo00 = urllib2 . urlopen ( iiI1iI )
  print O00Oooo00 . getcode ( )
  O00Oooo00 . close ( )
  if 100 - 100: IiI1i11I + Iii + i1iIi + IiI1i11I / ooOoO0O00
  pass
  if 74 - 74: o0o00Oo0O % ii * I1ii11iIi11i + oooOo0oo0oo * IiI1i11I
 except urllib2 . HTTPError , Ooo0O0oooo :
  print Ooo0O0oooo . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 100 - 100: oooOo0oo0oo + o0ii1I * I11i + IIiIiII11i
 oOOo0O00o = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 oOo0O000Ooo0 ( oOOo0O00o , i11o00Ooo + "uide.xml" )
 if 30 - 30: ooOoO0O00
 O0oO0 = open ( O0OOO00OOO00o , 'r+' )
 input = open ( O0OOO00OOO00o ) . read ( ) . decode ( 'UTF-8' )
 O0Oo0O00o0oo0OO = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 O0oO0 . write ( O0Oo0O00o0oo0OO )
 O0oO0 . truncate ( )
 O0oO0 . close ( )
 OooO00 ( )
 if 66 - 66: o0ii1I % o0ii1I - III1iiIii
def OooO00 ( ) :
 open = OooOoooOo ( oOooO0OoO )
 all = IiI1Ii11Ii ( open , '{"num' , 'direct' )
 for OoO0oO0oo0O in all :
  if '"tv_archive":1' in OoO0oO0oo0O :
   iIIIiIi = I1i1I ( OoO0oO0oo0O , '"epg_channel_id":"' , '"' )
   oooOOO0ooOoOOO = I1i1I ( OoO0oO0oo0O , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = I1i1I ( OoO0oO0oo0O , 'stream_id":"' , '"' )
   iIIIiIi = iIIIiIi . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   I1I1II1I11 ( iIIIiIi , id , 90027 , oooOOO0ooOoOOO , IIo0o0O0O00oOOo , iIIIiIi )
   if 58 - 58: o0ii1I % ii
   if 49 - 49: Ii1I + o0o00Oo0O . o0ii1I * ii
def oO0OOO00 ( name , url , description ) :
 id = url
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 I1iIiI1iiiiI1 = open ( O0OOO00OOO00o )
 IIII1ii1 = ElementTree . parse ( I1iIiI1iiiiI1 )
 OOO0O0OOo = "apples"
 import datetime as dt
 from datetime import time
 Iii1 = datetime . now ( ) - timedelta ( days = 5 )
 ii11II1i = str ( Iii1 )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 OOoO = IIII1ii1 . findall ( "programme" )
 for i1IiiI in OOoO :
  if name in i1IiiI . attrib . get ( 'channel' ) :
   O0OOO0 = i1IiiI . attrib . get ( 'start' )
   o0OIi , IIi1iiI , o0ooOO00OO0o0O = O0OOO0 . partition ( ' +' )
   ii11II1i = str ( ii11II1i ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   oo0oOO , III1IiiIiiI1i , Ii1i1I1 = O0OOO0 . partition ( '2017' )
   OoO0o00OoO = i1IiiI . find ( 'title' ) . text + O0OOO0
   Ii1i1I1 = Ii1i1I1 [ : - 6 ]
   if o0OIi > ii11II1i :
    if o0OIi < I1IIIii :
     Oo00Oooo00o = o0OIi
     Oo00Oooo00o = Oo00Oooo00o [ : 4 ] + '/' + Oo00Oooo00o [ 4 : ]
     o0OIi = o0OIi [ : 4 ] + '-' + o0OIi [ 4 : ]
     Oo00Oooo00o = Oo00Oooo00o [ : 7 ] + '/' + Oo00Oooo00o [ 7 : ]
     o0OIi = o0OIi [ : 7 ] + '-' + o0OIi [ 7 : ]
     Oo00Oooo00o = Oo00Oooo00o [ : 10 ] + ' - ' + Oo00Oooo00o [ 10 : ]
     o0OIi = o0OIi [ : 10 ] + ':' + o0OIi [ 10 : ]
     Oo00Oooo00o = Oo00Oooo00o [ : 15 ] + ':' + Oo00Oooo00o [ 15 : ]
     o0OIi = o0OIi [ : 13 ] + '-' + o0OIi [ 13 : ]
     Oo00Oooo00o = Oo00Oooo00o [ : - 2 ]
     o0OIi = o0OIi [ : - 2 ]
     II11II1I = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&start=" + str ( o0OIi ) + "&duration=240" + "&stream=%s" ) % ( OO0o , Ooo , id )
     OOO0O0OOo = II11II1I + str ( o0OIi ) + "&duration=240"
     Oo00Oooo00o = '[COLOR blue]%s - [/COLOR]' % Oo00Oooo00o
     OoO0o00OoO = str ( Oo00Oooo00o ) + i1IiiI . find ( 'title' ) . text
     O000OOO = i1IiiI . find ( 'desc' ) . text
     Ii1I1i ( OoO0o00OoO , II11II1I , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , O000OOO )
def O0OO00000o00 ( url ) :
 url = str ( url ) . replace ( 'USERNAME' , OO0o ) . replace ( 'PASSWORD' , Ooo )
 i1I11iIiII = xbmcgui . ListItem ( '' , iconImage = 'DefaultVideo.png' , thumbnailImage = O0O )
 i1I11iIiII . setInfo ( type = 'Video' , infoLabels = { 'Title' : '' , 'Plot' : '' } )
 i1I11iIiII . setProperty ( 'IsPlayable' , 'true' )
 i1I11iIiII . setPath ( str ( url ) )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1I11iIiII )
def oOo0O000Ooo0 ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 OOO000Oo = time . time ( )
 urllib . urlretrieve ( url , dest , lambda I1IIIi1i , OooIii1I1iI , oOoOo0 : iIi ( I1IIIi1i , OooIii1I1iI , oOoOo0 , o0oOoO00o , OOO000Oo ) )
def iIi ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  oOo = min ( numblocks * blocksize * 100 / filesize , 100 )
  ooOo0o = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  III = numblocks * blocksize / ( time . time ( ) - start_time )
  if III > 0 :
   IiiI = ( filesize - numblocks * blocksize ) / III
  else :
   IiiI = 0
  III = III / 1024
  OoOoO00o00 = III / 1024
  OOooooO0o0O0 = float ( filesize ) / ( 1024 * 1024 )
  oO0oo = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( ooOo0o )
  Ooo0O0oooo = '[COLOR white]Speed:  %.02f Mb/s ' % OoOoO00o00 + '[/COLOR]'
  dp . update ( oOo , oO0oo , Ooo0O0oooo )
 except :
  oOo = 100
  dp . update ( oOo )
 if dp . iscanceled ( ) :
  o00o0o000Oo = xbmcgui . Dialog ( )
  o00o0o000Oo . ok ( "GenieTv" , 'The download was cancelled.' )
  if 100 - 100: ooOoO0O00 - Ii . i1IiiiI1iI * oO0o
  sys . exit ( )
  dp . close ( )
  if 62 - 62: o0o00Oo0O
def iiIIIIiii ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  iiii1iii1IiiiI1i1 ( )
  if 37 - 37: I1ii11iIi11i - ooOoO0O00 - III1iiIii + Iii . iI11I1II1I1I
  if 59 - 59: ii - i1IiiiI1iI % I11i . Iii + ooOoO0O00 * Iii
  if 5 - 5: IIiIiII11i - III1iiIii
  if 86 - 86: III1iiIii * Iii + o0o00Oo0O * i1IiiiI1iI + Ii - Ii1I
  if 70 - 70: Ii
  if 57 - 57: Iii % oooOo0oo0oo + i1iIi * o0ii1I . I1ii11iIi11i
  if 78 - 78: ii / ooOoO0O00 . oooOo0oo0oo
  if 88 - 88: Iii + oOo0O0Ooo - Iii / ii - Ii
def iiii1iii1IiiiI1i1 ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for oOOo0O00o in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def i11Ii1IiIIIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OOOoo00o0o = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IIII1ii = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 ii1I1IIii11 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 II1i11I = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IiIIi1I1I11Ii = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OOoOoo00Oo = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 III1I11i1iIi = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 O00o0OO0OO0oo = Ooo0O0ooo0o ( )
 IiiiIIiii = OO0Oo00Oo ( )
 for url in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OOOoo00o0o :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IIII1ii :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in II1i11I :
  dt = datetime . fromtimestamp ( float ( II1i11I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   oOOo000oOoO0 ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in ii1I1IIii11 :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IiIIi1I1I11Ii :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OOoOoo00Oo :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in III1I11i1iIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + O00o0OO0OO0oo , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + IiiiIIiii , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 25 - 25: iI11I1II1I1I
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 63 - 63: i1iIi
def oO0oOOOooo ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 Ii1iiI1i1 ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 3 - 3: oooOo0oo0oo . III1iiIii / I1ii11iIi11i
def OooIIi111 ( data ) :
 oO0o0o0O = len ( data ) % 4
 if 11 - 11: i1IiiiI1iI - Iii % Ii . iI11I1II1I1I * oOo0O0Ooo - I1ii11iIi11i
 if 73 - 73: o0o00Oo0O + i1iIi - o0o00Oo0O / ii * I1ii11iIi11i
 if 32 - 32: oO0o % oOo0O0Ooo % IiI1i11I
 if 66 - 66: OOooOOo + I11i
 if 54 - 54: Ii1I + Ii1I + Iii % ooOoO0O00 % Ii
 if 100 - 100: Ii1I
 if oO0o0o0O != 0 :
  data += b'=' * ( 4 - oO0o0o0O )
 return base64 . decodestring ( data )
def I1i1I ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : OOOoo000o0oo0 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : OOOoo000o0oo0 = ''
 else :
  try : OOOoo000o0oo0 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : OOOoo000o0oo0 = ''
 return OOOoo000o0oo0
 if 71 - 71: i1iIi . Iii + oooOo0oo0oo
 if 8 - 8: Ii * o0o00Oo0O + Ii1I . iI11I1II1I1I % Iii / Iii
def IiI1Ii11Ii ( text , start_with , end_with ) :
 OOOoo000o0oo0 = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return OOOoo000o0oo0
def Ooo0O0ooo0o ( ) :
 oO00oo = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 oO00oo . connect ( ( '8.8.8.8' , 0 ) )
 oO00oo = oO00oo . getsockname ( ) [ 0 ]
 return oO00oo
 if 89 - 89: o0ii1I
def OO0Oo00Oo ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 O00o0OO0OO0oo = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( O00o0OO0OO0oo . group ( ) )
o0IIi1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
oOooO0OoO = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
o00O00O0Oo0 = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
OoOiI11IiI1i1 = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
ooO = '&action=get_live_categories'
oOoO0 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
O00O00o = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 31 - 31: Ii - i1iIi / Ii1I - o0ii1I
O0OO0OoO = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
iiIiIi1111iI1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
IIIOoO0o = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
OO0o0O0O0O0 = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 34 - 34: oO0o * o0ii1I * I1ii11iIi11i
def Iioo0O00ooo0o ( ) :
 o0ooo0o0 ( )
 open = OooOoooOo ( IIIOoO0o )
 o0OOo = IiI1Ii11Ii ( open , '<channel>' , '</channel>' )
 for OoO0oO0oo0O in o0OOo :
  iIIIiIi = I1i1I ( OoO0oO0oo0O , '<title>' , '</title>' )
  iIIIiIi = base64 . b64decode ( iIIIiIi )
  ooOo0O0O0oOO0 = I1i1I ( OoO0oO0oo0O , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  I1I1II1I11 ( '[COLORsteelblue]' + iIIIiIi + '[/COLOR]' , ooOo0O0O0oOO0 , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 29 - 29: ii . IIiIiII11i % OOooOOo
def IiiIi1I11 ( url ) :
 open = OooOoooOo ( OO0o0O0O0O0 + url )
 o0OOo = IiI1Ii11Ii ( open , '<channel>' , '</channel>' )
 for OoO0oO0oo0O in o0OOo :
  iIIIiIi = I1i1I ( OoO0oO0oo0O , '<title>' , '</title>' )
  iIIIiIi = base64 . b64decode ( iIIIiIi )
  xbmc . log ( str ( iIIIiIi ) )
  oooOOO0ooOoOOO = I1i1I ( OoO0oO0oo0O , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  ooOo0O0O0oOO0 = I1i1I ( OoO0oO0oo0O , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  O000OOO = I1i1I ( OoO0oO0oo0O , '<description>' , '</description>' )
  O000OOO = base64 . b64decode ( O000OOO )
  i1I1Ii11II1i = '('
  oooOoOOoOO0O = ')'
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , ooOo0O0O0oOO0 , 222 , oooOOO0ooOoOOO , IIo0o0O0O00oOOo , ( '[COLOR' + ooOoOoo0O + ']' + O000OOO + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( oooOoOOoOO0O , '[COLORsteelblue]' ) . replace ( i1I1Ii11II1i , '[COLORorangered]' ) )
  if 9 - 9: i1IiiiI1iI * ii % oOo0O0Ooo / OOooOOo * Iii
def iiIiII1 ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( oOoO0 + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , type , ooO0000o00O , o0OO in IIi :
  O0Ooo = ( OoOiI11IiI1i1 + ooO0000o00O + '.m3u8' ) . strip ( )
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , O0Ooo , 222 , ( o0OO ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
def ii111iI ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIIi , ii11I1 in IIi :
  if name == iIiIIi :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) + ii11I1 , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def I1I ( name ) :
 oOO0o0 = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , ooO0OO , oOOo0O00o in IIi :
  oOOo0O00o = ( oOOo0O00o ) . replace ( '.ts' , '.m3u8' )
  Ii1I1i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oOOo0O00o ) . strip ( ) , 222 , ooO0OO , ooO0OO , '' )
 else :
  Ii1I1i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 36 - 36: Ii + Ii1I % oooOo0oo0oo . oOo0O0Ooo - i1iIi
  if 94 - 94: oOo0O0Ooo % OOooOOo . III1iiIii . i1iIi . oO0o
  if 53 - 53: OOooOOo
  if 84 - 84: oO0o
  if 97 - 97: ooOoO0O00
  if 98 - 98: ii - oOo0O0Ooo + i1iIi
  if 98 - 98: IiI1i11I . III1iiIii . III1iiIii - oooOo0oo0oo
  if 65 - 65: I1ii11iIi11i + I11i - o0ii1I
  if 12 - 12: ii + Ii1I
  if 55 - 55: oooOo0oo0oo * IIiIiII11i + i1i1I1IIii1II
  if 93 - 93: IiI1i11I * i1i1I1IIii1II . oO0o - o0ii1I + o0o00Oo0O * oO0o
  if 59 - 59: IIiIiII11i
def o00o0 ( ) :
 I1I1II1I11 ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  I1I1II1I11 ( 'Backup Genie Favourites' , oOOo0O00o , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  I1I1II1I11 ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  I1I1II1I11 ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 43 - 43: I1ii11iIi11i + ii
  if 47 - 47: i1iIi
  if 92 - 92: Iii % Ii % I1ii11iIi11i
zip = oo00 . getSetting ( 'zip' )
ii11Ii1IiiI1 = xbmc . translatePath ( os . path . join ( zip ) )
def O00o0o ( ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 65 - 65: Ii1I % i1i1I1IIii1II . ii * I11i * oO0o
  if 10 - 10: i1i1I1IIii1II - IiI1i11I % IIiIiII11i - i1IiiiI1iI - ooOoO0O00
  if 10 - 10: Ii1I - Iii . i1IiiiI1iI
def iiIIIi1iIi ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  O00o0o ( )
  OOo0OOOoOOo = open ( url ) . read ( )
  IIIooo0o0O = os . path . join ( ii11Ii1IiiI1 , description . split ( 'Your ' ) [ 1 ] )
  O0oO0 = open ( IIIooo0o0O , mode = 'w' )
  O0oO0 . write ( OOo0OOOoOOo )
  O0oO0 . close ( )
 else :
  if 'guisettings.xml' in description :
   OoO0oO0oo0O = open ( os . path . join ( ii11Ii1IiiI1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOOoo000o0oo0 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( OOOoo000o0oo0 ) . findall ( OoO0oO0oo0O )
   for type , IiiiIIi11II , o0oooOo0oo in IIi :
    o0oooOo0oo = o0oooOo0oo . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IiiiIIi11II , o0oooOo0oo ) )
  else :
   IIIooo0o0O = os . path . join ( url )
   OOo0OOOoOOo = open ( os . path . join ( ii11Ii1IiiI1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O0oO0 = open ( IIIooo0o0O , mode = 'w' )
   O0oO0 . write ( OOo0OOOoOOo )
   O0oO0 . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 33 - 33: i1IiiiI1iI % IIiIiII11i
 if 49 - 49: Ii1I + Iii / I11i + ii + oooOo0oo0oo / III1iiIii
 if 29 - 29: o0ii1I - o0ii1I / i1iIi
 if 49 - 49: Iii + i1i1I1IIii1II % oO0o - I1ii11iIi11i - o0o00Oo0O - ii
def Ii1I1Iiii ( ) :
 oOIii = 1
 O00o0o ( )
 i1IIIIiiI11 = xbmc . translatePath ( os . path . join ( ii11Ii1IiiI1 , 'Build Backup' , 'Full Backup' , '' ) )
 I1iii1I = xbmc . translatePath ( os . path . join ( ii11Ii1IiiI1 , 'Build Backup' , 'my_full_backup.zip' ) )
 ooo = xbmc . translatePath ( os . path . join ( ii11Ii1IiiI1 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( i1IIIIiiI11 ) :
  os . makedirs ( i1IIIIiiI11 )
 II111 = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not II111 ) : return False , 0
 I11iIi = II111
 Ii1IIiII1I = xbmc . translatePath ( os . path . join ( i1IIIIiiI11 , I11iIi + '.zip' ) )
 OOOii = [ 'plugin.video.GenieTv' ]
 Iii1I11 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 O0o0o = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 IiiiIi1111I = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iII1i1ii = "Creating full backup of existing build"
 i1I1ii1i = "Creating Community Build"
 iiiiII11iIi = "Archiving..."
 OO00 = ""
 Oooo = "Please Wait"
 O00 ( oOo0oooo00o , Ii1IIiII1I , i1I1ii1i , iiiiII11iIi , OO00 , Oooo , O0o0o , IiiiIi1111I )
 time . sleep ( 1 )
 IiIIIIi = xbmc . translatePath ( os . path . join ( i1IIIIiiI11 , I11iIi + '_guisettings.zip' ) )
 OoIIiIIIII1I = zipfile . ZipFile ( IiIIIIi , mode = 'w' )
 try :
  OoIIiIIIII1I . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 OoIIiIIIII1I . close ( )
 if oOIii == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + I1iii1I , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + Ii1IIiII1I + '[/COLOR]' )
  if 96 - 96: Ii . IIiIiII11i
def O00 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iI1I = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 Iii1IiI1iI1I = len ( sourcefile )
 Iiii = [ ]
 oOii11I = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for Ooo0O00 , oooo0oOOoO000 , Oo00o00Oo in os . walk ( sourcefile ) :
  for file in Oo00o00Oo :
   oOii11I . append ( file )
 i1I1i1I111 = len ( oOii11I )
 for Ooo0O00 , oooo0oOOoO000 , Oo00o00Oo in os . walk ( sourcefile ) :
  oooo0oOOoO000 [ : ] = [ oOo00OO0ooOOO for oOo00OO0ooOOO in oooo0oOOoO000 if oOo00OO0ooOOO not in exclude_dirs ]
  Oo00o00Oo [ : ] = [ O0oO0 for O0oO0 in Oo00o00Oo if O0oO0 not in exclude_files ]
  for file in Oo00o00Oo :
   Iiii . append ( file )
   i1i1I1Ii1IIii = len ( Iiii ) / float ( i1I1i1I111 ) * 100
   o0oOoO00o . update ( int ( i1i1I1Ii1IIii ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   oooOOoo = os . path . join ( Ooo0O00 , file )
   if not 'temp' in oooo0oOOoO000 :
    if not 'plugin.program.originwizard' in oooo0oOOoO000 :
     import time
     iI1iii1iIiiI = '01/01/1980'
     II1iiiiI1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( oooOOoo ) ) )
     if II1iiiiI1 > iI1iii1iIiiI :
      iI1I . write ( oooOOoo , oooOOoo [ Iii1IiI1iI1I : ] )
 iI1I . close ( )
 o0oOoO00o . close ( )
 if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
 if 63 - 63: III1iiIii + iI11I1II1I1I + oOo0O0Ooo + i1IiiiI1iI
def oOOoO0O ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 76 - 76: ooOoO0O00 / iI11I1II1I1I - Ii1I - IIiIiII11i
 if 76 - 76: Ii + III1iiIii % OOooOOo
def iIIiiIii111 ( ) :
 iii ( )
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  OoOo0oOooOoOO ( )
 if O0O00Oo == 1 :
  i1i1I111iIi1 ( )
 if O0O00Oo == 2 :
  i11I1I1iiI ( )
 if O0O00Oo == 3 :
  IIIIIIi1IiIi ( )
  if 6 - 6: Iii . OOooOOo
  if 23 - 23: oOo0O0Ooo * i1iIi / OOooOOo . iI11I1II1I1I % Ii
  if 61 - 61: o0o00Oo0O
  if 21 - 21: oO0o % iI11I1II1I1I . oO0o
  if 99 - 99: I11i * oooOo0oo0oo % i1i1I1IIii1II * i1i1I1IIii1II + ii
  if 82 - 82: Iii / OOooOOo - oooOo0oo0oo / i1iIi
  if 50 - 50: oooOo0oo0oo + oO0o . Ii + Ii1I + Ii
  if 31 - 31: i1i1I1IIii1II * i1IiiiI1iI . OOooOOo * Iii
  if 28 - 28: III1iiIii + oOo0O0Ooo - I1ii11iIi11i % oooOo0oo0oo . Iii + oOo0O0Ooo
def O0oO0oOO00Oo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   ooO00O00oOO ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if O0O00Oo == 1 :
   ooO00O00oOO ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if O0O00Oo == 2 :
   IIIi1i ( )
  if O0O00Oo == 3 :
   iI1111i1i11Ii ( )
  if O0O00Oo == 4 :
   oo0O00o0O0Oo ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if O0O00Oo == 5 :
   iii11 ( )
  if O0O00Oo == 6 :
   I1i11IIIi ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if O0O00Oo == 7 :
   III1IIIIIiiI ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if O0O00Oo == 8 :
   i1iIii ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if O0O00Oo == 9 :
   O0o00 ( )
  if O0O00Oo == 10 :
   I1IIi1iI1iiI ( )
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
  if 27 - 27: iI11I1II1I1I % Iii - i1IiiiI1iI
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 67 - 67: o0o00Oo0O / i1IiiiI1iI * o0ii1I % i1iIi . Ii1I * i1i1I1IIii1II
def IiiiIIIi11ii1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   O00Oo00OOoO0 ( )
  if O0O00Oo == 1 :
   iiI ( )
  if O0O00Oo == 2 :
   I1i ( )
  if O0O00Oo == 3 :
   oOoo ( oOOo0O00o )
  if O0O00Oo == 4 :
   o00O0o00oo ( oOOo0O00o )
  if O0O00Oo == 5 :
   OOOOo0o00OO0000 ( )
  if O0O00Oo == 6 :
   iIiiII ( url = 'http://www.iplocation.net/' , inc = 1 )
  if O0O00Oo == 7 :
   iII1I ( )
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
  if 92 - 92: i1IiiiI1iI % o0ii1I
  if 30 - 30: IIiIiII11i - I11i % i1IiiiI1iI . Iii
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 63 - 63: iI11I1II1I1I / i1iIi
 if 24 - 24: I1ii11iIi11i / iI11I1II1I1I % oooOo0oo0oo * OOooOOo - iI11I1II1I1I
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
 if 50 - 50: IIiIiII11i
 if 39 - 39: IIiIiII11i . OOooOOo - I1ii11iIi11i * ooOoO0O00 . ii
def iIIiI ( ) :
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
 if 90 - 90: IiI1i11I * o0ii1I - IiI1i11I + oO0o + Iii % o0o00Oo0O
def II1III1I1I1Ii ( ) :
 iii ( )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 Ii1I1i ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 11 - 11: oooOo0oo0oo % i1IiiiI1iI * OOooOOo
def OoO00oo0 ( ) :
 iii ( )
 Ii1I1i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 Ii1I1i ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 96 - 96: ooOoO0O00
 if 55 - 55: i1i1I1IIii1II + oooOo0oo0oo + o0ii1I
 if 82 - 82: Ii1I . IIiIiII11i / OOooOOo / oO0o
def I1ii1iI ( ) :
 iii ( )
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  i1i1 ( )
 if O0O00Oo == 0 :
  IIii1Ii1i1ii1 ( oOOo0O00o )
 if O0O00Oo == 0 :
  oOOoOOooO0 ( oOOo0O00o )
  if 42 - 42: iI11I1II1I1I * o0ii1I / oO0o + oooOo0oo0oo
  if 48 - 48: ii - i1IiiiI1iI . Ii * IiI1i11I - o0ii1I - I11i
  if 59 - 59: IiI1i11I / Iii . I1ii11iIi11i
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 100 - 100: o0o00Oo0O
def oOOO00Oo ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for ooO0OO , iIIIiIi in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , ooO0OO , ooO0OO , '' )
 I1iI1ii1II ( 'tvshows' , 'INFO' )
 if 48 - 48: IIiIiII11i + IIiIiII11i * ooOoO0O00 / o0ii1I
def iii11III1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0oO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 59 - 59: IIiIiII11i
def i1i1 ( ) :
 iii ( )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 29 - 29: oO0o . i1iIi
def O00oooO00oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Ii111III1i11I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 62 - 62: Iii . oO0o + oO0o + IIiIiII11i * iI11I1II1I1I + ii
def Oo0OOOOOOO0oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + II1Iiiii111i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 52 - 52: o0o00Oo0O - iI11I1II1I1I / oO0o / III1iiIii
def I11Iii11i11I1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiOO0oo00OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 87 - 87: iI11I1II1I1I % o0o00Oo0O + Iii % I11i / i1i1I1IIii1II / I11i
def O0O00 ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 32 - 32: III1iiIii - i1i1I1IIii1II . iI11I1II1I1I . i1IiiiI1iI + IIiIiII11i % ii
def IIii1Ii1i1ii1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Oo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 40 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 75 - 75: o0o00Oo0O
def oOoO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 80 - 80: OOooOOo + iI11I1II1I1I . III1iiIii
def oooooo0O000o ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  ooOoOoo000O0O ( )
 if O0O00Oo == 1 :
  iI11i ( )
 if O0O00Oo == 2 :
  oOOO0I1iIIi ( )
  if 21 - 21: i1i1I1IIii1II * i1i1I1IIii1II / Iii . IiI1i11I
  if 10 - 10: o0ii1I * oooOo0oo0oo - I1ii11iIi11i - ii / I11i
  if 86 - 86: i1IiiiI1iI % oOo0O0Ooo
  if 22 - 22: Ii * i1IiiiI1iI . I1ii11iIi11i . ii + oOo0O0Ooo
def iI11i ( ) :
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , Iii1oooo00Oo0O in IIi :
  IiI11i1IIiiI ( 'Android Apps' + Iii1oooo00Oo0O , 'https://www.apkfiles.com' + oOOo0O00o , 30035 , iiIi1IIiIi + 'apps.png' )
 for oOOo0O00o , Iii1oooo00Oo0O in i1Iii1i1I :
  IiI11i1IIiiI ( 'Android Games' + Iii1oooo00Oo0O , 'https://www.apkfiles.com' + oOOo0O00o , 30035 , iiIi1IIiIi + 'GAMES.png' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
def IiIiiIiiiiI ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '/cat' in url :
   IiI11i1IIiiI ( ( iIIIiIi ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def i1I ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '/app' in url :
   IiI11i1IIiiI ( ( iIIIiIi ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def IiiIIIIi ( url ) :
 I1i111I = OooOoooOo ( url )
 ooOo0O0O0oOO0 = url
 if "page=" in str ( url ) :
  ooOo0O0O0oOO0 = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  if 'apk' in url :
   Ii1I1i ( ( iIIIiIi ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + ooO0OO )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 Ii1I1i ( 'Next Page' , ooOo0O0O0oOO0 + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def IiIIIi ( name , url ) :
 I1i111I = ii1IIIIiI11 ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( I1i111I )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  Oo0 ( name , url , 'Brackets' )
def oOOO0I1iIIi ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIi1iiII = 'https://www.apkfiles.com/search?q=' + ( OO00o ) . replace ( ' ' , '+' ) + '&search_type=1'
 OOOOoOO0O = iIIi1iiII . lower ( )
 IiiIIIIi ( OOOOoOO0O )
 if 49 - 49: i1i1I1IIii1II . OOooOOo
def O0oo ( url ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( iIIi1OoOo0O00 , 'Download' ) )
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
 if 9 - 9: oooOo0oo0oo
def I1iII ( url ) :
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
 if 18 - 18: Iii + I1ii11iIi11i - oO0o / i1IiiiI1iI / oooOo0oo0oo
 if 53 - 53: oooOo0oo0oo + I11i . i1i1I1IIii1II / Iii
def o0000oO ( name , url , description ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 I11ii1IIiIi = os . path . join ( o00oo0 , name )
 try :
  os . remove ( I11ii1IIiIi )
 except :
  pass
 downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
 ooo0oo = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print ooo0oo
 print '======================================='
 extract . all ( I11ii1IIiIi , ooo0oo , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 70 - 70: o0o00Oo0O / ii + Ii1I + ooOoO0O00
 if 63 - 63: IiI1i11I / Ii1I * i1i1I1IIii1II / IIiIiII11i + oooOo0oo0oo - o0o00Oo0O
 if 16 - 16: IIiIiII11i / o0ii1I . o0ii1I - o0ii1I / Ii1I
 if 28 - 28: oooOo0oo0oo * ii + i1iIi % IiI1i11I . iI11I1II1I1I
 if 17 - 17: III1iiIii / I11i . oooOo0oo0oo + I11i / Ii1I . I1ii11iIi11i
def ooOoOoo000O0O ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , oOOo0O00o , o0OO , IIo0o0O0O00oOOo , iII11O00OO00OOOoO in IIi :
  Ii1I1i ( iIIIiIi , oOOo0O00o , 80003 , o0OO , iiIi1IIiIi + 'APKToolsB.png' , iII11O00OO00OOOoO )
def IiI11Ii1iI ( apk , ret = None ) :
 if apk == "kodi" :
  ooOo0 = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( ooOo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   oOo0o = IIi [ 0 ] [ 0 ]
   I11iIi = IIi [ 0 ] [ 1 ]
   O000OOO000o = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( oOo0o , I11iIi )
  if ret == 'version' : return oOo0o
  else : return O000OOO000o
 elif apk == "spmc" :
  I11iiIiiI1iIi11 = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( I11iiIiiI1iIi11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  oOo0o = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  O000OOO000o = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( oOo0o , oOo0o )
  if ret == 'version' : return oOo0o
  else : return O000OOO000o
def Oo0 ( name , url , Brackets ) :
 if OO ( ) == 'android' :
  II1I1I11i1I1 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not II1I1I11i1I1 : iiIi1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  oOOO0oo0 = name
  if II1I1I11i1I1 :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not II1I1Ii ( url ) == True : iiIi1 ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % oOOO0oo0 , '' , 'Please Wait' )
   I11ii1IIiIi = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( I11ii1IIiIi )
   except : pass
   downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    OoIIiIIIII1I = zipfile . ZipFile ( I11ii1IIiIi )
    for file in OoIIiIIIII1I . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as O0oO0 :
       I11iIi1i1I1i1 = file . split ( '/' ) [ 1 ]
       O0oO0 . write ( OoIIiIIIII1I . read ( file ) )
       xbmc . sleep ( 500 )
       O0oO0 . close ( )
       try :
        os . remove ( I11ii1IIiIi )
       except :
        pass
       I11ii1IIiIi = os . path . join ( i1iIIi1 , I11iIi1i1I1i1 )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I11ii1IIiIi + '")' )
  else : iiIi1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iiIi1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 14 - 14: Iii
 if 18 - 18: oOo0O0Ooo
 if 23 - 23: ii * IIiIiII11i
 if 70 - 70: Ii1I + oOo0O0Ooo
def o0o0OOo0O ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  oOOo0O00o = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oOOo0O00o )
  O0O0 ( ( iIIIiIi ) . replace ( '_' , ' ' ) , oOOo0O00o )
  if 80 - 80: o0ii1I
def O0O0 ( name , url ) :
 if OO ( ) == 'android' :
  II1I1I11i1I1 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not II1I1I11i1I1 : iiIi1 ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  oOOO0oo0 = name
  if II1I1I11i1I1 :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not II1I1Ii ( url ) == True : iiIi1 ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % oOOO0oo0 , '' , 'Please Wait' )
   I11ii1IIiIi = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( I11ii1IIiIi )
   except : pass
   downloader . download ( url , I11ii1IIiIi , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + I11ii1IIiIi + '")' )
  else : iiIi1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iiIi1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 26 - 26: iI11I1II1I1I . ii - iI11I1II1I1I
 if 59 - 59: Ii1I + Iii . i1i1I1IIii1II
def oOOo0oO ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'INFO' )
 if 19 - 19: IiI1i11I
 if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + oooOo0oo0oo
def II11IiiIII ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 30015 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 31 - 31: o0ii1I * I11i * o0ii1I + oO0o * I11i . i1IiiiI1iI
def Oo00oo00o00Oo ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 i1ii1ii1II1 = url
 ooO0OO = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for ooO0000o00O , iIIIiIi in IIi :
  if '.mp4' in iIIIiIi :
   Ii1I1i ( 'Watch VIDEO' , url + '/' + ooO0000o00O , 222 , ooO0OO , fanart , '' )
  if 'description' in iIIIiIi :
   Ii1I1i ( 'Read Description' , url + '/' + ooO0000o00O , 30017 , ooO0OO , fanart , '' )
  if 'images' in iIIIiIi :
   I1I1II1I11 ( 'View Images' , url + '/' + ooO0000o00O , 30018 , ooO0OO , fanart , '' )
  if 'url' in iIIIiIi :
   Ii1I1i ( 'Install Build On Android' , url + '/' + ooO0000o00O , 30016 , ooO0OO , fanart , '' )
  if 'url' in iIIIiIi :
   Ii1I1i ( 'Install Build On Pc' , url + '/' + ooO0000o00O , 30019 , ooO0OO , fanart , '' )
 I1iI1ii1II ( 'movies' , 'INFO' )
 if 1 - 1: III1iiIii
def iiii ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  OOOO00 ( url )
  if 92 - 92: Iii % o0o00Oo0O % o0ii1I . o0ii1I . III1iiIii
def OOoO0Oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  OO0O00 ( url )
  if 65 - 65: ii
def iIIiI1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o0Ooo0o0Oo in IIi :
  o0OIiII ( 'Description:' , o0Ooo0o0Oo )
  if 4 - 4: ii + IiI1i11I % o0o00Oo0O + iI11I1II1I1I % IiI1i11I * Ii
def III1I1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for ooO0000o00O , iIIIiIi in IIi :
  if 'png' in iIIIiIi :
   Ii1I1i ( 'image' , '' , '' , url + '/' + ooO0000o00O , url + '/' + ooO0000o00O , '' )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 31 - 31: i1i1I1IIii1II - IiI1i11I
def iIII11I ( name , url , description ) :
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
 if 39 - 39: oOo0O0Ooo . Ii1I * IiI1i11I / OOooOOo % Ii
 if 29 - 29: OOooOOo
def OO0O00 ( url ) :
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
 O00Oo00OOoO0 ( )
 if 37 - 37: IIiIiII11i % IIiIiII11i + I11i % I1ii11iIi11i / oOo0O0Ooo . i1i1I1IIii1II
def OOOO00 ( url ) :
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
 O00Oo00OOoO0 ( )
 if 60 - 60: Iii . o0o00Oo0O / o0o00Oo0O
def Oo00o00 ( name , url , description ) :
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
 O00Oo00OOoO0 ( )
 if 74 - 74: o0o00Oo0O + iI11I1II1I1I + i1i1I1IIii1II * III1iiIii
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
  I1o0 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  O0oO0 . write ( I1o0 . rstrip ( '\r\n' ) + '\n' )
def O00Oo00OOoO0 ( ) :
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
  if 26 - 26: IiI1i11I * iI11I1II1I1I + IIiIiII11i / oOo0O0Ooo
  if 52 - 52: o0ii1I / OOooOOo + oO0o % o0ii1I % oooOo0oo0oo / i1i1I1IIii1II
  if 91 - 91: oO0o / oO0o . IIiIiII11i . i1iIi - oOo0O0Ooo
def oOOoOOooO0 ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iii11OO0oO , oooo0oOOoO000 , Oo00o00Oo in os . walk ( url ) :
  for file in Oo00o00Oo :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    OoO0oO0oo0O = open ( ( os . path . join ( iii11OO0oO , file ) ) ) . read ( )
    i1i11ii = OoO0oO0oo0O . replace ( oOo0oooo00o , 'special://home/' )
    O0oO0 = open ( ( os . path . join ( iii11OO0oO , file ) ) , mode = 'w' )
    O0oO0 . write ( str ( i1i11ii ) )
    O0oO0 . close ( )
 O00Oo00OOoO0 ( )
 if 86 - 86: Ii1I - ooOoO0O00 + I1ii11iIi11i * oOo0O0Ooo / Ii % i1i1I1IIii1II
def IIIi1i ( ) :
 IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 17 - 17: i1iIi + i1iIi . Ii1I
def iiI1ii1Iii11I ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def IIiIi11 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def oO0OO0O0 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in i1Iii1i1I :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , ooO0OO , iIIIiIi in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , ooO0OO )
def iIIi1II1 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( I1i111I )
 for url in IIi :
  I11iiiiI1i ( url )
def IiI1I11ii ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o
 oO0O00oO0o0 = 'https://www.radionomy.com/en/search/index?query=' + ( OO00o ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( oO0O00oO0o0 )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + iIIIiIi + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oOOo0O00o , 70005 , ooO0OO )
  if 93 - 93: III1iiIii / ooOoO0O00
  if 47 - 47: i1iIi - o0ii1I
def iii11 ( ) :
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.listenlive.eu/' + oOOo0O00o , 10111113 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def oo0O00o0O0Oo ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 if 98 - 98: i1i1I1IIii1II . i1IiiiI1iI / OOooOOo . i1iIi
 if 1 - 1: oooOo0oo0oo
 IIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , OoOo0o0OOoO0 , url , i1I1IIIiii1 in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' [COLORorangered] ' + i1I1IIIiii1 + '[/COLOR]' , url , 222225 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[CR]' + OoOo0o0OOoO0 + '[CR]' + i1I1IIIiii1 + '[/COLOR]' )
  if 76 - 76: ii
def i1iiIi1IiiiI ( ) :
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.toonjet.com/' + oOOo0O00o , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OO0oooOO ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
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
   IiI11i1IIiiI ( ( ooO0OO ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIIi1iiIIiiiI ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I1i111I )
 for url in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 26 - 26: i1iIi % i1i1I1IIii1II + oOo0O0Ooo / III1iiIii . oOo0O0Ooo
  if 38 - 38: ii + ii - Ii * oOo0O0Ooo * ooOoO0O00 / IIiIiII11i
def I1IIi1iI1iiI ( ) :
 iiiO000OOO ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 iiiO000OOO ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 78 - 78: I1ii11iIi11i - i1IiiiI1iI + IiI1i11I * o0ii1I * I11i
def iIiiiII11 ( ) :
 iiiO000OOO ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 iiiO000OOO ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 iiiO000OOO ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 98 - 98: Ii1I
def i1Ii1IiIIi ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oOOo0O00o , I1oOOO in IIi :
  if 'Parent' in iIIIiIi :
   pass
  elif '2' in I1oOOO :
   iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 54 - 54: i1i1I1IIii1II / iI11I1II1I1I / ii . ooOoO0O00 - OOooOOo
def Oo00o0OOo0OO ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oOOo0O00o , I1oOOO in IIi :
  if OO00o in iIIIiIi . lower ( ) :
   if '1' in I1oOOO :
    iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in I1oOOO :
    iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in I1oOOO :
    iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 18 - 18: i1iIi - III1iiIii / IIiIiII11i / Ii1I
    if 31 - 31: i1IiiiI1iI * oOo0O0Ooo + i1iIi
def iIIIIi11i ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIIIiIi , oOOo0O00o , I1oOOO in IIi :
  if '1' in I1oOOO :
   iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in I1oOOO :
   iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in I1oOOO :
   iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOOo0O00o , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 51 - 51: iI11I1II1I1I - oOo0O0Ooo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: ii . o0ii1I % i1i1I1IIii1II * ii
def O00o0O0oo ( url ) :
 ooO0000o00O = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in i1Iii1i1I :
  if 'mp3' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ooO0000o00O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ooO0000o00O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ooO0000o00O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in iIIIiIi :
   iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooO0000o00O + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 34 - 34: oO0o % I1ii11iIi11i + oO0o
   if 77 - 77: I1ii11iIi11i * i1iIi % o0ii1I
   if 2 - 2: Iii / I1ii11iIi11i / o0ii1I / Ii1I / ii
def IiiiI1I1iI11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 ooO0000o00O = url
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
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooO0000o00O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooO0000o00O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooO0000o00O + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 49 - 49: I1ii11iIi11i - iI11I1II1I1I
   if 64 - 64: i1IiiiI1iI + iI11I1II1I1I
def I1Iii ( ) :
 iiiO000OOO ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 iiiO000OOO ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 iiiO000OOO ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 30 - 30: ooOoO0O00 . Ii1I
def ooo0o00o ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oOOo0O00o + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in ooO0OO :
   pass
  else :
   iiiO000OOO ( ooO0OO , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oOOo0O00o ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + ooO0OO + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 86 - 86: III1iiIii + OOooOOo / oOo0O0Ooo + Iii % Iii / Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: OOooOOo + I11i . i1IiiiI1iI
 if 52 - 52: oO0o
def I1III1I11I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if '</a>' in iIIIiIi :
   pass
  elif '(' in iIIIiIi :
   iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 85 - 85: i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: o0ii1I % IIiIiII11i + III1iiIii + oooOo0oo0oo % i1i1I1IIii1II . oOo0O0Ooo
def OOoOo0ooOoo ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if OO00o in iIIIiIi . lower ( ) :
   if '</a>' in iIIIiIi :
    pass
   elif '(' in iIIIiIi :
    iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 68 - 68: oooOo0oo0oo + o0ii1I
    if 58 - 58: III1iiIii * o0ii1I . ooOoO0O00
def i11I1iiii ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if '</a>' in iIIIiIi :
   pass
  elif '(' in iIIIiIi :
   iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOOo0O00o , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 31 - 31: i1IiiiI1iI / I1ii11iIi11i / iI11I1II1I1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: I1ii11iIi11i * Iii + Iii
 if 39 - 39: ooOoO0O00 + IiI1i11I + o0o00Oo0O
def Ii1iII1ii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  ooO0000o00O = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( ooO0000o00O )
  if 80 - 80: iI11I1II1I1I / Ii + IiI1i11I
def I11I1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  if '<p align' in iIIIiIi :
   pass
  elif '&nbsp;' in iIIIiIi :
   pass
  else :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 100 - 100: i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 39 - 39: IIiIiII11i * oOo0O0Ooo - iI11I1II1I1I
 if 25 - 25: ii . o0ii1I % IiI1i11I . III1iiIii
def I1i1iii1Ii ( ) :
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
def ooo000 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iIiIii = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , ooO0OO , ooO0OO , iIIIiIi )
 for url , iIIIiIi in I1iIiIii :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def oooOoO0oo0o0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ii1IiIiI1 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIIIii1i1iI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 OoOOoO0o = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in IiIIIii1i1iI :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , iIIIiIi in ii1IiIiI1 :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def o0O00ooo0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 23 - 23: o0o00Oo0O
def O0O00OOo ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if '9cart' in oOOo0O00o :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 41 - 41: ooOoO0O00 . oooOo0oo0oo / i1iIi / I11i % III1iiIii - o0ii1I
def iI1i1Iiii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , iIIIiIi in ii1I1IIii11 :
  if '9cart' in url :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 15 - 15: o0ii1I
def iIII1IIi ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 20003 , ooO0OO )
 for url , iIIIiIi in i1Iii1i1I :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 63 - 63: IIiIiII11i . i1IiiiI1iI % III1iiIii + IIiIiII11i
def oO0OOoOO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   IiI11i1IIiiI ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 97 - 97: ooOoO0O00
def ii1iI1i1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 51 - 51: i1iIi * IiI1i11I / ooOoO0O00
def IIi1I1 ( url ) :
 url = cloudflare . source ( url )
 i11i1i ( url )
 if 37 - 37: I11i * I1ii11iIi11i
def iI11i1I1i ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  i11i1i ( url )
  if 96 - 96: i1IiiiI1iI / III1iiIii * iI11I1II1I1I + Ii * Ii1I / oOo0O0Ooo
  if 93 - 93: o0o00Oo0O * iI11I1II1I1I + o0ii1I % IiI1i11I
def iI ( ) :
 if 96 - 96: i1i1I1IIii1II % I1ii11iIi11i
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 20 - 20: i1iIi . III1iiIii / Iii . ii * oooOo0oo0oo + o0ii1I
def i11I1I1iiI ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 2 - 2: oOo0O0Ooo
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 11 - 11: oooOo0oo0oo + iI11I1II1I1I / OOooOOo % o0o00Oo0O
 for oOOo0O00o , iIIIiIi in IIi :
  if OO00o in iIIIiIi . lower ( ) :
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
    if 98 - 98: IIiIiII11i + I1ii11iIi11i * iI11I1II1I1I * Ii1I + oooOo0oo0oo * o0ii1I
    if 76 - 76: i1iIi . i1i1I1IIii1II
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 60 - 60: oooOo0oo0oo * i1iIi * oO0o
def OoOOo ( url ) :
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
 if 64 - 64: Iii / IIiIiII11i / oO0o - i1iIi * iI11I1II1I1I . IiI1i11I
def iIi11I1II ( url ) :
 I1i111I = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i111I )
 for ooO0OO in i1Iii1i1I :
  oO00Oo0O0 = ooO0OO
 ii1I1IIii11 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1i111I )
 for url in ii1I1IIii11 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10007 , oO00Oo0O0 )
  if 91 - 91: Iii + o0ii1I + III1iiIii
  if 58 - 58: IiI1i11I * o0ii1I - Ii % Ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: i1IiiiI1iI . Iii % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * oO0o
def ii1i1IiII111I ( url , IMAGE ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  print iIIIiIi + '     ' + url
  if 'easy' in url :
   Oo0o0OoOoOo0 ( url )
   if 36 - 36: o0ii1I * oOo0O0Ooo * Ii1I . Iii * Ii1I
   if 76 - 76: oooOo0oo0oo + o0o00Oo0O / III1iiIii - oO0o
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 27 - 27: I1ii11iIi11i - iI11I1II1I1I * IiI1i11I * IIiIiII11i * Ii1I
def Oo0o0OoOoOo0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I1i111I )
 for url in IIi :
  I11iiiiI1i ( url )
  if 9 - 9: Ii + oooOo0oo0oo - OOooOOo / i1iIi % ooOoO0O00 / i1i1I1IIii1II
  if 22 - 22: ooOoO0O00
  if 3 - 3: oO0o * Ii1I - IiI1i11I + Ii1I
def O0000oO00oO0o ( ) :
 if 86 - 86: I11i / i1iIi . I11i % oOo0O0Ooo + i1i1I1IIii1II % Iii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 72 - 72: i1iIi - Ii1I + i1i1I1IIii1II . OOooOOo
def IIIi ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  if 'elete' in iIIIiIi :
   pass
  else :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 222 , ooO0OO )
   if 35 - 35: oooOo0oo0oo . Iii . i1IiiiI1iI - Iii % Iii + i1IiiiI1iI
def oO0oO00 ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiiI1Ii1II = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , OO0oIii1I1I , i1iII1IiiIiI1 in IiiI1Ii1II :
  for OO00o in OO0oIii1I1I :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   IIiIIiIi1II1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oOOo0O00o , iIIIiIi in IIiIIiIi1II1IiI :
    if 'tube' in oOOo0O00o :
     pass
    elif 'stage' in oOOo0O00o :
     oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + OO0oIii1I1I + '   -   ' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ooO0OO , )
    elif 'vee' in oOOo0O00o :
     pass
     if 99 - 99: I1ii11iIi11i
def IiIi1I11 ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiiI1Ii1II = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , OO0oIii1I1I , i1iII1IiiIiI1 in IiiI1Ii1II :
  IIiIIiIi1II1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oOOo0O00o , iIIIiIi in IIiIIiIi1II1IiI :
   if 'tube' in oOOo0O00o :
    pass
   elif 'stage' in oOOo0O00o :
    oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + OO0oIii1I1I + '   -   ' + iIIIiIi + '[/COLOR]' , ( oOOo0O00o ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ooO0OO )
   elif 'vee' in oOOo0O00o :
    pass
    if 19 - 19: ooOoO0O00 / III1iiIii + Ii1I * Ii1I
    if 90 - 90: ii * IiI1i11I . Ii . i1iIi - i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: oOo0O0Ooo / ii
def I1iIi1iiiIiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 III1I1Ii11iI = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( III1I1Ii11iI ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in III1I1Ii11iI :
  OoO00oo00 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 52 - 52: i1i1I1IIii1II + i1IiiiI1iI * i1IiiiI1iI * I1ii11iIi11i - iI11I1II1I1I + Ii1I
  if 34 - 34: IiI1i11I / oO0o / I1ii11iIi11i
  if 92 - 92: i1IiiiI1iI % IiI1i11I % I11i . oOo0O0Ooo - Ii1I - I11i
  if 40 - 40: oOo0O0Ooo / ii + oO0o * oO0o
  if 9 - 9: iI11I1II1I1I
  if 57 - 57: i1iIi / o0ii1I % I11i % Ii
  if 95 - 95: i1IiiiI1iI - I11i
def iiI1 ( ) :
 if 65 - 65: Ii - ii / o0o00Oo0O * III1iiIii % Iii
 o00o00 ( '[COLOR darkgoldenrod]By Category[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 o00o00 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 72 - 72: ooOoO0O00
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 21 - 21: i1IiiiI1iI . oooOo0oo0oo / Ii * ooOoO0O00
def O00O0ooo00OO0 ( ) :
 o00o00 ( 'Search Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 o00o00 ( 'Search TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 63 - 63: Iii * IIiIiII11i
 I1iI1ii1II ( 'movies' , 'MAIN' )
def oo00OO ( ) :
 if 63 - 63: oO0o % ooOoO0O00 - i1i1I1IIii1II
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 ooOO0o = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 12 - 12: ii + i1IiiiI1iI / oooOo0oo0oo / I1ii11iIi11i * IIiIiII11i - Ii1I
 for ii11I in ooOO0o :
  i1IiIiiiIIIIi = oO0 + ii11I + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( i1IiIiiiIIIIi )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iiIIIiIi1IIi , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
   if OO00o in iIIIiIi . lower ( ) :
    i11IIi1Iii1 ( iIIIiIi , oOOo0O00o , 222 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , O000OOO )
    if 19 - 19: ooOoO0O00 % oO0o - Ii1I . i1IiiiI1iI . o0ii1I
    I1iI1ii1II ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 19 - 19: Ii1I / i1IiiiI1iI
    if 35 - 35: I1ii11iIi11i * i1i1I1IIii1II / ii + o0o00Oo0O / ii / oooOo0oo0oo
def IiO0o ( ) :
 if 69 - 69: i1i1I1IIii1II - i1IiiiI1iI / I1ii11iIi11i
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 ooOO0o = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 15 - 15: ooOoO0O00
 for ii11I in ooOO0o :
  I1iiIIiI11I = oO0 + ii11I + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( I1iiIIiI11I )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIIIiIi , O000OOO , oOOo0O00o , ooO0OO , IIo0o0O0O00oOOo , i1Ii11II in IIi :
   if OO00o in iIIIiIi . lower ( ) :
    o00o00 ( iIIIiIi , oOOo0O00o , i1Ii11II , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
    if 29 - 29: Iii + i1i1I1IIii1II % i1iIi + OOooOOo
    I1iI1ii1II ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 92 - 92: I11i
    if 37 - 37: i1i1I1IIii1II
def I1Ii1iI1IiI1I ( ) :
 if 95 - 95: Iii + I1ii11iIi11i + I1ii11iIi11i
 I1i111I = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , O000OOO , oOOo0O00o , ooO0OO , IIo0o0O0O00oOOo , i1Ii11II in IIi :
  o00o00 ( iIIIiIi , oOOo0O00o , i1Ii11II , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  I1iI1ii1II ( 'movies' , 'MAIN' )
def iiiii1II1I ( url ) :
 if 77 - 77: ooOoO0O00 - iI11I1II1I1I . oooOo0oo0oo
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IIiiIiIIiI1 = ( '%s%s' % ( I1IiI , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in IIi :
  ooOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for ooo00Ooo in ooOo00 :
   if ooo00Ooo == url :
    iIIIiIi = ( '[COLORred]Watched - [/COLOR]' + iIIIiIi ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  i11IIi1Iii1 ( iIIIiIi , url , 222 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
  if 79 - 79: OOooOOo + III1iiIii
  I1iI1ii1II ( 'movies' , 'MAIN' )
  if 14 - 14: i1IiiiI1iI / Iii - oooOo0oo0oo * o0o00Oo0O % III1iiIii . o0o00Oo0O
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 86 - 86: ooOoO0O00 * ii
  if 22 - 22: i1IiiiI1iI + IiI1i11I - Iii + iI11I1II1I1I / i1IiiiI1iI - ii
def IiII1111I ( url ) :
 if 15 - 15: iI11I1II1I1I % I1ii11iIi11i + ii
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , O000OOO , url , ooO0OO , IIo0o0O0O00oOOo , i1Ii11II in IIi :
  o00o00 ( iIIIiIi , url , i1Ii11II , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
  if 2 - 2: i1IiiiI1iI % ii - i1iIi * Ii1I * III1iiIii
  I1iI1ii1II ( 'movies' , 'MAIN' )
  if 99 - 99: iI11I1II1I1I . I1ii11iIi11i / i1iIi . oooOo0oo0oo % oOo0O0Ooo * Iii
  if 95 - 95: i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: III1iiIii
def i11IIi1Iii1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 42 - 42: ii * IIiIiII11i
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1I11iIiII . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OO0OO0OO = [ ]
  OO0OO0OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OO0OO0OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   OO0OO0OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1I11iIiII . addContextMenuItems ( OO0OO0OO )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = False )
 return iiIii1I
 if 53 - 53: i1IiiiI1iI + ooOoO0O00 . oO0o / Ii + o0ii1I % OOooOOo
def o00o00 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 9 - 9: i1iIi . Iii - I1ii11iIi11i . i1IiiiI1iI
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1I11iIiII . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OO0OO0OO = [ ]
  OO0OO0OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OO0OO0OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   OO0OO0OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1I11iIiII . addContextMenuItems ( OO0OO0OO )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = True )
 return iiIii1I
if 39 - 39: oooOo0oo0oo
if 70 - 70: III1iiIii % oO0o % oOo0O0Ooo
if 95 - 95: OOooOOo - i1IiiiI1iI / o0o00Oo0O * oOo0O0Ooo - I11i
if 12 - 12: iI11I1II1I1I % I1ii11iIi11i . IiI1i11I . III1iiIii % Ii
if 2 - 2: i1i1I1IIii1II * i1i1I1IIii1II . OOooOOo * o0ii1I * iI11I1II1I1I
if 13 - 13: Iii / o0o00Oo0O . Ii * ooOoO0O00 % Ii
if 8 - 8: OOooOOo - ii
if 99 - 99: IIiIiII11i / III1iiIii % ii . Ii
if 18 - 18: I11i . i1iIi
if 70 - 70: ii . i1iIi / i1i1I1IIii1II . i1i1I1IIii1II - I11i
if 29 - 29: Iii % oooOo0oo0oo - i1iIi
if 26 - 26: o0o00Oo0O . Iii + IiI1i11I - o0ii1I . Iii
if 2 - 2: Ii1I . I1ii11iIi11i * oooOo0oo0oo % IIiIiII11i . IiI1i11I
if 46 - 46: OOooOOo + oOo0O0Ooo % ii * Ii - I1ii11iIi11i
if 47 - 47: IiI1i11I * OOooOOo * III1iiIii
def iIiii1IIi1I ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 18 - 18: o0o00Oo0O / iI11I1II1I1I + Ii + I1ii11iIi11i
def IiI1I1i1 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 Iii11I = [ ]
 try :
  if 2 - 2: i1i1I1IIii1II . oooOo0oo0oo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  iIiii1IIi1I ( 'Making Favorites File' )
  Iii11I . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  OoO0oO0oo0O = open ( i1I1iI , "w" )
  OoO0oO0oo0O . write ( json . dumps ( Iii11I ) )
  OoO0oO0oo0O . close ( )
 else :
  iIiii1IIi1I ( 'Appending Favorites' )
  OoO0oO0oo0O = open ( i1I1iI ) . read ( )
  ii1O0oOOo = json . loads ( OoO0oO0oo0O )
  ii1O0oOOo . append ( ( name , url , iconimage , fanart , mode ) )
  i1i11ii = open ( i1I1iI , "w" )
  i1i11ii . write ( json . dumps ( ii1O0oOOo ) )
  i1i11ii . close ( )
  if 33 - 33: oOo0O0Ooo * i1IiiiI1iI
  if 98 - 98: Ii1I - ii / oOo0O0Ooo . i1iIi - ooOoO0O00
def oOOoOo0OoOO ( ) :
 if os . path . exists ( i1I1iI ) == False :
  Iii11I = [ ]
  iIiii1IIi1I ( 'Making Favorites File' )
  Iii11I . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  OoO0oO0oo0O = open ( i1I1iI , "w" )
  OoO0oO0oo0O . write ( json . dumps ( Iii11I ) )
  OoO0oO0oo0O . close ( )
 else :
  OO00oIi = json . loads ( open ( i1I1iI ) . read ( ) )
  OOooooO0o0O0 = len ( OO00oIi )
  for oOooo0OO0O0 in OO00oIi :
   iIIIiIi = oOooo0OO0O0 [ 0 ]
   oOOo0O00o = oOooo0OO0O0 [ 1 ]
   iiIIIiIi1IIi = oOooo0OO0O0 [ 2 ]
   try :
    o0o0o0O0oo = oOooo0OO0O0 [ 3 ]
    if o0o0o0O0oo == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     o0o0o0O0oo = iiIIIiIi1IIi
    else :
     o0o0o0O0oo = IIo0o0O0O00oOOo
   try : i1iI1iIII = oOooo0OO0O0 [ 5 ]
   except : i1iI1iIII = None
   try : oo0Oo = oOooo0OO0O0 [ 6 ]
   except : oo0Oo = None
   if 13 - 13: III1iiIii . I1ii11iIi11i - Iii / i1i1I1IIii1II - I1ii11iIi11i - oOo0O0Ooo
   if oOooo0OO0O0 [ 4 ] == 0 :
    I1I1II1I11 ( iIIIiIi , oOOo0O00o , '' , iiIIIiIi1IIi , IIo0o0O0O00oOOo , '' , 'fav' )
   else :
    I1I1II1I11 ( iIIIiIi , oOOo0O00o , oOooo0OO0O0 [ 4 ] , iiIIIiIi1IIi , IIo0o0O0O00oOOo , '' , 'fav' )
    if 84 - 84: IIiIiII11i
def Oo0ooooO0o00 ( name ) :
 ii1O0oOOo = json . loads ( open ( i1I1iI ) . read ( ) )
 for iIIIIIi11Ii in range ( len ( ii1O0oOOo ) ) :
  if ii1O0oOOo [ iIIIIIi11Ii ] [ 0 ] == name :
   del ii1O0oOOo [ iIIIIIi11Ii ]
   i1i11ii = open ( i1I1iI , "w" )
   i1i11ii . write ( json . dumps ( ii1O0oOOo ) )
   i1i11ii . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 92 - 92: i1i1I1IIii1II / Ii1I
 if 6 - 6: Ii / ooOoO0O00 / III1iiIii . oOo0O0Ooo - oooOo0oo0oo % Ii
def Ii1iiI1i1 ( ) :
 o0OoOoOo0O = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 IiIOOOoo = open ( o0OoOoOo0O , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 IiIOOOoo . write ( r'[' + IiII + ']' + '\n' )
 for iIIIiIi , ooO0OO , ooooo , oOOo0O00o in IIi :
  oOOo0O00o = ( oOOo0O00o + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  OOoo000o = ( iIIIiIi + '=plugin://' + IiII + '/?url=' + oOOo0O00o + '&mode=10012&name=' + ( iIIIiIi ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( ooO0OO ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( ooO0OO ) . replace ( ' ' , '' ) + '+&amp;description=' )
  IiIOOOoo . write ( OOoo000o + '\n' )
  if 58 - 58: oooOo0oo0oo % IiI1i11I * o0o00Oo0O + Ii1I - III1iiIii
  if 26 - 26: ooOoO0O00 / oOo0O0Ooo / Iii + Iii
def i1II111iiii ( ) :
 I1i111I = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o in IIi :
  IiI11i1IIiiI ( '24/7' , oOOo0O00o , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 6 - 6: IIiIiII11i
def i1iII11IiI ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def iI1111i1i11Ii ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def IiiIi1III ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def iiIOoO0000oo0O0 ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  Ii1I1i ( iIIIiIi , ( oOOo0O00o ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def oOIIIi ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  Ii1I1i ( iIIIiIi , oOOo0O00o , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 44 - 44: Ii / oooOo0oo0oo * i1iIi
  if 88 - 88: ooOoO0O00 % oooOo0oo0oo / ii * IiI1i11I % i1iIi
def II1111iiI1II ( ) :
 if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - o0ii1I * iI11I1II1I1I
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / i1i1I1IIii1II * I11i + oooOo0oo0oo
def o0oOO00O000O0 ( ) :
 if 89 - 89: I11i - IIiIiII11i - i1IiiiI1iI - oooOo0oo0oo % OOooOOo % oOo0O0Ooo
 I1i111I = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi , o0ooO00O0O in IIi :
  I1I1II1I11 ( iIIIiIi + '  -  ' + ( o0ooO00O0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOOo0O00o , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 84 - 84: I11i * ooOoO0O00 % I1ii11iIi11i
  if 41 - 41: i1i1I1IIii1II . IiI1i11I + ii * o0ii1I . I11i
  if 11 - 11: o0o00Oo0O
def o0Oo0o ( ) :
 if 4 - 4: ii
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
 if 78 - 78: IIiIiII11i
def oO0oOo ( url ) :
 i1ii1ii1II1 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( i1ii1ii1II1 )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 43 - 43: i1i1I1IIii1II + OOooOOo . oOo0O0Ooo . Ii
  if 71 - 71: I11i + oooOo0oo0oo . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
  if 91 - 91: o0o00Oo0O - Iii % i1IiiiI1iI
  if 46 - 46: i1iIi / oOo0O0Ooo . III1iiIii % oO0o / Ii
def I1III1I1IiI ( ) :
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 oOOo0O00o = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OO00o ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( oOOo0O00o )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  if OO00o in iIIIiIi . lower ( ) :
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 11 - 11: IiI1i11I
   if 20 - 20: o0ii1I . i1IiiiI1iI % o0ii1I
   if 5 - 5: oooOo0oo0oo + IiI1i11I
def i1ii11III1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0000o00O , oO0O , IIiIiIIii1 , iIIIiIi in IIi :
  i11iiIII1Iii1 = ( IIiIiIIii1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iiii1ii1 = ( oO0O ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Ii1i111iI = 'Season ' + iiii1ii1 + 'Episode ' + i11iiIII1Iii1 + iIIIiIi
  iII1ii ( Ii1i111iI , ooO0000o00O )
  if 51 - 51: I11i . Ii1I * o0ii1I / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 44 - 44: Ii % i1IiiiI1iI % i1i1I1IIii1II + Iii * i1i1I1IIii1II . o0ii1I
  if 89 - 89: ii % IIiIiII11i - oO0o % Ii
def iII1ii ( name , url ) :
 ooO0000o00O = url
 iiIIII11iIii = name
 o0o = cloudflare . source ( ooO0000o00O )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for III1I1Ii11iI , O0000O in i1Iii1i1I :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iiIIII11iIii + O0000O + '[/COLOR]' , III1I1Ii11iI , 222 , iiIi1IIiIi + 'dtv.png' )
  if 67 - 67: o0o00Oo0O + oOo0O0Ooo + i1i1I1IIii1II - IIiIiII11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 27 - 27: I11i / oOo0O0Ooo
 if 91 - 91: oOo0O0Ooo - IiI1i11I / oO0o - oO0o / o0ii1I - III1iiIii
def oo00O00oO000o ( ) :
 if 14 - 14: oooOo0oo0oo / I11i + o0ii1I / ii - Iii
 if 88 - 88: o0ii1I / ii % OOooOOo - ooOoO0O00
 if 49 - 49: I11i - iI11I1II1I1I
 if 61 - 61: IiI1i11I * i1iIi
 if 1 - 1: i1IiiiI1iI * OOooOOo
 if 100 - 100: Ii1I / o0o00Oo0O / i1iIi + Ii1I
 if 48 - 48: ii . IiI1i11I + o0o00Oo0O
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 85 - 85: IIiIiII11i - o0ii1I
def O0OoIIiII ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIii11iI1i1 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + ooO0OO , '' , '' )
 for url in IiIii11iI1i1 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 98 - 98: o0o00Oo0O + IiI1i11I
def iiiiIIIi ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIii11iI1i1 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  ooO0OO = 'http://watchepisodes.cc/' + ooO0OO
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 10093 , ooO0OO , ooO0OO , '' )
 for url in IiIii11iI1i1 :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 11 - 11: Iii
def IIIIi1 ( url , iconimage ) :
 ooO0OO = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IIiIiIIii1 , url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + IIiIiIIii1 + ' - ' + iIIIiIi + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , ooO0OO , '' , '' )
  if 50 - 50: oOo0O0Ooo - i1i1I1IIii1II + i1i1I1IIii1II * Iii + i1i1I1IIii1II
def oooOoooOOo0 ( url , iconimage ) :
 ooO0OO = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  if 'player' in iIIIiIi :
   pass
  elif 'vod' in iIIIiIi :
   I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , ooO0OO , '' , '' )
   if 25 - 25: IiI1i11I + oOo0O0Ooo + OOooOOo + i1IiiiI1iI % o0o00Oo0O
   if 26 - 26: i1iIi + OOooOOo
   if 17 - 17: Ii1I - IiI1i11I % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * oooOo0oo0oo
   if 6 - 6: i1IiiiI1iI
   if 46 - 46: IIiIiII11i * i1IiiiI1iI
   if 23 - 23: ooOoO0O00 - o0o00Oo0O
def OOo00OoO ( ) :
 if 6 - 6: i1iIi % ii * i1IiiiI1iI - III1iiIii
 if 24 - 24: Iii / iI11I1II1I1I . ii % OOooOOo . o0ii1I
 if 73 - 73: i1IiiiI1iI
 if 25 - 25: III1iiIii
 if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . o0ii1I - I1ii11iIi11i . Ii
 if 47 - 47: I1ii11iIi11i % oO0o - i1iIi - I1ii11iIi11i * i1i1I1IIii1II
 if 72 - 72: I11i % I11i + IiI1i11I + Ii1I / I1ii11iIi11i
 if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
 if 64 - 64: III1iiIii
 if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
 if 89 - 89: o0o00Oo0O + III1iiIii * i1IiiiI1iI
 if 30 - 30: OOooOOo
 if 39 - 39: Ii1I + I11i + i1IiiiI1iI + III1iiIii
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 48 - 48: i1IiiiI1iI / i1iIi . iI11I1II1I1I
 if 72 - 72: ooOoO0O00 . I11i
def iIIiiIiII1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00OooOo00o = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( O00OooOo00o ) )
 for url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 78 - 78: o0o00Oo0O - i1IiiiI1iI * oooOo0oo0oo + Iii + IIiIiII11i
def IIIiiII1iIi1ii1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 49 - 49: OOooOOo
def OoO0O00 ( url ) :
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
  if 96 - 96: III1iiIii - IiI1i11I
  if 34 - 34: oooOo0oo0oo - Ii1I * IiI1i11I % o0ii1I
def Ii1i11i ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O0o = 'http://www.watchseriesgo.to/search/' + OO00o . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( O0O0o )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , oOOo0O00o , iIIIiIi in IIi :
  if 'watch online' in iIIIiIi :
   pass
  else :
   print oOOo0O00o
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.watchseriesgo.to' + oOOo0O00o , 10044 , ooO0OO , '' , '' )
   if 96 - 96: o0o00Oo0O . I1ii11iIi11i - Iii
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 42 - 42: ii . OOooOOo
def o0O0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , IIiIiIIii1 , O000OOO in IIi :
  oo0000Oo00o = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( IIiIiIIii1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + oo0000Oo00o + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , ooO0OO , '' , O000OOO )
  if 48 - 48: i1IiiiI1iI
def iI1II1iIiiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  oo0000Oo00o = ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + oo0000Oo00o + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 9 - 9: o0ii1I
def Ii11I1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , ooO0OO , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 18 - 18: i1iIi
def IIIi1iiI1I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O00OooOo00o = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0O , IiiI1Ii1II in O00OooOo00o :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( IiiI1Ii1II ) )
  for url , iIIIiIi in IIi :
   oo0000Oo00o = ( oO0O ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + oo0000Oo00o + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 20 - 20: i1iIi + iI11I1II1I1I
class O0ooOoO0 ( ) :
 if 10 - 10: Ii % oooOo0oo0oo * IiI1i11I % I1ii11iIi11i
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 51 - 51: oO0o % IiI1i11I
  oo0000Oo00o = name
  self . Get_Sources ( oOOo0O00o , oo0000Oo00o )
  if 24 - 24: oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . iI11I1II1I1I - oO0o . iI11I1II1I1I
  if 8 - 8: Ii1I % oO0o % i1i1I1IIii1II . Ii1I * Ii1I
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iIIIiIi in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + oOOo0O00o
   self . Get_site_link ( URL , season_name )
   if 94 - 94: Ii + ii
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
   if 20 - 20: Ii
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   oOOO = 'DACLIPS'
   if oOOO in O0ooOoO0 . source_list :
    pass
   else :
    self . daclips ( url , season_name , oOOO )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    oOOO = 'THEVIDEO'
    if oOOO in O0ooOoO0 . source_list :
     pass
    else :
     self . thevideo ( url , season_name , oOOO )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     oOOO = 'ALLMYVIDEOS'
     if oOOO in O0ooOoO0 . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , oOOO )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      oOOO = 'VIDSPOT'
      if oOOO in O0ooOoO0 . source_list :
       pass
      else :
       self . vidspot ( url , season_name , oOOO )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       oOOO = 'VODLOCKER'
       if oOOO in O0ooOoO0 . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , oOOO )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        oOOO = 'VIDTO'
        if oOOO in O0ooOoO0 . source_list :
         pass
        else :
         self . vidto ( url , season_name , oOOO )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 71 - 71: oOo0O0Ooo . i1iIi
       else :
        if 'youwatch' in url :
         oOOO = 'YouWatch'
         if oOOO in O0ooOoO0 . source_list :
          pass
         else :
          self . youwatch ( url , season_name , oOOO )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 43 - 43: Ii1I * oooOo0oo0oo
          if 1 - 1: oO0o * i1iIi + III1iiIii . i1i1I1IIii1II / i1iIi
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OO00oOooo0O , iIIIiIi in IIi :
   self . Printer ( OO00oOooo0O , season_name , source_name )
   if 91 - 91: o0ii1I + Iii - I1ii11iIi11i % OOooOOo . IiI1i11I
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for OO00oOooo0O , iIIIiIi in IIi :
   self . Printer ( OO00oOooo0O , season_name , source_name )
   if 51 - 51: oooOo0oo0oo / Iii
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for OO00oOooo0O in IIi :
   self . Printer ( OO00oOooo0O , season_name , source_name )
   if 51 - 51: i1iIi * i1i1I1IIii1II - i1IiiiI1iI + IiI1i11I
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for OO00oOooo0O in IIi :
   self . Printer ( OO00oOooo0O , season_name , source_name )
   if 46 - 46: I11i - Ii % oO0o / o0ii1I - OOooOOo
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for OO00oOooo0O in IIi :
   self . Printer ( OO00oOooo0O , season_name , source_name )
   if 88 - 88: i1i1I1IIii1II * oOo0O0Ooo / oO0o - oooOo0oo0oo / ooOoO0O00 . i1IiiiI1iI
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for OO00oOooo0O in IIi :
   self . Printer ( OO00oOooo0O , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for OO00oOooo0O in IIi :
   self . Printer ( OO00oOooo0O , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for OO00oOooo0O in IIi :
   self . youplay ( OO00oOooo0O , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for OO00oOooo0O in IIi :
   self . Printer ( OO00oOooo0O , season_name , source_name )
   if 26 - 26: Ii - i1iIi
 def Printer ( self , Link , season_name , source_name ) :
  if 45 - 45: i1iIi + IIiIiII11i % IiI1i11I
  if Link in O0ooOoO0 . List :
   pass
  elif source_name in O0ooOoO0 . source_list :
   pass
  else :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   O0ooOoO0 . List . append ( Link )
   O0ooOoO0 . source_list . append ( source_name )
   if 55 - 55: i1iIi - i1i1I1IIii1II % oOo0O0Ooo
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 61 - 61: i1iIi
   if 22 - 22: iI11I1II1I1I / i1iIi / oOo0O0Ooo - I11i
   if 21 - 21: i1i1I1IIii1II . Ii * Iii . oooOo0oo0oo / oooOo0oo0oo
   if 42 - 42: ii / i1IiiiI1iI . I11i / o0o00Oo0O - III1iiIii * III1iiIii
   if 1 - 1: o0ii1I % i1IiiiI1iI
def iI111i1II ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 97 - 97: OOooOOo
def IIi1ii1IIi1 ( url ) :
 O000oOO0o = '20'
 OOO0oO = [ ]
 oO00 = '                                                    '
 II1IoooOoO00O = '        '
 I1I1II1I11 ( oO00 + 'pl' + II1IoooOoO00O + 'w' + II1IoooOoO00O + 'd' + II1IoooOoO00O + 'l' + II1IoooOoO00O + 'f' + II1IoooOoO00O + 'a' + II1IoooOoO00O + 'pts' , '' , '' , '' , '' , '' )
 I1i111I = oO0o0O0Ooo0o ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( I1i111I )
 for I1i1IIiiI11II , Ii1i1 , iiiIiIIiIiiii , oOo00OO0ooOOO , o00O0OooO0 , O0oO0 , OoO0oO0oo0O , iii1II11II1 , I11i1Iii1I in IIi :
  iIIiII1 = iI1Iii1i1 ( Ii1i1 )
  OoOo00oOoo0oO = iI1Iii1i1 ( iiiIiIIiIiiii )
  i1ii1iIII = iI1Iii1i1 ( oOo00OO0ooOOO )
  ooooooo0000oo0 = iI1Iii1i1 ( o00O0OooO0 )
  O0oooo000o = iI1Iii1i1 ( O0oO0 )
  IIiIiI11II = iI1Iii1i1 ( OoO0oO0oo0O )
  OOO0oO . append ( I1i1IIiiI11II [ 0 ] )
  oOo00 = len ( OOO0oO )
  OoooI1iIiii = int ( len ( oO00 ) - len ( I1i1IIiiI11II ) - 2 )
  if len ( OOO0oO ) >= 10 :
   OoooI1iIiii = OoooI1iIiii - 1
  if len ( OOO0oO ) <= int ( O000oOO0o ) :
   Ii1I1i ( str ( oOo00 ) + ' ' + I1i1IIiiI11II + oO00 [ 0 : OoooI1iIiii ] + Ii1i1 + iIIiII1 + iiiIiIIiIiiii + OoOo00oOoo0oO + oOo00OO0ooOOO + i1ii1iIII + o00O0OooO0 + ooooooo0000oo0 + O0oO0 + O0oooo000o + OoO0oO0oo0O + IIiIiI11II + ' ' + I11i1Iii1I , '' , '' , '' , '' , '' )
   if 87 - 87: IIiIiII11i * oO0o + o0ii1I . I1ii11iIi11i - Ii1I * i1i1I1IIii1II
   if 15 - 15: IIiIiII11i + o0o00Oo0O
def iI1Iii1i1 ( space ) :
 if len ( space ) > 1 :
  i1IIOo0 = len ( '        ' ) - len ( space ) + 1
  space = int ( i1IIOo0 ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 87 - 87: oO0o / i1iIi . III1iiIii . IIiIiII11i
def I1I11I1i1i1II ( ) :
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
 if 8 - 8: I11i
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
 if 48 - 48: o0ii1I - ii + i1IiiiI1iI % I11i - OOooOOo . oOo0O0Ooo
 if 42 - 42: i1IiiiI1iI
 if 70 - 70: I11i / Iii + i1i1I1IIii1II % oOo0O0Ooo % I1ii11iIi11i + oO0o
 if 80 - 80: oooOo0oo0oo
 if 12 - 12: o0ii1I
 if 2 - 2: ii
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
 if 46 - 46: o0o00Oo0O % ii
 if 22 - 22: IiI1i11I + ii - OOooOOo - oO0o * i1IiiiI1iI - i1i1I1IIii1II
 if 99 - 99: i1iIi / oOo0O0Ooo . o0ii1I - o0ii1I * oOo0O0Ooo
 if 24 - 24: Iii * oO0o - i1i1I1IIii1II / iI11I1II1I1I - I1ii11iIi11i . oooOo0oo0oo
 if 2 - 2: i1iIi - o0o00Oo0O - Ii1I / Iii * OOooOOo
 if 26 - 26: Ii1I + i1IiiiI1iI - i1i1I1IIii1II + III1iiIii % oooOo0oo0oo
 if 84 - 84: Iii % o0ii1I % o0o00Oo0O * I11i
 if 15 - 15: i1i1I1IIii1II - iI11I1II1I1I - IIiIiII11i - III1iiIii % Ii1I
 if 80 - 80: III1iiIii * IiI1i11I . ooOoO0O00 % o0ii1I % Ii1I + i1iIi
 if 6 - 6: Ii1I . i1i1I1IIii1II . oO0o + III1iiIii
 if 65 - 65: Ii1I / i1iIi
 if 23 - 23: oooOo0oo0oo / oooOo0oo0oo * I11i * oooOo0oo0oo
 if 57 - 57: IiI1i11I
 if 29 - 29: oOo0O0Ooo
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOOo0O00o , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ooO0OO , Oo00OOOOO , '' )
  if 41 - 41: i1IiiiI1iI * oO0o - IiI1i11I . o0ii1I
def IiIiIIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00OooOo00o = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O00OooOo00o in O00OooOo00o :
  Ii1i1I1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( O00OooOo00o ) )
  for o0o0000o in Ii1i1I1 :
   o0o0000o = o0o0000o
  I11i11i111i1 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( O00OooOo00o ) )
  for II1I1i1I , ooO0OO , time , Ii1iIi111i1i1 in I11i11i111i1 :
   o0Oo0 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( Ii1iIi111i1i1 )
   I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + o0o0000o + ' - ' + II1I1i1I + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + ooO0OO , Oo00OOOOO , ( str ( o0Oo0 ) ) )
   if 21 - 21: ii
 I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if 62 - 62: Ii % I1ii11iIi11i * i1i1I1IIii1II . i1i1I1IIii1II . o0o00Oo0O
def ooOoOO ( ) :
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
 if 42 - 42: Iii
def iIi1I ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  i1IIIi111111 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIIIiIi :
   pass
  else :
   i1IIIi111111 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + i1IIIi111111 + '[/COLOR]' , url , 10013 , ooO0OO )
 for url , ooO0OO , iIIIiIi in i1Iii1i1I :
  i1IIIi111111 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIIIiIi :
   pass
  else :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + i1IIIi111111 + '[/COLOR]' , url , 10013 , ooO0OO )
def O0Ii1iIii1I1 ( url ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 21 - 21: OOooOOo + OOooOOo * i1iIi / oooOo0oo0oo * ii . I1ii11iIi11i
 if 22 - 22: i1iIi % OOooOOo / I11i
 if 98 - 98: oO0o / I11i * oOo0O0Ooo
 if 60 - 60: Ii1I / III1iiIii . Ii / oO0o % IIiIiII11i
 if 6 - 6: IiI1i11I % I11i + i1IiiiI1iI
 if 91 - 91: I11i + o0o00Oo0O * i1i1I1IIii1II * III1iiIii * Ii1I
 if 83 - 83: ii
 for url , ooO0OO , iIIIiIi in i1Iii1i1I :
  i1IIIi111111 = iIIIiIi . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIIIiIi :
   pass
  else :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + i1IIIi111111 + '[/COLOR]' , url , 10013 , ooO0OO )
   if 52 - 52: I11i / OOooOOo % i1i1I1IIii1II % oO0o / III1iiIii % I11i
def O0ooIi1I1I11I1I1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for III1I1Ii11iI in IIi :
  I1II1i = ( III1I1Ii11iI ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OoO00oo00 ( 'http:' + I1II1i )
  if 63 - 63: i1iIi . oooOo0oo0oo
  if 66 - 66: oOo0O0Ooo
  if 99 - 99: oO0o % o0o00Oo0O . i1IiiiI1iI - Ii1I . I1ii11iIi11i / OOooOOo
  if 60 - 60: Ii1I
def oOoOoo0 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  oOOo000oOoO0 ( iIIIiIi , url , 8046 , ooO0OO )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def iIO0O0Ooo0 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  OoO00oo00 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 34 - 34: i1i1I1IIii1II - IIiIiII11i - I11i + IiI1i11I + i1IiiiI1iI
def oo0OOo ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I1i111I )
 for url in IIi :
  yt . PlayVideo ( url )
  if 77 - 77: i1i1I1IIii1II . o0ii1I / o0o00Oo0O * i1i1I1IIii1II
def ii11i11i1 ( ) :
 IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , oOOo0O00o , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOoO0O0o ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + ooO0OO )
 for url in next :
  IiI11i1IIiiI ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 84 - 84: OOooOOo - Iii
  if 80 - 80: Ii % oooOo0oo0oo - I1ii11iIi11i % oooOo0oo0oo
def O0O0oOo0o0o0 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i111I )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def oOOOIii111111 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , '' )
  if 23 - 23: i1IiiiI1iI - iI11I1II1I1I - IIiIiII11i + i1IiiiI1iI % o0ii1I / Iii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0o0o0OO0o00 ( name , url ) :
 IiII11 = 0
 name = name
 url = url
 oOOoo00O00o = [ '144' , '240' , '380' , '480' , '720' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  I11iiiiI1i ( url )
  if 56 - 56: oOo0O0Ooo
  if 49 - 49: ooOoO0O00 % i1i1I1IIii1II / oooOo0oo0oo . Ii1I - i1IiiiI1iI
  if 12 - 12: Ii + Iii - Ii1I
  if 27 - 27: IiI1i11I
  if 22 - 22: OOooOOo / oOo0O0Ooo
  if 33 - 33: Iii
  if 37 - 37: OOooOOo % I11i * oO0o / Ii * IIiIiII11i * IiI1i11I
  if 70 - 70: i1iIi . Ii % OOooOOo + i1i1I1IIii1II
def oOo0oOoo0 ( ) :
 I1i111I = ii1IIIIiI11 ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  if 'genre' in oOOo0O00o :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oOOo0O00o , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oooo00 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , ooO0OO )
 for url in next :
  IiI11i1IIiiI ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 43 - 43: oOo0O0Ooo
def OOOooOOO00O ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( I1i111I )
 for url in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  oOOOIii111111 ( url )
  if 34 - 34: o0ii1I * Iii / ii - iI11I1II1I1I
def O0Ooo00o0OoOo ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIIi1iiII = 'http://documentarylovers.com/?s=' + ( OO00o ) . replace ( ' ' , '+' )
 OOOOoOO0O = iIIi1iiII . lower ( )
 Oooo00 ( OOOOoOO0O )
 if 96 - 96: III1iiIii
def O0ooOooOOoo ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if 'films' in url :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def III1II11 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  if 'films' in url :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + ooO0OO )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def iI1IiiII1 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1i111I )
 for url in IIi :
  if 'rtd' in url :
   i1I1 ( url )
   if 18 - 18: Iii % o0o00Oo0O / iI11I1II1I1I / IiI1i11I
def i1I1 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( I1i111I )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  I11iiiiI1i ( url )
  if 1 - 1: I1ii11iIi11i . Ii
  if 9 - 9: ii / Iii
def iII ( ) :
 II11iIiIIIiI = ii1IIIIiI11 ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , ooO0OO , iIIIiIi , iIiIIi in IIi :
  IiI11i1IIiiI ( ( iIIIiIi + '[COLOR' + ooOoOoo0O + ']' + iIiIIi + '[/COLOR]' ) , oOOo0O00o , 8086 , ooO0OO )
  if 9 - 9: III1iiIii % oOo0O0Ooo + Iii
def II11iII ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , ooO0OO , iIIIiIi in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 8087 , ooO0OO )
  if 78 - 78: III1iiIii + Iii - I11i + oO0o / iI11I1II1I1I
def ii111I111i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  II11111I ( url , iIIIiIi )
  if 59 - 59: Ii1I / ii / Iii - ooOoO0O00
def II11111I ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 58 - 58: Ii1I / oO0o / i1i1I1IIii1II + III1iiIii % IiI1i11I / IIiIiII11i
def Oo00Oo00Oooo ( ) :
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oOOo0O00o , 3002 , 'http://www.solie.org/alibrary/' + ooO0OO )
def iIIIiI1iII1i ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ooO0OO )
def Ii1I11Ii1iI ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 OOOOOo00OOoO = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I1i111I )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , iIIIiIi in OOOOOo00OOoO :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']Season- ' + iIIIiIi + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , ooO0OO , iIIIiIi in i1Iii1i1I :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ooO0OO )
def i111iii1I11I ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I1i111I )
 for url in IIi :
  iii111iiI11I ( url )
def iii111iiI11I ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I1i111I )
 for url in IIi :
  I11iiiiI1i ( url )
  if 35 - 35: oOo0O0Ooo
def OoOIiiiii111i1ii ( ) :
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOOo0O00o , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def IiIiiIIiIi ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( I1i111I )
 for url in IIi :
  i11i1i ( url )
  if 97 - 97: Ii
def oOoooo000Oo00 ( ) :
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOOo0O00o , 8065 , iiIi1IIiIi + 'classictv.png' )
def ii11 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  if 'mp4' in url :
   I11iiiiI1i ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 47 - 47: o0o00Oo0O - Iii - o0o00Oo0O
def iiioO000oO0oO ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oOOo0O00o , 8071 , iiIi1IIiIi + 'streams.png' )
def iII111i1 ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIIIiIi , url in IIi :
  if '(Free Access)' in iIIIiIi :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def i11Ii ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , ooO0OO , IIo0o0O0O00oOOo , '' )
  if 34 - 34: oooOo0oo0oo
def oo0O0 ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  I1i1I1i1Ii ( 'http://watchxxxfree.com/categories' )
 if O0O00Oo == 1 :
  oooOOoO ( 'http://www.perfectgirls.net' )
 if O0O00Oo == 2 :
  Ii11 ( 'http://www.xvideos.com/best' )
 if O0O00Oo == 3 :
  o0OOooOoOo00O ( 'http://www.xvideos.com/best' )
 if O0O00Oo == 4 :
  Ii11 ( 'http://www.xvideos.com/best' )
 if O0O00Oo == 5 :
  Ii11 ( 'http://www.xvideos.com/verified/videos' )
 if O0O00Oo == 6 :
  oooOo000O ( 'http://www.xvideos.com/tags' )
 if O0O00Oo == 7 :
  IiiI1 ( 'http://www.xvideos.com/porn' )
 if O0O00Oo == 8 :
  iII1iiI11IIi ( )
  if 25 - 25: IiI1i11I . oO0o / iI11I1II1I1I
  if 56 - 56: I11i % Ii . o0ii1I * iI11I1II1I1I - I1ii11iIi11i
  if 77 - 77: ii
  if 52 - 52: IiI1i11I - oO0o % Ii . Iii
  if 98 - 98: ii + OOooOOo . OOooOOo / o0o00Oo0O / Ii
  if 88 - 88: IIiIiII11i - IiI1i11I / ii
  if 71 - 71: Ii1I
  if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
  if 1 - 1: III1iiIii % ooOoO0O00
def IIiII1iII11Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  if 'ch' in url :
   iiiO000OOO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def oooO00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 OooO0o000Oo = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for iIIIiIi , url in OooO0o000Oo :
  I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def ii1iII1i111II ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   OoO00OOoO ( url )
def iiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiiiI1i ( url )
def I1i1I1i1Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , i1IIOo0 in IIi :
  if 'category' in url :
   iiiO000OOO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORorange]   ' + i1IIOo0 + '[/COLOR]' , url , 90006 , ooO0OO , iiIi1IIiIi + 'Jizbox.png' , '' )
def iii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OooO0o000Oo = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi in IIi :
  Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , ooO0OO , '' , '' )
 for url in OooO0o000Oo :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OO00Oo00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   OoO00OOoO ( url )
def OoO00OOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I11iiiiI1i ( url )
def oooOOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , i1IIOo0 in IIi :
  if 'category' in url :
   iiiO000OOO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORorange]' + i1IIOo0 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def IiII1Iiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 ooO0000o00O = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OooO0o000Oo = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , ooO0OO , '' , '' )
 for url in OooO0o000Oo :
  I1I1II1I11 ( '[COLORred]NEXT[/COLOR]' , ooO0000o00O + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def I1o000o00OO00Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  I1II11I11111i ( 'http://www.perfectgirls.net' + url )
def I1II11I11111i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OoO00oo00 ( 'http://' + url )
def IiiI1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , i1IIOo0 in IIi :
  iiiO000OOO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - No of Videos : [COLORorange]' + i1IIOo0 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def oooOo000O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OooO0o000Oo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in OooO0o000Oo :
  iiiO000OOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , i1IIOo0 in IIi :
  iiiO000OOO ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - No of Videos : [COLORorange]' + ( i1IIOo0 + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 14 - 14: III1iiIii + I11i + Ii1I * I11i + oO0o
def iiiIIi11IiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OooO0o000Oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in OooO0o000Oo :
  iiiO000OOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , Iii1oooo00Oo0O in IIi :
  iiiO000OOO ( iIIIiIi + '--' + ( Iii1oooo00Oo0O ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( ooO0OO ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 10 - 10: ii . oooOo0oo0oo * o0ii1I - Ii1I
  if 43 - 43: Iii . i1IiiiI1iI + IiI1i11I % o0o00Oo0O - I1ii11iIi11i . Iii
def Ii11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , url , iIIIiIi , III1i , IIIi1Iii11I in IIi :
  iiiO000OOO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - Porn Quality : [COLORorange]' + IIIi1Iii11I + ' - [COLORred]' + III1i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , ooO0OO , ooO0OO , IIIi1Iii11I + ' - ' + III1i )
 i1IOoO000oOO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in i1IOoO000oOO :
  iiiO000OOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 25 - 25: Ii - OOooOOo
def o0OOooOoOo00O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O00OooOo00o = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OooO0o000Oo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in OooO0o000Oo :
  iiiO000OOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( O00OooOo00o ) )
 for url , iIIIiIi in IIi :
  if '/c/' in url :
   iiiO000OOO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 32 - 32: Ii
   if 57 - 57: iI11I1II1I1I
def iII1iiI11IIi ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOO0oOO = ( OO00o ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OOOOoOO0O = o0OOoOO0oOO . lower ( )
 oO0O00oO0o0 = 'http://www.xvideos.com/?k=' + OOOOoOO0O
 print oO0O00oO0o0 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( oO0O00oO0o0 )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , oOOo0O00o , iIIIiIi , III1i , IIIi1Iii11I in IIi :
  iiiO000OOO ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgreen] - Porn Quality : [COLORorange]' + IIIi1Iii11I + ' - [COLORred]' + III1i + '[/COLOR]' , 'http://www.xvideos.com' + oOOo0O00o , 10108 , ooO0OO , ooO0OO , IIIi1Iii11I + ' - ' + III1i )
 i1IOoO000oOO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in i1IOoO000oOO :
  iiiO000OOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oOOo0O00o , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 51 - 51: iI11I1II1I1I * OOooOOo / o0ii1I * oO0o
if 58 - 58: o0o00Oo0O - ooOoO0O00 / IiI1i11I
if 59 - 59: I1ii11iIi11i % Ii1I % i1iIi % Iii * iI11I1II1I1I
if 22 - 22: oOo0O0Ooo * Ii * Ii1I / oOo0O0Ooo . IiI1i11I
if 3 - 3: i1IiiiI1iI
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
if 17 - 17: IIiIiII11i / i1iIi
if 80 - 80: oooOo0oo0oo * oO0o + o0ii1I
if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
if 98 - 98: I11i * I1ii11iIi11i - o0ii1I . i1iIi
if 2 - 2: I1ii11iIi11i - i1iIi % iI11I1II1I1I
if 88 - 88: i1IiiiI1iI - oO0o
if 79 - 79: IiI1i11I
if 45 - 45: IIiIiII11i + IiI1i11I . Iii . o0o00Oo0O * ooOoO0O00 - o0ii1I
if 48 - 48: Ii1I + I1ii11iIi11i
if 76 - 76: Ii1I
def OoOooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 ii1I1IIii11 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in ii1I1IIii11 :
  if 'http' in url :
   oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 76 - 76: I1ii11iIi11i * i1iIi % oooOo0oo0oo . oO0o
def iIii1i1i1 ( url ) :
 ii1IiIiI1 = xbmc . Player ( OOOoOo00O ( ) )
 import urlresolver
 try : ii1IiIiI1 . play ( url )
 except : pass
 if 45 - 45: Iii - oooOo0oo0oo * IiI1i11I - oO0o . o0ii1I
 if 77 - 77: i1i1I1IIii1II / Iii
def iIIiiI1Ii1II ( ) :
 if 25 - 25: oOo0O0Ooo
 if 64 - 64: i1i1I1IIii1II
 if 80 - 80: I11i % iI11I1II1I1I
 if 63 - 63: III1iiIii * Ii
 if 86 - 86: Iii % Iii - OOooOOo + i1IiiiI1iI / oOo0O0Ooo * ii
 if 26 - 26: IIiIiII11i * IiI1i11I + I11i / o0o00Oo0O + ooOoO0O00 - Iii
 if 56 - 56: oooOo0oo0oo
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + III1iiIii - Iii
 if 81 - 81: Ii1I + ii - oooOo0oo0oo * o0o00Oo0O
 if 100 - 100: iI11I1II1I1I - OOooOOo
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 8091 , iiIi1IIiIi + 'gofish.png' )
def iIiI1Iii11II ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIIIiIi , ooO0OO in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 8092 , ooO0OO )
 for url in next :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def ii11III1 ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOOoO0oo0oo0o = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO in OOOoO0oo0oo0o :
  ooO0OO = ooO0OO
 for url , iIIIiIi in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 8092 , ooO0OO )
 for url in next :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 70 - 70: iI11I1II1I1I + I11i * i1i1I1IIii1II
def OOOoooO0o0o ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 56 - 56: i1i1I1IIii1II - I11i . OOooOOo . o0ii1I + i1i1I1IIii1II * ii
  if 31 - 31: IiI1i11I - Ii % o0ii1I / IiI1i11I . ii + I1ii11iIi11i
  if 82 - 82: Ii1I * o0o00Oo0O + oooOo0oo0oo . i1iIi + oO0o % o0o00Oo0O
  if 2 - 2: IIiIiII11i * o0o00Oo0O . i1iIi * ooOoO0O00
IiI1I1II = '{PQ},' ; IIIiiIIIiI1 = '{SC},' ; OOOoO0O0 = '{XG},' ; iII1I1iIi1i = '{JP},' ; O0OO0o = '{HW},' ; Ii11IiiI = '{RT},'
def OoOo0oOooOoOO ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOO0ooOoO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 oOOo0O00o = 'http://onlinemovies.tube/?s=' + ( OO00o ) . replace ( ' ' , '+' )
 ooO0000o00O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvc2VhcmNobW92aWVzLnBocA==' ) )
 O0Ooo = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 IIiIIIIii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 iIiI1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIIiI1ii = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + OO00o
 oo0OOoOoo0O0O = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iiI11ii1111 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 34 - 34: OOooOOo * OOooOOo
 ooOOooo0Oo = ( i11 ( 'http://genietvcunts.co.uk/herovision/vod/movfull.php' ) )
 oo0O0o = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 71 - 71: IIiIiII11i . o0ii1I - oooOo0oo0oo . Ii1I * IIiIiII11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 o0o = O00O0oOO00O00 ( ooO0000o00O )
 o0oOoO00o . update ( 14 , "" , "Checking Source Technica " )
 O0oOoo0OoO0O = O00O0oOO00O00 ( ooO0000o00O )
 o0oOoO00o . update ( 32 , "" , "Checking Source Pandoras Box " )
 o00OooOO000 = O00O0oOO00O00 ( O0Ooo )
 o0oOoO00o . update ( 59 , "" , "Checking Source Lazy List " )
 OOoOoo = O00O0oOO00O00 ( oO00oOOo0Oo )
 o0oOoO00o . update ( 72 , "" , "Checking Source RaizTv " )
 oo00IiI1 = O00O0oOO00O00 ( iiI11ii1111 )
 o0oOoO00o . update ( 91 , "" , "Checking WebSpace " )
 if 61 - 61: oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
 if 45 - 45: i1IiiiI1iI * Iii / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
 if 49 - 49: o0ii1I / IiI1i11I . IiI1i11I . IiI1i11I + Ii % Iii
 if 7 - 7: III1iiIii * i1iIi + OOooOOo
 if 22 - 22: IiI1i11I
 if 48 - 48: Ii1I . oOo0O0Ooo
 if 73 - 73: o0o00Oo0O . i1IiiiI1iI - ii % Iii % ooOoO0O00
 if 14 - 14: i1IiiiI1iI + o0ii1I * I1ii11iIi11i
 o0Oo = O00O0oOO00O00 ( oo0O0o )
 if 49 - 49: I1ii11iIi11i
 if oo00IiI1 != 'Failed' :
  i1IIi1i1Ii1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oo00IiI1 )
  for oOOo0O00o , iIIIiIi in i1IIi1i1Ii1 :
   Iiio0Oo0oO = O00O0oOO00O00 ( oOOo0O00o )
   iIII1iiIi11 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Iiio0Oo0oO )
   for ooOo0O0O0oOO0 , iIiIIi in iIII1iiIi11 :
    iIiIIi = ( iIiIIi . replace ( '.' , ' ' ) )
    if OOOOoOO0O in iIiIIi . lower ( ) :
     if '.mkv' in ooOo0O0O0oOO0 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + ooOo0O0O0oOO0 , 222 , '' , '' , '' )
     elif '.mp4' in ooOo0O0O0oOO0 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + ooOo0O0O0oOO0 , 222 , '' , '' , '' )
     elif '.avi' in ooOo0O0O0oOO0 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + ooOo0O0O0oOO0 , 222 , '' , '' , '' )
     elif '.wav' in ooOo0O0O0oOO0 :
      Ii1I1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + ooOo0O0O0oOO0 , 222 , '' , '' , '' )
     else :
      I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + ooOo0O0O0oOO0 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting WebSpace Links" )
      if 57 - 57: o0o00Oo0O * i1iIi - IiI1i11I - iI11I1II1I1I * IiI1i11I
      I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for oOOo0O00o , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in i1Iii1i1I :
   if OO00o in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source Technica[/COLOR]' ) , oOOo0O00o , 222 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 9 - 9: III1iiIii . Iii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for I11oOOooo , iIIIiIi in ii1I1IIii11 :
   if OO00o in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] Lazy List[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O0Ooo + I11oOOooo ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Lazy List Links" )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for oOOo0O00o , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in II1i11I :
   if OO00o in iIIIiIi . lower ( ) :
    Ii1I1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORred] source RaizTv[/COLOR]' ) , oOOo0O00o , 222 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 96 - 96: i1iIi % o0o00Oo0O
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
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
    if 72 - 72: oooOo0oo0oo . OOooOOo / IIiIiII11i
    if 69 - 69: oooOo0oo0oo * IIiIiII11i - i1iIi - ooOoO0O00 + Ii
    if 50 - 50: ii * ooOoO0O00 / i1i1I1IIii1II
    if 83 - 83: ooOoO0O00
    if 38 - 38: ii * iI11I1II1I1I
    if 54 - 54: ii . i1IiiiI1iI
    if 71 - 71: o0ii1I
    if 31 - 31: Iii . Ii . oO0o * I1ii11iIi11i % o0ii1I . I11i
    if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
    if 93 - 93: i1iIi % i1IiiiI1iI
    if 46 - 46: Ii1I * OOooOOo * III1iiIii * Ii1I . Ii1I
    if 43 - 43: i1iIi . ooOoO0O00
 ooOO0o = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 68 - 68: III1iiIii % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
 for ii11I in ooOO0o :
  i1IiIiiiIIIIi = oO0 + ii11I + oOoOooOo0o0
  oo00IiI1 = O00O0oOO00O00 ( i1IiIiiiIIIIi )
  if oo00IiI1 != 'Failed' :
   i1IIi1i1Ii1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo00IiI1 )
   for oOOo0O00o , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in i1IIi1i1Ii1 :
    if OO00o in iIIIiIi . lower ( ) :
     Ii1I1i ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , oOOo0O00o , 222 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 45 - 45: oOo0O0Ooo
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 17 - 17: ii - i1iIi + o0ii1I . ii % I1ii11iIi11i
 ooOO0o = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 92 - 92: i1IiiiI1iI - oooOo0oo0oo % oO0o - I11i % ooOoO0O00
 if 38 - 38: Ii1I . Iii / OOooOOo % Iii
 for ii11I in ooOO0o :
  i1IiIiiiIIIIi = o0oOO0ooOoO + ii11I
  I1I11ii = O00O0oOO00O00 ( i1IiIiiiIIIIi )
  if I1I11ii != 'Failed' :
   OOoOoo00Oo = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( I1I11ii )
   for I11oOOooo , iIIIiIi in OOoOoo00Oo :
    if OO00o in iIIIiIi . lower ( ) :
     oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o0oOO0ooOoO + ii11I + I11oOOooo ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / IiI1i11I
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: I1ii11iIi11i - i1IiiiI1iI
def i1i1I111iIi1 ( ) :
 if 51 - 51: IiI1i11I * i1iIi / o0o00Oo0O / o0o00Oo0O
 if 52 - 52: ii % o0o00Oo0O
 if 56 - 56: i1i1I1IIii1II - ooOoO0O00 * ii - IIiIiII11i
 if 28 - 28: ooOoO0O00 / Iii . I11i
 if 11 - 11: I1ii11iIi11i * ii - Ii
 if 13 - 13: Ii . o0o00Oo0O / oooOo0oo0oo * ooOoO0O00
 if 14 - 14: III1iiIii + III1iiIii . Iii / o0ii1I . iI11I1II1I1I
 if 10 - 10: IIiIiII11i . oooOo0oo0oo / IiI1i11I
 if 35 - 35: IiI1i11I / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
 if 3 - 3: Ii1I
 if 42 - 42: Iii % I1ii11iIi11i + III1iiIii - Iii . iI11I1II1I1I - o0ii1I
 if 27 - 27: IiI1i11I % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
 if 37 - 37: IiI1i11I + i1IiiiI1iI * o0ii1I + III1iiIii
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + o0ii1I / IIiIiII11i
 if 66 - 66: i1iIi + i1i1I1IIii1II % ii
 if 23 - 23: i1i1I1IIii1II . OOooOOo + iI11I1II1I1I
 if 17 - 17: III1iiIii
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 if 12 - 12: ooOoO0O00 . oO0o
 if 14 - 14: oooOo0oo0oo + IIiIiII11i % oooOo0oo0oo . i1i1I1IIii1II * i1iIi
 ooOo0O0O0oOO0 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( OO00o ) . replace ( ' ' , '+' )
 ooO0000o00O = 'http://onlinemovies.tube/?s=' + ( OO00o ) . replace ( ' ' , '+' )
 O0Ooo = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 iIiI1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 54 - 54: i1iIi * Iii - i1IiiiI1iI
 oo0OOoOoo0O0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iiI11ii1111 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 15 - 15: IiI1i11I / o0o00Oo0O
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Scanning Sources" , '' , 'Please Wait' )
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + i1iIi . i1IiiiI1iI * i1iIi
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
 if 82 - 82: o0o00Oo0O / IiI1i11I * oO0o - Iii + I1ii11iIi11i
 oo0o = O00O0oOO00O00 ( ooOo0O0O0oOO0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( ooO0000o00O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( O0Ooo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( oO00oOOo0Oo )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 I1I11ii = O00O0oOO00O00 ( iIiI1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + o0ii1I * IIiIiII11i
 if 78 - 78: i1IiiiI1iI - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
 O0oOoo0OoO0O = O00O0oOO00O00 ( oo0OOoOoo0O0O )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 oo00IiI1 = O00O0oOO00O00 ( iiI11ii1111 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 97 - 97: ooOoO0O00
 if 29 - 29: oOo0O0Ooo
 if oo00IiI1 != 'Failed' :
  i1IIi1i1Ii1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oo00IiI1 )
  for oOOo0O00o , iIIIiIi in i1IIi1i1Ii1 :
   Iiio0Oo0oO = O00O0oOO00O00 ( oOOo0O00o )
   iIII1iiIi11 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( Iiio0Oo0oO )
   for ooOo0O0O0oOO0 , iIiIIi in iIII1iiIi11 :
    if OOOOoOO0O in iIiIIi . lower ( ) :
     I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']*' + iIiIIi + '-[COLORgold] source ' + iIIIiIi + '[/COLOR]' ) , oOOo0O00o + ooOo0O0O0oOO0 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 37 - 37: Ii1I * i1IiiiI1iI * oOo0O0Ooo * o0o00Oo0O
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if O0oOoo0OoO0O != 'Failed' :
  O0Oo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0oOoo0OoO0O )
  for oOOo0O00o , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in O0Oo0 :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] source HeroVision[/COLOR]' ) , oOOo0O00o , 1016 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
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
    if 65 - 65: i1i1I1IIii1II
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  O00oo = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for oOOo0O00o , ooO0OO , iIIIiIi , OoOo0oO0o in i1Iii1i1I :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    if 'season' in OoOo0oO0o :
     IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOOo0O00o , 90054 , ooO0OO , ooO0OO , '' )
    if 'episodes' in OoOo0oO0o :
     IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOOo0O00o , 90044 , ooO0OO , ooO0OO , '' )
  for oOOo0O00o in O00oo :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oOOo0O00o , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 82 - 82: I11i
   I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  IIII1ii = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( oo0o )
  for oOOo0O00o , iIIIiIi , ooO0OO in IIII1ii :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + ( iIIIiIi ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oOOo0O00o , 8022 , ooO0OO , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + i1IiiiI1iI
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 65 - 65: o0ii1I
    if 71 - 71: i1IiiiI1iI % i1IiiiI1iI . i1i1I1IIii1II + Ii - Ii
    if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / i1IiiiI1iI - Ii . i1iIi / oooOo0oo0oo
    if 13 - 13: I11i % o0o00Oo0O - i1IiiiI1iI * ii / I1ii11iIi11i - ii
    if 78 - 78: i1i1I1IIii1II % ii
    if 73 - 73: oOo0O0Ooo % i1iIi % III1iiIii + ooOoO0O00 - ii / i1i1I1IIii1II
    if 78 - 78: ii % i1i1I1IIii1II - Ii
    if 37 - 37: III1iiIii % o0ii1I % ooOoO0O00
    if 23 - 23: i1iIi - o0o00Oo0O + Ii
 if o00OooOO000 != 'Failed' :
  ii1I1IIii11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for iIIIiIi in ii1I1IIii11 :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( O0Ooo + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 98 - 98: ii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  II1i11I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for iIIIiIi in II1i11I :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( oO00oOOo0Oo + iIIIiIi ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 61 - 61: I11i . III1iiIii . o0o00Oo0O + ii + o0o00Oo0O
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if I1I11ii != 'Failed' :
  OOoOoo00Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1I11ii )
  for oOOo0O00o , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in OOoOoo00Oo :
   if OOOOoOO0O in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '-[COLORgold] Source Scooby[/COLOR]' ) , oOOo0O00o , 1016 , iiIIIiIi1IIi , iiiIIiIi , O000OOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 65 - 65: ooOoO0O00 * oooOo0oo0oo * ii - III1iiIii . IiI1i11I - oO0o
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 71 - 71: o0ii1I * OOooOOo
 oOo00o = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for ii11I in oOo00o :
  i1IiIiiiIIIIi = oO0 + ii11I + oOoOooOo0o0
  oO000o = O00O0oOO00O00 ( i1IiIiiiIIIIi )
  if oO000o != 'Failed' :
   o0O0O0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO000o )
   for iIIIiIi , O000OOO , oOOo0O00o , ooO0OO , IIo0o0O0O00oOOo , i1Ii11II in o0O0O0 :
    if OOOOoOO0O in iIIIiIi . lower ( ) :
     I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - Source Pandoras[/COLOR]' , oOOo0O00o , i1Ii11II , ooO0OO , IIo0o0O0O00oOOo , O000OOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % i1IiiiI1iI * I11i
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
     if 64 - 64: i1iIi / i1iIi + Ii1I * oooOo0oo0oo % oooOo0oo0oo
     if 87 - 87: oO0o * I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoO0o00O0oOOo ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOOo0O00o = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( OO00o ) . replace ( ' ' , '+' )
 if 69 - 69: ooOoO0O00 . oOo0O0Ooo + III1iiIii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( oOOo0O00o )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 95 - 95: oOo0O0Ooo - oooOo0oo0oo . I1ii11iIi11i / o0o00Oo0O + o0ii1I
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iIIIiIi in i1Iii1i1I :
   if OO00o in iIIIiIi . lower ( ) :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oOOo0O00o ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 67 - 67: OOooOOo % I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
IiiI11III1i = '{ZH},' ; OOo0o0 = '{IX},' ; oOOoO = '{LM},'
if 1 - 1: IIiIiII11i
def iIooo0O0O0OO ( url ) :
 oOooOOoO = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( oOooOOoO )
 for url , oO0O , o0ooO00O0O , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( oO0O ) . replace ( 'Sezon' , ' Season ' ) + ( o0ooO00O0O ) . replace ( 'Bölüm' , ' Episode ' ) + iIIIiIi , url , 8063 , '' )
  if 78 - 78: oooOo0oo0oo
  if 68 - 68: i1iIi
  if 70 - 70: OOooOOo - I1ii11iIi11i - i1IiiiI1iI * oooOo0oo0oo * oooOo0oo0oo * oOo0O0Ooo
  if 12 - 12: o0ii1I
def i11Iiiiii11II ( url ) :
 oOooOOoO = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( oOooOOoO )
 for url , iIIIiIi in IIi :
  oOOo000oOoO0 ( iIIIiIi , url , 222 , '' )
  if 100 - 100: i1IiiiI1iI + Iii + oO0o . Ii1I
  if 40 - 40: oO0o - oO0o
  if 58 - 58: III1iiIii * IiI1i11I . oOo0O0Ooo + oooOo0oo0oo
  if 4 - 4: oO0o . oooOo0oo0oo + Ii + i1iIi % i1i1I1IIii1II - i1iIi
def iIi1ii1I1iiI ( ) :
 if 21 - 21: III1iiIii * i1i1I1IIii1II
 oOooOOoO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oOooOOoO )
 for oOOo0O00o , ooO0OO , iIIIiIi , o0ooO00O0O in IIi :
  IiI11i1IIiiI ( iIIIiIi + '  -  ' + ( o0ooO00O0O ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOOo0O00o , 8063 , ooO0OO )
  if 92 - 92: Ii1I - I1ii11iIi11i + oO0o * oO0o
def i111i ( ) :
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi , ooO0OO in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 8002 , ooO0OO )
def iII1I1i11iIi ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , time , url , iIIIiIi , iII11O00OO00OOOoO in IIi :
  I1I1II1I11 ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , time ) , url , 1015 , ooO0OO , iII11O00OO00OOOoO )
  if 89 - 89: I11i / oooOo0oo0oo % iI11I1II1I1I - oOo0O0Ooo . i1i1I1IIii1II + OOooOOo
def OO0O0oooo0 ( ) :
 if 58 - 58: oooOo0oo0oo
 IiI11i1IIiiI ( 'Coronation Street' , '' , 8001 , '' )
 IiI11i1IIiiI ( 'Eastenders' , '' , 8002 , '' )
 IiI11i1IIiiI ( 'Emmerdale' , '' , 8003 , '' )
 IiI11i1IIiiI ( 'Hollyoaks' , '' , 8004 , '' )
 IiI11i1IIiiI ( 'Im a Celebrity' , '' , 8005 , '' )
 if 12 - 12: oOo0O0Ooo . I11i * ii
 if 64 - 64: OOooOOo + III1iiIii - ooOoO0O00 . IIiIiII11i . oO0o
 if 31 - 31: i1i1I1IIii1II . IiI1i11I - Iii . iI11I1II1I1I + Iii . OOooOOo
 if 86 - 86: Ii1I - Ii1I / IiI1i11I - Ii1I * IiI1i11I + i1IiiiI1iI
def OOoooiII1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Holly' in iIIIiIi :
   ooO0OO = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oOOo0O00o :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 30 - 30: ii % oooOo0oo0oo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - oooOo0oo0oo
def o0o00O00Oo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'East' in iIIIiIi :
   ooO0OO = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oOOo0O00o :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 96 - 96: IiI1i11I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 9 - 9: III1iiIii + IIiIiII11i . oOo0O0Ooo * IiI1i11I
def i11i1IiIi11 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Emmer' in iIIIiIi :
   ooO0OO = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oOOo0O00o :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 76 - 76: iI11I1II1I1I / i1i1I1IIii1II * iI11I1II1I1I / oO0o . i1iIi
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: ooOoO0O00 / OOooOOo / oooOo0oo0oo . oO0o % i1IiiiI1iI + Ii
def oO0o0oo ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Coro' in iIIIiIi :
   ooO0OO = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oOOo0O00o :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 38 - 38: i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: o0ii1I - IiI1i11I
def i11iI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Celeb' in iIIIiIi :
   ooO0OO = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oOOo0O00o :
    oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOOo0O00o . replace ( '\\/' , '/' ) , 8006 , ooO0OO )
   else :
    pass
    if 46 - 46: IiI1i11I % i1IiiiI1iI % OOooOOo . ii . IIiIiII11i % III1iiIii
def I1i1I1i1I1 ( name , url ) :
 i1IOO = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if i1IOO :
  Oo0OO0ooO0O0O = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I1i111I = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( I1i111I ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I1i111I = open_url ( url )
  oO00O = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( I1i111I ) [ - 1 ]
  Oo0OO0ooO0O0O = oO00O . replace ( '\\/' , '/' )
 i1I11iIiII = xbmcgui . ListItem ( name , '' , '' )
 i1I11iIiII . setPath ( Oo0OO0ooO0O0O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1I11iIiII )
 if 63 - 63: o0o00Oo0O % iI11I1II1I1I / o0o00Oo0O
 if 5 - 5: Ii * i1iIi % IiI1i11I - Iii
def Ii11I111IIIIi ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oOOo0O00o , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for oOOo0O00o , iIIIiIi in i1Iii1i1I :
  IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oOOo0O00o , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 36 - 36: III1iiIii % iI11I1II1I1I . i1IiiiI1iI / i1IiiiI1iI
def ooo0ooo0 ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Movies' in iIIIiIi :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( oOOo0O00o ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def oO000oOo0oO0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ooO0OO )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 2 - 2: I11i - oOo0O0Ooo - Ii / ii
  if 87 - 87: I11i + i1i1I1IIii1II + ii * oooOo0oo0oo
def o00oOoOo0 ( url ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url , ooO0OO in IIi :
  if '{{' in iIIIiIi :
   pass
  else :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , ooO0OO )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
IIIi1Iiii1I1 = '{UJ},' ; iI1iiII1iii111 = '{WE},' ; i11II = '{WP},' ; II1OoOOoOOOoooO0 = '{PP},'
def i11i1i1i ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url , ooO0OO in IIi :
  if '{{' in iIIIiIi :
   pass
  else :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ooO0OO )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoO00O ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  O0oo0ooO ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0oo0ooO ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 6 - 6: iI11I1II1I1I / IiI1i11I
 if 1 - 1: i1IiiiI1iI / OOooOOo * OOooOOo - I11i % o0ii1I
 if 96 - 96: III1iiIii / o0ii1I % oO0o . iI11I1II1I1I
def i1Iiiiiii ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '(cooltvseries.com)' in iIIIiIi :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , iIIIiIi in i1Iii1i1I :
  if '(cooltvseries.com)' in iIIIiIi :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def Oo000O00o0O ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I1i111I )
 for url in IIi :
  OoO00oo00 ( ( url ) . replace ( ' ' , '%20' ) )
o0o0oo0oO = '{XX},' ; Ii1iii1 = '{UD},' ; OO0oooOo = '{YT},' ; OoO0o00o = '{JS},' ; I1111iI = '{PF},'
if 89 - 89: III1iiIii - III1iiIii % IiI1i11I / Iii + i1i1I1IIii1II - III1iiIii
def O0oOoO0o0oO ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi , ooO0OO in IIi :
  oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oOOo0O00o ) ) , 222 , ooO0OO )
  if 80 - 80: i1i1I1IIii1II / o0o00Oo0O
def I1i11IIIi ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  if 'youtu' in url :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + ooO0OO )
 for url in next :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 55 - 55: oOo0O0Ooo * Iii / o0o00Oo0O % OOooOOo
def Oo0OOOOOOOo0O ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 11 - 11: o0ii1I / OOooOOo - oO0o + OOooOOo
def oO0OOoOo000oO ( url ) :
 I1i111I = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 222 , ooO0OO )
  if 37 - 37: I1ii11iIi11i + III1iiIii / o0o00Oo0O - ooOoO0O00 / Ii1I - III1iiIii
  if 17 - 17: oooOo0oo0oo - i1i1I1IIii1II
  if 1 - 1: iI11I1II1I1I / Ii * IIiIiII11i
  if 48 - 48: Ii1I + o0o00Oo0O * i1i1I1IIii1II + Ii1I + Ii1I
  if 60 - 60: IIiIiII11i % I1ii11iIi11i
def OoO000 ( ) :
 if 12 - 12: OOooOOo / oOo0O0Ooo * I1ii11iIi11i
 IiI11i1IIiiI ( 'All Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Entertainment' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Movies' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Music' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'News' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Sports' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Documentary' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Kids' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Food' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Religious' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'USA Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 IiI11i1IIiiI ( 'Other' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 if 59 - 59: I1ii11iIi11i . I11i % oOo0O0Ooo / ii % i1i1I1IIii1II
 if 81 - 81: ii / i1iIi * iI11I1II1I1I . I1ii11iIi11i + i1i1I1IIii1II / o0o00Oo0O
def ooO0o0Oo ( Cat_Name ) :
 if 67 - 67: OOooOOo
 OOO0 = False
 o0oo00 = '0'
 if Cat_Name == 'All Channels' : OOO0 = True
 if Cat_Name == 'Entertainment' : o0oo00 = '1'
 if Cat_Name == 'Movies' : o0oo00 = '2'
 if Cat_Name == 'Music' : o0oo00 = '3'
 if Cat_Name == 'News' : o0oo00 = '4'
 if Cat_Name == 'Sports' : o0oo00 = '5'
 if Cat_Name == 'Documentary' : o0oo00 = '6'
 if Cat_Name == 'Kids' : o0oo00 = '7'
 if Cat_Name == 'Food' : o0oo00 = '8'
 if Cat_Name == 'Religious' : o0oo00 = '9'
 if Cat_Name == 'USA Channels' : o0oo00 = '10'
 if Cat_Name == 'Other' : o0oo00 = '11'
 if 92 - 92: ooOoO0O00
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I1i111I )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for iIIIiIi , ooO0OO , OOO0OOo0OoO in IIi :
  oO00OOO = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ooO0OO ) . replace ( '\\' , '' )
  if OOO0OOo0OoO == o0oo00 :
   IiI11i1IIiiI ( iIIIiIi , '' , 7022 , oO00OOO )
  elif OOO0 == True :
   IiI11i1IIiiI ( iIIIiIi , '' , 7022 , oO00OOO )
  else : pass
  if 48 - 48: iI11I1II1I1I . oO0o + Ii - o0ii1I . oO0o
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 89 - 89: ooOoO0O00
def ooOoOO0O00Ooo ( Search_Name ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1i111I )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I1i111I )
 for ooO0OO , oOOo0O00o , ooO0000o00O , O0Ooo in IIi :
  oO00OOO = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ooO0OO ) . replace ( '\\' , '' )
  oOOo000oOoO0 ( Search_Name + ': Link 1' , ( oOOo0O00o ) . replace ( '\\' , '' ) , 222 , oO00OOO )
  oOOo000oOoO0 ( Search_Name + ': Link 2' , ( ooO0000o00O ) . replace ( '\\' , '' ) , 222 , oO00OOO )
  oOOo000oOoO0 ( Search_Name + ': Link 3' , ( O0Ooo ) . replace ( '\\' , '' ) , 222 , oO00OOO )
  if 15 - 15: i1IiiiI1iI . oO0o - oOo0O0Ooo + ii + i1IiiiI1iI
def IiIII ( ) :
 I1i111I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  oOOo000oOoO0 ( iIIIiIi , ( oOOo0O00o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def iII1iII ( ) :
 I1i111I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  oOOo000oOoO0 ( iIIIiIi , ( oOOo0O00o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def iiii11i1ii1 ( ) :
 I1i111I = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I1i111I )
 for iIIIiIi , oOOo0O00o in IIi :
  oOOo000oOoO0 ( iIIIiIi , ( oOOo0O00o ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 90 - 90: Iii
def I1i1I1IIIi1II ( url ) :
 url
 ooo00Ooo = xbmcgui . ListItem ( iIIIiIi , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo00Ooo )
 return
 if 25 - 25: oooOo0oo0oo / ii - Ii1I
 if 31 - 31: Iii + oO0o / oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
def iiiiIiI1IIiI ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( I1i111I )
 for url , O000OOO , ooO0OO , iIIIiIi in IIi :
  I1I1II1I11 ( iIIIiIi , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + ooO0OO , '' , ( O000OOO ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  IiI11i1IIiiI ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 53 - 53: iI11I1II1I1I % OOooOOo % oOo0O0Ooo + Ii1I % ii
def IIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , O000OOO , ooO0OO in IIi :
  Ii1I1i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + ooO0OO , '' , O000OOO )
  I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 IiiI1Ii1II = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ii11I1IiIIi1i1IIi in IiiI1Ii1II :
  I1i11 = ( ii11I1IiIIi1i1IIi ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1I1II1I11 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + ooO0OO , '' , I1i11 )
  if 83 - 83: o0o00Oo0O / oO0o / oOo0O0Ooo
def I1I1IiIiIIi1I ( INFO ) :
 o0OIiII ( 'info for workout' , INFO )
 if 74 - 74: ii + Ii1I % o0o00Oo0O
 if 32 - 32: Ii1I + Ii1I
 if 89 - 89: i1iIi + i1i1I1IIii1II + o0ii1I - oooOo0oo0oo
def IIIIi11i ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  IiI11i1IIiiI ( ( iIIIiIi ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def OO0ooo ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , url , 9032 , iiIi1IIiIi + 'icon.png' )
def O0000 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  if '=' in iIIIiIi :
   pass
  else :
   oOOo000oOoO0 ( ( iIIIiIi ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def o000o0OO ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  if '=' in iIIIiIi :
   pass
  else :
   oOOo000oOoO0 ( iIIIiIi , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 95 - 95: o0o00Oo0O * oO0o . Iii - III1iiIii - IiI1i11I
   if 84 - 84: I11i / i1IiiiI1iI - o0o00Oo0O + oOo0O0Ooo . Ii1I
   if 30 - 30: IiI1i11I * o0ii1I % OOooOOo / I11i * I11i + o0o00Oo0O
def OO00i1II ( url ) :
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , iiIi1IIiIi + 'bamf.png' )
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  if 'mp4' in url :
   pass
  else :
   oOOo000oOoO0 ( ( iIIIiIi ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1i1I11I ( url ) :
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , iiIi1IIiIi + 'bamf.png' )
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  if 'mp4' in url :
   oOOo000oOoO0 ( ( iIIIiIi ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: Ii1I + iI11I1II1I1I + i1IiiiI1iI * ooOoO0O00 - o0o00Oo0O % IiI1i11I
 if 32 - 32: o0ii1I % Iii + oooOo0oo0oo % ii
 if 68 - 68: Iii
def ii1I11iIi ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'Daily' in iIIIiIi :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , oOOo0O00o , 9008 , O0O )
def IiO00oo0o0ooO ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def OOO0o0O ( url ) :
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 oOOo000oOoO0 ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  oOOo000oOoO0 ( ( iIIIiIi ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 60 - 60: ooOoO0O00 / Iii - I11i - i1iIi
def OO0OoO0 ( ) :
 I1i111I = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if '.m3u' in oOOo0O00o :
   IiI11i1IIiiI ( ( iIIIiIi ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oOOo0O00o ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def ooO0ooO ( url ) :
 I1i111I = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  oOOo000oOoO0 ( ( iIIIiIi ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 68 - 68: iI11I1II1I1I
def Ooo0o00o0o ( ) :
 I1i111I = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  if 'category' in oOOo0O00o :
   IiI11i1IIiiI ( iIIIiIi , 'http://www.disclose.tv/' + oOOo0O00o , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 51 - 51: OOooOOo + III1iiIii
   if 55 - 55: I1ii11iIi11i % i1IiiiI1iI . IIiIiII11i
def oo0OoI1IiI11 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I1i111I )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1i111I )
 for url , iIIIiIi , ooO0OO in IIi :
  IiI11i1IIiiI ( iIIIiIi , 'http://www.disclose.tv/' + url , 7011 , ooO0OO )
 for url in next :
  IiI11i1IIiiI ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 41 - 41: i1iIi * Ii
  if 67 - 67: i1iIi . iI11I1II1I1I . oO0o + i1IiiiI1iI
def o0OOOO00O ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I1i111I )
 ii1I1IIii11 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  if 'http' in url :
   oOOo000oOoO0 ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , iIIIiIi in i1Iii1i1I :
  oOOo000oOoO0 ( iIIIiIi , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in ii1I1IIii11 :
  oOOo000oOoO0 ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 58 - 58: OOooOOo
  if 27 - 27: III1iiIii * oooOo0oo0oo - ii . o0ii1I - IIiIiII11i
def oo0o0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 84 - 84: III1iiIii - OOooOOo . III1iiIii + i1iIi . IiI1i11I
def O00000oooOO ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iI11iiI1 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1Ioo000oooooooO = len ( iI11iiI1 )
 if 18 - 18: i1i1I1IIii1II * I1ii11iIi11i % Ii + o0o00Oo0O % oooOo0oo0oo . oooOo0oo0oo
 if 84 - 84: ii - I1ii11iIi11i
 if I1Ioo000oooooooO == 1 :
  for OoOOoOo0O in iI11iiI1 :
   OoOOoOo0O = OoOOoOo0O . replace ( 'player' , 'watch' )
   II111IiiiI = OoOOoOo0O + '&fv=&sou='
   ii1Ii = OooOoooOo ( II111IiiiI )
   iiiII1iIiI1 = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( ii1Ii )
   for OO00oOooo0O in iiiII1iIiI1 :
    IiIoOoOo0OoOOoo = False
    Resolve ( OO00oOooo0O )
    if 25 - 25: i1iIi % OOooOOo . i1i1I1IIii1II
 elif I1Ioo000oooooooO > 1 :
  if 9 - 9: OOooOOo . iI11I1II1I1I . I1ii11iIi11i - I11i . III1iiIii
  for OoOOoOo0O in iI11iiI1 :
   oo0oO00oo00Ooo = OooOoooOo ( OoOOoOo0O )
   i11i11iiIiIiI = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oo0oO00oo00Ooo )
   o00Oo00OoO = i11i11iiIiIiI
   o00Oo00OoO = ( str ( o00Oo00OoO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + o00Oo00OoO
   oOOo000oOoO0 ( 'DOUBLE LINK' , o00Oo00OoO , 424 , '' )
   if 21 - 21: I1ii11iIi11i - o0o00Oo0O
   for url in i11i11iiIiIiI :
    IiI11i1IIiiI ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     ooO0000o00O = Google . resolve ( url )
    except :
     pass
    try :
     oOO0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( ooO0000o00O ) )
     for IIIiiiIi1I1 , II1iIIII in oOO0 :
      if 43 - 43: oooOo0oo0oo * OOooOOo . i1IiiiI1iI * IIiIiII11i - Ii + Iii
      HD_URLS . append ( IIIiiiIi1I1 )
      SD_URLS . append ( II1iIIII )
    except :
     pass
 else :
  pass
  if 44 - 44: i1iIi * Ii . IiI1i11I / iI11I1II1I1I
def i11111 ( ) :
 if 21 - 21: iI11I1II1I1I % oOo0O0Ooo / I11i / I11i
 if 28 - 28: ii . i1iIi / IIiIiII11i + Iii / o0o00Oo0O . ii
 IiI11i1IIiiI ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 75 - 75: iI11I1II1I1I * i1IiiiI1iI . Ii
 IiI11i1IIiiI ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 21 - 21: Ii . I11i
 if 25 - 25: oO0o % ooOoO0O00
def iI11ii1i ( ) :
 I1i111I = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , 'http://cnfstudio.com/genre/' + oOOo0O00o , 7003 , iiIi1IIiIi + 'icon.png' )
  if 96 - 96: o0ii1I + IiI1i11I - OOooOOo . Iii * I11i - o0ii1I
iIii1 = xbmcgui . Dialog ( )
if 73 - 73: I1ii11iIi11i - Iii - i1iIi / i1IiiiI1iI * III1iiIii
ooo00 = '{UN},' ; Oooo00oo0o = '{IG},' ; OoO00o = '{PL},' ; o0oOo = '{LO},' ; iiOO00O = '{LP},' ; iiO0OoO0OOO00 = '{HA},' ; IIIiii1I = '{XD},' ; ii1iiii11IiI1 = '{TA},' ; O0OoO0ooOoo = '{DP},' ; iIIi1i1i11IIi = '{JT},' ; oOOO0o00 = '{JJ},' ; O00ooi1i1iIiiI1Ii1 = '{MM},' ; iIII = '{FQ},' ; i11iI1I1I11II = '{HH},'
if 70 - 70: iI11I1II1I1I . i1iIi * i1i1I1IIii1II
def II1iII1IIIIi ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I1i111I )
 oOOooo00 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I1i111I )
 for ooO0OO , url , iIIIiIi in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , ooO0OO )
 oOOooo00 = oOOooo00
 for url in oOOooo00 :
  IiI11i1IIiiI ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 31 - 31: Iii + I1ii11iIi11i
def i1IIIIi1I ( url ) :
 if 28 - 28: o0ii1I % iI11I1II1I1I
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  oOOOIi11 = O0Oo0O0O0o0 ( iiI111I1iIiI )
  Oo0o = O0Oo0O0O0o0 ( url )
  if 66 - 66: ii % III1iiIii
  if 12 - 12: Iii / Ii - i1IiiiI1iI
def O0Oo0O0O0o0 ( url ) :
 if 50 - 50: Iii
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( I1i111I )
 for url in IIi :
  i11i1i ( url )
  if 88 - 88: ooOoO0O00 * oooOo0oo0oo . iI11I1II1I1I
  if 45 - 45: i1IiiiI1iI - o0o00Oo0O . i1IiiiI1iI / i1IiiiI1iI / OOooOOo
def i1IIII1iII ( ) :
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 I1I1II1I11 ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 93 - 93: oooOo0oo0oo * o0ii1I - I11i . i1i1I1IIii1II . IiI1i11I
def OOoooi1i1I11I ( ) :
 if os . path . exists ( II ) :
  i11I1ii = open ( II , 'r' )
  for ooo00Ooo in i11I1ii :
   o0o000O0o = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( ooo00Ooo )
   for iIIIiIi , oOOo0O00o in o0o000O0o :
    oOOo000oOoO0 ( iIIIiIi , oOOo0O00o , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 50 - 50: ii
def iI11i1I ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = ii1IIIIiI11 ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIIIiIi , url in IIi :
   url = ( url ) . strip ( )
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 68 - 68: I1ii11iIi11i + I11i * oooOo0oo0oo . IIiIiII11i % o0ii1I
  if 14 - 14: ii * I1ii11iIi11i % i1iIi . o0ii1I - IiI1i11I - IIiIiII11i
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in IIi :
  oOOo0O00o = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oOOo0O00o
 iIIIiIi = 'plugin.video.GenieTv'
 if 67 - 67: IiI1i11I
 o0o00O0 ( oOOo0O00o , iIIIiIi )
 if 88 - 88: oOo0O0Ooo
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o in IIi :
  oOOo0O00o = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oOOo0O00o
 iIIIiIi = 'repository.GenieTv'
 if 74 - 74: IiI1i11I * Ii + ooOoO0O00 * i1iIi + i1i1I1IIii1II * o0ii1I
 o0o00O0 ( oOOo0O00o , iIIIiIi )
 if 90 - 90: IiI1i11I
 if 71 - 71: III1iiIii - IIiIiII11i - I11i * Ii / i1IiiiI1iI
def OoO ( ) :
 oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOOoo00O00o )
 if O0O00Oo == 0 :
  O0oooOoOO0O ( )
 if O0O00Oo == 1 :
  ii111iIii1 ( )
  if 89 - 89: IIiIiII11i + i1iIi
  if 50 - 50: oO0o - oOo0O0Ooo * oOo0O0Ooo / i1IiiiI1iI % iI11I1II1I1I
  if 55 - 55: oO0o
  if 50 - 50: Ii1I . OOooOOo % I1ii11iIi11i . III1iiIii . i1i1I1IIii1II
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
OoOo0O0 = 'https://addons.tvaddons.ag/'
if 100 - 100: OOooOOo + I1ii11iIi11i . Ii + IiI1i11I / OOooOOo
def ii111iIii1 ( ) :
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 oO0O00oO0o0 = 'https://addons.tvaddons.ag/search/?keyword=' + OOOOoOO0O
 II11iIiIIIiI = OooOoooOo ( oO0O00oO0o0 )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for oOOo0O00o , IioO0oOOO0Ooo , iIIIiIi in IIi :
  I1I1II1I11 ( iIIIiIi , oOOo0O00o , 10054 , 'https://addons.tvaddons.ag/' + IioO0oOOO0Ooo , Oo00OOOOO , '' )
  if 37 - 37: OOooOOo % o0ii1I * Iii + OOooOOo / oOo0O0Ooo
  if 23 - 23: ii
def O0oooOoOO0O ( ) :
 II11iIiIIIiI = OooOoooOo ( OoOo0O0 )
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
   if 45 - 45: I11i * OOooOOo / Ii / oOo0O0Ooo - o0ii1I
   if 40 - 40: III1iiIii * I11i / Ii / oO0o
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
  if 26 - 26: oooOo0oo0oo
  if 38 - 38: o0o00Oo0O + IiI1i11I
def i1IIiIiI11 ( url , name ) :
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
   if 61 - 61: Ii % i1IiiiI1iI / I11i
def o0o00O0 ( url , name ) :
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
 if 40 - 40: oooOo0oo0oo / o0ii1I % oOo0O0Ooo / I11i . IiI1i11I
def OOOOo0o00OO0000 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 78 - 78: Iii - oOo0O0Ooo * III1iiIii
 if 43 - 43: ii . oooOo0oo0oo
def iI1IIiIi1i ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , IioO0oOOO0Ooo , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , url , 1007 , IioO0oOOO0Ooo )
def OooIiii1ii ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , IioO0oOOO0Ooo , iIIIiIi in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 1006 , IioO0oOOO0Ooo )
  if 77 - 77: oooOo0oo0oo % i1i1I1IIii1II + iI11I1II1I1I * o0ii1I . III1iiIii . I1ii11iIi11i
def IIiiiI ( ) :
 I1i111I = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , iiIIIiIi1IIi , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
  ooooO0OOo0o0 ( iIIIiIi , 100109 , oOOo0O00o , image = iiIIIiIi1IIi , isFolder = True )
  if 27 - 27: I11i . OOooOOo * o0ii1I * IiI1i11I * o0o00Oo0O
def o000ooo0o0O ( url ) :
 import random
 iiiI11iiI11 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 iiiI11iiI11 . clear ( )
 iII1i1iIi11I = [ ]
 ooOOo0OOoOOO = [ ]
 i1IIIi111111 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0000o00O , iiIIIiIi1IIi , O000OOO , IIo0o0O0O00oOOo , iIIIiIi in IIi :
  iII1i1iIi11I . append ( [ ooO0000o00O , iIIIiIi ] )
  if len ( iII1i1iIi11I ) == len ( IIi ) :
   for ooo00Ooo in iII1i1iIi11I :
    iIi1Ii1Ii1II = random . randint ( 1 , len ( iII1i1iIi11I ) )
    try :
     i111iii1i1 = iII1i1iIi11I [ int ( iIi1Ii1Ii1II ) ]
    except :
     pass
    if len ( ooOOo0OOoOOO ) <= 20 :
     if i111iii1i1 [ 1 ] not in i1IIIi111111 :
      o0o = OooOoooOo ( i111iii1i1 [ 0 ] )
      ii1I1IIii11 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for O00OoooOoo0Oooo , i1O0o0oO in ii1I1IIii11 :
       OOoOoo = OooOoooOo ( O00OoooOoo0Oooo )
       II1i11I = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for IiIIII1ii1ii , iiI111I1iIiI in II1i11I :
        if 'panda' in iiI111I1iIiI :
         I1iiIII = OooOoooOo ( iiI111I1iIiI )
         IiIIi1I1I11Ii = re . compile ( "url: '(.+?)'" ) . findall ( I1iiIII )
         for oOooOOo000o0o in IiIIi1I1I11Ii :
          if 'http' in oOooOOo000o0o :
           i1I11iIiII = xbmcgui . ListItem ( i111iii1i1 [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : i111iii1i1 [ 1 ] } )
           i1I11iIiII . setProperty ( "IsPlayable" , "true" )
           iiiI11iiI11 . add ( oOooOOo000o0o , i1I11iIiII )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1I11iIiII )
           if 79 - 79: i1IiiiI1iI + i1i1I1IIii1II - iI11I1II1I1I * OOooOOo / ii
def ooooO0OOo0o0 ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 Ii1I11I = sys . argv [ 0 ]
 Ii1I11I += '?mode=' + str ( mode )
 Ii1I11I += '&title=' + urllib . quote_plus ( name )
 Ii1I11I += '&image=' + urllib . quote_plus ( image )
 Ii1I11I += '&page=' + str ( page )
 if url != '' :
  Ii1I11I += '&url=' + urllib . quote_plus ( url )
 if keyword :
  Ii1I11I += '&keyword=' + urllib . quote_plus ( keyword )
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  i1I11iIiII . addContextMenuItems ( contextMenu )
 if infoLabels :
  i1I11iIiII . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  i1I11iIiII . setProperty ( "IsPlayable" , "true" )
 i1I11iIiII . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = isFolder )
 if 49 - 49: ii + i1IiiiI1iI
 if 39 - 39: i1i1I1IIii1II * i1IiiiI1iI - i1iIi + o0o00Oo0O
def iiIIiii ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , iconimage , O000OOO , IIo0o0O0O00oOOo , name in IIi :
  if 'http' in url :
   if '.php' in url :
    ooOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for ooo00Ooo in ooOo00 :
     if ooo00Ooo == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    o00o00 ( name , url , 1016 , iconimage , IIo0o0O0O00oOOo , O000OOO )
   else :
    if 'youtube' in url :
     ooOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for ooo00Ooo in ooOo00 :
      if ooo00Ooo == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i11IIi1Iii1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , IIo0o0O0O00oOOo , O000OOO )
    else :
     ooOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for ooo00Ooo in ooOo00 :
      if ooo00Ooo == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i11IIi1Iii1 ( name , url , 222 , iconimage , IIo0o0O0O00oOOo , O000OOO )
     I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
  else :
   iii11ii1 ( url , iconimage , name )
   if 51 - 51: iI11I1II1I1I / Iii * oO0o * o0ii1I + Ii1I . ii
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
  for url , IioO0oOOO0Ooo , name in IIi :
   if 'http' in url :
    if '.php' in url :
     IiI11i1IIiiI ( name , url , 1016 , IioO0oOOO0Ooo )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      oOOo000oOoO0 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IioO0oOOO0Ooo )
     else :
      ooOo00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for ooo00Ooo in ooOo00 :
       if ooo00Ooo == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      oOOo000oOoO0 ( name , url , 222 , IioO0oOOO0Ooo )
      I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
   else :
    iii11ii1 ( url , IioO0oOOO0Ooo , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 75 - 75: III1iiIii / ii / o0o00Oo0O % oooOo0oo0oo
def iii11ii1 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oo0oO = ( url ) . replace ( OOo0o0 , 'http' ) . replace ( Ii1iii1 , '.com' ) ;
 iII1IiI1I11i = ( oo0oO ) . replace ( oOOoO , 'a' ) . replace ( OOOoO0O0 , 'b' ) . replace ( iII1I1iIi1i , 'c' ) . replace ( iI1iiII1iii111 , 'd' ) . replace ( OoO00o , 'e' ) . replace ( iIIi1i1i11IIi , 'f' ) ;
 Ii1i11I11i = ( iII1IiI1I11i ) . replace ( o0o0oo0oO , 'g' ) . replace ( iiO0OoO0OOO00 , 'h' ) . replace ( OO0oooOo , 'i' ) . replace ( I1111iI , 'j' ) . replace ( O0OO0o , 'k' ) . replace ( Ii11IiiI , 'l' ) ;
 oO0oooo = ( Ii1i11I11i ) . replace ( OOOoO0 , 'm' ) . replace ( O0OO0 , 'n' ) . replace ( OO0oO0o0oOO , 'o' ) . replace ( Iii1OO , 'p' ) . replace ( iI1III11IIi11Ii11 , 'q' ) . replace ( iII1IoOoOo0O00Oo , 'r' ) ;
 Iiii1iiIi = ( oO0oooo ) . replace ( oOoOO , 's' ) . replace ( i11II , 't' ) . replace ( i1iIiII111i11 , 'u' ) . replace ( i1iIiiii , 'v' ) . replace ( O0o0oOo0OooO , 'w' ) . replace ( iI1IiI1 , 'x' ) ;
 o0o0ooo = ( Iiii1iiIi ) . replace ( oOooO , 'y' ) . replace ( o0OOooo0ooo0o , 'z' ) . replace ( ooo00 , '.' ) . replace ( Oooo00oo0o , '(' ) . replace ( o0oOo , ')' ) . replace ( iiOO00O , '/' ) ;
 i11IIi = ( o0o0ooo ) . replace ( IiiI11III1i , '1' ) . replace ( II1OoOOoOOOoooO0 , '2' ) . replace ( O00iiIi1iI1iI1i , '3' ) . replace ( ii1iiii11IiI1 , '4' ) . replace ( O0OoO0ooOoo , '5' ) . replace ( OoO0o00o , '6' ) ;
 I1I1iI = ( i11IIi ) . replace ( oOOO0o00 , '7' ) . replace ( O00ooi1i1iIiiI1Ii1 , '8' ) . replace ( iIII , '9' ) . replace ( i11iI1I1I11II , '0' ) . replace ( IiI1I1II , ':' ) . replace ( IIIiiIIIiI1 , '%' ) ;
 url = ( I1I1iI ) . replace ( IIIi1Iiii1I1 , '-' ) . replace ( IIIiii1I , '_' ) ;
 oOOo000oOoO0 ( name , url , 222 , iconimage ) ;
 if 28 - 28: Ii - o0ii1I
 if 59 - 59: IIiIiII11i - oO0o
def I1iI1IiII ( ) :
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for oOOo0O00o , IioO0oOOO0Ooo , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , oOOo0O00o , 1007 , IioO0oOOO0Ooo )
def II11iIIoO00 ( url ) :
 if 7 - 7: o0o00Oo0O * I11i + Ii - o0o00Oo0O
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , IioO0oOOO0Ooo , iIIIiIi in IIi :
  IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 1006 , IioO0oOOO0Ooo )
  if 46 - 46: IiI1i11I / I11i . oooOo0oo0oo + IiI1i11I - IIiIiII11i + ooOoO0O00
def I1iIIiI ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 ii1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 ii1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ii1 )
 if 65 - 65: oO0o . III1iiIii % i1IiiiI1iI . ii
 if 19 - 19: i1IiiiI1iI * o0ii1I - i1i1I1IIii1II
def i1iIii ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1i111I )
 for url , ooO0OO , iIIIiIi in IIi :
  if '-dir-' in iIIIiIi :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , ooO0OO )
  else :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' , url , 1006 , ooO0OO )
   if 78 - 78: oO0o - o0ii1I / oooOo0oo0oo
def ooOo000 ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 OO0o0oo = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '[To Parent Directory]' in iIIIiIi :
   iIIIiIi = 'HOME'
   pass
  elif 'HOME' in iIIIiIi :
   pass
  elif '.m3u' in iIIIiIi :
   IiI11i1IIiiI ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , OO0o0oo + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in iIIIiIi :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , OO0o0oo + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in iIIIiIi :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , OO0o0oo + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) , OO0o0oo + url , 1012 , iiIi1IIiIi + 'music.png' )
def o00I11II1iI ( url ) :
 II11iIiIIIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ooO0OO , iIIIiIi , url in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 19 - 19: o0o00Oo0O
def O0oo0O0OO0OOo ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 OO0o0oo = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  if '.mp3' in iIIIiIi :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '/' , '' ) , OO0o0oo + url , 1011 , iiIi1IIiIi + 'music.png' )
def i111ii11I1 ( ) :
 I1i111I = ii1IIIIiI11 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I1i111I )
 for oOOo0O00o , ooO0OO , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , ( 'http://www.cyn.net/music/' + oOOo0O00o ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + ooO0OO ) . replace ( ' ' , '%20' ) )
def iii1I1 ( url , img ) :
 I1i111I = ii1IIIIiI11 ( url )
 ooO0000o00O = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( ooO0000o00O + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 67 - 67: o0ii1I . oOo0O0Ooo * i1i1I1IIii1II * IIiIiII11i . i1i1I1IIii1II % oO0o
def III1IIIIIiiI ( url ) :
 I1i111I = ii1IIIIiI11 ( url )
 ooO0000o00O = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1i111I )
 for type , url , iIIIiIi in IIi :
  if '[VID]' in type :
   oOOo000oOoO0 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , ooO0000o00O + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   III1IIIIIiiI ( ooO0000o00O + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: i1i1I1IIii1II / oO0o % Ii
 if 26 - 26: i1iIi . i1IiiiI1iI / IIiIiII11i % o0ii1I
def O0o00 ( ) :
 o0oOO0ooOoO = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 OO00o = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OOOOoOO0O = OO00o . lower ( )
 oOOo0O00o = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 ooOo0O0O0oOO0 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 ooO0000o00O = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 82 - 82: oooOo0oo0oo % o0o00Oo0O % iI11I1II1I1I % III1iiIii + Ii
 II11iIiIIIiI = O00O0oOO00O00 ( oOOo0O00o )
 oo0o = O00O0oOO00O00 ( ooOo0O0O0oOO0 )
 o0o = O00O0oOO00O00 ( ooO0000o00O )
 if 64 - 64: ooOoO0O00 / III1iiIii . III1iiIii - i1IiiiI1iI % oooOo0oo0oo . IIiIiII11i
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for oOOo0O00o , iiIIIiIi1IIi , O000OOO , iiiIIiIi , iIIIiIi in IIi :
   if OO00o in iIIIiIi . lower ( ) :
    I1I1II1I11 ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oOOo0O00o , 1016 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , O000OOO )
    if 78 - 78: i1IiiiI1iI - o0o00Oo0O - i1IiiiI1iI . iI11I1II1I1I % Ii1I . ii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  IIII1ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oo0o )
  for oOOo0O00o , iIIIiIi in IIII1ii :
   if OO00o in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oOOo0O00o ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 64 - 64: III1iiIii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for oOOo0O00o , iIIIiIi in i1Iii1i1I :
   if OO00o in iIIIiIi . lower ( ) :
    IiI11i1IIiiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oOOo0O00o ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 21 - 21: I11i - i1iIi * ii . ii
    I1iI1ii1II ( 'tvshows' , 'Media Info 3' )
    if 17 - 17: oooOo0oo0oo - IiI1i11I % oOo0O0Ooo * oooOo0oo0oo * iI11I1II1I1I . I11i
    if 58 - 58: i1i1I1IIii1II - IIiIiII11i + o0o00Oo0O
    if 54 - 54: iI11I1II1I1I - III1iiIii - III1iiIii
    if 18 - 18: Ii + iI11I1II1I1I . Ii
    if 63 - 63: IiI1i11I - oO0o * oooOo0oo0oo
    if 89 - 89: IiI1i11I / I1ii11iIi11i
OOOoO0 = '{SF},' ; O0OO0 = '{IF},' ; OO0oO0o0oOO = '{PW},' ; O00iiIi1iI1iI1i = '{AM},' ; Iii1OO = '{GF},' ; iI1III11IIi11Ii11 = '{DD},' ; iII1IoOoOo0O00Oo = '{UO},' ; oOoOO = '{LE},' ; i1iIiII111i11 = '{ZY},' ; i1iIiiii = '{UE},' ; O0o0oOo0OooO = '{PE},' ; iI1IiI1 = '{JE},' ; oOooO = '{TH},' ; o0OOooo0ooo0o = '{LK},'
if 66 - 66: I11i + OOooOOo % ii . Iii
if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
def iIi1 ( ) :
 I1i111I = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , oOOo0O00o , 8021 , iiIi1IIiIi + 'iwatch.png' )
  I1iI1ii1II ( 'movies' , 'MAIN' )
def Ooo0OO0 ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I1i111I )
 for url , iIIIiIi , I11iIi in IIi :
  IiI11i1IIiiI ( iIIIiIi + I11iIi , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def o0o0oO ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1i111I )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  IiI1IIiIII ( url )
def IiI1IIiIII ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1i111I )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1i111I )
 ii1I1IIii11 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I1i111I )
 II1i11I = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  oOOo000oOoO0 ( 'VidSpot - ' + iIIIiIi , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  oOOo000oOoO0 ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , iIIIiIi in II1i11I :
  oOOo000oOoO0 ( 'VidUp' + iIIIiIi , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for iIIIiIi , url in ii1I1IIii11 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   oOOo000oOoO0 ( 'TheVideo - ' + iIIIiIi , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 95 - 95: III1iiIii * IIiIiII11i % I11i * I1ii11iIi11i . Iii
def ii1I11ii ( ) :
 I1i111I = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , oOOo0O00o , 1021 , iiIi1IIiIi + 'anime.png' )
  if 41 - 41: i1iIi % Ii1I + iI11I1II1I1I
  if 59 - 59: i1IiiiI1iI + i1IiiiI1iI * o0o00Oo0O . IIiIiII11i
def oOOiI ( ) :
 I1i111I = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1i111I )
 for oOOo0O00o , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , oOOo0O00o , 1002 , iiIi1IIiIi + 'anime.png' )
  if 94 - 94: III1iiIii / i1iIi + i1IiiiI1iI * oooOo0oo0oo
  if 16 - 16: i1iIi - ooOoO0O00 - Iii % I1ii11iIi11i * Iii - OOooOOo
  if 19 - 19: oOo0O0Ooo + I11i / i1IiiiI1iI . III1iiIii % o0o00Oo0O % ooOoO0O00
def oo0Oo0oo000 ( url ) :
 I1i111I = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I1i111I )
 for ooO0OO in i1Iii1i1I :
  oO00Oo0O0 = ooO0OO
 ii1I1IIii11 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I1i111I )
 for url in ii1I1IIii11 :
  IiI11i1IIiiI ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I1i111I )
 for url , iIIIiIi in IIi :
  IiI11i1IIiiI ( iIIIiIi , url , 1003 , oO00Oo0O0 )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii11I111Ii ( url , IMAGE ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I1i111I )
 for iIIIiIi , url in IIi :
  print iIIIiIi + '     ' + url
  if 'easy' in url :
   iIiIIiIII1I ( url )
  elif 'playpanda' in url :
   iIiIIiIII1I ( url )
   if 16 - 16: iI11I1II1I1I * oOo0O0Ooo * i1i1I1IIii1II * ii . oOo0O0Ooo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIiIIiIII1I ( url ) :
 I1i111I = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I1i111I )
 for url in IIi :
  oOOo000oOoO0 ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 24 - 24: oO0o + IiI1i11I - IIiIiII11i - i1IiiiI1iI
  if 41 - 41: i1iIi - i1IiiiI1iI % Ii * I1ii11iIi11i * III1iiIii - o0o00Oo0O
def oOOoOO0o00O00 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 1 - 1: OOooOOo * iI11I1II1I1I
def ii1IIIIiI11 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 17 - 17: ii . oooOo0oo0oo
def iII1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IIiiIiIIiI1 = ( '%s%s' % ( I1IiI , url ) )
 iiI111I1iIiI = ii1IIIIiI11 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , IioO0oOOO0Ooo , iIIIiIi in IIi :
  oOOo000oOoO0 ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + iIIIiIi + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , IioO0oOOO0Ooo )
  if 35 - 35: Ii1I . oooOo0oo0oo
def oO0Ooo ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  iiiiIIiiII1Iii1 ( url , iIIIiIi )
 else :
  I11iiiiI1i ( url )
def I11iiiiI1i ( url ) :
 import urlresolver
 try :
  OOo0O0O000 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( OOo0O0O000 , xbmcgui . ListItem ( iIIIiIi ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( iIIIiIi ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def i11i1i ( url ) :
 if 98 - 98: oooOo0oo0oo
 O00O0 = open ( OOOO0OOoO0O0 , "a" )
 O00O0 . write ( 'url="' + url + '"\n' )
 O00O0 . close
 if 97 - 97: I11i
 ii1IiIiI1 = xbmc . Player ( OOOoOo00O ( ) )
 import urlresolver
 try : ii1IiIiI1 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iIIIiIi ) )
 ii1IiIiI1 = xbmc . Player ( OOOoOo00O ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : ii1IiIiI1 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def iiiiIIiiII1Iii1 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  I1oOOO = '.mp4'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   i1i1IIi11i1i1I1i ( url , name , I1oOOO )
 elif '.mkv' in url :
  I1oOOO = '.mkv'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   i1i1IIi11i1i1I1i ( url , name , I1oOOO )
 elif '.mp3' in url :
  I1oOOO = '.mp3'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   i1i1IIi11i1i1I1i ( url , name , I1oOOO )
 elif '.avi' in url :
  I1oOOO = '.avi'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   i1i1IIi11i1i1I1i ( url , name , I1oOOO )
 elif '.mov' in url :
  I1oOOO = '.mov'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   i1i1IIi11i1i1I1i ( url , name , I1oOOO )
 elif '.mpeg' in url :
  I1oOOO = '.mpeg'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   i1i1IIi11i1i1I1i ( url , name , I1oOOO )
 elif '.mpg' in url :
  I1oOOO = '.mpg'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   i1i1IIi11i1i1I1i ( url , name , I1oOOO )
 elif '.flv' in url :
  I1oOOO = '.flv'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   i1i1IIi11i1i1I1i ( url , name , I1oOOO )
 elif '.wmv' in url :
  I1oOOO = '.wmv'
  oOOoo00O00o = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  O0O00Oo = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOOoo00O00o )
  if O0O00Oo == 0 :
   I11iiiiI1i ( url )
  if O0O00Oo == 1 :
   i1i1IIi11i1i1I1i ( url , name , I1oOOO )
 else :
  I11iiiiI1i ( url )
def i1i1IIi11i1i1I1i ( url , name , cat ) :
 OOii ( )
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
def OOii ( ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def o0ooo ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iIIIiIi )
 xbmc . sleep ( 1 )
 ii1IiIiI1 = xbmc . Player ( OOOoOo00O ( ) )
 o0oOoO00o . update ( 100 , '%s' % iIIIiIi )
 xbmc . sleep ( 1 )
 ii1IiIiI1 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 77 - 77: I11i % IiI1i11I / ooOoO0O00 . I1ii11iIi11i
def OoO00oo00 ( url ) :
 ii1IiIiI1 = xbmc . Player ( OOOoOo00O ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : ii1IiIiI1 . play ( url ) . strip ( )
 except : pass
 if 77 - 77: Ii % i1IiiiI1iI - I1ii11iIi11i - i1i1I1IIii1II * oooOo0oo0oo
def iiiII1I1 ( url ) :
 ii1IiIiI1 = xbmc . Player ( OOOoOo00O ( ) )
 import urlresolver
 oo0oii1IIi1Ii1II1 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 ii1IiIiI1 . play ( oo0oii1IIi1Ii1II1 )
 xbmc . sleep ( 1 )
 ii1IiIiI1 . play ( url )
 if 60 - 60: oooOo0oo0oo
 if 12 - 12: IiI1i11I . i1i1I1IIii1II % III1iiIii * ii . III1iiIii
def OOOoOo00O ( ) :
 try :
  iIiiIi = getSet ( "core-player" )
  if ( iIiiIi == 'DVDPLAYER' ) : IiI11i = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iIiiIi == 'MPLAYER' ) : IiI11i = xbmc . PLAYER_CORE_MPLAYER
  elif ( iIiiIi == 'PAPLAYER' ) : IiI11i = xbmc . PLAYER_CORE_PAPLAYER
  else : IiI11i = xbmc . PLAYER_CORE_AUTO
 except : IiI11i = xbmc . PLAYER_CORE_AUTO
 return IiI11i
 return True
 if 32 - 32: Ii + IIiIiII11i + IIiIiII11i % Iii
def IiI11i1IIiiI ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  OO0OO0OO = [ ]
  OO0OO0OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OO0OO0OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   OO0OO0OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1I11iIiII . addContextMenuItems ( OO0OO0OO )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = True )
 return iiIii1I
 if 96 - 96: I11i
def iiiO000OOO ( name , url , mode , iconimage , fanart , description ) :
 if 90 - 90: III1iiIii * o0ii1I . Iii / Ii1I % Iii
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1I11iIiII . setProperty ( "Fanart_Image" , fanart )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = True )
 return iiIii1I
 if 58 - 58: IiI1i11I % iI11I1II1I1I * oO0o
def oOOo000oOoO0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  OO0OO0OO = [ ]
  OO0OO0OO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   OO0OO0OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   OO0OO0OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i1I11iIiII . addContextMenuItems ( OO0OO0OO )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = False )
 return iiIii1I
 if 25 - 25: i1IiiiI1iI - i1iIi + I1ii11iIi11i . oOo0O0Ooo % iI11I1II1I1I
 if 49 - 49: ooOoO0O00 + oO0o + IiI1i11I / I1ii11iIi11i
 if 5 - 5: Ii + Iii . III1iiIii
 if 9 - 9: Ii / iI11I1II1I1I - Ii1I * Ii1I
 if 99 - 99: Iii
 if 64 - 64: iI11I1II1I1I
def o0OOOOooOo ( url , heading , announce ) :
 class iIi1I1Iii1 ( ) :
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
   try : O0oO0 = open ( announce ) ; o0Ooo0o0Oo = O0oO0 . read ( )
   except : o0Ooo0o0Oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( o0Ooo0o0Oo ) )
   return
 iIi1I1Iii1 ( )
 iIi1I1Iii1 ( )
def o0OIiII ( heading , announce ) :
 class iIi1I1Iii1 ( ) :
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
   try : O0oO0 = open ( announce ) ; o0Ooo0o0Oo = O0oO0 . read ( )
   except : o0Ooo0o0Oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( o0Ooo0o0Oo ) )
   return
 iIi1I1Iii1 ( )
 iIi1I1Iii1 ( )
def iIiIi11 ( ) :
 o0OOOOooOo ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 99 - 99: oOo0O0Ooo . i1iIi % IIiIiII11i / oOo0O0Ooo
 if 52 - 52: Ii
 if 57 - 57: oOo0O0Ooo - ooOoO0O00 + IiI1i11I * I1ii11iIi11i % oO0o
 if 87 - 87: iI11I1II1I1I % OOooOOo + oO0o / Ii
 if 97 - 97: IiI1i11I % oO0o / oO0o
def OOOOo0o00OO0000 ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 30 - 30: oO0o . Ii * o0ii1I / I11i . I1ii11iIi11i . ii
 if 1 - 1: i1i1I1IIii1II % OOooOOo . o0o00Oo0O
 if 43 - 43: o0o00Oo0O + IIiIiII11i . o0o00Oo0O
 if 25 - 25: IIiIiII11i + Iii
 if 97 - 97: o0o00Oo0O + oooOo0oo0oo % OOooOOo * Iii . iI11I1II1I1I
 if 94 - 94: i1i1I1IIii1II
 if 53 - 53: i1iIi + IiI1i11I * ooOoO0O00 + oOo0O0Ooo
 if 89 - 89: oOo0O0Ooo / IIiIiII11i - OOooOOo % I11i
 if 1 - 1: ii . Iii / OOooOOo + I11i % ooOoO0O00
 if 1 - 1: ii - oO0o - ii / IiI1i11I
 if 70 - 70: o0ii1I + Ii1I . IIiIiII11i * Ii
 if 87 - 87: o0ii1I / i1IiiiI1iI % OOooOOo * Ii1I - ii / OOooOOo
 if 24 - 24: Iii . oooOo0oo0oo * ooOoO0O00 . Ii1I / i1iIi / o0o00Oo0O
 if 62 - 62: I11i % IIiIiII11i
 if 22 - 22: i1i1I1IIii1II - I11i
 if 89 - 89: oooOo0oo0oo
 if 34 - 34: IiI1i11I . oooOo0oo0oo
 if 13 - 13: oO0o * oooOo0oo0oo + i1i1I1IIii1II
 if 21 - 21: Ii . o0ii1I % ooOoO0O00 * o0ii1I . i1i1I1IIii1II + o0ii1I
 if 92 - 92: ooOoO0O00 + oO0o * Iii
 if 70 - 70: I1ii11iIi11i
 if 93 - 93: IiI1i11I . Ii1I . I1ii11iIi11i . i1i1I1IIii1II . ii
 if 51 - 51: o0o00Oo0O - IiI1i11I
 if 65 - 65: o0o00Oo0O / IIiIiII11i * III1iiIii % o0ii1I + I11i
def i11Ii1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iII11I1iIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 27 - 27: ooOoO0O00 - ooOoO0O00 - o0ii1I - oooOo0oo0oo
def O0OoO0OOOo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1i11Iiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 60 - 60: iI11I1II1I1I . Ii1I % I11i * oooOo0oo0oo - oOo0O0Ooo * IIiIiII11i
def o0i11iiII11i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOOo0O0oOOOoO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 39 - 39: oooOo0oo0oo
def oOOo0OO0oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOO0o0ooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 16 - 16: IiI1i11I . III1iiIii . oO0o
def ii1OoO00o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oo0oOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 53 - 53: oO0o % iI11I1II1I1I - oooOo0oo0oo
def iii11i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Ooo0oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 100 - 100: o0ii1I
def O0O0OoO0o0OO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 61 - 61: ooOoO0O00 % Ii % i1i1I1IIii1II % OOooOOo % IiI1i11I + IiI1i11I
def oOoooOooooo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + II1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 64 - 64: Ii / oOo0O0Ooo
def OOiiI1iii1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o0oooiIIIII1iiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 42 , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 43 - 43: I11i * ii
def ooO0O0O0ooOOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1iI111iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIIIiIi , url , iiIIIiIi1IIi , IIo0o0O0O00oOOo , OoOo000oOo0oo in IIi :
  I1I1II1I11 ( iIIIiIi , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , OoOo000oOo0oo )
 I1iI1ii1II ( 'movies' , 'MAIN' )
 if 65 - 65: oO0o * Iii
 if 37 - 37: o0ii1I % oO0o . i1IiiiI1iI + ooOoO0O00
 if 85 - 85: I1ii11iIi11i % Ii1I / oooOo0oo0oo
 if 65 - 65: i1iIi + III1iiIii - OOooOOo % IIiIiII11i - iI11I1II1I1I
 if 39 - 39: oOo0O0Ooo + Ii1I - Ii
 if 43 - 43: iI11I1II1I1I
 if 73 - 73: OOooOOo + I11i
 if 58 - 58: ooOoO0O00 * Ii1I % IiI1i11I . oO0o % III1iiIii % Iii
 if 63 - 63: Ii1I % i1iIi % Ii1I
def iII1I ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iii11OO0oO , oooo0oOOoO000 , Oo00o00Oo in os . walk ( o0 ) :
     oOooO00OOoO = 0
     oOooO00OOoO += len ( Oo00o00Oo )
     if oOooO00OOoO > 0 :
      for O0oO0 in Oo00o00Oo :
       os . unlink ( os . path . join ( iii11OO0oO , O0oO0 ) )
  IiIiII = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( IiIiII )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 99 - 99: ii - ooOoO0O00 % I11i / I11i + III1iiIii
 if 96 - 96: ii + oooOo0oo0oo - i1IiiiI1iI / i1i1I1IIii1II % i1i1I1IIii1II
 if 34 - 34: III1iiIii
 if 55 - 55: Ii1I
 if 79 - 79: oooOo0oo0oo + I11i % IiI1i11I . i1i1I1IIii1II
 if 49 - 49: o0ii1I + Ii * OOooOOo . OOooOOo . Ii1I . I1ii11iIi11i
 if 61 - 61: Iii / oooOo0oo0oo
 if 85 - 85: OOooOOo - Iii . OOooOOo . OOooOOo
def iiIi1 ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 62 - 62: III1iiIii % ii * oO0o + oO0o % o0ii1I % IiI1i11I
def oOoo ( url ) :
 OoOO0OOOO0 = os . path . join ( oooOOOOO , 'addon_data' )
 OooOOo0ooO = [
 ( OoOO0OOOO0 ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( OoOO0OOOO0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OoOO0OOOO0 , 'plugin.video.itv' , 'Images' ) ) ]
 if 6 - 6: ii . i1i1I1IIii1II / Ii / i1iIi + i1i1I1IIii1II . I1ii11iIi11i
 OoOOo0o00 = 0
 if 63 - 63: IIiIiII11i - Ii1I * IIiIiII11i
 for ooo00Ooo in OooOOo0ooO :
  if os . path . exists ( ooo00Ooo ) and not ooo00Ooo in [ oo0o0O00 , OoOO0OOOO0 ] :
   for iii11OO0oO , oooo0oOOoO000 , Oo00o00Oo in os . walk ( ooo00Ooo ) :
    oOooO00OOoO = 0
    oOooO00OOoO += len ( Oo00o00Oo )
    if oOooO00OOoO > 0 :
     for O0oO0 in Oo00o00Oo :
      if not O0oO0 in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( iii11OO0oO , O0oO0 ) )
       except :
        pass
      else : O00Oooo ( 'Ignore Log File: %s' % O0oO0 )
     for oOo00OO0ooOOO in oooo0oOOoO000 :
      try :
       shutil . rmtree ( os . path . join ( iii11OO0oO , oOo00OO0ooOOO ) )
       OoOOo0o00 += 1
       O00Oooo ( "[Success] cleared %s files from %s" % ( str ( oOooO00OOoO ) , os . path . join ( ooo00Ooo , oOo00OO0ooOOO ) ) )
      except :
       O00Oooo ( "[Failed] to wipe cache in: %s" % os . path . join ( ooo00Ooo , oOo00OO0ooOOO ) )
  else :
   for iii11OO0oO , oooo0oOOoO000 , Oo00o00Oo in os . walk ( ooo00Ooo ) :
    for oOo00OO0ooOOO in oooo0oOOoO000 :
     if 'cache' in oOo00OO0ooOOO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iii11OO0oO , oOo00OO0ooOOO ) )
       OoOOo0o00 += 1
       O00Oooo ( "[Success] wiped %s " % os . path . join ( ooo00Ooo , oOo00OO0ooOOO ) )
      except :
       O00Oooo ( "[Failed] to wipe cache in: %s" % os . path . join ( ooo00Ooo , oOo00OO0ooOOO ) )
       if 92 - 92: oO0o % i1iIi * o0o00Oo0O % iI11I1II1I1I / ooOoO0O00 / OOooOOo
 iiIi1 ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % OoOOo0o00 )
 if 67 - 67: i1IiiiI1iI + Iii + i1IiiiI1iI . oooOo0oo0oo % I11i / i1iIi
 if 78 - 78: Ii1I . o0o00Oo0O
 if 56 - 56: i1i1I1IIii1II - ooOoO0O00 * o0o00Oo0O / Iii * oOo0O0Ooo . Iii
 if 54 - 54: Ii % ooOoO0O00 + I1ii11iIi11i / OOooOOo
 if 26 - 26: Iii . Ii1I
 if 55 - 55: OOooOOo * i1IiiiI1iI % oO0o - oO0o
 if 34 - 34: o0o00Oo0O * oO0o - i1i1I1IIii1II - III1iiIii * o0ii1I . IIiIiII11i
def o00O0o00oo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iiI1iIIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iii11OO0oO , oooo0oOOoO000 , Oo00o00Oo in os . walk ( iiI1iIIi1I ) :
   oOooO00OOoO = 0
   oOooO00OOoO += len ( Oo00o00Oo )
   if 72 - 72: oO0o
   if 67 - 67: o0ii1I * ii . i1i1I1IIii1II * Iii * i1i1I1IIii1II - I1ii11iIi11i
   if oOooO00OOoO > 0 :
    if 82 - 82: III1iiIii
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( oOooO00OOoO ) + " files found" , "Do you want to delete them?" ) :
     if 42 - 42: Iii . oO0o * i1iIi
     for O0oO0 in Oo00o00Oo :
      os . unlink ( os . path . join ( iii11OO0oO , O0oO0 ) )
     for oOo00OO0ooOOO in oooo0oOOoO000 :
      shutil . rmtree ( os . path . join ( iii11OO0oO , oOo00OO0ooOOO ) )
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
 if 1 - 1: i1IiiiI1iI % IiI1i11I / iI11I1II1I1I * iI11I1II1I1I * i1iIi % IIiIiII11i
 if 59 - 59: III1iiIii
 if 21 - 21: ooOoO0O00 + I1ii11iIi11i + Iii
 if 10 - 10: oOo0O0Ooo - IIiIiII11i - IIiIiII11i + ii . III1iiIii / o0o00Oo0O
 if 31 - 31: III1iiIii + IiI1i11I . IiI1i11I
 if 12 - 12: iI11I1II1I1I + Ii1I / o0ii1I
 if 36 - 36: i1i1I1IIii1II + Ii1I + ii . I1ii11iIi11i % IiI1i11I * IIiIiII11i
 if 5 - 5: o0ii1I * IiI1i11I
 if 33 - 33: oOo0O0Ooo % Iii . i1IiiiI1iI / o0ii1I * IIiIiII11i * I11i
def ooO0O00Oo0o ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 iiI1iIIi1I = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iii11OO0oO , oooo0oOOoO000 , Oo00o00Oo in os . walk ( iiI1iIIi1I ) :
   oOooO00OOoO = 0
   oOooO00OOoO += len ( Oo00o00Oo )
   if 49 - 49: ooOoO0O00 * Ii
   if 47 - 47: IIiIiII11i / I1ii11iIi11i
   if oOooO00OOoO > 0 :
    if 38 - 38: oooOo0oo0oo . IiI1i11I / o0o00Oo0O . o0ii1I / OOooOOo
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( oOooO00OOoO ) + " files found" , "Do you want to delete them?" ) :
     if 52 - 52: o0o00Oo0O / Ii * oOo0O0Ooo . ooOoO0O00
     for O0oO0 in Oo00o00Oo :
      os . unlink ( os . path . join ( iii11OO0oO , O0oO0 ) )
     for oOo00OO0ooOOO in oooo0oOOoO000 :
      shutil . rmtree ( os . path . join ( iii11OO0oO , oOo00OO0ooOOO ) )
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
 oOoo ( url )
 return
 if 50 - 50: ii . IiI1i11I % I11i
 if 6 - 6: i1iIi - ooOoO0O00 . o0o00Oo0O . ooOoO0O00 . OOooOOo
 if 42 - 42: Ii * o0o00Oo0O % Ii + oooOo0oo0oo
 if 64 - 64: oOo0O0Ooo / OOooOOo
 if 6 - 6: Ii - IiI1i11I * ooOoO0O00 - IiI1i11I
 if 8 - 8: Iii / Ii . o0o00Oo0O / oO0o * i1i1I1IIii1II + i1IiiiI1iI
 if 91 - 91: oOo0O0Ooo
 if 84 - 84: o0o00Oo0O % o0ii1I
 if 3 - 3: oOo0O0Ooo . Iii / Ii1I
 if 2 - 2: III1iiIii + Iii / iI11I1II1I1I . Ii . ooOoO0O00 * i1iIi
def IIoOoo0oooo ( url , name ) :
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iI11 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 I1IiiI1IIi = os . path . join ( o00oo0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( I1IiiI1IIi ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   iI11 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
   try :
    os . remove ( iI11 )
    print '=== GenieTv - REMOVING    ' + str ( iI11 ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   OoO0oO0oo0O = open ( iI11 , "w" )
   OoO0oO0oo0O . write ( iiI111I1iIiI )
   OoO0oO0oo0O . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( iI11 ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  iI11 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
  try :
   os . remove ( iI11 )
   print '=== GenieTv - REMOVING    ' + str ( iI11 ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  OoO0oO0oo0O = open ( iI11 , "w" )
  OoO0oO0oo0O . write ( iiI111I1iIiI )
  OoO0oO0oo0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iI11 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 27 - 27: IIiIiII11i + Iii % I1ii11iIi11i - oO0o
def I1iIIIiIi ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iI11 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
 try :
  OoO0oO0oo0O = open ( iI11 ) . read ( )
  if 'zero' in OoO0oO0oo0O :
   name = '0CACHE'
  elif 'tuxen' in OoO0oO0oo0O :
   name = 'TUXENS'
  elif 'muckys' in OoO0oO0oo0O :
   name = 'MUCKYS'
  elif 'p2p1' in OoO0oO0oo0O :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in OoO0oO0oo0O :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in OoO0oO0oo0O :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 41 - 41: ii + i1iIi + oOo0O0Ooo + IIiIiII11i * o0ii1I
def i1IIIii1Ii1 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 o00oo0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iI11 = os . path . join ( o00oo0 , 'advancedsettings.xml' )
 try :
  os . remove ( iI11 )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( iI11 ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 70 - 70: III1iiIii
 if 78 - 78: I1ii11iIi11i * oooOo0oo0oo % Ii1I + oooOo0oo0oo % o0ii1I + III1iiIii
 if 58 - 58: ii % i1IiiiI1iI / I1ii11iIi11i % ii * OOooOOo . ii
 if 46 - 46: i1iIi * I11i % IIiIiII11i / i1IiiiI1iI
 if 29 - 29: oO0o - Ii % I1ii11iIi11i % I11i
 if 30 - 30: i1i1I1IIii1II - o0ii1I % o0ii1I
 if 8 - 8: III1iiIii
 if 68 - 68: III1iiIii . ii - Ii + Ii
 if 81 - 81: OOooOOo + IiI1i11I . Ii
 if 10 - 10: OOooOOo + Iii - iI11I1II1I1I - Iii
def iIiiII ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for O00o0OO0OO0oo , o0Oo00OoO000O , II1iii , O0oOOOO0o in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % O00o0OO0OO0oo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % II1iii , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % O0oOOOO0o )
  inc = inc + 1
  if 65 - 65: IIiIiII11i + i1i1I1IIii1II + oooOo0oo0oo + III1iiIii + ooOoO0O00
  if 33 - 33: i1iIi . oOo0O0Ooo . Ii % oO0o
  if 72 - 72: Ii1I / o0o00Oo0O % IIiIiII11i / IIiIiII11i
  if 48 - 48: oooOo0oo0oo % oooOo0oo0oo / iI11I1II1I1I - Ii
  if 57 - 57: Iii / III1iiIii * ooOoO0O00 + IIiIiII11i . I11i
  if 11 - 11: IIiIiII11i
  if 66 - 66: o0ii1I - oOo0O0Ooo . ii * i1IiiiI1iI
  if 16 - 16: III1iiIii * oO0o * Ii - i1iIi
  if 88 - 88: iI11I1II1I1I / o0ii1I * III1iiIii / i1IiiiI1iI
def iiii1i11i1 ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  o00oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iI11 = os . path . join ( o00oo0 , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  OoO0oO0oo0O = open ( iI11 , "w" )
  OoO0oO0oo0O . write ( iiI111I1iIiI )
  OoO0oO0oo0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iI11 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 39 - 39: o0ii1I
def IIiIi1ii11i ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  o00oo0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iI11 = os . path . join ( o00oo0 , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  OoO0oO0oo0O = open ( iI11 , "w" )
  OoO0oO0oo0O . write ( iiI111I1iIiI )
  OoO0oO0oo0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iI11 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 98 - 98: o0o00Oo0O % iI11I1II1I1I . III1iiIii - IIiIiII11i
 if 14 - 14: o0ii1I % i1iIi - OOooOOo
def oOOo0 ( ) :
 try :
  IIi1iIi = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IIi1iIi ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    i1ii1i = os . path . join ( IIi1iIi , "source.db" )
    os . unlink ( i1ii1i )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 6 - 6: oooOo0oo0oo + oO0o + oOo0O0Ooo / ii
 if 33 - 33: oOo0O0Ooo + iI11I1II1I1I . OOooOOo + i1IiiiI1iI % OOooOOo
 if 55 - 55: I11i / oO0o * I11i - Ii1I * i1iIi
 if 4 - 4: i1iIi
 if 71 - 71: i1IiiiI1iI + ooOoO0O00 * I1ii11iIi11i
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 51 - 51: ii * o0o00Oo0O - oO0o . I1ii11iIi11i % IIiIiII11i + III1iiIii
 if 48 - 48: III1iiIii . IIiIiII11i - Ii * IiI1i11I
 if 51 - 51: ii + Iii . IiI1i11I + Ii * IiI1i11I - oO0o
 if 60 - 60: IiI1i11I * iI11I1II1I1I . OOooOOo . I11i / iI11I1II1I1I
 if 36 - 36: ooOoO0O00 . ii - IIiIiII11i - OOooOOo - III1iiIii
 if 53 - 53: Ii1I - IIiIiII11i . Ii
 if 76 - 76: iI11I1II1I1I - I1ii11iIi11i
def OOOOoO00o0O ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; OOo00o000oOO0 = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OOo00o000oOO0 :
  II1IIOooO0oo = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; II1IIOooO0oo = xbmc . translatePath ( II1IIOooO0oo ) ;
  OooO0o00oO = os . path . join ( II1IIOooO0oo , ".." , ".." ) ; OooO0o00oO = os . path . abspath ( OooO0o00oO ) ; pluginlog ( "freshstart.main_list xbmcPath=" + OooO0o00oO ) ; Ii1iiiIIIii = False
  try :
   for iii11OO0oO , oooo0oOOoO000 , Oo00o00Oo in os . walk ( OooO0o00oO , topdown = True ) :
    oooo0oOOoO000 [ : ] = [ oOo00OO0ooOOO for oOo00OO0ooOOO in oooo0oOOoO000 if oOo00OO0ooOOO not in o0oO0 ]
    for iIIIiIi in Oo00o00Oo :
     try : os . remove ( os . path . join ( iii11OO0oO , iIIIiIi ) )
     except :
      if iIIIiIi not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Ii1iiiIIIii = True
      pluginlog ( "Error removing " + iii11OO0oO + " " + iIIIiIi )
    for iIIIiIi in oooo0oOOoO000 :
     try : os . rmdir ( os . path . join ( iii11OO0oO , iIIIiIi ) )
     except :
      if iIIIiIi not in [ "Database" , "userdata" ] : Ii1iiiIIIii = True
      pluginlog ( "Error removing " + iii11OO0oO + " " + iIIIiIi )
   if not Ii1iiiIIIii : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 O00Oo00OOoO0 ( )
 if 35 - 35: Iii - i1iIi . Ii1I + iI11I1II1I1I . oooOo0oo0oo / Iii
 if 72 - 72: ooOoO0O00 * Iii
 if 60 - 60: IiI1i11I
def O0Oo0OoO00OO ( ) :
 OoOOoo = [ ]
 ii1I1ii = sys . argv [ 2 ]
 if len ( ii1I1ii ) >= 2 :
  I1I1I1IIi1III = sys . argv [ 2 ]
  iIiI = I1I1I1IIi1III . replace ( '?' , '' )
  if ( I1I1I1IIi1III [ len ( I1I1I1IIi1III ) - 1 ] == '/' ) :
   I1I1I1IIi1III = I1I1I1IIi1III [ 0 : len ( I1I1I1IIi1III ) - 2 ]
  oooOI1ii1I1i1 = iIiI . split ( '&' )
  OoOOoo = { }
  for oOooo0OO0O0 in range ( len ( oooOI1ii1I1i1 ) ) :
   i11i = { }
   i11i = oooOI1ii1I1i1 [ oOooo0OO0O0 ] . split ( '=' )
   if ( len ( i11i ) ) == 2 :
    OoOOoo [ i11i [ 0 ] ] = i11i [ 1 ]
    if 31 - 31: Ii
 return OoOOoo
 if 9 - 9: Iii / i1IiiiI1iI + iI11I1II1I1I + oOo0O0Ooo - IIiIiII11i
O0OOoo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
iIIi1OoOo0O00 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i1I1Ii11II1i = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
iii11iiiiI1 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oO0oO0O = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iiO00OOo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
iII11I1iIiI = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iiiI1IiiIII1ii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
I1i11Iiii = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OOOo0O0oOOOoO0o = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OOO0o0ooO0 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
oo0oOoo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Ooo0oO0 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
IiIIi = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
II1II = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0oooiIIIII1iiI = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OOooooO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iiOo00ooO0 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
Oo000 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
Ii111III1i11I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
II1Iiiii111i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
IiOO0oo00OOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I1iI111iIi = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
I1IiI = base64 . decodestring ( 'Q1VOVA==' )
def OO0 ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 i1I11iIiII . setProperty ( 'fanart_image' , fanart )
 i1I11iIiII . setProperty ( "IsPlayable" , "true" )
 IiIIIIiIi = [ ]
 IiIIIIiIi . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 IiIIIIiIi . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 i1I11iIiII . addContextMenuItems ( IiIIIIiIi , replaceItems = True )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = False )
 return iiIii1I
def I1I1II1I11 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1I11iIiII . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OO0OO0OO = [ ]
  if showcontext == 'fav' :
   OO0OO0OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   OO0OO0OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1I11iIiII . addContextMenuItems ( OO0OO0OO )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = True )
 return iiIii1I
 if 59 - 59: iI11I1II1I1I . I1ii11iIi11i * Iii
def Ii1I1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 Ii1I11I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiIii1I = True
 i1I11iIiII = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1I11iIiII . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i1I11iIiII . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  OO0OO0OO = [ ]
  if showcontext == 'fav' :
   OO0OO0OO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   OO0OO0OO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i1I11iIiII . addContextMenuItems ( OO0OO0OO )
 iiIii1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1I11I , listitem = i1I11iIiII , isFolder = False )
 return iiIii1I
 if 29 - 29: I1ii11iIi11i - oOo0O0Ooo * Iii
 if 58 - 58: ooOoO0O00 * o0ii1I / i1iIi % iI11I1II1I1I
I1I1I1IIi1III = O0Oo0OoO00OO ( )
oOOo0O00o = None
iIIIiIi = None
i1Ii11II = None
iiIIIiIi1IIi = None
IIo0o0O0O00oOOo = None
OoOo000oOo0oo = None
II1Iiii11 = None
Ii1 = None
if 20 - 20: i1IiiiI1iI * i1iIi % oO0o + oO0o
if 6 - 6: III1iiIii + oO0o
try :
 Ii1 = int ( I1I1I1IIi1III [ "fav_mode" ] )
except :
 pass
 if 13 - 13: o0o00Oo0O . oOo0O0Ooo % oO0o - Iii . o0o00Oo0O
try :
 oOOo0O00o = urllib . unquote_plus ( I1I1I1IIi1III [ "url" ] )
except :
 pass
try :
 iIIIiIi = urllib . unquote_plus ( I1I1I1IIi1III [ "name" ] )
except :
 pass
try :
 iiIIIiIi1IIi = urllib . unquote_plus ( I1I1I1IIi1III [ "iconimage" ] )
except :
 pass
try :
 i1Ii11II = int ( I1I1I1IIi1III [ "mode" ] )
except :
 pass
try :
 IIo0o0O0O00oOOo = urllib . unquote_plus ( I1I1I1IIi1III [ "fanart" ] )
except :
 pass
try :
 OoOo000oOo0oo = urllib . unquote_plus ( I1I1I1IIi1III [ "description" ] )
except :
 pass
 if 14 - 14: iI11I1II1I1I
 if 48 - 48: Ii * OOooOOo - oOo0O0Ooo + iI11I1II1I1I
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( i1Ii11II )
print "URL: " + str ( oOOo0O00o )
print "Name: " + str ( iIIIiIi )
print "IconImage: " + str ( iiIIIiIi1IIi )
if 20 - 20: Ii1I - iI11I1II1I1I . IiI1i11I
if 52 - 52: oO0o - i1IiiiI1iI
def I1iI1ii1II ( content , viewType ) :
 if 9 - 9: oOo0O0Ooo . Ii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 3 - 3: oOo0O0Ooo + Ii1I * i1IiiiI1iI - ooOoO0O00 . oooOo0oo0oo
if iiIIIiIi1IIi == None : iiIIIiIi1IIi = O0O
if IIo0o0O0O00oOOo == None : IIo0o0O0O00oOOo = Oo00OOOOO
if i1Ii11II == None :
 Iii1I1I11iiI1 ( )
 if 21 - 21: oooOo0oo0oo + I11i
elif i1Ii11II == 1 :
 oOOo0oO ( oOOo0O00o )
 if 39 - 39: OOooOOo . Iii * oooOo0oo0oo . ooOoO0O00
elif i1Ii11II == 44 :
 II11IiiIII ( oOOo0O00o )
 if 69 - 69: III1iiIii - ooOoO0O00 + I11i
elif i1Ii11II == 2 :
 iI11i ( )
 if 5 - 5: IIiIiII11i
elif i1Ii11II == 3 :
 IiiiIIIi11ii1 ( )
 if 88 - 88: ii % IIiIiII11i + III1iiIii + III1iiIii * I1ii11iIi11i
elif i1Ii11II == 21 :
 i1i1II ( )
 if 81 - 81: oOo0O0Ooo * i1iIi + i1IiiiI1iI
elif i1Ii11II == 4 :
 iIIiI ( )
 if 49 - 49: oOo0O0Ooo % i1i1I1IIii1II % IIiIiII11i * IIiIiII11i + ii + IiI1i11I
elif i1Ii11II == 5 :
 OO0O00 ( oOOo0O00o )
 if 58 - 58: Ii % iI11I1II1I1I + oO0o . Ii1I . oOo0O0Ooo
elif i1Ii11II == 6 :
 o00O0o00oo ( oOOo0O00o )
 if 54 - 54: IiI1i11I . oO0o . iI11I1II1I1I
elif i1Ii11II == 7 :
 IIoOoo0oooo ( oOOo0O00o , iIIIiIi )
 if 45 - 45: Ii1I + oOo0O0Ooo / Ii
elif i1Ii11II == 8 :
 I1iIIIiIi ( oOOo0O00o , iIIIiIi )
 if 45 - 45: III1iiIii / o0o00Oo0O * oOo0O0Ooo - oooOo0oo0oo * i1IiiiI1iI
elif i1Ii11II == 9 :
 FIXREPOSADDONS ( oOOo0O00o )
 if 19 - 19: OOooOOo / III1iiIii - oooOo0oo0oo * Ii % i1IiiiI1iI
elif i1Ii11II == 10 :
 OOOOo0o00OO0000 ( )
 if 98 - 98: III1iiIii + III1iiIii + oooOo0oo0oo / ooOoO0O00 + i1i1I1IIii1II
elif i1Ii11II == 11 :
 i1IIIii1Ii1 ( oOOo0O00o )
 if 53 - 53: OOooOOo
elif i1Ii11II == 12 :
 iIiiII ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 69 - 69: iI11I1II1I1I * oO0o / ii % Ii1I . oOo0O0Ooo % Iii
elif i1Ii11II == 13 :
 iII1I ( )
 if 40 - 40: Ii % i1i1I1IIii1II / oooOo0oo0oo
elif i1Ii11II == 14 :
 oOoo ( oOOo0O00o )
 if 85 - 85: oO0o % o0o00Oo0O . o0ii1I . IiI1i11I . IiI1i11I
elif i1Ii11II == 15 :
 OoO00oo0 ( )
 if 90 - 90: I11i - I1ii11iIi11i / i1iIi / ooOoO0O00 - o0ii1I
elif i1Ii11II == 16 :
 iiii1i11i1 ( oOOo0O00o , iIIIiIi )
 if 43 - 43: Ii - ii % i1iIi
elif i1Ii11II == 17 :
 IIiIi1ii11i ( oOOo0O00o , iIIIiIi )
 if 55 - 55: i1i1I1IIii1II % I1ii11iIi11i % III1iiIii
elif i1Ii11II == 18 :
 oOOo0 ( )
 if 65 - 65: III1iiIii * III1iiIii
elif i1Ii11II == 19 :
 O0oo ( oOOo0O00o )
 if 60 - 60: i1iIi
elif i1Ii11II == 40 :
 o0000oO ( iIIIiIi , oOOo0O00o , OoOo000oOo0oo )
 if 92 - 92: o0o00Oo0O % III1iiIii
elif i1Ii11II == 42 :
 iIII11I ( iIIIiIi , oOOo0O00o , OoOo000oOo0oo )
 if 15 - 15: o0o00Oo0O % ooOoO0O00 - oooOo0oo0oo . III1iiIii
elif i1Ii11II == 43 :
 OOOO00 ( oOOo0O00o )
 if 1 - 1: oOo0O0Ooo
elif i1Ii11II == 20 :
 iii11III1I ( oOOo0O00o )
 if 40 - 40: I11i % Iii % o0o00Oo0O
elif i1Ii11II == 22 :
 i11Ii1 ( oOOo0O00o )
 if 88 - 88: I11i - i1i1I1IIii1II
elif i1Ii11II == 23 :
 O0OoO0OOOo ( oOOo0O00o )
 if 73 - 73: IIiIiII11i
elif i1Ii11II == 24 :
 o0i11iiII11i ( oOOo0O00o )
 if 7 - 7: o0o00Oo0O / oO0o
elif i1Ii11II == 25 :
 oOOo0OO0oo ( oOOo0O00o )
 if 90 - 90: IiI1i11I % i1i1I1IIii1II / iI11I1II1I1I
elif i1Ii11II == 26 :
 ii1OoO00o ( oOOo0O00o )
 if 52 - 52: oOo0O0Ooo / I11i
elif i1Ii11II == 27 :
 iii11i ( oOOo0O00o )
 if 20 - 20: i1IiiiI1iI . oOo0O0Ooo - iI11I1II1I1I / IiI1i11I
elif i1Ii11II == 28 :
 O0O0OoO0o0OO ( oOOo0O00o )
 if 46 - 46: i1IiiiI1iI . Ii
elif i1Ii11II == 29 :
 oOoooOooooo0 ( oOOo0O00o )
 if 89 - 89: oO0o - oooOo0oo0oo - ooOoO0O00 - oO0o % iI11I1II1I1I
elif i1Ii11II == 30 :
 oOoO ( oOOo0O00o )
 if 52 - 52: I11i * o0o00Oo0O + Ii1I
elif i1Ii11II == 31 :
 OOiiI1iii1I ( oOOo0O00o )
 if 83 - 83: Iii + oooOo0oo0oo - ii
elif i1Ii11II == 32 :
 I1ii1iI ( )
 if 7 - 7: III1iiIii % i1iIi / ii / I11i + oO0o - oO0o
elif i1Ii11II == 33 :
 i1i1 ( )
 if 15 - 15: ooOoO0O00 + oooOo0oo0oo / o0ii1I
elif i1Ii11II == 35 :
 oOOoOOooO0 ( oOOo0O00o )
 if 51 - 51: oooOo0oo0oo + o0o00Oo0O
elif i1Ii11II == 34 :
 IIii1Ii1i1ii1 ( oOOo0O00o )
 if 91 - 91: Ii + I11i % oO0o / i1i1I1IIii1II - ooOoO0O00
elif i1Ii11II == 36 :
 O00oooO00oo ( oOOo0O00o )
 if 82 - 82: o0ii1I . ii + ii % oO0o % Ii1I
elif i1Ii11II == 37 :
 Oo0OOOOOOO0oo ( oOOo0O00o )
 if 65 - 65: I1ii11iIi11i . Iii
elif i1Ii11II == 38 :
 I11Iii11i11I1 ( oOOo0O00o )
 if 7 - 7: I1ii11iIi11i * IIiIiII11i
elif i1Ii11II == 41 :
 OOOOoO00o0O ( I1I1I1IIi1III )
 if 11 - 11: OOooOOo % ii
elif i1Ii11II == 39 :
 ooO0O0O0ooOOO ( oOOo0O00o )
 if 92 - 92: OOooOOo - IiI1i11I * o0ii1I - ooOoO0O00
elif i1Ii11II == 45 :
 TEXTS ( )
 if 87 - 87: o0ii1I * i1IiiiI1iI + iI11I1II1I1I * I11i * iI11I1II1I1I . Iii
elif i1Ii11II == 46 :
 iIiIi11 ( )
 if 66 - 66: o0ii1I / oO0o . o0o00Oo0O . Iii % ii / oooOo0oo0oo
elif i1Ii11II == 47 :
 GEVID ( )
 if 49 - 49: oOo0O0Ooo * IiI1i11I - oO0o % o0ii1I + o0ii1I * i1IiiiI1iI
elif i1Ii11II == 48 :
 Oo00o00 ( iIIIiIi , oOOo0O00o , OoOo000oOo0oo )
 if 94 - 94: OOooOOo - Iii + o0ii1I + OOooOOo + IIiIiII11i
elif i1Ii11II == 49 :
 II1III1I1I1Ii ( )
 if 61 - 61: III1iiIii + o0ii1I / i1i1I1IIii1II . ii + IiI1i11I
elif i1Ii11II == 22222 :
 i11i1i ( oOOo0O00o )
 if 29 - 29: oooOo0oo0oo
elif i1Ii11II == 222225 :
 IiIIiIIIiIii ( oOOo0O00o )
 if 69 - 69: i1i1I1IIii1II % ii * IiI1i11I
elif i1Ii11II == 222 :
 oO0Ooo ( oOOo0O00o )
 if 58 - 58: i1i1I1IIii1II / Ii . OOooOOo % o0o00Oo0O / iI11I1II1I1I
elif i1Ii11II == 2222222 :
 I11iiiiI1i ( oOOo0O00o )
 if 50 - 50: i1IiiiI1iI . Iii / o0o00Oo0O . Iii
elif i1Ii11II == 222222 :
 iiiiIIiiII1Iii1 ( oOOo0O00o , iIIIiIi )
 if 91 - 91: Ii . Ii1I + Iii
elif i1Ii11II == 333 :
 iII1 ( oOOo0O00o )
 if 67 - 67: Ii1I * i1IiiiI1iI * oOo0O0Ooo / Iii - III1iiIii + i1i1I1IIii1II
 if 11 - 11: o0o00Oo0O + ooOoO0O00 / I11i * oO0o
elif i1Ii11II == 1020 :
 ii1I11ii ( )
 if 64 - 64: ooOoO0O00 % III1iiIii . i1iIi . iI11I1II1I1I + oO0o - iI11I1II1I1I
elif i1Ii11II == 1021 :
 ANIMEEP ( )
 if 52 - 52: IIiIiII11i - III1iiIii
elif i1Ii11II == 1022 :
 ANIMEPLAY ( oOOo0O00o )
 if 91 - 91: iI11I1II1I1I + IiI1i11I . Iii % Ii - Ii + oOo0O0Ooo
elif i1Ii11II == 1001 :
 oOOiI ( )
 if 75 - 75: Ii1I / oOo0O0Ooo - iI11I1II1I1I / oO0o * oooOo0oo0oo
elif i1Ii11II == 1005 :
 I1iI1IiII ( )
 if 73 - 73: ii % III1iiIii / i1IiiiI1iI * Iii + ooOoO0O00 % Ii
elif i1Ii11II == 1007 :
 II11iIIoO00 ( oOOo0O00o )
 if 91 - 91: Ii
elif i1Ii11II == 1010 :
 i1iIii ( oOOo0O00o )
 if 6 - 6: o0o00Oo0O - iI11I1II1I1I + i1IiiiI1iI . I11i * Ii
elif i1Ii11II == 1011 :
 O0oo0O0OO0OOo ( oOOo0O00o )
 if 53 - 53: oooOo0oo0oo / oOo0O0Ooo / i1i1I1IIii1II * oooOo0oo0oo / ooOoO0O00 - i1IiiiI1iI
elif i1Ii11II == 1012 :
 ooOo000 ( oOOo0O00o )
 if 71 - 71: o0o00Oo0O + I1ii11iIi11i % i1i1I1IIii1II - I11i
elif i1Ii11II == 1030 :
 i111ii11I1 ( )
 if 82 - 82: iI11I1II1I1I
elif i1Ii11II == 1031 :
 iii1I1 ( oOOo0O00o , iiIIIiIi1IIi )
 if 64 - 64: i1iIi + oOo0O0Ooo % oooOo0oo0oo + IIiIiII11i
elif i1Ii11II == 1032 :
 III1IIIIIiiI ( oOOo0O00o )
 if 46 - 46: oOo0O0Ooo
elif i1Ii11II == 1006 :
 Parse . ParseURL ( oOOo0O00o )
 if 72 - 72: IiI1i11I
elif i1Ii11II == 2030 :
 Parse . addonParseURL ( oOOo0O00o )
 if 100 - 100: oOo0O0Ooo
elif i1Ii11II == 2031 :
 Parse . apkParseURL ( oOOo0O00o )
 if 55 - 55: ooOoO0O00 % III1iiIii
elif i1Ii11II == 2032 :
 Parse . ParseBOSS ( oOOo0O00o )
 if 44 - 44: i1i1I1IIii1II - iI11I1II1I1I / i1iIi - iI11I1II1I1I % ooOoO0O00 + i1iIi
elif i1Ii11II == 1002 :
 oo0Oo0oo000 ( oOOo0O00o )
 if 74 - 74: Iii . OOooOOo + OOooOOo
elif i1Ii11II == 1003 :
 Ii11I111Ii ( oOOo0O00o , iiIIIiIi1IIi )
 if 87 - 87: III1iiIii + I11i . ooOoO0O00 % i1IiiiI1iI
elif i1Ii11II == 1004 :
 iIiIIiIII1I ( oOOo0O00o )
 if 44 - 44: I1ii11iIi11i - oooOo0oo0oo . o0ii1I * ii
elif i1Ii11II == 1008 :
 O0oOoO0o0oO ( )
 if 93 - 93: oO0o . oO0o
elif i1Ii11II == 1009 :
 iI11i1I ( oOOo0O00o )
 if 52 - 52: oooOo0oo0oo . i1i1I1IIii1II / I1ii11iIi11i . ii % Ii1I
elif i1Ii11II == 2001 :
 OOoooi1i1I11I ( )
 if 65 - 65: i1iIi % IIiIiII11i . IiI1i11I - iI11I1II1I1I - oOo0O0Ooo
elif i1Ii11II == 2002 :
 o00I11II1iI ( oOOo0O00o )
 if 63 - 63: oOo0O0Ooo . OOooOOo - IIiIiII11i
elif i1Ii11II == 1013 :
 iii11 ( )
elif i1Ii11II == 10111113 :
 oo0O00o0O0Oo ( oOOo0O00o )
 if 55 - 55: i1iIi - I11i
elif i1Ii11II == 1014 :
 i111i ( )
 if 32 - 32: i1IiiiI1iI * o0ii1I / i1IiiiI1iI . OOooOOo + Ii1I - i1iIi
elif i1Ii11II == 1015 :
 iII1I1i11iIi ( oOOo0O00o )
 if 14 - 14: III1iiIii * o0o00Oo0O + o0o00Oo0O - i1iIi . Ii - III1iiIii
elif i1Ii11II == 1016 :
 iiIIiii ( oOOo0O00o , iiIIIiIi1IIi , iIIIiIi )
 if 37 - 37: Iii
elif i1Ii11II == 1017 :
 O0O0oOOo0O ( )
 if 19 - 19: ii % i1IiiiI1iI
elif i1Ii11II == 1018 :
 ii11i ( oOOo0O00o )
 if 57 - 57: OOooOOo + ooOoO0O00 . iI11I1II1I1I . iI11I1II1I1I / iI11I1II1I1I % i1i1I1IIii1II
elif i1Ii11II == 1019 :
 OoOo00o0OO ( oOOo0O00o )
elif i1Ii11II == 10190 :
 iI1IIIii ( oOOo0O00o )
 if 7 - 7: Ii * Ii1I / oO0o * i1i1I1IIii1II
elif i1Ii11II == 1023 :
 oOOoO0O ( )
 if 35 - 35: III1iiIii . ooOoO0O00 + Ii1I . III1iiIii + i1iIi . i1i1I1IIii1II
elif i1Ii11II == 1024 :
 iI1IIiIi1i ( oOOo0O00o )
 if 2 - 2: IIiIiII11i
elif i1Ii11II == 1025 :
 OooIiii1ii ( oOOo0O00o )
 if 18 - 18: iI11I1II1I1I % Ii1I % I1ii11iIi11i
elif i1Ii11II == 4001 :
 o000oo ( )
 if 47 - 47: i1iIi - oOo0O0Ooo % oooOo0oo0oo * o0ii1I % oOo0O0Ooo
elif i1Ii11II == 4002 :
 i1i1ii ( )
 if 95 - 95: oO0o + OOooOOo % I1ii11iIi11i . o0ii1I * oOo0O0Ooo + i1IiiiI1iI
elif i1Ii11II == 4003 :
 O0oO0oOO00Oo ( )
 if 22 - 22: I1ii11iIi11i . oO0o
elif i1Ii11II == 4004 :
 O0OoO0ooOO0o ( )
 if 55 - 55: I1ii11iIi11i % ii * IIiIiII11i % ii
elif i1Ii11II == 4005 :
 ii1O000OOO0OOo ( )
 if 30 - 30: i1IiiiI1iI / I11i + ii + OOooOOo + oO0o
elif i1Ii11II == 4006 :
 I1Iiiiiii ( )
 if 40 - 40: ii / III1iiIii
elif i1Ii11II == 4007 :
 O0ooooo0OOOO0 ( )
 if 82 - 82: Ii - i1i1I1IIii1II - ooOoO0O00
elif i1Ii11II == 4008 :
 O0Oo ( )
 if 78 - 78: i1i1I1IIii1II % IiI1i11I / ooOoO0O00 / i1iIi
elif i1Ii11II == 40099 : iiI1ii111 ( )
elif i1Ii11II == 4009 : I1iI1I1ii1 ( )
elif i1Ii11II == 4010 : oO0oOOOooo ( )
elif i1Ii11II == 3000 :
 i1IIII1iII ( )
 if 44 - 44: I11i + o0ii1I + oOo0O0Ooo % o0o00Oo0O
elif i1Ii11II == 3001 :
 Oo00Oo00Oooo ( )
 if 100 - 100: ii
elif i1Ii11II == 3002 :
 iIIIiI1iII1i ( oOOo0O00o )
 if 27 - 27: Ii % IIiIiII11i + i1IiiiI1iI
elif i1Ii11II == 3003 :
 Ii1I11Ii1iI ( oOOo0O00o )
 if 76 - 76: oooOo0oo0oo - i1IiiiI1iI + iI11I1II1I1I + oOo0O0Ooo * i1i1I1IIii1II
elif i1Ii11II == 3004 :
 i111iii1I11I ( oOOo0O00o )
 if 93 - 93: Ii * Ii - oOo0O0Ooo + iI11I1II1I1I * Ii
elif i1Ii11II == 404 :
 I1iIIiI ( iIIIiIi , oOOo0O00o , iiIIIiIi1IIi )
 if 14 - 14: i1iIi . ii . oOo0O0Ooo - III1iiIii + iI11I1II1I1I
elif i1Ii11II == 405 :
 o0ooo ( oOOo0O00o )
 if 47 - 47: oooOo0oo0oo % ooOoO0O00
elif i1Ii11II == 7030 :
 OoO000 ( )
 if 23 - 23: o0ii1I * o0ii1I / Iii
elif i1Ii11II == 7021 :
 ooO0o0Oo ( iIIIiIi )
 if 11 - 11: oooOo0oo0oo
elif i1Ii11II == 7022 :
 ooOoOO0O00Ooo ( iIIIiIi )
 if 58 - 58: oO0o * ii
elif i1Ii11II == 7000 :
 O00000oooOO ( iIIIiIi , oOOo0O00o , img )
 if 47 - 47: IiI1i11I - I1ii11iIi11i
elif i1Ii11II == 7050 :
 I1i11IIIi ( oOOo0O00o )
 if 19 - 19: o0o00Oo0O . ooOoO0O00 + Iii / IIiIiII11i + i1iIi
elif i1Ii11II == 7051 :
 Oo0OOOOOOOo0O ( oOOo0O00o )
 if 26 - 26: o0ii1I * i1i1I1IIii1II % oOo0O0Ooo - oooOo0oo0oo . i1IiiiI1iI
elif i1Ii11II == 7052 :
 i1Iiiiiii ( oOOo0O00o )
 if 35 - 35: ooOoO0O00 % Ii + o0ii1I
elif i1Ii11II == 7053 :
 Oo000O00o0O ( oOOo0O00o )
 if 14 - 14: oO0o * ii
elif i1Ii11II == 7054 :
 CoolPlay ( oOOo0O00o )
 if 45 - 45: iI11I1II1I1I * oOo0O0Ooo . OOooOOo
elif i1Ii11II == 7060 :
 ooo0ooo0 ( )
 if 97 - 97: Iii % IIiIiII11i % o0ii1I . IIiIiII11i . iI11I1II1I1I
elif i1Ii11II == 7061 :
 o00oOoOo0 ( oOOo0O00o )
 if 98 - 98: Ii + o0o00Oo0O - o0o00Oo0O - IiI1i11I
elif i1Ii11II == 7063 :
 oO000oOo0oO0 ( oOOo0O00o )
 if 25 - 25: i1i1I1IIii1II / o0o00Oo0O + i1IiiiI1iI % Ii / oOo0O0Ooo
elif i1Ii11II == 7062 :
 i11i1i1i ( oOOo0O00o )
 if 62 - 62: IiI1i11I . Iii * ooOoO0O00 + IiI1i11I
elif i1Ii11II == 7064 :
 NATatozcat ( )
 if 95 - 95: o0ii1I / I11i % i1iIi - oOo0O0Ooo / oooOo0oo0oo * oooOo0oo0oo
elif i1Ii11II == 7067 :
 OoO00O ( oOOo0O00o )
 if 6 - 6: oO0o % III1iiIii + iI11I1II1I1I
elif i1Ii11II == 7066 :
 NATatozA ( oOOo0O00o )
 if 18 - 18: IIiIiII11i . o0ii1I + OOooOOo + o0o00Oo0O - Iii
elif i1Ii11II == 7065 :
 O0oo0ooO ( oOOo0O00o )
 if 30 - 30: IIiIiII11i
elif i1Ii11II == 7070 :
 Ii11I111IIIIi ( )
 if 26 - 26: Iii - ooOoO0O00 - I1ii11iIi11i * o0o00Oo0O * oooOo0oo0oo . ii
elif i1Ii11II == 7071 :
 DIZIlist ( oOOo0O00o )
 if 99 - 99: i1i1I1IIii1II . oO0o / oooOo0oo0oo
elif i1Ii11II == 7072 :
 DIZIpull ( oOOo0O00o )
 if 12 - 12: iI11I1II1I1I + i1iIi * i1IiiiI1iI % ii / iI11I1II1I1I
elif i1Ii11II == 7073 :
 WATCHDIZI ( oOOo0O00o )
 if 43 - 43: o0o00Oo0O . ooOoO0O00 - ii - ooOoO0O00 - Ii1I
elif i1Ii11II == 7002 :
 iI11ii1i ( )
 if 8 - 8: OOooOOo / o0ii1I
elif i1Ii11II == 7003 :
 II1iII1IIIIi ( oOOo0O00o )
 if 12 - 12: iI11I1II1I1I
elif i1Ii11II == 7004 :
 i1IIIIi1I ( oOOo0O00o )
 if 52 - 52: i1i1I1IIii1II . Ii1I + i1i1I1IIii1II
elif i1Ii11II == 7020 :
 O0Oo0O0O0o0 ( oOOo0O00o )
 if 73 - 73: IIiIiII11i / Ii / i1iIi
elif i1Ii11II == 7001 :
 Ooo0o00o0o ( )
 if 1 - 1: IiI1i11I + OOooOOo / III1iiIii - oOo0O0Ooo % oOo0O0Ooo
elif i1Ii11II == 7010 :
 oo0OoI1IiI11 ( oOOo0O00o )
 if 6 - 6: OOooOOo - ooOoO0O00 + IIiIiII11i % i1i1I1IIii1II
elif i1Ii11II == 7011 :
 o0OOOO00O ( oOOo0O00o )
 if 72 - 72: oooOo0oo0oo + oooOo0oo0oo
elif i1Ii11II == 7012 :
 oo0o0 ( oOOo0O00o )
 if 30 - 30: Iii
elif i1Ii11II == 7013 :
 cnfTVPlay2 ( oOOo0O00o )
elif i1Ii11II == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oOOo0O00o )
elif i1Ii11II == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oOOo0O00o )
elif i1Ii11II == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iIIIiIi , oOOo0O00o , iiIIIiIi1IIi )
elif i1Ii11II == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif i1Ii11II == 7018 :
 i11111 ( )
elif i1Ii11II == 7019 :
 CNF_Studio_Indexer . List_Movies ( oOOo0O00o )
elif i1Ii11II == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oOOo0O00o )
elif i1Ii11II == 7024 :
 CNF_Studio_Indexer . Box_Office ( oOOo0O00o )
 if 15 - 15: o0o00Oo0O - ooOoO0O00 . iI11I1II1I1I - Ii / o0ii1I
elif i1Ii11II == 8000 :
 OO0O0oooo0 ( )
elif i1Ii11II == 8001 :
 oO0o0oo ( )
elif i1Ii11II == 8002 :
 o0o00O00Oo0 ( )
elif i1Ii11II == 8003 :
 i11i1IiIi11 ( )
elif i1Ii11II == 8004 :
 OOoooiII1 ( )
elif i1Ii11II == 8005 :
 i11iI ( )
elif i1Ii11II == 8006 :
 I1i1I1i1I1 ( iIIIiIi , oOOo0O00o )
elif i1Ii11II == 8030 :
 O0O00 ( oOOo0O00o )
elif i1Ii11II == 8045 :
 oOoOoo0 ( oOOo0O00o )
elif i1Ii11II == 8046 :
 iIO0O0Ooo0 ( oOOo0O00o )
elif i1Ii11II == 8047 :
 oo0OOo ( oOOo0O00o )
elif i1Ii11II == 8048 :
 O0ooOooOOoo ( oOOo0O00o )
elif i1Ii11II == 8049 :
 III1II11 ( oOOo0O00o )
elif i1Ii11II == 804900 :
 iI1IiiII1 ( oOOo0O00o )
elif i1Ii11II == 8020 :
 iIi1 ( )
elif i1Ii11II == 8021 :
 Ooo0OO0 ( oOOo0O00o )
elif i1Ii11II == 8022 :
 o0o0oO ( oOOo0O00o )
elif i1Ii11II == 8023 :
 IiI1IIiIII ( oOOo0O00o )
elif i1Ii11II == 8040 :
 ii11i11i1 ( )
elif i1Ii11II == 8041 :
 oOoO0O0o ( oOOo0O00o )
elif i1Ii11II == 8042 :
 O0O0oOo0o0o0 ( oOOo0O00o )
elif i1Ii11II == 8043 :
 yt . PlayVideo ( oOOo0O00o )
elif i1Ii11II == 8044 :
 oOOOIii111111 ( oOOo0O00o )
elif i1Ii11II == 8060 :
 OoOIiiiii111i1ii ( )
elif i1Ii11II == 8061 :
 IiIiiIIiIi ( oOOo0O00o )
elif i1Ii11II == 8064 :
 oOoooo000Oo00 ( )
elif i1Ii11II == 8065 :
 ii11 ( oOOo0O00o )
elif i1Ii11II == 8070 :
 iiioO000oO0oO ( )
elif i1Ii11II == 8071 :
 iII111i1 ( oOOo0O00o )
elif i1Ii11II == 7080 :
 i11Ii ( oOOo0O00o )
elif i1Ii11II == 8090 :
 iIIiiI1Ii1II ( )
elif i1Ii11II == 8091 :
 iIiI1Iii11II ( oOOo0O00o )
elif i1Ii11II == 8092 :
 OOOoooO0o0o ( oOOo0O00o )
elif i1Ii11II == 8093 :
 ii11III1 ( oOOo0O00o )
elif i1Ii11II == 8081 :
 iIi1ii1I1iiI ( )
elif i1Ii11II == 8062 :
 iIooo0O0O0OO ( oOOo0O00o )
elif i1Ii11II == 8063 :
 i11Iiiiii11II ( oOOo0O00o )
elif i1Ii11II == 8050 :
 i1iiIi1IiiiI ( )
elif i1Ii11II == 8051 :
 OO0oooOO ( oOOo0O00o )
elif i1Ii11II == 8052 :
 IIIi1iiIIiiiI ( oOOo0O00o )
elif i1Ii11II == 8085 :
 iII ( )
elif i1Ii11II == 8086 :
 II11iII ( oOOo0O00o )
elif i1Ii11II == 8087 :
 ii111I111i ( oOOo0O00o )
elif i1Ii11II == 8088 :
 II11111I ( oOOo0O00o , iIIIiIi )
elif i1Ii11II == 9000 :
 iIIiiIii111 ( )
elif i1Ii11II == 1111 :
 O0o00 ( )
elif i1Ii11II == 9001 :
 OoOo0oOooOoOO ( )
elif i1Ii11II == 9002 :
 i1i1I111iIi1 ( )
elif i1Ii11II == 9003 :
 OoO0o00O0oOOo ( )
elif i1Ii11II == 9004 :
 World1 ( )
elif i1Ii11II == 9005 :
 World2 ( oOOo0O00o )
elif i1Ii11II == 9006 :
 World3 ( oOOo0O00o )
elif i1Ii11II == 9007 :
 ii1I11iIi ( )
elif i1Ii11II == 9008 :
 IiO00oo0o0ooO ( oOOo0O00o )
elif i1Ii11II == 9009 :
 OOO0o0O ( oOOo0O00o )
elif i1Ii11II == 9010 :
 OO0OoO0 ( )
elif i1Ii11II == 9011 :
 ooO0ooO ( oOOo0O00o )
elif i1Ii11II == 50 :
 I1iII ( oOOo0O00o )
elif i1Ii11II == 9020 :
 champlist ( )
elif i1Ii11II == 9021 :
 IiIII ( )
elif i1Ii11II == 9022 :
 iII1iII ( )
elif i1Ii11II == 9023 :
 iiii11i1ii1 ( )
elif i1Ii11II == 9024 :
 I1i1I1IIIi1II ( oOOo0O00o )
elif i1Ii11II == 9030 :
 IIIIi11i ( oOOo0O00o )
elif i1Ii11II == 9031 :
 OO0ooo ( oOOo0O00o )
elif i1Ii11II == 9032 :
 O0000 ( oOOo0O00o )
elif i1Ii11II == 9033 :
 o000o0OO ( oOOo0O00o )
elif i1Ii11II == 9034 :
 iiI1ii11i1 ( )
elif i1Ii11II == 7085 :
 iiiiIiI1IIiI ( oOOo0O00o )
elif i1Ii11II == 7086 :
 IIII ( oOOo0O00o )
elif i1Ii11II == 7087 :
 I1I1IiIiIIi1I ( OoOo000oOo0oo )
elif i1Ii11II == 9666 :
 ooO0O00Oo0o ( oOOo0O00o )
elif i1Ii11II == 10100 : oo0O0 ( )
elif i1Ii11II == 101001 : IiiI1 ( oOOo0O00o )
elif i1Ii11II == 10105 : Ii11 ( oOOo0O00o )
elif i1Ii11II == 10106 : o0OOooOoOo00O ( oOOo0O00o )
elif i1Ii11II == 10104 : iiiIIi11IiI ( oOOo0O00o )
elif i1Ii11II == 10107 : iII1iiI11IIi ( )
elif i1Ii11II == 10103 : oooOo000O ( oOOo0O00o )
elif i1Ii11II == 10108 : OoOooO ( oOOo0O00o )
elif i1Ii11II == 10000 : Origin_Menu ( )
elif i1Ii11II == 10001 : iI ( )
elif i1Ii11II == 10002 : iI111i1II ( )
elif i1Ii11II == 10003 : O0000oO00oO0o ( )
elif i1Ii11II == 10004 : OoOOo ( oOOo0O00o )
elif i1Ii11II == 10005 : i11I1I1iiI ( )
elif i1Ii11II == 10006 : iIi11I1II ( oOOo0O00o )
elif i1Ii11II == 10007 : ii1i1IiII111I ( oOOo0O00o , iiIIIiIi1IIi )
elif i1Ii11II == 10008 : ooOoOO ( )
elif i1Ii11II == 10009 : I1I11I1i1i1II ( )
elif i1Ii11II == 10010 : IiIiIIII ( oOOo0O00o )
elif i1Ii11II == 10011 : iIi1I ( oOOo0O00o )
elif i1Ii11II == 10012 : I11iiiiI1i ( oOOo0O00o )
elif i1Ii11II == 10113 : GRABG ( oOOo0O00o , iIIIiIi )
elif i1Ii11II == 10109 : iiiII1I1 ( oOOo0O00o )
elif i1Ii11II == 10013 : O0ooIi1I1I11I1I1i ( oOOo0O00o )
elif i1Ii11II == 10014 : IiIi1I11 ( )
elif i1Ii11II == 10015 : oO0oO00 ( )
elif i1Ii11II == 10016 : I1iIi1iiiIiI ( oOOo0O00o )
elif i1Ii11II == 10017 : IIIi ( )
elif i1Ii11II == 10018 : II1111iiI1II ( )
elif i1Ii11II == 10019 : o0oOO00O000O0 ( )
elif i1Ii11II == 10020 : o0Oo0o ( )
elif i1Ii11II == 10021 : I1III1I1IiI ( )
elif i1Ii11II == 10022 : i1ii11III1 ( oOOo0O00o )
elif i1Ii11II == 10023 : iII1ii ( iIIIiIi , oOOo0O00o )
elif i1Ii11II == 10024 : oO0oOo ( oOOo0O00o )
elif i1Ii11II == 10025 : iiI1 ( )
elif i1Ii11II == 10026 : O00O0ooo00OO0 ( )
elif i1Ii11II == 10027 : oo00OO ( )
elif i1Ii11II == 10028 : IiO0o ( )
elif i1Ii11II == 10029 : I1Ii1iI1IiI1I ( )
elif i1Ii11II == 423 : IiII1111I ( oOOo0O00o )
elif i1Ii11II == 426 : iiiii1II1I ( oOOo0O00o )
elif i1Ii11II == 10030 : Izle_Films ( )
elif i1Ii11II == 10031 : Latest_Izle_Movies ( )
elif i1Ii11II == 10032 : Izle_Genres ( )
elif i1Ii11II == 10033 : Izle_Pop_Movies ( )
elif i1Ii11II == 10034 : Izle_Boxsets ( )
elif i1Ii11II == 10035 : Izle_Search ( )
elif i1Ii11II == 10036 : Izle_Genres_Movie ( oOOo0O00o )
elif i1Ii11II == 10037 : Izle_Boxset_single ( oOOo0O00o )
elif i1Ii11II == 10038 : Izle_IFRAME ( )
elif i1Ii11II == 10039 : Izle_Boxsets_Next ( oOOo0O00o )
elif i1Ii11II == 10040 : OOo00OoO ( )
elif i1Ii11II == 10041 : Ii11I1i ( oOOo0O00o )
elif i1Ii11II == 10042 : o0O0o ( oOOo0O00o )
elif i1Ii11II == 10043 : Ii1i11i ( )
elif i1Ii11II == 10044 : IIIi1iiI1I1 ( oOOo0O00o )
elif i1Ii11II == 10045 : O0ooOoO0 ( iIIIiIi )
elif i1Ii11II == 10046 : iI1II1iIiiiI ( oOOo0O00o )
elif i1Ii11II == 10047 : iIIiiIiII1i ( oOOo0O00o )
elif i1Ii11II == 10048 : IIIiiII1iIi1ii1i ( oOOo0O00o )
elif i1Ii11II == 10049 : OoO0O00 ( oOOo0O00o )
elif i1Ii11II == 10050 : OoO ( )
elif i1Ii11II == 10051 : O0oooOoOO0O ( )
elif i1Ii11II == 10052 : ii111iIii1 ( )
elif i1Ii11II == 10053 : Addon ( oOOo0O00o )
elif i1Ii11II == 10054 : i1IIiIiI11 ( oOOo0O00o , iIIIiIi )
elif i1Ii11II == 10055 :
 iIiii1IIi1I ( "addFavorite" )
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 IiI1I1i1 ( iIIIiIi , oOOo0O00o , iiIIIiIi1IIi , IIo0o0O0O00oOOo , Ii1 )
elif i1Ii11II == 10056 :
 iIiii1IIi1I ( "rmFavorite" )
 try :
  iIIIiIi = iIIIiIi . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIIIiIi = iIIIiIi . split ( '  - ' ) [ 0 ]
 except :
  pass
 Oo0ooooO0o00 ( iIIIiIi )
elif i1Ii11II == 10057 :
 iIiii1IIi1I ( "getFavorites" )
 oOOoOo0OoOO ( )
elif i1Ii11II == 10058 : iiIIIIiii ( )
elif i1Ii11II == 10059 : Donators_Guide ( )
elif i1Ii11II == 10060 : o00o0 ( )
elif i1Ii11II == 10061 : Ii1I1Iiii ( )
elif i1Ii11II == 10062 : iiIIIi1iIi ( iIIIiIi , oOOo0O00o , OoOo000oOo0oo )
elif i1Ii11II == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif i1Ii11II == 10064 : IIIIIIi1IiIi ( )
elif i1Ii11II == 10065 : II111I1Iii ( oOOo0O00o )
elif i1Ii11II == 10066 : OO0OoO0o ( oOOo0O00o )
elif i1Ii11II == 10068 : oo000ii ( oOOo0O00o )
elif i1Ii11II == 10069 : OOoo ( oOOo0O00o )
elif i1Ii11II == 10070 : i111IiiI1Ii ( oOOo0O00o )
elif i1Ii11II == 10071 : Genie_Watch ( )
elif i1Ii11II == 10072 : iiiIiIIII1iiIIi ( )
elif i1Ii11II == 10073 : O0OOoo0 ( oOOo0O00o )
elif i1Ii11II == 10074 : OOOOO ( oOOo0O00o )
elif i1Ii11II == 10075 : IIiI1I ( iiIIIiIi1IIi , iIIIiIi , oOOo0O00o )
elif i1Ii11II == 10076 : i1I111Ii ( oOOo0O00o )
elif i1Ii11II == 10077 : iiI1iiii1 ( oOOo0O00o )
elif i1Ii11II == 10078 : oOoO0ooO0000 ( )
elif i1Ii11II == 10079 : Genie_Watch_Tv_Shows ( )
elif i1Ii11II == 10080 : Genie_Watch_Tv_Genre ( oOOo0O00o )
elif i1Ii11II == 10081 : Genie_Watch_TV_PlayRun ( oOOo0O00o )
elif i1Ii11II == 10082 : Genie_Watch_TV_Episodes ( oOOo0O00o , iiIIIiIi1IIi )
elif i1Ii11II == 10083 : Genie_Watch_Tv_Recent ( oOOo0O00o )
elif i1Ii11II == 10084 : IIIii ( )
elif i1Ii11II == 10085 : oo0OOo0 ( )
elif i1Ii11II == 10086 : O0 ( )
elif i1Ii11II == 20000 : O0O00OOo ( )
elif i1Ii11II == 20001 : iI1i1Iiii ( oOOo0O00o )
elif i1Ii11II == 20002 : iIII1IIi ( oOOo0O00o )
elif i1Ii11II == 20003 : oO0OOoOO ( oOOo0O00o )
elif i1Ii11II == 20004 : ii1iI1i1 ( oOOo0O00o )
elif i1Ii11II == 20005 : IIi1I1 ( oOOo0O00o )
elif i1Ii11II == 21004 : I1i1iii1Ii ( )
elif i1Ii11II == 21005 : ooo000 ( oOOo0O00o )
elif i1Ii11II == 21006 : oooOoO0oo0o0 ( oOOo0O00o )
elif i1Ii11II == 21007 : o0O00ooo0 ( oOOo0O00o )
elif i1Ii11II == 21008 : IiI ( oOOo0O00o )
elif i1Ii11II == 21009 : O00oO000O0O ( oOOo0O00o )
elif i1Ii11II == 30000 : I1IIi1iI1iiI ( )
elif i1Ii11II == 30001 : iIIIIi11i ( )
elif i1Ii11II == 100121 : Resolve ( oOOo0O00o )
elif i1Ii11II == 30003 : i11I1iiii ( )
elif i1Ii11II == 30004 : Ii1iII1ii1 ( oOOo0O00o )
elif i1Ii11II == 30005 : I11I1i ( oOOo0O00o )
elif i1Ii11II == 30006 : I1Iii ( )
elif i1Ii11II == 30007 : ooo0o00o ( )
elif i1Ii11II == 30008 : I1III1I11I1 ( oOOo0O00o )
elif i1Ii11II == 30009 : O00o0O0oo ( oOOo0O00o )
elif i1Ii11II == 30010 : IiiiI1I1iI11 ( oOOo0O00o )
elif i1Ii11II == 30011 : iIiiiII11 ( )
elif i1Ii11II == 30012 : i1Ii1IiIIi ( )
elif i1Ii11II == 30013 : Oo00o0OOo0OO ( )
elif i1Ii11II == 30014 : OOoOo0ooOoo ( )
elif i1Ii11II == 30015 : Oo00oo00o00Oo ( oOOo0O00o , iiIIIiIi1IIi , IIo0o0O0O00oOOo )
elif i1Ii11II == 30016 : iiii ( oOOo0O00o )
elif i1Ii11II == 30019 : OOoO0Oo ( oOOo0O00o )
elif i1Ii11II == 30017 : iIIiI1 ( oOOo0O00o )
elif i1Ii11II == 30018 : III1I1 ( oOOo0O00o )
elif i1Ii11II == 30030 : i1iII11IiI ( )
elif i1Ii11II == 30031 : iI1111i1i11Ii ( )
elif i1Ii11II == 30032 : IiiIi1III ( )
elif i1Ii11II == 30033 : iiIOoO0000oo0O0 ( )
elif i1Ii11II == 30034 : oOIIIi ( )
elif i1Ii11II == 30035 : IiIiiIiiiiI ( oOOo0O00o )
elif i1Ii11II == 30036 : i1I ( oOOo0O00o )
elif i1Ii11II == 30037 : IiiIIIIi ( oOOo0O00o )
elif i1Ii11II == 30038 : oOOO0I1iIIi ( )
elif i1Ii11II == 30039 : oooooo0O000o ( )
elif i1Ii11II == 50000 : I1i ( )
elif i1Ii11II == 50001 : oOOO00Oo ( )
elif i1Ii11II == 50002 : IIi1ii1IIi1 ( oOOo0O00o )
elif i1Ii11II == 50003 : Table_Menu ( OoOo000oOo0oo )
elif i1Ii11II == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif i1Ii11II == 60001 : Iioo0O00ooo0o ( )
elif i1Ii11II == 60002 : I1I ( iIIIiIi )
elif i1Ii11II == 60003 : IiiIi1I11 ( oOOo0O00o )
elif i1Ii11II == 600033 : iiIiII1 ( oOOo0O00o )
elif i1Ii11II == 60004 : i11Ii1IiIIIi ( oOOo0O00o )
elif i1Ii11II == 50004 : iiI ( )
elif i1Ii11II == 50005 : speedtest . runtest ( oOOo0O00o )
elif i1Ii11II == 70001 : IIIi1i ( )
elif i1Ii11II == 70002 : iiI1ii1Iii11I ( oOOo0O00o )
elif i1Ii11II == 70003 : IIiIi11 ( oOOo0O00o )
elif i1Ii11II == 70004 : oO0OO0O0 ( oOOo0O00o )
elif i1Ii11II == 70005 : iIIi1II1 ( oOOo0O00o )
elif i1Ii11II == 70006 : IiI1I11ii ( )
elif i1Ii11II == 50006 : o0OIiII ( i1 , i1111 )
elif i1Ii11II == 80000 : O00Oo00OOoO0 ( )
elif i1Ii11II == 80001 : resolvefilmon ( oOOo0O00o )
elif i1Ii11II == 80002 : ooOoOoo000O0O ( )
elif i1Ii11II == 80003 : Oo0 ( iIIIiIi , oOOo0O00o , "None" )
elif i1Ii11II == 80004 : IiIIIi ( iIIIiIi , oOOo0O00o )
elif i1Ii11II == 80005 : o0O0O0ooo0oOO ( )
elif i1Ii11II == 80006 : I1iiIiiii1111 ( oOOo0O00o )
elif i1Ii11II == 80007 : I1ii1i11i ( oOOo0O00o )
elif i1Ii11II == 80008 : Oooooo0O00o ( )
elif i1Ii11II == 80009 : oOo0oOoo0 ( )
elif i1Ii11II == 80010 : Oooo00 ( oOOo0O00o )
elif i1Ii11II == 80011 : OOOooOOO00O ( oOOo0O00o )
elif i1Ii11II == 80012 : O0Ooo00o0OoOo ( )
elif i1Ii11II == 90000 : oO0o0o0OO0o00 ( iIIIiIi , oOOo0O00o )
elif i1Ii11II == 90001 : tools ( )
elif i1Ii11II == 90002 : Oo00O ( )
elif i1Ii11II == 90003 : IiII1Iiii ( oOOo0O00o )
elif i1Ii11II == 90004 : I1o000o00OO00Oo ( oOOo0O00o )
elif i1Ii11II == 90005 : I1II11I11111i ( oOOo0O00o )
elif i1Ii11II == 90006 : iii1 ( oOOo0O00o )
elif i1Ii11II == 90007 : OO00Oo00o ( oOOo0O00o )
elif i1Ii11II == 90008 : oooO00o ( oOOo0O00o )
elif i1Ii11II == 90009 : ii1iII1i111II ( oOOo0O00o )
elif i1Ii11II == 90010 : iiIiii1IIIII ( )
elif i1Ii11II == 90020 : i1II111iiii ( )
elif i1Ii11II == 90021 : hellyeah2 ( oOOo0O00o )
elif i1Ii11II == 90022 : hellyeah3 ( oOOo0O00o )
elif i1Ii11II == 90023 : i11ii ( )
elif i1Ii11II == 90024 : IIOO0ooOo0OoOo0 ( oOOo0O00o )
elif i1Ii11II == 90025 : i1iIIIiiiI ( oOOo0O00o )
if 11 - 11: iI11I1II1I1I + oOo0O0Ooo
elif i1Ii11II == 90026 : IIIIiI11Ii1i ( )
elif i1Ii11II == 90027 : oO0OOO00 ( iIIIiIi , oOOo0O00o , OoOo000oOo0oo )
elif i1Ii11II == 90028 : O0OO00000o00 ( oOOo0O00o )
if 15 - 15: I11i
elif i1Ii11II == 900300 : OoOiiI1IIIi ( )
elif i1Ii11II == 900301 : II11IiIi11 ( oOOo0O00o )
elif i1Ii11II == 900302 : oO00ooooO0o ( oOOo0O00o )
elif i1Ii11II == 90030 : I1III1111iIi ( )
elif i1Ii11II == 90031 : IiIi1I1 ( )
elif i1Ii11II == 90032 : IiIIi1 ( oOOo0O00o )
elif i1Ii11II == 90033 : IIIIiii1IIii ( oOOo0O00o )
elif i1Ii11II == 90034 : ooOoOo0 ( oOOo0O00o )
elif i1Ii11II == 90035 : iI1i11 ( oOOo0O00o )
elif i1Ii11II == 90036 : OO00i1II ( oOOo0O00o )
elif i1Ii11II == 90039 : I1i1I11I ( oOOo0O00o )
elif i1Ii11II == 90037 : ooO00O00oOO ( oOOo0O00o )
elif i1Ii11II == 900377 : iiIiI ( oOOo0O00o )
elif i1Ii11II == 90038 : O0oooo0OoO0oo ( )
if 55 - 55: Ii / ii - Iii
elif i1Ii11II == 10090 : oo00O00oO000o ( )
elif i1Ii11II == 10091 : O0OoIIiII ( oOOo0O00o )
elif i1Ii11II == 10092 : iiiiIIIi ( oOOo0O00o )
elif i1Ii11II == 10093 : IIIIi1 ( oOOo0O00o , iiIIIiIi1IIi )
elif i1Ii11II == 10094 : oooOoooOOo0 ( oOOo0O00o , iiIIIiIi1IIi )
if 89 - 89: Iii - ooOoO0O00 - ooOoO0O00 * oooOo0oo0oo - o0o00Oo0O
elif i1Ii11II == 10095 : i11iiI1111 ( )
elif i1Ii11II == 10096 : OOOo ( oOOo0O00o )
elif i1Ii11II == 10097 : I111Ii ( oOOo0O00o )
elif i1Ii11II == 10098 : iiO0O0o0oO0O00 ( oOOo0O00o )
elif i1Ii11II == 10099 : o00ooo0 ( oOOo0O00o )
if 94 - 94: I1ii11iIi11i / Iii . Ii1I
elif i1Ii11II == 10200 : oo00ooOoO00 ( )
elif i1Ii11II == 10201 : i1i1IiIiIi1Ii ( oOOo0O00o )
elif i1Ii11II == 10202 : Ii1II11II1iii ( oOOo0O00o )
elif i1Ii11II == 10203 : RT4 ( oOOo0O00o )
if 31 - 31: Ii + iI11I1II1I1I . IIiIiII11i
elif i1Ii11II == 90040 : II1iIii111iII ( )
elif i1Ii11II == 90041 : oOOoOOO0oo0 ( oOOo0O00o )
elif i1Ii11II == 90042 : oOOOoo0o ( oOOo0O00o )
elif i1Ii11II == 90043 : IiIIiii1I ( oOOo0O00o )
elif i1Ii11II == 90044 : IIii ( oOOo0O00o )
elif i1Ii11II == 90045 : O0O000oOo0O ( )
elif i1Ii11II == 90046 : oOOO0 ( oOOo0O00o )
elif i1Ii11II == 90050 : o0Oi11i1I ( )
elif i1Ii11II == 90051 : IIiI11I1I1i1i ( oOOo0O00o )
elif i1Ii11II == 90052 : i111i1iIi1 ( oOOo0O00o )
elif i1Ii11II == 90053 : I1iiI1II ( oOOo0O00o )
elif i1Ii11II == 90054 : Ooii1IIi1ii ( oOOo0O00o )
elif i1Ii11II == 90055 : oOO0o00o0Oo0O ( )
if 72 - 72: i1IiiiI1iI * oO0o + I1ii11iIi11i / o0ii1I % oooOo0oo0oo
elif i1Ii11II == 100001 : Stand_up ( )
if 84 - 84: OOooOOo / I11i
elif i1Ii11II == 100003 : I1iIi1iiiIiI ( oOOo0O00o )
elif i1Ii11II == 100004 : o0O0Oo00Oo0o ( oOOo0O00o )
elif i1Ii11II == 100005 : Resolve ( oOOo0O00o )
elif i1Ii11II == 100008 : Search ( )
elif i1Ii11II == 100007 : IIi1IIIIi ( oOOo0O00o )
elif i1Ii11II == 100009 : yt . PlayVideo ( oOOo0O00o )
elif i1Ii11II == 100010 : ii1oOoO0o0ooo ( oOOo0O00o )
elif i1Ii11II == 100100 : o0oOoO0O ( iiIIIiIi1IIi , oOOo0O00o , II1Iiii11 )
elif i1Ii11II == 100101 : Iiii11iIi1 ( oOOo0O00o , iIIIiIi , IIo0o0O0O00oOOo , II1Iiii11 , iiIIIiIi1IIi )
elif i1Ii11II == 100102 : O0OoOoO00O ( iIIIiIi , oOOo0O00o , iiIIIiIi1IIi , IIo0o0O0O00oOOo )
elif i1Ii11II == 100106 : oo00o ( oOOo0O00o , iIIIiIi )
elif i1Ii11II == 100107 : i1II ( )
elif i1Ii11II == 100108 : IIiiiI ( )
elif i1Ii11II == 100109 : o000ooo0o0O ( oOOo0O00o )
elif i1Ii11II == 40000 : Oo0oOOOOo ( )
elif i1Ii11II == 40001 : I11IiI1iI ( oOOo0O00o )
elif i1Ii11II == 100110 : OoO0O000 ( )
elif i1Ii11II == 100111 : II1Ii ( oOOo0O00o )
elif i1Ii11II == 100110 : OoO0O000 ( )
elif i1Ii11II == 100210 : o0oO00 ( oOOo0O00o )
elif i1Ii11II == 100211 : oOOOOO0Ooooo ( )
elif i1Ii11II == 100212 : ii11Iiii ( )
elif i1Ii11II == 100213 : iii1iiii11I ( )
elif i1Ii11II == 100214 : o0oO0o00O ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
