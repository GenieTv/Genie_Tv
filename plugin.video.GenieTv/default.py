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
IiiIII111iI = "3.5.0"
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
  oooO ( 'Change Log 16/3/17 - v3.4.8' , 'All Categories In GTV Live Lists Updated,[CR]BamfTv Added To StreamTeam,[CR] Pirate Movies Added To StreamTeam,[CR]GenieTv Now Krypton Compatible,[CR] G.O.D.S (GenieTv On Demand Soaps) Added To GenieTv,[CR] RaysRavers And RaizTv Updated,[CR] More Sections Now Available For Download Including Kids,[CR] Tv Guide Removed And Replaced By External App,[CR] Boss Documentaries A Masterpiece By Jason Cadd,[CR] Updates To All Searches,[CR] StreamTeam Cleaned Up,[CR] Addon Overall CleanUp,[CR] General Maintence' )
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
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0' ) ) , 90037 , iiIi1IIiIi + 'raiztv.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , iiIi1IIiIi + 'bamftv.png' , Oo00OOOOO , '' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']PIRATE MOVIES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , 1016 , iiIi1IIiIi + 'pirate.png' , Oo00OOOOO , '' )
  if 31 - 31: Iii . i1IiiiI1iI * i1iIi + Ii * i1i1I1IIii1II
  if 93 - 93: Ii1I / iI11I1II1I1I * ooOoO0O00 % ii * o0o00Oo0O * Iii
  if 64 - 64: IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / I1ii11iIi11i . i1iIi % III1iiIii
  if 50 - 50: iI11I1II1I1I - III1iiIii + oooOo0oo0oo
  if 69 - 69: o0o00Oo0O
  if 85 - 85: i1iIi / o0o00Oo0O
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 18 - 18: I11i % o0o00Oo0O * Ii1I
def o0Iii ( ) :
 iii ( )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , iiIi1IIiIi + 'SilentHunter.png' , Oo00OOOOO , '' )
def o00oO ( url ) :
 I11iiii = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( I11iiii )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( I1iiiiI1iI ) )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( I1iiiiI1iI ) )
 IiIi1I1 = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( I1iiiiI1iI ) )
 for OOoO , iIiIi11 , url in IIi :
  if '247ch' in url :
   iIiiiii1i ( OOoO , url , 10190 , iIiIi11 )
  elif '.m3u' in url :
   iIiiiii1i ( OOoO , url , 1019 , iIiIi11 )
  elif '.xml' in url :
   iIiiiii1i ( OOoO , url , 1018 , iIiIi11 )
  else :
   iiIi1IIiI ( OOoO , url , 222 , iIiIi11 )
 for OOoO , url , iIiIi11 in i1Iii1i1I :
  if '.xml' in url :
   iIiiiii1i ( OOoO , url , 1018 , iIiIi11 )
  elif '.m3u' in url :
   iIiiiii1i ( OOoO , url , 1019 , iIiIi11 )
  else :
   iiIi1IIiI ( OOoO , url , 222 , iIiIi11 )
 for OOoO , url , iIiIi11 in IiIi1I1 :
  iiIi1IIiI ( OOoO , url , 8043 , iIiIi11 )
def i1oO0OO0 ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'BAMFTV.png' )
def O0Oo0o000oO ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url , iIiIi11 in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iIiIi11 )
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
 for OOoO , url , oO0oOOoo00000 , oOo00 , oooOo0OOOoo0 , OOOiiiiI in IIi :
  if oOo00 == '123' :
   oOo00 = iiIi1IIiIi + 'appstreams.png'
  if oooOo0OOOoo0 == '123' :
   oooOo0OOOoo0 = iiIi1IIiIi + 'appstreams.png'
  if 'php' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100010 , oOo00 , oooOo0OOOoo0 , OOOiiiiI )
  elif 'playlist' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100007 , oOo00 , oooOo0OOOoo0 , OOOiiiiI )
  elif 'watchseries' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100100 , oOo00 , oooOo0OOOoo0 , OOOiiiiI )
  elif not 'http' in url :
   i1iI11i1IIi ( OOoO , url , 100009 , oOo00 , oooOo0OOOoo0 , OOOiiiiI , '' )
  else :
   i1iI11i1IIi ( OOoO , url , 100005 , oOo00 , oooOo0OOOoo0 , OOOiiiiI , '' )
   if 4 - 4: ii - Ii1I * oOo0O0Ooo
def I1iIiI11I1 ( url ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
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
   i1iI11i1IIi ( OOoO , url , 100009 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI , '' )
  else :
   i1iI11i1IIi ( OOoO , url , 100005 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI , '' )
   if 27 - 27: o0ii1I . Ii % i1IiiiI1iI
def Oo ( url ) :
 if 81 - 81: i1i1I1IIii1II * oO0o
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 iI11I = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1iiiiI1iI in iI11I :
  oOo00 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( I1iiiiI1iI ) )
  for oOo00 in oOo00 :
   oOo00 = oOo00
  OOoO = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( I1iiiiI1iI ) )
  for OOoO in OOoO :
   if 'elete' in OOoO :
    pass
   elif 'rivate Vid' in OOoO :
    pass
   else :
    OOoO = ( OOoO ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  I1IIIiii1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( I1iiiiI1iI ) )
  for I1IIIiii1 in I1IIIiii1 :
   I1IIIiii1 = I1IIIiii1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( I1iiiiI1iI ) )
  for url in url :
   url = url
  i1iI11i1IIi ( '[COLORred]' + str ( I1IIIiii1 ) + '[/COLOR] : ' + str ( OOoO ) , str ( url ) , 100009 , str ( oOo00 ) , Oo00OOOOO , '' , '' )
  oOI1Ii1I1 ( 'movies' , '' )
  if 65 - 65: Iii / IIiIiII11i * o0ii1I . IiI1i11I * i1i1I1IIii1II % oooOo0oo0oo
  if 69 - 69: i1iIi - oO0o / Ii + Ii1I % ii
  if 73 - 73: o0ii1I - i1IiiiI1iI
  if 68 - 68: IiI1i11I * ii * iI11I1II1I1I . IIiIiII11i
def O0Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oOOo0O00o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOOiiiiI , oooOo0OOOoo0 , OOoO in oOOo0O00o :
  if '.php' in url :
   Iii1I1I11iiI1 ( OOoO , url , 100210 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  else :
   iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
   if 36 - 36: o0ii1I / IIiIiII11i / III1iiIii / III1iiIii + Ii1I
   if 95 - 95: III1iiIii
   if 51 - 51: IIiIiII11i + III1iiIii . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
def OOoOoo0 ( iconimage , url , extra ) :
 oOo00 = ' '
 I1iIII1 = ' '
 oooOo0OOOoo0 = ' '
 iIii = ' '
 oOo0OoOOo0 = O0i11i1iiI1i ( url )
 oOo00 = re . compile ( '<img src="(.+?)">' ) . findall ( oOo0OoOOo0 )
 for oOo00 in oOo00 :
  oOo00 = oOo00
 iII11I1Ii1 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( oOo0OoOOo0 )
 for oooOo0OOOoo0 in iII11I1Ii1 :
  oooOo0OOOoo0 = oooOo0OOOoo0
 IIi = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( oOo0OoOOo0 )
 for url , iIii in IIi :
  iIii = 'S' + ( iIii ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oOOoo0Oo + url
  o0o0 ( ( iIii ) . replace ( '  ' , '' ) , url , 100101 , oOo00 , oooOo0OOOoo0 , I1iIII1 , '' )
  oOI1Ii1I1 ( 'Movies' , 'info' )
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
  ooo = name + ' - [COLORred]' + I1i + '[/COLOR]'
  o0o0 ( ooo , url , 100102 , oOo00 , fanart , 'Aired : ' + I1i , ooo )
  if 20 - 20: ooOoO0O00 - Iii
def ii1ii11 ( name , URL , iconimage , fanart ) :
 II11iIiIIIiI = O0i11i1iiI1i ( URL )
 IIi = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , name in IIi :
  for iII1i11 in o00OO00OoO :
   if iII1i11 in O0O00Oo :
    URL = 'http://www.watchseriesgo.to/link/' + O0O00Oo
    i1iI11i1IIi ( name , URL , 100106 , iiIi1IIiIi + 'appstreams.png' , Oo00OOOOO , '' , '' )
 if len ( IIi ) <= 0 :
  o0o0 ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 84 - 84: o0o00Oo0O . Iii - IIiIiII11i . i1iIi / IIiIiII11i
  if 47 - 47: ii
def ii1i1i1IiII ( url , name ) :
 O0oII11I = name
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  oo0oOO00oO ( url , O0oII11I )
 for url in i1Iii1i1I :
  oo0oOO00oO ( url , O0oII11I )
 for url in IiIi1I1 :
  oo0oOO00oO ( url , O0oII11I )
  if 36 - 36: oooOo0oo0oo
def oo0oOO00oO ( url , season_name ) :
 if 'daclips.in' in url :
  O0oii111 ( url , season_name )
 elif 'filehoot.com' in url :
  O0OO0oOoO0O0O ( url , season_name )
 elif 'allmyvideos.net' in url :
  oo000oOo0 ( url , season_name )
 elif 'vidspot.net' in url :
  iIiI1I1Ii ( url , season_name )
 elif 'vodlocker' in url :
  III ( url , season_name )
 elif 'vidto' in url :
  iIiIi11Ii ( url , season_name )
  if 23 - 23: i1i1I1IIii1II - oooOo0oo0oo + Iii
  if 12 - 12: oOo0O0Ooo / i1iIi % I11i / Ii % ii
def iIiIi11Ii ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi1II11i , OOoO in IIi :
  II1II1iIIi11 ( IiIi1II11i , season_name )
  if 49 - 49: ii * Iii - I1ii11iIi11i . i1i1I1IIii1II
  if 89 - 89: i1iIi + o0ii1I * i1iIi / i1iIi
def oo000oOo0 ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi1II11i , OOoO in IIi :
  II1II1iIIi11 ( IiIi1II11i , season_name )
  if 46 - 46: oO0o
def iIiI1I1Ii ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( II11iIiIIIiI )
 for IiIi1II11i , OOoO in IIi :
  II1II1iIIi11 ( IiIi1II11i , season_name )
  if 71 - 71: Iii / Iii * i1i1I1IIii1II * i1i1I1IIii1II / IIiIiII11i
def III ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi1II11i in IIi :
  II1II1iIIi11 ( IiIi1II11i , season_name )
  if 35 - 35: oooOo0oo0oo * I11i * oOo0O0Ooo % I1ii11iIi11i . OOooOOo
def O0oii111 ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( II11iIiIIIiI )
 for IiIi1II11i in IIi :
  II1II1iIIi11 ( IiIi1II11i , season_name )
  if 58 - 58: Iii + IIiIiII11i * IiI1i11I * Ii - iI11I1II1I1I
def O0OO0oOoO0O0O ( url , season_name ) :
 II11iIiIIIiI = O0i11i1iiI1i ( url )
 IIi = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IiIi1II11i in IIi :
  II1II1iIIi11 ( IiIi1II11i , season_name )
  if 68 - 68: ii % IIiIiII11i
def II1II1iIIi11 ( Link , season_name ) :
 if 'http:/' in Link :
  Ii1i1i1111 ( Link )
  if 57 - 57: o0ii1I % IIiIiII11i
def O00oOo ( url ) :
 II11iIiIIIiI = OPEN_URL_1 ( url )
 I1111I1II11 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 for url in I1111I1II11 :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 30 - 30: ii % ii
def o0o0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oooooOo0 = [ ]
  if 54 - 54: i1iIi % oooOo0oo0oo . i1IiiiI1iI + i1i1I1IIii1II - oooOo0oo0oo * oOo0O0Ooo
  if showcontext == 'fav' :
   oooooOo0 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oooooOo0 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  I1iiii . addContextMenuItems ( oooooOo0 )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = True )
 return ii1II
 if 92 - 92: I11i + i1IiiiI1iI / I1ii11iIi11i % oO0o % III1iiIii . ii
 if 52 - 52: i1iIi / Ii - oooOo0oo0oo . III1iiIii % iI11I1II1I1I + I11i
def i1iI11i1IIi ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oooooOo0 = [ ]
  oooooOo0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oooooOo0 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oooooOo0 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  I1iiii . addContextMenuItems ( oooooOo0 )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = False )
 return ii1II
 if 71 - 71: i1i1I1IIii1II % Iii * OOooOOo . o0o00Oo0O / o0ii1I . Ii1I
def oOOOo ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 68 - 68: i1i1I1IIii1II - Ii1I % o0o00Oo0O % i1IiiiI1iI
def Ii1II ( url ) :
 ooO0O0o0 = xbmc . Player ( OO0OOooOO0 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : ooO0O0o0 . play ( url ) . strip ( )
 except : pass
 if 31 - 31: oOo0O0Ooo * i1i1I1IIii1II + ii - IiI1i11I / ii
def Ii1i1i1111 ( url ) :
 ooO0O0o0 = xbmc . Player ( )
 import urlresolver
 try : ooO0O0o0 . play ( url )
 except : pass
 if 19 - 19: III1iiIii * i1iIi * I11i + o0o00Oo0O / o0o00Oo0O
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
  if 73 - 73: iI11I1II1I1I / iI11I1II1I1I - i1i1I1IIii1II
  if 91 - 91: i1i1I1IIii1II + oOo0O0Ooo
  if 59 - 59: oOo0O0Ooo + Ii + ooOoO0O00 / Iii
def iiIi1i ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MORE CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANIME LAND[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Kids[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   I11iIiI1 ( )
  if o0Oo00 == 1 :
   oo0oooOo ( )
  if o0Oo00 == 2 :
   o0OO0O0Oo ( )
  if o0Oo00 == 3 :
   OOOOO ( )
  if o0Oo00 == 4 :
   OOoOOo0O00O ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
 if 36 - 36: o0o00Oo0O + I1ii11iIi11i
 if 5 - 5: I1ii11iIi11i * OOooOOo
 if 46 - 46: i1iIi
def I11IiI ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIi = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( II11iIiIIIiI )
 for II1I in IIi :
  II1I = ( str ( II1I ) )
  if os . path . exists ( xbmc . translatePath ( II1I ) ) :
   I11iIiII = ( II1I ) . replace ( 'special://home/addons/' , '' )
   oooO ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + I11iIiII + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   o0Oo00 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if o0Oo00 == 0 :
    OO0OO0OO ( II1I )
    ii1iii1i ( )
   elif o0Oo00 == 1 :
    OoooO0o ( II1I )
  else :
   pass
   if 24 - 24: OOooOOo % ooOoO0O00 + IiI1i11I . Ii . Ii1I
def OoooO0o ( addon ) :
 I11iIiII = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 17 - 17: Ii1I . IIiIiII11i . i1iIi / Ii1I
def OO0OO0OO ( addon ) :
 iIii1 . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 oOooO00o0O = os . path . join ( IIIII , 'default.py' )
 OOo0 = open ( oOooO00o0O , "w+" )
 if 35 - 35: ooOoO0O00 - iI11I1II1I1I + ooOoO0O00
 OOo0 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 OOo0 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 OOo0 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 86 - 86: iI11I1II1I1I + OOooOOo . Ii - o0ii1I
 if 51 - 51: OOooOOo
 if 14 - 14: III1iiIii % i1i1I1IIii1II % I1ii11iIi11i - Ii
 if 53 - 53: o0ii1I % I1ii11iIi11i
def OOo00OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O0ooOo0o0Oo = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OooO0oOo = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1i11 = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oOOo00O0OOOo = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url , i11I1I1iiI , oooOo0OOOoo0 , OOOiiiiI in O0ooOo0o0Oo :
  if 'php' in url :
   Iii1I1I11iiI1 ( OOoO , url , 90037 , i11I1I1iiI , oooOo0OOOoo0 , OOOiiiiI )
  elif OOoO == 'Search' :
   Iii1I1I11iiI1 ( 'Search' , url , 90038 , i11I1I1iiI , oooOo0OOOoo0 , OOOiiiiI )
  else :
   iI1Ii1iI11iiI ( OOoO , url , 222 , i11I1I1iiI , oooOo0OOOoo0 , OOOiiiiI )
 for OOoO , iIiIi11 , url , I1i1iii1Ii in OooO0oOo :
  Iii1I1I11iiI1 ( OOoO , url , 90037 , iIiIi11 , I1i1iii1Ii , '' )
 for OOoO , iIiIi11 , url , I1i1iii1Ii in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 90037 , iIiIi11 , I1i1iii1Ii , '' )
 for OOoO , url , iIiIi11 , I1i1iii1Ii in i1Iii1i1I :
  iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , I1i1iii1Ii , '' )
 for OOoO , url , iIiIi11 , I1i1iii1Ii in IiIi1I1 :
  iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , I1i1iii1Ii , '' )
 for OOoO , url , iIiIi11 , I1i1iii1Ii in I1i11 :
  iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , I1i1iii1Ii , '' )
 for OOoO , url , iIiIi11 in oOOo00O0OOOo :
  iI1Ii1iI11iiI ( OOoO , url , 222 , iIiIi11 , '' , '' )
  oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
  if 23 - 23: Ii
def II1I11IIi ( ) :
 OoOOo = [ 'serialsearch' , 'moviesearch' ]
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 if oOO0oo == '' :
  pass
 else :
  for II1iIi1IiIii in OoOOo :
   I111I11I111 = Oo0o0000o0o0 + II1iIi1IiIii + '.php'
   oOo0OoOOo0 = OooOoooOo ( I111I11I111 )
   if oOo0OoOOo0 != 'Opened' :
    oOOo0O00o = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( oOo0OoOOo0 )
    for OOoO , O0O00Oo , i11I1I1iiI , oooOo0OOOoo0 , OOOiiiiI in oOOo0O00o :
     if oOO0oo in OOoO . lower ( ) :
      iiiiI11ii = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in iiiiI11ii :
       if iII1i11 == O0O00Oo :
        OOoO = '[COLORred]* [/COLOR]' + ( OOoO ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        O0i1i1II1i11 = open ( OOOO0OOoO0O0 , "a" )
        O0i1i1II1i11 . write ( 'item="' + OOoO + '"\n' )
        O0i1i1II1i11 . close
      if 'php' in O0O00Oo :
       Iii1I1I11iiI1 ( OOoO , O0O00Oo , 90037 , i11I1I1iiI , oooOo0OOOoo0 , OOOiiiiI )
      else :
       iI1Ii1iI11iiI ( OOoO , O0O00Oo , 222 , i11I1I1iiI , oooOo0OOOoo0 , OOOiiiiI )
       if 91 - 91: Iii / ooOoO0O00 * ooOoO0O00
   oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
   if 25 - 25: iI11I1II1I1I . oooOo0oo0oo * i1i1I1IIii1II - o0ii1I
def oOO000O ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://www.tvcatchup.com/channels/' )
 o0o = OooOoooOo ( 'http://www.djing.com/' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img style="" src="([^"]*)" alt="([^"]*)"/>.+?<br/>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OoOo0 = re . compile ( 'title="([^"]*)".+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( o0o )
 for O0O00Oo , iIiIi11 , II1i11I1 , OOoO in IIi :
  iiIi1IIiI ( ( '[COLORgold]' + II1i11I1 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + OOoO + '[/COLOR]' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' ) , 'http://www.tvcatchup.com' + O0O00Oo , 90024 , iIiIi11 )
 for I1IIIii , O0O00Oo , iIiIi11 in OoOo0 :
  iiIi1IIiI ( I1IIIii , 'http://www.tvcatchup.com' + O0O00Oo , 90024 , iIiIi11 )
 for O0O00Oo , iIiIi11 , OOoO in i1Iii1i1I :
  if 'Submit' in OOoO :
   pass
  elif '&lt;' in OOoO :
   pass
  else :
   iI1Ii1iI11iiI ( '[COLORgold]DJing  [/COLOR][COLORwhite]- [COLORsteelblue]' + OOoO + '[/COLOR]' , O0O00Oo , 90025 , 'http://www.djing.com' + iIiIi11 , Oo00OOOOO , '' )
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
def iiIiIiII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 if 37 - 37: Iii / III1iiIii + IIiIiII11i
 IIi = re . compile ( "file: '([^']*)'," ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def iiiiiIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<iframe src='([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  ooO00O00oOO ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 40 - 40: IiI1i11I . i1i1I1IIii1II + oOo0O0Ooo + Ii1I + i1IiiiI1iI
def O0o ( ) :
 if 26 - 26: iI11I1II1I1I
 if 87 - 87: Ii1I / ii - I1ii11iIi11i % OOooOOo % III1iiIii % I1ii11iIi11i
 if 29 - 29: ii . oOo0O0Ooo % Ii1I - IiI1i11I
 if 8 - 8: ooOoO0O00
 if 32 - 32: i1i1I1IIii1II / IIiIiII11i
 if 45 - 45: Ii1I + oO0o * Ii / oooOo0oo0oo % Iii * o0o00Oo0O
 II11iIiIIIiI = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'yr' in O0O00Oo :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + O0O00Oo , 10201 , iiIi1IIiIi + 'rated.png' )
   if 17 - 17: o0o00Oo0O
def OOooO0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for ii1iI1iI1 , url , OOoO in IIi :
  if 'id' in url :
   iIiiiii1i ( ( '[COLORred]RANK [COLORblue]' + ii1iI1iI1 + '[COLORred] - [COLORblue]' + OOoO + '[/COLOR]' ) , OOoO , 10202 , iiIi1IIiIi + 'rated.png' )
   if 55 - 55: i1iIi + oooOo0oo0oo
def IIIIIiII1 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iii11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iii1 = ( url )
 oOO0oo = iii1 . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( iii1 ) . replace ( ' ' , '+' )
 i1oO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 iIIi1IIi = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i111i11I1ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OOooooo0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oOOII1i11i1iIi11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oo0O0oO0O0O = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iii1
 oOo0O = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 I11iIiii1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 1 - 1: o0ii1I
 IiiiI1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 OOOo0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 79 - 79: oO0o % oooOo0oo0oo / iI11I1II1I1I + OOooOOo * oO0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( i1oO )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iIIi1IIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( i111i11I1ii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 IiI1 = O00O0oOO00O00 ( OOooooo0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IIiiiiIiIIii = O00O0oOO00O00 ( oo0O0oO0O0O )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O0OO = O00O0oOO00O00 ( oOo0O )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 IIIiIiI = O00O0oOO00O00 ( I11iIiii1 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 7 - 7: III1iiIii . OOooOOo / Ii1I . oooOo0oo0oo * Iii - IIiIiII11i
 if 37 - 37: i1IiiiI1iI . OOooOOo / o0o00Oo0O * IiI1i11I
 III11iiii11i1 = O00O0oOO00O00 ( IiiiI1 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 ooOo0OoO = O00O0oOO00O00 ( OOOo0 )
 if 36 - 36: III1iiIii - ii / oO0o
 if 34 - 34: i1iIi
 if 45 - 45: i1iIi / I1ii11iIi11i / o0ii1I
 if 44 - 44: Ii1I - o0ii1I / IIiIiII11i * oO0o * I1ii11iIi11i
 if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * oooOo0oo0oo % IIiIiII11i
 if 56 - 56: ii * I1ii11iIi11i . I1ii11iIi11i . Ii1I
 if 24 - 24: I1ii11iIi11i . Iii * o0ii1I % IiI1i11I / oooOo0oo0oo
 if 58 - 58: oOo0O0Ooo - Ii1I % o0o00Oo0O . oOo0O0Ooo % oO0o % III1iiIii
 if 87 - 87: i1i1I1IIii1II - Ii
 if 78 - 78: Ii / iI11I1II1I1I - I11i
 if 23 - 23: Iii
 if 40 - 40: I11i - IIiIiII11i / I1ii11iIi11i
 if 14 - 14: Ii1I
 if IIIiIiI != 'Failed' :
  iI1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( IIIiIiI )
  for url , OOoO in iI1 :
   iIIiI1ii = O00O0oOO00O00 ( url )
   oo0OOoOoo0O0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIIiI1ii )
   for iiI11ii1111 , IIiIIiI in oo0OOoOoo0O0O :
    IIiIIiI = ( IIiIIiI . replace ( '.' , ' ' ) )
    if oOO0oo in IIiIIiI . lower ( ) :
     if '.mkv' in iiI11ii1111 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + iiI11ii1111 , 222 , '' , '' , '' )
     elif '.mp4' in iiI11ii1111 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + iiI11ii1111 , 222 , '' , '' , '' )
     elif '.avi' in iiI11ii1111 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + iiI11ii1111 , 222 , '' , '' , '' )
     elif '.wav' in iiI11ii1111 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + iiI11ii1111 , 222 , '' , '' , '' )
     else :
      Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + iiI11ii1111 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 73 - 73: oooOo0oo0oo
      oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for url , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in i1Iii1i1I :
   if iii1 in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 2 - 2: Ii - IIiIiII11i / i1i1I1IIii1II % o0o00Oo0O
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 66 - 66: I1ii11iIi11i
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for I1i1IiI1i , OOoO in IiIi1I1 :
   if iii1 in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIIi1IIi + I1i1IiI1i ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for url , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in I1i11 :
   if iii1 in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 32 - 32: ii - OOooOOo - Ii * I11i / I1ii11iIi11i + ii
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if IiI1 != 'Failed' :
  ii1I1I111 = [ ]
  oOOo00O0OOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiI1 )
  for url , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in oOOo00O0OOOo :
   if iii1 in OOoO . lower ( ) :
    if OOoO in ii1I1I111 :
     pass
    else :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
     ii1I1I111 . append ( OOoO )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if IIiiiiIiIIii != 'Failed' :
  Ii1Ii = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIiiiiIiIIii )
  for url , iIiIi11 , OOoO in Ii1Ii :
   if iii1 in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , iIiIi11 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 39 - 39: i1i1I1IIii1II - ooOoO0O00 / i1iIi . oOo0O0Ooo * ooOoO0O00 - iI11I1II1I1I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: oOo0O0Ooo * I11i % i1iIi . iI11I1II1I1I * i1IiiiI1iI
    if 92 - 92: i1IiiiI1iI - iI11I1II1I1I
    if 32 - 32: o0ii1I % oO0o * oO0o + III1iiIii * IIiIiII11i * o0ii1I
    if 11 - 11: i1i1I1IIii1II % IIiIiII11i
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
    if 38 - 38: i1IiiiI1iI % oooOo0oo0oo - ii
 if III11iiii11i1 != 'Failed' :
  oOo0OOoooO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III11iiii11i1 )
  for url , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in oOo0OOoooO :
   if iii1 in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 26 - 26: I11i * III1iiIii . ooOoO0O00
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
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
 IIii1 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 35 - 35: Ii - oOo0O0Ooo / oooOo0oo0oo + o0ii1I * i1i1I1IIii1II
 for II1iIi1IiIii in IIii1 :
  I111I11I111 = oO0 + II1iIi1IiIii + oOoOooOo0o0
  IIIiIiI = O00O0oOO00O00 ( I111I11I111 )
  if IIIiIiI != 'Failed' :
   iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIiIiI )
   for url , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in iI1 :
    if iii1 in OOoO . lower ( ) :
     iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 49 - 49: I11i * o0ii1I + Iii + IiI1i11I
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
     if 30 - 30: I11i / oooOo0oo0oo / III1iiIii % i1iIi + IIiIiII11i
 IIii1 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 4 - 4: IiI1i11I - I1ii11iIi11i - III1iiIii - Iii % Ii / oO0o
 if 50 - 50: i1iIi + ooOoO0O00
 for II1iIi1IiIii in IIii1 :
  I111I11I111 = iii11 + II1iIi1IiIii
  i11IiIIi11I = O00O0oOO00O00 ( I111I11I111 )
  if i11IiIIi11I != 'Failed' :
   o000o0O0Oo00 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( i11IiIIi11I )
   for I1i1IiI1i , OOoO in o000o0O0Oo00 :
    if iii1 in OOoO . lower ( ) :
     iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iii11 + II1iIi1IiIii + I1i1IiI1i ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 60 - 60: OOooOOo
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: oOo0O0Ooo - oOo0O0Ooo - oOo0O0Ooo * ii
def o0O0O0ooo0oOO ( ) :
 iIiiiii1i ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , iiIi1IIiIi + 'running.png' )
 iIiiiii1i ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , iiIi1IIiIi + 'countdown.png' )
 iIiiiii1i ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , iiIi1IIiIi + 'unknown.png' )
 iIiiiii1i ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , iiIi1IIiIi + 'cancelled.png' )
 oOI1Ii1I1 ( 'tvshows' , 'INFO' )
 if 28 - 28: iI11I1II1I1I + iI11I1II1I1I
def iIiIii1ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , iIii , IIiI1i , I1i , iII1 in IIi :
  iIiiiii1i ( ( '[COLORblue]' + OOoO + '[/COLOR] [COLORred]Season[/COLOR]-' + iIii + ' [COLORred]Returns [/COLOR]- ' + iII1 + ' ' + I1i ) , OOoO , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 70 - 70: IiI1i11I / oooOo0oo0oo % i1iIi - o0ii1I
def i1II11Iii1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , iIii , IIiI1i in IIi :
  iIiiiii1i ( ( '[COLORblue]' + OOoO + '[/COLOR] [COLORred]Season[/COLOR]-' + iIii + ' [COLORred] Status Unknown[/COLOR] ' ) , OOoO , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 92 - 92: oooOo0oo0oo % III1iiIii % OOooOOo
def iIi1Ii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , iIii , IIiI1i , I1i in IIi :
  iIiiiii1i ( ( '[COLORblue]' + OOoO + ' [COLORred] Cancelled On[/COLOR] ' + I1i ) , OOoO , 10099 , iiIi1IIiIi + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 11 - 11: oOo0O0Ooo % o0ii1I - oO0o - i1i1I1IIii1II + I11i
def o0O0O0 ( url ) :
 iii1 = ( url )
 oOO0oo = iii1 . lower ( )
 if 55 - 55: o0o00Oo0O - i1IiiiI1iI
 if 58 - 58: OOooOOo - IiI1i11I - ii
 iiI11ii1111 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( iii1 ) . replace ( ' ' , '+' )
 i1oO = 'http://onlinemovies.tube/?s=' + ( iii1 ) . replace ( ' ' , '+' )
 iIIi1IIi = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i111i11I1ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oOOII1i11i1iIi11 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 96 - 96: iI11I1II1I1I
 oOo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 I11iIiii1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 OOOo00 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 91 - 91: iI11I1II1I1I . I11i . Ii1I + ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 69 - 69: i1IiiiI1iI - oOo0O0Ooo
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 95 - 95: oOo0O0Ooo * Ii . i1iIi
 if 41 - 41: IIiIiII11i
 i11II1I11I1 = O00O0oOO00O00 ( iiI11ii1111 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( i1oO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iIIi1IIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( i111i11I1ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 i11IiIIi11I = O00O0oOO00O00 ( oOOII1i11i1iIi11 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 37 - 37: Iii . I1ii11iIi11i % III1iiIii * ooOoO0O00
 if 71 - 71: I1ii11iIi11i / I11i + oooOo0oo0oo
 O0OO = O00O0oOO00O00 ( oOo0O )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 IIIiIiI = O00O0oOO00O00 ( I11iIiii1 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 i11i11 = O00O0oOO00O00 ( OOOo00 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 14 - 14: Ii
 if IIIiIiI != 'Failed' :
  iI1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( IIIiIiI )
  for url , OOoO in iI1 :
   iIIiI1ii = O00O0oOO00O00 ( url )
   oo0OOoOoo0O0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIIiI1ii )
   for iiI11ii1111 , IIiIIiI in oo0OOoOoo0O0O :
    if oOO0oo in IIiIIiI . lower ( ) :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , url + iiI11ii1111 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 73 - 73: i1iIi + i1i1I1IIii1II . oO0o
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if O0OO != 'Failed' :
  IIiIIIIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0OO )
  for url , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in IIiIIIIiI :
   if oOO0oo in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 58 - 58: I11i / I11i + i1iIi + Iii - OOooOOo . oooOo0oo0oo
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 15 - 15: i1iIi * OOooOOo % III1iiIii . OOooOOo . Iii
    if 97 - 97: i1i1I1IIii1II
    if 80 - 80: oOo0O0Ooo . o0ii1I
    if 47 - 47: Iii + i1iIi + IIiIiII11i % Ii
    if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / IiI1i11I * i1i1I1IIii1II
    if 29 - 29: I11i
    if 86 - 86: IIiIiII11i . III1iiIii
    if 2 - 2: ii
    if 60 - 60: oO0o
    if 81 - 81: OOooOOo % o0ii1I
    if 87 - 87: iI11I1II1I1I . ii * OOooOOo
 if i11i11 != 'Failed' :
  OOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i11i11 )
  for url , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in OOOo :
   if oOO0oo in OOoO . lower ( ) :
    iIiiiii1i ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 74 - 74: o0ii1I - ii . I1ii11iIi11i
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  III1Ii1i1I1 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for url , iIiIi11 , OOoO , O0O00OooO in i1Iii1i1I :
   if oOO0oo in OOoO . lower ( ) :
    if 'season' in O0O00OooO :
     iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , iIiIi11 , iIiIi11 , '' )
    if 'episodes' in O0O00OooO :
     iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , iIiIi11 , iIiIi11 , '' )
  for url in III1Ii1i1I1 :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 40 - 40: Iii % ii - oooOo0oo0oo + I11i / oooOo0oo0oo
   oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if i11II1I11I1 != 'Failed' :
  OooO0oOo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( i11II1I11I1 )
  for url , OOoO , iIiIi11 in OooO0oOo :
   if oOO0oo in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( OOoO ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , iIiIi11 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 84 - 84: o0o00Oo0O
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 11 - 11: IIiIiII11i / Ii / o0o00Oo0O
    if 94 - 94: i1iIi * Iii - III1iiIii . iI11I1II1I1I
    if 66 - 66: i1iIi - oooOo0oo0oo * OOooOOo / i1i1I1IIii1II * IIiIiII11i * oO0o
    if 91 - 91: ii / o0ii1I . oOo0O0Ooo + i1iIi . IIiIiII11i
    if 45 - 45: i1i1I1IIii1II * OOooOOo / iI11I1II1I1I
    if 77 - 77: i1IiiiI1iI - Iii
    if 11 - 11: Ii1I
    if 26 - 26: iI11I1II1I1I * i1IiiiI1iI - oooOo0oo0oo
    if 27 - 27: Ii1I * i1IiiiI1iI - oO0o + o0ii1I * o0ii1I
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for OOoO in IiIi1I1 :
   if oOO0oo in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iIIi1IIi + OOoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 55 - 55: i1iIi
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for OOoO in I1i11 :
   if oOO0oo in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i111i11I1ii + OOoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 82 - 82: i1IiiiI1iI - oooOo0oo0oo + oO0o
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if i11IiIIi11I != 'Failed' :
  o000o0O0Oo00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i11IiIIi11I )
  for url , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in o000o0O0Oo00 :
   if oOO0oo in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 64 - 64: I11i . o0o00Oo0O * o0ii1I + ii - I1ii11iIi11i . ii
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: I1ii11iIi11i - i1i1I1IIii1II . iI11I1II1I1I % Iii / OOooOOo - o0o00Oo0O
 o0O0oo0o = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for II1iIi1IiIii in o0O0oo0o :
  I111I11I111 = oO0 + II1iIi1IiIii + oOoOooOo0o0
  III11iiii11i1 = O00O0oOO00O00 ( I111I11I111 )
  if III11iiii11i1 != 'Failed' :
   oOo0OOoooO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( III11iiii11i1 )
   for OOoO , OOOiiiiI , url , iIiIi11 , oooOo0OOOoo0 , oO0oOOoo00000 in oOo0OOoooO :
    if oOO0oo in OOoO . lower ( ) :
     Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - Source Pandoras[/COLOR]' , url , oO0oOOoo00000 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 12 - 12: OOooOOo % III1iiIii % Ii1I . Ii * iI11I1II1I1I
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
     if 66 - 66: Ii * iI11I1II1I1I % ii
     if 5 - 5: OOooOOo % ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: OOooOOo . ooOoO0O00 % oO0o % i1iIi % oooOo0oo0oo
def Ii111IIi ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( ( OOoO ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + O0O00Oo , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + O0O00Oo )
def iII1ii1I1i ( url ) :
 iiI1 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( iiI1 )
 sys . exit ( 1 )
 if 42 - 42: oooOo0oo0oo % i1i1I1IIii1II / oO0o - i1i1I1IIii1II * Ii
def iI1IiiiIiI1Ii ( ) :
 if 78 - 78: ii / oooOo0oo0oo % OOooOOo * ii
 if 68 - 68: i1i1I1IIii1II
 if 29 - 29: IiI1i11I + Ii % Iii
 if 93 - 93: OOooOOo % iI11I1II1I1I
 if 90 - 90: oOo0O0Ooo - oooOo0oo0oo / o0ii1I / o0o00Oo0O / Iii
 if 87 - 87: OOooOOo / III1iiIii + iI11I1II1I1I
 if 93 - 93: iI11I1II1I1I + i1i1I1IIii1II % i1iIi
 if 21 - 21: oooOo0oo0oo
 if 6 - 6: III1iiIii
 if 46 - 46: III1iiIii + i1i1I1IIii1II
 if 79 - 79: ii - III1iiIii * III1iiIii . OOooOOo
 iIiiiii1i ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , iiIi1IIiIi + 'seasons.png' )
 iIiiiii1i ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , iiIi1IIiIi + 'episodes.png' )
 iIiiiii1i ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , iiIi1IIiIi + 'Search.png' )
 oOI1Ii1I1 ( 'tvshows' , 'INFO' )
 if 100 - 100: IIiIiII11i * Iii % oOo0O0Ooo / Ii1I
def OOoo0oOO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , ii11iiIi in IIi :
  iIiiiii1i ( ( OOoO + ' - ' + ii11iiIi ) . replace ( '&amp;' , '&' ) , url , 90053 , iiIi1IIiIi + 'seasons.png' )
  if 48 - 48: III1iiIii % Iii
def i1I1III1i1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  iIiiiii1i ( OOoO , url , 90054 , iiIi1IIiIi + 'episodes.png' )
  if 4 - 4: i1IiiiI1iI / o0ii1I - o0ii1I
def Ii111iIIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , url in IIi :
  iIiiiii1i ( OOoO , url , 90054 , iIiIi11 )
 for url in next :
  iIiiiii1i ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 56 - 56: Iii
def IiI1O0oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for iIiIi11 , ii11iiIi , url , OOoO , IiIII in IIi :
  Iii1I1I11iiI1 ( ii11iiIi + ' - ' + OOoO + ' - ' + IiIII , url , 90044 , iIiIi11 , iIiIi11 , '' )
 for iIiIi11 , OOoO , url in i1Iii1i1I :
  iIiiiii1i ( OOoO , url , 90044 , iIiIi11 , iIiIi11 , '' )
 for url in next :
  iIiiiii1i ( 'NEXT' , url , 90053 , iiIi1IIiIi + 'Next.png' )
  if 13 - 13: I11i % i1i1I1IIii1II / i1IiiiI1iI % i1IiiiI1iI % o0o00Oo0O
def o0Ii1 ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IiII = 'http://onlinemovies.tube/?s=' + ( iii1 ) . replace ( ' ' , '+' )
 oOO0oo = IIi1IiII . lower ( )
 II11iIiIIIiI = OooOoooOo ( oOO0oo )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO , O0O00OooO in IIi :
  if 'season' in O0O00OooO :
   iIiiiii1i ( OOoO , O0O00Oo , 90054 , iIiIi11 , iIiIi11 , '' )
  if 'episodes' in O0O00OooO :
   iIiiiii1i ( OOoO , O0O00Oo , 90044 , iIiIi11 , iIiIi11 , '' )
 for O0O00Oo in next :
  iIiiiii1i ( 'NEXT' , O0O00Oo , 90053 , iiIi1IIiIi + 'Next.png' )
  if 65 - 65: III1iiIii . ooOoO0O00
def OOOoO0 ( ) :
 if 85 - 85: iI11I1II1I1I / ii % IIiIiII11i
 if 49 - 49: Ii % OOooOOo + i1IiiiI1iI . IIiIiII11i % IiI1i11I * oooOo0oo0oo
 if 67 - 67: ooOoO0O00
 if 5 - 5: IIiIiII11i . ii
 if 57 - 57: oOo0O0Ooo
 if 35 - 35: ii - i1IiiiI1iI / oO0o
 if 50 - 50: OOooOOo
 if 33 - 33: Iii
 if 98 - 98: OOooOOo % IIiIiII11i
 if 95 - 95: iI11I1II1I1I - i1IiiiI1iI - oooOo0oo0oo + i1IiiiI1iI % Ii1I . oOo0O0Ooo
 iIiiiii1i ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , iiIi1IIiIi + 'allmov.png' )
 iIiiiii1i ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , iiIi1IIiIi + 'Genre.png' )
 iIiiiii1i ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , iiIi1IIiIi + 'Years.png' )
 iIiiiii1i ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , iiIi1IIiIi + 'Search.png' )
 oOI1Ii1I1 ( 'tvshows' , 'INFO' )
 if 41 - 41: o0o00Oo0O + i1i1I1IIii1II . ooOoO0O00 - IIiIiII11i * I11i . oO0o
def oooO00Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , ii11iiIi in IIi :
  if 'genre' in url :
   iIiiiii1i ( ( OOoO + ' - ' + ii11iiIi ) . replace ( '&amp;' , '&' ) , url , 90043 , iiIi1IIiIi + 'Genre.png' )
   if 86 - 86: IIiIiII11i + i1iIi + III1iiIii
def I11i11I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  if 'release' in url :
   iIiiiii1i ( OOoO , url , 90043 , iiIi1IIiIi + 'Years.png' )
   if 90 - 90: Ii1I
def i11i11i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , II11ii , url , OOOiiiiI in IIi :
  Iii1I1I11iiI1 ( OOoO + ' ' + II11ii , url , 90044 , iIiIi11 , iIiIi11 , OOOiiiiI )
 for iIiIi11 , OOoO , O0O00OooO , url , I1 , OOOiiiiI in i1Iii1i1I :
  if 'movies' in O0O00OooO :
   Iii1I1I11iiI1 ( OOoO + ' - ' + I1 , url , 90044 , iIiIi11 , iIiIi11 , OOOiiiiI )
 for url in next :
  iIiiiii1i ( 'NEXT' , url , 90043 , iiIi1IIiIi + 'Next.png' )
  if 84 - 84: OOooOOo - Ii
def i1II1II1iii1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  O0OO0oOO ( 'http:' + url )
  if 85 - 85: o0o00Oo0O
def O0OO0oOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  iiIi1IIiI ( ( OOoO ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , iiIi1IIiIi + 'movhub.png' )
def IiiIiI1I1 ( ) :
 if 19 - 19: o0ii1I
 if 55 - 55: oooOo0oo0oo % oooOo0oo0oo / o0o00Oo0O % IiI1i11I - I11i . I1ii11iIi11i
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
 if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
 if 8 - 8: OOooOOo * I1ii11iIi11i / III1iiIii % o0ii1I - oOo0O0Ooo
 if 71 - 71: IiI1i11I
 if 23 - 23: ooOoO0O00 . iI11I1II1I1I . oooOo0oo0oo . o0o00Oo0O % o0ii1I % Ii
 if 11 - 11: o0o00Oo0O - IIiIiII11i . oooOo0oo0oo . o0ii1I % i1IiiiI1iI
 if 21 - 21: I1ii11iIi11i / IiI1i11I . i1IiiiI1iI * ii + Iii - ooOoO0O00
 if 58 - 58: Ii1I
 if 2 - 2: IIiIiII11i / i1IiiiI1iI
 if 54 - 54: ooOoO0O00 . Iii - Ii1I + i1iIi + I1ii11iIi11i / I1ii11iIi11i
 if 22 - 22: i1iIi . iI11I1II1I1I
 if 12 - 12: o0ii1I
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IiII = 'http://onlinemovies.tube/?s=' + ( iii1 ) . replace ( ' ' , '+' )
 oOO0oo = IIi1IiII . lower ( )
 II11iIiIIIiI = OooOoooOo ( oOO0oo )
 IIi = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO , Ooii1IIi1ii in IIi :
  if 'movies' in Ooii1IIi1ii :
   iIiiiii1i ( Ooii1IIi1ii + '-' + OOoO , O0O00Oo , 90044 , iIiIi11 )
 for O0O00Oo in next :
  i11i11i ( O0O00Oo )
  if 85 - 85: ii % OOooOOo * iI11I1II1I1I
def II1iiiiII ( ) :
 iIiiiii1i ( 'Search' , '' , 80008 , iiIi1IIiIi + 'Search.png' )
 II11iIiIIIiI = OooOoooOo ( 'http://www.join4films.com/' )
 IIi = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( OOoO , O0O00Oo , 80006 , iiIi1IIiIi + 'Desi.png' )
def IiI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( II11iIiIIIiI )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOoO in IIi :
  iiIi1IIiI ( OOoO , url , 80007 , iIiIi11 )
 for url , iIiIi11 , OOoO in IIi :
  iIiiiii1i ( 'Next' , url , 80006 , iiIi1IIiIi + 'Next.png' )
def o0o0OO0o00o0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  url = ( url ) . replace ( ' ' , '%20' )
  OooO0OO ( url )
def IIIIIIi1i ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IiII = 'http://www.join4films.com/?s=' + ( iii1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 oOO0oo = IIi1IiII . lower ( )
 IiI ( oOO0oo )
 if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
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
 if 50 - 50: IiI1i11I % IIiIiII11i - i1iIi . ooOoO0O00 + o0o00Oo0O % IiI1i11I
 if 10 - 10: IiI1i11I . ooOoO0O00 + o0ii1I
 if 66 - 66: oO0o % I11i
 if 21 - 21: OOooOOo - ii % Ii
 if 71 - 71: ooOoO0O00 - Iii * i1IiiiI1iI + i1i1I1IIii1II - oO0o % Ii1I
def Ooo0oO ( ) :
 Iii1I1I11iiI1 ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( 'Search' , '' , 10078 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
 if 32 - 32: ooOoO0O00 . IiI1i11I + IIiIiII11i - oO0o - iI11I1II1I1I
def iIIIIiiii1I ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IiII = 'http://imoviemax.se/?s=' + ( iii1 ) . replace ( ' ' , '+' )
 oOO0oo = IIi1IiII . lower ( )
 IIi1iI11IIIi1 ( oOO0oo )
def o00O0o0oo0oOO0oO ( url ) :
 iIiIII1iI1111 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , Ii1I1I111iI in IIi :
  if OOoO in iIiIII1iI1111 :
   pass
  else :
   Iii1I1I11iiI1 ( OOoO + ' - ' + Ii1I1I111iI + ' Films' , url , 10074 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
   iIiIII1iI1111 . append ( OOoO )
   if 31 - 31: IiI1i11I + III1iiIii . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
def o00O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO , Oo000O in IIi :
  Iii1I1I11iiI1 ( OOoO + ' - Views:' + Oo000O , url , 10075 , iiIi1IIiIi + 'genievision.png' , Oo00OOOOO , '' )
  if 42 - 42: III1iiIii % IiI1i11I % I11i % i1i1I1IIii1II + Iii % OOooOOo
  if 3 - 3: i1i1I1IIii1II
def IIi1iI11IIIi1 ( url ) :
 OOOiI1 = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( II11iIiIIIiI )
 for next in next :
  Iii1I1I11iiI1 ( 'NEXT PAGE' , next , 10074 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , url in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 10075 , iIiIi11 , iIiIi11 , '' )
  OOOiI1 . append ( OOoO )
  if 84 - 84: oooOo0oo0oo * oOo0O0Ooo % Iii + oooOo0oo0oo / IiI1i11I
def oo000o ( img , name , url ) :
 img = img
 name = name
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( II11iIiIIIiI )
 for OO00o0oOO , url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  i1i1I1 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + i1i1I1
  I1iOOo0O = ( OO00o0oOO ) . replace ( 'play-' , 'Server ' )
  iI1Ii1iI11iiI ( I1iOOo0O , i1i1I1 , 10076 , img , img , '' )
  if 100 - 100: oO0o % oO0o
def iI1I1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( II11iIiIIIiI )
 for i1oO in IIi :
  if '=m' in i1oO :
   ii1O0ooooo000 ( i1oO )
  elif 'php' in i1oO :
   iI1I1 ( url )
  else :
   II11iIiIIIiI = OooOoooOo ( i1oO )
   IIi = re . compile ( 'content="([^"]*)">' ) . findall ( II11iIiIIIiI )
   for iIIi1IIi in IIi :
    ii1O0ooooo000 ( i1oO )
    if 97 - 97: Ii % i1i1I1IIii1II / I1ii11iIi11i / I1ii11iIi11i
    if 97 - 97: IIiIiII11i - i1IiiiI1iI - iI11I1II1I1I * oOo0O0Ooo
    if 54 - 54: iI11I1II1I1I
def i111i1I1ii1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 O0OoooI11iI1I = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1i , Iii1iiIi1II1 in O0OoooI11iI1I :
  print 'there ><><><><><><><><><><><><'
  I1i = I1i
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Iii1iiIi1II1 ) )
  for OOoO , Oo000o in IIi :
   print 'here <><><><><><><><><><><><>'
   Iii1I1I11iiI1 ( '[COLORred]' + I1i + '[/COLOR] - ' + OOoO + ' - [COLOR' + ooOoOoo0O + ']' + Oo000o + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
 I1iiiiI1iI = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1i , OO00oo in I1iiiiI1iI :
  print 'there ><><><><><><><><><><><><'
  I1i = I1i
  IIi = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OO00oo ) )
  for OOoO , Oo000o in IIi :
   print 'here <><><><><><><><><><><><>'
   Iii1I1I11iiI1 ( '[COLORred]' + I1i + '[/COLOR] - ' + OOoO + ' - [COLOR' + ooOoOoo0O + ']' + Oo000o + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , iiIi1IIiIi + 'loader.png' , Oo00OOOOO , '' )
   if 84 - 84: i1iIi + Ii - oooOo0oo0oo * i1iIi
   if 33 - 33: i1iIi % ooOoO0O00 - i1i1I1IIii1II . o0o00Oo0O / o0o00Oo0O
   if 96 - 96: ii + III1iiIii * o0o00Oo0O
def OoO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1iiiiI1iI in I1iiiiI1iI :
  OOoO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
  for OOoO in OOoO :
   OOoO = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1iiiiI1iI ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  oOo00 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
  for oOo00 in oOo00 :
   oOo00 = 'http:' + oOo00
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , '' , '' )
  if 86 - 86: o0ii1I
  if 29 - 29: iI11I1II1I1I - oO0o + oOo0O0Ooo % iI11I1II1I1I % oooOo0oo0oo
  if 84 - 84: III1iiIii + Ii1I + o0ii1I + IiI1i11I
  if 62 - 62: Ii + OOooOOo + ooOoO0O00
def O0OoOO0oo0 ( url ) :
 if 69 - 69: OOooOOo
 OO0Oo = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1oO , iIiIi11 , OOoO , IIiiiiiIiIIi in IIi :
  OOoO = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  o0o = OooOoooOo ( i1oO )
  i1Iii1i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( o0o )
  for I1111I1II11 , I1iIII1 in i1Iii1i1I :
   iiIiiIi1 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( I1iIII1 ) )
   for OOOiiiiI in iiIiiIi1 :
    if OOoO in OO0Oo :
     pass
    else :
     iI1Ii1iI11iiI ( OOoO , I1111I1II11 , 8043 , iIiIi11 , iIiIi11 , OOOiiiiI )
     oOI1Ii1I1 ( 'movies' , 'INFO' )
     OO0Oo . append ( OOoO )
     if 30 - 30: oooOo0oo0oo + IIiIiII11i - III1iiIii * ii
     if 19 - 19: III1iiIii - I11i . iI11I1II1I1I . OOooOOo / oooOo0oo0oo
def OOO0O00Oo ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , oo00O00oO000o , OOOiiiiI , oooOo0OOOoo0 , OOoO in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 10065 , oo00O00oO000o , oooOo0OOOoo0 , OOOiiiiI )
 oOI1Ii1I1 ( 'movies' , 'INFO' )
 if 13 - 13: iI11I1II1I1I
def IiIIII1iiIIi ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IiII = 'https://www.youtube.com/results?search_query=' + ( iii1 ) . replace ( ' ' , '+' )
 oOO0oo = IIi1IiII . lower ( )
 II11iIiIIIiI = OooOoooOo ( oOO0oo )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo in next :
  O0O00Oo = 'https://www.youtube.com' + O0O00Oo
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , O0O00Oo , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for iIiIi11 , O0O00Oo , OOoO , i1I1IiI1ii , I1iIII1 in IIi :
  OOO00 . append ( OOoO )
  oOI1Ii1I1 ( 'tvshows' , 'INFO' )
  oOo00 = 'http:' + ( iIiIi11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOo00
  O0O00Oo = 'http://www.youtube.com' + O0O00Oo
  iI1Ii1iI11iiI ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , oOo00 , I1iIII1 )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIiIi11 , O0O00Oo , OOoO , i1I1IiI1ii in IIi :
   print 'im doing it'
   oOI1Ii1I1 ( 'tvshows' , 'INFO' )
   oOo00 = 'http:' + ( iIiIi11 ) . replace ( 'https:' , '' )
   O0O00Oo = 'http://www.youtube.com' + O0O00Oo
   if '&' in O0O00Oo :
    print ' i got here'
    II11iIiIIIiI = OooOoooOo ( O0O00Oo )
    I1iiiiI1iI = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for I1iiiiI1iI in I1iiiiI1iI :
     OOoO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
     for OOoO in OOoO :
      OOoO = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     O0O00Oo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1iiiiI1iI ) )
     for O0O00Oo in O0O00Oo :
      O0O00Oo = 'https://www.youtube.com/w' + O0O00Oo
     oOo00 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
     for oOo00 in oOo00 :
      oOo00 = 'http:' + oOo00
     iI1Ii1iI11iiI ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , Oo00OOOOO , '' )
   elif OOoO in OOO00 :
    pass
   elif 'user' in O0O00Oo or 'elete' in OOoO :
    pass
   elif 'hannel' in O0O00Oo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + O0O00Oo
    II11iIiIIIiI = OooOoooOo ( O0O00Oo )
    O00OOoOOOO00O = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for iIiIi11 , O0O00Oo , OOoO in O00OOoOOOO00O :
     if 'outube' in O0O00Oo or 'list' in O0O00Oo :
      pass
     elif 'atch' in O0O00Oo :
      O0O00Oo = ( O0O00Oo ) . replace ( '/watch?v=' , '' )
      iI1Ii1iI11iiI ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iIiIi11 , 'http:' + iIiIi11 , '' )
     else :
      pass
   else :
    iI1Ii1iI11iiI ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , oOo00 , '' )
    if 72 - 72: oOo0O0Ooo + III1iiIii . OOooOOo + OOooOOo
def ooooOoo0OO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( II11iIiIIIiI )
 for url in next :
  url = 'https://www.youtube.com' + url
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + '] NEXT [/COLOR]' , url , 10065 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 for iIiIi11 , url , OOoO , i1I1IiI1ii , I1iIII1 in IIi :
  OOO00 . append ( OOoO )
  oOI1Ii1I1 ( 'tvshows' , 'INFO' )
  oOo00 = 'http:' + ( iIiIi11 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOo00
  url = 'http://www.youtube.com' + url
  iI1Ii1iI11iiI ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , oOo00 , I1iIII1 )
 else :
  IIi = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for iIiIi11 , url , OOoO , i1I1IiI1ii in IIi :
   oOI1Ii1I1 ( 'tvshows' , 'INFO' )
   oOo00 = 'http:' + ( iIiIi11 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    II11iIiIIIiI = OooOoooOo ( url )
    I1iiiiI1iI = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for I1iiiiI1iI in I1iiiiI1iI :
     OOoO = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
     for OOoO in OOoO :
      OOoO = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1iiiiI1iI ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     oOo00 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1iiiiI1iI ) )
     for oOo00 in oOo00 :
      oOo00 = 'http:' + oOo00
     iI1Ii1iI11iiI ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , Oo00OOOOO , '' )
   elif OOoO in OOO00 :
    pass
   elif 'user' in url or 'elete' in OOoO :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    II11iIiIIIiI = OooOoooOo ( url )
    O00OOoOOOO00O = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
    for iIiIi11 , url , OOoO in O00OOoOOOO00O :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      iI1Ii1iI11iiI ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iIiIi11 , 'http:' + iIiIi11 , '' )
     else :
      pass
   else :
    iI1Ii1iI11iiI ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 , oOo00 , '' )
    if 85 - 85: IIiIiII11i . i1iIi % oooOo0oo0oo % Iii
    if 80 - 80: i1i1I1IIii1II * Iii / iI11I1II1I1I % i1i1I1IIii1II / iI11I1II1I1I
    if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * IiI1i11I . Ii * o0o00Oo0O
def Iiii1 ( ) :
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']Setup Tv Guide[/COLOR]' , '' , 100212 , iiIi1IIiIi + 'linkchannels.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']Open Guide[/COLOR]' , '' , 100213 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 if 27 - 27: oooOo0oo0oo
def O0OO0ooO00 ( ) :
 ivuesetup . iVueInt ( )
 if 83 - 83: iI11I1II1I1I
def OooOO0oOOo0O ( ) :
 I1II ( )
 return
 if 9 - 9: I1ii11iIi11i % ii - o0ii1I
def I1II ( ) :
 if 43 - 43: oO0o % oO0o
 II1I = xbmcaddon . Addon ( 'plugin.video.GenieTv' )
 IIiii11ii1i = II1I . getSetting ( id = 'User' )
 II1iI1IIi = II1I . getSetting ( id = 'Pass' )
 Ii11iiI1 = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
 oO0O = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
 OOoooO00o0o = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
 I1ii1Ii1 = "http://piesustv.net:8000/get.php?username=" + IIiii11ii1i + "&password=" + II1iI1IIi + "&type=m3u_plus&output=ts"
 OoOoO = "http://piesustv.net:8000/xmltv.php?username=" + IIiii11ii1i + "&password=" + II1iI1IIi + "&type=m3u_plus&output=ts"
 if 13 - 13: OOooOOo % i1iIi
 xbmc . executeJSONRPC ( Ii11iiI1 )
 xbmc . executeJSONRPC ( oO0O )
 xbmc . executeJSONRPC ( OOoooO00o0o )
 if 81 - 81: III1iiIii - I11i - I1ii11iIi11i - o0ii1I / oooOo0oo0oo % Iii
 oO0OoOo = xbmcaddon . Addon ( 'pvr.iptvsimple' )
 oO0OoOo . setSetting ( id = 'm3uUrl' , value = I1ii1Ii1 )
 oO0OoOo . setSetting ( id = 'epgUrl' , value = OoOoO )
 oO0OoOo . setSetting ( id = 'm3uCache' , value = "false" )
 oO0OoOo . setSetting ( id = 'epgCache' , value = "false" )
 xbmc . executebuiltin ( "Container.Refresh" )
def oOOOOOo ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(TVGuide)' )
 i1I11ii ( )
if 72 - 72: Iii
if 87 - 87: ooOoO0O00
def i1I11ii ( ) :
 if 48 - 48: I1ii11iIi11i * i1i1I1IIii1II * iI11I1II1I1I + Ii - ii
 if 38 - 38: OOooOOo / iI11I1II1I1I % Ii - III1iiIii * IiI1i11I / OOooOOo
 if 13 - 13: oO0o * Ii1I - i1IiiiI1iI
 if 79 - 79: i1i1I1IIii1II % I11i % OOooOOo
 if 45 - 45: oOo0O0Ooo * oooOo0oo0oo % oO0o
 if 24 - 24: i1iIi - Iii * i1i1I1IIii1II
 if 87 - 87: o0ii1I - Ii1I % Ii1I . i1i1I1IIii1II / Ii1I
 if 6 - 6: OOooOOo / iI11I1II1I1I * ii * Ii
 if 79 - 79: III1iiIii % oO0o
 if 81 - 81: Ii + Ii * oO0o + III1iiIii
 if 32 - 32: o0o00Oo0O . ii
 if 15 - 15: oOo0O0Ooo . oO0o
 if OO0o == "insert_username" :
  IiiIi = i1ii1I ( )
  IiiIII = ii11iI1iIiIi ( )
  I11 ( 'User' , IiiIi )
  I11 ( 'Pass' , IiiIII )
  xbmc . executebuiltin ( 'Container.Refresh' )
  o0OO0OoO0o0o0 = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_categories' % ( IiiIi , IiiIII )
  o0OO0OoO0o0o0 = OooOoooOo ( o0OO0OoO0o0o0 )
  if o0OO0OoO0o0o0 == "" :
   IIIIIIi1IiIi = "[COLOR " + ooOoOoo0O + "]Incorrect Login Details[/COLOR]"
   III1i = "[COLOR " + ooOoOoo0O + "]Please Re-enter[/COLOR]"
   o0Oo0 = ""
   xbmcgui . Dialog ( ) . ok ( 'Attention' , IIIIIIi1IiIi , III1i , o0Oo0 )
   i1I11ii ( )
  else :
   IIIIIIi1IiIi = "[COLOR " + ooOoOoo0O + "]Login Successful[/COLOR]"
   III1i = "[COLOR " + ooOoOoo0O + "]Welcome to GenieTv[/COLOR]"
   o0Oo0 = ( '[COLOR ' + ooOoOoo0O + ']%s[/COLOR]' % IiiIi )
   xbmcgui . Dialog ( ) . ok ( 'GenieTv' , IIIIIIi1IiIi , III1i , o0Oo0 )
   xbmc . executebuiltin ( 'Container.Refresh' )
   ii1IiI11I ( )
 else :
  ii1IiI11I ( )
def i1ii1I ( ) :
 OO0Ooo000O0 = xbmc . Keyboard ( '' , 'heading' , True )
 OO0Ooo000O0 . setHeading ( 'Enter Username' )
 OO0Ooo000O0 . setHiddenInput ( False )
 OO0Ooo000O0 . doModal ( )
 if ( OO0Ooo000O0 . isConfirmed ( ) ) :
  o00oIiii1Ii = OO0Ooo000O0 . getText ( )
  return o00oIiii1Ii
 else :
  return False
  if 62 - 62: ooOoO0O00 % OOooOOo
  if 37 - 37: Iii * ooOoO0O00
def ii11iI1iIiIi ( ) :
 OO0Ooo000O0 = xbmc . Keyboard ( '' , 'heading' , True )
 OO0Ooo000O0 . setHeading ( 'Enter Password' )
 OO0Ooo000O0 . setHiddenInput ( False )
 OO0Ooo000O0 . doModal ( )
 if ( OO0Ooo000O0 . isConfirmed ( ) ) :
  o00oIiii1Ii = OO0Ooo000O0 . getText ( )
  return o00oIiii1Ii
 else :
  return False
def I1IIII ( ) :
 I1ii1Ii1 = "http://piesustv.net:8000//get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  OooooOoO = urllib2 . urlopen ( I1ii1Ii1 )
  print OooooOoO . getcode ( )
  OooooOoO . close ( )
  if 79 - 79: i1iIi % oooOo0oo0oo
  pass
  if 54 - 54: OOooOOo - i1IiiiI1iI
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLORorangered]Expired Account[/COLOR]" , '[COLOR ' + ooOoOoo0O + ']You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR ' + ooOoOoo0O + ']Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
def ii1IiI11I ( ) :
 iii ( )
 if 65 - 65: i1IiiiI1iI . i1iIi + oooOo0oo0oo / I1ii11iIi11i + III1iiIii % ooOoO0O00
 if 28 - 28: Ii + o0o00Oo0O / Ii1I
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo , 60004 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Guide Menu[/COLOR]' , '' , 100211 , iiIi1IIiIi + 'TvGuide.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']CatchUp Tv[/COLOR]' , '' , 90026 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']VOD Lists[/COLOR]' , '' , 40000 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
 if 81 - 81: oOo0O0Ooo - iI11I1II1I1I / oOo0O0Ooo / o0o00Oo0O
 if 34 - 34: o0ii1I * o0ii1I - Ii1I - o0o00Oo0O . Ii
 if 32 - 32: iI11I1II1I1I . oO0o * i1i1I1IIii1II / oooOo0oo0oo . IIiIiII11i - I1ii11iIi11i
def IIIi ( ) :
 xbmc . executebuiltin ( "ActivateWindow(busydialog)" )
 III11IiiiIi1 = 'http://piesustv.net%3A8000%2Fget.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo + '%26type%3Dm3u_plus%26output%3Dts'
 IiI1Ii1ii = 'http://piesustv.net%3A8000%2Fxmltv.php%3Fusername%3D' + OO0o + '%26password%3D' + Ooo
 o0OO0OoO0o0o0 = 'http://piesustv.net:8000/enigma2.php?username=' + OO0o + '&password=' + Ooo + '&type=get_vod_categories'
 o0OO0OoO0o0o0 = OooOoooOo ( o0OO0OoO0o0o0 )
 if not o0OO0OoO0o0o0 == "" :
  Ii11iiIIiI1 = 'https://tinyurl.com/create.php?source=indexpage&url=' + III11IiiiIi1 + '&submit=Make+TinyURL%21&alias='
  xbmc . log ( str ( Ii11iiIIiI1 ) )
  I1Iii11I111I = 'https://tinyurl.com/create.php?source=indexpage&url=' + IiI1Ii1ii + '&submit=Make+TinyURL%21&alias='
  III11IiiiIi1 = OooOoooOo ( Ii11iiIIiI1 )
  IiI1Ii1ii = OooOoooOo ( I1Iii11I111I )
  xbmc . log ( str ( IiI1Ii1ii ) )
  IIIiI1iiiiiIi = O0oo0 ( III11IiiiIi1 , '<div class="indent"><b>' , '</b>' )
  iii1iiii11I = O0oo0 ( IiI1Ii1ii , '<div class="indent"><b>' , '</b>' )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  xbmcgui . Dialog ( ) . ok ( '[COLOR' + ooOoOoo0O + ']GenieTv[/COLOR]' , '[COLORsteelblue]PLAYLIST URL: [/COLOR]%s' % IIIiI1iiiiiIi , '' , '[COLORsteelblue]EPG URL: [/COLOR]%s' % iii1iiii11I )
 else :
  return
def o0oO0o0oo0O0 ( ) :
 I1IIII ( )
 O0oo00oOOO0o ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , II1iI111iiIIiI1I + '&action=get_vod_streams' , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( ooO00Oo )
 IIi = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  Iii1I1I11iiI1 ( ( '[COLORsteelblue]' + OOoO + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , O0O00Oo , 40001 , iiIi1IIiIi + 'Vod_Lists.png' , Oo00OOOOO , '' )
def Iiii1Ii1I ( url ) :
 open = OooOoooOo ( oooOOOOOi1iIii + url )
 o0O0ooooooo00 = I1111ii11IIII ( open , '<channel>' , '</channel>' )
 for IiIi1II111I in o0O0ooooooo00 :
  if '<playlist_url>' in open :
   OOoO = O0oo0 ( IiIi1II111I , '<title>' , '</title>' )
   iiI11ii1111 = O0oo0 ( IiIi1II111I , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   Iii1I1I11iiI1 ( str ( base64 . b64decode ( OOoO ) ) . replace ( '?' , '' ) , iiI11ii1111 , 3 , icon , oooOo0OOOoo0 , '' )
  else :
   OOoO = O0oo0 ( IiIi1II111I , '<title>' , '</title>' )
   OOoO = base64 . b64decode ( OOoO )
   o00oIIi1i1 = O0oo0 ( IiIi1II111I , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   url = O0oo0 ( IiIi1II111I , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
   OOOiiiiI = O0oo0 ( IiIi1II111I , '<description>' , '</description>' )
   OOOiiiiI = base64 . b64decode ( OOOiiiiI )
   o0O0Ooo = O0oo0 ( OOOiiiiI , 'PLOT:' , '\n' )
   O0oO00oOOooO = O0oo0 ( OOOiiiiI , 'CAST:' , '\n' )
   IiIIii1iiI = O0oo0 ( OOOiiiiI , 'RATING:' , '\n' )
   ii1IiiII = O0oo0 ( OOOiiiiI , 'RELEASEDATE:' , '\n' ) . replace ( ' ' , '-' )
   ii1IiiII = re . compile ( '-.*?-.*?-(.*?)-' , re . DOTALL ) . findall ( ii1IiiII )
   IiiI1II1II1i = O0oo0 ( OOOiiiiI , 'DURATION_SECS:' , '\n' )
   iIO0OO0o0O00oO = O0oo0 ( OOOiiiiI , 'GENRE:' , '\n' )
   o00OoO0o0oOo ( str ( OOoO ) . replace ( '[/COLOR].' , '.[/COLOR]' ) , url , 222 , o00oIIi1i1 , oooOo0OOOoo0 , o0O0Ooo , str ( ii1IiiII ) . replace ( "['" , "" ) . replace ( "']" , "" ) , str ( O0oO00oOOooO ) . split ( ) , IiIIii1iiI , IiiI1II1II1i , iIO0OO0o0O00oO )
   xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
   if 92 - 92: ooOoO0O00 % i1iIi + i1iIi - iI11I1II1I1I . o0ii1I
iIIi1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'guide.xml' ) )
o0Ooo0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/catchup' , 'g' ) )
if 55 - 55: iI11I1II1I1I * IiI1i11I
def ooIi11iI ( ) :
 I1ii1Ii1 = "http://piesustv.net:8000/get.php?username=" + OO0o + "&password=" + Ooo + "&type=m3u_plus&output=ts"
 try :
  OooooOoO = urllib2 . urlopen ( I1ii1Ii1 )
  print OooooOoO . getcode ( )
  OooooOoO . close ( )
  if 22 - 22: oooOo0oo0oo
  pass
  if 22 - 22: IiI1i11I * Iii - I1ii11iIi11i * o0o00Oo0O / Ii
 except urllib2 . HTTPError , II1iI1I11I :
  print II1iI1I11I . getcode ( )
  iIii1 . ok ( "[COLOR white]Expired Account[/COLOR]" , '[COLOR white]You cannot use this service with an expired account[/COLOR]' , ' ' , '[COLOR white]Please check your account information[/COLOR]' )
  sys . exit ( 1 )
  xbmc . executebuiltin ( "Dialog.Close(busydialog)" )
  if 78 - 78: I1ii11iIi11i * o0o00Oo0O / i1iIi + ii + oooOo0oo0oo
 O0O00Oo = "http://piesustv.net:8000/xmltv.php?username=%s&password=%s" % ( OO0o , Ooo )
 I1iiIiiIiiI ( O0O00Oo , o0Ooo0o0Oo + "uide.xml" )
 if 94 - 94: ooOoO0O00
 IiII111i1i11 = open ( iIIi1 , 'r+' )
 input = open ( iIIi1 ) . read ( ) . decode ( 'UTF-8' )
 iiIIi1 = unicodedata . normalize ( 'NFKD' , input ) . encode ( 'ASCII' , 'ignore' )
 IiII111i1i11 . write ( iiIIi1 )
 IiII111i1i11 . truncate ( )
 IiII111i1i11 . close ( )
 ooIiI11i1I11111 ( )
 if 34 - 34: oOo0O0Ooo * OOooOOo * i1i1I1IIii1II + Ii1I
def ooIiI11i1I11111 ( ) :
 open = OooOoooOo ( II1iO00Oo )
 all = I1111ii11IIII ( open , '{"num' , 'direct' )
 for IiIi1II111I in all :
  if '"tv_archive":1' in IiIi1II111I :
   OOoO = O0oo0 ( IiIi1II111I , '"epg_channel_id":"' , '"' )
   o00oIIi1i1 = O0oo0 ( IiIi1II111I , '"stream_icon":"' , '"' ) . replace ( '\/' , '/' )
   id = O0oo0 ( IiIi1II111I , 'stream_id":"' , '"' )
   OOoO = OOoO . replace ( 'ENT:' , '[COLOR blue]ENT:[/COLOR]' ) . replace ( 'DOC:' , '[COLOR blue]DOC:[/COLOR]' ) . replace ( 'MOV:' , '[COLOR blue]MOV:[/COLOR]' ) . replace ( 'SSS:' , '[COLOR blue]SSS[/COLOR]' ) . replace ( 'BTS:' , '[COLOR blue]BTS:[/COLOR]' ) . replace ( 'TEST' , '[COLOR blue]TEST[/COLOR]' ) . replace ( 'Install' , '[COLOR blue]Install[/COLOR]' ) . replace ( '24/7' , '[COLOR blue]24/7[/COLOR]' ) . replace ( 'INT:' , '[COLOR blue]INT:[/COLOR]' ) . replace ( 'DE:' , '[COLOR blue]DE:[/COLOR]' ) . replace ( 'FR:' , '[COLOR blue]FR:[/COLOR]' ) . replace ( 'PL:' , '[COLOR blue]PL:[/COLOR]' ) . replace ( 'AR:' , '[COLOR blue]AR:[/COLOR]' ) . replace ( 'LIVE:' , '[COLOR blue]LIVE:[/COLOR]' ) . replace ( 'ES:' , '[COLOR blue]ES:[/COLOR]' ) . replace ( 'IN:' , '[COLOR blue]IN:[/COLOR]' ) . replace ( 'PK:' , '[COLOR blue]PK:[/COLOR]' )
   Iii1I1I11iiI1 ( OOoO , 'url' , 90027 , o00oIIi1i1 , oooOo0OOOoo0 , OOoO )
   if 38 - 38: ooOoO0O00 . Ii
   if 93 - 93: Iii * IIiIiII11i / o0ii1I - I11i
def Oo0oo ( name , description ) :
 name = str ( name . replace ( '[COLOR blue]ENT:[/COLOR]' , 'ENT:' ) . replace ( '[COLOR blue]DOC:[/COLOR]' , 'DOC:' ) . replace ( '[COLOR blue]MOV:[/COLOR]' , 'MOV' ) . replace ( '[COLOR blue]SSSS[/COLOR]' , 'SSS:' ) . replace ( '[COLOR blue]BTS:[/COLOR]' , 'BTS:' ) . replace ( '[COLOR blue]INT:[/COLOR]' , 'INT:' ) . replace ( '[COLOR blue]DE:[/COLOR]' , 'DE:' ) . replace ( '[COLOR blue]FR:[/COLOR]' , 'FR:' ) . replace ( '[COLOR blue]PL:[/COLOR]' , 'PL:' ) . replace ( '[COLOR blue]AR:[/COLOR]' , 'AR:' ) . replace ( '[COLOR blue]LIVE:[/COLOR]' , 'LIVE:' ) . replace ( '[COLOR blue]ES:[/COLOR]' , 'ES:' ) . replace ( '[COLOR blue]IN:[/COLOR]' , 'IN:' ) . replace ( '[COLOR blue]PK:[/COLOR]' , 'PK' ) )
 Oo00OOoOo = open ( iIIi1 )
 oOoo = ElementTree . parse ( Oo00OOoOo )
 I1ii1i1iiii = "apples"
 import datetime as dt
 from datetime import time
 I1i1I = datetime . now ( ) - timedelta ( days = 5 )
 I1i = str ( I1i1I )
 I1IIIii = str ( datetime . now ( ) ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
 i1111iI1 = oOoo . findall ( "programme" )
 for Oo0oOOOOo in i1111iI1 :
  if name in Oo0oOOOOo . attrib . get ( 'channel' ) :
   iiiO000OOO = Oo0oOOOOo . attrib . get ( 'start' )
   o0IIi1 , O00O00o , I11IiI1iI = iiiO000OOO . partition ( ' +' )
   I1i = str ( I1i ) . replace ( '-' , '' ) . replace ( ':' , '' ) . replace ( ' ' , '' )
   ii1IiiII , O0OO0OoO , iII1 = iiiO000OOO . partition ( '2017' )
   o0OOo = Oo0oOOOOo . find ( 'title' ) . text + iiiO000OOO
   iII1 = iII1 [ : - 6 ]
   if o0IIi1 > I1i :
    if o0IIi1 < I1IIIii :
     IiI1Ii11Ii = o0IIi1
     IiI1Ii11Ii = IiI1Ii11Ii [ : 4 ] + '/' + IiI1Ii11Ii [ 4 : ]
     o0IIi1 = o0IIi1 [ : 4 ] + '-' + o0IIi1 [ 4 : ]
     IiI1Ii11Ii = IiI1Ii11Ii [ : 7 ] + '/' + IiI1Ii11Ii [ 7 : ]
     o0IIi1 = o0IIi1 [ : 7 ] + '-' + o0IIi1 [ 7 : ]
     IiI1Ii11Ii = IiI1Ii11Ii [ : 10 ] + ' - ' + IiI1Ii11Ii [ 10 : ]
     o0IIi1 = o0IIi1 [ : 10 ] + ':' + o0IIi1 [ 10 : ]
     IiI1Ii11Ii = IiI1Ii11Ii [ : 15 ] + ':' + IiI1Ii11Ii [ 15 : ]
     o0IIi1 = o0IIi1 [ : 13 ] + '-' + o0IIi1 [ 13 : ]
     IiI1Ii11Ii = IiI1Ii11Ii [ : - 2 ]
     o0IIi1 = o0IIi1 [ : - 2 ]
     OoO0oO0oo0O = ( "http://piesustv.net:8000/streaming/timeshift.php?username=%s&password=%s&stream=%s&start=" ) % ( OO0o , Ooo , description )
     I1ii1i1iiii = OoO0oO0oo0O + str ( o0IIi1 ) + "&duration=240"
     IiI1Ii11Ii = '[COLOR blue]%s - [/COLOR]' % IiI1Ii11Ii
     o0OOo = str ( IiI1Ii11Ii ) + Oo0oOOOOo . find ( 'title' ) . text
     OOOiiiiI = Oo0oOOOOo . find ( 'desc' ) . text
     iI1Ii1iI11iiI ( o0OOo , I1ii1i1iiii , 222 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , OOOiiiiI )
     if 82 - 82: ii . o0ii1I
def I1iiIiiIiiI ( url , dest ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching latest Catch Up' , "Fetching latest Catch Up..." , ' ' , ' ' )
 o0oOoO00o . update ( 0 )
 III1ii = time . time ( )
 urllib . urlretrieve ( url , dest , lambda iII1ii , o0oOoO00 , oOO000 : OoOooO ( iII1ii , o0oOoO00 , oOO000 , o0oOoO00o , III1ii ) )
def OoOooO ( numblocks , blocksize , filesize , dp , start_time ) :
 try :
  OoO0o00OOOOO = min ( numblocks * blocksize * 100 / filesize , 100 )
  I1iIi1iIIIIiI = float ( numblocks ) * blocksize / ( 1024 * 1024 )
  O000oooOO0Oo0 = numblocks * blocksize / ( time . time ( ) - start_time )
  if O000oooOO0Oo0 > 0 :
   I1iIiIii = ( filesize - numblocks * blocksize ) / O000oooOO0Oo0
  else :
   I1iIiIii = 0
  O000oooOO0Oo0 = O000oooOO0Oo0 / 1024
  OO0 = O000oooOO0Oo0 / 1024
  I1iiI1iiI1i1 = float ( filesize ) / ( 1024 * 1024 )
  OOOO00OOO00 = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % ( I1iIi1iIIIIiI )
  II1iI1I11I = '[COLOR white]Speed:  %.02f Mb/s ' % OO0 + '[/COLOR]'
  dp . update ( OoO0o00OOOOO , OOOO00OOO00 , II1iI1I11I )
 except :
  OoO0o00OOOOO = 100
  dp . update ( OoO0o00OOOOO )
 if dp . iscanceled ( ) :
  ii1OO0 = xbmcgui . Dialog ( )
  ii1OO0 . ok ( "GenieTv" , 'The download was cancelled.' )
  if 96 - 96: o0o00Oo0O . IiI1i11I - oOo0O0Ooo * I1ii11iIi11i
  sys . exit ( )
  dp . close ( )
  if 68 - 68: i1i1I1IIii1II - I1ii11iIi11i / OOooOOo - i1IiiiI1iI . IiI1i11I
def iiI11Ii1i ( ) :
 if Ooo == 'insert_password' :
  iIii1 . ok ( '[COLOR' + ooOoOoo0O + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + ooOoOoo0O + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  O0O0O0o ( )
  if 83 - 83: IiI1i11I % Iii
  if 6 - 6: OOooOOo / i1iIi + IiI1i11I - I11i * oooOo0oo0oo + i1iIi
  if 76 - 76: IIiIiII11i - ii % III1iiIii
  if 40 - 40: o0ii1I
  if 59 - 59: Iii * ii + oooOo0oo0oo . iI11I1II1I1I / ooOoO0O00
  if 75 - 75: Iii . oooOo0oo0oo - iI11I1II1I1I * oO0o * IiI1i11I
  if 93 - 93: i1iIi
  if 18 - 18: i1iIi
def O0O0O0o ( ) :
 iiI111I1iIiI = OooOoooOo ( 'http://piesustv.net:8000/panel_api.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 for O0O00Oo in IIi :
  dt = datetime . fromtimestamp ( float ( IIi [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iIii1 . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + ooOoOoo0O + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + ooOoOoo0O + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + ooOoOoo0O + '] To Purchase A licence[/COLOR]' )
def OOOooO00OO00O ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '"username":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OoOOooO0O = re . compile ( '"password":"(.+?)"' ) . findall ( iiI111I1iIiI )
 OooO0oOo = re . compile ( '"status":"(.+?)"' ) . findall ( iiI111I1iIiI )
 i1Iii1i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( iiI111I1iIiI )
 IiIi1I1 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( iiI111I1iIiI )
 I1i11 = re . compile ( '"created_at":"(.+?)"' ) . findall ( iiI111I1iIiI )
 oOOo00O0OOOo = re . compile ( '"max_connections":"(.+?)"' ) . findall ( iiI111I1iIiI )
 o000o0O0Oo00 = re . compile ( '"is_trial":"1"' ) . findall ( iiI111I1iIiI )
 Ii1Ii = re . compile ( '"is_trial":"0"' ) . findall ( iiI111I1iIiI )
 Ii11iIII = o0ooOO0OOO00o ( )
 OoOoO0ooooO0 = IIII1ii1 ( )
 for url in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']My GTV Account Information[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OoOOooO0O :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in OooO0oOo :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in I1i11 :
  dt = datetime . fromtimestamp ( float ( I1i11 [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Created:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in i1Iii1i1I :
  dt = datetime . fromtimestamp ( float ( i1Iii1i1I [ 0 ] ) )
  dt . strftime ( '%Y-%m-%d %H:%M:%S' )
  if I1IIIii <= dt <= I1IIIii + timedelta ( hours = 24 ) :
   iiIi1IIiI ( '[COLORred]Expires Today[/COLOR]' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Expires:[/COLOR]  %s' % ( dt ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in IiIi1I1 :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in oOOo00O0OOOo :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in o000o0O0Oo00 :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] Yes' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 for url in Ii1Ii :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Trial:[/COLOR] No' , '' , '' , iiIi1IIiIi + 'MyAcc.png' )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']Get Short Links[/COLOR]' , '' , 100214 , iiIi1IIiIi + 'shortlinks.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Local IP Address:[/COLOR] ' + Ii11iIII , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']External IP Address:[/COLOR] ' + OoOoO0ooooO0 , '' , '' , iiIi1IIiIi + 'CheckMyIP.png' , Oo00OOOOO , '' )
 if 52 - 52: oO0o - oooOo0oo0oo - i1iIi - I11i + ooOoO0O00
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 10 - 10: ii / IiI1i11I / i1i1I1IIii1II * I1ii11iIi11i / iI11I1II1I1I
def oO0OoiIi111iII1 ( ) :
 iIii1 . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
 o0OIi ( )
 iIii1 . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 11 - 11: i1i1I1IIii1II . oOo0O0Ooo + III1iiIii / ooOoO0O00
def iIi1i1i1II11I ( data ) :
 O0OOOO0OooOo = len ( data ) % 4
 if 13 - 13: o0o00Oo0O % i1iIi % Iii
 if 25 - 25: ii % o0ii1I * IIiIiII11i - oO0o
 if 95 - 95: oOo0O0Ooo % i1IiiiI1iI * oOo0O0Ooo + o0o00Oo0O . i1IiiiI1iI % ii
 if 6 - 6: OOooOOo - i1iIi * I11i + OOooOOo % I11i
 if 100 - 100: oO0o % i1IiiiI1iI - Iii % Iii % Iii / i1iIi
 if 83 - 83: i1i1I1IIii1II - i1iIi - III1iiIii % ooOoO0O00 - IiI1i11I . I11i
 if O0OOOO0OooOo != 0 :
  data += b'=' * ( 4 - O0OOOO0OooOo )
 return base64 . decodestring ( data )
def O0oo0 ( text , from_string , to_string , excluding = True ) :
 if excluding :
  try : oOo0oO = re . search ( "(?i)" + from_string + "([\S\s]+?)" + to_string , text ) . group ( 1 )
  except : oOo0oO = ''
 else :
  try : oOo0oO = re . search ( "(?i)(" + from_string + "[\S\s]+?" + to_string + ")" , text ) . group ( 1 )
  except : oOo0oO = ''
 return oOo0oO
 if 77 - 77: IIiIiII11i
 if 30 - 30: Ii1I % ooOoO0O00
def I1111ii11IIII ( text , start_with , end_with ) :
 oOo0oO = re . findall ( "(?i)(" + start_with + "[\S\s]+?" + end_with + ")" , text )
 return oOo0oO
def o0ooOO0OOO00o ( ) :
 I1iIIIIIi = socket . socket ( socket . AF_INET , socket . SOCK_DGRAM )
 I1iIIIIIi . connect ( ( '8.8.8.8' , 0 ) )
 I1iIIIIIi = I1iIIIIIi . getsockname ( ) [ 0 ]
 return I1iIIIIIi
 if 36 - 36: III1iiIii
def IIII1ii1 ( ) :
 open = OooOoooOo ( 'http://canyouseeme.org/' )
 Ii11iIII = re . search ( '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' , open )
 return str ( Ii11iIII . group ( ) )
II1iI111iiIIiI1I = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( OO0o , Ooo )
II1iO00Oo = 'http://piesustv.net:8000/panel_api.php?username=%s&password=%s' % ( OO0o , Ooo )
iIi = 'http://piesustv.net:8000/movie/%s/%s/' % ( OO0o , Ooo )
oOo = 'http://piesustv.net:8000/live/%s/%s/' % ( OO0o , Ooo )
ooOo0o = '&action=get_live_categories'
IIIIiiI = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( OO0o , Ooo )
ooO00Oo = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( OO0o , Ooo )
if 75 - 75: ii . oooOo0oo0oo + oO0o / o0ii1I - oOo0O0Ooo % o0ii1I
oooOOOOOi1iIii = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_vod_streams&cat_id=' % ( OO0o , Ooo )
O0OooooO0o0O0 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( OO0o , Ooo )
oO0oo = 'http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_categories' % ( OO0o , Ooo )
o00o0o000Oo = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( OO0o , Ooo )
if 100 - 100: ooOoO0O00 - Ii . i1IiiiI1iI * oO0o
def oOIIII ( ) :
 I1IIII ( )
 open = OooOoooOo ( oO0oo )
 o0O0ooooooo00 = I1111ii11IIII ( open , '<channel>' , '</channel>' )
 for IiIi1II111I in o0O0ooooooo00 :
  OOoO = O0oo0 ( IiIi1II111I , '<title>' , '</title>' )
  OOoO = base64 . b64decode ( OOoO )
  iiI11ii1111 = O0oo0 ( IiIi1II111I , '<playlist_url>' , '</playlist_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  Iii1I1I11iiI1 ( '[COLORsteelblue]' + OOoO + '[/COLOR]' , iiI11ii1111 , 60003 , iiIi1IIiIi + 'GTV.png' , Oo00OOOOO , '' )
  if 65 - 65: IIiIiII11i / I1ii11iIi11i
def iiII1i ( url ) :
 open = OooOoooOo ( o00o0o000Oo + url )
 o0O0ooooooo00 = I1111ii11IIII ( open , '<channel>' , '</channel>' )
 for IiIi1II111I in o0O0ooooooo00 :
  OOoO = O0oo0 ( IiIi1II111I , '<title>' , '</title>' )
  OOoO = base64 . b64decode ( OOoO )
  xbmc . log ( str ( OOoO ) )
  o00oIIi1i1 = O0oo0 ( IiIi1II111I , '<desc_image>' , '</desc_image>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  iiI11ii1111 = O0oo0 ( IiIi1II111I , '<stream_url>' , '</stream_url>' ) . replace ( '<![CDATA[' , '' ) . replace ( ']]>' , '' )
  OOOiiiiI = O0oo0 ( IiIi1II111I , '<description>' , '</description>' )
  OOOiiiiI = base64 . b64decode ( OOOiiiiI )
  IiiiI1I1IIIi = '('
  I1iOo00oOO00 = ')'
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , iiI11ii1111 , 222 , o00oIIi1i1 , oooOo0OOOoo0 , ( '[COLOR' + ooOoOoo0O + ']' + OOOiiiiI + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( I1iOo00oOO00 , '[COLORsteelblue]' ) . replace ( IiiiI1I1IIIi , '[COLORorangered]' ) )
  if 21 - 21: ii . IIiIiII11i - III1iiIii * i1iIi * III1iiIii
def IiI1IiI1iiI1 ( url ) :
 url = url
 II11iIiIIIiI = OooOoooOo ( IIIIiiI + url )
 IIi = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , type , i1oO , i11I1I1iiI in IIi :
  iIIi1IIi = ( oOo + i1oO + '.m3u8' ) . strip ( )
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , iIIi1IIi , 222 , ( i11I1I1iiI ) . replace ( '\/' , '/' ) + 'jpg' , Oo00OOOOO , type )
  oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
def O000o0 ( url , name , img ) :
 img = img
 name = name
 url = url
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/xmltv.php?username=' + OO0o + '&password=' + Ooo )
 IIi = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for IIiIIiI , Iiiii1 in IIi :
  if name == IIiIIiI :
   iI1Ii1iI11iiI ( ( '' + name + '' ) . replace ( '_' , ' ' ) + Iiiii1 , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   iI1Ii1iI11iiI ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def O0Ooo0O ( name ) :
 iii1oOo0OoOOOo0 = name
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( II11iIiIIIiI )
 for name , iIiIi11 , O0O00Oo in IIi :
  O0O00Oo = ( O0O00Oo ) . replace ( '.ts' , '.m3u8' )
  iI1Ii1iI11iiI ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( O0O00Oo ) . strip ( ) , 222 , iIiIi11 , iIiIi11 , '' )
 else :
  iI1Ii1iI11iiI ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 55 - 55: i1i1I1IIii1II + o0o00Oo0O / IiI1i11I % i1iIi / ii
  if 98 - 98: o0ii1I * iI11I1II1I1I % I1ii11iIi11i % oooOo0oo0oo
  if 88 - 88: IiI1i11I - IIiIiII11i / IiI1i11I - o0ii1I
  if 16 - 16: I1ii11iIi11i % i1IiiiI1iI
  if 10 - 10: III1iiIii / ii
  if 50 - 50: Ii - ii . i1i1I1IIii1II + o0o00Oo0O . ooOoO0O00
  if 91 - 91: I11i . IiI1i11I % I1ii11iIi11i - IiI1i11I . i1i1I1IIii1II % Ii
  if 25 - 25: iI11I1II1I1I
  if 63 - 63: i1iIi
  if 96 - 96: Iii
  if 34 - 34: OOooOOo / oO0o - oOo0O0Ooo . o0o00Oo0O . oooOo0oo0oo
  if 63 - 63: IiI1i11I
def iiIiii1iI1i ( ) :
 Iii1I1I11iiI1 ( 'Full Backup' , '' , 10061 , iiIi1IIiIi + 'FullBackUp.png' , Oo00OOOOO , 'Back Up Your Full System' )
 if os . path . exists ( Oo0oOOo ) :
  Iii1I1I11iiI1 ( 'Backup Genie Favourites' , O0O00Oo , 10062 , iiIi1IIiIi + 'BackupGenieFavourites.png' , Oo00OOOOO , 'Back Up Your favourites' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  Iii1I1I11iiI1 ( 'Backup Ivue Config' , Ii1iIiII1ii1 , 10062 , iiIi1IIiIi + 'BackUpIvueConfig.png' , Oo00OOOOO , 'Back Up Your master.db' )
 if os . path . exists ( ooOooo000oOO ) :
  Iii1I1I11iiI1 ( 'Backup Kodi Favourites' , ooOooo000oOO , 10062 , iiIi1IIiIi + 'BackKodiFavourites.png' , Oo00OOOOO , 'Back Up Your favourites.xml' )
  if 11 - 11: IiI1i11I - iI11I1II1I1I
  if 92 - 92: oO0o
  if 15 - 15: III1iiIii / III1iiIii + iI11I1II1I1I % ii
zip = oo00 . getSetting ( 'zip' )
iIIi111IiII1i = xbmc . translatePath ( os . path . join ( zip ) )
def oOo0O000oo0 ( ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 15 - 15: I1ii11iIi11i / o0ii1I % o0o00Oo0O + Ii1I
  if 96 - 96: i1iIi . ii
  if 39 - 39: oooOo0oo0oo + oO0o
def oOoOOOO0OOO ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Oo0oOOo
  elif 'Ivue' in name :
   url = Ii1iIiII1ii1
  elif 'Kodi' in name :
   url = ooOooo000oOO
  oOo0O000oo0 ( )
  O0oo0oO00o = open ( url ) . read ( )
  I1ii111i1ii1 = os . path . join ( iIIi111IiII1i , description . split ( 'Your ' ) [ 1 ] )
  IiII111i1i11 = open ( I1ii111i1ii1 , mode = 'w' )
  IiII111i1i11 . write ( O0oo0oO00o )
  IiII111i1i11 . close ( )
 else :
  if 'guisettings.xml' in description :
   IiIi1II111I = open ( os . path . join ( iIIi111IiII1i , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oOo0oO = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIi = re . compile ( oOo0oO ) . findall ( IiIi1II111I )
   for type , o0Ii11iIiiI , o000 in IIi :
    o000 = o000 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , o0Ii11iIiiI , o000 ) )
  else :
   I1ii111i1ii1 = os . path . join ( url )
   O0oo0oO00o = open ( os . path . join ( iIIi111IiII1i , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiII111i1i11 = open ( I1ii111i1ii1 , mode = 'w' )
   IiII111i1i11 . write ( O0oo0oO00o )
   IiII111i1i11 . close ( )
 iIii1 . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 30 - 30: o0ii1I + IIiIiII11i % ii
 if 89 - 89: o0ii1I
 if 51 - 51: IiI1i11I
 if 68 - 68: IiI1i11I - I11i * oO0o % i1iIi . i1iIi - iI11I1II1I1I
def Ii1IOoO0o0O ( ) :
 iIoOoO0 = 1
 oOo0O000oo0 ( )
 Iii1II1ii = xbmc . translatePath ( os . path . join ( iIIi111IiII1i , 'Build Backup' , 'Full Backup' , '' ) )
 ooOo00 = xbmc . translatePath ( os . path . join ( iIIi111IiII1i , 'Build Backup' , 'my_full_backup.zip' ) )
 OO0III = xbmc . translatePath ( os . path . join ( iIIi111IiII1i , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( Iii1II1ii ) :
  os . makedirs ( Iii1II1ii )
 OoO0o = iIii1 . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not OoO0o ) : return False , 0
 OO0o0O0O0O0 = OoO0o
 iI11IiIiiII1 = xbmc . translatePath ( os . path . join ( Iii1II1ii , OO0o0O0O0O0 + '.zip' ) )
 I11iii1i = [ 'plugin.video.GenieTv' ]
 ii1i1Iii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 oO00oO00O0Oo = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OO0o0o0oo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iIiII1 = "Creating full backup of existing build"
 i111iii1I1 = "Creating Community Build"
 iiIiII1 = "Archiving..."
 ii111iI = ""
 ii11I1 = "Please Wait"
 I1I ( oOo0oooo00o , iI11IiIiiII1 , i111iii1I1 , iiIiII1 , ii111iI , ii11I1 , oO00oO00O0Oo , OO0o0o0oo )
 time . sleep ( 1 )
 oOO0o0 = xbmc . translatePath ( os . path . join ( Iii1II1ii , OO0o0O0O0O0 + '_guisettings.zip' ) )
 Ii1Ii1 = zipfile . ZipFile ( oOO0o0 , mode = 'w' )
 try :
  Ii1Ii1 . write ( xbmc . translatePath ( os . path . join ( oOo0oooo00o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 Ii1Ii1 . close ( )
 if iIoOoO0 == 0 :
  iIii1 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  iIii1 . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  iIii1 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + ooOo00 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + iI11IiIiiII1 + '[/COLOR]' )
  if 62 - 62: i1IiiiI1iI * Iii
def I1I ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 oOooOOoO0oO0oo0O = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 oO00Oo = len ( sourcefile )
 oO00OOOOOO0o = [ ]
 iIII = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for OoO0000 , III11iIIi , iIIi in os . walk ( sourcefile ) :
  for file in iIIi :
   iIII . append ( file )
 i1I111iIii1i1 = len ( iIII )
 for OoO0000 , III11iIIi , iIIi in os . walk ( sourcefile ) :
  III11iIIi [ : ] = [ o0Oo for o0Oo in III11iIIi if o0Oo not in exclude_dirs ]
  iIIi [ : ] = [ IiII111i1i11 for IiII111i1i11 in iIIi if IiII111i1i11 not in exclude_files ]
  for file in iIIi :
   oO00OOOOOO0o . append ( file )
   i1II11i1iI1 = len ( oO00OOOOOO0o ) / float ( i1I111iIii1i1 ) * 100
   o0oOoO00o . update ( int ( i1II11i1iI1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   OO0IIi1II11 = os . path . join ( OoO0000 , file )
   if not 'temp' in III11iIIi :
    if not 'plugin.program.originwizard' in III11iIIi :
     import time
     o0ooOOOo = '01/01/1980'
     OOoOOo0oO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( OO0IIi1II11 ) ) )
     if OOoOOo0oO > o0ooOOOo :
      oOooOOoO0oO0oo0O . write ( OO0IIi1II11 , OO0IIi1II11 [ oO00Oo : ] )
 oOooOOoO0oO0oo0O . close ( )
 o0oOoO00o . close ( )
 if 25 - 25: o0ii1I % IIiIiII11i - i1i1I1IIii1II * Ii1I - iI11I1II1I1I
 if 46 - 46: IIiIiII11i . o0o00Oo0O * I1ii11iIi11i + IiI1i11I
def iioOo00oooOO ( ) :
 iii ( )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , iiIi1IIiIi + 'scoob.png' , Oo00OOOOO , '' )
 if 4 - 4: OOooOOo * I11i - Iii . ii * Ii . I11i
 if 16 - 16: ooOoO0O00 . ooOoO0O00 / i1IiiiI1iI % OOooOOo / oOo0O0Ooo * Ii1I
def IIIii11 ( ) :
 iii ( )
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH SERIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH YOUTUBE[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Search Genie[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  I1IiiI1ii1i ( )
 if o0Oo00 == 1 :
  O0OoO0ooOO0o ( )
 if o0Oo00 == 2 :
  I11iIiI1 ( )
 if o0Oo00 == 3 :
  IiIIII1iiIIi ( )
  if 29 - 29: o0ii1I - o0ii1I / i1iIi
  if 49 - 49: Iii + i1i1I1IIii1II % oO0o - I1ii11iIi11i - o0o00Oo0O - ii
  if 4 - 4: IIiIiII11i - i1i1I1IIii1II % I1ii11iIi11i * Ii
  if 18 - 18: I1ii11iIi11i % o0o00Oo0O
  if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
  if 47 - 47: Ii1I * i1i1I1IIii1II + iI11I1II1I1I - i1i1I1IIii1II / III1iiIii
  if 86 - 86: III1iiIii
  if 43 - 43: oOo0O0Ooo / IiI1i11I / i1iIi + iI11I1II1I1I + ii
  if 33 - 33: IIiIiII11i - III1iiIii - i1iIi
def oO00oOoo00o0 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']RaysRavers[/COLOR]' , '[COLOR' + ooOoOoo0O + ']QuickSilver[/COLOR]' , '[COLOR' + ooOoOoo0O + ']RadioNomy[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']UK RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']WORLD RADIO[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CONCERTS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC[/COLOR]' , '[COLOR' + ooOoOoo0O + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Music[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OOo00OoO ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if o0Oo00 == 1 :
   OOo00OoO ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if o0Oo00 == 2 :
   III1I ( )
  if o0Oo00 == 3 :
   OOOii ( )
  if o0Oo00 == 4 :
   Iii1I11 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if o0Oo00 == 5 :
   O0o0o ( )
  if o0Oo00 == 6 :
   IiiiIi1111I ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if o0Oo00 == 7 :
   iII1i1ii ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if o0Oo00 == 8 :
   i1I1ii1i ( str ( oO0000OOo00 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if o0Oo00 == 9 :
   iiiiII11iIi ( )
  if o0Oo00 == 10 :
   OO00 ( )
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
  if 52 - 52: IIiIiII11i / oOo0O0Ooo . i1i1I1IIii1II * III1iiIii . Iii
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 25 - 25: Ii / OOooOOo - i1IiiiI1iI / oO0o . I11i . I11i
def iI1iIIII1 ( ) :
 iii ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']KILL KODI[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SPEEDTEST[/COLOR]' , '[COLOR' + ooOoOoo0O + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE CACHE[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']FORCE REFRESH[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CHECK MY IP[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Maintenance[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   Oooo ( )
  if o0Oo00 == 1 :
   o0OO0 ( )
  if o0Oo00 == 2 :
   Iii1I1111ii ( )
  if o0Oo00 == 3 :
   iI1I ( O0O00Oo )
  if o0Oo00 == 4 :
   Iii1IiI1iI1I ( O0O00Oo )
  if o0Oo00 == 5 :
   ii1iii1i ( )
  if o0Oo00 == 6 :
   Iiii ( url = 'http://www.iplocation.net/' , inc = 1 )
  if o0Oo00 == 7 :
   oOii11I ( )
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
  if 97 - 97: ooOoO0O00 + IiI1i11I . i1iIi - IiI1i11I
  if 53 - 53: o0o00Oo0O . oOo0O0Ooo
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 74 - 74: i1iIi % OOooOOo / I1ii11iIi11i
 if 2 - 2: III1iiIii % III1iiIii % i1IiiiI1iI
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
 if 60 - 60: oooOo0oo0oo
 if 73 - 73: i1iIi
def OOoO0o0O0 ( ) :
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
 if 88 - 88: oO0o * I11i * oooOo0oo0oo / I1ii11iIi11i * oO0o
def I1ii1ii11i1I ( ) :
 iii ( )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']My Local Zip[/COLOR]' , O0OoO000O0OO , 48 , iiIi1IIiIi + 'MyLocalZIP.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']My Online Zip[/COLOR]' , oOOoO0 , 43 , iiIi1IIiIi + 'MyOnlineZip.png' , Oo00OOOOO , '' )
 if 100 - 100: I11i . oOo0O0Ooo
def o00o0O0 ( ) :
 iii ( )
 iI1Ii1iI11iiI ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( oO0000OOo00 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , iiIi1IIiIi + 'FTV4.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( oO0000OOo00 ) + '/wizard/customftv/settings.xml' , 17 , iiIi1IIiIi + 'FTV3.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , iiIi1IIiIi + 'FTV1.png' , Oo00OOOOO , '' )
 iI1Ii1iI11iiI ( 'RESET FTV DATABASE' , 'url' , 18 , iiIi1IIiIi + 'FTV2.png' , Oo00OOOOO , '' )
 if 47 - 47: i1iIi
 if 63 - 63: IIiIiII11i / Ii % IIiIiII11i . Ii1I
 if 6 - 6: oooOo0oo0oo + Ii
def i1I1i ( ) :
 iii ( )
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']SKINS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + ooOoOoo0O + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  iiIiiII1II1ii ( )
 if o0Oo00 == 0 :
  i1iI1iiI ( O0O00Oo )
 if o0Oo00 == 0 :
  iIII1IiI ( O0O00Oo )
  if 32 - 32: OOooOOo % oO0o + Ii + i1iIi - o0ii1I + i1i1I1IIii1II
  if 31 - 31: iI11I1II1I1I - I11i
  if 57 - 57: I1ii11iIi11i % oO0o
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 1 - 1: OOooOOo * o0o00Oo0O . i1i1I1IIii1II % o0o00Oo0O + IIiIiII11i
def i1Oo ( ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIi = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( iiI111I1iIiI )
 for iIiIi11 , OOoO in IIi :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , iIiIi11 , iIiIi11 , '' )
 oOI1Ii1I1 ( 'tvshows' , 'INFO' )
 if 15 - 15: ooOoO0O00 + III1iiIii % oOo0O0Ooo / Ii * OOooOOo
def oOiI1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( i111I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 5 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 69 - 69: oO0o - ii - oooOo0oo0oo % Iii / OOooOOo - IIiIiII11i
def iiIiiII1II1ii ( ) :
 iii ( )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']GOTHAM SKINS[/COLOR]' , str ( oO0000OOo00 ) , 36 , iiIi1IIiIi + 'GothamSkins.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']HELIX SKINS[/COLOR]' , str ( oO0000OOo00 ) , 37 , iiIi1IIiIi + 'HelixSkins.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']ISENGAARD SKINS[/COLOR]' , oOo0oooo00o , 38 , iiIi1IIiIi + 'IsengaardSkins.png' , Oo00OOOOO , '' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 67 - 67: oooOo0oo0oo + oooOo0oo0oo + oO0o . Ii + Ii1I + Ii
def IIi11I1i1I1I ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiII1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 72 - 72: o0ii1I / I1ii11iIi11i / i1i1I1IIii1II * OOooOOo + oooOo0oo0oo
def OOoo0OOOo0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iI1111i1i11Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 62 - 62: IiI1i11I
def I11i1I1Ii ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + iii11I1i11IIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 19 - 19: i1i1I1IIii1II * IiI1i11I + OOooOOo - i1i1I1IIii1II + Ii1I
def iIii1ii ( url ) :
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 24 - 24: ooOoO0O00 / i1IiiiI1iI * Iii / o0o00Oo0O
def i1iI1iiI ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOOOo0oO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 40 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 3 - 3: oOo0O0Ooo / iI11I1II1I1I % I11i
def O0oo0000o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + OOoO0oooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 5 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 66 - 66: IiI1i11I / Ii * o0o00Oo0O
def iI ( ) :
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']GenieTv Apps[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Factory[/COLOR]' , '[COLOR' + ooOoOoo0O + ']APK Search[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']APK TOOL[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  O000Oo00 ( )
 if o0Oo00 == 1 :
  iI1oOoo ( )
 if o0Oo00 == 2 :
  o00O0o00oo ( )
  if 19 - 19: oOo0O0Ooo
  if 66 - 66: i1i1I1IIii1II / OOooOOo
  if 13 - 13: IIiIiII11i
  if 55 - 55: I1ii11iIi11i % ooOoO0O00 * Iii
def iI1oOoo ( ) :
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIi = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , OOOo0o0Oooo0o0oO0 in IIi :
  iIiiiii1i ( 'Android Apps' + OOOo0o0Oooo0o0oO0 , 'https://www.apkfiles.com' + O0O00Oo , 30035 , iiIi1IIiIi + 'apps.png' )
 for O0O00Oo , OOOo0o0Oooo0o0oO0 in i1Iii1i1I :
  iIiiiii1i ( 'Android Games' + OOOo0o0Oooo0o0oO0 , 'https://www.apkfiles.com' + O0O00Oo , 30035 , iiIi1IIiIi + 'GAMES.png' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
def IIIiIiiI1i ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '/cat' in url :
   iIiiiii1i ( ( OOoO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def I1IiiiI ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '/app' in url :
   iIiiiii1i ( ( OOoO ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , iiIi1IIiIi + 'APK.png' )
def iIiI1111 ( url ) :
 I11iiii = OooOoooOo ( url )
 iiI11ii1111 = url
 if "page=" in str ( url ) :
  iiI11ii1111 = url . split ( '?' ) [ 0 ]
 IIi = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  if 'apk' in url :
   iI1Ii1iI11iiI ( ( OOoO ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + iIiIi11 )
 if len ( i1Iii1i1I ) > 1 :
  i1Iii1i1I = str ( i1Iii1i1I [ len ( i1Iii1i1I ) - 1 ] )
 iI1Ii1iI11iiI ( 'Next Page' , iiI11ii1111 + str ( i1Iii1i1I ) , 30037 , iiIi1IIiIi + 'Next.png' )
def O0OO00 ( name , url ) :
 I11iiii = o0O0Oo00 ( url )
 name = name
 IIi = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( I11iiii )
 for url in IIi :
  url = 'https://www.apkfiles.com' + url
  i1111I ( name , url , 'Brackets' )
def o00O0o00oo ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IiII = 'https://www.apkfiles.com/search?q=' + ( iii1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 oOO0oo = IIi1IiII . lower ( )
 iIiI1111 ( oOO0oo )
 if 58 - 58: ii - Iii + iI11I1II1I1I * Ii
def OoOiII11IiIi ( url ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( iII1I1i , 'Download' ) )
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
 if 6 - 6: i1i1I1IIii1II / o0o00Oo0O / o0ii1I / III1iiIii / i1i1I1IIii1II . iI11I1II1I1I
def oo0 ( url ) :
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
 if 87 - 87: Iii . Iii . IIiIiII11i / oooOo0oo0oo
 if 86 - 86: i1i1I1IIii1II % o0o00Oo0O + oO0o
def oO0OO ( name , url , description ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ooI1111i = os . path . join ( OO0OoOO0o0o , name )
 try :
  os . remove ( ooI1111i )
 except :
  pass
 downloader . download ( url , ooI1111i , o0oOoO00o )
 o0OOO = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o0OOO
 print '======================================='
 extract . all ( ooI1111i , o0OOO , o0oOoO00o )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 48 - 48: ii - i1IiiiI1iI . Ii * IiI1i11I - o0ii1I - I11i
 if 59 - 59: IiI1i11I / Iii . I1ii11iIi11i
 if 100 - 100: o0o00Oo0O
 if 94 - 94: Ii1I - I11i
 if 42 - 42: I11i * OOooOOo . oO0o - IiI1i11I / IIiIiII11i
def O000Oo00 ( ) :
 iiI111I1iIiI = OooOoooOo ( iI111I11I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIi = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( iiI111I1iIiI )
 for OOoO , O0O00Oo , i11I1I1iiI , oooOo0OOOoo0 , iII1ii11III in IIi :
  iI1Ii1iI11iiI ( OOoO , O0O00Oo , 80003 , i11I1I1iiI , iiIi1IIiIi + 'APKToolsB.png' , iII1ii11III )
def OOOO0oO0O ( apk , ret = None ) :
 if apk == "kodi" :
  ooooO = "https://kodi.tv/download/"
  iiI111I1iIiI = OooOoooOo ( ooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( iiI111I1iIiI )
  if len ( IIi ) == 1 :
   O000oooO0 = IIi [ 0 ] [ 0 ]
   OO0o0O0O0O0 = IIi [ 0 ] [ 1 ]
   oOO00 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( O000oooO0 , OO0o0O0O0O0 )
  if ret == 'version' : return O000oooO0
  else : return oOO00
 elif apk == "spmc" :
  oO0o00 = 'https://github.com/koying/SPMC/releases/latest/'
  iiI111I1iIiI = OooOoooOo ( oO0o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIi = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( iiI111I1iIiI )
  O000oooO0 = re . sub ( '<[^<]+?>' , '' , IIi [ 0 ] ) . replace ( ' ' , '' )
  oOO00 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( O000oooO0 , O000oooO0 )
  if ret == 'version' : return O000oooO0
  else : return oOO00
def i1111I ( name , url , Brackets ) :
 if OO0OO0O00oO0 ( ) == 'android' :
  Oo0OOOO0oOoo0 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not Oo0OOOO0oOoo0 : O0OIIII1i ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  i1I1Iiii = name
  if Oo0OOOO0oOoo0 :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not OOooo0O0o0 ( url ) == True : O0OIIII1i ( i1iiIIiiI111 , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % i1I1Iiii , '' , 'Please Wait' )
   ooI1111i = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( ooI1111i )
   except : pass
   downloader . download ( url , ooI1111i , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    Ii1Ii1 = zipfile . ZipFile ( ooI1111i )
    for file in Ii1Ii1 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iIIi1 , os . path . basename ( file ) ) , 'wb' ) as IiII111i1i11 :
       I1iIIIiiii = file . split ( '/' ) [ 1 ]
       IiII111i1i11 . write ( Ii1Ii1 . read ( file ) )
       xbmc . sleep ( 500 )
       IiII111i1i11 . close ( )
       try :
        os . remove ( ooI1111i )
       except :
        pass
       ooI1111i = os . path . join ( i1iIIi1 , I1iIIIiiii )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ooI1111i + '")' )
  else : O0OIIII1i ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : O0OIIII1i ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 44 - 44: i1IiiiI1iI / o0ii1I * oooOo0oo0oo * ooOoO0O00 . o0ii1I * Ii
 if 91 - 91: o0ii1I - IiI1i11I . ooOoO0O00 . Ii1I * I11i % IiI1i11I
 if 30 - 30: Iii
 if 85 - 85: IIiIiII11i + i1iIi * Iii
def i1ooOO00o0 ( ) :
 if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
 iiI111I1iIiI = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( iiI111I1iIiI )
 for O0O00Oo , OOoO in IIi :
  O0O00Oo = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + O0O00Oo )
  Ii1I1iIiiI1 ( ( OOoO ) . replace ( '_' , ' ' ) , O0O00Oo )
  if 68 - 68: IiI1i11I . Iii
def Ii1I1iIiiI1 ( name , url ) :
 if OO0OO0O00oO0 ( ) == 'android' :
  Oo0OOOO0oOoo0 = iIii1 . yesno ( i1iiIIiiI111 , "Would you like to download and install:" , "%s" % name )
  if not Oo0OOOO0oOoo0 : O0OIIII1i ( i1iiIIiiI111 , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  i1I1Iiii = name
  if Oo0OOOO0oOoo0 :
   if not os . path . exists ( ii11iIi1I ) : os . makedirs ( ii11iIi1I )
   if not OOooo0O0o0 ( url ) == True : O0OIIII1i ( i1iiIIiiI111 , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( i1iiIIiiI111 , 'Downloading %s' % i1I1Iiii , '' , 'Please Wait' )
   ooI1111i = os . path . join ( ii11iIi1I , "%s.apk" % name )
   try : os . remove ( ooI1111i )
   except : pass
   downloader . download ( url , ooI1111i , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   iIii1 . ok ( i1iiIIiiI111 , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ooI1111i + '")' )
  else : O0OIIII1i ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : O0OIIII1i ( i1iiIIiiI111 , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 29 - 29: i1iIi * III1iiIii
 if 75 - 75: o0o00Oo0O
def oOoO ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 5 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'INFO' )
 if 59 - 59: oooOo0oo0oo + oOo0O0Ooo / IIiIiII11i / OOooOOo
 if 80 - 80: OOooOOo + iI11I1II1I1I . III1iiIii
def oOoO00o ( url ) :
 iiI111I1iIiI = OooOoooOo ( oO0000OOo00 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 30015 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 76 - 76: oOo0O0Ooo * oooOo0oo0oo
def ii111 ( url , iconimage , fanart ) :
 iiI111I1iIiI = OooOoooOo ( url )
 i1i1I1 = url
 iIiIi11 = iconimage
 fanart = fanart
 IIi = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for i1oO , OOoO in IIi :
  if '.mp4' in OOoO :
   iI1Ii1iI11iiI ( 'Watch VIDEO' , url + '/' + i1oO , 222 , iIiIi11 , fanart , '' )
  if 'description' in OOoO :
   iI1Ii1iI11iiI ( 'Read Description' , url + '/' + i1oO , 30017 , iIiIi11 , fanart , '' )
  if 'images' in OOoO :
   Iii1I1I11iiI1 ( 'View Images' , url + '/' + i1oO , 30018 , iIiIi11 , fanart , '' )
  if 'url' in OOoO :
   iI1Ii1iI11iiI ( 'Install Build On Android' , url + '/' + i1oO , 30016 , iIiIi11 , fanart , '' )
  if 'url' in OOoO :
   iI1Ii1iI11iiI ( 'Install Build On Pc' , url + '/' + i1oO , 30019 , iIiIi11 , fanart , '' )
 oOI1Ii1I1 ( 'movies' , 'INFO' )
 if 49 - 49: oO0o + IIiIiII11i / III1iiIii - o0o00Oo0O % o0ii1I
def iII1i1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  IIIii ( url )
  if 63 - 63: oOo0O0Ooo - Ii - IiI1i11I % Iii . o0ii1I * Ii1I
def OooO0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'url="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for url in IIi :
  Oo00o ( url )
  if 3 - 3: I1ii11iIi11i . ii + ooOoO0O00 / ooOoO0O00 % iI11I1II1I1I / o0ii1I
def oooo00Oo0O ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( 'desc="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for o00oIiii1Ii in IIi :
  oooO ( 'Description:' , o00oIiii1Ii )
  if 16 - 16: ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
def Iii1II1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( url )
 url = url
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiI111I1iIiI )
 for i1oO , OOoO in IIi :
  if 'png' in OOoO :
   iI1Ii1iI11iiI ( 'image' , '' , '' , url + '/' + i1oO , url + '/' + i1oO , '' )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 54 - 54: OOooOOo . I1ii11iIi11i
def Ii1 ( name , url , description ) :
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
 if 40 - 40: Ii1I + i1i1I1IIii1II
 if 34 - 34: o0o00Oo0O * III1iiIii / ooOoO0O00 + i1i1I1IIii1II . OOooOOo
def Oo00o ( url ) :
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
 Oooo ( )
 if 73 - 73: o0ii1I / oOo0O0Ooo / ii + oOo0O0Ooo
def IIIii ( url ) :
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
 Oooo ( )
 if 57 - 57: oooOo0oo0oo . o0ii1I % I11i
def I1I11 ( name , url , description ) :
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
 Oooo ( )
 if 9 - 9: oooOo0oo0oo
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
  I1iII = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  IiII111i1i11 . write ( I1iII . rstrip ( '\r\n' ) + '\n' )
def Oooo ( ) :
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
  if 18 - 18: Iii + I1ii11iIi11i - oO0o / i1IiiiI1iI / oooOo0oo0oo
  if 53 - 53: oooOo0oo0oo + I11i . i1i1I1IIii1II / Iii
  if 52 - 52: i1IiiiI1iI + i1IiiiI1iI
def iIII1IiI ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OO0ii1 , III11iIIi , iIIi in os . walk ( url ) :
  for file in iIIi :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    IiIi1II111I = open ( ( os . path . join ( OO0ii1 , file ) ) ) . read ( )
    iIiiIiIIiI = IiIi1II111I . replace ( oOo0oooo00o , 'special://home/' )
    IiII111i1i11 = open ( ( os . path . join ( OO0ii1 , file ) ) , mode = 'w' )
    IiII111i1i11 . write ( str ( iIiiIiIIiI ) )
    IiII111i1i11 . close ( )
 Oooo ( )
 if 93 - 93: III1iiIii % Ii1I
def III1I ( ) :
 iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , iiIi1IIiIi + 'RadioNomy.png' )
 iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , iiIi1IIiIi + 'RadioNomy.png' )
 iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ) , '' , 70006 , iiIi1IIiIi + 'RadioNomy.png' )
 if 31 - 31: IIiIiII11i + oooOo0oo0oo - ii . Iii
def i1I ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def oOo000Oo00o ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
def o0ooOOoOoOO ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in i1Iii1i1I :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']Filter - ' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , iiIi1IIiIi + 'RadioNomy.png' )
 for url , iIiIi11 , OOoO in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , iIiIi11 )
def iII11 ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( I11iiii )
 for url in IIi :
  OooO0OO ( url )
def O00OO00OOOoO ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1
 IiI11Ii1iI = 'https://www.radionomy.com/en/search/index?query=' + ( iii1 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = OooOoooOo ( IiI11Ii1iI )
 IIi = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']Stream - ' + OOoO + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + O0O00Oo , 70005 , iIiIi11 )
  if 53 - 53: oOo0O0Ooo
  if 10 - 10: i1IiiiI1iI / Ii - IIiIiII11i
def O0o0o ( ) :
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( OOoO , 'http://www.listenlive.eu/' + O0O00Oo , 10111113 , iiIi1IIiIi + 'radio.png' )
def Iii1I11 ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url in IIi :
  iiIi1IIiI ( OOoO , url , 222 , iiIi1IIiIi + 'radio.png' )
  if 48 - 48: oooOo0oo0oo
def I1111III111ii ( ) :
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIi = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.toonjet.com/' + O0O00Oo , 8051 , iiIi1IIiIi + 'classictoons.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oO0oOooO ( url ) :
 I11iiii = o0O0Oo00 ( url )
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
   iIiiiii1i ( ( iIiIi11 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , iiIi1IIiIi + 'vod.png' )
 for url in i1Iii1i1I :
  iIiiiii1i ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , iiIi1IIiIi + 'Next.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo00o00O0 ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( I11iiii )
 for url in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , iiIi1IIiIi + 'classictoons.png' )
  if 52 - 52: IiI1i11I + o0o00Oo0O % I11i % o0o00Oo0O % IIiIiII11i + ii
  if 51 - 51: IiI1i11I % Ii
def OO00 ( ) :
 O0oo00oOOO0o ( 'Audio Books' , '' , 30011 , iiIi1IIiIi + 'AudioBooks.png' , iiIi1IIiIi + 'AudioBooks.png' , '' )
 O0oo00oOOO0o ( 'Kids Audio Books' , '' , 30006 , iiIi1IIiIi + 'KidsAudioBooks.png' , iiIi1IIiIi + 'KidsAudioBooks.png' , '' )
 if 28 - 28: Ii1I + Ii1I % OOooOOo
def iiI111iIi1 ( ) :
 O0oo00oOOO0o ( 'All' , '' , 30001 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 O0oo00oOOO0o ( 'Popular' , '' , 30012 , iiIi1IIiIi + 'POPULARv.png' , iiIi1IIiIi + 'POPULARv.png' , '' )
 O0oo00oOOO0o ( 'Search' , '' , 30013 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'Search.png' , '' )
 if 25 - 25: i1IiiiI1iI - o0ii1I / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
def Ii1i ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OOoO , O0O00Oo , IIII1i in IIi :
  if 'Parent' in OOoO :
   pass
  elif '2' in IIII1i :
   O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 84 - 84: ooOoO0O00 - oOo0O0Ooo % IiI1i11I
def oO00o0oOoo ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OOoO , O0O00Oo , IIII1i in IIi :
  if iii1 in OOoO . lower ( ) :
   if '1' in IIII1i :
    O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '2' in IIII1i :
    O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   elif '3' in IIII1i :
    O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 66 - 66: Ii1I . I1ii11iIi11i
    if 38 - 38: Iii . III1iiIii - oO0o . oOo0O0Ooo
def ooOoo0OOOO0o ( ) :
 II11iIiIIIiI = OooOoooOo ( OOOO + 'books' + oOoOooOo0o0 )
 IIi = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( II11iIiIIIiI )
 for OOoO , O0O00Oo , IIII1i in IIi :
  if '1' in IIII1i :
   O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 3010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '2' in IIII1i :
   O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '3' in IIII1i :
   O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , O0O00Oo , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 38 - 38: oOo0O0Ooo % III1iiIii * o0ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: o0ii1I + oO0o * I11i . i1IiiiI1iI
def Oo00oo00o00Oo ( url ) :
 i1oO = url
 II11iIiIIIiI = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , OOoO in i1Iii1i1I :
  if 'mp3' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1oO + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'wma' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1oO + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i1oO + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif '/' in OOoO :
   O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1oO + url , 30009 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 1 - 1: III1iiIii
   if 31 - 31: ooOoO0O00
   if 21 - 21: ooOoO0O00
def OOOO00 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1oO = url
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
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1oO + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1oO + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i1oO + url , 30010 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 92 - 92: Iii % o0o00Oo0O % o0ii1I . o0ii1I . III1iiIii
   if 82 - 82: I1ii11iIi11i + OOooOOo . Ii1I % i1i1I1IIii1II / o0ii1I
def iI11IiiiIII ( ) :
 O0oo00oOOO0o ( 'A-Z' , '' , 30007 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 O0oo00oOOO0o ( 'All' , '' , 30003 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 O0oo00oOOO0o ( 'Search' , '' , 30014 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
 if 43 - 43: IiI1i11I + Ii
def o00ii11iiIIII ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 in IIi :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + O0O00Oo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in iIiIi11 :
   pass
  else :
   O0oo00oOOO0o ( iIiIi11 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( O0O00Oo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + iIiIi11 + '.gif' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 96 - 96: oOo0O0Ooo % i1i1I1IIii1II / i1i1I1IIii1II
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: OOooOOo + I11i + I1ii11iIi11i
 if 79 - 79: I1ii11iIi11i - ii % i1IiiiI1iI + ii - Iii % OOooOOo
def iII ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  if '</a>' in OOoO :
   pass
  elif '(' in OOoO :
   O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 89 - 89: oOo0O0Ooo / IiI1i11I / ii - Ii + oOo0O0Ooo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . Iii
def o00o0 ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if iii1 in OOoO . lower ( ) :
   if '</a>' in OOoO :
    pass
   elif '(' in OOoO :
    O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0O00Oo , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   else :
    Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0O00Oo , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
    if 84 - 84: OOooOOo - I1ii11iIi11i . i1iIi . III1iiIii - I1ii11iIi11i
    if 99 - 99: i1IiiiI1iI
def o0I1IiiiiI1i1I ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIi = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if '</a>' in OOoO :
   pass
  elif '(' in OOoO :
   O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0O00Oo , 30005 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + O0O00Oo , 30004 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 48 - 48: Iii + IIiIiII11i % i1i1I1IIii1II % oooOo0oo0oo * IIiIiII11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: oO0o
 if 13 - 13: i1iIi - oOo0O0Ooo
def iii11OO0oO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  i1oO = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( i1oO )
  if 35 - 35: Iii + oooOo0oo0oo / oooOo0oo0oo
def i1IIIi1Iii1i ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  if '<p align' in OOoO :
   pass
  elif '&nbsp;' in OOoO :
   pass
  else :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , iiIi1IIiIi + 'KodibleAudioBooks.png' , iiIi1IIiIi + 'KodibleAudioBooks.png' , '' )
   if 63 - 63: oO0o + i1iIi
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: OOooOOo - i1IiiiI1iI / i1i1I1IIii1II . o0o00Oo0O * i1iIi / Ii1I
 if 18 - 18: o0ii1I
def oo0oooOo ( ) :
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
def o0OOoO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 iIO0OO0o0O00oO = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( II11iIiIIIiI )
 for url , OOoO , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , iIiIi11 , iIiIi11 , OOoO )
 for url , OOoO in iIO0OO0o0O00oO :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in next :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 21005 , iiIi1IIiIi + 'Next.png' , '' , '' )
def I1iII1II1I1ii ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 ooO0O0o0 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 oo0OO0O = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( II11iIiIIIiI )
 OO0OooOOoO00OO00 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url in oo0OO0O :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , 'http:' + url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 for url , OOoO in ooO0O0o0 :
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
 else :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
def ii11ii1iIiI1 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'watchcartoons.png' , '' , '' )
  if 80 - 80: iI11I1II1I1I - oOo0O0Ooo - ii * i1iIi + Ii . oooOo0oo0oo
def OOOOO ( ) :
 II11iIiIIIiI = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIi = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if '9cart' in O0O00Oo :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 20001 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 87 - 87: o0o00Oo0O * IIiIiII11i + iI11I1II1I1I % i1i1I1IIii1II % Ii - OOooOOo
def o00O0Oooo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiIi1I1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if '9cart' in url :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']ALL[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url in i1Iii1i1I :
  if '9cart' in url :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']123[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
 for url , OOoO in IiIi1I1 :
  if '9cart' in url :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 83 - 83: ii . oOo0O0Ooo + o0ii1I * o0o00Oo0O / i1i1I1IIii1II
def IiiiI11 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 20003 , iIiIi11 )
 for url , OOoO in i1Iii1i1I :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 57 - 57: iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
def oOOo00ooO ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'Watch' in url :
   iIiiiii1i ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
   if 64 - 64: ooOoO0O00
def I111I ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 20005 , iiIi1IIiIi + 'ORIGINCARTOON.png' )
  if 62 - 62: ii + III1iiIii
def iIiIi1i1Iiii ( url ) :
 url = cloudflare . source ( url )
 ii1O0ooooo000 ( url )
 if 78 - 78: I1ii11iIi11i - i1IiiiI1iI + IiI1i11I * o0ii1I * I11i
def iIiiiII11 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . recompile ( 'src="([^"]*)"' )
 for url in IIi :
  ii1O0ooooo000 ( url )
  if 98 - 98: Ii1I
  if 25 - 25: oooOo0oo0oo % oooOo0oo0oo
def o0OO0O0Oo ( ) :
 if 25 - 25: Ii + Ii1I - ii . o0o00Oo0O % i1IiiiI1iI
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search Cartoons[/COLOR]' , '' , 10005 , iiIi1IIiIi + 'ORIGINCARTOON.png' , Oo00OOOOO , '' )
 if 53 - 53: ooOoO0O00
def I11iIiI1 ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( II11iIiIIIiI )
 if 9 - 9: ooOoO0O00 - OOooOOo
 for O0O00Oo , OOoO in IIi :
  if iii1 in OOoO . lower ( ) :
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
    if 57 - 57: iI11I1II1I1I * o0ii1I * IiI1i11I / i1i1I1IIii1II
    if 46 - 46: o0ii1I
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 61 - 61: I11i / i1iIi - IIiIiII11i
def OOoOOo0O00O ( url ) :
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
 if 87 - 87: Ii1I / oOo0O0Ooo
def IIi1IiiIi1III ( url ) :
 I11iiii = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I11iiii )
 for iIiIi11 in i1Iii1i1I :
  IiIiIiiIIii = iIiIi11
 IiIi1I1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I11iiii )
 for url in IiIi1I1 :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , url , 10006 , iiIi1IIiIi + 'Next.png' , Oo00OOOOO , '' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 10007 , IiIiIiiIIii )
  if 77 - 77: i1i1I1IIii1II * i1iIi . oooOo0oo0oo * o0ii1I % IIiIiII11i
  if 94 - 94: oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: I1ii11iIi11i + o0ii1I + oO0o
def o00o0o0oOo0 ( url , IMAGE ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  print OOoO + '     ' + url
  if 'easy' in url :
   IiI1iI1I1 ( url )
   if 5 - 5: i1IiiiI1iI % IIiIiII11i + I1ii11iIi11i - iI11I1II1I1I
   if 64 - 64: i1IiiiI1iI + iI11I1II1I1I
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 14 - 14: o0ii1I / ii + IIiIiII11i . o0o00Oo0O / ooOoO0O00
def IiI1iI1I1 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I11iiii )
 for url in IIi :
  OooO0OO ( url )
  if 58 - 58: I11i / Ii / o0o00Oo0O % Iii % oOo0O0Ooo
  if 86 - 86: III1iiIii + OOooOOo / oOo0O0Ooo + Iii % Iii / Ii
  if 12 - 12: OOooOOo + I11i . i1IiiiI1iI
def ooO00OO ( ) :
 if 64 - 64: i1iIi - I11i % IiI1i11I % i1IiiiI1iI . i1i1I1IIii1II
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Stand Up[/COLOR]' , '' , 10014 , iiIi1IIiIi + 'StandUp.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search Comedian[/COLOR]' , '' , 10015 , iiIi1IIiIi + 'SearchComedian.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Others[/COLOR]' , '' , 10017 , iiIi1IIiIi + 'Others.png' , Oo00OOOOO , '' )
 if 100 - 100: oO0o % OOooOOo / Iii * o0o00Oo0O - i1i1I1IIii1II
def I1IiIi1iiI ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  if 'elete' in OOoO :
   pass
  else :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 222 , iIiIi11 )
   if 26 - 26: oOo0O0Ooo % OOooOOo
def OO00o0oo ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 I1I1iiiiiIi1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , i1Io00OOOo , i1iII1IiiIiI1 in I1I1iiiiiIi1 :
  for iii1 in i1Io00OOOo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   Ii1ooOO0oo00Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for O0O00Oo , OOoO in Ii1ooOO0oo00Oo :
    if 'tube' in O0O00Oo :
     pass
    elif 'stage' in O0O00Oo :
     iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + i1Io00OOOo + '   -   ' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iIiIi11 , )
    elif 'vee' in O0O00Oo :
     pass
     if 12 - 12: IiI1i11I . III1iiIii + I1ii11iIi11i
def O0o0oOO ( ) :
 II11iIiIIIiI = OooOoooOo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 I1I1iiiiiIi1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , i1Io00OOOo , i1iII1IiiIiI1 in I1I1iiiiiIi1 :
  Ii1ooOO0oo00Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for O0O00Oo , OOoO in Ii1ooOO0oo00Oo :
   if 'tube' in O0O00Oo :
    pass
   elif 'stage' in O0O00Oo :
    iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + i1Io00OOOo + '   -   ' + OOoO + '[/COLOR]' , ( O0O00Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iIiIi11 )
   elif 'vee' in O0O00Oo :
    pass
    if 48 - 48: i1i1I1IIii1II / iI11I1II1I1I / Ii1I / ii . o0ii1I % o0o00Oo0O
    if 81 - 81: I1ii11iIi11i - ii + i1IiiiI1iI / Iii * ii % III1iiIii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 11 - 11: OOooOOo
def O00oOo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1111I1II11 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( II11iIiIIIiI )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( I1111I1II11 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in I1111I1II11 :
  ooO00O00oOO ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 31 - 31: IIiIiII11i * o0ii1I / III1iiIii / Ii
  if 88 - 88: I1ii11iIi11i . I11i - Ii . o0o00Oo0O * iI11I1II1I1I * OOooOOo
  if 99 - 99: iI11I1II1I1I - i1i1I1IIii1II - OOooOOo / iI11I1II1I1I * I1ii11iIi11i - i1i1I1IIii1II
  if 72 - 72: III1iiIii % ooOoO0O00 / iI11I1II1I1I
  if 95 - 95: o0o00Oo0O . oO0o
  if 89 - 89: ooOoO0O00
  if 19 - 19: i1iIi / I11i % III1iiIii - o0ii1I
def O000OOO0OOo ( ) :
 if 14 - 14: Ii1I - Ii * i1IiiiI1iI
 iiii ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , Oo00OOOOO , '' )
 iiii ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 80 - 80: oOo0O0Ooo
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 58 - 58: i1i1I1IIii1II + Ii1I % OOooOOo
def Iii11I1i ( ) :
 iiii ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 iiii ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , Oo00OOOOO , '' )
 if 81 - 81: oooOo0oo0oo - oOo0O0Ooo % I11i
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
def i1iiIiIi1 ( ) :
 if 31 - 31: o0o00Oo0O * I11i * I1ii11iIi11i
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 IIii1 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 95 - 95: IiI1i11I / Ii / I1ii11iIi11i % ii - I11i * IiI1i11I
 for II1iIi1IiIii in IIii1 :
  I111I11I111 = oO0 + II1iIi1IiIii + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( I111I11I111 )
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , oooOo0OOOoo0 , OOoO in IIi :
   if iii1 in OOoO . lower ( ) :
    iIIiiII11i1I1 ( OOoO , O0O00Oo , 222 , oo00O00oO000o , oooOo0OOOoo0 , OOOiiiiI )
    if 28 - 28: IIiIiII11i * i1iIi * OOooOOo * i1IiiiI1iI . IIiIiII11i . Ii1I
    oOI1Ii1I1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 32 - 32: i1iIi - oO0o . IiI1i11I . IiI1i11I % ooOoO0O00 * o0ii1I
    if 65 - 65: IiI1i11I / i1iIi . IIiIiII11i
def o0oO00oooo ( ) :
 if 63 - 63: IIiIiII11i - Iii . OOooOOo
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 IIii1 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 8 - 8: oOo0O0Ooo * i1iIi / III1iiIii + OOooOOo . III1iiIii - oooOo0oo0oo
 for II1iIi1IiIii in IIii1 :
  Oo0O = oO0 + II1iIi1IiIii + oOoOooOo0o0
  II11iIiIIIiI = O00O0oOO00O00 ( Oo0O )
  IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OOoO , OOOiiiiI , O0O00Oo , iIiIi11 , oooOo0OOOoo0 , oO0oOOoo00000 in IIi :
   if iii1 in OOoO . lower ( ) :
    iiii ( OOoO , O0O00Oo , oO0oOOoo00000 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
    if 60 - 60: oooOo0oo0oo * i1iIi * oO0o
    oOI1Ii1I1 ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 64 - 64: Iii / IIiIiII11i / oO0o - i1iIi * iI11I1II1I1I . IiI1i11I
    if 25 - 25: oooOo0oo0oo - o0ii1I . Iii
def OO0OOO ( ) :
 if 80 - 80: iI11I1II1I1I - I1ii11iIi11i % i1IiiiI1iI % I1ii11iIi11i + oOo0O0Ooo % o0ii1I
 I11iiii = OooOoooOo ( oO0 + 'spongemain.php' )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , OOOiiiiI , O0O00Oo , iIiIi11 , oooOo0OOOoo0 , oO0oOOoo00000 in IIi :
  iiii ( OOoO , O0O00Oo , oO0oOOoo00000 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
def O00O00oO ( url ) :
 if 3 - 3: i1IiiiI1iI . Iii % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * oO0o
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ii1i1IiII111I = ( '%s%s' % ( Oo0o0OoOoOo0 , url ) )
 iiI111I1iIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in IIi :
  iiiiI11ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
  for iII1i11 in iiiiI11ii :
   if iII1i11 == url :
    OOoO = ( '[COLORred]Watched - [/COLOR]' + OOoO ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  iIIiiII11i1I1 ( OOoO , url , 222 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
  if 36 - 36: o0ii1I * oOo0O0Ooo * Ii1I . Iii * Ii1I
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
  if 76 - 76: oooOo0oo0oo + o0o00Oo0O / III1iiIii - oO0o
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 27 - 27: I1ii11iIi11i - iI11I1II1I1I * IiI1i11I * IIiIiII11i * Ii1I
  if 9 - 9: Ii + oooOo0oo0oo - OOooOOo / i1iIi % ooOoO0O00 / i1i1I1IIii1II
def iiI1II1II111 ( url ) :
 if 71 - 71: IIiIiII11i % i1IiiiI1iI + oOo0O0Ooo * i1iIi + III1iiIii . i1iIi
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , OOOiiiiI , url , iIiIi11 , oooOo0OOOoo0 , oO0oOOoo00000 in IIi :
  iiii ( OOoO , url , oO0oOOoo00000 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
  if 25 - 25: i1iIi . I11i % oOo0O0Ooo + IiI1i11I
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
  if 61 - 61: i1i1I1IIii1II % i1iIi - Ii1I + i1i1I1IIii1II . OOooOOo
  if 44 - 44: Ii1I / o0o00Oo0O - III1iiIii + oooOo0oo0oo . Iii . Ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: OOooOOo % i1IiiiI1iI % ooOoO0O00 * I11i + oooOo0oo0oo
def iIIiiII11i1I1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 34 - 34: i1IiiiI1iI * I11i . oOo0O0Ooo % Ii
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oooooOo0 = [ ]
  oooooOo0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oooooOo0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oooooOo0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1iiii . addContextMenuItems ( oooooOo0 )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = False )
 return ii1II
 if 61 - 61: iI11I1II1I1I + i1i1I1IIii1II * Iii - ooOoO0O00 % i1i1I1IIii1II
def iiii ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 76 - 76: i1i1I1IIii1II / OOooOOo
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oooooOo0 = [ ]
  oooooOo0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oooooOo0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oooooOo0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1iiii . addContextMenuItems ( oooooOo0 )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = True )
 return ii1II
if 12 - 12: i1IiiiI1iI
if 58 - 58: oO0o + iI11I1II1I1I % o0o00Oo0O + Iii + OOooOOo * ii
if 41 - 41: i1i1I1IIii1II * oOo0O0Ooo
if 76 - 76: i1i1I1IIii1II . o0o00Oo0O * ii + i1iIi
if 53 - 53: I1ii11iIi11i
if 3 - 3: III1iiIii - ii * ii - oOo0O0Ooo / i1IiiiI1iI * Ii1I
if 58 - 58: III1iiIii % iI11I1II1I1I / Ii % I11i . i1IiiiI1iI * IiI1i11I
if 32 - 32: ii + I11i
if 91 - 91: i1iIi - i1IiiiI1iI * i1IiiiI1iI
if 55 - 55: iI11I1II1I1I + oOo0O0Ooo - I1ii11iIi11i
if 24 - 24: oO0o / i1IiiiI1iI + IiI1i11I * Iii * IiI1i11I
if 10 - 10: oOo0O0Ooo - Ii1I - I1ii11iIi11i - I11i
if 21 - 21: ii + i1IiiiI1iI
if 43 - 43: Ii . Ii1I . i1i1I1IIii1II
if 31 - 31: o0ii1I % I11i % i1IiiiI1iI . Ii1I / I11i * i1i1I1IIii1II
def OoI1 ( string ) :
 if O0o0O00Oo0o0 == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 88 - 88: ii - oooOo0oo0oo + o0o00Oo0O * III1iiIii * Iii
def iIi1 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 Iii11111I1iii = [ ]
 try :
  if 67 - 67: Ii1I + i1i1I1IIii1II * III1iiIii / IIiIiII11i % oO0o % oO0o
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( i1I1iI ) == False :
  OoI1 ( 'Making Favorites File' )
  Iii11111I1iii . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  IiIi1II111I = open ( i1I1iI , "w" )
  IiIi1II111I . write ( json . dumps ( Iii11111I1iii ) )
  IiIi1II111I . close ( )
 else :
  OoI1 ( 'Appending Favorites' )
  IiIi1II111I = open ( i1I1iI ) . read ( )
  IIIII1IIiIi = json . loads ( IiIi1II111I )
  IIIII1IIiIi . append ( ( name , url , iconimage , fanart , mode ) )
  iIiiIiIIiI = open ( i1I1iI , "w" )
  iIiiIiIIiI . write ( json . dumps ( IIIII1IIiIi ) )
  iIiiIiIIiI . close ( )
  if 91 - 91: oOo0O0Ooo / IIiIiII11i * oooOo0oo0oo
  if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
def OOOo0Ooo0o00o ( ) :
 if os . path . exists ( i1I1iI ) == False :
  Iii11111I1iii = [ ]
  OoI1 ( 'Making Favorites File' )
  Iii11111I1iii . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  IiIi1II111I = open ( i1I1iI , "w" )
  IiIi1II111I . write ( json . dumps ( Iii11111I1iii ) )
  IiIi1II111I . close ( )
 else :
  oOoOooO = json . loads ( open ( i1I1iI ) . read ( ) )
  I1iiI1iiI1i1 = len ( oOoOooO )
  for o0OoOOoooooOO in oOoOooO :
   OOoO = o0OoOOoooooOO [ 0 ]
   O0O00Oo = o0OoOOoooooOO [ 1 ]
   oo00O00oO000o = o0OoOOoooooOO [ 2 ]
   try :
    oOOo = o0OoOOoooooOO [ 3 ]
    if oOOo == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     oOOo = oo00O00oO000o
    else :
     oOOo = oooOo0OOOoo0
   try : oOOOo0Oooo = o0OoOOoooooOO [ 5 ]
   except : oOOOo0Oooo = None
   try : I1iiIIiI11I = o0OoOOoooooOO [ 6 ]
   except : I1iiIIiI11I = None
   if 29 - 29: Iii + i1i1I1IIii1II % i1iIi + OOooOOo
   if o0OoOOoooooOO [ 4 ] == 0 :
    Iii1I1I11iiI1 ( OOoO , O0O00Oo , '' , oo00O00oO000o , oooOo0OOOoo0 , '' , 'fav' )
   else :
    Iii1I1I11iiI1 ( OOoO , O0O00Oo , o0OoOOoooooOO [ 4 ] , oo00O00oO000o , oooOo0OOOoo0 , '' , 'fav' )
    if 92 - 92: I11i
def ii111Ii1i ( name ) :
 IIIII1IIiIi = json . loads ( open ( i1I1iI ) . read ( ) )
 for IiI1I1II in range ( len ( IIIII1IIiIi ) ) :
  if IIIII1IIiIi [ IiI1I1II ] [ 0 ] == name :
   del IIIII1IIiIi [ IiI1I1II ]
   iIiiIiIIiI = open ( i1I1iI , "w" )
   iIiiIiIIiI . write ( json . dumps ( IIIII1IIiIi ) )
   iIiiIiIIiI . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 74 - 74: I1ii11iIi11i + I1ii11iIi11i / Iii
 if 21 - 21: ii / III1iiIii
def o0OIi ( ) :
 OO0OOoooOo00 = os . path . join ( iIi1ii1I1 , 'addons.ini' )
 oOoOo0O0o0O = open ( OO0OOoooOo00 , "w+" )
 II11iIiIIIiI = OooOoooOo ( 'http://piesustv.net:8000/get.php?username=' + OO0o + '&password=' + Ooo + '&type=m3u_plus&output=mpegts' )
 IIi = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( II11iIiIIIiI )
 oOoOo0O0o0O . write ( r'[' + IiII + ']' + '\n' )
 for OOoO , iIiIi11 , iiII1i1i1I1 , O0O00Oo in IIi :
  O0O00Oo = ( O0O00Oo + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  Ooo0o0o0ooo = ( OOoO + '=plugin://' + IiII + '/?url=' + O0O00Oo + '&mode=10012&name=' + ( OOoO ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( iIiIi11 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( iIiIi11 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  oOoOo0O0o0O . write ( Ooo0o0o0ooo + '\n' )
  if 85 - 85: Ii1I * OOooOOo % Iii
  if 29 - 29: Ii1I
def oOOoOO ( ) :
 I11iiii = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIi = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo in IIi :
  iIiiiii1i ( '24/7' , O0O00Oo , 90021 , iiIi1IIiIi + '247Streams.png' )
  if 99 - 99: i1iIi * iI11I1II1I1I - o0ii1I + I1ii11iIi11i . I1ii11iIi11i
def i11Ii111I1 ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iI1Ii1iI11iiI ( OOoO , ( O0O00Oo ) . strip ( ) , 222 , iiIi1IIiIi + '247Streams.png' , iiIi1IIiIi + '247Streams.png' , '' )
def OOOii ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iI1Ii1iI11iiI ( OOoO , ( O0O00Oo ) . strip ( ) , 222 , iiIi1IIiIi + 'musicch.png' , iiIi1IIiIi + 'musicch.png' , '' )
def I1i11111i1i11 ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iI1Ii1iI11iiI ( OOoO , ( O0O00Oo ) . strip ( ) , 222 , iiIi1IIiIi + 'NEWS.png' , iiIi1IIiIi + 'NEWS.png' , '' )
def Ooi11 ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iI1Ii1iI11iiI ( OOoO , ( O0O00Oo ) . strip ( ) , 222 , iiIi1IIiIi + 'adult.png' , iiIi1IIiIi + 'adult.png' , '' )
def O00oOoOo0ooO0O0oo ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIi = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iI1Ii1iI11iiI ( OOoO , O0O00Oo , 1016 , iiIi1IIiIi + 'TUTS.png' , iiIi1IIiIi + 'TUTS.png' , '' )
  if 31 - 31: Ii + o0ii1I % OOooOOo
  if 9 - 9: i1iIi . Iii - I1ii11iIi11i . i1IiiiI1iI
def i1I111II11 ( ) :
 if 56 - 56: i1IiiiI1iI / o0o00Oo0O * oooOo0oo0oo
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Recent Episodes[/COLOR]' , '' , 10019 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '' , 10020 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' , '' , 10021 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
 if 32 - 32: IiI1i11I . iI11I1II1I1I % I1ii11iIi11i . ii
def Ooo00OoO0O00 ( ) :
 if 11 - 11: Iii
 I11iiii = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , iIiIi11 , OOoO , Oo000o in IIi :
  Iii1I1I11iiI1 ( OOoO + '  -  ' + ( Oo000o ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , O0O00Oo , 10023 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 20 - 20: o0o00Oo0O . Ii * ooOoO0O00 % o0o00Oo0O . oOo0O0Ooo
  if 53 - 53: i1iIi / ii - IIiIiII11i
  if 68 - 68: ii . ii . iI11I1II1I1I / i1iIi - Iii % o0o00Oo0O
def iiIIIIiI11II1 ( ) :
 if 26 - 26: o0o00Oo0O . Iii + IiI1i11I - o0ii1I . Iii
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
 if 2 - 2: Ii1I . I1ii11iIi11i * oooOo0oo0oo % IIiIiII11i . IiI1i11I
def II1i1iI ( url ) :
 i1i1I1 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 II11iIiIIIiI = cloudflare . source ( i1i1I1 )
 IIi = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 10022 , iiIi1IIiIi + 'dtv.png' , Oo00OOOOO , '' )
  if 5 - 5: OOooOOo + IiI1i11I * i1iIi
  if 47 - 47: iI11I1II1I1I + oO0o % iI11I1II1I1I . i1iIi / I1ii11iIi11i - Ii
  if 80 - 80: Ii1I / o0o00Oo0O / iI11I1II1I1I + oOo0O0Ooo
  if 3 - 3: i1iIi / ooOoO0O00 - OOooOOo
def oo0o0ooOoo00O ( ) :
 if 2 - 2: i1i1I1IIii1II . oooOo0oo0oo
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 O0O00Oo = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iii1 ) . replace ( ' ' , '+' )
 II11iIiIIIiI = cloudflare . source ( O0O00Oo )
 IIi = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  if iii1 in OOoO . lower ( ) :
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 10022 , iiIi1IIiIi + 'dtv.png' )
   if 43 - 43: iI11I1II1I1I
   if 29 - 29: III1iiIii % i1iIi + oO0o . ooOoO0O00 + oOo0O0Ooo
   if 24 - 24: i1IiiiI1iI / o0ii1I * Ii1I - ii / oOo0O0Ooo . i1i1I1IIii1II
def oo0OOoOo0 ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1oO , iIii , oO00oO0 , OOoO in IIi :
  o0oI1Iii = ( oO00oO0 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  II1I1Ii11 = ( iIii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1I1iiI = 'Season ' + II1I1Ii11 + 'Episode ' + o0oI1Iii + OOoO
  o0oOOO0 ( I1I1iiI , i1oO )
  if 11 - 11: Iii / OOooOOo
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 17 - 17: i1iIi
  if 13 - 13: I1ii11iIi11i - Iii / i1i1I1IIii1II - I1ii11iIi11i - IiI1i11I / Ii
def o0oOOO0 ( name , url ) :
 i1oO = url
 I1i1iiii = name
 o0o = cloudflare . source ( i1oO )
 i1Iii1i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0o )
 for I1111I1II11 , O00O in i1Iii1i1I :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + I1i1iiii + O00O + '[/COLOR]' , I1111I1II11 , 222 , iiIi1IIiIi + 'dtv.png' )
  if 42 - 42: I11i + i1i1I1IIii1II - ii + IiI1i11I % oO0o
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: ooOoO0O00 / Ii1I - IiI1i11I . Ii / ooOoO0O00 / ii
 if 88 - 88: o0ii1I / Ii % OOooOOo % oooOo0oo0oo
def OoOo0oOooOoOO ( ) :
 if 70 - 70: Ii1I . Ii1I / Iii . Ii1I
 if 37 - 37: ooOoO0O00 . i1IiiiI1iI - IIiIiII11i % I11i - ooOoO0O00 . i1i1I1IIii1II
 if 34 - 34: iI11I1II1I1I / IIiIiII11i
 if 3 - 3: I11i - ii + IiI1i11I . Iii
 if 88 - 88: Iii - IiI1i11I
 if 68 - 68: I1ii11iIi11i % i1i1I1IIii1II . III1iiIii - I11i / ooOoO0O00 / ii
 if 34 - 34: Iii % I1ii11iIi11i + o0ii1I
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' , '' , 10091 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 if 93 - 93: o0ii1I - i1IiiiI1iI % o0o00Oo0O
def iiiI ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOOOoOooo = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + iIiIi11 , '' , '' )
 for url in OOOOoOooo :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 15 - 15: i1iIi * iI11I1II1I1I * i1i1I1IIii1II
def O0oo0O00ooOo ( url ) :
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 OOOOoOooo = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  iIiIi11 = 'http://watchepisodes.cc/' + iIiIi11
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 10093 , iIiIi11 , iIiIi11 , '' )
 for url in OOOOoOooo :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 70 - 70: I1ii11iIi11i + Ii
def ii1I ( url , iconimage ) :
 iIiIi11 = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for oO00oO0 , url , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + oO00oO0 + ' - ' + OOoO + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , iIiIi11 , '' , '' )
  if 96 - 96: Iii % IIiIiII11i / i1iIi % oooOo0oo0oo / i1iIi % Ii
def O0000ooO ( url , iconimage ) :
 iIiIi11 = iconimage
 II11iIiIIIiI = cloudflare . source ( url )
 IIi = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  if 'player' in OOoO :
   pass
  elif 'vod' in OOoO :
   Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , iIiIi11 , '' , '' )
   if 83 - 83: i1IiiiI1iI + I11i % i1i1I1IIii1II / oO0o
   if 59 - 59: o0ii1I * oooOo0oo0oo . III1iiIii
   if 68 - 68: o0o00Oo0O * iI11I1II1I1I / i1IiiiI1iI
   if 65 - 65: oooOo0oo0oo - oOo0O0Ooo * i1IiiiI1iI
   if 99 - 99: oOo0O0Ooo
   if 64 - 64: Ii1I * o0ii1I * I1ii11iIi11i % III1iiIii % i1iIi
def oo00ooOoO00 ( ) :
 if 55 - 55: IIiIiII11i - i1IiiiI1iI - oooOo0oo0oo % o0ii1I
 if 49 - 49: I1ii11iIi11i * i1IiiiI1iI
 if 53 - 53: I1ii11iIi11i / o0ii1I + i1i1I1IIii1II . IiI1i11I + III1iiIii
 if 19 - 19: o0ii1I
 if 51 - 51: iI11I1II1I1I
 if 8 - 8: oO0o / I11i % IiI1i11I . Ii . ii . o0ii1I
 if 8 - 8: oO0o * I1ii11iIi11i
 if 41 - 41: I1ii11iIi11i / oO0o / OOooOOo - Ii - OOooOOo
 if 4 - 4: Iii . III1iiIii
 if 39 - 39: oooOo0oo0oo . I1ii11iIi11i - OOooOOo * Ii
 if 4 - 4: OOooOOo * o0o00Oo0O - Iii
 if 72 - 72: Iii + i1iIi / oOo0O0Ooo . III1iiIii % oO0o / Ii
 if 13 - 13: i1IiiiI1iI % I11i + oooOo0oo0oo + i1IiiiI1iI + Ii - Ii1I
 if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , iiIi1IIiIi + 'latest.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , iiIi1IIiIi + 'popular.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , iiIi1IIiIi + 'Genre.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , iiIi1IIiIi + 'series.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Search Program[/COLOR]' , '' , 10043 , iiIi1IIiIi + 'Search.png' , iiIi1IIiIi + 'WatchSeries.png' , '' )
 if 11 - 11: IiI1i11I
 if 20 - 20: o0ii1I . i1IiiiI1iI % o0ii1I
def i11iI1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IIi = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I1iiiiI1iI ) )
 for url , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 92 - 92: iI11I1II1I1I
def OOO0oO0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
  if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
def o000oo ( url ) :
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
  if 58 - 58: i1iIi + IIiIiII11i + o0ii1I . ii
  if 42 - 42: iI11I1II1I1I / Iii . o0o00Oo0O . o0ii1I
def Ii1i111iI ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iII1iiOO = 'http://www.watchseriesgo.to/search/' + iii1 . replace ( ' ' , '%20' )
 II11iIiIIIiI = OooOoooOo ( iII1iiOO )
 IIi = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , O0O00Oo , OOoO in IIi :
  if 'watch online' in OOoO :
   pass
  else :
   print O0O00Oo
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.watchseriesgo.to' + O0O00Oo , 10044 , iIiIi11 , '' , '' )
   if 99 - 99: o0ii1I / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
   xbmcplugin . setContent ( OOOOi11i1 , 'movies' )
   if 44 - 44: Ii % i1IiiiI1iI % i1i1I1IIii1II + Iii * i1i1I1IIii1II . o0ii1I
def OoOo0Oooo0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO , oO00oO0 , OOOiiiiI in IIi :
  O0oII11I = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oO00oO0 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + O0oII11I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iIiIi11 , '' , OOOiiiiI )
  if 65 - 65: OOooOOo + i1IiiiI1iI % oOo0O0Ooo
def o0OO0OOOOOoOOOOooo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  O0oII11I = ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + O0oII11I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 29 - 29: i1IiiiI1iI / Ii1I * oOo0O0Ooo + IiI1i11I
def oOO00I1IIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO , iIiIi11 in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iIiIi11 , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 80 - 80: Iii / i1i1I1IIii1II * o0ii1I / IiI1i11I
def IiIiIIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 I1iiiiI1iI = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIii , I1I1iiiiiIi1 in I1iiiiI1iI :
  IIi = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( I1I1iiiiiIi1 ) )
  for url , OOoO in IIi :
   O0oII11I = ( iIii ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + O0oII11I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 i1Iii1i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , iiIi1IIiIi + 'WATCHSERIES.png' , '' , '' )
 for url in i1Iii1i1I :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iiIi1IIiIi + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 61 - 61: IiI1i11I * i1iIi
class i1I1IiIiiI1II ( ) :
 if 39 - 39: ii
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 37 - 37: IiI1i11I . I11i / o0ii1I / oooOo0oo0oo * ooOoO0O00
  O0oII11I = name
  self . Get_Sources ( O0O00Oo , O0oII11I )
  if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + i1i1I1IIii1II
  if 58 - 58: IiI1i11I - ii
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  II11iIiIIIiI = OooOoooOo ( URL )
  IIi = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for O0O00Oo , OOoO in IIi :
   URL = 'http://www.watchseriesgo.to/link/' + O0O00Oo
   self . Get_site_link ( URL , season_name )
   if 56 - 56: IiI1i11I / IiI1i11I
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
   if 21 - 21: o0o00Oo0O * i1iIi % OOooOOo / o0o00Oo0O
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   ooooooo = 'DACLIPS'
   if ooooooo in i1I1IiIiiI1II . source_list :
    pass
   else :
    self . daclips ( url , season_name , ooooooo )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    ooooooo = 'THEVIDEO'
    if ooooooo in i1I1IiIiiI1II . source_list :
     pass
    else :
     self . thevideo ( url , season_name , ooooooo )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     ooooooo = 'ALLMYVIDEOS'
     if ooooooo in i1I1IiIiiI1II . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , ooooooo )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      ooooooo = 'VIDSPOT'
      if ooooooo in i1I1IiIiiI1II . source_list :
       pass
      else :
       self . vidspot ( url , season_name , ooooooo )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       ooooooo = 'VODLOCKER'
       if ooooooo in i1I1IiIiiI1II . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , ooooooo )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        ooooooo = 'VIDTO'
        if ooooooo in i1I1IiIiiI1II . source_list :
         pass
        else :
         self . vidto ( url , season_name , ooooooo )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 58 - 58: ooOoO0O00 + o0o00Oo0O . oO0o % Iii
       else :
        if 'youwatch' in url :
         ooooooo = 'YouWatch'
         if ooooooo in i1I1IiIiiI1II . source_list :
          pass
         else :
          self . youwatch ( url , season_name , ooooooo )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 39 - 39: I11i + III1iiIii / o0ii1I + I11i
          if 33 - 33: IiI1i11I - I1ii11iIi11i - Iii
 def allmyvid ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for IiIi1II11i , OOoO in IIi :
   self . Printer ( IiIi1II11i , season_name , source_name )
   if 61 - 61: o0ii1I + oOo0O0Ooo / ooOoO0O00 + ooOoO0O00 / i1i1I1IIii1II
 def vidspot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIi1II11i , OOoO in IIi :
   self . Printer ( IiIi1II11i , season_name , source_name )
   if 47 - 47: i1IiiiI1iI
 def thevideo ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{"file":"([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIi1II11i in IIi :
   self . Printer ( IiIi1II11i , season_name , source_name )
   if 25 - 25: IiI1i11I + oOo0O0Ooo + OOooOOo + i1IiiiI1iI % o0o00Oo0O
 def vodlocker ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIi1II11i in IIi :
   self . Printer ( IiIi1II11i , season_name , source_name )
   if 26 - 26: i1iIi + OOooOOo
 def daclips ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( II11iIiIIIiI )
  for IiIi1II11i in IIi :
   self . Printer ( IiIi1II11i , season_name , source_name )
   if 17 - 17: Ii1I - IiI1i11I % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * oooOo0oo0oo
 def filehoot ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIi1II11i in IIi :
   self . Printer ( IiIi1II11i , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIi1II11i in IIi :
   self . Printer ( IiIi1II11i , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIi1II11i in IIi :
   self . youplay ( IiIi1II11i , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  II11iIiIIIiI = OooOoooOo ( url )
  IIi = re . compile ( 'file: "([^"]*)"' ) . findall ( II11iIiIIIiI )
  for IiIi1II11i in IIi :
   self . Printer ( IiIi1II11i , season_name , source_name )
   if 6 - 6: i1IiiiI1iI
 def Printer ( self , Link , season_name , source_name ) :
  if 46 - 46: IIiIiII11i * i1IiiiI1iI
  if Link in i1I1IiIiiI1II . List :
   pass
  elif source_name in i1I1IiIiiI1II . source_list :
   pass
  else :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + source_name + '[/COLOR]' , Link , 222 , iiIi1IIiIi + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   i1I1IiIiiI1II . List . append ( Link )
   i1I1IiIiiI1II . source_list . append ( source_name )
   if 23 - 23: ooOoO0O00 - o0o00Oo0O
   xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 6 - 6: i1iIi % ii * i1IiiiI1iI - III1iiIii
   if 24 - 24: Iii / iI11I1II1I1I . ii % OOooOOo . o0ii1I
   if 73 - 73: i1IiiiI1iI
   if 25 - 25: III1iiIii
   if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
def O0Oooo ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Highlights[/COLOR]' , '' , 10008 , iiIi1IIiIi + 'Highlights.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Fixtures[/COLOR]' , '' , 10009 , iiIi1IIiIi + 'Fixtures.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'Sport.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , iiIi1IIiIi + 'PremiereLeague.png' , Oo00OOOOO , '' )
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . o0ii1I - I1ii11iIi11i . Ii
def IIIII11II1 ( url ) :
 OOOO0oOO = '20'
 IIIiii = [ ]
 I11OoooO = '                                                    '
 i1IIi11 = '        '
 Iii1I1I11iiI1 ( I11OoooO + 'pl' + i1IIi11 + 'w' + i1IIi11 + 'd' + i1IIi11 + 'l' + i1IIi11 + 'f' + i1IIi11 + 'a' + i1IIi11 + 'pts' , '' , '' , '' , '' , '' )
 I11iiii = O0i11i1iiI1i ( url )
 IIi = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( I11iiii )
 for oOIIIII11 , i1i1 , IiiIiIIiiIiI , o0Oo , I1O0 , IiII111i1i11 , IiIi1II111I , oO0oo0oOO , iiII1iIi1ii1i in IIi :
  i11IiI1 = O0oO00oOO00O ( i1i1 )
  Oo0Oo0o00oO = O0oO00oOO00O ( IiiIiIIiiIiI )
  oO0o0OooOO0 = O0oO00oOO00O ( o0Oo )
  iiIi = O0oO00oOO00O ( I1O0 )
  ooOo0oo0O0O = O0oO00oOO00O ( IiII111i1i11 )
  IIiii = O0oO00oOO00O ( IiIi1II111I )
  IIIiii . append ( oOIIIII11 [ 0 ] )
  i1Ii11I1i = len ( IIIiii )
  iI11IIi1iiI1I = int ( len ( I11OoooO ) - len ( oOIIIII11 ) - 2 )
  if len ( IIIiii ) >= 10 :
   iI11IIi1iiI1I = iI11IIi1iiI1I - 1
  if len ( IIIiii ) <= int ( OOOO0oOO ) :
   iI1Ii1iI11iiI ( str ( i1Ii11I1i ) + ' ' + oOIIIII11 + I11OoooO [ 0 : iI11IIi1iiI1I ] + i1i1 + i11IiI1 + IiiIiIIiiIiI + Oo0Oo0o00oO + o0Oo + oO0o0OooOO0 + I1O0 + iiIi + IiII111i1i11 + ooOo0oo0O0O + IiIi1II111I + IIiii + ' ' + iiII1iIi1ii1i , '' , '' , '' , '' , '' )
   if 83 - 83: I1ii11iIi11i / i1iIi
   if 11 - 11: I11i - IIiIiII11i % i1i1I1IIii1II . IIiIiII11i
def O0oO00oOO00O ( space ) :
 if len ( space ) > 1 :
  Ii1I1I111iI = len ( '        ' ) - len ( space ) + 1
  space = int ( Ii1I1I111iI ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 65 - 65: i1i1I1IIii1II . Ii % oooOo0oo0oo * IiI1i11I % I1ii11iIi11i
def oO0o0ooooo ( ) :
 if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + o0ii1I . oooOo0oo0oo
 if 58 - 58: iI11I1II1I1I + i1IiiiI1iI - Ii1I - ooOoO0O00 * OOooOOo
 if 4 - 4: ii
 if 7 - 7: III1iiIii
 if 26 - 26: oooOo0oo0oo + I1ii11iIi11i
 if 71 - 71: oOo0O0Ooo . i1iIi
 if 43 - 43: Ii1I * oooOo0oo0oo
 if 1 - 1: oO0o * i1iIi + III1iiIii . i1i1I1IIii1II / i1iIi
 if 91 - 91: o0ii1I + Iii - I1ii11iIi11i % OOooOOo . IiI1i11I
 if 51 - 51: oooOo0oo0oo / Iii
 if 51 - 51: i1iIi * i1i1I1IIii1II - i1IiiiI1iI + IiI1i11I
 if 46 - 46: I11i - Ii % oO0o / o0ii1I - OOooOOo
 if 88 - 88: i1i1I1IIii1II * oOo0O0Ooo / oO0o - oooOo0oo0oo / ooOoO0O00 . i1IiiiI1iI
 if 26 - 26: Ii - i1iIi
 if 45 - 45: i1iIi + IIiIiII11i % IiI1i11I
 if 55 - 55: i1iIi - i1i1I1IIii1II % oOo0O0Ooo
 if 61 - 61: i1iIi
 if 22 - 22: iI11I1II1I1I / i1iIi / oOo0O0Ooo - I11i
 if 21 - 21: i1i1I1IIii1II . Ii * Iii . oooOo0oo0oo / oooOo0oo0oo
 if 42 - 42: ii / i1IiiiI1iI . I11i / o0o00Oo0O - III1iiIii * III1iiIii
 if 1 - 1: o0ii1I % i1IiiiI1iI
 if 97 - 97: OOooOOo
 if 13 - 13: OOooOOo % oooOo0oo0oo . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
 if 19 - 19: i1IiiiI1iI % i1iIi - i1iIi % oOo0O0Ooo . oooOo0oo0oo - ii
 if 100 - 100: oOo0O0Ooo + o0ii1I + I11i . ooOoO0O00 % ii
 if 64 - 64: o0o00Oo0O % ooOoO0O00 * i1IiiiI1iI - o0ii1I + I1ii11iIi11i
 if 65 - 65: OOooOOo . Ii
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
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIi = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + O0O00Oo , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iIiIi11 , Oo00OOOOO , '' )
  if 73 - 73: o0ii1I % oO0o * oooOo0oo0oo
def oooo0O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I1iiiiI1iI in I1iiiiI1iI :
  iII1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( I1iiiiI1iI ) )
  for iII11OO0OoO0OOoOo in iII1 :
   iII11OO0OoO0OOoOo = iII11OO0OoO0OOoOo
  oO000 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I1iiiiI1iI ) )
  for iIiI1ii1I1I , iIiIi11 , time , II1i11I1 in oO000 :
   O00OOoOOOO00O = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( II1i11I1 )
   Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + iII11OO0OoO0OOoOo + ' - ' + iIiI1ii1I1I + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iIiIi11 , Oo00OOOOO , ( str ( O00OOoOOOO00O ) ) )
   if 40 - 40: IiI1i11I % ii . o0ii1I * ooOoO0O00
 oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if 6 - 6: o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - I11i / Ii % OOooOOo
def o0ooOOOo0O0 ( ) :
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
 if 100 - 100: Ii . oooOo0oo0oo . Ii
def o00Oo ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  I1III11i11Iii = OOoO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OOoO :
   pass
  else :
   I1III11i11Iii = OOoO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + I1III11i11Iii + '[/COLOR]' , url , 10013 , iIiIi11 )
 for url , iIiIi11 , OOoO in i1Iii1i1I :
  I1III11i11Iii = OOoO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OOoO :
   pass
  else :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + I1III11i11Iii + '[/COLOR]' , url , 10013 , iIiIi11 )
def I1IIi1iIiIiIiI ( url ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , iiIi1IIiIi + 'TodaysMacthes.png' , Oo00OOOOO , '' )
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 i1Iii1i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 if 1 - 1: oOo0O0Ooo / oOo0O0Ooo
 if 37 - 37: oO0o - ooOoO0O00 - IIiIiII11i . ooOoO0O00
 if 33 - 33: IiI1i11I + I1ii11iIi11i % Iii . i1i1I1IIii1II
 if 6 - 6: III1iiIii + Ii1I
 if 62 - 62: i1i1I1IIii1II . i1IiiiI1iI - ii * IIiIiII11i . Ii
 if 13 - 13: iI11I1II1I1I * I11i - Ii
 if 63 - 63: ii * i1IiiiI1iI
 for url , iIiIi11 , OOoO in i1Iii1i1I :
  I1III11i11Iii = OOoO . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in OOoO :
   pass
  else :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + I1III11i11Iii + '[/COLOR]' , url , 10013 , iIiIi11 )
   if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . i1i1I1IIii1II % IIiIiII11i
def I1IiiI1I1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( II11iIiIIIiI )
 for I1111I1II11 in IIi :
  ii11i1II111 = ( I1111I1II11 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  ooO00O00oOO ( 'http:' + ii11i1II111 )
  if 5 - 5: oooOo0oo0oo / oooOo0oo0oo + IIiIiII11i
  if 96 - 96: o0o00Oo0O . oO0o + IIiIiII11i / IiI1i11I - i1IiiiI1iI - o0ii1I
  if 74 - 74: I11i - i1iIi / oOo0O0Ooo
  if 98 - 98: o0o00Oo0O % Ii % oooOo0oo0oo
def I1i1 ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO , iIiIi11 in IIi :
  iiIi1IIiI ( OOoO , url , 8046 , iIiIi11 )
 for url in i1Iii1i1I :
  iIiiiii1i ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , iiIi1IIiIi + 'Next.png' )
def Ii1IiiII ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  ooO00O00oOO ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 73 - 73: i1i1I1IIii1II - Ii1I / ii - oO0o / oOo0O0Ooo
def I111II1iIIII ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( I11iiii )
 for url in IIi :
  yt . PlayVideo ( url )
  if 56 - 56: Ii * IiI1i11I / Ii * o0ii1I . iI11I1II1I1I . Ii1I
def I1I1i ( ) :
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , iiIi1IIiIi + 'documentary.png' )
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , iiIi1IIiIi + 'documentary.png' )
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']Search Docs[/COLOR]' , '' , 80012 , iiIi1IIiIi + 'Search.png' )
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( OOoO , O0O00Oo , 8041 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0oo0 ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( I11iiii )
 for iIiIi11 , url , OOoO in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + iIiIi11 )
 for url in next :
  iIiiiii1i ( 'NEXT PAGE' , url , 8041 , iiIi1IIiIi + 'Next.png' )
  if 12 - 12: Ii + ooOoO0O00 - o0ii1I + o0o00Oo0O . oOo0O0Ooo
  if 8 - 8: I11i
def ooOO0O0O ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I11iiii )
 for url in IIi :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
  else :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def IIIiIIIi111iI ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url in IIi :
  url = ( url ) . replace ( '\/' , '/' )
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , '' )
  if 41 - 41: i1i1I1IIii1II % oOo0O0Ooo % I1ii11iIi11i + o0ii1I + Ii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0oiIiI1i1iiIi1i ( name , url ) :
 iI1IiII1II1I = 0
 name = name
 url = url
 IiI1i = [ '144' , '240' , '380' , '480' , '720' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Resolution[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  OooO0OO ( url )
  if 99 - 99: i1iIi / oOo0O0Ooo . o0ii1I - o0ii1I * oOo0O0Ooo
  if 24 - 24: Iii * oO0o - i1i1I1IIii1II / iI11I1II1I1I - I1ii11iIi11i . oooOo0oo0oo
  if 2 - 2: i1iIi - o0o00Oo0O - Ii1I / Iii * OOooOOo
  if 26 - 26: Ii1I + i1IiiiI1iI - i1i1I1IIii1II + III1iiIii % oooOo0oo0oo
  if 84 - 84: Iii % o0ii1I % o0o00Oo0O * I11i
  if 15 - 15: i1i1I1IIii1II - iI11I1II1I1I - IIiIiII11i - III1iiIii % Ii1I
  if 80 - 80: III1iiIii * IiI1i11I . ooOoO0O00 % o0ii1I % Ii1I + i1iIi
  if 6 - 6: Ii1I . i1i1I1IIii1II . oO0o + III1iiIii
def oO0oo0O0OOOo0 ( ) :
 I11iiii = o0O0Oo00 ( 'http://documentarylovers.com/' )
 IIi = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  if 'genre' in O0O00Oo :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , O0O00Oo , 80010 , iiIi1IIiIi + 'documentary.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iII11I ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( I11iiii )
 for url , OOoO , iIiIi11 in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , iIiIi11 )
 for url in next :
  iIiiiii1i ( 'NEXT PAGE' , url , 80010 , iiIi1IIiIi + 'Next.png' )
  if 44 - 44: IiI1i11I
def oOoOoOOOO0o ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( I11iiii )
 for url in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']YouTube[/COLOR]' , url , 8043 , iiIi1IIiIi + 'documentary.png' )
 for url in i1Iii1i1I :
  IIIiIIIi111iI ( url )
  if 57 - 57: IiI1i11I . o0ii1I * oOo0O0Ooo % i1IiiiI1iI + iI11I1II1I1I
def OoO00o ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIi1IiII = 'http://documentarylovers.com/?s=' + ( iii1 ) . replace ( ' ' , '+' )
 oOO0oo = IIi1IiII . lower ( )
 iII11I ( oOO0oo )
 if 90 - 90: ii % Ii % I11i % i1IiiiI1iI - i1iIi + iI11I1II1I1I
def oooOO0 ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if 'films' in url :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , iiIi1IIiIi + 'documentary.png' )
def iiIi1iIiI ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( I11iiii )
 for iIiIi11 , url , OOoO in IIi :
  if 'films' in url :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + iIiIi11 )
 for url in i1Iii1i1I :
  iIiiiii1i ( 'NEXT' , url , 8049 , iiIi1IIiIi + 'Next.png' )
def IIi1iii ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I11iiii )
 for url in IIi :
  if 'rtd' in url :
   ii1Ii ( url )
   if 41 - 41: Ii1I % Ii1I + III1iiIii . IiI1i11I % i1IiiiI1iI * i1iIi
def ii1Ii ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( I11iiii )
 for iiI111I1iIiI , file in IIi :
  url = ( 'https://rtd.rt.com' + iiI111I1iIiI + file )
  OooO0OO ( url )
  if 57 - 57: o0ii1I . i1IiiiI1iI . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
  if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
def o000iiI11i ( ) :
 II11iIiIIIiI = o0O0Oo00 ( 'http://www.stream2watch.co/live-tv' )
 IIi = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for O0O00Oo , iIiIi11 , OOoO , IIiIIiI in IIi :
  iIiiiii1i ( ( OOoO + '[COLOR' + ooOoOoo0O + ']' + IIiIIiI + '[/COLOR]' ) , O0O00Oo , 8086 , iIiIi11 )
  if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
def OOo0iIiiI11II11 ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , iIiIi11 , OOoO in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 8087 , iIiIi11 )
  if 75 - 75: i1IiiiI1iI - IiI1i11I . i1i1I1IIii1II
def O0ooO0oO0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  IiI11I11i ( url , OOoO )
  if 69 - 69: ooOoO0O00 . o0ii1I
def IiI11I11i ( url , name ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  print url
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 96 - 96: o0ii1I
def O00O0O0 ( ) :
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + O0O00Oo , 3002 , 'http://www.solie.org/alibrary/' + iIiIi11 )
def ii1IiIi1iIi ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iIiIi11 )
def IIiI111Iii ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 OOiIiI1iI = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( I11iiii )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , iiIi1IIiIi + 'classicmovies.png' )
 for url , OOoO in OOiIiI1iI :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']Season- ' + OOoO + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'classicmovies.png' )
 for url in next :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , iiIi1IIiIi + 'Next.png' )
 for url , iIiIi11 , OOoO in i1Iii1i1I :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iIiIi11 )
def ooo0oooO ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( I11iiii )
 for url in IIi :
  O0O0Ooo0 ( url )
def O0O0Ooo0 ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( I11iiii )
 for url in IIi :
  OooO0OO ( url )
  if 34 - 34: i1i1I1IIii1II - IIiIiII11i - I11i + IiI1i11I + i1IiiiI1iI
def oOO ( ) :
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , O0O00Oo , 8065 , iiIi1IIiIi + 'classicmovies.png' )
def oo0OOo ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( "v.src = '([^']*)';" ) . findall ( I11iiii )
 for url in IIi :
  ii1O0ooooo000 ( url )
  if 77 - 77: i1i1I1IIii1II . o0ii1I / o0o00Oo0O * i1i1I1IIii1II
def oo000ii ( ) :
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIi = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , O0O00Oo , 8065 , iiIi1IIiIi + 'classictv.png' )
def oOoO0O0o ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  if 'mp4' in url :
   OooO0OO ( url )
 for url in i1Iii1i1I :
  yt . PlayVideo ( url )
  if 84 - 84: OOooOOo - Iii
def OoO00O00O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIi = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + O0O00Oo , 8071 , iiIi1IIiIi + 'streams.png' )
def ooOo0o0o00 ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for OOoO , url in IIi :
  if '(Free Access)' in OOoO :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , iiIi1IIiIi + 'streams.png' )
def iIIi1Iii ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , url in IIi :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + OO0o + '/' + Ooo + url ) . strip ( )
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iIiIi11 , oooOo0OOOoo0 , '' )
  if 96 - 96: IiI1i11I % IiI1i11I % i1IiiiI1iI / i1IiiiI1iI - Ii1I
def i11i1 ( ) :
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']XXX Vids[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Perfect Girls[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Best Videos[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Genres[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Recently Uploaded[/COLOR]' , '[COLOR' + ooOoOoo0O + ']100% Verified[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Tags[/COLOR]' , '[COLOR' + ooOoOoo0O + ']In Your Language[/COLOR]' , '[COLOR' + ooOoOoo0O + ']Search[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  O0O0 ( 'http://watchxxxfree.com/categories' )
 if o0Oo00 == 1 :
  I1IIo0o0OoOO00Oo ( 'http://www.perfectgirls.net' )
 if o0Oo00 == 2 :
  i1iiIi1II1 ( 'http://www.xvideos.com/best' )
 if o0Oo00 == 3 :
  iiI1Iii ( 'http://www.xvideos.com/best' )
 if o0Oo00 == 4 :
  i1iiIi1II1 ( 'http://www.xvideos.com/best' )
 if o0Oo00 == 5 :
  i1iiIi1II1 ( 'http://www.xvideos.com/verified/videos' )
 if o0Oo00 == 6 :
  ooOoo ( 'http://www.xvideos.com/tags' )
 if o0Oo00 == 7 :
  I11I1I ( 'http://www.xvideos.com/porn' )
 if o0Oo00 == 8 :
  ii1i11Ii11iI ( )
  if 46 - 46: iI11I1II1I1I * OOooOOo - Iii . iI11I1II1I1I
  if 48 - 48: IiI1i11I . I11i
  if 86 - 86: iI11I1II1I1I . IiI1i11I / IiI1i11I
  if 43 - 43: oOo0O0Ooo
  if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
  if 34 - 34: I11i % Ii1I + o0ii1I * Iii / i1i1I1IIii1II
  if 18 - 18: i1iIi
  if 92 - 92: oO0o % iI11I1II1I1I / III1iiIii * IiI1i11I . ooOoO0O00 + i1i1I1IIii1II
  if 24 - 24: III1iiIii . IiI1i11I * III1iiIii % Ii . Ii + ooOoO0O00
def Ooo0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  if 'ch' in url :
   O0oo00oOOO0o ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Jizbox.png' , iiIi1IIiIi + 'Jizbox.png' , '' )
def o0OO00oOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiiII1iIi = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( II11iIiIIIiI )
 for url , OOoO in IIi :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 for OOoO , url in IiiII1iIi :
  Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OoO00oooo0o ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   iiiiii ( url )
def ooII1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def O0O0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO , Ii1I1I111iI in IIi :
  if 'category' in url :
   O0oo00oOOO0o ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORorange]   ' + Ii1I1I111iI + '[/COLOR]' , url , 90006 , iIiIi11 , iiIi1IIiIi + 'Jizbox.png' , '' )
def o0OOOIiII11I1I1IIi ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiiII1iIi = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO in IIi :
  iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , iIiIi11 , '' , '' )
 for url in IiiII1iIi :
  Iii1I1I11iiI1 ( '[COLORred]NEXT[/COLOR]' , url , 90006 , iiIi1IIiIi + 'Next.png' , '' , '' )
def ii1i111 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'jetload' in url :
   iiiiii ( url )
def iiiiii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OooO0OO ( url )
def I1IIo0o0OoOO00Oo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO , Ii1I1I111iI in IIi :
  if 'category' in url :
   O0oo00oOOO0o ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORorange]' + Ii1I1I111iI + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def O0ooOOO00000O ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 i1oO = url
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiiII1iIi = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , iIiIi11 in IIi :
  iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , iIiIi11 , '' , '' )
 for url in IiiII1iIi :
  Iii1I1I11iiI1 ( '[COLORred]NEXT[/COLOR]' , i1oO + '/' + url , 90003 , iiIi1IIiIi + 'Next.png' , '' , '' )
def OOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'get\("(.*)", function' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  OO0ooOO00o0 ( 'http://www.perfectgirls.net' + url )
def OO0ooOO00o0 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( 'http://(.+?)\n' ) . findall ( II11iIiIIIiI )
 for url in IIi :
  ooO00O00oOO ( 'http://' + url )
def I11I1I ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , Ii1I1I111iI in IIi :
  O0oo00oOOO0o ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgreen] - No of Videos : [COLORorange]' + Ii1I1I111iI + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
def ooOoo ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IiiII1iIi = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in IiiII1iIi :
  O0oo00oOOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( II11iIiIIIiI )
 for url , OOoO , Ii1I1I111iI in IIi :
  O0oo00oOOO0o ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgreen] - No of Videos : [COLORorange]' + ( Ii1I1I111iI + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
  if 29 - 29: IIiIiII11i - IiI1i11I / i1i1I1IIii1II % ii % IiI1i11I + III1iiIii
def iiiioOoO0oOO ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IiiII1iIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in IiiII1iIi :
  O0oo00oOOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO , OOOo0o0Oooo0o0oO0 in IIi :
  O0oo00oOOO0o ( OOoO + '--' + ( OOOo0o0Oooo0o0oO0 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iIiIi11 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 92 - 92: IiI1i11I . o0ii1I
  if 10 - 10: o0ii1I + I11i * III1iiIii / Ii1I / i1i1I1IIii1II
def i1iiIi1II1 ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , url , OOoO , i1I1IiI1ii , OOOOo00O in IIi :
  O0oo00oOOO0o ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgreen] - Porn Quality : [COLORorange]' + OOOOo00O + ' - [COLORred]' + i1I1IiI1ii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , iIiIi11 , iIiIi11 , OOOOo00O + ' - ' + i1I1IiI1ii )
 oOo0000oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for url in oOo0000oo :
  O0oo00oOOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
  if 31 - 31: IiI1i11I - Ii1I * o0o00Oo0O . ii * Iii / III1iiIii
def iiI1Iii ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 I1iiiiI1iI = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 IiiII1iIi = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( II11iIiIIIiI )
 for url in IiiII1iIi :
  O0oo00oOOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , iiIi1IIiIi + 'Next.png' , '' , '' )
 IIi = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I1iiiiI1iI ) )
 for url , OOoO in IIi :
  if '/c/' in url :
   O0oo00oOOO0o ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , iiIi1IIiIi + 'Jizbox.png' , '' , '' )
   if 87 - 87: iI11I1II1I1I
   if 58 - 58: Ii1I % Ii + OOooOOo / Iii - ii
def ii1i11Ii11iI ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOii1iiiiii = ( iii1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 oOO0oo = oOii1iiiiii . lower ( )
 IiI11Ii1iI = 'http://www.xvideos.com/?k=' + oOO0oo
 print IiI11Ii1iI + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 II11iIiIIIiI = OooOoooOo ( IiI11Ii1iI )
 IIi = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , O0O00Oo , OOoO , i1I1IiI1ii , OOOOo00O in IIi :
  O0oo00oOOO0o ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgreen] - Porn Quality : [COLORorange]' + OOOOo00O + ' - [COLORred]' + i1I1IiI1ii + '[/COLOR]' , 'http://www.xvideos.com' + O0O00Oo , 10108 , iIiIi11 , iIiIi11 , OOOOo00O + ' - ' + i1I1IiI1ii )
 oOo0000oo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo in oOo0000oo :
  O0oo00oOOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + O0O00Oo , 10105 , iiIi1IIiIi + 'Next.png' , '' , '' )
if 69 - 69: OOooOOo + o0o00Oo0O - Iii - iI11I1II1I1I . oO0o
if 13 - 13: Iii . oO0o
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
 IiIi1I1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( II11iIiIIIiI )
 for url in IIi :
  if 'http' in url :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in i1Iii1i1I :
  if 'http' in url :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
 for url in IiIi1I1 :
  if 'http' in url :
   iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , iiIi1IIiIi + 'Jizbox.png' )
   if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . oooOo0oo0oo
def Ii1111i11 ( url ) :
 ooO0O0o0 = xbmc . Player ( OO0OOooOO0 ( ) )
 import urlresolver
 try : ooO0O0o0 . play ( url )
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
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 8091 , iiIi1IIiIi + 'gofish.png' )
def O0ooO00OO ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOoO , iIiIi11 in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 8092 , iIiIi11 )
 for url in next :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 8093 , iiIi1IIiIi + 'Next.png' )
def IiI11I1I111 ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( II11iIiIIIiI )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( II11iIiIIIiI )
 o00OoOoo0 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 in o00OoOoo0 :
  iIiIi11 = iIiIi11
 for url , OOoO in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 8092 , iIiIi11 )
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
o0oOo = '{PQ},' ; II1 = '{SC},' ; oOO0O0Ooo0 = '{XG},' ; I11iiI1i = '{JP},' ; ooOoOO = '{HW},' ; iIiiII11 = '{RT},'
def I1IiiI1ii1i ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iii11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 O0O00Oo = 'http://onlinemovies.tube/?s=' + ( iii1 ) . replace ( ' ' , '+' )
 i1oO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 iIIi1IIi = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i111i11I1ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OOooooo0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oOOII1i11i1iIi11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oo0O0oO0O0O = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + iii1
 oOo0O = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 I11iIiii1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 75 - 75: OOooOOo + o0ii1I . Ii / o0ii1I
 IiiiI1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 OOOo0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 32 - 32: o0ii1I + III1iiIii + Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 II11iIiIIIiI = O00O0oOO00O00 ( O0O00Oo )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 o0o = O00O0oOO00O00 ( i1oO )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iIIi1IIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OOoOoo = O00O0oOO00O00 ( i111i11I1ii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 IiI1 = O00O0oOO00O00 ( OOooooo0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IIiiiiIiIIii = O00O0oOO00O00 ( oo0O0oO0O0O )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O0OO = O00O0oOO00O00 ( oOo0O )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 IIIiIiI = O00O0oOO00O00 ( I11iIiii1 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 79 - 79: ooOoO0O00 / o0ii1I
 if 81 - 81: iI11I1II1I1I
 III11iiii11i1 = O00O0oOO00O00 ( IiiiI1 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 ooOo0OoO = O00O0oOO00O00 ( OOOo0 )
 if 86 - 86: III1iiIii % III1iiIii % ii
 if IIIiIiI != 'Failed' :
  iI1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( IIIiIiI )
  for O0O00Oo , OOoO in iI1 :
   iIIiI1ii = O00O0oOO00O00 ( O0O00Oo )
   oo0OOoOoo0O0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIIiI1ii )
   for iiI11ii1111 , IIiIIiI in oo0OOoOoo0O0O :
    IIiIIiI = ( IIiIIiI . replace ( '.' , ' ' ) )
    if oOO0oo in IIiIIiI . lower ( ) :
     if '.mkv' in iiI11ii1111 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + iiI11ii1111 , 222 , '' , '' , '' )
     elif '.mp4' in iiI11ii1111 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + iiI11ii1111 , 222 , '' , '' , '' )
     elif '.avi' in iiI11ii1111 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + iiI11ii1111 , 222 , '' , '' , '' )
     elif '.wav' in iiI11ii1111 :
      iI1Ii1iI11iiI ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + iiI11ii1111 , 222 , '' , '' , '' )
     else :
      Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + iiI11ii1111 , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 42 - 42: I1ii11iIi11i . i1i1I1IIii1II + o0o00Oo0O / oooOo0oo0oo % ii
      oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in i1Iii1i1I :
   if iii1 in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] source Technica[/COLOR]' ) , O0O00Oo , 222 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 19 - 19: i1iIi / o0ii1I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 43 - 43: OOooOOo % o0ii1I + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o00OooOO000 )
  for I1i1IiI1i , OOoO in IiIi1I1 :
   if iii1 in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIIi1IIi + I1i1IiI1i ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOoOoo )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in I1i11 :
   if iii1 in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORred] source RaizTv[/COLOR]' ) , O0O00Oo , 222 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 98 - 98: I11i * I1ii11iIi11i - o0ii1I . i1iIi
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if IiI1 != 'Failed' :
  ii1I1I111 = [ ]
  oOOo00O0OOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiI1 )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in oOOo00O0OOOo :
   if iii1 in OOoO . lower ( ) :
    if OOoO in ii1I1I111 :
     pass
    else :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , O0O00Oo , 1016 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
     ii1I1I111 . append ( OOoO )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if IIiiiiIiIIii != 'Failed' :
  Ii1Ii = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIiiiiIiIIii )
  for O0O00Oo , iIiIi11 , OOoO in Ii1Ii :
   if iii1 in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + O0O00Oo , 7067 , iIiIi11 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 2 - 2: I1ii11iIi11i - i1iIi % iI11I1II1I1I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if III11iiii11i1 != 'Failed' :
  oOo0OOoooO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( III11iiii11i1 )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in oOo0OOoooO :
   if iii1 in OOoO . lower ( ) :
    iI1Ii1iI11iiI ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source APPRENTICE[/COLOR]' ) , O0O00Oo , 222 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 88 - 88: i1IiiiI1iI - oO0o
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 79 - 79: IiI1i11I
    if 45 - 45: IIiIiII11i + IiI1i11I . Iii . o0o00Oo0O * ooOoO0O00 - o0ii1I
    if 48 - 48: Ii1I + I1ii11iIi11i
    if 76 - 76: Ii1I
    if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . o0ii1I
    if 51 - 51: o0ii1I + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
    if 20 - 20: i1IiiiI1iI . Iii . o0ii1I + Iii - oooOo0oo0oo * i1i1I1IIii1II
    if 82 - 82: oO0o
    if 78 - 78: IIiIiII11i / Iii - Ii + Ii1I * I1ii11iIi11i
    if 17 - 17: OOooOOo
 IIii1 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 72 - 72: IiI1i11I . I1ii11iIi11i - Ii / oOo0O0Ooo
 for II1iIi1IiIii in IIii1 :
  I111I11I111 = oO0 + II1iIi1IiIii + oOoOooOo0o0
  IIIiIiI = O00O0oOO00O00 ( I111I11I111 )
  if IIIiIiI != 'Failed' :
   iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IIIiIiI )
   for O0O00Oo , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in iI1 :
    if iii1 in OOoO . lower ( ) :
     iI1Ii1iI11iiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - Source Pandoras[/COLOR]' , O0O00Oo , 222 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 64 - 64: i1i1I1IIii1II
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
     if 80 - 80: I11i % iI11I1II1I1I
 IIii1 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 63 - 63: III1iiIii * Ii
 if 86 - 86: Iii % Iii - OOooOOo + i1IiiiI1iI / oOo0O0Ooo * ii
 for II1iIi1IiIii in IIii1 :
  I111I11I111 = iii11 + II1iIi1IiIii
  i11IiIIi11I = O00O0oOO00O00 ( I111I11I111 )
  if i11IiIIi11I != 'Failed' :
   o000o0O0Oo00 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( i11IiIIi11I )
   for I1i1IiI1i , OOoO in o000o0O0Oo00 :
    if iii1 in OOoO . lower ( ) :
     iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iii11 + II1iIi1IiIii + I1i1IiI1i ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 26 - 26: IIiIiII11i * IiI1i11I + I11i / o0o00Oo0O + ooOoO0O00 - Iii
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 56 - 56: oooOo0oo0oo
def O0OoO0ooOO0o ( ) :
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + III1iiIii - Iii
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
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 if 93 - 93: OOooOOo % Ii - o0ii1I % oO0o
 if 55 - 55: I11i . Ii1I
 iiI11ii1111 = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( iii1 ) . replace ( ' ' , '+' )
 i1oO = 'http://onlinemovies.tube/?s=' + ( iii1 ) . replace ( ' ' , '+' )
 iIIi1IIi = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i111i11I1ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oOOII1i11i1iIi11 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 63 - 63: i1i1I1IIii1II
 oOo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 I11iIiii1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 79 - 79: Ii1I - i1i1I1IIii1II - I11i . oooOo0oo0oo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 65 - 65: Ii . oO0o % IiI1i11I + III1iiIii - Ii
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 60 - 60: i1IiiiI1iI
 if 14 - 14: I1ii11iIi11i % i1i1I1IIii1II * IiI1i11I - Ii / Ii1I * Ii
 i11II1I11I1 = O00O0oOO00O00 ( iiI11ii1111 )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 o0o = O00O0oOO00O00 ( i1oO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 o00OooOO000 = O00O0oOO00O00 ( iIIi1IIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OOoOoo = O00O0oOO00O00 ( i111i11I1ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 i11IiIIi11I = O00O0oOO00O00 ( oOOII1i11i1iIi11 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * Iii + oooOo0oo0oo
 if 14 - 14: o0ii1I - o0o00Oo0O
 O0OO = O00O0oOO00O00 ( oOo0O )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 IIIiIiI = O00O0oOO00O00 ( I11iIiii1 )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 68 - 68: IIiIiII11i - Ii1I - oO0o * iI11I1II1I1I / oOo0O0Ooo * Ii1I
 if 45 - 45: i1IiiiI1iI * Iii / iI11I1II1I1I / oOo0O0Ooo % IIiIiII11i
 if IIIiIiI != 'Failed' :
  iI1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( IIIiIiI )
  for O0O00Oo , OOoO in iI1 :
   iIIiI1ii = O00O0oOO00O00 ( O0O00Oo )
   oo0OOoOoo0O0O = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIIiI1ii )
   for iiI11ii1111 , IIiIIiI in oo0OOoOoo0O0O :
    if oOO0oo in IIiIIiI . lower ( ) :
     Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']*' + IIiIIiI + '-[COLORgold] source ' + OOoO + '[/COLOR]' ) , O0O00Oo + iiI11ii1111 , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 49 - 49: o0ii1I / IiI1i11I . IiI1i11I . IiI1i11I + Ii % Iii
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if O0OO != 'Failed' :
  IIiIIIIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0OO )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in IIiIIIIiI :
   if oOO0oo in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] source HeroVision[/COLOR]' ) , O0O00Oo , 1016 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 7 - 7: III1iiIii * i1iIi + OOooOOo
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
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
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( o0o )
  III1Ii1i1I1 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( o0o )
  for O0O00Oo , iIiIi11 , OOoO , O0O00OooO in i1Iii1i1I :
   if oOO0oo in OOoO . lower ( ) :
    if 'season' in O0O00OooO :
     iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' - [COLORred]Source - Tv HUB[/COLOR]' , O0O00Oo , 90054 , iIiIi11 , iIiIi11 , '' )
    if 'episodes' in O0O00OooO :
     iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' - [COLORred]Source - Tv HUB[/COLOR]' , O0O00Oo , 90044 , iIiIi11 , iIiIi11 , '' )
  for O0O00Oo in III1Ii1i1I1 :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , O0O00Oo , 90053 , iiIi1IIiIi + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 87 - 87: IIiIiII11i . o0ii1I * oO0o
   oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if i11II1I11I1 != 'Failed' :
  OooO0oOo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( i11II1I11I1 )
  for O0O00Oo , OOoO , iIiIi11 in OooO0oOo :
   if oOO0oo in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + ( OOoO ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , O0O00Oo , 8022 , iIiIi11 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 74 - 74: I11i % OOooOOo . IiI1i11I % i1IiiiI1iI . o0o00Oo0O % IIiIiII11i
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 5 - 5: i1i1I1IIii1II - ii / OOooOOo
    if 30 - 30: Iii % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
    if 55 - 55: oO0o
    if 20 - 20: i1iIi * i1IiiiI1iI * I11i - i1iIi
    if 32 - 32: o0ii1I * i1i1I1IIii1II
    if 85 - 85: Ii . oO0o + oO0o
    if 28 - 28: I1ii11iIi11i
    if 62 - 62: I1ii11iIi11i + ii / IiI1i11I
    if 60 - 60: o0ii1I / OOooOOo . Iii % oooOo0oo0oo
 if o00OooOO000 != 'Failed' :
  IiIi1I1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( o00OooOO000 )
  for OOoO in IiIi1I1 :
   if oOO0oo in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iIIi1IIi + OOoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 61 - 61: o0o00Oo0O . o0ii1I . o0o00Oo0O * Ii * IIiIiII11i / i1IiiiI1iI
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if OOoOoo != 'Failed' :
  I1i11 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OOoOoo )
  for OOoO in I1i11 :
   if oOO0oo in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i111i11I1ii + OOoO ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 69 - 69: Iii
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if i11IiIIi11I != 'Failed' :
  o000o0O0Oo00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i11IiIIi11I )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in o000o0O0Oo00 :
   if oOO0oo in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLORred]*[COLOR' + ooOoOoo0O + ']' + OOoO + '-[COLORgold] Source Scooby[/COLOR]' ) , O0O00Oo , 1016 , oo00O00oO000o , iII11I1Ii1 , OOOiiiiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 17 - 17: Iii
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 38 - 38: i1IiiiI1iI % oooOo0oo0oo
 o0O0oo0o = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for II1iIi1IiIii in o0O0oo0o :
  I111I11I111 = oO0 + II1iIi1IiIii + oOoOooOo0o0
  III11iiii11i1 = O00O0oOO00O00 ( I111I11I111 )
  if III11iiii11i1 != 'Failed' :
   oOo0OOoooO = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( III11iiii11i1 )
   for OOoO , OOOiiiiI , O0O00Oo , iIiIi11 , oooOo0OOOoo0 , oO0oOOoo00000 in oOo0OOoooO :
    if oOO0oo in OOoO . lower ( ) :
     Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - Source Pandoras[/COLOR]' , O0O00Oo , oO0oOOoo00000 , iIiIi11 , oooOo0OOOoo0 , OOOiiiiI )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 9 - 9: o0o00Oo0O . iI11I1II1I1I
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
     if 44 - 44: Ii1I % III1iiIii
     if 6 - 6: oO0o
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoI11I ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0O00Oo = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( iii1 ) . replace ( ' ' , '+' )
 if 69 - 69: i1i1I1IIii1II - Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 II11iIiIIIiI = O00O0oOO00O00 ( O0O00Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 29 - 29: o0ii1I + IiI1i11I % Ii1I + Iii * I1ii11iIi11i - Ii
 if II11iIiIIIiI != 'Failed' :
  i1Iii1i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for O0O00Oo , OOoO in i1Iii1i1I :
   if iii1 in OOoO . lower ( ) :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + O0O00Oo ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 24 - 24: Ii . i1iIi + i1iIi - Ii % oooOo0oo0oo
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
o00OO0 = '{ZH},' ; oO000OO0 = '{IX},' ; ooOOoOoo0OO = '{LM},'
if 65 - 65: i1IiiiI1iI + o0o00Oo0O % I11i
def o0i111I ( url ) :
 o0OooOO0 = cloudflare . source ( url )
 IIi = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( o0OooOO0 )
 for url , iIii , Oo000o , OOoO in IIi :
  iIiiiii1i ( ( iIii ) . replace ( 'Sezon' , ' Season ' ) + ( Oo000o ) . replace ( 'Bölüm' , ' Episode ' ) + OOoO , url , 8063 , '' )
  if 16 - 16: i1i1I1IIii1II / IiI1i11I
  if 8 - 8: IIiIiII11i + III1iiIii
  if 19 - 19: I11i
  if 19 - 19: ii
def O0oooo0O0Oo0O ( url ) :
 o0OooOO0 = cloudflare . source ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0OooOO0 )
 for url , OOoO in IIi :
  iiIi1IIiI ( OOoO , url , 222 , '' )
  if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
  if 93 - 93: i1iIi % i1IiiiI1iI
  if 46 - 46: Ii1I * OOooOOo * III1iiIii * Ii1I . Ii1I
  if 43 - 43: i1iIi . ooOoO0O00
def O0oOOoOOoOo ( ) :
 if 45 - 45: oOo0O0Ooo
 o0OooOO0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIi = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( o0OooOO0 )
 for O0O00Oo , iIiIi11 , OOoO , Oo000o in IIi :
  iIiiiii1i ( OOoO + '  -  ' + ( Oo000o ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , O0O00Oo , 8063 , iIiIi11 )
  if 17 - 17: ii - i1iIi + o0ii1I . ii % I1ii11iIi11i
def O000OO0O ( ) :
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIi = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , OOoO , iIiIi11 in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 8002 , iIiIi11 )
def iiIi11I1 ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( I11iiii )
 for iIiIi11 , time , url , OOoO , iII1ii11III in IIi :
  Iii1I1I11iiI1 ( '%s %s' % ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , time ) , url , 1015 , iIiIi11 , iII1ii11III )
  if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / IiI1i11I
def oO0OO00o ( ) :
 if 97 - 97: o0o00Oo0O . I11i
 iIiiiii1i ( 'Coronation Street' , '' , 8001 , '' )
 iIiiiii1i ( 'Eastenders' , '' , 8002 , '' )
 iIiiiii1i ( 'Emmerdale' , '' , 8003 , '' )
 iIiiiii1i ( 'Hollyoaks' , '' , 8004 , '' )
 iIiiiii1i ( 'Im a Celebrity' , '' , 8005 , '' )
 if 17 - 17: o0o00Oo0O . i1i1I1IIii1II - i1i1I1IIii1II - ooOoO0O00 * oooOo0oo0oo
 if 16 - 16: OOooOOo / IIiIiII11i
 if 22 - 22: Iii
 if 53 - 53: oO0o
def ooooOoooo ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'Holly' in OOoO :
   iIiIi11 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in O0O00Oo :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 94 - 94: iI11I1II1I1I / OOooOOo % iI11I1II1I1I * ooOoO0O00 * Iii
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 5 - 5: o0o00Oo0O . Ii + ii / IiI1i11I % oOo0O0Ooo
def oOO0oOooooO ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'East' in OOoO :
   iIiIi11 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in O0O00Oo :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 42 - 42: Iii % I1ii11iIi11i + III1iiIii - Iii . iI11I1II1I1I - o0ii1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 27 - 27: IiI1i11I % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
def I111I1 ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'Emmer' in OOoO :
   iIiIi11 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in O0O00Oo :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 90 - 90: i1IiiiI1iI % I11i . I1ii11iIi11i
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 37 - 37: o0ii1I / IIiIiII11i
def o00OooO ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'Coro' in OOoO :
   iIiIi11 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in O0O00Oo :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 1 - 1: OOooOOo + ii . III1iiIii . iI11I1II1I1I
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: ooOoO0O00
def iII1ii11I1I ( ) :
 II11iIiIIIiI = OooOoooOo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , OOoO in IIi :
  if 'Celeb' in OOoO :
   iIiIi11 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in O0O00Oo :
    iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , O0O00Oo . replace ( '\\/' , '/' ) , 8006 , iIiIi11 )
   else :
    pass
    if 50 - 50: i1i1I1IIii1II * i1IiiiI1iI % ooOoO0O00 . IiI1i11I / i1i1I1IIii1II . oooOo0oo0oo
def iii111 ( name , url ) :
 ooOooo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if ooOooo :
  Oo00 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  I11iiii = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( I11iiii ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  I11iiii = open_url ( url )
  o0OO00oOO00 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( I11iiii ) [ - 1 ]
  Oo00 = o0OO00oOO00 . replace ( '\\/' , '/' )
 I1iiii = xbmcgui . ListItem ( name , '' , '' )
 I1iiii . setPath ( Oo00 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1iiii )
 if 27 - 27: i1i1I1IIii1II * I1ii11iIi11i * I1ii11iIi11i / III1iiIii + I1ii11iIi11i
 if 94 - 94: i1iIi - ooOoO0O00 . o0o00Oo0O / oOo0O0Ooo
def II111iiI1Ii1 ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIi = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , O0O00Oo , 7071 , iiIi1IIiIi + 'popcorn.png' )
 for O0O00Oo , OOoO in i1Iii1i1I :
  iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , O0O00Oo , 7071 , iiIi1IIiIi + 'popcorn.png' )
  if 58 - 58: ii * ooOoO0O00 * OOooOOo
def o00oO0 ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  if 'Movies' in OOoO :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.snagfilms.com' + ( O0O00Oo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , iiIi1IIiIi + 'popcorn.png' )
def IIIi111iii1iI ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I11iiii )
 IIi = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iIiIi11 )
 for url in i1Iii1i1I :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , iiIi1IIiIi + 'Next.png' )
  if 23 - 23: i1iIi / Ii % oooOo0oo0oo - i1IiiiI1iI . IiI1i11I
  if 92 - 92: iI11I1II1I1I
def oO0OoO00o ( url ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url , iIiIi11 in IIi :
  if '{{' in OOoO :
   pass
  else :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iIiIi11 )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
I1iii1I11i1I1iII = '{UJ},' ; IiI111iIIII = '{WE},' ; ii1Ii11 = '{WP},' ; Oo0OOOooo0ooo = '{PP},'
def Iiii11i11IIi1 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url , iIiIi11 in IIi :
  if '{{' in OOoO :
   pass
  else :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iIiIi11 )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOooOo000O00O ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  OooO ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OooO ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iiIi1IIiIi + 'popcorn.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 78 - 78: ii % i1i1I1IIii1II - Ii
 if 37 - 37: III1iiIii % o0ii1I % ooOoO0O00
 if 23 - 23: i1iIi - o0o00Oo0O + Ii
def oO0ooOoOooO00o00 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '(cooltvseries.com)' in OOoO :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
 for url , OOoO in i1Iii1i1I :
  if '(cooltvseries.com)' in OOoO :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , iiIi1IIiIi + 'CoolSeries.png' )
def o0Ooo00Oo0oo0 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( I11iiii )
 for url in IIi :
  ooO00O00oOO ( ( url ) . replace ( ' ' , '%20' ) )
I11Oo0O00O0O00 = '{XX},' ; II1I1i = '{UD},' ; O00OoOo0OooOo = '{YT},' ; OOooOoOOo0O = '{JS},' ; IIi11ii = '{PF},'
if 57 - 57: oooOo0oo0oo * oO0o + o0o00Oo0O % i1IiiiI1iI - oOo0O0Ooo
def ii1IiiIIiIiii ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIi = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , OOoO , iIiIi11 in IIi :
  iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( O0O00Oo ) ) , 222 , iIiIi11 )
  if 44 - 44: Ii
def IiiiIi1111I ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( I11iiii )
 for iIiIi11 , url , OOoO in IIi :
  if 'youtu' in url :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iIiIi11 )
 for url in next :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NEXT[/COLOR]' , url , 7050 , iiIi1IIiIi + 'Next.png' )
  if 63 - 63: Iii . oOo0O0Ooo . Ii1I * o0ii1I
def IIIIII ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 22 - 22: OOooOOo
def i1iI1i111 ( url ) :
 I11iiii = OooOoooOo
 IIi = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 222 , iIiIi11 )
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
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( I11iiii )
 print 'Len Match: >>>' + str ( len ( IIi ) )
 for OOoO , iIiIi11 , OO0O0oooo0 in IIi :
  ooOoo0OoO0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iIiIi11 ) . replace ( '\\' , '' )
  if OO0O0oooo0 == IiIi11iI1IIi :
   iIiiiii1i ( OOoO , '' , 7022 , ooOoo0OoO0 )
  elif i11iii1II1I1 == True :
   iIiiiii1i ( OOoO , '' , 7022 , ooOoo0OoO0 )
  else : pass
  if 38 - 38: III1iiIii - ooOoO0O00 . Ii
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 28 - 28: i1IiiiI1iI / i1i1I1IIii1II . Ii1I
def oOoo0O00OO ( Search_Name ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I11iiii )
 IIi = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( I11iiii )
 for iIiIi11 , O0O00Oo , i1oO , iIIi1IIi in IIi :
  ooOoo0OoO0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iIiIi11 ) . replace ( '\\' , '' )
  iiIi1IIiI ( Search_Name + ': Link 1' , ( O0O00Oo ) . replace ( '\\' , '' ) , 222 , ooOoo0OoO0 )
  iiIi1IIiI ( Search_Name + ': Link 2' , ( i1oO ) . replace ( '\\' , '' ) , 222 , ooOoo0OoO0 )
  iiIi1IIiI ( Search_Name + ': Link 3' , ( iIIi1IIi ) . replace ( '\\' , '' ) , 222 , ooOoo0OoO0 )
  if 20 - 20: IiI1i11I - Ii1I * IiI1i11I + i1IiiiI1iI
def OOoooiII1 ( ) :
 I11iiii = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iiIi1IIiI ( OOoO , ( O0O00Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , iiIi1IIiIi + 'english.png' )
def ii1i1iIiIIi ( ) :
 I11iiii = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iiIi1IIiI ( OOoO , ( O0O00Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'xxx.png' )
def iI11I11i ( ) :
 I11iiii = OooOoooOo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIi = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( I11iiii )
 for OOoO , O0O00Oo in IIi :
  iiIi1IIiI ( OOoO , ( O0O00Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , iiIi1IIiIi + 'vod(1).png' )
  if 80 - 80: Iii - Ii1I * o0ii1I / ii * o0o00Oo0O % oooOo0oo0oo
def Iiooo000o0OoOo ( url ) :
 url
 iII1i11 = xbmcgui . ListItem ( OOoO , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iII1i11 )
 return
 if 76 - 76: o0ii1I % iI11I1II1I1I / i1i1I1IIii1II * iI11I1II1I1I / iI11I1II1I1I
 if 41 - 41: III1iiIii / ooOoO0O00 / OOooOOo / oooOo0oo0oo . oO0o % OOooOOo
def ooOO0o0ooOo0 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( I11iiii )
 for url , OOOiiiiI , iIiIi11 , OOoO in IIi :
  Iii1I1I11iiI1 ( OOoO , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + iIiIi11 , '' , ( OOOiiiiI ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 for url in i1Iii1i1I :
  iIiiiii1i ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , iiIi1IIiIi + 'Next.png' )
  if 18 - 18: o0ii1I - IiI1i11I
def i11iI ( url ) :
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for url , OOOiiiiI , iIiIi11 in IIi :
  iI1Ii1iI11iiI ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iIiIi11 , '' , OOOiiiiI )
  oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 I1I1iiiiiIi1 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for I111iIii1i1 in I1I1iiiiiIi1 :
  IiI1iiiIii = ( I111iIii1i1 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  Iii1I1I11iiI1 ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iIiIi11 , '' , IiI1iiiIii )
  if 6 - 6: i1IiiiI1iI % III1iiIii / o0ii1I + i1IiiiI1iI . i1i1I1IIii1II
def oo0O0 ( INFO ) :
 oooO ( 'info for workout' , INFO )
 if 93 - 93: I1ii11iIi11i
 if 55 - 55: ii * i1i1I1IIii1II % III1iiIii + o0o00Oo0O
 if 16 - 16: Ii1I % I1ii11iIi11i % IIiIiII11i % IIiIiII11i
def OOOO0oooooO0o ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iIiiiii1i ( ( OOoO ) . replace ( 'SlyNet' , '' ) , url , 9031 , iiIi1IIiIi + 'Sport.png' )
def O00o00o0 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iIiiiii1i ( OOoO , url , 9032 , iiIi1IIiIi + 'icon.png' )
def o00OOOOoOO ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( I11iiii )
 for OOoO , url in IIi :
  if '=' in OOoO :
   pass
  else :
   iiIi1IIiI ( ( OOoO ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , iiIi1IIiIi + 'icon.png' )
def OooOoOoo0ooo0 ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  if '=' in OOoO :
   pass
  else :
   iiIi1IIiI ( OOoO , url , 222 , iiIi1IIiIi + 'icon.png' )
   if 69 - 69: I1ii11iIi11i * i1iIi
   if 91 - 91: I11i . i1iIi / oO0o / Ii * I11i
   if 52 - 52: oOo0O0Ooo - Ii / III1iiIii . i1i1I1IIii1II
def II1i1I ( url ) :
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , iiIi1IIiIi + 'bamf.png' , iiIi1IIiIi + 'bamf.png' )
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , iiIi1IIiIi + 'bamf.png' )
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  if 'mp4' in url :
   pass
  else :
   iiIi1IIiI ( ( OOoO ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOo0Oo ( url ) :
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , iiIi1IIiIi + 'bamf.png' )
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  if 'mp4' in url :
   iiIi1IIiI ( ( OOoO ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'bamf.png' )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: OOooOOo * o0ii1I
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
 if 81 - 81: oooOo0oo0oo
def OooOooo00OOO0o ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIi = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  if 'Daily' in OOoO :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , O0O00Oo , 9008 , O0O )
def II1iIIiIII ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , O0O )
def iI1i11i1i1i ( url ) :
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 iiIi1IIiI ( '[COLOR' + ooOoOoo0O + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  iiIi1IIiI ( ( OOoO ) . replace ( '_' , ' ' ) , url , 222 , O0O )
  if 83 - 83: IIiIiII11i + III1iiIii - I11i % I11i * I11i
def o0iiiii1i1 ( ) :
 I11iiii = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  if '.m3u' in O0O00Oo :
   iIiiiii1i ( ( OOoO ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + O0O00Oo ) , 9011 , iiIi1IIiIi + 'disclose.png' )
def IIII1I11Ii11 ( url ) :
 I11iiii = cloudflare . source ( url )
 IIi = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  iiIi1IIiI ( ( OOoO ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 78 - 78: oO0o
def I1IIIiIiIi ( ) :
 I11iiii = OooOoooOo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIi = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  if 'category' in O0O00Oo :
   iIiiiii1i ( OOoO , 'http://www.disclose.tv/' + O0O00Oo , 7010 , iiIi1IIiIi + 'disclose.png' )
   if 13 - 13: i1i1I1IIii1II / Iii
   if 44 - 44: o0o00Oo0O
def iiOo000O00o0O ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( I11iiii )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I11iiii )
 for url , OOoO , iIiIi11 in IIi :
  iIiiiii1i ( OOoO , 'http://www.disclose.tv/' + url , 7011 , iIiIi11 )
 for url in next :
  iIiiiii1i ( 'NEXT' , url , 7010 , iiIi1IIiIi + 'Next.png' )
  if 83 - 83: i1iIi - oooOo0oo0oo / o0o00Oo0O
  if 17 - 17: I11i . III1iiIii . Ii + ii % Ii
def IIiI1iIiii ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( I11iiii )
 IiIi1I1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  if 'http' in url :
   iiIi1IIiI ( 'video/flv' , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url , OOoO in i1Iii1i1I :
  iiIi1IIiI ( OOoO , url , 222 , iiIi1IIiIi + 'disclose.png' )
 for url in IiIi1I1 :
  iiIi1IIiI ( 'YT Link' , url , 8043 , iiIi1IIiIi + 'disclose.png' )
  if 53 - 53: i1IiiiI1iI % Ii1I
  if 17 - 17: ii % o0ii1I % o0o00Oo0O
def I1111iI ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iIiiiii1i ( OOoO , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , iiIi1IIiIi + 'icon.png' )
  if 89 - 89: III1iiIii - III1iiIii % IiI1i11I / Iii + i1i1I1IIii1II - III1iiIii
def O0oOoO0o0oO ( name , url , img ) :
 II11iIiIIIiI = OooOoooOo ( url )
 oOoOOo00oO = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 Oo0OOOOOOOo0O = len ( oOoOOo00oO )
 if 11 - 11: o0ii1I / OOooOOo - oO0o + OOooOOo
 if 51 - 51: i1iIi
 if Oo0OOOOOOOo0O == 1 :
  for IIiIi111i in oOoOOo00oO :
   IIiIi111i = IIiIi111i . replace ( 'player' , 'watch' )
   iIIi1IiiiII1i = IIiIi111i + '&fv=&sou='
   IIiIii1iiI = OooOoooOo ( iIIi1IiiiII1i )
   o0oOOOOOO = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( IIiIii1iiI )
   for IiIi1II11i in o0oOOOOOO :
    IIIIII11iIiI1III = False
    Resolve ( IiIi1II11i )
    if 81 - 81: I1ii11iIi11i
 elif Oo0OOOOOOOo0O > 1 :
  if 78 - 78: oOo0O0Ooo / ii % IiI1i11I - III1iiIii
  for IIiIi111i in oOoOOo00oO :
   i1iiIIiIi1iI = OooOoooOo ( IIiIi111i )
   Ii1IiIiI1Ii = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( i1iiIIiIi1iI )
   o0oO0oo000oo = Ii1IiIiI1Ii
   o0oO0oo000oo = ( str ( o0oO0oo000oo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + o0oO0oo000oo
   iiIi1IIiI ( 'DOUBLE LINK' , o0oO0oo000oo , 424 , '' )
   if 68 - 68: oO0o % III1iiIii - i1i1I1IIii1II - i1iIi . I1ii11iIi11i
   for url in Ii1IiIiI1Ii :
    iIiiiii1i ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     i1oO = Google . resolve ( url )
    except :
     pass
    try :
     IiII11IIII1 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( i1oO ) )
     for iIIii1I , o0o0II in IiII11IIII1 :
      if 67 - 67: i1IiiiI1iI - I1ii11iIi11i % Ii / o0ii1I . i1IiiiI1iI . i1i1I1IIii1II
      HD_URLS . append ( iIIii1I )
      SD_URLS . append ( o0o0II )
    except :
     pass
 else :
  pass
  if 44 - 44: oO0o / i1IiiiI1iI / ii
def oOOO ( ) :
 if 3 - 3: I1ii11iIi11i + oooOo0oo0oo - oOo0O0Ooo
 if 60 - 60: o0o00Oo0O / ooOoO0O00 % Ii / IiI1i11I
 iIiiiii1i ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , iiIi1IIiIi + 'Movies.png' )
 if 97 - 97: ooOoO0O00 % ii
 iIiiiii1i ( 'Search Movies' , '' , 7017 , iiIi1IIiIi + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 83 - 83: Iii . oooOo0oo0oo + i1IiiiI1iI * Iii . i1IiiiI1iI + i1i1I1IIii1II
 if 64 - 64: o0ii1I . I11i - ooOoO0O00
def iIiIi1I1iI ( ) :
 I11iiii = OooOoooOo ( 'http://cnfstudio.com/' )
 IIi = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( OOoO , 'http://cnfstudio.com/genre/' + O0O00Oo , 7003 , iiIi1IIiIi + 'icon.png' )
  if 98 - 98: o0o00Oo0O + o0o00Oo0O
iIii1 = xbmcgui . Dialog ( )
if 34 - 34: III1iiIii
iIiIIiII11i1 = '{UN},' ; i1Iii = '{IG},' ; oOOooo = '{PL},' ; IiI11IiIIi = '{LO},' ; oOOo0OoooOo = '{LP},' ; I1I1IiIiIIi1I = '{HA},' ; oo0Ooo = '{XD},' ; iI1II1III = '{TA},' ; OOOIi11i1II = '{DP},' ; Ooo0o000OOO000o = '{JT},' ; o000ooOO = '{JJ},' ; O000oOO0Oooo = '{MM},' ; o0000oO0OOOo0 = '{FQ},' ; o00ooo0O = '{HH},'
if 54 - 54: Ii1I * III1iiIii
def I11I11III ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( I11iiii )
 IIi1i1iI11I11 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( I11iiii )
 for iIiIi11 , url , OOoO in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iIiIi11 )
 IIi1i1iI11I11 = IIi1i1iI11I11
 for url in IIi1i1iI11I11 :
  iIiiiii1i ( 'Next Page' , url , 7003 , iiIi1IIiIi + 'Next.png' )
  if 67 - 67: Ii % Iii
def ii1I11iIi ( url ) :
 if 13 - 13: o0o00Oo0O . IiI1i11I - III1iiIii % Ii % oOo0O0Ooo
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  iiI111I1iIiI = url + '&fv=&sou='
  iiI111I1iIiI = iiI111I1iIiI . replace ( 'player' , 'watch' )
  oooO00OOO0 = IIIiiI1I ( iiI111I1iIiI )
  O0OO0OoO00oOo = IIIiiI1I ( url )
  if 35 - 35: IIiIiII11i . oooOo0oo0oo + iI11I1II1I1I . ooOoO0O00 - OOooOOo + III1iiIii
  if 55 - 55: I1ii11iIi11i % i1IiiiI1iI . IIiIiII11i
def IIIiiI1I ( url ) :
 if 53 - 53: o0o00Oo0O / oO0o % Ii
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( I11iiii )
 for url in IIi :
  ii1O0ooooo000 ( url )
  if 11 - 11: i1IiiiI1iI + ooOoO0O00 - IiI1i11I - oO0o * i1iIi / i1iIi
  if 4 - 4: iI11I1II1I1I - Ii * oO0o . i1IiiiI1iI + I11i
def IIIII11IIi ( ) :
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Local M3u[/COLOR]' , II , 2001 , iiIi1IIiIi + 'LocalM3U.png' , Oo00OOOOO , '' )
 Iii1I1I11iiI1 ( '[COLOR' + ooOoOoo0O + ']Remote M3u[/COLOR]' , iiI1IiI , 7080 , iiIi1IIiIi + 'RemoteM3U.png' , Oo00OOOOO , '' )
 if 50 - 50: i1IiiiI1iI % III1iiIii
def OoOOOoo ( ) :
 if os . path . exists ( II ) :
  o00O0oOO0o = open ( II , 'r' )
  for iII1i11 in o00O0oOO0o :
   O0000000oooOO = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iII1i11 )
   for OOoO , O0O00Oo in O0000000oooOO :
    iiIi1IIiI ( OOoO , O0O00Oo , 222 , iiIi1IIiIi + 'streams.png' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 7 - 7: oO0o - i1iIi % ooOoO0O00
def iI1i1IIi1i1 ( url ) :
 if os . path . exists ( Remote ) :
  II11iIiIIIiI = o0O0Oo00 ( url )
  IIi = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
  for OOoO , url in IIi :
   url = ( url ) . strip ( )
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  iIii1 . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 88 - 88: iI11I1II1I1I / IIiIiII11i . Ii / oooOo0oo0oo / III1iiIii / III1iiIii
  if 62 - 62: OOooOOo + o0ii1I . o0o00Oo0O . oooOo0oo0oo % IiI1i11I
def oo0OOo0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo in IIi :
  O0O00Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + O0O00Oo
 OOoO = 'plugin.video.GenieTv'
 if 28 - 28: I1ii11iIi11i . IiI1i11I % o0o00Oo0O - OOooOOo
 oo0OOO0O0 ( O0O00Oo , OOoO )
 if 99 - 99: ooOoO0O00 - o0o00Oo0O / IIiIiII11i + IIiIiII11i . III1iiIii / i1i1I1IIii1II
def O0 ( ) :
 II11iIiIIIiI = OooOoooOo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIi = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo in IIi :
  O0O00Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + O0O00Oo
 OOoO = 'repository.GenieTv'
 if 22 - 22: IiI1i11I . ii . I1ii11iIi11i
 oo0OOO0O0 ( O0O00Oo , OOoO )
 if 44 - 44: OOooOOo / I1ii11iIi11i . ii % ii * Ii
 if 60 - 60: III1iiIii / iI11I1II1I1I + ii - Ii1I * Ii
def O0O0Oooo0o ( ) :
 IiI1i = [ '[COLOR' + ooOoOoo0O + ']CATAGORIES[/COLOR]' , '[COLOR' + ooOoOoo0O + ']SEARCH[/COLOR]' ]
 o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']TOOLS[/COLOR]' , IiI1i )
 if o0Oo00 == 0 :
  Iii1iIIi1iIii ( )
 if o0Oo00 == 1 :
  oOOoo0o00 ( )
  if 75 - 75: iI11I1II1I1I * IiI1i11I / OOooOOo * IIiIiII11i . ooOoO0O00
  if 6 - 6: o0ii1I % o0ii1I / ii * i1i1I1IIii1II . oOo0O0Ooo . ooOoO0O00
  if 59 - 59: Iii . Iii * oOo0O0Ooo - o0ii1I % OOooOOo
  if 19 - 19: ii / I1ii11iIi11i - i1IiiiI1iI . OOooOOo
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
iIii1 = xbmcgui . Dialog ( )
oOo0oooo00o = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
i1i1i11IIii = 'https://addons.tvaddons.ag/'
if 11 - 11: i1iIi . i1IiiiI1iI - IiI1i11I . I11i
def oOOoo0o00 ( ) :
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 IiI11Ii1iI = 'https://addons.tvaddons.ag/search/?keyword=' + oOO0oo
 II11iIiIIIiI = OooOoooOo ( IiI11Ii1iI )
 IIi = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( II11iIiIIIiI )
 for O0O00Oo , oOo00 , OOoO in IIi :
  Iii1I1I11iiI1 ( OOoO , O0O00Oo , 10054 , 'https://addons.tvaddons.ag/' + oOo00 , Oo00OOOOO , '' )
  if 41 - 41: i1i1I1IIii1II / oO0o - oO0o + i1iIi * oooOo0oo0oo
  if 13 - 13: i1IiiiI1iI * IIiIiII11i - OOooOOo
def Iii1iIIi1iIii ( ) :
 II11iIiIIIiI = OooOoooOo ( i1i1i11IIii )
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
   if 3 - 3: oooOo0oo0oo + i1iIi * Ii . IiI1i11I / iI11I1II1I1I
   if 44 - 44: oO0o
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
  if 74 - 74: o0ii1I * ooOoO0O00 * Iii - ii . oOo0O0Ooo
  if 24 - 24: IIiIiII11i - Ii * ooOoO0O00 . i1iIi
def i1ii ( url , name ) :
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
   if 17 - 17: i1IiiiI1iI + Ii . Ii * ooOoO0O00 / o0o00Oo0O
def oo0OOO0O0 ( url , name ) :
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
 if 2 - 2: IIiIiII11i / oO0o % iI11I1II1I1I / Ii
def ii1iii1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 52 - 52: i1iIi % iI11I1II1I1I . Ii % i1iIi
 if 86 - 86: i1i1I1IIii1II % iI11I1II1I1I % OOooOOo
def OO000OOO ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , oOo00 , OOoO in IIi :
  iIiiiii1i ( OOoO , url , 1007 , oOo00 )
def o000OOooo000O ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , oOo00 , OOoO in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 1006 , oOo00 )
  if 69 - 69: o0o00Oo0O . IiI1i11I
def o0oOoO00oo0oOo ( ) :
 I11iiii = OooOoooOo ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , oo00O00oO000o , OOOiiiiI , oooOo0OOOoo0 , OOoO in IIi :
  iiOO00O ( OOoO , 100109 , O0O00Oo , image = oo00O00oO000o , isFolder = True )
  if 15 - 15: o0o00Oo0O
def I11IiI1III ( url ) :
 import random
 O0oOo = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 O0oOo . clear ( )
 i1IiI1ii = [ ]
 i1IiI11I11I = [ ]
 I1III11i11Iii = [ ]
 II11iIiIIIiI = OooOoooOo ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for i1oO , oo00O00oO000o , OOOiiiiI , oooOo0OOOoo0 , OOoO in IIi :
  i1IiI1ii . append ( [ i1oO , OOoO ] )
  if len ( i1IiI1ii ) == len ( IIi ) :
   for iII1i11 in i1IiI1ii :
    IiiIiiIiiIII = random . randint ( 1 , len ( i1IiI1ii ) )
    try :
     Ii1i11IIiI = i1IiI1ii [ int ( IiiIiiIiiIII ) ]
    except :
     pass
    if len ( i1IiI11I11I ) <= 20 :
     if Ii1i11IIiI [ 1 ] not in I1III11i11Iii :
      o0o = OooOoooOo ( Ii1i11IIiI [ 0 ] )
      IiIi1I1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( o0o )
      for III1i1 , Oo00oooO00o in IiIi1I1 :
       OOoOoo = OooOoooOo ( III1i1 )
       I1i11 = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( OOoOoo )
       for oooO0Oo0O , iiI111I1iIiI in I1i11 :
        if 'panda' in iiI111I1iIiI :
         IiI1 = OooOoooOo ( iiI111I1iIiI )
         oOOo00O0OOOo = re . compile ( "url: '(.+?)'" ) . findall ( IiI1 )
         for iIIIi111 in oOOo00O0OOOo :
          if 'http' in iIIIi111 :
           I1iiii = xbmcgui . ListItem ( Ii1i11IIiI [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : Ii1i11IIiI [ 1 ] } )
           I1iiii . setProperty ( "IsPlayable" , "true" )
           O0oOo . add ( iIIIi111 , I1iiii )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1iiii )
           if 13 - 13: I1ii11iIi11i * I11i * IiI1i11I
def iiOO00O ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = O0O
 oOoOoo0 = sys . argv [ 0 ]
 oOoOoo0 += '?mode=' + str ( mode )
 oOoOoo0 += '&title=' + urllib . quote_plus ( name )
 oOoOoo0 += '&image=' + urllib . quote_plus ( image )
 oOoOoo0 += '&page=' + str ( page )
 if url != '' :
  oOoOoo0 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  oOoOoo0 += '&keyword=' + urllib . quote_plus ( keyword )
 I1iiii = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  I1iiii . addContextMenuItems ( contextMenu )
 if infoLabels :
  I1iiii . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  I1iiii . setProperty ( "IsPlayable" , "true" )
 I1iiii . setProperty ( 'Fanart_Image' , Oo00OOOOO )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = isFolder )
 if 71 - 71: oooOo0oo0oo + ii + iI11I1II1I1I
 if 99 - 99: oO0o - III1iiIii * III1iiIii + i1i1I1IIii1II / IiI1i11I + oooOo0oo0oo
def i1i1I111iIi1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , iconimage , OOOiiiiI , oooOo0OOOoo0 , name in IIi :
  if 'http' in url :
   if '.php' in url :
    iiiiI11ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
    for iII1i11 in iiiiI11ii :
     if iII1i11 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    iiii ( name , url , 1016 , iconimage , oooOo0OOOoo0 , OOOiiiiI )
   else :
    if 'youtube' in url :
     iiiiI11ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in iiiiI11ii :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iIIiiII11i1I1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , oooOo0OOOoo0 , OOOiiiiI )
    else :
     iiiiI11ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
     for iII1i11 in iiiiI11ii :
      if iII1i11 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iIIiiII11i1I1 ( name , url , 222 , iconimage , oooOo0OOOoo0 , OOOiiiiI )
     oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
  else :
   Oo0oOO ( url , iconimage , name )
   if 49 - 49: ooOoO0O00 . III1iiIii
 else :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
  for url , oOo00 , name in IIi :
   if 'http' in url :
    if '.php' in url :
     iIiiiii1i ( name , url , 1016 , oOo00 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      iiIi1IIiI ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOo00 )
     else :
      iiiiI11ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( O0Oo000ooO00 ) )
      for iII1i11 in iiiiI11ii :
       if iII1i11 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      iiIi1IIiI ( name , url , 222 , oOo00 )
      oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
   else :
    Oo0oOO ( url , oOo00 , name )
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 82 - 82: oO0o / Iii
def Oo0oOO ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ii1iIIIi1Iii1 = ( url ) . replace ( oO000OO0 , 'http' ) . replace ( II1I1i , '.com' ) ;
 oOoOOOo0oo = ( ii1iIIIi1Iii1 ) . replace ( ooOOoOoo0OO , 'a' ) . replace ( oOO0O0Ooo0 , 'b' ) . replace ( I11iiI1i , 'c' ) . replace ( IiI111iIIII , 'd' ) . replace ( oOOooo , 'e' ) . replace ( Ooo0o000OOO000o , 'f' ) ;
 O000Oo0O = ( oOoOOOo0oo ) . replace ( I11Oo0O00O0O00 , 'g' ) . replace ( I1I1IiIiIIi1I , 'h' ) . replace ( O00OoOo0OooOo , 'i' ) . replace ( IIi11ii , 'j' ) . replace ( ooOoOO , 'k' ) . replace ( iIiiII11 , 'l' ) ;
 oo000oo0oOo0 = ( O000Oo0O ) . replace ( IIiO0 , 'm' ) . replace ( i1I1ii1iI1 , 'n' ) . replace ( OoI1Ii , 'o' ) . replace ( IIIII1iII1 , 'p' ) . replace ( OO0oOoO0O0 , 'q' ) . replace ( iiiI1i , 'r' ) ;
 O0OooO00O0 = ( oo000oo0oOo0 ) . replace ( iiI1i111I1 , 's' ) . replace ( ii1Ii11 , 't' ) . replace ( iiI , 'u' ) . replace ( i11i1I1 , 'v' ) . replace ( o0OoO0 , 'w' ) . replace ( I11Ii1I1I , 'x' ) ;
 oo00OO0o0 = ( O0OooO00O0 ) . replace ( o0oo0000Oo , 'y' ) . replace ( o00O00 , 'z' ) . replace ( iIiIIiII11i1 , '.' ) . replace ( i1Iii , '(' ) . replace ( IiI11IiIIi , ')' ) . replace ( oOOo0OoooOo , '/' ) ;
 I1I1Ii1Iii = ( oo00OO0o0 ) . replace ( o00OO0 , '1' ) . replace ( Oo0OOOooo0ooo , '2' ) . replace ( O00oooOoO , '3' ) . replace ( iI1II1III , '4' ) . replace ( OOOIi11i1II , '5' ) . replace ( OOooOoOOo0O , '6' ) ;
 IIi1i111 = ( I1I1Ii1Iii ) . replace ( o000ooOO , '7' ) . replace ( O000oOO0Oooo , '8' ) . replace ( o0000oO0OOOo0 , '9' ) . replace ( o00ooo0O , '0' ) . replace ( o0oOo , ':' ) . replace ( II1 , '%' ) ;
 url = ( IIi1i111 ) . replace ( I1iii1I11i1I1iII , '-' ) . replace ( oo0Ooo , '_' ) ;
 iiIi1IIiI ( name , url , 222 , iconimage ) ;
 if 24 - 24: oOo0O0Ooo . III1iiIii % OOooOOo / IIiIiII11i
 if 100 - 100: Ii1I % i1iIi + oOo0O0Ooo
def i1iIiII1iI ( ) :
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for O0O00Oo , oOo00 , OOoO in IIi :
  iIiiiii1i ( OOoO , O0O00Oo , 1007 , oOo00 )
def oOoO0OoOo0O000 ( url ) :
 if 43 - 43: I1ii11iIi11i . Ii + ooOoO0O00
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , oOo00 , OOoO in IIi :
  iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 1006 , oOo00 )
  if 83 - 83: IiI1i11I + OOooOOo % i1iIi
def ooOooooO00 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 OOOiII1 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 OOOiII1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOOiII1 )
 if 51 - 51: ii + Ii
 if 57 - 57: I1ii11iIi11i % I11i
def i1I1ii1i ( url ) :
 I11iiii = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iiii )
 for url , iIiIi11 , OOoO in IIi :
  if '-dir-' in OOoO :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , iIiIi11 )
  else :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' , url , 1006 , iIiIi11 )
   if 99 - 99: I11i / Ii / IIiIiII11i + oooOo0oo0oo . ooOoO0O00 + OOooOOo
def II11 ( url ) :
 I11iiii = o0O0Oo00 ( url )
 iIiOOO0oo0OO0o0 = ( 'http://afewbitsmore.com/' )
 IIi = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '[To Parent Directory]' in OOoO :
   OOoO = 'HOME'
   pass
  elif 'HOME' in OOoO :
   pass
  elif '.m3u' in OOoO :
   iIiiiii1i ( '[COLOR' + ooOoOoo0O + ']PLAY ALL[/COLOR]' , iIiOOO0oo0OO0o0 + url , 2002 , iiIi1IIiIi + 'music.png' )
  elif '.mp3' in OOoO :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , iIiOOO0oo0OO0o0 + url , 222 , iiIi1IIiIi + 'music.png' )
  elif '.m4a' in OOoO :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , iIiOOO0oo0OO0o0 + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) , iIiOOO0oo0OO0o0 + url , 1012 , iiIi1IIiIi + 'music.png' )
def OOoO0 ( url ) :
 II11iIiIIIiI = o0O0Oo00 ( url )
 IIi = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( II11iIiIIIiI )
 for iIiIi11 , OOoO , url in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iiIi1IIiIi + 'music.png' )
  if 78 - 78: Iii - oOo0O0Ooo * III1iiIii
def iio0O0OOo ( url ) :
 I11iiii = o0O0Oo00 ( url )
 iIiOOO0oo0OO0o0 = url
 IIi = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( I11iiii )
 for url , OOoO in IIi :
  if '.mp3' in OOoO :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , iiIi1IIiIi + 'music.png' )
  else :
   iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '/' , '' ) , iIiOOO0oo0OO0o0 + url , 1011 , iiIi1IIiIi + 'music.png' )
def ii1IiiiI1I ( ) :
 I11iiii = o0O0Oo00 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIi = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( I11iiii )
 for O0O00Oo , iIiIi11 , OOoO in IIi :
  iIiiiii1i ( OOoO , ( 'http://www.cyn.net/music/' + O0O00Oo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iIiIi11 ) . replace ( ' ' , '%20' ) )
def i1iiOOOO0oo0o0O ( url , img ) :
 I11iiii = o0O0Oo00 ( url )
 i1oO = url
 img = img
 IIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( i1oO + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 29 - 29: Ii1I + ii . oO0o . ooOoO0O00 - ii * Ii
def iII1i1ii ( url ) :
 I11iiii = o0O0Oo00 ( url )
 i1oO = url
 IIi = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I11iiii )
 for type , url , OOoO in IIi :
  if '[VID]' in type :
   iiIi1IIiI ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , i1oO + url , 222 , iiIi1IIiIi + 'music.png' )
  if '[DIR]' in type :
   iII1i1ii ( i1oO + url )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 19 - 19: Ii1I * o0o00Oo0O - i1iIi
 if 27 - 27: IiI1i11I / I11i . OOooOOo * o0ii1I * i1IiiiI1iI
def iiiiII11iIi ( ) :
 iii11 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 iii1 = iIii1 . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOO0oo = iii1 . lower ( )
 O0O00Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 iiI11ii1111 = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 i1oO = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 81 - 81: i1IiiiI1iI
 II11iIiIIIiI = O00O0oOO00O00 ( O0O00Oo )
 i11II1I11I1 = O00O0oOO00O00 ( iiI11ii1111 )
 o0o = O00O0oOO00O00 ( i1oO )
 if 45 - 45: oooOo0oo0oo * IIiIiII11i * ii / ii * i1IiiiI1iI
 if II11iIiIIIiI != 'Failed' :
  IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II11iIiIIIiI )
  for O0O00Oo , oo00O00oO000o , OOOiiiiI , iII11I1Ii1 , OOoO in IIi :
   if iii1 in OOoO . lower ( ) :
    Iii1I1I11iiI1 ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , O0O00Oo , 1016 , oo00O00oO000o , oooOo0OOOoo0 , OOOiiiiI )
    if 38 - 38: IiI1i11I . ii
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if i11II1I11I1 != 'Failed' :
  OooO0oOo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i11II1I11I1 )
  for O0O00Oo , OOoO in OooO0oOo :
   if iii1 in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + O0O00Oo ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 28 - 28: i1IiiiI1iI * ooOoO0O00 . Ii1I
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
 if o0o != 'Failed' :
  i1Iii1i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( o0o )
  for O0O00Oo , OOoO in i1Iii1i1I :
   if iii1 in OOoO . lower ( ) :
    iIiiiii1i ( ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + O0O00Oo ) . replace ( ' ' , '%20' ) , 1006 , iiIi1IIiIi + 'Music.png' )
    if 75 - 75: o0o00Oo0O / i1i1I1IIii1II * i1iIi - oooOo0oo0oo / ooOoO0O00
    oOI1Ii1I1 ( 'tvshows' , 'Media Info 3' )
    if 61 - 61: Iii
    if 100 - 100: o0o00Oo0O - iI11I1II1I1I * I1ii11iIi11i
    if 35 - 35: i1iIi
    if 57 - 57: oO0o . I1ii11iIi11i + oOo0O0Ooo
    if 18 - 18: oOo0O0Ooo - Ii1I * Iii / Ii - I11i % I11i
    if 31 - 31: Iii
IIiO0 = '{SF},' ; i1I1ii1iI1 = '{IF},' ; OoI1Ii = '{PW},' ; O00oooOoO = '{AM},' ; IIIII1iII1 = '{GF},' ; OO0oOoO0O0 = '{DD},' ; iiiI1i = '{UO},' ; iiI1i111I1 = '{LE},' ; iiI = '{ZY},' ; i11i1I1 = '{UE},' ; o0OoO0 = '{PE},' ; I11Ii1I1I = '{JE},' ; o0oo0000Oo = '{TH},' ; o00O00 = '{LK},'
if 100 - 100: Ii * Ii . iI11I1II1I1I % IiI1i11I * Ii1I
if 17 - 17: o0ii1I * III1iiIii * Ii / Ii1I / Ii
def o00oOoOo0 ( ) :
 I11iiii = OooOoooOo ( 'http://www.iwatchseries.me/tv-list/' )
 IIi = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( OOoO , O0O00Oo , 8021 , iiIi1IIiIi + 'iwatch.png' )
  oOI1Ii1I1 ( 'movies' , 'MAIN' )
def IiiiiI ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( I11iiii )
 for url , OOoO , OO0o0O0O0O0 in IIi :
  iIiiiii1i ( OOoO + OO0o0O0O0O0 , url , 8022 , iiIi1IIiIi + 'iwatch.png' )
def I1I1i1iIi11i ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I11iiii )
 for url in IIi :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  II1ii1ii ( url )
def II1ii1ii ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I11iiii )
 i1Iii1i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I11iiii )
 IiIi1I1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( I11iiii )
 I1i11 = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iiIi1IIiI ( 'VidSpot - ' + OOoO , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url in i1Iii1i1I :
  iiIi1IIiI ( 'VodLocker' , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for url , OOoO in I1i11 :
  iiIi1IIiI ( 'VidUp' + OOoO , url , 222 , iiIi1IIiIi + 'iwatch.png' )
 for OOoO , url in IiIi1I1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   iiIi1IIiI ( 'TheVideo - ' + OOoO , url , 222 , iiIi1IIiIi + 'iwatch.png' )
   if 85 - 85: oO0o . I11i . oOo0O0Ooo
def Oo000o0o0 ( ) :
 I11iiii = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIi = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( OOoO , O0O00Oo , 1021 , iiIi1IIiIi + 'anime.png' )
  if 76 - 76: i1i1I1IIii1II * i1iIi - iI11I1II1I1I
  if 25 - 25: OOooOOo / I1ii11iIi11i / ii
def o0OO0O0oo ( ) :
 I11iiii = OooOoooOo ( 'http://www.animetoon.org/cartoon' )
 IIi = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I11iiii )
 for O0O00Oo , OOoO in IIi :
  iIiiiii1i ( OOoO , O0O00Oo , 1002 , iiIi1IIiIi + 'anime.png' )
  if 40 - 40: ooOoO0O00
  if 49 - 49: i1IiiiI1iI + III1iiIii
  if 28 - 28: I11i % i1IiiiI1iI
def i11II1iIi1Ii ( url ) :
 I11iiii = OooOoooOo ( url )
 i1Iii1i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( I11iiii )
 for iIiIi11 in i1Iii1i1I :
  IiIiIiiIIii = iIiIi11
 IiIi1I1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( I11iiii )
 for url in IiIi1I1 :
  iIiiiii1i ( 'NEXT PAGE' , url , 1002 , iiIi1IIiIi + 'Next.png' )
 IIi = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( I11iiii )
 for url , OOoO in IIi :
  iIiiiii1i ( OOoO , url , 1003 , IiIiIiiIIii )
 xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o0oo0oO ( url , IMAGE ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( I11iiii )
 for OOoO , url in IIi :
  print OOoO + '     ' + url
  if 'easy' in url :
   iII1IiI1I11i ( url )
  elif 'playpanda' in url :
   iII1IiI1I11i ( url )
   if 10 - 10: IIiIiII11i % oOo0O0Ooo % o0ii1I * Ii1I
  xbmcplugin . addSortMethod ( OOOOi11i1 , xbmcplugin . SORT_METHOD_TITLE ) ;
def iII1IiI1I11i ( url ) :
 I11iiii = OooOoooOo ( url )
 IIi = re . compile ( "url: '(.+?)'," ) . findall ( I11iiii )
 for url in IIi :
  iiIi1IIiI ( 'STREAM' , url , 222 , iiIi1IIiIi + 'anime.png' )
  if 74 - 74: I11i / oO0o + IiI1i11I - ooOoO0O00 / ii / Ii1I
  if 56 - 56: i1i1I1IIii1II + oOo0O0Ooo . Iii
def O0OO0 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 . add_header ( 'referer' , url )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 74 - 74: I11i % oOo0O0Ooo * o0ii1I + iI11I1II1I1I
def o0O0Oo00 ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 79 - 79: I11i
def iiii111iI ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ii1i1IiII111I = ( '%s%s' % ( Oo0o0OoOoOo0 , url ) )
 iiI111I1iIiI = o0O0Oo00 ( url )
 IIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iiI111I1iIiI )
 for url , oOo00 , OOoO in IIi :
  iiIi1IIiI ( '%s' % ( '[COLOR' + ooOoOoo0O + ']' + OOoO + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oOo00 )
  if 17 - 17: ii
def II11I11I ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  o0Oo00oooOO ( url , OOoO )
 else :
  OooO0OO ( url )
def OooO0OO ( url ) :
 import urlresolver
 try :
  OO0OoOo0O = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( OO0OoOo0O , xbmcgui . ListItem ( OOoO ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( OOoO ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def ii1O0ooooo000 ( url ) :
 if 84 - 84: ii + IiI1i11I . Ii - o0o00Oo0O / o0o00Oo0O % ooOoO0O00
 O0i1i1II1i11 = open ( OOOO0OOoO0O0 , "a" )
 O0i1i1II1i11 . write ( 'url="' + url + '"\n' )
 O0i1i1II1i11 . close
 if 38 - 38: iI11I1II1I1I - IIiIiII11i
 ooO0O0o0 = xbmc . Player ( OO0OOooOO0 ( ) )
 import urlresolver
 try : ooO0O0o0 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( OOoO ) )
 ooO0O0o0 = xbmc . Player ( OO0OOooOO0 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  iIii1 = xbmcgui . Dialog ( )
  if iIii1 . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   iIii1 . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : ooO0O0o0 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def o0Oo00oooOO ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  IIII1i = '.mp4'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   iIii11iIi ( url , name , IIII1i )
 elif '.mkv' in url :
  IIII1i = '.mkv'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   iIii11iIi ( url , name , IIII1i )
 elif '.mp3' in url :
  IIII1i = '.mp3'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   iIii11iIi ( url , name , IIII1i )
 elif '.avi' in url :
  IIII1i = '.avi'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   iIii11iIi ( url , name , IIII1i )
 elif '.mov' in url :
  IIII1i = '.mov'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   iIii11iIi ( url , name , IIII1i )
 elif '.mpeg' in url :
  IIII1i = '.mpeg'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   iIii11iIi ( url , name , IIII1i )
 elif '.mpg' in url :
  IIII1i = '.mpg'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   iIii11iIi ( url , name , IIII1i )
 elif '.flv' in url :
  IIII1i = '.flv'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   iIii11iIi ( url , name , IIII1i )
 elif '.wmv' in url :
  IIII1i = '.wmv'
  IiI1i = [ '[COLOR' + ooOoOoo0O + ']PLAY[/COLOR]' , '[COLOR' + ooOoOoo0O + ']DOWNLOAD[/COLOR]' ]
  o0Oo00 = xbmcgui . Dialog ( ) . select ( '[COLOR' + ooOoOoo0O + ']Play/Download[/COLOR]' , IiI1i )
  if o0Oo00 == 0 :
   OooO0OO ( url )
  if o0Oo00 == 1 :
   iIii11iIi ( url , name , IIII1i )
 else :
  OooO0OO ( url )
def iIii11iIi ( url , name , cat ) :
 i11i11IiI1iIi ( )
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
def i11i11IiI1iIi ( ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( OooO0 ) )
 if not os . path . exists ( OooO0 ) :
  iIii1 . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def i1IO0oO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % OOoO )
 xbmc . sleep ( 1 )
 ooO0O0o0 = xbmc . Player ( OO0OOooOO0 ( ) )
 o0oOoO00o . update ( 100 , '%s' % OOoO )
 xbmc . sleep ( 1 )
 ooO0O0o0 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 2 - 2: IIiIiII11i - oO0o . ooOoO0O00 . oOo0O0Ooo . IIiIiII11i * i1IiiiI1iI
def ooO00O00oOO ( url ) :
 ooO0O0o0 = xbmc . Player ( OO0OOooOO0 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : ooO0O0o0 . play ( url ) . strip ( )
 except : pass
 if 20 - 20: III1iiIii + I11i
def ii1iiiIiiIiiI ( url ) :
 ooO0O0o0 = xbmc . Player ( OO0OOooOO0 ( ) )
 import urlresolver
 o0OOooo0ooo0o = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 ooO0O0o0 . play ( o0OOooo0ooo0o )
 xbmc . sleep ( 1 )
 ooO0O0o0 . play ( url )
 if 50 - 50: o0ii1I + o0ii1I
 if 51 - 51: Ii1I / ii * III1iiIii
def OO0OOooOO0 ( ) :
 try :
  o0oO = getSet ( "core-player" )
  if ( o0oO == 'DVDPLAYER' ) : II1iOO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0oO == 'MPLAYER' ) : II1iOO = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0oO == 'PAPLAYER' ) : II1iOO = xbmc . PLAYER_CORE_PAPLAYER
  else : II1iOO = xbmc . PLAYER_CORE_AUTO
 except : II1iOO = xbmc . PLAYER_CORE_AUTO
 return II1iOO
 return True
 if 51 - 51: OOooOOo * ii * I1ii11iIi11i
def iIiiiii1i ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oooooOo0 = [ ]
  oooooOo0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oooooOo0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oooooOo0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1iiii . addContextMenuItems ( oooooOo0 )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = True )
 return ii1II
 if 28 - 28: Ii - o0ii1I
def O0oo00oOOO0o ( name , url , mode , iconimage , fanart , description ) :
 if 59 - 59: IIiIiII11i - oO0o
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iiii . setProperty ( "Fanart_Image" , fanart )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = True )
 return ii1II
 if 31 - 31: Iii - OOooOOo / I11i * OOooOOo / I1ii11iIi11i + I11i
def iiIi1IIiI ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  oooooOo0 = [ ]
  oooooOo0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   oooooOo0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oooooOo0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  I1iiii . addContextMenuItems ( oooooOo0 )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = False )
 return ii1II
 if 46 - 46: III1iiIii * oO0o / oooOo0oo0oo + I1ii11iIi11i
 if 24 - 24: i1iIi % oooOo0oo0oo . o0o00Oo0O * I1ii11iIi11i
 if 52 - 52: o0o00Oo0O . i1IiiiI1iI + IiI1i11I / Ii
 if 52 - 52: i1i1I1IIii1II % I1ii11iIi11i * IIiIiII11i
 if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
 if 27 - 27: ooOoO0O00 - i1i1I1IIii1II + oooOo0oo0oo
def i1i1iiI11I ( url , heading , announce ) :
 class OOOOo000oOo ( ) :
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
   try : IiII111i1i11 = open ( announce ) ; o00oIiii1Ii = IiII111i1i11 . read ( )
   except : o00oIiii1Ii = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( o00oIiii1Ii ) )
   return
 OOOOo000oOo ( )
 OOOOo000oOo ( )
def oooO ( heading , announce ) :
 class OOOOo000oOo ( ) :
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
   try : IiII111i1i11 = open ( announce ) ; o00oIiii1Ii = IiII111i1i11 . read ( )
   except : o00oIiii1Ii = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( o00oIiii1Ii ) )
   return
 OOOOo000oOo ( )
 OOOOo000oOo ( )
def oooooo0O000o ( ) :
 i1i1iiI11I ( iiIi1IIiIi + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 42 - 42: oooOo0oo0oo % oooOo0oo0oo
 if 87 - 87: I1ii11iIi11i + oOo0O0Ooo % oOo0O0Ooo * Ii
 if 68 - 68: IiI1i11I . oooOo0oo0oo
 if 6 - 6: o0ii1I - I11i % Iii + Ii
 if 40 - 40: o0o00Oo0O . o0ii1I
def ii1iii1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 58 - 58: Ii * IiI1i11I / o0ii1I - i1i1I1IIii1II - Ii1I % I11i
 if 16 - 16: ii
 if 71 - 71: o0ii1I % o0o00Oo0O / i1IiiiI1iI % IiI1i11I - IIiIiII11i / oO0o
 if 30 - 30: Iii
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
 if 63 - 63: IiI1i11I - oO0o * oooOo0oo0oo
 if 89 - 89: IiI1i11I / I1ii11iIi11i
 if 66 - 66: I11i + OOooOOo % ii . Iii
 if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
 if 93 - 93: ooOoO0O00 + i1IiiiI1iI / oO0o - Iii % I1ii11iIi11i / o0ii1I
 if 1 - 1: I1ii11iIi11i / o0ii1I . Ii % oooOo0oo0oo + I11i + o0o00Oo0O
 if 54 - 54: i1IiiiI1iI + i1iIi % III1iiIii
 if 83 - 83: I11i * iI11I1II1I1I
def IIIi1I1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOIIIiIII111iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 61 - 61: oO0o . Ii - oO0o
def iIi1I111Ii1I1 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + o00OO0Oo0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 25 - 25: i1IiiiI1iI . III1iiIii % o0o00Oo0O % ooOoO0O00
def oo0Oo0oo000 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + Ii11I111Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 12 - 12: OOooOOo % ii
def OOOOo00o0 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiiIiIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 81 - 81: i1IiiiI1iI / i1IiiiI1iI + i1iIi - o0ii1I
def O0IiIi1IIiII1i ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + O00oo0Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 23 - 23: ii
def ooOOOo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + ooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 97 - 97: oOo0O0Ooo
def OooOooooo ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + oOooOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 42 - 42: ooOoO0O00
def O0Oo0O0O0000 ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiIIiI1i1IIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 75 - 75: oOo0O0Ooo % IIiIiII11i * i1i1I1IIii1II % ooOoO0O00 % oooOo0oo0oo
def oOooo0o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + IiiOOo0ooO000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 42 , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 52 - 52: I1ii11iIi11i - i1i1I1IIii1II * Ii % I11i + oOo0O0Ooo . i1i1I1IIii1II
def oOOoo00O00o ( url ) :
 iiI111I1iIiI = OooOoooOo ( str ( oO0000OOo00 ) + I11iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIi = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( iiI111I1iIiI )
 for OOoO , url , oo00O00oO000o , oooOo0OOOoo0 , I1iIII1 in IIi :
  Iii1I1I11iiI1 ( OOoO , url , 5 , iiIi1IIiIi + 'GenieTVRSSFeed.png' , iiIi1IIiIi + 'GenieTVRSSFeed.png' , I1iIII1 )
 oOI1Ii1I1 ( 'movies' , 'MAIN' )
 if 73 - 73: o0o00Oo0O
 if 19 - 19: III1iiIii / I11i - o0ii1I . Ii + i1i1I1IIii1II % OOooOOo
 if 97 - 97: oooOo0oo0oo . oooOo0oo0oo . IiI1i11I . IiI1i11I
 if 63 - 63: o0o00Oo0O * III1iiIii / I1ii11iIi11i . oOo0O0Ooo . oOo0O0Ooo / Ii
 if 17 - 17: iI11I1II1I1I / oO0o - IIiIiII11i
 if 46 - 46: iI11I1II1I1I * i1i1I1IIii1II / Ii + IIiIiII11i + Iii
 if 30 - 30: o0o00Oo0O * III1iiIii - i1IiiiI1iI % o0o00Oo0O * o0ii1I
 if 29 - 29: Ii1I % Ii1I % o0ii1I + i1iIi % iI11I1II1I1I
 if 41 - 41: Ii1I % i1IiiiI1iI
def oOii11I ( ) :
 try :
  if os . path . exists ( o0 ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OO0ii1 , III11iIIi , iIIi in os . walk ( o0 ) :
     II1iIIiIIi = 0
     II1iIIiIIi += len ( iIIi )
     if II1iIIiIIi > 0 :
      for IiII111i1i11 in iIIi :
       os . unlink ( os . path . join ( OO0ii1 , IiII111i1i11 ) )
  oOi1 = os . path . join ( I11i1 , "Textures13.db" )
  os . unlink ( oOi1 )
  iIii1 . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 89 - 89: i1i1I1IIii1II
 if 27 - 27: I11i
 if 13 - 13: Ii1I - o0o00Oo0O * i1i1I1IIii1II % iI11I1II1I1I . oOo0O0Ooo - oooOo0oo0oo
 if 77 - 77: OOooOOo + ooOoO0O00 - iI11I1II1I1I
 if 65 - 65: Ii + Iii
 if 44 - 44: i1iIi
 if 35 - 35: IIiIiII11i + IiI1i11I / Ii1I * oOo0O0Ooo . Iii
 if 97 - 97: oOo0O0Ooo / I11i
def O0OIIII1i ( title , message , times = 2000 , icon = O0O ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 13 - 13: Ii1I
def iI1I ( url ) :
 OOo000 = os . path . join ( oooOOOOO , 'addon_data' )
 iI1iIIiIi1I1 = [
 ( OOo000 ) ,
 ( oo0o0O00 ) ,
 ( os . path . join ( oOo0oooo00o , 'cache' ) ) ,
 ( os . path . join ( oOo0oooo00o , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oo0o0O00 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oo0o0O00 , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( OOo000 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OOo000 , 'plugin.video.itv' , 'Images' ) ) ]
 if 85 - 85: oO0o + IIiIiII11i
 o0oo0oO = 0
 if 3 - 3: Ii / oooOo0oo0oo + i1i1I1IIii1II
 for iII1i11 in iI1iIIiIi1I1 :
  if os . path . exists ( iII1i11 ) and not iII1i11 in [ oo0o0O00 , OOo000 ] :
   for OO0ii1 , III11iIIi , iIIi in os . walk ( iII1i11 ) :
    II1iIIiIIi = 0
    II1iIIiIIi += len ( iIIi )
    if II1iIIiIIi > 0 :
     for IiII111i1i11 in iIIi :
      if not IiII111i1i11 in i1iiIII111ii :
       try :
        os . unlink ( os . path . join ( OO0ii1 , IiII111i1i11 ) )
       except :
        pass
      else : ooOoO00 ( 'Ignore Log File: %s' % IiII111i1i11 )
     for o0Oo in III11iIIi :
      try :
       shutil . rmtree ( os . path . join ( OO0ii1 , o0Oo ) )
       o0oo0oO += 1
       ooOoO00 ( "[Success] cleared %s files from %s" % ( str ( II1iIIiIIi ) , os . path . join ( iII1i11 , o0Oo ) ) )
      except :
       ooOoO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , o0Oo ) )
  else :
   for OO0ii1 , III11iIIi , iIIi in os . walk ( iII1i11 ) :
    for o0Oo in III11iIIi :
     if 'cache' in o0Oo . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( OO0ii1 , o0Oo ) )
       o0oo0oO += 1
       ooOoO00 ( "[Success] wiped %s " % os . path . join ( iII1i11 , o0Oo ) )
      except :
       ooOoO00 ( "[Failed] to wipe cache in: %s" % os . path . join ( iII1i11 , o0Oo ) )
       if 10 - 10: oO0o . oO0o + o0o00Oo0O
 O0OIIII1i ( i1iiIIiiI111 , 'Clear Cache: Removed %s Files' % o0oo0oO )
 if 13 - 13: ooOoO0O00 . oOo0O0Ooo
 if 45 - 45: i1iIi % Iii
 if 37 - 37: IiI1i11I
 if 70 - 70: o0o00Oo0O + iI11I1II1I1I % o0o00Oo0O * I11i - I1ii11iIi11i - i1iIi
 if 94 - 94: ooOoO0O00 + III1iiIii / ii - i1i1I1IIii1II / oooOo0oo0oo / OOooOOo
 if 55 - 55: oooOo0oo0oo
 if 5 - 5: Iii / OOooOOo
def Iii1IiI1iI1I ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IiiIIiII = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OO0ii1 , III11iIIi , iIIi in os . walk ( IiiIIiII ) :
   II1iIIiIIi = 0
   II1iIIiIIi += len ( iIIi )
   if 25 - 25: oooOo0oo0oo % i1i1I1IIii1II
   if 48 - 48: Ii1I . IIiIiII11i * III1iiIii . oOo0O0Ooo * o0ii1I
   if II1iIIiIIi > 0 :
    if 82 - 82: OOooOOo * Ii1I - ii / ooOoO0O00 + ii * Iii
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( II1iIIiIIi ) + " files found" , "Do you want to delete them?" ) :
     if 87 - 87: ooOoO0O00 . Ii1I / i1iIi / o0o00Oo0O
     for IiII111i1i11 in iIIi :
      os . unlink ( os . path . join ( OO0ii1 , IiII111i1i11 ) )
     for o0Oo in III11iIIi :
      shutil . rmtree ( os . path . join ( OO0ii1 , o0Oo ) )
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
 if 62 - 62: I11i % IIiIiII11i
 if 22 - 22: i1i1I1IIii1II - I11i
 if 89 - 89: oooOo0oo0oo
 if 34 - 34: IiI1i11I . oooOo0oo0oo
 if 13 - 13: oO0o * oooOo0oo0oo + i1i1I1IIii1II
 if 21 - 21: Ii . o0ii1I % ooOoO0O00 * o0ii1I . i1i1I1IIii1II + o0ii1I
 if 92 - 92: ooOoO0O00 + oO0o * Iii
 if 70 - 70: I1ii11iIi11i
 if 93 - 93: IiI1i11I . Ii1I . I1ii11iIi11i . i1i1I1IIii1II . ii
def o00O0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IiiIIiII = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OO0ii1 , III11iIIi , iIIi in os . walk ( IiiIIiII ) :
   II1iIIiIIi = 0
   II1iIIiIIi += len ( iIIi )
   if 51 - 51: o0o00Oo0O - IiI1i11I
   if 65 - 65: o0o00Oo0O / IIiIiII11i * III1iiIii % o0ii1I + I11i
   if II1iIIiIIi > 0 :
    if 43 - 43: i1IiiiI1iI + oO0o * ii
    iIii1 = xbmcgui . Dialog ( )
    if iIii1 . yesno ( "Delete Package Cache Files" , str ( II1iIIiIIi ) + " files found" , "Do you want to delete them?" ) :
     if 85 - 85: IiI1i11I + oooOo0oo0oo
     for IiII111i1i11 in iIIi :
      os . unlink ( os . path . join ( OO0ii1 , IiII111i1i11 ) )
     for o0Oo in III11iIIi :
      shutil . rmtree ( os . path . join ( OO0ii1 , o0Oo ) )
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
 iI1I ( url )
 return
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
def oOOo0OO0oo ( url , name ) :
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOO0o0ooO0 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
 iIii1 = xbmcgui . Dialog ( )
 i1ioooo00 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml.bak' )
 if os . path . exists ( i1ioooo00 ) == False :
  if iIii1 . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OOO0o0ooO0 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
   try :
    os . remove ( OOO0o0ooO0 )
    print '=== GenieTv - REMOVING    ' + str ( OOO0o0ooO0 ) + '    ==='
   except :
    pass
   iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
   IiIi1II111I = open ( OOO0o0ooO0 , "w" )
   IiIi1II111I . write ( iiI111I1iIiI )
   IiIi1II111I . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OOO0o0ooO0 ) + '    ==='
   iIii1 = xbmcgui . Dialog ( )
   iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OOO0o0ooO0 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
  try :
   os . remove ( OOO0o0ooO0 )
   print '=== GenieTv - REMOVING    ' + str ( OOO0o0ooO0 ) + '    ==='
  except :
   pass
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  IiIi1II111I = open ( OOO0o0ooO0 , "w" )
  IiIi1II111I . write ( iiI111I1iIiI )
  IiIi1II111I . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOO0o0ooO0 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 69 - 69: OOooOOo / i1IiiiI1iI * oOo0O0Ooo
def oo0oOoo ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOO0o0ooO0 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
 try :
  IiIi1II111I = open ( OOO0o0ooO0 ) . read ( )
  if 'zero' in IiIi1II111I :
   name = '0CACHE'
  elif 'tuxen' in IiIi1II111I :
   name = 'TUXENS'
  elif 'muckys' in IiIi1II111I :
   name = 'MUCKYS'
  elif 'p2p1' in IiIi1II111I :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in IiIi1II111I :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in IiIi1II111I :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 iIii1 = xbmcgui . Dialog ( )
 iIii1 . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 53 - 53: oO0o % iI11I1II1I1I - oooOo0oo0oo
def iii11i ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOO0o0ooO0 = os . path . join ( OO0OoOO0o0o , 'advancedsettings.xml' )
 try :
  os . remove ( OOO0o0ooO0 )
  iIii1 = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OOO0o0ooO0 ) + '    ==='
  iIii1 . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 77 - 77: IIiIiII11i + IiI1i11I . I11i / i1IiiiI1iI
 if 100 - 100: o0ii1I
 if 84 - 84: Iii * i1iIi + Ii + IiI1i11I - IIiIiII11i
 if 92 - 92: ii + oOo0O0Ooo % i1i1I1IIii1II . I11i
 if 4 - 4: Iii * oooOo0oo0oo / o0ii1I . i1i1I1IIii1II
 if 83 - 83: IiI1i11I + Ii1I % OOooOOo
 if 85 - 85: IIiIiII11i . I1ii11iIi11i / IIiIiII11i
 if 2 - 2: ooOoO0O00 . o0ii1I
 if 38 - 38: I11i / Ii1I * i1i1I1IIii1II + IIiIiII11i / Ii
 if 34 - 34: Ii % oO0o - i1i1I1IIii1II / oooOo0oo0oo / IiI1i11I
def Iiii ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIi = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( OOooO0OOoo . http_GET ( url ) . content )
 for Ii11iIII , i1Io0ooo , iIIIII1iiI , iIiiI11iI111 in IIi :
  if inc < 2 : iIii1 = xbmcgui . Dialog ( ) ; iIii1 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % Ii11iIII , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iIIIII1iiI , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iIiiI11iI111 )
  inc = inc + 1
  if 28 - 28: i1i1I1IIii1II . i1iIi / Iii + I1ii11iIi11i
  if 55 - 55: ii % OOooOOo + ooOoO0O00 * oO0o * oooOo0oo0oo
  if 39 - 39: oooOo0oo0oo - i1i1I1IIii1II
  if 69 - 69: I11i * o0ii1I * OOooOOo
  if 51 - 51: I1ii11iIi11i . I1ii11iIi11i
  if 34 - 34: Ii1I - Ii
  if 43 - 43: iI11I1II1I1I
  if 73 - 73: OOooOOo + I11i
  if 58 - 58: ooOoO0O00 * Ii1I % IiI1i11I . oO0o % III1iiIii % Iii
def oO00O0o0Oo ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOO0o0ooO0 = os . path . join ( OO0OoOO0o0o , 'addons2.ini' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  IiIi1II111I = open ( OOO0o0ooO0 , "w" )
  IiIi1II111I . write ( iiI111I1iIiI )
  IiIi1II111I . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOO0o0ooO0 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 21 - 21: III1iiIii * i1i1I1IIii1II - OOooOOo . ooOoO0O00
def oOI11Ii1 ( url , name ) :
 iIii1 = xbmcgui . Dialog ( )
 if iIii1 . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  OO0OoOO0o0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOO0o0ooO0 = os . path . join ( OO0OoOO0o0o , 'settings.xml' )
  iiI111I1iIiI = OOooO0OOoo . http_GET ( url ) . content
  IiIi1II111I = open ( OOO0o0ooO0 , "w" )
  IiIi1II111I . write ( iiI111I1iIiI )
  IiIi1II111I . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOO0o0ooO0 ) + '    ==='
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 22 - 22: oO0o - I11i
 if 87 - 87: I1ii11iIi11i % Ii1I . ii % o0ii1I * i1i1I1IIii1II - oOo0O0Ooo
def IiI1III1 ( ) :
 try :
  oOO0O00ooOo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( oOO0O00ooOo ) == True :
   iIii1 = xbmcgui . Dialog ( )
   if iIii1 . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    iIIii1I1 = os . path . join ( oOO0O00ooOo , "source.db" )
    os . unlink ( iIIii1I1 )
  iIii1 . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  iIii1 = xbmcgui . Dialog ( )
  iIii1 . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 67 - 67: Ii + Ii % OOooOOo + i1i1I1IIii1II
 if 87 - 87: i1iIi * I1ii11iIi11i / IiI1i11I + Iii + o0ii1I
 if 84 - 84: iI11I1II1I1I * i1i1I1IIii1II / o0ii1I % oO0o
 if 91 - 91: I11i - oooOo0oo0oo - Iii
 if 52 - 52: Ii / I11i + i1iIi / oOo0O0Ooo / OOooOOo
def OooOoooOo ( url ) :
 i1Oo00 = urllib2 . Request ( url )
 i1Oo00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1i = urllib2 . urlopen ( i1Oo00 )
 iiI111I1iIiI = i1i . read ( )
 i1i . close ( )
 return iiI111I1iIiI
 if 6 - 6: ii . i1i1I1IIii1II / Ii / i1iIi + i1i1I1IIii1II . I1ii11iIi11i
 if 94 - 94: Ii . III1iiIii - oO0o + o0o00Oo0O
 if 89 - 89: IiI1i11I * i1i1I1IIii1II
 if 36 - 36: i1iIi / IIiIiII11i - i1iIi * IiI1i11I
 if 43 - 43: IiI1i11I * ooOoO0O00 . oOo0O0Ooo . OOooOOo / III1iiIii - I1ii11iIi11i
 if 95 - 95: ii % oooOo0oo0oo * oooOo0oo0oo
 if 24 - 24: o0ii1I * Ii / o0o00Oo0O - Ii1I
def o0OoOO ( params ) :
 pluginlog ( "freshstart.main_list " + repr ( params ) ) ; O0ooo00oO = pluginmessage_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if O0ooo00oO :
  O0oOooOO = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; O0oOooOO = xbmc . translatePath ( O0oOooOO ) ;
  i1IOO00OOOO00oOO = os . path . join ( O0oOooOO , ".." , ".." ) ; i1IOO00OOOO00oOO = os . path . abspath ( i1IOO00OOOO00oOO ) ; pluginlog ( "freshstart.main_list xbmcPath=" + i1IOO00OOOO00oOO ) ; O0o0ooO0oO0oO = False
  try :
   for OO0ii1 , III11iIIi , iIIi in os . walk ( i1IOO00OOOO00oOO , topdown = True ) :
    III11iIIi [ : ] = [ o0Oo for o0Oo in III11iIIi if o0Oo not in o0oO0 ]
    for OOoO in iIIi :
     try : os . remove ( os . path . join ( OO0ii1 , OOoO ) )
     except :
      if OOoO not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O0o0ooO0oO0oO = True
      pluginlog ( "Error removing " + OO0ii1 + " " + OOoO )
    for OOoO in III11iIIi :
     try : os . rmdir ( os . path . join ( OO0ii1 , OOoO ) )
     except :
      if OOoO not in [ "Database" , "userdata" ] : O0o0ooO0oO0oO = True
      pluginlog ( "Error removing " + OO0ii1 + " " + OOoO )
   if not O0o0ooO0oO0oO : pluginlog ( "freshstart.main_list All user files removed, you now have a clean install" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : pluginlog ( "freshstart.main_list User files partially removed" ) ; pluginmessage ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : pluginmessage ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; pluginlog ( traceback . format_exc ( ) ) ; pluginlog ( "freshstart.main_list NOT removed" )
  pluginadd_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : pluginmessage ( i1 , "Your settings" , "has not been changed" ) ; pluginadd_item ( action = "" , title = "Done" , folder = False )
 Oooo ( )
 if 45 - 45: i1iIi
 if 60 - 60: oO0o . i1iIi - o0ii1I * ii . i1iIi
 if 64 - 64: Ii1I % I1ii11iIi11i - iI11I1II1I1I % oO0o * iI11I1II1I1I + Iii
def oo000o00o0o00 ( ) :
 I1iiII1i1 = [ ]
 ooOoooo0o = sys . argv [ 2 ]
 if len ( ooOoooo0o ) >= 2 :
  O0O0Oo00 = sys . argv [ 2 ]
  i1i11i = O0O0Oo00 . replace ( '?' , '' )
  if ( O0O0Oo00 [ len ( O0O0Oo00 ) - 1 ] == '/' ) :
   O0O0Oo00 = O0O0Oo00 [ 0 : len ( O0O0Oo00 ) - 2 ]
  iiIoOOOOoo0O00o = i1i11i . split ( '&' )
  I1iiII1i1 = { }
  for o0OoOOoooooOO in range ( len ( iiIoOOOOoo0O00o ) ) :
   i11i11Ii1i11 = { }
   i11i11Ii1i11 = iiIoOOOOoo0O00o [ o0OoOOoooooOO ] . split ( '=' )
   if ( len ( i11i11Ii1i11 ) ) == 2 :
    I1iiII1i1 [ i11i11Ii1i11 [ 0 ] ] = i11i11Ii1i11 [ 1 ]
    if 78 - 78: I11i / ii + ooOoO0O00 * OOooOOo . ooOoO0O00 / IIiIiII11i
 return I1iiII1i1
 if 37 - 37: o0o00Oo0O % IIiIiII11i % IiI1i11I
i1III = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
iII1I1i = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
IiiiI1I1IIIi = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
iiiiiIIii11I = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i111I1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
I1iiiiii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
oOIIIiIII111iii = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i1i1iIi1I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
o00OO0Oo0Oo = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
Ii11I111Ii = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
IiiIiIIII = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
O00oo0Ooo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
ooOO = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
oOooOO0 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
IiIIiI1i1IIiI = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
IiiOOo0ooO000o = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OOoO0oooO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iIiII = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOOOo0oO0o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
IiII1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iI1111i1i11Ii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iii11I1i11IIIi = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I11iii = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
Oo0o0OoOoOo0 = base64 . decodestring ( 'Q1VOVA==' )
def o00OoO0o0oOo ( name , url , mode , iconimage , fanart , description , year , cast , rating , runtime , genre ) :
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Rating" : rating , "Year" : year , "Duration" : runtime , "Cast" : cast , "Genre" : genre } )
 I1iiii . setProperty ( 'fanart_image' , fanart )
 I1iiii . setProperty ( "IsPlayable" , "true" )
 IIi1i1i1iii = [ ]
 IIi1i1i1iii . append ( ( 'Play Trailer' , 'XBMC.RunPlugin(plugin://plugin.video.rootIPTV/?mode=9&url=' + str ( name ) + ')' ) )
 IIi1i1i1iii . append ( ( 'Movie Information' , 'XBMC.Action(Info)' ) )
 I1iiii . addContextMenuItems ( IIi1i1i1iii , replaceItems = True )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = False )
 return ii1II
def Iii1I1I11iiI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oooooOo0 = [ ]
  if showcontext == 'fav' :
   oooooOo0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oooooOo0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  I1iiii . addContextMenuItems ( oooooOo0 )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = True )
 return ii1II
 if 6 - 6: oOo0O0Ooo + i1IiiiI1iI - Ii * IiI1i11I / Iii / o0o00Oo0O
def iI1Ii1iI11iiI ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oOoOoo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1II = True
 I1iiii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1iiii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 I1iiii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  oooooOo0 = [ ]
  if showcontext == 'fav' :
   oooooOo0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOoOO0oo0ooO :
   oooooOo0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  I1iiii . addContextMenuItems ( oooooOo0 )
 ii1II = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOoo0 , listitem = I1iiii , isFolder = False )
 return ii1II
 if 79 - 79: oO0o
 if 4 - 4: Iii / Ii1I
O0O0Oo00 = oo000o00o0o00 ( )
O0O00Oo = None
OOoO = None
oO0oOOoo00000 = None
oo00O00oO000o = None
oooOo0OOOoo0 = None
I1iIII1 = None
I1i1ii = None
ii1iIiIIiIIii = None
if 76 - 76: ooOoO0O00 / iI11I1II1I1I
if 23 - 23: I1ii11iIi11i / i1iIi
try :
 ii1iIiIIiIIii = int ( O0O0Oo00 [ "fav_mode" ] )
except :
 pass
 if 80 - 80: Iii
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
 oO0oOOoo00000 = int ( O0O0Oo00 [ "mode" ] )
except :
 pass
try :
 oooOo0OOOoo0 = urllib . unquote_plus ( O0O0Oo00 [ "fanart" ] )
except :
 pass
try :
 I1iIII1 = urllib . unquote_plus ( O0O0Oo00 [ "description" ] )
except :
 pass
 if 26 - 26: IIiIiII11i + oOo0O0Ooo . IIiIiII11i - i1i1I1IIii1II % oO0o
 if 1 - 1: oO0o - IIiIiII11i
print str ( I11II1i ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( oO0oOOoo00000 )
print "URL: " + str ( O0O00Oo )
print "Name: " + str ( OOoO )
print "IconImage: " + str ( oo00O00oO000o )
if 75 - 75: I1ii11iIi11i - OOooOOo + i1i1I1IIii1II % ooOoO0O00 * oooOo0oo0oo
if 56 - 56: OOooOOo / oO0o / oOo0O0Ooo % ii
def oOI1Ii1I1 ( content , viewType ) :
 if 39 - 39: oOo0O0Ooo + IIiIiII11i * I1ii11iIi11i % o0ii1I . I11i * i1i1I1IIii1II
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 42 - 42: o0ii1I / I1ii11iIi11i
if oo00O00oO000o == None : oo00O00oO000o = O0O
if oooOo0OOOoo0 == None : oooOo0OOOoo0 = Oo00OOOOO
if oO0oOOoo00000 == None :
 I1IiiiiI ( )
 if 25 - 25: ii % o0ii1I * i1IiiiI1iI * Iii + oOo0O0Ooo % Ii1I
elif oO0oOOoo00000 == 1 :
 oOoO ( O0O00Oo )
 if 70 - 70: o0ii1I + Ii1I * Iii * ooOoO0O00 . i1IiiiI1iI
elif oO0oOOoo00000 == 44 :
 oOoO00o ( O0O00Oo )
 if 76 - 76: ii * OOooOOo . ii
elif oO0oOOoo00000 == 2 :
 iI1oOoo ( )
 if 46 - 46: i1iIi * I11i % IIiIiII11i / i1IiiiI1iI
elif oO0oOOoo00000 == 3 :
 iI1iIIII1 ( )
 if 29 - 29: oO0o - Ii % I1ii11iIi11i % I11i
elif oO0oOOoo00000 == 21 :
 i1i1II ( )
 if 30 - 30: i1i1I1IIii1II - o0ii1I % o0ii1I
elif oO0oOOoo00000 == 4 :
 OOoO0o0O0 ( )
 if 8 - 8: III1iiIii
elif oO0oOOoo00000 == 5 :
 Oo00o ( O0O00Oo )
 if 68 - 68: III1iiIii . ii - Ii + Ii
elif oO0oOOoo00000 == 6 :
 Iii1IiI1iI1I ( O0O00Oo )
 if 81 - 81: OOooOOo + IiI1i11I . Ii
elif oO0oOOoo00000 == 7 :
 oOOo0OO0oo ( O0O00Oo , OOoO )
 if 10 - 10: OOooOOo + Iii - iI11I1II1I1I - Iii
elif oO0oOOoo00000 == 8 :
 oo0oOoo ( O0O00Oo , OOoO )
 if 58 - 58: i1iIi
elif oO0oOOoo00000 == 9 :
 FIXREPOSADDONS ( O0O00Oo )
 if 98 - 98: o0ii1I / oO0o % ii
elif oO0oOOoo00000 == 10 :
 ii1iii1i ( )
 if 65 - 65: i1iIi % I1ii11iIi11i - oOo0O0Ooo % i1IiiiI1iI + iI11I1II1I1I / iI11I1II1I1I
elif oO0oOOoo00000 == 11 :
 iii11i ( O0O00Oo )
 if 94 - 94: III1iiIii - I1ii11iIi11i . I11i - i1iIi - i1i1I1IIii1II . Iii
elif oO0oOOoo00000 == 12 :
 Iiii ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 39 - 39: i1i1I1IIii1II + OOooOOo
elif oO0oOOoo00000 == 13 :
 oOii11I ( )
 if 68 - 68: ooOoO0O00 * i1i1I1IIii1II / Ii
elif oO0oOOoo00000 == 14 :
 iI1I ( O0O00Oo )
 if 96 - 96: oOo0O0Ooo
elif oO0oOOoo00000 == 15 :
 o00o0O0 ( )
 if 78 - 78: oO0o
elif oO0oOOoo00000 == 16 :
 oO00O0o0Oo ( O0O00Oo , OOoO )
 if 72 - 72: Ii1I / o0o00Oo0O % IIiIiII11i / IIiIiII11i
elif oO0oOOoo00000 == 17 :
 oOI11Ii1 ( O0O00Oo , OOoO )
 if 48 - 48: oooOo0oo0oo % oooOo0oo0oo / iI11I1II1I1I - Ii
elif oO0oOOoo00000 == 18 :
 IiI1III1 ( )
 if 57 - 57: Iii / III1iiIii * ooOoO0O00 + IIiIiII11i . I11i
elif oO0oOOoo00000 == 19 :
 OoOiII11IiIi ( O0O00Oo )
 if 11 - 11: IIiIiII11i
elif oO0oOOoo00000 == 40 :
 oO0OO ( OOoO , O0O00Oo , I1iIII1 )
 if 66 - 66: o0ii1I - oOo0O0Ooo . ii * i1IiiiI1iI
elif oO0oOOoo00000 == 42 :
 Ii1 ( OOoO , O0O00Oo , I1iIII1 )
 if 16 - 16: III1iiIii * oO0o * Ii - i1iIi
elif oO0oOOoo00000 == 43 :
 IIIii ( O0O00Oo )
 if 88 - 88: iI11I1II1I1I / o0ii1I * III1iiIii / i1IiiiI1iI
elif oO0oOOoo00000 == 20 :
 oOiI1I ( O0O00Oo )
 if 31 - 31: o0o00Oo0O . oOo0O0Ooo
elif oO0oOOoo00000 == 22 :
 IIIi1I1 ( O0O00Oo )
 if 8 - 8: OOooOOo
elif oO0oOOoo00000 == 23 :
 iIi1I111Ii1I1 ( O0O00Oo )
 if 99 - 99: IiI1i11I
elif oO0oOOoo00000 == 24 :
 oo0Oo0oo000 ( O0O00Oo )
 if 93 - 93: i1IiiiI1iI
elif oO0oOOoo00000 == 25 :
 OOOOo00o0 ( O0O00Oo )
 if 39 - 39: o0ii1I
elif oO0oOOoo00000 == 26 :
 O0IiIi1IIiII1i ( O0O00Oo )
 if 10 - 10: OOooOOo . iI11I1II1I1I / Ii1I % IiI1i11I / Ii
elif oO0oOOoo00000 == 27 :
 ooOOOo ( O0O00Oo )
 if 14 - 14: Ii % I11i * o0o00Oo0O % iI11I1II1I1I . III1iiIii - IIiIiII11i
elif oO0oOOoo00000 == 28 :
 OooOooooo ( O0O00Oo )
 if 14 - 14: o0ii1I % i1iIi - OOooOOo
elif oO0oOOoo00000 == 29 :
 O0Oo0O0O0000 ( O0O00Oo )
 if 52 - 52: oO0o / ooOoO0O00 - o0ii1I
elif oO0oOOoo00000 == 30 :
 O0oo0000o ( O0O00Oo )
 if 8 - 8: i1i1I1IIii1II + i1iIi . Ii1I . ooOoO0O00 / oOo0O0Ooo . III1iiIii
elif oO0oOOoo00000 == 31 :
 oOooo0o ( O0O00Oo )
 if 8 - 8: ooOoO0O00 * o0o00Oo0O
elif oO0oOOoo00000 == 32 :
 i1I1i ( )
 if 60 - 60: I1ii11iIi11i - IIiIiII11i + oOo0O0Ooo
elif oO0oOOoo00000 == 33 :
 iiIiiII1II1ii ( )
 if 17 - 17: OOooOOo % oOo0O0Ooo
elif oO0oOOoo00000 == 35 :
 iIII1IiI ( O0O00Oo )
 if 8 - 8: I1ii11iIi11i
elif oO0oOOoo00000 == 34 :
 i1iI1iiI ( O0O00Oo )
 if 49 - 49: OOooOOo * Iii - I11i / oO0o * i1i1I1IIii1II
elif oO0oOOoo00000 == 36 :
 IIi11I1i1I1I ( O0O00Oo )
 if 51 - 51: i1iIi - iI11I1II1I1I . Iii * OOooOOo + i1IiiiI1iI * ooOoO0O00
elif oO0oOOoo00000 == 37 :
 OOoo0OOOo0o ( O0O00Oo )
 if 37 - 37: III1iiIii * i1i1I1IIii1II / ii . oO0o
elif oO0oOOoo00000 == 38 :
 I11i1I1Ii ( O0O00Oo )
 if 77 - 77: IIiIiII11i + OOooOOo * oooOo0oo0oo
elif oO0oOOoo00000 == 41 :
 o0OoOO ( O0O0Oo00 )
 if 9 - 9: IIiIiII11i - Ii * I11i % oO0o * Ii / Iii
elif oO0oOOoo00000 == 39 :
 oOOoo00O00o ( O0O00Oo )
 if 45 - 45: Ii * IiI1i11I - Ii1I + i1iIi % IiI1i11I
elif oO0oOOoo00000 == 45 :
 TEXTS ( )
 if 11 - 11: iI11I1II1I1I
elif oO0oOOoo00000 == 46 :
 oooooo0O000o ( )
 if 48 - 48: iI11I1II1I1I - I1ii11iIi11i
elif oO0oOOoo00000 == 47 :
 GEVID ( )
 if 80 - 80: ooOoO0O00
elif oO0oOOoo00000 == 48 :
 I1I11 ( OOoO , O0O00Oo , I1iIII1 )
 if 56 - 56: IIiIiII11i - I11i
elif oO0oOOoo00000 == 49 :
 I1ii1ii11i1I ( )
 if 48 - 48: I1ii11iIi11i - Ii1I - IIiIiII11i . o0ii1I . i1i1I1IIii1II / iI11I1II1I1I
elif oO0oOOoo00000 == 22222 :
 ii1O0ooooo000 ( O0O00Oo )
 if 38 - 38: i1IiiiI1iI % Ii + o0ii1I * i1iIi / i1IiiiI1iI
elif oO0oOOoo00000 == 222 :
 II11I11I ( O0O00Oo )
 if 93 - 93: i1i1I1IIii1II
elif oO0oOOoo00000 == 2222222 :
 OooO0OO ( O0O00Oo )
 if 60 - 60: i1IiiiI1iI . i1i1I1IIii1II / I1ii11iIi11i * i1iIi + OOooOOo - ooOoO0O00
elif oO0oOOoo00000 == 222222 :
 o0Oo00oooOO ( O0O00Oo , OOoO )
 if 13 - 13: Ii * i1i1I1IIii1II / Iii * oOo0O0Ooo
elif oO0oOOoo00000 == 333 :
 iiii111iI ( O0O00Oo )
 if 31 - 31: iI11I1II1I1I * o0ii1I % oooOo0oo0oo . IIiIiII11i
 if 56 - 56: III1iiIii / Ii . I11i . i1i1I1IIii1II - Ii
elif oO0oOOoo00000 == 1020 :
 Oo000o0o0 ( )
 if 23 - 23: Ii1I * Ii % i1iIi
elif oO0oOOoo00000 == 1021 :
 ANIMEEP ( )
 if 47 - 47: iI11I1II1I1I . oooOo0oo0oo / Iii % IIiIiII11i
elif oO0oOOoo00000 == 1022 :
 ANIMEPLAY ( O0O00Oo )
 if 92 - 92: Ii1I % Ii
elif oO0oOOoo00000 == 1001 :
 o0OO0O0oo ( )
 if 82 - 82: i1IiiiI1iI * Ii1I % o0ii1I / I11i
elif oO0oOOoo00000 == 1005 :
 i1iIiII1iI ( )
 if 28 - 28: IiI1i11I % oO0o - oooOo0oo0oo - I1ii11iIi11i
elif oO0oOOoo00000 == 1007 :
 oOoO0OoOo0O000 ( O0O00Oo )
 if 16 - 16: Ii - Ii . OOooOOo / ooOoO0O00
elif oO0oOOoo00000 == 1010 :
 i1I1ii1i ( O0O00Oo )
 if 76 - 76: o0o00Oo0O * oO0o / o0o00Oo0O
elif oO0oOOoo00000 == 1011 :
 iio0O0OOo ( O0O00Oo )
 if 23 - 23: Ii1I . iI11I1II1I1I - Ii / IIiIiII11i
elif oO0oOOoo00000 == 1012 :
 II11 ( O0O00Oo )
 if 48 - 48: i1i1I1IIii1II - IIiIiII11i * oOo0O0Ooo
elif oO0oOOoo00000 == 1030 :
 ii1IiiiI1I ( )
 if 78 - 78: oOo0O0Ooo * Ii * IIiIiII11i
elif oO0oOOoo00000 == 1031 :
 i1iiOOOO0oo0o0O ( O0O00Oo , oo00O00oO000o )
 if 19 - 19: ii * Ii / o0o00Oo0O . oOo0O0Ooo % Iii
elif oO0oOOoo00000 == 1032 :
 iII1i1ii ( O0O00Oo )
 if 35 - 35: iI11I1II1I1I + oOo0O0Ooo - i1iIi / I1ii11iIi11i * Ii1I * I1ii11iIi11i
elif oO0oOOoo00000 == 1006 :
 Parse . ParseURL ( O0O00Oo )
 if 17 - 17: OOooOOo
elif oO0oOOoo00000 == 2030 :
 Parse . addonParseURL ( O0O00Oo )
 if 24 - 24: iI11I1II1I1I / oooOo0oo0oo % ii / o0o00Oo0O / i1i1I1IIii1II
elif oO0oOOoo00000 == 2031 :
 Parse . apkParseURL ( O0O00Oo )
 if 93 - 93: I1ii11iIi11i
elif oO0oOOoo00000 == 2032 :
 Parse . ParseBOSS ( O0O00Oo )
 if 5 - 5: IiI1i11I
elif oO0oOOoo00000 == 1002 :
 i11II1iIi1Ii ( O0O00Oo )
 if 61 - 61: oooOo0oo0oo * oO0o - o0o00Oo0O
elif oO0oOOoo00000 == 1003 :
 o0o0oo0oO ( O0O00Oo , oo00O00oO000o )
 if 30 - 30: iI11I1II1I1I
elif oO0oOOoo00000 == 1004 :
 iII1IiI1I11i ( O0O00Oo )
 if 14 - 14: I11i + o0ii1I
elif oO0oOOoo00000 == 1008 :
 ii1IiiIIiIiii ( )
 if 91 - 91: ii / i1i1I1IIii1II + OOooOOo
elif oO0oOOoo00000 == 1009 :
 iI1i1IIi1i1 ( O0O00Oo )
 if 100 - 100: ooOoO0O00
elif oO0oOOoo00000 == 2001 :
 OoOOOoo ( )
 if 13 - 13: ooOoO0O00 . Ii1I * I11i
elif oO0oOOoo00000 == 2002 :
 OOoO0 ( O0O00Oo )
 if 31 - 31: Ii % oO0o . Ii % i1i1I1IIii1II - ooOoO0O00
elif oO0oOOoo00000 == 1013 :
 O0o0o ( )
elif oO0oOOoo00000 == 10111113 :
 Iii1I11 ( O0O00Oo )
 if 62 - 62: i1i1I1IIii1II + i1i1I1IIii1II . ii
elif oO0oOOoo00000 == 1014 :
 O000OO0O ( )
 if 59 - 59: iI11I1II1I1I . I1ii11iIi11i * Iii
elif oO0oOOoo00000 == 1015 :
 iiIi11I1 ( O0O00Oo )
 if 29 - 29: I1ii11iIi11i - oOo0O0Ooo * Iii
elif oO0oOOoo00000 == 1016 :
 i1i1I111iIi1 ( O0O00Oo , oo00O00oO000o , OOoO )
 if 58 - 58: ooOoO0O00 * o0ii1I / i1iIi % iI11I1II1I1I
elif oO0oOOoo00000 == 1017 :
 oOooO0 ( )
 if 24 - 24: OOooOOo - I11i * oOo0O0Ooo . Iii / oO0o * o0ii1I
elif oO0oOOoo00000 == 1018 :
 o00oO ( O0O00Oo )
 if 12 - 12: ii % i1i1I1IIii1II
elif oO0oOOoo00000 == 1019 :
 i1oO0OO0 ( O0O00Oo )
elif oO0oOOoo00000 == 10190 :
 O0Oo0o000oO ( O0O00Oo )
 if 92 - 92: i1iIi % oO0o + o0o00Oo0O + OOooOOo / oO0o * iI11I1II1I1I
elif oO0oOOoo00000 == 1023 :
 iioOo00oooOO ( )
 if 79 - 79: o0o00Oo0O
elif oO0oOOoo00000 == 1024 :
 OO000OOO ( O0O00Oo )
 if 71 - 71: oO0o - o0o00Oo0O
elif oO0oOOoo00000 == 1025 :
 o000OOooo000O ( O0O00Oo )
 if 73 - 73: iI11I1II1I1I
elif oO0oOOoo00000 == 4001 :
 OoOooOoO ( )
 if 7 - 7: OOooOOo
elif oO0oOOoo00000 == 4002 :
 oOOo0OOOo00O ( )
 if 55 - 55: i1i1I1IIii1II . oO0o + iI11I1II1I1I + OOooOOo / Ii1I - o0o00Oo0O
elif oO0oOOoo00000 == 4003 :
 oO00oOoo00o0 ( )
 if 14 - 14: IIiIiII11i - oO0o - o0o00Oo0O * ii / oOo0O0Ooo
elif oO0oOOoo00000 == 4004 :
 ii1 ( )
 if 3 - 3: Iii
elif oO0oOOoo00000 == 4005 :
 IiIi1iIIi1 ( )
 if 46 - 46: Ii1I * i1IiiiI1iI - iI11I1II1I1I
elif oO0oOOoo00000 == 4006 :
 II1i ( )
 if 25 - 25: IIiIiII11i / oooOo0oo0oo + I1ii11iIi11i - iI11I1II1I1I - OOooOOo
elif oO0oOOoo00000 == 4007 :
 iiIi1i ( )
 if 97 - 97: oooOo0oo0oo . oooOo0oo0oo / Ii1I + oOo0O0Ooo * ooOoO0O00
elif oO0oOOoo00000 == 4008 :
 OOoOOO0 ( )
 if 53 - 53: o0o00Oo0O
elif oO0oOOoo00000 == 40099 : i1I11ii ( )
elif oO0oOOoo00000 == 4009 : ii1IiI11I ( )
elif oO0oOOoo00000 == 4010 : oO0OoiIi111iII1 ( )
elif oO0oOOoo00000 == 3000 :
 IIIII11IIi ( )
 if 28 - 28: IiI1i11I % oO0o . oO0o / III1iiIii * I1ii11iIi11i * IiI1i11I
elif oO0oOOoo00000 == 3001 :
 O00O0O0 ( )
 if 49 - 49: oOo0O0Ooo / i1IiiiI1iI * IiI1i11I + oOo0O0Ooo % i1i1I1IIii1II % i1iIi
elif oO0oOOoo00000 == 3002 :
 ii1IiIi1iIi ( O0O00Oo )
 if 27 - 27: oO0o / IiI1i11I . Ii1I
elif oO0oOOoo00000 == 3003 :
 IIiI111Iii ( O0O00Oo )
 if 71 - 71: oO0o . Ii . iI11I1II1I1I + oOo0O0Ooo - I11i
elif oO0oOOoo00000 == 3004 :
 ooo0oooO ( O0O00Oo )
 if 34 - 34: IiI1i11I
elif oO0oOOoo00000 == 404 :
 ooOooooO00 ( OOoO , O0O00Oo , oo00O00oO000o )
 if 6 - 6: oO0o . OOooOOo + Ii1I
elif oO0oOOoo00000 == 405 :
 i1IO0oO ( O0O00Oo )
 if 24 - 24: oO0o . o0ii1I
elif oO0oOOoo00000 == 7030 :
 IIoOOOO ( )
 if 26 - 26: o0o00Oo0O * oOo0O0Ooo - oooOo0oo0oo * ii * IIiIiII11i % OOooOOo
elif oO0oOOoo00000 == 7021 :
 iI1iIiiIii ( OOoO )
 if 56 - 56: oooOo0oo0oo * Ii % i1iIi * OOooOOo % I1ii11iIi11i * III1iiIii
elif oO0oOOoo00000 == 7022 :
 oOoo0O00OO ( OOoO )
 if 30 - 30: ooOoO0O00 + I11i - OOooOOo . oooOo0oo0oo
elif oO0oOOoo00000 == 7000 :
 O0oOoO0o0oO ( OOoO , O0O00Oo , img )
 if 95 - 95: ooOoO0O00 . Iii + o0o00Oo0O . Iii - Iii / I1ii11iIi11i
elif oO0oOOoo00000 == 7050 :
 IiiiIi1111I ( O0O00Oo )
 if 41 - 41: ii . oooOo0oo0oo - o0ii1I * oO0o % Ii
elif oO0oOOoo00000 == 7051 :
 IIIIII ( O0O00Oo )
 if 7 - 7: o0ii1I
elif oO0oOOoo00000 == 7052 :
 oO0ooOoOooO00o00 ( O0O00Oo )
 if 16 - 16: III1iiIii * I11i % IIiIiII11i - IIiIiII11i + i1iIi
elif oO0oOOoo00000 == 7053 :
 o0Ooo00Oo0oo0 ( O0O00Oo )
 if 55 - 55: oO0o % OOooOOo
elif oO0oOOoo00000 == 7054 :
 CoolPlay ( O0O00Oo )
 if 58 - 58: o0ii1I
elif oO0oOOoo00000 == 7060 :
 o00oO0 ( )
 if 17 - 17: oO0o - i1i1I1IIii1II % I1ii11iIi11i % i1i1I1IIii1II * i1IiiiI1iI / III1iiIii
elif oO0oOOoo00000 == 7061 :
 oO0OoO00o ( O0O00Oo )
 if 88 - 88: i1iIi . IIiIiII11i * o0o00Oo0O % III1iiIii
elif oO0oOOoo00000 == 7063 :
 IIIi111iii1iI ( O0O00Oo )
 if 15 - 15: o0o00Oo0O % ooOoO0O00 - oooOo0oo0oo . III1iiIii
elif oO0oOOoo00000 == 7062 :
 Iiii11i11IIi1 ( O0O00Oo )
 if 1 - 1: oOo0O0Ooo
elif oO0oOOoo00000 == 7064 :
 NATatozcat ( )
 if 40 - 40: I11i % Iii % o0o00Oo0O
elif oO0oOOoo00000 == 7067 :
 oOOooOo000O00O ( O0O00Oo )
 if 88 - 88: I11i - i1i1I1IIii1II
elif oO0oOOoo00000 == 7066 :
 NATatozA ( O0O00Oo )
 if 73 - 73: IIiIiII11i
elif oO0oOOoo00000 == 7065 :
 OooO ( O0O00Oo )
 if 7 - 7: o0o00Oo0O / oO0o
elif oO0oOOoo00000 == 7070 :
 II111iiI1Ii1 ( )
 if 90 - 90: IiI1i11I % i1i1I1IIii1II / iI11I1II1I1I
elif oO0oOOoo00000 == 7071 :
 DIZIlist ( O0O00Oo )
 if 52 - 52: oOo0O0Ooo / I11i
elif oO0oOOoo00000 == 7072 :
 DIZIpull ( O0O00Oo )
 if 20 - 20: i1IiiiI1iI . oOo0O0Ooo - iI11I1II1I1I / IiI1i11I
elif oO0oOOoo00000 == 7073 :
 WATCHDIZI ( O0O00Oo )
 if 46 - 46: i1IiiiI1iI . Ii
elif oO0oOOoo00000 == 7002 :
 iIiIi1I1iI ( )
 if 89 - 89: oO0o - oooOo0oo0oo - ooOoO0O00 - oO0o % iI11I1II1I1I
elif oO0oOOoo00000 == 7003 :
 I11I11III ( O0O00Oo )
 if 52 - 52: I11i * o0o00Oo0O + Ii1I
elif oO0oOOoo00000 == 7004 :
 ii1I11iIi ( O0O00Oo )
 if 83 - 83: Iii + oooOo0oo0oo - ii
elif oO0oOOoo00000 == 7020 :
 IIIiiI1I ( O0O00Oo )
 if 7 - 7: III1iiIii % i1iIi / ii / I11i + oO0o - oO0o
elif oO0oOOoo00000 == 7001 :
 I1IIIiIiIi ( )
 if 15 - 15: ooOoO0O00 + oooOo0oo0oo / o0ii1I
elif oO0oOOoo00000 == 7010 :
 iiOo000O00o0O ( O0O00Oo )
 if 51 - 51: oooOo0oo0oo + o0o00Oo0O
elif oO0oOOoo00000 == 7011 :
 IIiI1iIiii ( O0O00Oo )
 if 91 - 91: Ii + I11i % oO0o / i1i1I1IIii1II - ooOoO0O00
elif oO0oOOoo00000 == 7012 :
 I1111iI ( O0O00Oo )
 if 82 - 82: o0ii1I . ii + ii % oO0o % Ii1I
elif oO0oOOoo00000 == 7013 :
 cnfTVPlay2 ( O0O00Oo )
elif oO0oOOoo00000 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( O0O00Oo )
elif oO0oOOoo00000 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( O0O00Oo )
elif oO0oOOoo00000 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( OOoO , O0O00Oo , oo00O00oO000o )
elif oO0oOOoo00000 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif oO0oOOoo00000 == 7018 :
 oOOO ( )
elif oO0oOOoo00000 == 7019 :
 CNF_Studio_Indexer . List_Movies ( O0O00Oo )
elif oO0oOOoo00000 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( O0O00Oo )
elif oO0oOOoo00000 == 7024 :
 CNF_Studio_Indexer . Box_Office ( O0O00Oo )
 if 65 - 65: I1ii11iIi11i . Iii
elif oO0oOOoo00000 == 8000 :
 oO0OO00o ( )
elif oO0oOOoo00000 == 8001 :
 o00OooO ( )
elif oO0oOOoo00000 == 8002 :
 oOO0oOooooO ( )
elif oO0oOOoo00000 == 8003 :
 I111I1 ( )
elif oO0oOOoo00000 == 8004 :
 ooooOoooo ( )
elif oO0oOOoo00000 == 8005 :
 iII1ii11I1I ( )
elif oO0oOOoo00000 == 8006 :
 iii111 ( OOoO , O0O00Oo )
elif oO0oOOoo00000 == 8030 :
 iIii1ii ( O0O00Oo )
elif oO0oOOoo00000 == 8045 :
 I1i1 ( O0O00Oo )
elif oO0oOOoo00000 == 8046 :
 Ii1IiiII ( O0O00Oo )
elif oO0oOOoo00000 == 8047 :
 I111II1iIIII ( O0O00Oo )
elif oO0oOOoo00000 == 8048 :
 oooOO0 ( O0O00Oo )
elif oO0oOOoo00000 == 8049 :
 iiIi1iIiI ( O0O00Oo )
elif oO0oOOoo00000 == 804900 :
 IIi1iii ( O0O00Oo )
elif oO0oOOoo00000 == 8020 :
 o00oOoOo0 ( )
elif oO0oOOoo00000 == 8021 :
 IiiiiI ( O0O00Oo )
elif oO0oOOoo00000 == 8022 :
 I1I1i1iIi11i ( O0O00Oo )
elif oO0oOOoo00000 == 8023 :
 II1ii1ii ( O0O00Oo )
elif oO0oOOoo00000 == 8040 :
 I1I1i ( )
elif oO0oOOoo00000 == 8041 :
 oO0oo0 ( O0O00Oo )
elif oO0oOOoo00000 == 8042 :
 ooOO0O0O ( O0O00Oo )
elif oO0oOOoo00000 == 8043 :
 yt . PlayVideo ( O0O00Oo )
elif oO0oOOoo00000 == 8044 :
 IIIiIIIi111iI ( O0O00Oo )
elif oO0oOOoo00000 == 8060 :
 oOO ( )
elif oO0oOOoo00000 == 8061 :
 oo0OOo ( O0O00Oo )
elif oO0oOOoo00000 == 8064 :
 oo000ii ( )
elif oO0oOOoo00000 == 8065 :
 oOoO0O0o ( O0O00Oo )
elif oO0oOOoo00000 == 8070 :
 OoO00O00O0 ( )
elif oO0oOOoo00000 == 8071 :
 ooOo0o0o00 ( O0O00Oo )
elif oO0oOOoo00000 == 7080 :
 iIIi1Iii ( O0O00Oo )
elif oO0oOOoo00000 == 8090 :
 Oo0O0 ( )
elif oO0oOOoo00000 == 8091 :
 O0ooO00OO ( O0O00Oo )
elif oO0oOOoo00000 == 8092 :
 iiiiiiI ( O0O00Oo )
elif oO0oOOoo00000 == 8093 :
 IiI11I1I111 ( O0O00Oo )
elif oO0oOOoo00000 == 8081 :
 O0oOOoOOoOo ( )
elif oO0oOOoo00000 == 8062 :
 o0i111I ( O0O00Oo )
elif oO0oOOoo00000 == 8063 :
 O0oooo0O0Oo0O ( O0O00Oo )
elif oO0oOOoo00000 == 8050 :
 I1111III111ii ( )
elif oO0oOOoo00000 == 8051 :
 o0oO0oOooO ( O0O00Oo )
elif oO0oOOoo00000 == 8052 :
 oo00o00O0 ( O0O00Oo )
elif oO0oOOoo00000 == 8085 :
 o000iiI11i ( )
elif oO0oOOoo00000 == 8086 :
 OOo0iIiiI11II11 ( O0O00Oo )
elif oO0oOOoo00000 == 8087 :
 O0ooO0oO0 ( O0O00Oo )
elif oO0oOOoo00000 == 8088 :
 IiI11I11i ( O0O00Oo , OOoO )
elif oO0oOOoo00000 == 9000 :
 IIIii11 ( )
elif oO0oOOoo00000 == 1111 :
 iiiiII11iIi ( )
elif oO0oOOoo00000 == 9001 :
 I1IiiI1ii1i ( )
elif oO0oOOoo00000 == 9002 :
 O0OoO0ooOO0o ( )
elif oO0oOOoo00000 == 9003 :
 OoI11I ( )
elif oO0oOOoo00000 == 9004 :
 World1 ( )
elif oO0oOOoo00000 == 9005 :
 World2 ( O0O00Oo )
elif oO0oOOoo00000 == 9006 :
 World3 ( O0O00Oo )
elif oO0oOOoo00000 == 9007 :
 OooOooo00OOO0o ( )
elif oO0oOOoo00000 == 9008 :
 II1iIIiIII ( O0O00Oo )
elif oO0oOOoo00000 == 9009 :
 iI1i11i1i1i ( O0O00Oo )
elif oO0oOOoo00000 == 9010 :
 o0iiiii1i1 ( )
elif oO0oOOoo00000 == 9011 :
 IIII1I11Ii11 ( O0O00Oo )
elif oO0oOOoo00000 == 50 :
 oo0 ( O0O00Oo )
elif oO0oOOoo00000 == 9020 :
 champlist ( )
elif oO0oOOoo00000 == 9021 :
 OOoooiII1 ( )
elif oO0oOOoo00000 == 9022 :
 ii1i1iIiIIi ( )
elif oO0oOOoo00000 == 9023 :
 iI11I11i ( )
elif oO0oOOoo00000 == 9024 :
 Iiooo000o0OoOo ( O0O00Oo )
elif oO0oOOoo00000 == 9030 :
 OOOO0oooooO0o ( O0O00Oo )
elif oO0oOOoo00000 == 9031 :
 O00o00o0 ( O0O00Oo )
elif oO0oOOoo00000 == 9032 :
 o00OOOOoOO ( O0O00Oo )
elif oO0oOOoo00000 == 9033 :
 OooOoOoo0ooo0 ( O0O00Oo )
elif oO0oOOoo00000 == 9034 :
 iiOOO0oOOoo ( )
elif oO0oOOoo00000 == 7085 :
 ooOO0o0ooOo0 ( O0O00Oo )
elif oO0oOOoo00000 == 7086 :
 i11iI ( O0O00Oo )
elif oO0oOOoo00000 == 7087 :
 oo0O0 ( I1iIII1 )
elif oO0oOOoo00000 == 9666 :
 o00O0O ( O0O00Oo )
elif oO0oOOoo00000 == 10100 : i11i1 ( )
elif oO0oOOoo00000 == 101001 : I11I1I ( O0O00Oo )
elif oO0oOOoo00000 == 10105 : i1iiIi1II1 ( O0O00Oo )
elif oO0oOOoo00000 == 10106 : iiI1Iii ( O0O00Oo )
elif oO0oOOoo00000 == 10104 : iiiioOoO0oOO ( O0O00Oo )
elif oO0oOOoo00000 == 10107 : ii1i11Ii11iI ( )
elif oO0oOOoo00000 == 10103 : ooOoo ( O0O00Oo )
elif oO0oOOoo00000 == 10108 : iii1OO00Oo00o ( O0O00Oo )
elif oO0oOOoo00000 == 10000 : Origin_Menu ( )
elif oO0oOOoo00000 == 10001 : o0OO0O0Oo ( )
elif oO0oOOoo00000 == 10002 : O0Oooo ( )
elif oO0oOOoo00000 == 10003 : ooO00OO ( )
elif oO0oOOoo00000 == 10004 : OOoOOo0O00O ( O0O00Oo )
elif oO0oOOoo00000 == 10005 : I11iIiI1 ( )
elif oO0oOOoo00000 == 10006 : IIi1IiiIi1III ( O0O00Oo )
elif oO0oOOoo00000 == 10007 : o00o0o0oOo0 ( O0O00Oo , oo00O00oO000o )
elif oO0oOOoo00000 == 10008 : o0ooOOOo0O0 ( )
elif oO0oOOoo00000 == 10009 : oO0o0ooooo ( )
elif oO0oOOoo00000 == 10010 : oooo0O ( O0O00Oo )
elif oO0oOOoo00000 == 10011 : o00Oo ( O0O00Oo )
elif oO0oOOoo00000 == 10012 : OooO0OO ( O0O00Oo )
elif oO0oOOoo00000 == 10113 : GRABG ( O0O00Oo , OOoO )
elif oO0oOOoo00000 == 10109 : ii1iiiIiiIiiI ( O0O00Oo )
elif oO0oOOoo00000 == 10013 : I1IiiI1I1I ( O0O00Oo )
elif oO0oOOoo00000 == 10014 : O0o0oOO ( )
elif oO0oOOoo00000 == 10015 : OO00o0oo ( )
elif oO0oOOoo00000 == 10016 : O00oOo ( O0O00Oo )
elif oO0oOOoo00000 == 10017 : I1IiIi1iiI ( )
elif oO0oOOoo00000 == 10018 : i1I111II11 ( )
elif oO0oOOoo00000 == 10019 : Ooo00OoO0O00 ( )
elif oO0oOOoo00000 == 10020 : iiIIIIiI11II1 ( )
elif oO0oOOoo00000 == 10021 : oo0o0ooOoo00O ( )
elif oO0oOOoo00000 == 10022 : oo0OOoOo0 ( O0O00Oo )
elif oO0oOOoo00000 == 10023 : o0oOOO0 ( OOoO , O0O00Oo )
elif oO0oOOoo00000 == 10024 : II1i1iI ( O0O00Oo )
elif oO0oOOoo00000 == 10025 : O000OOO0OOo ( )
elif oO0oOOoo00000 == 10026 : Iii11I1i ( )
elif oO0oOOoo00000 == 10027 : i1iiIiIi1 ( )
elif oO0oOOoo00000 == 10028 : o0oO00oooo ( )
elif oO0oOOoo00000 == 10029 : OO0OOO ( )
elif oO0oOOoo00000 == 423 : iiI1II1II111 ( O0O00Oo )
elif oO0oOOoo00000 == 426 : O00O00oO ( O0O00Oo )
elif oO0oOOoo00000 == 10030 : Izle_Films ( )
elif oO0oOOoo00000 == 10031 : Latest_Izle_Movies ( )
elif oO0oOOoo00000 == 10032 : Izle_Genres ( )
elif oO0oOOoo00000 == 10033 : Izle_Pop_Movies ( )
elif oO0oOOoo00000 == 10034 : Izle_Boxsets ( )
elif oO0oOOoo00000 == 10035 : Izle_Search ( )
elif oO0oOOoo00000 == 10036 : Izle_Genres_Movie ( O0O00Oo )
elif oO0oOOoo00000 == 10037 : Izle_Boxset_single ( O0O00Oo )
elif oO0oOOoo00000 == 10038 : Izle_IFRAME ( )
elif oO0oOOoo00000 == 10039 : Izle_Boxsets_Next ( O0O00Oo )
elif oO0oOOoo00000 == 10040 : oo00ooOoO00 ( )
elif oO0oOOoo00000 == 10041 : oOO00I1IIi ( O0O00Oo )
elif oO0oOOoo00000 == 10042 : OoOo0Oooo0o ( O0O00Oo )
elif oO0oOOoo00000 == 10043 : Ii1i111iI ( )
elif oO0oOOoo00000 == 10044 : IiIiIIi ( O0O00Oo )
elif oO0oOOoo00000 == 10045 : i1I1IiIiiI1II ( OOoO )
elif oO0oOOoo00000 == 10046 : o0OO0OOOOOoOOOOooo ( O0O00Oo )
elif oO0oOOoo00000 == 10047 : i11iI1 ( O0O00Oo )
elif oO0oOOoo00000 == 10048 : OOO0oO0O ( O0O00Oo )
elif oO0oOOoo00000 == 10049 : o000oo ( O0O00Oo )
elif oO0oOOoo00000 == 10050 : O0O0Oooo0o ( )
elif oO0oOOoo00000 == 10051 : Iii1iIIi1iIii ( )
elif oO0oOOoo00000 == 10052 : oOOoo0o00 ( )
elif oO0oOOoo00000 == 10053 : Addon ( O0O00Oo )
elif oO0oOOoo00000 == 10054 : i1ii ( O0O00Oo , OOoO )
elif oO0oOOoo00000 == 10055 :
 OoI1 ( "addFavorite" )
 try :
  OOoO = OOoO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OOoO = OOoO . split ( '  - ' ) [ 0 ]
 except :
  pass
 iIi1 ( OOoO , O0O00Oo , oo00O00oO000o , oooOo0OOOoo0 , ii1iIiIIiIIii )
elif oO0oOOoo00000 == 10056 :
 OoI1 ( "rmFavorite" )
 try :
  OOoO = OOoO . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OOoO = OOoO . split ( '  - ' ) [ 0 ]
 except :
  pass
 ii111Ii1i ( OOoO )
elif oO0oOOoo00000 == 10057 :
 OoI1 ( "getFavorites" )
 OOOo0Ooo0o00o ( )
elif oO0oOOoo00000 == 10058 : iiI11Ii1i ( )
elif oO0oOOoo00000 == 10059 : Donators_Guide ( )
elif oO0oOOoo00000 == 10060 : iiIiii1iI1i ( )
elif oO0oOOoo00000 == 10061 : Ii1IOoO0o0O ( )
elif oO0oOOoo00000 == 10062 : oOoOOOO0OOO ( OOoO , O0O00Oo , I1iIII1 )
elif oO0oOOoo00000 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + O000OO0 + ")" )
elif oO0oOOoo00000 == 10064 : IiIIII1iiIIi ( )
elif oO0oOOoo00000 == 10065 : ooooOoo0OO ( O0O00Oo )
elif oO0oOOoo00000 == 10066 : OOO0O00Oo ( O0O00Oo )
elif oO0oOOoo00000 == 10068 : O0OoOO0oo0 ( O0O00Oo )
elif oO0oOOoo00000 == 10069 : OoO ( O0O00Oo )
elif oO0oOOoo00000 == 10070 : i111i1I1ii1i ( O0O00Oo )
elif oO0oOOoo00000 == 10071 : Genie_Watch ( )
elif oO0oOOoo00000 == 10072 : Ooo0oO ( )
elif oO0oOOoo00000 == 10073 : o00O0o0oo0oOO0oO ( O0O00Oo )
elif oO0oOOoo00000 == 10074 : IIi1iI11IIIi1 ( O0O00Oo )
elif oO0oOOoo00000 == 10075 : oo000o ( oo00O00oO000o , OOoO , O0O00Oo )
elif oO0oOOoo00000 == 10076 : iI1I1 ( O0O00Oo )
elif oO0oOOoo00000 == 10077 : o00O ( O0O00Oo )
elif oO0oOOoo00000 == 10078 : iIIIIiiii1I ( )
elif oO0oOOoo00000 == 10079 : Genie_Watch_Tv_Shows ( )
elif oO0oOOoo00000 == 10080 : Genie_Watch_Tv_Genre ( O0O00Oo )
elif oO0oOOoo00000 == 10081 : Genie_Watch_TV_PlayRun ( O0O00Oo )
elif oO0oOOoo00000 == 10082 : Genie_Watch_TV_Episodes ( O0O00Oo , oo00O00oO000o )
elif oO0oOOoo00000 == 10083 : Genie_Watch_Tv_Recent ( O0O00Oo )
elif oO0oOOoo00000 == 10084 : o0Iii ( )
elif oO0oOOoo00000 == 10085 : oo0OOo0 ( )
elif oO0oOOoo00000 == 10086 : O0 ( )
elif oO0oOOoo00000 == 20000 : OOOOO ( )
elif oO0oOOoo00000 == 20001 : o00O0Oooo ( O0O00Oo )
elif oO0oOOoo00000 == 20002 : IiiiI11 ( O0O00Oo )
elif oO0oOOoo00000 == 20003 : oOOo00ooO ( O0O00Oo )
elif oO0oOOoo00000 == 20004 : I111I ( O0O00Oo )
elif oO0oOOoo00000 == 20005 : iIiIi1i1Iiii ( O0O00Oo )
elif oO0oOOoo00000 == 21004 : oo0oooOo ( )
elif oO0oOOoo00000 == 21005 : o0OOoO ( O0O00Oo )
elif oO0oOOoo00000 == 21006 : I1iII1II1I1ii ( O0O00Oo )
elif oO0oOOoo00000 == 21007 : ii11ii1iIiI1 ( O0O00Oo )
elif oO0oOOoo00000 == 21008 : O0O0ooOOO ( O0O00Oo )
elif oO0oOOoo00000 == 21009 : iiIiI1i1 ( O0O00Oo )
elif oO0oOOoo00000 == 30000 : OO00 ( )
elif oO0oOOoo00000 == 30001 : ooOoo0OOOO0o ( )
elif oO0oOOoo00000 == 100121 : Resolve ( O0O00Oo )
elif oO0oOOoo00000 == 30003 : o0I1IiiiiI1i1I ( )
elif oO0oOOoo00000 == 30004 : iii11OO0oO ( O0O00Oo )
elif oO0oOOoo00000 == 30005 : i1IIIi1Iii1i ( O0O00Oo )
elif oO0oOOoo00000 == 30006 : iI11IiiiIII ( )
elif oO0oOOoo00000 == 30007 : o00ii11iiIIII ( )
elif oO0oOOoo00000 == 30008 : iII ( O0O00Oo )
elif oO0oOOoo00000 == 30009 : Oo00oo00o00Oo ( O0O00Oo )
elif oO0oOOoo00000 == 30010 : OOOO00 ( O0O00Oo )
elif oO0oOOoo00000 == 30011 : iiI111iIi1 ( )
elif oO0oOOoo00000 == 30012 : Ii1i ( )
elif oO0oOOoo00000 == 30013 : oO00o0oOoo ( )
elif oO0oOOoo00000 == 30014 : o00o0 ( )
elif oO0oOOoo00000 == 30015 : ii111 ( O0O00Oo , oo00O00oO000o , oooOo0OOOoo0 )
elif oO0oOOoo00000 == 30016 : iII1i1 ( O0O00Oo )
elif oO0oOOoo00000 == 30019 : OooO0o ( O0O00Oo )
elif oO0oOOoo00000 == 30017 : oooo00Oo0O ( O0O00Oo )
elif oO0oOOoo00000 == 30018 : Iii1II1 ( O0O00Oo )
elif oO0oOOoo00000 == 30030 : i11Ii111I1 ( )
elif oO0oOOoo00000 == 30031 : OOOii ( )
elif oO0oOOoo00000 == 30032 : I1i11111i1i11 ( )
elif oO0oOOoo00000 == 30033 : Ooi11 ( )
elif oO0oOOoo00000 == 30034 : O00oOoOo0ooO0O0oo ( )
elif oO0oOOoo00000 == 30035 : IIIiIiiI1i ( O0O00Oo )
elif oO0oOOoo00000 == 30036 : I1IiiiI ( O0O00Oo )
elif oO0oOOoo00000 == 30037 : iIiI1111 ( O0O00Oo )
elif oO0oOOoo00000 == 30038 : o00O0o00oo ( )
elif oO0oOOoo00000 == 30039 : iI ( )
elif oO0oOOoo00000 == 50000 : Iii1I1111ii ( )
elif oO0oOOoo00000 == 50001 : i1Oo ( )
elif oO0oOOoo00000 == 50002 : IIIII11II1 ( O0O00Oo )
elif oO0oOOoo00000 == 50003 : Table_Menu ( I1iIII1 )
elif oO0oOOoo00000 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif oO0oOOoo00000 == 60001 : oOIIII ( )
elif oO0oOOoo00000 == 60002 : O0Ooo0O ( OOoO )
elif oO0oOOoo00000 == 60003 : iiII1i ( O0O00Oo )
elif oO0oOOoo00000 == 600033 : IiI1IiI1iiI1 ( O0O00Oo )
elif oO0oOOoo00000 == 60004 : OOOooO00OO00O ( O0O00Oo )
elif oO0oOOoo00000 == 50004 : o0OO0 ( )
elif oO0oOOoo00000 == 50005 : speedtest . runtest ( O0O00Oo )
elif oO0oOOoo00000 == 70001 : III1I ( )
elif oO0oOOoo00000 == 70002 : i1I ( O0O00Oo )
elif oO0oOOoo00000 == 70003 : oOo000Oo00o ( O0O00Oo )
elif oO0oOOoo00000 == 70004 : o0ooOOoOoOO ( O0O00Oo )
elif oO0oOOoo00000 == 70005 : iII11 ( O0O00Oo )
elif oO0oOOoo00000 == 70006 : O00OO00OOOoO ( )
elif oO0oOOoo00000 == 50006 : oooO ( i1 , i1111 )
elif oO0oOOoo00000 == 80000 : Oooo ( )
elif oO0oOOoo00000 == 80001 : resolvefilmon ( O0O00Oo )
elif oO0oOOoo00000 == 80002 : O000Oo00 ( )
elif oO0oOOoo00000 == 80003 : i1111I ( OOoO , O0O00Oo , "None" )
elif oO0oOOoo00000 == 80004 : O0OO00 ( OOoO , O0O00Oo )
elif oO0oOOoo00000 == 80005 : II1iiiiII ( )
elif oO0oOOoo00000 == 80006 : IiI ( O0O00Oo )
elif oO0oOOoo00000 == 80007 : o0o0OO0o00o0O ( O0O00Oo )
elif oO0oOOoo00000 == 80008 : IIIIIIi1i ( )
elif oO0oOOoo00000 == 80009 : oO0oo0O0OOOo0 ( )
elif oO0oOOoo00000 == 80010 : iII11I ( O0O00Oo )
elif oO0oOOoo00000 == 80011 : oOoOoOOOO0o ( O0O00Oo )
elif oO0oOOoo00000 == 80012 : OoO00o ( )
elif oO0oOOoo00000 == 90000 : o0oiIiI1i1iiIi1i ( OOoO , O0O00Oo )
elif oO0oOOoo00000 == 90001 : tools ( )
elif oO0oOOoo00000 == 90002 : Oo00o0OO0O00o ( )
elif oO0oOOoo00000 == 90003 : O0ooOOO00000O ( O0O00Oo )
elif oO0oOOoo00000 == 90004 : OOoo ( O0O00Oo )
elif oO0oOOoo00000 == 90005 : OO0ooOO00o0 ( O0O00Oo )
elif oO0oOOoo00000 == 90006 : o0OOOIiII11I1I1IIi ( O0O00Oo )
elif oO0oOOoo00000 == 90007 : ii1i111 ( O0O00Oo )
elif oO0oOOoo00000 == 90008 : o0OO00oOO ( O0O00Oo )
elif oO0oOOoo00000 == 90009 : OoO00oooo0o ( O0O00Oo )
elif oO0oOOoo00000 == 90010 : i1I1i111Ii ( )
elif oO0oOOoo00000 == 90020 : oOOoOO ( )
elif oO0oOOoo00000 == 90021 : hellyeah2 ( O0O00Oo )
elif oO0oOOoo00000 == 90022 : hellyeah3 ( O0O00Oo )
elif oO0oOOoo00000 == 90023 : oOO000O ( )
elif oO0oOOoo00000 == 90024 : iiIiIiII ( O0O00Oo )
elif oO0oOOoo00000 == 90025 : iiiiiIIi ( O0O00Oo )
if 7 - 7: I1ii11iIi11i * IIiIiII11i
elif oO0oOOoo00000 == 90026 : ooIi11iI ( )
elif oO0oOOoo00000 == 90027 : Oo0oo ( OOoO , I1iIII1 )
if 11 - 11: OOooOOo % ii
elif oO0oOOoo00000 == 900300 : o0oooOO00 ( )
elif oO0oOOoo00000 == 900301 : iiIiii1IIIII ( O0O00Oo )
elif oO0oOOoo00000 == 900302 : oo00o0 ( O0O00Oo )
elif oO0oOOoo00000 == 90030 : II1iIi11 ( )
elif oO0oOOoo00000 == 90031 : I1III1111iIi ( )
elif oO0oOOoo00000 == 90032 : I1i111I ( O0O00Oo )
elif oO0oOOoo00000 == 90033 : OooOo0oo0O0o00O ( O0O00Oo )
elif oO0oOOoo00000 == 90034 : OOOooo ( O0O00Oo )
elif oO0oOOoo00000 == 90035 : o0OOo0o0O0O ( O0O00Oo )
elif oO0oOOoo00000 == 90036 : II1i1I ( O0O00Oo )
elif oO0oOOoo00000 == 90039 : OOo0Oo ( O0O00Oo )
elif oO0oOOoo00000 == 90037 : OOo00OoO ( O0O00Oo )
elif oO0oOOoo00000 == 90038 : II1I11IIi ( )
if 92 - 92: OOooOOo - IiI1i11I * o0ii1I - ooOoO0O00
elif oO0oOOoo00000 == 10090 : OoOo0oOooOoOO ( )
elif oO0oOOoo00000 == 10091 : iiiI ( O0O00Oo )
elif oO0oOOoo00000 == 10092 : O0oo0O00ooOo ( O0O00Oo )
elif oO0oOOoo00000 == 10093 : ii1I ( O0O00Oo , oo00O00oO000o )
elif oO0oOOoo00000 == 10094 : O0000ooO ( O0O00Oo , oo00O00oO000o )
if 87 - 87: o0ii1I * i1IiiiI1iI + iI11I1II1I1I * I11i * iI11I1II1I1I . Iii
elif oO0oOOoo00000 == 10095 : o0O0O0ooo0oOO ( )
elif oO0oOOoo00000 == 10096 : iIiIii1ii ( O0O00Oo )
elif oO0oOOoo00000 == 10097 : i1II11Iii1I ( O0O00Oo )
elif oO0oOOoo00000 == 10098 : iIi1Ii ( O0O00Oo )
elif oO0oOOoo00000 == 10099 : o0O0O0 ( O0O00Oo )
if 66 - 66: o0ii1I / oO0o . o0o00Oo0O . Iii % ii / oooOo0oo0oo
elif oO0oOOoo00000 == 10200 : O0o ( )
elif oO0oOOoo00000 == 10201 : OOooO0o ( O0O00Oo )
elif oO0oOOoo00000 == 10202 : IIIIIiII1 ( O0O00Oo )
elif oO0oOOoo00000 == 10203 : RT4 ( O0O00Oo )
if 49 - 49: oOo0O0Ooo * IiI1i11I - oO0o % o0ii1I + o0ii1I * i1IiiiI1iI
elif oO0oOOoo00000 == 90040 : OOOoO0 ( )
elif oO0oOOoo00000 == 90041 : oooO00Oo ( O0O00Oo )
elif oO0oOOoo00000 == 90042 : I11i11I ( O0O00Oo )
elif oO0oOOoo00000 == 90043 : i11i11i ( O0O00Oo )
elif oO0oOOoo00000 == 90044 : i1II1II1iii1i ( O0O00Oo )
elif oO0oOOoo00000 == 90045 : IiiIiI1I1 ( )
elif oO0oOOoo00000 == 90046 : O0OO0oOO ( O0O00Oo )
elif oO0oOOoo00000 == 90050 : iI1IiiiIiI1Ii ( )
elif oO0oOOoo00000 == 90051 : OOoo0oOO00 ( O0O00Oo )
elif oO0oOOoo00000 == 90052 : i1I1III1i1i ( O0O00Oo )
elif oO0oOOoo00000 == 90053 : Ii111iIIIi ( O0O00Oo )
elif oO0oOOoo00000 == 90054 : IiI1O0oO ( O0O00Oo )
elif oO0oOOoo00000 == 90055 : o0Ii1 ( )
if 94 - 94: OOooOOo - Iii + o0ii1I + OOooOOo + IIiIiII11i
elif oO0oOOoo00000 == 100001 : Stand_up ( )
if 61 - 61: III1iiIii + o0ii1I / i1i1I1IIii1II . ii + IiI1i11I
elif oO0oOOoo00000 == 100003 : O00oOo ( O0O00Oo )
elif oO0oOOoo00000 == 100004 : I1iIiI11I1 ( O0O00Oo )
elif oO0oOOoo00000 == 100005 : Resolve ( O0O00Oo )
elif oO0oOOoo00000 == 100008 : Search ( )
elif oO0oOOoo00000 == 100007 : Oo ( O0O00Oo )
elif oO0oOOoo00000 == 100009 : yt . PlayVideo ( O0O00Oo )
elif oO0oOOoo00000 == 100010 : OoOiIIiii ( O0O00Oo )
elif oO0oOOoo00000 == 100100 : OOoOoo0 ( oo00O00oO000o , O0O00Oo , I1i1ii )
elif oO0oOOoo00000 == 100101 : oo0OOo0O ( O0O00Oo , OOoO , oooOo0OOOoo0 , I1i1ii , oo00O00oO000o )
elif oO0oOOoo00000 == 100102 : ii1ii11 ( OOoO , O0O00Oo , oo00O00oO000o , oooOo0OOOoo0 )
elif oO0oOOoo00000 == 100106 : ii1i1i1IiII ( O0O00Oo , OOoO )
elif oO0oOOoo00000 == 100107 : oOOOo ( )
elif oO0oOOoo00000 == 100108 : o0oOoO00oo0oOo ( )
elif oO0oOOoo00000 == 100109 : I11IiI1III ( O0O00Oo )
elif oO0oOOoo00000 == 40000 : o0oO0o0oo0O0 ( )
elif oO0oOOoo00000 == 40001 : Iiii1Ii1I ( O0O00Oo )
elif oO0oOOoo00000 == 100110 : Ii111IIi ( )
elif oO0oOOoo00000 == 100111 : iII1ii1I1i ( O0O00Oo )
elif oO0oOOoo00000 == 100110 : Ii111IIi ( )
elif oO0oOOoo00000 == 100210 : O0Oo ( O0O00Oo )
elif oO0oOOoo00000 == 100211 : Iiii1 ( )
elif oO0oOOoo00000 == 100212 : OooOO0oOOo0O ( )
elif oO0oOOoo00000 == 100213 : oOOOOOo ( )
elif oO0oOOoo00000 == 100214 : IIIi ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
