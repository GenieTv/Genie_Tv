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
IiiIII111iI = "3.4.2"
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
 if 5 - 5: ii % OOooOOo % o000O0o % O0OOOoOoo0
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
def Iiiii1I ( ) :
 O0oO0 = [ '[COLOR' + II + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + II + ']APK TOOL[/COLOR]' , '[COLOR' + II + ']ADDONS[/COLOR]' , '[COLOR' + II + ']BUILDERS TOOLBOX[/COLOR]' , '[COLOR' + II + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + II + ']CONTACT US[/COLOR]' , '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + II + ']SOURCE LIST[/COLOR]' , '[COLOR' + II + ']GUIDE SKINS[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  Iiii1i1 ( )
 if oO0O0OO0O == 1 :
  OOOoOoO ( )
 if oO0O0OO0O == 2 :
  Ii1I1i ( )
 if oO0O0OO0O == 3 :
  OOI1iI1ii1II ( )
 if oO0O0OO0O == 4 :
  O0O0OOOOoo ( oOooO0 )
 if oO0O0OO0O == 5 :
  OOooO0OOoo . ok ( i1 , i1111 )
 if oO0O0OO0O == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if oO0O0OO0O == 7 :
  Ii1I1Ii ( )
 if oO0O0OO0O == 8 :
  OOoO0 ( )
def OOoO0 ( ) :
 oOooO0 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , 'GuideSkins' + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( oOooO0 , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 ( oOooO0 )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1iIIiiIIi1i ( )
def O0O0ooOOO ( ) :
 oOOo0O00o = iIiIi11 ( )
 OOO = oOOo0O00o . replace ( OooO0 , "" )
 if os . path . exists ( oOOo0O00o ) or not oOOo0O00o == False :
  iiiiI = open ( oOOo0O00o , mode = 'r' ) ; oooOo0OOOoo0 = iiiiI . read ( ) ; iiiiI . close ( )
  OOoO ( "%s - %s" % ( i1 , OOO ) , oooOo0OOOoo0 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def OOoO0 ( ) :
 oOooO0 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , 'GuideSkins' + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( oOooO0 , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 ( oOooO0 )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1iIIiiIIi1i ( )
def OO0O000 ( ) :
 OOiIiIIi1 ( '[COLOR' + II + ']Todays Games[/COLOR]' , str ( I1I1IiI1 ) , 90030 , III1iII1I1ii + 'tgames.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Replays[/COLOR]' , str ( I1I1IiI1 ) , 90031 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 37 - 37: ii - o0o00Oo0O - I11i
def o0o0O0O00oOOo ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 i1IIIII11I1IiI = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 for OO0O0 , I11I11 in i1IIIII11I1IiI :
  OOoO ( '[COLOR' + II + ']Tommys List[/COLOR]  ' + OO0O0 , I11I11 )
def o000O0O ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 i1IIIII11I1IiI = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 90032 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
def I1111i ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( iIIIiIi )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( iIIIiIi )
 for url , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , iIIii , O0o0Oo , '' )
 for url in next :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , III1iII1I1ii + 'NEXT.png' , O0o0Oo , '' )
def o00O0O ( url ) :
 iIIIiIi = OoOooO ( url )
 ii1iii1i = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 Iii1I1111ii = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 i1IIIII11I1IiI = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for I1i1i1iii , url in i1I :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for I1i1i1iii , url in Iii1I1111ii :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for url in ii1iii1i :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
  if 72 - 72: IIiIiII11i + ooOoO0O00 + I11i
def OOOIIiI1i1i ( url ) :
 if 'drive' in url :
  O00Oo0 ( url )
 else :
  iIIIiIi = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( iIIIiIi )
  for url in i1IIIII11I1IiI :
   O00Oo0 ( url )
def IiII111i1i11 ( url ) :
 i111iIi1i1II1 = liveresolver . resolve ( url )
 oooO = xbmcgui . ListItem ( path = i111iIi1i1II1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oooO )
def i1I1i111Ii ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 ooo = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo )
def iIiIi11 ( ) :
 i1i1iI1iiiI = False
 if os . path . exists ( os . path . join ( OooO0 , 'xbmc.log' ) ) :
  i1i1iI1iiiI = os . path . join ( OooO0 , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'kodi.log' ) ) :
  i1i1iI1iiiI = os . path . join ( OooO0 , 'kodi.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'spmc.log' ) ) :
  i1i1iI1iiiI = os . path . join ( OooO0 , 'spmc.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'tvmc.log' ) ) :
  i1i1iI1iiiI = os . path . join ( OooO0 , 'tvmc.log' )
 return i1i1iI1iiiI
 if 51 - 51: oOo0O0Ooo % iiiiiiii1 . o000O0o / iI11I1II1I1I / ooOOOoO . o000O0o
def IIIii11 ( url ) :
 if url == 'http://' : return False
 try :
  O00O0oOO00O00 = urllib2 . Request ( url )
  O00O0oOO00O00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
  i1Oo00 . close ( )
 except Exception , iiIiIIIiiI :
  return iiIiIIIiiI
 return True
def iiI1IIIi ( ) :
 if 47 - 47: I1ii11iIi11i % ooOOOoO % Ii - o0o00Oo0O + I11i1ii1
 if 94 - 94: iiiiiiii1
 if 4 - 4: ii1ii11IIIiiI % o000O0o * oO0o
 if 100 - 100: iiiiiiii1 * Ii1IIIi1 + Ii1IIIi1
 if 54 - 54: ii + I11i - ooOoO0O00 % Ii
 i1i = OoOooO ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( i1i )
 if len ( i1IIIII11I1IiI ) > 0 :
  for I1i1i1iii , oOooO0 , iII1iIi11i , o0ooooO0o0O in i1IIIII11I1IiI :
   OOiIiIIi1 ( I1i1i1iii , oOooO0 , 50005 , iII1iIi11i , o0ooooO0o0O , '' )
def iiIi11iI1iii ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + II + ']WIPE GENIE[/COLOR]' , '[COLOR' + II + ']Genie BUILDS[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Wizard[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   oo000o0000oO ( )
  if oO0O0OO0O == 1 :
   iI1i111I1Ii ( )
  if oO0O0OO0O == 2 :
   i11i1ii1I ( o0OO0o0o00o )
  if oO0O0OO0O == 3 :
   oOo0 ( oOooO0 )
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
  iiOOooooO0Oo ( '[COLOR' + II + ']BOSS COMEDY[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvY29tL2Jvc3Njb20ucGhw' ) , 1016 , III1iII1I1ii + 'boss.png' , O0o0Oo , '' )
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
  if 94 - 94: ii + I1ii11iIi11i / OOooOOo * Ii1IIIi1
  if 69 - 69: I11i1ii1 % o000O0o
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
  if 84 - 84: I11i1ii1 % ii1ii11IIIiiI + Ii
  if 28 - 28: I1ii11iIi11i + oO0o * Ii1IIIi1 % o000O0o . ooOOOoO % o0o00Oo0O
 I1I11i ( 'movies' , 'MAIN' )
def I1iiiiIii ( ) :
 O0oO0 = [ '[COLOR' + II + ']FOOTBALL[/COLOR]' , '[COLOR' + II + ']KIDS[/COLOR]' , '[COLOR' + II + ']NEWS[/COLOR]' , '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + II + ']HOBBIES[/COLOR]' , '[COLOR' + II + ']STAND UP[/COLOR]' , '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']CATEGORIES[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  iIiIiIiI ( )
 if oO0O0OO0O == 1 :
  i11OOoo ( )
 if oO0O0OO0O == 2 :
  iIIiiiI ( )
 if oO0O0OO0O == 3 :
  oo0 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , IiI111ii1ii , I1i1i1iii )
 if oO0O0OO0O == 4 :
  O0OOo ( )
 if oO0O0OO0O == 5 :
  IiIII1 ( )
 if oO0O0OO0O == 6 :
  O0Oo000 ( )
 if oO0O0OO0O == 7 :
  iiI11i1II ( )
 if oO0O0OO0O == 8 :
  OO0O0OOo0O ( )
  if 36 - 36: I11i1ii1 . I1ii11iIi11i % I11i1ii1 % oO0o
  if 2 - 2: I11i - Ii1I
def ii1Ii11I ( ) :
 if not os . path . exists ( IIIII ) :
  OOoO ( 'Change Log 19/2/17 - v3.4.2' , 'GenieTv Now Krypton Compatible,[CR] Tv Guide Removed And Replaced By External App,[CR] Boss Documentaries A Masterpiece By Jason Cadd,[CR] Updates To All Searches,[CR] StreamTeam Cleaned Up,[CR] Addon Overall CleanUp,[CR] General Maintence' )
  os . makedirs ( IIIII )
  if 58 - 58: ii1ii11IIIiiI + I11i - oOo0O0Ooo
  if 3 - 3: oO0o
def oooOoOOO0oo0o ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   Oo0oooO0oO ( )
  if oO0O0OO0O == 1 :
   IiIiII1 ( )
  if oO0O0OO0O == 2 :
   Iii1iiIi1II ( oOooO0 )
  if oO0O0OO0O == 3 :
   OO0O00oOo ( )
  if oO0O0OO0O == 4 :
   ii1II ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if oO0O0OO0O == 5 :
   iI1I ( )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 10200 , III1iII1I1ii + 'rated.png' , O0o0Oo , '' )
  if 100 - 100: iI11I1II1I1I + OOooOOo / I1ii11iIi11i . Ii
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']POPCORN BOX[/COLOR]' , str ( I1I1IiI1 ) , 7061 , III1iII1I1ii + 'PopcornBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Desi Flix[/COLOR]' , '' , 80005 , III1iII1I1ii + 'Desi.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , III1iII1I1ii + 'FilmTrailers.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , III1iII1I1ii + 'ClassicMovies.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def OO0O0OOo0O ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']DAILY LISTS[/COLOR]' , '' , 9007 , Oo00OOOOO , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Oo00OOOOO , O0o0Oo , '' )
 if 14 - 14: I11i * Ii1IIIi1 + O0OOOoOoo0 + o0o00Oo0O + Ii
 if 77 - 77: I11i / ii
 if 46 - 46: I11i % iI11I1II1I1I . O0OOOoOoo0 % O0OOOoOoo0 + Ii
 if 72 - 72: iI11I1II1I1I * ii1ii11IIIiiI % I11i1ii1 / oO0o
 if 35 - 35: I11i1ii1 + ooOoO0O00 % Ii1I % ooOOOoO + o000O0o
def iiiI ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']THE SOURCE[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']RETURN DATES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   I1ii1 ( )
  if oO0O0OO0O == 1 :
   O00 ( )
  if oO0O0OO0O == 2 :
   Oo0o0000OOoO ( )
  if oO0O0OO0O == 3 :
   IiIi1I1ii111 ( )
  if oO0O0OO0O == 4 :
   IiIiIi ( )
  if oO0O0OO0O == 5 :
   IIIII1 ( )
  if oO0O0OO0O == 6 :
   iIi1Ii1i1iI ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  if 16 - 16: Ii1IIIi1 / I1ii11iIi11i / ii * oOo0O0Ooo + ooOoO0O00 % Ii1IIIi1
  if 71 - 71: OOooOOo
  if 14 - 14: Ii % Ii1IIIi1
  iiOOooooO0Oo ( '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '' , 8020 , III1iII1I1ii + 'iWatchSeries.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RETURN DATES[/COLOR]' , str ( I1I1IiI1 ) , 10095 , III1iII1I1ii + 'RD.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC TV[/COLOR]' , str ( I1I1IiI1 ) , 8064 , III1iII1I1ii + 'ClassicTV.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , III1iII1I1ii + 'TVShowTrailers.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def OooO0oo ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   o0o0oOoOO0O = '[COLOR' + II + ']PANDORAS BOX[/COLOR]'
   if 16 - 16: I1111IIi % iI11I1II1I1I . ii1ii11IIIiiI
   if 59 - 59: oOo0O0Ooo * IIiIiII11i . o0o00Oo0O
   if 56 - 56: ii1ii11IIIiiI - O0OOOoOoo0 % oOo0O0Ooo - I11i
   if 51 - 51: o0o00Oo0O / I11i1ii1 * iI11I1II1I1I + Ii1I + I11i
  O0oO0 = [ o0o0oOoOO0O , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + II + ']RAIZ TV[/COLOR]' , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   Oo0OO0000oooo ( )
  if oO0O0OO0O == 1 :
   oo0 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , IiI111ii1ii , I1i1i1iii )
   if 7 - 7: o000O0o - oO0o - o0o00Oo0O % o000O0o - IIiIiII11i
   if 31 - 31: O0OOOoOoo0 / I1ii11iIi11i - O0OOOoOoo0 - Ii1IIIi1
   if 7 - 7: O0OOOoOoo0 % o0o00Oo0O . OOooOOo + oOo0O0Ooo - ooOOOoO
  if oO0O0OO0O == 2 :
   oo0 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , IiI111ii1ii , I1i1i1iii )
   if 75 - 75: ooOOOoO
   if 71 - 71: I11i1ii1
  if oO0O0OO0O == 3 :
   oo0 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , IiI111ii1ii , I1i1i1iii )
 else :
  if 53 - 53: ii % ii1ii11IIIiiI . I1111IIi / Ii % O0OOOoOoo0
  if 28 - 28: ooOOOoO
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']PANDORAS BOX[/COLOR]' , str ( I1I1IiI1 ) , 10025 , III1iII1I1ii + 'PandorasBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Technica-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'Roadrunner-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , III1iII1I1ii + 'raiztv.png' , O0o0Oo , '' )
  if 58 - 58: OOooOOo
  if 37 - 37: I1ii11iIi11i - iI11I1II1I1I / Ii1I
  if 73 - 73: Ii - I1111IIi
  if 25 - 25: ii + I1111IIi * Ii1I
  if 92 - 92: oOo0O0Ooo + ooOOOoO + o0o00Oo0O / I11i + iiiiiiii1
  if 18 - 18: I11i1ii1 * OOooOOo . O0OOOoOoo0 / Ii1I / Ii
 I1I11i ( 'movies' , 'MAIN' )
 if 21 - 21: o000O0o / Ii1I + ii1ii11IIIiiI + ii
def OoOo ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
def I1iI11iIiIi1 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( iIIIiIi )
 for oo000ii , OoO in i1IIIII11I1IiI :
  if '[DIR]' in oo000ii :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + OoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + OoO , 1018 , III1iII1I1ii + 'SilentHunter.png' )
  if 'mkv' in OoO :
   i1i1iII1 ( ( '[COLOR' + II + ']' + OoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + OoO , 222 , III1iII1I1ii + 'SilentHunter.png' )
  if 'avi' in OoO :
   i1i1iII1 ( ( '[COLOR' + II + ']' + OoO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + OoO , 222 , III1iII1I1ii + 'SilentHunter.png' )
   if 25 - 25: iI11I1II1I1I % O0OOOoOoo0 . I11i1ii1
def IIIIi1 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , III1iII1I1ii + 'scraped.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 if 3 - 3: iiiiiiii1
def i1iiIiI1Ii1i ( url ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , url , O0OOO0OOooo00 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o in i1IIIII11I1IiI :
  if I111iIi1 == '123' :
   I111iIi1 = III1iII1I1ii + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = III1iII1I1ii + 'appstreams.png'
  if 'php' in url :
   iiOOooooO0Oo ( I1i1i1iii , url , 100010 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1i1i1iii , url , 100007 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1i1i1iii , url , 100100 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o )
  elif not 'http' in url :
   OOo00OoO ( I1i1i1iii , url , 100009 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o , '' )
  else :
   OOo00OoO ( I1i1i1iii , url , 100005 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o , '' )
   if 10 - 10: I11i / Ii
def o00oO ( url ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 O00O0Ooooo00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , iIIii , oo00O00oO000o , o0ooooO0o0O , I1i1i1iii in O00O0Ooooo00 :
  if iIIii == '123' :
   iIIii = III1iII1I1ii + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = O0o0Oo
  if 'php' in url :
   iiOOooooO0Oo ( I1i1i1iii , url , 100004 , iIIii , o0ooooO0o0O , oo00O00oO000o )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1i1i1iii , url , 100007 , iIIii , o0ooooO0o0O , oo00O00oO000o )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1i1i1iii , url , 100100 , iIIii , o0ooooO0o0O , oo00O00oO000o )
  elif not 'http' in url :
   OOo00OoO ( I1i1i1iii , url , 100009 , iIIii , o0ooooO0o0O , oo00O00oO000o , '' )
  else :
   OOo00OoO ( I1i1i1iii , url , 100005 , iIIii , o0ooooO0o0O , oo00O00oO000o , '' )
   if 97 - 97: I11i1ii1 / iiiiiiii1 % ooOoO0O00 % Ii1I
def ii111I11iI ( url ) :
 if 93 - 93: Ii1I / iI11I1II1I1I * ooOoO0O00 % ii * o0o00Oo0O * ooOOOoO
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 Ooooooo = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1IIIiI1I1ii1 in Ooooooo :
  I111iIi1 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for I111iIi1 in I111iIi1 :
   I111iIi1 = I111iIi1
  I1i1i1iii = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for I1i1i1iii in I1i1i1iii :
   if 'elete' in I1i1i1iii :
    pass
   elif 'rivate Vid' in I1i1i1iii :
    pass
   else :
    I1i1i1iii = ( I1i1i1iii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  iiiI1I1iIIIi1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for iiiI1I1iIIIi1 in iiiI1I1iIIIi1 :
   iiiI1I1iIIIi1 = iiiI1I1iIIIi1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for url in url :
   url = url
  OOo00OoO ( '[COLORred]' + str ( iiiI1I1iIIIi1 ) + '[/COLOR] : ' + str ( I1i1i1iii ) , str ( url ) , 100009 , str ( I111iIi1 ) , O0o0Oo , '' , '' )
  I1I11i ( 'movies' , '' )
  if 17 - 17: iI11I1II1I1I . ii / ooOOOoO % IIiIiII11i % ooOoO0O00 / Ii
  if 58 - 58: I1ii11iIi11i . IIiIiII11i + o000O0o - Ii / IIiIiII11i / o0o00Oo0O
  if 85 - 85: OOooOOo + Ii1IIIi1
  if 10 - 10: I1111IIi / oO0o + OOooOOo / ooOoO0O00
  if 27 - 27: ii1ii11IIIiiI
def oO0OO0 ( iconimage , url , extra ) :
 I111iIi1 = ' '
 o0O0Oo00 = ' '
 o0ooooO0o0O = ' '
 O0Oo0o000oO = ' '
 oO0o00oOOooO0 = i1iIiiiiii1II ( url )
 I111iIi1 = re . compile ( '<img src="(.+?)">' ) . findall ( oO0o00oOOooO0 )
 for I111iIi1 in I111iIi1 :
  I111iIi1 = I111iIi1
 OOOoO000 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( oO0o00oOOooO0 )
 for o0ooooO0o0O in OOOoO000 :
  o0ooooO0o0O = o0ooooO0o0O
 i1IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( oO0o00oOOooO0 )
 for url , O0Oo0o000oO in i1IIIII11I1IiI :
  O0Oo0o000oO = 'S' + ( O0Oo0o000oO ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oO0Oo + url
  oOOOO ( ( O0Oo0o000oO ) . replace ( '  ' , '' ) , url , 100101 , I111iIi1 , o0ooooO0o0O , o0O0Oo00 , '' )
  I1I11i ( 'Movies' , 'info' )
  if 49 - 49: IIiIiII11i . o000O0o . Ii % I1111IIi
def i11i1iiI1i ( url , name , fanart , extra , iconimage ) :
 oO0oOOoo00000 = extra
 O0Oo0o000oO = name
 oO0o00oOOooO0 = i1iIiiiiii1II ( url )
 I111iIi1 = iconimage
 i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( oO0o00oOOooO0 )
 for url , name , oOo00 in i1IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oO0Oo + url
  oOo00 = oOo00
  i1iI11i1IIi = name + ' - [COLORred]' + oOo00 + '[/COLOR]'
  oOOOO ( i1iI11i1IIi , url , 100102 , I111iIi1 , fanart , 'Aired : ' + oOo00 , i1iI11i1IIi )
  if 4 - 4: ii - Ii1I * oOo0O0Ooo
def I1iIiI11I1 ( name , URL , iconimage , fanart ) :
 oO0OOoo0OO = i1iIiiiiii1II ( URL )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , name in i1IIIII11I1IiI :
  for oooO in oOOoo0Oo :
   if oooO in oOooO0 :
    URL = 'http://www.watchseriesgo.to/link/' + oOooO0
    OOo00OoO ( name , URL , 100106 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( i1IIIII11I1IiI ) <= 0 :
  oOOOO ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 27 - 27: ii1ii11IIIiiI . Ii % iiiiiiii1
  if 65 - 65: IIiIiII11i . oOo0O0Ooo % o000O0o * oO0o
def iI11I ( url , name ) :
 I1IIIiii1 = name
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 Iii1I1111ii = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  O00oo ( url , I1IIIiii1 )
 for url in i1I :
  O00oo ( url , I1IIIiii1 )
 for url in Iii1I1111ii :
  O00oo ( url , I1IIIiii1 )
  if 77 - 77: O0OOOoOoo0 % Ii1IIIi1 - ooOOOoO % I11i1ii1 - oO0o / I1ii11iIi11i
def O00oo ( url , season_name ) :
 if 'daclips.in' in url :
  Ii1iI111 ( url , season_name )
 elif 'filehoot.com' in url :
  O0oooo00o0Oo ( url , season_name )
 elif 'allmyvideos.net' in url :
  I1iii ( url , season_name )
 elif 'vidspot.net' in url :
  oO0o0O0Ooo0o ( url , season_name )
 elif 'vodlocker' in url :
  i1Ii11II ( url , season_name )
 elif 'vidto' in url :
  IioO0oOOO0Ooo ( url , season_name )
  if 38 - 38: oOo0O0Ooo
  if 84 - 84: o000O0o % ooOoO0O00
def IioO0oOOO0Ooo ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOO , I1i1i1iii in i1IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 89 - 89: iiiiiiii1 + ii + iiiiiiii1 * ooOoO0O00 + iI11I1II1I1I % ooOOOoO
  if 59 - 59: Ii1IIIi1 + Ii
def I1iii ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOO , I1i1i1iii in i1IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 88 - 88: Ii - I11i1ii1
def oO0o0O0Ooo0o ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0OOoo0OO )
 for oOO , I1i1i1iii in i1IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 67 - 67: Ii1IIIi1 . I1ii11iIi11i + OOooOOo - ii
def i1Ii11II ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOO in i1IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 70 - 70: Ii1IIIi1 / IIiIiII11i - iI11I1II1I1I - O0OOOoOoo0
def Ii1iI111 ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0OOoo0OO )
 for oOO in i1IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 11 - 11: iI11I1II1I1I . ii . IIiIiII11i / ooOoO0O00 - ooOOOoO
def O0oooo00o0Oo ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOO in i1IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 30 - 30: OOooOOo
def Ii1II ( Link , season_name ) :
 if 'http:/' in Link :
  Ii111 ( Link )
  if 67 - 67: o0o00Oo0O
def Oooooooo0o ( url ) :
 oO0OOoo0OO = OPEN_URL_1 ( url )
 oo0OoOOO0o0 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 for url in oo0OoOOO0o0 :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 19 - 19: IIiIiII11i * I1111IIi + ii1ii11IIIiiI
def oOOOO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0ooO00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11i1iIiii = True
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOO00OO0oOo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1I1iI = [ ]
  if 16 - 16: I1111IIi * OOooOOo . I11i1ii1 / ooOoO0O00 . oO0o - ooOoO0O00
  if showcontext == 'fav' :
   I1I1iI . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   I1I1iI . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OOO00OO0oOo . addContextMenuItems ( I1I1iI )
 i11i1iIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = True )
 return i11i1iIiii
 if 46 - 46: I1111IIi + iI11I1II1I1I + Ii1IIIi1 + oO0o . Ii1I
 if 1 - 1: o000O0o
def OOo00OoO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0ooO00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11i1iIiii = True
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOO00OO0oOo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1I1iI = [ ]
  I1I1iI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1I1iI . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   I1I1iI . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OOO00OO0oOo . addContextMenuItems ( I1I1iI )
 i11i1iIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = False )
 return i11i1iIiii
 if 62 - 62: ooOoO0O00 - Ii1IIIi1
def ooIII1i1iI1 ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 97 - 97: ooOOOoO - Ii
def i1iIi1II11 ( url ) :
 i1I1II1iIIi11 = xbmc . Player ( IiI1iII1II111 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : i1I1II1iIIi11 . play ( url ) . strip ( )
 except : pass
 if 28 - 28: OOooOOo * oO0o . ooOOOoO % ooOOOoO / ooOOOoO * iiiiiiii1
def Ii111 ( url ) :
 i1I1II1iIIi11 = xbmc . Player ( )
 import urlresolver
 try : i1I1II1iIIi11 . play ( url )
 except : pass
 if 64 - 64: IIiIiII11i - oOo0O0Ooo
def i1iIiiiiii1II ( url ) :
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
  if 68 - 68: I11i1ii1 - Ii1IIIi1 - iI11I1II1I1I / OOooOOo + Ii1IIIi1 - oO0o
  if 75 - 75: O0OOOoOoo0 / I11i % iI11I1II1I1I . ii % ii % IIiIiII11i
  if 26 - 26: IIiIiII11i % Ii % iI11I1II1I1I % ooOOOoO * ooOOOoO * Ii1I
def i11OOoo ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   IiI1I11iIii ( )
  if oO0O0OO0O == 1 :
   O000O0OO00oo ( )
  if oO0O0OO0O == 2 :
   oOOO ( )
  if oO0O0OO0O == 3 :
   ooo0oooo0 ( )
  if oO0O0OO0O == 4 :
   OOO0ooo ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def O0OOo ( ) :
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
 if 7 - 7: I11i + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
 if 22 - 22: I11i1ii1 - I11i1ii1 % Ii1IIIi1 . iiiiiiii1 + o000O0o
 if 63 - 63: oOo0O0Ooo % iiiiiiii1 * I11i + iiiiiiii1 / I1ii11iIi11i % O0OOOoOoo0
def OO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 i1IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0OOoo0OO )
 for IIiIi1iI in i1IIIII11I1IiI :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   iiI1i1Iii111 = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OOoO ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + iiI1i1Iii111 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   oO0O0OO0O = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if oO0O0OO0O == 0 :
    i111I11i ( IIiIi1iI )
    I1iIIiiIIi1i ( )
   elif oO0O0OO0O == 1 :
    ii1OoOO ( IIiIi1iI )
  else :
   pass
   if 44 - 44: Ii1IIIi1
def ii1OoOO ( addon ) :
 iiI1i1Iii111 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 54 - 54: ii1ii11IIIiiI - ooOOOoO - iiiiiiii1 . iI11I1II1I1I
def i111I11i ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 o0OIIiI1I1 = os . path . join ( I11II1i , 'default.py' )
 I11I1IIiiII1 = open ( o0OIIiI1I1 , "w+" )
 if 31 - 31: oOo0O0Ooo * o000O0o + ii - O0OOOoOoo0 / ii
 I11I1IIiiII1 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 I11I1IIiiII1 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 I11I1IIiiII1 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 19 - 19: I1111IIi * I11i1ii1 * I11i + o0o00Oo0O / o0o00Oo0O
 if 73 - 73: iI11I1II1I1I / iI11I1II1I1I - o000O0o
 if 91 - 91: o000O0o + oOo0O0Ooo
 if 59 - 59: oOo0O0Ooo + Ii + ooOoO0O00 / ooOOOoO
def I11iIiI1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 oo0oooOo = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0OO0O0Oo = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 Iii1I1111ii = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii1iii1i = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OOOOO = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , url , iII1iIi11i , o0ooooO0o0O , oo00O00oO000o in oo0oooOo :
  if 'php' in url :
   iiOOooooO0Oo ( I1i1i1iii , url , 90037 , iII1iIi11i , o0ooooO0o0O , oo00O00oO000o )
  elif I1i1i1iii == 'Search' :
   iiOOooooO0Oo ( 'Search' , url , 90038 , iII1iIi11i , o0ooooO0o0O , oo00O00oO000o )
  else :
   OOiIiIIi1 ( I1i1i1iii , url , 222 , iII1iIi11i , o0ooooO0o0O , oo00O00oO000o )
 for I1i1i1iii , iIIii , url , OOoOOo0O00O in o0OO0O0Oo :
  iiOOooooO0Oo ( I1i1i1iii , url , 90037 , iIIii , OOoOOo0O00O , '' )
 for I1i1i1iii , iIIii , url , OOoOOo0O00O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 90037 , iIIii , OOoOOo0O00O , '' )
 for I1i1i1iii , url , iIIii , OOoOOo0O00O in i1I :
  OOiIiIIi1 ( I1i1i1iii , url , 222 , iIIii , OOoOOo0O00O , '' )
 for I1i1i1iii , url , iIIii , OOoOOo0O00O in Iii1I1111ii :
  OOiIiIIi1 ( I1i1i1iii , url , 222 , iIIii , OOoOOo0O00O , '' )
 for I1i1i1iii , url , iIIii , OOoOOo0O00O in ii1iii1i :
  OOiIiIIi1 ( I1i1i1iii , url , 222 , iIIii , OOoOOo0O00O , '' )
 for I1i1i1iii , url , iIIii in OOOOO :
  OOiIiIIi1 ( I1i1i1iii , url , 222 , iIIii , '' , '' )
  I1I11i ( 'tvshows' , 'Media Info 3' )
  if 36 - 36: o0o00Oo0O + I1ii11iIi11i
def iIIIi1i1I11i ( ) :
 oOO0OO0OO = [ 'serialsearch' , 'moviesearch' ]
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 if i1ii11 == '' :
  pass
 else :
  for ii1i in oOO0OO0OO :
   IIi = I11 + ii1i + '.php'
   oO0o00oOOooO0 = OoOooO ( IIi )
   if oO0o00oOOooO0 != 'Opened' :
    O00O0Ooooo00 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( oO0o00oOOooO0 )
    for I1i1i1iii , oOooO0 , iII1iIi11i , o0ooooO0o0O , oo00O00oO000o in O00O0Ooooo00 :
     if i1ii11 in I1i1i1iii . lower ( ) :
      oo0OO = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for oooO in oo0OO :
       if oooO == oOooO0 :
        I1i1i1iii = '[COLORred]* [/COLOR]' + ( I1i1i1iii ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        IiiI11i1I = open ( o00OO00OoO , "a" )
        IiiI11i1I . write ( 'item="' + I1i1i1iii + '"\n' )
        IiiI11i1I . close
      if 'php' in oOooO0 :
       iiOOooooO0Oo ( I1i1i1iii , oOooO0 , 90037 , iII1iIi11i , o0ooooO0o0O , oo00O00oO000o )
      else :
       OOiIiIIi1 ( I1i1i1iii , oOooO0 , 222 , iII1iIi11i , o0ooooO0o0O , oo00O00oO000o )
       if 80 - 80: Ii1IIIi1 / ooOOOoO / OOooOOo + ooOoO0O00 - I1ii11iIi11i
   I1I11i ( 'tvshows' , 'Media Info 3' )
   if 11 - 11: I11i * oO0o
def iIi1IiI ( ) :
 oO0OOoo0OO = OoOooO ( 'http://www.tvcatchup.com/channels/' )
 O0 = OoOooO ( 'http://www.djing.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 I11IIIiIi11 = re . compile ( 'title="([^"]*)" >.+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( O0 )
 for IIiiiiiiIi1I1 , iIIii , oOooO0 in i1IIIII11I1IiI :
  i1i1iII1 ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + oOooO0 , 90024 , 'http://www.tvcatchup.com' + iIIii )
 for IIiiiiiiIi1I1 , oOooO0 , iIIii in I11IIIiIi11 :
  i1i1iII1 ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + oOooO0 , 90024 , iIIii )
 for oOooO0 , iIIii , I1i1i1iii in i1I :
  if 'Submit' in I1i1i1iii :
   pass
  elif '&lt;' in I1i1i1iii :
   pass
  else :
   OOiIiIIi1 ( 'DJing  ' + I1i1i1iii , oOooO0 , 90025 , 'http://www.djing.com' + iIIii , O0o0Oo , '' )
  I1I11i ( 'movies' , 'MAIN' )
def I11iiIi1i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 if 41 - 41: ii1ii11IIIiiI % Ii1I
 i1IIIII11I1IiI = re . compile ( "file: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  O00Oo0 ( url )
def i1iIiIi1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  i1I1IIIiiI ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 71 - 71: Ii1IIIi1 * oO0o % ii % oO0o / oOo0O0Ooo
def IiIiII1 ( ) :
 if 56 - 56: ii % Ii * iI11I1II1I1I . oO0o * o0o00Oo0O
 if 23 - 23: Ii
 if 39 - 39: I11i - Ii1I % O0OOOoOoo0 * oO0o - Ii1IIIi1 / O0OOOoOoo0
 if 29 - 29: Ii1I
 if 52 - 52: Ii / ooOoO0O00
 if 1 - 1: I11i1ii1
 oO0OOoo0OO = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'yr' in oOooO0 :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + oOooO0 , 10201 , III1iII1I1ii + 'rated.png' )
   if 78 - 78: Ii1I + ooOOOoO - o0o00Oo0O
def i1I1iIi1IiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1111O0O000OOOo , url , I1i1i1iii in i1IIIII11I1IiI :
  if 'id' in url :
   Iiiiii111i1ii ( ( '[COLORred]RANK [COLORblue]' + i1111O0O000OOOo + '[COLORred] - [COLORblue]' + I1i1i1iii + '[/COLOR]' ) , I1i1i1iii , 10202 , III1iII1I1ii + 'rated.png' )
   if 12 - 12: o000O0o
def Oo0O ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 Ii11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOOoooO = ( url )
 i1ii11 = oOOoooO . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( oOOoooO ) . replace ( ' ' , '+' )
 OoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 II1i111 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1iiiIii11 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OOoOOO000O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oOo0II1i11I1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiIiIiII = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOOoooO
 i1I1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 10 - 10: oO0o / I1ii11iIi11i
 I1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 II11iIII1i1I = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 63 - 63: I1ii11iIi11i + iiiiiiii1 - IIiIiII11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( OoO )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1i111 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( i1iiiIii11 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 i1iIIi1I1I11 = O0o0O00Oo0o0 ( OOoOOO000O0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iii1III1i = O0o0O00Oo0o0 ( iiIiIiII )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 iiiIi = O0o0O00Oo0o0 ( i1I1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 II1Iii = O0o0O00Oo0o0 ( iIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 73 - 73: ooOOOoO * ii . o0o00Oo0O . I1111IIi
 if 55 - 55: I1ii11iIi11i
 ooO0o = O0o0O00Oo0o0 ( I1i )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 ii1iI1iI1 = O0o0O00Oo0o0 ( II11iIII1i1I )
 if 55 - 55: I11i1ii1 + Ii1IIIi1
 if 18 - 18: o000O0o - I11i - oOo0O0Ooo - oOo0O0Ooo
 if 54 - 54: I1ii11iIi11i + oOo0O0Ooo / O0OOOoOoo0 . oOo0O0Ooo * OOooOOo
 if 1 - 1: OOooOOo * oO0o . ooOoO0O00 / I1ii11iIi11i . Ii1I + I1ii11iIi11i
 if 17 - 17: I1ii11iIi11i + oO0o / ii1ii11IIIiiI / O0OOOoOoo0 * Ii1IIIi1
 if 29 - 29: oO0o % ii * o000O0o / IIiIiII11i - o000O0o
 if 19 - 19: Ii
 if 54 - 54: IIiIiII11i . ooOOOoO
 if 73 - 73: OOooOOo . oOo0O0Ooo
 if 32 - 32: OOooOOo * oOo0O0Ooo % I11i1ii1 * ii1ii11IIIiiI . o0o00Oo0O
 if 48 - 48: O0OOOoOoo0 * O0OOOoOoo0
 if 13 - 13: ii1ii11IIIiiI / ooOOOoO + OOooOOo . I11i % I11i1ii1
 if 48 - 48: oOo0O0Ooo / Ii - I11i * o000O0o / ii
 if II1Iii != 'Failed' :
  OoOoi1i = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( II1Iii )
  for url , I1i1i1iii in OoOoi1i :
   IIIiiiI = O0o0O00Oo0o0 ( url )
   OoO00oo00 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIIiiiI )
   for Oo0Oo0O , iiiI1i11Ii in OoO00oo00 :
    iiiI1i11Ii = ( iiiI1i11Ii . replace ( '.' , ' ' ) )
    if i1ii11 in iiiI1i11Ii . lower ( ) :
     if '.mkv' in Oo0Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , url + Oo0Oo0O , 222 , '' , '' , '' )
     elif '.mp4' in Oo0Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , url + Oo0Oo0O , 222 , '' , '' , '' )
     elif '.avi' in Oo0Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , url + Oo0Oo0O , 222 , '' , '' , '' )
     elif '.wav' in Oo0Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , url + Oo0Oo0O , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , url + Oo0Oo0O , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 16 - 16: I1ii11iIi11i / Ii
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for url , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in i1I :
   if oOOoooO in I1i1i1iii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 64 - 64: Ii / ii1ii11IIIiiI * ooOoO0O00
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 73 - 73: I1ii11iIi11i - OOooOOo - o000O0o - oOo0O0Ooo
 if ii1ii1ii != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for oo0o0oOo , I1i1i1iii in Iii1I1111ii :
   if oOOoooO in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( II1i111 + oo0o0oOo ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  ii1iii1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for url , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in ii1iii1i :
   if oOOoooO in I1i1i1iii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 58 - 58: I11i - IIiIiII11i % o000O0o + iiiiiiii1 . OOooOOo / I1111IIi
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if i1iIIi1I1I11 != 'Failed' :
  IIo00ooo = [ ]
  OOOOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIi1I1I11 )
  for url , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in OOOOO :
   if oOOoooO in I1i1i1iii . lower ( ) :
    if I1i1i1iii in IIo00ooo :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
     IIo00ooo . append ( I1i1i1iii )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1III1i != 'Failed' :
  Ii1IiIiIi1IiI = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iii1III1i )
  for url , iIIii , I1i1i1iii in Ii1IiIiIi1IiI :
   if oOOoooO in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , iIIii )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 36 - 36: I1111IIi - ii / oO0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: I11i1ii1
    if 45 - 45: I11i1ii1 / I1ii11iIi11i / ii1ii11IIIiiI
    if 44 - 44: Ii1I - ii1ii11IIIiiI / IIiIiII11i * oO0o * I1ii11iIi11i
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
 if ooO0o != 'Failed' :
  oOooo0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO0o )
  for url , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in oOooo0Oo :
   if oOOoooO in I1i1i1iii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 66 - 66: I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 28 - 28: I1111IIi - I1111IIi . ooOoO0O00 - I11i1ii1 + oOo0O0Ooo . I1111IIi
    if 54 - 54: OOooOOo - iiiiiiii1
    if 3 - 3: oOo0O0Ooo - I1ii11iIi11i
    if 16 - 16: o000O0o + I11i1ii1 / I11i
    if 82 - 82: I1111IIi * Ii % IIiIiII11i - ii
    if 90 - 90: I1ii11iIi11i . o000O0o * ooOoO0O00 - ooOoO0O00
    if 16 - 16: oOo0O0Ooo * ooOoO0O00 - I11i . I1111IIi % ooOOOoO / I11i
    if 14 - 14: iI11I1II1I1I * iiiiiiii1 * Ii1I / iI11I1II1I1I * I1111IIi / ooOOOoO
    if 77 - 77: oO0o + iiiiiiii1 + iiiiiiii1 * ii1ii11IIIiiI / ii . ii1ii11IIIiiI
    if 62 - 62: ooOoO0O00 - ooOoO0O00
 oOOO0O0Ooo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 4 - 4: IIiIiII11i . ooOOOoO + ii1ii11IIIiiI * iiiiiiii1 . I11i1ii1
 for ii1i in oOOO0O0Ooo :
  IIi = O0Oo000ooO00 + ii1i + I1IIIii
  II1Iii = O0o0O00Oo0o0 ( IIi )
  if II1Iii != 'Failed' :
   OoOoi1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II1Iii )
   for url , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in OoOoi1i :
    if oOOoooO in I1i1i1iii . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 87 - 87: OOooOOo / oO0o / Ii
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 74 - 74: o000O0o / Ii1I % I11i
 oOOO0O0Ooo = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 88 - 88: OOooOOo - Ii % I11i * ooOOOoO + Ii1I
 if 52 - 52: IIiIiII11i . oOo0O0Ooo + OOooOOo % oO0o
 for ii1i in oOOO0O0Ooo :
  IIi = Ii11 + ii1i
  oo0O0o00 = O0o0O00Oo0o0 ( IIi )
  if oo0O0o00 != 'Failed' :
   oOoO0o = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0O0o00 )
   for oo0o0oOo , I1i1i1iii in oOoO0o :
    if oOOoooO in I1i1i1iii . lower ( ) :
     i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( Ii11 + ii1i + oo0o0oOo ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 46 - 46: iiiiiiii1 % ii1ii11IIIiiI
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 72 - 72: iI11I1II1I1I
def IiIiIi ( ) :
 Iiiiii111i1ii ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , III1iII1I1ii + 'running.png' )
 Iiiiii111i1ii ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , III1iII1I1ii + 'countdown.png' )
 Iiiiii111i1ii ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , III1iII1I1ii + 'unknown.png' )
 Iiiiii111i1ii ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , III1iII1I1ii + 'cancelled.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 45 - 45: I1ii11iIi11i - I11i % iiiiiiii1
def i1IIi1i1Ii1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , O0Oo0o000oO , Iii , oOo00 , o0Oo0oO in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLORblue]' + I1i1i1iii + '[/COLOR] [COLORred]Season[/COLOR]-' + O0Oo0o000oO + ' [COLORred]Returns [/COLOR]- ' + o0Oo0oO + ' ' + oOo00 ) , I1i1i1iii , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 48 - 48: o000O0o . I11i / o000O0o
def Oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , O0Oo0o000oO , Iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLORblue]' + I1i1i1iii + '[/COLOR] [COLORred]Season[/COLOR]-' + O0Oo0o000oO + ' [COLORred] Status Unknown[/COLOR] ' ) , I1i1i1iii , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 66 - 66: I1111IIi
def O0oOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , O0Oo0o000oO , Iii , oOo00 in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLORblue]' + I1i1i1iii + ' [COLORred] Cancelled On[/COLOR] ' + oOo00 ) , I1i1i1iii , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 68 - 68: Ii1I % ii % Ii1I + iiiiiiii1
def iIiIIi ( url ) :
 oOOoooO = ( url )
 i1ii11 = oOOoooO . lower ( )
 if 14 - 14: I11i / Ii1IIIi1 - iI11I1II1I1I - o000O0o % I11i1ii1
 if 49 - 49: I11i1ii1 * o000O0o / I11i / I1ii11iIi11i * iI11I1II1I1I
 Oo0Oo0O = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( oOOoooO ) . replace ( ' ' , '+' )
 OoO = 'http://onlinemovies.tube/?s=' + ( oOOoooO ) . replace ( ' ' , '+' )
 II1i111 = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i1iiiIii11 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oOo0II1i11I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 57 - 57: OOooOOo - o000O0o / I11i1ii1 % Ii
 i1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 I11oOOooo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 80 - 80: oOo0O0Ooo - Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 69 - 69: o000O0o % ii . oOo0O0Ooo
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 34 - 34: ii1ii11IIIiiI * OOooOOo - I1111IIi - oOo0O0Ooo - ii1ii11IIIiiI
 if 42 - 42: IIiIiII11i * oOo0O0Ooo % ooOoO0O00 - ii1ii11IIIiiI % I1111IIi
 Ii1I1 = O0o0O00Oo0o0 ( Oo0Oo0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( OoO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1i111 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( i1iiiIii11 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 oo0O0o00 = O0o0O00Oo0o0 ( oOo0II1i11I1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 58 - 58: I1111IIi - ooOOOoO % oOo0O0Ooo
 if 4 - 4: ooOoO0O00 + I11i1ii1 + ooOoO0O00
 iiiIi = O0o0O00Oo0o0 ( i1I1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 II1Iii = O0o0O00Oo0o0 ( iIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 i11IiIIi11I = O0o0O00Oo0o0 ( I11oOOooo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 78 - 78: I1111IIi
 if II1Iii != 'Failed' :
  OoOoi1i = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( II1Iii )
  for url , I1i1i1iii in OoOoi1i :
   IIIiiiI = O0o0O00Oo0o0 ( url )
   OoO00oo00 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIIiiiI )
   for Oo0Oo0O , iiiI1i11Ii in OoO00oo00 :
    if i1ii11 in iiiI1i11Ii . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , url + Oo0Oo0O , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % iiiiiiii1 . Ii1I % o0o00Oo0O
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if iiiIi != 'Failed' :
  iIiIi1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiiIi )
  for url , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in iIiIi1ii :
   if i1ii11 in I1i1i1iii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 28 - 28: iI11I1II1I1I + iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 28 - 28: o000O0o
    if 52 - 52: oOo0O0Ooo + iI11I1II1I1I
    if 71 - 71: o0o00Oo0O / o000O0o
    if 34 - 34: OOooOOo . iI11I1II1I1I % o0o00Oo0O
    if 43 - 43: Ii1I - O0OOOoOoo0
    if 70 - 70: O0OOOoOoo0 / Ii1IIIi1 % I11i1ii1 - ii1ii11IIIiiI
    if 47 - 47: O0OOOoOoo0
    if 92 - 92: Ii1IIIi1 + OOooOOo % ooOoO0O00
    if 23 - 23: iiiiiiii1 - Ii1IIIi1 + ii1ii11IIIiiI - OOooOOo * OOooOOo . I1ii11iIi11i
    if 47 - 47: o000O0o % iI11I1II1I1I
    if 11 - 11: oOo0O0Ooo % ii1ii11IIIiiI - oO0o - o000O0o + I11i
 if i11IiIIi11I != 'Failed' :
  o0O0O0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i11IiIIi11I )
  for url , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in o0O0O0 :
   if i1ii11 in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , IiI111ii1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 55 - 55: o0o00Oo0O - iiiiiiii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  oOO0o0oo0 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for url , iIIii , I1i1i1iii , oOo000O in i1I :
   if i1ii11 in I1i1i1iii . lower ( ) :
    if 'season' in oOo000O :
     Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , iIIii , iIIii , '' )
    if 'episodes' in oOo000O :
     Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , iIIii , iIIii , '' )
  for url in oOO0o0oo0 :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 1 - 1: iI11I1II1I1I
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if Ii1I1 != 'Failed' :
  o0OO0O0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( Ii1I1 )
  for url , I1i1i1iii , iIIii in o0OO0O0Oo :
   if i1ii11 in I1i1i1iii . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1i1i1iii ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , iIIii , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 54 - 54: ii - oOo0O0Ooo % Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 92 - 92: oO0o * I11i1ii1
    if 35 - 35: Ii
    if 99 - 99: IIiIiII11i . I11i + o0o00Oo0O
    if 71 - 71: I1111IIi + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
    if 55 - 55: ii + iiiiiiii1 + ii * I11i1ii1
    if 68 - 68: o0o00Oo0O
    if 2 - 2: oO0o + o0o00Oo0O * oO0o - ii1ii11IIIiiI + o000O0o
    if 43 - 43: Ii1I - OOooOOo
    if 36 - 36: Ii1I - O0OOOoOoo0
 if ii1ii1ii != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for I1i1i1iii in Iii1I1111ii :
   if i1ii11 in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( II1i111 + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 24 - 24: I11i + I11i1ii1 + ooOOOoO - iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  ii1iii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for I1i1i1iii in ii1iii1i :
   if i1ii11 in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i1iiiIii11 + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 49 - 49: ooOOOoO . I11i1ii1 * OOooOOo % I1111IIi . o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0O0o00 != 'Failed' :
  oOoO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0O0o00 )
  for url , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in oOoO0o :
   if i1ii11 in I1i1i1iii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 48 - 48: o0o00Oo0O * ii1ii11IIIiiI - o0o00Oo0O / ii1ii11IIIiiI + OOooOOo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 52 - 52: oO0o % ii1ii11IIIiiI * IIiIiII11i
 I1IiIii11I = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for ii1i in I1IiIii11I :
  IIi = O0Oo000ooO00 + ii1i + I1IIIii
  ooO0o = O0o0O00Oo0o0 ( IIi )
  if ooO0o != 'Failed' :
   oOooo0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( ooO0o )
   for I1i1i1iii , oo00O00oO000o , url , iIIii , o0ooooO0o0O , O0OOO0OOooo00 in oOooo0Oo :
    if i1ii11 in I1i1i1iii . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgold] - Source Pandoras[/COLOR]' , url , O0OOO0OOooo00 , iIIii , o0ooooO0o0O , oo00O00oO000o )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 29 - 29: I11i
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 86 - 86: IIiIiII11i . I1111IIi
     if 2 - 2: ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: oO0o
def oO00Ooo0oO ( ) :
 if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % ii1ii11IIIiiI - iI11I1II1I1I
 if 17 - 17: ooOOOoO / I11i % I1ii11iIi11i
 if 71 - 71: I1111IIi . iiiiiiii1 . oO0o
 if 68 - 68: Ii % o000O0o * oO0o * I1111IIi * IIiIiII11i + o0o00Oo0O
 if 66 - 66: ooOOOoO % Ii1I % ii
 if 34 - 34: I11i / O0OOOoOoo0 % o0o00Oo0O . oO0o . ooOoO0O00
 if 29 - 29: o0o00Oo0O . iiiiiiii1
 if 66 - 66: o000O0o * iI11I1II1I1I % iI11I1II1I1I * I1111IIi - I11i1ii1 - I1111IIi
 if 70 - 70: iiiiiiii1 + o000O0o
 if 93 - 93: iiiiiiii1 + ii1ii11IIIiiI
 if 33 - 33: o0o00Oo0O
 Iiiiii111i1ii ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , III1iII1I1ii + 'seasons.png' )
 Iiiiii111i1ii ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , III1iII1I1ii + 'episodes.png' )
 Iiiiii111i1ii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 78 - 78: o0o00Oo0O / IIiIiII11i * oO0o
def IiIi1iI11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , iiI1iI1I in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( I1i1i1iii + ' - ' + iiI1iI1I ) . replace ( '&amp;' , '&' ) , url , 90053 , III1iII1I1ii + 'seasons.png' )
  if 27 - 27: Ii1I * iiiiiiii1 - oO0o + ii1ii11IIIiiI * ii1ii11IIIiiI
def o0OO0O0OO0oO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , url , 90054 , III1iII1I1ii + 'episodes.png' )
  if 9 - 9: o000O0o % Ii / I1ii11iIi11i
def IIIiI1ii1IIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for iIIii , I1i1i1iii , url in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , url , 90054 , iIIii )
 for url in next :
  Iiiiii111i1ii ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 55 - 55: O0OOOoOoo0 - oO0o
def o0i1I11iI1iiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for iIIii , iiI1iI1I , url , I1i1i1iii , I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI1iI1I + ' - ' + I1i1i1iii + ' - ' + I1 , url , 90044 , iIIii , iIIii , '' )
 for iIIii , I1i1i1iii , url in i1I :
  Iiiiii111i1ii ( I1i1i1iii , url , 90044 , iIIii , iIIii , '' )
 for url in next :
  Iiiiii111i1ii ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 14 - 14: oOo0O0Ooo . ii1ii11IIIiiI
def i1iI1i1I1 ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Oo0 = 'http://onlinemovies.tube/?s=' + ( oOOoooO ) . replace ( ' ' , '+' )
 i1ii11 = O0Oo0 . lower ( )
 oO0OOoo0OO = OoOooO ( i1ii11 )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iIIii , I1i1i1iii , oOo000O in i1IIIII11I1IiI :
  if 'season' in oOo000O :
   Iiiiii111i1ii ( I1i1i1iii , oOooO0 , 90054 , iIIii , iIIii , '' )
  if 'episodes' in oOo000O :
   Iiiiii111i1ii ( I1i1i1iii , oOooO0 , 90044 , iIIii , iIIii , '' )
 for oOooO0 in next :
  Iiiiii111i1ii ( 'NEXT' , oOooO0 , 90053 , III1iII1I1ii + 'Next.png' )
  if 80 - 80: oOo0O0Ooo - iI11I1II1I1I . Ii1IIIi1 + oO0o - iiiiiiii1
def iI1iIiiiI1I1 ( ) :
 if 78 - 78: o000O0o / oO0o - o000O0o * ii . OOooOOo
 if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
 if 37 - 37: ooOoO0O00 - Ii1IIIi1 % ii / Ii1IIIi1 % I11i1ii1
 if 48 - 48: Ii % o000O0o
 if 29 - 29: O0OOOoOoo0 + Ii % ooOOOoO
 if 93 - 93: OOooOOo % iI11I1II1I1I
 if 90 - 90: oOo0O0Ooo - Ii1IIIi1 / ii1ii11IIIiiI / o0o00Oo0O / ooOOOoO
 if 87 - 87: OOooOOo / I1111IIi + iI11I1II1I1I
 if 93 - 93: iI11I1II1I1I + o000O0o % I11i1ii1
 if 21 - 21: Ii1IIIi1
 Iiiiii111i1ii ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , III1iII1I1ii + 'allmov.png' )
 Iiiiii111i1ii ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , III1iII1I1ii + 'Genre.png' )
 Iiiiii111i1ii ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , III1iII1I1ii + 'Years.png' )
 Iiiiii111i1ii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 6 - 6: I1111IIi
def i1I1II ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , iiI1iI1I in i1IIIII11I1IiI :
  if 'genre' in url :
   Iiiiii111i1ii ( ( I1i1i1iii + ' - ' + iiI1iI1I ) . replace ( '&amp;' , '&' ) , url , 90043 , III1iII1I1ii + 'Genre.png' )
   if 17 - 17: o0o00Oo0O * OOooOOo * Ii1I * IIiIiII11i * ooOOOoO % ooOoO0O00
def IIiIi1iI1iII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if 'release' in url :
   Iiiiii111i1ii ( I1i1i1iii , url , 90043 , III1iII1I1ii + 'Years.png' )
   if 80 - 80: ooOoO0O00 + Ii - iiiiiiii1 % IIiIiII11i . o000O0o
def i111i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for iIIii , I1i1i1iii , II1III1i1iiI , url , oo00O00oO000o in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii + ' ' + II1III1i1iiI , url , 90044 , iIIii , iIIii , oo00O00oO000o )
 for iIIii , I1i1i1iii , oOo000O , url , I11i11i1 , oo00O00oO000o in i1I :
  if 'movies' in oOo000O :
   iiOOooooO0Oo ( I1i1i1iii + ' - ' + I11i11i1 , url , 90044 , iIIii , iIIii , oo00O00oO000o )
 for url in next :
  Iiiiii111i1ii ( 'NEXT' , url , 90043 , III1iII1I1ii + 'Next.png' )
  if 68 - 68: I1ii11iIi11i . I1ii11iIi11i - Ii1I / ooOOOoO . I11i1ii1 / ooOoO0O00
def iI1i1iIi1iiII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  o0OoO0000o ( 'http:' + url )
  if 90 - 90: I1111IIi . I11i1ii1 / iI11I1II1I1I
def o0OoO0000o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( ( I1i1i1iii ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , III1iII1I1ii + 'movhub.png' )
def I1IIi1I ( ) :
 if 14 - 14: o000O0o + o0o00Oo0O / I1111IIi
 if 24 - 24: oO0o - o000O0o + Ii1I / O0OOOoOoo0 % oOo0O0Ooo + iI11I1II1I1I
 if 79 - 79: OOooOOo / I11i1ii1
 if 77 - 77: I1ii11iIi11i
 if 46 - 46: iiiiiiii1
 if 72 - 72: O0OOOoOoo0 * Ii1IIIi1
 if 67 - 67: ooOoO0O00
 if 5 - 5: IIiIiII11i . ii
 if 57 - 57: oOo0O0Ooo
 if 35 - 35: ii - iiiiiiii1 / oO0o
 if 50 - 50: OOooOOo
 if 33 - 33: ooOOOoO
 if 98 - 98: OOooOOo % IIiIiII11i
 if 95 - 95: iI11I1II1I1I - iiiiiiii1 - Ii1IIIi1 + iiiiiiii1 % Ii1I . oOo0O0Ooo
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Oo0 = 'http://onlinemovies.tube/?s=' + ( oOOoooO ) . replace ( ' ' , '+' )
 i1ii11 = O0Oo0 . lower ( )
 oO0OOoo0OO = OoOooO ( i1ii11 )
 i1IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iIIii , I1i1i1iii , IiiIIi1 in i1IIIII11I1IiI :
  if 'movies' in IiiIIi1 :
   Iiiiii111i1ii ( IiiIIi1 + '-' + I1i1i1iii , oOooO0 , 90044 , iIIii )
 for oOooO0 in next :
  i111i ( oOooO0 )
  if 28 - 28: I11i
def OO0O00oOo ( ) :
 Iiiiii111i1ii ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 oO0OOoo0OO = OoOooO ( 'http://www.join4films.com/' )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , oOooO0 , 80006 , III1iII1I1ii + 'Desi.png' )
def IIiI1Ii1IIiI11i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oO0OOoo0OO )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( I1i1i1iii , url , 80007 , iIIii )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def Ii11I1iIiiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  O00Oo0 ( url )
def O0o0OO00 ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Oo0 = 'http://www.join4films.com/?s=' + ( oOOoooO ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1ii11 = O0Oo0 . lower ( )
 IIiI1Ii1IIiI11i1 ( i1ii11 )
 if 14 - 14: Ii1I + Ii
 if 83 - 83: Ii1I / Ii + IIiIiII11i . O0OOOoOoo0 * Ii1IIIi1 + I1111IIi
 if 42 - 42: ooOoO0O00 % IIiIiII11i . I11i1ii1
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
def OoOoO0oOOooo ( ) :
 iiOOooooO0Oo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 if 99 - 99: iI11I1II1I1I
def IIiiiiIi1I ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Oo0 = 'http://imoviemax.se/?s=' + ( oOOoooO ) . replace ( ' ' , '+' )
 i1ii11 = O0Oo0 . lower ( )
 ooo0O0o0OoOO ( i1ii11 )
def iIi11i ( url ) :
 o0o00o0Oo = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , OOOOOo in i1IIIII11I1IiI :
  if I1i1i1iii in o0o00o0Oo :
   pass
  else :
   iiOOooooO0Oo ( I1i1i1iii + ' - ' + OOOOOo + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
   o0o00o0Oo . append ( I1i1i1iii )
   if 77 - 77: IIiIiII11i
def IiiII1iIii111iII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , iI1iI1IiIIiI in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii + ' - Views:' + iI1iI1IiIIiI , url , 10075 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
  if 87 - 87: OOooOOo % iI11I1II1I1I
  if 72 - 72: Ii1IIIi1 . Ii1IIIi1 - Ii1I
def ooo0O0o0OoOO ( url ) :
 III1II1i = [ ]
 oO0OOoo0OO = OoOooO ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0OOoo0OO )
 for next in next :
  iiOOooooO0Oo ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , I1i1i1iii , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 10075 , iIIii , iIIii , '' )
  III1II1i . append ( I1i1i1iii )
  if 3 - 3: O0OOOoOoo0
def I1iIIIiI ( img , name , url ) :
 img = img
 name = name
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oO0OOoo0OO )
 for OoiI1I1 , url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  I1III1i1I = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + I1III1i1I
  OOOOO0 = ( OoiI1I1 ) . replace ( 'play-' , 'Server ' )
  OOiIiIIi1 ( OOOOO0 , I1III1i1I , 10076 , img , img , '' )
  if 79 - 79: IIiIiII11i - I11i1ii1 . ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * oOo0O0Ooo
def Ii1Ii1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oO0OOoo0OO )
 for OoO in i1IIIII11I1IiI :
  if '=m' in OoO :
   oOO0oo ( OoO )
  elif 'php' in OoO :
   Ii1Ii1I ( url )
  else :
   oO0OOoo0OO = OoOooO ( OoO )
   i1IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( oO0OOoo0OO )
   for II1i111 in i1IIIII11I1IiI :
    oOO0oo ( OoO )
    if 71 - 71: ooOoO0O00 - ooOOOoO * iiiiiiii1 + o000O0o - oO0o % Ii1I
    if 63 - 63: iI11I1II1I1I + Ii1IIIi1 . oO0o / oOo0O0Ooo
    if 84 - 84: ooOoO0O00
def IiIIiii1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 ooooo0Oo0 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo00 , o0I1IIIi11ii11 in ooooo0Oo0 :
  print 'there ><><><><><><><><><><><><'
  oOo00 = oOo00
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( o0I1IIIi11ii11 ) )
  for I1i1i1iii , O0o0oo0oOO0oO in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + oOo00 + '[/COLOR] - ' + I1i1i1iii + ' - [COLOR' + II + ']' + O0o0oo0oOO0oO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
 I1IIIiI1I1ii1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo00 , iIiIII1iI1111 in I1IIIiI1I1ii1 :
  print 'there ><><><><><><><><><><><><'
  oOo00 = oOo00
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iIiIII1iI1111 ) )
  for I1i1i1iii , O0o0oo0oOO0oO in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + oOo00 + '[/COLOR] - ' + I1i1i1iii + ' - [COLOR' + II + ']' + O0o0oo0oOO0oO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
   if 37 - 37: Ii % o000O0o * Ii1IIIi1 * Ii1IIIi1 * ii1ii11IIIiiI
   if 24 - 24: I11i1ii1 / O0OOOoOoo0 + I1111IIi . I1111IIi
   if 39 - 39: I11i1ii1 + o0o00Oo0O / ooOoO0O00 % I1111IIi / o000O0o * I1111IIi
def iIi1Ii1i1iI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I1IIIiI1I1ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
  I1i1i1iii = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for I1i1i1iii in I1i1i1iii :
   I1i1i1iii = ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  I111iIi1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for I111iIi1 in I111iIi1 :
   I111iIi1 = 'http:' + I111iIi1
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , '' , '' )
  if 77 - 77: I1111IIi . iiiiiiii1 % OOooOOo
  if 42 - 42: I1111IIi % O0OOOoOoo0 % I11i % o000O0o + ooOOOoO % OOooOOo
  if 3 - 3: o000O0o
  if 64 - 64: oO0o . oOo0O0Ooo - ii . I11i1ii1 - O0OOOoOoo0
def ii1II ( url ) :
 if 77 - 77: ii1ii11IIIiiI % OOooOOo / IIiIiII11i % O0OOOoOoo0 % ii % oO0o
 I1i11II11i1iI = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO , iIIii , I1i1i1iii , iI1 in i1IIIII11I1IiI :
  I1i1i1iii = ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = OoOooO ( OoO )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for oo0OoOOO0o0 , o0O0Oo00 in i1I :
   I1I1i1i = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( o0O0Oo00 ) )
   for oo00O00oO000o in I1I1i1i :
    if I1i1i1iii in I1i11II11i1iI :
     pass
    else :
     OOiIiIIi1 ( I1i1i1iii , oo0OoOOO0o0 , 8043 , iIIii , iIIii , oo00O00oO000o )
     I1I11i ( 'movies' , 'INFO' )
     I1i11II11i1iI . append ( I1i1i1iii )
     if 87 - 87: OOooOOo / I1111IIi . I11i1ii1 - Ii1IIIi1 / oO0o
     if 41 - 41: IIiIiII11i
def II1Iiii11111 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIIiIi )
 for url , IiI111ii1ii , oo00O00oO000o , o0ooooO0o0O , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 10065 , IiI111ii1ii , o0ooooO0o0O , oo00O00oO000o )
 I1I11i ( 'movies' , 'INFO' )
 if 26 - 26: o0o00Oo0O
def i111I1iiIiII ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Oo0 = 'https://www.youtube.com/results?search_query=' + ( oOOoooO ) . replace ( ' ' , '+' )
 i1ii11 = O0Oo0 . lower ( )
 oO0OOoo0OO = OoOooO ( i1ii11 )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in next :
  oOooO0 = 'https://www.youtube.com' + oOooO0
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , oOooO0 , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for iIIii , oOooO0 , I1i1i1iii , OoO00ooO , o0O0Oo00 in i1IIIII11I1IiI :
  OOOO . append ( I1i1i1iii )
  I1I11i ( 'tvshows' , 'INFO' )
  I111iIi1 = 'http:' + ( iIIii ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I111iIi1
  oOooO0 = 'http://www.youtube.com' + oOooO0
  OOiIiIIi1 ( '[COLORred]' + OoO00ooO + '[/COLOR]' + '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , I111iIi1 , o0O0Oo00 )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for iIIii , oOooO0 , I1i1i1iii , OoO00ooO in i1IIIII11I1IiI :
   print 'im doing it'
   I1I11i ( 'tvshows' , 'INFO' )
   I111iIi1 = 'http:' + ( iIIii ) . replace ( 'https:' , '' )
   oOooO0 = 'http://www.youtube.com' + oOooO0
   if '&' in oOooO0 :
    print ' i got here'
    oO0OOoo0OO = OoOooO ( oOooO0 )
    I1IIIiI1I1ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
     I1i1i1iii = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for I1i1i1iii in I1i1i1iii :
      I1i1i1iii = ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oOooO0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for oOooO0 in oOooO0 :
      oOooO0 = 'https://www.youtube.com/w' + oOooO0
     I111iIi1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for I111iIi1 in I111iIi1 :
      I111iIi1 = 'http:' + I111iIi1
     OOiIiIIi1 ( '[COLORred]' + OoO00ooO + '[/COLOR]' + '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , O0o0Oo , '' )
   elif I1i1i1iii in OOOO :
    pass
   elif 'user' in oOooO0 or 'elete' in I1i1i1iii :
    pass
   elif 'hannel' in oOooO0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oOooO0
    oO0OOoo0OO = OoOooO ( oOooO0 )
    iiO0o0O0oo0o = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for iIIii , oOooO0 , I1i1i1iii in iiO0o0O0oo0o :
     if 'outube' in oOooO0 or 'list' in oOooO0 :
      pass
     elif 'atch' in oOooO0 :
      oOooO0 = ( oOooO0 ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + OoO00ooO + '[/COLOR]' + '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iIIii , 'http:' + iIIii , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + OoO00ooO + '[/COLOR]' + '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , I111iIi1 , '' )
    if 100 - 100: I1111IIi . ii1ii11IIIiiI - iI11I1II1I1I . Ii / IIiIiII11i
def o0oO0OO00oo0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for iIIii , url , I1i1i1iii , OoO00ooO , o0O0Oo00 in i1IIIII11I1IiI :
  OOOO . append ( I1i1i1iii )
  I1I11i ( 'tvshows' , 'INFO' )
  I111iIi1 = 'http:' + ( iIIii ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I111iIi1
  url = 'http://www.youtube.com' + url
  OOiIiIIi1 ( '[COLORred]' + OoO00ooO + '[/COLOR]' + '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , I111iIi1 , o0O0Oo00 )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for iIIii , url , I1i1i1iii , OoO00ooO in i1IIIII11I1IiI :
   I1I11i ( 'tvshows' , 'INFO' )
   I111iIi1 = 'http:' + ( iIIii ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oO0OOoo0OO = OoOooO ( url )
    I1IIIiI1I1ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
     I1i1i1iii = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for I1i1i1iii in I1i1i1iii :
      I1i1i1iii = ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     I111iIi1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for I111iIi1 in I111iIi1 :
      I111iIi1 = 'http:' + I111iIi1
     OOiIiIIi1 ( '[COLORred]' + OoO00ooO + '[/COLOR]' + '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , O0o0Oo , '' )
   elif I1i1i1iii in OOOO :
    pass
   elif 'user' in url or 'elete' in I1i1i1iii :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0OOoo0OO = OoOooO ( url )
    iiO0o0O0oo0o = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for iIIii , url , I1i1i1iii in iiO0o0O0oo0o :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + OoO00ooO + '[/COLOR]' + '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + iIIii , 'http:' + iIIii , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + OoO00ooO + '[/COLOR]' + '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , I111iIi1 , '' )
    if 17 - 17: I1111IIi / Ii1I - I11i * Ii1I
def i11i11II11i ( ) :
 Oo0oO ( )
 II1Ii1I1i ( )
 if 74 - 74: Ii1I * Ii / oOo0O0Ooo - o0o00Oo0O . I11i1ii1
 if 39 - 39: I11i1ii1 / o0o00Oo0O * I1111IIi
 iiOOooooO0Oo ( '[COLOR' + II + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o , 60004 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 I1IiI ( '[COLORsteelblue]VOD Lists[/COLOR]' , '' , 40000 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
 if 44 - 44: Ii1IIIi1 / Ii1IIIi1 . I11i % I1111IIi + OOooOOo
 if 57 - 57: O0OOOoOoo0 % oO0o - oO0o
 if 5 - 5: ooOoO0O00 + ii % OOooOOo
def OO0Oo ( ) :
 I1IiI ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIiiiiiIiIIi + '&action=get_vod_streams' , 40001 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( iiIiiIi1 )
 i1IIIII11I1IiI = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLORsteelblue]' + I1i1i1iii + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOooO0 , 40001 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
def I1Ii11i ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( I1iIiiiI1 + url )
 i1IIIII11I1IiI = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg .+?,"container_extension":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , type , OoO , iII1iIi11i , OOO0O00Oo in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1i1i1iii , ii1oOOO0ooOO + OoO + '.' + OOO0O00Oo , 222 , ( iII1iIi11i ) . replace ( '\/' , '/' ) + 'jpg' , O0o0Oo , 'Type: ' + type )
  if 3 - 3: ii
def II1Ii1I1i ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  O0OoO0o ( )
  if 1 - 1: I11i1ii1 % ooOOOoO * Ii1I - IIiIiII11i
  if 49 - 49: o000O0o - O0OOOoOoo0 % OOooOOo
  if 72 - 72: oOo0O0Ooo + I1111IIi . OOooOOo + OOooOOo
  if 94 - 94: Ii % ii / oOo0O0Ooo
  if 24 - 24: oOo0O0Ooo * o000O0o
  if 85 - 85: IIiIiII11i . I11i1ii1 % Ii1IIIi1 % ooOOOoO
  if 80 - 80: o000O0o * ooOOOoO / iI11I1II1I1I % o000O0o / iI11I1II1I1I
  if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * O0OOOoOoo0 . Ii * o0o00Oo0O
def O0OoO0o ( ) :
 i1i = OoOooO ( 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 for oOooO0 in i1IIIII11I1IiI :
  Iiii1 = datetime . fromtimestamp ( float ( i1IIIII11I1IiI [ 0 ] ) )
  Iiii1 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= Iiii1 <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   OOooO0OOoo . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + II + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + II + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + II + '] To Purchase A licence[/COLOR]' )
def iI111II1ii ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"username":"(.+?)"' ) . findall ( i1i )
 O0ooO00ooOO0o = re . compile ( '"password":"(.+?)"' ) . findall ( i1i )
 o0OO0O0Oo = re . compile ( '"status":"(.+?)"' ) . findall ( i1i )
 i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 Iii1I1111ii = re . compile ( '"active_cons":"(.+?)"' ) . findall ( i1i )
 ii1iii1i = re . compile ( '"created_at":"(.+?)"' ) . findall ( i1i )
 OOOOO = re . compile ( '"max_connections":"(.+?)"' ) . findall ( i1i )
 oOoO0o = re . compile ( '"is_trial":"1"' ) . findall ( i1i )
 Ii1IiIiIi1IiI = re . compile ( '"is_trial":"0"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']My GTV Account Information[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  i1i1iII1 ( '[COLOR' + II + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in O0ooO00ooOO0o :
  i1i1iII1 ( '[COLOR' + II + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in o0OO0O0Oo :
  i1i1iII1 ( '[COLOR' + II + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in ii1iii1i :
  Iiii1 = datetime . fromtimestamp ( float ( ii1iii1i [ 0 ] ) )
  Iiii1 . strftime ( '%Y-%m-%d %H:%M:%S' )
  i1i1iII1 ( '[COLOR' + II + ']Created:[/COLOR]  %s' % ( Iiii1 ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in i1I :
  Iiii1 = datetime . fromtimestamp ( float ( i1I [ 0 ] ) )
  Iiii1 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= Iiii1 <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   i1i1iII1 ( '[COLORred]Expires Today[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  i1i1iII1 ( '[COLOR' + II + ']Expires:[/COLOR]  %s' % ( Iiii1 ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in Iii1I1111ii :
  i1i1iII1 ( '[COLOR' + II + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in OOOOO :
  i1i1iII1 ( '[COLOR' + II + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in oOoO0o :
  i1i1iII1 ( '[COLOR' + II + ']Trial:[/COLOR] Yes' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in Ii1IiIiIi1IiI :
  i1i1iII1 ( '[COLOR' + II + ']Trial:[/COLOR] No' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 i1i1iII1 ( '' , '' , '' , '' )
 i1i1iII1 ( '' , '' , '' , '' )
 i1i1iII1 ( '[COLOR' + II + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 65 - 65: O0OOOoOoo0 . oO0o + ii1ii11IIIiiI
def IIiI1I ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
 oOo0OOO00Oo ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 15 - 15: O0OOOoOoo0
IIiiiiiIiIIi = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( II11iiii1Ii , OO0o )
ii1oOOO0ooOO = 'http://piesustv.net:8000/movie/%s/%s/' % ( II11iiii1Ii , OO0o )
o0oo0 = 'http://piesustv.net:8000/live/%s/%s/' % ( II11iiii1Ii , OO0o )
OoO0OOoO0Oo0 = '&action=get_live_categories'
oO00O = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( II11iiii1Ii , OO0o )
iiIiiIi1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( II11iiii1Ii , OO0o )
I1iIiiiI1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_streams&category_id=' % ( II11iiii1Ii , OO0o )
II111IiiiI1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( II11iiii1Ii , OO0o )
if 75 - 75: I11i1ii1
def iI1ii1Ii ( ) :
 if 78 - 78: iI11I1II1I1I * I1ii11iIi11i . I1ii11iIi11i - Ii1IIIi1 . iI11I1II1I1I
 iiOOooooO0Oo ( ( '[COLORsteelblue]Full List[/COLOR]' ) . replace ( '\/' , ' - ' ) , IIiiiiiIiIIi + '&action=get_live_streams' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( IIiiiiiIiIIi + OoO0OOoO0Oo0 )
 i1IIIII11I1IiI = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLORsteelblue]' + I1i1i1iii + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOooO0 , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
def I111I1I ( ) :
 Oo0000 = 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o
 oO0OoOo = urllib2 . Request ( Oo0000 , headers = { "Accept" : "application/xml" } )
 i1Oo00 = urllib2 . urlopen ( oO0OoOo )
 if i1Oo00 and i1Oo00 . getcode ( ) == 200 :
  oOOOOOo = [ ]
  i1I11ii = ElementTree . parse ( i1Oo00 )
  o0ooO00O0O = i1I11ii . getroot ( )
  for iiO0o0O0oo0o in i1I11ii . findall ( "channel" ) :
   iiiI1iI1 = iiO0o0O0oo0o . find ( 'title' ) . text
   iiiI1iI1 = base64 . b64decode ( iiiI1iI1 )
   iiiI1iI1 = iiiI1iI1 . partition ( "[" )
   I1oOoO0OOO00O = iiiI1iI1 [ 1 ] + iiiI1iI1 [ 2 ]
   I1oOoO0OOO00O = I1oOoO0OOO00O . partition ( "]" )
   I1oOoO0OOO00O = I1oOoO0OOO00O [ 2 ]
   I1oOoO0OOO00O = I1oOoO0OOO00O . partition ( "   " )
   I1oOoO0OOO00O = I1oOoO0OOO00O [ 2 ]
   if 73 - 73: I11i % oO0o + I1111IIi + oOo0O0Ooo
   OoOO00 = iiO0o0O0oo0o . find ( "description" ) . text
   if OoOO00 :
    OoOO00 = base64 . b64decode ( OoOO00 )
    O0O00OoOoOOo = OoOO00 . partition ( "(" )
    O0O00OoOoOOo = "NOW:  " + O0O00OoOoOOo [ 0 ]
    o0o0oo0 = OoOO00 . partition ( ")\n" )
    o0o0oo0 = o0o0oo0 [ 2 ] . partition ( "(" )
    o0o0oo0 = "NEXT:  " + o0o0oo0 [ 0 ]
    II1IIi1iII1i = O0O00OoOoOOo + o0o0oo0
   else :
    II1IIi1iII1i = ""
   oOOOOOo . append ( { 'title' : iiiI1iI1 [ 0 ] , 'cs' : I1oOoO0OOO00O , 'schedule' : II1IIi1iII1i } )
 return oOOOOOo
def iii ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( oO00O + url )
 i1IIIII11I1IiI = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , type , OoO , iII1iIi11i in i1IIIII11I1IiI :
  II1i111 = ( o0oo0 + OoO + '.m3u8' ) . strip ( )
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , II1i111 , 222 , ( iII1iIi11i ) . replace ( '\/' , '/' ) + 'jpg' , O0o0Oo , type )
  if 26 - 26: oOo0O0Ooo
def iiiiIiIiI ( url , name , img ) :
 img = img
 name = name
 url = url
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiiI1i11Ii , o0OO in i1IIIII11I1IiI :
  if name == iiiI1i11Ii :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) + o0OO , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def ooO ( name ) :
 ii1i11 = name
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , iIIii , oOooO0 in i1IIIII11I1IiI :
  oOooO0 = ( oOooO0 ) . replace ( '.ts' , '.m3u8' )
  OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oOooO0 ) . strip ( ) , 222 , iIIii , iIIii , '' )
 else :
  OOiIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - I11i1ii1
  if 38 - 38: I11i % iiiiiiii1 + Ii + O0OOOoOoo0 + I11i1ii1 / Ii
  if 94 - 94: O0OOOoOoo0 - I1ii11iIi11i + o000O0o
  if 59 - 59: ooOOOoO . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
  if 56 - 56: o000O0o + I11i1ii1
  if 32 - 32: IIiIiII11i + OOooOOo % I11i1ii1 / OOooOOo + Ii1I
  if 2 - 2: Ii - iiiiiiii1 + oO0o % ooOOOoO * ii1ii11IIIiiI
  if 54 - 54: o0o00Oo0O - O0OOOoOoo0 . Ii1IIIi1 % O0OOOoOoo0 + O0OOOoOoo0
  if 36 - 36: Ii1IIIi1 % Ii
  if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * o000O0o . ooOOOoO / ooOoO0O00
  if 50 - 50: iiiiiiii1 / ooOoO0O00 % ii
  if 83 - 83: Ii1I * Ii1I + Ii1IIIi1
def oo000o0000oO ( ) :
 iiOOooooO0Oo ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( ooOooo000oOO ) :
  iiOOooooO0Oo ( 'Backup Genie Favourites' , oOooO0 , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( oO0 ) :
  iiOOooooO0Oo ( 'Backup Ivue Config' , oO0 , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  iiOOooooO0Oo ( 'Backup Kodi Favourites' , Ii1iIiII1ii1 , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 57 - 57: o0o00Oo0O - o0o00Oo0O . Ii1I / I11i / ii1ii11IIIiiI
  if 20 - 20: Ii1IIIi1 * IIiIiII11i - OOooOOo - o000O0o * iiiiiiii1
  if 6 - 6: I11i1ii1 + Ii1IIIi1 / I1ii11iIi11i + I1111IIi % IIiIiII11i / oO0o
zip = oo00 . getSetting ( 'zip' )
iiIi = xbmc . translatePath ( os . path . join ( zip ) )
def OooooOo ( ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 48 - 48: o000O0o - IIiIiII11i + ooOoO0O00 . o0o00Oo0O + oOo0O0Ooo
  if 80 - 80: o000O0o % o000O0o % o0o00Oo0O - Ii . O0OOOoOoo0 / o0o00Oo0O
  if 13 - 13: oOo0O0Ooo + o0o00Oo0O - Ii1I % I1ii11iIi11i / ii1ii11IIIiiI . ooOoO0O00
def OOOO00OoooO ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = ooOooo000oOO
  elif 'Ivue' in name :
   url = oO0
  elif 'Kodi' in name :
   url = Ii1iIiII1ii1
  OooooOo ( )
  IIIi = open ( url ) . read ( )
  Ii1iiI1 = os . path . join ( iiIi , description . split ( 'Your ' ) [ 1 ] )
  iiiiI = open ( Ii1iiI1 , mode = 'w' )
  iiiiI . write ( IIIi )
  iiiiI . close ( )
 else :
  if 'guisettings.xml' in description :
   o0ooOOoO0oO0 = open ( os . path . join ( iiIi , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oo00I1IiI1IIiI = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   i1IIIII11I1IiI = re . compile ( oo00I1IiI1IIiI ) . findall ( o0ooOOoO0oO0 )
   for type , oooo , o0o0oo0Ooo in i1IIIII11I1IiI :
    o0o0oo0Ooo = o0o0oo0Ooo . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , oooo , o0o0oo0Ooo ) )
  else :
   Ii1iiI1 = os . path . join ( url )
   IIIi = open ( os . path . join ( iiIi , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   iiiiI = open ( Ii1iiI1 , mode = 'w' )
   iiiiI . write ( IIIi )
   iiiiI . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 12 - 12: Ii1I / ii1ii11IIIiiI
 if 5 - 5: ii
 if 18 - 18: oOo0O0Ooo % ii - O0OOOoOoo0 . Ii * I1ii11iIi11i % ii1ii11IIIiiI
 if 12 - 12: ooOoO0O00 / Ii1IIIi1 % I11i1ii1 * I1111IIi * o0o00Oo0O * iI11I1II1I1I
def OOOOoO ( ) :
 Iii11111iiI = 1
 OooooOo ( )
 o0OOOOoO = xbmc . translatePath ( os . path . join ( iiIi , 'Build Backup' , 'Full Backup' , '' ) )
 OoO0Ooo = xbmc . translatePath ( os . path . join ( iiIi , 'Build Backup' , 'my_full_backup.zip' ) )
 Ii1I1I = xbmc . translatePath ( os . path . join ( iiIi , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( o0OOOOoO ) :
  os . makedirs ( o0OOOOoO )
 oOOoOOO0oOoo = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not oOOoOOO0oOoo ) : return False , 0
 iiiI1iI1 = oOOoOOO0oOoo
 o0O0ooooooo00 = xbmc . translatePath ( os . path . join ( o0OOOOoO , iiiI1iI1 + '.zip' ) )
 I1111ii11IIII = [ 'plugin.video.GenieTv' ]
 IiIi1II111I = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 o00o = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 IIi1i1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 o0O0Ooo = "Creating full backup of existing build"
 O0oO00oOOooO = "Creating Community Build"
 IiI = "Archiving..."
 Iii1iiI = ""
 ii1IiiII = "Please Wait"
 IiiI1II1II1i ( Oo0o0000o0o0 , o0O0ooooooo00 , O0oO00oOOooO , IiI , Iii1iiI , ii1IiiII , o00o , IIi1i1 )
 time . sleep ( 1 )
 iI = xbmc . translatePath ( os . path . join ( o0OOOOoO , iiiI1iI1 + '_guisettings.zip' ) )
 O0OO0o0O00oO = zipfile . ZipFile ( iI , mode = 'w' )
 try :
  O0OO0o0O00oO . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 O0OO0o0O00oO . close ( )
 if Iii11111iiI == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + OoO0Ooo , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + o0O0ooooooo00 + '[/COLOR]' )
  if 81 - 81: I1111IIi / ooOOOoO
def IiiI1II1II1i ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 III1 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 IIi11 = len ( sourcefile )
 o0O0oo0 = [ ]
 iIIi1 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for o0Ooo0o0Oo , oo00ooooOOo00 , ii1iOO00Oooo000 in os . walk ( sourcefile ) :
  for file in ii1iOO00Oooo000 :
   iIIi1 . append ( file )
 iI1ii111iiIii = len ( iIIi1 )
 for o0Ooo0o0Oo , oo00ooooOOo00 , ii1iOO00Oooo000 in os . walk ( sourcefile ) :
  oo00ooooOOo00 [ : ] = [ oO0oiIiI for oO0oiIiI in oo00ooooOOo00 if oO0oiIiI not in exclude_dirs ]
  ii1iOO00Oooo000 [ : ] = [ iiiiI for iiiiI in ii1iOO00Oooo000 if iiiiI not in exclude_files ]
  for file in ii1iOO00Oooo000 :
   o0O0oo0 . append ( file )
   iIIiiiI1iI1 = len ( o0O0oo0 ) / float ( iI1ii111iiIii ) * 100
   o0oOoO00o . update ( int ( iIIiiiI1iI1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   oO00000oO0o0O = os . path . join ( o0Ooo0o0Oo , file )
   if not 'temp' in oo00ooooOOo00 :
    if not 'plugin.program.originwizard' in oo00ooooOOo00 :
     import time
     IIIiI1iI1 = '01/01/1980'
     IIiIiiii1I1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( oO00000oO0o0O ) ) )
     if IIiIiiii1I1 > IIIiI1iI1 :
      III1 . write ( oO00000oO0o0O , oO00000oO0o0O [ IIi11 : ] )
 III1 . close ( )
 o0oOoO00o . close ( )
 if 74 - 74: o000O0o / ii1ii11IIIiiI
 if 53 - 53: IIiIiII11i - O0OOOoOoo0 . ooOoO0O00 / iiiiiiii1 - ooOoO0O00 - Ii1IIIi1
def OoOo0o ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 if 20 - 20: ooOoO0O00 . Ii1I . iiiiiiii1 % ooOoO0O00
 if 8 - 8: ooOOOoO / ii / IIiIiII11i / o000O0o + IIiIiII11i
def oOoOO0000oO00 ( ) :
 Oo0oO ( )
 O0oO0 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  Oo0oooO0oO ( )
 if oO0O0OO0O == 1 :
  I1ii1 ( )
 if oO0O0OO0O == 2 :
  IiI1I11iIii ( )
 if oO0O0OO0O == 3 :
  i111I1iiIiII ( )
  if 93 - 93: ooOOOoO . OOooOOo / I1ii11iIi11i + o000O0o
  if 8 - 8: OOooOOo
  if 16 - 16: I11i . ooOOOoO
  if 50 - 50: I11i1ii1 * OOooOOo + Ii1I - Ii + I1ii11iIi11i * Ii1I
  if 20 - 20: iiiiiiii1 / I11i % OOooOOo
  if 69 - 69: iiiiiiii1 - ooOoO0O00 % O0OOOoOoo0 . Ii1IIIi1 - Ii1IIIi1
  if 65 - 65: Ii1IIIi1 + IIiIiII11i
  if 61 - 61: Ii * o000O0o % I1ii11iIi11i * iiiiiiii1 - ii - oO0o
  if 83 - 83: I11i1ii1 / Ii1IIIi1
def i11iI1 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   oo0 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , IiI111ii1ii , I1i1i1iii )
  if oO0O0OO0O == 1 :
   I11iIiI1 ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if oO0O0OO0O == 2 :
   i1Ii11ii1I ( )
  if oO0O0OO0O == 3 :
   OO0oI1iii1i ( )
  if oO0O0OO0O == 4 :
   oO0ooOoOO ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if oO0O0OO0O == 5 :
   Ii1 ( )
  if oO0O0OO0O == 6 :
   IiIiI111IIII1 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if oO0O0OO0O == 7 :
   OOOoOooO000oO ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if oO0O0OO0O == 8 :
   o0OOOOOo00 ( str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if oO0O0OO0O == 9 :
   oo0oOO ( )
  if oO0O0OO0O == 10 :
   IIO000oooOO0Oo0 ( )
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
  if 31 - 31: I1111IIi - oO0o / Ii1IIIi1 . ooOoO0O00 / ii1ii11IIIiiI
 I1I11i ( 'movies' , 'MAIN' )
 if 66 - 66: oO0o
def o00ooO0ooO0o0 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  O0oO0 = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   OOOO00OOO00 ( )
  if oO0O0OO0O == 1 :
   iiI1IIIi ( )
  if oO0O0OO0O == 2 :
   O0O0ooOOO ( )
  if oO0O0OO0O == 3 :
   ii1OO0 ( oOooO0 )
  if oO0O0OO0O == 4 :
   OoOoO00OOoOOOo0 ( oOooO0 )
  if oO0O0OO0O == 5 :
   I1iIIiiIIi1i ( )
  if oO0O0OO0O == 6 :
   oOoO00O ( url = 'http://www.iplocation.net/' , inc = 1 )
  if oO0O0OO0O == 7 :
   I11I1I1i1i ( )
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
  if 74 - 74: o0o00Oo0O % ii * I1ii11iIi11i + Ii1IIIi1 * O0OOOoOoo0
  if 100 - 100: Ii1IIIi1 + ii1ii11IIIiiI * I11i + IIiIiII11i
 I1I11i ( 'movies' , 'MAIN' )
 if 70 - 70: I1ii11iIi11i * iI11I1II1I1I
 if 76 - 76: O0OOOoOoo0 % OOooOOo % iI11I1II1I1I . Ii1IIIi1
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
 if 30 - 30: ooOoO0O00
 if 75 - 75: ooOOOoO . Ii1IIIi1 - iI11I1II1I1I * oO0o * O0OOOoOoo0
def ooo0OO0OOooO0 ( ) :
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
 if 96 - 96: Ii1IIIi1 + Ii1IIIi1 % I1111IIi % Ii1IIIi1
def iI1i111I1Ii ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , III1iII1I1ii + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 28 - 28: iI11I1II1I1I + OOooOOo . I11i % Ii
def O00oOooo00o0o ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , O0o0Oo , '' )
 if 56 - 56: OOooOOo % Ii1I - ii1ii11IIIiiI % iI11I1II1I1I
 if 76 - 76: ii * ii - O0OOOoOoo0 - iI11I1II1I1I . ii / Ii1I
 if 86 - 86: I11i1ii1
def OOI1iI1ii1II ( ) :
 Oo0oO ( )
 O0oO0 = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  oO0oo0O0 ( )
 if oO0O0OO0O == 0 :
  o0O0OOoo ( oOooO0 )
 if oO0O0OO0O == 0 :
  oo00ooOooO ( oOooO0 )
  if 91 - 91: IIiIiII11i . Ii1IIIi1 + I11i
  if 8 - 8: Ii1IIIi1 * I1ii11iIi11i / O0OOOoOoo0 - oO0o - ii
  if 100 - 100: o000O0o . iI11I1II1I1I . iI11I1II1I1I
 I1I11i ( 'movies' , 'MAIN' )
 if 55 - 55: o000O0o
def i1iiI ( ) :
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 i1IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1i )
 for iIIii , I1i1i1iii in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , iIIii , iIIii , '' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 97 - 97: iiiiiiii1 . ooOOOoO / oOo0O0Ooo
def o00OO0o0 ( url ) :
 i1i = OoOooO ( i1II1IiiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 5 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 13 - 13: o0o00Oo0O % I11i1ii1 % ooOOOoO
def oO0oo0O0 ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 25 - 25: ii % ii1ii11IIIiiI * IIiIiII11i - oO0o
def Oo00Oooo00o ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + II11II1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 52 - 52: Ii1IIIi1 * o000O0o + ooOOOoO * ooOOOoO % ooOoO0O00 % ooOOOoO
def OOOO000Ooo0O ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + oOo0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 77 - 77: IIiIiII11i
def iIii1I1iII ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iiIi1iIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 9 - 9: iI11I1II1I1I . ii + ooOoO0O00 - I1ii11iIi11i
def i1iI ( url ) :
 i1i = OoOooO ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 84 - 84: I1ii11iIi11i
def o0O0OOoo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iiiiI11iiIIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 40 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 43 - 43: ooOOOoO % ii1ii11IIIiiI / I11i * iiiiiiii1
def oooIi1I11IiI1i ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + I111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 5 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 25 - 25: ooOOOoO / ooOOOoO % ii - Ii1I * o000O0o
def OOOoOoO ( ) :
 O0oO0 = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  i1oooOoOoOO ( )
 if oO0O0OO0O == 1 :
  OooOO ( )
 if oO0O0OO0O == 2 :
  iio0oo0Oo ( )
  if 10 - 10: Ii1I
  if 87 - 87: I1ii11iIi11i % ii1ii11IIIiiI
  if 53 - 53: ooOoO0O00 - I1111IIi + iI11I1II1I1I
  if 75 - 75: Ii1I
def OooOO ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( iIIIiIi )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( iIIIiIi )
 for oOooO0 , O00o in i1IIIII11I1IiI :
  Iiiiii111i1ii ( 'Android Apps' + O00o , 'https://www.apkfiles.com' + oOooO0 , 30035 , III1iII1I1ii + 'apps.png' )
 for oOooO0 , O00o in i1I :
  Iiiiii111i1ii ( 'Android Games' + O00o , 'https://www.apkfiles.com' + oOooO0 , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I11i ( 'movies' , 'MAIN' )
def o0o0ooOo00 ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if '/cat' in url :
   Iiiiii111i1ii ( ( I1i1i1iii ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def OO00oO0OoO0o ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if '/app' in url :
   Iiiiii111i1ii ( ( I1i1i1iii ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def I11I111i1I1 ( url ) :
 iIIIiIi = OoOooO ( url )
 Oo0Oo0O = url
 if "page=" in str ( url ) :
  Oo0Oo0O = url . split ( '?' ) [ 0 ]
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( iIIIiIi )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  if 'apk' in url :
   OOiIiIIi1 ( ( I1i1i1iii ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + iIIii )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 OOiIiIIi1 ( 'Next Page' , Oo0Oo0O + str ( i1I ) , 30037 , III1iII1I1ii + 'Next.png' )
def iii1 ( name , url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 name = name
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  O0Ooo0O ( name , url , 'Brackets' )
def iio0oo0Oo ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Oo0 = 'https://www.apkfiles.com/search?q=' + ( oOOoooO ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1ii11 = O0Oo0 . lower ( )
 I11I111i1I1 ( i1ii11 )
 if 18 - 18: ooOoO0O00
def i1i1Ii1IiIII ( url ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( I1IIii11 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , I1i1i1iii + '.apk' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 22 - 22: I11i1ii1 / I11i1ii1 - ii1ii11IIIiiI % ooOOOoO . Ii1IIIi1 + I1111IIi
def OooO00oo0O0 ( url ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , I1i1i1iii + '.mp4' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 10 - 10: I1111IIi / ii
 if 50 - 50: Ii - ii . o000O0o + o0o00Oo0O . ooOoO0O00
def OO0 ( name , url , description ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , name )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 Oo00Oo = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print Oo00Oo
 print '======================================='
 extract . all ( o00O0 , Oo00Oo , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 25 - 25: iI11I1II1I1I
 if 63 - 63: I11i1ii1
 if 96 - 96: ooOOOoO
 if 34 - 34: OOooOOo / oO0o - oOo0O0Ooo . o0o00Oo0O . Ii1IIIi1
 if 63 - 63: O0OOOoOoo0
def i1oooOoOoOO ( ) :
 i1i = OoOooO ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1i )
 for I1i1i1iii , oOooO0 , iII1iIi11i , o0ooooO0o0O , i1i1iIiI in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1i1i1iii , oOooO0 , 80003 , iII1iIi11i , III1iII1I1ii + 'APKToolsB.png' , i1i1iIiI )
def I11iii ( apk , ret = None ) :
 if apk == "kodi" :
  IIi111 = "https://kodi.tv/download/"
  i1i = OoOooO ( IIi111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1i )
  if len ( i1IIIII11I1IiI ) == 1 :
   oO0o0o0O = i1IIIII11I1IiI [ 0 ] [ 0 ]
   iiiI1iI1 = i1IIIII11I1IiI [ 0 ] [ 1 ]
   I111ii1iI = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( oO0o0o0O , iiiI1iI1 )
  if ret == 'version' : return oO0o0o0O
  else : return I111ii1iI
 elif apk == "spmc" :
  i1IiI1ii1i = 'https://github.com/koying/SPMC/releases/latest/'
  i1i = OoOooO ( i1IiI1ii1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1i )
  oO0o0o0O = re . sub ( '<[^<]+?>' , '' , i1IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  I111ii1iI = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( oO0o0o0O , oO0o0o0O )
  if ret == 'version' : return oO0o0o0O
  else : return I111ii1iI
def O0Ooo0O ( name , url , Brackets ) :
 if I1IIII1i ( ) == 'android' :
  i1I1I1I = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not i1I1I1I : iII1III ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  O0oo0oO00o = name
  if i1I1I1I :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not IIIii11 ( url ) == True : iII1III ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % O0oo0oO00o , '' , 'Please Wait' )
   o00O0 = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( o00O0 )
   except : pass
   downloader . download ( url , o00O0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    O0OO0o0O00oO = zipfile . ZipFile ( o00O0 )
    for file in O0OO0o0O00oO . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as iiiiI :
       I1ii111i1ii1 = file . split ( '/' ) [ 1 ]
       iiiiI . write ( O0OO0o0O00oO . read ( file ) )
       xbmc . sleep ( 500 )
       iiiiI . close ( )
       try :
        os . remove ( o00O0 )
       except :
        pass
       o00O0 = os . path . join ( i1iiIII111ii , I1ii111i1ii1 )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + o00O0 + '")' )
  else : iII1III ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iII1III ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 71 - 71: I11i1ii1 . ooOOOoO + Ii1IIIi1
 if 8 - 8: Ii * o0o00Oo0O + Ii1I . iI11I1II1I1I % ooOOOoO / ooOOOoO
 if 70 - 70: oOo0O0Ooo + ii1ii11IIIiiI
 if 70 - 70: I1111IIi . Ii
def O0O00O0Oo0 ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1i )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  oOooO0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oOooO0 )
  OoOiI11IiI1i1 ( ( I1i1i1iii ) . replace ( '_' , ' ' ) , oOooO0 )
  if 65 - 65: o0o00Oo0O . o000O0o
def OoOiI11IiI1i1 ( name , url ) :
 if I1IIII1i ( ) == 'android' :
  i1I1I1I = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not i1I1I1I : iII1III ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  O0oo0oO00o = name
  if i1I1I1I :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not IIIii11 ( url ) == True : iII1III ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % O0oo0oO00o , '' , 'Please Wait' )
   o00O0 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( o00O0 )
   except : pass
   downloader . download ( url , o00O0 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + o00O0 + '")' )
  else : iII1III ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iII1III ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 85 - 85: IIiIiII11i
 if 55 - 55: Ii1I
def oOoo0OO0 ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 5 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'INFO' )
 if 5 - 5: Ii * I1ii11iIi11i
 if 29 - 29: ii1ii11IIIiiI / I11i1ii1 % ooOOOoO
def oOo0 ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 30015 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 10 - 10: iI11I1II1I1I % ii % Ii1I
def IiiI1i111I1i ( url , iconimage , fanart ) :
 i1i = OoOooO ( url )
 I1III1i1I = url
 iIIii = iconimage
 fanart = fanart
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for OoO , I1i1i1iii in i1IIIII11I1IiI :
  if '.mp4' in I1i1i1iii :
   OOiIiIIi1 ( 'Watch VIDEO' , url + '/' + OoO , 222 , iIIii , fanart , '' )
  if 'description' in I1i1i1iii :
   OOiIiIIi1 ( 'Read Description' , url + '/' + OoO , 30017 , iIIii , fanart , '' )
  if 'images' in I1i1i1iii :
   iiOOooooO0Oo ( 'View Images' , url + '/' + OoO , 30018 , iIIii , fanart , '' )
  if 'url' in I1i1i1iii :
   OOiIiIIi1 ( 'Install Build On Android' , url + '/' + OoO , 30016 , iIIii , fanart , '' )
  if 'url' in I1i1i1iii :
   OOiIiIIi1 ( 'Install Build On Pc' , url + '/' + OoO , 30019 , iIIii , fanart , '' )
 I1I11i ( 'movies' , 'INFO' )
 if 97 - 97: Ii1IIIi1 % oOo0O0Ooo * oOo0O0Ooo % I1ii11iIi11i
def o0OoOooOO0o0 ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  Oooo0ooOoo0 ( url )
  if 26 - 26: I1111IIi / iI11I1II1I1I - iI11I1II1I1I
def oO00oO00O0Oo ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  OO0o0o0oo ( url )
  if 40 - 40: I1ii11iIi11i
def iI1Ii11 ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1i )
 for Ooo0 in i1IIIII11I1IiI :
  OOoO ( 'Description:' , Ooo0 )
  if 49 - 49: IIiIiII11i + ii . o000O0o + Ii / o000O0o
def IIIi11 ( url ) :
 i1i = OoOooO ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for OoO , I1i1i1iii in i1IIIII11I1IiI :
  if 'png' in I1i1i1iii :
   OOiIiIIi1 ( 'image' , '' , '' , url + '/' + OoO , url + '/' + OoO , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 69 - 69: o0o00Oo0O - o0o00Oo0O
def i1I1i1i1I1 ( name , url , description ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , name + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 I1iIIiiIIi1i ( )
 if 17 - 17: OOooOOo + ii % Ii1IIIi1
 if 36 - 36: Ii + Ii1I % Ii1IIIi1 . oOo0O0Ooo - I11i1ii1
def OO0o0o0oo ( url ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 ( url )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOOO00OOO00 ( )
 if 94 - 94: oOo0O0Ooo % OOooOOo . I1111IIi . I11i1ii1 . oO0o
def Oooo0ooOoo0 ( url ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 ( url )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOOO00OOO00 ( )
 if 53 - 53: OOooOOo
def o0oo0OO ( name , url , description ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o00O0 = os . path . join ( oOOoO0 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 OOOO00OOO00 ( )
 if 17 - 17: I11i1ii1 + Ii1I * Ii
def I1IIII1i ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def oOOo0O00o ( log ) :
 xbmc . log ( "[%s]: %s" % ( oO , log ) )
 if not os . path . exists ( oO0o0o0ooO0oO ) : os . makedirs ( oO0o0o0ooO0oO )
 if not os . path . exists ( oo0o0O00 ) : iiiiI = open ( oo0o0O00 , 'w' ) ; iiiiI . close ( )
 with open ( oo0o0O00 , 'a' ) as iiiiI :
  oO00OOOOOO0o = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  iiiiI . write ( oO00OOOOOO0o . rstrip ( '\r\n' ) + '\n' )
def OOOO00OOO00 ( ) :
 oO0O0OO0O = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if oO0O0OO0O == 0 : return
 elif oO0O0OO0O == 1 : pass
 iIII = I1IIII1i ( )
 oOOo0O00o ( "Platform: " + str ( iIII ) )
 os . _exit ( 1 )
 oOOo0O00o ( "Force close failed!  Trying alternate methods." )
 if iIII == 'osx' :
  oOOo0O00o ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIII == 'linux' :
  oOOo0O00o ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif iIII == 'android' :
  oOOo0O00o ( "############ try android force close #################" )
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
 elif iIII == 'windows' :
  oOOo0O00o ( "############ try windows force close #################" )
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
  oOOo0O00o ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  oOOo0O00o ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 85 - 85: IIiIiII11i + iiiiiiii1 - I11i1ii1 * iI11I1II1I1I % o000O0o
  if 62 - 62: ii1ii11IIIiiI + o0o00Oo0O * oO0o
  if 59 - 59: IIiIiII11i
def oo00ooOooO ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iIiIi11I1iIii1i11 , oo00ooooOOo00 , ii1iOO00Oooo000 in os . walk ( url ) :
  for file in ii1iOO00Oooo000 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    o0ooOOoO0oO0 = open ( ( os . path . join ( iIiIi11I1iIii1i11 , file ) ) ) . read ( )
    iIiiI11II11i = o0ooOOoO0oO0 . replace ( Oo0o0000o0o0 , 'special://home/' )
    iiiiI = open ( ( os . path . join ( iIiIi11I1iIii1i11 , file ) ) , mode = 'w' )
    iiiiI . write ( str ( iIiiI11II11i ) )
    iiiiI . close ( )
 OOOO00OOO00 ( )
 if 98 - 98: O0OOOoOoo0 - O0OOOoOoo0
def i1Ii11ii1I ( ) :
 Iiiiii111i1ii ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 Iiiiii111i1ii ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 Iiiiii111i1ii ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 58 - 58: o000O0o
def oOOo0OO00OoO ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def oOOo0oO0oOOOo ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def oo000Oo0 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1I :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']Filter - ' + I1i1i1iii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']Stream - ' + I1i1i1iii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , iIIii )
def OoOOoo0o ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  O00Oo0 ( url )
def iIIii1i1Ii11 ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO
 iIIi = 'https://www.radionomy.com/en/search/index?query=' + ( oOOoooO ) . replace ( ' ' , '+' )
 oO0OOoo0OO = OoOooO ( iIIi )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']Stream - ' + I1i1i1iii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oOooO0 , 70005 , iIIii )
  if 98 - 98: o000O0o + ii - iiiiiiii1 % Ii / I11i . ii
  if 87 - 87: ooOoO0O00
def Ii1 ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , 'http://www.listenlive.eu/' + oOooO0 , 10111113 , III1iII1I1ii + 'radio.png' )
def oO0ooOoOO ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  i1i1iII1 ( I1i1i1iii , url , 222 , III1iII1I1ii + 'radio.png' )
  if 33 - 33: iiiiiiii1 % IIiIiII11i
def IIi1II ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.toonjet.com/' + oOooO0 , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def i11i ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( iIIIiIi )
 i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( iIIIiIi )
 for url , iIIii in i1IIIII11I1IiI :
  if 'ol.gif' in iIIii :
   pass
  elif 'link_block_' in iIIii :
   pass
  elif '.png' in iIIii :
   pass
  else :
   Iiiiii111i1ii ( ( iIIii ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in i1I :
  Iiiiii111i1ii ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii11I1I11II ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 43 - 43: o000O0o + ii . I11i . Ii1I
  if 30 - 30: I11i1ii1 - Ii + oOo0O0Ooo / I1ii11iIi11i % o0o00Oo0O
def IIO000oooOO0Oo0 ( ) :
 I1IiI ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 I1IiI ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
def IIIIIiiI11i1 ( ) :
 I1IiI ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 I1IiI ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 I1IiI ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 43 - 43: oOo0O0Ooo / O0OOOoOoo0 / I11i1ii1 + iI11I1II1I1I + ii
def iiI111i1 ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , oOooO0 , IiIii11i1IIiI in i1IIIII11I1IiI :
  if 'Parent' in I1i1i1iii :
   pass
  elif '2' in IiIii11i1IIiI :
   I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 40 - 40: O0OOOoOoo0 + iI11I1II1I1I * o000O0o + Ii . Ii
def iIii1I1111 ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , oOooO0 , IiIii11i1IIiI in i1IIIII11I1IiI :
  if oOOoooO in I1i1i1iii . lower ( ) :
   if '1' in IiIii11i1IIiI :
    I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in IiIii11i1IIiI :
    I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in IiIii11i1IIiI :
    I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 26 - 26: iiiiiiii1 . oOo0O0Ooo . O0OOOoOoo0 - ii / iI11I1II1I1I
    if 47 - 47: I1111IIi
def OOOoOOO0o0ooo ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , oOooO0 , IiIii11i1IIiI in i1IIIII11I1IiI :
  if '1' in IiIii11i1IIiI :
   I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in IiIii11i1IIiI :
   I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in IiIii11i1IIiI :
   I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 9 - 9: Ii1IIIi1 * ooOoO0O00 % I11i1ii1 . o0o00Oo0O
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 2 - 2: ii % iI11I1II1I1I
def I11iIiI1i1I1iiii1Ii11 ( url ) :
 OoO = url
 oO0OOoo0OO = OoOooO ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1I :
  if 'mp3' in I1i1i1iii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in I1i1i1iii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in I1i1i1iii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in I1i1i1iii :
   I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OoO + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 25 - 25: Ii / OOooOOo - iiiiiiii1 / oO0o . I11i . I11i
   if 6 - 6: o000O0o . ooOOOoO
   if 43 - 43: Ii1I + I11i
def iI1iiiiiii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OoO = url
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if 'Parent' in I1i1i1iii :
   pass
  elif '.db' in I1i1i1iii :
   pass
  elif '.jpg' in I1i1i1iii :
   pass
  elif '.html' in I1i1i1iii :
   pass
  elif '.doc' in I1i1i1iii :
   pass
  elif 'mp3' in I1i1i1iii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in I1i1i1iii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OoO + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 63 - 63: iI11I1II1I1I + I1111IIi % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
   if 60 - 60: I11i . OOooOOo % iiiiiiii1 / oOo0O0Ooo / o0o00Oo0O
def IiIii11I ( ) :
 I1IiI ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 I1IiI ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 I1IiI ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 97 - 97: ooOoO0O00 + O0OOOoOoo0 . I11i1ii1 - O0OOOoOoo0
def oooo0oOOoO000 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iIIii in i1IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oOooO0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in iIIii :
   pass
  else :
   I1IiI ( iIIii , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oOooO0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + iIIii + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 86 - 86: iI11I1II1I1I - ooOOOoO % I11i1ii1 . Ii1IIIi1 * OOooOOo . ooOoO0O00
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: ooOOOoO + I11i1ii1 / I11i1ii1 - Ii1IIIi1 * oO0o * I11i1ii1
 if 53 - 53: I1111IIi % I1ii11iIi11i
def IiIII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if '</a>' in I1i1i1iii :
   pass
  elif '(' in I1i1i1iii :
   I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 44 - 44: ii1ii11IIIiiI * I11i1ii1 / OOooOOo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 69 - 69: I11i1ii1 . Ii1IIIi1 - oOo0O0Ooo
def IiIi ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if oOOoooO in I1i1i1iii . lower ( ) :
   if '</a>' in I1i1i1iii :
    pass
   elif '(' in I1i1i1iii :
    I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 44 - 44: IIiIiII11i . IIiIiII11i + Ii1IIIi1 * ii1ii11IIIiiI
    if 16 - 16: IIiIiII11i
def oooOO0OO0 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if '</a>' in I1i1i1iii :
   pass
  elif '(' in I1i1i1iii :
   I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 10 - 10: oOo0O0Ooo / Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 68 - 68: Ii1IIIi1 - ii
 if 14 - 14: o0o00Oo0O / o000O0o - I1ii11iIi11i - I1111IIi
def ii11III ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OoO = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( OoO )
  if 42 - 42: Ii1I
def oOooOoOOo0O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  if '<p align' in I1i1i1iii :
   pass
  elif '&nbsp;' in I1i1i1iii :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 41 - 41: O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 88 - 88: o0o00Oo0O . o000O0o % oOo0O0Ooo
 if 10 - 10: oOo0O0Ooo + o0o00Oo0O
def O000O0OO00oo ( ) :
 oO0OOoo0OO = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'ongoing' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'CartoonShows.png' , '' , '' )
  if 'disney' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'Disney.png' , '' , '' )
  if 'genre' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'Genre.png' , '' , '' )
  if 'years' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'Years.png' , '' , '' )
def Oooo0Oo00o ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 IIoO = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , iIIii , iIIii , I1i1i1iii )
 for url , I1i1i1iii in IIoO :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def iI1Ii111I1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I1II1iIIi11 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OOOo0Oo0O = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0OOoo0OO )
 i1I1I1iIIi = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in OOOo0Oo0O :
  iiOOooooO0Oo ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , I1i1i1iii in i1I1II1iIIi11 :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def IiOo00O0o0O ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 86 - 86: ooOOOoO + o0o00Oo0O + I1ii11iIi11i - ooOOOoO
def ooo0oooo0 ( ) :
 oO0OOoo0OO = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 i1IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if '9cart' in oOooO0 :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 34 - 34: IIiIiII11i % oOo0O0Ooo % iiiiiiii1 + I1ii11iIi11i - OOooOOo
def O0Ooo0OOOo0oo ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 Iii1I1111ii = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if '9cart' in url :
   Iiiiii111i1ii ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   Iiiiii111i1ii ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url , I1i1i1iii in Iii1I1111ii :
  if '9cart' in url :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 11 - 11: ii1ii11IIIiiI + O0OOOoOoo0 * ooOoO0O00 % ii * ii1ii11IIIiiI * oO0o
def I1iO0o0O0OooOoo ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , url , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 20003 , iIIii )
 for url , I1i1i1iii in i1I :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 17 - 17: ii % o000O0o - ooOoO0O00 % I1111IIi % I1ii11iIi11i
def IiOO0OOOOOo ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'Watch' in url :
   Iiiiii111i1ii ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 7 - 7: o0o00Oo0O + ii1ii11IIIiiI . IIiIiII11i
def iii11i1i1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 20005 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 97 - 97: Ii1I
def OOo0oO0o ( url ) :
 url = cloudflare . source ( url )
 oOO0oo ( url )
 if 3 - 3: oOo0O0Ooo / iI11I1II1I1I % I11i
def O0oo0000o ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in i1IIIII11I1IiI :
  oOO0oo ( url )
  if 99 - 99: o000O0o - Ii1I . IIiIiII11i * Ii . Ii1IIIi1 - oO0o
  if 31 - 31: Ii * ii1ii11IIIiiI . I11i % Ii1IIIi1 * Ii1I % o0o00Oo0O
def oOOO ( ) :
 if 77 - 77: oO0o + oO0o . I11i1ii1 * ii + oO0o
 iiOOooooO0Oo ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 6 - 6: ooOoO0O00 - ooOOOoO
def IiI1I11iIii ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 89 - 89: I11i1ii1 - ooOOOoO . o0o00Oo0O % ii . Ii
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO0OOoo0OO )
 if 35 - 35: IIiIiII11i / OOooOOo - o0o00Oo0O . IIiIiII11i
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if oOOoooO in I1i1i1iii . lower ( ) :
   if 'Dad!' in I1i1i1iii :
    pass
   elif 'Family Guy' in I1i1i1iii :
    pass
   elif '2 Stupid' in I1i1i1iii :
    pass
   elif 'The Zelfs' in I1i1i1iii :
    pass
   elif 'A Clone' in I1i1i1iii :
    pass
   elif 'A.T.O.M' in I1i1i1iii :
    pass
   elif 'Almost Naked' in I1i1i1iii :
    pass
   elif 'Angry Kid' in I1i1i1iii :
    pass
   elif 'Annoying Orange' in I1i1i1iii :
    pass
   elif 'Aqua Teen' in I1i1i1iii :
    pass
   elif 'Assy Mcgee' in I1i1i1iii :
    pass
   elif 'Astroblast' in I1i1i1iii :
    pass
   elif 'Atomic Betty' in I1i1i1iii :
    pass
   elif 'Axe Cop' in I1i1i1iii :
    pass
   elif 'Baby Playpen' in I1i1i1iii :
    pass
   elif 'Beavis and Butt' in I1i1i1iii :
    pass
   elif 'Celebrity Deathmatch' in I1i1i1iii :
    pass
   elif 'Clerks The' in I1i1i1iii :
    pass
   elif 'Crapston Villas' in I1i1i1iii :
    pass
   elif 'Duckman:' in I1i1i1iii :
    pass
   elif 'Stripperella' in I1i1i1iii :
    pass
   elif 'Vixen' in I1i1i1iii :
    pass
   else :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
    if 55 - 55: I1ii11iIi11i % ooOoO0O00 * ooOOOoO
    if 95 - 95: Ii1IIIi1 / IIiIiII11i - I11i % iiiiiiii1 . ooOOOoO
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 63 - 63: iI11I1II1I1I / I11i1ii1
def OOO0ooo ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if 'Dad!' in I1i1i1iii :
   pass
  elif 'Family Guy' in I1i1i1iii :
   pass
  elif '2 Stupid' in I1i1i1iii :
   pass
  elif 'The Zelfs' in I1i1i1iii :
   pass
  elif 'A Clone' in I1i1i1iii :
   pass
  elif 'A.T.O.M' in I1i1i1iii :
   pass
  elif 'Almost Naked' in I1i1i1iii :
   pass
  elif 'Angry Kid' in I1i1i1iii :
   pass
  elif 'Annoying Orange' in I1i1i1iii :
   pass
  elif 'Aqua Teen' in I1i1i1iii :
   pass
  elif 'Assy Mcgee' in I1i1i1iii :
   pass
  elif 'Astroblast' in I1i1i1iii :
   pass
  elif 'Atomic Betty' in I1i1i1iii :
   pass
  elif 'Axe Cop' in I1i1i1iii :
   pass
  elif 'Baby Playpen' in I1i1i1iii :
   pass
  elif 'Beavis and Butt' in I1i1i1iii :
   pass
  elif 'Celebrity Deathmatch' in I1i1i1iii :
   pass
  elif 'Clerks The' in I1i1i1iii :
   pass
  elif 'Crapston Villas' in I1i1i1iii :
   pass
  elif 'Duckman:' in I1i1i1iii :
   pass
  elif 'Stripperella' in I1i1i1iii :
   pass
  elif 'Vixen' in I1i1i1iii :
   pass
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: I1ii11iIi11i / iI11I1II1I1I % Ii1IIIi1 * OOooOOo - iI11I1II1I1I
def iI1ii ( url ) :
 iIIIiIi = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIIiIi )
 for iIIii in i1I :
  oOoooOooOOoO = iIIii
 Iii1I1111ii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIIiIi )
 for url in Iii1I1111ii :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 10007 , oOoooOooOOoO )
  if 90 - 90: O0OOOoOoo0 * ii1ii11IIIiiI - O0OOOoOoo0 + oO0o + ooOOOoO % o0o00Oo0O
  if 11 - 11: Ii1IIIi1 % iiiiiiii1 * OOooOOo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 58 - 58: ii - ooOOOoO + iI11I1II1I1I * Ii
def OoOiII11IiIi ( url , IMAGE ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  print I1i1i1iii + '     ' + url
  if 'easy' in url :
   iII1I1i ( url )
   if 6 - 6: o000O0o / o0o00Oo0O / ii1ii11IIIiiI / I1111IIi / o000O0o . iI11I1II1I1I
   if 62 - 62: iI11I1II1I1I
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 4 - 4: Ii1I * ooOOOoO . ooOOOoO . IIiIiII11i / Ii1IIIi1
def iII1I1i ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  O00Oo0 ( url )
  if 86 - 86: o000O0o % o0o00Oo0O + oO0o
  if 52 - 52: I1ii11iIi11i / O0OOOoOoo0
  if 42 - 42: iI11I1II1I1I * ii1ii11IIIiiI / oO0o + Ii1IIIi1
def IiIII1 ( ) :
 if 48 - 48: ii - iiiiiiii1 . Ii * O0OOOoOoo0 - ii1ii11IIIiiI - I11i
 iiOOooooO0Oo ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , O0o0Oo , '' )
 if 59 - 59: O0OOOoOoo0 / ooOOOoO . I1ii11iIi11i
def o0III11IiI ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  if 'elete' in I1i1i1iii :
   pass
  else :
   i1i1iII1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 222 , iIIii )
   if 53 - 53: O0OOOoOoo0 / ooOoO0O00 / ooOoO0O00
def o0oo00O ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IIIIII1iI1II = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , iiiI1 , i1iII1IiiIiI1 in IIIIII1iI1II :
  for oOOoooO in iiiI1 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   O00oooO00oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oOooO0 , I1i1i1iii in O00oooO00oo :
    if 'tube' in oOooO0 :
     pass
    elif 'stage' in oOooO0 :
     i1i1iII1 ( '[COLOR' + II + ']' + iiiI1 + '   -   ' + I1i1i1iii + '[/COLOR]' , ( oOooO0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iIIii , )
    elif 'vee' in oOooO0 :
     pass
     if 44 - 44: iI11I1II1I1I * iiiiiiii1 * I1ii11iIi11i * Ii1I + ooOOOoO
def III1i1IIII1i ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IIIIII1iI1II = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , iiiI1 , i1iII1IiiIiI1 in IIIIII1iI1II :
  O00oooO00oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oOooO0 , I1i1i1iii in O00oooO00oo :
   if 'tube' in oOooO0 :
    pass
   elif 'stage' in oOooO0 :
    i1i1iII1 ( '[COLOR' + II + ']' + iiiI1 + '   -   ' + I1i1i1iii + '[/COLOR]' , ( oOooO0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + iIIii )
   elif 'vee' in oOooO0 :
    pass
    if 48 - 48: ii
    if 77 - 77: o0o00Oo0O * Ii1I * o000O0o + oO0o + Ii1I - iiiiiiii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: Ii1I + I1111IIi
def Oooooooo0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oo0OoOOO0o0 = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( oo0OoOOO0o0 ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in oo0OoOOO0o0 :
  i1I1IIIiiI ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 58 - 58: oOo0O0Ooo + ii / O0OOOoOoo0 . I11i1ii1 % I11i / Ii1I
  if 62 - 62: IIiIiII11i
  if 12 - 12: I1111IIi + IIiIiII11i
  if 92 - 92: iiiiiiii1 % iI11I1II1I1I - O0OOOoOoo0 / Ii % I11i1ii1 * I11i
  if 80 - 80: O0OOOoOoo0
  if 3 - 3: Ii1I * ooOOOoO
  if 53 - 53: iI11I1II1I1I / O0OOOoOoo0 % oO0o + I1111IIi / I11i1ii1
def Oo0OO0000oooo ( ) :
 if 74 - 74: I1ii11iIi11i
 IiIiII11i1 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 IiIiII11i1 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 44 - 44: oOo0O0Ooo % Ii1IIIi1 * Ii * Ii - I1ii11iIi11i . iiiiiiii1
 I1I11i ( 'movies' , 'MAIN' )
 if 68 - 68: O0OOOoOoo0 . ooOOOoO
def i111iiIiiIiI ( ) :
 IiIiII11i1 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 IiIiII11i1 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 59 - 59: Ii1IIIi1 + oOo0O0Ooo / IIiIiII11i / OOooOOo
 I1I11i ( 'movies' , 'MAIN' )
def oOoo00 ( ) :
 if 29 - 29: Ii1IIIi1 / OOooOOo . iI11I1II1I1I / ooOOOoO % OOooOOo % O0OOOoOoo0
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 oOOO0O0Ooo = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 49 - 49: IIiIiII11i / I1111IIi - ii1ii11IIIiiI
 for ii1i in oOOO0O0Ooo :
  IIi = O0Oo000ooO00 + ii1i + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( IIi )
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oOooO0 , IiI111ii1ii , oo00O00oO000o , o0ooooO0o0O , I1i1i1iii in i1IIIII11I1IiI :
   if oOOoooO in I1i1i1iii . lower ( ) :
    IiIIIoO0oOOooO0 ( I1i1i1iii , oOooO0 , 222 , IiI111ii1ii , o0ooooO0o0O , oo00O00oO000o )
    if 62 - 62: Ii - ooOOOoO
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 81 - 81: ooOOOoO
    if 92 - 92: Ii1IIIi1 - I1ii11iIi11i - ii / I1111IIi - ooOoO0O00
def Oo00o ( ) :
 if 3 - 3: I1ii11iIi11i . ii + ooOoO0O00 / ooOoO0O00 % iI11I1II1I1I / ii1ii11IIIiiI
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 oOOO0O0Ooo = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 66 - 66: ooOOOoO
 for ii1i in oOOO0O0Ooo :
  i1o0 = O0Oo000ooO00 + ii1i + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( i1o0 )
  i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1i1i1iii , oo00O00oO000o , oOooO0 , iIIii , o0ooooO0o0O , O0OOO0OOooo00 in i1IIIII11I1IiI :
   if oOOoooO in I1i1i1iii . lower ( ) :
    IiIiII11i1 ( I1i1i1iii , oOooO0 , O0OOO0OOooo00 , iIIii , o0ooooO0o0O , oo00O00oO000o )
    if 61 - 61: ooOOOoO
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 80 - 80: oOo0O0Ooo - oOo0O0Ooo
    if 52 - 52: IIiIiII11i
def iIii1II1I ( ) :
 if 25 - 25: OOooOOo
 iIIIiIi = OoOooO ( O0Oo000ooO00 + 'spongemain.php' )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , oo00O00oO000o , oOooO0 , iIIii , o0ooooO0o0O , O0OOO0OOooo00 in i1IIIII11I1IiI :
  IiIiII11i1 ( I1i1i1iii , oOooO0 , O0OOO0OOooo00 , iIIii , o0ooooO0o0O , oo00O00oO000o )
  I1I11i ( 'movies' , 'MAIN' )
def iii1IiII ( url ) :
 if 65 - 65: I11i1ii1 % o0o00Oo0O
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiiII1I = ( '%s%s' % ( IiIii , url ) )
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in i1IIIII11I1IiI :
  oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
  for oooO in oo0OO :
   if oooO == url :
    I1i1i1iii = ( '[COLORred]Watched - [/COLOR]' + I1i1i1iii ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  IiIIIoO0oOOooO0 ( I1i1i1iii , url , 222 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
  if 57 - 57: Ii1IIIi1 . ii1ii11IIIiiI % I11i
  I1I11i ( 'movies' , 'MAIN' )
  if 32 - 32: ooOOOoO / I1111IIi - o0o00Oo0O * iI11I1II1I1I
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 70 - 70: ii % ii % oO0o
  if 98 - 98: oO0o
def I1IIiIi ( url ) :
 if 93 - 93: o000O0o - Ii1IIIi1 + I11i . o000O0o / ooOOOoO
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , oo00O00oO000o , url , iIIii , o0ooooO0o0O , O0OOO0OOooo00 in i1IIIII11I1IiI :
  IiIiII11i1 ( I1i1i1iii , url , O0OOO0OOooo00 , iIIii , o0ooooO0o0O , oo00O00oO000o )
  if 52 - 52: iiiiiiii1 + iiiiiiii1
  I1I11i ( 'movies' , 'MAIN' )
  if 73 - 73: I11i . Ii % ii + I11i1ii1 . ii / Ii1IIIi1
  if 54 - 54: OOooOOo . ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: o000O0o / IIiIiII11i * I1111IIi % Ii1I
def IiIIIoO0oOOooO0 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 31 - 31: IIiIiII11i + Ii1IIIi1 - ii . ooOOOoO
 O0ooO00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11i1iIiii = True
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOO00OO0oOo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1I1iI = [ ]
  I1I1iI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1I1iI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   I1I1iI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OOO00OO0oOo . addContextMenuItems ( I1I1iI )
 i11i1iIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = False )
 return i11i1iIiii
 if 28 - 28: ii1ii11IIIiiI . Ii1I
def IiIiII11i1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 77 - 77: Ii1I % IIiIiII11i
 O0ooO00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11i1iIiii = True
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOO00OO0oOo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1I1iI = [ ]
  I1I1iI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1I1iI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   I1I1iI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OOO00OO0oOo . addContextMenuItems ( I1I1iI )
 i11i1iIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = True )
 return i11i1iIiii
if 81 - 81: OOooOOo % ii1ii11IIIiiI / o0o00Oo0O * iI11I1II1I1I % I1111IIi . oOo0O0Ooo
if 90 - 90: I11i
if 44 - 44: I11i / Ii1I . I1ii11iIi11i + OOooOOo
if 32 - 32: I1111IIi - I11i1ii1 * O0OOOoOoo0 * ooOOOoO
if 84 - 84: ii1ii11IIIiiI + Ii1I % oOo0O0Ooo + Ii
if 37 - 37: ooOOOoO % Ii1I / I11i1ii1
if 94 - 94: ooOOOoO / oO0o . I11i
if 1 - 1: I1ii11iIi11i . IIiIiII11i
if 93 - 93: IIiIiII11i . Ii + IIiIiII11i % o000O0o
if 98 - 98: iiiiiiii1 * o000O0o * OOooOOo + ii1ii11IIIiiI * O0OOOoOoo0
if 4 - 4: I1111IIi
if 16 - 16: iI11I1II1I1I * O0OOOoOoo0 + o000O0o . o0o00Oo0O . I11i
if 99 - 99: Ii - O0OOOoOoo0
if 85 - 85: iiiiiiii1 % Ii1I
if 95 - 95: oO0o * Ii1IIIi1 * O0OOOoOoo0 . I11i
def oooOo00 ( string ) :
 if OOoOO0oo0ooO == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 1 - 1: oOo0O0Ooo + Ii1I
def Ooo0oO0 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OOo0 = [ ]
 try :
  if 25 - 25: iiiiiiii1 - ii1ii11IIIiiI / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( IIIii1II1II ) == False :
  oooOo00 ( 'Making Favorites File' )
  OOo0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  o0ooOOoO0oO0 = open ( IIIii1II1II , "w" )
  o0ooOOoO0oO0 . write ( json . dumps ( OOo0 ) )
  o0ooOOoO0oO0 . close ( )
 else :
  oooOo00 ( 'Appending Favorites' )
  o0ooOOoO0oO0 = open ( IIIii1II1II ) . read ( )
  Ii1i = json . loads ( o0ooOOoO0oO0 )
  Ii1i . append ( ( name , url , iconimage , fanart , mode ) )
  iIiiI11II11i = open ( IIIii1II1II , "w" )
  iIiiI11II11i . write ( json . dumps ( Ii1i ) )
  iIiiI11II11i . close ( )
  if 49 - 49: o000O0o + o000O0o + Ii % O0OOOoOoo0
  if 39 - 39: ooOOOoO / O0OOOoOoo0 + ooOoO0O00 % Ii1IIIi1
def Oo0oOooOooO ( ) :
 if os . path . exists ( IIIii1II1II ) == False :
  OOo0 = [ ]
  oooOo00 ( 'Making Favorites File' )
  OOo0 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  o0ooOOoO0oO0 = open ( IIIii1II1II , "w" )
  o0ooOOoO0oO0 . write ( json . dumps ( OOo0 ) )
  o0ooOOoO0oO0 . close ( )
 else :
  ii1I1iIII = json . loads ( open ( IIIii1II1II ) . read ( ) )
  IIii1 = len ( ii1I1iIII )
  for II1iII1 in ii1I1iIII :
   I1i1i1iii = II1iII1 [ 0 ]
   oOooO0 = II1iII1 [ 1 ]
   IiI111ii1ii = II1iII1 [ 2 ]
   try :
    I11II11IiI11 = II1iII1 [ 3 ]
    if I11II11IiI11 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     I11II11IiI11 = IiI111ii1ii
    else :
     I11II11IiI11 = o0ooooO0o0O
   try : O00oIi11Iiii1iiii = II1iII1 [ 5 ]
   except : O00oIi11Iiii1iiii = None
   try : i1IIII1111 = II1iII1 [ 6 ]
   except : i1IIII1111 = None
   if 84 - 84: o0o00Oo0O % ii1ii11IIIiiI . ii1ii11IIIiiI . O0OOOoOoo0 * ooOOOoO
   if II1iII1 [ 4 ] == 0 :
    iiOOooooO0Oo ( I1i1i1iii , oOooO0 , '' , IiI111ii1ii , o0ooooO0o0O , '' , 'fav' )
   else :
    iiOOooooO0Oo ( I1i1i1iii , oOooO0 , II1iII1 [ 4 ] , IiI111ii1ii , o0ooooO0o0O , '' , 'fav' )
    if 43 - 43: OOooOOo . Ii1I % ooOoO0O00
def OO0O00 ( name ) :
 Ii1i = json . loads ( open ( IIIii1II1II ) . read ( ) )
 for ooOO in range ( len ( Ii1i ) ) :
  if Ii1i [ ooOO ] [ 0 ] == name :
   del Ii1i [ ooOO ]
   iIiiI11II11i = open ( IIIii1II1II , "w" )
   iIiiI11II11i . write ( json . dumps ( Ii1i ) )
   iIiiI11II11i . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 66 - 66: I1ii11iIi11i / Ii % I11i1ii1
 if 43 - 43: Ii1IIIi1
def oOo0OOO00Oo ( ) :
 o0IiiIIII1I1i = os . path . join ( I11i1 , 'addons.ini' )
 I1IIIIII1 = open ( o0IiiIIII1I1i , "w+" )
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oO0OOoo0OO )
 I1IIIIII1 . write ( r'[' + IiII + ']' + '\n' )
 for I1i1i1iii , iIIii , O0oO0O , oOooO0 in i1IIIII11I1IiI :
  oOooO0 = ( oOooO0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  IIiiiII11i = ( I1i1i1iii + '=plugin://' + IiII + '/?url=' + oOooO0 + '&mode=10012&name=' + ( I1i1i1iii ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( iIIii ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( iIIii ) . replace ( ' ' , '' ) + '+&amp;description=' )
  I1IIIIII1 . write ( IIiiiII11i + '\n' )
  if 34 - 34: I11i % ii
  if 36 - 36: oOo0O0Ooo
def Oo0ooo ( ) :
 iIIIiIi = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '24/7' , oOooO0 , 90021 , III1iII1I1ii + '247Streams.png' )
  if 73 - 73: IIiIiII11i + Ii1IIIi1 * O0OOOoOoo0 / O0OOOoOoo0
def OoOo0O0 ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1i1i1iii , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + '247Streams.png' , III1iII1I1ii + '247Streams.png' , '' )
def OO0oI1iii1i ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1i1i1iii , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def iIIiiiI ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1i1i1iii , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def I1o0 ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1i1i1iii , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def I1IiiiiI1i1I ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 i1IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1i1i1iii , oOooO0 , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 48 - 48: ooOOOoO + IIiIiII11i % o000O0o % Ii1IIIi1 * IIiIiII11i
  if 41 - 41: oO0o
def i1iiiiii1 ( ) :
 if 83 - 83: oOo0O0Ooo - iiiiiiii1 + oOo0O0Ooo . oOo0O0Ooo
 iiOOooooO0Oo ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 if 45 - 45: ooOoO0O00 % Ii1IIIi1 % IIiIiII11i
def IIIIi1Iii1iIi ( ) :
 if 36 - 36: Ii * Ii1I * OOooOOo
 iIIIiIi = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , iIIii , I1i1i1iii , O0o0oo0oOO0oO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii + '  -  ' + ( O0o0oo0oOO0oO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOooO0 , 10023 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 24 - 24: o000O0o . o0o00Oo0O * I11i1ii1 / ii - ii1ii11IIIiiI . ooOOOoO
  if 41 - 41: oO0o % oOo0O0Ooo - I1ii11iIi11i
  if 11 - 11: ii1ii11IIIiiI * I11i / I1111IIi + OOooOOo + oO0o % iiiiiiii1
def iIIi1II1 ( ) :
 if 42 - 42: iI11I1II1I1I - I11i1ii1 - ooOOOoO - iiiiiiii1
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
 if 33 - 33: OOooOOo - o0o00Oo0O
def III11iI1i11i ( url ) :
 I1III1i1I = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0OOoo0OO = cloudflare . source ( I1III1i1I )
 i1IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 30 - 30: OOooOOo / o000O0o / ii1ii11IIIiiI * I11i * o000O0o . oOo0O0Ooo
  if 93 - 93: OOooOOo
  if 97 - 97: Ii
  if 68 - 68: I1111IIi * oO0o . ooOOOoO / ii1ii11IIIiiI . I11i - Ii
def II11I ( ) :
 if 72 - 72: oO0o - iI11I1II1I1I . O0OOOoOoo0 / ii1ii11IIIiiI
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 oOooO0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oOOoooO ) . replace ( ' ' , '+' )
 oO0OOoo0OO = cloudflare . source ( oOooO0 )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  if oOOoooO in I1i1i1iii . lower ( ) :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 10022 , III1iII1I1ii + 'dtv.png' )
   if 12 - 12: oOo0O0Ooo + iiiiiiii1
   if 80 - 80: o000O0o . o0o00Oo0O
   if 90 - 90: IIiIiII11i / oO0o / ii1ii11IIIiiI
def O0oooOOo0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO , O0Oo0o000oO , IIi11ii , I1i1i1iii in i1IIIII11I1IiI :
  IiI111I = ( IIi11ii ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oo0oO0 = ( O0Oo0o000oO ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ii1i1Iii = 'Season ' + oo0oO0 + 'Episode ' + IiI111I + I1i1i1iii
  IIII11111Ii ( ii1i1Iii , OoO )
  if 21 - 21: o0o00Oo0O + o0o00Oo0O / I11i - ooOOOoO
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 88 - 88: Ii1I . IIiIiII11i / Ii1IIIi1 % ooOoO0O00 - OOooOOo % Ii
  if 61 - 61: ii . o0o00Oo0O % I11i * o0o00Oo0O
def IIII11111Ii ( name , url ) :
 OoO = url
 III1iIii = name
 O0 = cloudflare . source ( OoO )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for oo0OoOOO0o0 , iiIII1i1 in i1I :
  i1i1iII1 ( '[COLOR' + II + ']' + III1iIii + iiIII1i1 + '[/COLOR]' , oo0OoOOO0o0 , 222 , III1iII1I1ii + 'dtv.png' )
  if 78 - 78: o000O0o % OOooOOo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 1 - 1: OOooOOo - I11i / I11i1ii1 - I1111IIi / ooOoO0O00
 if 28 - 28: oO0o / iiiiiiii1 * oOo0O0Ooo + I11i1ii1
def O00 ( ) :
 if 48 - 48: o0o00Oo0O
 if 44 - 44: oO0o * o000O0o
 if 54 - 54: ii1ii11IIIiiI % ooOoO0O00
 if 51 - 51: iI11I1II1I1I - oOo0O0Ooo
 if 61 - 61: ii . ii1ii11IIIiiI % o000O0o * ii
 if 96 - 96: ii1ii11IIIiiI - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 if 75 - 75: I1ii11iIi11i + ii1ii11IIIiiI + oO0o
 iiOOooooO0Oo ( '[COLOR' + II + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , '' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 97 - 97: I11i1ii1 % Ii % ooOOOoO
def IIi1i ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oO0oi1I1iI1 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for iIIii , url , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + iIIii , '' , '' )
 for url in oO0oi1I1iI1 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 91 - 91: o000O0o / iI11I1II1I1I + o000O0o
def iii1i1Iiiiiii ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oO0oi1I1iI1 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for iIIii , url , I1i1i1iii in i1IIIII11I1IiI :
  iIIii = 'http://watchepisodes.cc/' + iIIii
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 10093 , iIIii , iIIii , '' )
 for url in oO0oi1I1iI1 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 58 - 58: I11i / Ii / o0o00Oo0O % ooOOOoO % oOo0O0Ooo
def O0oOOo0 ( url , iconimage ) :
 iIIii = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for IIi11ii , url , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + IIi11ii + ' - ' + I1i1i1iii + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , iIIii , '' , '' )
  if 71 - 71: Ii % iI11I1II1I1I
def iiI1IiII1III1I11I1 ( url , iconimage ) :
 iIIii = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  if 'player' in I1i1i1iii :
   pass
  elif 'vod' in I1i1i1iii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , iIIii , '' , '' )
   if 85 - 85: iiiiiiii1
   if 62 - 62: ii1ii11IIIiiI % IIiIiII11i + I1111IIi + Ii1IIIi1 % o000O0o . oOo0O0Ooo
   if 53 - 53: oO0o % Ii1I . O0OOOoOoo0 . ooOoO0O00 . oO0o
   if 26 - 26: oOo0O0Ooo % OOooOOo
   if 67 - 67: I1ii11iIi11i - I1111IIi * ii1ii11IIIiiI . ii / Ii
   if 61 - 61: I11i % oOo0O0Ooo * ooOoO0O00 / oOo0O0Ooo / IIiIiII11i + iiiiiiii1
def Oo0o0000OOoO ( ) :
 if 22 - 22: I1111IIi . O0OOOoOoo0 + I1ii11iIi11i
 if 45 - 45: I1ii11iIi11i % I1ii11iIi11i + I1ii11iIi11i / o0o00Oo0O % ii
 if 92 - 92: ii1ii11IIIiiI . OOooOOo . ooOOOoO - ii / I11i1ii1
 if 80 - 80: iI11I1II1I1I / Ii + O0OOOoOoo0
 if 41 - 41: iiiiiiii1 + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
 if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
 if 25 - 25: ii . ii1ii11IIIiiI % O0OOOoOoo0 . I1111IIi
 if 67 - 67: ii + iiiiiiii1 / I11i1ii1
 if 75 - 75: I1111IIi / ii . oOo0O0Ooo + iiiiiiii1 - IIiIiII11i
 if 33 - 33: I1111IIi / I1111IIi . Ii * Ii1I + I11i
 if 16 - 16: I1111IIi
 if 10 - 10: OOooOOo . I1111IIi * iI11I1II1I1I - o000O0o - OOooOOo / iiiiiiii1
 if 13 - 13: o000O0o + OOooOOo % I1111IIi % ii
 if 22 - 22: iiiiiiii1
 iiOOooooO0Oo ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , III1iII1I1ii + 'latest.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , III1iII1I1ii + 'popular.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , III1iII1I1ii + 'Genre.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , III1iII1I1ii + 'series.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 if 23 - 23: o0o00Oo0O
 if 41 - 41: ooOoO0O00 . Ii1IIIi1 / I11i1ii1 / I11i % I1111IIi - ii1ii11IIIiiI
def iI1i1Iiii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I1IIIiI1I1ii1 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 15 - 15: ii1ii11IIIiiI
def iIII1IIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 63 - 63: IIiIiII11i . iiiiiiii1 % I1111IIi + IIiIiII11i
def oO0OOoOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if 'episode' in url :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 97 - 97: ooOoO0O00
  if 46 - 46: Ii1I
def II1i1 ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o0oo0OOo0O0 = 'http://www.watchseriesgo.to/search/' + oOOoooO . replace ( ' ' , '%20' )
 oO0OOoo0OO = OoOooO ( o0o0oo0OOo0O0 )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'watch online' in I1i1i1iii :
   pass
  else :
   print oOooO0
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.watchseriesgo.to' + oOooO0 , 10044 , iIIii , '' , '' )
   if 37 - 37: I11i * I1ii11iIi11i
   xbmcplugin . setContent ( O000oo0O , 'movies' )
   if 11 - 11: o000O0o
def Oo0O0o00o00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , url , I1i1i1iii , IIi11ii , oo00O00oO000o in i1IIIII11I1IiI :
  I1IIIiii1 = ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( IIi11ii ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1IIIiii1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , iIIii , '' , oo00O00oO000o )
  if 90 - 90: iiiiiiii1 . IIiIiII11i . Ii1I
def I1iIi1111 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  I1IIIiii1 = ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1IIIiii1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 25 - 25: I1ii11iIi11i - O0OOOoOoo0 / I11i1ii1 . I1111IIi / iI11I1II1I1I
def OO0ooo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , iIIii , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 63 - 63: IIiIiII11i - ooOOOoO . OOooOOo
def IIi1I1iII111 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 I1IIIiI1I1ii1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0Oo0o000oO , IIIIII1iI1II in I1IIIiI1I1ii1 :
  i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( IIIIII1iI1II ) )
  for url , I1i1i1iii in i1IIIII11I1IiI :
   I1IIIiii1 = ( O0Oo0o000oO ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1IIIiii1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 76 - 76: I11i1ii1 . o000O0o
class oO00OO0o0ooO ( ) :
 if 42 - 42: o0o00Oo0O * O0OOOoOoo0 . OOooOOo / Ii1IIIi1 - ii1ii11IIIiiI . ooOOOoO
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 57 - 57: I11i + I1ii11iIi11i * Ii1I - I11i1ii1 % iI11I1II1I1I - ii1ii11IIIiiI
  I1IIIiii1 = name
  self . Get_Sources ( oOooO0 , I1IIIiii1 )
  if 37 - 37: oO0o * ooOOOoO + ii1ii11IIIiiI + Ii1I * I11i
  if 95 - 95: ii1ii11IIIiiI - Ii % Ii - o0o00Oo0O * iiiiiiii1
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  oO0OOoo0OO = OoOooO ( URL )
  i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + oOooO0
   self . Get_site_link ( URL , season_name )
   if 81 - 81: IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * Ii + OOooOOo
 def Get_site_link ( self , url , season_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  Iii1I1111ii = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for url in i1IIIII11I1IiI :
   self . main ( url , season_name )
  for url in i1I :
   self . main ( url , season_name )
  for url in Iii1I1111ii :
   self . main ( url , season_name )
   if 100 - 100: ooOoO0O00 % ii1ii11IIIiiI
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   oO000O = 'DACLIPS'
   if oO000O in oO00OO0o0ooO . source_list :
    pass
   else :
    self . daclips ( url , season_name , oO000O )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    oO000O = 'THEVIDEO'
    if oO000O in oO00OO0o0ooO . source_list :
     pass
    else :
     self . thevideo ( url , season_name , oO000O )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     oO000O = 'ALLMYVIDEOS'
     if oO000O in oO00OO0o0ooO . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , oO000O )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      oO000O = 'VIDSPOT'
      if oO000O in oO00OO0o0ooO . source_list :
       pass
      else :
       self . vidspot ( url , season_name , oO000O )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       oO000O = 'VODLOCKER'
       if oO000O in oO00OO0o0ooO . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , oO000O )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        oO000O = 'VIDTO'
        if oO000O in oO00OO0o0ooO . source_list :
         pass
        else :
         self . vidto ( url , season_name , oO000O )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 62 - 62: ooOoO0O00 * iI11I1II1I1I % o000O0o % OOooOOo / ii
       else :
        if 'youwatch' in url :
         oO000O = 'YouWatch'
         if oO000O in oO00OO0o0ooO . source_list :
          pass
         else :
          self . youwatch ( url , season_name , oO000O )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 39 - 39: I1ii11iIi11i % O0OOOoOoo0
          if 90 - 90: oOo0O0Ooo * Ii1I . ooOOOoO * ii1ii11IIIiiI - I11i
 def allmyvid ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oOO , I1i1i1iii in i1IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 40 - 40: o0o00Oo0O / I1111IIi - IIiIiII11i + I11i % I1ii11iIi11i
 def vidspot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for oOO , I1i1i1iii in i1IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 93 - 93: I11i1ii1
 def thevideo ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( oO0OOoo0OO )
  for oOO in i1IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 82 - 82: Ii1I / I11i1ii1 . Ii + Ii1IIIi1 - OOooOOo / O0OOOoOoo0
 def vodlocker ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for oOO in i1IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 99 - 99: o000O0o / ooOoO0O00
 def daclips ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oO0OOoo0OO )
  for oOO in i1IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 2 - 2: o000O0o . O0OOOoOoo0
 def filehoot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for oOO in i1IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for oOO in i1IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for oOO in i1IIIII11I1IiI :
   self . youplay ( oOO , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for oOO in i1IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 42 - 42: oO0o - Ii1I * I1111IIi - I11i1ii1
 def Printer ( self , Link , season_name , source_name ) :
  if 75 - 75: O0OOOoOoo0 * I1ii11iIi11i / iiiiiiii1 * I1ii11iIi11i / I11i1ii1
  if Link in oO00OO0o0ooO . List :
   pass
  elif source_name in oO00OO0o0ooO . source_list :
   pass
  else :
   i1i1iII1 ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 222 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   oO00OO0o0ooO . List . append ( Link )
   oO00OO0o0ooO . source_list . append ( source_name )
   if 14 - 14: ooOoO0O00 * iI11I1II1I1I - ii1ii11IIIiiI * OOooOOo - O0OOOoOoo0 / o000O0o
   xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 73 - 73: Ii1I - OOooOOo * o0o00Oo0O - OOooOOo - oO0o
   if 96 - 96: Ii1I - o0o00Oo0O
   if 35 - 35: Ii1IIIi1 . ooOOOoO . iiiiiiii1 - ooOOOoO % ooOOOoO + iiiiiiii1
   if 99 - 99: I11i + Ii1IIIi1
   if 34 - 34: iiiiiiii1 * I11i . oOo0O0Ooo % Ii
def iIiIiIiI ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 61 - 61: iI11I1II1I1I + o000O0o * ooOOOoO - ooOoO0O00 % o000O0o
def oOOo ( url ) :
 iiOOooooO0Oo ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( iIIIiIi )
 for I1II1iIi , url , IIiIi1II1IiI , oo0OoO , I11iIiiI , oO0oiIiI , OO000oo0o , iiiiI , o0ooOOoO0oO0 , I11iiIiI1II11 , OOOoOOOo in i1IIIII11I1IiI :
  IIiIi1II1IiI = IIiIi1II1IiI
  if 'Arsenal' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'arsenal-logo.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                                  ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Bournemouth' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'afc-bournemouth.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                       ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Burnley' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'KEGnQWW.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                                   ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Chelsea' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'chelsea.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                                  ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Crystal' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'CrystalPalace.0.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                       ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Everton' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'Everton.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                                   ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Hull' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'hull-city-afc.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                                 ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Leicester' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'leicester-city-fc-hd-logo.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                       ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Liverpool' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'liverpool-logo.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                               ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Manchester City' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'city-logo.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '               ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Manchester United' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + '91.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '          ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Middlesbrough' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'middlesbrough-fc-hd-logo.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                 ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Southampton' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'southampton-fc-logo.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                   ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Stoke City' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'stoke-city.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                          ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Sunderland' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'sunderland-logo.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                        ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Swansea' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'swansea-city-afc.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                    ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Tottenham' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'tottenham-hotspur_zps4e3ed7c1.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '        ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Watford' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'watford-fc-hd-logo.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '                              ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'Bromwich' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'west-bromwich-albion-logo.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '   ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  elif 'West Ham' in IIiIi1II1IiI :
   I111iIi1 = III1iII1I1ii + 'west-ham.png'
   I1i1i1iii = '[COLOR' + II + ']' + I1II1iIi + ' - ' + IIiIi1II1IiI + '             ' + oo0OoO + '        ' + I11iIiiI + '        ' + oO0oiIiI + '        ' + OO000oo0o + '        ' + iiiiI + '        ' + o0ooOOoO0oO0 + '        ' + I11iiIiI1II11 + '[/COLOR]'
  iiOOooooO0Oo ( str ( I1i1i1iii ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , I111iIi1 , I111iIi1 , IIiIi1II1IiI )
  if 82 - 82: I1ii11iIi11i + iiiiiiii1
def O00oOOoOOOOO ( description ) :
 IIiIi1II1IiI = description
 oOooO0 = ( 'http://www.fullmatchesandshows.com/?s=' + IIiIi1II1IiI ) . replace ( ' ' , '%20' )
 ii1IIii ( oOooO0 )
 if 11 - 11: oOo0O0Ooo - ii1ii11IIIiiI * Ii1IIIi1 % I11i
def II1II ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 i1IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOooO0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iIIii , O0o0Oo , '' )
  if 74 - 74: oOo0O0Ooo . I11i1ii1 / O0OOOoOoo0 . I1111IIi
def OO00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I1IIIiI1I1ii1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
  o0Oo0oO = re . compile ( '(.*?)</h2>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for I1iiiIi1i11i in o0Oo0oO :
   I1iiiIi1i11i = I1iiiIi1i11i
  I111I1iii11 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for IIi11i1IIi11 , iIIii , time , II1IIiIi1 in I111I1iii11 :
   iiO0o0O0oo0o = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( II1IIiIi1 )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1iiiIi1i11i + ' - ' + IIi11i1IIi11 + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + iIIii , O0o0Oo , ( str ( iiO0o0O0oo0o ) ) )
   if 49 - 49: iiiiiiii1 / IIiIiII11i
 I1I11i ( 'tvshows' , 'Media Info 3' )
 if 69 - 69: I11i + Ii1I / iI11I1II1I1I . I1111IIi % Ii1I * OOooOOo
def Iii1i11 ( ) :
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
 if 25 - 25: iI11I1II1I1I + Ii - ii1ii11IIIiiI * ii
def i1I11IiI ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , url , I1i1i1iii in i1IIIII11I1IiI :
  iiiiIIi = I1i1i1iii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1i1i1iii :
   pass
  else :
   iiiiIIi = I1i1i1iii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   i1i1iII1 ( '[COLOR' + II + ']' + iiiiIIi + '[/COLOR]' , url , 10013 , iIIii )
 for url , iIIii , I1i1i1iii in i1I :
  iiiiIIi = I1i1i1iii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1i1i1iii :
   pass
  else :
   i1i1iII1 ( '[COLOR' + II + ']' + iiiiIIi + '[/COLOR]' , url , 10013 , iIIii )
def ii1IIii ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 if 53 - 53: I11i1ii1 . Ii1IIIi1 . I11i + o000O0o
 if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + ii1ii11IIIiiI % ooOoO0O00 . o000O0o
 if 57 - 57: o000O0o
 if 92 - 92: IIiIiII11i - oO0o - Ii1IIIi1 % oOo0O0Ooo - OOooOOo * iiiiiiii1
 if 16 - 16: iI11I1II1I1I + ii - I11i1ii1 * I1111IIi
 if 37 - 37: O0OOOoOoo0
 if 15 - 15: I11i % oO0o / O0OOOoOoo0
 for url , iIIii , I1i1i1iii in i1I :
  iiiiIIi = I1i1i1iii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1i1i1iii :
   pass
  else :
   i1i1iII1 ( '[COLOR' + II + ']' + iiiiIIi + '[/COLOR]' , url , 10013 , iIIii )
   if 36 - 36: oO0o + oO0o % I1ii11iIi11i + I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
def iII1I1IIiiiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oO0OOoo0OO )
 for oo0OoOOO0o0 in i1IIIII11I1IiI :
  IIiiIiIIiI1 = ( oo0OoOOO0o0 ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  i1I1IIIiiI ( 'http:' + IIiiIiIIiI1 )
  if 39 - 39: ooOOOoO / ii - ii1ii11IIIiiI + oO0o / OOooOOo
  if 87 - 87: iiiiiiii1
  if 32 - 32: ooOOOoO - Ii1IIIi1 * o0o00Oo0O % I1111IIi . I1111IIi . oOo0O0Ooo
  if 91 - 91: ooOoO0O00 . O0OOOoOoo0
def I1I1iiI1i ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIIIiIi )
 for url , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  i1i1iII1 ( I1i1i1iii , url , 8046 , iIIii )
 for url in i1I :
  Iiiiii111i1ii ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def IiII1111I ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIIIiIi )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  i1I1IIIiiI ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 15 - 15: iI11I1II1I1I % I1ii11iIi11i + ii
def I1Ii111I111 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 7 - 7: oOo0O0Ooo
def O0Oo000 ( ) :
 Iiiiii111i1ii ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , III1iII1I1ii + 'documentary.png' )
 Iiiiii111i1ii ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , III1iII1I1ii + 'documentary.png' )
 Iiiiii111i1ii ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , III1iII1I1ii + 'Search.png' )
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , oOooO0 , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def i111i11iI1i1I ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIIiIi )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( iIIIiIi )
 for iIIii , url , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + iIIii )
 for url in next :
  Iiiiii111i1ii ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 17 - 17: IIiIiII11i / iiiiiiii1 - iiiiiiii1 + ooOoO0O00 . oO0o / oO0o
  if 5 - 5: OOooOOo % Ii1I . I11i1ii1 . ooOOOoO - Ii
def Ii11I1 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIIiIi )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   i1i1iII1 ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   Iiiiii111i1ii ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def OO00OO ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  i1i1iII1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 222 , '' )
  if 27 - 27: o0o00Oo0O * oOo0O0Ooo - iI11I1II1I1I - O0OOOoOoo0 % o0o00Oo0O . I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1ii11IiI1I ( name , url ) :
 Oo0 = 0
 name = name
 url = url
 O0oO0 = [ '144' , '240' , '380' , '480' , '720' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  O00Oo0 ( url )
  if 20 - 20: o0o00Oo0O . Ii * ooOoO0O00 % o0o00Oo0O . oOo0O0Ooo
  if 53 - 53: I11i1ii1 / ii - IIiIiII11i
  if 68 - 68: ii . ii . iI11I1II1I1I / I11i1ii1 - ooOOOoO % o0o00Oo0O
  if 19 - 19: ii * o000O0o
  if 60 - 60: IIiIiII11i - O0OOOoOoo0 + I11i % Ii1IIIi1
  if 97 - 97: o0o00Oo0O % o0o00Oo0O
  if 35 - 35: O0OOOoOoo0 - ii1ii11IIIiiI . Ii % o0o00Oo0O % Ii1I
  if 92 - 92: Ii1IIIi1 % IIiIiII11i . O0OOOoOoo0
def II1i1iI ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( 'http://documentarylovers.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( iIIIiIi )
 for I1i1i1iii , oOooO0 in i1IIIII11I1IiI :
  if 'genre' in oOooO0 :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oOooO0 , 80010 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI111I1 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( iIIIiIi )
 for url , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , iIIii )
 for url in next :
  Iiiiii111i1ii ( 'NEXT PAGE' , url , 80010 , III1iII1I1ii + 'Next.png' )
  if 46 - 46: ii1ii11IIIiiI
def ii1o0 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( iIIIiIi )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
 for url in i1I :
  OO00OO ( url )
  if 67 - 67: ii - o0o00Oo0O
def iiIi1I ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 O0Oo0 = 'http://documentarylovers.com/?s=' + ( oOOoooO ) . replace ( ' ' , '+' )
 i1ii11 = O0Oo0 . lower ( )
 iI111I1 ( i1ii11 )
 if 23 - 23: oO0o % ii * I11i1ii1
def Iii11I ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if 'films' in url :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , III1iII1I1ii + 'documentary.png' )
def iI1ii1 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIIiIi )
 for iIIii , url , I1i1i1iii in i1IIIII11I1IiI :
  if 'films' in url :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + iIIii )
 for url in i1I :
  Iiiiii111i1ii ( 'NEXT' , url , 8049 , III1iII1I1ii + 'Next.png' )
def O0oOOo ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  if 'rtd' in url :
   ii111IIiiiiI ( url )
   if 98 - 98: ooOoO0O00 - O0OOOoOoo0
def ii111IIiiiiI ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iIIIiIi )
 for i1i , file in i1IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1i + file )
  O00Oo0 ( url )
  if 49 - 49: I11i . ii1ii11IIIiiI . o000O0o
  if 9 - 9: I1111IIi - IIiIiII11i * oO0o
def Oo0oo ( ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( 'http://www.stream2watch.co/live-tv' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iIIii , I1i1i1iii , iiiI1i11Ii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( I1i1i1iii + '[COLOR' + II + ']' + iiiI1i11Ii + '[/COLOR]' ) , oOooO0 , 8086 , iIIii )
  if 64 - 64: OOooOOo % iI11I1II1I1I
def iII1I1Ii11i1i ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 8087 , iIIii )
  if 80 - 80: Ii % iI11I1II1I1I / Ii
def OOoOO0ooo0O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  ii1IIi1IIIIi1 ( url , I1i1i1iii )
  if 4 - 4: Ii1I - I1111IIi
def ii1IIi1IIIIi1 ( url , name ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  print url
  i1i1iII1 ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 6 - 6: o0o00Oo0O . ii . iiiiiiii1 - ii1ii11IIIiiI / I11i1ii1
def iIIIIIi11Ii ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oOooO0 , 3002 , 'http://www.solie.org/alibrary/' + iIIii )
def oOOooo ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIIiIi )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iIIii )
def iIi11i1I11Ii ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIIiIi )
 oo0OO0oo = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIIIiIi )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIIIiIi )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , I1i1i1iii in oo0OO0oo :
  Iiiiii111i1ii ( '[COLOR' + II + ']Season- ' + I1i1i1iii + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , iIIii , I1i1i1iii in i1I :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + iIIii )
def OoOOooOOoo ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  iIOoo000 ( url )
def iIOoo000 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  O00Oo0 ( url )
  if 21 - 21: O0OOOoOoo0 % I1111IIi % I1ii11iIi11i % o0o00Oo0O
def iI1I ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOooO0 , 8065 , III1iII1I1ii + 'classicmovies.png' )
def OoOoooOO00OO ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  oOO0oo ( url )
  if 76 - 76: Ii1I + Ii1IIIi1 % o0o00Oo0O * Ii . o0o00Oo0O . Ii
def IIIII1 ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOooO0 , 8065 , III1iII1I1ii + 'classictv.png' )
def i11iII1 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  if 'mp4' in url :
   O00Oo0 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 75 - 75: Ii1IIIi1 / Ii / iI11I1II1I1I
def i11iI1111ii1I ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oOooO0 , 8071 , III1iII1I1ii + 'streams.png' )
def OoOo0 ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  if '(Free Access)' in I1i1i1iii :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def iiIIii ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , I1i1i1iii , url in i1IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , iIIii , o0ooooO0o0O , '' )
  if 90 - 90: I1111IIi * ooOOOoO % IIiIiII11i / Ii1IIIi1
def o00oO0O000 ( ) :
 O0oO0 = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  oO0o0OoOOOO00o0 ( 'http://watchxxxfree.com/categories' )
 if oO0O0OO0O == 1 :
  O0ooo0 ( 'http://www.perfectgirls.net' )
 if oO0O0OO0O == 2 :
  o00O00oO ( 'http://www.xvideos.com/best' )
 if oO0O0OO0O == 3 :
  OO000O000OOO ( 'http://www.xvideos.com/best' )
 if oO0O0OO0O == 4 :
  o00O00oO ( 'http://www.xvideos.com/best' )
 if oO0O0OO0O == 5 :
  o00O00oO ( 'http://www.xvideos.com/verified/videos' )
 if oO0O0OO0O == 6 :
  I111Ii1I1I1iI ( 'http://www.xvideos.com/tags' )
 if oO0O0OO0O == 7 :
  III ( 'http://www.xvideos.com/porn' )
 if oO0O0OO0O == 8 :
  Oo0Oi1 ( )
  if 25 - 25: I11i % O0OOOoOoo0 . Ii
  if 4 - 4: ii
  if 78 - 78: IIiIiII11i
  if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
  if 21 - 21: OOooOOo - Ii - OOooOOo
  if 4 - 4: ooOOOoO . I1111IIi
  if 39 - 39: Ii1IIIi1 . I1ii11iIi11i - OOooOOo * Ii
  if 4 - 4: OOooOOo * o0o00Oo0O - ooOOOoO
  if 72 - 72: ooOOOoO + I11i1ii1 / oOo0O0Ooo . I1111IIi % oO0o / Ii
def I1III1I1IiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if 'ch' in url :
   I1IiI ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Jizbox.png' , III1iII1I1ii + 'Jizbox.png' , '' )
def ooooooo0oOo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oO0OOoo0OO )
 OooO00oO00o = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 for I1i1i1iii , url in OooO00oO00o :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Next.png' , '' , '' )
def IIII1iI1IiIiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   i1II1 ( url )
def OoOoOoo0oOOooo0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  O00Oo0 ( url )
def oO0o0OoOOOO00o0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , url , I1i1i1iii , OOOOOo in i1IIIII11I1IiI :
  if 'category' in url :
   I1IiI ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORorange]   ' + OOOOOo + '[/COLOR]' , url , 90006 , iIIii , III1iII1I1ii + 'Jizbox.png' , '' )
def IIII11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OooO00oO00o = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oO0OOoo0OO )
 for iIIii , url , I1i1i1iii in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , iIIii , '' , '' )
 for url in OooO00oO00o :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , III1iII1I1ii + 'Next.png' , '' , '' )
def oOoOOO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   i1II1 ( url )
def i1II1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  O00Oo0 ( url )
def O0ooo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , OOOOOo in i1IIIII11I1IiI :
  if 'category' in url :
   I1IiI ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORorange]' + OOOOOo + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def i1iI1Ii1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OoO = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OooO00oO00o = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , iIIii , '' , '' )
 for url in OooO00oO00o :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , OoO + '/' + url , 90003 , III1iII1I1ii + 'Next.png' , '' , '' )
def oooOO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  o00oO00O0 ( 'http://www.perfectgirls.net' + url )
def o00oO00O0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  i1I1IIIiiI ( 'http://' + url )
def III ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , OOOOOo in i1IIIII11I1IiI :
  I1IiI ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgreen] - No of Videos : [COLORorange]' + OOOOOo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def I111Ii1I1I1iI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OooO00oO00o = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in OooO00oO00o :
  I1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , OOOOOo in i1IIIII11I1IiI :
  I1IiI ( ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgreen] - No of Videos : [COLORorange]' + ( OOOOOo + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 16 - 16: ii1ii11IIIiiI / Ii + o0o00Oo0O . I1111IIi
def III11i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OooO00oO00o = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in OooO00oO00o :
  I1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , url , I1i1i1iii , O00o in i1IIIII11I1IiI :
  I1IiI ( I1i1i1iii + '--' + ( O00o ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( iIIii ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 54 - 54: iiiiiiii1 / I11i
  if 39 - 39: Ii1IIIi1 % o000O0o * Ii1I - o0o00Oo0O + oOo0O0Ooo + I11i
def o00O00oO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , url , I1i1i1iii , OoO00ooO , oooOo in i1IIIII11I1IiI :
  I1IiI ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgreen] - Porn Quality : [COLORorange]' + oooOo + ' - [COLORred]' + OoO00ooO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , iIIii , iIIii , oooOo + ' - ' + OoO00ooO )
 OOo0OOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in OOo0OOoO :
  I1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 66 - 66: iI11I1II1I1I * IIiIiII11i % I1ii11iIi11i % oOo0O0Ooo - ii1ii11IIIiiI
def OO000O000OOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I1IIIiI1I1ii1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OooO00oO00o = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in OooO00oO00o :
  I1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if '/c/' in url :
   I1IiI ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
   if 59 - 59: I1111IIi % o000O0o
   if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
def Oo0Oi1 ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I111i = ( oOOoooO ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 i1ii11 = I111i . lower ( )
 iIIi = 'http://www.xvideos.com/?k=' + i1ii11
 print iIIi + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0OOoo0OO = OoOooO ( iIIi )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , oOooO0 , I1i1i1iii , OoO00ooO , oooOo in i1IIIII11I1IiI :
  I1IiI ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgreen] - Porn Quality : [COLORorange]' + oooOo + ' - [COLORred]' + OoO00ooO + '[/COLOR]' , 'http://www.xvideos.com' + oOooO0 , 10108 , iIIii , iIIii , oooOo + ' - ' + OoO00ooO )
 OOo0OOoO = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in OOo0OOoO :
  I1IiI ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oOooO0 , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
if 19 - 19: OOooOOo * Ii1I * Ii1I / o0o00Oo0O / I11i1ii1 + Ii1I
if 48 - 48: ii . O0OOOoOoo0 + o0o00Oo0O
if 85 - 85: IIiIiII11i - ii1ii11IIIiiI
if 93 - 93: I1111IIi / Ii - o000O0o + oO0o / ooOoO0O00
if 62 - 62: Ii1I / ii * oOo0O0Ooo - ooOoO0O00
if 81 - 81: o000O0o / o0o00Oo0O * I11i1ii1 % OOooOOo / o0o00Oo0O
if 85 - 85: ii + ii
if 23 - 23: ooOoO0O00
if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / ooOOOoO . oO0o
if 74 - 74: I1ii11iIi11i - IIiIiII11i - I1111IIi
if 50 - 50: oOo0O0Ooo - o000O0o + o000O0o * ooOOOoO + o000O0o
if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
if 30 - 30: OOooOOo - Ii
if 94 - 94: OOooOOo % O0OOOoOoo0
if 39 - 39: OOooOOo + iiiiiiii1 % o0o00Oo0O
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
if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . ii1ii11IIIiiI - I1ii11iIi11i . Ii
if 47 - 47: I1ii11iIi11i % oO0o - I11i1ii1 - I1ii11iIi11i * o000O0o
if 72 - 72: I11i % I11i + O0OOOoOoo0 + Ii1I / I1ii11iIi11i
if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
if 64 - 64: I1111IIi
if 80 - 80: oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
if 89 - 89: o0o00Oo0O + I1111IIi * iiiiiiii1
if 30 - 30: OOooOOo
if 39 - 39: Ii1I + I11i + iiiiiiii1 + I1111IIi
if 48 - 48: iiiiiiii1 / I11i1ii1 . iI11I1II1I1I
def ooo0OOoo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 Iii1I1111ii = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   i1i1iII1 ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   i1i1iII1 ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in Iii1I1111ii :
  if 'http' in url :
   i1i1iII1 ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 52 - 52: oO0o
def I1O0 ( url ) :
 i1I1II1iIIi11 = xbmc . Player ( IiI1iII1II111 ( ) )
 import urlresolver
 try : i1I1II1iIIi11 . play ( url )
 except : pass
 if 94 - 94: oO0o - IIiIiII11i % iI11I1II1I1I
 if 92 - 92: I1ii11iIi11i
def i1iII ( ) :
 if 83 - 83: I11i
 if 26 - 26: o0o00Oo0O . IIiIiII11i * o0o00Oo0O + I11i1ii1 + OOooOOo * o0o00Oo0O
 if 46 - 46: I11i1ii1 - I11i1ii1 * Ii1I / O0OOOoOoo0 * Ii1IIIi1 / I11i
 if 67 - 67: Ii1IIIi1 - ii1ii11IIIiiI % O0OOOoOoo0 / IIiIiII11i + oOo0O0Ooo * I11i1ii1
 if 100 - 100: Ii1I
 if 81 - 81: Ii1I % O0OOOoOoo0
 if 22 - 22: ii + I11i . ooOOOoO + oOo0O0Ooo + ii . OOooOOo
 if 93 - 93: oOo0O0Ooo
 if 89 - 89: ii % Ii + iiiiiiii1
 if 12 - 12: OOooOOo * I11i1ii1
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 8091 , III1iII1I1ii + 'gofish.png' )
def ooOoooOoo0oO ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 8092 , iIIii )
 for url in next :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
def i1I1iii1I11II ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 IiI1I = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii in IiI1I :
  iIIii = iIIii
 for url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 8092 , iIIii )
 for url in next :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
  if 83 - 83: I1ii11iIi11i / I11i1ii1
def II1iiIiI1 ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 10 - 10: Ii % Ii1IIIi1 * O0OOOoOoo0 % I1ii11iIi11i
  if 51 - 51: oO0o % O0OOOoOoo0
  if 24 - 24: oOo0O0Ooo / iI11I1II1I1I / o0o00Oo0O . iI11I1II1I1I - oO0o . iI11I1II1I1I
  if 8 - 8: Ii1I % oO0o % o000O0o . Ii1I * Ii1I
oooooo0 = '{PQ},' ; iII1iii = '{SC},' ; o0O0o = '{XG},' ; OO0o0o = '{JP},' ; O0O0O00OoO0O = '{HW},' ; i1II11III = '{RT},'
def Oo0oooO0oO ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 Ii11 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 oOooO0 = 'http://onlinemovies.tube/?s=' + ( oOOoooO ) . replace ( ' ' , '+' )
 OoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 II1i111 = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 i1iiiIii11 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 OOoOOO000O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oOo0II1i11I1 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iiIiIiII = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOOoooO
 i1I1 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 95 - 95: ooOOOoO + I11i - Ii % oO0o / o000O0o
 I1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 II11iIII1i1I = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 80 - 80: iiiiiiii1 * o000O0o * ooOoO0O00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oOooO0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( OoO )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1i111 )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( i1iiiIii11 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 i1iIIi1I1I11 = O0o0O00Oo0o0 ( OOoOOO000O0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iii1III1i = O0o0O00Oo0o0 ( iiIiIiII )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 iiiIi = O0o0O00Oo0o0 ( i1I1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 II1Iii = O0o0O00Oo0o0 ( iIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 32 - 32: oOo0O0Ooo + Ii - iiiiiiii1 / IIiIiII11i
 if 27 - 27: I11i1ii1 . I1ii11iIi11i + I11i1ii1 + O0OOOoOoo0
 ooO0o = O0o0O00Oo0o0 ( I1i )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 ii1iI1iI1 = O0o0O00Oo0o0 ( II11iIII1i1I )
 if 28 - 28: oO0o - I11i1ii1 - o000O0o % o000O0o / o0o00Oo0O
 if 99 - 99: IIiIiII11i - iI11I1II1I1I
 if 24 - 24: oOo0O0Ooo - ooOoO0O00 - o0o00Oo0O % iiiiiiii1 - iI11I1II1I1I . ooOOOoO
 if 26 - 26: oO0o % ooOoO0O00 * o0o00Oo0O . iiiiiiii1
 if 31 - 31: o0o00Oo0O - I1111IIi * Ii * ooOoO0O00
 if 78 - 78: I11i1ii1 * OOooOOo . ii1ii11IIIiiI . OOooOOo % iI11I1II1I1I
 if 67 - 67: ii1ii11IIIiiI . I1ii11iIi11i
 if 39 - 39: ooOOOoO * iiiiiiii1
 if 63 - 63: I11i1ii1 % oOo0O0Ooo . Ii1IIIi1 - I11i1ii1 / I1ii11iIi11i % oOo0O0Ooo
 if 39 - 39: I11i . ooOoO0O00 % o000O0o / ooOOOoO % o0o00Oo0O
 if 100 - 100: iiiiiiii1 - OOooOOo
 if 78 - 78: ii - OOooOOo . Ii
 if 36 - 36: o000O0o * O0OOOoOoo0 + I1111IIi * O0OOOoOoo0 . Ii1I - iI11I1II1I1I
 if II1Iii != 'Failed' :
  OoOoi1i = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( II1Iii )
  for oOooO0 , I1i1i1iii in OoOoi1i :
   IIIiiiI = O0o0O00Oo0o0 ( oOooO0 )
   OoO00oo00 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIIiiiI )
   for Oo0Oo0O , iiiI1i11Ii in OoO00oo00 :
    iiiI1i11Ii = ( iiiI1i11Ii . replace ( '.' , ' ' ) )
    if i1ii11 in iiiI1i11Ii . lower ( ) :
     if '.mkv' in Oo0Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , oOooO0 + Oo0Oo0O , 222 , '' , '' , '' )
     elif '.mp4' in Oo0Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , oOooO0 + Oo0Oo0O , 222 , '' , '' , '' )
     elif '.avi' in Oo0Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , oOooO0 + Oo0Oo0O , 222 , '' , '' , '' )
     elif '.wav' in Oo0Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , oOooO0 + Oo0Oo0O , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , oOooO0 + Oo0Oo0O , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 14 - 14: ooOOOoO * o000O0o + Ii
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for oOooO0 , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in i1I :
   if oOOoooO in I1i1i1iii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORred] source Technica[/COLOR]' ) , oOooO0 , 222 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 84 - 84: O0OOOoOoo0 / IIiIiII11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 86 - 86: oOo0O0Ooo
 if ii1ii1ii != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for oo0o0oOo , I1i1i1iii in Iii1I1111ii :
   if oOOoooO in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( II1i111 + oo0o0oOo ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  ii1iii1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for oOooO0 , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in ii1iii1i :
   if oOOoooO in I1i1i1iii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORred] source RaizTv[/COLOR]' ) , oOooO0 , 222 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 97 - 97: IIiIiII11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if i1iIIi1I1I11 != 'Failed' :
  IIo00ooo = [ ]
  OOOOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIi1I1I11 )
  for oOooO0 , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in OOOOO :
   if oOOoooO in I1i1i1iii . lower ( ) :
    if I1i1i1iii in IIo00ooo :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oOooO0 , 1016 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
     IIo00ooo . append ( I1i1i1iii )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1III1i != 'Failed' :
  Ii1IiIiIi1IiI = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( iii1III1i )
  for oOooO0 , iIIii , I1i1i1iii in Ii1IiIiIi1IiI :
   if oOOoooO in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oOooO0 , 7067 , iIIii )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 38 - 38: oOo0O0Ooo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 42 - 42: I11i
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
 if ooO0o != 'Failed' :
  oOooo0Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO0o )
  for oOooO0 , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in oOooo0Oo :
   if oOOoooO in I1i1i1iii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source APPRENTICE[/COLOR]' ) , oOooO0 , 222 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 87 - 87: Ii1IIIi1 + Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: ooOoO0O00 - I1ii11iIi11i
    if 87 - 87: OOooOOo - oO0o * oO0o / ii1ii11IIIiiI . ooOOOoO * I11i
    if 21 - 21: IIiIiII11i
    if 29 - 29: OOooOOo % ii1ii11IIIiiI
    if 7 - 7: ooOoO0O00 / I1111IIi / O0OOOoOoo0
    if 97 - 97: oO0o + iI11I1II1I1I
    if 79 - 79: I11i1ii1 + o000O0o - IIiIiII11i . I1ii11iIi11i
    if 26 - 26: I1111IIi
    if 52 - 52: o0o00Oo0O + I11i1ii1
    if 11 - 11: ooOoO0O00 / iiiiiiii1 * Ii1I * iiiiiiii1 * I11i1ii1 - Ii
 oOOO0O0Ooo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 96 - 96: Ii1I % Ii1I
 for ii1i in oOOO0O0Ooo :
  IIi = O0Oo000ooO00 + ii1i + I1IIIii
  II1Iii = O0o0O00Oo0o0 ( IIi )
  if II1Iii != 'Failed' :
   OoOoi1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( II1Iii )
   for oOooO0 , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in OoOoi1i :
    if oOOoooO in I1i1i1iii . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgold] - Source Pandoras[/COLOR]' , oOooO0 , 222 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 1 - 1: oOo0O0Ooo . ii1ii11IIIiiI
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 26 - 26: o000O0o - I11i1ii1 % I1ii11iIi11i - o000O0o + I1111IIi
 oOOO0O0Ooo = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 33 - 33: ii1ii11IIIiiI + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * I1111IIi
 if 21 - 21: o0o00Oo0O * I11i1ii1 % oO0o
 for ii1i in oOOO0O0Ooo :
  IIi = Ii11 + ii1i
  oo0O0o00 = O0o0O00Oo0o0 ( IIi )
  if oo0O0o00 != 'Failed' :
   oOoO0o = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0O0o00 )
   for oo0o0oOo , I1i1i1iii in oOoO0o :
    if oOOoooO in I1i1i1iii . lower ( ) :
     i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( Ii11 + ii1i + oo0o0oOo ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 14 - 14: o0o00Oo0O / iiiiiiii1 / I11i1ii1 + I1111IIi - I1111IIi
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: o0o00Oo0O - Ii1I / iiiiiiii1 % OOooOOo / ii / ii1ii11IIIiiI
def I1ii1 ( ) :
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
 if 45 - 45: oO0o * oOo0O0Ooo
 if 61 - 61: O0OOOoOoo0 % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
 if 74 - 74: Ii1I * o000O0o + O0OOOoOoo0 % o0o00Oo0O
 if 18 - 18: ooOoO0O00 % I1111IIi . o0o00Oo0O - o0o00Oo0O - o0o00Oo0O - IIiIiII11i
 if 55 - 55: OOooOOo . iI11I1II1I1I * Ii1IIIi1 % iI11I1II1I1I . oO0o
 if 43 - 43: ii1ii11IIIiiI . Ii1IIIi1 + oOo0O0Ooo * Ii
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 if 2 - 2: Ii1IIIi1
 if 3 - 3: oOo0O0Ooo . O0OOOoOoo0 % o0o00Oo0O - I11i1ii1 / o0o00Oo0O
 Oo0Oo0O = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( oOOoooO ) . replace ( ' ' , '+' )
 OoO = 'http://onlinemovies.tube/?s=' + ( oOOoooO ) . replace ( ' ' , '+' )
 II1i111 = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 i1iiiIii11 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oOo0II1i11I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 79 - 79: ii1ii11IIIiiI + o000O0o % I11i1ii1 % oOo0O0Ooo
 i1I1 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 iIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 I11oOOooo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 68 - 68: IIiIiII11i - ii / iI11I1II1I1I - I11i % IIiIiII11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 53 - 53: O0OOOoOoo0 . o000O0o / I1ii11iIi11i . oO0o . Ii
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 60 - 60: IIiIiII11i
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 Ii1I1 = O0o0O00Oo0o0 ( Oo0Oo0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( OoO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1i111 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( i1iiiIii11 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 oo0O0o00 = O0o0O00Oo0o0 ( oOo0II1i11I1 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 57 - 57: IIiIiII11i . ooOoO0O00
 if 33 - 33: O0OOOoOoo0 + I1ii11iIi11i % ooOOOoO . o000O0o
 iiiIi = O0o0O00Oo0o0 ( i1I1 )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 II1Iii = O0o0O00Oo0o0 ( iIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 i11IiIIi11I = O0o0O00Oo0o0 ( I11oOOooo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 6 - 6: I1111IIi + Ii1I
 if II1Iii != 'Failed' :
  OoOoi1i = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( II1Iii )
  for oOooO0 , I1i1i1iii in OoOoi1i :
   IIIiiiI = O0o0O00Oo0o0 ( oOooO0 )
   OoO00oo00 = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( IIIiiiI )
   for Oo0Oo0O , iiiI1i11Ii in OoO00oo00 :
    if i1ii11 in iiiI1i11Ii . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + iiiI1i11Ii + '-[COLORgold] source ' + I1i1i1iii + '[/COLOR]' ) , oOooO0 + Oo0Oo0O , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 62 - 62: o000O0o . iiiiiiii1 - ii * IIiIiII11i . Ii
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if iiiIi != 'Failed' :
  iIiIi1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiiIi )
  for oOooO0 , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in iIiIi1ii :
   if i1ii11 in I1i1i1iii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] source HeroVision[/COLOR]' ) , oOooO0 , 1016 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 13 - 13: iI11I1II1I1I * I11i - Ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 63 - 63: ii * iiiiiiii1
    if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . o000O0o % IIiIiII11i
    if 18 - 18: ooOOOoO % ii + oO0o / ooOOOoO
    if 37 - 37: ooOoO0O00 - ii1ii11IIIiiI / I1111IIi . IIiIiII11i % I11i1ii1
    if 39 - 39: ii1ii11IIIiiI % Ii * oO0o
    if 23 - 23: Ii1IIIi1 + I11i1ii1 / Ii * I1ii11iIi11i . oO0o
    if 28 - 28: O0OOOoOoo0 - I11i
    if 92 - 92: I1ii11iIi11i % I11i - I11i1ii1 / I11i1ii1 / OOooOOo
    if 84 - 84: Ii1IIIi1
    if 4 - 4: I1111IIi . iiiiiiii1 / ii1ii11IIIiiI / O0OOOoOoo0 + IIiIiII11i
    if 32 - 32: ooOoO0O00 + iI11I1II1I1I . Ii1I . ooOOOoO - ii1ii11IIIiiI
 if i11IiIIi11I != 'Failed' :
  o0O0O0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i11IiIIi11I )
  for oOooO0 , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in o0O0O0 :
   if i1ii11 in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORred] RaizTv[/COLOR]' , oOooO0 , 1016 , IiI111ii1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 55 - 55: Ii1I / ii - oO0o / oOo0O0Ooo
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  oOO0o0oo0 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for oOooO0 , iIIii , I1i1i1iii , oOo000O in i1I :
   if i1ii11 in I1i1i1iii . lower ( ) :
    if 'season' in oOo000O :
     Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOooO0 , 90054 , iIIii , iIIii , '' )
    if 'episodes' in oOo000O :
     Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOooO0 , 90044 , iIIii , iIIii , '' )
  for oOooO0 in oOO0o0oo0 :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oOooO0 , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 23 - 23: ooOOOoO * iiiiiiii1 * I11i - oOo0O0Ooo % OOooOOo + I11i
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if Ii1I1 != 'Failed' :
  o0OO0O0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( Ii1I1 )
  for oOooO0 , I1i1i1iii , iIIii in o0OO0O0Oo :
   if i1ii11 in I1i1i1iii . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1i1i1iii ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oOooO0 , 8022 , iIIii , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 41 - 41: I1111IIi * ii . I11i1ii1 % Ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 11 - 11: iI11I1II1I1I . iiiiiiii1 - I1ii11iIi11i / ooOOOoO + IIiIiII11i
    if 29 - 29: ooOOOoO . Ii + ooOoO0O00 - ii1ii11IIIiiI + o0o00Oo0O . oOo0O0Ooo
    if 8 - 8: I11i
    if 78 - 78: ooOoO0O00 - I1ii11iIi11i
    if 48 - 48: ii1ii11IIIiiI - ii + iiiiiiii1 % I11i - OOooOOo . oOo0O0Ooo
    if 42 - 42: iiiiiiii1
    if 70 - 70: I11i / ooOOOoO + o000O0o % oOo0O0Ooo % I1ii11iIi11i + oO0o
    if 80 - 80: Ii1IIIi1
    if 12 - 12: ii1ii11IIIiiI
 if ii1ii1ii != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for I1i1i1iii in Iii1I1111ii :
   if i1ii11 in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( II1i111 + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 2 - 2: ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  ii1iii1i = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for I1i1i1iii in ii1iii1i :
   if i1ii11 in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( i1iiiIii11 + I1i1i1iii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0O0o00 != 'Failed' :
  oOoO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0O0o00 )
  for oOooO0 , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in oOoO0o :
   if i1ii11 in I1i1i1iii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1i1i1iii + '-[COLORgold] Source Scooby[/COLOR]' ) , oOooO0 , 1016 , IiI111ii1ii , OOOoO000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 46 - 46: o0o00Oo0O % ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 22 - 22: O0OOOoOoo0 + ii - OOooOOo - oO0o * iiiiiiii1 - o000O0o
 I1IiIii11I = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for ii1i in I1IiIii11I :
  IIi = O0Oo000ooO00 + ii1i + I1IIIii
  ooO0o = O0o0O00Oo0o0 ( IIi )
  if ooO0o != 'Failed' :
   oOooo0Oo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( ooO0o )
   for I1i1i1iii , oo00O00oO000o , oOooO0 , iIIii , o0ooooO0o0O , O0OOO0OOooo00 in oOooo0Oo :
    if i1ii11 in I1i1i1iii . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgold] - Source Pandoras[/COLOR]' , oOooO0 , O0OOO0OOooo00 , iIIii , o0ooooO0o0O , oo00O00oO000o )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 99 - 99: I11i1ii1 / oOo0O0Ooo . ii1ii11IIIiiI - ii1ii11IIIiiI * oOo0O0Ooo
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 24 - 24: ooOOOoO * oO0o - o000O0o / iI11I1II1I1I - I1ii11iIi11i . Ii1IIIi1
     if 2 - 2: I11i1ii1 - o0o00Oo0O - Ii1I / ooOOOoO * OOooOOo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def III1II ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOooO0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( oOOoooO ) . replace ( ' ' , '+' )
 if 81 - 81: O0OOOoOoo0 - ii1ii11IIIiiI - Ii1IIIi1 % I1111IIi % I11i . iI11I1II1I1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oOooO0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 79 - 79: Ii1I - Ii1I . ii1ii11IIIiiI / I1111IIi
 if oO0OOoo0OO != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oOooO0 , I1i1i1iii in i1I :
   if oOOoooO in I1i1i1iii . lower ( ) :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oOooO0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 57 - 57: I11i1ii1 * iI11I1II1I1I * O0OOOoOoo0 * ii1ii11IIIiiI / ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
IiIiIiIII1Iii = '{ZH},' ; OOoOOOOOo0ooOOO0 = '{IX},' ; Oo00O0O = '{LM},'
if 15 - 15: Ii1I . oOo0O0Ooo - iiiiiiii1 - ooOoO0O00
def O00OO0o0 ( url ) :
 oO0o00o0o0OO0O0 = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( oO0o00o0o0OO0O0 )
 for url , O0Oo0o000oO , O0o0oo0oOO0oO , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( O0Oo0o000oO ) . replace ( 'Sezon' , ' Season ' ) + ( O0o0oo0oOO0oO ) . replace ( 'Bölüm' , ' Episode ' ) + I1i1i1iii , url , 8063 , '' )
  if 12 - 12: ooOoO0O00 + ii . O0OOOoOoo0 - Ii % I1ii11iIi11i * o0o00Oo0O
  if 65 - 65: o000O0o
  if 8 - 8: oO0o . o000O0o / Ii1I / oO0o + iI11I1II1I1I
  if 73 - 73: Ii / OOooOOo
def i1Ii1IIIi111111 ( url ) :
 oO0o00o0o0OO0O0 = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( oO0o00o0o0OO0O0 )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( I1i1i1iii , url , 222 , '' )
  if 57 - 57: ii1ii11IIIiiI . iiiiiiii1 . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
  if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
  if 93 - 93: I11i1ii1 / Ii1IIIi1 * o0o00Oo0O
  if 17 - 17: oO0o / I11i1ii1 % oOo0O0Ooo
def IIiI1IiI1iIi1 ( ) :
 if 30 - 30: O0OOOoOoo0
 oO0o00o0o0OO0O0 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oO0o00o0o0OO0O0 )
 for oOooO0 , iIIii , I1i1i1iii , O0o0oo0oOO0oO in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii + '  -  ' + ( O0o0oo0oOO0oO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOooO0 , 8063 , iIIii )
  if 44 - 44: OOooOOo . Ii1IIIi1
def o000OO0o ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 8002 , iIIii )
def O0O0ooO0oO0O ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIIIiIi )
 for iIIii , time , url , I1i1i1iii , i1i1iIiI in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '%s %s' % ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , time ) , url , 1015 , iIIii , i1i1iIiI )
  if 74 - 74: oO0o / I1111IIi % I1111IIi - O0OOOoOoo0
def Iii11 ( ) :
 if 3 - 3: ooOOOoO - Ii1IIIi1 + OOooOOo * oO0o % iiiiiiii1
 Iiiiii111i1ii ( 'Coronation Street' , '' , 8001 , '' )
 Iiiiii111i1ii ( 'Eastenders' , '' , 8002 , '' )
 Iiiiii111i1ii ( 'Emmerdale' , '' , 8003 , '' )
 Iiiiii111i1ii ( 'Hollyoaks' , '' , 8004 , '' )
 Iiiiii111i1ii ( 'Im a Celebrity' , '' , 8005 , '' )
 if 24 - 24: iI11I1II1I1I % I1ii11iIi11i % Ii
 if 55 - 55: O0OOOoOoo0
 if 19 - 19: ii / Ii1IIIi1 * Ii - oOo0O0Ooo
 if 99 - 99: oO0o % o0o00Oo0O . iiiiiiii1 - Ii1I . I1ii11iIi11i / OOooOOo
def o0oOOoOoo ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'Holly' in I1i1i1iii :
   iIIii = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oOooO0 :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , iIIii )
   else :
    pass
    if 90 - 90: oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 4 - 4: Ii1IIIi1 % I11i1ii1 - Ii1IIIi1 - I11i
def iI1IIIiIII11 ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'East' in I1i1i1iii :
   iIIii = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oOooO0 :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , iIIii )
   else :
    pass
    if 70 - 70: ii + oO0o * I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 20 - 20: Ii - IIiIiII11i - I11i1ii1 % o000O0o . I11i1ii1
def IiI1I1 ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'Emmer' in I1i1i1iii :
   iIIii = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oOooO0 :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , iIIii )
   else :
    pass
    if 16 - 16: Ii1I / ooOOOoO + I11i % Ii % Ii1IIIi1 - ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 37 - 37: Ii1IIIi1 * ii1ii11IIIiiI * ooOOOoO + OOooOOo / Ii
def oo00ooOOOo0O ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'Coro' in I1i1i1iii :
   iIIii = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oOooO0 :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , iIIii )
   else :
    pass
    if 19 - 19: Ii1IIIi1 * ooOOOoO
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: ooOoO0O00 % I11i * Ii1I * oO0o . IIiIiII11i
def O000 ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'Celeb' in I1i1i1iii :
   iIIii = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oOooO0 :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , iIIii )
   else :
    pass
    if 18 - 18: I11i1ii1 + iiiiiiii1 / Ii1IIIi1 / o000O0o + iI11I1II1I1I % I1111IIi
def oOoOO00Ooo ( name , url ) :
 IiiIi1II1iI = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IiiIi1II1iI :
  i1Iii1ii = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIIIiIi = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( iIIIiIi ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIIIiIi = open_url ( url )
  iii1I = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( iIIIiIi ) [ - 1 ]
  i1Iii1ii = iii1I . replace ( '\\/' , '/' )
 OOO00OO0oOo = xbmcgui . ListItem ( name , '' , '' )
 OOO00OO0oOo . setPath ( i1Iii1ii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOO00OO0oOo )
 if 89 - 89: O0OOOoOoo0 + ooOoO0O00 - I1111IIi + I11i1ii1 . IIiIiII11i
 if 85 - 85: iI11I1II1I1I - ii1ii11IIIiiI * I1ii11iIi11i . o000O0o + iiiiiiii1
def Ii1iIii ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIIIiIi )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oOooO0 , 7071 , III1iII1I1ii + 'popcorn.png' )
 for oOooO0 , I1i1i1iii in i1I :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oOooO0 , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . O0OOOoOoo0 / O0OOOoOoo0
def i1I1I ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'Movies' in I1i1i1iii :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.snagfilms.com' + ( oOooO0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def iIIIOOO00o0O ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIIiIi )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIIIiIi )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iIIii )
 for url in i1I :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 18 - 18: I11i1ii1
  if 92 - 92: oO0o % iI11I1II1I1I / I1111IIi * O0OOOoOoo0 . ooOoO0O00 + o000O0o
def Iii1iiIi1II ( url ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , url , iIIii in i1IIIII11I1IiI :
  if '{{' in I1i1i1iii :
   pass
  else :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , iIIii )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
I11OooOooOOooo0 = '{UJ},' ; o0OO00oOO = '{WE},' ; IiiII1iIi = '{WP},' ; OoO00oooo0o = '{PP},'
def iiiiii ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , url , iIIii in i1IIIII11I1IiI :
  if '{{' in I1i1i1iii :
   pass
  else :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , iIIii )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooII1 ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  o0OOO ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0OOO ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 38 - 38: oOo0O0Ooo * I11i - Ii1IIIi1 % I1111IIi + ooOOOoO - I1ii11iIi11i
 if 55 - 55: iI11I1II1I1I + OOooOOo
 if 7 - 7: ii1ii11IIIiiI / iiiiiiii1 % I11i1ii1 - iiiiiiii1 * oOo0O0Ooo
def II11111I ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIIiIi )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if '(cooltvseries.com)' in I1i1i1iii :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , I1i1i1iii in i1I :
  if '(cooltvseries.com)' in I1i1i1iii :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def OOoo ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  i1I1IIIiiI ( ( url ) . replace ( ' ' , '%20' ) )
OO0ooOO00o0 = '{XX},' ; Iii11I1i = '{UD},' ; IIiiiii1IIIi = '{YT},' ; III1i = '{JS},' ; Ii1I11Ii1iI = '{PF},'
if 61 - 61: I11i * Ii1I - ooOoO0O00 + ooOOOoO % I11i + ii
def o0Oooo0O00Ooo ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oOooO0 ) ) , 222 , iIIii )
  if 84 - 84: ooOoO0O00
def IiIiI111IIII1 ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIIIiIi )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIIIiIi )
 for iIIii , url , I1i1i1iii in i1IIIII11I1IiI :
  if 'youtu' in url :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + iIIii )
 for url in next :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 73 - 73: Ii * Ii1I . ooOOOoO % oOo0O0Ooo - oOo0O0Ooo . OOooOOo
def OOooiIi1 ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 15 - 15: ii
def i11iiI1iiIii ( url ) :
 iIIIiIi = OoOooO
 i1IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 222 , iIIii )
  if 13 - 13: ooOOOoO + iiiiiiii1 - iiiiiiii1 % o000O0o / ooOOOoO
  if 4 - 4: oOo0O0Ooo + Ii1IIIi1 - I1111IIi + O0OOOoOoo0
  if 78 - 78: ii1ii11IIIiiI
  if 29 - 29: IIiIiII11i
  if 79 - 79: iI11I1II1I1I - Ii + I11i1ii1 - IIiIiII11i . iI11I1II1I1I
def OO000o0O0o ( ) :
 if 67 - 67: Ii1IIIi1 . Ii + I11i1ii1 . iI11I1II1I1I
 Iiiiii111i1ii ( 'All Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'Entertainment' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'Movies' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'Music' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'News' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'Sports' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'Documentary' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'Kids' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'Food' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'Religious' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'USA Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 Iiiiii111i1ii ( 'Other' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 if 28 - 28: oOo0O0Ooo + oOo0O0Ooo + iiiiiiii1
 if 22 - 22: iiiiiiii1
def O0oooOoO ( Cat_Name ) :
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / Ii1IIIi1 / iiiiiiii1
 i11Ii1iiiI1I = False
 II1iiI11I = '0'
 if Cat_Name == 'All Channels' : i11Ii1iiiI1I = True
 if Cat_Name == 'Entertainment' : II1iiI11I = '1'
 if Cat_Name == 'Movies' : II1iiI11I = '2'
 if Cat_Name == 'Music' : II1iiI11I = '3'
 if Cat_Name == 'News' : II1iiI11I = '4'
 if Cat_Name == 'Sports' : II1iiI11I = '5'
 if Cat_Name == 'Documentary' : II1iiI11I = '6'
 if Cat_Name == 'Kids' : II1iiI11I = '7'
 if Cat_Name == 'Food' : II1iiI11I = '8'
 if Cat_Name == 'Religious' : II1iiI11I = '9'
 if Cat_Name == 'USA Channels' : II1iiI11I = '10'
 if Cat_Name == 'Other' : II1iiI11I = '11'
 if 43 - 43: OOooOOo / iI11I1II1I1I
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIIiIi )
 print 'Len Match: >>>' + str ( len ( i1IIIII11I1IiI ) )
 for I1i1i1iii , iIIii , ooO00Oo in i1IIIII11I1IiI :
  IIiI1iiIII1 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iIIii ) . replace ( '\\' , '' )
  if ooO00Oo == II1iiI11I :
   Iiiiii111i1ii ( I1i1i1iii , '' , 7022 , IIiI1iiIII1 )
  elif i11Ii1iiiI1I == True :
   Iiiiii111i1ii ( I1i1i1iii , '' , 7022 , IIiI1iiIII1 )
  else : pass
  if 68 - 68: Ii . I11i1ii1 % ooOOOoO
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 47 - 47: OOooOOo . ooOoO0O00
def iiooo0o0oO ( Search_Name ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIIiIi )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIIiIi )
 for iIIii , oOooO0 , OoO , II1i111 in i1IIIII11I1IiI :
  IIiI1iiIII1 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( iIIii ) . replace ( '\\' , '' )
  i1i1iII1 ( Search_Name + ': Link 1' , ( oOooO0 ) . replace ( '\\' , '' ) , 222 , IIiI1iiIII1 )
  i1i1iII1 ( Search_Name + ': Link 2' , ( OoO ) . replace ( '\\' , '' ) , 222 , IIiI1iiIII1 )
  i1i1iII1 ( Search_Name + ': Link 3' , ( II1i111 ) . replace ( '\\' , '' ) , 222 , IIiI1iiIII1 )
  if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
def i1iI11IiII ( ) :
 iIIIiIi = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIIIiIi )
 for I1i1i1iii , oOooO0 in i1IIIII11I1IiI :
  i1i1iII1 ( I1i1i1iii , ( oOooO0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def oO00Oo0OO ( ) :
 iIIIiIi = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIIIiIi )
 for I1i1i1iii , oOooO0 in i1IIIII11I1IiI :
  i1i1iII1 ( I1i1i1iii , ( oOooO0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def i11iIIiii ( ) :
 iIIIiIi = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIIIiIi )
 for I1i1i1iii , oOooO0 in i1IIIII11I1IiI :
  i1i1iII1 ( I1i1i1iii , ( oOooO0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 66 - 66: iiiiiiii1 - ooOOOoO . I1111IIi % o000O0o
def i1i1 ( url ) :
 url
 oooO = xbmcgui . ListItem ( I1i1i1iii , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oooO )
 return
 if 5 - 5: O0OOOoOoo0 - O0OOOoOoo0 / iiiiiiii1 % I1ii11iIi11i
 if 61 - 61: o000O0o - Ii1I / O0OOOoOoo0 % Ii1I + oO0o / I1ii11iIi11i
def iiIii ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIIIiIi )
 for url , oo00O00oO000o , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + iIIii , '' , ( oo00O00oO000o ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  Iiiiii111i1ii ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 18 - 18: ooOOOoO / I11i1ii1
def O00Oo00o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , oo00O00oO000o , iIIii in i1IIIII11I1IiI :
  OOiIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + iIIii , '' , oo00O00oO000o )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 IIIIII1iI1II = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for IiII1Iiii in IIIIII1iI1II :
  I11I11 = ( IiII1Iiii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiOOooooO0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + iIIii , '' , I11I11 )
  if 16 - 16: O0OOOoOoo0 . o0o00Oo0O - iiiiiiii1 * iiiiiiii1
def o0OO00Ooo0 ( INFO ) :
 OOoO ( 'info for workout' , INFO )
 if 97 - 97: o000O0o - iiiiiiii1 * O0OOOoOoo0 - I11i1ii1 * iiiiiiii1
 if 90 - 90: ii1ii11IIIiiI . OOooOOo
 if 89 - 89: iiiiiiii1 - oO0o - I11i
def i1ii ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( I1i1i1iii ) . replace ( 'SlyNet' , '' ) , url , 9031 , III1iII1I1ii + 'Sport.png' )
def i11iiIii11I1 ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , url , 9032 , III1iII1I1ii + 'icon.png' )
def oo0O000OooO0 ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  if '=' in I1i1i1iii :
   pass
  else :
   i1i1iII1 ( ( I1i1i1iii ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , III1iII1I1ii + 'icon.png' )
def IIIi1Iii11I ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  if '=' in I1i1i1iii :
   pass
  else :
   i1i1iII1 ( I1i1i1iii , url , 222 , III1iII1I1ii + 'icon.png' )
   if 34 - 34: iiiiiiii1 . I1111IIi - Ii1IIIi1
   if 65 - 65: I1111IIi - iiiiiiii1
   if 71 - 71: I1ii11iIi11i - ooOoO0O00
def IIiI ( url ) :
 i1i1iII1 ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 i1i1iII1 ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 Iiiiii111i1ii ( '[COLOR' + II + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , III1iII1I1ii + 'bamf.png' )
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   pass
  else :
   i1i1iII1 ( ( I1i1i1iii ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI11IIiII1iII ( url ) :
 i1i1iII1 ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 i1i1iII1 ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 Iiiiii111i1ii ( '[COLOR' + II + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , III1iII1I1ii + 'bamf.png' )
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   i1i1iII1 ( ( I1i1i1iii ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 51 - 51: iI11I1II1I1I * OOooOOo / ii1ii11IIIiiI * oO0o
 if 58 - 58: o0o00Oo0O - ooOoO0O00 / O0OOOoOoo0
 if 59 - 59: I1ii11iIi11i % Ii1I % I11i1ii1 % ooOOOoO * iI11I1II1I1I
def II1iiIii1ii1 ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 i1IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'Daily' in I1i1i1iii :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 9008 , Oo00OOOOO )
def iiiiiiI ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def iI111iiI1II ( url ) :
 i1i1iII1 ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 i1i1iII1 ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 i1i1iII1 ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  i1i1iII1 ( ( I1i1i1iii ) . replace ( '_' , ' ' ) , url , 222 , Oo00OOOOO )
  if 96 - 96: OOooOOo * o0o00Oo0O - IIiIiII11i . I11i1ii1 - ii1ii11IIIiiI
def OO0OOO0o0OOO0 ( ) :
 iIIIiIi = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if '.m3u' in oOooO0 :
   Iiiiii111i1ii ( ( I1i1i1iii ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oOooO0 ) , 9011 , III1iII1I1ii + 'disclose.png' )
def iiIiiIiI11i1 ( url ) :
 iIIIiIi = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  i1i1iII1 ( ( I1i1i1iii ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 48 - 48: I1ii11iIi11i % I1ii11iIi11i % o0o00Oo0O
def iiI11i1II ( ) :
 iIIIiIi = OoOooO ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  if 'category' in oOooO0 :
   Iiiiii111i1ii ( I1i1i1iii , 'http://www.disclose.tv/' + oOooO0 , 7010 , III1iII1I1ii + 'disclose.png' )
   if 8 - 8: O0OOOoOoo0 . ii1ii11IIIiiI - ooOoO0O00 % oO0o / ooOOOoO
   if 13 - 13: I1ii11iIi11i / OOooOOo . Ii1I . Ii1IIIi1
def iIiiII11 ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIIIiIi )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIIiIi )
 for url , I1i1i1iii , iIIii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , 'http://www.disclose.tv/' + url , 7011 , iIIii )
 for url in next :
  Iiiiii111i1ii ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 75 - 75: OOooOOo + ii1ii11IIIiiI . Ii / ii1ii11IIIiiI
  if 32 - 32: ii1ii11IIIiiI + I1111IIi + Ii1I
def oo00o ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iIIIiIi )
 Iii1I1111ii = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   i1i1iII1 ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , I1i1i1iii in i1I :
  i1i1iII1 ( I1i1i1iii , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in Iii1I1111ii :
  i1i1iII1 ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 14 - 14: ii1ii11IIIiiI + ii1ii11IIIiiI * ii * ooOOOoO + I1ii11iIi11i . oOo0O0Ooo
  if 61 - 61: Ii1IIIi1 . Ii1IIIi1
def ii11 ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 43 - 43: OOooOOo % ii1ii11IIIiiI + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
def OOOOo00oOOO00 ( name , url , img ) :
 oO0OOoo0OO = OoOooO ( url )
 II1I = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oO0Ooo0o00o = len ( II1I )
 if 53 - 53: OOooOOo % ooOoO0O00
 if 35 - 35: ii1ii11IIIiiI + Ii1I . o000O0o * I1ii11iIi11i
 if oO0Ooo0o00o == 1 :
  for IiI1Io0o0OoOOOoo in II1I :
   IiI1Io0o0OoOOOoo = IiI1Io0o0OoOOOoo . replace ( 'player' , 'watch' )
   oo0O0O000O0oO = IiI1Io0o0OoOOOoo + '&fv=&sou='
   OoO0 = OoOooO ( oo0O0O000O0oO )
   iIIiiI1Ii1II = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( OoO0 )
   for oOO in iIIiiI1Ii1II :
    iIiI1 = False
    Resolve ( oOO )
    if 23 - 23: iI11I1II1I1I - ooOoO0O00 - I1111IIi * I1111IIi . I1111IIi
 elif oO0Ooo0o00o > 1 :
  if 79 - 79: ooOOOoO - OOooOOo + iiiiiiii1 / oOo0O0Ooo * ii
  for IiI1Io0o0OoOOOoo in II1I :
   IiI1iIIiIi1Ii = OoOooO ( IiI1Io0o0OoOOOoo )
   O0oOoOOO000 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( IiI1iIIiIi1Ii )
   oOo00o0oO = O0oOoOOO000
   oOo00o0oO = ( str ( oOo00o0oO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + oOo00o0oO
   i1i1iII1 ( 'DOUBLE LINK' , oOo00o0oO , 424 , '' )
   if 14 - 14: oO0o / I1ii11iIi11i . Ii
   for url in O0oOoOOO000 :
    Iiiiii111i1ii ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     OoO = Google . resolve ( url )
    except :
     pass
    try :
     I1Iii11II = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( OoO ) )
     for ii11III1 , OOOoO0oo0oo0o in I1Iii11II :
      if 70 - 70: iI11I1II1I1I + I11i * o000O0o
      HD_URLS . append ( ii11III1 )
      SD_URLS . append ( OOOoO0oo0oo0o )
    except :
     pass
 else :
  pass
  if 68 - 68: OOooOOo % Ii + IIiIiII11i . I1ii11iIi11i
def ooO0OOoOoOO00 ( ) :
 if 65 - 65: I1111IIi / Ii1I
 if 84 - 84: ii . Ii % oO0o * I1ii11iIi11i / O0OOOoOoo0
 Iiiiii111i1ii ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 95 - 95: oO0o - Ii . oO0o % Ii1IIIi1 * o0o00Oo0O + Ii
 Iiiiii111i1ii ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 65 - 65: o0o00Oo0O / O0OOOoOoo0 . ooOoO0O00 * O0OOOoOoo0 / iI11I1II1I1I - o000O0o
 if 93 - 93: OOooOOo % Ii - ii1ii11IIIiiI % oO0o
def oOOo0OOOOOoO ( ) :
 iIIIiIi = OoOooO ( 'http://cnfstudio.com/' )
 i1IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , 'http://cnfstudio.com/genre/' + oOooO0 , 7003 , III1iII1I1ii + 'icon.png' )
  if 69 - 69: o0o00Oo0O % O0OOOoOoo0 . I1ii11iIi11i + O0OOOoOoo0
OOooO0OOoo = xbmcgui . Dialog ( )
if 57 - 57: Ii1I . iiiiiiii1 . I1111IIi . I1ii11iIi11i % o000O0o * Ii1I
o0o0OooOOo0OO00 = '{UN},' ; i1i11IiII = '{IG},' ; oo0O = '{PL},' ; o00o0oo0OoO = '{LO},' ; oo0o0O00o0o = '{LP},' ; II1Iii1IiiIi = '{HA},' ; OoOo00ooOO000 = '{XD},' ; iIOoO0O00o0ooo0 = '{TA},' ; o0oOoooOoo0 = '{DP},' ; IiI1Iii1iIIII = '{JT},' ; oo0o00OoO00o0 = '{JJ},' ; ooOOO = '{MM},' ; ii111II = '{FQ},' ; ooOOoOoOoO00 = '{HH},'
if 90 - 90: I11i - oOo0O0Ooo * iiiiiiii1 / o000O0o % oO0o * iI11I1II1I1I
def iIiiIII ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIIIiIi )
 ii1I = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIIIiIi )
 for iIIii , url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , iIIii )
 ii1I = ii1I
 for url in ii1I :
  Iiiiii111i1ii ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 55 - 55: iI11I1II1I1I % OOooOOo
def OO0ooo00o ( url ) :
 if 99 - 99: oOo0O0Ooo
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  i1i = url + '&fv=&sou='
  i1i = i1i . replace ( 'player' , 'watch' )
  Ii1ii1Ii11 = ooooiI1iiI11iii ( i1i )
  o0O0oOOoo0O0 = ooooiI1iiI11iii ( url )
  if 71 - 71: Ii1I + ooOOOoO * I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % Ii
  if 40 - 40: I11i1ii1 - Ii % Ii1I % oOo0O0Ooo . I1111IIi * oO0o
def ooooiI1iiI11iii ( url ) :
 if 51 - 51: o0o00Oo0O % o000O0o - I11i1ii1 * oOo0O0Ooo * o000O0o
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  oOO0oo ( url )
  if 90 - 90: ii1ii11IIIiiI + I1ii11iIi11i / iI11I1II1I1I - o0o00Oo0O + I11i1ii1 . Ii1I
  if 58 - 58: oO0o + O0OOOoOoo0 * I11i . ooOOOoO
def iiIi111IIi ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , III1iII1I1ii + 'LocalM3U.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , III1iII1I1ii + 'RemoteM3U.png' , O0o0Oo , '' )
 if 59 - 59: ooOoO0O00 + OOooOOo . O0OOOoOoo0 + oOo0O0Ooo . o000O0o / O0OOOoOoo0
def ii1iiI ( ) :
 if os . path . exists ( iiI1IiI ) :
  i11ioo0oo0O0Oo0O = open ( iiI1IiI , 'r' )
  for oooO in i11ioo0oo0O0Oo0O :
   Oo0o = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oooO )
   for I1i1i1iii , oOooO0 in Oo0o :
    i1i1iII1 ( I1i1i1iii , oOooO0 , 222 , III1iII1I1ii + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 40 - 40: iiiiiiii1 . IIiIiII11i
def OO00O0O00oOOO ( url ) :
 if os . path . exists ( Remote ) :
  oO0OOoo0OO = o0O0O0ooo0oOO ( url )
  i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1i1i1iii , url in i1IIIII11I1IiI :
   url = ( url ) . strip ( )
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 17 - 17: I11i1ii1
  if 25 - 25: ii1ii11IIIiiI * iI11I1II1I1I * I11i + OOooOOo . OOooOOo
def Iiii1i1 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in i1IIIII11I1IiI :
  oOooO0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oOooO0
 I1i1i1iii = 'plugin.video.GenieTv'
 if 3 - 3: oO0o . oOo0O0Ooo . ooOOOoO . Ii1I
 ii11iI11I111I ( oOooO0 , I1i1i1iii )
 if 44 - 44: ooOoO0O00 - Ii1I + Ii1I . ooOOOoO / Ii1IIIi1
def i1IiiiI1iI ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in i1IIIII11I1IiI :
  oOooO0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oOooO0
 I1i1i1iii = 'repository.GenieTv'
 if 48 - 48: Ii1I . o0o00Oo0O . oOo0O0Ooo * I11i / O0OOOoOoo0
 ii11iI11I111I ( oOooO0 , I1i1i1iii )
 if 61 - 61: I1ii11iIi11i - iiiiiiii1
 if 51 - 51: O0OOOoOoo0 * I11i1ii1 / o0o00Oo0O / o0o00Oo0O
def Ii1I1i ( ) :
 O0oO0 = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , O0oO0 )
 if oO0O0OO0O == 0 :
  oooOOOO0oOo ( )
 if oO0O0OO0O == 1 :
  iiii1Ii ( )
  if 43 - 43: o000O0o + Ii / o000O0o . Ii . o0o00Oo0O / iiiiiiii1
  if 70 - 70: ooOOOoO . OOooOOo
  if 86 - 86: I1111IIi
  if 25 - 25: ii1ii11IIIiiI . o0o00Oo0O . Ii + ii / Ii1IIIi1
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
oo0OO0oOooo = 'https://addons.tvaddons.ag/'
if 17 - 17: I1111IIi + ooOOOoO % I1ii11iIi11i + o000O0o
def iiii1Ii ( ) :
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 iIIi = 'https://addons.tvaddons.ag/search/?keyword=' + i1ii11
 oO0OOoo0OO = OoOooO ( iIIi )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , I111iIi1 , I1i1i1iii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , oOooO0 , 10054 , 'https://addons.tvaddons.ag/' + I111iIi1 , O0o0Oo , '' )
  if 87 - 87: ooOOOoO
  if 54 - 54: ii1ii11IIIiiI
def oooOOOO0oOo ( ) :
 oO0OOoo0OO = OoOooO ( oo0OO0oOooo )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  if 'Repositories' in I1i1i1iii :
   pass
  elif 'Services' in I1i1i1iii :
   pass
  elif 'International' in I1i1i1iii :
   pass
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , oOooO0 , 10053 , 'https://addons.tvaddons.ag/' + iIIii , O0o0Oo , '' )
   if 27 - 27: O0OOOoOoo0 % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
   if 37 - 37: O0OOOoOoo0 + iiiiiiii1 * ii1ii11IIIiiI + I1111IIi
def Addon ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 IiIIIii1iIII1 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  if 'Please' in I1i1i1iii :
   pass
  else :
   OOiIiIIi1 ( I1i1i1iii , url , 10054 , 'https://addons.tvaddons.ag/' + iIIii , O0o0Oo , '' )
 for url in IiIIIii1iIII1 :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
  if 69 - 69: ooOoO0O00 / Ii + I1ii11iIi11i - OOooOOo
  if 13 - 13: I1111IIi . iI11I1II1I1I
def iIi1 ( url , name ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   o00O0 = os . path . join ( OO0Oooo0oOO0O , name + '.zip' )
   try :
    os . remove ( o00O0 )
   except :
    pass
   downloader . download ( url , o00O0 , o0oOoO00o )
   oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print oOO0O00Oo0O0o
   print '======================================='
   extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
   I1iIIiiIIi1i ( )
   if 35 - 35: IIiIiII11i % Ii1IIIi1 . o000O0o * I11i1ii1
def ii11iI11I111I ( url , name ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , name + '.zip' )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print oOO0O00Oo0O0o
 print '======================================='
 extract . all ( o00O0 , oOO0O00Oo0O0o , o0oOoO00o )
 I1iIIiiIIi1i ( )
 if 54 - 54: I11i1ii1 * ooOOOoO - iiiiiiii1
def I1iIIiiIIi1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 15 - 15: O0OOOoOoo0 / o0o00Oo0O
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + I11i1ii1 . iiiiiiii1 * I11i1ii1
def iIi11iIIII1II11Iii ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIIiIi )
 for url , I111iIi1 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , url , 1007 , I111iIi1 )
def I1i11I1IiII1 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIIiIi )
 for url , I111iIi1 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 1006 , I111iIi1 )
  if 40 - 40: I11i - o0o00Oo0O * IIiIiII11i / oOo0O0Ooo . I11i + iiiiiiii1
def O0ooO0Oo0OO0o ( ) :
 iIIIiIi = OoOooO ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , IiI111ii1ii , oo00O00oO000o , o0ooooO0o0O , I1i1i1iii in i1IIIII11I1IiI :
  o0oO00o ( I1i1i1iii , 100109 , oOooO0 , image = IiI111ii1ii , isFolder = True )
  if 39 - 39: I11i1ii1 / Ii1IIIi1 * ooOoO0O00 - iiiiiiii1 * oOo0O0Ooo % oOo0O0Ooo
def III11iO00 ( url ) :
 import random
 oOOIiI1i = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 oOOIiI1i . clear ( )
 o0o0O0oOOoO0 = [ ]
 I11iIIIIiiI = [ ]
 iiiiIIi = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO , IiI111ii1ii , oo00O00oO000o , o0ooooO0o0O , I1i1i1iii in i1IIIII11I1IiI :
  o0o0O0oOOoO0 . append ( [ OoO , I1i1i1iii ] )
  if len ( o0o0O0oOOoO0 ) == len ( i1IIIII11I1IiI ) :
   for oooO in o0o0O0oOOoO0 :
    Ii11111i1 = random . randint ( 1 , len ( o0o0O0oOOoO0 ) )
    try :
     Iiii1iiii = o0o0O0oOOoO0 [ int ( Ii11111i1 ) ]
    except :
     pass
    if len ( I11iIIIIiiI ) <= 20 :
     if Iiii1iiii [ 1 ] not in iiiiIIi :
      O0 = OoOooO ( Iiii1iiii [ 0 ] )
      Iii1I1111ii = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( O0 )
      for OooO00 , O00iIi1i1Ii1 in Iii1I1111ii :
       oooooOoo0ooo = OoOooO ( OooO00 )
       ii1iii1i = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oooooOoo0ooo )
       for O00O0O , i1i in ii1iii1i :
        if 'panda' in i1i :
         i1iIIi1I1I11 = OoOooO ( i1i )
         OOOOO = re . compile ( "url: '(.+?)'" ) . findall ( i1iIIi1I1I11 )
         for iI1IoOoOO000 in OOOOO :
          if 'http' in iI1IoOoOO000 :
           OOO00OO0oOo = xbmcgui . ListItem ( Iiii1iiii [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : Iiii1iiii [ 1 ] } )
           OOO00OO0oOo . setProperty ( "IsPlayable" , "true" )
           oOOIiI1i . add ( iI1IoOoOO000 , OOO00OO0oOo )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOO00OO0oOo )
           if 79 - 79: oO0o / I11i
def o0oO00o ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = Oo00OOOOO
 O0ooO00oO = sys . argv [ 0 ]
 O0ooO00oO += '?mode=' + str ( mode )
 O0ooO00oO += '&title=' + urllib . quote_plus ( name )
 O0ooO00oO += '&image=' + urllib . quote_plus ( image )
 O0ooO00oO += '&page=' + str ( page )
 if url != '' :
  O0ooO00oO += '&url=' + urllib . quote_plus ( url )
 if keyword :
  O0ooO00oO += '&keyword=' + urllib . quote_plus ( keyword )
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  OOO00OO0oOo . addContextMenuItems ( contextMenu )
 if infoLabels :
  OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  OOO00OO0oOo . setProperty ( "IsPlayable" , "true" )
 OOO00OO0oOo . setProperty ( 'Fanart_Image' , O0o0Oo )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = isFolder )
 if 98 - 98: Ii . Ii * ii
 if 61 - 61: I11i . I1111IIi . o0o00Oo0O + ii + o0o00Oo0O
def oo0 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIIiIi )
 for url , iconimage , oo00O00oO000o , o0ooooO0o0O , name in i1IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
    for oooO in oo0OO :
     if oooO == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    IiIiII11i1 ( name , url , 1016 , iconimage , o0ooooO0o0O , oo00O00oO000o )
   else :
    if 'youtube' in url :
     oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for oooO in oo0OO :
      if oooO == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IiIIIoO0oOOooO0 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , o0ooooO0o0O , oo00O00oO000o )
    else :
     oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for oooO in oo0OO :
      if oooO == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IiIIIoO0oOOooO0 ( name , url , 222 , iconimage , o0ooooO0o0O , oo00O00oO000o )
     I1I11i ( 'tvshows' , 'Media Info 3' )
  else :
   Oo00Ooo0O0O0o ( url , iconimage , name )
   if 86 - 86: oOo0O0Ooo + iI11I1II1I1I % I11i1ii1 / Ii1IIIi1 / ii
 else :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIIiIi )
  for url , I111iIi1 , name in i1IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     Iiiiii111i1ii ( name , url , 1016 , I111iIi1 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      i1i1iII1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 )
     else :
      oo0OO = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for oooO in oo0OO :
       if oooO == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      i1i1iII1 ( name , url , 222 , I111iIi1 )
      I1I11i ( 'tvshows' , 'Media Info 3' )
   else :
    Oo00Ooo0O0O0o ( url , I111iIi1 , name )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 96 - 96: o000O0o - IIiIiII11i % oOo0O0Ooo * I1111IIi * ooOOOoO - Ii1IIIi1
def Oo00Ooo0O0O0o ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 O0OO = ( url ) . replace ( OOoOOOOOo0ooOOO0 , 'http' ) . replace ( Iii11I1i , '.com' ) ;
 OoO0o00O0oOOo = ( O0OO ) . replace ( Oo00O0O , 'a' ) . replace ( o0O0o , 'b' ) . replace ( OO0o0o , 'c' ) . replace ( o0OO00oOO , 'd' ) . replace ( oo0O , 'e' ) . replace ( IiI1Iii1iIIII , 'f' ) ;
 ooOI1IiiIiIIi1Ii = ( OoO0o00O0oOOo ) . replace ( OO0ooOO00o0 , 'g' ) . replace ( II1Iii1IiiIi , 'h' ) . replace ( IIiiiii1IIIi , 'i' ) . replace ( Ii1I11Ii1iI , 'j' ) . replace ( O0O0O00OoO0O , 'k' ) . replace ( i1II11III , 'l' ) ;
 oo00oo = ( ooOI1IiiIiIIi1Ii ) . replace ( OOOO0oO0OOo0o , 'm' ) . replace ( OoOOii , 'n' ) . replace ( iiI , 'o' ) . replace ( ooo0O0O0OO , 'p' ) . replace ( oOooOOoO , 'q' ) . replace ( o0o000OOO , 'r' ) ;
 I1111iii1ii11 = ( oo00oo ) . replace ( Oooo , 's' ) . replace ( IiiII1iIi , 't' ) . replace ( III1II1I1iI , 'u' ) . replace ( oOOOOOo0OO0o0oOO0 , 'v' ) . replace ( i1II1IiIIi , 'w' ) . replace ( o0O0 , 'x' ) ;
 iiIi1I1IIIII1IIi = ( I1111iii1ii11 ) . replace ( i11iii1II1I1 , 'y' ) . replace ( IiIi11iI1IIi , 'z' ) . replace ( o0o0OooOOo0OO00 , '.' ) . replace ( i1i11IiII , '(' ) . replace ( o00o0oo0OoO , ')' ) . replace ( oo0o0O00o0o , '/' ) ;
 iII111I = ( iiIi1I1IIIII1IIi ) . replace ( IiIiIiIII1Iii , '1' ) . replace ( OoO00oooo0o , '2' ) . replace ( Ooooo0Oo0oOo , '3' ) . replace ( iIOoO0O00o0ooo0 , '4' ) . replace ( o0oOoooOoo0 , '5' ) . replace ( III1i , '6' ) ;
 IiI1III1 = ( iII111I ) . replace ( oo0o00OoO00o0 , '7' ) . replace ( ooOOO , '8' ) . replace ( ii111II , '9' ) . replace ( ooOOoOoOoO00 , '0' ) . replace ( oooooo0 , ':' ) . replace ( iII1iii , '%' ) ;
 url = ( IiI1III1 ) . replace ( I11OooOooOOooo0 , '-' ) . replace ( OoOo00ooOO000 , '_' ) ;
 i1i1iII1 ( name , url , 222 , iconimage ) ;
 if 13 - 13: IIiIiII11i . oO0o
 if 31 - 31: o000O0o . O0OOOoOoo0 - ooOOOoO . iI11I1II1I1I + ooOOOoO . OOooOOo
def OOoOO00O ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIIiIi )
 for oOooO0 , I111iIi1 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , oOooO0 , 1007 , I111iIi1 )
def II1iIiiiIiiII ( url ) :
 if 89 - 89: O0OOOoOoo0 / ii
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIIiIi )
 for url , I111iIi1 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 1006 , I111iIi1 )
  if 68 - 68: I1111IIi
def iIIiiI11I11i ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 ooo = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooo )
 if 80 - 80: ooOOOoO - Ii1I * ii1ii11IIIiiI / ii * o0o00Oo0O % Ii1IIIi1
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * ii1ii11IIIiiI / iiiiiiii1 * ii
def o0OOOOOo00 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIIiIi )
 for url , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  if '-dir-' in I1i1i1iii :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , iIIii )
  else :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' , url , 1006 , iIIii )
   if 82 - 82: I1ii11iIi11i / ii1ii11IIIiiI / ii1ii11IIIiiI % ii1ii11IIIiiI
def iIiiiI1i1iiiI ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 III1i1iII1 = ( 'http://afewbitsmore.com/' )
 i1IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if '[To Parent Directory]' in I1i1i1iii :
   I1i1i1iii = 'HOME'
   pass
  elif 'HOME' in I1i1i1iii :
   pass
  elif '.m3u' in I1i1i1iii :
   Iiiiii111i1ii ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , III1i1iII1 + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in I1i1i1iii :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , III1i1iII1 + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in I1i1i1iii :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , III1i1iII1 + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) , III1i1iII1 + url , 1012 , III1iII1I1ii + 'music.png' )
def IiiiiI11iii11iI ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iIIii , I1i1i1iii , url in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'music.png' )
  if 46 - 46: O0OOOoOoo0 % iiiiiiii1 % OOooOOo . ii . IIiIiII11i % I1111IIi
def I1i1I1i1I1 ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 III1i1iII1 = url
 i1IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  if '.mp3' in I1i1i1iii :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '/' , '' ) , III1i1iII1 + url , 1011 , III1iII1I1ii + 'music.png' )
def i1IOO ( ) :
 iIIIiIi = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIIIiIi )
 for oOooO0 , iIIii , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , ( 'http://www.cyn.net/music/' + oOooO0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + iIIii ) . replace ( ' ' , '%20' ) )
def Oo0OO0ooO0O0O ( url , img ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 OoO = url
 img = img
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( OoO + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 76 - 76: I11i / ooOOOoO
def OOOoOooO000oO ( url ) :
 iIIIiIi = o0O0O0ooo0oOO ( url )
 OoO = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIIiIi )
 for type , url , I1i1i1iii in i1IIIII11I1IiI :
  if '[VID]' in type :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , OoO + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   OOOoOooO000oO ( OoO + url )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
 if 13 - 13: Ii
def oo0oOO ( ) :
 Ii11 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oOOoooO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1ii11 = oOOoooO . lower ( )
 oOooO0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 Oo0Oo0O = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 OoO = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 54 - 54: Ii1IIIi1 . Ii1I * ooOOOoO % iiiiiiii1 . o0o00Oo0O * I1111IIi
 oO0OOoo0OO = O0o0O00Oo0o0 ( oOooO0 )
 Ii1I1 = O0o0O00Oo0o0 ( Oo0Oo0O )
 O0 = O0o0O00Oo0o0 ( OoO )
 if 87 - 87: ii1ii11IIIiiI % Ii1I * I1ii11iIi11i
 if oO0OOoo0OO != 'Failed' :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oOooO0 , IiI111ii1ii , oo00O00oO000o , OOOoO000 , I1i1i1iii in i1IIIII11I1IiI :
   if oOOoooO in I1i1i1iii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oOooO0 , 1016 , IiI111ii1ii , o0ooooO0o0O , oo00O00oO000o )
    if 59 - 59: I1ii11iIi11i / ooOOOoO - iI11I1II1I1I * iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if Ii1I1 != 'Failed' :
  o0OO0O0Oo = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Ii1I1 )
  for oOooO0 , I1i1i1iii in o0OO0O0Oo :
   if oOOoooO in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oOooO0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 18 - 18: ooOOOoO * Ii1I / Ii / iI11I1II1I1I * ii . Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( O0 )
  for oOooO0 , I1i1i1iii in i1I :
   if oOOoooO in I1i1i1iii . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1i1i1iii + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oOooO0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 69 - 69: I1ii11iIi11i * I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 91 - 91: I11i . I11i1ii1 / oO0o / Ii * I11i
    if 52 - 52: oOo0O0Ooo - Ii / I1111IIi . o000O0o
    if 38 - 38: o000O0o + ii * OOooOOo % o000O0o
    if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
    if 24 - 24: OOooOOo * ii1ii11IIIiiI
    if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
OOOO0oO0OOo0o = '{SF},' ; OoOOii = '{IF},' ; iiI = '{PW},' ; Ooooo0Oo0oOo = '{AM},' ; ooo0O0O0OO = '{GF},' ; oOooOOoO = '{DD},' ; o0o000OOO = '{UO},' ; Oooo = '{LE},' ; III1II1I1iI = '{ZY},' ; oOOOOOo0OO0o0oOO0 = '{UE},' ; i1II1IiIIi = '{PE},' ; o0O0 = '{JE},' ; i11iii1II1I1 = '{TH},' ; IiIi11iI1IIi = '{LK},'
if 81 - 81: Ii1IIIi1
if 58 - 58: IIiIiII11i . iiiiiiii1 . ii1ii11IIIiiI * ii / ii1ii11IIIiiI / ooOOOoO
def IiIi1I1ii111 ( ) :
 iIIIiIi = OoOooO ( 'http://www.iwatchseries.me/tv-list/' )
 i1IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , oOooO0 , 8021 , III1iII1I1ii + 'iwatch.png' )
  I1I11i ( 'movies' , 'MAIN' )
def i1iI11I ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii , iiiI1iI1 in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii + iiiI1iI1 , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def oOoOOO ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  iI1i11i1i1i ( url )
def iI1i11i1i1i ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( iIIIiIi )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( iIIIiIi )
 Iii1I1111ii = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iIIIiIi )
 ii1iii1i = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( 'VidSpot - ' + I1i1i1iii , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in i1I :
  i1i1iII1 ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url , I1i1i1iii in ii1iii1i :
  i1i1iII1 ( 'VidUp' + I1i1i1iii , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for I1i1i1iii , url in Iii1I1111ii :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   i1i1iII1 ( 'TheVideo - ' + I1i1i1iii , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 83 - 83: IIiIiII11i + I1111IIi - I11i % I11i * I11i
def o0iiiii1i1 ( ) :
 iIIIiIi = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 i1IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , oOooO0 , 1021 , III1iII1I1ii + 'anime.png' )
  if 18 - 18: OOooOOo * OOooOOo - I11i % I11i1ii1 % IIiIiII11i - I1111IIi
  if 75 - 75: oO0o . IIiIiII11i . o000O0o / oO0o % iI11I1II1I1I
def iiiII ( ) :
 iIIIiIi = OoOooO ( 'http://www.animetoon.org/cartoon' )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIIiIi )
 for oOooO0 , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , oOooO0 , 1002 , III1iII1I1ii + 'anime.png' )
  if 80 - 80: ooOOOoO
  if 94 - 94: I1111IIi - o0o00Oo0O * oO0o * oO0o % I11i1ii1 - IIiIiII11i
  if 70 - 70: ii
def oo0Oo0oo ( url ) :
 iIIIiIi = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIIiIi )
 for iIIii in i1I :
  oOoooOooOOoO = iIIii
 Iii1I1111ii = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIIiIi )
 for url in Iii1I1111ii :
  Iiiiii111i1ii ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIIiIi )
 for url , I1i1i1iii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1i1i1iii , url , 1003 , oOoooOooOOoO )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIiI1iIiii ( url , IMAGE ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIIiIi )
 for I1i1i1iii , url in i1IIIII11I1IiI :
  print I1i1i1iii + '     ' + url
  if 'easy' in url :
   o0OoO0o00o ( url )
  elif 'playpanda' in url :
   o0OoO0o00o ( url )
   if 46 - 46: O0OOOoOoo0 + iiiiiiii1 % ii * Ii1I
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0OoO0o00o ( url ) :
 iIIIiIi = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIIiIi )
 for url in i1IIIII11I1IiI :
  i1i1iII1 ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 89 - 89: I1111IIi - I1111IIi % O0OOOoOoo0 / ooOOOoO + o000O0o - I1111IIi
  if 97 - 97: ii1ii11IIIiiI % OOooOOo / Ii1I / iI11I1II1I1I * ii * Ii1IIIi1
def oOoO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 . add_header ( 'referer' , url )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 51 - 51: ii + ooOOOoO % OOooOOo . ii1ii11IIIiiI % Ii * I11i1ii1
def o0O0O0ooo0oOO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 49 - 49: oO0o - I1ii11iIi11i - Ii1I
def IiIi1III ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiiII1I = ( '%s%s' % ( IiIii , url ) )
 i1i = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , I111iIi1 , I1i1i1iii in i1IIIII11I1IiI :
  i1i1iII1 ( '%s' % ( '[COLOR' + II + ']' + I1i1i1iii + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I111iIi1 )
  if 41 - 41: iI11I1II1I1I - oO0o * I1111IIi
def OOo00 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  oO0OOo ( url , I1i1i1iii )
 else :
  O00Oo0 ( url )
def O00Oo0 ( url ) :
 import urlresolver
 try :
  OooOooO0OoOoo0o = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( OooOooO0OoOoo0o , xbmcgui . ListItem ( I1i1i1iii ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( I1i1i1iii ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def oOO0oo ( url ) :
 if 27 - 27: oO0o % I11i1ii1 - o0o00Oo0O
 IiiI11i1I = open ( o00OO00OoO , "a" )
 IiiI11i1I . write ( 'url="' + url + '"\n' )
 IiiI11i1I . close
 if 44 - 44: Ii1I + Ii1I - Ii1IIIi1 / IIiIiII11i
 i1I1II1iIIi11 = xbmc . Player ( IiI1iII1II111 ( ) )
 import urlresolver
 try : i1I1II1iIIi11 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( I1i1i1iii ) )
 i1I1II1iIIi11 = xbmc . Player ( IiI1iII1II111 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  OOooO0OOoo = xbmcgui . Dialog ( )
  if OOooO0OOoo . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   OOooO0OOoo . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : i1I1II1iIIi11 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def oO0OOo ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  IiIii11i1IIiI = '.mp4'
  O0oO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   O00Oo0 ( url )
  if oO0O0OO0O == 1 :
   IIiI111i ( url , name , IiIii11i1IIiI )
 elif '.mkv' in url :
  IiIii11i1IIiI = '.mkv'
  O0oO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   O00Oo0 ( url )
  if oO0O0OO0O == 1 :
   IIiI111i ( url , name , IiIii11i1IIiI )
 elif '.mp3' in url :
  IiIii11i1IIiI = '.mp3'
  O0oO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   O00Oo0 ( url )
  if oO0O0OO0O == 1 :
   IIiI111i ( url , name , IiIii11i1IIiI )
 elif '.avi' in url :
  IiIii11i1IIiI = '.avi'
  O0oO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   O00Oo0 ( url )
  if oO0O0OO0O == 1 :
   IIiI111i ( url , name , IiIii11i1IIiI )
 elif '.mov' in url :
  IiIii11i1IIiI = '.mov'
  O0oO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   O00Oo0 ( url )
  if oO0O0OO0O == 1 :
   IIiI111i ( url , name , IiIii11i1IIiI )
 elif '.mpeg' in url :
  IiIii11i1IIiI = '.mpeg'
  O0oO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   O00Oo0 ( url )
  if oO0O0OO0O == 1 :
   IIiI111i ( url , name , IiIii11i1IIiI )
 elif '.mpg' in url :
  IiIii11i1IIiI = '.mpg'
  O0oO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   O00Oo0 ( url )
  if oO0O0OO0O == 1 :
   IIiI111i ( url , name , IiIii11i1IIiI )
 elif '.flv' in url :
  IiIii11i1IIiI = '.flv'
  O0oO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   O00Oo0 ( url )
  if oO0O0OO0O == 1 :
   IIiI111i ( url , name , IiIii11i1IIiI )
 elif '.wmv' in url :
  IiIii11i1IIiI = '.wmv'
  O0oO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  oO0O0OO0O = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , O0oO0 )
  if oO0O0OO0O == 0 :
   O00Oo0 ( url )
  if oO0O0OO0O == 1 :
   IIiI111i ( url , name , IiIii11i1IIiI )
 else :
  O00Oo0 ( url )
def IIiI111i ( url , name , cat ) :
 i1III1i ( )
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 o00O0 = os . path . join ( OO0Oooo0oOO0O , file )
 try :
  os . remove ( o00O0 )
 except :
  pass
 downloader . download ( url , o00O0 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def i1III1i ( ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def Iii1iI11 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % I1i1i1iii )
 xbmc . sleep ( 1 )
 i1I1II1iIIi11 = xbmc . Player ( IiI1iII1II111 ( ) )
 o0oOoO00o . update ( 100 , '%s' % I1i1i1iii )
 xbmc . sleep ( 1 )
 i1I1II1iIIi11 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 33 - 33: I11i1ii1 * ii
def i1I1IIIiiI ( url ) :
 i1I1II1iIIi11 = xbmc . Player ( IiI1iII1II111 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : i1I1II1iIIi11 . play ( url ) . strip ( )
 except : pass
 if 14 - 14: IIiIiII11i + o0o00Oo0O - O0OOOoOoo0
def II1i1ooO0OoOO0 ( url ) :
 i1I1II1iIIi11 = xbmc . Player ( IiI1iII1II111 ( ) )
 import urlresolver
 o0oo00 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 i1I1II1iIIi11 . play ( o0oo00 )
 xbmc . sleep ( 1 )
 i1I1II1iIIi11 . play ( url )
 if 92 - 92: ooOoO0O00
 if 68 - 68: oO0o % I1111IIi - o000O0o - I11i1ii1 . I1ii11iIi11i
def IiI1iII1II111 ( ) :
 try :
  IiII11IIII1 = getSet ( "core-player" )
  if ( IiII11IIII1 == 'DVDPLAYER' ) : iIIii1I = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( IiII11IIII1 == 'MPLAYER' ) : iIIii1I = xbmc . PLAYER_CORE_MPLAYER
  elif ( IiII11IIII1 == 'PAPLAYER' ) : iIIii1I = xbmc . PLAYER_CORE_PAPLAYER
  else : iIIii1I = xbmc . PLAYER_CORE_AUTO
 except : iIIii1I = xbmc . PLAYER_CORE_AUTO
 return iIIii1I
 return True
 if 89 - 89: ooOoO0O00
def Iiiiii111i1ii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O0ooO00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i11i1iIiii = True
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1I1iI = [ ]
  I1I1iI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1I1iI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   I1I1iI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OOO00OO0oOo . addContextMenuItems ( I1I1iI )
 i11i1iIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = True )
 return i11i1iIiii
 if 92 - 92: iI11I1II1I1I * Ii1I
def I1IiI ( name , url , mode , iconimage , fanart , description ) :
 if 5 - 5: I11i1ii1 - iiiiiiii1 - O0OOOoOoo0
 O0ooO00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11i1iIiii = True
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOO00OO0oOo . setProperty ( "Fanart_Image" , fanart )
 i11i1iIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = True )
 return i11i1iIiii
 if 38 - 38: iI11I1II1I1I . ii1ii11IIIiiI
def i1i1iII1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O0ooO00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i11i1iIiii = True
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I1I1iI = [ ]
  I1I1iI . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I1I1iI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   I1I1iI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OOO00OO0oOo . addContextMenuItems ( I1I1iI )
 i11i1iIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = False )
 return i11i1iIiii
 if 12 - 12: oO0o - oOo0O0Ooo + ii + ii * oOo0O0Ooo - ooOoO0O00
 if 64 - 64: Ii + OOooOOo + I11i + Ii1IIIi1
 if 33 - 33: oOo0O0Ooo - O0OOOoOoo0 . ooOoO0O00 / Ii
 if 84 - 84: ooOOOoO / ii / I1111IIi % ooOOOoO . Ii1IIIi1 + iiiiiiii1
 if 94 - 94: ooOOOoO
 if 48 - 48: o000O0o - ii + I11i % ooOoO0O00 - oOo0O0Ooo + Ii1IIIi1
def OOoO ( heading , announce ) :
 class oo0O0oO0o ( ) :
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
   try : iiiiI = open ( announce ) ; Ooo0 = iiiiI . read ( )
   except : Ooo0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( Ooo0 ) )
   return
 oo0O0oO0o ( )
 oo0O0oO0o ( )
 if 37 - 37: o0o00Oo0O
def Ii1I1Ii ( ) :
 OOoO ( 'GenieTv Recomended Sources' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Reaper[/COLOR] [CR]  [COLORred]http://roguemedia.info/cerberus/repo/[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 34 - 34: I1111IIi
 if 5 - 5: oO0o . oOo0O0Ooo
 if 48 - 48: I1ii11iIi11i - oO0o . ooOOOoO - iI11I1II1I1I % ii1ii11IIIiiI
 if 47 - 47: O0OOOoOoo0 / ii - IIiIiII11i
 if 91 - 91: OOooOOo + I11i
def I1iIIiiIIi1i ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 23 - 23: ooOoO0O00
 if 9 - 9: ooOoO0O00 % iiiiiiii1 - oO0o * OOooOOo . I11i
 if 18 - 18: ii1ii11IIIiiI . OOooOOo + O0OOOoOoo0 . oOo0O0Ooo + ii . oO0o
 if 31 - 31: iiiiiiii1 - ooOOOoO
 if 49 - 49: iI11I1II1I1I - iI11I1II1I1I - OOooOOo + I1111IIi / OOooOOo
 if 74 - 74: ii + Ii1I % o0o00Oo0O
 if 32 - 32: Ii1I + Ii1I
 if 89 - 89: I11i1ii1 + o000O0o + ii1ii11IIIiiI - Ii1IIIi1
 if 12 - 12: OOooOOo - I11i - iiiiiiii1 / ooOOOoO
 if 17 - 17: oO0o - iiiiiiii1 - IIiIiII11i / iiiiiiii1 / ii1ii11IIIiiI
 if 30 - 30: Ii1IIIi1 * Ii1I % Ii1I + O0OOOoOoo0 * I1111IIi
 if 33 - 33: I11i + ooOOOoO * o0o00Oo0O * oO0o . Ii1I
 if 74 - 74: O0OOOoOoo0 * O0OOOoOoo0 * I11i / o000O0o
 if 91 - 91: Ii . Ii1I / IIiIiII11i
 if 97 - 97: ii1ii11IIIiiI % ooOoO0O00 % I1111IIi + I1ii11iIi11i - o0o00Oo0O - ooOOOoO
 if 64 - 64: ii1ii11IIIiiI - O0OOOoOoo0
 if 12 - 12: ooOoO0O00
 if 99 - 99: IIiIiII11i - Ii1I * I1111IIi
 if 3 - 3: I1111IIi - Ii1I * O0OOOoOoo0 * Ii1I + I1ii11iIi11i
 if 15 - 15: Ii1I * ii1ii11IIIiiI / O0OOOoOoo0 . I11i / ii1ii11IIIiiI % OOooOOo
 if 75 - 75: ii % Ii % iI11I1II1I1I % Ii1I / Ii
 if 96 - 96: I11i1ii1 * o000O0o / iI11I1II1I1I / ooOOOoO
 if 5 - 5: I11i
 if 83 - 83: ooOOOoO * oOo0O0Ooo . IIiIiII11i * ooOoO0O00 % o0o00Oo0O
def IIII1i1IIIi ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + III111II1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 25 - 25: O0OOOoOoo0 * OOooOOo / oOo0O0Ooo / I1111IIi
def i1iiIi ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iII1Ii1iIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 71 - 71: iI11I1II1I1I . OOooOOo * iiiiiiii1
def o00Oo00o ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + O0oi1IiI1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 53 - 53: ii1ii11IIIiiI - Ii1I * Ii - OOooOOo
def I1I1iiI1iIIii ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o00O0oOO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 97 - 97: I11i1ii1 * ii1ii11IIIiiI % O0OOOoOoo0 * ii1ii11IIIiiI % Ii
def iIiIII11 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + i1I1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 61 - 61: I11i1ii1 . O0OOOoOoo0 / I11i1ii1 * ii
def iiiiIII1IIi1ii111 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 85 - 85: OOooOOo . o0o00Oo0O - iI11I1II1I1I - ii1ii11IIIiiI
def o0O000Ooo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iiii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 65 - 65: iI11I1II1I1I + O0OOOoOoo0
def iI1iIi ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + I1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 60 - 60: I1111IIi / iI11I1II1I1I + ii - Ii1I * Ii
def Iii1iIIi1iIii ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + oOOoo0o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 42 , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 75 - 75: iI11I1II1I1I * O0OOOoOoo0 / OOooOOo * IIiIiII11i . ooOoO0O00
def O0O0OOOOoo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + I1i11iiIiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1i1i1iii , url , IiI111ii1ii , o0ooooO0o0O , o0O0Oo00 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1i1i1iii , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , o0O0Oo00 )
 I1I11i ( 'movies' , 'MAIN' )
 if 59 - 59: ooOOOoO . ooOOOoO * oOo0O0Ooo - ii1ii11IIIiiI % OOooOOo
 if 19 - 19: ii / I1ii11iIi11i - iiiiiiii1 . OOooOOo
 if 8 - 8: ooOOOoO % I11i1ii1 . iI11I1II1I1I
 if 95 - 95: I11i + Ii . Ii1I . I11i1ii1 . I11i
 if 93 - 93: O0OOOoOoo0
 if 55 - 55: IIiIiII11i % I11i - oO0o
 if 48 - 48: I11i1ii1 * iI11I1II1I1I % OOooOOo
 if 100 - 100: IIiIiII11i - Ii + oO0o % I11i1ii1 - iI11I1II1I1I * Ii
 if 30 - 30: oO0o . oO0o . ii1ii11IIIiiI % ii1ii11IIIiiI * ooOoO0O00 * o000O0o
def I11I1I1i1i ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iIiIi11I1iIii1i11 , oo00ooooOOo00 , ii1iOO00Oooo000 in os . walk ( iIi1ii1I1 ) :
     oooOoooo0Ooo0ooo0 = 0
     oooOoooo0Ooo0ooo0 += len ( ii1iOO00Oooo000 )
     if oooOoooo0Ooo0ooo0 > 0 :
      for iiiiI in ii1iOO00Oooo000 :
       os . unlink ( os . path . join ( iIiIi11I1iIii1i11 , iiiiI ) )
  Ii1iiiI = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( Ii1iiiI )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 25 - 25: oO0o % ooOoO0O00
 if 12 - 12: I11i
 if 58 - 58: iI11I1II1I1I * ii1ii11IIIiiI . I11i1ii1 . I1ii11iIi11i * ii1ii11IIIiiI
 if 63 - 63: OOooOOo . ooOOOoO * I11i - ooOOOoO % ooOOOoO
 if 62 - 62: ooOOOoO - I11i1ii1 / I11i1ii1
 if 95 - 95: OOooOOo - ooOoO0O00 / iiiiiiii1 . I11i1ii1 % Ii1IIIi1 - ooOoO0O00
 if 12 - 12: O0OOOoOoo0
 if 96 - 96: o0o00Oo0O
def iII1III ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 89 - 89: Ii1I - I1ii11iIi11i
def ii1OO0 ( url ) :
 I1i1ii1iIii = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 i1IiI = [
 ( I1i1ii1iIii ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( I1i1ii1iIii , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1i1ii1iIii , 'plugin.video.itv' , 'Images' ) ) ]
 if 71 - 71: iI11I1II1I1I + o0o00Oo0O . I1111IIi . O0OOOoOoo0 % I11i % o0o00Oo0O
 OOO00o0oO = 0
 if 51 - 51: IIiIiII11i
 for oooO in i1IiI :
  if os . path . exists ( oooO ) and not oooO in [ oO0o0o0ooO0oO , I1i1ii1iIii ] :
   for iIiIi11I1iIii1i11 , oo00ooooOOo00 , ii1iOO00Oooo000 in os . walk ( oooO ) :
    oooOoooo0Ooo0ooo0 = 0
    oooOoooo0Ooo0ooo0 += len ( ii1iOO00Oooo000 )
    if oooOoooo0Ooo0ooo0 > 0 :
     for iiiiI in ii1iOO00Oooo000 :
      if not iiiiI in oooOOOOO :
       try :
        os . unlink ( os . path . join ( iIiIi11I1iIii1i11 , iiiiI ) )
       except :
        pass
      else : oOOo0O00o ( 'Ignore Log File: %s' % iiiiI )
     for oO0oiIiI in oo00ooooOOo00 :
      try :
       shutil . rmtree ( os . path . join ( iIiIi11I1iIii1i11 , oO0oiIiI ) )
       OOO00o0oO += 1
       oOOo0O00o ( "[Success] cleared %s files from %s" % ( str ( oooOoooo0Ooo0ooo0 ) , os . path . join ( oooO , oO0oiIiI ) ) )
      except :
       oOOo0O00o ( "[Failed] to wipe cache in: %s" % os . path . join ( oooO , oO0oiIiI ) )
  else :
   for iIiIi11I1iIii1i11 , oo00ooooOOo00 , ii1iOO00Oooo000 in os . walk ( oooO ) :
    for oO0oiIiI in oo00ooooOOo00 :
     if 'cache' in oO0oiIiI . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iIiIi11I1iIii1i11 , oO0oiIiI ) )
       OOO00o0oO += 1
       oOOo0O00o ( "[Success] wiped %s " % os . path . join ( oooO , oO0oiIiI ) )
      except :
       oOOo0O00o ( "[Failed] to wipe cache in: %s" % os . path . join ( oooO , oO0oiIiI ) )
       if 33 - 33: ooOoO0O00
 iII1III ( oO , 'Clear Cache: Removed %s Files' % OOO00o0oO )
 if 92 - 92: oOo0O0Ooo / ooOoO0O00 * Ii * IIiIiII11i
 if 16 - 16: ii1ii11IIIiiI
 if 96 - 96: I11i / iiiiiiii1 % ii1ii11IIIiiI - I11i1ii1
 if 35 - 35: Ii1IIIi1
 if 90 - 90: Ii
 if 47 - 47: oO0o . Ii
 if 9 - 9: OOooOOo - ooOOOoO . ii % I11i1ii1
def OoOoO00OOoOOOo0 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IIIiIiIIII1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIiIi11I1iIii1i11 , oo00ooooOOo00 , ii1iOO00Oooo000 in os . walk ( IIIiIiIIII1i1 ) :
   oooOoooo0Ooo0ooo0 = 0
   oooOoooo0Ooo0ooo0 += len ( ii1iOO00Oooo000 )
   if 90 - 90: oOo0O0Ooo % I11i1ii1 % ii / oO0o . I1111IIi * IIiIiII11i
   if 83 - 83: o000O0o
   if oooOoooo0Ooo0ooo0 > 0 :
    if 34 - 34: OOooOOo
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( oooOoooo0Ooo0ooo0 ) + " files found" , "Do you want to delete them?" ) :
     if 75 - 75: ooOOOoO / iI11I1II1I1I + Ii1I / oO0o
     for iiiiI in ii1iOO00Oooo000 :
      os . unlink ( os . path . join ( iIiIi11I1iIii1i11 , iiiiI ) )
     for oO0oiIiI in oo00ooooOOo00 :
      shutil . rmtree ( os . path . join ( iIiIi11I1iIii1i11 , oO0oiIiI ) )
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
 if 50 - 50: iiiiiiii1 / ooOOOoO % iI11I1II1I1I
 if 46 - 46: I11i1ii1 + O0OOOoOoo0 - I1ii11iIi11i % Ii1IIIi1 + ii + iI11I1II1I1I
 if 99 - 99: oO0o - I1111IIi * I1111IIi + o000O0o / O0OOOoOoo0 + Ii1IIIi1
 if 58 - 58: Ii + iI11I1II1I1I * I11i - OOooOOo
 if 31 - 31: ooOoO0O00
 if 87 - 87: oOo0O0Ooo / ooOOOoO + ii + o0o00Oo0O . ii1ii11IIIiiI
 if 44 - 44: I1ii11iIi11i % I1ii11iIi11i
 if 58 - 58: Ii1IIIi1 * IIiIiII11i
 if 29 - 29: iI11I1II1I1I % OOooOOo % Ii1I / OOooOOo - Ii
def ii1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 IIIiIiIIII1i1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iIiIi11I1iIii1i11 , oo00ooooOOo00 , ii1iOO00Oooo000 in os . walk ( IIIiIiIIII1i1 ) :
   oooOoooo0Ooo0ooo0 = 0
   oooOoooo0Ooo0ooo0 += len ( ii1iOO00Oooo000 )
   if 67 - 67: Ii1IIIi1 / ii1ii11IIIiiI
   if 51 - 51: ooOOOoO % IIiIiII11i - I11i % oO0o * Ii * O0OOOoOoo0
   if oooOoooo0Ooo0ooo0 > 0 :
    if 82 - 82: ii / oOo0O0Ooo * IIiIiII11i - ii % iI11I1II1I1I * oO0o
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( oooOoooo0Ooo0ooo0 ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: Ii - OOooOOo * ooOOOoO . I1ii11iIi11i * I11i1ii1
     for iiiiI in ii1iOO00Oooo000 :
      os . unlink ( os . path . join ( iIiIi11I1iIii1i11 , iiiiI ) )
     for oO0oiIiI in oo00ooooOOo00 :
      shutil . rmtree ( os . path . join ( iIiIi11I1iIii1i11 , oO0oiIiI ) )
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
 ii1OO0 ( url )
 return
 if 21 - 21: Ii1IIIi1
 if 11 - 11: o000O0o % Ii * o0o00Oo0O
 if 28 - 28: iiiiiiii1 / iI11I1II1I1I + Ii1IIIi1 . Ii1I % Ii1IIIi1 + oO0o
 if 79 - 79: o000O0o
 if 39 - 39: iiiiiiii1 % o000O0o % o0o00Oo0O % o0o00Oo0O - O0OOOoOoo0 - o000O0o
 if 83 - 83: Ii + iI11I1II1I1I
 if 21 - 21: I11i / Ii % iiiiiiii1
 if 56 - 56: I11i * iI11I1II1I1I . ii1ii11IIIiiI + OOooOOo % iiiiiiii1
 if 11 - 11: Ii1IIIi1
 if 12 - 12: ii * Ii1IIIi1 * Ii1I * I11i1ii1
def iiIi11i1I1 ( url , name ) :
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0OoO0 = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 I11Ii1I1I = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml.bak' )
 if os . path . exists ( I11Ii1I1I ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   o0OoO0 = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
   try :
    os . remove ( o0OoO0 )
    print '=== GenieTv - REMOVING    ' + str ( o0OoO0 ) + '    ==='
   except :
    pass
   i1i = iI111I11I1I1 . http_GET ( url ) . content
   o0ooOOoO0oO0 = open ( o0OoO0 , "w" )
   o0ooOOoO0oO0 . write ( i1i )
   o0ooOOoO0oO0 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( o0OoO0 ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  o0OoO0 = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
  try :
   os . remove ( o0OoO0 )
   print '=== GenieTv - REMOVING    ' + str ( o0OoO0 ) + '    ==='
  except :
   pass
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  o0ooOOoO0oO0 = open ( o0OoO0 , "w" )
  o0ooOOoO0oO0 . write ( i1i )
  o0ooOOoO0oO0 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0OoO0 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 85 - 85: Ii - O0OOOoOoo0
def o0o00O0 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0OoO0 = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
 try :
  o0ooOOoO0oO0 = open ( o0OoO0 ) . read ( )
  if 'zero' in o0ooOOoO0oO0 :
   name = '0CACHE'
  elif 'tuxen' in o0ooOOoO0oO0 :
   name = 'TUXENS'
  elif 'muckys' in o0ooOOoO0oO0 :
   name = 'MUCKYS'
  elif 'p2p1' in o0ooOOoO0oO0 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in o0ooOOoO0oO0 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in o0ooOOoO0oO0 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 88 - 88: oOo0O0Ooo
def O0Oo0oO00O00 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 o0OoO0 = os . path . join ( OO0Oooo0oOO0O , 'advancedsettings.xml' )
 try :
  os . remove ( o0OoO0 )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( o0OoO0 ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 16 - 16: Ii1IIIi1 % I1111IIi - IIiIiII11i - I11i * Ii / iiiiiiii1
 if 74 - 74: O0OOOoOoo0 % ooOoO0O00 / I1ii11iIi11i . o0o00Oo0O
 if 48 - 48: Ii1I % IIiIiII11i + ooOOOoO
 if 25 - 25: I1111IIi * I11i / oOo0O0Ooo . I1111IIi % IIiIiII11i
 if 50 - 50: OOooOOo * O0OOOoOoo0
 if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / ooOOOoO
 if 92 - 92: I11i
 if 8 - 8: O0OOOoOoo0 + Ii1I . ii1ii11IIIiiI
 if 50 - 50: I1ii11iIi11i
 if 16 - 16: ii1ii11IIIiiI - OOooOOo % I1ii11iIi11i / ii1ii11IIIiiI . ooOOOoO + I11i1ii1
def oOoO00O ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 i1IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for ooOOoo0 , i1I11I1iIii , i11IiIi , I1II1 in i1IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ooOOoo0 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % i11IiIi , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I1II1 )
  inc = inc + 1
  if 90 - 90: oOo0O0Ooo - Ii
  if 42 - 42: Ii1IIIi1 . I1ii11iIi11i
  if 21 - 21: O0OOOoOoo0 . oOo0O0Ooo / ooOOOoO
  if 97 - 97: iI11I1II1I1I + ooOoO0O00 - I11i
  if 73 - 73: oO0o - Ii % iiiiiiii1 / I1ii11iIi11i - ii % Ii1IIIi1
  if 79 - 79: oOo0O0Ooo / I11i . ii1ii11IIIiiI * Ii1I + ooOOOoO
  if 96 - 96: oO0o * IIiIiII11i
  if 1 - 1: oOo0O0Ooo - OOooOOo
  if 74 - 74: OOooOOo * IIiIiII11i + o0o00Oo0O + ooOOOoO
def IiiiI1Ii ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0OoO0 = os . path . join ( OO0Oooo0oOO0O , 'addons2.ini' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  o0ooOOoO0oO0 = open ( o0OoO0 , "w" )
  o0ooOOoO0oO0 . write ( i1i )
  o0ooOOoO0oO0 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0OoO0 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 6 - 6: iI11I1II1I1I * iI11I1II1I1I
def OOOO0oo0o0O ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  OO0Oooo0oOO0O = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  o0OoO0 = os . path . join ( OO0Oooo0oOO0O , 'settings.xml' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  o0ooOOoO0oO0 = open ( o0OoO0 , "w" )
  o0ooOOoO0oO0 . write ( i1i )
  o0ooOOoO0oO0 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( o0OoO0 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 29 - 29: Ii1I + ii . oO0o . ooOoO0O00 - ii * Ii
 if 19 - 19: Ii1I * o0o00Oo0O - I11i1ii1
def I1iI1 ( ) :
 try :
  I11i1I1111i = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( I11i1I1111i ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    ii1Iii1iiI11 = os . path . join ( I11i1I1111i , "source.db" )
    os . unlink ( ii1Iii1iiI11 )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 1 - 1: ooOOOoO - ii1ii11IIIiiI
 if 33 - 33: I1111IIi
 if 62 - 62: oOo0O0Ooo * ooOoO0O00 % iI11I1II1I1I - ooOOOoO
 if 100 - 100: o0o00Oo0O - iI11I1II1I1I * I1ii11iIi11i
 if 35 - 35: I11i1ii1
def OoOooO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 57 - 57: oO0o . I1ii11iIi11i + oOo0O0Ooo
 if 18 - 18: oOo0O0Ooo - Ii1I * ooOOOoO / Ii - I11i % I11i
 if 31 - 31: ooOOOoO
 if 100 - 100: Ii * Ii . iI11I1II1I1I % O0OOOoOoo0 * Ii1I
 if 17 - 17: ii1ii11IIIiiI * I1111IIi * Ii / Ii1I / Ii
 if 23 - 23: ii + Ii / I1ii11iIi11i / O0OOOoOoo0 . O0OOOoOoo0 * oOo0O0Ooo
 if 98 - 98: I1111IIi
def i11i1ii1I ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; i11iI = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if i11iI :
  O0oo0oo0 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; O0oo0oo0 = xbmc . translatePath ( O0oo0oo0 ) ;
  iiII1II = os . path . join ( O0oo0oo0 , ".." , ".." ) ; iiII1II = os . path . abspath ( iiII1II ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + iiII1II ) ; I1i1i11I1II = False
  try :
   for iIiIi11I1iIii1i11 , oo00ooooOOo00 , ii1iOO00Oooo000 in os . walk ( iiII1II , topdown = True ) :
    oo00ooooOOo00 [ : ] = [ oO0oiIiI for oO0oiIiI in oo00ooooOOo00 if oO0oiIiI not in o0oO0 ]
    for I1i1i1iii in ii1iOO00Oooo000 :
     try : os . remove ( os . path . join ( iIiIi11I1iIii1i11 , I1i1i1iii ) )
     except :
      if I1i1i1iii not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : I1i1i11I1II = True
      plugintools . log ( "Error removing " + iIiIi11I1iIii1i11 + " " + I1i1i1iii )
    for I1i1i1iii in oo00ooooOOo00 :
     try : os . rmdir ( os . path . join ( iIiIi11I1iIii1i11 , I1i1i1iii ) )
     except :
      if I1i1i1iii not in [ "Database" , "userdata" ] : I1i1i11I1II = True
      plugintools . log ( "Error removing " + iIiIi11I1iIii1i11 + " " + I1i1i1iii )
   if not I1i1i11I1II : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OOOO00OOO00 ( )
 if 96 - 96: ooOoO0O00
 if 50 - 50: oOo0O0Ooo + I1ii11iIi11i
 if 17 - 17: Ii1I + o000O0o * iiiiiiii1 - I11i1ii1 + iI11I1II1I1I . I1ii11iIi11i
def iiI11ii ( ) :
 Ooo000OO0oOo0 = [ ]
 ooo0o00Ooo0o = sys . argv [ 2 ]
 if len ( ooo0o00Ooo0o ) >= 2 :
  o0OO0o0o00o = sys . argv [ 2 ]
  o0OOoO0 = o0OO0o0o00o . replace ( '?' , '' )
  if ( o0OO0o0o00o [ len ( o0OO0o0o00o ) - 1 ] == '/' ) :
   o0OO0o0o00o = o0OO0o0o00o [ 0 : len ( o0OO0o0o00o ) - 2 ]
  IiiI1i1i11I1 = o0OOoO0 . split ( '&' )
  Ooo000OO0oOo0 = { }
  for II1iII1 in range ( len ( IiiI1i1i11I1 ) ) :
   oOOO0ooo = { }
   oOOO0ooo = IiiI1i1i11I1 [ II1iII1 ] . split ( '=' )
   if ( len ( oOOO0ooo ) ) == 2 :
    Ooo000OO0oOo0 [ oOOO0ooo [ 0 ] ] = oOOO0ooo [ 1 ]
    if 18 - 18: I1ii11iIi11i - o000O0o + oOo0O0Ooo . ooOOOoO
 return Ooo000OO0oOo0
 if 67 - 67: I1111IIi / I11i + ooOOOoO % O0OOOoOoo0 - I11i1ii1 - oOo0O0Ooo
I1ioOo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
I1IIii11 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i11iIiiiI1I = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
II11IIi11Ii11 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i1II1IiiIi = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iII1I = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
III111II1I = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
oOoOo0O00Oo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
iII1Ii1iIIii = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
O0oi1IiI1I = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
o00O0oOO0o = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i1I1i1 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
II1 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
iiii1 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
I1ii = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
oOOoo0o00 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
I111 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Iiii1iiIi = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
iiiiI11iiIIi = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
II11II1I = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
oOo0oO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iiIi1iIiI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
I1i11iiIiIi = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
IiIii = base64 . decodestring ( 'Q1VOVA==' )
def iiOOooooO0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O0ooO00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11i1iIiii = True
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOO00OO0oOo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1I1iI = [ ]
  if showcontext == 'fav' :
   I1I1iI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   I1I1iI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OOO00OO0oOo . addContextMenuItems ( I1I1iI )
 i11i1iIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = True )
 return i11i1iIiii
 if 62 - 62: IIiIiII11i
def OOiIiIIi1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O0ooO00oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 i11i1iIiii = True
 OOO00OO0oOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00OO0oOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OOO00OO0oOo . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I1I1iI = [ ]
  if showcontext == 'fav' :
   I1I1iI . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   I1I1iI . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OOO00OO0oOo . addContextMenuItems ( I1I1iI )
 i11i1iIiii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooO00oO , listitem = OOO00OO0oOo , isFolder = False )
 return i11i1iIiii
 if 47 - 47: Ii1I
 if 39 - 39: Ii
o0OO0o0o00o = iiI11ii ( )
oOooO0 = None
I1i1i1iii = None
O0OOO0OOooo00 = None
IiI111ii1ii = None
o0ooooO0o0O = None
o0O0Oo00 = None
OOo = None
i11i11IiI1iIi = None
if 18 - 18: O0OOOoOoo0 . Ii1IIIi1
if 86 - 86: I1111IIi / oO0o / iiiiiiii1 . IIiIiII11i - o0o00Oo0O
try :
 i11i11IiI1iIi = int ( o0OO0o0o00o [ "fav_mode" ] )
except :
 pass
 if 44 - 44: ooOoO0O00
try :
 oOooO0 = urllib . unquote_plus ( o0OO0o0o00o [ "url" ] )
except :
 pass
try :
 I1i1i1iii = urllib . unquote_plus ( o0OO0o0o00o [ "name" ] )
except :
 pass
try :
 IiI111ii1ii = urllib . unquote_plus ( o0OO0o0o00o [ "iconimage" ] )
except :
 pass
try :
 O0OOO0OOooo00 = int ( o0OO0o0o00o [ "mode" ] )
except :
 pass
try :
 o0ooooO0o0O = urllib . unquote_plus ( o0OO0o0o00o [ "fanart" ] )
except :
 pass
try :
 o0O0Oo00 = urllib . unquote_plus ( o0OO0o0o00o [ "description" ] )
except :
 pass
 if 10 - 10: IIiIiII11i * ii * ii
 if 47 - 47: OOooOOo - iiiiiiii1 + I1111IIi . IIiIiII11i / o000O0o / Ii
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( O0OOO0OOooo00 )
print "URL: " + str ( oOooO0 )
print "Name: " + str ( I1i1i1iii )
print "IconImage: " + str ( IiI111ii1ii )
if 28 - 28: oOo0O0Ooo . I11i + oO0o
if 100 - 100: o000O0o + IIiIiII11i / I1111IIi / ooOoO0O00 / ii1ii11IIIiiI / o0o00Oo0O
def I1I11i ( content , viewType ) :
 if 50 - 50: ii1ii11IIIiiI + ii1ii11IIIiiI
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 51 - 51: Ii1I / ii * I1111IIi
if IiI111ii1ii == None : IiI111ii1ii = Oo00OOOOO
if o0ooooO0o0O == None : o0ooooO0o0O = O0o0Oo
if O0OOO0OOooo00 == None :
 o0o0o0oO0oOO ( )
 if 78 - 78: O0OOOoOoo0 / Ii1I . Ii
elif O0OOO0OOooo00 == 1 :
 oOoo0OO0 ( oOooO0 )
 if 69 - 69: ooOOOoO - IIiIiII11i
elif O0OOO0OOooo00 == 44 :
 oOo0 ( oOooO0 )
 if 66 - 66: oOo0O0Ooo . oOo0O0Ooo - OOooOOo * ii * IIiIiII11i + oOo0O0Ooo
elif O0OOO0OOooo00 == 2 :
 OooOO ( )
 if 59 - 59: ii1ii11IIIiiI
elif O0OOO0OOooo00 == 3 :
 o00ooO0ooO0o0 ( )
 if 59 - 59: IIiIiII11i - oO0o
elif O0OOO0OOooo00 == 21 :
 i1i1II ( )
 if 31 - 31: ooOOOoO - OOooOOo / I11i * OOooOOo / I1ii11iIi11i + I11i
elif O0OOO0OOooo00 == 4 :
 ooo0OO0OOooO0 ( )
 if 46 - 46: I1111IIi * oO0o / Ii1IIIi1 + I1ii11iIi11i
elif O0OOO0OOooo00 == 5 :
 OO0o0o0oo ( oOooO0 )
 if 24 - 24: I11i1ii1 % Ii1IIIi1 . o0o00Oo0O * I1ii11iIi11i
elif O0OOO0OOooo00 == 6 :
 OoOoO00OOoOOOo0 ( oOooO0 )
 if 52 - 52: o0o00Oo0O . iiiiiiii1 + O0OOOoOoo0 / Ii
elif O0OOO0OOooo00 == 7 :
 iiIi11i1I1 ( oOooO0 , I1i1i1iii )
 if 52 - 52: o000O0o % I1ii11iIi11i * IIiIiII11i
elif O0OOO0OOooo00 == 8 :
 o0o00O0 ( oOooO0 , I1i1i1iii )
 if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
elif O0OOO0OOooo00 == 9 :
 FIXREPOSADDONS ( oOooO0 )
 if 27 - 27: ooOoO0O00 - o000O0o + Ii1IIIi1
elif O0OOO0OOooo00 == 10 :
 I1iIIiiIIi1i ( )
 if 3 - 3: I1111IIi % iiiiiiii1 . ii
elif O0OOO0OOooo00 == 11 :
 O0Oo0oO00O00 ( oOooO0 )
 if 19 - 19: iiiiiiii1 * ii1ii11IIIiiI - o000O0o
elif O0OOO0OOooo00 == 12 :
 oOoO00O ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 78 - 78: oO0o - ii1ii11IIIiiI / Ii1IIIi1
elif O0OOO0OOooo00 == 13 :
 I11I1I1i1i ( )
 if 81 - 81: OOooOOo
elif O0OOO0OOooo00 == 14 :
 ii1OO0 ( oOooO0 )
 if 21 - 21: O0OOOoOoo0 / Ii1IIIi1 % I1111IIi
elif O0OOO0OOooo00 == 15 :
 O00oOooo00o0o ( )
 if 51 - 51: ooOOOoO + I11i1ii1 / oOo0O0Ooo
elif O0OOO0OOooo00 == 16 :
 IiiiI1Ii ( oOooO0 , I1i1i1iii )
 if 3 - 3: iI11I1II1I1I / Ii1IIIi1 % o000O0o . ii1ii11IIIiiI - ii1ii11IIIiiI
elif O0OOO0OOooo00 == 17 :
 OOOO0oo0o0O ( oOooO0 , I1i1i1iii )
 if 55 - 55: Ii % ii + o0o00Oo0O
elif O0OOO0OOooo00 == 18 :
 I1iI1 ( )
 if 7 - 7: I11i1ii1 - Ii * O0OOOoOoo0 / ii1ii11IIIiiI - I11i
elif O0OOO0OOooo00 == 19 :
 i1i1Ii1IiIII ( oOooO0 )
 if 62 - 62: I11i - iI11I1II1I1I . ooOOOoO . ii1ii11IIIiiI * ii1ii11IIIiiI
elif O0OOO0OOooo00 == 40 :
 OO0 ( I1i1i1iii , oOooO0 , o0O0Oo00 )
 if 24 - 24: ooOOOoO
elif O0OOO0OOooo00 == 42 :
 i1I1i1i1I1 ( I1i1i1iii , oOooO0 , o0O0Oo00 )
 if 93 - 93: oOo0O0Ooo % oO0o / Ii / ooOOOoO
elif O0OOO0OOooo00 == 43 :
 Oooo0ooOoo0 ( oOooO0 )
 if 60 - 60: I11i1ii1 - ii1ii11IIIiiI . oOo0O0Ooo * o000O0o * Ii
elif O0OOO0OOooo00 == 20 :
 o00OO0o0 ( oOooO0 )
 if 29 - 29: oO0o - I1ii11iIi11i . o000O0o / oO0o % Ii
elif O0OOO0OOooo00 == 22 :
 IIII1i1IIIi ( oOooO0 )
 if 26 - 26: I11i1ii1 . iiiiiiii1 / IIiIiII11i % ii1ii11IIIiiI
elif O0OOO0OOooo00 == 23 :
 i1iiIi ( oOooO0 )
 if 82 - 82: Ii1IIIi1 % o0o00Oo0O % iI11I1II1I1I % I1111IIi + Ii
elif O0OOO0OOooo00 == 24 :
 o00Oo00o ( oOooO0 )
 if 64 - 64: ooOoO0O00 / I1111IIi . I1111IIi - iiiiiiii1 % Ii1IIIi1 . IIiIiII11i
elif O0OOO0OOooo00 == 25 :
 I1I1iiI1iIIii ( oOooO0 )
 if 78 - 78: iiiiiiii1 - o0o00Oo0O - iiiiiiii1 . iI11I1II1I1I % Ii1I . ii
elif O0OOO0OOooo00 == 26 :
 iIiIII11 ( oOooO0 )
 if 64 - 64: I1111IIi
elif O0OOO0OOooo00 == 27 :
 iiiiIII1IIi1ii111 ( oOooO0 )
 if 21 - 21: I11i - I11i1ii1 * ii . ii
elif O0OOO0OOooo00 == 28 :
 o0O000Ooo ( oOooO0 )
 if 17 - 17: Ii1IIIi1 - O0OOOoOoo0 % oOo0O0Ooo * Ii1IIIi1 * iI11I1II1I1I . I11i
elif O0OOO0OOooo00 == 29 :
 iI1iIi ( oOooO0 )
 if 58 - 58: o000O0o - IIiIiII11i + o0o00Oo0O
elif O0OOO0OOooo00 == 30 :
 oooIi1I11IiI1i ( oOooO0 )
 if 54 - 54: iI11I1II1I1I - I1111IIi - I1111IIi
elif O0OOO0OOooo00 == 31 :
 Iii1iIIi1iIii ( oOooO0 )
 if 18 - 18: Ii + iI11I1II1I1I . Ii
elif O0OOO0OOooo00 == 32 :
 OOI1iI1ii1II ( )
 if 63 - 63: O0OOOoOoo0 - oO0o * Ii1IIIi1
elif O0OOO0OOooo00 == 33 :
 oO0oo0O0 ( )
 if 89 - 89: O0OOOoOoo0 / I1ii11iIi11i
elif O0OOO0OOooo00 == 35 :
 oo00ooOooO ( oOooO0 )
 if 66 - 66: I11i + OOooOOo % ii . ooOOOoO
elif O0OOO0OOooo00 == 34 :
 o0O0OOoo ( oOooO0 )
 if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
elif O0OOO0OOooo00 == 36 :
 Oo00Oooo00o ( oOooO0 )
 if 93 - 93: ooOoO0O00 + iiiiiiii1 / oO0o - ooOOOoO % I1ii11iIi11i / ii1ii11IIIiiI
elif O0OOO0OOooo00 == 37 :
 OOOO000Ooo0O ( oOooO0 )
 if 1 - 1: I1ii11iIi11i / ii1ii11IIIiiI . Ii % Ii1IIIi1 + I11i + o0o00Oo0O
elif O0OOO0OOooo00 == 38 :
 iIii1I1iII ( oOooO0 )
 if 54 - 54: iiiiiiii1 + I11i1ii1 % I1111IIi
elif O0OOO0OOooo00 == 41 :
 i11i1ii1I ( o0OO0o0o00o )
 if 83 - 83: I11i * iI11I1II1I1I
elif O0OOO0OOooo00 == 39 :
 O0O0OOOOoo ( oOooO0 )
 if 36 - 36: OOooOOo + IIiIiII11i - oO0o % I11i1ii1 * ooOoO0O00
elif O0OOO0OOooo00 == 45 :
 TEXTS ( )
 if 4 - 4: ii1ii11IIIiiI + oO0o * Ii1I
elif O0OOO0OOooo00 == 46 :
 Ii1I1Ii ( )
 if 13 - 13: OOooOOo - I1111IIi * iI11I1II1I1I * o0o00Oo0O
elif O0OOO0OOooo00 == 47 :
 GEVID ( )
 if 26 - 26: ii + o000O0o + oO0o . o0o00Oo0O
elif O0OOO0OOooo00 == 48 :
 o0oo0OO ( I1i1i1iii , oOooO0 , o0O0Oo00 )
 if 46 - 46: ii - I1ii11iIi11i * iiiiiiii1 * Ii1IIIi1 * iiiiiiii1 . o000O0o
elif O0OOO0OOooo00 == 49 :
 iI1i111I1Ii ( )
 if 96 - 96: ii1ii11IIIiiI / I1111IIi % I11i + ooOOOoO
elif O0OOO0OOooo00 == 22222 :
 oOO0oo ( oOooO0 )
 if 46 - 46: oO0o * oOo0O0Ooo
elif O0OOO0OOooo00 == 222 :
 OOo00 ( oOooO0 )
 if 25 - 25: iiiiiiii1 . I1111IIi % o0o00Oo0O % ooOoO0O00
elif O0OOO0OOooo00 == 2222222 :
 O00Oo0 ( oOooO0 )
 if 53 - 53: o0o00Oo0O % I11i1ii1
elif O0OOO0OOooo00 == 222222 :
 oO0OOo ( oOooO0 , I1i1i1iii )
 if 41 - 41: I1111IIi
elif O0OOO0OOooo00 == 333 :
 IiIi1III ( oOooO0 )
 if 29 - 29: I11i1ii1
 if 70 - 70: o000O0o . o0o00Oo0O % ooOOOoO % I1111IIi - ooOOOoO * Ii1I
elif O0OOO0OOooo00 == 1020 :
 o0iiiii1i1 ( )
 if 22 - 22: ooOoO0O00
elif O0OOO0OOooo00 == 1021 :
 ANIMEEP ( )
 if 82 - 82: o000O0o . iI11I1II1I1I - Ii1I
elif O0OOO0OOooo00 == 1022 :
 ANIMEPLAY ( oOooO0 )
 if 55 - 55: I1ii11iIi11i % ii1ii11IIIiiI . iI11I1II1I1I * iiiiiiii1
elif O0OOO0OOooo00 == 1001 :
 iiiII ( )
 if 33 - 33: o0o00Oo0O - oOo0O0Ooo / Ii1I / oO0o + O0OOOoOoo0 - o000O0o
elif O0OOO0OOooo00 == 1005 :
 OOoOO00O ( )
 if 27 - 27: iiiiiiii1 + I11i1ii1 - iiiiiiii1 % Ii * I1ii11iIi11i * I11i
elif O0OOO0OOooo00 == 1007 :
 II1iIiiiIiiII ( oOooO0 )
 if 88 - 88: Ii1IIIi1
elif O0OOO0OOooo00 == 1010 :
 o0OOOOOo00 ( oOooO0 )
 if 25 - 25: oO0o + I11i . I11i1ii1 - ii1ii11IIIiiI . o000O0o * ii1ii11IIIiiI
elif O0OOO0OOooo00 == 1011 :
 I1i1I1i1I1 ( oOooO0 )
 if 85 - 85: ooOoO0O00
elif O0OOO0OOooo00 == 1012 :
 iIiiiI1i1iiiI ( oOooO0 )
 if 94 - 94: ii . o0o00Oo0O / ii
elif O0OOO0OOooo00 == 1030 :
 i1IOO ( )
 if 67 - 67: Ii + OOooOOo
elif O0OOO0OOooo00 == 1031 :
 Oo0OO0ooO0O0O ( oOooO0 , IiI111ii1ii )
 if 50 - 50: I11i1ii1 . ooOoO0O00 + Ii1I . Ii1IIIi1
elif O0OOO0OOooo00 == 1032 :
 OOOoOooO000oO ( oOooO0 )
 if 97 - 97: oOo0O0Ooo
elif O0OOO0OOooo00 == 1006 :
 Parse . ParseURL ( oOooO0 )
 if 63 - 63: o0o00Oo0O - OOooOOo / Ii / ii / I11i1ii1 / IIiIiII11i
elif O0OOO0OOooo00 == 2030 :
 Parse . addonParseURL ( oOooO0 )
 if 45 - 45: IIiIiII11i . oO0o + oO0o * iI11I1II1I1I
elif O0OOO0OOooo00 == 2031 :
 Parse . apkParseURL ( oOooO0 )
 if 23 - 23: I1111IIi * OOooOOo % ii1ii11IIIiiI / ii1ii11IIIiiI - I11i1ii1 - Ii1IIIi1
elif O0OOO0OOooo00 == 2032 :
 Parse . ParseBOSS ( oOooO0 )
 if 86 - 86: Ii1IIIi1 . ii * oOo0O0Ooo - I1ii11iIi11i / Ii * O0OOOoOoo0
elif O0OOO0OOooo00 == 1002 :
 oo0Oo0oo ( oOooO0 )
 if 56 - 56: oOo0O0Ooo . ooOOOoO % O0OOOoOoo0
elif O0OOO0OOooo00 == 1003 :
 IIiI1iIiii ( oOooO0 , IiI111ii1ii )
 if 33 - 33: ooOOOoO / Ii1IIIi1 - Ii1IIIi1 / Ii * OOooOOo + o0o00Oo0O
elif O0OOO0OOooo00 == 1004 :
 o0OoO0o00o ( oOooO0 )
 if 2 - 2: Ii % oOo0O0Ooo
elif O0OOO0OOooo00 == 1008 :
 o0Oooo0O00Ooo ( )
 if 90 - 90: IIiIiII11i
elif O0OOO0OOooo00 == 1009 :
 OO00O0O00oOOO ( oOooO0 )
 if 2 - 2: ii1ii11IIIiiI - ii - Ii % I1ii11iIi11i / ii1ii11IIIiiI
elif O0OOO0OOooo00 == 2001 :
 ii1iiI ( )
 if 77 - 77: I11i . I11i * iiiiiiii1 + Ii1IIIi1 - Ii
elif O0OOO0OOooo00 == 2002 :
 IiiiiI11iii11iI ( oOooO0 )
 if 45 - 45: oOo0O0Ooo . oOo0O0Ooo - I1ii11iIi11i * Ii1IIIi1
elif O0OOO0OOooo00 == 1013 :
 Ii1 ( )
elif O0OOO0OOooo00 == 10111113 :
 oO0ooOoOO ( oOooO0 )
 if 71 - 71: ooOoO0O00 / ooOOOoO
elif O0OOO0OOooo00 == 1014 :
 o000OO0o ( )
 if 14 - 14: ii
elif O0OOO0OOooo00 == 1015 :
 O0O0ooO0oO0O ( oOooO0 )
 if 99 - 99: I11i * I11i
elif O0OOO0OOooo00 == 1016 :
 oo0 ( oOooO0 , IiI111ii1ii , I1i1i1iii )
 if 6 - 6: Ii + o000O0o % I11i1ii1 + Ii - Ii1IIIi1
elif O0OOO0OOooo00 == 1017 :
 IIIIi1 ( )
 if 12 - 12: O0OOOoOoo0 . o000O0o % I1111IIi * ii . I1111IIi
elif O0OOO0OOooo00 == 1018 :
 I1iI11iIiIi1 ( oOooO0 )
 if 15 - 15: oOo0O0Ooo . oOo0O0Ooo / Ii
elif O0OOO0OOooo00 == 1023 :
 OoOo0o ( )
 if 17 - 17: iI11I1II1I1I / oO0o - IIiIiII11i
elif O0OOO0OOooo00 == 1024 :
 iIi11iIIII1II11Iii ( oOooO0 )
 if 46 - 46: iI11I1II1I1I * o000O0o / Ii + IIiIiII11i + ooOOOoO
elif O0OOO0OOooo00 == 1025 :
 I1i11I1IiII1 ( oOooO0 )
 if 30 - 30: o0o00Oo0O * I1111IIi - iiiiiiii1 % o0o00Oo0O * ii1ii11IIIiiI
elif O0OOO0OOooo00 == 4001 :
 iiIi11iI1iii ( )
 if 29 - 29: Ii1I % Ii1I % ii1ii11IIIiiI + I11i1ii1 % iI11I1II1I1I
elif O0OOO0OOooo00 == 4002 :
 OOOooo ( )
 if 41 - 41: Ii1I % iiiiiiii1
elif O0OOO0OOooo00 == 4003 :
 i11iI1 ( )
 if 37 - 37: I1ii11iIi11i . oOo0O0Ooo % OOooOOo . oO0o - I1ii11iIi11i / oO0o
elif O0OOO0OOooo00 == 4004 :
 oooOoOOO0oo0o ( )
 if 34 - 34: Ii + oO0o + Ii . I1111IIi % o0o00Oo0O
elif O0OOO0OOooo00 == 4005 :
 iiiI ( )
 if 64 - 64: I11i . iI11I1II1I1I
elif O0OOO0OOooo00 == 4006 :
 OooO0oo ( )
 if 86 - 86: I11i1ii1 - ooOOOoO . iI11I1II1I1I - iI11I1II1I1I
elif O0OOO0OOooo00 == 4007 :
 i11OOoo ( )
 if 61 - 61: ii1ii11IIIiiI % I1ii11iIi11i + OOooOOo
elif O0OOO0OOooo00 == 4008 :
 O0OOo ( )
 if 60 - 60: o000O0o . ii
elif O0OOO0OOooo00 == 4009 : i11i11II11i ( )
elif O0OOO0OOooo00 == 4010 : IIiI1I ( )
elif O0OOO0OOooo00 == 3000 :
 iiIi111IIi ( )
 if 40 - 40: ooOOOoO
elif O0OOO0OOooo00 == 3001 :
 iIIIIIi11Ii ( )
 if 44 - 44: I11i1ii1
elif O0OOO0OOooo00 == 3002 :
 oOOooo ( oOooO0 )
 if 35 - 35: IIiIiII11i + O0OOOoOoo0 / Ii1I * oOo0O0Ooo . ooOOOoO
elif O0OOO0OOooo00 == 3003 :
 iIi11i1I11Ii ( oOooO0 )
 if 97 - 97: oOo0O0Ooo / I11i
elif O0OOO0OOooo00 == 3004 :
 OoOOooOOoo ( oOooO0 )
 if 13 - 13: Ii1I
elif O0OOO0OOooo00 == 404 :
 iIIiiI11I11i ( I1i1i1iii , oOooO0 , IiI111ii1ii )
 if 72 - 72: I1ii11iIi11i + I1111IIi / ii1ii11IIIiiI * I1ii11iIi11i
elif O0OOO0OOooo00 == 405 :
 Iii1iI11 ( oOooO0 )
 if 41 - 41: Ii1IIIi1 - OOooOOo . oOo0O0Ooo + Ii + oO0o * O0OOOoOoo0
elif O0OOO0OOooo00 == 7030 :
 OO000o0O0o ( )
 if 85 - 85: oO0o + IIiIiII11i
elif O0OOO0OOooo00 == 7021 :
 O0oooOoO ( I1i1i1iii )
 if 87 - 87: oO0o
elif O0OOO0OOooo00 == 7022 :
 iiooo0o0oO ( I1i1i1iii )
 if 93 - 93: ii
elif O0OOO0OOooo00 == 7000 :
 OOOOo00oOOO00 ( I1i1i1iii , oOooO0 , img )
 if 80 - 80: I11i
elif O0OOO0OOooo00 == 7050 :
 IiIiI111IIII1 ( oOooO0 )
 if 3 - 3: Ii / Ii1IIIi1 + o000O0o
elif O0OOO0OOooo00 == 7051 :
 OOooiIi1 ( oOooO0 )
 if 10 - 10: oO0o . oO0o + o0o00Oo0O
elif O0OOO0OOooo00 == 7052 :
 II11111I ( oOooO0 )
 if 13 - 13: ooOoO0O00 . oOo0O0Ooo
elif O0OOO0OOooo00 == 7053 :
 OOoo ( oOooO0 )
 if 45 - 45: I11i1ii1 % ooOOOoO
elif O0OOO0OOooo00 == 7054 :
 CoolPlay ( oOooO0 )
 if 37 - 37: O0OOOoOoo0
elif O0OOO0OOooo00 == 7060 :
 i1I1I ( )
 if 70 - 70: o0o00Oo0O + iI11I1II1I1I % o0o00Oo0O * I11i - I1ii11iIi11i - I11i1ii1
elif O0OOO0OOooo00 == 7061 :
 Iii1iiIi1II ( oOooO0 )
 if 94 - 94: ooOoO0O00 + I1111IIi / ii - o000O0o / Ii1IIIi1 / OOooOOo
elif O0OOO0OOooo00 == 7063 :
 iIIIOOO00o0O ( oOooO0 )
 if 55 - 55: Ii1IIIi1
elif O0OOO0OOooo00 == 7062 :
 iiiiii ( oOooO0 )
 if 5 - 5: ooOOOoO / OOooOOo
elif O0OOO0OOooo00 == 7064 :
 NATatozcat ( )
 if 48 - 48: ooOoO0O00 - o000O0o . ii - oO0o - ooOoO0O00
elif O0OOO0OOooo00 == 7067 :
 ooII1 ( oOooO0 )
 if 19 - 19: o000O0o % ii1ii11IIIiiI + Ii1I . IIiIiII11i * Ii
elif O0OOO0OOooo00 == 7066 :
 NATatozA ( oOooO0 )
 if 87 - 87: ii1ii11IIIiiI / iiiiiiii1 % OOooOOo * Ii1I - ii / OOooOOo
elif O0OOO0OOooo00 == 7065 :
 o0OOO ( oOooO0 )
 if 24 - 24: ooOOOoO . Ii1IIIi1 * ooOoO0O00 . Ii1I / I11i1ii1 / o0o00Oo0O
elif O0OOO0OOooo00 == 7070 :
 Ii1iIii ( )
 if 62 - 62: I11i % IIiIiII11i
elif O0OOO0OOooo00 == 7071 :
 DIZIlist ( oOooO0 )
 if 22 - 22: o000O0o - I11i
elif O0OOO0OOooo00 == 7072 :
 DIZIpull ( oOooO0 )
 if 89 - 89: Ii1IIIi1
elif O0OOO0OOooo00 == 7073 :
 WATCHDIZI ( oOooO0 )
 if 34 - 34: O0OOOoOoo0 . Ii1IIIi1
elif O0OOO0OOooo00 == 7002 :
 oOOo0OOOOOoO ( )
 if 13 - 13: oO0o * Ii1IIIi1 + o000O0o
elif O0OOO0OOooo00 == 7003 :
 iIiiIII ( oOooO0 )
 if 21 - 21: Ii . ii1ii11IIIiiI % ooOoO0O00 * ii1ii11IIIiiI . o000O0o + ii1ii11IIIiiI
elif O0OOO0OOooo00 == 7004 :
 OO0ooo00o ( oOooO0 )
 if 92 - 92: ooOoO0O00 + oO0o * ooOOOoO
elif O0OOO0OOooo00 == 7020 :
 ooooiI1iiI11iii ( oOooO0 )
 if 70 - 70: I1ii11iIi11i
elif O0OOO0OOooo00 == 7001 :
 iiI11i1II ( )
 if 93 - 93: O0OOOoOoo0 . Ii1I . I1ii11iIi11i . o000O0o . ii
elif O0OOO0OOooo00 == 7010 :
 iIiiII11 ( oOooO0 )
 if 51 - 51: o0o00Oo0O - O0OOOoOoo0
elif O0OOO0OOooo00 == 7011 :
 oo00o ( oOooO0 )
 if 65 - 65: o0o00Oo0O / IIiIiII11i * I1111IIi % ii1ii11IIIiiI + I11i
elif O0OOO0OOooo00 == 7012 :
 ii11 ( oOooO0 )
 if 43 - 43: iiiiiiii1 + oO0o * ii
elif O0OOO0OOooo00 == 7013 :
 cnfTVPlay2 ( oOooO0 )
elif O0OOO0OOooo00 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oOooO0 )
elif O0OOO0OOooo00 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oOooO0 )
elif O0OOO0OOooo00 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1i1i1iii , oOooO0 , IiI111ii1ii )
elif O0OOO0OOooo00 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif O0OOO0OOooo00 == 7018 :
 ooO0OOoOoOO00 ( )
elif O0OOO0OOooo00 == 7019 :
 CNF_Studio_Indexer . List_Movies ( oOooO0 )
elif O0OOO0OOooo00 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oOooO0 )
elif O0OOO0OOooo00 == 7024 :
 CNF_Studio_Indexer . Box_Office ( oOooO0 )
 if 85 - 85: O0OOOoOoo0 + Ii1IIIi1
elif O0OOO0OOooo00 == 8000 :
 Iii11 ( )
elif O0OOO0OOooo00 == 8001 :
 oo00ooOOOo0O ( )
elif O0OOO0OOooo00 == 8002 :
 iI1IIIiIII11 ( )
elif O0OOO0OOooo00 == 8003 :
 IiI1I1 ( )
elif O0OOO0OOooo00 == 8004 :
 o0oOOoOoo ( )
elif O0OOO0OOooo00 == 8005 :
 O000 ( )
elif O0OOO0OOooo00 == 8006 :
 oOoOO00Ooo ( I1i1i1iii , oOooO0 )
elif O0OOO0OOooo00 == 8030 :
 i1iI ( oOooO0 )
elif O0OOO0OOooo00 == 8045 :
 I1I1iiI1i ( oOooO0 )
elif O0OOO0OOooo00 == 8046 :
 IiII1111I ( oOooO0 )
elif O0OOO0OOooo00 == 8047 :
 I1Ii111I111 ( oOooO0 )
elif O0OOO0OOooo00 == 8048 :
 Iii11I ( oOooO0 )
elif O0OOO0OOooo00 == 8049 :
 iI1ii1 ( oOooO0 )
elif O0OOO0OOooo00 == 804900 :
 O0oOOo ( oOooO0 )
elif O0OOO0OOooo00 == 8020 :
 IiIi1I1ii111 ( )
elif O0OOO0OOooo00 == 8021 :
 i1iI11I ( oOooO0 )
elif O0OOO0OOooo00 == 8022 :
 oOoOOO ( oOooO0 )
elif O0OOO0OOooo00 == 8023 :
 iI1i11i1i1i ( oOooO0 )
elif O0OOO0OOooo00 == 8040 :
 O0Oo000 ( )
elif O0OOO0OOooo00 == 8041 :
 i111i11iI1i1I ( oOooO0 )
elif O0OOO0OOooo00 == 8042 :
 Ii11I1 ( oOooO0 )
elif O0OOO0OOooo00 == 8043 :
 yt . PlayVideo ( oOooO0 )
elif O0OOO0OOooo00 == 8044 :
 OO00OO ( oOooO0 )
elif O0OOO0OOooo00 == 8060 :
 iI1I ( )
elif O0OOO0OOooo00 == 8061 :
 OoOoooOO00OO ( oOooO0 )
elif O0OOO0OOooo00 == 8064 :
 IIIII1 ( )
elif O0OOO0OOooo00 == 8065 :
 i11iII1 ( oOooO0 )
elif O0OOO0OOooo00 == 8070 :
 i11iI1111ii1I ( )
elif O0OOO0OOooo00 == 8071 :
 OoOo0 ( oOooO0 )
elif O0OOO0OOooo00 == 7080 :
 iiIIii ( oOooO0 )
elif O0OOO0OOooo00 == 8090 :
 i1iII ( )
elif O0OOO0OOooo00 == 8091 :
 ooOoooOoo0oO ( oOooO0 )
elif O0OOO0OOooo00 == 8092 :
 II1iiIiI1 ( oOooO0 )
elif O0OOO0OOooo00 == 8093 :
 i1I1iii1I11II ( oOooO0 )
elif O0OOO0OOooo00 == 8081 :
 IIiI1IiI1iIi1 ( )
elif O0OOO0OOooo00 == 8062 :
 O00OO0o0 ( oOooO0 )
elif O0OOO0OOooo00 == 8063 :
 i1Ii1IIIi111111 ( oOooO0 )
elif O0OOO0OOooo00 == 8050 :
 IIi1II ( )
elif O0OOO0OOooo00 == 8051 :
 i11i ( oOooO0 )
elif O0OOO0OOooo00 == 8052 :
 Ii11I1I11II ( oOooO0 )
elif O0OOO0OOooo00 == 8085 :
 Oo0oo ( )
elif O0OOO0OOooo00 == 8086 :
 iII1I1Ii11i1i ( oOooO0 )
elif O0OOO0OOooo00 == 8087 :
 OOoOO0ooo0O ( oOooO0 )
elif O0OOO0OOooo00 == 8088 :
 ii1IIi1IIIIi1 ( oOooO0 , I1i1i1iii )
elif O0OOO0OOooo00 == 9000 :
 oOoOO0000oO00 ( )
elif O0OOO0OOooo00 == 1111 :
 oo0oOO ( )
elif O0OOO0OOooo00 == 9001 :
 Oo0oooO0oO ( )
elif O0OOO0OOooo00 == 9002 :
 I1ii1 ( )
elif O0OOO0OOooo00 == 9003 :
 III1II ( )
elif O0OOO0OOooo00 == 9004 :
 World1 ( )
elif O0OOO0OOooo00 == 9005 :
 World2 ( oOooO0 )
elif O0OOO0OOooo00 == 9006 :
 World3 ( oOooO0 )
elif O0OOO0OOooo00 == 9007 :
 II1iiIii1ii1 ( )
elif O0OOO0OOooo00 == 9008 :
 iiiiiiI ( oOooO0 )
elif O0OOO0OOooo00 == 9009 :
 iI111iiI1II ( oOooO0 )
elif O0OOO0OOooo00 == 9010 :
 OO0OOO0o0OOO0 ( )
elif O0OOO0OOooo00 == 9011 :
 iiIiiIiI11i1 ( oOooO0 )
elif O0OOO0OOooo00 == 50 :
 OooO00oo0O0 ( oOooO0 )
elif O0OOO0OOooo00 == 9020 :
 champlist ( )
elif O0OOO0OOooo00 == 9021 :
 i1iI11IiII ( )
elif O0OOO0OOooo00 == 9022 :
 oO00Oo0OO ( )
elif O0OOO0OOooo00 == 9023 :
 i11iIIiii ( )
elif O0OOO0OOooo00 == 9024 :
 i1i1 ( oOooO0 )
elif O0OOO0OOooo00 == 9030 :
 i1ii ( oOooO0 )
elif O0OOO0OOooo00 == 9031 :
 i11iiIii11I1 ( oOooO0 )
elif O0OOO0OOooo00 == 9032 :
 oo0O000OooO0 ( oOooO0 )
elif O0OOO0OOooo00 == 9033 :
 IIIi1Iii11I ( oOooO0 )
elif O0OOO0OOooo00 == 9034 :
 OO0O0OOo0O ( )
elif O0OOO0OOooo00 == 7085 :
 iiIii ( oOooO0 )
elif O0OOO0OOooo00 == 7086 :
 O00Oo00o ( oOooO0 )
elif O0OOO0OOooo00 == 7087 :
 o0OO00Ooo0 ( o0O0Oo00 )
elif O0OOO0OOooo00 == 9666 :
 ii1 ( oOooO0 )
elif O0OOO0OOooo00 == 10100 : o00oO0O000 ( )
elif O0OOO0OOooo00 == 101001 : III ( oOooO0 )
elif O0OOO0OOooo00 == 10105 : o00O00oO ( oOooO0 )
elif O0OOO0OOooo00 == 10106 : OO000O000OOO ( oOooO0 )
elif O0OOO0OOooo00 == 10104 : III11i ( oOooO0 )
elif O0OOO0OOooo00 == 10107 : Oo0Oi1 ( )
elif O0OOO0OOooo00 == 10103 : I111Ii1I1I1iI ( oOooO0 )
elif O0OOO0OOooo00 == 10108 : ooo0OOoo ( oOooO0 )
elif O0OOO0OOooo00 == 10000 : Origin_Menu ( )
elif O0OOO0OOooo00 == 10001 : oOOO ( )
elif O0OOO0OOooo00 == 10002 : iIiIiIiI ( )
elif O0OOO0OOooo00 == 10003 : IiIII1 ( )
elif O0OOO0OOooo00 == 10004 : OOO0ooo ( oOooO0 )
elif O0OOO0OOooo00 == 10005 : IiI1I11iIii ( )
elif O0OOO0OOooo00 == 10006 : iI1ii ( oOooO0 )
elif O0OOO0OOooo00 == 10007 : OoOiII11IiIi ( oOooO0 , IiI111ii1ii )
elif O0OOO0OOooo00 == 10008 : Iii1i11 ( )
elif O0OOO0OOooo00 == 10009 : II1II ( )
elif O0OOO0OOooo00 == 10010 : OO00 ( oOooO0 )
elif O0OOO0OOooo00 == 10011 : i1I11IiI ( oOooO0 )
elif O0OOO0OOooo00 == 10012 : O00Oo0 ( oOooO0 )
elif O0OOO0OOooo00 == 10113 : GRABG ( oOooO0 , I1i1i1iii )
elif O0OOO0OOooo00 == 10109 : II1i1ooO0OoOO0 ( oOooO0 )
elif O0OOO0OOooo00 == 10013 : iII1I1IIiiiI ( oOooO0 )
elif O0OOO0OOooo00 == 10014 : III1i1IIII1i ( )
elif O0OOO0OOooo00 == 10015 : o0oo00O ( )
elif O0OOO0OOooo00 == 10016 : Oooooooo0o ( oOooO0 )
elif O0OOO0OOooo00 == 10017 : o0III11IiI ( )
elif O0OOO0OOooo00 == 10018 : i1iiiiii1 ( )
elif O0OOO0OOooo00 == 10019 : IIIIi1Iii1iIi ( )
elif O0OOO0OOooo00 == 10020 : iIIi1II1 ( )
elif O0OOO0OOooo00 == 10021 : II11I ( )
elif O0OOO0OOooo00 == 10022 : O0oooOOo0 ( oOooO0 )
elif O0OOO0OOooo00 == 10023 : IIII11111Ii ( I1i1i1iii , oOooO0 )
elif O0OOO0OOooo00 == 10024 : III11iI1i11i ( oOooO0 )
elif O0OOO0OOooo00 == 10025 : Oo0OO0000oooo ( )
elif O0OOO0OOooo00 == 10026 : i111iiIiiIiI ( )
elif O0OOO0OOooo00 == 10027 : oOoo00 ( )
elif O0OOO0OOooo00 == 10028 : Oo00o ( )
elif O0OOO0OOooo00 == 10029 : iIii1II1I ( )
elif O0OOO0OOooo00 == 423 : I1IIiIi ( oOooO0 )
elif O0OOO0OOooo00 == 426 : iii1IiII ( oOooO0 )
elif O0OOO0OOooo00 == 10030 : Izle_Films ( )
elif O0OOO0OOooo00 == 10031 : Latest_Izle_Movies ( )
elif O0OOO0OOooo00 == 10032 : Izle_Genres ( )
elif O0OOO0OOooo00 == 10033 : Izle_Pop_Movies ( )
elif O0OOO0OOooo00 == 10034 : Izle_Boxsets ( )
elif O0OOO0OOooo00 == 10035 : Izle_Search ( )
elif O0OOO0OOooo00 == 10036 : Izle_Genres_Movie ( oOooO0 )
elif O0OOO0OOooo00 == 10037 : Izle_Boxset_single ( oOooO0 )
elif O0OOO0OOooo00 == 10038 : Izle_IFRAME ( )
elif O0OOO0OOooo00 == 10039 : Izle_Boxsets_Next ( oOooO0 )
elif O0OOO0OOooo00 == 10040 : Oo0o0000OOoO ( )
elif O0OOO0OOooo00 == 10041 : OO0ooo ( oOooO0 )
elif O0OOO0OOooo00 == 10042 : Oo0O0o00o00 ( oOooO0 )
elif O0OOO0OOooo00 == 10043 : II1i1 ( )
elif O0OOO0OOooo00 == 10044 : IIi1I1iII111 ( oOooO0 )
elif O0OOO0OOooo00 == 10045 : oO00OO0o0ooO ( I1i1i1iii )
elif O0OOO0OOooo00 == 10046 : I1iIi1111 ( oOooO0 )
elif O0OOO0OOooo00 == 10047 : iI1i1Iiii ( oOooO0 )
elif O0OOO0OOooo00 == 10048 : iIII1IIi ( oOooO0 )
elif O0OOO0OOooo00 == 10049 : oO0OOoOO ( oOooO0 )
elif O0OOO0OOooo00 == 10050 : Ii1I1i ( )
elif O0OOO0OOooo00 == 10051 : oooOOOO0oOo ( )
elif O0OOO0OOooo00 == 10052 : iiii1Ii ( )
elif O0OOO0OOooo00 == 10053 : Addon ( oOooO0 )
elif O0OOO0OOooo00 == 10054 : iIi1 ( oOooO0 , I1i1i1iii )
elif O0OOO0OOooo00 == 10055 :
 oooOo00 ( "addFavorite" )
 try :
  I1i1i1iii = I1i1i1iii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1i1i1iii = I1i1i1iii . split ( '  - ' ) [ 0 ]
 except :
  pass
 Ooo0oO0 ( I1i1i1iii , oOooO0 , IiI111ii1ii , o0ooooO0o0O , i11i11IiI1iIi )
elif O0OOO0OOooo00 == 10056 :
 oooOo00 ( "rmFavorite" )
 try :
  I1i1i1iii = I1i1i1iii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1i1i1iii = I1i1i1iii . split ( '  - ' ) [ 0 ]
 except :
  pass
 OO0O00 ( I1i1i1iii )
elif O0OOO0OOooo00 == 10057 :
 oooOo00 ( "getFavorites" )
 Oo0oOooOooO ( )
elif O0OOO0OOooo00 == 10058 : II1Ii1I1i ( )
elif O0OOO0OOooo00 == 10059 : Donators_Guide ( )
elif O0OOO0OOooo00 == 10060 : oo000o0000oO ( )
elif O0OOO0OOooo00 == 10061 : OOOOoO ( )
elif O0OOO0OOooo00 == 10062 : OOOO00OoooO ( I1i1i1iii , oOooO0 , o0O0Oo00 )
elif O0OOO0OOooo00 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
elif O0OOO0OOooo00 == 10064 : i111I1iiIiII ( )
elif O0OOO0OOooo00 == 10065 : o0oO0OO00oo0o ( oOooO0 )
elif O0OOO0OOooo00 == 10066 : II1Iiii11111 ( oOooO0 )
elif O0OOO0OOooo00 == 10068 : ii1II ( oOooO0 )
elif O0OOO0OOooo00 == 10069 : iIi1Ii1i1iI ( oOooO0 )
elif O0OOO0OOooo00 == 10070 : IiIIiii1I ( oOooO0 )
elif O0OOO0OOooo00 == 10071 : Genie_Watch ( )
elif O0OOO0OOooo00 == 10072 : OoOoO0oOOooo ( )
elif O0OOO0OOooo00 == 10073 : iIi11i ( oOooO0 )
elif O0OOO0OOooo00 == 10074 : ooo0O0o0OoOO ( oOooO0 )
elif O0OOO0OOooo00 == 10075 : I1iIIIiI ( IiI111ii1ii , I1i1i1iii , oOooO0 )
elif O0OOO0OOooo00 == 10076 : Ii1Ii1I ( oOooO0 )
elif O0OOO0OOooo00 == 10077 : IiiII1iIii111iII ( oOooO0 )
elif O0OOO0OOooo00 == 10078 : IIiiiiIi1I ( )
elif O0OOO0OOooo00 == 10079 : Genie_Watch_Tv_Shows ( )
elif O0OOO0OOooo00 == 10080 : Genie_Watch_Tv_Genre ( oOooO0 )
elif O0OOO0OOooo00 == 10081 : Genie_Watch_TV_PlayRun ( oOooO0 )
elif O0OOO0OOooo00 == 10082 : Genie_Watch_TV_Episodes ( oOooO0 , IiI111ii1ii )
elif O0OOO0OOooo00 == 10083 : Genie_Watch_Tv_Recent ( oOooO0 )
elif O0OOO0OOooo00 == 10084 : OoOo ( )
elif O0OOO0OOooo00 == 10085 : Iiii1i1 ( )
elif O0OOO0OOooo00 == 10086 : i1IiiiI1iI ( )
elif O0OOO0OOooo00 == 20000 : ooo0oooo0 ( )
elif O0OOO0OOooo00 == 20001 : O0Ooo0OOOo0oo ( oOooO0 )
elif O0OOO0OOooo00 == 20002 : I1iO0o0O0OooOoo ( oOooO0 )
elif O0OOO0OOooo00 == 20003 : IiOO0OOOOOo ( oOooO0 )
elif O0OOO0OOooo00 == 20004 : iii11i1i1 ( oOooO0 )
elif O0OOO0OOooo00 == 20005 : OOo0oO0o ( oOooO0 )
elif O0OOO0OOooo00 == 21004 : O000O0OO00oo ( )
elif O0OOO0OOooo00 == 21005 : Oooo0Oo00o ( oOooO0 )
elif O0OOO0OOooo00 == 21006 : iI1Ii111I1 ( oOooO0 )
elif O0OOO0OOooo00 == 21007 : IiOo00O0o0O ( oOooO0 )
elif O0OOO0OOooo00 == 30000 : IIO000oooOO0Oo0 ( )
elif O0OOO0OOooo00 == 30001 : OOOoOOO0o0ooo ( )
elif O0OOO0OOooo00 == 100121 : Resolve ( oOooO0 )
elif O0OOO0OOooo00 == 30003 : oooOO0OO0 ( )
elif O0OOO0OOooo00 == 30004 : ii11III ( oOooO0 )
elif O0OOO0OOooo00 == 30005 : oOooOoOOo0O ( oOooO0 )
elif O0OOO0OOooo00 == 30006 : IiIii11I ( )
elif O0OOO0OOooo00 == 30007 : oooo0oOOoO000 ( )
elif O0OOO0OOooo00 == 30008 : IiIII ( oOooO0 )
elif O0OOO0OOooo00 == 30009 : I11iIiI1i1I1iiii1Ii11 ( oOooO0 )
elif O0OOO0OOooo00 == 30010 : iI1iiiiiii ( oOooO0 )
elif O0OOO0OOooo00 == 30011 : IIIIIiiI11i1 ( )
elif O0OOO0OOooo00 == 30012 : iiI111i1 ( )
elif O0OOO0OOooo00 == 30013 : iIii1I1111 ( )
elif O0OOO0OOooo00 == 30014 : IiIi ( )
elif O0OOO0OOooo00 == 30015 : IiiI1i111I1i ( oOooO0 , IiI111ii1ii , o0ooooO0o0O )
elif O0OOO0OOooo00 == 30016 : o0OoOooOO0o0 ( oOooO0 )
elif O0OOO0OOooo00 == 30019 : oO00oO00O0Oo ( oOooO0 )
elif O0OOO0OOooo00 == 30017 : iI1Ii11 ( oOooO0 )
elif O0OOO0OOooo00 == 30018 : IIIi11 ( oOooO0 )
elif O0OOO0OOooo00 == 30030 : OoOo0O0 ( )
elif O0OOO0OOooo00 == 30031 : OO0oI1iii1i ( )
elif O0OOO0OOooo00 == 30032 : iIIiiiI ( )
elif O0OOO0OOooo00 == 30033 : I1o0 ( )
elif O0OOO0OOooo00 == 30034 : I1IiiiiI1i1I ( )
elif O0OOO0OOooo00 == 30035 : o0o0ooOo00 ( oOooO0 )
elif O0OOO0OOooo00 == 30036 : OO00oO0OoO0o ( oOooO0 )
elif O0OOO0OOooo00 == 30037 : I11I111i1I1 ( oOooO0 )
elif O0OOO0OOooo00 == 30038 : iio0oo0Oo ( )
elif O0OOO0OOooo00 == 30039 : OOOoOoO ( )
elif O0OOO0OOooo00 == 50000 : O0O0ooOOO ( )
elif O0OOO0OOooo00 == 50001 : i1iiI ( )
elif O0OOO0OOooo00 == 50002 : oOOo ( oOooO0 )
elif O0OOO0OOooo00 == 50003 : O00oOOoOOOOO ( o0O0Oo00 )
elif O0OOO0OOooo00 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif O0OOO0OOooo00 == 60001 : iI1ii1Ii ( )
elif O0OOO0OOooo00 == 60002 : ooO ( I1i1i1iii )
elif O0OOO0OOooo00 == 60003 : iii ( oOooO0 )
elif O0OOO0OOooo00 == 60004 : iI111II1ii ( oOooO0 )
elif O0OOO0OOooo00 == 50004 : iiI1IIIi ( )
elif O0OOO0OOooo00 == 50005 : speedtest . runtest ( oOooO0 )
elif O0OOO0OOooo00 == 70001 : i1Ii11ii1I ( )
elif O0OOO0OOooo00 == 70002 : oOOo0OO00OoO ( oOooO0 )
elif O0OOO0OOooo00 == 70003 : oOOo0oO0oOOOo ( oOooO0 )
elif O0OOO0OOooo00 == 70004 : oo000Oo0 ( oOooO0 )
elif O0OOO0OOooo00 == 70005 : OoOOoo0o ( oOooO0 )
elif O0OOO0OOooo00 == 70006 : iIIii1i1Ii11 ( )
elif O0OOO0OOooo00 == 50006 : OOoO ( i1 , i1111 )
elif O0OOO0OOooo00 == 80000 : OOOO00OOO00 ( )
elif O0OOO0OOooo00 == 80001 : resolvefilmon ( oOooO0 )
elif O0OOO0OOooo00 == 80002 : i1oooOoOoOO ( )
elif O0OOO0OOooo00 == 80003 : O0Ooo0O ( I1i1i1iii , oOooO0 , "None" )
elif O0OOO0OOooo00 == 80004 : iii1 ( I1i1i1iii , oOooO0 )
elif O0OOO0OOooo00 == 80005 : OO0O00oOo ( )
elif O0OOO0OOooo00 == 80006 : IIiI1Ii1IIiI11i1 ( oOooO0 )
elif O0OOO0OOooo00 == 80007 : Ii11I1iIiiI ( oOooO0 )
elif O0OOO0OOooo00 == 80008 : O0o0OO00 ( )
elif O0OOO0OOooo00 == 80009 : II1i1iI ( )
elif O0OOO0OOooo00 == 80010 : iI111I1 ( oOooO0 )
elif O0OOO0OOooo00 == 80011 : ii1o0 ( oOooO0 )
elif O0OOO0OOooo00 == 80012 : iiIi1I ( )
elif O0OOO0OOooo00 == 90000 : I1ii11IiI1I ( I1i1i1iii , oOooO0 )
elif O0OOO0OOooo00 == 90001 : Iiiii1I ( )
elif O0OOO0OOooo00 == 90002 : I1iiiiIii ( )
elif O0OOO0OOooo00 == 90003 : i1iI1Ii1 ( oOooO0 )
elif O0OOO0OOooo00 == 90004 : oooOO0 ( oOooO0 )
elif O0OOO0OOooo00 == 90005 : o00oO00O0 ( oOooO0 )
elif O0OOO0OOooo00 == 90006 : IIII11 ( oOooO0 )
elif O0OOO0OOooo00 == 90007 : oOoOOO0 ( oOooO0 )
elif O0OOO0OOooo00 == 90008 : ooooooo0oOo0 ( oOooO0 )
elif O0OOO0OOooo00 == 90009 : IIII1iI1IiIiI ( oOooO0 )
elif O0OOO0OOooo00 == 90010 : OO0O000 ( )
elif O0OOO0OOooo00 == 90020 : Oo0ooo ( )
elif O0OOO0OOooo00 == 90021 : hellyeah2 ( oOooO0 )
elif O0OOO0OOooo00 == 90022 : hellyeah3 ( oOooO0 )
elif O0OOO0OOooo00 == 90023 : iIi1IiI ( )
elif O0OOO0OOooo00 == 90024 : I11iiIi1i1 ( oOooO0 )
elif O0OOO0OOooo00 == 90025 : i1iIiIi1I ( oOooO0 )
if 36 - 36: oO0o % IIiIiII11i * o0o00Oo0O + IIiIiII11i - o000O0o - ooOoO0O00
elif O0OOO0OOooo00 == 90030 : o0o0O0O00oOOo ( )
elif O0OOO0OOooo00 == 90031 : o000O0O ( )
elif O0OOO0OOooo00 == 90032 : I1111i ( oOooO0 )
elif O0OOO0OOooo00 == 90033 : o00O0O ( oOooO0 )
elif O0OOO0OOooo00 == 90034 : OOOIIiI1i1i ( oOooO0 )
elif O0OOO0OOooo00 == 90035 : IiII111i1i11 ( oOooO0 )
elif O0OOO0OOooo00 == 90036 : IIiI ( oOooO0 )
elif O0OOO0OOooo00 == 90039 : iI11IIiII1iII ( oOooO0 )
elif O0OOO0OOooo00 == 90037 : I11iIiI1 ( oOooO0 )
elif O0OOO0OOooo00 == 90038 : iIIIi1i1I11i ( )
if 53 - 53: ii1ii11IIIiiI - Ii1IIIi1
elif O0OOO0OOooo00 == 10090 : O00 ( )
elif O0OOO0OOooo00 == 10091 : IIi1i ( oOooO0 )
elif O0OOO0OOooo00 == 10092 : iii1i1Iiiiiii ( oOooO0 )
elif O0OOO0OOooo00 == 10093 : O0oOOo0 ( oOooO0 , IiI111ii1ii )
elif O0OOO0OOooo00 == 10094 : iiI1IiII1III1I11I1 ( oOooO0 , IiI111ii1ii )
if 75 - 75: O0OOOoOoo0 % o0o00Oo0O - ooOOOoO - Ii1I + oOo0O0Ooo - oOo0O0Ooo
elif O0OOO0OOooo00 == 10095 : IiIiIi ( )
elif O0OOO0OOooo00 == 10096 : i1IIi1i1Ii1 ( oOooO0 )
elif O0OOO0OOooo00 == 10097 : Oo ( oOooO0 )
elif O0OOO0OOooo00 == 10098 : O0oOo ( oOooO0 )
elif O0OOO0OOooo00 == 10099 : iIiIIi ( oOooO0 )
if 87 - 87: ooOoO0O00 % ii1ii11IIIiiI % ooOoO0O00 + iI11I1II1I1I
elif O0OOO0OOooo00 == 10200 : IiIiII1 ( )
elif O0OOO0OOooo00 == 10201 : i1I1iIi1IiI ( oOooO0 )
elif O0OOO0OOooo00 == 10202 : Oo0O ( oOooO0 )
elif O0OOO0OOooo00 == 10203 : RT4 ( oOooO0 )
if 23 - 23: iI11I1II1I1I * ooOOOoO . iiiiiiii1 - I11i
elif O0OOO0OOooo00 == 90040 : iI1iIiiiI1I1 ( )
elif O0OOO0OOooo00 == 90041 : i1I1II ( oOooO0 )
elif O0OOO0OOooo00 == 90042 : IIiIi1iI1iII ( oOooO0 )
elif O0OOO0OOooo00 == 90043 : i111i ( oOooO0 )
elif O0OOO0OOooo00 == 90044 : iI1i1iIi1iiII ( oOooO0 )
elif O0OOO0OOooo00 == 90045 : I1IIi1I ( )
elif O0OOO0OOooo00 == 90046 : o0OoO0000o ( oOooO0 )
elif O0OOO0OOooo00 == 90050 : oO00Ooo0oO ( )
elif O0OOO0OOooo00 == 90051 : IiIi1iI11 ( oOooO0 )
elif O0OOO0OOooo00 == 90052 : o0OO0O0OO0oO0 ( oOooO0 )
elif O0OOO0OOooo00 == 90053 : IIIiI1ii1IIi ( oOooO0 )
elif O0OOO0OOooo00 == 90054 : o0i1I11iI1iiI ( oOooO0 )
elif O0OOO0OOooo00 == 90055 : i1iI1i1I1 ( )
if 66 - 66: oOo0O0Ooo * iiiiiiii1 / Ii / Ii1IIIi1
elif O0OOO0OOooo00 == 100001 : Stand_up ( )
if 19 - 19: I11i1ii1 % iI11I1II1I1I * ii
elif O0OOO0OOooo00 == 100003 : Oooooooo0o ( oOooO0 )
elif O0OOO0OOooo00 == 100004 : o00oO ( oOooO0 )
elif O0OOO0OOooo00 == 100005 : Resolve ( oOooO0 )
elif O0OOO0OOooo00 == 100008 : Search ( )
elif O0OOO0OOooo00 == 100007 : ii111I11iI ( oOooO0 )
elif O0OOO0OOooo00 == 100009 : yt . PlayVideo ( oOooO0 )
elif O0OOO0OOooo00 == 100010 : i1iiIiI1Ii1i ( oOooO0 )
elif O0OOO0OOooo00 == 100100 : oO0OO0 ( IiI111ii1ii , oOooO0 , OOo )
elif O0OOO0OOooo00 == 100101 : i11i1iiI1i ( oOooO0 , I1i1i1iii , o0ooooO0o0O , OOo , IiI111ii1ii )
elif O0OOO0OOooo00 == 100102 : I1iIiI11I1 ( I1i1i1iii , oOooO0 , IiI111ii1ii , o0ooooO0o0O )
elif O0OOO0OOooo00 == 100106 : iI11I ( oOooO0 , I1i1i1iii )
elif O0OOO0OOooo00 == 100107 : ooIII1i1iI1 ( )
elif O0OOO0OOooo00 == 100108 : O0ooO0Oo0OO0o ( )
elif O0OOO0OOooo00 == 100109 : III11iO00 ( oOooO0 )
elif O0OOO0OOooo00 == 40000 : OO0Oo ( )
elif O0OOO0OOooo00 == 40001 : I1Ii11i ( oOooO0 )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
