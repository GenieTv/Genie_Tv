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
IiiIII111iI = "3.5.1"
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
  if 18 - 18: oooOo0oo0oo + IiI1i11I - o0ii1I . IIiIiII11i + Ii
  if oo00 . getSetting ( 'Music' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , iiIi1IIiIi + 'settings.png' , Oo00OOOOO , '' )
  if OO0OO0O00oO0 ( ) == 'android' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , str ( oO0000OOo00 ) , 30039 , iiIi1IIiIi + 'APKpng' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' , str ( oO0000OOo00 ) , 46 , iiIi1IIiIi + 'SoruceList.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '' , 10050 , iiIi1IIiIi + 'Addons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , str ( oO0000OOo00 ) , 39 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , Oo00OOOOO , '' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
def ii1iII1II ( ) :
 if 28 - 28: o0o00Oo0O * I1ii11iIi11i - oooOo0oo0oo % iI11I1II1I1I * o0ii1I - Ii
 if 7 - 7: I1ii11iIi11i + i1i1I1IIii1II - i1IiiiI1iI % o0ii1I + Ii1I
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']WIZARD[/COLOR]' , str ( oO0000OOo00 ) , 4001 , iiIi1IIiIi + 'Wizard.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']STREAMS[/COLOR]' , str ( oO0000OOo00 ) , 4002 , iiIi1IIiIi + 'Streams.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Tommys Sports[/COLOR]' , '' , 90010 , iiIi1IIiIi + 'tommys.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']G-Tv Live List[/COLOR]' , '' , 40099 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 if 53 - 53: ooOoO0O00 - Iii . OOooOOo
 if oo00 . getSetting ( 'Music' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , str ( oO0000OOo00 ) , 4003 , iiIi1IIiIi + 'Music.png' , Oo00OOOOO , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MAINTENANCE[/COLOR]' , str ( oO0000OOo00 ) , 3 , iiIi1IIiIi + 'Maintenance.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , '' , 90001 , iiIi1IIiIi + 'png' , Oo00OOOOO , '' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
def tools ( ) :
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ADDONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONTACT US[/COLOR]' , '[COLOR' + ooOoOoo0O + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SOURCE LIST[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  oo0OOo0 ( )
 if o0Oo00 == 1 :
  iI ( )
 if o0Oo00 == 2 :
  O0O0Oooo0o ( )
 if o0Oo00 == 3 :
  oOOoo00O00o ( O0O00Oo )
 if o0Oo00 == 4 :
  iIii1 . ok ( i1 , i1111 )
 if o0Oo00 == 5 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if o0Oo00 == 6 :
  oooooo0O000o ( )
  if 64 - 64: oOo0O0Ooo . I11i - i1IiiiI1iI / ii
def O0O0ooOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oOOo0O00o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOOiiiiI , oooOo0OOOoo0 , OOoO in oOOo0O00o :
  iI1Ii1iI11iiI ( OOoO , url , 21009 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  if 89 - 89: I11i + oO0o * Iii * o0ii1I
def iiIiI1i1 ( url ) :
 url = url
 oO0O00oOOoooO = OO0OO0O00oO0 ( )
 if oO0O00oOOoooO ( ) == 'android' :
  try :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.android.browser,android.intent.action.VIEW,' + url + ')' )
  except :
   pass
  else :
   xbmc . executebuiltin ( 'StartAndroidActivity(com.google.chrome,android.intent.action.VIEW,' + url + ')' )
 elif oO0O00oOOoooO ( ) == 'windows' :
  webbrowser . open_new ( url )
  if 46 - 46: oOo0O0Ooo - ii - Iii * IIiIiII11i
  if 34 - 34: Iii - IiI1i11I / oooOo0oo0oo + Ii1I * o0ii1I
def OO ( ) :
 O0O00Oo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , 'GuideSkins' + '.zip' )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( O0O00Oo , ooI1111i , o0oOoO00o )
 iIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIIii
 print '======================================='
 extract . all ( ooI1111i , iIIii , o0oOoO00o )
 o00O0O ( O0O00Oo )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 ii1iii1i ( )
def Iii1I1111ii ( ) :
 ooOoO00 = Ii1IIiI1i ( )
 o0O00Oo0 = ooOoO00 . replace ( II11iiii1Ii , "" )
 if os . path . exists ( ooOoO00 ) or not ooOoO00 == False :
  IiII111i1i11 = open ( ooOoO00 , mode = 'r' ) ; i111iIi1i1II1 = IiII111i1i11 . read ( ) ; IiII111i1i11 . close ( )
  oooO ( "%s - %s" % ( i1 , o0O00Oo0 ) , i111iIi1i1II1 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OO ( ) :
 O0O00Oo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , 'GuideSkins' + '.zip' )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( O0O00Oo , ooI1111i , o0oOoO00o )
 iIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIIii
 print '======================================='
 extract . all ( ooI1111i , iIIii , o0oOoO00o )
 o00O0O ( O0O00Oo )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 ii1iii1i ( )
def i1I1i111Ii ( ) :
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']Todays Games[/COLOR]' , str ( oO0000OOo00 ) , 90030 , iiIi1IIiIi + 'tgames.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Tommys Replays[/COLOR]' , str ( oO0000OOo00 ) , 900300 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 if 67 - 67: oOo0O0Ooo . ooOoO0O00
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 27 - 27: i1iIi % oOo0O0Ooo
def o0oooOO00 ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match eng prem[/COLOR]' , 'http://ourmatch.net/videos/england/premier-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match la liga[/COLOR]' , 'http://ourmatch.net/videos/spain/la-liga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match serie a[/COLOR]' , 'http://ourmatch.net/videos/italy/serie-a-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match bund[/COLOR]' , 'http://ourmatch.net/videos/germany/bundesliga-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match ligue 1[/COLOR]' , 'http://ourmatch.net/videos/france/ligue-1-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']our match uefa champ[/COLOR]' , 'http://ourmatch.net/videos/europe/uefa-champions-league-highlights/' , 900301 , iiIi1IIiIi + 'tommysreplays.png' , '' , '' )
iiIi1IIiIi + 'tommysreplays.png'
def iiIiii1IIIII ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GOAL OF THE MONTH[/COLOR]' , 'http://ourmatch.net/goal-of-the-month/' , 900302 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 o00o = re . compile ( 'href="([^"]*)".+?<img src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIIIiiIiiI = re . compile ( 'class=\'current\'>.+?</span><a class=.+? href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOoO in o00o :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 900302 , iIiIi11 , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for IIIIiI11I11 in IIIIiiIiiI :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , IIIIiI11I11 , 900301 , iiIi1IIiIi + 'NEXT.png' , '' , '' )
def oo00o0 ( url ) :
 i11II1I11I1 = OooOoooOo ( url )
 o00o = re . compile ( "<source src=\"(.+?)\"></video>',.+?'type':'([^']*)'," , re . DOTALL ) . findall ( i11II1I11I1 )
 OOoOO0ooo = re . compile ( "embed:'<iframe src=\"(.+?)\" width=.+? 'type':'([^']*)'," , re . DOTALL ) . findall ( i11II1I11I1 )
 for url , OOoO in o00o :
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
 for url , OOoO in OOoOO0ooo :
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , iiIi1IIiIi + 'tommysreplays.png' , '' )
def II1iIi11 ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIi = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for O0i1iI , IiI1iiiIii in IIi :
  oooO ( '[COLOR' + ooOoOoo0O + ']Tommys List[/COLOR]  ' + O0i1iI , IiI1iiiIii )
def I1III1111iIi ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIi = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 90032 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
def I1i111I ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( I11iiii )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , iIiIi11 , Oo00OOOOO , '' )
 for url in next :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , iiIi1IIiIi + 'NEXT.png' , Oo00OOOOO , '' )
def OooOo0oo0O0o00O ( url ) :
 I11iiii = OooOoooOo ( url )
 I1i11 = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 IiIi1I1 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 IIi = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url in IIi :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for OOoO , url in i1Iii1i1I :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for OOoO , url in IiIi1I1 :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
 for url in I1i11 :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , iiIi1IIiIi + 'tommysreplays.png' , Oo00OOOOO , '' )
  if 39 - 39: IIiIiII11i + OOooOOo - i1iIi . OOooOOo
def OOOooo ( url ) :
 if 'drive' in url :
  OooO0OO ( url )
 else :
  I11iiii = OooOoooOo ( url )
  IIi = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( I11iiii )
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
def Ii1IIiI1i ( ) :
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
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Wizard[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   iiIiii1iI1i ( )
  if o0Oo00 == 1 :
   I1ii1ii11i1I ( )
  if o0Oo00 == 2 :
   o0OoOO ( O0O0Oo00 )
  if o0Oo00 == 3 :
   oOoO00o ( O0O00Oo )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BACKUP MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 10060 , iiIi1IIiIi + 'BackupMyBuild.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']RESTORE MY BUILD[/COLOR]' , str ( oO0000OOo00 ) , 49 , iiIi1IIiIi + 'RestoreMyBuild.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']WIPE GENIE[/COLOR]' , str ( oO0000OOo00 ) , 41 , iiIi1IIiIi + 'WipeGenie.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genie BUILDS[/COLOR]' , str ( oO0000OOo00 ) , 44 , iiIi1IIiIi + 'GenieBuilds.png' , Oo00OOOOO , '' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
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
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzL2RvY3Mv' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
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
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzL2RvY3Mv' ) , 2032 , iiIi1IIiIi + 'boss.png' , Oo00OOOOO , '' )
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
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
def Oo00o0OO0O00o ( ) :
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']FOOTBALL[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KIDS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']NEWS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']HOBBIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DISCLOSE TV[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']CATEGORIES[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  O0Oooo ( )
 if o0Oo00 == 1 :
  iiIi1i ( )
 if o0Oo00 == 2 :
  I1i11111i1i11 ( )
 if o0Oo00 == 3 :
  OOoOOO0 ( )
 if o0Oo00 == 4 :
  I1I1i ( )
 if o0Oo00 == 5 :
  I1IIIiIiIi ( )
  if 27 - 27: Ii1I + OOooOOo - oooOo0oo0oo + o0o00Oo0O . o0ii1I
  if 46 - 46: III1iiIii
  if 45 - 45: i1iIi
def o0OIiII ( ) :
 if not os . path . exists ( ooooooO0oo ) :
  oooO ( 'Change Log 16/3/17 - v3.5.1' , 'All Categories In GTV Live Lists Updated,[CR]BamfTv Added To StreamTeam,[CR] Pirate Movies Added To StreamTeam,[CR]GenieTv Now Krypton Compatible,[CR] G.O.D.S (GenieTv On Demand Soaps) Added To GenieTv,[CR] More Sections Now Available For Download Including Kids,[CR] Tv Guide Removed And Replaced By External App,[CR] Boss Documentaries A Masterpiece By Jason Cadd,[CR] Updates To All Searches,[CR] StreamTeam Cleaned Up,[CR] Addon Overall CleanUp,[CR] General Maintence' )
  os . makedirs ( ooooooO0oo )
  if 21 - 21: i1i1I1IIii1II . i1IiiiI1iI . oooOo0oo0oo / I1ii11iIi11i / i1IiiiI1iI
  if 17 - 17: oooOo0oo0oo / oooOo0oo0oo / Iii
def ii1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']POPCORN BOX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DESI FLIX[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FILM TRAILERS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC MOVIES[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']MOVIES[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   I1IiiI1ii1i ( )
  if o0Oo00 == 1 :
   O0o ( )
  if o0Oo00 == 2 :
   oO0OoO00o ( O0O00Oo )
  if o0Oo00 == 3 :
   II1iiiiII ( )
  if o0Oo00 == 4 :
   O0OoOO0oo0 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if o0Oo00 == 5 :
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
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
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
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']THE SOURCE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']iWATCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RETURN DATES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CLASSIC TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']TV SHOW TRAILERS[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TV SHOWS[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   O0OoO0ooOO0o ( )
  if o0Oo00 == 1 :
   OoOo0oOooOoOO ( )
  if o0Oo00 == 2 :
   oo00ooOoO00 ( )
  if o0Oo00 == 3 :
   o00oOoOo0 ( )
  if o0Oo00 == 4 :
   o0O0O0ooo0oOO ( )
  if o0Oo00 == 5 :
   oo000ii ( )
  if o0Oo00 == 6 :
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
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
def II1i ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   Ii1IIIIi1ii1I = '[COLOR' + ooOoOoo0O + ']PANDORAS BOX[/COLOR]'
   if 13 - 13: oOo0O0Ooo % OOooOOo . Ii1I / I1ii11iIi11i % oooOo0oo0oo . ii
   if 22 - 22: III1iiIii / Ii
   if 62 - 62: oO0o / Ii1I
   if 7 - 7: ii . III1iiIii
  IiI1i = [ Ii1IIIIi1ii1I , '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RAIZ TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ROADRUNNER STREAMS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']StreamTeam[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   O000OOO0OOo ( )
  if o0Oo00 == 1 :
   i1i1I111iIi1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , oo00O00oO000o , OOoO )
  if o0Oo00 == 2 :
   OOo00OoO ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0' ) ) )
  if o0Oo00 == 3 :
   i1i1I111iIi1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , oo00O00oO000o , OOoO )
   if 10 - 10: I11i / Ii
  if o0Oo00 == 4 :
   o00oO ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if o0Oo00 == 5 :
   i1i1I111iIi1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , oo00O00oO000o , OOoO )
 else :
  if 92 - 92: III1iiIii * I1ii11iIi11i * I1ii11iIi11i * oOo0O0Ooo . iI11I1II1I1I
  if 16 - 16: i1iIi % ii - oooOo0oo0oo * o0ii1I * Ii1I / ii
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']PANDORAS BOX[/COLOR]' , str ( oO0000OOo00 ) , 10025 , iiIi1IIiIi + 'PandorasBox.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'Technica-Streams.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'Roadrunner-Streams.png' , Oo00OOOOO , '' )
  if 31 - 31: Iii . i1IiiiI1iI * i1iIi + Ii * i1i1I1IIii1II
  if 93 - 93: Ii1I / iI11I1II1I1I * ooOoO0O00 % ii * o0o00Oo0O * Iii
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'pirate.png' , Oo00OOOOO , '' )
  if 64 - 64: IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / I1ii11iIi11i . i1iIi % III1iiIii
  if 50 - 50: iI11I1II1I1I - III1iiIii + oooOo0oo0oo
  if 69 - 69: o0o00Oo0O
  if 85 - 85: i1iIi / o0o00Oo0O
  if 18 - 18: I11i % o0o00Oo0O * Ii1I
  if 62 - 62: i1IiiiI1iI . III1iiIii . ii
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 11 - 11: oooOo0oo0oo / Iii
def oooO0 ( ) :
 iii ( )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def o00oO ( url ) :
 I11iiii = OooOoooOo ( url )
 iiIIiii = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( I11iiii )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( iiIIiii ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( iiIIiii ) )
 IiIi1I1 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( iiIIiii ) )
 for OOoO , iIiIi11 , url in IIi :
  if '247ch' in url :
   iiIIIiIi1IIi ( OOoO , url , 10190 , iIiIi11 )
  elif '.m3u' in url :
   iiIIIiIi1IIi ( OOoO , url , 1019 , iIiIi11 )
  elif '.xml' in url :
   iiIIIiIi1IIi ( OOoO , url , 1018 , iIiIi11 )
  else :
   ii11i ( OOoO , url , 222 , iIiIi11 )
 for OOoO , url , iIiIi11 in i1Iii1i1I :
  if '.xml' in url :
   iiIIIiIi1IIi ( OOoO , url , 1018 , iIiIi11 )
  elif '.m3u' in url :
   iiIIIiIi1IIi ( OOoO , url , 1019 , iIiIi11 )
  else :
   ii11i ( OOoO , url , 222 , iIiIi11 )
 for OOoO , url , iIiIi11 in IiIi1I1 :
  ii11i ( OOoO , url , 8043 , iIiIi11 )
def III11II1I1Ii1 ( url ) :
 II11iIiIIIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def oO0o00oOOooO0 ( url ) :
 II11iIiIIIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url , iIiIi11 in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iIiIi11 )
  if 79 - 79: oO0o - iI11I1II1I1I + o0ii1I - i1IiiiI1iI
def OoOiIIiii ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , iiIi1IIiIi + 'scraped.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , iiIi1IIiIi + 'newaddmagic.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLORred]****[/COLOR][COLOR' + ooOoOoo0O + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , iiIi1IIiIi + 'newaddsit.png' , Oo00OOOOO , '' )
 if 61 - 61: III1iiIii . ooOoO0O00 / i1IiiiI1iI % Ii * IiI1i11I
def i1i1i1I ( url ) :
 II11iIiIIIiI = oOoo000 ( url )
 IIi = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for OOoO , url , OooOo00o , IiI11i1IIiiI , oooOo0OOOoo0 , OOOiiiiI in IIi :
  if IiI11i1IIiiI == '123' :
   IiI11i1IIiiI = iiIi1IIiIi + 'appstreams.png'
  if oooOo0OOOoo0 == '123' :
   oooOo0OOOoo0 = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100010 , IiI11i1IIiiI , oooOo0OOOoo0 , OOOiiiiI )
  elif 'playlist' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100007 , IiI11i1IIiiI , oooOo0OOOoo0 , OOOiiiiI )
  elif 'watchseries' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100100 , IiI11i1IIiiI , oooOo0OOOoo0 , OOOiiiiI )
  elif not 'http' in url :
   oOOo000oOoO0 ( OOoO , url , 100009 , IiI11i1IIiiI , oooOo0OOOoo0 , OOOiiiiI , '' )
  else :
   oOOo000oOoO0 ( OOoO , url , 100005 , IiI11i1IIiiI , oooOo0OOOoo0 , OOOiiiiI , '' )
   if 86 - 86: IIiIiII11i % Ii + o0ii1I % Ii
def Ooo0o0OOO ( url ) :
 II11iIiIIIiI = oOoo000 ( url )
 oOOo0O00o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOOiiiiI , oooOo0OOOoo0 , OOoO in oOOo0O00o :
  if iIiIi11 == '123' :
   iIiIi11 = iiIi1IIiIi + 'appstreams.png'
  if oooOo0OOOoo0 == '123' :
   oooOo0OOOoo0 = Oo00OOOOO
  if 'php' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100004 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  elif 'playlist' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100007 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  elif 'watchseries' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100100 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  elif not 'http' in url :
   oOOo000oOoO0 ( OOoO , url , 100009 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI , '' )
  else :
   oOOo000oOoO0 ( OOoO , url , 100005 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI , '' )
   if 35 - 35: oooOo0oo0oo + IiI1i11I
def iI1IIIii ( url ) :
 if 7 - 7: III1iiIii - Iii / IIiIiII11i * o0ii1I . IiI1i11I * IiI1i11I
 II11iIiIIIiI = oOoo000 ( url )
 O0O0oOOo0O = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iiIIiii in O0O0oOOo0O :
  IiI11i1IIiiI = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( iiIIiii ) )
  for IiI11i1IIiiI in IiI11i1IIiiI :
   IiI11i1IIiiI = IiI11i1IIiiI
  OOoO = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( iiIIiii ) )
  for OOoO in OOoO :
   if 'elete' in OOoO :
    pass
   elif 'rivate Vid' in OOoO :
    pass
   else :
    OOoO = ( OOoO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  II11 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( iiIIiii ) )
  for II11 in II11 :
   II11 = II11
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( iiIIiii ) )
  for url in url :
   url = url
  oOOo000oOoO0 ( '[COLORred]' + str ( II11 ) + '[/COLOR] : ' + str ( OOoO ) , str ( url ) , 100009 , str ( IiI11i1IIiiI ) , Oo00OOOOO , '' , '' )
  oOI1Ii1I1 ( 'movies' , '' )
  if 68 - 68: IiI1i11I * ii * iI11I1II1I1I . IIiIiII11i
  if 81 - 81: oooOo0oo0oo / o0o00Oo0O + Iii + o0ii1I / oOo0O0Ooo
  if 27 - 27: OOooOOo * III1iiIii
  if 59 - 59: III1iiIii . III1iiIii - IIiIiII11i + III1iiIii . ooOoO0O00 . oO0o
def Oo00OOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oOOo0O00o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOOiiiiI , oooOo0OOOoo0 , OOoO in oOOo0O00o :
  if '.php' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100210 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  else :
   iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
   if 64 - 64: IIiIiII11i
   if 77 - 77: OOooOOo % o0ii1I
   if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def ii1Ii1IiIIi ( iconimage , url , extra ) :
 IiI11i1IIiiI = ' '
 o0OO0oOo00Oo0o0Oo = ' '
 oooOo0OOOoo0 = ' '
 I1 = ' '
 I1O0 = oOoo000 ( url )
 IiI11i1IIiiI = re . compile ( '<img src="(.+?)">' ) . findall ( I1O0 )
 for IiI11i1IIiiI in IiI11i1IIiiI :
  IiI11i1IIiiI = IiI11i1IIiiI
 iIi1IiII = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( I1O0 )
 for oooOo0OOOoo0 in iIi1IiII :
  oooOo0OOOoo0 = oooOo0OOOoo0
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( I1O0 )
 for url , I1 in IIi :
  I1 = 'S' + ( I1 ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  I1i ( ( I1 ) . replace ( '  ' , '' ) , url , 100101 , IiI11i1IIiiI , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo , '' )
  oOI1Ii1I1 ( 'Movies' , 'info' )
  if 72 - 72: iI11I1II1I1I
def iiIi ( url , name , fanart , extra , iconimage ) :
 oOIi111 = extra
 I1 = name
 I1O0 = oOoo000 ( url )
 IiI11i1IIiiI = iconimage
 IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( I1O0 )
 for url , name , oO0i1iI in IIi :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oOOoo0Oo + url
  oO0i1iI = oO0i1iI
  iioo0o0OoOOO = name + ' - [COLORred]' + oO0i1iI + '[/COLOR]'
  I1i ( iioo0o0OoOOO , url , 100102 , IiI11i1IIiiI , fanart , 'Aired : ' + oO0i1iI , iioo0o0OoOOO )
  if 88 - 88: IiI1i11I
def iiI11I1i1i1iI ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = oOoo000 ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , name in IIi :
  for iII1i11 in o00OO00OoO :
   if iII1i11 in O0O00Oo :
    URL = 'http://www.watchseriesgo.to/link/' + O0O00Oo
    oOOo000oOoO0 ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  I1i ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 60 - 60: ii % I1ii11iIi11i + oooOo0oo0oo . i1iIi * iI11I1II1I1I
  if 93 - 93: oO0o
def i111I ( url , name ) :
 OOO0oOoO0O = name
 II11iIiIIIiI = oOoo000 ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OoOo000oOo0oo ( url , OOO0oOoO0O )
 for url in i1Iii1i1I :
  OoOo000oOo0oo ( url , OOO0oOoO0O )
 for url in IiIi1I1 :
  OoOo000oOo0oo ( url , OOO0oOoO0O )
  if 65 - 65: OOooOOo / oO0o % III1iiIii
def OoOo000oOo0oo ( url , season_name ) :
 if 'daclips.in' in url :
  iIiIIii ( url , season_name )
 elif 'filehoot.com' in url :
  OOo00 ( url , season_name )
 elif 'allmyvideos.net' in url :
  iIII ( url , season_name )
 elif 'vidspot.net' in url :
  Ii1iI11iI1 ( url , season_name )
 elif 'vodlocker' in url :
  i11I1II ( url , season_name )
 elif 'vidto' in url :
  OO0 ( url , season_name )
  if 84 - 84: OOooOOo % i1iIi - OOooOOo . I11i
  if 5 - 5: OOooOOo * i1IiiiI1iI - Ii1I / iI11I1II1I1I % i1i1I1IIii1II + III1iiIii
def OO0 ( url , season_name ) :
 II11iIiIIIiI = oOoo000 ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00o00OoO00o0 , OOoO in IIi :
  OOoOoO00O0O0o ( o00o00OoO00o0 , season_name )
  if 12 - 12: Ii1I + oO0o % Iii
  if 85 - 85: IiI1i11I * I11i
def iIII ( url , season_name ) :
 II11iIiIIIiI = oOoo000 ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00o00OoO00o0 , OOoO in IIi :
  OOoOoO00O0O0o ( o00o00OoO00o0 , season_name )
  if 3 - 3: oooOo0oo0oo
def Ii1iI11iI1 ( url , season_name ) :
 II11iIiIIIiI = oOoo000 ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for o00o00OoO00o0 , OOoO in IIi :
  OOoOoO00O0O0o ( o00o00OoO00o0 , season_name )
  if 20 - 20: IIiIiII11i . IiI1i11I / IIiIiII11i % Ii % IiI1i11I
def i11I1II ( url , season_name ) :
 II11iIiIIIiI = oOoo000 ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00o00OoO00o0 in IIi :
  OOoOoO00O0O0o ( o00o00OoO00o0 , season_name )
  if 11 - 11: III1iiIii % Ii1I % o0ii1I / IIiIiII11i % i1IiiiI1iI - I1ii11iIi11i
def iIiIIii ( url , season_name ) :
 II11iIiIIIiI = oOoo000 ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for o00o00OoO00o0 in IIi :
  OOoOoO00O0O0o ( o00o00OoO00o0 , season_name )
  if 96 - 96: Ii1I / IIiIiII11i . o0ii1I - IiI1i11I * Iii * i1i1I1IIii1II
def OOo00 ( url , season_name ) :
 II11iIiIIIiI = oOoo000 ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for o00o00OoO00o0 in IIi :
  OOoOoO00O0O0o ( o00o00OoO00o0 , season_name )
  if 76 - 76: o0ii1I - IIiIiII11i * oooOo0oo0oo / ii
def OOoOoO00O0O0o ( Link , season_name ) :
 if 'http:/' in Link :
  IIIiIi ( Link )
  if 34 - 34: ii . o0o00Oo0O / i1i1I1IIii1II * OOooOOo - Ii1I
def IiiiI ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 Iiii1I1 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in Iiii1I1 :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 83 - 83: oooOo0oo0oo . i1IiiiI1iI + i1i1I1IIii1II - oooOo0oo0oo * i1IiiiI1iI / i1IiiiI1iI
def I1i ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111I11i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1OoOO = [ ]
  if 44 - 44: oooOo0oo0oo
  if showcontext == 'fav' :
   ii1OoOO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   ii1OoOO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111I11i . addContextMenuItems ( ii1OoOO )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = True )
 return iiI1i1Iii111
 if 54 - 54: o0ii1I - Iii - i1IiiiI1iI . iI11I1II1I1I
 if 79 - 79: o0ii1I . oO0o
def oOOo000oOoO0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111I11i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1OoOO = [ ]
  ii1OoOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1OoOO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   ii1OoOO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111I11i . addContextMenuItems ( ii1OoOO )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = False )
 return iiI1i1Iii111
 if 40 - 40: I11i + I1ii11iIi11i . I11i % i1iIi
def I11I1IIiiII1 ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 31 - 31: oOo0O0Ooo * i1i1I1IIii1II + ii - IiI1i11I / ii
def I111IIiii1Ii ( url ) :
 II1 = xbmc . Player ( iiIIIiIii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : II1 . play ( url ) . strip ( )
 except : pass
 if 23 - 23: IiI1i11I + Iii . OOooOOo * oOo0O0Ooo + Ii1I
def IIIiIi ( url ) :
 II1 = xbmc . Player ( )
 import urlresolver
 try : II1 . play ( url )
 except : pass
 if 18 - 18: III1iiIii * I11i . III1iiIii / o0o00Oo0O
def oOoo000 ( url ) :
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
  if 8 - 8: I11i
  if 4 - 4: Ii1I + Ii1I * i1iIi - OOooOOo
  if 78 - 78: o0ii1I / IIiIiII11i % OOooOOo
def iiIi1i ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   oO00OoOO ( )
  if o0Oo00 == 1 :
   I11IIiIiI ( )
  if o0Oo00 == 2 :
   iIIIi1i1I11i ( )
  if o0Oo00 == 3 :
   oOO0OO0OO ( )
  if o0Oo00 == 4 :
   oOOoooO ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'SearchCartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( oO0000OOo00 ) , 21004 , iiIi1IIiIi + 'watchcartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '' , 10001 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '' , 20000 , iiIi1IIiIi + 'Cartoons.png' , Oo00OOOOO , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , iiIi1IIiIi + 'anime.png' , Oo00OOOOO , '' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
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
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 22 - 22: Iii + iI11I1II1I1I
 if 24 - 24: OOooOOo % ooOoO0O00 + IiI1i11I . Ii . Ii1I
 if 17 - 17: Ii1I . IIiIiII11i . i1iIi / Ii1I
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   oOooO00o0O = ( II1I ) . replace ( 'special://home/addons/' , '' )
   oooO ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + oOooO00o0O + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   o0Oo00 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if o0Oo00 == 0 :
    OOo0 ( II1I )
    ii1iii1i ( )
   elif o0Oo00 == 1 :
    iiIii1IIi ( II1I )
  else :
   pass
   if 10 - 10: Ii - I11i % iI11I1II1I1I
def iiIii1IIi ( addon ) :
 oOooO00o0O = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 49 - 49: i1i1I1IIii1II
def OOo0 ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OOOOoOo00OO = os . path . join ( IIIII , 'default.py' )
 OooOo0o0Oo = open ( OOOOoOo00OO , "w+" )
 if 71 - 71: iI11I1II1I1I - oooOo0oo0oo . oOo0O0Ooo % ii + oooOo0oo0oo
 OooOo0o0Oo . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 OooOo0o0Oo . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 OooOo0o0Oo . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 26 - 26: I1ii11iIi11i + oooOo0oo0oo / oO0o % OOooOOo % Ii1I + IIiIiII11i
 if 31 - 31: Iii % oooOo0oo0oo * Iii
 if 45 - 45: ooOoO0O00 . oOo0O0Ooo + oooOo0oo0oo - ii % i1iIi
 if 1 - 1: iI11I1II1I1I
def OOo00OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 ooi1II1I = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOoO0ooOO = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1i11 = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iii1IIII1iii11I = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url , oo0OoOooo , oooOo0OOOoo0 , OOOiiiiI in ooi1II1I :
  if 'php' in url :
   Iii1I1I11iiI1 ( OOoO , url , 90037 , oo0OoOooo , oooOo0OOOoo0 , OOOiiiiI )
  elif OOoO == 'Search' :
   Iii1I1I11iiI1 ( 'Search' , url , 90038 , oo0OoOooo , oooOo0OOOoo0 , OOOiiiiI )
  else :
   iI1Ii1iI11iiI ( OOoO , url , 222 , oo0OoOooo , oooOo0OOOoo0 , OOOiiiiI )
 for OOoO , iIiIi11 , url , O00O00O000OOO in OOoO0ooOO :
  Iii1I1I11iiI1 ( OOoO , url , 90037 , iIiIi11 , O00O00O000OOO , '' )
 for OOoO , iIiIi11 , url , O00O00O000OOO in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 90037 , iIiIi11 , O00O00O000OOO , '' )
 for OOoO , url , iIiIi11 , O00O00O000OOO in i1Iii1i1I :
  iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , O00O00O000OOO , '' )
 for OOoO , url , iIiIi11 , O00O00O000OOO in IiIi1I1 :
  iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , O00O00O000OOO , '' )
 for OOoO , url , iIiIi11 , O00O00O000OOO in I1i11 :
  iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , O00O00O000OOO , '' )
 for OOoO , url , iIiIi11 in iii1IIII1iii11I :
  iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , '' , '' )
  oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
def iIOo0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , iIiIi11 , url , O00O00O000OOO in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 90037 , iIiIi11 , O00O00O000OOO , '' )
 for OOoO , url , iIiIi11 , O00O00O000OOO in i1Iii1i1I :
  iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , O00O00O000OOO , '' )
  oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
  if 1 - 1: o0o00Oo0O / IiI1i11I % i1IiiiI1iI . I1ii11iIi11i + III1iiIii
def I1Ii11iiiI ( ) :
 i1II1IiIII111 = [ 'serialsearch' , 'moviesearch' ]
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 if O0ooOoO == '' :
  pass
 else :
  for IIII in i1II1IiIII111 :
   iI1iiiIiii = Oo0o0000o0o0 + IIII + '.php'
   I1O0 = OooOoooOo ( iI1iiiIiii )
   if I1O0 != 'Opened' :
    oOOo0O00o = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( I1O0 )
    for OOoO , O0O00Oo , oo0OoOooo , oooOo0OOOoo0 , OOOiiiiI in oOOo0O00o :
     if O0ooOoO in OOoO . lower ( ) :
      ii1i1i = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in ii1i1i :
       if iII1i11 == O0O00Oo :
        OOoO = '[COLORred]* [/COLOR]' + ( OOoO ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        II11iIII1i1I = open ( OOOO0OOoO0O0 , "a" )
        II11iIII1i1I . write ( 'item="' + OOoO + '"\n' )
        II11iIII1i1I . close
      if 'php' in O0O00Oo :
       Iii1I1I11iiI1 ( OOoO , O0O00Oo , 90037 , oo0OoOooo , oooOo0OOOoo0 , OOOiiiiI )
      else :
       iI1Ii1iI11iiI ( OOoO , O0O00Oo , 222 , oo0OoOooo , oooOo0OOOoo0 , OOOiiiiI )
       if 63 - 63: I1ii11iIi11i + i1IiiiI1iI - IIiIiII11i
   oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
   if 2 - 2: III1iiIii
def oOo0O0O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://www.tvcatchup.com/channels/' )
 o0o = OooOoooOo ( 'http://www.djing.com/' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img style="" src="([^"]*)" alt="([^"]*)"/>.+?<br/>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oOoo0 = re . compile ( 'title="([^"]*)".+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( o0o )
 for O0O00Oo , iIiIi11 , I1iiiiii , OOoO in IIi :
  ii11i ( ( '[COLORgold]' + I1iiiiii + '[/COLOR][COLORwhite] - [COLORsteelblue]' + OOoO + '[/COLOR]' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' ) , 'http://www.tvcatchup.com' + O0O00Oo , 90024 , iIiIi11 )
 for I1IIIii , O0O00Oo , iIiIi11 in oOoo0 :
  ii11i ( I1IIIii , 'http://www.tvcatchup.com' + O0O00Oo , 90024 , iIiIi11 )
 for O0O00Oo , iIiIi11 , OOoO in i1Iii1i1I :
  if 'Submit' in OOoO :
   pass
  elif '&lt;' in OOoO :
   pass
  else :
   iI1Ii1iI11iiI ( '[COLORgold]DJing  [/COLOR][COLORwhite]- [COLORsteelblue]' + OOoO + '[/COLOR]' , O0O00Oo , 90025 , 'http://www.djing.com' + iIiIi11 , Oo00OOOOO , '' )
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
def o0OO0Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 3 - 3: i1IiiiI1iI - o0o00Oo0O % iI11I1II1I1I / III1iiIii . I11i
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def iiiiI1iiiIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  o0oO0OoO0 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 70 - 70: i1i1I1IIii1II - i1i1I1IIii1II
def O0o ( ) :
 if 57 - 57: oOo0O0Ooo - I11i + oO0o % I1ii11iIi11i
 if 26 - 26: IiI1i11I . IiI1i11I
 if 35 - 35: i1IiiiI1iI . OOooOOo * Ii
 if 44 - 44: Ii / I1ii11iIi11i
 if 42 - 42: ii + I1ii11iIi11i % IIiIiII11i + oO0o
 if 24 - 24: IiI1i11I * IIiIiII11i % IiI1i11I % III1iiIii + ii
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'yr' in O0O00Oo :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + O0O00Oo , 10201 , iiIi1IIiIi + 'rated.png' )
   if 29 - 29: IIiIiII11i - ii - Ii . I11i
def i11ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i11I1 , url , OOoO in IIi :
  if 'id' in url :
   iiIIIiIi1IIi ( ( '[COLORred]RANK [COLORblue]' + i11I1 + '[COLORred] - [COLORblue]' + OOoO + '[/COLOR]' ) , OOoO , 10202 , iiIi1IIiIi + 'rated.png' )
   if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + IiI1i11I * iI11I1II1I1I % o0ii1I
def I1iI1I1 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 IiIi1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiiIi1IIII1i = ( url )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 oo00ooOoo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 iii1IIIiiiI = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OoO00oo00 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 iiiI1i11Ii = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIiII = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IiiIi1IIII1i
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 oo0o0oOo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 58 - 58: I11i - IIiIiII11i % i1i1I1IIii1II + i1IiiiI1iI . OOooOOo / III1iiIii
 IIo00ooo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 Ii1IiIiIi1IiI = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 36 - 36: III1iiIii - ii / oO0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( oo00ooOoo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iii1IIIiiiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( OoO00oo00 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 iIIi1iI1I1IIi = O00O0oOO00O00 ( Oo0Oo0O )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 O0OO0 = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O0ooo0o0 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 oO0ooOoO = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 59 - 59: o0o00Oo0O % I1ii11iIi11i
 if 92 - 92: o0ii1I % IiI1i11I / Ii1I % Ii1I * oOo0O0Ooo
 Oo = O00O0oOO00O00 ( IIo00ooo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 oO00oOOo0Oo = O00O0oOO00O00 ( Ii1IiIiIi1IiI )
 if 5 - 5: I11i . o0o00Oo0O / I1ii11iIi11i % oO0o
 if 60 - 60: IIiIiII11i / iI11I1II1I1I + Ii1I . Ii
 if 40 - 40: I11i
 if 78 - 78: iI11I1II1I1I
 if 56 - 56: ii - Iii - ooOoO0O00
 if 8 - 8: i1IiiiI1iI / oooOo0oo0oo . oOo0O0Ooo + Ii1I / Ii
 if 31 - 31: i1iIi - iI11I1II1I1I + IiI1i11I . I1ii11iIi11i / III1iiIii % iI11I1II1I1I
 if 6 - 6: III1iiIii * Ii % iI11I1II1I1I % Ii + I11i / ooOoO0O00
 if 53 - 53: Iii + iI11I1II1I1I
 if 70 - 70: Ii1I
 if 67 - 67: ii
 if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + oooOo0oo0oo * III1iiIii
 if 2 - 2: ooOoO0O00 - i1iIi + oOo0O0Ooo . I11i * I11i / OOooOOo
 if oO0ooOoO != 'Failed' :
  oOOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oO0ooOoO )
  for url , OOoO in oOOO :
   iIi1I1 = O00O0oOO00O00 ( url )
   O0oOoo0OoO0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi1I1 )
   for oo00IiI1 , oOo00o00oO in O0oOoo0OoO0O :
    oOo00o00oO = ( oOo00o00oO . replace ( '.' , ' ' ) )
    if O0ooOoO in oOo00o00oO . lower ( ) :
     if '.mkv' in oo00IiI1 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + oo00IiI1 , 222 , '' , '' , '' )
     elif '.mp4' in oo00IiI1 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + oo00IiI1 , 222 , '' , '' , '' )
     elif '.avi' in oo00IiI1 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + oo00IiI1 , 222 , '' , '' , '' )
     elif '.wav' in oo00IiI1 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + oo00IiI1 , 222 , '' , '' , '' )
     else :
      Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + oo00IiI1 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 95 - 95: oOo0O0Ooo
      oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in i1Iii1i1I :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 88 - 88: III1iiIii % oO0o + i1IiiiI1iI + i1IiiiI1iI * IIiIiII11i
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 78 - 78: ii
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for OOoo0 , OOoO in IiIi1I1 :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iii1IIIiiiI + OOoo0 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in I1i11 :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 36 - 36: I11i + Iii - III1iiIii + iI11I1II1I1I + ii
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if iIIi1iI1I1IIi != 'Failed' :
  IiI1i111IiIiIi1 = [ ]
  iii1IIII1iii11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi1iI1I1IIi )
  for url , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in iii1IIII1iii11I :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    if OOoO in IiI1i111IiIiIi1 :
     pass
    else :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
     IiI1i111IiIiIi1 . append ( OOoO )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if O0OO0 != 'Failed' :
  i1II11II1 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( O0OO0 )
  for url , iIiIi11 , OOoO in i1II11II1 :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , iIiIi11 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 5 - 5: I1ii11iIi11i - Ii1I % i1i1I1IIii1II - IIiIiII11i . oOo0O0Ooo + IiI1i11I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 47 - 47: o0o00Oo0O - iI11I1II1I1I - IiI1i11I
    if 46 - 46: o0ii1I . oooOo0oo0oo * oO0o . ii + Ii1I
    if 72 - 72: IIiIiII11i + oooOo0oo0oo
    if 91 - 91: iI11I1II1I1I % oO0o . I11i + o0ii1I + I11i
    if 95 - 95: o0ii1I + Ii1I * oooOo0oo0oo
    if 16 - 16: Iii / oOo0O0Ooo + oO0o % iI11I1II1I1I - ooOoO0O00 . i1i1I1IIii1II
    if 26 - 26: I11i * III1iiIii . ooOoO0O00
    if 59 - 59: o0o00Oo0O + ooOoO0O00 - I11i
    if 62 - 62: Ii % oooOo0oo0oo . III1iiIii . oooOo0oo0oo
    if 84 - 84: Ii * oO0o
    if 18 - 18: oooOo0oo0oo - o0ii1I - OOooOOo / i1IiiiI1iI - o0o00Oo0O
    if 30 - 30: o0o00Oo0O + Ii1I + IIiIiII11i
    if 14 - 14: I11i / oooOo0oo0oo - iI11I1II1I1I - i1i1I1IIii1II % i1iIi
    if 49 - 49: i1iIi * i1i1I1IIii1II / I11i / I1ii11iIi11i * iI11I1II1I1I
    if 57 - 57: OOooOOo - i1i1I1IIii1II / i1iIi % Ii
    if 3 - 3: IiI1i11I . i1iIi % oOo0O0Ooo + Ii1I
    if 64 - 64: ooOoO0O00
    if 29 - 29: I11i / Ii / oOo0O0Ooo % i1i1I1IIii1II % Ii
 if Oo != 'Failed' :
  i111II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo )
  for url , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in i111II :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 63 - 63: oOo0O0Ooo - oO0o % IiI1i11I % Iii / I11i / ooOoO0O00
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 69 - 69: I1ii11iIi11i * IIiIiII11i * i1iIi . IiI1i11I - Ii1I
    if 39 - 39: o0ii1I * oOo0O0Ooo % oO0o . OOooOOo
    if 24 - 24: ooOoO0O00 * iI11I1II1I1I / o0ii1I
    if 78 - 78: Ii + I11i + i1IiiiI1iI / I11i % iI11I1II1I1I % III1iiIii
    if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % i1IiiiI1iI . Ii1I % o0o00Oo0O
    if 47 - 47: I11i
    if 66 - 66: oOo0O0Ooo - III1iiIii
    if 33 - 33: oOo0O0Ooo / oO0o
    if 12 - 12: IIiIiII11i
    if 2 - 2: ooOoO0O00 - oOo0O0Ooo + Iii . IIiIiII11i
 iIIiI1iiI = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 18 - 18: IiI1i11I - i1i1I1IIii1II % IiI1i11I / Iii
 for IIII in iIIiI1iiI :
  iI1iiiIiii = oO0 + IIII + oOoOooOo0o0
  oO0ooOoO = O00O0oOO00O00 ( iI1iiiIiii )
  if oO0ooOoO != 'Failed' :
   oOOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0ooOoO )
   for url , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in oOOO :
    if IiiIi1IIII1i in OOoO . lower ( ) :
     iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 68 - 68: o0ii1I * iI11I1II1I1I + i1IiiiI1iI % OOooOOo
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
     if 46 - 46: OOooOOo % ooOoO0O00 / i1i1I1IIii1II * I1ii11iIi11i * oooOo0oo0oo
 iIIiI1iiI = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 67 - 67: OOooOOo * OOooOOo . OOooOOo + o0ii1I / i1i1I1IIii1II
 if 13 - 13: IiI1i11I
 for IIII in iIIiI1iiI :
  iI1iiiIiii = IiIi1 + IIII
  o0OOOOO0O = O00O0oOO00O00 ( iI1iiiIiii )
  if o0OOOOO0O != 'Failed' :
   I1I1IiIi1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( o0OOOOO0O )
   for OOoo0 , OOoO in I1I1IiIi1 :
    if IiiIi1IIII1i in OOoO . lower ( ) :
     ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( IiIi1 + IIII + OOoo0 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 58 - 58: OOooOOo - IiI1i11I - ii
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: iI11I1II1I1I
def o0O0O0ooo0oOO ( ) :
 iiIIIiIi1IIi ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 iiIIIiIi1IIi ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 iiIIIiIi1IIi ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 iiIIIiIi1IIi ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 oOI1Ii1I1 ( 'tvshows' , 'INFO' )
 if 82 - 82: OOooOOo + o0o00Oo0O - III1iiIii % i1i1I1IIii1II * Ii
def iIIi1iI1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , I1 , I1Iii1I , oO0i1iI , iIi11I in IIi :
  iiIIIiIi1IIi ( ( '[COLORblue]' + OOoO + '[/COLOR] [COLORred]Season[/COLOR]-' + I1 + ' [COLORred]Returns [/COLOR]- ' + iIi11I + ' ' + oO0i1iI ) , OOoO , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 87 - 87: Iii / oOo0O0Ooo + I1ii11iIi11i + oooOo0oo0oo - ii + I1ii11iIi11i
def O00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , I1 , I1Iii1I in IIi :
  iiIIIiIi1IIi ( ( '[COLORblue]' + OOoO + '[/COLOR] [COLORred]Season[/COLOR]-' + I1 + ' [COLORred] Status Unknown[/COLOR] ' ) , OOoO , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 14 - 14: Ii
def o0oOOO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , I1 , I1Iii1I , oO0i1iI in IIi :
  iiIIIiIi1IIi ( ( '[COLORblue]' + OOoO + ' [COLORred] Cancelled On[/COLOR] ' + oO0i1iI ) , OOoO , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 61 - 61: I11i / OOooOOo - I1ii11iIi11i
def I1iIIII1 ( url ) :
 IiiIi1IIII1i = ( url )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 if 57 - 57: OOooOOo . iI11I1II1I1I % i1iIi % o0ii1I * OOooOOo
 if 8 - 8: OOooOOo . i1iIi % i1i1I1IIii1II . oOo0O0Ooo % oOo0O0Ooo . o0ii1I
 oo00IiI1 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 oo00ooOoo = 'http://onlinemovies.tube/?s=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 iii1IIIiiiI = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 OoO00oo00 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 iiiI1i11Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 47 - 47: Iii + i1iIi + IIiIiII11i % Ii
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 oo0o0oOo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 OOoOoo00Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 18 - 18: oO0o . IIiIiII11i % OOooOOo % o0ii1I
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 87 - 87: iI11I1II1I1I . ii * OOooOOo
 if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % o0ii1I - iI11I1II1I1I
 i11II1I11I1 = O00O0oOO00O00 ( oo00IiI1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( oo00ooOoo )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iii1IIIiiiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( OoO00oo00 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 o0OOOOO0O = O00O0oOO00O00 ( iiiI1i11Ii )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 17 - 17: Iii / I11i % I1ii11iIi11i
 if 71 - 71: III1iiIii . i1IiiiI1iI . oO0o
 O0ooo0o0 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 oO0ooOoO = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 Oo0O0O00Oo = O00O0oOO00O00 ( OOoOoo00Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 10 - 10: o0ii1I + Iii % ii - oOo0O0Ooo
 if oO0ooOoO != 'Failed' :
  oOOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oO0ooOoO )
  for url , OOoO in oOOO :
   iIi1I1 = O00O0oOO00O00 ( url )
   O0oOoo0OoO0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi1I1 )
   for oo00IiI1 , oOo00o00oO in O0oOoo0OoO0O :
    if O0ooOoO in oOo00o00oO . lower ( ) :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + oo00IiI1 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 70 - 70: oooOo0oo0oo - IiI1i11I
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if O0ooo0o0 != 'Failed' :
  iIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0ooo0o0 )
  for url , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in iIi :
   if O0ooOoO in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 29 - 29: o0o00Oo0O . i1IiiiI1iI
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 66 - 66: i1i1I1IIii1II * iI11I1II1I1I % iI11I1II1I1I * III1iiIii - i1iIi - III1iiIii
    if 70 - 70: i1IiiiI1iI + i1i1I1IIii1II
    if 93 - 93: i1IiiiI1iI + o0ii1I
    if 33 - 33: o0o00Oo0O
    if 78 - 78: o0o00Oo0O / IIiIiII11i * oO0o
    if 50 - 50: ii - iI11I1II1I1I + ooOoO0O00 % i1IiiiI1iI - iI11I1II1I1I % o0o00Oo0O
    if 58 - 58: III1iiIii + iI11I1II1I1I
    if 65 - 65: IIiIiII11i - i1IiiiI1iI % I11i - OOooOOo * IiI1i11I + o0ii1I
    if 79 - 79: i1iIi . OOooOOo % i1IiiiI1iI - I1ii11iIi11i
    if 69 - 69: i1iIi - I11i . i1iIi
    if 9 - 9: i1i1I1IIii1II % Ii / I1ii11iIi11i
 if Oo0O0O00Oo != 'Failed' :
  IIIiI1ii1IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo0O0O00Oo )
  for url , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in IIIiI1ii1IIi :
   if O0ooOoO in OOoO . lower ( ) :
    iiIIIiIi1IIi ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 55 - 55: IiI1i11I - oO0o
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  o0i1I11iI1iiI = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , iIiIi11 , OOoO , I1ii in i1Iii1i1I :
   if O0ooOoO in OOoO . lower ( ) :
    if 'season' in I1ii :
     iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , iIiIi11 , iIiIi11 , '' )
    if 'episodes' in I1ii :
     iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , iIiIi11 , iIiIi11 , '' )
  for url in o0i1I11iI1iiI :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 80 - 80: Ii1I / iI11I1II1I1I % OOooOOo
   oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if i11II1I11I1 != 'Failed' :
  OOoO0ooOO = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( i11II1I11I1 )
  for url , OOoO , iIiIi11 in OOoO0ooOO :
   if O0ooOoO in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( OOoO ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , iIiIi11 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 80 - 80: oO0o % IiI1i11I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 99 - 99: i1iIi / iI11I1II1I1I - o0ii1I * Ii1I % oOo0O0Ooo
    if 13 - 13: oO0o
    if 70 - 70: i1IiiiI1iI + o0o00Oo0O . i1i1I1IIii1II * o0ii1I
    if 2 - 2: ii . oooOo0oo0oo . III1iiIii
    if 42 - 42: oooOo0oo0oo % i1i1I1IIii1II / oO0o - i1i1I1IIii1II * Ii
    if 19 - 19: i1i1I1IIii1II * oOo0O0Ooo % Ii
    if 24 - 24: I11i
    if 10 - 10: I11i % o0ii1I / oooOo0oo0oo
    if 28 - 28: oooOo0oo0oo % i1iIi
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for OOoO in IiIi1I1 :
   if O0ooOoO in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iii1IIIiiiI + OOoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 48 - 48: Ii % i1i1I1IIii1II
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for OOoO in I1i11 :
   if O0ooOoO in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( OoO00oo00 + OOoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 29 - 29: IiI1i11I + Ii % Iii
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0OOOOO0O != 'Failed' :
  I1I1IiIi1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OOOOO0O )
  for url , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in I1I1IiIi1 :
   if O0ooOoO in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 93 - 93: OOooOOo % iI11I1II1I1I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 90 - 90: oOo0O0Ooo - oooOo0oo0oo / o0ii1I / o0o00Oo0O / Iii
 oOO0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for IIII in oOO0 :
  iI1iiiIiii = oO0 + IIII + oOoOooOo0o0
  Oo = O00O0oOO00O00 ( iI1iiiIiii )
  if Oo != 'Failed' :
   i111II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Oo )
   for OOoO , OOOiiiiI , url , iIiIi11 , oooOo0OOOoo0 , OooOo00o in i111II :
    if O0ooOoO in OOoO . lower ( ) :
     Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - Source Pandoras[/COLOR]' , url , OooOo00o , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 15 - 15: I1ii11iIi11i + Iii . i1iIi - iI11I1II1I1I / o0o00Oo0O % iI11I1II1I1I
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
     if 86 - 86: oOo0O0Ooo / i1i1I1IIii1II * o0ii1I
     if 64 - 64: i1iIi / o0o00Oo0O * OOooOOo * i1iIi
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: Iii / ooOoO0O00 % Ii1I / Ii1I * Ii1I . Ii
def o0oOO00 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( ( OOoO ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + O0O00Oo , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + O0O00Oo )
def ii11iiIi ( url ) :
 i11iI11I1I = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( i11iI11I1I )
 sys . exit ( 1 )
 if 47 - 47: o0o00Oo0O * oOo0O0Ooo * oO0o . IIiIiII11i
def O0o00o000oO ( ) :
 if 62 - 62: Ii1I / Iii . ooOoO0O00
 if 99 - 99: OOooOOo . i1IiiiI1iI
 if 59 - 59: Iii / I1ii11iIi11i / oooOo0oo0oo / o0o00Oo0O / OOooOOo + I11i
 if 13 - 13: I11i % i1i1I1IIii1II / i1IiiiI1iI % i1IiiiI1iI % o0o00Oo0O
 if 90 - 90: III1iiIii . i1iIi / iI11I1II1I1I
 if 28 - 28: III1iiIii + i1i1I1IIii1II - i1iIi / iI11I1II1I1I - oOo0O0Ooo
 if 45 - 45: o0o00Oo0O / ooOoO0O00 * i1i1I1IIii1II * oO0o
 if 35 - 35: Ii1I / IiI1i11I % oOo0O0Ooo + iI11I1II1I1I
 if 79 - 79: OOooOOo / i1iIi
 if 77 - 77: I1ii11iIi11i
 if 46 - 46: i1IiiiI1iI
 iiIIIiIi1IIi ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 iiIIIiIi1IIi ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 iiIIIiIi1IIi ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 oOI1Ii1I1 ( 'tvshows' , 'INFO' )
 if 72 - 72: IiI1i11I * oooOo0oo0oo
def oooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , iiiIIIii in IIi :
  iiIIIiIi1IIi ( ( OOoO + ' - ' + iiiIIIii ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 93 - 93: iI11I1II1I1I + oOo0O0Ooo + Ii
def O0Oo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 99 - 99: Ii1I . oO0o * Iii % i1IiiiI1iI
def II1Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , url in IIi :
  iiIIIiIi1IIi ( OOoO , url , 90054 , iIiIi11 )
 for url in next :
  iiIIIiIi1IIi ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 6 - 6: ooOoO0O00 - IIiIiII11i * I11i . oO0o
def oooO00Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for iIiIi11 , iiiIIIii , url , OOoO , ooO00o in IIi :
  Iii1I1I11iiI1 ( iiiIIIii + ' - ' + OOoO + ' - ' + ooO00o , url , 90044 , iIiIi11 , iIiIi11 , '' )
 for iIiIi11 , OOoO , url in i1Iii1i1I :
  iiIIIiIi1IIi ( OOoO , url , 90044 , iIiIi11 , iIiIi11 , '' )
 for url in next :
  iiIIIiIi1IIi ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 73 - 73: IiI1i11I * IiI1i11I / i1iIi
def IIii1i11iI1II11 ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi11i = 'http://onlinemovies.tube/?s=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 O0ooOoO = iIi11i . lower ( )
 II11iIiIIIiI = OooOoooOo ( O0ooOoO )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO , I1ii in IIi :
  if 'season' in I1ii :
   iiIIIiIi1IIi ( OOoO , O0O00Oo , 90054 , iIiIi11 , iIiIi11 , '' )
  if 'episodes' in I1ii :
   iiIIIiIi1IIi ( OOoO , O0O00Oo , 90044 , iIiIi11 , iIiIi11 , '' )
 for O0O00Oo in next :
  iiIIIiIi1IIi ( 'NEXT' , O0O00Oo , 90053 , iiIi1IIiIi + 'Next.png' )
  if 56 - 56: Ii . i1iIi / IiI1i11I
def III1iii1i1II ( ) :
 if 87 - 87: oooOo0oo0oo + I11i . IiI1i11I - ii
 if 6 - 6: iI11I1II1I1I * ii
 if 28 - 28: I1ii11iIi11i * I11i / i1IiiiI1iI
 if 52 - 52: o0o00Oo0O / I11i % IiI1i11I * oOo0O0Ooo % oooOo0oo0oo
 if 69 - 69: Ii1I
 if 83 - 83: I11i
 if 38 - 38: i1IiiiI1iI + ii . ooOoO0O00
 if 19 - 19: IiI1i11I - I11i - o0ii1I - OOooOOo . IiI1i11I . i1IiiiI1iI
 if 48 - 48: IiI1i11I + III1iiIii
 if 60 - 60: Iii + IiI1i11I . III1iiIii / ooOoO0O00 . iI11I1II1I1I
 iiIIIiIi1IIi ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 iiIIIiIi1IIi ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 iiIIIiIi1IIi ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 iiIIIiIi1IIi ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 oOI1Ii1I1 ( 'tvshows' , 'INFO' )
 if 14 - 14: oooOo0oo0oo
def o0oo0Ooooo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , iiiIIIii in IIi :
  if 'genre' in url :
   iiIIIiIi1IIi ( ( OOoO + ' - ' + iiiIIIii ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 76 - 76: ooOoO0O00 * ii * o0o00Oo0O + i1IiiiI1iI * i1IiiiI1iI
def i1iIiIii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  if 'release' in url :
   iiIIIiIi1IIi ( OOoO , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 20 - 20: I11i * i1iIi
def i1III1iI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , ii1i , url , OOOiiiiI in IIi :
  Iii1I1I11iiI1 ( OOoO + ' ' + ii1i , url , 90044 , iIiIi11 , iIiIi11 , OOOiiiiI )
 for iIiIi11 , OOoO , I1ii , url , i1IiiiiIi1I , OOOiiiiI in i1Iii1i1I :
  if 'movies' in I1ii :
   Iii1I1I11iiI1 ( OOoO + ' - ' + i1IiiiiIi1I , url , 90044 , iIiIi11 , iIiIi11 , OOOiiiiI )
 for url in next :
  iiIIIiIi1IIi ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 56 - 56: ii * o0o00Oo0O
def oo0OoOOooO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  o0o0OO0o00o0O ( 'http:' + url )
  if 28 - 28: oO0o - i1i1I1IIii1II + OOooOOo + o0ii1I / iI11I1II1I1I
def o0o0OO0o00o0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  ii11i ( ( OOoO ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def iiiii11I1 ( ) :
 if 16 - 16: o0o00Oo0O . o0ii1I % ooOoO0O00 % oooOo0oo0oo
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
 if 50 - 50: IiI1i11I % IIiIiII11i - i1iIi . ooOoO0O00 + o0o00Oo0O % IiI1i11I
 if 10 - 10: IiI1i11I . ooOoO0O00 + o0ii1I
 if 66 - 66: oO0o % I11i
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi11i = 'http://onlinemovies.tube/?s=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 O0ooOoO = iIi11i . lower ( )
 II11iIiIIIiI = OooOoooOo ( O0ooOoO )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO , iI1ii11Ii in IIi :
  if 'movies' in iI1ii11Ii :
   iiIIIiIi1IIi ( iI1ii11Ii + '-' + OOoO , O0O00Oo , 90044 , iIiIi11 )
 for O0O00Oo in next :
  i1III1iI ( O0O00Oo )
  if 97 - 97: i1IiiiI1iI + i1i1I1IIii1II - oO0o % i1i1I1IIii1II - I11i
def II1iiiiII ( ) :
 iiIIIiIi1IIi ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , O0O00Oo , 80006 , iiIi1IIiIi + 'Desi.png' )
def i1iiiiI1IiIIii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOoO in IIi :
  ii11i ( OOoO , url , 80007 , iIiIi11 )
 for url , iIiIi11 , OOoO in IIi :
  iiIIIiIi1IIi ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def IIIIiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  OooO0OO ( url )
def Ii11Ii1iI ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi11i = 'http://www.join4films.com/?s=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' ) + '&search_type=1'
 O0ooOoO = iIi11i . lower ( )
 i1iiiiI1IiIIii ( O0ooOoO )
 if 87 - 87: I1ii11iIi11i + o0o00Oo0O - Iii * iI11I1II1I1I . i1IiiiI1iI % I11i
 if 83 - 83: IIiIiII11i * ooOoO0O00 * IiI1i11I . Ii1I / Iii + ooOoO0O00
 if 43 - 43: ii
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
 if 80 - 80: ii + III1iiIii
 if 95 - 95: i1IiiiI1iI / i1i1I1IIii1II * i1IiiiI1iI - ii * ii % oO0o
 if 43 - 43: I1ii11iIi11i . i1IiiiI1iI
 if 12 - 12: i1IiiiI1iI + oooOo0oo0oo + Iii . III1iiIii / o0ii1I
def i1I ( ) :
 Iii1I1I11iiI1 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 100 - 100: oO0o % oO0o
def iI1I1 ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi11i = 'http://imoviemax.se/?s=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 O0ooOoO = iIi11i . lower ( )
 ii1O0ooooo000 ( O0ooOoO )
def OooOoOO0OO ( url ) :
 I1iiIiiii1111 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , I1ii1i11i in IIi :
  if OOoO in I1iiIiiii1111 :
   pass
  else :
   Iii1I1I11iiI1 ( OOoO + ' - ' + I1ii1i11i + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   I1iiIiiii1111 . append ( OOoO )
   if 86 - 86: o0o00Oo0O % ooOoO0O00 . IIiIiII11i . Iii
def IiI1II11ii1ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO , oOO0OOOo000o in IIi :
  Iii1I1I11iiI1 ( OOoO + ' - Views:' + oOO0OOOo000o , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 69 - 69: Ii1I + IiI1i11I * o0o00Oo0O . oooOo0oo0oo % OOooOOo
  if 96 - 96: i1iIi . i1iIi - Iii / Iii
def ii1O0ooooo000 ( url ) :
 OoOo = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  Iii1I1I11iiI1 ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , url in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 10075 , iIiIi11 , iIiIi11 , '' )
  OoOo . append ( OOoO )
  if 6 - 6: i1iIi
def i11i ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for oo0OoOO0o0o , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  OO0OOO00 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + OO0OOO00
  ooOOo0o = ( oo0OoOO0o0o ) . replace ( 'play-' , 'Server ' )
  iI1Ii1iI11iiI ( ooOOo0o , OO0OOO00 , 10076 , img , img , '' )
  if 50 - 50: IIiIiII11i - i1IiiiI1iI + iI11I1II1I1I + iI11I1II1I1I
def OoooooOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for oo00ooOoo in IIi :
  if '=m' in oo00ooOoo :
   OooOo ( oo00ooOoo )
  elif 'php' in oo00ooOoo :
   OoooooOo ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( oo00ooOoo )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for iii1IIIiiiI in IIi :
    OooOo ( oo00ooOoo )
    if 67 - 67: I1ii11iIi11i / o0o00Oo0O
    if 88 - 88: OOooOOo - oooOo0oo0oo
    if 63 - 63: III1iiIii * ii
def I1iIiiiI1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 OOO0O00Oo = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0i1iI , ii1oOOO0ooOO in OOO0O00Oo :
  print 'there ><><><><><><><><><><><><'
  oO0i1iI = oO0i1iI
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( ii1oOOO0ooOO ) )
  for OOoO , i11IiI1iiI11 in IIi :
   print 'here <><><><><><><><><><><><>'
   Iii1I1I11iiI1 ( '[COLORred]' + oO0i1iI + '[/COLOR] - ' + OOoO + ' - [COLOR' + ooOoOoo0O + ']' + i11IiI1iiI11 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 iiIIiii = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO0i1iI , OOoOOOO00 in iiIIiii :
  print 'there ><><><><><><><><><><><><'
  oO0i1iI = oO0i1iI
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OOoOOOO00 ) )
  for OOoO , i11IiI1iiI11 in IIi :
   print 'here <><><><><><><><><><><><>'
   Iii1I1I11iiI1 ( '[COLORred]' + oO0i1iI + '[/COLOR] - ' + OOoO + ' - [COLOR' + ooOoOoo0O + ']' + i11IiI1iiI11 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + i1IiiiI1iI
   if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * i1i1I1IIii1II
   if 85 - 85: IIiIiII11i . i1iIi % oooOo0oo0oo % Iii
def OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIIiii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iiIIiii in iiIIiii :
  OOoO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iiIIiii ) )
  for OOoO in OOoO :
   OOoO = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iiIIiii ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  IiI11i1IIiiI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iiIIiii ) )
  for IiI11i1IIiiI in IiI11i1IIiiI :
   IiI11i1IIiiI = 'http:' + IiI11i1IIiiI
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiI11i1IIiiI , '' , '' )
  if 80 - 80: i1i1I1IIii1II * Iii / iI11I1II1I1I % i1i1I1IIii1II / iI11I1II1I1I
  if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * IiI1i11I . Ii * o0o00Oo0O
  if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + III1iiIii
  if 27 - 27: oooOo0oo0oo
def O0OoOO0oo0 ( url ) :
 if 52 - 52: i1IiiiI1iI % OOooOOo + iI11I1II1I1I * i1i1I1IIii1II . o0ii1I
 OoOooOO0oOOo0O = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oo00ooOoo , iIiIi11 , OOoO , I1II in IIi :
  OOoO = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( oo00ooOoo )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for Iiii1I1 , o0OO0oOo00Oo0o0Oo in i1Iii1i1I :
   iIIi1Ii1III = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( o0OO0oOo00Oo0o0Oo ) )
   for OOOiiiiI in iIIi1Ii1III :
    if OOoO in OoOooOO0oOOo0O :
     pass
    else :
     iI1Ii1iI11iiI ( OOoO , Iiii1I1 , 8043 , iIiIi11 , iIiIi11 , OOOiiiiI )
     oOI1Ii1I1 ( 'movies' , 'INFO' )
     OoOooOO0oOOo0O . append ( OOoO )
     if 86 - 86: Ii + Ii . i1IiiiI1iI % oOo0O0Ooo . i1iIi
     if 17 - 17: o0ii1I
def OoO0OOoO0Oo0 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , oo00O00oO000o , OOOiiiiI , oooOo0OOOoo0 , OOoO in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 10065 , oo00O00oO000o , oooOo0OOOoo0 , OOOiiiiI )
 oOI1Ii1I1 ( 'movies' , 'INFO' )
 if 91 - 91: IIiIiII11i
def OOoO0O000O ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi11i = 'https://www.youtube.com/results?search_query=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 O0ooOoO = iIi11i . lower ( )
 II11iIiIIIiI = OooOoooOo ( O0ooOoO )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo in next :
  O0O00Oo = 'https://www.youtube.com' + O0O00Oo
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , O0O00Oo , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for iIiIi11 , O0O00Oo , OOoO , iIO0o , o0OO0oOo00Oo0o0Oo in IIi :
  OOO00 . append ( OOoO )
  oOI1Ii1I1 ( 'tvshows' , 'INFO' )
  IiI11i1IIiiI = 'http:' + ( iIiIi11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IiI11i1IIiiI
  O0O00Oo = 'http://www.youtube.com' + O0O00Oo
  iI1Ii1iI11iiI ( '[COLORred]' + iIO0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiI11i1IIiiI , IiI11i1IIiiI , o0OO0oOo00Oo0o0Oo )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIiIi11 , O0O00Oo , OOoO , iIO0o in IIi :
   print 'im doing it'
   oOI1Ii1I1 ( 'tvshows' , 'INFO' )
   IiI11i1IIiiI = 'http:' + ( iIiIi11 ) . replace ( 'https:' , '' )
   O0O00Oo = 'http://www.youtube.com' + O0O00Oo
   if '&' in O0O00Oo :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( O0O00Oo )
    iiIIiii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for iiIIiii in iiIIiii :
     OOoO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iiIIiii ) )
     for OOoO in OOoO :
      OOoO = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     O0O00Oo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iiIIiii ) )
     for O0O00Oo in O0O00Oo :
      O0O00Oo = 'https://www.youtube.com/w' + O0O00Oo
     IiI11i1IIiiI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iiIIiii ) )
     for IiI11i1IIiiI in IiI11i1IIiiI :
      IiI11i1IIiiI = 'http:' + IiI11i1IIiiI
     iI1Ii1iI11iiI ( '[COLORred]' + iIO0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiI11i1IIiiI , Oo00OOOOO , '' )
   elif OOoO in OOO00 :
    pass
   elif 'user' in O0O00Oo or 'elete' in OOoO :
    pass
   elif 'hannel' in O0O00Oo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + O0O00Oo
    II11iIiIIIiI = OooOoooOo ( O0O00Oo )
    I1ii1Ii1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for iIiIi11 , O0O00Oo , OOoO in I1ii1Ii1 :
     if 'outube' in O0O00Oo or 'list' in O0O00Oo :
      pass
     elif 'atch' in O0O00Oo :
      O0O00Oo = ( O0O00Oo ) . replace ( '/watch?v=' , '' )
      iI1Ii1iI11iiI ( '[COLORred]' + iIO0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iIiIi11 , 'http:' + iIiIi11 , '' )
     else :
      pass
   else :
    iI1Ii1iI11iiI ( '[COLORred]' + iIO0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiI11i1IIiiI , IiI11i1IIiiI , '' )
    if 73 - 73: o0o00Oo0O . i1i1I1IIii1II + Ii + iI11I1II1I1I - Iii / OOooOOo
def OO0OOOOo0000O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for iIiIi11 , url , OOoO , iIO0o , o0OO0oOo00Oo0o0Oo in IIi :
  OOO00 . append ( OOoO )
  oOI1Ii1I1 ( 'tvshows' , 'INFO' )
  IiI11i1IIiiI = 'http:' + ( iIiIi11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IiI11i1IIiiI
  url = 'http://www.youtube.com' + url
  iI1Ii1iI11iiI ( '[COLORred]' + iIO0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiI11i1IIiiI , IiI11i1IIiiI , o0OO0oOo00Oo0o0Oo )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIiIi11 , url , OOoO , iIO0o in IIi :
   oOI1Ii1I1 ( 'tvshows' , 'INFO' )
   IiI11i1IIiiI = 'http:' + ( iIiIi11 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    iiIIiii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for iiIIiii in iiIIiii :
     OOoO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iiIIiii ) )
     for OOoO in OOoO :
      OOoO = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iiIIiii ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     IiI11i1IIiiI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iiIIiii ) )
     for IiI11i1IIiiI in IiI11i1IIiiI :
      IiI11i1IIiiI = 'http:' + IiI11i1IIiiI
     iI1Ii1iI11iiI ( '[COLORred]' + iIO0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiI11i1IIiiI , Oo00OOOOO , '' )
   elif OOoO in OOO00 :
    pass
   elif 'user' in url or 'elete' in OOoO :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    I1ii1Ii1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for iIiIi11 , url , OOoO in I1ii1Ii1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      iI1Ii1iI11iiI ( '[COLORred]' + iIO0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iIiIi11 , 'http:' + iIiIi11 , '' )
     else :
      pass
   else :
    iI1Ii1iI11iiI ( '[COLORred]' + iIO0o + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiI11i1IIiiI , IiI11i1IIiiI , '' )
    if 25 - 25: IiI1i11I - I1ii11iIi11i
    if 10 - 10: o0o00Oo0O % III1iiIii . oO0o + I11i + Ii1I
    if 52 - 52: OOooOOo / oO0o + i1IiiiI1iI
def Iii1i11iiI1 ( ) :
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
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
 II1iI111iiIIiI1I = xbmc . Keyboard ( '' , 'heading' , True )
 II1iI111iiIIiI1I . setHeading ( 'Enter Username' )
 II1iI111iiIIiI1I . setHiddenInput ( False )
 II1iI111iiIIiI1I . doModal ( )
 if ( II1iI111iiIIiI1I . isConfirmed ( ) ) :
  ooO00Oo = II1iI111iiIIiI1I . getText ( )
  return ooO00Oo
 else :
  return False
  if 41 - 41: Ii - ooOoO0O00 / I1ii11iIi11i * III1iiIii / i1IiiiI1iI - I1ii11iIi11i
  if 56 - 56: o0o00Oo0O
def I1Iii11I111I ( ) :
 II1iI111iiIIiI1I = xbmc . Keyboard ( '' , 'heading' , True )
 II1iI111iiIIiI1I . setHeading ( 'Enter Password' )
 II1iI111iiIIiI1I . setHiddenInput ( False )
 II1iI111iiIIiI1I . doModal ( )
 if ( II1iI111iiIIiI1I . isConfirmed ( ) ) :
  ooO00Oo = II1iI111iiIIiI1I . getText ( )
  return ooO00Oo
 else :
  return False
def iIIIII1iI ( ) :
 iII1IiiIIII = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  iIi1II11i = urllib2 . urlopen ( iII1IiiIIII )
  print iIi1II11i . getcode ( )
  iIi1II11i . close ( )
  if 8 - 8: ooOoO0O00
  pass
  if 20 - 20: IiI1i11I / oooOo0oo0oo
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def O0oo00oOOO0o ( ) :
 iii ( )
 if 28 - 28: i1iIi * Iii % Ii * IiI1i11I / o0ii1I
 if 41 - 41: oooOo0oo0oo - I11i + o0ii1I
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 15 - 15: Iii / I11i + o0ii1I
 if 76 - 76: o0ii1I + ii / oooOo0oo0oo % oO0o / Ii1I
 if 38 - 38: i1IiiiI1iI . IiI1i11I . oOo0O0Ooo * oO0o
 if 69 - 69: I11i % Ii / o0ii1I
def ooOOO00oOOooO ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 IiI = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 Iii1iiI = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 IIIiI1iiiiiIi = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 IIIiI1iiiiiIi = OooOoooOo ( IIIiI1iiiiiIi )
 if not IIIiI1iiiiiIi == "" :
  ii1IiiII = 'https://tinyurl.com/create.php?source=indexpage&url=' + IiI + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( ii1IiiII ) )
  IiiI1II1II1i = 'https://tinyurl.com/create.php?source=indexpage&url=' + Iii1iiI + '&submit=Make+TinyURL%21&alias='
  IiI = OooOoooOo ( ii1IiiII )
  Iii1iiI = OooOoooOo ( IiiI1II1II1i )
  xbmc . log ( str ( Iii1iiI ) )
  iIO0OO0o0O00oO = o00O ( IiI , '<div class="indent"><b>' , '</b>' )
  oO0o0oOo = o00O ( Iii1iiI , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % iIO0OO0o0O00oO , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % oO0o0oOo )
 else :
  return
def OoO0O0oo0o ( ) :
 iIIIII1iI ( )
 iIi11I11 ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , i1ioO + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( I11iiI )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  Iii1I1I11iiI1 ( ( '[COLORsteelblue]' + OOoO + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , O0O00Oo , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def i1iIii1i111 ( url ) :
 open = OooOoooOo ( OOooo000OooO + url )
 o0o0 = OoOoIiI1 ( open , '<channel>' , '</channel>' )
 for iiIiII in o0o0 :
  if '<playlist_url>' in open :
   OOoO = o00O ( iiIiII , '<title>' , '</title>' )
   oo00IiI1 = o00O ( iiIiII , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   Iii1I1I11iiI1 ( str ( base64 . b64decode ( OOoO ) ) . replace ( '?' , '' ) , oo00IiI1 , 3 , icon , oooOo0OOOoo0 , '' )
  else :
   OOoO = o00O ( iiIiII , '<title>' , '</title>' )
   OOoO = base64 . b64decode ( OOoO )
   IIiiiI1iI = o00O ( iiIiII , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = o00O ( iiIiII , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   OOOiiiiI = o00O ( iiIiII , '<description>' , '</description>' )
   OOOiiiiI = base64 . b64decode ( OOOiiiiI )
   O0O0 = o00O ( OOOiiiiI , 'PLOT:' , '\n' )
   O0oO0o0OOOOOO = o00O ( OOOiiiiI , 'CAST:' , '\n' )
   IiI1i11IiIiii = o00O ( OOOiiiiI , 'RATING:' , '\n' )
   I11iiI1I1 = o00O ( OOOiiiiI , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   I11iiI1I1 = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( I11iiI1I1 )
   o0i1Ii11II = o00O ( OOOiiiiI , 'DURATION_SECS:' , '\n' )
   i1iiiiI11ii = o00O ( OOOiiiiI , 'GENRE:' , '\n' )
   oooooOOo0o ( str ( OOoO ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , IIiiiI1iI , oooOo0OOOoo0 , O0O0 , str ( I11iiI1I1 ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( O0oO0o0OOOOOO ) . split ( ) , IiI1i11IiIiii , o0i1Ii11II , i1iiiiI11ii )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 98 - 98: oO0o / Iii - o0ii1I
OOOOo0oOOOOooOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
i1I111II = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
def III11I11ii ( ) :
 iII1IiiIIII = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  iIi1II11i = urllib2 . urlopen ( iII1IiiIIII )
  print iIi1II11i . getcode ( )
  iIi1II11i . close ( )
  if 82 - 82: oooOo0oo0oo % IIiIiII11i - oooOo0oo0oo + IIiIiII11i
  pass
  if 61 - 61: Ii * i1i1I1IIii1II % I1ii11iIi11i * i1IiiiI1iI - ii - oO0o
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 83 - 83: i1iIi / oooOo0oo0oo
 O0O00Oo = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 i11iI1 ( O0O00Oo , i1I111II + "uide.xml" )
 if 35 - 35: Iii
 IiII111i1i11 = open ( OOOOo0oOOOOooOo , 'r+' )
 input = open ( OOOOo0oOOOOooOo ) . read ( ) . decode ( 'UTF-8' )
 o00oo = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 IiII111i1i11 . write ( o00oo )
 IiII111i1i11 . truncate ( )
 IiII111i1i11 . close ( )
 O0oO0oo0O ( )
 if 82 - 82: ii . o0ii1I
def O0oO0oo0O ( ) :
 open = OooOoooOo ( III1ii )
 all = OoOoIiI1 ( open , '{"num' , 'direct' )
 for iiIiII in all :
  if '"tv_archive":1' in iiIiII :
   OOoO = o00O ( iiIiII , '"epg_channel_id":"' , '"' )
   IIiiiI1iI = o00O ( iiIiII , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = o00O ( iiIiII , 'stream_id":"' , '"' )
   OOoO = OOoO . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   Iii1I1I11iiI1 ( OOoO , 'url' , 90027 , IIiiiI1iI , oooOo0OOOoo0 , OOoO )
   if 38 - 38: Ii1I + OOooOOo
   if 68 - 68: o0o00Oo0O
def o0oOoO00 ( name , description ) :
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 oOO000 = open ( OOOOo0oOOOOooOo )
 OoOooO = ElementTree . parse ( oOO000 )
 OoO0o00OOOOO = "apples"
 import datetime as dt
 from datetime import time
 I1iIi1iIIIIiI = datetime . now ( ) - timedelta ( days = 5 )
 oO0i1iI = str ( I1iIi1iIIIIiI )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 O000oooOO0Oo0 = OoOooO . findall ( "programme" )
 for I1iIiIii in O000oooOO0Oo0 :
  if name in I1iIiIii . attrib . get ( 'channel' ) :
   OO0I1iiI1iiI1i1 = I1iIiIii . attrib . get ( 'start' )
   OOOO00OOO00 , ii1OO0 , OoOoO00OOoOOOo0 = OO0I1iiI1iiI1i1 . partition ( ' +' )
   oO0i1iI = str ( oO0i1iI ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   I11iiI1I1 , oOoO00O , iIi11I = OO0I1iiI1iiI1i1 . partition ( '2017' )
   I11I1I1i1i = I1iIiIii . find ( 'title' ) . text + OO0I1iiI1iiI1i1
   iIi11I = iIi11I [ : - 6 ]
   if OOOO00OOO00 > oO0i1iI :
    if OOOO00OOO00 < I1IIIii :
     Oo0oOO0O00 = OOOO00OOO00
     Oo0oOO0O00 = Oo0oOO0O00 [ : 4 ] + '/' + Oo0oOO0O00 [ 4 : ]
     OOOO00OOO00 = OOOO00OOO00 [ : 4 ] + '-' + OOOO00OOO00 [ 4 : ]
     Oo0oOO0O00 = Oo0oOO0O00 [ : 7 ] + '/' + Oo0oOO0O00 [ 7 : ]
     OOOO00OOO00 = OOOO00OOO00 [ : 7 ] + '-' + OOOO00OOO00 [ 7 : ]
     Oo0oOO0O00 = Oo0oOO0O00 [ : 10 ] + ' - ' + Oo0oOO0O00 [ 10 : ]
     OOOO00OOO00 = OOOO00OOO00 [ : 10 ] + ':' + OOOO00OOO00 [ 10 : ]
     Oo0oOO0O00 = Oo0oOO0O00 [ : 15 ] + ':' + Oo0oOO0O00 [ 15 : ]
     OOOO00OOO00 = OOOO00OOO00 [ : 13 ] + '-' + OOOO00OOO00 [ 13 : ]
     Oo0oOO0O00 = Oo0oOO0O00 [ : - 2 ]
     OOOO00OOO00 = OOOO00OOO00 [ : - 2 ]
     o00OOo0o0O = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&stream=%s&start=" ) % ( OO0o , Ooo , description )
     OoO0o00OOOOO = o00OOo0o0O + str ( OOOO00OOO00 ) + "&duration=240"
     Oo0oOO0O00 = '[COLOR blue]%s - [/COLOR]' % Oo0oOO0O00
     I11I1I1i1i = str ( Oo0oOO0O00 ) + I1iIiIii . find ( 'title' ) . text
     OOOiiiiI = I1iIiIii . find ( 'desc' ) . text
     iI1Ii1iI11iiI ( I11I1I1i1i , OoO0o00OOOOO , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , OOOiiiiI )
     if 14 - 14: IiI1i11I - Iii * ii + oooOo0oo0oo . IIiIiII11i
def i11iI1 ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 i1i1I11i1I = time . time ( )
 urllib . urlretrieve ( url , dest , lambda O0oII1IIiiI1 , O00O00 , oOooO0OoO : o0oOOOOoo0 ( O0oII1IIiiI1 , O00O00 , oOooO0OoO , o0oOoO00o , i1i1I11i1I ) )
def o0oOOOOoo0 ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  ooOO0OOO00o = min ( numblocks * blocksize * 100 / filesize , 100 )
  OoOoO0ooooO0 = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  IIII1ii1 = numblocks * blocksize / ( time . time ( ) - start_time )
  if IIII1ii1 > 0 :
   OOO0O0OOo = ( filesize - numblocks * blocksize ) / IIII1ii1
  else :
   OOO0O0OOo = 0
  IIII1ii1 = IIII1ii1 / 1024
  Iii1 = IIII1ii1 / 1024
  OOoOi1IiiI = float ( filesize ) / ( 1024 * 1024 )
  O0OOO0 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( OoOoO0ooooO0 )
  II1iI1I11I = '[COLOR white]Speed:  %.02f Mb/s ' % Iii1 + '[/COLOR]'
  dp . update ( ooOO0OOO00o , O0OOO0 , II1iI1I11I )
 except :
  ooOO0OOO00o = 100
  dp . update ( ooOO0OOO00o )
 if dp . iscanceled ( ) :
  o0OIi = xbmcgui . Dialog ( )
  o0OIi . ok ( "GenieTv" , 'The download was cancelled.' )
  if 11 - 11: i1i1I1IIii1II . oOo0O0Ooo + III1iiIii / ooOoO0O00
  sys . exit ( )
  dp . close ( )
  if 1 - 1: I1ii11iIi11i * i1IiiiI1iI . ii
def oOO00OO0o0O ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  III1IiiIiiI1i ( )
  if 73 - 73: ooOoO0O00 % Iii - i1iIi / I11i % oO0o / i1IiiiI1iI
  if 89 - 89: III1iiIii / oO0o * o0o00Oo0O / Iii . i1IiiiI1iI
  if 17 - 17: Iii
  if 56 - 56: i1iIi * I11i + Iii
  if 48 - 48: III1iiIii * oO0o % i1IiiiI1iI - Iii
  if 72 - 72: ooOoO0O00 % i1iIi % III1iiIii % i1i1I1IIii1II - i1i1I1IIii1II
  if 97 - 97: I11i * o0o00Oo0O / I11i * oO0o * I1ii11iIi11i
  if 38 - 38: i1IiiiI1iI
def III1IiiIiiI1i ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for O0O00Oo in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def Iiiii1Iii1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 oOOOOoO = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OOoO0ooOO = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IiIi1I1 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 I1i11 = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 iii1IIII1iii11I = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 I1I1IiIi1 = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 i1II11II1 = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 IIiI = IiIIIiI ( )
 II1iI1iiiI = OoOoO00o00 ( )
 for url in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  ii11i ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in oOOOOoO :
  ii11i ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OOoO0ooOO :
  ii11i ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1i11 :
  dt = datetime . fromtimestamp ( float ( I1i11 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  ii11i ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   ii11i ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  ii11i ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IiIi1I1 :
  ii11i ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in iii1IIII1iii11I :
  ii11i ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1I1IiIi1 :
  ii11i ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1II11II1 :
  ii11i ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + IIiI , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + II1iI1iiiI , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 51 - 51: I1ii11iIi11i * iI11I1II1I1I . ii . o0ii1I - oooOo0oo0oo / oOo0O0Ooo
 ii11i ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 98 - 98: IIiIiII11i + o0ii1I + ii / ooOoO0O00 - o0ii1I
def O0o0 ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 Oo0OOooo ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 100 - 100: i1i1I1IIii1II + o0o00Oo0O . oOo0O0Ooo + ooOoO0O00 - OOooOOo + I11i
def ooOOo ( data ) :
 i1iii1IiiiI1i1 = len ( data ) % 4
 if 37 - 37: I1ii11iIi11i - ooOoO0O00 - III1iiIii + Iii . iI11I1II1I1I
 if 59 - 59: ii - i1IiiiI1iI % I11i . Iii + ooOoO0O00 * Iii
 if 5 - 5: IIiIiII11i - III1iiIii
 if 86 - 86: III1iiIii * Iii + o0o00Oo0O * i1IiiiI1iI + Ii - Ii1I
 if 70 - 70: Ii
 if 57 - 57: Iii % oooOo0oo0oo + i1iIi * o0ii1I . I1ii11iIi11i
 if i1iii1IiiiI1i1 != 0 :
  data += b'=' * ( 4 - i1iii1IiiiI1i1 )
 return base64 . decodestring ( data )
def o00O ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : oooo0 = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : oooo0 = ''
 else :
  try : oooo0 = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : oooo0 = ''
 return oooo0
 if 88 - 88: Iii + oOo0O0Ooo - Iii / ii - Ii
 if 24 - 24: iI11I1II1I1I
def OoOoIiI1 ( text , start_with , end_with ) :
 oooo0 = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return oooo0
def IiIIIiI ( ) :
 O0Oo0oOOo0O = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 O0Oo0oOOo0O . connect ( ( '8.8.8.8' , 0 ) )
 O0Oo0oOOo0O = O0Oo0oOOo0O . getsockname ( ) [ 0 ]
 return O0Oo0oOOo0O
 if 73 - 73: oOo0O0Ooo - IiI1i11I . IiI1i11I
def OoOoO00o00 ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 IIiI = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( IIiI . group ( ) )
i1ioO = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
III1ii = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
I1I1 = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
O0OOO0ooO00o = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
I1iii1 = '&action=get_live_categories'
iIiiiIIiii = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
I11iiI = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 91 - 91: I11i . IiI1i11I % I1ii11iIi11i - IiI1i11I . i1i1I1IIii1II % Ii
OOooo000OooO = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
iIiO0O = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
oOOoooo = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
O0oIi1iIiIi1I11 = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 12 - 12: iI11I1II1I1I . i1iIi
def I11OOO0 ( ) :
 iIIIII1iI ( )
 open = OooOoooOo ( oOOoooo )
 o0o0 = OoOoIiI1 ( open , '<channel>' , '</channel>' )
 for iiIiII in o0o0 :
  OOoO = o00O ( iiIiII , '<title>' , '</title>' )
  OOoO = base64 . b64decode ( OOoO )
  oo00IiI1 = o00O ( iiIiII , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  Iii1I1I11iiI1 ( '[COLORsteelblue]' + OOoO + '[/COLOR]' , oo00IiI1 , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 16 - 16: IiI1i11I / iI11I1II1I1I + oooOo0oo0oo * IiI1i11I * Iii
def iiIiI11IiI1ii ( url ) :
 open = OooOoooOo ( O0oIi1iIiIi1I11 + url )
 o0o0 = OoOoIiI1 ( open , '<channel>' , '</channel>' )
 for iiIiII in o0o0 :
  OOoO = o00O ( iiIiII , '<title>' , '</title>' )
  OOoO = base64 . b64decode ( OOoO )
  xbmc . log ( str ( OOoO ) )
  IIiiiI1iI = o00O ( iiIiII , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  oo00IiI1 = o00O ( iiIiII , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  OOOiiiiI = o00O ( iiIiII , '<description>' , '</description>' )
  OOOiiiiI = base64 . b64decode ( OOOiiiiI )
  ooO0O0 = '('
  IiIIII1II = ')'
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , oo00IiI1 , 222 , IIiiiI1iI , oooOo0OOOoo0 , ( '[COLOR' + ooOoOoo0O + ']' + OOOiiiiI + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( IiIIII1II , '[COLORsteelblue]' ) . replace ( ooO0O0 , '[COLORorangered]' ) )
  if 43 - 43: Iii % ooOoO0O00 % i1iIi . Ii
def OoO000oo000o0 ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( iIiiiIIiii + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , type , oo00ooOoo , oo0OoOooo in IIi :
  iii1IIIiiiI = ( O0OOO0ooO00o + oo00ooOoo + '.m3u8' ) . strip ( )
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , iii1IIIiiiI , 222 , ( oo0OoOooo ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
def i1Ii1I1Ii11iI ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oOo00o00oO , i1ii111i in IIi :
  if name == oOo00o00oO :
   iI1Ii1iI11iiI ( ( '' + name + '' ) . replace ( '_' , ' ' ) + i1ii111i , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   iI1Ii1iI11iiI ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def i1ii1i1Ii11 ( name ) :
 O0O0Oo0O0oo = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , iIiIi11 , O0O00Oo in IIi :
  O0O00Oo = ( O0O00Oo ) . replace ( '.ts' , '.m3u8' )
  iI1Ii1iI11iiI ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( O0O00Oo ) . strip ( ) , 222 , iIiIi11 , iIiIi11 , '' )
 else :
  iI1Ii1iI11iiI ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 62 - 62: Iii / Ii1I
  if 85 - 85: oOo0O0Ooo + IiI1i11I - IiI1i11I . ii - iI11I1II1I1I
  if 8 - 8: Ii * I11i / Ii1I . o0ii1I
  if 31 - 31: Ii - i1iIi / Ii1I - o0ii1I
  if 5 - 5: Ii * I1ii11iIi11i
  if 29 - 29: o0ii1I / i1iIi % Iii
  if 10 - 10: iI11I1II1I1I % ii % Ii1I
  if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * Iii
  if 89 - 89: o0ii1I - i1iIi . Iii - i1IiiiI1iI - oOo0O0Ooo
  if 79 - 79: III1iiIii + III1iiIii + o0ii1I
  if 39 - 39: o0o00Oo0O - ii
  if 63 - 63: iI11I1II1I1I % I11i * i1iIi
def iiIiii1iI1i ( ) :
 Iii1I1I11iiI1 ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  Iii1I1I11iiI1 ( 'Backup Genie Favourites' , O0O00Oo , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  Iii1I1I11iiI1 ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  Iii1I1I11iiI1 ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 79 - 79: o0o00Oo0O
  if 32 - 32: IIiIiII11i . o0o00Oo0O + o0ii1I / OOooOOo / III1iiIii / oooOo0oo0oo
  if 15 - 15: Ii1I
zip = oo00 . getSetting ( 'zip' )
I11iI1 = xbmc . translatePath ( os . path . join ( zip ) )
def oOo00OO0o0 ( ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 1 - 1: ii / o0o00Oo0O + OOooOOo + OOooOOo . i1IiiiI1iI - OOooOOo
  if 9 - 9: i1IiiiI1iI * ii % oOo0O0Ooo / OOooOOo * Iii
  if 48 - 48: ii . OOooOOo
def oOIIIi11 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  oOo00OO0o0 ( )
  oooOo00O0 = open ( url ) . read ( )
  I1I = os . path . join ( I11iI1 , description . split ( 'Your ' ) [ 1 ] )
  IiII111i1i11 = open ( I1I , mode = 'w' )
  IiII111i1i11 . write ( oooOo00O0 )
  IiII111i1i11 . close ( )
 else :
  if 'guisettings.xml' in description :
   iiIiII = open ( os . path . join ( I11iI1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oooo0 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( oooo0 ) . findall ( iiIiII )
   for type , oOO0o0 , Ii1Ii1 in IIi :
    Ii1Ii1 = Ii1Ii1 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , oOO0o0 , Ii1Ii1 ) )
  else :
   I1I = os . path . join ( url )
   oooOo00O0 = open ( os . path . join ( I11iI1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiII111i1i11 = open ( I1I , mode = 'w' )
   IiII111i1i11 . write ( oooOo00O0 )
   IiII111i1i11 . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 62 - 62: i1IiiiI1iI * Iii
 if 74 - 74: OOooOOo . iI11I1II1I1I
 if 87 - 87: i1iIi
 if 41 - 41: OOooOOo . iI11I1II1I1I % i1iIi + o0o00Oo0O
def IIiII11 ( ) :
 oo0O00OOOOO = 1
 oOo00OO0o0 ( )
 OoOII11IiI1 = xbmc . translatePath ( os . path . join ( I11iI1 , 'Build Backup' , 'Full Backup' , '' ) )
 OoOOOO00oOO = xbmc . translatePath ( os . path . join ( I11iI1 , 'Build Backup' , 'my_full_backup.zip' ) )
 iiIIiIi = xbmc . translatePath ( os . path . join ( I11iI1 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( OoOII11IiI1 ) :
  os . makedirs ( OoOII11IiI1 )
 O000oO = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not O000oO ) : return False , 0
 ii11Ii1IiiI1 = O000oO
 O00o0o = xbmc . translatePath ( os . path . join ( OoOII11IiI1 , ii11Ii1IiiI1 + '.zip' ) )
 OOoO0o0OOo0 = [ 'plugin.video.GenieTv' ]
 O0OoO0ooOOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 IiI1iIIIi1iIi = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OOo0OOOoOOo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 III = "Creating full backup of existing build"
 ooo0o0O = "Creating Community Build"
 IiiiIIi11II = "Archiving..."
 o0oooOo0oo = ""
 i1iI1IIi1I = "Please Wait"
 oo00i1i11I1I1 ( oOo0oooo00o , O00o0o , ooo0o0O , IiiiIIi11II , o0oooOo0oo , i1iI1IIi1I , IiI1iIIIi1iIi , OOo0OOOoOOo )
 time . sleep ( 1 )
 OOOOOoooO = xbmc . translatePath ( os . path . join ( OoOII11IiI1 , ii11Ii1IiiI1 + '_guisettings.zip' ) )
 oO0Oooo0OoO = zipfile . ZipFile ( OOOOOoooO , mode = 'w' )
 try :
  oO0Oooo0OoO . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oO0Oooo0OoO . close ( )
 if oo0O00OOOOO == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + OoOOOO00oOO , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + O00o0o + '[/COLOR]' )
  if 38 - 38: oOo0O0Ooo . oOo0O0Ooo . o0ii1I + Ii1I * I1ii11iIi11i
def oo00i1i11I1I1 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
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
  OOOii [ : ] = [ IiII111i1i11 for IiII111i1i11 in OOOii if IiII111i1i11 not in exclude_files ]
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
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 6 - 6: i1i1I1IIii1II . Iii
 if 43 - 43: Ii1I + I11i
def iI1iiiiiii ( ) :
 iii ( )
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  I1IiiI1ii1i ( )
 if o0Oo00 == 1 :
  O0OoO0ooOO0o ( )
 if o0Oo00 == 2 :
  oO00OoOO ( )
 if o0Oo00 == 3 :
  OOoO0O000O ( )
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
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OOo00OoO ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if o0Oo00 == 1 :
   OOo00OoO ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if o0Oo00 == 2 :
   oOo0OOoo0o ( )
  if o0Oo00 == 3 :
   iiiIIiiIi ( )
  if o0Oo00 == 4 :
   Oooo0oOooOO ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if o0Oo00 == 5 :
   O0ooooO ( )
  if o0Oo00 == 6 :
   o0ooOooO ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if o0Oo00 == 7 :
   O0OoOo ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if o0Oo00 == 8 :
   OOOOoO0 ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if o0Oo00 == 9 :
   IiiIiIIi1 ( )
  if o0Oo00 == 10 :
   i1oo ( )
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
  if 83 - 83: o0o00Oo0O + OOooOOo / o0o00Oo0O / Iii
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 68 - 68: ooOoO0O00 . Iii . ooOoO0O00 + III1iiIii % oOo0O0Ooo
def IIoO ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   iI1I ( )
  if o0Oo00 == 1 :
   o0OO0 ( )
  if o0Oo00 == 2 :
   Iii1I1111ii ( )
  if o0Oo00 == 3 :
   i111I1 ( O0O00Oo )
  if o0Oo00 == 4 :
   OOOo0Oo0O ( O0O00Oo )
  if o0Oo00 == 5 :
   ii1iii1i ( )
  if o0Oo00 == 6 :
   i1I1I1iIIi ( url = 'http://www.iplocation.net/' , inc = 1 )
  if o0Oo00 == 7 :
   IiOo00O0o0O ( )
 else :
  iI1Ii1iI11iiI ( 'CLLEANUP' , 'url' , 9666 , iiIi1IIiIi + 'MAIN5.png' , Oo00OOOOO , '' )
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '' , 80000 , iiIi1IIiIi + 'KillKodi.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '' , 50004 , iiIi1IIiIi + 'Speedtest.png' , Oo00OOOOO , '' )
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , iiIi1IIiIi + 'View-Log-File.png' , Oo00OOOOO , '' )
  iI1Ii1iI11iiI ( 'DELETE CACHE' , 'url' , 14 , iiIi1IIiIi + 'DeleteCache.png' , Oo00OOOOO , '' )
  iI1Ii1iI11iiI ( 'DELETE PACKAGES' , 'url' , 6 , iiIi1IIiIi + 'DeletePackages.png' , Oo00OOOOO , '' )
  iI1Ii1iI11iiI ( 'FORCE REFRESH' , 'url' , 10 , iiIi1IIiIi + 'ForceRefresh.png' , Oo00OOOOO , 'Force Refresh All Repos' )
  Iii1I1I11iiI1 ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , iiIi1IIiIi + '1.jpg' , Oo00OOOOO , 'Fix Corrupt Database' )
  iI1Ii1iI11iiI ( 'CHECK MY IP' , 'url' , 12 , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
  iI1Ii1iI11iiI ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , iiIi1IIiIi + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , Oo00OOOOO , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 86 - 86: Iii + o0o00Oo0O + I1ii11iIi11i - Iii
  if 34 - 34: IIiIiII11i % oOo0O0Ooo % i1IiiiI1iI + I1ii11iIi11i - OOooOOo
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 66 - 66: o0ii1I * iI11I1II1I1I - i1iIi / oOo0O0Ooo
 if 62 - 62: III1iiIii . o0o00Oo0O . iI11I1II1I1I
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
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 94 - 94: i1iIi % Iii % ooOoO0O00
 if 90 - 90: o0ii1I * oO0o
def I1iO0o0O0OooOoo ( ) :
 iii ( )
 iI1Ii1iI11iiI ( 'CHECK ADVANCED XML' , str ( oO0000OOo00 ) , 8 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'MUCKYS XML' , str ( oO0000OOo00 ) + '/wizard/muckys.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( '0CACHE XML' , str ( oO0000OOo00 ) + '/wizard/0cache.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'MIKEY1234 XML' , str ( oO0000OOo00 ) + '/wizard/mikey.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'TUXENS XML' , str ( oO0000OOo00 ) + '/wizard/tuxens.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'P2P RECOMMENDED XML1' , str ( oO0000OOo00 ) + '/wizard/p2p1.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'P2P RECOMMENDED XML2' , str ( oO0000OOo00 ) + '/wizard/p2p2.xml' , 7 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'DELETE XML' , str ( oO0000OOo00 ) , 11 , iiIi1IIiIi + 'XML.png' , Oo00OOOOO , '' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 17 - 17: ii % i1i1I1IIii1II - ooOoO0O00 % III1iiIii % I1ii11iIi11i
def I1ii1ii11i1I ( ) :
 iii ( )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 41 - 41: ii . i1IiiiI1iI % OOooOOo - IiI1i11I
def oOOooO ( ) :
 iii ( )
 iI1Ii1iI11iiI ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 38 - 38: o0o00Oo0O
 if 79 - 79: ooOoO0O00 . i1i1I1IIii1II
 if 34 - 34: i1IiiiI1iI * IIiIiII11i
def o0oO00OOo0oO ( ) :
 iii ( )
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  oOiiI11I1ii11 ( )
 if o0Oo00 == 0 :
  O0OoO0oooOO ( O0O00Oo )
 if o0Oo00 == 0 :
  i1ii11I111Ii ( O0O00Oo )
  if 77 - 77: oO0o + oO0o . i1iIi * ii + oO0o
  if 6 - 6: ooOoO0O00 - Iii
  if 89 - 89: i1iIi - Iii . o0o00Oo0O % ii . Ii
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 35 - 35: IIiIiII11i / OOooOOo - o0o00Oo0O . IIiIiII11i
def oO0o000oOO ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for iIiIi11 , OOoO in IIi :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , iIiIi11 , iIiIi11 , '' )
 oOI1Ii1I1 ( 'tvshows' , 'INFO' )
 if 27 - 27: o0o00Oo0O - Iii * IIiIiII11i - iI11I1II1I1I / i1iIi
def II1iOOoOooO0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( I1IiiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 5 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 6 - 6: oOo0O0Ooo - Ii
def oOiiI11I1ii11 ( ) :
 iii ( )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 61 - 61: i1IiiiI1iI * Ii1I % oOo0O0Ooo % oO0o % Iii + Iii
def i1111I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OoO00oo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 96 - 96: ooOoO0O00
def oOOO00 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + ooooOOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 49 - 49: o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . IIiIiII11i % III1iiIii
def IIii1Ii1i1ii1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOOoOOooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 42 - 42: iI11I1II1I1I * o0ii1I / oO0o + oooOo0oo0oo
def Iii11iI1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 79 - 79: oOo0O0Ooo - IiI1i11I / Iii . I1ii11iIi11i
def O0OoO0oooOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o0III11IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 40 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 53 - 53: IiI1i11I / ooOoO0O00 / ooOoO0O00
def o0oo00O ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IIIIII1iI1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 5 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 14 - 14: oOo0O0Ooo / o0o00Oo0O
def iI ( ) :
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  II111iii ( )
 if o0Oo00 == 1 :
  OooO00o000 ( )
 if o0Oo00 == 2 :
  i1i11II1 ( )
  if 5 - 5: oO0o + oO0o + IIiIiII11i * iI11I1II1I1I + ii
  if 77 - 77: o0o00Oo0O * Ii1I * i1i1I1IIii1II + oO0o + Ii1I - i1IiiiI1iI
  if 10 - 10: Ii1I + III1iiIii
  if 58 - 58: oOo0O0Ooo + ii / IiI1i11I . i1iIi % I11i / Ii1I
def OooO00o000 ( ) :
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , oooO0I11Iii11i11I1 in IIi :
  iiIIIiIi1IIi ( 'Android Apps' + oooO0I11Iii11i11I1 , 'https://www.apkfiles.com' + O0O00Oo , 30035 , iiIi1IIiIi + 'apps.png' )
 for O0O00Oo , oooO0I11Iii11i11I1 in i1Iii1i1I :
  iiIIIiIi1IIi ( 'Android Games' + oooO0I11Iii11i11I1 , 'https://www.apkfiles.com' + O0O00Oo , 30035 , iiIi1IIiIi + 'GAMES.png' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
def IiOO0oo00OOo ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '/cat' in url :
   iiIIIiIi1IIi ( ( OOoO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def OoOo00oOoO ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '/app' in url :
   iiIIIiIi1IIi ( ( OOoO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def Oo0O00o0O0 ( url ) :
 I11iiii = OooOoooOo ( url )
 oo00IiI1 = url
 if "page=" in str ( url ) :
  oo00IiI1 = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  if 'apk' in url :
   iI1Ii1iI11iiI ( ( OOoO ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + iIiIi11 )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 iI1Ii1iI11iiI ( 'Next Page' , oo00IiI1 + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def IiIii11ii111 ( name , url ) :
 I11iiii = O00Oo0o000oO ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( I11iiii )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  oOiiIIIII ( name , url , 'Brackets' )
def i1i11II1 ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi11i = 'https://www.apkfiles.com/search?q=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' ) + '&search_type=1'
 O0ooOoO = iIi11i . lower ( )
 Oo0O00o0O0 ( O0ooOoO )
 if 19 - 19: IIiIiII11i / OOooOOo
def oOoo00 ( url ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( IIiIi , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , OOoO + '.apk' )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( url , ooI1111i , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 12 - 12: o0ii1I % IiI1i11I + oO0o + IIiIiII11i / I11i
def O0iII1i1 ( url ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , OOoO + '.mp4' )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( url , ooI1111i , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 34 - 34: oO0o / ii - i1i1I1IIii1II / i1i1I1IIii1II * oOo0O0Ooo
 if 61 - 61: Iii
def o00OOOOooO ( name , url , description ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , name )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( url , ooI1111i , o0oOoO00o )
 o0oo00oo0oO = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o0oo00oo0oO
 print '======================================='
 extract . all ( ooI1111i , o0oo00oo0oO , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 49 - 49: oOo0O0Ooo
 if 24 - 24: IIiIiII11i / o0ii1I . iI11I1II1I1I - IIiIiII11i % o0o00Oo0O
 if 8 - 8: oO0o % IiI1i11I . ii - o0ii1I % ii
 if 61 - 61: I11i / Ii
 if 28 - 28: oooOo0oo0oo / OOooOOo
def II111iii ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for OOoO , O0O00Oo , oo0OoOooo , oooOo0OOOoo0 , iII1IiiIIIIii in IIi :
  iI1Ii1iI11iiI ( OOoO , O0O00Oo , 80003 , oo0OoOooo , iiIi1IIiIi + 'APKToolsB.png' , iII1IiiIIIIii )
def oOOOIii1IiiII1Ii1 ( apk , ret = None ) :
 if apk == "kodi" :
  iiiIIi = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( iiiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   OOoOo0O00oo = IIi [ 0 ] [ 0 ]
   ii11Ii1IiiI1 = IIi [ 0 ] [ 1 ]
   oo0oO0oOo0O = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( OOoOo0O00oo , ii11Ii1IiiI1 )
  if ret == 'version' : return OOoOo0O00oo
  else : return oo0oO0oOo0O
 elif apk == "spmc" :
  OoOo00 = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( OoOo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  OOoOo0O00oo = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  oo0oO0oOo0O = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( OOoOo0O00oo , OOoOo0O00oo )
  if ret == 'version' : return OOoOo0O00oo
  else : return oo0oO0oOo0O
def oOiiIIIII ( name , url , Brackets ) :
 if OO0OO0O00oO0 ( ) == 'android' :
  OOoOoO = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not OOoOoO : OO000 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  o0oOoo0o = name
  if OOoOoO :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not OOooo0O0o0 ( url ) == True : OO000 ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % o0oOoo0o , '' , 'Please Wait' )
   ooI1111i = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( ooI1111i )
   except : pass
   downloader . download ( url , ooI1111i , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    oO0Oooo0OoO = zipfile . ZipFile ( ooI1111i )
    for file in oO0Oooo0OoO . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as IiII111i1i11 :
       IiiIiIIi = file . split ( '/' ) [ 1 ]
       IiII111i1i11 . write ( oO0Oooo0OoO . read ( file ) )
       xbmc . sleep ( 500 )
       IiII111i1i11 . close ( )
       try :
        os . remove ( ooI1111i )
       except :
        pass
       ooI1111i = os . path . join ( i1iIIi1 , IiiIiIIi )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ooI1111i + '")' )
  else : OO000 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : OO000 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 63 - 63: IiI1i11I / Ii1I * i1i1I1IIii1II / IIiIiII11i + oooOo0oo0oo - o0o00Oo0O
 if 16 - 16: IIiIiII11i / o0ii1I . o0ii1I - o0ii1I / Ii1I
 if 28 - 28: oooOo0oo0oo * ii + i1iIi % IiI1i11I . iI11I1II1I1I
 if 17 - 17: III1iiIii / I11i . oooOo0oo0oo + I11i / Ii1I . I1ii11iIi11i
def iII11 ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for O0O00Oo , OOoO in IIi :
  O0O00Oo = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + O0O00Oo )
  O00OO00OOOoO ( ( OOoO ) . replace ( '_' , ' ' ) , O0O00Oo )
  if 47 - 47: ooOoO0O00 % i1iIi - I1ii11iIi11i * Iii / Ii
def O00OO00OOOoO ( name , url ) :
 if OO0OO0O00oO0 ( ) == 'android' :
  OOoOoO = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not OOoOoO : OO000 ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  o0oOoo0o = name
  if OOoOoO :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not OOooo0O0o0 ( url ) == True : OO000 ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % o0oOoo0o , '' , 'Please Wait' )
   ooI1111i = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( ooI1111i )
   except : pass
   downloader . download ( url , ooI1111i , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ooI1111i + '")' )
  else : OO000 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : OO000 ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . i1IiiiI1iI / i1i1I1IIii1II
 if 4 - 4: Ii + oooOo0oo0oo
def I1111III111ii ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 5 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'INFO' )
 if 90 - 90: Iii
 if 88 - 88: oO0o
def oOoO00o ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC8=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 30015 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 85 - 85: i1i1I1IIii1II
def i1iIi11i ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 OO0OOO00 = url
 iIiIi11 = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for oo00ooOoo , OOoO in IIi :
  if '.mp4' in OOoO :
   iI1Ii1iI11iiI ( 'Watch VIDEO' , url + '/' + oo00ooOoo , 222 , iIiIi11 , fanart , '' )
  if 'description' in OOoO :
   iI1Ii1iI11iiI ( 'Read Description' , url + '/' + oo00ooOoo , 30017 , iIiIi11 , fanart , '' )
  if 'images' in OOoO :
   Iii1I1I11iiI1 ( 'View Images' , url + '/' + oo00ooOoo , 30018 , iIiIi11 , fanart , '' )
  if 'url' in OOoO :
   iI1Ii1iI11iiI ( 'Install Build On Android' , url + '/' + oo00ooOoo , 30016 , iIiIi11 , fanart , '' )
  if 'url' in OOoO :
   iI1Ii1iI11iiI ( 'Install Build On Pc' , url + '/' + oo00ooOoo , 30019 , iIiIi11 , fanart , '' )
 oOI1Ii1I1 ( 'movies' , 'INFO' )
 if 71 - 71: i1IiiiI1iI - i1IiiiI1iI - IiI1i11I + o0o00Oo0O % I11i % Iii
def iiIi1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  oOOO0 ( url )
  if 57 - 57: o0o00Oo0O . ii % Ii1I
def OoOo0o0O0o0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  iiiiii1ii1 ( url )
  if 27 - 27: oOo0O0Ooo - oO0o - i1i1I1IIii1II
def oOOo0O00o0O0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for ooO00Oo in IIi :
  oooO ( 'Description:' , ooO00Oo )
  if 80 - 80: o0ii1I
def iioOO ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for oo00ooOoo , OOoO in IIi :
  if 'png' in OOoO :
   iI1Ii1iI11iiI ( 'image' , '' , '' , url + '/' + oo00ooOoo , url + '/' + oo00ooOoo , '' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 38 - 38: Iii . III1iiIii - oO0o . oOo0O0Ooo
def ooOoo0OOOO0o ( name , url , description ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , name + '.zip' )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( url , ooI1111i , o0oOoO00o )
 iIIii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIIii
 print '======================================='
 extract . all ( ooI1111i , iIIii , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 ii1iii1i ( )
 if 38 - 38: oOo0O0Ooo % III1iiIii * o0ii1I
 if 91 - 91: o0ii1I + oO0o * I11i . i1IiiiI1iI
def iiiiii1ii1 ( url ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( url , ooI1111i , o0oOoO00o )
 iIIii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIIii
 print '======================================='
 extract . all ( ooI1111i , iIIii , o0oOoO00o )
 o00O0O ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iI1I ( )
 if 89 - 89: ii * o0ii1I * oOo0O0Ooo . i1iIi * o0ii1I / IiI1i11I
def oOOO0 ( url ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( url , ooI1111i , o0oOoO00o )
 iIIii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIIii
 print '======================================='
 extract . all ( ooI1111i , iIIii , o0oOoO00o )
 o00O0O ( url )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iI1I ( )
 if 46 - 46: Ii
def Iiiii ( name , url , description ) :
 iIIii = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 ooI1111i = os . path . join ( O0OoO000O0OO )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print iIIii
 print '======================================='
 extract . all ( ooI1111i , iIIii , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iI1I ( )
 if 25 - 25: I1ii11iIi11i * oOo0O0Ooo + oooOo0oo0oo + i1IiiiI1iI % oooOo0oo0oo
def OO0OO0O00oO0 ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def ooOoO00 ( log ) :
 xbmc . log ( "[%s]: %s" % ( i1iiIIiiI111 , log ) )
 if not os . path . exists ( oo0o0O00 ) : os . makedirs ( oo0o0O00 )
 if not os . path . exists ( oO ) : IiII111i1i11 = open ( oO , 'w' ) ; IiII111i1i11 . close ( )
 with open ( oO , 'a' ) as IiII111i1i11 :
  Ooo0o0000OO = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  IiII111i1i11 . write ( Ooo0o0000OO . rstrip ( '\r\n' ) + '\n' )
def iI1I ( ) :
 o0Oo00 = iIii1 . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if o0Oo00 == 0 : return
 elif o0Oo00 == 1 : pass
 oO0O00oOOoooO = OO0OO0O00oO0 ( )
 ooOoO00 ( "Platform: " + str ( oO0O00oOOoooO ) )
 os . _exit ( 1 )
 ooOoO00 ( "Force close failed!  Trying alternate methods." )
 if oO0O00oOOoooO == 'osx' :
  ooOoO00 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oO0O00oOOoooO == 'linux' :
  ooOoO00 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif oO0O00oOOoooO == 'android' :
  ooOoO00 ( "############ try android force close #################" )
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
 elif oO0O00oOOoooO == 'windows' :
  ooOoO00 ( "############ try windows force close #################" )
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
  ooOoO00 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  ooOoO00 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  iIii1 . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 8 - 8: Ii1I % i1i1I1IIii1II / o0ii1I
  if 37 - 37: i1i1I1IIii1II % i1IiiiI1iI % i1i1I1IIii1II
  if 14 - 14: oO0o / oOo0O0Ooo
def i1ii11I111Ii ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for oO0o0 , Ii1IIiII1I , OOOii in os . walk ( url ) :
  for file in OOOii :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    iiIiII = open ( ( os . path . join ( oO0o0 , file ) ) ) . read ( )
    i1Ii1i11ii = iiIiII . replace ( oOo0oooo00o , 'special://home/' )
    IiII111i1i11 = open ( ( os . path . join ( oO0o0 , file ) ) , mode = 'w' )
    IiII111i1i11 . write ( str ( i1Ii1i11ii ) )
    IiII111i1i11 . close ( )
 iI1I ( )
 if 58 - 58: OOooOOo + oO0o * o0ii1I
def oOo0OOoo0o ( ) :
 iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 31 - 31: i1i1I1IIii1II - IiI1i11I
def iIII11I ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def II1o0OoooOO00o ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def iIiIiiIIIi1 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in i1Iii1i1I :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , iIiIi11 , OOoO in IIi :
  ii11i ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , iIiIi11 )
def i1Ii1i111IIiIi1I ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( I11iiii )
 for url in IIi :
  OooO0OO ( url )
def oo00Oo0oO00Oo ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i
 iI1i1 = 'https://www.radionomy.com/en/search/index?query=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( iI1i1 )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  ii11i ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + O0O00Oo , 70005 , iIiIi11 )
  if 38 - 38: oO0o % o0ii1I % IIiIiII11i
  if 68 - 68: oooOo0oo0oo * oO0o / oO0o . iI11I1II1I1I
def O0ooooO ( ) :
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.listenlive.eu/' + O0O00Oo , 10111113 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , 'Radio Stations From Around The World.' )
def Oooo0oOooOO ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 if 27 - 27: oOo0O0Ooo * Ii / o0o00Oo0O / IIiIiII11i
 if 72 - 72: i1i1I1IIii1II - I1ii11iIi11i / Ii * oOo0O0Ooo + oO0o
 IIi = re . compile ( '<tr>\n<td><a href=".+?"><b>(.+?)</b></a>.+?<td>(.+?)</td>.+?<td><a href="([^"]*)">.+?<td>(.+?)</td>\n</tr>' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , I11iIIIIi1Iii1iIi , url , ii1IIi1iI1ii1 in IIi :
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' [COLORorangered] ' + ii1IIi1iI1ii1 + '[/COLOR]' , url , 222225 , iiIi1IIiIi + 'WorldRadio.png' , iiIi1IIiIi + 'WorldRadio.png' , '[COLOR' + ooOoOoo0O + ']' + OOoO + '[CR]' + I11iIIIIi1Iii1iIi + '[CR]' + ii1IIi1iI1ii1 + '[/COLOR]' )
  if 58 - 58: o0ii1I . Iii
def iIIiIi111iI ( ) :
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.toonjet.com/' + O0O00Oo , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1I1ii ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( I11iiii )
 for url , iIiIi11 in IIi :
  if 'ol.gif' in iIiIi11 :
   pass
  elif 'link_block_' in iIiIi11 :
   pass
  elif '.png' in iIiIi11 :
   pass
  else :
   iiIIIiIi1IIi ( ( iIiIi11 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  iiIIIiIi1IIi ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo0OO0O ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I11iiii )
 for url in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 64 - 64: i1i1I1IIii1II . Ii1I * i1IiiiI1iI % oOo0O0Ooo
  if 25 - 25: o0o00Oo0O + Iii + oooOo0oo0oo * Ii1I
def i1oo ( ) :
 iIi11I11 ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 iIi11I11 ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 87 - 87: I1ii11iIi11i . ii * i1IiiiI1iI * IIiIiII11i / ooOoO0O00 * OOooOOo
def I11IiIi1iI1ii ( ) :
 iIi11I11 ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 iIi11I11 ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 iIi11I11 ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 68 - 68: III1iiIii * oO0o . Iii / o0ii1I . I11i - Ii
def II11I ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OOoO , O0O00Oo , OOooo00oo in IIi :
  if 'Parent' in OOoO :
   pass
  elif '2' in OOooo00oo :
   iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 42 - 42: o0ii1I * o0o00Oo0O / i1i1I1IIii1II
def IiiiI11 ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OOoO , O0O00Oo , OOooo00oo in IIi :
  if IiiIi1IIII1i in OOoO . lower ( ) :
   if '1' in OOooo00oo :
    iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in OOooo00oo :
    iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in OOooo00oo :
    iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 57 - 57: iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
    if 95 - 95: i1i1I1IIii1II
def i11iiIi ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OOoO , O0O00Oo , OOooo00oo in IIi :
  if '1' in OOooo00oo :
   iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in OOooo00oo :
   iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in OOooo00oo :
   iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 31 - 31: Iii / i1iIi % i1i1I1IIii1II + ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 35 - 35: III1iiIii
def iIiIi1i1Iiii ( url ) :
 oo00ooOoo = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , OOoO in i1Iii1i1I :
  if 'mp3' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo00ooOoo + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo00ooOoo + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oo00ooOoo + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in OOoO :
   iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00ooOoo + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 78 - 78: I1ii11iIi11i - i1IiiiI1iI + IiI1i11I * o0ii1I * I11i
   if 23 - 23: I1ii11iIi11i - o0o00Oo0O
   if 33 - 33: Ii1I
def O0oOoo00Oo0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oo00ooOoo = url
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  if 'Parent' in OOoO :
   pass
  elif '.db' in OOoO :
   pass
  elif '.jpg' in OOoO :
   pass
  elif '.html' in OOoO :
   pass
  elif '.doc' in OOoO :
   pass
  elif 'mp3' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00ooOoo + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00ooOoo + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oo00ooOoo + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 5 - 5: o0o00Oo0O - IiI1i11I / i1IiiiI1iI . I11i
   if 7 - 7: Ii1I - OOooOOo
def OOoooIIII ( ) :
 iIi11I11 ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 iIi11I11 ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 iIi11I11 ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 87 - 87: III1iiIii
def oOOo0OOoOO0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + O0O00Oo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in iIiIi11 :
   pass
  else :
   iIi11I11 ( iIiIi11 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( O0O00Oo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + iIiIi11 + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 30 - 30: IIiIiII11i / oOo0O0Ooo - i1iIi + OOooOOo * i1iIi / OOooOOo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 17 - 17: oO0o
 if 31 - 31: i1i1I1IIii1II + ii - o0ii1I % I11i / I11i / iI11I1II1I1I
def Iii111Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  if '</a>' in OOoO :
   pass
  elif '(' in OOoO :
   iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 96 - 96: o0ii1I - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: I1ii11iIi11i + o0ii1I + oO0o
def o00o0o0oOo0 ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if IiiIi1IIII1i in OOoO . lower ( ) :
   if '</a>' in OOoO :
    pass
   elif '(' in OOoO :
    iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0O00Oo , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0O00Oo , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 33 - 33: ooOoO0O00 / III1iiIii - ooOoO0O00 . oOo0O0Ooo
    if 48 - 48: i1iIi + oooOo0oo0oo . i1IiiiI1iI % IIiIiII11i + i1i1I1IIii1II
def iiI1ii1i1 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if '</a>' in OOoO :
   pass
  elif '(' in OOoO :
   iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0O00Oo , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0O00Oo , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 42 - 42: ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: ooOoO0O00 . Ii1I
 if 77 - 77: IIiIiII11i - Ii
def o0o00O0oOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  oo00ooOoo = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( oo00ooOoo )
  if 68 - 68: Iii / iI11I1II1I1I . I1ii11iIi11i + Ii + I11i
def OOI1III1I11I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  if '<p align' in OOoO :
   pass
  elif '&nbsp;' in OOoO :
   pass
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 85 - 85: i1IiiiI1iI
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: o0ii1I % IIiIiII11i + III1iiIii + oooOo0oo0oo % i1i1I1IIii1II . oOo0O0Ooo
 if 53 - 53: oO0o % Ii1I . IiI1i11I . ooOoO0O00 . oO0o
def I11IIiIiI ( ) :
 II11iIiIIIiI = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIi = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'ongoing' in O0O00Oo :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 21005 , iiIi1IIiIi + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in O0O00Oo :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 21005 , iiIi1IIiIi + 'CartoonShows.png' , '' , '' )
  if 'disney' in O0O00Oo :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 21005 , iiIi1IIiIi + 'Disney.png' , '' , '' )
  if 'genre' in O0O00Oo :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 21005 , iiIi1IIiIi + 'Genre.png' , '' , '' )
  if 'years' in O0O00Oo :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 21005 , iiIi1IIiIi + 'Years.png' , '' , '' )
def iiII1II11i ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1iiiiI11ii = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , OOoO , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , iIiIi11 , iIiIi11 , OOoO )
 for url , OOoO in i1iiiiI11ii :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def ooO0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 II1 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OoooooOo0oOo0 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 II11II = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in OoooooOo0oOo0 :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , OOoO in II1 :
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def i1ii11 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 13 - 13: OOooOOo . Iii - ii / o0ii1I * I1ii11iIi11i
def oOO0OO0OO ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if '9cart' in O0O00Oo :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 26 - 26: OOooOOo
def I1I11I ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , OOoO in IiIi1I1 :
  if '9cart' in url :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 85 - 85: o0o00Oo0O * i1i1I1IIii1II
def iiIiiiIii11i1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 20003 , iIiIi11 )
 for url , OOoO in i1Iii1i1I :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 87 - 87: oO0o + ii . i1iIi * Iii
def oooOoO0oo0o0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   iiIIIiIi1IIi ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 4 - 4: Ii * Ii1I + ii - III1iiIii . i1iIi . iI11I1II1I1I
def IIiIIiI1iIII ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 72 - 72: III1iiIii % ooOoO0O00 / iI11I1II1I1I
def ooIii ( url ) :
 url = cloudflare . source ( url )
 OooOo ( url )
 if 66 - 66: oooOo0oo0oo * I11i
def OoOOO0o0Ooo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  OooOo ( url )
  if 19 - 19: Ii
  if 80 - 80: oOo0O0Ooo
def iIIIi1i1I11i ( ) :
 if 58 - 58: i1i1I1IIii1II + Ii1I % OOooOOo
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 22 - 22: iI11I1II1I1I - o0ii1I / oOo0O0Ooo * III1iiIii
def oO00OoOO ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 26 - 26: I11i + oooOo0oo0oo - I11i + I1ii11iIi11i . i1i1I1IIii1II
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 97 - 97: ooOoO0O00
 for O0O00Oo , OOoO in IIi :
  if IiiIi1IIII1i in OOoO . lower ( ) :
   if 'Dad!' in OOoO :
    pass
   elif 'Family Guy' in OOoO :
    pass
   elif '2 Stupid' in OOoO :
    pass
   elif 'The Zelfs' in OOoO :
    pass
   elif 'A Clone' in OOoO :
    pass
   elif 'A.T.O.M' in OOoO :
    pass
   elif 'Almost Naked' in OOoO :
    pass
   elif 'Angry Kid' in OOoO :
    pass
   elif 'Annoying Orange' in OOoO :
    pass
   elif 'Aqua Teen' in OOoO :
    pass
   elif 'Assy Mcgee' in OOoO :
    pass
   elif 'Astroblast' in OOoO :
    pass
   elif 'Atomic Betty' in OOoO :
    pass
   elif 'Axe Cop' in OOoO :
    pass
   elif 'Baby Playpen' in OOoO :
    pass
   elif 'Beavis and Butt' in OOoO :
    pass
   elif 'Celebrity Deathmatch' in OOoO :
    pass
   elif 'Clerks The' in OOoO :
    pass
   elif 'Crapston Villas' in OOoO :
    pass
   elif 'Duckman:' in OOoO :
    pass
   elif 'Stripperella' in OOoO :
    pass
   elif 'Vixen' in OOoO :
    pass
   else :
    Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
    if 46 - 46: Ii1I
    if 30 - 30: oO0o / o0o00Oo0O * I11i * i1IiiiI1iI + ii * IiI1i11I
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 23 - 23: Iii
def oOOoooO ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if 'Dad!' in OOoO :
   pass
  elif 'Family Guy' in OOoO :
   pass
  elif '2 Stupid' in OOoO :
   pass
  elif 'The Zelfs' in OOoO :
   pass
  elif 'A Clone' in OOoO :
   pass
  elif 'A.T.O.M' in OOoO :
   pass
  elif 'Almost Naked' in OOoO :
   pass
  elif 'Angry Kid' in OOoO :
   pass
  elif 'Annoying Orange' in OOoO :
   pass
  elif 'Aqua Teen' in OOoO :
   pass
  elif 'Assy Mcgee' in OOoO :
   pass
  elif 'Astroblast' in OOoO :
   pass
  elif 'Atomic Betty' in OOoO :
   pass
  elif 'Axe Cop' in OOoO :
   pass
  elif 'Baby Playpen' in OOoO :
   pass
  elif 'Beavis and Butt' in OOoO :
   pass
  elif 'Celebrity Deathmatch' in OOoO :
   pass
  elif 'Clerks The' in OOoO :
   pass
  elif 'Crapston Villas' in OOoO :
   pass
  elif 'Duckman:' in OOoO :
   pass
  elif 'Stripperella' in OOoO :
   pass
  elif 'Vixen' in OOoO :
   pass
  else :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 10006 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: III1iiIii . IiI1i11I - ooOoO0O00 + i1IiiiI1iI
def ooO ( url ) :
 I11iiii = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I11iiii )
 for iIiIi11 in i1Iii1i1I :
  Oo0O0o00o00 = iIiIi11
 IiIi1I1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I11iiii )
 for url in IiIi1I1 :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 10007 , Oo0O0o00o00 )
  if 90 - 90: i1IiiiI1iI . IIiIiII11i . Ii1I
  if 32 - 32: i1iIi - oO0o . IiI1i11I . IiI1i11I % ooOoO0O00 * o0ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 65 - 65: IiI1i11I / i1iIi . IIiIiII11i
def o0oO00oooo ( url , IMAGE ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  print OOoO + '     ' + url
  if 'easy' in url :
   ooo0Oo00O ( url )
   if 28 - 28: III1iiIii + OOooOOo . III1iiIii - o0ii1I % ooOoO0O00 % iI11I1II1I1I
   if 100 - 100: I1ii11iIi11i - oooOo0oo0oo * i1iIi * oO0o
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 64 - 64: Iii / IIiIiII11i / oO0o - i1iIi * iI11I1II1I1I . IiI1i11I
def ooo0Oo00O ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I11iiii )
 for url in IIi :
  OooO0OO ( url )
  if 25 - 25: oooOo0oo0oo - o0ii1I . Iii
  if 57 - 57: I11i + I1ii11iIi11i * Ii1I - i1iIi % iI11I1II1I1I - o0ii1I
  if 37 - 37: oO0o * Iii + o0ii1I + Ii1I * I11i
def O00oOo0o0 ( ) :
 if 81 - 81: IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * Ii + OOooOOo
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 100 - 100: ooOoO0O00 % o0ii1I
def oO000O ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  if 'elete' in OOoO :
   pass
  else :
   ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 222 , iIiIi11 )
   if 62 - 62: ooOoO0O00 * iI11I1II1I1I % i1i1I1IIii1II % OOooOOo / ii
def iI1111iiI1 ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OOO0ooO0Oo0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , oo000oOo0OoO0 , i1iII1IiiIiI1 in OOO0ooO0Oo0 :
  for IiiIi1IIII1i in oo000oOo0OoO0 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1iiIiiiiI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for O0O00Oo , OOoO in i1iiIiiiiI1 :
    if 'tube' in O0O00Oo :
     pass
    elif 'stage' in O0O00Oo :
     ii11i ( '[COLOR' + ooOoOoo0O + ']' + oo000oOo0OoO0 + '   -   ' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iIiIi11 , )
    elif 'vee' in O0O00Oo :
     pass
     if 42 - 42: oO0o - Ii1I * III1iiIii - i1iIi
def O0oO00oO0o00o ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 OOO0ooO0Oo0 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , oo000oOo0OoO0 , i1iII1IiiIiI1 in OOO0ooO0Oo0 :
  i1iiIiiiiI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for O0O00Oo , OOoO in i1iiIiiiiI1 :
   if 'tube' in O0O00Oo :
    pass
   elif 'stage' in O0O00Oo :
    ii11i ( '[COLOR' + ooOoOoo0O + ']' + oo000oOo0OoO0 + '   -   ' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iIiIi11 )
   elif 'vee' in O0O00Oo :
    pass
    if 54 - 54: i1iIi
    if 79 - 79: oOo0O0Ooo + i1i1I1IIii1II % Iii % i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: Ii1I + i1i1I1IIii1II . oO0o + ii * Ii1I - o0o00Oo0O
def IiiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 Iiii1I1 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( Iiii1I1 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in Iiii1I1 :
  o0oO0OoO0 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 35 - 35: oooOo0oo0oo . Iii . i1IiiiI1iI - Iii % Iii + i1IiiiI1iI
  if 99 - 99: I11i + oooOo0oo0oo
  if 34 - 34: i1IiiiI1iI * I11i . oOo0O0Ooo % Ii
  if 61 - 61: iI11I1II1I1I + i1i1I1IIii1II * Iii - ooOoO0O00 % i1i1I1IIii1II
  if 76 - 76: i1i1I1IIii1II / OOooOOo
  if 12 - 12: i1IiiiI1iI
  if 58 - 58: oO0o + iI11I1II1I1I % o0o00Oo0O + Iii + OOooOOo * ii
def O000OOO0OOo ( ) :
 if 41 - 41: i1i1I1IIii1II * oOo0O0Ooo
 OOoo0OoO ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 OOoo0OoO ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 3 - 3: III1iiIii - ii * ii - oOo0O0Ooo / i1IiiiI1iI * Ii1I
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 58 - 58: III1iiIii % iI11I1II1I1I / Ii % I11i . i1IiiiI1iI * IiI1i11I
def iiI1II ( ) :
 OOoo0OoO ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 OOoo0OoO ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 100 - 100: i1IiiiI1iI * I1ii11iIi11i - iI11I1II1I1I + oOo0O0Ooo - ooOoO0O00 + IiI1i11I
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
def i11111 ( ) :
 if 84 - 84: I11i
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 iIIiI1iiI = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 67 - 67: Ii1I - I11i
 for IIII in iIIiI1iiI :
  iI1iiiIiii = oO0 + IIII + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( iI1iiiIiii )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , oooOo0OOOoo0 , OOoO in IIi :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    IiIi ( OOoO , O0O00Oo , 222 , oo00O00oO000o , oooOo0OOOoo0 , OOOiiiiI )
    if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
    oOI1Ii1I1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 61 - 61: o0ii1I * o0ii1I
    if 70 - 70: i1IiiiI1iI . Ii1I / I11i * i1i1I1IIii1II
def OoI1 ( ) :
 if 88 - 88: ii - oooOo0oo0oo + o0o00Oo0O * III1iiIii * Iii
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 iIIiI1iiI = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 8 - 8: i1i1I1IIii1II / Ii
 for IIII in iIIiI1iiI :
  o0oo00000O = oO0 + IIII + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( o0oo00000O )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OOoO , OOOiiiiI , O0O00Oo , iIiIi11 , oooOo0OOOoo0 , OooOo00o in IIi :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    OOoo0OoO ( OOoO , O0O00Oo , OooOo00o , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
    if 84 - 84: iI11I1II1I1I
    oOI1Ii1I1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 25 - 25: oO0o * III1iiIii - ooOoO0O00 - Iii * IIiIiII11i
    if 70 - 70: IIiIiII11i + IiI1i11I * OOooOOo
def O0OOoO ( ) :
 if 12 - 12: ii + i1IiiiI1iI / oooOo0oo0oo / I1ii11iIi11i * IIiIiII11i - Ii1I
 I11iiii = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , OOOiiiiI , O0O00Oo , iIiIi11 , oooOo0OOOoo0 , OooOo00o in IIi :
  OOoo0OoO ( OOoO , O0O00Oo , OooOo00o , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
def i11IIi1Iii1 ( url ) :
 if 19 - 19: ooOoO0O00 % oO0o - Ii1I . i1IiiiI1iI . o0ii1I
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iI1I1oOOo = ( '%s%s' % ( iiII , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in IIi :
  ii1i1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for iII1i11 in ii1i1i :
   if iII1i11 == url :
    OOoO = ( '[COLORred]Watched - [/COLOR]' + OOoO ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  IiIi ( OOoO , url , 222 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
  if 88 - 88: ooOoO0O00
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
  if 53 - 53: i1iIi . oooOo0oo0oo . I11i + i1i1I1IIii1II
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + o0ii1I % ooOoO0O00 . i1i1I1IIii1II
  if 57 - 57: i1i1I1IIii1II
def OoOO00OO0 ( url ) :
 if 46 - 46: I11i . iI11I1II1I1I + ii - i1iIi * I1ii11iIi11i * Ii
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , OOOiiiiI , url , iIiIi11 , oooOo0OOOoo0 , OooOo00o in IIi :
  OOoo0OoO ( OOoO , url , OooOo00o , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  if 81 - 81: OOooOOo
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
  if 72 - 72: oO0o / I1ii11iIi11i * oO0o * oO0o
  if 74 - 74: I1ii11iIi11i + I1ii11iIi11i / Iii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 21 - 21: ii / III1iiIii
def IiIi ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 66 - 66: I11i * oO0o % ooOoO0O00 - iI11I1II1I1I
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111I11i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1OoOO = [ ]
  ii1OoOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1OoOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   ii1OoOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111I11i . addContextMenuItems ( ii1OoOO )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = False )
 return iiI1i1Iii111
 if 11 - 11: IiI1i11I / i1i1I1IIii1II % ooOoO0O00 . Ii1I
def OOoo0OoO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 16 - 16: ii - oooOo0oo0oo + I1ii11iIi11i
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111I11i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1OoOO = [ ]
  ii1OoOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1OoOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   ii1OoOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111I11i . addContextMenuItems ( ii1OoOO )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = True )
 return iiI1i1Iii111
if 67 - 67: Ii1I % ii
if 41 - 41: oO0o / III1iiIii + i1IiiiI1iI . i1IiiiI1iI / i1i1I1IIii1II
if 74 - 74: o0ii1I % Ii . o0o00Oo0O * oOo0O0Ooo * ooOoO0O00 * ii
if 22 - 22: i1IiiiI1iI + IiI1i11I - Iii + iI11I1II1I1I / i1IiiiI1iI - ii
if 42 - 42: ii - OOooOOo - oooOo0oo0oo * i1IiiiI1iI
if 98 - 98: oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
if 2 - 2: i1IiiiI1iI % ii - i1iIi * Ii1I * III1iiIii
if 99 - 99: iI11I1II1I1I . I1ii11iIi11i / i1iIi . oooOo0oo0oo % oOo0O0Ooo * Iii
if 95 - 95: i1i1I1IIii1II
if 80 - 80: III1iiIii
if 42 - 42: ii * IIiIiII11i
if 53 - 53: i1IiiiI1iI + ooOoO0O00 . oO0o / Ii + o0ii1I % OOooOOo
if 9 - 9: i1iIi . Iii - I1ii11iIi11i . i1IiiiI1iI
if 39 - 39: oooOo0oo0oo
if 70 - 70: III1iiIii % oO0o % oOo0O0Ooo
def OOo00oOo ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 51 - 51: IiI1i11I
def oOI1ii11IiI1I ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 Oo0 = [ ]
 try :
  if 20 - 20: o0o00Oo0O . Ii * ooOoO0O00 % o0o00Oo0O . oOo0O0Ooo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  OOo00oOo ( 'Making Favorites File' )
  Oo0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  iiIiII = open ( i1I1iI , "w" )
  iiIiII . write ( json . dumps ( Oo0 ) )
  iiIiII . close ( )
 else :
  OOo00oOo ( 'Appending Favorites' )
  iiIiII = open ( i1I1iI ) . read ( )
  o0Oo = json . loads ( iiIiII )
  o0Oo . append ( ( name , url , iconimage , fanart , mode ) )
  i1Ii1i11ii = open ( i1I1iI , "w" )
  i1Ii1i11ii . write ( json . dumps ( o0Oo ) )
  i1Ii1i11ii . close ( )
  if 29 - 29: o0o00Oo0O * Ii / ii / I11i . i1iIi
  if 70 - 70: ii . i1iIi / i1i1I1IIii1II . i1i1I1IIii1II - I11i
def i1II1i1iiI1 ( ) :
 if os . path . exists ( i1I1iI ) == False :
  Oo0 = [ ]
  OOo00oOo ( 'Making Favorites File' )
  Oo0 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  iiIiII = open ( i1I1iI , "w" )
  iiIiII . write ( json . dumps ( Oo0 ) )
  iiIiII . close ( )
 else :
  O0ooO0O00oo0 = json . loads ( open ( i1I1iI ) . read ( ) )
  OOoOi1IiiI = len ( O0ooO0O00oo0 )
  for II1i1iI in O0ooO0O00oo0 :
   OOoO = II1i1iI [ 0 ]
   O0O00Oo = II1i1iI [ 1 ]
   oo00O00oO000o = II1i1iI [ 2 ]
   try :
    iI111I1 = II1i1iI [ 3 ]
    if iI111I1 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     iI111I1 = oo00O00oO000o
    else :
     iI111I1 = oooOo0OOOoo0
   try : iIiii1IIi1I = II1i1iI [ 5 ]
   except : iIiii1IIi1I = None
   try : IiIiii1IiI = II1i1iI [ 6 ]
   except : IiIiii1IiI = None
   if 73 - 73: ii * o0o00Oo0O * i1iIi
   if II1i1iI [ 4 ] == 0 :
    Iii1I1I11iiI1 ( OOoO , O0O00Oo , '' , oo00O00oO000o , oooOo0OOOoo0 , '' , 'fav' )
   else :
    Iii1I1I11iiI1 ( OOoO , O0O00Oo , II1i1iI [ 4 ] , oo00O00oO000o , oooOo0OOOoo0 , '' , 'fav' )
    if 7 - 7: IIiIiII11i + ooOoO0O00
def OoooO0 ( name ) :
 o0Oo = json . loads ( open ( i1I1iI ) . read ( ) )
 for ii1O0oOOo in range ( len ( o0Oo ) ) :
  if o0Oo [ ii1O0oOOo ] [ 0 ] == name :
   del o0Oo [ ii1O0oOOo ]
   i1Ii1i11ii = open ( i1I1iI , "w" )
   i1Ii1i11ii . write ( json . dumps ( o0Oo ) )
   i1Ii1i11ii . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 33 - 33: oOo0O0Ooo * i1IiiiI1iI
 if 98 - 98: Ii1I - ii / oOo0O0Ooo . i1iIi - ooOoO0O00
def Oo0OOooo ( ) :
 oOOoOo0OoOO = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 OO00o = open ( oOOoOo0OoOO , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 OO00o . write ( r'[' + IiII + ']' + '\n' )
 for OOoO , iIiIi11 , IioOooo0OO0O0 , O0O00Oo in IIi :
  O0O00Oo = ( O0O00Oo + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  o0o0o0O0oo = ( OOoO + '=plugin://' + IiII + '/?url=' + O0O00Oo + '&mode=10012&name=' + ( OOoO ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( iIiIi11 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( iIiIi11 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  OO00o . write ( o0o0o0O0oo + '\n' )
  if 15 - 15: oooOo0oo0oo
  if 77 - 77: OOooOOo
def oOO0ooo0O ( ) :
 I11iiii = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo in IIi :
  iiIIIiIi1IIi ( '24/7' , O0O00Oo , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 17 - 17: i1iIi
def IIi1IIII ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iI1Ii1iI11iiI ( OOoO , ( O0O00Oo ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def iiiIIiiIi ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iI1Ii1iI11iiI ( OOoO , ( O0O00Oo ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def I1i11111i1i11 ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iI1Ii1iI11iiI ( OOoO , ( O0O00Oo ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def IiOo0ooooO0o00 ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iI1Ii1iI11iiI ( OOoO , ( O0O00Oo ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def iIIIIIi11Ii ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iI1Ii1iI11iiI ( OOoO , O0O00Oo , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 92 - 92: i1i1I1IIii1II / Ii1I
  if 6 - 6: Ii / ooOoO0O00 / III1iiIii . oOo0O0Ooo - oooOo0oo0oo % Ii
def o0OoOoOo0O ( ) :
 if 37 - 37: ooOoO0O00 . i1IiiiI1iI - IIiIiII11i % I11i - ooOoO0O00 . i1i1I1IIii1II
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
def IIIii111i ( ) :
 if 58 - 58: oooOo0oo0oo % IiI1i11I * o0o00Oo0O + Ii1I - III1iiIii
 I11iiii = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , iIiIi11 , OOoO , i11IiI1iiI11 in IIi :
  Iii1I1I11iiI1 ( OOoO + '  -  ' + ( i11IiI1iiI11 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , O0O00Oo , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 26 - 26: ooOoO0O00 / oOo0O0Ooo / Iii + Iii
  if 46 - 46: i1IiiiI1iI % Ii1I + o0ii1I
  if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / Iii + i1iIi
def i11IiIiii ( ) :
 if 15 - 15: i1iIi * iI11I1II1I1I * i1i1I1IIii1II
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
 if 96 - 96: i1IiiiI1iI * iI11I1II1I1I / OOooOOo % oooOo0oo0oo * IIiIiII11i
def I1iiIIii ( url ) :
 OO0OOO00 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( OO0OOO00 )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 90 - 90: III1iiIii * Iii % IIiIiII11i / oooOo0oo0oo
  if 97 - 97: IiI1i11I % i1iIi
  if 5 - 5: Ii1I * o0ii1I % Iii % IIiIiII11i
  if 9 - 9: I11i % i1IiiiI1iI + Iii
def oOOO00o00 ( ) :
 if 68 - 68: o0o00Oo0O * iI11I1II1I1I / i1IiiiI1iI
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 O0O00Oo = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( O0O00Oo )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  if IiiIi1IIII1i in OOoO . lower ( ) :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 65 - 65: oooOo0oo0oo - oOo0O0Ooo * i1IiiiI1iI
   if 99 - 99: oOo0O0Ooo
   if 64 - 64: Ii1I * o0ii1I * I1ii11iIi11i % III1iiIii % i1iIi
def OoO0000O ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oo00ooOoo , I1 , I1I1iI , OOoO in IIi :
  IIIOo0O = ( I1I1iI ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i1iIi1iiii1ii = ( I1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oO0oOo = 'Season ' + i1iIi1iiii1ii + 'Episode ' + IIIOo0O + OOoO
  IIiIiii ( oO0oOo , oo00ooOoo )
  if 71 - 71: I11i + oooOo0oo0oo . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 91 - 91: o0o00Oo0O - Iii % i1IiiiI1iI
  if 46 - 46: i1iIi / oOo0O0Ooo . III1iiIii % oO0o / Ii
def IIiIiii ( name , url ) :
 oo00ooOoo = url
 I1III1I1IiI = name
 o0o = cloudflare . source ( oo00ooOoo )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for Iiii1I1 , ooooooo0oOo0 in i1Iii1i1I :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + I1III1I1IiI + ooooooo0oOo0 + '[/COLOR]' , Iiii1I1 , 222 , iiIi1IIiIi + 'dtv.png' )
  if 81 - 81: Ii % oOo0O0Ooo / IiI1i11I % oO0o / i1IiiiI1iI % iI11I1II1I1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: Ii1I * I1ii11iIi11i + Ii % oooOo0oo0oo - i1i1I1IIii1II
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
def OoOo0oOooOoOO ( ) :
 if 95 - 95: i1IiiiI1iI + III1iiIii * iI11I1II1I1I
 if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / o0ii1I
 if 19 - 19: ooOoO0O00 - iI11I1II1I1I . Iii
 if 2 - 2: o0ii1I
 if 12 - 12: Ii - iI11I1II1I1I * III1iiIii * IiI1i11I
 if 19 - 19: o0o00Oo0O + i1i1I1IIii1II + I11i
 if 81 - 81: iI11I1II1I1I
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 51 - 51: I11i . Ii1I * o0ii1I / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
def Ii11II11iI1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OoOo0Oooo0o = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + iIiIi11 , '' , '' )
 for url in OoOo0Oooo0o :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 65 - 65: OOooOOo + i1IiiiI1iI % oOo0O0Ooo
def o0OO0OOOOOoOOOOooo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OoOo0Oooo0o = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  iIiIi11 = 'http://watchepisodes.cc/' + iIiIi11
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 10093 , iIiIi11 , iIiIi11 , '' )
 for url in OoOo0Oooo0o :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 29 - 29: i1IiiiI1iI / Ii1I * oOo0O0Ooo + IiI1i11I
def oOO00 ( url , iconimage ) :
 iIiIi11 = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1I1iI , url , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + I1I1iI + ' - ' + OOoO + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , iIiIi11 , '' , '' )
  if 14 - 14: oooOo0oo0oo / I11i + o0ii1I / ii - Iii
def O00o ( url , iconimage ) :
 iIiIi11 = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  if 'player' in OOoO :
   pass
  elif 'vod' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , iIiIi11 , '' , '' )
   if 65 - 65: OOooOOo / Ii1I / I11i
   if 15 - 15: i1iIi / i1iIi % ii . i1IiiiI1iI
   if 93 - 93: Ii1I * Ii1I / ii
   if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
   if 19 - 19: o0o00Oo0O % IIiIiII11i * I11i
   if 27 - 27: oooOo0oo0oo * III1iiIii / Ii - i1i1I1IIii1II + IIiIiII11i
def oo00ooOoO00 ( ) :
 if 43 - 43: Ii1I - IIiIiII11i
 if 56 - 56: Ii1I . ooOoO0O00 / IiI1i11I % i1i1I1IIii1II / o0o00Oo0O * Iii
 if 98 - 98: o0o00Oo0O + IiI1i11I
 if 23 - 23: ii . iI11I1II1I1I / ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / Iii . oO0o
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - III1iiIii
 if 50 - 50: oOo0O0Ooo - i1i1I1IIii1II + i1i1I1IIii1II * Iii + i1i1I1IIii1II
 if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
 if 30 - 30: OOooOOo - Ii
 if 94 - 94: OOooOOo % IiI1i11I
 if 39 - 39: OOooOOo + i1IiiiI1iI % o0o00Oo0O
 if 26 - 26: i1iIi + OOooOOo
 if 17 - 17: Ii1I - IiI1i11I % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * oooOo0oo0oo
 if 6 - 6: i1IiiiI1iI
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 46 - 46: IIiIiII11i * i1IiiiI1iI
 if 23 - 23: ooOoO0O00 - o0o00Oo0O
def I11iI11i1i1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIIiii = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( iiIIiii ) )
 for url , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 7 - 7: IiI1i11I
def i11i1ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 86 - 86: Ii - o0o00Oo0O - Ii . iI11I1II1I1I . III1iiIii
def Ooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  if 'episode' in url :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  else :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 65 - 65: I1ii11iIi11i . OOooOOo . oooOo0oo0oo % I11i + oO0o
  if 53 - 53: I1ii11iIi11i * Iii - o0ii1I % oO0o - OOooOOo - IiI1i11I
def IiIIII ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIo00OooooOOOO = 'http://www.watchseriesgo.to/search/' + IiiIi1IIII1i . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( iIo00OooooOOOO )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , O0O00Oo , OOoO in IIi :
  if 'watch online' in OOoO :
   pass
  else :
   print O0O00Oo
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.watchseriesgo.to' + O0O00Oo , 10044 , iIiIi11 , '' , '' )
   if 89 - 89: o0o00Oo0O + III1iiIii * i1IiiiI1iI
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 30 - 30: OOooOOo
def IIIII11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO , I1I1iI , OOOiiiiI in IIi :
  OOO0oOoO0O = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( I1I1iI ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOO0oOoO0O + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iIiIi11 , '' , OOOiiiiI )
  if 48 - 48: i1IiiiI1iI / i1iIi . iI11I1II1I1I
def ooo0OOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  OOO0oOoO0O = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOO0oOoO0O + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 52 - 52: oO0o
def I1O0oO0oo0oOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iIiIi11 , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 5 - 5: ii * Ii1I
def IIio0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iiIIiii = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1 , OOO0ooO0Oo0 in iiIIiii :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( OOO0ooO0Oo0 ) )
  for url , OOoO in IIi :
   OOO0oOoO0O = ( I1 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOO0oOoO0O + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 27 - 27: OOooOOo . i1IiiiI1iI * OOooOOo
class iI111iI11iII ( ) :
 if 67 - 67: oooOo0oo0oo - o0ii1I % IiI1i11I / IIiIiII11i + oOo0O0Ooo * i1iIi
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 100 - 100: Ii1I
  OOO0oOoO0O = name
  self . Get_Sources ( O0O00Oo , OOO0oOoO0O )
  if 81 - 81: Ii1I % IiI1i11I
  if 22 - 22: ii + I11i . Iii + oOo0O0Ooo + ii . OOooOOo
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for O0O00Oo , OOoO in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + O0O00Oo
   self . Get_site_link ( URL , season_name )
   if 93 - 93: oOo0O0Ooo
 def Get_site_link ( self , url , season_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  i1Iii1i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  IiIi1I1 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for url in IIi :
   self . main ( url , season_name )
  for url in i1Iii1i1I :
   self . main ( url , season_name )
  for url in IiIi1I1 :
   self . main ( url , season_name )
   if 89 - 89: ii % Ii + i1IiiiI1iI
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   iI1II1iIiiiI = 'DACLIPS'
   if iI1II1iIiiiI in iI111iI11iII . source_list :
    pass
   else :
    self . daclips ( url , season_name , iI1II1iIiiiI )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    iI1II1iIiiiI = 'THEVIDEO'
    if iI1II1iIiiiI in iI111iI11iII . source_list :
     pass
    else :
     self . thevideo ( url , season_name , iI1II1iIiiiI )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     iI1II1iIiiiI = 'ALLMYVIDEOS'
     if iI1II1iIiiiI in iI111iI11iII . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , iI1II1iIiiiI )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      iI1II1iIiiiI = 'VIDSPOT'
      if iI1II1iIiiiI in iI111iI11iII . source_list :
       pass
      else :
       self . vidspot ( url , season_name , iI1II1iIiiiI )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       iI1II1iIiiiI = 'VODLOCKER'
       if iI1II1iIiiiI in iI111iI11iII . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , iI1II1iIiiiI )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        iI1II1iIiiiI = 'VIDTO'
        if iI1II1iIiiiI in iI111iI11iII . source_list :
         pass
        else :
         self . vidto ( url , season_name , iI1II1iIiiiI )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 9 - 9: o0ii1I
       else :
        if 'youwatch' in url :
         iI1II1iIiiiI = 'YouWatch'
         if iI1II1iIiiiI in iI111iI11iII . source_list :
          pass
         else :
          self . youwatch ( url , season_name , iI1II1iIiiiI )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 1 - 1: o0o00Oo0O + IiI1i11I * i1iIi - Ii
          if 18 - 18: i1iIi
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for o00o00OoO00o0 , OOoO in IIi :
   self . Printer ( o00o00OoO00o0 , season_name , source_name )
   if 37 - 37: I1ii11iIi11i % Ii - oOo0O0Ooo * Ii1I . i1iIi
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for o00o00OoO00o0 , OOoO in IIi :
   self . Printer ( o00o00OoO00o0 , season_name , source_name )
   if 62 - 62: ii / i1iIi + Ii1I . I11i - IiI1i11I
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for o00o00OoO00o0 in IIi :
   self . Printer ( o00o00OoO00o0 , season_name , source_name )
   if 29 - 29: i1i1I1IIii1II
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for o00o00OoO00o0 in IIi :
   self . Printer ( o00o00OoO00o0 , season_name , source_name )
   if 26 - 26: o0o00Oo0O % oooOo0oo0oo - III1iiIii . oooOo0oo0oo
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for o00o00OoO00o0 in IIi :
   self . Printer ( o00o00OoO00o0 , season_name , source_name )
   if 70 - 70: I11i + Iii / IiI1i11I + i1iIi / oOo0O0Ooo
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for o00o00OoO00o0 in IIi :
   self . Printer ( o00o00OoO00o0 , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for o00o00OoO00o0 in IIi :
   self . Printer ( o00o00OoO00o0 , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for o00o00OoO00o0 in IIi :
   self . youplay ( o00o00OoO00o0 , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for o00o00OoO00o0 in IIi :
   self . Printer ( o00o00OoO00o0 , season_name , source_name )
   if 33 - 33: ii . o0o00Oo0O
 def Printer ( self , Link , season_name , source_name ) :
  if 59 - 59: iI11I1II1I1I
  if Link in iI111iI11iII . List :
   pass
  elif source_name in iI111iI11iII . source_list :
   pass
  else :
   ii11i ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   iI111iI11iII . List . append ( Link )
   iI111iI11iII . source_list . append ( source_name )
   if 45 - 45: o0o00Oo0O
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 78 - 78: Iii - iI11I1II1I1I + i1IiiiI1iI - Ii1I - i1IiiiI1iI
   if 21 - 21: ii . o0o00Oo0O / Ii
   if 86 - 86: OOooOOo / oooOo0oo0oo
   if 40 - 40: iI11I1II1I1I / i1iIi / oOo0O0Ooo + Ii1I * oooOo0oo0oo
   if 1 - 1: oO0o * i1iIi + III1iiIii . i1i1I1IIii1II / i1iIi
def O0Oooo ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 91 - 91: o0ii1I + Iii - I1ii11iIi11i % OOooOOo . IiI1i11I
def oO0OO ( url ) :
 OOO00O0OO = '20'
 oOO0O = [ ]
 OOooOOoOoo0o = '                                                    '
 I1i11i1II = '        '
 Iii1I1I11iiI1 ( OOooOOoOoo0o + 'pl' + I1i11i1II + 'w' + I1i11i1II + 'd' + I1i11i1II + 'l' + I1i11i1II + 'f' + I1i11i1II + 'a' + I1i11i1II + 'pts' , '' , '' , '' , '' , '' )
 I11iiii = oOoo000 ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( I11iiii )
 for OOoOo0oOooo , OOo0o , Ooo0O0ooo0o , O0o0o , O0Oo , IiII111i1i11 , iiIiII , O0oOo00Oo0oo0 , i111 in IIi :
  O0oOO0o00OO = II1i11i1iI1I ( OOo0o )
  oooOoO00O = II1i11i1iI1I ( Ooo0O0ooo0o )
  I1i1IIiiI11II = II1i11i1iI1I ( O0o0o )
  Ii1i1 = II1i11i1iI1I ( O0Oo )
  iiiIiIIiIiiii = II1i11i1iI1I ( IiII111i1i11 )
  o00O0OooO0 = II1i11i1iI1I ( iiIiII )
  oOO0O . append ( OOoOo0oOooo [ 0 ] )
  iii1II11II1 = len ( oOO0O )
  I11i1Iii1I = int ( len ( OOooOOoOoo0o ) - len ( OOoOo0oOooo ) - 2 )
  if len ( oOO0O ) >= 10 :
   I11i1Iii1I = I11i1Iii1I - 1
  if len ( oOO0O ) <= int ( OOO00O0OO ) :
   iI1Ii1iI11iiI ( str ( iii1II11II1 ) + ' ' + OOoOo0oOooo + OOooOOoOoo0o [ 0 : I11i1Iii1I ] + OOo0o + O0oOO0o00OO + Ooo0O0ooo0o + oooOoO00O + O0o0o + I1i1IIiiI11II + O0Oo + Ii1i1 + IiII111i1i11 + iiiIiIIiIiiii + iiIiII + o00O0OooO0 + ' ' + i111 , '' , '' , '' , '' , '' )
   if 11 - 11: I1ii11iIi11i + IIiIiII11i - Ii1I
   if 57 - 57: ii . Ii1I - i1i1I1IIii1II * ooOoO0O00 . Iii
def II1i11i1iI1I ( space ) :
 if len ( space ) > 1 :
  I1ii1i11i = len ( '        ' ) - len ( space ) + 1
  space = int ( I1ii1i11i ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 17 - 17: I11i * Ii * IIiIiII11i - o0ii1I % I11i / o0o00Oo0O
def IIIIOo0oO ( ) :
 if 65 - 65: oO0o * IIiIiII11i / iI11I1II1I1I
 if 19 - 19: oooOo0oo0oo . Ii . Iii * Iii
 if 69 - 69: ooOoO0O00
 if 96 - 96: Iii - Ii % ooOoO0O00 . iI11I1II1I1I
 if 73 - 73: oOo0O0Ooo * oooOo0oo0oo + oO0o % i1i1I1IIii1II / ooOoO0O00
 if 36 - 36: oooOo0oo0oo * i1IiiiI1iI + IIiIiII11i + ii + IiI1i11I % Iii
 if 53 - 53: IIiIiII11i . IIiIiII11i
 if 18 - 18: o0ii1I + OOooOOo . ooOoO0O00 / III1iiIii / IiI1i11I
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
 if 8 - 8: I11i
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
 if 48 - 48: o0ii1I - ii + i1IiiiI1iI % I11i - OOooOOo . oOo0O0Ooo
 if 42 - 42: i1IiiiI1iI
 if 70 - 70: I11i / Iii + i1i1I1IIii1II % oOo0O0Ooo % I1ii11iIi11i + oO0o
 if 80 - 80: oooOo0oo0oo
 if 12 - 12: o0ii1I
 if 2 - 2: ii
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + O0O00Oo , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iIiIi11 , Oo00OOOOO , '' )
  if 46 - 46: o0o00Oo0O % ii
def I1IiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIIiii = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iiIIiii in iiIIiii :
  iIi11I = re . compile ( '(.*?)</h2>' ) . findall ( str ( iiIIiii ) )
  for o0O00o0o in iIi11I :
   o0O00o0o = o0O00o0o
  I11Ii111IIi = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iiIIiii ) )
  for OoOoO0OooO00Oo , iIiIi11 , time , I1iiiiii in I11Ii111IIi :
   I1ii1Ii1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I1iiiiii )
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + o0O00o0o + ' - ' + OoOoO0OooO00Oo + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iIiIi11 , Oo00OOOOO , ( str ( I1ii1Ii1 ) ) )
   if 81 - 81: Ii1I - oO0o * i1i1I1IIii1II
 oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if 81 - 81: IiI1i11I - o0ii1I - oooOo0oo0oo % III1iiIii % I11i . iI11I1II1I1I
def OOoOo00O0 ( ) :
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
 if 86 - 86: iI11I1II1I1I * IiI1i11I * o0ii1I / oO0o % i1iIi - o0o00Oo0O
def ooOOO0Oo ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  IiIiI1I1IIIi1 = OOoO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OOoO :
   pass
  else :
   IiIiI1I1IIIi1 = OOoO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   ii11i ( '[COLOR' + ooOoOoo0O + ']' + IiIiI1I1IIIi1 + '[/COLOR]' , url , 10013 , iIiIi11 )
 for url , iIiIi11 , OOoO in i1Iii1i1I :
  IiIiI1I1IIIi1 = OOoO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OOoO :
   pass
  else :
   ii11i ( '[COLOR' + ooOoOoo0O + ']' + IiIiI1I1IIIi1 + '[/COLOR]' , url , 10013 , iIiIi11 )
def iII11I ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 44 - 44: IiI1i11I
 if 79 - 79: I11i % oooOo0oo0oo . o0o00Oo0O
 if 56 - 56: i1i1I1IIii1II + ooOoO0O00 * IiI1i11I - o0o00Oo0O
 if 84 - 84: IiI1i11I % oOo0O0Ooo / iI11I1II1I1I * o0ii1I * iI11I1II1I1I + Ii1I
 if 78 - 78: III1iiIii / IiI1i11I * o0ii1I . oooOo0oo0oo . i1i1I1IIii1II - i1IiiiI1iI
 if 39 - 39: i1iIi . ooOoO0O00 + ii . IiI1i11I - Ii % i1IiiiI1iI
 if 38 - 38: i1i1I1IIii1II
 for url , iIiIi11 , OOoO in i1Iii1i1I :
  IiIiI1I1IIIi1 = OOoO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OOoO :
   pass
  else :
   ii11i ( '[COLOR' + ooOoOoo0O + ']' + IiIiI1I1IIIi1 + '[/COLOR]' , url , 10013 , iIiIi11 )
   if 9 - 9: Iii . oO0o . i1i1I1IIii1II / ii
def oo0ooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for Iiii1I1 in IIi :
  ii1Ii = ( Iiii1I1 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  o0oO0OoO0 ( 'http:' + ii1Ii )
  if 41 - 41: Ii1I % Ii1I + III1iiIii . IiI1i11I % i1IiiiI1iI * i1iIi
  if 57 - 57: o0ii1I . i1IiiiI1iI . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
  if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
  if 93 - 93: i1iIi / oooOo0oo0oo * o0o00Oo0O
def iI11 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO , iIiIi11 in IIi :
  ii11i ( OOoO , url , 8046 , iIiIi11 )
 for url in i1Iii1i1I :
  iiIIIiIi1IIi ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def i1IiI1Ii ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  o0oO0OoO0 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 60 - 60: Ii1I / III1iiIii . Ii / oO0o % IIiIiII11i
def i1II111II1 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I11iiii )
 for url in IIi :
  yt . PlayVideo ( url )
  if 8 - 8: III1iiIii - Ii1I * iI11I1II1I1I % I11i / ii * I11i
def I1I1i ( ) :
 iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , O0O00Oo , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOoO00O00o ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( I11iiii )
 for iIiIi11 , url , OOoO in IIi :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + iIiIi11 )
 for url in next :
  iiIIIiIi1IIi ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 69 - 69: ooOoO0O00 . o0ii1I
  if 96 - 96: o0ii1I
def O00O0O0 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I11iiii )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   ii11i ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def ii1IiIi1iIi ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , '' )
  if 16 - 16: oooOo0oo0oo % oOo0O0Ooo . i1IiiiI1iI * oO0o % o0o00Oo0O . oooOo0oo0oo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOOOoO0 ( name , url ) :
 iiIii1iii = 0
 name = name
 url = url
 IiI1i = [ '144' , '240' , '380' , '480' , '720' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  OooO0OO ( url )
  if 61 - 61: I11i - Ii1I * I11i % iI11I1II1I1I / III1iiIii
  if 34 - 34: i1i1I1IIii1II - IIiIiII11i - I11i + IiI1i11I + i1IiiiI1iI
  if 70 - 70: ii + oO0o * I1ii11iIi11i
  if 20 - 20: Ii - IIiIiII11i - i1iIi % i1i1I1IIii1II . i1iIi
  if 50 - 50: iI11I1II1I1I + i1IiiiI1iI - Iii - ii
  if 84 - 84: OOooOOo - Iii
  if 80 - 80: Ii % oooOo0oo0oo - I1ii11iIi11i % oooOo0oo0oo
  if 89 - 89: o0ii1I * Iii + OOooOOo / Ii
def oo00ooOOOo0O ( ) :
 I11iiii = O00Oo0o000oO ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  if 'genre' in O0O00Oo :
   iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , O0O00Oo , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def i11111i1I1IiI ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( I11iiii )
 for url , OOoO , iIiIi11 in IIi :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , iIiIi11 )
 for url in next :
  iiIIIiIi1IIi ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 27 - 27: ii * Iii % ii * I1ii11iIi11i * i1iIi
def I1IIo0o0OoOO00Oo ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( I11iiii )
 for url in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  ii1IiIi1iIi ( url )
  if 33 - 33: IiI1i11I % ii / i1i1I1IIii1II
def II1iIIiI ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi11i = 'http://documentarylovers.com/?s=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 O0ooOoO = iIi11i . lower ( )
 i11111i1I1IiI ( O0ooOoO )
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
def i1IO0OoO0o ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if 'films' in url :
   iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def o0Oo00oOOO0o ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I11iiii )
 for iIiIi11 , url , OOoO in IIi :
  if 'films' in url :
   ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + iIiIi11 )
 for url in i1Iii1i1I :
  iiIIIiIi1IIi ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def o0ii1I1 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I11iiii )
 for url in IIi :
  if 'rtd' in url :
   ii1oo ( url )
   if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
def ii1oo ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( I11iiii )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  OooO0OO ( url )
  if 34 - 34: I11i % Ii1I + o0ii1I * Iii / i1i1I1IIii1II
  if 18 - 18: i1iIi
def OOoo00o0OoO ( ) :
 II11iIiIIIiI = O00Oo0o000oO ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO , oOo00o00oO in IIi :
  iiIIIiIi1IIi ( ( OOoO + '[COLOR' + ooOoOoo0O + ']' + oOo00o00oO + '[/COLOR]' ) , O0O00Oo , 8086 , iIiIi11 )
  if 24 - 24: III1iiIii . IiI1i11I * III1iiIii % Ii . Ii + ooOoO0O00
def Ooo0 ( url ) :
 II11iIiIIIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOoO in IIi :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 8087 , iIiIi11 )
  if 53 - 53: i1iIi - OOooOOo + III1iiIii
def oOO0Ooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  IiIi1I1iI1 ( url , OOoO )
  if 74 - 74: ooOoO0O00 . iI11I1II1I1I
def IiIi1I1iI1 ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 85 - 85: oOo0O0Ooo
def iii1I ( ) :
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + O0O00Oo , 3002 , 'http://www.solie.org/alibrary/' + iIiIi11 )
def iIiI11I ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iIiIi11 )
def IIII11 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 I11I1I1I = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I11iiii )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , OOoO in I11I1I1I :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']Season- ' + OOoO + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , iIiIi11 , OOoO in i1Iii1i1I :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iIiIi11 )
def ooOo0o0 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I11iiii )
 for url in IIi :
  O000ooOOO ( url )
def O000ooOOO ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I11iiii )
 for url in IIi :
  OooO0OO ( url )
  if 75 - 75: Iii * oooOo0oo0oo % i1i1I1IIii1II - Ii1I / ii / oooOo0oo0oo
def oOO ( ) :
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , O0O00Oo , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def o0oOoOOO ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( I11iiii )
 for url in IIi :
  OooOo ( url )
  if 74 - 74: IiI1i11I / i1IiiiI1iI / IIiIiII11i - IiI1i11I / i1i1I1IIii1II % Iii
def oo000ii ( ) :
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , O0O00Oo , 8065 , iiIi1IIiIi + 'classictv.png' )
def i1Iiiiii1II ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  if 'mp4' in url :
   OooO0OO ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 50 - 50: OOooOOo
def oO0oo00o ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + O0O00Oo , 8071 , iiIi1IIiIi + 'streams.png' )
def o0Oo0oOO00O ( url ) :
 II11iIiIIIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  if '(Free Access)' in OOoO :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def Oo00OO ( url ) :
 II11iIiIIIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iIiIi11 , oooOo0OOOoo0 , '' )
  if 19 - 19: o0o00Oo0O + o0ii1I * o0ii1I * ooOoO0O00
def iI11Iii1ii111 ( ) :
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  i11IIiiI ( 'http://watchxxxfree.com/categories' )
 if o0Oo00 == 1 :
  OOoo ( 'http://www.perfectgirls.net' )
 if o0Oo00 == 2 :
  iIi1 ( 'http://www.xvideos.com/best' )
 if o0Oo00 == 3 :
  iiiIIIIiI1iiI ( 'http://www.xvideos.com/best' )
 if o0Oo00 == 4 :
  iIi1 ( 'http://www.xvideos.com/best' )
 if o0Oo00 == 5 :
  iIi1 ( 'http://www.xvideos.com/verified/videos' )
 if o0Oo00 == 6 :
  i1IO00oO0oOOOOOO ( 'http://www.xvideos.com/tags' )
 if o0Oo00 == 7 :
  Oo0ooo00OoO ( 'http://www.xvideos.com/porn' )
 if o0Oo00 == 8 :
  Iiii1I1I111i1 ( )
  if 66 - 66: oooOo0oo0oo / iI11I1II1I1I - OOooOOo % o0o00Oo0O . i1iIi
  if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
  if 37 - 37: ooOoO0O00 * Ii
  if 95 - 95: Ii % i1IiiiI1iI * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
  if 7 - 7: oO0o * Ii * iI11I1II1I1I / oooOo0oo0oo / i1IiiiI1iI
  if 35 - 35: IiI1i11I * oooOo0oo0oo
  if 65 - 65: IIiIiII11i % ooOoO0O00
  if 13 - 13: oO0o * i1IiiiI1iI + I1ii11iIi11i - III1iiIii
  if 31 - 31: oO0o
def OOooOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  if 'ch' in url :
   iIi11I11 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def ooO00OoIIiI1iiIII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 oo0 = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for OOoO , url in oo0 :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OooOoOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   iIIii1i1iIiI ( url )
def oOooooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def i11IIiiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO , I1ii1i11i in IIi :
  if 'category' in url :
   iIi11I11 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORorange]   ' + I1ii1i11i + '[/COLOR]' , url , 90006 , iIiIi11 , iiIi1IIiIi + 'Jizbox.png' , '' )
def OO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oo0 = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , iIiIi11 , '' , '' )
 for url in oo0 :
  Iii1I1I11iiI1 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def iI1iII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   iIIii1i1iIiI ( url )
def iIIii1i1iIiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def OOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO , I1ii1i11i in IIi :
  if 'category' in url :
   iIi11I11 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORorange]' + I1ii1i11i + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def o0iiI11 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oo00ooOoo = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oo0 = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , iIiIi11 in IIi :
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , iIiIi11 , '' , '' )
 for url in oo0 :
  Iii1I1I11iiI1 ( '[COLORred]NEXT[/COLOR]' , oo00ooOoo + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def IiiiIII1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OOooo0o0oOO0 ( 'http://www.perfectgirls.net' + url )
def OOooo0o0oOO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  o0oO0OoO0 ( 'http://' + url )
def Oo0ooo00OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , I1ii1i11i in IIi :
  iIi11I11 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgreen] - No of Videos : [COLORorange]' + I1ii1i11i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def i1IO00oO0oOOOOOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oo0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in oo0 :
  iIi11I11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , I1ii1i11i in IIi :
  iIi11I11 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgreen] - No of Videos : [COLORorange]' + ( I1ii1i11i + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 30 - 30: i1IiiiI1iI % i1i1I1IIii1II + i1i1I1IIii1II * ii - Ii1I
def OOoOOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oo0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in oo0 :
  iIi11I11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO , oooO0I11Iii11i11I1 in IIi :
  iIi11I11 ( OOoO + '--' + ( oooO0I11Iii11i11I1 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iIiIi11 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 22 - 22: OOooOOo . IIiIiII11i
  if 24 - 24: ii / Iii
def iIi1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO , iIO0o , OO00Oo00o in IIi :
  iIi11I11 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgreen] - Porn Quality : [COLORorange]' + OO00Oo00o + ' - [COLORred]' + iIO0o + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , iIiIi11 , iIiIi11 , OO00Oo00o + ' - ' + iIO0o )
 IiII1Iiii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in IiII1Iiii :
  iIi11I11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 16 - 16: IiI1i11I . o0o00Oo0O - i1IiiiI1iI * i1IiiiI1iI
def iiiIIIIiI1iiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 iiIIiii = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oo0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in oo0 :
  iIi11I11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( iiIIiii ) )
 for url , OOoO in IIi :
  if '/c/' in url :
   iIi11I11 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 80 - 80: o0ii1I % Ii1I
   if 60 - 60: oO0o % iI11I1II1I1I . i1iIi * I11i % i1iIi - i1IiiiI1iI
def Iiii1I1I111i1 ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O000oo0O0OO0 = ( IiiIi1IIII1i ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 O0ooOoO = O000oo0O0OO0 . lower ( )
 iI1i1 = 'http://www.xvideos.com/?k=' + O0ooOoO
 print iI1i1 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( iI1i1 )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , O0O00Oo , OOoO , iIO0o , OO00Oo00o in IIi :
  iIi11I11 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgreen] - Porn Quality : [COLORorange]' + OO00Oo00o + ' - [COLORred]' + iIO0o + '[/COLOR]' , 'http://www.xvideos.com' + O0O00Oo , 10108 , iIiIi11 , iIiIi11 , OO00Oo00o + ' - ' + iIO0o )
 IiII1Iiii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo in IiII1Iiii :
  iIi11I11 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + O0O00Oo , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 58 - 58: oO0o - ii . IiI1i11I
if 26 - 26: OOooOOo
if 48 - 48: IiI1i11I
if 85 - 85: Ii1I . i1i1I1IIii1II . o0o00Oo0O
if 16 - 16: Ii1I % Ii1I % i1IiiiI1iI + Iii . i1IiiiI1iI + oooOo0oo0oo
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
 IiIi1I1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   ii11i ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   ii11i ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in IiIi1I1 :
  if 'http' in url :
   ii11i ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 43 - 43: OOooOOo % o0ii1I + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
def OOOOo00oOOO00 ( url ) :
 II1 = xbmc . Player ( iiIIIiIii ( ) )
 import urlresolver
 try : II1 . play ( url )
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
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 8091 , iiIi1IIiIi + 'gofish.png' )
def O0O0OOo00Oo ( url ) :
 II11iIiIIIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO , iIiIi11 in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 8092 , iIiIi11 )
 for url in next :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def IiI1iIIiIi1Ii ( url ) :
 II11iIiIIIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 O0oOoOOO000 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 in O0oOoOOO000 :
  iIiIi11 = iIiIi11
 for url , OOoO in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 8092 , iIiIi11 )
 for url in next :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
  if 57 - 57: I11i - III1iiIii . oooOo0oo0oo
def IIiIiiii1I1 ( url ) :
 II11iIiIIIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( "videoId: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  yt . PlayVideo ( url )
  if 39 - 39: i1IiiiI1iI / IiI1i11I
  if 65 - 65: ooOoO0O00 . iI11I1II1I1I - i1iIi * oooOo0oo0oo
  if 50 - 50: i1IiiiI1iI % i1iIi - I11i
  if 52 - 52: Ii1I
o0oI1 = '{PQ},' ; i1IO0OOoooO = '{SC},' ; ooO0OOoOoOO00 = '{XG},' ; o0O00 = '{JP},' ; ii1IiI111II = '{HW},' ; iI11IiiI1i = '{RT},'
def I1IiiI1ii1i ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 IiIi1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 O0O00Oo = 'http://onlinemovies.tube/?s=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 oo00ooOoo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 iii1IIIiiiI = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 OoO00oo00 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 iiiI1i11Ii = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIiII = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IiiIi1IIII1i
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 oo0o0oOo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 9 - 9: IiI1i11I
 IIo00ooo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 Ii1IiIiIi1IiI = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 100 - 100: IiI1i11I / I11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( O0O00Oo )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( oo00ooOoo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iii1IIIiiiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( OoO00oo00 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 iIIi1iI1I1IIi = O00O0oOO00O00 ( Oo0Oo0O )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 O0OO0 = O00O0oOO00O00 ( iIiII )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O0ooo0o0 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 oO0ooOoO = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 11 - 11: Ii1I * OOooOOo % Ii - o0ii1I
 if 77 - 77: IIiIiII11i - I11i . Ii1I
 Oo = O00O0oOO00O00 ( IIo00ooo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 oO00oOOo0Oo = O00O0oOO00O00 ( Ii1IiIiIi1IiI )
 if 63 - 63: i1i1I1IIii1II
 if oO0ooOoO != 'Failed' :
  oOOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oO0ooOoO )
  for O0O00Oo , OOoO in oOOO :
   iIi1I1 = O00O0oOO00O00 ( O0O00Oo )
   O0oOoo0OoO0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi1I1 )
   for oo00IiI1 , oOo00o00oO in O0oOoo0OoO0O :
    oOo00o00oO = ( oOo00o00oO . replace ( '.' , ' ' ) )
    if O0ooOoO in oOo00o00oO . lower ( ) :
     if '.mkv' in oo00IiI1 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + oo00IiI1 , 222 , '' , '' , '' )
     elif '.mp4' in oo00IiI1 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + oo00IiI1 , 222 , '' , '' , '' )
     elif '.avi' in oo00IiI1 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + oo00IiI1 , 222 , '' , '' , '' )
     elif '.wav' in oo00IiI1 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + oo00IiI1 , 222 , '' , '' , '' )
     else :
      Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + oo00IiI1 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 79 - 79: Ii1I - i1i1I1IIii1II - I11i . oooOo0oo0oo
      oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in i1Iii1i1I :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] source Technica[/COLOR]' ) , O0O00Oo , 222 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 65 - 65: Ii . oO0o % IiI1i11I + III1iiIii - Ii
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 60 - 60: i1IiiiI1iI
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for OOoo0 , OOoO in IiIi1I1 :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iii1IIIiiiI + OOoo0 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in I1i11 :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] source RaizTv[/COLOR]' ) , O0O00Oo , 222 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 14 - 14: I1ii11iIi11i % i1i1I1IIii1II * IiI1i11I - Ii / Ii1I * Ii
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if iIIi1iI1I1IIi != 'Failed' :
  IiI1i111IiIiIi1 = [ ]
  iii1IIII1iii11I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi1iI1I1IIi )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in iii1IIII1iii11I :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    if OOoO in IiI1i111IiIiIi1 :
     pass
    else :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , O0O00Oo , 1016 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
     IiI1i111IiIiIi1 . append ( OOoO )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if O0OO0 != 'Failed' :
  i1II11II1 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( O0OO0 )
  for O0O00Oo , iIiIi11 , OOoO in i1II11II1 :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + O0O00Oo , 7067 , iIiIi11 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * Iii + oooOo0oo0oo
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if Oo != 'Failed' :
  i111II = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in i111II :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source APPRENTICE[/COLOR]' ) , O0O00Oo , 222 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 14 - 14: o0ii1I - o0o00Oo0O
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
    if 45 - 45: i1IiiiI1iI * Iii / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
    if 49 - 49: o0ii1I / IiI1i11I . IiI1i11I . IiI1i11I + Ii % Iii
    if 7 - 7: III1iiIii * i1iIi + OOooOOo
    if 22 - 22: IiI1i11I
    if 48 - 48: Ii1I . oOo0O0Ooo
    if 73 - 73: o0o00Oo0O . i1IiiiI1iI - ii % Iii % ooOoO0O00
    if 14 - 14: i1IiiiI1iI + o0ii1I * I1ii11iIi11i
    if 49 - 49: I1ii11iIi11i
    if 57 - 57: o0o00Oo0O * i1iIi - IiI1i11I - iI11I1II1I1I * IiI1i11I
 iIIiI1iiI = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 9 - 9: III1iiIii . Iii
 for IIII in iIIiI1iiI :
  iI1iiiIiii = oO0 + IIII + oOoOooOo0o0
  oO0ooOoO = O00O0oOO00O00 ( iI1iiiIiii )
  if oO0ooOoO != 'Failed' :
   oOOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0ooOoO )
   for O0O00Oo , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in oOOO :
    if IiiIi1IIII1i in OOoO . lower ( ) :
     iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - Source Pandoras[/COLOR]' , O0O00Oo , 222 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
     if 96 - 96: i1iIi % o0o00Oo0O
 iIIiI1iiI = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 51 - 51: oOo0O0Ooo - IiI1i11I / Ii1I . Ii1I + Ii1I
 if 87 - 87: IIiIiII11i . o0ii1I * oO0o
 for IIII in iIIiI1iiI :
  iI1iiiIiii = IiIi1 + IIII
  o0OOOOO0O = O00O0oOO00O00 ( iI1iiiIiii )
  if o0OOOOO0O != 'Failed' :
   I1I1IiIi1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( o0OOOOO0O )
   for OOoo0 , OOoO in I1I1IiIi1 :
    if IiiIi1IIII1i in OOoO . lower ( ) :
     ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( IiIi1 + IIII + OOoo0 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 74 - 74: I11i % OOooOOo . IiI1i11I % i1IiiiI1iI . o0o00Oo0O % IIiIiII11i
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: i1i1I1IIii1II - ii / OOooOOo
def O0OoO0ooOO0o ( ) :
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
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 if 96 - 96: Iii % OOooOOo * Ii1I
 if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . i1iIi
 oo00IiI1 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 oo00ooOoo = 'http://onlinemovies.tube/?s=' + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 iii1IIIiiiI = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 OoO00oo00 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 iiiI1i11Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 63 - 63: Ii % Ii1I % oOo0O0Ooo . III1iiIii * I11i + oooOo0oo0oo
 i1i1IIIIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 oo0o0oOo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 77 - 77: I11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 63 - 63: i1iIi * i1i1I1IIii1II + i1iIi * o0ii1I + I1ii11iIi11i / Ii1I
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
 if 65 - 65: i1IiiiI1iI + o0o00Oo0O % I11i
 i11II1I11I1 = O00O0oOO00O00 ( oo00IiI1 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( oo00ooOoo )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iii1IIIiiiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( OoO00oo00 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 o0OOOOO0O = O00O0oOO00O00 ( iiiI1i11Ii )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 72 - 72: oooOo0oo0oo . OOooOOo / IIiIiII11i
 if 69 - 69: oooOo0oo0oo * IIiIiII11i - i1iIi - ooOoO0O00 + Ii
 O0ooo0o0 = O00O0oOO00O00 ( i1i1IIIIIIIi )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 oO0ooOoO = O00O0oOO00O00 ( oo0o0oOo )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 50 - 50: ii * ooOoO0O00 / i1i1I1IIii1II
 if 83 - 83: ooOoO0O00
 if oO0ooOoO != 'Failed' :
  oOOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( oO0ooOoO )
  for O0O00Oo , OOoO in oOOO :
   iIi1I1 = O00O0oOO00O00 ( O0O00Oo )
   O0oOoo0OoO0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi1I1 )
   for oo00IiI1 , oOo00o00oO in O0oOoo0OoO0O :
    if O0ooOoO in oOo00o00oO . lower ( ) :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + oOo00o00oO + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + oo00IiI1 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 38 - 38: ii * iI11I1II1I1I
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if O0ooo0o0 != 'Failed' :
  iIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0ooo0o0 )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in iIi :
   if O0ooOoO in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source HeroVision[/COLOR]' ) , O0O00Oo , 1016 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 54 - 54: ii . i1IiiiI1iI
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 71 - 71: o0ii1I
    if 31 - 31: Iii . Ii . oO0o * I1ii11iIi11i % o0ii1I . I11i
    if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
    if 93 - 93: i1iIi % i1IiiiI1iI
    if 46 - 46: Ii1I * OOooOOo * III1iiIii * Ii1I . Ii1I
    if 43 - 43: i1iIi . ooOoO0O00
    if 68 - 68: III1iiIii % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
    if 45 - 45: oOo0O0Ooo
    if 17 - 17: ii - i1iIi + o0ii1I . ii % I1ii11iIi11i
    if 92 - 92: i1IiiiI1iI - oooOo0oo0oo % oO0o - I11i % ooOoO0O00
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  o0i1I11iI1iiI = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for O0O00Oo , iIiIi11 , OOoO , I1ii in i1Iii1i1I :
   if O0ooOoO in OOoO . lower ( ) :
    if 'season' in I1ii :
     iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' - [COLORred]Source - Tv HUB[/COLOR]' , O0O00Oo , 90054 , iIiIi11 , iIiIi11 , '' )
    if 'episodes' in I1ii :
     iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' - [COLORred]Source - Tv HUB[/COLOR]' , O0O00Oo , 90044 , iIiIi11 , iIiIi11 , '' )
  for O0O00Oo in o0i1I11iI1iiI :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , O0O00Oo , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 38 - 38: Ii1I . Iii / OOooOOo % Iii
   oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if i11II1I11I1 != 'Failed' :
  OOoO0ooOO = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( i11II1I11I1 )
  for O0O00Oo , OOoO , iIiIi11 in OOoO0ooOO :
   if O0ooOoO in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( OOoO ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , O0O00Oo , 8022 , iIiIi11 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / IiI1i11I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 61 - 61: I1ii11iIi11i - i1IiiiI1iI
    if 51 - 51: IiI1i11I * i1iIi / o0o00Oo0O / o0o00Oo0O
    if 52 - 52: ii % o0o00Oo0O
    if 56 - 56: i1i1I1IIii1II - ooOoO0O00 * ii - IIiIiII11i
    if 28 - 28: ooOoO0O00 / Iii . I11i
    if 11 - 11: I1ii11iIi11i * ii - Ii
    if 13 - 13: Ii . o0o00Oo0O / oooOo0oo0oo * ooOoO0O00
    if 14 - 14: III1iiIii + III1iiIii . Iii / o0ii1I . iI11I1II1I1I
    if 10 - 10: IIiIiII11i . oooOo0oo0oo / IiI1i11I
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for OOoO in IiIi1I1 :
   if O0ooOoO in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iii1IIIiiiI + OOoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 35 - 35: IiI1i11I / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for OOoO in I1i11 :
   if O0ooOoO in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( OoO00oo00 + OOoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 3 - 3: Ii1I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0OOOOO0O != 'Failed' :
  I1I1IiIi1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OOOOO0O )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in I1I1IiIi1 :
   if O0ooOoO in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] Source Scooby[/COLOR]' ) , O0O00Oo , 1016 , oo00O00oO000o , iIi1IiII , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 42 - 42: Iii % I1ii11iIi11i + III1iiIii - Iii . iI11I1II1I1I - o0ii1I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 27 - 27: IiI1i11I % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
 oOO0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for IIII in oOO0 :
  iI1iiiIiii = oO0 + IIII + oOoOooOo0o0
  Oo = O00O0oOO00O00 ( iI1iiiIiii )
  if Oo != 'Failed' :
   i111II = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( Oo )
   for OOoO , OOOiiiiI , O0O00Oo , iIiIi11 , oooOo0OOOoo0 , OooOo00o in i111II :
    if O0ooOoO in OOoO . lower ( ) :
     Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - Source Pandoras[/COLOR]' , O0O00Oo , OooOo00o , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 37 - 37: IiI1i11I + i1IiiiI1iI * o0ii1I + III1iiIii
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
     if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + o0ii1I / IIiIiII11i
     if 66 - 66: i1iIi + i1i1I1IIii1II % ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIiii ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O00Oo = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( IiiIi1IIII1i ) . replace ( ' ' , '+' )
 if 89 - 89: IIiIiII11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( O0O00Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 15 - 15: iI11I1II1I1I + IiI1i11I
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for O0O00Oo , OOoO in i1Iii1i1I :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + O0O00Oo ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 35 - 35: IIiIiII11i % oooOo0oo0oo . i1i1I1IIii1II * i1iIi
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
o0O00ooo0oO0o = '{ZH},' ; ii11OOoO = '{IX},' ; i11iIIII1II11Iii = '{LM},'
if 46 - 46: o0ii1I * o0ii1I / i1i1I1IIii1II * i1IiiiI1iI
def iI1I1I ( url ) :
 OoiII1I1 = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( OoiII1I1 )
 for url , I1 , i11IiI1iiI11 , OOoO in IIi :
  iiIIIiIi1IIi ( ( I1 ) . replace ( 'Sezon' , ' Season ' ) + ( i11IiI1iiI11 ) . replace ( 'Bölüm' , ' Episode ' ) + OOoO , url , 8063 , '' )
  if 94 - 94: o0o00Oo0O / o0ii1I + oOo0O0Ooo - Ii1I * IiI1i11I + ii
  if 86 - 86: i1iIi + iI11I1II1I1I
  if 37 - 37: IIiIiII11i * i1IiiiI1iI + i1iIi / oooOo0oo0oo * Ii1I
  if 25 - 25: IiI1i11I * oOo0O0Ooo / Iii / Ii1I . o0ii1I / ooOoO0O00
def OOo00ooOOo0ooO0 ( url ) :
 OoiII1I1 = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( OoiII1I1 )
 for url , OOoO in IIi :
  ii11i ( OOoO , url , 222 , '' )
  if 28 - 28: i1IiiiI1iI + IIiIiII11i % oooOo0oo0oo * Ii % i1i1I1IIii1II + ii
  if 65 - 65: I11i . III1iiIii % ooOoO0O00 % OOooOOo + Ii1I
  if 41 - 41: OOooOOo / iI11I1II1I1I
  if 92 - 92: o0ii1I . IiI1i11I % i1IiiiI1iI % o0o00Oo0O
def oOooo0ooo ( ) :
 if 32 - 32: iI11I1II1I1I * oOo0O0Ooo . oooOo0oo0oo * iI11I1II1I1I
 OoiII1I1 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OoiII1I1 )
 for O0O00Oo , iIiIi11 , OOoO , i11IiI1iiI11 in IIi :
  iiIIIiIi1IIi ( OOoO + '  -  ' + ( i11IiI1iiI11 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , O0O00Oo , 8063 , iIiIi11 )
  if 92 - 92: i1i1I1IIii1II - i1iIi . ii * i1i1I1IIii1II / I1ii11iIi11i
def I1Ii ( ) :
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , OOoO , iIiIi11 in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 8002 , iIiIi11 )
def OO00O0OoooO ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I11iiii )
 for iIiIi11 , time , url , OOoO , iII1IiiIIIIii in IIi :
  Iii1I1I11iiI1 ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , time ) , url , 1015 , iIiIi11 , iII1IiiIIIIii )
  if 78 - 78: ii % i1i1I1IIii1II - Ii
def i111iiII1I ( ) :
 if 10 - 10: i1iIi
 iiIIIiIi1IIi ( 'Coronation Street' , '' , 8001 , '' )
 iiIIIiIi1IIi ( 'Eastenders' , '' , 8002 , '' )
 iiIIIiIi1IIi ( 'Emmerdale' , '' , 8003 , '' )
 iiIIIiIi1IIi ( 'Hollyoaks' , '' , 8004 , '' )
 iiIIIiIi1IIi ( 'Im a Celebrity' , '' , 8005 , '' )
 if 5 - 5: o0ii1I - iI11I1II1I1I
 if 51 - 51: III1iiIii
 if 39 - 39: OOooOOo
 if 16 - 16: i1i1I1IIii1II
def O00O ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'Holly' in OOoO :
   iIiIi11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in O0O00Oo :
    ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 19 - 19: III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 67 - 67: Iii + III1iiIii / OOooOOo % o0ii1I / ooOoO0O00 . i1iIi
def I11Oo0O00O0O00 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'East' in OOoO :
   iIiIi11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in O0O00Oo :
    ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 18 - 18: I1ii11iIi11i + i1i1I1IIii1II % ooOoO0O00 * i1IiiiI1iI - III1iiIii / o0ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: i1i1I1IIii1II . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
def I1IiiIiIIi1Ii ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'Emmer' in OOoO :
   iIiIi11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in O0O00Oo :
    ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 83 - 83: o0o00Oo0O + o0ii1I % Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: i1IiiiI1iI % I1ii11iIi11i - Iii + o0o00Oo0O
def OOo0o0 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'Coro' in OOoO :
   iIiIi11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in O0O00Oo :
    ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 60 - 60: I11i / I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: iI11I1II1I1I . oO0o / ii
def Ii1ii1I1I ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'Celeb' in OOoO :
   iIiIi11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in O0O00Oo :
    ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 95 - 95: i1i1I1IIii1II - Ii1I + I11i
def iIiI1iI ( name , url ) :
 o00OOOO000000 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if o00OOOO000000 :
  i1iI1Iiiiii11 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I11iiii = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( I11iiii ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I11iiii = open_url ( url )
  iII1I1iIIIiII = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( I11iiii ) [ - 1 ]
  i1iI1Iiiiii11 = iII1I1iIIIiII . replace ( '\\/' , '/' )
 i111I11i = xbmcgui . ListItem ( name , '' , '' )
 i111I11i . setPath ( i1iI1Iiiiii11 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i111I11i )
 if 41 - 41: i1IiiiI1iI - o0o00Oo0O * I1ii11iIi11i % oOo0O0Ooo
 if 70 - 70: III1iiIii
def i1Ii11 ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , O0O00Oo , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for O0O00Oo , OOoO in i1Iii1i1I :
  iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , O0O00Oo , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 57 - 57: oO0o * i1i1I1IIii1II . iI11I1II1I1I - oooOo0oo0oo
def iI1iIiiIii ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  if 'Movies' in OOoO :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.snagfilms.com' + ( O0O00Oo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def O0OOOOO0O ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I11iiii )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iIiIi11 )
 for url in i1Iii1i1I :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 44 - 44: IIiIiII11i / i1IiiiI1iI
  if 93 - 93: IIiIiII11i / III1iiIii . I1ii11iIi11i - Ii1I * o0ii1I
def oO0OoO00o ( url ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url , iIiIi11 in IIi :
  if '{{' in OOoO :
   pass
  else :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iIiIi11 )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
IiIi11iI1IIi = '{UJ},' ; iII111I = '{WE},' ; Ooooo0Oo0oOo = '{WP},' ; IiI1III1 = '{PP},'
def iiiiII1i1Iii1I1 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url , iIiIi11 in IIi :
  if '{{' in OOoO :
   pass
  else :
   iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iIiIi11 )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoOO00OO0OoOoooOooOO0o ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  I1iooOOooO ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1iooOOooO ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: IiI1i11I % IiI1i11I + Ii % o0ii1I
 if 99 - 99: III1iiIii % IIiIiII11i - i1iIi % ii
 if 81 - 81: oooOo0oo0oo
def Iiooo000o0OoOo ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '(cooltvseries.com)' in OOoO :
   ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , OOoO in i1Iii1i1I :
  if '(cooltvseries.com)' in OOoO :
   ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def O0oo0OoooO0 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I11iiii )
 for url in IIi :
  o0oO0OoO0 ( ( url ) . replace ( ' ' , '%20' ) )
IiiI = '{XX},' ; III1i1iII1 = '{UD},' ; IiiiiI11iii11iI = '{YT},' ; I111iIii1i1 = '{JS},' ; I1i1I1i1I1 = '{PF},'
if 33 - 33: o0ii1I . i1i1I1IIii1II
def OOOo0OO0ooO0O0O ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , OOoO , iIiIi11 in IIi :
  ii11i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( O0O00Oo ) ) , 222 , iIiIi11 )
  if 76 - 76: I11i / Iii
def o0ooOooO ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I11iiii )
 for iIiIi11 , url , OOoO in IIi :
  if 'youtu' in url :
   ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iIiIi11 )
 for url in next :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 95 - 95: OOooOOo - o0o00Oo0O % ii
def iIo0O00o00o0 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 87 - 87: o0ii1I % Ii1I * I1ii11iIi11i
def OOO00i111 ( url ) :
 I11iiii = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iIiIi11 )
  if 25 - 25: Ii / iI11I1II1I1I * ii . oooOo0oo0oo
  if 69 - 69: I1ii11iIi11i * i1iIi
  if 91 - 91: I11i . i1iIi / oO0o / Ii * I11i
  if 52 - 52: oOo0O0Ooo - Ii / III1iiIii . i1i1I1IIii1II
  if 38 - 38: i1i1I1IIii1II + ii * OOooOOo % i1i1I1IIii1II
def oo0Oooo0O ( ) :
 if 80 - 80: I1ii11iIi11i
 iiIIIiIi1IIi ( 'All Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'Entertainment' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'Movies' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'Music' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'News' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'Sports' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'Documentary' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'Kids' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'Food' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'Religious' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'USA Channels' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 iiIIIiIi1IIi ( 'Other' , '' , 7021 , iiIi1IIiIi + 'livetv.png' )
 if 16 - 16: oOo0O0Ooo * IiI1i11I . iI11I1II1I1I
 if 66 - 66: ii * o0o00Oo0O / i1iIi * o0ii1I
def i11II ( Cat_Name ) :
 if 47 - 47: oO0o . Iii % i1iIi - I1ii11iIi11i . oOo0O0Ooo
 IIiiiI1ii = False
 Oo0o0o00Oo = '0'
 if Cat_Name == 'All Channels' : IIiiiI1ii = True
 if Cat_Name == 'Entertainment' : Oo0o0o00Oo = '1'
 if Cat_Name == 'Movies' : Oo0o0o00Oo = '2'
 if Cat_Name == 'Music' : Oo0o0o00Oo = '3'
 if Cat_Name == 'News' : Oo0o0o00Oo = '4'
 if Cat_Name == 'Sports' : Oo0o0o00Oo = '5'
 if Cat_Name == 'Documentary' : Oo0o0o00Oo = '6'
 if Cat_Name == 'Kids' : Oo0o0o00Oo = '7'
 if Cat_Name == 'Food' : Oo0o0o00Oo = '8'
 if Cat_Name == 'Religious' : Oo0o0o00Oo = '9'
 if Cat_Name == 'USA Channels' : Oo0o0o00Oo = '10'
 if Cat_Name == 'Other' : Oo0o0o00Oo = '11'
 if 67 - 67: I11i % I11i * i1iIi - Ii / iI11I1II1I1I % oOo0O0Ooo
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I11iiii )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for OOoO , iIiIi11 , ooo0o in IIi :
  o0OOO0O00Oo00 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iIiIi11 ) . replace ( '\\' , '' )
  if ooo0o == Oo0o0o00Oo :
   iiIIIiIi1IIi ( OOoO , '' , 7022 , o0OOO0O00Oo00 )
  elif IIiiiI1ii == True :
   iiIIIiIi1IIi ( OOoO , '' , 7022 , o0OOO0O00Oo00 )
  else : pass
  if 78 - 78: oO0o
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 13 - 13: i1i1I1IIii1II / Iii
def iiiII1i ( Search_Name ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I11iiii )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I11iiii )
 for iIiIi11 , O0O00Oo , oo00ooOoo , iii1IIIiiiI in IIi :
  o0OOO0O00Oo00 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iIiIi11 ) . replace ( '\\' , '' )
  ii11i ( Search_Name + ': Link 1' , ( O0O00Oo ) . replace ( '\\' , '' ) , 222 , o0OOO0O00Oo00 )
  ii11i ( Search_Name + ': Link 2' , ( oo00ooOoo ) . replace ( '\\' , '' ) , 222 , o0OOO0O00Oo00 )
  ii11i ( Search_Name + ': Link 3' , ( iii1IIIiiiI ) . replace ( '\\' , '' ) , 222 , o0OOO0O00Oo00 )
  if 74 - 74: Ii1I * III1iiIii * III1iiIii . IiI1i11I + i1i1I1IIii1II + i1iIi
def Ii1 ( ) :
 I11iiii = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  ii11i ( OOoO , ( O0O00Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def I1iiii11IiI1 ( ) :
 I11iiii = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  ii11i ( OOoO , ( O0O00Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def IiiIi ( ) :
 I11iiii = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  ii11i ( OOoO , ( O0O00Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 71 - 71: ii - IiI1i11I + o0ii1I / o0o00Oo0O % I11i + oO0o
def O0oO00O000o0O ( url ) :
 url
 iII1i11 = xbmcgui . ListItem ( OOoO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1i11 )
 return
 if 75 - 75: III1iiIii - i1IiiiI1iI * o0ii1I % ii
 if 46 - 46: i1iIi - iI11I1II1I1I
def o0ooOoOO0 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( I11iiii )
 for url , OOOiiiiI , iIiIi11 , OOoO in IIi :
  Iii1I1I11iiI1 ( OOoO , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + iIiIi11 , '' , ( OOOiiiiI ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  iiIIIiIi1IIi ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 35 - 35: Iii % o0o00Oo0O
def I1i1IIIIIII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOOiiiiI , iIiIi11 in IIi :
  iI1Ii1iI11iiI ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iIiIi11 , '' , OOOiiiiI )
  oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 OOO0ooO0Oo0 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi1III in OOO0ooO0Oo0 :
  IiI1iiiIii = ( IiIi1III ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  Iii1I1I11iiI1 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iIiIi11 , '' , IiI1iiiIii )
  if 41 - 41: iI11I1II1I1I - oO0o * III1iiIii
def OOo00oO0OOo ( INFO ) :
 oooO ( 'info for workout' , INFO )
 if 87 - 87: oOo0O0Ooo . i1i1I1IIii1II / III1iiIii - ii
 if 33 - 33: i1i1I1IIii1II % oO0o . iI11I1II1I1I / III1iiIii
 if 3 - 3: o0ii1I + oO0o
def OOoOOo0oOO ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIIIiIi1IIi ( ( OOoO ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def oOOoOoO0OOO0oO ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , url , 9032 , iiIi1IIiIi + 'icon.png' )
def Oo0oO ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url in IIi :
  if '=' in OOoO :
   pass
  else :
   ii11i ( ( OOoO ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def Oo00o ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  if '=' in OOoO :
   pass
  else :
   ii11i ( OOoO , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 14 - 14: IIiIiII11i + o0o00Oo0O - IiI1i11I
   if 18 - 18: I11i / Ii % Ii1I * ii
   if 67 - 67: OOooOOo
def OOO0 ( url ) :
 ii11i ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 ii11i ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , iiIi1IIiIi + 'bamf.png' )
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  if 'mp4' in url :
   pass
  else :
   ii11i ( ( OOoO ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oo00 ( url ) :
 ii11i ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 ii11i ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , iiIi1IIiIi + 'bamf.png' )
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  if 'mp4' in url :
   ii11i ( ( OOoO ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: ooOoO0O00
 if 68 - 68: oO0o % III1iiIii - i1i1I1IIii1II - i1iIi . I1ii11iIi11i
 if 30 - 30: ii % I11i + i1iIi * oO0o
def O0ooOOO ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  if 'Daily' in OOoO :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 9008 , O0O )
def iI1ii1i1iIi ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def II11Iiii1i1II ( url ) :
 ii11i ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 ii11i ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 ii11i ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  ii11i ( ( OOoO ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 48 - 48: ii + i1IiiiI1iI
def IiIII ( ) :
 I11iiii = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  if '.m3u' in O0O00Oo :
   iiIIIiIi1IIi ( ( OOoO ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + O0O00Oo ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def iII1iII ( url ) :
 I11iiii = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  ii11i ( ( OOoO ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 33 - 33: IiI1i11I
def I1IIIiIiIi ( ) :
 I11iiii = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  if 'category' in O0O00Oo :
   iiIIIiIi1IIi ( OOoO , 'http://www.disclose.tv/' + O0O00Oo , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 24 - 24: IiI1i11I . i1iIi
   if 29 - 29: ii / III1iiIii % Iii . oooOo0oo0oo + i1IiiiI1iI
def oO0OOOo0OO ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I11iiii )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I11iiii )
 for url , OOoO , iIiIi11 in IIi :
  iiIIIiIi1IIi ( OOoO , 'http://www.disclose.tv/' + url , 7011 , iIiIi11 )
 for url in next :
  iiIIIiIi1IIi ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 25 - 25: oooOo0oo0oo / ii - Ii1I
  if 31 - 31: Iii + oO0o / oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
def iiiiIiI1IIiI ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I11iiii )
 IiIi1I1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  if 'http' in url :
   ii11i ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , OOoO in i1Iii1i1I :
  ii11i ( OOoO , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in IiIi1I1 :
  ii11i ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 53 - 53: iI11I1II1I1I % OOooOOo % oOo0O0Ooo + Ii1I % ii
  if 29 - 29: oOo0O0Ooo / I11i + iI11I1II1I1I / o0o00Oo0O / oooOo0oo0oo % ooOoO0O00
def OOoOOo0o0OOo0 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 44 - 44: ii . oO0o
def i11I1IiIi ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1I1I = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIiiiIII1II = len ( i1I1I )
 if 98 - 98: Ii1I - oooOo0oo0oo % iI11I1II1I1I
 if 54 - 54: Ii1I + ooOoO0O00 - Iii * ii
 if iIiiiIII1II == 1 :
  for OO0ooo in i1I1I :
   OO0ooo = OO0ooo . replace ( 'player' , 'watch' )
   O0000 = OO0ooo + '&fv=&sou='
   o000o0OO = OooOoooOo ( O0000 )
   OooOO0O0000o = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( o000o0OO )
   for o00o00OoO00o0 in OooOO0O0000o :
    OOoooOo00000 = False
    Resolve ( o00o00OoO00o0 )
    if 21 - 21: I11i * I11i + o0o00Oo0O
 elif iIiiiIII1II > 1 :
  if 73 - 73: I11i / IiI1i11I % o0o00Oo0O . ooOoO0O00
  for OO0ooo in i1I1I :
   oo0O0o0O = OooOoooOo ( OO0ooo )
   O00OOOo0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oo0O0o0O )
   O0o0I1I111i1i1i = O00OOOo0
   O0o0I1I111i1i1i = ( str ( O0o0I1I111i1i1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + O0o0I1I111i1i1i
   ii11i ( 'DOUBLE LINK' , O0o0I1I111i1i1i , 424 , '' )
   if 25 - 25: i1iIi . III1iiIii - oOo0O0Ooo * i1i1I1IIii1II
   for url in O00OOOo0 :
    iiIIIiIi1IIi ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     oo00ooOoo = Google . resolve ( url )
    except :
     pass
    try :
     iiiI1111ii = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( oo00ooOoo ) )
     for oooO00OOO0 , IIIiiI1I in iiiI1111ii :
      if 55 - 55: IiI1i11I * I1ii11iIi11i + OOooOOo * oooOo0oo0oo / IiI1i11I * ooOoO0O00
      HD_URLS . append ( oooO00OOO0 )
      SD_URLS . append ( IIIiiI1I )
    except :
     pass
 else :
  pass
  if 49 - 49: III1iiIii + iI11I1II1I1I
def iiiIiII1II ( ) :
 if 77 - 77: i1IiiiI1iI . I11i / I1ii11iIi11i
 if 26 - 26: Iii
 iiIIIiIi1IIi ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 42 - 42: iI11I1II1I1I
 iiIIIiIi1IIi ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 100 - 100: i1i1I1IIii1II * I11i / IiI1i11I
 if 92 - 92: i1iIi / Ii * oooOo0oo0oo
def oooOO0OoO0OOO ( ) :
 I11iiii = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , 'http://cnfstudio.com/genre/' + O0O00Oo , 7003 , iiIi1IIiIi + 'icon.png' )
  if 60 - 60: Ii1I * Ii - IIiIiII11i + i1IiiiI1iI % III1iiIii
iIii1 = xbmcgui . Dialog ( )
if 63 - 63: ii . o0ii1I - i1i1I1IIii1II / IIiIiII11i + oOo0O0Ooo
o00O0oOO0o = '{UN},' ; O0000000oooOO = '{IG},' ; iI11iiI1 = '{PL},' ; I1Ioo000oooooooO = '{LO},' ; II1IIi1ii111 = '{LP},' ; II1OO = '{HA},' ; oo0OOO0O0 = '{XD},' ; OoooOooo = '{TA},' ; IiIi1iiII = '{DP},' ; ooO0o0o = '{JT},' ; Ii1IiIi1IiI = '{JJ},' ; ooOOO = '{MM},' ; ooOooOOoO0O = '{FQ},' ; i1I111ii11Iii = '{HH},'
if 25 - 25: i1iIi
def O00oo ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I11iiii )
 ooO0o0 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I11iiii )
 for iIiIi11 , url , OOoO in IIi :
  ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iIiIi11 )
 ooO0o0 = ooO0o0
 for url in ooO0o0 :
  iiIIIiIi1IIi ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 94 - 94: oOo0O0Ooo - o0ii1I % ii + ooOoO0O00 - ii
def o0Oi1i1i11IIii ( url ) :
 if 11 - 11: i1iIi . i1IiiiI1iI - IiI1i11I . I11i
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  IIIIII1iI11IiIi1II = OooooO0000 ( iiI111I1iIiI )
  o0ooooOOo = OooooO0000 ( url )
  if 95 - 95: ii
  if 23 - 23: IIiIiII11i + Iii / o0o00Oo0O . Iii . i1IiiiI1iI + iI11I1II1I1I
def OooooO0000 ( url ) :
 if 2 - 2: ooOoO0O00 . o0o00Oo0O / I11i . IIiIiII11i / oO0o % ooOoO0O00
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  OooOo ( url )
  if 12 - 12: I11i
  if 58 - 58: iI11I1II1I1I * o0ii1I . i1iIi . I1ii11iIi11i * o0ii1I
def OO0O000OOO0 ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 31 - 31: i1IiiiI1iI * I11i * IIiIiII11i + o0o00Oo0O / IiI1i11I * i1iIi
def Ooo0o0o ( ) :
 if os . path . exists ( II ) :
  OoO00o = open ( II , 'r' )
  for iII1i11 in OoO00o :
   o0oOo = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iII1i11 )
   for OOoO , O0O00Oo in o0oOo :
    ii11i ( OOoO , O0O00Oo , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 24 - 24: oOo0O0Ooo . i1i1I1IIii1II * IIiIiII11i
def OOoooo0000Oo ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = O00Oo0o000oO ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OOoO , url in IIi :
   url = ( url ) . strip ( )
   ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 51 - 51: I11i - o0ii1I - iI11I1II1I1I * iI11I1II1I1I * I11i - o0o00Oo0O
  if 27 - 27: ooOoO0O00 . i1IiiiI1iI
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo in IIi :
  O0O00Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + O0O00Oo
 OOoO = 'plugin.video.GenieTv'
 if 64 - 64: i1iIi / ooOoO0O00
 ooo00 ( O0O00Oo , OOoO )
 if 56 - 56: oooOo0oo0oo - i1IiiiI1iI
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo in IIi :
  O0O00Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + O0O00Oo
 OOoO = 'repository.GenieTv'
 if 63 - 63: oOo0O0Ooo * oooOo0oo0oo . iI11I1II1I1I * OOooOOo . ii
 ooo00 ( O0O00Oo , OOoO )
 if 6 - 6: o0o00Oo0O . I11i - OOooOOo
 if 3 - 3: ii % iI11I1II1I1I * i1IiiiI1iI % I1ii11iIi11i + iI11I1II1I1I
def O0O0Oooo0o ( ) :
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  oOOO0o00 ( )
 if o0Oo00 == 1 :
  O00ooi1i1iIiiI1Ii1 ( )
  if 50 - 50: ooOoO0O00
  if 56 - 56: oO0o + i1IiiiI1iI / o0ii1I
  if 75 - 75: OOooOOo
  if 96 - 96: I11i * Iii * I1ii11iIi11i
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
Iii11I = 'https://addons.tvaddons.ag/'
if 45 - 45: oO0o * IIiIiII11i * OOooOOo - oooOo0oo0oo % i1i1I1IIii1II - I1ii11iIi11i
def O00ooi1i1iIiiI1Ii1 ( ) :
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 iI1i1 = 'https://addons.tvaddons.ag/search/?keyword=' + O0ooOoO
 II11iIiIIIiI = OooOoooOo ( iI1i1 )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , IiI11i1IIiiI , OOoO in IIi :
  Iii1I1I11iiI1 ( OOoO , O0O00Oo , 10054 , 'https://addons.tvaddons.ag/' + IiI11i1IIiiI , Oo00OOOOO , '' )
  if 4 - 4: I11i . OOooOOo - iI11I1II1I1I / III1iiIii / oOo0O0Ooo % oOo0O0Ooo
  if 42 - 42: ii + o0o00Oo0O . oO0o % Iii / I1ii11iIi11i
def oOOO0o00 ( ) :
 II11iIiIIIiI = OooOoooOo ( Iii11I )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  if 'Repositories' in OOoO :
   pass
  elif 'Services' in OOoO :
   pass
  elif 'International' in OOoO :
   pass
  else :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 10053 , 'https://addons.tvaddons.ag/' + iIiIi11 , Oo00OOOOO , '' )
   if 36 - 36: i1iIi / IIiIiII11i - IiI1i11I / o0ii1I
   if 11 - 11: ii + I11i - Ii + ooOoO0O00 % ooOoO0O00
def Addon ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIIIiI11I11 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOoO in IIi :
  if 'Please' in OOoO :
   pass
  else :
   iI1Ii1iI11iiI ( OOoO , url , 10054 , 'https://addons.tvaddons.ag/' + iIiIi11 , Oo00OOOOO , '' )
 for url in IIIIiI11I11 :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
  if 68 - 68: III1iiIii - Iii % IIiIiII11i - I11i % i1iIi
  if 41 - 41: IiI1i11I . i1iIi % ii / oOo0O0Ooo * IIiIiII11i - IiI1i11I
def IIiO0 ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   ooI1111i = os . path . join ( OO0OoOO0o0o , name + '.zip' )
   try :
    os . remove ( ooI1111i )
   except :
    pass
   downloader . download ( url , ooI1111i , o0oOoO00o )
   iIIii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print iIIii
   print '======================================='
   extract . all ( ooI1111i , iIIii , o0oOoO00o )
   ii1iii1i ( )
   if 50 - 50: Iii
def ooo00 ( url , name ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , name + '.zip' )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( url , ooI1111i , o0oOoO00o )
 iIIii = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print iIIii
 print '======================================='
 extract . all ( ooI1111i , iIIii , o0oOoO00o )
 ii1iii1i ( )
 if 88 - 88: ooOoO0O00 * oooOo0oo0oo . iI11I1II1I1I
def ii1iii1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 45 - 45: i1IiiiI1iI - o0o00Oo0O . i1IiiiI1iI / i1IiiiI1iI / OOooOOo
 if 12 - 12: oooOo0oo0oo
def OOO0oOO ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , IiI11i1IIiiI , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , url , 1007 , IiI11i1IIiiI )
def O0O0oOoO0O0oO ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , IiI11i1IIiiI , OOoO in IIi :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 1006 , IiI11i1IIiiI )
  if 1 - 1: ooOoO0O00
def i1i1I11I ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , oo00O00oO000o , OOOiiiiI , oooOo0OOOoo0 , OOoO in IIi :
  i11I1ii ( OOoO , 100109 , O0O00Oo , image = oo00O00oO000o , isFolder = True )
  if 70 - 70: i1i1I1IIii1II
def o00O0oOooOoO ( url ) :
 import random
 Ii1I11II1IiI = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 Ii1I11II1IiI . clear ( )
 oo00o0Oo0O0 = [ ]
 OOo00ii11I11ii1 = [ ]
 IiIiI1I1IIIi1 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oo00ooOoo , oo00O00oO000o , OOOiiiiI , oooOo0OOOoo0 , OOoO in IIi :
  oo00o0Oo0O0 . append ( [ oo00ooOoo , OOoO ] )
  if len ( oo00o0Oo0O0 ) == len ( IIi ) :
   for iII1i11 in oo00o0Oo0O0 :
    OOo0oO00O00 = random . randint ( 1 , len ( oo00o0Oo0O0 ) )
    try :
     I1I1Ii1Iii = oo00o0Oo0O0 [ int ( OOo0oO00O00 ) ]
    except :
     pass
    if len ( OOo00ii11I11ii1 ) <= 20 :
     if I1I1Ii1Iii [ 1 ] not in IiIiI1I1IIIi1 :
      o0o = OooOoooOo ( I1I1Ii1Iii [ 0 ] )
      IiIi1I1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for O00oooOoO , IIi1i111 in IiIi1I1 :
       OOoOoo = OooOoooOo ( O00oooOoO )
       I1i11 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for Ii1oo0O0OO , iiI111I1iIiI in I1i11 :
        if 'panda' in iiI111I1iIiI :
         iIIi1iI1I1IIi = OooOoooOo ( iiI111I1iIiI )
         iii1IIII1iii11I = re . compile ( "url: '(.+?)'" ) . findall ( iIIi1iI1I1IIi )
         for oO00 in iii1IIII1iii11I :
          if 'http' in oO00 :
           i111I11i = xbmcgui . ListItem ( I1I1Ii1Iii [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : I1I1Ii1Iii [ 1 ] } )
           i111I11i . setProperty ( "IsPlayable" , "true" )
           Ii1I11II1IiI . add ( oO00 , i111I11i )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i111I11i )
           if 12 - 12: oO0o . IiI1i11I + Ii1I . o0ii1I
def i11I1ii ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 I11I1 = sys . argv [ 0 ]
 I11I1 += '?mode=' + str ( mode )
 I11I1 += '&title=' + urllib . quote_plus ( name )
 I11I1 += '&image=' + urllib . quote_plus ( image )
 I11I1 += '&page=' + str ( page )
 if url != '' :
  I11I1 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  I11I1 += '&keyword=' + urllib . quote_plus ( keyword )
 i111I11i = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  i111I11i . addContextMenuItems ( contextMenu )
 if infoLabels :
  i111I11i . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  i111I11i . setProperty ( "IsPlayable" , "true" )
 i111I11i . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = isFolder )
 if 50 - 50: I1ii11iIi11i
 if 16 - 16: o0ii1I - OOooOOo % I1ii11iIi11i / o0ii1I . Iii + i1iIi
def i1i1I111iIi1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , iconimage , OOOiiiiI , oooOo0OOOoo0 , name in IIi :
  if 'http' in url :
   if '.php' in url :
    ii1i1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for iII1i11 in ii1i1i :
     if iII1i11 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    OOoo0OoO ( name , url , 1016 , iconimage , oooOo0OOOoo0 , OOOiiiiI )
   else :
    if 'youtube' in url :
     ii1i1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in ii1i1i :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IiIi ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , oooOo0OOOoo0 , OOOiiiiI )
    else :
     ii1i1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in ii1i1i :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IiIi ( name , url , 222 , iconimage , oooOo0OOOoo0 , OOOiiiiI )
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
  else :
   ooOOoo0 ( url , iconimage , name )
   if 47 - 47: o0ii1I % i1iIi + o0ii1I
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
  for url , IiI11i1IIiiI , name in IIi :
   if 'http' in url :
    if '.php' in url :
     iiIIIiIi1IIi ( name , url , 1016 , IiI11i1IIiiI )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      ii11i ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IiI11i1IIiiI )
     else :
      ii1i1i = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in ii1i1i :
       if iII1i11 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      ii11i ( name , url , 222 , IiI11i1IIiiI )
      oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
   else :
    ooOOoo0 ( url , IiI11i1IIiiI , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 49 - 49: OOooOOo / ooOoO0O00 / ii . IiI1i11I + IiI1i11I
def ooOOoo0 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 oooOo0O = ( url ) . replace ( ii11OOoO , 'http' ) . replace ( III1i1iII1 , '.com' ) ;
 OoOooOooOOoO = ( oooOo0O ) . replace ( i11iIIII1II11Iii , 'a' ) . replace ( ooO0OOoOoOO00 , 'b' ) . replace ( o0O00 , 'c' ) . replace ( iII111I , 'd' ) . replace ( iI11iiI1 , 'e' ) . replace ( ooO0o0o , 'f' ) ;
 II11iIi = ( OoOooOooOOoO ) . replace ( IiiI , 'g' ) . replace ( II1OO , 'h' ) . replace ( IiiiiI11iii11iI , 'i' ) . replace ( I1i1I1i1I1 , 'j' ) . replace ( ii1IiI111II , 'k' ) . replace ( iI11IiiI1i , 'l' ) ;
 OOO0oo0OO0o0 = ( II11iIi ) . replace ( OOoO0 , 'm' ) . replace ( o00o0Ooo , 'n' ) . replace ( II1I1 , 'o' ) . replace ( iIi1i , 'p' ) . replace ( OooIiii1ii , 'q' ) . replace ( OOOO0oo0o0O , 'r' ) ;
 IIiiiI = ( OOO0oo0OO0o0 ) . replace ( ooooO0OOo0o0 , 's' ) . replace ( Ooooo0Oo0oOo , 't' ) . replace ( IIo000o0O0000o , 'u' ) . replace ( ii1Iii1iiI11 , 'v' ) . replace ( i11ii1II , 'w' ) . replace ( ooOo00OOo0 , 'x' ) ;
 ii1IIi = ( IIiiiI ) . replace ( iii1Ii , 'y' ) . replace ( O0Oo0Oo000 , 'z' ) . replace ( o00O0oOO0o , '.' ) . replace ( O0000000oooOO , '(' ) . replace ( I1Ioo000oooooooO , ')' ) . replace ( II1IIi1ii111 , '/' ) ;
 ooo0Oo00000oooO = ( ii1IIi ) . replace ( o0O00ooo0oO0o , '1' ) . replace ( IiI1III1 , '2' ) . replace ( iIiiiiIi111I , '3' ) . replace ( OoooOooo , '4' ) . replace ( IiIi1iiII , '5' ) . replace ( I111iIii1i1 , '6' ) ;
 ooOo00oOOOO0 = ( ooo0Oo00000oooO ) . replace ( Ii1IiIi1IiI , '7' ) . replace ( ooOOO , '8' ) . replace ( ooOooOOoO0O , '9' ) . replace ( i1I111ii11Iii , '0' ) . replace ( o0oI1 , ':' ) . replace ( i1IO0OOoooO , '%' ) ;
 url = ( ooOo00oOOOO0 ) . replace ( IiIi11iI1IIi , '-' ) . replace ( oo0OOO0O0 , '_' ) ;
 ii11i ( name , url , 222 , iconimage ) ;
 if 21 - 21: ii % ii
 if 85 - 85: oO0o . I11i . oOo0O0Ooo
def Oo000o0o0 ( ) :
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for O0O00Oo , IiI11i1IIiiI , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , O0O00Oo , 1007 , IiI11i1IIiiI )
def oOO0ooOoOoOo ( url ) :
 if 91 - 91: III1iiIii - Ii1I - i1IiiiI1iI
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , IiI11i1IIiiI , OOoO in IIi :
  iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 1006 , IiI11i1IIiiI )
  if 35 - 35: iI11I1II1I1I . o0o00Oo0O + OOooOOo / oO0o / III1iiIii * IIiIiII11i
def I1ii111I ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OOOiII1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OOOiII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOiII1 )
 if 45 - 45: Ii1I . Iii . IIiIiII11i - IIiIiII11i * ii
 if 71 - 71: oooOo0oo0oo
def OOOOoO0 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  if '-dir-' in OOoO :
   iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , iIiIi11 )
  else :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 1006 , iIiIi11 )
   if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
def iII1IiI1I11i ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 Ii1i11I11i = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '[To Parent Directory]' in OOoO :
   OOoO = 'HOME'
   pass
  elif 'HOME' in OOoO :
   pass
  elif '.m3u' in OOoO :
   iiIIIiIi1IIi ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , Ii1i11I11i + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in OOoO :
   ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , Ii1i11I11i + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in OOoO :
   ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , Ii1i11I11i + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) , Ii1i11I11i + url , 1012 , iiIi1IIiIi + 'music.png' )
def oO0oooo ( url ) :
 II11iIiIIIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , url in IIi :
  ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 59 - 59: I1ii11iIi11i + o0o00Oo0O - Iii + oooOo0oo0oo
def oOO00O0O0oO0 ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 Ii1i11I11i = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '.mp3' in OOoO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '/' , '' ) , Ii1i11I11i + url , 1011 , iiIi1IIiIi + 'music.png' )
def IIiiii111iI ( ) :
 I11iiii = O00Oo0o000oO ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , ( 'http://www.cyn.net/music/' + O0O00Oo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iIiIi11 ) . replace ( ' ' , '%20' ) )
def iI1III11IIi11Ii11 ( url , img ) :
 I11iiii = O00Oo0o000oO ( url )
 oo00ooOoo = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( oo00ooOoo + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 25 - 25: Ii1I / Ii1I
def O0OoOo ( url ) :
 I11iiii = O00Oo0o000oO ( url )
 oo00ooOoo = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 for type , url , OOoO in IIi :
  if '[VID]' in type :
   ii11i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , oo00ooOoo + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   O0OoOo ( oo00ooOoo + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: I1ii11iIi11i - oO0o % I1ii11iIi11i . IIiIiII11i
 if 84 - 84: i1iIi * ii + o0o00Oo0O
def IiiIiIIi1 ( ) :
 IiIi1 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IiiIi1IIII1i = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0ooOoO = IiiIi1IIII1i . lower ( )
 O0O00Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 oo00IiI1 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 oo00ooOoo = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 84 - 84: ooOoO0O00 . Iii . ooOoO0O00 . I1ii11iIi11i
 II11iIiIIIiI = O00O0oOO00O00 ( O0O00Oo )
 i11II1I11I1 = O00O0oOO00O00 ( oo00IiI1 )
 o0o = O00O0oOO00O00 ( oo00ooOoo )
 if 21 - 21: IIiIiII11i . o0o00Oo0O + I1ii11iIi11i - Ii
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iIi1IiII , OOoO in IIi :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , O0O00Oo , 1016 , oo00O00oO000o , oooOo0OOOoo0 , OOOiiiiI )
    if 5 - 5: iI11I1II1I1I * Ii + oO0o + Iii * o0o00Oo0O % i1iIi
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if i11II1I11I1 != 'Failed' :
  OOoO0ooOO = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i11II1I11I1 )
  for O0O00Oo , OOoO in OOoO0ooOO :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + O0O00Oo ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 88 - 88: I11i / Ii * Ii1I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for O0O00Oo , OOoO in i1Iii1i1I :
   if IiiIi1IIII1i in OOoO . lower ( ) :
    iiIIIiIi1IIi ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + O0O00Oo ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 23 - 23: o0o00Oo0O / IiI1i11I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 66 - 66: ooOoO0O00 % ii * Ii + i1i1I1IIii1II * o0o00Oo0O / oO0o
    if 14 - 14: oOo0O0Ooo . III1iiIii
    if 29 - 29: ii / III1iiIii + OOooOOo - i1IiiiI1iI + III1iiIii . ooOoO0O00
    if 26 - 26: Ii - IIiIiII11i
    if 43 - 43: oOo0O0Ooo
    if 35 - 35: i1iIi + OOooOOo * ii - IIiIiII11i
OOoO0 = '{SF},' ; o00o0Ooo = '{IF},' ; II1I1 = '{PW},' ; iIiiiiIi111I = '{AM},' ; iIi1i = '{GF},' ; OooIiii1ii = '{DD},' ; OOOO0oo0o0O = '{UO},' ; ooooO0OOo0o0 = '{LE},' ; IIo000o0O0000o = '{ZY},' ; ii1Iii1iiI11 = '{UE},' ; i11ii1II = '{PE},' ; ooOo00OOo0 = '{JE},' ; iii1Ii = '{TH},' ; O0Oo0Oo000 = '{LK},'
if 19 - 19: ooOoO0O00 / o0ii1I / OOooOOo . oOo0O0Ooo / o0ii1I % I11i
if 39 - 39: i1iIi - ii
def o00oOoOo0 ( ) :
 I11iiii = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , O0O00Oo , 8021 , iiIi1IIiIi + 'iwatch.png' )
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
def Oo0oOo ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I11iiii )
 for url , OOoO , ii11Ii1IiiI1 in IIi :
  iiIIIiIi1IIi ( OOoO + ii11Ii1IiiI1 , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def o0oO0oOO ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I11iiii )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  I1iIiiI ( url )
def I1iIiiI ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I11iiii )
 IiIi1I1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I11iiii )
 I1i11 = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  ii11i ( 'VidSpot - ' + OOoO , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  ii11i ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , OOoO in I1i11 :
  ii11i ( 'VidUp' + OOoO , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for OOoO , url in IiIi1I1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   ii11i ( 'TheVideo - ' + OOoO , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 2 - 2: ooOoO0O00 - IIiIiII11i - oOo0O0Ooo + i1i1I1IIii1II * Iii
def iIiIIIIII11iI ( ) :
 I11iiii = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , O0O00Oo , 1021 , iiIi1IIiIi + 'anime.png' )
  if 47 - 47: ooOoO0O00 + IiI1i11I - o0o00Oo0O * III1iiIii - o0o00Oo0O
  if 38 - 38: Ii - OOooOOo . ii * IiI1i11I
def I1I1Ii ( ) :
 I11iiii = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , O0O00Oo , 1002 , iiIi1IIiIi + 'anime.png' )
  if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
  if 27 - 27: ooOoO0O00 - i1i1I1IIii1II + oooOo0oo0oo
  if 3 - 3: III1iiIii % i1IiiiI1iI . ii
def i1I1I1IIIi11 ( url ) :
 I11iiii = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I11iiii )
 for iIiIi11 in i1Iii1i1I :
  Oo0O0o00o00 = iIiIi11
 IiIi1I1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I11iiii )
 for url in IiIi1I1 :
  iiIIIiIi1IIi ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIIIiIi1IIi ( OOoO , url , 1003 , Oo0O0o00o00 )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOo000 ( url , IMAGE ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  print OOoO + '     ' + url
  if 'easy' in url :
   OO0o0oo ( url )
  elif 'playpanda' in url :
   OO0o0oo ( url )
   if 68 - 68: IiI1i11I . oooOo0oo0oo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OO0o0oo ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I11iiii )
 for url in IIi :
  ii11i ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 6 - 6: o0ii1I - I11i % Iii + Ii
  if 40 - 40: o0o00Oo0O . o0ii1I
def Ooo0O0OO0OOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 12 - 12: Iii
def O00Oo0o000oO ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 97 - 97: ooOoO0O00 % Iii . I11i * oOo0O0Ooo % IIiIiII11i
def i1O0o00o0Oo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iI1I1oOOo = ( '%s%s' % ( iiII , url ) )
 iiI111I1iIiI = O00Oo0o000oO ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , IiI11i1IIiiI , OOoO in IIi :
  ii11i ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , IiI11i1IIiiI )
  if 29 - 29: oO0o - I1ii11iIi11i . i1i1I1IIii1II / oO0o % Ii
def I1iO0000 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  O0iiI1iii1I111 ( url , OOoO )
 else :
  OooO0OO ( url )
def OooO0OO ( url ) :
 import urlresolver
 try :
  I11I1o0 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( I11I1o0 , xbmcgui . ListItem ( OOoO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( OOoO ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def OooOo ( url ) :
 if 78 - 78: o0o00Oo0O
 II11iIII1i1I = open ( OOOO0OOoO0O0 , "a" )
 II11iIII1i1I . write ( 'url="' + url + '"\n' )
 II11iIII1i1I . close
 if 60 - 60: i1i1I1IIii1II
 II1 = xbmc . Player ( iiIIIiIii ( ) )
 import urlresolver
 try : II1 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( OOoO ) )
 II1 = xbmc . Player ( iiIIIiIii ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : II1 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def O0iiI1iii1I111 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  OOooo00oo = '.mp4'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   IIIIOo ( url , name , OOooo00oo )
 elif '.mkv' in url :
  OOooo00oo = '.mkv'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   IIIIOo ( url , name , OOooo00oo )
 elif '.mp3' in url :
  OOooo00oo = '.mp3'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   IIIIOo ( url , name , OOooo00oo )
 elif '.avi' in url :
  OOooo00oo = '.avi'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   IIIIOo ( url , name , OOooo00oo )
 elif '.mov' in url :
  OOooo00oo = '.mov'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   IIIIOo ( url , name , OOooo00oo )
 elif '.mpeg' in url :
  OOooo00oo = '.mpeg'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   IIIIOo ( url , name , OOooo00oo )
 elif '.mpg' in url :
  OOooo00oo = '.mpg'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   IIIIOo ( url , name , OOooo00oo )
 elif '.flv' in url :
  OOooo00oo = '.flv'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   IIIIOo ( url , name , OOooo00oo )
 elif '.wmv' in url :
  OOooo00oo = '.wmv'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   IIIIOo ( url , name , OOooo00oo )
 else :
  OooO0OO ( url )
def IIIIOo ( url , name , cat ) :
 iII111i1IiiII ( )
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( OooO0 ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , file )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( url , ooI1111i , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def iII111i1IiiII ( ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def IIiiIIIiI ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % OOoO )
 xbmc . sleep ( 1 )
 II1 = xbmc . Player ( iiIIIiIii ( ) )
 o0oOoO00o . update ( 100 , '%s' % OOoO )
 xbmc . sleep ( 1 )
 II1 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 90 - 90: OOooOOo / Ii + iI11I1II1I1I . i1i1I1IIii1II . i1i1I1IIii1II + IiI1i11I
def o0oO0OoO0 ( url ) :
 II1 = xbmc . Player ( iiIIIiIii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : II1 . play ( url ) . strip ( )
 except : pass
 if 100 - 100: III1iiIii % ooOoO0O00 / IiI1i11I
def III1Iii1i ( url ) :
 II1 = xbmc . Player ( iiIIIiIii ( ) )
 import urlresolver
 OOOOo = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 II1 . play ( OOOOo )
 xbmc . sleep ( 1 )
 II1 . play ( url )
 if 10 - 10: OOooOOo * ii / Ii1I * IiI1i11I + ooOoO0O00 % I1ii11iIi11i
 if 77 - 77: i1IiiiI1iI
def iiIIIiIii ( ) :
 try :
  i11iIIiIII111 = getSet ( "core-player" )
  if ( i11iIIiIII111 == 'DVDPLAYER' ) : O0OoO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( i11iIIiIII111 == 'MPLAYER' ) : O0OoO = xbmc . PLAYER_CORE_MPLAYER
  elif ( i11iIIiIII111 == 'PAPLAYER' ) : O0OoO = xbmc . PLAYER_CORE_PAPLAYER
  else : O0OoO = xbmc . PLAYER_CORE_AUTO
 except : O0OoO = xbmc . PLAYER_CORE_AUTO
 return O0OoO
 return True
 if 72 - 72: I11i + Iii / oO0o
def iiIIIiIi1IIi ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii1OoOO = [ ]
  ii1OoOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1OoOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   ii1OoOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111I11i . addContextMenuItems ( ii1OoOO )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = True )
 return iiI1i1Iii111
 if 100 - 100: Ii / OOooOOo + i1iIi % Ii1I + Ii1I . Ii1I
def iIi11I11 ( name , url , mode , iconimage , fanart , description ) :
 if 49 - 49: i1IiiiI1iI * o0o00Oo0O . i1i1I1IIii1II / ii + i1i1I1IIii1II + Ii
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111I11i . setProperty ( "Fanart_Image" , fanart )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = True )
 return iiI1i1Iii111
 if 42 - 42: OOooOOo
def ii11i ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ii1OoOO = [ ]
  ii1OoOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ii1OoOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   ii1OoOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111I11i . addContextMenuItems ( ii1OoOO )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = False )
 return iiI1i1Iii111
 if 94 - 94: III1iiIii / i1iIi + i1IiiiI1iI * oooOo0oo0oo
 if 16 - 16: i1iIi - ooOoO0O00 - Iii % I1ii11iIi11i * Iii - OOooOOo
 if 19 - 19: oOo0O0Ooo + I11i / i1IiiiI1iI . III1iiIii % o0o00Oo0O % ooOoO0O00
 if 53 - 53: o0o00Oo0O % i1iIi
 if 41 - 41: III1iiIii
 if 29 - 29: i1iIi
def OO0II111Iiii1 ( url , heading , announce ) :
 class iIiIII1Ii ( ) :
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
   try : IiII111i1i11 = open ( announce ) ; ooO00Oo = IiII111i1i11 . read ( )
   except : ooO00Oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( ooO00Oo ) )
   return
 iIiIII1Ii ( )
 iIiIII1Ii ( )
def oooO ( heading , announce ) :
 class iIiIII1Ii ( ) :
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
   try : IiII111i1i11 = open ( announce ) ; ooO00Oo = IiII111i1i11 . read ( )
   except : ooO00Oo = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( ooO00Oo ) )
   return
 iIiIII1Ii ( )
 iIiIII1Ii ( )
def oooooo0O000o ( ) :
 OO0II111Iiii1 ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 79 - 79: i1IiiiI1iI . i1iIi / o0o00Oo0O - oOo0O0Ooo / Ii1I / OOooOOo
 if 43 - 43: i1i1I1IIii1II % i1IiiiI1iI / i1IiiiI1iI + Ii1I
 if 98 - 98: i1iIi * i1iIi . I11i + o0o00Oo0O * oooOo0oo0oo
 if 25 - 25: oO0o + I11i . i1iIi - o0ii1I . i1i1I1IIii1II * o0ii1I
 if 85 - 85: ooOoO0O00
def ii1iii1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 94 - 94: ii . o0o00Oo0O / ii
 if 67 - 67: Ii + OOooOOo
 if 50 - 50: i1iIi . ooOoO0O00 + Ii1I . oooOo0oo0oo
 if 97 - 97: oOo0O0Ooo
 if 63 - 63: o0o00Oo0O - OOooOOo / Ii / ii / i1iIi / IIiIiII11i
 if 45 - 45: IIiIiII11i . oO0o + oO0o * iI11I1II1I1I
 if 23 - 23: III1iiIii * OOooOOo % o0ii1I / o0ii1I - i1iIi - oooOo0oo0oo
 if 86 - 86: oooOo0oo0oo . ii * oOo0O0Ooo - I1ii11iIi11i / Ii * IiI1i11I
 if 56 - 56: oOo0O0Ooo . Iii % IiI1i11I
 if 33 - 33: Iii / oooOo0oo0oo - oooOo0oo0oo / Ii * OOooOOo + o0o00Oo0O
 if 2 - 2: Ii % oOo0O0Ooo
 if 90 - 90: IIiIiII11i
 if 2 - 2: o0ii1I - ii - Ii % I1ii11iIi11i / o0ii1I
 if 77 - 77: I11i . I11i * i1IiiiI1iI + oooOo0oo0oo - Ii
 if 45 - 45: oOo0O0Ooo . oOo0O0Ooo - I1ii11iIi11i * oooOo0oo0oo
 if 71 - 71: ooOoO0O00 / Iii
 if 14 - 14: ii
 if 99 - 99: I11i * I11i
 if 6 - 6: Ii + i1i1I1IIii1II % i1iIi + Ii - oooOo0oo0oo
 if 12 - 12: IiI1i11I . i1i1I1IIii1II % III1iiIii * ii . III1iiIii
 if 15 - 15: oOo0O0Ooo . oOo0O0Ooo / Ii
 if 17 - 17: iI11I1II1I1I / oO0o - IIiIiII11i
 if 46 - 46: iI11I1II1I1I * i1i1I1IIii1II / Ii + IIiIiII11i + Iii
 if 30 - 30: o0o00Oo0O * III1iiIii - i1IiiiI1iI % o0o00Oo0O * o0ii1I
def II1II111iIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OO0oO0ooOOOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 41 - 41: I1ii11iIi11i % Ii
def iiOOo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1IO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 64 - 64: iI11I1II1I1I
def o0OOOOooOo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iIi1I1Iii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 99 - 99: oOo0O0Ooo . i1iIi % IIiIiII11i / oOo0O0Ooo
def oOOOo000 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iI1iIIiIi1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 85 - 85: oO0o + IIiIiII11i
def o0oo0oO ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 64 - 64: OOooOOo
def iIiiii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + ii111Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 82 - 82: OOooOOo * Iii . i1IiiiI1iI . i1i1I1IIii1II . I11i
def o00Ooo0OooOo0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I1i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 74 - 74: Ii / Ii1I - i1i1I1IIii1II . oO0o
def i1II1iI1ii1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o000OOOooOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 94 - 94: Iii
def OoI1iIi ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 53 - 53: oooOo0oo0oo . oOo0O0Ooo / IiI1i11I . iI11I1II1I1I % i1IiiiI1iI + oO0o
def oOOoo00O00o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Ii1ii111i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , o0OO0oOo00Oo0o0Oo in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , o0OO0oOo00Oo0o0Oo )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 16 - 16: i1i1I1IIii1II + i1IiiiI1iI % OOooOOo + i1IiiiI1iI / oO0o
 if 73 - 73: I1ii11iIi11i . Iii * IiI1i11I . Ii1I . o0o00Oo0O
 if 38 - 38: i1i1I1IIii1II
 if 17 - 17: i1i1I1IIii1II / IiI1i11I . o0ii1I - IIiIiII11i
 if 6 - 6: oooOo0oo0oo / OOooOOo * I11i % oO0o + i1IiiiI1iI + IiI1i11I
 if 43 - 43: IiI1i11I
 if 25 - 25: oooOo0oo0oo % IiI1i11I + IiI1i11I
 if 41 - 41: oO0o / Ii1I . Ii1I / ooOoO0O00 - ooOoO0O00 - Ii1I
 if 78 - 78: IiI1i11I % IiI1i11I % o0o00Oo0O - Iii - oO0o
def IiOo00O0o0O ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for oO0o0 , Ii1IIiII1I , OOOii in os . walk ( o0 ) :
     Oo0O0 = 0
     Oo0O0 += len ( OOOii )
     if Oo0O0 > 0 :
      for IiII111i1i11 in OOOii :
       os . unlink ( os . path . join ( oO0o0 , IiII111i1i11 ) )
  IIiiiI1ii1I = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( IIiiiI1ii1I )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 94 - 94: oooOo0oo0oo - oOo0O0Ooo * i1IiiiI1iI / ooOoO0O00
 if 2 - 2: OOooOOo / i1iIi % iI11I1II1I1I * Ii1I / I11i
 if 92 - 92: IiI1i11I / ii * OOooOOo + OOooOOo - o0ii1I * I11i
 if 91 - 91: OOooOOo
 if 65 - 65: oooOo0oo0oo . IIiIiII11i * Ii + oooOo0oo0oo
 if 99 - 99: Ii1I % I1ii11iIi11i
 if 31 - 31: I11i - IIiIiII11i * oooOo0oo0oo . oooOo0oo0oo - i1i1I1IIii1II
 if 57 - 57: oooOo0oo0oo / Ii / i1IiiiI1iI - I1ii11iIi11i . iI11I1II1I1I
def OO000 ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 84 - 84: III1iiIii
def i111I1 ( url ) :
 iiiOOoO00o0OO = os . path . join ( oooOOOOO , 'addon_data' )
 IIiiI = [
 ( iiiOOoO00o0OO ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( iiiOOoO00o0OO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( iiiOOoO00o0OO , 'plugin.video.itv' , 'Images' ) ) ]
 if 34 - 34: I11i + oooOo0oo0oo . oO0o + oOo0O0Ooo + ii
 O0OOo = 0
 if 15 - 15: I11i / i1iIi * o0ii1I . IiI1i11I * Iii * OOooOOo
 for iII1i11 in IIiiI :
  if os . path . exists ( iII1i11 ) and not iII1i11 in [ oo0o0O00 , iiiOOoO00o0OO ] :
   for oO0o0 , Ii1IIiII1I , OOOii in os . walk ( iII1i11 ) :
    Oo0O0 = 0
    Oo0O0 += len ( OOOii )
    if Oo0O0 > 0 :
     for IiII111i1i11 in OOOii :
      if not IiII111i1i11 in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( oO0o0 , IiII111i1i11 ) )
       except :
        pass
      else : ooOoO00 ( 'Ignore Log File: %s' % IiII111i1i11 )
     for O0o0o in Ii1IIiII1I :
      try :
       shutil . rmtree ( os . path . join ( oO0o0 , O0o0o ) )
       O0OOo += 1
       ooOoO00 ( "[Success] cleared %s files from %s" % ( str ( Oo0O0 ) , os . path . join ( iII1i11 , O0o0o ) ) )
      except :
       ooOoO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , O0o0o ) )
  else :
   for oO0o0 , Ii1IIiII1I , OOOii in os . walk ( iII1i11 ) :
    for O0o0o in Ii1IIiII1I :
     if 'cache' in O0o0o . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( oO0o0 , O0o0o ) )
       O0OOo += 1
       ooOoO00 ( "[Success] wiped %s " % os . path . join ( iII1i11 , O0o0o ) )
      except :
       ooOoO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , O0o0o ) )
       if 96 - 96: i1i1I1IIii1II . IIiIiII11i % i1IiiiI1iI
 OO000 ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % O0OOo )
 if 52 - 52: o0ii1I / Ii / i1i1I1IIii1II
 if 54 - 54: i1i1I1IIii1II
 if 88 - 88: oooOo0oo0oo / o0ii1I . IiI1i11I - OOooOOo + IiI1i11I
 if 83 - 83: IiI1i11I + ii + ooOoO0O00 / I1ii11iIi11i
 if 28 - 28: oOo0O0Ooo
 if 5 - 5: I1ii11iIi11i % oooOo0oo0oo
 if 30 - 30: Ii1I * i1i1I1IIii1II + IIiIiII11i / Ii
def OOOo0Oo0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IiIIiIiI1ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oO0o0 , Ii1IIiII1I , OOOii in os . walk ( IiIIiIiI1ii ) :
   Oo0O0 = 0
   Oo0O0 += len ( OOOii )
   if 10 - 10: o0ii1I - IIiIiII11i / Ii * oOo0O0Ooo / o0o00Oo0O . Iii
   if 67 - 67: OOooOOo - i1iIi - iI11I1II1I1I
   if Oo0O0 > 0 :
    if 31 - 31: IIiIiII11i + I11i * Ii . I11i
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( Oo0O0 ) + " files found" , "Do you want to delete them?" ) :
     if 73 - 73: i1i1I1IIii1II / oooOo0oo0oo * IIiIiII11i % ii - ooOoO0O00 - i1iIi
     for IiII111i1i11 in OOOii :
      os . unlink ( os . path . join ( oO0o0 , IiII111i1i11 ) )
     for O0o0o in Ii1IIiII1I :
      shutil . rmtree ( os . path . join ( oO0o0 , O0o0o ) )
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
 if 43 - 43: I11i + o0ii1I % oO0o . i1IiiiI1iI + ooOoO0O00
 if 85 - 85: I1ii11iIi11i % Ii1I / oooOo0oo0oo
 if 65 - 65: i1iIi + III1iiIii - OOooOOo % IIiIiII11i - iI11I1II1I1I
 if 39 - 39: oOo0O0Ooo + Ii1I - Ii
 if 43 - 43: iI11I1II1I1I
 if 73 - 73: OOooOOo + I11i
 if 58 - 58: ooOoO0O00 * Ii1I % IiI1i11I . oO0o % III1iiIii % Iii
 if 63 - 63: Ii1I % i1iIi % Ii1I
 if 71 - 71: o0ii1I
def o00O0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IiIIiIiI1ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oO0o0 , Ii1IIiII1I , OOOii in os . walk ( IiIIiIiI1ii ) :
   Oo0O0 = 0
   Oo0O0 += len ( OOOii )
   if 43 - 43: I11i / i1iIi
   if 88 - 88: Ii - ooOoO0O00 + I1ii11iIi11i - o0o00Oo0O
   if Oo0O0 > 0 :
    if 50 - 50: Ii1I
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( Oo0O0 ) + " files found" , "Do you want to delete them?" ) :
     if 37 - 37: i1i1I1IIii1II % IiI1i11I / IIiIiII11i / oO0o - III1iiIii - i1iIi
     for IiII111i1i11 in OOOii :
      os . unlink ( os . path . join ( oO0o0 , IiII111i1i11 ) )
     for O0o0o in Ii1IIiII1I :
      shutil . rmtree ( os . path . join ( oO0o0 , O0o0o ) )
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
 if 69 - 69: Ii1I . ii % i1IiiiI1iI
 if 79 - 79: oOo0O0Ooo - III1iiIii . ii - Ii1I
 if 79 - 79: oooOo0oo0oo + I11i % IiI1i11I . i1i1I1IIii1II
 if 49 - 49: o0ii1I + Ii * OOooOOo . OOooOOo . Ii1I . I1ii11iIi11i
 if 61 - 61: Iii / oooOo0oo0oo
 if 85 - 85: OOooOOo - Iii . OOooOOo . OOooOOo
 if 62 - 62: III1iiIii % ii * oO0o + oO0o % o0ii1I % IiI1i11I
 if 66 - 66: oOo0O0Ooo . oooOo0oo0oo - oO0o % I1ii11iIi11i * I11i - i1i1I1IIii1II
 if 68 - 68: Iii - Ii / I11i + i1iIi / oOo0O0Ooo
 if 31 - 31: i1IiiiI1iI . ii . ooOoO0O00
def oOoO0OooO0O ( url , name ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ii11IIIi1Ii1 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 O000ooo = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml.bak' )
 if os . path . exists ( O000ooo ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   ii11IIIi1Ii1 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
   try :
    os . remove ( ii11IIIi1Ii1 )
    print '=== GenieTv - REMOVING    ' + str ( ii11IIIi1Ii1 ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   iiIiII = open ( ii11IIIi1Ii1 , "w" )
   iiIiII . write ( iiI111I1iIiI )
   iiIiII . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( ii11IIIi1Ii1 ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  ii11IIIi1Ii1 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
  try :
   os . remove ( ii11IIIi1Ii1 )
   print '=== GenieTv - REMOVING    ' + str ( ii11IIIi1Ii1 ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  iiIiII = open ( ii11IIIi1Ii1 , "w" )
  iiIiII . write ( iiI111I1iIiI )
  iiIiII . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ii11IIIi1Ii1 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 32 - 32: oooOo0oo0oo + III1iiIii
def I1i11I ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ii11IIIi1Ii1 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
 try :
  iiIiII = open ( ii11IIIi1Ii1 ) . read ( )
  if 'zero' in iiIiII :
   name = '0CACHE'
  elif 'tuxen' in iiIiII :
   name = 'TUXENS'
  elif 'muckys' in iiIiII :
   name = 'MUCKYS'
  elif 'p2p1' in iiIiII :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in iiIiII :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in iiIiII :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 24 - 24: o0ii1I * Ii / o0o00Oo0O - Ii1I
def O0ooo00oO ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ii11IIIi1Ii1 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
 try :
  os . remove ( ii11IIIi1Ii1 )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( ii11IIIi1Ii1 ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 74 - 74: o0ii1I - OOooOOo . IIiIiII11i / I1ii11iIi11i
 if 48 - 48: iI11I1II1I1I / Iii
 if 58 - 58: i1IiiiI1iI - Iii + i1i1I1IIii1II * oO0o
 if 45 - 45: III1iiIii * oooOo0oo0oo . oO0o
 if 56 - 56: III1iiIii * o0ii1I . IIiIiII11i / OOooOOo
 if 70 - 70: Ii1I
 if 82 - 82: oO0o + Ii
 if 100 - 100: iI11I1II1I1I % oooOo0oo0oo + i1iIi * o0ii1I
 if 3 - 3: i1iIi
 if 64 - 64: Ii1I % I1ii11iIi11i - iI11I1II1I1I % oO0o * iI11I1II1I1I + Iii
def i1I1I1iIIi ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for IIiI , oo000o00o0o00 , I1iiII1i1 , ooOoooo0o in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % IIiI , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % I1iiII1i1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % ooOoooo0o )
  inc = inc + 1
  if 31 - 31: III1iiIii + IiI1i11I . IiI1i11I
  if 12 - 12: iI11I1II1I1I + Ii1I / o0ii1I
  if 36 - 36: i1i1I1IIii1II + Ii1I + ii . I1ii11iIi11i % IiI1i11I * IIiIiII11i
  if 5 - 5: o0ii1I * IiI1i11I
  if 33 - 33: oOo0O0Ooo % Iii . i1IiiiI1iI / o0ii1I * IIiIiII11i * I11i
  if 49 - 49: ooOoO0O00 * Ii
  if 47 - 47: IIiIiII11i / I1ii11iIi11i
  if 38 - 38: oooOo0oo0oo . IiI1i11I / o0o00Oo0O . o0ii1I / OOooOOo
  if 52 - 52: o0o00Oo0O / Ii * oOo0O0Ooo . ooOoO0O00
def ii1O0 ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  ii11IIIi1Ii1 = os . path . join ( OO0OoOO0o0o , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  iiIiII = open ( ii11IIIi1Ii1 , "w" )
  iiIiII . write ( iiI111I1iIiI )
  iiIiII . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ii11IIIi1Ii1 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 54 - 54: ooOoO0O00 . o0o00Oo0O . ooOoO0O00 . oO0o + i1IiiiI1iI - Ii
def oo0Oooo ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  ii11IIIi1Ii1 = os . path . join ( OO0OoOO0o0o , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  iiIiII = open ( ii11IIIi1Ii1 , "w" )
  iiIiII . write ( iiI111I1iIiI )
  iiIiII . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ii11IIIi1Ii1 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 46 - 46: i1i1I1IIii1II
 if 66 - 66: III1iiIii
def O0o0Ii ( ) :
 try :
  iIII11ii1i1i1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iIII11ii1i1i1 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    iiIi1I1i1i = os . path . join ( iIII11ii1i1i1 , "source.db" )
    os . unlink ( iiIi1I1i1i )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 14 - 14: Ii
 if 100 - 100: iI11I1II1I1I * oooOo0oo0oo
 if 5 - 5: o0o00Oo0O - i1i1I1IIii1II - Ii
 if 8 - 8: oOo0O0Ooo / iI11I1II1I1I / ii / I1ii11iIi11i / i1iIi
 if 80 - 80: Iii
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 26 - 26: IIiIiII11i + oOo0O0Ooo . IIiIiII11i - i1i1I1IIii1II % oO0o
 if 1 - 1: oO0o - IIiIiII11i
 if 75 - 75: I1ii11iIi11i - OOooOOo + i1i1I1IIii1II % ooOoO0O00 * oooOo0oo0oo
 if 56 - 56: OOooOOo / oO0o / oOo0O0Ooo % ii
 if 39 - 39: oOo0O0Ooo + IIiIiII11i * I1ii11iIi11i % o0ii1I . I11i * i1i1I1IIii1II
 if 42 - 42: o0ii1I / I1ii11iIi11i
 if 25 - 25: ii % o0ii1I * i1IiiiI1iI * Iii + oOo0O0Ooo % Ii1I
def o0OoOO ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; O00O00i1I1iiIiII11 = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if O00O00i1I1iiIiII11 :
  Oo0o = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; Oo0o = xbmc . translatePath ( Oo0o ) ;
  O0o0OOo = os . path . join ( Oo0o , ".." , ".." ) ; O0o0OOo = os . path . abspath ( O0o0OOo ) ; pluginlog ( "freshstart.main_list xbmcPath=" + O0o0OOo ) ; I111ii11I = False
  try :
   for oO0o0 , Ii1IIiII1I , OOOii in os . walk ( O0o0OOo , topdown = True ) :
    Ii1IIiII1I [ : ] = [ O0o0o for O0o0o in Ii1IIiII1I if O0o0o not in o0oO0 ]
    for OOoO in OOOii :
     try : os . remove ( os . path . join ( oO0o0 , OOoO ) )
     except :
      if OOoO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : I111ii11I = True
      pluginlog ( "Error removing " + oO0o0 + " " + OOoO )
    for OOoO in Ii1IIiII1I :
     try : os . rmdir ( os . path . join ( oO0o0 , OOoO ) )
     except :
      if OOoO not in [ "Database" , "userdata" ] : I111ii11I = True
      pluginlog ( "Error removing " + oO0o0 + " " + OOoO )
   if not I111ii11I : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 iI1I ( )
 if 11 - 11: ii - Ii + IiI1i11I . I1ii11iIi11i + ii + IiI1i11I
 if 1 - 1: I11i
 if 43 - 43: Iii - iI11I1II1I1I - Iii
def o0Oo00OoO000O ( ) :
 II1iii = [ ]
 O0oOOOO0o = sys . argv [ 2 ]
 if len ( O0oOOOO0o ) >= 2 :
  O0O0Oo00 = sys . argv [ 2 ]
  OoOOO0 = O0O0Oo00 . replace ( '?' , '' )
  if ( O0O0Oo00 [ len ( O0O0Oo00 ) - 1 ] == '/' ) :
   O0O0Oo00 = O0O0Oo00 [ 0 : len ( O0O0Oo00 ) - 2 ]
  IiIio0oO0O = OoOOO0 . split ( '&' )
  II1iii = { }
  for II1i1iI in range ( len ( IiIio0oO0O ) ) :
   IiiiiII1Ii1 = { }
   IiiiiII1Ii1 = IiIio0oO0O [ II1i1iI ] . split ( '=' )
   if ( len ( IiiiiII1Ii1 ) ) == 2 :
    II1iii [ IiiiiII1Ii1 [ 0 ] ] = IiiiiII1Ii1 [ 1 ]
    if 54 - 54: Ii
 return II1iii
 if 57 - 57: Iii / III1iiIii * ooOoO0O00 + IIiIiII11i . I11i
iIII1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
IIiIi = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ooO0O0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
ii1iI111IIi1 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I1IiiiI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
Oo00 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
OO0oO0ooOOOoO = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
IiiiiiiiI1i11 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
I1IO0 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
iIi1I1Iii1 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iI1iIIiIi1I1 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
iiI1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
ii111Ii = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
I1i1II = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
o000OOOooOo = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OooOO = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
IIIIII1iI1II = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Ii1i1i = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o0III11IiI = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OoO00oo0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
ooooOOO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oOOoOOooO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
Ii1ii111i = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
iiII = base64 . decodestring ( 'Q1VOVA==' )
def oooooOOo0o ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 i111I11i . setProperty ( 'fanart_image' , fanart )
 i111I11i . setProperty ( "IsPlayable" , "true" )
 i1IIi = [ ]
 i1IIi . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 i1IIi . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 i111I11i . addContextMenuItems ( i1IIi , replaceItems = True )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = False )
 return iiI1i1Iii111
def Iii1I1I11iiI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111I11i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1OoOO = [ ]
  if showcontext == 'fav' :
   ii1OoOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   ii1OoOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111I11i . addContextMenuItems ( ii1OoOO )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = True )
 return iiI1i1Iii111
 if 91 - 91: i1iIi . IiI1i11I - o0o00Oo0O . I11i . III1iiIii
def iI1Ii1iI11iiI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 I11I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 iiI1i1Iii111 = True
 i111I11i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111I11i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111I11i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ii1OoOO = [ ]
  if showcontext == 'fav' :
   ii1OoOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   ii1OoOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111I11i . addContextMenuItems ( ii1OoOO )
 iiI1i1Iii111 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I11I1 , listitem = i111I11i , isFolder = False )
 return iiI1i1Iii111
 if 30 - 30: OOooOOo
 if 70 - 70: i1iIi - I11i + IIiIiII11i + i1i1I1IIii1II + ooOoO0O00
O0O0Oo00 = o0Oo00OoO000O ( )
O0O00Oo = None
OOoO = None
OooOo00o = None
oo00O00oO000o = None
oooOo0OOOoo0 = None
o0OO0oOo00Oo0o0Oo = None
oOOo0oOoooO0o = None
IiIIooOoo0 = None
if 50 - 50: iI11I1II1I1I . I1ii11iIi11i
if 49 - 49: OOooOOo * Iii - I11i / oO0o * i1i1I1IIii1II
try :
 IiIIooOoo0 = int ( O0O0Oo00 [ "fav_mode" ] )
except :
 pass
 if 51 - 51: i1iIi - iI11I1II1I1I . Iii * OOooOOo + i1IiiiI1iI * ooOoO0O00
try :
 O0O00Oo = urllib . unquote_plus ( O0O0Oo00 [ "url" ] )
except :
 pass
try :
 OOoO = urllib . unquote_plus ( O0O0Oo00 [ "name" ] )
except :
 pass
try :
 oo00O00oO000o = urllib . unquote_plus ( O0O0Oo00 [ "iconimage" ] )
except :
 pass
try :
 OooOo00o = int ( O0O0Oo00 [ "mode" ] )
except :
 pass
try :
 oooOo0OOOoo0 = urllib . unquote_plus ( O0O0Oo00 [ "fanart" ] )
except :
 pass
try :
 o0OO0oOo00Oo0o0Oo = urllib . unquote_plus ( O0O0Oo00 [ "description" ] )
except :
 pass
 if 37 - 37: III1iiIii * i1i1I1IIii1II / ii . oO0o
 if 77 - 77: IIiIiII11i + OOooOOo * oooOo0oo0oo
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( OooOo00o )
print "URL: " + str ( O0O00Oo )
print "Name: " + str ( OOoO )
print "IconImage: " + str ( oo00O00oO000o )
if 9 - 9: IIiIiII11i - Ii * I11i % oO0o * Ii / Iii
if 45 - 45: Ii * IiI1i11I - Ii1I + i1iIi % IiI1i11I
def oOI1Ii1I1 ( content , viewType ) :
 if 11 - 11: iI11I1II1I1I
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 48 - 48: iI11I1II1I1I - I1ii11iIi11i
if oo00O00oO000o == None : oo00O00oO000o = O0O
if oooOo0OOOoo0 == None : oooOo0OOOoo0 = Oo00OOOOO
if OooOo00o == None :
 I1IiiiiI ( )
 if 80 - 80: ooOoO0O00
elif OooOo00o == 1 :
 I1111III111ii ( O0O00Oo )
 if 56 - 56: IIiIiII11i - I11i
elif OooOo00o == 44 :
 oOoO00o ( O0O00Oo )
 if 48 - 48: I1ii11iIi11i - Ii1I - IIiIiII11i . o0ii1I . i1i1I1IIii1II / iI11I1II1I1I
elif OooOo00o == 2 :
 OooO00o000 ( )
 if 38 - 38: i1IiiiI1iI % Ii + o0ii1I * i1iIi / i1IiiiI1iI
elif OooOo00o == 3 :
 IIoO ( )
 if 93 - 93: i1i1I1IIii1II
elif OooOo00o == 21 :
 i1i1II ( )
 if 60 - 60: i1IiiiI1iI . i1i1I1IIii1II / I1ii11iIi11i * i1iIi + OOooOOo - ooOoO0O00
elif OooOo00o == 4 :
 I1iO0o0O0OooOoo ( )
 if 13 - 13: Ii * i1i1I1IIii1II / Iii * oOo0O0Ooo
elif OooOo00o == 5 :
 iiiiii1ii1 ( O0O00Oo )
 if 31 - 31: iI11I1II1I1I * o0ii1I % oooOo0oo0oo . IIiIiII11i
elif OooOo00o == 6 :
 OOOo0Oo0O ( O0O00Oo )
 if 56 - 56: III1iiIii / Ii . I11i . i1i1I1IIii1II - Ii
elif OooOo00o == 7 :
 oOoO0OooO0O ( O0O00Oo , OOoO )
 if 23 - 23: Ii1I * Ii % i1iIi
elif OooOo00o == 8 :
 I1i11I ( O0O00Oo , OOoO )
 if 47 - 47: iI11I1II1I1I . oooOo0oo0oo / Iii % IIiIiII11i
elif OooOo00o == 9 :
 FIXREPOSADDONS ( O0O00Oo )
 if 92 - 92: Ii1I % Ii
elif OooOo00o == 10 :
 ii1iii1i ( )
 if 82 - 82: i1IiiiI1iI * Ii1I % o0ii1I / I11i
elif OooOo00o == 11 :
 O0ooo00oO ( O0O00Oo )
 if 28 - 28: IiI1i11I % oO0o - oooOo0oo0oo - I1ii11iIi11i
elif OooOo00o == 12 :
 i1I1I1iIIi ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 16 - 16: Ii - Ii . OOooOOo / ooOoO0O00
elif OooOo00o == 13 :
 IiOo00O0o0O ( )
 if 76 - 76: o0o00Oo0O * oO0o / o0o00Oo0O
elif OooOo00o == 14 :
 i111I1 ( O0O00Oo )
 if 23 - 23: Ii1I . iI11I1II1I1I - Ii / IIiIiII11i
elif OooOo00o == 15 :
 oOOooO ( )
 if 48 - 48: i1i1I1IIii1II - IIiIiII11i * oOo0O0Ooo
elif OooOo00o == 16 :
 ii1O0 ( O0O00Oo , OOoO )
 if 78 - 78: oOo0O0Ooo * Ii * IIiIiII11i
elif OooOo00o == 17 :
 oo0Oooo ( O0O00Oo , OOoO )
 if 19 - 19: ii * Ii / o0o00Oo0O . oOo0O0Ooo % Iii
elif OooOo00o == 18 :
 O0o0Ii ( )
 if 35 - 35: iI11I1II1I1I + oOo0O0Ooo - i1iIi / I1ii11iIi11i * Ii1I * I1ii11iIi11i
elif OooOo00o == 19 :
 oOoo00 ( O0O00Oo )
 if 17 - 17: OOooOOo
elif OooOo00o == 40 :
 o00OOOOooO ( OOoO , O0O00Oo , o0OO0oOo00Oo0o0Oo )
 if 24 - 24: iI11I1II1I1I / oooOo0oo0oo % ii / o0o00Oo0O / i1i1I1IIii1II
elif OooOo00o == 42 :
 ooOoo0OOOO0o ( OOoO , O0O00Oo , o0OO0oOo00Oo0o0Oo )
 if 93 - 93: I1ii11iIi11i
elif OooOo00o == 43 :
 oOOO0 ( O0O00Oo )
 if 5 - 5: IiI1i11I
elif OooOo00o == 20 :
 II1iOOoOooO0o ( O0O00Oo )
 if 61 - 61: oooOo0oo0oo * oO0o - o0o00Oo0O
elif OooOo00o == 22 :
 II1II111iIi ( O0O00Oo )
 if 30 - 30: iI11I1II1I1I
elif OooOo00o == 23 :
 iiOOo ( O0O00Oo )
 if 14 - 14: I11i + o0ii1I
elif OooOo00o == 24 :
 o0OOOOooOo ( O0O00Oo )
 if 91 - 91: ii / i1i1I1IIii1II + OOooOOo
elif OooOo00o == 25 :
 oOOOo000 ( O0O00Oo )
 if 100 - 100: ooOoO0O00
elif OooOo00o == 26 :
 o0oo0oO ( O0O00Oo )
 if 13 - 13: ooOoO0O00 . Ii1I * I11i
elif OooOo00o == 27 :
 iIiiii ( O0O00Oo )
 if 31 - 31: Ii % oO0o . Ii % i1i1I1IIii1II - ooOoO0O00
elif OooOo00o == 28 :
 o00Ooo0OooOo0 ( O0O00Oo )
 if 62 - 62: i1i1I1IIii1II + i1i1I1IIii1II . ii
elif OooOo00o == 29 :
 i1II1iI1ii1 ( O0O00Oo )
 if 59 - 59: iI11I1II1I1I . I1ii11iIi11i * Iii
elif OooOo00o == 30 :
 o0oo00O ( O0O00Oo )
 if 29 - 29: I1ii11iIi11i - oOo0O0Ooo * Iii
elif OooOo00o == 31 :
 OoI1iIi ( O0O00Oo )
 if 58 - 58: ooOoO0O00 * o0ii1I / i1iIi % iI11I1II1I1I
elif OooOo00o == 32 :
 o0oO00OOo0oO ( )
 if 24 - 24: OOooOOo - I11i * oOo0O0Ooo . Iii / oO0o * o0ii1I
elif OooOo00o == 33 :
 oOiiI11I1ii11 ( )
 if 12 - 12: ii % i1i1I1IIii1II
elif OooOo00o == 35 :
 i1ii11I111Ii ( O0O00Oo )
 if 92 - 92: i1iIi % oO0o + o0o00Oo0O + OOooOOo / oO0o * iI11I1II1I1I
elif OooOo00o == 34 :
 O0OoO0oooOO ( O0O00Oo )
 if 79 - 79: o0o00Oo0O
elif OooOo00o == 36 :
 i1111I ( O0O00Oo )
 if 71 - 71: oO0o - o0o00Oo0O
elif OooOo00o == 37 :
 oOOO00 ( O0O00Oo )
 if 73 - 73: iI11I1II1I1I
elif OooOo00o == 38 :
 IIii1Ii1i1ii1 ( O0O00Oo )
 if 7 - 7: OOooOOo
elif OooOo00o == 41 :
 o0OoOO ( O0O0Oo00 )
 if 55 - 55: i1i1I1IIii1II . oO0o + iI11I1II1I1I + OOooOOo / Ii1I - o0o00Oo0O
elif OooOo00o == 39 :
 oOOoo00O00o ( O0O00Oo )
 if 14 - 14: IIiIiII11i - oO0o - o0o00Oo0O * ii / oOo0O0Ooo
elif OooOo00o == 45 :
 TEXTS ( )
 if 3 - 3: Iii
elif OooOo00o == 46 :
 oooooo0O000o ( )
 if 46 - 46: Ii1I * i1IiiiI1iI - iI11I1II1I1I
elif OooOo00o == 47 :
 GEVID ( )
 if 25 - 25: IIiIiII11i / oooOo0oo0oo + I1ii11iIi11i - iI11I1II1I1I - OOooOOo
elif OooOo00o == 48 :
 Iiiii ( OOoO , O0O00Oo , o0OO0oOo00Oo0o0Oo )
 if 97 - 97: oooOo0oo0oo . oooOo0oo0oo / Ii1I + oOo0O0Ooo * ooOoO0O00
elif OooOo00o == 49 :
 I1ii1ii11i1I ( )
 if 53 - 53: o0o00Oo0O
elif OooOo00o == 22222 :
 OooOo ( O0O00Oo )
 if 28 - 28: IiI1i11I % oO0o . oO0o / III1iiIii * I1ii11iIi11i * IiI1i11I
elif OooOo00o == 222225 :
 IIIiIi ( O0O00Oo )
 if 49 - 49: oOo0O0Ooo / i1IiiiI1iI * IiI1i11I + oOo0O0Ooo % i1i1I1IIii1II % i1iIi
elif OooOo00o == 222 :
 I1iO0000 ( O0O00Oo )
 if 27 - 27: oO0o / IiI1i11I . Ii1I
elif OooOo00o == 2222222 :
 OooO0OO ( O0O00Oo )
 if 71 - 71: oO0o . Ii . iI11I1II1I1I + oOo0O0Ooo - I11i
elif OooOo00o == 222222 :
 O0iiI1iii1I111 ( O0O00Oo , OOoO )
 if 34 - 34: IiI1i11I
elif OooOo00o == 333 :
 i1O0o00o0Oo ( O0O00Oo )
 if 6 - 6: oO0o . OOooOOo + Ii1I
 if 24 - 24: oO0o . o0ii1I
elif OooOo00o == 1020 :
 iIiIIIIII11iI ( )
 if 26 - 26: o0o00Oo0O * oOo0O0Ooo - oooOo0oo0oo * ii * IIiIiII11i % OOooOOo
elif OooOo00o == 1021 :
 ANIMEEP ( )
 if 56 - 56: oooOo0oo0oo * Ii % i1iIi * OOooOOo % I1ii11iIi11i * III1iiIii
elif OooOo00o == 1022 :
 ANIMEPLAY ( O0O00Oo )
 if 30 - 30: ooOoO0O00 + I11i - OOooOOo . oooOo0oo0oo
elif OooOo00o == 1001 :
 I1I1Ii ( )
 if 95 - 95: ooOoO0O00 . Iii + o0o00Oo0O . Iii - Iii / I1ii11iIi11i
elif OooOo00o == 1005 :
 Oo000o0o0 ( )
 if 41 - 41: ii . oooOo0oo0oo - o0ii1I * oO0o % Ii
elif OooOo00o == 1007 :
 oOO0ooOoOoOo ( O0O00Oo )
 if 7 - 7: o0ii1I
elif OooOo00o == 1010 :
 OOOOoO0 ( O0O00Oo )
 if 16 - 16: III1iiIii * I11i % IIiIiII11i - IIiIiII11i + i1iIi
elif OooOo00o == 1011 :
 oOO00O0O0oO0 ( O0O00Oo )
 if 55 - 55: oO0o % OOooOOo
elif OooOo00o == 1012 :
 iII1IiI1I11i ( O0O00Oo )
 if 58 - 58: o0ii1I
elif OooOo00o == 1030 :
 IIiiii111iI ( )
 if 17 - 17: oO0o - i1i1I1IIii1II % I1ii11iIi11i % i1i1I1IIii1II * i1IiiiI1iI / III1iiIii
elif OooOo00o == 1031 :
 iI1III11IIi11Ii11 ( O0O00Oo , oo00O00oO000o )
 if 88 - 88: i1iIi . IIiIiII11i * o0o00Oo0O % III1iiIii
elif OooOo00o == 1032 :
 O0OoOo ( O0O00Oo )
 if 15 - 15: o0o00Oo0O % ooOoO0O00 - oooOo0oo0oo . III1iiIii
elif OooOo00o == 1006 :
 Parse . ParseURL ( O0O00Oo )
 if 1 - 1: oOo0O0Ooo
elif OooOo00o == 2030 :
 Parse . addonParseURL ( O0O00Oo )
 if 40 - 40: I11i % Iii % o0o00Oo0O
elif OooOo00o == 2031 :
 Parse . apkParseURL ( O0O00Oo )
 if 88 - 88: I11i - i1i1I1IIii1II
elif OooOo00o == 2032 :
 Parse . ParseBOSS ( O0O00Oo )
 if 73 - 73: IIiIiII11i
elif OooOo00o == 1002 :
 i1I1I1IIIi11 ( O0O00Oo )
 if 7 - 7: o0o00Oo0O / oO0o
elif OooOo00o == 1003 :
 ooOo000 ( O0O00Oo , oo00O00oO000o )
 if 90 - 90: IiI1i11I % i1i1I1IIii1II / iI11I1II1I1I
elif OooOo00o == 1004 :
 OO0o0oo ( O0O00Oo )
 if 52 - 52: oOo0O0Ooo / I11i
elif OooOo00o == 1008 :
 OOOo0OO0ooO0O0O ( )
 if 20 - 20: i1IiiiI1iI . oOo0O0Ooo - iI11I1II1I1I / IiI1i11I
elif OooOo00o == 1009 :
 OOoooo0000Oo ( O0O00Oo )
 if 46 - 46: i1IiiiI1iI . Ii
elif OooOo00o == 2001 :
 Ooo0o0o ( )
 if 89 - 89: oO0o - oooOo0oo0oo - ooOoO0O00 - oO0o % iI11I1II1I1I
elif OooOo00o == 2002 :
 oO0oooo ( O0O00Oo )
 if 52 - 52: I11i * o0o00Oo0O + Ii1I
elif OooOo00o == 1013 :
 O0ooooO ( )
elif OooOo00o == 10111113 :
 Oooo0oOooOO ( O0O00Oo )
 if 83 - 83: Iii + oooOo0oo0oo - ii
elif OooOo00o == 1014 :
 I1Ii ( )
 if 7 - 7: III1iiIii % i1iIi / ii / I11i + oO0o - oO0o
elif OooOo00o == 1015 :
 OO00O0OoooO ( O0O00Oo )
 if 15 - 15: ooOoO0O00 + oooOo0oo0oo / o0ii1I
elif OooOo00o == 1016 :
 i1i1I111iIi1 ( O0O00Oo , oo00O00oO000o , OOoO )
 if 51 - 51: oooOo0oo0oo + o0o00Oo0O
elif OooOo00o == 1017 :
 OoOiIIiii ( )
 if 91 - 91: Ii + I11i % oO0o / i1i1I1IIii1II - ooOoO0O00
elif OooOo00o == 1018 :
 o00oO ( O0O00Oo )
 if 82 - 82: o0ii1I . ii + ii % oO0o % Ii1I
elif OooOo00o == 1019 :
 III11II1I1Ii1 ( O0O00Oo )
elif OooOo00o == 10190 :
 oO0o00oOOooO0 ( O0O00Oo )
 if 65 - 65: I1ii11iIi11i . Iii
elif OooOo00o == 1023 :
 oooOOo0oOoOO ( )
 if 7 - 7: I1ii11iIi11i * IIiIiII11i
elif OooOo00o == 1024 :
 OOO0oOO ( O0O00Oo )
 if 11 - 11: OOooOOo % ii
elif OooOo00o == 1025 :
 O0O0oOoO0O0oO ( O0O00Oo )
 if 92 - 92: OOooOOo - IiI1i11I * o0ii1I - ooOoO0O00
elif OooOo00o == 4001 :
 OoOooOoO ( )
 if 87 - 87: o0ii1I * i1IiiiI1iI + iI11I1II1I1I * I11i * iI11I1II1I1I . Iii
elif OooOo00o == 4002 :
 oOOo0OOOo00O ( )
 if 66 - 66: o0ii1I / oO0o . o0o00Oo0O . Iii % ii / oooOo0oo0oo
elif OooOo00o == 4003 :
 iIIII11i ( )
 if 49 - 49: oOo0O0Ooo * IiI1i11I - oO0o % o0ii1I + o0ii1I * i1IiiiI1iI
elif OooOo00o == 4004 :
 ii1 ( )
 if 94 - 94: OOooOOo - Iii + o0ii1I + OOooOOo + IIiIiII11i
elif OooOo00o == 4005 :
 IiIi1iIIi1 ( )
 if 61 - 61: III1iiIii + o0ii1I / i1i1I1IIii1II . ii + IiI1i11I
elif OooOo00o == 4006 :
 II1i ( )
 if 29 - 29: oooOo0oo0oo
elif OooOo00o == 4007 :
 iiIi1i ( )
 if 69 - 69: i1i1I1IIii1II % ii * IiI1i11I
elif OooOo00o == 4008 :
 OOoOOO0 ( )
 if 58 - 58: i1i1I1IIii1II / Ii . OOooOOo % o0o00Oo0O / iI11I1II1I1I
elif OooOo00o == 40099 : i1IiI ( )
elif OooOo00o == 4009 : O0oo00oOOO0o ( )
elif OooOo00o == 4010 : O0o0 ( )
elif OooOo00o == 3000 :
 OO0O000OOO0 ( )
 if 50 - 50: i1IiiiI1iI . Iii / o0o00Oo0O . Iii
elif OooOo00o == 3001 :
 iii1I ( )
 if 91 - 91: Ii . Ii1I + Iii
elif OooOo00o == 3002 :
 iIiI11I ( O0O00Oo )
 if 67 - 67: Ii1I * i1IiiiI1iI * oOo0O0Ooo / Iii - III1iiIii + i1i1I1IIii1II
elif OooOo00o == 3003 :
 IIII11 ( O0O00Oo )
 if 11 - 11: o0o00Oo0O + ooOoO0O00 / I11i * oO0o
elif OooOo00o == 3004 :
 ooOo0o0 ( O0O00Oo )
 if 64 - 64: ooOoO0O00 % III1iiIii . i1iIi . iI11I1II1I1I + oO0o - iI11I1II1I1I
elif OooOo00o == 404 :
 I1ii111I ( OOoO , O0O00Oo , oo00O00oO000o )
 if 52 - 52: IIiIiII11i - III1iiIii
elif OooOo00o == 405 :
 IIiiIIIiI ( O0O00Oo )
 if 91 - 91: iI11I1II1I1I + IiI1i11I . Iii % Ii - Ii + oOo0O0Ooo
elif OooOo00o == 7030 :
 oo0Oooo0O ( )
 if 75 - 75: Ii1I / oOo0O0Ooo - iI11I1II1I1I / oO0o * oooOo0oo0oo
elif OooOo00o == 7021 :
 i11II ( OOoO )
 if 73 - 73: ii % III1iiIii / i1IiiiI1iI * Iii + ooOoO0O00 % Ii
elif OooOo00o == 7022 :
 iiiII1i ( OOoO )
 if 91 - 91: Ii
elif OooOo00o == 7000 :
 i11I1IiIi ( OOoO , O0O00Oo , img )
 if 6 - 6: o0o00Oo0O - iI11I1II1I1I + i1IiiiI1iI . I11i * Ii
elif OooOo00o == 7050 :
 o0ooOooO ( O0O00Oo )
 if 53 - 53: oooOo0oo0oo / oOo0O0Ooo / i1i1I1IIii1II * oooOo0oo0oo / ooOoO0O00 - i1IiiiI1iI
elif OooOo00o == 7051 :
 iIo0O00o00o0 ( O0O00Oo )
 if 71 - 71: o0o00Oo0O + I1ii11iIi11i % i1i1I1IIii1II - I11i
elif OooOo00o == 7052 :
 Iiooo000o0OoOo ( O0O00Oo )
 if 82 - 82: iI11I1II1I1I
elif OooOo00o == 7053 :
 O0oo0OoooO0 ( O0O00Oo )
 if 64 - 64: i1iIi + oOo0O0Ooo % oooOo0oo0oo + IIiIiII11i
elif OooOo00o == 7054 :
 CoolPlay ( O0O00Oo )
 if 46 - 46: oOo0O0Ooo
elif OooOo00o == 7060 :
 iI1iIiiIii ( )
 if 72 - 72: IiI1i11I
elif OooOo00o == 7061 :
 oO0OoO00o ( O0O00Oo )
 if 100 - 100: oOo0O0Ooo
elif OooOo00o == 7063 :
 O0OOOOO0O ( O0O00Oo )
 if 55 - 55: ooOoO0O00 % III1iiIii
elif OooOo00o == 7062 :
 iiiiII1i1Iii1I1 ( O0O00Oo )
 if 44 - 44: i1i1I1IIii1II - iI11I1II1I1I / i1iIi - iI11I1II1I1I % ooOoO0O00 + i1iIi
elif OooOo00o == 7064 :
 NATatozcat ( )
 if 74 - 74: Iii . OOooOOo + OOooOOo
elif OooOo00o == 7067 :
 OoOO00OO0OoOoooOooOO0o ( O0O00Oo )
 if 87 - 87: III1iiIii + I11i . ooOoO0O00 % i1IiiiI1iI
elif OooOo00o == 7066 :
 NATatozA ( O0O00Oo )
 if 44 - 44: I1ii11iIi11i - oooOo0oo0oo . o0ii1I * ii
elif OooOo00o == 7065 :
 I1iooOOooO ( O0O00Oo )
 if 93 - 93: oO0o . oO0o
elif OooOo00o == 7070 :
 i1Ii11 ( )
 if 52 - 52: oooOo0oo0oo . i1i1I1IIii1II / I1ii11iIi11i . ii % Ii1I
elif OooOo00o == 7071 :
 DIZIlist ( O0O00Oo )
 if 65 - 65: i1iIi % IIiIiII11i . IiI1i11I - iI11I1II1I1I - oOo0O0Ooo
elif OooOo00o == 7072 :
 DIZIpull ( O0O00Oo )
 if 63 - 63: oOo0O0Ooo . OOooOOo - IIiIiII11i
elif OooOo00o == 7073 :
 WATCHDIZI ( O0O00Oo )
 if 55 - 55: i1iIi - I11i
elif OooOo00o == 7002 :
 oooOO0OoO0OOO ( )
 if 32 - 32: i1IiiiI1iI * o0ii1I / i1IiiiI1iI . OOooOOo + Ii1I - i1iIi
elif OooOo00o == 7003 :
 O00oo ( O0O00Oo )
 if 14 - 14: III1iiIii * o0o00Oo0O + o0o00Oo0O - i1iIi . Ii - III1iiIii
elif OooOo00o == 7004 :
 o0Oi1i1i11IIii ( O0O00Oo )
 if 37 - 37: Iii
elif OooOo00o == 7020 :
 OooooO0000 ( O0O00Oo )
 if 19 - 19: ii % i1IiiiI1iI
elif OooOo00o == 7001 :
 I1IIIiIiIi ( )
 if 57 - 57: OOooOOo + ooOoO0O00 . iI11I1II1I1I . iI11I1II1I1I / iI11I1II1I1I % i1i1I1IIii1II
elif OooOo00o == 7010 :
 oO0OOOo0OO ( O0O00Oo )
 if 7 - 7: Ii * Ii1I / oO0o * i1i1I1IIii1II
elif OooOo00o == 7011 :
 iiiiIiI1IIiI ( O0O00Oo )
 if 35 - 35: III1iiIii . ooOoO0O00 + Ii1I . III1iiIii + i1iIi . i1i1I1IIii1II
elif OooOo00o == 7012 :
 OOoOOo0o0OOo0 ( O0O00Oo )
 if 2 - 2: IIiIiII11i
elif OooOo00o == 7013 :
 cnfTVPlay2 ( O0O00Oo )
elif OooOo00o == 7014 :
 CNF_Studio_Indexer . MV_Movies ( O0O00Oo )
elif OooOo00o == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( O0O00Oo )
elif OooOo00o == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( OOoO , O0O00Oo , oo00O00oO000o )
elif OooOo00o == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif OooOo00o == 7018 :
 iiiIiII1II ( )
elif OooOo00o == 7019 :
 CNF_Studio_Indexer . List_Movies ( O0O00Oo )
elif OooOo00o == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( O0O00Oo )
elif OooOo00o == 7024 :
 CNF_Studio_Indexer . Box_Office ( O0O00Oo )
 if 18 - 18: iI11I1II1I1I % Ii1I % I1ii11iIi11i
elif OooOo00o == 8000 :
 i111iiII1I ( )
elif OooOo00o == 8001 :
 OOo0o0 ( )
elif OooOo00o == 8002 :
 I11Oo0O00O0O00 ( )
elif OooOo00o == 8003 :
 I1IiiIiIIi1Ii ( )
elif OooOo00o == 8004 :
 O00O ( )
elif OooOo00o == 8005 :
 Ii1ii1I1I ( )
elif OooOo00o == 8006 :
 iIiI1iI ( OOoO , O0O00Oo )
elif OooOo00o == 8030 :
 Iii11iI1I ( O0O00Oo )
elif OooOo00o == 8045 :
 iI11 ( O0O00Oo )
elif OooOo00o == 8046 :
 i1IiI1Ii ( O0O00Oo )
elif OooOo00o == 8047 :
 i1II111II1 ( O0O00Oo )
elif OooOo00o == 8048 :
 i1IO0OoO0o ( O0O00Oo )
elif OooOo00o == 8049 :
 o0Oo00oOOO0o ( O0O00Oo )
elif OooOo00o == 804900 :
 o0ii1I1 ( O0O00Oo )
elif OooOo00o == 8020 :
 o00oOoOo0 ( )
elif OooOo00o == 8021 :
 Oo0oOo ( O0O00Oo )
elif OooOo00o == 8022 :
 o0oO0oOO ( O0O00Oo )
elif OooOo00o == 8023 :
 I1iIiiI ( O0O00Oo )
elif OooOo00o == 8040 :
 I1I1i ( )
elif OooOo00o == 8041 :
 oOoO00O00o ( O0O00Oo )
elif OooOo00o == 8042 :
 O00O0O0 ( O0O00Oo )
elif OooOo00o == 8043 :
 yt . PlayVideo ( O0O00Oo )
elif OooOo00o == 8044 :
 ii1IiIi1iIi ( O0O00Oo )
elif OooOo00o == 8060 :
 oOO ( )
elif OooOo00o == 8061 :
 o0oOoOOO ( O0O00Oo )
elif OooOo00o == 8064 :
 oo000ii ( )
elif OooOo00o == 8065 :
 i1Iiiiii1II ( O0O00Oo )
elif OooOo00o == 8070 :
 oO0oo00o ( )
elif OooOo00o == 8071 :
 o0Oo0oOO00O ( O0O00Oo )
elif OooOo00o == 7080 :
 Oo00OO ( O0O00Oo )
elif OooOo00o == 8090 :
 I1iI1I ( )
elif OooOo00o == 8091 :
 O0O0OOo00Oo ( O0O00Oo )
elif OooOo00o == 8092 :
 IIiIiiii1I1 ( O0O00Oo )
elif OooOo00o == 8093 :
 IiI1iIIiIi1Ii ( O0O00Oo )
elif OooOo00o == 8081 :
 oOooo0ooo ( )
elif OooOo00o == 8062 :
 iI1I1I ( O0O00Oo )
elif OooOo00o == 8063 :
 OOo00ooOOo0ooO0 ( O0O00Oo )
elif OooOo00o == 8050 :
 iIIiIi111iI ( )
elif OooOo00o == 8051 :
 II1I1ii ( O0O00Oo )
elif OooOo00o == 8052 :
 oo0OO0O ( O0O00Oo )
elif OooOo00o == 8085 :
 OOoo00o0OoO ( )
elif OooOo00o == 8086 :
 Ooo0 ( O0O00Oo )
elif OooOo00o == 8087 :
 oOO0Ooo ( O0O00Oo )
elif OooOo00o == 8088 :
 IiIi1I1iI1 ( O0O00Oo , OOoO )
elif OooOo00o == 9000 :
 iI1iiiiiii ( )
elif OooOo00o == 1111 :
 IiiIiIIi1 ( )
elif OooOo00o == 9001 :
 I1IiiI1ii1i ( )
elif OooOo00o == 9002 :
 O0OoO0ooOO0o ( )
elif OooOo00o == 9003 :
 iIiii ( )
elif OooOo00o == 9004 :
 World1 ( )
elif OooOo00o == 9005 :
 World2 ( O0O00Oo )
elif OooOo00o == 9006 :
 World3 ( O0O00Oo )
elif OooOo00o == 9007 :
 O0ooOOO ( )
elif OooOo00o == 9008 :
 iI1ii1i1iIi ( O0O00Oo )
elif OooOo00o == 9009 :
 II11Iiii1i1II ( O0O00Oo )
elif OooOo00o == 9010 :
 IiIII ( )
elif OooOo00o == 9011 :
 iII1iII ( O0O00Oo )
elif OooOo00o == 50 :
 O0iII1i1 ( O0O00Oo )
elif OooOo00o == 9020 :
 champlist ( )
elif OooOo00o == 9021 :
 Ii1 ( )
elif OooOo00o == 9022 :
 I1iiii11IiI1 ( )
elif OooOo00o == 9023 :
 IiiIi ( )
elif OooOo00o == 9024 :
 O0oO00O000o0O ( O0O00Oo )
elif OooOo00o == 9030 :
 OOoOOo0oOO ( O0O00Oo )
elif OooOo00o == 9031 :
 oOOoOoO0OOO0oO ( O0O00Oo )
elif OooOo00o == 9032 :
 Oo0oO ( O0O00Oo )
elif OooOo00o == 9033 :
 Oo00o ( O0O00Oo )
elif OooOo00o == 9034 :
 iiOOO0oOOoo ( )
elif OooOo00o == 7085 :
 o0ooOoOO0 ( O0O00Oo )
elif OooOo00o == 7086 :
 I1i1IIIIIII ( O0O00Oo )
elif OooOo00o == 7087 :
 OOo00oO0OOo ( o0OO0oOo00Oo0o0Oo )
elif OooOo00o == 9666 :
 o00O0O ( O0O00Oo )
elif OooOo00o == 10100 : iI11Iii1ii111 ( )
elif OooOo00o == 101001 : Oo0ooo00OoO ( O0O00Oo )
elif OooOo00o == 10105 : iIi1 ( O0O00Oo )
elif OooOo00o == 10106 : iiiIIIIiI1iiI ( O0O00Oo )
elif OooOo00o == 10104 : OOoOOo ( O0O00Oo )
elif OooOo00o == 10107 : Iiii1I1I111i1 ( )
elif OooOo00o == 10103 : i1IO00oO0oOOOOOO ( O0O00Oo )
elif OooOo00o == 10108 : ii11 ( O0O00Oo )
elif OooOo00o == 10000 : Origin_Menu ( )
elif OooOo00o == 10001 : iIIIi1i1I11i ( )
elif OooOo00o == 10002 : O0Oooo ( )
elif OooOo00o == 10003 : O00oOo0o0 ( )
elif OooOo00o == 10004 : oOOoooO ( O0O00Oo )
elif OooOo00o == 10005 : oO00OoOO ( )
elif OooOo00o == 10006 : ooO ( O0O00Oo )
elif OooOo00o == 10007 : o0oO00oooo ( O0O00Oo , oo00O00oO000o )
elif OooOo00o == 10008 : OOoOo00O0 ( )
elif OooOo00o == 10009 : IIIIOo0oO ( )
elif OooOo00o == 10010 : I1IiII ( O0O00Oo )
elif OooOo00o == 10011 : ooOOO0Oo ( O0O00Oo )
elif OooOo00o == 10012 : OooO0OO ( O0O00Oo )
elif OooOo00o == 10113 : GRABG ( O0O00Oo , OOoO )
elif OooOo00o == 10109 : III1Iii1i ( O0O00Oo )
elif OooOo00o == 10013 : oo0ooo ( O0O00Oo )
elif OooOo00o == 10014 : O0oO00oO0o00o ( )
elif OooOo00o == 10015 : iI1111iiI1 ( )
elif OooOo00o == 10016 : IiiiI ( O0O00Oo )
elif OooOo00o == 10017 : oO000O ( )
elif OooOo00o == 10018 : o0OoOoOo0O ( )
elif OooOo00o == 10019 : IIIii111i ( )
elif OooOo00o == 10020 : i11IiIiii ( )
elif OooOo00o == 10021 : oOOO00o00 ( )
elif OooOo00o == 10022 : OoO0000O ( O0O00Oo )
elif OooOo00o == 10023 : IIiIiii ( OOoO , O0O00Oo )
elif OooOo00o == 10024 : I1iiIIii ( O0O00Oo )
elif OooOo00o == 10025 : O000OOO0OOo ( )
elif OooOo00o == 10026 : iiI1II ( )
elif OooOo00o == 10027 : i11111 ( )
elif OooOo00o == 10028 : OoI1 ( )
elif OooOo00o == 10029 : O0OOoO ( )
elif OooOo00o == 423 : OoOO00OO0 ( O0O00Oo )
elif OooOo00o == 426 : i11IIi1Iii1 ( O0O00Oo )
elif OooOo00o == 10030 : Izle_Films ( )
elif OooOo00o == 10031 : Latest_Izle_Movies ( )
elif OooOo00o == 10032 : Izle_Genres ( )
elif OooOo00o == 10033 : Izle_Pop_Movies ( )
elif OooOo00o == 10034 : Izle_Boxsets ( )
elif OooOo00o == 10035 : Izle_Search ( )
elif OooOo00o == 10036 : Izle_Genres_Movie ( O0O00Oo )
elif OooOo00o == 10037 : Izle_Boxset_single ( O0O00Oo )
elif OooOo00o == 10038 : Izle_IFRAME ( )
elif OooOo00o == 10039 : Izle_Boxsets_Next ( O0O00Oo )
elif OooOo00o == 10040 : oo00ooOoO00 ( )
elif OooOo00o == 10041 : I1O0oO0oo0oOO ( O0O00Oo )
elif OooOo00o == 10042 : IIIII11 ( O0O00Oo )
elif OooOo00o == 10043 : IiIIII ( )
elif OooOo00o == 10044 : IIio0 ( O0O00Oo )
elif OooOo00o == 10045 : iI111iI11iII ( OOoO )
elif OooOo00o == 10046 : ooo0OOoo ( O0O00Oo )
elif OooOo00o == 10047 : I11iI11i1i1 ( O0O00Oo )
elif OooOo00o == 10048 : i11i1ii ( O0O00Oo )
elif OooOo00o == 10049 : Ooooo ( O0O00Oo )
elif OooOo00o == 10050 : O0O0Oooo0o ( )
elif OooOo00o == 10051 : oOOO0o00 ( )
elif OooOo00o == 10052 : O00ooi1i1iIiiI1Ii1 ( )
elif OooOo00o == 10053 : Addon ( O0O00Oo )
elif OooOo00o == 10054 : IIiO0 ( O0O00Oo , OOoO )
elif OooOo00o == 10055 :
 OOo00oOo ( "addFavorite" )
 try :
  OOoO = OOoO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OOoO = OOoO . split ( '  - ' ) [ 0 ]
 except :
  pass
 oOI1ii11IiI1I ( OOoO , O0O00Oo , oo00O00oO000o , oooOo0OOOoo0 , IiIIooOoo0 )
elif OooOo00o == 10056 :
 OOo00oOo ( "rmFavorite" )
 try :
  OOoO = OOoO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OOoO = OOoO . split ( '  - ' ) [ 0 ]
 except :
  pass
 OoooO0 ( OOoO )
elif OooOo00o == 10057 :
 OOo00oOo ( "getFavorites" )
 i1II1i1iiI1 ( )
elif OooOo00o == 10058 : oOO00OO0o0O ( )
elif OooOo00o == 10059 : Donators_Guide ( )
elif OooOo00o == 10060 : iiIiii1iI1i ( )
elif OooOo00o == 10061 : IIiII11 ( )
elif OooOo00o == 10062 : oOIIIi11 ( OOoO , O0O00Oo , o0OO0oOo00Oo0o0Oo )
elif OooOo00o == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif OooOo00o == 10064 : OOoO0O000O ( )
elif OooOo00o == 10065 : OO0OOOOo0000O ( O0O00Oo )
elif OooOo00o == 10066 : OoO0OOoO0Oo0 ( O0O00Oo )
elif OooOo00o == 10068 : O0OoOO0oo0 ( O0O00Oo )
elif OooOo00o == 10069 : OoO ( O0O00Oo )
elif OooOo00o == 10070 : I1iIiiiI1 ( O0O00Oo )
elif OooOo00o == 10071 : Genie_Watch ( )
elif OooOo00o == 10072 : i1I ( )
elif OooOo00o == 10073 : OooOoOO0OO ( O0O00Oo )
elif OooOo00o == 10074 : ii1O0ooooo000 ( O0O00Oo )
elif OooOo00o == 10075 : i11i ( oo00O00oO000o , OOoO , O0O00Oo )
elif OooOo00o == 10076 : OoooooOo ( O0O00Oo )
elif OooOo00o == 10077 : IiI1II11ii1ii ( O0O00Oo )
elif OooOo00o == 10078 : iI1I1 ( )
elif OooOo00o == 10079 : Genie_Watch_Tv_Shows ( )
elif OooOo00o == 10080 : Genie_Watch_Tv_Genre ( O0O00Oo )
elif OooOo00o == 10081 : Genie_Watch_TV_PlayRun ( O0O00Oo )
elif OooOo00o == 10082 : Genie_Watch_TV_Episodes ( O0O00Oo , oo00O00oO000o )
elif OooOo00o == 10083 : Genie_Watch_Tv_Recent ( O0O00Oo )
elif OooOo00o == 10084 : oooO0 ( )
elif OooOo00o == 10085 : oo0OOo0 ( )
elif OooOo00o == 10086 : O0 ( )
elif OooOo00o == 20000 : oOO0OO0OO ( )
elif OooOo00o == 20001 : I1I11I ( O0O00Oo )
elif OooOo00o == 20002 : iiIiiiIii11i1 ( O0O00Oo )
elif OooOo00o == 20003 : oooOoO0oo0o0 ( O0O00Oo )
elif OooOo00o == 20004 : IIiIIiI1iIII ( O0O00Oo )
elif OooOo00o == 20005 : ooIii ( O0O00Oo )
elif OooOo00o == 21004 : I11IIiIiI ( )
elif OooOo00o == 21005 : iiII1II11i ( O0O00Oo )
elif OooOo00o == 21006 : ooO0 ( O0O00Oo )
elif OooOo00o == 21007 : i1ii11 ( O0O00Oo )
elif OooOo00o == 21008 : O0O0ooOOO ( O0O00Oo )
elif OooOo00o == 21009 : iiIiI1i1 ( O0O00Oo )
elif OooOo00o == 30000 : i1oo ( )
elif OooOo00o == 30001 : i11iiIi ( )
elif OooOo00o == 100121 : Resolve ( O0O00Oo )
elif OooOo00o == 30003 : iiI1ii1i1 ( )
elif OooOo00o == 30004 : o0o00O0oOOo ( O0O00Oo )
elif OooOo00o == 30005 : OOI1III1I11I1 ( O0O00Oo )
elif OooOo00o == 30006 : OOoooIIII ( )
elif OooOo00o == 30007 : oOOo0OOoOO0 ( )
elif OooOo00o == 30008 : Iii111Ii ( O0O00Oo )
elif OooOo00o == 30009 : iIiIi1i1Iiii ( O0O00Oo )
elif OooOo00o == 30010 : O0oOoo00Oo0O ( O0O00Oo )
elif OooOo00o == 30011 : I11IiIi1iI1ii ( )
elif OooOo00o == 30012 : II11I ( )
elif OooOo00o == 30013 : IiiiI11 ( )
elif OooOo00o == 30014 : o00o0o0oOo0 ( )
elif OooOo00o == 30015 : i1iIi11i ( O0O00Oo , oo00O00oO000o , oooOo0OOOoo0 )
elif OooOo00o == 30016 : iiIi1 ( O0O00Oo )
elif OooOo00o == 30019 : OoOo0o0O0o0 ( O0O00Oo )
elif OooOo00o == 30017 : oOOo0O00o0O0 ( O0O00Oo )
elif OooOo00o == 30018 : iioOO ( O0O00Oo )
elif OooOo00o == 30030 : IIi1IIII ( )
elif OooOo00o == 30031 : iiiIIiiIi ( )
elif OooOo00o == 30032 : I1i11111i1i11 ( )
elif OooOo00o == 30033 : IiOo0ooooO0o00 ( )
elif OooOo00o == 30034 : iIIIIIi11Ii ( )
elif OooOo00o == 30035 : IiOO0oo00OOo ( O0O00Oo )
elif OooOo00o == 30036 : OoOo00oOoO ( O0O00Oo )
elif OooOo00o == 30037 : Oo0O00o0O0 ( O0O00Oo )
elif OooOo00o == 30038 : i1i11II1 ( )
elif OooOo00o == 30039 : iI ( )
elif OooOo00o == 50000 : Iii1I1111ii ( )
elif OooOo00o == 50001 : oO0o000oOO ( )
elif OooOo00o == 50002 : oO0OO ( O0O00Oo )
elif OooOo00o == 50003 : Table_Menu ( o0OO0oOo00Oo0o0Oo )
elif OooOo00o == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif OooOo00o == 60001 : I11OOO0 ( )
elif OooOo00o == 60002 : i1ii1i1Ii11 ( OOoO )
elif OooOo00o == 60003 : iiIiI11IiI1ii ( O0O00Oo )
elif OooOo00o == 600033 : OoO000oo000o0 ( O0O00Oo )
elif OooOo00o == 60004 : Iiiii1Iii1I ( O0O00Oo )
elif OooOo00o == 50004 : o0OO0 ( )
elif OooOo00o == 50005 : speedtest . runtest ( O0O00Oo )
elif OooOo00o == 70001 : oOo0OOoo0o ( )
elif OooOo00o == 70002 : iIII11I ( O0O00Oo )
elif OooOo00o == 70003 : II1o0OoooOO00o ( O0O00Oo )
elif OooOo00o == 70004 : iIiIiiIIIi1 ( O0O00Oo )
elif OooOo00o == 70005 : i1Ii1i111IIiIi1I ( O0O00Oo )
elif OooOo00o == 70006 : oo00Oo0oO00Oo ( )
elif OooOo00o == 50006 : oooO ( i1 , i1111 )
elif OooOo00o == 80000 : iI1I ( )
elif OooOo00o == 80001 : resolvefilmon ( O0O00Oo )
elif OooOo00o == 80002 : II111iii ( )
elif OooOo00o == 80003 : oOiiIIIII ( OOoO , O0O00Oo , "None" )
elif OooOo00o == 80004 : IiIii11ii111 ( OOoO , O0O00Oo )
elif OooOo00o == 80005 : II1iiiiII ( )
elif OooOo00o == 80006 : i1iiiiI1IiIIii ( O0O00Oo )
elif OooOo00o == 80007 : IIIIiii ( O0O00Oo )
elif OooOo00o == 80008 : Ii11Ii1iI ( )
elif OooOo00o == 80009 : oo00ooOOOo0O ( )
elif OooOo00o == 80010 : i11111i1I1IiI ( O0O00Oo )
elif OooOo00o == 80011 : I1IIo0o0OoOO00Oo ( O0O00Oo )
elif OooOo00o == 80012 : II1iIIiI ( )
elif OooOo00o == 90000 : ooOOOoO0 ( OOoO , O0O00Oo )
elif OooOo00o == 90001 : tools ( )
elif OooOo00o == 90002 : Oo00o0OO0O00o ( )
elif OooOo00o == 90003 : o0iiI11 ( O0O00Oo )
elif OooOo00o == 90004 : IiiiIII1i ( O0O00Oo )
elif OooOo00o == 90005 : OOooo0o0oOO0 ( O0O00Oo )
elif OooOo00o == 90006 : OO00 ( O0O00Oo )
elif OooOo00o == 90007 : iI1iII1 ( O0O00Oo )
elif OooOo00o == 90008 : ooO00OoIIiI1iiIII1 ( O0O00Oo )
elif OooOo00o == 90009 : OooOoOo ( O0O00Oo )
elif OooOo00o == 90010 : i1I1i111Ii ( )
elif OooOo00o == 90020 : oOO0ooo0O ( )
elif OooOo00o == 90021 : hellyeah2 ( O0O00Oo )
elif OooOo00o == 90022 : hellyeah3 ( O0O00Oo )
elif OooOo00o == 90023 : oOo0O0O0 ( )
elif OooOo00o == 90024 : o0OO0Oo ( O0O00Oo )
elif OooOo00o == 90025 : iiiiI1iiiIi ( O0O00Oo )
if 47 - 47: i1iIi - oOo0O0Ooo % oooOo0oo0oo * o0ii1I % oOo0O0Ooo
elif OooOo00o == 90026 : III11I11ii ( )
elif OooOo00o == 90027 : o0oOoO00 ( OOoO , o0OO0oOo00Oo0o0Oo )
if 95 - 95: oO0o + OOooOOo % I1ii11iIi11i . o0ii1I * oOo0O0Ooo + i1IiiiI1iI
elif OooOo00o == 900300 : o0oooOO00 ( )
elif OooOo00o == 900301 : iiIiii1IIIII ( O0O00Oo )
elif OooOo00o == 900302 : oo00o0 ( O0O00Oo )
elif OooOo00o == 90030 : II1iIi11 ( )
elif OooOo00o == 90031 : I1III1111iIi ( )
elif OooOo00o == 90032 : I1i111I ( O0O00Oo )
elif OooOo00o == 90033 : OooOo0oo0O0o00O ( O0O00Oo )
elif OooOo00o == 90034 : OOOooo ( O0O00Oo )
elif OooOo00o == 90035 : o0OOo0o0O0O ( O0O00Oo )
elif OooOo00o == 90036 : OOO0 ( O0O00Oo )
elif OooOo00o == 90039 : o0oo00 ( O0O00Oo )
elif OooOo00o == 90037 : OOo00OoO ( O0O00Oo )
elif OooOo00o == 900377 : iIOo0O ( O0O00Oo )
elif OooOo00o == 90038 : I1Ii11iiiI ( )
if 22 - 22: I1ii11iIi11i . oO0o
elif OooOo00o == 10090 : OoOo0oOooOoOO ( )
elif OooOo00o == 10091 : Ii11II11iI1 ( O0O00Oo )
elif OooOo00o == 10092 : o0OO0OOOOOoOOOOooo ( O0O00Oo )
elif OooOo00o == 10093 : oOO00 ( O0O00Oo , oo00O00oO000o )
elif OooOo00o == 10094 : O00o ( O0O00Oo , oo00O00oO000o )
if 55 - 55: I1ii11iIi11i % ii * IIiIiII11i % ii
elif OooOo00o == 10095 : o0O0O0ooo0oOO ( )
elif OooOo00o == 10096 : iIIi1iI1 ( O0O00Oo )
elif OooOo00o == 10097 : O00 ( O0O00Oo )
elif OooOo00o == 10098 : o0oOOO0 ( O0O00Oo )
elif OooOo00o == 10099 : I1iIIII1 ( O0O00Oo )
if 30 - 30: i1IiiiI1iI / I11i + ii + OOooOOo + oO0o
elif OooOo00o == 10200 : O0o ( )
elif OooOo00o == 10201 : i11ii ( O0O00Oo )
elif OooOo00o == 10202 : I1iI1I1 ( O0O00Oo )
elif OooOo00o == 10203 : RT4 ( O0O00Oo )
if 40 - 40: ii / III1iiIii
elif OooOo00o == 90040 : III1iii1i1II ( )
elif OooOo00o == 90041 : o0oo0Ooooo0 ( O0O00Oo )
elif OooOo00o == 90042 : i1iIiIii ( O0O00Oo )
elif OooOo00o == 90043 : i1III1iI ( O0O00Oo )
elif OooOo00o == 90044 : oo0OoOOooO ( O0O00Oo )
elif OooOo00o == 90045 : iiiii11I1 ( )
elif OooOo00o == 90046 : o0o0OO0o00o0O ( O0O00Oo )
elif OooOo00o == 90050 : O0o00o000oO ( )
elif OooOo00o == 90051 : oooo ( O0O00Oo )
elif OooOo00o == 90052 : O0Oo0 ( O0O00Oo )
elif OooOo00o == 90053 : II1Ii ( O0O00Oo )
elif OooOo00o == 90054 : oooO00Oo ( O0O00Oo )
elif OooOo00o == 90055 : IIii1i11iI1II11 ( )
if 82 - 82: Ii - i1i1I1IIii1II - ooOoO0O00
elif OooOo00o == 100001 : Stand_up ( )
if 78 - 78: i1i1I1IIii1II % IiI1i11I / ooOoO0O00 / i1iIi
elif OooOo00o == 100003 : IiiiI ( O0O00Oo )
elif OooOo00o == 100004 : Ooo0o0OOO ( O0O00Oo )
elif OooOo00o == 100005 : Resolve ( O0O00Oo )
elif OooOo00o == 100008 : Search ( )
elif OooOo00o == 100007 : iI1IIIii ( O0O00Oo )
elif OooOo00o == 100009 : yt . PlayVideo ( O0O00Oo )
elif OooOo00o == 100010 : i1i1i1I ( O0O00Oo )
elif OooOo00o == 100100 : ii1Ii1IiIIi ( oo00O00oO000o , O0O00Oo , oOOo0oOoooO0o )
elif OooOo00o == 100101 : iiIi ( O0O00Oo , OOoO , oooOo0OOOoo0 , oOOo0oOoooO0o , oo00O00oO000o )
elif OooOo00o == 100102 : iiI11I1i1i1iI ( OOoO , O0O00Oo , oo00O00oO000o , oooOo0OOOoo0 )
elif OooOo00o == 100106 : i111I ( O0O00Oo , OOoO )
elif OooOo00o == 100107 : I11I1IIiiII1 ( )
elif OooOo00o == 100108 : i1i1I11I ( )
elif OooOo00o == 100109 : o00O0oOooOoO ( O0O00Oo )
elif OooOo00o == 40000 : OoO0O0oo0o ( )
elif OooOo00o == 40001 : i1iIii1i111 ( O0O00Oo )
elif OooOo00o == 100110 : o0oOO00 ( )
elif OooOo00o == 100111 : ii11iiIi ( O0O00Oo )
elif OooOo00o == 100110 : o0oOO00 ( )
elif OooOo00o == 100210 : Oo00OOo ( O0O00Oo )
elif OooOo00o == 100211 : Iii1i11iiI1 ( )
elif OooOo00o == 100212 : oOoO0OOO00O ( )
elif OooOo00o == 100213 : iIiIi1Ii1Ii1IIIi ( )
elif OooOo00o == 100214 : ooOOO00oOOooO ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
