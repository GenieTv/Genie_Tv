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
IiiIII111iI = "3.3.9"
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
IIiiiiiiIi1I1 = base64 . decodestring ( 'LnBocA==' )
I1IIIii = base64 . decodestring ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC8=' )
oOoOooOo0o0 = [ ]
OOOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/ResetDatabase.py' ) )
OOO00 = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/imports/tvGuide/addon.py' ) )
iiiiiIIii = oo00 . getLocalizedString
O000OO0 = CookieJar ( )
I11iii1Ii = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( O000OO0 ) )
I11iii1Ii . addheaders = [ ( 'User-Agent' , 'Mozilla/5.0' ) ]
I1IIiiIiii = int ( sys . argv [ 1 ] )
O000oo0O = xbmc . translatePath ( oo00 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
OOOOi11i1 = os . path . join ( I11i1 , 'favorites' )
IIIii1II1II = I11i1 + '/addons.ini'
oOo0oooo00o = xbmc . translatePath ( 'special://home/userdata/' )
i1I1iI = xbmc . translatePath ( 'special://home/userdatabroke/' )
oo0OooOOo0 = xbmc . translatePath ( 'special://home/addons/plugin.video.GenieTv' )
o0O = xbmc . translatePath ( 'special://home/userdata/addon_data' )
O00oO = o0O + 'GenieTvWatched'
I11i1I1I = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllcy5hYw==' ) )
oO0Oo = [ 'daclips' , 'filehoot' , 'allmyvideos' , 'vidspot' , 'vodlocker' , 'vidto' ]
if not os . path . exists ( O00oO ) :
 os . makedirs ( O00oO )
oOOoo0Oo = O00oO + 'watched.txt'
if not os . path . exists ( oOOoo0Oo ) :
 open ( oOOoo0Oo , 'w+' )
o00OO00OoO = open ( oOOoo0Oo ) . read ( )
OOOO0OOoO0O0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9QYW5zQm94L09SSUdJTlMv' ) )
O0Oo000ooO00 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.ivueguide/master.db' ) )
oO0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , 'favourites.xml' ) )
Ii1iIiII1ii1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/plugin.video.GenieTv/favorites' ) )
ooOooo000oOO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/addon.xml' ) )
Oo0oOOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/repository.GenieTv/addon.xml' ) )
if os . path . exists ( OOOOi11i1 ) == True :
 Oo0OoO00oOO0o = open ( OOOOi11i1 ) . read ( )
else : Oo0OoO00oOO0o = [ ]
OOO00O = oo00 . getSetting ( 'debug' )
if os . path . exists ( I11i1 ) == False :
 os . makedirs ( I11i1 )
def OOoOO0oo0ooO ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00O0oOO00O00 = ''
 i1Oo00 = ''
 try :
  O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
  i1Oo00 = O00O0oOO00O00 . read ( )
  O00O0oOO00O00 . close ( )
 except : pass
 if i1Oo00 != '' :
  return i1Oo00
 else :
  i1Oo00 = 'Failed'
  return i1Oo00
  if 31 - 31: oo0oO00 . IIi * iiII11i1I1IIi
IIIIi1i = [ ]
I1 = OOoOO0oo0ooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if I1 != 'Failed' :
 IIIIi1i . append ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby8=' ) )
if not I1 != 'Failed' :
 iii1i1iiiiIi = OOoOO0oo0ooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if iii1i1iiiiIi != 'Failed' :
  IIIIi1i . append ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20v' ) )
 if not iii1i1iiiiIi != 'Failed' :
  Iiii = OOoOO0oo0ooO ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if Iiii != 'Failed' :
   IIIIi1i . append ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vaGVyb3Zpc2lvbi54MTBob3N0LmNvbS9HZW5pZVR2L3JlZG8v' ) )
  if not Iiii != 'Failed' :
   OO0OoO0o00 = OOoOO0oo0ooO ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
   if OO0OoO0o00 != 'Failed' :
    IIIIi1i . append ( i11 ( 'aHR0cDovLzUuMTM1LjEuNDYvcmVkby8=' ) )
else :
 pass
ooOO0O0ooOooO = ( str ( IIIIi1i ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' )
oOOOo00O00oOo = ooOO0O0ooOooO + 'GenieArt/NEW/'
if 34 - 34: iIi1i1ii1 + OooOO000 % OOoOoo
if 85 - 85: O00OOo00oo0o % IIiIi1iI + oOo0O0Ooo
def IIiiiI1iIII ( ) :
 if not os . path . exists ( iI1Ii11111iIi ) :
  OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will only work with" , 'its official repo please install from trusted source' , '' )
  IIiooOOoooooo = 'genie tv repo not being installed '
  II1I ( )
 else :
  O0 ( )
  if 5 - 5: O00OOo00oo0o
def O0 ( ) :
 if 87 - 87: iiII11i1I1IIi - iI11I1II1I1I + oOo0O0Ooo . OooOO000
 Oo0oOOOoOooOo = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvYmxvYi9tYXN0ZXIvVmVyc2lvbl9Mb2cudHh0' ) )
 IIi1I11I1II = open ( ooOooo000oOO ) . read ( )
 OooOoooOo = open ( Oo0oOOo ) . read ( )
 if 46 - 46: OooOO000
 IIIII11I1IiI = re . compile ( 'version="([^"]*)" provider' ) . findall ( IIi1I11I1II )
 i1I = re . compile ( 'version="([^"]*)" provider-name' ) . findall ( OooOoooOo )
 OoOO = re . compile ( 'GENIE TV ADDON - Version = &quot;(.+?)&quot;' ) . findall ( Oo0oOOOoOooOo )
 ooOOO0 = re . compile ( 'GENIE TV REPO - Version = &quot;(.+?)&quot;' ) . findall ( Oo0oOOOoOooOo )
 for o0o in IIIII11I1IiI :
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
    II1I ( )
   if o0OoOO000ooO0 == iiIi1IIi1I :
    xbmc . sleep ( 100 )
    OO
def o0o0o0oO0oOO ( ) :
 IIiiiI1iIII ( )
 ii1Ii11I ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  o00o0 ( )
 else :
  if oo00 . getSetting ( 'My Build' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']WIZARD[/COLOR]' , str ( ooOO0O0ooOooO ) , 4001 , oOOOo00O00oOo + 'Wizard.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4002 , oOOOo00O00oOo + 'Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Sports[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Live List[/COLOR]' , '' , 4009 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Music' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']Music[/COLOR]' , str ( ooOO0O0ooOooO ) , 4003 , oOOOo00O00oOo + 'Music.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TOOLS[/COLOR]' , '' , 90001 , oOOOo00O00oOo + 'tools.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']Force Genie Update Kodi 16+[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , oOOOo00O00oOo + 'GenieUpdate.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']CONTACT US[/COLOR]' , '' , 50006 , oOOOo00O00oOo + 'Contact-Us.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , oOOOo00O00oOo + 'settings.png' , O0o0Oo , '' )
  if I1IIII1i ( ) == 'android' :
   iiOOooooO0Oo ( '[COLOR' + II + ']APK TOOL[/COLOR]' , str ( ooOO0O0ooOooO ) , 30039 , oOOOo00O00oOo + 'APKTools.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']BUILDERS TOOLBOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 32 , oOOOo00O00oOo + 'BuildersToolbox.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   OOiIiIIi1 ( '[COLOR' + II + ']SOURCE LIST[/COLOR]' , str ( ooOO0O0ooOooO ) , 46 , oOOOo00O00oOo + 'SoruceList.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']MAINTENANCE[/COLOR]' , str ( ooOO0O0ooOooO ) , 3 , oOOOo00O00oOo + 'Maintenance.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']ADDONS[/COLOR]' , '' , 10050 , oOOOo00O00oOo + 'Addons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']GenieTv RSS Feed[/COLOR]' , str ( ooOO0O0ooOooO ) , 39 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def o00o0 ( ) :
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']WIZARD[/COLOR]' , str ( ooOO0O0ooOooO ) , 4001 , oOOOo00O00oOo + 'Wizard.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4002 , oOOOo00O00oOo + 'Streams.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Sports[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Live List[/COLOR]' , '' , 4009 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']Music[/COLOR]' , str ( ooOO0O0ooOooO ) , 4003 , oOOOo00O00oOo + 'Music.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']MAINTENANCE[/COLOR]' , str ( ooOO0O0ooOooO ) , 3 , oOOOo00O00oOo + 'Maintenance.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']TOOLS[/COLOR]' , '' , 90001 , oOOOo00O00oOo + 'tools.png' , O0o0Oo , '' )
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
 OOiIiIIi1 ( '[COLOR' + II + ']Todays Games[/COLOR]' , str ( ooOO0O0ooOooO ) , 90030 , oOOOo00O00oOo + 'tgames.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Replays[/COLOR]' , str ( ooOO0O0ooOooO ) , 90031 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , O0o0Oo , '' )
 if 69 - 69: IIiIi1iI
def I11iII ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIIII11I1IiI = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I11iI1i1I11I11 , o000O0O in IIIII11I1IiI :
  OO0O000 ( '[COLOR' + II + ']Tommys List[/COLOR]  ' + I11iI1i1I11I11 , o000O0O )
def I1i1i1iii ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 iIIII = O000oo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIIII11I1IiI = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 90032 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
def iIIii ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , o00O0O , O0o0Oo , '' )
 for url in next :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , oOOOo00O00oOo + 'NEXT.png' , O0o0Oo , '' )
def ii1iii1i ( url ) :
 iIIII = O000oo ( url )
 Iii1I1111ii = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 IIIII11I1IiI = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 for I1111i , url in i1I :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 for I1111i , url in ooOoO00 :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 for url in Iii1I1111ii :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
  if 14 - 14: ooOoO0O00 - I11i % o0o00Oo0O - oO0o
def ooO0O00Oo0o ( url ) :
 if 'drive' in url :
  OOOOo0o00OO0000 ( url )
 else :
  iIIII = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( iIIII )
  for url in IIIII11I1IiI :
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
 if 32 - 32: O00OOo00oo0o
def Iii1 ( url ) :
 if url == 'http://' : return False
 try :
  O0o0O00Oo0o0 = urllib2 . Request ( url )
  O0o0O00Oo0o0 . add_header ( 'User-Agent' , I1i1iiI1 )
  O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
  O00O0oOO00O00 . close ( )
 except Exception , oOOOoo00 :
  return oOOOoo00
 return True
def iiIiIIIiiI ( ) :
 if 12 - 12: o0o00Oo0O - I11i
 if 81 - 81: OOooOOo - OOooOOo . OooOO000
 if 73 - 73: iiII11i1I1IIi % Ii - oOo0O0Ooo
 if 7 - 7: o0o00Oo0O * Ii * iIi1i1ii1 + IIiIi1iI % oO0o - IIiIi1iI
 if 39 - 39: I1ii11iIi11i * IIi % IIi - ii + I11i - iiII11i1I1IIi
 i1Oo00 = O000oo ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( i1Oo00 )
 if len ( IIIII11I1IiI ) > 0 :
  for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O in IIIII11I1IiI :
   OOiIiIIi1 ( I1111i , oO0o0 , 50005 , iiO0oOo00o , o0ooooO0o0O , '' )
def iiIi11iI1iii ( ) :
 IIiiiI1iIII ( )
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
  iiOOooooO0Oo ( '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 10060 , oOOOo00O00oOo + 'BackupMyBuild.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 49 , oOOOo00O00oOo + 'RestoreMyBuild.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']WIPE GENIE[/COLOR]' , str ( ooOO0O0ooOooO ) , 41 , oOOOo00O00oOo + 'WipeGenie.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']WISHES PC[/COLOR]' , str ( ooOO0O0ooOooO ) , 1 , oOOOo00O00oOo + 'WISHESPC.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Genie BUILDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 44 , oOOOo00O00oOo + 'GenieBuilds.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 56 - 56: I11i + IIiIiII11i + OOooOOo - IIiIi1iI . OOooOOo
def OOOooo ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FAVOURITES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10057 , oOOOo00O00oOo + 'Favourites.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 9000 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAM TEAM[/COLOR]' , str ( ooOO0O0ooOooO ) , 4006 , oOOOo00O00oOo + 'StreamTeam.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , oOOOo00O00oOo + 'bamf.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 4004 , oOOOo00O00oOo + 'Movies.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4005 , oOOOo00O00oOo + 'TVShows.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']KIDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4007 , oOOOo00O00oOo + 'Kids.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , O0o0Oo , '' )
  if 94 - 94: ii + I1ii11iIi11i / OOooOOo * IIi
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAM CATEGORIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 90002 , oOOOo00O00oOo + 'cats.png' , O0o0Oo , '' )
  if Ooo == '5knuckleshuffle' :
   iiOOooooO0Oo ( '[COLOR' + II + ']XVID[/COLOR]' , str ( ooOO0O0ooOooO ) , 10100 , oOOOo00O00oOo + 'Jizbox.png' , O0o0Oo , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']ADULT CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30033 , oOOOo00O00oOo + 'adu.png' , O0o0Oo , '' )
 else :
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FAVOURITES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10057 , oOOOo00O00oOo + 'Favourites.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 9000 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAM TEAM[/COLOR]' , str ( ooOO0O0ooOooO ) , 4006 , oOOOo00O00oOo + 'StreamTeam.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , oOOOo00O00oOo + 'bamf.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 4004 , oOOOo00O00oOo + 'Movies.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4005 , oOOOo00O00oOo + 'TVShows.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']KIDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4007 , oOOOo00O00oOo + 'Kids.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cDovL3hyYXk4NDAuc3RhcnRkZWRpY2F0ZWQubmV0L2Jvc3Mv' ) , 2032 , oOOOo00O00oOo + 'boss.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , O0o0Oo , '' )
  if Ooo == '5knuckleshuffle' :
   iiOOooooO0Oo ( '[COLOR' + II + ']XVID[/COLOR]' , str ( ooOO0O0ooOooO ) , 10100 , oOOOo00O00oOo + 'Jizbox.png' , O0o0Oo , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']ADULT CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30033 , oOOOo00O00oOo + 'adu.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' , '' , 9034 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   OOiIiIIi1 ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FOOTBALL[/COLOR]' , '' , 10002 , oOOOo00O00oOo + 'Football.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']NEWS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30032 , oOOOo00O00oOo + 'News.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'GenieTVTutorials.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']HOBBIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 4008 , oOOOo00O00oOo + 'Hobbies.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Stand Up' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']STAND UP[/COLOR]' , '' , 10003 , oOOOo00O00oOo + 'StandUp.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 8040 , oOOOo00O00oOo + 'documentaries.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 7001 , oOOOo00O00oOo + 'DiscloseTV.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']24/7 STREAMS[/COLOR]' , '' , 30030 , oOOOo00O00oOo + '247Streams.png' , O0o0Oo , '' )
  if 69 - 69: IIiIi1iI % oo0oO00
  if 50 - 50: ii % iiII11i1I1IIi
  if 49 - 49: oo0oO00 - Ii . O00OOo00oo0o * iIi1i1ii1 % OooOO000 + ooOoO0O00
  if 71 - 71: I11i
  if 38 - 38: oo0oO00 % OOooOOo + Ii1I . Ii
  if 53 - 53: Ii * OooOO000
  if 68 - 68: iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
  if 38 - 38: IIiIi1iI - IIi / OooOO000
  if 66 - 66: o0o00Oo0O % Ii1I + Ii . OOooOOo / iIi1i1ii1 + Ii1I
  if 86 - 86: I11i
  if 5 - 5: OOoOoo * OOooOOo
  if 5 - 5: O00OOo00oo0o
  if 90 - 90: O00OOo00oo0o . IIiIi1iI / iIi1i1ii1 - iiII11i1I1IIi
  if 40 - 40: ii
  if 25 - 25: OOoOoo + iIi1i1ii1 / IIiIi1iI . I11i % o0o00Oo0O * oO0o
  if 84 - 84: IIiIi1iI % iIi1i1ii1 + Ii
 I1I11i ( 'movies' , 'MAIN' )
def II1I1Ii ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']FOOTBALL[/COLOR]' , '[COLOR' + II + ']KIDS[/COLOR]' , '[COLOR' + II + ']NEWS[/COLOR]' , '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + II + ']HOBBIES[/COLOR]' , '[COLOR' + II + ']STAND UP[/COLOR]' , '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']CATEGORIES[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  Ooo0O0oooo ( )
 if i11I1II1I11i == 1 :
  iiI ( )
 if i11I1II1I11i == 2 :
  oOIIiIi ( )
 if i11I1II1I11i == 3 :
  OOoOooOoOOOoo ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , Iiii1iI1i , I1111i )
 if i11I1II1I11i == 4 :
  I1ii1ii11i1I ( )
 if i11I1II1I11i == 5 :
  o0OoOO ( )
 if i11I1II1I11i == 6 :
  O0O0Oo00 ( )
 if i11I1II1I11i == 7 :
  oOoO00o ( )
 if i11I1II1I11i == 8 :
  oO00O0 ( )
  if 36 - 36: oo0oO00 - iIi1i1ii1 . I1ii11iIi11i - Ii - IIi * I1ii11iIi11i
  if 76 - 76: Ii + I11i / Ii1I - oO0o - iIi1i1ii1 + Ii1I
def ii1Ii11I ( ) :
 if not os . path . exists ( IIIII ) :
  OO0O000 ( 'Change Log 06/12/16 - v3.3.5' , 'NEW SECTIONS ADDED, MOVIE HUB(streams>>stream categories>>movies), Tv HUB(streams>>stream categories>>tv shows), BAMF IPTV revamped, WATCH SERIES revamped, General Maintence' )
  os . makedirs ( IIIII )
  if 51 - 51: iI11I1II1I1I . IIiIi1iI + iI11I1II1I1I
  if 95 - 95: oOo0O0Ooo
def iII1ii1 ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + II + ']MOVIE HUB[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   I1i1iiiI1 ( )
  if i11I1II1I11i == 1 :
   iIIi ( )
  if i11I1II1I11i == 2 :
   oO0o00oo0 ( )
  if i11I1II1I11i == 3 :
   ii1IIII ( oO0o0 )
  if i11I1II1I11i == 4 :
   oO00oOooooo0 ( )
  if i11I1II1I11i == 5 :
   oOo ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if i11I1II1I11i == 6 :
   O0OOooOoO ( )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9001 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10200 , oOOOo00O00oOo + 'rated.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MOVIE HUB[/COLOR]' , '' , 90040 , oOOOo00O00oOo + 'movhub.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']POPCORN BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 7061 , oOOOo00O00oOo + 'PopcornBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Desi Flix[/COLOR]' , '' , 80005 , oOOOo00O00oOo + 'Desi.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , oOOOo00O00oOo + 'FilmTrailers.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOOo00O00oOo + 'ClassicMovies.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def i1II1I1Iii1 ( ) :
 IIiiiI1iIII ( )
 iiI11Iii ( )
 if 78 - 78: OooOO000 + iiII11i1I1IIi . IIiIi1iI - OooOO000 . iIi1i1ii1
 if 30 - 30: oOo0O0Ooo + oO0o % iIi1i1ii1 * OooOO000 / I1ii11iIi11i - iiII11i1I1IIi
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  OOiIiIIi1 ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']Link GTV to Guide[/COLOR]' , '' , 4010 , oOOOo00O00oOo + 'linkchannels.png' , O0o0Oo , '' )
def oO00O0 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']DAILY LISTS[/COLOR]' , '' , 9007 , Oo00OOOOO , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Oo00OOOOO , O0o0Oo , '' )
 if 64 - 64: iI11I1II1I1I
 if 21 - 21: I1ii11iIi11i . IIiIiII11i
 if 54 - 54: IIiIiII11i % IIiIiII11i
 if 86 - 86: o0o00Oo0O % iIi1i1ii1 * IIiIi1iI * iI11I1II1I1I * ooOoO0O00 * iiII11i1I1IIi
 if 83 - 83: OOooOOo % IIiIiII11i - OOooOOo + OOoOoo - o0o00Oo0O
def oO0oo000OOOoO ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']Tv HUB[/COLOR]' , '[COLOR' + II + ']THE SOURCE[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']RETURN DATES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   ii1I ( )
  if i11I1II1I11i == 1 :
   OO0oo0O ( )
  if i11I1II1I11i == 2 :
   Ii1i1iI ( )
  if i11I1II1I11i == 3 :
   IIiI1 ( )
  if i11I1II1I11i == 4 :
   i1iI1 ( )
  if i11I1II1I11i == 5 :
   ii1I1IiiI1ii1i ( )
  if i11I1II1I11i == 6 :
   O0o ( )
  if i11I1II1I11i == 7 :
   oO0OoO00o ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9002 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Tv HUB[/COLOR]' , str ( ooOO0O0ooOooO ) , 90050 , oOOOo00O00oOo + 'Tv HUB.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '' , 10040 , oOOOo00O00oOo + 'WatchSeries.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '' , 8020 , oOOOo00O00oOo + 'iWatchSeries.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RETURN DATES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10095 , oOOOo00O00oOo + 'RD.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 8064 , oOOOo00O00oOo + 'ClassicTV.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , oOOOo00O00oOo + 'TVShowTrailers.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def II1iiiiII ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   O0OoOO0oo0 = '[COLOR' + II + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   oOO = '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   O0o0OO0000ooo = '[COLOR' + II + ']APPRENTICE[/COLOR]'
  i1Oo0oO00o = [ O0OoOO0oo0 , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , O0o0OO0000ooo , '[COLOR' + II + ']RAIZ TV[/COLOR]' , oOO , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   iIIII1iIIii ( )
  if i11I1II1I11i == 1 :
   OOoOooOoOOOoo ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , Iiii1iI1i , I1111i )
   if 52 - 52: I11i % I1ii11iIi11i
  if i11I1II1I11i == 2 :
   OOoOooOoOOOoo ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , Iiii1iI1i , I1111i )
  if i11I1II1I11i == 3 :
   Oo000ooOOO ( )
  if i11I1II1I11i == 4 :
   OOoOooOoOOOoo ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , Iiii1iI1i , I1111i )
  if i11I1II1I11i == 5 :
   Ii11i1I11i ( )
  if i11I1II1I11i == 6 :
   OOoOooOoOOOoo ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , Iiii1iI1i , I1111i )
 else :
  if 13 - 13: OOoOoo / Ii % IIiIiII11i % iiII11i1I1IIi . Ii1I
  if 8 - 8: OOooOOo + I1ii11iIi11i - IIiIiII11i
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']PANDORAS BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 10025 , oOOOo00O00oOo + 'PandorasBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'DojoStreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , oOOOo00O00oOo + 'Roadrunner-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'Technica-Streams.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , '' , 1017 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'raiztv.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 1023 , oOOOo00O00oOo + 'ScoobyStreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'ITVStreams.png' , O0o0Oo , '' )
  if 11 - 11: ooOoO0O00 % Ii - ooOoO0O00 * OOooOOo
 I1I11i ( 'movies' , 'MAIN' )
 if 39 - 39: O00OOo00oo0o
def O0OoO0ooOO0o ( ) :
 IIiiiI1iIII ( )
 OOiIiIIi1 ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
def OoOo0oOooOoOO ( url ) :
 iIIII = oo00ooOoO00 ( url )
 url = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( iIIII )
 for o00oOoOo0 , o0O0O0ooo0oOO in IIIII11I1IiI :
  if '[DIR]' in o00oOoOo0 :
   oo000ii ( ( '[COLOR' + II + ']' + o0O0O0ooo0oOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + o0O0O0ooo0oOO , 1018 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'mkv' in o0O0O0ooo0oOO :
   OoO ( ( '[COLOR' + II + ']' + o0O0O0ooo0oOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + o0O0O0ooo0oOO , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'avi' in o0O0O0ooo0oOO :
   OoO ( ( '[COLOR' + II + ']' + o0O0O0ooo0oOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + o0O0O0ooo0oOO , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
   if 41 - 41: ooOoO0O00 * IIiIiII11i / ii . IIi
def Oo000ooOOO ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , oOOOo00O00oOo + 'scraped.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 if 83 - 83: OooOO000 . o0o00Oo0O / I1ii11iIi11i / IIi - IIiIiII11i
def oO0oO0 ( url ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( I1 )
 for I1111i , url , Ii11iiI , IIi1iiii1iI , o0ooooO0o0O , iIiiii in IIIII11I1IiI :
  if IIi1iiii1iI == '123' :
   IIi1iiii1iI = oOOOo00O00oOo + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = oOOOo00O00oOo + 'appstreams.png'
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100010 , IIi1iiii1iI , o0ooooO0o0O , iIiiii )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , IIi1iiii1iI , o0ooooO0o0O , iIiiii )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , IIi1iiii1iI , o0ooooO0o0O , iIiiii )
  elif not 'http' in url :
   O0000OOO0 ( I1111i , url , 100009 , IIi1iiii1iI , o0ooooO0o0O , iIiiii , '' )
  else :
   O0000OOO0 ( I1111i , url , 100005 , IIi1iiii1iI , o0ooooO0o0O , iIiiii , '' )
   if 51 - 51: oOo0O0Ooo / OOoOoo / iIi1i1ii1
def I111iIi1 ( url ) :
 I1 = i1i1IIIIi1i ( url )
 oo00O00oO000o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for url , o00O0O , iIiiii , o0ooooO0o0O , I1111i in oo00O00oO000o :
  if o00O0O == '123' :
   o00O0O = oOOOo00O00oOo + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = O0o0Oo
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100004 , o00O0O , o0ooooO0o0O , iIiiii )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , o00O0O , o0ooooO0o0O , iIiiii )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , o00O0O , o0ooooO0o0O , iIiiii )
  elif not 'http' in url :
   O0000OOO0 ( I1111i , url , 100009 , o00O0O , o0ooooO0o0O , iIiiii , '' )
  else :
   O0000OOO0 ( I1111i , url , 100005 , o00O0O , o0ooooO0o0O , iIiiii , '' )
   if 71 - 71: Ii1I - IIiIi1iI / OOooOOo * OOooOOo / ooOoO0O00 . ooOoO0O00
def ooo000ooO0000 ( url ) :
 if 97 - 97: I1ii11iIi11i * oOo0O0Ooo . iI11I1II1I1I
 I1 = i1i1IIIIi1i ( url )
 I1Ii1111iIi = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( I1 )
 for I11o0oO00oO0o0o0 in I1Ii1111iIi :
  IIi1iiii1iI = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for IIi1iiii1iI in IIi1iiii1iI :
   IIi1iiii1iI = IIi1iiii1iI
  I1111i = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for I1111i in I1111i :
   if 'elete' in I1111i :
    pass
   elif 'rivate Vid' in I1111i :
    pass
   else :
    I1111i = ( I1111i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  I1I = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for I1I in I1I :
   I1I = I1I
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for url in url :
   url = url
  O0000OOO0 ( '[COLORred]' + str ( I1I ) + '[/COLOR] : ' + str ( I1111i ) , str ( url ) , 100009 , str ( IIi1iiii1iI ) , O0o0Oo , '' , '' )
  I1I11i ( 'movies' , '' )
  if 89 - 89: ooOoO0O00 / IIiIiII11i . iI11I1II1I1I
  if 1 - 1: IIiIi1iI % OOooOOo * I1ii11iIi11i
  if 55 - 55: OOooOOo
  if 87 - 87: ii % OooOO000 . oOo0O0Ooo / IIiIi1iI
  if 8 - 8: iiII11i1I1IIi + I11i
def oOOo0o0oo ( iconimage , url , extra ) :
 IIi1iiii1iI = ' '
 i11iiiiI1i = ' '
 o0ooooO0o0O = ' '
 iIIiii1 = ' '
 iIiIi1I = i1i1IIIIi1i ( url )
 IIi1iiii1iI = re . compile ( '<img src="(.+?)">' ) . findall ( iIiIi1I )
 for IIi1iiii1iI in IIi1iiii1iI :
  IIi1iiii1iI = IIi1iiii1iI
 iiii11i = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( iIiIi1I )
 for o0ooooO0o0O in iiii11i :
  o0ooooO0o0O = o0ooooO0o0O
 IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( iIiIi1I )
 for url , iIIiii1 in IIIII11I1IiI :
  iIIiii1 = 'S' + ( iIIiii1 ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = I11i1I1I + url
  III11II1I1Ii1 ( ( iIIiii1 ) . replace ( '  ' , '' ) , url , 100101 , IIi1iiii1iI , o0ooooO0o0O , i11iiiiI1i , '' )
  I1I11i ( 'Movies' , 'info' )
  if 72 - 72: OooOO000 * oo0oO00 % iIi1i1ii1 . ii
def OoO0O0O0o00 ( url , name , fanart , extra , iconimage ) :
 iiiI11 = extra
 iIIiii1 = name
 iIiIi1I = i1i1IIIIi1i ( url )
 IIi1iiii1iI = iconimage
 IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( iIiIi1I )
 for url , name , OOoO000 in IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = I11i1I1I + url
  OOoO000 = OOoO000
  oOOOO = name + ' - [COLORred]' + OOoO000 + '[/COLOR]'
  III11II1I1Ii1 ( oOOOO , url , 100102 , IIi1iiii1iI , fanart , 'Aired : ' + OOoO000 , oOOOO )
  if 49 - 49: IIiIiII11i . oo0oO00 . Ii % OOoOoo
def i11i1iiI1i ( name , URL , iconimage , fanart ) :
 I1 = i1i1IIIIi1i ( URL )
 IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , name in IIIII11I1IiI :
  for i11I in oO0Oo :
   if i11I in oO0o0 :
    URL = 'http://www.watchseriesgo.to/link/' + oO0o0
    O0000OOO0 ( name , URL , 100106 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( IIIII11I1IiI ) <= 0 :
  III11II1I1Ii1 ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 87 - 87: IIiIi1iI
  if 45 - 45: oO0o / ii - OooOO000 / iIi1i1ii1 % OOoOoo
def OoOIii11iI11i1I ( url , name ) :
 oOoOOo000oOoO0 = name
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( I1 )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( I1 )
 ooOoO00 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OoOo00o0OO ( url , oOoOOo000oOoO0 )
 for url in i1I :
  OoOo00o0OO ( url , oOoOOo000oOoO0 )
 for url in ooOoO00 :
  OoOo00o0OO ( url , oOoOOo000oOoO0 )
  if 1 - 1: oOo0O0Ooo % IIiIi1iI
def OoOo00o0OO ( url , season_name ) :
 if 'daclips.in' in url :
  oOoO00 ( url , season_name )
 elif 'filehoot.com' in url :
  iI1IIIii ( url , season_name )
 elif 'allmyvideos.net' in url :
  I1i11ii11 ( url , season_name )
 elif 'vidspot.net' in url :
  OO00O0oOO ( url , season_name )
 elif 'vodlocker' in url :
  Ii1iI111 ( url , season_name )
 elif 'vidto' in url :
  O0oooo00o0Oo ( url , season_name )
  if 36 - 36: iIi1i1ii1 / IIiIiII11i / OOoOoo / OOoOoo + Ii1I
  if 95 - 95: OOoOoo
def O0oooo00o0Oo ( url , season_name ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for Ooo0oo , I1111i in IIIII11I1IiI :
  IIi11IIiIii1 ( Ooo0oo , season_name )
  if 17 - 17: iIi1i1ii1 + oo0oO00 . oO0o - I1ii11iIi11i * Ii
  if 20 - 20: oOo0O0Ooo . ii % IIi
def I1i11ii11 ( url , season_name ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for Ooo0oo , I1111i in IIIII11I1IiI :
  IIi11IIiIii1 ( Ooo0oo , season_name )
  if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
def OO00O0oOO ( url , season_name ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I1 )
 for Ooo0oo , I1111i in IIIII11I1IiI :
  IIi11IIiIii1 ( Ooo0oo , season_name )
  if 39 - 39: OooOO000 / IIiIiII11i / Ii1I % oOo0O0Ooo
def Ii1iI111 ( url , season_name ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for Ooo0oo in IIIII11I1IiI :
  IIi11IIiIii1 ( Ooo0oo , season_name )
  if 89 - 89: O00OOo00oo0o + ii + O00OOo00oo0o * ooOoO0O00 + iI11I1II1I1I % iiII11i1I1IIi
def oOoO00 ( url , season_name ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( I1 )
 for Ooo0oo in IIIII11I1IiI :
  IIi11IIiIii1 ( Ooo0oo , season_name )
  if 59 - 59: IIi + Ii
def iI1IIIii ( url , season_name ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for Ooo0oo in IIIII11I1IiI :
  IIi11IIiIii1 ( Ooo0oo , season_name )
  if 88 - 88: Ii - IIiIi1iI
def IIi11IIiIii1 ( Link , season_name ) :
 if 'http:/' in Link :
  O0iIi1IiII ( Link )
  if 27 - 27: OooOO000 . iiII11i1I1IIi . iI11I1II1I1I . iI11I1II1I1I
def iIi1i ( url ) :
 I1 = OPEN_URL_1 ( url )
 i1ii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 for url in i1ii :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 68 - 68: IIi * o0o00Oo0O . iiII11i1I1IIi - IIiIiII11i . IIiIi1iI / IIiIiII11i
def III11II1I1Ii1 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1iOOOO = True
 ooO0oO00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooO0oO00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooO0oO00O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooOO00oOOo000 = [ ]
  if 14 - 14: oO0o . IIiIiII11i . iiII11i1I1IIi / iIi1i1ii1 % Ii1I - IIiIi1iI
  if showcontext == 'fav' :
   ooOO00oOOo000 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooOO00oOOo000 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooO0oO00O0o . addContextMenuItems ( ooOO00oOOo000 )
 I1iOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1 , listitem = ooO0oO00O0o , isFolder = True )
 return I1iOOOO
 if 67 - 67: iiII11i1I1IIi - IIi . ooOoO0O00
 if 35 - 35: OooOO000 + IIiIi1iI - oo0oO00 . OooOO000 . OOoOoo
def O0000OOO0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1iOOOO = True
 ooO0oO00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooO0oO00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooO0oO00O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooOO00oOOo000 = [ ]
  ooOO00oOOo000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooOO00oOOo000 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooOO00oOOo000 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooO0oO00O0o . addContextMenuItems ( ooOO00oOOo000 )
 I1iOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1 , listitem = ooO0oO00O0o , isFolder = False )
 return I1iOOOO
 if 87 - 87: OOooOOo
def IioO0O ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 86 - 86: OOooOOo . iI11I1II1I1I - oO0o
def oOOI11I ( url ) :
 iIIII1i = xbmc . Player ( o00oO0 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iIIII1i . play ( url ) . strip ( )
 except : pass
 if 5 - 5: iI11I1II1I1I
def O0iIi1IiII ( url ) :
 iIIII1i = xbmc . Player ( )
 import urlresolver
 try : iIIII1i . play ( url )
 except : pass
 if 72 - 72: oo0oO00 . O00OOo00oo0o / OOooOOo + iiII11i1I1IIi % iI11I1II1I1I
def i1i1IIIIi1i ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00O0oOO00O00 = ''
 i1Oo00 = ''
 try :
  O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
  i1Oo00 = O00O0oOO00O00 . read ( )
  O00O0oOO00O00 . close ( )
 except : pass
 if i1Oo00 != '' :
  return i1Oo00
 else :
  i1Oo00 = 'Opened'
  return i1Oo00
  if 42 - 42: Ii1I * OOooOOo % IIiIi1iI - OOooOOo . Ii - O00OOo00oo0o
  if 84 - 84: O00OOo00oo0o - Ii1I / iiII11i1I1IIi
  if 13 - 13: OOoOoo - I1ii11iIi11i - IIiIi1iI
def iiI ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   O00Oo ( )
  if i11I1II1I11i == 1 :
   Ii1111IiIi ( )
  if i11I1II1I11i == 2 :
   II1I1iiIII1I1 ( )
  if i11I1II1I11i == 3 :
   o0Ooo0o0ooo0 ( )
  if i11I1II1I11i == 4 :
   oo0o0000Oo0 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'SearchCartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( ooOO0O0ooOooO ) , 21004 , oOOOo00O00oOo + 'watchcartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CARTOONS[/COLOR]' , '' , 10001 , oOOOo00O00oOo + 'Cartoons.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '' , 20000 , oOOOo00O00oOo + 'Cartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , oOOOo00O00oOo + 'anime.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def I1ii1ii11i1I ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']FOOTBALL[/COLOR]' , '' , 10002 , oOOOo00O00oOo + 'Football.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , oOOOo00O00oOo + 'Fitness.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']Go Fishing[/COLOR]' , str ( ooOO0O0ooOooO ) , 8090 , oOOOo00O00oOo + 'GoFishing.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , oOOOo00O00oOo + 'GenieTVKitchen.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 80 - 80: O00OOo00oo0o - I1ii11iIi11i
 if 96 - 96: Ii1I / IIiIiII11i . iIi1i1ii1 - OooOO000 * iiII11i1I1IIi * oo0oO00
 if 76 - 76: iIi1i1ii1 - IIiIiII11i * IIi / ii
def OO ( ) :
 I1 = O000oo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiooOOoooooo in IIIII11I1IiI :
  IIiooOOoooooo = ( str ( IIiooOOoooooo ) )
  if os . path . exists ( xbmc . translatePath ( IIiooOOoooooo ) ) :
   IIIiIi = ( IIiooOOoooooo ) . replace ( 'special://home/addons/' , '' )
   OO0O000 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + IIIiIi + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   i11I1II1I11i = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if i11I1II1I11i == 0 :
    Iii ( IIiooOOoooooo )
    O0O0ooOOO ( )
   elif i11I1II1I11i == 1 :
    IIIII1iii ( IIiooOOoooooo )
  else :
   pass
   if 7 - 7: I11i + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
def IIIII1iii ( addon ) :
 IIIiIi = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 22 - 22: IIiIi1iI - IIiIi1iI % IIi . O00OOo00oo0o + oo0oO00
def Iii ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 Oo00OOo00O = os . path . join ( I11II1i , 'default.py' )
 o0Ii1Iii111IiI1 = open ( Oo00OOo00O , "w+" )
 if 98 - 98: O00OOo00oo0o - ii % oOo0O0Ooo + o0o00Oo0O . iIi1i1ii1
 o0Ii1Iii111IiI1 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 o0Ii1Iii111IiI1 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 o0Ii1Iii111IiI1 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 56 - 56: IIiIiII11i / oo0oO00 + Ii + IIi
 if 54 - 54: iIi1i1ii1 - iiII11i1I1IIi - O00OOo00oo0o . iI11I1II1I1I
 if 79 - 79: iIi1i1ii1 . oO0o
 if 40 - 40: I11i + I1ii11iIi11i . I11i % IIiIi1iI
def I11I1IIiiII1 ( url ) :
 I1 = O000oo ( url )
 IIIIIii1ii11 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 OOOooo0OooOoO = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 ooOoO00 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 Iii1I1111ii = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 oOoOOOo = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( I1 )
 for I1111i , url , iiO0oOo00o , o0ooooO0o0O , iIiiii in IIIIIii1ii11 :
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 90037 , iiO0oOo00o , o0ooooO0o0O , iIiiii )
  elif I1111i == 'Search' :
   iiOOooooO0Oo ( 'Search' , url , 90038 , iiO0oOo00o , o0ooooO0o0O , iIiiii )
  else :
   OOiIiIIi1 ( I1111i , url , 222 , iiO0oOo00o , o0ooooO0o0O , iIiiii )
 for I1111i , o00O0O , url , ii1Io0OOoOoO00 in OOOooo0OooOoO :
  iiOOooooO0Oo ( I1111i , url , 90037 , o00O0O , ii1Io0OOoOoO00 , '' )
 for I1111i , o00O0O , url , ii1Io0OOoOoO00 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 90037 , o00O0O , ii1Io0OOoOoO00 , '' )
 for I1111i , url , o00O0O , ii1Io0OOoOoO00 in i1I :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , ii1Io0OOoOoO00 , '' )
 for I1111i , url , o00O0O , ii1Io0OOoOoO00 in ooOoO00 :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , ii1Io0OOoOoO00 , '' )
 for I1111i , url , o00O0O , ii1Io0OOoOoO00 in Iii1I1111ii :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , ii1Io0OOoOoO00 , '' )
 for I1111i , url , o00O0O in oOoOOOo :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , '' , '' )
  I1I11i ( 'tvshows' , 'Media Info 3' )
  if 15 - 15: OOoOoo / o0o00Oo0O . I11i . Ii
def o0OO0O0Oo ( ) :
 OOOOO = [ 'serialsearch' , 'moviesearch' ]
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 if iiIii1I == '' :
  pass
 else :
  for i1I11iIiII in OOOOO :
   OO0OO0OO = I11 + i1I11iIiII + '.php'
   iIiIi1I = O000oo ( OO0OO0OO )
   if iIiIi1I != 'Opened' :
    oo00O00oO000o = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( iIiIi1I )
    for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O , iIiiii in oo00O00oO000o :
     if iiIii1I in I1111i . lower ( ) :
      OoooO0o = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( o00OO00OoO ) )
      for i11I in OoooO0o :
       if i11I == oO0o0 :
        I1111i = '[COLORred]* [/COLOR]' + ( I1111i ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        IIIii1iiIi = open ( oOOoo0Oo , "a" )
        IIIii1iiIi . write ( 'item="' + I1111i + '"\n' )
        IIIii1iiIi . close
      if 'php' in oO0o0 :
       iiOOooooO0Oo ( I1111i , oO0o0 , 90037 , iiO0oOo00o , o0ooooO0o0O , iIiiii )
      else :
       OOiIiIIi1 ( I1111i , oO0o0 , 222 , iiO0oOo00o , o0ooooO0o0O , iIiiii )
       if 63 - 63: Ii1I
   I1I11i ( 'tvshows' , 'Media Info 3' )
   if 6 - 6: IIiIi1iI / Ii1I
def oOooO00o0O ( ) :
 I1 = O000oo ( 'http://www.tvcatchup.com/channels/' )
 iii1i1iiiiIi = O000oo ( 'http://www.djing.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 OOo0 = re . compile ( 'title="([^"]*)" >.+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for iiIii1IIi , o00O0O , oO0o0 in IIIII11I1IiI :
  OoO ( iiIii1IIi , 'http://www.tvcatchup.com' + oO0o0 , 90024 , 'http://www.tvcatchup.com' + o00O0O )
 for iiIii1IIi , oO0o0 , o00O0O in OOo0 :
  OoO ( iiIii1IIi , 'http://www.tvcatchup.com' + oO0o0 , 90024 , o00O0O )
 for oO0o0 , o00O0O , I1111i in i1I :
  if 'Submit' in I1111i :
   pass
  elif '&lt;' in I1111i :
   pass
  else :
   OOiIiIIi1 ( 'DJing  ' + I1111i , oO0o0 , 90025 , 'http://www.djing.com' + o00O0O , O0o0Oo , '' )
  I1I11i ( 'movies' , 'MAIN' )
def ii1IiIiI1 ( url ) :
 I1 = O000oo ( url )
 if 90 - 90: I11i - Ii + ooOoO0O00 - iIi1i1ii1 % I1ii11iIi11i
 IIIII11I1IiI = re . compile ( "file: '([^']*)'," ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def O0ooOo0o0Oo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 71 - 71: iI11I1II1I1I - IIi . oOo0O0Ooo % ii + IIi
def iIIi ( ) :
 if 26 - 26: I1ii11iIi11i + IIi / oO0o % OOooOOo % Ii1I + IIiIiII11i
 if 31 - 31: iiII11i1I1IIi % IIi * iiII11i1I1IIi
 if 45 - 45: ooOoO0O00 . oOo0O0Ooo + IIi - ii % IIiIi1iI
 if 1 - 1: iI11I1II1I1I
 if 93 - 93: ooOoO0O00 . Ii . I1ii11iIi11i
 if 99 - 99: iiII11i1I1IIi - O00OOo00oo0o - oo0oO00 % oO0o
 I1 = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'yr' in oO0o0 :
   oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + oO0o0 , 10201 , oOOOo00O00oOo + 'rated.png' )
   if 21 - 21: IIiIiII11i % Ii1I . ooOoO0O00 - ii
def iiOOOO0o ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( I1 )
 for i1I1iIi1IiI , url , I1111i in IIIII11I1IiI :
  if 'id' in url :
   oo000ii ( ( '[COLORred]RANK [COLORblue]' + i1I1iIi1IiI + '[COLORred] - [COLORblue]' + I1111i + '[/COLOR]' ) , I1111i , 10202 , oOOOo00O00oOo + 'rated.png' )
   if 11 - 11: IIiIiII11i
def O00O00O000OOO ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iI = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOoOOo0O00O = ( url )
 iiIii1I = OOoOOo0O00O . lower ( )
 Oo0O = 'http://onlinemovies.tube/?s=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 if 1 - 1: o0o00Oo0O / OooOO000 % O00OOo00oo0o . I1ii11iIi11i + OOoOoo
 I1Ii11iiiI = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 if 16 - 16: O00OOo00oo0o
 O0OoOOO00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 o0ooOo0OOOO0o = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0ooOoO = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + OOoOOo0O00O
 IIII = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iI1iiiIiii = ( i11 ( 'aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9tb3ZpZXNlYXJjaC5waHA=' ) )
 ii1i1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 if 50 - 50: I11i * iIi1i1ii1 % Ii1I / I1ii11iIi11i - o0o00Oo0O % OooOO000
 if 48 - 48: oOo0O0Ooo + Ii1I + IIiIiII11i * Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = OOoOO0oo0ooO ( Oo0O )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 13 - 13: ii * oo0oO00 - iIi1i1ii1 / IIi + iiII11i1I1IIi + OOoOoo
 if 39 - 39: iI11I1II1I1I - ii
 Iiii = OOoOO0oo0ooO ( I1Ii11iiiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 if 81 - 81: Ii1I - o0o00Oo0O * ii
 if 23 - 23: IIiIiII11i / oo0oO00
 iII1Iii1I11i = OOoOO0oo0ooO ( O0OoOOO00 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1o0oooO = OOoOO0oo0ooO ( O0ooOoO )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooOo = OOoOO0oo0ooO ( IIII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 o0oO0OoO0 = OOoOO0oo0ooO ( iI1iiiIiii )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 oOOOOOoOO = OOoOO0oo0ooO ( ii1i1i )
 if 81 - 81: IIiIiII11i + Ii / OooOO000
 if 85 - 85: Ii + O00OOo00oo0o * OOooOOo
 if 1 - 1: ooOoO0O00 / I1ii11iIi11i . oO0o
 if 57 - 57: iiII11i1I1IIi . I1ii11iIi11i + IIiIiII11i
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( I1 )
  next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( I1 )
  for url , o00O0O , I1111i , i111i11I1ii in IIIII11I1IiI :
   if iiIii1I in I1111i . lower ( ) :
    if 'movies' in i111i11I1ii :
     oo000ii ( '[COLORred]*[COLOR' + II + ']' + i111i11I1ii + '-' + I1111i + '-[COLORred] source MOVIE HUB[/COLOR]' , url , 90044 , o00O0O )
  for url in next :
   OOooo ( url )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 0 , "" , "Getting Source MOVIE HUB" )
   if 54 - 54: IIiIiII11i . iiII11i1I1IIi
   if 73 - 73: OOooOOo . oOo0O0Ooo
   if 32 - 32: OOooOOo * oOo0O0Ooo % IIiIi1iI * iIi1i1ii1 . o0o00Oo0O
   if 48 - 48: OooOO000 * OooOO000
   if 13 - 13: iIi1i1ii1 / iiII11i1I1IIi + OOooOOo . I11i % IIiIi1iI
   if 48 - 48: oOo0O0Ooo / Ii - I11i * oo0oO00 / ii
   if 89 - 89: iI11I1II1I1I / oOo0O0Ooo - IIiIiII11i / iIi1i1ii1 . Ii . iIi1i1ii1
 if Iiii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for IiiiI1 , I1111i in ooOoO00 :
   if iiIii1I in I1111i . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1Ii11iiiI + IiiiI1 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
    if 100 - 100: oo0oO00 . iIi1i1ii1 % ooOoO0O00 . IIiIi1iI
    if 79 - 79: oO0o % IIi / iI11I1II1I1I + OOooOOo * oO0o
    if 30 - 30: ii / iiII11i1I1IIi + OooOO000 / Ii1I * o0o00Oo0O
    if 16 - 16: I1ii11iIi11i / Ii
    if 64 - 64: Ii / iIi1i1ii1 * ooOoO0O00
    if 73 - 73: I1ii11iIi11i - OOooOOo - oo0oO00 - oOo0O0Ooo
    if 65 - 65: I11i
    if 7 - 7: OOoOoo . OOooOOo / Ii1I . IIi * iiII11i1I1IIi - IIiIiII11i
    if 37 - 37: O00OOo00oo0o . OOooOOo / o0o00Oo0O * OooOO000
 if iII1Iii1I11i != 'Failed' :
  III11iiii11i1 = [ ]
  oOoOOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iII1Iii1I11i )
  for url , Iiii1iI1i , iIiiii , iiii11i , I1111i in oOoOOOo :
   if iiIii1I in I1111i . lower ( ) :
    if I1111i in III11iiii11i1 :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , Iiii1iI1i , iiii11i , iIiiii )
     III11iiii11i1 . append ( I1111i )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if i1o0oooO != 'Failed' :
  ooOo0OoO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1o0oooO )
  for url , o00O0O , I1111i in ooOo0OoO :
   if iiIii1I in I1111i . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 36 - 36: OOoOoo - ii / oO0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: IIiIi1iI
    if 45 - 45: IIiIi1iI / I1ii11iIi11i / iIi1i1ii1
    if 44 - 44: Ii1I - iIi1i1ii1 / IIiIiII11i * oO0o * I1ii11iIi11i
    if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * IIi % IIiIiII11i
    if 56 - 56: ii * I1ii11iIi11i . I1ii11iIi11i . Ii1I
    if 24 - 24: I1ii11iIi11i . iiII11i1I1IIi * iIi1i1ii1 % OooOO000 / IIi
    if 58 - 58: oOo0O0Ooo - Ii1I % o0o00Oo0O . oOo0O0Ooo % oO0o % OOoOoo
    if 87 - 87: oo0oO00 - Ii
    if 78 - 78: Ii / iI11I1II1I1I - I11i
 if o0oO0OoO0 != 'Failed' :
  iIIIIiiIii = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( o0oO0OoO0 )
  for I1111i , url , Iiii1iI1i , iiii11i , iIiiii in iIIIIiiIii :
   if iiIii1I in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Reaper[/COLOR]' ) , url , 222 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 58 - 58: I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oOOOOOoOO != 'Failed' :
  IiiIIIiI1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOOOOoOO )
  for url , Iiii1iI1i , iIiiii , iiii11i , I1111i in IiiIIIiI1ii :
   if iiIii1I in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 78 - 78: o0o00Oo0O * IIi
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 43 - 43: Ii1I / oOo0O0Ooo . IIiIi1iI
    if 62 - 62: iI11I1II1I1I + OooOO000 . I1ii11iIi11i / OOoOoo % o0o00Oo0O . O00OOo00oo0o
    if 93 - 93: Ii % iI11I1II1I1I % Ii + I11i / I11i / IIiIiII11i
    if 49 - 49: IIi . Ii1I . Ii - IIiIiII11i / iIi1i1ii1
    if 62 - 62: IIi
    if 1 - 1: OOoOoo / OOoOoo - Ii
    if 87 - 87: I1ii11iIi11i / o0o00Oo0O * OOoOoo / I11i
    if 19 - 19: O00OOo00oo0o + ooOoO0O00 . oOo0O0Ooo - I1ii11iIi11i
    if 16 - 16: oo0oO00 + IIiIi1iI / I11i
    if 82 - 82: OOoOoo * Ii % IIiIiII11i - ii
 OO0 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 62 - 62: ooOoO0O00 / IIiIi1iI . oOo0O0Ooo * I11i
 for i1I11iIiII in OO0 :
  OO0OO0OO = OOOO0OOoO0O0 + i1I11iIiII + IIiiiiiiIi1I1
  i11i1Ii1 = OOoOO0oo0ooO ( OO0OO0OO )
  if i11i1Ii1 != 'Failed' :
   o0oO0oo0000OO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i11i1Ii1 )
   for url , Iiii1iI1i , iIiiii , iiii11i , I1111i in o0oO0oo0000OO :
    if iiIii1I in I1111i . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , Iiii1iI1i , iiii11i , iIiiii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 45 - 45: O00OOo00oo0o * iIi1i1ii1 / ii . oo0oO00 % Ii1I / ooOoO0O00
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 24 - 24: IIi + I11i + iiII11i1I1IIi - OOoOoo + OOooOOo
 OO0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 14 - 14: iIi1i1ii1 . Ii
 if 27 - 27: IIiIi1iI % o0o00Oo0O % O00OOo00oo0o
 for i1I11iIiII in OO0 :
  OO0OO0OO = iI + i1I11iIiII
  OoOoOo0 = OOoOO0oo0ooO ( OO0OO0OO )
  if OoOoOo0 != 'Failed' :
   i1II11II1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( OoOoOo0 )
   for IiiiI1 , I1111i in i1II11II1 :
    if OOoOOo0O00O in I1111i . lower ( ) :
     OoO ( ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iI + i1I11iIiII + IiiiI1 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 5 - 5: I1ii11iIi11i - Ii1I % oo0oO00 - IIiIiII11i . oOo0O0Ooo + OooOO000
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 47 - 47: o0o00Oo0O - iI11I1II1I1I - OooOO000
def ii1I1IiiI1ii1i ( ) :
 oo000ii ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , oOOOo00O00oOo + 'running.png' )
 oo000ii ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , oOOOo00O00oOo + 'countdown.png' )
 oo000ii ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , oOOOo00O00oOo + 'unknown.png' )
 oo000ii ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , oOOOo00O00oOo + 'cancelled.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 46 - 46: iIi1i1ii1 . IIi * oO0o . ii + Ii1I
def oo0000o ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( I1 )
 for I1111i , iIIiii1 , iII1I1 , OOoO000 , i1IIi1i1Ii1 in IIIII11I1IiI :
  oo000ii ( ( '[COLORblue]' + I1111i + '[/COLOR] [COLORred]Season[/COLOR]-' + iIIiii1 + ' [COLORred]Returns [/COLOR]- ' + i1IIi1i1Ii1 + ' ' + OOoO000 ) , I1111i , 10099 , oOOOo00O00oOo + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 45 - 45: iI11I1II1I1I . oo0oO00 / OOooOOo / OOoOoo
def ooOOOoOoOOO0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( I1 )
 for I1111i , iIIiii1 , iII1I1 in IIIII11I1IiI :
  oo000ii ( ( '[COLORblue]' + I1111i + '[/COLOR] [COLORred]Season[/COLOR]-' + iIIiii1 + ' [COLORred] Status Unknown[/COLOR] ' ) , I1111i , 10099 , oOOOo00O00oOo + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 5 - 5: IIi
def I1i1iIi1I1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( I1 )
 for I1111i , iIIiii1 , iII1I1 , OOoO000 in IIIII11I1IiI :
  oo000ii ( ( '[COLORblue]' + I1111i + ' [COLORred] Cancelled On[/COLOR] ' + OOoO000 ) , I1111i , 10099 , oOOOo00O00oOo + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 60 - 60: OOooOOo / O00OOo00oo0o - IIiIiII11i . I1ii11iIi11i + o0o00Oo0O
def Ii1iI ( url ) :
 OOoOOo0O00O = ( url )
 iiIii1I = OOoOOo0O00O . lower ( )
 if 53 - 53: iI11I1II1I1I - oo0oO00 % OOooOOo * O00OOo00oo0o % IIiIi1iI
 url = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllc2dvLnRvL3NlYXJjaC8=' ) ) + ( OOoOOo0O00O ) . replace ( ' ' , '%20' )
 Oo0O = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 o0O0O0ooo0oOO = 'http://onlinemovies.tube/?s=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 I1Ii11iiiI = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 II1Ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 O0OoOOO00 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiIii1I ) . replace ( ' ' , '+' )
 o0ooOo0OOOO0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 O0ooOoO = ( i11 ( 'aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9zZXJpYWxzZWFyY2gucGhw' ) )
 IIII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 57 - 57: OOooOOo - oo0oO00 / IIiIi1iI % Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 3 - 3: OooOO000 . IIiIi1iI % oOo0O0Ooo + Ii1I
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = OOoOO0oo0ooO ( url )
 o0oOoO00o . update ( 7 , "" , "Checking Source 2/9 Links" )
 oo0o = OOoOO0oo0ooO ( Oo0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = OOoOO0oo0ooO ( o0O0O0ooo0oOO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = OOoOO0oo0ooO ( I1Ii11iiiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = OOoOO0oo0ooO ( II1Ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iII1Iii1I11i = cloudflare . source ( O0OoOOO00 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 OoOoOo0 = OOoOO0oo0ooO ( o0ooOo0OOOO0o )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 i1o0oooO = OOoOO0oo0ooO ( O0ooOoO )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 ooOo = OOoOO0oo0ooO ( IIII )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 51 - 51: IIi . oOo0O0Ooo
 if ooOo != 'Failed' :
  Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOo )
  for url , Iiii1iI1i , iIiiii , iiii11i , I1111i in Oo :
   if iiIii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 34 - 34: O00OOo00oo0o % oo0oO00 % OOooOOo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 63 - 63: oOo0O0Ooo - oO0o % OooOO000 % iiII11i1I1IIi / I11i / ooOoO0O00
 if i1o0oooO != 'Failed' :
  ooOo0OoO = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( i1o0oooO )
  for I1111i , url , Iiii1iI1i , iiii11i , iIiiii in ooOo0OoO :
   if iiIii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Reaper[/COLOR]' ) , url , 90037 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 69 - 69: I1ii11iIi11i * IIiIiII11i * IIiIi1iI . OooOO000 - Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 39 - 39: iIi1i1ii1 * oOo0O0Ooo % oO0o . OOooOOo
    if 24 - 24: ooOoO0O00 * iI11I1II1I1I / iIi1i1ii1
    if 78 - 78: Ii + I11i + O00OOo00oo0o / I11i % iI11I1II1I1I % OOoOoo
    if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % O00OOo00oo0o . Ii1I % o0o00Oo0O
    if 47 - 47: I11i
    if 66 - 66: oOo0O0Ooo - OOoOoo
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 33 - 33: oOo0O0Ooo / oO0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  iiIIi = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for url , o00O0O , I1111i , i1i in i1I :
   if iiIii1I in I1111i . lower ( ) :
    if 'season' in i1i :
     oo000ii ( '[COLORred]*[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , o00O0O , o00O0O , '' )
    if 'episodes' in i1i :
     oo000ii ( '[COLORred]*[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , o00O0O , o00O0O , '' )
  for url in iiIIi :
   oo000ii ( '[COLORred]*[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , oOOOo00O00oOo + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 25 - 25: oo0oO00
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  OOOooo0OooOoO = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( oo0o )
  for url , I1111i , o00O0O in OOOooo0OooOoO :
   if iiIii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 34 - 34: OOooOOo . iI11I1II1I1I % o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for o00O0O , url , I1111i in IIIII11I1IiI :
   if iiIii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - WatchSeries[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , 'http://www.watchseriesgo.to/' + o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Source WatchSeries Links" )
    if 43 - 43: Ii1I - OooOO000
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for I1111i in ooOoO00 :
   if iiIii1I in I1111i . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( I1Ii11iiiI + I1111i ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 70 - 70: OooOO000 / IIi % IIiIi1iI - iIi1i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for I1111i in Iii1I1111ii :
   if iiIii1I in I1111i . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( II1Ii + I1111i ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 47 - 47: OooOO000
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iII1Iii1I11i != 'Failed' :
  oOoOOOo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iII1Iii1I11i )
  for url , o00O0O , I1111i in oOoOOOo :
   if iiIii1I in I1111i . lower ( ) :
    oo000ii ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] Source - Dizi[/COLOR]' , url , 8062 , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 92 - 92: IIi + OOooOOo % ooOoO0O00
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if OoOoOo0 != 'Failed' :
  i1II11II1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOoOo0 )
  for url , Iiii1iI1i , iIiiii , iiii11i , I1111i in i1II11II1 :
   if iiIii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 23 - 23: O00OOo00oo0o - IIi + iIi1i1ii1 - OOooOOo * OOooOOo . I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 47 - 47: oo0oO00 % iI11I1II1I1I
 IiI1IIIII1I = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for i1I11iIiII in IiI1IIIII1I :
  OO0OO0OO = OOOO0OOoO0O0 + i1I11iIiII + IIiiiiiiIi1I1
  oOOOOOoOO = OOoOO0oo0ooO ( OO0OO0OO )
  if oOOOOOoOO != 'Failed' :
   IiiIIIiI1ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOOOOOoOO )
   for I1111i , iIiiii , url , o00O0O , o0ooooO0o0O , Ii11iiI in IiiIIIiI1ii :
    if iiIii1I in I1111i . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , url , Ii11iiI , o00O0O , o0ooooO0o0O , iIiiii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 35 - 35: iIi1i1ii1 - iIi1i1ii1 + ooOoO0O00 - o0o00Oo0O - O00OOo00oo0o
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 58 - 58: OOooOOo - OooOO000 - ii
     if 96 - 96: iI11I1II1I1I
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 82 - 82: OOooOOo + o0o00Oo0O - OOoOoo % oo0oO00 * Ii
def OO0oo0O ( ) :
 if 15 - 15: I11i
 if 39 - 39: IIi / Ii1I / oOo0O0Ooo * O00OOo00oo0o
 if 44 - 44: o0o00Oo0O + IIiIi1iI . iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - iiII11i1I1IIi
 if 83 - 83: OOoOoo * iiII11i1I1IIi / I1ii11iIi11i
 if 32 - 32: I11i + OOooOOo - ii
 if 39 - 39: ii * IIi * o0o00Oo0O . iiII11i1I1IIi . oO0o + IIiIi1iI
 if 9 - 9: OOooOOo + oo0oO00 % ii + I11i
 if 56 - 56: ii + Ii1I - OooOO000
 if 24 - 24: I11i + IIiIi1iI + iiII11i1I1IIi - iI11I1II1I1I
 if 49 - 49: iiII11i1I1IIi . IIiIi1iI * OOooOOo % OOoOoo . o0o00Oo0O
 if 48 - 48: o0o00Oo0O * iIi1i1ii1 - o0o00Oo0O / iIi1i1ii1 + OOooOOo
 oo000ii ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , oOOOo00O00oOo + 'seasons.png' )
 oo000ii ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , oOOOo00O00oOo + 'episodes.png' )
 oo000ii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , oOOOo00O00oOo + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 52 - 52: oO0o % iIi1i1ii1 * IIiIiII11i
def I1IiIii11I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( I1 )
 for url , I1111i , i1iii1ii in IIIII11I1IiI :
  oo000ii ( ( I1111i + ' - ' + i1iii1ii ) . replace ( '&amp;' , '&' ) , url , 90053 , oOOOo00O00oOo + 'seasons.png' )
  if 18 - 18: oO0o . IIiIiII11i % OOooOOo % iIi1i1ii1
def oo0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , url , 90054 , oOOOo00O00oOo + 'episodes.png' )
  if 16 - 16: iIi1i1ii1 * oO0o / oo0oO00
def II1iiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( I1 )
 for o00O0O , I1111i , url in IIIII11I1IiI :
  oo000ii ( I1111i , url , 90054 , o00O0O )
 for url in next :
  oo000ii ( 'NEXT' , url , 90053 , oOOOo00O00oOo + 'Next.png' )
  if 31 - 31: I11i % iiII11i1I1IIi + iI11I1II1I1I + Ii * O00OOo00oo0o
def I1i1I1I11IiiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( I1 )
 for o00O0O , i1iii1ii , url , I1111i , I1IiI1iI11 in IIIII11I1IiI :
  iiOOooooO0Oo ( i1iii1ii + ' - ' + I1111i + ' - ' + I1IiI1iI11 , url , 90044 , o00O0O , o00O0O , '' )
 for o00O0O , I1111i , url in i1I :
  oo000ii ( I1111i , url , 90044 , o00O0O , o00O0O , '' )
 for url in next :
  oo000ii ( 'NEXT' , url , 90053 , oOOOo00O00oOo + 'Next.png' )
  if 2 - 2: iI11I1II1I1I
def iiii1 ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0o0oO0O000o = 'http://onlinemovies.tube/?s=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 iiIii1I = OO0o0oO0O000o . lower ( )
 I1 = O000oo ( iiIii1I )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i , i1i in IIIII11I1IiI :
  if 'season' in i1i :
   oo000ii ( I1111i , oO0o0 , 90054 , o00O0O , o00O0O , '' )
  if 'episodes' in i1i :
   oo000ii ( I1111i , oO0o0 , 90044 , o00O0O , o00O0O , '' )
 for oO0o0 in next :
  oo000ii ( 'NEXT' , oO0o0 , 90053 , oOOOo00O00oOo + 'Next.png' )
  if 47 - 47: O00OOo00oo0o - oO0o / iIi1i1ii1 * ii / iIi1i1ii1 . I1ii11iIi11i
def oO0o00oo0 ( ) :
 if 34 - 34: IIiIi1iI
 if 27 - 27: O00OOo00oo0o + ii - OOooOOo
 if 15 - 15: oo0oO00 / iiII11i1I1IIi * o0o00Oo0O . IIiIiII11i - oO0o
 if 90 - 90: oo0oO00
 if 94 - 94: iiII11i1I1IIi / Ii1I * O00OOo00oo0o - OOooOOo
 if 44 - 44: iIi1i1ii1 % Ii - OooOO000 * Ii1I + I1ii11iIi11i * IIi
 if 41 - 41: o0o00Oo0O * IIiIi1iI - OOooOOo . iIi1i1ii1
 if 65 - 65: I1ii11iIi11i . ii
 if 70 - 70: I1ii11iIi11i - oo0oO00 . iI11I1II1I1I % iiII11i1I1IIi / OOooOOo - o0o00Oo0O
 if 55 - 55: OooOO000 - oO0o
 oo000ii ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , oOOOo00O00oOo + 'allmov.png' )
 oo000ii ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , oOOOo00O00oOo + 'Genre.png' )
 oo000ii ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , oOOOo00O00oOo + 'Years.png' )
 oo000ii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , oOOOo00O00oOo + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 100 - 100: o0o00Oo0O
def o00IiI1iiII1i1i ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( I1 )
 for url , I1111i , i1iii1ii in IIIII11I1IiI :
  if 'genre' in url :
   oo000ii ( ( I1111i + ' - ' + i1iii1ii ) . replace ( '&amp;' , '&' ) , url , 90043 , oOOOo00O00oOo + 'Genre.png' )
   if 18 - 18: oOo0O0Ooo
def oO0oI1I1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  if 'release' in url :
   oo000ii ( I1111i , url , 90043 , oOOOo00O00oOo + 'Years.png' )
   if 99 - 99: IIiIi1iI / iI11I1II1I1I - iIi1i1ii1 * Ii1I % oOo0O0Ooo
def OOooo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( I1 )
 for o00O0O , I1111i , i1II1i , url , iIiiii in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' ' + i1II1i , url , 90044 , o00O0O , o00O0O , iIiiii )
 for o00O0O , I1111i , i1i , url , I1iIiiiI1 , iIiiii in i1I :
  if 'movies' in i1i :
   iiOOooooO0Oo ( I1111i + ' - ' + I1iIiiiI1 , url , 90044 , o00O0O , o00O0O , iIiiii )
 for url in next :
  oo000ii ( 'NEXT' , url , 90043 , oOOOo00O00oOo + 'Next.png' )
  if 42 - 42: IIi % oo0oO00 / oO0o - oo0oO00 * Ii
def iI1IiiiIiI1Ii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  Oo000 ( 'http:' + url )
  if 48 - 48: Ii % oo0oO00
def Oo000 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  OoO ( ( I1111i ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , oOOOo00O00oOo + 'movhub.png' )
def i11i11 ( ) :
 if 18 - 18: iI11I1II1I1I + iiII11i1I1IIi * oOo0O0Ooo - IIi / oOo0O0Ooo
 if 78 - 78: iiII11i1I1IIi . OOoOoo
 if 38 - 38: OOooOOo + OOoOoo
 if 15 - 15: I1ii11iIi11i + iiII11i1I1IIi . IIiIi1iI - iI11I1II1I1I / o0o00Oo0O % iI11I1II1I1I
 if 86 - 86: oOo0O0Ooo / oo0oO00 * iIi1i1ii1
 if 64 - 64: IIiIi1iI / o0o00Oo0O * OOooOOo * IIiIi1iI
 if 60 - 60: iiII11i1I1IIi / ooOoO0O00 % Ii1I / Ii1I * Ii1I . Ii
 if 99 - 99: OOooOOo
 if 77 - 77: I11i
 if 48 - 48: OOooOOo % Ii1I / iiII11i1I1IIi . iI11I1II1I1I * IIiIiII11i
 if 65 - 65: OOooOOo
 if 31 - 31: iiII11i1I1IIi * OOooOOo . OOoOoo % iIi1i1ii1 + I1ii11iIi11i
 if 47 - 47: o0o00Oo0O * oOo0O0Ooo * oO0o . IIiIiII11i
 if 95 - 95: iIi1i1ii1 % OOoOoo . o0o00Oo0O % O00OOo00oo0o
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0o0oO0O000o = 'http://onlinemovies.tube/?s=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 iiIii1I = OO0o0oO0O000o . lower ( )
 I1 = O000oo ( iiIii1I )
 IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i , i111i11I1ii in IIIII11I1IiI :
  if 'movies' in i111i11I1ii :
   oo000ii ( i111i11I1ii + '-' + I1111i , oO0o0 , 90044 , o00O0O )
 for oO0o0 in next :
  OOooo ( oO0o0 )
  if 68 - 68: I1ii11iIi11i . I1ii11iIi11i - Ii1I / iiII11i1I1IIi . IIiIi1iI / ooOoO0O00
def oO00oOooooo0 ( ) :
 oo000ii ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O000oo ( 'http://www.join4films.com/' )
 IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , oO0o0 , 80006 , oOOOo00O00oOo + 'Desi.png' )
def iI1i1iIi1iiII ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  OoO ( I1111i , url , 80007 , o00O0O )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  oo000ii ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def o0OoO0000o ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  OOOOo0o00OO0000 ( url )
def o0Ii1 ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0o0oO0O000o = 'http://www.join4films.com/?s=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' ) + '&search_type=1'
 iiIii1I = OO0o0oO0O000o . lower ( )
 iI1i1iIi1iiII ( iiIii1I )
 if 50 - 50: oo0oO00 - IIiIi1iI / iI11I1II1I1I - oO0o + IIiIiII11i - o0o00Oo0O
 if 88 - 88: oo0oO00 * oO0o
 if 35 - 35: Ii1I / OooOO000 % oOo0O0Ooo + iI11I1II1I1I
 if 79 - 79: OOooOOo / IIiIi1iI
 if 77 - 77: I1ii11iIi11i
 if 46 - 46: O00OOo00oo0o
 if 72 - 72: OooOO000 * IIi
 if 67 - 67: ooOoO0O00
 if 5 - 5: IIiIiII11i . ii
 if 57 - 57: oOo0O0Ooo
 if 35 - 35: ii - O00OOo00oo0o / oO0o
 if 50 - 50: OOooOOo
 if 33 - 33: iiII11i1I1IIi
 if 98 - 98: OOooOOo % IIiIiII11i
 if 95 - 95: iI11I1II1I1I - O00OOo00oo0o - IIi + O00OOo00oo0o % Ii1I . oOo0O0Ooo
 if 41 - 41: o0o00Oo0O + oo0oO00 . ooOoO0O00 - IIiIiII11i * I11i . oO0o
 if 68 - 68: I11i
def i11Ii1IIi ( ) :
 iiOOooooO0Oo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 if 36 - 36: o0o00Oo0O * oO0o % OooOO000 * OooOO000 / oO0o * OOoOoo
def IiI ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0o0oO0O000o = 'http://imoviemax.se/?s=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 iiIii1I = OO0o0oO0O000o . lower ( )
 O0o0OO00 ( iiIii1I )
def iIi11i ( url ) :
 ooIII1II1iii1i = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , I1111i , O0OO0oOO in IIIII11I1IiI :
  if I1111i in ooIII1II1iii1i :
   pass
  else :
   iiOOooooO0Oo ( I1111i + ' - ' + O0OO0oOO + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
   ooIII1II1iii1i . append ( I1111i )
   if 85 - 85: o0o00Oo0O
def IiiIiI1I1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , iI111i11iI1 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' - Views:' + iI111i11iI1 , url , 10075 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
  if 2 - 2: OOooOOo + O00OOo00oo0o + ii . ooOoO0O00
  if 19 - 19: OooOO000 - I11i - iIi1i1ii1 - OOooOOo . OooOO000 . O00OOo00oo0o
def O0o0OO00 ( url ) :
 i11I1I = [ ]
 I1 = O000oo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  iiOOooooO0Oo ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , I1111i , url in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10075 , o00O0O , o00O0O , '' )
  i11I1I . append ( I1111i )
  if 71 - 71: OooOO000
def Iiii1i11ii1Ii ( img , name , url ) :
 img = img
 name = name
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for i1Oo0oOo000OoO0 , url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  IIii1I1i = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + IIii1I1i
  IIII1iIIii = ( i1Oo0oOo000OoO0 ) . replace ( 'play-' , 'Server ' )
  OOiIiIIi1 ( IIII1iIIii , IIii1I1i , 10076 , img , img , '' )
  if 12 - 12: iI11I1II1I1I . iIi1i1ii1 . Ii1I % oOo0O0Ooo . IIiIiII11i . oo0oO00
def IIi1ii1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for o0O0O0ooo0oOO in IIIII11I1IiI :
  if '=m' in o0O0O0ooo0oOO :
   I1Ii ( o0O0O0ooo0oOO )
  elif 'php' in o0O0O0ooo0oOO :
   IIi1ii1 ( url )
  else :
   I1 = O000oo ( o0O0O0ooo0oOO )
   IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for I1Ii11iiiI in IIIII11I1IiI :
    I1Ii ( o0O0O0ooo0oOO )
    if 44 - 44: iI11I1II1I1I . Ii1I + O00OOo00oo0o . IIiIi1iI
    if 7 - 7: Ii1I + iI11I1II1I1I * iiII11i1I1IIi * iiII11i1I1IIi / IIiIiII11i - iIi1i1ii1
    if 65 - 65: oo0oO00 + OOooOOo + IIiIiII11i
def oOOoo ( url ) :
 I1 = O000oo ( url )
 i1I1iIii11 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for OOoO000 , oOoO0O0oO in i1I1iIii11 :
  print 'there ><><><><><><><><><><><><'
  OOoO000 = OOoO000
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oOoO0O0oO ) )
  for I1111i , oOOoO in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + OOoO000 + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + oOOoO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
 I11o0oO00oO0o0o0 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for OOoO000 , oOo0Oo0O0O in I11o0oO00oO0o0o0 :
  print 'there ><><><><><><><><><><><><'
  OOoO000 = OOoO000
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oOo0Oo0O0O ) )
  for I1111i , oOOoO in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + OOoO000 + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + oOOoO + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
   if 48 - 48: I1ii11iIi11i - IIiIi1iI + I1ii11iIi11i - oOo0O0Ooo * Ii . OooOO000
   if 35 - 35: OOoOoo . o0o00Oo0O + I1ii11iIi11i + IIi + ooOoO0O00
   if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
def oO0OoO00o ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
 for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
  I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for I1111i in I1111i :
   I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  IIi1iiii1iI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for IIi1iiii1iI in IIi1iiii1iI :
   IIi1iiii1iI = 'http:' + IIi1iiii1iI
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , '' , '' )
  if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
  if 58 - 58: IIi . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
  if 50 - 50: OooOO000 % IIiIiII11i - IIiIi1iI . ooOoO0O00 + o0o00Oo0O % OooOO000
  if 10 - 10: OooOO000 . ooOoO0O00 + iIi1i1ii1
def oOo ( url ) :
 if 66 - 66: oO0o % I11i
 iI1ii11Ii = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for o0O0O0ooo0oOO , o00O0O , I1111i , O0OO0OO in IIIII11I1IiI :
  I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O000oo ( o0O0O0ooo0oOO )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for i1ii , i11iiiiI1i in i1I :
   Ooo0oO = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( i11iiiiI1i ) )
   for iIiiii in Ooo0oO :
    if I1111i in iI1ii11Ii :
     pass
    else :
     OOiIiIIi1 ( I1111i , i1ii , 8043 , o00O0O , o00O0O , iIiiii )
     I1I11i ( 'movies' , 'INFO' )
     iI1ii11Ii . append ( I1111i )
     if 32 - 32: ooOoO0O00 . OooOO000 + IIiIiII11i - oO0o - iI11I1II1I1I
     if 20 - 20: OOooOOo % Ii1I
def IiiIi11Ii1iI1 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , Iiii1iI1i , iIiiii , o0ooooO0o0O , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10065 , Iiii1iI1i , o0ooooO0o0O , iIiiii )
 I1I11i ( 'movies' , 'INFO' )
 if 91 - 91: IIi + O00OOo00oo0o . iiII11i1I1IIi
def i1I111i1ii ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0o0oO0O000o = 'https://www.youtube.com/results?search_query=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 iiIii1I = OO0o0oO0O000o . lower ( )
 I1 = O000oo ( iiIii1I )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for oO0o0 in next :
  oO0o0 = 'https://www.youtube.com' + oO0o0
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , oO0o0 , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for o00O0O , oO0o0 , I1111i , oO0oOoo0O , i11iiiiI1i in IIIII11I1IiI :
  oOoOooOo0o0 . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  IIi1iiii1iI = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IIi1iiii1iI
  oO0o0 = 'http://www.youtube.com' + oO0o0
  OOiIiIIi1 ( '[COLORred]' + oO0oOoo0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , IIi1iiii1iI , i11iiiiI1i )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for o00O0O , oO0o0 , I1111i , oO0oOoo0O in IIIII11I1IiI :
   print 'im doing it'
   I1I11i ( 'tvshows' , 'INFO' )
   IIi1iiii1iI = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   oO0o0 = 'http://www.youtube.com' + oO0o0
   if '&' in oO0o0 :
    print ' i got here'
    I1 = O000oo ( oO0o0 )
    I11o0oO00oO0o0o0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oO0o0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for oO0o0 in oO0o0 :
      oO0o0 = 'https://www.youtube.com/w' + oO0o0
     IIi1iiii1iI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for IIi1iiii1iI in IIi1iiii1iI :
      IIi1iiii1iI = 'http:' + IIi1iiii1iI
     OOiIiIIi1 ( '[COLORred]' + oO0oOoo0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , O0o0Oo , '' )
   elif I1111i in oOoOooOo0o0 :
    pass
   elif 'user' in oO0o0 or 'elete' in I1111i :
    pass
   elif 'hannel' in oO0o0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oO0o0
    I1 = O000oo ( oO0o0 )
    II1iI11 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for o00O0O , oO0o0 , I1111i in II1iI11 :
     if 'outube' in oO0o0 or 'list' in oO0o0 :
      pass
     elif 'atch' in oO0o0 :
      oO0o0 = ( oO0o0 ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + oO0oOoo0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + oO0oOoo0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , IIi1iiii1iI , '' )
    if 88 - 88: iiII11i1I1IIi + Ii % oo0oO00 * IIi * IIi * iIi1i1ii1
def I1I1i ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for o00O0O , url , I1111i , oO0oOoo0O , i11iiiiI1i in IIIII11I1IiI :
  oOoOooOo0o0 . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  IIi1iiii1iI = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IIi1iiii1iI
  url = 'http://www.youtube.com' + url
  OOiIiIIi1 ( '[COLORred]' + oO0oOoo0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , IIi1iiii1iI , i11iiiiI1i )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for o00O0O , url , I1111i , oO0oOoo0O in IIIII11I1IiI :
   I1I11i ( 'tvshows' , 'INFO' )
   IIi1iiii1iI = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    I1 = O000oo ( url )
    I11o0oO00oO0o0o0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     IIi1iiii1iI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for IIi1iiii1iI in IIi1iiii1iI :
      IIi1iiii1iI = 'http:' + IIi1iiii1iI
     OOiIiIIi1 ( '[COLORred]' + oO0oOoo0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , O0o0Oo , '' )
   elif I1111i in oOoOooOo0o0 :
    pass
   elif 'user' in url or 'elete' in I1111i :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O000oo ( url )
    II1iI11 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for o00O0O , url , I1111i in II1iI11 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + oO0oOoo0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + oO0oOoo0O + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , IIi1iiii1iI , '' )
    if 87 - 87: O00OOo00oo0o + IIiIi1iI + o0o00Oo0O / ooOoO0O00 % OOoOoo / O00OOo00oo0o
    if 64 - 64: oO0o % OOoOoo . O00OOo00oo0o % oO0o + iiII11i1I1IIi * OOoOoo
def iiI11Iii ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  OOOO00OooO = open ( IIIii1II1II )
  IIIII11I1IiI = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( OOOO00OooO ) )
  for OOOiI1 , O00oO0o000oO in IIIII11I1IiI :
   if OOOiI1 == 'needs replacing' or O00oO0o000oO == 'needs replacing' :
    I1i11II11i1iI ( )
    if 43 - 43: I1ii11iIi11i . O00OOo00oo0o
  iiOOooooO0Oo ( '[COLOR' + II + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o , 60004 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
def I1I1i1i ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"username":"(.+?)"' ) . findall ( i1Oo00 )
 OOOooo0OooOoO = re . compile ( '"status":"(.+?)"' ) . findall ( i1Oo00 )
 i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1Oo00 )
 ooOoO00 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( i1Oo00 )
 Iii1I1111ii = re . compile ( '"created_at":"(.+?)"' ) . findall ( i1Oo00 )
 oOoOOOo = re . compile ( '"max_connections":"(.+?)"' ) . findall ( i1Oo00 )
 i1II11II1 = re . compile ( '"is_trial":"1"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  OoO ( 'My GTV Account Information' , '' , '' , oOOOo00O00oOo + 'MyAcc.png' )
  OoO ( 'Username:  %s' % ( url ) , '' , '' , oOOOo00O00oOo + 'MyAcc.png' )
 for url in OOOooo0OooOoO :
  OoO ( 'Status:  %s' % ( url ) , '' , '' , oOOOo00O00oOo + 'MyAcc.png' )
 for url in Iii1I1111ii :
  OOo0O = datetime . fromtimestamp ( float ( Iii1I1111ii [ 0 ] ) )
  OOo0O . strftime ( '%Y-%m-%d %H:%M:%S' )
  OoO ( 'Created:  %s' % ( OOo0O ) , '' , '' , oOOOo00O00oOo + 'MyAcc.png' )
 for url in i1I :
  OOo0O = datetime . fromtimestamp ( float ( i1I [ 0 ] ) )
  OOo0O . strftime ( '%Y-%m-%d %H:%M:%S' )
  OoO ( 'Expires:  %s' % ( OOo0O ) , '' , '' , oOOOo00O00oOo + 'MyAcc.png' )
 for url in ooOoO00 :
  OoO ( 'Active Connection:  %s' % ( url ) , '' , '' , oOOOo00O00oOo + 'MyAcc.png' )
 for url in oOoOOOo :
  OoO ( 'Max Connection:  %s' % ( url ) , '' , '' , oOOOo00O00oOo + 'MyAcc.png' )
 for url in i1II11II1 :
  OoO ( 'Trial: Yes' , '' , '' , oOOOo00O00oOo + 'MyAcc.png' )
 OoO ( '' , '' , '' , '' )
 OoO ( '' , '' , '' , '' )
 OoO ( 'Sign up' , '' , 50006 , '' )
 if 100 - 100: oO0o % oO0o
def iI1I1 ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOOO + ")" )
 I1i11II11i1iI ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 46 - 46: iI11I1II1I1I
def I111iiiii1 ( ) :
 iiOOooooO0Oo ( 'Full List' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'PPV' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Entertainment' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Factual' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Movie Channels' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'US Movie Channels TEST' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Kids' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Music' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'UK Sports' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'International Sports' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'US Sports Live Event/Ticket/Pass' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'News UK & International' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'German' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Arabic' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'TV Series Latest' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'VOD Latest' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'VOD Bollywood' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
def OO0ooOoOO0OOo ( ) :
 OooOoooo0000 = 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o
 I1ii1i11i = urllib2 . Request ( OooOoooo0000 , headers = { "Accept" : "application/xml" } )
 O00O0oOO00O00 = urllib2 . urlopen ( I1ii1i11i )
 if O00O0oOO00O00 and O00O0oOO00O00 . getcode ( ) == 200 :
  Oooooo0O00o = [ ]
  II11ii1 = ElementTree . parse ( O00O0oOO00O00 )
  ii1II1II = II11ii1 . getroot ( )
  for II1iI11 in II11ii1 . findall ( "channel" ) :
   i11i11II11i = II1iI11 . find ( 'title' ) . text
   i11i11II11i = base64 . b64decode ( i11i11II11i )
   i11i11II11i = i11i11II11i . partition ( "[" )
   II1Ii1I1i = i11i11II11i [ 1 ] + i11i11II11i [ 2 ]
   II1Ii1I1i = II1Ii1I1i . partition ( "]" )
   II1Ii1I1i = II1Ii1I1i [ 2 ]
   II1Ii1I1i = II1Ii1I1i . partition ( "   " )
   II1Ii1I1i = II1Ii1I1i [ 2 ]
   if 74 - 74: Ii1I * Ii / oOo0O0Ooo - o0o00Oo0O . IIiIi1iI
   i11i = II1iI11 . find ( "description" ) . text
   if i11i :
    i11i = base64 . b64decode ( i11i )
    oo0OoOO0o0o = i11i . partition ( "(" )
    oo0OoOO0o0o = "NOW:  " + oo0OoOO0o0o [ 0 ]
    OO0OOO00 = i11i . partition ( ")\n" )
    OO0OOO00 = OO0OOO00 [ 2 ] . partition ( "(" )
    OO0OOO00 = "NEXT:  " + OO0OOO00 [ 0 ]
    ooOOo0o = oo0OoOO0o0o + OO0OOO00
   else :
    ooOOo0o = ""
   Oooooo0O00o . append ( { 'title' : i11i11II11i [ 0 ] , 'cs' : II1Ii1I1i , 'schedule' : ooOOo0o } )
 return Oooooo0O00o
def IiI1Iii1 ( name ) :
 if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
 OooOo = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , o00O0O , oOo0I1Ii11i , oO0o0 in IIIII11I1IiI :
  if OooOo == 'Full List' :
   oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
   if 19 - 19: OOoOoo - I11i . iI11I1II1I1I . OOooOOo / IIi
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
  else :
   OooOo = ( OooOo ) . replace ( 'World' , 'القنوات العربية' )
   if OooOo in oOo0I1Ii11i :
    oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
    print oO0o0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    if 87 - 87: OOooOOo - IIiIi1iI - IIi + I1ii11iIi11i % iI11I1II1I1I / Ii
    OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
   else :
    pass
    if 12 - 12: IIiIi1iI
def oOOO0ooOO ( name ) :
 OooOo = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , o00O0O , oO0o0 in IIIII11I1IiI :
  oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
  OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
 else :
  OOiIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 3 - 3: ii
  if 71 - 71: OOoOoo + ooOoO0O00 - OooOO000 - Ii . iiII11i1I1IIi - IIiIi1iI
  if 85 - 85: Ii1I - OOooOOo / Ii1I + IIi - OooOO000
  if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + O00OOo00oo0o
  if 35 - 35: IIiIiII11i . oOo0O0Ooo / ooOoO0O00 / oOo0O0Ooo * oo0oO00
  if 85 - 85: IIiIiII11i . IIiIi1iI % IIi % iiII11i1I1IIi
  if 80 - 80: oo0oO00 * iiII11i1I1IIi / iI11I1II1I1I % oo0oO00 / iI11I1II1I1I
  if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * OooOO000 . Ii * o0o00Oo0O
  if 44 - 44: ooOoO0O00 . oOo0O0Ooo / Ii + OOoOoo
  if 27 - 27: IIi
  if 52 - 52: O00OOo00oo0o % OOooOOo + iI11I1II1I1I * oo0oO00 . iIi1i1ii1
  if 95 - 95: iI11I1II1I1I . OOoOoo - ii * oO0o / I11i
def oo000o0000oO ( ) :
 iiOOooooO0Oo ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  iiOOooooO0Oo ( 'Backup Genie Favourites' , oO0o0 , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( O0Oo000ooO00 ) :
  iiOOooooO0Oo ( 'Backup Ivue Config' , O0Oo000ooO00 , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( oO0 ) :
  iiOOooooO0Oo ( 'Backup Kodi Favourites' , oO0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 74 - 74: oo0oO00
  if 34 - 34: OooOO000
  if 44 - 44: ooOoO0O00 % oOo0O0Ooo % I11i
zip = oo00 . getSetting ( 'zip' )
iIIi1Ii1III = xbmc . translatePath ( os . path . join ( zip ) )
def Oooo00 ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 9 - 9: ii * o0o00Oo0O
  if 76 - 76: O00OOo00oo0o - oo0oO00 . IIi % I11i
  if 30 - 30: Ii1I % iiII11i1I1IIi / O00OOo00oo0o
def i11IiI1I ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Ii1iIiII1ii1
  elif 'Ivue' in name :
   url = O0Oo000ooO00
  elif 'Kodi' in name :
   url = oO0
  Oooo00 ( )
  OOoooO00o0o = open ( url ) . read ( )
  I1ii1Ii1 = os . path . join ( iIIi1Ii1III , description . split ( 'Your ' ) [ 1 ] )
  oooOo0OOOoo0 = open ( I1ii1Ii1 , mode = 'w' )
  oooOo0OOOoo0 . write ( OOoooO00o0o )
  oooOo0OOOoo0 . close ( )
 else :
  if 'guisettings.xml' in description :
   OoOoO = open ( os . path . join ( iIIi1Ii1III , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   iI111I1III = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIIII11I1IiI = re . compile ( iI111I1III ) . findall ( OoOoO )
   for type , i111IiiI1Ii , OooOOOOOo in IIIII11I1IiI :
    OooOOOOOo = OooOOOOOo . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , i111IiiI1Ii , OooOOOOOo ) )
  else :
   I1ii1Ii1 = os . path . join ( url )
   OOoooO00o0o = open ( os . path . join ( iIIi1Ii1III , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oooOo0OOOoo0 = open ( I1ii1Ii1 , mode = 'w' )
   oooOo0OOOoo0 . write ( OOoooO00o0o )
   oooOo0OOOoo0 . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 50 - 50: O00OOo00oo0o + IIiIi1iI + OooOO000
 if 15 - 15: iiII11i1I1IIi
 if 13 - 13: iI11I1II1I1I * OOooOOo / O00OOo00oo0o % IIiIi1iI + oo0oO00
 if 41 - 41: Ii1I
def i1iI1i ( ) :
 o0o0OoO0OOO0 = 1
 Oooo00 ( )
 oO0OOOO0o0 = xbmc . translatePath ( os . path . join ( iIIi1Ii1III , 'Build Backup' , 'Full Backup' , '' ) )
 oOO0 = xbmc . translatePath ( os . path . join ( iIIi1Ii1III , 'Build Backup' , 'my_full_backup.zip' ) )
 O00O00OoO = xbmc . translatePath ( os . path . join ( iIIi1Ii1III , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oO0OOOO0o0 ) :
  os . makedirs ( oO0OOOO0o0 )
 IiIiI1i1 = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not IiIiI1i1 ) : return False , 0
 i11i11II11i = IiIiI1i1
 ii11I1IIi1i = xbmc . translatePath ( os . path . join ( oO0OOOO0o0 , i11i11II11i + '.zip' ) )
 iiiiiiiiiiIi = [ 'plugin.video.GenieTv' ]
 ooiiI1ii = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 O0OooOO = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 i1i1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 o0oOoOo0 = "Creating full backup of existing build"
 III1IiI1i1i = "Creating Community Build"
 o0OOOOOo0 = "Archiving..."
 oooOoO = ""
 O0Oo0 = "Please Wait"
 iIIIi1IiI11I1 ( Oo0o0000o0o0 , ii11I1IIi1i , III1IiI1i1i , o0OOOOOo0 , oooOoO , O0Oo0 , O0OooOO , i1i1 )
 time . sleep ( 1 )
 O0Ooo000 = xbmc . translatePath ( os . path . join ( oO0OOOO0o0 , i11i11II11i + '_guisettings.zip' ) )
 IIi11iI1Iii = zipfile . ZipFile ( O0Ooo000 , mode = 'w' )
 try :
  IIi11iI1Iii . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 IIi11iI1Iii . close ( )
 if o0o0OoO0OOO0 == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + oOO0 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + ii11I1IIi1i + '[/COLOR]' )
  if 29 - 29: o0o00Oo0O + oOo0O0Ooo - ooOoO0O00 % I1ii11iIi11i + O00OOo00oo0o / iiII11i1I1IIi
def iIIIi1IiI11I1 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iI1IIIII1Ii = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iIiI1 = len ( sourcefile )
 I1IiII1I1i1I1 = [ ]
 II11iiI = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for iiIi , OooooOo , IIIiiiIiI in os . walk ( sourcefile ) :
  for file in IIIiiiIiI :
   II11iiI . append ( file )
 OO0OOoooo0o = len ( II11iiI )
 for iiIi , OooooOo , IIIiiiIiI in os . walk ( sourcefile ) :
  OooooOo [ : ] = [ IiIi1Ii for IiIi1Ii in OooooOo if IiIi1Ii not in exclude_dirs ]
  IIIiiiIiI [ : ] = [ oooOo0OOOoo0 for oooOo0OOOoo0 in IIIiiiIiI if oooOo0OOOoo0 not in exclude_files ]
  for file in IIIiiiIiI :
   I1IiII1I1i1I1 . append ( file )
   iiIIiI11II1 = len ( I1IiII1I1i1I1 ) / float ( OO0OOoooo0o ) * 100
   o0oOoO00o . update ( int ( iiIIiI11II1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   oooOo = os . path . join ( iiIi , file )
   if not 'temp' in OooooOo :
    if not 'plugin.program.originwizard' in OooooOo :
     import time
     oOoO0Oo0 = '01/01/1980'
     i11i11i = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( oooOo ) ) )
     if i11i11i > oOoO0Oo0 :
      iI1IIIII1Ii . write ( oooOo , oooOo [ iIiI1 : ] )
 iI1IIIII1Ii . close ( )
 o0oOoO00o . close ( )
 if 31 - 31: Ii + IIi - o0o00Oo0O
 if 51 - 51: oO0o * ooOoO0O00 / iIi1i1ii1 * IIi + IIiIi1iI % Ii1I
def Ii11i1I11i ( ) :
 IIiiiI1iIII ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 if 34 - 34: oo0oO00 * ii + iIi1i1ii1 + Ii
 if 22 - 22: ooOoO0O00
def I11io0Oo ( ) :
 IIiiiI1iIII ( )
 i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  I1i1iiiI1 ( )
 if i11I1II1I11i == 1 :
  ii1I ( )
 if i11I1II1I11i == 2 :
  O00Oo ( )
 if i11I1II1I11i == 3 :
  i1I111i1ii ( )
  if 4 - 4: IIiIiII11i
  if 20 - 20: Ii % ii . OOoOoo / iiII11i1I1IIi
  if 34 - 34: Ii / O00OOo00oo0o * IIi . I1ii11iIi11i
  if 79 - 79: O00OOo00oo0o
  if 31 - 31: IIi % O00OOo00oo0o
  if 98 - 98: OOoOoo * iI11I1II1I1I . iIi1i1ii1 * I1ii11iIi11i / Ii1I + IIiIi1iI
  if 25 - 25: oo0oO00
  if 19 - 19: oOo0O0Ooo % iIi1i1ii1 . OOoOoo * IIiIi1iI
  if 89 - 89: OOooOOo . IIi
def IIIIIiI11Ii ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   OOoOooOoOOOoo ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , Iiii1iI1i , I1111i )
  if i11I1II1I11i == 1 :
   I11I1IIiiII1 ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if i11I1II1I11i == 2 :
   Iiii1Ii1I ( )
  if i11I1II1I11i == 3 :
   oooOOOOOi1iIii ( )
  if i11I1II1I11i == 4 :
   o0O0ooooooo00 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if i11I1II1I11i == 5 :
   I1111ii11IIII ( )
  if i11I1II1I11i == 6 :
   IiIi1II111I ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if i11I1II1I11i == 7 :
   o00o ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if i11I1II1I11i == 8 :
   IIi1i1 ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if i11I1II1I11i == 9 :
   o0O0Ooo ( )
  if i11I1II1I11i == 10 :
   O0oO00oOOooO ( )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , oOOOo00O00oOo + 'Rays-Ravers.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 90037 , oOOOo00O00oOo + 'Quicksilver.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RadioNomy[/COLOR]' , '' , 70001 , oOOOo00O00oOo + 'RadioNomy.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30031 , oOOOo00O00oOo + 'MusicChannels.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , oOOOo00O00oOo + 'UKRadio.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']WORLD RADIO[/COLOR]' , str ( ooOO0O0ooOooO ) , 1013 , oOOOo00O00oOo + 'WorldRadio.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , oOOOo00O00oOo + 'Concerts.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC[/COLOR]' , str ( ooOO0O0ooOooO ) , 1030 , oOOOo00O00oOo + 'MUSIC.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , oOOOo00O00oOo + 'MusicVideos.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC[/COLOR]' , str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , oOOOo00O00oOo + 'Music.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 1111 , oOOOo00O00oOo + 'MusicSearch.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , O0o0Oo , '' )
  if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
 I1I11i ( 'movies' , 'MAIN' )
 if 66 - 66: o0o00Oo0O
def oOooOOo00ooO ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   o0OO0oooo ( )
  if i11I1II1I11i == 1 :
   iiIiIIIiiI ( )
  if i11I1II1I11i == 2 :
   oOOo0O00o ( )
  if i11I1II1I11i == 3 :
   I11II1i1 ( oO0o0 )
  if i11I1II1I11i == 4 :
   IiI1ii11I1 ( oO0o0 )
  if i11I1II1I11i == 5 :
   O0O0ooOOO ( )
  if i11I1II1I11i == 6 :
   I1i1iI ( url = 'http://www.iplocation.net/' , inc = 1 )
  if i11I1II1I11i == 7 :
   I1iI1I1ii1 ( )
 else :
  OOiIiIIi1 ( 'CLLEANUP' , 'url' , 9666 , oOOOo00O00oOo + 'MAIN5.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']KILL KODI[/COLOR]' , '' , 80000 , oOOOo00O00oOo + 'KillKodi.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '' , 50004 , oOOOo00O00oOo + 'Speedtest.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , oOOOo00O00oOo + 'View-Log-File.png' , O0o0Oo , '' )
  OOiIiIIi1 ( 'DELETE CACHE' , 'url' , 14 , oOOOo00O00oOo + 'DeleteCache.png' , O0o0Oo , '' )
  OOiIiIIi1 ( 'DELETE PACKAGES' , 'url' , 6 , oOOOo00O00oOo + 'DeletePackages.png' , O0o0Oo , '' )
  OOiIiIIi1 ( 'FORCE REFRESH' , 'url' , 10 , oOOOo00O00oOo + 'ForceRefresh.png' , O0o0Oo , 'Force Refresh All Repos' )
  iiOOooooO0Oo ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , oOOOo00O00oOo + '1.jpg' , O0o0Oo , 'Fix Corrupt Database' )
  OOiIiIIi1 ( 'CHECK MY IP' , 'url' , 12 , oOOOo00O00oOo + 'CheckMyIP.png' , O0o0Oo , '' )
  OOiIiIIi1 ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , oOOOo00O00oOo + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , O0o0Oo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 33 - 33: I11i / o0o00Oo0O + IIi
  if 75 - 75: OOoOoo % Ii + iI11I1II1I1I
 I1I11i ( 'movies' , 'MAIN' )
 if 92 - 92: OOooOOo % o0o00Oo0O
 if 55 - 55: iI11I1II1I1I * OooOO000
def i1i1II ( ) :
 IIiiiI1iIII ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , oOOOo00O00oOo + 'repos.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']NEW[/COLOR]' , str ( ooOO0O0ooOooO ) , 22 , oOOOo00O00oOo + 'NEW.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']IPTV[/COLOR]' , str ( ooOO0O0ooOooO ) , 23 , oOOOo00O00oOo + 'IPTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']VIDEO[/COLOR]' , str ( ooOO0O0ooOooO ) , 24 , oOOOo00O00oOo + 'VIDEO.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SPORTS[/COLOR]' , str ( ooOO0O0ooOooO ) , 25 , oOOOo00O00oOo + 'SPORTS.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']KIDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 26 , oOOOo00O00oOo + 'KIDS.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']MUSIC[/COLOR]' , str ( ooOO0O0ooOooO ) , 27 , oOOOo00O00oOo + 'MUSIC.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']PROGRAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 28 , oOOOo00O00oOo + 'PROGRAMS.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']XXX[/COLOR]' , 'URL' , 29 , oOOOo00O00oOo + 'XXX.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 85 - 85: iI11I1II1I1I . IIiIiII11i
 if 54 - 54: iIi1i1ii1 . ii % I1ii11iIi11i
def ii111I11Ii ( ) :
 IIiiiI1iIII ( )
 OOiIiIIi1 ( 'CHECK ADVANCED XML' , str ( ooOO0O0ooOooO ) , 8 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'MUCKYS XML' , str ( ooOO0O0ooOooO ) + '/wizard/muckys.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '0CACHE XML' , str ( ooOO0O0ooOooO ) + '/wizard/0cache.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'MIKEY1234 XML' , str ( ooOO0O0ooOooO ) + '/wizard/mikey.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'TUXENS XML' , str ( ooOO0O0ooOooO ) + '/wizard/tuxens.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'P2P RECOMMENDED XML1' , str ( ooOO0O0ooOooO ) + '/wizard/p2p1.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'P2P RECOMMENDED XML2' , str ( ooOO0O0ooOooO ) + '/wizard/p2p2.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'DELETE XML' , str ( ooOO0O0ooOooO ) , 11 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 6 - 6: iIi1i1ii1
def iI1i111I1Ii ( ) :
 IIiiiI1iIII ( )
 OOiIiIIi1 ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 77 - 77: ooOoO0O00 + oO0o . oOo0O0Ooo * IIi / OOoOoo / iIi1i1ii1
def oOoo ( ) :
 IIiiiI1iIII ( )
 OOiIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , O0o0Oo , '' )
 if 57 - 57: I11i / O00OOo00oo0o
 if 13 - 13: ii + oO0o
 if 32 - 32: o0o00Oo0O + oo0oO00 % I1ii11iIi11i
def Iii1IIII11I ( ) :
 IIiiiI1iIII ( )
 i1Oo0oO00o = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  iI1iI ( )
 if i11I1II1I11i == 0 :
  O0O0 ( oO0o0 )
 if i11I1II1I11i == 0 :
  O0oO0o0OOOOOO ( oO0o0 )
  if 24 - 24: ooOoO0O00 * OOoOoo - iiII11i1I1IIi / iIi1i1ii1
  if 62 - 62: I1ii11iIi11i
  if 30 - 30: ooOoO0O00
 I1I11i ( 'movies' , 'MAIN' )
 if 4 - 4: O00OOo00oo0o - oOo0O0Ooo % oo0oO00 / I11i % oo0oO00 * IIiIiII11i
def IiI1I ( ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1Oo00 )
 for o00O0O , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , o00O0O , o00O0O , '' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 25 - 25: oo0oO00 % oOo0O0Ooo + Ii + o0o00Oo0O * ii
def ooO0 ( url ) :
 i1Oo00 = O000oo ( o0Iiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 45 - 45: iIi1i1ii1 / IIiIi1iI . ii + oO0o
def iI1iI ( ) :
 IIiiiI1iIII ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 51 - 51: OooOO000 % Ii % OOoOoo + O00OOo00oo0o % Ii1I
def IIIIIiiiiI1I ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OOOOOOo0OOoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 92 - 92: OOooOOo - IIi % O00OOo00oo0o - ooOoO0O00 % Ii
def O0OoO0oO00 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + I1II1IiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 26 - 26: IIi * I1ii11iIi11i
def i1iI1Ii11Ii1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o0OoO0oo0O0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 6 - 6: IIiIiII11i % O00OOo00oo0o
def I1iiIiIII ( url ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 68 - 68: o0o00Oo0O
def O0O0 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o0oOoO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 40 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 94 - 94: oO0o + OOoOoo + IIiIi1iI
def OOoOooO00 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o0o00OOOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 42 - 42: IIiIi1iI * OooOO000
def OooOoOO0 ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  i1iIIiI1111 ( )
 if i11I1II1I11i == 1 :
  OooOO ( )
 if i11I1II1I11i == 2 :
  O0oOoOoOoo0OoO0 ( )
  if 17 - 17: iIi1i1ii1 * IIiIiII11i / OOoOoo + iI11I1II1I1I . iiII11i1I1IIi - o0o00Oo0O
  if 70 - 70: iIi1i1ii1 * oo0oO00 - iiII11i1I1IIi + I1ii11iIi11i % Ii1I - OOoOoo
  if 81 - 81: o0o00Oo0O . o0o00Oo0O
  if 75 - 75: iI11I1II1I1I % OOoOoo + Ii1I * o0o00Oo0O . OooOO000 - IIiIi1iI
def OooOO ( ) :
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( iIIII )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , i1IIiIIIi1 in IIIII11I1IiI :
  oo000ii ( 'Android Apps' + i1IIiIIIi1 , 'https://www.apkfiles.com' + oO0o0 , 30035 , oOOOo00O00oOo + 'apps.png' )
 for oO0o0 , i1IIiIIIi1 in i1I :
  oo000ii ( 'Android Games' + i1IIiIIIi1 , 'https://www.apkfiles.com' + oO0o0 , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 I1I11i ( 'movies' , 'MAIN' )
def oOoO00O ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '/cat' in url :
   oo000ii ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def I11I1I1i1i ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '/app' in url :
   oo000ii ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def Oo0oOO0O00 ( url ) :
 iIIII = O000oo ( url )
 Oo0O = url
 if "page=" in str ( url ) :
  Oo0O = url . split ( '?' ) [ 0 ]
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  if 'apk' in url :
   OOiIiIIi1 ( ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + o00O0O )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 OOiIiIIi1 ( 'Next Page' , Oo0O + str ( i1I ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def o00OOo0o0O ( name , url ) :
 iIIII = oo00ooOoO00 ( url )
 name = name
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  I111Iii1 ( name , url , 'Brackets' )
def O0oOoOoOoo0OoO0 ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0o0oO0O000o = 'https://www.apkfiles.com/search?q=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' ) + '&search_type=1'
 iiIii1I = OO0o0oO0O000o . lower ( )
 Oo0oOO0O00 ( iiIii1I )
 if 30 - 30: ooOoO0O00
def O0Oo0O00o0oo0OO ( url ) :
 o00O0 = xbmc . translatePath ( os . path . join ( OooO00 , 'Download' ) )
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
 if 66 - 66: iIi1i1ii1 % iIi1i1ii1 - OOoOoo
def oOooO0OoO ( url ) :
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
 if 58 - 58: iIi1i1ii1 % ii
 if 49 - 49: Ii1I + o0o00Oo0O . iIi1i1ii1 * ii
def oO0OOO00 ( name , url , description ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , name )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 I1iIiI1iiiiI1 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print I1iIiI1iiiiI1
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , I1iIiI1iiiiI1 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 4 - 4: I1ii11iIi11i - oO0o - Ii * O00OOo00oo0o / iIi1i1ii1 - IIi
 if 45 - 45: I11i % I1ii11iIi11i * ooOoO0O00 - o0o00Oo0O
 if 82 - 82: IIiIiII11i / OooOO000
 if 96 - 96: I1ii11iIi11i / oo0oO00 . IIiIiII11i . I1ii11iIi11i
 if 91 - 91: IIiIiII11i . IIi + I11i
def i1iIIiI1111 ( ) :
 i1Oo00 = O000oo ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1Oo00 )
 for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O , I1iII1IIi1IiI in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , oO0o0 , 80003 , iiO0oOo00o , oOOOo00O00oOo + 'APKToolsB.png' , I1iII1IIi1IiI )
def iIi ( apk , ret = None ) :
 if apk == "kodi" :
  oo0ooO = "https://kodi.tv/download/"
  i1Oo00 = O000oo ( oo0ooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1Oo00 )
  if len ( IIIII11I1IiI ) == 1 :
   o0ooOO00OO0o0O = IIIII11I1IiI [ 0 ] [ 0 ]
   i11i11II11i = IIIII11I1IiI [ 0 ] [ 1 ]
   III1IiiIiiI1i = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( o0ooOO00OO0o0O , i11i11II11i )
  if ret == 'version' : return o0ooOO00OO0o0O
  else : return III1IiiIiiI1i
 elif apk == "spmc" :
  OoO0o00OoO = 'https://github.com/koying/SPMC/releases/latest/'
  i1Oo00 = O000oo ( OoO0o00OoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1Oo00 )
  o0ooOO00OO0o0O = re . sub ( '<[^<]+?>' , '' , IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  III1IiiIiiI1i = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( o0ooOO00OO0o0O , o0ooOO00OO0o0O )
  if ret == 'version' : return o0ooOO00OO0o0O
  else : return III1IiiIiiI1i
def I111Iii1 ( name , url , Brackets ) :
 if I1IIII1i ( ) == 'android' :
  Oo00Oooo00o = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not Oo00Oooo00o : II11II1I ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  O0OO00000o00 = name
  if Oo00Oooo00o :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not Iii1 ( url ) == True : II11II1I ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % O0OO00000o00 , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    IIi11iI1Iii = zipfile . ZipFile ( oOO0O00Oo0O0o )
    for file in IIi11iI1Iii . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as oooOo0OOOoo0 :
       OOO000Oo = file . split ( '/' ) [ 1 ]
       oooOo0OOOoo0 . write ( IIi11iI1Iii . read ( file ) )
       xbmc . sleep ( 500 )
       oooOo0OOOoo0 . close ( )
       try :
        os . remove ( oOO0O00Oo0O0o )
       except :
        pass
       oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , OOO000Oo )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : II11II1I ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : II11II1I ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 8 - 8: IIiIi1iI - I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * iIi1i1ii1 - iI11I1II1I1I
 if 30 - 30: iiII11i1I1IIi / Ii1I
 if 22 - 22: oo0oO00 * OooOO000
 if 4 - 4: OOooOOo - oo0oO00 + oOo0O0Ooo
def iiIiIiIiiIiI ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1Oo00 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oO0o0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oO0o0 )
  iIi1iIII ( ( I1111i ) . replace ( '_' , ' ' ) , oO0o0 )
  if 36 - 36: ii / I1ii11iIi11i . O00OOo00oo0o % ii . IIi + IIiIiII11i
def iIi1iIII ( name , url ) :
 if I1IIII1i ( ) == 'android' :
  Oo00Oooo00o = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not Oo00Oooo00o : II11II1I ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  O0OO00000o00 = name
  if Oo00Oooo00o :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not Iii1 ( url ) == True : II11II1I ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % O0OO00000o00 , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : II11II1I ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : II11II1I ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 43 - 43: iiII11i1I1IIi % iIi1i1ii1 / I11i * O00OOo00oo0o
 if 85 - 85: iI11I1II1I1I . ii . I11i
def oO00OoO0oo ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'INFO' )
 if 52 - 52: OOoOoo % IIiIi1iI
 if 25 - 25: iiII11i1I1IIi / iiII11i1I1IIi % ii - Ii1I * oo0oO00
def oOo0 ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 30015 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 23 - 23: Ii
def OOooOoO ( url , iconimage , fanart ) :
 i1Oo00 = O000oo ( url )
 IIii1I1i = url
 o00O0O = iconimage
 fanart = fanart
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for o0O0O0ooo0oOO , I1111i in IIIII11I1IiI :
  if '.mp4' in I1111i :
   OOiIiIIi1 ( 'Watch VIDEO' , url + '/' + o0O0O0ooo0oOO , 222 , o00O0O , fanart , '' )
  if 'description' in I1111i :
   OOiIiIIi1 ( 'Read Description' , url + '/' + o0O0O0ooo0oOO , 30017 , o00O0O , fanart , '' )
  if 'images' in I1111i :
   iiOOooooO0Oo ( 'View Images' , url + '/' + o0O0O0ooo0oOO , 30018 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Android' , url + '/' + o0O0O0ooo0oOO , 30016 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Pc' , url + '/' + o0O0O0ooo0oOO , 30019 , o00O0O , fanart , '' )
 I1I11i ( 'movies' , 'INFO' )
 if 24 - 24: I11i + oOo0O0Ooo - IIiIiII11i
def iiiii1i ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  Ii1 ( url )
  if 37 - 37: Ii . Ii1I
def oO0OOOoO0o ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  o0Oo00oOO ( url )
  if 73 - 73: iiII11i1I1IIi / ii . IIiIiII11i - OOoOoo * IIiIi1iI * OOoOoo
def IiI1IiI1iiI1 ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1Oo00 )
 for O000o0 in IIIII11I1IiI :
  OO0O000 ( 'Description:' , O000o0 )
  if 39 - 39: IIiIiII11i + ii / IIi / iIi1i1ii1 * OOooOOo
def Oo0Oo ( url ) :
 i1Oo00 = O000oo ( url )
 url = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for o0O0O0ooo0oOO , I1111i in IIIII11I1IiI :
  if 'png' in I1111i :
   OOiIiIIi1 ( 'image' , '' , '' , url + '/' + o0O0O0ooo0oOO , url + '/' + o0O0O0ooo0oOO , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 5 - 5: iI11I1II1I1I . OOoOoo
def oOo0OoOOOo0 ( name , url , description ) :
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
 if 55 - 55: oo0oO00 + o0o00Oo0O / OooOO000 % IIiIi1iI / ii
 if 98 - 98: iIi1i1ii1 * iI11I1II1I1I % I1ii11iIi11i % IIi
def o0Oo00oOO ( url ) :
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
 o0OO0oooo ( )
 if 88 - 88: OooOO000 - IIiIiII11i / OooOO000 - iIi1i1ii1
def Ii1 ( url ) :
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
 o0OO0oooo ( )
 if 16 - 16: I1ii11iIi11i % O00OOo00oo0o
def i1iI ( name , url , description ) :
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
 o0OO0oooo ( )
 if 73 - 73: ii . I1ii11iIi11i / o0o00Oo0O - o0o00Oo0O
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
  IiI11IIi11Iii = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oooOo0OOOoo0 . write ( IiI11IIi11Iii . rstrip ( '\r\n' ) + '\n' )
def o0OO0oooo ( ) :
 i11I1II1I11i = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if i11I1II1I11i == 0 : return
 elif i11I1II1I11i == 1 : pass
 ii11i1I1i = I1IIII1i ( )
 iIiIi11 ( "Platform: " + str ( ii11i1I1i ) )
 os . _exit ( 1 )
 iIiIi11 ( "Force close failed!  Trying alternate methods." )
 if ii11i1I1i == 'osx' :
  iIiIi11 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif ii11i1I1i == 'linux' :
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
 elif ii11i1I1i == 'android' :
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
 elif ii11i1I1i == 'windows' :
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
  if 49 - 49: ii + ii / IIi . oo0oO00
  if 13 - 13: IIiIiII11i . OooOO000 - O00OOo00oo0o . oO0o . iI11I1II1I1I
  if 66 - 66: I1ii11iIi11i * OOoOoo
def O0oO0o0OOOOOO ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for ooo0 , OooooOo , IIIiiiIiI in os . walk ( url ) :
  for file in IIIiiiIiI :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    OoOoO = open ( ( os . path . join ( ooo0 , file ) ) ) . read ( )
    I11OOO0 = OoOoO . replace ( Oo0o0000o0o0 , 'special://home/' )
    oooOo0OOOoo0 = open ( ( os . path . join ( ooo0 , file ) ) , mode = 'w' )
    oooOo0OOOoo0 . write ( str ( I11OOO0 ) )
    oooOo0OOOoo0 . close ( )
 o0OO0oooo ( )
 if 16 - 16: OooOO000 / iI11I1II1I1I + IIi * OooOO000 * iiII11i1I1IIi
def Iiii1Ii1I ( ) :
 oo000ii ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 oo000ii ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 oo000ii ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 8 - 8: O00OOo00oo0o
def II11I ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def Iii1iIiI1I1I1 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def oOOO0OO ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1I :
  oo000ii ( ( '[COLOR' + II + ']Filter - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , o00O0O )
def I11ii1iI11 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def i11ii111i1ii ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O
 Oo0O0O = 'https://www.radionomy.com/en/search/index?query=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 I1 = O000oo ( Oo0O0O )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oO0o0 , 70005 , o00O0O )
  if 8 - 8: Ii * o0o00Oo0O + Ii1I . iI11I1II1I1I % iiII11i1I1IIi / iiII11i1I1IIi
  if 70 - 70: oOo0O0Ooo + iIi1i1ii1
def I1111ii11IIII ( ) :
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , 'http://www.listenlive.eu/' + oO0o0 , 10111113 , oOOOo00O00oOo + 'radio.png' )
def o0O0ooooooo00 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  OoO ( I1111i , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 70 - 70: OOoOoo . Ii
def O0O00O0Oo0 ( ) :
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.toonjet.com/' + oO0o0 , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoOiI11IiI1i1 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( iIIII )
 i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( iIIII )
 for url , o00O0O in IIIII11I1IiI :
  if 'ol.gif' in o00O0O :
   pass
  elif 'link_block_' in o00O0O :
   pass
  elif '.png' in o00O0O :
   pass
  else :
   oo000ii ( ( o00O0O ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOOo00O00oOo + 'vod.png' )
 for url in i1I :
  oo000ii ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOOo00O00oOo + 'Next.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 85 - 85: IIiIiII11i
  if 55 - 55: Ii1I
def O0oO00oOOooO ( ) :
 oOoo0OO0 ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 oOoo0OO0 ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 5 - 5: Ii * I1ii11iIi11i
def i111 ( ) :
 oOoo0OO0 ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 oOoo0OO0 ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 oOoo0OO0 ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 71 - 71: oO0o
def ooOOO0ooO0o ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for I1111i , oO0o0 , OO0o0O0O0O0 in IIIII11I1IiI :
  if 'Parent' in I1111i :
   pass
  elif '2' in OO0o0O0O0O0 :
   oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 34 - 34: oO0o * iIi1i1ii1 * I1ii11iIi11i
def Iioo0O00ooo0o ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for I1111i , oO0o0 , OO0o0O0O0O0 in IIIII11I1IiI :
  if OOoOOo0O00O in I1111i . lower ( ) :
   if '1' in OO0o0O0O0O0 :
    oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in OO0o0O0O0O0 :
    oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in OO0o0O0O0O0 :
    oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 29 - 29: ii . IIiIiII11i % OOooOOo
    if 26 - 26: iI11I1II1I1I - Ii1I . OOoOoo . OOoOoo + iI11I1II1I1I * I1ii11iIi11i
def O0Oo00 ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for I1111i , oO0o0 , OO0o0O0O0O0 in IIIII11I1IiI :
  if '1' in OO0o0O0O0O0 :
   oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in OO0o0O0O0O0 :
   oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in OO0o0O0O0O0 :
   oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 63 - 63: ooOoO0O00 % Ii % IIiIiII11i * ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 40 - 40: I1ii11iIi11i
def iI1Ii11 ( url ) :
 o0O0O0ooo0oOO = url
 I1 = O000oo ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
 for url , I1111i in i1I :
  if 'mp3' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in I1111i :
   oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0O0O0ooo0oOO + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 93 - 93: oOo0O0Ooo / IIiIi1iI / iiII11i1I1IIi + IIiIiII11i + Ii
   if 16 - 16: oOo0O0Ooo - oo0oO00 . I1ii11iIi11i
   if 94 - 94: OOooOOo + OOoOoo . IIiIi1iI
def oooOo00O0 ( url ) :
 I1 = O000oo ( url )
 o0O0O0ooo0oOO = url
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
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
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0O0O0ooo0oOO + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 26 - 26: O00OOo00oo0o . iIi1i1ii1 + oOo0O0Ooo . OOooOOo + IIi
   if 17 - 17: IIi + Ii + Ii1I % IIi . oo0oO00
def I11iiIi1i1IIi ( ) :
 oOoo0OO0 ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 oOoo0OO0 ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 oOoo0OO0 ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 46 - 46: oO0o . o0o00Oo0O * IIiIi1iI / I11i + ii
def i1Ii1i1I11III ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O in IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oO0o0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in o00O0O :
   pass
  else :
   oOoo0OO0 ( o00O0O , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oO0o0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + o00O0O + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 36 - 36: iIi1i1ii1 - ii . ii + Ii1I
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 55 - 55: IIi * IIiIiII11i + oo0oO00
 if 93 - 93: OooOO000 * oo0oO00 . oO0o - iIi1i1ii1 + o0o00Oo0O * oO0o
def oOoOO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 20 - 20: IIiIi1iI . oO0o * OooOO000
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 71 - 71: I1ii11iIi11i . IIiIiII11i / IIiIiII11i * iIi1i1ii1 * oO0o
def IiiI11 ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if OOoOOo0O00O in I1111i . lower ( ) :
   if '</a>' in I1111i :
    pass
   elif '(' in I1111i :
    oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 60 - 60: IIiIi1iI * IIiIi1iI / ii
    if 65 - 65: Ii1I % oo0oO00 . ii * I11i * oO0o
def II11IiI1 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 21 - 21: oO0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 63 - 63: iiII11i1I1IIi . o0o00Oo0O * iiII11i1I1IIi + iI11I1II1I1I
 if 46 - 46: ooOoO0O00 + IIiIiII11i * ooOoO0O00 - iIi1i1ii1
def Oo0OOOoOO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  o0O0O0ooo0oOO = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( o0O0O0ooo0oOO )
  if 11 - 11: o0o00Oo0O * OOooOOo
def IIii1i ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for I1111i , url in IIIII11I1IiI :
  if '<p align' in I1111i :
   pass
  elif '&nbsp;' in I1111i :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 69 - 69: O00OOo00oo0o / ii % Ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: Ii - IIiIi1iI * oo0oO00 + I11i
 if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
def Ii1111IiIi ( ) :
 I1 = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'ongoing' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , oOOOo00O00oOo + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , oOOOo00O00oOo + 'CartoonShows.png' , '' , '' )
  if 'disney' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , oOOOo00O00oOo + 'Disney.png' , '' , '' )
  if 'genre' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , oOOOo00O00oOo + 'Genre.png' , '' , '' )
  if 'years' in oO0o0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 21005 , oOOOo00O00oOo + 'Years.png' , '' , '' )
def i1iI1IIi1I ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 oo00i1i11I1I1 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , o00O0O , o00O0O , I1111i )
 for url , I1111i in oo00i1i11I1I1 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def OOOOOoooO ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 iIIII1i = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 oO0Oooo0OoO = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 Iiii1IIIIiiI11 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in oO0Oooo0OoO :
  iiOOooooO0Oo ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , I1111i in iIIII1i :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def I1iii1I ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 100 - 100: ii . I1ii11iIi11i / Ii1I
def o0Ooo0o0ooo0 ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if '9cart' in oO0o0 :
   oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 29 - 29: IIiIi1iI * IIiIiII11i * oO0o * OOoOoo
def ooo00o0OO ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( I1 )
 ooOoO00 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if '9cart' in url :
   oo000ii ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   oo000ii ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url , I1111i in ooOoO00 :
  if '9cart' in url :
   oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 32 - 32: IIi + OooOO000 + iI11I1II1I1I * I1ii11iIi11i
def ooiIii1I1111 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20003 , o00O0O )
 for url , I1111i in i1I :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 26 - 26: O00OOo00oo0o . oOo0O0Ooo . OooOO000 - ii / iI11I1II1I1I
def i111IIiIII1i ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'Watch' in url :
   oo000ii ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 74 - 74: IIiIiII11i / o0o00Oo0O
def O0oo0ooo0 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 19 - 19: ooOoO0O00
def O0oOoO0oO00O ( url ) :
 url = cloudflare . source ( url )
 I1Ii ( url )
 if 79 - 79: ii / oOo0O0Ooo
def O00 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in IIIII11I1IiI :
  I1Ii ( url )
  if 25 - 25: Ii / OOooOOo - O00OOo00oo0o / oO0o . I11i . I11i
  if 6 - 6: oo0oO00 . iiII11i1I1IIi
def II1I1iiIII1I1 ( ) :
 if 43 - 43: Ii1I + I11i
 iiOOooooO0Oo ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 50 - 50: oo0oO00 % ooOoO0O00 * o0o00Oo0O
def O00Oo ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 4 - 4: iI11I1II1I1I . ooOoO0O00
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 63 - 63: iI11I1II1I1I + OOoOoo % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
 for oO0o0 , I1111i in IIIII11I1IiI :
  if OOoOOo0O00O in I1111i . lower ( ) :
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
    iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
    if 60 - 60: I11i . OOooOOo % O00OOo00oo0o / oOo0O0Ooo / o0o00Oo0O
    if 19 - 19: Ii . oOo0O0Ooo + IIiIiII11i / IIi . Ii1I * IIiIi1iI
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 59 - 59: iI11I1II1I1I / Ii1I % IIiIi1iI
def oo0o0000Oo0 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
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
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 84 - 84: iI11I1II1I1I / oOo0O0Ooo . OOooOOo % iiII11i1I1IIi
def oOoO000 ( url ) :
 iIIII = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  Oo00o00Oo = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10007 , Oo00o00Oo )
  if 50 - 50: IIiIi1iI % I1ii11iIi11i
  if 75 - 75: oo0oO00 * IIiIi1iI
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 88 - 88: oO0o * I11i * IIi / I1ii11iIi11i * oO0o
def oOII11i1I ( url , IMAGE ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   o0Oo0ooo ( url )
   if 60 - 60: oOo0O0Ooo
   if 44 - 44: IIiIiII11i . IIiIiII11i + IIi * iIi1i1ii1
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 16 - 16: IIiIiII11i
def o0Oo0ooo ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 100 - 100: o0o00Oo0O - ooOoO0O00
  if 48 - 48: oo0oO00 % IIiIi1iI + o0o00Oo0O
  if 27 - 27: Ii1I / IIi
def o0OoOO ( ) :
 if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
 iiOOooooO0Oo ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , O0o0Oo , '' )
 if 63 - 63: OOoOoo + iI11I1II1I1I + oOo0O0Ooo + O00OOo00oo0o
def oOOoO0O ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  if 'elete' in I1111i :
   pass
  else :
   OoO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 222 , o00O0O )
   if 76 - 76: ooOoO0O00 / iI11I1II1I1I - Ii1I - IIiIiII11i
def oo00Oo ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IIiiIii11 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , oo0O , i1iII1IiiIiI1 in IIiiIii11 :
  for OOoOOo0O00O in oo0O :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   Iii1iI1iiIii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oO0o0 , I1111i in Iii1iI1iiIii :
    if 'tube' in oO0o0 :
     pass
    elif 'stage' in oO0o0 :
     OoO ( '[COLOR' + II + ']' + oo0O + '   -   ' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O , )
    elif 'vee' in oO0o0 :
     pass
     if 21 - 21: oO0o % iI11I1II1I1I . oO0o
def OO000OOOo0Oo ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IIiiIii11 = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , oo0O , i1iII1IiiIiI1 in IIiiIii11 :
  Iii1iI1iiIii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oO0o0 , I1111i in Iii1iI1iiIii :
   if 'tube' in oO0o0 :
    pass
   elif 'stage' in oO0o0 :
    OoO ( '[COLOR' + II + ']' + oo0O + '   -   ' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O )
   elif 'vee' in oO0o0 :
    pass
    if 75 - 75: IIiIiII11i + IIiIi1iI % IIi + I1ii11iIi11i
    if 70 - 70: oO0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 43 - 43: OOooOOo
def iIi1i ( url ) :
 I1 = O000oo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 i1ii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( i1ii ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in i1ii :
  OOOOo0o00OO0000 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 57 - 57: oOo0O0Ooo
  if 65 - 65: Ii - IIiIi1iI * iiII11i1I1IIi + IIiIi1iI / OOoOoo + I11i
  if 35 - 35: o0o00Oo0O + I1ii11iIi11i - oOo0O0Ooo % iIi1i1ii1 % IIiIiII11i
  if 77 - 77: O00OOo00oo0o + oo0oO00
  if 38 - 38: Ii1I - iIi1i1ii1 * I11i
  if 13 - 13: oOo0O0Ooo * oo0oO00
  if 41 - 41: OOoOoo
def iIIII1iIIii ( ) :
 if 16 - 16: iI11I1II1I1I
 o000o0o00Oo ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 o000o0o00Oo ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 62 - 62: OooOO000
 I1I11i ( 'movies' , 'MAIN' )
 if 8 - 8: OooOO000 - oOo0O0Ooo * I1ii11iIi11i % Ii1I * ii
def iii11 ( ) :
 o000o0o00Oo ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 o000o0o00Oo ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 20 - 20: IIi - OooOO000 / I1ii11iIi11i * oO0o
 I1I11i ( 'movies' , 'MAIN' )
def o00O ( ) :
 if 50 - 50: OOooOOo - oo0oO00 + iI11I1II1I1I - oO0o . I1ii11iIi11i
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 OO0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 8 - 8: iIi1i1ii1
 for i1I11iIiII in OO0 :
  OO0OO0OO = OOOO0OOoO0O0 + i1I11iIiII + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( OO0OO0OO )
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for oO0o0 , Iiii1iI1i , iIiiii , o0ooooO0o0O , I1111i in IIIII11I1IiI :
   if OOoOOo0O00O in I1111i . lower ( ) :
    iIii ( I1111i , oO0o0 , 222 , Iiii1iI1i , o0ooooO0o0O , iIiiii )
    if 95 - 95: iiII11i1I1IIi / OOoOoo . o0o00Oo0O * OOoOoo - I11i * I1ii11iIi11i
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 6 - 6: OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / iIi1i1ii1
    if 14 - 14: O00OOo00oo0o % OOoOoo - o0o00Oo0O / O00OOo00oo0o
def Oo00OOoO0oo ( ) :
 if 4 - 4: oO0o - OooOO000 / Ii * o0o00Oo0O
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 OO0 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 78 - 78: OOoOoo - iiII11i1I1IIi % o0o00Oo0O - IIi % oO0o
 for i1I11iIiII in OO0 :
  i11IiIi = OOOO0OOoO0O0 + i1I11iIiII + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( i11IiIi )
  IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for I1111i , iIiiii , oO0o0 , o00O0O , o0ooooO0o0O , Ii11iiI in IIIII11I1IiI :
   if OOoOOo0O00O in I1111i . lower ( ) :
    o000o0o00Oo ( I1111i , oO0o0 , Ii11iiI , o00O0O , o0ooooO0o0O , iIiiii )
    if 24 - 24: iiII11i1I1IIi / iIi1i1ii1 * IIiIi1iI - Ii
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 72 - 72: iI11I1II1I1I . Ii / IIi + IIiIiII11i / oo0oO00
    if 48 - 48: o0o00Oo0O
def I1I1i11 ( ) :
 if 79 - 79: I11i - IIiIiII11i
 iIIII = O000oo ( OOOO0OOoO0O0 + 'spongemain.php' )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , iIiiii , oO0o0 , o00O0O , o0ooooO0o0O , Ii11iiI in IIIII11I1IiI :
  o000o0o00Oo ( I1111i , oO0o0 , Ii11iiI , o00O0O , o0ooooO0o0O , iIiiii )
  I1I11i ( 'movies' , 'MAIN' )
def O0Ooo0o ( url ) :
 if 75 - 75: OooOO000 + iI11I1II1I1I
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OOoOooO0o = ( '%s%s' % ( I1IiiiI , url ) )
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , Iiii1iI1i , iIiiii , iiii11i , I1111i in IIIII11I1IiI :
  OoooO0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
  for i11I in OoooO0o :
   if i11I == url :
    I1111i = ( '[COLORred]Watched - [/COLOR]' + I1111i ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  iIii ( I1111i , url , 222 , Iiii1iI1i , iiii11i , iIiiii )
  if 6 - 6: oOo0O0Ooo - Ii
  I1I11i ( 'movies' , 'MAIN' )
  if 61 - 61: O00OOo00oo0o * Ii1I % oOo0O0Ooo % oO0o % iiII11i1I1IIi + iiII11i1I1IIi
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 6 - 6: I1ii11iIi11i
  if 73 - 73: O00OOo00oo0o * Ii1I + I11i - I1ii11iIi11i . iiII11i1I1IIi
def o0oOOO ( url ) :
 if 62 - 62: iIi1i1ii1 - oo0oO00 % iI11I1II1I1I
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , iIiiii , url , o00O0O , o0ooooO0o0O , Ii11iiI in IIIII11I1IiI :
  o000o0o00Oo ( I1111i , url , Ii11iiI , o00O0O , o0ooooO0o0O , iIiiii )
  if 57 - 57: ii / OOooOOo
  I1I11i ( 'movies' , 'MAIN' )
  if 44 - 44: OOooOOo * ooOoO0O00 * o0o00Oo0O
  if 94 - 94: oOo0O0Ooo - o0o00Oo0O
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: OOoOoo / oo0oO00 . oo0oO00 . iI11I1II1I1I . Ii
def iIii ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 69 - 69: Ii - o0o00Oo0O % IIiIiII11i % IIi / I1ii11iIi11i * iiII11i1I1IIi
 iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1iOOOO = True
 ooO0oO00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooO0oO00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooO0oO00O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooOO00oOOo000 = [ ]
  ooOO00oOOo000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooOO00oOOo000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooOO00oOOo000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooO0oO00O0o . addContextMenuItems ( ooOO00oOOo000 )
 I1iOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1 , listitem = ooO0oO00O0o , isFolder = False )
 return I1iOOOO
 if 61 - 61: oO0o . ooOoO0O00 - oOo0O0Ooo
def o000o0o00Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 38 - 38: oo0oO00 + iI11I1II1I1I * iIi1i1ii1 / oO0o + IIi
 iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1iOOOO = True
 ooO0oO00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooO0oO00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooO0oO00O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooOO00oOOo000 = [ ]
  ooOO00oOOo000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooOO00oOOo000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooOO00oOOo000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooO0oO00O0o . addContextMenuItems ( ooOO00oOOo000 )
 I1iOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1 , listitem = ooO0oO00O0o , isFolder = True )
 return I1iOOOO
if 48 - 48: ii - O00OOo00oo0o . Ii * OooOO000 - iIi1i1ii1 - I11i
if 59 - 59: OooOO000 / iiII11i1I1IIi . I1ii11iIi11i
if 100 - 100: o0o00Oo0O
if 94 - 94: Ii1I - I11i
if 42 - 42: I11i * OOooOOo . oO0o - OooOO000 / IIiIiII11i
if 25 - 25: I1ii11iIi11i % OOooOOo
if 75 - 75: ooOoO0O00
if 74 - 74: I1ii11iIi11i + O00OOo00oo0o - oo0oO00 - oO0o + OooOO000 - iI11I1II1I1I
if 54 - 54: Ii1I + IIiIiII11i . oOo0O0Ooo / oO0o . IIiIi1iI
if 58 - 58: OOoOoo % Ii * IIiIiII11i . Ii1I
if 94 - 94: Ii . IIi + iI11I1II1I1I * O00OOo00oo0o * O00OOo00oo0o
if 36 - 36: iiII11i1I1IIi - OOoOoo . OOoOoo
if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
if 84 - 84: iI11I1II1I1I + ii
if 77 - 77: o0o00Oo0O * Ii1I * oo0oO00 + oO0o + Ii1I - O00OOo00oo0o
def iI1I1I ( string ) :
 if OOO00O == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 33 - 33: iI11I1II1I1I / OooOO000
def OOOOiiI ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 o000Ooo00o00O = [ ]
 try :
  if 80 - 80: OooOO000
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( OOOOi11i1 ) == False :
  iI1I1I ( 'Making Favorites File' )
  o000Ooo00o00O . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  OoOoO = open ( OOOOi11i1 , "w" )
  OoOoO . write ( json . dumps ( o000Ooo00o00O ) )
  OoOoO . close ( )
 else :
  iI1I1I ( 'Appending Favorites' )
  OoOoO = open ( OOOOi11i1 ) . read ( )
  iI1I1ii11IIi1 = json . loads ( OoOoO )
  iI1I1ii11IIi1 . append ( ( name , url , iconimage , fanart , mode ) )
  I11OOO0 = open ( OOOOi11i1 , "w" )
  I11OOO0 . write ( json . dumps ( iI1I1ii11IIi1 ) )
  I11OOO0 . close ( )
  if 100 - 100: I1ii11iIi11i . iIi1i1ii1 . oOo0O0Ooo % IIiIiII11i - oo0oO00
  if 52 - 52: oOo0O0Ooo % oO0o * iIi1i1ii1 * OooOO000 / IIi
def oooO00oo0 ( ) :
 if os . path . exists ( OOOOi11i1 ) == False :
  o000Ooo00o00O = [ ]
  iI1I1I ( 'Making Favorites File' )
  o000Ooo00o00O . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  OoOoO = open ( OOOOi11i1 , "w" )
  OoOoO . write ( json . dumps ( o000Ooo00o00O ) )
  OoOoO . close ( )
 else :
  o000 = json . loads ( open ( OOOOi11i1 ) . read ( ) )
  oOiiIIIII = len ( o000 )
  for iiI1 in o000 :
   I1111i = iiI1 [ 0 ]
   oO0o0 = iiI1 [ 1 ]
   Iiii1iI1i = iiI1 [ 2 ]
   try :
    iii11i1 = iiI1 [ 3 ]
    if iii11i1 == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     iii11i1 = Iiii1iI1i
    else :
     iii11i1 = o0ooooO0o0O
   try : IIiI1I1IIiiI1 = iiI1 [ 5 ]
   except : IIiI1I1IIiiI1 = None
   try : oooOOO0o0O0 = iiI1 [ 6 ]
   except : oooOOO0o0O0 = None
   if 31 - 31: ii - oo0oO00 / O00OOo00oo0o
   if iiI1 [ 4 ] == 0 :
    iiOOooooO0Oo ( I1111i , oO0o0 , '' , Iiii1iI1i , o0ooooO0o0O , '' , 'fav' )
   else :
    iiOOooooO0Oo ( I1111i , oO0o0 , iiI1 [ 4 ] , Iiii1iI1i , o0ooooO0o0O , '' , 'fav' )
    if 62 - 62: Ii - iiII11i1I1IIi
def o00OOOOooO ( name ) :
 iI1I1ii11IIi1 = json . loads ( open ( OOOOi11i1 ) . read ( ) )
 for o0oo00oo0oO in range ( len ( iI1I1ii11IIi1 ) ) :
  if iI1I1ii11IIi1 [ o0oo00oo0oO ] [ 0 ] == name :
   del iI1I1ii11IIi1 [ o0oo00oo0oO ]
   I11OOO0 = open ( OOOOi11i1 , "w" )
   I11OOO0 . write ( json . dumps ( iI1I1ii11IIi1 ) )
   I11OOO0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 49 - 49: oOo0O0Ooo
 if 24 - 24: IIiIiII11i / iIi1i1ii1 . iI11I1II1I1I - IIiIiII11i % o0o00Oo0O
def I1i11II11i1iI ( ) :
 IIi1Ii11iIi = os . path . join ( I11i1 , 'addons.ini' )
 IiiIii1II1I = open ( IIi1Ii11iIi , "w+" )
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 IiiIii1II1I . write ( r'[' + IiII + ']' + '\n' )
 for I1111i , o00O0O , oOo0I1Ii11i , oO0o0 in IIIII11I1IiI :
  oO0o0 = ( oO0o0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  iIIIii1 = ( I1111i + '=plugin://' + IiII + '/?url=' + oO0o0 + '&mode=10012&name=' + ( I1111i ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;description=' )
  IiiIii1II1I . write ( iIIIii1 + '\n' )
  if 40 - 40: Ii1I + oo0oO00
  if 34 - 34: o0o00Oo0O * OOoOoo / ooOoO0O00 + oo0oO00 . OOooOOo
def O0oo ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 in IIIII11I1IiI :
  oo000ii ( '24/7' , oO0o0 , 90021 , oOOOo00O00oOo + '247Streams.png' )
  if 34 - 34: oOo0O0Ooo
def o0OoOo0O00 ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , oOOOo00O00oOo + '247Streams.png' , oOOOo00O00oOo + '247Streams.png' , '' )
def oooOOOOOi1iIii ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def oOIIiIi ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def iI1i1iI1iI ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def I1IIiIi ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , oO0o0 , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 93 - 93: oo0oO00 - IIi + I11i . oo0oO00 / iiII11i1I1IIi
  if 52 - 52: O00OOo00oo0o + O00OOo00oo0o
def OO0ii1 ( ) :
 if 32 - 32: I11i % oOo0O0Ooo
 iiOOooooO0Oo ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 if 7 - 7: I1ii11iIi11i . ooOoO0O00 - oo0oO00
def o0OoOOoOOoo ( ) :
 if 74 - 74: iI11I1II1I1I / iIi1i1ii1
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i , oOOoO in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + '  -  ' + ( oOOoO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oO0o0 , 10023 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 59 - 59: iIi1i1ii1 / IIiIiII11i - OOoOoo % OOooOOo % ii
  if 79 - 79: OooOO000 . ii . oOo0O0Ooo * o0o00Oo0O * oO0o - IIi
  if 33 - 33: Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
def O00000OO00OO ( ) :
 if 35 - 35: I1ii11iIi11i
 iiOOooooO0Oo ( '[COLOR' + II + ']Action[/COLOR]' , 'Aksiyon' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Adventure[/COLOR]' , 'Macera' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Animation[/COLOR]' , 'Animasyon' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Anime[/COLOR]' , 'Anime' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Biography[/COLOR]' , 'Biyografi' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Comedy[/COLOR]' , 'Komedi' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Drama[/COLOR]' , 'Dram' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Family[/COLOR]' , 'Aile' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']History[/COLOR]' , 'Tarih' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Horror[/COLOR]' , 'Korku' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Mystery[/COLOR]' , 'Gizem' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Romance[/COLOR]' , 'Romantik' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Sport[/COLOR]' , 'Spor' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Western[/COLOR]' , 'Tarih' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 if 47 - 47: ooOoO0O00 % IIiIi1iI - I1ii11iIi11i * iiII11i1I1IIi / Ii
def Iii1Iii ( url ) :
 IIii1I1i = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( IIii1I1i )
 IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 48 - 48: IIi
  if 26 - 26: OooOO000 * O00OOo00oo0o * oo0oO00 * OOooOOo
  if 48 - 48: OooOO000 % Ii . ii * OOoOoo % oO0o . OooOO000
  if 6 - 6: o0o00Oo0O . IIiIi1iI - oo0oO00 / Ii
def O00O0 ( ) :
 if 52 - 52: OooOO000 + o0o00Oo0O % I11i % o0o00Oo0O % IIiIiII11i + ii
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 oO0o0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( oO0o0 )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  if OOoOOo0O00O in I1111i . lower ( ) :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 51 - 51: OooOO000 % Ii
   if 28 - 28: Ii1I + Ii1I % OOooOOo
   if 12 - 12: iiII11i1I1IIi
def I11iIi1i1I1i1 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for o0O0O0ooo0oOO , iIIiii1 , iiiiii1ii1 , I1111i in IIIII11I1IiI :
  iIIII1i1 = ( iiiiii1ii1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1I1 = ( iIIiii1 ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oO00o0oOoo = 'Season ' + I1I1 + 'Episode ' + iIIII1i1 + I1111i
  oOOI1 ( oO00o0oOoo , o0O0O0ooo0oOO )
  if 63 - 63: oO0o . oo0oO00 + O00OOo00oo0o . OOooOOo / Ii / OooOO000
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + IIi
  if 31 - 31: iIi1i1ii1 * I11i * iIi1i1ii1 + oO0o * I11i . O00OOo00oo0o
def oOOI1 ( name , url ) :
 o0O0O0ooo0oOO = url
 Oo00oo00o00Oo = name
 iii1i1iiiiIi = cloudflare . source ( o0O0O0ooo0oOO )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for i1ii , iiiiiii11III in i1I :
  OoO ( '[COLOR' + II + ']' + Oo00oo00o00Oo + iiiiiii11III + '[/COLOR]' , i1ii , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 48 - 48: O00OOo00oo0o % OooOO000 % iIi1i1ii1 % iI11I1II1I1I . iIi1i1ii1
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 14 - 14: OooOO000 * oO0o % o0o00Oo0O + iiII11i1I1IIi + Ii1I
 if 23 - 23: I1ii11iIi11i % OooOO000 + iIi1i1ii1 - O00OOo00oo0o
def Ii1i1iI ( ) :
 if 65 - 65: ii
 if 22 - 22: IIi + IIiIiII11i + I1ii11iIi11i
 if 83 - 83: IIiIi1iI
 if 43 - 43: IIi
 if 84 - 84: IIi . OOoOoo . OooOO000
 if 2 - 2: I1ii11iIi11i - OOooOOo
 if 49 - 49: iIi1i1ii1 + IIiIiII11i / oo0oO00 - OOooOOo % OOooOOo + oOo0O0Ooo
 iiOOooooO0Oo ( '[COLOR' + II + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , '' , 10091 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 54 - 54: IIiIi1iI % I1ii11iIi11i - IIi
def iIi11IiiiII11 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( I1 )
 i1IiI = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + o00O0O , '' , '' )
 for url in i1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 2 - 2: Ii1I - I1ii11iIi11i
def Iii1o00o0 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( I1 )
 i1IiI = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  o00O0O = 'http://watchepisodes.cc/' + o00O0O
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10093 , o00O0O , o00O0O , '' )
 for url in i1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 84 - 84: OOooOOo - I1ii11iIi11i . IIiIi1iI . OOoOoo - I1ii11iIi11i
def o0Oo0oO00Oooo ( url , iconimage ) :
 o00O0O = iconimage
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( I1 )
 for iiiiii1ii1 , url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + iiiiii1ii1 + ' - ' + I1111i + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , o00O0O , '' , '' )
  if 31 - 31: ooOoO0O00 * I1ii11iIi11i % iIi1i1ii1 + oO0o
def O0O00 ( url , iconimage ) :
 o00O0O = iconimage
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for I1111i , url in IIIII11I1IiI :
  if 'player' in I1111i :
   pass
  elif 'vod' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , o00O0O , '' , '' )
   if 28 - 28: oO0o . IIiIiII11i . Ii1I
   if 98 - 98: Ii / oOo0O0Ooo
   if 7 - 7: OooOO000 % Ii1I
   if 64 - 64: O00OOo00oo0o + Ii
   if 35 - 35: OOooOOo + ooOoO0O00 % IIi
   if 68 - 68: OOoOoo . IIiIi1iI
def IIiI1 ( ) :
 if 64 - 64: ooOoO0O00 + I1ii11iIi11i * oOo0O0Ooo / IIi
 if 3 - 3: I1ii11iIi11i / IIiIi1iI + IIiIi1iI . Ii1I
 if 50 - 50: iI11I1II1I1I * oo0oO00
 if 85 - 85: ooOoO0O00
 if 100 - 100: ii / iiII11i1I1IIi % oO0o + iIi1i1ii1
 if 42 - 42: I1ii11iIi11i / OOoOoo . iIi1i1ii1 * oOo0O0Ooo
 if 54 - 54: OOooOOo * OooOO000 + oO0o
 if 93 - 93: I11i / oOo0O0Ooo
 if 47 - 47: I1ii11iIi11i * IIi
 if 98 - 98: oo0oO00 - oo0oO00 . IIiIi1iI
 if 60 - 60: oOo0O0Ooo * Ii1I / o0o00Oo0O + iiII11i1I1IIi + OOoOoo
 if 66 - 66: OOoOoo * I1ii11iIi11i . ii * O00OOo00oo0o
 if 93 - 93: OOoOoo / ooOoO0O00
 if 47 - 47: IIiIi1iI - iIi1i1ii1
 iiOOooooO0Oo ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , oOOOo00O00oOo + 'latest.png' , oOOOo00O00oOo + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , oOOOo00O00oOo + 'popular.png' , oOOOo00O00oOo + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , oOOOo00O00oOo + 'Genre.png' , oOOOo00O00oOo + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , oOOOo00O00oOo + 'series.png' , oOOOo00O00oOo + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'WatchSeries.png' , '' )
 if 98 - 98: oo0oO00 . O00OOo00oo0o / OOooOOo . IIiIi1iI
 if 1 - 1: IIi
def OoOo0o0OOoO0 ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
 for url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 30 - 30: iIi1i1ii1 % iiII11i1I1IIi + I11i
def ooo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 83 - 83: ii . oOo0O0Ooo + iIi1i1ii1 * o0o00Oo0O / oo0oO00
def IiiiI11 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  if 'episode' in url :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 57 - 57: iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
  if 95 - 95: oo0oO00
def i11ii ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IiI111I = 'http://www.watchseriesgo.to/search/' + OOoOOo0O00O . replace ( ' ' , '%20' )
 I1 = O000oo ( IiI111I )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , oO0o0 , I1111i in IIIII11I1IiI :
  if 'watch online' in I1111i :
   pass
  else :
   print oO0o0
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to' + oO0o0 , 10044 , o00O0O , '' , '' )
   if 62 - 62: ii + OOoOoo
   xbmcplugin . setContent ( I1IIiiIiii , 'movies' )
   if 32 - 32: OOooOOo * I11i / ii
def oOooo00OOO000 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i , iiiiii1ii1 , iIiiii in IIIII11I1IiI :
  oOoOOo000oOoO0 = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iiiiii1ii1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + oOoOOo000oOoO0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , o00O0O , '' , iIiiii )
  if 85 - 85: ooOoO0O00 - IIi / o0o00Oo0O + o0o00Oo0O / Ii1I
def O0oOoo00Oo0O ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  oOoOOo000oOoO0 = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + oOoOOo000oOoO0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 5 - 5: o0o00Oo0O - OooOO000 / O00OOo00oo0o . I11i
def iIII1iIii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , o00O0O , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 9 - 9: ooOoO0O00 - OOooOOo
def Oo00o0OOo0OO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 I11o0oO00oO0o0o0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for iIIiii1 , IIiiIii11 in I11o0oO00oO0o0o0 :
  IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( IIiiIii11 ) )
  for url , I1111i in IIIII11I1IiI :
   oOoOOo000oOoO0 = ( iIIiii1 ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + oOoOOo000oOoO0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for I1111i , url in IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 18 - 18: IIiIi1iI - OOoOoo / IIiIiII11i / Ii1I
class i1Ii1IiiIi1II ( ) :
 if 54 - 54: iIi1i1ii1 % ooOoO0O00
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 51 - 51: iI11I1II1I1I - oOo0O0Ooo
  oOoOOo000oOoO0 = name
  self . Get_Sources ( oO0o0 , oOoOOo000oOoO0 )
  if 61 - 61: ii . iIi1i1ii1 % oo0oO00 * ii
  if 96 - 96: iIi1i1ii1 - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O000oo ( URL )
  IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for oO0o0 , I1111i in IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + oO0o0
   self . Get_site_link ( URL , season_name )
   if 75 - 75: I1ii11iIi11i + iIi1i1ii1 + oO0o
 def Get_site_link ( self , url , season_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
  i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( I1 )
  ooOoO00 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( I1 )
  for url in IIIII11I1IiI :
   self . main ( url , season_name )
  for url in i1I :
   self . main ( url , season_name )
  for url in ooOoO00 :
   self . main ( url , season_name )
   if 97 - 97: IIiIi1iI % Ii % iiII11i1I1IIi
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   IIi1i = 'DACLIPS'
   if IIi1i in i1Ii1IiiIi1II . source_list :
    pass
   else :
    self . daclips ( url , season_name , IIi1i )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    IIi1i = 'THEVIDEO'
    if IIi1i in i1Ii1IiiIi1II . source_list :
     pass
    else :
     self . thevideo ( url , season_name , IIi1i )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     IIi1i = 'ALLMYVIDEOS'
     if IIi1i in i1Ii1IiiIi1II . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , IIi1i )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      IIi1i = 'VIDSPOT'
      if IIi1i in i1Ii1IiiIi1II . source_list :
       pass
      else :
       self . vidspot ( url , season_name , IIi1i )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       IIi1i = 'VODLOCKER'
       if IIi1i in i1Ii1IiiIi1II . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , IIi1i )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        IIi1i = 'VIDTO'
        if IIi1i in i1Ii1IiiIi1II . source_list :
         pass
        else :
         self . vidto ( url , season_name , IIi1i )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 56 - 56: I11i / OOoOoo
       else :
        if 'youwatch' in url :
         IIi1i = 'YouWatch'
         if IIi1i in i1Ii1IiiIi1II . source_list :
          pass
         else :
          self . youwatch ( url , season_name , IIi1i )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 11 - 11: OOooOOo / iiII11i1I1IIi
          if 47 - 47: IIi . O00OOo00oo0o % IIiIiII11i + I1ii11iIi11i - oo0oO00 . IIiIiII11i
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for Ooo0oo , I1111i in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 37 - 37: iI11I1II1I1I . oOo0O0Ooo % oO0o % ii . ii / o0o00Oo0O
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for Ooo0oo , I1111i in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 25 - 25: IIiIiII11i % IIiIiII11i - iIi1i1ii1 . o0o00Oo0O
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 79 - 79: OOoOoo / oO0o * ii * OOooOOo + oOo0O0Ooo
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 68 - 68: iiII11i1I1IIi / iI11I1II1I1I . I1ii11iIi11i + Ii + I11i
 def daclips ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 92 - 92: oO0o . I11i . iIi1i1ii1 % OOooOOo
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . youplay ( Ooo0oo , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 58 - 58: Ii1I % iIi1i1ii1 * iIi1i1ii1 - OooOO000
 def Printer ( self , Link , season_name , source_name ) :
  if 9 - 9: IIiIi1iI - iIi1i1ii1 % IIiIiII11i + OOoOoo + IIi % o0o00Oo0O
  if Link in i1Ii1IiiIi1II . List :
   pass
  elif source_name in i1Ii1IiiIi1II . source_list :
   pass
  else :
   OoO ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   i1Ii1IiiIi1II . List . append ( Link )
   i1Ii1IiiIi1II . source_list . append ( source_name )
   if 65 - 65: IIi - oO0o % Ii
   xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 58 - 58: OooOO000
   if 2 - 2: IIiIiII11i + ooOoO0O00
   if 68 - 68: IIi + iIi1i1ii1
   if 58 - 58: OOoOoo * iIi1i1ii1 . ooOoO0O00
   if 19 - 19: oo0oO00
def Ooo0O0oooo ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , O0o0Oo , '' )
 if 85 - 85: IIiIi1iI - oOo0O0Ooo / ooOoO0O00 / oO0o / IIiIiII11i
def oo0O0O ( url ) :
 iiOOooooO0Oo ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( iIIII )
 for IIIIiI1ii1 , url , ooOO0oo00Oo , i1I11I1i , oOO0oOooo , IiIi1Ii , o00IIIIii1111i1 , oooOo0OOOoo0 , OoOoO , iiI1ii1 , I1oOOoo0 in IIIII11I1IiI :
  ooOO0oo00Oo = ooOO0oo00Oo
  if 'Arsenal' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'arsenal-logo.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                                  ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Bournemouth' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'afc-bournemouth.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                       ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Burnley' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'KEGnQWW.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                                   ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Chelsea' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'chelsea.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                                  ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Crystal' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'CrystalPalace.0.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                       ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Everton' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'Everton.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                                   ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Hull' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'hull-city-afc.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                                 ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Leicester' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                       ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Liverpool' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'liverpool-logo.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                               ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Manchester City' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'city-logo.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '               ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Manchester United' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + '91.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '          ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Middlesbrough' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                 ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Southampton' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'southampton-fc-logo.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                   ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Stoke City' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'stoke-city.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                          ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Sunderland' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'sunderland-logo.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                        ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Swansea' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'swansea-city-afc.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                    ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Tottenham' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '        ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Watford' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '                              ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'Bromwich' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '   ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  elif 'West Ham' in ooOO0oo00Oo :
   IIi1iiii1iI = oOOOo00O00oOo + 'west-ham.png'
   I1111i = '[COLOR' + II + ']' + IIIIiI1ii1 + ' - ' + ooOO0oo00Oo + '             ' + i1I11I1i + '        ' + oOO0oOooo + '        ' + IiIi1Ii + '        ' + o00IIIIii1111i1 + '        ' + oooOo0OOOoo0 + '        ' + OoOoO + '        ' + iiI1ii1 + '[/COLOR]'
  iiOOooooO0Oo ( str ( I1111i ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , IIi1iiii1iI , IIi1iiii1iI , ooOO0oo00Oo )
  if 10 - 10: OOooOOo . OOoOoo * iI11I1II1I1I - oo0oO00 - OOooOOo / O00OOo00oo0o
def II1I11 ( description ) :
 ooOO0oo00Oo = description
 oO0o0 = ( 'http://www.fullmatchesandshows.com/?s=' + ooOO0oo00Oo ) . replace ( ' ' , '%20' )
 i1ii1iiiI ( oO0o0 )
 if 33 - 33: I11i % OOoOoo - iI11I1II1I1I % IIi + O00OOo00oo0o - Ii
def ooi1 ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oO0o0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o00O0O , O0o0Oo , '' )
  if 17 - 17: OOooOOo - oOo0O0Ooo
def OOoOOoo0 ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
  i1IIi1i1Ii1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for oo0OOO0OOoOO in i1IIi1i1Ii1 :
   oo0OOO0OOoOO = oo0OOO0OOoOO
  oOoO = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for II1i1 , o00O0O , time , o0o0oo0OOo0O0 in oOoO :
   II1iI11 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( o0o0oo0OOo0O0 )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + oo0OOO0OOoOO + ' - ' + II1i1 + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + o00O0O , O0o0Oo , ( str ( II1iI11 ) ) )
   if 37 - 37: I11i * I1ii11iIi11i
 I1I11i ( 'tvshows' , 'Media Info 3' )
 if 11 - 11: oo0oO00
def Oo0O0o00o00 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 if 90 - 90: O00OOo00oo0o . IIiIiII11i . Ii1I
def I1iIi1111 ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  IIi1i1i1i = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   IIi1i1i1i = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OoO ( '[COLOR' + II + ']' + IIi1i1i1i + '[/COLOR]' , url , 10013 , o00O0O )
 for url , o00O0O , I1111i in i1I :
  IIi1i1i1i = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   OoO ( '[COLOR' + II + ']' + IIi1i1i1i + '[/COLOR]' , url , 10013 , o00O0O )
def i1ii1iiiI ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 74 - 74: oO0o . iIi1i1ii1 % iI11I1II1I1I . iI11I1II1I1I / OOooOOo - IIi
 if 30 - 30: iiII11i1I1IIi
 if 46 - 46: IIiIi1iI
 if 92 - 92: IIiIi1iI / OOoOoo + iI11I1II1I1I
 if 47 - 47: IIi * iIi1i1ii1 % iI11I1II1I1I / IIiIi1iI
 if 61 - 61: OOoOoo + OooOO000 - oO0o * oo0oO00
 if 87 - 87: IIiIiII11i % IIiIiII11i
 for url , o00O0O , I1111i in i1I :
  IIi1i1i1i = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   OoO ( '[COLOR' + II + ']' + IIi1i1i1i + '[/COLOR]' , url , 10013 , o00O0O )
   if 51 - 51: IIiIi1iI * iI11I1II1I1I . OooOO000
def iIi11I1II ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for i1ii in IIIII11I1IiI :
  oO00Oo0O0 = ( i1ii ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOOOo0o00OO0000 ( 'http:' + oO00Oo0O0 )
  if 91 - 91: iiII11i1I1IIi + iIi1i1ii1 + OOoOoo
  if 58 - 58: OooOO000 * iIi1i1ii1 - Ii % Ii1I
  if 3 - 3: O00OOo00oo0o . iiII11i1I1IIi % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * oO0o
  if 5 - 5: IIiIiII11i * ooOoO0O00 % iIi1i1ii1
def oO000O ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  OoO ( I1111i , url , 8046 , o00O0O )
 for url in i1I :
  oo000ii ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def Oo0o0OoOoOo0 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  OOOOo0o00OO0000 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 36 - 36: iIi1i1ii1 * oOo0O0Ooo * Ii1I . iiII11i1I1IIi * Ii1I
def O0ooO0 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 41 - 41: I11i % I1ii11iIi11i
def O0O0Oo00 ( ) :
 oo000ii ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 oo000ii ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 oo000ii ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , oO0o0 , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def o00oOo0OoO0oO ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + o00O0O )
 for url in next :
  oo000ii ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 84 - 84: ooOoO0O00 / ooOoO0O00 - ooOoO0O00 . oo0oO00 . oO0o * Ii1I
  if 57 - 57: Ii1I * OOoOoo - IIiIi1iI
def O0oO00oO0o00o ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OoO ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   oo000ii ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def o0OOo0O00OO0O ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  OoO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10012 , '' )
  if 58 - 58: oo0oO00
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiIIiI1i1i1I1 ( name , url ) :
 O000oOO = 0
 name = name
 url = url
 i1Oo0oO00o = [ '144' , '240' , '380' , '480' , '720' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OOOOo0o00OO0000 ( url )
  if 68 - 68: OOoOoo - O00OOo00oo0o
  if 15 - 15: oOo0O0Ooo % oo0oO00 . I1ii11iIi11i % iI11I1II1I1I
  if 98 - 98: iiII11i1I1IIi - ooOoO0O00 % iIi1i1ii1 - ii
  if 19 - 19: iI11I1II1I1I + O00OOo00oo0o . O00OOo00oo0o - I1ii11iIi11i
  if 41 - 41: oOo0O0Ooo . I1ii11iIi11i . OOoOoo % ii + oO0o
  if 23 - 23: oOo0O0Ooo - I11i % oo0oO00 . o0o00Oo0O * ii + IIiIi1iI
  if 53 - 53: I1ii11iIi11i
  if 3 - 3: OOoOoo - ii * ii - oOo0O0Ooo / O00OOo00oo0o * Ii1I
def O0oo0ooO00 ( ) :
 iIIII = oo00ooOoO00 ( 'http://documentarylovers.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  if 'genre' in oO0o0 :
   oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oO0o0 , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOoO0 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( iIIII )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , o00O0O )
 for url in next :
  oo000ii ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 50 - 50: O00OOo00oo0o * O00OOo00oo0o * I1ii11iIi11i - oO0o
def IIi1iI ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( iIIII )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in i1I :
  o0OOo0O00OO0O ( url )
  if 36 - 36: OooOO000 * iiII11i1I1IIi * o0o00Oo0O * IIi - I11i / Ii1I
def oooOo0OO ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0o0oO0O000o = 'http://documentarylovers.com/?s=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 iiIii1I = OO0o0oO0O000o . lower ( )
 oOoO0 ( iiIii1I )
 if 9 - 9: iI11I1II1I1I
def O0000 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if 'films' in url :
   oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def ooO0OO0Oooo0o ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  if 'films' in url :
   OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + o00O0O )
 for url in i1I :
  oo000ii ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def OOoO00o000 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  if 'rtd' in url :
   iIi1 ( url )
   if 21 - 21: Ii * OooOO000 / IIiIi1iI % OooOO000 * I1ii11iIi11i
def iIi1 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iIIII )
 for i1Oo00 , file in IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1Oo00 + file )
  OOOOo0o00OO0000 ( url )
  if 84 - 84: iI11I1II1I1I
  if 25 - 25: oO0o * OOoOoo - ooOoO0O00 - iiII11i1I1IIi * IIiIiII11i
def oo00OO ( ) :
 I1 = oo00ooOoO00 ( 'http://www.stream2watch.co/live-tv' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i , oOOoOo0Ooo in IIIII11I1IiI :
  oo000ii ( ( I1111i + '[COLOR' + II + ']' + oOOoOo0Ooo + '[/COLOR]' ) , oO0o0 , 8086 , o00O0O )
  if 95 - 95: O00OOo00oo0o % I1ii11iIi11i
def ooo000OO ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8087 , o00O0O )
  if 13 - 13: iI11I1II1I1I + OooOO000 / iIi1i1ii1 / ooOoO0O00 % oO0o - iI11I1II1I1I
def o0oooO0O00OoO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  iiiiIIi ( url , I1111i )
  if 53 - 53: IIiIi1iI . IIi . I11i + oo0oO00
def iiiiIIi ( url , name ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  print url
  OoO ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + iIi1i1ii1 % ooOoO0O00 . oo0oO00
def o00OoOO00 ( ) :
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oO0o0 , 3002 , 'http://www.solie.org/alibrary/' + o00O0O )
def oO0oOOoOo000O ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def II1 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 o0O0OO = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIIII )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , I1111i in o0O0OO :
  oo000ii ( '[COLOR' + II + ']Season- ' + I1111i + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  oo000ii ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , o00O0O , I1111i in i1I :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def oOoO0o ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  i1II ( url )
def i1II ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . IIi
def O0OOooOoO ( ) :
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oO0o0 , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def IIiiIiIIiI1 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  I1Ii ( url )
  if 39 - 39: iiII11i1I1IIi / ii - iIi1i1ii1 + oO0o / OOooOOo
def O0o ( ) :
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oO0o0 , 8065 , oOOOo00O00oOo + 'classictv.png' )
def oo0O0000oo0o0 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  if 'mp4' in url :
   OOOOo0o00OO0000 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 32 - 32: ii / OooOO000 / O00OOo00oo0o + OooOO000 - iiII11i1I1IIi + IIiIiII11i
def IiIIIiII1111 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oO0o0 , 8071 , oOOOo00O00oOo + 'streams.png' )
def o0oOOoo ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for I1111i , url in IIIII11I1IiI :
  if '(Free Access)' in I1111i :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def OOo000O000ooo ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for o00O0O , I1111i , url in IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , o00O0O , o0ooooO0o0O , '' )
  if 40 - 40: IIiIi1iI
def Oo00oO0o0Oo0o ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  II1iiiIIi11I ( 'http://watchxxxfree.com/categories' )
 if i11I1II1I11i == 1 :
  I1Io0Oo00 ( 'http://www.perfectgirls.net' )
 if i11I1II1I11i == 2 :
  I1II11IIi11i ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 3 :
  oo00ooOo ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 4 :
  I1II11IIi11i ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 5 :
  I1II11IIi11i ( 'http://www.xvideos.com/verified/videos' )
 if i11I1II1I11i == 6 :
  Ooo00OoO0O00 ( 'http://www.xvideos.com/tags' )
 if i11I1II1I11i == 7 :
  ii1ii1i1ii ( 'http://www.xvideos.com/porn' )
 if i11I1II1I11i == 8 :
  iIi1Iii1 ( )
  if 87 - 87: ii
  if 1 - 1: iI11I1II1I1I / I11i
  if 98 - 98: o0o00Oo0O % oOo0O0Ooo / ii * Ii1I - oo0oO00
  if 51 - 51: OooOO000 + iiII11i1I1IIi
  if 54 - 54: IIiIiII11i * o0o00Oo0O % oOo0O0Ooo . iiII11i1I1IIi
  if 62 - 62: iIi1i1ii1 . Ii % o0o00Oo0O % O00OOo00oo0o - I1ii11iIi11i
  if 69 - 69: IIiIiII11i . OOooOOo * OOooOOo % iIi1i1ii1 + oOo0O0Ooo
  if 100 - 100: Ii - I1ii11iIi11i
  if 47 - 47: OooOO000 * OOooOOo * OOoOoo
def iIiii1IIi1I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  if 'ch' in url :
   oOoo0OO0 ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def IiIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 ii1IiI = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for I1111i , url in ii1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def oo0o0ooOoo00O ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   iI1 ( url )
def ii1O0oOOo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def II1iiiIIi11I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i , O0OO0oOO in IIIII11I1IiI :
  if 'category' in url :
   oOoo0OO0 ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   ' + O0OO0oOO + '[/COLOR]' , url , 90006 , o00O0O , oOOOo00O00oOo + 'Jizbox.png' , '' )
def ii111IIiiiiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 ii1IiI = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , o00O0O , '' , '' )
 for url in ii1IiI :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def oo0OOoOo0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   iI1 ( url )
def iI1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def I1Io0Oo00 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , O0OO0oOO in IIIII11I1IiI :
  if 'category' in url :
   oOoo0OO0 ( '[COLOR' + II + ']' + I1111i + '[COLORorange]' + O0OO0oOO + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def oO00oO0 ( url ) :
 I1 = O000oo ( url )
 o0O0O0ooo0oOO = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 ii1IiI = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , o00O0O , '' , '' )
 for url in ii1IiI :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , o0O0O0ooo0oOO + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def o0oI1Iii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  II1I1Ii11 ( 'http://www.perfectgirls.net' + url )
def II1I1Ii11 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( 'http://' + url )
def ii1ii1i1ii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , I1111i , O0OO0oOO in IIIII11I1IiI :
  oOoo0OO0 ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + O0OO0oOO + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def Ooo00OoO0O00 ( url ) :
 I1 = O000oo ( url )
 ii1IiI = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in ii1IiI :
  oOoo0OO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , I1111i , O0OO0oOO in IIIII11I1IiI :
  oOoo0OO0 ( ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + ( O0OO0oOO + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 20 - 20: iIi1i1ii1 / OooOO000 + IIiIiII11i . Ii . IIi
def o0oOOO0 ( url ) :
 I1 = O000oo ( url )
 ii1IiI = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in ii1IiI :
  oOoo0OO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i , i1IIiIIIi1 in IIIII11I1IiI :
  oOoo0OO0 ( I1111i + '--' + ( i1IIiIIIi1 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( o00O0O ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 11 - 11: iiII11i1I1IIi / OOooOOo
  if 17 - 17: IIiIi1iI
def I1II11IIi11i ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i , oO0oOoo0O , IIi1IIII in IIIII11I1IiI :
  oOoo0OO0 ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + IIi1IIII + ' - [COLORred]' + oO0oOoo0O + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , o00O0O , o00O0O , IIi1IIII + ' - ' + oO0oOoo0O )
 IiOo0ooooO0o00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in IiOo0ooooO0o00 :
  oOoo0OO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 34 - 34: OOooOOo % I11i - oo0oO00
def oo00ooOo ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 ii1IiI = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in ii1IiI :
  oOoo0OO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
 for url , I1111i in IIIII11I1IiI :
  if '/c/' in url :
   oOoo0OO0 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 40 - 40: OooOO000
   if 82 - 82: O00OOo00oo0o . ooOoO0O00 / oo0oO00
def iIi1Iii1 ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oooooo0Oo00o = ( OOoOOo0O00O ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 iiIii1I = oooooo0Oo00o . lower ( )
 Oo0O0O = 'http://www.xvideos.com/?k=' + iiIii1I
 print Oo0O0O + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O000oo ( Oo0O0O )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for o00O0O , oO0o0 , I1111i , oO0oOoo0O , IIi1IIII in IIIII11I1IiI :
  oOoo0OO0 ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + IIi1IIII + ' - [COLORred]' + oO0oOoo0O + '[/COLOR]' , 'http://www.xvideos.com' + oO0o0 , 10108 , o00O0O , o00O0O , IIi1IIII + ' - ' + oO0oOoo0O )
 IiOo0ooooO0o00 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for oO0o0 in IiOo0ooooO0o00 :
  oOoo0OO0 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oO0o0 , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
if 77 - 77: IIi % Ii - Ii1I
if 21 - 21: iiII11i1I1IIi . I1ii11iIi11i - ii * ooOoO0O00
if 54 - 54: IIiIiII11i % I11i - ooOoO0O00 . oOo0O0Ooo - IIiIiII11i / iI11I1II1I1I
if 29 - 29: oo0oO00
if 66 - 66: ii + OooOO000 . OOoOoo % ooOoO0O00
if 58 - 58: IIi % OooOO000 * o0o00Oo0O + Ii1I - OOoOoo
if 26 - 26: ooOoO0O00 / oOo0O0Ooo / iiII11i1I1IIi + iiII11i1I1IIi
if 46 - 46: O00OOo00oo0o % Ii1I + iIi1i1ii1
if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / iiII11i1I1IIi + IIiIi1iI
if 10 - 10: IIiIi1iI - I1ii11iIi11i % IIiIiII11i
if 66 - 66: iI11I1II1I1I . iI11I1II1I1I
if 46 - 46: O00OOo00oo0o * oo0oO00 . iIi1i1ii1 * O00OOo00oo0o * iI11I1II1I1I / iiII11i1I1IIi
if 46 - 46: IIiIiII11i % Ii1I . IIi . I1ii11iIi11i / Ii + oO0o
if 47 - 47: OOoOoo . IIi
if 96 - 96: iiII11i1I1IIi % IIiIiII11i / IIiIi1iI % IIi / IIiIi1iI % Ii
if 57 - 57: iiII11i1I1IIi - iiII11i1I1IIi % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - iIi1i1ii1 * iI11I1II1I1I
if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / oo0oO00 * I11i + IIi
if 89 - 89: IIiIi1iI * oOo0O0Ooo . oo0oO00
if 75 - 75: IIiIi1iI - OooOO000 % OooOO000 + IIiIi1iI * I11i - Ii1I
if 26 - 26: iiII11i1I1IIi * iIi1i1ii1 % oOo0O0Ooo + OooOO000
if 38 - 38: OooOO000 - I1ii11iIi11i / iIi1i1ii1 + oo0oO00 . OooOO000 + OOoOoo
if 19 - 19: iIi1i1ii1
if 51 - 51: iI11I1II1I1I
if 8 - 8: oO0o / I11i % OooOO000 . Ii . ii . iIi1i1ii1
if 8 - 8: oO0o * I1ii11iIi11i
if 41 - 41: I1ii11iIi11i / oO0o / OOooOOo - Ii - OOooOOo
if 4 - 4: iiII11i1I1IIi . OOoOoo
if 39 - 39: IIi . I1ii11iIi11i - OOooOOo * Ii
if 4 - 4: OOooOOo * o0o00Oo0O - iiII11i1I1IIi
if 72 - 72: iiII11i1I1IIi + IIiIi1iI / oOo0O0Ooo . OOoOoo % oO0o / Ii
if 13 - 13: O00OOo00oo0o % I11i + IIi + O00OOo00oo0o + Ii - Ii1I
if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
if 11 - 11: OooOO000
if 20 - 20: iIi1i1ii1 . O00OOo00oo0o % iIi1i1ii1
def i11iI1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( I1 )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( I1 )
 ooOoO00 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'http' in url :
   OoO ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   OoO ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in ooOoO00 :
  if 'http' in url :
   OoO ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
   if 92 - 92: iI11I1II1I1I
def OOO0oO0O ( url ) :
 iIIII1i = xbmc . Player ( o00oO0 ( ) )
 import urlresolver
 try : iIIII1i . play ( url )
 except : pass
 if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
 if 95 - 95: O00OOo00oo0o + OOoOoo * iI11I1II1I1I
def II1Iii1iI ( ) :
 if 56 - 56: iI11I1II1I1I . iiII11i1I1IIi
 if 2 - 2: iIi1i1ii1
 if 12 - 12: Ii - iI11I1II1I1I * OOoOoo * OooOO000
 if 19 - 19: o0o00Oo0O + oo0oO00 + I11i
 if 81 - 81: iI11I1II1I1I
 if 51 - 51: I11i . Ii1I * iIi1i1ii1 / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
 if 44 - 44: Ii % O00OOo00oo0o % oo0oO00 + iiII11i1I1IIi * oo0oO00 . iIi1i1ii1
 if 89 - 89: ii % IIiIiII11i - oO0o % Ii
 if 7 - 7: OOoOoo
 if 15 - 15: I1ii11iIi11i + OooOO000 + oOo0O0Ooo * I11i
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 8091 , oOOOo00O00oOo + 'gofish.png' )
def iII1111IIIIiI ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  oo000ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def IiiiiIi11 ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 o0OOo = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for o00O0O in o0OOo :
  o00O0O = o00O0O
 for url , I1111i in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  oo000ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 43 - 43: OOoOoo % iIi1i1ii1 . IIi / I1ii11iIi11i
def oOo00Oo00oO ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 50 - 50: IIiIiII11i + Ii1I
  if 54 - 54: oo0oO00
  if 26 - 26: IIiIi1iI % ii . O00OOo00oo0o * IIiIi1iI + IIiIiII11i - Ii1I
  if 20 - 20: oO0o
OOooO0o = '{PQ},' ; oo000o0O = '{SC},' ; iiIiIIiI1 = '{XG},' ; Ii11i = '{JP},' ; O00i1i = '{HW},' ; iiii = '{RT},'
def I1i1iiiI1 ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iI = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 oO0o0 = 'http://onlinemovies.tube/?s=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 o0O0O0ooo0oOO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 I1Ii11iiiI = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 II1Ii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 O0OoOOO00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 o0ooOo0OOOO0o = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 O0ooOoO = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + OOoOOo0O00O
 IIII = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 IIiii1I1I = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 62 - 62: IIiIiII11i - OOooOOo * iIi1i1ii1
 ii1i1i = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 oO0OO0O = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 70 - 70: ooOoO0O00 % oO0o / ooOoO0O00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = OOoOO0oo0ooO ( oO0o0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 iii1i1iiiiIi = OOoOO0oo0ooO ( o0O0O0ooo0oOO )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 Iiii = OOoOO0oo0ooO ( I1Ii11iiiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OO0OoO0o00 = OOoOO0oo0ooO ( II1Ii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 iII1Iii1I11i = OOoOO0oo0ooO ( O0OoOOO00 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 i1o0oooO = OOoOO0oo0ooO ( O0ooOoO )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooOo = OOoOO0oo0ooO ( IIII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 i11i1Ii1 = OOoOO0oo0ooO ( IIiii1I1I )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 30 - 30: OOooOOo - Ii
 if 94 - 94: OOooOOo % OooOO000
 oOOOOOoOO = OOoOO0oo0ooO ( ii1i1i )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 iI11ii = OOoOO0oo0ooO ( oO0OO0O )
 if 23 - 23: OOooOOo * OOoOoo / oo0oO00
 if 60 - 60: IIiIi1iI * iIi1i1ii1 + O00OOo00oo0o . IIi . o0o00Oo0O
 if 8 - 8: IIiIiII11i + IIiIiII11i * ooOoO0O00 * I11i / o0o00Oo0O / o0o00Oo0O
 if 66 - 66: O00OOo00oo0o * I11i / OOoOoo * OooOO000 / ii
 if 72 - 72: iI11I1II1I1I
 if 82 - 82: OOooOOo . iIi1i1ii1
 if 73 - 73: O00OOo00oo0o
 if 25 - 25: OOoOoo
 if 77 - 77: I11i . iI11I1II1I1I . ii . iI11I1II1I1I
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . iIi1i1ii1 - I1ii11iIi11i . Ii
 if 47 - 47: I1ii11iIi11i % oO0o - IIiIi1iI - I1ii11iIi11i * oo0oO00
 if 72 - 72: I11i % I11i + OooOO000 + Ii1I / I1ii11iIi11i
 if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
 if i11i1Ii1 != 'Failed' :
  o0oO0oo0000OO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i11i1Ii1 )
  for oO0o0 , I1111i in o0oO0oo0000OO :
   o00OooooOOOO = OOoOO0oo0ooO ( oO0o0 )
   oo000oiIIIII = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o00OooooOOOO )
   for Oo0O , oOOoOo0Ooo in oo000oiIIIII :
    oOOoOo0Ooo = ( oOOoOo0Ooo . replace ( '.' , ' ' ) )
    if iiIii1I in oOOoOo0Ooo . lower ( ) :
     if '.mkv' in Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + oOOoOo0Ooo + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + Oo0O , 222 , '' , '' , '' )
     elif '.mp4' in Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + oOOoOo0Ooo + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + Oo0O , 222 , '' , '' , '' )
     elif '.avi' in Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + oOOoOo0Ooo + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + Oo0O , 222 , '' , '' , '' )
     elif '.wav' in Oo0O :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + oOOoOo0Ooo + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + Oo0O , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + oOOoOo0Ooo + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + Oo0O , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iii1i1iiiiIi )
  for oO0o0 , Iiii1iI1i , iIiiii , iiii11i , I1111i in i1I :
   if OOoOOo0O00O in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source Technica[/COLOR]' ) , oO0o0 , 222 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 22 - 22: oO0o . OOooOOo % IIiIiII11i - o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 52 - 52: oO0o
 if Iiii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for IiiiI1 , I1111i in ooOoO00 :
   if OOoOOo0O00O in I1111i . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( I1Ii11iiiI + IiiiI1 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OO0OoO0o00 != 'Failed' :
  Iii1I1111ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoO0o00 )
  for oO0o0 , Iiii1iI1i , iIiiii , iiii11i , I1111i in Iii1I1111ii :
   if OOoOOo0O00O in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] source RaizTv[/COLOR]' ) , oO0o0 , 222 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 49 - 49: iIi1i1ii1 . Ii1I % IIiIi1iI . I1ii11iIi11i * IIi
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iII1Iii1I11i != 'Failed' :
  III11iiii11i1 = [ ]
  oOoOOOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iII1Iii1I11i )
  for oO0o0 , Iiii1iI1i , iIiiii , iiii11i , I1111i in oOoOOOo :
   if OOoOOo0O00O in I1111i . lower ( ) :
    if I1111i in III11iiii11i1 :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oO0o0 , 1016 , Iiii1iI1i , iiii11i , iIiiii )
     III11iiii11i1 . append ( I1111i )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if i1o0oooO != 'Failed' :
  ooOo0OoO = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( i1o0oooO )
  for oO0o0 , o00O0O , I1111i in ooOo0OoO :
   if OOoOOo0O00O in I1111i . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oO0o0 , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . IIiIi1iI
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 20 - 20: OooOO000 + I11i . O00OOo00oo0o / Ii
    if 7 - 7: OOooOOo / OOooOOo . O00OOo00oo0o * o0o00Oo0O + OOoOoo + oo0oO00
    if 98 - 98: IIiIiII11i * OOoOoo - oOo0O0Ooo % I11i - OooOO000 % Ii1I
    if 69 - 69: ooOoO0O00 % oO0o % O00OOo00oo0o / IIiIi1iI / IIiIi1iI
    if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * IIiIi1iI
    if 47 - 47: o0o00Oo0O
    if 55 - 55: oO0o % o0o00Oo0O / ii
    if 49 - 49: oOo0O0Ooo . oO0o * ii % Ii + iI11I1II1I1I * ooOoO0O00
    if 88 - 88: Ii1I * OooOO000 + IIiIiII11i
    if 62 - 62: ii
    if 33 - 33: o0o00Oo0O . Ii % I11i
    if 50 - 50: IIiIi1iI
    if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * IIi
    if 83 - 83: Ii - oOo0O0Ooo * Ii
    if 59 - 59: OooOO000 - ii / IIiIi1iI + Ii1I . I11i - OooOO000
    if 29 - 29: oo0oO00
    if 26 - 26: o0o00Oo0O % IIi - OOoOoo . IIi
    if 70 - 70: I11i + iiII11i1I1IIi / OooOO000 + IIiIi1iI / oOo0O0Ooo
 if oOOOOOoOO != 'Failed' :
  IiiIIIiI1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOOOOOoOO )
  for oO0o0 , Iiii1iI1i , iIiiii , iiii11i , I1111i in IiiIIIiI1ii :
   if OOoOOo0O00O in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source APPRENTICE[/COLOR]' ) , oO0o0 , 222 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 33 - 33: ii . o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 59 - 59: iI11I1II1I1I
    if 45 - 45: o0o00Oo0O
    if 78 - 78: iiII11i1I1IIi - iI11I1II1I1I + O00OOo00oo0o - Ii1I - O00OOo00oo0o
    if 21 - 21: ii . o0o00Oo0O / Ii
    if 86 - 86: OOooOOo / IIi
    if 40 - 40: iI11I1II1I1I / IIiIi1iI / oOo0O0Ooo + Ii1I * IIi
    if 1 - 1: oO0o * IIiIi1iI + OOoOoo . oo0oO00 / IIiIi1iI
    if 91 - 91: iIi1i1ii1 + iiII11i1I1IIi - I1ii11iIi11i % OOooOOo . OooOO000
    if 51 - 51: IIi / iiII11i1I1IIi
    if 51 - 51: IIiIi1iI * oo0oO00 - O00OOo00oo0o + OooOO000
 OO0 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 46 - 46: I11i - Ii % oO0o / iIi1i1ii1 - OOooOOo
 for i1I11iIiII in OO0 :
  OO0OO0OO = OOOO0OOoO0O0 + i1I11iIiII + IIiiiiiiIi1I1
  i11i1Ii1 = OOoOO0oo0ooO ( OO0OO0OO )
  if i11i1Ii1 != 'Failed' :
   o0oO0oo0000OO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i11i1Ii1 )
   for oO0o0 , Iiii1iI1i , iIiiii , iiii11i , I1111i in o0oO0oo0000OO :
    if OOoOOo0O00O in I1111i . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , oO0o0 , 222 , Iiii1iI1i , iiii11i , iIiiii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 88 - 88: oo0oO00 * oOo0O0Ooo / oO0o - IIi / ooOoO0O00 . O00OOo00oo0o
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 26 - 26: Ii - IIiIi1iI
 OO0 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 45 - 45: IIiIi1iI + IIiIiII11i % OooOO000
 if 55 - 55: IIiIi1iI - oo0oO00 % oOo0O0Ooo
 for i1I11iIiII in OO0 :
  OO0OO0OO = iI + i1I11iIiII
  OoOoOo0 = OOoOO0oo0ooO ( OO0OO0OO )
  if OoOoOo0 != 'Failed' :
   i1II11II1 = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( OoOoOo0 )
   for IiiiI1 , I1111i in i1II11II1 :
    if OOoOOo0O00O in I1111i . lower ( ) :
     OoO ( ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iI + i1I11iIiII + IiiiI1 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 61 - 61: IIiIi1iI
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: iI11I1II1I1I / IIiIi1iI / oOo0O0Ooo - I11i
def ii1I ( ) :
 if 21 - 21: oo0oO00 . Ii * iiII11i1I1IIi . IIi / IIi
 if 42 - 42: ii / O00OOo00oo0o . I11i / o0o00Oo0O - OOoOoo * OOoOoo
 if 1 - 1: iIi1i1ii1 % O00OOo00oo0o
 if 97 - 97: OOooOOo
 if 13 - 13: OOooOOo % IIi . o0o00Oo0O / I1ii11iIi11i % I1ii11iIi11i
 if 19 - 19: O00OOo00oo0o % IIiIi1iI - IIiIi1iI % oOo0O0Ooo . IIi - ii
 if 100 - 100: oOo0O0Ooo + iIi1i1ii1 + I11i . ooOoO0O00 % ii
 if 64 - 64: o0o00Oo0O % ooOoO0O00 * O00OOo00oo0o - iIi1i1ii1 + I1ii11iIi11i
 if 65 - 65: OOooOOo . Ii
 if 36 - 36: oo0oO00 * OooOO000 + OOoOoo * OooOO000 . Ii1I - iI11I1II1I1I
 if 14 - 14: iiII11i1I1IIi * oo0oO00 + Ii
 if 84 - 84: OooOO000 / IIiIiII11i
 if 86 - 86: oOo0O0Ooo
 if 97 - 97: IIiIiII11i
 if 38 - 38: oOo0O0Ooo
 if 42 - 42: I11i
 if 8 - 8: Ii / IIiIi1iI
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 oO0o0 = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllc2dvLnRvL3NlYXJjaC8=' ) ) + ( OOoOOo0O00O ) . replace ( ' ' , '%20' )
 Oo0O = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 o0O0O0ooo0oOO = 'http://onlinemovies.tube/?s=' + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 I1Ii11iiiI = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 II1Ii = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 O0OoOOO00 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiIii1I ) . replace ( ' ' , '+' )
 o0ooOo0OOOO0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 33 - 33: O00OOo00oo0o * OOoOoo - o0o00Oo0O + oOo0O0Ooo / OOoOoo
 IIII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 IIiii1I1I = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 iI1iiiIiii = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 19 - 19: ooOoO0O00 % IIiIiII11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 85 - 85: OOoOoo - I11i % IIi - IIiIiII11i
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 I1 = OOoOO0oo0ooO ( oO0o0 )
 o0oOoO00o . update ( 7 , "" , "Checking Source 1/11 Links" )
 oo0o = OOoOO0oo0ooO ( Oo0O )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 iii1i1iiiiIi = OOoOO0oo0ooO ( o0O0O0ooo0oOO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 Iiii = OOoOO0oo0ooO ( I1Ii11iiiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 OO0OoO0o00 = OOoOO0oo0ooO ( II1Ii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 iII1Iii1I11i = cloudflare . source ( O0OoOOO00 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 7/11 Links" )
 OoOoOo0 = OOoOO0oo0ooO ( o0ooOo0OOOO0o )
 o0oOoO00o . update ( 76 , "" , "Checking Source 8/11 Links" )
 if 56 - 56: iIi1i1ii1 * Ii
 if 92 - 92: IIiIiII11i - o0o00Oo0O . O00OOo00oo0o
 ooOo = OOoOO0oo0ooO ( IIII )
 o0oOoO00o . update ( 95 , "" , "Checking Source 10/11 Links" )
 i11i1Ii1 = OOoOO0oo0ooO ( IIiii1I1I )
 o0oOoO00o . update ( 97 , "" , "Checking Source 11/11 Links" )
 o0oO0OoO0 = OOoOO0oo0ooO ( iI1iiiIiii )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 59 - 59: OOooOOo
 if i11i1Ii1 != 'Failed' :
  o0oO0oo0000OO = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i11i1Ii1 )
  for oO0o0 , I1111i in o0oO0oo0000OO :
   o00OooooOOOO = OOoOO0oo0ooO ( oO0o0 )
   oo000oiIIIII = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( o00OooooOOOO )
   for Oo0O , oOOoOo0Ooo in oo000oiIIIII :
    if iiIii1I in oOOoOo0Ooo . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + oOOoOo0Ooo + '-[COLORgold] source ' + I1111i + '[/COLOR]' ) , oO0o0 + Oo0O , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 47 - 47: IIiIiII11i - Ii1I - iIi1i1ii1
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if ooOo != 'Failed' :
  Oo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOo )
  for oO0o0 , Iiii1iI1i , iIiiii , iiii11i , I1111i in Oo :
   if iiIii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] source HeroVision[/COLOR]' ) , oO0o0 , 1016 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 9 - 9: Ii1I - OOoOoo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 64 - 64: ooOoO0O00
    if 71 - 71: OOoOoo * I11i
    if 99 - 99: I11i
    if 28 - 28: ii % o0o00Oo0O - IIi / I11i / oOo0O0Ooo
    if 41 - 41: IIiIiII11i * OOoOoo / oO0o . oo0oO00
    if 50 - 50: ii + iI11I1II1I1I / oo0oO00 / IIi . Ii . IIiIi1iI
    if 75 - 75: iI11I1II1I1I % IIiIi1iI / IIi - OooOO000 % Ii
    if 11 - 11: iiII11i1I1IIi . iIi1i1ii1
    if 87 - 87: IIi + IIi
    if 45 - 45: ooOoO0O00 - I1ii11iIi11i
    if 87 - 87: OOooOOo - oO0o * oO0o / iIi1i1ii1 . iiII11i1I1IIi * I11i
 if o0oO0OoO0 != 'Failed' :
  iIIIIiiIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0oO0OoO0 )
  for oO0o0 , Iiii1iI1i , iIiiii , iiii11i , I1111i in iIIIIiiIii :
   if iiIii1I in I1111i . lower ( ) :
    oo000ii ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORred] RaizTv[/COLOR]' , oO0o0 , 1016 , Iiii1iI1i )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 21 - 21: IIiIiII11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  iiIIi = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for oO0o0 , o00O0O , I1111i , i1i in i1I :
   if iiIii1I in I1111i . lower ( ) :
    if 'season' in i1i :
     oo000ii ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90054 , o00O0O , o00O0O , '' )
    if 'episodes' in i1i :
     oo000ii ( '[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90044 , o00O0O , o00O0O , '' )
  for oO0o0 in iiIIi :
   oo000ii ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90053 , oOOOo00O00oOo + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 29 - 29: OOooOOo % iIi1i1ii1
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  OOOooo0OooOoO = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( oo0o )
  for oO0o0 , I1111i , o00O0O in OOOooo0OooOoO :
   if iiIii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oO0o0 , 8022 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 7 - 7: ooOoO0O00 / OOoOoo / OooOO000
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for o00O0O , oO0o0 , I1111i in IIIII11I1IiI :
   if iiIii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - WatchSeries[/COLOR]' , 'http://www.watchseriesgo.to' + oO0o0 , 10044 , 'http://www.watchseriesgo.to/' + o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Source WatchSeries Links" )
    if 97 - 97: oO0o + iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for I1111i in ooOoO00 :
   if iiIii1I in I1111i . lower ( ) :
    oo000ii ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( I1Ii11iiiI + I1111i ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 79 - 79: IIiIi1iI + oo0oO00 - IIiIiII11i . I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for I1111i in Iii1I1111ii :
   if iiIii1I in I1111i . lower ( ) :
    oo000ii ( ( '[COLORred]*[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( II1Ii + I1111i ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 26 - 26: OOoOoo
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iII1Iii1I11i != 'Failed' :
  oOoOOOo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iII1Iii1I11i )
  for oO0o0 , o00O0O , I1111i in oOoOOOo :
   if iiIii1I in I1111i . lower ( ) :
    oo000ii ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] Source - Dizi[/COLOR]' , oO0o0 , 8062 , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 52 - 52: o0o00Oo0O + IIiIi1iI
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if OoOoOo0 != 'Failed' :
  i1II11II1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOoOo0 )
  for oO0o0 , Iiii1iI1i , iIiiii , iiii11i , I1111i in i1II11II1 :
   if iiIii1I in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + I1111i + '-[COLORgold] Source Scooby[/COLOR]' ) , oO0o0 , 1016 , Iiii1iI1i , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 11 - 11: ooOoO0O00 / O00OOo00oo0o * Ii1I * O00OOo00oo0o * IIiIi1iI - Ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 96 - 96: Ii1I % Ii1I
 IiI1IIIII1I = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for i1I11iIiII in IiI1IIIII1I :
  OO0OO0OO = OOOO0OOoO0O0 + i1I11iIiII + IIiiiiiiIi1I1
  oOOOOOoOO = OOoOO0oo0ooO ( OO0OO0OO )
  if oOOOOOoOO != 'Failed' :
   IiiIIIiI1ii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOOOOOoOO )
   for I1111i , iIiiii , oO0o0 , o00O0O , o0ooooO0o0O , Ii11iiI in IiiIIIiI1ii :
    if iiIii1I in I1111i . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , oO0o0 , Ii11iiI , o00O0O , o0ooooO0o0O , iIiiii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 1 - 1: oOo0O0Ooo . iIi1i1ii1
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 26 - 26: oo0oO00 - IIiIi1iI % I1ii11iIi11i - oo0oO00 + OOoOoo
     if 33 - 33: iIi1i1ii1 + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * OOoOoo
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii11Ii1iii1I1 ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( OOoOOo0O00O ) . replace ( ' ' , '+' )
 if 65 - 65: o0o00Oo0O * oo0oO00 * IIiIiII11i . iiII11i1I1IIi - ooOoO0O00 * OOooOOo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = OOoOO0oo0ooO ( oO0o0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 28 - 28: iiII11i1I1IIi % O00OOo00oo0o
 if I1 != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for oO0o0 , I1111i in i1I :
   if OOoOOo0O00O in I1111i . lower ( ) :
    OoO ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oO0o0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 49 - 49: OOoOoo % I11i . Ii1I / IIi . iIi1i1ii1 * Ii1I
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
II1i1iii1iiiI = '{ZH},' ; o0O000O00o = '{IX},' ; iiooo = '{LM},'
if 42 - 42: ii % iiII11i1I1IIi % OOoOoo
def O0OoO0OOo ( url ) :
 iIiI111ii1Ii = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iIiI111ii1Ii )
 for url , iIIiii1 , oOOoO , I1111i in IIIII11I1IiI :
  oo000ii ( ( iIIiii1 ) . replace ( 'Sezon' , ' Season ' ) + ( oOOoO ) . replace ( 'Bölüm' , ' Episode ' ) + I1111i , url , 8063 , '' )
  if 59 - 59: o0o00Oo0O . I11i % Ii1I * oo0oO00 + iiII11i1I1IIi
  if 82 - 82: ii
  if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
  if 27 - 27: Ii % OooOO000 + iIi1i1ii1 . IIi
def iIIi1I1 ( url ) :
 iIiI111ii1Ii = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iIiI111ii1Ii )
 for url , I1111i in IIIII11I1IiI :
  OoO ( I1111i , url , 222 , '' )
  if 100 - 100: Ii . IIi . Ii
  if 81 - 81: oOo0O0Ooo
  if 76 - 76: o0o00Oo0O - IIiIi1iI / iIi1i1ii1 . I1ii11iIi11i - iIi1i1ii1
  if 75 - 75: IIiIi1iI % IIi / I11i % IIiIiII11i
def ii1IiI1i ( ) :
 if 83 - 83: Ii - I1ii11iIi11i
 iIiI111ii1Ii = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIiI111ii1Ii )
 for oO0o0 , o00O0O , I1111i , oOOoO in IIIII11I1IiI :
  oo000ii ( I1111i + '  -  ' + ( oOOoO ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oO0o0 , 8063 , o00O0O )
  if 5 - 5: Ii1I . IIiIiII11i . ooOoO0O00
def iIIIIi ( ) :
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i , o00O0O in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 8002 , o00O0O )
def iiII ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , time , url , I1111i , I1iII1IIi1IiI in IIIII11I1IiI :
  iiOOooooO0Oo ( '%s %s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , time ) , url , 1015 , o00O0O , I1iII1IIi1IiI )
  if 83 - 83: Ii + oo0oO00 % ooOoO0O00 . OOoOoo + Ii1I
def OOOoooooO0oOOoO ( ) :
 if 26 - 26: O00OOo00oo0o / O00OOo00oo0o + I1ii11iIi11i - I11i % IIiIiII11i . ii
 oo000ii ( 'Coronation Street' , '' , 8001 , '' )
 oo000ii ( 'Eastenders' , '' , 8002 , '' )
 oo000ii ( 'Emmerdale' , '' , 8003 , '' )
 oo000ii ( 'Hollyoaks' , '' , 8004 , '' )
 oo000ii ( 'Im a Celebrity' , '' , 8005 , '' )
 if 7 - 7: IIiIiII11i - Ii1I / iiII11i1I1IIi % ii + ooOoO0O00
 if 42 - 42: iiII11i1I1IIi + ooOoO0O00 - iIi1i1ii1 / OOoOoo . OooOO000
 if 30 - 30: I1ii11iIi11i + iIi1i1ii1 % Ii * ooOoO0O00 + oOo0O0Ooo % IIi
 if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % O00OOo00oo0o
def OOOo0o ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Holly' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oO0o0 :
    OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 98 - 98: o0o00Oo0O % Ii % IIi
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 6 - 6: O00OOo00oo0o / iIi1i1ii1 / OooOO000 + oOo0O0Ooo / I1ii11iIi11i % ooOoO0O00
def iII ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'East' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oO0o0 :
    OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 73 - 73: oo0oO00 - Ii1I / ii - oO0o / oOo0O0Ooo
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 23 - 23: iiII11i1I1IIi * O00OOo00oo0o * I11i - oOo0O0Ooo % OOooOOo + I11i
def I1ii11ii1iiI ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Emmer' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oO0o0 :
    OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 93 - 93: OOooOOo + iiII11i1I1IIi
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 27 - 27: iI11I1II1I1I * iiII11i1I1IIi
def iiI1iiiii ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Coro' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oO0o0 :
    OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 53 - 53: I11i / I1ii11iIi11i / OooOO000 + iIi1i1ii1 - oO0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 18 - 18: oo0oO00 * o0o00Oo0O - oOo0O0Ooo + o0o00Oo0O + O00OOo00oo0o
def OOO00OOOO0o ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Celeb' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oO0o0 :
    OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 70 - 70: iI11I1II1I1I
def ooOO0o ( name , url ) :
 oOooo0O = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if oOooo0O :
  OOO0 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIIII = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( iIIII ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIIII = open_url ( url )
  II11i1iiI111 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( iIIII ) [ - 1 ]
  OOO0 = II11i1iiI111 . replace ( '\\/' , '/' )
 ooO0oO00O0o = xbmcgui . ListItem ( name , '' , '' )
 ooO0oO00O0o . setPath ( OOO0 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooO0oO00O0o )
 if 35 - 35: O00OOo00oo0o * iiII11i1I1IIi
 if 53 - 53: oo0oO00 / iI11I1II1I1I - iI11I1II1I1I
def I1OooO00Oo ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oO0o0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for oO0o0 , I1111i in i1I :
  oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oO0o0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 81 - 81: Ii1I - oO0o * oo0oO00
def O0O00000o ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Movies' in I1111i :
   oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( oO0o0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def oOOOoOo00O0 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 for url in i1I :
  oo000ii ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 86 - 86: iI11I1II1I1I * OooOO000 * iIi1i1ii1 / oO0o % IIiIi1iI - o0o00Oo0O
  if 63 - 63: Ii1I
def ii1IIII ( url ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , o00O0O )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
II1IiiI = '{UJ},' ; ooO0O0OOO = '{WE},' ; IiIII = '{WP},' ; OOo00O0O = '{PP},'
def III ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiI1i1111iI1i ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OoO00o ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoO00o ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: ii % Ii % I11i % O00OOo00oo0o - IIiIi1iI + iI11I1II1I1I
 if 98 - 98: o0o00Oo0O / oo0oO00 / OooOO000
 if 83 - 83: O00OOo00oo0o
def iiIi1iIiI ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '(cooltvseries.com)' in I1111i :
   OoO ( ( '[COLOR' + II + ']' + I1111i + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , I1111i in i1I :
  if '(cooltvseries.com)' in I1111i :
   OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def IIi1iii ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( ( url ) . replace ( ' ' , '%20' ) )
ii1Ii = '{XX},' ; IIIIi11111 = '{UD},' ; Oo0o00o0oOoo0 = '{YT},' ; I1II = '{JS},' ; o000iiI11i = '{PF},'
if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
def OOo0iIiiI11II11 ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i , o00O0O in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oO0o0 ) ) , 222 , o00O0O )
  if 75 - 75: O00OOo00oo0o - OooOO000 . oo0oO00
def IiIi1II111I ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  if 'youtu' in url :
   OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + o00O0O )
 for url in next :
  oo000ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 88 - 88: OooOO000 - ii . IIiIi1iI - I11i / OOooOOo % iiII11i1I1IIi
def o00O00o ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 69 - 69: ooOoO0O00 . iIi1i1ii1
def oO0O00O0O0o ( url ) :
 iIIII = O000oo
 IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , o00O0O )
  if 41 - 41: iIi1i1ii1 . Ii + o0o00Oo0O - ii * oo0oO00
  if 33 - 33: IIiIi1iI
  if 68 - 68: oOo0O0Ooo . O00OOo00oo0o * oO0o % ii
  if 8 - 8: o0o00Oo0O * oOo0O0Ooo - OOooOOo + Ii1I
  if 4 - 4: IIiIiII11i % oo0oO00 + I11i / Ii
def IiIII1I1Iii1 ( ) :
 if 34 - 34: oo0oO00 - IIiIiII11i - I11i + OooOO000 + O00OOo00oo0o
 oo000ii ( 'All Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'Entertainment' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'Movies' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'Music' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'News' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'Sports' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'Documentary' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'Kids' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'Food' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'Religious' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'USA Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 oo000ii ( 'Other' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 if 70 - 70: ii + oO0o * I1ii11iIi11i
 if 20 - 20: Ii - IIiIiII11i - IIiIi1iI % oo0oO00 . IIiIi1iI
def IiI1I1 ( Cat_Name ) :
 if 16 - 16: Ii1I / iiII11i1I1IIi + I11i % Ii % IIi - iIi1i1ii1
 II11I1iIi1i1 = False
 IiiIIIi1Iii1 = '0'
 if Cat_Name == 'All Channels' : II11I1iIi1i1 = True
 if Cat_Name == 'Entertainment' : IiiIIIi1Iii1 = '1'
 if Cat_Name == 'Movies' : IiiIIIi1Iii1 = '2'
 if Cat_Name == 'Music' : IiiIIIi1Iii1 = '3'
 if Cat_Name == 'News' : IiiIIIi1Iii1 = '4'
 if Cat_Name == 'Sports' : IiiIIIi1Iii1 = '5'
 if Cat_Name == 'Documentary' : IiiIIIi1Iii1 = '6'
 if Cat_Name == 'Kids' : IiiIIIi1Iii1 = '7'
 if Cat_Name == 'Food' : IiiIIIi1Iii1 = '8'
 if Cat_Name == 'Religious' : IiiIIIi1Iii1 = '9'
 if Cat_Name == 'USA Channels' : IiiIIIi1Iii1 = '10'
 if Cat_Name == 'Other' : IiiIIIi1Iii1 = '11'
 if 69 - 69: iIi1i1ii1 * ooOoO0O00 % I11i * Ii1I * iI11I1II1I1I
 iIIII = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIII )
 print 'Len Match: >>>' + str ( len ( IIIII11I1IiI ) )
 for I1111i , o00O0O , i1i111i1I1 in IIIII11I1IiI :
  I1IIo0o0OoOO00Oo = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  if i1i111i1I1 == IiiIIIi1Iii1 :
   oo000ii ( I1111i , '' , 7022 , I1IIo0o0OoOO00Oo )
  elif II11I1iIi1i1 == True :
   oo000ii ( I1111i , '' , 7022 , I1IIo0o0OoOO00Oo )
  else : pass
  if 33 - 33: OooOO000 % ii / oo0oO00
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 12 - 12: Ii1I - iI11I1II1I1I * OOooOOo + I11i . iiII11i1I1IIi
def o0iIiii ( Search_Name ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , oO0o0 , o0O0O0ooo0oOO , I1Ii11iiiI in IIIII11I1IiI :
  I1IIo0o0OoOO00Oo = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  OoO ( Search_Name + ': Link 1' , ( oO0o0 ) . replace ( '\\' , '' ) , 222 , I1IIo0o0OoOO00Oo )
  OoO ( Search_Name + ': Link 2' , ( o0O0O0ooo0oOO ) . replace ( '\\' , '' ) , 222 , I1IIo0o0OoOO00Oo )
  OoO ( Search_Name + ': Link 3' , ( I1Ii11iiiI ) . replace ( '\\' , '' ) , 222 , I1IIo0o0OoOO00Oo )
  if 73 - 73: OooOO000 * OooOO000 + I11i
def ii1i11Ii11iI ( ) :
 iIIII = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OoO ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def IiIIi1iIii1I1 ( ) :
 iIIII = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OoO ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def ii1oo ( ) :
 iIIII = O000oo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OoO ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
def IIII11i1Ii ( url ) :
 url
 i11I = xbmcgui . ListItem ( I1111i , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11I )
 return
 if 13 - 13: IIiIi1iI * oO0o % iI11I1II1I1I / OOoOoo * OooOO000 . I1ii11iIi11i
 if 23 - 23: IIiIi1iI / OOoOoo . OooOO000 * iIi1i1ii1
def oOiIiii1III ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIIII )
 for url , iIiiii , o00O0O , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + o00O0O , '' , ( iIiiii ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  oo000ii ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 100 - 100: OOoOoo + ooOoO0O00 * oO0o
def oOooOO0oOo0O0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , iIiiii , o00O0O in IIIII11I1IiI :
  OOiIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + o00O0O , '' , iIiiii )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 IIiiIii11 = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for I1iiii1iiiI in IIiiIii11 :
  o000O0O = ( I1iiii1iiiI ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiOOooooO0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + o00O0O , '' , o000O0O )
  if 1 - 1: ooOoO0O00
def iIiiIIiI11 ( INFO ) :
 OO0O000 ( 'info for workout' , INFO )
 if 49 - 49: I1ii11iIi11i % oo0oO00
 if 49 - 49: O00OOo00oo0o * oo0oO00 / I11i
 if 78 - 78: OOoOoo + iiII11i1I1IIi - I11i + oO0o / iI11I1II1I1I
def ii111I111i ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  oo000ii ( ( I1111i ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def II11111I ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def OOoo ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   OoO ( ( I1111i ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def OO0ooOO00o0 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   OoO ( I1111i , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 29 - 29: IIiIiII11i - OooOO000 / oo0oO00 % ii % OooOO000 + OOoOoo
   if 44 - 44: o0o00Oo0O / o0o00Oo0O
   if 25 - 25: I11i + iI11I1II1I1I + OOoOoo + Ii1I / O00OOo00oo0o - ooOoO0O00
def Ii1I11Ii1iI ( url ) :
 OoO ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , oOOOo00O00oOo + 'bamf.png' , oOOOo00O00oOo + 'bamf.png' )
 OoO ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , oOOOo00O00oOo + 'bamf.png' , oOOOo00O00oOo + 'bamf.png' )
 oo000ii ( '[COLOR' + II + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , oOOOo00O00oOo + 'bamf.png' )
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  if 'mp4' in url :
   pass
  else :
   OoO ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'bamf.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOOOo00OOoO ( url ) :
 OoO ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 OoO ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 oo000ii ( '[COLOR' + II + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , oOOOo00O00oOo + 'bamf.png' )
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  if 'mp4' in url :
   OoO ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'bamf.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 40 - 40: OooOO000
 if 76 - 76: ooOoO0O00 % oOo0O0Ooo / oo0oO00 * OOoOoo % iI11I1II1I1I - o0o00Oo0O
 if 84 - 84: ooOoO0O00
def OooO00OOooOO ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Daily' in I1111i :
   oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 9008 , Oo00OOOOO )
def oooOOoOo0 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def iii ( url ) :
 OoO ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 OoO ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 OoO ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  OoO ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , Oo00OOOOO )
  if 12 - 12: OOooOOo % IIi + oo0oO00 . o0o00Oo0O % iI11I1II1I1I
def ii1IO00oO0oOOOOOO ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if '.m3u' in oO0o0 :
   oo000ii ( ( I1111i ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oO0o0 ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def Oo0ooo00OoO ( url ) :
 iIIII = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  OoO ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 1 - 1: ii * iI11I1II1I1I / Ii1I * iiII11i1I1IIi
def oOoO00o ( ) :
 iIIII = O000oo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'category' in oO0o0 :
   oo000ii ( I1111i , 'http://www.disclose.tv/' + oO0o0 , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 37 - 37: OooOO000 % iiII11i1I1IIi . OooOO000 - IIi / iI11I1II1I1I - IIi
   if 50 - 50: o0o00Oo0O
def oOOoOIi11 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIII )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  oo000ii ( I1111i , 'http://www.disclose.tv/' + url , 7011 , o00O0O )
 for url in next :
  oo000ii ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 78 - 78: IIiIi1iI
  if 94 - 94: ii + OOooOOo / o0o00Oo0O
def o0O0ooooO0 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  if 'http' in url :
   OoO ( 'video/flv' , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url , I1111i in i1I :
  OoO ( I1111i , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url in ooOoO00 :
  OoO ( 'YT Link' , url , 8043 , oOOOo00O00oOo + 'disclose.png' )
  if 35 - 35: OooOO000 * IIi
  if 65 - 65: IIiIiII11i % ooOoO0O00
def III1II1iiI11 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
  if 38 - 38: ooOoO0O00 / iI11I1II1I1I + OooOO000
def iI1Oo ( name , url , img ) :
 I1 = O000oo ( url )
 OoO0ooOO = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1 )
 OOoo000Ooo = len ( OoO0ooOO )
 if 46 - 46: ooOoO0O00 + o0o00Oo0O
 if 5 - 5: I11i + oOo0O0Ooo / ii % Ii % ii - I11i
 if OOoo000Ooo == 1 :
  for oOooooo in OoO0ooOO :
   oOooooo = oOooooo . replace ( 'player' , 'watch' )
   OO00 = oOooooo + '&fv=&sou='
   iI1iII1 = O000oo ( OO00 )
   o0iiI11 = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( iI1iII1 )
   for Ooo0oo in o0iiI11 :
    IiiiIII1i = False
    Resolve ( Ooo0oo )
    if 72 - 72: oo0oO00 * Ii / IIiIi1iI / iIi1i1ii1 . Ii
 elif OOoo000Ooo > 1 :
  if 62 - 62: IIiIiII11i % OooOO000 % I1ii11iIi11i * oo0oO00
  for oOooooo in OoO0ooOO :
   OoO00OOoO = O000oo ( oOooooo )
   iiiI = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OoO00OOoO )
   iii1OO00Oo00o = iiiI
   iii1OO00Oo00o = ( str ( iii1OO00Oo00o ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iii1OO00Oo00o
   OoO ( 'DOUBLE LINK' , iii1OO00Oo00o , 424 , '' )
   if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . IIi
   for url in iiiI :
    oo000ii ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     o0O0O0ooo0oOO = Google . resolve ( url )
    except :
     pass
    try :
     Ii1111i11 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( o0O0O0ooo0oOO ) )
     for O0Ooo000OO00 , O000oo0O0OO0 in Ii1111i11 :
      if 58 - 58: oO0o - ii . OooOO000
      HD_URLS . append ( O0Ooo000OO00 )
      SD_URLS . append ( O000oo0O0OO0 )
    except :
     pass
 else :
  pass
  if 26 - 26: OOooOOo
def i1IiIiIii11I ( ) :
 if 80 - 80: O00OOo00oo0o + iiII11i1I1IIi . O00OOo00oo0o + IIi
 if 85 - 85: Ii . iiII11i1I1IIi + iIi1i1ii1 / iIi1i1ii1
 oo000ii ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 43 - 43: OOoOoo . ii - IIiIiII11i
 oo000ii ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * IIi * oo0oO00
 if 19 - 19: O00OOo00oo0o * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
def IIiI ( ) :
 iIIII = O000oo ( 'http://cnfstudio.com/' )
 IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , 'http://cnfstudio.com/genre/' + oO0o0 , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 11 - 11: IIiIi1iI
OOooO0OOoo = xbmcgui . Dialog ( )
if 36 - 36: oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
O0ooO00OO = '{UN},' ; IiI11I1I111 = '{IG},' ; o00OoOoo0 = '{PL},' ; iiiiiiiiiiiI = '{LO},' ; iI111iiI1II = '{LP},' ; OOOoooO000O0 = '{HA},' ; OOO0o0OO = '{XD},' ; Ii1iIi = '{TA},' ; II1oOO0O0Ooo0 = '{DP},' ; I11iiI1i = '{JT},' ; ooOoOO = '{JJ},' ; iIiiII11 = '{MM},' ; OOo0oo0 = '{FQ},' ; i1I1I1 = '{HH},'
if 31 - 31: iIi1i1ii1 / OooOO000
def iI1111iI1iII ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIIII )
 o0ooo0 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIIII )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , o00O0O )
 o0ooo0 = o0ooo0
 for url in o0ooo0 :
  oo000ii ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 80 - 80: IIi * oO0o + iIi1i1ii1
def oo0iI1IIIi11iIII ( url ) :
 if 72 - 72: OOoOoo . Ii1I / oO0o * Ii % oO0o % IIiIi1iI
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  i1Oo00 = url + '&fv=&sou='
  i1Oo00 = i1Oo00 . replace ( 'player' , 'watch' )
  i1iOO = IiIII1i ( i1Oo00 )
  OOoOooO0O = IiIII1i ( url )
  if 88 - 88: IIiIi1iI % IIi . oO0o
  if 31 - 31: oOo0O0Ooo - ii . OOoOoo
def IiIII1i ( url ) :
 if 12 - 12: iiII11i1I1IIi . iIi1i1ii1 + iiII11i1I1IIi - IIi * OooOO000 - o0o00Oo0O
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  I1Ii ( url )
  if 44 - 44: ooOoO0O00 % oo0oO00 / OOooOOo % OOoOoo . Ii1I
  if 38 - 38: OOooOOo . iiII11i1I1IIi
def oOOoooOoO0o0 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , O0o0Oo , '' )
 if 51 - 51: oo0oO00
def Ii1111I1IIi1 ( ) :
 if os . path . exists ( iiI1IiI ) :
  oo00iiIIiIi1Ii1 = open ( iiI1IiI , 'r' )
  for i11I in oo00iiIIiIi1Ii1 :
   OoOoOOO000 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( i11I )
   for I1111i , oO0o0 in OoOoOOO000 :
    OoO ( I1111i , oO0o0 , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 57 - 57: I11i - OOoOoo . IIi
def IIiIi ( url ) :
 if os . path . exists ( Remote ) :
  I1 = oo00ooOoO00 ( url )
  IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for I1111i , url in IIIII11I1IiI :
   url = ( url ) . strip ( )
   OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 45 - 45: I1ii11iIi11i
  if 4 - 4: iiII11i1I1IIi
def Iiii1i1 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for oO0o0 in IIIII11I1IiI :
  oO0o0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oO0o0
 I1111i = 'plugin.video.GenieTv'
 if 60 - 60: IIiIiII11i + O00OOo00oo0o / oo0oO00 % ii - ooOoO0O00
 o0OOO00O0OOoO ( oO0o0 , I1111i )
 if 93 - 93: OooOO000 . Ii
def II1I ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for oO0o0 in IIIII11I1IiI :
  oO0o0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oO0o0
 I1111i = 'repository.GenieTv'
 if 24 - 24: IIi . oO0o + O00OOo00oo0o . oo0oO00 - Ii1I % OooOO000
 o0OOO00O0OOoO ( oO0o0 , I1111i )
 if 49 - 49: o0o00Oo0O . I1ii11iIi11i / iIi1i1ii1
 if 29 - 29: Ii1I / oo0oO00 * o0o00Oo0O - Ii - oO0o + iIi1i1ii1
def iI1i11iII111 ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  Oo0OOo ( )
 if i11I1II1I11i == 1 :
  oOoO000OOoo0 ( )
  if 44 - 44: oO0o % Ii . O00OOo00oo0o - o0o00Oo0O / OooOO000 . IIiIi1iI
  if 23 - 23: I11i % iI11I1II1I1I
  if 62 - 62: iIi1i1ii1 - I11i + iIi1i1ii1 . oO0o % IIiIiII11i - iI11I1II1I1I
  if 54 - 54: ii - iIi1i1ii1 - I11i - Ii1I
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
OO0Oo = 'https://addons.tvaddons.ag/'
if 81 - 81: OooOO000 + OOoOoo - Ii
def oOoO000OOoo0 ( ) :
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 Oo0O0O = 'https://addons.tvaddons.ag/search/?keyword=' + iiIii1I
 I1 = O000oo ( Oo0O0O )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for oO0o0 , IIi1iiii1iI , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , oO0o0 , 10054 , 'https://addons.tvaddons.ag/' + IIi1iiii1iI , O0o0Oo , '' )
  if 60 - 60: O00OOo00oo0o
  if 14 - 14: I1ii11iIi11i % oo0oO00 * OooOO000 - Ii / Ii1I * Ii
def Oo0OOo ( ) :
 I1 = O000oo ( OO0Oo )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  if 'Repositories' in I1111i :
   pass
  elif 'Services' in I1111i :
   pass
  elif 'International' in I1111i :
   pass
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 10053 , 'https://addons.tvaddons.ag/' + o00O0O , O0o0Oo , '' )
   if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * iiII11i1I1IIi + IIi
   if 14 - 14: iIi1i1ii1 - o0o00Oo0O
def Addon ( url ) :
 I1 = O000oo ( url )
 OoOO0Ooo = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  if 'Please' in I1111i :
   pass
  else :
   OOiIiIIi1 ( I1111i , url , 10054 , 'https://addons.tvaddons.ag/' + o00O0O , O0o0Oo , '' )
 for url in OoOO0Ooo :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
  if 95 - 95: oO0o - OOoOoo % O00OOo00oo0o
  if 27 - 27: iI11I1II1I1I / oOo0O0Ooo % OOooOOo / oOo0O0Ooo * iIi1i1ii1
def I1IO0 ( url , name ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
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
   if 7 - 7: OOoOoo * IIiIi1iI + OOooOOo
def o0OOO00O0OOoO ( url , name ) :
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
 if 22 - 22: OooOO000
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 48 - 48: Ii1I . oOo0O0Ooo
 if 73 - 73: o0o00Oo0O . O00OOo00oo0o - ii % iiII11i1I1IIi % ooOoO0O00
def i111II ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , IIi1iiii1iI , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , url , 1007 , IIi1iiii1iI )
def i11iI1I1 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , IIi1iiii1iI , I1111i in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , IIi1iiii1iI )
  if 89 - 89: OooOO000
  if 9 - 9: OOoOoo . iiII11i1I1IIi
def OOoOooOoOOOoo ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , iconimage , iIiiii , o0ooooO0o0O , name in IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    OoooO0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
    for i11I in OoooO0o :
     if i11I == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    o000o0o00Oo ( name , url , 1016 , iconimage , o0ooooO0o0O , iIiiii )
   else :
    if 'youtube' in url :
     OoooO0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for i11I in OoooO0o :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iIii ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , o0ooooO0o0O , iIiiii )
    else :
     OoooO0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for i11I in OoooO0o :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     iIii ( name , url , 222 , iconimage , o0ooooO0o0O , iIiiii )
     I1I11i ( 'tvshows' , 'Media Info 3' )
  else :
   IiIiiiIii1i ( url , iconimage , name )
   if 71 - 71: I11i . Ii1I % IIiIiII11i / iI11I1II1I1I % OOooOOo - Ii1I
 else :
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
  for url , IIi1iiii1iI , name in IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     oo000ii ( name , url , 1016 , IIi1iiii1iI )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OoO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI )
     else :
      OoooO0o = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
      for i11I in OoooO0o :
       if i11I == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OoO ( name , url , 222 , IIi1iiii1iI )
      I1I11i ( 'tvshows' , 'Media Info 3' )
   else :
    IiIiiiIii1i ( url , IIi1iiii1iI , name )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 58 - 58: iI11I1II1I1I + IIiIi1iI / oO0o % IIiIi1iI % I11i % iI11I1II1I1I
def IiIiiiIii1i ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 Ii11iiiIIIi = ( url ) . replace ( o0O000O00o , 'http' ) . replace ( IIIIi11111 , '.com' ) ;
 i111I = ( Ii11iiiIIIi ) . replace ( iiooo , 'a' ) . replace ( iiIiIIiI1 , 'b' ) . replace ( Ii11i , 'c' ) . replace ( ooO0O0OOO , 'd' ) . replace ( o00OoOoo0 , 'e' ) . replace ( I11iiI1i , 'f' ) ;
 O0oO = ( i111I ) . replace ( ii1Ii , 'g' ) . replace ( OOOoooO000O0 , 'h' ) . replace ( Oo0o00o0oOoo0 , 'i' ) . replace ( o000iiI11i , 'j' ) . replace ( O00i1i , 'k' ) . replace ( iiii , 'l' ) ;
 iiIiI111 = ( O0oO ) . replace ( O0oo00O0 , 'm' ) . replace ( iIiiIII , 'n' ) . replace ( ii1IooO00OO0ooo , 'o' ) . replace ( O0oi1i1ii1Ii111i , 'p' ) . replace ( iiiI1iiI11iii , 'q' ) . replace ( o0O0oOOoo0O0 , 'r' ) ;
 OO00OOo = ( iiIiI111 ) . replace ( IiI11i1IiI1 , 's' ) . replace ( IiIII , 't' ) . replace ( o00oOO00 , 'u' ) . replace ( o00O0oOOo , 'v' ) . replace ( i1OOO00oO0O , 'w' ) . replace ( IIi1 , 'x' ) ;
 OOoO0OooO = ( OO00OOo ) . replace ( IiiOo , 'y' ) . replace ( iiiIiii11i1i , 'z' ) . replace ( O0ooO00OO , '.' ) . replace ( IiI11I1I111 , '(' ) . replace ( iiiiiiiiiiiI , ')' ) . replace ( iI111iiI1II , '/' ) ;
 ooo0O0Oo0O = ( OOoO0OooO ) . replace ( II1i1iii1iiiI , '1' ) . replace ( OOo00O0O , '2' ) . replace ( Oo0o , '3' ) . replace ( Ii1iIi , '4' ) . replace ( II1oOO0O0Ooo0 , '5' ) . replace ( I1II , '6' ) ;
 i1iOO00O0O00oOOO = ( ooo0O0Oo0O ) . replace ( ooOoOO , '7' ) . replace ( iIiiII11 , '8' ) . replace ( OOo0oo0 , '9' ) . replace ( i1I1I1 , '0' ) . replace ( OOooO0o , ':' ) . replace ( oo000o0O , '%' ) ;
 url = ( i1iOO00O0O00oOOO ) . replace ( II1IiiI , '-' ) . replace ( OOO0o0OO , '_' ) ;
 OoO ( name , url , 222 , iconimage ) ;
 if 17 - 17: IIiIi1iI
 if 25 - 25: iIi1i1ii1 * iI11I1II1I1I * I11i + OOooOOo . OOooOOo
def IIi1I ( ) :
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for oO0o0 , IIi1iiii1iI , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , oO0o0 , 1007 , IIi1iiii1iI )
def ii11iI11I111I ( url ) :
 if 44 - 44: ooOoO0O00 - Ii1I + Ii1I . iiII11i1I1IIi / IIi
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , IIi1iiii1iI , I1111i in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , IIi1iiii1iI )
  if 48 - 48: Ii1I . o0o00Oo0O . oOo0O0Ooo * I11i / OooOO000
def oO0OO00o ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O0oO0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O0oO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0oO0 )
 if 97 - 97: o0o00Oo0O . I11i
 if 17 - 17: o0o00Oo0O . oo0oO00 - oo0oO00 - ooOoO0O00 * IIi
def IIi1i1 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  if '-dir-' in I1111i :
   oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , o00O0O )
  else :
   oo000ii ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , o00O0O )
   if 16 - 16: OOooOOo / IIiIiII11i
def iIiI1IIiii ( url ) :
 iIIII = oo00ooOoO00 ( url )
 ooIii1I1i1i1 = ( 'http://afewbitsmore.com/' )
 IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '[To Parent Directory]' in I1111i :
   I1111i = 'HOME'
   pass
  elif 'HOME' in I1111i :
   pass
  elif '.m3u' in I1111i :
   oo000ii ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , ooIii1I1i1i1 + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in I1111i :
   OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , ooIii1I1i1i1 + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in I1111i :
   OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , ooIii1I1i1i1 + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ooIii1I1i1i1 + url , 1012 , oOOOo00O00oOo + 'music.png' )
def IiIi11I ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for o00O0O , I1111i , url in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 80 - 80: OOooOOo % I1ii11iIi11i
def oooooOO0 ( url ) :
 iIIII = oo00ooOoO00 ( url )
 ooIii1I1i1i1 = url
 IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '.mp3' in I1111i :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/' , '' ) , ooIii1I1i1i1 + url , 1011 , oOOOo00O00oOo + 'music.png' )
def OOO0o0O ( ) :
 iIIII = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , ( 'http://www.cyn.net/music/' + oO0o0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + o00O0O ) . replace ( ' ' , '%20' ) )
def I111i ( url , img ) :
 iIIII = oo00ooOoO00 ( url )
 o0O0O0ooo0oOO = url
 img = img
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( o0O0O0ooo0oOO + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 39 - 39: Ii1I
def o00o ( url ) :
 iIIII = oo00ooOoO00 ( url )
 o0O0O0ooo0oOO = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for type , url , I1111i in IIIII11I1IiI :
  if '[VID]' in type :
   OoO ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , o0O0O0ooo0oOO + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   o00o ( o0O0O0ooo0oOO + url )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: OOooOOo . I11i
 if 37 - 37: OooOO000 + O00OOo00oo0o * iIi1i1ii1 + OOoOoo
def o0O0Ooo ( ) :
 iI = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 OOoOOo0O00O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiIii1I = OOoOOo0O00O . lower ( )
 oO0o0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 Oo0O = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 o0O0O0ooo0oOO = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + iIi1i1ii1 / IIiIiII11i
 I1 = OOoOO0oo0ooO ( oO0o0 )
 oo0o = OOoOO0oo0ooO ( Oo0O )
 iii1i1iiiiIi = OOoOO0oo0ooO ( o0O0O0ooo0oOO )
 if 66 - 66: IIiIi1iI + oo0oO00 % ii
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for oO0o0 , Iiii1iI1i , iIiiii , iiii11i , I1111i in IIIII11I1IiI :
   if OOoOOo0O00O in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oO0o0 , 1016 , Iiii1iI1i , o0ooooO0o0O , iIiiii )
    if 23 - 23: oo0oO00 . OOooOOo + iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  OOOooo0OooOoO = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oo0o )
  for oO0o0 , I1111i in OOOooo0OooOoO :
   if OOoOOo0O00O in I1111i . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oO0o0 ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'Music.png' )
    if 17 - 17: OOoOoo
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( iii1i1iiiiIi )
  for oO0o0 , I1111i in i1I :
   if OOoOOo0O00O in I1111i . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oO0o0 ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'Music.png' )
    if 12 - 12: ooOoO0O00 . oO0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 14 - 14: IIi + IIiIiII11i % IIi . oo0oO00 * IIiIi1iI
    if 54 - 54: IIiIi1iI * iiII11i1I1IIi - O00OOo00oo0o
    if 15 - 15: OooOO000 / o0o00Oo0O
    if 61 - 61: ooOoO0O00 / ooOoO0O00 + IIiIi1iI . O00OOo00oo0o * IIiIi1iI
    if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
    if 82 - 82: o0o00Oo0O / OooOO000 * oO0o - iiII11i1I1IIi + I1ii11iIi11i
O0oo00O0 = '{SF},' ; iIiiIII = '{IF},' ; ii1IooO00OO0ooo = '{PW},' ; Oo0o = '{AM},' ; O0oi1i1ii1Ii111i = '{GF},' ; iiiI1iiI11iii = '{DD},' ; o0O0oOOoo0O0 = '{UO},' ; IiI11i1IiI1 = '{LE},' ; o00oOO00 = '{ZY},' ; o00O0oOOo = '{UE},' ; i1OOO00oO0O = '{PE},' ; IIi1 = '{JE},' ; IiiOo = '{TH},' ; iiiIiii11i1i = '{LK},'
if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + iIi1i1ii1 * IIiIiII11i
if 78 - 78: O00OOo00oo0o - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
def i1iI1 ( ) :
 iIIII = O000oo ( 'http://www.iwatchseries.me/tv-list/' )
 IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , oO0o0 , 8021 , oOOOo00O00oOo + 'iwatch.png' )
  I1I11i ( 'movies' , 'MAIN' )
def oooO ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIIII )
 for url , I1111i , i11i11II11i in IIIII11I1IiI :
  oo000ii ( I1111i + i11i11II11i , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def II111iiI1Ii1 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oo0oO0oO00oO ( url )
def oo0oO0oO00oO ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iIIII )
 Iii1I1111ii = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  OoO ( 'VidSpot - ' + I1111i , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url in i1I :
  OoO ( 'VodLocker' , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url , I1111i in Iii1I1111ii :
  OoO ( 'VidUp' + I1111i , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for I1111i , url in ooOoO00 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OoO ( 'TheVideo - ' + I1111i , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
   if 94 - 94: IIiIi1iI * IIi
def o00ooo0oOo0o ( ) :
 iIIII = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , oO0o0 , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 97 - 97: I11i . iI11I1II1I1I % OooOO000 * iI11I1II1I1I * iI11I1II1I1I
  if 37 - 37: O00OOo00oo0o . ii / IIiIi1iI + IIiIiII11i
def o0o0O0oOOoO0 ( ) :
 iIIII = O000oo ( 'http://www.animetoon.org/cartoon' )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , oO0o0 , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 3 - 3: OOoOoo % ooOoO0O00 % OOooOOo + Ii1I
  if 41 - 41: OOooOOo / iI11I1II1I1I
  if 92 - 92: iIi1i1ii1 . OooOO000 % O00OOo00oo0o % o0o00Oo0O
def oOooo0ooo ( url ) :
 iIIII = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  Oo00o00Oo = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  oo000ii ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  oo000ii ( I1111i , url , 1003 , Oo00o00Oo )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def Iiii11i11IIi1 ( url , IMAGE ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   oOOo ( url )
  elif 'playpanda' in url :
   oOOo ( url )
   if 78 - 78: oo0oO00 % ii
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOo ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OoO ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 73 - 73: oOo0O0Ooo % IIiIi1iI % OOoOoo + ooOoO0O00 - ii / oo0oO00
  if 78 - 78: ii % oo0oO00 - Ii
def i111iiII1I ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0o0O00Oo0o0 . add_header ( 'referer' , url )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 10 - 10: IIiIi1iI
def oo00ooOoO00 ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 5 - 5: iIi1i1ii1 - iI11I1II1I1I
def oOoOooO00o00 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OOoOooO0o = ( '%s%s' % ( I1IiiiI , url ) )
 i1Oo00 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , IIi1iiii1iI , I1111i in IIIII11I1IiI :
  OoO ( '%s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , IIi1iiii1iI )
  if 64 - 64: OOoOoo . IIi
def oo00Oo0oo0 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  I11Oo0O00O0O00 ( url , I1111i )
 else :
  II1I1i ( url )
def II1I1i ( url ) :
 import urlresolver
 try :
  O00O = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( O00O , xbmcgui . ListItem ( I1111i ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( I1111i ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def I1Ii ( url ) :
 if 80 - 80: oo0oO00
 IIIii1iiIi = open ( oOOoo0Oo , "a" )
 IIIii1iiIi . write ( 'url="' + url + '"\n' )
 IIIii1iiIi . close
 if 54 - 54: OOooOOo % iI11I1II1I1I
 iIIII1i = xbmc . Player ( o00oO0 ( ) )
 import urlresolver
 try : iIIII1i . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( I1111i ) )
 iIIII1i = xbmc . Player ( o00oO0 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  OOooO0OOoo = xbmcgui . Dialog ( )
  if OOooO0OOoo . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   OOooO0OOoo . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : iIIII1i . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def I11Oo0O00O0O00 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  OO0o0O0O0O0 = '.mp4'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   II1I1i ( url )
  if i11I1II1I11i == 1 :
   i111IiiIIi1Ii1 ( url , name , OO0o0O0O0O0 )
 elif '.mkv' in url :
  OO0o0O0O0O0 = '.mkv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   II1I1i ( url )
  if i11I1II1I11i == 1 :
   i111IiiIIi1Ii1 ( url , name , OO0o0O0O0O0 )
 elif '.mp3' in url :
  OO0o0O0O0O0 = '.mp3'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   II1I1i ( url )
  if i11I1II1I11i == 1 :
   i111IiiIIi1Ii1 ( url , name , OO0o0O0O0O0 )
 elif '.avi' in url :
  OO0o0O0O0O0 = '.avi'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   II1I1i ( url )
  if i11I1II1I11i == 1 :
   i111IiiIIi1Ii1 ( url , name , OO0o0O0O0O0 )
 elif '.mov' in url :
  OO0o0O0O0O0 = '.mov'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   II1I1i ( url )
  if i11I1II1I11i == 1 :
   i111IiiIIi1Ii1 ( url , name , OO0o0O0O0O0 )
 elif '.mpeg' in url :
  OO0o0O0O0O0 = '.mpeg'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   II1I1i ( url )
  if i11I1II1I11i == 1 :
   i111IiiIIi1Ii1 ( url , name , OO0o0O0O0O0 )
 elif '.mpg' in url :
  OO0o0O0O0O0 = '.mpg'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   II1I1i ( url )
  if i11I1II1I11i == 1 :
   i111IiiIIi1Ii1 ( url , name , OO0o0O0O0O0 )
 elif '.flv' in url :
  OO0o0O0O0O0 = '.flv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   II1I1i ( url )
  if i11I1II1I11i == 1 :
   i111IiiIIi1Ii1 ( url , name , OO0o0O0O0O0 )
 elif '.wmv' in url :
  OO0o0O0O0O0 = '.wmv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   II1I1i ( url )
  if i11I1II1I11i == 1 :
   i111IiiIIi1Ii1 ( url , name , OO0o0O0O0O0 )
 else :
  II1I1i ( url )
def i111IiiIIi1Ii1 ( url , name , cat ) :
 i1oO00O ( )
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
def i1oO00O ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def iiI1IIi1i1 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 iIIII1i = xbmc . Player ( o00oO0 ( ) )
 o0oOoO00o . update ( 100 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 iIIII1i . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 60 - 60: I11i / I1ii11iIi11i
def OOOOo0o00OO0000 ( url ) :
 iIIII1i = xbmc . Player ( o00oO0 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : iIIII1i . play ( url ) . strip ( )
 except : pass
 if 19 - 19: iI11I1II1I1I . oO0o / ii
def Ii1ii1I1I ( url ) :
 iIIII1i = xbmc . Player ( o00oO0 ( ) )
 import urlresolver
 oOOOOooO = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 iIIII1i . play ( oOOOOooO )
 xbmc . sleep ( 1 )
 iIIII1i . play ( url )
 if 49 - 49: oo0oO00
 if 78 - 78: IIi
def o00oO0 ( ) :
 try :
  o00OOOO000000 = getSet ( "core-player" )
  if ( o00OOOO000000 == 'DVDPLAYER' ) : i1iI1Iiiiii11 = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o00OOOO000000 == 'MPLAYER' ) : i1iI1Iiiiii11 = xbmc . PLAYER_CORE_MPLAYER
  elif ( o00OOOO000000 == 'PAPLAYER' ) : i1iI1Iiiiii11 = xbmc . PLAYER_CORE_PAPLAYER
  else : i1iI1Iiiiii11 = xbmc . PLAYER_CORE_AUTO
 except : i1iI1Iiiiii11 = xbmc . PLAYER_CORE_AUTO
 return i1iI1Iiiiii11
 return True
 if 49 - 49: Ii1I * O00OOo00oo0o + OOooOOo
def oo000ii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1iOOOO = True
 ooO0oO00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooO0oO00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooOO00oOOo000 = [ ]
  ooOO00oOOo000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooOO00oOOo000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooOO00oOOo000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooO0oO00O0o . addContextMenuItems ( ooOO00oOOo000 )
 I1iOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1 , listitem = ooO0oO00O0o , isFolder = True )
 return I1iOOOO
 if 72 - 72: oO0o
def oOoo0OO0 ( name , url , mode , iconimage , fanart , description ) :
 if 57 - 57: IIi / oO0o + Ii1I
 iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1iOOOO = True
 ooO0oO00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooO0oO00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooO0oO00O0o . setProperty ( "Fanart_Image" , fanart )
 I1iOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1 , listitem = ooO0oO00O0o , isFolder = True )
 return I1iOOOO
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % IIi + OOoOoo . oO0o . I1ii11iIi11i
def OoO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 I1iOOOO = True
 ooO0oO00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooO0oO00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooOO00oOOo000 = [ ]
  ooOO00oOOo000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooOO00oOOo000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooOO00oOOo000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooO0oO00O0o . addContextMenuItems ( ooOO00oOOo000 )
 I1iOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1 , listitem = ooO0oO00O0o , isFolder = False )
 return I1iOOOO
 if 70 - 70: iiII11i1I1IIi . Ii1I * oo0oO00
 if 97 - 97: oo0oO00 . iI11I1II1I1I - IIi
 if 23 - 23: Ii1I % iiII11i1I1IIi
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
 if 99 - 99: O00OOo00oo0o - Ii1I - oOo0O0Ooo - O00OOo00oo0o + oO0o + IIiIiII11i
 if 34 - 34: O00OOo00oo0o * iiII11i1I1IIi
def OO0O000 ( heading , announce ) :
 class i1oO0o00oOo00oO ( ) :
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
   try : oooOo0OOOoo0 = open ( announce ) ; O000o0 = oooOo0OOOoo0 . read ( )
   except : O000o0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( O000o0 ) )
   return
 i1oO0o00oOo00oO ( )
 i1oO0o00oOo00oO ( )
 if 68 - 68: iI11I1II1I1I - oOo0O0Ooo . oo0oO00 + OOooOOo
def iI1Ii11iIiI1 ( ) :
 OO0O000 ( 'GenieTv Recomended Sources' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Reaper[/COLOR] [CR]  [COLORred]http://roguemedia.info/cerberus/repo/[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 94 - 94: I11i % I11i % IIiIiII11i * iI11I1II1I1I / OOoOoo . Ii1I
 if 13 - 13: OOooOOo . oOo0O0Ooo . I11i * oo0oO00 / iIi1i1ii1
 if 38 - 38: OOoOoo - ooOoO0O00 . Ii
 if 28 - 28: O00OOo00oo0o / oo0oO00 . Ii1I
 if 83 - 83: iiII11i1I1IIi
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 36 - 36: iI11I1II1I1I
 if 74 - 74: OOoOoo * Ii1I - ii
 if 59 - 59: IIiIi1iI * oO0o - O00OOo00oo0o % oo0oO00
 if 95 - 95: IIiIiII11i + IIiIiII11i
 if 33 - 33: ooOoO0O00 . I1ii11iIi11i - OOoOoo
 if 30 - 30: ii % IIi
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - IIi
 if 81 - 81: OooOO000 % iIi1i1ii1 . IIiIi1iI
 if 66 - 66: Ii1I * iIi1i1ii1 / ii * o0o00Oo0O % IIi
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * iIi1i1ii1 / O00OOo00oo0o * ii
 if 82 - 82: I1ii11iIi11i / iIi1i1ii1 / iIi1i1ii1 % iIi1i1ii1
 if 20 - 20: IIiIi1iI
 if 63 - 63: iI11I1II1I1I . oO0o
 if 100 - 100: ooOoO0O00 * ooOoO0O00
 if 26 - 26: IIi . oO0o % OOooOOo
 if 94 - 94: OOoOoo
 if 15 - 15: iIi1i1ii1 - OOoOoo / o0o00Oo0O
 if 28 - 28: O00OOo00oo0o . ooOoO0O00 / Ii1I
 if 77 - 77: Ii / O00OOo00oo0o / Ii % OOooOOo - O00OOo00oo0o
 if 80 - 80: O00OOo00oo0o % OOooOOo . ii . IIiIiII11i % OOoOoo
 if 6 - 6: O00OOo00oo0o % OOoOoo / iIi1i1ii1 + O00OOo00oo0o . oo0oO00
 if 70 - 70: iI11I1II1I1I / iIi1i1ii1
 if 61 - 61: o0o00Oo0O * I11i + O00OOo00oo0o - IIi . oOo0O0Ooo - OOoOoo
 if 7 - 7: Ii1I
def OO0ooO00OO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + IiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 97 - 97: IIi
def O0o00o00O00 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OOOoOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 74 - 74: iI11I1II1I1I . O00OOo00oo0o / iiII11i1I1IIi * Ii1I / Ii / OOoOoo
def i11io00oOo0oO0oOO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + Oooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 62 - 62: oOo0O0Ooo - OOoOoo - ii
def o0OOo0Ooo ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + I1iIiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 35 - 35: OooOO000
def I1iii111 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + i11II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 47 - 47: oO0o . iiII11i1I1IIi % IIiIi1iI - I1ii11iIi11i . oOo0O0Ooo
def IIiiiI1ii ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + Oo0o0o00Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 67 - 67: I11i % I11i * IIiIi1iI - Ii / iI11I1II1I1I % oOo0O0Ooo
def ooo0o ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o0OOO0O00Oo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 78 - 78: oO0o
def iI1I ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iiiiOo000O00o0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 83 - 83: IIiIi1iI - IIi / o0o00Oo0O
def IIio0 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + i1OO0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 64 - 64: ooOoO0O00 / I11i
def OOOoo0OO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + IIiI1i11iIII1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , Iiii1iI1i , o0ooooO0o0O , i11iiiiI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , i11iiiiI1i )
 I1I11i ( 'movies' , 'MAIN' )
 if 76 - 76: ii * OOoOoo - I11i * IIi * ooOoO0O00 * OooOO000
 if 41 - 41: oo0oO00 - IIiIi1iI * iIi1i1ii1 * ii % OOooOOo
 if 25 - 25: iI11I1II1I1I * ii * iIi1i1ii1 - ooOoO0O00
 if 23 - 23: I11i . IIiIi1iI - ii + iiII11i1I1IIi
 if 73 - 73: OOooOOo
 if 71 - 71: Ii * OOooOOo * IIi + oo0oO00 + I1ii11iIi11i
 if 59 - 59: OOoOoo
 if 54 - 54: IIi
 if 27 - 27: OOooOOo - oO0o + I11i + IIiIi1iI . oO0o
def I1iI1I1ii1 ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for ooo0 , OooooOo , IIIiiiIiI in os . walk ( iIi1ii1I1 ) :
     OoOo000o = 0
     OoOo000o += len ( IIIiiiIiI )
     if OoOo000o > 0 :
      for oooOo0OOOoo0 in IIIiiiIiI :
       os . unlink ( os . path . join ( ooo0 , oooOo0OOOoo0 ) )
  iIIi1IiiiII1i = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( iIIi1IiiiII1i )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 33 - 33: oo0oO00 % oO0o . iI11I1II1I1I / OOoOoo
 if 3 - 3: iIi1i1ii1 + oO0o
 if 60 - 60: oO0o . OOooOOo - Ii1I - oOo0O0Ooo - IIiIiII11i % I1ii11iIi11i
 if 62 - 62: o0o00Oo0O + OooOO000 - OooOO000 % iI11I1II1I1I
 if 47 - 47: O00OOo00oo0o + oOo0O0Ooo
 if 40 - 40: iI11I1II1I1I % iIi1i1ii1 + IIiIiII11i - oOo0O0Ooo
 if 80 - 80: oo0oO00
 if 81 - 81: ii / IIiIi1iI * iI11I1II1I1I . I1ii11iIi11i + oo0oO00 / o0o00Oo0O
def II11II1I ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 84 - 84: IIiIiII11i - I11i
def I11II1i1 ( url ) :
 oOoOoO0OoOO0 = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 o0oo00 = [
 ( oOoOoO0OoOO0 ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( oOoOoO0OoOO0 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOoOoO0OoOO0 , 'plugin.video.itv' , 'Images' ) ) ]
 if 92 - 92: ooOoO0O00
 OOO0OOo0OoO = 0
 if 77 - 77: I11i + OooOO000
 for i11I in o0oo00 :
  if os . path . exists ( i11I ) and not i11I in [ oO0o0o0ooO0oO , oOoOoO0OoOO0 ] :
   for ooo0 , OooooOo , IIIiiiIiI in os . walk ( i11I ) :
    OoOo000o = 0
    OoOo000o += len ( IIIiiiIiI )
    if OoOo000o > 0 :
     for oooOo0OOOoo0 in IIIiiiIiI :
      if not oooOo0OOOoo0 in oooOOOOO :
       try :
        os . unlink ( os . path . join ( ooo0 , oooOo0OOOoo0 ) )
       except :
        pass
      else : iIiIi11 ( 'Ignore Log File: %s' % oooOo0OOOoo0 )
     for IiIi1Ii in OooooOo :
      try :
       shutil . rmtree ( os . path . join ( ooo0 , IiIi1Ii ) )
       OOO0OOo0OoO += 1
       iIiIi11 ( "[Success] cleared %s files from %s" % ( str ( OoOo000o ) , os . path . join ( i11I , IiIi1Ii ) ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , IiIi1Ii ) )
  else :
   for ooo0 , OooooOo , IIIiiiIiI in os . walk ( i11I ) :
    for IiIi1Ii in OooooOo :
     if 'cache' in IiIi1Ii . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( ooo0 , IiIi1Ii ) )
       OOO0OOo0OoO += 1
       iIiIi11 ( "[Success] wiped %s " % os . path . join ( i11I , IiIi1Ii ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , IiIi1Ii ) )
       if 100 - 100: I11i - iiII11i1I1IIi + Ii
 II11II1I ( oO , 'Clear Cache: Removed %s Files' % OOO0OOo0OoO )
 if 12 - 12: oo0oO00 + iI11I1II1I1I . iIi1i1ii1
 if 43 - 43: ooOoO0O00 . oOo0O0Ooo * iI11I1II1I1I * Ii - IIi + IIiIi1iI
 if 56 - 56: I1ii11iIi11i % Ii / iIi1i1ii1 . O00OOo00oo0o . oO0o - OOooOOo
 if 32 - 32: O00OOo00oo0o / oo0oO00 / oOo0O0Ooo
 if 22 - 22: oO0o - OOooOOo . I1ii11iIi11i + I11i
 if 69 - 69: oo0oO00 - oOo0O0Ooo
 if 10 - 10: ooOoO0O00 / OooOO000 . IIiIiII11i * ooOoO0O00 % ii
def IiI1ii11I1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 O0I1i1I1IIIi1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooo0 , OooooOo , IIIiiiIiI in os . walk ( O0I1i1I1IIIi1II ) :
   OoOo000o = 0
   OoOo000o += len ( IIIiiiIiI )
   if 25 - 25: IIi / ii - Ii1I
   if 31 - 31: iiII11i1I1IIi + oO0o / oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
   if OoOo000o > 0 :
    if 34 - 34: OOoOoo
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( OoOo000o ) + " files found" , "Do you want to delete them?" ) :
     if 5 - 5: oO0o . oOo0O0Ooo
     for oooOo0OOOoo0 in IIIiiiIiI :
      os . unlink ( os . path . join ( ooo0 , oooOo0OOOoo0 ) )
     for IiIi1Ii in OooooOo :
      shutil . rmtree ( os . path . join ( ooo0 , IiIi1Ii ) )
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
 if 48 - 48: I1ii11iIi11i - oO0o . iiII11i1I1IIi - iI11I1II1I1I % iIi1i1ii1
 if 47 - 47: OooOO000 / ii - IIiIiII11i
 if 91 - 91: OOooOOo + I11i
 if 23 - 23: ooOoO0O00
 if 9 - 9: ooOoO0O00 % O00OOo00oo0o - oO0o * OOooOOo . I11i
 if 18 - 18: iIi1i1ii1 . OOooOOo + OooOO000 . oOo0O0Ooo + ii . oO0o
 if 31 - 31: O00OOo00oo0o - iiII11i1I1IIi
 if 49 - 49: iI11I1II1I1I - iI11I1II1I1I - OOooOOo + OOoOoo / OOooOOo
 if 74 - 74: ii + Ii1I % o0o00Oo0O
def I1iIIiiIIi1i ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 O0I1i1I1IIIi1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for ooo0 , OooooOo , IIIiiiIiI in os . walk ( O0I1i1I1IIIi1II ) :
   OoOo000o = 0
   OoOo000o += len ( IIIiiiIiI )
   if 32 - 32: Ii1I + Ii1I
   if 89 - 89: IIiIi1iI + oo0oO00 + iIi1i1ii1 - IIi
   if OoOo000o > 0 :
    if 12 - 12: OOooOOo - I11i - O00OOo00oo0o / iiII11i1I1IIi
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( OoOo000o ) + " files found" , "Do you want to delete them?" ) :
     if 17 - 17: oO0o - O00OOo00oo0o - IIiIiII11i / O00OOo00oo0o / iIi1i1ii1
     for oooOo0OOOoo0 in IIIiiiIiI :
      os . unlink ( os . path . join ( ooo0 , oooOo0OOOoo0 ) )
     for IiIi1Ii in OooooOo :
      shutil . rmtree ( os . path . join ( ooo0 , IiIi1Ii ) )
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
 I11II1i1 ( url )
 return
 if 30 - 30: IIi * Ii1I % Ii1I + OooOO000 * OOoOoo
 if 33 - 33: I11i + iiII11i1I1IIi * o0o00Oo0O * oO0o . Ii1I
 if 74 - 74: OooOO000 * OooOO000 * I11i / oo0oO00
 if 91 - 91: Ii . Ii1I / IIiIiII11i
 if 97 - 97: iIi1i1ii1 % ooOoO0O00 % OOoOoo + I1ii11iIi11i - o0o00Oo0O - iiII11i1I1IIi
 if 64 - 64: iIi1i1ii1 - OooOO000
 if 12 - 12: ooOoO0O00
 if 99 - 99: IIiIiII11i - Ii1I * OOoOoo
 if 3 - 3: OOoOoo - Ii1I * OooOO000 * Ii1I + I1ii11iIi11i
 if 15 - 15: Ii1I * iIi1i1ii1 / OooOO000 . I11i / iIi1i1ii1 % OOooOOo
def Oo0o0ooOo0 ( url , name ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoo0ooO0000 = os . path . join ( o00O0 , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 ii1iiI11III1 = os . path . join ( o00O0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( ii1iiI11III1 ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   OoOoo0ooO0000 = os . path . join ( o00O0 , 'advancedsettings.xml' )
   try :
    os . remove ( OoOoo0ooO0000 )
    print '=== GenieTv - REMOVING    ' + str ( OoOoo0ooO0000 ) + '    ==='
   except :
    pass
   i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
   OoOoO = open ( OoOoo0ooO0000 , "w" )
   OoOoO . write ( i1Oo00 )
   OoOoO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( OoOoo0ooO0000 ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  OoOoo0ooO0000 = os . path . join ( o00O0 , 'advancedsettings.xml' )
  try :
   os . remove ( OoOoo0ooO0000 )
   print '=== GenieTv - REMOVING    ' + str ( OoOoo0ooO0000 ) + '    ==='
  except :
   pass
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  OoOoO = open ( OoOoo0ooO0000 , "w" )
  OoOoO . write ( i1Oo00 )
  OoOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoo0ooO0000 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 8 - 8: Ii1I - ooOoO0O00 - oo0oO00 / oo0oO00 % I11i
def OOO0OoO00oOo ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoo0ooO0000 = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  OoOoO = open ( OoOoo0ooO0000 ) . read ( )
  if 'zero' in OoOoO :
   name = '0CACHE'
  elif 'tuxen' in OoOoO :
   name = 'TUXENS'
  elif 'muckys' in OoOoO :
   name = 'MUCKYS'
  elif 'p2p1' in OoOoO :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in OoOoO :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in OoOoO :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 35 - 35: IIiIiII11i . IIi + iI11I1II1I1I . ooOoO0O00 - OOooOOo + OOoOoo
def oOo0oOOoo0O ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 OoOoo0ooO0000 = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  os . remove ( OoOoo0ooO0000 )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( OoOoo0ooO0000 ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 4 - 4: IIiIi1iI
 if 47 - 47: ooOoO0O00 - OooOO000 - oO0o * IIiIi1iI / Ii * IIi
 if 55 - 55: IIiIi1iI
 if 1 - 1: oO0o
 if 43 - 43: iI11I1II1I1I - IIi - I11i + Ii1I - O00OOo00oo0o % Ii1I
 if 58 - 58: OOooOOo
 if 27 - 27: OOoOoo * IIi - ii . iIi1i1ii1 - IIiIiII11i
 if 62 - 62: oOo0O0Ooo / iI11I1II1I1I * iiII11i1I1IIi
 if 84 - 84: OOoOoo - OOooOOo . OOoOoo + IIiIi1iI . OooOO000
 if 96 - 96: iIi1i1ii1 % OooOO000 * iIi1i1ii1 % oOo0O0Ooo . I11i / I11i
def I1i1iI ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for iI11iiI1 , I1Ioo000oooooooO , II1IIi1ii111 , II1OO in IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % iI11iiI1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % II1IIi1ii111 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % II1OO )
  inc = inc + 1
  if 62 - 62: oo0oO00
  if 15 - 15: OOooOOo - iiII11i1I1IIi - iiII11i1I1IIi + OOoOoo * Ii1I
  if 21 - 21: OOooOOo . IIiIiII11i
  if 15 - 15: OOoOoo / oo0oO00
  if 22 - 22: OooOO000 . ii . I1ii11iIi11i
  if 44 - 44: OOooOOo / I1ii11iIi11i . ii % ii * Ii
  if 60 - 60: OOoOoo / iI11I1II1I1I + ii - Ii1I * Ii
  if 47 - 47: o0o00Oo0O . oOo0O0Ooo / IIiIi1iI % Ii
  if 47 - 47: iIi1i1ii1 . OOooOOo . iI11I1II1I1I . I11i
def i1IIii1i ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoOoo0ooO0000 = os . path . join ( o00O0 , 'addons2.ini' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  OoOoO = open ( OoOoo0ooO0000 , "w" )
  OoOoO . write ( i1Oo00 )
  OoOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoo0ooO0000 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 93 - 93: iIi1i1ii1 % iI11I1II1I1I * OooOO000 / OOooOOo * Ii
def i1O00oo ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  OoOoo0ooO0000 = os . path . join ( o00O0 , 'settings.xml' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  OoOoO = open ( OoOoo0ooO0000 , "w" )
  OoOoO . write ( i1Oo00 )
  OoOoO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( OoOoo0ooO0000 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 65 - 65: oOo0O0Ooo
 if 22 - 22: iI11I1II1I1I % O00OOo00oo0o % Ii1I % oOo0O0Ooo
def OoOooOO ( ) :
 try :
  IiI11i1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( IiI11i1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    IIIiiiIi1I1 = os . path . join ( IiI11i1 , "source.db" )
    os . unlink ( IIIiiiIi1I1 )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 10 - 10: oO0o - IIiIiII11i % I11i - OOooOOo + oO0o
 if 88 - 88: iI11I1II1I1I % IIiIi1iI + I11i * OOooOOo / iiII11i1I1IIi . oO0o
 if 66 - 66: iI11I1II1I1I * IIiIiII11i . iI11I1II1I1I * Ii + iiII11i1I1IIi + iIi1i1ii1
 if 94 - 94: ooOoO0O00 * iiII11i1I1IIi - ii . ooOoO0O00 / I11i
 if 51 - 51: Ii * ii
def O000oo ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 23 - 23: IIiIiII11i + iiII11i1I1IIi / o0o00Oo0O . iiII11i1I1IIi . O00OOo00oo0o + iI11I1II1I1I
 if 2 - 2: ooOoO0O00 . o0o00Oo0O / I11i . IIiIiII11i / oO0o % ooOoO0O00
 if 12 - 12: I11i
 if 58 - 58: iI11I1II1I1I * iIi1i1ii1 . IIiIi1iI . I1ii11iIi11i * iIi1i1ii1
 if 63 - 63: OOooOOo . iiII11i1I1IIi * I11i - iiII11i1I1IIi % iiII11i1I1IIi
 if 62 - 62: iiII11i1I1IIi - IIiIi1iI / IIiIi1iI
 if 95 - 95: OOooOOo - ooOoO0O00 / O00OOo00oo0o . IIiIi1iI % IIi - ooOoO0O00
def i11i1ii1I ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; i1ii1iIIIiI1 = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if i1ii1iIIIiI1 :
  ooo0oOooOoo0O = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; ooo0oOooOoo0O = xbmc . translatePath ( ooo0oOooOoo0O ) ;
  I1Iiiii111 = os . path . join ( ooo0oOooOoo0O , ".." , ".." ) ; I1Iiiii111 = os . path . abspath ( I1Iiiii111 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + I1Iiiii111 ) ; OO0O00o0oOOo = False
  try :
   for ooo0 , OooooOo , IIIiiiIiI in os . walk ( I1Iiiii111 , topdown = True ) :
    OooooOo [ : ] = [ IiIi1Ii for IiIi1Ii in OooooOo if IiIi1Ii not in o0oO0 ]
    for I1111i in IIIiiiIiI :
     try : os . remove ( os . path . join ( ooo0 , I1111i ) )
     except :
      if I1111i not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : OO0O00o0oOOo = True
      plugintools . log ( "Error removing " + ooo0 + " " + I1111i )
    for I1111i in OooooOo :
     try : os . rmdir ( os . path . join ( ooo0 , I1111i ) )
     except :
      if I1111i not in [ "Database" , "userdata" ] : OO0O00o0oOOo = True
      plugintools . log ( "Error removing " + ooo0 + " " + I1111i )
   if not OO0O00o0oOOo : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 o0OO0oooo ( )
 if 27 - 27: ooOoO0O00 . O00OOo00oo0o
 if 64 - 64: IIiIi1iI / ooOoO0O00
 if 100 - 100: IIiIiII11i
def i1IiI11I11I ( ) :
 IiiIiiIiiIII = [ ]
 Ii1i11IIiI = sys . argv [ 2 ]
 if len ( Ii1i11IIiI ) >= 2 :
  o0OO0o0o00o = sys . argv [ 2 ]
  III1i1 = o0OO0o0o00o . replace ( '?' , '' )
  if ( o0OO0o0o00o [ len ( o0OO0o0o00o ) - 1 ] == '/' ) :
   o0OO0o0o00o = o0OO0o0o00o [ 0 : len ( o0OO0o0o00o ) - 2 ]
  Oo00oooO00o = III1i1 . split ( '&' )
  IiiIiiIiiIII = { }
  for iiI1 in range ( len ( Oo00oooO00o ) ) :
   oooO0Oo0O = { }
   oooO0Oo0O = Oo00oooO00o [ iiI1 ] . split ( '=' )
   if ( len ( oooO0Oo0O ) ) == 2 :
    IiiIiiIiiIII [ oooO0Oo0O [ 0 ] ] = oooO0Oo0O [ 1 ]
    if 15 - 15: oO0o - OOooOOo
 return IiiIiiIiiIII
 if 41 - 41: iIi1i1ii1 * iiII11i1I1IIi
iI1I11II1Iii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
OooO00 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
O00O0oO = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
IIIIi1iII = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
o0Iiii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
ii1oO0Oo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
IiiI = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iIi1IIIi1Ii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
OOOoOO = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
Oooo0 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
I1iIiI1 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
i11II = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Oo0o0o00Oo = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o0OOO0O00Oo00 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iiiiOo000O00o0O = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
i1OO0o = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
o0o00OOOO = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
Ii1IiIIIi1i = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
o0oOoO00 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OOOOOOo0OOoOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
I1II1IiI1 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
o0OoO0oo0O0o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
IIiI1i11iIII1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
I1IiiiI = base64 . decodestring ( 'Q1VOVA==' )
def iiOOooooO0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1iOOOO = True
 ooO0oO00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooO0oO00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooO0oO00O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooOO00oOOo000 = [ ]
  if showcontext == 'fav' :
   ooOO00oOOo000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooOO00oOOo000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooO0oO00O0o . addContextMenuItems ( ooOO00oOOo000 )
 I1iOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1 , listitem = ooO0oO00O0o , isFolder = True )
 return I1iOOOO
 if 23 - 23: I11i % OooOO000 * I11i % OooOO000 / I11i
def OOiIiIIi1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 iii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 I1iOOOO = True
 ooO0oO00O0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooO0oO00O0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooO0oO00O0o . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooOO00oOOo000 = [ ]
  if showcontext == 'fav' :
   ooOO00oOOo000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooOO00oOOo000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooO0oO00O0o . addContextMenuItems ( ooOO00oOOo000 )
 I1iOOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1 , listitem = ooO0oO00O0o , isFolder = False )
 return I1iOOOO
 if 100 - 100: Ii * OooOO000 * IIiIi1iI
 if 19 - 19: OOoOoo
o0OO0o0o00o = i1IiI11I11I ( )
oO0o0 = None
I1111i = None
Ii11iiI = None
Iiii1iI1i = None
o0ooooO0o0O = None
i11iiiiI1i = None
I1i1i = None
iIi1Ii11I1 = None
if 21 - 21: IIi
if 11 - 11: oo0oO00 % Ii * o0o00Oo0O
try :
 iIi1Ii11I1 = int ( o0OO0o0o00o [ "fav_mode" ] )
except :
 pass
 if 28 - 28: O00OOo00oo0o / iI11I1II1I1I + IIi . Ii1I % IIi + oO0o
try :
 oO0o0 = urllib . unquote_plus ( o0OO0o0o00o [ "url" ] )
except :
 pass
try :
 I1111i = urllib . unquote_plus ( o0OO0o0o00o [ "name" ] )
except :
 pass
try :
 Iiii1iI1i = urllib . unquote_plus ( o0OO0o0o00o [ "iconimage" ] )
except :
 pass
try :
 Ii11iiI = int ( o0OO0o0o00o [ "mode" ] )
except :
 pass
try :
 o0ooooO0o0O = urllib . unquote_plus ( o0OO0o0o00o [ "fanart" ] )
except :
 pass
try :
 i11iiiiI1i = urllib . unquote_plus ( o0OO0o0o00o [ "description" ] )
except :
 pass
 if 79 - 79: oo0oO00
 if 39 - 39: O00OOo00oo0o % oo0oO00 % o0o00Oo0O % o0o00Oo0O - OooOO000 - oo0oO00
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( Ii11iiI )
print "URL: " + str ( oO0o0 )
print "Name: " + str ( I1111i )
print "IconImage: " + str ( Iiii1iI1i )
if 83 - 83: Ii + iI11I1II1I1I
if 21 - 21: I11i / Ii % O00OOo00oo0o
def I1I11i ( content , viewType ) :
 if 56 - 56: I11i * iI11I1II1I1I . iIi1i1ii1 + OOooOOo % O00OOo00oo0o
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 11 - 11: IIi
if Iiii1iI1i == None : Iiii1iI1i = Oo00OOOOO
if o0ooooO0o0O == None : o0ooooO0o0O = O0o0Oo
if Ii11iiI == None :
 o0o0o0oO0oOO ( )
 if 12 - 12: ii * IIi * Ii1I * IIiIi1iI
elif Ii11iiI == 1 :
 oO00OoO0oo ( oO0o0 )
 if 26 - 26: ii . ooOoO0O00 + oO0o
elif Ii11iiI == 44 :
 oOo0 ( oO0o0 )
 if 42 - 42: Ii * I11i % iiII11i1I1IIi % I1ii11iIi11i + I11i * Ii
elif Ii11iiI == 2 :
 OooOO ( )
 if 66 - 66: iIi1i1ii1 / OOoOoo . ii * I1ii11iIi11i % Ii
elif Ii11iiI == 3 :
 oOooOOo00ooO ( )
 if 100 - 100: Ii1I % IIiIiII11i * Ii - OooOO000
elif Ii11iiI == 21 :
 i1i1II ( )
 if 69 - 69: IIi + OooOO000 / O00OOo00oo0o
elif Ii11iiI == 4 :
 ii111I11Ii ( )
 if 37 - 37: iI11I1II1I1I * iiII11i1I1IIi / OOoOoo * I1ii11iIi11i % Ii
elif Ii11iiI == 5 :
 o0Oo00oOO ( oO0o0 )
 if 93 - 93: IIiIi1iI + IIiIi1iI
elif Ii11iiI == 6 :
 IiI1ii11I1 ( oO0o0 )
 if 65 - 65: ii * iiII11i1I1IIi * oo0oO00 % Ii1I * IIiIiII11i
elif Ii11iiI == 7 :
 Oo0o0ooOo0 ( oO0o0 , I1111i )
 if 86 - 86: Ii / iiII11i1I1IIi * OooOO000 - OooOO000
elif Ii11iiI == 8 :
 OOO0OoO00oOo ( oO0o0 , I1111i )
 if 32 - 32: I1ii11iIi11i . o0o00Oo0O
elif Ii11iiI == 9 :
 FIXREPOSADDONS ( oO0o0 )
 if 48 - 48: Ii1I % IIiIiII11i + iiII11i1I1IIi
elif Ii11iiI == 10 :
 O0O0ooOOO ( )
 if 25 - 25: OOoOoo * I11i / oOo0O0Ooo . OOoOoo % IIiIiII11i
elif Ii11iiI == 11 :
 oOo0oOOoo0O ( oO0o0 )
 if 50 - 50: OOooOOo * OooOO000
elif Ii11iiI == 12 :
 I1i1iI ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / iiII11i1I1IIi
elif Ii11iiI == 13 :
 I1iI1I1ii1 ( )
 if 92 - 92: I11i
elif Ii11iiI == 14 :
 I11II1i1 ( oO0o0 )
 if 8 - 8: OooOO000 + Ii1I . iIi1i1ii1
elif Ii11iiI == 15 :
 oOoo ( )
 if 50 - 50: I1ii11iIi11i
elif Ii11iiI == 16 :
 i1IIii1i ( oO0o0 , I1111i )
 if 16 - 16: iIi1i1ii1 - OOooOOo % I1ii11iIi11i / iIi1i1ii1 . iiII11i1I1IIi + IIiIi1iI
elif Ii11iiI == 17 :
 i1O00oo ( oO0o0 , I1111i )
 if 78 - 78: iI11I1II1I1I + oO0o + Ii
elif Ii11iiI == 18 :
 OoOooOO ( )
 if 21 - 21: I1ii11iIi11i + iIi1i1ii1 % IIiIi1iI + OOooOOo % iiII11i1I1IIi
elif Ii11iiI == 19 :
 O0Oo0O00o0oo0OO ( oO0o0 )
 if 22 - 22: ooOoO0O00 / ii . oO0o
elif Ii11iiI == 40 :
 oO0OOO00 ( I1111i , oO0o0 , i11iiiiI1i )
 if 83 - 83: oOo0O0Ooo - ii + Ii1I . iIi1i1ii1 / I11i + IIiIi1iI
elif Ii11iiI == 42 :
 oOo0OoOOOo0 ( I1111i , oO0o0 , i11iiiiI1i )
 if 90 - 90: oOo0O0Ooo - Ii
elif Ii11iiI == 43 :
 Ii1 ( oO0o0 )
 if 42 - 42: IIi . I1ii11iIi11i
elif Ii11iiI == 20 :
 ooO0 ( oO0o0 )
 if 21 - 21: OooOO000 . oOo0O0Ooo / iiII11i1I1IIi
elif Ii11iiI == 22 :
 OO0ooO00OO ( oO0o0 )
 if 97 - 97: iI11I1II1I1I + ooOoO0O00 - I11i
elif Ii11iiI == 23 :
 O0o00o00O00 ( oO0o0 )
 if 73 - 73: oO0o - Ii % O00OOo00oo0o / I1ii11iIi11i - ii % IIi
elif Ii11iiI == 24 :
 i11io00oOo0oO0oOO ( oO0o0 )
 if 79 - 79: oOo0O0Ooo / I11i . iIi1i1ii1 * Ii1I + iiII11i1I1IIi
elif Ii11iiI == 25 :
 o0OOo0Ooo ( oO0o0 )
 if 96 - 96: oO0o * IIiIiII11i
elif Ii11iiI == 26 :
 I1iii111 ( oO0o0 )
 if 1 - 1: oOo0O0Ooo - OOooOOo
elif Ii11iiI == 27 :
 IIiiiI1ii ( oO0o0 )
 if 74 - 74: OOooOOo * IIiIiII11i + o0o00Oo0O + iiII11i1I1IIi
elif Ii11iiI == 28 :
 ooo0o ( oO0o0 )
 if 3 - 3: iI11I1II1I1I - ooOoO0O00 / OooOO000 + ooOoO0O00 + o0o00Oo0O
elif Ii11iiI == 29 :
 iI1I ( oO0o0 )
 if 18 - 18: iI11I1II1I1I . OooOO000 % IIi % oo0oO00 + iI11I1II1I1I * ii
elif Ii11iiI == 30 :
 OOoOooO00 ( oO0o0 )
 if 78 - 78: OOoOoo
elif Ii11iiI == 31 :
 IIio0 ( oO0o0 )
 if 38 - 38: oO0o * Ii1I
elif Ii11iiI == 32 :
 Iii1IIII11I ( )
 if 4 - 4: oO0o . Ii1I
elif Ii11iiI == 33 :
 iI1iI ( )
 if 21 - 21: Ii / oO0o / Ii1I * o0o00Oo0O - IIiIiII11i * IIi
elif Ii11iiI == 35 :
 O0oO0o0OOOOOO ( oO0o0 )
 if 27 - 27: I11i . OOooOOo * iIi1i1ii1 * OooOO000 * o0o00Oo0O
elif Ii11iiI == 34 :
 O0O0 ( oO0o0 )
 if 93 - 93: OOoOoo % O00OOo00oo0o % IIiIiII11i
elif Ii11iiI == 36 :
 IIIIIiiiiI1I ( oO0o0 )
 if 20 - 20: ii * O00OOo00oo0o
elif Ii11iiI == 37 :
 O0OoO0oO00 ( oO0o0 )
 if 38 - 38: OooOO000 . ii
elif Ii11iiI == 38 :
 i1iI1Ii11Ii1 ( oO0o0 )
 if 28 - 28: O00OOo00oo0o * ooOoO0O00 . Ii1I
elif Ii11iiI == 41 :
 i11i1ii1I ( o0OO0o0o00o )
 if 75 - 75: o0o00Oo0O / oo0oO00 * IIiIi1iI - IIi / ooOoO0O00
elif Ii11iiI == 39 :
 OOOoo0OO ( oO0o0 )
 if 61 - 61: iiII11i1I1IIi
elif Ii11iiI == 45 :
 TEXTS ( )
 if 100 - 100: o0o00Oo0O - iI11I1II1I1I * I1ii11iIi11i
elif Ii11iiI == 46 :
 iI1Ii11iIiI1 ( )
 if 35 - 35: IIiIi1iI
elif Ii11iiI == 47 :
 GEVID ( )
 if 57 - 57: oO0o . I1ii11iIi11i + oOo0O0Ooo
elif Ii11iiI == 48 :
 i1iI ( I1111i , oO0o0 , i11iiiiI1i )
 if 18 - 18: oOo0O0Ooo - Ii1I * iiII11i1I1IIi / Ii - I11i % I11i
elif Ii11iiI == 49 :
 iI1i111I1Ii ( )
 if 31 - 31: iiII11i1I1IIi
elif Ii11iiI == 22222 :
 I1Ii ( oO0o0 )
 if 100 - 100: Ii * Ii . iI11I1II1I1I % OooOO000 * Ii1I
elif Ii11iiI == 222 :
 oo00Oo0oo0 ( oO0o0 )
 if 17 - 17: iIi1i1ii1 * OOoOoo * Ii / Ii1I / Ii
elif Ii11iiI == 2222222 :
 II1I1i ( oO0o0 )
 if 23 - 23: ii + Ii / I1ii11iIi11i / OooOO000 . OooOO000 * oOo0O0Ooo
elif Ii11iiI == 222222 :
 I11Oo0O00O0O00 ( oO0o0 , I1111i )
 if 98 - 98: OOoOoo
elif Ii11iiI == 333 :
 oOoOooO00o00 ( oO0o0 )
 if 23 - 23: iiII11i1I1IIi / ooOoO0O00 * oO0o
 if 51 - 51: IIi - ii / ii % ii
elif Ii11iiI == 1020 :
 o00ooo0oOo0o ( )
 if 85 - 85: oO0o . I11i . oOo0O0Ooo
elif Ii11iiI == 1021 :
 ANIMEEP ( )
 if 75 - 75: iI11I1II1I1I - iIi1i1ii1 % o0o00Oo0O % OOoOoo
elif Ii11iiI == 1022 :
 ANIMEPLAY ( oO0o0 )
 if 6 - 6: I1ii11iIi11i % oo0oO00 * IIiIi1iI - ooOoO0O00 . OOooOOo
elif Ii11iiI == 1001 :
 o0o0O0oOOoO0 ( )
 if 20 - 20: I1ii11iIi11i / O00OOo00oo0o . I1ii11iIi11i
elif Ii11iiI == 1005 :
 IIi1I ( )
 if 60 - 60: Ii1I - oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i . ooOoO0O00 . OOooOOo
elif Ii11iiI == 1007 :
 ii11iI11I111I ( oO0o0 )
 if 24 - 24: OOoOoo * oOo0O0Ooo / IIi
elif Ii11iiI == 1010 :
 IIi1i1 ( oO0o0 )
 if 51 - 51: iI11I1II1I1I / iiII11i1I1IIi * oO0o * iIi1i1ii1 + Ii1I . ii
elif Ii11iiI == 1011 :
 oooooOO0 ( oO0o0 )
 if 75 - 75: OOoOoo / ii / o0o00Oo0O % IIi
elif Ii11iiI == 1012 :
 iIiI1IIiii ( oO0o0 )
 if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
elif Ii11iiI == 1030 :
 OOO0o0O ( )
 if 11 - 11: I11i * oO0o
elif Ii11iiI == 1031 :
 I111i ( oO0o0 , Iiii1iI1i )
 if 92 - 92: OOooOOo . I1ii11iIi11i * iiII11i1I1IIi
elif Ii11iiI == 1032 :
 o00o ( oO0o0 )
 if 86 - 86: o0o00Oo0O
elif Ii11iiI == 1006 :
 Parse . ParseURL ( oO0o0 )
 if 55 - 55: iIi1i1ii1 / O00OOo00oo0o / Ii1I % IIiIi1iI % oOo0O0Ooo
elif Ii11iiI == 2030 :
 Parse . addonParseURL ( oO0o0 )
 if 55 - 55: oo0oO00 + ii % ooOoO0O00
elif Ii11iiI == 2031 :
 Parse . apkParseURL ( oO0o0 )
 if 24 - 24: Ii1I - I1ii11iIi11i
elif Ii11iiI == 2032 :
 Parse . ParseBOSS ( oO0o0 )
 if 36 - 36: oOo0O0Ooo . IIi % IIiIiII11i * OOoOoo
elif Ii11iiI == 1002 :
 oOooo0ooo ( oO0o0 )
 if 34 - 34: iiII11i1I1IIi % OooOO000 - IIiIi1iI - oOo0O0Ooo
elif Ii11iiI == 1003 :
 Iiii11i11IIi1 ( oO0o0 , Iiii1iI1i )
 if 44 - 44: iIi1i1ii1 . I11i . iI11I1II1I1I + ii - oOo0O0Ooo
elif Ii11iiI == 1004 :
 oOOo ( oO0o0 )
 if 22 - 22: iiII11i1I1IIi * Ii1I . ii / I1ii11iIi11i / iIi1i1ii1
elif Ii11iiI == 1008 :
 OOo0iIiiI11II11 ( )
 if 54 - 54: O00OOo00oo0o % iIi1i1ii1 + IIiIi1iI
elif Ii11iiI == 1009 :
 IIiIi ( oO0o0 )
 if 45 - 45: iIi1i1ii1 / oo0oO00 * O00OOo00oo0o . iIi1i1ii1
elif Ii11iiI == 2001 :
 Ii1111I1IIi1 ( )
 if 25 - 25: Ii1I / Ii1I
elif Ii11iiI == 2002 :
 IiIi11I ( oO0o0 )
 if 79 - 79: I1ii11iIi11i - oO0o % I1ii11iIi11i . IIiIiII11i
elif Ii11iiI == 1013 :
 I1111ii11IIII ( )
elif Ii11iiI == 10111113 :
 o0O0ooooooo00 ( oO0o0 )
 if 84 - 84: IIiIi1iI * ii + o0o00Oo0O
elif Ii11iiI == 1014 :
 iIIIIi ( )
 if 84 - 84: ooOoO0O00 . iiII11i1I1IIi . ooOoO0O00 . I1ii11iIi11i
elif Ii11iiI == 1015 :
 iiII ( oO0o0 )
 if 21 - 21: IIiIiII11i . o0o00Oo0O + I1ii11iIi11i - Ii
elif Ii11iiI == 1016 :
 OOoOooOoOOOoo ( oO0o0 , Iiii1iI1i , I1111i )
 if 5 - 5: iI11I1II1I1I * Ii + oO0o + iiII11i1I1IIi * o0o00Oo0O % IIiIi1iI
elif Ii11iiI == 1017 :
 Oo000ooOOO ( )
 if 88 - 88: I11i / Ii * Ii1I
elif Ii11iiI == 1018 :
 OoOo0oOooOoOO ( oO0o0 )
 if 23 - 23: o0o00Oo0O / OooOO000
elif Ii11iiI == 1023 :
 Ii11i1I11i ( )
 if 66 - 66: ooOoO0O00 % ii * Ii + oo0oO00 * o0o00Oo0O / oO0o
elif Ii11iiI == 1024 :
 i111II ( oO0o0 )
 if 14 - 14: oOo0O0Ooo . OOoOoo
elif Ii11iiI == 1025 :
 i11iI1I1 ( oO0o0 )
 if 29 - 29: ii / OOoOoo + OOooOOo - O00OOo00oo0o + OOoOoo . ooOoO0O00
elif Ii11iiI == 4001 :
 iiIi11iI1iii ( )
 if 26 - 26: Ii - IIiIiII11i
elif Ii11iiI == 4002 :
 OOOooo ( )
 if 43 - 43: oOo0O0Ooo
elif Ii11iiI == 4003 :
 IIIIIiI11Ii ( )
 if 35 - 35: IIiIi1iI + OOooOOo * ii - IIiIiII11i
elif Ii11iiI == 4004 :
 iII1ii1 ( )
 if 19 - 19: ooOoO0O00 / iIi1i1ii1 / OOooOOo . oOo0O0Ooo / iIi1i1ii1 % I11i
elif Ii11iiI == 4005 :
 oO0oo000OOOoO ( )
 if 39 - 39: IIiIi1iI - ii
elif Ii11iiI == 4006 :
 II1iiiiII ( )
 if 88 - 88: ooOoO0O00 + iI11I1II1I1I * Ii - ii % I11i
elif Ii11iiI == 4007 :
 iiI ( )
 if 74 - 74: IIiIi1iI - Ii
elif Ii11iiI == 4008 :
 I1ii1ii11i1I ( )
 if 34 - 34: OOoOoo + O00OOo00oo0o + I1ii11iIi11i / IIiIiII11i
elif Ii11iiI == 4009 : i1II1I1Iii1 ( )
elif Ii11iiI == 4010 : iI1I1 ( )
elif Ii11iiI == 3000 :
 oOOoooOoO0o0 ( )
 if 33 - 33: iIi1i1ii1 . ooOoO0O00 - IIiIiII11i - oO0o
elif Ii11iiI == 3001 :
 o00OoOO00 ( )
 if 31 - 31: iiII11i1I1IIi - OOooOOo / I11i * OOooOOo / I1ii11iIi11i + I11i
elif Ii11iiI == 3002 :
 oO0oOOoOo000O ( oO0o0 )
 if 46 - 46: OOoOoo * oO0o / IIi + I1ii11iIi11i
elif Ii11iiI == 3003 :
 II1 ( oO0o0 )
 if 24 - 24: IIiIi1iI % IIi . o0o00Oo0O * I1ii11iIi11i
elif Ii11iiI == 3004 :
 oOoO0o ( oO0o0 )
 if 52 - 52: o0o00Oo0O . O00OOo00oo0o + OooOO000 / Ii
elif Ii11iiI == 404 :
 oO0OO00o ( I1111i , oO0o0 , Iiii1iI1i )
 if 52 - 52: oo0oO00 % I1ii11iIi11i * IIiIiII11i
elif Ii11iiI == 405 :
 iiI1IIi1i1 ( oO0o0 )
 if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
elif Ii11iiI == 7030 :
 IiIII1I1Iii1 ( )
 if 27 - 27: ooOoO0O00 - oo0oO00 + IIi
elif Ii11iiI == 7021 :
 IiI1I1 ( I1111i )
 if 3 - 3: OOoOoo % O00OOo00oo0o . ii
elif Ii11iiI == 7022 :
 o0iIiii ( I1111i )
 if 19 - 19: O00OOo00oo0o * iIi1i1ii1 - oo0oO00
elif Ii11iiI == 7000 :
 iI1Oo ( I1111i , oO0o0 , img )
 if 78 - 78: oO0o - iIi1i1ii1 / IIi
elif Ii11iiI == 7050 :
 IiIi1II111I ( oO0o0 )
 if 81 - 81: OOooOOo
elif Ii11iiI == 7051 :
 o00O00o ( oO0o0 )
 if 21 - 21: OooOO000 / IIi % OOoOoo
elif Ii11iiI == 7052 :
 iiIi1iIiI ( oO0o0 )
 if 51 - 51: iiII11i1I1IIi + IIiIi1iI / oOo0O0Ooo
elif Ii11iiI == 7053 :
 IIi1iii ( oO0o0 )
 if 3 - 3: iI11I1II1I1I / IIi % oo0oO00 . iIi1i1ii1 - iIi1i1ii1
elif Ii11iiI == 7054 :
 CoolPlay ( oO0o0 )
 if 55 - 55: Ii % ii + o0o00Oo0O
elif Ii11iiI == 7060 :
 O0O00000o ( )
 if 7 - 7: IIiIi1iI - Ii * OooOO000 / iIi1i1ii1 - I11i
elif Ii11iiI == 7061 :
 ii1IIII ( oO0o0 )
 if 62 - 62: I11i - iI11I1II1I1I . iiII11i1I1IIi . iIi1i1ii1 * iIi1i1ii1
elif Ii11iiI == 7063 :
 oOOOoOo00O0 ( oO0o0 )
 if 24 - 24: iiII11i1I1IIi
elif Ii11iiI == 7062 :
 III ( oO0o0 )
 if 93 - 93: oOo0O0Ooo % oO0o / Ii / iiII11i1I1IIi
elif Ii11iiI == 7064 :
 NATatozcat ( )
 if 60 - 60: IIiIi1iI - iIi1i1ii1 . oOo0O0Ooo * oo0oO00 * Ii
elif Ii11iiI == 7067 :
 IiI1i1111iI1i ( oO0o0 )
 if 29 - 29: oO0o - I1ii11iIi11i . oo0oO00 / oO0o % Ii
elif Ii11iiI == 7066 :
 NATatozA ( oO0o0 )
 if 26 - 26: IIiIi1iI . O00OOo00oo0o / IIiIiII11i % iIi1i1ii1
elif Ii11iiI == 7065 :
 OoO00o ( oO0o0 )
 if 82 - 82: IIi % o0o00Oo0O % iI11I1II1I1I % OOoOoo + Ii
elif Ii11iiI == 7070 :
 I1OooO00Oo ( )
 if 64 - 64: ooOoO0O00 / OOoOoo . OOoOoo - O00OOo00oo0o % IIi . IIiIiII11i
elif Ii11iiI == 7071 :
 DIZIlist ( oO0o0 )
 if 78 - 78: O00OOo00oo0o - o0o00Oo0O - O00OOo00oo0o . iI11I1II1I1I % Ii1I . ii
elif Ii11iiI == 7072 :
 DIZIpull ( oO0o0 )
 if 64 - 64: OOoOoo
elif Ii11iiI == 7073 :
 WATCHDIZI ( oO0o0 )
 if 21 - 21: I11i - IIiIi1iI * ii . ii
elif Ii11iiI == 7002 :
 IIiI ( )
 if 17 - 17: IIi - OooOO000 % oOo0O0Ooo * IIi * iI11I1II1I1I . I11i
elif Ii11iiI == 7003 :
 iI1111iI1iII ( oO0o0 )
 if 58 - 58: oo0oO00 - IIiIiII11i + o0o00Oo0O
elif Ii11iiI == 7004 :
 oo0iI1IIIi11iIII ( oO0o0 )
 if 54 - 54: iI11I1II1I1I - OOoOoo - OOoOoo
elif Ii11iiI == 7020 :
 IiIII1i ( oO0o0 )
 if 18 - 18: Ii + iI11I1II1I1I . Ii
elif Ii11iiI == 7001 :
 oOoO00o ( )
 if 63 - 63: OooOO000 - oO0o * IIi
elif Ii11iiI == 7010 :
 oOOoOIi11 ( oO0o0 )
 if 89 - 89: OooOO000 / I1ii11iIi11i
elif Ii11iiI == 7011 :
 o0O0ooooO0 ( oO0o0 )
 if 66 - 66: I11i + OOooOOo % ii . iiII11i1I1IIi
elif Ii11iiI == 7012 :
 III1II1iiI11 ( oO0o0 )
 if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
elif Ii11iiI == 7013 :
 cnfTVPlay2 ( oO0o0 )
elif Ii11iiI == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oO0o0 )
elif Ii11iiI == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oO0o0 )
elif Ii11iiI == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1111i , oO0o0 , Iiii1iI1i )
elif Ii11iiI == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif Ii11iiI == 7018 :
 i1IiIiIii11I ( )
elif Ii11iiI == 7019 :
 CNF_Studio_Indexer . List_Movies ( oO0o0 )
elif Ii11iiI == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oO0o0 )
elif Ii11iiI == 7024 :
 CNF_Studio_Indexer . Box_Office ( oO0o0 )
 if 93 - 93: ooOoO0O00 + O00OOo00oo0o / oO0o - iiII11i1I1IIi % I1ii11iIi11i / iIi1i1ii1
elif Ii11iiI == 8000 :
 OOOoooooO0oOOoO ( )
elif Ii11iiI == 8001 :
 iiI1iiiii ( )
elif Ii11iiI == 8002 :
 iII ( )
elif Ii11iiI == 8003 :
 I1ii11ii1iiI ( )
elif Ii11iiI == 8004 :
 OOOo0o ( )
elif Ii11iiI == 8005 :
 OOO00OOOO0o ( )
elif Ii11iiI == 8006 :
 ooOO0o ( I1111i , oO0o0 )
elif Ii11iiI == 8030 :
 I1iiIiIII ( oO0o0 )
elif Ii11iiI == 8045 :
 oO000O ( oO0o0 )
elif Ii11iiI == 8046 :
 Oo0o0OoOoOo0 ( oO0o0 )
elif Ii11iiI == 8047 :
 O0ooO0 ( oO0o0 )
elif Ii11iiI == 8048 :
 O0000 ( oO0o0 )
elif Ii11iiI == 8049 :
 ooO0OO0Oooo0o ( oO0o0 )
elif Ii11iiI == 804900 :
 OOoO00o000 ( oO0o0 )
elif Ii11iiI == 8020 :
 i1iI1 ( )
elif Ii11iiI == 8021 :
 oooO ( oO0o0 )
elif Ii11iiI == 8022 :
 II111iiI1Ii1 ( oO0o0 )
elif Ii11iiI == 8023 :
 oo0oO0oO00oO ( oO0o0 )
elif Ii11iiI == 8040 :
 O0O0Oo00 ( )
elif Ii11iiI == 8041 :
 o00oOo0OoO0oO ( oO0o0 )
elif Ii11iiI == 8042 :
 O0oO00oO0o00o ( oO0o0 )
elif Ii11iiI == 8043 :
 yt . PlayVideo ( oO0o0 )
elif Ii11iiI == 8044 :
 o0OOo0O00OO0O ( oO0o0 )
elif Ii11iiI == 8060 :
 O0OOooOoO ( )
elif Ii11iiI == 8061 :
 IIiiIiIIiI1 ( oO0o0 )
elif Ii11iiI == 8064 :
 O0o ( )
elif Ii11iiI == 8065 :
 oo0O0000oo0o0 ( oO0o0 )
elif Ii11iiI == 8070 :
 IiIIIiII1111 ( )
elif Ii11iiI == 8071 :
 o0oOOoo ( oO0o0 )
elif Ii11iiI == 7080 :
 OOo000O000ooo ( oO0o0 )
elif Ii11iiI == 8090 :
 II1Iii1iI ( )
elif Ii11iiI == 8091 :
 iII1111IIIIiI ( oO0o0 )
elif Ii11iiI == 8092 :
 oOo00Oo00oO ( oO0o0 )
elif Ii11iiI == 8093 :
 IiiiiIi11 ( oO0o0 )
elif Ii11iiI == 8081 :
 ii1IiI1i ( )
elif Ii11iiI == 8062 :
 O0OoO0OOo ( oO0o0 )
elif Ii11iiI == 8063 :
 iIIi1I1 ( oO0o0 )
elif Ii11iiI == 8050 :
 O0O00O0Oo0 ( )
elif Ii11iiI == 8051 :
 OoOiI11IiI1i1 ( oO0o0 )
elif Ii11iiI == 8052 :
 ooO ( oO0o0 )
elif Ii11iiI == 8085 :
 oo00OO ( )
elif Ii11iiI == 8086 :
 ooo000OO ( oO0o0 )
elif Ii11iiI == 8087 :
 o0oooO0O00OoO ( oO0o0 )
elif Ii11iiI == 8088 :
 iiiiIIi ( oO0o0 , I1111i )
elif Ii11iiI == 9000 :
 I11io0Oo ( )
elif Ii11iiI == 1111 :
 o0O0Ooo ( )
elif Ii11iiI == 9001 :
 I1i1iiiI1 ( )
elif Ii11iiI == 9002 :
 ii1I ( )
elif Ii11iiI == 9003 :
 ii11Ii1iii1I1 ( )
elif Ii11iiI == 9004 :
 World1 ( )
elif Ii11iiI == 9005 :
 World2 ( oO0o0 )
elif Ii11iiI == 9006 :
 World3 ( oO0o0 )
elif Ii11iiI == 9007 :
 OooO00OOooOO ( )
elif Ii11iiI == 9008 :
 oooOOoOo0 ( oO0o0 )
elif Ii11iiI == 9009 :
 iii ( oO0o0 )
elif Ii11iiI == 9010 :
 ii1IO00oO0oOOOOOO ( )
elif Ii11iiI == 9011 :
 Oo0ooo00OoO ( oO0o0 )
elif Ii11iiI == 50 :
 oOooO0OoO ( oO0o0 )
elif Ii11iiI == 9020 :
 champlist ( )
elif Ii11iiI == 9021 :
 ii1i11Ii11iI ( )
elif Ii11iiI == 9022 :
 IiIIi1iIii1I1 ( )
elif Ii11iiI == 9023 :
 ii1oo ( )
elif Ii11iiI == 9024 :
 IIII11i1Ii ( oO0o0 )
elif Ii11iiI == 9030 :
 ii111I111i ( oO0o0 )
elif Ii11iiI == 9031 :
 II11111I ( oO0o0 )
elif Ii11iiI == 9032 :
 OOoo ( oO0o0 )
elif Ii11iiI == 9033 :
 OO0ooOO00o0 ( oO0o0 )
elif Ii11iiI == 9034 :
 oO00O0 ( )
elif Ii11iiI == 7085 :
 oOiIiii1III ( oO0o0 )
elif Ii11iiI == 7086 :
 oOooOO0oOo0O0 ( oO0o0 )
elif Ii11iiI == 7087 :
 iIiiIIiI11 ( i11iiiiI1i )
elif Ii11iiI == 9666 :
 I1iIIiiIIi1i ( oO0o0 )
elif Ii11iiI == 10100 : Oo00oO0o0Oo0o ( )
elif Ii11iiI == 101001 : ii1ii1i1ii ( oO0o0 )
elif Ii11iiI == 10105 : I1II11IIi11i ( oO0o0 )
elif Ii11iiI == 10106 : oo00ooOo ( oO0o0 )
elif Ii11iiI == 10104 : o0oOOO0 ( oO0o0 )
elif Ii11iiI == 10107 : iIi1Iii1 ( )
elif Ii11iiI == 10103 : Ooo00OoO0O00 ( oO0o0 )
elif Ii11iiI == 10108 : i11iI1 ( oO0o0 )
elif Ii11iiI == 10000 : Origin_Menu ( )
elif Ii11iiI == 10001 : II1I1iiIII1I1 ( )
elif Ii11iiI == 10002 : Ooo0O0oooo ( )
elif Ii11iiI == 10003 : o0OoOO ( )
elif Ii11iiI == 10004 : oo0o0000Oo0 ( oO0o0 )
elif Ii11iiI == 10005 : O00Oo ( )
elif Ii11iiI == 10006 : oOoO000 ( oO0o0 )
elif Ii11iiI == 10007 : oOII11i1I ( oO0o0 , Iiii1iI1i )
elif Ii11iiI == 10008 : Oo0O0o00o00 ( )
elif Ii11iiI == 10009 : ooi1 ( )
elif Ii11iiI == 10010 : OOoOOoo0 ( oO0o0 )
elif Ii11iiI == 10011 : I1iIi1111 ( oO0o0 )
elif Ii11iiI == 10012 : OOOOo0o00OO0000 ( oO0o0 )
elif Ii11iiI == 10109 : Ii1ii1I1I ( oO0o0 )
elif Ii11iiI == 10013 : iIi11I1II ( oO0o0 )
elif Ii11iiI == 10014 : OO000OOOo0Oo ( )
elif Ii11iiI == 10015 : oo00Oo ( )
elif Ii11iiI == 10016 : iIi1i ( oO0o0 )
elif Ii11iiI == 10017 : oOOoO0O ( )
elif Ii11iiI == 10018 : OO0ii1 ( )
elif Ii11iiI == 10019 : o0OoOOoOOoo ( )
elif Ii11iiI == 10020 : O00000OO00OO ( )
elif Ii11iiI == 10021 : O00O0 ( )
elif Ii11iiI == 10022 : I11iIi1i1I1i1 ( oO0o0 )
elif Ii11iiI == 10023 : oOOI1 ( I1111i , oO0o0 )
elif Ii11iiI == 10024 : Iii1Iii ( oO0o0 )
elif Ii11iiI == 10025 : iIIII1iIIii ( )
elif Ii11iiI == 10026 : iii11 ( )
elif Ii11iiI == 10027 : o00O ( )
elif Ii11iiI == 10028 : Oo00OOoO0oo ( )
elif Ii11iiI == 10029 : I1I1i11 ( )
elif Ii11iiI == 423 : o0oOOO ( oO0o0 )
elif Ii11iiI == 426 : O0Ooo0o ( oO0o0 )
elif Ii11iiI == 10030 : Izle_Films ( )
elif Ii11iiI == 10031 : Latest_Izle_Movies ( )
elif Ii11iiI == 10032 : Izle_Genres ( )
elif Ii11iiI == 10033 : Izle_Pop_Movies ( )
elif Ii11iiI == 10034 : Izle_Boxsets ( )
elif Ii11iiI == 10035 : Izle_Search ( )
elif Ii11iiI == 10036 : Izle_Genres_Movie ( oO0o0 )
elif Ii11iiI == 10037 : Izle_Boxset_single ( oO0o0 )
elif Ii11iiI == 10038 : Izle_IFRAME ( )
elif Ii11iiI == 10039 : Izle_Boxsets_Next ( oO0o0 )
elif Ii11iiI == 10040 : IIiI1 ( )
elif Ii11iiI == 10041 : iIII1iIii ( oO0o0 )
elif Ii11iiI == 10042 : oOooo00OOO000 ( oO0o0 )
elif Ii11iiI == 10043 : i11ii ( )
elif Ii11iiI == 10044 : Oo00o0OOo0OO ( oO0o0 )
elif Ii11iiI == 10045 : i1Ii1IiiIi1II ( I1111i )
elif Ii11iiI == 10046 : O0oOoo00Oo0O ( oO0o0 )
elif Ii11iiI == 10047 : OoOo0o0OOoO0 ( oO0o0 )
elif Ii11iiI == 10048 : ooo ( oO0o0 )
elif Ii11iiI == 10049 : IiiiI11 ( oO0o0 )
elif Ii11iiI == 10050 : iI1i11iII111 ( )
elif Ii11iiI == 10051 : Oo0OOo ( )
elif Ii11iiI == 10052 : oOoO000OOoo0 ( )
elif Ii11iiI == 10053 : Addon ( oO0o0 )
elif Ii11iiI == 10054 : I1IO0 ( oO0o0 , I1111i )
elif Ii11iiI == 10055 :
 iI1I1I ( "addFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOOOiiI ( I1111i , oO0o0 , Iiii1iI1i , o0ooooO0o0O , iIi1Ii11I1 )
elif Ii11iiI == 10056 :
 iI1I1I ( "rmFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 o00OOOOooO ( I1111i )
elif Ii11iiI == 10057 :
 iI1I1I ( "getFavorites" )
 oooO00oo0 ( )
elif Ii11iiI == 10058 : iiI11Iii ( )
elif Ii11iiI == 10059 : Donators_Guide ( )
elif Ii11iiI == 10060 : oo000o0000oO ( )
elif Ii11iiI == 10061 : i1iI1i ( )
elif Ii11iiI == 10062 : i11IiI1I ( I1111i , oO0o0 , i11iiiiI1i )
elif Ii11iiI == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
elif Ii11iiI == 10064 : i1I111i1ii ( )
elif Ii11iiI == 10065 : I1I1i ( oO0o0 )
elif Ii11iiI == 10066 : IiiIi11Ii1iI1 ( oO0o0 )
elif Ii11iiI == 10068 : oOo ( oO0o0 )
elif Ii11iiI == 10069 : oO0OoO00o ( oO0o0 )
elif Ii11iiI == 10070 : oOOoo ( oO0o0 )
elif Ii11iiI == 10071 : Genie_Watch ( )
elif Ii11iiI == 10072 : i11Ii1IIi ( )
elif Ii11iiI == 10073 : iIi11i ( oO0o0 )
elif Ii11iiI == 10074 : O0o0OO00 ( oO0o0 )
elif Ii11iiI == 10075 : Iiii1i11ii1Ii ( Iiii1iI1i , I1111i , oO0o0 )
elif Ii11iiI == 10076 : IIi1ii1 ( oO0o0 )
elif Ii11iiI == 10077 : IiiIiI1I1 ( oO0o0 )
elif Ii11iiI == 10078 : IiI ( )
elif Ii11iiI == 10079 : Genie_Watch_Tv_Shows ( )
elif Ii11iiI == 10080 : Genie_Watch_Tv_Genre ( oO0o0 )
elif Ii11iiI == 10081 : Genie_Watch_TV_PlayRun ( oO0o0 )
elif Ii11iiI == 10082 : Genie_Watch_TV_Episodes ( oO0o0 , Iiii1iI1i )
elif Ii11iiI == 10083 : Genie_Watch_Tv_Recent ( oO0o0 )
elif Ii11iiI == 10084 : O0OoO0ooOO0o ( )
elif Ii11iiI == 10085 : Iiii1i1 ( )
elif Ii11iiI == 10086 : II1I ( )
elif Ii11iiI == 20000 : o0Ooo0o0ooo0 ( )
elif Ii11iiI == 20001 : ooo00o0OO ( oO0o0 )
elif Ii11iiI == 20002 : ooiIii1I1111 ( oO0o0 )
elif Ii11iiI == 20003 : i111IIiIII1i ( oO0o0 )
elif Ii11iiI == 20004 : O0oo0ooo0 ( oO0o0 )
elif Ii11iiI == 20005 : O0oOoO0oO00O ( oO0o0 )
elif Ii11iiI == 21004 : Ii1111IiIi ( )
elif Ii11iiI == 21005 : i1iI1IIi1I ( oO0o0 )
elif Ii11iiI == 21006 : OOOOOoooO ( oO0o0 )
elif Ii11iiI == 21007 : I1iii1I ( oO0o0 )
elif Ii11iiI == 30000 : O0oO00oOOooO ( )
elif Ii11iiI == 30001 : O0Oo00 ( )
elif Ii11iiI == 10012 : Resolve ( oO0o0 )
elif Ii11iiI == 30003 : II11IiI1 ( )
elif Ii11iiI == 30004 : Oo0OOOoOO ( oO0o0 )
elif Ii11iiI == 30005 : IIii1i ( oO0o0 )
elif Ii11iiI == 30006 : I11iiIi1i1IIi ( )
elif Ii11iiI == 30007 : i1Ii1i1I11III ( )
elif Ii11iiI == 30008 : oOoOO ( oO0o0 )
elif Ii11iiI == 30009 : iI1Ii11 ( oO0o0 )
elif Ii11iiI == 30010 : oooOo00O0 ( oO0o0 )
elif Ii11iiI == 30011 : i111 ( )
elif Ii11iiI == 30012 : ooOOO0ooO0o ( )
elif Ii11iiI == 30013 : Iioo0O00ooo0o ( )
elif Ii11iiI == 30014 : IiiI11 ( )
elif Ii11iiI == 30015 : OOooOoO ( oO0o0 , Iiii1iI1i , o0ooooO0o0O )
elif Ii11iiI == 30016 : iiiii1i ( oO0o0 )
elif Ii11iiI == 30019 : oO0OOOoO0o ( oO0o0 )
elif Ii11iiI == 30017 : IiI1IiI1iiI1 ( oO0o0 )
elif Ii11iiI == 30018 : Oo0Oo ( oO0o0 )
elif Ii11iiI == 30030 : o0OoOo0O00 ( )
elif Ii11iiI == 30031 : oooOOOOOi1iIii ( )
elif Ii11iiI == 30032 : oOIIiIi ( )
elif Ii11iiI == 30033 : iI1i1iI1iI ( )
elif Ii11iiI == 30034 : I1IIiIi ( )
elif Ii11iiI == 30035 : oOoO00O ( oO0o0 )
elif Ii11iiI == 30036 : I11I1I1i1i ( oO0o0 )
elif Ii11iiI == 30037 : Oo0oOO0O00 ( oO0o0 )
elif Ii11iiI == 30038 : O0oOoOoOoo0OoO0 ( )
elif Ii11iiI == 30039 : OooOoOO0 ( )
elif Ii11iiI == 50000 : oOOo0O00o ( )
elif Ii11iiI == 50001 : IiI1I ( )
elif Ii11iiI == 50002 : oo0O0O ( oO0o0 )
elif Ii11iiI == 50003 : II1I11 ( i11iiiiI1i )
elif Ii11iiI == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif Ii11iiI == 60001 : I111iiiii1 ( )
elif Ii11iiI == 60002 : oOOO0ooOO ( I1111i )
elif Ii11iiI == 60003 : IiI1Iii1 ( I1111i )
elif Ii11iiI == 60004 : I1I1i1i ( oO0o0 )
elif Ii11iiI == 50004 : iiIiIIIiiI ( )
elif Ii11iiI == 50005 : speedtest . runtest ( oO0o0 )
elif Ii11iiI == 70001 : Iiii1Ii1I ( )
elif Ii11iiI == 70002 : II11I ( oO0o0 )
elif Ii11iiI == 70003 : Iii1iIiI1I1I1 ( oO0o0 )
elif Ii11iiI == 70004 : oOOO0OO ( oO0o0 )
elif Ii11iiI == 70005 : I11ii1iI11 ( oO0o0 )
elif Ii11iiI == 70006 : i11ii111i1ii ( )
elif Ii11iiI == 50006 : OO0O000 ( i1 , i1111 )
elif Ii11iiI == 80000 : o0OO0oooo ( )
elif Ii11iiI == 80001 : resolvefilmon ( oO0o0 )
elif Ii11iiI == 80002 : i1iIIiI1111 ( )
elif Ii11iiI == 80003 : I111Iii1 ( I1111i , oO0o0 , "None" )
elif Ii11iiI == 80004 : o00OOo0o0O ( I1111i , oO0o0 )
elif Ii11iiI == 80005 : oO00oOooooo0 ( )
elif Ii11iiI == 80006 : iI1i1iIi1iiII ( oO0o0 )
elif Ii11iiI == 80007 : o0OoO0000o ( oO0o0 )
elif Ii11iiI == 80008 : o0Ii1 ( )
elif Ii11iiI == 80009 : O0oo0ooO00 ( )
elif Ii11iiI == 80010 : oOoO0 ( oO0o0 )
elif Ii11iiI == 80011 : IIi1iI ( oO0o0 )
elif Ii11iiI == 80012 : oooOo0OO ( )
elif Ii11iiI == 90000 : iiIIiI1i1i1I1 ( I1111i , oO0o0 )
elif Ii11iiI == 90001 : Ii1I1I1i1Ii ( )
elif Ii11iiI == 90002 : II1I1Ii ( )
elif Ii11iiI == 90003 : oO00oO0 ( oO0o0 )
elif Ii11iiI == 90004 : o0oI1Iii ( oO0o0 )
elif Ii11iiI == 90005 : II1I1Ii11 ( oO0o0 )
elif Ii11iiI == 90006 : ii111IIiiiiI ( oO0o0 )
elif Ii11iiI == 90007 : oo0OOoOo0 ( oO0o0 )
elif Ii11iiI == 90008 : IiIi ( oO0o0 )
elif Ii11iiI == 90009 : oo0o0ooOoo00O ( oO0o0 )
elif Ii11iiI == 90010 : iiIiI1i1 ( )
elif Ii11iiI == 90020 : O0oo ( )
elif Ii11iiI == 90021 : hellyeah2 ( oO0o0 )
elif Ii11iiI == 90022 : hellyeah3 ( oO0o0 )
elif Ii11iiI == 90023 : oOooO00o0O ( )
elif Ii11iiI == 90024 : ii1IiIiI1 ( oO0o0 )
elif Ii11iiI == 90025 : O0ooOo0o0Oo ( oO0o0 )
if 1 - 1: I1ii11iIi11i / iIi1i1ii1 . Ii % IIi + I11i + o0o00Oo0O
elif Ii11iiI == 90030 : I11iII ( )
elif Ii11iiI == 90031 : I1i1i1iii ( )
elif Ii11iiI == 90032 : iIIii ( oO0o0 )
elif Ii11iiI == 90033 : ii1iii1i ( oO0o0 )
elif Ii11iiI == 90034 : ooO0O00Oo0o ( oO0o0 )
elif Ii11iiI == 90035 : I1i ( oO0o0 )
elif Ii11iiI == 90036 : Ii1I11Ii1iI ( oO0o0 )
elif Ii11iiI == 90039 : OOOOOo00OOoO ( oO0o0 )
elif Ii11iiI == 90037 : I11I1IIiiII1 ( oO0o0 )
elif Ii11iiI == 90038 : o0OO0O0Oo ( )
if 54 - 54: O00OOo00oo0o + IIiIi1iI % OOoOoo
elif Ii11iiI == 10090 : Ii1i1iI ( )
elif Ii11iiI == 10091 : iIi11IiiiII11 ( oO0o0 )
elif Ii11iiI == 10092 : Iii1o00o0 ( oO0o0 )
elif Ii11iiI == 10093 : o0Oo0oO00Oooo ( oO0o0 , Iiii1iI1i )
elif Ii11iiI == 10094 : O0O00 ( oO0o0 , Iiii1iI1i )
if 83 - 83: I11i * iI11I1II1I1I
elif Ii11iiI == 10095 : ii1I1IiiI1ii1i ( )
elif Ii11iiI == 10096 : oo0000o ( oO0o0 )
elif Ii11iiI == 10097 : ooOOOoOoOOO0 ( oO0o0 )
elif Ii11iiI == 10098 : I1i1iIi1I1 ( oO0o0 )
elif Ii11iiI == 10099 : Ii1iI ( oO0o0 )
if 36 - 36: OOooOOo + IIiIiII11i - oO0o % IIiIi1iI * ooOoO0O00
elif Ii11iiI == 10200 : iIIi ( )
elif Ii11iiI == 10201 : iiOOOO0o ( oO0o0 )
elif Ii11iiI == 10202 : O00O00O000OOO ( oO0o0 )
elif Ii11iiI == 10203 : RT4 ( oO0o0 )
if 4 - 4: iIi1i1ii1 + oO0o * Ii1I
elif Ii11iiI == 90040 : oO0o00oo0 ( )
elif Ii11iiI == 90041 : o00IiI1iiII1i1i ( oO0o0 )
elif Ii11iiI == 90042 : oO0oI1I1 ( oO0o0 )
elif Ii11iiI == 90043 : OOooo ( oO0o0 )
elif Ii11iiI == 90044 : iI1IiiiIiI1Ii ( oO0o0 )
elif Ii11iiI == 90045 : i11i11 ( )
elif Ii11iiI == 90046 : Oo000 ( oO0o0 )
elif Ii11iiI == 90050 : OO0oo0O ( )
elif Ii11iiI == 90051 : I1IiIii11I ( oO0o0 )
elif Ii11iiI == 90052 : oo0 ( oO0o0 )
elif Ii11iiI == 90053 : II1iiI ( oO0o0 )
elif Ii11iiI == 90054 : I1i1I1I11IiiI ( oO0o0 )
elif Ii11iiI == 90055 : iiii1 ( )
if 13 - 13: OOooOOo - OOoOoo * iI11I1II1I1I * o0o00Oo0O
elif Ii11iiI == 100001 : Stand_up ( )
if 26 - 26: ii + oo0oO00 + oO0o . o0o00Oo0O
elif Ii11iiI == 100003 : iIi1i ( oO0o0 )
elif Ii11iiI == 100004 : I111iIi1 ( oO0o0 )
elif Ii11iiI == 100005 : Resolve ( oO0o0 )
elif Ii11iiI == 100008 : Search ( )
elif Ii11iiI == 100007 : ooo000ooO0000 ( oO0o0 )
elif Ii11iiI == 100009 : yt . PlayVideo ( oO0o0 )
elif Ii11iiI == 100010 : oO0oO0 ( oO0o0 )
elif Ii11iiI == 100100 : oOOo0o0oo ( Iiii1iI1i , oO0o0 , I1i1i )
elif Ii11iiI == 100101 : OoO0O0O0o00 ( oO0o0 , I1111i , o0ooooO0o0O , I1i1i , Iiii1iI1i )
elif Ii11iiI == 100102 : i11i1iiI1i ( I1111i , oO0o0 , Iiii1iI1i , o0ooooO0o0O )
elif Ii11iiI == 100106 : OoOIii11iI11i1I ( oO0o0 , I1111i )
elif Ii11iiI == 100107 : IioO0O ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
