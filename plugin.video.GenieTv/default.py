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
IiiIII111iI = "3.4.0"
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
  iiOOooooO0Oo ( '[COLOR' + II + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cHM6Ly9hdGxhbnRpYzI4MC5zdGFydGRlZGljYXRlZC5uZXQvYm9zcy9kb2NzLw==' ) , 1006 , III1iII1I1ii + 'boss.png' , O0o0Oo , '' )
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
  iiOOooooO0Oo ( '[COLOR' + II + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cHM6Ly9hdGxhbnRpYzI4MC5zdGFydGRlZGljYXRlZC5uZXQvYm9zcy9kb2NzLw==' ) , 1006 , III1iII1I1ii + 'boss.png' , O0o0Oo , '' )
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
  OO0O000 ( 'Change Log 19/01/17 - v3.4.0' , 'General Maintence, Nothing To Scream About' )
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
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   O0OoOO0oo0 = '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   oOO = '[COLOR' + II + ']APPRENTICE[/COLOR]'
  i1Oo0oO00o = [ II1iiiiII , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , oOO , '[COLOR' + II + ']RAIZ TV[/COLOR]' , O0OoOO0oo0 , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   O0o0OO0000ooo ( )
  if i11I1II1I11i == 1 :
   oOIIiIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , OOoOooOoOOOoo , I1111i )
   if 4 - 4: ii1ii11IIIiiI
  if i11I1II1I11i == 2 :
   oOIIiIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , OOoOooOoOOOoo , I1111i )
  if i11I1II1I11i == 3 :
   OO0oOOoo ( )
  if i11I1II1I11i == 4 :
   oOIIiIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , OOoOooOoOOOoo , I1111i )
  if i11I1II1I11i == 5 :
   oOOO00o000o ( )
  if i11I1II1I11i == 6 :
   oOIIiIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , OOoOooOoOOOoo , I1111i )
 else :
  if 9 - 9: o000O0o + ooOOOoO / ooOOOoO
  if 12 - 12: ii % I11i * ooOOOoO % iI11I1II1I1I / ii1ii11IIIiiI
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']PANDORAS BOX[/COLOR]' , str ( I1I1IiI1 ) , 10025 , III1iII1I1ii + 'PandorasBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'DojoStreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Roadrunner-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'Technica-Streams.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , '' , 1017 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , III1iII1I1ii + 'raiztv.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , str ( I1I1IiI1 ) , 1023 , III1iII1I1ii + 'ScoobyStreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'ITVStreams.png' , O0o0Oo , '' )
  if 27 - 27: Ii % IIiIiII11i % ooOOOoO . o0o00Oo0O - I1ii11iIi11i + OOooOOo
 I1I11i ( 'movies' , 'MAIN' )
 if 57 - 57: iI11I1II1I1I / ooOOOoO - ooOoO0O00
def ooOOo00O00Oo ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
def IiII1 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( iIIII )
 for I1i11ii , i111iI in i1IIIII11I1IiI :
  if '[DIR]' in I1i11ii :
   OOo ( ( '[COLOR' + II + ']' + i111iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + i111iI , 1018 , III1iII1I1ii + 'SilentHunter.png' )
  if 'mkv' in i111iI :
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + i111iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + i111iI , 222 , III1iII1I1ii + 'SilentHunter.png' )
  if 'avi' in i111iI :
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + i111iI + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + i111iI , 222 , III1iII1I1ii + 'SilentHunter.png' )
   if 8 - 8: I11i1ii1 + IIiIiII11i / O0OOOoOoo0 / ooOOOoO
def OO0oOOoo ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , III1iII1I1ii + 'scraped.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 if 74 - 74: o0o00Oo0O / ooOoO0O00
def OoO ( url ) :
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 i1IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for I1111i , url , i1i1iII1 , iii11i1IIII , o0ooooO0o0O , Iio00 in i1IIIII11I1IiI :
  if iii11i1IIII == '123' :
   iii11i1IIII = III1iII1I1ii + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = III1iII1I1ii + 'appstreams.png'
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100010 , iii11i1IIII , o0ooooO0o0O , Iio00 )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , iii11i1IIII , o0ooooO0o0O , Iio00 )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , iii11i1IIII , o0ooooO0o0O , Iio00 )
  elif not 'http' in url :
   iiI1Ii1 ( I1111i , url , 100009 , iii11i1IIII , o0ooooO0o0O , Iio00 , '' )
  else :
   iiI1Ii1 ( I1111i , url , 100005 , iii11i1IIII , o0ooooO0o0O , Iio00 , '' )
   if 18 - 18: IIiIiII11i / I1111IIi
def IiIIii1 ( url ) :
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 O000OOO0OOo = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , Iio00 , o0ooooO0o0O , I1111i in O000OOO0OOo :
  if o00O0O == '123' :
   o00O0O = III1iII1I1ii + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = O0o0Oo
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100004 , o00O0O , o0ooooO0o0O , Iio00 )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , o00O0O , o0ooooO0o0O , Iio00 )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , o00O0O , o0ooooO0o0O , Iio00 )
  elif not 'http' in url :
   iiI1Ii1 ( I1111i , url , 100009 , o00O0O , o0ooooO0o0O , Iio00 , '' )
  else :
   iiI1Ii1 ( I1111i , url , 100005 , o00O0O , o0ooooO0o0O , Iio00 , '' )
   if 32 - 32: ii1ii11IIIiiI * o0o00Oo0O
def O00oOo00o0o ( url ) :
 if 85 - 85: O0OOOoOoo0 + ii * O0OOOoOoo0 - iiiiiiii1 % Ii
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 OOo00OoO = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIi1 in OOo00OoO :
  iii11i1IIII = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( iIi1 ) )
  for iii11i1IIII in iii11i1IIII :
   iii11i1IIII = iii11i1IIII
  I1111i = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( iIi1 ) )
  for I1111i in I1111i :
   if 'elete' in I1111i :
    pass
   elif 'rivate Vid' in I1111i :
    pass
   else :
    I1111i = ( I1111i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  i11iiI1111 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( iIi1 ) )
  for i11iiI1111 in i11iiI1111 :
   i11iiI1111 = i11iiI1111
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( iIi1 ) )
  for url in url :
   url = url
  iiI1Ii1 ( '[COLORred]' + str ( i11iiI1111 ) + '[/COLOR] : ' + str ( I1111i ) , str ( url ) , 100009 , str ( iii11i1IIII ) , O0o0Oo , '' , '' )
  I1I11i ( 'movies' , '' )
  if 97 - 97: I1ii11iIi11i * oOo0O0Ooo . iI11I1II1I1I
  if 16 - 16: I11i1ii1 % ii - Ii1IIIi1 * ii1ii11IIIiiI * Ii1I / ii
  if 31 - 31: ooOOOoO . iiiiiiii1 * I11i1ii1 + Ii * o000O0o
  if 93 - 93: Ii1I / iI11I1II1I1I * ooOoO0O00 % ii * o0o00Oo0O * ooOOOoO
  if 64 - 64: IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / I1ii11iIi11i . I11i1ii1 % I1111IIi
def iiI1I1ii ( iconimage , url , extra ) :
 iii11i1IIII = ' '
 o0ooO = ' '
 o0ooooO0o0O = ' '
 OoOOOo0o0ooo = ' '
 I1iiiiI1iI = Iiiiii111i1ii ( url )
 iii11i1IIII = re . compile ( '<img src="(.+?)">' ) . findall ( I1iiiiI1iI )
 for iii11i1IIII in iii11i1IIII :
  iii11i1IIII = iii11i1IIII
 iIiiiii1i = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( I1iiiiI1iI )
 for o0ooooO0o0O in iIiiiii1i :
  o0ooooO0o0O = o0ooooO0o0O
 i1IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( I1iiiiI1iI )
 for url , OoOOOo0o0ooo in i1IIIII11I1IiI :
  OoOOOo0o0ooo = 'S' + ( OoOOOo0o0ooo ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oO0Oo + url
  iiIi1IIiI ( ( OoOOOo0o0ooo ) . replace ( '  ' , '' ) , url , 100101 , iii11i1IIII , o0ooooO0o0O , o0ooO , '' )
  I1I11i ( 'Movies' , 'info' )
  if 23 - 23: ii1ii11IIIiiI . Ii1IIIi1
def i1II11II ( url , name , fanart , extra , iconimage ) :
 oOo00O000Oo0 = extra
 OoOOOo0o0ooo = name
 I1iiiiI1iI = Iiiiii111i1ii ( url )
 iii11i1IIII = iconimage
 i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( I1iiiiI1iI )
 for url , name , I1iI1I1I1i11i in i1IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oO0Oo + url
  I1iI1I1I1i11i = I1iI1I1I1i11i
  iiI11 = name + ' - [COLORred]' + I1iI1I1I1i11i + '[/COLOR]'
  iiIi1IIiI ( iiI11 , url , 100102 , iii11i1IIII , fanart , 'Aired : ' + I1iI1I1I1i11i , iiI11 )
  if 63 - 63: oO0o + Ii1I . iiiiiiii1 % iiiiiiii1
def oOOOO ( name , URL , iconimage , fanart ) :
 oO0OOoo0OO = Iiiiii111i1ii ( URL )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , name in i1IIIII11I1IiI :
  for i11I in oOOoo0Oo :
   if i11I in oO0o0 :
    URL = 'http://www.watchseriesgo.to/link/' + oO0o0
    iiI1Ii1 ( name , URL , 100106 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( i1IIIII11I1IiI ) <= 0 :
  iiIi1IIiI ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 49 - 49: IIiIiII11i . o000O0o . Ii % I1111IIi
  if 34 - 34: iiiiiiii1 % I1111IIi
def IiI1i ( url , name ) :
 oO0oOOoo00000 = name
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  oOo00 ( url , oO0oOOoo00000 )
 for url in i1I :
  oOo00 ( url , oO0oOOoo00000 )
 for url in ooOoO00 :
  oOo00 ( url , oO0oOOoo00000 )
  if 3 - 3: O0OOOoOoo0 % ooOoO0O00
def oOo00 ( url , season_name ) :
 if 'daclips.in' in url :
  Ii1IIiiIIi ( url , season_name )
 elif 'filehoot.com' in url :
  Oo000o ( url , season_name )
 elif 'allmyvideos.net' in url :
  i11I1iIi ( url , season_name )
 elif 'vidspot.net' in url :
  O0Oo ( url , season_name )
 elif 'vodlocker' in url :
  oOOOOoO00OoOO ( url , season_name )
 elif 'vidto' in url :
  oOooo0O0o ( url , season_name )
  if 72 - 72: iI11I1II1I1I / I1111IIi % O0OOOoOoo0 % Ii1IIIi1 - ooOOOoO % Ii1IIIi1
  if 100 - 100: I1ii11iIi11i + Ii
def oOooo0O0o ( url , season_name ) :
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0oO , I1111i in i1IIIII11I1IiI :
  OO000oooo0 ( O0oO , season_name )
  if 77 - 77: oOo0O0Ooo % o0o00Oo0O
  if 36 - 36: ii1ii11IIIiiI / IIiIiII11i / I1111IIi / I1111IIi + Ii1I
def i11I1iIi ( url , season_name ) :
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0oO , I1111i in i1IIIII11I1IiI :
  OO000oooo0 ( O0oO , season_name )
  if 95 - 95: I1111IIi
def O0Oo ( url , season_name ) :
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0OOoo0OO )
 for O0oO , I1111i in i1IIIII11I1IiI :
  OO000oooo0 ( O0oO , season_name )
  if 51 - 51: IIiIiII11i + I1111IIi . ooOoO0O00 . Ii1I + OOooOOo * oOo0O0Ooo
def oOOOOoO00OoOO ( url , season_name ) :
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0oO in i1IIIII11I1IiI :
  OO000oooo0 ( O0oO , season_name )
  if 72 - 72: o000O0o + o000O0o / IIiIiII11i . ii % ii1ii11IIIiiI
def Ii1IIiiIIi ( url , season_name ) :
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 i1IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0OOoo0OO )
 for O0oO in i1IIIII11I1IiI :
  OO000oooo0 ( O0oO , season_name )
  if 49 - 49: o000O0o . oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def Oo000o ( url , season_name ) :
 oO0OOoo0OO = Iiiiii111i1ii ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0oO in i1IIIII11I1IiI :
  OO000oooo0 ( O0oO , season_name )
  if 2 - 2: ii % Ii1IIIi1
def OO000oooo0 ( Link , season_name ) :
 if 'http:/' in Link :
  oOoOOo0oo0 ( Link )
  if 60 - 60: I11i1ii1 * iiiiiiii1 + I1ii11iIi11i
def IIi1i1IiIIi1i ( url ) :
 oO0OOoo0OO = OPEN_URL_1 ( url )
 oOOo0OOOOo0Oo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 for url in oOOo0OOOOo0Oo :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 67 - 67: o000O0o / O0OOOoOoo0 . ooOOOoO . iI11I1II1I1I
def iiIi1IIiI ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 iiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  if 30 - 30: ooOOOoO / ii1ii11IIIiiI . I1111IIi . ii - I1ii11iIi11i
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   IIiii . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiI , listitem = i111iiI1ii , isFolder = True )
 return IiIi1
 if 44 - 44: o0o00Oo0O * ii % I11i1ii1 + IIiIiII11i
 if 39 - 39: o000O0o % iI11I1II1I1I % o0o00Oo0O % ii * Ii1I + O0OOOoOoo0
def iiI1Ii1 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 iiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   IIiii . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiI , listitem = i111iiI1ii , isFolder = False )
 return IiIi1
 if 68 - 68: I1ii11iIi11i + Ii
def Oo0oOooo000OO ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 98 - 98: I11i + o0o00Oo0O % ooOoO0O00 - Ii1IIIi1 + I1ii11iIi11i
def OoOo000oOo0oo ( url ) :
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0O . play ( url ) . strip ( )
 except : pass
 if 68 - 68: o0o00Oo0O + OOooOOo / o000O0o - Ii1IIIi1 + iI11I1II1I1I % ii1ii11IIIiiI
def oOoOOo0oo0 ( url ) :
 oO0O = xbmc . Player ( )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 if 23 - 23: I11i1ii1 % I11i / ooOOOoO
def Iiiiii111i1ii ( url ) :
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
  if 5 - 5: iI11I1II1I1I
  if 72 - 72: o000O0o . iiiiiiii1 / OOooOOo + ooOOOoO % iI11I1II1I1I
  if 42 - 42: Ii1I * OOooOOo % I11i1ii1 - OOooOOo . Ii - iiiiiiii1
def o0Oooo ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0oO0oOO ( )
  if i11I1II1I11i == 1 :
   O000o0 ( )
  if i11I1II1I11i == 2 :
   oO0o000OoOoO0 ( )
  if i11I1II1I11i == 3 :
   OO0ooOOO0O00o ( )
  if i11I1II1I11i == 4 :
   Ooo0o0oo ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
 if 26 - 26: IIiIiII11i % Ii % iI11I1II1I1I % ooOOOoO * ooOOOoO * Ii1I
 if 24 - 24: IIiIiII11i % iiiiiiii1 - I11i1ii1 + oOo0O0Ooo * Ii1I
 if 2 - 2: ii1ii11IIIiiI - I1111IIi
def OO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 i1IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0OOoo0OO )
 for IIiIi1iI in i1IIIII11I1IiI :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   OO0OO00oo0 = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OO0O000 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + OO0OO00oo0 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   i11I1II1I11i = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if i11I1II1I11i == 0 :
    iIIIiIii ( IIiIi1iI )
    O0O0ooOOO ( )
   elif i11I1II1I11i == 1 :
    ooo ( IIiIi1iI )
  else :
   pass
   if 94 - 94: OOooOOo - I1ii11iIi11i - oOo0O0Ooo % ooOoO0O00
def ooo ( addon ) :
 OO0OO00oo0 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 19 - 19: I11i
def iIIIiIii ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 Iiii1I1 = os . path . join ( I11II1i , 'default.py' )
 O0II11i11II = open ( Iiii1I1 , "w+" )
 if 29 - 29: I1ii11iIi11i % oO0o % I1111IIi . I11i / ii * I11i1ii1
 O0II11i11II . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 O0II11i11II . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 O0II11i11II . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 54 - 54: o0o00Oo0O
 if 68 - 68: oO0o * I11i . I11i1ii1 % o000O0o % iiiiiiii1
 if 75 - 75: OOooOOo
 if 34 - 34: o0o00Oo0O
def OooOOOo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 O0O0o0o0o = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 IIIIIiI = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 Iii1I1111ii = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 Oo0000O0OOooO = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url , iiO0oOo00o , o0ooooO0o0O , Iio00 in O0O0o0o0o :
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 90037 , iiO0oOo00o , o0ooooO0o0O , Iio00 )
  elif I1111i == 'Search' :
   iiOOooooO0Oo ( 'Search' , url , 90038 , iiO0oOo00o , o0ooooO0o0O , Iio00 )
  else :
   OOiIiIIi1 ( I1111i , url , 222 , iiO0oOo00o , o0ooooO0o0O , Iio00 )
 for I1111i , o00O0O , url , O00OO in IIIIIiI :
  iiOOooooO0Oo ( I1111i , url , 90037 , o00O0O , O00OO , '' )
 for I1111i , o00O0O , url , O00OO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 90037 , o00O0O , O00OO , '' )
 for I1111i , url , o00O0O , O00OO in i1I :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , O00OO , '' )
 for I1111i , url , o00O0O , O00OO in ooOoO00 :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , O00OO , '' )
 for I1111i , url , o00O0O , O00OO in Iii1I1111ii :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , O00OO , '' )
 for I1111i , url , o00O0O in Oo0000O0OOooO :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , '' , '' )
  I1I11i ( 'tvshows' , 'Media Info 3' )
  if 65 - 65: ooOoO0O00 . ii * ii1ii11IIIiiI / I1111IIi
def OOOooo0OooOoO ( ) :
 oOoOOOo = [ 'serialsearch' , 'moviesearch' ]
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 if o0OOoOoO00 == '' :
  pass
 else :
  for I1iii in oOoOOOo :
   oOO0OO0O = I11 + I1iii + '.php'
   I1iiiiI1iI = OoOooO ( oOO0OO0O )
   if I1iiiiI1iI != 'Opened' :
    O000OOO0OOo = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( I1iiiiI1iI )
    for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O , Iio00 in O000OOO0OOo :
     if o0OOoOoO00 in I1111i . lower ( ) :
      o00o = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for i11I in o00o :
       if i11I == oO0o0 :
        I1111i = '[COLORred]* [/COLOR]' + ( I1111i ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        III11I = open ( o00OO00OoO , "a" )
        III11I . write ( 'item="' + I1111i + '"\n' )
        III11I . close
      if 'php' in oO0o0 :
       iiOOooooO0Oo ( I1111i , oO0o0 , 90037 , iiO0oOo00o , o0ooooO0o0O , Iio00 )
      else :
       OOiIiIIi1 ( I1111i , oO0o0 , 222 , iiO0oOo00o , o0ooooO0o0O , Iio00 )
       if 17 - 17: ii + Ii1IIIi1 * ooOOOoO * OOooOOo
   I1I11i ( 'tvshows' , 'Media Info 3' )
   if 36 - 36: o0o00Oo0O + I1ii11iIi11i
def iIIIi1i1I11i ( ) :
 oO0OOoo0OO = OoOooO ( 'http://www.tvcatchup.com/channels/' )
 O0 = OoOooO ( 'http://www.djing.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oOO0OO0OO = re . compile ( 'title="([^"]*)" >.+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( O0 )
 for IIiiiiiiIi1I1 , o00O0O , oO0o0 in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + oO0o0 , 90024 , 'http://www.tvcatchup.com' + o00O0O )
 for IIiiiiiiIi1I1 , oO0o0 , o00O0O in oOO0OO0OO :
  i1i11I1I1iii1 ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + oO0o0 , 90024 , o00O0O )
 for oO0o0 , o00O0O , I1111i in i1I :
  if 'Submit' in I1111i :
   pass
  elif '&lt;' in I1111i :
   pass
  else :
   OOiIiIIi1 ( 'DJing  ' + I1111i , oO0o0 , 90025 , 'http://www.djing.com' + o00O0O , O0o0Oo , '' )
  I1I11i ( 'movies' , 'MAIN' )
def oOOoooO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 if 22 - 22: ooOOOoO + iI11I1II1I1I
 i1IIIII11I1IiI = re . compile ( "file: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def IIIii1iiIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 63 - 63: Ii1I
def o0o0O ( ) :
 if 6 - 6: I11i1ii1 / Ii1I
 if 57 - 57: ooOOOoO
 if 67 - 67: oO0o . I11i1ii1
 if 87 - 87: o000O0o % ii1ii11IIIiiI
 if 83 - 83: IIiIiII11i - ooOOOoO
 if 35 - 35: ooOoO0O00 - iI11I1II1I1I + ooOoO0O00
 oO0OOoo0OO = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'yr' in oO0o0 :
   OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + oO0o0 , 10201 , III1iII1I1ii + 'rated.png' )
   if 86 - 86: iI11I1II1I1I + OOooOOo . Ii - ii1ii11IIIiiI
def ooO000O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOIII111iiIi1 , url , I1111i in i1IIIII11I1IiI :
  if 'id' in url :
   OOo ( ( '[COLORred]RANK [COLORblue]' + oOIII111iiIi1 + '[COLORred] - [COLORblue]' + I1111i + '[/COLOR]' ) , I1111i , 10202 , III1iII1I1ii + 'rated.png' )
   if 29 - 29: ii + ii1ii11IIIiiI % iI11I1II1I1I - Ii1IIIi1 . oOo0O0Ooo % I1ii11iIi11i
def I1IIi ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 O0OOOo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ii1I = ( url )
 o0OOoOoO00 = ii1I . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( ii1I ) . replace ( ' ' , '+' )
 i111iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 i11I1I1iiI = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 I1i1iii1Ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 O0O00OOo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OoOOo = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + ii1I
 iii1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 oOO0oo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 29 - 29: oOo0O0Ooo * IIiIiII11i * ii - Ii1I * IIiIiII11i
 iiO00O00O000OOO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 iIOo0O = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 1 - 1: o0o00Oo0O / O0OOOoOoo0 % iiiiiiii1 . I1ii11iIi11i + I1111IIi
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( i111iI )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( i11I1I1iiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( I1i1iii1Ii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 I1Ii11iiiI = O0o0O00Oo0o0 ( iI )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1II1IiIII111 = O0o0O00Oo0o0 ( OoOOo )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 IiiIi1IIII1i = O0o0O00Oo0o0 ( iii1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0ooOoO = O0o0O00Oo0o0 ( oOO0oo )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 26 - 26: OOooOOo / I1ii11iIi11i - ooOoO0O00 + ooOOOoO
 if 38 - 38: ii / Ii1I . o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
 ooO00O00oOO = O0o0O00Oo0o0 ( iiO00O00O000OOO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 I1 = O0o0O00Oo0o0 ( iIOo0O )
 if 48 - 48: oOo0O0Ooo + Ii1I + IIiIiII11i * Ii
 if 13 - 13: ii * o000O0o - ii1ii11IIIiiI / Ii1IIIi1 + ooOOOoO + I1111IIi
 if 39 - 39: iI11I1II1I1I - ii
 if 81 - 81: Ii1I - o0o00Oo0O * ii
 if 23 - 23: IIiIiII11i / o000O0o
 if 28 - 28: I1ii11iIi11i * I11i1ii1 - oO0o
 if 19 - 19: ooOOOoO
 if 67 - 67: o0o00Oo0O % iI11I1II1I1I / I1111IIi . Ii - ii1ii11IIIiiI + o0o00Oo0O
 if 27 - 27: Ii1IIIi1
 if 89 - 89: IIiIiII11i / o000O0o
 if 14 - 14: Ii1IIIi1 . oOo0O0Ooo * I11i1ii1 + IIiIiII11i - I11i1ii1 + Ii1IIIi1
 if 18 - 18: o000O0o - I11i - oOo0O0Ooo - oOo0O0Ooo
 if 54 - 54: I1ii11iIi11i + oOo0O0Ooo / O0OOOoOoo0 . oOo0O0Ooo * OOooOOo
 if O0ooOoO != 'Failed' :
  IIiIiiiIIIIi1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0ooOoO )
  for url , I1111i in IIiIiiiIIIIi1 :
   iIi11 = O0o0O00Oo0o0 ( url )
   O00O0 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi11 )
   for iIiIiiiIi , i1iiIIi11I in O00O0 :
    i1iiIIi11I = ( i1iiIIi11I . replace ( '.' , ' ' ) )
    if o0OOoOoO00 in i1iiIIi11I . lower ( ) :
     if '.mkv' in iIiIiiiIi :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiIiiiIi , 222 , '' , '' , '' )
     elif '.mp4' in iIiIiiiIi :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiIiiiIi , 222 , '' , '' , '' )
     elif '.avi' in iIiIiiiIi :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiIiiiIi , 222 , '' , '' , '' )
     elif '.wav' in iIiIiiiIi :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiIiiiIi , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiIiiiIi , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 80 - 80: I11i1ii1 * o0o00Oo0O
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for url , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in i1I :
   if ii1I in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 78 - 78: OOooOOo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 20 - 20: O0OOOoOoo0 % ii1ii11IIIiiI . ii1ii11IIIiiI / ooOOOoO + OOooOOo . ii1ii11IIIiiI
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for O0ooOo0 , I1111i in ooOoO00 :
   if ii1I in I1111i . lower ( ) :
    OOo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i11I1I1iiI + O0ooOo0 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for url , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in Iii1I1111ii :
   if ii1I in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 53 - 53: ii - I1111IIi
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if I1Ii11iiiI != 'Failed' :
  oOo = [ ]
  Oo0000O0OOooO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1Ii11iiiI )
  for url , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in Oo0000O0OOooO :
   if ii1I in I1111i . lower ( ) :
    if I1111i in oOo :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
     oOo . append ( I1111i )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if i1II1IiIII111 != 'Failed' :
  i1iIIIiiiI = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1II1IiIII111 )
  for url , o00O0O , I1111i in i1iIIIiiiI :
   if ii1I in I1111i . lower ( ) :
    OOo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 94 - 94: o0o00Oo0O - ooOOOoO - iI11I1II1I1I % I11i1ii1 / ii1ii11IIIiiI % O0OOOoOoo0
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 44 - 44: I1ii11iIi11i % iI11I1II1I1I
    if 90 - 90: IIiIiII11i + ii % ii
    if 35 - 35: O0OOOoOoo0 / Ii1I * ii . IIiIiII11i / I1ii11iIi11i
    if 1 - 1: ii + I1111IIi . ooOoO0O00 % ooOOOoO
    if 66 - 66: I11i + Ii1I + oOo0O0Ooo - o000O0o
    if 12 - 12: O0OOOoOoo0 . I1111IIi . OOooOOo / o0o00Oo0O
    if 58 - 58: I11i - IIiIiII11i % o000O0o + iiiiiiii1 . OOooOOo / I1111IIi
    if 8 - 8: Ii1I . oO0o * ooOOOoO + IIiIiII11i % Ii
    if 8 - 8: I11i1ii1 * o0o00Oo0O
    if 73 - 73: I11i / o000O0o / ooOOOoO / oO0o
    if 11 - 11: OOooOOo + I1111IIi - ii / oO0o
    if 34 - 34: I11i1ii1
    if 45 - 45: I11i1ii1 / I1ii11iIi11i / ii1ii11IIIiiI
    if 44 - 44: Ii1I - ii1ii11IIIiiI / IIiIiII11i * oO0o * I1ii11iIi11i
    if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * Ii1IIIi1 % IIiIiII11i
    if 56 - 56: ii * I1ii11iIi11i . I1ii11iIi11i . Ii1I
    if 24 - 24: I1ii11iIi11i . ooOOOoO * ii1ii11IIIiiI % O0OOOoOoo0 / Ii1IIIi1
    if 58 - 58: oOo0O0Ooo - Ii1I % o0o00Oo0O . oOo0O0Ooo % oO0o % I1111IIi
 if ooO00O00oOO != 'Failed' :
  oOo0OooOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO00O00oOO )
  for url , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in oOo0OooOo :
   if ii1I in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 51 - 51: ooOOOoO . I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: ooOoO0O00 - I1ii11iIi11i / o0o00Oo0O . Ii1I
    if 5 - 5: I11i . iI11I1II1I1I % iI11I1II1I1I
    if 56 - 56: ii - ooOOOoO - ooOoO0O00
    if 8 - 8: iiiiiiii1 / Ii1IIIi1 . oOo0O0Ooo + Ii1I / Ii
    if 31 - 31: I11i1ii1 - iI11I1II1I1I + O0OOOoOoo0 . I1ii11iIi11i / I1111IIi % iI11I1II1I1I
    if 6 - 6: I1111IIi * Ii % iI11I1II1I1I % Ii + I11i / ooOoO0O00
    if 53 - 53: ooOOOoO + iI11I1II1I1I
    if 70 - 70: Ii1I
    if 67 - 67: ii
    if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + Ii1IIIi1 * I1111IIi
 IiI1ii1Ii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 51 - 51: Ii * I11i / oOo0O0Ooo
 for I1iii in IiI1ii1Ii :
  oOO0OO0O = O0Oo000ooO00 + I1iii + I1IIIii
  O0ooOoO = O0o0O00Oo0o0 ( oOO0OO0O )
  if O0ooOoO != 'Failed' :
   IIiIiiiIIIIi1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0ooOoO )
   for url , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in IIiIiiiIIIIi1 :
    if ii1I in I1111i . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 40 - 40: oOo0O0Ooo
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 36 - 36: I11i1ii1 / O0OOOoOoo0 - I1111IIi - I1111IIi
 IiI1ii1Ii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 82 - 82: Ii1I
 if 29 - 29: I1111IIi
 for I1iii in IiI1ii1Ii :
  oOO0OO0O = O0OOOo + I1iii
  o0OOoo = O0o0O00Oo0o0 ( oOO0OO0O )
  if o0OOoo != 'Failed' :
   IiIiiI11i1Ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( o0OOoo )
   for O0ooOo0 , I1111i in IiIiiI11i1Ii :
    if ii1I in I1111i . lower ( ) :
     i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O0OOOo + I1iii + O0ooOo0 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 100 - 100: iiiiiiii1 . oOo0O0Ooo * iiiiiiii1 - oOo0O0Ooo . ooOOOoO * ii1ii11IIIiiI
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: oO0o + I1111IIi * iiiiiiii1
def IIiI1 ( ) :
 OOo ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , III1iII1I1ii + 'running.png' )
 OOo ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , III1iII1I1ii + 'countdown.png' )
 OOo ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , III1iII1I1ii + 'unknown.png' )
 OOo ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , III1iII1I1ii + 'cancelled.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 28 - 28: ii . o000O0o % Ii1I / ooOoO0O00 / Ii1IIIi1
def III1I1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , OoOOOo0o0ooo , i1i111i1 , I1iI1I1I1i11i , OoOoOo0 in i1IIIII11I1IiI :
  OOo ( ( '[COLORblue]' + I1111i + '[/COLOR] [COLORred]Season[/COLOR]-' + OoOOOo0o0ooo + ' [COLORred]Returns [/COLOR]- ' + OoOoOo0 + ' ' + I1iI1I1I1i11i ) , I1111i , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 39 - 39: ooOOOoO - Ii1I
def OOO0o0OO0OO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , OoOOOo0o0ooo , i1i111i1 in i1IIIII11I1IiI :
  OOo ( ( '[COLORblue]' + I1111i + '[/COLOR] [COLORred]Season[/COLOR]-' + OoOOOo0o0ooo + ' [COLORred] Status Unknown[/COLOR] ' ) , I1111i , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 64 - 64: IIiIiII11i
def iIIIiIi1I1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , OoOOOo0o0ooo , i1i111i1 , I1iI1I1I1i11i in i1IIIII11I1IiI :
  OOo ( ( '[COLORblue]' + I1111i + ' [COLORred] Cancelled On[/COLOR] ' + I1iI1I1I1i11i ) , I1111i , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 78 - 78: iI11I1II1I1I % OOooOOo + Ii1I / ooOoO0O00 % IIiIiII11i + Ii1IIIi1
def OooOOOO0O0 ( url ) :
 ii1I = ( url )
 o0OOoOoO00 = ii1I . lower ( )
 if 38 - 38: iiiiiiii1 % Ii1IIIi1 - ii
 if 87 - 87: oO0o % oOo0O0Ooo
 iIiIiiiIi = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( ii1I ) . replace ( ' ' , '+' )
 i111iI = 'http://onlinemovies.tube/?s=' + ( ii1I ) . replace ( ' ' , '+' )
 i11I1I1iiI = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 I1i1iii1Ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 O0O00OOo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 77 - 77: iI11I1II1I1I - ooOoO0O00 . o000O0o
 iii1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 oOO0oo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 iIi1iIIIiIiI = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 62 - 62: Ii % Ii1IIIi1 . I1111IIi . Ii1IIIi1
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 84 - 84: Ii * oO0o
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 18 - 18: Ii1IIIi1 - ii1ii11IIIiiI - OOooOOo / iiiiiiii1 - o0o00Oo0O
 if 30 - 30: o0o00Oo0O + Ii1I + IIiIiII11i
 III1I = O0o0O00Oo0o0 ( iIiIiiiIi )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( i111iI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( i11I1I1iiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( I1i1iii1Ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 o0OOoo = O0o0O00Oo0o0 ( O0O00OOo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 11 - 11: I11i1ii1 - Ii1IIIi1 + I11i1ii1 * o000O0o / oOo0O0Ooo
 if 53 - 53: iI11I1II1I1I + I11i - OOooOOo - o000O0o / I11i1ii1 % Ii
 IiiIi1IIII1i = O0o0O00Oo0o0 ( iii1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 O0ooOoO = O0o0O00Oo0o0 ( oOO0oo )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 I11oOOooo = O0o0O00Oo0o0 ( iIi1iIIIiIiI )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 80 - 80: oOo0O0Ooo - Ii
 if O0ooOoO != 'Failed' :
  IIiIiiiIIIIi1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0ooOoO )
  for url , I1111i in IIiIiiiIIIIi1 :
   iIi11 = O0o0O00Oo0o0 ( url )
   O00O0 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi11 )
   for iIiIiiiIi , i1iiIIi11I in O00O0 :
    if o0OOoOoO00 in i1iiIIi11I . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + iIiIiiiIi , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 69 - 69: o000O0o % ii . oOo0O0Ooo
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if IiiIi1IIII1i != 'Failed' :
  I1III1II1I11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiIi1IIII1i )
  for url , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in I1III1II1I11 :
   if o0OOoOoO00 in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 30 - 30: I11i / Ii1IIIi1 / I1111IIi % I11i1ii1 + IIiIiII11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 4 - 4: O0OOOoOoo0 - I1ii11iIi11i - I1111IIi - ooOOOoO % Ii / oO0o
    if 50 - 50: I11i1ii1 + ooOoO0O00
    if 31 - 31: ii1ii11IIIiiI
    if 78 - 78: Ii + I11i + iiiiiiii1 / I11i % iI11I1II1I1I % I1111IIi
    if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % iiiiiiii1 . Ii1I % o0o00Oo0O
    if 47 - 47: I11i
    if 66 - 66: oOo0O0Ooo - I1111IIi
    if 33 - 33: oOo0O0Ooo / oO0o
    if 12 - 12: IIiIiII11i
    if 2 - 2: ooOoO0O00 - oOo0O0Ooo + ooOOOoO . IIiIiII11i
    if 25 - 25: o000O0o
 if I11oOOooo != 'Failed' :
  iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11oOOooo )
  for url , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in iI1 :
   if o0OOoOoO00 in I1111i . lower ( ) :
    OOo ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , OOoOooOoOOOoo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 11 - 11: oO0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  I11Ii111I = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for url , o00O0O , I1111i , Oo00OO0 in i1I :
   if o0OOoOoO00 in I1111i . lower ( ) :
    if 'season' in Oo00OO0 :
     OOo ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , o00O0O , o00O0O , '' )
    if 'episodes' in Oo00OO0 :
     OOo ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , o00O0O , o00O0O , '' )
  for url in I11Ii111I :
   OOo ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 72 - 72: ooOoO0O00 / o000O0o * iiiiiiii1
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if III1I != 'Failed' :
  IIIIIiI = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( III1I )
  for url , I1111i , o00O0O in IIIIIiI :
   if o0OOoOoO00 in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 40 - 40: ii1ii11IIIiiI - OOooOOo * OOooOOo . OOooOOo + ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 77 - 77: iI11I1II1I1I . ii1ii11IIIiiI % o000O0o / ii1ii11IIIiiI
    if 54 - 54: o000O0o + I11i1ii1 - I1ii11iIi11i
    if 35 - 35: ii1ii11IIIiiI - ii1ii11IIIiiI + ooOoO0O00 - o0o00Oo0O - iiiiiiii1
    if 58 - 58: OOooOOo - O0OOOoOoo0 - ii
    if 96 - 96: iI11I1II1I1I
    if 82 - 82: OOooOOo + o0o00Oo0O - I1111IIi % o000O0o * Ii
    if 15 - 15: I11i
    if 39 - 39: Ii1IIIi1 / Ii1I / oOo0O0Ooo * iiiiiiii1
    if 44 - 44: o0o00Oo0O + I11i1ii1 . iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - ooOOOoO
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for I1111i in ooOoO00 :
   if o0OOoOoO00 in I1111i . lower ( ) :
    OOo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( i11I1I1iiI + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 83 - 83: I1111IIi * ooOOOoO / I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for I1111i in Iii1I1111ii :
   if o0OOoOoO00 in I1111i . lower ( ) :
    OOo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( I1i1iii1Ii + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 32 - 32: I11i + OOooOOo - ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if o0OOoo != 'Failed' :
  IiIiiI11i1Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OOoo )
  for url , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in IiIiiI11i1Ii :
   if o0OOoOoO00 in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 39 - 39: ii * Ii1IIIi1 * o0o00Oo0O . ooOOOoO . oO0o + I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 9 - 9: OOooOOo + o000O0o % ii + I11i
 ooOO0o = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for I1iii in ooOO0o :
  oOO0OO0O = O0Oo000ooO00 + I1iii + I1IIIii
  ooO00O00oOO = O0o0O00Oo0o0 ( oOO0OO0O )
  if ooO00O00oOO != 'Failed' :
   oOo0OooOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( ooO00O00oOO )
   for I1111i , Iio00 , url , o00O0O , o0ooooO0o0O , i1i1iII1 in oOo0OooOo :
    if o0OOoOoO00 in I1111i . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , url , i1i1iII1 , o00O0O , o0ooooO0o0O , Iio00 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 51 - 51: I1ii11iIi11i - Ii1I * ooOOOoO
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 12 - 12: iI11I1II1I1I % I11i1ii1 % I11i1ii1
     if 78 - 78: I1111IIi . OOooOOo . ooOOOoO
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 97 - 97: o000O0o
def I1ii11 ( ) :
 if 80 - 80: oOo0O0Ooo . ii1ii11IIIiiI
 if 47 - 47: ooOOOoO + I11i1ii1 + IIiIiII11i % Ii
 if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / O0OOOoOoo0 * o000O0o
 if 29 - 29: I11i
 if 86 - 86: IIiIiII11i . I1111IIi
 if 2 - 2: ii
 if 60 - 60: oO0o
 if 81 - 81: OOooOOo % ii1ii11IIIiiI
 if 87 - 87: iI11I1II1I1I . ii * OOooOOo
 if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % ii1ii11IIIiiI - iI11I1II1I1I
 if 17 - 17: ooOOOoO / I11i % I1ii11iIi11i
 OOo ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , III1iII1I1ii + 'seasons.png' )
 OOo ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , III1iII1I1ii + 'episodes.png' )
 OOo ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 71 - 71: I1111IIi . iiiiiiii1 . oO0o
def Oo0O0O00Oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , I111Ii in i1IIIII11I1IiI :
  OOo ( ( I1111i + ' - ' + I111Ii ) . replace ( '&amp;' , '&' ) , url , 90053 , III1iII1I1ii + 'seasons.png' )
  if 34 - 34: I11i / O0OOOoOoo0 % o0o00Oo0O . oO0o . ooOoO0O00
def iiO0O0o0oO0O00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , url , 90054 , III1iII1I1ii + 'episodes.png' )
  if 70 - 70: iiiiiiii1 + o000O0o
def o00ooo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  OOo ( I1111i , url , 90054 , o00O0O )
 for url in next :
  OOo ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 39 - 39: I11i1ii1 . IIiIiII11i
def iIiIi1iI11iiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for o00O0O , I111Ii , url , I1111i , iiI1Ii11II1I in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I111Ii + ' - ' + I1111i + ' - ' + iiI1Ii11II1I , url , 90044 , o00O0O , o00O0O , '' )
 for o00O0O , I1111i , url in i1I :
  OOo ( I1111i , url , 90044 , o00O0O , o00O0O , '' )
 for url in next :
  OOo ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 44 - 44: ii1ii11IIIiiI % Ii - O0OOOoOoo0 * Ii1I + I1ii11iIi11i * Ii1IIIi1
def IiI1iI1IiiIi1 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO0oo = 'http://onlinemovies.tube/?s=' + ( ii1I ) . replace ( ' ' , '+' )
 o0OOoOoO00 = OoO0oo . lower ( )
 oO0OOoo0OO = OoOooO ( o0OOoOoO00 )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i , Oo00OO0 in i1IIIII11I1IiI :
  if 'season' in Oo00OO0 :
   OOo ( I1111i , oO0o0 , 90054 , o00O0O , o00O0O , '' )
  if 'episodes' in Oo00OO0 :
   OOo ( I1111i , oO0o0 , 90044 , o00O0O , o00O0O , '' )
 for oO0o0 in next :
  OOo ( 'NEXT' , oO0o0 , 90053 , III1iII1I1ii + 'Next.png' )
  if 72 - 72: o0o00Oo0O + oOo0O0Ooo - O0OOOoOoo0 - oO0o
def ooooO0oOoOOoO ( ) :
 if 100 - 100: o0o00Oo0O
 if 79 - 79: iI11I1II1I1I
 if 81 - 81: Ii1IIIi1 + iI11I1II1I1I * iiiiiiii1 - iI11I1II1I1I . Ii1IIIi1
 if 48 - 48: ooOOOoO . ii . oOo0O0Ooo . OOooOOo % Ii1I / O0OOOoOoo0
 if 11 - 11: ooOoO0O00 % oO0o % O0OOOoOoo0
 if 99 - 99: I11i1ii1 / iI11I1II1I1I - ii1ii11IIIiiI * Ii1I % oOo0O0Ooo
 if 13 - 13: oO0o
 if 70 - 70: iiiiiiii1 + o0o00Oo0O . o000O0o * ii1ii11IIIiiI
 if 2 - 2: ii . Ii1IIIi1 . I1111IIi
 if 42 - 42: Ii1IIIi1 % o000O0o / oO0o - o000O0o * Ii
 OOo ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , III1iII1I1ii + 'allmov.png' )
 OOo ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , III1iII1I1ii + 'Genre.png' )
 OOo ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , III1iII1I1ii + 'Years.png' )
 OOo ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 19 - 19: o000O0o * oOo0O0Ooo % Ii
def iiI1Ii1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , I111Ii in i1IIIII11I1IiI :
  if 'genre' in url :
   OOo ( ( I1111i + ' - ' + I111Ii ) . replace ( '&amp;' , '&' ) , url , 90043 , III1iII1I1ii + 'Genre.png' )
   if 28 - 28: Ii1IIIi1 % I11i1ii1
def iiIiII11i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if 'release' in url :
   OOo ( I1111i , url , 90043 , III1iII1I1ii + 'Years.png' )
   if 93 - 93: OOooOOo % iI11I1II1I1I
def Ooo0o0oo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , oOO0 , url , Iio00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' ' + oOO0 , url , 90044 , o00O0O , o00O0O , Iio00 )
 for o00O0O , I1111i , Oo00OO0 , url , IIi1I1i , Iio00 in i1I :
  if 'movies' in Oo00OO0 :
   iiOOooooO0Oo ( I1111i + ' - ' + IIi1I1i , url , 90044 , o00O0O , o00O0O , Iio00 )
 for url in next :
  OOo ( 'NEXT' , url , 90043 , III1iII1I1ii + 'Next.png' )
  if 13 - 13: iI11I1II1I1I . OOooOOo * oOo0O0Ooo / o000O0o * ii1ii11IIIiiI
def O00o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  oO0o00ooO0OoO ( 'http:' + url )
  if 1 - 1: OOooOOo . Ii % OOooOOo - O0OOOoOoo0 % ooOoO0O00 + Ii1I
def oO0o00ooO0OoO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( I1111i ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , III1iII1I1ii + 'movhub.png' )
def IiiIiIi111iI1 ( ) :
 if 88 - 88: I1ii11iIi11i % o000O0o + I1111IIi
 if 8 - 8: Ii / IIiIiII11i + I11i * ii1ii11IIIiiI % I1111IIi . ooOOOoO
 if 6 - 6: I1111IIi % I1ii11iIi11i . I1ii11iIi11i - Ii1I / ooOOOoO . ooOoO0O00
 if 99 - 99: OOooOOo . iiiiiiii1
 if 59 - 59: ooOOOoO / I1ii11iIi11i / Ii1IIIi1 / o0o00Oo0O / OOooOOo + I11i
 if 13 - 13: I11i % o000O0o / iiiiiiii1 % iiiiiiii1 % o0o00Oo0O
 if 90 - 90: I1111IIi . I11i1ii1 / iI11I1II1I1I
 if 28 - 28: I1111IIi + o000O0o - I11i1ii1 / iI11I1II1I1I - oOo0O0Ooo
 if 45 - 45: o0o00Oo0O / ooOoO0O00 * o000O0o * oO0o
 if 35 - 35: Ii1I / O0OOOoOoo0 % oOo0O0Ooo + iI11I1II1I1I
 if 79 - 79: OOooOOo / I11i1ii1
 if 77 - 77: I1ii11iIi11i
 if 46 - 46: iiiiiiii1
 if 72 - 72: O0OOOoOoo0 * Ii1IIIi1
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO0oo = 'http://onlinemovies.tube/?s=' + ( ii1I ) . replace ( ' ' , '+' )
 o0OOoOoO00 = OoO0oo . lower ( )
 oO0OOoo0OO = OoOooO ( o0OOoOoO00 )
 i1IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i , oooo in i1IIIII11I1IiI :
  if 'movies' in oooo :
   OOo ( oooo + '-' + I1111i , oO0o0 , 90044 , o00O0O )
 for oO0o0 in next :
  Ooo0o0oo0 ( oO0o0 )
  if 27 - 27: Ii - oOo0O0Ooo
def IiIi ( ) :
 OOo ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 oO0OOoo0OO = OoOooO ( 'http://www.join4films.com/' )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , oO0o0 , 80006 , III1iII1I1ii + 'Desi.png' )
def iii1IIiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oO0OOoo0OO )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( I1111i , url , 80007 , o00O0O )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  OOo ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def i1i1Ii11Ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  OOOOo0o00OO0000 ( url )
def O000oOo ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO0oo = 'http://www.join4films.com/?s=' + ( ii1I ) . replace ( ' ' , '+' ) + '&search_type=1'
 o0OOoOoO00 = OoO0oo . lower ( )
 iii1IIiI ( o0OOoOoO00 )
 if 41 - 41: o0o00Oo0O + o000O0o . ooOoO0O00 - IIiIiII11i * I11i . oO0o
 if 68 - 68: I11i
 if 20 - 20: iiiiiiii1 - iiiiiiii1
 if 37 - 37: I1111IIi
 if 37 - 37: I1ii11iIi11i / I1111IIi * o0o00Oo0O
 if 73 - 73: O0OOOoOoo0 * O0OOOoOoo0 / I11i1ii1
 if 43 - 43: Ii1I . ooOoO0O00 . I1111IIi + o0o00Oo0O * ii1ii11IIIiiI * o0o00Oo0O
 if 41 - 41: Ii1I + ii1ii11IIIiiI % ii . Ii1I + O0OOOoOoo0 . O0OOOoOoo0
 if 31 - 31: Ii + IIiIiII11i . O0OOOoOoo0 * OOooOOo
 if 66 - 66: OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
 if 87 - 87: Ii1IIIi1 + I11i . O0OOOoOoo0 - ii
 if 6 - 6: iI11I1II1I1I * ii
 if 28 - 28: I1ii11iIi11i * I11i / iiiiiiii1
 if 52 - 52: o0o00Oo0O / I11i % O0OOOoOoo0 * oOo0O0Ooo % Ii1IIIi1
 if 69 - 69: Ii1I
 if 83 - 83: I11i
 if 38 - 38: iiiiiiii1 + ii . ooOoO0O00
def I1III1iIi ( ) :
 iiOOooooO0Oo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 if 82 - 82: oOo0O0Ooo + O0OOOoOoo0 + Ii1I * oOo0O0Ooo % Ii % O0OOOoOoo0
def Iiii1i11ii1Ii ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO0oo = 'http://imoviemax.se/?s=' + ( ii1I ) . replace ( ' ' , '+' )
 o0OOoOoO00 = OoO0oo . lower ( )
 i1Oo0oOo000OoO0 ( o0OOoOoO00 )
def IIi ( url ) :
 i1I1i = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , IIII1iIIii in i1IIIII11I1IiI :
  if I1111i in i1I1i :
   pass
  else :
   iiOOooooO0Oo ( I1111i + ' - ' + IIII1iIIii + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
   i1I1i . append ( I1111i )
   if 12 - 12: iI11I1II1I1I . ii1ii11IIIiiI . Ii1I % oOo0O0Ooo . IIiIiII11i . o000O0o
def IIi1ii1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , I1Ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' - Views:' + I1Ii , url , 10075 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
  if 44 - 44: iI11I1II1I1I . Ii1I + iiiiiiii1 . I11i1ii1
  if 7 - 7: Ii1I + iI11I1II1I1I * ooOOOoO * ooOOOoO / IIiIiII11i - ii1ii11IIIiiI
def i1Oo0oOo000OoO0 ( url ) :
 oOOOo0o = [ ]
 oO0OOoo0OO = OoOooO ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0OOoo0OO )
 for next in next :
  iiOOooooO0Oo ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10075 , o00O0O , o00O0O , '' )
  oOOOo0o . append ( I1111i )
  if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
def O0oOoo ( img , name , url ) :
 img = img
 name = name
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oO0OOoo0OO )
 for OoOOoO0O0oO , url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  oOOoO = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + oOOoO
  oOo0Oo0O0O = ( OoOOoO0O0oO ) . replace ( 'play-' , 'Server ' )
  OOiIiIIi1 ( oOo0Oo0O0O , oOOoO , 10076 , img , img , '' )
  if 48 - 48: I1ii11iIi11i - I11i1ii1 + I1ii11iIi11i - oOo0O0Ooo * Ii . O0OOOoOoo0
def I1iIIIiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oO0OOoo0OO )
 for i111iI in i1IIIII11I1IiI :
  if '=m' in i111iI :
   Oo ( i111iI )
  elif 'php' in i111iI :
   I1iIIIiI ( url )
  else :
   oO0OOoo0OO = OoOooO ( i111iI )
   i1IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( oO0OOoo0OO )
   for i11I1I1iiI in i1IIIII11I1IiI :
    Oo ( i111iI )
    if 34 - 34: oOo0O0Ooo
    if 47 - 47: iiiiiiii1 - Ii1IIIi1 / I11i1ii1 - I1ii11iIi11i + O0OOOoOoo0 - iI11I1II1I1I
    if 68 - 68: ii1ii11IIIiiI - o000O0o + I1ii11iIi11i
def i11Iii1Ii1i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1iIi1IIiIII1 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iI1I1I1i11i , i1Ii11I1II in i1iIi1IIiIII1 :
  print 'there ><><><><><><><><><><><><'
  I1iI1I1I1i11i = I1iI1I1I1i11i
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1Ii11I1II ) )
  for I1111i , oOOOoo0o in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + I1iI1I1I1i11i + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + oOOOoo0o + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
 iIi1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iI1I1I1i11i , iiiI1IiIIii in iIi1 :
  print 'there ><><><><><><><><><><><><'
  I1iI1I1I1i11i = I1iI1I1I1i11i
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iiiI1IiIIii ) )
  for I1111i , oOOOoo0o in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + I1iI1I1I1i11i + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + oOOOoo0o + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
   if 25 - 25: Ii1I + o000O0o + ii . IIiIiII11i . O0OOOoOoo0
   if 66 - 66: I11i1ii1 * OOooOOo
   if 2 - 2: o000O0o . iiiiiiii1 * I1ii11iIi11i + o0o00Oo0O - ooOOOoO * iI11I1II1I1I
def ii1I1IiiI1ii1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iIi1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIi1 in iIi1 :
  I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iIi1 ) )
  for I1111i in I1111i :
   I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iIi1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iii11i1IIII = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iIi1 ) )
  for iii11i1IIII in iii11i1IIII :
   iii11i1IIII = 'http:' + iii11i1IIII
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iii11i1IIII , '' , '' )
  if 12 - 12: I11i * iiiiiiii1 % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
  if 81 - 81: I1ii11iIi11i - ooOOOoO
  if 24 - 24: ii . oO0o * IIiIiII11i
  if 59 - 59: iiiiiiii1 + oO0o / Ii1IIIi1
def OOOOO0O00 ( url ) :
 if 97 - 97: I1ii11iIi11i * O0OOOoOoo0 % I11i1ii1 . O0OOOoOoo0 - iiiiiiii1 - Ii1IIIi1
 oo0O0o00 = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i111iI , o00O0O , I1111i , I1ii1i in i1IIIII11I1IiI :
  I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = OoOooO ( i111iI )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for oOOo0OOOOo0Oo , o0ooO in i1I :
   II11Ii111II1 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( o0ooO ) )
   for Iio00 in II11Ii111II1 :
    if I1111i in oo0O0o00 :
     pass
    else :
     OOiIiIIi1 ( I1111i , oOOo0OOOOo0Oo , 8043 , o00O0O , o00O0O , Iio00 )
     I1I11i ( 'movies' , 'INFO' )
     oo0O0o00 . append ( I1111i )
     if 72 - 72: O0OOOoOoo0 % I11i % o000O0o + ooOOOoO % Ii + o0o00Oo0O
     if 65 - 65: iI11I1II1I1I % o000O0o + o0o00Oo0O / ii
def O0000oO0o00 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , OOoOooOoOOOoo , Iio00 , o0ooooO0o0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10065 , OOoOooOoOOOoo , o0ooooO0o0O , Iio00 )
 I1I11i ( 'movies' , 'INFO' )
 if 80 - 80: ii + I1111IIi
def O00O ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO0oo = 'https://www.youtube.com/results?search_query=' + ( ii1I ) . replace ( ' ' , '+' )
 o0OOoOoO00 = OoO0oo . lower ( )
 oO0OOoo0OO = OoOooO ( o0OOoOoO00 )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 in next :
  oO0o0 = 'https://www.youtube.com' + oO0o0
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , oO0o0 , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for o00O0O , oO0o0 , I1111i , Oo0oOOooO0o0O , o0ooO in i1IIIII11I1IiI :
  OOOO . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  iii11i1IIII = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iii11i1IIII
  oO0o0 = 'http://www.youtube.com' + oO0o0
  OOiIiIIi1 ( '[COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iii11i1IIII , iii11i1IIII , o0ooO )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o00O0O , oO0o0 , I1111i , Oo0oOOooO0o0O in i1IIIII11I1IiI :
   print 'im doing it'
   I1I11i ( 'tvshows' , 'INFO' )
   iii11i1IIII = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   oO0o0 = 'http://www.youtube.com' + oO0o0
   if '&' in oO0o0 :
    print ' i got here'
    oO0OOoo0OO = OoOooO ( oO0o0 )
    iIi1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for iIi1 in iIi1 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iIi1 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oO0o0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iIi1 ) )
     for oO0o0 in oO0o0 :
      oO0o0 = 'https://www.youtube.com/w' + oO0o0
     iii11i1IIII = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iIi1 ) )
     for iii11i1IIII in iii11i1IIII :
      iii11i1IIII = 'http:' + iii11i1IIII
     OOiIiIIi1 ( '[COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iii11i1IIII , O0o0Oo , '' )
   elif I1111i in OOOO :
    pass
   elif 'user' in oO0o0 or 'elete' in I1111i :
    pass
   elif 'hannel' in oO0o0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oO0o0
    oO0OOoo0OO = OoOooO ( oO0o0 )
    oo0o00oOo0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for o00O0O , oO0o0 , I1111i in oo0o00oOo0 :
     if 'outube' in oO0o0 or 'list' in oO0o0 :
      pass
     elif 'atch' in oO0o0 :
      oO0o0 = ( oO0o0 ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iii11i1IIII , iii11i1IIII , '' )
    if 61 - 61: Ii1IIIi1 / oO0o + IIiIiII11i . o000O0o / I1ii11iIi11i * Ii1IIIi1
def ii1O0ooooo000 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for o00O0O , url , I1111i , Oo0oOOooO0o0O , o0ooO in i1IIIII11I1IiI :
  OOOO . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  iii11i1IIII = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iii11i1IIII
  url = 'http://www.youtube.com' + url
  OOiIiIIi1 ( '[COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iii11i1IIII , iii11i1IIII , o0ooO )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o00O0O , url , I1111i , Oo0oOOooO0o0O in i1IIIII11I1IiI :
   I1I11i ( 'tvshows' , 'INFO' )
   iii11i1IIII = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oO0OOoo0OO = OoOooO ( url )
    iIi1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for iIi1 in iIi1 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iIi1 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iIi1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     iii11i1IIII = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iIi1 ) )
     for iii11i1IIII in iii11i1IIII :
      iii11i1IIII = 'http:' + iii11i1IIII
     OOiIiIIi1 ( '[COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iii11i1IIII , O0o0Oo , '' )
   elif I1111i in OOOO :
    pass
   elif 'user' in url or 'elete' in I1111i :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0OOoo0OO = OoOooO ( url )
    oo0o00oOo0 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for o00O0O , url , I1111i in oo0o00oOo0 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iii11i1IIII , iii11i1IIII , '' )
    if 97 - 97: Ii % o000O0o / I1ii11iIi11i / I1ii11iIi11i
    if 97 - 97: IIiIiII11i - iiiiiiii1 - iI11I1II1I1I * oOo0O0Ooo
def ooO ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  oooO0o0O0oo0o ( )
  O0Oooo = open ( i1I1iI )
  i1IIIII11I1IiI = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( O0Oooo ) )
  for I11iI1I , Iii1iiIi1II1 in i1IIIII11I1IiI :
   if I11iI1I == 'needs replacing' or Iii1iiIi1II1 == 'needs replacing' :
    Oo000oOO00oo ( )
    if 84 - 84: I11i1ii1 + Ii - Ii1IIIi1 * I11i1ii1
  iiOOooooO0Oo ( '[COLOR' + II + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o , 60004 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
def oooO0o0O0oo0o ( ) :
 i1i = OoOooO ( 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 for oO0o0 in i1IIIII11I1IiI :
  I1IiiIiii1 = datetime . fromtimestamp ( float ( i1IIIII11I1IiI [ 0 ] ) )
  I1IiiIiii1 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= I1IiiIiii1 <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   OOooO0OOoo . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + II + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + II + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + II + '] To Purchase A licence[/COLOR]' )
def i11i ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"username":"(.+?)"' ) . findall ( i1i )
 oo0OoOO0o0o = re . compile ( '"password":"(.+?)"' ) . findall ( i1i )
 IIIIIiI = re . compile ( '"status":"(.+?)"' ) . findall ( i1i )
 i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 ooOoO00 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( i1i )
 Iii1I1111ii = re . compile ( '"created_at":"(.+?)"' ) . findall ( i1i )
 Oo0000O0OOooO = re . compile ( '"max_connections":"(.+?)"' ) . findall ( i1i )
 IiIiiI11i1Ii = re . compile ( '"is_trial":"1"' ) . findall ( i1i )
 i1iIIIiiiI = re . compile ( '"is_trial":"0"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']My GTV Account Information[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  i1i11I1I1iii1 ( '[COLOR' + II + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in oo0OoOO0o0o :
  i1i11I1I1iii1 ( '[COLOR' + II + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in IIIIIiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in Iii1I1111ii :
  I1IiiIiii1 = datetime . fromtimestamp ( float ( Iii1I1111ii [ 0 ] ) )
  I1IiiIiii1 . strftime ( '%Y-%m-%d %H:%M:%S' )
  i1i11I1I1iii1 ( '[COLOR' + II + ']Created:[/COLOR]  %s' % ( I1IiiIiii1 ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in i1I :
  I1IiiIiii1 = datetime . fromtimestamp ( float ( i1I [ 0 ] ) )
  I1IiiIiii1 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= I1IiiIiii1 <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   i1i11I1I1iii1 ( '[COLORred]Expires Today[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  i1i11I1I1iii1 ( '[COLOR' + II + ']Expires:[/COLOR]  %s' % ( I1IiiIiii1 ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in ooOoO00 :
  i1i11I1I1iii1 ( '[COLOR' + II + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in Oo0000O0OOooO :
  i1i11I1I1iii1 ( '[COLOR' + II + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in IiIiiI11i1Ii :
  i1i11I1I1iii1 ( '[COLOR' + II + ']Trial:[/COLOR] Yes' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in i1iIIIiiiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']Trial:[/COLOR] No' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 i1i11I1I1iii1 ( '' , '' , '' , '' )
 i1i11I1I1iii1 ( '' , '' , '' , '' )
 i1i11I1I1iii1 ( '[COLOR' + II + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 67 - 67: OOooOOo - OOooOOo * oO0o - O0OOOoOoo0 % o000O0o
def iIiiIIIiI1Ii ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
 Oo000oOO00oo ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 13 - 13: I11i * Ii / Ii . oO0o . Ii1IIIi1 . Ii1I
def iIIiIi ( ) :
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
def oO0Oo00oo ( ) :
 OoOoooO000OO = 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o
 O00Ooo = urllib2 . Request ( OoOoooO000OO , headers = { "Accept" : "application/xml" } )
 i1Oo00 = urllib2 . urlopen ( O00Ooo )
 if i1Oo00 and i1Oo00 . getcode ( ) == 200 :
  i1oOOO0ooOO = [ ]
  i11IiI1iiI11 = ElementTree . parse ( i1Oo00 )
  OOoOOOO00 = i11IiI1iiI11 . getroot ( )
  for oo0o00oOo0 in i11IiI1iiI11 . findall ( "channel" ) :
   IIii1III = oo0o00oOo0 . find ( 'title' ) . text
   IIii1III = base64 . b64decode ( IIii1III )
   IIii1III = IIii1III . partition ( "[" )
   ooooOoo0OO = IIii1III [ 1 ] + IIii1III [ 2 ]
   ooooOoo0OO = ooooOoo0OO . partition ( "]" )
   ooooOoo0OO = ooooOoo0OO [ 2 ]
   ooooOoo0OO = ooooOoo0OO . partition ( "   " )
   ooooOoo0OO = ooooOoo0OO [ 2 ]
   if 85 - 85: IIiIiII11i . I11i1ii1 % Ii1IIIi1 % ooOOOoO
   OOo00ooOoO0o = oo0o00oOo0 . find ( "description" ) . text
   if OOo00ooOoO0o :
    OOo00ooOoO0o = base64 . b64decode ( OOo00ooOoO0o )
    i1i1iiIIiiiII = OOo00ooOoO0o . partition ( "(" )
    i1i1iiIIiiiII = "NOW:  " + i1i1iiIIiiiII [ 0 ]
    Ii1I1 = OOo00ooOoO0o . partition ( ")\n" )
    Ii1I1 = Ii1I1 [ 2 ] . partition ( "(" )
    Ii1I1 = "NEXT:  " + Ii1I1 [ 0 ]
    OO0ooO0 = i1i1iiIIiiiII + Ii1I1
   else :
    OO0ooO0 = ""
   i1oOOO0ooOO . append ( { 'title' : IIii1III [ 0 ] , 'cs' : ooooOoo0OO , 'schedule' : OO0ooO0 } )
 return i1oOOO0ooOO
def OoOooOO0oOOo0O ( name ) :
 if 42 - 42: O0OOOoOoo0 / I11i + I1ii11iIi11i . I1ii11iIi11i % Ii1IIIi1
 Ii1III1 = name
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , o00O0O , ooIii1ii1II1iI1 , oO0o0 in i1IIIII11I1IiI :
  if Ii1III1 == 'Full List' :
   oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
   if 67 - 67: oO0o / Ii1I % ooOOOoO / iiiiiiii1
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
  else :
   Ii1III1 = ( Ii1III1 ) . replace ( 'World' , 'القنوات العربية' )
   if Ii1III1 in ooIii1ii1II1iI1 :
    oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
    if 1 - 1: iiiiiiii1 - ooOOOoO
    print oO0o0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    if 45 - 45: ii1ii11IIIiiI - Ii1IIIi1
    OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
    if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . ooOOOoO % I11i1ii1 . IIiIiII11i
   else :
    pass
def I1ii1Ii1 ( url , name , img ) :
 img = img
 name = name
 url = url
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1iiIIi11I , OoOoO in i1IIIII11I1IiI :
  if name == i1iiIIi11I :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) + OoOoO , ( url ) . strip ( ) , 10012 , img , img , '' )
  else :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 10012 , img , img , '' )
def iI111I1III ( name ) :
 Ii1III1 = name
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , o00O0O , oO0o0 in i1IIIII11I1IiI :
  oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
  OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
 else :
  OOiIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 36 - 36: ooOOOoO % Ii1IIIi1
  if 72 - 72: oOo0O0Ooo / O0OOOoOoo0 - o0o00Oo0O + ooOOOoO
  if 83 - 83: o0o00Oo0O
  if 89 - 89: I1ii11iIi11i + Ii1I - I11i
  if 40 - 40: oO0o + oO0o
  if 94 - 94: O0OOOoOoo0 * iI11I1II1I1I . ooOOOoO
  if 13 - 13: iI11I1II1I1I * OOooOOo / iiiiiiii1 % I11i1ii1 + o000O0o
  if 41 - 41: Ii1I
  if 5 - 5: I1ii11iIi11i
  if 100 - 100: ii1ii11IIIiiI + iI11I1II1I1I
  if 59 - 59: I1111IIi
  if 89 - 89: OOooOOo % iI11I1II1I1I
def oo000o0000oO ( ) :
 iiOOooooO0Oo ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( ooOooo000oOO ) :
  iiOOooooO0Oo ( 'Backup Genie Favourites' , oO0o0 , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( oO0 ) :
  iiOOooooO0Oo ( 'Backup Ivue Config' , oO0 , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  iiOOooooO0Oo ( 'Backup Kodi Favourites' , Ii1iIiII1ii1 , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 35 - 35: Ii1I + iiiiiiii1 - OOooOOo % o000O0o % I11i % OOooOOo
  if 45 - 45: oOo0O0Ooo * Ii1IIIi1 % oO0o
  if 24 - 24: I11i1ii1 - ooOOOoO * o000O0o
zip = oo00 . getSetting ( 'zip' )
O00OoOoO = xbmc . translatePath ( os . path . join ( zip ) )
def ooO0o0oo ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 79 - 79: I1111IIi % oO0o
  if 81 - 81: Ii + Ii * oO0o + I1111IIi
  if 32 - 32: o0o00Oo0O . ii
def iiIIiiIi ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = ooOooo000oOO
  elif 'Ivue' in name :
   url = oO0
  elif 'Kodi' in name :
   url = Ii1iIiII1ii1
  ooO0o0oo ( )
  i1ii1I = open ( url ) . read ( )
  IiiIII = os . path . join ( O00OoOoO , description . split ( 'Your ' ) [ 1 ] )
  oooOo0OOOoo0 = open ( IiiIII , mode = 'w' )
  oooOo0OOOoo0 . write ( i1ii1I )
  oooOo0OOOoo0 . close ( )
 else :
  if 'guisettings.xml' in description :
   ii11iI1iIiIi = open ( os . path . join ( O00OoOoO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0OO0OoO0o0o0 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   i1IIIII11I1IiI = re . compile ( o0OO0OoO0o0o0 ) . findall ( ii11iI1iIiIi )
   for type , IIIIIIi1IiIi , III1i in i1IIIII11I1IiI :
    III1i = III1i . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IIIIIIi1IiIi , III1i ) )
  else :
   IiiIII = os . path . join ( url )
   i1ii1I = open ( os . path . join ( O00OoOoO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oooOo0OOOoo0 = open ( IiiIII , mode = 'w' )
   oooOo0OOOoo0 . write ( i1ii1I )
   oooOo0OOOoo0 . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 69 - 69: ii1ii11IIIiiI / ooOoO0O00 + I11i1ii1
 if 35 - 35: Ii - o000O0o % Ii
 if 48 - 48: oO0o % ooOOOoO * I11i % o000O0o % Ii . O0OOOoOoo0
 if 68 - 68: O0OOOoOoo0 + I1ii11iIi11i % ii1ii11IIIiiI / Ii % OOooOOo
def ooo0 ( ) :
 ii1iIIi11 = 1
 ooO0o0oo ( )
 iI1IIIII1Ii = xbmc . translatePath ( os . path . join ( O00OoOoO , 'Build Backup' , 'Full Backup' , '' ) )
 iIiI1 = xbmc . translatePath ( os . path . join ( O00OoOoO , 'Build Backup' , 'my_full_backup.zip' ) )
 I1IiII1I1i1I1 = xbmc . translatePath ( os . path . join ( O00OoOoO , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( iI1IIIII1Ii ) :
  os . makedirs ( iI1IIIII1Ii )
 II11iiI = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not II11iiI ) : return False , 0
 IIii1III = II11iiI
 iiIi = xbmc . translatePath ( os . path . join ( iI1IIIII1Ii , IIii1III + '.zip' ) )
 OooooOo = [ 'plugin.video.GenieTv' ]
 IIIiiiIiI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 OO0OOoooo0o = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 IiIi1Ii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iiIIiI11II1 = "Creating full backup of existing build"
 oooOo = "Creating Community Build"
 oOoO0Oo0 = "Archiving..."
 i11i11i = ""
 iiI1iI = "Please Wait"
 Ooo00O0 ( Oo0o0000o0o0 , iiIi , oooOo , oOoO0Oo0 , i11i11i , iiI1iI , OO0OOoooo0o , IiIi1Ii )
 time . sleep ( 1 )
 OoO0OOoO0 = xbmc . translatePath ( os . path . join ( iI1IIIII1Ii , IIii1III + '_guisettings.zip' ) )
 iiI11i = zipfile . ZipFile ( OoO0OOoO0 , mode = 'w' )
 try :
  iiI11i . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iiI11i . close ( )
 if ii1iIIi11 == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + iIiI1 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + iiIi + '[/COLOR]' )
  if 75 - 75: I11i1ii1 / I1ii11iIi11i
def Ooo00O0 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iii = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 Ooi1IIii11i1I1 = len ( sourcefile )
 Ii1I1O0oo00oOOO0o = [ ]
 II1i = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for I111iiIIiI1I , ooO00Oo , Iiii1Ii1I in os . walk ( sourcefile ) :
  for file in Iiii1Ii1I :
   II1i . append ( file )
 oooOOOOOi1iIii = len ( II1i )
 for I111iiIIiI1I , ooO00Oo , Iiii1Ii1I in os . walk ( sourcefile ) :
  ooO00Oo [ : ] = [ o0O0ooooooo00 for o0O0ooooooo00 in ooO00Oo if o0O0ooooooo00 not in exclude_dirs ]
  Iiii1Ii1I [ : ] = [ oooOo0OOOoo0 for oooOo0OOOoo0 in Iiii1Ii1I if oooOo0OOOoo0 not in exclude_files ]
  for file in Iiii1Ii1I :
   Ii1I1O0oo00oOOO0o . append ( file )
   I1111ii11IIII = len ( Ii1I1O0oo00oOOO0o ) / float ( oooOOOOOi1iIii ) * 100
   o0oOoO00o . update ( int ( I1111ii11IIII ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   IiIi1II111I = os . path . join ( I111iiIIiI1I , file )
   if not 'temp' in ooO00Oo :
    if not 'plugin.program.originwizard' in ooO00Oo :
     import time
     o00oIIi1i1 = '01/01/1980'
     o0O0Ooo = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( IiIi1II111I ) ) )
     if o0O0Ooo > o00oIIi1i1 :
      iii . write ( IiIi1II111I , IiIi1II111I [ Ooi1IIii11i1I1 : ] )
 iii . close ( )
 o0oOoO00o . close ( )
 if 79 - 79: I11i1ii1 . o000O0o / o000O0o - I11i1ii1 * I1ii11iIi11i / I11i
 if 19 - 19: Ii1I
def oOOO00o000o ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
 if 66 - 66: o0o00Oo0O
def oOooOOo00ooO ( ) :
 Oo0oO ( )
 i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  iIII ( )
 if i11I1II1I11i == 1 :
  O0oO0OOoOOO0oO ( )
 if i11I1II1I11i == 2 :
  o0oO0oOO ( )
 if i11I1II1I11i == 3 :
  O00O ( )
  if 71 - 71: iiiiiiii1 - I11i - Ii1IIIi1
  if 28 - 28: iI11I1II1I1I
  if 7 - 7: I11i % I1111IIi * OOooOOo
  if 58 - 58: I1111IIi / ooOOOoO + IIiIiII11i % O0OOOoOoo0 - ii
  if 25 - 25: OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * o000O0o
  if 30 - 30: ooOOOoO % OOooOOo / Ii1I * o0o00Oo0O * ii1ii11IIIiiI . oOo0O0Ooo
  if 46 - 46: OOooOOo - o0o00Oo0O
  if 70 - 70: ooOOOoO + I1ii11iIi11i * iI11I1II1I1I . oOo0O0Ooo * ooOOOoO
  if 49 - 49: I11i
def I11iiI ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   oOIIiIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , OOoOooOoOOOoo , I1111i )
  if i11I1II1I11i == 1 :
   OooOOOo0 ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if i11I1II1I11i == 2 :
   i1iIii1i111 ( )
  if i11I1II1I11i == 3 :
   OOooo000OooO ( )
  if i11I1II1I11i == 4 :
   o0o0 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if i11I1II1I11i == 5 :
   OoOo ( )
  if i11I1II1I11i == 6 :
   IiI1 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if i11I1II1I11i == 7 :
   iiIiII ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if i11I1II1I11i == 8 :
   IIiiiI1iI ( str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if i11I1II1I11i == 9 :
   O0O0 ( )
  if i11I1II1I11i == 10 :
   O0oO0o0OOOOOO ( )
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
  if 24 - 24: ooOoO0O00 * I1111IIi - ooOOOoO / ii1ii11IIIiiI
 I1I11i ( 'movies' , 'MAIN' )
 if 62 - 62: I1ii11iIi11i
def ii1IOoO0O ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   Oo0oo ( )
  if i11I1II1I11i == 1 :
   iiIiIIIiiI ( )
  if i11I1II1I11i == 2 :
   oOOo0O00o ( )
  if i11I1II1I11i == 3 :
   Oo00OOoOo ( oO0o0 )
  if i11I1II1I11i == 4 :
   oOoo ( oO0o0 )
  if i11I1II1I11i == 5 :
   O0O0ooOOO ( )
  if i11I1II1I11i == 6 :
   I1ii1i1iiii ( url = 'http://www.iplocation.net/' , inc = 1 )
  if i11I1II1I11i == 7 :
   I1i1I ( )
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
  if 17 - 17: ooOOOoO - O0OOOoOoo0 % ii1ii11IIIiiI
  if 2 - 2: ii1ii11IIIiiI * Ii1I * ii
 I1I11i ( 'movies' , 'MAIN' )
 if 73 - 73: OOooOOo + I1ii11iIi11i
 if 61 - 61: iI11I1II1I1I
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
 if 47 - 47: ii
 if 2 - 2: OOooOOo % iiiiiiii1 * I1ii11iIi11i * OOooOOo
def Oo0OOo ( ) :
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
 if 44 - 44: ooOOOoO * I11i
def iI1i111I1Ii ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , III1iII1I1ii + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 49 - 49: Ii1IIIi1 % ooOOOoO * Ii / o000O0o % Ii1IIIi1
def OO0oO ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , O0o0Oo , '' )
 if 96 - 96: ii1ii11IIIiiI . iiiiiiii1 - Ii1I + I11i * oO0o / O0OOOoOoo0
 if 26 - 26: Ii1IIIi1 * I1ii11iIi11i
 if 31 - 31: ooOOOoO * o000O0o . ii1ii11IIIiiI
def Iii1IIII11I ( ) :
 Oo0oO ( )
 i1Oo0oO00o = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  i1Ii11ii1I ( )
 if i11I1II1I11i == 0 :
  OO0oI1iii1i ( oO0o0 )
 if i11I1II1I11i == 0 :
  oO0ooOoOO ( oO0o0 )
  if 48 - 48: o0o00Oo0O . Ii % I11i1ii1 - I11i . Ii
  if 61 - 61: iiiiiiii1 % oOo0O0Ooo + I1ii11iIi11i + I11i1ii1 * iiiiiiii1 % Ii1IIIi1
  if 38 - 38: I1ii11iIi11i
 I1I11i ( 'movies' , 'MAIN' )
 if 34 - 34: OOooOOo
def OoO0o00OOOOO ( ) :
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 i1IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1i )
 for o00O0O , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , o00O0O , o00O0O , '' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 19 - 19: O0OOOoOoo0 * I1ii11iIi11i . O0OOOoOoo0 . oO0o / oO0o - o000O0o
def i11111iiiII1I ( url ) :
 i1i = OoOooO ( I1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 45 - 45: Ii1IIIi1
def i1Ii11ii1I ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 25 - 25: Ii1IIIi1 % o0o00Oo0O
def I11oO0oo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + O00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 94 - 94: o000O0o - ooOOOoO + I1ii11iIi11i % Ii1I - I1111IIi
def oooOoO00OooO0 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o00OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 40 - 40: iI11I1II1I1I + O0OOOoOoo0 * OOooOOo + o000O0o
def I1Ii1i11I1I ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + oo0o000o0oOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 66 - 66: I11i * Ii1IIIi1 + ii1ii11IIIiiI * I11i + Ii1IIIi1 / ii
def o0OOOoo0ooo00 ( url ) :
 i1i = OoOooO ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 1 - 1: Ii1IIIi1 - iI11I1II1I1I * oO0o * iiiiiiii1 * o0o00Oo0O
def OO0oI1iii1i ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o0OOOooO00OO00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 40 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 78 - 78: IIiIiII11i - I1ii11iIi11i - o0o00Oo0O . Ii1IIIi1 + Ii - Ii1I
def o0oOOOOoo0 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + ooOO0OOO00o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 76 - 76: ii * ii - O0OOOoOoo0 - iI11I1II1I1I . ii / Ii1I
def OooOoOO0 ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  oOOOO0oo0O0OO ( )
 if i11I1II1I11i == 1 :
  O0OOoo0o ( )
 if i11I1II1I11i == 2 :
  i1IiIiIiiI1 ( )
  if 41 - 41: IIiIiII11i
  if 43 - 43: o0o00Oo0O - I11i1ii1 % ii % Ii1IIIi1 + O0OOOoOoo0
  if 61 - 61: I11i1ii1 . Ii + o000O0o
  if 8 - 8: iI11I1II1I1I
def O0OOoo0o ( ) :
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( iIIII )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , oOOo0ooO0 in i1IIIII11I1IiI :
  OOo ( 'Android Apps' + oOOo0ooO0 , 'https://www.apkfiles.com' + oO0o0 , 30035 , III1iII1I1ii + 'apps.png' )
 for oO0o0 , oOOo0ooO0 in i1I :
  OOo ( 'Android Games' + oOOo0ooO0 , 'https://www.apkfiles.com' + oO0o0 , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I11i ( 'movies' , 'MAIN' )
def ii1i1II11II1i ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '/cat' in url :
   OOo ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def o00OO0 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '/app' in url :
   OOo ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def iIi1i111 ( url ) :
 iIIII = OoOooO ( url )
 iIiIiiiIi = url
 if "page=" in str ( url ) :
  iIiIiiiIi = url . split ( '?' ) [ 0 ]
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'apk' in url :
   OOiIiIIi1 ( ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + o00O0O )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 OOiIiIIi1 ( 'Next Page' , iIiIiiiIi + str ( i1I ) , 30037 , III1iII1I1ii + 'Next.png' )
def Ii11IiI111 ( name , url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 name = name
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  IIiii11ii1II1 ( name , url , 'Brackets' )
def i1IiIiIiiI1 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO0oo = 'https://www.apkfiles.com/search?q=' + ( ii1I ) . replace ( ' ' , '+' ) + '&search_type=1'
 o0OOoOoO00 = OoO0oo . lower ( )
 iIi1i111 ( o0OOoOoO00 )
 if 97 - 97: ooOOOoO - I11i + I11i1ii1
def OO0000 ( url ) :
 o00O0 = xbmc . translatePath ( os . path . join ( o000OOO000 , 'Download' ) )
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
 if 53 - 53: O0OOOoOoo0 . I11i
def oOo0oO ( url ) :
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
 if 77 - 77: IIiIiII11i
 if 30 - 30: Ii1I % ooOoO0O00
def I1iIIIIIi ( name , url , description ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , name )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 iiIiIiIiiIiI = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iiIiIiIiiIiI
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , iiIiIiIiiIiI , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 23 - 23: oO0o / O0OOOoOoo0 / iI11I1II1I1I
 if 44 - 44: I1ii11iIi11i . I1ii11iIi11i + ii * Ii / ooOOOoO + iiiiiiii1
 if 17 - 17: Ii1IIIi1 + IIiIiII11i
 if 43 - 43: ooOOOoO % ii1ii11IIIiiI / I11i * iiiiiiii1
 if 85 - 85: iI11I1II1I1I . ii . I11i
def oOOOO0oo0O0OO ( ) :
 i1i = OoOooO ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1i )
 for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O , oO00OoO0oo in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , oO0o0 , 80003 , iiO0oOo00o , III1iII1I1ii + 'APKToolsB.png' , oO00OoO0oo )
def o00o0o000Oo ( apk , ret = None ) :
 if apk == "kodi" :
  Oooo00OOo = "https://kodi.tv/download/"
  i1i = OoOooO ( Oooo00OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1i )
  if len ( i1IIIII11I1IiI ) == 1 :
   iIiII = i1IIIII11I1IiI [ 0 ] [ 0 ]
   IIii1III = i1IIIII11I1IiI [ 0 ] [ 1 ]
   OooOO = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( iIiII , IIii1III )
  if ret == 'version' : return iIiII
  else : return OooOO
 elif apk == "spmc" :
  iio0oo0Oo = 'https://github.com/koying/SPMC/releases/latest/'
  i1i = OoOooO ( iio0oo0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1i )
  iIiII = re . sub ( '<[^<]+?>' , '' , i1IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  OooOO = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( iIiII , iIiII )
  if ret == 'version' : return iIiII
  else : return OooOO
def IIiii11ii1II1 ( name , url , Brackets ) :
 if I1IIII1i ( ) == 'android' :
  i1i1I1II = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not i1i1I1II : o0o0oO ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  O00oo0o0ooOo00 = name
  if i1i1I1II :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not Iii1 ( url ) == True : o0o0oO ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % O00oo0o0ooOo00 , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    iiI11i = zipfile . ZipFile ( oOO0O00Oo0O0o )
    for file in iiI11i . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as oooOo0OOOoo0 :
       OO00oO0OoO0o = file . split ( '/' ) [ 1 ]
       oooOo0OOOoo0 . write ( iiI11i . read ( file ) )
       xbmc . sleep ( 500 )
       oooOo0OOOoo0 . close ( )
       try :
        os . remove ( oOO0O00Oo0O0o )
       except :
        pass
       oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , OO00oO0OoO0o )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : o0o0oO ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0o0oO ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 5 - 5: Ii1IIIi1 % I1ii11iIi11i % I1111IIi % I11i1ii1
 if 17 - 17: ii1ii11IIIiiI + IIiIiII11i + ii / Ii1IIIi1 / I1111IIi
 if 80 - 80: I11i % ooOoO0O00 / ooOOOoO
 if 56 - 56: ooOoO0O00 . Ii
def Ii1Ii1IiIIIi1 ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1i )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  oO0o0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oO0o0 )
  OOoo00 ( ( I1111i ) . replace ( '_' , ' ' ) , oO0o0 )
  if 22 - 22: I11i1ii1 / I11i1ii1 - ii1ii11IIIiiI % ooOOOoO . Ii1IIIi1 + I1111IIi
def OOoo00 ( name , url ) :
 if I1IIII1i ( ) == 'android' :
  i1i1I1II = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not i1i1I1II : o0o0oO ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  O00oo0o0ooOo00 = name
  if i1i1I1II :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not Iii1 ( url ) == True : o0o0oO ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % O00oo0o0ooOo00 , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : o0o0oO ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : o0o0oO ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 64 - 64: ooOoO0O00 % Ii1I / ii1ii11IIIiiI % ii
 if 24 - 24: iiiiiiii1 + ii . I1111IIi / OOooOOo / ooOOOoO
def ooOoo ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'INFO' )
 if 91 - 91: I11i . O0OOOoOoo0 % I1ii11iIi11i - O0OOOoOoo0 . o000O0o % Ii
 if 25 - 25: iI11I1II1I1I
def oOo0 ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 30015 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 63 - 63: I11i1ii1
def oO0oOOOooo ( url , iconimage , fanart ) :
 i1i = OoOooO ( url )
 oOOoO = url
 o00O0O = iconimage
 fanart = fanart
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for i111iI , I1111i in i1IIIII11I1IiI :
  if '.mp4' in I1111i :
   OOiIiIIi1 ( 'Watch VIDEO' , url + '/' + i111iI , 222 , o00O0O , fanart , '' )
  if 'description' in I1111i :
   OOiIiIIi1 ( 'Read Description' , url + '/' + i111iI , 30017 , o00O0O , fanart , '' )
  if 'images' in I1111i :
   iiOOooooO0Oo ( 'View Images' , url + '/' + i111iI , 30018 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Android' , url + '/' + i111iI , 30016 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Pc' , url + '/' + i111iI , 30019 , o00O0O , fanart , '' )
 I1I11i ( 'movies' , 'INFO' )
 if 6 - 6: iI11I1II1I1I - iI11I1II1I1I % I11i / iI11I1II1I1I * iiiiiiii1
def iIi ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  o0oooo0OOo00 ( url )
  if 90 - 90: I11i / Ii1IIIi1 - Ii1IIIi1 . oOo0O0Ooo
def o0OOoo0oOoO00 ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  i1ii1iIi ( url )
  if 43 - 43: ii1ii11IIIiiI + O0OOOoOoo0 + ooOoO0O00 - OOooOOo + I11i
def OOOO00 ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1i )
 for o0I1iI111ii111i in i1IIIII11I1IiI :
  OO0O000 ( 'Description:' , o0I1iI111ii111i )
  if 83 - 83: iI11I1II1I1I
def Oo0O0O ( url ) :
 i1i = OoOooO ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for i111iI , I1111i in i1IIIII11I1IiI :
  if 'png' in I1111i :
   OOiIiIIi1 ( 'image' , '' , '' , url + '/' + i111iI , url + '/' + i111iI , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 8 - 8: Ii * o0o00Oo0O + Ii1I . iI11I1II1I1I % ooOOOoO / ooOOOoO
def oO00oo ( name , url , description ) :
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
 if 89 - 89: ii1ii11IIIiiI
 if 51 - 51: O0OOOoOoo0
def i1ii1iIi ( url ) :
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
 Oo0oo ( )
 if 68 - 68: O0OOOoOoo0 - I11i * oO0o % I11i1ii1 . I11i1ii1 - iI11I1II1I1I
def o0oooo0OOo00 ( url ) :
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
 Oo0oo ( )
 if 22 - 22: ii / Ii1I % O0OOOoOoo0 * OOooOOo
def Ii1IiiiI1ii ( name , url , description ) :
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
 Oo0oo ( )
 if 55 - 55: Ii1I
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
  oOoo0OO0 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oooOo0OOOoo0 . write ( oOoo0OO0 . rstrip ( '\r\n' ) + '\n' )
def Oo0oo ( ) :
 i11I1II1I11i = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if i11I1II1I11i == 0 : return
 elif i11I1II1I11i == 1 : pass
 iiIiIi1111iI1 = I1IIII1i ( )
 iIiIi11 ( "Platform: " + str ( iiIiIi1111iI1 ) )
 os . _exit ( 1 )
 iIiIi11 ( "Force close failed!  Trying alternate methods." )
 if iiIiIi1111iI1 == 'osx' :
  iIiIi11 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iiIiIi1111iI1 == 'linux' :
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
 elif iiIiIi1111iI1 == 'android' :
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
 elif iiIiIi1111iI1 == 'windows' :
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
  if 11 - 11: Ii1I . Ii1I + IIiIiII11i * OOooOOo . I1111IIi
  if 10 - 10: O0OOOoOoo0 * ii1ii11IIIiiI - I11i1ii1 . ooOOOoO - Ii1IIIi1
  if 94 - 94: oOo0O0Ooo % I1111IIi + oO0o
def oO0ooOoOO ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OoOooOI1I , ooO00Oo , Iiii1Ii1I in os . walk ( url ) :
  for file in Iiii1Ii1I :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    ii11iI1iIiIi = open ( ( os . path . join ( OoOooOI1I , file ) ) ) . read ( )
    OoooOoo0 = ii11iI1iIiIi . replace ( Oo0o0000o0o0 , 'special://home/' )
    oooOo0OOOoo0 = open ( ( os . path . join ( OoOooOI1I , file ) ) , mode = 'w' )
    oooOo0OOOoo0 . write ( str ( OoooOoo0 ) )
    oooOo0OOOoo0 . close ( )
 Oo0oo ( )
 if 26 - 26: I1111IIi / iI11I1II1I1I - iI11I1II1I1I
def i1iIii1i111 ( ) :
 OOo ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 OOo ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 OOo ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 57 - 57: I1111IIi
def IiI11I1Ii11II ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def oo0ooOoOOoO ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def Oo0000o ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1I :
  OOo ( ( '[COLOR' + II + ']Filter - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , o00O0O )
def iI1IiiiIIiiII ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def oOo000o ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I
 oOII1i1i1I1iII = 'https://www.radionomy.com/en/search/index?query=' + ( ii1I ) . replace ( ' ' , '+' )
 oO0OOoo0OO = OoOooO ( oOII1i1i1I1iII )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oO0o0 , 70005 , o00O0O )
  if 48 - 48: Ii1IIIi1 . Ii1IIIi1 + Ii + Ii1I % o0o00Oo0O
  if 67 - 67: I11i1ii1 / ooOOOoO * oOo0O0Ooo % ii
def OoOo ( ) :
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , 'http://www.listenlive.eu/' + oO0o0 , 10111113 , III1iII1I1ii + 'radio.png' )
def o0o0 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( I1111i , url , 222 , III1iII1I1ii + 'radio.png' )
  if 46 - 46: I1111IIi
def IIiI1i ( ) :
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.toonjet.com/' + oO0o0 , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii1 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
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
   OOo ( ( o00O0O ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in i1I :
  OOo ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def III ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 96 - 96: Ii - Ii % I11i * Ii1IIIi1 * OOooOOo - oO0o
  if 36 - 36: ii1ii11IIIiiI - ii . ii + Ii1I
def O0oO0o0OOOOOO ( ) :
 o0OoO0000oOO ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 o0OoO0000oOO ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 42 - 42: iiiiiiii1 % oO0o . Ii1I
def iiIIiIi ( ) :
 o0OoO0000oOO ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 o0OoO0000oOO ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 o0OoO0000oOO ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 97 - 97: O0OOOoOoo0 + ooOOOoO % I1ii11iIi11i . IIiIiII11i / IIiIiII11i * O0OOOoOoo0
def o0Oo ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , oO0o0 , i1II11i1iI1 in i1IIIII11I1IiI :
  if 'Parent' in I1111i :
   pass
  elif '2' in i1II11i1iI1 :
   o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 81 - 81: o000O0o . ii * I11i * oO0o
def II11IiI1 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , oO0o0 , i1II11i1iI1 in i1IIIII11I1IiI :
  if ii1I in I1111i . lower ( ) :
   if '1' in i1II11i1iI1 :
    o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in i1II11i1iI1 :
    o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in i1II11i1iI1 :
    o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 21 - 21: oO0o
    if 63 - 63: ooOOOoO . o0o00Oo0O * ooOOOoO + iI11I1II1I1I
def Ii1iIi ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , oO0o0 , i1II11i1iI1 in i1IIIII11I1IiI :
  if '1' in i1II11i1iI1 :
   o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in i1II11i1iI1 :
   o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in i1II11i1iI1 :
   o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 79 - 79: Ii1IIIi1 % iiiiiiii1 / o000O0o - iI11I1II1I1I - OOooOOo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: IIiIiII11i
def oO0OOoo ( url ) :
 i111iI = url
 oO0OOoo0OO = OoOooO ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1I :
  if 'mp3' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i111iI + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i111iI + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , i111iI + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in I1111i :
   o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i111iI + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 96 - 96: Ii1IIIi1
   if 38 - 38: O0OOOoOoo0 * ii
   if 2 - 2: o000O0o - Ii
def OOOo00o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i111iI = url
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
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i111iI + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i111iI + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , i111iI + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 3 - 3: I11i
   if 16 - 16: ooOoO0O00 . ooOoO0O00 / iiiiiiii1 % OOooOOo / oOo0O0Ooo * Ii1I
def IIIii11 ( ) :
 o0OoO0000oOO ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 o0OoO0000oOO ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 o0OoO0000oOO ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 29 - 29: ii1ii11IIIiiI - ii1ii11IIIiiI / I11i1ii1
def I11IIII ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O in i1IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oO0o0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in o00O0O :
   pass
  else :
   o0OoO0000oOO ( o00O0O , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oO0o0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + o00O0O + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 38 - 38: ii . I11i . IIiIiII11i - O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 65 - 65: Ii + oOo0O0Ooo / I1ii11iIi11i % Ii1IIIi1 . ii1ii11IIIiiI + iI11I1II1I1I
 if 32 - 32: oOo0O0Ooo
def IIIIIiiI11i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 43 - 43: oOo0O0Ooo / O0OOOoOoo0 / I11i1ii1 + iI11I1II1I1I + ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: IIiIiII11i - I1111IIi - I11i1ii1
def oO00oOoo00o0 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if ii1I in I1111i . lower ( ) :
   if '</a>' in I1111i :
    pass
   elif '(' in I1111i :
    o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 41 - 41: o000O0o / Ii1IIIi1 + O0OOOoOoo0 + I11i1ii1
    if 13 - 13: Ii - Ii . iI11I1II1I1I
def Iii1I11 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 94 - 94: ii1ii11IIIiiI / iiiiiiii1 . oOo0O0Ooo . O0OOOoOoo0 - ii / iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: I1111IIi
 if 76 - 76: oO0o * iI11I1II1I1I + Ii1I - I11i1ii1 - ooOOOoO / ooOoO0O00
def iIOoo0ooo0oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  i111iI = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( i111iI )
  if 21 - 21: I1111IIi - oOo0O0Ooo % ii + I11i
def o00O0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  if '<p align' in I1111i :
   pass
  elif '&nbsp;' in I1111i :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 28 - 28: oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: I1111IIi . ooOoO0O00 % ii * Ii
 if 67 - 67: iiiiiiii1 / oO0o . ii
def O000o0 ( ) :
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
def OoIIiIIIII1I ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ooiiI = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , o00O0O , o00O0O , I1111i )
 for url , I1111i in ooiiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def o00iIiI1iI1Ii1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oO0O = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iioO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0OOoo0OO )
 ii11I = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in iioO :
  iiOOooooO0Oo ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , I1111i in oO0O :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def Ooo0O00 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 53 - 53: o0o00Oo0O . oOo0O0Ooo
def OO0ooOOO0O00o ( ) :
 oO0OOoo0OO = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 i1IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if '9cart' in oO0o0 :
   OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 74 - 74: I11i1ii1 % OOooOOo / I1ii11iIi11i
def i1111Ii11i ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if '9cart' in url :
   OOo ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   OOo ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url , I1111i in ooOoO00 :
  if '9cart' in url :
   OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 98 - 98: iI11I1II1I1I - ooOoO0O00 + I11i1ii1 % ooOOOoO + I11i1ii1 / o000O0o
def O0O0Oo00OO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20003 , o00O0O )
 for url , I1111i in i1I :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 100 - 100: I11i . oOo0O0Ooo
def o00o0O0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'Watch' in url :
   OOo ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 47 - 47: I11i1ii1
def Oo0ooIi ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20005 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 44 - 44: IIiIiII11i . IIiIiII11i + Ii1IIIi1 * ii1ii11IIIiiI
def i1iIii1II1i ( url ) :
 url = cloudflare . source ( url )
 Oo ( url )
 if 27 - 27: Ii1I / Ii1IIIi1
def IiiIiiIIII ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in i1IIIII11I1IiI :
  Oo ( url )
  if 88 - 88: oO0o . iiiiiiii1 / ooOOOoO
  if 47 - 47: oO0o + Ii1I . I11i1ii1
def oO0o000OoOoO0 ( ) :
 if 43 - 43: oOo0O0Ooo - I11i / I11i . IIiIiII11i - ii1ii11IIIiiI
 iiOOooooO0Oo ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 40 - 40: O0OOOoOoo0 . OOooOOo * o0o00Oo0O
def o0oO0oOO ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 6 - 6: oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + ooOOOoO . Ii1IIIi1
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO0OOoo0OO )
 if 74 - 74: ooOoO0O00
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if ii1I in I1111i . lower ( ) :
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
    if 15 - 15: ooOoO0O00 + I1111IIi % oOo0O0Ooo / Ii * OOooOOo
    if 69 - 69: Ii
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 61 - 61: o0o00Oo0O
def Ooo0o0oo ( url ) :
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
 if 21 - 21: oO0o % iI11I1II1I1I . oO0o
def OO000OOOo0Oo ( url ) :
 iIIII = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  Oo00O0O = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10007 , Oo00O0O )
  if 70 - 70: oO0o
  if 43 - 43: OOooOOo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: oOo0O0Ooo
def Oo00O0o0O ( url , IMAGE ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   O0OoOO ( url )
   if 72 - 72: ii1ii11IIIiiI % ii1ii11IIIiiI / oOo0O0Ooo
   if 40 - 40: I1ii11iIi11i - Ii1IIIi1 + iiiiiiii1 - I11i % oOo0O0Ooo . I11i1ii1
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 35 - 35: Ii + ii * iI11I1II1I1I . iiiiiiii1
def O0OoOO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 48 - 48: O0OOOoOoo0 * ooOoO0O00 % ii * ii1ii11IIIiiI * oO0o
  if 7 - 7: O0OOOoOoo0 . ii1ii11IIIiiI . O0OOOoOoo0 - iiiiiiii1
  if 33 - 33: I11i1ii1 + ii - oO0o / ooOoO0O00 / ii
def I1ii1ii11i1I ( ) :
 if 82 - 82: Ii1I / Ii1IIIi1 - O0OOOoOoo0 / I1ii11iIi11i * oO0o
 iiOOooooO0Oo ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , O0o0Oo , '' )
 if 55 - 55: ii
def OO0OOOOOo ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'elete' in I1111i :
   pass
  else :
   i1i11I1I1iii1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 222 , o00O0O )
   if 7 - 7: o0o00Oo0O + ii1ii11IIIiiI . IIiIiII11i
def iii11i1i1 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o00OOo0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , IiIiI , i1iII1IiiIiI1 in o00OOo0o :
  for ii1I in IiIiI :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   o00O0oo0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oO0o0 , I1111i in o00O0oo0 :
    if 'tube' in oO0o0 :
     pass
    elif 'stage' in oO0o0 :
     i1i11I1I1iii1 ( '[COLOR' + II + ']' + IiIiI + '   -   ' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O , )
    elif 'vee' in oO0o0 :
     pass
     if 91 - 91: Ii % iiiiiiii1 * o000O0o - Ii1I . iiiiiiii1
def iIo00oo ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o00OOo0o = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , IiIiI , i1iII1IiiIiI1 in o00OOo0o :
  o00O0oo0 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oO0o0 , I1111i in o00O0oo0 :
   if 'tube' in oO0o0 :
    pass
   elif 'stage' in oO0o0 :
    i1i11I1I1iii1 ( '[COLOR' + II + ']' + IiIiI + '   -   ' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O )
   elif 'vee' in oO0o0 :
    pass
    if 78 - 78: I1111IIi - ooOOOoO % o0o00Oo0O - Ii1IIIi1 % oO0o
    if 43 - 43: oO0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: ii + o0o00Oo0O + Ii1I / ooOOOoO / ii1ii11IIIiiI * Ii1I
def IIi1i1IiIIi1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oOOo0OOOOo0Oo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oOOo0OOOOo0Oo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oOOo0OOOOo0Oo :
  OOOOo0o00OO0000 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 100 - 100: ooOOOoO
  if 82 - 82: iI11I1II1I1I
  if 19 - 19: oOo0O0Ooo
  if 66 - 66: o000O0o / OOooOOo
  if 13 - 13: IIiIiII11i
  if 55 - 55: I1ii11iIi11i % ooOoO0O00 * ooOOOoO
  if 95 - 95: Ii1IIIi1 / IIiIiII11i - I11i % iiiiiiii1 . ooOOOoO
def O0o0OO0000ooo ( ) :
 if 63 - 63: iI11I1II1I1I / I11i1ii1
 II1iOOoOooO0o ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 II1iOOoOooO0o ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 28 - 28: I1111IIi + Ii + ii / oO0o
 I1I11i ( 'movies' , 'MAIN' )
 if 6 - 6: oOo0O0Ooo - Ii
def O00O0O0OO00oo ( ) :
 II1iOOoOooO0o ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 II1iOOoOooO0o ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 39 - 39: I1111IIi % OOooOOo * Ii1I - ii - I1ii11iIi11i
 I1I11i ( 'movies' , 'MAIN' )
def Oo0 ( ) :
 if 96 - 96: ooOoO0O00
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 IiI1ii1Ii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 55 - 55: o000O0o + Ii1IIIi1 + ii1ii11IIIiiI
 for I1iii in IiI1ii1Ii :
  oOO0OO0O = O0Oo000ooO00 + I1iii + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( oOO0OO0O )
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oO0o0 , OOoOooOoOOOoo , Iio00 , o0ooooO0o0O , I1111i in i1IIIII11I1IiI :
   if ii1I in I1111i . lower ( ) :
    OOoiII1I1i ( I1111i , oO0o0 , 222 , OOoOooOoOOOoo , o0ooooO0o0O , Iio00 )
    if 6 - 6: o000O0o / o0o00Oo0O / ii1ii11IIIiiI / I1111IIi / o000O0o . iI11I1II1I1I
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 62 - 62: iI11I1II1I1I
    if 4 - 4: Ii1I * ooOOOoO . ooOOOoO . IIiIiII11i / Ii1IIIi1
def oOOoOOooO0 ( ) :
 if 42 - 42: iI11I1II1I1I * ii1ii11IIIiiI / oO0o + Ii1IIIi1
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 IiI1ii1Ii = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 48 - 48: ii - iiiiiiii1 . Ii * O0OOOoOoo0 - ii1ii11IIIiiI - I11i
 for I1iii in IiI1ii1Ii :
  o0o0Ii = O0Oo000ooO00 + I1iii + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( o0o0Ii )
  i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1111i , Iio00 , oO0o0 , o00O0O , o0ooooO0o0O , i1i1iII1 in i1IIIII11I1IiI :
   if ii1I in I1111i . lower ( ) :
    II1iOOoOooO0o ( I1111i , oO0o0 , i1i1iII1 , o00O0O , o0ooooO0o0O , Iio00 )
    if 94 - 94: Ii1I - I11i
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 42 - 42: I11i * OOooOOo . oO0o - O0OOOoOoo0 / IIiIiII11i
    if 25 - 25: I1ii11iIi11i % OOooOOo
def o00O ( ) :
 if 36 - 36: Ii1IIIi1 * oO0o - Ii1I + O0OOOoOoo0
 iIIII = OoOooO ( O0Oo000ooO00 + 'spongemain.php' )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , Iio00 , oO0o0 , o00O0O , o0ooooO0o0O , i1i1iII1 in i1IIIII11I1IiI :
  II1iOOoOooO0o ( I1111i , oO0o0 , i1i1iII1 , o00O0O , o0ooooO0o0O , Iio00 )
  I1I11i ( 'movies' , 'MAIN' )
def IIIiiiiiI1I ( url ) :
 if 64 - 64: I1111IIi * iI11I1II1I1I . Ii1I / ooOOOoO * iI11I1II1I1I
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i1i111III1 = ( '%s%s' % ( III1i1IIII1i , url ) )
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in i1IIIII11I1IiI :
  o00o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
  for i11I in o00o :
   if i11I == url :
    I1111i = ( '[COLORred]Watched - [/COLOR]' + I1111i ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  OOoiII1I1i ( I1111i , url , 222 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
  if 48 - 48: ii
  I1I11i ( 'movies' , 'MAIN' )
  if 77 - 77: o0o00Oo0O * Ii1I * o000O0o + oO0o + Ii1I - iiiiiiii1
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 10 - 10: Ii1I + I1111IIi
  if 58 - 58: oOo0O0Ooo + ii / O0OOOoOoo0 . I11i1ii1 % I11i / Ii1I
def oooO0 ( url ) :
 if 29 - 29: ii1ii11IIIiiI * Ii1IIIi1 * ooOoO0O00 . ii1ii11IIIiiI * iiiiiiii1 . I11i1ii1
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , Iio00 , url , o00O0O , o0ooooO0o0O , i1i1iII1 in i1IIIII11I1IiI :
  II1iOOoOooO0o ( I1111i , url , i1i1iII1 , o00O0O , o0ooooO0o0O , Iio00 )
  if 54 - 54: O0OOOoOoo0 . ooOoO0O00 . Ii1I * I11i % O0OOOoOoo0
  I1I11i ( 'movies' , 'MAIN' )
  if 30 - 30: ooOOOoO
  if 85 - 85: IIiIiII11i + I11i1ii1 * ooOOOoO
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: ii1ii11IIIiiI . oOo0O0Ooo % I11i
def OOoiII1I1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 28 - 28: ii1ii11IIIiiI - oOo0O0Ooo % oO0o * iiiiiiii1
 iiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiI , listitem = i111iiI1ii , isFolder = False )
 return IiIi1
 if 80 - 80: Ii1IIIi1 * I1111IIi
def II1iOOoOooO0o ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 4 - 4: iI11I1II1I1I . iiiiiiii1 + IIiIiII11i % ii
 iiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiI , listitem = i111iiI1ii , isFolder = True )
 return IiIi1
if 82 - 82: ii / I11i1ii1 * ooOOOoO * o0o00Oo0O . Ii1I
if 21 - 21: IIiIiII11i + I1ii11iIi11i
if 59 - 59: Ii1IIIi1 + oOo0O0Ooo / IIiIiII11i / OOooOOo
if 80 - 80: OOooOOo + iI11I1II1I1I . I1111IIi
if 76 - 76: oOo0O0Ooo * Ii1IIIi1
if 12 - 12: iI11I1II1I1I / ooOOOoO % ii1ii11IIIiiI
if 49 - 49: oO0o + IIiIiII11i / I1111IIi - o0o00Oo0O % ii1ii11IIIiiI
if 27 - 27: oO0o + I1ii11iIi11i
if 92 - 92: oOo0O0Ooo % O0OOOoOoo0
if 31 - 31: ii - o000O0o / iiiiiiii1
if 62 - 62: Ii - ooOOOoO
if 81 - 81: ooOOOoO
if 92 - 92: Ii1IIIi1 - I1ii11iIi11i - ii / I1111IIi - ooOoO0O00
if 81 - 81: ooOoO0O00 / iiiiiiii1 % Ii . iI11I1II1I1I * OOooOOo + ii
if 31 - 31: ooOoO0O00 % IIiIiII11i
def Ii1iii11I ( string ) :
 if OOoOO0oo0ooO == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 2 - 2: ii - ii1ii11IIIiiI % o000O0o / oOo0O0Ooo / I11i
def iiII ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 iII1IiiIIIIii = [ ]
 try :
  if 98 - 98: I1ii11iIi11i / o000O0o - oOo0O0Ooo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( IIIii1II1II ) == False :
  Ii1iii11I ( 'Making Favorites File' )
  iII1IiiIIIIii . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  ii11iI1iIiIi = open ( IIIii1II1II , "w" )
  ii11iI1iIiIi . write ( json . dumps ( iII1IiiIIIIii ) )
  ii11iI1iIiIi . close ( )
 else :
  Ii1iii11I ( 'Appending Favorites' )
  ii11iI1iIiIi = open ( IIIii1II1II ) . read ( )
  Oo0iII = json . loads ( ii11iI1iIiIi )
  Oo0iII . append ( ( name , url , iconimage , fanart , mode ) )
  OoooOoo0 = open ( IIIii1II1II , "w" )
  OoooOoo0 . write ( json . dumps ( Oo0iII ) )
  OoooOoo0 . close ( )
  if 73 - 73: ii1ii11IIIiiI / oOo0O0Ooo / ii + oOo0O0Ooo
  if 57 - 57: Ii1IIIi1 . ii1ii11IIIiiI % I11i
def I1I11 ( ) :
 if os . path . exists ( IIIii1II1II ) == False :
  iII1IiiIIIIii = [ ]
  Ii1iii11I ( 'Making Favorites File' )
  iII1IiiIIIIii . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  ii11iI1iIiIi = open ( IIIii1II1II , "w" )
  ii11iI1iIiIi . write ( json . dumps ( iII1IiiIIIIii ) )
  ii11iI1iIiIi . close ( )
 else :
  iI1i1iI1iI = json . loads ( open ( IIIii1II1II ) . read ( ) )
  I1IIiIi = len ( iI1i1iI1iI )
  for OOOOoOoO in iI1i1iI1iI :
   I1111i = OOOOoOoO [ 0 ]
   oO0o0 = OOOOoOoO [ 1 ]
   OOoOooOoOOOoo = OOOOoOoO [ 2 ]
   try :
    OO000 = OOOOoOoO [ 3 ]
    if OO000 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     OO000 = OOoOooOoOOOoo
    else :
     OO000 = o0ooooO0o0O
   try : o0oOoo0o = OOOOoOoO [ 5 ]
   except : o0oOoo0o = None
   try : IiiIiIIi = OOOOoOoO [ 6 ]
   except : IiiIiIIi = None
   if 63 - 63: O0OOOoOoo0 / Ii1I * o000O0o / IIiIiII11i + Ii1IIIi1 - o0o00Oo0O
   if OOOOoOoO [ 4 ] == 0 :
    iiOOooooO0Oo ( I1111i , oO0o0 , '' , OOoOooOoOOOoo , o0ooooO0o0O , '' , 'fav' )
   else :
    iiOOooooO0Oo ( I1111i , oO0o0 , OOOOoOoO [ 4 ] , OOoOooOoOOOoo , o0ooooO0o0O , '' , 'fav' )
    if 16 - 16: IIiIiII11i / ii1ii11IIIiiI . ii1ii11IIIiiI - ii1ii11IIIiiI / Ii1I
def I1Ii11i1ii1i ( name ) :
 Oo0iII = json . loads ( open ( IIIii1II1II ) . read ( ) )
 for oOOoOoOO in range ( len ( Oo0iII ) ) :
  if Oo0iII [ oOOoOoOO ] [ 0 ] == name :
   del Oo0iII [ oOOoOoOO ]
   OoooOoo0 = open ( IIIii1II1II , "w" )
   OoooOoo0 . write ( json . dumps ( Oo0iII ) )
   OoooOoo0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 39 - 39: I11i / I1111IIi - O0OOOoOoo0
 if 96 - 96: ooOOOoO * Ii1I * ii1ii11IIIiiI + Ii1I % oOo0O0Ooo + Ii
def Oo000oOO00oo ( ) :
 i1iI11Ii1i = os . path . join ( I11i1 , 'addons.ini' )
 Iii1Iii = open ( i1iI11Ii1i , "w+" )
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oO0OOoo0OO )
 Iii1Iii . write ( r'[' + IiII + ']' + '\n' )
 for I1111i , o00O0O , ooIii1ii1II1iI1 , oO0o0 in i1IIIII11I1IiI :
  oO0o0 = ( oO0o0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  iiI11111II = ( I1111i + '=plugin://' + IiII + '/?url=' + oO0o0 + '&mode=10012&name=' + ( I1111i ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;description=' )
  Iii1Iii . write ( iiI11111II + '\n' )
  if 48 - 48: O0OOOoOoo0 % Ii . ii * I1111IIi % oO0o . O0OOOoOoo0
  if 6 - 6: o0o00Oo0O . I11i1ii1 - o000O0o / Ii
def O00O0O00o0O ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 in i1IIIII11I1IiI :
  OOo ( '24/7' , oO0o0 , 90021 , III1iII1I1ii + '247Streams.png' )
  if 73 - 73: oO0o
def ii11iiII ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , III1iII1I1ii + '247Streams.png' , III1iII1I1ii + '247Streams.png' , '' )
def OOooo000OooO ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def iiI ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def OOoo0oO0 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def OOo0 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 i1IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , oO0o0 , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 25 - 25: iiiiiiii1 - ii1ii11IIIiiI / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
  if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + o000O0o + o000O0o + O0OOOoOoo0
def IIi1I1 ( ) :
 if 80 - 80: I11i % O0OOOoOoo0
 iiOOooooO0Oo ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 if 80 - 80: ii1ii11IIIiiI
def iioOO ( ) :
 if 38 - 38: ooOOOoO . I1111IIi - oO0o . oOo0O0Ooo
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i , oOOOoo0o in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + '  -  ' + ( oOOOoo0o ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oO0o0 , 10023 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 65 - 65: iiiiiiii1
  if 31 - 31: Ii / OOooOOo % Ii1I
  if 44 - 44: IIiIiII11i * oOo0O0Ooo + Ii1IIIi1
def I11II11IiI11 ( ) :
 if 97 - 97: I11i1ii1 / iI11I1II1I1I % I11i1ii1 / oOo0O0Ooo * O0OOOoOoo0 % OOooOOo
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
 if 17 - 17: iI11I1II1I1I
def ooi11I ( url ) :
 oOOoO = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0OOoo0OO = cloudflare . source ( oOOoO )
 i1IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 48 - 48: Ii1IIIi1 + iiiiiiii1 % Ii1IIIi1
  if 84 - 84: o0o00Oo0O % ii1ii11IIIiiI . ii1ii11IIIiiI . O0OOOoOoo0 * ooOOOoO
  if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
  if 61 - 61: oOo0O0Ooo + o000O0o % iiiiiiii1 % iI11I1II1I1I - ii
def iIIiI1 ( ) :
 if 4 - 4: ii + O0OOOoOoo0 % o0o00Oo0O + iI11I1II1I1I % O0OOOoOoo0 * Ii
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 oO0o0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( ii1I ) . replace ( ' ' , '+' )
 oO0OOoo0OO = cloudflare . source ( oO0o0 )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  if ii1I in I1111i . lower ( ) :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 10022 , III1iII1I1ii + 'dtv.png' )
   if 32 - 32: OOooOOo + I11i1ii1 + ii1ii11IIIiiI + oOo0O0Ooo
   if 26 - 26: O0OOOoOoo0 - I1ii11iIi11i + oOo0O0Ooo + I11i
   if 37 - 37: I11i * Ii1IIIi1 + oOo0O0Ooo . Ii1I * ii
def OoooOO0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i111iI , OoOOOo0o0ooo , oo0OoO , I1111i in i1IIIII11I1IiI :
  iIIi1iii1 = ( oo0OoO ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o00o0OOoOo0O0 = ( OoOOOo0o0ooo ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1o0 = 'Season ' + o00o0OOoOo0O0 + 'Episode ' + iIIi1iii1 + I1111i
  I1IiiiiI1i1I ( I1o0 , i111iI )
  if 48 - 48: ooOOOoO + IIiIiII11i % o000O0o % Ii1IIIi1 * IIiIiII11i
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 41 - 41: oO0o
  if 13 - 13: I11i1ii1 - oOo0O0Ooo
def I1IiiiiI1i1I ( name , url ) :
 i111iI = url
 iii11 = name
 O0 = cloudflare . source ( i111iI )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for oOOo0OOOOo0Oo , OO0oOi1i11ii in i1I :
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + iii11 + OO0oOi1i11ii + '[/COLOR]' , oOOo0OOOOo0Oo , 10012 , III1iII1I1ii + 'dtv.png' )
  if 86 - 86: Ii1I - ooOoO0O00 + I1ii11iIi11i * oOo0O0Ooo / Ii % o000O0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 17 - 17: I11i1ii1 + I11i1ii1 . Ii1I
 if 50 - 50: iI11I1II1I1I * o000O0o
def oOoOoOoo0 ( ) :
 if 85 - 85: ooOoO0O00
 if 100 - 100: ii / ooOOOoO % oO0o + ii1ii11IIIiiI
 if 42 - 42: I1ii11iIi11i / I1111IIi . ii1ii11IIIiiI * oOo0O0Ooo
 if 54 - 54: OOooOOo * O0OOOoOoo0 + oO0o
 if 93 - 93: I11i / oOo0O0Ooo
 if 47 - 47: I1ii11iIi11i * Ii1IIIi1
 if 98 - 98: o000O0o - o000O0o . I11i1ii1
 iiOOooooO0Oo ( '[COLOR' + II + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , '' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 60 - 60: oOo0O0Ooo * Ii1I / o0o00Oo0O + ooOOOoO + I1111IIi
def O0oO0o00oo0o ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i111IiIi1 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + o00O0O , '' , '' )
 for url in i111IiIi1 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 16 - 16: Ii * Ii1IIIi1 . I1111IIi
def OOI1I ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i111IiIi1 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  o00O0O = 'http://watchepisodes.cc/' + o00O0O
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10093 , o00O0O , o00O0O , '' )
 for url in i111IiIi1 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 54 - 54: OOooOOo
def o00O0Oooo ( url , iconimage ) :
 o00O0O = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oo0OoO , url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + oo0OoO + ' - ' + I1111i + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , o00O0O , '' , '' )
  if 83 - 83: ii . oOo0O0Ooo + ii1ii11IIIiiI * o0o00Oo0O / o000O0o
def IiiiI11 ( url , iconimage ) :
 o00O0O = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  if 'player' in I1111i :
   pass
  elif 'vod' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , o00O0O , '' , '' )
   if 57 - 57: iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
   if 95 - 95: o000O0o
   if 48 - 48: ooOOOoO / iI11I1II1I1I % IIiIiII11i
   if 39 - 39: ooOoO0O00 . Ii1I / ooOOOoO / ooOOOoO
   if 100 - 100: ii - ii + I1111IIi
   if 32 - 32: OOooOOo * I11i / ii
def III1ii1I ( ) :
 if 90 - 90: iiiiiiii1
 if 35 - 35: IIiIiII11i / ii1ii11IIIiiI
 if 79 - 79: OOooOOo + iiiiiiii1 * O0OOOoOoo0 * ii1ii11IIIiiI
 if 53 - 53: Ii1IIIi1 / I1ii11iIi11i
 if 10 - 10: Ii1I . I11i
 if 75 - 75: o0o00Oo0O * ooOoO0O00 - ooOOOoO / Ii1IIIi1 % Ii1IIIi1 / OOooOOo
 if 5 - 5: o0o00Oo0O - O0OOOoOoo0 / iiiiiiii1 . I11i
 if 7 - 7: Ii1I - OOooOOo
 if 54 - 54: o000O0o / iI11I1II1I1I / ii . ooOoO0O00 - OOooOOo
 if 57 - 57: iI11I1II1I1I * ii1ii11IIIiiI * O0OOOoOoo0 / o000O0o
 if 46 - 46: ii1ii11IIIiiI
 if 61 - 61: I11i / I11i1ii1 - IIiIiII11i
 if 87 - 87: Ii1I / oOo0O0Ooo
 if 45 - 45: OOooOOo * I11i1ii1 / ii + oO0o . iiiiiiii1 / oO0o
 iiOOooooO0Oo ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , III1iII1I1ii + 'latest.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , III1iII1I1ii + 'popular.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , III1iII1I1ii + 'Genre.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , III1iII1I1ii + 'series.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 if 64 - 64: ii1ii11IIIiiI / ooOoO0O00 % oOo0O0Ooo - I11i
 if 11 - 11: Ii1I - ii
def I1Ii11I11i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iIi1 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( iIi1 ) )
 for url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 48 - 48: iI11I1II1I1I / I1ii11iIi11i + oO0o % I1ii11iIi11i + ii1ii11IIIiiI + oO0o
def o00o0o0oOo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 33 - 33: ooOoO0O00 / I1111IIi - ooOoO0O00 . oOo0O0Ooo
def I1iI11I ( url ) :
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
  if 29 - 29: iI11I1II1I1I + IIiIiII11i - iiiiiiii1 + iI11I1II1I1I
  if 14 - 14: ii1ii11IIIiiI / ii + IIiIiII11i . o0o00Oo0O / ooOoO0O00
def OOoo0 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii11I1iIIi = 'http://www.watchseriesgo.to/search/' + ii1I . replace ( ' ' , '%20' )
 oO0OOoo0OO = OoOooO ( Ii11I1iIIi )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'watch online' in I1111i :
   pass
  else :
   print oO0o0
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to' + oO0o0 , 10044 , o00O0O , '' , '' )
   if 68 - 68: ooOOOoO / iI11I1II1I1I . I1ii11iIi11i + Ii + I11i
   xbmcplugin . setContent ( O000oo0O , 'movies' )
   if 92 - 92: oO0o . I11i . ii1ii11IIIiiI % OOooOOo
def OO00O00o0O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , oo0OoO , Iio00 in i1IIIII11I1IiI :
  oO0oOOoo00000 = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oo0OoO ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + oO0oOOoo00000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , o00O0O , '' , Iio00 )
  if 100 - 100: oO0o % OOooOOo / ooOOOoO * o0o00Oo0O - o000O0o
def I1IiIi1iiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  oO0oOOoo00000 = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + oO0oOOoo00000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 26 - 26: oOo0O0Ooo % OOooOOo
def OO00o0oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , o00O0O , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 3 - 3: ii1ii11IIIiiI * I11i1ii1 - oOo0O0Ooo / ooOoO0O00
def ii1iIi1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIi1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoOOOo0o0ooo , o00OOo0o in iIi1 :
  i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( o00OOo0o ) )
  for url , I1111i in i1IIIII11I1IiI :
   oO0oOOoo00000 = ( OoOOOo0o0ooo ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + oO0oOOoo00000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 44 - 44: oO0o + ooOOOoO % oO0o + ooOoO0O00 + O0OOOoOoo0 + o0o00Oo0O
class Ii1iII1ii1 ( ) :
 if 80 - 80: iI11I1II1I1I / Ii + O0OOOoOoo0
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 41 - 41: iiiiiiii1 + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
  oO0oOOoo00000 = name
  self . Get_Sources ( oO0o0 , oO0oOOoo00000 )
  if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
  if 25 - 25: ii . ii1ii11IIIiiI % O0OOOoOoo0 . I1111IIi
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  oO0OOoo0OO = OoOooO ( URL )
  i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oO0o0 , I1111i in i1IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + oO0o0
   self . Get_site_link ( URL , season_name )
   if 67 - 67: ii + iiiiiiii1 / I11i1ii1
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
   if 75 - 75: I1111IIi / ii . oOo0O0Ooo + iiiiiiii1 - IIiIiII11i
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   I1i11 = 'DACLIPS'
   if I1i11 in Ii1iII1ii1 . source_list :
    pass
   else :
    self . daclips ( url , season_name , I1i11 )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    I1i11 = 'THEVIDEO'
    if I1i11 in Ii1iII1ii1 . source_list :
     pass
    else :
     self . thevideo ( url , season_name , I1i11 )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     I1i11 = 'ALLMYVIDEOS'
     if I1i11 in Ii1iII1ii1 . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , I1i11 )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      I1i11 = 'VIDSPOT'
      if I1i11 in Ii1iII1ii1 . source_list :
       pass
      else :
       self . vidspot ( url , season_name , I1i11 )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       I1i11 = 'VODLOCKER'
       if I1i11 in Ii1iII1ii1 . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , I1i11 )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        I1i11 = 'VIDTO'
        if I1i11 in Ii1iII1ii1 . source_list :
         pass
        else :
         self . vidto ( url , season_name , I1i11 )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 5 - 5: I11i - Ii . I1111IIi
       else :
        if 'youwatch' in url :
         I1i11 = 'YouWatch'
         if I1i11 in Ii1iII1ii1 . source_list :
          pass
         else :
          self . youwatch ( url , season_name , I1i11 )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 10 - 10: OOooOOo . I1111IIi * iI11I1II1I1I - o000O0o - OOooOOo / iiiiiiii1
          if 13 - 13: o000O0o + OOooOOo % I1111IIi % ii
 def allmyvid ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for O0oO , I1111i in i1IIIII11I1IiI :
   self . Printer ( O0oO , season_name , source_name )
   if 22 - 22: iiiiiiii1
 def vidspot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0oO , I1111i in i1IIIII11I1IiI :
   self . Printer ( O0oO , season_name , source_name )
   if 23 - 23: o0o00Oo0O
 def thevideo ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0oO in i1IIIII11I1IiI :
   self . Printer ( O0oO , season_name , source_name )
   if 41 - 41: ooOoO0O00 . Ii1IIIi1 / I11i1ii1 / I11i % I1111IIi - ii1ii11IIIiiI
 def vodlocker ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0oO in i1IIIII11I1IiI :
   self . Printer ( O0oO , season_name , source_name )
   if 14 - 14: Ii1I - Ii * iiiiiiii1
 def daclips ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oO0OOoo0OO )
  for O0oO in i1IIIII11I1IiI :
   self . Printer ( O0oO , season_name , source_name )
   if 39 - 39: ii
 def filehoot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0oO in i1IIIII11I1IiI :
   self . Printer ( O0oO , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0oO in i1IIIII11I1IiI :
   self . Printer ( O0oO , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0oO in i1IIIII11I1IiI :
   self . youplay ( O0oO , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0oO in i1IIIII11I1IiI :
   self . Printer ( O0oO , season_name , source_name )
   if 19 - 19: Ii
 def Printer ( self , Link , season_name , source_name ) :
  if 80 - 80: oOo0O0Ooo
  if Link in Ii1iII1ii1 . List :
   pass
  elif source_name in Ii1iII1ii1 . source_list :
   pass
  else :
   i1i11I1I1iii1 ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 10012 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   Ii1iII1ii1 . List . append ( Link )
   Ii1iII1ii1 . source_list . append ( source_name )
   if 58 - 58: o000O0o + Ii1I % OOooOOo
   xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 22 - 22: iI11I1II1I1I - ii1ii11IIIiiI / oOo0O0Ooo * I1111IIi
   if 26 - 26: I11i + Ii1IIIi1 - I11i + I1ii11iIi11i . o000O0o
   if 97 - 97: ooOoO0O00
   if 46 - 46: Ii1I
   if 30 - 30: oO0o / o0o00Oo0O * I11i * iiiiiiii1 + ii * O0OOOoOoo0
def OO0 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 23 - 23: ooOOOoO
def I1I ( url ) :
 iiOOooooO0Oo ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( iIIII )
 for o0OO , url , iI11i1I1i , O000O , IioO0oOo0000o0O , o0O0ooooooo00 , ii1i1i11iI11 , oooOo0OOOoo0 , ii11iI1iIiIi , iiIII , iIi11Ii1I1 in i1IIIII11I1IiI :
  iI11i1I1i = iI11i1I1i
  if 'Arsenal' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'arsenal-logo.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                                  ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Bournemouth' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'afc-bournemouth.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                       ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Burnley' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'KEGnQWW.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                                   ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Chelsea' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'chelsea.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                                  ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Crystal' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'CrystalPalace.0.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                       ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Everton' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'Everton.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                                   ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Hull' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'hull-city-afc.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                                 ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Leicester' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'leicester-city-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                       ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Liverpool' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'liverpool-logo.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                               ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Manchester City' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'city-logo.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '               ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Manchester United' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + '91.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '          ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Middlesbrough' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'middlesbrough-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                 ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Southampton' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'southampton-fc-logo.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                   ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Stoke City' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'stoke-city.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                          ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Sunderland' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'sunderland-logo.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                        ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Swansea' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'swansea-city-afc.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                    ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Tottenham' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'tottenham-hotspur_zps4e3ed7c1.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '        ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Watford' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'watford-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '                              ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'Bromwich' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'west-bromwich-albion-logo.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '   ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  elif 'West Ham' in iI11i1I1i :
   iii11i1IIII = III1iII1I1ii + 'west-ham.png'
   I1111i = '[COLOR' + II + ']' + o0OO + ' - ' + iI11i1I1i + '             ' + O000O + '        ' + IioO0oOo0000o0O + '        ' + o0O0ooooooo00 + '        ' + ii1i1i11iI11 + '        ' + oooOo0OOOoo0 + '        ' + ii11iI1iIiIi + '        ' + iiIII + '[/COLOR]'
  iiOOooooO0Oo ( str ( I1111i ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , iii11i1IIII , iii11i1IIII , iI11i1I1i )
  if 12 - 12: I1111IIi - ii1ii11IIIiiI % ii1ii11IIIiiI
def iIII1I11II1i1 ( description ) :
 iI11i1I1i = description
 oO0o0 = ( 'http://www.fullmatchesandshows.com/?s=' + iI11i1I1i ) . replace ( ' ' , '%20' )
 iI11ii1i ( oO0o0 )
 if 50 - 50: iI11I1II1I1I - ooOOOoO % O0OOOoOoo0 - I1ii11iIi11i
def OOO00OI11II1 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 i1IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oO0o0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o00O0O , O0o0Oo , '' )
  if 35 - 35: Ii1I * iiiiiiii1 - o000O0o % Ii1IIIi1 % Ii
def oo0000o0O0oOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iIi1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIi1 in iIi1 :
  OoOoOo0 = re . compile ( '(.*?)</h2>' ) . findall ( str ( iIi1 ) )
  for I1i1Ii111II in OoOoOo0 :
   I1i1Ii111II = I1i1Ii111II
  O0o0 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iIi1 ) )
  for ooOo0O0 , o00O0O , time , OooO00O0OO0oo in O0o0 :
   oo0o00oOo0 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( OooO00O0OO0oo )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1Ii111II + ' - ' + ooOo0O0 + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + o00O0O , O0o0Oo , ( str ( oo0o00oOo0 ) ) )
   if 60 - 60: IIiIiII11i + I11i % iiiiiiii1 + I11i1ii1 . I1111IIi % IIiIiII11i
 I1I11i ( 'tvshows' , 'Media Info 3' )
 if 58 - 58: I11i1ii1
def i1iI11ii ( ) :
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
 if 65 - 65: ooOoO0O00 . Ii
def OOOO0O ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  O0000oO00oO0o = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   O0000oO00oO0o = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   i1i11I1I1iii1 ( '[COLOR' + II + ']' + O0000oO00oO0o + '[/COLOR]' , url , 10013 , o00O0O )
 for url , o00O0O , I1111i in i1I :
  O0000oO00oO0o = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   i1i11I1I1iii1 ( '[COLOR' + II + ']' + O0000oO00oO0o + '[/COLOR]' , url , 10013 , o00O0O )
def iI11ii1i ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 if 86 - 86: I11i / I11i1ii1 . I11i % oOo0O0Ooo + o000O0o % ooOOOoO
 if 72 - 72: I11i1ii1 - Ii1I + o000O0o . OOooOOo
 if 44 - 44: Ii1I / o0o00Oo0O - I1111IIi + Ii1IIIi1 . ooOOOoO . Ii1I
 if 95 - 95: OOooOOo % iiiiiiii1 % ooOoO0O00 * I11i + Ii1IIIi1
 if 34 - 34: iiiiiiii1 * I11i . oOo0O0Ooo % Ii
 if 61 - 61: iI11I1II1I1I + o000O0o * ooOOOoO - ooOoO0O00 % o000O0o
 if 76 - 76: o000O0o / OOooOOo
 for url , o00O0O , I1111i in i1I :
  O0000oO00oO0o = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   i1i11I1I1iii1 ( '[COLOR' + II + ']' + O0000oO00oO0o + '[/COLOR]' , url , 10013 , o00O0O )
   if 12 - 12: iiiiiiii1
def OO0oOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oO0OOoo0OO )
 for oOOo0OOOOo0Oo in i1IIIII11I1IiI :
  IIiIi1II1IiI = ( oOOo0OOOOo0Oo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOOOo0o00OO0000 ( 'http:' + IIiIi1II1IiI )
  if 99 - 99: I1ii11iIi11i
  if 17 - 17: Ii - Ii + Ii1I * I11i1ii1 * o000O0o / ii
  if 22 - 22: iiiiiiii1 * Ii1I - I1111IIi
  if 71 - 71: iI11I1II1I1I / Ii % I11i . iiiiiiii1 * oOo0O0Ooo % IIiIiII11i
def i1II1111 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( I1111i , url , 8046 , o00O0O )
 for url in i1I :
  OOo ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def ooOOOo0 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 19 - 19: iiiiiiii1 + O0OOOoOoo0 * iiiiiiii1
def OOOIIIIiiIi ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
def o0OoOO ( ) :
 OOo ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , III1iII1I1ii + 'documentary.png' )
 OOo ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , III1iII1I1ii + 'documentary.png' )
 OOo ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , III1iII1I1ii + 'Search.png' )
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , oO0o0 , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def o000Oo0oO0OO0 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + o00O0O )
 for url in next :
  OOo ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 54 - 54: oOo0O0Ooo
  if 19 - 19: O0OOOoOoo0 . ooOOOoO * ii - Ii1IIIi1 + o0o00Oo0O * iiiiiiii1
def OoI1 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   i1i11I1I1iii1 ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   OOo ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def Iii11111I1iii ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10012 , '' )
  if 67 - 67: Ii1I + o000O0o * I1111IIi / IIiIiII11i % oO0o % oO0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIIII1IIiIi ( name , url ) :
 oo0o = 0
 name = name
 url = url
 i1Oo0oO00o = [ '144' , '240' , '380' , '480' , '720' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OOOOo0o00OO0000 ( url )
  if 69 - 69: I11i + Ii1I / iI11I1II1I1I . I1111IIi % Ii1I * OOooOOo
  if 13 - 13: iI11I1II1I1I + O0OOOoOoo0 / ii1ii11IIIiiI / ooOoO0O00 % oO0o - iI11I1II1I1I
  if 60 - 60: iiiiiiii1
  if 77 - 77: oOo0O0Ooo / Ii1I
  if 95 - 95: iiiiiiii1 * ooOoO0O00 + o000O0o
  if 40 - 40: IIiIiII11i
  if 7 - 7: Ii1IIIi1 / oO0o
  if 88 - 88: ooOoO0O00
def O0ooOo0Oooo ( ) :
 iIIII = I1iIi1iIiiIiI ( 'http://documentarylovers.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  if 'genre' in oO0o0 :
   OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oO0o0 , 80010 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1iiIIiI11I ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , o00O0O )
 for url in next :
  OOo ( 'NEXT PAGE' , url , 80010 , III1iII1I1ii + 'Next.png' )
  if 29 - 29: ooOOOoO + o000O0o % I11i1ii1 + OOooOOo
def oOoOo000 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( iIIII )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
 for url in i1I :
  Iii11111I1iii ( url )
  if 37 - 37: O0OOOoOoo0
def iIiI1I1II1 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoO0oo = 'http://documentarylovers.com/?s=' + ( ii1I ) . replace ( ' ' , '+' )
 o0OOoOoO00 = OoO0oo . lower ( )
 I1iiIIiI11I ( o0OOoOoO00 )
 if 45 - 45: oOo0O0Ooo + ooOOOoO + ooOoO0O00
def i1II ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if 'films' in url :
   OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , III1iII1I1ii + 'documentary.png' )
def OOOoooOo00O ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  if 'films' in url :
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + o00O0O )
 for url in i1I :
  OOo ( 'NEXT' , url , 8049 , III1iII1I1ii + 'Next.png' )
def iiIIiI1I ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'rtd' in url :
   oOoO0oOO0o ( url )
   if 94 - 94: o000O0o * ooOOOoO
def oOoO0oOO0o ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iIIII )
 for i1i , file in i1IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1i + file )
  OOOOo0o00OO0000 ( url )
  if 88 - 88: o0o00Oo0O % I1111IIi . I1111IIi . iiiiiiii1 / ooOoO0O00
  if 16 - 16: I1ii11iIi11i * iiiiiiii1
def O0ooO0o ( ) :
 oO0OOoo0OO = I1iIi1iIiiIiI ( 'http://www.stream2watch.co/live-tv' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , o00O0O , I1111i , i1iiIIi11I in i1IIIII11I1IiI :
  OOo ( ( I1111i + '[COLOR' + II + ']' + i1iiIIi11I + '[/COLOR]' ) , oO0o0 , 8086 , o00O0O )
  if 42 - 42: ii - OOooOOo - Ii1IIIi1 * iiiiiiii1
def OO0iii111 ( url ) :
 oO0OOoo0OO = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8087 , o00O0O )
  if 59 - 59: I11i1ii1 * iiiiiiii1
def O0oooOo0000o0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  o0o0Oo0oo ( url , I1111i )
  if 53 - 53: iiiiiiii1 + ooOoO0O00 . oO0o / Ii + ii1ii11IIIiiI % OOooOOo
def o0o0Oo0oo ( url , name ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  print url
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 9 - 9: I11i1ii1 . ooOOOoO - I1ii11iIi11i . iiiiiiii1
def i1I111II11 ( ) :
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oO0o0 , 3002 , 'http://www.solie.org/alibrary/' + o00O0O )
def o00oO ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def I11ii111i ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 IIiI1I11ii1i = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIIII )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , I1111i in IIiI1I11ii1i :
  OOo ( '[COLOR' + II + ']Season- ' + I1111i + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  OOo ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , o00O0O , I1111i in i1I :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def o0ooo ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  Ii1Iii1 ( url )
def Ii1Iii1 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 87 - 87: ii
def Iii ( ) :
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oO0o0 , 8065 , III1iII1I1ii + 'classicmovies.png' )
def iiI1 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  Oo ( url )
  if 70 - 70: ii . I11i1ii1 / o000O0o . o000O0o - I11i
def i1iI1 ( ) :
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oO0o0 , 8065 , III1iII1I1ii + 'classictv.png' )
def i1II1i1iiI1 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'mp4' in url :
   OOOOo0o00OO0000 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 62 - 62: ii1ii11IIIiiI . Ii % o0o00Oo0O % iiiiiiii1 - I1ii11iIi11i
def OooOO0o0oOoO ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oO0o0 , 8071 , III1iII1I1ii + 'streams.png' )
def i11I1Ii1Iiii1 ( url ) :
 oO0OOoo0OO = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  if '(Free Access)' in I1111i :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def o0oooOoOoOo ( url ) :
 oO0OOoo0OO = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , o00O0O , o0ooooO0o0O , '' )
  if 96 - 96: OOooOOo / oO0o % ii * I11i1ii1
def Iii11I ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  iI1ii1 ( 'http://watchxxxfree.com/categories' )
 if i11I1II1I11i == 1 :
  O0oOOo ( 'http://www.perfectgirls.net' )
 if i11I1II1I11i == 2 :
  ii111IIiiiiI ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 3 :
  oo0OOoOo0 ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 4 :
  ii111IIiiiiI ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 5 :
  ii111IIiiiiI ( 'http://www.xvideos.com/verified/videos' )
 if i11I1II1I11i == 6 :
  oO00oO0 ( 'http://www.xvideos.com/tags' )
 if i11I1II1I11i == 7 :
  o0oI1Iii ( 'http://www.xvideos.com/porn' )
 if i11I1II1I11i == 8 :
  II1I1Ii11 ( )
  if 20 - 20: ii1ii11IIIiiI / O0OOOoOoo0 + IIiIiII11i . Ii . Ii1IIIi1
  if 77 - 77: OOooOOo
  if 91 - 91: o000O0o
  if 56 - 56: iI11I1II1I1I % IIiIiII11i / OOooOOo % ii
  if 13 - 13: I1111IIi . I1ii11iIi11i - ooOOOoO / o000O0o - I1ii11iIi11i - oOo0O0Ooo
  if 84 - 84: IIiIiII11i
  if 57 - 57: o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
  if 53 - 53: ii1ii11IIIiiI / oOo0O0Ooo * ii1ii11IIIiiI + I11i + o000O0o - I1ii11iIi11i
  if 16 - 16: oO0o % iiiiiiii1 . ooOoO0O00 / Ii1I - o0o00Oo0O
def ooiIi11i1I11Ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if 'ch' in url :
   o0OoO0000oOO ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Jizbox.png' , III1iII1I1ii + 'Jizbox.png' , '' )
def oo0OO0oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oO0OOoo0OO )
 OoOOooOOoo = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 for I1111i , url in OoOOooOOoo :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Next.png' , '' , '' )
def iIOoo000 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   I1111IiII1 ( url )
def IiiII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def iI1ii1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , IIII1iIIii in i1IIIII11I1IiI :
  if 'category' in url :
   o0OoO0000oOO ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   ' + IIII1iIIii + '[/COLOR]' , url , 90006 , o00O0O , III1iII1I1ii + 'Jizbox.png' , '' )
def OO00OO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OoOOooOOoo = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , o00O0O , '' , '' )
 for url in OoOOooOOoo :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , III1iII1I1ii + 'Next.png' , '' , '' )
def Ooii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   I1111IiII1 ( url )
def I1111IiII1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def O0oOOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , IIII1iIIii in i1IIIII11I1IiI :
  if 'category' in url :
   o0OoO0000oOO ( '[COLOR' + II + ']' + I1111i + '[COLORorange]' + IIII1iIIii + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def i11iII1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i111iI = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OoOOooOOoo = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , o00O0O , '' , '' )
 for url in OoOOooOOoo :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , i111iI + '/' + url , 90003 , III1iII1I1ii + 'Next.png' , '' , '' )
def oOooo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  i11iI1111ii1I ( 'http://www.perfectgirls.net' + url )
def i11iI1111ii1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( 'http://' + url )
def o0oI1Iii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , IIII1iIIii in i1IIIII11I1IiI :
  o0OoO0000oOO ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + IIII1iIIii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def oO00oO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OoOOooOOoo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in OoOOooOOoo :
  o0OoO0000oOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , IIII1iIIii in i1IIIII11I1IiI :
  o0OoO0000oOO ( ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + ( IIII1iIIii + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 89 - 89: Ii / o0o00Oo0O - ooOoO0O00 % I1ii11iIi11i + Ii
def ii1IO0oo00o000 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OoOOooOOoo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in OoOOooOOoo :
  o0OoO0000oOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , oOOo0ooO0 in i1IIIII11I1IiI :
  o0OoO0000oOO ( I1111i + '--' + ( oOOo0ooO0 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( o00O0O ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 5 - 5: Ii1I * ii1ii11IIIiiI % ooOOOoO % IIiIiII11i
  if 9 - 9: I11i % iiiiiiii1 + ooOOOoO
def ii111IIiiiiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , Oo0oOOooO0o0O , oOOO00o00 in i1IIIII11I1IiI :
  o0OoO0000oOO ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + oOOO00o00 + ' - [COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , o00O0O , o00O0O , oOOO00o00 + ' - ' + Oo0oOOooO0o0O )
 oooo0OOO00O00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in oooo0OOO00O00 :
  o0OoO0000oOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 15 - 15: ooOOOoO - Ii1I * I11i1ii1
def oo0OOoOo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iIi1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OoOOooOOoo = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in OoOOooOOoo :
  o0OoO0000oOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( iIi1 ) )
 for url , I1111i in i1IIIII11I1IiI :
  if '/c/' in url :
   o0OoO0000oOO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
   if 80 - 80: O0OOOoOoo0 + I11i1ii1 * I11i - IIiIiII11i - Ii1I
   if 95 - 95: ii1ii11IIIiiI % oOo0O0Ooo + I1ii11iIi11i * I11i * O0OOOoOoo0
def II1I1Ii11 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1iII1 = ( ii1I ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 o0OOoOoO00 = i1iII1 . lower ( )
 oOII1i1i1I1iII = 'http://www.xvideos.com/?k=' + o0OOoOoO00
 print oOII1i1i1I1iII + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0OOoo0OO = OoOooO ( oOII1i1i1I1iII )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , oO0o0 , I1111i , Oo0oOOooO0o0O , oOOO00o00 in i1IIIII11I1IiI :
  o0OoO0000oOO ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + oOOO00o00 + ' - [COLORred]' + Oo0oOOooO0o0O + '[/COLOR]' , 'http://www.xvideos.com' + oO0o0 , 10108 , o00O0O , o00O0O , oOOO00o00 + ' - ' + Oo0oOOooO0o0O )
 oooo0OOO00O00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for oO0o0 in oooo0OOO00O00 :
  o0OoO0000oOO ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oO0o0 , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
if 90 - 90: ii1ii11IIIiiI . I11i
if 11 - 11: o0o00Oo0O
if 96 - 96: O0OOOoOoo0 + I11i
if 10 - 10: Ii . ii . o0o00Oo0O % I11i1ii1 / oO0o
if 36 - 36: oOo0O0Ooo % ooOoO0O00 + oO0o
if 59 - 59: Ii - Ii + oOo0O0Ooo
if 4 - 4: I1ii11iIi11i * o0o00Oo0O - o000O0o % I11i1ii1 + OOooOOo
if 3 - 3: OOooOOo
if 91 - 91: o0o00Oo0O - ooOOOoO % iiiiiiii1
if 46 - 46: I11i1ii1 / oOo0O0Ooo . I1111IIi % oO0o / Ii
if 13 - 13: iiiiiiii1 % I11i + Ii1IIIi1 + iiiiiiii1 + Ii - Ii1I
if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
if 11 - 11: O0OOOoOoo0
if 20 - 20: ii1ii11IIIiiI . iiiiiiii1 % ii1ii11IIIiiI
if 5 - 5: Ii1IIIi1 + O0OOOoOoo0
if 23 - 23: iiiiiiii1 % iI11I1II1I1I . ooOOOoO
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
def o0Oo00oOOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   i1i11I1I1iii1 ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   i1i11I1I1iii1 ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in ooOoO00 :
  if 'http' in url :
   i1i11I1I1iii1 ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 49 - 49: I11i - iI11I1II1I1I
def o00oo00O0OoOo ( url ) :
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 if 6 - 6: Ii1I * I1ii11iIi11i + iI11I1II1I1I
 if 19 - 19: o0o00Oo0O % IIiIiII11i * I11i
def I1i1IiIIiIiII ( ) :
 if 27 - 27: ii * oOo0O0Ooo - O0OOOoOoo0 / O0OOOoOoo0
 if 21 - 21: o0o00Oo0O * I11i1ii1 % OOooOOo / o0o00Oo0O
 if 85 - 85: ii + ii
 if 23 - 23: ooOoO0O00
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / ooOOOoO . oO0o
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - I1111IIi
 if 50 - 50: oOo0O0Ooo - o000O0o + o000O0o * ooOOOoO + o000O0o
 if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
 if 30 - 30: OOooOOo - Ii
 if 94 - 94: OOooOOo % O0OOOoOoo0
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 8091 , III1iII1I1ii + 'gofish.png' )
def iI11ii ( url ) :
 oO0OOoo0OO = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  OOo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
def iIi1II111I1i1 ( url ) :
 oO0OOoo0OO = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 Iio0o0o = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O in Iio0o0o :
  o00O0O = o00O0O
 for url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  OOo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
  if 32 - 32: o0o00Oo0O / Ii1IIIi1 . I11i1ii1 % iiiiiiii1
def I1i1i1ii1iiI1 ( url ) :
 oO0OOoo0OO = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 73 - 73: iiiiiiii1
  if 25 - 25: I1111IIi
  if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
  if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . ii1ii11IIIiiI - I1ii11iIi11i . Ii
IIIII11II1 = '{PQ},' ; OOOO0oOO = '{SC},' ; IIIiii = '{XG},' ; I11OoooO = '{JP},' ; i1IIi11 = '{HW},' ; oOIIIII11 = '{RT},'
def iIII ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 O0OOOo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 oO0o0 = 'http://onlinemovies.tube/?s=' + ( ii1I ) . replace ( ' ' , '+' )
 i111iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 i11I1I1iiI = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 I1i1iii1Ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 O0O00OOo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OoOOo = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + ii1I
 iii1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 oOO0oo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 48 - 48: iiiiiiii1 / I11i1ii1 . iI11I1II1I1I
 iiO00O00O000OOO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 iIOo0O = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 72 - 72: ooOoO0O00 . I11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oO0o0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( i111iI )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( i11I1I1iiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( I1i1iii1Ii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 I1Ii11iiiI = O0o0O00Oo0o0 ( iI )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1II1IiIII111 = O0o0O00Oo0o0 ( OoOOo )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 IiiIi1IIII1i = O0o0O00Oo0o0 ( iii1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 O0ooOoO = O0o0O00Oo0o0 ( oOO0oo )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 3 - 3: OOooOOo % IIiIiII11i - o0o00Oo0O
 if 52 - 52: oO0o
 ooO00O00oOO = O0o0O00Oo0o0 ( iiO00O00O000OOO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 I1 = O0o0O00Oo0o0 ( iIOo0O )
 if 49 - 49: ii1ii11IIIiiI . Ii1I % I11i1ii1 . I1ii11iIi11i * Ii1IIIi1
 if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . I11i1ii1
 if 20 - 20: O0OOOoOoo0 + I11i . iiiiiiii1 / Ii
 if 7 - 7: OOooOOo / OOooOOo . iiiiiiii1 * o0o00Oo0O + I1111IIi + o000O0o
 if 98 - 98: IIiIiII11i * I1111IIi - oOo0O0Ooo % I11i - O0OOOoOoo0 % Ii1I
 if 69 - 69: ooOoO0O00 % oO0o % iiiiiiii1 / I11i1ii1 / I11i1ii1
 if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * I11i1ii1
 if 47 - 47: o0o00Oo0O
 if 55 - 55: oO0o % o0o00Oo0O / ii
 if 49 - 49: oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
 if 88 - 88: Ii1I * O0OOOoOoo0 + IIiIiII11i
 if 62 - 62: ii
 if 33 - 33: o0o00Oo0O . Ii % I11i
 if O0ooOoO != 'Failed' :
  IIiIiiiIIIIi1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0ooOoO )
  for oO0o0 , I1111i in IIiIiiiIIIIi1 :
   iIi11 = O0o0O00Oo0o0 ( oO0o0 )
   O00O0 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi11 )
   for iIiIiiiIi , i1iiIIi11I in O00O0 :
    i1iiIIi11I = ( i1iiIIi11I . replace ( '.' , ' ' ) )
    if o0OOoOoO00 in i1iiIIi11I . lower ( ) :
     if '.mkv' in iIiIiiiIi :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiIiiiIi , 222 , '' , '' , '' )
     elif '.mp4' in iIiIiiiIi :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiIiiiIi , 222 , '' , '' , '' )
     elif '.avi' in iIiIiiiIi :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiIiiiIi , 222 , '' , '' , '' )
     elif '.wav' in iIiIiiiIi :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiIiiiIi , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiIiiiIi , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 50 - 50: I11i1ii1
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for oO0o0 , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in i1I :
   if ii1I in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source Technica[/COLOR]' ) , oO0o0 , 222 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 83 - 83: Ii - oOo0O0Ooo * Ii
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for O0ooOo0 , I1111i in ooOoO00 :
   if ii1I in I1111i . lower ( ) :
    OOo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( i11I1I1iiI + O0ooOo0 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for oO0o0 , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in Iii1I1111ii :
   if ii1I in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source RaizTv[/COLOR]' ) , oO0o0 , 222 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 59 - 59: O0OOOoOoo0 - ii / I11i1ii1 + Ii1I . I11i - O0OOOoOoo0
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if I1Ii11iiiI != 'Failed' :
  oOo = [ ]
  Oo0000O0OOooO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1Ii11iiiI )
  for oO0o0 , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in Oo0000O0OOooO :
   if ii1I in I1111i . lower ( ) :
    if I1111i in oOo :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oO0o0 , 1016 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
     oOo . append ( I1111i )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if i1II1IiIII111 != 'Failed' :
  i1iIIIiiiI = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1II1IiIII111 )
  for oO0o0 , o00O0O , I1111i in i1iIIIiiiI :
   if ii1I in I1111i . lower ( ) :
    OOo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oO0o0 , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 29 - 29: o000O0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 26 - 26: o0o00Oo0O % Ii1IIIi1 - I1111IIi . Ii1IIIi1
    if 70 - 70: I11i + ooOOOoO / O0OOOoOoo0 + I11i1ii1 / oOo0O0Ooo
    if 33 - 33: ii . o0o00Oo0O
    if 59 - 59: iI11I1II1I1I
    if 45 - 45: o0o00Oo0O
    if 78 - 78: ooOOOoO - iI11I1II1I1I + iiiiiiii1 - Ii1I - iiiiiiii1
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
 if ooO00O00oOO != 'Failed' :
  oOo0OooOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO00O00oOO )
  for oO0o0 , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in oOo0OooOo :
   if ii1I in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source APPRENTICE[/COLOR]' ) , oO0o0 , 222 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 61 - 61: I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 22 - 22: iI11I1II1I1I / I11i1ii1 / oOo0O0Ooo - I11i
    if 21 - 21: o000O0o . Ii * ooOOOoO . Ii1IIIi1 / Ii1IIIi1
    if 42 - 42: ii / iiiiiiii1 . I11i / o0o00Oo0O - I1111IIi * I1111IIi
    if 1 - 1: ii1ii11IIIiiI % iiiiiiii1
    if 97 - 97: OOooOOo
    if 13 - 13: OOooOOo % Ii1IIIi1 . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
    if 19 - 19: iiiiiiii1 % I11i1ii1 - I11i1ii1 % oOo0O0Ooo . Ii1IIIi1 - ii
    if 100 - 100: oOo0O0Ooo + ii1ii11IIIiiI + I11i . ooOoO0O00 % ii
    if 64 - 64: o0o00Oo0O % ooOoO0O00 * iiiiiiii1 - ii1ii11IIIiiI + I1ii11iIi11i
    if 65 - 65: OOooOOo . Ii
 IiI1ii1Ii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 36 - 36: o000O0o * O0OOOoOoo0 + I1111IIi * O0OOOoOoo0 . Ii1I - iI11I1II1I1I
 for I1iii in IiI1ii1Ii :
  oOO0OO0O = O0Oo000ooO00 + I1iii + I1IIIii
  O0ooOoO = O0o0O00Oo0o0 ( oOO0OO0O )
  if O0ooOoO != 'Failed' :
   IIiIiiiIIIIi1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0ooOoO )
   for oO0o0 , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in IIiIiiiIIIIi1 :
    if ii1I in I1111i . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , oO0o0 , 222 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 14 - 14: ooOOOoO * o000O0o + Ii
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 84 - 84: O0OOOoOoo0 / IIiIiII11i
 IiI1ii1Ii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 86 - 86: oOo0O0Ooo
 if 97 - 97: IIiIiII11i
 for I1iii in IiI1ii1Ii :
  oOO0OO0O = O0OOOo + I1iii
  o0OOoo = O0o0O00Oo0o0 ( oOO0OO0O )
  if o0OOoo != 'Failed' :
   IiIiiI11i1Ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( o0OOoo )
   for O0ooOo0 , I1111i in IiIiiI11i1Ii :
    if ii1I in I1111i . lower ( ) :
     i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( O0OOOo + I1iii + O0ooOo0 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 38 - 38: oOo0O0Ooo
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 42 - 42: I11i
def O0oO0OOoOOO0oO ( ) :
 if 8 - 8: Ii / I11i1ii1
 if 33 - 33: iiiiiiii1 * I1111IIi - o0o00Oo0O + oOo0O0Ooo / I1111IIi
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 if 85 - 85: I1111IIi - I11i % Ii1IIIi1 - IIiIiII11i
 if 56 - 56: ii1ii11IIIiiI * Ii
 if 92 - 92: IIiIiII11i - o0o00Oo0O . iiiiiiii1
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
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 if 87 - 87: Ii1IIIi1 + Ii1IIIi1
 if 45 - 45: ooOoO0O00 - I1ii11iIi11i
 iIiIiiiIi = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( ii1I ) . replace ( ' ' , '+' )
 i111iI = 'http://onlinemovies.tube/?s=' + ( ii1I ) . replace ( ' ' , '+' )
 i11I1I1iiI = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 I1i1iii1Ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 O0O00OOo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 87 - 87: OOooOOo - oO0o * oO0o / ii1ii11IIIiiI . ooOOOoO * I11i
 iii1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 oOO0oo = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 iIi1iIIIiIiI = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 21 - 21: IIiIiII11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 29 - 29: OOooOOo % ii1ii11IIIiiI
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 7 - 7: ooOoO0O00 / I1111IIi / O0OOOoOoo0
 if 97 - 97: oO0o + iI11I1II1I1I
 III1I = O0o0O00Oo0o0 ( iIiIiiiIi )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( i111iI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( i11I1I1iiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( I1i1iii1Ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 o0OOoo = O0o0O00Oo0o0 ( O0O00OOo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 79 - 79: I11i1ii1 + o000O0o - IIiIiII11i . I1ii11iIi11i
 if 26 - 26: I1111IIi
 IiiIi1IIII1i = O0o0O00Oo0o0 ( iii1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 O0ooOoO = O0o0O00Oo0o0 ( oOO0oo )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 I11oOOooo = O0o0O00Oo0o0 ( iIi1iIIIiIiI )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 52 - 52: o0o00Oo0O + I11i1ii1
 if O0ooOoO != 'Failed' :
  IIiIiiiIIIIi1 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( O0ooOoO )
  for oO0o0 , I1111i in IIiIiiiIIIIi1 :
   iIi11 = O0o0O00Oo0o0 ( oO0o0 )
   O00O0 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( iIi11 )
   for iIiIiiiIi , i1iiIIi11I in O00O0 :
    if o0OOoOoO00 in i1iiIIi11I . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + i1iiIIi11I + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + iIiIiiiIi , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 11 - 11: ooOoO0O00 / iiiiiiii1 * Ii1I * iiiiiiii1 * I11i1ii1 - Ii
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if IiiIi1IIII1i != 'Failed' :
  I1III1II1I11 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiiIi1IIII1i )
  for oO0o0 , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in I1III1II1I11 :
   if o0OOoOoO00 in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source HeroVision[/COLOR]' ) , oO0o0 , 1016 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 96 - 96: Ii1I % Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 1 - 1: oOo0O0Ooo . ii1ii11IIIiiI
    if 26 - 26: o000O0o - I11i1ii1 % I1ii11iIi11i - o000O0o + I1111IIi
    if 33 - 33: ii1ii11IIIiiI + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * I1111IIi
    if 21 - 21: o0o00Oo0O * I11i1ii1 % oO0o
    if 14 - 14: o0o00Oo0O / iiiiiiii1 / I11i1ii1 + I1111IIi - I1111IIi
    if 10 - 10: o0o00Oo0O - Ii1I / iiiiiiii1 % OOooOOo / ii / ii1ii11IIIiiI
    if 73 - 73: I11i1ii1 + I1111IIi % I11i . Ii1I / Ii1IIIi1 . iiiiiiii1
    if 76 - 76: ooOOOoO . Ii1I * ii % O0OOOoOoo0
    if 24 - 24: ii
    if 83 - 83: o0o00Oo0O / oO0o
    if 62 - 62: ooOOOoO
 if I11oOOooo != 'Failed' :
  iI1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11oOOooo )
  for oO0o0 , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in iI1 :
   if o0OOoOoO00 in I1111i . lower ( ) :
    OOo ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] RaizTv[/COLOR]' , oO0o0 , 1016 , OOoOooOoOOOoo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 73 - 73: ii1ii11IIIiiI % oO0o * Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  I11Ii111I = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for oO0o0 , o00O0O , I1111i , Oo00OO0 in i1I :
   if o0OOoOoO00 in I1111i . lower ( ) :
    if 'season' in Oo00OO0 :
     OOo ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90054 , o00O0O , o00O0O , '' )
    if 'episodes' in Oo00OO0 :
     OOo ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90044 , o00O0O , o00O0O , '' )
  for oO0o0 in I11Ii111I :
   OOo ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 84 - 84: I1ii11iIi11i
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if III1I != 'Failed' :
  IIIIIiI = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( III1I )
  for oO0o0 , I1111i , o00O0O in IIIIIiI :
   if o0OOoOoO00 in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oO0o0 , 8022 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 18 - 18: ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 85 - 85: ii . oO0o . oO0o
    if 70 - 70: ooOOOoO
    if 72 - 72: iiiiiiii1 - I11i1ii1 - oOo0O0Ooo - O0OOOoOoo0 + Ii1IIIi1 - ooOoO0O00
    if 45 - 45: oO0o * oOo0O0Ooo
    if 61 - 61: O0OOOoOoo0 % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
    if 74 - 74: Ii1I * o000O0o + O0OOOoOoo0 % o0o00Oo0O
    if 18 - 18: ooOoO0O00 % I1111IIi . o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - IIiIiII11i
    if 55 - 55: OOooOOo . iI11I1II1I1I * Ii1IIIi1 % iI11I1II1I1I . oO0o
    if 43 - 43: ii1ii11IIIiiI . Ii1IIIi1 + oOo0O0Ooo * Ii
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for I1111i in ooOoO00 :
   if o0OOoOoO00 in I1111i . lower ( ) :
    OOo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( i11I1I1iiI + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 2 - 2: Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for I1111i in Iii1I1111ii :
   if o0OOoOoO00 in I1111i . lower ( ) :
    OOo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( I1i1iii1Ii + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 3 - 3: oOo0O0Ooo . O0OOOoOoo0 % o0o00Oo0O - I11i1ii1 / o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if o0OOoo != 'Failed' :
  IiIiiI11i1Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OOoo )
  for oO0o0 , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in IiIiiI11i1Ii :
   if o0OOoOoO00 in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] Source Scooby[/COLOR]' ) , oO0o0 , 1016 , OOoOooOoOOOoo , iIiiiii1i , Iio00 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 79 - 79: ii1ii11IIIiiI + o000O0o % I11i1ii1 % oOo0O0Ooo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
 ooOO0o = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for I1iii in ooOO0o :
  oOO0OO0O = O0Oo000ooO00 + I1iii + I1IIIii
  ooO00O00oOO = O0o0O00Oo0o0 ( oOO0OO0O )
  if ooO00O00oOO != 'Failed' :
   oOo0OooOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( ooO00O00oOO )
   for I1111i , Iio00 , oO0o0 , o00O0O , o0ooooO0o0O , i1i1iII1 in oOo0OooOo :
    if o0OOoOoO00 in I1111i . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , oO0o0 , i1i1iII1 , o00O0O , o0ooooO0o0O , Iio00 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 53 - 53: O0OOOoOoo0 . o000O0o / I1ii11iIi11i . oO0o . Ii
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 60 - 60: IIiIiII11i
     if 25 - 25: I1ii11iIi11i + I11i - oO0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oooI11Ii1 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( ii1I ) . replace ( ' ' , '+' )
 if 63 - 63: ooOoO0O00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oO0o0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 42 - 42: o000O0o - Ii % o000O0o - iiiiiiii1 * o0o00Oo0O / IIiIiII11i
 if oO0OOoo0OO != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oO0o0 , I1111i in i1I :
   if ii1I in I1111i . lower ( ) :
    i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oO0o0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 5 - 5: I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
oOoOo0o0 = '{ZH},' ; II1Iiiii = '{IX},' ; OoO00 = '{LM},'
if 41 - 41: ooOoO0O00
def I1Iii1 ( url ) :
 Ii1II111iIi = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( Ii1II111iIi )
 for url , OoOOOo0o0ooo , oOOOoo0o , I1111i in i1IIIII11I1IiI :
  OOo ( ( OoOOOo0o0ooo ) . replace ( 'Sezon' , ' Season ' ) + ( oOOOoo0o ) . replace ( 'Bölüm' , ' Episode ' ) + I1111i , url , 8063 , '' )
  if 68 - 68: IIiIiII11i % iiiiiiii1 * Ii
  if 9 - 9: IIiIiII11i + Ii1I / O0OOOoOoo0
  if 51 - 51: ooOOOoO % Ii1I + ii - oOo0O0Ooo * OOooOOo * O0OOOoOoo0
  if 7 - 7: Ii1IIIi1 . I1111IIi . iiiiiiii1 / ii1ii11IIIiiI / I1ii11iIi11i
def o0Ooo ( url ) :
 Ii1II111iIi = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( Ii1II111iIi )
 for url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( I1111i , url , 222 , '' )
  if 11 - 11: Ii1I
  if 53 - 53: I11i % ii - o000O0o - ooOoO0O00 / oO0o
  if 33 - 33: I1111IIi * ooOOOoO
  if 96 - 96: I11i - oOo0O0Ooo % OOooOOo + oO0o - I1111IIi - I1111IIi
def i1ii1iiI1iI ( ) :
 if 48 - 48: IIiIiII11i / iI11I1II1I1I * oO0o % o000O0o . ooOoO0O00
 Ii1II111iIi = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( Ii1II111iIi )
 for oO0o0 , o00O0O , I1111i , oOOOoo0o in i1IIIII11I1IiI :
  OOo ( I1111i + '  -  ' + ( oOOOoo0o ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oO0o0 , 8063 , o00O0O )
  if 37 - 37: o0o00Oo0O . o0o00Oo0O / I11i . IIiIiII11i % I11i
def i1I1Ii1 ( ) :
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i , o00O0O in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 8002 , o00O0O )
def OoOOOo00 ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , time , url , I1111i , oO00OoO0oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '%s %s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , time ) , url , 1015 , o00O0O , oO00OoO0oo )
  if 86 - 86: oO0o - ooOOOoO
def OOOOO0o0oo0 ( ) :
 if 2 - 2: ii
 OOo ( 'Coronation Street' , '' , 8001 , '' )
 OOo ( 'Eastenders' , '' , 8002 , '' )
 OOo ( 'Emmerdale' , '' , 8003 , '' )
 OOo ( 'Hollyoaks' , '' , 8004 , '' )
 OOo ( 'Im a Celebrity' , '' , 8005 , '' )
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
 if 46 - 46: o0o00Oo0O % ii
 if 22 - 22: O0OOOoOoo0 + ii - OOooOOo - oO0o * iiiiiiii1 - o000O0o
 if 99 - 99: I11i1ii1 / oOo0O0Ooo . ii1ii11IIIiiI - ii1ii11IIIiiI * oOo0O0Ooo
def I1IIiIIiiI1i ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Holly' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oO0o0 :
    i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 83 - 83: Ii1I * IIiIiII11i . iiiiiiii1 - ooOOOoO
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 46 - 46: oO0o % Ii1I
def OO00O0O ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'East' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oO0o0 :
    i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 76 - 76: ii1ii11IIIiiI % o0o00Oo0O * iI11I1II1I1I - Ii1I % o000O0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: Ii1I
def II1111i11i11 ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Emmer' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oO0o0 :
    i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 43 - 43: o0o00Oo0O * Ii - ii - o000O0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 46 - 46: o000O0o * ooOoO0O00 / Ii1I
def ooO0O0OOO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Coro' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oO0o0 :
    i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 2 - 2: Ii / oO0o + I11i1ii1 - Ii1I * oO0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 3 - 3: oO0o % I11i % Ii1IIIi1 . Ii1I . Ii1I
def IiI1i1111iI1i ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Celeb' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oO0o0 :
    i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 85 - 85: iI11I1II1I1I + ii1ii11IIIiiI - IIiIiII11i * I1111IIi * O0OOOoOoo0
def I1OO0o0OoooO00 ( name , url ) :
 IiIiIi = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IiIiIi :
  ooOoOO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIIII = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( iIIII ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIIII = open_url ( url )
  iiiiIIii1I = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( iIIII ) [ - 1 ]
  ooOoOO = iiiiIIii1I . replace ( '\\/' , '/' )
 i111iiI1ii = xbmcgui . ListItem ( name , '' , '' )
 i111iiI1ii . setPath ( ooOoOO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i111iiI1ii )
 if 14 - 14: Ii1IIIi1 * oOo0O0Ooo - Ii1I
 if 10 - 10: O0OOOoOoo0 % iiiiiiii1 * Ii1I * o0o00Oo0O * Ii % iiiiiiii1
def ooOoo0O0o0OO0 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oO0o0 , 7071 , III1iII1I1ii + 'popcorn.png' )
 for oO0o0 , I1111i in i1I :
  OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oO0o0 , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 47 - 47: iiiiiiii1 * Ii1IIIi1
def iiI11iIIiI1IiI1iIi1 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Movies' in I1111i :
   OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( oO0o0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def iIiiI11II11 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 for url in i1I :
  OOo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 75 - 75: iiiiiiii1 - O0OOOoOoo0 . o000O0o
  if 88 - 88: O0OOOoOoo0 - ii . I11i1ii1 - I11i / OOooOOo % ooOOOoO
def I1i11i ( url ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in i1IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , o00O0O )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
o00O00o = '{UJ},' ; ooO0 = '{WE},' ; O00O0O0 = '{WP},' ; ii1IiIi1iIi = '{PP},'
def IIiI111Iii ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in i1IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOiIiI1iI ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  ooo0oooO ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooo0oooO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 73 - 73: I11i1ii1 - Ii1IIIi1 - IIiIiII11i - iI11I1II1I1I
 if 89 - 89: I11i % o000O0o - IIiIiII11i
 if 46 - 46: O0OOOoOoo0 + Ii1IIIi1 * I1ii11iIi11i + ii
def oo0OoOIiI1IIIiI1I1i ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '(cooltvseries.com)' in I1111i :
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , I1111i in i1I :
  if '(cooltvseries.com)' in I1111i :
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def oO00O0oO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( ( url ) . replace ( ' ' , '%20' ) )
O00O00 = '{XX},' ; IIi1i = '{UD},' ; o0ooOOOo0O = '{YT},' ; i11111i1I1IiI = '{JS},' ; Ii111i1I1i1i = '{PF},'
if 70 - 70: Ii1IIIi1 - I1111IIi . iiiiiiii1
def IiII11 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i , o00O0O in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oO0o0 ) ) , 222 , o00O0O )
  if 56 - 56: oOo0O0Ooo
def IiI1 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  if 'youtu' in url :
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + o00O0O )
 for url in next :
  OOo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 49 - 49: ooOoO0O00 % o000O0o / Ii1IIIi1 . Ii1I - iiiiiiii1
def iiI1Iii ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 84 - 84: oOo0O0Ooo / OOooOOo
def i1IO0OoO0o ( url ) :
 iIIII = OoOooO
 i1IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , o00O0O )
  if 96 - 96: Ii1IIIi1 * o000O0o
  if 11 - 11: Ii % OOooOOo + iiiiiiii1 - Ii1I . o0o00Oo0O + ooOOOoO
  if 14 - 14: iI11I1II1I1I / I11i * I1111IIi
  if 35 - 35: iI11I1II1I1I
  if 34 - 34: oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
def iII11II ( ) :
 if 59 - 59: oOo0O0Ooo % o000O0o % iI11I1II1I1I / iiiiiiii1 * O0OOOoOoo0 * oO0o
 OOo ( 'All Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'Entertainment' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'Movies' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'Music' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'News' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'Sports' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'Documentary' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'Kids' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'Food' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'Religious' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'USA Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 OOo ( 'Other' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 if 34 - 34: I1111IIi
 if 89 - 89: O0OOOoOoo0
def ii1i11111 ( Cat_Name ) :
 if 7 - 7: oOo0O0Ooo
 iIiii1III = False
 o00oOOO = '0'
 if Cat_Name == 'All Channels' : iIiii1III = True
 if Cat_Name == 'Entertainment' : o00oOOO = '1'
 if Cat_Name == 'Movies' : o00oOOO = '2'
 if Cat_Name == 'Music' : o00oOOO = '3'
 if Cat_Name == 'News' : o00oOOO = '4'
 if Cat_Name == 'Sports' : o00oOOO = '5'
 if Cat_Name == 'Documentary' : o00oOOO = '6'
 if Cat_Name == 'Kids' : o00oOOO = '7'
 if Cat_Name == 'Food' : o00oOOO = '8'
 if Cat_Name == 'Religious' : o00oOOO = '9'
 if Cat_Name == 'USA Channels' : o00oOOO = '10'
 if Cat_Name == 'Other' : o00oOOO = '11'
 if 95 - 95: Ii . I11i + ii % I1ii11iIi11i
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIII )
 print 'Len Match: >>>' + str ( len ( i1IIIII11I1IiI ) )
 for I1111i , o00O0O , I1iI11ii in i1IIIII11I1IiI :
  iiiiIiiiii1I = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  if I1iI11ii == o00oOOO :
   OOo ( I1111i , '' , 7022 , iiiiIiiiii1I )
  elif iIiii1III == True :
   OOo ( I1111i , '' , 7022 , iiiiIiiiii1I )
  else : pass
  if 3 - 3: OOooOOo
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 52 - 52: OOooOOo
def Oo0OOOO ( Search_Name ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , oO0o0 , i111iI , i11I1I1iiI in i1IIIII11I1IiI :
  iiiiIiiiii1I = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  i1i11I1I1iii1 ( Search_Name + ': Link 1' , ( oO0o0 ) . replace ( '\\' , '' ) , 222 , iiiiIiiiii1I )
  i1i11I1I1iii1 ( Search_Name + ': Link 2' , ( i111iI ) . replace ( '\\' , '' ) , 222 , iiiiIiiiii1I )
  i1i11I1I1iii1 ( Search_Name + ': Link 3' , ( i11I1I1iiI ) . replace ( '\\' , '' ) , 222 , iiiiIiiiii1I )
  if 87 - 87: o000O0o / ii1ii11IIIiiI - OOooOOo % Ii1I * I1ii11iIi11i % I11i
def iIio00O000ooOO ( ) :
 iIIII = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def O000OOOoOooO ( ) :
 iIIII = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def o0oOoOOO ( ) :
 iIIII = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 74 - 74: O0OOOoOoo0 / iiiiiiii1 / IIiIiII11i - O0OOOoOoo0 / o000O0o % ooOOOoO
def i1Iiiiii1II ( url ) :
 url
 i11I = xbmcgui . ListItem ( I1111i , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11I )
 return
 if 50 - 50: OOooOOo
 if 90 - 90: Ii1I - iiiiiiii1
def i1i1I11Ii1i ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIIII )
 for url , Iio00 , o00O0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + o00O0O , '' , ( Iio00 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  OOo ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 56 - 56: I1111IIi * I11i - oOo0O0Ooo - ooOoO0O00
def OOoOOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iio00 , o00O0O in i1IIIII11I1IiI :
  OOiIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + o00O0O , '' , Iio00 )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 o00OOo0o = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0ooo0O00Ooo0 in o00OOo0o :
  o000O0O = ( O0ooo0O00Ooo0 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiOOooooO0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + o00O0O , '' , o000O0O )
  if 17 - 17: I1111IIi % I1111IIi
def i11IIiiI ( INFO ) :
 OO0O000 ( 'info for workout' , INFO )
 if 66 - 66: o000O0o / Ii / OOooOOo + Ii1I / o0o00Oo0O
 if 97 - 97: Ii
 if 16 - 16: ooOoO0O00
def IIIIiI1iiI ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  OOo ( ( I1111i ) . replace ( 'SlyNet' , '' ) , url , 9031 , III1iII1I1ii + 'Sport.png' )
def i1IO00oO0oOOOOOO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , url , 9032 , III1iII1I1ii + 'icon.png' )
def Oo0ooo00OoO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   i1i11I1I1iii1 ( ( I1111i ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , III1iII1I1ii + 'icon.png' )
def Iiii1I1I111i1 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   i1i11I1I1iii1 ( I1111i , url , 222 , III1iII1I1ii + 'icon.png' )
   if 66 - 66: Ii1IIIi1 / iI11I1II1I1I - OOooOOo % o0o00Oo0O . I11i1ii1
   if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
   if 37 - 37: ooOoO0O00 * Ii
def Oo00OOooOoO ( url ) :
 i1i11I1I1iii1 ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 i1i11I1I1iii1 ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 OOo ( '[COLOR' + II + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , III1iII1I1ii + 'bamf.png' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   pass
  else :
   i1i11I1I1iii1 ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1iiiiI1Ii11 ( url ) :
 i1i11I1I1iii1 ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 i1i11I1I1iii1 ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 OOo ( '[COLOR' + II + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , III1iII1I1ii + 'bamf.png' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   i1i11I1I1iii1 ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 69 - 69: ooOOOoO / ooOoO0O00 / o000O0o . iiiiiiii1
 if 41 - 41: o000O0o * I1111IIi + oOo0O0Ooo
 if 7 - 7: I11i1ii1 % oO0o + ii
def i1ii11Iii11 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 i1IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'Daily' in I1111i :
   OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 9008 , Oo00OOOOO )
def o0ooOO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOo ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def OOoo000Ooo ( url ) :
 i1i11I1I1iii1 ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 i1i11I1I1iii1 ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 i1i11I1I1iii1 ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , Oo00OOOOO )
  if 46 - 46: ooOoO0O00 + o0o00Oo0O
def IIii1i ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if '.m3u' in oO0o0 :
   OOo ( ( I1111i ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oO0o0 ) , 9011 , III1iII1I1ii + 'disclose.png' )
def ooOOOOOo ( url ) :
 iIIII = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 3 - 3: Ii
def O0O0Oo00 ( ) :
 iIIII = OoOooO ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  if 'category' in oO0o0 :
   OOo ( I1111i , 'http://www.disclose.tv/' + oO0o0 , 7010 , III1iII1I1ii + 'disclose.png' )
   if 20 - 20: ooOoO0O00 * O0OOOoOoo0 + oO0o * oO0o / I1ii11iIi11i
   if 83 - 83: Ii1I
def OOo0OOooO0 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  OOo ( I1111i , 'http://www.disclose.tv/' + url , 7011 , o00O0O )
 for url in next :
  OOo ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 80 - 80: Ii1I
  if 67 - 67: IIiIiII11i
def II1i111Ii ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   i1i11I1I1iii1 ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , I1111i in i1I :
  i1i11I1I1iii1 ( I1111i , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in ooOoO00 :
  i1i11I1I1iii1 ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 1 - 1: o0o00Oo0O * ii1ii11IIIiiI
  if 5 - 5: O0OOOoOoo0 - O0OOOoOoo0 / iiiiiiii1 % I1ii11iIi11i
def OOoO00OOo ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 42 - 42: ooOoO0O00 . Ii / OOooOOo
def iii1OO00Oo00o ( name , url , img ) :
 oO0OOoo0OO = OoOooO ( url )
 IiII1Iiii = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 I1o000o00OO00Oo = len ( IiII1Iiii )
 if 12 - 12: ooOOOoO * o000O0o - iiiiiiii1 * O0OOOoOoo0 - I11i1ii1 * iiiiiiii1
 if 90 - 90: ii1ii11IIIiiI . OOooOOo
 if I1o000o00OO00Oo == 1 :
  for o0OOOOoo in IiII1Iiii :
   o0OOOOoo = o0OOOOoo . replace ( 'player' , 'watch' )
   oOi1IiIiIii11I = o0OOOOoo + '&fv=&sou='
   O0o0O00 = OoOooO ( oOi1IiIiIii11I )
   OoI11II = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( O0o0O00 )
   for O0oO in OoI11II :
    Iii11IiIi = False
    Resolve ( O0oO )
    if 94 - 94: Ii1IIIi1 * ii - I1111IIi - iiiiiiii1
 elif I1o000o00OO00Oo > 1 :
  if 71 - 71: I1ii11iIi11i - ooOoO0O00
  for o0OOOOoo in IiII1Iiii :
   IIiI = OoOooO ( o0OOOOoo )
   iI11IIiII1iII = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( IIiI )
   OooO00OOOOoo = iI11IIiII1iII
   OooO00OOOOoo = ( str ( OooO00OOOOoo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + OooO00OOOOoo
   i1i11I1I1iii1 ( 'DOUBLE LINK' , OooO00OOOOoo , 424 , '' )
   if 22 - 22: ii1ii11IIIiiI - I1ii11iIi11i % Ii1I % I11i1ii1 % I1111IIi
   for url in iI11IIiII1iII :
    OOo ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     i111iI = Google . resolve ( url )
    except :
     pass
    try :
     o00OoOoo0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( i111iI ) )
     for iiiiiiiiiiiI , iI111iiI1II in o00OoOoo0 :
      if 96 - 96: OOooOOo * o0o00Oo0O - IIiIiII11i . I11i1ii1 - ii1ii11IIIiiI
      HD_URLS . append ( iiiiiiiiiiiI )
      SD_URLS . append ( iI111iiI1II )
    except :
     pass
 else :
  pass
  if 84 - 84: o000O0o * I11i * I11i - O0OOOoOoo0
def III1Ii ( ) :
 if 90 - 90: oOo0O0Ooo
 if 27 - 27: iI11I1II1I1I - o000O0o
 OOo ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 73 - 73: Ii1IIIi1 . I1ii11iIi11i + I1ii11iIi11i % I1ii11iIi11i % o0o00Oo0O
 OOo ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 8 - 8: O0OOOoOoo0 . ii1ii11IIIiiI - ooOoO0O00 % oO0o / ooOOOoO
 if 13 - 13: I1ii11iIi11i / OOooOOo . Ii1I . Ii1IIIi1
def iIiiII11 ( ) :
 iIIII = OoOooO ( 'http://cnfstudio.com/' )
 i1IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , 'http://cnfstudio.com/genre/' + oO0o0 , 7003 , III1iII1I1ii + 'icon.png' )
  if 75 - 75: OOooOOo + ii1ii11IIIiiI . Ii / ii1ii11IIIiiI
OOooO0OOoo = xbmcgui . Dialog ( )
if 32 - 32: ii1ii11IIIiiI + I1111IIi + Ii1I
oo00o = '{UN},' ; I1111iII = '{IG},' ; Ii11 = '{PL},' ; ii11 = '{LO},' ; III1IIii1i = '{LP},' ; I1IIIi11 = '{HA},' ; iI11i1iI = '{XD},' ; oo0O0Ooo0o0 = '{TA},' ; oo0OoOOO = '{DP},' ; o0OOoOoo = '{JT},' ; O0O00o0O = '{JJ},' ; iIii1i1i1 = '{MM},' ; I111I1iI1 = '{FQ},' ; oO0OoOooO0O = '{HH},'
if 7 - 7: I1ii11iIi11i - Ii / o000O0o / o000O0o . ooOoO0O00 % ooOOOoO
def oo00o0000 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIIII )
 OOo00O = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , o00O0O )
 OOo00O = OOo00O
 for url in OOo00O :
  OOo ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 18 - 18: I11i1ii1 * IIiIiII11i
def IIIi ( url ) :
 if 61 - 61: Ii1I % Ii
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1i = url + '&fv=&sou='
  i1i = i1i . replace ( 'player' , 'watch' )
  O0oOoOOO000 = oOo00o0oO ( i1i )
  iIiIi = oOo00o0oO ( url )
  if 9 - 9: ooOOOoO - IIiIiII11i + iiiiiiii1 / o000O0o % Ii1I
  if 17 - 17: iI11I1II1I1I - I11i1ii1
def oOo00o0oO ( url ) :
 if 99 - 99: I1ii11iIi11i + iiiiiiii1 % I11i1ii1 - I11i
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  Oo ( url )
  if 52 - 52: Ii1I
  if 93 - 93: O0OOOoOoo0 . Ii
def I1i1IO0OOoooO ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , III1iII1I1ii + 'LocalM3U.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , III1iII1I1ii + 'RemoteM3U.png' , O0o0Oo , '' )
 if 80 - 80: ooOoO0O00 * Ii1I
def OoOoOO00O ( ) :
 if os . path . exists ( iiI1IiI ) :
  iI11ii1i1IiI = open ( iiI1IiI , 'r' )
  for i11I in iI11ii1i1IiI :
   OOOoo0O00OooO = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( i11I )
   for I1111i , oO0o0 in OOOoo0O00OooO :
    i1i11I1I1iii1 ( I1111i , oO0o0 , 222 , III1iII1I1ii + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 92 - 92: o0o00Oo0O . O0OOOoOoo0
def o0OoO ( url ) :
 if os . path . exists ( Remote ) :
  oO0OOoo0OO = I1iIi1iIiiIiI ( url )
  i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1111i , url in i1IIIII11I1IiI :
   url = ( url ) . strip ( )
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 93 - 93: OOooOOo % Ii - ii1ii11IIIiiI % oO0o
  if 55 - 55: I11i . Ii1I
def Iiii1i1 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oO0o0 in i1IIIII11I1IiI :
  oO0o0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oO0o0
 I1111i = 'plugin.video.GenieTv'
 if 63 - 63: o000O0o
 OOOOoO0O ( oO0o0 , I1111i )
 if 79 - 79: Ii
def i1IiiiI1iI ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oO0o0 in i1IIIII11I1IiI :
  oO0o0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oO0o0
 I1111i = 'repository.GenieTv'
 if 81 - 81: O0OOOoOoo0 + I1111IIi - Ii
 OOOOoO0O ( oO0o0 , I1111i )
 if 60 - 60: iiiiiiii1
 if 14 - 14: I1ii11iIi11i % o000O0o * O0OOOoOoo0 - Ii / Ii1I * Ii
def iI1i11iII111 ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OooOOo ( )
 if i11I1II1I11i == 1 :
  o00ooO0 ( )
  if 10 - 10: Ii1I * o000O0o / iiiiiiii1 - ii + iI11I1II1I1I
  if 95 - 95: oO0o - I1111IIi % iiiiiiii1
  if 27 - 27: iI11I1II1I1I / oOo0O0Ooo % OOooOOo / oOo0O0Ooo * ii1ii11IIIiiI
  if 13 - 13: O0OOOoOoo0 . O0OOOoOoo0 + Ii % o0o00Oo0O % iiiiiiii1 + I1111IIi
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
Iii1Iiio0ooO00o00 = 'https://addons.tvaddons.ag/'
if 25 - 25: oO0o
def o00ooO0 ( ) :
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 oOII1i1i1I1iII = 'https://addons.tvaddons.ag/search/?keyword=' + o0OOoOoO00
 oO0OOoo0OO = OoOooO ( oOII1i1i1I1iII )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for oO0o0 , iii11i1IIII , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , oO0o0 , 10054 , 'https://addons.tvaddons.ag/' + iii11i1IIII , O0o0Oo , '' )
  if 39 - 39: ii1ii11IIIiiI * OOooOOo + I1ii11iIi11i . Ii1IIIi1 - o0o00Oo0O * Ii1I
  if 98 - 98: I1111IIi * O0OOOoOoo0 . ii . o0o00Oo0O
def OooOOo ( ) :
 oO0OOoo0OO = OoOooO ( Iii1Iiio0ooO00o00 )
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
   if 89 - 89: O0OOOoOoo0 / o0o00Oo0O % ii - o0o00Oo0O . oO0o
   if 32 - 32: I11i1ii1
def Addon ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 IiI1Iii1iIIII = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'Please' in I1111i :
   pass
  else :
   OOiIiIIi1 ( I1111i , url , 10054 , 'https://addons.tvaddons.ag/' + o00O0O , O0o0Oo , '' )
 for url in IiI1Iii1iIIII :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
  if 87 - 87: IIiIiII11i . ii1ii11IIIiiI * oO0o
  if 74 - 74: I11i % OOooOOo . O0OOOoOoo0 % iiiiiiii1 . o0o00Oo0O % IIiIiII11i
def iIiiIi11 ( url , name ) :
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
   if 73 - 73: I1111IIi - I1111IIi / ii
def OOOOoO0O ( url , name ) :
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
 if 53 - 53: I11i / oO0o . ii
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 55 - 55: I1111IIi * I11i * I11i1ii1 - ooOoO0O00 / ii1ii11IIIiiI * o000O0o
 if 85 - 85: Ii . oO0o + oO0o
def iIIIIi ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , iii11i1IIII , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , url , 1007 , iii11i1IIII )
def IIi1iI11I ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , iii11i1IIII , I1111i in i1IIIII11I1IiI :
  OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , iii11i1IIII )
  if 61 - 61: o0o00Oo0O . ii1ii11IIIiiI . o0o00Oo0O * Ii * IIiIiII11i / iiiiiiii1
  if 69 - 69: ooOOOoO
def oOIIiIi ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , iconimage , Iio00 , o0ooooO0o0O , name in i1IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    o00o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
    for i11I in o00o :
     if i11I == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    II1iOOoOooO0o ( name , url , 1016 , iconimage , o0ooooO0o0O , Iio00 )
   else :
    if 'youtube' in url :
     o00o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for i11I in o00o :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     OOoiII1I1i ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , o0ooooO0o0O , Iio00 )
    else :
     o00o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for i11I in o00o :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     OOoiII1I1i ( name , url , 222 , iconimage , o0ooooO0o0O , Iio00 )
     I1I11i ( 'tvshows' , 'Media Info 3' )
  else :
   iIi111iiii ( url , iconimage , name )
   if 14 - 14: ii1ii11IIIiiI / I1111IIi - o0o00Oo0O
 else :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
  for url , iii11i1IIII , name in i1IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     OOo ( name , url , 1016 , iii11i1IIII )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      i1i11I1I1iii1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iii11i1IIII )
     else :
      o00o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for i11I in o00o :
       if i11I == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      i1i11I1I1iii1 ( name , url , 222 , iii11i1IIII )
      I1I11i ( 'tvshows' , 'Media Info 3' )
   else :
    iIi111iiii ( url , iii11i1IIII , name )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 16 - 16: iiiiiiii1 % iI11I1II1I1I . ooOoO0O00
def iIi111iiii ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 o0O0oOOoo0O0 = ( url ) . replace ( II1Iiiii , 'http' ) . replace ( IIi1i , '.com' ) ;
 OO00OOo = ( o0O0oOOoo0O0 ) . replace ( OoO00 , 'a' ) . replace ( IIIiii , 'b' ) . replace ( I11OoooO , 'c' ) . replace ( ooO0 , 'd' ) . replace ( Ii11 , 'e' ) . replace ( o0OOoOoo , 'f' ) ;
 IiI11i1IiI1 = ( OO00OOo ) . replace ( O00O00 , 'g' ) . replace ( I1IIIi11 , 'h' ) . replace ( o0ooOOOo0O , 'i' ) . replace ( Ii111i1I1i1i , 'j' ) . replace ( i1IIi11 , 'k' ) . replace ( oOIIIII11 , 'l' ) ;
 o00oOO00 = ( IiI11i1IiI1 ) . replace ( o00O0oOOo , 'm' ) . replace ( i1OOO00oO0O , 'n' ) . replace ( IIi1 , 'o' ) . replace ( OOoO0OooO , 'p' ) . replace ( IiiOo , 'q' ) . replace ( iiiIiii11i1i , 'r' ) ;
 ooo0O0Oo0O = ( o00oOO00 ) . replace ( Oo0o , 's' ) . replace ( O00O0O0 , 't' ) . replace ( i1iOO00O0O00oOOO , 'u' ) . replace ( ii1111iIIiIIi , 'v' ) . replace ( ooOo0Oo , 'w' ) . replace ( I11i1I111II1IiI , 'x' ) ;
 oo00O0oOo = ( ooo0O0Oo0O ) . replace ( IiI1Ii , 'y' ) . replace ( oOO00o0oooOo0 , 'z' ) . replace ( oo00o , '.' ) . replace ( I1111iII , '(' ) . replace ( ii11 , ')' ) . replace ( III1IIii1i , '/' ) ;
 iIII1iIi = ( oo00O0oOo ) . replace ( oOoOo0o0 , '1' ) . replace ( ii1IiIi1iIi , '2' ) . replace ( iiii1Ii , '3' ) . replace ( oo0O0Ooo0o0 , '4' ) . replace ( oo0OoOOO , '5' ) . replace ( i11111i1I1IiI , '6' ) ;
 IIiiiI = ( iIII1iIi ) . replace ( O0O00o0O , '7' ) . replace ( iIii1i1i1 , '8' ) . replace ( I111I1iI1 , '9' ) . replace ( oO0OoOooO0O , '0' ) . replace ( IIIII11II1 , ':' ) . replace ( OOOO0oOO , '%' ) ;
 url = ( IIiiiI ) . replace ( o00O00o , '-' ) . replace ( iI11i1iI , '_' ) ;
 i1i11I1I1iii1 ( name , url , 222 , iconimage ) ;
 if 2 - 2: ooOoO0O00
 if 6 - 6: ooOoO0O00 % ooOOOoO . I1111IIi + I1111IIi . ooOOOoO / Ii
def oOoi1I1i1II1i ( ) :
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for oO0o0 , iii11i1IIII , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , oO0o0 , 1007 , iii11i1IIII )
def ooI111II ( url ) :
 if 61 - 61: ooOOOoO . iI11I1II1I1I - IIiIiII11i % ooOOOoO * o0o00Oo0O % I1ii11iIi11i
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , iii11i1IIII , I1111i in i1IIIII11I1IiI :
  OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , iii11i1IIII )
  if 17 - 17: ooOoO0O00 % OOooOOo . I1ii11iIi11i - Ii1I
def I1I11I11iIII ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O0oO0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O0oO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0oO0 )
 if 31 - 31: IIiIiII11i % Ii1IIIi1
 if 45 - 45: Ii1IIIi1 * ii - ooOoO0O00
def IIiiiI1iI ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  if '-dir-' in I1111i :
   OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , o00O0O )
  else :
   OOo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , o00O0O )
   if 42 - 42: o000O0o
def iiioooOo ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 o0oo00O0O = ( 'http://afewbitsmore.com/' )
 i1IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '[To Parent Directory]' in I1111i :
   I1111i = 'HOME'
   pass
  elif 'HOME' in I1111i :
   pass
  elif '.m3u' in I1111i :
   OOo ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , o0oo00O0O + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in I1111i :
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , o0oo00O0O + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in I1111i :
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , o0oo00O0O + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , o0oo00O0O + url , 1012 , III1iII1I1ii + 'music.png' )
def II11iii1iI1ii ( url ) :
 oO0OOoo0OO = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , III1iII1I1ii + 'music.png' )
  if 34 - 34: I11i1ii1 . I11i1ii1
def OOoOi11i ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 o0oo00O0O = url
 i1IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '.mp3' in I1111i :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   OOo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/' , '' ) , o0oo00O0O + url , 1011 , III1iII1I1ii + 'music.png' )
def IIII1II11Iii ( ) :
 iIIII = I1iIi1iIiiIiI ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , ( 'http://www.cyn.net/music/' + oO0o0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + o00O0O ) . replace ( ' ' , '%20' ) )
def I1i11I1IiII1 ( url , img ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i111iI = url
 img = img
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( i111iI + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 40 - 40: I11i - o0o00Oo0O * IIiIiII11i / oOo0O0Ooo . I11i + iiiiiiii1
def iiIiII ( url ) :
 iIIII = I1iIi1iIiiIiI ( url )
 i111iI = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for type , url , I1111i in i1IIIII11I1IiI :
  if '[VID]' in type :
   i1i11I1I1iii1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , i111iI + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   iiIiII ( i111iI + url )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: iiiiiiii1 * o0o00Oo0O / ii1ii11IIIiiI + oOo0O0Ooo - Ii1I * I1ii11iIi11i
 if 85 - 85: ooOoO0O00 * OOooOOo
def O0O0 ( ) :
 O0OOOo = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 ii1I = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0OOoOoO00 = ii1I . lower ( )
 oO0o0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 iIiIiiiIi = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 i111iI = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 99 - 99: I1ii11iIi11i
 oO0OOoo0OO = O0o0O00Oo0o0 ( oO0o0 )
 III1I = O0o0O00Oo0o0 ( iIiIiiiIi )
 O0 = O0o0O00Oo0o0 ( i111iI )
 if 72 - 72: I1ii11iIi11i / IIiIiII11i * I11i1ii1 * Ii1I - I1111IIi / iiiiiiii1
 if oO0OOoo0OO != 'Failed' :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oO0o0 , OOoOooOoOOOoo , Iio00 , iIiiiii1i , I1111i in i1IIIII11I1IiI :
   if ii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oO0o0 , 1016 , OOoOooOoOOOoo , o0ooooO0o0O , Iio00 )
    if 82 - 82: oOo0O0Ooo / ooOOOoO
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if III1I != 'Failed' :
  IIIIIiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( III1I )
  for oO0o0 , I1111i in IIIIIiI :
   if ii1I in I1111i . lower ( ) :
    OOo ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oO0o0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 6 - 6: ii1ii11IIIiiI / I11i1ii1 / Ii % I11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( O0 )
  for oO0o0 , I1111i in i1I :
   if ii1I in I1111i . lower ( ) :
    OOo ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oO0o0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 69 - 69: iiiiiiii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 83 - 83: iI11I1II1I1I . I11i + iiiiiiii1 . ii / I11i1ii1 + IIiIiII11i
    if 90 - 90: ii1ii11IIIiiI * O0OOOoOoo0 / Ii1IIIi1
    if 68 - 68: OOooOOo
    if 65 - 65: o000O0o
    if 82 - 82: I11i
    if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + iiiiiiii1
o00O0oOOo = '{SF},' ; i1OOO00oO0O = '{IF},' ; IIi1 = '{PW},' ; iiii1Ii = '{AM},' ; OOoO0OooO = '{GF},' ; IiiOo = '{DD},' ; iiiIiii11i1i = '{UO},' ; Oo0o = '{LE},' ; i1iOO00O0O00oOOO = '{ZY},' ; ii1111iIIiIIi = '{UE},' ; ooOo0Oo = '{PE},' ; I11i1I111II1IiI = '{JE},' ; IiI1Ii = '{TH},' ; oOO00o0oooOo0 = '{LK},'
if 65 - 65: ii1ii11IIIiiI
if 71 - 71: iiiiiiii1 % iiiiiiii1 . o000O0o + Ii - Ii
def Ii1i1iI ( ) :
 iIIII = OoOooO ( 'http://www.iwatchseries.me/tv-list/' )
 i1IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , oO0o0 , 8021 , III1iII1I1ii + 'iwatch.png' )
  I1I11i ( 'movies' , 'MAIN' )
def Iiii ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIIII )
 for url , I1111i , IIii1III in i1IIIII11I1IiI :
  OOo ( I1111i + IIii1III , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def OooO00 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  O00iIi1i1Ii1 ( url )
def O00iIi1i1Ii1 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iIIII )
 Iii1I1111ii = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( 'VidSpot - ' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in i1I :
  i1i11I1I1iii1 ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url , I1111i in Iii1I1111ii :
  i1i11I1I1iii1 ( 'VidUp' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for I1111i , url in ooOoO00 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   i1i11I1I1iii1 ( 'TheVideo - ' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 86 - 86: ooOOOoO + I1ii11iIi11i * Ii1IIIi1 * ooOoO0O00 / ii
def O0oOOoO ( ) :
 iIIII = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 i1IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , oO0o0 , 1021 , III1iII1I1ii + 'anime.png' )
  if 48 - 48: O0OOOoOoo0 * ooOoO0O00 % oO0o / I11i1ii1 - OOooOOo
  if 10 - 10: I11i1ii1
def i1iIi1IiI ( ) :
 iIIII = OoOooO ( 'http://www.animetoon.org/cartoon' )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIII )
 for oO0o0 , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , oO0o0 , 1002 , III1iII1I1ii + 'anime.png' )
  if 16 - 16: o000O0o
  if 96 - 96: I11i1ii1 / o000O0o % o0o00Oo0O / Ii1IIIi1 * oO0o * ooOOOoO
  if 27 - 27: OOooOOo % ii1ii11IIIiiI / ooOoO0O00 . ooOoO0O00 * ii % I11i1ii1
def O0o0O00O0 ( url ) :
 iIIII = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  Oo00O0O = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  OOo ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  OOo ( I1111i , url , 1003 , Oo00O0O )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0OO0O0oO0o ( url , IMAGE ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   O0oOOo0 ( url )
  elif 'playpanda' in url :
   O0oOOo0 ( url )
   if 50 - 50: ooOoO0O00
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0oOOo0 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 49 - 49: iiiiiiii1 * ii1ii11IIIiiI
  if 66 - 66: Ii1IIIi1 . ooOoO0O00
def i1oOOo00ooO00 ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 . add_header ( 'referer' , url )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 66 - 66: ooOOOoO + Ii1I . iiiiiiii1
def I1iIi1iIiiIiI ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 35 - 35: iiiiiiii1 . ooOOOoO . Ii1I
def iIiIiiiI ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i1i111III1 = ( '%s%s' % ( III1i1IIII1i , url ) )
 i1i = I1iIi1iIiiIiI ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , iii11i1IIII , I1111i in i1IIIII11I1IiI :
  i1i11I1I1iii1 ( '%s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iii11i1IIII )
  if 16 - 16: o000O0o
def ooo0O0O0OO ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  oOooOOoO ( url , I1111i )
 else :
  o0o000OOO ( url )
def o0o000OOO ( url ) :
 import urlresolver
 try :
  I1111iii1ii11 = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( I1111iii1ii11 , xbmcgui . ListItem ( I1111i ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( I1111i ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def Oo ( url ) :
 if 79 - 79: iI11I1II1I1I / iI11I1II1I1I . O0OOOoOoo0 . ii1ii11IIIiiI
 III11I = open ( o00OO00OoO , "a" )
 III11I . write ( 'url="' + url + '"\n' )
 III11I . close
 if 49 - 49: Ii1I * iiiiiiii1 + OOooOOo
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( I1111i ) )
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  OOooO0OOoo = xbmcgui . Dialog ( )
  if OOooO0OOoo . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   OOooO0OOoo . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oO0O . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def oOooOOoO ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  i1II11i1iI1 = '.mp4'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0o000OOO ( url )
  if i11I1II1I11i == 1 :
   oOOoOOO ( url , name , i1II11i1iI1 )
 elif '.mkv' in url :
  i1II11i1iI1 = '.mkv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0o000OOO ( url )
  if i11I1II1I11i == 1 :
   oOOoOOO ( url , name , i1II11i1iI1 )
 elif '.mp3' in url :
  i1II11i1iI1 = '.mp3'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0o000OOO ( url )
  if i11I1II1I11i == 1 :
   oOOoOOO ( url , name , i1II11i1iI1 )
 elif '.avi' in url :
  i1II11i1iI1 = '.avi'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0o000OOO ( url )
  if i11I1II1I11i == 1 :
   oOOoOOO ( url , name , i1II11i1iI1 )
 elif '.mov' in url :
  i1II11i1iI1 = '.mov'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0o000OOO ( url )
  if i11I1II1I11i == 1 :
   oOOoOOO ( url , name , i1II11i1iI1 )
 elif '.mpeg' in url :
  i1II11i1iI1 = '.mpeg'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0o000OOO ( url )
  if i11I1II1I11i == 1 :
   oOOoOOO ( url , name , i1II11i1iI1 )
 elif '.mpg' in url :
  i1II11i1iI1 = '.mpg'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0o000OOO ( url )
  if i11I1II1I11i == 1 :
   oOOoOOO ( url , name , i1II11i1iI1 )
 elif '.flv' in url :
  i1II11i1iI1 = '.flv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0o000OOO ( url )
  if i11I1II1I11i == 1 :
   oOOoOOO ( url , name , i1II11i1iI1 )
 elif '.wmv' in url :
  i1II11i1iI1 = '.wmv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0o000OOO ( url )
  if i11I1II1I11i == 1 :
   oOOoOOO ( url , name , i1II11i1iI1 )
 else :
  o0o000OOO ( url )
def oOOoOOO ( url , name , cat ) :
 O0o0OO0o0oOO0 ( )
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
def O0o0OO0o0oOO0 ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def i1II1IiIIi ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 o0oOoO00o . update ( 100 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 oO0O . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 70 - 70: Ii1IIIi1 / Ii1I
def OOOOo0o00OO0000 ( url ) :
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0O . play ( url ) . strip ( )
 except : pass
 if 72 - 72: ii + ii
def i11I1 ( url ) :
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 import urlresolver
 OOO0OOoo = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 oO0O . play ( OOO0OOoo )
 xbmc . sleep ( 1 )
 oO0O . play ( url )
 if 27 - 27: ooOOOoO * IIiIiII11i / I1111IIi . I1ii11iIi11i - Ii1I * ii1ii11IIIiiI
 if 25 - 25: IIiIiII11i * ooOoO0O00 + I1111IIi * I11i / Ii1IIIi1
def oOOiiiIIiIi ( ) :
 try :
  OooI111I1I = getSet ( "core-player" )
  if ( OooI111I1I == 'DVDPLAYER' ) : ooo0ooOoo0OoO0 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( OooI111I1I == 'MPLAYER' ) : ooo0ooOoo0OoO0 = xbmc . PLAYER_CORE_MPLAYER
  elif ( OooI111I1I == 'PAPLAYER' ) : ooo0ooOoo0OoO0 = xbmc . PLAYER_CORE_PAPLAYER
  else : ooo0ooOoo0OoO0 = xbmc . PLAYER_CORE_AUTO
 except : ooo0ooOoo0OoO0 = xbmc . PLAYER_CORE_AUTO
 return ooo0ooOoo0OoO0
 return True
 if 38 - 38: I1111IIi - ooOoO0O00 . Ii
def OOo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiI , listitem = i111iiI1ii , isFolder = True )
 return IiIi1
 if 28 - 28: iiiiiiii1 / o000O0o . Ii1I
def o0OoO0000oOO ( name , url , mode , iconimage , fanart , description ) :
 if 83 - 83: ooOOOoO
 iiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiI , listitem = i111iiI1ii , isFolder = True )
 return IiIi1
 if 36 - 36: iI11I1II1I1I
def i1i11I1I1iii1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 IiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiI , listitem = i111iiI1ii , isFolder = False )
 return IiIi1
 if 74 - 74: I1111IIi * Ii1I - ii
 if 59 - 59: I11i1ii1 * oO0o - iiiiiiii1 % o000O0o
 if 95 - 95: IIiIiII11i + IIiIiII11i
 if 33 - 33: ooOoO0O00 . I1ii11iIi11i - I1111IIi
 if 30 - 30: ii % Ii1IIIi1
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - Ii1IIIi1
def OO0O000 ( heading , announce ) :
 class o0o00O00Oo0 ( ) :
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
   try : oooOo0OOOoo0 = open ( announce ) ; o0I1iI111ii111i = oooOo0OOOoo0 . read ( )
   except : o0I1iI111ii111i = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( o0I1iI111ii111i ) )
   return
 o0o00O00Oo0 ( )
 o0o00O00Oo0 ( )
 if 96 - 96: O0OOOoOoo0
def iI1Ii11iIiI1 ( ) :
 OO0O000 ( 'GenieTv Recomended Sources' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Reaper[/COLOR] [CR]  [COLORred]http://roguemedia.info/cerberus/repo/[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 9 - 9: I1111IIi + IIiIiII11i . oOo0O0Ooo * O0OOOoOoo0
 if 6 - 6: O0OOOoOoo0 % iiiiiiii1
 if 17 - 17: IIiIiII11i - ii + ooOOOoO % ii1ii11IIIiiI % ii
 if 14 - 14: ooOoO0O00 - iI11I1II1I1I . I11i1ii1 + I1111IIi / ooOoO0O00 / IIiIiII11i
 if 47 - 47: Ii1IIIi1
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 68 - 68: iiiiiiii1 + I1111IIi . iI11I1II1I1I
 if 48 - 48: oOo0O0Ooo % o0o00Oo0O * I1ii11iIi11i / o0o00Oo0O
 if 95 - 95: Ii1I / ii1ii11IIIiiI
 if 82 - 82: IIiIiII11i . iiiiiiii1
 if 80 - 80: I11i
 if 46 - 46: O0OOOoOoo0 % iiiiiiii1 % OOooOOo . ii . IIiIiII11i % I1111IIi
 if 6 - 6: iiiiiiii1 % I1111IIi / ii1ii11IIIiiI + iiiiiiii1 . o000O0o
 if 70 - 70: iI11I1II1I1I / ii1ii11IIIiiI
 if 61 - 61: o0o00Oo0O * I11i + iiiiiiii1 - Ii1IIIi1 . oOo0O0Ooo - I1111IIi
 if 7 - 7: Ii1I
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / ooOOOoO
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
 if 13 - 13: Ii
 if 54 - 54: Ii1IIIi1 . Ii1I * ooOOOoO % iiiiiiii1 . o0o00Oo0O * I1111IIi
 if 87 - 87: ii1ii11IIIiiI % Ii1I * I1ii11iIi11i
 if 59 - 59: I1ii11iIi11i / ooOOOoO - iI11I1II1I1I * iI11I1II1I1I
 if 18 - 18: ooOOOoO * Ii1I / Ii / iI11I1II1I1I * ii . Ii1IIIi1
 if 69 - 69: I1ii11iIi11i * I11i1ii1
 if 91 - 91: I11i . I11i1ii1 / oO0o / Ii * I11i
 if 52 - 52: oOo0O0Ooo - Ii / I1111IIi . o000O0o
 if 38 - 38: o000O0o + ii * OOooOOo % o000O0o
 if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
 if 24 - 24: OOooOOo * ii1ii11IIIiiI
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
def oO0ooo000 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + i11II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 47 - 47: oO0o . ooOOOoO % I11i1ii1 - I1ii11iIi11i . oOo0O0Ooo
def IIiiiI1ii ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + Oo0o0o00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 67 - 67: I11i % I11i * I11i1ii1 - Ii / iI11I1II1I1I % oOo0O0Ooo
def ooo0o ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o0OOO0O00Oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 78 - 78: oO0o
def iI1I ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 62 - 62: iI11I1II1I1I % iiiiiiii1 % Ii1I * I1111IIi
def oO0OO0o0oo0o ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + oOo0ooo00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 88 - 88: o000O0o
def iIi1OO0 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + IiIII1111iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 89 - 89: I1111IIi - I1111IIi % O0OOOoOoo0 / ooOOOoO + o000O0o - I1111IIi
def O0oOoO0o0oO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + oOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 51 - 51: ii + ooOOOoO % OOooOOo . ii1ii11IIIiiI % Ii * I11i1ii1
def iIIIIi1Ii ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + oOOOOOOo0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 65 - 65: Ii1IIIi1 / Ii1IIIi1 / O0OOOoOoo0 * ii
def iIIi1IiiiII1i ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + IIiIii1iiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 77 - 77: I11i1ii1 - oO0o . o000O0o
def OOOoo0OO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + IIi1iIII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , OOoOooOoOOOoo , o0ooooO0o0O , o0ooO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , o0ooO )
 I1I11i ( 'movies' , 'MAIN' )
 if 41 - 41: I11i
 if 81 - 81: iI11I1II1I1I * IIiIiII11i + iiiiiiii1 + I1ii11iIi11i + Ii1I
 if 81 - 81: I1ii11iIi11i
 if 78 - 78: oOo0O0Ooo / ii % O0OOOoOoo0 - I1111IIi
 if 33 - 33: I11i1ii1 * ii
 if 14 - 14: IIiIiII11i + o0o00Oo0O - O0OOOoOoo0
 if 18 - 18: I11i / Ii % Ii1I * ii
 if 67 - 67: OOooOOo
 if 67 - 67: Ii1I / O0OOOoOoo0 + iI11I1II1I1I % oOo0O0Ooo
def I1i1I ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OoOooOI1I , ooO00Oo , Iiii1Ii1I in os . walk ( iIi1ii1I1 ) :
     o00o000 = 0
     o00o000 += len ( Iiii1Ii1I )
     if o00o000 > 0 :
      for oooOo0OOOoo0 in Iiii1Ii1I :
       os . unlink ( os . path . join ( OoOooOI1I , oooOo0OOOoo0 ) )
  IIIi1IiI1iII = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( IIIi1IiI1iII )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 85 - 85: Ii1I + OOooOOo - Ii % OOooOOo . o000O0o + Ii
 if 12 - 12: I1111IIi + ooOoO0O00 . oOo0O0Ooo * iI11I1II1I1I * Ii1I
 if 5 - 5: I11i1ii1 - iiiiiiii1 - O0OOOoOoo0
 if 38 - 38: iI11I1II1I1I . ii1ii11IIIiiI
 if 12 - 12: oO0o - oOo0O0Ooo + ii + ii * oOo0O0Ooo - ooOoO0O00
 if 64 - 64: Ii + OOooOOo + I11i + Ii1IIIi1
 if 33 - 33: oOo0O0Ooo - O0OOOoOoo0 . ooOoO0O00 / Ii
 if 84 - 84: ooOOOoO / ii / I1111IIi % ooOOOoO . Ii1IIIi1 + iiiiiiii1
def o0o0oO ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 94 - 94: ooOOOoO
def Oo00OOoOo ( url ) :
 IIIi1IIiI = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 IiIi1I1i = [
 ( IIIi1IIiI ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( IIIi1IIiI , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( IIIi1IIiI , 'plugin.video.itv' , 'Images' ) ) ]
 if 41 - 41: I1ii11iIi11i / o0o00Oo0O . o0o00Oo0O + Ii * o0o00Oo0O / oO0o
 iIIiII11i1I = 0
 if 36 - 36: Ii1I % ii
 for i11I in IiIi1I1i :
  if os . path . exists ( i11I ) and not i11I in [ oO0o0o0ooO0oO , IIIi1IIiI ] :
   for OoOooOI1I , ooO00Oo , Iiii1Ii1I in os . walk ( i11I ) :
    o00o000 = 0
    o00o000 += len ( Iiii1Ii1I )
    if o00o000 > 0 :
     for oooOo0OOOoo0 in Iiii1Ii1I :
      if not oooOo0OOOoo0 in oooOOOOO :
       try :
        os . unlink ( os . path . join ( OoOooOI1I , oooOo0OOOoo0 ) )
       except :
        pass
      else : iIiIi11 ( 'Ignore Log File: %s' % oooOo0OOOoo0 )
     for o0O0ooooooo00 in ooO00Oo :
      try :
       shutil . rmtree ( os . path . join ( OoOooOI1I , o0O0ooooooo00 ) )
       iIIiII11i1I += 1
       iIiIi11 ( "[Success] cleared %s files from %s" % ( str ( o00o000 ) , os . path . join ( i11I , o0O0ooooooo00 ) ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , o0O0ooooooo00 ) )
  else :
   for OoOooOI1I , ooO00Oo , Iiii1Ii1I in os . walk ( i11I ) :
    for o0O0ooooooo00 in ooO00Oo :
     if 'cache' in o0O0ooooooo00 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( OoOooOI1I , o0O0ooooooo00 ) )
       iIIiII11i1I += 1
       iIiIi11 ( "[Success] wiped %s " % os . path . join ( i11I , o0O0ooooooo00 ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , o0O0ooooooo00 ) )
       if 29 - 29: oOo0O0Ooo / I11i + iI11I1II1I1I / o0o00Oo0O / Ii1IIIi1 % ooOoO0O00
 o0o0oO ( oO , 'Clear Cache: Removed %s Files' % iIIiII11i1I )
 if 65 - 65: oO0o * OOooOOo . ii - o0o00Oo0O * OOooOOo % OOooOOo
 if 1 - 1: oOo0O0Ooo + ii . oOo0O0Ooo + Ii1IIIi1 / iiiiiiii1
 if 73 - 73: I11i % Ii1I . iI11I1II1I1I
 if 43 - 43: I1111IIi / ooOOOoO + oO0o
 if 38 - 38: O0OOOoOoo0
 if 59 - 59: oOo0O0Ooo
 if 21 - 21: Ii1I - o000O0o * oO0o
def oOoo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oO00oOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OoOooOI1I , ooO00Oo , Iiii1Ii1I in os . walk ( oO00oOOOO ) :
   o00o000 = 0
   o00o000 += len ( Iiii1Ii1I )
   if 54 - 54: ooOOOoO * ii
   if 71 - 71: I11i + ii * IIiIiII11i / iiiiiiii1
   if o00o000 > 0 :
    if 78 - 78: iiiiiiii1 % Ii1IIIi1
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( o00o000 ) + " files found" , "Do you want to delete them?" ) :
     if 73 - 73: Ii1I + O0OOOoOoo0 * oOo0O0Ooo * ooOOOoO
     for oooOo0OOOoo0 in Iiii1Ii1I :
      os . unlink ( os . path . join ( OoOooOI1I , oooOo0OOOoo0 ) )
     for o0O0ooooooo00 in ooO00Oo :
      shutil . rmtree ( os . path . join ( OoOooOI1I , o0O0ooooooo00 ) )
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
 if 35 - 35: ooOOOoO * o0o00Oo0O * oO0o . Ii1I
 if 74 - 74: O0OOOoOoo0 * O0OOOoOoo0 * I11i / o000O0o
 if 91 - 91: Ii . Ii1I / IIiIiII11i
 if 97 - 97: ii1ii11IIIiiI % ooOoO0O00 % I1111IIi + I1ii11iIi11i - o0o00Oo0O - ooOOOoO
 if 64 - 64: ii1ii11IIIiiI - O0OOOoOoo0
 if 12 - 12: ooOoO0O00
 if 99 - 99: IIiIiII11i - Ii1I * I1111IIi
 if 3 - 3: I1111IIi - Ii1I * O0OOOoOoo0 * Ii1I + I1ii11iIi11i
 if 15 - 15: Ii1I * ii1ii11IIIiiI / O0OOOoOoo0 . I11i / ii1ii11IIIiiI % OOooOOo
def I1iIIiiIIi1i ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oO00oOOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OoOooOI1I , ooO00Oo , Iiii1Ii1I in os . walk ( oO00oOOOO ) :
   o00o000 = 0
   o00o000 += len ( Iiii1Ii1I )
   if 75 - 75: ii % Ii % iI11I1II1I1I % Ii1I / Ii
   if 96 - 96: I11i1ii1 * o000O0o / iI11I1II1I1I / ooOOOoO
   if o00o000 > 0 :
    if 5 - 5: I11i
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( o00o000 ) + " files found" , "Do you want to delete them?" ) :
     if 83 - 83: ooOOOoO * oOo0O0Ooo . IIiIiII11i * ooOoO0O00 % o0o00Oo0O
     for oooOo0OOOoo0 in Iiii1Ii1I :
      os . unlink ( os . path . join ( OoOooOI1I , oooOo0OOOoo0 ) )
     for o0O0ooooooo00 in ooO00Oo :
      shutil . rmtree ( os . path . join ( OoOooOI1I , o0O0ooooooo00 ) )
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
 Oo00OOoOo ( url )
 return
 if 35 - 35: OOooOOo % oO0o + o0o00Oo0O * I11i % Ii1I
 if 57 - 57: o000O0o / ooOOOoO
 if 63 - 63: I11i1ii1 * oO0o * I11i1ii1 + OOooOOo
 if 25 - 25: O0OOOoOoo0 * OOooOOo / oOo0O0Ooo / I1111IIi
 if 11 - 11: Ii1IIIi1 + Ii
 if 14 - 14: OOooOOo / I1111IIi + oO0o - ii1ii11IIIiiI
 if 38 - 38: iiiiiiii1
 if 30 - 30: IIiIiII11i + ooOOOoO . Ii + iI11I1II1I1I
 if 100 - 100: o000O0o * I11i / O0OOOoOoo0
 if 92 - 92: I11i1ii1 / Ii * Ii1IIIi1
def oooOO0OoO0OOO ( url , name ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOOoOo000O0oo = os . path . join ( o00O0 , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOOoo = os . path . join ( o00O0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( OOOoo ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OOOoOo000O0oo = os . path . join ( o00O0 , 'advancedsettings.xml' )
   try :
    os . remove ( OOOoOo000O0oo )
    print '=== GenieTv - REMOVING    ' + str ( OOOoOo000O0oo ) + '    ==='
   except :
    pass
   i1i = iI111I11I1I1 . http_GET ( url ) . content
   ii11iI1iIiIi = open ( OOOoOo000O0oo , "w" )
   ii11iI1iIiIi . write ( i1i )
   ii11iI1iIiIi . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OOOoOo000O0oo ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OOOoOo000O0oo = os . path . join ( o00O0 , 'advancedsettings.xml' )
  try :
   os . remove ( OOOoOo000O0oo )
   print '=== GenieTv - REMOVING    ' + str ( OOOoOo000O0oo ) + '    ==='
  except :
   pass
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  ii11iI1iIiIi = open ( OOOoOo000O0oo , "w" )
  ii11iI1iIiIi . write ( i1i )
  ii11iI1iIiIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOOoOo000O0oo ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 97 - 97: ooOOOoO
def O0oOO0o0 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOOoOo000O0oo = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  ii11iI1iIiIi = open ( OOOoOo000O0oo ) . read ( )
  if 'zero' in ii11iI1iIiIi :
   name = '0CACHE'
  elif 'tuxen' in ii11iI1iIiIi :
   name = 'TUXENS'
  elif 'muckys' in ii11iI1iIiIi :
   name = 'MUCKYS'
  elif 'p2p1' in ii11iI1iIiIi :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in ii11iI1iIiIi :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in ii11iI1iIiIi :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 81 - 81: ii1ii11IIIiiI * O0OOOoOoo0 % ii1ii11IIIiiI % Ii % ooOoO0O00 / I11i
def oOO00oo ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OOOoOo000O0oo = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  os . remove ( OOOoOo000O0oo )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OOOoOo000O0oo ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 41 - 41: O0OOOoOoo0 + ooOOOoO . o000O0o - I11i1ii1 . ii
 if 83 - 83: ii * iI11I1II1I1I . ii / IIiIiII11i . ii - I1111IIi
 if 90 - 90: I1ii11iIi11i % Ii + o0o00Oo0O % o0o00Oo0O
 if 70 - 70: IIiIiII11i * ii - ii1ii11IIIiiI + o000O0o * o0o00Oo0O
 if 49 - 49: o000O0o . ii1ii11IIIiiI . OOooOOo - Ii1I
 if 74 - 74: I11i1ii1 % Ii1I * ooOoO0O00
 if 18 - 18: OOooOOo
 if 30 - 30: IIiIiII11i
 if 27 - 27: ooOoO0O00 - iI11I1II1I1I + o0o00Oo0O % I1ii11iIi11i / Ii1IIIi1 + ooOoO0O00
 if 48 - 48: I1ii11iIi11i
def I1ii1i1iiii ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 i1IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for oooO0o0OoOo0O , iiiiI11iI , ooOooOOoO0O , i1I111ii11Iii in i1IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % oooO0o0OoOo0O , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % ooOooOOoO0O , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % i1I111ii11Iii )
  inc = inc + 1
  if 25 - 25: I11i1ii1
  if 83 - 83: ii1ii11IIIiiI / ii * o000O0o . oOo0O0Ooo . ooOoO0O00
  if 59 - 59: ooOOOoO . ooOOOoO * oOo0O0Ooo - ii1ii11IIIiiI % OOooOOo
  if 19 - 19: ii / I1ii11iIi11i - iiiiiiii1 . OOooOOo
  if 8 - 8: ooOOOoO % I11i1ii1 . iI11I1II1I1I
  if 95 - 95: I11i + Ii . Ii1I . I11i1ii1 . I11i
  if 93 - 93: O0OOOoOoo0
  if 55 - 55: IIiIiII11i % I11i - oO0o
  if 48 - 48: I11i1ii1 * iI11I1II1I1I % OOooOOo
def OoOo0OO0 ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOOoOo000O0oo = os . path . join ( o00O0 , 'addons2.ini' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  ii11iI1iIiIi = open ( OOOoOo000O0oo , "w" )
  ii11iI1iIiIi . write ( i1i )
  ii11iI1iIiIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOOoOo000O0oo ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 98 - 98: Ii
def IIiI111iI1iiii ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OOOoOo000O0oo = os . path . join ( o00O0 , 'settings.xml' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  ii11iI1iIiIi = open ( OOOoOo000O0oo , "w" )
  ii11iI1iIiIi . write ( i1i )
  ii11iI1iIiIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OOOoOo000O0oo ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 55 - 55: iiiiiiii1 / ii . I11i1ii1 / oO0o
 if 28 - 28: Ii % o0o00Oo0O
def I1ii1ii ( ) :
 try :
  iIiIiiiII11i = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iIiIiiiII11i ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    I1oO0oO00OO00 = os . path . join ( iIiIiiiII11i , "source.db" )
    os . unlink ( I1oO0oO00OO00 )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 75 - 75: I11i + oOo0O0Ooo % I11i1ii1 * iiiiiiii1
 if 87 - 87: IIiIiII11i + o0o00Oo0O / O0OOOoOoo0 * I11i1ii1
 if 52 - 52: iI11I1II1I1I / O0OOOoOoo0 . o0o00Oo0O * I1111IIi . oOo0O0Ooo
 if 67 - 67: IIiIiII11i + ii1ii11IIIiiI - oOo0O0Ooo * I11i1ii1
 if 19 - 19: Ii * I1ii11iIi11i
def OoOooO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 33 - 33: Ii + oOo0O0Ooo
 if 95 - 95: Ii1I / I1111IIi % iI11I1II1I1I + o0o00Oo0O
 if 6 - 6: I1111IIi
 if 73 - 73: I11i % I11i . Ii1IIIi1 * Ii1I - ii1ii11IIIiiI
 if 97 - 97: I1111IIi
 if 15 - 15: o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . iiiiiiii1
 if 64 - 64: I11i1ii1 / ooOoO0O00
def i11i1ii1I ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; ooo00 = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if ooo00 :
  o00O00Oo = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; o00O00Oo = xbmc . translatePath ( o00O00Oo ) ;
  OoOiiiIIIi = os . path . join ( o00O00Oo , ".." , ".." ) ; OoOiiiIIIi = os . path . abspath ( OoOiiiIIIi ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + OoOiiiIIIi ) ; O0o0ooOoOO = False
  try :
   for OoOooOI1I , ooO00Oo , Iiii1Ii1I in os . walk ( OoOiiiIIIi , topdown = True ) :
    ooO00Oo [ : ] = [ o0O0ooooooo00 for o0O0ooooooo00 in ooO00Oo if o0O0ooooooo00 not in o0oO0 ]
    for I1111i in Iiii1Ii1I :
     try : os . remove ( os . path . join ( OoOooOI1I , I1111i ) )
     except :
      if I1111i not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : O0o0ooOoOO = True
      plugintools . log ( "Error removing " + OoOooOI1I + " " + I1111i )
    for I1111i in ooO00Oo :
     try : os . rmdir ( os . path . join ( OoOooOI1I , I1111i ) )
     except :
      if I1111i not in [ "Database" , "userdata" ] : O0o0ooOoOO = True
      plugintools . log ( "Error removing " + OoOooOI1I + " " + I1111i )
   if not O0o0ooOoOO : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 Oo0oo ( )
 if 50 - 50: ooOoO0O00 % I1111IIi % iiiiiiii1
 if 76 - 76: I11i1ii1 % oOo0O0Ooo
 if 18 - 18: oO0o
def O0oOo ( ) :
 iIi1IiiIII = [ ]
 i11iI1I1I11II = sys . argv [ 2 ]
 if len ( i11iI1I1I11II ) >= 2 :
  o0OO0o0o00o = sys . argv [ 2 ]
  oo0 = o0OO0o0o00o . replace ( '?' , '' )
  if ( o0OO0o0o00o [ len ( o0OO0o0o00o ) - 1 ] == '/' ) :
   o0OO0o0o00o = o0OO0o0o00o [ 0 : len ( o0OO0o0o00o ) - 2 ]
  O00O0oO = oo0 . split ( '&' )
  iIi1IiiIII = { }
  for OOOOoOoO in range ( len ( O00O0oO ) ) :
   IIIIi1iII = { }
   IIIIi1iII = O00O0oO [ OOOOoOoO ] . split ( '=' )
   if ( len ( IIIIi1iII ) ) == 2 :
    iIi1IiiIII [ IIIIi1iII [ 0 ] ] = IIIIi1iII [ 1 ]
    if 49 - 49: ooOoO0O00 . I1111IIi
 return iIi1IiiIII
 if 82 - 82: oO0o / ooOOOoO
ii1iIIIi1Iii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
o000OOO000 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
oOoOOOo0oo = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
O000Oo0O = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I1I1i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
oo000oo0oOo0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
i11II = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
IIiO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
Oo0o0o00Oo = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o0OOO0O00Oo00 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iiii = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
oOo0ooo00OoO = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
IiIII1111iI = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
oOoO = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
oOOOOOOo0O0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
IIiIii1iiI = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
ooOO0OOO00o = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
i1I1ii1iI1 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o0OOOooO00OO00O = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
O00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
o00OOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oo0o000o0oOO0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IIi1iIII = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
III1i1IIII1i = base64 . decodestring ( 'Q1VOVA==' )
def iiOOooooO0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 iiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiI , listitem = i111iiI1ii , isFolder = True )
 return IiIi1
 if 63 - 63: o0o00Oo0O . iiiiiiii1 / iiiiiiii1 / iI11I1II1I1I + Ii1IIIi1 . ooOOOoO
def OOiIiIIi1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 iiiI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 IiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 IiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiiI , listitem = i111iiI1ii , isFolder = False )
 return IiIi1
 if 59 - 59: oO0o - iI11I1II1I1I % o000O0o
 if 39 - 39: iiiiiiii1 % o000O0o % o0o00Oo0O % o0o00Oo0O - O0OOOoOoo0 - o000O0o
o0OO0o0o00o = O0oOo ( )
oO0o0 = None
I1111i = None
i1i1iII1 = None
OOoOooOoOOOoo = None
o0ooooO0o0O = None
o0ooO = None
ooooOo = None
O0OOooO00O0oo0 = None
if 12 - 12: ii * Ii1IIIi1 * Ii1I * I11i1ii1
if 26 - 26: ii . ooOoO0O00 + oO0o
try :
 O0OOooO00O0oo0 = int ( o0OO0o0o00o [ "fav_mode" ] )
except :
 pass
 if 42 - 42: Ii * I11i % ooOOOoO % I1ii11iIi11i + I11i * Ii
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
 i1i1iII1 = int ( o0OO0o0o00o [ "mode" ] )
except :
 pass
try :
 o0ooooO0o0O = urllib . unquote_plus ( o0OO0o0o00o [ "fanart" ] )
except :
 pass
try :
 o0ooO = urllib . unquote_plus ( o0OO0o0o00o [ "description" ] )
except :
 pass
 if 66 - 66: ii1ii11IIIiiI / I1111IIi . ii * I1ii11iIi11i % Ii
 if 100 - 100: Ii1I % IIiIiII11i * Ii - O0OOOoOoo0
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( i1i1iII1 )
print "URL: " + str ( oO0o0 )
print "Name: " + str ( I1111i )
print "IconImage: " + str ( OOoOooOoOOOoo )
if 69 - 69: Ii1IIIi1 + O0OOOoOoo0 / iiiiiiii1
if 37 - 37: iI11I1II1I1I * ooOOOoO / I1111IIi * I1ii11iIi11i % Ii
def I1I11i ( content , viewType ) :
 if 93 - 93: I11i1ii1 + I11i1ii1
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 65 - 65: ii * ooOOOoO * o000O0o % Ii1I * IIiIiII11i
if OOoOooOoOOOoo == None : OOoOooOoOOOoo = Oo00OOOOO
if o0ooooO0o0O == None : o0ooooO0o0O = O0o0Oo
if i1i1iII1 == None :
 o0o0o0oO0oOO ( )
 if 86 - 86: Ii / ooOOOoO * O0OOOoOoo0 - O0OOOoOoo0
elif i1i1iII1 == 1 :
 ooOoo ( oO0o0 )
 if 32 - 32: I1ii11iIi11i . o0o00Oo0O
elif i1i1iII1 == 44 :
 oOo0 ( oO0o0 )
 if 48 - 48: Ii1I % IIiIiII11i + ooOOOoO
elif i1i1iII1 == 2 :
 O0OOoo0o ( )
 if 25 - 25: I1111IIi * I11i / oOo0O0Ooo . I1111IIi % IIiIiII11i
elif i1i1iII1 == 3 :
 ii1IOoO0O ( )
 if 50 - 50: OOooOOo * O0OOOoOoo0
elif i1i1iII1 == 21 :
 i1i1II ( )
 if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / ooOOOoO
elif i1i1iII1 == 4 :
 Oo0OOo ( )
 if 92 - 92: I11i
elif i1i1iII1 == 5 :
 i1ii1iIi ( oO0o0 )
 if 8 - 8: O0OOOoOoo0 + Ii1I . ii1ii11IIIiiI
elif i1i1iII1 == 6 :
 oOoo ( oO0o0 )
 if 50 - 50: I1ii11iIi11i
elif i1i1iII1 == 7 :
 oooOO0OoO0OOO ( oO0o0 , I1111i )
 if 16 - 16: ii1ii11IIIiiI - OOooOOo % I1ii11iIi11i / ii1ii11IIIiiI . ooOOOoO + I11i1ii1
elif i1i1iII1 == 8 :
 O0oOO0o0 ( oO0o0 , I1111i )
 if 78 - 78: iI11I1II1I1I + oO0o + Ii
elif i1i1iII1 == 9 :
 FIXREPOSADDONS ( oO0o0 )
 if 21 - 21: I1ii11iIi11i + ii1ii11IIIiiI % I11i1ii1 + OOooOOo % ooOOOoO
elif i1i1iII1 == 10 :
 O0O0ooOOO ( )
 if 22 - 22: ooOoO0O00 / ii . oO0o
elif i1i1iII1 == 11 :
 oOO00oo ( oO0o0 )
 if 83 - 83: oOo0O0Ooo - ii + Ii1I . ii1ii11IIIiiI / I11i + I11i1ii1
elif i1i1iII1 == 12 :
 I1ii1i1iiii ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 90 - 90: oOo0O0Ooo - Ii
elif i1i1iII1 == 13 :
 I1i1I ( )
 if 42 - 42: Ii1IIIi1 . I1ii11iIi11i
elif i1i1iII1 == 14 :
 Oo00OOoOo ( oO0o0 )
 if 21 - 21: O0OOOoOoo0 . oOo0O0Ooo / ooOOOoO
elif i1i1iII1 == 15 :
 OO0oO ( )
 if 97 - 97: iI11I1II1I1I + ooOoO0O00 - I11i
elif i1i1iII1 == 16 :
 OoOo0OO0 ( oO0o0 , I1111i )
 if 73 - 73: oO0o - Ii % iiiiiiii1 / I1ii11iIi11i - ii % Ii1IIIi1
elif i1i1iII1 == 17 :
 IIiI111iI1iiii ( oO0o0 , I1111i )
 if 79 - 79: oOo0O0Ooo / I11i . ii1ii11IIIiiI * Ii1I + ooOOOoO
elif i1i1iII1 == 18 :
 I1ii1ii ( )
 if 96 - 96: oO0o * IIiIiII11i
elif i1i1iII1 == 19 :
 OO0000 ( oO0o0 )
 if 1 - 1: oOo0O0Ooo - OOooOOo
elif i1i1iII1 == 40 :
 I1iIIIIIi ( I1111i , oO0o0 , o0ooO )
 if 74 - 74: OOooOOo * IIiIiII11i + o0o00Oo0O + ooOOOoO
elif i1i1iII1 == 42 :
 oO00oo ( I1111i , oO0o0 , o0ooO )
 if 3 - 3: iI11I1II1I1I - ooOoO0O00 / O0OOOoOoo0 + ooOoO0O00 + o0o00Oo0O
elif i1i1iII1 == 43 :
 o0oooo0OOo00 ( oO0o0 )
 if 18 - 18: iI11I1II1I1I . O0OOOoOoo0 % Ii1IIIi1 % o000O0o + iI11I1II1I1I * ii
elif i1i1iII1 == 20 :
 i11111iiiII1I ( oO0o0 )
 if 78 - 78: I1111IIi
elif i1i1iII1 == 22 :
 oO0ooo000 ( oO0o0 )
 if 38 - 38: oO0o * Ii1I
elif i1i1iII1 == 23 :
 IIiiiI1ii ( oO0o0 )
 if 4 - 4: oO0o . Ii1I
elif i1i1iII1 == 24 :
 ooo0o ( oO0o0 )
 if 21 - 21: Ii / oO0o / Ii1I * o0o00Oo0O - IIiIiII11i * Ii1IIIi1
elif i1i1iII1 == 25 :
 iI1I ( oO0o0 )
 if 27 - 27: I11i . OOooOOo * ii1ii11IIIiiI * O0OOOoOoo0 * o0o00Oo0O
elif i1i1iII1 == 26 :
 oO0OO0o0oo0o ( oO0o0 )
 if 93 - 93: I1111IIi % iiiiiiii1 % IIiIiII11i
elif i1i1iII1 == 27 :
 iIi1OO0 ( oO0o0 )
 if 20 - 20: ii * iiiiiiii1
elif i1i1iII1 == 28 :
 O0oOoO0o0oO ( oO0o0 )
 if 38 - 38: O0OOOoOoo0 . ii
elif i1i1iII1 == 29 :
 iIIIIi1Ii ( oO0o0 )
 if 28 - 28: iiiiiiii1 * ooOoO0O00 . Ii1I
elif i1i1iII1 == 30 :
 o0oOOOOoo0 ( oO0o0 )
 if 75 - 75: o0o00Oo0O / o000O0o * I11i1ii1 - Ii1IIIi1 / ooOoO0O00
elif i1i1iII1 == 31 :
 iIIi1IiiiII1i ( oO0o0 )
 if 61 - 61: ooOOOoO
elif i1i1iII1 == 32 :
 Iii1IIII11I ( )
 if 100 - 100: o0o00Oo0O - iI11I1II1I1I * I1ii11iIi11i
elif i1i1iII1 == 33 :
 i1Ii11ii1I ( )
 if 35 - 35: I11i1ii1
elif i1i1iII1 == 35 :
 oO0ooOoOO ( oO0o0 )
 if 57 - 57: oO0o . I1ii11iIi11i + oOo0O0Ooo
elif i1i1iII1 == 34 :
 OO0oI1iii1i ( oO0o0 )
 if 18 - 18: oOo0O0Ooo - Ii1I * ooOOOoO / Ii - I11i % I11i
elif i1i1iII1 == 36 :
 I11oO0oo ( oO0o0 )
 if 31 - 31: ooOOOoO
elif i1i1iII1 == 37 :
 oooOoO00OooO0 ( oO0o0 )
 if 100 - 100: Ii * Ii . iI11I1II1I1I % O0OOOoOoo0 * Ii1I
elif i1i1iII1 == 38 :
 I1Ii1i11I1I ( oO0o0 )
 if 17 - 17: ii1ii11IIIiiI * I1111IIi * Ii / Ii1I / Ii
elif i1i1iII1 == 41 :
 i11i1ii1I ( o0OO0o0o00o )
 if 23 - 23: ii + Ii / I1ii11iIi11i / O0OOOoOoo0 . O0OOOoOoo0 * oOo0O0Ooo
elif i1i1iII1 == 39 :
 OOOoo0OO ( oO0o0 )
 if 98 - 98: I1111IIi
elif i1i1iII1 == 45 :
 TEXTS ( )
 if 23 - 23: ooOOOoO / ooOoO0O00 * oO0o
elif i1i1iII1 == 46 :
 iI1Ii11iIiI1 ( )
 if 51 - 51: Ii1IIIi1 - ii / ii % ii
elif i1i1iII1 == 47 :
 GEVID ( )
 if 85 - 85: oO0o . I11i . oOo0O0Ooo
elif i1i1iII1 == 48 :
 Ii1IiiiI1ii ( I1111i , oO0o0 , o0ooO )
 if 75 - 75: iI11I1II1I1I - ii1ii11IIIiiI % o0o00Oo0O % I1111IIi
elif i1i1iII1 == 49 :
 iI1i111I1Ii ( )
 if 6 - 6: I1ii11iIi11i % o000O0o * I11i1ii1 - ooOoO0O00 . OOooOOo
elif i1i1iII1 == 22222 :
 Oo ( oO0o0 )
 if 20 - 20: I1ii11iIi11i / iiiiiiii1 . I1ii11iIi11i
elif i1i1iII1 == 222 :
 ooo0O0O0OO ( oO0o0 )
 if 60 - 60: Ii1I - oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i . ooOoO0O00 . OOooOOo
elif i1i1iII1 == 2222222 :
 o0o000OOO ( oO0o0 )
 if 24 - 24: I1111IIi * oOo0O0Ooo / Ii1IIIi1
elif i1i1iII1 == 222222 :
 oOooOOoO ( oO0o0 , I1111i )
 if 51 - 51: iI11I1II1I1I / ooOOOoO * oO0o * ii1ii11IIIiiI + Ii1I . ii
elif i1i1iII1 == 333 :
 iIiIiiiI ( oO0o0 )
 if 75 - 75: I1111IIi / ii / o0o00Oo0O % Ii1IIIi1
 if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
elif i1i1iII1 == 1020 :
 O0oOOoO ( )
 if 11 - 11: I11i * oO0o
elif i1i1iII1 == 1021 :
 ANIMEEP ( )
 if 92 - 92: OOooOOo . I1ii11iIi11i * ooOOOoO
elif i1i1iII1 == 1022 :
 ANIMEPLAY ( oO0o0 )
 if 86 - 86: o0o00Oo0O
elif i1i1iII1 == 1001 :
 i1iIi1IiI ( )
 if 55 - 55: ii1ii11IIIiiI / iiiiiiii1 / Ii1I % I11i1ii1 % oOo0O0Ooo
elif i1i1iII1 == 1005 :
 oOoi1I1i1II1i ( )
 if 55 - 55: o000O0o + ii % ooOoO0O00
elif i1i1iII1 == 1007 :
 ooI111II ( oO0o0 )
 if 24 - 24: Ii1I - I1ii11iIi11i
elif i1i1iII1 == 1010 :
 IIiiiI1iI ( oO0o0 )
 if 36 - 36: oOo0O0Ooo . Ii1IIIi1 % IIiIiII11i * I1111IIi
elif i1i1iII1 == 1011 :
 OOoOi11i ( oO0o0 )
 if 34 - 34: ooOOOoO % O0OOOoOoo0 - I11i1ii1 - oOo0O0Ooo
elif i1i1iII1 == 1012 :
 iiioooOo ( oO0o0 )
 if 44 - 44: ii1ii11IIIiiI . I11i . iI11I1II1I1I + ii - oOo0O0Ooo
elif i1i1iII1 == 1030 :
 IIII1II11Iii ( )
 if 22 - 22: ooOOOoO * Ii1I . ii / I1ii11iIi11i / ii1ii11IIIiiI
elif i1i1iII1 == 1031 :
 I1i11I1IiII1 ( oO0o0 , OOoOooOoOOOoo )
 if 54 - 54: iiiiiiii1 % ii1ii11IIIiiI + I11i1ii1
elif i1i1iII1 == 1032 :
 iiIiII ( oO0o0 )
 if 45 - 45: ii1ii11IIIiiI / o000O0o * iiiiiiii1 . ii1ii11IIIiiI
elif i1i1iII1 == 1006 :
 Parse . ParseURL ( oO0o0 )
 if 25 - 25: Ii1I / Ii1I
elif i1i1iII1 == 2030 :
 Parse . addonParseURL ( oO0o0 )
 if 79 - 79: I1ii11iIi11i - oO0o % I1ii11iIi11i . IIiIiII11i
elif i1i1iII1 == 2031 :
 Parse . apkParseURL ( oO0o0 )
 if 84 - 84: I11i1ii1 * ii + o0o00Oo0O
elif i1i1iII1 == 2032 :
 Parse . ParseBOSS ( oO0o0 )
 if 84 - 84: ooOoO0O00 . ooOOOoO . ooOoO0O00 . I1ii11iIi11i
elif i1i1iII1 == 1002 :
 O0o0O00O0 ( oO0o0 )
 if 21 - 21: IIiIiII11i . o0o00Oo0O + I1ii11iIi11i - Ii
elif i1i1iII1 == 1003 :
 Oo0OO0O0oO0o ( oO0o0 , OOoOooOoOOOoo )
 if 5 - 5: iI11I1II1I1I * Ii + oO0o + ooOOOoO * o0o00Oo0O % I11i1ii1
elif i1i1iII1 == 1004 :
 O0oOOo0 ( oO0o0 )
 if 88 - 88: I11i / Ii * Ii1I
elif i1i1iII1 == 1008 :
 IiII11 ( )
 if 23 - 23: o0o00Oo0O / O0OOOoOoo0
elif i1i1iII1 == 1009 :
 o0OoO ( oO0o0 )
 if 66 - 66: ooOoO0O00 % ii * Ii + o000O0o * o0o00Oo0O / oO0o
elif i1i1iII1 == 2001 :
 OoOoOO00O ( )
 if 14 - 14: oOo0O0Ooo . I1111IIi
elif i1i1iII1 == 2002 :
 II11iii1iI1ii ( oO0o0 )
 if 29 - 29: ii / I1111IIi + OOooOOo - iiiiiiii1 + I1111IIi . ooOoO0O00
elif i1i1iII1 == 1013 :
 OoOo ( )
elif i1i1iII1 == 10111113 :
 o0o0 ( oO0o0 )
 if 26 - 26: Ii - IIiIiII11i
elif i1i1iII1 == 1014 :
 i1I1Ii1 ( )
 if 43 - 43: oOo0O0Ooo
elif i1i1iII1 == 1015 :
 OoOOOo00 ( oO0o0 )
 if 35 - 35: I11i1ii1 + OOooOOo * ii - IIiIiII11i
elif i1i1iII1 == 1016 :
 oOIIiIi ( oO0o0 , OOoOooOoOOOoo , I1111i )
 if 19 - 19: ooOoO0O00 / ii1ii11IIIiiI / OOooOOo . oOo0O0Ooo / ii1ii11IIIiiI % I11i
elif i1i1iII1 == 1017 :
 OO0oOOoo ( )
 if 39 - 39: I11i1ii1 - ii
elif i1i1iII1 == 1018 :
 IiII1 ( oO0o0 )
 if 88 - 88: ooOoO0O00 + iI11I1II1I1I * Ii - ii % I11i
elif i1i1iII1 == 1023 :
 oOOO00o000o ( )
 if 74 - 74: I11i1ii1 - Ii
elif i1i1iII1 == 1024 :
 iIIIIi ( oO0o0 )
 if 34 - 34: I1111IIi + iiiiiiii1 + I1ii11iIi11i / IIiIiII11i
elif i1i1iII1 == 1025 :
 IIi1iI11I ( oO0o0 )
 if 33 - 33: ii1ii11IIIiiI . ooOoO0O00 - IIiIiII11i - oO0o
elif i1i1iII1 == 4001 :
 iiIi11iI1iii ( )
 if 31 - 31: ooOOOoO - OOooOOo / I11i * OOooOOo / I1ii11iIi11i + I11i
elif i1i1iII1 == 4002 :
 OOOooo ( )
 if 46 - 46: I1111IIi * oO0o / Ii1IIIi1 + I1ii11iIi11i
elif i1i1iII1 == 4003 :
 I11iiI ( )
 if 24 - 24: I11i1ii1 % Ii1IIIi1 . o0o00Oo0O * I1ii11iIi11i
elif i1i1iII1 == 4004 :
 ooI1i ( )
 if 52 - 52: o0o00Oo0O . iiiiiiii1 + O0OOOoOoo0 / Ii
elif i1i1iII1 == 4005 :
 ooo000o000 ( )
 if 52 - 52: o000O0o % I1ii11iIi11i * IIiIiII11i
elif i1i1iII1 == 4006 :
 O0ooO0OoO00o ( )
 if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
elif i1i1iII1 == 4007 :
 o0Oooo ( )
 if 27 - 27: ooOoO0O00 - o000O0o + Ii1IIIi1
elif i1i1iII1 == 4008 :
 Iiii1iI1i ( )
 if 3 - 3: I1111IIi % iiiiiiii1 . ii
elif i1i1iII1 == 4009 : iIIiIiI1I1 ( )
elif i1i1iII1 == 4010 : iIiiIIIiI1Ii ( )
elif i1i1iII1 == 3000 :
 I1i1IO0OOoooO ( )
 if 19 - 19: iiiiiiii1 * ii1ii11IIIiiI - o000O0o
elif i1i1iII1 == 3001 :
 i1I111II11 ( )
 if 78 - 78: oO0o - ii1ii11IIIiiI / Ii1IIIi1
elif i1i1iII1 == 3002 :
 o00oO ( oO0o0 )
 if 81 - 81: OOooOOo
elif i1i1iII1 == 3003 :
 I11ii111i ( oO0o0 )
 if 21 - 21: O0OOOoOoo0 / Ii1IIIi1 % I1111IIi
elif i1i1iII1 == 3004 :
 o0ooo ( oO0o0 )
 if 51 - 51: ooOOOoO + I11i1ii1 / oOo0O0Ooo
elif i1i1iII1 == 404 :
 I1I11I11iIII ( I1111i , oO0o0 , OOoOooOoOOOoo )
 if 3 - 3: iI11I1II1I1I / Ii1IIIi1 % o000O0o . ii1ii11IIIiiI - ii1ii11IIIiiI
elif i1i1iII1 == 405 :
 i1II1IiIIi ( oO0o0 )
 if 55 - 55: Ii % ii + o0o00Oo0O
elif i1i1iII1 == 7030 :
 iII11II ( )
 if 7 - 7: I11i1ii1 - Ii * O0OOOoOoo0 / ii1ii11IIIiiI - I11i
elif i1i1iII1 == 7021 :
 ii1i11111 ( I1111i )
 if 62 - 62: I11i - iI11I1II1I1I . ooOOOoO . ii1ii11IIIiiI * ii1ii11IIIiiI
elif i1i1iII1 == 7022 :
 Oo0OOOO ( I1111i )
 if 24 - 24: ooOOOoO
elif i1i1iII1 == 7000 :
 iii1OO00Oo00o ( I1111i , oO0o0 , img )
 if 93 - 93: oOo0O0Ooo % oO0o / Ii / ooOOOoO
elif i1i1iII1 == 7050 :
 IiI1 ( oO0o0 )
 if 60 - 60: I11i1ii1 - ii1ii11IIIiiI . oOo0O0Ooo * o000O0o * Ii
elif i1i1iII1 == 7051 :
 iiI1Iii ( oO0o0 )
 if 29 - 29: oO0o - I1ii11iIi11i . o000O0o / oO0o % Ii
elif i1i1iII1 == 7052 :
 oo0OoOIiI1IIIiI1I1i ( oO0o0 )
 if 26 - 26: I11i1ii1 . iiiiiiii1 / IIiIiII11i % ii1ii11IIIiiI
elif i1i1iII1 == 7053 :
 oO00O0oO ( oO0o0 )
 if 82 - 82: Ii1IIIi1 % o0o00Oo0O % iI11I1II1I1I % I1111IIi + Ii
elif i1i1iII1 == 7054 :
 CoolPlay ( oO0o0 )
 if 64 - 64: ooOoO0O00 / I1111IIi . I1111IIi - iiiiiiii1 % Ii1IIIi1 . IIiIiII11i
elif i1i1iII1 == 7060 :
 iiI11iIIiI1IiI1iIi1 ( )
 if 78 - 78: iiiiiiii1 - o0o00Oo0O - iiiiiiii1 . iI11I1II1I1I % Ii1I . ii
elif i1i1iII1 == 7061 :
 I1i11i ( oO0o0 )
 if 64 - 64: I1111IIi
elif i1i1iII1 == 7063 :
 iIiiI11II11 ( oO0o0 )
 if 21 - 21: I11i - I11i1ii1 * ii . ii
elif i1i1iII1 == 7062 :
 IIiI111Iii ( oO0o0 )
 if 17 - 17: Ii1IIIi1 - O0OOOoOoo0 % oOo0O0Ooo * Ii1IIIi1 * iI11I1II1I1I . I11i
elif i1i1iII1 == 7064 :
 NATatozcat ( )
 if 58 - 58: o000O0o - IIiIiII11i + o0o00Oo0O
elif i1i1iII1 == 7067 :
 OOiIiI1iI ( oO0o0 )
 if 54 - 54: iI11I1II1I1I - I1111IIi - I1111IIi
elif i1i1iII1 == 7066 :
 NATatozA ( oO0o0 )
 if 18 - 18: Ii + iI11I1II1I1I . Ii
elif i1i1iII1 == 7065 :
 ooo0oooO ( oO0o0 )
 if 63 - 63: O0OOOoOoo0 - oO0o * Ii1IIIi1
elif i1i1iII1 == 7070 :
 ooOoo0O0o0OO0 ( )
 if 89 - 89: O0OOOoOoo0 / I1ii11iIi11i
elif i1i1iII1 == 7071 :
 DIZIlist ( oO0o0 )
 if 66 - 66: I11i + OOooOOo % ii . ooOOOoO
elif i1i1iII1 == 7072 :
 DIZIpull ( oO0o0 )
 if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
elif i1i1iII1 == 7073 :
 WATCHDIZI ( oO0o0 )
 if 93 - 93: ooOoO0O00 + iiiiiiii1 / oO0o - ooOOOoO % I1ii11iIi11i / ii1ii11IIIiiI
elif i1i1iII1 == 7002 :
 iIiiII11 ( )
 if 1 - 1: I1ii11iIi11i / ii1ii11IIIiiI . Ii % Ii1IIIi1 + I11i + o0o00Oo0O
elif i1i1iII1 == 7003 :
 oo00o0000 ( oO0o0 )
 if 54 - 54: iiiiiiii1 + I11i1ii1 % I1111IIi
elif i1i1iII1 == 7004 :
 IIIi ( oO0o0 )
 if 83 - 83: I11i * iI11I1II1I1I
elif i1i1iII1 == 7020 :
 oOo00o0oO ( oO0o0 )
 if 36 - 36: OOooOOo + IIiIiII11i - oO0o % I11i1ii1 * ooOoO0O00
elif i1i1iII1 == 7001 :
 O0O0Oo00 ( )
 if 4 - 4: ii1ii11IIIiiI + oO0o * Ii1I
elif i1i1iII1 == 7010 :
 OOo0OOooO0 ( oO0o0 )
 if 13 - 13: OOooOOo - I1111IIi * iI11I1II1I1I * o0o00Oo0O
elif i1i1iII1 == 7011 :
 II1i111Ii ( oO0o0 )
 if 26 - 26: ii + o000O0o + oO0o . o0o00Oo0O
elif i1i1iII1 == 7012 :
 OOoO00OOo ( oO0o0 )
 if 46 - 46: ii - I1ii11iIi11i * iiiiiiii1 * Ii1IIIi1 * iiiiiiii1 . o000O0o
elif i1i1iII1 == 7013 :
 cnfTVPlay2 ( oO0o0 )
elif i1i1iII1 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oO0o0 )
elif i1i1iII1 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oO0o0 )
elif i1i1iII1 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1111i , oO0o0 , OOoOooOoOOOoo )
elif i1i1iII1 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif i1i1iII1 == 7018 :
 III1Ii ( )
elif i1i1iII1 == 7019 :
 CNF_Studio_Indexer . List_Movies ( oO0o0 )
elif i1i1iII1 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oO0o0 )
elif i1i1iII1 == 7024 :
 CNF_Studio_Indexer . Box_Office ( oO0o0 )
 if 96 - 96: ii1ii11IIIiiI / I1111IIi % I11i + ooOOOoO
elif i1i1iII1 == 8000 :
 OOOOO0o0oo0 ( )
elif i1i1iII1 == 8001 :
 ooO0O0OOO ( )
elif i1i1iII1 == 8002 :
 OO00O0O ( )
elif i1i1iII1 == 8003 :
 II1111i11i11 ( )
elif i1i1iII1 == 8004 :
 I1IIiIIiiI1i ( )
elif i1i1iII1 == 8005 :
 IiI1i1111iI1i ( )
elif i1i1iII1 == 8006 :
 I1OO0o0OoooO00 ( I1111i , oO0o0 )
elif i1i1iII1 == 8030 :
 o0OOOoo0ooo00 ( oO0o0 )
elif i1i1iII1 == 8045 :
 i1II1111 ( oO0o0 )
elif i1i1iII1 == 8046 :
 ooOOOo0 ( oO0o0 )
elif i1i1iII1 == 8047 :
 OOOIIIIiiIi ( oO0o0 )
elif i1i1iII1 == 8048 :
 i1II ( oO0o0 )
elif i1i1iII1 == 8049 :
 OOOoooOo00O ( oO0o0 )
elif i1i1iII1 == 804900 :
 iiIIiI1I ( oO0o0 )
elif i1i1iII1 == 8020 :
 Ii1i1iI ( )
elif i1i1iII1 == 8021 :
 Iiii ( oO0o0 )
elif i1i1iII1 == 8022 :
 OooO00 ( oO0o0 )
elif i1i1iII1 == 8023 :
 O00iIi1i1Ii1 ( oO0o0 )
elif i1i1iII1 == 8040 :
 o0OoOO ( )
elif i1i1iII1 == 8041 :
 o000Oo0oO0OO0 ( oO0o0 )
elif i1i1iII1 == 8042 :
 OoI1 ( oO0o0 )
elif i1i1iII1 == 8043 :
 yt . PlayVideo ( oO0o0 )
elif i1i1iII1 == 8044 :
 Iii11111I1iii ( oO0o0 )
elif i1i1iII1 == 8060 :
 Iii ( )
elif i1i1iII1 == 8061 :
 iiI1 ( oO0o0 )
elif i1i1iII1 == 8064 :
 i1iI1 ( )
elif i1i1iII1 == 8065 :
 i1II1i1iiI1 ( oO0o0 )
elif i1i1iII1 == 8070 :
 OooOO0o0oOoO ( )
elif i1i1iII1 == 8071 :
 i11I1Ii1Iiii1 ( oO0o0 )
elif i1i1iII1 == 7080 :
 o0oooOoOoOo ( oO0o0 )
elif i1i1iII1 == 8090 :
 I1i1IiIIiIiII ( )
elif i1i1iII1 == 8091 :
 iI11ii ( oO0o0 )
elif i1i1iII1 == 8092 :
 I1i1i1ii1iiI1 ( oO0o0 )
elif i1i1iII1 == 8093 :
 iIi1II111I1i1 ( oO0o0 )
elif i1i1iII1 == 8081 :
 i1ii1iiI1iI ( )
elif i1i1iII1 == 8062 :
 I1Iii1 ( oO0o0 )
elif i1i1iII1 == 8063 :
 o0Ooo ( oO0o0 )
elif i1i1iII1 == 8050 :
 IIiI1i ( )
elif i1i1iII1 == 8051 :
 Ii1 ( oO0o0 )
elif i1i1iII1 == 8052 :
 III ( oO0o0 )
elif i1i1iII1 == 8085 :
 O0ooO0o ( )
elif i1i1iII1 == 8086 :
 OO0iii111 ( oO0o0 )
elif i1i1iII1 == 8087 :
 O0oooOo0000o0 ( oO0o0 )
elif i1i1iII1 == 8088 :
 o0o0Oo0oo ( oO0o0 , I1111i )
elif i1i1iII1 == 9000 :
 oOooOOo00ooO ( )
elif i1i1iII1 == 1111 :
 O0O0 ( )
elif i1i1iII1 == 9001 :
 iIII ( )
elif i1i1iII1 == 9002 :
 O0oO0OOoOOO0oO ( )
elif i1i1iII1 == 9003 :
 oooI11Ii1 ( )
elif i1i1iII1 == 9004 :
 World1 ( )
elif i1i1iII1 == 9005 :
 World2 ( oO0o0 )
elif i1i1iII1 == 9006 :
 World3 ( oO0o0 )
elif i1i1iII1 == 9007 :
 i1ii11Iii11 ( )
elif i1i1iII1 == 9008 :
 o0ooOO ( oO0o0 )
elif i1i1iII1 == 9009 :
 OOoo000Ooo ( oO0o0 )
elif i1i1iII1 == 9010 :
 IIii1i ( )
elif i1i1iII1 == 9011 :
 ooOOOOOo ( oO0o0 )
elif i1i1iII1 == 50 :
 oOo0oO ( oO0o0 )
elif i1i1iII1 == 9020 :
 champlist ( )
elif i1i1iII1 == 9021 :
 iIio00O000ooOO ( )
elif i1i1iII1 == 9022 :
 O000OOOoOooO ( )
elif i1i1iII1 == 9023 :
 o0oOoOOO ( )
elif i1i1iII1 == 9024 :
 i1Iiiiii1II ( oO0o0 )
elif i1i1iII1 == 9030 :
 IIIIiI1iiI ( oO0o0 )
elif i1i1iII1 == 9031 :
 i1IO00oO0oOOOOOO ( oO0o0 )
elif i1i1iII1 == 9032 :
 Oo0ooo00OoO ( oO0o0 )
elif i1i1iII1 == 9033 :
 Iiii1I1I111i1 ( oO0o0 )
elif i1i1iII1 == 9034 :
 oOoO00o ( )
elif i1i1iII1 == 7085 :
 i1i1I11Ii1i ( oO0o0 )
elif i1i1iII1 == 7086 :
 OOoOOo ( oO0o0 )
elif i1i1iII1 == 7087 :
 i11IIiiI ( o0ooO )
elif i1i1iII1 == 9666 :
 I1iIIiiIIi1i ( oO0o0 )
elif i1i1iII1 == 10100 : Iii11I ( )
elif i1i1iII1 == 101001 : o0oI1Iii ( oO0o0 )
elif i1i1iII1 == 10105 : ii111IIiiiiI ( oO0o0 )
elif i1i1iII1 == 10106 : oo0OOoOo0 ( oO0o0 )
elif i1i1iII1 == 10104 : ii1IO0oo00o000 ( oO0o0 )
elif i1i1iII1 == 10107 : II1I1Ii11 ( )
elif i1i1iII1 == 10103 : oO00oO0 ( oO0o0 )
elif i1i1iII1 == 10108 : o0Oo00oOOo ( oO0o0 )
elif i1i1iII1 == 10000 : Origin_Menu ( )
elif i1i1iII1 == 10001 : oO0o000OoOoO0 ( )
elif i1i1iII1 == 10002 : OO0 ( )
elif i1i1iII1 == 10003 : I1ii1ii11i1I ( )
elif i1i1iII1 == 10004 : Ooo0o0oo ( oO0o0 )
elif i1i1iII1 == 10005 : o0oO0oOO ( )
elif i1i1iII1 == 10006 : OO000OOOo0Oo ( oO0o0 )
elif i1i1iII1 == 10007 : Oo00O0o0O ( oO0o0 , OOoOooOoOOOoo )
elif i1i1iII1 == 10008 : i1iI11ii ( )
elif i1i1iII1 == 10009 : OOO00OI11II1 ( )
elif i1i1iII1 == 10010 : oo0000o0O0oOo ( oO0o0 )
elif i1i1iII1 == 10011 : OOOO0O ( oO0o0 )
elif i1i1iII1 == 10012 : OOOOo0o00OO0000 ( oO0o0 )
elif i1i1iII1 == 10113 : GRABG ( oO0o0 , I1111i )
elif i1i1iII1 == 10109 : i11I1 ( oO0o0 )
elif i1i1iII1 == 10013 : OO0oOo ( oO0o0 )
elif i1i1iII1 == 10014 : iIo00oo ( )
elif i1i1iII1 == 10015 : iii11i1i1 ( )
elif i1i1iII1 == 10016 : IIi1i1IiIIi1i ( oO0o0 )
elif i1i1iII1 == 10017 : OO0OOOOOo ( )
elif i1i1iII1 == 10018 : IIi1I1 ( )
elif i1i1iII1 == 10019 : iioOO ( )
elif i1i1iII1 == 10020 : I11II11IiI11 ( )
elif i1i1iII1 == 10021 : iIIiI1 ( )
elif i1i1iII1 == 10022 : OoooOO0 ( oO0o0 )
elif i1i1iII1 == 10023 : I1IiiiiI1i1I ( I1111i , oO0o0 )
elif i1i1iII1 == 10024 : ooi11I ( oO0o0 )
elif i1i1iII1 == 10025 : O0o0OO0000ooo ( )
elif i1i1iII1 == 10026 : O00O0O0OO00oo ( )
elif i1i1iII1 == 10027 : Oo0 ( )
elif i1i1iII1 == 10028 : oOOoOOooO0 ( )
elif i1i1iII1 == 10029 : o00O ( )
elif i1i1iII1 == 423 : oooO0 ( oO0o0 )
elif i1i1iII1 == 426 : IIIiiiiiI1I ( oO0o0 )
elif i1i1iII1 == 10030 : Izle_Films ( )
elif i1i1iII1 == 10031 : Latest_Izle_Movies ( )
elif i1i1iII1 == 10032 : Izle_Genres ( )
elif i1i1iII1 == 10033 : Izle_Pop_Movies ( )
elif i1i1iII1 == 10034 : Izle_Boxsets ( )
elif i1i1iII1 == 10035 : Izle_Search ( )
elif i1i1iII1 == 10036 : Izle_Genres_Movie ( oO0o0 )
elif i1i1iII1 == 10037 : Izle_Boxset_single ( oO0o0 )
elif i1i1iII1 == 10038 : Izle_IFRAME ( )
elif i1i1iII1 == 10039 : Izle_Boxsets_Next ( oO0o0 )
elif i1i1iII1 == 10040 : III1ii1I ( )
elif i1i1iII1 == 10041 : OO00o0oo ( oO0o0 )
elif i1i1iII1 == 10042 : OO00O00o0O ( oO0o0 )
elif i1i1iII1 == 10043 : OOoo0 ( )
elif i1i1iII1 == 10044 : ii1iIi1 ( oO0o0 )
elif i1i1iII1 == 10045 : Ii1iII1ii1 ( I1111i )
elif i1i1iII1 == 10046 : I1IiIi1iiI ( oO0o0 )
elif i1i1iII1 == 10047 : I1Ii11I11i1 ( oO0o0 )
elif i1i1iII1 == 10048 : o00o0o0oOo0 ( oO0o0 )
elif i1i1iII1 == 10049 : I1iI11I ( oO0o0 )
elif i1i1iII1 == 10050 : iI1i11iII111 ( )
elif i1i1iII1 == 10051 : OooOOo ( )
elif i1i1iII1 == 10052 : o00ooO0 ( )
elif i1i1iII1 == 10053 : Addon ( oO0o0 )
elif i1i1iII1 == 10054 : iIiiIi11 ( oO0o0 , I1111i )
elif i1i1iII1 == 10055 :
 Ii1iii11I ( "addFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiII ( I1111i , oO0o0 , OOoOooOoOOOoo , o0ooooO0o0O , O0OOooO00O0oo0 )
elif i1i1iII1 == 10056 :
 Ii1iii11I ( "rmFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 I1Ii11i1ii1i ( I1111i )
elif i1i1iII1 == 10057 :
 Ii1iii11I ( "getFavorites" )
 I1I11 ( )
elif i1i1iII1 == 10058 : ooO ( )
elif i1i1iII1 == 10059 : Donators_Guide ( )
elif i1i1iII1 == 10060 : oo000o0000oO ( )
elif i1i1iII1 == 10061 : ooo0 ( )
elif i1i1iII1 == 10062 : iiIIiiIi ( I1111i , oO0o0 , o0ooO )
elif i1i1iII1 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
elif i1i1iII1 == 10064 : O00O ( )
elif i1i1iII1 == 10065 : ii1O0ooooo000 ( oO0o0 )
elif i1i1iII1 == 10066 : O0000oO0o00 ( oO0o0 )
elif i1i1iII1 == 10068 : OOOOO0O00 ( oO0o0 )
elif i1i1iII1 == 10069 : ii1I1IiiI1ii1i ( oO0o0 )
elif i1i1iII1 == 10070 : i11Iii1Ii1i1 ( oO0o0 )
elif i1i1iII1 == 10071 : Genie_Watch ( )
elif i1i1iII1 == 10072 : I1III1iIi ( )
elif i1i1iII1 == 10073 : IIi ( oO0o0 )
elif i1i1iII1 == 10074 : i1Oo0oOo000OoO0 ( oO0o0 )
elif i1i1iII1 == 10075 : O0oOoo ( OOoOooOoOOOoo , I1111i , oO0o0 )
elif i1i1iII1 == 10076 : I1iIIIiI ( oO0o0 )
elif i1i1iII1 == 10077 : IIi1ii1 ( oO0o0 )
elif i1i1iII1 == 10078 : Iiii1i11ii1Ii ( )
elif i1i1iII1 == 10079 : Genie_Watch_Tv_Shows ( )
elif i1i1iII1 == 10080 : Genie_Watch_Tv_Genre ( oO0o0 )
elif i1i1iII1 == 10081 : Genie_Watch_TV_PlayRun ( oO0o0 )
elif i1i1iII1 == 10082 : Genie_Watch_TV_Episodes ( oO0o0 , OOoOooOoOOOoo )
elif i1i1iII1 == 10083 : Genie_Watch_Tv_Recent ( oO0o0 )
elif i1i1iII1 == 10084 : ooOOo00O00Oo ( )
elif i1i1iII1 == 10085 : Iiii1i1 ( )
elif i1i1iII1 == 10086 : i1IiiiI1iI ( )
elif i1i1iII1 == 20000 : OO0ooOOO0O00o ( )
elif i1i1iII1 == 20001 : i1111Ii11i ( oO0o0 )
elif i1i1iII1 == 20002 : O0O0Oo00OO ( oO0o0 )
elif i1i1iII1 == 20003 : o00o0O0 ( oO0o0 )
elif i1i1iII1 == 20004 : Oo0ooIi ( oO0o0 )
elif i1i1iII1 == 20005 : i1iIii1II1i ( oO0o0 )
elif i1i1iII1 == 21004 : O000o0 ( )
elif i1i1iII1 == 21005 : OoIIiIIIII1I ( oO0o0 )
elif i1i1iII1 == 21006 : o00iIiI1iI1Ii1 ( oO0o0 )
elif i1i1iII1 == 21007 : Ooo0O00 ( oO0o0 )
elif i1i1iII1 == 30000 : O0oO0o0OOOOOO ( )
elif i1i1iII1 == 30001 : Ii1iIi ( )
elif i1i1iII1 == 10012 : Resolve ( oO0o0 )
elif i1i1iII1 == 30003 : Iii1I11 ( )
elif i1i1iII1 == 30004 : iIOoo0ooo0oo ( oO0o0 )
elif i1i1iII1 == 30005 : o00O0o ( oO0o0 )
elif i1i1iII1 == 30006 : IIIii11 ( )
elif i1i1iII1 == 30007 : I11IIII ( )
elif i1i1iII1 == 30008 : IIIIIiiI11i1 ( oO0o0 )
elif i1i1iII1 == 30009 : oO0OOoo ( oO0o0 )
elif i1i1iII1 == 30010 : OOOo00o ( oO0o0 )
elif i1i1iII1 == 30011 : iiIIiIi ( )
elif i1i1iII1 == 30012 : o0Oo ( )
elif i1i1iII1 == 30013 : II11IiI1 ( )
elif i1i1iII1 == 30014 : oO00oOoo00o0 ( )
elif i1i1iII1 == 30015 : oO0oOOOooo ( oO0o0 , OOoOooOoOOOoo , o0ooooO0o0O )
elif i1i1iII1 == 30016 : iIi ( oO0o0 )
elif i1i1iII1 == 30019 : o0OOoo0oOoO00 ( oO0o0 )
elif i1i1iII1 == 30017 : OOOO00 ( oO0o0 )
elif i1i1iII1 == 30018 : Oo0O0O ( oO0o0 )
elif i1i1iII1 == 30030 : ii11iiII ( )
elif i1i1iII1 == 30031 : OOooo000OooO ( )
elif i1i1iII1 == 30032 : iiI ( )
elif i1i1iII1 == 30033 : OOoo0oO0 ( )
elif i1i1iII1 == 30034 : OOo0 ( )
elif i1i1iII1 == 30035 : ii1i1II11II1i ( oO0o0 )
elif i1i1iII1 == 30036 : o00OO0 ( oO0o0 )
elif i1i1iII1 == 30037 : iIi1i111 ( oO0o0 )
elif i1i1iII1 == 30038 : i1IiIiIiiI1 ( )
elif i1i1iII1 == 30039 : OooOoOO0 ( )
elif i1i1iII1 == 50000 : oOOo0O00o ( )
elif i1i1iII1 == 50001 : OoO0o00OOOOO ( )
elif i1i1iII1 == 50002 : I1I ( oO0o0 )
elif i1i1iII1 == 50003 : iIII1I11II1i1 ( o0ooO )
elif i1i1iII1 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif i1i1iII1 == 60001 : iIIiIi ( )
elif i1i1iII1 == 60002 : iI111I1III ( I1111i )
elif i1i1iII1 == 60003 : OoOooOO0oOOo0O ( I1111i )
elif i1i1iII1 == 60004 : i11i ( oO0o0 )
elif i1i1iII1 == 50004 : iiIiIIIiiI ( )
elif i1i1iII1 == 50005 : speedtest . runtest ( oO0o0 )
elif i1i1iII1 == 70001 : i1iIii1i111 ( )
elif i1i1iII1 == 70002 : IiI11I1Ii11II ( oO0o0 )
elif i1i1iII1 == 70003 : oo0ooOoOOoO ( oO0o0 )
elif i1i1iII1 == 70004 : Oo0000o ( oO0o0 )
elif i1i1iII1 == 70005 : iI1IiiiIIiiII ( oO0o0 )
elif i1i1iII1 == 70006 : oOo000o ( )
elif i1i1iII1 == 50006 : OO0O000 ( i1 , i1111 )
elif i1i1iII1 == 80000 : Oo0oo ( )
elif i1i1iII1 == 80001 : resolvefilmon ( oO0o0 )
elif i1i1iII1 == 80002 : oOOOO0oo0O0OO ( )
elif i1i1iII1 == 80003 : IIiii11ii1II1 ( I1111i , oO0o0 , "None" )
elif i1i1iII1 == 80004 : Ii11IiI111 ( I1111i , oO0o0 )
elif i1i1iII1 == 80005 : IiIi ( )
elif i1i1iII1 == 80006 : iii1IIiI ( oO0o0 )
elif i1i1iII1 == 80007 : i1i1Ii11Ii ( oO0o0 )
elif i1i1iII1 == 80008 : O000oOo ( )
elif i1i1iII1 == 80009 : O0ooOo0Oooo ( )
elif i1i1iII1 == 80010 : I1iiIIiI11I ( oO0o0 )
elif i1i1iII1 == 80011 : oOoOo000 ( oO0o0 )
elif i1i1iII1 == 80012 : iIiI1I1II1 ( )
elif i1i1iII1 == 90000 : IIIII1IIiIi ( I1111i , oO0o0 )
elif i1i1iII1 == 90001 : Ii1I1I1i1Ii ( )
elif i1i1iII1 == 90002 : o0O0oo0OO0O ( )
elif i1i1iII1 == 90003 : i11iII1 ( oO0o0 )
elif i1i1iII1 == 90004 : oOooo ( oO0o0 )
elif i1i1iII1 == 90005 : i11iI1111ii1I ( oO0o0 )
elif i1i1iII1 == 90006 : OO00OO0 ( oO0o0 )
elif i1i1iII1 == 90007 : Ooii ( oO0o0 )
elif i1i1iII1 == 90008 : oo0OO0oo ( oO0o0 )
elif i1i1iII1 == 90009 : iIOoo000 ( oO0o0 )
elif i1i1iII1 == 90010 : iiIiI1i1 ( )
elif i1i1iII1 == 90020 : O00O0O00o0O ( )
elif i1i1iII1 == 90021 : hellyeah2 ( oO0o0 )
elif i1i1iII1 == 90022 : hellyeah3 ( oO0o0 )
elif i1i1iII1 == 90023 : iIIIi1i1I11i ( )
elif i1i1iII1 == 90024 : oOOoooO ( oO0o0 )
elif i1i1iII1 == 90025 : IIIii1iiIi ( oO0o0 )
if 46 - 46: oO0o * oOo0O0Ooo
elif i1i1iII1 == 90030 : I11iII ( )
elif i1i1iII1 == 90031 : I1i1i1iii ( )
elif i1i1iII1 == 90032 : iIIii ( oO0o0 )
elif i1i1iII1 == 90033 : ii1iii1i ( oO0o0 )
elif i1i1iII1 == 90034 : ooO0O00Oo0o ( oO0o0 )
elif i1i1iII1 == 90035 : I1i ( oO0o0 )
elif i1i1iII1 == 90036 : Oo00OOooOoO ( oO0o0 )
elif i1i1iII1 == 90039 : II1iiiiI1Ii11 ( oO0o0 )
elif i1i1iII1 == 90037 : OooOOOo0 ( oO0o0 )
elif i1i1iII1 == 90038 : OOOooo0OooOoO ( )
if 25 - 25: iiiiiiii1 . I1111IIi % o0o00Oo0O % ooOoO0O00
elif i1i1iII1 == 10090 : oOoOoOoo0 ( )
elif i1i1iII1 == 10091 : O0oO0o00oo0o ( oO0o0 )
elif i1i1iII1 == 10092 : OOI1I ( oO0o0 )
elif i1i1iII1 == 10093 : o00O0Oooo ( oO0o0 , OOoOooOoOOOoo )
elif i1i1iII1 == 10094 : IiiiI11 ( oO0o0 , OOoOooOoOOOoo )
if 53 - 53: o0o00Oo0O % I11i1ii1
elif i1i1iII1 == 10095 : IIiI1 ( )
elif i1i1iII1 == 10096 : III1I1I ( oO0o0 )
elif i1i1iII1 == 10097 : OOO0o0OO0OO ( oO0o0 )
elif i1i1iII1 == 10098 : iIIIiIi1I1i ( oO0o0 )
elif i1i1iII1 == 10099 : OooOOOO0O0 ( oO0o0 )
if 41 - 41: I1111IIi
elif i1i1iII1 == 10200 : o0o0O ( )
elif i1i1iII1 == 10201 : ooO000O ( oO0o0 )
elif i1i1iII1 == 10202 : I1IIi ( oO0o0 )
elif i1i1iII1 == 10203 : RT4 ( oO0o0 )
if 29 - 29: I11i1ii1
elif i1i1iII1 == 90040 : ooooO0oOoOOoO ( )
elif i1i1iII1 == 90041 : iiI1Ii1I ( oO0o0 )
elif i1i1iII1 == 90042 : iiIiII11i1 ( oO0o0 )
elif i1i1iII1 == 90043 : Ooo0o0oo0 ( oO0o0 )
elif i1i1iII1 == 90044 : O00o ( oO0o0 )
elif i1i1iII1 == 90045 : IiiIiIi111iI1 ( )
elif i1i1iII1 == 90046 : oO0o00ooO0OoO ( oO0o0 )
elif i1i1iII1 == 90050 : I1ii11 ( )
elif i1i1iII1 == 90051 : Oo0O0O00Oo ( oO0o0 )
elif i1i1iII1 == 90052 : iiO0O0o0oO0O00 ( oO0o0 )
elif i1i1iII1 == 90053 : o00ooo0 ( oO0o0 )
elif i1i1iII1 == 90054 : iIiIi1iI11iiI ( oO0o0 )
elif i1i1iII1 == 90055 : IiI1iI1IiiIi1 ( )
if 70 - 70: o000O0o . o0o00Oo0O % ooOOOoO % I1111IIi - ooOOOoO * Ii1I
elif i1i1iII1 == 100001 : Stand_up ( )
if 22 - 22: ooOoO0O00
elif i1i1iII1 == 100003 : IIi1i1IiIIi1i ( oO0o0 )
elif i1i1iII1 == 100004 : IiIIii1 ( oO0o0 )
elif i1i1iII1 == 100005 : Resolve ( oO0o0 )
elif i1i1iII1 == 100008 : Search ( )
elif i1i1iII1 == 100007 : O00oOo00o0o ( oO0o0 )
elif i1i1iII1 == 100009 : yt . PlayVideo ( oO0o0 )
elif i1i1iII1 == 100010 : OoO ( oO0o0 )
elif i1i1iII1 == 100100 : iiI1I1ii ( OOoOooOoOOOoo , oO0o0 , ooooOo )
elif i1i1iII1 == 100101 : i1II11II ( oO0o0 , I1111i , o0ooooO0o0O , ooooOo , OOoOooOoOOOoo )
elif i1i1iII1 == 100102 : oOOOO ( I1111i , oO0o0 , OOoOooOoOOOoo , o0ooooO0o0O )
elif i1i1iII1 == 100106 : IiI1i ( oO0o0 , I1111i )
elif i1i1iII1 == 100107 : Oo0oOooo000OO ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
