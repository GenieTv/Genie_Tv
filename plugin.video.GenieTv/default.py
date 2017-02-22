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
IiiIII111iI = "3.4.3"
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
 if 7 - 7: IIiIiII11i + ii . iiiiiiii1 . I11i1ii1 - I11i
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
def II11 ( ) :
 i111I1 = [ '[COLOR' + II + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + II + ']APK TOOL[/COLOR]' , '[COLOR' + II + ']ADDONS[/COLOR]' , '[COLOR' + II + ']BUILDERS TOOLBOX[/COLOR]' , '[COLOR' + II + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + II + ']CONTACT US[/COLOR]' , '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + II + ']SOURCE LIST[/COLOR]' , '[COLOR' + II + ']GUIDE SKINS[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  Iiii1i1 ( )
 if iI11iI1IiiIiI == 1 :
  Ii1I1i ( )
 if iI11iI1IiiIiI == 2 :
  OOI1iI1ii1II ( )
 if iI11iI1IiiIiI == 3 :
  O0O0OOOOoo ( )
 if iI11iI1IiiIiI == 4 :
  oOooO0 ( Ii1I1Ii )
 if iI11iI1IiiIiI == 5 :
  OOooO0OOoo . ok ( i1 , i1111 )
 if iI11iI1IiiIiI == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if iI11iI1IiiIiI == 7 :
  OOoO0 ( )
 if iI11iI1IiiIiI == 8 :
  OO0Oooo0oOO0O ( )
def OO0Oooo0oOO0O ( ) :
 Ii1I1Ii = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( Ii1I1Ii , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
 I1iIIiiIIi1i ( Ii1I1Ii )
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
 Ii1I1Ii = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , 'GuideSkins' + '.zip' )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( Ii1I1Ii , oOO0O00Oo0O0o , o0oOoO00o )
 ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print ii1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , ii1 , o0oOoO00o )
 I1iIIiiIIi1i ( Ii1I1Ii )
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
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 90032 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
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
  for I1111i , Ii1I1Ii , iiO0oOo00o , o0ooooO0o0O in i1IIIII11I1IiI :
   OOiIiIIi1 ( I1111i , Ii1I1Ii , 50005 , iiO0oOo00o , o0ooooO0o0O , '' )
def iiIi11iI1iii ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + II + ']WIPE GENIE[/COLOR]' , '[COLOR' + II + ']Genie BUILDS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Wizard[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   oo000o0000oO ( )
  if iI11iI1IiiIiI == 1 :
   iI1i111I1Ii ( )
  if iI11iI1IiiIiI == 2 :
   i11i1ii1I ( o0OO0o0o00o )
  if iI11iI1IiiIiI == 3 :
   oOo0 ( Ii1I1Ii )
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
  iiOOooooO0Oo ( '[COLOR' + II + ']Genie On Demand Soaps[/COLOR]' , ( i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzL0cuTy5ELlMvZ29kcy5waHA=' ) ) , 100210 , III1iII1I1ii + 'gods.png' , O0o0Oo , '' )
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
  iiOOooooO0Oo ( '[COLOR' + II + ']Genie On Demand Soaps[/COLOR]' , ( i11 ( 'aHR0cDovL2F0bGFudGljMjgwLnN0YXJ0ZGVkaWNhdGVkLm5ldC9ib3NzL0cuTy5ELlMvZ29kcy5waHA=' ) ) , 100210 , III1iII1I1ii + 'gods.png' , O0o0Oo , '' )
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
 i111I1 = [ '[COLOR' + II + ']FOOTBALL[/COLOR]' , '[COLOR' + II + ']KIDS[/COLOR]' , '[COLOR' + II + ']NEWS[/COLOR]' , '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + II + ']HOBBIES[/COLOR]' , '[COLOR' + II + ']STAND UP[/COLOR]' , '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']CATEGORIES[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  iIiIiIiI ( )
 if iI11iI1IiiIiI == 1 :
  i11OOoo ( )
 if iI11iI1IiiIiI == 2 :
  iIIiiiI ( )
 if iI11iI1IiiIiI == 3 :
  oo0 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , IiI111ii1ii , I1111i )
 if iI11iI1IiiIiI == 4 :
  O0OOo ( )
 if iI11iI1IiiIiI == 5 :
  IiIII1 ( )
 if iI11iI1IiiIiI == 6 :
  O0Oo000 ( )
 if iI11iI1IiiIiI == 7 :
  iiI11i1II ( )
 if iI11iI1IiiIiI == 8 :
  OO0O0OOo0O ( )
  if 36 - 36: I11i1ii1 . I1ii11iIi11i % I11i1ii1 % oO0o
  if 2 - 2: I11i - Ii1I
def ii1Ii11I ( ) :
 if not os . path . exists ( IIIII ) :
  OO0O000 ( 'Change Log 22/2/17 - v3.4.3' , 'GenieTv Now Krypton Compatible,[CR] G.O.D.S (GenieTv On Demand Soaps) Added To GenieTv,[CR] More Sections Now Available For Download Including Kids,[CR] Tv Guide Removed And Replaced By External App,[CR] Boss Documentaries A Masterpiece By Jason Cadd,[CR] Updates To All Searches,[CR] StreamTeam Cleaned Up,[CR] Addon Overall CleanUp,[CR] General Maintence' )
  os . makedirs ( IIIII )
  if 58 - 58: ii1ii11IIIiiI + I11i - oOo0O0Ooo
  if 3 - 3: oO0o
def oooOoOOO0oo0o ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   Oo0oooO0oO ( )
  if iI11iI1IiiIiI == 1 :
   IiIiII1 ( )
  if iI11iI1IiiIiI == 2 :
   Iii1iiIi1II ( Ii1I1Ii )
  if iI11iI1IiiIiI == 3 :
   OO0O00oOo ( )
  if iI11iI1IiiIiI == 4 :
   ii1II ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if iI11iI1IiiIiI == 5 :
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
  i111I1 = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']THE SOURCE[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']RETURN DATES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   I1ii1 ( )
  if iI11iI1IiiIiI == 1 :
   O00 ( )
  if iI11iI1IiiIiI == 2 :
   Oo0o0000OOoO ( )
  if iI11iI1IiiIiI == 3 :
   IiIi1I1ii111 ( )
  if iI11iI1IiiIiI == 4 :
   IiIiIi ( )
  if iI11iI1IiiIiI == 5 :
   IIIII1 ( )
  if iI11iI1IiiIiI == 6 :
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
  i111I1 = [ o0o0oOoOO0O , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + II + ']RAIZ TV[/COLOR]' , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   Oo0OO0000oooo ( )
  if iI11iI1IiiIiI == 1 :
   oo0 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , IiI111ii1ii , I1111i )
   if 7 - 7: o000O0o - oO0o - o0o00Oo0O % o000O0o - IIiIiII11i
   if 31 - 31: O0OOOoOoo0 / I1ii11iIi11i - O0OOOoOoo0 - Ii1IIIi1
   if 7 - 7: O0OOOoOoo0 % o0o00Oo0O . OOooOOo + oOo0O0Ooo - ooOOOoO
  if iI11iI1IiiIiI == 2 :
   oo0 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , IiI111ii1ii , I1111i )
   if 75 - 75: ooOOOoO
   if 71 - 71: I11i1ii1
  if iI11iI1IiiIiI == 3 :
   oo0 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , IiI111ii1ii , I1111i )
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
 iIIII = o0O0O0ooo0oOO ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( iIIII )
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
 for I1111i , url , O0OOO0OOooo00 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o in i1IIIII11I1IiI :
  if I111iIi1 == '123' :
   I111iIi1 = III1iII1I1ii + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = III1iII1I1ii + 'appstreams.png'
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100010 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o )
  elif not 'http' in url :
   OOo00OoO ( I1111i , url , 100009 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o , '' )
  else :
   OOo00OoO ( I1111i , url , 100005 , I111iIi1 , o0ooooO0o0O , oo00O00oO000o , '' )
   if 10 - 10: I11i / Ii
def o00oO ( url ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 O00O0Ooooo00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , oo00O00oO000o , o0ooooO0o0O , I1111i in O00O0Ooooo00 :
  if o00O0O == '123' :
   o00O0O = III1iII1I1ii + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = O0o0Oo
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100004 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
  elif not 'http' in url :
   OOo00OoO ( I1111i , url , 100009 , o00O0O , o0ooooO0o0O , oo00O00oO000o , '' )
  else :
   OOo00OoO ( I1111i , url , 100005 , o00O0O , o0ooooO0o0O , oo00O00oO000o , '' )
   if 97 - 97: I11i1ii1 / iiiiiiii1 % ooOoO0O00 % Ii1I
def ii111I11iI ( url ) :
 if 93 - 93: Ii1I / iI11I1II1I1I * ooOoO0O00 % ii * o0o00Oo0O * ooOOOoO
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 Ooooooo = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1IIIiI1I1ii1 in Ooooooo :
  I111iIi1 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for I111iIi1 in I111iIi1 :
   I111iIi1 = I111iIi1
  I1111i = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for I1111i in I1111i :
   if 'elete' in I1111i :
    pass
   elif 'rivate Vid' in I1111i :
    pass
   else :
    I1111i = ( I1111i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  iiiI1I1iIIIi1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for iiiI1I1iIIIi1 in iiiI1I1iIIIi1 :
   iiiI1I1iIIIi1 = iiiI1I1iIIIi1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for url in url :
   url = url
  OOo00OoO ( '[COLORred]' + str ( iiiI1I1iIIIi1 ) + '[/COLOR] : ' + str ( I1111i ) , str ( url ) , 100009 , str ( I111iIi1 ) , O0o0Oo , '' , '' )
  I1I11i ( 'movies' , '' )
  if 17 - 17: iI11I1II1I1I . ii / ooOOOoO % IIiIiII11i % ooOoO0O00 / Ii
  if 58 - 58: I1ii11iIi11i . IIiIiII11i + o000O0o - Ii / IIiIiII11i / o0o00Oo0O
  if 85 - 85: OOooOOo + Ii1IIIi1
  if 10 - 10: I1111IIi / oO0o + OOooOOo / ooOoO0O00
def i1iII1II11I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 O00O0Ooooo00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , oo00O00oO000o , o0ooooO0o0O , I1111i in O00O0Ooooo00 :
  if '.php' in url :
   iiOOooooO0Oo ( I1111i , url , 100210 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
  else :
   OOiIiIIi1 ( I1111i , url , 222 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
   if 54 - 54: I1111IIi + o0o00Oo0O + ooOOOoO * iiiiiiii1 - Ii1IIIi1 % o000O0o
   if 13 - 13: I11i1ii1 / O0OOOoOoo0 * oO0o . oO0o * I11i1ii1
   if 63 - 63: iiiiiiii1 / o0o00Oo0O * I1ii11iIi11i + IIiIiII11i / I1111IIi + ii1ii11IIIiiI
def OOoO000 ( iconimage , url , extra ) :
 I111iIi1 = ' '
 oOOOO = ' '
 o0ooooO0o0O = ' '
 IiIi1ii111i1 = ' '
 i1i1i1I = i1iIiiiiii1II ( url )
 I111iIi1 = re . compile ( '<img src="(.+?)">' ) . findall ( i1i1i1I )
 for I111iIi1 in I111iIi1 :
  I111iIi1 = I111iIi1
 oOoo000 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( i1i1i1I )
 for o0ooooO0o0O in oOoo000 :
  o0ooooO0o0O = o0ooooO0o0O
 i1IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( i1i1i1I )
 for url , IiIi1ii111i1 in i1IIIII11I1IiI :
  IiIi1ii111i1 = 'S' + ( IiIi1ii111i1 ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oO0Oo + url
  OooOo00o ( ( IiIi1ii111i1 ) . replace ( '  ' , '' ) , url , 100101 , I111iIi1 , o0ooooO0o0O , oOOOO , '' )
  I1I11i ( 'Movies' , 'info' )
  if 20 - 20: ooOoO0O00 * iiiiiiii1 + IIiIiII11i % I11i % o000O0o
def iIi1II ( url , name , fanart , extra , iconimage ) :
 I1iIiI11I1 = extra
 IiIi1ii111i1 = name
 i1i1i1I = i1iIiiiiii1II ( url )
 I111iIi1 = iconimage
 i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( i1i1i1I )
 for url , name , i1oOOoo0o0OOOO in i1IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oO0Oo + url
  i1oOOoo0o0OOOO = i1oOOoo0o0OOOO
  i1IiII1III = name + ' - [COLORred]' + i1oOOoo0o0OOOO + '[/COLOR]'
  OooOo00o ( i1IiII1III , url , 100102 , I111iIi1 , fanart , 'Aired : ' + i1oOOoo0o0OOOO , i1IiII1III )
  if 30 - 30: o0o00Oo0O
def Oo00oo0000OO ( name , URL , iconimage , fanart ) :
 oO0OOoo0OO = i1iIiiiiii1II ( URL )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , name in i1IIIII11I1IiI :
  for i11I in oOOoo0Oo :
   if i11I in Ii1I1Ii :
    URL = 'http://www.watchseriesgo.to/link/' + Ii1I1Ii
    OOo00OoO ( name , URL , 100106 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( i1IIIII11I1IiI ) <= 0 :
  OooOo00o ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 69 - 69: I11i1ii1 - oO0o / Ii + Ii1I % ii
  if 73 - 73: ii1ii11IIIiiI - iiiiiiii1
def O00oooo00o0O ( url , name ) :
 ii1iii1I1I = name
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  oO0Ooo0ooOO0 ( url , ii1iii1I1I )
 for url in i1I :
  oO0Ooo0ooOO0 ( url , ii1iii1I1I )
 for url in ooOoO00 :
  oO0Ooo0ooOO0 ( url , ii1iii1I1I )
  if 46 - 46: ii1ii11IIIiiI % OOooOOo
def oO0Ooo0ooOO0 ( url , season_name ) :
 if 'daclips.in' in url :
  ooo0o0O0o ( url , season_name )
 elif 'filehoot.com' in url :
  O0OooO ( url , season_name )
 elif 'allmyvideos.net' in url :
  ii1Ii1IiIIi ( url , season_name )
 elif 'vidspot.net' in url :
  o0OO0 ( url , season_name )
 elif 'vodlocker' in url :
  oOo00Oo0o0Oo ( url , season_name )
 elif 'vidto' in url :
  I1 ( url , season_name )
  if 26 - 26: I11i1ii1 . Ii1IIIi1 - Ii1IIIi1 . oO0o
  if 39 - 39: ii + o000O0o % Ii1IIIi1 / Ii1IIIi1
def I1 ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iooo , I1111i in i1IIIII11I1IiI :
  ii1iiIi1 ( I1iooo , season_name )
  if 34 - 34: Ii1IIIi1
  if 91 - 91: iI11I1II1I1I % I11i . iI11I1II1I1I % ooOoO0O00 / IIiIiII11i * OOooOOo
def ii1Ii1IiIIi ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iooo , I1111i in i1IIIII11I1IiI :
  ii1iiIi1 ( I1iooo , season_name )
  if 10 - 10: IIiIiII11i . O0OOOoOoo0
def o0OO0 ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0OOoo0OO )
 for I1iooo , I1111i in i1IIIII11I1IiI :
  ii1iiIi1 ( I1iooo , season_name )
  if 32 - 32: ii1ii11IIIiiI . I1111IIi . ii - oO0o + o000O0o
def oOo00Oo0o0Oo ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iooo in i1IIIII11I1IiI :
  ii1iiIi1 ( I1iooo , season_name )
  if 88 - 88: O0OOOoOoo0
def ooo0o0O0o ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0OOoo0OO )
 for I1iooo in i1IIIII11I1IiI :
  ii1iiIi1 ( I1iooo , season_name )
  if 19 - 19: IIiIiII11i * I1111IIi + ii1ii11IIIiiI
def O0OooO ( url , season_name ) :
 oO0OOoo0OO = i1iIiiiiii1II ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iooo in i1IIIII11I1IiI :
  ii1iiIi1 ( I1iooo , season_name )
  if 65 - 65: Ii1IIIi1 . iiiiiiii1 . oO0o . O0OOOoOoo0 - Ii1IIIi1
def ii1iiIi1 ( Link , season_name ) :
 if 'http:/' in Link :
  ii111i ( Link )
  if 93 - 93: oO0o
def i111I ( url ) :
 oO0OOoo0OO = OPEN_URL_1 ( url )
 OOO0oOoO0O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 for url in OOO0oOoO0O :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 84 - 84: o0o00Oo0O * ii - I1111IIi * I1111IIi
def OooOo00o ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 i1ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0O = True
 oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iiiIIiIi = [ ]
  if 68 - 68: o0o00Oo0O + OOooOOo / o000O0o - Ii1IIIi1 + iI11I1II1I1I % ii1ii11IIIiiI
  if showcontext == 'fav' :
   iiiIIiIi . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   iiiIIiIi . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oOO . addContextMenuItems ( iiiIIiIi )
 oO0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = True )
 return oO0O
 if 23 - 23: I11i1ii1 % I11i / ooOOOoO
 if 5 - 5: iI11I1II1I1I
def OOo00OoO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 i1ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0O = True
 oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iiiIIiIi = [ ]
  iiiIIiIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iiiIIiIi . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   iiiIIiIi . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oOO . addContextMenuItems ( iiiIIiIi )
 oO0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = False )
 return oO0O
 if 72 - 72: o000O0o . iiiiiiii1 / OOooOOo + ooOOOoO % iI11I1II1I1I
def II1II1iIIi11 ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 49 - 49: ii * ooOOOoO - I1ii11iIi11i . o000O0o
def O000o0 ( url ) :
 oO0o000OoOoO0 = xbmc . Player ( OO0ooOOO0O00o ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0o000OoOoO0 . play ( url ) . strip ( )
 except : pass
 if 85 - 85: Ii - Ii1IIIi1 . ii1ii11IIIiiI / IIiIiII11i . IIiIiII11i
def ii111i ( url ) :
 oO0o000OoOoO0 = xbmc . Player ( )
 import urlresolver
 try : oO0o000OoOoO0 . play ( url )
 except : pass
 if 84 - 84: ii1ii11IIIiiI / O0OOOoOoo0 . I1111IIi . I1111IIi % ooOOOoO
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
  if 57 - 57: ii1ii11IIIiiI % IIiIiII11i
  if 67 - 67: I11i1ii1 + oOo0O0Ooo * Ii - o000O0o / I1111IIi % O0OOOoOoo0
  if 92 - 92: ii1ii11IIIiiI - o000O0o - I11i1ii1 % ii / Ii1IIIi1
def i11OOoo ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iIIIiIii ( )
  if iI11iI1IiiIiI == 1 :
   ooo ( )
  if iI11iI1IiiIiI == 2 :
   OOOO0oooo ( )
  if iI11iI1IiiIiI == 3 :
   oooooOo0 ( )
  if iI11iI1IiiIiI == 4 :
   O0o0O0OO00o ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
 if 92 - 92: I11i + iiiiiiii1 / I1ii11iIi11i % oO0o % I1111IIi . ii
 if 52 - 52: I11i1ii1 / Ii - Ii1IIIi1 . I1111IIi % iI11I1II1I1I + I11i
 if 71 - 71: o000O0o % ooOOOoO * OOooOOo . o0o00Oo0O / ii1ii11IIIiiI . Ii1I
def OO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 i1IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0OOoo0OO )
 for IIiIi1iI in i1IIIII11I1IiI :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   oOOOo = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   OO0O000 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + oOOOo + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iI11iI1IiiIiI = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iI11iI1IiiIiI == 0 :
    OO0O0o0o0 ( IIiIi1iI )
    O0O0ooOOO ( )
   elif iI11iI1IiiIiI == 1 :
    iIIIIIiI1I1 ( IIiIi1iI )
  else :
   pass
   if 15 - 15: ii1ii11IIIiiI * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
def iIIIIIiI1I1 ( addon ) :
 oOOOo = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 60 - 60: oOo0O0Ooo * iiiiiiii1 % oO0o + o000O0o
def OO0O0o0o0 ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 o0oo = os . path . join ( I11II1i , 'default.py' )
 O00OOooo0Ooo = open ( o0oo , "w+" )
 if 66 - 66: o000O0o
 O00OOooo0Ooo . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 O00OOooo0Ooo . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 O00OOooo0Ooo . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 91 - 91: o000O0o + oOo0O0Ooo
 if 59 - 59: oOo0O0Ooo + Ii + ooOoO0O00 / ooOOOoO
 if 44 - 44: ooOOOoO . OOooOOo * oOo0O0Ooo + ii - O0OOOoOoo0 - I1111IIi
 if 15 - 15: I1111IIi / o0o00Oo0O . I11i . Ii
def o0OO0O0Oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OOOOO = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OOoOOo0O00O = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 Iii1I1111ii = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iiIii1I = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url , iiO0oOo00o , o0ooooO0o0O , oo00O00oO000o in OOOOO :
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 90037 , iiO0oOo00o , o0ooooO0o0O , oo00O00oO000o )
  elif I1111i == 'Search' :
   iiOOooooO0Oo ( 'Search' , url , 90038 , iiO0oOo00o , o0ooooO0o0O , oo00O00oO000o )
  else :
   OOiIiIIi1 ( I1111i , url , 222 , iiO0oOo00o , o0ooooO0o0O , oo00O00oO000o )
 for I1111i , o00O0O , url , i1I11iIiII in OOoOOo0O00O :
  iiOOooooO0Oo ( I1111i , url , 90037 , o00O0O , i1I11iIiII , '' )
 for I1111i , o00O0O , url , i1I11iIiII in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 90037 , o00O0O , i1I11iIiII , '' )
 for I1111i , url , o00O0O , i1I11iIiII in i1I :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , i1I11iIiII , '' )
 for I1111i , url , o00O0O , i1I11iIiII in ooOoO00 :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , i1I11iIiII , '' )
 for I1111i , url , o00O0O , i1I11iIiII in Iii1I1111ii :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , i1I11iIiII , '' )
 for I1111i , url , o00O0O in iiIii1I :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , '' , '' )
  I1I11i ( 'tvshows' , 'Media Info 3' )
  if 66 - 66: I1ii11iIi11i - I11i * I1111IIi + OOooOOo + I11i - iI11I1II1I1I
def iiiI1ii11 ( ) :
 ii1i = [ 'serialsearch' , 'moviesearch' ]
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 if oo0OO == '' :
  pass
 else :
  for IiiI11i1I in ii1i :
   OOo0 = I11 + IiiI11i1I + '.php'
   i1i1i1I = OoOooO ( OOo0 )
   if i1i1i1I != 'Opened' :
    O00O0Ooooo00 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( i1i1i1I )
    for I1111i , Ii1I1Ii , iiO0oOo00o , o0ooooO0o0O , oo00O00oO000o in O00O0Ooooo00 :
     if oo0OO in I1111i . lower ( ) :
      iiIii1IIi = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for i11I in iiIii1IIi :
       if i11I == Ii1I1Ii :
        I1111i = '[COLORred]* [/COLOR]' + ( I1111i ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        ii1IiIiI1 = open ( o00OO00OoO , "a" )
        ii1IiIiI1 . write ( 'item="' + I1111i + '"\n' )
        ii1IiIiI1 . close
      if 'php' in Ii1I1Ii :
       iiOOooooO0Oo ( I1111i , Ii1I1Ii , 90037 , iiO0oOo00o , o0ooooO0o0O , oo00O00oO000o )
      else :
       OOiIiIIi1 ( I1111i , Ii1I1Ii , 222 , iiO0oOo00o , o0ooooO0o0O , oo00O00oO000o )
       if 90 - 90: I11i - Ii + ooOoO0O00 - ii1ii11IIIiiI % I1ii11iIi11i
   I1I11i ( 'tvshows' , 'Media Info 3' )
   if 59 - 59: Ii1IIIi1 % iI11I1II1I1I . ooOoO0O00 + IIiIiII11i * I1111IIi
def i1IiiI1iIi ( ) :
 oO0OOoo0OO = OoOooO ( 'http://www.tvcatchup.com/channels/' )
 O0 = OoOooO ( 'http://www.djing.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oOOo00O0OOOo = re . compile ( 'title="([^"]*)" >.+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( O0 )
 for IIiiiiiiIi1I1 , o00O0O , Ii1I1Ii in i1IIIII11I1IiI :
  i1i1iII1 ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + Ii1I1Ii , 90024 , 'http://www.tvcatchup.com' + o00O0O )
 for IIiiiiiiIi1I1 , Ii1I1Ii , o00O0O in oOOo00O0OOOo :
  i1i1iII1 ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + Ii1I1Ii , 90024 , o00O0O )
 for Ii1I1Ii , o00O0O , I1111i in i1I :
  if 'Submit' in I1111i :
   pass
  elif '&lt;' in I1111i :
   pass
  else :
   OOiIiIIi1 ( 'DJing  ' + I1111i , Ii1I1Ii , 90025 , 'http://www.djing.com' + o00O0O , O0o0Oo , '' )
  I1I11i ( 'movies' , 'MAIN' )
def i11I1I1iiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 if 34 - 34: ooOOOoO % I11i1ii1 . o0o00Oo0O . iI11I1II1I1I
 i1IIIII11I1IiI = re . compile ( "file: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def ooi1II1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOoO0ooOO ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 24 - 24: ooOoO0O00 . Ii
def IiIiII1 ( ) :
 if 16 - 16: I1ii11iIi11i % Ii1I + ooOOOoO - o0o00Oo0O . O0OOOoOoo0 / iiiiiiii1
 if 35 - 35: o000O0o / iiiiiiii1 / IIiIiII11i - iI11I1II1I1I + IIiIiII11i . iiiiiiii1
 if 81 - 81: O0OOOoOoo0 * Ii1IIIi1 - Ii1I * ii1ii11IIIiiI % OOooOOo * OOooOOo
 if 59 - 59: iI11I1II1I1I
 if 7 - 7: Ii1IIIi1 * oOo0O0Ooo / I11i * Ii
 if 84 - 84: Ii1IIIi1 . O0OOOoOoo0
 oO0OOoo0OO = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'yr' in Ii1I1Ii :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + Ii1I1Ii , 10201 , III1iII1I1ii + 'rated.png' )
   if 8 - 8: I1ii11iIi11i + IIiIiII11i * Ii1IIIi1 * OOooOOo * ooOOOoO / I1111IIi
def iIii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OO0OoOOO0 , url , I1111i in i1IIIII11I1IiI :
  if 'id' in url :
   Iiiiii111i1ii ( ( '[COLORred]RANK [COLORblue]' + OO0OoOOO0 + '[COLORred] - [COLORblue]' + I1111i + '[/COLOR]' ) , I1111i , 10202 , III1iII1I1ii + 'rated.png' )
   if 90 - 90: I11i1ii1 + IIiIiII11i * Ii1I / ii1ii11IIIiiI . I11i + I11i
def I11I ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oOoO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIi = ( url )
 oo0OO = IIi . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( IIi ) . replace ( ' ' , '+' )
 OoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 IIII = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iI1iiiIiii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 ii1i1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 II11iIII1i1I = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOO0oo = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IIi
 IiIIi1I1I11Ii = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 o0OO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 58 - 58: ii . oOo0O0Ooo / IIiIiII11i / IIiIiII11i - I1111IIi + I1ii11iIi11i
 Ooo0O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 ooo0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 55 - 55: I1ii11iIi11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( OoO )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( IIII )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( iI1iiiIiii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 ooO0o = O0o0O00Oo0o0 ( ii1i1i )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 ii1iI1iI1 = O0o0O00Oo0o0 ( oOO0oo )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 o00oOOO = O0o0O00Oo0o0 ( IiIIi1I1I11Ii )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 OoOO0OOoo = O0o0O00Oo0o0 ( o0OO )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 1 - 1: oOo0O0Ooo * Ii + iiiiiiii1 * Ii + oO0o
 if 30 - 30: I1ii11iIi11i . oO0o
 o0Oii1111i = O0o0O00Oo0o0 ( Ooo0O0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 O0ooOO = O0o0O00Oo0o0 ( ooo0 )
 if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
 if 72 - 72: ii / oOo0O0Ooo + ii1ii11IIIiiI / OOooOOo * ii1ii11IIIiiI
 if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + O0OOOoOoo0 * iI11I1II1I1I % ii1ii11IIIiiI
 if 25 - 25: ooOOOoO + OOooOOo . I11i % OOooOOo * Ii1IIIi1
 if 32 - 32: Ii - iiiiiiii1
 if 53 - 53: ii - I1111IIi
 if 87 - 87: o000O0o . oOo0O0Ooo
 if 17 - 17: ii1ii11IIIiiI . Ii
 if 5 - 5: Ii1I + o0o00Oo0O + o0o00Oo0O . iiiiiiii1 - I11i1ii1
 if 63 - 63: o000O0o
 if 71 - 71: ooOoO0O00 . ii1ii11IIIiiI * O0OOOoOoo0 % ii + Ii1IIIi1
 if 36 - 36: I1111IIi
 if 49 - 49: Ii1IIIi1 / ii / oOo0O0Ooo
 if OoOO0OOoo != 'Failed' :
  o0OooooOoOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( OoOO0OOoo )
  for url , I1111i in o0OooooOoOO :
   i1i1IIIIIIIi = O0o0O00Oo0o0 ( url )
   oo0o0oOo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( i1i1IIIIIIIi )
   for OO0oOOo0o , I1III11iiii11i1 in oo0o0oOo :
    I1III11iiii11i1 = ( I1III11iiii11i1 . replace ( '.' , ' ' ) )
    if oo0OO in I1III11iiii11i1 . lower ( ) :
     if '.mkv' in OO0oOOo0o :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + OO0oOOo0o , 222 , '' , '' , '' )
     elif '.mp4' in OO0oOOo0o :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + OO0oOOo0o , 222 , '' , '' , '' )
     elif '.avi' in OO0oOOo0o :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + OO0oOOo0o , 222 , '' , '' , '' )
     elif '.wav' in OO0oOOo0o :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + OO0oOOo0o , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + OO0oOOo0o , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 54 - 54: ooOoO0O00 - o000O0o
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for url , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in i1I :
   if IIi in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 18 - 18: iI11I1II1I1I + I1ii11iIi11i - Ii1IIIi1 + ii * ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 41 - 41: I11i1ii1 . I1ii11iIi11i + oOo0O0Ooo
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for o0O0OO , I1111i in ooOoO00 :
   if IIi in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IIII + o0O0OO ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for url , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in Iii1I1111ii :
   if IIi in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 22 - 22: IIiIiII11i * oO0o * ooOOOoO + Ii1I * I11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if ooO0o != 'Failed' :
  oo0o0 = [ ]
  iiIii1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO0o )
  for url , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in iiIii1I :
   if IIi in I1111i . lower ( ) :
    if I1111i in oo0o0 :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
     oo0o0 . append ( I1111i )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if ii1iI1iI1 != 'Failed' :
  oO0ooOoO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( ii1iI1iI1 )
  for url , o00O0O , I1111i in oO0ooOoO :
   if IIi in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 59 - 59: o0o00Oo0O % I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 92 - 92: ii1ii11IIIiiI % O0OOOoOoo0 / Ii1I % Ii1I * oOo0O0Ooo
    if 74 - 74: o0o00Oo0O . oOo0O0Ooo % oO0o % I1111IIi
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
    if 67 - 67: ii
    if 29 - 29: o0o00Oo0O - Ii - IIiIiII11i + Ii1IIIi1 * I1111IIi
    if 2 - 2: ooOoO0O00 - I11i1ii1 + oOo0O0Ooo . I11i * I11i / OOooOOo
    if 93 - 93: ooOoO0O00
 if o0Oii1111i != 'Failed' :
  ooOOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0Oii1111i )
  for url , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in ooOOOo :
   if IIi in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 98 - 98: o000O0o % I1111IIi * Ii % Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 29 - 29: I1111IIi
    if 66 - 66: I1ii11iIi11i
    if 97 - 97: ooOoO0O00 - ii / iiiiiiii1 * oOo0O0Ooo
    if 55 - 55: I11i . O0OOOoOoo0
    if 87 - 87: I11i % iI11I1II1I1I
    if 100 - 100: iiiiiiii1 . oOo0O0Ooo * iiiiiiii1 - oOo0O0Ooo . ooOOOoO * ii1ii11IIIiiI
    if 89 - 89: oO0o + I1111IIi * iiiiiiii1
    if 28 - 28: ii . o000O0o % Ii1I / ooOoO0O00 / Ii1IIIi1
    if 36 - 36: I11i + ooOOOoO - I1111IIi + iI11I1II1I1I + ii
    if 4 - 4: IIiIiII11i . ooOOOoO + ii1ii11IIIiiI * iiiiiiii1 . I11i1ii1
 oOoOo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 74 - 74: o000O0o / Ii1I % I11i
 for IiiI11i1I in oOoOo :
  OOo0 = O0Oo000ooO00 + IiiI11i1I + I1IIIii
  OoOO0OOoo = O0o0O00Oo0o0 ( OOo0 )
  if OoOO0OOoo != 'Failed' :
   o0OooooOoOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOO0OOoo )
   for url , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in o0OooooOoOO :
    if IIi in I1111i . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 88 - 88: OOooOOo - Ii % I11i * ooOOOoO + Ii1I
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 52 - 52: IIiIiII11i . oOo0O0Ooo + OOooOOo % oO0o
 oOoOo = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 62 - 62: I11i
 if 15 - 15: ooOOOoO + ii1ii11IIIiiI . Ii1IIIi1 * oO0o . OOooOOo
 for IiiI11i1I in oOoOo :
  OOo0 = oOoO + IiiI11i1I
  IiIi1111ii = O0o0O00Oo0o0 ( OOo0 )
  if IiIi1111ii != 'Failed' :
   iI1I1II1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( IiIi1111ii )
   for o0O0OO , I1111i in iI1I1II1 :
    if IIi in I1111i . lower ( ) :
     i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oOoO + IiiI11i1I + o0O0OO ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 92 - 92: ii - ii * oO0o % oOo0O0Ooo
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: iI11I1II1I1I - ooOoO0O00 . o000O0o
def IiIiIi ( ) :
 Iiiiii111i1ii ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , III1iII1I1ii + 'running.png' )
 Iiiiii111i1ii ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , III1iII1I1ii + 'countdown.png' )
 Iiiiii111i1ii ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , III1iII1I1ii + 'unknown.png' )
 Iiiiii111i1ii ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , III1iII1I1ii + 'cancelled.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 26 - 26: I11i * I1111IIi . ooOoO0O00
def ooOoOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , IiIi1ii111i1 , Oo , i1oOOoo0o0OOOO , o00o0oOo0O0O in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLORblue]' + I1111i + '[/COLOR] [COLORred]Season[/COLOR]-' + IiIi1ii111i1 + ' [COLORred]Returns [/COLOR]- ' + o00o0oOo0O0O + ' ' + i1oOOoo0o0OOOO ) , I1111i , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 79 - 79: Ii1I + iiiiiiii1
def iIiIIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , IiIi1ii111i1 , Oo in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLORblue]' + I1111i + '[/COLOR] [COLORred]Season[/COLOR]-' + IiIi1ii111i1 + ' [COLORred] Status Unknown[/COLOR] ' ) , I1111i , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 14 - 14: I11i / Ii1IIIi1 - iI11I1II1I1I - o000O0o % I11i1ii1
def I1iIiI1IiIIII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , IiIi1ii111i1 , Oo , i1oOOoo0o0OOOO in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLORblue]' + I1111i + ' [COLORred] Cancelled On[/COLOR] ' + i1oOOoo0o0OOOO ) , I1111i , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 18 - 18: I11i1ii1 % Ii . iI11I1II1I1I - O0OOOoOoo0
def OOOOoo ( url ) :
 IIi = ( url )
 oo0OO = IIi . lower ( )
 if 29 - 29: I11i / Ii / oOo0O0Ooo % o000O0o % Ii
 if 18 - 18: Ii1IIIi1 + iiiiiiii1
 OO0oOOo0o = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( IIi ) . replace ( ' ' , '+' )
 OoO = 'http://onlinemovies.tube/?s=' + ( IIi ) . replace ( ' ' , '+' )
 IIII = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 iI1iiiIiii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 II11iIII1i1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 80 - 80: o000O0o + I11i * ii1ii11IIIiiI + oO0o
 IiIIi1I1I11Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 o0OO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 O0oOo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 69 - 69: I1ii11iIi11i * IIiIiII11i * I11i1ii1 . O0OOOoOoo0 - Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 39 - 39: ii1ii11IIIiiI * oOo0O0Ooo % oO0o . OOooOOo
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 24 - 24: ooOoO0O00 * iI11I1II1I1I / ii1ii11IIIiiI
 if 78 - 78: Ii + I11i + iiiiiiii1 / I11i % iI11I1II1I1I % I1111IIi
 Oo0O0Oo00O = O0o0O00Oo0o0 ( OO0oOOo0o )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( OoO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( IIII )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( iI1iiiIiii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 IiIi1111ii = O0o0O00Oo0o0 ( II11iIII1i1I )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 9 - 9: I11i . oOo0O0Ooo - Ii1I
 if 32 - 32: ii / oOo0O0Ooo / iI11I1II1I1I + IIiIiII11i . o000O0o . I11i
 o00oOOO = O0o0O00Oo0o0 ( IiIIi1I1I11Ii )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 OoOO0OOoo = O0o0O00Oo0o0 ( o0OO )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 ii1ii = O0o0O00Oo0o0 ( O0oOo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
 if OoOO0OOoo != 'Failed' :
  o0OooooOoOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( OoOO0OOoo )
  for url , I1111i in o0OooooOoOO :
   i1i1IIIIIIIi = O0o0O00Oo0o0 ( url )
   oo0o0oOo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( i1i1IIIIIIIi )
   for OO0oOOo0o , I1III11iiii11i1 in oo0o0oOo :
    if oo0OO in I1III11iiii11i1 . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , url + OO0oOOo0o , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 43 - 43: Ii1I - O0OOOoOoo0
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if o00oOOO != 'Failed' :
  O000O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00oOOO )
  for url , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in O000O :
   if oo0OO in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 98 - 98: iI11I1II1I1I + iiiiiiii1 % OOooOOo + ooOOOoO % OOooOOo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 24 - 24: o000O0o * iiiiiiii1
    if 40 - 40: ii1ii11IIIiiI - OOooOOo * OOooOOo . OOooOOo + ii
    if 77 - 77: iI11I1II1I1I . ii1ii11IIIiiI % o000O0o / ii1ii11IIIiiI
    if 54 - 54: o000O0o + I11i1ii1 - I1ii11iIi11i
    if 35 - 35: ii1ii11IIIiiI - ii1ii11IIIiiI + ooOoO0O00 - o0o00Oo0O - iiiiiiii1
    if 58 - 58: OOooOOo - O0OOOoOoo0 - ii
    if 96 - 96: iI11I1II1I1I
    if 82 - 82: OOooOOo + o0o00Oo0O - I1111IIi % o000O0o * Ii
    if 15 - 15: I11i
    if 39 - 39: Ii1IIIi1 / Ii1I / oOo0O0Ooo * iiiiiiii1
    if 44 - 44: o0o00Oo0O + I11i1ii1 . iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - ooOOOoO
 if ii1ii != 'Failed' :
  o0o0OoOOOOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ii1ii )
  for url , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in o0o0OoOOOOOo :
   if oo0OO in I1111i . lower ( ) :
    Iiiiii111i1ii ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , IiI111ii1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 39 - 39: ii * Ii1IIIi1 * o0o00Oo0O . ooOOOoO . oO0o + I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  II1IIi = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for url , o00O0O , I1111i , OOoOO0o in i1I :
   if oo0OO in I1111i . lower ( ) :
    if 'season' in OOoOO0o :
     Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , o00O0O , o00O0O , '' )
    if 'episodes' in OOoOO0o :
     Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , o00O0O , o00O0O , '' )
  for url in II1IIi :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 51 - 51: I1ii11iIi11i - Ii1I * ooOOOoO
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if Oo0O0Oo00O != 'Failed' :
  OOoOOo0O00O = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( Oo0O0Oo00O )
  for url , I1111i , o00O0O in OOoOOo0O00O :
   if oo0OO in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 12 - 12: iI11I1II1I1I % I11i1ii1 % I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 78 - 78: I1111IIi . OOooOOo . ooOOOoO
    if 97 - 97: o000O0o
    if 80 - 80: oOo0O0Ooo . ii1ii11IIIiiI
    if 47 - 47: ooOOOoO + I11i1ii1 + IIiIiII11i % Ii
    if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / O0OOOoOoo0 * o000O0o
    if 29 - 29: I11i
    if 86 - 86: IIiIiII11i . I1111IIi
    if 2 - 2: ii
    if 60 - 60: oO0o
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for I1111i in ooOoO00 :
   if oo0OO in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( IIII + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 81 - 81: OOooOOo % ii1ii11IIIiiI
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for I1111i in Iii1I1111ii :
   if oo0OO in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( iI1iiiIiii + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 87 - 87: iI11I1II1I1I . ii * OOooOOo
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if IiIi1111ii != 'Failed' :
  iI1I1II1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiIi1111ii )
  for url , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in iI1I1II1 :
   if oo0OO in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % ii1ii11IIIiiI - iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 17 - 17: ooOOOoO / I11i % I1ii11iIi11i
 o0oo00o0O0O00 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for IiiI11i1I in o0oo00o0O0O00 :
  OOo0 = O0Oo000ooO00 + IiiI11i1I + I1IIIii
  o0Oii1111i = O0o0O00Oo0o0 ( OOo0 )
  if o0Oii1111i != 'Failed' :
   ooOOOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0Oii1111i )
   for I1111i , oo00O00oO000o , url , o00O0O , o0ooooO0o0O , O0OOO0OOooo00 in ooOOOo :
    if oo0OO in I1111i . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , url , O0OOO0OOooo00 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 34 - 34: Ii1IIIi1 . I1ii11iIi11i
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 78 - 78: Ii1I % oOo0O0Ooo / ii % Ii1IIIi1 - O0OOOoOoo0
     if 2 - 2: iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: ii / Ii
def I11I1i1iI ( ) :
 oO0OOoo0OO = OoOooO ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( I1111i ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + Ii1I1Ii , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + Ii1I1Ii )
def O00oO0O0oO00o ( url ) :
 iIii1iII1Ii = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( iIii1iII1Ii )
 sys . exit ( 1 )
 if 50 - 50: ii1ii11IIIiiI
def I1iiIiI1iI1I ( ) :
 if 27 - 27: Ii1I * iiiiiiii1 - oO0o + ii1ii11IIIiiI * ii1ii11IIIiiI
 if 55 - 55: I11i1ii1
 if 82 - 82: iiiiiiii1 - Ii1IIIi1 + oO0o
 if 64 - 64: I11i . o0o00Oo0O * ii1ii11IIIiiI + ii - I1ii11iIi11i . ii
 if 70 - 70: I1ii11iIi11i - o000O0o . iI11I1II1I1I % ooOOOoO / OOooOOo - o0o00Oo0O
 if 55 - 55: O0OOOoOoo0 - oO0o
 if 100 - 100: o0o00Oo0O
 if 79 - 79: iI11I1II1I1I
 if 81 - 81: Ii1IIIi1 + iI11I1II1I1I * iiiiiiii1 - iI11I1II1I1I . Ii1IIIi1
 if 48 - 48: ooOOOoO . ii . oOo0O0Ooo . OOooOOo % Ii1I / O0OOOoOoo0
 if 11 - 11: ooOoO0O00 % oO0o % O0OOOoOoo0
 Iiiiii111i1ii ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , III1iII1I1ii + 'seasons.png' )
 Iiiiii111i1ii ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , III1iII1I1ii + 'episodes.png' )
 Iiiiii111i1ii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 99 - 99: I11i1ii1 / iI11I1II1I1I - ii1ii11IIIiiI * Ii1I % oOo0O0Ooo
def i1II1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , I1iIiiiI1 in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( I1111i + ' - ' + I1iIiiiI1 ) . replace ( '&amp;' , '&' ) , url , 90053 , III1iII1I1ii + 'seasons.png' )
  if 42 - 42: Ii1IIIi1 % o000O0o / oO0o - o000O0o * Ii
def iI1IiiiIiI1Ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , url , 90054 , III1iII1I1ii + 'episodes.png' )
  if 78 - 78: ii / Ii1IIIi1 % OOooOOo * ii
def ooOO00o00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , url , 90054 , o00O0O )
 for url in next :
  Iiiiii111i1ii ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 18 - 18: iI11I1II1I1I + ooOOOoO * oOo0O0Ooo - Ii1IIIi1 / oOo0O0Ooo
def o00iI1i1II ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for o00O0O , I1iIiiiI1 , url , I1111i , I1ii1ii1I in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1iIiiiI1 + ' - ' + I1111i + ' - ' + I1ii1ii1I , url , 90044 , o00O0O , o00O0O , '' )
 for o00O0O , I1111i , url in i1I :
  Iiiiii111i1ii ( I1111i , url , 90044 , o00O0O , o00O0O , '' )
 for url in next :
  Iiiiii111i1ii ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 18 - 18: o000O0o * o000O0o % o000O0o
def Ii1I1I1i11ii ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oO0o = 'http://onlinemovies.tube/?s=' + ( IIi ) . replace ( ' ' , '+' )
 oo0OO = OoOo0oO0o . lower ( )
 oO0OOoo0OO = OoOooO ( oo0OO )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , o00O0O , I1111i , OOoOO0o in i1IIIII11I1IiI :
  if 'season' in OOoOO0o :
   Iiiiii111i1ii ( I1111i , Ii1I1Ii , 90054 , o00O0O , o00O0O , '' )
  if 'episodes' in OOoOO0o :
   Iiiiii111i1ii ( I1111i , Ii1I1Ii , 90044 , o00O0O , o00O0O , '' )
 for Ii1I1Ii in next :
  Iiiiii111i1ii ( 'NEXT' , Ii1I1Ii , 90053 , III1iII1I1ii + 'Next.png' )
  if 54 - 54: O0OOOoOoo0 % ooOoO0O00 + Ii1I
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
 Iiiiii111i1ii ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , III1iII1I1ii + 'allmov.png' )
 Iiiiii111i1ii ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , III1iII1I1ii + 'Genre.png' )
 Iiiiii111i1ii ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , III1iII1I1ii + 'Years.png' )
 Iiiiii111i1ii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 79 - 79: OOooOOo / I11i1ii1
def oOo00o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , I1iIiiiI1 in i1IIIII11I1IiI :
  if 'genre' in url :
   Iiiiii111i1ii ( ( I1111i + ' - ' + I1iIiiiI1 ) . replace ( '&amp;' , '&' ) , url , 90043 , III1iII1I1ii + 'Genre.png' )
   if 98 - 98: Ii1IIIi1 % ooOoO0O00 . oOo0O0Ooo . IIiIiII11i . Ii1I / Ii
def iIii1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if 'release' in url :
   Iiiiii111i1ii ( I1111i , url , 90043 , III1iII1I1ii + 'Years.png' )
   if 50 - 50: OOooOOo
def i1i1Ii11Ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , O000oOo , url , oo00O00oO000o in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' ' + O000oOo , url , 90044 , o00O0O , o00O0O , oo00O00oO000o )
 for o00O0O , I1111i , OOoOO0o , url , IiiIIi1 , oo00O00oO000o in i1I :
  if 'movies' in OOoOO0o :
   iiOOooooO0Oo ( I1111i + ' - ' + IiiIIi1 , url , 90044 , o00O0O , o00O0O , oo00O00oO000o )
 for url in next :
  Iiiiii111i1ii ( 'NEXT' , url , 90043 , III1iII1I1ii + 'Next.png' )
  if 28 - 28: I11i
def IIiI1Ii1IIiI11i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  Ii11I1iIiiI ( 'http:' + url )
  if 87 - 87: I11i1ii1 . o0o00Oo0O % iiiiiiii1 + Ii1I + ii1ii11IIIiiI % iI11I1II1I1I
def Ii11I1iIiiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( ( I1111i ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , III1iII1I1ii + 'movhub.png' )
def ii11iIIi ( ) :
 if 1 - 1: O0OOOoOoo0 * OOooOOo
 if 66 - 66: OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
 if 87 - 87: Ii1IIIi1 + I11i . O0OOOoOoo0 - ii
 if 6 - 6: iI11I1II1I1I * ii
 if 28 - 28: I1ii11iIi11i * I11i / iiiiiiii1
 if 52 - 52: o0o00Oo0O / I11i % O0OOOoOoo0 * oOo0O0Ooo % Ii1IIIi1
 if 69 - 69: Ii1I
 if 83 - 83: I11i
 if 38 - 38: iiiiiiii1 + ii . ooOoO0O00
 if 19 - 19: O0OOOoOoo0 - I11i - ii1ii11IIIiiI - OOooOOo . O0OOOoOoo0 . iiiiiiii1
 if 48 - 48: O0OOOoOoo0 + I1111IIi
 if 60 - 60: ooOOOoO + O0OOOoOoo0 . I1111IIi / ooOoO0O00 . iI11I1II1I1I
 if 14 - 14: Ii1IIIi1
 if 79 - 79: ii1ii11IIIiiI
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oO0o = 'http://onlinemovies.tube/?s=' + ( IIi ) . replace ( ' ' , '+' )
 oo0OO = OoOo0oO0o . lower ( )
 oO0OOoo0OO = OoOooO ( oo0OO )
 i1IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , o00O0O , I1111i , o0Oii111 in i1IIIII11I1IiI :
  if 'movies' in o0Oii111 :
   Iiiiii111i1ii ( o0Oii111 + '-' + I1111i , Ii1I1Ii , 90044 , o00O0O )
 for Ii1I1Ii in next :
  i1i1Ii11Ii ( Ii1I1Ii )
  if 93 - 93: ii * I1ii11iIi11i
def OO0O00oOo ( ) :
 Iiiiii111i1ii ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 oO0OOoo0OO = OoOooO ( 'http://www.join4films.com/' )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , Ii1I1Ii , 80006 , III1iII1I1ii + 'Desi.png' )
def I1IiI1iIiIiii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oO0OOoo0OO )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( I1111i , url , 80007 , o00O0O )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def I1iiI1II ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  OOOOo0o00OO0000 ( url )
def IIIi ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oO0o = 'http://www.join4films.com/?s=' + ( IIi ) . replace ( ' ' , '+' ) + '&search_type=1'
 oo0OO = OoOo0oO0o . lower ( )
 I1IiI1iIiIiii ( oo0OO )
 if 23 - 23: I11i1ii1
 if 13 - 13: iI11I1II1I1I
 if 77 - 77: Ii - iI11I1II1I1I / o000O0o / I11i1ii1 / oO0o
 if 56 - 56: ii * o0o00Oo0O
 if 85 - 85: ii % OOooOOo * iI11I1II1I1I
 if 44 - 44: iI11I1II1I1I . Ii1I + iiiiiiii1 . I11i1ii1
 if 7 - 7: Ii1I + iI11I1II1I1I * ooOOOoO * ooOOOoO / IIiIiII11i - ii1ii11IIIiiI
 if 65 - 65: o000O0o + OOooOOo + IIiIiII11i
 if 77 - 77: IIiIiII11i
 if 50 - 50: o0o00Oo0O . o0o00Oo0O . I11i1ii1 % I1ii11iIi11i
 if 68 - 68: o000O0o
 if 10 - 10: ii1ii11IIIiiI
 if 77 - 77: Ii1IIIi1 / IIiIiII11i + I1111IIi + I11i1ii1 - Ii
 if 44 - 44: oOo0O0Ooo + OOooOOo + Ii1I . oOo0O0Ooo * OOooOOo % iI11I1II1I1I
 if 72 - 72: Ii1IIIi1 . Ii1IIIi1 - Ii1I
 if 48 - 48: I1ii11iIi11i - I11i1ii1 + I1ii11iIi11i - oOo0O0Ooo * Ii . O0OOOoOoo0
 if 35 - 35: I1111IIi . o0o00Oo0O + I1ii11iIi11i + Ii1IIIi1 + ooOoO0O00
def OooOooO0O0o0 ( ) :
 iiOOooooO0Oo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 if 59 - 59: I1ii11iIi11i + O0OOOoOoo0 - Ii1IIIi1 . I11i + oOo0O0Ooo % o000O0o
def i111Iii ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oO0o = 'http://imoviemax.se/?s=' + ( IIi ) . replace ( ' ' , '+' )
 oo0OO = OoOo0oO0o . lower ( )
 o0o0 ( oo0OO )
def i1iIi1IIiIII1 ( url ) :
 i1Ii11I1II = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , oOOOoo0o in i1IIIII11I1IiI :
  if I1111i in i1Ii11I1II :
   pass
  else :
   iiOOooooO0Oo ( I1111i + ' - ' + oOOOoo0o + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
   i1Ii11I1II . append ( I1111i )
   if 44 - 44: o0o00Oo0O % ooOoO0O00
def IiIIiii1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , ooooo0Oo0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' - Views:' + ooooo0Oo0 , url , 10075 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
  if 97 - 97: I1111IIi . o000O0o . I1111IIi
  if 91 - 91: Ii1IIIi1 + iiiiiiii1 . ooOOOoO
def o0o0 ( url ) :
 i1I111i1ii = [ ]
 oO0OOoo0OO = OoOooO ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0OOoo0OO )
 for next in next :
  iiOOooooO0Oo ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10075 , o00O0O , o00O0O , '' )
  i1I111i1ii . append ( I1111i )
  if 81 - 81: I1ii11iIi11i - ooOOOoO
def ii1iII1iI111 ( img , name , url ) :
 img = img
 name = name
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oO0OOoo0OO )
 for o0o0O0O000 , url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  I1I1i = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + I1I1i
  O0O0oo = ( o0o0O0O000 ) . replace ( 'play-' , 'Server ' )
  OOiIiIIi1 ( O0O0oo , I1I1i , 10076 , img , img , '' )
  if 83 - 83: I1111IIi / iiiiiiii1
def OOo000OO000 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oO0OOoo0OO )
 for OoO in i1IIIII11I1IiI :
  if '=m' in OoO :
   OOOO00OooO ( OoO )
  elif 'php' in OoO :
   OOo000OO000 ( url )
  else :
   oO0OOoo0OO = OoOooO ( OoO )
   i1IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( oO0OOoo0OO )
   for IIII in i1IIIII11I1IiI :
    OOOO00OooO ( OoO )
    if 64 - 64: oO0o . oOo0O0Ooo - ii . I11i1ii1 - O0OOOoOoo0
    if 77 - 77: ii1ii11IIIiiI % OOooOOo / IIiIiII11i % O0OOOoOoo0 % ii % oO0o
    if 19 - 19: I1111IIi * iiiiiiii1 / o000O0o * iiiiiiii1 - ii * ooOOOoO
def iiiI1i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I1i1i11 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1oOOoo0o0OOOO , i1IoOOoooO0O0 in I1i1i11 :
  print 'there ><><><><><><><><><><><><'
  i1oOOoo0o0OOOO = i1oOOoo0o0OOOO
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i1IoOOoooO0O0 ) )
  for I1111i , ii1O0ooooo000 in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + i1oOOoo0o0OOOO + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + ii1O0ooooo000 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
 I1IIIiI1I1ii1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1oOOoo0o0OOOO , OooOoOO0OO in I1IIIiI1I1ii1 :
  print 'there ><><><><><><><><><><><><'
  i1oOOoo0o0OOOO = i1oOOoo0o0OOOO
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OooOoOO0OO ) )
  for I1111i , ii1O0ooooo000 in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + i1oOOoo0o0OOOO + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + ii1O0ooooo000 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
   if 27 - 27: I1111IIi * oOo0O0Ooo . iI11I1II1I1I - iI11I1II1I1I
   if 5 - 5: I1111IIi
   if 84 - 84: IIiIiII11i * o000O0o * IIiIiII11i % I1111IIi / oOo0O0Ooo
def iIi1Ii1i1iI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I1IIIiI1I1ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
  I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for I1111i in I1111i :
   I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  I111iIi1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for I111iIi1 in I111iIi1 :
   I111iIi1 = 'http:' + I111iIi1
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , '' , '' )
  if 100 - 100: I1111IIi . ii1ii11IIIiiI - iI11I1II1I1I . Ii / IIiIiII11i
  if 71 - 71: iiiiiiii1 * I1ii11iIi11i . ooOOOoO
  if 49 - 49: I1111IIi * o0o00Oo0O . I1111IIi
  if 19 - 19: IIiIiII11i - I1111IIi
def ii1II ( url ) :
 if 59 - 59: I11i * oO0o - ii1ii11IIIiiI . Ii1IIIi1
 o0OO00oo0O = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO , o00O0O , I1111i , Ii1I1i111 in i1IIIII11I1IiI :
  I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = OoOooO ( OoO )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for OOO0oOoO0O , oOOOO in i1I :
   oOi1 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oOOOO ) )
   for oo00O00oO000o in oOi1 :
    if I1111i in o0OO00oo0O :
     pass
    else :
     OOiIiIIi1 ( I1111i , OOO0oOoO0O , 8043 , o00O0O , o00O0O , oo00O00oO000o )
     I1I11i ( 'movies' , 'INFO' )
     o0OO00oo0O . append ( I1111i )
     if 39 - 39: I11i1ii1 / o0o00Oo0O * I1111IIi
     if 17 - 17: ii1ii11IIIiiI / iI11I1II1I1I - oO0o + oOo0O0Ooo % Ii1IIIi1
def III1III11II ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , IiI111ii1ii , oo00O00oO000o , o0ooooO0o0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10065 , IiI111ii1ii , o0ooooO0o0O , oo00O00oO000o )
 I1I11i ( 'movies' , 'INFO' )
 if 43 - 43: oOo0O0Ooo
def iiIIIiI1Ii ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oO0o = 'https://www.youtube.com/results?search_query=' + ( IIi ) . replace ( ' ' , '+' )
 oo0OO = OoOo0oO0o . lower ( )
 oO0OOoo0OO = OoOooO ( oo0OO )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii in next :
  Ii1I1Ii = 'https://www.youtube.com' + Ii1I1Ii
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , Ii1I1Ii , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for o00O0O , Ii1I1Ii , I1111i , IIiiiiiIiIIi , oOOOO in i1IIIII11I1IiI :
  OOOO . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  I111iIi1 = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I111iIi1
  Ii1I1Ii = 'http://www.youtube.com' + Ii1I1Ii
  OOiIiIIi1 ( '[COLORred]' + IIiiiiiIiIIi + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( Ii1I1Ii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , I111iIi1 , oOOOO )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o00O0O , Ii1I1Ii , I1111i , IIiiiiiIiIIi in i1IIIII11I1IiI :
   print 'im doing it'
   I1I11i ( 'tvshows' , 'INFO' )
   I111iIi1 = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   Ii1I1Ii = 'http://www.youtube.com' + Ii1I1Ii
   if '&' in Ii1I1Ii :
    print ' i got here'
    oO0OOoo0OO = OoOooO ( Ii1I1Ii )
    I1IIIiI1I1ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     Ii1I1Ii = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for Ii1I1Ii in Ii1I1Ii :
      Ii1I1Ii = 'https://www.youtube.com/w' + Ii1I1Ii
     I111iIi1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for I111iIi1 in I111iIi1 :
      I111iIi1 = 'http:' + I111iIi1
     OOiIiIIi1 ( '[COLORred]' + IIiiiiiIiIIi + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( Ii1I1Ii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , O0o0Oo , '' )
   elif I1111i in OOOO :
    pass
   elif 'user' in Ii1I1Ii or 'elete' in I1111i :
    pass
   elif 'hannel' in Ii1I1Ii :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + Ii1I1Ii
    oO0OOoo0OO = OoOooO ( Ii1I1Ii )
    iiIiiIi1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for o00O0O , Ii1I1Ii , I1111i in iiIiiIi1 :
     if 'outube' in Ii1I1Ii or 'list' in Ii1I1Ii :
      pass
     elif 'atch' in Ii1I1Ii :
      Ii1I1Ii = ( Ii1I1Ii ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + IIiiiiiIiIIi + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( Ii1I1Ii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + IIiiiiiIiIIi + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( Ii1I1Ii ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , I111iIi1 , '' )
    if 30 - 30: Ii1IIIi1 + IIiIiII11i - I1111IIi * ii
def I1iIiiiI1OOO0O00Oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for o00O0O , url , I1111i , IIiiiiiIiIIi , oOOOO in i1IIIII11I1IiI :
  OOOO . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  I111iIi1 = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + I111iIi1
  url = 'http://www.youtube.com' + url
  OOiIiIIi1 ( '[COLORred]' + IIiiiiiIiIIi + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , I111iIi1 , oOOOO )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for o00O0O , url , I1111i , IIiiiiiIiIIi in i1IIIII11I1IiI :
   I1I11i ( 'tvshows' , 'INFO' )
   I111iIi1 = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oO0OOoo0OO = OoOooO ( url )
    I1IIIiI1I1ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     I111iIi1 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for I111iIi1 in I111iIi1 :
      I111iIi1 = 'http:' + I111iIi1
     OOiIiIIi1 ( '[COLORred]' + IIiiiiiIiIIi + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , O0o0Oo , '' )
   elif I1111i in OOOO :
    pass
   elif 'user' in url or 'elete' in I1111i :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0OOoo0OO = OoOooO ( url )
    iiIiiIi1 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for o00O0O , url , I1111i in iiIiiIi1 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + IIiiiiiIiIIi + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + IIiiiiiIiIIi + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 , I111iIi1 , '' )
    if 13 - 13: iI11I1II1I1I
def IiIIII1iiIIi ( ) :
 Oo0oO ( )
 i1I1IiI1ii ( )
 if 64 - 64: O0OOOoOoo0 * Ii1I % IIiIiII11i - OOooOOo + Ii1I
 if 62 - 62: OOooOOo % I11i % oOo0O0Ooo + I1111IIi . oO0o
 iiOOooooO0Oo ( '[COLOR' + II + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o , 60004 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iI1iiiIii1II1 ( '[COLORsteelblue]VOD Lists[/COLOR]' , '' , 40000 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
 if 66 - 66: IIiIiII11i
 if 72 - 72: Ii1IIIi1 % ii1ii11IIIiiI % O0OOOoOoo0 % IIiIiII11i - Ii1IIIi1 % iI11I1II1I1I
 if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
def o00iIiiiII ( ) :
 iI1iiiIii1II1 ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , Ii1I1 + '&action=get_vod_streams' , 40001 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( OO0ooO0 )
 i1IIIII11I1IiI = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLORsteelblue]' + I1111i + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , Ii1I1Ii , 40001 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
def OoOooOO0oOOo0O ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( I1II + url )
 i1IIIII11I1IiI = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg .+?,"container_extension":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , type , OoO , iiO0oOo00o , iIIi1Ii1III in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , Oooo00 + OoO + '.' + iIIi1Ii1III , 222 , ( iiO0oOo00o ) . replace ( '\/' , '/' ) + 'jpg' , O0o0Oo , 'Type: ' + type )
  if 9 - 9: ii * o0o00Oo0O
def i1I1IiI1ii ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  O0oO0OOoO ( )
  if 69 - 69: ooOOOoO / Ii * I11i / iiiiiiii1
  if 71 - 71: I11i / Ii1IIIi1 % Ii1IIIi1
  if 89 - 89: ii + Ii / ooOOOoO + iI11I1II1I1I % I11i1ii1
  if 29 - 29: Ii1I
  if 53 - 53: Ii . Ii1I % ii1ii11IIIiiI / I11i1ii1 % iI11I1II1I1I
  if 6 - 6: I1ii11iIi11i - Ii1IIIi1 . iI11I1II1I1I
  if 30 - 30: I11i1ii1 + I11i1ii1 % I1111IIi - I11i - Ii1I
  if 36 - 36: ooOOOoO % Ii1IIIi1
def O0oO0OOoO ( ) :
 i1i = OoOooO ( 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 for Ii1I1Ii in i1IIIII11I1IiI :
  OoO0 = datetime . fromtimestamp ( float ( i1IIIII11I1IiI [ 0 ] ) )
  OoO0 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= OoO0 <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   OOooO0OOoo . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + II + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + II + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + II + '] To Purchase A licence[/COLOR]' )
def i1ii1IIIII ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"username":"(.+?)"' ) . findall ( i1i )
 oOOO0 = re . compile ( '"password":"(.+?)"' ) . findall ( i1i )
 OOoOOo0O00O = re . compile ( '"status":"(.+?)"' ) . findall ( i1i )
 i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 ooOoO00 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( i1i )
 Iii1I1111ii = re . compile ( '"created_at":"(.+?)"' ) . findall ( i1i )
 iiIii1I = re . compile ( '"max_connections":"(.+?)"' ) . findall ( i1i )
 iI1I1II1 = re . compile ( '"is_trial":"1"' ) . findall ( i1i )
 oO0ooOoO = re . compile ( '"is_trial":"0"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']My GTV Account Information[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  i1i1iII1 ( '[COLOR' + II + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in oOOO0 :
  i1i1iII1 ( '[COLOR' + II + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in OOoOOo0O00O :
  i1i1iII1 ( '[COLOR' + II + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in Iii1I1111ii :
  OoO0 = datetime . fromtimestamp ( float ( Iii1I1111ii [ 0 ] ) )
  OoO0 . strftime ( '%Y-%m-%d %H:%M:%S' )
  i1i1iII1 ( '[COLOR' + II + ']Created:[/COLOR]  %s' % ( OoO0 ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in i1I :
  OoO0 = datetime . fromtimestamp ( float ( i1I [ 0 ] ) )
  OoO0 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= OoO0 <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   i1i1iII1 ( '[COLORred]Expires Today[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  i1i1iII1 ( '[COLOR' + II + ']Expires:[/COLOR]  %s' % ( OoO0 ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in ooOoO00 :
  i1i1iII1 ( '[COLOR' + II + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in iiIii1I :
  i1i1iII1 ( '[COLOR' + II + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in iI1I1II1 :
  i1i1iII1 ( '[COLOR' + II + ']Trial:[/COLOR] Yes' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in oO0ooOoO :
  i1i1iII1 ( '[COLOR' + II + ']Trial:[/COLOR] No' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 i1i1iII1 ( '' , '' , '' , '' )
 i1i1iII1 ( '' , '' , '' , '' )
 i1i1iII1 ( '[COLOR' + II + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 49 - 49: iI11I1II1I1I % ooOOOoO . ooOOOoO . iI11I1II1I1I * OOooOOo / ooOOOoO
def oOOoOooO0oO0o ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
 o0o0OoO0OOO0 ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 79 - 79: o000O0o % I11i % OOooOOo
Ii1I1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( II11iiii1Ii , OO0o )
Oooo00 = 'http://piesustv.net:8000/movie/%s/%s/' % ( II11iiii1Ii , OO0o )
ii1IIiII111I = 'http://piesustv.net:8000/live/%s/%s/' % ( II11iiii1Ii , OO0o )
O00OoOoO = '&action=get_live_categories'
ooO0o0oo = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( II11iiii1Ii , OO0o )
OO0ooO0 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( II11iiii1Ii , OO0o )
I1II = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_streams&category_id=' % ( II11iiii1Ii , OO0o )
o0O0OOo0oO = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( II11iiii1Ii , OO0o )
if 42 - 42: IIiIiII11i / o0o00Oo0O . iI11I1II1I1I / o0o00Oo0O / oO0o / ii
def ooiiI1ii ( ) :
 if 76 - 76: ii1ii11IIIiiI + iI11I1II1I1I + OOooOOo . oO0o
 iiOOooooO0Oo ( ( '[COLORsteelblue]Full List[/COLOR]' ) . replace ( '\/' , ' - ' ) , Ii1I1 + '&action=get_live_streams' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( Ii1I1 + O00OoOoO )
 i1IIIII11I1IiI = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLORsteelblue]' + I1111i + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , Ii1I1Ii , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
def i1i1 ( ) :
 o0oOoOo0 = 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o
 III1IiI1i1i = urllib2 . Request ( o0oOoOo0 , headers = { "Accept" : "application/xml" } )
 i1Oo00 = urllib2 . urlopen ( III1IiI1i1i )
 if i1Oo00 and i1Oo00 . getcode ( ) == 200 :
  o0OOOOOo0 = [ ]
  oooOoO = ElementTree . parse ( i1Oo00 )
  O0Oo0 = oooOoO . getroot ( )
  for iiIiiIi1 in oooOoO . findall ( "channel" ) :
   iIIIi1IiI11I1 = iiIiiIi1 . find ( 'title' ) . text
   iIIIi1IiI11I1 = base64 . b64decode ( iIIIi1IiI11I1 )
   iIIIi1IiI11I1 = iIIIi1IiI11I1 . partition ( "[" )
   O0Ooo000 = iIIIi1IiI11I1 [ 1 ] + iIIIi1IiI11I1 [ 2 ]
   O0Ooo000 = O0Ooo000 . partition ( "]" )
   O0Ooo000 = O0Ooo000 [ 2 ]
   O0Ooo000 = O0Ooo000 . partition ( "   " )
   O0Ooo000 = O0Ooo000 [ 2 ]
   if 36 - 36: I1ii11iIi11i % ii1ii11IIIiiI / Ii % iiiiiiii1 + oO0o
   i1IiI = iiIiiIi1 . find ( "description" ) . text
   if i1IiI :
    i1IiI = base64 . b64decode ( i1IiI )
    IIIiOo0O = i1IiI . partition ( "(" )
    IIIiOo0O = "NOW:  " + IIIiOo0O [ 0 ]
    OOOO0Oo = i1IiI . partition ( ")\n" )
    OOOO0Oo = OOOO0Oo [ 2 ] . partition ( "(" )
    OOOO0Oo = "NEXT:  " + OOOO0Oo [ 0 ]
    iIiI1 = IIIiOo0O + OOOO0Oo
   else :
    iIiI1 = ""
   o0OOOOOo0 . append ( { 'title' : iIIIi1IiI11I1 [ 0 ] , 'cs' : O0Ooo000 , 'schedule' : iIiI1 } )
 return o0OOOOOo0
def I1IiII1I1i1I1 ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( ooO0o0oo + url )
 i1IIIII11I1IiI = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , type , OoO , iiO0oOo00o in i1IIIII11I1IiI :
  IIII = ( ii1IIiII111I + OoO + '.m3u8' ) . strip ( )
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , IIII , 222 , ( iiO0oOo00o ) . replace ( '\/' , '/' ) + 'jpg' , O0o0Oo , type )
  if 28 - 28: I1ii11iIi11i + I1111IIi % IIiIiII11i / oO0o + Ii
def ii11Iiii ( url , name , img ) :
 img = img
 name = name
 url = url
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1III11iiii11i1 , II1 in i1IIIII11I1IiI :
  if name == I1III11iiii11i1 :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) + II1 , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def OoooOo ( name ) :
 I1I1IIiiii1ii = name
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , o00O0O , Ii1I1Ii in i1IIIII11I1IiI :
  Ii1I1Ii = ( Ii1I1Ii ) . replace ( '.ts' , '.m3u8' )
  OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( Ii1I1Ii ) . strip ( ) , 222 , o00O0O , o00O0O , '' )
 else :
  OOiIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 92 - 92: o000O0o / Ii1IIIi1 . Ii1I
  if 30 - 30: ii1ii11IIIiiI . Ii1I / Ii1IIIi1
  if 2 - 2: I1111IIi % oOo0O0Ooo - iiiiiiii1
  if 79 - 79: ii / Ii1I . o0o00Oo0O
  if 79 - 79: o000O0o - IIiIiII11i
  if 43 - 43: ooOoO0O00 + o0o00Oo0O % oO0o / ii1ii11IIIiiI * oOo0O0Ooo
  if 89 - 89: oOo0O0Ooo . I1ii11iIi11i + Ii1I . o0o00Oo0O % I11i
  if 84 - 84: ii + iiiiiiii1 / oOo0O0Ooo % Ii1IIIi1 % Ii1I * oOo0O0Ooo
  if 58 - 58: oO0o - OOooOOo . Ii % Ii / ooOoO0O00 / o000O0o
  if 24 - 24: oOo0O0Ooo * ooOoO0O00 % I11i1ii1 / o0o00Oo0O + Ii
  if 12 - 12: Ii1I / ii1ii11IIIiiI
  if 5 - 5: ii
def oo000o0000oO ( ) :
 iiOOooooO0Oo ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( ooOooo000oOO ) :
  iiOOooooO0Oo ( 'Backup Genie Favourites' , Ii1I1Ii , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( oO0 ) :
  iiOOooooO0Oo ( 'Backup Ivue Config' , oO0 , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  iiOOooooO0Oo ( 'Backup Kodi Favourites' , Ii1iIiII1ii1 , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 18 - 18: oOo0O0Ooo % ii - O0OOOoOoo0 . Ii * I1ii11iIi11i % ii1ii11IIIiiI
  if 12 - 12: ooOoO0O00 / Ii1IIIi1 % I11i1ii1 * I1111IIi * o0o00Oo0O * iI11I1II1I1I
  if 93 - 93: I1ii11iIi11i / Ii1I + ooOoO0O00 * o000O0o . ii
zip = oo00 . getSetting ( 'zip' )
Oo000 = xbmc . translatePath ( os . path . join ( zip ) )
def OoOOIIIIIiI11Ii ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 41 - 41: Ii - ooOoO0O00 / I1ii11iIi11i * I1111IIi / iiiiiiii1 - I1ii11iIi11i
  if 56 - 56: o0o00Oo0O
  if 45 - 45: OOooOOo - oO0o - OOooOOo
def IIiiI ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = ooOooo000oOO
  elif 'Ivue' in name :
   url = oO0
  elif 'Kodi' in name :
   url = Ii1iIiII1ii1
  OoOOIIIIIiI11Ii ( )
  iII11iiiiiii = open ( url ) . read ( )
  O0000 = os . path . join ( Oo000 , description . split ( 'Your ' ) [ 1 ] )
  oooOo0OOOoo0 = open ( O0000 , mode = 'w' )
  oooOo0OOOoo0 . write ( iII11iiiiiii )
  oooOo0OOOoo0 . close ( )
 else :
  if 'guisettings.xml' in description :
   OoOOOOOO = open ( os . path . join ( Oo000 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oo0OO0 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   i1IIIII11I1IiI = re . compile ( oo0OO0 ) . findall ( OoOOOOOO )
   for type , O0oo00o , IIi1i1 in i1IIIII11I1IiI :
    IIi1i1 = IIi1i1 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , O0oo00o , IIi1i1 ) )
  else :
   O0000 = os . path . join ( url )
   iII11iiiiiii = open ( os . path . join ( Oo000 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oooOo0OOOoo0 = open ( O0000 , mode = 'w' )
   oooOo0OOOoo0 . write ( iII11iiiiiii )
   oooOo0OOOoo0 . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 84 - 84: Ii1IIIi1 + ii1ii11IIIiiI + I11i
 if 33 - 33: ii1ii11IIIiiI
 if 93 - 93: I11i1ii1
 if 34 - 34: o000O0o - I11i1ii1 * I1ii11iIi11i / I11i
def iI1iiIi1 ( ) :
 i1iiiIi1Iii = 1
 OoOOIIIIIiI11Ii ( )
 o0oO0O = xbmc . translatePath ( os . path . join ( Oo000 , 'Build Backup' , 'Full Backup' , '' ) )
 OO0ooooO0 = xbmc . translatePath ( os . path . join ( Oo000 , 'Build Backup' , 'my_full_backup.zip' ) )
 OOO0o0O00oO0 = xbmc . translatePath ( os . path . join ( Oo000 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( o0oO0O ) :
  os . makedirs ( o0oO0O )
 i1I1iII1i1iI = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not i1I1iII1i1iI ) : return False , 0
 iIIIi1IiI11I1 = i1I1iII1i1iI
 I1iI1I1ii1 = xbmc . translatePath ( os . path . join ( o0oO0O , iIIIi1IiI11I1 + '.zip' ) )
 iIIi1 = [ 'plugin.video.GenieTv' ]
 o0Ooo0o0Oo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 oo00ooooOOo00 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 ii1iOO00Oooo000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iI1 = "Creating full backup of existing build"
 ii111iiIii = "Creating Community Build"
 oO0oiIiI = "Archiving..."
 iIIiiiI1iI1 = ""
 oO00000oO0o0O = "Please Wait"
 IIIiI1iI1 ( Oo0o0000o0o0 , I1iI1I1ii1 , ii111iiIii , oO0oiIiI , iIIiiiI1iI1 , oO00000oO0o0O , oo00ooooOOo00 , ii1iOO00Oooo000 )
 time . sleep ( 1 )
 IIiIiiii1I1 = xbmc . translatePath ( os . path . join ( o0oO0O , iIIIi1IiI11I1 + '_guisettings.zip' ) )
 oO0O0 = zipfile . ZipFile ( IIiIiiii1I1 , mode = 'w' )
 try :
  oO0O0 . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oO0O0 . close ( )
 if i1iiiIi1Iii == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + OO0ooooO0 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + I1iI1I1ii1 + '[/COLOR]' )
  if 65 - 65: O0OOOoOoo0 . oOo0O0Ooo
def IIIiI1iI1 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 IIi11IIiIi1i = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 Iii = len ( sourcefile )
 Ooo0o0ooooOOo = [ ]
 oOoOO0000oO00 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for O0oiIiiIi , i1I111II , Oo0OOo in os . walk ( sourcefile ) :
  for file in Oo0OOo :
   oOoOO0000oO00 . append ( file )
 i1II11I11ii1 = len ( oOoOO0000oO00 )
 for O0oiIiiIi , i1I111II , Oo0OOo in os . walk ( sourcefile ) :
  i1I111II [ : ] = [ OOoO0oO00o for OOoO0oO00o in i1I111II if OOoO0oO00o not in exclude_dirs ]
  Oo0OOo [ : ] = [ oooOo0OOOoo0 for oooOo0OOOoo0 in Oo0OOo if oooOo0OOOoo0 not in exclude_files ]
  for file in Oo0OOo :
   Ooo0o0ooooOOo . append ( file )
   OOO0OoO0oo0OO = len ( Ooo0o0ooooOOo ) / float ( i1II11I11ii1 ) * 100
   o0oOoO00o . update ( int ( OOO0OoO0oo0OO ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   i1iI1Ii11Ii1 = os . path . join ( O0oiIiiIi , file )
   if not 'temp' in i1I111II :
    if not 'plugin.program.originwizard' in i1I111II :
     import time
     o0OoO0oo0O0o = '01/01/1980'
     ii1III1iiIi = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( i1iI1Ii11Ii1 ) ) )
     if ii1III1iiIi > o0OoO0oo0O0o :
      IIi11IIiIi1i . write ( i1iI1Ii11Ii1 , i1iI1Ii11Ii1 [ Iii : ] )
 IIi11IIiIi1i . close ( )
 o0oOoO00o . close ( )
 if 35 - 35: Ii1IIIi1 + o0o00Oo0O . Ii % Ii1I
 if 99 - 99: I11i
def I11IIII1111II ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 if 6 - 6: iI11I1II1I1I / Ii1IIIi1 + ooOOOoO
 if 89 - 89: o000O0o
def o0OOOOOo00 ( ) :
 Oo0oO ( )
 i111I1 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  Oo0oooO0oO ( )
 if iI11iI1IiiIiI == 1 :
  I1ii1 ( )
 if iI11iI1IiiIiI == 2 :
  iIIIiIii ( )
 if iI11iI1IiiIiI == 3 :
  iiIIIiI1Ii ( )
  if 82 - 82: I1ii11iIi11i
  if 5 - 5: oO0o / oO0o - o0o00Oo0O - iiiiiiii1 + iiiiiiii1
  if 99 - 99: ooOOOoO * ii / I11i . I1111IIi - iI11I1II1I1I - ii1ii11IIIiiI
  if 31 - 31: I1111IIi - oO0o / Ii1IIIi1 . ooOoO0O00 / ii1ii11IIIiiI
  if 66 - 66: oO0o
  if 72 - 72: iiiiiiii1
  if 91 - 91: IIiIiII11i / I1111IIi + iI11I1II1I1I . ooOOOoO - o0o00Oo0O
  if 70 - 70: ii1ii11IIIiiI * o000O0o - ooOOOoO + I1ii11iIi11i % Ii1I - I1111IIi
  if 81 - 81: o0o00Oo0O . o0o00Oo0O
def OoO00OooO0 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   oo0 ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , IiI111ii1ii , I1111i )
  if iI11iI1IiiIiI == 1 :
   o0OO0O0Oo ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if iI11iI1IiiIiI == 2 :
   o00OOo ( )
  if iI11iI1IiiIiI == 3 :
   Ii11III ( )
  if iI11iI1IiiIiI == 4 :
   I1Ii1i11I1I ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if iI11iI1IiiIiI == 5 :
   oo0o000o0oOO0 ( )
  if iI11iI1IiiIiI == 6 :
   OOO000OOo0o0O ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if iI11iI1IiiIiI == 7 :
   I111Iii1 ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if iI11iI1IiiIiI == 8 :
   i11i ( str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if iI11iI1IiiIiI == 9 :
   O0o0O00o0o ( )
  if iI11iI1IiiIiI == 10 :
   II1IIiiI1 ( )
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
  if 96 - 96: Ii1IIIi1 + Ii1IIIi1 % I1111IIi % Ii1IIIi1
 I1I11i ( 'movies' , 'MAIN' )
 if 28 - 28: iI11I1II1I1I + OOooOOo . I11i % Ii
def O00oOooo00o0o ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOO00o000o ( )
  if iI11iI1IiiIiI == 1 :
   iiIiIIIiiI ( )
  if iI11iI1IiiIiI == 2 :
   oOOo0O00o ( )
  if iI11iI1IiiIiI == 3 :
   o0ooooO0 ( Ii1I1Ii )
  if iI11iI1IiiIiI == 4 :
   IIII1ii1 ( Ii1I1Ii )
  if iI11iI1IiiIiI == 5 :
   O0O0ooOOO ( )
  if iI11iI1IiiIiI == 6 :
   OOO0O0OOo ( url = 'http://www.iplocation.net/' , inc = 1 )
  if iI11iI1IiiIiI == 7 :
   Iii1OOoO ( )
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
  if 8 - 8: iiiiiiii1 + oO0o
  if 9 - 9: Ii1IIIi1 + I11i
 I1I11i ( 'movies' , 'MAIN' )
 if 8 - 8: Ii1IIIi1 * I1ii11iIi11i / O0OOOoOoo0 - oO0o - ii
 if 100 - 100: o000O0o . iI11I1II1I1I . iI11I1II1I1I
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
 if 55 - 55: o000O0o
 if 37 - 37: I1111IIi / Ii / I1ii11iIi11i
def o0ooOO00OO0o0O ( ) :
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
 if 35 - 35: I11i * O0OOOoOoo0 - iI11I1II1I1I + I11i . ii
def iI1i111I1Ii ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , III1iII1I1ii + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 13 - 13: o0o00Oo0O % I11i1ii1 % ooOOOoO
def Ii11IiI111 ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , O0o0Oo , '' )
 if 31 - 31: oO0o * o0o00Oo0O / ooOOOoO . ii * ooOOOoO . Ii1I
 if 50 - 50: oO0o * ooOOOoO - I11i + I1111IIi * oO0o % o000O0o
 if 92 - 92: ooOOOoO % ooOoO0O00 % I11i1ii1 % I1111IIi % I11i
def O0O0OOOOoo ( ) :
 Oo0oO ( )
 i111I1 = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  O00Ooo0O0OOOo ( )
 if iI11iI1IiiIiI == 0 :
  o0oooo0O ( Ii1I1Ii )
 if iI11iI1IiiIiI == 0 :
  iI1iIIIIIiIi1 ( Ii1I1Ii )
  if 19 - 19: OOooOOo . I11i . ii
  if 13 - 13: Ii1IIIi1 . I1ii11iIi11i / IIiIiII11i
  if 43 - 43: iI11I1II1I1I % oO0o
 I1I11i ( 'movies' , 'MAIN' )
 if 84 - 84: I1ii11iIi11i
def iiiiI11iiIIi ( ) :
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 i1IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1i )
 for o00O0O , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , o00O0O , o00O0O , '' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 43 - 43: ooOOOoO % ii1ii11IIIiiI / I11i * iiiiiiii1
def oooIi1I11IiI1i ( url ) :
 i1i = OoOooO ( I111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 25 - 25: ooOOOoO / ooOOOoO % ii - Ii1I * o000O0o
def O00Ooo0O0OOOo ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 23 - 23: Ii
def OOooOoO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iIIiiiIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 6 - 6: OOooOOo / iI11I1II1I1I * iiiiiiii1 / oOo0O0Ooo + o0o00Oo0O
def Ii1I1IIIiI1i ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o0Oo00oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 73 - 73: ooOOOoO / ii . IIiIiII11i - I1111IIi * I11i1ii1 * I1111IIi
def IiI1IiI1iiI1 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + O000o0Iiiii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 88 - 88: ooOOOoO + oOo0O0Ooo - ooOOOoO / ii - Ii
def i11Ii1IiIIIi ( url ) :
 i1i = OoOooO ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 71 - 71: oO0o % oOo0O0Ooo - O0OOOoOoo0 . O0OOOoOoo0
def o0oooo0O ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + I1I1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 40 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 78 - 78: ooOOOoO . Ii1IIIi1 + o000O0o * O0OOOoOoo0 - ooOoO0O00
def I1ii1I1iii1 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iIiiiIIiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 91 - 91: I11i . O0OOOoOoo0 % I1ii11iIi11i - O0OOOoOoo0 . o000O0o % Ii
def Ii1I1i ( ) :
 i111I1 = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  iIi ( )
 if iI11iI1IiiIiI == 1 :
  O0OoOOoooo ( )
 if iI11iI1IiiIiI == 2 :
  O0oIi1iIiIi1I11 ( )
  if 12 - 12: iI11I1II1I1I . I11i1ii1
  if 36 - 36: iiiiiiii1 . I1111IIi * ii - I11i
  if 60 - 60: Ii1IIIi1 . O0OOOoOoo0 / iI11I1II1I1I + Ii1IIIi1 * iiiiiiii1
  if 82 - 82: Ii . iI11I1II1I1I * oOo0O0Ooo - ooOOOoO + ii1ii11IIIiiI
def O0OoOOoooo ( ) :
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( iIIII )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( iIIII )
 for Ii1I1Ii , i1ii1iIi in i1IIIII11I1IiI :
  Iiiiii111i1ii ( 'Android Apps' + i1ii1iIi , 'https://www.apkfiles.com' + Ii1I1Ii , 30035 , III1iII1I1ii + 'apps.png' )
 for Ii1I1Ii , i1ii1iIi in i1I :
  Iiiiii111i1ii ( 'Android Games' + i1ii1iIi , 'https://www.apkfiles.com' + Ii1I1Ii , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I11i ( 'movies' , 'MAIN' )
def I1I1Ii ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '/cat' in url :
   Iiiiii111i1ii ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def iI1IIII1 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '/app' in url :
   Iiiiii111i1ii ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def Oo0o ( url ) :
 iIIII = OoOooO ( url )
 OO0oOOo0o = url
 if "page=" in str ( url ) :
  OO0oOOo0o = url . split ( '?' ) [ 0 ]
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'apk' in url :
   OOiIiIIi1 ( ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + o00O0O )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 OOiIiIIi1 ( 'Next Page' , OO0oOOo0o + str ( i1I ) , 30037 , III1iII1I1ii + 'Next.png' )
def OoO000oo000o0 ( name , url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 name = name
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  i1Ii1I1Ii11iI ( name , url , 'Brackets' )
def O0oIi1iIiIi1I11 ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oO0o = 'https://www.apkfiles.com/search?q=' + ( IIi ) . replace ( ' ' , '+' ) + '&search_type=1'
 oo0OO = OoOo0oO0o . lower ( )
 Oo0o ( oo0OO )
 if 8 - 8: Ii1I
def o000 ( url ) :
 o00O0 = xbmc . translatePath ( os . path . join ( i11ii1 , 'Download' ) )
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
 if 4 - 4: Ii - Ii1IIIi1 % Ii1I * iiiiiiii1 % I11i
def o0OoOoo ( url ) :
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
 if 75 - 75: O0OOOoOoo0 * oOo0O0Ooo + O0OOOoOoo0 - ii
 if 81 - 81: iI11I1II1I1I / o000O0o . Ii * IIiIiII11i
def o0oOOoo0O ( name , url , description ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , name )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 OoooOo00 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print OoooOo00
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , OoooOo00 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 98 - 98: oO0o . iI11I1II1I1I % ii % I1ii11iIi11i - Ii1I
 if 86 - 86: OOooOOo . I1111IIi
 if 10 - 10: O0OOOoOoo0 * ii1ii11IIIiiI - I11i1ii1 . ooOOOoO - Ii1IIIi1
 if 94 - 94: oOo0O0Ooo % I1111IIi + oO0o
 if 90 - 90: ooOoO0O00 + o0o00Oo0O - o000O0o . O0OOOoOoo0 + iI11I1II1I1I
def iIi ( ) :
 i1i = OoOooO ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1i )
 for I1111i , Ii1I1Ii , iiO0oOo00o , o0ooooO0o0O , O0ooo0ooOoo0o in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , Ii1I1Ii , 80003 , iiO0oOo00o , III1iII1I1ii + 'APKToolsB.png' , O0ooo0ooOoo0o )
def iIiiIi1I11iI ( apk , ret = None ) :
 if apk == "kodi" :
  O0Oo00 = "https://kodi.tv/download/"
  i1i = OoOooO ( O0Oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1i )
  if len ( i1IIIII11I1IiI ) == 1 :
   Oo0o0ooOoO = i1IIIII11I1IiI [ 0 ] [ 0 ]
   iIIIi1IiI11I1 = i1IIIII11I1IiI [ 0 ] [ 1 ]
   iI1Ii11 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( Oo0o0ooOoO , iIIIi1IiI11I1 )
  if ret == 'version' : return Oo0o0ooOoO
  else : return iI1Ii11
 elif apk == "spmc" :
  Ooo0 = 'https://github.com/koying/SPMC/releases/latest/'
  i1i = OoOooO ( Ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1i )
  Oo0o0ooOoO = re . sub ( '<[^<]+?>' , '' , i1IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  iI1Ii11 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( Oo0o0ooOoO , Oo0o0ooOoO )
  if ret == 'version' : return Oo0o0ooOoO
  else : return iI1Ii11
def i1Ii1I1Ii11iI ( name , url , Brackets ) :
 if I1IIII1i ( ) == 'android' :
  IiiiIIi = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not IiiiIIi : I1IIIi ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  OoOooOo00O = name
  if IiiiIIi :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not Iii1 ( url ) == True : I1IIIi ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % OoOooOo00O , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    oO0O0 = zipfile . ZipFile ( oOO0O00Oo0O0o )
    for file in oO0O0 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as oooOo0OOOoo0 :
       oo0O0oOOO0o = file . split ( '/' ) [ 1 ]
       oooOo0OOOoo0 . write ( oO0O0 . read ( file ) )
       xbmc . sleep ( 500 )
       oooOo0OOOoo0 . close ( )
       try :
        os . remove ( oOO0O00Oo0O0o )
       except :
        pass
       oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , oo0O0oOOO0o )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : I1IIIi ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : I1IIIi ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 70 - 70: I1ii11iIi11i % ii1ii11IIIiiI . Ii1I
 if 8 - 8: oOo0O0Ooo - iiiiiiii1 * ooOOOoO % ii / OOooOOo
 if 15 - 15: I11i1ii1 . I11i + OOooOOo . iI11I1II1I1I % I11i1ii1 + o0o00Oo0O
 if 22 - 22: I11i + I1ii11iIi11i . I11i1ii1 + Ii1I * O0OOOoOoo0 . Ii
def O0OOOOOO0ooO ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1i )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Ii1I1Ii = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + Ii1I1Ii )
  II11IiI1 ( ( I1111i ) . replace ( '_' , ' ' ) , Ii1I1Ii )
  if 86 - 86: iI11I1II1I1I % o000O0o - OOooOOo + iiiiiiii1 % oO0o . Ii1I
def II11IiI1 ( name , url ) :
 if I1IIII1i ( ) == 'android' :
  IiiiIIi = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not IiiiIIi : I1IIIi ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  OoOooOo00O = name
  if IiiiIIi :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not Iii1 ( url ) == True : I1IIIi ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % OoOooOo00O , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : I1IIIi ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : I1IIIi ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 4 - 4: ooOoO0O00 + OOooOOo
 if 39 - 39: iI11I1II1I1I + I11i1ii1
def o00oOoo0o00 ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'INFO' )
 if 42 - 42: oO0o * Ii
 if 16 - 16: O0OOOoOoo0 % oOo0O0Ooo - I11i1ii1
def oOo0 ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 30015 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 100 - 100: ii * o000O0o
def OoO0o0OO ( url , iconimage , fanart ) :
 i1i = OoOooO ( url )
 I1I1i = url
 o00O0O = iconimage
 fanart = fanart
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for OoO , I1111i in i1IIIII11I1IiI :
  if '.mp4' in I1111i :
   OOiIiIIi1 ( 'Watch VIDEO' , url + '/' + OoO , 222 , o00O0O , fanart , '' )
  if 'description' in I1111i :
   OOiIiIIi1 ( 'Read Description' , url + '/' + OoO , 30017 , o00O0O , fanart , '' )
  if 'images' in I1111i :
   iiOOooooO0Oo ( 'View Images' , url + '/' + OoO , 30018 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Android' , url + '/' + OoO , 30016 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Pc' , url + '/' + OoO , 30019 , o00O0O , fanart , '' )
 I1I11i ( 'movies' , 'INFO' )
 if 10 - 10: o000O0o - O0OOOoOoo0 % IIiIiII11i - iiiiiiii1 - ooOoO0O00
def iIi11iI1i ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  Ii1iIi ( url )
  if 79 - 79: Ii1IIIi1 % iiiiiiii1 / o000O0o - iI11I1II1I1I - OOooOOo
def o0oOO ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  ooo0o0O ( url )
  if 32 - 32: ii % ii . o000O0o - I11i1ii1 . OOooOOo * o000O0o
def o0oooOo0oo ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1i )
 for i1iI1IIi1I in i1IIIII11I1IiI :
  OO0O000 ( 'Description:' , i1iI1IIi1I )
  if 52 - 52: ii / I1111IIi % IIiIiII11i
def Ii11I1I11II ( url ) :
 i1i = OoOooO ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for OoO , I1111i in i1IIIII11I1IiI :
  if 'png' in I1111i :
   OOiIiIIi1 ( 'image' , '' , '' , url + '/' + OoO , url + '/' + OoO , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 43 - 43: o000O0o + ii . I11i . Ii1I
def I1Iiii1Ii ( name , url , description ) :
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
 if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
 if 47 - 47: Ii1I * o000O0o + iI11I1II1I1I - o000O0o / I1111IIi
def ooo0o0O ( url ) :
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
 OOOO00o000o ( )
 if 86 - 86: I1111IIi
def Ii1iIi ( url ) :
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
 OOOO00o000o ( )
 if 43 - 43: oOo0O0Ooo / O0OOOoOoo0 / I11i1ii1 + iI11I1II1I1I + ii
def iiI111i1 ( name , url , description ) :
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
 OOOO00o000o ( )
 if 41 - 41: Ii * o0o00Oo0O - O0OOOoOoo0 . IIiIiII11i % oO0o % Ii1I
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
  I1I11iIi = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oooOo0OOOoo0 . write ( I1I11iIi . rstrip ( '\r\n' ) + '\n' )
def OOOO00o000o ( ) :
 iI11iI1IiiIiI = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iI11iI1IiiIiI == 0 : return
 elif iI11iI1IiiIiI == 1 : pass
 i1Iii = I1IIII1i ( )
 iIiIi11 ( "Platform: " + str ( i1Iii ) )
 os . _exit ( 1 )
 iIiIi11 ( "Force close failed!  Trying alternate methods." )
 if i1Iii == 'osx' :
  iIiIi11 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1Iii == 'linux' :
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
 elif i1Iii == 'android' :
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
 elif i1Iii == 'windows' :
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
  if 91 - 91: I11i1ii1 * I1111IIi * IIiIiII11i
  if 79 - 79: iiiiiiii1
  if 8 - 8: O0OOOoOoo0 - IIiIiII11i
def iI1iIIIIIiIi1 ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for ii1111I , i1I111II , Oo0OOo in os . walk ( url ) :
  for file in Oo0OOo :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    OoOOOOOO = open ( ( os . path . join ( ii1111I , file ) ) ) . read ( )
    iII1i1ii = OoOOOOOO . replace ( Oo0o0000o0o0 , 'special://home/' )
    oooOo0OOOoo0 = open ( ( os . path . join ( ii1111I , file ) ) , mode = 'w' )
    oooOo0OOOoo0 . write ( str ( iII1i1ii ) )
    oooOo0OOOoo0 . close ( )
 OOOO00o000o ( )
 if 30 - 30: Ii1I
def o00OOo ( ) :
 Iiiiii111i1ii ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 Iiiiii111i1ii ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 Iiiiii111i1ii ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 88 - 88: ooOoO0O00 % I11i1ii1 . Ii . ooOoO0O00
def ooO ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def OoOoO0oO00O ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def ooo0O ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1I :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']Filter - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , o00O0O )
def Ii1iiIIi1i ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def iIiiiI1I ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi
 iIII1I1ii = 'https://www.radionomy.com/en/search/index?query=' + ( IIi ) . replace ( ' ' , '+' )
 oO0OOoo0OO = OoOooO ( iIII1I1ii )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , o00O0O , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + Ii1I1Ii , 70005 , o00O0O )
  if 4 - 4: iI11I1II1I1I . ooOoO0O00
  if 63 - 63: iI11I1II1I1I + I1111IIi % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
def oo0o000o0oOO0 ( ) :
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , 'http://www.listenlive.eu/' + Ii1I1Ii , 10111113 , III1iII1I1ii + 'radio.png' )
def I1Ii1i11I1I ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  i1i1iII1 ( I1111i , url , 222 , III1iII1I1ii + 'radio.png' )
  if 60 - 60: I11i . OOooOOo % iiiiiiii1 / oOo0O0Ooo / o0o00Oo0O
def IiI ( ) :
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.toonjet.com/' + Ii1I1Ii , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii11I ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
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
   Iiiiii111i1ii ( ( o00O0O ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in i1I :
  Iiiiii111i1ii ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ooo0O00 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 53 - 53: o0o00Oo0O . oOo0O0Ooo
  if 74 - 74: I11i1ii1 % OOooOOo / I1ii11iIi11i
def II1IIiiI1 ( ) :
 iI1iiiIii1II1 ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 iI1iiiIii1II1 ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 2 - 2: I1111IIi % I1111IIi % iiiiiiii1
def o0o00OoOo0 ( ) :
 iI1iiiIii1II1 ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 iI1iiiIii1II1 ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 iI1iiiIii1II1 ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 98 - 98: ii % o000O0o * I11i1ii1
def OO0Oo00OO0oo ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , Ii1I1Ii , oOO00o0O0 in i1IIIII11I1IiI :
  if 'Parent' in I1111i :
   pass
  elif '2' in oOO00o0O0 :
   iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1I1Ii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 47 - 47: I11i1ii1
def Oo0oo ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , Ii1I1Ii , oOO00o0O0 in i1IIIII11I1IiI :
  if IIi in I1111i . lower ( ) :
   if '1' in oOO00o0O0 :
    iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1I1Ii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in oOO00o0O0 :
    iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1I1Ii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in oOO00o0O0 :
    iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1I1Ii , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 29 - 29: oOo0O0Ooo . Ii1IIIi1 + IIiIiII11i . I1ii11iIi11i
    if 29 - 29: ii1ii11IIIiiI - o0o00Oo0O . I11i1ii1 / Ii1I / ooOoO0O00 . OOooOOo
def II1iiiiI1 ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for I1111i , Ii1I1Ii , oOO00o0O0 in i1IIIII11I1IiI :
  if '1' in oOO00o0O0 :
   iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1I1Ii , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in oOO00o0O0 :
   iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1I1Ii , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in oOO00o0O0 :
   iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , Ii1I1Ii , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: I1111IIi + iI11I1II1I1I + oOo0O0Ooo + iiiiiiii1
def oOOoO0O ( url ) :
 OoO = url
 oO0OOoo0OO = OoOooO ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1I :
  if 'mp3' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in I1111i :
   iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OoO + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 76 - 76: ooOoO0O00 / iI11I1II1I1I - Ii1I - IIiIiII11i
   if 76 - 76: Ii + I1111IIi % OOooOOo
   if 6 - 6: O0OOOoOoo0
def ooOi11iii1Ii1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OoO = url
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
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OoO + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , OoO + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 86 - 86: I11i1ii1 / Ii
   if 49 - 49: Ii . iI11I1II1I1I - ooOoO0O00 . O0OOOoOoo0 + oO0o
def i111I1OOOo0Oo0O ( ) :
 iI1iiiIii1II1 ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 iI1iiiIii1II1 ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 iI1iiiIii1II1 ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 48 - 48: I11i1ii1 % OOooOOo
def ooOOoOOooO ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , o00O0O in i1IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + Ii1I1Ii + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in o00O0O :
   pass
  else :
   iI1iiiIii1II1 ( o00O0O , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( Ii1I1Ii ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + o00O0O + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 90 - 90: iiiiiiii1 . OOooOOo * IIiIiII11i % I11i1ii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: oOo0O0Ooo - I1ii11iIi11i % Ii1IIIi1 . ooOOOoO + ooOOOoO + ii1ii11IIIiiI
 if 28 - 28: I1ii11iIi11i / o000O0o * OOooOOo + Ii1I - iiiiiiii1
def Oo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 35 - 35: Ii + ii * iI11I1II1I1I . iiiiiiii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: O0OOOoOoo0 * ooOoO0O00 % ii * ii1ii11IIIiiI * oO0o
def I1iO0o0O0OooOoo ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if IIi in I1111i . lower ( ) :
   if '</a>' in I1111i :
    pass
   elif '(' in I1111i :
    iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ii1I1Ii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ii1I1Ii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 17 - 17: ii % o000O0o - ooOoO0O00 % I1111IIi % I1ii11iIi11i
    if 41 - 41: ii . iiiiiiii1 % OOooOOo - O0OOOoOoo0
def oOOooO ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ii1I1Ii , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + Ii1I1Ii , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 38 - 38: o0o00Oo0O
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: ooOoO0O00 . o000O0o
 if 34 - 34: iiiiiiii1 * IIiIiII11i
def o0oO00OOo0oO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OoO = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( OoO )
  if 92 - 92: oOo0O0Ooo . IIiIiII11i
def II1Ooo0000o00OO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  if '<p align' in I1111i :
   pass
  elif '&nbsp;' in I1111i :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 9 - 9: IIiIiII11i * Ii . Ii1IIIi1 - oO0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: Ii * ii1ii11IIIiiI . I11i % Ii1IIIi1 * Ii1I % o0o00Oo0O
 if 77 - 77: oO0o + oO0o . I11i1ii1 * ii + oO0o
def ooo ( ) :
 oO0OOoo0OO = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'ongoing' in Ii1I1Ii :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 21005 , III1iII1I1ii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in Ii1I1Ii :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 21005 , III1iII1I1ii + 'CartoonShows.png' , '' , '' )
  if 'disney' in Ii1I1Ii :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 21005 , III1iII1I1ii + 'Disney.png' , '' , '' )
  if 'genre' in Ii1I1Ii :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 21005 , III1iII1I1ii + 'Genre.png' , '' , '' )
  if 'years' in Ii1I1Ii :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 21005 , III1iII1I1ii + 'Years.png' , '' , '' )
def ii111I1i1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oooIiII = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , o00O0O , o00O0O , I1111i )
 for url , I1111i in oooIiII :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def iII1I ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oO0o000OoOoO0 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o00oOOo0Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0OOoo0OO )
 Oooo0o0oO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in o00oOOo0Oo :
  iiOOooooO0Oo ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , I1111i in oO0o000OoOoO0 :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def o0OOoOooO0ooO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 50 - 50: Ii + ii / o0o00Oo0O + I11i / Ii + o000O0o
def oooooOo0 ( ) :
 oO0OOoo0OO = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 i1IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if '9cart' in Ii1I1Ii :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 90 - 90: O0OOOoOoo0 * ii1ii11IIIiiI - O0OOOoOoo0 + oO0o + ooOOOoO % o0o00Oo0O
def i111IIIIiI ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if '9cart' in url :
   Iiiiii111i1ii ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   Iiiiii111i1ii ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url , I1111i in ooOoO00 :
  if '9cart' in url :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 75 - 75: Ii . I11i1ii1 % ooOoO0O00 . oOo0O0Ooo - o000O0o + I1ii11iIi11i
def OOoOoooOOO0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20003 , o00O0O )
 for url , I1111i in i1I :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 49 - 49: o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . IIiIiII11i % I1111IIi
def IIii1Ii1i1ii1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'Watch' in url :
   Iiiiii111i1ii ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 86 - 86: o000O0o % o0o00Oo0O + oO0o
def oO0OO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20005 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 88 - 88: oOo0O0Ooo
def oOO0Oo ( url ) :
 url = cloudflare . source ( url )
 OOOO00OooO ( url )
 if 5 - 5: Ii * O0OOOoOoo0 - ii1ii11IIIiiI - Ii1I - ooOoO0O00 + O0OOOoOoo0
def I1ii1i ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in i1IIIII11I1IiI :
  OOOO00OooO ( url )
  if 51 - 51: oO0o - O0OOOoOoo0 % o0o00Oo0O - OOooOOo
  if 53 - 53: O0OOOoOoo0 / ooOoO0O00 / ooOoO0O00
def OOOO0oooo ( ) :
 if 77 - 77: ooOOOoO + ooOoO0O00 . ooOOOoO
 iiOOooooO0Oo ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 89 - 89: I11i + Ii1IIIi1 * o000O0o
def iIIIiIii ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 45 - 45: O0OOOoOoo0 - I11i . ii1ii11IIIiiI
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO0OOoo0OO )
 if 41 - 41: IIiIiII11i . oOo0O0Ooo / oO0o . I11i1ii1
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if IIi in I1111i . lower ( ) :
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
    iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
    if 58 - 58: I1111IIi % Ii * IIiIiII11i . Ii1I
    if 94 - 94: Ii . Ii1IIIi1 + iI11I1II1I1I * iiiiiiii1 * iiiiiiii1
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 36 - 36: ooOOOoO - I1111IIi . I1111IIi
def O0o0O0OO00o ( url ) :
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
 if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
def ooo000o ( url ) :
 iIIII = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  OOOOOO = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10007 , OOOOOO )
  if 95 - 95: IIiIiII11i
  if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: I11i1ii1 % I11i / o000O0o - IIiIiII11i . iI11I1II1I1I
def ii1111Iii11i ( url , IMAGE ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   O0o0oo0O ( url )
   if 74 - 74: IIiIiII11i % ooOOOoO . oO0o * oO0o
   if 27 - 27: ooOOOoO * I1ii11iIi11i . ii1ii11IIIiiI . oOo0O0Ooo % IIiIiII11i - o000O0o
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 52 - 52: oOo0O0Ooo % oO0o * ii1ii11IIIiiI * O0OOOoOoo0 / Ii1IIIi1
def O0o0oo0O ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 88 - 88: o000O0o
  if 1 - 1: I1ii11iIi11i
  if 95 - 95: ii / ooOOOoO % ii / I11i1ii1 * I1111IIi
def IiIII1 ( ) :
 if 75 - 75: o0o00Oo0O
 iiOOooooO0Oo ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , O0o0Oo , '' )
 if 56 - 56: oO0o / IIiIiII11i
def IIIiiiiI1 ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'elete' in I1111i :
   pass
  else :
   i1i1iII1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 222 , o00O0O )
   if 40 - 40: o0o00Oo0O + I1111IIi . ii1ii11IIIiiI
def IIiIi ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 I1I1IIiiI1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , oooOOO0o0O0 , i1iII1IiiIiI1 in I1I1IIiiI1 :
  for IIi in oooOOO0o0O0 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iiiI1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for Ii1I1Ii , I1111i in iiiI1IiI :
    if 'tube' in Ii1I1Ii :
     pass
    elif 'stage' in Ii1I1Ii :
     i1i1iII1 ( '[COLOR' + II + ']' + oooOOO0o0O0 + '   -   ' + I1111i + '[/COLOR]' , ( Ii1I1Ii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O , )
    elif 'vee' in Ii1I1Ii :
     pass
     if 2 - 2: o0o00Oo0O % iiiiiiii1 % Ii1I % I11i - I1ii11iIi11i
def i1i11ii1 ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 I1I1IIiiI1 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , oooOOO0o0O0 , i1iII1IiiIiI1 in I1I1IIiiI1 :
  iiiI1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for Ii1I1Ii , I1111i in iiiI1IiI :
   if 'tube' in Ii1I1Ii :
    pass
   elif 'stage' in Ii1I1Ii :
    i1i1iII1 ( '[COLOR' + II + ']' + oooOOO0o0O0 + '   -   ' + I1111i + '[/COLOR]' , ( Ii1I1Ii ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O )
   elif 'vee' in Ii1I1Ii :
    pass
    if 95 - 95: Ii
    if 95 - 95: I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: oOo0O0Ooo
def i111I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OOO0oOoO0O = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( OOO0oOoO0O ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in OOO0oOoO0O :
  OOoO0ooOO ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 24 - 24: IIiIiII11i / ii1ii11IIIiiI . iI11I1II1I1I - IIiIiII11i % o0o00Oo0O
  if 8 - 8: oO0o % O0OOOoOoo0 . ii - ii1ii11IIIiiI % ii
  if 61 - 61: I11i / Ii
  if 28 - 28: Ii1IIIi1 / OOooOOo
  if 30 - 30: I11i1ii1
  if 57 - 57: I11i * Ii / OOooOOo
  if 40 - 40: iI11I1II1I1I - I11i1ii1 / I1ii11iIi11i
def Oo0OO0000oooo ( ) :
 if 24 - 24: o000O0o - O0OOOoOoo0 / I11i1ii1
 iIiiII1Ii1ii ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 iIiiII1Ii1ii ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 34 - 34: oOo0O0Ooo
 I1I11i ( 'movies' , 'MAIN' )
 if 57 - 57: Ii1IIIi1 . ii1ii11IIIiiI % I11i
def I1I11 ( ) :
 iIiiII1Ii1ii ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 iIiiII1Ii1ii ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 9 - 9: Ii1IIIi1
 I1I11i ( 'movies' , 'MAIN' )
def I1iII ( ) :
 if 18 - 18: ooOOOoO + I1ii11iIi11i - oO0o / iiiiiiii1 / Ii1IIIi1
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 oOoOo = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 53 - 53: Ii1IIIi1 + I11i . o000O0o / ooOOOoO
 for IiiI11i1I in oOoOo :
  OOo0 = O0Oo000ooO00 + IiiI11i1I + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( OOo0 )
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , o0ooooO0o0O , I1111i in i1IIIII11I1IiI :
   if IIi in I1111i . lower ( ) :
    o0000oO ( I1111i , Ii1I1Ii , 222 , IiI111ii1ii , o0ooooO0o0O , oo00O00oO000o )
    if 83 - 83: oO0o
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 16 - 16: I11i1ii1
    if 32 - 32: I11i % oOo0O0Ooo
def iII ( ) :
 if 23 - 23: IIiIiII11i * I1111IIi % oOo0O0Ooo - o000O0o
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 oOoOo = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 41 - 41: Ii1IIIi1 - o0o00Oo0O
 for IiiI11i1I in oOoOo :
  Iii1I = O0Oo000ooO00 + IiiI11i1I + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( Iii1I )
  i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1111i , oo00O00oO000o , Ii1I1Ii , o00O0O , o0ooooO0o0O , O0OOO0OOooo00 in i1IIIII11I1IiI :
   if IIi in I1111i . lower ( ) :
    iIiiII1Ii1ii ( I1111i , Ii1I1Ii , O0OOO0OOooo00 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
    if 77 - 77: Ii1I % IIiIiII11i
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 81 - 81: OOooOOo % ii1ii11IIIiiI / o0o00Oo0O * iI11I1II1I1I % I1111IIi . oOo0O0Ooo
    if 90 - 90: I11i
def IIiII ( ) :
 if 39 - 39: I11i / I1111IIi - O0OOOoOoo0
 iIIII = OoOooO ( O0Oo000ooO00 + 'spongemain.php' )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oo00O00oO000o , Ii1I1Ii , o00O0O , o0ooooO0o0O , O0OOO0OOooo00 in i1IIIII11I1IiI :
  iIiiII1Ii1ii ( I1111i , Ii1I1Ii , O0OOO0OOooo00 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
  I1I11i ( 'movies' , 'MAIN' )
def O00OO00OOOoO ( url ) :
 if 47 - 47: ooOoO0O00 % I11i1ii1 - I1ii11iIi11i * ooOOOoO / Ii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 Iii1Iii = ( '%s%s' % ( iiI11111II , url ) )
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in i1IIIII11I1IiI :
  iiIii1IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
  for i11I in iiIii1IIi :
   if i11I == url :
    I1111i = ( '[COLORred]Watched - [/COLOR]' + I1111i ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  o0000oO ( I1111i , url , 222 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
  if 48 - 48: O0OOOoOoo0 % Ii . ii * I1111IIi % oO0o . O0OOOoOoo0
  I1I11i ( 'movies' , 'MAIN' )
  if 6 - 6: o0o00Oo0O . I11i1ii1 - o000O0o / Ii
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 84 - 84: ooOOOoO / Ii1I * I11i * oO0o * Ii1IIIi1 * o0o00Oo0O
  if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
def Ooi1IIii1i ( url ) :
 if 60 - 60: ii1ii11IIIiiI % I1ii11iIi11i / ooOOOoO . O0OOOoOoo0 / iiiiiiii1 - ii
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oo00O00oO000o , url , o00O0O , o0ooooO0o0O , O0OOO0OOooo00 in i1IIIII11I1IiI :
  iIiiII1Ii1ii ( I1111i , url , O0OOO0OOooo00 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
  if 76 - 76: o0o00Oo0O
  I1I11i ( 'movies' , 'MAIN' )
  if 71 - 71: oOo0O0Ooo . ooOoO0O00
  if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + o000O0o + o000O0o + O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 4 - 4: I11i + ooOOOoO / O0OOOoOoo0 + ooOoO0O00 % I11i % O0OOOoOoo0
def o0000oO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 80 - 80: ii1ii11IIIiiI
 i1ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0O = True
 oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iiiIIiIi = [ ]
  iiiIIiIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iiiIIiIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   iiiIIiIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOO . addContextMenuItems ( iiiIIiIi )
 oO0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = False )
 return oO0O
 if 26 - 26: iI11I1II1I1I . ii - iI11I1II1I1I
def iIiiII1Ii1ii ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 59 - 59: Ii1I + ooOOOoO . o000O0o
 i1ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0O = True
 oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iiiIIiIi = [ ]
  iiiIIiIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iiiIIiIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   iiiIIiIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOO . addContextMenuItems ( iiiIIiIi )
 oO0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = True )
 return oO0O
if 87 - 87: oO0o
if 34 - 34: iiiiiiii1 . OOooOOo / Ii / O0OOOoOoo0
if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + Ii1IIIi1
if 31 - 31: ii1ii11IIIiiI * I11i * ii1ii11IIIiiI + oO0o * I11i . iiiiiiii1
if 89 - 89: ii * ii1ii11IIIiiI * oOo0O0Ooo . I11i1ii1 * ii1ii11IIIiiI / O0OOOoOoo0
if 46 - 46: Ii
if 15 - 15: o0o00Oo0O / ooOoO0O00 / ooOoO0O00 . O0OOOoOoo0 % OOooOOo + oOo0O0Ooo
if 48 - 48: iiiiiiii1 % O0OOOoOoo0 % ii1ii11IIIiiI % iI11I1II1I1I . ii1ii11IIIiiI
if 14 - 14: O0OOOoOoo0 * oO0o % o0o00Oo0O + ooOOOoO + Ii1I
if 23 - 23: I1ii11iIi11i % O0OOOoOoo0 + ii1ii11IIIiiI - iiiiiiii1
if 65 - 65: ii
if 22 - 22: Ii1IIIi1 + IIiIiII11i + I1ii11iIi11i
if 83 - 83: I11i1ii1
if 43 - 43: Ii1IIIi1
if 84 - 84: Ii1IIIi1 . I1111IIi . O0OOOoOoo0
def iIII1I1i ( string ) :
 if OOoOO0oo0ooO == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 26 - 26: O0OOOoOoo0 - I1ii11iIi11i + oOo0O0Ooo + I11i
def III1iI1Ii11Ii ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 iI11iIi = [ ]
 try :
  if 82 - 82: I1ii11iIi11i / oOo0O0Ooo . Ii1I - I1ii11iIi11i
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( IIIii1II1II ) == False :
  iIII1I1i ( 'Making Favorites File' )
  iI11iIi . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  OoOOOOOO = open ( IIIii1II1II , "w" )
  OoOOOOOO . write ( json . dumps ( iI11iIi ) )
  OoOOOOOO . close ( )
 else :
  iIII1I1i ( 'Appending Favorites' )
  OoOOOOOO = open ( IIIii1II1II ) . read ( )
  Iii1o00o0 = json . loads ( OoOOOOOO )
  Iii1o00o0 . append ( ( name , url , iconimage , fanart , mode ) )
  iII1i1ii = open ( IIIii1II1II , "w" )
  iII1i1ii . write ( json . dumps ( Iii1o00o0 ) )
  iII1i1ii . close ( )
  if 84 - 84: OOooOOo - I1ii11iIi11i . I11i1ii1 . I1111IIi - I1ii11iIi11i
  if 99 - 99: iiiiiiii1
def o0I1IiiiiI1i1I ( ) :
 if os . path . exists ( IIIii1II1II ) == False :
  iI11iIi = [ ]
  iIII1I1i ( 'Making Favorites File' )
  iI11iIi . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  OoOOOOOO = open ( IIIii1II1II , "w" )
  OoOOOOOO . write ( json . dumps ( iI11iIi ) )
  OoOOOOOO . close ( )
 else :
  I11i1I1 = json . loads ( open ( IIIii1II1II ) . read ( ) )
  ooOooO = len ( I11i1I1 )
  for oooo in I11i1I1 :
   I1111i = oooo [ 0 ]
   Ii1I1Ii = oooo [ 1 ]
   IiI111ii1ii = oooo [ 2 ]
   try :
    IIIiI1iIIII = oooo [ 3 ]
    if IIIiI1iIIII == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     IIIiI1iIIII = IiI111ii1ii
    else :
     IIIiI1iIIII = o0ooooO0o0O
   try : o0oo00OOOo = oooo [ 5 ]
   except : o0oo00OOOo = None
   try : oo0oO = oooo [ 6 ]
   except : oo0oO = None
   if 17 - 17: I11i1ii1 + I11i1ii1 . Ii1I
   if oooo [ 4 ] == 0 :
    iiOOooooO0Oo ( I1111i , Ii1I1Ii , '' , IiI111ii1ii , o0ooooO0o0O , '' , 'fav' )
   else :
    iiOOooooO0Oo ( I1111i , Ii1I1Ii , oooo [ 4 ] , IiI111ii1ii , o0ooooO0o0O , '' , 'fav' )
    if 50 - 50: iI11I1II1I1I * o000O0o
def o0Oo ( name ) :
 Iii1o00o0 = json . loads ( open ( IIIii1II1II ) . read ( ) )
 for III1IIiIi1 in range ( len ( Iii1o00o0 ) ) :
  if Iii1o00o0 [ III1IIiIi1 ] [ 0 ] == name :
   del Iii1o00o0 [ III1IIiIi1 ]
   iII1i1ii = open ( IIIii1II1II , "w" )
   iII1i1ii . write ( json . dumps ( Iii1o00o0 ) )
   iII1i1ii . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 97 - 97: I11i / I1111IIi + OOooOOo + oO0o % iiiiiiii1
 if 18 - 18: oOo0O0Ooo - OOooOOo
def o0o0OoO0OOO0 ( ) :
 II1III = os . path . join ( I11i1 , 'addons.ini' )
 II11iiIIiI11I = open ( II1III , "w+" )
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oO0OOoo0OO )
 II11iiIIiI11I . write ( r'[' + IiII + ']' + '\n' )
 for I1111i , o00O0O , OoO0o00oo0oO , Ii1I1Ii in i1IIIII11I1IiI :
  Ii1I1Ii = ( Ii1I1Ii + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  I11IiIi1iI1ii = ( I1111i + '=plugin://' + IiII + '/?url=' + Ii1I1Ii + '&mode=10012&name=' + ( I1111i ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;description=' )
  II11iiIIiI11I . write ( I11IiIi1iI1ii + '\n' )
  if 68 - 68: I1111IIi * oO0o . ooOOOoO / ii1ii11IIIiiI . I11i - Ii
  if 49 - 49: I1ii11iIi11i / ii1ii11IIIiiI % ooOOOoO + o000O0o - oO0o
def i11ii ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '24/7' , Ii1I1Ii , 90021 , III1iII1I1ii + '247Streams.png' )
  if 42 - 42: ii1ii11IIIiiI * o0o00Oo0O / o000O0o
def IiiiI11 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , Ii1I1Ii in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( Ii1I1Ii ) . strip ( ) , 222 , III1iII1I1ii + '247Streams.png' , III1iII1I1ii + '247Streams.png' , '' )
def Ii11III ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , Ii1I1Ii in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( Ii1I1Ii ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def iIIiiiI ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , Ii1I1Ii in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( Ii1I1Ii ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def OoooOOo0oOO ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , Ii1I1Ii in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( Ii1I1Ii ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def i1iiIIiiiI ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 i1IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , Ii1I1Ii , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 26 - 26: I11i1ii1 % o000O0o + oOo0O0Ooo / I1111IIi . oOo0O0Ooo
  if 38 - 38: ii + ii - Ii * oOo0O0Ooo * ooOoO0O00 / IIiIiII11i
def OOO00000O ( ) :
 if 23 - 23: I1ii11iIi11i - o0o00Oo0O
 iiOOooooO0Oo ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 if 33 - 33: Ii1I
def O0oOoo00Oo0O ( ) :
 if 5 - 5: o0o00Oo0O - O0OOOoOoo0 / iiiiiiii1 . I11i
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii , o00O0O , I1111i , ii1O0ooooo000 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + '  -  ' + ( ii1O0ooooo000 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Ii1I1Ii , 10023 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 7 - 7: Ii1I - OOooOOo
  if 54 - 54: o000O0o / iI11I1II1I1I / ii . ooOoO0O00 - OOooOOo
  if 57 - 57: iI11I1II1I1I * ii1ii11IIIiiI * O0OOOoOoo0 / o000O0o
def iIIiII1i1ii ( ) :
 if 57 - 57: I11i1ii1 + iiiiiiii1
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
 if 49 - 49: OOooOOo * ii
def i1III ( url ) :
 I1I1i = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0OOoo0OO = cloudflare . source ( I1I1i )
 i1IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 19 - 19: ooOoO0O00 % oOo0O0Ooo - iI11I1II1I1I - o000O0o / Ii1I
  if 16 - 16: ii1ii11IIIiiI
  if 79 - 79: ii - I11i1ii1 * ii1ii11IIIiiI - IIiIiII11i % OOooOOo * I1111IIi
  if 31 - 31: oOo0O0Ooo
def IIII1I1 ( ) :
 if 36 - 36: ii1ii11IIIiiI * ooOOOoO . ooOOOoO / I1ii11iIi11i / oOo0O0Ooo
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 Ii1I1Ii = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( IIi ) . replace ( ' ' , '+' )
 oO0OOoo0OO = cloudflare . source ( Ii1I1Ii )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , o00O0O , I1111i in i1IIIII11I1IiI :
  if IIi in I1111i . lower ( ) :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 10022 , III1iII1I1ii + 'dtv.png' )
   if 80 - 80: ii - ooOoO0O00
   if 51 - 51: ooOoO0O00 . OOooOOo / OOooOOo % Ii * Ii1IIIi1 - iiiiiiii1
   if 49 - 49: I1ii11iIi11i - iI11I1II1I1I
def o0oo0o ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO , IiIi1ii111i1 , oooiI1i , I1111i in i1IIIII11I1IiI :
  o0Ii11I1iIIi = ( oooiI1i ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  O0ooO = ( IiIi1ii111i1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  iI = 'Season ' + O0ooO + 'Episode ' + o0Ii11I1iIIi + I1111i
  OOI1III1I11I1 ( iI , OoO )
  if 85 - 85: iiiiiiii1
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 62 - 62: ii1ii11IIIiiI % IIiIiII11i + I1111IIi + Ii1IIIi1 % o000O0o . oOo0O0Ooo
  if 53 - 53: oO0o % Ii1I . O0OOOoOoo0 . ooOoO0O00 . oO0o
def OOI1III1I11I1 ( name , url ) :
 OoO = url
 iiII1II11i = name
 O0 = cloudflare . source ( OoO )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for OOO0oOoO0O , ooO0 in i1I :
  i1i1iII1 ( '[COLOR' + II + ']' + iiII1II11i + ooO0 + '[/COLOR]' , OOO0oOoO0O , 222 , III1iII1I1ii + 'dtv.png' )
  if 78 - 78: oOo0O0Ooo * ooOoO0O00 / oOo0O0Ooo / oO0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: I1ii11iIi11i / I1111IIi . O0OOOoOoo0 + oO0o + ooOOOoO % I1ii11iIi11i
 if 45 - 45: I1ii11iIi11i / o0o00Oo0O % ii
def O00 ( ) :
 if 92 - 92: ii1ii11IIIiiI . OOooOOo . ooOOOoO - ii / I11i1ii1
 if 80 - 80: iI11I1II1I1I / Ii + O0OOOoOoo0
 if 41 - 41: iiiiiiii1 + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
 if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
 if 25 - 25: ii . ii1ii11IIIiiI % O0OOOoOoo0 . I1111IIi
 if 67 - 67: ii + iiiiiiii1 / I11i1ii1
 if 75 - 75: I1111IIi / ii . oOo0O0Ooo + iiiiiiii1 - IIiIiII11i
 iiOOooooO0Oo ( '[COLOR' + II + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , '' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 33 - 33: I1111IIi / I1111IIi . Ii * Ii1I + I11i
def ii1iI11IiIIi ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 III = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + o00O0O , '' , '' )
 for url in III :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 62 - 62: ooOOOoO + ii * iI11I1II1I1I / ooOoO0O00 * o0o00Oo0O
def iiiiIi11II11 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 III = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  o00O0O = 'http://watchepisodes.cc/' + o00O0O
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10093 , o00O0O , o00O0O , '' )
 for url in III :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 14 - 14: Ii1I - Ii * iiiiiiii1
def iiii ( url , iconimage ) :
 o00O0O = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oooiI1i , url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + oooiI1i + ' - ' + I1111i + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , o00O0O , '' , '' )
  if 80 - 80: oOo0O0Ooo
def oO0OOo ( url , iconimage ) :
 o00O0O = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  if 'player' in I1111i :
   pass
  elif 'vod' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , o00O0O , '' , '' )
   if 63 - 63: IIiIiII11i . iiiiiiii1 % I1111IIi + IIiIiII11i
   if 81 - 81: Ii1IIIi1 - oOo0O0Ooo % I11i
   if 7 - 7: I11i1ii1 - ooOoO0O00 . OOooOOo
   if 12 - 12: I1111IIi / oO0o / o0o00Oo0O * I1111IIi
   if 51 - 51: I11i1ii1 * O0OOOoOoo0 / ooOoO0O00
   if 2 - 2: o000O0o + I1111IIi . O0OOOoOoo0 - ooOoO0O00 + iiiiiiii1
def Oo0o0000OOoO ( ) :
 if 54 - 54: ii . o000O0o - O0OOOoOoo0
 if 76 - 76: iiiiiiii1
 if 61 - 61: I11i1ii1 / IIiIiII11i * I11i1ii1 * OOooOOo * iiiiiiii1 . Ii
 if 26 - 26: iiiiiiii1 / I11i1ii1 - oO0o . iI11I1II1I1I
 if 83 - 83: I11i1ii1 % ii1ii11IIIiiI / I1ii11iIi11i - O0OOOoOoo0 / o0o00Oo0O
 if 97 - 97: iI11I1II1I1I * ooOOOoO
 if 95 - 95: oO0o
 if 68 - 68: iI11I1II1I1I . iI11I1II1I1I / OOooOOo - IIiIiII11i - iI11I1II1I1I
 if 75 - 75: I11i1ii1 . oOo0O0Ooo * IIiIiII11i
 if 99 - 99: iI11I1II1I1I * Ii1I + I1111IIi
 if 70 - 70: ooOoO0O00 % I11i1ii1 . Ii1I - I1111IIi + Ii1IIIi1
 if 84 - 84: o000O0o + IIiIiII11i * IIiIiII11i % I11i / O0OOOoOoo0 + I11i1ii1
 if 9 - 9: O0OOOoOoo0
 if 25 - 25: Ii1IIIi1 - ii1ii11IIIiiI . ooOOOoO
 iiOOooooO0Oo ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , III1iII1I1ii + 'latest.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , III1iII1I1ii + 'popular.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , III1iII1I1ii + 'Genre.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , III1iII1I1ii + 'series.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 if 57 - 57: I11i + I1ii11iIi11i * Ii1I - I11i1ii1 % iI11I1II1I1I - ii1ii11IIIiiI
 if 37 - 37: oO0o * ooOOOoO + ii1ii11IIIiiI + Ii1I * I11i
def O00oOo0o0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I1IIIiI1I1ii1 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
 for url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 81 - 81: IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * Ii + OOooOOo
def oo0OoOO000O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 62 - 62: ooOoO0O00 * iI11I1II1I1I % o000O0o % OOooOOo / ii
def iI1111iiI1 ( url ) :
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
  if 71 - 71: I11i % Ii1IIIi1 + o0o00Oo0O / Ii1I
  if 88 - 88: ooOOOoO / I1ii11iIi11i - iiiiiiii1
def I1iIi1IiI1i ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiiIiiiiI1III = 'http://www.watchseriesgo.to/search/' + IIi . replace ( ' ' , '%20' )
 oO0OOoo0OO = OoOooO ( IiiIiiiiI1III )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'watch online' in I1111i :
   pass
  else :
   print Ii1I1Ii
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to' + Ii1I1Ii , 10044 , o00O0O , '' , '' )
   if 42 - 42: o000O0o - I11i1ii1 * ooOOOoO % O0OOOoOoo0 * I1ii11iIi11i / iiiiiiii1
   xbmcplugin . setContent ( O000oo0O , 'movies' )
   if 94 - 94: I11i1ii1 + iI11I1II1I1I
def OOo0Oo0O00O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , oooiI1i , oo00O00oO000o in i1IIIII11I1IiI :
  ii1iii1I1I = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( oooiI1i ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ii1iii1I1I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , o00O0O , '' , oo00O00oO000o )
  if 56 - 56: Ii1I + o000O0o . oO0o + ii * Ii1I - o0o00Oo0O
def I1iO00O000oOO0oO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  ii1iii1I1I = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ii1iii1I1I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 88 - 88: I11i . oOo0O0Ooo % o000O0o . I1ii11iIi11i % I11i1ii1 . o000O0o
def OoO0ooOOoo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , o00O0O , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 95 - 95: I1ii11iIi11i * Ii1IIIi1 + oOo0O0Ooo . o0o00Oo0O
def IIiIi1II1IiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 I1IIIiI1I1ii1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for IiIi1ii111i1 , I1I1IIiiI1 in I1IIIiI1I1ii1 :
  i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( I1I1IIiiI1 ) )
  for url , I1111i in i1IIIII11I1IiI :
   ii1iii1I1I = ( IiIi1ii111i1 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ii1iii1I1I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 99 - 99: I1ii11iIi11i
class IiIi1I11 ( ) :
 if 19 - 19: ooOoO0O00 / I1111IIi + Ii1I * Ii1I
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 90 - 90: ii * O0OOOoOoo0 . Ii . I11i1ii1 - iiiiiiii1
  ii1iii1I1I = name
  self . Get_Sources ( Ii1I1Ii , ii1iii1I1I )
  if 81 - 81: oOo0O0Ooo / ii
  if 52 - 52: o000O0o + iiiiiiii1 * iiiiiiii1 * I1ii11iIi11i - iI11I1II1I1I + Ii1I
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  oO0OOoo0OO = OoOooO ( URL )
  i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + Ii1I1Ii
   self . Get_site_link ( URL , season_name )
   if 34 - 34: O0OOOoOoo0 / oO0o / I1ii11iIi11i
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
   if 92 - 92: iiiiiiii1 % O0OOOoOoo0 % I11i . oOo0O0Ooo - Ii1I - I11i
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   IiIi = 'DACLIPS'
   if IiIi in IiIi1I11 . source_list :
    pass
   else :
    self . daclips ( url , season_name , IiIi )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    IiIi = 'THEVIDEO'
    if IiIi in IiIi1I11 . source_list :
     pass
    else :
     self . thevideo ( url , season_name , IiIi )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     IiIi = 'ALLMYVIDEOS'
     if IiIi in IiIi1I11 . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , IiIi )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      IiIi = 'VIDSPOT'
      if IiIi in IiIi1I11 . source_list :
       pass
      else :
       self . vidspot ( url , season_name , IiIi )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       IiIi = 'VODLOCKER'
       if IiIi in IiIi1I11 . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , IiIi )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        IiIi = 'VIDTO'
        if IiIi in IiIi1I11 . source_list :
         pass
        else :
         self . vidto ( url , season_name , IiIi )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 95 - 95: o0o00Oo0O + iI11I1II1I1I . Ii1I
       else :
        if 'youwatch' in url :
         IiIi = 'YouWatch'
         if IiIi in IiIi1I11 . source_list :
          pass
         else :
          self . youwatch ( url , season_name , IiIi )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 61 - 61: ii1ii11IIIiiI * ii1ii11IIIiiI
          if 70 - 70: iiiiiiii1 . Ii1I / I11i * o000O0o
 def allmyvid ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1iooo , I1111i in i1IIIII11I1IiI :
   self . Printer ( I1iooo , season_name , source_name )
   if 74 - 74: oOo0O0Ooo . I11i1ii1 / O0OOOoOoo0 . I1111IIi
 def vidspot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for I1iooo , I1111i in i1IIIII11I1IiI :
   self . Printer ( I1iooo , season_name , source_name )
   if 74 - 74: I1ii11iIi11i / iiiiiiii1 % iiiiiiii1 . I1111IIi
 def thevideo ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( oO0OOoo0OO )
  for I1iooo in i1IIIII11I1IiI :
   self . Printer ( I1iooo , season_name , source_name )
   if 72 - 72: ooOoO0O00
 def vodlocker ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for I1iooo in i1IIIII11I1IiI :
   self . Printer ( I1iooo , season_name , source_name )
   if 21 - 21: iiiiiiii1 . Ii1IIIi1 / Ii * ooOoO0O00
 def daclips ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oO0OOoo0OO )
  for I1iooo in i1IIIII11I1IiI :
   self . Printer ( I1iooo , season_name , source_name )
   if 82 - 82: I11i1ii1 * I1ii11iIi11i % Ii * ooOoO0O00 . Ii1IIIi1
 def filehoot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for I1iooo in i1IIIII11I1IiI :
   self . Printer ( I1iooo , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for I1iooo in i1IIIII11I1IiI :
   self . Printer ( I1iooo , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for I1iooo in i1IIIII11I1IiI :
   self . youplay ( I1iooo , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for I1iooo in i1IIIII11I1IiI :
   self . Printer ( I1iooo , season_name , source_name )
   if 89 - 89: I1111IIi - ooOoO0O00 - I1111IIi
 def Printer ( self , Link , season_name , source_name ) :
  if 74 - 74: oO0o % oO0o
  if Link in IiIi1I11 . List :
   pass
  elif source_name in IiIi1I11 . source_list :
   pass
  else :
   i1i1iII1 ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 222 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   IiIi1I11 . List . append ( Link )
   IiIi1I11 . source_list . append ( source_name )
   if 28 - 28: OOooOOo % o000O0o - Ii1IIIi1 + Ii1IIIi1 + o000O0o / iI11I1II1I1I
   xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 91 - 91: oOo0O0Ooo / IIiIiII11i * Ii1IIIi1
   if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
   if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % ii1ii11IIIiiI
   if 81 - 81: oO0o - iI11I1II1I1I
   if 60 - 60: iiiiiiii1
def iIiIiIiI ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 77 - 77: oOo0O0Ooo / Ii1I
def o0OoOOoooooOO ( url ) :
 iiOOooooO0Oo ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( iIIII )
 for oOOo , url , oOOOo0Oooo , I1iiIIiI11I , I11II1I , OOoO0oO00o , oOoOo000 , oooOo0OOOoo0 , OoOOOOOO , iiI1IiI1I1I , IIIiI1i in i1IIIII11I1IiI :
  oOOOo0Oooo = oOOOo0Oooo
  if 'Arsenal' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'arsenal-logo.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                                  ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Bournemouth' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'afc-bournemouth.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                       ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Burnley' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'KEGnQWW.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                                   ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Chelsea' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'chelsea.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                                  ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Crystal' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'CrystalPalace.0.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                       ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Everton' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'Everton.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                                   ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Hull' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'hull-city-afc.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                                 ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Leicester' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'leicester-city-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                       ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Liverpool' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'liverpool-logo.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                               ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Manchester City' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'city-logo.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '               ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Manchester United' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + '91.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '          ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Middlesbrough' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'middlesbrough-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                 ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Southampton' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'southampton-fc-logo.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                   ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Stoke City' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'stoke-city.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                          ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Sunderland' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'sunderland-logo.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                        ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Swansea' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'swansea-city-afc.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                    ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Tottenham' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'tottenham-hotspur_zps4e3ed7c1.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '        ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Watford' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'watford-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '                              ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'Bromwich' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'west-bromwich-albion-logo.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '   ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  elif 'West Ham' in oOOOo0Oooo :
   I111iIi1 = III1iII1I1ii + 'west-ham.png'
   I1111i = '[COLOR' + II + ']' + oOOo + ' - ' + oOOOo0Oooo + '             ' + I1iiIIiI11I + '        ' + I11II1I + '        ' + OOoO0oO00o + '        ' + oOoOo000 + '        ' + oooOo0OOOoo0 + '        ' + OoOOOOOO + '        ' + iiI1IiI1I1I + '[/COLOR]'
  iiOOooooO0Oo ( str ( I1111i ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , I111iIi1 , I111iIi1 , oOOOo0Oooo )
  if 22 - 22: I1111IIi / Ii1IIIi1
def O0OOoooO ( description ) :
 oOOOo0Oooo = description
 Ii1I1Ii = ( 'http://www.fullmatchesandshows.com/?s=' + oOOOo0Oooo ) . replace ( ' ' , '%20' )
 IIiiIiIIiI1 ( Ii1I1Ii )
 if 39 - 39: ooOOOoO / ii - ii1ii11IIIiiI + oO0o / OOooOOo
def oo0O0000oo0o0 ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 i1IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii , o00O0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + Ii1I1Ii , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o00O0O , O0o0Oo , '' )
  if 32 - 32: ii / O0OOOoOoo0 / iiiiiiii1 + O0OOOoOoo0 - ooOOOoO + IIiIiII11i
def IiIIIiII1111 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I1IIIiI1I1ii1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
  o00o0oOo0O0O = re . compile ( '(.*?)</h2>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for o0oOOoo in o00o0oOo0O0O :
   o0oOOoo = o0oOOoo
  OOo000O000ooo = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for i111i11iI1i1I , o00O0O , time , IiI1 in OOo000O000ooo :
   iiIiiIi1 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( IiI1 )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + o0oOOoo + ' - ' + i111i11iI1i1I + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + o00O0O , O0o0Oo , ( str ( iiIiiIi1 ) ) )
   if 49 - 49: ooOoO0O00 . oO0o / Ii + ii1ii11IIIiiI % o0o00Oo0O + Ii1I
 I1I11i ( 'tvshows' , 'Media Info 3' )
 if 14 - 14: ooOOOoO - I1ii11iIi11i . I1ii11iIi11i * Ii1IIIi1 . oOo0O0Ooo % O0OOOoOoo0
def OO00OO ( ) :
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
 if 27 - 27: o0o00Oo0O * oOo0O0Ooo - iI11I1II1I1I - O0OOOoOoo0 % o0o00Oo0O . I1ii11iIi11i
def I1ii11IiI1I ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  Oo0Ii = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   Oo0Ii = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   i1i1iII1 ( '[COLOR' + II + ']' + Oo0Ii + '[/COLOR]' , url , 10013 , o00O0O )
 for url , o00O0O , I1111i in i1I :
  Oo0Ii = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   i1i1iII1 ( '[COLOR' + II + ']' + Oo0Ii + '[/COLOR]' , url , 10013 , o00O0O )
def IIiiIiIIiI1 ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 if 96 - 96: ii1ii11IIIiiI
 if 24 - 24: o0o00Oo0O
 if 33 - 33: ii + o000O0o * IIiIiII11i / Ii1IIIi1
 if 87 - 87: ii
 if 1 - 1: iI11I1II1I1I / I11i
 if 98 - 98: o0o00Oo0O % oOo0O0Ooo / ii * Ii1I - o000O0o
 if 51 - 51: O0OOOoOoo0 + ooOOOoO
 for url , o00O0O , I1111i in i1I :
  Oo0Ii = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   i1i1iII1 ( '[COLOR' + II + ']' + Oo0Ii + '[/COLOR]' , url , 10013 , o00O0O )
   if 54 - 54: IIiIiII11i * o0o00Oo0O % oOo0O0Ooo . ooOOOoO
def O0ooO0O00oo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oO0OOoo0OO )
 for OOO0oOoO0O in i1IIIII11I1IiI :
  II1i1iI = ( OOO0oOoO0O ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOoO0ooOO ( 'http:' + II1i1iI )
  if 5 - 5: OOooOOo + O0OOOoOoo0 * I11i1ii1
  if 47 - 47: iI11I1II1I1I + oO0o % iI11I1II1I1I . I11i1ii1 / I1ii11iIi11i - Ii
  if 80 - 80: Ii1I / o0o00Oo0O / iI11I1II1I1I + oOo0O0Ooo
  if 3 - 3: I11i1ii1 / ooOoO0O00 - OOooOOo
def oo0o0ooOoo00O ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  i1i1iII1 ( I1111i , url , 8046 , o00O0O )
 for url in i1I :
  Iiiiii111i1ii ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def iI1ii1 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  OOoO0ooOO ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 81 - 81: I11i1ii1 + oO0o . ooOoO0O00 + ooOoO0O00 / oOo0O0Ooo * iiiiiiii1
def OOooooO0 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 23 - 23: O0OOOoOoo0 / OOooOOo + I11i . o0o00Oo0O
def O0Oo000 ( ) :
 Iiiiii111i1ii ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , III1iII1I1ii + 'documentary.png' )
 Iiiiii111i1ii ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , III1iII1I1ii + 'documentary.png' )
 Iiiiii111i1ii ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , III1iII1I1ii + 'Search.png' )
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , Ii1I1Ii , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOoO00oo0ooOo0 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + o00O0O )
 for url in next :
  Iiiiii111i1ii ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 49 - 49: IIiIiII11i
  if 33 - 33: I11i - o000O0o % Ii1I * ooOOOoO . ii % ii1ii11IIIiiI
def I1iiiiI ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   i1i1iII1 ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   Iiiiii111i1ii ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def o0oOOO0 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  i1i1iII1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , '' )
  if 11 - 11: ooOOOoO / OOooOOo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii1IIi1IIIIi1 ( name , url ) :
 iI1i1iii = 0
 name = name
 url = url
 i111I1 = [ '144' , '240' , '380' , '480' , '720' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  OOOOo0o00OO0000 ( url )
  if 16 - 16: ooOoO0O00 * I11i1ii1 % oO0o + ii1ii11IIIiiI
  if 50 - 50: o000O0o - ii + O0OOOoOoo0 % oO0o
  if 12 - 12: ooOoO0O00 / Ii1I - O0OOOoOoo0 . Ii / ooOoO0O00 / ii
  if 88 - 88: ii1ii11IIIiiI / Ii % OOooOOo % Ii1IIIi1
  if 70 - 70: Ii1I . Ii1I / ooOOOoO . Ii1I
  if 37 - 37: ooOoO0O00 . iiiiiiii1 - IIiIiII11i % I11i - ooOoO0O00 . o000O0o
  if 34 - 34: iI11I1II1I1I / IIiIiII11i
  if 3 - 3: I11i - ii + O0OOOoOoo0 . ooOOOoO
def o00000Oo ( ) :
 iIIII = o0O0O0ooo0oOO ( 'http://documentarylovers.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( iIIII )
 for I1111i , Ii1I1Ii in i1IIIII11I1IiI :
  if 'genre' in Ii1I1Ii :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , Ii1I1Ii , 80010 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoOoooOO00OO ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , o00O0O )
 for url in next :
  Iiiiii111i1ii ( 'NEXT PAGE' , url , 80010 , III1iII1I1ii + 'Next.png' )
  if 76 - 76: Ii1I + Ii1IIIi1 % o0o00Oo0O * Ii . o0o00Oo0O . Ii
def i11iII1 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( iIIII )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
 for url in i1I :
  o0oOOO0 ( url )
  if 75 - 75: Ii1IIIi1 / Ii / iI11I1II1I1I
def i11iI1111ii1I ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOo0oO0o = 'http://documentarylovers.com/?s=' + ( IIi ) . replace ( ' ' , '+' )
 oo0OO = OoOo0oO0o . lower ( )
 OoOoooOO00OO ( oo0OO )
 if 89 - 89: Ii / o0o00Oo0O - ooOoO0O00 % I1ii11iIi11i + Ii
def ii1I ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if 'films' in url :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , III1iII1I1ii + 'documentary.png' )
def O0oo00o000 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  if 'films' in url :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + o00O0O )
 for url in i1I :
  Iiiiii111i1ii ( 'NEXT' , url , 8049 , III1iII1I1ii + 'Next.png' )
def II1111iiI1II ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'rtd' in url :
   OoOOOO00 ( url )
   if 15 - 15: Ii1IIIi1 * I11i1ii1 + IIiIiII11i . iiiiiiii1 . o000O0o
def OoOOOO00 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iIIII )
 for i1i , file in i1IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1i + file )
  OOOOo0o00OO0000 ( url )
  if 46 - 46: I1111IIi % iiiiiiii1 + iI11I1II1I1I * oOo0O0Ooo
  if 64 - 64: Ii1I * ii1ii11IIIiiI * I1ii11iIi11i % I1111IIi % I11i1ii1
def OoO0000O ( ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( 'http://www.stream2watch.co/live-tv' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , o00O0O , I1111i , I1III11iiii11i1 in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( I1111i + '[COLOR' + II + ']' + I1III11iiii11i1 + '[/COLOR]' ) , Ii1I1Ii , 8086 , o00O0O )
  if 33 - 33: iiiiiiii1 + O0OOOoOoo0 - I1ii11iIi11i / ii1ii11IIIiiI + o000O0o . OOooOOo
def Oo0O ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8087 , o00O0O )
  if 11 - 11: o0o00Oo0O
def o0Oo0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  i1iioO0oOo ( url , I1111i )
  if 43 - 43: o000O0o + OOooOOo . oOo0O0Ooo . Ii
def i1iioO0oOo ( url , name ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  print url
  i1i1iII1 ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 71 - 71: I11i + Ii1IIIi1 . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
def oo000O0o ( ) :
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii , o00O0O , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + Ii1I1Ii , 3002 , 'http://www.solie.org/alibrary/' + o00O0O )
def o00oOi11III1I1IiI ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def ooooooo0oOo0 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 OooO00oO00o = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIIII )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , I1111i in OooO00oO00o :
  Iiiiii111i1ii ( '[COLOR' + II + ']Season- ' + I1111i + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , o00O0O , I1111i in i1I :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def IIII1iI1IiIiI ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1II1 ( url )
def i1II1 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 91 - 91: ii . Ii1IIIi1 - I11i1ii1 + IIiIiII11i + ii1ii11IIIiiI . ii
def iI1I ( ) :
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Ii1I1Ii , 8065 , III1iII1I1ii + 'classicmovies.png' )
def Iii1iiIIi1i111i ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOO00OooO ( url )
  if 48 - 48: I1ii11iIi11i . I11i - O0OOOoOoo0
def IIIII1 ( ) :
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , Ii1I1Ii , 8065 , III1iII1I1ii + 'classictv.png' )
def i1iI1Ii1 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'mp4' in url :
   OOOOo0o00OO0000 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 84 - 84: IIiIiII11i / oO0o . I1111IIi
def o0OO00oO00 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + Ii1I1Ii , 8071 , III1iII1I1ii + 'streams.png' )
def OOo ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1111i , url in i1IIIII11I1IiI :
  if '(Free Access)' in I1111i :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def ooIII ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , o00O0O , o0ooooO0o0O , '' )
  if 40 - 40: iiiiiiii1 % I11i / oOo0O0Ooo
def II1111II ( ) :
 i111I1 = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  oOOOoooO ( 'http://watchxxxfree.com/categories' )
 if iI11iI1IiiIiI == 1 :
  IIIi1IIiII11 ( 'http://www.perfectgirls.net' )
 if iI11iI1IiiIiI == 2 :
  I1IIi ( 'http://www.xvideos.com/best' )
 if iI11iI1IiiIiI == 3 :
  O00O ( 'http://www.xvideos.com/best' )
 if iI11iI1IiiIiI == 4 :
  I1IIi ( 'http://www.xvideos.com/best' )
 if iI11iI1IiiIiI == 5 :
  I1IIi ( 'http://www.xvideos.com/verified/videos' )
 if iI11iI1IiiIiI == 6 :
  IiIIiIiIIiI ( 'http://www.xvideos.com/tags' )
 if iI11iI1IiiIiI == 7 :
  I1ii11I1IiI ( 'http://www.xvideos.com/porn' )
 if iI11iI1IiiIiI == 8 :
  i1IIIii ( )
  if 37 - 37: O0OOOoOoo0 . I11i / ii1ii11IIIiiI / Ii1IIIi1 * ooOoO0O00
  if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + o000O0o
  if 58 - 58: O0OOOoOoo0 - ii
  if 56 - 56: O0OOOoOoo0 / O0OOOoOoo0
  if 21 - 21: o0o00Oo0O * I11i1ii1 % OOooOOo / o0o00Oo0O
  if 85 - 85: ii + ii
  if 23 - 23: ooOoO0O00
  if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / ooOOOoO . oO0o
  if 74 - 74: I1ii11iIi11i - IIiIiII11i - I1111IIi
def IiII1II1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  if 'ch' in url :
   iI1iiiIii1II1 ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Jizbox.png' , III1iII1I1ii + 'Jizbox.png' , '' )
def O0ooOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIi1i1I1I = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 for I1111i , url in iIi1i1I1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Next.png' , '' , '' )
def i11iiiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   o0OOOO0o0o0oo0Oo0 ( url )
def IiIii111iI11i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def oOOOoooO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , oOOOoo0o in i1IIIII11I1IiI :
  if 'category' in url :
   iI1iiiIii1II1 ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   ' + oOOOoo0o + '[/COLOR]' , url , 90006 , o00O0O , III1iII1I1ii + 'Jizbox.png' , '' )
def ooo0ooO00o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIi1i1I1I = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , o00O0O , '' , '' )
 for url in iIi1i1I1I :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , III1iII1I1ii + 'Next.png' , '' , '' )
def o0OOii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   o0OOOO0o0o0oo0Oo0 ( url )
def o0OOOO0o0o0oo0Oo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def IIIi1IIiII11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , oOOOoo0o in i1IIIII11I1IiI :
  if 'category' in url :
   iI1iiiIii1II1 ( '[COLOR' + II + ']' + I1111i + '[COLORorange]' + oOOOoo0o + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def IIiiiiiI1iIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OoO = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIi1i1I1I = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , o00O0O , '' , '' )
 for url in iIi1i1I1I :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , OoO + '/' + url , 90003 , III1iII1I1ii + 'Next.png' , '' , '' )
def IIIII11II1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOO0oOO ( 'http://www.perfectgirls.net' + url )
def OOOO0oOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOoO0ooOO ( 'http://' + url )
def I1ii11I1IiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , oOOOoo0o in i1IIIII11I1IiI :
  iI1iiiIii1II1 ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + oOOOoo0o + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def IiIIiIiIIiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iIi1i1I1I = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in iIi1i1I1I :
  iI1iiiIii1II1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , I1111i , oOOOoo0o in i1IIIII11I1IiI :
  iI1iiiIii1II1 ( ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + ( oOOOoo0o + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iIi1i1I1I = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in iIi1i1I1I :
  iI1iiiIii1II1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , i1ii1iIi in i1IIIII11I1IiI :
  iI1iiiIii1II1 ( I1111i + '--' + ( i1ii1iIi ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( o00O0O ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 89 - 89: o0o00Oo0O + I1111IIi * iiiiiiii1
  if 30 - 30: OOooOOo
def I1IIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , url , I1111i , IIiiiiiIiIIi , IIIII11 in i1IIIII11I1IiI :
  iI1iiiIii1II1 ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + IIIII11 + ' - [COLORred]' + IIiiiiiIiIIi + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , o00O0O , o00O0O , IIIII11 + ' - ' + IIiiiiiIiIIi )
 i1i1IiiIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in i1i1IiiIi :
  iI1iiiIii1II1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 41 - 41: o000O0o + o0o00Oo0O / iI11I1II1I1I - OOooOOo + ii1ii11IIIiiI
def O00O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I1IIIiI1I1ii1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIi1i1I1I = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in iIi1i1I1I :
  iI1iiiIii1II1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
 for url , I1111i in i1IIIII11I1IiI :
  if '/c/' in url :
   iI1iiiIii1II1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
   if 4 - 4: Ii1I % I11i1ii1 . I1ii11iIi11i * oO0o - ooOOOoO
   if 27 - 27: iiiiiiii1
def i1IIIii ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iii1iI = ( IIi ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 oo0OO = iii1iI . lower ( )
 iIII1I1ii = 'http://www.xvideos.com/?k=' + oo0OO
 print iIII1I1ii + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0OOoo0OO = OoOooO ( iIII1I1ii )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , Ii1I1Ii , I1111i , IIiiiiiIiIIi , IIIII11 in i1IIIII11I1IiI :
  iI1iiiIii1II1 ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + IIIII11 + ' - [COLORred]' + IIiiiiiIiIIi + '[/COLOR]' , 'http://www.xvideos.com' + Ii1I1Ii , 10108 , o00O0O , o00O0O , IIIII11 + ' - ' + IIiiiiiIiIIi )
 i1i1IiiIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii in i1i1IiiIi :
  iI1iiiIii1II1 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + Ii1I1Ii , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
if 42 - 42: I11i . iiiiiiii1 / o0o00Oo0O . IIiIiII11i * OOooOOo
if 7 - 7: iiiiiiii1 * o0o00Oo0O + OOooOOo
if 90 - 90: I1111IIi * IIiIiII11i * I1111IIi - O0OOOoOoo0
if 34 - 34: Ii1IIIi1 - Ii1I * O0OOOoOoo0 % ii1ii11IIIiiI
if 25 - 25: IIiIiII11i + oOo0O0Ooo * I11i1ii1 * Ii1I . O0OOOoOoo0
if 26 - 26: O0OOOoOoo0 - I11i1ii1 / ii + I11i . I1ii11iIi11i
if 75 - 75: o0o00Oo0O / OOooOOo . iiiiiiii1
if 7 - 7: oO0o * O0OOOoOoo0
if 16 - 16: iiiiiiii1 . ooOoO0O00 . I1111IIi
if 50 - 50: oO0o - IIiIiII11i * ii - oOo0O0Ooo . o0o00Oo0O + o0o00Oo0O
if 80 - 80: I11i
if 50 - 50: I11i1ii1
if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * Ii1IIIi1
if 83 - 83: Ii - oOo0O0Ooo * Ii
if 59 - 59: O0OOOoOoo0 - ii / I11i1ii1 + Ii1I . I11i - O0OOOoOoo0
if 29 - 29: o000O0o
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
if 61 - 61: I11i1ii1
def Iii1II1iI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 ooOoO00 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   i1i1iII1 ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   i1i1iII1 ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in ooOoO00 :
  if 'http' in url :
   i1i1iII1 ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 95 - 95: iI11I1II1I1I
def o0O0ooo0o ( url ) :
 oO0o000OoOoO0 = xbmc . Player ( OO0ooOOO0O00o ( ) )
 import urlresolver
 try : oO0o000OoOoO0 . play ( url )
 except : pass
 if 55 - 55: I11i1ii1 . I1111IIi * ooOoO0O00 . ii1ii11IIIiiI
 if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + ii1ii11IIIiiI % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def oo000O ( ) :
 if 97 - 97: ii * I11i + ii % ii1ii11IIIiiI * I1ii11iIi11i
 if 35 - 35: iI11I1II1I1I % O0OOOoOoo0 - ooOoO0O00
 if 20 - 20: ooOOOoO % I11i1ii1 . Ii1IIIi1 / iiiiiiii1
 if 50 - 50: o000O0o + Ii / Ii + I11i1ii1 + iiiiiiii1
 if 65 - 65: I11i1ii1 * o0o00Oo0O * O0OOOoOoo0
 if 60 - 60: iI11I1II1I1I . I11i1ii1 + oOo0O0Ooo % o000O0o
 if 4 - 4: oOo0O0Ooo / IIiIiII11i % o0o00Oo0O * I11i1ii1 / IIiIiII11i . I1ii11iIi11i
 if 16 - 16: o0o00Oo0O + o0o00Oo0O - oOo0O0Ooo
 if 30 - 30: I11i1ii1
 if 33 - 33: iiiiiiii1 * I1111IIi - o0o00Oo0O + oOo0O0Ooo / I1111IIi
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 8091 , III1iII1I1ii + 'gofish.png' )
def iii1II11II1 ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
def I11i1Iii1I ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIIiII1 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O in iIIiII1 :
  o00O0O = o00O0O
 for url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
  if 9 - 9: Ii1I - I1111IIi
def o0o0OoOo00oOoo0oO ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 35 - 35: iiiiiiii1 - ooOoO0O00 / I1111IIi
  if 13 - 13: OOooOOo - oO0o * ii
  if 26 - 26: ii
  if 65 - 65: Ii1IIIi1
i111ii1II11ii = '{PQ},' ; i11iII1IiI = '{SC},' ; i1II1IiIi111 = '{XG},' ; oooI1iIiii = '{JP},' ; OoOOo0OO0OOoo = '{HW},' ; i1Ii1 = '{RT},'
def Oo0oooO0oO ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oOoO = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 Ii1I1Ii = 'http://onlinemovies.tube/?s=' + ( IIi ) . replace ( ' ' , '+' )
 OoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 IIII = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 iI1iiiIiii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 ii1i1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 II11iIII1i1I = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOO0oo = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + IIi
 IiIIi1I1I11Ii = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 o0OO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 11 - 11: ooOoO0O00 / iiiiiiii1 * Ii1I * iiiiiiii1 * I11i1ii1 - Ii
 Ooo0O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 ooo0 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 96 - 96: Ii1I % Ii1I
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( Ii1I1Ii )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( OoO )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( IIII )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( iI1iiiIiii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 ooO0o = O0o0O00Oo0o0 ( ii1i1i )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 ii1iI1iI1 = O0o0O00Oo0o0 ( oOO0oo )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 o00oOOO = O0o0O00Oo0o0 ( IiIIi1I1I11Ii )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 OoOO0OOoo = O0o0O00Oo0o0 ( o0OO )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 1 - 1: oOo0O0Ooo . ii1ii11IIIiiI
 if 26 - 26: o000O0o - I11i1ii1 % I1ii11iIi11i - o000O0o + I1111IIi
 o0Oii1111i = O0o0O00Oo0o0 ( Ooo0O0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 O0ooOO = O0o0O00Oo0o0 ( ooo0 )
 if 33 - 33: ii1ii11IIIiiI + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * I1111IIi
 if 21 - 21: o0o00Oo0O * I11i1ii1 % oO0o
 if 14 - 14: o0o00Oo0O / iiiiiiii1 / I11i1ii1 + I1111IIi - I1111IIi
 if 10 - 10: o0o00Oo0O - Ii1I / iiiiiiii1 % OOooOOo / ii / ii1ii11IIIiiI
 if 73 - 73: I11i1ii1 + I1111IIi % I11i . Ii1I / Ii1IIIi1 . iiiiiiii1
 if 76 - 76: ooOOOoO . Ii1I * ii % O0OOOoOoo0
 if 24 - 24: ii
 if 83 - 83: o0o00Oo0O / oO0o
 if 62 - 62: ooOOOoO
 if 73 - 73: ii1ii11IIIiiI % oO0o * Ii1IIIi1
 if 84 - 84: I1ii11iIi11i
 if 18 - 18: ii
 if 85 - 85: ii . oO0o . oO0o
 if OoOO0OOoo != 'Failed' :
  o0OooooOoOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( OoOO0OOoo )
  for Ii1I1Ii , I1111i in o0OooooOoOO :
   i1i1IIIIIIIi = O0o0O00Oo0o0 ( Ii1I1Ii )
   oo0o0oOo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( i1i1IIIIIIIi )
   for OO0oOOo0o , I1III11iiii11i1 in oo0o0oOo :
    I1III11iiii11i1 = ( I1III11iiii11i1 . replace ( '.' , ' ' ) )
    if oo0OO in I1III11iiii11i1 . lower ( ) :
     if '.mkv' in OO0oOOo0o :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , Ii1I1Ii + OO0oOOo0o , 222 , '' , '' , '' )
     elif '.mp4' in OO0oOOo0o :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , Ii1I1Ii + OO0oOOo0o , 222 , '' , '' , '' )
     elif '.avi' in OO0oOOo0o :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , Ii1I1Ii + OO0oOOo0o , 222 , '' , '' , '' )
     elif '.wav' in OO0oOOo0o :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , Ii1I1Ii + OO0oOOo0o , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , Ii1I1Ii + OO0oOOo0o , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 70 - 70: ooOOOoO
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in i1I :
   if IIi in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source Technica[/COLOR]' ) , Ii1I1Ii , 222 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 72 - 72: iiiiiiii1 - I11i1ii1 - oOo0O0Ooo - O0OOOoOoo0 + Ii1IIIi1 - ooOoO0O00
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 45 - 45: oO0o * oOo0O0Ooo
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for o0O0OO , I1111i in ooOoO00 :
   if IIi in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IIII + o0O0OO ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in Iii1I1111ii :
   if IIi in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source RaizTv[/COLOR]' ) , Ii1I1Ii , 222 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 61 - 61: O0OOOoOoo0 % IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if ooO0o != 'Failed' :
  oo0o0 = [ ]
  iiIii1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO0o )
  for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in iiIii1I :
   if IIi in I1111i . lower ( ) :
    if I1111i in oo0o0 :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , Ii1I1Ii , 1016 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
     oo0o0 . append ( I1111i )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if ii1iI1iI1 != 'Failed' :
  oO0ooOoO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( ii1iI1iI1 )
  for Ii1I1Ii , o00O0O , I1111i in oO0ooOoO :
   if IIi in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + Ii1I1Ii , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
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
    if 25 - 25: I1ii11iIi11i + I11i - oO0o
    if 57 - 57: IIiIiII11i . ooOoO0O00
    if 33 - 33: O0OOOoOoo0 + I1ii11iIi11i % ooOOOoO . o000O0o
    if 6 - 6: I1111IIi + Ii1I
    if 62 - 62: o000O0o . iiiiiiii1 - ii * IIiIiII11i . Ii
    if 13 - 13: iI11I1II1I1I * I11i - Ii
    if 63 - 63: ii * iiiiiiii1
    if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . o000O0o % IIiIiII11i
    if 18 - 18: ooOOOoO % ii + oO0o / ooOOOoO
 if o0Oii1111i != 'Failed' :
  ooOOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0Oii1111i )
  for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in ooOOOo :
   if IIi in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source APPRENTICE[/COLOR]' ) , Ii1I1Ii , 222 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 37 - 37: ooOoO0O00 - ii1ii11IIIiiI / I1111IIi . IIiIiII11i % I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 39 - 39: ii1ii11IIIiiI % Ii * oO0o
    if 23 - 23: Ii1IIIi1 + I11i1ii1 / Ii * I1ii11iIi11i . oO0o
    if 28 - 28: O0OOOoOoo0 - I11i
    if 92 - 92: I1ii11iIi11i % I11i - I11i1ii1 / I11i1ii1 / OOooOOo
    if 84 - 84: Ii1IIIi1
    if 4 - 4: I1111IIi . iiiiiiii1 / ii1ii11IIIiiI / O0OOOoOoo0 + IIiIiII11i
    if 32 - 32: ooOoO0O00 + iI11I1II1I1I . Ii1I . ooOOOoO - ii1ii11IIIiiI
    if 55 - 55: Ii1I / ii - oO0o / oOo0O0Ooo
    if 23 - 23: ooOOOoO * iiiiiiii1 * I11i - oOo0O0Ooo % OOooOOo + I11i
    if 41 - 41: I1111IIi * ii . I11i1ii1 % Ii
 oOoOo = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 11 - 11: iI11I1II1I1I . iiiiiiii1 - I1ii11iIi11i / ooOOOoO + IIiIiII11i
 for IiiI11i1I in oOoOo :
  OOo0 = O0Oo000ooO00 + IiiI11i1I + I1IIIii
  OoOO0OOoo = O0o0O00Oo0o0 ( OOo0 )
  if OoOO0OOoo != 'Failed' :
   o0OooooOoOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOO0OOoo )
   for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in o0OooooOoOO :
    if IIi in I1111i . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , Ii1I1Ii , 222 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 29 - 29: ooOOOoO . Ii + ooOoO0O00 - ii1ii11IIIiiI + o0o00Oo0O . oOo0O0Ooo
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 8 - 8: I11i
 oOoOo = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 78 - 78: ooOoO0O00 - I1ii11iIi11i
 if 48 - 48: ii1ii11IIIiiI - ii + iiiiiiii1 % I11i - OOooOOo . oOo0O0Ooo
 for IiiI11i1I in oOoOo :
  OOo0 = oOoO + IiiI11i1I
  IiIi1111ii = O0o0O00Oo0o0 ( OOo0 )
  if IiIi1111ii != 'Failed' :
   iI1I1II1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( IiIi1111ii )
   for o0O0OO , I1111i in iI1I1II1 :
    if IIi in I1111i . lower ( ) :
     i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oOoO + IiiI11i1I + o0O0OO ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 42 - 42: iiiiiiii1
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 70 - 70: I11i / ooOOOoO + o000O0o % oOo0O0Ooo % I1ii11iIi11i + oO0o
def I1ii1 ( ) :
 if 80 - 80: Ii1IIIi1
 if 12 - 12: ii1ii11IIIiiI
 if 2 - 2: ii
 if 100 - 100: I1ii11iIi11i / o0o00Oo0O * Ii * ii
 if 46 - 46: o0o00Oo0O % ii
 if 22 - 22: O0OOOoOoo0 + ii - OOooOOo - oO0o * iiiiiiii1 - o000O0o
 if 99 - 99: I11i1ii1 / oOo0O0Ooo . ii1ii11IIIiiI - ii1ii11IIIiiI * oOo0O0Ooo
 if 24 - 24: ooOOOoO * oO0o - o000O0o / iI11I1II1I1I - I1ii11iIi11i . Ii1IIIi1
 if 2 - 2: I11i1ii1 - o0o00Oo0O - Ii1I / ooOOOoO * OOooOOo
 if 26 - 26: Ii1I + iiiiiiii1 - o000O0o + I1111IIi % Ii1IIIi1
 if 84 - 84: ooOOOoO % ii1ii11IIIiiI % o0o00Oo0O * I11i
 if 15 - 15: o000O0o - iI11I1II1I1I - IIiIiII11i - I1111IIi % Ii1I
 if 80 - 80: I1111IIi * O0OOOoOoo0 . ooOoO0O00 % ii1ii11IIIiiI % Ii1I + I11i1ii1
 if 6 - 6: Ii1I . o000O0o . oO0o + I1111IIi
 if 65 - 65: Ii1I / I11i1ii1
 if 23 - 23: Ii1IIIi1 / Ii1IIIi1 * I11i * Ii1IIIi1
 if 57 - 57: O0OOOoOoo0
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 if 29 - 29: oOo0O0Ooo
 if 41 - 41: iiiiiiii1 * oO0o - O0OOOoOoo0 . ii1ii11IIIiiI
 OO0oOOo0o = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( IIi ) . replace ( ' ' , '+' )
 OoO = 'http://onlinemovies.tube/?s=' + ( IIi ) . replace ( ' ' , '+' )
 IIII = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 iI1iiiIiii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 II11iIII1i1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - o000O0o + iiiiiiii1
 IiIIi1I1I11Ii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 o0OO = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 O0oOo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 22 - 22: o0o00Oo0O % I1111IIi % O0OOOoOoo0 % oOo0O0Ooo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 34 - 34: O0OOOoOoo0 . I1ii11iIi11i % Ii1I . O0OOOoOoo0 % I1111IIi / I1111IIi
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 84 - 84: ii1ii11IIIiiI
 if 1 - 1: o000O0o - I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
 Oo0O0Oo00O = O0o0O00Oo0o0 ( OO0oOOo0o )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( OoO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( IIII )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( iI1iiiIiii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 IiIi1111ii = O0o0O00Oo0o0 ( II11iIII1i1I )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 9 - 9: O0OOOoOoo0 - O0OOOoOoo0
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + o000O0o
 o00oOOO = O0o0O00Oo0o0 ( IiIIi1I1I11Ii )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 OoOO0OOoo = O0o0O00Oo0o0 ( o0OO )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 ii1ii = O0o0O00Oo0o0 ( O0oOo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 20 - 20: oO0o + ooOOOoO . IIiIiII11i / Ii
 if OoOO0OOoo != 'Failed' :
  o0OooooOoOO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( OoOO0OOoo )
  for Ii1I1Ii , I1111i in o0OooooOoOO :
   i1i1IIIIIIIi = O0o0O00Oo0o0 ( Ii1I1Ii )
   oo0o0oOo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( i1i1IIIIIIIi )
   for OO0oOOo0o , I1III11iiii11i1 in oo0o0oOo :
    if oo0OO in I1III11iiii11i1 . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + I1III11iiii11i1 + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , Ii1I1Ii + OO0oOOo0o , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 50 - 50: ii / oO0o % iI11I1II1I1I
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if o00oOOO != 'Failed' :
  O000O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00oOOO )
  for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in O000O :
   if oo0OO in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source HeroVision[/COLOR]' ) , Ii1I1Ii , 1016 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 41 - 41: Ii1I % Ii1I + I1111IIi . O0OOOoOoo0 % iiiiiiii1 * I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 57 - 57: ii1ii11IIIiiI . iiiiiiii1 . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
    if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
    if 93 - 93: I11i1ii1 / Ii1IIIi1 * o0o00Oo0O
    if 17 - 17: oO0o / I11i1ii1 % oOo0O0Ooo
    if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
    if 60 - 60: Ii1I / I1111IIi . Ii / oO0o % IIiIiII11i
    if 6 - 6: O0OOOoOoo0 % I11i + iiiiiiii1
    if 91 - 91: I11i + o0o00Oo0O * o000O0o * I1111IIi * Ii1I
    if 83 - 83: ii
    if 52 - 52: I11i / OOooOOo % o000O0o % oO0o / I1111IIi % I11i
    if 88 - 88: Ii1IIIi1 / Ii / ii1ii11IIIiiI / Ii * Ii1I % ooOOOoO
 if ii1ii != 'Failed' :
  o0o0OoOOOOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ii1ii )
  for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in o0o0OoOOOOOo :
   if oo0OO in I1111i . lower ( ) :
    Iiiiii111i1ii ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] RaizTv[/COLOR]' , Ii1I1Ii , 1016 , IiI111ii1ii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 43 - 43: OOooOOo * oO0o % ooOoO0O00 * ii1ii11IIIiiI + iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  II1IIi = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for Ii1I1Ii , o00O0O , I1111i , OOoOO0o in i1I :
   if oo0OO in I1111i . lower ( ) :
    if 'season' in OOoOO0o :
     Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , Ii1I1Ii , 90054 , o00O0O , o00O0O , '' )
    if 'episodes' in OOoOO0o :
     Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , Ii1I1Ii , 90044 , o00O0O , o00O0O , '' )
  for Ii1I1Ii in II1IIi :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , Ii1I1Ii , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 80 - 80: I11i . O0OOOoOoo0 . ii
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if Oo0O0Oo00O != 'Failed' :
  OOoOOo0O00O = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( Oo0O0Oo00O )
  for Ii1I1Ii , I1111i , o00O0O in OOoOOo0O00O :
   if oo0OO in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , Ii1I1Ii , 8022 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 63 - 63: I11i1ii1 . Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 66 - 66: oOo0O0Ooo
    if 99 - 99: oO0o % o0o00Oo0O . iiiiiiii1 - Ii1I . I1ii11iIi11i / OOooOOo
    if 60 - 60: Ii1I
    if 78 - 78: o000O0o + IIiIiII11i
    if 55 - 55: ii
    if 90 - 90: oOo0O0Ooo
    if 4 - 4: Ii1IIIi1 % I11i1ii1 - Ii1IIIi1 - I11i
    if 30 - 30: I1111IIi
    if 34 - 34: o000O0o - IIiIiII11i - I11i + O0OOOoOoo0 + iiiiiiii1
 if ii1ii1ii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for I1111i in ooOoO00 :
   if oo0OO in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( IIII + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 70 - 70: ii + oO0o * I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for I1111i in Iii1I1111ii :
   if oo0OO in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( iI1iiiIiii + I1111i ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 20 - 20: Ii - IIiIiII11i - I11i1ii1 % o000O0o . I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if IiIi1111ii != 'Failed' :
  iI1I1II1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( IiIi1111ii )
  for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in iI1I1II1 :
   if oo0OO in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] Source Scooby[/COLOR]' ) , Ii1I1Ii , 1016 , IiI111ii1ii , oOoo000 , oo00O00oO000o )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 50 - 50: iI11I1II1I1I + iiiiiiii1 - ooOOOoO - ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 84 - 84: OOooOOo - ooOOOoO
 o0oo00o0O0O00 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for IiiI11i1I in o0oo00o0O0O00 :
  OOo0 = O0Oo000ooO00 + IiiI11i1I + I1IIIii
  o0Oii1111i = O0o0O00Oo0o0 ( OOo0 )
  if o0Oii1111i != 'Failed' :
   ooOOOo = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o0Oii1111i )
   for I1111i , oo00O00oO000o , Ii1I1Ii , o00O0O , o0ooooO0o0O , O0OOO0OOooo00 in ooOOOo :
    if oo0OO in I1111i . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , Ii1I1Ii , O0OOO0OOooo00 , o00O0O , o0ooooO0o0O , oo00O00oO000o )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 80 - 80: Ii % Ii1IIIi1 - I1ii11iIi11i % Ii1IIIi1
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 89 - 89: ii1ii11IIIiiI * ooOOOoO + OOooOOo / Ii
     if 68 - 68: ii * ooOOOoO
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOO ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Ii1I1Ii = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( IIi ) . replace ( ' ' , '+' )
 if 15 - 15: ii - I11i1ii1 / ooOOOoO % ii1ii11IIIiiI * O0OOOoOoo0
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 oO0OOoo0OO = O0o0O00Oo0o0 ( Ii1I1Ii )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 23 - 23: iiiiiiii1 - iI11I1II1I1I - IIiIiII11i + iiiiiiii1 % ii1ii11IIIiiI / ooOOOoO
 if oO0OOoo0OO != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for Ii1I1Ii , I1111i in i1I :
   if IIi in I1111i . lower ( ) :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + Ii1I1Ii ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 94 - 94: I1ii11iIi11i * I11i1ii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
I1IIo0o0OoOO00Oo = '{ZH},' ; i1iiIi1II1 = '{IX},' ; iiI1Iii = '{LM},'
if 84 - 84: oOo0O0Ooo / OOooOOo
def i1IO0OoO0o ( url ) :
 o0Oo00oOOO0o = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( o0Oo00oOOO0o )
 for url , IiIi1ii111i1 , ii1O0ooooo000 , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( IiIi1ii111i1 ) . replace ( 'Sezon' , ' Season ' ) + ( ii1O0ooooo000 ) . replace ( 'Bölüm' , ' Episode ' ) + I1111i , url , 8063 , '' )
  if 60 - 60: ooOOOoO . OOooOOo . IIiIiII11i
  if 13 - 13: I1111IIi - ii + oOo0O0Ooo . O0OOOoOoo0 % o0o00Oo0O + oOo0O0Ooo
  if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
  if 34 - 34: I11i % Ii1I + ii1ii11IIIiiI * ooOOOoO / o000O0o
def i111Iii11i1Ii ( url ) :
 o0Oo00oOOO0o = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( o0Oo00oOOO0o )
 for url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( I1111i , url , 222 , '' )
  if 65 - 65: iI11I1II1I1I * I1111IIi
  if 89 - 89: I1111IIi % Ii . Ii + o000O0o / Ii1I
  if 19 - 19: oOo0O0Ooo
  if 86 - 86: Ii1I + OOooOOo * I1111IIi + I11i1ii1
def iI1IiiII1 ( ) :
 if 17 - 17: I11i1ii1 / O0OOOoOoo0 - ii
 o0Oo00oOOO0o = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( o0Oo00oOOO0o )
 for Ii1I1Ii , o00O0O , I1111i , ii1O0ooooo000 in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i + '  -  ' + ( ii1O0ooooo000 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , Ii1I1Ii , 8063 , o00O0O )
  if 55 - 55: ii % ooOoO0O00 . O0OOOoOoo0 . oOo0O0Ooo . o0o00Oo0O
def iii ( ) :
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii , I1111i , o00O0O in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 8002 , o00O0O )
def IiiIIiI ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , time , url , I1111i , O0ooo0ooOoo0o in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '%s %s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , time ) , url , 1015 , o00O0O , O0ooo0ooOoo0o )
  if 79 - 79: oOo0O0Ooo + I1ii11iIi11i % OOooOOo - I1111IIi + oOo0O0Ooo * o000O0o
def OO0O0OOoOo ( ) :
 if 47 - 47: Ii1IIIi1
 Iiiiii111i1ii ( 'Coronation Street' , '' , 8001 , '' )
 Iiiiii111i1ii ( 'Eastenders' , '' , 8002 , '' )
 Iiiiii111i1ii ( 'Emmerdale' , '' , 8003 , '' )
 Iiiiii111i1ii ( 'Hollyoaks' , '' , 8004 , '' )
 Iiiiii111i1ii ( 'Im a Celebrity' , '' , 8005 , '' )
 if 20 - 20: iiiiiiii1 % I11i1ii1 - iiiiiiii1 * ii / Ii1I
 if 57 - 57: I1111IIi % ooOOOoO * Ii1IIIi1 % Ii1I
 if 65 - 65: ooOoO0O00 - ii
 if 66 - 66: Ii1I / ooOoO0O00 * oOo0O0Ooo - OOooOOo + o000O0o
def O0o0 ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'Holly' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in Ii1I1Ii :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1I1Ii . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 58 - 58: O0OOOoOoo0 / ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 62 - 62: oO0o / I1111IIi % ii + o0o00Oo0O / o0o00Oo0O
def IIIiI1iOoo00o0O00Oo ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'East' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in Ii1I1Ii :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1I1Ii . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 89 - 89: o000O0o - iiiiiiii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: Ii1I - ooOoO0O00 + ooOOOoO % I1ii11iIi11i
def oOo0000oo ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'Emmer' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in Ii1I1Ii :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1I1Ii . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 31 - 31: O0OOOoOoo0 - Ii1I * o0o00Oo0O . ii * ooOOOoO / I1111IIi
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 87 - 87: iI11I1II1I1I
def OOOooOO0oO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'Coro' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in Ii1I1Ii :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1I1Ii . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 20 - 20: oO0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: o0o00Oo0O - I11i1ii1
def iiiIIIIiI1iiI ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'Celeb' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in Ii1I1Ii :
    i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , Ii1I1Ii . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 13 - 13: ooOOOoO . oO0o
def O00oO0oOOOOOO ( name , url ) :
 Oo0ooo00OoO = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if Oo0ooo00OoO :
  Iiii1I1I111i1 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIIII = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( iIIII ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIIII = open_url ( url )
  O0Oo = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( iIIII ) [ - 1 ]
  Iiii1I1I111i1 = O0Oo . replace ( '\\/' , '/' )
 oOO = xbmcgui . ListItem ( name , '' , '' )
 oOO . setPath ( Iiii1I1I111i1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOO )
 if 70 - 70: o0o00Oo0O . iI11I1II1I1I * IIiIiII11i
 if 43 - 43: I1ii11iIi11i / iiiiiiii1 / ooOoO0O00
def I1i11IIiiIiI ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , Ii1I1Ii , 7071 , III1iII1I1ii + 'popcorn.png' )
 for Ii1I1Ii , I1111i in i1I :
  Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , Ii1I1Ii , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 7 - 7: oO0o * Ii * iI11I1II1I1I / Ii1IIIi1 / iiiiiiii1
def i11Ii1iiiI1I ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'Movies' in I1111i :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( Ii1I1Ii ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def II1iiI11I ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 for url in i1I :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 43 - 43: OOooOOo / iI11I1II1I1I
  if 84 - 84: iI11I1II1I1I + Ii1I
def Iii1iiIi1II ( url ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in i1IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , o00O0O )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
Ooo00OoO = '{UJ},' ; oOOOOoo000Ooo = '{WE},' ; iiii1II = '{WP},' ; ii1iIiIIIII = '{PP},'
def iiiOO00 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in i1IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1iII1o0 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  iiI11 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiI11 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 6 - 6: iI11I1II1I1I - Ii / Ii1I - I11i
 if 95 - 95: ooOOOoO
 if 76 - 76: IIiIiII11i - ooOoO0O00 . o0o00Oo0O * Ii % I11i - O0OOOoOoo0
def I1II1IIiI11 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '(cooltvseries.com)' in I1111i :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , I1111i in i1I :
  if '(cooltvseries.com)' in I1111i :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def IIIii ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOoO0ooOO ( ( url ) . replace ( ' ' , '%20' ) )
iiiiii1 = '{XX},' ; OO00Oo00o = '{UD},' ; IiII1Iiii = '{YT},' ; I1o000o00OO00Oo = '{JS},' ; I1II11I11111i = '{PF},'
if 14 - 14: I1111IIi + I11i + Ii1I * I11i + oO0o
def iiiIIi11IiI ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii , I1111i , o00O0O in i1IIIII11I1IiI :
  i1i1iII1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( Ii1I1Ii ) ) , 222 , o00O0O )
  if 10 - 10: ii . Ii1IIIi1 * ii1ii11IIIiiI - Ii1I
def OOO000OOo0o0O ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  if 'youtu' in url :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + o00O0O )
 for url in next :
  Iiiiii111i1ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 43 - 43: ooOOOoO . iiiiiiii1 + O0OOOoOoo0 % o0o00Oo0O - I1ii11iIi11i . ooOOOoO
def IIIi1Iii11I ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 34 - 34: iiiiiiii1 . I1111IIi - Ii1IIIi1
def o000oOOoo ( url ) :
 iIIII = OoOooO
 i1IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , o00O0O )
  if 62 - 62: OOooOOo
  if 32 - 32: Ii
  if 57 - 57: iI11I1II1I1I
  if 99 - 99: O0OOOoOoo0 % I11i + iI11I1II1I1I
  if 51 - 51: ooOoO0O00 % I11i - o000O0o - I1111IIi
def i11IIII ( ) :
 if 7 - 7: O0OOOoOoo0 / Ii1I
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
 if 76 - 76: ii1ii11IIIiiI + O0OOOoOoo0 - I1111IIi * iI11I1II1I1I % ooOoO0O00
 if 72 - 72: I11i1ii1 + IIiIiII11i . o0o00Oo0O - O0OOOoOoo0 / ii . iiiiiiii1
def iiiiiiI ( Cat_Name ) :
 if 41 - 41: ii1ii11IIIiiI
 I1iiI1II11 = False
 ooooO000 = '0'
 if Cat_Name == 'All Channels' : I1iiI1II11 = True
 if Cat_Name == 'Entertainment' : ooooO000 = '1'
 if Cat_Name == 'Movies' : ooooO000 = '2'
 if Cat_Name == 'Music' : ooooO000 = '3'
 if Cat_Name == 'News' : ooooO000 = '4'
 if Cat_Name == 'Sports' : ooooO000 = '5'
 if Cat_Name == 'Documentary' : ooooO000 = '6'
 if Cat_Name == 'Kids' : ooooO000 = '7'
 if Cat_Name == 'Food' : ooooO000 = '8'
 if Cat_Name == 'Religious' : ooooO000 = '9'
 if Cat_Name == 'USA Channels' : ooooO000 = '10'
 if Cat_Name == 'Other' : ooooO000 = '11'
 if 63 - 63: iiiiiiii1 - o000O0o - O0OOOoOoo0 - I11i1ii1 / o000O0o + oO0o
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIII )
 print 'Len Match: >>>' + str ( len ( i1IIIII11I1IiI ) )
 for I1111i , o00O0O , o0oOo in i1IIIII11I1IiI :
  II1oOO0O0Ooo0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  if o0oOo == ooooO000 :
   Iiiiii111i1ii ( I1111i , '' , 7022 , II1oOO0O0Ooo0 )
  elif I1iiI1II11 == True :
   Iiiiii111i1ii ( I1111i , '' , 7022 , II1oOO0O0Ooo0 )
  else : pass
  if 7 - 7: ii1ii11IIIiiI - ooOoO0O00 % oO0o / iI11I1II1I1I % I11i
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 26 - 26: OOooOOo . Ii1I . Ii1IIIi1
def iIiiII11 ( Search_Name ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , Ii1I1Ii , OoO , IIII in i1IIIII11I1IiI :
  II1oOO0O0Ooo0 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  i1i1iII1 ( Search_Name + ': Link 1' , ( Ii1I1Ii ) . replace ( '\\' , '' ) , 222 , II1oOO0O0Ooo0 )
  i1i1iII1 ( Search_Name + ': Link 2' , ( OoO ) . replace ( '\\' , '' ) , 222 , II1oOO0O0Ooo0 )
  i1i1iII1 ( Search_Name + ': Link 3' , ( IIII ) . replace ( '\\' , '' ) , 222 , II1oOO0O0Ooo0 )
  if 75 - 75: OOooOOo + ii1ii11IIIiiI . Ii / ii1ii11IIIiiI
def i1I1I1 ( ) :
 iIIII = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , Ii1I1Ii in i1IIIII11I1IiI :
  i1i1iII1 ( I1111i , ( Ii1I1Ii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def i11iI1111i ( ) :
 iIIII = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , Ii1I1Ii in i1IIIII11I1IiI :
  i1i1iII1 ( I1111i , ( Ii1I1Ii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def IIIi11 ( ) :
 iIIII = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , Ii1I1Ii in i1IIIII11I1IiI :
  i1i1iII1 ( I1111i , ( Ii1I1Ii ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 17 - 17: IIiIiII11i / I11i1ii1
def o0OO0OOoo0oO ( url ) :
 url
 i11I = xbmcgui . ListItem ( I1111i , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11I )
 return
 if 98 - 98: I11i * I1ii11iIi11i - ii1ii11IIIiiI . I11i1ii1
 if 2 - 2: I1ii11iIi11i - I11i1ii1 % iI11I1II1I1I
def o0O0o0O0O ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIIII )
 for url , oo00O00oO000o , o00O0O , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + o00O0O , '' , ( oo00O00oO000o ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  Iiiiii111i1ii ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 27 - 27: O0OOOoOoo0
def IiIi1IiIII1iI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , oo00O00oO000o , o00O0O in i1IIIII11I1IiI :
  OOiIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + o00O0O , '' , oo00O00oO000o )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 I1I1IIiiI1 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoOooOOO00o0OoOOOo in I1I1IIiiI1 :
  o000O0O = ( OoOooOOO00o0OoOOOo ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiOOooooO0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + o00O0O , '' , o000O0O )
  if 20 - 20: iiiiiiii1 . ooOOOoO . ii1ii11IIIiiI + ooOOOoO - Ii1IIIi1 * o000O0o
def o00ooO0 ( INFO ) :
 OO0O000 ( 'info for workout' , INFO )
 if 49 - 49: I1111IIi
 if 56 - 56: o0o00Oo0O / ooOOOoO + Ii1IIIi1
 if 7 - 7: I1ii11iIi11i - Ii / o000O0o / o000O0o . ooOoO0O00 % ooOOOoO
def oo00o0000 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( ( I1111i ) . replace ( 'SlyNet' , '' ) , url , 9031 , III1iII1I1ii + 'Sport.png' )
def OOo00O ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , url , 9032 , III1iII1I1ii + 'icon.png' )
def i1iI1iIIiIi1I ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   i1i1iII1 ( ( I1111i ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , III1iII1I1ii + 'icon.png' )
def I11iIiIII11 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   i1i1iII1 ( I1111i , url , 222 , III1iII1I1ii + 'icon.png' )
   if 81 - 81: Ii1I + ii - Ii1IIIi1 * o0o00Oo0O
   if 100 - 100: iI11I1II1I1I - OOooOOo
   if 28 - 28: I1ii11iIi11i . o0o00Oo0O . ooOOOoO
def Ooo00O ( url ) :
 i1i1iII1 ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 i1i1iII1 ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 Iiiiii111i1ii ( '[COLOR' + II + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , III1iII1I1ii + 'bamf.png' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   pass
  else :
   i1i1iII1 ( ( I1111i ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOo0OO00O0O ( url ) :
 i1i1iII1 ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 i1i1iII1 ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 Iiiiii111i1ii ( '[COLOR' + II + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , III1iII1I1ii + 'bamf.png' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   i1i1iII1 ( ( I1111i ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 52 - 52: Ii1I
 if 93 - 93: O0OOOoOoo0 . Ii
 if 24 - 24: Ii1IIIi1 . oO0o + iiiiiiii1 . o000O0o - Ii1I % O0OOOoOoo0
def iiii1iI1IIiIi ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 i1IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'Daily' in I1111i :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 9008 , Oo00OOOOO )
def i1Iii1I11ii ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def oOoO000OOoo0 ( url ) :
 i1i1iII1 ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 i1i1iII1 ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 i1i1iII1 ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  i1i1iII1 ( ( I1111i ) . replace ( '_' , ' ' ) , url , 222 , Oo00OOOOO )
  if 44 - 44: oO0o % Ii . iiiiiiii1 - o0o00Oo0O / O0OOOoOoo0 . I11i1ii1
def iIiI1I1IIi1 ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if '.m3u' in Ii1I1Ii :
   Iiiiii111i1ii ( ( I1111i ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + Ii1I1Ii ) , 9011 , III1iII1I1ii + 'disclose.png' )
def oooOOOoO ( url ) :
 iIIII = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  i1i1iII1 ( ( I1111i ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 79 - 79: Ii1I - o000O0o - I11i . Ii1IIIi1
def iiI11i1II ( ) :
 iIIII = OoOooO ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  if 'category' in Ii1I1Ii :
   Iiiiii111i1ii ( I1111i , 'http://www.disclose.tv/' + Ii1I1Ii , 7010 , III1iII1I1ii + 'disclose.png' )
   if 65 - 65: Ii . oO0o % O0OOOoOoo0 + I1111IIi - Ii
   if 60 - 60: iiiiiiii1
def II1II1ii1Ii ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIII )
 for url , I1111i , o00O0O in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , 'http://www.disclose.tv/' + url , 7011 , o00O0O )
 for url in next :
  Iiiiii111i1ii ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * ooOOOoO + Ii1IIIi1
  if 14 - 14: ii1ii11IIIiiI - o0o00Oo0O
def OoOO0Ooo ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   i1i1iII1 ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , I1111i in i1I :
  i1i1iII1 ( I1111i , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in ooOoO00 :
  i1i1iII1 ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 95 - 95: oO0o - I1111IIi % iiiiiiii1
  if 27 - 27: iI11I1II1I1I / oOo0O0Ooo % OOooOOo / oOo0O0Ooo * ii1ii11IIIiiI
def I1I ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 84 - 84: ooOOOoO . I1ii11iIi11i . I1111IIi * I11i1ii1 + OOooOOo
def iIiiIi11iiI1 ( name , url , img ) :
 oO0OOoo0OO = OoOooO ( url )
 o0ooOO000O = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iI11iI = len ( o0ooOO000O )
 if 98 - 98: I1111IIi * O0OOOoOoo0 . ii . o0o00Oo0O
 if 89 - 89: O0OOOoOoo0 / o0o00Oo0O % ii - o0o00Oo0O . oO0o
 if iI11iI == 1 :
  for ii11iI1Iii1iI in o0ooOO000O :
   ii11iI1Iii1iI = ii11iI1Iii1iI . replace ( 'player' , 'watch' )
   I1Iii11I = ii11iI1Iii1iI + '&fv=&sou='
   OOoO00o00oo = OoOooO ( I1Iii11I )
   iIiiIi11 = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( OOoO00o00oo )
   for I1iooo in iIiiIi11 :
    o0o0oOOo = False
    Resolve ( I1iooo )
    if 55 - 55: oO0o
 elif iI11iI > 1 :
  if 20 - 20: I11i1ii1 * iiiiiiii1 * I11i - I11i1ii1
  for ii11iI1Iii1iI in o0ooOO000O :
   i1I1IiiIIIiiI = OoOooO ( ii11iI1Iii1iI )
   oOoo0O = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( i1I1IiiIIIiiI )
   ooO00OO0ooo = oOoo0O
   ooO00OO0ooo = ( str ( ooO00OO0ooo ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + ooO00OO0ooo
   i1i1iII1 ( 'DOUBLE LINK' , ooO00OO0ooo , 424 , '' )
   if 78 - 78: I11i1ii1 . oOo0O0Ooo . iiiiiiii1 / o0o00Oo0O % ii % Ii
   for url in oOoo0O :
    Iiiiii111i1ii ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     OoO = Google . resolve ( url )
    except :
     pass
    try :
     o000ii = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( OoO ) )
     for i1I1i , i1iii1i11I1 in o000ii :
      if 26 - 26: Ii - I11i1ii1 / ii1ii11IIIiiI + ooOOOoO
      HD_URLS . append ( i1I1i )
      SD_URLS . append ( i1iii1i11I1 )
    except :
     pass
 else :
  pass
  if 85 - 85: iiiiiiii1 - Ii1I % I1ii11iIi11i
def iiiI1I11i1I ( ) :
 if 1 - 1: I1111IIi * I11i + Ii1IIIi1
 if 77 - 77: I11i
 Iiiiii111i1ii ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 63 - 63: I11i1ii1 * o000O0o + I11i1ii1 * ii1ii11IIIiiI + I1ii11iIi11i / Ii1I
 Iiiiii111i1ii ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
 if 65 - 65: iiiiiiii1 + o0o00Oo0O % I11i
def o0i111I ( ) :
 iIIII = OoOooO ( 'http://cnfstudio.com/' )
 i1IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , 'http://cnfstudio.com/genre/' + Ii1I1Ii , 7003 , III1iII1I1ii + 'icon.png' )
  if 58 - 58: I11i1ii1 - I1ii11iIi11i
OOooO0OOoo = xbmcgui . Dialog ( )
if 23 - 23: OOooOOo
IiiOo = '{UN},' ; iiiIiii11i1i = '{IG},' ; ooo0O0Oo0O = '{PL},' ; Oo0oi1i = '{LO},' ; OO00O0O00oOOO = '{LP},' ; ii1111iIIiIIi = '{HA},' ; ooOo0Oo = '{XD},' ; I11i1I111II1IiI = '{TA},' ; oo00O0oOo = '{DP},' ; IiI1Ii = '{JT},' ; oOO00o0oooOo0 = '{JJ},' ; iIII1iIi = '{MM},' ; iiii1Ii = '{FQ},' ; IIiiiI = '{HH},'
if 2 - 2: ooOoO0O00
def Iii1I1i1i1 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIIII )
 IiIi11I = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIIII )
 for o00O0O , url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , o00O0O )
 IiIi11I = IiIi11I
 for url in IiIi11I :
  Iiiiii111i1ii ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 80 - 80: OOooOOo % I1ii11iIi11i
def oooooOO0 ( url ) :
 if 69 - 69: I1ii11iIi11i + I1111IIi - ooOOOoO . iI11I1II1I1I - ii1ii11IIIiiI
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1i = url + '&fv=&sou='
  i1i = i1i . replace ( 'player' , 'watch' )
  I1iIiI1iiI = oO000O00 ( i1i )
  IiIIIii1iIII1 = oO000O00 ( url )
  if 69 - 69: ooOoO0O00 / Ii + I1ii11iIi11i - OOooOOo
  if 13 - 13: I1111IIi . iI11I1II1I1I
def oO000O00 ( url ) :
 if 30 - 30: ooOoO0O00
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  OOOO00OooO ( url )
  if 42 - 42: O0OOOoOoo0
  if 35 - 35: IIiIiII11i % Ii1IIIi1 . o000O0o * I11i1ii1
def o0O00ooo0oO0o ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , III1iII1I1ii + 'LocalM3U.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , III1iII1I1ii + 'RemoteM3U.png' , O0o0Oo , '' )
 if 21 - 21: iI11I1II1I1I / I11i1ii1 * iiiiiiii1
def ooOooo ( ) :
 if os . path . exists ( iiI1IiI ) :
  Oo00 = open ( iiI1IiI , 'r' )
  for i11I in Oo00 :
   o0OO00oOO00 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( i11I )
   for I1111i , Ii1I1Ii in o0OO00oOO00 :
    i1i1iII1 ( I1111i , Ii1I1Ii , 222 , III1iII1I1ii + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 27 - 27: o000O0o * I1ii11iIi11i * I1ii11iIi11i / I1111IIi + I1ii11iIi11i
def O0ooooOO ( url ) :
 if os . path . exists ( Remote ) :
  oO0OOoo0OO = o0O0O0ooo0oOO ( url )
  i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for I1111i , url in i1IIIII11I1IiI :
   url = ( url ) . strip ( )
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 54 - 54: iiiiiiii1 - iiiiiiii1 * o0o00Oo0O / ii1ii11IIIiiI + oOo0O0Ooo - iiiiiiii1
  if 58 - 58: ii * ooOoO0O00 * OOooOOo
def Iiii1i1 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii in i1IIIII11I1IiI :
  Ii1I1Ii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + Ii1I1Ii
 I1111i = 'plugin.video.GenieTv'
 if 99 - 99: I1ii11iIi11i
 OO0o0 ( Ii1I1Ii , I1111i )
 if 96 - 96: ooOoO0O00 - iiiiiiii1 * oOo0O0Ooo % oOo0O0Ooo
def i1IiiiI1iI ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii in i1IIIII11I1IiI :
  Ii1I1Ii = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + Ii1I1Ii
 I1111i = 'repository.GenieTv'
 if 31 - 31: Ii1I . ii1ii11IIIiiI / I11i1ii1 / Ii % I11i
 OO0o0 ( Ii1I1Ii , I1111i )
 if 69 - 69: iiiiiiii1
 if 83 - 83: iI11I1II1I1I . I11i + iiiiiiii1 . ii / I11i1ii1 + IIiIiII11i
def OOI1iI1ii1II ( ) :
 i111I1 = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  o0o0O0oOOoO0 ( )
 if iI11iI1IiiIiI == 1 :
  I11iIIIIiiI ( )
  if 12 - 12: Ii - ooOOOoO % O0OOOoOoo0 % o0o00Oo0O * I1ii11iIi11i * o000O0o
  if 66 - 66: Ii
  if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / iiiiiiii1 - Ii . I11i1ii1 / Ii1IIIi1
  if 13 - 13: I11i % o0o00Oo0O - iiiiiiii1 * ii / I1ii11iIi11i - ii
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
oOo000O00O = 'https://addons.tvaddons.ag/'
if 90 - 90: ooOoO0O00 / o000O0o / oO0o % Ii1IIIi1
def I11iIIIIiiI ( ) :
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 iIII1I1ii = 'https://addons.tvaddons.ag/search/?keyword=' + oo0OO
 oO0OOoo0OO = OoOooO ( iIII1I1ii )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , I111iIi1 , I1111i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , Ii1I1Ii , 10054 , 'https://addons.tvaddons.ag/' + I111iIi1 , O0o0Oo , '' )
  if 20 - 20: Ii - OOooOOo + I1111IIi % O0OOOoOoo0
  if 79 - 79: oO0o / I11i
def o0o0O0oOOoO0 ( ) :
 oO0OOoo0OO = OoOooO ( oOo000O00O )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for Ii1I1Ii , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'Repositories' in I1111i :
   pass
  elif 'Services' in I1111i :
   pass
  elif 'International' in I1111i :
   pass
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , Ii1I1Ii , 10053 , 'https://addons.tvaddons.ag/' + o00O0O , O0o0Oo , '' )
   if 98 - 98: Ii . Ii * ii
   if 61 - 61: I11i . I1111IIi . o0o00Oo0O + ii + o0o00Oo0O
def Addon ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 Oo00Ooo0O0O0o = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  if 'Please' in I1111i :
   pass
  else :
   OOiIiIIi1 ( I1111i , url , 10054 , 'https://addons.tvaddons.ag/' + o00O0O , O0o0Oo , '' )
 for url in Oo00Ooo0O0O0o :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
  if 86 - 86: oOo0O0Ooo + iI11I1II1I1I % I11i1ii1 / Ii1IIIi1 / ii
  if 96 - 96: o000O0o - IIiIiII11i % oOo0O0Ooo * I1111IIi * ooOOOoO - Ii1IIIi1
def O0OO ( url , name ) :
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
   if 83 - 83: ooOoO0O00 * iiiiiiii1 - I1111IIi / ii1ii11IIIiiI
def OO0o0 ( url , name ) :
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
 if 48 - 48: o000O0o . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 32 - 32: ii1ii11IIIiiI * oOo0O0Ooo - Ii1IIIi1 . I1ii11iIi11i / o0o00Oo0O + ii1ii11IIIiiI
 if 67 - 67: OOooOOo % I1ii11iIi11i
def IiiI11III1i ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , I111iIi1 , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , url , 1007 , I111iIi1 )
def OOo0o0 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , I111iIi1 , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , I111iIi1 )
  if 60 - 60: I11i / I1ii11iIi11i
def iiiiIooo0O0O0OO ( ) :
 iIIII = OoOooO ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , o0ooooO0o0O , I1111i in i1IIIII11I1IiI :
  oOooOOoO ( I1111i , 100109 , Ii1I1Ii , image = IiI111ii1ii , isFolder = True )
  if 78 - 78: Ii1IIIi1
def o00OOOO000000 ( url ) :
 import random
 i1iI1Iiiiii11 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 i1iI1Iiiiii11 . clear ( )
 iII1I1iIIIiII = [ ]
 I11i1II1i = [ ]
 Oo0Ii = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoO , IiI111ii1ii , oo00O00oO000o , o0ooooO0o0O , I1111i in i1IIIII11I1IiI :
  iII1I1iIIIiII . append ( [ OoO , I1111i ] )
  if len ( iII1I1iIIIiII ) == len ( i1IIIII11I1IiI ) :
   for i11I in iII1I1iIIIiII :
    oO0Oo0 = random . randint ( 1 , len ( iII1I1iIIIiII ) )
    try :
     O0OoOOo0o = iII1I1iIIIiII [ int ( oO0Oo0 ) ]
    except :
     pass
    if len ( I11i1II1i ) <= 20 :
     if O0OoOOo0o [ 1 ] not in Oo0Ii :
      O0 = OoOooO ( O0OoOOo0o [ 0 ] )
      ooOoO00 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( O0 )
      for I1iIiiIii , O0OOOOO0O in ooOoO00 :
       oooooOoo0ooo = OoOooO ( I1iIiiIii )
       Iii1I1111ii = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oooooOoo0ooo )
       for ii111 , i1i in Iii1I1111ii :
        if 'panda' in i1i :
         ooO0o = OoOooO ( i1i )
         iiIii1I = re . compile ( "url: '(.+?)'" ) . findall ( ooO0o )
         for i1oO0o00oOo00oO in iiIii1I :
          if 'http' in i1oO0o00oOo00oO :
           oOO = xbmcgui . ListItem ( O0OoOOo0o [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           oOO . setInfo ( type = "Video" , infoLabels = { "Title" : O0OoOOo0o [ 1 ] } )
           oOO . setProperty ( "IsPlayable" , "true" )
           i1iI1Iiiiii11 . add ( i1oO0o00oOo00oO , oOO )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOO )
           if 68 - 68: iI11I1II1I1I - oOo0O0Ooo . o000O0o + OOooOOo
def oOooOOoO ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = Oo00OOOOO
 i1ii = sys . argv [ 0 ]
 i1ii += '?mode=' + str ( mode )
 i1ii += '&title=' + urllib . quote_plus ( name )
 i1ii += '&image=' + urllib . quote_plus ( image )
 i1ii += '&page=' + str ( page )
 if url != '' :
  i1ii += '&url=' + urllib . quote_plus ( url )
 if keyword :
  i1ii += '&keyword=' + urllib . quote_plus ( keyword )
 oOO = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  oOO . addContextMenuItems ( contextMenu )
 if infoLabels :
  oOO . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  oOO . setProperty ( "IsPlayable" , "true" )
 oOO . setProperty ( 'Fanart_Image' , O0o0Oo )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = isFolder )
 if 94 - 94: I11i % I11i % IIiIiII11i * iI11I1II1I1I / I1111IIi . Ii1I
 if 13 - 13: OOooOOo . oOo0O0Ooo . I11i * o000O0o / ii1ii11IIIiiI
def oo0 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , iconimage , oo00O00oO000o , o0ooooO0o0O , name in i1IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    iiIii1IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
    for i11I in iiIii1IIi :
     if i11I == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    iIiiII1Ii1ii ( name , url , 1016 , iconimage , o0ooooO0o0O , oo00O00oO000o )
   else :
    if 'youtube' in url :
     iiIii1IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for i11I in iiIii1IIi :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0000oO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , o0ooooO0o0O , oo00O00oO000o )
    else :
     iiIii1IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for i11I in iiIii1IIi :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0000oO ( name , url , 222 , iconimage , o0ooooO0o0O , oo00O00oO000o )
     I1I11i ( 'tvshows' , 'Media Info 3' )
  else :
   i1iiiiIi1 ( url , iconimage , name )
   if 15 - 15: O0OOOoOoo0 - ooOOOoO . iI11I1II1I1I + iI11I1II1I1I
 else :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
  for url , I111iIi1 , name in i1IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     Iiiiii111i1ii ( name , url , 1016 , I111iIi1 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      i1i1iII1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , I111iIi1 )
     else :
      iiIii1IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for i11I in iiIii1IIi :
       if i11I == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      i1i1iII1 ( name , url , 222 , I111iIi1 )
      I1I11i ( 'tvshows' , 'Media Info 3' )
   else :
    i1iiiiIi1 ( url , I111iIi1 , name )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 74 - 74: I1111IIi * Ii1I - ii
def i1iiiiIi1 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 O0OO00O0oOoo = ( url ) . replace ( i1iiIi1II1 , 'http' ) . replace ( OO00Oo00o , '.com' ) ;
 iiI = ( O0OO00O0oOoo ) . replace ( iiI1Iii , 'a' ) . replace ( i1II1IiIi111 , 'b' ) . replace ( oooI1iIiii , 'c' ) . replace ( oOOOOoo000Ooo , 'd' ) . replace ( ooo0O0Oo0O , 'e' ) . replace ( IiI1Ii , 'f' ) ;
 Ii1i1 = ( iiI ) . replace ( iiiiii1 , 'g' ) . replace ( ii1111iIIiIIi , 'h' ) . replace ( IiII1Iiii , 'i' ) . replace ( I1II11I11111i , 'j' ) . replace ( OoOOo0OO0OOoo , 'k' ) . replace ( i1Ii1 , 'l' ) ;
 IIiI = ( Ii1i1 ) . replace ( oOOOO00o00 , 'm' ) . replace ( OOo00o0oOO0o , 'n' ) . replace ( I1ii1O0O , 'o' ) . replace ( i111 , 'p' ) . replace ( o0OiI1 , 'q' ) . replace ( IiiI , 'r' ) ;
 III1i1iII1 = ( IIiI ) . replace ( IiiiiI11iii11iI , 's' ) . replace ( iiii1II , 't' ) . replace ( I111iIii1i1 , 'u' ) . replace ( I1i1I1i1I1 , 'v' ) . replace ( i1IOO , 'w' ) . replace ( Oo0OO0ooO0O0O , 'x' ) ;
 oO00O = ( III1i1iII1 ) . replace ( ooooooO0o00 , 'y' ) . replace ( Oo00o00O00 , 'z' ) . replace ( IiiOo , '.' ) . replace ( iiiIiii11i1i , '(' ) . replace ( Oo0oi1i , ')' ) . replace ( OO00O0O00oOOO , '/' ) ;
 OOOoOO = ( oO00O ) . replace ( I1IIo0o0OoOO00Oo , '1' ) . replace ( ii1iIiIIIII , '2' ) . replace ( OooOoOoo0ooo0 , '3' ) . replace ( I11i1I111II1IiI , '4' ) . replace ( oo00O0oOo , '5' ) . replace ( I1o000o00OO00Oo , '6' ) ;
 oO000oOo0oO0 = ( OOOoOO ) . replace ( oOO00o0oooOo0 , '7' ) . replace ( iIII1iIi , '8' ) . replace ( iiii1Ii , '9' ) . replace ( IIiiiI , '0' ) . replace ( i111ii1II11ii , ':' ) . replace ( i11iII1IiI , '%' ) ;
 url = ( oO000oOo0oO0 ) . replace ( Ooo00OoO , '-' ) . replace ( ooOo0Oo , '_' ) ;
 i1i1iII1 ( name , url , 222 , iconimage ) ;
 if 2 - 2: I11i - oOo0O0Ooo - Ii / ii
 if 87 - 87: I11i + o000O0o + ii * Ii1IIIi1
def IIIi1Iiii1I1 ( ) :
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for Ii1I1Ii , I111iIi1 , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , Ii1I1Ii , 1007 , I111iIi1 )
def iI1iiII1iii111 ( url ) :
 if 22 - 22: oOo0O0Ooo
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , I111iIi1 , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , I111iIi1 )
  if 76 - 76: oO0o + ooOOOoO + oO0o . ooOOOoO % Ii1IIIi1
def oOoOOO ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O0oO0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O0oO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0oO0 )
 if 10 - 10: Ii1IIIi1 . ii1ii11IIIiiI
 if 5 - 5: I1111IIi - ooOOOoO
def i11i ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in i1IIIII11I1IiI :
  if '-dir-' in I1111i :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , o00O0O )
  else :
   Iiiiii111i1ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , o00O0O )
   if 16 - 16: I1111IIi . O0OOOoOoo0 . I1ii11iIi11i % Ii1IIIi1 / I1111IIi
def OOO0oo0ooOoo ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 ii1i11III1I1 = ( 'http://afewbitsmore.com/' )
 i1IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '[To Parent Directory]' in I1111i :
   I1111i = 'HOME'
   pass
  elif 'HOME' in I1111i :
   pass
  elif '.m3u' in I1111i :
   Iiiiii111i1ii ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , ii1i11III1I1 + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in I1111i :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , ii1i11III1I1 + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in I1111i :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , ii1i11III1I1 + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ii1i11III1I1 + url , 1012 , III1iII1I1ii + 'music.png' )
def O000o ( url ) :
 oO0OOoo0OO = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for o00O0O , I1111i , url in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'music.png' )
  if 44 - 44: IIiIiII11i
def IIiiiiiiII ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 ii1i11III1I1 = url
 i1IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  if '.mp3' in I1111i :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/' , '' ) , ii1i11III1I1 + url , 1011 , III1iII1I1ii + 'music.png' )
def o00O00o0O0 ( ) :
 iIIII = o0O0O0ooo0oOO ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIIII )
 for Ii1I1Ii , o00O0O , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , ( 'http://www.cyn.net/music/' + Ii1I1Ii ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + o00O0O ) . replace ( ' ' , '%20' ) )
def Ii1ii1iIi1Ii1 ( url , img ) :
 iIIII = o0O0O0ooo0oOO ( url )
 OoO = url
 img = img
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( OoO + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 17 - 17: Ii
def I111Iii1 ( url ) :
 iIIII = o0O0O0ooo0oOO ( url )
 OoO = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for type , url , I1111i in i1IIIII11I1IiI :
  if '[VID]' in type :
   i1i1iII1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , OoO + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   I111Iii1 ( OoO + url )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: ii - I1111IIi + o000O0o . ii / ooOoO0O00
 if 53 - 53: iiiiiiii1 % Ii1I
def O0o0O00o0o ( ) :
 oOoO = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 IIi = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oo0OO = IIi . lower ( )
 Ii1I1Ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 OO0oOOo0o = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 OoO = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 17 - 17: ii % ii1ii11IIIiiI % o0o00Oo0O
 oO0OOoo0OO = O0o0O00Oo0o0 ( Ii1I1Ii )
 Oo0O0Oo00O = O0o0O00Oo0o0 ( OO0oOOo0o )
 O0 = O0o0O00Oo0o0 ( OoO )
 if 46 - 46: O0OOOoOoo0 + iiiiiiii1 % ii * Ii1I
 if oO0OOoo0OO != 'Failed' :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for Ii1I1Ii , IiI111ii1ii , oo00O00oO000o , oOoo000 , I1111i in i1IIIII11I1IiI :
   if IIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , Ii1I1Ii , 1016 , IiI111ii1ii , o0ooooO0o0O , oo00O00oO000o )
    if 89 - 89: I1111IIi - I1111IIi % O0OOOoOoo0 / ooOOOoO + o000O0o - I1111IIi
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if Oo0O0Oo00O != 'Failed' :
  OOoOOo0O00O = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Oo0O0Oo00O )
  for Ii1I1Ii , I1111i in OOoOOo0O00O :
   if IIi in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + Ii1I1Ii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 97 - 97: ii1ii11IIIiiI % OOooOOo / Ii1I / iI11I1II1I1I * ii * Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( O0 )
  for Ii1I1Ii , I1111i in i1I :
   if IIi in I1111i . lower ( ) :
    Iiiiii111i1ii ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + Ii1I1Ii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 80 - 80: o000O0o / o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: oOo0O0Ooo * ooOOOoO / o0o00Oo0O % OOooOOo
    if 71 - 71: Ii * OOooOOo * Ii1IIIi1 + o000O0o + I1ii11iIi11i
    if 59 - 59: I1111IIi
    if 54 - 54: Ii1IIIi1
    if 27 - 27: OOooOOo - oO0o + I11i + I11i1ii1 . oO0o
    if 86 - 86: IIiIiII11i - ii - I11i1ii1 % O0OOOoOoo0
oOOOO00o00 = '{SF},' ; OOo00o0oOO0o = '{IF},' ; I1ii1O0O = '{PW},' ; OooOoOoo0ooo0 = '{AM},' ; i111 = '{GF},' ; o0OiI1 = '{DD},' ; IiiI = '{UO},' ; IiiiiI11iii11iI = '{LE},' ; I111iIii1i1 = '{ZY},' ; I1i1I1i1I1 = '{UE},' ; i1IOO = '{PE},' ; Oo0OO0ooO0O0O = '{JE},' ; ooooooO0o00 = '{TH},' ; Oo00o00O00 = '{LK},'
if 16 - 16: I11i1ii1 + I1ii11iIi11i + ii
if 87 - 87: oOo0O0Ooo . o000O0o / I1111IIi - ii
def IiIi1I1ii111 ( ) :
 iIIII = OoOooO ( 'http://www.iwatchseries.me/tv-list/' )
 i1IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , Ii1I1Ii , 8021 , III1iII1I1ii + 'iwatch.png' )
  I1I11i ( 'movies' , 'MAIN' )
def IIiIii1iiI ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIIII )
 for url , I1111i , iIIIi1IiI11I1 in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i + iIIIi1IiI11I1 , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def o0oOOOOOO ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  IIIIII11iIiI1III ( url )
def IIIIII11iIiI1III ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iIIII )
 Iii1I1111ii = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( 'VidSpot - ' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in i1I :
  i1i1iII1 ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url , I1111i in Iii1I1111ii :
  i1i1iII1 ( 'VidUp' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for I1111i , url in ooOoO00 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   i1i1iII1 ( 'TheVideo - ' + I1111i , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 81 - 81: I1ii11iIi11i
def Oo0oOOo00o ( ) :
 iIIII = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 i1IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , Ii1I1Ii , 1021 , III1iII1I1ii + 'anime.png' )
  if 14 - 14: IIiIiII11i + o0o00Oo0O - O0OOOoOoo0
  if 18 - 18: I11i / Ii % Ii1I * ii
def o0OoOO0 ( ) :
 iIIII = OoOooO ( 'http://www.animetoon.org/cartoon' )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIII )
 for Ii1I1Ii , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , Ii1I1Ii , 1002 , III1iII1I1ii + 'anime.png' )
  if 75 - 75: oOo0O0Ooo
  if 99 - 99: I11i1ii1 . ii1ii11IIIiiI
  if 92 - 92: ooOoO0O00
def OOO0OOo0OoO ( url ) :
 iIIII = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  OOOOOO = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  Iiiiii111i1ii ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1IIIII11I1IiI :
  Iiiiii111i1ii ( I1111i , url , 1003 , OOOOOO )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO00OOO ( url , IMAGE ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in i1IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   Iiiii1I1ii1 ( url )
  elif 'playpanda' in url :
   Iiiii1I1ii1 ( url )
   if 31 - 31: Ii1I . OOooOOo . I11i1ii1 - iiiiiiii1 - I1ii11iIi11i % oOo0O0Ooo
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def Iiiii1I1ii1 ( url ) :
 iIIII = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in i1IIIII11I1IiI :
  i1i1iII1 ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 4 - 4: ii1ii11IIIiiI
  if 12 - 12: oO0o - oOo0O0Ooo + ii + ii * oOo0O0Ooo - ooOoO0O00
def OoOOOO0 ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 . add_header ( 'referer' , url )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 33 - 33: oOo0O0Ooo - O0OOOoOoo0 . ooOoO0O00 / Ii
def o0O0O0ooo0oOO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 84 - 84: ooOOOoO / ii / I1111IIi % ooOOOoO . Ii1IIIi1 + iiiiiiii1
def oO0OOOo0OO ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 Iii1Iii = ( '%s%s' % ( iiI11111II , url ) )
 i1i = o0O0O0ooo0oOO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , I111iIi1 , I1111i in i1IIIII11I1IiI :
  i1i1iII1 ( '%s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , I111iIi1 )
  if 25 - 25: Ii1IIIi1 / ii - Ii1I
def I1iI1i ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  iIIi ( url , I1111i )
 else :
  OOOOo0o00OO0000 ( url )
def OOOOo0o00OO0000 ( url ) :
 import urlresolver
 try :
  iI1II = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( iI1II , xbmcgui . ListItem ( I1111i ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( I1111i ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def OOOO00OooO ( url ) :
 if 15 - 15: ooOOOoO - iI11I1II1I1I % ii1ii11IIIiiI
 ii1IiIiI1 = open ( o00OO00OoO , "a" )
 ii1IiIiI1 . write ( 'url="' + url + '"\n' )
 ii1IiIiI1 . close
 if 47 - 47: O0OOOoOoo0 / ii - IIiIiII11i
 oO0o000OoOoO0 = xbmc . Player ( OO0ooOOO0O00o ( ) )
 import urlresolver
 try : oO0o000OoOoO0 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( I1111i ) )
 oO0o000OoOoO0 = xbmc . Player ( OO0ooOOO0O00o ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  OOooO0OOoo = xbmcgui . Dialog ( )
  if OOooO0OOoo . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   OOooO0OOoo . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oO0o000OoOoO0 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def iIIi ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  oOO00o0O0 = '.mp4'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOOo0o00OO0000 ( url )
  if iI11iI1IiiIiI == 1 :
   oOOooo ( url , name , oOO00o0O0 )
 elif '.mkv' in url :
  oOO00o0O0 = '.mkv'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOOo0o00OO0000 ( url )
  if iI11iI1IiiIiI == 1 :
   oOOooo ( url , name , oOO00o0O0 )
 elif '.mp3' in url :
  oOO00o0O0 = '.mp3'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOOo0o00OO0000 ( url )
  if iI11iI1IiiIiI == 1 :
   oOOooo ( url , name , oOO00o0O0 )
 elif '.avi' in url :
  oOO00o0O0 = '.avi'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOOo0o00OO0000 ( url )
  if iI11iI1IiiIiI == 1 :
   oOOooo ( url , name , oOO00o0O0 )
 elif '.mov' in url :
  oOO00o0O0 = '.mov'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOOo0o00OO0000 ( url )
  if iI11iI1IiiIiI == 1 :
   oOOooo ( url , name , oOO00o0O0 )
 elif '.mpeg' in url :
  oOO00o0O0 = '.mpeg'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOOo0o00OO0000 ( url )
  if iI11iI1IiiIiI == 1 :
   oOOooo ( url , name , oOO00o0O0 )
 elif '.mpg' in url :
  oOO00o0O0 = '.mpg'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOOo0o00OO0000 ( url )
  if iI11iI1IiiIiI == 1 :
   oOOooo ( url , name , oOO00o0O0 )
 elif '.flv' in url :
  oOO00o0O0 = '.flv'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOOo0o00OO0000 ( url )
  if iI11iI1IiiIiI == 1 :
   oOOooo ( url , name , oOO00o0O0 )
 elif '.wmv' in url :
  oOO00o0O0 = '.wmv'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOOo0o00OO0000 ( url )
  if iI11iI1IiiIiI == 1 :
   oOOooo ( url , name , oOO00o0O0 )
 else :
  OOOOo0o00OO0000 ( url )
def oOOooo ( url , name , cat ) :
 IiI11IiIIi ( )
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
def IiI11IiIIi ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def oOOo0OoooOo ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 oO0o000OoOoO0 = xbmc . Player ( OO0ooOOO0O00o ( ) )
 o0oOoO00o . update ( 100 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 oO0o000OoOoO0 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 33 - 33: ooOOOoO * O0OOOoOoo0 + iI11I1II1I1I - Ii1I
def OOoO0ooOO ( url ) :
 oO0o000OoOoO0 = xbmc . Player ( OO0ooOOO0O00o ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0o000OoOoO0 . play ( url ) . strip ( )
 except : pass
 if 11 - 11: IIiIiII11i + OOooOOo * ooOOOoO
def i1IiIII ( url ) :
 oO0o000OoOoO0 = xbmc . Player ( OO0ooOOO0O00o ( ) )
 import urlresolver
 O0OOO00 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 oO0o000OoOoO0 . play ( O0OOO00 )
 xbmc . sleep ( 1 )
 oO0o000OoOoO0 . play ( url )
 if 12 - 12: OOooOOo - I11i - iiiiiiii1 / ooOOOoO
 if 17 - 17: oO0o - iiiiiiii1 - IIiIiII11i / iiiiiiii1 / ii1ii11IIIiiI
def OO0ooOOO0O00o ( ) :
 try :
  I11III111i1I = getSet ( "core-player" )
  if ( I11III111i1I == 'DVDPLAYER' ) : O0ooOO0O00 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( I11III111i1I == 'MPLAYER' ) : O0ooOO0O00 = xbmc . PLAYER_CORE_MPLAYER
  elif ( I11III111i1I == 'PAPLAYER' ) : O0ooOO0O00 = xbmc . PLAYER_CORE_PAPLAYER
  else : O0ooOO0O00 = xbmc . PLAYER_CORE_AUTO
 except : O0ooOO0O00 = xbmc . PLAYER_CORE_AUTO
 return O0ooOO0O00
 return True
 if 84 - 84: I11i / iiiiiiii1 - o0o00Oo0O + oOo0O0Ooo . Ii1I
def Iiiiii111i1ii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i1ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oO0O = True
 oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iiiIIiIi = [ ]
  iiiIIiIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iiiIIiIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   iiiIIiIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOO . addContextMenuItems ( iiiIIiIi )
 oO0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = True )
 return oO0O
 if 30 - 30: O0OOOoOoo0 * ii1ii11IIIiiI % OOooOOo / I11i * I11i + o0o00Oo0O
def iI1iiiIii1II1 ( name , url , mode , iconimage , fanart , description ) :
 if 73 - 73: I11i / O0OOOoOoo0 % o0o00Oo0O . ooOoO0O00
 i1ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0O = True
 oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO . setProperty ( "Fanart_Image" , fanart )
 oO0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = True )
 return oO0O
 if 99 - 99: IIiIiII11i - Ii1I * I1111IIi
def i1i1iII1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i1ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oO0O = True
 oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  iiiIIiIi = [ ]
  iiiIIiIi . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   iiiIIiIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   iiiIIiIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  oOO . addContextMenuItems ( iiiIIiIi )
 oO0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = False )
 return oO0O
 if 3 - 3: I1111IIi - Ii1I * O0OOOoOoo0 * Ii1I + I1ii11iIi11i
 if 15 - 15: Ii1I * ii1ii11IIIiiI / O0OOOoOoo0 . I11i / ii1ii11IIIiiI % OOooOOo
 if 75 - 75: ii % Ii % iI11I1II1I1I % Ii1I / Ii
 if 96 - 96: I11i1ii1 * o000O0o / iI11I1II1I1I / ooOOOoO
 if 5 - 5: I11i
 if 83 - 83: ooOOOoO * oOo0O0Ooo . IIiIiII11i * ooOoO0O00 % o0o00Oo0O
def OO0O000 ( heading , announce ) :
 class IIII1i1IIIi ( ) :
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
   try : oooOo0OOOoo0 = open ( announce ) ; i1iI1IIi1I = oooOo0OOOoo0 . read ( )
   except : i1iI1IIi1I = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( i1iI1IIi1I ) )
   return
 IIII1i1IIIi ( )
 IIII1i1IIIi ( )
 if 25 - 25: o000O0o % I11i1ii1 - O0OOOoOoo0 * oO0o
def OOoO0 ( ) :
 OO0O000 ( 'GenieTv Recomended Sources' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Reaper[/COLOR] [CR]  [COLORred]http://roguemedia.info/cerberus/repo/[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 37 - 37: ooOoO0O00 + I1111IIi - ooOoO0O00 % ii + I1111IIi + iI11I1II1I1I
 if 30 - 30: Ii % I11i . ooOoO0O00
 if 49 - 49: I11i * ii1ii11IIIiiI + I1ii11iIi11i
 if 1 - 1: I11i / IIiIiII11i + ooOOOoO . Ii + I11i1ii1 . OOooOOo
 if 95 - 95: I11i / iiiiiiii1 % IIiIiII11i + I11i1ii1
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 97 - 97: Ii1IIIi1
 if 55 - 55: I11i1ii1
 if 1 - 1: oO0o
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
 if 17 - 17: IIiIiII11i
 if 66 - 66: I1111IIi * o000O0o
 if 73 - 73: Ii + o0o00Oo0O % o0o00Oo0O
 if 70 - 70: IIiIiII11i * ii - ii1ii11IIIiiI + o000O0o * o0o00Oo0O
 if 49 - 49: o000O0o . ii1ii11IIIiiI . OOooOOo - Ii1I
 if 74 - 74: I11i1ii1 % Ii1I * ooOoO0O00
 if 18 - 18: OOooOOo
 if 30 - 30: IIiIiII11i
 if 27 - 27: ooOoO0O00 - iI11I1II1I1I + o0o00Oo0O % I1ii11iIi11i / Ii1IIIi1 + ooOoO0O00
 if 48 - 48: I1ii11iIi11i
 if 70 - 70: ii * Ii
def O0OooOoOOoooO00oO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + ooOooOOoO0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 50 - 50: O0OOOoOoo0 . oOo0O0Ooo
def O00oo00Ooo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + i11i11iiIiIiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 76 - 76: ooOOOoO
def Oo00OoOoo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o0Oi1i1i11IIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 11 - 11: I11i1ii1 . iiiiiiii1 - O0OOOoOoo0 . I11i
def IIIIII1iI11IiIi1II ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + OooooO0000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 95 - 95: ooOOOoO - iI11I1II1I1I
def iIIioo0 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + i1iiI1ii1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 22 - 22: Ii
def o0Ooo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + I11ii1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 86 - 86: o000O0o % iI11I1II1I1I % OOooOOo
def OO000OOO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o000OOooo000O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 69 - 69: o0o00Oo0O . O0OOOoOoo0
def o0oOoO00oo0oOo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iiOO00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 15 - 15: o0o00Oo0O
def I11IiI1III ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + O0oOoi1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , IiI111ii1ii , o0ooooO0o0O , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 32 - 32: I11i1ii1 / IIiIiII11i . o0o00Oo0O . I11i1ii1 % oOo0O0Ooo - I11i
def oOooO0 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + O00OoO0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for I1111i , url , IiI111ii1ii , o0ooooO0o0O , oOOOO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , oOOOO )
 I1I11i ( 'movies' , 'MAIN' )
 if 47 - 47: oO0o . Ii
 if 9 - 9: OOooOOo - ooOOOoO . ii % I11i1ii1
 if 13 - 13: oO0o * iI11I1II1I1I + IIiIiII11i - I1ii11iIi11i - OOooOOo
 if 43 - 43: O0OOOoOoo0 / iiiiiiii1 * oOo0O0Ooo % I11i1ii1 % oOo0O0Ooo
 if 18 - 18: oO0o
 if 99 - 99: O0OOOoOoo0 / o000O0o . Ii / ooOOOoO + ooOoO0O00 - ooOOOoO
 if 50 - 50: ooOoO0O00
 if 56 - 56: oO0o + iiiiiiii1 / ii1ii11IIIiiI
 if 75 - 75: OOooOOo
def Iii1OOoO ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for ii1111I , i1I111II , Oo0OOo in os . walk ( iIi1ii1I1 ) :
     oO00OO0Ooo00O = 0
     oO00OO0Ooo00O += len ( Oo0OOo )
     if oO00OO0Ooo00O > 0 :
      for oooOo0OOOoo0 in Oo0OOo :
       os . unlink ( os . path . join ( ii1111I , oooOo0OOOoo0 ) )
  II1iII1IIIIi = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( II1iII1IIIIi )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 98 - 98: I11i
 if 51 - 51: iI11I1II1I1I / I1111IIi / O0OOOoOoo0
 if 31 - 31: ooOOOoO + I1ii11iIi11i
 if 16 - 16: o0o00Oo0O
 if 80 - 80: ooOOOoO / I1ii11iIi11i + Ii1I
 if 18 - 18: IIiIiII11i - O0OOOoOoo0 / iI11I1II1I1I % OOooOOo % Ii1I / I11i
 if 47 - 47: Ii1IIIi1
 if 24 - 24: ii1ii11IIIiiI % I11i
def I1IIIi ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 87 - 87: I11i % O0OOOoOoo0 / I11i1ii1 - I1111IIi + Ii
def o0ooooO0 ( url ) :
 Ooo0oOo0o0oOo = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 O0i1I1ii1iI1 = [
 ( Ooo0oOo0o0oOo ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( Ooo0oOo0o0oOo , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( Ooo0oOo0o0oOo , 'plugin.video.itv' , 'Images' ) ) ]
 if 63 - 63: o0o00Oo0O . iiiiiiii1 / iiiiiiii1 / iI11I1II1I1I + Ii1IIIi1 . ooOOOoO
 oO0oOO000 = 0
 if 69 - 69: o0o00Oo0O % o0o00Oo0O - O0OOOoOoo0 - o000O0o
 for i11I in O0i1I1ii1iI1 :
  if os . path . exists ( i11I ) and not i11I in [ oO0o0o0ooO0oO , Ooo0oOo0o0oOo ] :
   for ii1111I , i1I111II , Oo0OOo in os . walk ( i11I ) :
    oO00OO0Ooo00O = 0
    oO00OO0Ooo00O += len ( Oo0OOo )
    if oO00OO0Ooo00O > 0 :
     for oooOo0OOOoo0 in Oo0OOo :
      if not oooOo0OOOoo0 in oooOOOOO :
       try :
        os . unlink ( os . path . join ( ii1111I , oooOo0OOOoo0 ) )
       except :
        pass
      else : iIiIi11 ( 'Ignore Log File: %s' % oooOo0OOOoo0 )
     for OOoO0oO00o in i1I111II :
      try :
       shutil . rmtree ( os . path . join ( ii1111I , OOoO0oO00o ) )
       oO0oOO000 += 1
       iIiIi11 ( "[Success] cleared %s files from %s" % ( str ( oO00OO0Ooo00O ) , os . path . join ( i11I , OOoO0oO00o ) ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , OOoO0oO00o ) )
  else :
   for ii1111I , i1I111II , Oo0OOo in os . walk ( i11I ) :
    for OOoO0oO00o in i1I111II :
     if 'cache' in OOoO0oO00o . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ii1111I , OOoO0oO00o ) )
       oO0oOO000 += 1
       iIiIi11 ( "[Success] wiped %s " % os . path . join ( i11I , OOoO0oO00o ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , OOoO0oO00o ) )
       if 83 - 83: Ii + iI11I1II1I1I
 I1IIIi ( oO , 'Clear Cache: Removed %s Files' % oO0oOO000 )
 if 21 - 21: I11i / Ii % iiiiiiii1
 if 56 - 56: I11i * iI11I1II1I1I . ii1ii11IIIiiI + OOooOOo % iiiiiiii1
 if 11 - 11: Ii1IIIi1
 if 12 - 12: ii * Ii1IIIi1 * Ii1I * I11i1ii1
 if 26 - 26: ii . ooOoO0O00 + oO0o
 if 42 - 42: Ii * I11i % ooOOOoO % I1ii11iIi11i + I11i * Ii
 if 66 - 66: ii1ii11IIIiiI / I1111IIi . ii * I1ii11iIi11i % Ii
def IIII1ii1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 OO0oOo00OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1111I , i1I111II , Oo0OOo in os . walk ( OO0oOo00OO0 ) :
   oO00OO0Ooo00O = 0
   oO00OO0Ooo00O += len ( Oo0OOo )
   if 25 - 25: I1ii11iIi11i * I1111IIi % oOo0O0Ooo . O0OOOoOoo0 % O0OOOoOoo0 * I1ii11iIi11i
   if 1 - 1: I1ii11iIi11i / I11i1ii1 * ii1ii11IIIiiI - ii * ooOOOoO * Ii1IIIi1
   if oO00OO0Ooo00O > 0 :
    if 63 - 63: IIiIiII11i - I11i * Ii / ooOOOoO * O0OOOoOoo0 - O0OOOoOoo0
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( oO00OO0Ooo00O ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: I1ii11iIi11i . o0o00Oo0O
     for oooOo0OOOoo0 in Oo0OOo :
      os . unlink ( os . path . join ( ii1111I , oooOo0OOOoo0 ) )
     for OOoO0oO00o in i1I111II :
      shutil . rmtree ( os . path . join ( ii1111I , OOoO0oO00o ) )
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
 if 48 - 48: Ii1I % IIiIiII11i + ooOOOoO
 if 25 - 25: I1111IIi * I11i / oOo0O0Ooo . I1111IIi % IIiIiII11i
 if 50 - 50: OOooOOo * O0OOOoOoo0
 if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / ooOOOoO
 if 92 - 92: I11i
 if 8 - 8: O0OOOoOoo0 + Ii1I . ii1ii11IIIiiI
 if 50 - 50: I1ii11iIi11i
 if 16 - 16: ii1ii11IIIiiI - OOooOOo % I1ii11iIi11i / ii1ii11IIIiiI . ooOOOoO + I11i1ii1
 if 78 - 78: iI11I1II1I1I + oO0o + Ii
def I1iIIiiIIi1i ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 OO0oOo00OO0 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ii1111I , i1I111II , Oo0OOo in os . walk ( OO0oOo00OO0 ) :
   oO00OO0Ooo00O = 0
   oO00OO0Ooo00O += len ( Oo0OOo )
   if 21 - 21: I1ii11iIi11i + ii1ii11IIIiiI % I11i1ii1 + OOooOOo % ooOOOoO
   if 22 - 22: ooOoO0O00 / ii . oO0o
   if oO00OO0Ooo00O > 0 :
    if 83 - 83: oOo0O0Ooo - ii + Ii1I . ii1ii11IIIiiI / I11i + I11i1ii1
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( oO00OO0Ooo00O ) + " files found" , "Do you want to delete them?" ) :
     if 90 - 90: oOo0O0Ooo - Ii
     for oooOo0OOOoo0 in Oo0OOo :
      os . unlink ( os . path . join ( ii1111I , oooOo0OOOoo0 ) )
     for OOoO0oO00o in i1I111II :
      shutil . rmtree ( os . path . join ( ii1111I , OOoO0oO00o ) )
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
 o0ooooO0 ( url )
 return
 if 42 - 42: Ii1IIIi1 . I1ii11iIi11i
 if 21 - 21: O0OOOoOoo0 . oOo0O0Ooo / ooOOOoO
 if 97 - 97: iI11I1II1I1I + ooOoO0O00 - I11i
 if 73 - 73: oO0o - Ii % iiiiiiii1 / I1ii11iIi11i - ii % Ii1IIIi1
 if 79 - 79: oOo0O0Ooo / I11i . ii1ii11IIIiiI * Ii1I + ooOOOoO
 if 96 - 96: oO0o * IIiIiII11i
 if 1 - 1: oOo0O0Ooo - OOooOOo
 if 74 - 74: OOooOOo * IIiIiII11i + o0o00Oo0O + ooOOOoO
 if 3 - 3: iI11I1II1I1I - ooOoO0O00 / O0OOOoOoo0 + ooOoO0O00 + o0o00Oo0O
 if 18 - 18: iI11I1II1I1I . O0OOOoOoo0 % Ii1IIIi1 % o000O0o + iI11I1II1I1I * ii
def oOo0OOoooOOo ( url , name ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ooIIi1i1i1 = os . path . join ( o00O0 , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 II1111i1I111 = os . path . join ( o00O0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( II1111i1I111 ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   ooIIi1i1i1 = os . path . join ( o00O0 , 'advancedsettings.xml' )
   try :
    os . remove ( ooIIi1i1i1 )
    print '=== GenieTv - REMOVING    ' + str ( ooIIi1i1i1 ) + '    ==='
   except :
    pass
   i1i = iI111I11I1I1 . http_GET ( url ) . content
   OoOOOOOO = open ( ooIIi1i1i1 , "w" )
   OoOOOOOO . write ( i1i )
   OoOOOOOO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( ooIIi1i1i1 ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  ooIIi1i1i1 = os . path . join ( o00O0 , 'advancedsettings.xml' )
  try :
   os . remove ( ooIIi1i1i1 )
   print '=== GenieTv - REMOVING    ' + str ( ooIIi1i1i1 ) + '    ==='
  except :
   pass
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  OoOOOOOO = open ( ooIIi1i1i1 , "w" )
  OoOOOOOO . write ( i1i )
  OoOOOOOO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ooIIi1i1i1 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 95 - 95: ii / O0OOOoOoo0
def Iii1ii ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ooIIi1i1i1 = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  OoOOOOOO = open ( ooIIi1i1i1 ) . read ( )
  if 'zero' in OoOOOOOO :
   name = '0CACHE'
  elif 'tuxen' in OoOOOOOO :
   name = 'TUXENS'
  elif 'muckys' in OoOOOOOO :
   name = 'MUCKYS'
  elif 'p2p1' in OoOOOOOO :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in OoOOOOOO :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in OoOOOOOO :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 45 - 45: Ii * Ii1I / ii1ii11IIIiiI % o0o00Oo0O / o000O0o * o000O0o
def ooOo00OOo0 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 ooIIi1i1i1 = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  os . remove ( ooIIi1i1i1 )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( ooIIi1i1i1 ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 12 - 12: Ii + Ii1I * oO0o
 if 13 - 13: I1ii11iIi11i + ii / I1111IIi
 if 56 - 56: Ii1I * IIiIiII11i
 if 75 - 75: ooOOOoO . I11i - Ii / ooOOOoO
 if 100 - 100: Ii * Ii . iI11I1II1I1I % O0OOOoOoo0 * Ii1I
 if 17 - 17: ii1ii11IIIiiI * I1111IIi * Ii / Ii1I / Ii
 if 23 - 23: ii + Ii / I1ii11iIi11i / O0OOOoOoo0 . O0OOOoOoo0 * oOo0O0Ooo
 if 98 - 98: I1111IIi
 if 23 - 23: ooOOOoO / ooOoO0O00 * oO0o
 if 51 - 51: Ii1IIIi1 - ii / ii % ii
def OOO0O0OOo ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 i1IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for oOo , oOOo000o0o , O0OO0o , iIiI in i1IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % oOo , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % O0OO0o , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iIiI )
  inc = inc + 1
  if 17 - 17: Ii1I + o000O0o * iiiiiiii1 - I11i1ii1 + iI11I1II1I1I . I1ii11iIi11i
  if 8 - 8: ooOoO0O00 + oO0o
  if 95 - 95: oOo0O0Ooo / I11i % IIiIiII11i * iiiiiiii1 . I1111IIi % oO0o
  if 45 - 45: Ii1I . ooOOOoO . IIiIiII11i - IIiIiII11i * ii
  if 71 - 71: Ii1IIIi1
  if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
  if 11 - 11: I11i * oO0o
  if 92 - 92: OOooOOo . I1ii11iIi11i * ooOOOoO
  if 86 - 86: o0o00Oo0O
def O0o00 ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  ooIIi1i1i1 = os . path . join ( o00O0 , 'addons2.ini' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  OoOOOOOO = open ( ooIIi1i1i1 , "w" )
  OoOOOOOO . write ( i1i )
  OoOOOOOO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ooIIi1i1i1 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 60 - 60: oOo0O0Ooo * OOooOOo - o000O0o + ii % ooOoO0O00
def iIIIIiI1I ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  ooIIi1i1i1 = os . path . join ( o00O0 , 'settings.xml' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  OoOOOOOO = open ( ooIIi1i1i1 , "w" )
  OoOOOOOO . write ( i1i )
  OoOOOOOO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( ooIIi1i1i1 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 97 - 97: oOo0O0Ooo * I11i
 if 79 - 79: O0OOOoOoo0 - I11i1ii1 - oO0o / iI11I1II1I1I % ii1ii11IIIiiI
def IiIiii ( ) :
 try :
  OoOoooO0OO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OoOoooO0OO ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    O00OOo = os . path . join ( OoOoooO0OO , "source.db" )
    os . unlink ( O00OOo )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 77 - 77: o0o00Oo0O - ii1ii11IIIiiI * IIiIiII11i / Ii1I / ii1ii11IIIiiI - o000O0o
 if 66 - 66: oO0o % I1ii11iIi11i . IIiIiII11i
 if 84 - 84: I11i1ii1 * ii + o0o00Oo0O
 if 84 - 84: ooOoO0O00 . ooOOOoO . ooOoO0O00 . I1ii11iIi11i
 if 21 - 21: IIiIiII11i . o0o00Oo0O + I1ii11iIi11i - Ii
def OoOooO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 5 - 5: iI11I1II1I1I * Ii + oO0o + ooOOOoO * o0o00Oo0O % I11i1ii1
 if 88 - 88: I11i / Ii * Ii1I
 if 23 - 23: o0o00Oo0O / O0OOOoOoo0
 if 66 - 66: ooOoO0O00 % ii * Ii + o000O0o * o0o00Oo0O / oO0o
 if 14 - 14: oOo0O0Ooo . I1111IIi
 if 29 - 29: ii / I1111IIi + OOooOOo - iiiiiiii1 + I1111IIi . ooOoO0O00
 if 26 - 26: Ii - IIiIiII11i
def i11i1ii1I ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iIII1 = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iIII1 :
  oooo0ooo0 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; oooo0ooo0 = xbmc . translatePath ( oooo0ooo0 ) ;
  iI11 = os . path . join ( oooo0ooo0 , ".." , ".." ) ; iI11 = os . path . abspath ( iI11 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + iI11 ) ; oO0o0 = False
  try :
   for ii1111I , i1I111II , Oo0OOo in os . walk ( iI11 , topdown = True ) :
    i1I111II [ : ] = [ OOoO0oO00o for OOoO0oO00o in i1I111II if OOoO0oO00o not in o0oO0 ]
    for I1111i in Oo0OOo :
     try : os . remove ( os . path . join ( ii1111I , I1111i ) )
     except :
      if I1111i not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : oO0o0 = True
      plugintools . log ( "Error removing " + ii1111I + " " + I1111i )
    for I1111i in i1I111II :
     try : os . rmdir ( os . path . join ( ii1111I , I1111i ) )
     except :
      if I1111i not in [ "Database" , "userdata" ] : oO0o0 = True
      plugintools . log ( "Error removing " + ii1111I + " " + I1111i )
   if not oO0o0 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OOOO00o000o ( )
 if 78 - 78: O0OOOoOoo0 / Ii1I . Ii
 if 69 - 69: ooOOOoO - IIiIiII11i
 if 66 - 66: oOo0O0Ooo . oOo0O0Ooo - OOooOOo * ii * IIiIiII11i + oOo0O0Ooo
def oOoOoOo0O0o ( ) :
 IiIIIIII = [ ]
 OOO0O = sys . argv [ 2 ]
 if len ( OOO0O ) >= 2 :
  o0OO0o0o00o = sys . argv [ 2 ]
  I1iI1iIIIii = o0OO0o0o00o . replace ( '?' , '' )
  if ( o0OO0o0o00o [ len ( o0OO0o0o00o ) - 1 ] == '/' ) :
   o0OO0o0o00o = o0OO0o0o00o [ 0 : len ( o0OO0o0o00o ) - 2 ]
  I1iI = I1iI1iIIIii . split ( '&' )
  IiIIIIII = { }
  for oooo in range ( len ( I1iI ) ) :
   I1IiiI1i1 = { }
   I1IiiI1i1 = I1iI [ oooo ] . split ( '=' )
   if ( len ( I1IiiI1i1 ) ) == 2 :
    IiIIIIII [ I1IiiI1i1 [ 0 ] ] = I1IiiI1i1 [ 1 ]
    if 23 - 23: oO0o / I11i
 return IiIIIIII
 if 22 - 22: Ii1IIIi1 - oO0o . ooOOOoO
oooO00O0O0OOO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
i11ii1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
I1iIiIi111 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OO0o0oo = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
I111 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
o00I11II1iI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
ooOooOOoO0O = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
i1Ooo0O0OO0OOo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
i11i11iiIiIiI = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
o0Oi1i1i11IIii = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OooooO0000 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i1iiI1ii1ii = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
I11ii1i1 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o000OOooo000O = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iiOO00O = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
O0oOoi1Ii = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iIiiiIIiii = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
i111ii11I1 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
I1I1 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
iIIiiiIii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
o0Oo00oOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
O000o0Iiiii1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
O00OoO0oo = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
iiI11111II = base64 . decodestring ( 'Q1VOVA==' )
def iiOOooooO0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 i1ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0O = True
 oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iiiIIiIi = [ ]
  if showcontext == 'fav' :
   iiiIIiIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   iiiIIiIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oOO . addContextMenuItems ( iiiIIiIi )
 oO0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = True )
 return oO0O
 if 31 - 31: IIiIiII11i + Ii
def OOiIiIIi1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 i1ii = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 oO0O = True
 oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 oOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  iiiIIiIi = [ ]
  if showcontext == 'fav' :
   iiiIIiIi . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   iiiIIiIi . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  oOO . addContextMenuItems ( iiiIIiIi )
 oO0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1ii , listitem = oOO , isFolder = False )
 return oO0O
 if 72 - 72: Ii1IIIi1 % o0o00Oo0O * I11i1ii1 % oOo0O0Ooo
 if 99 - 99: IIiIiII11i . o000O0o % Ii + I1ii11iIi11i
o0OO0o0o00o = oOoOoOo0O0o ( )
Ii1I1Ii = None
I1111i = None
O0OOO0OOooo00 = None
IiI111ii1ii = None
o0ooooO0o0O = None
oOOOO = None
IIiiIi1i11i = None
O000o0oO0o = None
if 64 - 64: ooOoO0O00 / I1111IIi . I1111IIi - iiiiiiii1 % Ii1IIIi1 . IIiIiII11i
if 78 - 78: iiiiiiii1 - o0o00Oo0O - iiiiiiii1 . iI11I1II1I1I % Ii1I . ii
try :
 O000o0oO0o = int ( o0OO0o0o00o [ "fav_mode" ] )
except :
 pass
 if 64 - 64: I1111IIi
try :
 Ii1I1Ii = urllib . unquote_plus ( o0OO0o0o00o [ "url" ] )
except :
 pass
try :
 I1111i = urllib . unquote_plus ( o0OO0o0o00o [ "name" ] )
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
 oOOOO = urllib . unquote_plus ( o0OO0o0o00o [ "description" ] )
except :
 pass
 if 21 - 21: I11i - I11i1ii1 * ii . ii
 if 17 - 17: Ii1IIIi1 - O0OOOoOoo0 % oOo0O0Ooo * Ii1IIIi1 * iI11I1II1I1I . I11i
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( O0OOO0OOooo00 )
print "URL: " + str ( Ii1I1Ii )
print "Name: " + str ( I1111i )
print "IconImage: " + str ( IiI111ii1ii )
if 58 - 58: o000O0o - IIiIiII11i + o0o00Oo0O
if 54 - 54: iI11I1II1I1I - I1111IIi - I1111IIi
def I1I11i ( content , viewType ) :
 if 18 - 18: Ii + iI11I1II1I1I . Ii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 63 - 63: O0OOOoOoo0 - oO0o * Ii1IIIi1
if IiI111ii1ii == None : IiI111ii1ii = Oo00OOOOO
if o0ooooO0o0O == None : o0ooooO0o0O = O0o0Oo
if O0OOO0OOooo00 == None :
 o0o0o0oO0oOO ( )
 if 89 - 89: O0OOOoOoo0 / I1ii11iIi11i
elif O0OOO0OOooo00 == 1 :
 o00oOoo0o00 ( Ii1I1Ii )
 if 66 - 66: I11i + OOooOOo % ii . ooOOOoO
elif O0OOO0OOooo00 == 44 :
 oOo0 ( Ii1I1Ii )
 if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
elif O0OOO0OOooo00 == 2 :
 O0OoOOoooo ( )
 if 93 - 93: ooOoO0O00 + iiiiiiii1 / oO0o - ooOOOoO % I1ii11iIi11i / ii1ii11IIIiiI
elif O0OOO0OOooo00 == 3 :
 O00oOooo00o0o ( )
 if 1 - 1: I1ii11iIi11i / ii1ii11IIIiiI . Ii % Ii1IIIi1 + I11i + o0o00Oo0O
elif O0OOO0OOooo00 == 21 :
 i1i1II ( )
 if 54 - 54: iiiiiiii1 + I11i1ii1 % I1111IIi
elif O0OOO0OOooo00 == 4 :
 o0ooOO00OO0o0O ( )
 if 83 - 83: I11i * iI11I1II1I1I
elif O0OOO0OOooo00 == 5 :
 ooo0o0O ( Ii1I1Ii )
 if 36 - 36: OOooOOo + IIiIiII11i - oO0o % I11i1ii1 * ooOoO0O00
elif O0OOO0OOooo00 == 6 :
 IIII1ii1 ( Ii1I1Ii )
 if 4 - 4: ii1ii11IIIiiI + oO0o * Ii1I
elif O0OOO0OOooo00 == 7 :
 oOo0OOoooOOo ( Ii1I1Ii , I1111i )
 if 13 - 13: OOooOOo - I1111IIi * iI11I1II1I1I * o0o00Oo0O
elif O0OOO0OOooo00 == 8 :
 Iii1ii ( Ii1I1Ii , I1111i )
 if 26 - 26: ii + o000O0o + oO0o . o0o00Oo0O
elif O0OOO0OOooo00 == 9 :
 FIXREPOSADDONS ( Ii1I1Ii )
 if 46 - 46: ii - I1ii11iIi11i * iiiiiiii1 * Ii1IIIi1 * iiiiiiii1 . o000O0o
elif O0OOO0OOooo00 == 10 :
 O0O0ooOOO ( )
 if 96 - 96: ii1ii11IIIiiI / I1111IIi % I11i + ooOOOoO
elif O0OOO0OOooo00 == 11 :
 ooOo00OOo0 ( Ii1I1Ii )
 if 46 - 46: oO0o * oOo0O0Ooo
elif O0OOO0OOooo00 == 12 :
 OOO0O0OOo ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 25 - 25: iiiiiiii1 . I1111IIi % o0o00Oo0O % ooOoO0O00
elif O0OOO0OOooo00 == 13 :
 Iii1OOoO ( )
 if 53 - 53: o0o00Oo0O % I11i1ii1
elif O0OOO0OOooo00 == 14 :
 o0ooooO0 ( Ii1I1Ii )
 if 41 - 41: I1111IIi
elif O0OOO0OOooo00 == 15 :
 Ii11IiI111 ( )
 if 29 - 29: I11i1ii1
elif O0OOO0OOooo00 == 16 :
 O0o00 ( Ii1I1Ii , I1111i )
 if 70 - 70: o000O0o . o0o00Oo0O % ooOOOoO % I1111IIi - ooOOOoO * Ii1I
elif O0OOO0OOooo00 == 17 :
 iIIIIiI1I ( Ii1I1Ii , I1111i )
 if 22 - 22: ooOoO0O00
elif O0OOO0OOooo00 == 18 :
 IiIiii ( )
 if 82 - 82: o000O0o . iI11I1II1I1I - Ii1I
elif O0OOO0OOooo00 == 19 :
 o000 ( Ii1I1Ii )
 if 55 - 55: I1ii11iIi11i % ii1ii11IIIiiI . iI11I1II1I1I * iiiiiiii1
elif O0OOO0OOooo00 == 40 :
 o0oOOoo0O ( I1111i , Ii1I1Ii , oOOOO )
 if 33 - 33: o0o00Oo0O - oOo0O0Ooo / Ii1I / oO0o + O0OOOoOoo0 - o000O0o
elif O0OOO0OOooo00 == 42 :
 I1Iiii1Ii ( I1111i , Ii1I1Ii , oOOOO )
 if 27 - 27: iiiiiiii1 + I11i1ii1 - iiiiiiii1 % Ii * I1ii11iIi11i * I11i
elif O0OOO0OOooo00 == 43 :
 Ii1iIi ( Ii1I1Ii )
 if 88 - 88: Ii1IIIi1
elif O0OOO0OOooo00 == 20 :
 oooIi1I11IiI1i ( Ii1I1Ii )
 if 25 - 25: oO0o + I11i . I11i1ii1 - ii1ii11IIIiiI . o000O0o * ii1ii11IIIiiI
elif O0OOO0OOooo00 == 22 :
 O0OooOoOOoooO00oO ( Ii1I1Ii )
 if 85 - 85: ooOoO0O00
elif O0OOO0OOooo00 == 23 :
 O00oo00Ooo ( Ii1I1Ii )
 if 94 - 94: ii . o0o00Oo0O / ii
elif O0OOO0OOooo00 == 24 :
 Oo00OoOoo ( Ii1I1Ii )
 if 67 - 67: Ii + OOooOOo
elif O0OOO0OOooo00 == 25 :
 IIIIII1iI11IiIi1II ( Ii1I1Ii )
 if 50 - 50: I11i1ii1 . ooOoO0O00 + Ii1I . Ii1IIIi1
elif O0OOO0OOooo00 == 26 :
 iIIioo0 ( Ii1I1Ii )
 if 97 - 97: oOo0O0Ooo
elif O0OOO0OOooo00 == 27 :
 o0Ooo ( Ii1I1Ii )
 if 63 - 63: o0o00Oo0O - OOooOOo / Ii / ii / I11i1ii1 / IIiIiII11i
elif O0OOO0OOooo00 == 28 :
 OO000OOO ( Ii1I1Ii )
 if 45 - 45: IIiIiII11i . oO0o + oO0o * iI11I1II1I1I
elif O0OOO0OOooo00 == 29 :
 o0oOoO00oo0oOo ( Ii1I1Ii )
 if 23 - 23: I1111IIi * OOooOOo % ii1ii11IIIiiI / ii1ii11IIIiiI - I11i1ii1 - Ii1IIIi1
elif O0OOO0OOooo00 == 30 :
 I1ii1I1iii1 ( Ii1I1Ii )
 if 86 - 86: Ii1IIIi1 . ii * oOo0O0Ooo - I1ii11iIi11i / Ii * O0OOOoOoo0
elif O0OOO0OOooo00 == 31 :
 I11IiI1III ( Ii1I1Ii )
 if 56 - 56: oOo0O0Ooo . ooOOOoO % O0OOOoOoo0
elif O0OOO0OOooo00 == 32 :
 O0O0OOOOoo ( )
 if 33 - 33: ooOOOoO / Ii1IIIi1 - Ii1IIIi1 / Ii * OOooOOo + o0o00Oo0O
elif O0OOO0OOooo00 == 33 :
 O00Ooo0O0OOOo ( )
 if 2 - 2: Ii % oOo0O0Ooo
elif O0OOO0OOooo00 == 35 :
 iI1iIIIIIiIi1 ( Ii1I1Ii )
 if 90 - 90: IIiIiII11i
elif O0OOO0OOooo00 == 34 :
 o0oooo0O ( Ii1I1Ii )
 if 2 - 2: ii1ii11IIIiiI - ii - Ii % I1ii11iIi11i / ii1ii11IIIiiI
elif O0OOO0OOooo00 == 36 :
 OOooOoO ( Ii1I1Ii )
 if 77 - 77: I11i . I11i * iiiiiiii1 + Ii1IIIi1 - Ii
elif O0OOO0OOooo00 == 37 :
 Ii1I1IIIiI1i ( Ii1I1Ii )
 if 45 - 45: oOo0O0Ooo . oOo0O0Ooo - I1ii11iIi11i * Ii1IIIi1
elif O0OOO0OOooo00 == 38 :
 IiI1IiI1iiI1 ( Ii1I1Ii )
 if 71 - 71: ooOoO0O00 / ooOOOoO
elif O0OOO0OOooo00 == 41 :
 i11i1ii1I ( o0OO0o0o00o )
 if 14 - 14: ii
elif O0OOO0OOooo00 == 39 :
 oOooO0 ( Ii1I1Ii )
 if 99 - 99: I11i * I11i
elif O0OOO0OOooo00 == 45 :
 TEXTS ( )
 if 6 - 6: Ii + o000O0o % I11i1ii1 + Ii - Ii1IIIi1
elif O0OOO0OOooo00 == 46 :
 OOoO0 ( )
 if 12 - 12: O0OOOoOoo0 . o000O0o % I1111IIi * ii . I1111IIi
elif O0OOO0OOooo00 == 47 :
 GEVID ( )
 if 15 - 15: oOo0O0Ooo . oOo0O0Ooo / Ii
elif O0OOO0OOooo00 == 48 :
 iiI111i1 ( I1111i , Ii1I1Ii , oOOOO )
 if 17 - 17: iI11I1II1I1I / oO0o - IIiIiII11i
elif O0OOO0OOooo00 == 49 :
 iI1i111I1Ii ( )
 if 46 - 46: iI11I1II1I1I * o000O0o / Ii + IIiIiII11i + ooOOOoO
elif O0OOO0OOooo00 == 22222 :
 OOOO00OooO ( Ii1I1Ii )
 if 30 - 30: o0o00Oo0O * I1111IIi - iiiiiiii1 % o0o00Oo0O * ii1ii11IIIiiI
elif O0OOO0OOooo00 == 222 :
 I1iI1i ( Ii1I1Ii )
 if 29 - 29: Ii1I % Ii1I % ii1ii11IIIiiI + I11i1ii1 % iI11I1II1I1I
elif O0OOO0OOooo00 == 2222222 :
 OOOOo0o00OO0000 ( Ii1I1Ii )
 if 41 - 41: Ii1I % iiiiiiii1
elif O0OOO0OOooo00 == 222222 :
 iIIi ( Ii1I1Ii , I1111i )
 if 37 - 37: I1ii11iIi11i . oOo0O0Ooo % OOooOOo . oO0o - I1ii11iIi11i / oO0o
elif O0OOO0OOooo00 == 333 :
 oO0OOOo0OO ( Ii1I1Ii )
 if 34 - 34: Ii + oO0o + Ii . I1111IIi % o0o00Oo0O
 if 64 - 64: I11i . iI11I1II1I1I
elif O0OOO0OOooo00 == 1020 :
 Oo0oOOo00o ( )
 if 86 - 86: I11i1ii1 - ooOOOoO . iI11I1II1I1I - iI11I1II1I1I
elif O0OOO0OOooo00 == 1021 :
 ANIMEEP ( )
 if 61 - 61: ii1ii11IIIiiI % I1ii11iIi11i + OOooOOo
elif O0OOO0OOooo00 == 1022 :
 ANIMEPLAY ( Ii1I1Ii )
 if 60 - 60: o000O0o . ii
elif O0OOO0OOooo00 == 1001 :
 o0OoOO0 ( )
 if 40 - 40: ooOOOoO
elif O0OOO0OOooo00 == 1005 :
 IIIi1Iiii1I1 ( )
 if 44 - 44: I11i1ii1
elif O0OOO0OOooo00 == 1007 :
 iI1iiII1iii111 ( Ii1I1Ii )
 if 35 - 35: IIiIiII11i + O0OOOoOoo0 / Ii1I * oOo0O0Ooo . ooOOOoO
elif O0OOO0OOooo00 == 1010 :
 i11i ( Ii1I1Ii )
 if 97 - 97: oOo0O0Ooo / I11i
elif O0OOO0OOooo00 == 1011 :
 IIiiiiiiII ( Ii1I1Ii )
 if 13 - 13: Ii1I
elif O0OOO0OOooo00 == 1012 :
 OOO0oo0ooOoo ( Ii1I1Ii )
 if 72 - 72: I1ii11iIi11i + I1111IIi / ii1ii11IIIiiI * I1ii11iIi11i
elif O0OOO0OOooo00 == 1030 :
 o00O00o0O0 ( )
 if 41 - 41: Ii1IIIi1 - OOooOOo . oOo0O0Ooo + Ii + oO0o * O0OOOoOoo0
elif O0OOO0OOooo00 == 1031 :
 Ii1ii1iIi1Ii1 ( Ii1I1Ii , IiI111ii1ii )
 if 85 - 85: oO0o + IIiIiII11i
elif O0OOO0OOooo00 == 1032 :
 I111Iii1 ( Ii1I1Ii )
 if 87 - 87: oO0o
elif O0OOO0OOooo00 == 1006 :
 Parse . ParseURL ( Ii1I1Ii )
 if 93 - 93: ii
elif O0OOO0OOooo00 == 2030 :
 Parse . addonParseURL ( Ii1I1Ii )
 if 80 - 80: I11i
elif O0OOO0OOooo00 == 2031 :
 Parse . apkParseURL ( Ii1I1Ii )
 if 3 - 3: Ii / Ii1IIIi1 + o000O0o
elif O0OOO0OOooo00 == 2032 :
 Parse . ParseBOSS ( Ii1I1Ii )
 if 10 - 10: oO0o . oO0o + o0o00Oo0O
elif O0OOO0OOooo00 == 1002 :
 OOO0OOo0OoO ( Ii1I1Ii )
 if 13 - 13: ooOoO0O00 . oOo0O0Ooo
elif O0OOO0OOooo00 == 1003 :
 oO00OOO ( Ii1I1Ii , IiI111ii1ii )
 if 45 - 45: I11i1ii1 % ooOOOoO
elif O0OOO0OOooo00 == 1004 :
 Iiiii1I1ii1 ( Ii1I1Ii )
 if 37 - 37: O0OOOoOoo0
elif O0OOO0OOooo00 == 1008 :
 iiiIIi11IiI ( )
 if 70 - 70: o0o00Oo0O + iI11I1II1I1I % o0o00Oo0O * I11i - I1ii11iIi11i - I11i1ii1
elif O0OOO0OOooo00 == 1009 :
 O0ooooOO ( Ii1I1Ii )
 if 94 - 94: ooOoO0O00 + I1111IIi / ii - o000O0o / Ii1IIIi1 / OOooOOo
elif O0OOO0OOooo00 == 2001 :
 ooOooo ( )
 if 55 - 55: Ii1IIIi1
elif O0OOO0OOooo00 == 2002 :
 O000o ( Ii1I1Ii )
 if 5 - 5: ooOOOoO / OOooOOo
elif O0OOO0OOooo00 == 1013 :
 oo0o000o0oOO0 ( )
elif O0OOO0OOooo00 == 10111113 :
 I1Ii1i11I1I ( Ii1I1Ii )
 if 48 - 48: ooOoO0O00 - o000O0o . ii - oO0o - ooOoO0O00
elif O0OOO0OOooo00 == 1014 :
 iii ( )
 if 19 - 19: o000O0o % ii1ii11IIIiiI + Ii1I . IIiIiII11i * Ii
elif O0OOO0OOooo00 == 1015 :
 IiiIIiI ( Ii1I1Ii )
 if 87 - 87: ii1ii11IIIiiI / iiiiiiii1 % OOooOOo * Ii1I - ii / OOooOOo
elif O0OOO0OOooo00 == 1016 :
 oo0 ( Ii1I1Ii , IiI111ii1ii , I1111i )
 if 24 - 24: ooOOOoO . Ii1IIIi1 * ooOoO0O00 . Ii1I / I11i1ii1 / o0o00Oo0O
elif O0OOO0OOooo00 == 1017 :
 IIIIi1 ( )
 if 62 - 62: I11i % IIiIiII11i
elif O0OOO0OOooo00 == 1018 :
 I1iI11iIiIi1 ( Ii1I1Ii )
 if 22 - 22: o000O0o - I11i
elif O0OOO0OOooo00 == 1023 :
 I11IIII1111II ( )
 if 89 - 89: Ii1IIIi1
elif O0OOO0OOooo00 == 1024 :
 IiiI11III1i ( Ii1I1Ii )
 if 34 - 34: O0OOOoOoo0 . Ii1IIIi1
elif O0OOO0OOooo00 == 1025 :
 OOo0o0 ( Ii1I1Ii )
 if 13 - 13: oO0o * Ii1IIIi1 + o000O0o
elif O0OOO0OOooo00 == 4001 :
 iiIi11iI1iii ( )
 if 21 - 21: Ii . ii1ii11IIIiiI % ooOoO0O00 * ii1ii11IIIiiI . o000O0o + ii1ii11IIIiiI
elif O0OOO0OOooo00 == 4002 :
 OOOooo ( )
 if 92 - 92: ooOoO0O00 + oO0o * ooOOOoO
elif O0OOO0OOooo00 == 4003 :
 OoO00OooO0 ( )
 if 70 - 70: I1ii11iIi11i
elif O0OOO0OOooo00 == 4004 :
 oooOoOOO0oo0o ( )
 if 93 - 93: O0OOOoOoo0 . Ii1I . I1ii11iIi11i . o000O0o . ii
elif O0OOO0OOooo00 == 4005 :
 iiiI ( )
 if 51 - 51: o0o00Oo0O - O0OOOoOoo0
elif O0OOO0OOooo00 == 4006 :
 OooO0oo ( )
 if 65 - 65: o0o00Oo0O / IIiIiII11i * I1111IIi % ii1ii11IIIiiI + I11i
elif O0OOO0OOooo00 == 4007 :
 i11OOoo ( )
 if 43 - 43: iiiiiiii1 + oO0o * ii
elif O0OOO0OOooo00 == 4008 :
 O0OOo ( )
 if 85 - 85: O0OOOoOoo0 + Ii1IIIi1
elif O0OOO0OOooo00 == 4009 : IiIIII1iiIIi ( )
elif O0OOO0OOooo00 == 4010 : oOOoOooO0oO0o ( )
elif O0OOO0OOooo00 == 3000 :
 o0O00ooo0oO0o ( )
 if 36 - 36: oO0o % IIiIiII11i * o0o00Oo0O + IIiIiII11i - o000O0o - ooOoO0O00
elif O0OOO0OOooo00 == 3001 :
 oo000O0o ( )
 if 53 - 53: ii1ii11IIIiiI - Ii1IIIi1
elif O0OOO0OOooo00 == 3002 :
 o00oOi11III1I1IiI ( Ii1I1Ii )
 if 75 - 75: O0OOOoOoo0 % o0o00Oo0O - ooOOOoO - Ii1I + oOo0O0Ooo - oOo0O0Ooo
elif O0OOO0OOooo00 == 3003 :
 ooooooo0oOo0 ( Ii1I1Ii )
 if 87 - 87: ooOoO0O00 % ii1ii11IIIiiI % ooOoO0O00 + iI11I1II1I1I
elif O0OOO0OOooo00 == 3004 :
 IIII1iI1IiIiI ( Ii1I1Ii )
 if 23 - 23: iI11I1II1I1I * ooOOOoO . iiiiiiii1 - I11i
elif O0OOO0OOooo00 == 404 :
 oOoOOO ( I1111i , Ii1I1Ii , IiI111ii1ii )
 if 66 - 66: oOo0O0Ooo * iiiiiiii1 / Ii / Ii1IIIi1
elif O0OOO0OOooo00 == 405 :
 oOOo0OoooOo ( Ii1I1Ii )
 if 19 - 19: I11i1ii1 % iI11I1II1I1I * ii
elif O0OOO0OOooo00 == 7030 :
 i11IIII ( )
 if 60 - 60: iiiiiiii1 * O0OOOoOoo0 / ii * I1ii11iIi11i
elif O0OOO0OOooo00 == 7021 :
 iiiiiiI ( I1111i )
 if 47 - 47: O0OOOoOoo0 + I11i % iI11I1II1I1I * OOooOOo
elif O0OOO0OOooo00 == 7022 :
 iIiiII11 ( I1111i )
 if 65 - 65: Ii1IIIi1 . IIiIiII11i * Ii + Ii1IIIi1
elif O0OOO0OOooo00 == 7000 :
 iIiiIi11iiI1 ( I1111i , Ii1I1Ii , img )
 if 99 - 99: Ii1I % I1ii11iIi11i
elif O0OOO0OOooo00 == 7050 :
 OOO000OOo0o0O ( Ii1I1Ii )
 if 31 - 31: I11i - IIiIiII11i * Ii1IIIi1 . Ii1IIIi1 - o000O0o
elif O0OOO0OOooo00 == 7051 :
 IIIi1Iii11I ( Ii1I1Ii )
 if 57 - 57: Ii1IIIi1 / Ii / iiiiiiii1 - I1ii11iIi11i . iI11I1II1I1I
elif O0OOO0OOooo00 == 7052 :
 I1II1IIiI11 ( Ii1I1Ii )
 if 84 - 84: I1111IIi
elif O0OOO0OOooo00 == 7053 :
 IIIii ( Ii1I1Ii )
 if 42 - 42: o0o00Oo0O . iiiiiiii1 / ooOOOoO
elif O0OOO0OOooo00 == 7054 :
 CoolPlay ( Ii1I1Ii )
 if 69 - 69: OOooOOo / iiiiiiii1 * oOo0O0Ooo
elif O0OOO0OOooo00 == 7060 :
 i11Ii1iiiI1I ( )
 if 76 - 76: o0o00Oo0O + IIiIiII11i * oO0o
elif O0OOO0OOooo00 == 7061 :
 Iii1iiIi1II ( Ii1I1Ii )
 if 1 - 1: I11i
elif O0OOO0OOooo00 == 7063 :
 II1iiI11I ( Ii1I1Ii )
 if 34 - 34: I11i + Ii1IIIi1 . oO0o + oOo0O0Ooo + ii
elif O0OOO0OOooo00 == 7062 :
 iiiOO00 ( Ii1I1Ii )
 if 90 - 90: ii1ii11IIIiiI / OOooOOo - iI11I1II1I1I / ooOoO0O00 * iiiiiiii1 - I11i1ii1
elif O0OOO0OOooo00 == 7064 :
 NATatozcat ( )
 if 2 - 2: O0OOOoOoo0 * ooOOOoO * I11i1ii1 + Ii + o000O0o
elif O0OOO0OOooo00 == 7067 :
 iI1iII1o0 ( Ii1I1Ii )
 if 81 - 81: I11i * oO0o
elif O0OOO0OOooo00 == 7066 :
 NATatozA ( Ii1I1Ii )
 if 18 - 18: Ii / I11i - o000O0o . ooOOOoO * ooOoO0O00
elif O0OOO0OOooo00 == 7065 :
 iiI11 ( Ii1I1Ii )
 if 67 - 67: ii1ii11IIIiiI
elif O0OOO0OOooo00 == 7070 :
 I1i11IIiiIiI ( )
 if 64 - 64: OOooOOo + O0OOOoOoo0 * OOooOOo - oOo0O0Ooo * ii
elif O0OOO0OOooo00 == 7071 :
 DIZIlist ( Ii1I1Ii )
 if 27 - 27: IIiIiII11i + Ii
elif O0OOO0OOooo00 == 7072 :
 DIZIpull ( Ii1I1Ii )
 if 32 - 32: ooOoO0O00
elif O0OOO0OOooo00 == 7073 :
 WATCHDIZI ( Ii1I1Ii )
 if 76 - 76: IIiIiII11i % I11i1ii1 - Ii1I
elif O0OOO0OOooo00 == 7002 :
 o0i111I ( )
 if 50 - 50: IIiIiII11i / oOo0O0Ooo . ii1ii11IIIiiI % Ii
elif O0OOO0OOooo00 == 7003 :
 Iii1I1i1i1 ( Ii1I1Ii )
 if 66 - 66: o000O0o / Ii1IIIi1 / O0OOOoOoo0
elif O0OOO0OOooo00 == 7004 :
 oooooOO0 ( Ii1I1Ii )
 if 5 - 5: iiiiiiii1 . o000O0o
elif O0OOO0OOooo00 == 7020 :
 oO000O00 ( Ii1I1Ii )
 if 77 - 77: O0OOOoOoo0 / Ii
elif O0OOO0OOooo00 == 7001 :
 iiI11i1II ( )
 if 20 - 20: o0o00Oo0O . ooOOOoO
elif O0OOO0OOooo00 == 7010 :
 II1II1ii1Ii ( Ii1I1Ii )
 if 67 - 67: OOooOOo - I11i1ii1 - iI11I1II1I1I
elif O0OOO0OOooo00 == 7011 :
 OoOO0Ooo ( Ii1I1Ii )
 if 31 - 31: IIiIiII11i + I11i * Ii . I11i
elif O0OOO0OOooo00 == 7012 :
 I1I ( Ii1I1Ii )
 if 73 - 73: o000O0o / Ii1IIIi1 * IIiIiII11i % ii - ooOoO0O00 - I11i1ii1
elif O0OOO0OOooo00 == 7013 :
 cnfTVPlay2 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( Ii1I1Ii )
elif O0OOO0OOooo00 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( Ii1I1Ii )
elif O0OOO0OOooo00 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1111i , Ii1I1Ii , IiI111ii1ii )
elif O0OOO0OOooo00 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif O0OOO0OOooo00 == 7018 :
 iiiI1I11i1I ( )
elif O0OOO0OOooo00 == 7019 :
 CNF_Studio_Indexer . List_Movies ( Ii1I1Ii )
elif O0OOO0OOooo00 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( Ii1I1Ii )
elif O0OOO0OOooo00 == 7024 :
 CNF_Studio_Indexer . Box_Office ( Ii1I1Ii )
 if 43 - 43: I11i + ii1ii11IIIiiI % oO0o . iiiiiiii1 + ooOoO0O00
elif O0OOO0OOooo00 == 8000 :
 OO0O0OOoOo ( )
elif O0OOO0OOooo00 == 8001 :
 OOOooOO0oO ( )
elif O0OOO0OOooo00 == 8002 :
 IIIiI1iOoo00o0O00Oo ( )
elif O0OOO0OOooo00 == 8003 :
 oOo0000oo ( )
elif O0OOO0OOooo00 == 8004 :
 O0o0 ( )
elif O0OOO0OOooo00 == 8005 :
 iiiIIIIiI1iiI ( )
elif O0OOO0OOooo00 == 8006 :
 O00oO0oOOOOOO ( I1111i , Ii1I1Ii )
elif O0OOO0OOooo00 == 8030 :
 i11Ii1IiIIIi ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8045 :
 oo0o0ooOoo00O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8046 :
 iI1ii1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8047 :
 OOooooO0 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8048 :
 ii1I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8049 :
 O0oo00o000 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 804900 :
 II1111iiI1II ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8020 :
 IiIi1I1ii111 ( )
elif O0OOO0OOooo00 == 8021 :
 IIiIii1iiI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8022 :
 o0oOOOOOO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8023 :
 IIIIII11iIiI1III ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8040 :
 O0Oo000 ( )
elif O0OOO0OOooo00 == 8041 :
 OOOoO00oo0ooOo0 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8042 :
 I1iiiiI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8043 :
 yt . PlayVideo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8044 :
 o0oOOO0 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8060 :
 iI1I ( )
elif O0OOO0OOooo00 == 8061 :
 Iii1iiIIi1i111i ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8064 :
 IIIII1 ( )
elif O0OOO0OOooo00 == 8065 :
 i1iI1Ii1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8070 :
 o0OO00oO00 ( )
elif O0OOO0OOooo00 == 8071 :
 OOo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 7080 :
 ooIII ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8090 :
 oo000O ( )
elif O0OOO0OOooo00 == 8091 :
 iii1II11II1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8092 :
 o0o0OoOo00oOoo0oO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8093 :
 I11i1Iii1I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8081 :
 iI1IiiII1 ( )
elif O0OOO0OOooo00 == 8062 :
 i1IO0OoO0o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8063 :
 i111Iii11i1Ii ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8050 :
 IiI ( )
elif O0OOO0OOooo00 == 8051 :
 ii11I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8052 :
 Ooo0O00 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8085 :
 OoO0000O ( )
elif O0OOO0OOooo00 == 8086 :
 Oo0O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8087 :
 o0Oo0o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 8088 :
 i1iioO0oOo ( Ii1I1Ii , I1111i )
elif O0OOO0OOooo00 == 9000 :
 o0OOOOOo00 ( )
elif O0OOO0OOooo00 == 1111 :
 O0o0O00o0o ( )
elif O0OOO0OOooo00 == 9001 :
 Oo0oooO0oO ( )
elif O0OOO0OOooo00 == 9002 :
 I1ii1 ( )
elif O0OOO0OOooo00 == 9003 :
 oOOO ( )
elif O0OOO0OOooo00 == 9004 :
 World1 ( )
elif O0OOO0OOooo00 == 9005 :
 World2 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9006 :
 World3 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9007 :
 iiii1iI1IIiIi ( )
elif O0OOO0OOooo00 == 9008 :
 i1Iii1I11ii ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9009 :
 oOoO000OOoo0 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9010 :
 iIiI1I1IIi1 ( )
elif O0OOO0OOooo00 == 9011 :
 oooOOOoO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 50 :
 o0OoOoo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9020 :
 champlist ( )
elif O0OOO0OOooo00 == 9021 :
 i1I1I1 ( )
elif O0OOO0OOooo00 == 9022 :
 i11iI1111i ( )
elif O0OOO0OOooo00 == 9023 :
 IIIi11 ( )
elif O0OOO0OOooo00 == 9024 :
 o0OO0OOoo0oO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9030 :
 oo00o0000 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9031 :
 OOo00O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9032 :
 i1iI1iIIiIi1I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9033 :
 I11iIiIII11 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 9034 :
 OO0O0OOo0O ( )
elif O0OOO0OOooo00 == 7085 :
 o0O0o0O0O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 7086 :
 IiIi1IiIII1iI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 7087 :
 o00ooO0 ( oOOOO )
elif O0OOO0OOooo00 == 9666 :
 I1iIIiiIIi1i ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10100 : II1111II ( )
elif O0OOO0OOooo00 == 101001 : I1ii11I1IiI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10105 : I1IIi ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10106 : O00O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10104 : o00OooooOOOO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10107 : i1IIIii ( )
elif O0OOO0OOooo00 == 10103 : IiIIiIiIIiI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10108 : Iii1II1iI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10000 : Origin_Menu ( )
elif O0OOO0OOooo00 == 10001 : OOOO0oooo ( )
elif O0OOO0OOooo00 == 10002 : iIiIiIiI ( )
elif O0OOO0OOooo00 == 10003 : IiIII1 ( )
elif O0OOO0OOooo00 == 10004 : O0o0O0OO00o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10005 : iIIIiIii ( )
elif O0OOO0OOooo00 == 10006 : ooo000o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10007 : ii1111Iii11i ( Ii1I1Ii , IiI111ii1ii )
elif O0OOO0OOooo00 == 10008 : OO00OO ( )
elif O0OOO0OOooo00 == 10009 : oo0O0000oo0o0 ( )
elif O0OOO0OOooo00 == 10010 : IiIIIiII1111 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10011 : I1ii11IiI1I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10012 : OOOOo0o00OO0000 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10113 : GRABG ( Ii1I1Ii , I1111i )
elif O0OOO0OOooo00 == 10109 : i1IiIII ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10013 : O0ooO0O00oo0 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10014 : i1i11ii1 ( )
elif O0OOO0OOooo00 == 10015 : IIiIi ( )
elif O0OOO0OOooo00 == 10016 : i111I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10017 : IIIiiiiI1 ( )
elif O0OOO0OOooo00 == 10018 : OOO00000O ( )
elif O0OOO0OOooo00 == 10019 : O0oOoo00Oo0O ( )
elif O0OOO0OOooo00 == 10020 : iIIiII1i1ii ( )
elif O0OOO0OOooo00 == 10021 : IIII1I1 ( )
elif O0OOO0OOooo00 == 10022 : o0oo0o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10023 : OOI1III1I11I1 ( I1111i , Ii1I1Ii )
elif O0OOO0OOooo00 == 10024 : i1III ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10025 : Oo0OO0000oooo ( )
elif O0OOO0OOooo00 == 10026 : I1I11 ( )
elif O0OOO0OOooo00 == 10027 : I1iII ( )
elif O0OOO0OOooo00 == 10028 : iII ( )
elif O0OOO0OOooo00 == 10029 : IIiII ( )
elif O0OOO0OOooo00 == 423 : Ooi1IIii1i ( Ii1I1Ii )
elif O0OOO0OOooo00 == 426 : O00OO00OOOoO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10030 : Izle_Films ( )
elif O0OOO0OOooo00 == 10031 : Latest_Izle_Movies ( )
elif O0OOO0OOooo00 == 10032 : Izle_Genres ( )
elif O0OOO0OOooo00 == 10033 : Izle_Pop_Movies ( )
elif O0OOO0OOooo00 == 10034 : Izle_Boxsets ( )
elif O0OOO0OOooo00 == 10035 : Izle_Search ( )
elif O0OOO0OOooo00 == 10036 : Izle_Genres_Movie ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10037 : Izle_Boxset_single ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10038 : Izle_IFRAME ( )
elif O0OOO0OOooo00 == 10039 : Izle_Boxsets_Next ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10040 : Oo0o0000OOoO ( )
elif O0OOO0OOooo00 == 10041 : OoO0ooOOoo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10042 : OOo0Oo0O00O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10043 : I1iIi1IiI1i ( )
elif O0OOO0OOooo00 == 10044 : IIiIi1II1IiI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10045 : IiIi1I11 ( I1111i )
elif O0OOO0OOooo00 == 10046 : I1iO00O000oOO0oO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10047 : O00oOo0o0 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10048 : oo0OoOO000O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10049 : iI1111iiI1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10050 : OOI1iI1ii1II ( )
elif O0OOO0OOooo00 == 10051 : o0o0O0oOOoO0 ( )
elif O0OOO0OOooo00 == 10052 : I11iIIIIiiI ( )
elif O0OOO0OOooo00 == 10053 : Addon ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10054 : O0OO ( Ii1I1Ii , I1111i )
elif O0OOO0OOooo00 == 10055 :
 iIII1I1i ( "addFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 III1iI1Ii11Ii ( I1111i , Ii1I1Ii , IiI111ii1ii , o0ooooO0o0O , O000o0oO0o )
elif O0OOO0OOooo00 == 10056 :
 iIII1I1i ( "rmFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0Oo ( I1111i )
elif O0OOO0OOooo00 == 10057 :
 iIII1I1i ( "getFavorites" )
 o0I1IiiiiI1i1I ( )
elif O0OOO0OOooo00 == 10058 : i1I1IiI1ii ( )
elif O0OOO0OOooo00 == 10059 : Donators_Guide ( )
elif O0OOO0OOooo00 == 10060 : oo000o0000oO ( )
elif O0OOO0OOooo00 == 10061 : iI1iiIi1 ( )
elif O0OOO0OOooo00 == 10062 : IIiiI ( I1111i , Ii1I1Ii , oOOOO )
elif O0OOO0OOooo00 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
elif O0OOO0OOooo00 == 10064 : iiIIIiI1Ii ( )
elif O0OOO0OOooo00 == 10065 : I1iIiiiI1OOO0O00Oo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10066 : III1III11II ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10068 : ii1II ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10069 : iIi1Ii1i1iI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10070 : iiiI1i1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10071 : Genie_Watch ( )
elif O0OOO0OOooo00 == 10072 : OooOooO0O0o0 ( )
elif O0OOO0OOooo00 == 10073 : i1iIi1IIiIII1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10074 : o0o0 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10075 : ii1iII1iI111 ( IiI111ii1ii , I1111i , Ii1I1Ii )
elif O0OOO0OOooo00 == 10076 : OOo000OO000 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10077 : IiIIiii1I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10078 : i111Iii ( )
elif O0OOO0OOooo00 == 10079 : Genie_Watch_Tv_Shows ( )
elif O0OOO0OOooo00 == 10080 : Genie_Watch_Tv_Genre ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10081 : Genie_Watch_TV_PlayRun ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10082 : Genie_Watch_TV_Episodes ( Ii1I1Ii , IiI111ii1ii )
elif O0OOO0OOooo00 == 10083 : Genie_Watch_Tv_Recent ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10084 : OoOo ( )
elif O0OOO0OOooo00 == 10085 : Iiii1i1 ( )
elif O0OOO0OOooo00 == 10086 : i1IiiiI1iI ( )
elif O0OOO0OOooo00 == 20000 : oooooOo0 ( )
elif O0OOO0OOooo00 == 20001 : i111IIIIiI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 20002 : OOoOoooOOO0 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 20003 : IIii1Ii1i1ii1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 20004 : oO0OO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 20005 : oOO0Oo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 21004 : ooo ( )
elif O0OOO0OOooo00 == 21005 : ii111I1i1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 21006 : iII1I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 21007 : o0OOoOooO0ooO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30000 : II1IIiiI1 ( )
elif O0OOO0OOooo00 == 30001 : II1iiiiI1 ( )
elif O0OOO0OOooo00 == 100121 : Resolve ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30003 : oOOooO ( )
elif O0OOO0OOooo00 == 30004 : o0oO00OOo0oO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30005 : II1Ooo0000o00OO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30006 : i111I1OOOo0Oo0O ( )
elif O0OOO0OOooo00 == 30007 : ooOOoOOooO ( )
elif O0OOO0OOooo00 == 30008 : Oo0 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30009 : oOOoO0O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30010 : ooOi11iii1Ii1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30011 : o0o00OoOo0 ( )
elif O0OOO0OOooo00 == 30012 : OO0Oo00OO0oo ( )
elif O0OOO0OOooo00 == 30013 : Oo0oo ( )
elif O0OOO0OOooo00 == 30014 : I1iO0o0O0OooOoo ( )
elif O0OOO0OOooo00 == 30015 : OoO0o0OO ( Ii1I1Ii , IiI111ii1ii , o0ooooO0o0O )
elif O0OOO0OOooo00 == 30016 : iIi11iI1i ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30019 : o0oOO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30017 : o0oooOo0oo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30018 : Ii11I1I11II ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30030 : IiiiI11 ( )
elif O0OOO0OOooo00 == 30031 : Ii11III ( )
elif O0OOO0OOooo00 == 30032 : iIIiiiI ( )
elif O0OOO0OOooo00 == 30033 : OoooOOo0oOO ( )
elif O0OOO0OOooo00 == 30034 : i1iiIIiiiI ( )
elif O0OOO0OOooo00 == 30035 : I1I1Ii ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30036 : iI1IIII1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30037 : Oo0o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 30038 : O0oIi1iIiIi1I11 ( )
elif O0OOO0OOooo00 == 30039 : Ii1I1i ( )
elif O0OOO0OOooo00 == 50000 : oOOo0O00o ( )
elif O0OOO0OOooo00 == 50001 : iiiiI11iiIIi ( )
elif O0OOO0OOooo00 == 50002 : o0OoOOoooooOO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 50003 : O0OOoooO ( oOOOO )
elif O0OOO0OOooo00 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif O0OOO0OOooo00 == 60001 : ooiiI1ii ( )
elif O0OOO0OOooo00 == 60002 : OoooOo ( I1111i )
elif O0OOO0OOooo00 == 60003 : I1IiII1I1i1I1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 60004 : i1ii1IIIII ( Ii1I1Ii )
elif O0OOO0OOooo00 == 50004 : iiIiIIIiiI ( )
elif O0OOO0OOooo00 == 50005 : speedtest . runtest ( Ii1I1Ii )
elif O0OOO0OOooo00 == 70001 : o00OOo ( )
elif O0OOO0OOooo00 == 70002 : ooO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 70003 : OoOoO0oO00O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 70004 : ooo0O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 70005 : Ii1iiIIi1i ( Ii1I1Ii )
elif O0OOO0OOooo00 == 70006 : iIiiiI1I ( )
elif O0OOO0OOooo00 == 50006 : OO0O000 ( i1 , i1111 )
elif O0OOO0OOooo00 == 80000 : OOOO00o000o ( )
elif O0OOO0OOooo00 == 80001 : resolvefilmon ( Ii1I1Ii )
elif O0OOO0OOooo00 == 80002 : iIi ( )
elif O0OOO0OOooo00 == 80003 : i1Ii1I1Ii11iI ( I1111i , Ii1I1Ii , "None" )
elif O0OOO0OOooo00 == 80004 : OoO000oo000o0 ( I1111i , Ii1I1Ii )
elif O0OOO0OOooo00 == 80005 : OO0O00oOo ( )
elif O0OOO0OOooo00 == 80006 : I1IiI1iIiIiii ( Ii1I1Ii )
elif O0OOO0OOooo00 == 80007 : I1iiI1II ( Ii1I1Ii )
elif O0OOO0OOooo00 == 80008 : IIIi ( )
elif O0OOO0OOooo00 == 80009 : o00000Oo ( )
elif O0OOO0OOooo00 == 80010 : OoOoooOO00OO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 80011 : i11iII1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 80012 : i11iI1111ii1I ( )
elif O0OOO0OOooo00 == 90000 : ii1IIi1IIIIi1 ( I1111i , Ii1I1Ii )
elif O0OOO0OOooo00 == 90001 : II11 ( )
elif O0OOO0OOooo00 == 90002 : I1iiiiIii ( )
elif O0OOO0OOooo00 == 90003 : IIiiiiiI1iIi ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90004 : IIIII11II1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90005 : OOOO0oOO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90006 : ooo0ooO00o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90007 : o0OOii ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90008 : O0ooOo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90009 : i11iiiI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90010 : iiIiI1i1 ( )
elif O0OOO0OOooo00 == 90020 : i11ii ( )
elif O0OOO0OOooo00 == 90021 : hellyeah2 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90022 : hellyeah3 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90023 : i1IiiI1iIi ( )
elif O0OOO0OOooo00 == 90024 : i11I1I1iiI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90025 : ooi1II1I ( Ii1I1Ii )
if 85 - 85: I1ii11iIi11i % Ii1I / Ii1IIIi1
elif O0OOO0OOooo00 == 90030 : I11iII ( )
elif O0OOO0OOooo00 == 90031 : I1i1i1iii ( )
elif O0OOO0OOooo00 == 90032 : iIIii ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90033 : ii1iii1i ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90034 : ooO0O00Oo0o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90035 : I1i ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90036 : Ooo00O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90039 : oOo0OO00O0O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90037 : o0OO0O0Oo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90038 : iiiI1ii11 ( )
if 65 - 65: I11i1ii1 + I1111IIi - OOooOOo % IIiIiII11i - iI11I1II1I1I
elif O0OOO0OOooo00 == 10090 : O00 ( )
elif O0OOO0OOooo00 == 10091 : ii1iI11IiIIi ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10092 : iiiiIi11II11 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10093 : iiii ( Ii1I1Ii , IiI111ii1ii )
elif O0OOO0OOooo00 == 10094 : oO0OOo ( Ii1I1Ii , IiI111ii1ii )
if 39 - 39: oOo0O0Ooo + Ii1I - Ii
elif O0OOO0OOooo00 == 10095 : IiIiIi ( )
elif O0OOO0OOooo00 == 10096 : ooOoOO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10097 : iIiIIi ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10098 : I1iIiI1IiIIII ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10099 : OOOOoo ( Ii1I1Ii )
if 43 - 43: iI11I1II1I1I
elif O0OOO0OOooo00 == 10200 : IiIiII1 ( )
elif O0OOO0OOooo00 == 10201 : iIii ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10202 : I11I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 10203 : RT4 ( Ii1I1Ii )
if 73 - 73: OOooOOo + I11i
elif O0OOO0OOooo00 == 90040 : IiiIiIi111iI1 ( )
elif O0OOO0OOooo00 == 90041 : oOo00o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90042 : iIii1I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90043 : i1i1Ii11Ii ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90044 : IIiI1Ii1IIiI11i1 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90045 : ii11iIIi ( )
elif O0OOO0OOooo00 == 90046 : Ii11I1iIiiI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90050 : I1iiIiI1iI1I ( )
elif O0OOO0OOooo00 == 90051 : i1II1i ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90052 : iI1IiiiIiI1Ii ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90053 : ooOO00o00 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90054 : o00iI1i1II ( Ii1I1Ii )
elif O0OOO0OOooo00 == 90055 : Ii1I1I1i11ii ( )
if 58 - 58: ooOoO0O00 * Ii1I % O0OOOoOoo0 . oO0o % I1111IIi % ooOOOoO
elif O0OOO0OOooo00 == 100001 : Stand_up ( )
if 63 - 63: Ii1I % I11i1ii1 % Ii1I
elif O0OOO0OOooo00 == 100003 : i111I ( Ii1I1Ii )
elif O0OOO0OOooo00 == 100004 : o00oO ( Ii1I1Ii )
elif O0OOO0OOooo00 == 100005 : Resolve ( Ii1I1Ii )
elif O0OOO0OOooo00 == 100008 : Search ( )
elif O0OOO0OOooo00 == 100007 : ii111I11iI ( Ii1I1Ii )
elif O0OOO0OOooo00 == 100009 : yt . PlayVideo ( Ii1I1Ii )
elif O0OOO0OOooo00 == 100010 : i1iiIiI1Ii1i ( Ii1I1Ii )
elif O0OOO0OOooo00 == 100100 : OOoO000 ( IiI111ii1ii , Ii1I1Ii , IIiiIi1i11i )
elif O0OOO0OOooo00 == 100101 : iIi1II ( Ii1I1Ii , I1111i , o0ooooO0o0O , IIiiIi1i11i , IiI111ii1ii )
elif O0OOO0OOooo00 == 100102 : Oo00oo0000OO ( I1111i , Ii1I1Ii , IiI111ii1ii , o0ooooO0o0O )
elif O0OOO0OOooo00 == 100106 : O00oooo00o0O ( Ii1I1Ii , I1111i )
elif O0OOO0OOooo00 == 100107 : II1II1iIIi11 ( )
elif O0OOO0OOooo00 == 100108 : iiiiIooo0O0O0OO ( )
elif O0OOO0OOooo00 == 100109 : o00OOOO000000 ( Ii1I1Ii )
elif O0OOO0OOooo00 == 40000 : o00iIiiiII ( )
elif O0OOO0OOooo00 == 40001 : OoOooOO0oOOo0O ( Ii1I1Ii )
elif O0OOO0OOooo00 == 100110 : I11I1i1iI ( )
elif O0OOO0OOooo00 == 100111 : O00oO0O0oO00o ( Ii1I1Ii )
elif O0OOO0OOooo00 == 100110 : I11I1i1iI ( )
elif O0OOO0OOooo00 == 100210 : i1iII1II11I ( Ii1I1Ii )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
