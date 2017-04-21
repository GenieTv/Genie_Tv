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
IiiIII111iI = "3.4.9"
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
oO0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
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
 iii ( )
 o0OIiII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  ii1iII1II ( )
 else :
  if oo00 . getSetting ( 'My Build' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']WIZARD[/COLOR]' , str ( oO0000OOo00 ) , 4001 , iiIi1IIiIi + 'Wizard.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 4009 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GENIE STORE[/COLOR]' , 'http://genietv.co.uk/store.php' , 21008 , iiIi1IIiIi + 'store.png' , Oo00OOOOO , 'Direct Access To The GenieTv Store' )
  if oo00 . getSetting ( 'Music' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , iiIi1IIiIi + 'settings.png' , Oo00OOOOO , '' )
  if ii1I ( ) == 'android' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , str ( oO0000OOo00 ) , 30039 , iiIi1IIiIi + 'APKpng' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   I1I1i1I ( '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' , str ( oO0000OOo00 ) , 46 , iiIi1IIiIi + 'SoruceList.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '' , 10050 , iiIi1IIiIi + 'Addons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , str ( oO0000OOo00 ) , 39 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def ii1iII1II ( ) :
 if 87 - 87: I1ii11iIi11i . III1iiIii
 if 75 - 75: i1iIi + OOooOOo + I11i * Iii % i1i1I1IIii1II . IiI1i11I
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']WIZARD[/COLOR]' , str ( oO0000OOo00 ) , 4001 , iiIi1IIiIi + 'Wizard.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 40099 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GENIE STORE[/COLOR]' , 'http://genietv.co.uk/store.php' , 21008 , iiIi1IIiIi + 'store.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def tools ( ) :
 oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONTACT US[/COLOR]' , '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' ]
 IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOI1Ii1I1 )
 if IiII111iI1ii1 == 0 :
  oo0OOo0 ( )
 if IiII111iI1ii1 == 1 :
  iI11I1II ( )
 if IiII111iI1ii1 == 2 :
  Ii1IIiI1i ( )
 if IiII111iI1ii1 == 3 :
  o0Oo00 ( iI )
 if IiII111iI1ii1 == 4 :
  iIii1 . ok ( i1 , i1111 )
 if IiII111iI1ii1 == 5 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if IiII111iI1ii1 == 6 :
  O0O0Oooo0o ( )
  if 56 - 56: Ii1I % o0o00Oo0O - oOo0O0Ooo
def O00o0OO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi1I1iiiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , o00oOOooOOo0o , O0O0ooOOO , oOOo0O00o , iIiIi11 in IIi1I1iiiii :
  I1I1i1I ( iIiIi11 , url , 21009 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
  if 87 - 87: I1ii11iIi11i . oOo0O0Ooo - IIiIiII11i + o0o00Oo0O / I1ii11iIi11i / i1i1I1IIii1II
def IiI ( url ) :
 url = url
 IIIii1I = ii1I ( )
 if IIIii1I ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif IIIii1I ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 97 - 97: o0o00Oo0O + OOooOOo
  if 89 - 89: I11i + oO0o * Iii * o0ii1I
def iiIiI1i1 ( ) :
 iI = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , 'GuideSkins' + '.zip' )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( iI , IiIi11iI , o0oOoO00o )
 Oo0O00O000 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Oo0O00O000
 print '======================================='
 extract . all ( IiIi11iI , Oo0O00O000 , o0oOoO00o )
 i11I1IiII1i1i ( iI )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 ooI1111i ( )
def iIIii ( ) :
 o00O0O = ii1iii1i ( )
 Iii1I1111ii = o00O0O . replace ( II11iiii1Ii , "" )
 if os . path . exists ( o00O0O ) or not o00O0O == False :
  ooOoO00 = open ( o00O0O , mode = 'r' ) ; Ii1IIiI1io0O00Oo0 = ooOoO00 . read ( ) ; ooOoO00 . close ( )
  IiII111i1i11 ( "%s - %s" % ( i1 , Iii1I1111ii ) , Ii1IIiI1io0O00Oo0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def iiIiI1i1 ( ) :
 iI = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , 'GuideSkins' + '.zip' )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( iI , IiIi11iI , o0oOoO00o )
 Oo0O00O000 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Oo0O00O000
 print '======================================='
 extract . all ( IiIi11iI , Oo0O00O000 , o0oOoO00o )
 i11I1IiII1i1i ( iI )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 ooI1111i ( )
def i111iIi1i1II1 ( ) :
 I1I1i1I ( '[COLOR' + ooOoOoo0O + ']Todays Games[/COLOR]' , str ( oO0000OOo00 ) , 90030 , iiIi1IIiIi + 'tgames.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Tommys Replays[/COLOR]' , str ( oO0000OOo00 ) , 900300 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 86 - 86: iI11I1II1I1I / OOooOOo . IIiIiII11i
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 19 - 19: Ii1I % ii % III1iiIii * I11i % o0o00Oo0O
def ooo ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match eng prem[/COLOR]' , 'http://ourmatch.net/videos/england/premier-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match la liga[/COLOR]' , 'http://ourmatch.net/videos/spain/la-liga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match serie a[/COLOR]' , 'http://ourmatch.net/videos/italy/serie-a-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match bund[/COLOR]' , 'http://ourmatch.net/videos/germany/bundesliga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match ligue 1[/COLOR]' , 'http://ourmatch.net/videos/france/ligue-1-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match uefa champ[/COLOR]' , 'http://ourmatch.net/videos/europe/uefa-champions-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
iiIi1IIiIi + 'tommysreplays.png'
def i1i1iI1iiiI ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GOAL OF THE MONTH[/COLOR]' , 'http://ourmatch.net/goal-of-the-month/' , 900302 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 Ooo0oOooo0 = re . compile ( 'href="([^"]*)".+?<img src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oOOOoo00 = re . compile ( 'class=\'current\'>.+?</span><a class=.+? href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , o00oOOooOOo0o , iIiIi11 in Ooo0oOooo0 :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 900302 , o00oOOooOOo0o , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for iiIiIIIiiI in oOOOoo00 :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , iiIiIIIiiI , 900301 , iiIi1IIiIi + 'NEXT.png' , '' , '' )
def iiI1IIIi ( url ) :
 II11IiIi11 = OooOoooOo ( url )
 Ooo0oOooo0 = re . compile ( "<source src=\"(.+?)\"></video>',.+?'type':'([^']*)'," , re . DOTALL ) . findall ( II11IiIi11 )
 IIOOO0O00O0OOOO = re . compile ( "embed:'<iframe src=\"(.+?)\" width=.+? 'type':'([^']*)'," , re . DOTALL ) . findall ( II11IiIi11 )
 for url , iIiIi11 in Ooo0oOooo0 :
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for url , iIiIi11 in IIOOO0O00O0OOOO :
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
def I1iiii1I ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIi = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 for oO00ooooO0o , oo0o in IIi :
  IiII111i1i11 ( '[COLOR' + ooOoOoo0O + ']Tommys List[/COLOR]  ' + oO00ooooO0o , oo0o )
def o0oO0oooOoo ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIi = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
def I1III1111iIi ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( OOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( OOo0 )
 for url , iIiIi11 , o00oOOooOOo0o in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , o00oOOooOOo0o , Oo00OOOOO , '' )
 for url in next :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , iiIi1IIiIi + 'NEXT.png' , Oo00OOOOO , '' )
def I1i111I ( url ) :
 OOo0 = OooOoooOo ( url )
 OooOo0oo0O0o00O = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 I1i11 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 IIi = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for iIiIi11 , url in i1Iii1i1I :
  I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for iIiIi11 , url in I1i11 :
  I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for url in OooOo0oo0O0o00O :
  I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
  if 12 - 12: ooOoO0O00 + ooOoO0O00 - Ii1I * I1ii11iIi11i % I1ii11iIi11i - IIiIiII11i
def o0OOOOooo ( url ) :
 if 'drive' in url :
  OooO0OO ( url )
 else :
  OOo0 = OooOoooOo ( url )
  IIi = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( OOo0 )
  for url in IIi :
   OooO0OO ( url )
def o0OOo0o0O0O ( url ) :
 o0OO0o0oOOO0O = liveresolver . resolve ( url )
 iII1i11 = xbmcgui . ListItem ( path = o0OO0o0oOOO0O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1i11 )
def OooIiIIII1i11I ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 OOOiII1 = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOiII1 )
def ii1iii1i ( ) :
 OOo = False
 if os . path . exists ( os . path . join ( II11iiii1Ii , 'xbmc.log' ) ) :
  OOo = os . path . join ( II11iiii1Ii , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'kodi.log' ) ) :
  OOo = os . path . join ( II11iiii1Ii , 'kodi.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'spmc.log' ) ) :
  OOo = os . path . join ( II11iiii1Ii , 'spmc.log' )
 elif os . path . exists ( os . path . join ( II11iiii1Ii , 'tvmc.log' ) ) :
  OOo = os . path . join ( II11iiii1Ii , 'tvmc.log' )
 return OOo
 if 22 - 22: OOooOOo * o0o00Oo0O . III1iiIii * Ii - oOo0O0Ooo * i1iIi
def OOooo0O0o0 ( url ) :
 if url == 'http://' : return False
 try :
  i1Oo00 = urllib2 . Request ( url )
  i1Oo00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1i = urllib2 . urlopen ( i1Oo00 )
  i1i . close ( )
 except Exception , II1iI1I11I :
  return II1iI1I11I
 return True
def o0OO0 ( ) :
 if 44 - 44: o0o00Oo0O - o0ii1I - o0o00Oo0O % Iii . i1i1I1IIii1II
 if 74 - 74: Ii . oOo0O0Ooo
 if 36 - 36: ii . oO0o
 if 56 - 56: I1ii11iIi11i . Ii1I . oOo0O0Ooo
 if 39 - 39: o0o00Oo0O + i1IiiiI1iI
 xbmc . executebuiltin ( 'Runscript("special://home/addons/plugin.video.GenieTv/resources/speedtest.py")' )
def OoOooOoO ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Wizard[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   iiIiii1iI1i ( )
  if IiII111iI1ii1 == 1 :
   I1ii1ii11i1I ( )
  if IiII111iI1ii1 == 2 :
   o0OoOO ( O0O0Oo00 )
  if IiII111iI1ii1 == 3 :
   oOoO00o ( iI )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 10060 , iiIi1IIiIi + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 49 , iiIi1IIiIi + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , str ( oO0000OOo00 ) , 41 , iiIi1IIiIi + 'WipeGenie.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' , str ( oO0000OOo00 ) , 44 , iiIi1IIiIi + 'GenieBuilds.png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 100 - 100: I11i + oooOo0oo0oo * I11i
def oOOo0OOOo00O ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']FAVOURITES[/COLOR]' , str ( oO0000OOo00 ) , 10057 , iiIi1IIiIi + 'Favourites.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 9000 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']STREAM TEAM[/COLOR]' , str ( oO0000OOo00 ) , 4006 , iiIi1IIiIi + 'StreamTeam.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , iiIi1IIiIi + 'bamf.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Series[/COLOR]' , ( i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzL0cuTy5ELlMvZ29kcy5waHA=' ) ) , 100210 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cHM6Ly9hdGxhbnRpYzI4MC5zdGFydGRlZGljYXRlZC5uZXQvYm9zcy9kb2NzLw==' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiIi1IIiIi + 'zone.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']STREAM CATEGORIES[/COLOR]' , str ( oO0000OOo00 ) , 90002 , iiIi1IIiIi + 'cats.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
 else :
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']FAVOURITES[/COLOR]' , str ( oO0000OOo00 ) , 10057 , iiIi1IIiIi + 'Favourites.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 9000 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']STREAM TEAM[/COLOR]' , str ( oO0000OOo00 ) , 4006 , iiIi1IIiIi + 'StreamTeam.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , iiIi1IIiIi + 'bamf.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genie On Demand Series[/COLOR]' , ( i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzL0cuTy5ELlMvZ29kcy5waHA=' ) ) , 100210 , iiIi1IIiIi + 'gods.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 4004 , iiIi1IIiIi + 'Movies.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , str ( oO0000OOo00 ) , 4005 , iiIi1IIiIi + 'TVShows.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 4007 , iiIi1IIiIi + 'Kids.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cHM6Ly9hdGxhbnRpYzI4MC5zdGFydGRlZGljYXRlZC5uZXQvYm9zcy9kb2NzLw==' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , iiIi1IIiIi + 'zone.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']FREEVIEW[/COLOR]' , str ( oO0000OOo00 ) , 90023 , iiIi1IIiIi + 'freeview.png' , Oo00OOOOO , '' )
  if O0o0Oo == '5knuckleshuffle' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']XVID[/COLOR]' , str ( oO0000OOo00 ) , 10100 , iiIi1IIiIi + 'Jizbox.png' , Oo00OOOOO , '' )
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']ADULT CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30033 , iiIi1IIiIi + 'adu.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , str ( oO0000OOo00 ) , 30032 , iiIi1IIiIi + 'News.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , str ( oO0000OOo00 ) , 4008 , iiIi1IIiIi + 'Hobbies.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , str ( oO0000OOo00 ) , 8040 , iiIi1IIiIi + 'documentaries.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' , str ( oO0000OOo00 ) , 7001 , iiIi1IIiIi + 'DiscloseTV.png' , Oo00OOOOO , '' )
   if 76 - 76: Ii + I11i / Ii1I - oO0o - o0ii1I + Ii1I
   if 51 - 51: iI11I1II1I1I . i1iIi + iI11I1II1I1I
   if 95 - 95: oOo0O0Ooo
   if 46 - 46: OOooOOo + oO0o
   if 70 - 70: IiI1i11I / iI11I1II1I1I
   if 85 - 85: ii % ooOoO0O00 * ii / Ii1I
   if 96 - 96: ii + i1i1I1IIii1II
   if 44 - 44: i1i1I1IIii1II
   if 20 - 20: Iii + o0ii1I / o0o00Oo0O % iI11I1II1I1I
   if 88 - 88: OOooOOo / IIiIiII11i
   if 87 - 87: Ii1I - Ii1I - IiI1i11I + i1i1I1IIii1II
   if 82 - 82: i1i1I1IIii1II / iI11I1II1I1I . oOo0O0Ooo . oooOo0oo0oo / I11i
   if 42 - 42: I1ii11iIi11i
   if 19 - 19: i1i1I1IIii1II % Ii1I * iI11I1II1I1I + oOo0O0Ooo
   if 46 - 46: I1ii11iIi11i
   if 1 - 1: IiI1i11I
   if 97 - 97: oooOo0oo0oo + IiI1i11I + o0o00Oo0O + Ii
   if 77 - 77: I11i / ii
   if 46 - 46: I11i % iI11I1II1I1I . IiI1i11I % IiI1i11I + Ii
 O0oO0 ( 'movies' , 'MAIN' )
def Oo00o0OO0O00o ( ) :
 oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , oOI1Ii1I1 )
 if IiII111iI1ii1 == 0 :
  O0Oooo ( )
 if IiII111iI1ii1 == 1 :
  iiIi1i ( )
 if IiII111iI1ii1 == 2 :
  I1i11111i1i11 ( )
 if IiII111iI1ii1 == 3 :
  OOoOOO0 ( )
 if IiII111iI1ii1 == 4 :
  I1I1i ( )
 if IiII111iI1ii1 == 5 :
  I1IIIiIiIi ( )
  if 27 - 27: Ii1I + OOooOOo - oooOo0oo0oo + o0o00Oo0O . o0ii1I
  if 46 - 46: III1iiIii
  if 45 - 45: i1iIi
def o0OIiII ( ) :
 if not os . path . exists ( ooooooO0oo ) :
  IiII111i1i11 ( 'Change Log 16/3/17 - v3.4.8' , 'All Categories In GTV Live Lists Updated,[CR]BamfTv Added To StreamTeam,[CR] Pirate Movies Added To StreamTeam,[CR]GenieTv Now Krypton Compatible,[CR] G.O.D.S (GenieTv On Demand Soaps) Added To GenieTv,[CR] RaysRavers And RaizTv Updated,[CR] More Sections Now Available For Download Including Kids,[CR] Tv Guide Removed And Replaced By External App,[CR] Boss Documentaries A Masterpiece By Jason Cadd,[CR] Updates To All Searches,[CR] StreamTeam Cleaned Up,[CR] Addon Overall CleanUp,[CR] General Maintence' )
  os . makedirs ( ooooooO0oo )
  if 21 - 21: i1i1I1IIii1II . i1IiiiI1iI . oooOo0oo0oo / I1ii11iIi11i / i1IiiiI1iI
  if 17 - 17: oooOo0oo0oo / oooOo0oo0oo / Iii
def ii1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   I1IiiI1ii1i ( )
  if IiII111iI1ii1 == 1 :
   O0o ( )
  if IiII111iI1ii1 == 2 :
   oO0OoO00o ( iI )
  if IiII111iI1ii1 == 3 :
   II1iiiiII ( )
  if IiII111iI1ii1 == 4 :
   O0OoOO0oo0 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if IiII111iI1ii1 == 5 :
   oOO ( )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 9001 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , str ( oO0000OOo00 ) , 10200 , iiIi1IIiIi + 'rated.png' , Oo00OOOOO , '' )
  if 53 - 53: i1IiiiI1iI * III1iiIii . I1ii11iIi11i - o0ii1I % o0ii1I * Ii
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , str ( oO0000OOo00 ) , 7061 , iiIi1IIiIi + 'PopcornBox.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Desi Flix[/COLOR]' , '' , 80005 , iiIi1IIiIi + 'Desi.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , iiIi1IIiIi + 'FilmTrailers.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , iiIi1IIiIi + 'ClassicMovies.png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def iiOOO0oOOoo ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']DAILY LISTS[/COLOR]' , '' , 9007 , O0O , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , O0O , Oo00OOOOO , '' )
 if 52 - 52: I11i % I1ii11iIi11i
 if 64 - 64: o0o00Oo0O % Iii % o0o00Oo0O * oO0o . i1i1I1IIii1II + oOo0O0Ooo
 if 75 - 75: Iii . ii % I11i * Iii % ii
 if 13 - 13: III1iiIii / Ii % IIiIiII11i % Iii . Ii1I
 if 8 - 8: OOooOOo + I1ii11iIi11i - IIiIiII11i
def IiIi1iIIi1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   O0OoO0ooOO0o ( )
  if IiII111iI1ii1 == 1 :
   OoOo0oOooOoOO ( )
  if IiII111iI1ii1 == 2 :
   oo00ooOoO00 ( )
  if IiII111iI1ii1 == 3 :
   o00oOoOo0 ( )
  if IiII111iI1ii1 == 4 :
   o0O0O0ooo0oOO ( )
  if IiII111iI1ii1 == 5 :
   oo000ii ( )
  if IiII111iI1ii1 == 6 :
   OoO ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , str ( oO0000OOo00 ) , 9002 , iiIi1IIiIi + 'Search.png' , Oo00OOOOO , '' )
  if 41 - 41: ooOoO0O00 * IIiIiII11i / ii . oooOo0oo0oo
  if 83 - 83: IiI1i11I . o0o00Oo0O / I1ii11iIi11i / oooOo0oo0oo - IIiIiII11i
  if 100 - 100: oO0o
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '' , 8020 , iiIi1IIiIi + 'iWatchSeries.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , str ( oO0000OOo00 ) , 10095 , iiIi1IIiIi + 'RD.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , str ( oO0000OOo00 ) , 8064 , iiIi1IIiIi + 'ClassicTV.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , iiIi1IIiIi + 'TVShowTrailers.png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def II1i ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   Ii1IIIIi1ii1I = '[COLOR' + ooOoOoo0O + ']PANDORAS BOX[/COLOR]'
   if 13 - 13: oOo0O0Ooo % OOooOOo . Ii1I / I1ii11iIi11i % oooOo0oo0oo . ii
   if 22 - 22: III1iiIii / Ii
   if 62 - 62: oO0o / Ii1I
   if 7 - 7: ii . III1iiIii
  oOI1Ii1I1 = [ Ii1IIIIi1ii1I , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RAIZ TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ROADRUNNER STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   O000OOO0OOo ( )
  if IiII111iI1ii1 == 1 :
   i1i1I111iIi1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , oo00O00oO000o , iIiIi11 )
  if IiII111iI1ii1 == 2 :
   OOo00OoO ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0' ) ) )
  if IiII111iI1ii1 == 3 :
   i1i1I111iIi1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , oo00O00oO000o , iIiIi11 )
   if 10 - 10: I11i / Ii
  if IiII111iI1ii1 == 4 :
   o00oO ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if IiII111iI1ii1 == 5 :
   i1i1I111iIi1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , oo00O00oO000o , iIiIi11 )
 else :
  if 92 - 92: III1iiIii * I1ii11iIi11i * I1ii11iIi11i * oOo0O0Ooo . iI11I1II1I1I
  if 16 - 16: i1iIi % ii - oooOo0oo0oo * o0ii1I * Ii1I / ii
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']PANDORAS BOX[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'Roadrunner-Streams.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0' ) ) , 90037 , iiIi1IIiIi + 'raiztv.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'pirate.png' , Oo00OOOOO , '' )
  if 31 - 31: Iii . i1IiiiI1iI * i1iIi + Ii * i1i1I1IIii1II
  if 93 - 93: Ii1I / iI11I1II1I1I * ooOoO0O00 % ii * o0o00Oo0O * Iii
  if 64 - 64: IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / I1ii11iIi11i . i1iIi % III1iiIii
  if 50 - 50: iI11I1II1I1I - III1iiIii + oooOo0oo0oo
  if 69 - 69: o0o00Oo0O
  if 85 - 85: i1iIi / o0o00Oo0O
 O0oO0 ( 'movies' , 'MAIN' )
 if 18 - 18: I11i % o0o00Oo0O * Ii1I
def o0Iii ( ) :
 iii ( )
 I1I1i1I ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def o00oO ( url ) :
 OOo0 = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( OOo0 )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( I1iiiiI1iI ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( I1iiiiI1iI ) )
 I1i11 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( I1iiiiI1iI ) )
 for iIiIi11 , o00oOOooOOo0o , url in IIi :
  if '247ch' in url :
   iIiiiii1i ( iIiIi11 , url , 10190 , o00oOOooOOo0o )
  elif '.m3u' in url :
   iIiiiii1i ( iIiIi11 , url , 1019 , o00oOOooOOo0o )
  elif '.xml' in url :
   iIiiiii1i ( iIiIi11 , url , 1018 , o00oOOooOOo0o )
  else :
   iiIi1IIiI ( iIiIi11 , url , 222 , o00oOOooOOo0o )
 for iIiIi11 , url , o00oOOooOOo0o in i1Iii1i1I :
  if '.xml' in url :
   iIiiiii1i ( iIiIi11 , url , 1018 , o00oOOooOOo0o )
  elif '.m3u' in url :
   iIiiiii1i ( iIiIi11 , url , 1019 , o00oOOooOOo0o )
  else :
   iiIi1IIiI ( iIiIi11 , url , 222 , o00oOOooOOo0o )
 for iIiIi11 , url , o00oOOooOOo0o in I1i11 :
  iiIi1IIiI ( iIiIi11 , url , 8043 , o00oOOooOOo0o )
def i1oO0OO0 ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def O0Oo0o000oO ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , o00oOOooOOo0o in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 222 , o00oOOooOOo0o )
  if 99 - 99: i1i1I1IIii1II * IIiIiII11i * i1IiiiI1iI
def oOooO0 ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 79 - 79: oO0o - iI11I1II1I1I + o0ii1I - i1IiiiI1iI
def OoOiIIiii ( url ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , oO0oOOoo00000 , oOo00 , oOOo0O00o , O0O0ooOOO in IIi :
  if oOo00 == '123' :
   oOo00 = iiIi1IIiIi + 'appstreams.png'
  if oOOo0O00o == '123' :
   oOOo0O00o = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   Iii1I1I11iiI1 ( iIiIi11 , url , 100010 , oOo00 , oOOo0O00o , O0O0ooOOO )
  elif 'playlist' in url :
   Iii1I1I11iiI1 ( iIiIi11 , url , 100007 , oOo00 , oOOo0O00o , O0O0ooOOO )
  elif 'watchseries' in url :
   Iii1I1I11iiI1 ( iIiIi11 , url , 100100 , oOo00 , oOOo0O00o , O0O0ooOOO )
  elif not 'http' in url :
   i1iI11i1IIi ( iIiIi11 , url , 100009 , oOo00 , oOOo0O00o , O0O0ooOOO , '' )
  else :
   i1iI11i1IIi ( iIiIi11 , url , 100005 , oOo00 , oOOo0O00o , O0O0ooOOO , '' )
   if 4 - 4: ii - Ii1I * oOo0O0Ooo
def I1iIiI11I1 ( url ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi1I1iiiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , o00oOOooOOo0o , O0O0ooOOO , oOOo0O00o , iIiIi11 in IIi1I1iiiii :
  if o00oOOooOOo0o == '123' :
   o00oOOooOOo0o = iiIi1IIiIi + 'appstreams.png'
  if oOOo0O00o == '123' :
   oOOo0O00o = Oo00OOOOO
  if 'php' in url :
   Iii1I1I11iiI1 ( iIiIi11 , url , 100004 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
  elif 'playlist' in url :
   Iii1I1I11iiI1 ( iIiIi11 , url , 100007 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
  elif 'watchseries' in url :
   Iii1I1I11iiI1 ( iIiIi11 , url , 100100 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
  elif not 'http' in url :
   i1iI11i1IIi ( iIiIi11 , url , 100009 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO , '' )
  else :
   i1iI11i1IIi ( iIiIi11 , url , 100005 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO , '' )
   if 27 - 27: o0ii1I . Ii % i1IiiiI1iI
def Oo ( url ) :
 if 81 - 81: i1i1I1IIii1II * oO0o
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 iI11I = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1iiiiI1iI in iI11I :
  oOo00 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( I1iiiiI1iI ) )
  for oOo00 in oOo00 :
   oOo00 = oOo00
  iIiIi11 = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( I1iiiiI1iI ) )
  for iIiIi11 in iIiIi11 :
   if 'elete' in iIiIi11 :
    pass
   elif 'rivate Vid' in iIiIi11 :
    pass
   else :
    iIiIi11 = ( iIiIi11 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  I1IIIiii1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( I1iiiiI1iI ) )
  for I1IIIiii1 in I1IIIiii1 :
   I1IIIiii1 = I1IIIiii1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( I1iiiiI1iI ) )
  for url in url :
   url = url
  i1iI11i1IIi ( '[COLORred]' + str ( I1IIIiii1 ) + '[/COLOR] : ' + str ( iIiIi11 ) , str ( url ) , 100009 , str ( oOo00 ) , Oo00OOOOO , '' , '' )
  O0oO0 ( 'movies' , '' )
  if 65 - 65: Iii / IIiIiII11i * o0ii1I . IiI1i11I * i1i1I1IIii1II % oooOo0oo0oo
  if 69 - 69: i1iIi - oO0o / Ii + Ii1I % ii
  if 73 - 73: o0ii1I - i1IiiiI1iI
  if 68 - 68: IiI1i11I * ii * iI11I1II1I1I . IIiIiII11i
def O0Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi1I1iiiii = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , o00oOOooOOo0o , O0O0ooOOO , oOOo0O00o , iIiIi11 in IIi1I1iiiii :
  if '.php' in url :
   Iii1I1I11iiI1 ( iIiIi11 , url , 100210 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
  else :
   I1I1i1I ( iIiIi11 , url , 222 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
   if 36 - 36: o0ii1I / IIiIiII11i / III1iiIii / III1iiIii + Ii1I
   if 95 - 95: III1iiIii
   if 51 - 51: IIiIiII11i + III1iiIii . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
def OOoOoo0 ( iconimage , url , extra ) :
 oOo00 = ' '
 I1iIII1 = ' '
 oOOo0O00o = ' '
 iIii = ' '
 oOo0OoOOo0 = O0i11i1iiI1i ( url )
 oOo00 = re . compile ( '<img src="(.+?)">' ) . findall ( oOo0OoOOo0 )
 for oOo00 in oOo00 :
  oOo00 = oOo00
 iII11I1Ii1 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( oOo0OoOOo0 )
 for oOOo0O00o in iII11I1Ii1 :
  oOOo0O00o = oOOo0O00o
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( oOo0OoOOo0 )
 for url , iIii in IIi :
  iIii = 'S' + ( iIii ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  o0o0 ( ( iIii ) . replace ( '  ' , '' ) , url , 100101 , oOo00 , oOOo0O00o , I1iIII1 , '' )
  O0oO0 ( 'Movies' , 'info' )
  if 59 - 59: oooOo0oo0oo + Ii
def oo0OOo0O ( url , name , fanart , extra , iconimage ) :
 Ii1IiII = extra
 iIii = name
 oOo0OoOOo0 = O0i11i1iiI1i ( url )
 oOo00 = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( oOo0OoOOo0 )
 for url , name , I1i in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  I1i = I1i
  oooii1iiIi1 = name + ' - [COLORred]' + I1i + '[/COLOR]'
  o0o0 ( oooii1iiIi1 , url , 100102 , oOo00 , fanart , 'Aired : ' + I1i , oooii1iiIi1 )
  if 34 - 34: oooOo0oo0oo
def OooO0ooo0o ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = O0i11i1iiI1i ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , name in IIi :
  for iII1i11 in o00OO00OoO :
   if iII1i11 in iI :
    URL = 'http://www.watchseriesgo.to/link/' + iI
    i1iI11i1IIi ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  o0o0 ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 47 - 47: ii
  if 4 - 4: oOo0O0Ooo % Iii
def I1 ( url , name ) :
 oOO0o0 = name
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 I1i11 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iiI11I1i1i1iI ( url , oOO0o0 )
 for url in i1Iii1i1I :
  iiI11I1i1i1iI ( url , oOO0o0 )
 for url in I1i11 :
  iiI11I1i1i1iI ( url , oOO0o0 )
  if 60 - 60: ii % I1ii11iIi11i + oooOo0oo0oo . i1iIi * iI11I1II1I1I
def iiI11I1i1i1iI ( url , season_name ) :
 if 'daclips.in' in url :
  oooo00 ( url , season_name )
 elif 'filehoot.com' in url :
  O00OO0oO ( url , season_name )
 elif 'allmyvideos.net' in url :
  iI1I1iIi11 ( url , season_name )
 elif 'vidspot.net' in url :
  oo0ooOO ( url , season_name )
 elif 'vodlocker' in url :
  iI1IiIIiIIi ( url , season_name )
 elif 'vidto' in url :
  IiIi11Iii ( url , season_name )
  if 46 - 46: OOooOOo - Iii - o0ii1I . ooOoO0O00
  if 35 - 35: IIiIiII11i * Iii - ii . Iii . Iii
def IiIi11Iii ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1II , iIiIi11 in IIi :
  OO0 ( I1II , season_name )
  if 84 - 84: OOooOOo % i1iIi - OOooOOo . I11i
  if 5 - 5: OOooOOo * i1IiiiI1iI - Ii1I / iI11I1II1I1I % i1i1I1IIii1II + III1iiIii
def iI1I1iIi11 ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1II , iIiIi11 in IIi :
  OO0 ( I1II , season_name )
  if 51 - 51: i1IiiiI1iI * IIiIiII11i % i1iIi
def oo0ooOO ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for I1II , iIiIi11 in IIi :
  OO0 ( I1II , season_name )
  if 98 - 98: oO0o . Iii % IIiIiII11i
def iI1IiIIiIIi ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1II in IIi :
  OO0 ( I1II , season_name )
  if 71 - 71: i1IiiiI1iI % ooOoO0O00 - IIiIiII11i - oooOo0oo0oo + oooOo0oo0oo * i1iIi
def oooo00 ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for I1II in IIi :
  OO0 ( I1II , season_name )
  if 51 - 51: iI11I1II1I1I / OOooOOo + oooOo0oo0oo - Iii + IiI1i11I
def O00OO0oO ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1II in IIi :
  OO0 ( I1II , season_name )
  if 29 - 29: I11i % iI11I1II1I1I . ii % ii % IIiIiII11i / IiI1i11I
def OO0 ( Link , season_name ) :
 if 'http:/' in Link :
  oo0o0000Oo0 ( Link )
  if 80 - 80: i1IiiiI1iI - I1ii11iIi11i
def OOooO ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 O00O0OO00oo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in O00O0OO00oo :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 69 - 69: I11i / I1ii11iIi11i
def o0o0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIiiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iI111i1I1II = [ ]
  if 96 - 96: i1IiiiI1iI / I1ii11iIi11i * IIiIiII11i - IiI1i11I * I1ii11iIi11i
  if showcontext == 'fav' :
   iI111i1I1II . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   iI111i1I1II . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IIiiii . addContextMenuItems ( iI111i1I1II )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = True )
 return IIIII1iii
 if 81 - 81: III1iiIii . I11i / i1IiiiI1iI
 if 17 - 17: Ii - oooOo0oo0oo . III1iiIii % iI11I1II1I1I + Iii - i1iIi
def i1iI11i1IIi ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIiiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iI111i1I1II = [ ]
  iI111i1I1II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iI111i1I1II . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   iI111i1I1II . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IIiiii . addContextMenuItems ( iI111i1I1II )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = False )
 return IIIII1iii
 if 78 - 78: Iii * OOooOOo . o0o00Oo0O / o0o00Oo0O
def OooOOOo0 ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 54 - 54: o0ii1I - Iii - i1IiiiI1iI . iI11I1II1I1I
def o0OIIiI1I1 ( url ) :
 I11I1IIiiII1 = xbmc . Player ( IIIIIii1ii11 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I11I1IIiiII1 . play ( url ) . strip ( )
 except : pass
 if 86 - 86: OOooOOo * IIiIiII11i - o0o00Oo0O . OOooOOo % iI11I1II1I1I / oooOo0oo0oo
def oo0o0000Oo0 ( url ) :
 I11I1IIiiII1 = xbmc . Player ( )
 import urlresolver
 try : I11I1IIiiII1 . play ( url )
 except : pass
 if 11 - 11: oOo0O0Ooo * i1i1I1IIii1II + Ii1I / Ii1I
def O0i11i1iiI1i ( url ) :
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
  if 37 - 37: Ii + ooOoO0O00
  if 23 - 23: IiI1i11I + Iii . OOooOOo * oOo0O0Ooo + Ii1I
  if 18 - 18: III1iiIii * I11i . III1iiIii / o0o00Oo0O
def iiIi1i ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   iiIII1II ( )
  if IiII111iI1ii1 == 1 :
   oOo00oOOOOO ( )
  if IiII111iI1ii1 == 2 :
   OoOOo0O00 ( )
  if IiII111iI1ii1 == 3 :
   iIiI ( )
  if IiII111iI1ii1 == 4 :
   iIIIi1i1I11i ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'SearchCartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( oO0000OOo00 ) , 21004 , iiIi1IIiIi + 'watchcartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '' , 10001 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '' , 20000 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , iiIi1IIiIi + 'anime.png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
def OOoOOO0 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '' , 10002 , iiIi1IIiIi + 'Football.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , iiIi1IIiIi + 'Fitness.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Go Fishing[/COLOR]' , str ( oO0000OOo00 ) , 8090 , iiIi1IIiIi + 'GoFishing.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , iiIi1IIiIi + 'GenieTVKitchen.png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 55 - 55: I1ii11iIi11i - oooOo0oo0oo
 if 84 - 84: i1IiiiI1iI + I1ii11iIi11i - OOooOOo * OOooOOo
 if 61 - 61: ii . i1i1I1IIii1II . ii / I1ii11iIi11i
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   o00O = ( II1I ) . replace ( 'special://home/addons/' , '' )
   IiII111i1i11 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + o00O + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   IiII111iI1ii1 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if IiII111iI1ii1 == 0 :
    i1iIIi ( II1I )
    ooI1111i ( )
   elif IiII111iI1ii1 == 1 :
    oo0OO ( II1I )
  else :
   pass
   if 2 - 2: IIiIiII11i - oO0o . III1iiIii * IiI1i11I / i1i1I1IIii1II
def oo0OO ( addon ) :
 o00O = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 80 - 80: oooOo0oo0oo / Iii / OOooOOo + ooOoO0O00 - I1ii11iIi11i
def i1iIIi ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 iIIiiIIi1IiI = os . path . join ( IIIII , 'default.py' )
 I11IIIiIi11 = open ( iIIiiIIi1IiI , "w+" )
 if 39 - 39: o0ii1I % o0o00Oo0O % OOooOOo . ooOoO0O00
 I11IIIiIi11 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 I11IIIiIi11 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 I11IIIiIi11 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 86 - 86: oO0o * ii
 if 71 - 71: iI11I1II1I1I - oooOo0oo0oo . oOo0O0Ooo % ii + oooOo0oo0oo
 if 26 - 26: I1ii11iIi11i + oooOo0oo0oo / oO0o % OOooOOo % Ii1I + IIiIiII11i
 if 31 - 31: Iii % oooOo0oo0oo * Iii
def OOo00OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IiII1i1iii1Ii = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIO0O00OOo = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1i11 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OooOo0oo0O0o00O = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OoOOo = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , iii1 , oOOo0O00o , O0O0ooOOO in IiII1i1iii1Ii :
  if 'php' in url :
   Iii1I1I11iiI1 ( iIiIi11 , url , 90037 , iii1 , oOOo0O00o , O0O0ooOOO )
  elif iIiIi11 == 'Search' :
   Iii1I1I11iiI1 ( 'Search' , url , 90038 , iii1 , oOOo0O00o , O0O0ooOOO )
  else :
   I1I1i1I ( iIiIi11 , url , 222 , iii1 , oOOo0O00o , O0O0ooOOO )
 for iIiIi11 , o00oOOooOOo0o , url , oOO0oo in iIO0O00OOo :
  Iii1I1I11iiI1 ( iIiIi11 , url , 90037 , o00oOOooOOo0o , oOO0oo , '' )
 for iIiIi11 , o00oOOooOOo0o , url , oOO0oo in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 90037 , o00oOOooOOo0o , oOO0oo , '' )
 for iIiIi11 , url , o00oOOooOOo0o , oOO0oo in i1Iii1i1I :
  I1I1i1I ( iIiIi11 , url , 222 , o00oOOooOOo0o , oOO0oo , '' )
 for iIiIi11 , url , o00oOOooOOo0o , oOO0oo in I1i11 :
  I1I1i1I ( iIiIi11 , url , 222 , o00oOOooOOo0o , oOO0oo , '' )
 for iIiIi11 , url , o00oOOooOOo0o , oOO0oo in OooOo0oo0O0o00O :
  I1I1i1I ( iIiIi11 , url , 222 , o00oOOooOOo0o , oOO0oo , '' )
 for iIiIi11 , url , o00oOOooOOo0o in OoOOo :
  I1I1i1I ( iIiIi11 , url , 222 , o00oOOooOOo0o , '' , '' )
  O0oO0 ( 'tvshows' , 'Media Info 3' )
  if 29 - 29: oOo0O0Ooo * IIiIiII11i * ii - Ii1I * IIiIiII11i
def iiO00O00O000OOO ( ) :
 iIOo0O = [ 'serialsearch' , 'moviesearch' ]
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 if II1i111 == '' :
  pass
 else :
  for i1iiiIii11 in iIOo0O :
   OOoOOO000O0 = Oo0o0000o0o0 + i1iiiIii11 + '.php'
   oOo0OoOOo0 = OooOoooOo ( OOoOOO000O0 )
   if oOo0OoOOo0 != 'Opened' :
    IIi1I1iiiii = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( oOo0OoOOo0 )
    for iIiIi11 , iI , iii1 , oOOo0O00o , O0O0ooOOO in IIi1I1iiiii :
     if II1i111 in iIiIi11 . lower ( ) :
      oOo0 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in oOo0 :
       if iII1i11 == iI :
        iIiIi11 = '[COLORred]* [/COLOR]' + ( iIiIi11 ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        II1i11I1 = open ( OOOO0OOoO0O0 , "a" )
        II1i11I1 . write ( 'item="' + iIiIi11 + '"\n' )
        II1i11I1 . close
      if 'php' in iI :
       Iii1I1I11iiI1 ( iIiIi11 , iI , 90037 , iii1 , oOOo0O00o , O0O0ooOOO )
      else :
       I1I1i1I ( iIiIi11 , iI , 222 , iii1 , oOOo0O00o , O0O0ooOOO )
       if 2 - 2: oOo0O0Ooo - i1i1I1IIii1II
   O0oO0 ( 'tvshows' , 'Media Info 3' )
   if 26 - 26: OOooOOo / I1ii11iIi11i - ooOoO0O00 + Iii
def IiiIi ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://www.tvcatchup.com/channels/' )
 o0o = OooOoooOo ( 'http://www.djing.com/' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img style="" src="([^"]*)" alt="([^"]*)"/>.+?<br/>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIIi = re . compile ( 'title="([^"]*)".+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( o0o )
 for iI , o00oOOooOOo0o , ooO00O00oOO , iIiIi11 in IIi :
  iiIi1IIiI ( ( '[COLORgold]' + ooO00O00oOO + '[/COLOR][COLORwhite] - [COLORsteelblue]' + iIiIi11 + '[/COLOR]' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' ) , 'http://www.tvcatchup.com' + iI , 90024 , o00oOOooOOo0o )
 for I1IIIii , iI , o00oOOooOOo0o in iIIi :
  iiIi1IIiI ( I1IIIii , 'http://www.tvcatchup.com' + iI , 90024 , o00oOOooOOo0o )
 for iI , o00oOOooOOo0o , iIiIi11 in i1Iii1i1I :
  if 'Submit' in iIiIi11 :
   pass
  elif '&lt;' in iIiIi11 :
   pass
  else :
   I1I1i1I ( '[COLORgold]DJing  [/COLOR][COLORwhite]- [COLORsteelblue]' + iIiIi11 + '[/COLOR]' , iI , 90025 , 'http://www.djing.com' + o00oOOooOOo0o , Oo00OOOOO , '' )
  O0oO0 ( 'movies' , 'MAIN' )
def I1IIII1ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 13 - 13: ii * i1i1I1IIii1II - o0ii1I / oooOo0oo0oo + Iii + III1iiIii
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def iii1III1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iiiIi ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 45 - 45: Ii1I + oO0o * Ii / oooOo0oo0oo % Iii * o0o00Oo0O
def O0o ( ) :
 if 17 - 17: o0o00Oo0O
 if 88 - 88: I1ii11iIi11i . o0o00Oo0O % ii / oooOo0oo0oo
 if 89 - 89: IIiIiII11i / i1i1I1IIii1II
 if 14 - 14: oooOo0oo0oo . oOo0O0Ooo * i1iIi + IIiIiII11i - i1iIi + oooOo0oo0oo
 if 18 - 18: i1i1I1IIii1II - I11i - oOo0O0Ooo - oOo0O0Ooo
 if 54 - 54: I1ii11iIi11i + oOo0O0Ooo / IiI1i11I . oOo0O0Ooo * OOooOOo
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if 'yr' in iI :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + iI , 10201 , iiIi1IIiIi + 'rated.png' )
   if 1 - 1: OOooOOo * oO0o . ooOoO0O00 / I1ii11iIi11i . Ii1I + I1ii11iIi11i
def IIiIi1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for Oo00O0ooOO , url , iIiIi11 in IIi :
  if 'id' in url :
   iIiiiii1i ( ( '[COLORred]RANK [COLORblue]' + Oo00O0ooOO + '[COLORred] - [COLORblue]' + iIiIi11 + '[/COLOR]' ) , iIiIi11 , 10202 , iiIi1IIiIi + 'rated.png' )
   if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
def OoOO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 II1i11i1iIi11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Ii11 = ( url )
 II1i111 = Ii11 . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( Ii11 ) . replace ( ' ' , '+' )
 oo0O0oO0O0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 oOo0O = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 I11iIiii1 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 iIIIiiiI11I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1ii1111Ii = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0OiiiI1i11Ii = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + Ii11
 iIiII = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 65 - 65: I11i
 I1ii1II1iII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 II1io0OO00oo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 8 - 8: i1iIi * o0o00Oo0O
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( oo0O0oO0O0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( oOo0O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( I11iIiii1 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OOoO = O00O0oOO00O00 ( iIIIiiiI11I )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IiIIII = O00O0oOO00O00 ( o0OiiiI1i11Ii )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOOo = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 oo0oO0 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 44 - 44: Ii1I - o0ii1I / IIiIiII11i * oO0o * I1ii11iIi11i
 if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * oooOo0oo0oo % IIiIiII11i
 OooOoOOo0oO00 = O00O0oOO00O00 ( I1ii1II1iII )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 O00O = O00O0oOO00O00 ( II1io0OO00oo )
 if 91 - 91: Iii / o0o00Oo0O - o0ii1I . oOo0O0Ooo
 if 82 - 82: III1iiIii * oooOo0oo0oo / i1i1I1IIii1II
 if 2 - 2: oOo0O0Ooo + I11i . I11i . o0o00Oo0O / Iii
 if 40 - 40: I11i - IIiIiII11i / I1ii11iIi11i
 if 14 - 14: Ii1I
 if 5 - 5: I11i . iI11I1II1I1I % iI11I1II1I1I
 if 56 - 56: ii - Iii - ooOoO0O00
 if 8 - 8: i1IiiiI1iI / oooOo0oo0oo . oOo0O0Ooo + Ii1I / Ii
 if 31 - 31: i1iIi - iI11I1II1I1I + IiI1i11I . I1ii11iIi11i / III1iiIii % iI11I1II1I1I
 if 6 - 6: III1iiIii * Ii % iI11I1II1I1I % Ii + I11i / ooOoO0O00
 if 53 - 53: Iii + iI11I1II1I1I
 if 70 - 70: Ii1I
 if 67 - 67: ii
 if oo0oO0 != 'Failed' :
  IiIiIi1I1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oo0oO0 )
  for url , iIiIi11 in IiIiIi1I1 :
   IiI1ii1Ii = O00O0oOO00O00 ( url )
   oooOOOoOOOo0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiI1ii1Ii )
   for O00oOoo0OoO0 , Ooo0 in oooOOOoOOOo0O :
    Ooo0 = ( Ooo0 . replace ( '.' , ' ' ) )
    if II1i111 in Ooo0 . lower ( ) :
     if '.mkv' in O00oOoo0OoO0 :
      I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , url + O00oOoo0OoO0 , 222 , '' , '' , '' )
     elif '.mp4' in O00oOoo0OoO0 :
      I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , url + O00oOoo0OoO0 , 222 , '' , '' , '' )
     elif '.avi' in O00oOoo0OoO0 :
      I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , url + O00oOoo0OoO0 , 222 , '' , '' , '' )
     elif '.wav' in O00oOoo0OoO0 :
      I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , url + O00oOoo0OoO0 , 222 , '' , '' , '' )
     else :
      Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , url + O00oOoo0OoO0 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 91 - 91: ooOoO0O00 - iI11I1II1I1I
      O0oO0 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in i1Iii1i1I :
   if Ii11 in iIiIi11 . lower ( ) :
    I1I1i1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 55 - 55: oOo0O0Ooo * I11i % i1iIi . iI11I1II1I1I * i1IiiiI1iI
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 92 - 92: i1IiiiI1iI - iI11I1II1I1I
 if o00OooOO000 != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for I11III111i , iIiIi11 in I1i11 :
   if Ii11 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOo0O + I11III111i ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  OooOo0oo0O0o00O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in OooOo0oo0O0o00O :
   if Ii11 in iIiIi11 . lower ( ) :
    I1I1i1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 78 - 78: ii
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if OOoO != 'Failed' :
  OOoo0 = [ ]
  OoOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoO )
  for url , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in OoOOo :
   if Ii11 in iIiIi11 . lower ( ) :
    if iIiIi11 in OOoo0 :
     pass
    else :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
     OOoo0 . append ( iIiIi11 )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     O0oO0 ( 'tvshows' , 'Media Info 3' )
 if IiIIII != 'Failed' :
  III1I1I = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IiIIII )
  for url , o00oOOooOOo0o , iIiIi11 in III1I1I :
   if Ii11 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , o00oOOooOOo0o )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 14 - 14: o0ii1I . Ii
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 27 - 27: i1iIi % o0o00Oo0O % i1IiiiI1iI
    if 99 - 99: oOo0O0Ooo + ooOoO0O00 + Ii + I1ii11iIi11i % i1i1I1IIii1II / Iii
    if 60 - 60: o0ii1I * OOooOOo - Ii % i1iIi
    if 52 - 52: Ii1I % i1i1I1IIii1II - Ii
    if 30 - 30: IiI1i11I / oO0o + i1i1I1IIii1II
    if 6 - 6: IiI1i11I . Iii + o0ii1I . i1IiiiI1iI
    if 70 - 70: oO0o
    if 46 - 46: Iii - ooOoO0O00
    if 46 - 46: i1IiiiI1iI % o0ii1I
    if 72 - 72: iI11I1II1I1I
    if 45 - 45: I1ii11iIi11i - I11i % i1IiiiI1iI
    if 38 - 38: i1IiiiI1iI % oooOo0oo0oo - ii
    if 87 - 87: oO0o % oOo0O0Ooo
    if 77 - 77: iI11I1II1I1I - ooOoO0O00 . i1i1I1IIii1II
    if 26 - 26: I11i * III1iiIii . ooOoO0O00
    if 59 - 59: o0o00Oo0O + ooOoO0O00 - I11i
    if 62 - 62: Ii % oooOo0oo0oo . III1iiIii . oooOo0oo0oo
    if 84 - 84: Ii * oO0o
 if OooOoOOo0oO00 != 'Failed' :
  I1I1iII1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OooOoOOo0oO00 )
  for url , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in I1I1iII1i :
   if Ii11 in iIiIi11 . lower ( ) :
    I1I1i1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 30 - 30: o0o00Oo0O + Ii1I + IIiIiII11i
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 14 - 14: I11i / oooOo0oo0oo - iI11I1II1I1I - i1i1I1IIii1II % i1iIi
    if 49 - 49: i1iIi * i1i1I1IIii1II / I11i / I1ii11iIi11i * iI11I1II1I1I
    if 57 - 57: OOooOOo - i1i1I1IIii1II / i1iIi % Ii
    if 3 - 3: IiI1i11I . i1iIi % oOo0O0Ooo + Ii1I
    if 64 - 64: ooOoO0O00
    if 29 - 29: I11i / Ii / oOo0O0Ooo % i1i1I1IIii1II % Ii
    if 18 - 18: oooOo0oo0oo + i1IiiiI1iI
    if 80 - 80: i1i1I1IIii1II + I11i * o0ii1I + oO0o
    if 75 - 75: Iii / I11i / oooOo0oo0oo / III1iiIii % i1iIi + IIiIiII11i
    if 4 - 4: IiI1i11I - I1ii11iIi11i - III1iiIii - Iii % Ii / oO0o
 i1iii11 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 92 - 92: OOooOOo . ii - i1IiiiI1iI
 for i1iiiIii11 in i1iii11 :
  OOoOOO000O0 = oO0 + i1iiiIii11 + oOoOooOo0o0
  oo0oO0 = O00O0oOO00O00 ( OOoOOO000O0 )
  if oo0oO0 != 'Failed' :
   IiIiIi1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0oO0 )
   for url , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in IiIiIi1I1 :
    if Ii11 in iIiIi11 . lower ( ) :
     I1I1i1I ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 74 - 74: iI11I1II1I1I % IiI1i11I * oooOo0oo0oo * iI11I1II1I1I
     O0oO0 ( 'tvshows' , 'Media Info 3' )
     if 73 - 73: I11i % i1IiiiI1iI . oooOo0oo0oo
 i1iii11 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 60 - 60: OOooOOo
 if 5 - 5: oOo0O0Ooo - oOo0O0Ooo - oOo0O0Ooo * ii
 for i1iiiIii11 in i1iii11 :
  OOoOOO000O0 = II1i11i1iIi11 + i1iiiIii11
  iiiiiII = O00O0oOO00O00 ( OOoOOO000O0 )
  if iiiiiII != 'Failed' :
   ii1ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( iiiiiII )
   for I11III111i , iIiIi11 in ii1ii :
    if Ii11 in iIiIi11 . lower ( ) :
     iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( II1i11i1iIi11 + i1iiiIii11 + I11III111i ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
     O0oO0 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 43 - 43: Ii1I - IiI1i11I
def o0O0O0ooo0oOO ( ) :
 iIiiiii1i ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 iIiiiii1i ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 iIiiiii1i ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 iIiiiii1i ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 O0oO0 ( 'tvshows' , 'INFO' )
 if 70 - 70: IiI1i11I / oooOo0oo0oo % i1iIi - o0ii1I
def i1II11Iii1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , iIii , oO00OoOOOo , I1i , Oo0 in IIi :
  iIiiiii1i ( ( '[COLORblue]' + iIiIi11 + '[/COLOR] [COLORred]Season[/COLOR]-' + iIii + ' [COLORred]Returns [/COLOR]- ' + Oo0 + ' ' + I1i ) , iIiIi11 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 80 - 80: o0ii1I - I11i
def iI1II1I1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , iIii , oO00OoOOOo in IIi :
  iIiiiii1i ( ( '[COLORblue]' + iIiIi11 + '[/COLOR] [COLORred]Season[/COLOR]-' + iIii + ' [COLORred] Status Unknown[/COLOR] ' ) , iIiIi11 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 79 - 79: oooOo0oo0oo / i1IiiiI1iI . OOooOOo - Ii1I
def Ii1ii11IIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , iIii , oO00OoOOOo , I1i in IIi :
  iIiiiii1i ( ( '[COLORblue]' + iIiIi11 + ' [COLORred] Cancelled On[/COLOR] ' + I1i ) , iIiIi11 , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 82 - 82: i1i1I1IIii1II * iI11I1II1I1I . I11i . Ii1I + oooOo0oo0oo / oOo0O0Ooo
def O0O0O ( url ) :
 Ii11 = ( url )
 II1i111 = Ii11 . lower ( )
 if 9 - 9: i1iIi
 if 41 - 41: IIiIiII11i
 O00oOoo0OoO0 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( Ii11 ) . replace ( ' ' , '+' )
 oo0O0oO0O0O = 'http://onlinemovies.tube/?s=' + ( Ii11 ) . replace ( ' ' , '+' )
 oOo0O = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 I11iIiii1 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I1ii1111Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 37 - 37: Iii . I1ii11iIi11i % III1iiIii * ooOoO0O00
 iIiII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 oOOOO = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 48 - 48: i1IiiiI1iI + IiI1i11I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 16 - 16: iI11I1II1I1I % Ii . OOooOOo % i1iIi + i1i1I1IIii1II . oO0o
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 46 - 46: oO0o - I11i / OOooOOo - ii + i1i1I1IIii1II
 if 58 - 58: I11i / I11i + i1iIi + Iii - OOooOOo . oooOo0oo0oo
 II11IiIi11 = O00O0oOO00O00 ( O00oOoo0OoO0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( oo0O0oO0O0O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( oOo0O )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( I11iIiii1 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 iiiiiII = O00O0oOO00O00 ( I1ii1111Ii )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 15 - 15: i1iIi * OOooOOo % III1iiIii . OOooOOo . Iii
 if 97 - 97: i1i1I1IIii1II
 oOOo = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 oo0oO0 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 oOoO0O00oo = O00O0oOO00O00 ( oOOOO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / IiI1i11I * i1i1I1IIii1II
 if oo0oO0 != 'Failed' :
  IiIiIi1I1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oo0oO0 )
  for url , iIiIi11 in IiIiIi1I1 :
   IiI1ii1Ii = O00O0oOO00O00 ( url )
   oooOOOoOOOo0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiI1ii1Ii )
   for O00oOoo0OoO0 , Ooo0 in oooOOOoOOOo0O :
    if II1i111 in Ooo0 . lower ( ) :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , url + O00oOoo0OoO0 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 29 - 29: I11i
     O0oO0 ( 'tvshows' , 'Media Info 3' )
 if oOOo != 'Failed' :
  oo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo )
  for url , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in oo0 :
   if II1i111 in iIiIi11 . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 2 - 2: ii
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 60 - 60: oO0o
    if 81 - 81: OOooOOo % o0ii1I
    if 87 - 87: iI11I1II1I1I . ii * OOooOOo
    if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % o0ii1I - iI11I1II1I1I
    if 17 - 17: Iii / I11i % I1ii11iIi11i
    if 71 - 71: III1iiIii . i1IiiiI1iI . oO0o
    if 68 - 68: Ii % i1i1I1IIii1II * oO0o * III1iiIii * IIiIiII11i + o0o00Oo0O
    if 66 - 66: Iii % Ii1I % ii
    if 34 - 34: I11i / IiI1i11I % o0o00Oo0O . oO0o . ooOoO0O00
    if 29 - 29: o0o00Oo0O . i1IiiiI1iI
    if 66 - 66: i1i1I1IIii1II * iI11I1II1I1I % iI11I1II1I1I * III1iiIii - i1iIi - III1iiIii
 if oOoO0O00oo != 'Failed' :
  o0O0oO0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOoO0O00oo )
  for url , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in o0O0oO0 :
   if II1i111 in iIiIi11 . lower ( ) :
    iIiiiii1i ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 77 - 77: o0o00Oo0O . o0ii1I
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  i1i1IiIi1 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , o00oOOooOOo0o , iIiIi11 , I1iiIiI1iI1I in i1Iii1i1I :
   if II1i111 in iIiIi11 . lower ( ) :
    if 'season' in I1iiIiI1iI1I :
     iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
    if 'episodes' in I1iiIiI1iI1I :
     iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
  for url in i1i1IiIi1 :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 27 - 27: Ii1I * i1IiiiI1iI - oO0o + o0ii1I * o0ii1I
   O0oO0 ( 'tvshows' , 'Media Info 3' )
 if II11IiIi11 != 'Failed' :
  iIO0O00OOo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11IiIi11 )
  for url , iIiIi11 , o00oOOooOOo0o in iIO0O00OOo :
   if II1i111 in iIiIi11 . lower ( ) :
    Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( iIiIi11 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , o00oOOooOOo0o , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 55 - 55: i1iIi
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 82 - 82: i1IiiiI1iI - oooOo0oo0oo + oO0o
    if 64 - 64: I11i . o0o00Oo0O * o0ii1I + ii - I1ii11iIi11i . ii
    if 70 - 70: I1ii11iIi11i - i1i1I1IIii1II . iI11I1II1I1I % Iii / OOooOOo - o0o00Oo0O
    if 55 - 55: IiI1i11I - oO0o
    if 100 - 100: o0o00Oo0O
    if 79 - 79: iI11I1II1I1I
    if 81 - 81: oooOo0oo0oo + iI11I1II1I1I * i1IiiiI1iI - iI11I1II1I1I . oooOo0oo0oo
    if 48 - 48: Iii . ii . oOo0O0Ooo . OOooOOo % Ii1I / IiI1i11I
    if 11 - 11: ooOoO0O00 % oO0o % IiI1i11I
 if o00OooOO000 != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for iIiIi11 in I1i11 :
   if II1i111 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( oOo0O + iIiIi11 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 99 - 99: i1iIi / iI11I1II1I1I - o0ii1I * Ii1I % oOo0O0Ooo
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  OooOo0oo0O0o00O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for iIiIi11 in OooOo0oo0O0o00O :
   if II1i111 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( I11iIiii1 + iIiIi11 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 13 - 13: oO0o
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if iiiiiII != 'Failed' :
  ii1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiiiiII )
  for url , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in ii1ii :
   if II1i111 in iIiIi11 . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 70 - 70: i1IiiiI1iI + o0o00Oo0O . i1i1I1IIii1II * o0ii1I
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 2 - 2: ii . oooOo0oo0oo . III1iiIii
 I1iIII1IiiI = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for i1iiiIii11 in I1iIII1IiiI :
  OOoOOO000O0 = oO0 + i1iiiIii11 + oOoOooOo0o0
  OooOoOOo0oO00 = O00O0oOO00O00 ( OOoOOO000O0 )
  if OooOoOOo0oO00 != 'Failed' :
   I1I1iII1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OooOoOOo0oO00 )
   for iIiIi11 , O0O0ooOOO , url , o00oOOooOOo0o , oOOo0O00o , oO0oOOoo00000 in I1I1iII1i :
    if II1i111 in iIiIi11 . lower ( ) :
     Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgold] - Source Pandoras[/COLOR]' , url , oO0oOOoo00000 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
     O0oO0 ( 'tvshows' , 'Media Info 3' )
     if 37 - 37: ooOoO0O00 - oooOo0oo0oo % ii / oooOo0oo0oo % i1iIi
     if 48 - 48: Ii % i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: IiI1i11I + Ii % Iii
def oOo00Ooo0o0 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( ( iIiIi11 ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + iI , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + iI )
def i1IiII1i1I ( url ) :
 iI1ii1ii1I = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( iI1ii1ii1I )
 sys . exit ( 1 )
 if 18 - 18: i1i1I1IIii1II * i1i1I1IIii1II % i1i1I1IIii1II
def Ii1I1I1i11ii ( ) :
 if 58 - 58: iI11I1II1I1I - Ii - Ii * o0ii1I + I11i . OOooOOo
 if 80 - 80: ooOoO0O00 + Ii - i1IiiiI1iI % IIiIiII11i . i1i1I1IIii1II
 if 10 - 10: Iii / Iii * Ii
 if 46 - 46: oO0o * I1ii11iIi11i % i1i1I1IIii1II + o0o00Oo0O * III1iiIii
 if 34 - 34: oO0o
 if 27 - 27: o0ii1I - o0o00Oo0O % Iii * i1IiiiI1iI . III1iiIii % iI11I1II1I1I
 if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % i1iIi
 if 24 - 24: OOooOOo
 if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + oooOo0oo0oo
 if 28 - 28: oOo0O0Ooo
 if 49 - 49: Iii . I11i % i1i1I1IIii1II / o0ii1I
 iIiiiii1i ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 iIiiiii1i ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 iIiiiii1i ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 O0oO0 ( 'tvshows' , 'INFO' )
 if 95 - 95: o0o00Oo0O * OOooOOo * III1iiIii . i1iIi / iI11I1II1I1I
def I1IIi1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , iIii1i1 in IIi :
  iIiiiii1i ( ( iIiIi11 + ' - ' + iIii1i1 ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 65 - 65: i1i1I1IIii1II + Ii1I / oooOo0oo0oo
def oo0oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 49 - 49: Ii % OOooOOo + i1IiiiI1iI . IIiIiII11i % IiI1i11I * oooOo0oo0oo
def oooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , iIiIi11 , url in IIi :
  iIiiiii1i ( iIiIi11 , url , 90054 , o00oOOooOOo0o )
 for url in next :
  iIiiiii1i ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 27 - 27: Ii - oOo0O0Ooo
def iii1IIiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , iIii1i1 , url , iIiIi11 , i1i1Ii11Ii in IIi :
  Iii1I1I11iiI1 ( iIii1i1 + ' - ' + iIiIi11 + ' - ' + i1i1Ii11Ii , url , 90044 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
 for o00oOOooOOo0o , iIiIi11 , url in i1Iii1i1I :
  iIiiiii1i ( iIiIi11 , url , 90044 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
 for url in next :
  iIiiiii1i ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 57 - 57: oooOo0oo0oo + i1IiiiI1iI % Ii1I . oO0o / oO0o * o0o00Oo0O
def Ii1iiII1i ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO00O = 'http://onlinemovies.tube/?s=' + ( Ii11 ) . replace ( ' ' , '+' )
 II1i111 = oO00O . lower ( )
 II11iIiIIIiI = OooOoooOo ( II1i111 )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , o00oOOooOOo0o , iIiIi11 , I1iiIiI1iI1I in IIi :
  if 'season' in I1iiIiI1iI1I :
   iIiiiii1i ( iIiIi11 , iI , 90054 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
  if 'episodes' in I1iiIiI1iI1I :
   iIiiiii1i ( iIiIi11 , iI , 90044 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
 for iI in next :
  iIiiiii1i ( 'NEXT' , iI , 90053 , iiIi1IIiIi + 'Next.png' )
  if 15 - 15: I1ii11iIi11i + I1ii11iIi11i / III1iiIii * Iii . i1iIi + IiI1i11I
def II1iIiiI11i11 ( ) :
 if 9 - 9: oO0o * Iii - o0ii1I
 if 14 - 14: Ii1I + Ii
 if 83 - 83: Ii1I / Ii + IIiIiII11i . IiI1i11I * oooOo0oo0oo + III1iiIii
 if 42 - 42: ooOoO0O00 % IIiIiII11i . i1iIi
 if 7 - 7: Ii1I - i1i1I1IIii1II * oooOo0oo0oo + I11i . Ii1I
 if 85 - 85: o0o00Oo0O
 if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * o0ii1I
 if 19 - 19: o0ii1I
 if 55 - 55: oooOo0oo0oo % oooOo0oo0oo / o0o00Oo0O % IiI1i11I - I11i . I1ii11iIi11i
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
 iIiiiii1i ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 iIiiiii1i ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 iIiiiii1i ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 iIiiiii1i ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 O0oO0 ( 'tvshows' , 'INFO' )
 if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
def IIiI11I1I1i1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , iIii1i1 in IIi :
  if 'genre' in url :
   iIiiiii1i ( ( iIiIi11 + ' - ' + iIii1i1 ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 86 - 86: ooOoO0O00
def i1o0oo0Ooooo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  if 'release' in url :
   iIiiiii1i ( iIiIi11 , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 76 - 76: ooOoO0O00 * ii * o0o00Oo0O + i1IiiiI1iI * i1IiiiI1iI
def i1iIiIii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , iIiIi11 , iI1iiI1III1i , url , O0O0ooOOO in IIi :
  Iii1I1I11iiI1 ( iIiIi11 + ' ' + iI1iiI1III1i , url , 90044 , o00oOOooOOo0o , o00oOOooOOo0o , O0O0ooOOO )
 for o00oOOooOOo0o , iIiIi11 , I1iiIiI1iI1I , url , iii1i11 , O0O0ooOOO in i1Iii1i1I :
  if 'movies' in I1iiIiI1iI1I :
   Iii1I1I11iiI1 ( iIiIi11 + ' - ' + iii1i11 , url , 90044 , o00oOOooOOo0o , o00oOOooOOo0o , O0O0ooOOO )
 for url in next :
  iIiiiii1i ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 56 - 56: oOo0O0Ooo
def ii1IIi1ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  oo0OoOOooO ( 'http:' + url )
  if 60 - 60: i1IiiiI1iI
def oo0OoOOooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  iiIi1IIiI ( ( iIiIi11 ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def oOO0o00o0Oo0O ( ) :
 if 41 - 41: oO0o - IIiIiII11i + o0ii1I
 if 11 - 11: i1i1I1IIii1II + iI11I1II1I1I
 if 10 - 10: o0o00Oo0O
 if 68 - 68: oooOo0oo0oo + i1i1I1IIii1II . o0o00Oo0O . o0ii1I % ooOoO0O00 % oooOo0oo0oo
 if 50 - 50: III1iiIii + I11i
 if 96 - 96: oO0o
 if 92 - 92: I1ii11iIi11i / Ii + Ii1I
 if 87 - 87: OOooOOo % iI11I1II1I1I
 if 72 - 72: oooOo0oo0oo . oooOo0oo0oo - Ii1I
 if 48 - 48: I1ii11iIi11i - i1iIi + I1ii11iIi11i - oOo0O0Ooo * Ii . IiI1i11I
 if 35 - 35: III1iiIii . o0o00Oo0O + I1ii11iIi11i + oooOo0oo0oo + ooOoO0O00
 if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
 if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
 if 58 - 58: oooOo0oo0oo . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO00O = 'http://onlinemovies.tube/?s=' + ( Ii11 ) . replace ( ' ' , '+' )
 II1i111 = oO00O . lower ( )
 II11iIiIIIiI = OooOoooOo ( II1i111 )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , o00oOOooOOo0o , iIiIi11 , I1Iii1Ii1i1 in IIi :
  if 'movies' in I1Iii1Ii1i1 :
   iIiiiii1i ( I1Iii1Ii1i1 + '-' + iIiIi11 , iI , 90044 , o00oOOooOOo0o )
 for iI in next :
  i1iIiIii ( iI )
  if 10 - 10: IiI1i11I . ooOoO0O00 + o0ii1I
def II1iiiiII ( ) :
 iIiiiii1i ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , iI , 80006 , iiIi1IIiIi + 'Desi.png' )
def oOOoOOO0oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  iiIi1IIiI ( iIiIi11 , url , 80007 , o00oOOooOOo0o )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  iIiiiii1i ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def O00OO0OOOOOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  OooO0OO ( url )
def oo0ooO0 ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO00O = 'http://www.join4films.com/?s=' + ( Ii11 ) . replace ( ' ' , '+' ) + '&search_type=1'
 II1i111 = oO00O . lower ( )
 oOOoOOO0oo0 ( II1i111 )
 if 65 - 65: oO0o - iI11I1II1I1I
 if 20 - 20: OOooOOo % Ii1I
 if 44 - 44: ii . IIiIiII11i . oooOo0oo0oo % ii
 if 86 - 86: Ii + o0o00Oo0O * III1iiIii - oO0o * oooOo0oo0oo + o0o00Oo0O
 if 95 - 95: iI11I1II1I1I . i1IiiiI1iI % IiI1i11I - i1IiiiI1iI * IIiIiII11i
 if 89 - 89: IiI1i11I . oOo0O0Ooo
 if 59 - 59: ooOoO0O00 % iI11I1II1I1I + ii
 if 97 - 97: Ii1I / I1ii11iIi11i + i1IiiiI1iI
 if 32 - 32: i1iIi % i1IiiiI1iI * I1ii11iIi11i
 if 72 - 72: i1iIi . IiI1i11I - i1IiiiI1iI - o0ii1I % ooOoO0O00
 if 56 - 56: I1ii11iIi11i * IiI1i11I
 if 13 - 13: I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * IiI1i11I . ooOoO0O00 / III1iiIii
 if 92 - 92: o0ii1I * Ii + IiI1i11I * i1IiiiI1iI
 if 48 - 48: Iii * IiI1i11I * IiI1i11I
 if 70 - 70: i1i1I1IIii1II + Iii % Ii + o0o00Oo0O
 if 65 - 65: iI11I1II1I1I % i1i1I1IIii1II + o0o00Oo0O / ii
 if 52 - 52: o0ii1I % oooOo0oo0oo * oOo0O0Ooo % Iii + oooOo0oo0oo / IiI1i11I
def oo000o ( ) :
 Iii1I1I11iiI1 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 95 - 95: i1i1I1IIii1II - i1iIi * Iii / oO0o / IIiIiII11i + o0o00Oo0O
def I1I ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO00O = 'http://imoviemax.se/?s=' + ( Ii11 ) . replace ( ' ' , '+' )
 II1i111 = oO00O . lower ( )
 oo0o00oOo0 ( II1i111 )
def O0OOo ( url ) :
 i1I1Iiii1 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , O0ooooo000 in IIi :
  if iIiIi11 in i1I1Iiii1 :
   pass
  else :
   Iii1I1I11iiI1 ( iIiIi11 + ' - ' + O0ooooo000 + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   i1I1Iiii1 . append ( iIiIi11 )
   if 97 - 97: Ii % i1i1I1IIii1II / I1ii11iIi11i / I1ii11iIi11i
def OoO00ooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , iiO0o0O0oo0o in IIi :
  Iii1I1I11iiI1 ( iIiIi11 + ' - Views:' + iiO0o0O0oo0o , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 100 - 100: III1iiIii . o0ii1I - iI11I1II1I1I . Ii / IIiIiII11i
  if 71 - 71: i1IiiiI1iI * I1ii11iIi11i . Iii
def oo0o00oOo0 ( url ) :
 i1ii1iiIi1II = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  Iii1I1I11iiI1 ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , iIiIi11 , url in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 10075 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
  i1ii1iiIi1II . append ( iIiIi11 )
  if 98 - 98: oO0o - o0ii1I . III1iiIii % Ii
def OO00oo ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for O0Oo0O0 , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  I1IiiIiii1 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + I1IiiIiii1
  i11i = ( O0Oo0O0 ) . replace ( 'play-' , 'Server ' )
  I1I1i1I ( i11i , I1IiiIiii1 , 10076 , img , img , '' )
  if 86 - 86: o0ii1I
def IiII1i1iI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for oo0O0oO0O0O in IIi :
  if '=m' in oo0O0oO0O0O :
   O0OOO00 ( oo0O0oO0O0O )
  elif 'php' in oo0O0oO0O0O :
   IiII1i1iI ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( oo0O0oO0O0O )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for oOo0O in IIi :
    O0OOO00 ( oo0O0oO0O0O )
    if 62 - 62: Ii + OOooOOo + ooOoO0O00
    if 69 - 69: OOooOOo
    if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . i1IiiiI1iI
def Ooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iIiiiIiIi = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1i , i1I1Ii11i in iIiiiIiIi :
  print 'there ><><><><><><><><><><><><'
  I1i = I1i
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1I1Ii11i ) )
  for iIiIi11 , I1iIiiiI1 in IIi :
   print 'here <><><><><><><><><><><><>'
   Iii1I1I11iiI1 ( '[COLORred]' + I1i + '[/COLOR] - ' + iIiIi11 + ' - [COLOR' + ooOoOoo0O + ']' + I1iIiiiI1 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 I1iiiiI1iI = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1i , OOO0O00Oo in I1iiiiI1iI :
  print 'there ><><><><><><><><><><><><'
  I1i = I1i
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OOO0O00Oo ) )
  for iIiIi11 , I1iIiiiI1 in IIi :
   print 'here <><><><><><><><><><><><>'
   Iii1I1I11iiI1 ( '[COLORred]' + I1i + '[/COLOR] - ' + iIiIi11 + ' - [COLOR' + ooOoOoo0O + ']' + I1iIiiiI1 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 13 - 13: iI11I1II1I1I
   if 2 - 2: ooOoO0O00 * i1i1I1IIii1II - i1i1I1IIii1II + ii % OOooOOo / OOooOOo
   if 3 - 3: ii
def OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1iiiiI1iI in I1iiiiI1iI :
  iIiIi11 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
  for iIiIi11 in iIiIi11 :
   iIiIi11 = ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1iiiiI1iI ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  oOo00 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
  for oOo00 in oOo00 :
   oOo00 = 'http:' + oOo00
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , '' , '' )
  if 71 - 71: III1iiIii + ooOoO0O00 - IiI1i11I - Ii . Iii - i1iIi
  if 85 - 85: Ii1I - OOooOOo / Ii1I + oooOo0oo0oo - IiI1i11I
  if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + i1IiiiI1iI
  if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * i1i1I1IIii1II
def O0OoOO0oo0 ( url ) :
 if 85 - 85: IIiIiII11i . i1iIi % oooOo0oo0oo % Iii
 OOo00ooOoO0o = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oo0O0oO0O0O , o00oOOooOOo0o , iIiIi11 , i1i1iiIIiiiII in IIi :
  iIiIi11 = ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( oo0O0oO0O0O )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for O00O0OO00oo , I1iIII1 in i1Iii1i1I :
   Ii1I1 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( I1iIII1 ) )
   for O0O0ooOOO in Ii1I1 :
    if iIiIi11 in OOo00ooOoO0o :
     pass
    else :
     I1I1i1I ( iIiIi11 , O00O0OO00oo , 8043 , o00oOOooOOo0o , o00oOOooOOo0o , O0O0ooOOO )
     O0oO0 ( 'movies' , 'INFO' )
     OOo00ooOoO0o . append ( iIiIi11 )
     if 71 - 71: OOooOOo + iI11I1II1I1I * i1i1I1IIii1II . i1IiiiI1iI % Ii % iI11I1II1I1I
     if 63 - 63: ii * oO0o / Iii - i1i1I1IIii1II . iI11I1II1I1I + IiI1i11I
def ii1IIiI1IIi ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOo0 )
 for url , oo00O00oO000o , O0O0ooOOO , oOOo0O00o , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 10065 , oo00O00oO000o , oOOo0O00o , O0O0ooOOO )
 O0oO0 ( 'movies' , 'INFO' )
 if 76 - 76: IiI1i11I / oO0o + OOooOOo
def Oooo00 ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO00O = 'https://www.youtube.com/results?search_query=' + ( Ii11 ) . replace ( ' ' , '+' )
 II1i111 = oO00O . lower ( )
 II11iIiIIIiI = OooOoooOo ( II1i111 )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for iI in next :
  iI = 'https://www.youtube.com' + iI
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , iI , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for o00oOOooOOo0o , iI , iIiIi11 , iii1II1iI1IIi , I1iIII1 in IIi :
  OOO00 . append ( iIiIi11 )
  O0oO0 ( 'tvshows' , 'INFO' )
  oOo00 = 'http:' + ( o00oOOooOOo0o ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOo00
  iI = 'http://www.youtube.com' + iI
  I1I1i1I ( '[COLORred]' + iii1II1iI1IIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , ( iI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , oOo00 , I1iIII1 )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for o00oOOooOOo0o , iI , iIiIi11 , iii1II1iI1IIi in IIi :
   print 'im doing it'
   O0oO0 ( 'tvshows' , 'INFO' )
   oOo00 = 'http:' + ( o00oOOooOOo0o ) . replace ( 'https:' , '' )
   iI = 'http://www.youtube.com' + iI
   if '&' in iI :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( iI )
    I1iiiiI1iI = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for I1iiiiI1iI in I1iiiiI1iI :
     iIiIi11 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
     for iIiIi11 in iIiIi11 :
      iIiIi11 = ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     iI = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1iiiiI1iI ) )
     for iI in iI :
      iI = 'https://www.youtube.com/w' + iI
     oOo00 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
     for oOo00 in oOo00 :
      oOo00 = 'http:' + oOo00
     I1I1i1I ( '[COLORred]' + iii1II1iI1IIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , ( iI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , Oo00OOOOO , '' )
   elif iIiIi11 in OOO00 :
    pass
   elif 'user' in iI or 'elete' in iIiIi11 :
    pass
   elif 'hannel' in iI :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iI
    II11iIiIIIiI = OooOoooOo ( iI )
    Ii11iiI1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for o00oOOooOOo0o , iI , iIiIi11 in Ii11iiI1 :
     if 'outube' in iI or 'list' in iI :
      pass
     elif 'atch' in iI :
      iI = ( iI ) . replace ( '/watch?v=' , '' )
      I1I1i1I ( '[COLORred]' + iii1II1iI1IIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , ( iI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00oOOooOOo0o , 'http:' + o00oOOooOOo0o , '' )
     else :
      pass
   else :
    I1I1i1I ( '[COLORred]' + iii1II1iI1IIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , ( iI ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , oOo00 , '' )
    if 71 - 71: I11i / oooOo0oo0oo % oooOo0oo0oo
def OoooO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for o00oOOooOOo0o , url , iIiIi11 , iii1II1iI1IIi , I1iIII1 in IIi :
  OOO00 . append ( iIiIi11 )
  O0oO0 ( 'tvshows' , 'INFO' )
  oOo00 = 'http:' + ( o00oOOooOOo0o ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOo00
  url = 'http://www.youtube.com' + url
  I1I1i1I ( '[COLORred]' + iii1II1iI1IIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , oOo00 , I1iIII1 )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for o00oOOooOOo0o , url , iIiIi11 , iii1II1iI1IIi in IIi :
   O0oO0 ( 'tvshows' , 'INFO' )
   oOo00 = 'http:' + ( o00oOOooOOo0o ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    I1iiiiI1iI = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for I1iiiiI1iI in I1iiiiI1iI :
     iIiIi11 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
     for iIiIi11 in iIiIi11 :
      iIiIi11 = ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1iiiiI1iI ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     oOo00 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
     for oOo00 in oOo00 :
      oOo00 = 'http:' + oOo00
     I1I1i1I ( '[COLORred]' + iii1II1iI1IIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , Oo00OOOOO , '' )
   elif iIiIi11 in OOO00 :
    pass
   elif 'user' in url or 'elete' in iIiIi11 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    Ii11iiI1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for o00oOOooOOo0o , url , iIiIi11 in Ii11iiI1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      I1I1i1I ( '[COLORred]' + iii1II1iI1IIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00oOOooOOo0o , 'http:' + o00oOOooOOo0o , '' )
     else :
      pass
   else :
    I1I1i1I ( '[COLORred]' + iii1II1iI1IIi + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , oOo00 , '' )
    if 75 - 75: i1iIi
    if 29 - 29: Ii1I
    if 53 - 53: Ii . Ii1I % o0ii1I / i1iIi % iI11I1II1I1I
def iIiIii1I1 ( ) :
 I1I1i1I ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 I1I1i1I ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 81 - 81: III1iiIii - I11i - I1ii11iIi11i - o0ii1I / oooOo0oo0oo % Iii
def oO0OoOo ( ) :
 ivuesetup . iVueInt ( )
 if 89 - 89: I1ii11iIi11i + Ii1I - I11i
def iII1I11 ( ) :
 ii11iiI11I ( )
 return
 if 96 - 96: iI11I1II1I1I + Ii - I1ii11iIi11i . i1iIi
def ii11iiI11I ( ) :
 if 31 - 31: iI11I1II1I1I % Ii - III1iiIii
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 oOoO0OOO00O = II1I . getSetting ( id = 'User' )
 OOOOO0o0OOo = II1I . getSetting ( id = 'Pass' )
 I11I11I11IiIi = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 OO = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 ii1ii1i11I1I = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 iiII1iiiiiii = "http://piesustv.net:8000/get.php?username=" + oOoO0OOO00O + "&password=" + OOOOO0o0OOo + "&type=m3u_plus&output=ts"
 iiIiii = "http://piesustv.net:8000/xmltv.php?username=" + oOoO0OOO00O + "&password=" + OOOOO0o0OOo + "&type=m3u_plus&output=ts"
 if 39 - 39: oOo0O0Ooo + I1ii11iIi11i
 xbmc . executeJSONRPC ( I11I11I11IiIi )
 xbmc . executeJSONRPC ( OO )
 xbmc . executeJSONRPC ( ii1ii1i11I1I )
 if 83 - 83: ooOoO0O00
 O0OooOO = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 O0OooOO . setSetting ( id = 'm3uUrl' , value = iiII1iiiiiii )
 O0OooOO . setSetting ( id = 'epgUrl' , value = iiIiii )
 O0OooOO . setSetting ( id = 'm3uCache' , value = "false" )
 O0OooOO . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def i1i1 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
 o0oOoOo0 ( )
if 38 - 38: I11i % i1IiiiI1iI + Ii + IiI1i11I + i1iIi / Ii
if 94 - 94: IiI1i11I - I1ii11iIi11i + i1i1I1IIii1II
def o0oOoOo0 ( ) :
 if 59 - 59: Iii . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
 if 56 - 56: i1i1I1IIii1II + i1iIi
 if 32 - 32: IIiIiII11i + OOooOOo % i1iIi / OOooOOo + Ii1I
 if 2 - 2: Ii - i1IiiiI1iI + oO0o % Iii * o0ii1I
 if 54 - 54: o0o00Oo0O - IiI1i11I . oooOo0oo0oo % IiI1i11I + IiI1i11I
 if 36 - 36: oooOo0oo0oo % Ii
 if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * i1i1I1IIii1II . Iii / ooOoO0O00
 if 50 - 50: i1IiiiI1iI / ooOoO0O00 % ii
 if 83 - 83: Ii1I * Ii1I + oooOo0oo0oo
 if 57 - 57: o0o00Oo0O - o0o00Oo0O . Ii1I / I11i / o0ii1I
 if 20 - 20: oooOo0oo0oo * IIiIiII11i - OOooOOo - i1i1I1IIii1II * i1IiiiI1iI
 if 6 - 6: i1iIi + oooOo0oo0oo / I1ii11iIi11i + III1iiIii % IIiIiII11i / oO0o
 if OO0o == "insert_username" :
  iiIi = OooooOo ( )
  IIIiiiIiI = OO0OOoooo0o ( )
  I11 ( 'User' , iiIi )
  I11 ( 'Pass' , IIIiiiIiI )
  xbmc . executebuiltin ( 'Container.Refresh' )
  IiIi1Ii = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( iiIi , IIIiiiIiI )
  IiIi1Ii = OooOoooOo ( IiIi1Ii )
  if IiIi1Ii == "" :
   iiIIiI11II1 = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   oooOo = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   oOoO0Oo0 = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , iiIIiI11II1 , oooOo , oOoO0Oo0 )
   o0oOoOo0 ( )
  else :
   iiIIiI11II1 = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   oooOo = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   oOoO0Oo0 = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % iiIi )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , iiIIiI11II1 , oooOo , oOoO0Oo0 )
   xbmc . executebuiltin ( 'Container.Refresh' )
   i11i11i ( )
 else :
  i11i11i ( )
def OooooOo ( ) :
 iiI1iI = xbmc . Keyboard ( '' , 'heading' , True )
 iiI1iI . setHeading ( 'Enter Username' )
 iiI1iI . setHiddenInput ( False )
 iiI1iI . doModal ( )
 if ( iiI1iI . isConfirmed ( ) ) :
  Ooo00O0 = iiI1iI . getText ( )
  return Ooo00O0
 else :
  return False
  if 70 - 70: oOo0O0Ooo - i1iIi - oO0o - OOooOOo . Ii % ooOoO0O00
  if 1 - 1: i1i1I1IIii1II / ooOoO0O00
def OO0OOoooo0o ( ) :
 iiI1iI = xbmc . Keyboard ( '' , 'heading' , True )
 iiI1iI . setHeading ( 'Enter Password' )
 iiI1iI . setHiddenInput ( False )
 iiI1iI . doModal ( )
 if ( iiI1iI . isConfirmed ( ) ) :
  Ooo00O0 = iiI1iI . getText ( )
  return Ooo00O0
 else :
  return False
def O0oo0 ( ) :
 iiII1iiiiiii = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  iii1iiii11I = urllib2 . urlopen ( iiII1iiiiiii )
  print iii1iiii11I . getcode ( )
  iii1iiii11I . close ( )
  if 56 - 56: IiI1i11I . i1IiiiI1iI
  pass
  if 3 - 3: o0ii1I + i1IiiiI1iI . ooOoO0O00 / oooOo0oo0oo % i1IiiiI1iI
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def i11i11i ( ) :
 iii ( )
 if 98 - 98: III1iiIii * iI11I1II1I1I . o0ii1I * I1ii11iIi11i / Ii1I + i1iIi
 if 25 - 25: i1i1I1IIii1II
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 19 - 19: oOo0O0Ooo % o0ii1I . III1iiIii * i1iIi
 if 89 - 89: OOooOOo . oooOo0oo0oo
 if 7 - 7: i1i1I1IIii1II % OOooOOo - oOo0O0Ooo + I1ii11iIi11i
 if 70 - 70: IIiIiII11i + i1IiiiI1iI + Ii - ooOoO0O00 / III1iiIii
def iI1IIiiIIIII ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 i1iIii = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 o0O0ooooooo00 = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 IiIi1Ii = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 IiIi1Ii = OooOoooOo ( IiIi1Ii )
 if not IiIi1Ii == "" :
  I1111ii11IIII = 'https://tinyurl.com/create.php?source=indexpage&url=' + i1iIii + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( I1111ii11IIII ) )
  IiIi1II111I = 'https://tinyurl.com/create.php?source=indexpage&url=' + o0O0ooooooo00 + '&submit=Make+TinyURL%21&alias='
  i1iIii = OooOoooOo ( I1111ii11IIII )
  o0O0ooooooo00 = OooOoooOo ( IiIi1II111I )
  xbmc . log ( str ( o0O0ooooooo00 ) )
  o00o = IIi1i1 ( i1iIii , '<div class="indent"><b>' , '</b>' )
  o0O0Ooo = IIi1i1 ( o0O0ooooooo00 , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % o00o , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % o0O0Ooo )
 else :
  return
def O0oO00oOOooO ( ) :
 O0oo0 ( )
 IiIIii1iiI ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , ii1IiiII + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( IiiI1II1II1i )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( ( '[COLORsteelblue]' + iIiIi11 + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , iI , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def iIO0OO0o0O00oO ( url ) :
 open = OooOoooOo ( o00OoO0o0oOo + url )
 OoO0O0oo0o = iIi11I11 ( open , '<channel>' , '</channel>' )
 for i1ioO in OoO0O0oo0o :
  if '<playlist_url>' in open :
   iIiIi11 = IIi1i1 ( i1ioO , '<title>' , '</title>' )
   O00oOoo0OoO0 = IIi1i1 ( i1ioO , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   Iii1I1I11iiI1 ( str ( base64 . b64decode ( iIiIi11 ) ) . replace ( '?' , '' ) , O00oOoo0OoO0 , 3 , icon , oOOo0O00o , '' )
  else :
   iIiIi11 = IIi1i1 ( i1ioO , '<title>' , '</title>' )
   iIiIi11 = base64 . b64decode ( iIiIi11 )
   I11iiI = IIi1i1 ( i1ioO , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = IIi1i1 ( i1ioO , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   O0O0ooOOO = IIi1i1 ( i1ioO , '<description>' , '</description>' )
   O0O0ooOOO = base64 . b64decode ( O0O0ooOOO )
   i1iIii1i111 = IIi1i1 ( O0O0ooOOO , 'PLOT:' , '\n' )
   OOooo000OooO = IIi1i1 ( O0O0ooOOO , 'CAST:' , '\n' )
   o0o0OoOo = IIi1i1 ( O0O0ooOOO , 'RATING:' , '\n' )
   IiI1 = IIi1i1 ( O0O0ooOOO , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   IiI1 = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( IiI1 )
   iiIiII = IIi1i1 ( O0O0ooOOO , 'DURATION_SECS:' , '\n' )
   IIiiiI1iI = IIi1i1 ( O0O0ooOOO , 'GENRE:' , '\n' )
   O0O0 ( str ( iIiIi11 ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , I11iiI , oOOo0O00o , i1iIii1i111 , str ( IiI1 ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( OOooo000OooO ) . split ( ) , o0o0OoOo , iiIiII , IIiiiI1iI )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 70 - 70: oooOo0oo0oo * i1i1I1IIii1II / oOo0O0Ooo * OOooOOo * oOo0O0Ooo
OOoO0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 38 - 38: ooOoO0O00 . Ii
def O0ooO0O0Ooo0o ( ) :
 iiII1iiiiiii = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  iii1iiii11I = urllib2 . urlopen ( iiII1iiiiiii )
  print iii1iiii11I . getcode ( )
  iii1iiii11I . close ( )
  if 25 - 25: oooOo0oo0oo * oooOo0oo0oo / i1i1I1IIii1II % I1ii11iIi11i
  pass
  if 33 - 33: III1iiIii . ii . i1i1I1IIii1II
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 15 - 15: Ii1I . IiI1i11I
 iI = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 o0Iiii ( iI , O00Oo + "uide.xml" )
 if 45 - 45: o0ii1I / i1iIi . ii + oO0o
 ooOoO00 = open ( OOoO0o , 'r+' )
 input = open ( OOoO0o ) . read ( ) . decode ( 'UTF-8' )
 O00oO000Oo0 = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 ooOoO00 . write ( O00oO000Oo0 )
 ooOoO00 . truncate ( )
 ooOoO00 . close ( )
 iIIiiIi ( )
 if 19 - 19: I11i
def iIIiiIi ( ) :
 open = OooOoooOo ( o00OOOOOo0OOo )
 all = iIi11I11 ( open , '{"num' , 'direct' )
 for i1ioO in all :
  if '"tv_archive":1' in i1ioO :
   iIiIi11 = IIi1i1 ( i1ioO , '"epg_channel_id":"' , '"' )
   I11iiI = IIi1i1 ( i1ioO , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = IIi1i1 ( i1ioO , 'stream_id":"' , '"' )
   iIiIi11 = iIiIi11 . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   Iii1I1I11iiI1 ( iIiIi11 , 'url' , 90027 , I11iiI , oOOo0O00o , iIiIi11 )
   if 44 - 44: Iii * I11i
   if 49 - 49: oooOo0oo0oo % Iii * Ii / i1i1I1IIii1II % oooOo0oo0oo
def OO0oO ( name , description ) :
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 O0OO0OoO = open ( OOoO0o )
 o0OOo = ElementTree . parse ( O0OO0OoO )
 IiI1Ii11Ii = "apples"
 import datetime as dt
 from datetime import time
 OoO0oO0oo0O = datetime . now ( ) - timedelta ( days = 5 )
 I1i = str ( OoO0oO0oo0O )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 oooOOO0ooOoOOO = o0OOo . findall ( "programme" )
 for o0IiIiI111IIII1 in oooOOO0ooOoOOO :
  if name in o0IiIiI111IIII1 . attrib . get ( 'channel' ) :
   OOOoOooO000oO = o0IiIiI111IIII1 . attrib . get ( 'start' )
   o0OOOOOo00 , oo0oOO , IIO000oooOO0Oo0 = OOOoOooO000oO . partition ( ' +' )
   I1i = str ( I1i ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   IiI1 , I1iIiIii , Oo0 = OOOoOooO000oO . partition ( '2017' )
   OO0I1iiI1iiI1i1 = o0IiIiI111IIII1 . find ( 'title' ) . text + OOOoOooO000oO
   Oo0 = Oo0 [ : - 6 ]
   if o0OOOOOo00 > I1i :
    if o0OOOOOo00 < I1IIIii :
     OOOO00OOO00 = o0OOOOOo00
     OOOO00OOO00 = OOOO00OOO00 [ : 4 ] + '/' + OOOO00OOO00 [ 4 : ]
     o0OOOOOo00 = o0OOOOOo00 [ : 4 ] + '-' + o0OOOOOo00 [ 4 : ]
     OOOO00OOO00 = OOOO00OOO00 [ : 7 ] + '/' + OOOO00OOO00 [ 7 : ]
     o0OOOOOo00 = o0OOOOOo00 [ : 7 ] + '-' + o0OOOOOo00 [ 7 : ]
     OOOO00OOO00 = OOOO00OOO00 [ : 10 ] + ' - ' + OOOO00OOO00 [ 10 : ]
     o0OOOOOo00 = o0OOOOOo00 [ : 10 ] + ':' + o0OOOOOo00 [ 10 : ]
     OOOO00OOO00 = OOOO00OOO00 [ : 15 ] + ':' + OOOO00OOO00 [ 15 : ]
     o0OOOOOo00 = o0OOOOOo00 [ : 13 ] + '-' + o0OOOOOo00 [ 13 : ]
     OOOO00OOO00 = OOOO00OOO00 [ : - 2 ]
     o0OOOOOo00 = o0OOOOOo00 [ : - 2 ]
     ii1OO0 = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&stream=%s&start=" ) % ( OO0o , Ooo , description )
     IiI1Ii11Ii = ii1OO0 + str ( o0OOOOOo00 ) + "&duration=240"
     OOOO00OOO00 = '[COLOR blue]%s - [/COLOR]' % OOOO00OOO00
     OO0I1iiI1iiI1i1 = str ( OOOO00OOO00 ) + o0IiIiI111IIII1 . find ( 'title' ) . text
     O0O0ooOOO = o0IiIiI111IIII1 . find ( 'desc' ) . text
     I1I1i1I ( OO0I1iiI1iiI1i1 , IiI1Ii11Ii , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , O0O0ooOOO )
     if 96 - 96: o0o00Oo0O . IiI1i11I - oOo0O0Ooo * I1ii11iIi11i
def o0Iiii ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 OOoOOOo0 = time . time ( )
 urllib . urlretrieve ( url , dest , lambda oOoO00O , I11I1I1i1i , Oo0oOO0O00 : o00OOo0o0O ( oOoO00O , I11I1I1i1i , Oo0oOO0O00 , o0oOoO00o , OOoOOOo0 ) )
def o00OOo0o0O ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  I111Iii1 = min ( numblocks * blocksize * 100 / filesize , 100 )
  i11iO0o0O00o0o = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  II1IIiiI1 = numblocks * blocksize / ( time . time ( ) - start_time )
  if II1IIiiI1 > 0 :
   O00O00 = ( filesize - numblocks * blocksize ) / II1IIiiI1
  else :
   O00O00 = 0
  II1IIiiI1 = II1IIiiI1 / 1024
  oOooO0OoO = II1IIiiI1 / 1024
  o0oOOOOoo0 = float ( filesize ) / ( 1024 * 1024 )
  ooOO0OOO00o = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( i11iO0o0O00o0o )
  II1iI1I11I = '[COLOR white]Speed:  %.02f Mb/s ' % oOooO0OoO + '[/COLOR]'
  dp . update ( I111Iii1 , ooOO0OOO00o , II1iI1I11I )
 except :
  I111Iii1 = 100
  dp . update ( I111Iii1 )
 if dp . iscanceled ( ) :
  OoOoO0ooooO0 = xbmcgui . Dialog ( )
  OoOoO0ooooO0 . ok ( "GenieTv" , 'The download was cancelled.' )
  if 4 - 4: I1ii11iIi11i - oO0o - Ii * i1IiiiI1iI / o0ii1I - oooOo0oo0oo
  sys . exit ( )
  dp . close ( )
  if 45 - 45: I11i % I1ii11iIi11i * ooOoO0O00 - o0o00Oo0O
def oo00ooOooO ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  ooIi111iII ( )
  if 83 - 83: ii + oO0o * i1i1I1IIii1II . o0o00Oo0O
  if 13 - 13: I11i
  if 7 - 7: oOo0O0Ooo + III1iiIii / Ii / I1ii11iIi11i
  if 97 - 97: i1IiiiI1iI . Iii / oOo0O0Ooo
  if 83 - 83: Iii - Ii1I * i1i1I1IIii1II
  if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
  if 75 - 75: Ii1I - OOooOOo * Ii . ii - I1ii11iIi11i . Iii
  if 6 - 6: Iii * i1i1I1IIii1II / ii % o0ii1I * I11i
def ooIi111iII ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for iI in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def i11i11Iiii11i ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 II11II1I = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 iIO0O00OOo = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 I1i11 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OooOo0oo0O0o00O = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OoOOo = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 ii1ii = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 III1I1I = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 O0OO00000o00 = OOO000Oo ( )
 I1IIIi1i = OooIii1I1iI ( )
 for url in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in II11II1I :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in iIO0O00OOo :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OooOo0oo0O0o00O :
  dt = datetime . fromtimestamp ( float ( OooOo0oo0O0o00O [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iiIi1IIiI ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1i11 :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OoOOo :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in ii1ii :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in III1I1I :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 I1I1i1I ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + O0OO00000o00 , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + I1IIIi1i , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 62 - 62: i1i1I1IIii1II + I1ii11iIi11i / Ii
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 90 - 90: iI11I1II1I1I + OOooOOo
def IiIIIiI ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 II1 ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 17 - 17: I1ii11iIi11i + ii * ii
def i1iiIIiII1 ( data ) :
 o0O00OooooO = len ( data ) % 4
 if 77 - 77: oOo0O0Ooo % i1iIi
 if 74 - 74: OOooOOo / ooOoO0O00 % ii
 if 52 - 52: III1iiIii % i1iIi
 if 25 - 25: Iii / Iii % ii - Ii1I * i1i1I1IIii1II
 if 23 - 23: Ii
 if 100 - 100: i1i1I1IIii1II + o0o00Oo0O . oOo0O0Ooo + ooOoO0O00 - OOooOOo + I11i
 if o0O00OooooO != 0 :
  data += b'=' * ( 4 - o0O00OooooO )
 return base64 . decodestring ( data )
def IIi1i1 ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : ooOOo = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : ooOOo = ''
 else :
  try : ooOOo = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : ooOOo = ''
 return ooOOo
 if 5 - 5: o0o00Oo0O
 if 75 - 75: i1IiiiI1iI + iI11I1II1I1I
def iIi11I11 ( text , start_with , end_with ) :
 ooOOo = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return ooOOo
def OOO000Oo ( ) :
 IiiiI1 = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 IiiiI1 . connect ( ( '8.8.8.8' , 0 ) )
 IiiiI1 = IiiiI1 . getsockname ( ) [ 0 ]
 return IiiiI1
 if 34 - 34: o0ii1I + I1ii11iIi11i - ooOoO0O00 - III1iiIii + iI11I1II1I1I
def OooIii1I1iI ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 O0OO00000o00 = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( O0OO00000o00 . group ( ) )
ii1IiiII = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
o00OOOOOo0OOo = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
o0Oo00oOO = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
O0oo = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
o0000O00oO0O = '&action=get_live_categories'
IiiI111I11 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
IiiI1II1II1i = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 98 - 98: o0ii1I
o00OoO0o0oOo = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
Iiiii1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
O0Ooo0O = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
iii1oOo0OoOOOo0 = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 55 - 55: i1i1I1IIii1II + o0o00Oo0O / IiI1i11I % i1iIi / ii
def O00o0OO0OO0oo ( ) :
 O0oo0 ( )
 open = OooOoooOo ( O0Ooo0O )
 OoO0O0oo0o = iIi11I11 ( open , '<channel>' , '</channel>' )
 for i1ioO in OoO0O0oo0o :
  iIiIi11 = IIi1i1 ( i1ioO , '<title>' , '</title>' )
  iIiIi11 = base64 . b64decode ( iIiIi11 )
  O00oOoo0OoO0 = IIi1i1 ( i1ioO , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  Iii1I1I11iiI1 ( '[COLORsteelblue]' + iIiIi11 + '[/COLOR]' , O00oOoo0OoO0 , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 59 - 59: ii % Iii / i1IiiiI1iI + ii . ii
def o0OoooO ( url ) :
 open = OooOoooOo ( iii1oOo0OoOOOo0 + url )
 OoO0O0oo0o = iIi11I11 ( open , '<channel>' , '</channel>' )
 for i1ioO in OoO0O0oo0o :
  iIiIi11 = IIi1i1 ( i1ioO , '<title>' , '</title>' )
  iIiIi11 = base64 . b64decode ( iIiIi11 )
  xbmc . log ( str ( iIiIi11 ) )
  I11iiI = IIi1i1 ( i1ioO , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  O00oOoo0OoO0 = IIi1i1 ( i1ioO , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  O0O0ooOOO = IIi1i1 ( i1ioO , '<description>' , '</description>' )
  O0O0ooOOO = base64 . b64decode ( O0O0ooOOO )
  ooOO0 = '('
  Oo00Oo = ')'
  I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , O00oOoo0OoO0 , 222 , I11iiI , oOOo0O00o , ( '[COLOR' + ooOoOoo0O + ']' + O0O0ooOOO + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( Oo00Oo , '[COLORsteelblue]' ) . replace ( ooOO0 , '[COLORorangered]' ) )
  if 25 - 25: iI11I1II1I1I
def o0o0O0oOOOooo ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( IiiI111I11 + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , type , oo0O0oO0O0O , iii1 in IIi :
  oOo0O = ( O0oo + oo0O0oO0O0O + '.m3u8' ) . strip ( )
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , oOo0O , 222 , ( iii1 ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  O0oO0 ( 'tvshows' , 'Media Info 3' )
def Ii1iiI1i1 ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for Ooo0 , iIi in IIi :
  if name == Ooo0 :
   I1I1i1I ( ( '' + name + '' ) . replace ( '_' , ' ' ) + iIi , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   I1I1i1I ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def o0oooo0OOo00 ( name ) :
 OOO0 = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , o00oOOooOOo0o , iI in IIi :
  iI = ( iI ) . replace ( '.ts' , '.m3u8' )
  I1I1i1I ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iI ) . strip ( ) , 222 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
 else :
  I1I1i1I ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 16 - 16: IiI1i11I / iI11I1II1I1I + oooOo0oo0oo * IiI1i11I * Iii
  if 8 - 8: i1IiiiI1iI
  if 15 - 15: I1ii11iIi11i / o0ii1I % o0o00Oo0O + Ii1I
  if 96 - 96: i1iIi . ii
  if 39 - 39: oooOo0oo0oo + oO0o
  if 80 - 80: oooOo0oo0oo % oO0o / OOooOOo
  if 54 - 54: I1ii11iIi11i % oO0o - oooOo0oo0oo - Iii
  if 71 - 71: i1iIi . Ii
  if 56 - 56: o0o00Oo0O * IiI1i11I + IiI1i11I * iI11I1II1I1I / i1iIi * i1IiiiI1iI
  if 25 - 25: iI11I1II1I1I . Iii * Ii + I1ii11iIi11i * Iii
  if 67 - 67: IiI1i11I
  if 88 - 88: I1ii11iIi11i
def iiIiii1iI1i ( ) :
 Iii1I1I11iiI1 ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  Iii1I1I11iiI1 ( 'Backup Genie Favourites' , iI , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  Iii1I1I11iiI1 ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  Iii1I1I11iiI1 ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 8 - 8: Ii1I
  if 82 - 82: ii
  if 75 - 75: IIiIiII11i % oOo0O0Ooo + oooOo0oo0oo % ii / III1iiIii
zip = oo00 . getSetting ( 'zip' )
Ii111I11 = xbmc . translatePath ( os . path . join ( zip ) )
def Oo0O0oo ( ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 62 - 62: Iii / Ii1I
  if 85 - 85: oOo0O0Ooo + IiI1i11I - IiI1i11I . ii - iI11I1II1I1I
  if 8 - 8: Ii * I11i / Ii1I . o0ii1I
def Iii1II1ii ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  Oo0O0oo ( )
  ooOo00 = open ( url ) . read ( )
  OO0III = os . path . join ( Ii111I11 , description . split ( 'Your ' ) [ 1 ] )
  ooOoO00 = open ( OO0III , mode = 'w' )
  ooOoO00 . write ( ooOo00 )
  ooOoO00 . close ( )
 else :
  if 'guisettings.xml' in description :
   i1ioO = open ( os . path . join ( Ii111I11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooOOo = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( ooOOo ) . findall ( i1ioO )
   for type , OoO0o , OO0o0O0O0O0 in IIi :
    OO0o0O0O0O0 = OO0o0O0O0O0 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , OoO0o , OO0o0O0O0O0 ) )
  else :
   OO0III = os . path . join ( url )
   ooOo00 = open ( os . path . join ( Ii111I11 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooOoO00 = open ( OO0III , mode = 'w' )
   ooOoO00 . write ( ooOo00 )
   ooOoO00 . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 34 - 34: oO0o * o0ii1I * I1ii11iIi11i
 if 21 - 21: ii . OOooOOo - iI11I1II1I1I % III1iiIii
 if 55 - 55: o0o00Oo0O % oOo0O0Ooo . ii * I1ii11iIi11i / ii . o0ii1I
 if 26 - 26: III1iiIii / iI11I1II1I1I - iI11I1II1I1I
def oO00oO00O0Oo ( ) :
 OO0o0o0oo = 1
 Oo0O0oo ( )
 iIiII1 = xbmc . translatePath ( os . path . join ( Ii111I11 , 'Build Backup' , 'Full Backup' , '' ) )
 i111iii1I1 = xbmc . translatePath ( os . path . join ( Ii111I11 , 'Build Backup' , 'my_full_backup.zip' ) )
 iiIiII1 = xbmc . translatePath ( os . path . join ( Ii111I11 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iIiII1 ) :
  os . makedirs ( iIiII1 )
 ii111iI = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not ii111iI ) : return False , 0
 ii11I1 = ii111iI
 I1IoOO0o0 = xbmc . translatePath ( os . path . join ( iIiII1 , ii11I1 + '.zip' ) )
 Ii1Ii1 = [ 'plugin.video.GenieTv' ]
 o000ooOo0o0OO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 iiI1ii1IIiI = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 IIi1i1I11IIII = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OooOoOOO00O = "Creating full backup of existing build"
 I111iIIII11iI = "Creating Community Build"
 oOoOO = "Archiving..."
 i11I1iIii1i11 = ""
 iIiiI11II11i = "Please Wait"
 o00OoO0o0 ( oOo0oooo00o , I1IoOO0o0 , I111iIIII11iI , oOoOO , i11I1iIii1i11 , iIiiI11II11i , iiI1ii1IIiI , IIi1i1I11IIII )
 time . sleep ( 1 )
 o0OOOoO0ooOOOo0 = xbmc . translatePath ( os . path . join ( iIiII1 , ii11I1 + '_guisettings.zip' ) )
 o0oOOO = zipfile . ZipFile ( o0OOOoO0ooOOOo0 , mode = 'w' )
 try :
  o0oOOO . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 o0oOOO . close ( )
 if OO0o0o0oo == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + i111iii1I1 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + I1IoOO0o0 + '[/COLOR]' )
  if 24 - 24: I11i / o0ii1I / o0ii1I % IIiIiII11i - i1i1I1IIii1II * i1i1I1IIii1II
def o00OoO0o0 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 oOoo0oO = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 IIii1i = len ( sourcefile )
 o00oo = [ ]
 Ii11IIIi1 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for ooooooo00oO0OO , IIIii11 , i1i11I1I1 in os . walk ( sourcefile ) :
  for file in i1i11I1I1 :
   Ii11IIIi1 . append ( file )
 OOOOOoooO = len ( Ii11IIIi1 )
 for ooooooo00oO0OO , IIIii11 , i1i11I1I1 in os . walk ( sourcefile ) :
  IIIii11 [ : ] = [ oO0Oooo0OoO for oO0Oooo0OoO in IIIii11 if oO0Oooo0OoO not in exclude_dirs ]
  i1i11I1I1 [ : ] = [ ooOoO00 for ooOoO00 in i1i11I1I1 if ooOoO00 not in exclude_files ]
  for file in i1i11I1I1 :
   o00oo . append ( file )
   Iiii1IIIIiiI11 = len ( o00oo ) / float ( OOOOOoooO ) * 100
   o0oOoO00o . update ( int ( Iiii1IIIIiiI11 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   I1iii1I = os . path . join ( ooooooo00oO0OO , file )
   if not 'temp' in IIIii11 :
    if not 'plugin.program.originwizard' in IIIii11 :
     import time
     oooII111 = '01/01/1980'
     I11iIi = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( I1iii1I ) ) )
     if I11iIi > oooII111 :
      oOoo0oO . write ( I1iii1I , I1iii1I [ IIii1i : ] )
 oOoo0oO . close ( )
 o0oOoO00o . close ( )
 if 10 - 10: IIiIiII11i % oO0o % oOo0O0Ooo - I1ii11iIi11i - oooOo0oo0oo
 if 46 - 46: iI11I1II1I1I * i1i1I1IIii1II + Ii . iI11I1II1I1I . oooOo0oo0oo / oO0o
def iI1111i1i1ii ( ) :
 iii ( )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 62 - 62: ii / OOooOOo . III1iiIii . III1iiIii % i1iIi
 if 42 - 42: I11i . oooOo0oo0oo - i1iIi
def Iiii ( ) :
 iii ( )
 oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , oOI1Ii1I1 )
 if IiII111iI1ii1 == 0 :
  I1IiiI1ii1i ( )
 if IiII111iI1ii1 == 1 :
  O0OoO0ooOO0o ( )
 if IiII111iI1ii1 == 2 :
  iiIII1II ( )
 if IiII111iI1ii1 == 3 :
  Oooo00 ( )
  if 56 - 56: Iii - o0o00Oo0O / o0o00Oo0O * ooOoO0O00 . ii % iI11I1II1I1I
  if 21 - 21: III1iiIii - oOo0O0Ooo % ii + I11i
  if 92 - 92: i1iIi + III1iiIii
  if 52 - 52: IIiIiII11i / oOo0O0Ooo . i1i1I1IIii1II * III1iiIii . Iii
  if 25 - 25: Ii / OOooOOo - i1IiiiI1iI / oO0o . I11i . I11i
  if 6 - 6: i1i1I1IIii1II . Iii
  if 43 - 43: Ii1I + I11i
  if 50 - 50: i1i1I1IIii1II % ooOoO0O00 * o0o00Oo0O
  if 4 - 4: iI11I1II1I1I . ooOoO0O00
def Oo00oo ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OOo00OoO ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if IiII111iI1ii1 == 1 :
   OOo00OoO ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if IiII111iI1ii1 == 2 :
   oO0oO ( )
  if IiII111iI1ii1 == 3 :
   o0ooo ( )
  if IiII111iI1ii1 == 4 :
   IiIii11I ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if IiII111iI1ii1 == 5 :
   Ooo0O00 ( )
  if IiII111iI1ii1 == 6 :
   oooo0oOOoO000 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if IiII111iI1ii1 == 7 :
   Oo00o00Oo ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if IiII111iI1ii1 == 8 :
   i1I1i1I111 ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if IiII111iI1ii1 == 9 :
   oOo00OO0ooOOO ( )
  if IiII111iI1ii1 == 10 :
   i1i1I1Ii1IIii ( )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 90037 , iiIi1IIiIi + 'Rays-Ravers.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 90037 , iiIi1IIiIi + 'Quicksilver.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '' , 70001 , iiIi1IIiIi + 'RadioNomy.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , str ( oO0000OOo00 ) , 30031 , iiIi1IIiIi + 'MusicChannels.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , iiIi1IIiIi + 'UKRadio.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , str ( oO0000OOo00 ) , 1013 , iiIi1IIiIi + 'WorldRadio.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , iiIi1IIiIi + 'Concerts.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) , 1030 , iiIi1IIiIi + 'MUSIC.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , iiIi1IIiIi + 'MusicVideos.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , str ( oO0000OOo00 ) , 1111 , iiIi1IIiIi + 'MusicSearch.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , iiIi1IIiIi + 'KodibleAudioBooks.png' , Oo00OOOOO , '' )
  if 80 - 80: Ii
 O0oO0 ( 'movies' , 'MAIN' )
 if 29 - 29: oOo0O0Ooo . oooOo0oo0oo + IIiIiII11i . I1ii11iIi11i
def I1iii1iIi ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   i1II1i ( )
  if IiII111iI1ii1 == 1 :
   o0OO0 ( )
  if IiII111iI1ii1 == 2 :
   iIIii ( )
  if IiII111iI1ii1 == 3 :
   iI1iI ( iI )
  if IiII111iI1ii1 == 4 :
   oOo ( iI )
  if IiII111iI1ii1 == 5 :
   ooI1111i ( )
  if IiII111iI1ii1 == 6 :
   III1IiIi1 ( url = 'http://www.iplocation.net/' , inc = 1 )
  if IiII111iI1ii1 == 7 :
   oOOoO0O ( )
 else :
  I1I1i1I ( 'CLLEANUP' , 'url' , 9666 , iiIi1IIiIi + 'MAIN5.png' , Oo00OOOOO , '' )
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '' , 80000 , iiIi1IIiIi + 'KillKodi.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '' , 50004 , iiIi1IIiIi + 'Speedtest.png' , Oo00OOOOO , '' )
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , iiIi1IIiIi + 'View-Log-File.png' , Oo00OOOOO , '' )
  I1I1i1I ( 'DELETE CACHE' , 'url' , 14 , iiIi1IIiIi + 'DeleteCache.png' , Oo00OOOOO , '' )
  I1I1i1I ( 'DELETE PACKAGES' , 'url' , 6 , iiIi1IIiIi + 'DeletePackages.png' , Oo00OOOOO , '' )
  I1I1i1I ( 'FORCE REFRESH' , 'url' , 10 , iiIi1IIiIi + 'ForceRefresh.png' , Oo00OOOOO , 'Force Refresh All Repos' )
  Iii1I1I11iiI1 ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , iiIi1IIiIi + '1.jpg' , Oo00OOOOO , 'Fix Corrupt Database' )
  I1I1i1I ( 'CHECK MY IP' , 'url' , 12 , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
  I1I1i1I ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , iiIi1IIiIi + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Oo00OOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 76 - 76: ooOoO0O00 / iI11I1II1I1I - Ii1I - IIiIiII11i
  if 76 - 76: Ii + III1iiIii % OOooOOo
 O0oO0 ( 'movies' , 'MAIN' )
 if 6 - 6: IiI1i11I
 if 65 - 65: IIiIiII11i . oOo0O0Ooo + o0o00Oo0O
def i1i1II ( ) :
 iii ( )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , iiIi1IIiIi + 'repos.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEW[/COLOR]' , str ( oO0000OOo00 ) , 22 , iiIi1IIiIi + 'NEW.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']IPTV[/COLOR]' , str ( oO0000OOo00 ) , 23 , iiIi1IIiIi + 'IPTV.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']VIDEO[/COLOR]' , str ( oO0000OOo00 ) , 24 , iiIi1IIiIi + 'VIDEO.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SPORTS[/COLOR]' , str ( oO0000OOo00 ) , 25 , iiIi1IIiIi + 'SPORTS.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , str ( oO0000OOo00 ) , 26 , iiIi1IIiIi + 'KIDS.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , str ( oO0000OOo00 ) , 27 , iiIi1IIiIi + 'MUSIC.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']PROGRAMS[/COLOR]' , str ( oO0000OOo00 ) , 28 , iiIi1IIiIi + 'PROGRAMS.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']XXX[/COLOR]' , 'URL' , 29 , iiIi1IIiIi + 'XXX.png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 75 - 75: o0o00Oo0O % iI11I1II1I1I / OOooOOo % oooOo0oo0oo / III1iiIii
 if 31 - 31: Ii * OOooOOo
def oOiI1I ( ) :
 iii ( )
 I1I1i1I ( 'CHECK ADVANCED XML' , str ( oO0000OOo00 ) , 8 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 I1I1i1I ( 'MUCKYS XML' , str ( oO0000OOo00 ) + '/wizard/muckys.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 I1I1i1I ( '0CACHE XML' , str ( oO0000OOo00 ) + '/wizard/0cache.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 I1I1i1I ( 'MIKEY1234 XML' , str ( oO0000OOo00 ) + '/wizard/mikey.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 I1I1i1I ( 'TUXENS XML' , str ( oO0000OOo00 ) + '/wizard/tuxens.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 I1I1i1I ( 'P2P RECOMMENDED XML1' , str ( oO0000OOo00 ) + '/wizard/p2p1.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 I1I1i1I ( 'P2P RECOMMENDED XML2' , str ( oO0000OOo00 ) + '/wizard/p2p2.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 I1I1i1I ( 'DELETE XML' , str ( oO0000OOo00 ) , 11 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 6 - 6: oO0o
def I1ii1ii11i1I ( ) :
 iii ( )
 I1I1i1I ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 I1I1i1I ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 99 - 99: I11i * oooOo0oo0oo % i1i1I1IIii1II * i1i1I1IIii1II + ii
def O0OO ( ) :
 iii ( )
 I1I1i1I ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 I1I1i1I ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 I1I1i1I ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 I1I1i1I ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 30 - 30: OOooOOo * I1ii11iIi11i % iI11I1II1I1I % oO0o + Ii
 if 46 - 46: oOo0O0Ooo . III1iiIii - Ii - i1IiiiI1iI
 if 97 - 97: IIiIiII11i % I1ii11iIi11i * III1iiIii
def oOoOO0O00o ( ) :
 iii ( )
 oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOI1Ii1I1 )
 if IiII111iI1ii1 == 0 :
  o0OOOO ( )
 if IiII111iI1ii1 == 0 :
  OOoo0OOOo0o ( iI )
 if IiII111iI1ii1 == 0 :
  iI1111i1i11Ii ( iI )
  if 62 - 62: IiI1i11I
  if 8 - 8: IiI1i11I - oOo0O0Ooo * I1ii11iIi11i % Ii1I * ii
  if 26 - 26: ooOoO0O00 / IiI1i11I . IiI1i11I
 O0oO0 ( 'movies' , 'MAIN' )
 if 20 - 20: oooOo0oo0oo - IiI1i11I / I1ii11iIi11i * oO0o
def o00OIIIIIiiI ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for o00oOOooOOo0o , iIiIi11 in IIi :
  I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , o00oOOooOOo0o , o00oOOooOOo0o , '' )
 O0oO0 ( 'tvshows' , 'INFO' )
 if 38 - 38: o0o00Oo0O
def ooO ( url ) :
 iiI111I1iIiI = OooOoooOo ( i1i1i11iI11II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 5 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 6 - 6: OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / o0ii1I
def o0OOOO ( ) :
 iii ( )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 14 - 14: i1IiiiI1iI % III1iiIii - o0o00Oo0O / i1IiiiI1iI
def Oo00OOoO0oo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IIi11ii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 54 - 54: Iii % o0o00Oo0O - oooOo0oo0oo % oO0o + oO0o . III1iiIii
def oOoo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o00O0o00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 19 - 19: oOo0O0Ooo
def oOOoo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1I1i11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 79 - 79: I11i - IIiIiII11i
def O0Ooo0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 75 - 75: IiI1i11I + iI11I1II1I1I
def OOoo0OOOo0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOoOooO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 40 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 28 - 28: III1iiIii + Ii + ii / oO0o
def iIiI1111 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + O0OO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 5 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 6 - 6: I1ii11iIi11i
def iI11I1II ( ) :
 oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , oOI1Ii1I1 )
 if IiII111iI1ii1 == 0 :
  O0OOOOoO00oo ( )
 if IiII111iI1ii1 == 1 :
  OoOiII11IiIi ( )
 if IiII111iI1ii1 == 2 :
  iII1I1i ( )
  if 6 - 6: i1i1I1IIii1II / o0o00Oo0O / o0ii1I / III1iiIii / i1i1I1IIii1II . iI11I1II1I1I
  if 62 - 62: iI11I1II1I1I
  if 4 - 4: Ii1I * Iii . Iii . IIiIiII11i / oooOo0oo0oo
  if 86 - 86: i1i1I1IIii1II % o0o00Oo0O + oO0o
def OoOiII11IiIi ( ) :
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OOo0 )
 for iI , oO0OO in IIi :
  iIiiiii1i ( 'Android Apps' + oO0OO , 'https://www.apkfiles.com' + iI , 30035 , iiIi1IIiIi + 'apps.png' )
 for iI , oO0OO in i1Iii1i1I :
  iIiiiii1i ( 'Android Games' + oO0OO , 'https://www.apkfiles.com' + iI , 30035 , iiIi1IIiIi + 'GAMES.png' )
 O0oO0 ( 'movies' , 'MAIN' )
def o0OOO ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  if '/cat' in url :
   iIiiiii1i ( ( iIiIi11 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def Iii11iI1I ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  if '/app' in url :
   iIiiiii1i ( ( iIiIi11 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def OOo0o0O0 ( url ) :
 OOo0 = OooOoooOo ( url )
 O00oOoo0OoO0 = url
 if "page=" in str ( url ) :
  O00oOoo0OoO0 = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OOo0 )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  if 'apk' in url :
   I1I1i1I ( ( iIiIi11 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + o00oOOooOOo0o )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 I1I1i1I ( 'Next Page' , O00oOoo0OoO0 + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def iiIIII11IiIII ( name , url ) :
 OOo0 = o0O0Oo00 ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( OOo0 )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  Iii1I ( name , url , 'Brackets' )
def iII1I1i ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO00O = 'https://www.apkfiles.com/search?q=' + ( Ii11 ) . replace ( ' ' , '+' ) + '&search_type=1'
 II1i111 = oO00O . lower ( )
 OOo0o0O0 ( II1i111 )
 if 46 - 46: ooOoO0O00 . III1iiIii % I1ii11iIi11i + i1IiiiI1iI - oooOo0oo0oo
def oO0oO0O ( url ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( ooooO , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , iIiIi11 + '.apk' )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( url , IiIi11iI , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 99 - 99: o0ii1I - III1iiIii * iI11I1II1I1I . IIiIiII11i
def OooO00o000 ( url ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , iIiIi11 + '.mp4' )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( url , IiIi11iI , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 36 - 36: Iii - III1iiIii . III1iiIii
 if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
def ooo000o ( name , url , description ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , name )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( url , IiIi11iI , o0oOoO00o )
 OOOOOO = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print OOOOOO
 print '======================================='
 extract . all ( IiIi11iI , OOOOOO , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 95 - 95: IIiIiII11i
 if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
 if 15 - 15: i1iIi % I11i / i1i1I1IIii1II - IIiIiII11i . iI11I1II1I1I
 if 28 - 28: IIiIiII11i * i1iIi * o0ii1I
 if 93 - 93: ooOoO0O00 . o0ii1I * i1IiiiI1iI . i1iIi
def O0OOOOoO00oo ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , iI , iii1 , oOOo0O00o , O0iI1I1ii11IIi1 in IIi :
  I1I1i1I ( iIiIi11 , iI , 80003 , iii1 , iiIi1IIiIi + 'APKToolsB.png' , O0iI1I1ii11IIi1 )
def OOoOOoOO ( apk , ret = None ) :
 if apk == "kodi" :
  O0O00 = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( O0O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   I1iIiiI11 = IIi [ 0 ] [ 0 ]
   ii11I1 = IIi [ 0 ] [ 1 ]
   i1ii1111iiI = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( I1iIiiI11 , ii11I1 )
  if ret == 'version' : return I1iIiiI11
  else : return i1ii1111iiI
 elif apk == "spmc" :
  iiIIIII = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( iiIIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  I1iIiiI11 = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  i1ii1111iiI = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( I1iIiiI11 , I1iIiiI11 )
  if ret == 'version' : return I1iIiiI11
  else : return i1ii1111iiI
def Iii1I ( name , url , Brackets ) :
 if ii1I ( ) == 'android' :
  iiI1 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not iiI1 : iii11i1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  IIiI1I1IIiiI1 = name
  if iiI1 :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not OOooo0O0o0 ( url ) == True : iii11i1 ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % IIiI1I1IIiiI1 , '' , 'Please Wait' )
   IiIi11iI = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( IiIi11iI )
   except : pass
   downloader . download ( url , IiIi11iI , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    o0oOOO = zipfile . ZipFile ( IiIi11iI )
    for file in o0oOOO . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as ooOoO00 :
       oooOOO0o0O0 = file . split ( '/' ) [ 1 ]
       ooOoO00 . write ( o0oOOO . read ( file ) )
       xbmc . sleep ( 500 )
       ooOoO00 . close ( )
       try :
        os . remove ( IiIi11iI )
       except :
        pass
       IiIi11iI = os . path . join ( i1iIIi1 , oooOOO0o0O0 )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + IiIi11iI + '")' )
  else : iii11i1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iii11i1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 31 - 31: ii - i1i1I1IIii1II / i1IiiiI1iI
 if 62 - 62: Ii - Iii
 if 81 - 81: Iii
 if 92 - 92: oooOo0oo0oo - I1ii11iIi11i - ii / III1iiIii - ooOoO0O00
def Oo00o ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for iI , iIiIi11 in IIi :
  iI = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + iI )
  III ( ( iIiIi11 ) . replace ( '_' , ' ' ) , iI )
  if 16 - 16: o0ii1I / ooOoO0O00
def III ( name , url ) :
 if ii1I ( ) == 'android' :
  iiI1 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not iiI1 : iii11i1 ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  IIiI1I1IIiiI1 = name
  if iiI1 :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not OOooo0O0o0 ( url ) == True : iii11i1 ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % IIiI1I1IIiiI1 , '' , 'Please Wait' )
   IiIi11iI = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( IiIi11iI )
   except : pass
   downloader . download ( url , IiIi11iI , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + IiIi11iI + '")' )
  else : iii11i1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iii11i1 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 28 - 28: o0ii1I
 if 66 - 66: Iii
def i1o0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 5 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'INFO' )
 if 61 - 61: Iii
 if 80 - 80: oOo0O0Ooo - oOo0O0Ooo
def oOoO00o ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 30015 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 52 - 52: IIiIiII11i
def iIii1II1I ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 I1IiiIiii1 = url
 o00oOOooOOo0o = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for oo0O0oO0O0O , iIiIi11 in IIi :
  if '.mp4' in iIiIi11 :
   I1I1i1I ( 'Watch VIDEO' , url + '/' + oo0O0oO0O0O , 222 , o00oOOooOOo0o , fanart , '' )
  if 'description' in iIiIi11 :
   I1I1i1I ( 'Read Description' , url + '/' + oo0O0oO0O0O , 30017 , o00oOOooOOo0o , fanart , '' )
  if 'images' in iIiIi11 :
   Iii1I1I11iiI1 ( 'View Images' , url + '/' + oo0O0oO0O0O , 30018 , o00oOOooOOo0o , fanart , '' )
  if 'url' in iIiIi11 :
   I1I1i1I ( 'Install Build On Android' , url + '/' + oo0O0oO0O0O , 30016 , o00oOOooOOo0o , fanart , '' )
  if 'url' in iIiIi11 :
   I1I1i1I ( 'Install Build On Pc' , url + '/' + oo0O0oO0O0O , 30019 , o00oOOooOOo0o , fanart , '' )
 O0oO0 ( 'movies' , 'INFO' )
 if 25 - 25: OOooOOo
def iii1IiII ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  o0oo0OooOO0 ( url )
  if 57 - 57: IIiIiII11i % oOo0O0Ooo
def iIIi1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  OoOo0O00 ( url )
  if 9 - 9: oooOo0oo0oo
def I1iII ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for Ooo00O0 in IIi :
  IiII111i1i11 ( 'Description:' , Ooo00O0 )
  if 18 - 18: Iii + I1ii11iIi11i - oO0o / i1IiiiI1iI / oooOo0oo0oo
def OOoOoO ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for oo0O0oO0O0O , iIiIi11 in IIi :
  if 'png' in iIiIi11 :
   I1I1i1I ( 'image' , '' , '' , url + '/' + oo0O0oO0O0O , url + '/' + oo0O0oO0O0O , '' )
 O0oO0 ( 'movies' , 'MAIN' )
 if 72 - 72: OOooOOo / i1IiiiI1iI * III1iiIii % iI11I1II1I1I
def OOiii1IiiIiIIiI ( name , url , description ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , name + '.zip' )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( url , IiIi11iI , o0oOoO00o )
 Oo0O00O000 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Oo0O00O000
 print '======================================='
 extract . all ( IiIi11iI , Oo0O00O000 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 ooI1111i ( )
 if 93 - 93: III1iiIii % Ii1I
 if 31 - 31: IIiIiII11i + oooOo0oo0oo - ii . Iii
def OoOo0O00 ( url ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( url , IiIi11iI , o0oOoO00o )
 Oo0O00O000 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Oo0O00O000
 print '======================================='
 extract . all ( IiIi11iI , Oo0O00O000 , o0oOoO00o )
 i11I1IiII1i1i ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 i1II1i ( )
 if 28 - 28: o0ii1I . Ii1I
def o0oo0OooOO0 ( url ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( url , IiIi11iI , o0oOoO00o )
 Oo0O00O000 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Oo0O00O000
 print '======================================='
 extract . all ( IiIi11iI , Oo0O00O000 , o0oOoO00o )
 i11I1IiII1i1i ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 i1II1i ( )
 if 77 - 77: Ii1I % IIiIiII11i
def OOo00o0oo0 ( name , url , description ) :
 Oo0O00O000 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 IiIi11iI = os . path . join ( O0OoO000O0OO )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print Oo0O00O000
 print '======================================='
 extract . all ( IiIi11iI , Oo0O00O000 , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 i1II1i ( )
 if 33 - 33: I11i . oooOo0oo0oo + I11i / Ii1I . I1ii11iIi11i + OOooOOo
def ii1I ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def o00O0O ( log ) :
 xbmc . log ( "[%s]: %s" % ( i1iiIIiiI111 , log ) )
 if not os . path . exists ( oo0o0O00 ) : os . makedirs ( oo0o0O00 )
 if not os . path . exists ( oO ) : ooOoO00 = open ( oO , 'w' ) ; ooOoO00 . close ( )
 with open ( oO , 'a' ) as ooOoO00 :
  I1111111 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  ooOoO00 . write ( I1111111 . rstrip ( '\r\n' ) + '\n' )
def i1II1i ( ) :
 IiII111iI1ii1 = iIii1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if IiII111iI1ii1 == 0 : return
 elif IiII111iI1ii1 == 1 : pass
 IIIii1I = ii1I ( )
 o00O0O ( "Platform: " + str ( IIIii1I ) )
 os . _exit ( 1 )
 o00O0O ( "Force close failed!  Trying alternate methods." )
 if IIIii1I == 'osx' :
  o00O0O ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IIIii1I == 'linux' :
  o00O0O ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif IIIii1I == 'android' :
  o00O0O ( "############ try android force close #################" )
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
 elif IIIii1I == 'windows' :
  o00O0O ( "############ try windows force close #################" )
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
  o00O0O ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  o00O0O ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 57 - 57: oooOo0oo0oo % oO0o - oOo0O0Ooo
  if 3 - 3: oooOo0oo0oo + ooOoO0O00 % Ii1I
  if 100 - 100: ii + Ii % I11i + oOo0O0Ooo . I1ii11iIi11i . IIiIiII11i
def iI1111i1i11Ii ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OoiiI11111II , IIIii11 , i1i11I1I1 in os . walk ( url ) :
  for file in i1i11I1I1 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    i1ioO = open ( ( os . path . join ( OoiiI11111II , file ) ) ) . read ( )
    I1ii1i11iI1 = i1ioO . replace ( oOo0oooo00o , 'special://home/' )
    ooOoO00 = open ( ( os . path . join ( OoiiI11111II , file ) ) , mode = 'w' )
    ooOoO00 . write ( str ( I1ii1i11iI1 ) )
    ooOoO00 . close ( )
 i1II1i ( )
 if 6 - 6: o0o00Oo0O . i1iIi - i1i1I1IIii1II / Ii
def oO0oO ( ) :
 iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 84 - 84: Iii / Ii1I * I11i * oO0o * oooOo0oo0oo * o0o00Oo0O
def OoOooOo00o ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def iI1IIi ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def II11 ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OOo0 )
 for url , iIiIi11 in i1Iii1i1I :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + iIiIi11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + iIiIi11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , o00oOOooOOo0o )
def oo0o0O ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( OOo0 )
 for url in IIi :
  OooO0OO ( url )
def ooo0ooooo0o ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11
 IIIIIIi1IIi1I11i = 'https://www.radionomy.com/en/search/index?query=' + ( Ii11 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( IIIIIIi1IIi1I11i )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , o00oOOooOOo0o , iIiIi11 in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + iIiIi11 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + iI , 70005 , o00oOOooOOo0o )
  if 70 - 70: o0ii1I % o0ii1I . OOooOOo / Ii
  if 12 - 12: iI11I1II1I1I / I1ii11iIi11i - Ii1I + Ii
def Ooo0O00 ( ) :
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , 'http://www.listenlive.eu/' + iI , 10111113 , iiIi1IIiIi + 'radio.png' )
def IiIii11I ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  iiIi1IIiI ( iIiIi11 , url , 222 , iiIi1IIiIi + 'radio.png' )
  if 71 - 71: Ii * oOo0O0Ooo + iI11I1II1I1I - i1IiiiI1iI
def ii1Io0oOO0 ( ) :
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.toonjet.com/' + iI , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I11II11IiI11 ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( OOo0 )
 for url , o00oOOooOOo0o in IIi :
  if 'ol.gif' in o00oOOooOOo0o :
   pass
  elif 'link_block_' in o00oOOooOOo0o :
   pass
  elif '.png' in o00oOOooOOo0o :
   pass
  else :
   iIiiiii1i ( ( o00oOOooOOo0o ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  iIiiiii1i ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00o ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OOo0 )
 for url in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 34 - 34: oOo0O0Ooo * IiI1i11I % ii + iI11I1II1I1I . oOo0O0Ooo * o0o00Oo0O
  if 24 - 24: ooOoO0O00 . oooOo0oo0oo
def i1i1I1Ii1IIii ( ) :
 IiIIii1iiI ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 IiIIii1iiI ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 85 - 85: oOo0O0Ooo + oooOo0oo0oo + oooOo0oo0oo
def O00oo0o0000 ( ) :
 IiIIii1iiI ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 IiIIii1iiI ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 IiIIii1iiI ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
def OO0O00 ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , iI , ooOO in IIi :
  if 'Parent' in iIiIi11 :
   pass
  elif '2' in ooOO :
   IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 66 - 66: I1ii11iIi11i / Ii % i1iIi
def i1Ii1i11ii ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , iI , ooOO in IIi :
  if Ii11 in iIiIi11 . lower ( ) :
   if '1' in ooOO :
    IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in ooOO :
    IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in ooOO :
    IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 58 - 58: OOooOOo + oO0o * o0ii1I
    if 31 - 31: i1i1I1IIii1II - IiI1i11I
def iIII11I ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , iI , ooOO in IIi :
  if '1' in ooOO :
   IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in ooOO :
   IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in ooOO :
   IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iI , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 39 - 39: oOo0O0Ooo . Ii1I * IiI1i11I / OOooOOo % Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: OOooOOo
def IiIi1IiIii ( url ) :
 oo0O0oO0O0O = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in i1Iii1i1I :
  if 'mp3' in iIiIi11 :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo0O0oO0O0O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iIiIi11 :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo0O0oO0O0O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iIiIi11 :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo0O0oO0O0O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in iIiIi11 :
   IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo0O0oO0O0O + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . Iii
   if 64 - 64: i1iIi / ooOoO0O00 % IiI1i11I
   if 84 - 84: OOooOOo - I1ii11iIi11i . i1iIi . III1iiIii - I1ii11iIi11i
def o0Oo0oO00Oooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oo0O0oO0O0O = url
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  if 'Parent' in iIiIi11 :
   pass
  elif '.db' in iIiIi11 :
   pass
  elif '.jpg' in iIiIi11 :
   pass
  elif '.html' in iIiIi11 :
   pass
  elif '.doc' in iIiIi11 :
   pass
  elif 'mp3' in iIiIi11 :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo0O0oO0O0O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iIiIi11 :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo0O0oO0O0O + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo0O0oO0O0O + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 31 - 31: ooOoO0O00 * I1ii11iIi11i % o0ii1I + oO0o
   if 75 - 75: oooOo0oo0oo / i1IiiiI1iI - IIiIiII11i % Ii + oO0o
def i1iiiiii1 ( ) :
 IiIIii1iiI ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 IiIIii1iiI ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 IiIIii1iiI ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 83 - 83: oOo0O0Ooo - i1IiiiI1iI + oOo0O0Ooo . oOo0O0Ooo
def ii11ii11II ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , o00oOOooOOo0o in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iI + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in o00oOOooOOo0o :
   pass
  else :
   IiIIii1iiI ( o00oOOooOOo0o , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iI ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + o00oOOooOOo0o + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: I1ii11iIi11i * IIiIiII11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: i1i1I1IIii1II . I1ii11iIi11i / i1iIi + i1iIi . Ii1I
 if 50 - 50: iI11I1II1I1I * i1i1I1IIii1II
def o0Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  if '</a>' in iIiIi11 :
   pass
  elif '(' in iIiIi11 :
   IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 16 - 16: oO0o % o0ii1I + Ii1I + I1ii11iIi11i / iI11I1II1I1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: oOo0O0Ooo % I1ii11iIi11i - OOooOOo * IiI1i11I + i1IiiiI1iI + ii
def IIi1II ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if Ii11 in iIiIi11 . lower ( ) :
   if '</a>' in iIiIi11 :
    pass
   elif '(' in iIiIi11 :
    IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 98 - 98: i1i1I1IIii1II - i1i1I1IIii1II . i1iIi
    if 60 - 60: oOo0O0Ooo * Ii1I / o0o00Oo0O + Iii + III1iiIii
def O0oO0o00oo0o ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if '</a>' in iIiIi11 :
   pass
  elif '(' in iIiIi11 :
   IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iI , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 47 - 47: i1iIi - o0ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: i1i1I1IIii1II . i1IiiiI1iI / OOooOOo . i1iIi
 if 1 - 1: oooOo0oo0oo
def OoOo0o0OOoO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  oo0O0oO0O0O = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( oo0O0oO0O0O )
  if 30 - 30: o0ii1I % Iii + I11i
def oooOoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url in IIi :
  if '<p align' in iIiIi11 :
   pass
  elif '&nbsp;' in iIiIi11 :
   pass
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 34 - 34: ooOoO0O00 % i1i1I1IIii1II . III1iiIii . ooOoO0O00 + IIiIiII11i / oO0o
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
 if 95 - 95: i1i1I1IIii1II
def oOo00oOOOOO ( ) :
 II11iIiIIIiI = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if 'ongoing' in iI :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 21005 , iiIi1IIiIi + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in iI :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 21005 , iiIi1IIiIi + 'CartoonShows.png' , '' , '' )
  if 'disney' in iI :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 21005 , iiIi1IIiIi + 'Disney.png' , '' , '' )
  if 'genre' in iI :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 21005 , iiIi1IIiIi + 'Genre.png' , '' , '' )
  if 'years' in iI :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 21005 , iiIi1IIiIi + 'Years.png' , '' , '' )
def i11ii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIiiiI1iI = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , o00oOOooOOo0o in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , o00oOOooOOo0o , o00oOOooOOo0o , iIiIi11 )
 for url , iIiIi11 in IIiiiI1iI :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def IiI111I ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I11I1IIiiII1 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oo0oO0ii1i1Iii = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 IIII11111Ii = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in oo0oO0ii1i1Iii :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , iIiIi11 in I11I1IIiiII1 :
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def IiiiII ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 75 - 75: o0o00Oo0O * ooOoO0O00 - Iii / oooOo0oo0oo % oooOo0oo0oo / OOooOOo
def iIiI ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if '9cart' in iI :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 5 - 5: o0o00Oo0O - IiI1i11I / i1IiiiI1iI . I11i
def iIII1iIii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1i11 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , iIiIi11 in I1i11 :
  if '9cart' in url :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 9 - 9: ooOoO0O00 - OOooOOo
def Oo00o0OOo0OO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , url , iIiIi11 in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 20003 , o00oOOooOOo0o )
 for url , iIiIi11 in i1Iii1i1I :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 18 - 18: i1iIi - III1iiIii / IIiIiII11i / Ii1I
def i1Ii1IiiIi1II ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   iIiiiii1i ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 54 - 54: o0ii1I % ooOoO0O00
def oooOOoo0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 79 - 79: ii - i1iIi * o0ii1I - IIiIiII11i % OOooOOo * III1iiIii
def iI1III ( url ) :
 url = cloudflare . source ( url )
 O0OOO00 ( url )
 if 42 - 42: i1iIi + IiI1i11I + o0ii1I * Iii . ooOoO0O00
def oo0oOo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  O0OOO00 ( url )
  if 22 - 22: iI11I1II1I1I * oOo0O0Ooo / Iii + OOooOOo
  if 98 - 98: oooOo0oo0oo
def OoOOo0O00 ( ) :
 if 69 - 69: IIiIiII11i + I1ii11iIi11i - i1i1I1IIii1II . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 75 - 75: oO0o % ii
def iiIII1II ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 16 - 16: o0o00Oo0O / ooOoO0O00
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 58 - 58: I11i / Ii / o0o00Oo0O % Iii % oOo0O0Ooo
 for iI , iIiIi11 in IIi :
  if Ii11 in iIiIi11 . lower ( ) :
   if 'Dad!' in iIiIi11 :
    pass
   elif 'Family Guy' in iIiIi11 :
    pass
   elif '2 Stupid' in iIiIi11 :
    pass
   elif 'The Zelfs' in iIiIi11 :
    pass
   elif 'A Clone' in iIiIi11 :
    pass
   elif 'A.T.O.M' in iIiIi11 :
    pass
   elif 'Almost Naked' in iIiIi11 :
    pass
   elif 'Angry Kid' in iIiIi11 :
    pass
   elif 'Annoying Orange' in iIiIi11 :
    pass
   elif 'Aqua Teen' in iIiIi11 :
    pass
   elif 'Assy Mcgee' in iIiIi11 :
    pass
   elif 'Astroblast' in iIiIi11 :
    pass
   elif 'Atomic Betty' in iIiIi11 :
    pass
   elif 'Axe Cop' in iIiIi11 :
    pass
   elif 'Baby Playpen' in iIiIi11 :
    pass
   elif 'Beavis and Butt' in iIiIi11 :
    pass
   elif 'Celebrity Deathmatch' in iIiIi11 :
    pass
   elif 'Clerks The' in iIiIi11 :
    pass
   elif 'Crapston Villas' in iIiIi11 :
    pass
   elif 'Duckman:' in iIiIi11 :
    pass
   elif 'Stripperella' in iIiIi11 :
    pass
   elif 'Vixen' in iIiIi11 :
    pass
   else :
    Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
    if 86 - 86: III1iiIii + OOooOOo / oOo0O0Ooo + Iii % Iii / Ii
    if 12 - 12: OOooOOo + I11i . i1IiiiI1iI
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 52 - 52: oO0o
def iIIIi1i1I11i ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  if 'Dad!' in iIiIi11 :
   pass
  elif 'Family Guy' in iIiIi11 :
   pass
  elif '2 Stupid' in iIiIi11 :
   pass
  elif 'The Zelfs' in iIiIi11 :
   pass
  elif 'A Clone' in iIiIi11 :
   pass
  elif 'A.T.O.M' in iIiIi11 :
   pass
  elif 'Almost Naked' in iIiIi11 :
   pass
  elif 'Angry Kid' in iIiIi11 :
   pass
  elif 'Annoying Orange' in iIiIi11 :
   pass
  elif 'Aqua Teen' in iIiIi11 :
   pass
  elif 'Assy Mcgee' in iIiIi11 :
   pass
  elif 'Astroblast' in iIiIi11 :
   pass
  elif 'Atomic Betty' in iIiIi11 :
   pass
  elif 'Axe Cop' in iIiIi11 :
   pass
  elif 'Baby Playpen' in iIiIi11 :
   pass
  elif 'Beavis and Butt' in iIiIi11 :
   pass
  elif 'Celebrity Deathmatch' in iIiIi11 :
   pass
  elif 'Clerks The' in iIiIi11 :
   pass
  elif 'Crapston Villas' in iIiIi11 :
   pass
  elif 'Duckman:' in iIiIi11 :
   pass
  elif 'Stripperella' in iIiIi11 :
   pass
  elif 'Vixen' in iIiIi11 :
   pass
  else :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: o0ii1I % Ii1I + Iii - Ii1I
def O00o0O00 ( url ) :
 OOo0 = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOo0 )
 for o00oOOooOOo0o in i1Iii1i1I :
  oO00OII11Ii = o00oOOooOOo0o
 I1i11 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OOo0 )
 for url in I1i11 :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 10007 , oO00OII11Ii )
  if 58 - 58: IiI1i11I
  if 2 - 2: IIiIiII11i + ooOoO0O00
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 68 - 68: oooOo0oo0oo + o0ii1I
def o0o0oooO00O0 ( url , IMAGE ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  print iIiIi11 + '     ' + url
  if 'easy' in url :
   iiiI ( url )
   if 28 - 28: I1ii11iIi11i / III1iiIii . IiI1i11I + oO0o + Iii % I1ii11iIi11i
   if 45 - 45: I1ii11iIi11i / o0o00Oo0O % ii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 92 - 92: o0ii1I . OOooOOo . Iii - ii / i1iIi
def iiiI ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( OOo0 )
 for url in IIi :
  OooO0OO ( url )
  if 80 - 80: iI11I1II1I1I / Ii + IiI1i11I
  if 41 - 41: i1IiiiI1iI + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
  if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
def Ii1 ( ) :
 if 77 - 77: IiI1i11I
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 87 - 87: oO0o + ii . i1iIi * Iii
def oooOoO0oo0o0 ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for iI , o00oOOooOOo0o , iIiIi11 in IIi :
  if 'elete' in iIiIi11 :
   pass
  else :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 222 , o00oOOooOOo0o )
   if 4 - 4: Ii * Ii1I + ii - III1iiIii . i1iIi . iI11I1II1I1I
def IIiIIiI1iIII ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0ooo0oooO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , ooOo , i1iII1IiiIiI1 in o0ooo0oooO :
  for Ii11 in ooOo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   OO00oOOO = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for iI , iIiIi11 in OO00oOOO :
    if 'tube' in iI :
     pass
    elif 'stage' in iI :
     iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + ooOo + '   -   ' + iIiIi11 + '[/COLOR]' , ( iI ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00oOOooOOo0o , )
    elif 'vee' in iI :
     pass
     if 94 - 94: i1IiiiI1iI
def iiii ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0ooo0oooO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , ooOo , i1iII1IiiIiI1 in o0ooo0oooO :
  OO00oOOO = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for iI , iIiIi11 in OO00oOOO :
   if 'tube' in iI :
    pass
   elif 'stage' in iI :
    iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + ooOo + '   -   ' + iIiIi11 + '[/COLOR]' , ( iI ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00oOOooOOo0o )
   elif 'vee' in iI :
    pass
    if 80 - 80: oOo0O0Ooo
    if 58 - 58: i1i1I1IIii1II + Ii1I % OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: iI11I1II1I1I - o0ii1I / oOo0O0Ooo * III1iiIii
def OOooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 O00O0OO00oo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( O00O0OO00oo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in O00O0OO00oo :
  iiiIi ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 26 - 26: I11i + oooOo0oo0oo - I11i + I1ii11iIi11i . i1i1I1IIii1II
  if 97 - 97: ooOoO0O00
  if 46 - 46: Ii1I
  if 30 - 30: oO0o / o0o00Oo0O * I11i * i1IiiiI1iI + ii * IiI1i11I
  if 23 - 23: Iii
  if 36 - 36: III1iiIii . IiI1i11I - ooOoO0O00 + i1IiiiI1iI
  if 54 - 54: ii . i1i1I1IIii1II - IiI1i11I
def O000OOO0OOo ( ) :
 if 76 - 76: i1IiiiI1iI
 O00o0 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 O00o0 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 98 - 98: iI11I1II1I1I + Ii * Ii1I / i1IiiiI1iI / i1iIi - o0o00Oo0O
 O0oO0 ( 'movies' , 'MAIN' )
 if 42 - 42: IiI1i11I
def Oo0OOo0o0o0o0 ( ) :
 O00o0 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 O00o0 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 95 - 95: oO0o
 O0oO0 ( 'movies' , 'MAIN' )
def OoiIIii1Ii1 ( ) :
 if 92 - 92: i1iIi / III1iiIii + iI11I1II1I1I
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 i1iii11 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 47 - 47: oooOo0oo0oo * o0ii1I % iI11I1II1I1I / i1iIi
 for i1iiiIii11 in i1iii11 :
  OOoOOO000O0 = oO0 + i1iiiIii11 + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( OOoOOO000O0 )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for iI , oo00O00oO000o , O0O0ooOOO , oOOo0O00o , iIiIi11 in IIi :
   if Ii11 in iIiIi11 . lower ( ) :
    O0O00O ( iIiIi11 , iI , 222 , oo00O00oO000o , oOOo0O00o , O0O0ooOOO )
    if 64 - 64: Iii / IIiIiII11i / oO0o - i1iIi * iI11I1II1I1I . IiI1i11I
    O0oO0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 25 - 25: oooOo0oo0oo - o0ii1I . Iii
    if 57 - 57: I11i + I1ii11iIi11i * Ii1I - i1iIi % iI11I1II1I1I - o0ii1I
def III1I11II11I ( ) :
 if 78 - 78: Ii1I . i1IiiiI1iI . i1IiiiI1iI . Iii % IiI1i11I
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 i1iii11 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 26 - 26: i1iIi + oO0o / OOooOOo . IIiIiII11i * o0ii1I
 for i1iiiIii11 in i1iii11 :
  IiII111I = oO0 + i1iiiIii11 + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( IiII111I )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIiIi11 , O0O0ooOOO , iI , o00oOOooOOo0o , oOOo0O00o , oO0oOOoo00000 in IIi :
   if Ii11 in iIiIi11 . lower ( ) :
    O00o0 ( iIiIi11 , iI , oO0oOOoo00000 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
    if 62 - 62: ooOoO0O00 * iI11I1II1I1I % i1i1I1IIii1II % OOooOOo / ii
    O0oO0 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 39 - 39: I1ii11iIi11i % IiI1i11I
    if 90 - 90: oOo0O0Ooo * Ii1I . Iii * o0ii1I - I11i
def IiI1iII1i111iI ( ) :
 if 9 - 9: Ii + oooOo0oo0oo - OOooOOo / i1iIi % ooOoO0O00 / i1i1I1IIii1II
 OOo0 = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , O0O0ooOOO , iI , o00oOOooOOo0o , oOOo0O00o , oO0oOOoo00000 in IIi :
  O00o0 ( iIiIi11 , iI , oO0oOOoo00000 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
  O0oO0 ( 'movies' , 'MAIN' )
def iiI1II1II111 ( url ) :
 if 71 - 71: IIiIiII11i % i1IiiiI1iI + oOo0O0Ooo * i1iIi + III1iiIii . i1iIi
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I11o0O00 = ( '%s%s' % ( OOOoOOO0oOOoO , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in IIi :
  oOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for iII1i11 in oOo0 :
   if iII1i11 == url :
    iIiIi11 = ( '[COLORred]Watched - [/COLOR]' + iIiIi11 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  O0O00O ( iIiIi11 , url , 222 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
  if 87 - 87: oooOo0oo0oo
  O0oO0 ( 'movies' , 'MAIN' )
  if 7 - 7: i1IiiiI1iI - Iii % Iii + i1iIi * ooOoO0O00
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 46 - 46: oOo0O0Ooo % III1iiIii - iI11I1II1I1I * I11i
  if 69 - 69: i1i1I1IIii1II . Iii
def iII11iI1iiIIi ( url ) :
 if 9 - 9: i1IiiiI1iI - oO0o + iI11I1II1I1I % o0o00Oo0O + Iii + III1iiIii
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , O0O0ooOOO , url , o00oOOooOOo0o , oOOo0O00o , oO0oOOoo00000 in IIi :
  O00o0 ( iIiIi11 , url , oO0oOOoo00000 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
  if 50 - 50: ooOoO0O00 + i1iIi
  O0oO0 ( 'movies' , 'MAIN' )
  if 64 - 64: I11i % i1i1I1IIii1II . i1iIi
  if 6 - 6: i1iIi / Ii - I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: III1iiIii - ii * ii - oOo0O0Ooo / i1IiiiI1iI * Ii1I
def O0O00O ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 58 - 58: III1iiIii % iI11I1II1I1I / Ii % I11i . i1IiiiI1iI * IiI1i11I
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIiiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iI111i1I1II = [ ]
  iI111i1I1II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iI111i1I1II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   iI111i1I1II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IIiiii . addContextMenuItems ( iI111i1I1II )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = False )
 return IIIII1iii
 if 32 - 32: ii + I11i
def O00o0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 91 - 91: i1iIi - i1IiiiI1iI * i1IiiiI1iI
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIiiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iI111i1I1II = [ ]
  iI111i1I1II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iI111i1I1II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   iI111i1I1II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IIiiii . addContextMenuItems ( iI111i1I1II )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = True )
 return IIIII1iii
if 55 - 55: iI11I1II1I1I + oOo0O0Ooo - I1ii11iIi11i
if 24 - 24: oO0o / i1IiiiI1iI + IiI1i11I * Iii * IiI1i11I
if 10 - 10: oOo0O0Ooo - Ii1I - I1ii11iIi11i - I11i
if 21 - 21: ii + i1IiiiI1iI
if 43 - 43: Ii . Ii1I . i1i1I1IIii1II
if 31 - 31: o0ii1I % I11i % i1IiiiI1iI . Ii1I / I11i * i1i1I1IIii1II
if 74 - 74: oOo0O0Ooo . i1iIi / IiI1i11I . III1iiIii
if 74 - 74: I1ii11iIi11i / i1IiiiI1iI % i1IiiiI1iI . III1iiIii
if 72 - 72: ooOoO0O00
if 21 - 21: i1IiiiI1iI . oooOo0oo0oo / Ii * ooOoO0O00
if 82 - 82: i1iIi * I1ii11iIi11i % Ii * ooOoO0O00 . oooOo0oo0oo
if 89 - 89: III1iiIii - ooOoO0O00 - III1iiIii
if 74 - 74: oO0o % oO0o
if 28 - 28: OOooOOo % i1i1I1IIii1II - oooOo0oo0oo + oooOo0oo0oo + i1i1I1IIii1II / iI11I1II1I1I
if 91 - 91: oOo0O0Ooo / IIiIiII11i * oooOo0oo0oo
def ooOoo000 ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 56 - 56: i1iIi . iI11I1II1I1I + ooOoO0O00
def o0oOOoOo00o ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 i1I11IiI = [ ]
 try :
  if 40 - 40: IIiIiII11i
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  ooOoo000 ( 'Making Favorites File' )
  i1I11IiI . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  i1ioO = open ( i1I1iI , "w" )
  i1ioO . write ( json . dumps ( i1I11IiI ) )
  i1ioO . close ( )
 else :
  ooOoo000 ( 'Appending Favorites' )
  i1ioO = open ( i1I1iI ) . read ( )
  iII1 = json . loads ( i1ioO )
  iII1 . append ( ( name , url , iconimage , fanart , mode ) )
  I1ii1i11iI1 = open ( i1I1iI , "w" )
  I1ii1i11iI1 . write ( json . dumps ( iII1 ) )
  I1ii1i11iI1 . close ( )
  if 7 - 7: Ii1I - iI11I1II1I1I
  if 97 - 97: oooOo0oo0oo
def Ii1IiiiII ( ) :
 if os . path . exists ( i1I1iI ) == False :
  i1I11IiI = [ ]
  ooOoo000 ( 'Making Favorites File' )
  i1I11IiI . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  i1ioO = open ( i1I1iI , "w" )
  i1ioO . write ( json . dumps ( i1I11IiI ) )
  i1ioO . close ( )
 else :
  OoOo00OoOO00 = json . loads ( open ( i1I1iI ) . read ( ) )
  o0oOOOOoo0 = len ( OoOo00OoOO00 )
  for oO0oOOoOo000O in OoOo00OoOO00 :
   iIiIi11 = oO0oOOoOo000O [ 0 ]
   iI = oO0oOOoOo000O [ 1 ]
   oo00O00oO000o = oO0oOOoOo000O [ 2 ]
   try :
    II1o0O0OO = oO0oOOoOo000O [ 3 ]
    if II1o0O0OO == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     II1o0O0OO = oo00O00oO000o
    else :
     II1o0O0OO = oOOo0O00o
   try : oOoO0o = oO0oOOoOo000O [ 5 ]
   except : oOoO0o = None
   try : i1II = oO0oOOoOo000O [ 6 ]
   except : i1II = None
   if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . oooOo0oo0oo
   if oO0oOOoOo000O [ 4 ] == 0 :
    Iii1I1I11iiI1 ( iIiIi11 , iI , '' , oo00O00oO000o , oOOo0O00o , '' , 'fav' )
   else :
    Iii1I1I11iiI1 ( iIiIi11 , iI , oO0oOOoOo000O [ 4 ] , oo00O00oO000o , oOOo0O00o , '' , 'fav' )
    if 31 - 31: i1i1I1IIii1II % ooOoO0O00 . ii - I11i + ii
def I1i1Ii ( name ) :
 iII1 = json . loads ( open ( i1I1iI ) . read ( ) )
 for III1 in range ( len ( iII1 ) ) :
  if iII1 [ III1 ] [ 0 ] == name :
   del iII1 [ III1 ]
   I1ii1i11iI1 = open ( i1I1iI , "w" )
   I1ii1i11iI1 . write ( json . dumps ( iII1 ) )
   I1ii1i11iI1 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 14 - 14: i1IiiiI1iI / Iii - oooOo0oo0oo * o0o00Oo0O % III1iiIii . o0o00Oo0O
 if 86 - 86: ooOoO0O00 * ii
def II1 ( ) :
 I1I1I1 = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 i1iIIIiI = open ( I1I1I1 , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 i1iIIIiI . write ( r'[' + IiII + ']' + '\n' )
 for iIiIi11 , o00oOOooOOo0o , I11IiI1iII , iI in IIi :
  iI = ( iI + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  i11Ii111I1 = ( iIiIi11 + '=plugin://' + IiII + '/?url=' + iI + '&mode=10012&name=' + ( iIiIi11 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( o00oOOooOOo0o ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( o00oOOooOOo0o ) . replace ( ' ' , '' ) + '+&amp;description=' )
  i1iIIIiI . write ( i11Ii111I1 + '\n' )
  if 99 - 99: iI11I1II1I1I . I1ii11iIi11i / i1iIi . oooOo0oo0oo % oOo0O0Ooo * Iii
  if 95 - 95: i1i1I1IIii1II
def oOo0ooO0O0oo ( ) :
 OOo0 = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( OOo0 )
 for iI in IIi :
  iIiiiii1i ( '24/7' , iI , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 31 - 31: Ii + o0ii1I % OOooOOo
def I1Io0Oo00 ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , iI in IIi :
  I1I1i1I ( iIiIi11 , ( iI ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def o0ooo ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , iI in IIi :
  I1I1i1I ( iIiIi11 , ( iI ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def I1i11111i1i11 ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , iI in IIi :
  I1I1i1I ( iIiIi11 , ( iI ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def I1II11IIi11i ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , iI in IIi :
  I1I1i1I ( iIiIi11 , ( iI ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def oo00ooOo ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  I1I1i1I ( iIiIi11 , iI , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 81 - 81: Ii * IiI1i11I . i1i1I1IIii1II * i1i1I1IIii1II . III1iiIii
  if 47 - 47: iI11I1II1I1I % Iii . Iii / o0o00Oo0O . Ii * o0ii1I
def iio0Oo ( ) :
 if 29 - 29: o0o00Oo0O * Ii / ii / I11i . i1iIi
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 70 - 70: ii . i1iIi / i1i1I1IIii1II . i1i1I1IIii1II - I11i
def i1II1i1iiI1 ( ) :
 if 62 - 62: o0ii1I . Ii % o0o00Oo0O % i1IiiiI1iI - I1ii11iIi11i
 OOo0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OOo0 )
 for iI , o00oOOooOOo0o , iIiIi11 , I1iIiiiI1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 + '  -  ' + ( I1iIiiiI1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iI , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 69 - 69: IIiIiII11i . OOooOOo * OOooOOo % o0ii1I + oOo0O0Ooo
  if 100 - 100: Ii - I1ii11iIi11i
  if 47 - 47: IiI1i11I * OOooOOo * III1iiIii
def iIiii1IIi1I ( ) :
 if 18 - 18: o0o00Oo0O / iI11I1II1I1I + Ii + I1ii11iIi11i
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Action[/COLOR]' , 'Aksiyon' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Adventure[/COLOR]' , 'Macera' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Animation[/COLOR]' , 'Animasyon' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Anime[/COLOR]' , 'Anime' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Biography[/COLOR]' , 'Biyografi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Comedy[/COLOR]' , 'Komedi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Drama[/COLOR]' , 'Dram' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Family[/COLOR]' , 'Aile' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']History[/COLOR]' , 'Tarih' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Horror[/COLOR]' , 'Korku' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Mystery[/COLOR]' , 'Gizem' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Romance[/COLOR]' , 'Romantik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Sport[/COLOR]' , 'Spor' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Western[/COLOR]' , 'Tarih' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 31 - 31: ooOoO0O00 - Iii + i1IiiiI1iI + i1iIi . i1iIi . o0o00Oo0O
def ii11I ( url ) :
 I1IiiIiii1 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( I1IiiIiii1 )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 2 - 2: i1i1I1IIii1II . oooOo0oo0oo
  if 43 - 43: iI11I1II1I1I
  if 29 - 29: III1iiIii % i1iIi + oO0o . ooOoO0O00 + oOo0O0Ooo
  if 24 - 24: i1IiiiI1iI / o0ii1I * Ii1I - ii / oOo0O0Ooo . i1i1I1IIii1II
def oo0OOoOo0 ( ) :
 if 63 - 63: OOooOOo
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 iI = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( Ii11 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( iI )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for iI , o00oOOooOOo0o , iIiIi11 in IIi :
  if Ii11 in iIiIi11 . lower ( ) :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 61 - 61: IIiIiII11i * o0ii1I + IIiIiII11i % IiI1i11I . ooOoO0O00 . i1i1I1IIii1II
   if 33 - 33: iI11I1II1I1I + oOo0O0Ooo / i1i1I1IIii1II * IiI1i11I - i1i1I1IIii1II
   if 96 - 96: Iii . ii % IIiIiII11i % o0ii1I
def Iii1iI1iIII ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oo0O0oO0O0O , iIii , oo0Oo , iIiIi11 in IIi :
  I1IiIIIIi1iiI = ( oo0Oo ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O0ii = ( iIii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O00OIIIIIi1 = 'Season ' + O0ii + 'Episode ' + I1IiIIIIi1iiI + iIiIi11
  o0oIi1iiiii ( O00OIIIIIi1 , oo0O0oO0O0O )
  if 88 - 88: o0ii1I / Ii % OOooOOo % oooOo0oo0oo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 70 - 70: Ii1I . Ii1I / Iii . Ii1I
  if 37 - 37: ooOoO0O00 . i1IiiiI1iI - IIiIiII11i % I11i - ooOoO0O00 . i1i1I1IIii1II
def o0oIi1iiiii ( name , url ) :
 oo0O0oO0O0O = url
 iiiiI = name
 o0o = cloudflare . source ( oo0O0oO0O0O )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for O00O0OO00oo , Ooo000 in i1Iii1i1I :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iiiiI + Ooo000 + '[/COLOR]' , O00O0OO00oo , 222 , iiIi1IIiIi + 'dtv.png' )
  if 21 - 21: IiI1i11I % III1iiIii % I1ii11iIi11i % o0o00Oo0O
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: IIiIiII11i * oOo0O0Ooo - ii / oOo0O0Ooo
 if 50 - 50: OOooOOo % o0ii1I + OOooOOo * o0ii1I - oooOo0oo0oo
def OoOo0oOooOoOO ( ) :
 if 94 - 94: iI11I1II1I1I
 if 1 - 1: o0o00Oo0O
 if 2 - 2: oO0o . Iii
 if 97 - 97: I1ii11iIi11i
 if 65 - 65: I1ii11iIi11i % oooOo0oo0oo / Ii / iI11I1II1I1I . i1IiiiI1iI + i1iIi
 if 92 - 92: i1i1I1IIii1II
 if 96 - 96: i1IiiiI1iI * iI11I1II1I1I / OOooOOo % oooOo0oo0oo * IIiIiII11i
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 3 - 3: oooOo0oo0oo . I1ii11iIi11i / Ii + oO0o
def i1O00oo00o000o ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0000ooO = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , url , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + o00oOOooOOo0o , '' , '' )
 for url in O0000ooO :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 83 - 83: i1IiiiI1iI + I11i % i1i1I1IIii1II / oO0o
def o0o000O0ooo0O ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0000ooO = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , url , iIiIi11 in IIi :
  o00oOOooOOo0o = 'http://watchepisodes.cc/' + o00oOOooOOo0o
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 10093 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
 for url in O0000ooO :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 46 - 46: III1iiIii % i1IiiiI1iI + iI11I1II1I1I * oOo0O0Ooo
def OO000O000OOO ( url , iconimage ) :
 o00oOOooOOo0o = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oo0Oo , url , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + oo0Oo + ' - ' + iIiIi11 + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , o00oOOooOOo0o , '' , '' )
  if 26 - 26: Iii * o0ii1I % oOo0O0Ooo + IiI1i11I
def I1iII1iI ( url , iconimage ) :
 o00oOOooOOo0o = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url in IIi :
  if 'player' in iIiIi11 :
   pass
  elif 'vod' in iIiIi11 :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , o00oOOooOOo0o , '' , '' )
   if 46 - 46: ii * o0ii1I . iI11I1II1I1I - o0o00Oo0O . ooOoO0O00 * oO0o
   if 83 - 83: IiI1i11I . Ii . ii . o0ii1I
   if 8 - 8: oO0o * I1ii11iIi11i
   if 41 - 41: I1ii11iIi11i / oO0o / OOooOOo - Ii - OOooOOo
   if 4 - 4: Iii . III1iiIii
   if 39 - 39: oooOo0oo0oo . I1ii11iIi11i - OOooOOo * Ii
def oo00ooOoO00 ( ) :
 if 4 - 4: OOooOOo * o0o00Oo0O - Iii
 if 72 - 72: Iii + i1iIi / oOo0O0Ooo . III1iiIii % oO0o / Ii
 if 13 - 13: i1IiiiI1iI % I11i + oooOo0oo0oo + i1IiiiI1iI + Ii - Ii1I
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 if 11 - 11: IiI1i11I
 if 20 - 20: o0ii1I . i1IiiiI1iI % o0ii1I
 if 5 - 5: oooOo0oo0oo + IiI1i11I
 if 23 - 23: i1IiiiI1iI % iI11I1II1I1I . Iii
 if 95 - 95: I1ii11iIi11i + Ii % oooOo0oo0oo - i1i1I1IIii1II
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
 if 95 - 95: i1IiiiI1iI + III1iiIii * iI11I1II1I1I
 if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / o0ii1I
 if 19 - 19: ooOoO0O00 - iI11I1II1I1I . Iii
 if 2 - 2: o0ii1I
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 12 - 12: Ii - iI11I1II1I1I * III1iiIii * IiI1i11I
 if 19 - 19: o0o00Oo0O + i1i1I1IIii1II + I11i
def oO0IIi11IiiiI11i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I1iiiiI1iI ) )
 for url , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 68 - 68: i1i1I1IIii1II + Iii * i1i1I1IIii1II . III1iiIii % o0ii1I - ii
def oOooo0oOOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 81 - 81: I11i / oOo0O0Ooo / I11i * III1iiIii + oooOo0oo0oo % i1IiiiI1iI
def OOoOOOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  if 'episode' in url :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  else :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 27 - 27: I11i / oOo0O0Ooo
  if 91 - 91: oOo0O0Ooo - IiI1i11I / oO0o - oO0o / o0ii1I - III1iiIii
def I1IIi ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O00OIiIIiIiIIiI = 'http://www.watchseriesgo.to/search/' + Ii11 . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( O00OIiIIiIiIIiI )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , iI , iIiIi11 in IIi :
  if 'watch online' in iIiIi11 :
   pass
  else :
   print iI
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.watchseriesgo.to' + iI , 10044 , o00oOOooOOo0o , '' , '' )
   if 26 - 26: i1iIi % ii . i1IiiiI1iI * i1iIi + IIiIiII11i - Ii1I
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 20 - 20: oO0o
def OOooO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , url , iIiIi11 , oo0Oo , O0O0ooOOO in IIi :
  oOO0o0 = ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oo0Oo ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + oOO0o0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , o00oOOooOOo0o , '' , O0O0ooOOO )
  if 85 - 85: IIiIiII11i - o0ii1I
def O0OoIIiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  oOO0o0 = ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + oOO0o0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 27 - 27: ii * oOo0O0Ooo - IiI1i11I / IiI1i11I
def Ii11iIi1iIiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , o00oOOooOOo0o in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , o00oOOooOOo0o , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 11 - 11: Ii1I / Ii1I
def ii1IIIIi1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iiiiI1iI = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIii , o0ooo0oooO in I1iiiiI1iI :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( o0ooo0oooO ) )
  for url , iIiIi11 in IIi :
   oOO0o0 = ( iIii ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + oOO0o0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 50 - 50: oOo0O0Ooo - i1i1I1IIii1II + i1i1I1IIii1II * Iii + i1i1I1IIii1II
class oooOoooOOo0 ( ) :
 if 25 - 25: IiI1i11I + oOo0O0Ooo + OOooOOo + i1IiiiI1iI % o0o00Oo0O
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 26 - 26: i1iIi + OOooOOo
  oOO0o0 = name
  self . Get_Sources ( iI , oOO0o0 )
  if 17 - 17: Ii1I - IiI1i11I % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * oooOo0oo0oo
  if 6 - 6: i1IiiiI1iI
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iI , iIiIi11 in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + iI
   self . Get_site_link ( URL , season_name )
   if 46 - 46: IIiIiII11i * i1IiiiI1iI
 def Get_site_link ( self , url , season_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  i1Iii1i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  I1i11 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for url in IIi :
   self . main ( url , season_name )
  for url in i1Iii1i1I :
   self . main ( url , season_name )
  for url in I1i11 :
   self . main ( url , season_name )
   if 23 - 23: ooOoO0O00 - o0o00Oo0O
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   I11iI11i1i1 = 'DACLIPS'
   if I11iI11i1i1 in oooOoooOOo0 . source_list :
    pass
   else :
    self . daclips ( url , season_name , I11iI11i1i1 )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    I11iI11i1i1 = 'THEVIDEO'
    if I11iI11i1i1 in oooOoooOOo0 . source_list :
     pass
    else :
     self . thevideo ( url , season_name , I11iI11i1i1 )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     I11iI11i1i1 = 'ALLMYVIDEOS'
     if I11iI11i1i1 in oooOoooOOo0 . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , I11iI11i1i1 )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      I11iI11i1i1 = 'VIDSPOT'
      if I11iI11i1i1 in oooOoooOOo0 . source_list :
       pass
      else :
       self . vidspot ( url , season_name , I11iI11i1i1 )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       I11iI11i1i1 = 'VODLOCKER'
       if I11iI11i1i1 in oooOoooOOo0 . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , I11iI11i1i1 )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        I11iI11i1i1 = 'VIDTO'
        if I11iI11i1i1 in oooOoooOOo0 . source_list :
         pass
        else :
         self . vidto ( url , season_name , I11iI11i1i1 )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 7 - 7: IiI1i11I
       else :
        if 'youwatch' in url :
         I11iI11i1i1 = 'YouWatch'
         if I11iI11i1i1 in oooOoooOOo0 . source_list :
          pass
         else :
          self . youwatch ( url , season_name , I11iI11i1i1 )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 18 - 18: OOooOOo
          if 77 - 77: i1IiiiI1iI . Ii / o0ii1I * Ii - I11i
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for I1II , iIiIi11 in IIi :
   self . Printer ( I1II , season_name , source_name )
   if 6 - 6: Ii
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for I1II , iIiIi11 in IIi :
   self . Printer ( I1II , season_name , source_name )
   if 16 - 16: III1iiIii
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for I1II in IIi :
   self . Printer ( I1II , season_name , source_name )
   if 84 - 84: ooOoO0O00 / iI11I1II1I1I / i1i1I1IIii1II / o0ii1I
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for I1II in IIi :
   self . Printer ( I1II , season_name , source_name )
   if 7 - 7: OOooOOo . oooOo0oo0oo % I1ii11iIi11i
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for I1II in IIi :
   self . Printer ( I1II , season_name , source_name )
   if 55 - 55: i1iIi - I1ii11iIi11i * i1i1I1IIii1II
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for I1II in IIi :
   self . Printer ( I1II , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for I1II in IIi :
   self . Printer ( I1II , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for I1II in IIi :
   self . youplay ( I1II , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for I1II in IIi :
   self . Printer ( I1II , season_name , source_name )
   if 72 - 72: I11i % I11i + IiI1i11I + Ii1I / I1ii11iIi11i
 def Printer ( self , Link , season_name , source_name ) :
  if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
  if Link in oooOoooOOo0 . List :
   pass
  elif source_name in oooOoooOOo0 . source_list :
   pass
  else :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   oooOoooOOo0 . List . append ( Link )
   oooOoooOOo0 . source_list . append ( source_name )
   if 64 - 64: III1iiIii
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
   if 89 - 89: o0o00Oo0O + III1iiIii * i1IiiiI1iI
   if 30 - 30: OOooOOo
   if 39 - 39: Ii1I + I11i + i1IiiiI1iI + III1iiIii
   if 48 - 48: i1IiiiI1iI / i1iIi . iI11I1II1I1I
def O0Oooo ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 72 - 72: ooOoO0O00 . I11i
def iIIiiIiII1i ( url ) :
 Oo00OOO0 = '20'
 iiIIii1iII1i = [ ]
 ooo0oOoO00Oo = '                                                    '
 I111iI11i = '        '
 Iii1I1I11iiI1 ( ooo0oOoO00Oo + 'pl' + I111iI11i + 'w' + I111iI11i + 'd' + I111iI11i + 'l' + I111iI11i + 'f' + I111iI11i + 'a' + I111iI11i + 'pts' , '' , '' , '' , '' , '' )
 OOo0 = O0i11i1iiI1i ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( OOo0 )
 for O0O000o0Oo , o0oO0o0O0o0Oo , I1Iiii , oO0Oooo0OoO , IiooOo0oo0O0O , ooOoO00 , i1ioO , IIiii , i1Ii11I1i in IIi :
  iI11IIi1iiI1I = oO0oO0ooOoO0 ( o0oO0o0O0o0Oo )
  Ii1I11IIi1 = oO0oO0ooOoO0 ( I1Iiii )
  I1ii = oO0oO0ooOoO0 ( oO0Oooo0OoO )
  iiI = oO0oO0ooOoO0 ( IiooOo0oo0O0O )
  iii11I1 = oO0oO0ooOoO0 ( ooOoO00 )
  i1II1iIii = oO0oO0ooOoO0 ( i1ioO )
  iiIIii1iII1i . append ( O0O000o0Oo [ 0 ] )
  i1iII1iii = len ( iiIIii1iII1i )
  o0O0o = int ( len ( ooo0oOoO00Oo ) - len ( O0O000o0Oo ) - 2 )
  if len ( iiIIii1iII1i ) >= 10 :
   o0O0o = o0O0o - 1
  if len ( iiIIii1iII1i ) <= int ( Oo00OOO0 ) :
   I1I1i1I ( str ( i1iII1iii ) + ' ' + O0O000o0Oo + ooo0oOoO00Oo [ 0 : o0O0o ] + o0oO0o0O0o0Oo + iI11IIi1iiI1I + I1Iiii + Ii1I11IIi1 + oO0Oooo0OoO + I1ii + IiooOo0oo0O0O + iiI + ooOoO00 + iii11I1 + i1ioO + i1II1iIii + ' ' + i1Ii11I1i , '' , '' , '' , '' , '' )
   if 79 - 79: OOooOOo + iI11I1II1I1I * ooOoO0O00 * i1iIi - Iii * oO0o
   if 78 - 78: IiI1i11I % Ii + IiI1i11I + I11i
def oO0oO0ooOoO0 ( space ) :
 if len ( space ) > 1 :
  O0ooooo000 = len ( '        ' ) - len ( space ) + 1
  space = int ( O0ooooo000 ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 22 - 22: Iii - I11i
def OOOO00O0OO0oo ( ) :
 if 41 - 41: OOooOOo % i1IiiiI1iI * i1i1I1IIii1II * ooOoO0O00
 if 32 - 32: oOo0O0Ooo + Ii - i1IiiiI1iI / IIiIiII11i
 if 27 - 27: i1iIi . I1ii11iIi11i + i1iIi + IiI1i11I
 if 28 - 28: oO0o - i1iIi - i1i1I1IIii1II % i1i1I1IIii1II / o0o00Oo0O
 if 99 - 99: IIiIiII11i - iI11I1II1I1I
 if 24 - 24: oOo0O0Ooo - ooOoO0O00 - o0o00Oo0O % i1IiiiI1iI - iI11I1II1I1I . Iii
 if 26 - 26: oO0o % ooOoO0O00 * o0o00Oo0O . i1IiiiI1iI
 if 31 - 31: o0o00Oo0O - III1iiIii * Ii * ooOoO0O00
 if 78 - 78: i1iIi * OOooOOo . o0ii1I . OOooOOo % iI11I1II1I1I
 if 67 - 67: o0ii1I . I1ii11iIi11i
 if 39 - 39: Iii * i1IiiiI1iI
 if 63 - 63: i1iIi % oOo0O0Ooo . oooOo0oo0oo - i1iIi / I1ii11iIi11i % oOo0O0Ooo
 if 39 - 39: I11i . ooOoO0O00 % i1i1I1IIii1II / Iii % o0o00Oo0O
 if 100 - 100: i1IiiiI1iI - OOooOOo
 if 78 - 78: ii - OOooOOo . Ii
 if 36 - 36: i1i1I1IIii1II * IiI1i11I + III1iiIii * IiI1i11I . Ii1I - iI11I1II1I1I
 if 14 - 14: Iii * i1i1I1IIii1II + Ii
 if 84 - 84: IiI1i11I / IIiIiII11i
 if 86 - 86: oOo0O0Ooo
 if 97 - 97: IIiIiII11i
 if 38 - 38: oOo0O0Ooo
 if 42 - 42: I11i
 if 8 - 8: Ii / i1iIi
 if 33 - 33: i1IiiiI1iI * III1iiIii - o0o00Oo0O + oOo0O0Ooo / III1iiIii
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 if 85 - 85: III1iiIii - I11i % oooOo0oo0oo - IIiIiII11i
 if 56 - 56: o0ii1I * Ii
 if 92 - 92: IIiIiII11i - o0o00Oo0O . i1IiiiI1iI
 if 59 - 59: OOooOOo
 if 47 - 47: IIiIiII11i - Ii1I - o0ii1I
 if 9 - 9: Ii1I - III1iiIii
 if 64 - 64: ooOoO0O00
 if 71 - 71: III1iiIii * I11i
 if 99 - 99: I11i
 if 28 - 28: ii % o0o00Oo0O - oooOo0oo0oo / I11i / oOo0O0Ooo
 if 41 - 41: IIiIiII11i * III1iiIii / oO0o . i1i1I1IIii1II
 if 50 - 50: ii + iI11I1II1I1I / i1i1I1IIii1II / oooOo0oo0oo . Ii . i1iIi
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
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 for iI , o00oOOooOOo0o , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iI , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o00oOOooOOo0o , Oo00OOOOO , '' )
  if 2 - 2: oooOo0oo0oo
def IiOoo0o0OO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1iiiiI1iI in I1iiiiI1iI :
  Oo0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( I1iiiiI1iI ) )
  for O0o00OoooO in Oo0 :
   O0o00OoooO = O0o00OoooO
  IiI1i1iI = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I1iiiiI1iI ) )
  for iIIiiIIIII , o00oOOooOOo0o , time , ooO00O00oOO in IiI1i1iI :
   Ii11iiI1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( ooO00O00oOO )
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + O0o00OoooO + ' - ' + iIIiiIIIII + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + o00oOOooOOo0o , Oo00OOOOO , ( str ( Ii11iiI1 ) ) )
   if 24 - 24: IIiIiII11i
 O0oO0 ( 'tvshows' , 'Media Info 3' )
 if 23 - 23: I1ii11iIi11i - IiI1i11I
def o0oO0O ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , iiIi1IIiIi + 'fanart.jpg' , '' )
 if 62 - 62: i1i1I1IIii1II . i1IiiiI1iI - ii * IIiIiII11i . Ii
def iiIIiIi1i1I1 ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , url , iIiIi11 in IIi :
  oOoooo0OooO = iIiIi11 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIiIi11 :
   pass
  else :
   oOoooo0OooO = iIiIi11 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + oOoooo0OooO + '[/COLOR]' , url , 10013 , o00oOOooOOo0o )
 for url , o00oOOooOOo0o , iIiIi11 in i1Iii1i1I :
  oOoooo0OooO = iIiIi11 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIiIi11 :
   pass
  else :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + oOoooo0OooO + '[/COLOR]' , url , 10013 , o00oOOooOOo0o )
def OooO0O ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 73 - 73: oOo0O0Ooo / o0o00Oo0O % IiI1i11I * IIiIiII11i
 if 99 - 99: o0ii1I + III1iiIii % Ii
 if 41 - 41: oOo0O0Ooo % oooOo0oo0oo
 if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % i1IiiiI1iI
 if 78 - 78: Ii1I + ii - oOo0O0Ooo * OOooOOo * IiI1i11I
 if 7 - 7: oooOo0oo0oo . III1iiIii . i1IiiiI1iI / o0ii1I / I1ii11iIi11i
 if 83 - 83: Iii / I1ii11iIi11i
 for url , o00oOOooOOo0o , iIiIi11 in i1Iii1i1I :
  oOoooo0OooO = iIiIi11 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iIiIi11 :
   pass
  else :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + oOoooo0OooO + '[/COLOR]' , url , 10013 , o00oOOooOOo0o )
   if 23 - 23: iI11I1II1I1I
def I11IIiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for O00O0OO00oo in IIi :
  iii111 = ( O00O0OO00oo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  iiiIi ( 'http:' + iii111 )
  if 96 - 96: I11i - oOo0O0Ooo % OOooOOo + oO0o - III1iiIii - III1iiIii
  if 2 - 2: i1iIi % Ii
  if 11 - 11: iI11I1II1I1I . i1IiiiI1iI - I1ii11iIi11i / Iii + IIiIiII11i
  if 29 - 29: Iii . Ii + ooOoO0O00 - o0ii1I + o0o00Oo0O . oOo0O0Ooo
def i1iIiII1 ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OOo0 )
 for url , iIiIi11 , o00oOOooOOo0o in IIi :
  iiIi1IIiI ( iIiIi11 , url , 8046 , o00oOOooOOo0o )
 for url in i1Iii1i1I :
  iIiiiii1i ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def Oo00OO ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OOo0 )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  iiiIi ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 8 - 8: oO0o + i1IiiiI1iI . oooOo0oo0oo
def oO00O0OO ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OOo0 )
 for url in IIi :
  yt . PlayVideo ( url )
  if 40 - 40: Ii % iI11I1II1I1I % iI11I1II1I1I
def I1I1i ( ) :
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , iI , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOO0o ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( OOo0 )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( OOo0 )
 for o00oOOooOOo0o , url , iIiIi11 in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + o00oOOooOOo0o )
 for url in next :
  iIiiiii1i ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 88 - 88: ii
  if 46 - 46: o0o00Oo0O % ii
def I1IiII ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOo0 )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def o0O00o0o ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 222 , '' )
  if 31 - 31: i1iIi % oOo0O0Ooo % III1iiIii / i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoOOoo ( name , url ) :
 I1OooO00Oo = 0
 name = name
 url = url
 oOI1Ii1I1 = [ '144' , '240' , '380' , '480' , '720' ]
 IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , oOI1Ii1I1 )
 if IiII111iI1ii1 == 0 :
  OooO0OO ( url )
  if 81 - 81: Ii1I - oO0o * i1i1I1IIii1II
  if 81 - 81: IiI1i11I - o0ii1I - oooOo0oo0oo % III1iiIii % I11i . iI11I1II1I1I
  if 79 - 79: Ii1I - Ii1I . o0ii1I / III1iiIii
  if 57 - 57: i1iIi * iI11I1II1I1I * IiI1i11I * o0ii1I / o0ii1I
  if 43 - 43: o0o00Oo0O * Ii - ii - i1i1I1IIii1II
  if 46 - 46: i1i1I1IIii1II * ooOoO0O00 / Ii1I
  if 100 - 100: oOo0O0Ooo - oooOo0oo0oo
  if 91 - 91: I11i * Ii1I - IiI1i11I . IIiIiII11i
def iI11II ( ) :
 OOo0 = o0O0Oo00 ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( OOo0 )
 for iIiIi11 , iI in IIi :
  if 'genre' in iI :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , iI , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1IiIiIIII ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( OOo0 )
 for url , iIiIi11 , o00oOOooOOo0o in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , o00oOOooOOo0o )
 for url in next :
  iIiiiii1i ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 93 - 93: IiI1i11I - o0o00Oo0O
def O0oO0o00OoO ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( OOo0 )
 for url in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  o0O00o0o ( url )
  if 78 - 78: III1iiIii / IiI1i11I * o0ii1I . oooOo0oo0oo . i1i1I1IIii1II - i1IiiiI1iI
def I1IiI11 ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO00O = 'http://documentarylovers.com/?s=' + ( Ii11 ) . replace ( ' ' , '+' )
 II1i111 = oO00O . lower ( )
 II1IiIiIIII ( II1i111 )
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + i1i1I1IIii1II
def IIi1iii ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  if 'films' in url :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def ii1Ii ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OOo0 )
 for o00oOOooOOo0o , url , iIiIi11 in IIi :
  if 'films' in url :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + o00oOOooOOo0o )
 for url in i1Iii1i1I :
  iIiiiii1i ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def IIIIi11111 ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OOo0 )
 for url in IIi :
  if 'rtd' in url :
   Oo0o00o0oOoo0 ( url )
   if 36 - 36: i1IiiiI1iI / OOooOOo + OOooOOo * i1iIi / oooOo0oo0oo * o0o00Oo0O
def Oo0o00o0oOoo0 ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OOo0 )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  OooO0OO ( url )
  if 17 - 17: oO0o / i1iIi % oOo0O0Ooo
  if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
def OOo0iIiiI11II11 ( ) :
 II11iIiIIIiI = o0O0Oo00 ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , o00oOOooOOo0o , iIiIi11 , Ooo0 in IIi :
  iIiiiii1i ( ( iIiIi11 + '[COLOR' + ooOoOoo0O + ']' + Ooo0 + '[/COLOR]' ) , iI , 8086 , o00oOOooOOo0o )
  if 75 - 75: i1IiiiI1iI - IiI1i11I . i1i1I1IIii1II
def O0ooO0oO0 ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 8087 , o00oOOooOOo0o )
  if 50 - 50: ooOoO0O00 - IiI1i11I + I11i * IiI1i11I * ii
def ooO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  O00O0O0 ( url , iIiIi11 )
  if 24 - 24: iI11I1II1I1I % I1ii11iIi11i % Ii
def O00O0O0 ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 55 - 55: IiI1i11I
def Ii11I ( ) :
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOo0 )
 for iI , o00oOOooOOo0o , iIiIi11 in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iI , 3002 , 'http://www.solie.org/alibrary/' + o00oOOooOOo0o )
def i11IiiI1iIiII ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOo0 )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00oOOooOOo0o )
def o0oOOoOoo ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OOo0 )
 ooO0O = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OOo0 )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , iIiIi11 in ooO0O :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']Season- ' + iIiIi11 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , o00oOOooOOo0o , iIiIi11 in i1Iii1i1I :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00oOOooOOo0o )
def O0Ooo0O0O ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OOo0 )
 for url in IIi :
  OOOO0 ( url )
def OOOO0 ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OOo0 )
 for url in IIi :
  OooO0OO ( url )
  if 92 - 92: I1ii11iIi11i + III1iiIii / I1ii11iIi11i + o0ii1I / oooOo0oo0oo
def oOO ( ) :
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iI , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def I11iI ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( OOo0 )
 for url in IIi :
  O0OOO00 ( url )
  if 98 - 98: I1ii11iIi11i - i1i1I1IIii1II . i1IiiiI1iI
def oo000ii ( ) :
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iI , 8065 , iiIi1IIiIi + 'classictv.png' )
def O0oo0O0oO00O0 ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OOo0 )
 for url in IIi :
  if 'mp4' in url :
   OooO0OO ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 89 - 89: o0ii1I * Iii + OOooOOo / Ii
def oo00ooOOOo0O ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iI , 8071 , iiIi1IIiIi + 'streams.png' )
def i11111i1I1IiI ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url in IIi :
  if '(Free Access)' in iIiIi11 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def Ii111i1I1i1i ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , iIiIi11 , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , o00oOOooOOo0o , oOOo0O00o , '' )
  if 70 - 70: oooOo0oo0oo - III1iiIii . i1IiiiI1iI
def IiII11 ( ) :
 oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOI1Ii1I1 )
 if IiII111iI1ii1 == 0 :
  oO00o ( 'http://watchxxxfree.com/categories' )
 if IiII111iI1ii1 == 1 :
  I1IOOO ( 'http://www.perfectgirls.net' )
 if IiII111iI1ii1 == 2 :
  IIii1iiiIi ( 'http://www.xvideos.com/best' )
 if IiII111iI1ii1 == 3 :
  iI11I1IiI1 ( 'http://www.xvideos.com/best' )
 if IiII111iI1ii1 == 4 :
  IIii1iiiIi ( 'http://www.xvideos.com/best' )
 if IiII111iI1ii1 == 5 :
  IIii1iiiIi ( 'http://www.xvideos.com/verified/videos' )
 if IiII111iI1ii1 == 6 :
  I11Ii ( 'http://www.xvideos.com/tags' )
 if IiII111iI1ii1 == 7 :
  OOIiIIi1iIii1I1 ( 'http://www.xvideos.com/porn' )
 if IiII111iI1ii1 == 8 :
  ii1oo ( )
  if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
  if 34 - 34: I11i % Ii1I + o0ii1I * Iii / i1i1I1IIii1II
  if 18 - 18: i1iIi
  if 92 - 92: oO0o % iI11I1II1I1I / III1iiIii * IiI1i11I . ooOoO0O00 + i1i1I1IIii1II
  if 24 - 24: III1iiIii . IiI1i11I * III1iiIii % Ii . Ii + ooOoO0O00
  if 64 - 64: iI11I1II1I1I / III1iiIii / I1ii11iIi11i - Ii1I
  if 100 - 100: III1iiIii + ooOoO0O00 * oO0o
  if 64 - 64: i1i1I1IIii1II * Ii . I1ii11iIi11i
  if 52 - 52: I1ii11iIi11i / i1iIi / IiI1i11I - I11i / IiI1i11I
def ooIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  if 'ch' in url :
   IiIIii1iiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def iii1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIiI11I = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 in IIi :
  I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for iIiIi11 , url in iIiI11I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def IIII11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   I11I1I1I ( url )
def ooOo0o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def oO00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , url , iIiIi11 , O0ooooo000 in IIi :
  if 'category' in url :
   IiIIii1iiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORorange]   ' + O0ooooo000 + '[/COLOR]' , url , 90006 , o00oOOooOOo0o , iiIi1IIiIi + 'Jizbox.png' , '' )
def O000ooOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIiI11I = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , url , iIiIi11 in IIi :
  I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , o00oOOooOOo0o , '' , '' )
 for url in iIiI11I :
  Iii1I1I11iiI1 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def O00OOOoOooO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   I11I1I1I ( url )
def I11I1I1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def I1IOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , O0ooooo000 in IIi :
  if 'category' in url :
   IiIIii1iiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORorange]' + O0ooooo000 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def OOoOI1i1i1Iii1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oo0O0oO0O0O = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIiI11I = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , o00oOOooOOo0o in IIi :
  I1I1i1I ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , o00oOOooOOo0o , '' , '' )
 for url in iIiI11I :
  Iii1I1I11iiI1 ( '[COLORred]NEXT[/COLOR]' , oo0O0oO0O0O + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OoO00Ooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  IIIiI1i ( 'http://www.perfectgirls.net' + url )
def IIIiI1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  iiiIi ( 'http://' + url )
def OOIiIIi1iIii1I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , O0ooooo000 in IIi :
  IiIIii1iiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgreen] - No of Videos : [COLORorange]' + O0ooooo000 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def I11Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iIiI11I = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in iIiI11I :
  IiIIii1iiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , O0ooooo000 in IIi :
  IiIIii1iiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgreen] - No of Videos : [COLORorange]' + ( O0ooooo000 + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 58 - 58: ooOoO0O00 * IiI1i11I . o0o00Oo0O % o0ii1I
def IIi1iII11III ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iIiI11I = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in iIiI11I :
  IiIIii1iiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , url , iIiIi11 , oO0OO in IIi :
  IiIIii1iiI ( iIiIi11 + '--' + ( oO0OO ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( o00oOOooOOo0o ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 35 - 35: Iii % I1ii11iIi11i
  if 52 - 52: I1ii11iIi11i - o0o00Oo0O
def IIii1iiiIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , url , iIiIi11 , iii1II1iI1IIi , O0ooo0O00Ooo0 in IIi :
  IiIIii1iiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgreen] - Porn Quality : [COLORorange]' + O0ooo0O00Ooo0 + ' - [COLORred]' + iii1II1iI1IIi + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , o00oOOooOOo0o , o00oOOooOOo0o , O0ooo0O00Ooo0 + ' - ' + iii1II1iI1IIi )
 i11iiI11II = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in i11iiI11II :
  IiIIii1iiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 3 - 3: oooOo0oo0oo + Iii
def iI11I1IiI1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIiI11I = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in iIiI11I :
  IiIIii1iiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I1iiiiI1iI ) )
 for url , iIiIi11 in IIi :
  if '/c/' in url :
   IiIIii1iiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 20 - 20: Ii / OOooOOo + Ii1I / o0o00Oo0O
   if 97 - 97: Ii
def ii1oo ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 ii11 = ( Ii11 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 II1i111 = ii11 . lower ( )
 IIIIIIi1IIi1I11i = 'http://www.xvideos.com/?k=' + II1i111
 print IIIIIIi1IIi1I11i + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( IIIIIIi1IIi1I11i )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , iI , iIiIi11 , iii1II1iI1IIi , O0ooo0O00Ooo0 in IIi :
  IiIIii1iiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgreen] - Porn Quality : [COLORorange]' + O0ooo0O00Ooo0 + ' - [COLORred]' + iii1II1iI1IIi + '[/COLOR]' , 'http://www.xvideos.com' + iI , 10108 , o00oOOooOOo0o , o00oOOooOOo0o , O0ooo0O00Ooo0 + ' - ' + iii1II1iI1IIi )
 i11iiI11II = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for iI in i11iiI11II :
  IiIIii1iiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iI , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 47 - 47: o0o00Oo0O - Iii - o0o00Oo0O
if 12 - 12: ii . Iii . oO0o
if 73 - 73: o0ii1I * ii * Iii - Ii
if 58 - 58: I11i + OOooOOo - III1iiIii
if 82 - 82: o0ii1I . iI11I1II1I1I / o0ii1I / i1i1I1IIii1II % iI11I1II1I1I
if 34 - 34: oooOo0oo0oo
if 99 - 99: IIiIiII11i
if 13 - 13: Iii - i1iIi + IiI1i11I % Iii . IiI1i11I - ooOoO0O00
if 67 - 67: oooOo0oo0oo . Ii + i1iIi . iI11I1II1I1I
if 28 - 28: oOo0O0Ooo + oOo0O0Ooo + i1IiiiI1iI
if 22 - 22: i1IiiiI1iI
if 89 - 89: i1iIi . oO0o * ii + OOooOOo / o0o00Oo0O
if 60 - 60: Iii
if 97 - 97: Ii * iI11I1II1I1I / IIiIiII11i
if 66 - 66: IIiIiII11i + IiI1i11I * i1i1I1IIii1II % Iii / ooOoO0O00 / iI11I1II1I1I
if 62 - 62: OOooOOo + i1i1I1IIii1II * III1iiIii + o0o00Oo0O / oooOo0oo0oo + i1iIi
if 38 - 38: ooOoO0O00 / iI11I1II1I1I + IiI1i11I
if 26 - 26: Ii1I . o0ii1I % I11i
if 4 - 4: i1IiiiI1iI
if 80 - 80: I1ii11iIi11i . o0o00Oo0O % I11i . I11i
if 52 - 52: oO0o % Ii . i1iIi % OOooOOo % ii
if 5 - 5: OOooOOo / o0o00Oo0O / Ii
if 88 - 88: IIiIiII11i - IiI1i11I / ii
if 71 - 71: Ii1I
if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
if 1 - 1: III1iiIii % ooOoO0O00
if 41 - 41: oO0o * oO0o / IiI1i11I + Ii1I . I11i
if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / o0ii1I
if 80 - 80: Ii1I
if 67 - 67: IIiIiII11i
if 2 - 2: I11i - o0o00Oo0O * o0ii1I % III1iiIii
if 64 - 64: ooOoO0O00 . i1iIi
if 7 - 7: i1i1I1IIii1II . IiI1i11I - IiI1i11I / i1IiiiI1iI % I1ii11iIi11i
if 61 - 61: i1i1I1IIii1II - Ii1I / IiI1i11I % Ii1I + oO0o / I1ii11iIi11i
if 10 - 10: Ii / OOooOOo
def iii1OO00Oo00o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 I1i11 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in I1i11 :
  if 'http' in url :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . oooOo0oo0oo
def Ii1111i11 ( url ) :
 I11I1IIiiII1 = xbmc . Player ( IIIIIii1ii11 ( ) )
 import urlresolver
 try : I11I1IIiiII1 . play ( url )
 except : pass
 if 58 - 58: o0ii1I * iI11I1II1I1I + i1iIi . i1iIi
 if 74 - 74: i1iIi - I11i * III1iiIii % i1iIi
def Oo0O0 ( ) :
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
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 8091 , iiIi1IIiIi + 'gofish.png' )
def O0ooO00OO ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , o00oOOooOOo0o in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 8092 , o00oOOooOOo0o )
 for url in next :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def IiI11I1I111 ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o00OoOoo0 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o in o00OoOoo0 :
  o00oOOooOOo0o = o00oOOooOOo0o
 for url , iIiIi11 in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 8092 , o00oOOooOOo0o )
 for url in next :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 3 - 3: i1IiiiI1iI
def iiiiiiI ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 41 - 41: o0ii1I
  if 49 - 49: o0ii1I % IIiIiII11i . o0ii1I - I11i - Iii * III1iiIii
  if 47 - 47: o0o00Oo0O . I11i / o0ii1I * IiI1i11I
  if 63 - 63: i1IiiiI1iI - i1i1I1IIii1II - IiI1i11I - i1iIi / i1i1I1IIii1II + oO0o
o0oOo = '{PQ},' ; II1oOO0O0Ooo0 = '{SC},' ; I11iiI1i = '{XG},' ; ooOoOO = '{JP},' ; iIiiII11 = '{HW},' ; OOo0oo0 = '{RT},'
def I1IiiI1ii1i ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 II1i11i1iIi11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 iI = 'http://onlinemovies.tube/?s=' + ( Ii11 ) . replace ( ' ' , '+' )
 oo0O0oO0O0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 oOo0O = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 I11iIiii1 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 iIIIiiiI11I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1ii1111Ii = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0OiiiI1i11Ii = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + Ii11
 iIiII = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 32 - 32: o0ii1I + III1iiIii + Ii1I
 I1ii1II1iII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 II1io0OO00oo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 79 - 79: ooOoO0O00 / o0ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( iI )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( oo0O0oO0O0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( oOo0O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( I11iIiii1 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OOoO = O00O0oOO00O00 ( iIIIiiiI11I )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IiIIII = O00O0oOO00O00 ( o0OiiiI1i11Ii )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOOo = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 oo0oO0 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 81 - 81: iI11I1II1I1I
 if 86 - 86: III1iiIii % III1iiIii % ii
 OooOoOOo0oO00 = O00O0oOO00O00 ( I1ii1II1iII )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 O00O = O00O0oOO00O00 ( II1io0OO00oo )
 if 42 - 42: I1ii11iIi11i . i1i1I1IIii1II + o0o00Oo0O / oooOo0oo0oo % ii
 if oo0oO0 != 'Failed' :
  IiIiIi1I1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oo0oO0 )
  for iI , iIiIi11 in IiIiIi1I1 :
   IiI1ii1Ii = O00O0oOO00O00 ( iI )
   oooOOOoOOOo0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiI1ii1Ii )
   for O00oOoo0OoO0 , Ooo0 in oooOOOoOOOo0O :
    Ooo0 = ( Ooo0 . replace ( '.' , ' ' ) )
    if II1i111 in Ooo0 . lower ( ) :
     if '.mkv' in O00oOoo0OoO0 :
      I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , iI + O00oOoo0OoO0 , 222 , '' , '' , '' )
     elif '.mp4' in O00oOoo0OoO0 :
      I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , iI + O00oOoo0OoO0 , 222 , '' , '' , '' )
     elif '.avi' in O00oOoo0OoO0 :
      I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , iI + O00oOoo0OoO0 , 222 , '' , '' , '' )
     elif '.wav' in O00oOoo0OoO0 :
      I1I1i1I ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , iI + O00oOoo0OoO0 , 222 , '' , '' , '' )
     else :
      Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , iI + O00oOoo0OoO0 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 19 - 19: i1iIi / o0ii1I
      O0oO0 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for iI , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in i1Iii1i1I :
   if Ii11 in iIiIi11 . lower ( ) :
    I1I1i1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORred] source Technica[/COLOR]' ) , iI , 222 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 43 - 43: OOooOOo % o0ii1I + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 98 - 98: I11i * I1ii11iIi11i - o0ii1I . i1iIi
 if o00OooOO000 != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for I11III111i , iIiIi11 in I1i11 :
   if Ii11 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOo0O + I11III111i ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  OooOo0oo0O0o00O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for iI , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in OooOo0oo0O0o00O :
   if Ii11 in iIiIi11 . lower ( ) :
    I1I1i1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORred] source RaizTv[/COLOR]' ) , iI , 222 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 2 - 2: I1ii11iIi11i - i1iIi % iI11I1II1I1I
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if OOoO != 'Failed' :
  OOoo0 = [ ]
  OoOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoO )
  for iI , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in OoOOo :
   if Ii11 in iIiIi11 . lower ( ) :
    if iIiIi11 in OOoo0 :
     pass
    else :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , iI , 1016 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
     OOoo0 . append ( iIiIi11 )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     O0oO0 ( 'tvshows' , 'Media Info 3' )
 if IiIIII != 'Failed' :
  III1I1I = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IiIIII )
  for iI , o00oOOooOOo0o , iIiIi11 in III1I1I :
   if Ii11 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iI , 7067 , o00oOOooOOo0o )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 88 - 88: i1IiiiI1iI - oO0o
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if OooOoOOo0oO00 != 'Failed' :
  I1I1iII1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OooOoOOo0oO00 )
  for iI , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in I1I1iII1i :
   if Ii11 in iIiIi11 . lower ( ) :
    I1I1i1I ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , iI , 222 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 79 - 79: IiI1i11I
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: IIiIiII11i + IiI1i11I . Iii . o0o00Oo0O * ooOoO0O00 - o0ii1I
    if 48 - 48: Ii1I + I1ii11iIi11i
    if 76 - 76: Ii1I
    if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . o0ii1I
    if 51 - 51: o0ii1I + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
    if 20 - 20: i1IiiiI1iI . Iii . o0ii1I + Iii - oooOo0oo0oo * i1i1I1IIii1II
    if 82 - 82: oO0o
    if 78 - 78: IIiIiII11i / Iii - Ii + Ii1I * I1ii11iIi11i
    if 17 - 17: OOooOOo
    if 72 - 72: IiI1i11I . I1ii11iIi11i - Ii / oOo0O0Ooo
 i1iii11 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 64 - 64: i1i1I1IIii1II
 for i1iiiIii11 in i1iii11 :
  OOoOOO000O0 = oO0 + i1iiiIii11 + oOoOooOo0o0
  oo0oO0 = O00O0oOO00O00 ( OOoOOO000O0 )
  if oo0oO0 != 'Failed' :
   IiIiIi1I1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0oO0 )
   for iI , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in IiIiIi1I1 :
    if Ii11 in iIiIi11 . lower ( ) :
     I1I1i1I ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgold] - Source Pandoras[/COLOR]' , iI , 222 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 80 - 80: I11i % iI11I1II1I1I
     O0oO0 ( 'tvshows' , 'Media Info 3' )
     if 63 - 63: III1iiIii * Ii
 i1iii11 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 86 - 86: Iii % Iii - OOooOOo + i1IiiiI1iI / oOo0O0Ooo * ii
 if 26 - 26: IIiIiII11i * IiI1i11I + I11i / o0o00Oo0O + ooOoO0O00 - Iii
 for i1iiiIii11 in i1iii11 :
  OOoOOO000O0 = II1i11i1iIi11 + i1iiiIii11
  iiiiiII = O00O0oOO00O00 ( OOoOOO000O0 )
  if iiiiiII != 'Failed' :
   ii1ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( iiiiiII )
   for I11III111i , iIiIi11 in ii1ii :
    if Ii11 in iIiIi11 . lower ( ) :
     iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( II1i11i1iIi11 + i1iiiIii11 + I11III111i ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 56 - 56: oooOo0oo0oo
     O0oO0 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + III1iiIii - Iii
def O0OoO0ooOO0o ( ) :
 if 81 - 81: Ii1I + ii - oooOo0oo0oo * o0o00Oo0O
 if 100 - 100: iI11I1II1I1I - OOooOOo
 if 28 - 28: I1ii11iIi11i . o0o00Oo0O . Iii
 if 60 - 60: IIiIiII11i + i1IiiiI1iI / i1i1I1IIii1II % ii - ooOoO0O00
 if 57 - 57: i1iIi
 if 99 - 99: I1ii11iIi11i + i1IiiiI1iI % i1iIi - I11i
 if 52 - 52: Ii1I
 if 93 - 93: IiI1i11I . Ii
 if 24 - 24: oooOo0oo0oo . oO0o + i1IiiiI1iI . i1i1I1IIii1II - Ii1I % IiI1i11I
 if 49 - 49: o0o00Oo0O . I1ii11iIi11i / o0ii1I
 if 29 - 29: Ii1I / i1i1I1IIii1II * o0o00Oo0O - Ii - oO0o + o0ii1I
 if 86 - 86: oOo0O0Ooo / Ii1I * o0ii1I % Ii
 if 20 - 20: IiI1i11I . ii + IiI1i11I + i1iIi * Ii1I
 if 44 - 44: Ii
 if 69 - 69: oooOo0oo0oo * o0o00Oo0O + Ii
 if 65 - 65: o0o00Oo0O / IiI1i11I . ooOoO0O00 * IiI1i11I / iI11I1II1I1I - i1i1I1IIii1II
 if 93 - 93: OOooOOo % Ii - o0ii1I % oO0o
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 if 55 - 55: I11i . Ii1I
 if 63 - 63: i1i1I1IIii1II
 O00oOoo0OoO0 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( Ii11 ) . replace ( ' ' , '+' )
 oo0O0oO0O0O = 'http://onlinemovies.tube/?s=' + ( Ii11 ) . replace ( ' ' , '+' )
 oOo0O = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 I11iIiii1 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I1ii1111Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 79 - 79: Ii1I - i1i1I1IIii1II - I11i . oooOo0oo0oo
 iIiII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 65 - 65: Ii . oO0o % IiI1i11I + III1iiIii - Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 60 - 60: i1IiiiI1iI
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 14 - 14: I1ii11iIi11i % i1i1I1IIii1II * IiI1i11I - Ii / Ii1I * Ii
 if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * Iii + oooOo0oo0oo
 II11IiIi11 = O00O0oOO00O00 ( O00oOoo0OoO0 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( oo0O0oO0O0O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( oOo0O )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( I11iIiii1 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 iiiiiII = O00O0oOO00O00 ( I1ii1111Ii )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 14 - 14: o0ii1I - o0o00Oo0O
 if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
 oOOo = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 oo0oO0 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 45 - 45: i1IiiiI1iI * Iii / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
 if 49 - 49: o0ii1I / IiI1i11I . IiI1i11I . IiI1i11I + Ii % Iii
 if oo0oO0 != 'Failed' :
  IiIiIi1I1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oo0oO0 )
  for iI , iIiIi11 in IiIiIi1I1 :
   IiI1ii1Ii = O00O0oOO00O00 ( iI )
   oooOOOoOOOo0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IiI1ii1Ii )
   for O00oOoo0OoO0 , Ooo0 in oooOOOoOOOo0O :
    if II1i111 in Ooo0 . lower ( ) :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + Ooo0 + '-[COLORgold] source ' + iIiIi11 + '[/COLOR]' ) , iI + O00oOoo0OoO0 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 7 - 7: III1iiIii * i1iIi + OOooOOo
     O0oO0 ( 'tvshows' , 'Media Info 3' )
 if oOOo != 'Failed' :
  oo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOo )
  for iI , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in oo0 :
   if II1i111 in iIiIi11 . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] source HeroVision[/COLOR]' ) , iI , 1016 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 22 - 22: IiI1i11I
    O0oO0 ( 'tvshows' , 'Media Info 3' )
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
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  i1i1IiIi1 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for iI , o00oOOooOOo0o , iIiIi11 , I1iiIiI1iI1I in i1Iii1i1I :
   if II1i111 in iIiIi11 . lower ( ) :
    if 'season' in I1iiIiI1iI1I :
     iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + ' - [COLORred]Source - Tv HUB[/COLOR]' , iI , 90054 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
    if 'episodes' in I1iiIiI1iI1I :
     iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + ' - [COLORred]Source - Tv HUB[/COLOR]' , iI , 90044 , o00oOOooOOo0o , o00oOOooOOo0o , '' )
  for iI in i1i1IiIi1 :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , iI , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 74 - 74: I11i % OOooOOo . IiI1i11I % i1IiiiI1iI . o0o00Oo0O % IIiIiII11i
   O0oO0 ( 'tvshows' , 'Media Info 3' )
 if II11IiIi11 != 'Failed' :
  iIO0O00OOo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11IiIi11 )
  for iI , iIiIi11 , o00oOOooOOo0o in iIO0O00OOo :
   if II1i111 in iIiIi11 . lower ( ) :
    Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( iIiIi11 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , iI , 8022 , o00oOOooOOo0o , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 5 - 5: i1i1I1IIii1II - ii / OOooOOo
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 30 - 30: Iii % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
    if 55 - 55: oO0o
    if 20 - 20: i1iIi * i1IiiiI1iI * I11i - i1iIi
    if 32 - 32: o0ii1I * i1i1I1IIii1II
    if 85 - 85: Ii . oO0o + oO0o
    if 28 - 28: I1ii11iIi11i
    if 62 - 62: I1ii11iIi11i + ii / IiI1i11I
    if 60 - 60: o0ii1I / OOooOOo . Iii % oooOo0oo0oo
    if 61 - 61: o0o00Oo0O . o0ii1I . o0o00Oo0O * Ii * IIiIiII11i / i1IiiiI1iI
 if o00OooOO000 != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for iIiIi11 in I1i11 :
   if II1i111 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( oOo0O + iIiIi11 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 69 - 69: Iii
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  OooOo0oo0O0o00O = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for iIiIi11 in OooOo0oo0O0o00O :
   if II1i111 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( I11iIiii1 + iIiIi11 ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 17 - 17: Iii
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if iiiiiII != 'Failed' :
  ii1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiiiiII )
  for iI , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in ii1ii :
   if II1i111 in iIiIi11 . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '-[COLORgold] Source Scooby[/COLOR]' ) , iI , 1016 , oo00O00oO000o , iII11I1Ii1 , O0O0ooOOO )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 38 - 38: i1IiiiI1iI % oooOo0oo0oo
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 9 - 9: o0o00Oo0O . iI11I1II1I1I
 I1iIII1IiiI = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for i1iiiIii11 in I1iIII1IiiI :
  OOoOOO000O0 = oO0 + i1iiiIii11 + oOoOooOo0o0
  OooOoOOo0oO00 = O00O0oOO00O00 ( OOoOOO000O0 )
  if OooOoOOo0oO00 != 'Failed' :
   I1I1iII1i = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OooOoOOo0oO00 )
   for iIiIi11 , O0O0ooOOO , iI , o00oOOooOOo0o , oOOo0O00o , oO0oOOoo00000 in I1I1iII1i :
    if II1i111 in iIiIi11 . lower ( ) :
     Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgold] - Source Pandoras[/COLOR]' , iI , oO0oOOoo00000 , o00oOOooOOo0o , oOOo0O00o , O0O0ooOOO )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 44 - 44: Ii1I % III1iiIii
     O0oO0 ( 'tvshows' , 'Media Info 3' )
     if 6 - 6: oO0o
     if 82 - 82: iI11I1II1I1I . Iii / III1iiIii / oooOo0oo0oo * IIiIiII11i % i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0O00 ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( Ii11 ) . replace ( ' ' , '+' )
 if 85 - 85: i1IiiiI1iI - Ii1I % I1ii11iIi11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( iI )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 3 - 3: o0o00Oo0O % Ii
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iI , iIiIi11 in i1Iii1i1I :
   if Ii11 in iIiIi11 . lower ( ) :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + iI ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 40 - 40: i1iIi - Ii % Ii1I % oOo0O0Ooo . III1iiIii * oO0o
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
OoOO000OO00 = '{ZH},' ; IIIi = '{IX},' ; i1OOO00oO0O = '{LM},'
if 5 - 5: OOooOOo / oooOo0oo0oo / i1iIi % Ii1I - IIiIiII11i
def OooOO0 ( url ) :
 iI1i = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iI1i )
 for url , iIii , I1iIiiiI1 , iIiIi11 in IIi :
  iIiiiii1i ( ( iIii ) . replace ( 'Sezon' , ' Season ' ) + ( I1iIiiiI1 ) . replace ( 'Bölüm' , ' Episode ' ) + iIiIi11 , url , 8063 , '' )
  if 22 - 22: III1iiIii / iI11I1II1I1I / I11i
  if 19 - 19: ii
  if 95 - 95: o0ii1I . III1iiIii / Iii . Ii . III1iiIii
  if 43 - 43: Ii + I11i % I11i * ii / i1IiiiI1iI
def ii1i ( url ) :
 iI1i = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iI1i )
 for url , iIiIi11 in IIi :
  iiIi1IIiI ( iIiIi11 , url , 222 , '' )
  if 68 - 68: OOooOOo * i1iIi % i1iIi - III1iiIii + o0o00Oo0O * Ii1I
  if 60 - 60: Ii / ooOoO0O00 * oooOo0oo0oo
  if 89 - 89: iI11I1II1I1I * I11i + OOooOOo . Ii + Ii1I
  if 1 - 1: oOo0O0Ooo . Iii . Ii1I
def ii11iI11I111I ( ) :
 if 44 - 44: ooOoO0O00 - Ii1I + Ii1I . Iii / oooOo0oo0oo
 iI1i = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iI1i )
 for iI , o00oOOooOOo0o , iIiIi11 , I1iIiiiI1 in IIi :
  iIiiiii1i ( iIiIi11 + '  -  ' + ( I1iIiiiI1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iI , 8063 , o00oOOooOOo0o )
  if 48 - 48: Ii1I . o0o00Oo0O . oOo0O0Ooo * I11i / IiI1i11I
def oO0OO00o ( ) :
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OOo0 )
 for iI , iIiIi11 , o00oOOooOOo0o in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 8002 , o00oOOooOOo0o )
def oooooOOOO0oOo ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OOo0 )
 for o00oOOooOOo0o , time , url , iIiIi11 , O0iI1I1ii11IIi1 in IIi :
  Iii1I1I11iiI1 ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , time ) , url , 1015 , o00oOOooOOo0o , O0iI1I1ii11IIi1 )
  if 26 - 26: IIiIiII11i + ooOoO0O00
def IiI1IIii ( ) :
 if 13 - 13: Ii . o0o00Oo0O / oooOo0oo0oo * ooOoO0O00
 iIiiiii1i ( 'Coronation Street' , '' , 8001 , '' )
 iIiiiii1i ( 'Eastenders' , '' , 8002 , '' )
 iIiiiii1i ( 'Emmerdale' , '' , 8003 , '' )
 iIiiiii1i ( 'Hollyoaks' , '' , 8004 , '' )
 iIiiiii1i ( 'Im a Celebrity' , '' , 8005 , '' )
 if 14 - 14: III1iiIii + III1iiIii . Iii / o0ii1I . iI11I1II1I1I
 if 10 - 10: IIiIiII11i . oooOo0oo0oo / IiI1i11I
 if 35 - 35: IiI1i11I / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
 if 3 - 3: Ii1I
def I1III1i1Ii ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if 'Holly' in iIiIi11 :
   o00oOOooOOo0o = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iI :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI . replace ( '\\/' , '/' ) , 8006 , o00oOOooOOo0o )
   else :
    pass
    if 79 - 79: Iii * IiI1i11I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 7 - 7: Ii1I . ooOoO0O00 % iI11I1II1I1I
def III111 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if 'East' in iIiIi11 :
   o00oOOooOOo0o = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iI :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI . replace ( '\\/' , '/' ) , 8006 , o00oOOooOOo0o )
   else :
    pass
    if 47 - 47: I1ii11iIi11i * i1IiiiI1iI % I11i . I1ii11iIi11i + oOo0O0Ooo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: oooOo0oo0oo / oO0o + oooOo0oo0oo * ii - ooOoO0O00
def iIIiii1ii ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if 'Emmer' in iIiIi11 :
   o00oOOooOOo0o = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iI :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI . replace ( '\\/' , '/' ) , 8006 , o00oOOooOOo0o )
   else :
    pass
    if 15 - 15: iI11I1II1I1I + IiI1i11I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 35 - 35: IIiIiII11i % oooOo0oo0oo . i1i1I1IIii1II * i1iIi
def o0O00ooo0oO0o ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if 'Coro' in iIiIi11 :
   o00oOOooOOo0o = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iI :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI . replace ( '\\/' , '/' ) , 8006 , o00oOOooOOo0o )
   else :
    pass
    if 21 - 21: iI11I1II1I1I / i1iIi * i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: o0o00Oo0O + I11i
def i11iIIII1II11Iii ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for iI , iIiIi11 in IIi :
  if 'Celeb' in iIiIi11 :
   o00oOOooOOo0o = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iI :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iI . replace ( '\\/' , '/' ) , 8006 , o00oOOooOOo0o )
   else :
    pass
    if 46 - 46: o0ii1I * o0ii1I / i1i1I1IIii1II * i1IiiiI1iI
def iI1I1I ( name , url ) :
 OoiII1I1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if OoiII1I1 :
  OoO0O = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OOo0 = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( OOo0 ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OOo0 = open_url ( url )
  II1i1iI1 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( OOo0 ) [ - 1 ]
  OoO0O = II1i1iI1 . replace ( '\\/' , '/' )
 IIiiii = xbmcgui . ListItem ( name , '' , '' )
 IIiiii . setPath ( OoO0O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIiiii )
 if 14 - 14: i1iIi % I1ii11iIi11i / i1IiiiI1iI
 if 29 - 29: oooOo0oo0oo * ooOoO0O00 - i1IiiiI1iI * oOo0O0Ooo % oOo0O0Ooo / Iii
def I1i1 ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iI , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for iI , iIiIi11 in i1Iii1i1I :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iI , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 69 - 69: I11i
def o00ooOOo0ooO0 ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  if 'Movies' in iIiIi11 :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.snagfilms.com' + ( iI ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def I11i1I1 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOo0 )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OOo0 )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00oOOooOOo0o )
 for url in i1Iii1i1I :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 5 - 5: ii - IiI1i11I - Ii
  if 53 - 53: IiI1i11I * oO0o / Ii1I + oOo0O0Ooo + ii
def oO0OoO00o ( url ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , url , o00oOOooOOo0o in IIi :
  if '{{' in iIiIi11 :
   pass
  else :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , o00oOOooOOo0o )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
iIi11111i1II = '{UJ},' ; ooooo = '{WE},' ; OooO00 = '{WP},' ; O00 = '{PP},'
def iIi1i1Ii1 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , url , o00oOOooOOo0o in IIi :
  if '{{' in iIiIi11 :
   pass
  else :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00oOOooOOo0o )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00O0O ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 for url in IIi :
  iI1I ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1I ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 70 - 70: i1i1I1IIii1II - Ii
 if 37 - 37: III1iiIii % o0ii1I % ooOoO0O00
 if 23 - 23: i1iIi - o0o00Oo0O + Ii
def oO0ooOoOooO00o00 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  if '(cooltvseries.com)' in iIiIi11 :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , iIiIi11 in i1Iii1i1I :
  if '(cooltvseries.com)' in iIiIi11 :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def o0Ooo00Oo0oo0 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OOo0 )
 for url in IIi :
  iiiIi ( ( url ) . replace ( ' ' , '%20' ) )
I11Oo0O00O0O00 = '{XX},' ; II1I1i = '{UD},' ; O00OoOo0OooOo = '{YT},' ; OOooOoOOo0O = '{JS},' ; IIi11ii = '{PF},'
if 57 - 57: oooOo0oo0oo * oO0o + o0o00Oo0O % i1IiiiI1iI - oOo0O0Ooo
def ii1IiiIIiIiii ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OOo0 )
 for iI , iIiIi11 , o00oOOooOOo0o in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( iI ) ) , 222 , o00oOOooOOo0o )
  if 44 - 44: Ii
def oooo0oOOoO000 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OOo0 )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OOo0 )
 for o00oOOooOOo0o , url , iIiIi11 in IIi :
  if 'youtu' in url :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + o00oOOooOOo0o )
 for url in next :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 63 - 63: Iii . oOo0O0Ooo . Ii1I * o0ii1I
def IIIIII ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OOo0 )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 22 - 22: OOooOOo
def i1iI1i111 ( url ) :
 OOo0 = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 222 , o00oOOooOOo0o )
  if 54 - 54: I1ii11iIi11i - i1IiiiI1iI * i1IiiiI1iI
  if 69 - 69: oOo0O0Ooo % o0o00Oo0O . oOo0O0Ooo % i1iIi / o0ii1I % i1i1I1IIii1II
  if 19 - 19: Ii
  if 13 - 13: IiI1i11I
  if 78 - 78: i1iIi + OOooOOo - i1IiiiI1iI
def IIoOOOO ( ) :
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % oooOo0oo0oo + III1iiIii . oO0o . I1ii11iIi11i
 iIiiiii1i ( 'All Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'Entertainment' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'Movies' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'Music' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'News' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'Sports' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'Documentary' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'Kids' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'Food' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'Religious' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'USA Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iIiiiii1i ( 'Other' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 if 70 - 70: Iii . Ii1I * i1i1I1IIii1II
 if 97 - 97: i1i1I1IIii1II . iI11I1II1I1I - oooOo0oo0oo
def iI1iIiiIii ( Cat_Name ) :
 if 99 - 99: i1IiiiI1iI - Ii1I - oOo0O0Ooo - i1IiiiI1iI + oO0o + IIiIiII11i
 i11iii1II1I1 = False
 IiIi11iI1IIi = '0'
 if Cat_Name == 'All Channels' : i11iii1II1I1 = True
 if Cat_Name == 'Entertainment' : IiIi11iI1IIi = '1'
 if Cat_Name == 'Movies' : IiIi11iI1IIi = '2'
 if Cat_Name == 'Music' : IiIi11iI1IIi = '3'
 if Cat_Name == 'News' : IiIi11iI1IIi = '4'
 if Cat_Name == 'Sports' : IiIi11iI1IIi = '5'
 if Cat_Name == 'Documentary' : IiIi11iI1IIi = '6'
 if Cat_Name == 'Kids' : IiIi11iI1IIi = '7'
 if Cat_Name == 'Food' : IiIi11iI1IIi = '8'
 if Cat_Name == 'Religious' : IiIi11iI1IIi = '9'
 if Cat_Name == 'USA Channels' : IiIi11iI1IIi = '10'
 if Cat_Name == 'Other' : IiIi11iI1IIi = '11'
 if 5 - 5: i1i1I1IIii1II + OOooOOo
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OOo0 )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for iIiIi11 , o00oOOooOOo0o , OO0O0oooo0 in IIi :
  ooOoo0OoO0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00oOOooOOo0o ) . replace ( '\\' , '' )
  if OO0O0oooo0 == IiIi11iI1IIi :
   iIiiiii1i ( iIiIi11 , '' , 7022 , ooOoo0OoO0 )
  elif i11iii1II1I1 == True :
   iIiiiii1i ( iIiIi11 , '' , 7022 , ooOoo0OoO0 )
  else : pass
  if 38 - 38: III1iiIii - ooOoO0O00 . Ii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 28 - 28: i1IiiiI1iI / i1i1I1IIii1II . Ii1I
def oOoo0O00OO ( Search_Name ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OOo0 )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OOo0 )
 for o00oOOooOOo0o , iI , oo0O0oO0O0O , oOo0O in IIi :
  ooOoo0OoO0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00oOOooOOo0o ) . replace ( '\\' , '' )
  iiIi1IIiI ( Search_Name + ': Link 1' , ( iI ) . replace ( '\\' , '' ) , 222 , ooOoo0OoO0 )
  iiIi1IIiI ( Search_Name + ': Link 2' , ( oo0O0oO0O0O ) . replace ( '\\' , '' ) , 222 , ooOoo0OoO0 )
  iiIi1IIiI ( Search_Name + ': Link 3' , ( oOo0O ) . replace ( '\\' , '' ) , 222 , ooOoo0OoO0 )
  if 20 - 20: IiI1i11I - Ii1I * IiI1i11I + i1IiiiI1iI
def OOoooiII1 ( ) :
 OOo0 = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OOo0 )
 for iIiIi11 , iI in IIi :
  iiIi1IIiI ( iIiIi11 , ( iI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def ii1i1iIiIIi ( ) :
 OOo0 = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OOo0 )
 for iIiIi11 , iI in IIi :
  iiIi1IIiI ( iIiIi11 , ( iI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def iI11I11i ( ) :
 OOo0 = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OOo0 )
 for iIiIi11 , iI in IIi :
  iiIi1IIiI ( iIiIi11 , ( iI ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 80 - 80: Iii - Ii1I * o0ii1I / ii * o0o00Oo0O % oooOo0oo0oo
def Iiooo000o0OoOo ( url ) :
 url
 iII1i11 = xbmcgui . ListItem ( iIiIi11 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1i11 )
 return
 if 76 - 76: o0ii1I % iI11I1II1I1I / i1i1I1IIii1II * iI11I1II1I1I / iI11I1II1I1I
 if 41 - 41: III1iiIii / ooOoO0O00 / OOooOOo / oooOo0oo0oo . oO0o % OOooOOo
def ooOO0o0ooOo0 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OOo0 )
 for url , O0O0ooOOO , o00oOOooOOo0o , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + o00oOOooOOo0o , '' , ( O0O0ooOOO ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  O0oO0 ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  iIiiiii1i ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 18 - 18: o0ii1I - IiI1i11I
def i11iI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , O0O0ooOOO , o00oOOooOOo0o in IIi :
  I1I1i1I ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + o00oOOooOOo0o , '' , O0O0ooOOO )
  O0oO0 ( 'tvshows' , 'Media Info 3' )
 o0ooo0oooO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I111iIii1i1 in o0ooo0oooO :
  oo0o = ( I111iIii1i1 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  Iii1I1I11iiI1 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + o00oOOooOOo0o , '' , oo0o )
  if 6 - 6: i1IiiiI1iI % III1iiIii / o0ii1I + i1IiiiI1iI . i1i1I1IIii1II
def oo0O0 ( INFO ) :
 IiII111i1i11 ( 'info for workout' , INFO )
 if 93 - 93: I1ii11iIi11i
 if 55 - 55: ii * i1i1I1IIii1II % III1iiIii + o0o00Oo0O
 if 16 - 16: Ii1I % I1ii11iIi11i % IIiIiII11i % IIiIiII11i
def OOOO0oooooO0o ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iIiiiii1i ( ( iIiIi11 ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def O00o00o0 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , url , 9032 , iiIi1IIiIi + 'icon.png' )
def o00OOOOoOO ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  if '=' in iIiIi11 :
   pass
  else :
   iiIi1IIiI ( ( iIiIi11 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def OooOoOoo0ooo0 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  if '=' in iIiIi11 :
   pass
  else :
   iiIi1IIiI ( iIiIi11 , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 69 - 69: I1ii11iIi11i * i1iIi
   if 91 - 91: I11i . i1iIi / oO0o / Ii * I11i
   if 52 - 52: oOo0O0Ooo - Ii / III1iiIii . i1i1I1IIii1II
def II1i1I ( url ) :
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , iiIi1IIiIi + 'bamf.png' )
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  if 'mp4' in url :
   pass
  else :
   iiIi1IIiI ( ( iIiIi11 ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOo0Oo ( url ) :
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , iiIi1IIiIi + 'bamf.png' )
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  if 'mp4' in url :
   iiIi1IIiI ( ( iIiIi11 ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: OOooOOo * o0ii1I
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
 if 81 - 81: oooOo0oo0oo
def OooOooo00OOO0o ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  if 'Daily' in iIiIi11 :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 9008 , O0O )
def II1iIIiIII ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( OOo0 )
 for url in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def iI1 ( url ) :
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  iiIi1IIiI ( ( iIiIi11 ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 5 - 5: III1iiIii - Iii
def I1iOoO00O ( ) :
 OOo0 = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  if '.m3u' in iI :
   iIiiiii1i ( ( iIiIi11 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + iI ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def O0oo0ooO ( url ) :
 OOo0 = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  iiIi1IIiI ( ( iIiIi11 ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 6 - 6: iI11I1II1I1I / IiI1i11I
def I1IIIiIiIi ( ) :
 OOo0 = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  if 'category' in iI :
   iIiiiii1i ( iIiIi11 , 'http://www.disclose.tv/' + iI , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 1 - 1: i1IiiiI1iI / OOooOOo * OOooOOo - I11i % o0ii1I
   if 96 - 96: III1iiIii / o0ii1I % oO0o . iI11I1II1I1I
def i1Iiiiiii ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OOo0 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OOo0 )
 for url , iIiIi11 , o00oOOooOOo0o in IIi :
  iIiiiii1i ( iIiIi11 , 'http://www.disclose.tv/' + url , 7011 , o00oOOooOOo0o )
 for url in next :
  iIiiiii1i ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 62 - 62: iI11I1II1I1I % i1IiiiI1iI % Ii1I * III1iiIii
  if 87 - 87: III1iiIii
def II1i1i ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OOo0 )
 I1i11 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OOo0 )
 for url in IIi :
  if 'http' in url :
   iiIi1IIiI ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , iIiIi11 in i1Iii1i1I :
  iiIi1IIiI ( iIiIi11 , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in I1i11 :
  iiIi1IIiI ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 17 - 17: I11i . III1iiIii . Ii + ii % Ii
  if 1 - 1: I11i % I1ii11iIi11i / Ii * oOo0O0Ooo - ooOoO0O00 / I11i
def IIiI1i11iIII1 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 76 - 76: ii * III1iiIii - I11i * oooOo0oo0oo * ooOoO0O00 * IiI1i11I
def II11111i ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1i1iI1i = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIIo00o = len ( i1i1iI1i )
 if 48 - 48: i1IiiiI1iI % i1iIi . I1ii11iIi11i + oO0o - i1i1I1IIii1II
 if 38 - 38: III1iiIii . iI11I1II1I1I - IIiIiII11i - o0ii1I
 if IIIo00o == 1 :
  for oOOOo0O in i1i1iI1i :
   oOOOo0O = oOOOo0O . replace ( 'player' , 'watch' )
   OoOo000o = oOOOo0O + '&fv=&sou='
   iIIi1IiiiII1i = OooOoooOo ( OoOo000o )
   IIiIii1iiI = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( iIIi1IiiiII1i )
   for I1II in IIiIii1iiI :
    o0oOOOOOO = False
    Resolve ( I1II )
    if 31 - 31: I1ii11iIi11i / Ii1I - o0o00Oo0O + IiI1i11I - IiI1i11I
 elif IIIo00o > 1 :
  if 85 - 85: OOooOOo
  for oOOOo0O in i1i1iI1i :
   iIII1iI1Iii1i = OooOoooOo ( oOOOo0O )
   Ooo00ooOOoOo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iIII1iI1Iii1i )
   ooO0o0Oo = Ooo00ooOOoOo
   ooO0o0Oo = ( str ( ooO0o0Oo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + ooO0o0Oo
   iiIi1IIiI ( 'DOUBLE LINK' , ooO0o0Oo , 424 , '' )
   if 67 - 67: OOooOOo
   for url in Ooo00ooOOoOo :
    iIiiiii1i ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     oo0O0oO0O0O = Google . resolve ( url )
    except :
     pass
    try :
     OOO0o0oo00 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( oo0O0oO0O0O ) )
     for o000 , IIIi1IiI1iII in OOO0o0oo00 :
      if 85 - 85: Ii1I + OOooOOo - Ii % OOooOOo . i1i1I1IIii1II + Ii
      HD_URLS . append ( o000 )
      SD_URLS . append ( IIIi1IiI1iII )
    except :
     pass
 else :
  pass
  if 12 - 12: III1iiIii + ooOoO0O00 . oOo0O0Ooo * iI11I1II1I1I * Ii1I
def i1I11Iiii ( ) :
 if 78 - 78: i1IiiiI1iI
 if 62 - 62: oOo0O0Ooo + ii + i1IiiiI1iI
 iIiiiii1i ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 19 - 19: ooOoO0O00 / oooOo0oo0oo - Ii + OOooOOo
 iIiiiii1i ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 49 - 49: oooOo0oo0oo - Ii1I / i1i1I1IIii1II
 if 33 - 33: IiI1i11I
def i1ooo00o0OO0 ( ) :
 OOo0 = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , 'http://cnfstudio.com/genre/' + iI , 7003 , iiIi1IIiIi + 'icon.png' )
  if 94 - 94: Iii
iIii1 = xbmcgui . Dialog ( )
if 48 - 48: i1i1I1IIii1II - ii + I11i % ooOoO0O00 - oOo0O0Ooo + oooOo0oo0oo
oo0O0oO0o = '{UN},' ; iIIiiI1II = '{IG},' ; i11i1IIi = '{PL},' ; Oo0o = '{LO},' ; iiiii11i = '{LP},' ; OOoOOo0o0OOo0 = '{HA},' ; iiiI11I = '{XD},' ; OOoi1I1I = '{TA},' ; iIiiiIII1II = '{DP},' ; oO00oOOOO = '{JT},' ; o0o0OOO0ooo00 = '{JJ},' ; I11III111i1I = '{MM},' ; O0ooOO0O00 = '{FQ},' ; OOO0O = '{HH},'
if 9 - 9: oOo0O0Ooo
def o0000oO0OOOo0 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OOo0 )
 o00ooo0O = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OOo0 )
 for o00oOOooOOo0o , url , iIiIi11 in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , o00oOOooOOo0o )
 o00ooo0O = o00ooo0O
 for url in o00ooo0O :
  iIiiiii1i ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 54 - 54: Ii1I * III1iiIii
def I11I11III ( url ) :
 if 15 - 15: Ii1I * o0ii1I / IiI1i11I . I11i / o0ii1I % OOooOOo
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OOo0 )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  Oo0o0ooOo0 = OoOoo0ooO0000 ( iiI111I1iIiI )
  ii1iiI11III1 = OoOoo0ooO0000 ( url )
  if 8 - 8: Ii1I - ooOoO0O00 - i1i1I1IIii1II / i1i1I1IIii1II % I11i
  if 98 - 98: oO0o * i1iIi + ooOoO0O00 + III1iiIii - ooOoO0O00 % OOooOOo
def OoOoo0ooO0000 ( url ) :
 if 19 - 19: iI11I1II1I1I * I1ii11iIi11i / oooOo0oo0oo
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( OOo0 )
 for url in IIi :
  O0OOO00 ( url )
  if 5 - 5: I11i
  if 24 - 24: III1iiIii + oO0o - o0ii1I
def iiIIii1Iii1I ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 95 - 95: I11i / i1IiiiI1iI % IIiIiII11i + i1iIi
def oOo0ooOO0O ( ) :
 if os . path . exists ( II ) :
  IIIII11IIi = open ( II , 'r' )
  for iII1i11 in IIIII11IIi :
   i11I1iiI1iI = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iII1i11 )
   for iIiIi11 , iI in i11I1iiI1iI :
    iiIi1IIiI ( iIiIi11 , iI , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 46 - 46: i1iIi / iI11I1II1I1I
def OO0oOO0o000 ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = o0O0Oo00 ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIiIi11 , url in IIi :
   url = ( url ) . strip ( )
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 99 - 99: IiI1i11I % o0ii1I % Ii % ooOoO0O00 / I11i
  if 53 - 53: OOooOOo
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for iI in IIi :
  iI = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + iI
 iIiIi11 = 'plugin.video.GenieTv'
 if 55 - 55: i1iIi % ooOoO0O00 / oO0o
 oo0OOo0o000 ( iI , iIiIi11 )
 if 19 - 19: iI11I1II1I1I
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for iI in IIi :
  iI = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + iI
 iIiIi11 = 'repository.GenieTv'
 if 27 - 27: IIiIiII11i . oooOo0oo0oo
 oo0OOo0o000 ( iI , iIiIi11 )
 if 18 - 18: i1i1I1IIii1II * I1ii11iIi11i % Ii + o0o00Oo0O % oooOo0oo0oo . oooOo0oo0oo
 if 84 - 84: ii - I1ii11iIi11i
def Ii1IIiI1i ( ) :
 oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , oOI1Ii1I1 )
 if IiII111iI1ii1 == 0 :
  OoOOoOo0O ( )
 if IiII111iI1ii1 == 1 :
  II111IiiiI ( )
  if 30 - 30: IIiIiII11i
  if 27 - 27: ooOoO0O00 - iI11I1II1I1I + o0o00Oo0O % I1ii11iIi11i / oooOo0oo0oo + ooOoO0O00
  if 48 - 48: I1ii11iIi11i
  if 70 - 70: ii * Ii
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
O0OooOoOOoooO00oO = 'https://addons.tvaddons.ag/'
if 62 - 62: o0ii1I
def II111IiiiI ( ) :
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 IIIIIIi1IIi1I11i = 'https://addons.tvaddons.ag/search/?keyword=' + II1i111
 II11iIiIIIiI = OooOoooOo ( IIIIIIi1IIi1I11i )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for iI , oOo00 , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , iI , 10054 , 'https://addons.tvaddons.ag/' + oOo00 , Oo00OOOOO , '' )
  if 4 - 4: iI11I1II1I1I . I1ii11iIi11i - Ii
  if 51 - 51: OOooOOo - Ii / oOo0O0Ooo % o0ii1I * o0ii1I % i1iIi
def OoOOoOo0O ( ) :
 II11iIiIIIiI = OooOoooOo ( O0OooOoOOoooO00oO )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for iI , o00oOOooOOo0o , iIiIi11 in IIi :
  if 'Repositories' in iIiIi11 :
   pass
  elif 'Services' in iIiIi11 :
   pass
  elif 'International' in iIiIi11 :
   pass
  else :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , iI , 10053 , 'https://addons.tvaddons.ag/' + o00oOOooOOo0o , Oo00OOOOO , '' )
   if 12 - 12: i1iIi % OOooOOo
   if 1 - 1: o0o00Oo0O / i1iIi
def Addon ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIiIIIiiI = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  if 'Please' in iIiIi11 :
   pass
  else :
   I1I1i1I ( iIiIi11 , url , 10054 , 'https://addons.tvaddons.ag/' + o00oOOooOOo0o , Oo00OOOOO , '' )
 for url in iiIiIIIiiI :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
  if 83 - 83: o0ii1I / ii * i1i1I1IIii1II . oOo0O0Ooo . ooOoO0O00
  if 59 - 59: Iii . Iii * oOo0O0Ooo - o0ii1I % OOooOOo
def IiIIIiI11i1 ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   IiIi11iI = os . path . join ( oO0O00oOOoooO , name + '.zip' )
   try :
    os . remove ( IiIi11iI )
   except :
    pass
   downloader . download ( url , IiIi11iI , o0oOoO00o )
   Oo0O00O000 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print Oo0O00O000
   print '======================================='
   extract . all ( IiIi11iI , Oo0O00O000 , o0oOoO00o )
   ooI1111i ( )
   if 14 - 14: I1ii11iIi11i % iI11I1II1I1I - iI11I1II1I1I . iI11I1II1I1I - I11i * i1IiiiI1iI
def oo0OOo0o000 ( url , name ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , name + '.zip' )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( url , IiIi11iI , o0oOoO00o )
 Oo0O00O000 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print Oo0O00O000
 print '======================================='
 extract . all ( IiIi11iI , Oo0O00O000 , o0oOoO00o )
 ooI1111i ( )
 if 10 - 10: oO0o - IIiIiII11i % I11i - OOooOOo + oO0o
def ooI1111i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 88 - 88: iI11I1II1I1I % i1iIi + I11i * OOooOOo / Iii . oO0o
 if 66 - 66: iI11I1II1I1I * IIiIiII11i . iI11I1II1I1I * Ii + Iii + o0ii1I
def OoO0ooooOOo0o ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOo0 )
 for url , oOo00 , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , url , 1007 , oOo00 )
def iIii1iii1I1ii ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOo0 )
 for url , oOo00 , iIiIi11 in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 1006 , oOo00 )
  if 91 - 91: ooOoO0O00
def iIiIiiiII11i ( ) :
 OOo0 = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( OOo0 )
 for iI , oo00O00oO000o , O0O0ooOOO , oOOo0O00o , iIiIi11 in IIi :
  I1oO0oO00OO00 ( iIiIi11 , 100109 , iI , image = oo00O00oO000o , isFolder = True )
  if 75 - 75: I11i + oOo0O0Ooo % i1iIi * i1IiiiI1iI
def Oooo000 ( url ) :
 import random
 Ooo0o0o = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 Ooo0o0o . clear ( )
 OoO00o = [ ]
 o0oOoii = [ ]
 oOoooo0OooO = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oo0O0oO0O0O , oo00O00oO000o , O0O0ooOOO , oOOo0O00o , iIiIi11 in IIi :
  OoO00o . append ( [ oo0O0oO0O0O , iIiIi11 ] )
  if len ( OoO00o ) == len ( IIi ) :
   for iII1i11 in OoO00o :
    OO00O = random . randint ( 1 , len ( OoO00o ) )
    try :
     iiO0OoO0OOO00 = OoO00o [ int ( OO00O ) ]
    except :
     pass
    if len ( o0oOoii ) <= 20 :
     if iiO0OoO0OOO00 [ 1 ] not in oOoooo0OooO :
      o0o = OooOoooOo ( iiO0OoO0OOO00 [ 0 ] )
      I1i11 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for IIIiii1I , ii1iiii11IiI1 in I1i11 :
       OOoOoo = OooOoooOo ( IIIiii1I )
       OooOo0oo0O0o00O = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for O0OoO0ooOoo , iiI111I1iIiI in OooOo0oo0O0o00O :
        if 'panda' in iiI111I1iIiI :
         OOoO = OooOoooOo ( iiI111I1iIiI )
         OoOOo = re . compile ( "url: '(.+?)'" ) . findall ( OOoO )
         for iII in OoOOo :
          if 'http' in iII :
           IIiiii = xbmcgui . ListItem ( iiO0OoO0OOO00 [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : iiO0OoO0OOO00 [ 1 ] } )
           IIiiii . setProperty ( "IsPlayable" , "true" )
           Ooo0o0o . add ( iII , IIiiii )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IIiiii )
           if 46 - 46: Iii
def I1oO0oO00OO00 ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 IIiIii = sys . argv [ 0 ]
 IIiIii += '?mode=' + str ( mode )
 IIiIii += '&title=' + urllib . quote_plus ( name )
 IIiIii += '&image=' + urllib . quote_plus ( image )
 IIiIii += '&page=' + str ( page )
 if url != '' :
  IIiIii += '&url=' + urllib . quote_plus ( url )
 if keyword :
  IIiIii += '&keyword=' + urllib . quote_plus ( keyword )
 IIiiii = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  IIiiii . addContextMenuItems ( contextMenu )
 if infoLabels :
  IIiiii . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  IIiiii . setProperty ( "IsPlayable" , "true" )
 IIiiii . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = isFolder )
 if 75 - 75: iI11I1II1I1I * Iii
 if 93 - 93: iI11I1II1I1I + IIiIiII11i - I11i
def i1i1I111iIi1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOo0 )
 for url , iconimage , O0O0ooOOO , oOOo0O00o , name in IIi :
  if 'http' in url :
   if '.php' in url :
    oOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for iII1i11 in oOo0 :
     if iII1i11 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    O00o0 ( name , url , 1016 , iconimage , oOOo0O00o , O0O0ooOOO )
   else :
    if 'youtube' in url :
     oOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in oOo0 :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O0O00O ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , oOOo0O00o , O0O0ooOOO )
    else :
     oOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in oOo0 :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     O0O00O ( name , url , 222 , iconimage , oOOo0O00o , O0O0ooOOO )
     O0oO0 ( 'tvshows' , 'Media Info 3' )
  else :
   i1i1111 ( url , iconimage , name )
   if 32 - 32: oOo0O0Ooo * iI11I1II1I1I / i1iIi + IIiIiII11i * IiI1i11I
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOo0 )
  for url , oOo00 , name in IIi :
   if 'http' in url :
    if '.php' in url :
     iIiiiii1i ( name , url , 1016 , oOo00 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      iiIi1IIiI ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 )
     else :
      oOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in oOo0 :
       if iII1i11 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      iiIi1IIiI ( name , url , 222 , oOo00 )
      O0oO0 ( 'tvshows' , 'Media Info 3' )
   else :
    i1i1111 ( url , oOo00 , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 3 - 3: Ii / Iii + ooOoO0O00 - Iii
def i1i1111 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 iIII = ( url ) . replace ( IIIi , 'http' ) . replace ( II1I1i , '.com' ) ;
 i11iI1I1I11II = ( iIII ) . replace ( i1OOO00oO0O , 'a' ) . replace ( I11iiI1i , 'b' ) . replace ( ooOoOO , 'c' ) . replace ( ooooo , 'd' ) . replace ( i11i1IIi , 'e' ) . replace ( oO00oOOOO , 'f' ) ;
 oo0O00O0oO = ( i11iI1I1I11II ) . replace ( I11Oo0O00O0O00 , 'g' ) . replace ( OOoOOo0o0OOo0 , 'h' ) . replace ( O00OoOo0OooOo , 'i' ) . replace ( IIi11ii , 'j' ) . replace ( iIiiII11 , 'k' ) . replace ( OOo0oo0 , 'l' ) ;
 IIIIi1iII = ( oo0O00O0oO ) . replace ( ii1oO0Oo , 'm' ) . replace ( iIi1IIIi1Ii , 'n' ) . replace ( Ii1IiIIIi1i , 'o' ) . replace ( II111Ii1I1I , 'p' ) . replace ( o00oo0oOo0o0 , 'q' ) . replace ( i1Ii1 , 'r' ) ;
 i1I1ii1iI1 = ( IIIIi1iII ) . replace ( OoI1Ii , 's' ) . replace ( OooO00 , 't' ) . replace ( IIIII1iII1 , 'u' ) . replace ( OO0oOoO0O0 , 'v' ) . replace ( iiiI1i , 'w' ) . replace ( O0OooO00O0 , 'x' ) ;
 iiI1i111I1 = ( i1I1ii1iI1 ) . replace ( iiIi11i1I1 , 'y' ) . replace ( o0OoO0 , 'z' ) . replace ( oo0O0oO0o , '.' ) . replace ( iIIiiI1II , '(' ) . replace ( Oo0o , ')' ) . replace ( iiiii11i , '/' ) ;
 I11Ii1I1I = ( iiI1i111I1 ) . replace ( OoOO000OO00 , '1' ) . replace ( O00 , '2' ) . replace ( oo00OO0o0 , '3' ) . replace ( OOoi1I1I , '4' ) . replace ( iIiiiIII1II , '5' ) . replace ( OOooOoOOo0O , '6' ) ;
 o0oo0000Oo = ( I11Ii1I1I ) . replace ( o0o0OOO0ooo00 , '7' ) . replace ( I11III111i1I , '8' ) . replace ( O0ooOO0O00 , '9' ) . replace ( OOO0O , '0' ) . replace ( o0oOo , ':' ) . replace ( II1oOO0O0Ooo0 , '%' ) ;
 url = ( o0oo0000Oo ) . replace ( iIi11111i1II , '-' ) . replace ( iiiI11I , '_' ) ;
 iiIi1IIiI ( name , url , 222 , iconimage ) ;
 if 93 - 93: i1iIi + i1iIi
 if 65 - 65: ii * Iii * i1i1I1IIii1II % Ii1I * IIiIiII11i
def Oo00 ( ) :
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOo0 )
 for iI , oOo00 , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , iI , 1007 , oOo00 )
def OoooOoOO0OO ( url ) :
 if 30 - 30: oooOo0oo0oo / III1iiIii * I11i / oOo0O0Ooo . IiI1i11I
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOo0 )
 for url , oOo00 , iIiIi11 in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 1006 , oOo00 )
  if 89 - 89: IIiIiII11i + i1iIi
def II1iiI11i ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OOOiII1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OOOiII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOiII1 )
 if 55 - 55: oO0o
 if 50 - 50: Ii1I . OOooOOo % I1ii11iIi11i . III1iiIii . i1i1I1IIii1II
def i1I1i1I111 ( url ) :
 OOo0 = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OOo0 )
 for url , o00oOOooOOo0o , iIiIi11 in IIi :
  if '-dir-' in iIiIi11 :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , o00oOOooOOo0o )
  else :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' , url , 1006 , o00oOOooOOo0o )
   if 77 - 77: ooOoO0O00 + ii + oO0o % i1iIi % o0ii1I
def iIIiII11I11I1i ( url ) :
 OOo0 = o0O0Oo00 ( url )
 iiiIOoOooOo0 = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  if '[To Parent Directory]' in iIiIi11 :
   iIiIi11 = 'HOME'
   pass
  elif 'HOME' in iIiIi11 :
   pass
  elif '.m3u' in iIiIi11 :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , iiiIOoOooOo0 + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in iIiIi11 :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , iiiIOoOooOo0 + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in iIiIi11 :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , iiiIOoOooOo0 + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) , iiiIOoOooOo0 + url , 1012 , iiIi1IIiIi + 'music.png' )
def I1iIiiIiiIIiI ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00oOOooOOo0o , iIiIi11 , url in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 7 - 7: oOo0O0Ooo / i1iIi % oO0o + i1i1I1IIii1II . I11i / Iii
def O0oo0O ( url ) :
 OOo0 = o0O0Oo00 ( url )
 iiiIOoOooOo0 = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  if '.mp3' in iIiIi11 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '/' , '' ) , iiiIOoOooOo0 + url , 1011 , iiIi1IIiIi + 'music.png' )
def I111 ( ) :
 OOo0 = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OOo0 )
 for iI , o00oOOooOOo0o , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , ( 'http://www.cyn.net/music/' + iI ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + o00oOOooOOo0o ) . replace ( ' ' , '%20' ) )
def iIOO00o0O ( url , img ) :
 OOo0 = o0O0Oo00 ( url )
 oo0O0oO0O0O = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( oo0O0oO0O0O + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 26 - 26: ii
def Oo00o00Oo ( url ) :
 OOo0 = o0O0Oo00 ( url )
 oo0O0oO0O0O = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OOo0 )
 for type , url , iIiIi11 in IIi :
  if '[VID]' in type :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , oo0O0oO0O0O + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   Oo00o00Oo ( oo0O0oO0O0O + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66: Iii + I11i
 if 89 - 89: IIiIiII11i + o0o00Oo0O + Iii
def oOo00OO0ooOOO ( ) :
 II1i11i1iIi11 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 Ii11 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 II1i111 = Ii11 . lower ( )
 iI = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 O00oOoo0OoO0 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 oo0O0oO0O0O = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 3 - 3: iI11I1II1I1I - ooOoO0O00 / IiI1i11I + ooOoO0O00 + o0o00Oo0O
 II11iIiIIIiI = O00O0oOO00O00 ( iI )
 II11IiIi11 = O00O0oOO00O00 ( O00oOoo0OoO0 )
 o0o = O00O0oOO00O00 ( oo0O0oO0O0O )
 if 18 - 18: iI11I1II1I1I . IiI1i11I % oooOo0oo0oo % i1i1I1IIii1II + iI11I1II1I1I * ii
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for iI , oo00O00oO000o , O0O0ooOOO , iII11I1Ii1 , iIiIi11 in IIi :
   if Ii11 in iIiIi11 . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , iI , 1016 , oo00O00oO000o , oOOo0O00o , O0O0ooOOO )
    if 78 - 78: III1iiIii
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if II11IiIi11 != 'Failed' :
  iIO0O00OOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11IiIi11 )
  for iI , iIiIi11 in iIO0O00OOo :
   if Ii11 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + iI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 38 - 38: oO0o * Ii1I
    O0oO0 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for iI , iIiIi11 in i1Iii1i1I :
   if Ii11 in iIiIi11 . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + iI ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 4 - 4: oO0o . Ii1I
    O0oO0 ( 'tvshows' , 'Media Info 3' )
    if 21 - 21: Ii / oO0o / Ii1I * o0o00Oo0O - IIiIiII11i * oooOo0oo0oo
    if 27 - 27: I11i . OOooOOo * o0ii1I * IiI1i11I * o0o00Oo0O
    if 93 - 93: III1iiIii % i1IiiiI1iI % IIiIiII11i
    if 20 - 20: ii * i1IiiiI1iI
    if 38 - 38: IiI1i11I . ii
    if 28 - 28: i1IiiiI1iI * ooOoO0O00 . Ii1I
ii1oO0Oo = '{SF},' ; iIi1IIIi1Ii = '{IF},' ; Ii1IiIIIi1i = '{PW},' ; oo00OO0o0 = '{AM},' ; II111Ii1I1I = '{GF},' ; o00oo0oOo0o0 = '{DD},' ; i1Ii1 = '{UO},' ; OoI1Ii = '{LE},' ; IIIII1iII1 = '{ZY},' ; OO0oOoO0O0 = '{UE},' ; iiiI1i = '{PE},' ; O0OooO00O0 = '{JE},' ; iiIi11i1I1 = '{TH},' ; o0OoO0 = '{LK},'
if 75 - 75: o0o00Oo0O / i1i1I1IIii1II * i1iIi - oooOo0oo0oo / ooOoO0O00
if 61 - 61: Iii
def o00oOoOo0 ( ) :
 OOo0 = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , iI , 8021 , iiIi1IIiIi + 'iwatch.png' )
  O0oO0 ( 'movies' , 'MAIN' )
def oo0oOOo0 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OOo0 )
 for url , iIiIi11 , ii11I1 in IIi :
  iIiiiii1i ( iIiIi11 + ii11I1 , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def oOOi1Ii ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OOo0 )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  O0Oo0 ( url )
def O0Oo0 ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( OOo0 )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OOo0 )
 I1i11 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OOo0 )
 OooOo0oo0O0o00O = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iiIi1IIiI ( 'VidSpot - ' + iIiIi11 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  iiIi1IIiI ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , iIiIi11 in OooOo0oo0O0o00O :
  iiIi1IIiI ( 'VidUp' + iIiIi11 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for iIiIi11 , url in I1i11 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   iiIi1IIiI ( 'TheVideo - ' + iIiIi11 , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 51 - 51: Ii / i1iIi % IiI1i11I % Ii
def ii11Ii1111 ( ) :
 OOo0 = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , iI , 1021 , iiIi1IIiIi + 'anime.png' )
  if 89 - 89: IIiIiII11i . Ii1I
  if 4 - 4: oOo0O0Ooo * ii
def iIi1 ( ) :
 OOo0 = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OOo0 )
 for iI , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , iI , 1002 , iiIi1IIiIi + 'anime.png' )
  if 91 - 91: i1iIi + III1iiIii . oOo0O0Ooo / Iii / III1iiIii
  if 23 - 23: Ii1I - oooOo0oo0oo - ooOoO0O00
  if 20 - 20: ii / I1ii11iIi11i * oO0o . I11i . oOo0O0Ooo
def Oo000o0o0 ( url ) :
 OOo0 = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OOo0 )
 for o00oOOooOOo0o in i1Iii1i1I :
  oO00OII11Ii = o00oOOooOOo0o
 I1i11 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OOo0 )
 for url in I1i11 :
  iIiiiii1i ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OOo0 )
 for url , iIiIi11 in IIi :
  iIiiiii1i ( iIiIi11 , url , 1003 , oO00OII11Ii )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOO0ooOoOoOo ( url , IMAGE ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OOo0 )
 for iIiIi11 , url in IIi :
  print iIiIi11 + '     ' + url
  if 'easy' in url :
   o0OO0O0oo ( url )
  elif 'playpanda' in url :
   o0OO0O0oo ( url )
   if 40 - 40: ooOoO0O00
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0OO0O0oo ( url ) :
 OOo0 = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( OOo0 )
 for url in IIi :
  iiIi1IIiI ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 49 - 49: i1IiiiI1iI + III1iiIii
  if 28 - 28: I11i % i1IiiiI1iI
def i11II1iIi1Ii ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 88 - 88: Iii / o0o00Oo0O
def o0O0Oo00 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 70 - 70: oOo0O0Ooo + Iii / Ii1I . ooOoO0O00 . I11i * oO0o
def oO0IiiI1i1i11I1 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 I11o0O00 = ( '%s%s' % ( OOOoOOO0oOOoO , url ) )
 iiI111I1iIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , oOo00 , iIiIi11 in IIi :
  iiIi1IIiI ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + iIiIi11 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oOo00 )
  if 97 - 97: OOooOOo - oO0o
def Oooo ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  OOOoO0 ( url , iIiIi11 )
 else :
  OooO0OO ( url )
def OooO0OO ( url ) :
 import urlresolver
 try :
  O0OO0 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( O0OO0 , xbmcgui . ListItem ( iIiIi11 ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( iIiIi11 ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def O0OOO00 ( url ) :
 if 74 - 74: I11i % oOo0O0Ooo * o0ii1I + iI11I1II1I1I
 II1i11I1 = open ( OOOO0OOoO0O0 , "a" )
 II1i11I1 . write ( 'url="' + url + '"\n' )
 II1i11I1 . close
 if 79 - 79: I11i
 I11I1IIiiII1 = xbmc . Player ( IIIIIii1ii11 ( ) )
 import urlresolver
 try : I11I1IIiiII1 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iIiIi11 ) )
 I11I1IIiiII1 = xbmc . Player ( IIIIIii1ii11 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : I11I1IIiiII1 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def OOOoO0 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  ooOO = '.mp4'
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OooO0OO ( url )
  if IiII111iI1ii1 == 1 :
   iiii111iI ( url , name , ooOO )
 elif '.mkv' in url :
  ooOO = '.mkv'
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OooO0OO ( url )
  if IiII111iI1ii1 == 1 :
   iiii111iI ( url , name , ooOO )
 elif '.mp3' in url :
  ooOO = '.mp3'
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OooO0OO ( url )
  if IiII111iI1ii1 == 1 :
   iiii111iI ( url , name , ooOO )
 elif '.avi' in url :
  ooOO = '.avi'
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OooO0OO ( url )
  if IiII111iI1ii1 == 1 :
   iiii111iI ( url , name , ooOO )
 elif '.mov' in url :
  ooOO = '.mov'
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OooO0OO ( url )
  if IiII111iI1ii1 == 1 :
   iiii111iI ( url , name , ooOO )
 elif '.mpeg' in url :
  ooOO = '.mpeg'
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OooO0OO ( url )
  if IiII111iI1ii1 == 1 :
   iiii111iI ( url , name , ooOO )
 elif '.mpg' in url :
  ooOO = '.mpg'
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OooO0OO ( url )
  if IiII111iI1ii1 == 1 :
   iiii111iI ( url , name , ooOO )
 elif '.flv' in url :
  ooOO = '.flv'
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OooO0OO ( url )
  if IiII111iI1ii1 == 1 :
   iiii111iI ( url , name , ooOO )
 elif '.wmv' in url :
  ooOO = '.wmv'
  oOI1Ii1I1 = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  IiII111iI1ii1 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , oOI1Ii1I1 )
  if IiII111iI1ii1 == 0 :
   OooO0OO ( url )
  if IiII111iI1ii1 == 1 :
   iiii111iI ( url , name , ooOO )
 else :
  OooO0OO ( url )
def iiii111iI ( url , name , cat ) :
 iI1III11IIi11Ii11 ( )
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( OooO0 ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 IiIi11iI = os . path . join ( oO0O00oOOoooO , file )
 try :
  os . remove ( IiIi11iI )
 except :
  pass
 downloader . download ( url , IiIi11iI , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def iI1III11IIi11Ii11 ( ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def iII1I ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iIiIi11 )
 xbmc . sleep ( 1 )
 I11I1IIiiII1 = xbmc . Player ( IIIIIii1ii11 ( ) )
 o0oOoO00o . update ( 100 , '%s' % iIiIi11 )
 xbmc . sleep ( 1 )
 I11I1IIiiII1 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 66 - 66: oO0o % I1ii11iIi11i . IIiIiII11i
def iiiIi ( url ) :
 I11I1IIiiII1 = xbmc . Player ( IIIIIii1ii11 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : I11I1IIiiII1 . play ( url ) . strip ( )
 except : pass
 if 84 - 84: i1iIi * ii + o0o00Oo0O
def OoIiI ( url ) :
 I11I1IIiiII1 = xbmc . Player ( IIIIIii1ii11 ( ) )
 import urlresolver
 IiIIii11i = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 I11I1IIiiII1 . play ( IiIIii11i )
 xbmc . sleep ( 1 )
 I11I1IIiiII1 . play ( url )
 if 49 - 49: I1ii11iIi11i
 if 41 - 41: IiI1i11I % i1iIi . I1ii11iIi11i * I11i / Ii * Ii1I
def IIIIIii1ii11 ( ) :
 try :
  ii1I1 = getSet ( "core-player" )
  if ( ii1I1 == 'DVDPLAYER' ) : ooOo0OooOooo = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ii1I1 == 'MPLAYER' ) : ooOo0OooOooo = xbmc . PLAYER_CORE_MPLAYER
  elif ( ii1I1 == 'PAPLAYER' ) : ooOo0OooOooo = xbmc . PLAYER_CORE_PAPLAYER
  else : ooOo0OooOooo = xbmc . PLAYER_CORE_AUTO
 except : ooOo0OooOooo = xbmc . PLAYER_CORE_AUTO
 return ooOo0OooOooo
 return True
 if 35 - 35: i1IiiiI1iI / ii / III1iiIii + OOooOOo - i1IiiiI1iI + Ii
def iIiiiii1i ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iI111i1I1II = [ ]
  iI111i1I1II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iI111i1I1II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   iI111i1I1II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IIiiii . addContextMenuItems ( iI111i1I1II )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = True )
 return IIIII1iii
 if 86 - 86: IIiIiII11i / i1i1I1IIii1II
def IiIIii1iiI ( name , url , mode , iconimage , fanart , description ) :
 if 5 - 5: o0o00Oo0O + oOo0O0Ooo
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIiiii . setProperty ( "Fanart_Image" , fanart )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = True )
 return IIIII1iii
 if 35 - 35: i1iIi + OOooOOo * ii - IIiIiII11i
def iiIi1IIiI ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iI111i1I1II = [ ]
  iI111i1I1II . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iI111i1I1II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   iI111i1I1II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IIiiii . addContextMenuItems ( iI111i1I1II )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = False )
 return IIIII1iii
 if 19 - 19: ooOoO0O00 / o0ii1I / OOooOOo . oOo0O0Ooo / o0ii1I % I11i
 if 39 - 39: i1iIi - ii
 if 88 - 88: ooOoO0O00 + iI11I1II1I1I * Ii - ii % I11i
 if 74 - 74: i1iIi - Ii
 if 34 - 34: III1iiIii + i1IiiiI1iI + I1ii11iIi11i / IIiIiII11i
 if 33 - 33: o0ii1I . ooOoO0O00 - IIiIiII11i - oO0o
def I1iI1IiII ( url , heading , announce ) :
 class II11iII ( ) :
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
   try : ooOoO00 = open ( announce ) ; Ooo00O0 = ooOoO00 . read ( )
   except : Ooo00O0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Ooo00O0 ) )
   return
 II11iII ( )
 II11iII ( )
def IiII111i1i11 ( heading , announce ) :
 class II11iII ( ) :
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
   try : ooOoO00 = open ( announce ) ; Ooo00O0 = ooOoO00 . read ( )
   except : Ooo00O0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Ooo00O0 ) )
   return
 II11iII ( )
 II11iII ( )
def O0O0Oooo0o ( ) :
 I1iI1IiII ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 68 - 68: Ii1I / i1iIi % o0o00Oo0O
 if 66 - 66: I1ii11iIi11i . i1i1I1IIii1II - o0o00Oo0O . i1IiiiI1iI + IiI1i11I / Ii
 if 52 - 52: i1i1I1IIii1II % I1ii11iIi11i * IIiIiII11i
 if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
 if 27 - 27: ooOoO0O00 - i1i1I1IIii1II + oooOo0oo0oo
def ooI1111i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 3 - 3: III1iiIii % i1IiiiI1iI . ii
 if 19 - 19: i1IiiiI1iI * o0ii1I - i1i1I1IIii1II
 if 78 - 78: oO0o - o0ii1I / oooOo0oo0oo
 if 81 - 81: OOooOOo
 if 21 - 21: IiI1i11I / oooOo0oo0oo % III1iiIii
 if 51 - 51: Iii + i1iIi / oOo0O0Ooo
 if 3 - 3: iI11I1II1I1I / oooOo0oo0oo % i1i1I1IIii1II . o0ii1I - o0ii1I
 if 55 - 55: Ii % ii + o0o00Oo0O
 if 7 - 7: i1iIi - Ii * IiI1i11I / o0ii1I - I11i
 if 62 - 62: I11i - iI11I1II1I1I . Iii . o0ii1I * o0ii1I
 if 24 - 24: Iii
 if 93 - 93: oOo0O0Ooo % oO0o / Ii / Iii
 if 60 - 60: i1iIi - o0ii1I . oOo0O0Ooo * i1i1I1IIii1II * Ii
 if 29 - 29: oO0o - I1ii11iIi11i . i1i1I1IIii1II / oO0o % Ii
 if 26 - 26: i1iIi . i1IiiiI1iI / IIiIiII11i % o0ii1I
 if 82 - 82: oooOo0oo0oo % o0o00Oo0O % iI11I1II1I1I % III1iiIii + Ii
 if 64 - 64: ooOoO0O00 / III1iiIii . III1iiIii - i1IiiiI1iI % oooOo0oo0oo . IIiIiII11i
 if 78 - 78: i1IiiiI1iI - o0o00Oo0O - i1IiiiI1iI . iI11I1II1I1I % Ii1I . ii
 if 64 - 64: III1iiIii
 if 21 - 21: I11i - i1iIi * ii . ii
 if 17 - 17: oooOo0oo0oo - IiI1i11I % oOo0O0Ooo * oooOo0oo0oo * iI11I1II1I1I . I11i
 if 58 - 58: i1i1I1IIii1II - IIiIiII11i + o0o00Oo0O
 if 54 - 54: iI11I1II1I1I - III1iiIii - III1iiIii
 if 18 - 18: Ii + iI11I1II1I1I . Ii
def o00O00oo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + III1Iii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 67 - 67: oooOo0oo0oo / oO0o + o0o00Oo0O . i1IiiiI1iI
def oo0O ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiI1i1iIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 69 - 69: I1ii11iIi11i
def ooOOO000 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + O0OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 72 - 72: I11i + Iii / oO0o
def OoOOOOoOOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OoooOOoOOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 46 - 46: ii - I1ii11iIi11i * i1IiiiI1iI * oooOo0oo0oo * i1IiiiI1iI . i1i1I1IIii1II
def O000 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IIi1IiiIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 81 - 81: o0o00Oo0O % I11i / o0ii1I / i1iIi . Ii + III1iiIii
def i11iI1i11I111 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oo0iIiIII1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 79 - 79: i1IiiiI1iI . i1iIi / o0o00Oo0O - oOo0O0Ooo / Ii1I / OOooOOo
def IIi1I1I1111 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + II1iIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 94 - 94: iI11I1II1I1I + Ii1I - i1iIi
def II11ii1Iiiii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IIiII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 65 - 65: i1iIi
def iIIoO0Ooo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiiiIIiiII1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 42 , oo00O00oO000o , oOOo0O00o , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 93 - 93: OOooOOo % o0ii1I / o0ii1I - i1iIi - III1iiIii % i1iIi
def o0Oo00 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiIIiI1i1IIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for iIiIi11 , url , oo00O00oO000o , oOOo0O00o , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( iIiIi11 , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , I1iIII1 )
 O0oO0 ( 'movies' , 'MAIN' )
 if 75 - 75: oOo0O0Ooo % IIiIiII11i * i1i1I1IIii1II % ooOoO0O00 % oooOo0oo0oo
 if 93 - 93: OOooOOo
 if 48 - 48: Ii
 if 25 - 25: oOo0O0Ooo . iI11I1II1I1I * Ii / i1i1I1IIii1II % o0ii1I
 if 55 - 55: Ii % ooOoO0O00
 if 39 - 39: Iii % I11i . I11i * i1IiiiI1iI + i1i1I1IIii1II
 if 70 - 70: oO0o
 if 55 - 55: oOo0O0Ooo
 if 61 - 61: I1ii11iIi11i * Iii % ooOoO0O00
def oOOoO0O ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OoiiI11111II , IIIii11 , i1i11I1I1 in os . walk ( o0 ) :
     iiii1i1IIi = 0
     iiii1i1IIi += len ( i1i11I1I1 )
     if iiii1i1IIi > 0 :
      for ooOoO00 in i1i11I1I1 :
       os . unlink ( os . path . join ( OoiiI11111II , ooOoO00 ) )
  o0oOo0o0o00O00o = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( o0oOo0o0o00O00o )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 20 - 20: I1ii11iIi11i . oOo0O0Ooo . oOo0O0Ooo / ii . ii + iI11I1II1I1I
 if 60 - 60: OOooOOo / i1iIi % iI11I1II1I1I
 if 32 - 32: Ii + IIiIiII11i + IIiIiII11i % Iii
 if 96 - 96: I11i
 if 90 - 90: III1iiIii * o0ii1I . Iii / Ii1I % Iii
 if 58 - 58: IiI1i11I % iI11I1II1I1I * oO0o
 if 25 - 25: i1IiiiI1iI - i1iIi + I1ii11iIi11i . oOo0O0Ooo % iI11I1II1I1I
 if 49 - 49: ooOoO0O00 + oO0o + IiI1i11I / I1ii11iIi11i
def iii11i1 ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 5 - 5: Ii + Iii . III1iiIii
def iI1iI ( url ) :
 IiIi1 = os . path . join ( oooOOOOO , 'addon_data' )
 Oo0OooOO00OOO = [
 ( IiIi1 ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( IiIi1 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( IiIi1 , 'plugin.video.itv' , 'Images' ) ) ]
 if 60 - 60: i1i1I1IIii1II . ii
 iIi1I1Iii1 = 0
 if 99 - 99: oOo0O0Ooo . i1iIi % IIiIiII11i / oOo0O0Ooo
 for iII1i11 in Oo0OooOO00OOO :
  if os . path . exists ( iII1i11 ) and not iII1i11 in [ oo0o0O00 , IiIi1 ] :
   for OoiiI11111II , IIIii11 , i1i11I1I1 in os . walk ( iII1i11 ) :
    iiii1i1IIi = 0
    iiii1i1IIi += len ( i1i11I1I1 )
    if iiii1i1IIi > 0 :
     for ooOoO00 in i1i11I1I1 :
      if not ooOoO00 in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( OoiiI11111II , ooOoO00 ) )
       except :
        pass
      else : o00O0O ( 'Ignore Log File: %s' % ooOoO00 )
     for oO0Oooo0OoO in IIIii11 :
      try :
       shutil . rmtree ( os . path . join ( OoiiI11111II , oO0Oooo0OoO ) )
       iIi1I1Iii1 += 1
       o00O0O ( "[Success] cleared %s files from %s" % ( str ( iiii1i1IIi ) , os . path . join ( iII1i11 , oO0Oooo0OoO ) ) )
      except :
       o00O0O ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , oO0Oooo0OoO ) )
  else :
   for OoiiI11111II , IIIii11 , i1i11I1I1 in os . walk ( iII1i11 ) :
    for oO0Oooo0OoO in IIIii11 :
     if 'cache' in oO0Oooo0OoO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( OoiiI11111II , oO0Oooo0OoO ) )
       iIi1I1Iii1 += 1
       o00O0O ( "[Success] wiped %s " % os . path . join ( iII1i11 , oO0Oooo0OoO ) )
      except :
       o00O0O ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , oO0Oooo0OoO ) )
       if 52 - 52: Ii
 iii11i1 ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % iIi1I1Iii1 )
 if 57 - 57: oOo0O0Ooo - ooOoO0O00 + IiI1i11I * I1ii11iIi11i % oO0o
 if 87 - 87: iI11I1II1I1I % OOooOOo + oO0o / Ii
 if 97 - 97: IiI1i11I % oO0o / oO0o
 if 30 - 30: oO0o . Ii * o0ii1I / I11i . I1ii11iIi11i . ii
 if 1 - 1: i1i1I1IIii1II % OOooOOo . o0o00Oo0O
 if 43 - 43: o0o00Oo0O + IIiIiII11i . o0o00Oo0O
 if 25 - 25: IIiIiII11i + Iii
def oOo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 Oo000O = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OoiiI11111II , IIIii11 , i1i11I1I1 in os . walk ( Oo000O ) :
   iiii1i1IIi = 0
   iiii1i1IIi += len ( i1i11I1I1 )
   if 6 - 6: i1IiiiI1iI . i1i1I1IIii1II . Ii1I - i1iIi + i1IiiiI1iI
   if 85 - 85: oOo0O0Ooo / Ii1I * ii
   if iiii1i1IIi > 0 :
    if 33 - 33: oooOo0oo0oo / I11i + oooOo0oo0oo . Ii
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( iiii1i1IIi ) + " files found" , "Do you want to delete them?" ) :
     if 19 - 19: OOooOOo % OOooOOo
     for ooOoO00 in i1i11I1I1 :
      os . unlink ( os . path . join ( OoiiI11111II , ooOoO00 ) )
     for oO0Oooo0OoO in IIIii11 :
      shutil . rmtree ( os . path . join ( OoiiI11111II , oO0Oooo0OoO ) )
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
 if 74 - 74: Ii / Ii1I - i1i1I1IIii1II . oO0o
 if 25 - 25: oooOo0oo0oo % i1i1I1IIii1II
 if 48 - 48: Ii1I . IIiIiII11i * III1iiIii . oOo0O0Ooo * o0ii1I
 if 82 - 82: OOooOOo * Ii1I - ii / ooOoO0O00 + ii * Iii
 if 87 - 87: ooOoO0O00 . Ii1I / i1iIi / o0o00Oo0O
 if 62 - 62: I11i % IIiIiII11i
 if 22 - 22: i1i1I1IIii1II - I11i
 if 89 - 89: oooOo0oo0oo
 if 34 - 34: IiI1i11I . oooOo0oo0oo
def i11I1IiII1i1i ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 Oo000O = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OoiiI11111II , IIIii11 , i1i11I1I1 in os . walk ( Oo000O ) :
   iiii1i1IIi = 0
   iiii1i1IIi += len ( i1i11I1I1 )
   if 13 - 13: oO0o * oooOo0oo0oo + i1i1I1IIii1II
   if 21 - 21: Ii . o0ii1I % ooOoO0O00 * o0ii1I . i1i1I1IIii1II + o0ii1I
   if iiii1i1IIi > 0 :
    if 92 - 92: ooOoO0O00 + oO0o * Iii
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( iiii1i1IIi ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: I1ii11iIi11i
     for ooOoO00 in i1i11I1I1 :
      os . unlink ( os . path . join ( OoiiI11111II , ooOoO00 ) )
     for oO0Oooo0OoO in IIIii11 :
      shutil . rmtree ( os . path . join ( OoiiI11111II , oO0Oooo0OoO ) )
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
 iI1iI ( url )
 return
 if 93 - 93: IiI1i11I . Ii1I . I1ii11iIi11i . i1i1I1IIii1II . ii
 if 51 - 51: o0o00Oo0O - IiI1i11I
 if 65 - 65: o0o00Oo0O / IIiIiII11i * III1iiIii % o0ii1I + I11i
 if 43 - 43: i1IiiiI1iI + oO0o * ii
 if 85 - 85: IiI1i11I + oooOo0oo0oo
 if 36 - 36: oO0o % IIiIiII11i * o0o00Oo0O + IIiIiII11i - i1i1I1IIii1II - ooOoO0O00
 if 53 - 53: o0ii1I - oooOo0oo0oo
 if 75 - 75: IiI1i11I % o0o00Oo0O - Iii - Ii1I + oOo0O0Ooo - oOo0O0Ooo
 if 87 - 87: ooOoO0O00 % o0ii1I % ooOoO0O00 + iI11I1II1I1I
 if 23 - 23: iI11I1II1I1I * Iii . i1IiiiI1iI - I11i
def Ooo0oo0oO000 ( url , name ) :
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iI11i11iI = os . path . join ( oO0O00oOOoooO , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 I11I1iI = os . path . join ( oO0O00oOOoooO , 'advancedsettings.xml.bak' )
 if os . path . exists ( I11I1iI ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   iI11i11iI = os . path . join ( oO0O00oOOoooO , 'advancedsettings.xml' )
   try :
    os . remove ( iI11i11iI )
    print '=== GenieTv - REMOVING    ' + str ( iI11i11iI ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   i1ioO = open ( iI11i11iI , "w" )
   i1ioO . write ( iiI111I1iIiI )
   i1ioO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( iI11i11iI ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  iI11i11iI = os . path . join ( oO0O00oOOoooO , 'advancedsettings.xml' )
  try :
   os . remove ( iI11i11iI )
   print '=== GenieTv - REMOVING    ' + str ( iI11i11iI ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  i1ioO = open ( iI11i11iI , "w" )
  i1ioO . write ( iiI111I1iIiI )
  i1ioO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iI11i11iI ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 65 - 65: oooOo0oo0oo . IIiIiII11i * Ii + oooOo0oo0oo
def oOOo0OO0oo ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iI11i11iI = os . path . join ( oO0O00oOOoooO , 'advancedsettings.xml' )
 try :
  i1ioO = open ( iI11i11iI ) . read ( )
  if 'zero' in i1ioO :
   name = '0CACHE'
  elif 'tuxen' in i1ioO :
   name = 'TUXENS'
  elif 'muckys' in i1ioO :
   name = 'MUCKYS'
  elif 'p2p1' in i1ioO :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in i1ioO :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in i1ioO :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 68 - 68: i1i1I1IIii1II % o0ii1I - oooOo0oo0oo / ooOoO0O00
def IiIi1i1IIiii1 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iI11i11iI = os . path . join ( oO0O00oOOoooO , 'advancedsettings.xml' )
 try :
  os . remove ( iI11i11iI )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( iI11i11iI ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 74 - 74: IIiIiII11i + i1IiiiI1iI + oOo0O0Ooo * I1ii11iIi11i % OOooOOo
 if 10 - 10: oO0o / o0o00Oo0O . oOo0O0Ooo - oO0o % iI11I1II1I1I - oooOo0oo0oo
 if 36 - 36: oOo0O0Ooo + III1iiIii . III1iiIii
 if 27 - 27: OOooOOo - iI11I1II1I1I / ooOoO0O00 * i1IiiiI1iI - i1iIi
 if 2 - 2: IiI1i11I * Iii * i1iIi + Ii + i1i1I1IIii1II
 if 81 - 81: I11i * oO0o
 if 18 - 18: Ii / I11i - i1i1I1IIii1II . Iii * ooOoO0O00
 if 67 - 67: o0ii1I
 if 64 - 64: OOooOOo + IiI1i11I * OOooOOo - oOo0O0Ooo * ii
 if 27 - 27: IIiIiII11i + Ii
def III1IiIi1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for O0OO00000o00 , i1I1 , IIIIiiiI11iII , II1ii in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % O0OO00000o00 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % IIIIiiiI11iII , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % II1ii )
  inc = inc + 1
  if 10 - 10: o0ii1I - IIiIiII11i / Ii * oOo0O0Ooo / o0o00Oo0O . Iii
  if 67 - 67: OOooOOo - i1iIi - iI11I1II1I1I
  if 31 - 31: IIiIiII11i + I11i * Ii . I11i
  if 73 - 73: i1i1I1IIii1II / oooOo0oo0oo * IIiIiII11i % ii - ooOoO0O00 - i1iIi
  if 43 - 43: I11i + o0ii1I % oO0o . i1IiiiI1iI + ooOoO0O00
  if 85 - 85: I1ii11iIi11i % Ii1I / oooOo0oo0oo
  if 65 - 65: i1iIi + III1iiIii - OOooOOo % IIiIiII11i - iI11I1II1I1I
  if 39 - 39: oOo0O0Ooo + Ii1I - Ii
  if 43 - 43: iI11I1II1I1I
def oOOO00o ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iI11i11iI = os . path . join ( oO0O00oOOoooO , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  i1ioO = open ( iI11i11iI , "w" )
  i1ioO . write ( iiI111I1iIiI )
  i1ioO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iI11i11iI ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 68 - 68: IiI1i11I . oO0o % III1iiIii % Iii
def oO00O0o0Oo ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oO0O00oOOoooO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iI11i11iI = os . path . join ( oO0O00oOOoooO , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  i1ioO = open ( iI11i11iI , "w" )
  i1ioO . write ( iiI111I1iIiI )
  i1ioO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iI11i11iI ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 21 - 21: III1iiIii * i1i1I1IIii1II - OOooOOo . ooOoO0O00
 if 52 - 52: OOooOOo . Ii1I . I1ii11iIi11i
def Oo0ooOOO0 ( ) :
 try :
  OoO0o0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OoO0o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    OOo0OoO0O = os . path . join ( OoO0o0 , "source.db" )
    os . unlink ( OOo0OoO0O )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 39 - 39: I11i % IiI1i11I . OOooOOo - i1IiiiI1iI
 if 39 - 39: Ii * OOooOOo . OOooOOo . Ii1I . I1ii11iIi11i
 if 61 - 61: Iii / oooOo0oo0oo
 if 85 - 85: OOooOOo - Iii . OOooOOo . OOooOOo
 if 62 - 62: III1iiIii % ii * oO0o + oO0o % o0ii1I % IiI1i11I
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 66 - 66: oOo0O0Ooo . oooOo0oo0oo - oO0o % I1ii11iIi11i * I11i - i1i1I1IIii1II
 if 68 - 68: Iii - Ii / I11i + i1iIi / oOo0O0Ooo
 if 31 - 31: i1IiiiI1iI . ii . ooOoO0O00
 if 65 - 65: oO0o . i1iIi
 if 12 - 12: i1IiiiI1iI + o0o00Oo0O - i1i1I1IIii1II . III1iiIii
 if 46 - 46: III1iiIii . i1iIi / IiI1i11I
 if 63 - 63: IIiIiII11i - Ii1I * IIiIiII11i
def o0OoOO ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; OO000oooooO = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OO000oooooO :
  O0O0o0 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; O0O0o0 = xbmc . translatePath ( O0O0o0 ) ;
  OO00 = os . path . join ( O0O0o0 , ".." , ".." ) ; OO00 = os . path . abspath ( OO00 ) ; pluginlog ( "freshstart.main_list xbmcPath=" + OO00 ) ; iiI1II1i = False
  try :
   for OoiiI11111II , IIIii11 , i1i11I1I1 in os . walk ( OO00 , topdown = True ) :
    IIIii11 [ : ] = [ oO0Oooo0OoO for oO0Oooo0OoO in IIIii11 if oO0Oooo0OoO not in o0oO0 ]
    for iIiIi11 in i1i11I1I1 :
     try : os . remove ( os . path . join ( OoiiI11111II , iIiIi11 ) )
     except :
      if iIiIi11 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : iiI1II1i = True
      pluginlog ( "Error removing " + OoiiI11111II + " " + iIiIi11 )
    for iIiIi11 in IIIii11 :
     try : os . rmdir ( os . path . join ( OoiiI11111II , iIiIi11 ) )
     except :
      if iIiIi11 not in [ "Database" , "userdata" ] : iiI1II1i = True
      pluginlog ( "Error removing " + OoiiI11111II + " " + iIiIi11 )
   if not iiI1II1i : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 i1II1i ( )
 if 18 - 18: III1iiIii
 if 74 - 74: oOo0O0Ooo
 if 74 - 74: o0ii1I - OOooOOo . IIiIiII11i / I1ii11iIi11i
def ii1IOO00OOOO00oOO ( ) :
 O0o0ooO0oO0oO = [ ]
 iI1iII111ii1I = sys . argv [ 2 ]
 if len ( iI1iII111ii1I ) >= 2 :
  O0O0Oo00 = sys . argv [ 2 ]
  OOO0o0OO = O0O0Oo00 . replace ( '?' , '' )
  if ( O0O0Oo00 [ len ( O0O0Oo00 ) - 1 ] == '/' ) :
   O0O0Oo00 = O0O0Oo00 [ 0 : len ( O0O0Oo00 ) - 2 ]
  II1i111i11i1i = OOO0o0OO . split ( '&' )
  O0o0ooO0oO0oO = { }
  for oO0oOOoOo000O in range ( len ( II1i111i11i1i ) ) :
   OOo0o = { }
   OOo0o = II1i111i11i1i [ oO0oOOoOo000O ] . split ( '=' )
   if ( len ( OOo0o ) ) == 2 :
    O0o0ooO0oO0oO [ OOo0o [ 0 ] ] = OOo0o [ 1 ]
    if 44 - 44: oO0o / Iii + o0o00Oo0O
 return O0o0ooO0oO0oO
 if 87 - 87: i1i1I1IIii1II / oO0o / Ii / ii
Iiii11iIIiiI1I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
ooooO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ooOO0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
oOOoo0O00 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i1i1i11iI11II = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
i111 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
III1Iii1i = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
IIi1i1111i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
IiI1i1iIi1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
O0OoO = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OoooOOoOOoOo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
IIi1IiiIi1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
oo0iIiIII1Ii = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
II1iIi = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
IIiII = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
iiiiIIiiII1Iii1 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
O0OO00 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
o0oo = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOoOooO0o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
IIi11ii11 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
o00O0o00oo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
I1I1i11 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IiIIiI1i1IIiI = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OOOoOOO0oOOoO = base64 . decodestring ( 'Q1VOVA==' )
def O0O0 ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 IIiiii . setProperty ( 'fanart_image' , fanart )
 IIiiii . setProperty ( "IsPlayable" , "true" )
 iiII = [ ]
 iiII . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 iiII . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 IIiiii . addContextMenuItems ( iiII , replaceItems = True )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = False )
 return IIIII1iii
def Iii1I1I11iiI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIiiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iI111i1I1II = [ ]
  if showcontext == 'fav' :
   iI111i1I1II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   iI111i1I1II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IIiiii . addContextMenuItems ( iI111i1I1II )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = True )
 return IIIII1iii
 if 74 - 74: oooOo0oo0oo
def I1I1i1I ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 IIiIii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IIIII1iii = True
 IIiiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIiiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IIiiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iI111i1I1II = [ ]
  if showcontext == 'fav' :
   iI111i1I1II . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   iI111i1I1II . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IIiiii . addContextMenuItems ( iI111i1I1II )
 IIIII1iii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIiIii , listitem = IIiiii , isFolder = False )
 return IIIII1iii
 if 30 - 30: o0o00Oo0O . o0ii1I / I11i + oOo0O0Ooo - o0o00Oo0O
 if 88 - 88: Ii
O0O0Oo00 = ii1IOO00OOOO00oOO ( )
iI = None
iIiIi11 = None
oO0oOOoo00000 = None
oo00O00oO000o = None
oOOo0O00o = None
I1iIII1 = None
iIii11I = None
I1iiiiii = None
if 49 - 49: i1IiiiI1iI - o0ii1I . o0o00Oo0O
if 46 - 46: oooOo0oo0oo
try :
 I1iiiiii = int ( O0O0Oo00 [ "fav_mode" ] )
except :
 pass
 if 64 - 64: oOo0O0Ooo / OOooOOo
try :
 iI = urllib . unquote_plus ( O0O0Oo00 [ "url" ] )
except :
 pass
try :
 iIiIi11 = urllib . unquote_plus ( O0O0Oo00 [ "name" ] )
except :
 pass
try :
 oo00O00oO000o = urllib . unquote_plus ( O0O0Oo00 [ "iconimage" ] )
except :
 pass
try :
 oO0oOOoo00000 = int ( O0O0Oo00 [ "mode" ] )
except :
 pass
try :
 oOOo0O00o = urllib . unquote_plus ( O0O0Oo00 [ "fanart" ] )
except :
 pass
try :
 I1iIII1 = urllib . unquote_plus ( O0O0Oo00 [ "description" ] )
except :
 pass
 if 6 - 6: Ii - IiI1i11I * ooOoO0O00 - IiI1i11I
 if 8 - 8: Iii / Ii . o0o00Oo0O / oO0o * i1i1I1IIii1II + i1IiiiI1iI
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( oO0oOOoo00000 )
print "URL: " + str ( iI )
print "Name: " + str ( iIiIi11 )
print "IconImage: " + str ( oo00O00oO000o )
if 91 - 91: oOo0O0Ooo
if 84 - 84: o0o00Oo0O % o0ii1I
def O0oO0 ( content , viewType ) :
 if 3 - 3: oOo0O0Ooo . Iii / Ii1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 2 - 2: III1iiIii + Iii / iI11I1II1I1I . Ii . ooOoO0O00 * i1iIi
if oo00O00oO000o == None : oo00O00oO000o = O0O
if oOOo0O00o == None : oOOo0O00o = Oo00OOOOO
if oO0oOOoo00000 == None :
 I1IiiiiI ( )
 if 14 - 14: I1ii11iIi11i . o0o00Oo0O - i1i1I1IIii1II - Ii
elif oO0oOOoo00000 == 1 :
 i1o0 ( iI )
 if 8 - 8: oOo0O0Ooo / iI11I1II1I1I / ii / I1ii11iIi11i / i1iIi
elif oO0oOOoo00000 == 44 :
 oOoO00o ( iI )
 if 80 - 80: Iii
elif oO0oOOoo00000 == 2 :
 OoOiII11IiIi ( )
 if 26 - 26: IIiIiII11i + oOo0O0Ooo . IIiIiII11i - i1i1I1IIii1II % oO0o
elif oO0oOOoo00000 == 3 :
 I1iii1iIi ( )
 if 1 - 1: oO0o - IIiIiII11i
elif oO0oOOoo00000 == 21 :
 i1i1II ( )
 if 75 - 75: I1ii11iIi11i - OOooOOo + i1i1I1IIii1II % ooOoO0O00 * oooOo0oo0oo
elif oO0oOOoo00000 == 4 :
 oOiI1I ( )
 if 56 - 56: OOooOOo / oO0o / oOo0O0Ooo % ii
elif oO0oOOoo00000 == 5 :
 OoOo0O00 ( iI )
 if 39 - 39: oOo0O0Ooo + IIiIiII11i * I1ii11iIi11i % o0ii1I . I11i * i1i1I1IIii1II
elif oO0oOOoo00000 == 6 :
 oOo ( iI )
 if 42 - 42: o0ii1I / I1ii11iIi11i
elif oO0oOOoo00000 == 7 :
 Ooo0oo0oO000 ( iI , iIiIi11 )
 if 25 - 25: ii % o0ii1I * i1IiiiI1iI * Iii + oOo0O0Ooo % Ii1I
elif oO0oOOoo00000 == 8 :
 oOOo0OO0oo ( iI , iIiIi11 )
 if 70 - 70: o0ii1I + Ii1I * Iii * ooOoO0O00 . i1IiiiI1iI
elif oO0oOOoo00000 == 9 :
 FIXREPOSADDONS ( iI )
 if 76 - 76: ii * OOooOOo . ii
elif oO0oOOoo00000 == 10 :
 ooI1111i ( )
 if 46 - 46: i1iIi * I11i % IIiIiII11i / i1IiiiI1iI
elif oO0oOOoo00000 == 11 :
 IiIi1i1IIiii1 ( iI )
 if 29 - 29: oO0o - Ii % I1ii11iIi11i % I11i
elif oO0oOOoo00000 == 12 :
 III1IiIi1 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 30 - 30: i1i1I1IIii1II - o0ii1I % o0ii1I
elif oO0oOOoo00000 == 13 :
 oOOoO0O ( )
 if 8 - 8: III1iiIii
elif oO0oOOoo00000 == 14 :
 iI1iI ( iI )
 if 68 - 68: III1iiIii . ii - Ii + Ii
elif oO0oOOoo00000 == 15 :
 O0OO ( )
 if 81 - 81: OOooOOo + IiI1i11I . Ii
elif oO0oOOoo00000 == 16 :
 oOOO00o ( iI , iIiIi11 )
 if 10 - 10: OOooOOo + Iii - iI11I1II1I1I - Iii
elif oO0oOOoo00000 == 17 :
 oO00O0o0Oo ( iI , iIiIi11 )
 if 58 - 58: i1iIi
elif oO0oOOoo00000 == 18 :
 Oo0ooOOO0 ( )
 if 98 - 98: o0ii1I / oO0o % ii
elif oO0oOOoo00000 == 19 :
 oO0oO0O ( iI )
 if 65 - 65: i1iIi % I1ii11iIi11i - oOo0O0Ooo % i1IiiiI1iI + iI11I1II1I1I / iI11I1II1I1I
elif oO0oOOoo00000 == 40 :
 ooo000o ( iIiIi11 , iI , I1iIII1 )
 if 94 - 94: III1iiIii - I1ii11iIi11i . I11i - i1iIi - i1i1I1IIii1II . Iii
elif oO0oOOoo00000 == 42 :
 OOiii1IiiIiIIiI ( iIiIi11 , iI , I1iIII1 )
 if 39 - 39: i1i1I1IIii1II + OOooOOo
elif oO0oOOoo00000 == 43 :
 o0oo0OooOO0 ( iI )
 if 68 - 68: ooOoO0O00 * i1i1I1IIii1II / Ii
elif oO0oOOoo00000 == 20 :
 ooO ( iI )
 if 96 - 96: oOo0O0Ooo
elif oO0oOOoo00000 == 22 :
 o00O00oo0 ( iI )
 if 78 - 78: oO0o
elif oO0oOOoo00000 == 23 :
 oo0O ( iI )
 if 72 - 72: Ii1I / o0o00Oo0O % IIiIiII11i / IIiIiII11i
elif oO0oOOoo00000 == 24 :
 ooOOO000 ( iI )
 if 48 - 48: oooOo0oo0oo % oooOo0oo0oo / iI11I1II1I1I - Ii
elif oO0oOOoo00000 == 25 :
 OoOOOOoOOO ( iI )
 if 57 - 57: Iii / III1iiIii * ooOoO0O00 + IIiIiII11i . I11i
elif oO0oOOoo00000 == 26 :
 O000 ( iI )
 if 11 - 11: IIiIiII11i
elif oO0oOOoo00000 == 27 :
 i11iI1i11I111 ( iI )
 if 66 - 66: o0ii1I - oOo0O0Ooo . ii * i1IiiiI1iI
elif oO0oOOoo00000 == 28 :
 IIi1I1I1111 ( iI )
 if 16 - 16: III1iiIii * oO0o * Ii - i1iIi
elif oO0oOOoo00000 == 29 :
 II11ii1Iiiii ( iI )
 if 88 - 88: iI11I1II1I1I / o0ii1I * III1iiIii / i1IiiiI1iI
elif oO0oOOoo00000 == 30 :
 iIiI1111 ( iI )
 if 31 - 31: o0o00Oo0O . oOo0O0Ooo
elif oO0oOOoo00000 == 31 :
 iIIoO0Ooo ( iI )
 if 8 - 8: OOooOOo
elif oO0oOOoo00000 == 32 :
 oOoOO0O00o ( )
 if 99 - 99: IiI1i11I
elif oO0oOOoo00000 == 33 :
 o0OOOO ( )
 if 93 - 93: i1IiiiI1iI
elif oO0oOOoo00000 == 35 :
 iI1111i1i11Ii ( iI )
 if 39 - 39: o0ii1I
elif oO0oOOoo00000 == 34 :
 OOoo0OOOo0o ( iI )
 if 10 - 10: OOooOOo . iI11I1II1I1I / Ii1I % IiI1i11I / Ii
elif oO0oOOoo00000 == 36 :
 Oo00OOoO0oo ( iI )
 if 14 - 14: Ii % I11i * o0o00Oo0O % iI11I1II1I1I . III1iiIii - IIiIiII11i
elif oO0oOOoo00000 == 37 :
 oOoo ( iI )
 if 14 - 14: o0ii1I % i1iIi - OOooOOo
elif oO0oOOoo00000 == 38 :
 oOOoo ( iI )
 if 52 - 52: oO0o / ooOoO0O00 - o0ii1I
elif oO0oOOoo00000 == 41 :
 o0OoOO ( O0O0Oo00 )
 if 8 - 8: i1i1I1IIii1II + i1iIi . Ii1I . ooOoO0O00 / oOo0O0Ooo . III1iiIii
elif oO0oOOoo00000 == 39 :
 o0Oo00 ( iI )
 if 8 - 8: ooOoO0O00 * o0o00Oo0O
elif oO0oOOoo00000 == 45 :
 TEXTS ( )
 if 60 - 60: I1ii11iIi11i - IIiIiII11i + oOo0O0Ooo
elif oO0oOOoo00000 == 46 :
 O0O0Oooo0o ( )
 if 17 - 17: OOooOOo % oOo0O0Ooo
elif oO0oOOoo00000 == 47 :
 GEVID ( )
 if 8 - 8: I1ii11iIi11i
elif oO0oOOoo00000 == 48 :
 OOo00o0oo0 ( iIiIi11 , iI , I1iIII1 )
 if 49 - 49: OOooOOo * Iii - I11i / oO0o * i1i1I1IIii1II
elif oO0oOOoo00000 == 49 :
 I1ii1ii11i1I ( )
 if 51 - 51: i1iIi - iI11I1II1I1I . Iii * OOooOOo + i1IiiiI1iI * ooOoO0O00
elif oO0oOOoo00000 == 22222 :
 O0OOO00 ( iI )
 if 37 - 37: III1iiIii * i1i1I1IIii1II / ii . oO0o
elif oO0oOOoo00000 == 222 :
 Oooo ( iI )
 if 77 - 77: IIiIiII11i + OOooOOo * oooOo0oo0oo
elif oO0oOOoo00000 == 2222222 :
 OooO0OO ( iI )
 if 9 - 9: IIiIiII11i - Ii * I11i % oO0o * Ii / Iii
elif oO0oOOoo00000 == 222222 :
 OOOoO0 ( iI , iIiIi11 )
 if 45 - 45: Ii * IiI1i11I - Ii1I + i1iIi % IiI1i11I
elif oO0oOOoo00000 == 333 :
 oO0IiiI1i1i11I1 ( iI )
 if 11 - 11: iI11I1II1I1I
 if 48 - 48: iI11I1II1I1I - I1ii11iIi11i
elif oO0oOOoo00000 == 1020 :
 ii11Ii1111 ( )
 if 80 - 80: ooOoO0O00
elif oO0oOOoo00000 == 1021 :
 ANIMEEP ( )
 if 56 - 56: IIiIiII11i - I11i
elif oO0oOOoo00000 == 1022 :
 ANIMEPLAY ( iI )
 if 48 - 48: I1ii11iIi11i - Ii1I - IIiIiII11i . o0ii1I . i1i1I1IIii1II / iI11I1II1I1I
elif oO0oOOoo00000 == 1001 :
 iIi1 ( )
 if 38 - 38: i1IiiiI1iI % Ii + o0ii1I * i1iIi / i1IiiiI1iI
elif oO0oOOoo00000 == 1005 :
 Oo00 ( )
 if 93 - 93: i1i1I1IIii1II
elif oO0oOOoo00000 == 1007 :
 OoooOoOO0OO ( iI )
 if 60 - 60: i1IiiiI1iI . i1i1I1IIii1II / I1ii11iIi11i * i1iIi + OOooOOo - ooOoO0O00
elif oO0oOOoo00000 == 1010 :
 i1I1i1I111 ( iI )
 if 13 - 13: Ii * i1i1I1IIii1II / Iii * oOo0O0Ooo
elif oO0oOOoo00000 == 1011 :
 O0oo0O ( iI )
 if 31 - 31: iI11I1II1I1I * o0ii1I % oooOo0oo0oo . IIiIiII11i
elif oO0oOOoo00000 == 1012 :
 iIIiII11I11I1i ( iI )
 if 56 - 56: III1iiIii / Ii . I11i . i1i1I1IIii1II - Ii
elif oO0oOOoo00000 == 1030 :
 I111 ( )
 if 23 - 23: Ii1I * Ii % i1iIi
elif oO0oOOoo00000 == 1031 :
 iIOO00o0O ( iI , oo00O00oO000o )
 if 47 - 47: iI11I1II1I1I . oooOo0oo0oo / Iii % IIiIiII11i
elif oO0oOOoo00000 == 1032 :
 Oo00o00Oo ( iI )
 if 92 - 92: Ii1I % Ii
elif oO0oOOoo00000 == 1006 :
 Parse . ParseURL ( iI )
 if 82 - 82: i1IiiiI1iI * Ii1I % o0ii1I / I11i
elif oO0oOOoo00000 == 2030 :
 Parse . addonParseURL ( iI )
 if 28 - 28: IiI1i11I % oO0o - oooOo0oo0oo - I1ii11iIi11i
elif oO0oOOoo00000 == 2031 :
 Parse . apkParseURL ( iI )
 if 16 - 16: Ii - Ii . OOooOOo / ooOoO0O00
elif oO0oOOoo00000 == 2032 :
 Parse . ParseBOSS ( iI )
 if 76 - 76: o0o00Oo0O * oO0o / o0o00Oo0O
elif oO0oOOoo00000 == 1002 :
 Oo000o0o0 ( iI )
 if 23 - 23: Ii1I . iI11I1II1I1I - Ii / IIiIiII11i
elif oO0oOOoo00000 == 1003 :
 oOO0ooOoOoOo ( iI , oo00O00oO000o )
 if 48 - 48: i1i1I1IIii1II - IIiIiII11i * oOo0O0Ooo
elif oO0oOOoo00000 == 1004 :
 o0OO0O0oo ( iI )
 if 78 - 78: oOo0O0Ooo * Ii * IIiIiII11i
elif oO0oOOoo00000 == 1008 :
 ii1IiiIIiIiii ( )
 if 19 - 19: ii * Ii / o0o00Oo0O . oOo0O0Ooo % Iii
elif oO0oOOoo00000 == 1009 :
 OO0oOO0o000 ( iI )
 if 35 - 35: iI11I1II1I1I + oOo0O0Ooo - i1iIi / I1ii11iIi11i * Ii1I * I1ii11iIi11i
elif oO0oOOoo00000 == 2001 :
 oOo0ooOO0O ( )
 if 17 - 17: OOooOOo
elif oO0oOOoo00000 == 2002 :
 I1iIiiIiiIIiI ( iI )
 if 24 - 24: iI11I1II1I1I / oooOo0oo0oo % ii / o0o00Oo0O / i1i1I1IIii1II
elif oO0oOOoo00000 == 1013 :
 Ooo0O00 ( )
elif oO0oOOoo00000 == 10111113 :
 IiIii11I ( iI )
 if 93 - 93: I1ii11iIi11i
elif oO0oOOoo00000 == 1014 :
 oO0OO00o ( )
 if 5 - 5: IiI1i11I
elif oO0oOOoo00000 == 1015 :
 oooooOOOO0oOo ( iI )
 if 61 - 61: oooOo0oo0oo * oO0o - o0o00Oo0O
elif oO0oOOoo00000 == 1016 :
 i1i1I111iIi1 ( iI , oo00O00oO000o , iIiIi11 )
 if 30 - 30: iI11I1II1I1I
elif oO0oOOoo00000 == 1017 :
 oOooO0 ( )
 if 14 - 14: I11i + o0ii1I
elif oO0oOOoo00000 == 1018 :
 o00oO ( iI )
 if 91 - 91: ii / i1i1I1IIii1II + OOooOOo
elif oO0oOOoo00000 == 1019 :
 i1oO0OO0 ( iI )
elif oO0oOOoo00000 == 10190 :
 O0Oo0o000oO ( iI )
 if 100 - 100: ooOoO0O00
elif oO0oOOoo00000 == 1023 :
 iI1111i1i1ii ( )
 if 13 - 13: ooOoO0O00 . Ii1I * I11i
elif oO0oOOoo00000 == 1024 :
 OoO0ooooOOo0o ( iI )
 if 31 - 31: Ii % oO0o . Ii % i1i1I1IIii1II - ooOoO0O00
elif oO0oOOoo00000 == 1025 :
 iIii1iii1I1ii ( iI )
 if 62 - 62: i1i1I1IIii1II + i1i1I1IIii1II . ii
elif oO0oOOoo00000 == 4001 :
 OoOooOoO ( )
 if 59 - 59: iI11I1II1I1I . I1ii11iIi11i * Iii
elif oO0oOOoo00000 == 4002 :
 oOOo0OOOo00O ( )
 if 29 - 29: I1ii11iIi11i - oOo0O0Ooo * Iii
elif oO0oOOoo00000 == 4003 :
 Oo00oo ( )
 if 58 - 58: ooOoO0O00 * o0ii1I / i1iIi % iI11I1II1I1I
elif oO0oOOoo00000 == 4004 :
 ii1 ( )
 if 24 - 24: OOooOOo - I11i * oOo0O0Ooo . Iii / oO0o * o0ii1I
elif oO0oOOoo00000 == 4005 :
 IiIi1iIIi1 ( )
 if 12 - 12: ii % i1i1I1IIii1II
elif oO0oOOoo00000 == 4006 :
 II1i ( )
 if 92 - 92: i1iIi % oO0o + o0o00Oo0O + OOooOOo / oO0o * iI11I1II1I1I
elif oO0oOOoo00000 == 4007 :
 iiIi1i ( )
 if 79 - 79: o0o00Oo0O
elif oO0oOOoo00000 == 4008 :
 OOoOOO0 ( )
 if 71 - 71: oO0o - o0o00Oo0O
elif oO0oOOoo00000 == 40099 : o0oOoOo0 ( )
elif oO0oOOoo00000 == 4009 : i11i11i ( )
elif oO0oOOoo00000 == 4010 : IiIIIiI ( )
elif oO0oOOoo00000 == 3000 :
 iiIIii1Iii1I ( )
 if 73 - 73: iI11I1II1I1I
elif oO0oOOoo00000 == 3001 :
 Ii11I ( )
 if 7 - 7: OOooOOo
elif oO0oOOoo00000 == 3002 :
 i11IiiI1iIiII ( iI )
 if 55 - 55: i1i1I1IIii1II . oO0o + iI11I1II1I1I + OOooOOo / Ii1I - o0o00Oo0O
elif oO0oOOoo00000 == 3003 :
 o0oOOoOoo ( iI )
 if 14 - 14: IIiIiII11i - oO0o - o0o00Oo0O * ii / oOo0O0Ooo
elif oO0oOOoo00000 == 3004 :
 O0Ooo0O0O ( iI )
 if 3 - 3: Iii
elif oO0oOOoo00000 == 404 :
 II1iiI11i ( iIiIi11 , iI , oo00O00oO000o )
 if 46 - 46: Ii1I * i1IiiiI1iI - iI11I1II1I1I
elif oO0oOOoo00000 == 405 :
 iII1I ( iI )
 if 25 - 25: IIiIiII11i / oooOo0oo0oo + I1ii11iIi11i - iI11I1II1I1I - OOooOOo
elif oO0oOOoo00000 == 7030 :
 IIoOOOO ( )
 if 97 - 97: oooOo0oo0oo . oooOo0oo0oo / Ii1I + oOo0O0Ooo * ooOoO0O00
elif oO0oOOoo00000 == 7021 :
 iI1iIiiIii ( iIiIi11 )
 if 53 - 53: o0o00Oo0O
elif oO0oOOoo00000 == 7022 :
 oOoo0O00OO ( iIiIi11 )
 if 28 - 28: IiI1i11I % oO0o . oO0o / III1iiIii * I1ii11iIi11i * IiI1i11I
elif oO0oOOoo00000 == 7000 :
 II11111i ( iIiIi11 , iI , img )
 if 49 - 49: oOo0O0Ooo / i1IiiiI1iI * IiI1i11I + oOo0O0Ooo % i1i1I1IIii1II % i1iIi
elif oO0oOOoo00000 == 7050 :
 oooo0oOOoO000 ( iI )
 if 27 - 27: oO0o / IiI1i11I . Ii1I
elif oO0oOOoo00000 == 7051 :
 IIIIII ( iI )
 if 71 - 71: oO0o . Ii . iI11I1II1I1I + oOo0O0Ooo - I11i
elif oO0oOOoo00000 == 7052 :
 oO0ooOoOooO00o00 ( iI )
 if 34 - 34: IiI1i11I
elif oO0oOOoo00000 == 7053 :
 o0Ooo00Oo0oo0 ( iI )
 if 6 - 6: oO0o . OOooOOo + Ii1I
elif oO0oOOoo00000 == 7054 :
 CoolPlay ( iI )
 if 24 - 24: oO0o . o0ii1I
elif oO0oOOoo00000 == 7060 :
 o00ooOOo0ooO0 ( )
 if 26 - 26: o0o00Oo0O * oOo0O0Ooo - oooOo0oo0oo * ii * IIiIiII11i % OOooOOo
elif oO0oOOoo00000 == 7061 :
 oO0OoO00o ( iI )
 if 56 - 56: oooOo0oo0oo * Ii % i1iIi * OOooOOo % I1ii11iIi11i * III1iiIii
elif oO0oOOoo00000 == 7063 :
 I11i1I1 ( iI )
 if 30 - 30: ooOoO0O00 + I11i - OOooOOo . oooOo0oo0oo
elif oO0oOOoo00000 == 7062 :
 iIi1i1Ii1 ( iI )
 if 95 - 95: ooOoO0O00 . Iii + o0o00Oo0O . Iii - Iii / I1ii11iIi11i
elif oO0oOOoo00000 == 7064 :
 NATatozcat ( )
 if 41 - 41: ii . oooOo0oo0oo - o0ii1I * oO0o % Ii
elif oO0oOOoo00000 == 7067 :
 O00O0O ( iI )
 if 7 - 7: o0ii1I
elif oO0oOOoo00000 == 7066 :
 NATatozA ( iI )
 if 16 - 16: III1iiIii * I11i % IIiIiII11i - IIiIiII11i + i1iIi
elif oO0oOOoo00000 == 7065 :
 iI1I ( iI )
 if 55 - 55: oO0o % OOooOOo
elif oO0oOOoo00000 == 7070 :
 I1i1 ( )
 if 58 - 58: o0ii1I
elif oO0oOOoo00000 == 7071 :
 DIZIlist ( iI )
 if 17 - 17: oO0o - i1i1I1IIii1II % I1ii11iIi11i % i1i1I1IIii1II * i1IiiiI1iI / III1iiIii
elif oO0oOOoo00000 == 7072 :
 DIZIpull ( iI )
 if 88 - 88: i1iIi . IIiIiII11i * o0o00Oo0O % III1iiIii
elif oO0oOOoo00000 == 7073 :
 WATCHDIZI ( iI )
 if 15 - 15: o0o00Oo0O % ooOoO0O00 - oooOo0oo0oo . III1iiIii
elif oO0oOOoo00000 == 7002 :
 i1ooo00o0OO0 ( )
 if 1 - 1: oOo0O0Ooo
elif oO0oOOoo00000 == 7003 :
 o0000oO0OOOo0 ( iI )
 if 40 - 40: I11i % Iii % o0o00Oo0O
elif oO0oOOoo00000 == 7004 :
 I11I11III ( iI )
 if 88 - 88: I11i - i1i1I1IIii1II
elif oO0oOOoo00000 == 7020 :
 OoOoo0ooO0000 ( iI )
 if 73 - 73: IIiIiII11i
elif oO0oOOoo00000 == 7001 :
 I1IIIiIiIi ( )
 if 7 - 7: o0o00Oo0O / oO0o
elif oO0oOOoo00000 == 7010 :
 i1Iiiiiii ( iI )
 if 90 - 90: IiI1i11I % i1i1I1IIii1II / iI11I1II1I1I
elif oO0oOOoo00000 == 7011 :
 II1i1i ( iI )
 if 52 - 52: oOo0O0Ooo / I11i
elif oO0oOOoo00000 == 7012 :
 IIiI1i11iIII1 ( iI )
 if 20 - 20: i1IiiiI1iI . oOo0O0Ooo - iI11I1II1I1I / IiI1i11I
elif oO0oOOoo00000 == 7013 :
 cnfTVPlay2 ( iI )
elif oO0oOOoo00000 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iI )
elif oO0oOOoo00000 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iI )
elif oO0oOOoo00000 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iIiIi11 , iI , oo00O00oO000o )
elif oO0oOOoo00000 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oO0oOOoo00000 == 7018 :
 i1I11Iiii ( )
elif oO0oOOoo00000 == 7019 :
 CNF_Studio_Indexer . List_Movies ( iI )
elif oO0oOOoo00000 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iI )
elif oO0oOOoo00000 == 7024 :
 CNF_Studio_Indexer . Box_Office ( iI )
 if 46 - 46: i1IiiiI1iI . Ii
elif oO0oOOoo00000 == 8000 :
 IiI1IIii ( )
elif oO0oOOoo00000 == 8001 :
 o0O00ooo0oO0o ( )
elif oO0oOOoo00000 == 8002 :
 III111 ( )
elif oO0oOOoo00000 == 8003 :
 iIIiii1ii ( )
elif oO0oOOoo00000 == 8004 :
 I1III1i1Ii ( )
elif oO0oOOoo00000 == 8005 :
 i11iIIII1II11Iii ( )
elif oO0oOOoo00000 == 8006 :
 iI1I1I ( iIiIi11 , iI )
elif oO0oOOoo00000 == 8030 :
 O0Ooo0o ( iI )
elif oO0oOOoo00000 == 8045 :
 i1iIiII1 ( iI )
elif oO0oOOoo00000 == 8046 :
 Oo00OO ( iI )
elif oO0oOOoo00000 == 8047 :
 oO00O0OO ( iI )
elif oO0oOOoo00000 == 8048 :
 IIi1iii ( iI )
elif oO0oOOoo00000 == 8049 :
 ii1Ii ( iI )
elif oO0oOOoo00000 == 804900 :
 IIIIi11111 ( iI )
elif oO0oOOoo00000 == 8020 :
 o00oOoOo0 ( )
elif oO0oOOoo00000 == 8021 :
 oo0oOOo0 ( iI )
elif oO0oOOoo00000 == 8022 :
 oOOi1Ii ( iI )
elif oO0oOOoo00000 == 8023 :
 O0Oo0 ( iI )
elif oO0oOOoo00000 == 8040 :
 I1I1i ( )
elif oO0oOOoo00000 == 8041 :
 ooOO0o ( iI )
elif oO0oOOoo00000 == 8042 :
 I1IiII ( iI )
elif oO0oOOoo00000 == 8043 :
 yt . PlayVideo ( iI )
elif oO0oOOoo00000 == 8044 :
 o0O00o0o ( iI )
elif oO0oOOoo00000 == 8060 :
 oOO ( )
elif oO0oOOoo00000 == 8061 :
 I11iI ( iI )
elif oO0oOOoo00000 == 8064 :
 oo000ii ( )
elif oO0oOOoo00000 == 8065 :
 O0oo0O0oO00O0 ( iI )
elif oO0oOOoo00000 == 8070 :
 oo00ooOOOo0O ( )
elif oO0oOOoo00000 == 8071 :
 i11111i1I1IiI ( iI )
elif oO0oOOoo00000 == 7080 :
 Ii111i1I1i1i ( iI )
elif oO0oOOoo00000 == 8090 :
 Oo0O0 ( )
elif oO0oOOoo00000 == 8091 :
 O0ooO00OO ( iI )
elif oO0oOOoo00000 == 8092 :
 iiiiiiI ( iI )
elif oO0oOOoo00000 == 8093 :
 IiI11I1I111 ( iI )
elif oO0oOOoo00000 == 8081 :
 ii11iI11I111I ( )
elif oO0oOOoo00000 == 8062 :
 OooOO0 ( iI )
elif oO0oOOoo00000 == 8063 :
 ii1i ( iI )
elif oO0oOOoo00000 == 8050 :
 ii1Io0oOO0 ( )
elif oO0oOOoo00000 == 8051 :
 I11II11IiI11 ( iI )
elif oO0oOOoo00000 == 8052 :
 O00o ( iI )
elif oO0oOOoo00000 == 8085 :
 OOo0iIiiI11II11 ( )
elif oO0oOOoo00000 == 8086 :
 O0ooO0oO0 ( iI )
elif oO0oOOoo00000 == 8087 :
 ooO0 ( iI )
elif oO0oOOoo00000 == 8088 :
 O00O0O0 ( iI , iIiIi11 )
elif oO0oOOoo00000 == 9000 :
 Iiii ( )
elif oO0oOOoo00000 == 1111 :
 oOo00OO0ooOOO ( )
elif oO0oOOoo00000 == 9001 :
 I1IiiI1ii1i ( )
elif oO0oOOoo00000 == 9002 :
 O0OoO0ooOO0o ( )
elif oO0oOOoo00000 == 9003 :
 o0O00 ( )
elif oO0oOOoo00000 == 9004 :
 World1 ( )
elif oO0oOOoo00000 == 9005 :
 World2 ( iI )
elif oO0oOOoo00000 == 9006 :
 World3 ( iI )
elif oO0oOOoo00000 == 9007 :
 OooOooo00OOO0o ( )
elif oO0oOOoo00000 == 9008 :
 II1iIIiIII ( iI )
elif oO0oOOoo00000 == 9009 :
 iI1 ( iI )
elif oO0oOOoo00000 == 9010 :
 I1iOoO00O ( )
elif oO0oOOoo00000 == 9011 :
 O0oo0ooO ( iI )
elif oO0oOOoo00000 == 50 :
 OooO00o000 ( iI )
elif oO0oOOoo00000 == 9020 :
 champlist ( )
elif oO0oOOoo00000 == 9021 :
 OOoooiII1 ( )
elif oO0oOOoo00000 == 9022 :
 ii1i1iIiIIi ( )
elif oO0oOOoo00000 == 9023 :
 iI11I11i ( )
elif oO0oOOoo00000 == 9024 :
 Iiooo000o0OoOo ( iI )
elif oO0oOOoo00000 == 9030 :
 OOOO0oooooO0o ( iI )
elif oO0oOOoo00000 == 9031 :
 O00o00o0 ( iI )
elif oO0oOOoo00000 == 9032 :
 o00OOOOoOO ( iI )
elif oO0oOOoo00000 == 9033 :
 OooOoOoo0ooo0 ( iI )
elif oO0oOOoo00000 == 9034 :
 iiOOO0oOOoo ( )
elif oO0oOOoo00000 == 7085 :
 ooOO0o0ooOo0 ( iI )
elif oO0oOOoo00000 == 7086 :
 i11iI ( iI )
elif oO0oOOoo00000 == 7087 :
 oo0O0 ( I1iIII1 )
elif oO0oOOoo00000 == 9666 :
 i11I1IiII1i1i ( iI )
elif oO0oOOoo00000 == 10100 : IiII11 ( )
elif oO0oOOoo00000 == 101001 : OOIiIIi1iIii1I1 ( iI )
elif oO0oOOoo00000 == 10105 : IIii1iiiIi ( iI )
elif oO0oOOoo00000 == 10106 : iI11I1IiI1 ( iI )
elif oO0oOOoo00000 == 10104 : IIi1iII11III ( iI )
elif oO0oOOoo00000 == 10107 : ii1oo ( )
elif oO0oOOoo00000 == 10103 : I11Ii ( iI )
elif oO0oOOoo00000 == 10108 : iii1OO00Oo00o ( iI )
elif oO0oOOoo00000 == 10000 : Origin_Menu ( )
elif oO0oOOoo00000 == 10001 : OoOOo0O00 ( )
elif oO0oOOoo00000 == 10002 : O0Oooo ( )
elif oO0oOOoo00000 == 10003 : Ii1 ( )
elif oO0oOOoo00000 == 10004 : iIIIi1i1I11i ( iI )
elif oO0oOOoo00000 == 10005 : iiIII1II ( )
elif oO0oOOoo00000 == 10006 : O00o0O00 ( iI )
elif oO0oOOoo00000 == 10007 : o0o0oooO00O0 ( iI , oo00O00oO000o )
elif oO0oOOoo00000 == 10008 : o0oO0O ( )
elif oO0oOOoo00000 == 10009 : OOOO00O0OO0oo ( )
elif oO0oOOoo00000 == 10010 : IiOoo0o0OO0 ( iI )
elif oO0oOOoo00000 == 10011 : iiIIiIi1i1I1 ( iI )
elif oO0oOOoo00000 == 10012 : OooO0OO ( iI )
elif oO0oOOoo00000 == 10113 : GRABG ( iI , iIiIi11 )
elif oO0oOOoo00000 == 10109 : OoIiI ( iI )
elif oO0oOOoo00000 == 10013 : I11IIiII ( iI )
elif oO0oOOoo00000 == 10014 : iiii ( )
elif oO0oOOoo00000 == 10015 : IIiIIiI1iIII ( )
elif oO0oOOoo00000 == 10016 : OOooO ( iI )
elif oO0oOOoo00000 == 10017 : oooOoO0oo0o0 ( )
elif oO0oOOoo00000 == 10018 : iio0Oo ( )
elif oO0oOOoo00000 == 10019 : i1II1i1iiI1 ( )
elif oO0oOOoo00000 == 10020 : iIiii1IIi1I ( )
elif oO0oOOoo00000 == 10021 : oo0OOoOo0 ( )
elif oO0oOOoo00000 == 10022 : Iii1iI1iIII ( iI )
elif oO0oOOoo00000 == 10023 : o0oIi1iiiii ( iIiIi11 , iI )
elif oO0oOOoo00000 == 10024 : ii11I ( iI )
elif oO0oOOoo00000 == 10025 : O000OOO0OOo ( )
elif oO0oOOoo00000 == 10026 : Oo0OOo0o0o0o0 ( )
elif oO0oOOoo00000 == 10027 : OoiIIii1Ii1 ( )
elif oO0oOOoo00000 == 10028 : III1I11II11I ( )
elif oO0oOOoo00000 == 10029 : IiI1iII1i111iI ( )
elif oO0oOOoo00000 == 423 : iII11iI1iiIIi ( iI )
elif oO0oOOoo00000 == 426 : iiI1II1II111 ( iI )
elif oO0oOOoo00000 == 10030 : Izle_Films ( )
elif oO0oOOoo00000 == 10031 : Latest_Izle_Movies ( )
elif oO0oOOoo00000 == 10032 : Izle_Genres ( )
elif oO0oOOoo00000 == 10033 : Izle_Pop_Movies ( )
elif oO0oOOoo00000 == 10034 : Izle_Boxsets ( )
elif oO0oOOoo00000 == 10035 : Izle_Search ( )
elif oO0oOOoo00000 == 10036 : Izle_Genres_Movie ( iI )
elif oO0oOOoo00000 == 10037 : Izle_Boxset_single ( iI )
elif oO0oOOoo00000 == 10038 : Izle_IFRAME ( )
elif oO0oOOoo00000 == 10039 : Izle_Boxsets_Next ( iI )
elif oO0oOOoo00000 == 10040 : oo00ooOoO00 ( )
elif oO0oOOoo00000 == 10041 : Ii11iIi1iIiii ( iI )
elif oO0oOOoo00000 == 10042 : OOooO0o ( iI )
elif oO0oOOoo00000 == 10043 : I1IIi ( )
elif oO0oOOoo00000 == 10044 : ii1IIIIi1 ( iI )
elif oO0oOOoo00000 == 10045 : oooOoooOOo0 ( iIiIi11 )
elif oO0oOOoo00000 == 10046 : O0OoIIiII ( iI )
elif oO0oOOoo00000 == 10047 : oO0IIi11IiiiI11i ( iI )
elif oO0oOOoo00000 == 10048 : oOooo0oOOOO ( iI )
elif oO0oOOoo00000 == 10049 : OOoOOOOo ( iI )
elif oO0oOOoo00000 == 10050 : Ii1IIiI1i ( )
elif oO0oOOoo00000 == 10051 : OoOOoOo0O ( )
elif oO0oOOoo00000 == 10052 : II111IiiiI ( )
elif oO0oOOoo00000 == 10053 : Addon ( iI )
elif oO0oOOoo00000 == 10054 : IiIIIiI11i1 ( iI , iIiIi11 )
elif oO0oOOoo00000 == 10055 :
 ooOoo000 ( "addFavorite" )
 try :
  iIiIi11 = iIiIi11 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIiIi11 = iIiIi11 . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0oOOoOo00o ( iIiIi11 , iI , oo00O00oO000o , oOOo0O00o , I1iiiiii )
elif oO0oOOoo00000 == 10056 :
 ooOoo000 ( "rmFavorite" )
 try :
  iIiIi11 = iIiIi11 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iIiIi11 = iIiIi11 . split ( '  - ' ) [ 0 ]
 except :
  pass
 I1i1Ii ( iIiIi11 )
elif oO0oOOoo00000 == 10057 :
 ooOoo000 ( "getFavorites" )
 Ii1IiiiII ( )
elif oO0oOOoo00000 == 10058 : oo00ooOooO ( )
elif oO0oOOoo00000 == 10059 : Donators_Guide ( )
elif oO0oOOoo00000 == 10060 : iiIiii1iI1i ( )
elif oO0oOOoo00000 == 10061 : oO00oO00O0Oo ( )
elif oO0oOOoo00000 == 10062 : Iii1II1ii ( iIiIi11 , iI , I1iIII1 )
elif oO0oOOoo00000 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif oO0oOOoo00000 == 10064 : Oooo00 ( )
elif oO0oOOoo00000 == 10065 : OoooO0 ( iI )
elif oO0oOOoo00000 == 10066 : ii1IIiI1IIi ( iI )
elif oO0oOOoo00000 == 10068 : O0OoOO0oo0 ( iI )
elif oO0oOOoo00000 == 10069 : OoO ( iI )
elif oO0oOOoo00000 == 10070 : Ooooo ( iI )
elif oO0oOOoo00000 == 10071 : Genie_Watch ( )
elif oO0oOOoo00000 == 10072 : oo000o ( )
elif oO0oOOoo00000 == 10073 : O0OOo ( iI )
elif oO0oOOoo00000 == 10074 : oo0o00oOo0 ( iI )
elif oO0oOOoo00000 == 10075 : OO00oo ( oo00O00oO000o , iIiIi11 , iI )
elif oO0oOOoo00000 == 10076 : IiII1i1iI ( iI )
elif oO0oOOoo00000 == 10077 : OoO00ooO ( iI )
elif oO0oOOoo00000 == 10078 : I1I ( )
elif oO0oOOoo00000 == 10079 : Genie_Watch_Tv_Shows ( )
elif oO0oOOoo00000 == 10080 : Genie_Watch_Tv_Genre ( iI )
elif oO0oOOoo00000 == 10081 : Genie_Watch_TV_PlayRun ( iI )
elif oO0oOOoo00000 == 10082 : Genie_Watch_TV_Episodes ( iI , oo00O00oO000o )
elif oO0oOOoo00000 == 10083 : Genie_Watch_Tv_Recent ( iI )
elif oO0oOOoo00000 == 10084 : o0Iii ( )
elif oO0oOOoo00000 == 10085 : oo0OOo0 ( )
elif oO0oOOoo00000 == 10086 : O0 ( )
elif oO0oOOoo00000 == 20000 : iIiI ( )
elif oO0oOOoo00000 == 20001 : iIII1iIii ( iI )
elif oO0oOOoo00000 == 20002 : Oo00o0OOo0OO ( iI )
elif oO0oOOoo00000 == 20003 : i1Ii1IiiIi1II ( iI )
elif oO0oOOoo00000 == 20004 : oooOOoo0 ( iI )
elif oO0oOOoo00000 == 20005 : iI1III ( iI )
elif oO0oOOoo00000 == 21004 : oOo00oOOOOO ( )
elif oO0oOOoo00000 == 21005 : i11ii ( iI )
elif oO0oOOoo00000 == 21006 : IiI111I ( iI )
elif oO0oOOoo00000 == 21007 : IiiiII ( iI )
elif oO0oOOoo00000 == 21008 : O00o0OO0 ( iI )
elif oO0oOOoo00000 == 21009 : IiI ( iI )
elif oO0oOOoo00000 == 30000 : i1i1I1Ii1IIii ( )
elif oO0oOOoo00000 == 30001 : iIII11I ( )
elif oO0oOOoo00000 == 100121 : Resolve ( iI )
elif oO0oOOoo00000 == 30003 : O0oO0o00oo0o ( )
elif oO0oOOoo00000 == 30004 : OoOo0o0OOoO0 ( iI )
elif oO0oOOoo00000 == 30005 : oooOoO ( iI )
elif oO0oOOoo00000 == 30006 : i1iiiiii1 ( )
elif oO0oOOoo00000 == 30007 : ii11ii11II ( )
elif oO0oOOoo00000 == 30008 : o0Oo ( iI )
elif oO0oOOoo00000 == 30009 : IiIi1IiIii ( iI )
elif oO0oOOoo00000 == 30010 : o0Oo0oO00Oooo ( iI )
elif oO0oOOoo00000 == 30011 : O00oo0o0000 ( )
elif oO0oOOoo00000 == 30012 : OO0O00 ( )
elif oO0oOOoo00000 == 30013 : i1Ii1i11ii ( )
elif oO0oOOoo00000 == 30014 : IIi1II ( )
elif oO0oOOoo00000 == 30015 : iIii1II1I ( iI , oo00O00oO000o , oOOo0O00o )
elif oO0oOOoo00000 == 30016 : iii1IiII ( iI )
elif oO0oOOoo00000 == 30019 : iIIi1 ( iI )
elif oO0oOOoo00000 == 30017 : I1iII ( iI )
elif oO0oOOoo00000 == 30018 : OOoOoO ( iI )
elif oO0oOOoo00000 == 30030 : I1Io0Oo00 ( )
elif oO0oOOoo00000 == 30031 : o0ooo ( )
elif oO0oOOoo00000 == 30032 : I1i11111i1i11 ( )
elif oO0oOOoo00000 == 30033 : I1II11IIi11i ( )
elif oO0oOOoo00000 == 30034 : oo00ooOo ( )
elif oO0oOOoo00000 == 30035 : o0OOO ( iI )
elif oO0oOOoo00000 == 30036 : Iii11iI1I ( iI )
elif oO0oOOoo00000 == 30037 : OOo0o0O0 ( iI )
elif oO0oOOoo00000 == 30038 : iII1I1i ( )
elif oO0oOOoo00000 == 30039 : iI11I1II ( )
elif oO0oOOoo00000 == 50000 : iIIii ( )
elif oO0oOOoo00000 == 50001 : o00OIIIIIiiI ( )
elif oO0oOOoo00000 == 50002 : iIIiiIiII1i ( iI )
elif oO0oOOoo00000 == 50003 : Table_Menu ( I1iIII1 )
elif oO0oOOoo00000 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif oO0oOOoo00000 == 60001 : O00o0OO0OO0oo ( )
elif oO0oOOoo00000 == 60002 : o0oooo0OOo00 ( iIiIi11 )
elif oO0oOOoo00000 == 60003 : o0OoooO ( iI )
elif oO0oOOoo00000 == 600033 : o0o0O0oOOOooo ( iI )
elif oO0oOOoo00000 == 60004 : i11i11Iiii11i ( iI )
elif oO0oOOoo00000 == 50004 : o0OO0 ( )
elif oO0oOOoo00000 == 50005 : speedtest . runtest ( iI )
elif oO0oOOoo00000 == 70001 : oO0oO ( )
elif oO0oOOoo00000 == 70002 : OoOooOo00o ( iI )
elif oO0oOOoo00000 == 70003 : iI1IIi ( iI )
elif oO0oOOoo00000 == 70004 : II11 ( iI )
elif oO0oOOoo00000 == 70005 : oo0o0O ( iI )
elif oO0oOOoo00000 == 70006 : ooo0ooooo0o ( )
elif oO0oOOoo00000 == 50006 : IiII111i1i11 ( i1 , i1111 )
elif oO0oOOoo00000 == 80000 : i1II1i ( )
elif oO0oOOoo00000 == 80001 : resolvefilmon ( iI )
elif oO0oOOoo00000 == 80002 : O0OOOOoO00oo ( )
elif oO0oOOoo00000 == 80003 : Iii1I ( iIiIi11 , iI , "None" )
elif oO0oOOoo00000 == 80004 : iiIIII11IiIII ( iIiIi11 , iI )
elif oO0oOOoo00000 == 80005 : II1iiiiII ( )
elif oO0oOOoo00000 == 80006 : oOOoOOO0oo0 ( iI )
elif oO0oOOoo00000 == 80007 : O00OO0OOOOOoo ( iI )
elif oO0oOOoo00000 == 80008 : oo0ooO0 ( )
elif oO0oOOoo00000 == 80009 : iI11II ( )
elif oO0oOOoo00000 == 80010 : II1IiIiIIII ( iI )
elif oO0oOOoo00000 == 80011 : O0oO0o00OoO ( iI )
elif oO0oOOoo00000 == 80012 : I1IiI11 ( )
elif oO0oOOoo00000 == 90000 : OoOOoo ( iIiIi11 , iI )
elif oO0oOOoo00000 == 90001 : tools ( )
elif oO0oOOoo00000 == 90002 : Oo00o0OO0O00o ( )
elif oO0oOOoo00000 == 90003 : OOoOI1i1i1Iii1 ( iI )
elif oO0oOOoo00000 == 90004 : OoO00Ooooo ( iI )
elif oO0oOOoo00000 == 90005 : IIIiI1i ( iI )
elif oO0oOOoo00000 == 90006 : O000ooOOO ( iI )
elif oO0oOOoo00000 == 90007 : O00OOOoOooO0o ( iI )
elif oO0oOOoo00000 == 90008 : iii1I ( iI )
elif oO0oOOoo00000 == 90009 : IIII11 ( iI )
elif oO0oOOoo00000 == 90010 : i111iIi1i1II1 ( )
elif oO0oOOoo00000 == 90020 : oOo0ooO0O0oo ( )
elif oO0oOOoo00000 == 90021 : hellyeah2 ( iI )
elif oO0oOOoo00000 == 90022 : hellyeah3 ( iI )
elif oO0oOOoo00000 == 90023 : IiiIi ( )
elif oO0oOOoo00000 == 90024 : I1IIII1ii ( iI )
elif oO0oOOoo00000 == 90025 : iii1III1i ( iI )
if 89 - 89: oO0o - oooOo0oo0oo - ooOoO0O00 - oO0o % iI11I1II1I1I
elif oO0oOOoo00000 == 90026 : O0ooO0O0Ooo0o ( )
elif oO0oOOoo00000 == 90027 : OO0oO ( iIiIi11 , I1iIII1 )
if 52 - 52: I11i * o0o00Oo0O + Ii1I
elif oO0oOOoo00000 == 900300 : ooo ( )
elif oO0oOOoo00000 == 900301 : i1i1iI1iiiI ( iI )
elif oO0oOOoo00000 == 900302 : iiI1IIIi ( iI )
elif oO0oOOoo00000 == 90030 : I1iiii1I ( )
elif oO0oOOoo00000 == 90031 : o0oO0oooOoo ( )
elif oO0oOOoo00000 == 90032 : I1III1111iIi ( iI )
elif oO0oOOoo00000 == 90033 : I1i111I ( iI )
elif oO0oOOoo00000 == 90034 : o0OOOOooo ( iI )
elif oO0oOOoo00000 == 90035 : o0OOo0o0O0O ( iI )
elif oO0oOOoo00000 == 90036 : II1i1I ( iI )
elif oO0oOOoo00000 == 90039 : OOo0Oo ( iI )
elif oO0oOOoo00000 == 90037 : OOo00OoO ( iI )
elif oO0oOOoo00000 == 90038 : iiO00O00O000OOO ( )
if 83 - 83: Iii + oooOo0oo0oo - ii
elif oO0oOOoo00000 == 10090 : OoOo0oOooOoOO ( )
elif oO0oOOoo00000 == 10091 : i1O00oo00o000o ( iI )
elif oO0oOOoo00000 == 10092 : o0o000O0ooo0O ( iI )
elif oO0oOOoo00000 == 10093 : OO000O000OOO ( iI , oo00O00oO000o )
elif oO0oOOoo00000 == 10094 : I1iII1iI ( iI , oo00O00oO000o )
if 7 - 7: III1iiIii % i1iIi / ii / I11i + oO0o - oO0o
elif oO0oOOoo00000 == 10095 : o0O0O0ooo0oOO ( )
elif oO0oOOoo00000 == 10096 : i1II11Iii1I ( iI )
elif oO0oOOoo00000 == 10097 : iI1II1I1I ( iI )
elif oO0oOOoo00000 == 10098 : Ii1ii11IIIi ( iI )
elif oO0oOOoo00000 == 10099 : O0O0O ( iI )
if 15 - 15: ooOoO0O00 + oooOo0oo0oo / o0ii1I
elif oO0oOOoo00000 == 10200 : O0o ( )
elif oO0oOOoo00000 == 10201 : IIiIi1 ( iI )
elif oO0oOOoo00000 == 10202 : OoOO ( iI )
elif oO0oOOoo00000 == 10203 : RT4 ( iI )
if 51 - 51: oooOo0oo0oo + o0o00Oo0O
elif oO0oOOoo00000 == 90040 : II1iIiiI11i11 ( )
elif oO0oOOoo00000 == 90041 : IIiI11I1I1i1i ( iI )
elif oO0oOOoo00000 == 90042 : i1o0oo0Ooooo0 ( iI )
elif oO0oOOoo00000 == 90043 : i1iIiIii ( iI )
elif oO0oOOoo00000 == 90044 : ii1IIi1ii ( iI )
elif oO0oOOoo00000 == 90045 : oOO0o00o0Oo0O ( )
elif oO0oOOoo00000 == 90046 : oo0OoOOooO ( iI )
elif oO0oOOoo00000 == 90050 : Ii1I1I1i11ii ( )
elif oO0oOOoo00000 == 90051 : I1IIi1I ( iI )
elif oO0oOOoo00000 == 90052 : oo0oo ( iI )
elif oO0oOOoo00000 == 90053 : oooo ( iI )
elif oO0oOOoo00000 == 90054 : iii1IIiI ( iI )
elif oO0oOOoo00000 == 90055 : Ii1iiII1i ( )
if 91 - 91: Ii + I11i % oO0o / i1i1I1IIii1II - ooOoO0O00
elif oO0oOOoo00000 == 100001 : Stand_up ( )
if 82 - 82: o0ii1I . ii + ii % oO0o % Ii1I
elif oO0oOOoo00000 == 100003 : OOooO ( iI )
elif oO0oOOoo00000 == 100004 : I1iIiI11I1 ( iI )
elif oO0oOOoo00000 == 100005 : Resolve ( iI )
elif oO0oOOoo00000 == 100008 : Search ( )
elif oO0oOOoo00000 == 100007 : Oo ( iI )
elif oO0oOOoo00000 == 100009 : yt . PlayVideo ( iI )
elif oO0oOOoo00000 == 100010 : OoOiIIiii ( iI )
elif oO0oOOoo00000 == 100100 : OOoOoo0 ( oo00O00oO000o , iI , iIii11I )
elif oO0oOOoo00000 == 100101 : oo0OOo0O ( iI , iIiIi11 , oOOo0O00o , iIii11I , oo00O00oO000o )
elif oO0oOOoo00000 == 100102 : OooO0ooo0o ( iIiIi11 , iI , oo00O00oO000o , oOOo0O00o )
elif oO0oOOoo00000 == 100106 : I1 ( iI , iIiIi11 )
elif oO0oOOoo00000 == 100107 : OooOOOo0 ( )
elif oO0oOOoo00000 == 100108 : iIiIiiiII11i ( )
elif oO0oOOoo00000 == 100109 : Oooo000 ( iI )
elif oO0oOOoo00000 == 40000 : O0oO00oOOooO ( )
elif oO0oOOoo00000 == 40001 : iIO0OO0o0O00oO ( iI )
elif oO0oOOoo00000 == 100110 : oOo00Ooo0o0 ( )
elif oO0oOOoo00000 == 100111 : i1IiII1i1I ( iI )
elif oO0oOOoo00000 == 100110 : oOo00Ooo0o0 ( )
elif oO0oOOoo00000 == 100210 : O0Oo ( iI )
elif oO0oOOoo00000 == 100211 : iIiIii1I1 ( )
elif oO0oOOoo00000 == 100212 : iII1I11 ( )
elif oO0oOOoo00000 == 100213 : i1i1 ( )
elif oO0oOOoo00000 == 100214 : iI1IIiiIIIII ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
