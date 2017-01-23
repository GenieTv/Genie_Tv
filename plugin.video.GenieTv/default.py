# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
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
from imports import Parse , CNF_Studio_Indexer , speedtest , uservar
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
IiiIII111iI = "3.4.1"
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
I11 = ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIv' ) )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
oOo0oooo00o = os . path . join ( Oo0o0000o0o0 , 'userdata' )
oO0o0o0ooO0oO = os . path . join ( oOo0oooo00o , 'addon_data' , IiII )
oo0o0O00 = os . path . join ( oO0o0o0ooO0oO , 'wizard.log' )
oO = uservar . ADDONTITLE
i1iiIIiiI111 = xbmc . translatePath ( 'special://profile/' )
oooOOOOO = [ 'xbmc.log' , 'xbmc.old.log' , 'kodi.log' , 'kodi.old.log' , 'spmc.log' , 'spmc.old.log' , 'tvmc.log' , 'tvmc.old.log' ]
i1i1II = os . path . join ( Oo0o0000o0o0 , 'addons' )
i1iiIII111ii = os . path . join ( i1i1II , 'packages' )
i1iIIi1 = os . path . join ( i1i1II , 'HUB' )
ii11iIi1I = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYXBrLnR4dA==' ) )
iI111I11I1I1 = Net ( )
OOooO0OOoo = xbmcgui . Dialog ( )
iIii1 = oo00 . getSetting ( 'Build' )
oOOoO0 = oo00 . getSetting ( 'Local' )
O0OoO000O0OO = oo00 . getSetting ( 'Remote' )
iiI1IiI = oo00 . getSetting ( 'LocalM3u' )
II = oo00 . getSetting ( 'TEXTCOL' )
ooOoOoo0O = oo00 . getSetting ( 'Downloads' )
OooO0 = xbmc . translatePath ( 'special://logpath/' )
II11iiii1Ii = oo00 . getSetting ( 'User' )
OO0o = oo00 . getSetting ( 'Pass' )
Ooo = oo00 . getSetting ( 'AdultPass' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
O0o0Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'fanart.jpg' ) )
Oo00OOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + iiIIIII1i1iI , 'icon.png' ) )
O0O = ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vR2VuaWVBcnQvb3JpZ2luLnBuZw==' ) )
O00o0OO = xbmc . translatePath ( 'special://database' )
I11i1 = xbmc . translatePath ( 'special://home/userdata/addon_data/plugin.video.GenieTV' )
iIi1ii1I1 = xbmc . translatePath ( 'special://thumbnails' ) ;
o0 = "GenieTv"
I11II1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv' ) )
IIIII = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/Change_Log_Temp' ) )
ooooooO0oo = 'http://'
IIiiiiiiIi1I1 = datetime . now ( )
I1IIIii = base64 . decodestring ( 'LnBocA==' )
oOoOooOo0o0 = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
OOOO = [ ]
OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
iiiiiIIii = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
O000OO0 = oo00 . getLocalizedString
I11iii1Ii = CookieJar ( )
I1IIiiIiii = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( I11iii1Ii ) )
I1IIiiIiii . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
O000oo0O = int ( sys . argv [ 1 ] )
OOOOi11i1 = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
IIIii1II1II = os . path . join ( I11i1 , 'favorites' )
i1I1iI = I11i1 + '/addons.ini'
oOo0oooo00o = xbmc . translatePath ( 'special://home/userdata/' )
oo0OooOOo0 = xbmc . translatePath ( 'special://home/userdatabroke/' )
o0O = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
O00oO = xbmc . translatePath ( 'special://home/userdata/addon_data' )
I11i1I1I = O00oO + 'GenieTvWatched'
oO0Oo = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYw==' ) )
oOOoo0Oo = [ 'daclips' , 'filehoot' , 'allmyvideos' , 'vidspot' , 'vodlocker' , 'vidto' ]
if not os . path . exists ( I11i1I1I ) :
 os . makedirs ( I11i1I1I )
o00OO00OoO = I11i1I1I + 'watched.txt'
if not os . path . exists ( o00OO00OoO ) :
 open ( o00OO00OoO , 'w+' )
OOOO0OOoO0O0 = open ( o00OO00OoO ) . read ( )
O0Oo000ooO00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
Ii1iIiII1ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
ooOooo000oOO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
Oo0oOOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
Oo0OoO00oOO0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( IIIii1II1II ) == True :
 OOO00O = open ( IIIii1II1II ) . read ( )
else : OOO00O = [ ]
OOoOO0oo0ooO = oo00 . getSetting ( 'debug' )
if os . path . exists ( I11i1 ) == False :
 os . makedirs ( I11i1 )
def O0o0O00Oo0o0 ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1Oo00 = ''
 i1i = ''
 try :
  i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
  i1i = i1Oo00 . read ( )
  i1Oo00 . close ( )
 except : pass
 if i1i != '' :
  return i1i
 else :
  i1i = 'Failed'
  return i1i
  if 50 - 50: o000O0o
iI1iII1 = [ ]
oO0OOoo0OO = O0o0O00Oo0o0 ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if oO0OOoo0OO != 'Failed' :
 iI1iII1 . append ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not oO0OOoo0OO != 'Failed' :
 O0 = O0o0O00Oo0o0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if O0 != 'Failed' :
  iI1iII1 . append ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not O0 != 'Failed' :
  ii1ii1ii = O0o0O00Oo0o0 ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if ii1ii1ii != 'Failed' :
   iI1iII1 . append ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not ii1ii1ii != 'Failed' :
   oooooOoo0ooo = O0o0O00Oo0o0 ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if oooooOoo0ooo != 'Failed' :
    iI1iII1 . append ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
I1I1IiI1 = ( str ( iI1iII1 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
III1iII1I1ii = I1I1IiI1 + 'GenieArt/NEW/'
if 61 - 61: Ii1IIIi1
if 86 - 86: ooOOOoO % ii1ii11IIIiiI - O0OOOoOoo0 - I1111IIi
def Oo0oO ( ) :
 if not os . path . exists ( iI1Ii11111iIi ) :
  OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  IIiIi1iI = 'genie tv repo not being installed '
  i1IiiiI1iI ( )
 else :
  i1iIi ( )
  if 68 - 68: iiiiiiii1 % I11i1ii1 / I1111IIi
def i1iIi ( ) :
 if 58 - 58: oO0o % Ii . O0OOOoOoo0 / o000O0o
 O0o = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 II111iiiI1Ii = open ( Oo0oOOo ) . read ( )
 o0O0OOO0Ooo = open ( Oo0OoO00oOO0o ) . read ( )
 if 45 - 45: o0o00Oo0O / I11i
 i1IIIII11I1IiI = re . compile ( 'version="([^"]*)" provider' ) . findall ( II111iiiI1Ii )
 i1I = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( o0O0OOO0Ooo )
 OoOO = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( O0o )
 ooOOO0 = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( O0o )
 for o0o in i1IIIII11I1IiI :
  O0OOoO00OO0o = o0o
  for I1111IIIIIi in OoOO :
   if not I1111IIIIIi == O0OOoO00OO0o :
    o0oOoO00o . create ( 'Incorrect Addon Version' , 'Downloading Correct Version' , )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    Iiii1i1 ( )
   if I1111IIIIIi == O0OOoO00OO0o :
    OO
 for oo000o in i1I :
  iiIi1IIi1I = oo000o
  for o0OoOO000ooO0 in ooOOO0 :
   if not o0OoOO000ooO0 == iiIi1IIi1I :
    o0oOoO00o . create ( 'Incorrect Repo Installed' , 'Installing Correct Version' , '' )
    xbmc . sleep ( 1000 )
    o0oOoO00o . close
    i1IiiiI1iI ( )
   if o0OoOO000ooO0 == iiIi1IIi1I :
    xbmc . sleep ( 100 )
    OO
def o0o0o0oO0oOO ( ) :
 Oo0oO ( )
 ii1Ii11I ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  o00o0 ( )
 else :
  if oo00 . getSetting ( 'My Build' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']WIZARD[/COLOR]' , str ( I1I1IiI1 ) , 4001 , III1iII1I1ii + 'Wizard.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 4002 , III1iII1I1ii + 'Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Sports[/COLOR]' , '' , 90010 , III1iII1I1ii + 'tommys.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Live List[/COLOR]' , '' , 4009 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Music' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']Music[/COLOR]' , str ( I1I1IiI1 ) , 4003 , III1iII1I1ii + 'Music.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TOOLS[/COLOR]' , '' , 90001 , III1iII1I1ii + 'tools.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']Force Genie Update Kodi 16+[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , III1iII1I1ii + 'GenieUpdate.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']CONTACT US[/COLOR]' , '' , 50006 , III1iII1I1ii + 'Contact-Us.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , III1iII1I1ii + 'settings.png' , O0o0Oo , '' )
  if I1IIII1i ( ) == 'android' :
   iiOOooooO0Oo ( '[COLOR' + II + ']APK TOOL[/COLOR]' , str ( I1I1IiI1 ) , 30039 , III1iII1I1ii + 'APKTools.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']BUILDERS TOOLBOX[/COLOR]' , str ( I1I1IiI1 ) , 32 , III1iII1I1ii + 'BuildersToolbox.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   OOiIiIIi1 ( '[COLOR' + II + ']SOURCE LIST[/COLOR]' , str ( I1I1IiI1 ) , 46 , III1iII1I1ii + 'SoruceList.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']MAINTENANCE[/COLOR]' , str ( I1I1IiI1 ) , 3 , III1iII1I1ii + 'Maintenance.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']ADDONS[/COLOR]' , '' , 10050 , III1iII1I1ii + 'Addons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']GenieTv RSS Feed[/COLOR]' , str ( I1I1IiI1 ) , 39 , III1iII1I1ii + 'GenieTVRSSFeed.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def o00o0 ( ) :
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']WIZARD[/COLOR]' , str ( I1I1IiI1 ) , 4001 , III1iII1I1ii + 'Wizard.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 4002 , III1iII1I1ii + 'Streams.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Sports[/COLOR]' , '' , 90010 , III1iII1I1ii + 'tommys.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Live List[/COLOR]' , '' , 4009 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']Music[/COLOR]' , str ( I1I1IiI1 ) , 4003 , III1iII1I1ii + 'Music.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']MAINTENANCE[/COLOR]' , str ( I1I1IiI1 ) , 3 , III1iII1I1ii + 'Maintenance.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']TOOLS[/COLOR]' , '' , 90001 , III1iII1I1ii + 'tools.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def Ii1I1I1i1Ii ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + II + ']APK TOOL[/COLOR]' , '[COLOR' + II + ']ADDONS[/COLOR]' , '[COLOR' + II + ']BUILDERS TOOLBOX[/COLOR]' , '[COLOR' + II + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + II + ']CONTACT US[/COLOR]' , '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + II + ']SOURCE LIST[/COLOR]' , '[COLOR' + II + ']GUIDE SKINS[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  Iiii1i1 ( )
 if i11I1II1I11i == 1 :
  OooOoOO0 ( )
 if i11I1II1I11i == 2 :
  iI1i11iII111 ( )
 if i11I1II1I11i == 3 :
  Iii1IIII11I ( )
 if i11I1II1I11i == 4 :
  OOOoo0OO ( oO0o0 )
 if i11I1II1I11i == 5 :
  OOooO0OOoo . ok ( i1 , i1111 )
 if i11I1II1I11i == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if i11I1II1I11i == 7 :
  iI1Ii11iIiI1 ( )
 if i11I1II1I11i == 8 :
  OO0Oooo0oOO0O ( )
def OO0Oooo0oOO0O ( ) :
 oO0o0 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( oO0o0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
 I1iIIiiIIi1i ( oO0o0 )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O0O0ooOOO ( )
def oOOo0O00o ( ) :
 iIiIi11 = OOO ( )
 iiiiI = iIiIi11 . replace ( OooO0 , "" )
 if os . path . exists ( iIiIi11 ) or not iIiIi11 == False :
  oooOo0OOOoo0 = open ( iIiIi11 , mode = 'r' ) ; OOoO = oooOo0OOOoo0 . read ( ) ; oooOo0OOOoo0 . close ( )
  OO0O000 ( "%s - %s" % ( i1 , iiiiI ) , OOoO )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OO0Oooo0oOO0O ( ) :
 oO0o0 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( oO0o0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
 I1iIIiiIIi1i ( oO0o0 )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O0O0ooOOO ( )
def iiIiI1i1 ( ) :
 OOiIiIIi1 ( '[COLOR' + II + ']Todays Games[/COLOR]' , str ( I1I1IiI1 ) , 90030 , III1iII1I1ii + 'tgames.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Replays[/COLOR]' , str ( I1I1IiI1 ) , 90031 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 69 - 69: I11i1ii1
def I11iII ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 i1IIIII11I1IiI = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I11iI1i1I11I11 , o000O0O in i1IIIII11I1IiI :
  OO0O000 ( '[COLOR' + II + ']Tommys List[/COLOR]  ' + I11iI1i1I11I11 , o000O0O )
def I1i1i1iii ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 i1IIIII11I1IiI = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 90032 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
def iIIii ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , o00O0O , O0o0Oo , '' )
 for url in next :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , III1iII1I1ii + 'NEXT.png' , O0o0Oo , '' )
def ii1iii1i ( url ) :
 iIIII = OoOooO ( url )
 Iii1I1111ii = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1IIIII11I1IiI = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for I1111i , url in i1I :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for I1111i , url in ooOoO00 :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for url in Iii1I1111ii :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
  if 14 - 14: ooOoO0O00 - I11i % o0o00Oo0O - oO0o
def ooO0O00Oo0o ( url ) :
 if 'drive' in url :
  OOOOo0o00OO0000 ( url )
 else :
  iIIII = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( iIIII )
  for url in i1IIIII11I1IiI :
   OOOOo0o00OO0000 ( url )
def I1i ( url ) :
 O00Oooo = liveresolver . resolve ( url )
 i11I = xbmcgui . ListItem ( path = O00Oooo )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11I )
def o00Oo0oooooo ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 O0oO0 = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0oO0 )
def OOO ( ) :
 iII11 = False
 if os . path . exists ( os . path . join ( OooO0 , 'xbmc.log' ) ) :
  iII11 = os . path . join ( OooO0 , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'kodi.log' ) ) :
  iII11 = os . path . join ( OooO0 , 'kodi.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'spmc.log' ) ) :
  iII11 = os . path . join ( OooO0 , 'spmc.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'tvmc.log' ) ) :
  iII11 = os . path . join ( OooO0 , 'tvmc.log' )
 return iII11
 if 32 - 32: iiiiiiii1
def Iii1 ( url ) :
 if url == 'http://' : return False
 try :
  O00O0oOO00O00 = urllib2 . Request ( url )
  O00O0oOO00O00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
  i1Oo00 . close ( )
 except Exception , oOOOoo00 :
  return oOOOoo00
 return True
def iiIiIIIiiI ( ) :
 if 12 - 12: o0o00Oo0O - I11i
 if 81 - 81: OOooOOo - OOooOOo . O0OOOoOoo0
 if 73 - 73: ooOOOoO % Ii - oOo0O0Ooo
 if 7 - 7: o0o00Oo0O * Ii * ii1ii11IIIiiI + I11i1ii1 % oO0o - I11i1ii1
 if 39 - 39: I1ii11iIi11i * Ii1IIIi1 % Ii1IIIi1 - ii + I11i - ooOOOoO
 i1i = OoOooO ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( i1i )
 if len ( i1IIIII11I1IiI ) > 0 :
  for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O in i1IIIII11I1IiI :
   OOiIiIIi1 ( I1111i , oO0o0 , 50005 , iiO0oOo00o , o0ooooO0o0O , '' )
def iiIi11iI1iii ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + II + ']WIPE GENIE[/COLOR]' , '[COLOR' + II + ']Genie BUILDS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Wizard[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   oo000o0000oO ( )
  if i11I1II1I11i == 1 :
   iI1i111I1Ii ( )
  if i11I1II1I11i == 2 :
   i11i1ii1I ( o0OO0o0o00o )
  if i11I1II1I11i == 3 :
   oOo0 ( oO0o0 )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 10060 , III1iII1I1ii + 'BackupMyBuild.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 49 , III1iII1I1ii + 'RestoreMyBuild.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']WIPE GENIE[/COLOR]' , str ( I1I1IiI1 ) , 41 , III1iII1I1ii + 'WipeGenie.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']WISHES PC[/COLOR]' , str ( I1I1IiI1 ) , 1 , III1iII1I1ii + 'WISHESPC.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Genie BUILDS[/COLOR]' , str ( I1I1IiI1 ) , 44 , III1iII1I1ii + 'GenieBuilds.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 56 - 56: I11i + IIiIiII11i + OOooOOo - I11i1ii1 . OOooOOo
def OOOooo ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FAVOURITES[/COLOR]' , str ( I1I1IiI1 ) , 10057 , III1iII1I1ii + 'Favourites.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 9000 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAM TEAM[/COLOR]' , str ( I1I1IiI1 ) , 4006 , III1iII1I1ii + 'StreamTeam.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , III1iII1I1ii + 'bamf.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 4004 , III1iII1I1ii + 'Movies.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , str ( I1I1IiI1 ) , 4005 , III1iII1I1ii + 'TVShows.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']KIDS[/COLOR]' , str ( I1I1IiI1 ) , 4007 , III1iII1I1ii + 'Kids.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( I1I1IiI1 ) , 90023 , III1iII1I1ii + 'freeview.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cHM6Ly9hdGxhbnRpYzI4MC5zdGFydGRlZGljYXRlZC5uZXQvYm9zcy9kb2NzLw==' ) , 2032 , III1iII1I1ii + 'boss.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAM CATEGORIES[/COLOR]' , str ( I1I1IiI1 ) , 90002 , III1iII1I1ii + 'cats.png' , O0o0Oo , '' )
  if Ooo == '5knuckleshuffle' :
   iiOOooooO0Oo ( '[COLOR' + II + ']XVID[/COLOR]' , str ( I1I1IiI1 ) , 10100 , III1iII1I1ii + 'Jizbox.png' , O0o0Oo , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']ADULT CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30033 , III1iII1I1ii + 'adu.png' , O0o0Oo , '' )
 else :
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FAVOURITES[/COLOR]' , str ( I1I1IiI1 ) , 10057 , III1iII1I1ii + 'Favourites.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 9000 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAM TEAM[/COLOR]' , str ( I1I1IiI1 ) , 4006 , III1iII1I1ii + 'StreamTeam.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , III1iII1I1ii + 'bamf.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 4004 , III1iII1I1ii + 'Movies.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , str ( I1I1IiI1 ) , 4005 , III1iII1I1ii + 'TVShows.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']KIDS[/COLOR]' , str ( I1I1IiI1 ) , 4007 , III1iII1I1ii + 'Kids.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cHM6Ly9hdGxhbnRpYzI4MC5zdGFydGRlZGljYXRlZC5uZXQvYm9zcy9kb2NzLw==' ) , 2032 , III1iII1I1ii + 'boss.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( I1I1IiI1 ) , 90023 , III1iII1I1ii + 'freeview.png' , O0o0Oo , '' )
  if Ooo == '5knuckleshuffle' :
   iiOOooooO0Oo ( '[COLOR' + II + ']XVID[/COLOR]' , str ( I1I1IiI1 ) , 10100 , III1iII1I1ii + 'Jizbox.png' , O0o0Oo , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']ADULT CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30033 , III1iII1I1ii + 'adu.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' , '' , 9034 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   OOiIiIIi1 ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FOOTBALL[/COLOR]' , '' , 10002 , III1iII1I1ii + 'Football.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']NEWS[/COLOR]' , str ( I1I1IiI1 ) , 30032 , III1iII1I1ii + 'News.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'GenieTVTutorials.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']HOBBIES[/COLOR]' , str ( I1I1IiI1 ) , 4008 , III1iII1I1ii + 'Hobbies.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Stand Up' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']STAND UP[/COLOR]' , '' , 10003 , III1iII1I1ii + 'StandUp.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , str ( I1I1IiI1 ) , 8040 , III1iII1I1ii + 'documentaries.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , str ( I1I1IiI1 ) , 7001 , III1iII1I1ii + 'DiscloseTV.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']24/7 STREAMS[/COLOR]' , '' , 30030 , III1iII1I1ii + '247Streams.png' , O0o0Oo , '' )
  if 94 - 94: ii + I1ii11iIi11i / OOooOOo * Ii1IIIi1
  if 69 - 69: I11i1ii1 % o000O0o
  if 50 - 50: ii % ooOOOoO
  if 49 - 49: o000O0o - Ii . iiiiiiii1 * ii1ii11IIIiiI % O0OOOoOoo0 + ooOoO0O00
  if 71 - 71: I11i
  if 38 - 38: o000O0o % OOooOOo + Ii1I . Ii
  if 53 - 53: Ii * O0OOOoOoo0
  if 68 - 68: iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
  if 38 - 38: I11i1ii1 - Ii1IIIi1 / O0OOOoOoo0
  if 66 - 66: o0o00Oo0O % Ii1I + Ii . OOooOOo / ii1ii11IIIiiI + Ii1I
  if 86 - 86: I11i
  if 5 - 5: I1111IIi * OOooOOo
  if 5 - 5: iiiiiiii1
  if 90 - 90: iiiiiiii1 . I11i1ii1 / ii1ii11IIIiiI - ooOOOoO
  if 40 - 40: ii
  if 25 - 25: I1111IIi + ii1ii11IIIiiI / I11i1ii1 . I11i % o0o00Oo0O * oO0o
 I1I11i ( 'movies' , 'MAIN' )
def o0O0oo0OO0O ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']FOOTBALL[/COLOR]' , '[COLOR' + II + ']KIDS[/COLOR]' , '[COLOR' + II + ']NEWS[/COLOR]' , '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + II + ']HOBBIES[/COLOR]' , '[COLOR' + II + ']STAND UP[/COLOR]' , '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']CATEGORIES[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OO0 ( )
 if i11I1II1I11i == 1 :
  o0Oooo ( )
 if i11I1II1I11i == 2 :
  iiI ( )
 if i11I1II1I11i == 3 :
  oOIIiIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , OOoOooOoOOOoo , I1111i )
 if i11I1II1I11i == 4 :
  Iiii1iI1i ( )
 if i11I1II1I11i == 5 :
  I1ii1ii11i1I ( )
 if i11I1II1I11i == 6 :
  o0OoOO ( )
 if i11I1II1I11i == 7 :
  O0O0Oo00 ( )
 if i11I1II1I11i == 8 :
  oOoO00o ( )
  if 100 - 100: I11i + Ii1IIIi1 * I11i
  if 80 - 80: I11i * o0o00Oo0O - ii1ii11IIIiiI
def ii1Ii11I ( ) :
 if not os . path . exists ( IIIII ) :
  OO0O000 ( 'Change Log 23/01/17 - v3.4.1' , 'Boss Documentaries A Masterpiece By Jason Cadd, Updates To All Searches, StreamTeam Cleaned Up, Addon Overall CleanUp, General Maintence' )
  os . makedirs ( IIIII )
  if 66 - 66: Ii - Ii1IIIi1 * I1ii11iIi11i
  if 76 - 76: Ii + I11i / Ii1I - oO0o - ii1ii11IIIiiI + Ii1I
def ooI1i ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + II + ']MOVIE HUB[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   iIII ( )
  if i11I1II1I11i == 1 :
   o0o0O ( )
  if i11I1II1I11i == 2 :
   ooooO0oOoOOoO ( )
  if i11I1II1I11i == 3 :
   I1i11i ( oO0o0 )
  if i11I1II1I11i == 4 :
   IiIi ( )
  if i11I1II1I11i == 5 :
   OOOOO0O00 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if i11I1II1I11i == 6 :
   Iii ( )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 10200 , III1iII1I1ii + 'rated.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MOVIE HUB[/COLOR]' , '' , 90040 , III1iII1I1ii + 'movhub.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']POPCORN BOX[/COLOR]' , str ( I1I1IiI1 ) , 7061 , III1iII1I1ii + 'PopcornBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Desi Flix[/COLOR]' , '' , 80005 , III1iII1I1ii + 'Desi.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , III1iII1I1ii + 'FilmTrailers.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , III1iII1I1ii + 'ClassicMovies.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def iIIiIiI1I1 ( ) :
 Oo0oO ( )
 ooO ( )
 if 6 - 6: iI11I1II1I1I . I11i1ii1 % I11i
 if 50 - 50: O0OOOoOoo0 + o0o00Oo0O + ii1ii11IIIiiI . IIiIiII11i / I11i
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  OOiIiIIi1 ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , III1iII1I1ii + 'TvGuide.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']Link GTV to Guide[/COLOR]' , '' , 4010 , III1iII1I1ii + 'linkchannels.png' , O0o0Oo , '' )
def oOoO00o ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']DAILY LISTS[/COLOR]' , '' , 9007 , Oo00OOOOO , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Oo00OOOOO , O0o0Oo , '' )
 if 17 - 17: ii1ii11IIIiiI % iI11I1II1I1I - iI11I1II1I1I
 if 78 - 78: O0OOOoOoo0 + ooOOOoO . I11i1ii1 - O0OOOoOoo0 . ii1ii11IIIiiI
 if 30 - 30: oOo0O0Ooo + oO0o % ii1ii11IIIiiI * O0OOOoOoo0 / I1ii11iIi11i - ooOOOoO
 if 64 - 64: iI11I1II1I1I
 if 21 - 21: I1ii11iIi11i . IIiIiII11i
def ooo000o000 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']Tv HUB[/COLOR]' , '[COLOR' + II + ']THE SOURCE[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']RETURN DATES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   O0oO0OOoOOO0oO ( )
  if i11I1II1I11i == 1 :
   I1ii11 ( )
  if i11I1II1I11i == 2 :
   oOoOoOoo0 ( )
  if i11I1II1I11i == 3 :
   III1ii1I ( )
  if i11I1II1I11i == 4 :
   Ii1i1iI ( )
  if i11I1II1I11i == 5 :
   IIiI1 ( )
  if i11I1II1I11i == 6 :
   i1iI1 ( )
  if i11I1II1I11i == 7 :
   ii1I1IiiI1ii1i ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Tv HUB[/COLOR]' , str ( I1I1IiI1 ) , 90050 , III1iII1I1ii + 'Tv HUB.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '' , 10040 , III1iII1I1ii + 'WatchSeries.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '' , 8020 , III1iII1I1ii + 'iWatchSeries.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RETURN DATES[/COLOR]' , str ( I1I1IiI1 ) , 10095 , III1iII1I1ii + 'RD.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC TV[/COLOR]' , str ( I1I1IiI1 ) , 8064 , III1iII1I1ii + 'ClassicTV.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , III1iII1I1ii + 'TVShowTrailers.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def O0ooO0OoO00o ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   II1iiiiII = '[COLOR' + II + ']PANDORAS BOX[/COLOR]'
   if 61 - 61: O0OOOoOoo0 % oOo0O0Ooo - I11i - IIiIiII11i % o0o00Oo0O
   if 90 - 90: iI11I1II1I1I + Ii1I + I11i1ii1 - iiiiiiii1 * I1111IIi . Ii1I
   if 37 - 37: I11i1ii1 % Ii % IIiIiII11i . o0o00Oo0O . ii1ii11IIIiiI
   if 51 - 51: oO0o - o0o00Oo0O % o000O0o - IIiIiII11i
  i1Oo0oO00o = [ II1iiiiII , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + II + ']RAIZ TV[/COLOR]' , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   I1II ( )
  if i11I1II1I11i == 1 :
   oOIIiIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , OOoOooOoOOOoo , I1111i )
   if 64 - 64: o0o00Oo0O % ooOOOoO % o0o00Oo0O * oO0o . o000O0o + oOo0O0Ooo
   if 75 - 75: ooOOOoO . ii % I11i * ooOOOoO % ii
   if 13 - 13: I1111IIi / Ii % IIiIiII11i % ooOOOoO . Ii1I
  if i11I1II1I11i == 2 :
   oOIIiIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , OOoOooOoOOOoo , I1111i )
   if 8 - 8: OOooOOo + I1ii11iIi11i - IIiIiII11i
   if 11 - 11: ooOoO0O00 % Ii - ooOoO0O00 * OOooOOo
  if i11I1II1I11i == 3 :
   oOIIiIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , OOoOooOoOOOoo , I1111i )
 else :
  if 39 - 39: iiiiiiii1
  if 86 - 86: ooOOOoO * oOo0O0Ooo + ooOOOoO + IIiIiII11i
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']PANDORAS BOX[/COLOR]' , str ( I1I1IiI1 ) , 10025 , III1iII1I1ii + 'PandorasBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Roadrunner-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'DojoStreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , III1iII1I1ii + 'raiztv.png' , O0o0Oo , '' )
  if 8 - 8: iiiiiiii1 - O0OOOoOoo0 / I11i1ii1
  if 96 - 96: OOooOOo
  if 29 - 29: Ii1I / ooOoO0O00 . oOo0O0Ooo - OOooOOo - OOooOOo - ii1ii11IIIiiI
  if 20 - 20: ooOoO0O00 % oO0o . oOo0O0Ooo / I1111IIi * Ii * Ii1IIIi1
  if 85 - 85: I11i . OOooOOo / I11i1ii1 . o0o00Oo0O % iiiiiiii1
  if 90 - 90: I1ii11iIi11i % o0o00Oo0O * iI11I1II1I1I . O0OOOoOoo0
 I1I11i ( 'movies' , 'MAIN' )
 if 8 - 8: I11i1ii1 + IIiIiII11i / O0OOOoOoo0 / ooOOOoO
def ooo0O ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
def iII1iii ( url ) :
 iIIII = i11i1iiiII ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( iIIII )
 for ooOO0oO0oo00o , oOOo0oo0O in i1IIIII11I1IiI :
  if '[DIR]' in ooOO0oO0oo00o :
   IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + oOOo0oo0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oOOo0oo0O , 1018 , III1iII1I1ii + 'SilentHunter.png' )
  if 'mkv' in oOOo0oo0O :
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + oOOo0oo0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oOOo0oo0O , 222 , III1iII1I1ii + 'SilentHunter.png' )
  if 'avi' in oOOo0oo0O :
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + oOOo0oo0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oOOo0oo0O , 222 , III1iII1I1ii + 'SilentHunter.png' )
   if 81 - 81: ii1ii11IIIiiI * I11i + iiiiiiii1 + I1ii11iIi11i - ii
def i1i1I111iIi1 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , III1iII1I1ii + 'scraped.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 if 92 - 92: I11i1ii1
def II11iI111i1 ( url ) :
 oO0OOoo0OO = Oo00OoOo ( url )
 i1IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for I1111i , url , ii1ii111 , i11111I1I , o0ooooO0o0O , ii1Oo0000oOo in i1IIIII11I1IiI :
  if i11111I1I == '123' :
   i11111I1I = III1iII1I1ii + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = III1iII1I1ii + 'appstreams.png'
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100010 , i11111I1I , o0ooooO0o0O , ii1Oo0000oOo )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , i11111I1I , o0ooooO0o0O , ii1Oo0000oOo )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , i11111I1I , o0ooooO0o0O , ii1Oo0000oOo )
  elif not 'http' in url :
   I11o0oO00oO0o0o0 ( I1111i , url , 100009 , i11111I1I , o0ooooO0o0O , ii1Oo0000oOo , '' )
  else :
   I11o0oO00oO0o0o0 ( I1111i , url , 100005 , i11111I1I , o0ooooO0o0O , ii1Oo0000oOo , '' )
   if 17 - 17: ooOOOoO . I1111IIi - IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / Ii
def I1IIIiI1I1ii1 ( url ) :
 oO0OOoo0OO = Oo00OoOo ( url )
 iiiI1I1iIIIi1 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , ii1Oo0000oOo , o0ooooO0o0O , I1111i in iiiI1I1iIIIi1 :
  if o00O0O == '123' :
   o00O0O = III1iII1I1ii + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = O0o0Oo
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100004 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo )
  elif not 'http' in url :
   I11o0oO00oO0o0o0 ( I1111i , url , 100009 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo , '' )
  else :
   I11o0oO00oO0o0o0 ( I1111i , url , 100005 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo , '' )
   if 17 - 17: iI11I1II1I1I . ii / ooOOOoO % IIiIiII11i % ooOoO0O00 / Ii
def OOOIiiiii1iI ( url ) :
 if 49 - 49: I11i . I1111IIi / oO0o + IIiIiII11i
 oO0OOoo0OO = Oo00OoOo ( url )
 ii11i = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for III11II1I1Ii1 in ii11i :
  i11111I1I = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( III11II1I1Ii1 ) )
  for i11111I1I in i11111I1I :
   i11111I1I = i11111I1I
  I1111i = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( III11II1I1Ii1 ) )
  for I1111i in I1111i :
   if 'elete' in I1111i :
    pass
   elif 'rivate Vid' in I1111i :
    pass
   else :
    I1111i = ( I1111i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  O00Oo0o000oO = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( III11II1I1Ii1 ) )
  for O00Oo0o000oO in O00Oo0o000oO :
   O00Oo0o000oO = O00Oo0o000oO
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( III11II1I1Ii1 ) )
  for url in url :
   url = url
  I11o0oO00oO0o0o0 ( '[COLORred]' + str ( O00Oo0o000oO ) + '[/COLOR] : ' + str ( I1111i ) , str ( url ) , 100009 , str ( i11111I1I ) , O0o0Oo , '' , '' )
  I1I11i ( 'movies' , '' )
  if 99 - 99: o000O0o * IIiIiII11i * iiiiiiii1
  if 92 - 92: I1ii11iIi11i
  if 40 - 40: OOooOOo / I1111IIi
  if 79 - 79: oO0o - iI11I1II1I1I + ii1ii11IIIiiI - iiiiiiii1
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
def ooO0o ( iconimage , url , extra ) :
 i11111I1I = ' '
 o000 = ' '
 o0ooooO0o0O = ' '
 IiI1i = ' '
 oO0oOOoo00000 = Oo00OoOo ( url )
 i11111I1I = re . compile ( '<img src="(.+?)">' ) . findall ( oO0oOOoo00000 )
 for i11111I1I in i11111I1I :
  i11111I1I = i11111I1I
 oOo00 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( oO0oOOoo00000 )
 for o0ooooO0o0O in oOo00 :
  o0ooooO0o0O = o0ooooO0o0O
 i1IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( oO0oOOoo00000 )
 for url , IiI1i in i1IIIII11I1IiI :
  IiI1i = 'S' + ( IiI1i ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oO0Oo + url
  i1iI11i1IIi ( ( IiI1i ) . replace ( '  ' , '' ) , url , 100101 , i11111I1I , o0ooooO0o0O , o000 , '' )
  I1I11i ( 'Movies' , 'info' )
  if 4 - 4: ii - Ii1I * oOo0O0Ooo
def I1iIiI11I1 ( url , name , fanart , extra , iconimage ) :
 i1oOOoo0o0OOOO = extra
 IiI1i = name
 oO0oOOoo00000 = Oo00OoOo ( url )
 i11111I1I = iconimage
 i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( oO0oOOoo00000 )
 for url , name , i1IiII1III in i1IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oO0Oo + url
  i1IiII1III = i1IiII1III
  i1O00oo = name + ' - [COLORred]' + i1IiII1III + '[/COLOR]'
  i1iI11i1IIi ( i1O00oo , url , 100102 , i11111I1I , fanart , 'Aired : ' + i1IiII1III , i1O00oo )
  if 77 - 77: O0OOOoOoo0 % Ii1IIIi1 - ooOOOoO % I11i1ii1 - oO0o / I1ii11iIi11i
def Ii1iI111 ( name , URL , iconimage , fanart ) :
 oO0OOoo0OO = Oo00OoOo ( URL )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , name in i1IIIII11I1IiI :
  for i11I in oOOoo0Oo :
   if i11I in oO0o0 :
    URL = 'http://www.watchseriesgo.to/link/' + oO0o0
    I11o0oO00oO0o0o0 ( name , URL , 100106 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( i1IIIII11I1IiI ) <= 0 :
  i1iI11i1IIi ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 51 - 51: I1111IIi * o0o00Oo0O / IIiIiII11i . ii1ii11IIIiiI % Ii1IIIi1 / oOo0O0Ooo
  if 9 - 9: oOo0O0Ooo % oOo0O0Ooo % IIiIiII11i
def I1I1i1I ( url , name ) :
 oo0oo = name
 oO0OOoo0OO = Oo00OoOo ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  IIi11IIiIii1 ( url , oo0oo )
 for url in i1I :
  IIi11IIiIii1 ( url , oo0oo )
 for url in ooOoO00 :
  IIi11IIiIii1 ( url , oo0oo )
  if 17 - 17: ii1ii11IIIiiI + o000O0o . oO0o - I1ii11iIi11i * Ii
def IIi11IIiIii1 ( url , season_name ) :
 if 'daclips.in' in url :
  iioOo0OoOOo0 ( url , season_name )
 elif 'filehoot.com' in url :
  iII11I1Ii1 ( url , season_name )
 elif 'allmyvideos.net' in url :
  o0o0 ( url , season_name )
 elif 'vidspot.net' in url :
  oOo0oO ( url , season_name )
 elif 'vodlocker' in url :
  IIi1IIIIi ( url , season_name )
 elif 'vidto' in url :
  OOOoO ( url , season_name )
  if 14 - 14: ooOOOoO . iI11I1II1I1I . ii . IIiIiII11i / I11i
  if 21 - 21: Ii / ooOoO0O00 + oOo0O0Ooo * Ii1IIIi1 . iiiiiiii1
def OOOoO ( url , season_name ) :
 oO0OOoo0OO = Oo00OoOo ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO , I1111i in i1IIIII11I1IiI :
  oo0oO ( OoO , season_name )
  if 10 - 10: IIiIiII11i . O0OOOoOoo0
  if 32 - 32: ii1ii11IIIiiI . I1111IIi . ii - oO0o + o000O0o
def o0o0 ( url , season_name ) :
 oO0OOoo0OO = Oo00OoOo ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO , I1111i in i1IIIII11I1IiI :
  oo0oO ( OoO , season_name )
  if 88 - 88: O0OOOoOoo0
def oOo0oO ( url , season_name ) :
 oO0OOoo0OO = Oo00OoOo ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0OOoo0OO )
 for OoO , I1111i in i1IIIII11I1IiI :
  oo0oO ( OoO , season_name )
  if 19 - 19: IIiIiII11i * I1111IIi + ii1ii11IIIiiI
def IIi1IIIIi ( url , season_name ) :
 oO0OOoo0OO = Oo00OoOo ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO in i1IIIII11I1IiI :
  oo0oO ( OoO , season_name )
  if 65 - 65: Ii1IIIi1 . iiiiiiii1 . oO0o . O0OOOoOoo0 - Ii1IIIi1
def iioOo0OoOOo0 ( url , season_name ) :
 oO0OOoo0OO = Oo00OoOo ( url )
 i1IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0OOoo0OO )
 for OoO in i1IIIII11I1IiI :
  oo0oO ( OoO , season_name )
  if 19 - 19: Ii + O0OOOoOoo0 % I11i1ii1
def iII11I1Ii1 ( url , season_name ) :
 oO0OOoo0OO = Oo00OoOo ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO in i1IIIII11I1IiI :
  oo0oO ( OoO , season_name )
  if 14 - 14: oO0o . IIiIiII11i . ooOOOoO / ii1ii11IIIiiI % Ii1I - I11i1ii1
def oo0oO ( Link , season_name ) :
 if 'http:/' in Link :
  o0oOoO0O ( Link )
  if 84 - 84: o0o00Oo0O * ii - I1111IIi * I1111IIi
def i1ii ( url ) :
 oO0OOoo0OO = OPEN_URL_1 ( url )
 oO0O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 for url in oO0O :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 86 - 86: OOooOOo . iI11I1II1I1I - oO0o
def i1iI11i1IIi ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I11I = True
 iIIII1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIII1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIII1i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o00oO0 = [ ]
  if 5 - 5: iI11I1II1I1I
  if showcontext == 'fav' :
   o00oO0 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o00oO0 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iIIII1i . addContextMenuItems ( o00oO0 )
 I11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO , listitem = iIIII1i , isFolder = True )
 return I11I
 if 72 - 72: o000O0o . iiiiiiii1 / OOooOOo + ooOOOoO % iI11I1II1I1I
 if 42 - 42: Ii1I * OOooOOo % I11i1ii1 - OOooOOo . Ii - iiiiiiii1
def I11o0oO00oO0o0o0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I11I = True
 iIIII1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIII1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIII1i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o00oO0 = [ ]
  o00oO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o00oO0 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o00oO0 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iIIII1i . addContextMenuItems ( o00oO0 )
 I11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO , listitem = iIIII1i , isFolder = False )
 return I11I
 if 84 - 84: iiiiiiii1 - Ii1I / ooOOOoO
def i1II111i1 ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 98 - 98: oO0o . ooOOOoO % IIiIiII11i
def O0OoOoO00O ( url ) :
 OooOOO0O00 = xbmc . Player ( IIii1i1iii1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : OooOOO0O00 . play ( url ) . strip ( )
 except : pass
 if 70 - 70: Ii % O0OOOoOoo0
def o0oOoO0O ( url ) :
 OooOOO0O00 = xbmc . Player ( )
 import urlresolver
 try : OooOOO0O00 . play ( url )
 except : pass
 if 11 - 11: I1111IIi % Ii1I % ii1ii11IIIiiI / IIiIiII11i % iiiiiiii1 - I1ii11iIi11i
def Oo00OoOo ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1Oo00 = ''
 i1i = ''
 try :
  i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
  i1i = i1Oo00 . read ( )
  i1Oo00 . close ( )
 except : pass
 if i1i != '' :
  return i1i
 else :
  i1i = 'Opened'
  return i1i
  if 96 - 96: Ii1I / IIiIiII11i . ii1ii11IIIiiI - O0OOOoOoo0 * ooOOOoO * o000O0o
  if 76 - 76: ii1ii11IIIiiI - IIiIiII11i * Ii1IIIi1 / ii
  if 18 - 18: oO0o + iI11I1II1I1I - IIiIiII11i - oOo0O0Ooo
def o0Oooo ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   ooo ( )
  if i11I1II1I11i == 1 :
   OOOO0oooo ( )
  if i11I1II1I11i == 2 :
   oooooOo0 ( )
  if i11I1II1I11i == 3 :
   O0o0O0OO00o ( )
  if i11I1II1I11i == 4 :
   OOo00O ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , III1iII1I1ii + 'SearchCartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( I1I1IiI1 ) , 21004 , III1iII1I1ii + 'watchcartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CARTOONS[/COLOR]' , '' , 10001 , III1iII1I1ii + 'Cartoons.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '' , 20000 , III1iII1I1ii + 'Cartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , III1iII1I1ii + 'anime.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def Iiii1iI1i ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']FOOTBALL[/COLOR]' , '' , 10002 , III1iII1I1ii + 'Football.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , III1iII1I1ii + 'Fitness.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']Go Fishing[/COLOR]' , str ( I1I1IiI1 ) , 8090 , III1iII1I1ii + 'GoFishing.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , III1iII1I1ii + 'GenieTVKitchen.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 81 - 81: I1111IIi . I11i / iiiiiiii1
 if 17 - 17: Ii - Ii1IIIi1 . I1111IIi % iI11I1II1I1I + ooOOOoO - I11i1ii1
 if 78 - 78: ooOOOoO * OOooOOo . o0o00Oo0O / o0o00Oo0O
def OO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 i1IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0OOoo0OO )
 for IIiIi1iI in i1IIIII11I1IiI :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   OooOOOo0 = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OO0O000 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + OooOOOo0 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   i11I1II1I11i = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if i11I1II1I11i == 0 :
    O0O0o0o0o ( IIiIi1iI )
    O0O0ooOOO ( )
   elif i11I1II1I11i == 1 :
    IIIIIiI ( IIiIi1iI )
  else :
   pass
   if 80 - 80: iI11I1II1I1I * iiiiiiii1 % ooOOOoO % I1ii11iIi11i
def IIIIIiI ( addon ) :
 OooOOOo0 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 95 - 95: iI11I1II1I1I - Ii1I . iiiiiiii1 - oOo0O0Ooo
def O0O0o0o0o ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 OOOOoo = os . path . join ( I11II1i , 'default.py' )
 o000OOooo0O = open ( OOOOoo , "w+" )
 if 34 - 34: Ii1IIIi1
 o000OOooo0O . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 o000OOooo0O . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 o000OOooo0O . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 11 - 11: oOo0O0Ooo * o000O0o + Ii1I / Ii1I
 if 37 - 37: Ii + ooOoO0O00
 if 23 - 23: O0OOOoOoo0 + ooOOOoO . OOooOOo * oOo0O0Ooo + Ii1I
 if 18 - 18: I1111IIi * I11i . I1111IIi / o0o00Oo0O
def iiIII1II ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 oOo00oOOOOO = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OoOOo0O00 = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 Iii1I1111ii = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIiI = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url , iiO0oOo00o , o0ooooO0o0O , ii1Oo0000oOo in oOo00oOOOOO :
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 90037 , iiO0oOo00o , o0ooooO0o0O , ii1Oo0000oOo )
  elif I1111i == 'Search' :
   iiOOooooO0Oo ( 'Search' , url , 90038 , iiO0oOo00o , o0ooooO0o0O , ii1Oo0000oOo )
  else :
   OOiIiIIi1 ( I1111i , url , 222 , iiO0oOo00o , o0ooooO0o0O , ii1Oo0000oOo )
 for I1111i , o00O0O , url , iIIIi1i1I11i in OoOOo0O00 :
  iiOOooooO0Oo ( I1111i , url , 90037 , o00O0O , iIIIi1i1I11i , '' )
 for I1111i , o00O0O , url , iIIIi1i1I11i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 90037 , o00O0O , iIIIi1i1I11i , '' )
 for I1111i , url , o00O0O , iIIIi1i1I11i in i1I :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , iIIIi1i1I11i , '' )
 for I1111i , url , o00O0O , iIIIi1i1I11i in ooOoO00 :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , iIIIi1i1I11i , '' )
 for I1111i , url , o00O0O , iIIIi1i1I11i in Iii1I1111ii :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , iIIIi1i1I11i , '' )
 for I1111i , url , o00O0O in iIiI :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , '' , '' )
  I1I11i ( 'tvshows' , 'Media Info 3' )
  if 55 - 55: I1ii11iIi11i - Ii1IIIi1
def O0OO0O ( ) :
 IiiiIiiI = [ 'serialsearch' , 'moviesearch' ]
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 if i1iIIi == '' :
  pass
 else :
  for oo0OO in IiiiIiiI :
   IiiI11i1I = I11 + oo0OO + '.php'
   oO0oOOoo00000 = OoOooO ( IiiI11i1I )
   if oO0oOOoo00000 != 'Opened' :
    iiiI1I1iIIIi1 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( oO0oOOoo00000 )
    for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O , ii1Oo0000oOo in iiiI1I1iIIIi1 :
     if i1iIIi in I1111i . lower ( ) :
      OOo0 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for i11I in OOo0 :
       if i11I == oO0o0 :
        I1111i = '[COLORred]* [/COLOR]' + ( I1111i ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        iiIii1IIi = open ( o00OO00OoO , "a" )
        iiIii1IIi . write ( 'item="' + I1111i + '"\n' )
        iiIii1IIi . close
      if 'php' in oO0o0 :
       iiOOooooO0Oo ( I1111i , oO0o0 , 90037 , iiO0oOo00o , o0ooooO0o0O , ii1Oo0000oOo )
      else :
       OOiIiIIi1 ( I1111i , oO0o0 , 222 , iiO0oOo00o , o0ooooO0o0O , ii1Oo0000oOo )
       if 10 - 10: Ii - I11i % iI11I1II1I1I
   I1I11i ( 'tvshows' , 'Media Info 3' )
   if 49 - 49: o000O0o
def OOOOoOo00OO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://www.tvcatchup.com/channels/' )
 O0 = OoOooO ( 'http://www.djing.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OooOo0o0Oo = re . compile ( 'title="([^"]*)" >.+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( O0 )
 for IIiiiiiiIi1I1 , o00O0O , oO0o0 in i1IIIII11I1IiI :
  i1iIiiiiii1II ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + oO0o0 , 90024 , 'http://www.tvcatchup.com' + o00O0O )
 for IIiiiiiiIi1I1 , oO0o0 , o00O0O in OooOo0o0Oo :
  i1iIiiiiii1II ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + oO0o0 , 90024 , o00O0O )
 for oO0o0 , o00O0O , I1111i in i1I :
  if 'Submit' in I1111i :
   pass
  elif '&lt;' in I1111i :
   pass
  else :
   OOiIiIIi1 ( 'DJing  ' + I1111i , oO0o0 , 90025 , 'http://www.djing.com' + o00O0O , O0o0Oo , '' )
  I1I11i ( 'movies' , 'MAIN' )
def OooO0oOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 if 66 - 66: oO0o * I1ii11iIi11i
 i1IIIII11I1IiI = re . compile ( "file: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def II1IIIiiI11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 86 - 86: oO0o % ii % oO0o / oOo0O0Ooo
def o0o0O ( ) :
 if 56 - 56: ii % Ii * iI11I1II1I1I . oO0o * o0o00Oo0O
 if 23 - 23: Ii
 if 39 - 39: I11i - Ii1I % O0OOOoOoo0 * oO0o - Ii1IIIi1 / O0OOOoOoo0
 if 29 - 29: Ii1I
 if 52 - 52: Ii / ooOoO0O00
 if 1 - 1: I11i1ii1
 oO0OOoo0OO = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'yr' in oO0o0 :
   IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + oO0o0 , 10201 , III1iII1I1ii + 'rated.png' )
   if 78 - 78: Ii1I + ooOOOoO - o0o00Oo0O
def i1I1iIi1IiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1111O0O000OOOo , url , I1111i in i1IIIII11I1IiI :
  if 'id' in url :
   IiiIiI1Ii1i ( ( '[COLORred]RANK [COLORblue]' + i1111O0O000OOOo + '[COLORred] - [COLORblue]' + I1111i + '[/COLOR]' ) , I1111i , 10202 , III1iII1I1ii + 'rated.png' )
   if 12 - 12: o000O0o
def Oo0O ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 Ii11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o00O = ( url )
 i1iIIi = o00O . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( o00O ) . replace ( ' ' , '+' )
 oOOo0oo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 II1i111 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1iiiIii11 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OOoOOO000O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oOo0II1i11I1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiIiIiII = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o00O
 i1I1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 10 - 10: oO0o / I1ii11iIi11i
 I1iII11iIII1i1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oOO0oo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 13 - 13: ii * o000O0o - ii1ii11IIIiiI / Ii1IIIi1 + ooOOOoO + I1111IIi
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( oOOo0oo0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1i111 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( i1iiiIii11 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 iii1III1i = O0o0O00Oo0o0 ( OOoOOO000O0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iiiIi = O0o0O00Oo0o0 ( iiIiIiII )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 II1Iii = O0o0O00Oo0o0 ( i1I1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0oooo0OoO0oo = O0o0O00Oo0o0 ( iIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 16 - 16: oOo0O0Ooo * IIiIiII11i / iI11I1II1I1I - O0OOOoOoo0
 if 3 - 3: oOo0O0Ooo * I11i1ii1 + IIiIiII11i - oO0o
 OOOOOoOO0OOoo = O0o0O00Oo0o0 ( I1iII11iIII1i1I )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 IIIi11IiIiii = O0o0O00Oo0o0 ( oOO0oo )
 if 38 - 38: I1ii11iIi11i - ooOOOoO . I1ii11iIi11i
 if 38 - 38: ooOoO0O00 + ii1ii11IIIiiI
 if 91 - 91: IIiIiII11i % O0OOOoOoo0 % I1111IIi + IIiIiII11i / o000O0o
 if 62 - 62: ii - Ii
 if 5 - 5: iI11I1II1I1I / ooOOOoO / ooOoO0O00 % ii
 if 50 - 50: ii1ii11IIIiiI / OOooOOo * ii1ii11IIIiiI
 if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + O0OOOoOoo0 * iI11I1II1I1I % ii1ii11IIIiiI
 if 25 - 25: ooOOOoO + OOooOOo . I11i % OOooOOo * Ii1IIIi1
 if 32 - 32: Ii - iiiiiiii1
 if 53 - 53: ii - I1111IIi
 if 87 - 87: o000O0o . oOo0O0Ooo
 if 17 - 17: ii1ii11IIIiiI . Ii
 if 5 - 5: Ii1I + o0o00Oo0O + o0o00Oo0O . iiiiiiii1 - I11i1ii1
 if O0oooo0OoO0oo != 'Failed' :
  o00oo0000 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0oooo0OoO0oo )
  for url , I1111i in o00oo0000 :
   iIi1IIi1ii = O0o0O00Oo0o0 ( url )
   I11Ii = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi1IIi1ii )
   for iIiII , i1i1IIIIIIIi in I11Ii :
    i1i1IIIIIIIi = ( i1i1IIIIIIIi . replace ( '.' , ' ' ) )
    if i1iIIi in i1i1IIIIIIIi . lower ( ) :
     if '.mkv' in iIiII :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiII , 222 , '' , '' , '' )
     elif '.mp4' in iIiII :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiII , 222 , '' , '' , '' )
     elif '.avi' in iIiII :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiII , 222 , '' , '' , '' )
     elif '.wav' in iIiII :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiII , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiII , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 65 - 65: I11i
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for url , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in i1I :
   if o00O in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 7 - 7: I1111IIi . OOooOOo / Ii1I . Ii1IIIi1 * ooOOOoO - IIiIiII11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 37 - 37: iiiiiiii1 . OOooOOo / o0o00Oo0O * O0OOOoOoo0
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for III11iiii11i1 , I1111i in ooOoO00 :
   if o00O in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( II1i111 + III11iiii11i1 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for url , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in Iii1I1111ii :
   if o00O in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 54 - 54: ooOoO0O00 - o000O0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1III1i != 'Failed' :
  IiIIII = [ ]
  iIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iii1III1i )
  for url , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in iIiI :
   if o00O in I1111i . lower ( ) :
    if I1111i in IiIIII :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
     IiIIII . append ( I1111i )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if iiiIi != 'Failed' :
  oOOo = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iiiIi )
  for url , o00O0O , I1111i in oOOo :
   if o00O in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 100 - 100: oOo0O0Ooo + oOo0O0Ooo * I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 77 - 77: o000O0o % ooOoO0O00 - ii1ii11IIIiiI
    if 93 - 93: oO0o * I1ii11iIi11i
    if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * Ii1IIIi1 % IIiIiII11i
    if 56 - 56: ii * I1ii11iIi11i . I1ii11iIi11i . Ii1I
    if 24 - 24: I1ii11iIi11i . ooOOOoO * ii1ii11IIIiiI % O0OOOoOoo0 / Ii1IIIi1
    if 58 - 58: oOo0O0Ooo - Ii1I % o0o00Oo0O . oOo0O0Ooo % oO0o % I1111IIi
    if 87 - 87: o000O0o - Ii
    if 78 - 78: Ii / iI11I1II1I1I - I11i
    if 23 - 23: ooOOOoO
    if 40 - 40: I11i - IIiIiII11i / I1ii11iIi11i
    if 14 - 14: Ii1I
    if 5 - 5: I11i . iI11I1II1I1I % iI11I1II1I1I
    if 56 - 56: ii - ooOOOoO - ooOoO0O00
    if 8 - 8: iiiiiiii1 / Ii1IIIi1 . oOo0O0Ooo + Ii1I / Ii
    if 31 - 31: I11i1ii1 - iI11I1II1I1I + O0OOOoOoo0 . I1ii11iIi11i / I1111IIi % iI11I1II1I1I
    if 6 - 6: I1111IIi * Ii % iI11I1II1I1I % Ii + I11i / ooOoO0O00
    if 53 - 53: ooOOOoO + iI11I1II1I1I
    if 70 - 70: Ii1I
 if OOOOOoOO0OOoo != 'Failed' :
  oo0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOOOoOO0OOoo )
  for url , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in oo0O :
   if o00O in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 6 - 6: I1ii11iIi11i . I1111IIi / I1111IIi - Ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 87 - 87: I1ii11iIi11i / o0o00Oo0O * I1111IIi / I11i
    if 19 - 19: iiiiiiii1 + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
    if 16 - 16: o000O0o + I11i1ii1 / I11i
    if 82 - 82: I1111IIi * Ii % IIiIiII11i - ii
    if 90 - 90: I1ii11iIi11i . o000O0o * ooOoO0O00 - ooOoO0O00
    if 16 - 16: oOo0O0Ooo * ooOoO0O00 - I11i . I1111IIi % ooOOOoO / I11i
    if 14 - 14: iI11I1II1I1I * iiiiiiii1 * Ii1I / iI11I1II1I1I * I1111IIi / ooOOOoO
    if 77 - 77: oO0o + iiiiiiii1 + iiiiiiii1 * ii1ii11IIIiiI / ii . ii1ii11IIIiiI
    if 62 - 62: ooOoO0O00 - ooOoO0O00
    if 69 - 69: OOooOOo % o000O0o - ooOOOoO
 Iiii1ii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 42 - 42: ii1ii11IIIiiI * iiiiiiii1 . I1111IIi * oOo0O0Ooo + OOooOOo
 for oo0OO in Iiii1ii :
  IiiI11i1I = O0Oo000ooO00 + oo0OO + I1IIIii
  O0oooo0OoO0oo = O0o0O00Oo0o0 ( IiiI11i1I )
  if O0oooo0OoO0oo != 'Failed' :
   o00oo0000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0oooo0OoO0oo )
   for url , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in o00oo0000 :
    if o00O in I1111i . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 25 - 25: ooOOOoO . oOo0O0Ooo + o000O0o
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 75 - 75: I1111IIi - I11i % O0OOOoOoo0 + Ii
 Iiii1ii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 100 - 100: ooOOOoO + I11i - Ii - IIiIiII11i
 if 40 - 40: OOooOOo % oO0o
 for oo0OO in Iiii1ii :
  IiiI11i1I = Ii11 + oo0OO
  oo0O0o00 = O0o0O00Oo0o0 ( IiiI11i1I )
  if oo0O0o00 != 'Failed' :
   oOoO0o = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0O0o00 )
   for III11iiii11i1 , I1111i in oOoO0o :
    if o00O in I1111i . lower ( ) :
     i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( Ii11 + oo0OO + III11iiii11i1 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 46 - 46: iiiiiiii1 % ii1ii11IIIiiI
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 72 - 72: iI11I1II1I1I
def IIiI1 ( ) :
 IiiIiI1Ii1i ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , III1iII1I1ii + 'running.png' )
 IiiIiI1Ii1i ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , III1iII1I1ii + 'countdown.png' )
 IiiIiI1Ii1i ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , III1iII1I1ii + 'unknown.png' )
 IiiIiI1Ii1i ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , III1iII1I1ii + 'cancelled.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 45 - 45: I1ii11iIi11i - I11i % iiiiiiii1
def i1IIi1i1Ii1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , IiI1i , Iiio0Oo0oO , i1IiII1III , iI in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLORblue]' + I1111i + '[/COLOR] [COLORred]Season[/COLOR]-' + IiI1i + ' [COLORred]Returns [/COLOR]- ' + iI + ' ' + i1IiII1III ) , I1111i , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 25 - 25: Ii1I - Ii % Ii1IIIi1 . Ii
def Oo0oOo0O0O0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , IiI1i , Iiio0Oo0oO in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLORblue]' + I1111i + '[/COLOR] [COLORred]Season[/COLOR]-' + IiI1i + ' [COLORred] Status Unknown[/COLOR] ' ) , I1111i , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 46 - 46: o0o00Oo0O * I1ii11iIi11i / o0o00Oo0O + oO0o
def o0oOOo0O0O000 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , IiI1i , Iiio0Oo0oO , i1IiII1III in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLORblue]' + I1111i + ' [COLORred] Cancelled On[/COLOR] ' + i1IiII1III ) , I1111i , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 29 - 29: I11i / I1ii11iIi11i * Ii1I . I11i
def oO00 ( url ) :
 o00O = ( url )
 i1iIIi = o00O . lower ( )
 if 1 - 1: o000O0o
 if 12 - 12: I11i1ii1 % oOo0O0Ooo + o000O0o - ooOoO0O00 . ii1ii11IIIiiI / oOo0O0Ooo
 iIiII = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( o00O ) . replace ( ' ' , '+' )
 oOOo0oo0O = 'http://onlinemovies.tube/?s=' + ( o00O ) . replace ( ' ' , '+' )
 II1i111 = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i1iiiIii11 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oOo0II1i11I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 51 - 51: Ii1IIIi1 . oOo0O0Ooo
 i1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 34 - 34: iiiiiiii1 % o000O0o % OOooOOo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 63 - 63: oOo0O0Ooo - oO0o % O0OOOoOoo0 % ooOOOoO / I11i / ooOoO0O00
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 69 - 69: I1ii11iIi11i * IIiIiII11i * I11i1ii1 . O0OOOoOoo0 - Ii1I
 if 39 - 39: ii1ii11IIIiiI * oOo0O0Ooo % oO0o . OOooOOo
 iiii111IiIIi1 = O0o0O00Oo0o0 ( iIiII )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( oOOo0oo0O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1i111 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( i1iiiIii11 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 oo0O0o00 = O0o0O00Oo0o0 ( oOo0II1i11I1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 74 - 74: iI11I1II1I1I % O0OOOoOoo0 * Ii1IIIi1 * iI11I1II1I1I
 if 73 - 73: I11i % iiiiiiii1 . Ii1IIIi1
 II1Iii = O0o0O00Oo0o0 ( i1I1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 O0oooo0OoO0oo = O0o0O00Oo0o0 ( iIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 ooOOoOo = O0o0O00Oo0o0 ( Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 90 - 90: IIiIiII11i / oOo0O0Ooo
 if O0oooo0OoO0oo != 'Failed' :
  o00oo0000 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0oooo0OoO0oo )
  for url , I1111i in o00oo0000 :
   iIi1IIi1ii = O0o0O00Oo0o0 ( url )
   I11Ii = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi1IIi1ii )
   for iIiII , i1i1IIIIIIIi in I11Ii :
    if i1iIIi in i1i1IIIIIIIi . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiII , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 45 - 45: iI11I1II1I1I
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if II1Iii != 'Failed' :
  iIiIii1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II1Iii )
  for url , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in iIiIii1ii :
   if i1iIIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 43 - 43: Ii1I - O0OOOoOoo0
    if 70 - 70: O0OOOoOoo0 / Ii1IIIi1 % I11i1ii1 - ii1ii11IIIiiI
    if 47 - 47: O0OOOoOoo0
    if 92 - 92: Ii1IIIi1 + OOooOOo % ooOoO0O00
    if 23 - 23: iiiiiiii1 - Ii1IIIi1 + ii1ii11IIIiiI - OOooOOo * OOooOOo . I1ii11iIi11i
    if 47 - 47: o000O0o % iI11I1II1I1I
    if 11 - 11: oOo0O0Ooo % ii1ii11IIIiiI - oO0o - o000O0o + I11i
    if 98 - 98: O0OOOoOoo0 + ii1ii11IIIiiI - oO0o
    if 79 - 79: Ii1IIIi1 / iiiiiiii1 . OOooOOo - Ii1I
    if 47 - 47: ii % o0o00Oo0O * O0OOOoOoo0 . ii1ii11IIIiiI
    if 38 - 38: o0o00Oo0O - I1111IIi % iiiiiiii1
 if ooOOoOo != 'Failed' :
  ooOI1iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOOoOo )
  for url , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in ooOI1iI :
   if i1iIIi in I1111i . lower ( ) :
    IiiIiI1Ii1i ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , OOoOooOoOOOoo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 92 - 92: oO0o * I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  i1iIIi1o0o0OoOOOOOo = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for url , o00O0O , I1111i , Ii11iii1II1i in i1I :
   if i1iIIi in I1111i . lower ( ) :
    if 'season' in Ii11iii1II1i :
     IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , o00O0O , o00O0O , '' )
    if 'episodes' in Ii11iii1II1i :
     IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , o00O0O , o00O0O , '' )
  for url in i1iIIi1o0o0OoOOOOOo :
   IiiIiI1Ii1i ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 65 - 65: ii1ii11IIIiiI + oO0o - ii
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if iiii111IiIIi1 != 'Failed' :
  OoOOo0O00 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( iiii111IiIIi1 )
  for url , I1111i , o00O0O in OoOOo0O00 :
   if i1iIIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 51 - 51: I1ii11iIi11i + o000O0o / O0OOOoOoo0 - ooOoO0O00
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 51 - 51: I1ii11iIi11i - Ii1I * ooOOOoO
    if 12 - 12: iI11I1II1I1I % I11i1ii1 % I11i1ii1
    if 78 - 78: I1111IIi . OOooOOo . ooOOOoO
    if 97 - 97: o000O0o
    if 80 - 80: oOo0O0Ooo . ii1ii11IIIiiI
    if 47 - 47: ooOOOoO + I11i1ii1 + IIiIiII11i % Ii
    if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / O0OOOoOoo0 * o000O0o
    if 29 - 29: I11i
    if 86 - 86: IIiIiII11i . I1111IIi
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for I1111i in ooOoO00 :
   if i1iIIi in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( II1i111 + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 2 - 2: ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for I1111i in Iii1I1111ii :
   if i1iIIi in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i1iiiIii11 + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 60 - 60: oO0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0O0o00 != 'Failed' :
  oOoO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0O0o00 )
  for url , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in oOoO0o :
   if i1iIIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 81 - 81: OOooOOo % ii1ii11IIIiiI
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 87 - 87: iI11I1II1I1I . ii * OOooOOo
 OOOo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oo0OO in OOOo :
  IiiI11i1I = O0Oo000ooO00 + oo0OO + I1IIIii
  OOOOOoOO0OOoo = O0o0O00Oo0o0 ( IiiI11i1I )
  if OOOOOoOO0OOoo != 'Failed' :
   oo0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOOOOoOO0OOoo )
   for I1111i , ii1Oo0000oOo , url , o00O0O , o0ooooO0o0O , ii1ii111 in oo0O :
    if i1iIIi in I1111i . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , url , ii1ii111 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 74 - 74: ii1ii11IIIiiI - ii . I1ii11iIi11i
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 31 - 31: I11i % ooOOOoO + iI11I1II1I1I + Ii * iiiiiiii1
     if 45 - 45: Ii1IIIi1 * iiiiiiii1 . I11i1ii1 - iiiiiiii1 + I1111IIi
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: Ii1IIIi1 . I1ii11iIi11i
def I1ii11 ( ) :
 if 78 - 78: Ii1I % oOo0O0Ooo / ii % Ii1IIIi1 - O0OOOoOoo0
 if 2 - 2: iI11I1II1I1I
 if 45 - 45: ii / Ii
 if 10 - 10: O0OOOoOoo0 - o000O0o * iI11I1II1I1I % iI11I1II1I1I * I1111IIi - Ii1I
 if 97 - 97: IIiIiII11i % iiiiiiii1 + iiiiiiii1 - oO0o / ii1ii11IIIiiI * oOo0O0Ooo
 if 17 - 17: ii1ii11IIIiiI
 if 39 - 39: I11i1ii1 . IIiIiII11i
 if 45 - 45: o000O0o * OOooOOo / iI11I1II1I1I
 if 77 - 77: iiiiiiii1 - ooOOOoO
 if 11 - 11: Ii1I
 if 26 - 26: iI11I1II1I1I * iiiiiiii1 - Ii1IIIi1
 IiiIiI1Ii1i ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , III1iII1I1ii + 'seasons.png' )
 IiiIiI1Ii1i ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , III1iII1I1ii + 'episodes.png' )
 IiiIiI1Ii1i ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 27 - 27: Ii1I * iiiiiiii1 - oO0o + ii1ii11IIIiiI * ii1ii11IIIiiI
def o0OO0O0OO0oO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , iIiiIi11IIi in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( I1111i + ' - ' + iIiiIi11IIi ) . replace ( '&amp;' , '&' ) , url , 90053 , III1iII1I1ii + 'seasons.png' )
  if 64 - 64: ii . Ii1I % o0o00Oo0O + oOo0O0Ooo - I11i
def ooo0oo00O00oO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , url , 90054 , III1iII1I1ii + 'episodes.png' )
  if 93 - 93: iI11I1II1I1I
def oo0oooo0OoO0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , url , 90054 , o00O0O )
 for url in next :
  IiiIiI1Ii1i ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 50 - 50: O0OOOoOoo0 / O0OOOoOoo0 + Ii1IIIi1 * I11i1ii1 / Ii1I
def I1IIiiI1II1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for o00O0O , iIiiIi11IIi , url , I1111i , iI1iIiiiI1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iIiiIi11IIi + ' - ' + I1111i + ' - ' + iI1iIiiiI1I1 , url , 90044 , o00O0O , o00O0O , '' )
 for o00O0O , I1111i , url in i1I :
  IiiIiI1Ii1i ( I1111i , url , 90044 , o00O0O , o00O0O , '' )
 for url in next :
  IiiIiI1Ii1i ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 78 - 78: o000O0o / oO0o - o000O0o * ii . OOooOOo
def OOoooOoO0Oo ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo000 = 'http://onlinemovies.tube/?s=' + ( o00O ) . replace ( ' ' , '+' )
 i1iIIi = Oo000 . lower ( )
 oO0OOoo0OO = OoOooO ( i1iIIi )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i , Ii11iii1II1i in i1IIIII11I1IiI :
  if 'season' in Ii11iii1II1i :
   IiiIiI1Ii1i ( I1111i , oO0o0 , 90054 , o00O0O , o00O0O , '' )
  if 'episodes' in Ii11iii1II1i :
   IiiIiI1Ii1i ( I1111i , oO0o0 , 90044 , o00O0O , o00O0O , '' )
 for oO0o0 in next :
  IiiIiI1Ii1i ( 'NEXT' , oO0o0 , 90053 , III1iII1I1ii + 'Next.png' )
  if 48 - 48: Ii % o000O0o
def ooooO0oOoOOoO ( ) :
 if 29 - 29: O0OOOoOoo0 + Ii % ooOOOoO
 if 93 - 93: OOooOOo % iI11I1II1I1I
 if 90 - 90: oOo0O0Ooo - Ii1IIIi1 / ii1ii11IIIiiI / o0o00Oo0O / ooOOOoO
 if 87 - 87: OOooOOo / I1111IIi + iI11I1II1I1I
 if 93 - 93: iI11I1II1I1I + o000O0o % I11i1ii1
 if 21 - 21: Ii1IIIi1
 if 6 - 6: I1111IIi
 if 46 - 46: I1111IIi + o000O0o
 if 79 - 79: ii - I1111IIi * I1111IIi . OOooOOo
 if 100 - 100: IIiIiII11i * ooOOOoO % oOo0O0Ooo / Ii1I
 IiiIiI1Ii1i ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , III1iII1I1ii + 'allmov.png' )
 IiiIiI1Ii1i ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , III1iII1I1ii + 'Genre.png' )
 IiiIiI1Ii1i ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , III1iII1I1ii + 'Years.png' )
 IiiIiI1Ii1i ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 90 - 90: Ii1I . I11i1ii1 . OOooOOo . ii1ii11IIIiiI
def I11IiIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , iIiiIi11IIi in i1IIIII11I1IiI :
  if 'genre' in url :
   IiiIiI1Ii1i ( ( I1111i + ' - ' + iIiiIi11IIi ) . replace ( '&amp;' , '&' ) , url , 90043 , III1iII1I1ii + 'Genre.png' )
   if 74 - 74: IIiIiII11i . o0o00Oo0O - oOo0O0Ooo + I1111IIi % Ii % OOooOOo
def O0OOO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if 'release' in url :
   IiiIiI1Ii1i ( I1111i , url , 90043 , III1iII1I1ii + 'Years.png' )
   if 8 - 8: Ii / IIiIiII11i + I11i * ii1ii11IIIiiI % I1111IIi . ooOOOoO
def I1iIIIiIi1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , IiI1 , url , ii1Oo0000oOo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' ' + IiI1 , url , 90044 , o00O0O , o00O0O , ii1Oo0000oOo )
 for o00O0O , I1111i , Ii11iii1II1i , url , O0oO , ii1Oo0000oOo in i1I :
  if 'movies' in Ii11iii1II1i :
   iiOOooooO0Oo ( I1111i + ' - ' + O0oO , url , 90044 , o00O0O , o00O0O , ii1Oo0000oOo )
 for url in next :
  IiiIiI1Ii1i ( 'NEXT' , url , 90043 , III1iII1I1ii + 'Next.png' )
  if 27 - 27: o0o00Oo0O / OOooOOo + iI11I1II1I1I - Ii1IIIi1 % I11i
def I111i1Ii1i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  iI1IIi1IiI ( 'http:' + url )
  if 45 - 45: o0o00Oo0O / ooOoO0O00 * o000O0o * oO0o
def iI1IIi1IiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( I1111i ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , III1iII1I1ii + 'movhub.png' )
def II11I ( ) :
 if 31 - 31: ii1ii11IIIiiI
 if 18 - 18: I11i1ii1 + ii1ii11IIIiiI
 if 5 - 5: ii + ooOOOoO * IIiIiII11i
 if 98 - 98: Ii1IIIi1 % ooOoO0O00 . oOo0O0Ooo . IIiIiII11i . Ii1I / Ii
 if 32 - 32: I11i + oOo0O0Ooo . iiiiiiii1
 if 41 - 41: OOooOOo . Ii / ooOOOoO
 if 98 - 98: OOooOOo % IIiIiII11i
 if 95 - 95: iI11I1II1I1I - iiiiiiii1 - Ii1IIIi1 + iiiiiiii1 % Ii1I . oOo0O0Ooo
 if 41 - 41: o0o00Oo0O + o000O0o . ooOoO0O00 - IIiIiII11i * I11i . oO0o
 if 68 - 68: I11i
 if 20 - 20: iiiiiiii1 - iiiiiiii1
 if 37 - 37: I1111IIi
 if 37 - 37: I1ii11iIi11i / I1111IIi * o0o00Oo0O
 if 73 - 73: O0OOOoOoo0 * O0OOOoOoo0 / I11i1ii1
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo000 = 'http://onlinemovies.tube/?s=' + ( o00O ) . replace ( ' ' , '+' )
 i1iIIi = Oo000 . lower ( )
 oO0OOoo0OO = OoOooO ( i1iIIi )
 i1IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i , IIi in i1IIIII11I1IiI :
  if 'movies' in IIi :
   IiiIiI1Ii1i ( IIi + '-' + I1111i , oO0o0 , 90044 , o00O0O )
 for oO0o0 in next :
  I1iIIIiIi1 ( oO0o0 )
  if 21 - 21: I11i1ii1 * I11i1ii1 . ii1ii11IIIiiI
def IiIi ( ) :
 IiiIiI1Ii1i ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 oO0OOoo0OO = OoOooO ( 'http://www.join4films.com/' )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , oO0o0 , 80006 , III1iII1I1ii + 'Desi.png' )
def iII11iiIIi11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oO0OOoo0OO )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( I1111i , url , 80007 , o00O0O )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def Iiii11I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  OOOOo0o00OO0000 ( url )
def OO0ooo0 ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo000 = 'http://www.join4films.com/?s=' + ( o00O ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1iIIi = Oo000 . lower ( )
 iII11iiIIi11 ( i1iIIi )
 if 7 - 7: Ii1I - o000O0o * Ii1IIIi1 + I11i . Ii1I
 if 85 - 85: o0o00Oo0O
 if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * ii1ii11IIIiiI
 if 19 - 19: ii1ii11IIIiiI
 if 55 - 55: Ii1IIIi1 % Ii1IIIi1 / o0o00Oo0O % O0OOOoOoo0 - I11i . I1ii11iIi11i
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
 if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
 if 8 - 8: OOooOOo * I1ii11iIi11i / I1111IIi % ii1ii11IIIiiI - oOo0O0Ooo
 if 71 - 71: O0OOOoOoo0
 if 23 - 23: ooOoO0O00 . iI11I1II1I1I . Ii1IIIi1 . o0o00Oo0O % ii1ii11IIIiiI % Ii
 if 11 - 11: o0o00Oo0O - IIiIiII11i . Ii1IIIi1 . ii1ii11IIIiiI % iiiiiiii1
 if 21 - 21: I1ii11iIi11i / O0OOOoOoo0 . iiiiiiii1 * ii + ooOOOoO - ooOoO0O00
 if 58 - 58: Ii1I
 if 2 - 2: IIiIiII11i / iiiiiiii1
 if 54 - 54: ooOoO0O00 . ooOOOoO - Ii1I + I11i1ii1 + I1ii11iIi11i / I1ii11iIi11i
 if 22 - 22: I11i1ii1 . iI11I1II1I1I
 if 12 - 12: ii1ii11IIIiiI
def Ooii1IIi1ii ( ) :
 iiOOooooO0Oo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 if 85 - 85: ii % OOooOOo * iI11I1II1I1I
def IiI ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo000 = 'http://imoviemax.se/?s=' + ( o00O ) . replace ( ' ' , '+' )
 i1iIIi = Oo000 . lower ( )
 o0o0OO0o00o0O ( i1iIIi )
def IIIIIIi1i ( url ) :
 iiiii11I1 = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , Ii1 in i1IIIII11I1IiI :
  if I1111i in iiiii11I1 :
   pass
  else :
   iiOOooooO0Oo ( I1111i + ' - ' + Ii1 + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
   iiiii11I1 . append ( I1111i )
   if 77 - 77: Ii1IIIi1 / IIiIiII11i + I1111IIi + I11i1ii1 - Ii
def IiIIiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , oOo0Oo0O0O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' - Views:' + oOo0Oo0O0O , url , 10075 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
  if 48 - 48: I1ii11iIi11i - I11i1ii1 + I1ii11iIi11i - oOo0O0Ooo * Ii . O0OOOoOoo0
  if 35 - 35: I1111IIi . o0o00Oo0O + I1ii11iIi11i + Ii1IIIi1 + ooOoO0O00
def o0o0OO0o00o0O ( url ) :
 OooOooO0O0o0 = [ ]
 oO0OOoo0OO = OoOooO ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0OOoo0OO )
 for next in next :
  iiOOooooO0Oo ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10075 , o00O0O , o00O0O , '' )
  OooOooO0O0o0 . append ( I1111i )
  if 59 - 59: I1ii11iIi11i + O0OOOoOoo0 - Ii1IIIi1 . I11i + oOo0O0Ooo % o000O0o
def i111Iii ( img , name , url ) :
 img = img
 name = name
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oO0OOoo0OO )
 for o0o0i1 , url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iIi1IIiIII1 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iIi1IIiIII1
  i1Ii11I1II = ( o0o0i1 ) . replace ( 'play-' , 'Server ' )
  OOiIiIIi1 ( i1Ii11I1II , iIi1IIiIII1 , 10076 , img , img , '' )
  if 77 - 77: o000O0o - I1ii11iIi11i - iI11I1II1I1I
def IIi1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oO0OOoo0OO )
 for oOOo0oo0O in i1IIIII11I1IiI :
  if '=m' in oOOo0oo0O :
   iIiIIiii1II ( oOOo0oo0O )
  elif 'php' in oOOo0oo0O :
   IIi1i ( url )
  else :
   oO0OOoo0OO = OoOooO ( oOOo0oo0O )
   i1IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( oO0OOoo0OO )
   for II1i111 in i1IIIII11I1IiI :
    iIiIIiii1II ( oOOo0oo0O )
    if 44 - 44: ii . IIiIiII11i . Ii1IIIi1 % ii
    if 86 - 86: Ii + o0o00Oo0O * I1111IIi - oO0o * Ii1IIIi1 + o0o00Oo0O
    if 95 - 95: iI11I1II1I1I . iiiiiiii1 % O0OOOoOoo0 - iiiiiiii1 * IIiIiII11i
def o0oooOoo0OoOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 II111 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1IiII1III , o0o0O0O000 in II111 :
  print 'there ><><><><><><><><><><><><'
  i1IiII1III = i1IiII1III
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0o0O0O000 ) )
  for I1111i , I1I1i in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + i1IiII1III + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + I1I1i + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
 III11II1I1Ii1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1IiII1III , O0O0oo in III11II1I1Ii1 :
  print 'there ><><><><><><><><><><><><'
  i1IiII1III = i1IiII1III
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( O0O0oo ) )
  for I1111i , I1I1i in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + i1IiII1III + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + I1I1i + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
   if 83 - 83: I1111IIi / iiiiiiii1
   if 64 - 64: oO0o % I1111IIi . iiiiiiii1 % oO0o + ooOOOoO * I1111IIi
   if 83 - 83: I11i % o000O0o + ooOOOoO % Ii + o0o00Oo0O
def ii1I1IiiI1ii1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 III11II1I1Ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for III11II1I1Ii1 in III11II1I1Ii1 :
  I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( III11II1I1Ii1 ) )
  for I1111i in I1111i :
   I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( III11II1I1Ii1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  i11111I1I = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( III11II1I1Ii1 ) )
  for i11111I1I in i11111I1I :
   i11111I1I = 'http:' + i11111I1I
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11111I1I , '' , '' )
  if 65 - 65: iI11I1II1I1I % o000O0o + o0o00Oo0O / ii
  if 52 - 52: ii1ii11IIIiiI % Ii1IIIi1 * oOo0O0Ooo % ooOOOoO + Ii1IIIi1 / O0OOOoOoo0
  if 80 - 80: ii + I1111IIi
  if 95 - 95: iiiiiiii1 / o000O0o * iiiiiiii1 - ii * ii % oO0o
def OOOOO0O00 ( url ) :
 if 43 - 43: I1ii11iIi11i . iiiiiiii1
 I1I1i1i = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOOo0oo0O , o00O0O , I1111i , OOo0O in i1IIIII11I1IiI :
  I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = OoOooO ( oOOo0oo0O )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for oO0O , o000 in i1I :
   oOOoooO0O0 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( o000 ) )
   for ii1Oo0000oOo in oOOoooO0O0 :
    if I1111i in I1I1i1i :
     pass
    else :
     OOiIiIIi1 ( I1111i , oO0O , 8043 , o00O0O , o00O0O , ii1Oo0000oOo )
     I1I11i ( 'movies' , 'INFO' )
     I1I1i1i . append ( I1111i )
     if 46 - 46: iI11I1II1I1I
     if 33 - 33: ooOOOoO % ooOOOoO % o0o00Oo0O / oOo0O0Ooo . ooOoO0O00
def O0O0ooOoOO0OO ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , OOoOooOoOOOoo , ii1Oo0000oOo , o0ooooO0o0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10065 , OOoOooOoOOOoo , o0ooooO0o0O , ii1Oo0000oOo )
 I1I11i ( 'movies' , 'INFO' )
 if 27 - 27: I1111IIi * oOo0O0Ooo . iI11I1II1I1I - iI11I1II1I1I
def i111i1I1ii1i ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo000 = 'https://www.youtube.com/results?search_query=' + ( o00O ) . replace ( ' ' , '+' )
 i1iIIi = Oo000 . lower ( )
 oO0OOoo0OO = OoOooO ( i1iIIi )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 in next :
  oO0o0 = 'https://www.youtube.com' + oO0o0
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , oO0o0 , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for o00O0O , oO0o0 , I1111i , O0Oooo , o000 in i1IIIII11I1IiI :
  OOOO . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  i11111I1I = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i11111I1I
  oO0o0 = 'http://www.youtube.com' + oO0o0
  OOiIiIIi1 ( '[COLORred]' + O0Oooo + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11111I1I , i11111I1I , o000 )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o00O0O , oO0o0 , I1111i , O0Oooo in i1IIIII11I1IiI :
   print 'im doing it'
   I1I11i ( 'tvshows' , 'INFO' )
   i11111I1I = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   oO0o0 = 'http://www.youtube.com' + oO0o0
   if '&' in oO0o0 :
    print ' i got here'
    oO0OOoo0OO = OoOooO ( oO0o0 )
    III11II1I1Ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for III11II1I1Ii1 in III11II1I1Ii1 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( III11II1I1Ii1 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oO0o0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( III11II1I1Ii1 ) )
     for oO0o0 in oO0o0 :
      oO0o0 = 'https://www.youtube.com/w' + oO0o0
     i11111I1I = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( III11II1I1Ii1 ) )
     for i11111I1I in i11111I1I :
      i11111I1I = 'http:' + i11111I1I
     OOiIiIIi1 ( '[COLORred]' + O0Oooo + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11111I1I , O0o0Oo , '' )
   elif I1111i in OOOO :
    pass
   elif 'user' in oO0o0 or 'elete' in I1111i :
    pass
   elif 'hannel' in oO0o0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oO0o0
    oO0OOoo0OO = OoOooO ( oO0o0 )
    I11iI1I = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for o00O0O , oO0o0 , I1111i in I11iI1I :
     if 'outube' in oO0o0 or 'list' in oO0o0 :
      pass
     elif 'atch' in oO0o0 :
      oO0o0 = ( oO0o0 ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + O0Oooo + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + O0Oooo + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11111I1I , i11111I1I , '' )
    if 50 - 50: iI11I1II1I1I * I1111IIi . ii / IIiIiII11i - Ii1I * Ii1I
def OOo000o0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for o00O0O , url , I1111i , O0Oooo , o000 in i1IIIII11I1IiI :
  OOOO . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  i11111I1I = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + i11111I1I
  url = 'http://www.youtube.com' + url
  OOiIiIIi1 ( '[COLORred]' + O0Oooo + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11111I1I , i11111I1I , o000 )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o00O0O , url , I1111i , O0Oooo in i1IIIII11I1IiI :
   I1I11i ( 'tvshows' , 'INFO' )
   i11111I1I = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oO0OOoo0OO = OoOooO ( url )
    III11II1I1Ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for III11II1I1Ii1 in III11II1I1Ii1 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( III11II1I1Ii1 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( III11II1I1Ii1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     i11111I1I = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( III11II1I1Ii1 ) )
     for i11111I1I in i11111I1I :
      i11111I1I = 'http:' + i11111I1I
     OOiIiIIi1 ( '[COLORred]' + O0Oooo + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11111I1I , O0o0Oo , '' )
   elif I1111i in OOOO :
    pass
   elif 'user' in url or 'elete' in I1111i :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0OOoo0OO = OoOooO ( url )
    I11iI1I = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for o00O0O , url , I1111i in I11iI1I :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + O0Oooo + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + O0Oooo + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11111I1I , i11111I1I , '' )
    if 69 - 69: I11i1ii1 - ii * o0o00Oo0O
    if 84 - 84: I11i1ii1 + Ii - Ii1IIIi1 * I11i1ii1
def ooO ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  I1IiiIiii1 ( )
  i11i = open ( i1I1iI )
  i1IIIII11I1IiI = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( i11i ) )
  for oo0OoOO0o0o , OO0OOO00 in i1IIIII11I1IiI :
   if oo0OoOO0o0o == 'needs replacing' or OO0OOO00 == 'needs replacing' :
    ooOOo0o ( )
    if 50 - 50: IIiIiII11i - iiiiiiii1 + iI11I1II1I1I + iI11I1II1I1I
  iiOOooooO0Oo ( '[COLOR' + II + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o , 60004 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
def I1IiiIiii1 ( ) :
 i1i = OoOooO ( 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 for oO0o0 in i1IIIII11I1IiI :
  OoooooOo = datetime . fromtimestamp ( float ( i1IIIII11I1IiI [ 0 ] ) )
  OoooooOo . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= OoooooOo <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   OOooO0OOoo . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + II + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + II + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + II + '] To Purchase A licence[/COLOR]' )
def OooOo ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"username":"(.+?)"' ) . findall ( i1i )
 oOo0I1Ii11i = re . compile ( '"password":"(.+?)"' ) . findall ( i1i )
 OoOOo0O00 = re . compile ( '"status":"(.+?)"' ) . findall ( i1i )
 i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 ooOoO00 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( i1i )
 Iii1I1111ii = re . compile ( '"created_at":"(.+?)"' ) . findall ( i1i )
 iIiI = re . compile ( '"max_connections":"(.+?)"' ) . findall ( i1i )
 oOoO0o = re . compile ( '"is_trial":"1"' ) . findall ( i1i )
 oOOo = re . compile ( '"is_trial":"0"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']My GTV Account Information[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  i1iIiiiiii1II ( '[COLOR' + II + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in oOo0I1Ii11i :
  i1iIiiiiii1II ( '[COLOR' + II + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in OoOOo0O00 :
  i1iIiiiiii1II ( '[COLOR' + II + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in Iii1I1111ii :
  OoooooOo = datetime . fromtimestamp ( float ( Iii1I1111ii [ 0 ] ) )
  OoooooOo . strftime ( '%Y-%m-%d %H:%M:%S' )
  i1iIiiiiii1II ( '[COLOR' + II + ']Created:[/COLOR]  %s' % ( OoooooOo ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in i1I :
  OoooooOo = datetime . fromtimestamp ( float ( i1I [ 0 ] ) )
  OoooooOo . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= OoooooOo <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   i1iIiiiiii1II ( '[COLORred]Expires Today[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  i1iIiiiiii1II ( '[COLOR' + II + ']Expires:[/COLOR]  %s' % ( OoooooOo ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in ooOoO00 :
  i1iIiiiiii1II ( '[COLOR' + II + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in iIiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in oOoO0o :
  i1iIiiiiii1II ( '[COLOR' + II + ']Trial:[/COLOR] Yes' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in oOOo :
  i1iIiiiiii1II ( '[COLOR' + II + ']Trial:[/COLOR] No' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 i1iIiiiiii1II ( '' , '' , '' , '' )
 i1iIiiiiii1II ( '' , '' , '' , '' )
 i1iIiiiiii1II ( '[COLOR' + II + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 19 - 19: I1111IIi - I11i . iI11I1II1I1I . OOooOOo / Ii1IIIi1
def OOO0O00Oo ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
 ooOOo0o ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 13 - 13: iI11I1II1I1I
def IiIIII1iiIIi ( ) :
 iiOOooooO0Oo ( 'Full List' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'PPV' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Entertainment' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Factual' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Movie Channels' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'US Movie Channels TEST' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Kids' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Music' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'UK Sports' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'International Sports' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'US Sports Live Event/Ticket/Pass' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'News UK & International' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'German' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Arabic' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'TV Series Latest' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'VOD Latest' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'VOD Bollywood' , '' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
def i1I1IiI1ii ( ) :
 O00OOoOOOO00O = 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o
 Ooo0OOO = urllib2 . Request ( O00OOoOOOO00O , headers = { "Accept" : "application/xml" } )
 i1Oo00 = urllib2 . urlopen ( Ooo0OOO )
 if i1Oo00 and i1Oo00 . getcode ( ) == 200 :
  ooooOoo0OO = [ ]
  Oo0 = ElementTree . parse ( i1Oo00 )
  O0000Oo00o = Oo0 . getroot ( )
  for I11iI1I in Oo0 . findall ( "channel" ) :
   II1 = I11iI1I . find ( 'title' ) . text
   II1 = base64 . b64decode ( II1 )
   II1 = II1 . partition ( "[" )
   iio00 = II1 [ 1 ] + II1 [ 2 ]
   iio00 = iio00 . partition ( "]" )
   iio00 = iio00 [ 2 ]
   iio00 = iio00 . partition ( "   " )
   iio00 = iio00 [ 2 ]
   if 4 - 4: oO0o
   ooOO = I11iI1I . find ( "description" ) . text
   if ooOO :
    ooOO = base64 . b64decode ( ooOO )
    Ii1I1 = ooOO . partition ( "(" )
    Ii1I1 = "NOW:  " + Ii1I1 [ 0 ]
    OO0ooO0 = ooOO . partition ( ")\n" )
    OO0ooO0 = OO0ooO0 [ 2 ] . partition ( "(" )
    OO0ooO0 = "NEXT:  " + OO0ooO0 [ 0 ]
    OoOooOO0oOOo0O = Ii1I1 + OO0ooO0
   else :
    OoOooOO0oOOo0O = ""
   ooooOoo0OO . append ( { 'title' : II1 [ 0 ] , 'cs' : iio00 , 'schedule' : OoOooOO0oOOo0O } )
 return ooooOoo0OO
def I1IIiIIi1Ii1III ( name ) :
 if 86 - 86: Ii + Ii . iiiiiiii1 % oOo0O0Ooo . I11i1ii1
 iII1iI1IIiI = name
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , o00O0O , O00oo , oO0o0 in i1IIIII11I1IiI :
  if iII1iI1IIiI == 'Full List' :
   oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
   if 53 - 53: oO0o % I11i / Ii1IIIi1 % I1111IIi % oO0o % ii
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
  else :
   iII1iI1IIiI = ( iII1iI1IIiI ) . replace ( 'World' , 'القنوات العربية' )
   if iII1iI1IIiI in O00oo :
    oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
    if 31 - 31: oOo0O0Ooo
    print oO0o0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    if 73 - 73: I11i1ii1 . o0o00Oo0O / I11i - ii % Ii
    OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
    if 80 - 80: ii1ii11IIIiiI / I11i1ii1 % o0o00Oo0O . I1ii11iIi11i
   else :
    pass
def oOiI111I1III ( url , name , img ) :
 img = img
 name = name
 url = url
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1i1IIIIIIIi , i111IiiI1Ii in i1IIIII11I1IiI :
  if name == i1i1IIIIIIIi :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) + i111IiiI1Ii , ( url ) . strip ( ) , 10012 , img , img , '' )
  else :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 10012 , img , img , '' )
def OooOOOOOo ( name ) :
 iII1iI1IIiI = name
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , o00O0O , oO0o0 in i1IIIII11I1IiI :
  oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
  OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
 else :
  OOiIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 50 - 50: iiiiiiii1 + I11i1ii1 + O0OOOoOoo0
  if 15 - 15: ooOOOoO
  if 13 - 13: iI11I1II1I1I * OOooOOo / iiiiiiii1 % I11i1ii1 + o000O0o
  if 41 - 41: Ii1I
  if 5 - 5: I1ii11iIi11i
  if 100 - 100: ii1ii11IIIiiI + iI11I1II1I1I
  if 59 - 59: I1111IIi
  if 89 - 89: OOooOOo % iI11I1II1I1I
  if 35 - 35: Ii1I + iiiiiiii1 - OOooOOo % o000O0o % I11i % OOooOOo
  if 45 - 45: oOo0O0Ooo * Ii1IIIi1 % oO0o
  if 24 - 24: I11i1ii1 - ooOOOoO * o000O0o
  if 87 - 87: ii1ii11IIIiiI - Ii1I % Ii1I . o000O0o / Ii1I
def oo000o0000oO ( ) :
 iiOOooooO0Oo ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( ooOooo000oOO ) :
  iiOOooooO0Oo ( 'Backup Genie Favourites' , oO0o0 , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( oO0 ) :
  iiOOooooO0Oo ( 'Backup Ivue Config' , oO0 , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  iiOOooooO0Oo ( 'Backup Kodi Favourites' , Ii1iIiII1ii1 , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 6 - 6: OOooOOo / iI11I1II1I1I * ii * Ii
  if 79 - 79: I1111IIi % oO0o
  if 81 - 81: Ii + Ii * oO0o + I1111IIi
zip = oo00 . getSetting ( 'zip' )
iii = xbmc . translatePath ( os . path . join ( zip ) )
def iiIIiiIi ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 42 - 42: O0OOOoOoo0 + iI11I1II1I1I
  if 21 - 21: OOooOOo - I1ii11iIi11i % o0o00Oo0O . oO0o + OOooOOo
  if 41 - 41: IIiIiII11i * I11i1ii1
def o0oOoOo0 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = ooOooo000oOO
  elif 'Ivue' in name :
   url = oO0
  elif 'Kodi' in name :
   url = Ii1iIiII1ii1
  iiIIiiIi ( )
  III1IiI1i1i = open ( url ) . read ( )
  o0OOOOOo0 = os . path . join ( iii , description . split ( 'Your ' ) [ 1 ] )
  oooOo0OOOoo0 = open ( o0OOOOOo0 , mode = 'w' )
  oooOo0OOOoo0 . write ( III1IiI1i1i )
  oooOo0OOOoo0 . close ( )
 else :
  if 'guisettings.xml' in description :
   oooOoO = open ( os . path . join ( iii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   O0Oo0 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   i1IIIII11I1IiI = re . compile ( O0Oo0 ) . findall ( oooOoO )
   for type , iIIIi1IiI11I1 , O0Ooo000 in i1IIIII11I1IiI :
    O0Ooo000 = O0Ooo000 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , iIIIi1IiI11I1 , O0Ooo000 ) )
  else :
   o0OOOOOo0 = os . path . join ( url )
   III1IiI1i1i = open ( os . path . join ( iii , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oooOo0OOOoo0 = open ( o0OOOOOo0 , mode = 'w' )
   oooOo0OOOoo0 . write ( III1IiI1i1i )
   oooOo0OOOoo0 . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 36 - 36: I1ii11iIi11i % ii1ii11IIIiiI / Ii % iiiiiiii1 + oO0o
 if 23 - 23: IIiIiII11i
 if 93 - 93: o000O0o . ooOOOoO / ooOoO0O00
 if 50 - 50: iiiiiiii1 / ooOoO0O00 % ii
def oOOOOO0Ooooo ( ) :
 o0o000Oo = 1
 iiIIiiIi ( )
 oO0o0O0o0OO00 = xbmc . translatePath ( os . path . join ( iii , 'Build Backup' , 'Full Backup' , '' ) )
 iIiiiIi = xbmc . translatePath ( os . path . join ( iii , 'Build Backup' , 'my_full_backup.zip' ) )
 OooooOo = xbmc . translatePath ( os . path . join ( iii , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oO0o0O0o0OO00 ) :
  os . makedirs ( oO0o0O0o0OO00 )
 IIIiiiIiI = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not IIIiiiIiI ) : return False , 0
 II1 = IIIiiiIiI
 OO0OOoooo0o = xbmc . translatePath ( os . path . join ( oO0o0O0o0OO00 , II1 + '.zip' ) )
 IiIi1Ii = [ 'plugin.video.GenieTv' ]
 iiIIiI11II1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 oooOo = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 oOoO0Oo0 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 i11i11i = "Creating full backup of existing build"
 iiI1iI = "Creating Community Build"
 Ooo00O0 = "Archiving..."
 OoO0OOoO0 = ""
 iiI11i = "Please Wait"
 o0Oo ( Oo0o0000o0o0 , OO0OOoooo0o , iiI1iI , Ooo00O0 , OoO0OOoO0 , iiI11i , oooOo , oOoO0Oo0 )
 time . sleep ( 1 )
 iiI1i = xbmc . translatePath ( os . path . join ( oO0o0O0o0OO00 , II1 + '_guisettings.zip' ) )
 i11Io0 = zipfile . ZipFile ( iiI1i , mode = 'w' )
 try :
  i11Io0 . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 i11Io0 . close ( )
 if o0o000Oo == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + iIiiiIi , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OO0OOoooo0o + '[/COLOR]' )
  if 92 - 92: Ii1IIIi1
def o0Oo ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 I1iI11111ii1 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 oOO0ooo0oo0000 = len ( sourcefile )
 oOo0OOOOoO = [ ]
 OoO0Ooo = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for Ii1I1I , oOOoOOO0oOoo , o0O0ooooooo00 in os . walk ( sourcefile ) :
  for file in o0O0ooooooo00 :
   OoO0Ooo . append ( file )
 I1111ii11IIII = len ( OoO0Ooo )
 for Ii1I1I , oOOoOOO0oOoo , o0O0ooooooo00 in os . walk ( sourcefile ) :
  oOOoOOO0oOoo [ : ] = [ IiIi1II111I for IiIi1II111I in oOOoOOO0oOoo if IiIi1II111I not in exclude_dirs ]
  o0O0ooooooo00 [ : ] = [ oooOo0OOOoo0 for oooOo0OOOoo0 in o0O0ooooooo00 if oooOo0OOOoo0 not in exclude_files ]
  for file in o0O0ooooooo00 :
   oOo0OOOOoO . append ( file )
   o00o = len ( oOo0OOOOoO ) / float ( I1111ii11IIII ) * 100
   o0oOoO00o . update ( int ( o00o ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   IIi1i1 = os . path . join ( Ii1I1I , file )
   if not 'temp' in oOOoOOO0oOoo :
    if not 'plugin.program.originwizard' in oOOoOOO0oOoo :
     import time
     o0O0Ooo = '01/01/1980'
     O0oO00oOOooO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( IIi1i1 ) ) )
     if O0oO00oOOooO > o0O0Ooo :
      I1iI11111ii1 . write ( IIi1i1 , IIi1i1 [ oOO0ooo0oo0000 : ] )
 I1iI11111ii1 . close ( )
 o0oOoO00o . close ( )
 if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
 if 66 - 66: o0o00Oo0O
def oOooOOo00ooO ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 if 71 - 71: iiiiiiii1 - I11i - Ii1IIIi1
 if 28 - 28: iI11I1II1I1I
def iI11II1i1I1 ( ) :
 Oo0oO ( )
 i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  iIII ( )
 if i11I1II1I11i == 1 :
  O0oO0OOoOOO0oO ( )
 if i11I1II1I11i == 2 :
  ooo ( )
 if i11I1II1I11i == 3 :
  i111i1I1ii1i ( )
  if 72 - 72: O0OOOoOoo0 - ii
  if 25 - 25: OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * o000O0o
  if 30 - 30: ooOOOoO % OOooOOo / Ii1I * o0o00Oo0O * ii1ii11IIIiiI . oOo0O0Ooo
  if 46 - 46: OOooOOo - o0o00Oo0O
  if 70 - 70: ooOOOoO + I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * ooOOOoO
  if 49 - 49: I11i
  if 25 - 25: O0OOOoOoo0 . ii * iI11I1II1I1I . I11i / o0o00Oo0O + ii1ii11IIIiiI
  if 68 - 68: I1ii11iIi11i
  if 22 - 22: Ii1IIIi1
def I1I11Iiii111 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   oOIIiIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , OOoOooOoOOOoo , I1111i )
  if i11I1II1I11i == 1 :
   iiIII1II ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if i11I1II1I11i == 2 :
   iI1 ( )
  if i11I1II1I11i == 3 :
   ii111iiIii ( )
  if i11I1II1I11i == 4 :
   oO0oiIiI ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if i11I1II1I11i == 5 :
   iIIiiiI1iI1 ( )
  if i11I1II1I11i == 6 :
   oO00000oO0o0O ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if i11I1II1I11i == 7 :
   IIIiI1iI1 ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if i11I1II1I11i == 8 :
   IIiIiiii1I1 ( str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if i11I1II1I11i == 9 :
   oO0O0 ( )
  if i11I1II1I11i == 10 :
   o0i1Ii11II ( )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Rays-Ravers.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 90037 , III1iII1I1ii + 'Quicksilver.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RadioNomy[/COLOR]' , '' , 70001 , III1iII1I1ii + 'RadioNomy.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30031 , III1iII1I1ii + 'MusicChannels.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , III1iII1I1ii + 'UKRadio.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']WORLD RADIO[/COLOR]' , str ( I1I1IiI1 ) , 1013 , III1iII1I1ii + 'WorldRadio.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , III1iII1I1ii + 'Concerts.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) , 1030 , III1iII1I1ii + 'MUSIC.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , III1iII1I1ii + 'MusicVideos.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , III1iII1I1ii + 'Music.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , str ( I1I1IiI1 ) , 1111 , III1iII1I1ii + 'MusicSearch.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , III1iII1I1ii + 'KodibleAudioBooks.png' , O0o0Oo , '' )
  if 33 - 33: I1111IIi . ii . o000O0o
 I1I11i ( 'movies' , 'MAIN' )
 if 15 - 15: Ii1I . O0OOOoOoo0
def o0Iiii ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   I1i1I ( )
  if i11I1II1I11i == 1 :
   iiIiIIIiiI ( )
  if i11I1II1I11i == 2 :
   oOOo0O00o ( )
  if i11I1II1I11i == 3 :
   i1111iI1 ( oO0o0 )
  if i11I1II1I11i == 4 :
   Oo0oOOOOo ( oO0o0 )
  if i11I1II1I11i == 5 :
   O0O0ooOOO ( )
  if i11I1II1I11i == 6 :
   iiiO000OOO ( url = 'http://www.iplocation.net/' , inc = 1 )
  if i11I1II1I11i == 7 :
   o0IIi1 ( )
 else :
  OOiIiIIi1 ( 'CLLEANUP' , 'url' , 9666 , III1iII1I1ii + 'MAIN5.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']KILL KODI[/COLOR]' , '' , 80000 , III1iII1I1ii + 'KillKodi.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '' , 50004 , III1iII1I1ii + 'Speedtest.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , III1iII1I1ii + 'View-Log-File.png' , O0o0Oo , '' )
  OOiIiIIi1 ( 'DELETE CACHE' , 'url' , 14 , III1iII1I1ii + 'DeleteCache.png' , O0o0Oo , '' )
  OOiIiIIi1 ( 'DELETE PACKAGES' , 'url' , 6 , III1iII1I1ii + 'DeletePackages.png' , O0o0Oo , '' )
  OOiIiIIi1 ( 'FORCE REFRESH' , 'url' , 10 , III1iII1I1ii + 'ForceRefresh.png' , O0o0Oo , 'Force Refresh All Repos' )
  iiOOooooO0Oo ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , III1iII1I1ii + '1.jpg' , O0o0Oo , 'Fix Corrupt Database' )
  OOiIiIIi1 ( 'CHECK MY IP' , 'url' , 12 , III1iII1I1ii + 'CheckMyIP.png' , O0o0Oo , '' )
  OOiIiIIi1 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , III1iII1I1ii + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , O0o0Oo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 73 - 73: Ii1IIIi1 + Ii1IIIi1 % ooOOOoO * ooOoO0O00
  if 4 - 4: Ii1IIIi1 - o000O0o % OOooOOo / IIiIiII11i % o000O0o
 I1I11i ( 'movies' , 'MAIN' )
 if 96 - 96: ii1ii11IIIiiI . iiiiiiii1 - Ii1I + I11i * oO0o / O0OOOoOoo0
 if 26 - 26: Ii1IIIi1 * I1ii11iIi11i
def i1i1II ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , III1iII1I1ii + 'repos.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']NEW[/COLOR]' , str ( I1I1IiI1 ) , 22 , III1iII1I1ii + 'NEW.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']IPTV[/COLOR]' , str ( I1I1IiI1 ) , 23 , III1iII1I1ii + 'IPTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']VIDEO[/COLOR]' , str ( I1I1IiI1 ) , 24 , III1iII1I1ii + 'VIDEO.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SPORTS[/COLOR]' , str ( I1I1IiI1 ) , 25 , III1iII1I1ii + 'SPORTS.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']KIDS[/COLOR]' , str ( I1I1IiI1 ) , 26 , III1iII1I1ii + 'KIDS.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC[/COLOR]' , str ( I1I1IiI1 ) , 27 , III1iII1I1ii + 'MUSIC.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']PROGRAMS[/COLOR]' , str ( I1I1IiI1 ) , 28 , III1iII1I1ii + 'PROGRAMS.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']XXX[/COLOR]' , 'URL' , 29 , III1iII1I1ii + 'XXX.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 31 - 31: ooOOOoO * o000O0o . ii1ii11IIIiiI
 if 35 - 35: ooOOOoO
def o00oo ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( 'CHECK ADVANCED XML' , str ( I1I1IiI1 ) , 8 , III1iII1I1ii + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'MUCKYS XML' , str ( I1I1IiI1 ) + '/wizard/muckys.xml' , 7 , III1iII1I1ii + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '0CACHE XML' , str ( I1I1IiI1 ) + '/wizard/0cache.xml' , 7 , III1iII1I1ii + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'MIKEY1234 XML' , str ( I1I1IiI1 ) + '/wizard/mikey.xml' , 7 , III1iII1I1ii + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'TUXENS XML' , str ( I1I1IiI1 ) + '/wizard/tuxens.xml' , 7 , III1iII1I1ii + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'P2P RECOMMENDED XML1' , str ( I1I1IiI1 ) + '/wizard/p2p1.xml' , 7 , III1iII1I1ii + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'P2P RECOMMENDED XML2' , str ( I1I1IiI1 ) + '/wizard/p2p2.xml' , 7 , III1iII1I1ii + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'DELETE XML' , str ( I1I1IiI1 ) , 11 , III1iII1I1ii + 'XML.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 70 - 70: ooOOOoO - I1ii11iIi11i / ii % ii
def iI1i111I1Ii ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , III1iII1I1ii + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 95 - 95: ii % ii . ii1ii11IIIiiI
def III1ii ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , O0o0Oo , '' )
 if 38 - 38: Ii1I + OOooOOo
 if 68 - 68: o0o00Oo0O
 if 76 - 76: Ii1I
def Iii1IIII11I ( ) :
 Oo0oO ( )
 i1Oo0oO00o = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  ooO000OO ( )
 if i11I1II1I11i == 0 :
  i111IIiIiiI1 ( oO0o0 )
 if i11I1II1I11i == 0 :
  OO0IIIIIIi111i ( oO0o0 )
  if 37 - 37: O0OOOoOoo0
  if 33 - 33: oO0o - o0o00Oo0O - oO0o
  if 94 - 94: I1111IIi * ooOOOoO * ii / I11i . I1111IIi - I11i
 I1I11i ( 'movies' , 'MAIN' )
 if 13 - 13: Ii1IIIi1 / I1111IIi - oO0o / Ii1IIIi1 . ooOoO0O00
def IiI1i111i ( ) :
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 i1IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1i )
 for o00O0O , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , o00O0O , o00O0O , '' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 26 - 26: iI11I1II1I1I * I11i . ooOOOoO
def I11III11III1 ( url ) :
 i1i = OoOooO ( oooOoO00OooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 98 - 98: Ii1IIIi1 + ii1ii11IIIiiI
def ooO000OO ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 52 - 52: I1ii11iIi11i / OOooOOo - iiiiiiii1 . O0OOOoOoo0
def iiI11Ii1i ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + O0O0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 83 - 83: O0OOOoOoo0 % ooOOOoO
def III1 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + OOO000OOo0o0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 14 - 14: O0OOOoOoo0 - ooOOOoO * ii + Ii1IIIi1 . IIiIiII11i
def i1i1I11i1I ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + O0oII1IIiiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 96 - 96: Ii1IIIi1 + Ii1IIIi1 % I1111IIi % Ii1IIIi1
def IiiI1I ( url ) :
 i1i = OoOooO ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 3 - 3: IIiIiII11i - ii1ii11IIIiiI % OOooOOo / o000O0o
def i111IIiIiiI1 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + Ii1ooOO0OOO00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 40 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 76 - 76: ii * ii - O0OOOoOoo0 - iI11I1II1I1I . ii / Ii1I
def oOOOO0oo0O0OO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + O0OOoo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 19 - 19: I11i1ii1 % o000O0o
def OooOoOO0 ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  iIiiIiiI1Ii111i ( )
 if i11I1II1I11i == 1 :
  IIIi1IiIiii ( )
 if i11I1II1I11i == 2 :
  oOOo0ooO0 ( )
  if 38 - 38: iiiiiiii1
  if 18 - 18: O0OOOoOoo0 / I11i + I1111IIi % o000O0o - I1111IIi
  if 18 - 18: oOo0O0Ooo + I11i1ii1 % Ii1I - OOooOOo * Ii . I11i
  if 16 - 16: I1ii11iIi11i
def IIIi1IiIiii ( ) :
 iIIII = i11i1iiiII ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( iIIII )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , o00oO0o00O in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( 'Android Apps' + o00oO0o00O , 'https://www.apkfiles.com' + oO0o0 , 30035 , III1iII1I1ii + 'apps.png' )
 for oO0o0 , o00oO0o00O in i1I :
  IiiIiI1Ii1i ( 'Android Games' + o00oO0o00O , 'https://www.apkfiles.com' + oO0o0 , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I11i ( 'movies' , 'MAIN' )
def i11i11Iiii11i ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '/cat' in url :
   IiiIiI1Ii1i ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def II11II1I ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '/app' in url :
   IiiIiI1Ii1i ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def O0OO00000o00 ( url ) :
 iIIII = OoOooO ( url )
 iIiII = url
 if "page=" in str ( url ) :
  iIiII = url . split ( '?' ) [ 0 ]
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'apk' in url :
   OOiIiIIi1 ( ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + o00O0O )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 OOiIiIIi1 ( 'Next Page' , iIiII + str ( i1I ) , 30037 , III1iII1I1ii + 'Next.png' )
def OOO000Oo ( name , url ) :
 iIIII = i11i1iiiII ( url )
 name = name
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  I1IIIi1i ( name , url , 'Brackets' )
def oOOo0ooO0 ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo000 = 'https://www.apkfiles.com/search?q=' + ( o00O ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1iIIi = Oo000 . lower ( )
 O0OO00000o00 ( i1iIIi )
 if 54 - 54: IIiIiII11i . ooOoO0O00 / Ii1I % oOo0O0Ooo / iiiiiiii1
def OOoOoOo0 ( url ) :
 o00O0 = xbmc . translatePath ( os . path . join ( iIioOo , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , I1111i + '.apk' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 66 - 66: IIiIiII11i + oO0o
def II1iI1iiiI ( url ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , I1111i + '.mp4' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 75 - 75: ii . Ii1IIIi1 + oO0o / ii1ii11IIIiiI - oOo0O0Ooo % ii1ii11IIIiiI
 if 89 - 89: O0OOOoOoo0 * iI11I1II1I1I + Ii . ii
def O0O0 ( name , url , description ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , name )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 oO0oo = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print oO0oo
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , oO0oo , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 52 - 52: I1111IIi % I11i1ii1
 if 25 - 25: ooOOOoO / ooOOOoO % ii - Ii1I * o000O0o
 if 23 - 23: Ii
 if 100 - 100: o000O0o + o0o00Oo0O . oOo0O0Ooo + ooOoO0O00 - OOooOOo + I11i
 if 65 - 65: IIiIiII11i / I1ii11iIi11i
def iIiiIiiI1Ii111i ( ) :
 i1i = OoOooO ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1i )
 for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O , iiII1i in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , oO0o0 , 80003 , iiO0oOo00o , III1iII1I1ii + 'APKToolsB.png' , iiII1i )
def IiiiI1 ( apk , ret = None ) :
 if apk == "kodi" :
  I1IIIi = "https://kodi.tv/download/"
  i1i = OoOooO ( I1IIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1i )
  if len ( i1IIIII11I1IiI ) == 1 :
   I1iOo00oOO00 = i1IIIII11I1IiI [ 0 ] [ 0 ]
   II1 = i1IIIII11I1IiI [ 0 ] [ 1 ]
   Iio0000O00oO0O = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( I1iOo00oOO00 , II1 )
  if ret == 'version' : return I1iOo00oOO00
  else : return Iio0000O00oO0O
 elif apk == "spmc" :
  IiiI111I11 = 'https://github.com/koying/SPMC/releases/latest/'
  i1i = OoOooO ( IiiI111I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1i )
  I1iOo00oOO00 = re . sub ( '<[^<]+?>' , '' , i1IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  Iio0000O00oO0O = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( I1iOo00oOO00 , I1iOo00oOO00 )
  if ret == 'version' : return I1iOo00oOO00
  else : return Iio0000O00oO0O
def I1IIIi1i ( name , url , Brackets ) :
 if I1IIII1i ( ) == 'android' :
  oO0Ooooo000 = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not oO0Ooooo000 : Iii1Iiii ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  i1i1Ii1IiIII = name
  if oO0Ooooo000 :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not Iii1 ( url ) == True : Iii1Iiii ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % i1i1Ii1IiIII , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    i11Io0 = zipfile . ZipFile ( oOO0O00Oo0O0o )
    for file in i11Io0 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as oooOo0OOOoo0 :
       I1IIii11 = file . split ( '/' ) [ 1 ]
       oooOo0OOOoo0 . write ( i11Io0 . read ( file ) )
       xbmc . sleep ( 500 )
       oooOo0OOOoo0 . close ( )
       try :
        os . remove ( oOO0O00Oo0O0o )
       except :
        pass
       oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , I1IIii11 )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : Iii1Iiii ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : Iii1Iiii ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 22 - 22: I11i1ii1 / I11i1ii1 - ii1ii11IIIiiI % ooOOOoO . Ii1IIIi1 + I1111IIi
 if 64 - 64: ooOoO0O00 % Ii1I / ii1ii11IIIiiI % ii
 if 24 - 24: iiiiiiii1 + ii . I1111IIi / OOooOOo / ooOOOoO
 if 65 - 65: ii
def iiii11iI1 ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1i )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  oO0o0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oO0o0 )
  Oo00Oo ( ( I1111i ) . replace ( '_' , ' ' ) , oO0o0 )
  if 25 - 25: iI11I1II1I1I
def Oo00Oo ( name , url ) :
 if I1IIII1i ( ) == 'android' :
  oO0Ooooo000 = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not oO0Ooooo000 : Iii1Iiii ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  i1i1Ii1IiIII = name
  if oO0Ooooo000 :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not Iii1 ( url ) == True : Iii1Iiii ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % i1i1Ii1IiIII , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : Iii1Iiii ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : Iii1Iiii ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 63 - 63: I11i1ii1
 if 96 - 96: ooOOOoO
def IIII ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'INFO' )
 if 17 - 17: o0o00Oo0O . Ii1IIIi1
 if 63 - 63: O0OOOoOoo0
def oOo0 ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 30015 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 11 - 11: O0OOOoOoo0 - iI11I1II1I1I
def ooOo0O0 ( url , iconimage , fanart ) :
 i1i = OoOooO ( url )
 iIi1IIiIII1 = url
 o00O0O = iconimage
 fanart = fanart
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for oOOo0oo0O , I1111i in i1IIIII11I1IiI :
  if '.mp4' in I1111i :
   OOiIiIIi1 ( 'Watch VIDEO' , url + '/' + oOOo0oo0O , 222 , o00O0O , fanart , '' )
  if 'description' in I1111i :
   OOiIiIIi1 ( 'Read Description' , url + '/' + oOOo0oo0O , 30017 , o00O0O , fanart , '' )
  if 'images' in I1111i :
   iiOOooooO0Oo ( 'View Images' , url + '/' + oOOo0oo0O , 30018 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Android' , url + '/' + oOOo0oo0O , 30016 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Pc' , url + '/' + oOOo0oo0O , 30019 , o00O0O , fanart , '' )
 I1I11i ( 'movies' , 'INFO' )
 if 83 - 83: ii
def iIIi111IiII1i ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  oOo0O000oo0 ( url )
  if 15 - 15: I1ii11iIi11i / ii1ii11IIIiiI % o0o00Oo0O + Ii1I
def o0oi1I1I1I ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  iII1III ( url )
  if 58 - 58: ooOOOoO % Ii / Ii * I11i1ii1 - iiiiiiii1
def i11ii111i1ii ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1i )
 for Oo0O0O in i1IIIII11I1IiI :
  OO0O000 ( 'Description:' , Oo0O0O )
  if 8 - 8: Ii * o0o00Oo0O + Ii1I . iI11I1II1I1I % ooOOOoO / ooOOOoO
def oO00oo ( url ) :
 i1i = OoOooO ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for oOOo0oo0O , I1111i in i1IIIII11I1IiI :
  if 'png' in I1111i :
   OOiIiIIi1 ( 'image' , '' , '' , url + '/' + oOOo0oo0O , url + '/' + oOOo0oo0O , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 89 - 89: ii1ii11IIIiiI
def o00O00O0Oo0 ( name , url , description ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , name + '.zip' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 O0O0ooOOO ( )
 if 53 - 53: ooOoO0O00 . ooOoO0O00 - ooOOOoO / O0OOOoOoo0 - OOooOOo % oOo0O0Ooo
 if 65 - 65: O0OOOoOoo0 . ii - o0o00Oo0O . O0OOOoOoo0 - Ii
def iII1III ( url ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
 I1iIIiiIIi1i ( url )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1i1I ( )
 if 29 - 29: Ii1I . oOo0O0Ooo % o000O0o - Ii
def oOo0O000oo0 ( url ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
 I1iIIiiIIi1i ( url )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1i1I ( )
 if 27 - 27: Ii1I - Ii % iiiiiiii1 / I1ii11iIi11i . I1ii11iIi11i / ii
def O0oO0o0oOOO0o ( name , url , description ) :
 ii1 = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oOO0O00Oo0O0o = os . path . join ( oOOoO0 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print ii1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1i1I ( )
 if 16 - 16: o0o00Oo0O * I1111IIi % O0OOOoOoo0
def I1IIII1i ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def iIiIi11 ( log ) :
 xbmc . log ( "[%s]: %s" % ( oO , log ) )
 if not os . path . exists ( oO0o0o0ooO0oO ) : os . makedirs ( oO0o0o0ooO0oO )
 if not os . path . exists ( oo0o0O00 ) : oooOo0OOOoo0 = open ( oo0o0O00 , 'w' ) ; oooOo0OOOoo0 . close ( )
 with open ( oo0o0O00 , 'a' ) as oooOo0OOOoo0 :
  O0OOO0OO0O00OoOo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oooOo0OOOoo0 . write ( O0OOO0OO0O00OoOo . rstrip ( '\r\n' ) + '\n' )
def I1i1I ( ) :
 i11I1II1I11i = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if i11I1II1I11i == 0 : return
 elif i11I1II1I11i == 1 : pass
 I1i1I11 = I1IIII1i ( )
 iIiIi11 ( "Platform: " + str ( I1i1I11 ) )
 os . _exit ( 1 )
 iIiIi11 ( "Force close failed!  Trying alternate methods." )
 if I1i1I11 == 'osx' :
  iIiIi11 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1i1I11 == 'linux' :
  iIiIi11 ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif I1i1I11 == 'android' :
  iIiIi11 ( "############ try android force close #################" )
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
  OOooO0OOoo . ok ( oO , "Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI" )
 elif I1i1I11 == 'windows' :
  iIiIi11 ( "############ try windows force close #################" )
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
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , "Use task manager and NOT ALT F4" )
 else :
  iIiIi11 ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  iIiIi11 ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 9 - 9: oOo0O0Ooo
  if 94 - 94: IIiIiII11i
  if 37 - 37: ii
def OO0IIIIIIi111i ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for oo0OooO , oOOoOOO0oOoo , o0O0ooooooo00 in os . walk ( url ) :
  for file in o0O0ooooooo00 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    oooOoO = open ( ( os . path . join ( oo0OooO , file ) ) ) . read ( )
    I11iI1 = oooOoO . replace ( Oo0o0000o0o0 , 'special://home/' )
    oooOo0OOOoo0 = open ( ( os . path . join ( oo0OooO , file ) ) , mode = 'w' )
    oooOo0OOOoo0 . write ( str ( I11iI1 ) )
    oooOo0OOOoo0 . close ( )
 I1i1I ( )
 if 96 - 96: I11i % I1111IIi / Ii1IIIi1
def iI1 ( ) :
 IiiIiI1Ii1i ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 IiiIiI1Ii1i ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 IiiIiI1Ii1i ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 63 - 63: ooOoO0O00 % Ii % IIiIiII11i * ii
def iIiII1 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def i111iii1I1 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def iiIiII1 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1I :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']Filter - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , o00O0O )
def ii111iI ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def ii11I1 ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O
 I1I = 'https://www.radionomy.com/en/search/index?query=' + ( o00O ) . replace ( ' ' , '+' )
 oO0OOoo0OO = OoOooO ( I1I )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oO0o0 , 70005 , o00O0O )
  if 76 - 76: oOo0O0Ooo
  if 42 - 42: ii % I1ii11iIi11i % Ii1IIIi1
def iIIiiiI1iI1 ( ) :
 iIIII = i11i1iiiII ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , 'http://www.listenlive.eu/' + oO0o0 , 10111113 , III1iII1I1ii + 'radio.png' )
def oO0oiIiI ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  i1iIiiiiii1II ( I1111i , url , 222 , III1iII1I1ii + 'radio.png' )
  if 39 - 39: ii1ii11IIIiiI
def oOo0000ooO ( ) :
 iIIII = i11i1iiiII ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.toonjet.com/' + oO0o0 , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1Io0oO0oo ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( iIIII )
 i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( iIIII )
 for url , o00O0O in i1IIIII11I1IiI :
  if 'ol.gif' in o00O0O :
   pass
  elif 'link_block_' in o00O0O :
   pass
  elif '.png' in o00O0O :
   pass
  else :
   IiiIiI1Ii1i ( ( o00O0O ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in i1I :
  IiiIiI1Ii1i ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOO00Oo ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 82 - 82: I1111IIi
  if 51 - 51: o000O0o % oO0o + I11i + ii1ii11IIIiiI - ii . oO0o
def o0i1Ii11II ( ) :
 II11IiI1 ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 II11IiI1 ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 86 - 86: iI11I1II1I1I % o000O0o - OOooOOo + iiiiiiii1 % oO0o . Ii1I
def iiIIiIi ( ) :
 II11IiI1 ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 II11IiI1 ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 II11IiI1 ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 97 - 97: O0OOOoOoo0 + ooOOOoO % I1ii11iIi11i . IIiIiII11i / IIiIiII11i * O0OOOoOoo0
def o0Ooi1II11i1iI1 ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , oO0o0 , OO0IIi1II11 in i1IIIII11I1IiI :
  if 'Parent' in I1111i :
   pass
  elif '2' in OO0IIi1II11 :
   II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 63 - 63: iiiiiiii1 - ooOoO0O00
def iIi11iI1i ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , oO0o0 , OO0IIi1II11 in i1IIIII11I1IiI :
  if o00O in I1111i . lower ( ) :
   if '1' in OO0IIi1II11 :
    II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in OO0IIi1II11 :
    II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in OO0IIi1II11 :
    II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 46 - 46: ooOoO0O00 + IIiIiII11i * ooOoO0O00 - ii1ii11IIIiiI
    if 79 - 79: IIiIiII11i - o000O0o * Ii1I - OOooOOo . Ii1I
def iiII1IIii1i1 ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , oO0o0 , OO0IIi1II11 in i1IIIII11I1IiI :
  if '1' in OO0IIi1II11 :
   II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in OO0IIi1II11 :
   II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in OO0IIi1II11 :
   II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 38 - 38: O0OOOoOoo0 * ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: o000O0o - Ii
def OOOo00o ( url ) :
 oOOo0oo0O = url
 oO0OOoo0OO = OoOooO ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1I :
  if 'mp3' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oOOo0oo0O + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oOOo0oo0O + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oOOo0oo0O + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in I1111i :
   II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oOOo0oo0O + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 3 - 3: I11i
   if 16 - 16: ooOoO0O00 . ooOoO0O00 / iiiiiiii1 % OOooOOo / oOo0O0Ooo * Ii1I
   if 30 - 30: I11i + ii + Ii1IIIi1 / IIiIiII11i * I1ii11iIi11i
def O00O0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 oOOo0oo0O = url
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if 'Parent' in I1111i :
   pass
  elif '.db' in I1111i :
   pass
  elif '.jpg' in I1111i :
   pass
  elif '.html' in I1111i :
   pass
  elif '.doc' in I1111i :
   pass
  elif 'mp3' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oOOo0oo0O + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oOOo0oo0O + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oOOo0oo0O + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 43 - 43: o000O0o % oO0o - I1ii11iIi11i - o0o00Oo0O - ii
   if 4 - 4: IIiIiII11i - o000O0o % I1ii11iIi11i * Ii
def iIiII1iiiiI ( ) :
 II11IiI1 ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 II11IiI1 ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 II11IiI1 ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 80 - 80: I1ii11iIi11i - I11i - IIiIiII11i . I1111IIi - o0o00Oo0O * I1111IIi
def Iii1I ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O in i1IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oO0o0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in o00O0O :
   pass
  else :
   II11IiI1 ( o00O0O , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oO0o0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + o00O0O + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 100 - 100: ii . I1ii11iIi11i / Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: I11i1ii1 * IIiIiII11i * oO0o * I1111IIi
 if 92 - 92: o000O0o
def i1i1IIiII1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 85 - 85: I1ii11iIi11i . Ii - Ii . oOo0O0Ooo . oO0o % ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 20 - 20: iiiiiiii1 + iiiiiiii1 * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
def OooOoO0OOoOOO0o0o ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if o00O in I1111i . lower ( ) :
   if '</a>' in I1111i :
    pass
   elif '(' in I1111i :
    II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 27 - 27: Ii1I . I1111IIi
    if 66 - 66: o0o00Oo0O / o0o00Oo0O * ooOoO0O00 . ii % iI11I1II1I1I
def I11iIiI1 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 22 - 22: I1111IIi * ii1ii11IIIiiI - ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: oOo0O0Ooo
 if 87 - 87: I1111IIi . ooOoO0O00 % ii * Ii
def o0oOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  oOOo0oo0O = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( oOOo0oo0O )
  if 51 - 51: IIiIiII11i . o000O0o . oO0o % IIiIiII11i
def III1I1ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  if '<p align' in I1111i :
   pass
  elif '&nbsp;' in I1111i :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 4 - 4: iI11I1II1I1I . ooOoO0O00
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: iI11I1II1I1I + I1111IIi % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
 if 60 - 60: I11i . OOooOOo % iiiiiiii1 / oOo0O0Ooo / o0o00Oo0O
def OOOO0oooo ( ) :
 oO0OOoo0OO = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'ongoing' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , III1iII1I1ii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , III1iII1I1ii + 'CartoonShows.png' , '' , '' )
  if 'disney' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , III1iII1I1ii + 'Disney.png' , '' , '' )
  if 'genre' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , III1iII1I1ii + 'Genre.png' , '' , '' )
  if 'years' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , III1iII1I1ii + 'Years.png' , '' , '' )
def IiIii11I ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 Ooo0O00 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , o00O0O , o00O0O , I1111i )
 for url , I1111i in Ooo0O00 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def oooo0oOOoO000 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OooOOO0O00 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 Oo00o00Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0OOoo0OO )
 i1I1i1I111 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in Oo00o00Oo :
  iiOOooooO0Oo ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , I1111i in OooOOO0O00 :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def oOo00OO0ooOOO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 44 - 44: ii1ii11IIIiiI * I11i1ii1 / OOooOOo
def O0o0O0OO00o ( ) :
 oO0OOoo0OO = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 i1IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if '9cart' in oO0o0 :
   IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 69 - 69: I11i1ii1 . Ii1IIIi1 - oOo0O0Ooo
def IiIiIi ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if '9cart' in url :
   IiiIiI1Ii1i ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   IiiIiI1Ii1i ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url , I1111i in ooOoO00 :
  if '9cart' in url :
   IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 36 - 36: Ii1IIIi1 * ii1ii11IIIiiI
def i1iIii1II1i ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20003 , o00O0O )
 for url , I1111i in i1I :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 27 - 27: Ii1I / Ii1IIIi1
def IiiIiiIIII ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'Watch' in url :
   IiiIiI1Ii1i ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 88 - 88: oO0o . iiiiiiii1 / ooOOOoO
def iIiI1I1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20005 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 62 - 62: I11i / iI11I1II1I1I
def O0OOo ( url ) :
 url = cloudflare . source ( url )
 iIiIIiii1II ( url )
 if 81 - 81: o0o00Oo0O + O0OOOoOoo0 . oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + o0o00Oo0O
def Oooo0Oo00o ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in i1IIIII11I1IiI :
  iIiIIiii1II ( url )
  if 32 - 32: OOooOOo . iI11I1II1I1I % o000O0o . o0o00Oo0O . OOooOOo / O0OOOoOoo0
  if 45 - 45: iI11I1II1I1I
def oooooOo0 ( ) :
 if 41 - 41: O0OOOoOoo0 % O0OOOoOoo0 - I1111IIi % oO0o - ii - O0OOOoOoo0
 iiOOooooO0Oo ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 66 - 66: I11i % OOooOOo
def ooo ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 30 - 30: OOooOOo * I1ii11iIi11i % iI11I1II1I1I % oO0o + Ii
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO0OOoo0OO )
 if 46 - 46: oOo0O0Ooo . I1111IIi - Ii - iiiiiiii1
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if o00O in I1111i . lower ( ) :
   if 'Dad!' in I1111i :
    pass
   elif 'Family Guy' in I1111i :
    pass
   elif '2 Stupid' in I1111i :
    pass
   elif 'The Zelfs' in I1111i :
    pass
   elif 'A Clone' in I1111i :
    pass
   elif 'A.T.O.M' in I1111i :
    pass
   elif 'Almost Naked' in I1111i :
    pass
   elif 'Angry Kid' in I1111i :
    pass
   elif 'Annoying Orange' in I1111i :
    pass
   elif 'Aqua Teen' in I1111i :
    pass
   elif 'Assy Mcgee' in I1111i :
    pass
   elif 'Astroblast' in I1111i :
    pass
   elif 'Atomic Betty' in I1111i :
    pass
   elif 'Axe Cop' in I1111i :
    pass
   elif 'Baby Playpen' in I1111i :
    pass
   elif 'Beavis and Butt' in I1111i :
    pass
   elif 'Celebrity Deathmatch' in I1111i :
    pass
   elif 'Clerks The' in I1111i :
    pass
   elif 'Crapston Villas' in I1111i :
    pass
   elif 'Duckman:' in I1111i :
    pass
   elif 'Stripperella' in I1111i :
    pass
   elif 'Vixen' in I1111i :
    pass
   else :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
    if 97 - 97: IIiIiII11i % I1ii11iIi11i * I1111IIi
    if 51 - 51: I1ii11iIi11i % Ii1IIIi1 . I1ii11iIi11i
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 72 - 72: ii1ii11IIIiiI % ii1ii11IIIiiI / oOo0O0Ooo
def OOo00O ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if 'Dad!' in I1111i :
   pass
  elif 'Family Guy' in I1111i :
   pass
  elif '2 Stupid' in I1111i :
   pass
  elif 'The Zelfs' in I1111i :
   pass
  elif 'A Clone' in I1111i :
   pass
  elif 'A.T.O.M' in I1111i :
   pass
  elif 'Almost Naked' in I1111i :
   pass
  elif 'Angry Kid' in I1111i :
   pass
  elif 'Annoying Orange' in I1111i :
   pass
  elif 'Aqua Teen' in I1111i :
   pass
  elif 'Assy Mcgee' in I1111i :
   pass
  elif 'Astroblast' in I1111i :
   pass
  elif 'Atomic Betty' in I1111i :
   pass
  elif 'Axe Cop' in I1111i :
   pass
  elif 'Baby Playpen' in I1111i :
   pass
  elif 'Beavis and Butt' in I1111i :
   pass
  elif 'Celebrity Deathmatch' in I1111i :
   pass
  elif 'Clerks The' in I1111i :
   pass
  elif 'Crapston Villas' in I1111i :
   pass
  elif 'Duckman:' in I1111i :
   pass
  elif 'Stripperella' in I1111i :
   pass
  elif 'Vixen' in I1111i :
   pass
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 40 - 40: I1ii11iIi11i - Ii1IIIi1 + iiiiiiii1 - I11i % oOo0O0Ooo . I11i1ii1
def Ii1iii ( url ) :
 iIIII = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  o000o0o00Oo = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10007 , o000o0o00Oo )
  if 62 - 62: O0OOOoOoo0
  if 8 - 8: O0OOOoOoo0 - oOo0O0Ooo * I1ii11iIi11i % Ii1I * ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 26 - 26: ooOoO0O00 / O0OOOoOoo0 . O0OOOoOoo0
def I1i11IIIi ( url , IMAGE ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   III1IIIIIiiI ( url )
   if 38 - 38: o0o00Oo0O
   if 79 - 79: ooOoO0O00 . o000O0o
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 34 - 34: iiiiiiii1 * IIiIiII11i
def III1IIIIIiiI ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 71 - 71: I1111IIi
  if 97 - 97: Ii1I
  if 86 - 86: I1ii11iIi11i - Ii1IIIi1 . OOooOOo . IIiIiII11i * oOo0O0Ooo . IIiIiII11i
def I1ii1ii11i1I ( ) :
 if 34 - 34: I11i . iiiiiiii1 % I1111IIi - o0o00Oo0O / iiiiiiii1
 iiOOooooO0Oo ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , O0o0Oo , '' )
 if 91 - 91: Ii % iiiiiiii1 * o000O0o - Ii1I . iiiiiiii1
def iIo00oo ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'elete' in I1111i :
   pass
  else :
   i1iIiiiiii1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 222 , o00O0O )
   if 78 - 78: I1111IIi - ooOOOoO % o0o00Oo0O - Ii1IIIi1 % oO0o
def i11IiIi ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 I111 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , O0ooo , i1iII1IiiIiI1 in I111 :
  for o00O in O0ooo :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   IiIIiII1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oO0o0 , I1111i in IiIIiII1I :
    if 'tube' in oO0o0 :
     pass
    elif 'stage' in oO0o0 :
     i1iIiiiiii1II ( '[COLOR' + II + ']' + O0ooo + '   -   ' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O , )
    elif 'vee' in oO0o0 :
     pass
     if 92 - 92: iiiiiiii1 % ii1ii11IIIiiI
def Ii1Ii11I ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 I111 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , O0ooo , i1iII1IiiIiI1 in I111 :
  IiIIiII1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oO0o0 , I1111i in IiIIiII1I :
   if 'tube' in oO0o0 :
    pass
   elif 'stage' in oO0o0 :
    i1iIiiiiii1II ( '[COLOR' + II + ']' + O0ooo + '   -   ' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O )
   elif 'vee' in oO0o0 :
    pass
    if 28 - 28: I11i1ii1 . ooOoO0O00
    if 75 - 75: O0OOOoOoo0 + iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: OOooOOo - OOooOOo . IIiIiII11i . O0OOOoOoo0 + o0o00Oo0O
def i1ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oO0O ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oO0O :
  OOOOo0o00OO0000 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 28 - 28: I1111IIi + Ii + ii / oO0o
  if 6 - 6: oOo0O0Ooo - Ii
  if 61 - 61: iiiiiiii1 * Ii1I % oOo0O0Ooo % oO0o % ooOOOoO + ooOOOoO
  if 6 - 6: I1ii11iIi11i
  if 73 - 73: iiiiiiii1 * Ii1I + I11i - I1ii11iIi11i . ooOOOoO
  if 93 - 93: Ii
  if 80 - 80: ooOoO0O00 . oOo0O0Ooo - o000O0o + Ii1IIIi1 + O0OOOoOoo0 % o000O0o
def I1II ( ) :
 if 13 - 13: IIiIiII11i / OOooOOo / OOooOOo + I11i1ii1
 Ii1i ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 Ii1i ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 62 - 62: ii . ii1ii11IIIiiI
 I1I11i ( 'movies' , 'MAIN' )
 if 28 - 28: o000O0o . o000O0o . iI11I1II1I1I . Ii1IIIi1 . Ii1I * Ii
def ooo00O0OOo ( ) :
 Ii1i ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 Ii1i ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 45 - 45: oOo0O0Ooo / O0OOOoOoo0 + o000O0o + I1111IIi
 I1I11i ( 'movies' , 'MAIN' )
def iIIII1Iii11 ( ) :
 if 3 - 3: I11i % I11i % oOo0O0Ooo - ooOoO0O00
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 Iiii1ii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 84 - 84: ooOOOoO
 for oo0OO in Iiii1ii :
  IiiI11i1I = O0Oo000ooO00 + oo0OO + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( IiiI11i1I )
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , o0ooooO0o0O , I1111i in i1IIIII11I1IiI :
   if o00O in I1111i . lower ( ) :
    IioOOO00Oo ( I1111i , oO0o0 , 222 , OOoOooOoOOOoo , o0ooooO0o0O , ii1Oo0000oOo )
    if 48 - 48: IIiIiII11i + IIiIiII11i * ooOoO0O00 / ii1ii11IIIiiI
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 37 - 37: iI11I1II1I1I % ooOOOoO / I1111IIi
    if 37 - 37: iiiiiiii1 - o000O0o - oO0o
def IiI1IIiiiii ( ) :
 if 43 - 43: o000O0o - I1111IIi % Ii * IIiIiII11i . iiiiiiii1 - ooOOOoO
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 Iiii1ii = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 13 - 13: oO0o
 for oo0OO in Iiii1ii :
  O00 = O0Oo000ooO00 + oo0OO + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( O00 )
  i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1111i , ii1Oo0000oOo , oO0o0 , o00O0O , o0ooooO0o0O , ii1ii111 in i1IIIII11I1IiI :
   if o00O in I1111i . lower ( ) :
    Ii1i ( I1111i , oO0o0 , ii1ii111 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo )
    if 91 - 91: Ii1I + iI11I1II1I1I % I1111IIi
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 90 - 90: I11i1ii1 - ooOOOoO . oO0o + oO0o
    if 45 - 45: OOooOOo / ii . iiiiiiii1 % o0o00Oo0O * Ii1I * I1ii11iIi11i
def oOO0ooO ( ) :
 if 57 - 57: O0OOOoOoo0 - oOo0O0Ooo + ii / O0OOOoOoo0 . I11i1ii1 % ooOoO0O00
 iIIII = OoOooO ( O0Oo000ooO00 + 'spongemain.php' )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , ii1Oo0000oOo , oO0o0 , o00O0O , o0ooooO0o0O , ii1ii111 in i1IIIII11I1IiI :
  Ii1i ( I1111i , oO0o0 , ii1ii111 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo )
  I1I11i ( 'movies' , 'MAIN' )
def OooooO0o0 ( url ) :
 if 99 - 99: Ii1IIIi1 * ooOoO0O00 . ii1ii11IIIiiI * iiiiiiii1 . I11i1ii1
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 O0iI1I1ii11IIi1 = ( '%s%s' % ( OOo , url ) )
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in i1IIIII11I1IiI :
  OOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
  for i11I in OOo0 :
   if i11I == url :
    I1111i = ( '[COLORred]Watched - [/COLOR]' + I1111i ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  IioOOO00Oo ( I1111i , url , 222 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
  if 80 - 80: I11i / o000O0o / ii1ii11IIIiiI - oOo0O0Ooo % iiiiiiii1
  I1I11i ( 'movies' , 'MAIN' )
  if 44 - 44: oOo0O0Ooo % Ii1IIIi1 * Ii * Ii - I1ii11iIi11i . iiiiiiii1
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 68 - 68: O0OOOoOoo0 . ooOOOoO
  if 29 - 29: I11i1ii1 * I1111IIi
def oOiiIIIII ( url ) :
 if 19 - 19: IIiIiII11i / OOooOOo
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , ii1Oo0000oOo , url , o00O0O , o0ooooO0o0O , ii1ii111 in i1IIIII11I1IiI :
  Ii1i ( I1111i , url , ii1ii111 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo )
  if 80 - 80: OOooOOo + iI11I1II1I1I . I1111IIi
  I1I11i ( 'movies' , 'MAIN' )
  if 76 - 76: oOo0O0Ooo * Ii1IIIi1
  if 12 - 12: iI11I1II1I1I / ooOOOoO % ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: oO0o + IIiIiII11i / I1111IIi - o0o00Oo0O % ii1ii11IIIiiI
def IioOOO00Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 27 - 27: oO0o + I1ii11iIi11i
 oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I11I = True
 iIIII1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIII1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIII1i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o00oO0 = [ ]
  o00oO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o00oO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o00oO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iIIII1i . addContextMenuItems ( o00oO0 )
 I11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO , listitem = iIIII1i , isFolder = False )
 return I11I
 if 92 - 92: oOo0O0Ooo % O0OOOoOoo0
def Ii1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 31 - 31: ii - o000O0o / iiiiiiii1
 oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I11I = True
 iIIII1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIII1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIII1i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o00oO0 = [ ]
  o00oO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o00oO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o00oO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iIIII1i . addContextMenuItems ( o00oO0 )
 I11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO , listitem = iIIII1i , isFolder = True )
 return I11I
if 62 - 62: Ii - ooOOOoO
if 81 - 81: ooOOOoO
if 92 - 92: Ii1IIIi1 - I1ii11iIi11i - ii / I1111IIi - ooOoO0O00
if 81 - 81: ooOoO0O00 / iiiiiiii1 % Ii . iI11I1II1I1I * OOooOOo + ii
if 31 - 31: ooOoO0O00 % IIiIiII11i
if 13 - 13: iI11I1II1I1I - IIiIiII11i % o0o00Oo0O . ii1ii11IIIiiI % oO0o
if 2 - 2: ii - ii1ii11IIIiiI % o000O0o / oOo0O0Ooo / I11i
if 3 - 3: IIiIiII11i / Ii1IIIi1
if 48 - 48: I11i1ii1 . Ii1I
if 49 - 49: ooOoO0O00 - OOooOOo . I1ii11iIi11i + iI11I1II1I1I - I11i1ii1 / I1ii11iIi11i
if 24 - 24: o000O0o - O0OOOoOoo0 / I11i1ii1
if 10 - 10: OOooOOo * ooOoO0O00
if 15 - 15: ooOOOoO + ooOoO0O00 - IIiIiII11i % oOo0O0Ooo
if 34 - 34: oOo0O0Ooo
if 57 - 57: Ii1IIIi1 . ii1ii11IIIiiI % I11i
def I1I11 ( string ) :
 if OOoOO0oo0ooO == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 9 - 9: Ii1IIIi1
def I1iII ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 I1IIiIi = [ ]
 try :
  if 93 - 93: o000O0o - Ii1IIIi1 + I11i . o000O0o / ooOOOoO
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( IIIii1II1II ) == False :
  I1I11 ( 'Making Favorites File' )
  I1IIiIi . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oooOoO = open ( IIIii1II1II , "w" )
  oooOoO . write ( json . dumps ( I1IIiIi ) )
  oooOoO . close ( )
 else :
  I1I11 ( 'Appending Favorites' )
  oooOoO = open ( IIIii1II1II ) . read ( )
  o0000oO = json . loads ( oooOoO )
  o0000oO . append ( ( name , url , iconimage , fanart , mode ) )
  I11iI1 = open ( IIIii1II1II , "w" )
  I11iI1 . write ( json . dumps ( o0000oO ) )
  I11iI1 . close ( )
  if 83 - 83: oO0o
  if 16 - 16: I11i1ii1
def iIiiIiIIiI ( ) :
 if os . path . exists ( IIIii1II1II ) == False :
  I1IIiIi = [ ]
  I1I11 ( 'Making Favorites File' )
  I1IIiIi . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  oooOoO = open ( IIIii1II1II , "w" )
  oooOoO . write ( json . dumps ( I1IIiIi ) )
  oooOoO . close ( )
 else :
  o0OoOOoOOoo = json . loads ( open ( IIIii1II1II ) . read ( ) )
  oo0O0 = len ( o0OoOOoOOoo )
  for Ii111Ii11 in o0OoOOoOOoo :
   I1111i = Ii111Ii11 [ 0 ]
   oO0o0 = Ii111Ii11 [ 1 ]
   OOoOooOoOOOoo = Ii111Ii11 [ 2 ]
   try :
    Ii1II = Ii111Ii11 [ 3 ]
    if Ii1II == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     Ii1II = OOoOooOoOOOoo
    else :
     Ii1II = o0ooooO0o0O
   try : IIiII = Ii111Ii11 [ 5 ]
   except : IIiII = None
   try : iII11O00OO00OOOoO = Ii111Ii11 [ 6 ]
   except : iII11O00OO00OOOoO = None
   if 47 - 47: ooOoO0O00 % I11i1ii1 - I1ii11iIi11i * ooOOOoO / Ii
   if Ii111Ii11 [ 4 ] == 0 :
    iiOOooooO0Oo ( I1111i , oO0o0 , '' , OOoOooOoOOOoo , o0ooooO0o0O , '' , 'fav' )
   else :
    iiOOooooO0Oo ( I1111i , oO0o0 , Ii111Ii11 [ 4 ] , OOoOooOoOOOoo , o0ooooO0o0O , '' , 'fav' )
    if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . iiiiiiii1 / o000O0o
def ii1iI11 ( name ) :
 o0000oO = json . loads ( open ( IIIii1II1II ) . read ( ) )
 for OOOO000oo0o00 in range ( len ( o0000oO ) ) :
  if o0000oO [ OOOO000oo0o00 ] [ 0 ] == name :
   del o0000oO [ OOOO000oo0o00 ]
   I11iI1 = open ( IIIii1II1II , "w" )
   I11iI1 . write ( json . dumps ( o0000oO ) )
   I11iI1 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 14 - 14: o0o00Oo0O * o0o00Oo0O - o0o00Oo0O
 if 55 - 55: o000O0o / O0OOOoOoo0 . oOo0O0Ooo * iiiiiiii1 % iiiiiiii1 - I11i
def ooOOo0o ( ) :
 o0o0O0oOooOo = os . path . join ( I11i1 , 'addons.ini' )
 Ooi1IIii1i = open ( o0o0O0oOooOo , "w+" )
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oO0OOoo0OO )
 Ooi1IIii1i . write ( r'[' + IiII + ']' + '\n' )
 for I1111i , o00O0O , O00oo , oO0o0 in i1IIIII11I1IiI :
  oO0o0 = ( oO0o0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  O0oOo0o0O0o = ( I1111i + '=plugin://' + IiII + '/?url=' + oO0o0 + '&mode=10012&name=' + ( I1111i ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;description=' )
  Ooi1IIii1i . write ( O0oOo0o0O0o + '\n' )
  if 76 - 76: o0o00Oo0O
  if 71 - 71: oOo0O0Ooo . ooOoO0O00
def Ii1iIIII1i ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '24/7' , oO0o0 , 90021 , III1iII1I1ii + '247Streams.png' )
  if 84 - 84: ooOoO0O00 - oOo0O0Ooo % O0OOOoOoo0
def oO00o0oOoo ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , III1iII1I1ii + '247Streams.png' , III1iII1I1ii + '247Streams.png' , '' )
def ii111iiIii ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def iiI ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def oOOI1 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def OOI1i ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 i1IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , oO0o0 , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 47 - 47: O0OOOoOoo0 . OOooOOo
  if 58 - 58: O0OOOoOoo0 + I1ii11iIi11i / oOo0O0Ooo
def o000OO00OoO00 ( ) :
 if 97 - 97: I11i1ii1 / iI11I1II1I1I % I11i1ii1 / oOo0O0Ooo * O0OOOoOoo0 % OOooOOo
 iiOOooooO0Oo ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 if 17 - 17: iI11I1II1I1I
def ooi11I ( ) :
 if 48 - 48: Ii1IIIi1 + iiiiiiii1 % Ii1IIIi1
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i , I1I1i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + '  -  ' + ( I1I1i ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oO0o0 , 10023 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 84 - 84: o0o00Oo0O % ii1ii11IIIiiI . ii1ii11IIIiiI . O0OOOoOoo0 * ooOOOoO
  if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
  if 61 - 61: oOo0O0Ooo + o000O0o % iiiiiiii1 % iI11I1II1I1I - ii
def iIIiI1 ( ) :
 if 4 - 4: ii + O0OOOoOoo0 % o0o00Oo0O + iI11I1II1I1I % O0OOOoOoo0 * Ii
 iiOOooooO0Oo ( '[COLOR' + II + ']Action[/COLOR]' , 'Aksiyon' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Adventure[/COLOR]' , 'Macera' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Animation[/COLOR]' , 'Animasyon' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Anime[/COLOR]' , 'Anime' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Biography[/COLOR]' , 'Biyografi' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Comedy[/COLOR]' , 'Komedi' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Drama[/COLOR]' , 'Dram' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Family[/COLOR]' , 'Aile' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']History[/COLOR]' , 'Tarih' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Horror[/COLOR]' , 'Korku' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Mystery[/COLOR]' , 'Gizem' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Romance[/COLOR]' , 'Romantik' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Sport[/COLOR]' , 'Spor' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Western[/COLOR]' , 'Tarih' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 if 32 - 32: OOooOOo + I11i1ii1 + ii1ii11IIIiiI + oOo0O0Ooo
def I1IIIIII1 ( url ) :
 iIi1IIiIII1 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0OOoo0OO = cloudflare . source ( iIi1IIiIII1 )
 i1IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 99 - 99: Ii1IIIi1 + oOo0O0Ooo . Ii1I * ii
  if 82 - 82: Ii + iI11I1II1I1I / I1ii11iIi11i + Ii1IIIi1 * IIiIiII11i
  if 34 - 34: I11i % ii
  if 36 - 36: oOo0O0Ooo
def Oo0ooo ( ) :
 if 73 - 73: IIiIiII11i + Ii1IIIi1 * O0OOOoOoo0 / O0OOOoOoo0
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 oO0o0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o00O ) . replace ( ' ' , '+' )
 oO0OOoo0OO = cloudflare . source ( oO0o0 )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  if o00O in I1111i . lower ( ) :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 10022 , III1iII1I1ii + 'dtv.png' )
   if 74 - 74: o0o00Oo0O + iI11I1II1I1I + o000O0o * I1111IIi
   if 39 - 39: iiiiiiii1 . oO0o % I11i1ii1 . Ii1IIIi1 / O0OOOoOoo0 * oO0o
   if 12 - 12: oOo0O0Ooo / I11i
def oOO0O00o0O0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOOo0oo0O , IiI1i , ooOooO , I1111i in i1IIIII11I1IiI :
  oooo = ( ooOooO ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  IIIiI1iIIII = ( IiI1i ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0oo00OOOo = 'Season ' + IIIiI1iIIII + 'Episode ' + oooo + I1111i
  oo0oOi1i1IIi ( o0oo00OOOo , oOOo0oo0O )
  if 93 - 93: o000O0o
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 85 - 85: ooOoO0O00
  if 100 - 100: ii / ooOOOoO % oO0o + ii1ii11IIIiiI
def oo0oOi1i1IIi ( name , url ) :
 oOOo0oo0O = url
 IIi11 = name
 O0 = cloudflare . source ( oOOo0oo0O )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for oO0O , oO0OO0O0 in i1I :
  i1iIiiiiii1II ( '[COLOR' + II + ']' + IIi11 + oO0OO0O0 + '[/COLOR]' , oO0O , 10012 , III1iII1I1ii + 'dtv.png' )
  if 18 - 18: oOo0O0Ooo - OOooOOo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: Ii1IIIi1 + oO0o * o000O0o - o000O0o . Ii1I * ooOOOoO
 if 95 - 95: Ii1I / OOooOOo
def oOoOoOoo0 ( ) :
 if 10 - 10: I1111IIi % Ii1I - I1111IIi
 if 86 - 86: I1ii11iIi11i
 if 88 - 88: iiiiiiii1 * oOo0O0Ooo
 if 30 - 30: OOooOOo / o000O0o / ii1ii11IIIiiI * I11i * o000O0o . oOo0O0Ooo
 if 93 - 93: OOooOOo
 if 97 - 97: Ii
 if 68 - 68: I1111IIi * oO0o . ooOOOoO / ii1ii11IIIiiI . I11i - Ii
 iiOOooooO0Oo ( '[COLOR' + II + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , '' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 49 - 49: I1ii11iIi11i / ii1ii11IIIiiI % ooOOOoO + o000O0o - oO0o
def i11ii ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1iiIi1IiiiI = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + o00O0O , '' , '' )
 for url in i1iiIi1IiiiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 79 - 79: Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
def oOOo00ooO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1iiIi1IiiiI = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  o00O0O = 'http://watchepisodes.cc/' + o00O0O
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10093 , o00O0O , o00O0O , '' )
 for url in i1iiIi1IiiiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 64 - 64: ooOoO0O00
def I111I ( url , iconimage ) :
 o00O0O = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ooOooO , url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ooOooO + ' - ' + I1111i + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , o00O0O , '' , '' )
  if 62 - 62: ii + I1111IIi
def iIiIi1i1Iiii ( url , iconimage ) :
 o00O0O = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  if 'player' in I1111i :
   pass
  elif 'vod' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , o00O0O , '' , '' )
   if 78 - 78: I1ii11iIi11i - iiiiiiii1 + O0OOOoOoo0 * ii1ii11IIIiiI * I11i
   if 23 - 23: I1ii11iIi11i - o0o00Oo0O
   if 33 - 33: Ii1I
   if 54 - 54: I11i1ii1 * Ii1I . IIiIiII11i / Ii1IIIi1 % Ii1IIIi1
   if 25 - 25: Ii + Ii1I - ii . o0o00Oo0O % iiiiiiii1
   if 53 - 53: ooOoO0O00
def III1ii1I ( ) :
 if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
 if 9 - 9: ooOoO0O00 - OOooOOo
 if 57 - 57: iI11I1II1I1I * ii1ii11IIIiiI * O0OOOoOoo0 / o000O0o
 if 46 - 46: ii1ii11IIIiiI
 if 61 - 61: I11i / I11i1ii1 - IIiIiII11i
 if 87 - 87: Ii1I / oOo0O0Ooo
 if 45 - 45: OOooOOo * I11i1ii1 / ii + oO0o . iiiiiiii1 / oO0o
 if 64 - 64: ii1ii11IIIiiI / ooOoO0O00 % oOo0O0Ooo - I11i
 if 11 - 11: Ii1I - ii
 if 16 - 16: I1111IIi % ii - I11i1ii1 * ii1ii11IIIiiI - ii1ii11IIIiiI
 if 27 - 27: I1111IIi + iI11I1II1I1I / I1ii11iIi11i + oO0o % I1ii11iIi11i + oO0o
 if 77 - 77: I1ii11iIi11i * I11i1ii1 % ii1ii11IIIiiI
 if 2 - 2: ooOOOoO / I1ii11iIi11i / ii1ii11IIIiiI / Ii1I / ii
 if 22 - 22: iI11I1II1I1I * oOo0O0Ooo / ooOOOoO + OOooOOo
 iiOOooooO0Oo ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , III1iII1I1ii + 'latest.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , III1iII1I1ii + 'popular.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , III1iII1I1ii + 'Genre.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , III1iII1I1ii + 'series.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 if 98 - 98: Ii1IIIi1
 if 69 - 69: IIiIiII11i + I1ii11iIi11i - o000O0o . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
def oOooooooO0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 III11II1I1Ii1 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( III11II1I1Ii1 ) )
 for url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 54 - 54: ii1ii11IIIiiI . o0o00Oo0O
def O00O0ii11i1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 12 - 12: OOooOOo + I11i . iiiiiiii1
def ooO00OO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if 'episode' in url :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 64 - 64: I11i1ii1 - I11i % O0OOOoOoo0 % iiiiiiii1 . o000O0o
  if 100 - 100: oO0o % OOooOOo / ooOOOoO * o0o00Oo0O - o000O0o
def I1IiIi1iiI ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiII1II11i = 'http://www.watchseriesgo.to/search/' + o00O . replace ( ' ' , '%20' )
 oO0OOoo0OO = OoOooO ( iiII1II11i )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'watch online' in I1111i :
   pass
  else :
   print oO0o0
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to' + oO0o0 , 10044 , o00O0O , '' , '' )
   if 78 - 78: Ii / o000O0o
   xbmcplugin . setContent ( O000oo0O , 'movies' )
   if 85 - 85: I11i1ii1 - oOo0O0Ooo / ooOoO0O00 / oO0o / IIiIiII11i
def oo0O0O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , ooOooO , ii1Oo0000oOo in i1IIIII11I1IiI :
  oo0oo = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( ooOooO ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + oo0oo + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , o00O0O , '' , ii1Oo0000oOo )
  if 45 - 45: I1ii11iIi11i % I1ii11iIi11i + I1ii11iIi11i / o0o00Oo0O % ii
def O0oIii11IiiIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  oo0oo = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + oo0oo + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 81 - 81: I1ii11iIi11i * O0OOOoOoo0 * oO0o
def ooOOO0oOoooOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , o00O0O , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 16 - 16: o0o00Oo0O % I1111IIi % I1ii11iIi11i - ii + ii
def O0o0ooOoO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 III11II1I1Ii1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for IiI1i , I111 in III11II1I1Ii1 :
  i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( I111 ) )
  for url , I1111i in i1IIIII11I1IiI :
   oo0oo = ( IiI1i ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + oo0oo + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 27 - 27: oOo0O0Ooo % I1111IIi
class IiIIIii1i1iI ( ) :
 if 99 - 99: iI11I1II1I1I - o000O0o - OOooOOo / iI11I1II1I1I * I1ii11iIi11i - o000O0o
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 72 - 72: I1111IIi % ooOoO0O00 / iI11I1II1I1I
  oo0oo = name
  self . Get_Sources ( oO0o0 , oo0oo )
  if 95 - 95: o0o00Oo0O . oO0o
  if 89 - 89: ooOoO0O00
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  oO0OOoo0OO = OoOooO ( URL )
  i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oO0o0 , I1111i in i1IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + oO0o0
   self . Get_site_link ( URL , season_name )
   if 19 - 19: I11i1ii1 / I11i % I1111IIi - ii1ii11IIIiiI
 def Get_site_link ( self , url , season_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  ooOoO00 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for url in i1IIIII11I1IiI :
   self . main ( url , season_name )
  for url in i1I :
   self . main ( url , season_name )
  for url in ooOoO00 :
   self . main ( url , season_name )
   if 14 - 14: Ii1I - Ii * iiiiiiii1
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   iiii = 'DACLIPS'
   if iiii in IiIIIii1i1iI . source_list :
    pass
   else :
    self . daclips ( url , season_name , iiii )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    iiii = 'THEVIDEO'
    if iiii in IiIIIii1i1iI . source_list :
     pass
    else :
     self . thevideo ( url , season_name , iiii )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     iiii = 'ALLMYVIDEOS'
     if iiii in IiIIIii1i1iI . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , iiii )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      iiii = 'VIDSPOT'
      if iiii in IiIIIii1i1iI . source_list :
       pass
      else :
       self . vidspot ( url , season_name , iiii )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       iiii = 'VODLOCKER'
       if iiii in IiIIIii1i1iI . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , iiii )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        iiii = 'VIDTO'
        if iiii in IiIIIii1i1iI . source_list :
         pass
        else :
         self . vidto ( url , season_name , iiii )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 80 - 80: oOo0O0Ooo
       else :
        if 'youwatch' in url :
         iiii = 'YouWatch'
         if iiii in IiIIIii1i1iI . source_list :
          pass
         else :
          self . youwatch ( url , season_name , iiii )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 58 - 58: o000O0o + Ii1I % OOooOOo
          if 22 - 22: iI11I1II1I1I - ii1ii11IIIiiI / oOo0O0Ooo * I1111IIi
 def allmyvid ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for OoO , I1111i in i1IIIII11I1IiI :
   self . Printer ( OoO , season_name , source_name )
   if 26 - 26: I11i + Ii1IIIi1 - I11i + I1ii11iIi11i . o000O0o
 def vidspot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for OoO , I1111i in i1IIIII11I1IiI :
   self . Printer ( OoO , season_name , source_name )
   if 97 - 97: ooOoO0O00
 def thevideo ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( oO0OOoo0OO )
  for OoO in i1IIIII11I1IiI :
   self . Printer ( OoO , season_name , source_name )
   if 46 - 46: Ii1I
 def vodlocker ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for OoO in i1IIIII11I1IiI :
   self . Printer ( OoO , season_name , source_name )
   if 30 - 30: oO0o / o0o00Oo0O * I11i * iiiiiiii1 + ii * O0OOOoOoo0
 def daclips ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oO0OOoo0OO )
  for OoO in i1IIIII11I1IiI :
   self . Printer ( OoO , season_name , source_name )
   if 23 - 23: ooOOOoO
 def filehoot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for OoO in i1IIIII11I1IiI :
   self . Printer ( OoO , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for OoO in i1IIIII11I1IiI :
   self . Printer ( OoO , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for OoO in i1IIIII11I1IiI :
   self . youplay ( OoO , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for OoO in i1IIIII11I1IiI :
   self . Printer ( OoO , season_name , source_name )
   if 36 - 36: I1111IIi . O0OOOoOoo0 - ooOoO0O00 + iiiiiiii1
 def Printer ( self , Link , season_name , source_name ) :
  if 54 - 54: ii . o000O0o - O0OOOoOoo0
  if Link in IiIIIii1i1iI . List :
   pass
  elif source_name in IiIIIii1i1iI . source_list :
   pass
  else :
   i1iIiiiiii1II ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 10012 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   IiIIIii1i1iI . List . append ( Link )
   IiIIIii1i1iI . source_list . append ( source_name )
   if 76 - 76: iiiiiiii1
   xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 61 - 61: I11i1ii1 / IIiIiII11i * I11i1ii1 * OOooOOo * iiiiiiii1 . Ii
   if 26 - 26: iiiiiiii1 / I11i1ii1 - oO0o . iI11I1II1I1I
   if 83 - 83: I11i1ii1 % ii1ii11IIIiiI / I1ii11iIi11i - O0OOOoOoo0 / o0o00Oo0O
   if 97 - 97: iI11I1II1I1I * ooOOOoO
   if 95 - 95: oO0o
def OO0 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 68 - 68: iI11I1II1I1I . iI11I1II1I1I / OOooOOo - IIiIiII11i - iI11I1II1I1I
def o0o0O0o ( url ) :
 iiOOooooO0Oo ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( iIIII )
 for I111ii1III1I , url , OO0o0oo , o0oo0oOOOo00 , OO0OOO , IiIi1II111I , Oo0O00OO , oooOo0OOOoo0 , oooOoO , o0OO00O00oO , I11O0O0o in i1IIIII11I1IiI :
  OO0o0oo = OO0o0oo
  if 'Arsenal' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'arsenal-logo.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                                  ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Bournemouth' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'afc-bournemouth.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                       ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Burnley' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'KEGnQWW.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                                   ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Chelsea' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'chelsea.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                                  ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Crystal' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'CrystalPalace.0.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                       ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Everton' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'Everton.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                                   ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Hull' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'hull-city-afc.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                                 ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Leicester' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'leicester-city-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                       ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Liverpool' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'liverpool-logo.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                               ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Manchester City' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'city-logo.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '               ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Manchester United' in OO0o0oo :
   i11111I1I = III1iII1I1ii + '91.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '          ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Middlesbrough' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'middlesbrough-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                 ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Southampton' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'southampton-fc-logo.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                   ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Stoke City' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'stoke-city.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                          ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Sunderland' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'sunderland-logo.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                        ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Swansea' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'swansea-city-afc.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                    ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Tottenham' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'tottenham-hotspur_zps4e3ed7c1.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '        ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Watford' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'watford-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '                              ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'Bromwich' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'west-bromwich-albion-logo.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '   ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  elif 'West Ham' in OO0o0oo :
   i11111I1I = III1iII1I1ii + 'west-ham.png'
   I1111i = '[COLOR' + II + ']' + I111ii1III1I + ' - ' + OO0o0oo + '             ' + o0oo0oOOOo00 + '        ' + OO0OOO + '        ' + IiIi1II111I + '        ' + Oo0O00OO + '        ' + oooOo0OOOoo0 + '        ' + oooOoO + '        ' + o0OO00O00oO + '[/COLOR]'
  iiOOooooO0Oo ( str ( I1111i ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , i11111I1I , i11111I1I , OO0o0oo )
  if 45 - 45: OOooOOo
def oo0OoOO000O ( description ) :
 OO0o0oo = description
 oO0o0 = ( 'http://www.fullmatchesandshows.com/?s=' + OO0o0oo ) . replace ( ' ' , '%20' )
 Oo0o0OoOoOo0 ( oO0o0 )
 if 36 - 36: ii1ii11IIIiiI * oOo0O0Ooo * Ii1I . ooOOOoO * Ii1I
def O0ooO0 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 i1IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oO0o0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o00O0O , O0o0Oo , '' )
  if 41 - 41: I11i % I1ii11iIi11i
def o00oOo0OoO0oO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 III11II1I1Ii1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for III11II1I1Ii1 in III11II1I1Ii1 :
  iI = re . compile ( '(.*?)</h2>' ) . findall ( str ( III11II1I1Ii1 ) )
  for OoOo in iI :
   OoOo = OoOo
  iIoOO0OO00 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( III11II1I1Ii1 ) )
  for O0oO00oO0o00o , o00O0O , time , o0OOo0O00OO0O in iIoOO0OO00 :
   I11iI1I = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( o0OOo0O00OO0O )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + OoOo + ' - ' + O0oO00oO0o00o + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + o00O0O , O0o0Oo , ( str ( I11iI1I ) ) )
   if 58 - 58: o000O0o
 I1I11i ( 'tvshows' , 'Media Info 3' )
 if 50 - 50: ii * Ii1I - o0o00Oo0O
def I1iO00O000oOO0oO ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , III1iII1I1ii + 'fanart.jpg' , '' )
 if 88 - 88: I11i . oOo0O0Ooo % o000O0o . I1ii11iIi11i % I11i1ii1 . o000O0o
def OoO0ooOOoo ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  OOO0oOoO00OoO = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   OOO0oOoO00OoO = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   i1iIiiiiii1II ( '[COLOR' + II + ']' + OOO0oOoO00OoO + '[/COLOR]' , url , 10013 , o00O0O )
 for url , o00O0O , I1111i in i1I :
  OOO0oOoO00OoO = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   i1iIiiiiii1II ( '[COLOR' + II + ']' + OOO0oOoO00OoO + '[/COLOR]' , url , 10013 , o00O0O )
def Oo0o0OoOoOo0 ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 if 23 - 23: oOo0O0Ooo - I11i % o000O0o . o0o00Oo0O * ii + I11i1ii1
 if 53 - 53: I1ii11iIi11i
 if 3 - 3: I1111IIi - ii * ii - oOo0O0Ooo / iiiiiiii1 * Ii1I
 if 58 - 58: I1111IIi % iI11I1II1I1I / Ii % I11i . iiiiiiii1 * O0OOOoOoo0
 if 32 - 32: ii + I11i
 if 91 - 91: I11i1ii1 - iiiiiiii1 * iiiiiiii1
 if 55 - 55: iI11I1II1I1I + oOo0O0Ooo - I1ii11iIi11i
 for url , o00O0O , I1111i in i1I :
  OOO0oOoO00OoO = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   i1iIiiiiii1II ( '[COLOR' + II + ']' + OOO0oOoO00OoO + '[/COLOR]' , url , 10013 , o00O0O )
   if 24 - 24: oO0o / iiiiiiii1 + O0OOOoOoo0 * ooOOOoO * O0OOOoOoo0
def IiIIIIIii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oO0OOoo0OO )
 for oO0O in i1IIIII11I1IiI :
  iIIiiiIIi1111 = ( oO0O ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOOOo0o00OO0000 ( 'http:' + iIIiiiIIi1111 )
  if 53 - 53: iiiiiiii1
  if 31 - 31: I11i * ooOOOoO - Ii - oOo0O0Ooo
  if 19 - 19: O0OOOoOoo0 . ooOOOoO * ii - Ii1IIIi1 + o0o00Oo0O * iiiiiiii1
  if 90 - 90: ooOoO0O00 . o000O0o / iiiiiiii1 . Ii1IIIi1 / iiiiiiii1
def i1111I1iii1 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  i1iIiiiiii1II ( I1111i , url , 8046 , o00O0O )
 for url in i1I :
  IiiIiI1Ii1i ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def o0Oo00o0 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 42 - 42: iiiiiiii1 / OOooOOo % o000O0o
def oOOoOo0Ooo ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 95 - 95: iiiiiiii1 % I1ii11iIi11i
def o0OoOO ( ) :
 IiiIiI1Ii1i ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , III1iII1I1ii + 'documentary.png' )
 IiiIiI1Ii1i ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , III1iII1I1ii + 'documentary.png' )
 IiiIiI1Ii1i ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , III1iII1I1ii + 'Search.png' )
 iIIII = i11i1iiiII ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , oO0o0 , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo000OO ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + o00O0O )
 for url in next :
  IiiIiI1Ii1i ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 13 - 13: iI11I1II1I1I + O0OOOoOoo0 / ii1ii11IIIiiI / ooOoO0O00 % oO0o - iI11I1II1I1I
  if 60 - 60: iiiiiiii1
def ooO0 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   i1iIiiiiii1II ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   IiiIiI1Ii1i ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def IIiIIiiiiiII1 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  i1iIiiiiii1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10012 , '' )
  if 7 - 7: Ii1I - iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOOo0Oooo ( name , url ) :
 I1iiIIiI11I = 0
 name = name
 url = url
 i1Oo0oO00o = [ '144' , '240' , '380' , '480' , '720' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OOOOo0o00OO0000 ( url )
  if 29 - 29: ooOOOoO + o000O0o % I11i1ii1 + OOooOOo
  if 92 - 92: I11i
  if 37 - 37: o000O0o
  if 18 - 18: I1111IIi * Ii + iI11I1II1I1I % ooOOOoO + ooOoO0O00 - oO0o
  if 85 - 85: oO0o * ooOOOoO + oO0o
  if 39 - 39: I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
  if 20 - 20: Ii1IIIi1 * o000O0o
  if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . Ii1IIIi1
def IIiiIiIIiI1 ( ) :
 iIIII = i11i1iiiII ( 'http://documentarylovers.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  if 'genre' in oO0o0 :
   IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oO0o0 , 80010 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1IiI ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , o00O0O )
 for url in next :
  IiiIiI1Ii1i ( 'NEXT PAGE' , url , 80010 , III1iII1I1ii + 'Next.png' )
  if 79 - 79: OOooOOo + I1111IIi
def I1I11Oo0 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( iIIII )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
 for url in i1I :
  IIiIIiiiiiII1 ( url )
  if 6 - 6: iiiiiiii1 / ii / O0OOOoOoo0 / iiiiiiii1 + O0OOOoOoo0 - OOooOOo
def oO0iIiII111 ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Oo000 = 'http://documentarylovers.com/?s=' + ( o00O ) . replace ( ' ' , '+' )
 i1iIIi = Oo000 . lower ( )
 I1IiI ( i1iIIi )
 if 98 - 98: oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
def I1Ii111I111 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if 'films' in url :
   IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , III1iII1I1ii + 'documentary.png' )
def iIi11 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  if 'films' in url :
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + o00O0O )
 for url in i1I :
  IiiIiI1Ii1i ( 'NEXT' , url , 8049 , III1iII1I1ii + 'Next.png' )
def O00oOoOo0ooO0O0oo ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'rtd' in url :
   ii11IiI ( url )
   if 14 - 14: ooOOOoO - I1ii11iIi11i . I1ii11iIi11i * Ii1IIIi1 . oOo0O0Ooo % O0OOOoOoo0
def ii11IiI ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iIIII )
 for i1i , file in i1IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1i + file )
  OOOOo0o00OO0000 ( url )
  if 86 - 86: oOo0O0Ooo + ooOOOoO * OOooOOo - iiiiiiii1 / iiiiiiii1
  if 9 - 9: I11i / O0OOOoOoo0 . iI11I1II1I1I % o0o00Oo0O
def i11ii11IiI1 ( ) :
 oO0OOoo0OO = i11i1iiiII ( 'http://www.stream2watch.co/live-tv' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i , i1i1IIIIIIIi in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( I1111i + '[COLOR' + II + ']' + i1i1IIIIIIIi + '[/COLOR]' ) , oO0o0 , 8086 , o00O0O )
  if 47 - 47: iI11I1II1I1I % ooOOOoO . ooOOOoO / o0o00Oo0O . Ii * ii1ii11IIIiiI
def iio0Oo ( url ) :
 oO0OOoo0OO = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8087 , o00O0O )
  if 29 - 29: o0o00Oo0O * Ii / ii / I11i . I11i1ii1
def OoIII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  OO00O ( url , I1111i )
  if 66 - 66: ii1ii11IIIiiI / o0o00Oo0O . ooOOOoO + O0OOOoOoo0 - ii1ii11IIIiiI . ooOOOoO
def OO00O ( url , name ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  print url
  i1iIiiiiii1II ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 2 - 2: Ii1I . I1ii11iIi11i * Ii1IIIi1 % IIiIiII11i . O0OOOoOoo0
def II1i1iI ( ) :
 iIIII = i11i1iiiII ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oO0o0 , 3002 , 'http://www.solie.org/alibrary/' + o00O0O )
def iI111I1 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def iIiii1IIi1I ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 IiIiii1IiI = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIIII )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , I1111i in IiIiii1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']Season- ' + I1111i + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  IiiIiI1Ii1i ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , o00O0O , I1111i in i1I :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def oo0o0ooOoo00O ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  iI1ii1 ( url )
def iI1ii1 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 81 - 81: I11i1ii1 + oO0o . ooOoO0O00 + ooOoO0O00 / oOo0O0Ooo * iiiiiiii1
def Iii ( ) :
 iIIII = i11i1iiiII ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oO0o0 , 8065 , III1iII1I1ii + 'classicmovies.png' )
def OOooooO0 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  iIiIIiii1II ( url )
  if 23 - 23: O0OOOoOoo0 / OOooOOo + I11i . o0o00Oo0O
def i1iI1 ( ) :
 iIIII = i11i1iiiII ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oO0o0 , 8065 , III1iII1I1ii + 'classictv.png' )
def OOOoO00oo0ooOo0 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'mp4' in url :
   OOOOo0o00OO0000 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 49 - 49: IIiIiII11i
def II1I1Ii11 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oO0o0 , 8071 , III1iII1I1ii + 'streams.png' )
def I1I1iiI ( url ) :
 oO0OOoo0OO = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  if '(Free Access)' in I1111i :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def o0oOOO0 ( url ) :
 oO0OOoo0OO = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , o00O0O , o0ooooO0o0O , '' )
  if 11 - 11: ooOOOoO / OOooOOo
def ii1IIi1IIIIi1 ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  iI1i1iii ( 'http://watchxxxfree.com/categories' )
 if i11I1II1I11i == 1 :
  Ii11II1IIIIIi ( 'http://www.perfectgirls.net' )
 if i11I1II1I11i == 2 :
  Oo0ooOO ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 3 :
  Iiii ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 4 :
  Oo0ooOO ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 5 :
  Oo0ooOO ( 'http://www.xvideos.com/verified/videos' )
 if i11I1II1I11i == 6 :
  Ii11i1I1 ( 'http://www.xvideos.com/tags' )
 if i11I1II1I11i == 7 :
  OOI1 ( 'http://www.xvideos.com/porn' )
 if i11I1II1I11i == 8 :
  oooO00oOOooO ( )
  if 34 - 34: iI11I1II1I1I / IIiIiII11i
  if 3 - 3: I11i - ii + O0OOOoOoo0 . ooOOOoO
  if 88 - 88: ooOOOoO - O0OOOoOoo0
  if 68 - 68: I1ii11iIi11i % o000O0o . I1111IIi - I11i / ooOoO0O00 / ii
  if 34 - 34: ooOOOoO % I1ii11iIi11i + ii1ii11IIIiiI
  if 93 - 93: ii1ii11IIIiiI - iiiiiiii1 % o0o00Oo0O
  if 11 - 11: Ii
  if 6 - 6: IIiIiII11i
  if 1 - 1: I11i1ii1 % I1ii11iIi11i . o000O0o
def OoOooo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if 'ch' in url :
   II11IiI1 ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Jizbox.png' , III1iII1I1ii + 'Jizbox.png' , '' )
def i11iI1111ii1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oO0OOoo0OO )
 OoOo0 = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 for I1111i , url in OoOo0 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Next.png' , '' , '' )
def iiIIii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   O000oo00o000o ( url )
def O0000ooO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def iI1i1iii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , Ii1 in i1IIIII11I1IiI :
  if 'category' in url :
   II11IiI1 ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   ' + Ii1 + '[/COLOR]' , url , 90006 , o00O0O , III1iII1I1ii + 'Jizbox.png' , '' )
def O00OoO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OoOo0 = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , o00O0O , '' , '' )
 for url in OoOo0 :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , III1iII1I1ii + 'Next.png' , '' , '' )
def I11i11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   O000oo00o000o ( url )
def O000oo00o000o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def Ii11II1IIIIIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , Ii1 in i1IIIII11I1IiI :
  if 'category' in url :
   II11IiI1 ( '[COLOR' + II + ']' + I1111i + '[COLORorange]' + Ii1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def oooo0OOO00O00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 oOOo0oo0O = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OoOo0 = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , o00O0O , '' , '' )
 for url in OoOo0 :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , oOOo0oo0O + '/' + url , 90003 , III1iII1I1ii + 'Next.png' , '' , '' )
def i11I111I1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOoO000 ( 'http://www.perfectgirls.net' + url )
def OOOoO000 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( 'http://' + url )
def OOI1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , Ii1 in i1IIIII11I1IiI :
  II11IiI1 ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + Ii1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def Ii11i1I1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OoOo0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in OoOo0 :
  II11IiI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , Ii1 in i1IIIII11I1IiI :
  II11IiI1 ( ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + ( Ii1 + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 79 - 79: O0OOOoOoo0 / iiiiiiii1 + I11i
def oO0oOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OoOo0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in OoOo0 :
  II11IiI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , o00oO0o00O in i1IIIII11I1IiI :
  II11IiI1 ( I1111i + '--' + ( o00oO0o00O ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( o00O0O ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 84 - 84: Ii / I11i % iI11I1II1I1I . I11i1ii1 . oO0o / O0OOOoOoo0
  if 55 - 55: O0OOOoOoo0
def Oo0ooOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , O0Oooo , ii1iIII1iIiIIIIi in i1IIIII11I1IiI :
  II11IiI1 ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + ii1iIII1iIiIIIIi + ' - [COLORred]' + O0Oooo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , o00O0O , o00O0O , ii1iIII1iIiIIIIi + ' - ' + O0Oooo )
 ii11I = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in ii11I :
  II11IiI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 54 - 54: Ii1IIIi1
def Iiii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 III11II1I1Ii1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OoOo0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in OoOo0 :
  II11IiI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( III11II1I1Ii1 ) )
 for url , I1111i in i1IIIII11I1IiI :
  if '/c/' in url :
   II11IiI1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
   if 63 - 63: OOooOOo * Ii . OOooOOo
   if 91 - 91: o0o00Oo0O - ooOOOoO % iiiiiiii1
def oooO00oOOooO ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii = ( o00O ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 i1iIIi = I1ii . lower ( )
 I1I = 'http://www.xvideos.com/?k=' + i1iIIi
 print I1I + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0OOoo0OO = OoOooO ( I1I )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , oO0o0 , I1111i , O0Oooo , ii1iIII1iIiIIIIi in i1IIIII11I1IiI :
  II11IiI1 ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + ii1iIII1iIiIIIIi + ' - [COLORred]' + O0Oooo + '[/COLOR]' , 'http://www.xvideos.com' + oO0o0 , 10108 , o00O0O , o00O0O , ii1iIII1iIiIIIIi + ' - ' + O0Oooo )
 ii11I = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for oO0o0 in ii11I :
  II11IiI1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oO0o0 , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
if 78 - 78: oO0o / iI11I1II1I1I . ii1ii11IIIiiI * oO0o * OOooOOo - Ii1IIIi1
if 39 - 39: Ii - Ii1IIIi1 - iiiiiiii1 + ii / oOo0O0Ooo / iI11I1II1I1I
if 16 - 16: OOooOOo / ii1ii11IIIiiI . iiiiiiii1 % Ii % oOo0O0Ooo / Ii1IIIi1
if 85 - 85: ooOOOoO + iiiiiiii1
if 11 - 11: ooOOOoO
if 95 - 95: I1ii11iIi11i + Ii % Ii1IIIi1 - o000O0o
if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
if 95 - 95: iiiiiiii1 + I1111IIi * iI11I1II1I1I
if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / ii1ii11IIIiiI
if 19 - 19: ooOoO0O00 - iI11I1II1I1I . ooOOOoO
if 2 - 2: ii1ii11IIIiiI
if 12 - 12: Ii - iI11I1II1I1I * I1111IIi * O0OOOoOoo0
if 19 - 19: o0o00Oo0O + o000O0o + I11i
if 81 - 81: iI11I1II1I1I
if 51 - 51: I11i . Ii1I * ii1ii11IIIiiI / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
if 44 - 44: Ii % iiiiiiii1 % o000O0o + ooOOOoO * o000O0o . ii1ii11IIIiiI
if 89 - 89: ii % IIiIiII11i - oO0o % Ii
if 7 - 7: I1111IIi
if 15 - 15: I1ii11iIi11i + O0OOOoOoo0 + oOo0O0Ooo * I11i
if 33 - 33: I11i * I1ii11iIi11i
if 88 - 88: iiiiiiii1 % Ii1IIIi1 - OOooOOo - OOooOOo . oOo0O0Ooo
if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - iiiiiiii1
if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
if 66 - 66: iI11I1II1I1I * IIiIiII11i % I1ii11iIi11i % oOo0O0Ooo - ii1ii11IIIiiI
if 59 - 59: I1111IIi % o000O0o
if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
if 15 - 15: I11i1ii1 / I11i1ii1 % ii . iiiiiiii1
if 93 - 93: Ii1I * Ii1I / ii
if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
if 19 - 19: o0o00Oo0O % IIiIiII11i * I11i
if 27 - 27: Ii1IIIi1 * I1111IIi / Ii - o000O0o + IIiIiII11i
if 43 - 43: Ii1I - IIiIiII11i
if 56 - 56: Ii1I . ooOoO0O00 / O0OOOoOoo0 % o000O0o / o0o00Oo0O * ooOOOoO
if 98 - 98: o0o00Oo0O + O0OOOoOoo0
if 23 - 23: ii . iI11I1II1I1I / ooOoO0O00
def IIiii1I1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   i1iIiiiiii1II ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   i1iIiiiiii1II ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in ooOoO00 :
  if 'http' in url :
   i1iIiiiiii1II ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 62 - 62: IIiIiII11i - OOooOOo * ii1ii11IIIiiI
def oO0OO0O ( url ) :
 OooOOO0O00 = xbmc . Player ( IIii1i1iii1 ( ) )
 import urlresolver
 try : OooOOO0O00 . play ( url )
 except : pass
 if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
 if 30 - 30: OOooOOo - Ii
def oO0OOOO00o ( ) :
 if 26 - 26: I11i1ii1 + OOooOOo
 if 17 - 17: Ii1I - O0OOOoOoo0 % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * Ii1IIIi1
 if 6 - 6: iiiiiiii1
 if 46 - 46: IIiIiII11i * iiiiiiii1
 if 23 - 23: ooOoO0O00 - o0o00Oo0O
 if 6 - 6: I11i1ii1 % ii * iiiiiiii1 - I1111IIi
 if 24 - 24: ooOOOoO / iI11I1II1I1I . ii % OOooOOo . ii1ii11IIIiiI
 if 73 - 73: iiiiiiii1
 if 25 - 25: I1111IIi
 if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 8091 , III1iII1I1ii + 'gofish.png' )
def OoooooO0 ( url ) :
 oO0OOoo0OO = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  IiiIiI1Ii1i ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
def iIOOOO00 ( url ) :
 oO0OOoo0OO = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 I11IIII1iI = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O in I11IIII1iI :
  o00O0O = o00O0O
 for url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  IiiIiI1Ii1i ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
  if 37 - 37: oO0o - I1ii11iIi11i
def iiII ( url ) :
 oO0OOoo0OO = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 15 - 15: ooOOOoO % oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
  if 89 - 89: o0o00Oo0O + I1111IIi * iiiiiiii1
  if 30 - 30: OOooOOo
  if 39 - 39: Ii1I + I11i + iiiiiiii1 + I1111IIi
i1i1 = '{PQ},' ; IiiIi = '{SC},' ; IIiiIiI = '{XG},' ; I1 = '{JP},' ; O0oO0oo0oOO = '{HW},' ; iiII1iIi1ii1i = '{RT},'
def iIII ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 Ii11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 oO0o0 = 'http://onlinemovies.tube/?s=' + ( o00O ) . replace ( ' ' , '+' )
 oOOo0oo0O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 II1i111 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1iiiIii11 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OOoOOO000O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oOo0II1i11I1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiIiIiII = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o00O
 i1I1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 49 - 49: OOooOOo
 I1iII11iIII1i1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oOO0oo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 99 - 99: o0o00Oo0O + I1111IIi + I11i1ii1 - I11i1ii1 * Ii1I / I1111IIi
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oO0o0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( oOOo0oo0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1i111 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( i1iiiIii11 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 iii1III1i = O0o0O00Oo0o0 ( OOoOOO000O0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iiiIi = O0o0O00Oo0o0 ( iiIiIiII )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 II1Iii = O0o0O00Oo0o0 ( i1I1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0oooo0OoO0oo = O0o0O00Oo0o0 ( iIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 82 - 82: I11i - Ii1IIIi1
 if 84 - 84: O0OOOoOoo0 % ooOoO0O00 % oO0o % IIiIiII11i
 OOOOOoOO0OOoo = O0o0O00Oo0o0 ( I1iII11iIII1i1I )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 IIIi11IiIiii = O0o0O00Oo0o0 ( oOO0oo )
 if 94 - 94: I11i1ii1 * o0o00Oo0O
 if 60 - 60: O0OOOoOoo0 / O0OOOoOoo0 - I11i1ii1 / ii + o0o00Oo0O
 if 55 - 55: oO0o % o0o00Oo0O / ii
 if 49 - 49: oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
 if 88 - 88: Ii1I * O0OOOoOoo0 + IIiIiII11i
 if 62 - 62: ii
 if 33 - 33: o0o00Oo0O . Ii % I11i
 if 50 - 50: I11i1ii1
 if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * Ii1IIIi1
 if 83 - 83: Ii - oOo0O0Ooo * Ii
 if 59 - 59: O0OOOoOoo0 - ii / I11i1ii1 + Ii1I . I11i - O0OOOoOoo0
 if 29 - 29: o000O0o
 if 26 - 26: o0o00Oo0O % Ii1IIIi1 - I1111IIi . Ii1IIIi1
 if O0oooo0OoO0oo != 'Failed' :
  o00oo0000 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0oooo0OoO0oo )
  for oO0o0 , I1111i in o00oo0000 :
   iIi1IIi1ii = O0o0O00Oo0o0 ( oO0o0 )
   I11Ii = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi1IIi1ii )
   for iIiII , i1i1IIIIIIIi in I11Ii :
    i1i1IIIIIIIi = ( i1i1IIIIIIIi . replace ( '.' , ' ' ) )
    if i1iIIi in i1i1IIIIIIIi . lower ( ) :
     if '.mkv' in iIiII :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiII , 222 , '' , '' , '' )
     elif '.mp4' in iIiII :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiII , 222 , '' , '' , '' )
     elif '.avi' in iIiII :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiII , 222 , '' , '' , '' )
     elif '.wav' in iIiII :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiII , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiII , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 70 - 70: I11i + ooOOOoO / O0OOOoOoo0 + I11i1ii1 / oOo0O0Ooo
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in i1I :
   if o00O in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source Technica[/COLOR]' ) , oO0o0 , 222 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 33 - 33: ii . o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: iI11I1II1I1I
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for III11iiii11i1 , I1111i in ooOoO00 :
   if o00O in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( II1i111 + III11iiii11i1 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in Iii1I1111ii :
   if o00O in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source RaizTv[/COLOR]' ) , oO0o0 , 222 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 45 - 45: o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1III1i != 'Failed' :
  IiIIII = [ ]
  iIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iii1III1i )
  for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in iIiI :
   if o00O in I1111i . lower ( ) :
    if I1111i in IiIIII :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oO0o0 , 1016 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
     IiIIII . append ( I1111i )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if iiiIi != 'Failed' :
  oOOo = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iiiIi )
  for oO0o0 , o00O0O , I1111i in oOOo :
   if o00O in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oO0o0 , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 78 - 78: ooOOOoO - iI11I1II1I1I + iiiiiiii1 - Ii1I - iiiiiiii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 21 - 21: ii . o0o00Oo0O / Ii
    if 86 - 86: OOooOOo / Ii1IIIi1
    if 40 - 40: iI11I1II1I1I / I11i1ii1 / oOo0O0Ooo + Ii1I * Ii1IIIi1
    if 1 - 1: oO0o * I11i1ii1 + I1111IIi . o000O0o / I11i1ii1
    if 91 - 91: ii1ii11IIIiiI + ooOOOoO - I1ii11iIi11i % OOooOOo . O0OOOoOoo0
    if 51 - 51: Ii1IIIi1 / ooOOOoO
    if 51 - 51: I11i1ii1 * o000O0o - iiiiiiii1 + O0OOOoOoo0
    if 46 - 46: I11i - Ii % oO0o / ii1ii11IIIiiI - OOooOOo
    if 88 - 88: o000O0o * oOo0O0Ooo / oO0o - Ii1IIIi1 / ooOoO0O00 . iiiiiiii1
    if 26 - 26: Ii - I11i1ii1
    if 45 - 45: I11i1ii1 + IIiIiII11i % O0OOOoOoo0
    if 55 - 55: I11i1ii1 - o000O0o % oOo0O0Ooo
    if 61 - 61: I11i1ii1
    if 22 - 22: iI11I1II1I1I / I11i1ii1 / oOo0O0Ooo - I11i
    if 21 - 21: o000O0o . Ii * ooOOOoO . Ii1IIIi1 / Ii1IIIi1
    if 42 - 42: ii / iiiiiiii1 . I11i / o0o00Oo0O - I1111IIi * I1111IIi
    if 1 - 1: ii1ii11IIIiiI % iiiiiiii1
    if 97 - 97: OOooOOo
 if OOOOOoOO0OOoo != 'Failed' :
  oo0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OOOOOoOO0OOoo )
  for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in oo0O :
   if o00O in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source APPRENTICE[/COLOR]' ) , oO0o0 , 222 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 13 - 13: OOooOOo % Ii1IIIi1 . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 19 - 19: iiiiiiii1 % I11i1ii1 - I11i1ii1 % oOo0O0Ooo . Ii1IIIi1 - ii
    if 100 - 100: oOo0O0Ooo + ii1ii11IIIiiI + I11i . ooOoO0O00 % ii
    if 64 - 64: o0o00Oo0O % ooOoO0O00 * iiiiiiii1 - ii1ii11IIIiiI + I1ii11iIi11i
    if 65 - 65: OOooOOo . Ii
    if 36 - 36: o000O0o * O0OOOoOoo0 + I1111IIi * O0OOOoOoo0 . Ii1I - iI11I1II1I1I
    if 14 - 14: ooOOOoO * o000O0o + Ii
    if 84 - 84: O0OOOoOoo0 / IIiIiII11i
    if 86 - 86: oOo0O0Ooo
    if 97 - 97: IIiIiII11i
    if 38 - 38: oOo0O0Ooo
 Iiii1ii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 42 - 42: I11i
 for oo0OO in Iiii1ii :
  IiiI11i1I = O0Oo000ooO00 + oo0OO + I1IIIii
  O0oooo0OoO0oo = O0o0O00Oo0o0 ( IiiI11i1I )
  if O0oooo0OoO0oo != 'Failed' :
   o00oo0000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0oooo0OoO0oo )
   for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in o00oo0000 :
    if o00O in I1111i . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , oO0o0 , 222 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 8 - 8: Ii / I11i1ii1
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 33 - 33: iiiiiiii1 * I1111IIi - o0o00Oo0O + oOo0O0Ooo / I1111IIi
 Iiii1ii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 if 85 - 85: I1111IIi - I11i % Ii1IIIi1 - IIiIiII11i
 for oo0OO in Iiii1ii :
  IiiI11i1I = Ii11 + oo0OO
  oo0O0o00 = O0o0O00Oo0o0 ( IiiI11i1I )
  if oo0O0o00 != 'Failed' :
   oOoO0o = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0O0o00 )
   for III11iiii11i1 , I1111i in oOoO0o :
    if o00O in I1111i . lower ( ) :
     i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( Ii11 + oo0OO + III11iiii11i1 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 56 - 56: ii1ii11IIIiiI * Ii
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 92 - 92: IIiIiII11i - o0o00Oo0O . iiiiiiii1
def O0oO0OOoOOO0oO ( ) :
 if 59 - 59: OOooOOo
 if 47 - 47: IIiIiII11i - Ii1I - ii1ii11IIIiiI
 if 9 - 9: Ii1I - I1111IIi
 if 64 - 64: ooOoO0O00
 if 71 - 71: I1111IIi * I11i
 if 99 - 99: I11i
 if 28 - 28: ii % o0o00Oo0O - Ii1IIIi1 / I11i / oOo0O0Ooo
 if 41 - 41: IIiIiII11i * I1111IIi / oO0o . o000O0o
 if 50 - 50: ii + iI11I1II1I1I / o000O0o / Ii1IIIi1 . Ii . I11i1ii1
 if 75 - 75: iI11I1II1I1I % I11i1ii1 / Ii1IIIi1 - O0OOOoOoo0 % Ii
 if 11 - 11: ooOOOoO . ii1ii11IIIiiI
 if 87 - 87: Ii1IIIi1 + Ii1IIIi1
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
 if 87 - 87: OOooOOo - oO0o * oO0o / ii1ii11IIIiiI . ooOOOoO * I11i
 if 21 - 21: IIiIiII11i
 if 29 - 29: OOooOOo % ii1ii11IIIiiI
 if 7 - 7: ooOoO0O00 / I1111IIi / O0OOOoOoo0
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 if 97 - 97: oO0o + iI11I1II1I1I
 if 79 - 79: I11i1ii1 + o000O0o - IIiIiII11i . I1ii11iIi11i
 iIiII = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( o00O ) . replace ( ' ' , '+' )
 oOOo0oo0O = 'http://onlinemovies.tube/?s=' + ( o00O ) . replace ( ' ' , '+' )
 II1i111 = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i1iiiIii11 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oOo0II1i11I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 26 - 26: I1111IIi
 i1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 Oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 52 - 52: o0o00Oo0O + I11i1ii1
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 11 - 11: ooOoO0O00 / iiiiiiii1 * Ii1I * iiiiiiii1 * I11i1ii1 - Ii
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 96 - 96: Ii1I % Ii1I
 if 1 - 1: oOo0O0Ooo . ii1ii11IIIiiI
 iiii111IiIIi1 = O0o0O00Oo0o0 ( iIiII )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( oOOo0oo0O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1i111 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( i1iiiIii11 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 oo0O0o00 = O0o0O00Oo0o0 ( oOo0II1i11I1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 26 - 26: o000O0o - I11i1ii1 % I1ii11iIi11i - o000O0o + I1111IIi
 if 33 - 33: ii1ii11IIIiiI + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * I1111IIi
 II1Iii = O0o0O00Oo0o0 ( i1I1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 O0oooo0OoO0oo = O0o0O00Oo0o0 ( iIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 ooOOoOo = O0o0O00Oo0o0 ( Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 21 - 21: o0o00Oo0O * I11i1ii1 % oO0o
 if O0oooo0OoO0oo != 'Failed' :
  o00oo0000 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0oooo0OoO0oo )
  for oO0o0 , I1111i in o00oo0000 :
   iIi1IIi1ii = O0o0O00Oo0o0 ( oO0o0 )
   I11Ii = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi1IIi1ii )
   for iIiII , i1i1IIIIIIIi in I11Ii :
    if i1iIIi in i1i1IIIIIIIi . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + i1i1IIIIIIIi + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiII , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 14 - 14: o0o00Oo0O / iiiiiiii1 / I11i1ii1 + I1111IIi - I1111IIi
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if II1Iii != 'Failed' :
  iIiIii1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II1Iii )
  for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in iIiIii1ii :
   if i1iIIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source HeroVision[/COLOR]' ) , oO0o0 , 1016 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 10 - 10: o0o00Oo0O - Ii1I / iiiiiiii1 % OOooOOo / ii / ii1ii11IIIiiI
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 73 - 73: I11i1ii1 + I1111IIi % I11i . Ii1I / Ii1IIIi1 . iiiiiiii1
    if 76 - 76: ooOOOoO . Ii1I * ii % O0OOOoOoo0
    if 24 - 24: ii
    if 83 - 83: o0o00Oo0O / oO0o
    if 62 - 62: ooOOOoO
    if 73 - 73: ii1ii11IIIiiI % oO0o * Ii1IIIi1
    if 84 - 84: I1ii11iIi11i
    if 18 - 18: ii
    if 85 - 85: ii . oO0o . oO0o
    if 70 - 70: ooOOOoO
    if 72 - 72: iiiiiiii1 - I11i1ii1 - oOo0O0Ooo - O0OOOoOoo0 + Ii1IIIi1 - ooOoO0O00
 if ooOOoOo != 'Failed' :
  ooOI1iI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOOoOo )
  for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in ooOI1iI :
   if i1iIIi in I1111i . lower ( ) :
    IiiIiI1Ii1i ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] RaizTv[/COLOR]' , oO0o0 , 1016 , OOoOooOoOOOoo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 45 - 45: oO0o * oOo0O0Ooo
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  i1iIIi1o0o0OoOOOOOo = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for oO0o0 , o00O0O , I1111i , Ii11iii1II1i in i1I :
   if i1iIIi in I1111i . lower ( ) :
    if 'season' in Ii11iii1II1i :
     IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90054 , o00O0O , o00O0O , '' )
    if 'episodes' in Ii11iii1II1i :
     IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90044 , o00O0O , o00O0O , '' )
  for oO0o0 in i1iIIi1o0o0OoOOOOOo :
   IiiIiI1Ii1i ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 61 - 61: O0OOOoOoo0 % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if iiii111IiIIi1 != 'Failed' :
  OoOOo0O00 = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( iiii111IiIIi1 )
  for oO0o0 , I1111i , o00O0O in OoOOo0O00 :
   if i1iIIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oO0o0 , 8022 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 74 - 74: Ii1I * o000O0o + O0OOOoOoo0 % o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 18 - 18: ooOoO0O00 % I1111IIi . o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - IIiIiII11i
    if 55 - 55: OOooOOo . iI11I1II1I1I * Ii1IIIi1 % iI11I1II1I1I . oO0o
    if 43 - 43: ii1ii11IIIiiI . Ii1IIIi1 + oOo0O0Ooo * Ii
    if 2 - 2: Ii1IIIi1
    if 3 - 3: oOo0O0Ooo . O0OOOoOoo0 % o0o00Oo0O - I11i1ii1 / o0o00Oo0O
    if 79 - 79: ii1ii11IIIiiI + o000O0o % I11i1ii1 % oOo0O0Ooo
    if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
    if 53 - 53: O0OOOoOoo0 . o000O0o / I1ii11iIi11i . oO0o . Ii
    if 60 - 60: IIiIiII11i
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for I1111i in ooOoO00 :
   if i1iIIi in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( II1i111 + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 25 - 25: I1ii11iIi11i + I11i - oO0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for I1111i in Iii1I1111ii :
   if i1iIIi in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i1iiiIii11 + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 57 - 57: IIiIiII11i . ooOoO0O00
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0O0o00 != 'Failed' :
  oOoO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0O0o00 )
  for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in oOoO0o :
   if i1iIIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] Source Scooby[/COLOR]' ) , oO0o0 , 1016 , OOoOooOoOOOoo , oOo00 , ii1Oo0000oOo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 33 - 33: O0OOOoOoo0 + I1ii11iIi11i % ooOOOoO . o000O0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 6 - 6: I1111IIi + Ii1I
 OOOo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oo0OO in OOOo :
  IiiI11i1I = O0Oo000ooO00 + oo0OO + I1IIIii
  OOOOOoOO0OOoo = O0o0O00Oo0o0 ( IiiI11i1I )
  if OOOOOoOO0OOoo != 'Failed' :
   oo0O = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OOOOOoOO0OOoo )
   for I1111i , ii1Oo0000oOo , oO0o0 , o00O0O , o0ooooO0o0O , ii1ii111 in oo0O :
    if i1iIIi in I1111i . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , oO0o0 , ii1ii111 , o00O0O , o0ooooO0o0O , ii1Oo0000oOo )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 62 - 62: o000O0o . iiiiiiii1 - ii * IIiIiII11i . Ii
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 13 - 13: iI11I1II1I1I * I11i - Ii
     if 63 - 63: ii * iiiiiiii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1Iiiii ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( o00O ) . replace ( ' ' , '+' )
 if 70 - 70: ii / Ii1IIIi1 - oO0o % ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oO0o0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 25 - 25: I1ii11iIi11i % I11i % ooOoO0O00
 if oO0OOoo0OO != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oO0o0 , I1111i in i1I :
   if o00O in I1111i . lower ( ) :
    i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oO0o0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 31 - 31: I1111IIi . IIiIiII11i % I1ii11iIi11i * ii1ii11IIIiiI + ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
oo0O0o = '{ZH},' ; OoiiI1I = '{IX},' ; OOOOo0o0O0 = '{LM},'
if 7 - 7: Ii1IIIi1 . I1111IIi . iiiiiiii1 / ii1ii11IIIiiI / I1ii11iIi11i
def o0Ooo ( url ) :
 iI11IIiII = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iI11IIiII )
 for url , IiI1i , I1I1i , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( IiI1i ) . replace ( 'Sezon' , ' Season ' ) + ( I1I1i ) . replace ( 'Bölüm' , ' Episode ' ) + I1111i , url , 8063 , '' )
  if 20 - 20: oOo0O0Ooo + ooOoO0O00
  if 89 - 89: I11i1ii1 % o000O0o * ii1ii11IIIiiI - I1ii11iIi11i / I11i + oO0o
  if 56 - 56: Ii * O0OOOoOoo0 / Ii * ii1ii11IIIiiI . iI11I1II1I1I . Ii1I
  if 93 - 93: OOooOOo + ooOOOoO
def ii1IiIiI1iiii ( url ) :
 iI11IIiII = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iI11IIiII )
 for url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( I1111i , url , 222 , '' )
  if 13 - 13: IIiIiII11i % ooOoO0O00 - OOooOOo + O0OOOoOoo0
  if 59 - 59: ii + iiiiiiii1 % I11i - OOooOOo . oOo0O0Ooo
  if 42 - 42: iiiiiiii1
  if 70 - 70: I11i / ooOOOoO + o000O0o % oOo0O0Ooo % I1ii11iIi11i + oO0o
def ooo0ooo0Oo ( ) :
 if 40 - 40: I1111IIi . ii . oOo0O0Ooo + o0o00Oo0O % ooOoO0O00 / I1111IIi
 iI11IIiII = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iI11IIiII )
 for oO0o0 , o00O0O , I1111i , I1I1i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i + '  -  ' + ( I1I1i ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oO0o0 , 8063 , o00O0O )
  if 36 - 36: ii - OOooOOo - oO0o * iiiiiiii1 - o000O0o
def O0ooO ( ) :
 iIIII = i11i1iiiII ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i , o00O0O in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 8002 , o00O0O )
def OOo000OOoOO ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , time , url , I1111i , iiII1i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '%s %s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , time ) , url , 1015 , o00O0O , iiII1i )
  if 13 - 13: I1ii11iIi11i
def oO0OooO00Oo ( ) :
 if 81 - 81: Ii1I - oO0o * o000O0o
 IiiIiI1Ii1i ( 'Coronation Street' , '' , 8001 , '' )
 IiiIiI1Ii1i ( 'Eastenders' , '' , 8002 , '' )
 IiiIiI1Ii1i ( 'Emmerdale' , '' , 8003 , '' )
 IiiIiI1Ii1i ( 'Hollyoaks' , '' , 8004 , '' )
 IiiIiI1Ii1i ( 'Im a Celebrity' , '' , 8005 , '' )
 if 81 - 81: O0OOOoOoo0 - ii1ii11IIIiiI - Ii1IIIi1 % I1111IIi % I11i . iI11I1II1I1I
 if 79 - 79: Ii1I - Ii1I . ii1ii11IIIiiI / I1111IIi
 if 57 - 57: I11i1ii1 * iI11I1II1I1I * O0OOOoOoo0 * ii1ii11IIIiiI / ii1ii11IIIiiI
 if 43 - 43: o0o00Oo0O * Ii - ii - o000O0o
def iIiiI1iIiI1I ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Holly' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oO0o0 :
    i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 90 - 90: Ii1I - O0OOOoOoo0 . Ii / oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 41 - 41: iiiiiiii1 * oO0o - O0OOOoOoo0 . ii1ii11IIIiiI
def IiIiIIII ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'East' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oO0o0 :
    i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 93 - 93: O0OOOoOoo0 - o0o00Oo0O
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 84 - 84: O0OOOoOoo0 % oOo0O0Ooo / iI11I1II1I1I * ii1ii11IIIiiI * iI11I1II1I1I + Ii1I
def O000o ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Emmer' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oO0o0 :
    i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 76 - 76: Ii1IIIi1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 52 - 52: I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
def i11i1IiIi ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Coro' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oO0o0 :
    i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 63 - 63: ooOOOoO
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 6 - 6: o000O0o / Ii1I / oO0o
def iiiiIIii1I ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Celeb' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oO0o0 :
    i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 14 - 14: Ii1IIIi1 * oOo0O0Ooo - Ii1I
def I1111I1i1i ( name , url ) :
 O0oOo = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if O0oOo :
  I1i1II = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIIII = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( iIIII ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIIII = open_url ( url )
  o000iiI11i = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( iIIII ) [ - 1 ]
  I1i1II = o000iiI11i . replace ( '\\/' , '/' )
 iIIII1i = xbmcgui . ListItem ( name , '' , '' )
 iIIII1i . setPath ( I1i1II )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIIII1i )
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
 if 60 - 60: Ii1I / I1111IIi . Ii / oO0o % IIiIiII11i
def i1II111II1 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oO0o0 , 7071 , III1iII1I1ii + 'popcorn.png' )
 for oO0o0 , I1111i in i1I :
  IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oO0o0 , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 8 - 8: I1111IIi - Ii1I * iI11I1II1I1I % I11i / ii * I11i
def oOoO00O00o ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Movies' in I1111i :
   IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( oO0o0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def ooO0O00O0O0 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 for url in i1I :
  IiiIiI1Ii1i ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 24 - 24: iI11I1II1I1I % I1ii11iIi11i % Ii
  if 55 - 55: O0OOOoOoo0
def I1i11i ( url ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in i1IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , o00O0O )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
Ii11I = '{UJ},' ; i11IiiI1iIiII = '{WE},' ; o0oOOoOoo = '{WP},' ; ooO0O = '{PP},'
def O0Ooo0O0O ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in i1IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOO0 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOo0OOo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOo0OOo ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: o000O0o . ii1ii11IIIiiI / o0o00Oo0O * o000O0o
 if 98 - 98: I1ii11iIi11i - o000O0o . iiiiiiii1
 if 51 - 51: O0OOOoOoo0 . Ii1I / ooOOOoO + I11i % Ii1IIIi1
def I1I11I11I1 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '(cooltvseries.com)' in I1111i :
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , I1111i in i1I :
  if '(cooltvseries.com)' in I1111i :
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def i1I11i ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( ( url ) . replace ( ' ' , '%20' ) )
IIi1Iii = '{XX},' ; O000o0O0Oo = '{UD},' ; i1i111i1I1 = '{YT},' ; I1IIo0o0OoOO00Oo = '{JS},' ; i1iiIi1II1 = '{PF},'
if 12 - 12: Ii + ooOOOoO - Ii1I
def iiiiIiii1I11 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i , o00O0O in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oO0o0 ) ) , 222 , o00O0O )
  if 48 - 48: ooOoO0O00 - I1111IIi + I11i1ii1 . O0OOOoOoo0 / o000O0o % iI11I1II1I1I
def oO00000oO0o0O ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  if 'youtu' in url :
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + o00O0O )
 for url in next :
  IiiIiI1Ii1i ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 96 - 96: I1ii11iIi11i . o000O0o + iI11I1II1I1I * OOooOOo - o0o00Oo0O
def ooo0O0O ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 17 - 17: oOo0O0Ooo
def Ooo0O0O ( url ) :
 iIIII = OoOooO
 i1IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , o00O0O )
  if 45 - 45: OOooOOo / oOo0O0Ooo
  if 34 - 34: I11i % Ii1I + ii1ii11IIIiiI * ooOOOoO / o000O0o
  if 18 - 18: I11i1ii1
  if 92 - 92: oO0o % iI11I1II1I1I / I1111IIi * O0OOOoOoo0 . ooOoO0O00 + o000O0o
  if 24 - 24: I1111IIi . O0OOOoOoo0 * I1111IIi % Ii . Ii + ooOoO0O00
def Ooo0 ( ) :
 if 53 - 53: I11i1ii1 - OOooOOo + I1111IIi
 IiiIiI1Ii1i ( 'All Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'Entertainment' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'Movies' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'Music' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'News' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'Sports' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'Documentary' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'Kids' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'Food' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'Religious' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'USA Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 IiiIiI1Ii1i ( 'Other' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 if 100 - 100: o000O0o + oO0o
 if 95 - 95: Ii . I11i + ii % I1ii11iIi11i
def I1iI11ii ( Cat_Name ) :
 if 21 - 21: O0OOOoOoo0
 iIiii1Ii = False
 iiI11Ii1 = '0'
 if Cat_Name == 'All Channels' : iIiii1Ii = True
 if Cat_Name == 'Entertainment' : iiI11Ii1 = '1'
 if Cat_Name == 'Movies' : iiI11Ii1 = '2'
 if Cat_Name == 'Music' : iiI11Ii1 = '3'
 if Cat_Name == 'News' : iiI11Ii1 = '4'
 if Cat_Name == 'Sports' : iiI11Ii1 = '5'
 if Cat_Name == 'Documentary' : iiI11Ii1 = '6'
 if Cat_Name == 'Kids' : iiI11Ii1 = '7'
 if Cat_Name == 'Food' : iiI11Ii1 = '8'
 if Cat_Name == 'Religious' : iiI11Ii1 = '9'
 if Cat_Name == 'USA Channels' : iiI11Ii1 = '10'
 if Cat_Name == 'Other' : iiI11Ii1 = '11'
 if 37 - 37: I1ii11iIi11i + iiiiiiii1 * o000O0o / I11i
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIII )
 print 'Len Match: >>>' + str ( len ( i1IIIII11I1IiI ) )
 for I1111i , o00O0O , O0O0OOo in i1IIIII11I1IiI :
  ii1i111 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  if O0O0OOo == iiI11Ii1 :
   IiiIiI1Ii1i ( I1111i , '' , 7022 , ii1i111 )
  elif iIiii1Ii == True :
   IiiIiI1Ii1i ( I1111i , '' , 7022 , ii1i111 )
  else : pass
  if 66 - 66: iiiiiiii1 * ii / Ii1I - ooOOOoO - I11i1ii1 * ooOOOoO
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 80 - 80: o000O0o - Ii1I / ii / Ii1IIIi1
def o0oOoOOO ( Search_Name ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , oO0o0 , oOOo0oo0O , II1i111 in i1IIIII11I1IiI :
  ii1i111 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  i1iIiiiiii1II ( Search_Name + ': Link 1' , ( oO0o0 ) . replace ( '\\' , '' ) , 222 , ii1i111 )
  i1iIiiiiii1II ( Search_Name + ': Link 2' , ( oOOo0oo0O ) . replace ( '\\' , '' ) , 222 , ii1i111 )
  i1iIiiiiii1II ( Search_Name + ': Link 3' , ( II1i111 ) . replace ( '\\' , '' ) , 222 , ii1i111 )
  if 74 - 74: O0OOOoOoo0 / iiiiiiii1 / IIiIiII11i - O0OOOoOoo0 / o000O0o % ooOOOoO
def i1Iiiiii1II ( ) :
 iIIII = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  i1iIiiiiii1II ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def i1iII1i ( ) :
 iIIII = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  i1iIiiiiii1II ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def Ii1I11Ii1iI ( ) :
 iIIII = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  i1iIiiiiii1II ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 61 - 61: I11i * Ii1I - ooOoO0O00 + ooOOOoO % I11i + ii
def o0Oooo0O00Ooo ( url ) :
 url
 i11I = xbmcgui . ListItem ( I1111i , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11I )
 return
 if 84 - 84: ooOoO0O00
 if 73 - 73: Ii * Ii1I . ooOOOoO % oOo0O0Ooo - oOo0O0Ooo . OOooOOo
def OOoo ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIIII )
 for url , ii1Oo0000oOo , o00O0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + o00O0O , '' , ( ii1Oo0000oOo ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  IiiIiI1Ii1i ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 42 - 42: Ii1I / I11i1ii1 . iI11I1II1I1I
def iiiOOOoO0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , ii1Oo0000oOo , o00O0O in i1IIIII11I1IiI :
  OOiIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + o00O0O , '' , ii1Oo0000oOo )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 I111 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiioO000oO0oO in I111 :
  o000O0O = ( iiioO000oO0oO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiOOooooO0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + o00O0O , '' , o000O0O )
  if 44 - 44: Ii1IIIi1 - I1111IIi + O0OOOoOoo0
def oooo00OoOoO ( INFO ) :
 OO0O000 ( 'info for workout' , INFO )
 if 99 - 99: IIiIiII11i
 if 13 - 13: ooOOOoO - I11i1ii1 + O0OOOoOoo0 % ooOOOoO . O0OOOoOoo0 - ooOoO0O00
 if 67 - 67: Ii1IIIi1 . Ii + I11i1ii1 . iI11I1II1I1I
def iiIi1i ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( ( I1111i ) . replace ( 'SlyNet' , '' ) , url , 9031 , III1iII1I1ii + 'Sport.png' )
def I1i11IIiiIiI ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , url , 9032 , III1iII1I1ii + 'icon.png' )
def II1iiiiI1Ii11 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   i1iIiiiiii1II ( ( I1111i ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , III1iII1I1ii + 'icon.png' )
def O0oo ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   i1iIiiiiii1II ( I1111i , url , 222 , III1iII1I1ii + 'icon.png' )
   if 13 - 13: oO0o * iiiiiiii1 + I1ii11iIi11i - I1111IIi
   if 31 - 31: oO0o
   if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
def Ooo00OoO ( url ) :
 i1iIiiiiii1II ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 i1iIiiiiii1II ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 IiiIiI1Ii1i ( '[COLOR' + II + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , III1iII1I1ii + 'bamf.png' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   pass
  else :
   i1iIiiiiii1II ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOOOoo000Ooo ( url ) :
 i1iIiiiiii1II ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 i1iIiiiiii1II ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 IiiIiI1Ii1i ( '[COLOR' + II + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , III1iII1I1ii + 'bamf.png' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   i1iIiiiiii1II ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 46 - 46: ooOoO0O00 + o0o00Oo0O
 if 5 - 5: I11i + oOo0O0Ooo / ii % Ii % ii - I11i
 if 53 - 53: oO0o + Ii / iI11I1II1I1I
def i1iI11IiII ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 i1IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Daily' in I1111i :
   IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 9008 , Oo00OOOOO )
def oO00Oo0OO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def i11iIIiii ( url ) :
 i1iIiiiiii1II ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 i1iIiiiiii1II ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 i1iIiiiiii1II ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , Oo00OOOOO )
  if 66 - 66: iiiiiiii1 - ooOOOoO . I1111IIi % o000O0o
def i1i1I1i111II ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if '.m3u' in oO0o0 :
   IiiIiI1Ii1i ( ( I1111i ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oO0o0 ) , 9011 , III1iII1I1ii + 'disclose.png' )
def OoO00OOoO ( url ) :
 iIIII = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 39 - 39: ooOoO0O00
def O0O0Oo00 ( ) :
 iIIII = OoOooO ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'category' in oO0o0 :
   IiiIiI1Ii1i ( I1111i , 'http://www.disclose.tv/' + oO0o0 , 7010 , III1iII1I1ii + 'disclose.png' )
   if 29 - 29: OOooOOo
   if 27 - 27: oOo0O0Ooo / ii
def OOO00Oo00o ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , 'http://www.disclose.tv/' + url , 7011 , o00O0O )
 for url in next :
  IiiIiI1Ii1i ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . Ii1IIIi1
  if 3 - 3: o0o00Oo0O - iiiiiiii1 * ii1ii11IIIiiI * Ii1IIIi1 / ii1ii11IIIiiI
def O0Ooo000OO00 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   i1iIiiiiii1II ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , I1111i in i1I :
  i1iIiiiiii1II ( I1111i , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in ooOoO00 :
  i1iIiiiiii1II ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 51 - 51: I11i1ii1 * I1111IIi * iI11I1II1I1I / OOooOOo % I1111IIi
  if 36 - 36: Ii1I * I11i + Ii + ii
def oOi1IiIiIii11I ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 80 - 80: iiiiiiii1 + ooOOOoO . iiiiiiii1 + Ii1IIIi1
def OoI11II ( name , url , img ) :
 oO0OOoo0OO = OoOooO ( url )
 Iii11IiIi = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OOOoO000oOOo = len ( Iii11IiIi )
 if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
 if 15 - 15: ii1ii11IIIiiI + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
 if OOOoO000oOOo == 1 :
  for O0ooO00OO in Iii11IiIi :
   O0ooO00OO = O0ooO00OO . replace ( 'player' , 'watch' )
   IiI11I1I111 = O0ooO00OO + '&fv=&sou='
   o00OoOoo0 = OoOooO ( IiI11I1I111 )
   iiiiiiiiiiiI = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( o00OoOoo0 )
   for OoO in iiiiiiiiiiiI :
    iI111iiI1II = False
    Resolve ( OoO )
    if 96 - 96: OOooOOo * o0o00Oo0O - IIiIiII11i . I11i1ii1 - ii1ii11IIIiiI
 elif OOOoO000oOOo > 1 :
  if 84 - 84: o000O0o * I11i * I11i - O0OOOoOoo0
  for O0ooO00OO in Iii11IiIi :
   III1Ii = OoOooO ( O0ooO00OO )
   oooOoOO0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( III1Ii )
   iI1Iii1i1I = oooOoOO0
   iI1Iii1i1I = ( str ( iI1Iii1i1I ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iI1Iii1i1I
   i1iIiiiiii1II ( 'DOUBLE LINK' , iI1Iii1i1I , 424 , '' )
   if 78 - 78: oOo0O0Ooo / ooOOOoO + I11i . I1ii11iIi11i / o0o00Oo0O
   for url in oooOoOO0 :
    IiiIiI1Ii1i ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     oOOo0oo0O = Google . resolve ( url )
    except :
     pass
    try :
     iIiiIIiiI = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( oOOo0oo0O ) )
     for I1IIIi1ii1i , iI1I1iii11i in iIiiIIiiI :
      if 14 - 14: ii1ii11IIIiiI + ii1ii11IIIiiI * ii * ooOOOoO + I1ii11iIi11i . oOo0O0Ooo
      HD_URLS . append ( I1IIIi1ii1i )
      SD_URLS . append ( iI1I1iii11i )
    except :
     pass
 else :
  pass
  if 61 - 61: Ii1IIIi1 . Ii1IIIi1
def ii11 ( ) :
 if 43 - 43: OOooOOo % ii1ii11IIIiiI + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
 if 98 - 98: I11i * I1ii11iIi11i - ii1ii11IIIiiI . I11i1ii1
 IiiIiI1Ii1i ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 2 - 2: I1ii11iIi11i - I11i1ii1 % iI11I1II1I1I
 IiiIiI1Ii1i ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 88 - 88: iiiiiiii1 - oO0o
 if 79 - 79: O0OOOoOoo0
def Iii1i1 ( ) :
 iIIII = OoOooO ( 'http://cnfstudio.com/' )
 i1IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , 'http://cnfstudio.com/genre/' + oO0o0 , 7003 , III1iII1I1ii + 'icon.png' )
  if 92 - 92: I11i
OOooO0OOoo = xbmcgui . Dialog ( )
if 23 - 23: ooOoO0O00 + Ii1I + ii1ii11IIIiiI + Ii1I . I11i1ii1
oOooO = '{UN},' ; OO00o0OoOOOo = '{IG},' ; I1ioO000O0oO00 = '{PL},' ; i1Ii1IIii = '{LO},' ; Ii1IIiiiI = '{LP},' ; Ii1IiIi11i1 = '{HA},' ; OO0OOo00Oo = '{XD},' ; IiI1iIIiIi1Ii = '{TA},' ; O0oOoOOO000 = '{DP},' ; oOo00o0oO = '{JT},' ; iIiIi = '{JJ},' ; I1Iii11II = '{MM},' ; ii11III1 = '{FQ},' ; OOOoO0oo0oo0o = '{HH},'
if 70 - 70: iI11I1II1I1I + I11i * o000O0o
def OOOoooO0o0o ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIIII )
 OOoOoOO00 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , o00O0O )
 OOoOoOO00 = OOoOoOO00
 for url in OOoOoOO00 :
  IiiIiI1Ii1i ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 65 - 65: I1111IIi / Ii1I
def OooOoO000OOoo0 ( url ) :
 if 44 - 44: oO0o % Ii . iiiiiiii1 - o0o00Oo0O / O0OOOoOoo0 . I11i1ii1
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1i = url + '&fv=&sou='
  i1i = i1i . replace ( 'player' , 'watch' )
  iIiI1I1IIi1 = oooOOOoO ( i1i )
  OOOOoO0O = oooOOOoO ( url )
  if 79 - 79: Ii
  if 81 - 81: O0OOOoOoo0 + I1111IIi - Ii
def oooOOOoO ( url ) :
 if 60 - 60: iiiiiiii1
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  iIiIIiii1II ( url )
  if 14 - 14: I1ii11iIi11i % o000O0o * O0OOOoOoo0 - Ii / Ii1I * Ii
  if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * ooOOOoO + Ii1IIIi1
def i1i11IiII ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , III1iII1I1ii + 'LocalM3U.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , III1iII1I1ii + 'RemoteM3U.png' , O0o0Oo , '' )
 if 94 - 94: iI11I1II1I1I / oOo0O0Ooo * Ii1I
def I1i1ii1IiI1i ( ) :
 if os . path . exists ( iiI1IiI ) :
  oo0O00o0oO00 = open ( iiI1IiI , 'r' )
  for i11I in oo0O00o0oO00 :
   Iii1Iii = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( i11I )
   for I1111i , oO0o0 in Iii1Iii :
    i1iIiiiiii1II ( I1111i , oO0o0 , 222 , III1iII1I1ii + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 56 - 56: ii1ii11IIIiiI % Ii
def I1i11iiII111I ( url ) :
 if os . path . exists ( Remote ) :
  oO0OOoo0OO = i11i1iiiII ( url )
  i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1111i , url in i1IIIII11I1IiI :
   url = ( url ) . strip ( )
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 49 - 49: I1ii11iIi11i
  if 57 - 57: o0o00Oo0O * I11i1ii1 - O0OOOoOoo0 - iI11I1II1I1I * O0OOOoOoo0
def Iiii1i1 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oO0o0 in i1IIIII11I1IiI :
  oO0o0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oO0o0
 I1111i = 'plugin.video.GenieTv'
 if 9 - 9: I1111IIi . ooOOOoO
 IiIiiiIii1i ( oO0o0 , I1111i )
 if 71 - 71: I11i . Ii1I % IIiIiII11i / iI11I1II1I1I % OOooOOo - Ii1I
def i1IiiiI1iI ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oO0o0 in i1IIIII11I1IiI :
  oO0o0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oO0o0
 I1111i = 'repository.GenieTv'
 if 58 - 58: iI11I1II1I1I + I11i1ii1 / oO0o % I11i1ii1 % I11i % iI11I1II1I1I
 IiIiiiIii1i ( oO0o0 , I1111i )
 if 48 - 48: o0o00Oo0O % ooOOOoO * IIiIiII11i . I1ii11iIi11i . Ii1I
 if 62 - 62: OOooOOo / IIiIiII11i
def iI1i11iII111 ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OOO0o0oOOo ( )
 if i11I1II1I11i == 1 :
  ooO0000 ( )
  if 51 - 51: oOo0O0Ooo * iiiiiiii1 / o000O0o % O0OOOoOoo0
  if 41 - 41: Ii
  if 34 - 34: IIiIiII11i + I1ii11iIi11i . o000O0o
  if 36 - 36: ooOoO0O00 + O0OOOoOoo0 / Ii1I
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
ooO00OO0ooo = 'https://addons.tvaddons.ag/'
if 78 - 78: I11i1ii1 . oOo0O0Ooo . iiiiiiii1 / o0o00Oo0O % ii % Ii
def ooO0000 ( ) :
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 I1I = 'https://addons.tvaddons.ag/search/?keyword=' + i1iIIi
 oO0OOoo0OO = OoOooO ( I1I )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , i11111I1I , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , oO0o0 , 10054 , 'https://addons.tvaddons.ag/' + i11111I1I , O0o0Oo , '' )
  if 72 - 72: O0OOOoOoo0 / Ii1IIIi1 * o0o00Oo0O
  if 18 - 18: o0o00Oo0O
def OOO0o0oOOo ( ) :
 oO0OOoo0OO = OoOooO ( ooO00OO0ooo )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'Repositories' in I1111i :
   pass
  elif 'Services' in I1111i :
   pass
  elif 'International' in I1111i :
   pass
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 10053 , 'https://addons.tvaddons.ag/' + o00O0O , O0o0Oo , '' )
   if 14 - 14: ii1ii11IIIiiI / I1111IIi - o0o00Oo0O
   if 16 - 16: iiiiiiii1 % iI11I1II1I1I . ooOoO0O00
def Addon ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 o0O0oOOoo0O0 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'Please' in I1111i :
   pass
  else :
   OOiIiIIi1 ( I1111i , url , 10054 , 'https://addons.tvaddons.ag/' + o00O0O , O0o0Oo , '' )
 for url in o0O0oOOoo0O0 :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
  if 71 - 71: Ii1I + ooOOOoO * I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % Ii
  if 40 - 40: I11i1ii1 - Ii % Ii1I % oOo0O0Ooo . I1111IIi * oO0o
def OoOO000OO00 ( url , name ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( o00O0 , name + '.zip' )
   try :
    os . remove ( oOO0O00Oo0O0o )
   except :
    pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   ii1 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print ii1
   print '======================================='
   extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
   O0O0ooOOO ( )
   if 36 - 36: I1ii11iIi11i / iI11I1II1I1I - o0o00Oo0O + I11i1ii1 . Ii1I
def IiIiiiIii1i ( url , name ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , name + '.zip' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
 O0O0ooOOO ( )
 if 58 - 58: oO0o + O0OOOoOoo0 * I11i . ooOOOoO
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 48 - 48: Ii1IIIi1
 if 25 - 25: Ii1IIIi1 / I11i1ii1 % Ii1IIIi1
def o0OooOO0 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , i11111I1I , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , url , 1007 , i11111I1I )
def iI1i ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , i11111I1I , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , i11111I1I )
  if 22 - 22: I1111IIi / iI11I1II1I1I / I11i
  if 19 - 19: ii
def oOIIiIi ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , iconimage , ii1Oo0000oOo , o0ooooO0o0O , name in i1IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    OOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
    for i11I in OOo0 :
     if i11I == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    Ii1i ( name , url , 1016 , iconimage , o0ooooO0o0O , ii1Oo0000oOo )
   else :
    if 'youtube' in url :
     OOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for i11I in OOo0 :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IioOOO00Oo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , o0ooooO0o0O , ii1Oo0000oOo )
    else :
     OOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for i11I in OOo0 :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IioOOO00Oo ( name , url , 222 , iconimage , o0ooooO0o0O , ii1Oo0000oOo )
     I1I11i ( 'tvshows' , 'Media Info 3' )
  else :
   O0oooo0O0Oo0O ( url , iconimage , name )
   if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
 else :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
  for url , i11111I1I , name in i1IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     IiiIiI1Ii1i ( name , url , 1016 , i11111I1I )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      i1iIiiiiii1II ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , i11111I1I )
     else :
      OOo0 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for i11I in OOo0 :
       if i11I == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      i1iIiiiiii1II ( name , url , 222 , i11111I1I )
      I1I11i ( 'tvshows' , 'Media Info 3' )
   else :
    O0oooo0O0Oo0O ( url , i11111I1I , name )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 93 - 93: I11i1ii1 % iiiiiiii1
def O0oooo0O0Oo0O ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 II1I11iIIIii1 = ( url ) . replace ( OoiiI1I , 'http' ) . replace ( O000o0O0Oo , '.com' ) ;
 I11iIIiIIiIi = ( II1I11iIIIii1 ) . replace ( OOOOo0o0O0 , 'a' ) . replace ( IIiiIiI , 'b' ) . replace ( I1 , 'c' ) . replace ( i11IiiI1iIiII , 'd' ) . replace ( I1ioO000O0oO00 , 'e' ) . replace ( oOo00o0oO , 'f' ) ;
 ii1IiI = ( I11iIIiIIiIi ) . replace ( IIi1Iii , 'g' ) . replace ( Ii1IiIi11i1 , 'h' ) . replace ( i1i111i1I1 , 'i' ) . replace ( i1iiIi1II1 , 'j' ) . replace ( O0oO0oo0oOO , 'k' ) . replace ( iiII1iIi1ii1i , 'l' ) ;
 o0oO00O000O = ( ii1IiI ) . replace ( IiIIiIi1 , 'm' ) . replace ( ooOoo0OoO0 , 'n' ) . replace ( oO0OO00o , 'o' ) . replace ( oooooOOOO0oOo , 'p' ) . replace ( iiii1Ii , 'q' ) . replace ( IIiiiI , 'r' ) ;
 ii11iI1i1i1i1i = ( o0oO00O000O ) . replace ( iiII1i1II1iIi , 's' ) . replace ( o0oOOoOoo , 't' ) . replace ( iII , 'u' ) . replace ( OOOO0o0Oo0 , 'v' ) . replace ( I1iIiI1iiI , 'w' ) . replace ( oO000O00 , 'x' ) ;
 IiIIIii1iIII1 = ( ii11iI1i1i1i1i ) . replace ( OoOooooo0oo , 'y' ) . replace ( ii1II1 , 'z' ) . replace ( oOooO , '.' ) . replace ( OO00o0OoOOOo , '(' ) . replace ( i1Ii1IIii , ')' ) . replace ( Ii1IIiiiI , '/' ) ;
 i1I1II11I1 = ( IiIIIii1iIII1 ) . replace ( oo0O0o , '1' ) . replace ( ooO0O , '2' ) . replace ( oo0o , '3' ) . replace ( IiI1iIIiIi1Ii , '4' ) . replace ( O0oOoOOO000 , '5' ) . replace ( I1IIo0o0OoOO00Oo , '6' ) ;
 OoOoo = ( i1I1II11I1 ) . replace ( iIiIi , '7' ) . replace ( I1Iii11II , '8' ) . replace ( ii11III1 , '9' ) . replace ( OOOoO0oo0oo0o , '0' ) . replace ( i1i1 , ':' ) . replace ( IiiIi , '%' ) ;
 url = ( OoOoo ) . replace ( Ii11I , '-' ) . replace ( OO0OOo00Oo , '_' ) ;
 i1iIiiiiii1II ( name , url , 222 , iconimage ) ;
 if 97 - 97: I11i1ii1 * I1ii11iIi11i / I11i . IIiIiII11i / O0OOOoOoo0 / O0OOOoOoo0
 if 25 - 25: O0OOOoOoo0
def OO0OO0 ( ) :
 iIIII = i11i1iiiII ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for oO0o0 , i11111I1I , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , oO0o0 , 1007 , i11111I1I )
def OoOO0 ( url ) :
 if 80 - 80: iiiiiiii1 % o000O0o
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , i11111I1I , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , i11111I1I )
  if 95 - 95: I1ii11iIi11i / I1111IIi + I1ii11iIi11i
def O0ooooOO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O0oO0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O0oO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0oO0 )
 if 54 - 54: iiiiiiii1 - iiiiiiii1 * o0o00Oo0O / ii1ii11IIIiiI + oOo0O0Ooo - iiiiiiii1
 if 58 - 58: ii * ooOoO0O00 * OOooOOo
def IIiIiiii1I1 ( url ) :
 iIIII = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  if '-dir-' in I1111i :
   IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , o00O0O )
  else :
   IiiIiI1Ii1i ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , o00O0O )
   if 99 - 99: I1ii11iIi11i
def OO0o0 ( url ) :
 iIIII = i11i1iiiII ( url )
 Oo000ooo0 = ( 'http://afewbitsmore.com/' )
 i1IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '[To Parent Directory]' in I1111i :
   I1111i = 'HOME'
   pass
  elif 'HOME' in I1111i :
   pass
  elif '.m3u' in I1111i :
   IiiIiI1Ii1i ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , Oo000ooo0 + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in I1111i :
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , Oo000ooo0 + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in I1111i :
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , Oo000ooo0 + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , Oo000ooo0 + url , 1012 , III1iII1I1ii + 'music.png' )
def I1i1 ( url ) :
 oO0OOoo0OO = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'music.png' )
  if 69 - 69: I11i
def o00ooOOo0ooO0 ( url ) :
 iIIII = i11i1iiiII ( url )
 Oo000ooo0 = url
 i1IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '.mp3' in I1111i :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/' , '' ) , Oo000ooo0 + url , 1011 , III1iII1I1ii + 'music.png' )
def I11i1I1 ( ) :
 iIIII = i11i1iiiII ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , ( 'http://www.cyn.net/music/' + oO0o0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + o00O0O ) . replace ( ' ' , '%20' ) )
def iiI1iI111 ( url , img ) :
 iIIII = i11i1iiiII ( url )
 oOOo0oo0O = url
 img = img
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( oOOo0oo0O + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 23 - 23: Ii1I + oOo0O0Ooo + ii
def IIIiI1iI1 ( url ) :
 iIIII = i11i1iiiII ( url )
 oOOo0oo0O = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for type , url , I1111i in i1IIIII11I1IiI :
  if '[VID]' in type :
   i1iIiiiiii1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , oOOo0oo0O + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   IIIiI1iI1 ( oOOo0oo0O + url )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: iiiiiiii1
 if 65 - 65: ii1ii11IIIiiI
def oO0O0 ( ) :
 Ii11 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 o00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iIIi = o00O . lower ( )
 oO0o0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 iIiII = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 oOOo0oo0O = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 71 - 71: iiiiiiii1 % iiiiiiii1 . o000O0o + Ii - Ii
 oO0OOoo0OO = O0o0O00Oo0o0 ( oO0o0 )
 iiii111IiIIi1 = O0o0O00Oo0o0 ( iIiII )
 O0 = O0o0O00Oo0o0 ( oOOo0oo0O )
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / iiiiiiii1 - Ii . I11i1ii1 / Ii1IIIi1
 if oO0OOoo0OO != 'Failed' :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oO0o0 , OOoOooOoOOOoo , ii1Oo0000oOo , oOo00 , I1111i in i1IIIII11I1IiI :
   if o00O in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oO0o0 , 1016 , OOoOooOoOOOoo , o0ooooO0o0O , ii1Oo0000oOo )
    if 13 - 13: I11i % o0o00Oo0O - iiiiiiii1 * ii / I1ii11iIi11i - ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iiii111IiIIi1 != 'Failed' :
  OoOOo0O00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iiii111IiIIi1 )
  for oO0o0 , I1111i in OoOOo0O00 :
   if o00O in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oO0o0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 78 - 78: o000O0o % ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( O0 )
  for oO0o0 , I1111i in i1I :
   if o00O in I1111i . lower ( ) :
    IiiIiI1Ii1i ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oO0o0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 73 - 73: oOo0O0Ooo % I11i1ii1 % I1111IIi + ooOoO0O00 - ii / o000O0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 78 - 78: ii % o000O0o - Ii
    if 37 - 37: I1111IIi % ii1ii11IIIiiI % ooOoO0O00
    if 23 - 23: I11i1ii1 - o0o00Oo0O + Ii
    if 98 - 98: ii
    if 61 - 61: I11i . I1111IIi . o0o00Oo0O + ii + o0o00Oo0O
    if 65 - 65: ooOoO0O00 * Ii1IIIi1 * ii - I1111IIi . O0OOOoOoo0 - oO0o
IiIIiIi1 = '{SF},' ; ooOoo0OoO0 = '{IF},' ; oO0OO00o = '{PW},' ; oo0o = '{AM},' ; oooooOOOO0oOo = '{GF},' ; iiii1Ii = '{DD},' ; IIiiiI = '{UO},' ; iiII1i1II1iIi = '{LE},' ; iII = '{ZY},' ; OOOO0o0Oo0 = '{UE},' ; I1iIiI1iiI = '{PE},' ; oO000O00 = '{JE},' ; OoOooooo0oo = '{TH},' ; ii1II1 = '{LK},'
if 71 - 71: ii1ii11IIIiiI * OOooOOo
if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % iiiiiiii1 * I11i
def Ii1i1iI ( ) :
 iIIII = OoOooO ( 'http://www.iwatchseries.me/tv-list/' )
 i1IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , oO0o0 , 8021 , III1iII1I1ii + 'iwatch.png' )
  I1I11i ( 'movies' , 'MAIN' )
def O0O00 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIIII )
 for url , I1111i , II1 in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i + II1 , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def O00o0OO0O ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  o0o00O0oO ( url )
def o0o00O0oO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iIIII )
 Iii1I1111ii = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( 'VidSpot - ' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in i1I :
  i1iIiiiiii1II ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url , I1111i in Iii1I1111ii :
  i1iIiiiiii1II ( 'VidUp' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for I1111i , url in ooOoO00 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   i1iIiiiiii1II ( 'TheVideo - ' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 54 - 54: OOooOOo % iI11I1II1I1I
def i111I ( ) :
 iIIII = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 i1IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , oO0o0 , 1021 , III1iII1I1ii + 'anime.png' )
  if 33 - 33: Ii1IIIi1
  if 22 - 22: o0o00Oo0O + Ii1IIIi1 % ooOoO0O00
def oo00oo ( ) :
 iIIII = OoOooO ( 'http://www.animetoon.org/cartoon' )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , oO0o0 , 1002 , III1iII1I1ii + 'anime.png' )
  if 57 - 57: Ii1IIIi1 * oO0o + o0o00Oo0O % iiiiiiii1 - oOo0O0Ooo
  if 43 - 43: iiiiiiii1
  if 10 - 10: ooOoO0O00 - I11i / ii + Ii + iI11I1II1I1I
def iiIooo0O0O0OO ( url ) :
 iIIII = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  o000o0o00Oo = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  IiiIiI1Ii1i ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  IiiIiI1Ii1i ( I1111i , url , 1003 , o000o0o00Oo )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOooOOoO ( url , IMAGE ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   o0o000OOO ( url )
  elif 'playpanda' in url :
   o0o000OOO ( url )
   if 36 - 36: iiiiiiii1 * iiiiiiii1 % oOo0O0Ooo % o0o00Oo0O . oOo0O0Ooo % ii
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o000OOO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1iIiiiiii1II ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 96 - 96: o000O0o % iI11I1II1I1I / iI11I1II1I1I . O0OOOoOoo0 . ii1ii11IIIiiI
  if 49 - 49: Ii1I * iiiiiiii1 + OOooOOo
def oOOoOOO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 . add_header ( 'referer' , url )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 58 - 58: I1111IIi * O0OOOoOoo0 . oOo0O0Ooo + Ii1IIIi1
def i11i1iiiII ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 4 - 4: oO0o . Ii1IIIi1 + Ii + I11i1ii1 % o000O0o - I11i1ii1
def iIi1ii1I1iiI ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 O0iI1I1ii11IIi1 = ( '%s%s' % ( OOo , url ) )
 i1i = i11i1iiiII ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , i11111I1I , I1111i in i1IIIII11I1IiI :
  i1iIiiiiii1II ( '%s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , i11111I1I )
  if 21 - 21: I1111IIi * o000O0o
def OOOO0OOo ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  i11iii1II1I1 ( url , I1111i )
 else :
  IiIi11iI1IIi ( url )
def IiIi11iI1IIi ( url ) :
 import urlresolver
 try :
  iII111I = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( iII111I , xbmcgui . ListItem ( I1111i ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( I1111i ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def iIiIIiii1II ( url ) :
 if 78 - 78: IIiIiII11i * iI11I1II1I1I / I1111IIi . Ii1I
 iiIii1IIi = open ( o00OO00OoO , "a" )
 iiIii1IIi . write ( 'url="' + url + '"\n' )
 iiIii1IIi . close
 if 13 - 13: OOooOOo . oOo0O0Ooo . I11i * o000O0o / ii1ii11IIIiiI
 OooOOO0O00 = xbmc . Player ( IIii1i1iii1 ( ) )
 import urlresolver
 try : OooOOO0O00 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( I1111i ) )
 OooOOO0O00 = xbmc . Player ( IIii1i1iii1 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  OOooO0OOoo = xbmcgui . Dialog ( )
  if OOooO0OOoo . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   OOooO0OOoo . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : OooOOO0O00 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def i11iii1II1I1 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  OO0IIi1II11 = '.mp4'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   IiIi11iI1IIi ( url )
  if i11I1II1I11i == 1 :
   i1iiiiIi1 ( url , name , OO0IIi1II11 )
 elif '.mkv' in url :
  OO0IIi1II11 = '.mkv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   IiIi11iI1IIi ( url )
  if i11I1II1I11i == 1 :
   i1iiiiIi1 ( url , name , OO0IIi1II11 )
 elif '.mp3' in url :
  OO0IIi1II11 = '.mp3'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   IiIi11iI1IIi ( url )
  if i11I1II1I11i == 1 :
   i1iiiiIi1 ( url , name , OO0IIi1II11 )
 elif '.avi' in url :
  OO0IIi1II11 = '.avi'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   IiIi11iI1IIi ( url )
  if i11I1II1I11i == 1 :
   i1iiiiIi1 ( url , name , OO0IIi1II11 )
 elif '.mov' in url :
  OO0IIi1II11 = '.mov'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   IiIi11iI1IIi ( url )
  if i11I1II1I11i == 1 :
   i1iiiiIi1 ( url , name , OO0IIi1II11 )
 elif '.mpeg' in url :
  OO0IIi1II11 = '.mpeg'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   IiIi11iI1IIi ( url )
  if i11I1II1I11i == 1 :
   i1iiiiIi1 ( url , name , OO0IIi1II11 )
 elif '.mpg' in url :
  OO0IIi1II11 = '.mpg'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   IiIi11iI1IIi ( url )
  if i11I1II1I11i == 1 :
   i1iiiiIi1 ( url , name , OO0IIi1II11 )
 elif '.flv' in url :
  OO0IIi1II11 = '.flv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   IiIi11iI1IIi ( url )
  if i11I1II1I11i == 1 :
   i1iiiiIi1 ( url , name , OO0IIi1II11 )
 elif '.wmv' in url :
  OO0IIi1II11 = '.wmv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   IiIi11iI1IIi ( url )
  if i11I1II1I11i == 1 :
   i1iiiiIi1 ( url , name , OO0IIi1II11 )
 else :
  IiIi11iI1IIi ( url )
def i1iiiiIi1 ( url , name , cat ) :
 I1i1Iii1 ( )
 o00O0 = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , file )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def I1i1Iii1 ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def IIIiII11II11 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 OooOOO0O00 = xbmc . Player ( IIii1i1iii1 ( ) )
 o0oOoO00o . update ( 100 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 OooOOO0O00 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - I1111IIi
def OOOOo0o00OO0000 ( url ) :
 OooOOO0O00 = xbmc . Player ( IIii1i1iii1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : OooOOO0O00 . play ( url ) . strip ( )
 except : pass
 if 30 - 30: ii % Ii1IIIi1
def IIiI ( url ) :
 OooOOO0O00 = xbmc . Player ( IIii1i1iii1 ( ) )
 import urlresolver
 oOOO = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 OooOOO0O00 . play ( oOOO )
 xbmc . sleep ( 1 )
 OooOOO0O00 . play ( url )
 if 70 - 70: O0OOOoOoo0 + Ii % I11i1ii1 % ooOOOoO - I1111IIi
 if 57 - 57: I11i1ii1 % ii
def IIii1i1iii1 ( ) :
 try :
  oO0oo0o0o = getSet ( "core-player" )
  if ( oO0oo0o0o == 'DVDPLAYER' ) : I1i1IiIi1111 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oO0oo0o0o == 'MPLAYER' ) : I1i1IiIi1111 = xbmc . PLAYER_CORE_MPLAYER
  elif ( oO0oo0o0o == 'PAPLAYER' ) : I1i1IiIi1111 = xbmc . PLAYER_CORE_PAPLAYER
  else : I1i1IiIi1111 = xbmc . PLAYER_CORE_AUTO
 except : I1i1IiIi1111 = xbmc . PLAYER_CORE_AUTO
 return I1i1IiIi1111
 return True
 if 20 - 20: I11i1ii1
def IiiIiI1Ii1i ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I11I = True
 iIIII1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIII1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  o00oO0 = [ ]
  o00oO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o00oO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o00oO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iIIII1i . addContextMenuItems ( o00oO0 )
 I11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO , listitem = iIIII1i , isFolder = True )
 return I11I
 if 63 - 63: iI11I1II1I1I . oO0o
def II11IiI1 ( name , url , mode , iconimage , fanart , description ) :
 if 100 - 100: ooOoO0O00 * ooOoO0O00
 oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I11I = True
 iIIII1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIII1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIII1i . setProperty ( "Fanart_Image" , fanart )
 I11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO , listitem = iIIII1i , isFolder = True )
 return I11I
 if 26 - 26: Ii1IIIi1 . oO0o % OOooOOo
def i1iIiiiiii1II ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I11I = True
 iIIII1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIII1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  o00oO0 = [ ]
  o00oO0 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o00oO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o00oO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iIIII1i . addContextMenuItems ( o00oO0 )
 I11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO , listitem = iIIII1i , isFolder = False )
 return I11I
 if 94 - 94: I1111IIi
 if 15 - 15: ii1ii11IIIiiI - I1111IIi / o0o00Oo0O
 if 28 - 28: iiiiiiii1 . ooOoO0O00 / Ii1I
 if 77 - 77: Ii / iiiiiiii1 / Ii % OOooOOo - iiiiiiii1
 if 80 - 80: iiiiiiii1 % OOooOOo . ii . IIiIiII11i % I1111IIi
 if 6 - 6: iiiiiiii1 % I1111IIi / ii1ii11IIIiiI + iiiiiiii1 . o000O0o
def OO0O000 ( heading , announce ) :
 class oo0O0oOO0o0 ( ) :
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
   try : oooOo0OOOoo0 = open ( announce ) ; Oo0O0O = oooOo0OOOoo0 . read ( )
   except : Oo0O0O = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Oo0O0O ) )
   return
 oo0O0oOO0o0 ( )
 oo0O0oOO0o0 ( )
 if 63 - 63: o0o00Oo0O * Ii1I . O0OOOoOoo0
def iI1Ii11iIiI1 ( ) :
 OO0O000 ( 'GenieTv Recomended Sources' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Reaper[/COLOR] [CR]  [COLORred]http://roguemedia.info/cerberus/repo/[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 59 - 59: ii1ii11IIIiiI + IIiIiII11i / ooOOOoO - OOooOOo * o000O0o
 if 46 - 46: ii . o0o00Oo0O . I11i . Ii * Ii1IIIi1
 if 99 - 99: ooOOOoO % iiiiiiii1 . o0o00Oo0O * I1111IIi
 if 87 - 87: ii1ii11IIIiiI % Ii1I * I1ii11iIi11i
 if 59 - 59: I1ii11iIi11i / ooOOOoO - iI11I1II1I1I * iI11I1II1I1I
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 18 - 18: ooOOOoO * Ii1I / Ii / iI11I1II1I1I * ii . Ii1IIIi1
 if 69 - 69: I1ii11iIi11i * I11i1ii1
 if 91 - 91: I11i . I11i1ii1 / oO0o / Ii * I11i
 if 52 - 52: oOo0O0Ooo - Ii / I1111IIi . o000O0o
 if 38 - 38: o000O0o + ii * OOooOOo % o000O0o
 if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
 if 24 - 24: OOooOOo * ii1ii11IIIiiI
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
 if 81 - 81: Ii1IIIi1
 if 58 - 58: IIiIiII11i . iiiiiiii1 . ii1ii11IIIiiI * ii / ii1ii11IIIiiI / ooOOOoO
 if 41 - 41: ooOOOoO + oO0o . O0OOOoOoo0
 if 73 - 73: Ii * oOo0O0Ooo + I11i / o000O0o
 if 56 - 56: ooOoO0O00
 if 11 - 11: Ii % I11i / ooOOOoO * ii
 if 82 - 82: I1111IIi
 if 10 - 10: I1ii11iIi11i % Ii1IIIi1 / ooOOOoO * I1111IIi - I11i
 if 54 - 54: Ii / iI11I1II1I1I % Ii1I / oOo0O0Ooo . iI11I1II1I1I / O0OOOoOoo0
 if 1 - 1: iiiiiiii1 / OOooOOo * OOooOOo - I11i % ii1ii11IIIiiI
 if 96 - 96: I1111IIi / ii1ii11IIIiiI % oO0o . iI11I1II1I1I
 if 30 - 30: ooOOOoO - oO0o
 if 15 - 15: ii
 if 31 - 31: IIiIiII11i
 if 62 - 62: iI11I1II1I1I % iiiiiiii1 % Ii1I * I1111IIi
 if 87 - 87: I1111IIi
def II1i1i ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + IIio0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 17 - 17: Ii
def OoO0oOoo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + I11Iii11iIII111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 86 - 86: I1111IIi - I1111IIi
def O0o0O0OO00 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + OoOoO0o0oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 21 - 21: o0o00Oo0O - I11i
def Oo00oO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + Oo0OOOOOOOo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 11 - 11: ii1ii11IIIiiI / OOooOOo - oO0o + OOooOOo
def oO0OOoOo000oO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + IIi1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 33 - 33: Ii1I - I1111IIi
def i1IiIii1i ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iII1iIIIIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 31 - 31: I1ii11iIi11i / Ii1I - o0o00Oo0O + O0OOOoOoo0 - O0OOOoOoo0
def ooO0OOO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o0Ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 17 - 17: I1111IIi % ii / I11i1ii1 * ii
def iiIi1io0o0OoOo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + IiII11iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 99 - 99: I11i1ii1 . ii1ii11IIIiiI
def o000IIIi1IiI1iII ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + OOOO0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 48 - 48: Ii - ii1ii11IIIiiI . oO0o
def OOOoo0OO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o0o0II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , o000 )
 I1I11i ( 'movies' , 'MAIN' )
 if 67 - 67: iiiiiiii1 - I1ii11iIi11i % Ii / ii1ii11IIIiiI . iiiiiiii1 . o000O0o
 if 44 - 44: oO0o / iiiiiiii1 / ii
 if 61 - 61: o000O0o / Ii1IIIi1
 if 44 - 44: OOooOOo
 if 49 - 49: Ii1IIIi1 - Ii1I / o000O0o
 if 33 - 33: O0OOOoOoo0
 if 24 - 24: O0OOOoOoo0 . I11i1ii1
 if 29 - 29: ii / I1111IIi % ooOOOoO . Ii1IIIi1 + iiiiiiii1
 if 94 - 94: ooOOOoO
def o0IIi1 ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for oo0OooO , oOOoOOO0oOoo , o0O0ooooooo00 in os . walk ( iIi1ii1I1 ) :
     IIIi1IIiI = 0
     IIIi1IIiI += len ( o0O0ooooooo00 )
     if IIIi1IIiI > 0 :
      for oooOo0OOOoo0 in o0O0ooooooo00 :
       os . unlink ( os . path . join ( oo0OooO , oooOo0OOOoo0 ) )
  IiIi1I1i = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( IiIi1I1i )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 41 - 41: I1ii11iIi11i / o0o00Oo0O . o0o00Oo0O + Ii * o0o00Oo0O / oO0o
 if 31 - 31: o000O0o % iI11I1II1I1I + oO0o
 if 53 - 53: iI11I1II1I1I % OOooOOo % oOo0O0Ooo + Ii1I % ii
 if 29 - 29: oOo0O0Ooo / I11i + iI11I1II1I1I / o0o00Oo0O / Ii1IIIi1 % ooOoO0O00
 if 65 - 65: oO0o * OOooOOo . ii - o0o00Oo0O * OOooOOo % OOooOOo
 if 1 - 1: oOo0O0Ooo + ii . oOo0O0Ooo + Ii1IIIi1 / iiiiiiii1
 if 73 - 73: I11i % Ii1I . iI11I1II1I1I
 if 43 - 43: I1111IIi / ooOOOoO + oO0o
def Iii1Iiii ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 38 - 38: O0OOOoOoo0
def i1111iI1 ( url ) :
 ooOOO = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 O0OOO00 = [
 ( ooOOO ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( ooOOO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( ooOOO , 'plugin.video.itv' , 'Images' ) ) ]
 if 12 - 12: OOooOOo - I11i - iiiiiiii1 / ooOOOoO
 III1iii1 = 0
 if 78 - 78: iiiiiiii1 % Ii1IIIi1
 for i11I in O0OOO00 :
  if os . path . exists ( i11I ) and not i11I in [ oO0o0o0ooO0oO , ooOOO ] :
   for oo0OooO , oOOoOOO0oOoo , o0O0ooooooo00 in os . walk ( i11I ) :
    IIIi1IIiI = 0
    IIIi1IIiI += len ( o0O0ooooooo00 )
    if IIIi1IIiI > 0 :
     for oooOo0OOOoo0 in o0O0ooooooo00 :
      if not oooOo0OOOoo0 in oooOOOOO :
       try :
        os . unlink ( os . path . join ( oo0OooO , oooOo0OOOoo0 ) )
       except :
        pass
      else : iIiIi11 ( 'Ignore Log File: %s' % oooOo0OOOoo0 )
     for IiIi1II111I in oOOoOOO0oOoo :
      try :
       shutil . rmtree ( os . path . join ( oo0OooO , IiIi1II111I ) )
       III1iii1 += 1
       iIiIi11 ( "[Success] cleared %s files from %s" % ( str ( IIIi1IIiI ) , os . path . join ( i11I , IiIi1II111I ) ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , IiIi1II111I ) )
  else :
   for oo0OooO , oOOoOOO0oOoo , o0O0ooooooo00 in os . walk ( i11I ) :
    for IiIi1II111I in oOOoOOO0oOoo :
     if 'cache' in IiIi1II111I . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( oo0OooO , IiIi1II111I ) )
       III1iii1 += 1
       iIiIi11 ( "[Success] wiped %s " % os . path . join ( i11I , IiIi1II111I ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , IiIi1II111I ) )
       if 73 - 73: Ii1I + O0OOOoOoo0 * oOo0O0Ooo * ooOOOoO
 Iii1Iiii ( oO , 'Clear Cache: Removed %s Files' % III1iii1 )
 if 35 - 35: ooOOOoO * o0o00Oo0O * oO0o . Ii1I
 if 74 - 74: O0OOOoOoo0 * O0OOOoOoo0 * I11i / o000O0o
 if 91 - 91: Ii . Ii1I / IIiIiII11i
 if 97 - 97: ii1ii11IIIiiI % ooOoO0O00 % I1111IIi + I1ii11iIi11i - o0o00Oo0O - ooOOOoO
 if 64 - 64: ii1ii11IIIiiI - O0OOOoOoo0
 if 12 - 12: ooOoO0O00
 if 99 - 99: IIiIiII11i - Ii1I * I1111IIi
def Oo0oOOOOo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 I11I11III = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oo0OooO , oOOoOOO0oOoo , o0O0ooooooo00 in os . walk ( I11I11III ) :
   IIIi1IIiI = 0
   IIIi1IIiI += len ( o0O0ooooooo00 )
   if 15 - 15: Ii1I * ii1ii11IIIiiI / O0OOOoOoo0 . I11i / ii1ii11IIIiiI % OOooOOo
   if 75 - 75: ii % Ii % iI11I1II1I1I % Ii1I / Ii
   if IIIi1IIiI > 0 :
    if 96 - 96: I11i1ii1 * o000O0o / iI11I1II1I1I / ooOOOoO
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( IIIi1IIiI ) + " files found" , "Do you want to delete them?" ) :
     if 5 - 5: I11i
     for oooOo0OOOoo0 in o0O0ooooooo00 :
      os . unlink ( os . path . join ( oo0OooO , oooOo0OOOoo0 ) )
     for IiIi1II111I in oOOoOOO0oOoo :
      shutil . rmtree ( os . path . join ( oo0OooO , IiIi1II111I ) )
     OOooO0OOoo = xbmcgui . Dialog ( )
     OOooO0OOoo . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    OOooO0OOoo = xbmcgui . Dialog ( )
    OOooO0OOoo . ok ( i1 , "       No Packages to DELETE" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 return
 if 83 - 83: ooOOOoO * oOo0O0Ooo . IIiIiII11i * ooOoO0O00 % o0o00Oo0O
 if 35 - 35: OOooOOo % oO0o + o0o00Oo0O * I11i % Ii1I
 if 57 - 57: o000O0o / ooOOOoO
 if 63 - 63: I11i1ii1 * oO0o * I11i1ii1 + OOooOOo
 if 25 - 25: O0OOOoOoo0 * OOooOOo / oOo0O0Ooo / I1111IIi
 if 11 - 11: Ii1IIIi1 + Ii
 if 14 - 14: OOooOOo / I1111IIi + oO0o - ii1ii11IIIiiI
 if 38 - 38: iiiiiiii1
 if 30 - 30: IIiIiII11i + ooOOOoO . Ii + iI11I1II1I1I
def I1iIIiiIIi1i ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 I11I11III = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for oo0OooO , oOOoOOO0oOoo , o0O0ooooooo00 in os . walk ( I11I11III ) :
   IIIi1IIiI = 0
   IIIi1IIiI += len ( o0O0ooooooo00 )
   if 100 - 100: o000O0o * I11i / O0OOOoOoo0
   if 92 - 92: I11i1ii1 / Ii * Ii1IIIi1
   if IIIi1IIiI > 0 :
    if 55 - 55: I11i1ii1
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( IIIi1IIiI ) + " files found" , "Do you want to delete them?" ) :
     if 1 - 1: oO0o
     for oooOo0OOOoo0 in o0O0ooooooo00 :
      os . unlink ( os . path . join ( oo0OooO , oooOo0OOOoo0 ) )
     for IiIi1II111I in oOOoOOO0oOoo :
      shutil . rmtree ( os . path . join ( oo0OooO , IiIi1II111I ) )
     OOooO0OOoo = xbmcgui . Dialog ( )
     OOooO0OOoo . ok ( i1 , "       Deleting Packages all done" )
    else :
     pass
   else :
    OOooO0OOoo = xbmcgui . Dialog ( )
    OOooO0OOoo . ok ( i1 , "       No Packages to DELETE" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Packages please visit The Support Group, GenieTv on facebook" )
 i1111iI1 ( url )
 return
 if 43 - 43: iI11I1II1I1I - Ii1IIIi1 - I11i + Ii1I - iiiiiiii1 % Ii1I
 if 58 - 58: OOooOOo
 if 27 - 27: I1111IIi * Ii1IIIi1 - ii . ii1ii11IIIiiI - IIiIiII11i
 if 62 - 62: oOo0O0Ooo / iI11I1II1I1I * ooOOOoO
 if 84 - 84: I1111IIi - OOooOOo . I1111IIi + I11i1ii1 . O0OOOoOoo0
 if 96 - 96: ii1ii11IIIiiI % O0OOOoOoo0 * ii1ii11IIIiiI % oOo0O0Ooo . I11i / I11i
 if 7 - 7: oO0o - I11i1ii1 % ooOoO0O00
 if 24 - 24: oO0o % o0o00Oo0O % ooOOOoO
 if 61 - 61: I11i1ii1 . O0OOOoOoo0 / I11i1ii1 * ii
 if 13 - 13: IIiIiII11i
def iIi11OOo0oo ( url , name ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoO00OoOOo = os . path . join ( o00O0 , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 oOOO0O000Oo = os . path . join ( o00O0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( oOOO0O000Oo ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OoOoO00OoOOo = os . path . join ( o00O0 , 'advancedsettings.xml' )
   try :
    os . remove ( OoOoO00OoOOo )
    print '=== GenieTv - REMOVING    ' + str ( OoOoO00OoOOo ) + '    ==='
   except :
    pass
   i1i = iI111I11I1I1 . http_GET ( url ) . content
   oooOoO = open ( OoOoO00OoOOo , "w" )
   oooOoO . write ( i1i )
   oooOoO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OoOoO00OoOOo ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OoOoO00OoOOo = os . path . join ( o00O0 , 'advancedsettings.xml' )
  try :
   os . remove ( OoOoO00OoOOo )
   print '=== GenieTv - REMOVING    ' + str ( OoOoO00OoOOo ) + '    ==='
  except :
   pass
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  oooOoO = open ( OoOoO00OoOOo , "w" )
  oooOoO . write ( i1i )
  oooOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoO00OoOOo ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 18 - 18: OOooOOo
def ii1Ii ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoO00OoOOo = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  oooOoO = open ( OoOoO00OoOOo ) . read ( )
  if 'zero' in oooOoO :
   name = '0CACHE'
  elif 'tuxen' in oooOoO :
   name = 'TUXENS'
  elif 'muckys' in oooOoO :
   name = 'MUCKYS'
  elif 'p2p1' in oooOoO :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oooOoO :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oooOoO :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 42 - 42: O0OOOoOoo0
def iI1iIi ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoO00OoOOo = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  os . remove ( OoOoO00OoOOo )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OoOoO00OoOOo ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 40 - 40: iiiiiiii1 / Ii . ii1ii11IIIiiI - I1111IIi / oO0o
 if 14 - 14: I11i1ii1 / Ii - o000O0o + Ii
 if 10 - 10: ii1ii11IIIiiI + I11i1ii1
 if 3 - 3: o0o00Oo0O - Ii % OOooOOo
 if 17 - 17: I11i
 if 39 - 39: I11i
 if 89 - 89: ii + O0OOOoOoo0 . iiiiiiii1 / ii1ii11IIIiiI
 if 75 - 75: iI11I1II1I1I * O0OOOoOoo0 / OOooOOo * IIiIiII11i . ooOoO0O00
 if 6 - 6: ii1ii11IIIiiI % ii1ii11IIIiiI / ii * o000O0o . oOo0O0Ooo . ooOoO0O00
 if 59 - 59: ooOOOoO . ooOOOoO * oOo0O0Ooo - ii1ii11IIIiiI % OOooOOo
def iiiO000OOO ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 i1IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for IiIIIiI11i1 , IIIiiiIi1I1 , II1iIIII , I1iI11IiIi1II in i1IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % IiIIIiI11i1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % II1iIIII , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I1iI11IiIi1II )
  inc = inc + 1
  if 98 - 98: Ii . O0OOOoOoo0 / oO0o . oO0o . ii1ii11IIIiiI % iiiiiiii1
  if 77 - 77: o000O0o / iI11I1II1I1I % oOo0O0Ooo / I11i / IIiIiII11i - iiiiiiii1
  if 4 - 4: ooOoO0O00
  if 97 - 97: ii / Ii % o0o00Oo0O
  if 17 - 17: iiiiiiii1 + Ii . Ii * ooOoO0O00 / o0o00Oo0O
  if 2 - 2: IIiIiII11i / oO0o % iI11I1II1I1I / Ii
  if 52 - 52: I11i1ii1 % iI11I1II1I1I . Ii % I11i1ii1
  if 86 - 86: o000O0o % iI11I1II1I1I % OOooOOo
  if 94 - 94: I11i - ooOOOoO % o000O0o % I11i + ooOOOoO
def I11IIiii111I1 ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoOoO00OoOOo = os . path . join ( o00O0 , 'addons2.ini' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  oooOoO = open ( OoOoO00OoOOo , "w" )
  oooOoO . write ( i1i )
  oooOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoO00OoOOo ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 25 - 25: o0o00Oo0O
def OooOOoO00o0 ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoOoO00OoOOo = os . path . join ( o00O0 , 'settings.xml' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  oooOoO = open ( OoOoO00OoOOo , "w" )
  oooOoO . write ( i1i )
  oooOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoO00OoOOo ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 19 - 19: Ii * I1ii11iIi11i
 if 33 - 33: Ii + oOo0O0Ooo
def OO00Oii ( ) :
 try :
  O0OoO0OOO00 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( O0OoO0OOO00 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    III = os . path . join ( O0OoO0OOO00 , "source.db" )
    os . unlink ( III )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 8 - 8: iI11I1II1I1I / ooOoO0O00
 if 92 - 92: oOo0O0Ooo / ooOoO0O00 * Ii * IIiIiII11i
 if 16 - 16: ii1ii11IIIiiI
 if 96 - 96: I11i / iiiiiiii1 % ii1ii11IIIiiI - I11i1ii1
 if 35 - 35: Ii1IIIi1
def OoOooO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 90 - 90: Ii
 if 47 - 47: oO0o . Ii
 if 9 - 9: OOooOOo - ooOOOoO . ii % I11i1ii1
 if 13 - 13: oO0o * iI11I1II1I1I + IIiIiII11i - I1ii11iIi11i - OOooOOo
 if 43 - 43: O0OOOoOoo0 / iiiiiiii1 * oOo0O0Ooo % I11i1ii1 % oOo0O0Ooo
 if 18 - 18: oO0o
 if 99 - 99: O0OOOoOoo0 / o000O0o . Ii / ooOOOoO + ooOoO0O00 - ooOOOoO
def i11i1ii1I ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iIIIi11iI1I1I11II = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iIIIi11iI1I1I11II :
  oo0 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; oo0 = xbmc . translatePath ( oo0 ) ;
  O00O0oO = os . path . join ( oo0 , ".." , ".." ) ; O00O0oO = os . path . abspath ( O00O0oO ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + O00O0oO ) ; IIIIi1iII = False
  try :
   for oo0OooO , oOOoOOO0oOoo , o0O0ooooooo00 in os . walk ( O00O0oO , topdown = True ) :
    oOOoOOO0oOoo [ : ] = [ IiIi1II111I for IiIi1II111I in oOOoOOO0oOoo if IiIi1II111I not in o0oO0 ]
    for I1111i in o0O0ooooooo00 :
     try : os . remove ( os . path . join ( oo0OooO , I1111i ) )
     except :
      if I1111i not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IIIIi1iII = True
      plugintools . log ( "Error removing " + oo0OooO + " " + I1111i )
    for I1111i in oOOoOOO0oOoo :
     try : os . rmdir ( os . path . join ( oo0OooO , I1111i ) )
     except :
      if I1111i not in [ "Database" , "userdata" ] : IIIIi1iII = True
      plugintools . log ( "Error removing " + oo0OooO + " " + I1111i )
   if not IIIIi1iII : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 I1i1I ( )
 if 49 - 49: ooOoO0O00 . I1111IIi
 if 82 - 82: oO0o / ooOOOoO
 if 38 - 38: iI11I1II1I1I
def Ii1IIIi ( ) :
 Oo00o = [ ]
 oOOOIi11 = sys . argv [ 2 ]
 if len ( oOOOIi11 ) >= 2 :
  o0OO0o0o00o = sys . argv [ 2 ]
  O0Oo0O0O0o0 = o0OO0o0o00o . replace ( '?' , '' )
  if ( o0OO0o0o00o [ len ( o0OO0o0o00o ) - 1 ] == '/' ) :
   o0OO0o0o00o = o0OO0o0o00o [ 0 : len ( o0OO0o0o00o ) - 2 ]
  Oo0o = O0Oo0O0O0o0 . split ( '&' )
  Oo00o = { }
  for Ii111Ii11 in range ( len ( Oo0o ) ) :
   oo0oOo0Oo0O = { }
   oo0oOo0Oo0O = Oo0o [ Ii111Ii11 ] . split ( '=' )
   if ( len ( oo0oOo0Oo0O ) ) == 2 :
    Oo00o [ oo0oOo0Oo0O [ 0 ] ] = oo0oOo0Oo0O [ 1 ]
    if 11 - 11: I1ii11iIi11i * ooOoO0O00 * Ii1IIIi1 . oO0o . O0OOOoOoo0
 return Oo00o
 if 63 - 63: o0o00Oo0O . iiiiiiii1 / iiiiiiii1 / iI11I1II1I1I + Ii1IIIi1 . ooOOOoO
oO0oOO000 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
iIioOo = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OoOoO0O0oOo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
iiI1i1I = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oooOoO00OooO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
OooO00O0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
IIio0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iiI1i111I1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
I11Iii11iIII111 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
OoOoO0o0oO0 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
Oo0OOOOOOOo0O = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
IIi1Ii = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iII1iIIIIII = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o0Ooo0 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
IiII11iI = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OOOO0oo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
O0OOoo0o = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iiIi11i1I1 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
Ii1ooOO0OOO00o = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
O0O0O0o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OOO000OOo0o0O = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
O0oII1IIiiI1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
o0o0II = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OOo = base64 . decodestring ( 'Q1VOVA==' )
def iiOOooooO0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I11I = True
 iIIII1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIII1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIII1i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o00oO0 = [ ]
  if showcontext == 'fav' :
   o00oO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o00oO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iIIII1i . addContextMenuItems ( o00oO0 )
 I11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO , listitem = iIIII1i , isFolder = True )
 return I11I
 if 72 - 72: I1111IIi + Ii - Ii1IIIi1
def OOiIiIIi1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I11I = True
 iIIII1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIIII1i . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iIIII1i . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o00oO0 = [ ]
  if showcontext == 'fav' :
   o00oO0 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o00oO0 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iIIII1i . addContextMenuItems ( o00oO0 )
 I11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOO , listitem = iIIII1i , isFolder = False )
 return I11I
 if 67 - 67: iI11I1II1I1I % I1111IIi
 if 97 - 97: O0OOOoOoo0
o0OO0o0o00o = Ii1IIIi ( )
oO0o0 = None
I1111i = None
ii1ii111 = None
OOoOooOoOOOoo = None
o0ooooO0o0O = None
o000 = None
iI1I1iIi11II1 = None
II11ii1111Ii = None
if 93 - 93: I11i1ii1 + I11i1ii1
if 65 - 65: ii * ooOOOoO * o000O0o % Ii1I * IIiIiII11i
try :
 II11ii1111Ii = int ( o0OO0o0o00o [ "fav_mode" ] )
except :
 pass
 if 86 - 86: Ii / ooOOOoO * O0OOOoOoo0 - O0OOOoOoo0
try :
 oO0o0 = urllib . unquote_plus ( o0OO0o0o00o [ "url" ] )
except :
 pass
try :
 I1111i = urllib . unquote_plus ( o0OO0o0o00o [ "name" ] )
except :
 pass
try :
 OOoOooOoOOOoo = urllib . unquote_plus ( o0OO0o0o00o [ "iconimage" ] )
except :
 pass
try :
 ii1ii111 = int ( o0OO0o0o00o [ "mode" ] )
except :
 pass
try :
 o0ooooO0o0O = urllib . unquote_plus ( o0OO0o0o00o [ "fanart" ] )
except :
 pass
try :
 o000 = urllib . unquote_plus ( o0OO0o0o00o [ "description" ] )
except :
 pass
 if 32 - 32: I1ii11iIi11i . o0o00Oo0O
 if 48 - 48: Ii1I % IIiIiII11i + ooOOOoO
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( ii1ii111 )
print "URL: " + str ( oO0o0 )
print "Name: " + str ( I1111i )
print "IconImage: " + str ( OOoOooOoOOOoo )
if 25 - 25: I1111IIi * I11i / oOo0O0Ooo . I1111IIi % IIiIiII11i
if 50 - 50: OOooOOo * O0OOOoOoo0
def I1I11i ( content , viewType ) :
 if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / ooOOOoO
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 92 - 92: I11i
if OOoOooOoOOOoo == None : OOoOooOoOOOoo = Oo00OOOOO
if o0ooooO0o0O == None : o0ooooO0o0O = O0o0Oo
if ii1ii111 == None :
 o0o0o0oO0oOO ( )
 if 8 - 8: O0OOOoOoo0 + Ii1I . ii1ii11IIIiiI
elif ii1ii111 == 1 :
 IIII ( oO0o0 )
 if 50 - 50: I1ii11iIi11i
elif ii1ii111 == 44 :
 oOo0 ( oO0o0 )
 if 16 - 16: ii1ii11IIIiiI - OOooOOo % I1ii11iIi11i / ii1ii11IIIiiI . ooOOOoO + I11i1ii1
elif ii1ii111 == 2 :
 IIIi1IiIiii ( )
 if 78 - 78: iI11I1II1I1I + oO0o + Ii
elif ii1ii111 == 3 :
 o0Iiii ( )
 if 21 - 21: I1ii11iIi11i + ii1ii11IIIiiI % I11i1ii1 + OOooOOo % ooOOOoO
elif ii1ii111 == 21 :
 i1i1II ( )
 if 22 - 22: ooOoO0O00 / ii . oO0o
elif ii1ii111 == 4 :
 o00oo ( )
 if 83 - 83: oOo0O0Ooo - ii + Ii1I . ii1ii11IIIiiI / I11i + I11i1ii1
elif ii1ii111 == 5 :
 iII1III ( oO0o0 )
 if 90 - 90: oOo0O0Ooo - Ii
elif ii1ii111 == 6 :
 Oo0oOOOOo ( oO0o0 )
 if 42 - 42: Ii1IIIi1 . I1ii11iIi11i
elif ii1ii111 == 7 :
 iIi11OOo0oo ( oO0o0 , I1111i )
 if 21 - 21: O0OOOoOoo0 . oOo0O0Ooo / ooOOOoO
elif ii1ii111 == 8 :
 ii1Ii ( oO0o0 , I1111i )
 if 97 - 97: iI11I1II1I1I + ooOoO0O00 - I11i
elif ii1ii111 == 9 :
 FIXREPOSADDONS ( oO0o0 )
 if 73 - 73: oO0o - Ii % iiiiiiii1 / I1ii11iIi11i - ii % Ii1IIIi1
elif ii1ii111 == 10 :
 O0O0ooOOO ( )
 if 79 - 79: oOo0O0Ooo / I11i . ii1ii11IIIiiI * Ii1I + ooOOOoO
elif ii1ii111 == 11 :
 iI1iIi ( oO0o0 )
 if 96 - 96: oO0o * IIiIiII11i
elif ii1ii111 == 12 :
 iiiO000OOO ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 1 - 1: oOo0O0Ooo - OOooOOo
elif ii1ii111 == 13 :
 o0IIi1 ( )
 if 74 - 74: OOooOOo * IIiIiII11i + o0o00Oo0O + ooOOOoO
elif ii1ii111 == 14 :
 i1111iI1 ( oO0o0 )
 if 3 - 3: iI11I1II1I1I - ooOoO0O00 / O0OOOoOoo0 + ooOoO0O00 + o0o00Oo0O
elif ii1ii111 == 15 :
 III1ii ( )
 if 18 - 18: iI11I1II1I1I . O0OOOoOoo0 % Ii1IIIi1 % o000O0o + iI11I1II1I1I * ii
elif ii1ii111 == 16 :
 I11IIiii111I1 ( oO0o0 , I1111i )
 if 78 - 78: I1111IIi
elif ii1ii111 == 17 :
 OooOOoO00o0 ( oO0o0 , I1111i )
 if 38 - 38: oO0o * Ii1I
elif ii1ii111 == 18 :
 OO00Oii ( )
 if 4 - 4: oO0o . Ii1I
elif ii1ii111 == 19 :
 OOoOoOo0 ( oO0o0 )
 if 21 - 21: Ii / oO0o / Ii1I * o0o00Oo0O - IIiIiII11i * Ii1IIIi1
elif ii1ii111 == 40 :
 O0O0 ( I1111i , oO0o0 , o000 )
 if 27 - 27: I11i . OOooOOo * ii1ii11IIIiiI * O0OOOoOoo0 * o0o00Oo0O
elif ii1ii111 == 42 :
 o00O00O0Oo0 ( I1111i , oO0o0 , o000 )
 if 93 - 93: I1111IIi % iiiiiiii1 % IIiIiII11i
elif ii1ii111 == 43 :
 oOo0O000oo0 ( oO0o0 )
 if 20 - 20: ii * iiiiiiii1
elif ii1ii111 == 20 :
 I11III11III1 ( oO0o0 )
 if 38 - 38: O0OOOoOoo0 . ii
elif ii1ii111 == 22 :
 II1i1i ( oO0o0 )
 if 28 - 28: iiiiiiii1 * ooOoO0O00 . Ii1I
elif ii1ii111 == 23 :
 OoO0oOoo ( oO0o0 )
 if 75 - 75: o0o00Oo0O / o000O0o * I11i1ii1 - Ii1IIIi1 / ooOoO0O00
elif ii1ii111 == 24 :
 O0o0O0OO00 ( oO0o0 )
 if 61 - 61: ooOOOoO
elif ii1ii111 == 25 :
 Oo00oO ( oO0o0 )
 if 100 - 100: o0o00Oo0O - iI11I1II1I1I * I1ii11iIi11i
elif ii1ii111 == 26 :
 oO0OOoOo000oO ( oO0o0 )
 if 35 - 35: I11i1ii1
elif ii1ii111 == 27 :
 i1IiIii1i ( oO0o0 )
 if 57 - 57: oO0o . I1ii11iIi11i + oOo0O0Ooo
elif ii1ii111 == 28 :
 ooO0OOO ( oO0o0 )
 if 18 - 18: oOo0O0Ooo - Ii1I * ooOOOoO / Ii - I11i % I11i
elif ii1ii111 == 29 :
 iiIi1io0o0OoOo ( oO0o0 )
 if 31 - 31: ooOOOoO
elif ii1ii111 == 30 :
 oOOOO0oo0O0OO ( oO0o0 )
 if 100 - 100: Ii * Ii . iI11I1II1I1I % O0OOOoOoo0 * Ii1I
elif ii1ii111 == 31 :
 o000IIIi1IiI1iII ( oO0o0 )
 if 17 - 17: ii1ii11IIIiiI * I1111IIi * Ii / Ii1I / Ii
elif ii1ii111 == 32 :
 Iii1IIII11I ( )
 if 23 - 23: ii + Ii / I1ii11iIi11i / O0OOOoOoo0 . O0OOOoOoo0 * oOo0O0Ooo
elif ii1ii111 == 33 :
 ooO000OO ( )
 if 98 - 98: I1111IIi
elif ii1ii111 == 35 :
 OO0IIIIIIi111i ( oO0o0 )
 if 23 - 23: ooOOOoO / ooOoO0O00 * oO0o
elif ii1ii111 == 34 :
 i111IIiIiiI1 ( oO0o0 )
 if 51 - 51: Ii1IIIi1 - ii / ii % ii
elif ii1ii111 == 36 :
 iiI11Ii1i ( oO0o0 )
 if 85 - 85: oO0o . I11i . oOo0O0Ooo
elif ii1ii111 == 37 :
 III1 ( oO0o0 )
 if 75 - 75: iI11I1II1I1I - ii1ii11IIIiiI % o0o00Oo0O % I1111IIi
elif ii1ii111 == 38 :
 i1i1I11i1I ( oO0o0 )
 if 6 - 6: I1ii11iIi11i % o000O0o * I11i1ii1 - ooOoO0O00 . OOooOOo
elif ii1ii111 == 41 :
 i11i1ii1I ( o0OO0o0o00o )
 if 20 - 20: I1ii11iIi11i / iiiiiiii1 . I1ii11iIi11i
elif ii1ii111 == 39 :
 OOOoo0OO ( oO0o0 )
 if 60 - 60: Ii1I - oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i . ooOoO0O00 . OOooOOo
elif ii1ii111 == 45 :
 TEXTS ( )
 if 24 - 24: I1111IIi * oOo0O0Ooo / Ii1IIIi1
elif ii1ii111 == 46 :
 iI1Ii11iIiI1 ( )
 if 51 - 51: iI11I1II1I1I / ooOOOoO * oO0o * ii1ii11IIIiiI + Ii1I . ii
elif ii1ii111 == 47 :
 GEVID ( )
 if 75 - 75: I1111IIi / ii / o0o00Oo0O % Ii1IIIi1
elif ii1ii111 == 48 :
 O0oO0o0oOOO0o ( I1111i , oO0o0 , o000 )
 if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
elif ii1ii111 == 49 :
 iI1i111I1Ii ( )
 if 11 - 11: I11i * oO0o
elif ii1ii111 == 22222 :
 iIiIIiii1II ( oO0o0 )
 if 92 - 92: OOooOOo . I1ii11iIi11i * ooOOOoO
elif ii1ii111 == 222 :
 OOOO0OOo ( oO0o0 )
 if 86 - 86: o0o00Oo0O
elif ii1ii111 == 2222222 :
 IiIi11iI1IIi ( oO0o0 )
 if 55 - 55: ii1ii11IIIiiI / iiiiiiii1 / Ii1I % I11i1ii1 % oOo0O0Ooo
elif ii1ii111 == 222222 :
 i11iii1II1I1 ( oO0o0 , I1111i )
 if 55 - 55: o000O0o + ii % ooOoO0O00
elif ii1ii111 == 333 :
 iIi1ii1I1iiI ( oO0o0 )
 if 24 - 24: Ii1I - I1ii11iIi11i
 if 36 - 36: oOo0O0Ooo . Ii1IIIi1 % IIiIiII11i * I1111IIi
elif ii1ii111 == 1020 :
 i111I ( )
 if 34 - 34: ooOOOoO % O0OOOoOoo0 - I11i1ii1 - oOo0O0Ooo
elif ii1ii111 == 1021 :
 ANIMEEP ( )
 if 44 - 44: ii1ii11IIIiiI . I11i . iI11I1II1I1I + ii - oOo0O0Ooo
elif ii1ii111 == 1022 :
 ANIMEPLAY ( oO0o0 )
 if 22 - 22: ooOOOoO * Ii1I . ii / I1ii11iIi11i / ii1ii11IIIiiI
elif ii1ii111 == 1001 :
 oo00oo ( )
 if 54 - 54: iiiiiiii1 % ii1ii11IIIiiI + I11i1ii1
elif ii1ii111 == 1005 :
 OO0OO0 ( )
 if 45 - 45: ii1ii11IIIiiI / o000O0o * iiiiiiii1 . ii1ii11IIIiiI
elif ii1ii111 == 1007 :
 OoOO0 ( oO0o0 )
 if 25 - 25: Ii1I / Ii1I
elif ii1ii111 == 1010 :
 IIiIiiii1I1 ( oO0o0 )
 if 79 - 79: I1ii11iIi11i - oO0o % I1ii11iIi11i . IIiIiII11i
elif ii1ii111 == 1011 :
 o00ooOOo0ooO0 ( oO0o0 )
 if 84 - 84: I11i1ii1 * ii + o0o00Oo0O
elif ii1ii111 == 1012 :
 OO0o0 ( oO0o0 )
 if 84 - 84: ooOoO0O00 . ooOOOoO . ooOoO0O00 . I1ii11iIi11i
elif ii1ii111 == 1030 :
 I11i1I1 ( )
 if 21 - 21: IIiIiII11i . o0o00Oo0O + I1ii11iIi11i - Ii
elif ii1ii111 == 1031 :
 iiI1iI111 ( oO0o0 , OOoOooOoOOOoo )
 if 5 - 5: iI11I1II1I1I * Ii + oO0o + ooOOOoO * o0o00Oo0O % I11i1ii1
elif ii1ii111 == 1032 :
 IIIiI1iI1 ( oO0o0 )
 if 88 - 88: I11i / Ii * Ii1I
elif ii1ii111 == 1006 :
 Parse . ParseURL ( oO0o0 )
 if 23 - 23: o0o00Oo0O / O0OOOoOoo0
elif ii1ii111 == 2030 :
 Parse . addonParseURL ( oO0o0 )
 if 66 - 66: ooOoO0O00 % ii * Ii + o000O0o * o0o00Oo0O / oO0o
elif ii1ii111 == 2031 :
 Parse . apkParseURL ( oO0o0 )
 if 14 - 14: oOo0O0Ooo . I1111IIi
elif ii1ii111 == 2032 :
 Parse . ParseBOSS ( oO0o0 )
 if 29 - 29: ii / I1111IIi + OOooOOo - iiiiiiii1 + I1111IIi . ooOoO0O00
elif ii1ii111 == 1002 :
 iiIooo0O0O0OO ( oO0o0 )
 if 26 - 26: Ii - IIiIiII11i
elif ii1ii111 == 1003 :
 oOooOOoO ( oO0o0 , OOoOooOoOOOoo )
 if 43 - 43: oOo0O0Ooo
elif ii1ii111 == 1004 :
 o0o000OOO ( oO0o0 )
 if 35 - 35: I11i1ii1 + OOooOOo * ii - IIiIiII11i
elif ii1ii111 == 1008 :
 iiiiIiii1I11 ( )
 if 19 - 19: ooOoO0O00 / ii1ii11IIIiiI / OOooOOo . oOo0O0Ooo / ii1ii11IIIiiI % I11i
elif ii1ii111 == 1009 :
 I1i11iiII111I ( oO0o0 )
 if 39 - 39: I11i1ii1 - ii
elif ii1ii111 == 2001 :
 I1i1ii1IiI1i ( )
 if 88 - 88: ooOoO0O00 + iI11I1II1I1I * Ii - ii % I11i
elif ii1ii111 == 2002 :
 I1i1 ( oO0o0 )
 if 74 - 74: I11i1ii1 - Ii
elif ii1ii111 == 1013 :
 iIIiiiI1iI1 ( )
elif ii1ii111 == 10111113 :
 oO0oiIiI ( oO0o0 )
 if 34 - 34: I1111IIi + iiiiiiii1 + I1ii11iIi11i / IIiIiII11i
elif ii1ii111 == 1014 :
 O0ooO ( )
 if 33 - 33: ii1ii11IIIiiI . ooOoO0O00 - IIiIiII11i - oO0o
elif ii1ii111 == 1015 :
 OOo000OOoOO ( oO0o0 )
 if 31 - 31: ooOOOoO - OOooOOo / I11i * OOooOOo / I1ii11iIi11i + I11i
elif ii1ii111 == 1016 :
 oOIIiIi ( oO0o0 , OOoOooOoOOOoo , I1111i )
 if 46 - 46: I1111IIi * oO0o / Ii1IIIi1 + I1ii11iIi11i
elif ii1ii111 == 1017 :
 i1i1I111iIi1 ( )
 if 24 - 24: I11i1ii1 % Ii1IIIi1 . o0o00Oo0O * I1ii11iIi11i
elif ii1ii111 == 1018 :
 iII1iii ( oO0o0 )
 if 52 - 52: o0o00Oo0O . iiiiiiii1 + O0OOOoOoo0 / Ii
elif ii1ii111 == 1023 :
 oOooOOo00ooO ( )
 if 52 - 52: o000O0o % I1ii11iIi11i * IIiIiII11i
elif ii1ii111 == 1024 :
 o0OooOO0 ( oO0o0 )
 if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
elif ii1ii111 == 1025 :
 iI1i ( oO0o0 )
 if 27 - 27: ooOoO0O00 - o000O0o + Ii1IIIi1
elif ii1ii111 == 4001 :
 iiIi11iI1iii ( )
 if 3 - 3: I1111IIi % iiiiiiii1 . ii
elif ii1ii111 == 4002 :
 OOOooo ( )
 if 19 - 19: iiiiiiii1 * ii1ii11IIIiiI - o000O0o
elif ii1ii111 == 4003 :
 I1I11Iiii111 ( )
 if 78 - 78: oO0o - ii1ii11IIIiiI / Ii1IIIi1
elif ii1ii111 == 4004 :
 ooI1i ( )
 if 81 - 81: OOooOOo
elif ii1ii111 == 4005 :
 ooo000o000 ( )
 if 21 - 21: O0OOOoOoo0 / Ii1IIIi1 % I1111IIi
elif ii1ii111 == 4006 :
 O0ooO0OoO00o ( )
 if 51 - 51: ooOOOoO + I11i1ii1 / oOo0O0Ooo
elif ii1ii111 == 4007 :
 o0Oooo ( )
 if 3 - 3: iI11I1II1I1I / Ii1IIIi1 % o000O0o . ii1ii11IIIiiI - ii1ii11IIIiiI
elif ii1ii111 == 4008 :
 Iiii1iI1i ( )
 if 55 - 55: Ii % ii + o0o00Oo0O
elif ii1ii111 == 4009 : iIIiIiI1I1 ( )
elif ii1ii111 == 4010 : OOO0O00Oo ( )
elif ii1ii111 == 3000 :
 i1i11IiII ( )
 if 7 - 7: I11i1ii1 - Ii * O0OOOoOoo0 / ii1ii11IIIiiI - I11i
elif ii1ii111 == 3001 :
 II1i1iI ( )
 if 62 - 62: I11i - iI11I1II1I1I . ooOOOoO . ii1ii11IIIiiI * ii1ii11IIIiiI
elif ii1ii111 == 3002 :
 iI111I1 ( oO0o0 )
 if 24 - 24: ooOOOoO
elif ii1ii111 == 3003 :
 iIiii1IIi1I ( oO0o0 )
 if 93 - 93: oOo0O0Ooo % oO0o / Ii / ooOOOoO
elif ii1ii111 == 3004 :
 oo0o0ooOoo00O ( oO0o0 )
 if 60 - 60: I11i1ii1 - ii1ii11IIIiiI . oOo0O0Ooo * o000O0o * Ii
elif ii1ii111 == 404 :
 O0ooooOO ( I1111i , oO0o0 , OOoOooOoOOOoo )
 if 29 - 29: oO0o - I1ii11iIi11i . o000O0o / oO0o % Ii
elif ii1ii111 == 405 :
 IIIiII11II11 ( oO0o0 )
 if 26 - 26: I11i1ii1 . iiiiiiii1 / IIiIiII11i % ii1ii11IIIiiI
elif ii1ii111 == 7030 :
 Ooo0 ( )
 if 82 - 82: Ii1IIIi1 % o0o00Oo0O % iI11I1II1I1I % I1111IIi + Ii
elif ii1ii111 == 7021 :
 I1iI11ii ( I1111i )
 if 64 - 64: ooOoO0O00 / I1111IIi . I1111IIi - iiiiiiii1 % Ii1IIIi1 . IIiIiII11i
elif ii1ii111 == 7022 :
 o0oOoOOO ( I1111i )
 if 78 - 78: iiiiiiii1 - o0o00Oo0O - iiiiiiii1 . iI11I1II1I1I % Ii1I . ii
elif ii1ii111 == 7000 :
 OoI11II ( I1111i , oO0o0 , img )
 if 64 - 64: I1111IIi
elif ii1ii111 == 7050 :
 oO00000oO0o0O ( oO0o0 )
 if 21 - 21: I11i - I11i1ii1 * ii . ii
elif ii1ii111 == 7051 :
 ooo0O0O ( oO0o0 )
 if 17 - 17: Ii1IIIi1 - O0OOOoOoo0 % oOo0O0Ooo * Ii1IIIi1 * iI11I1II1I1I . I11i
elif ii1ii111 == 7052 :
 I1I11I11I1 ( oO0o0 )
 if 58 - 58: o000O0o - IIiIiII11i + o0o00Oo0O
elif ii1ii111 == 7053 :
 i1I11i ( oO0o0 )
 if 54 - 54: iI11I1II1I1I - I1111IIi - I1111IIi
elif ii1ii111 == 7054 :
 CoolPlay ( oO0o0 )
 if 18 - 18: Ii + iI11I1II1I1I . Ii
elif ii1ii111 == 7060 :
 oOoO00O00o ( )
 if 63 - 63: O0OOOoOoo0 - oO0o * Ii1IIIi1
elif ii1ii111 == 7061 :
 I1i11i ( oO0o0 )
 if 89 - 89: O0OOOoOoo0 / I1ii11iIi11i
elif ii1ii111 == 7063 :
 ooO0O00O0O0 ( oO0o0 )
 if 66 - 66: I11i + OOooOOo % ii . ooOOOoO
elif ii1ii111 == 7062 :
 O0Ooo0O0O ( oO0o0 )
 if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
elif ii1ii111 == 7064 :
 NATatozcat ( )
 if 93 - 93: ooOoO0O00 + iiiiiiii1 / oO0o - ooOOOoO % I1ii11iIi11i / ii1ii11IIIiiI
elif ii1ii111 == 7067 :
 OOOO0 ( oO0o0 )
 if 1 - 1: I1ii11iIi11i / ii1ii11IIIiiI . Ii % Ii1IIIi1 + I11i + o0o00Oo0O
elif ii1ii111 == 7066 :
 NATatozA ( oO0o0 )
 if 54 - 54: iiiiiiii1 + I11i1ii1 % I1111IIi
elif ii1ii111 == 7065 :
 OOo0OOo ( oO0o0 )
 if 83 - 83: I11i * iI11I1II1I1I
elif ii1ii111 == 7070 :
 i1II111II1 ( )
 if 36 - 36: OOooOOo + IIiIiII11i - oO0o % I11i1ii1 * ooOoO0O00
elif ii1ii111 == 7071 :
 DIZIlist ( oO0o0 )
 if 4 - 4: ii1ii11IIIiiI + oO0o * Ii1I
elif ii1ii111 == 7072 :
 DIZIpull ( oO0o0 )
 if 13 - 13: OOooOOo - I1111IIi * iI11I1II1I1I * o0o00Oo0O
elif ii1ii111 == 7073 :
 WATCHDIZI ( oO0o0 )
 if 26 - 26: ii + o000O0o + oO0o . o0o00Oo0O
elif ii1ii111 == 7002 :
 Iii1i1 ( )
 if 46 - 46: ii - I1ii11iIi11i * iiiiiiii1 * Ii1IIIi1 * iiiiiiii1 . o000O0o
elif ii1ii111 == 7003 :
 OOOoooO0o0o ( oO0o0 )
 if 96 - 96: ii1ii11IIIiiI / I1111IIi % I11i + ooOOOoO
elif ii1ii111 == 7004 :
 OooOoO000OOoo0 ( oO0o0 )
 if 46 - 46: oO0o * oOo0O0Ooo
elif ii1ii111 == 7020 :
 oooOOOoO ( oO0o0 )
 if 25 - 25: iiiiiiii1 . I1111IIi % o0o00Oo0O % ooOoO0O00
elif ii1ii111 == 7001 :
 O0O0Oo00 ( )
 if 53 - 53: o0o00Oo0O % I11i1ii1
elif ii1ii111 == 7010 :
 OOO00Oo00o ( oO0o0 )
 if 41 - 41: I1111IIi
elif ii1ii111 == 7011 :
 O0Ooo000OO00 ( oO0o0 )
 if 29 - 29: I11i1ii1
elif ii1ii111 == 7012 :
 oOi1IiIiIii11I ( oO0o0 )
 if 70 - 70: o000O0o . o0o00Oo0O % ooOOOoO % I1111IIi - ooOOOoO * Ii1I
elif ii1ii111 == 7013 :
 cnfTVPlay2 ( oO0o0 )
elif ii1ii111 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oO0o0 )
elif ii1ii111 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oO0o0 )
elif ii1ii111 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1111i , oO0o0 , OOoOooOoOOOoo )
elif ii1ii111 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif ii1ii111 == 7018 :
 ii11 ( )
elif ii1ii111 == 7019 :
 CNF_Studio_Indexer . List_Movies ( oO0o0 )
elif ii1ii111 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oO0o0 )
elif ii1ii111 == 7024 :
 CNF_Studio_Indexer . Box_Office ( oO0o0 )
 if 22 - 22: ooOoO0O00
elif ii1ii111 == 8000 :
 oO0OooO00Oo ( )
elif ii1ii111 == 8001 :
 i11i1IiIi ( )
elif ii1ii111 == 8002 :
 IiIiIIII ( )
elif ii1ii111 == 8003 :
 O000o ( )
elif ii1ii111 == 8004 :
 iIiiI1iIiI1I ( )
elif ii1ii111 == 8005 :
 iiiiIIii1I ( )
elif ii1ii111 == 8006 :
 I1111I1i1i ( I1111i , oO0o0 )
elif ii1ii111 == 8030 :
 IiiI1I ( oO0o0 )
elif ii1ii111 == 8045 :
 i1111I1iii1 ( oO0o0 )
elif ii1ii111 == 8046 :
 o0Oo00o0 ( oO0o0 )
elif ii1ii111 == 8047 :
 oOOoOo0Ooo ( oO0o0 )
elif ii1ii111 == 8048 :
 I1Ii111I111 ( oO0o0 )
elif ii1ii111 == 8049 :
 iIi11 ( oO0o0 )
elif ii1ii111 == 804900 :
 O00oOoOo0ooO0O0oo ( oO0o0 )
elif ii1ii111 == 8020 :
 Ii1i1iI ( )
elif ii1ii111 == 8021 :
 O0O00 ( oO0o0 )
elif ii1ii111 == 8022 :
 O00o0OO0O ( oO0o0 )
elif ii1ii111 == 8023 :
 o0o00O0oO ( oO0o0 )
elif ii1ii111 == 8040 :
 o0OoOO ( )
elif ii1ii111 == 8041 :
 ooo000OO ( oO0o0 )
elif ii1ii111 == 8042 :
 ooO0 ( oO0o0 )
elif ii1ii111 == 8043 :
 yt . PlayVideo ( oO0o0 )
elif ii1ii111 == 8044 :
 IIiIIiiiiiII1 ( oO0o0 )
elif ii1ii111 == 8060 :
 Iii ( )
elif ii1ii111 == 8061 :
 OOooooO0 ( oO0o0 )
elif ii1ii111 == 8064 :
 i1iI1 ( )
elif ii1ii111 == 8065 :
 OOOoO00oo0ooOo0 ( oO0o0 )
elif ii1ii111 == 8070 :
 II1I1Ii11 ( )
elif ii1ii111 == 8071 :
 I1I1iiI ( oO0o0 )
elif ii1ii111 == 7080 :
 o0oOOO0 ( oO0o0 )
elif ii1ii111 == 8090 :
 oO0OOOO00o ( )
elif ii1ii111 == 8091 :
 OoooooO0 ( oO0o0 )
elif ii1ii111 == 8092 :
 iiII ( oO0o0 )
elif ii1ii111 == 8093 :
 iIOOOO00 ( oO0o0 )
elif ii1ii111 == 8081 :
 ooo0ooo0Oo ( )
elif ii1ii111 == 8062 :
 o0Ooo ( oO0o0 )
elif ii1ii111 == 8063 :
 ii1IiIiI1iiii ( oO0o0 )
elif ii1ii111 == 8050 :
 oOo0000ooO ( )
elif ii1ii111 == 8051 :
 I1Io0oO0oo ( oO0o0 )
elif ii1ii111 == 8052 :
 ooOO00Oo ( oO0o0 )
elif ii1ii111 == 8085 :
 i11ii11IiI1 ( )
elif ii1ii111 == 8086 :
 iio0Oo ( oO0o0 )
elif ii1ii111 == 8087 :
 OoIII ( oO0o0 )
elif ii1ii111 == 8088 :
 OO00O ( oO0o0 , I1111i )
elif ii1ii111 == 9000 :
 iI11II1i1I1 ( )
elif ii1ii111 == 1111 :
 oO0O0 ( )
elif ii1ii111 == 9001 :
 iIII ( )
elif ii1ii111 == 9002 :
 O0oO0OOoOOO0oO ( )
elif ii1ii111 == 9003 :
 II1Iiiii ( )
elif ii1ii111 == 9004 :
 World1 ( )
elif ii1ii111 == 9005 :
 World2 ( oO0o0 )
elif ii1ii111 == 9006 :
 World3 ( oO0o0 )
elif ii1ii111 == 9007 :
 i1iI11IiII ( )
elif ii1ii111 == 9008 :
 oO00Oo0OO ( oO0o0 )
elif ii1ii111 == 9009 :
 i11iIIiii ( oO0o0 )
elif ii1ii111 == 9010 :
 i1i1I1i111II ( )
elif ii1ii111 == 9011 :
 OoO00OOoO ( oO0o0 )
elif ii1ii111 == 50 :
 II1iI1iiiI ( oO0o0 )
elif ii1ii111 == 9020 :
 champlist ( )
elif ii1ii111 == 9021 :
 i1Iiiiii1II ( )
elif ii1ii111 == 9022 :
 i1iII1i ( )
elif ii1ii111 == 9023 :
 Ii1I11Ii1iI ( )
elif ii1ii111 == 9024 :
 o0Oooo0O00Ooo ( oO0o0 )
elif ii1ii111 == 9030 :
 iiIi1i ( oO0o0 )
elif ii1ii111 == 9031 :
 I1i11IIiiIiI ( oO0o0 )
elif ii1ii111 == 9032 :
 II1iiiiI1Ii11 ( oO0o0 )
elif ii1ii111 == 9033 :
 O0oo ( oO0o0 )
elif ii1ii111 == 9034 :
 oOoO00o ( )
elif ii1ii111 == 7085 :
 OOoo ( oO0o0 )
elif ii1ii111 == 7086 :
 iiiOOOoO0o ( oO0o0 )
elif ii1ii111 == 7087 :
 oooo00OoOoO ( o000 )
elif ii1ii111 == 9666 :
 I1iIIiiIIi1i ( oO0o0 )
elif ii1ii111 == 10100 : ii1IIi1IIIIi1 ( )
elif ii1ii111 == 101001 : OOI1 ( oO0o0 )
elif ii1ii111 == 10105 : Oo0ooOO ( oO0o0 )
elif ii1ii111 == 10106 : Iiii ( oO0o0 )
elif ii1ii111 == 10104 : oO0oOO ( oO0o0 )
elif ii1ii111 == 10107 : oooO00oOOooO ( )
elif ii1ii111 == 10103 : Ii11i1I1 ( oO0o0 )
elif ii1ii111 == 10108 : IIiii1I1I ( oO0o0 )
elif ii1ii111 == 10000 : Origin_Menu ( )
elif ii1ii111 == 10001 : oooooOo0 ( )
elif ii1ii111 == 10002 : OO0 ( )
elif ii1ii111 == 10003 : I1ii1ii11i1I ( )
elif ii1ii111 == 10004 : OOo00O ( oO0o0 )
elif ii1ii111 == 10005 : ooo ( )
elif ii1ii111 == 10006 : Ii1iii ( oO0o0 )
elif ii1ii111 == 10007 : I1i11IIIi ( oO0o0 , OOoOooOoOOOoo )
elif ii1ii111 == 10008 : I1iO00O000oOO0oO ( )
elif ii1ii111 == 10009 : O0ooO0 ( )
elif ii1ii111 == 10010 : o00oOo0OoO0oO ( oO0o0 )
elif ii1ii111 == 10011 : OoO0ooOOoo ( oO0o0 )
elif ii1ii111 == 10012 : OOOOo0o00OO0000 ( oO0o0 )
elif ii1ii111 == 10113 : GRABG ( oO0o0 , I1111i )
elif ii1ii111 == 10109 : IIiI ( oO0o0 )
elif ii1ii111 == 10013 : IiIIIIIii ( oO0o0 )
elif ii1ii111 == 10014 : Ii1Ii11I ( )
elif ii1ii111 == 10015 : i11IiIi ( )
elif ii1ii111 == 10016 : i1ii ( oO0o0 )
elif ii1ii111 == 10017 : iIo00oo ( )
elif ii1ii111 == 10018 : o000OO00OoO00 ( )
elif ii1ii111 == 10019 : ooi11I ( )
elif ii1ii111 == 10020 : iIIiI1 ( )
elif ii1ii111 == 10021 : Oo0ooo ( )
elif ii1ii111 == 10022 : oOO0O00o0O0 ( oO0o0 )
elif ii1ii111 == 10023 : oo0oOi1i1IIi ( I1111i , oO0o0 )
elif ii1ii111 == 10024 : I1IIIIII1 ( oO0o0 )
elif ii1ii111 == 10025 : I1II ( )
elif ii1ii111 == 10026 : ooo00O0OOo ( )
elif ii1ii111 == 10027 : iIIII1Iii11 ( )
elif ii1ii111 == 10028 : IiI1IIiiiii ( )
elif ii1ii111 == 10029 : oOO0ooO ( )
elif ii1ii111 == 423 : oOiiIIIII ( oO0o0 )
elif ii1ii111 == 426 : OooooO0o0 ( oO0o0 )
elif ii1ii111 == 10030 : Izle_Films ( )
elif ii1ii111 == 10031 : Latest_Izle_Movies ( )
elif ii1ii111 == 10032 : Izle_Genres ( )
elif ii1ii111 == 10033 : Izle_Pop_Movies ( )
elif ii1ii111 == 10034 : Izle_Boxsets ( )
elif ii1ii111 == 10035 : Izle_Search ( )
elif ii1ii111 == 10036 : Izle_Genres_Movie ( oO0o0 )
elif ii1ii111 == 10037 : Izle_Boxset_single ( oO0o0 )
elif ii1ii111 == 10038 : Izle_IFRAME ( )
elif ii1ii111 == 10039 : Izle_Boxsets_Next ( oO0o0 )
elif ii1ii111 == 10040 : III1ii1I ( )
elif ii1ii111 == 10041 : ooOOO0oOoooOo ( oO0o0 )
elif ii1ii111 == 10042 : oo0O0O ( oO0o0 )
elif ii1ii111 == 10043 : I1IiIi1iiI ( )
elif ii1ii111 == 10044 : O0o0ooOoO0 ( oO0o0 )
elif ii1ii111 == 10045 : IiIIIii1i1iI ( I1111i )
elif ii1ii111 == 10046 : O0oIii11IiiIi ( oO0o0 )
elif ii1ii111 == 10047 : oOooooooO0o ( oO0o0 )
elif ii1ii111 == 10048 : O00O0ii11i1i ( oO0o0 )
elif ii1ii111 == 10049 : ooO00OO ( oO0o0 )
elif ii1ii111 == 10050 : iI1i11iII111 ( )
elif ii1ii111 == 10051 : OOO0o0oOOo ( )
elif ii1ii111 == 10052 : ooO0000 ( )
elif ii1ii111 == 10053 : Addon ( oO0o0 )
elif ii1ii111 == 10054 : OoOO000OO00 ( oO0o0 , I1111i )
elif ii1ii111 == 10055 :
 I1I11 ( "addFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 I1iII ( I1111i , oO0o0 , OOoOooOoOOOoo , o0ooooO0o0O , II11ii1111Ii )
elif ii1ii111 == 10056 :
 I1I11 ( "rmFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 ii1iI11 ( I1111i )
elif ii1ii111 == 10057 :
 I1I11 ( "getFavorites" )
 iIiiIiIIiI ( )
elif ii1ii111 == 10058 : ooO ( )
elif ii1ii111 == 10059 : Donators_Guide ( )
elif ii1ii111 == 10060 : oo000o0000oO ( )
elif ii1ii111 == 10061 : oOOOOO0Ooooo ( )
elif ii1ii111 == 10062 : o0oOoOo0 ( I1111i , oO0o0 , o000 )
elif ii1ii111 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
elif ii1ii111 == 10064 : i111i1I1ii1i ( )
elif ii1ii111 == 10065 : OOo000o0 ( oO0o0 )
elif ii1ii111 == 10066 : O0O0ooOoOO0OO ( oO0o0 )
elif ii1ii111 == 10068 : OOOOO0O00 ( oO0o0 )
elif ii1ii111 == 10069 : ii1I1IiiI1ii1i ( oO0o0 )
elif ii1ii111 == 10070 : o0oooOoo0OoOO ( oO0o0 )
elif ii1ii111 == 10071 : Genie_Watch ( )
elif ii1ii111 == 10072 : Ooii1IIi1ii ( )
elif ii1ii111 == 10073 : IIIIIIi1i ( oO0o0 )
elif ii1ii111 == 10074 : o0o0OO0o00o0O ( oO0o0 )
elif ii1ii111 == 10075 : i111Iii ( OOoOooOoOOOoo , I1111i , oO0o0 )
elif ii1ii111 == 10076 : IIi1i ( oO0o0 )
elif ii1ii111 == 10077 : IiIIiI ( oO0o0 )
elif ii1ii111 == 10078 : IiI ( )
elif ii1ii111 == 10079 : Genie_Watch_Tv_Shows ( )
elif ii1ii111 == 10080 : Genie_Watch_Tv_Genre ( oO0o0 )
elif ii1ii111 == 10081 : Genie_Watch_TV_PlayRun ( oO0o0 )
elif ii1ii111 == 10082 : Genie_Watch_TV_Episodes ( oO0o0 , OOoOooOoOOOoo )
elif ii1ii111 == 10083 : Genie_Watch_Tv_Recent ( oO0o0 )
elif ii1ii111 == 10084 : ooo0O ( )
elif ii1ii111 == 10085 : Iiii1i1 ( )
elif ii1ii111 == 10086 : i1IiiiI1iI ( )
elif ii1ii111 == 20000 : O0o0O0OO00o ( )
elif ii1ii111 == 20001 : IiIiIi ( oO0o0 )
elif ii1ii111 == 20002 : i1iIii1II1i ( oO0o0 )
elif ii1ii111 == 20003 : IiiIiiIIII ( oO0o0 )
elif ii1ii111 == 20004 : iIiI1I1 ( oO0o0 )
elif ii1ii111 == 20005 : O0OOo ( oO0o0 )
elif ii1ii111 == 21004 : OOOO0oooo ( )
elif ii1ii111 == 21005 : IiIii11I ( oO0o0 )
elif ii1ii111 == 21006 : oooo0oOOoO000 ( oO0o0 )
elif ii1ii111 == 21007 : oOo00OO0ooOOO ( oO0o0 )
elif ii1ii111 == 30000 : o0i1Ii11II ( )
elif ii1ii111 == 30001 : iiII1IIii1i1 ( )
elif ii1ii111 == 10012 : Resolve ( oO0o0 )
elif ii1ii111 == 30003 : I11iIiI1 ( )
elif ii1ii111 == 30004 : o0oOo ( oO0o0 )
elif ii1ii111 == 30005 : III1I1ii ( oO0o0 )
elif ii1ii111 == 30006 : iIiII1iiiiI ( )
elif ii1ii111 == 30007 : Iii1I ( )
elif ii1ii111 == 30008 : i1i1IIiII1I ( oO0o0 )
elif ii1ii111 == 30009 : OOOo00o ( oO0o0 )
elif ii1ii111 == 30010 : O00O0 ( oO0o0 )
elif ii1ii111 == 30011 : iiIIiIi ( )
elif ii1ii111 == 30012 : o0Ooi1II11i1iI1 ( )
elif ii1ii111 == 30013 : iIi11iI1i ( )
elif ii1ii111 == 30014 : OooOoO0OOoOOO0o0o ( )
elif ii1ii111 == 30015 : ooOo0O0 ( oO0o0 , OOoOooOoOOOoo , o0ooooO0o0O )
elif ii1ii111 == 30016 : iIIi111IiII1i ( oO0o0 )
elif ii1ii111 == 30019 : o0oi1I1I1I ( oO0o0 )
elif ii1ii111 == 30017 : i11ii111i1ii ( oO0o0 )
elif ii1ii111 == 30018 : oO00oo ( oO0o0 )
elif ii1ii111 == 30030 : oO00o0oOoo ( )
elif ii1ii111 == 30031 : ii111iiIii ( )
elif ii1ii111 == 30032 : iiI ( )
elif ii1ii111 == 30033 : oOOI1 ( )
elif ii1ii111 == 30034 : OOI1i ( )
elif ii1ii111 == 30035 : i11i11Iiii11i ( oO0o0 )
elif ii1ii111 == 30036 : II11II1I ( oO0o0 )
elif ii1ii111 == 30037 : O0OO00000o00 ( oO0o0 )
elif ii1ii111 == 30038 : oOOo0ooO0 ( )
elif ii1ii111 == 30039 : OooOoOO0 ( )
elif ii1ii111 == 50000 : oOOo0O00o ( )
elif ii1ii111 == 50001 : IiI1i111i ( )
elif ii1ii111 == 50002 : o0o0O0o ( oO0o0 )
elif ii1ii111 == 50003 : oo0OoOO000O ( o000 )
elif ii1ii111 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif ii1ii111 == 60001 : IiIIII1iiIIi ( )
elif ii1ii111 == 60002 : OooOOOOOo ( I1111i )
elif ii1ii111 == 60003 : I1IIiIIi1Ii1III ( I1111i )
elif ii1ii111 == 60004 : OooOo ( oO0o0 )
elif ii1ii111 == 50004 : iiIiIIIiiI ( )
elif ii1ii111 == 50005 : speedtest . runtest ( oO0o0 )
elif ii1ii111 == 70001 : iI1 ( )
elif ii1ii111 == 70002 : iIiII1 ( oO0o0 )
elif ii1ii111 == 70003 : i111iii1I1 ( oO0o0 )
elif ii1ii111 == 70004 : iiIiII1 ( oO0o0 )
elif ii1ii111 == 70005 : ii111iI ( oO0o0 )
elif ii1ii111 == 70006 : ii11I1 ( )
elif ii1ii111 == 50006 : OO0O000 ( i1 , i1111 )
elif ii1ii111 == 80000 : I1i1I ( )
elif ii1ii111 == 80001 : resolvefilmon ( oO0o0 )
elif ii1ii111 == 80002 : iIiiIiiI1Ii111i ( )
elif ii1ii111 == 80003 : I1IIIi1i ( I1111i , oO0o0 , "None" )
elif ii1ii111 == 80004 : OOO000Oo ( I1111i , oO0o0 )
elif ii1ii111 == 80005 : IiIi ( )
elif ii1ii111 == 80006 : iII11iiIIi11 ( oO0o0 )
elif ii1ii111 == 80007 : Iiii11I ( oO0o0 )
elif ii1ii111 == 80008 : OO0ooo0 ( )
elif ii1ii111 == 80009 : IIiiIiIIiI1 ( )
elif ii1ii111 == 80010 : I1IiI ( oO0o0 )
elif ii1ii111 == 80011 : I1I11Oo0 ( oO0o0 )
elif ii1ii111 == 80012 : oO0iIiII111 ( )
elif ii1ii111 == 90000 : oOOOo0Oooo ( I1111i , oO0o0 )
elif ii1ii111 == 90001 : Ii1I1I1i1Ii ( )
elif ii1ii111 == 90002 : o0O0oo0OO0O ( )
elif ii1ii111 == 90003 : oooo0OOO00O00 ( oO0o0 )
elif ii1ii111 == 90004 : i11I111I1 ( oO0o0 )
elif ii1ii111 == 90005 : OOOoO000 ( oO0o0 )
elif ii1ii111 == 90006 : O00OoO ( oO0o0 )
elif ii1ii111 == 90007 : I11i11 ( oO0o0 )
elif ii1ii111 == 90008 : i11iI1111ii1I ( oO0o0 )
elif ii1ii111 == 90009 : iiIIii ( oO0o0 )
elif ii1ii111 == 90010 : iiIiI1i1 ( )
elif ii1ii111 == 90020 : Ii1iIIII1i ( )
elif ii1ii111 == 90021 : hellyeah2 ( oO0o0 )
elif ii1ii111 == 90022 : hellyeah3 ( oO0o0 )
elif ii1ii111 == 90023 : OOOOoOo00OO ( )
elif ii1ii111 == 90024 : OooO0oOo ( oO0o0 )
elif ii1ii111 == 90025 : II1IIIiiI11 ( oO0o0 )
if 82 - 82: o000O0o . iI11I1II1I1I - Ii1I
elif ii1ii111 == 90030 : I11iII ( )
elif ii1ii111 == 90031 : I1i1i1iii ( )
elif ii1ii111 == 90032 : iIIii ( oO0o0 )
elif ii1ii111 == 90033 : ii1iii1i ( oO0o0 )
elif ii1ii111 == 90034 : ooO0O00Oo0o ( oO0o0 )
elif ii1ii111 == 90035 : I1i ( oO0o0 )
elif ii1ii111 == 90036 : Ooo00OoO ( oO0o0 )
elif ii1ii111 == 90039 : oOOOOoo000Ooo ( oO0o0 )
elif ii1ii111 == 90037 : iiIII1II ( oO0o0 )
elif ii1ii111 == 90038 : O0OO0O ( )
if 55 - 55: I1ii11iIi11i % ii1ii11IIIiiI . iI11I1II1I1I * iiiiiiii1
elif ii1ii111 == 10090 : oOoOoOoo0 ( )
elif ii1ii111 == 10091 : i11ii ( oO0o0 )
elif ii1ii111 == 10092 : oOOo00ooO ( oO0o0 )
elif ii1ii111 == 10093 : I111I ( oO0o0 , OOoOooOoOOOoo )
elif ii1ii111 == 10094 : iIiIi1i1Iiii ( oO0o0 , OOoOooOoOOOoo )
if 33 - 33: o0o00Oo0O - oOo0O0Ooo / Ii1I / oO0o + O0OOOoOoo0 - o000O0o
elif ii1ii111 == 10095 : IIiI1 ( )
elif ii1ii111 == 10096 : i1IIi1i1Ii1 ( oO0o0 )
elif ii1ii111 == 10097 : Oo0oOo0O0O0o ( oO0o0 )
elif ii1ii111 == 10098 : o0oOOo0O0O000 ( oO0o0 )
elif ii1ii111 == 10099 : oO00 ( oO0o0 )
if 27 - 27: iiiiiiii1 + I11i1ii1 - iiiiiiii1 % Ii * I1ii11iIi11i * I11i
elif ii1ii111 == 10200 : o0o0O ( )
elif ii1ii111 == 10201 : i1I1iIi1IiI ( oO0o0 )
elif ii1ii111 == 10202 : Oo0O ( oO0o0 )
elif ii1ii111 == 10203 : RT4 ( oO0o0 )
if 88 - 88: Ii1IIIi1
elif ii1ii111 == 90040 : ooooO0oOoOOoO ( )
elif ii1ii111 == 90041 : I11IiIi ( oO0o0 )
elif ii1ii111 == 90042 : O0OOO0 ( oO0o0 )
elif ii1ii111 == 90043 : I1iIIIiIi1 ( oO0o0 )
elif ii1ii111 == 90044 : I111i1Ii1i1 ( oO0o0 )
elif ii1ii111 == 90045 : II11I ( )
elif ii1ii111 == 90046 : iI1IIi1IiI ( oO0o0 )
elif ii1ii111 == 90050 : I1ii11 ( )
elif ii1ii111 == 90051 : o0OO0O0OO0oO0 ( oO0o0 )
elif ii1ii111 == 90052 : ooo0oo00O00oO ( oO0o0 )
elif ii1ii111 == 90053 : oo0oooo0OoO0o ( oO0o0 )
elif ii1ii111 == 90054 : I1IIiiI1II1 ( oO0o0 )
elif ii1ii111 == 90055 : OOoooOoO0Oo ( )
if 25 - 25: oO0o + I11i . I11i1ii1 - ii1ii11IIIiiI . o000O0o * ii1ii11IIIiiI
elif ii1ii111 == 100001 : Stand_up ( )
if 85 - 85: ooOoO0O00
elif ii1ii111 == 100003 : i1ii ( oO0o0 )
elif ii1ii111 == 100004 : I1IIIiI1I1ii1 ( oO0o0 )
elif ii1ii111 == 100005 : Resolve ( oO0o0 )
elif ii1ii111 == 100008 : Search ( )
elif ii1ii111 == 100007 : OOOIiiiii1iI ( oO0o0 )
elif ii1ii111 == 100009 : yt . PlayVideo ( oO0o0 )
elif ii1ii111 == 100010 : II11iI111i1 ( oO0o0 )
elif ii1ii111 == 100100 : ooO0o ( OOoOooOoOOOoo , oO0o0 , iI1I1iIi11II1 )
elif ii1ii111 == 100101 : I1iIiI11I1 ( oO0o0 , I1111i , o0ooooO0o0O , iI1I1iIi11II1 , OOoOooOoOOOoo )
elif ii1ii111 == 100102 : Ii1iI111 ( I1111i , oO0o0 , OOoOooOoOOOoo , o0ooooO0o0O )
elif ii1ii111 == 100106 : I1I1i1I ( oO0o0 , I1111i )
elif ii1ii111 == 100107 : i1II111i1 ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
