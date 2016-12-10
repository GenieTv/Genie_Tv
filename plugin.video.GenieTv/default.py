# -*- coding: cp1252 -*-
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , os , base64 , sys , xbmcvfs , unicodedata
import urlresolver
from imports import cloudflare , googleplus , client , cleantitle
from imports import yt
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
IiiIII111iI = "3.3.5"
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
  iiOOooooO0Oo ( '[COLOR' + II + ']TOOLS[/COLOR]' , '' , 90001 , oOOOo00O00oOo + 'tools.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']CONTACT US[/COLOR]' , '' , 50006 , oOOOo00O00oOo + 'Contact-Us.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , oOOOo00O00oOo + 'settings.png' , O0o0Oo , '' )
  OOiIiIIi1 ( '[COLOR' + II + ']Force Genie Update Kodi 16+[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , oOOOo00O00oOo + 'GenieUpdate.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'My Build' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']WIZARD[/COLOR]' , str ( ooOO0O0ooOooO ) , 4001 , oOOOo00O00oOo + 'Wizard.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4002 , oOOOo00O00oOo + 'Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Sports[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Music' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']Music[/COLOR]' , str ( ooOO0O0ooOooO ) , 4003 , oOOOo00O00oOo + 'Music.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']BUILDERS TOOLBOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 32 , oOOOo00O00oOo + 'BuildersToolbox.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   OOiIiIIi1 ( '[COLOR' + II + ']SOURCE LIST[/COLOR]' , str ( ooOO0O0ooOooO ) , 46 , oOOOo00O00oOo + 'SoruceList.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']MAINTENANCE[/COLOR]' , str ( ooOO0O0ooOooO ) , 3 , oOOOo00O00oOo + 'Maintenance.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']ADDONS[/COLOR]' , '' , 10050 , oOOOo00O00oOo + 'Addons.png' , O0o0Oo , '' )
  if I1IIII1i ( ) == 'android' :
   iiOOooooO0Oo ( '[COLOR' + II + ']APK TOOL[/COLOR]' , str ( ooOO0O0ooOooO ) , 30039 , oOOOo00O00oOo + 'APKTools.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']GenieTv RSS Feed[/COLOR]' , str ( ooOO0O0ooOooO ) , 39 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def o00o0 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']TOOLS[/COLOR]' , '' , 90001 , oOOOo00O00oOo + 'tools.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']WIZARD[/COLOR]' , str ( ooOO0O0ooOooO ) , 4001 , oOOOo00O00oOo + 'Wizard.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4002 , oOOOo00O00oOo + 'Streams.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']Music[/COLOR]' , str ( ooOO0O0ooOooO ) , 4003 , oOOOo00O00oOo + 'Music.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Sports[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  iiOOooooO0Oo ( '[COLOR' + II + ']MAINTENANCE[/COLOR]' , str ( ooOO0O0ooOooO ) , 3 , oOOOo00O00oOo + 'Maintenance.png' , O0o0Oo , '' )
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
  if Ooo == '5knuckleshuffle' :
   iiOOooooO0Oo ( '[COLOR' + II + ']XVID[/COLOR]' , str ( ooOO0O0ooOooO ) , 10100 , oOOOo00O00oOo + 'Jizbox.png' , O0o0Oo , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']ADULT CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30033 , oOOOo00O00oOo + 'adu.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FAVOURITES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10057 , oOOOo00O00oOo + 'Favourites.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 9000 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Live List[/COLOR]' , '' , 4009 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   OOiIiIIi1 ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAM CATEGORIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 90002 , oOOOo00O00oOo + 'cats.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAM TEAM[/COLOR]' , str ( ooOO0O0ooOooO ) , 4006 , oOOOo00O00oOo + 'StreamTeam.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , oOOOo00O00oOo + 'bamf.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , O0o0Oo , '' )
 else :
  if Ooo == '5knuckleshuffle' :
   iiOOooooO0Oo ( '[COLOR' + II + ']XVID[/COLOR]' , str ( ooOO0O0ooOooO ) , 10100 , oOOOo00O00oOo + 'Jizbox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ADULT CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30033 , oOOOo00O00oOo + 'adu.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FAVOURITES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10057 , oOOOo00O00oOo + 'Favourites.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 9000 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Live List[/COLOR]' , '' , 4009 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   OOiIiIIi1 ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']STREAM TEAM[/COLOR]' , str ( ooOO0O0ooOooO ) , 4006 , oOOOo00O00oOo + 'StreamTeam.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 4004 , oOOOo00O00oOo + 'Movies.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4005 , oOOOo00O00oOo + 'TVShows.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , oOOOo00O00oOo + 'bamf.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' , '' , 9034 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FOOTBALL[/COLOR]' , '' , 10002 , oOOOo00O00oOo + 'Football.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']KIDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4007 , oOOOo00O00oOo + 'Kids.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']NEWS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30032 , oOOOo00O00oOo + 'News.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'GenieTVTutorials.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']HOBBIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 4008 , oOOOo00O00oOo + 'Hobbies.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Stand Up' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']STAND UP[/COLOR]' , '' , 10003 , oOOOo00O00oOo + 'StandUp.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 8040 , oOOOo00O00oOo + 'documentaries.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 7001 , oOOOo00O00oOo + 'DiscloseTV.png' , O0o0Oo , '' )
   if 94 - 94: ii + I1ii11iIi11i / OOooOOo * IIi
   if 69 - 69: IIiIi1iI % oo0oO00
  iiOOooooO0Oo ( '[COLOR' + II + ']24/7 STREAMS[/COLOR]' , '' , 30030 , oOOOo00O00oOo + '247Streams.png' , O0o0Oo , '' )
  if 50 - 50: ii % iiII11i1I1IIi
  if 49 - 49: oo0oO00 - Ii . O00OOo00oo0o * iIi1i1ii1 % OooOO000 + ooOoO0O00
  if 71 - 71: I11i
  if 38 - 38: oo0oO00 % OOooOOo + Ii1I . Ii
  if 53 - 53: Ii * OooOO000
  if 68 - 68: iI11I1II1I1I * iI11I1II1I1I . I11i / IIiIiII11i % I1ii11iIi11i
  if 38 - 38: IIiIi1iI - IIi / OooOO000
  if 66 - 66: o0o00Oo0O % Ii1I + Ii . OOooOOo / iIi1i1ii1 + Ii1I
  iiOOooooO0Oo ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , O0o0Oo , '' )
  if 86 - 86: I11i
  if 5 - 5: OOoOoo * OOooOOo
  if 5 - 5: O00OOo00oo0o
  if 90 - 90: O00OOo00oo0o . IIiIi1iI / iIi1i1ii1 - iiII11i1I1IIi
  if 40 - 40: ii
  if 25 - 25: OOoOoo + iIi1i1ii1 / IIiIi1iI . I11i % o0o00Oo0O * oO0o
 I1I11i ( 'movies' , 'MAIN' )
def o0O0oo0OO0O ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']MOVIES[/COLOR]' , '[COLOR' + II + ']TV SHOWS[/COLOR]' , '[COLOR' + II + ']FOOTBALL[/COLOR]' , '[COLOR' + II + ']KIDS[/COLOR]' , '[COLOR' + II + ']NEWS[/COLOR]' , '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + II + ']HOBBIES[/COLOR]' , '[COLOR' + II + ']STAND UP[/COLOR]' , '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']CATEGORIES[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OO0 ( )
 if i11I1II1I11i == 1 :
  o0Oooo ( )
 if i11I1II1I11i == 2 :
  iiI ( )
 if i11I1II1I11i == 3 :
  oOIIiIi ( )
 if i11I1II1I11i == 4 :
  OOoOooOoOOOoo ( )
 if i11I1II1I11i == 5 :
  Iiii1iI1i ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , I1ii1ii11i1I , I1111i )
 if i11I1II1I11i == 6 :
  o0OoOO ( )
 if i11I1II1I11i == 7 :
  O0O0Oo00 ( )
 if i11I1II1I11i == 8 :
  oOoO00o ( )
 if i11I1II1I11i == 9 :
  oO00O0 ( )
 if i11I1II1I11i == 10 :
  IIi1IIIi ( )
  if 99 - 99: iIi1i1ii1 + oO0o * IIiIiII11i . I11i - Ii1I
  if 58 - 58: iIi1i1ii1 + I11i - oOo0O0Ooo
def ii1Ii11I ( ) :
 if not os . path . exists ( IIIII ) :
  OO0O000 ( 'Change Log 06/12/16 - v3.3.5' , 'NEW SECTIONS ADDED, MOVIE HUB(streams>>stream categories>>movies), Tv HUB(streams>>stream categories>>tv shows), BAMF IPTV revamped, WATCH SERIES revamped, General Maintence' )
  os . makedirs ( IIIII )
  if 3 - 3: oO0o
  if 97 - 97: O00OOo00oo0o
def OO0 ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']MOVIE HUB[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   iiIII1i ( )
  if i11I1II1I11i == 1 :
   I1I ( )
  if i11I1II1I11i == 2 :
   ooooO0oOoOOoO ( oO0o0 )
  if i11I1II1I11i == 3 :
   I1i11i ( )
  if i11I1II1I11i == 4 :
   IiIi ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if i11I1II1I11i == 5 :
   OOOOO0O00 ( )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9001 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MOVIE HUB[/COLOR]' , '' , 90040 , oOOOo00O00oOo + 'movhub.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']POPCORN BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 7061 , oOOOo00O00oOo + 'PopcornBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Desi Flix[/COLOR]' , '' , 80005 , oOOOo00O00oOo + 'Desi.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , oOOOo00O00oOo + 'FilmTrailers.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOOo00O00oOo + 'ClassicMovies.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def Iii ( ) :
 IIiiiI1iIII ( )
 iIIiIiI1I1 ( )
 if 56 - 56: oOo0O0Ooo . o0o00Oo0O + I1ii11iIi11i
 if 1 - 1: OooOO000
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  OOiIiIIi1 ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']Link GTV to Guide[/COLOR]' , '' , 4010 , oOOOo00O00oOo + 'linkchannels.png' , O0o0Oo , '' )
def IIi1IIIi ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']DAILY LISTS[/COLOR]' , '' , 9007 , Oo00OOOOO , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Oo00OOOOO , O0o0Oo , '' )
 if 97 - 97: IIi + OooOO000 + o0o00Oo0O + Ii
 if 77 - 77: I11i / ii
 if 46 - 46: I11i % iI11I1II1I1I . OooOO000 % OooOO000 + Ii
 if 72 - 72: iI11I1II1I1I * iIi1i1ii1 % IIiIi1iI / oO0o
 if 35 - 35: IIiIi1iI + ooOoO0O00 % Ii1I % iiII11i1I1IIi + oo0oO00
def o0Oooo ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']Tv HUB[/COLOR]' , '[COLOR' + II + ']THE SOURCE[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   iiiI ( )
  if i11I1II1I11i == 1 :
   I1ii1 ( )
  if i11I1II1I11i == 2 :
   O00 ( )
  if i11I1II1I11i == 3 :
   Oo0o0000OOoO ( )
  if i11I1II1I11i == 4 :
   IiIi1I1ii111 ( )
  if i11I1II1I11i == 5 :
   IiIiIi ( )
  if i11I1II1I11i == 6 :
   IIIII1 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9002 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Tv HUB[/COLOR]' , str ( ooOO0O0ooOooO ) , 90050 , oOOOo00O00oOo + 'Tv HUB.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '' , 10040 , oOOOo00O00oOo + 'WatchSeries.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '' , 8020 , oOOOo00O00oOo + 'iWatchSeries.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 8064 , oOOOo00O00oOo + 'ClassicTV.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , oOOOo00O00oOo + 'TVShowTrailers.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def iIi1Ii1i1iI ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   IIiI1 = '[COLOR' + II + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   i1iI1 = '[COLOR' + II + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   ii1I1IiiI1ii1i = '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   O0o = '[COLOR' + II + ']APPRENTICE[/COLOR]'
  i1Oo0oO00o = [ IIiI1 , i1iI1 , '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , O0o , '[COLOR' + II + ']RAIZ TV[/COLOR]' , ii1I1IiiI1ii1i , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   oO0OoO00o ( ( i11 ( 'aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9tYWlubWVudS5waHA=' ) ) )
  if i11I1II1I11i == 1 :
   II1iiiiII ( )
  if i11I1II1I11i == 2 :
   Iiii1iI1i ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , I1ii1ii11i1I , I1111i )
  if i11I1II1I11i == 3 :
   O0OoOO0oo0 ( )
  if i11I1II1I11i == 4 :
   Iiii1iI1i ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , I1ii1ii11i1I , I1111i )
  if i11I1II1I11i == 5 :
   oOO ( )
  if i11I1II1I11i == 6 :
   Iiii1iI1i ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , I1ii1ii11i1I , I1111i )
  if i11I1II1I11i == 7 :
   Iiii1iI1i ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9tYWluLnBocA==' ) ) , I1ii1ii11i1I , I1111i )
 else :
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvbWFpbm1lbnUucGhw' ) ) , 90037 , oOOOo00O00oOo + 'TheReaper.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']PANDORAS BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 10025 , oOOOo00O00oOo + 'PandorasBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'DojoStreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'Roadrunner-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'Technica-Streams.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , '' , 1017 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'raiztv.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 1023 , oOOOo00O00oOo + 'ScoobyStreams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'ITVStreams.png' , O0o0Oo , '' )
  if 53 - 53: O00OOo00oo0o * OOoOoo . I1ii11iIi11i - iIi1i1ii1 % iIi1i1ii1 * Ii
 I1I11i ( 'movies' , 'MAIN' )
 if 7 - 7: o0o00Oo0O . iIi1i1ii1
def OO0oOOoo ( ) :
 IIiiiI1iIII ( )
 OOiIiIIi1 ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
def oOOO00o000o ( url ) :
 iIIII = iIi11i1 ( url )
 url = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( iIIII )
 for oO00oo0o00o0o , IiIIIIIi in IIIII11I1IiI :
  if '[DIR]' in oO00oo0o00o0o :
   IiIi1iIIi1 ( ( '[COLOR' + II + ']' + IiIIIIIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + IiIIIIIi , 1018 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'mkv' in IiIIIIIi :
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + IiIIIIIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + IiIIIIIi , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'avi' in IiIIIIIi :
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + IiIIIIIi + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + IiIIIIIi , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
   if 81 - 81: o0o00Oo0O * IIiIiII11i + oOo0O0Ooo * Ii - Ii1I / oOo0O0Ooo
def O0OoOO0oo0 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , oOOOo00O00oOo + 'scraped.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 if 63 - 63: OOooOOo - ii % O00OOo00oo0o
def oOi11iI11iIiIi ( url ) :
 I1 = O00O0ooo0 ( url )
 IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( I1 )
 for I1111i , url , I1iii11 , ooo0O , o0ooooO0o0O , iII1iii in IIIII11I1IiI :
  if ooo0O == '123' :
   ooo0O = oOOOo00O00oOo + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = oOOOo00O00oOo + 'appstreams.png'
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100010 , ooo0O , o0ooooO0o0O , iII1iii )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , ooo0O , o0ooooO0o0O , iII1iii )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , ooo0O , o0ooooO0o0O , iII1iii )
  elif not 'http' in url :
   i11i1iiiII ( I1111i , url , 100009 , ooo0O , o0ooooO0o0O , iII1iii , '' )
  else :
   i11i1iiiII ( I1111i , url , 100005 , ooo0O , o0ooooO0o0O , iII1iii , '' )
   if 68 - 68: Ii * oO0o
def II1i ( url ) :
 I1 = O00O0ooo0 ( url )
 Ii1IIIIi1ii1I = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for url , o00O0O , iII1iii , o0ooooO0o0O , I1111i in Ii1IIIIi1ii1I :
  if o00O0O == '123' :
   o00O0O = oOOOo00O00oOo + 'appstreams.png'
  if o0ooooO0o0O == '123' :
   o0ooooO0o0O = O0o0Oo
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 100004 , o00O0O , o0ooooO0o0O , iII1iii )
  elif 'playlist' in url :
   iiOOooooO0Oo ( I1111i , url , 100007 , o00O0O , o0ooooO0o0O , iII1iii )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( I1111i , url , 100100 , o00O0O , o0ooooO0o0O , iII1iii )
  elif not 'http' in url :
   i11i1iiiII ( I1111i , url , 100009 , o00O0O , o0ooooO0o0O , iII1iii , '' )
  else :
   i11i1iiiII ( I1111i , url , 100005 , o00O0O , o0ooooO0o0O , iII1iii , '' )
   if 13 - 13: oOo0O0Ooo % OOooOOo . Ii1I / I1ii11iIi11i % IIi . ii
def i1iIi ( url ) :
 if 30 - 30: o0o00Oo0O - iI11I1II1I1I / ii
 I1 = O00O0ooo0 ( url )
 O0000OOO0 = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( I1 )
 for ooo0 in O0000OOO0 :
  ooo0O = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( ooo0 ) )
  for ooo0O in ooo0O :
   ooo0O = ooo0O
  I1111i = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( ooo0 ) )
  for I1111i in I1111i :
   if 'elete' in I1111i :
    pass
   elif 'rivate Vid' in I1111i :
    pass
   else :
    I1111i = ( I1111i ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  oO000oOo00o0o = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( ooo0 ) )
  for oO000oOo00o0o in oO000oOo00o0o :
   oO000oOo00o0o = oO000oOo00o0o
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( ooo0 ) )
  for url in url :
   url = url
  i11i1iiiII ( '[COLORred]' + str ( oO000oOo00o0o ) + '[/COLOR] : ' + str ( I1111i ) , str ( url ) , 100009 , str ( ooo0O ) , O0o0Oo , '' , '' )
  I1I11i ( 'movies' , '' )
  if 85 - 85: OooOO000 + ii * OooOO000 - O00OOo00oo0o % Ii
  if 71 - 71: Ii1I - IIiIi1iI / OOooOOo * OOooOOo / ooOoO0O00 . ooOoO0O00
  if 53 - 53: O00OOo00oo0o
  if 21 - 21: iiII11i1I1IIi
  if 92 - 92: Ii / O00OOo00oo0o - OooOO000 % IIiIi1iI * O00OOo00oo0o + I1ii11iIi11i
def ii1Oo0000oOo ( iconimage , url , extra ) :
 ooo0O = ' '
 I11o0oO00oO0o0o0 = ' '
 o0ooooO0o0O = ' '
 I1Iooooo = ' '
 i11IIIiI1I = O00O0ooo0 ( url )
 ooo0O = re . compile ( '<img src="(.+?)">' ) . findall ( i11IIIiI1I )
 for ooo0O in ooo0O :
  ooo0O = ooo0O
 o0iiiI1I1iIIIi1 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( i11IIIiI1I )
 for o0ooooO0o0O in o0iiiI1I1iIIIi1 :
  o0ooooO0o0O = o0ooooO0o0O
 IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( i11IIIiI1I )
 for url , I1Iooooo in IIIII11I1IiI :
  I1Iooooo = 'S' + ( I1Iooooo ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = I11i1I1I + url
  IiiI1iiiiI1iI ( ( I1Iooooo ) . replace ( '  ' , '' ) , url , 100101 , ooo0O , o0ooooO0o0O , I11o0oO00oO0o0o0 , '' )
  I1I11i ( 'Movies' , 'info' )
  if 43 - 43: oo0oO00 - ii
def ii1iI ( url , name , fanart , extra , iconimage ) :
 IIiooOooo0 = extra
 I1Iooooo = name
 i11IIIiI1I = O00O0ooo0 ( url )
 ooo0O = iconimage
 IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( i11IIIiI1I )
 for url , name , oO0OO0 in IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = I11i1I1I + url
  oO0OO0 = oO0OO0
  o0O0Oo00 = name + ' - [COLORred]' + oO0OO0 + '[/COLOR]'
  IiiI1iiiiI1iI ( o0O0Oo00 , url , 100102 , ooo0O , fanart , 'Aired : ' + oO0OO0 , o0O0Oo00 )
  if 51 - 51: IIi % iI11I1II1I1I - ii % IIiIi1iI * iI11I1II1I1I % oO0o
def oO0o00oOOooO0 ( name , URL , iconimage , fanart ) :
 I1 = O00O0ooo0 ( URL )
 IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , name in IIIII11I1IiI :
  for i11I in oO0Oo :
   if i11I in oO0o0 :
    URL = 'http://www.watchseriesgo.to/link/' + oO0o0
    i11i1iiiII ( name , URL , 100106 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( IIIII11I1IiI ) <= 0 :
  IiiI1iiiiI1iI ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 79 - 79: oO0o - iI11I1II1I1I + iIi1i1ii1 - O00OOo00oo0o
  if 93 - 93: IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + OOooOOo
def ooO0o ( url , name ) :
 o000 = name
 I1 = O00O0ooo0 ( url )
 IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( I1 )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( I1 )
 ooOoO00 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  IiI1i ( url , o000 )
 for url in i1I :
  IiI1i ( url , o000 )
 for url in ooOoO00 :
  IiI1i ( url , o000 )
  if 87 - 87: IIiIi1iI
def IiI1i ( url , season_name ) :
 if 'daclips.in' in url :
  IIIii ( url , season_name )
 elif 'filehoot.com' in url :
  O00OooOo00o ( url , season_name )
 elif 'allmyvideos.net' in url :
  IiI11i1IIiiI ( url , season_name )
 elif 'vidspot.net' in url :
  oOOo000oOoO0 ( url , season_name )
 elif 'vodlocker' in url :
  OoOo00o0OO ( url , season_name )
 elif 'vidto' in url :
  ii1IIIIiI11 ( url , season_name )
  if 40 - 40: I11i
  if 67 - 67: oo0oO00 + IIiIiII11i - o0o00Oo0O . oo0oO00 * IIiIiII11i * iiII11i1I1IIi
def ii1IIIIiI11 ( url , season_name ) :
 I1 = O00O0ooo0 ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for o00OO00O0oOO , I1111i in IIIII11I1IiI :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 51 - 51: OOoOoo * o0o00Oo0O / IIiIiII11i . iIi1i1ii1 % IIi / oOo0O0Ooo
  if 9 - 9: oOo0O0Ooo % oOo0O0Ooo % IIiIiII11i
def IiI11i1IIiiI ( url , season_name ) :
 I1 = O00O0ooo0 ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for o00OO00O0oOO , I1111i in IIIII11I1IiI :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 30 - 30: OOoOoo + O00OOo00oo0o - OOoOoo . OOoOoo - IIiIiII11i + o0o00Oo0O
def oOOo000oOoO0 ( url , season_name ) :
 I1 = O00O0ooo0 ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I1 )
 for o00OO00O0oOO , I1111i in IIIII11I1IiI :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 86 - 86: ooOoO0O00
def OoOo00o0OO ( url , season_name ) :
 I1 = O00O0ooo0 ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for o00OO00O0oOO in IIIII11I1IiI :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 41 - 41: OOooOOo * iiII11i1I1IIi / OOooOOo % oo0oO00
def IIIii ( url , season_name ) :
 I1 = O00O0ooo0 ( url )
 IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( I1 )
 for o00OO00O0oOO in IIIII11I1IiI :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 18 - 18: IIiIiII11i . ii % OOooOOo % iIi1i1ii1
def O00OooOo00o ( url , season_name ) :
 I1 = O00O0ooo0 ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for o00OO00O0oOO in IIIII11I1IiI :
  Ii1iI111 ( o00OO00O0oOO , season_name )
  if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def Ii1iI111 ( Link , season_name ) :
 if 'http:/' in Link :
  ii1Ii1IiIIi ( Link )
  if 83 - 83: iiII11i1I1IIi / Ii1I
def II1Ii11Ii1i1I ( url ) :
 I1 = OPEN_URL_1 ( url )
 ii1iIi1II = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 for url in ii1iIi1II :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 2 - 2: I1ii11iIi11i + OOooOOo - IIi . oOo0O0Ooo - IIi
def IiiI1iiiiI1iI ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  if 30 - 30: iiII11i1I1IIi / iIi1i1ii1 . OOoOoo . ii - I1ii11iIi11i
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIiii . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
 if 44 - 44: o0o00Oo0O * ii % IIiIi1iI + IIiIiII11i
 if 39 - 39: oo0oO00 % iI11I1II1I1I % o0o00Oo0O % ii * Ii1I + OooOO000
def i11i1iiiII ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIiii . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = False )
 return ii1iiIi1
 if 68 - 68: I1ii11iIi11i + Ii
def Oo0oOooo000OO ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 98 - 98: I11i + o0o00Oo0O % ooOoO0O00 - IIi + I1ii11iIi11i
def OoOo000oOo0oo ( url ) :
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0O . play ( url ) . strip ( )
 except : pass
 if 68 - 68: o0o00Oo0O + OOooOOo / oo0oO00 - IIi + iI11I1II1I1I % iIi1i1ii1
def ii1Ii1IiIIi ( url ) :
 oO0O = xbmc . Player ( )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 if 23 - 23: IIiIi1iI % I11i / iiII11i1I1IIi
def O00O0ooo0 ( url ) :
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
  if 5 - 5: iI11I1II1I1I
  if 72 - 72: oo0oO00 . O00OOo00oo0o / OOooOOo + iiII11i1I1IIi % iI11I1II1I1I
  if 42 - 42: Ii1I * OOooOOo % IIiIi1iI - OOooOOo . Ii - O00OOo00oo0o
def oOIIiIi ( ) :
 IIiiiI1iIII ( )
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
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'SearchCartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( ooOO0O0ooOooO ) , 21004 , oOOOo00O00oOo + 'watchcartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CARTOONS[/COLOR]' , '' , 10001 , oOOOo00O00oOo + 'Cartoons.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '' , 20000 , oOOOo00O00oOo + 'Cartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , oOOOo00O00oOo + 'anime.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def o0OoOO ( ) :
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
 if 26 - 26: IIiIiII11i % Ii % iI11I1II1I1I % iiII11i1I1IIi * iiII11i1I1IIi * Ii1I
 if 24 - 24: IIiIiII11i % O00OOo00oo0o - IIiIi1iI + oOo0O0Ooo * Ii1I
 if 2 - 2: iIi1i1ii1 - OOoOoo
def OO ( ) :
 I1 = O000oo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiooOOoooooo in IIIII11I1IiI :
  IIiooOOoooooo = ( str ( IIiooOOoooooo ) )
  if os . path . exists ( xbmc . translatePath ( IIiooOOoooooo ) ) :
   OO0OO00oo0 = ( IIiooOOoooooo ) . replace ( 'special://home/addons/' , '' )
   OO0O000 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + OO0OO00oo0 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   i11I1II1I11i = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if i11I1II1I11i == 0 :
    iIIIiIii ( IIiooOOoooooo )
    O0O0ooOOO ( )
   elif i11I1II1I11i == 1 :
    ooo ( IIiooOOoooooo )
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
 if 29 - 29: I1ii11iIi11i % oO0o % OOoOoo . I11i / ii * IIiIi1iI
 O0II11i11II . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 O0II11i11II . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 O0II11i11II . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 54 - 54: o0o00Oo0O
 if 68 - 68: oO0o * I11i . IIiIi1iI % oo0oO00 % O00OOo00oo0o
 if 75 - 75: OOooOOo
 if 34 - 34: o0o00Oo0O
def oO0OoO00o ( url ) :
 I1 = O000oo ( url )
 OooOOOo0 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 ooOoO00 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 Iii1I1111ii = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 O0O0o0o0o = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( I1 )
 for I1111i , url , iiO0oOo00o , o0ooooO0o0O , iII1iii in OooOOOo0 :
  if 'php' in url :
   iiOOooooO0Oo ( I1111i , url , 90037 , iiO0oOo00o , o0ooooO0o0O , iII1iii )
  elif I1111i == 'Search' :
   iiOOooooO0Oo ( 'Search' , url , 90038 , iiO0oOo00o , o0ooooO0o0O , iII1iii )
  else :
   OOiIiIIi1 ( I1111i , url , 222 , iiO0oOo00o , o0ooooO0o0O , iII1iii )
 for I1111i , o00O0O , url , IIIIIiI in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 90037 , o00O0O , IIIIIiI , '' )
 for I1111i , url , o00O0O , IIIIIiI in i1I :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , IIIIIiI , '' )
 for I1111i , url , o00O0O , IIIIIiI in ooOoO00 :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , IIIIIiI , '' )
 for I1111i , url , o00O0O , IIIIIiI in Iii1I1111ii :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , IIIIIiI , '' )
 for I1111i , url , o00O0O in O0O0o0o0o :
  OOiIiIIi1 ( I1111i , url , 222 , o00O0O , '' , '' )
  I1I11i ( 'tvshows' , 'Media Info 3' )
  if 80 - 80: iI11I1II1I1I * O00OOo00oo0o % iiII11i1I1IIi % I1ii11iIi11i
def OooOO0o0 ( ) :
 oOOoo0 = [ 'serialsearch' , 'moviesearch' ]
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 if iIi == '' :
  pass
 else :
  for OOOoO in oOOoo0 :
   oOooo = I11 + OOOoO + '.php'
   i11IIIiI1I = O000oo ( oOooo )
   if i11IIIiI1I != 'Opened' :
    Ii1IIIIi1ii1I = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( i11IIIiI1I )
    for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O , iII1iii in Ii1IIIIi1ii1I :
     if iIi in I1111i . lower ( ) :
      oo00OOoOoO00 = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( o00OO00OoO ) )
      for i11I in oo00OOoOoO00 :
       if i11I == oO0o0 :
        I1111i = '[COLORred]* [/COLOR]' + ( I1111i ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        I1iii = open ( oOOoo0Oo , "a" )
        I1iii . write ( 'item="' + I1111i + '"\n' )
        I1iii . close
      if 'php' in oO0o0 :
       iiOOooooO0Oo ( I1111i , oO0o0 , 90037 , iiO0oOo00o , o0ooooO0o0O , iII1iii )
      else :
       OOiIiIIi1 ( I1111i , oO0o0 , 222 , iiO0oOo00o , o0ooooO0o0O , iII1iii )
       if 51 - 51: Ii1I
   I1I11i ( 'tvshows' , 'Media Info 3' )
   if 41 - 41: Ii1I * IIiIi1iI - iIi1i1ii1 + I1ii11iIi11i
def IiIIIII11I ( ) :
 I1 = O000oo ( 'http://www.tvcatchup.com/channels/' )
 iii1i1iiiiIi = O000oo ( 'http://www.djing.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for Ii1I11I , o00O0O , oO0o0 in IIIII11I1IiI :
  O0OoO0ooOO0o ( Ii1I11I , 'http://www.tvcatchup.com' + oO0o0 , 90024 , 'http://www.tvcatchup.com' + o00O0O )
 for oO0o0 , o00O0O , I1111i in i1I :
  if 'Submit' in I1111i :
   pass
  elif '&lt;' in I1111i :
   pass
  else :
   OOiIiIIi1 ( 'DJing  ' + I1111i , oO0o0 , 90025 , 'http://www.djing.com' + o00O0O , O0o0Oo , '' )
  I1I11i ( 'movies' , 'MAIN' )
def iiIii1I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'var url = "([^"]*)";' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def i1I11iIiII ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 66 - 66: I1ii11iIi11i - I11i * OOoOoo + OOooOOo + I11i - iI11I1II1I1I
def I1ii1 ( ) :
 if 17 - 17: oo0oO00
 if 22 - 22: iiII11i1I1IIi + iI11I1II1I1I
 if 24 - 24: OOooOOo % ooOoO0O00 + OooOO000 . Ii . Ii1I
 if 17 - 17: Ii1I . IIiIiII11i . IIiIi1iI / Ii1I
 if 57 - 57: iiII11i1I1IIi
 if 67 - 67: oO0o . IIiIi1iI
 if 87 - 87: oo0oO00 % iIi1i1ii1
 if 83 - 83: IIiIiII11i - iiII11i1I1IIi
 if 35 - 35: ooOoO0O00 - iI11I1II1I1I + ooOoO0O00
 if 86 - 86: iI11I1II1I1I + OOooOOo . Ii - iIi1i1ii1
 if 51 - 51: OOooOOo
 IiIi1iIIi1 ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , oOOOo00O00oOo + 'seasons.png' )
 IiIi1iIIi1 ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , oOOOo00O00oOo + 'episodes.png' )
 IiIi1iIIi1 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , oOOOo00O00oOo + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 14 - 14: OOoOoo % oo0oO00 % I1ii11iIi11i - Ii
def o0OO000ooOo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( I1 )
 for url , I1111i , oOo00OooO0oO in IIIII11I1IiI :
  IiIi1iIIi1 ( ( I1111i + ' - ' + oOo00OooO0oO ) . replace ( '&amp;' , '&' ) , url , 90053 , oOOOo00O00oOo + 'seasons.png' )
  if 16 - 16: OOoOoo / I1ii11iIi11i + IIi / iIi1i1ii1
def IIIiiI1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , url , 90054 , oOOOo00O00oOo + 'episodes.png' )
  if 74 - 74: iiII11i1I1IIi - IIi + ooOoO0O00 . oOo0O0Ooo + IIi - iiII11i1I1IIi
def IiIiiiiI1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( I1 )
 for o00O0O , I1111i , url in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , url , 90054 , o00O0O )
 for url in next :
  IiIi1iIIi1 ( 'NEXT' , url , 90053 , oOOOo00O00oOo + 'Next.png' )
  if 62 - 62: Ii1I % OooOO000 * oO0o - ooOoO0O00
def OoOOo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( I1 )
 for o00O0O , oOo00OooO0oO , url , I1111i , iii1 in IIIII11I1IiI :
  iiOOooooO0Oo ( oOo00OooO0oO + ' - ' + I1111i + ' - ' + iii1 , url , 90044 , o00O0O , o00O0O , '' )
 for o00O0O , I1111i , url in i1I :
  IiIi1iIIi1 ( I1111i , url , 90044 , o00O0O , o00O0O , '' )
 for url in next :
  IiIi1iIIi1 ( 'NEXT' , url , 90053 , oOOOo00O00oOo + 'Next.png' )
  if 78 - 78: Ii1I + iiII11i1I1IIi - o0o00Oo0O
def i1I1iIi1IiI ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1111O0O000OOOo = 'http://onlinemovies.tube/?s=' + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 iIi = i1111O0O000OOOo . lower ( )
 I1 = O000oo ( iIi )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i , i11ii1Ii1 in IIIII11I1IiI :
  if 'season' in i11ii1Ii1 :
   IiIi1iIIi1 ( I1111i , oO0o0 , 90054 , o00O0O , o00O0O , '' )
  if 'episodes' in i11ii1Ii1 :
   IiIi1iIIi1 ( I1111i , oO0o0 , 90044 , o00O0O , o00O0O , '' )
 for oO0o0 in next :
  IiIi1iIIi1 ( 'NEXT' , oO0o0 , 90053 , oOOOo00O00oOo + 'Next.png' )
  if 25 - 25: IIi
def I1I ( ) :
 if 83 - 83: O00OOo00oo0o
 if 48 - 48: IIiIiII11i * IIi * O00OOo00oo0o
 if 50 - 50: OOoOoo % ooOoO0O00
 if 21 - 21: ii - iI11I1II1I1I
 if 93 - 93: oo0oO00 - I11i % OOooOOo . OOooOOo - IIiIi1iI
 if 90 - 90: IIiIi1iI + IIiIiII11i * Ii1I / iIi1i1ii1 . I11i + I11i
 if 40 - 40: IIiIi1iI / OOooOOo % Ii % Ii1I / oOo0O0Ooo
 if 62 - 62: ooOoO0O00 - OOooOOo
 if 62 - 62: ooOoO0O00 + I1ii11iIi11i % OOoOoo
 if 28 - 28: Ii1I . ooOoO0O00
 IiIi1iIIi1 ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , oOOOo00O00oOo + 'allmov.png' )
 IiIi1iIIi1 ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , oOOOo00O00oOo + 'Genre.png' )
 IiIi1iIIi1 ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , oOOOo00O00oOo + 'Years.png' )
 IiIi1iIIi1 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , oOOOo00O00oOo + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 10 - 10: oO0o / I1ii11iIi11i
def I1iII11iIII1i1I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( I1 )
 for url , I1111i , oOo00OooO0oO in IIIII11I1IiI :
  if 'genre' in url :
   IiIi1iIIi1 ( ( I1111i + ' - ' + oOo00OooO0oO ) . replace ( '&amp;' , '&' ) , url , 90043 , oOOOo00O00oOo + 'Genre.png' )
   if 63 - 63: I1ii11iIi11i + O00OOo00oo0o - IIiIiII11i
def i1iIIi1I1I11 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  if 'release' in url :
   IiIi1iIIi1 ( I1111i , url , 90043 , oOOOo00O00oOo + 'Years.png' )
   if 39 - 39: iI11I1II1I1I - ii
def oO0oooooo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( I1 )
 for o00O0O , I1111i , o0OO0Oo , url , iII1iii in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' ' + o0OO0Oo , url , 90044 , o00O0O , o00O0O , iII1iii )
 for o00O0O , I1111i , i11ii1Ii1 , url , I11iiii1I , iII1iii in i1I :
  if 'movies' in i11ii1Ii1 :
   iiOOooooO0Oo ( I1111i + ' - ' + I11iiii1I , url , 90044 , o00O0O , o00O0O , iII1iii )
 for url in next :
  IiIi1iIIi1 ( 'NEXT' , url , 90043 , oOOOo00O00oOo + 'Next.png' )
  if 3 - 3: o0o00Oo0O % ii / IIi
def ooOo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  o0oO0OoO0 ( url )
  if 70 - 70: oo0oO00 - oo0oO00
def o0oO0OoO0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( I1111i ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , oOOOo00O00oOo + 'movhub.png' )
def OoOO0OOoo ( ) :
 if 1 - 1: oOo0O0Ooo * Ii + O00OOo00oo0o * Ii + oO0o
 if 30 - 30: I1ii11iIi11i . oO0o
 if 57 - 57: iiII11i1I1IIi . I1ii11iIi11i + IIiIiII11i
 if 43 - 43: O00OOo00oo0o % OooOO000
 if 69 - 69: OooOO000 % oO0o
 if 86 - 86: oo0oO00 / oo0oO00
 if 28 - 28: Ii / I11i . iI11I1II1I1I / IIiIiII11i
 if 72 - 72: ii / oOo0O0Ooo + iIi1i1ii1 / OOooOOo * iIi1i1ii1
 if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + OooOO000 * iI11I1II1I1I % iIi1i1ii1
 if 25 - 25: iiII11i1I1IIi + OOooOOo . I11i % OOooOOo * IIi
 if 32 - 32: Ii - O00OOo00oo0o
 if 53 - 53: ii - OOoOoo
 if 87 - 87: oo0oO00 . oOo0O0Ooo
 if 17 - 17: iIi1i1ii1 . Ii
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1111O0O000OOOo = 'http://onlinemovies.tube/?s=' + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 iIi = i1111O0O000OOOo . lower ( )
 I1 = O000oo ( iIi )
 IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i , IIIiiiI in IIIII11I1IiI :
  if 'movies' in IIIiiiI :
   IiIi1iIIi1 ( IIIiiiI + '-' + I1111i , oO0o0 , 90044 , o00O0O )
 for oO0o0 in next :
  oO0oooooo ( oO0o0 )
  if 94 - 94: o0o00Oo0O - iiII11i1I1IIi - iI11I1II1I1I % IIiIi1iI / iIi1i1ii1 % OooOO000
def I1i11i ( ) :
 IiIi1iIIi1 ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O000oo ( 'http://www.join4films.com/' )
 IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , oO0o0 , 80006 , oOOOo00O00oOo + 'Desi.png' )
def iIi1IIi1ii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( I1111i , url , 80007 , o00O0O )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def I11Ii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  OOOOo0o00OO0000 ( url )
def iIiII ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1111O0O000OOOo = 'http://www.join4films.com/?s=' + ( i1111IIiii1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 iIi = i1111O0O000OOOo . lower ( )
 iIi1IIi1ii ( iIi )
 if 19 - 19: OOoOoo
 if 78 - 78: IIi % I11i
 if 39 - 39: Ii1I + oOo0O0Ooo - iI11I1II1I1I - I11i
 if 7 - 7: OOoOoo . OOooOOo / Ii1I . IIi * iiII11i1I1IIi - IIiIiII11i
 if 37 - 37: O00OOo00oo0o . OOooOOo / o0o00Oo0O * OooOO000
 if 7 - 7: oO0o * iiII11i1I1IIi + IIiIiII11i % Ii
 if 8 - 8: IIiIi1iI * o0o00Oo0O
 if 73 - 73: I11i / oo0oO00 / iiII11i1I1IIi / oO0o
 if 11 - 11: OOooOOo + OOoOoo - ii / oO0o
 if 34 - 34: IIiIi1iI
 if 45 - 45: IIiIi1iI / I1ii11iIi11i / iIi1i1ii1
 if 44 - 44: Ii1I - iIi1i1ii1 / IIiIiII11i * oO0o * I1ii11iIi11i
 if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * IIi % IIiIiII11i
 if 56 - 56: ii * I1ii11iIi11i . I1ii11iIi11i . Ii1I
 if 24 - 24: I1ii11iIi11i . iiII11i1I1IIi * iIi1i1ii1 % OooOO000 / IIi
 if 58 - 58: oOo0O0Ooo - Ii1I % o0o00Oo0O . oOo0O0Ooo % oO0o % OOoOoo
 if 87 - 87: oo0oO00 - Ii
def ooOoO ( ) :
 iiOOooooO0Oo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 if 23 - 23: iiII11i1I1IIi
def iIiiIiiIi ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1111O0O000OOOo = 'http://imoviemax.se/?s=' + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 iIi = i1111O0O000OOOo . lower ( )
 i1iiIIIi ( iIi )
def Oo0o ( url ) :
 oOOoOoo0O0 = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , I1111i , i1i1ii1111i1i in IIIII11I1IiI :
  if I1111i in oOOoOoo0O0 :
   pass
  else :
   iiOOooooO0Oo ( I1111i + ' - ' + i1i1ii1111i1i + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
   oOOoOoo0O0 . append ( I1111i )
   if 46 - 46: ooOoO0O00
def ooO0o0oO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , oo0O in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + ' - Views:' + oo0O , url , 10075 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
  if 6 - 6: I1ii11iIi11i . OOoOoo / OOoOoo - Ii
  if 87 - 87: I1ii11iIi11i / o0o00Oo0O * OOoOoo / I11i
def i1iiIIIi ( url ) :
 I1iiIII = [ ]
 I1 = O000oo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  iiOOooooO0Oo ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , I1111i , url in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10075 , o00O0O , o00O0O , '' )
  I1iiIII . append ( I1111i )
  if 16 - 16: oo0oO00 + IIiIi1iI / I11i
def O00oOoo0OoO0 ( img , name , url ) :
 img = img
 name = name
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for Ooo0 , url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  oooO00o0 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + oooO00o0
  o0o00oO0oo000 = ( Ooo0 ) . replace ( 'play-' , 'Server ' )
  OOiIiIIi1 ( o0o00oO0oo000 , oooO00o0 , 10076 , img , img , '' )
  if 89 - 89: oO0o + OOoOoo * O00OOo00oo0o
def Ii1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for IiIIIIIi in IIIII11I1IiI :
  if '=m' in IiIIIIIi :
   ooo0O0OO ( IiIIIIIi )
  elif 'php' in IiIIIIIi :
   Ii1 ( url )
  else :
   I1 = O000oo ( IiIIIIIi )
   IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for O0Oooo in IIIII11I1IiI :
    ooo0O0OO ( IiIIIIIi )
    if 77 - 77: IIiIiII11i
    if 42 - 42: iIi1i1ii1 * O00OOo00oo0o . OOoOoo * oOo0O0Ooo + OOooOOo
    if 25 - 25: iiII11i1I1IIi . oOo0O0Ooo + oo0oO00
def O00OO0o0 ( url ) :
 I1 = O000oo ( url )
 oOOOooOo0O = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oO0OO0 , III1i111i in oOOOooOo0O :
  print 'there ><><><><><><><><><><><><'
  oO0OO0 = oO0OO0
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( III1i111i ) )
  for I1111i , iI1i in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + oO0OO0 + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + iI1i + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
 ooo0 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oO0OO0 , i111iiIIII in ooo0 :
  print 'there ><><><><><><><><><><><><'
  oO0OO0 = oO0OO0
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i111iiIIII ) )
  for I1111i , iI1i in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + oO0OO0 + '[/COLOR] - ' + I1111i + ' - [COLOR' + II + ']' + iI1i + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
   if 80 - 80: I1ii11iIi11i * iIi1i1ii1 + Ii1I * IIi
   if 16 - 16: iiII11i1I1IIi / oOo0O0Ooo + oO0o % iI11I1II1I1I - ooOoO0O00 . oo0oO00
   if 26 - 26: I11i * OOoOoo . ooOoO0O00
def IIIII1 ( url ) :
 I1 = O000oo ( url )
 ooo0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
 for ooo0 in ooo0 :
  I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ooo0 ) )
  for I1111i in I1111i :
   I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ooo0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  ooo0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ooo0 ) )
  for ooo0O in ooo0O :
   ooo0O = 'http:' + ooo0O
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , '' , '' )
  if 59 - 59: o0o00Oo0O + ooOoO0O00 - I11i
  if 62 - 62: Ii % IIi . OOoOoo . IIi
  if 84 - 84: Ii * oO0o
  if 18 - 18: IIi - iIi1i1ii1 - OOooOOo / O00OOo00oo0o - o0o00Oo0O
def IiIi ( url ) :
 if 30 - 30: o0o00Oo0O + Ii1I + IIiIiII11i
 III1I = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for IiIIIIIi , o00O0O , I1111i , I1I111iIi in IIIII11I1IiI :
  I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O000oo ( IiIIIIIi )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for ii1iIi1II , I11o0oO00oO0o0o0 in i1I :
   OoOOOO = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( I11o0oO00oO0o0o0 ) )
   for iII1iii in OoOOOO :
    if I1111i in III1I :
     pass
    else :
     OOiIiIIi1 ( I1111i , ii1iIi1II , 8043 , o00O0O , o00O0O , iII1iii )
     I1I11i ( 'movies' , 'INFO' )
     III1I . append ( I1111i )
     if 18 - 18: IIiIi1iI % Ii . iI11I1II1I1I - OooOO000
     if 80 - 80: oOo0O0Ooo + oo0oO00 - ooOoO0O00 . iIi1i1ii1 / I11i / oOo0O0Ooo
def I1Iiii ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , I1ii1ii11i1I , iII1iii , o0ooooO0o0O , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 10065 , I1ii1ii11i1I , o0ooooO0o0O , iII1iii )
 I1I11i ( 'movies' , 'INFO' )
 if 34 - 34: iIi1i1ii1 * OOooOOo - OOoOoo - oOo0O0Ooo - iIi1i1ii1
def Ii1iIi111I1i ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1111O0O000OOOo = 'https://www.youtube.com/results?search_query=' + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 iIi = i1111O0O000OOOo . lower ( )
 I1 = O000oo ( iIi )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for oO0o0 in next :
  oO0o0 = 'https://www.youtube.com' + oO0o0
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , oO0o0 , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for o00O0O , oO0o0 , I1111i , I1III111i , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  oOoOooOo0o0 . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  ooo0O = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooo0O
  oO0o0 = 'http://www.youtube.com' + oO0o0
  OOiIiIIi1 ( '[COLORred]' + I1III111i + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , ooo0O , I11o0oO00oO0o0o0 )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for o00O0O , oO0o0 , I1111i , I1III111i in IIIII11I1IiI :
   print 'im doing it'
   I1I11i ( 'tvshows' , 'INFO' )
   ooo0O = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   oO0o0 = 'http://www.youtube.com' + oO0o0
   if '&' in oO0o0 :
    print ' i got here'
    I1 = O000oo ( oO0o0 )
    ooo0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for ooo0 in ooo0 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ooo0 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oO0o0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ooo0 ) )
     for oO0o0 in oO0o0 :
      oO0o0 = 'https://www.youtube.com/w' + oO0o0
     ooo0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ooo0 ) )
     for ooo0O in ooo0O :
      ooo0O = 'http:' + ooo0O
     OOiIiIIi1 ( '[COLORred]' + I1III111i + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , O0o0Oo , '' )
   elif I1111i in oOoOooOo0o0 :
    pass
   elif 'user' in oO0o0 or 'elete' in I1111i :
    pass
   elif 'hannel' in oO0o0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oO0o0
    I1 = O000oo ( oO0o0 )
    iiI1iii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for o00O0O , oO0o0 , I1111i in iiI1iii :
     if 'outube' in oO0o0 or 'list' in oO0o0 :
      pass
     elif 'atch' in oO0o0 :
      oO0o0 = ( oO0o0 ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + I1III111i + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + I1III111i + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , ooo0O , '' )
    if 79 - 79: oO0o * OOooOOo . ii - iiII11i1I1IIi * I11i
def o000o0O0Oo00 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for o00O0O , url , I1111i , I1III111i , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  oOoOooOo0o0 . append ( I1111i )
  I1I11i ( 'tvshows' , 'INFO' )
  ooo0O = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooo0O
  url = 'http://www.youtube.com' + url
  OOiIiIIi1 ( '[COLORred]' + I1III111i + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , ooo0O , I11o0oO00oO0o0o0 )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for o00O0O , url , I1111i , I1III111i in IIIII11I1IiI :
   I1I11i ( 'tvshows' , 'INFO' )
   ooo0O = 'http:' + ( o00O0O ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    I1 = O000oo ( url )
    ooo0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for ooo0 in ooo0 :
     I1111i = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( ooo0 ) )
     for I1111i in I1111i :
      I1111i = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( ooo0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     ooo0O = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( ooo0 ) )
     for ooo0O in ooo0O :
      ooo0O = 'http:' + ooo0O
     OOiIiIIi1 ( '[COLORred]' + I1III111i + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , O0o0Oo , '' )
   elif I1111i in oOoOooOo0o0 :
    pass
   elif 'user' in url or 'elete' in I1111i :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O000oo ( url )
    iiI1iii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for o00O0O , url , I1111i in iiI1iii :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + I1III111i + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + o00O0O , 'http:' + o00O0O , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + I1III111i + '[/COLOR]' + '[COLOR' + II + ']' + I1111i + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O , ooo0O , '' )
    if 60 - 60: OOooOOo
    if 5 - 5: oOo0O0Ooo - oOo0O0Ooo - oOo0O0Ooo * ii
def iIIiIiI1I1 ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  iiiiiII = open ( IIIii1II1II )
  IIIII11I1IiI = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( iiiiiII ) )
  for ii1ii , IIiI1i in IIIII11I1IiI :
   if ii1ii == 'needs replacing' or IIiI1i == 'needs replacing' :
    iII1 ( )
    if 70 - 70: OooOO000 / IIi % IIiIi1iI - iIi1i1ii1
  iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if 47 - 47: OooOO000
def o00Ooo0 ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOOO + ")" )
 iII1 ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 62 - 62: IIi + iIi1i1ii1 - OOooOOo * OOooOOo . OOooOOo + ii
def Oo0 ( ) :
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
 if 80 - 80: iIi1i1ii1 - I11i
def iI1II1I1I ( name ) :
 OOo0 = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , o00O0O , oOO0o0oo0 , oO0o0 in IIIII11I1IiI :
  if OOo0 == 'Full List' :
   oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
  else :
   OOo0 = ( OOo0 ) . replace ( 'World' , 'القنوات العربية' )
   if OOo0 in oOO0o0oo0 :
    oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
    print oO0o0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
   else :
    pass
    if 78 - 78: IIi + OooOO000 . OOoOoo
def Oo ( name ) :
 OOo0 = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , o00O0O , oO0o0 in IIIII11I1IiI :
  oO0o0 = ( oO0o0 ) . replace ( '.ts' , '.m3u8' )
  OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oO0o0 ) . strip ( ) , 10012 , o00O0O , o00O0O , '' )
 else :
  OOiIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 15 - 15: Ii1I + IIi / Ii1I / O00OOo00oo0o
  if 31 - 31: IIiIi1iI + o0o00Oo0O + IIiIi1iI . iI11I1II1I1I + I1ii11iIi11i / I11i
  if 6 - 6: I1ii11iIi11i % OOoOoo * iiII11i1I1IIi / oOo0O0Ooo + I1ii11iIi11i
  if 39 - 39: OOooOOo - I1ii11iIi11i / OooOO000 * ii
  if 100 - 100: o0o00Oo0O . iiII11i1I1IIi . oO0o + o0o00Oo0O * oo0oO00
  if 42 - 42: oo0oO00 % ii + I11i
  if 56 - 56: ii + Ii1I - OooOO000
  if 24 - 24: I11i + IIiIi1iI + iiII11i1I1IIi - iI11I1II1I1I
  if 49 - 49: iiII11i1I1IIi . IIiIi1iI * OOooOOo % OOoOoo . o0o00Oo0O
  if 48 - 48: o0o00Oo0O * iIi1i1ii1 - o0o00Oo0O / iIi1i1ii1 + OOooOOo
  if 52 - 52: oO0o % iIi1i1ii1 * IIiIiII11i
  if 4 - 4: iiII11i1I1IIi % o0o00Oo0O - ii + IIiIi1iI . oo0oO00 % IIiIiII11i
def oo000o0000oO ( ) :
 iiOOooooO0Oo ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  iiOOooooO0Oo ( 'Backup Genie Favourites' , oO0o0 , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( O0Oo000ooO00 ) :
  iiOOooooO0Oo ( 'Backup Ivue Config' , O0Oo000ooO00 , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( oO0 ) :
  iiOOooooO0Oo ( 'Backup Kodi Favourites' , oO0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
  if 18 - 18: oO0o . IIiIiII11i % OOooOOo % iIi1i1ii1
  if 87 - 87: iI11I1II1I1I . ii * OOooOOo
zip = oo00 . getSetting ( 'zip' )
OOOo = xbmc . translatePath ( os . path . join ( zip ) )
def o0ooOo00O ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 38 - 38: iI11I1II1I1I + Ii * oO0o * IIiIi1iI % IIi
  if 5 - 5: IIiIi1iI - O00OOo00oo0o + oOo0O0Ooo * o0o00Oo0O / I1ii11iIi11i - iIi1i1ii1
  if 75 - 75: ii - IIi + I11i / OooOO000 % Ii
def iiiiii1 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Ii1iIiII1ii1
  elif 'Ivue' in name :
   url = O0Oo000ooO00
  elif 'Kodi' in name :
   url = oO0
  o0ooOo00O ( )
  OO0o0oO0O000o = open ( url ) . read ( )
  I1iI11iii = os . path . join ( OOOo , description . split ( 'Your ' ) [ 1 ] )
  oooOo0OOOoo0 = open ( I1iI11iii , mode = 'w' )
  oooOo0OOOoo0 . write ( OO0o0oO0O000o )
  oooOo0OOOoo0 . close ( )
 else :
  if 'guisettings.xml' in description :
   oo0oO = open ( os . path . join ( OOOo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiIi1iI11 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIIII11I1IiI = re . compile ( IiIi1iI11 ) . findall ( oo0oO )
   for type , iiI1iI1I , III1II111Ii1 in IIIII11I1IiI :
    III1II111Ii1 = III1II111Ii1 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , iiI1iI1I , III1II111Ii1 ) )
  else :
   I1iI11iii = os . path . join ( url )
   OO0o0oO0O000o = open ( os . path . join ( OOOo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   oooOo0OOOoo0 = open ( I1iI11iii , mode = 'w' )
   oooOo0OOOoo0 . write ( OO0o0oO0O000o )
   oooOo0OOOoo0 . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 82 - 82: O00OOo00oo0o - IIi + oO0o
 if 64 - 64: I11i . o0o00Oo0O * iIi1i1ii1 + ii - I1ii11iIi11i . ii
 if 70 - 70: I1ii11iIi11i - oo0oO00 . iI11I1II1I1I % iiII11i1I1IIi / OOooOOo - o0o00Oo0O
 if 55 - 55: OooOO000 - oO0o
def o0i1I11iI1iiI ( ) :
 I1ii = 1
 o0ooOo00O ( )
 oO0oI1I1 = xbmc . translatePath ( os . path . join ( OOOo , 'Build Backup' , 'Full Backup' , '' ) )
 O0Oo0 = xbmc . translatePath ( os . path . join ( OOOo , 'Build Backup' , 'my_full_backup.zip' ) )
 OOooO0OO0 = xbmc . translatePath ( os . path . join ( OOOo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( oO0oI1I1 ) :
  os . makedirs ( oO0oI1I1 )
 iI1iIiiiI1I1 = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not iI1iIiiiI1I1 ) : return False , 0
 OOOOOo = iI1iIiiiI1I1
 I1IiiiIiI = xbmc . translatePath ( os . path . join ( oO0oI1I1 , OOOOOo + '.zip' ) )
 O0Oo = [ 'plugin.video.GenieTv' ]
 I1Ii1iIiII = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 O0oOo00Ooo0o0 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 i1IiII1i1I = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iI1ii1ii1I = "Creating full backup of existing build"
 iI1IIi11i1I1 = "Creating Community Build"
 O00oo = "Archiving..."
 OoOo0oO0o = ""
 o0OoOo00ooO = "Please Wait"
 i111i ( Oo0o0000o0o0 , I1IiiiIiI , iI1IIi11i1I1 , O00oo , OoOo0oO0o , o0OoOo00ooO , O0oOo00Ooo0o0 , i1IiII1i1I )
 time . sleep ( 1 )
 II1III1i1iiI = xbmc . translatePath ( os . path . join ( oO0oI1I1 , OOOOOo + '_guisettings.zip' ) )
 I11i11i1 = zipfile . ZipFile ( II1III1i1iiI , mode = 'w' )
 try :
  I11i11i1 . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I11i11i1 . close ( )
 if I1ii == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + O0Oo0 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + I1IiiiIiI + '[/COLOR]' )
  if 68 - 68: I1ii11iIi11i . I1ii11iIi11i - Ii1I / iiII11i1I1IIi . IIiIi1iI / ooOoO0O00
def i111i ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iI1i1iIi1iiII = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0OoO0000o = len ( sourcefile )
 o0Ii1 = [ ]
 IIi1IiII = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for o0IIIIiI11I , iiiI11iIIi1 , o00OoooooooOo in os . walk ( sourcefile ) :
  for file in o00OoooooooOo :
   IIi1IiII . append ( file )
 iIii1I = len ( IIi1IiII )
 for o0IIIIiI11I , iiiI11iIIi1 , o00OoooooooOo in os . walk ( sourcefile ) :
  iiiI11iIIi1 [ : ] = [ iii11i1 for iii11i1 in iiiI11iIIi1 if iii11i1 not in exclude_dirs ]
  o00OoooooooOo [ : ] = [ oooOo0OOOoo0 for oooOo0OOOoo0 in o00OoooooooOo if oooOo0OOOoo0 not in exclude_files ]
  for file in o00OoooooooOo :
   o0Ii1 . append ( file )
   i1IiI1I111iIi = len ( o0Ii1 ) / float ( iIii1I ) * 100
   o0oOoO00o . update ( int ( i1IiI1I111iIi ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   IiiIIi1 = os . path . join ( o0IIIIiI11I , file )
   if not 'temp' in iiiI11iIIi1 :
    if not 'plugin.program.originwizard' in iiiI11iIIi1 :
     import time
     iI1iIiiI = '01/01/1980'
     Oo0OOo = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( IiiIIi1 ) ) )
     if Oo0OOo > iI1iIiiI :
      iI1i1iIi1iiII . write ( IiiIIi1 , IiiIIi1 [ o0OoO0000o : ] )
 iI1i1iIi1iiII . close ( )
 o0oOoO00o . close ( )
 if 36 - 36: o0o00Oo0O * oO0o % OooOO000 * OooOO000 / oO0o * OOoOoo
 if 14 - 14: ooOoO0O00 . OOoOoo + o0o00Oo0O * IIiIi1iI
def oOO ( ) :
 IIiiiI1iIII ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 if 76 - 76: oO0o
 if 92 - 92: iiII11i1I1IIi - iI11I1II1I1I % ii
def I1oOooo00O ( ) :
 IIiiiI1iIII ( )
 i1Oo0oO00o = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  iiIII1i ( )
 if i11I1II1I11i == 1 :
  iiiI ( )
 if i11I1II1I11i == 2 :
  o0oO0oOO ( )
 if i11I1II1I11i == 3 :
  Ii1iIi111I1i ( )
  if 66 - 66: OOooOOo + ooOoO0O00 % IIiIiII11i . o0o00Oo0O * Ii1I % Ii1I
  if 87 - 87: IIi + I11i . OooOO000 - ii
  if 6 - 6: iI11I1II1I1I * ii
  if 28 - 28: I1ii11iIi11i * I11i / O00OOo00oo0o
  if 52 - 52: o0o00Oo0O / I11i % OooOO000 * oOo0O0Ooo % IIi
  if 69 - 69: Ii1I
  if 83 - 83: I11i
  if 38 - 38: O00OOo00oo0o + ii . ooOoO0O00
  if 19 - 19: OooOO000 - I11i - iIi1i1ii1 - OOooOOo . OooOO000 . O00OOo00oo0o
def i11I1I ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   Iiii1iI1i ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , I1ii1ii11i1I , I1111i )
  if i11I1II1I11i == 1 :
   oO0OoO00o ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if i11I1II1I11i == 2 :
   oo0ooooo00o ( )
  if i11I1II1I11i == 3 :
   OoOo ( )
  if i11I1II1I11i == 4 :
   i111i1iIi1 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if i11I1II1I11i == 5 :
   OoO0oO ( )
  if i11I1II1I11i == 6 :
   IiiI1iiI1III1i ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if i11I1II1I11i == 7 :
   iii1i11 ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if i11I1II1I11i == 8 :
   oooOo ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if i11I1II1I11i == 9 :
   oo0oo0O0 ( )
  if i11I1II1I11i == 10 :
   IiIIiiI ( )
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
  if 60 - 60: O00OOo00oo0o
 I1I11i ( 'movies' , 'MAIN' )
 if 98 - 98: IIiIi1iI
def Ii11i1Ii1IIII ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i1Oo0oO00o = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   i1iiI ( )
  if i11I1II1I11i == 1 :
   iiIiIIIiiI ( )
  if i11I1II1I11i == 2 :
   oOOo0O00o ( )
  if i11I1II1I11i == 3 :
   oooO0oOoo ( oO0o0 )
  if i11I1II1I11i == 4 :
   OoOOoO0O0oO ( oO0o0 )
  if i11I1II1I11i == 5 :
   O0O0ooOOO ( )
  if i11I1II1I11i == 6 :
   oOOoO ( url = 'http://www.iplocation.net/' , inc = 1 )
  if i11I1II1I11i == 7 :
   oOo0Oo0O0O ( )
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
  if 48 - 48: I1ii11iIi11i - IIiIi1iI + I1ii11iIi11i - oOo0O0Ooo * Ii . OooOO000
  if 35 - 35: OOoOoo . o0o00Oo0O + I1ii11iIi11i + IIi + ooOoO0O00
 I1I11i ( 'movies' , 'MAIN' )
 if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
 if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
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
 if 58 - 58: IIi . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
 if 50 - 50: OooOO000 % IIiIiII11i - IIiIi1iI . ooOoO0O00 + o0o00Oo0O % OooOO000
def i1iIi1IIiIII1 ( ) :
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
 if 19 - 19: iiII11i1I1IIi
def iI1i111I1Ii ( ) :
 IIiiiI1iIII ( )
 OOiIiIIi1 ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 87 - 87: IIiIi1iI / OOooOOo % I11i * oo0oO00
def oOOOoo0o ( ) :
 IIiiiI1iIII ( )
 OOiIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , O0o0Oo , '' )
 if 44 - 44: o0o00Oo0O % ooOoO0O00
 if 42 - 42: IIiIiII11i - oO0o - ii . OooOO000 / OOooOOo
 if 56 - 56: Ii - iI11I1II1I1I . IIiIiII11i
def Iii1IIII11I ( ) :
 IIiiiI1iIII ( )
 i1Oo0oO00o = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  O00O ( )
 if i11I1II1I11i == 0 :
  II1 ( oO0o0 )
 if i11I1II1I11i == 0 :
  oOo00o ( oO0o0 )
  if 12 - 12: I11i * O00OOo00oo0o % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
  if 81 - 81: I1ii11iIi11i - iiII11i1I1IIi
  if 24 - 24: ii . oO0o * IIiIiII11i
 I1I11i ( 'movies' , 'MAIN' )
 if 59 - 59: O00OOo00oo0o + oO0o / IIi
def OO00o0O0O000o ( ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1Oo00 )
 for o00O0O , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , o00O0O , o00O0O , '' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 56 - 56: I1ii11iIi11i * OooOO000
def II1I1ii1ii11 ( url ) :
 i1Oo00 = O000oo ( OOo000OO000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 83 - 83: I11i % oo0oO00 + iiII11i1I1IIi % Ii + o0o00Oo0O
def O00O ( ) :
 IIiiiI1iIII ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 65 - 65: iI11I1II1I1I % oo0oO00 + o0o00Oo0O / ii
def O0000oO0o00 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + oo000oOO00o0oOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 27 - 27: I1ii11iIi11i
def oO0O0o0o00 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + i1IoOOoooO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 46 - 46: iI11I1II1I1I
def I111iiiii1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OO0ooOoOO0OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 51 - 51: iI11I1II1I1I * I11i / iI11I1II1I1I . iI11I1II1I1I . OooOO000 * iiII11i1I1IIi
def oO0oo0o00o0O ( url ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 80 - 80: iI11I1II1I1I
def II1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + i1I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 40 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 5 - 5: OOooOOo % OooOO000 + OOoOoo
def iiiIi1II1III ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + I1i11II11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 9 - 9: OOooOOo - Ii1I * IIiIi1iI . IIiIi1iI - oOo0O0Ooo
def OooOoOO0 ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OOooOooo0OOo0 ( )
 if i11I1II1I11i == 1 :
  oo0o0OoOO0o0 ( )
 if i11I1II1I11i == 2 :
  III1III11II ( )
  if 43 - 43: oOo0O0Ooo
  if 47 - 47: ii % OOooOOo
  if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . O00OOo00oo0o
  if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
def oo0o0OoOO0o0 ( ) :
 iIIII = iIi11i1 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( iIIII )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , OooOo in IIIII11I1IiI :
  IiIi1iIIi1 ( 'Android Apps' + OooOo , 'https://www.apkfiles.com' + oO0o0 , 30035 , oOOOo00O00oOo + 'apps.png' )
 for oO0o0 , OooOo in i1I :
  IiIi1iIIi1 ( 'Android Games' + OooOo , 'https://www.apkfiles.com' + oO0o0 , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 I1I11i ( 'movies' , 'MAIN' )
def oOo0I1Ii11i ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '/cat' in url :
   IiIi1iIIi1 ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def I1iIiiiI1 ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '/app' in url :
   IiIi1iIIi1 ( ( I1111i ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def OOO0O00Oo ( url ) :
 iIIII = O000oo ( url )
 ii1oOOO0ooOO = url
 if "page=" in str ( url ) :
  ii1oOOO0ooOO = url . split ( '?' ) [ 0 ]
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  if 'apk' in url :
   OOiIiIIi1 ( ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + o00O0O )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 OOiIiIIi1 ( 'Next Page' , ii1oOOO0ooOO + str ( i1I ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def i11IiI1iiI11 ( name , url ) :
 iIIII = iIi11i1 ( url )
 name = name
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  OOoOOOO00 ( name , url , 'Brackets' )
def III1III11II ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1111O0O000OOOo = 'https://www.apkfiles.com/search?q=' + ( i1111IIiii1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 iIi = i1111O0O000OOOo . lower ( )
 OOO0O00Oo ( iIi )
 if 49 - 49: oO0o - o0o00Oo0O / oO0o * OOooOOo + O00OOo00oo0o
def Iiii1I ( url ) :
 o00O0 = xbmc . translatePath ( os . path . join ( Ooo000000 , 'Download' ) )
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
 if 80 - 80: IIiIiII11i - IIi % ii . iI11I1II1I1I - IIiIi1iI + oOo0O0Ooo
def i1i1iiIIiiiII ( url ) :
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
 if 5 - 5: ii / I11i % iiII11i1I1IIi % oO0o * OooOO000 + iI11I1II1I1I
 if 11 - 11: O00OOo00oo0o % Ii % oo0oO00 . OOoOoo
def oOO0o ( name , url , description ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oOO0O00Oo0O0o = os . path . join ( o00O0 , name )
 try :
  os . remove ( oOO0O00Oo0O0o )
 except :
  pass
 downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
 o0OI1II = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print o0OI1II
 print '======================================='
 extract . all ( oOO0O00Oo0O0o , o0OI1II , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 9 - 9: I1ii11iIi11i % ii - iIi1i1ii1
 if 43 - 43: oO0o % oO0o
 if 46 - 46: I1ii11iIi11i % iI11I1II1I1I . OooOO000 . o0o00Oo0O * IIiIi1iI / ii
 if 7 - 7: oo0oO00 - o0o00Oo0O * iiII11i1I1IIi - I11i - IIiIiII11i
 if 41 - 41: oOo0O0Ooo - O00OOo00oo0o % IIiIiII11i . O00OOo00oo0o - iiII11i1I1IIi
def OOooOooo0OOo0 ( ) :
 i1Oo00 = O000oo ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1Oo00 )
 for I1111i , oO0o0 , iiO0oOo00o , o0ooooO0o0O , i1I111Ii in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , oO0o0 , 80003 , iiO0oOo00o , oOOOo00O00oOo + 'APKToolsB.png' , i1I111Ii )
def i11i1i ( apk , ret = None ) :
 if apk == "kodi" :
  I1ii1Ii1 = "https://kodi.tv/download/"
  i1Oo00 = O000oo ( I1ii1Ii1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1Oo00 )
  if len ( IIIII11I1IiI ) == 1 :
   OoO = IIIII11I1IiI [ 0 ] [ 0 ]
   OOOOOo = IIIII11I1IiI [ 0 ] [ 1 ]
   oOiI111I1III = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( OoO , OOOOOo )
  if ret == 'version' : return OoO
  else : return oOiI111I1III
 elif apk == "spmc" :
  i111IiiI1Ii = 'https://github.com/koying/SPMC/releases/latest/'
  i1Oo00 = O000oo ( i111IiiI1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1Oo00 )
  OoO = re . sub ( '<[^<]+?>' , '' , IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  oOiI111I1III = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( OoO , OoO )
  if ret == 'version' : return OoO
  else : return oOiI111I1III
def OOoOOOO00 ( name , url , Brackets ) :
 if I1IIII1i ( ) == 'android' :
  OooOOOOOo = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not OooOOOOOo : i1I11ii ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  o0ooO00O0O = name
  if OooOOOOOo :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not Iii1 ( url ) == True : i1I11ii ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % o0ooO00O0O , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    I11i11i1 = zipfile . ZipFile ( oOO0O00Oo0O0o )
    for file in I11i11i1 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as oooOo0OOOoo0 :
       iiiI1iI1 = file . split ( '/' ) [ 1 ]
       oooOo0OOOoo0 . write ( I11i11i1 . read ( file ) )
       xbmc . sleep ( 500 )
       oooOo0OOOoo0 . close ( )
       try :
        os . remove ( oOO0O00Oo0O0o )
       except :
        pass
       oOO0O00Oo0O0o = os . path . join ( i1iiIII111ii , iiiI1iI1 )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : i1I11ii ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : i1I11ii ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 15 - 15: OOoOoo . ooOoO0O00 * OOooOOo % iI11I1II1I1I
 if 35 - 35: Ii1I + O00OOo00oo0o - OOooOOo % oo0oO00 % I11i % OOooOOo
 if 45 - 45: oOo0O0Ooo * IIi % oO0o
 if 24 - 24: IIiIi1iI - iiII11i1I1IIi * oo0oO00
def O00OoOoO ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1Oo00 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  oO0o0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oO0o0 )
  ooO0o0oo ( ( I1111i ) . replace ( '_' , ' ' ) , oO0o0 )
  if 79 - 79: OOoOoo % oO0o
def ooO0o0oo ( name , url ) :
 if I1IIII1i ( ) == 'android' :
  OooOOOOOo = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not OooOOOOOo : i1I11ii ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  o0ooO00O0O = name
  if OooOOOOOo :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not Iii1 ( url ) == True : i1I11ii ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % o0ooO00O0O , '' , 'Please Wait' )
   oOO0O00Oo0O0o = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( oOO0O00Oo0O0o )
   except : pass
   downloader . download ( url , oOO0O00Oo0O0o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oOO0O00Oo0O0o + '")' )
  else : i1I11ii ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : i1I11ii ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 81 - 81: Ii + Ii * oO0o + OOoOoo
 if 32 - 32: o0o00Oo0O . ii
def iiIIiiIi ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'INFO' )
 if 42 - 42: OooOO000 + iI11I1II1I1I
 if 21 - 21: OOooOOo - I1ii11iIi11i % o0o00Oo0O . oO0o + OOooOOo
def oOo0 ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 30015 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 41 - 41: IIiIiII11i * IIiIi1iI
def o0oOoOo0 ( url , iconimage , fanart ) :
 i1Oo00 = O000oo ( url )
 oooO00o0 = url
 o00O0O = iconimage
 fanart = fanart
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for IiIIIIIi , I1111i in IIIII11I1IiI :
  if '.mp4' in I1111i :
   OOiIiIIi1 ( 'Watch VIDEO' , url + '/' + IiIIIIIi , 222 , o00O0O , fanart , '' )
  if 'description' in I1111i :
   OOiIiIIi1 ( 'Read Description' , url + '/' + IiIIIIIi , 30017 , o00O0O , fanart , '' )
  if 'images' in I1111i :
   iiOOooooO0Oo ( 'View Images' , url + '/' + IiIIIIIi , 30018 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Android' , url + '/' + IiIIIIIi , 30016 , o00O0O , fanart , '' )
  if 'url' in I1111i :
   OOiIiIIi1 ( 'Install Build On Pc' , url + '/' + IiIIIIIi , 30019 , o00O0O , fanart , '' )
 I1I11i ( 'movies' , 'INFO' )
 if 38 - 38: I11i % O00OOo00oo0o + Ii + OooOO000 + IIiIi1iI / Ii
def o0OOOOOo0 ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  oooOoO ( url )
  if 62 - 62: IIi / IIiIiII11i + OOooOOo % IIiIi1iI / OOooOOo + Ii1I
def IiI11I111 ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  Ooo000O00 ( url )
  if 36 - 36: IIi % Ii
def Iiii1Ii ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1Oo00 )
 for ooOOo00oo0 in IIIII11I1IiI :
  OO0O000 ( 'Description:' , ooOOo00oo0 )
  if 40 - 40: OOooOOo - IIi - IIi - o0o00Oo0O - o0o00Oo0O . IIiIiII11i
def o0o000Oo ( url ) :
 i1Oo00 = O000oo ( url )
 url = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for IiIIIIIi , I1111i in IIIII11I1IiI :
  if 'png' in I1111i :
   OOiIiIIi1 ( 'image' , '' , '' , url + '/' + IiIIIIIi , url + '/' + IiIIIIIi , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 57 - 57: oo0oO00 * o0o00Oo0O * O00OOo00oo0o
def I1II1 ( name , url , description ) :
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
 if 89 - 89: oO0o / oO0o
 if 1 - 1: Ii1I . Ii
def Ooo000O00 ( url ) :
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
 i1iiI ( )
 if 74 - 74: o0o00Oo0O + ii / oo0oO00 / OOooOOo . Ii1I % oo0oO00
def oooOoO ( url ) :
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
 i1iiI ( )
 if 34 - 34: ooOoO0O00 . oOo0O0Ooo
def i11I1IIiiii ( name , url , description ) :
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
 i1iiI ( )
 if 85 - 85: iI11I1II1I1I
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
  oOo0O = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  oooOo0OOOoo0 . write ( oOo0O . rstrip ( '\r\n' ) + '\n' )
def i1iiI ( ) :
 i11I1II1I11i = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if i11I1II1I11i == 0 : return
 elif i11I1II1I11i == 1 : pass
 i1i = I1IIII1i ( )
 iIiIi11 ( "Platform: " + str ( i1i ) )
 os . _exit ( 1 )
 iIiIi11 ( "Force close failed!  Trying alternate methods." )
 if i1i == 'osx' :
  iIiIi11 ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif i1i == 'linux' :
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
 elif i1i == 'android' :
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
 elif i1i == 'windows' :
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
  if 60 - 60: I1ii11iIi11i . OOoOoo % oOo0O0Ooo - O00OOo00oo0o
  if 79 - 79: ii / Ii1I . o0o00Oo0O
  if 79 - 79: oo0oO00 - IIiIiII11i
def oOo00o ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for Ii1iiI1 , iiiI11iIIi1 , o00OoooooooOo in os . walk ( url ) :
  for file in o00OoooooooOo :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    oo0oO = open ( ( os . path . join ( Ii1iiI1 , file ) ) ) . read ( )
    o0ooOOoO0oO0 = oo0oO . replace ( Oo0o0000o0o0 , 'special://home/' )
    oooOo0OOOoo0 = open ( ( os . path . join ( Ii1iiI1 , file ) ) , mode = 'w' )
    oooOo0OOOoo0 . write ( str ( o0ooOOoO0oO0 ) )
    oooOo0OOOoo0 . close ( )
 i1iiI ( )
 if 86 - 86: ooOoO0O00 / iIi1i1ii1 * oOo0O0Ooo
def oo0ooooo00o ( ) :
 IiIi1iIIi1 ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 IiIi1iIIi1 ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 IiIi1iIIi1 ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 67 - 67: Ii1I * Ii1I / oo0oO00 * ii + OOooOOo
def oooo ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def o0o0oo0Ooo ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def iI1ii11I ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in i1I :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']Filter - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , o00O0O )
def o0oO0o0oo0O0 ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def O0oo00oOOO0o ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1
 II1iI111iiIIiI1I = 'https://www.radionomy.com/en/search/index?query=' + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 I1 = O000oo ( II1iI111iiIIiI1I )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( '[COLOR' + II + ']Stream - ' + I1111i + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oO0o0 , 70005 , o00O0O )
  if 51 - 51: oOo0O0Ooo + IIi + iiII11i1I1IIi
  if 50 - 50: O00OOo00oo0o + Ii1I
def OoO0oO ( ) :
 iIIII = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , 'http://www.listenlive.eu/' + oO0o0 , 10111113 , oOOOo00O00oOo + 'radio.png' )
def i111i1iIi1 ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  O0OoO0ooOO0o ( I1111i , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 4 - 4: OOoOoo / I1ii11iIi11i
def I1IIiiII ( ) :
 iIIII = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.toonjet.com/' + oO0o0 , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def oOOO0oOoo ( url ) :
 iIIII = iIi11i1 ( url )
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
   IiIi1iIIi1 ( ( o00O0O ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOOo00O00oOo + 'vod.png' )
 for url in i1I :
  IiIi1iIIi1 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOOo00O00oOo + 'Next.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0O0ooooooo00 ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  O0OoO0ooOO0o ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 28 - 28: IIiIi1iI * iiII11i1I1IIi % Ii * OooOO000 / iIi1i1ii1
  if 41 - 41: IIi - I11i + iIi1i1ii1
def IiIIiiI ( ) :
 i1II ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 i1II ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 79 - 79: OOooOOo % oOo0O0Ooo % iIi1i1ii1 / ooOoO0O00 % oO0o
def oo0o00OO ( ) :
 i1II ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 i1II ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 i1II ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 69 - 69: I11i % Ii / iIi1i1ii1
def ooOOO00oOOooO ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for I1111i , oO0o0 , IiI in IIIII11I1IiI :
  if 'Parent' in I1111i :
   pass
  elif '2' in IiI :
   i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 4 - 4: ii + IIiIi1iI . ooOoO0O00 / o0o00Oo0O - o0o00Oo0O
def oOooOOo00ooO ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for I1111i , oO0o0 , IiI in IIIII11I1IiI :
  if i1111IIiii1 in I1111i . lower ( ) :
   if '1' in IiI :
    i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in IiI :
    i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in IiI :
    i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 71 - 71: O00OOo00oo0o - I11i - IIi
    if 28 - 28: iI11I1II1I1I
def iI11II1i1I1 ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for I1111i , oO0o0 , IiI in IIIII11I1IiI :
  if '1' in IiI :
   i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in IiI :
   i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in IiI :
   i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oO0o0 , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 72 - 72: OooOO000 - ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 25 - 25: OOooOOo % ii * I1ii11iIi11i - ooOoO0O00 * IIiIiII11i * oo0oO00
def I1iI1I1ii1 ( url ) :
 IiIIIIIi = url
 I1 = O000oo ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
 for url , I1111i in i1I :
  if 'mp3' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in I1111i :
   i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIIIIIi + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 33 - 33: I11i / o0o00Oo0O + IIi
   if 75 - 75: OOoOoo % Ii + iI11I1II1I1I
   if 92 - 92: OOooOOo % o0o00Oo0O
def oo00ooooOOo00 ( url ) :
 I1 = O000oo ( url )
 IiIIIIIi = url
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
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIIIIIi + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , IiIIIIIi + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 16 - 16: Ii / ooOoO0O00 % IIi
   if 84 - 84: iiII11i1I1IIi - I1ii11iIi11i * o0o00Oo0O / iIi1i1ii1 . iIi1i1ii1
def ooO0 ( ) :
 i1II ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 i1II ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 i1II ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 34 - 34: ooOoO0O00 % OOoOoo
def OoOoIiI1 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O in IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oO0o0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in o00O0O :
   pass
  else :
   i1II ( o00O0O , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oO0o0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + o00O0O + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 13 - 13: ii + oO0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: o0o00Oo0O + oo0oO00 % I1ii11iIi11i
 if 7 - 7: Ii1I / IIiIi1iI
def I1i1I11111iI1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 32 - 32: oOo0O0Ooo + Ii1I - oo0oO00 + Ii1I / ooOoO0O00 * oo0oO00
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: iIi1i1ii1 % oo0oO00
def iiii1 ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if i1111IIiii1 in I1111i . lower ( ) :
   if '</a>' in I1111i :
    pass
   elif '(' in I1111i :
    i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 60 - 60: oOo0O0Ooo % oo0oO00 / I11i % oo0oO00 * Ii / OooOO000
    if 34 - 34: O00OOo00oo0o - IIi
def IIIiIi1iiI ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if '</a>' in I1111i :
   pass
  elif '(' in I1111i :
   i1II ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oO0o0 , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 15 - 15: Ii1I . OooOO000
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 94 - 94: iiII11i1I1IIi . oOo0O0Ooo
 if 73 - 73: ooOoO0O00 / IIiIiII11i
def I1i1I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  IiIIIIIi = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( IiIIIIIi )
  if 17 - 17: iiII11i1I1IIi - OooOO000 % iIi1i1ii1
def i11Ii1iIIIIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for I1111i , url in IIIII11I1IiI :
  if '<p align' in I1111i :
   pass
  elif '&nbsp;' in I1111i :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 14 - 14: ii . I11i . iiII11i1I1IIi
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 50 - 50: IIiIi1iI * OOooOOo + Ii1I - Ii + I1ii11iIi11i * Ii1I
 if 20 - 20: O00OOo00oo0o / I11i % OOooOOo
def O000o0 ( ) :
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
def O00oo0O00 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o0oO00o = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , o00O0O , o00O0O , I1111i )
 for url , I1111i in o0oO00o :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def OOO0OoO0oo0OO ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 oO0O = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 i1iI1Ii11Ii1 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 o0OoO0oo0O0o = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in i1iI1Ii11Ii1 :
  iiOOooooO0Oo ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , I1111i in oO0O :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def ii1III1iiIi ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 35 - 35: IIi + o0o00Oo0O . Ii % Ii1I
def OO0ooOOO0O00o ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if '9cart' in oO0o0 :
   IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 99 - 99: I11i
def I11IIII1111II ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( I1 )
 ooOoO00 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if '9cart' in url :
   IiIi1iIIi1 ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   IiIi1iIIi1 ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url , I1111i in ooOoO00 :
  if '9cart' in url :
   IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 6 - 6: iI11I1II1I1I / IIi + iiII11i1I1IIi
def o0o00OOOO ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20003 , o00O0O )
 for url , I1111i in i1I :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 42 - 42: IIiIi1iI * OooOO000
def i1iIIiI1111 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'Watch' in url :
   IiIi1iIIi1 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 91 - 91: ii / I11i . OOoOoo - iI11I1II1I1I - iIi1i1ii1
def I1iIiIii ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 76 - 76: oO0o . ii % O00OOo00oo0o * iIi1i1ii1
def i1iiI1i ( url ) :
 url = cloudflare . source ( url )
 ooo0O0OO ( url )
 if 70 - 70: iIi1i1ii1 * oo0oO00 - iiII11i1I1IIi + I1ii11iIi11i % Ii1I - OOoOoo
def oooOoO00OooO0 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in IIIII11I1IiI :
  ooo0O0OO ( url )
  if 98 - 98: IIi + iIi1i1ii1
  if 52 - 52: I1ii11iIi11i / OOooOOo - O00OOo00oo0o . OooOO000
def oO0o000OoOoO0 ( ) :
 if 50 - 50: iI11I1II1I1I - OooOO000 - iiII11i1I1IIi
 iiOOooooO0Oo ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 60 - 60: iI11I1II1I1I * IIiIi1iI
def o0oO0oOO ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 71 - 71: OOooOOo % I1ii11iIi11i % IIiIi1iI
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 34 - 34: iiII11i1I1IIi / iiII11i1I1IIi % OOoOoo . OOooOOo / I1ii11iIi11i
 for oO0o0 , I1111i in IIIII11I1IiI :
  if i1111IIiii1 in I1111i . lower ( ) :
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
    if 99 - 99: IIiIi1iI * oOo0O0Ooo - IIiIi1iI % iIi1i1ii1
    if 40 - 40: IIi / OOoOoo / iI11I1II1I1I + iIi1i1ii1
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 59 - 59: iiII11i1I1IIi * ii + IIi . iI11I1II1I1I / ooOoO0O00
def Ooo0o0oo ( url ) :
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
 if 75 - 75: iiII11i1I1IIi . IIi - iI11I1II1I1I * oO0o * OooOO000
def ooo0OO0OOooO0 ( url ) :
 iIIII = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  O00O00 = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10007 , O00O00 )
  if 66 - 66: I1ii11iIi11i - iI11I1II1I1I
  if 9 - 9: I11i % Ii1I . Ii1I
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 28 - 28: ii % oo0oO00 + Ii1I + o0o00Oo0O . O00OOo00oo0o
def ooOO0OOO00o ( url , IMAGE ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   OoOoO0ooooO0 ( url )
   if 4 - 4: I1ii11iIi11i - oO0o - Ii * O00OOo00oo0o / iIi1i1ii1 - IIi
   if 45 - 45: I11i % I1ii11iIi11i * ooOoO0O00 - o0o00Oo0O
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 82 - 82: IIiIiII11i / OooOO000
def OoOoO0ooooO0 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 96 - 96: I1ii11iIi11i / oo0oO00 . IIiIiII11i . I1ii11iIi11i
  if 91 - 91: IIiIiII11i . IIi + I11i
  if 8 - 8: IIi * I1ii11iIi11i / OooOO000 - oO0o - ii
def O0O0Oo00 ( ) :
 if 100 - 100: oo0oO00 . iI11I1II1I1I . iI11I1II1I1I
 iiOOooooO0Oo ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , O0o0Oo , '' )
 if 55 - 55: oo0oO00
def i1iiIo0o ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  if 'elete' in I1111i :
   pass
  else :
   O0OoO0ooOO0o ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 222 , o00O0O )
   if 73 - 73: OOooOOo % I11i
def OO0o0OO0 ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0OooOooO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , o00oO0o00O , i1iII1IiiIiI1 in O0OooOooO :
  for i1111IIiii1 in o00oO0o00O :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   i11i11Iiii11i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oO0o0 , I1111i in i11i11Iiii11i :
    if 'tube' in oO0o0 :
     pass
    elif 'stage' in oO0o0 :
     O0OoO0ooOO0o ( '[COLOR' + II + ']' + o00oO0o00O + '   -   ' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O , )
    elif 'vee' in oO0o0 :
     pass
     if 6 - 6: OOooOOo - IIiIi1iI * I11i + OOooOOo % I11i
def OOO00000o0 ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 O0OooOooO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , o00oO0o00O , i1iII1IiiIiI1 in O0OooOooO :
  i11i11Iiii11i = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oO0o0 , I1111i in i11i11Iiii11i :
   if 'tube' in oO0o0 :
    pass
   elif 'stage' in oO0o0 :
    O0OoO0ooOO0o ( '[COLOR' + II + ']' + o00oO0o00O + '   -   ' + I1111i + '[/COLOR]' , ( oO0o0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + o00O0O )
   elif 'vee' in oO0o0 :
    pass
    if 96 - 96: I11i * oo0oO00 - IIi * I11i * ooOoO0O00
    if 8 - 8: IIiIi1iI - I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * iIi1i1ii1 - iI11I1II1I1I
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: iiII11i1I1IIi / Ii1I
def II1Ii11Ii1i1I ( url ) :
 I1 = O000oo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 ii1iIi1II = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( ii1iIi1II ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in ii1iIi1II :
  OOOOo0o00OO0000 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 22 - 22: oo0oO00 * OooOO000
  if 4 - 4: OOooOOo - oo0oO00 + oOo0O0Ooo
  if 36 - 36: OOoOoo
  if 19 - 19: OOooOOo . I11i . ii
  if 13 - 13: IIi . I1ii11iIi11i / IIiIiII11i
  if 43 - 43: iI11I1II1I1I % oO0o
  if 84 - 84: I1ii11iIi11i
def II1iiiiII ( ) :
 if 44 - 44: ii * Ii / I1ii11iIi11i
 OoOoO00o00 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 OoOoO00o00 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 51 - 51: I1ii11iIi11i * iI11I1II1I1I . ii . iIi1i1ii1 - IIi / oOo0O0Ooo
 I1I11i ( 'movies' , 'MAIN' )
 if 98 - 98: IIiIiII11i + iIi1i1ii1 + ii / ooOoO0O00 - iIi1i1ii1
def O0o0 ( ) :
 OoOoO00o00 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 OoOoO00o00 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 81 - 81: ii - Ii1I * ooOoO0O00 - Ii . IIiIi1iI
 I1I11i ( 'movies' , 'MAIN' )
def oooOoOoOO ( ) :
 if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 iiI1ii1Iii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 2 - 2: oOo0O0Ooo * I1ii11iIi11i % I11i % I1ii11iIi11i
 for OOOoO in iiI1ii1Iii :
  oOooo = OOOO0OOoO0O0 + OOOoO + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( oOooo )
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for oO0o0 , I1ii1ii11i1I , iII1iii , o0ooooO0o0O , I1111i in IIIII11I1IiI :
   if i1111IIiii1 in I1111i . lower ( ) :
    o0o0oO ( I1111i , oO0o0 , 222 , I1ii1ii11i1I , o0ooooO0o0O , iII1iii )
    if 92 - 92: iiII11i1I1IIi / o0o00Oo0O * oOo0O0Ooo - iiII11i1I1IIi
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 99 - 99: Ii % ii
    if 56 - 56: OOoOoo * O00OOo00oo0o
def O00oO0O ( ) :
 if 3 - 3: iI11I1II1I1I % Ii1I . IIi % iiII11i1I1IIi
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 iiI1ii1Iii = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 40 - 40: IIiIi1iI * iIi1i1ii1 . iIi1i1ii1 + IIiIiII11i + ii
 for OOOoO in iiI1ii1Iii :
  i11I1Iii1I = OOOO0OOoO0O0 + OOOoO + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( i11I1Iii1I )
  IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for I1111i , iII1iii , oO0o0 , o00O0O , o0ooooO0o0O , I1iii11 in IIIII11I1IiI :
   if i1111IIiii1 in I1111i . lower ( ) :
    OoOoO00o00 ( I1111i , oO0o0 , I1iii11 , o00O0O , o0ooooO0o0O , iII1iii )
    if 18 - 18: ooOoO0O00
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 4 - 4: OOoOoo
    if 93 - 93: oo0oO00 % ooOoO0O00
def OOo0OOoo00 ( ) :
 if 22 - 22: IIiIi1iI / IIiIi1iI - iIi1i1ii1 % iiII11i1I1IIi . IIi + OOoOoo
 iIIII = O000oo ( OOOO0OOoO0O0 + 'spongemain.php' )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , iII1iii , oO0o0 , o00O0O , o0ooooO0o0O , I1iii11 in IIIII11I1IiI :
  OoOoO00o00 ( I1111i , oO0o0 , I1iii11 , o00O0O , o0ooooO0o0O , iII1iii )
  I1I11i ( 'movies' , 'MAIN' )
def OooO00oo0O0 ( url ) :
 if 10 - 10: OOoOoo / ii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiiiIIiii = ( '%s%s' % ( OO0Oo00Oo , url ) )
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , I1ii1ii11i1I , iII1iii , o0iiiI1I1iIIIi1 , I1111i in IIIII11I1IiI :
  oo00OOoOoO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
  for i11I in oo00OOoOoO00 :
   if i11I == url :
    I1111i = ( '[COLORred]Watched - [/COLOR]' + I1111i ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  o0o0oO ( I1111i , url , 222 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii )
  if 25 - 25: iI11I1II1I1I
  I1I11i ( 'movies' , 'MAIN' )
  if 63 - 63: IIiIi1iI
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 96 - 96: iiII11i1I1IIi
  if 34 - 34: OOooOOo / oO0o - oOo0O0Ooo . o0o00Oo0O . IIi
def oooO0o0oOoO ( url ) :
 if 23 - 23: OOoOoo + iI11I1II1I1I % iI11I1II1I1I / IIiIi1iI . oo0oO00 + iI11I1II1I1I
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iIIII )
 for I1111i , iII1iii , url , o00O0O , o0ooooO0o0O , I1iii11 in IIIII11I1IiI :
  OoOoO00o00 ( I1111i , url , I1iii11 , o00O0O , o0ooooO0o0O , iII1iii )
  if 93 - 93: oo0oO00 * I11i / IIi - IIi . OooOO000 / oOo0O0Ooo
  I1I11i ( 'movies' , 'MAIN' )
  if 11 - 11: O00OOo00oo0o - iiII11i1I1IIi % Ii . iI11I1II1I1I * oOo0O0Ooo - I1ii11iIi11i
  if 73 - 73: o0o00Oo0O + IIiIi1iI - o0o00Oo0O / ii * I1ii11iIi11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: oO0o % oOo0O0Ooo % OooOO000
def o0o0oO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 66 - 66: OOooOOo + I11i
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = False )
 return ii1iiIi1
 if 54 - 54: Ii1I + Ii1I + iiII11i1I1IIi % ooOoO0O00 % Ii
def OoOoO00o00 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 100 - 100: Ii1I
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
if 96 - 96: oOo0O0Ooo . OOoOoo * IIiIiII11i % OOoOoo . O00OOo00oo0o * ooOoO0O00
if 83 - 83: iI11I1II1I1I
if 97 - 97: Ii + I1ii11iIi11i * IIi % OooOO000 . OOoOoo
if 4 - 4: o0o00Oo0O . OooOO000 - iI11I1II1I1I
if 19 - 19: IIi % oO0o / iIi1i1ii1 + IIiIiII11i % ii
if 89 - 89: iIi1i1ii1
if 51 - 51: OooOO000
if 68 - 68: OooOO000 - I11i * oO0o % IIiIi1iI . IIiIi1iI - iI11I1II1I1I
if 22 - 22: ii / Ii1I % OooOO000 * OOooOOo
if 32 - 32: ii % oo0oO00 % iI11I1II1I1I / o0o00Oo0O
if 61 - 61: IIiIiII11i . o0o00Oo0O - iIi1i1ii1 - Ii1I / Ii - IIiIiII11i
if 98 - 98: iIi1i1ii1 - oOo0O0Ooo . Ii * I1ii11iIi11i
if 29 - 29: iIi1i1ii1 / IIiIi1iI % iiII11i1I1IIi
if 10 - 10: iI11I1II1I1I % ii % Ii1I
if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * iiII11i1I1IIi
def O0o0O0O0O ( string ) :
 if OOO00O == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 79 - 79: OOoOoo + OOoOoo + iIi1i1ii1
def iiiII1i1I ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 OoooOoo0 = [ ]
 try :
  if 26 - 26: OOoOoo / iI11I1II1I1I - iI11I1II1I1I
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( OOOOi11i1 ) == False :
  O0o0O0O0O ( 'Making Favorites File' )
  OoooOoo0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oo0oO = open ( OOOOi11i1 , "w" )
  oo0oO . write ( json . dumps ( OoooOoo0 ) )
  oo0oO . close ( )
 else :
  O0o0O0O0O ( 'Appending Favorites' )
  oo0oO = open ( OOOOi11i1 ) . read ( )
  oO00oO00O0Oo = json . loads ( oo0oO )
  oO00oO00O0Oo . append ( ( name , url , iconimage , fanart , mode ) )
  o0ooOOoO0oO0 = open ( OOOOi11i1 , "w" )
  o0ooOOoO0oO0 . write ( json . dumps ( oO00oO00O0Oo ) )
  o0ooOOoO0oO0 . close ( )
  if 88 - 88: oo0oO00 - ooOoO0O00 % Ii % IIiIiII11i * ii
  if 40 - 40: I1ii11iIi11i
def iI1Ii11 ( ) :
 if os . path . exists ( OOOOi11i1 ) == False :
  OoooOoo0 = [ ]
  O0o0O0O0O ( 'Making Favorites File' )
  OoooOoo0 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  oo0oO = open ( OOOOi11i1 , "w" )
  oo0oO . write ( json . dumps ( OoooOoo0 ) )
  oo0oO . close ( )
 else :
  Ooo0IiiiIIi = json . loads ( open ( OOOOi11i1 ) . read ( ) )
  I1IIIi = len ( Ooo0IiiiIIi )
  for OoOooOo00O in Ooo0IiiiIIi :
   I1111i = OoOooOo00O [ 0 ]
   oO0o0 = OoOooOo00O [ 1 ]
   I1ii1ii11i1I = OoOooOo00O [ 2 ]
   try :
    oo0O0oOOO0o = OoOooOo00O [ 3 ]
    if oo0O0oOOO0o == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     oo0O0oOOO0o = I1ii1ii11i1I
    else :
     oo0O0oOOO0o = o0ooooO0o0O
   try : oOo0Oo0Oo0 = OoOooOo00O [ 5 ]
   except : oOo0Oo0Oo0 = None
   try : OooOo0o0OO = OoOooOo00O [ 6 ]
   except : OooOo0o0OO = None
   if 1 - 1: iI11I1II1I1I % IIiIi1iI + o0o00Oo0O
   if OoOooOo00O [ 4 ] == 0 :
    iiOOooooO0Oo ( I1111i , oO0o0 , '' , I1ii1ii11i1I , o0ooooO0o0O , '' , 'fav' )
   else :
    iiOOooooO0Oo ( I1111i , oO0o0 , OoOooOo00O [ 4 ] , I1ii1ii11i1I , o0ooooO0o0O , '' , 'fav' )
    if 22 - 22: I11i + I1ii11iIi11i . IIiIi1iI + Ii1I * OooOO000 . Ii
def O0OOOOOO0ooO ( name ) :
 oO00oO00O0Oo = json . loads ( open ( OOOOi11i1 ) . read ( ) )
 for II11IiI1 in range ( len ( oO00oO00O0Oo ) ) :
  if oO00oO00O0Oo [ II11IiI1 ] [ 0 ] == name :
   del oO00oO00O0Oo [ II11IiI1 ]
   o0ooOOoO0oO0 = open ( OOOOi11i1 , "w" )
   o0ooOOoO0oO0 . write ( json . dumps ( oO00oO00O0Oo ) )
   o0ooOOoO0oO0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 86 - 86: iI11I1II1I1I % oo0oO00 - OOooOOo + O00OOo00oo0o % oO0o . Ii1I
 if 4 - 4: ooOoO0O00 + OOooOOo
def iII1 ( ) :
 ii11I11 = os . path . join ( I11i1 , 'addons.ini' )
 ooo0o0 = open ( ii11I11 , "w+" )
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 ooo0o0 . write ( r'[' + IiII + ']' + '\n' )
 for I1111i , o00O0O , oOO0o0oo0 , oO0o0 in IIIII11I1IiI :
  oO0o0 = ( oO0o0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  o0Oo = ( I1111i + '=plugin://' + IiII + '/?url=' + oO0o0 + '&mode=10012&name=' + ( I1111i ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( o00O0O ) . replace ( ' ' , '' ) + '+&amp;description=' )
  ooo0o0 . write ( o0Oo + '\n' )
  if 16 - 16: OooOO000 % oOo0O0Ooo - IIiIi1iI
  if 100 - 100: ii * oo0oO00
def OoO0o0OO ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 in IIIII11I1IiI :
  IiIi1iIIi1 ( '24/7' , oO0o0 , 90021 , oOOOo00O00oOo + '247Streams.png' )
  if 10 - 10: oo0oO00 - OooOO000 % IIiIiII11i - O00OOo00oo0o - ooOoO0O00
def iIi11iI1i ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , oOOOo00O00oOo + '247Streams.png' , oOOOo00O00oOo + '247Streams.png' , '' )
def OoOo ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def OOoOooOoOOOoo ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def Ii1iIi ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , ( oO0o0 ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def OOo0OOOoOOo ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( I1111i , oO0o0 , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 29 - 29: OOooOOo . OooOO000 + OOooOOo + o0o00Oo0O . o0o00Oo0O * IIi
  if 38 - 38: OooOO000 * ii
def iIi11III ( ) :
 if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
 iiOOooooO0Oo ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 if 33 - 33: O00OOo00oo0o % IIiIiII11i
def IIi1II ( ) :
 if 40 - 40: IIi / OOoOoo
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i , iI1i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i + '  -  ' + ( iI1i ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oO0o0 , 10023 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 29 - 29: iIi1i1ii1 - iIi1i1ii1 / IIiIi1iI
  if 49 - 49: iiII11i1I1IIi + oo0oO00 % oO0o - I1ii11iIi11i - o0o00Oo0O - ii
  if 4 - 4: IIiIiII11i - oo0oO00 % I1ii11iIi11i * Ii
def iIiII1iiiiI ( ) :
 if 80 - 80: I1ii11iIi11i - I11i - IIiIiII11i . OOoOoo - o0o00Oo0O * OOoOoo
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
 if 43 - 43: oOo0O0Ooo / OooOO000 / IIiIi1iI + iI11I1II1I1I + ii
def iiI111i1 ( url ) :
 oooO00o0 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( oooO00o0 )
 IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 41 - 41: Ii * o0o00Oo0O - OooOO000 . IIiIiII11i % oO0o % Ii1I
  if 32 - 32: IIi + OooOO000 + iI11I1II1I1I * I1ii11iIi11i
  if 62 - 62: Ii
  if 2 - 2: oOo0O0Ooo
def oo0OO0o0o0ooO0ooo ( ) :
 if 47 - 47: OOoOoo
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 oO0o0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( oO0o0 )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  if i1111IIiii1 in I1111i . lower ( ) :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 76 - 76: oO0o * iI11I1II1I1I + Ii1I - IIiIi1iI - iiII11i1I1IIi / ooOoO0O00
   if 27 - 27: Ii1I . OOoOoo
   if 66 - 66: o0o00Oo0O / o0o00Oo0O * ooOoO0O00 . ii % iI11I1II1I1I
def I11iIiI1 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for IiIIIIIi , I1Iooooo , i1I1iiii1Ii11 , I1111i in IIIII11I1IiI :
  IiIIIIi = ( i1I1iiii1Ii11 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  OoIIiIIIII1I = ( I1Iooooo ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ooiiI = 'Season ' + OoIIiIIIII1I + 'Episode ' + IiIIIIi + I1111i
  o00iIiI1iI1Ii1 ( ooiiI , IiIIIIIi )
  if 24 - 24: ii . OOoOoo
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 15 - 15: OOooOOo
  if 34 - 34: o0o00Oo0O / IIi
def o00iIiI1iI1Ii1 ( name , url ) :
 IiIIIIIi = url
 OOOoo0O00Oooo = name
 iii1i1iiiiIi = cloudflare . source ( IiIIIIIi )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for ii1iIi1II , I11iIIi in i1I :
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + OOOoo0O00Oooo + I11iIIi + '[/COLOR]' , ii1iIi1II , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 36 - 36: iIi1i1ii1 * O00OOo00oo0o * iI11I1II1I1I - iiII11i1I1IIi % Ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: iI11I1II1I1I - ooOoO0O00 + IIiIi1iI % iiII11i1I1IIi + IIiIi1iI / oo0oO00
 if 97 - 97: OOoOoo % IIiIi1iI + IIiIiII11i - OOoOoo % oO0o + IIiIi1iI
def O00 ( ) :
 if 31 - 31: I11i
 if 35 - 35: OOooOOo + iIi1i1ii1 * IIiIi1iI / OOooOOo
 if 69 - 69: IIiIi1iI . IIi - oOo0O0Ooo
 if 29 - 29: Ii . Ii1I / oOo0O0Ooo . IIi + Ii
 if 26 - 26: OOoOoo / iIi1i1ii1 - ii
 if 9 - 9: ii * Ii1I
 if 9 - 9: I1ii11iIi11i + OooOO000
 iiOOooooO0Oo ( '[COLOR' + II + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , '' , 10091 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 64 - 64: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo
def OO0oo ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( I1 )
 oOOoOoOo00OOOOo = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + o00O0O , '' , '' )
 for url in oOOoOoOo00OOOOo :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 56 - 56: iIi1i1ii1 + oOo0O0Ooo - I11i / I11i . IIiIiII11i - iIi1i1ii1
def i1oo ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( I1 )
 oOOoOoOo00OOOOo = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  o00O0O = 'http://watchepisodes.cc/' + o00O0O
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10093 , o00O0O , o00O0O , '' )
 for url in oOOoOoOo00OOOOo :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 83 - 83: o0o00Oo0O + OOooOOo / o0o00Oo0O / iiII11i1I1IIi
def OoIi11ii1 ( url , iconimage ) :
 o00O0O = iconimage
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( I1 )
 for i1I1iiii1Ii11 , url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + i1I1iiii1Ii11 + ' - ' + I1111i + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , o00O0O , '' , '' )
  if 1 - 1: iI11I1II1I1I % oo0oO00 . iI11I1II1I1I
def i1IiiI1 ( url , iconimage ) :
 o00O0O = iconimage
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for I1111i , url in IIIII11I1IiI :
  if 'player' in I1111i :
   pass
  elif 'vod' in I1111i :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , o00O0O , '' , '' )
   if 83 - 83: OooOO000 - OOoOoo % oO0o - ii - IIi % ii
   if 75 - 75: IIiIiII11i + IIiIi1iI % IIi + I1ii11iIi11i
   if 70 - 70: oO0o
   if 43 - 43: OOooOOo
   if 57 - 57: oOo0O0Ooo
   if 65 - 65: Ii - IIiIi1iI * iiII11i1I1IIi + IIiIi1iI / OOoOoo + I11i
def Oo0o0000OOoO ( ) :
 if 35 - 35: o0o00Oo0O + I1ii11iIi11i - oOo0O0Ooo % iIi1i1ii1 % IIiIiII11i
 if 77 - 77: O00OOo00oo0o + oo0oO00
 if 38 - 38: Ii1I - iIi1i1ii1 * I11i
 if 13 - 13: oOo0O0Ooo * oo0oO00
 if 41 - 41: OOoOoo
 if 16 - 16: iI11I1II1I1I
 if 94 - 94: IIiIi1iI % iiII11i1I1IIi % ooOoO0O00
 if 90 - 90: iIi1i1ii1 * oO0o
 if 7 - 7: OooOO000 . iIi1i1ii1 . OooOO000 - O00OOo00oo0o
 if 33 - 33: IIiIi1iI + ii - oO0o / ooOoO0O00 / ii
 if 82 - 82: Ii1I / IIi - OooOO000 / I1ii11iIi11i * oO0o
 if 55 - 55: ii
 if 73 - 73: OOooOOo - Ii1I % I1ii11iIi11i + Ii1I - o0o00Oo0O . oO0o
 iiOOooooO0Oo ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 38 - 38: o0o00Oo0O
 if 79 - 79: ooOoO0O00 . oo0oO00
def i1i1i11iI11II ( url ) :
 I1 = O000oo ( url )
 ooo0 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( ooo0 ) )
 for url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 6 - 6: OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / iIi1i1ii1
def I1I1ii1111 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 4 - 4: Ii1I * o0o00Oo0O - O00OOo00oo0o - Ii / I11i . IIi
def i1ii11I111Ii ( url ) :
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
  if 77 - 77: oO0o + oO0o . IIiIi1iI * ii + oO0o
  if 6 - 6: ooOoO0O00 - iiII11i1I1IIi
def O0o00ooo ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiIIiiiI = 'http://www.watchseriesgo.to/search/' + i1111IIiii1 . replace ( ' ' , '%20' )
 I1 = O000oo ( iiiIIiiiI )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , oO0o0 , I1111i in IIIII11I1IiI :
  if 'watch online' in I1111i :
   pass
  else :
   print oO0o0
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.watchseriesgo.to' + oO0o0 , 10044 , o00O0O , '' , '' )
   if 50 - 50: O00OOo00oo0o + iiII11i1I1IIi / iIi1i1ii1 * IIi / I11i
   xbmcplugin . setContent ( I1IIiiIiii , 'movies' )
   if 27 - 27: o0o00Oo0O - iiII11i1I1IIi * IIiIiII11i - iI11I1II1I1I / IIiIi1iI
def II1iOOoOooO0o ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i , i1I1iiii1Ii11 , iII1iii in IIIII11I1IiI :
  o000 = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( i1I1iiii1Ii11 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + o000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , o00O0O , '' , iII1iii )
  if 28 - 28: OOoOoo + Ii + ii / oO0o
def iIiI1111 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  o000 = ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + o000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 60 - 60: OooOO000 + oO0o + iiII11i1I1IIi % iI11I1II1I1I . I1ii11iIi11i
def O0OOOOoO00oo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , o00O0O , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 80 - 80: ooOoO0O00 . oOo0O0Ooo - oo0oO00 + IIi + OooOO000 % oo0oO00
def IiiII ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 ooo0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for I1Iooooo , O0OooOooO in ooo0 :
  IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( O0OooOooO ) )
  for url , I1111i in IIIII11I1IiI :
   o000 = ( I1Iooooo ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + o000 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for I1111i , url in IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 47 - 47: OooOO000 + o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . iIi1i1ii1
class IIioo0 ( ) :
 if 87 - 87: iiII11i1I1IIi . iiII11i1I1IIi . IIiIiII11i / IIi
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 86 - 86: oo0oO00 % o0o00Oo0O + oO0o
  o000 = name
  self . Get_Sources ( oO0o0 , o000 )
  if 52 - 52: I1ii11iIi11i / OooOO000
  if 42 - 42: iI11I1II1I1I * iIi1i1ii1 / oO0o + IIi
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O000oo ( URL )
  IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for oO0o0 , I1111i in IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + oO0o0
   self . Get_site_link ( URL , season_name )
   if 48 - 48: ii - O00OOo00oo0o . Ii * OooOO000 - iIi1i1ii1 - I11i
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
   if 59 - 59: OooOO000 / iiII11i1I1IIi . I1ii11iIi11i
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   o0III11IiI = 'DACLIPS'
   if o0III11IiI in IIioo0 . source_list :
    pass
   else :
    self . daclips ( url , season_name , o0III11IiI )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    o0III11IiI = 'THEVIDEO'
    if o0III11IiI in IIioo0 . source_list :
     pass
    else :
     self . thevideo ( url , season_name , o0III11IiI )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     o0III11IiI = 'ALLMYVIDEOS'
     if o0III11IiI in IIioo0 . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , o0III11IiI )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      o0III11IiI = 'VIDSPOT'
      if o0III11IiI in IIioo0 . source_list :
       pass
      else :
       self . vidspot ( url , season_name , o0III11IiI )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       o0III11IiI = 'VODLOCKER'
       if o0III11IiI in IIioo0 . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , o0III11IiI )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        o0III11IiI = 'VIDTO'
        if o0III11IiI in IIioo0 . source_list :
         pass
        else :
         self . vidto ( url , season_name , o0III11IiI )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 53 - 53: OooOO000 / ooOoO0O00 / ooOoO0O00
       else :
        if 'youwatch' in url :
         o0III11IiI = 'YouWatch'
         if o0III11IiI in IIioo0 . source_list :
          pass
         else :
          self . youwatch ( url , season_name , o0III11IiI )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 77 - 77: iiII11i1I1IIi + ooOoO0O00 . iiII11i1I1IIi
          if 89 - 89: I11i + IIi * oo0oO00
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for o00OO00O0oOO , I1111i in IIIII11I1IiI :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 45 - 45: OooOO000 - I11i . iIi1i1ii1
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for o00OO00O0oOO , I1111i in IIIII11I1IiI :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 41 - 41: IIiIiII11i . oOo0O0Ooo / oO0o . IIiIi1iI
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( I1 )
  for o00OO00O0oOO in IIIII11I1IiI :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 58 - 58: OOoOoo % Ii * IIiIiII11i . Ii1I
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for o00OO00O0oOO in IIIII11I1IiI :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 94 - 94: Ii . IIi + iI11I1II1I1I * O00OOo00oo0o * O00OOo00oo0o
 def daclips ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for o00OO00O0oOO in IIIII11I1IiI :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 36 - 36: iiII11i1I1IIi - OOoOoo . OOoOoo
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for o00OO00O0oOO in IIIII11I1IiI :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for o00OO00O0oOO in IIIII11I1IiI :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
  for o00OO00O0oOO in IIIII11I1IiI :
   self . youplay ( o00OO00O0oOO , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for o00OO00O0oOO in IIIII11I1IiI :
   self . Printer ( o00OO00O0oOO , season_name , source_name )
   if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
 def Printer ( self , Link , season_name , source_name ) :
  if 84 - 84: iI11I1II1I1I + ii
  if Link in IIioo0 . List :
   pass
  elif source_name in IIioo0 . source_list :
   pass
  else :
   O0OoO0ooOO0o ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   IIioo0 . List . append ( Link )
   IIioo0 . source_list . append ( source_name )
   if 77 - 77: o0o00Oo0O * Ii1I * oo0oO00 + oO0o + Ii1I - O00OOo00oo0o
   xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 10 - 10: Ii1I + OOoOoo
   if 58 - 58: oOo0O0Ooo + ii / OooOO000 . IIiIi1iI % I11i / Ii1I
   if 62 - 62: IIiIiII11i
   if 12 - 12: OOoOoo + IIiIiII11i
   if 92 - 92: O00OOo00oo0o % iI11I1II1I1I - OooOO000 / Ii % IIiIi1iI * I11i
def iiI ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , O0o0Oo , '' )
 if 80 - 80: OooOO000
def iI1I1ii11IIi1 ( url ) :
 iiOOooooO0Oo ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( iIIII )
 for OOo , url , OOoOO , O0O00 , I1iIiiI11 , iii11i1 , i1ii1111iiI , oooOo0OOOoo0 , oo0oO , iiIIIII , iiI1 in IIIII11I1IiI :
  OOoOO = OOoOO
  if 'Arsenal' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'arsenal-logo.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                                  ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Bournemouth' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'afc-bournemouth.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                       ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Burnley' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'KEGnQWW.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                                   ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Chelsea' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'chelsea.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                                  ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Crystal' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'CrystalPalace.0.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                       ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Everton' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'Everton.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                                   ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Hull' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'hull-city-afc.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                                 ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Leicester' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                       ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Liverpool' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'liverpool-logo.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                               ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Manchester City' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'city-logo.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '               ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Manchester United' in OOoOO :
   ooo0O = oOOOo00O00oOo + '91.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '          ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Middlesbrough' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                 ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Southampton' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'southampton-fc-logo.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                   ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Stoke City' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'stoke-city.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                          ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Sunderland' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'sunderland-logo.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                        ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Swansea' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'swansea-city-afc.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                    ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Tottenham' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '        ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Watford' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '                              ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'Bromwich' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '   ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  elif 'West Ham' in OOoOO :
   ooo0O = oOOOo00O00oOo + 'west-ham.png'
   I1111i = '[COLOR' + II + ']' + OOo + ' - ' + OOoOO + '             ' + O0O00 + '        ' + I1iIiiI11 + '        ' + iii11i1 + '        ' + i1ii1111iiI + '        ' + oooOo0OOOoo0 + '        ' + oo0oO + '        ' + iiIIIII + '[/COLOR]'
  iiOOooooO0Oo ( str ( I1111i ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , ooo0O , ooo0O , OOoOO )
  if 40 - 40: o0o00Oo0O + OOoOoo . iIi1i1ii1
def IIiIi ( description ) :
 OOoOO = description
 oO0o0 = ( 'http://www.fullmatchesandshows.com/?s=' + OOoOO ) . replace ( ' ' , '%20' )
 I1I1IIiiI1 ( oO0o0 )
 if 79 - 79: iIi1i1ii1
def iII1i1 ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oO0o0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + o00O0O , O0o0Oo , '' )
  if 34 - 34: oO0o / ii - oo0oO00 / oo0oO00 * oOo0O0Ooo
def o0o000OOOO ( url ) :
 I1 = O000oo ( url )
 ooo0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for ooo0 in ooo0 :
  i1i11ii1 = re . compile ( '(.*?)</h2>' ) . findall ( str ( ooo0 ) )
  for o0iiii1ii in i1i11ii1 :
   o0iiii1ii = o0iiii1ii
  Ii1iii11I = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( ooo0 ) )
  for Ii11iIiiI , o00O0O , time , iiII in Ii1iii11I :
   iiI1iii = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( iiII )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + o0iiii1ii + ' - ' + Ii11iIiiI + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + o00O0O , O0o0Oo , ( str ( iiI1iii ) ) )
   if 30 - 30: IIiIi1iI
 I1I11i ( 'tvshows' , 'Media Info 3' )
 if 57 - 57: I11i * Ii / OOooOOo
def iii1IiII ( ) :
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
 if 65 - 65: IIiIi1iI % o0o00Oo0O
def IiiII1I ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  IiIii = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   IiIii = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   O0OoO0ooOO0o ( '[COLOR' + II + ']' + IiIii + '[/COLOR]' , url , 10013 , o00O0O )
 for url , o00O0O , I1111i in i1I :
  IiIii = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   O0OoO0ooOO0o ( '[COLOR' + II + ']' + IiIii + '[/COLOR]' , url , 10013 , o00O0O )
def I1I1IIiiI1 ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 57 - 57: IIi . iIi1i1ii1 % I11i
 if 32 - 32: iiII11i1I1IIi / OOoOoo - o0o00Oo0O * iI11I1II1I1I
 if 70 - 70: ii % ii % oO0o
 if 98 - 98: oO0o
 if 18 - 18: iiII11i1I1IIi + I1ii11iIi11i - oO0o / O00OOo00oo0o / IIi
 if 53 - 53: IIi + I11i . oo0oO00 / iiII11i1I1IIi
 if 52 - 52: O00OOo00oo0o + O00OOo00oo0o
 for url , o00O0O , I1111i in i1I :
  IiIii = I1111i . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in I1111i :
   pass
  else :
   O0OoO0ooOO0o ( '[COLOR' + II + ']' + IiIii + '[/COLOR]' , url , 10013 , o00O0O )
   if 73 - 73: I11i . Ii % ii + IIiIi1iI . ii / IIi
def oOiiI1i11I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for ii1iIi1II in IIIII11I1IiI :
  IiIIii = ( ii1iIi1II ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  OOOOo0o00OO0000 ( 'http:' + IiIIii )
  if 74 - 74: iI11I1II1I1I / iIi1i1ii1
  if 59 - 59: iIi1i1ii1 / IIiIiII11i - OOoOoo % OOooOOo % ii
  if 79 - 79: OooOO000 . ii . oOo0O0Ooo * o0o00Oo0O * oO0o - IIi
  if 33 - 33: Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
def O00000OO00OO ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  O0OoO0ooOO0o ( I1111i , url , 8046 , o00O0O )
 for url in i1I :
  IiIi1iIIi1 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def iI11iI ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  OOOOo0o00OO0000 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 100 - 100: ii + Ii % I11i + oOo0O0Ooo . I1ii11iIi11i . IIiIiII11i
def OoiiI11111II ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 48 - 48: OooOO000 % Ii . ii * OOoOoo % oO0o . OooOO000
def oOoO00o ( ) :
 IiIi1iIIi1 ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 IiIi1iIIi1 ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 IiIi1iIIi1 ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 iIIII = iIi11i1 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , oO0o0 , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiOOo0 ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + o00O0O )
 for url in next :
  IiIi1iIIi1 ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 85 - 85: O00OOo00oo0o % Ii1I
  if 95 - 95: oO0o * IIi * OooOO000 . I11i
def oooOo00 ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   O0OoO0ooOO0o ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   IiIi1iIIi1 ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def iII1II ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 10012 , '' )
  if 12 - 12: iiII11i1I1IIi
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def I11iIi1i1I1i1 ( name , url ) :
 iiiiii1ii1 = 0
 name = name
 url = url
 i1Oo0oO00o = [ '144' , '240' , '380' , '480' , '720' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OOOOo0o00OO0000 ( url )
  if 27 - 27: oOo0O0Ooo - oO0o - oo0oO00
  if 84 - 84: OooOO000
  if 39 - 39: iiII11i1I1IIi / OooOO000 + ooOoO0O00 % IIi
  if 51 - 51: o0o00Oo0O % IIiIiII11i % Ii + IIi . ii
  if 14 - 14: I1ii11iIi11i + Ii - oo0oO00 % OOoOoo
  if 1 - 1: oo0oO00 + O00OOo00oo0o . oOo0O0Ooo
  if 47 - 47: OooOO000 . OOooOOo
  if 58 - 58: OooOO000 + I1ii11iIi11i / oOo0O0Ooo
def o000OO00OoO00 ( ) :
 iIIII = iIi11i1 ( 'http://documentarylovers.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  if 'genre' in oO0o0 :
   IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oO0o0 , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00o ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( iIIII )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , o00O0O )
 for url in next :
  IiIi1iIIi1 ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 34 - 34: oOo0O0Ooo * OooOO000 % ii + iI11I1II1I1I . oOo0O0Ooo * o0o00Oo0O
def ii1oOO0000 ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( iIIII )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  O0OoO0ooOO0o ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in i1I :
  iII1II ( url )
  if 84 - 84: o0o00Oo0O % iIi1i1ii1 . iIi1i1ii1 . OooOO000 * iiII11i1I1IIi
def iI ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1111O0O000OOOo = 'http://documentarylovers.com/?s=' + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 iIi = i1111O0O000OOOo . lower ( )
 O00o ( iIi )
 if 75 - 75: oo0oO00 / I1ii11iIi11i % OooOO000 + oo0oO00
def OoooOOOOo ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if 'films' in url :
   IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def I1i1Ii1i11ii ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( iIIII )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  if 'films' in url :
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + o00O0O )
 for url in i1I :
  IiIi1iIIi1 ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def oO0O0oo ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  if 'rtd' in url :
   OOOOOOO00OO ( url )
   if 68 - 68: oOo0O0Ooo
def OOOOOOO00OO ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( iIIII )
 for i1Oo00 , file in IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1Oo00 + file )
  OOOOo0o00OO0000 ( url )
  if 94 - 94: OooOO000 / OOooOOo % IIiIiII11i . iI11I1II1I1I
  if 49 - 49: IIi * oOo0O0Ooo / IIiIiII11i
def OOoo ( ) :
 I1 = iIi11i1 ( 'http://www.stream2watch.co/live-tv' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , o00O0O , I1111i , Oo0ooo in IIIII11I1IiI :
  IiIi1iIIi1 ( ( I1111i + '[COLOR' + II + ']' + Oo0ooo + '[/COLOR]' ) , oO0o0 , 8086 , o00O0O )
  if 73 - 73: IIiIiII11i + IIi * OooOO000 / OooOO000
def OoOo0O0 ( url ) :
 I1 = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8087 , o00O0O )
  if 39 - 39: O00OOo00oo0o . oO0o % IIiIi1iI . IIi / OooOO000 * oO0o
def iiI1i ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  o0O00o0 ( url , I1111i )
  if 61 - 61: IIiIiII11i % Ii + iI11I1II1I1I + Ii1I / oOo0O0Ooo * ooOoO0O00
def o0O00o0 ( url , name ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  print url
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 2 - 2: IIiIiII11i . iiII11i1I1IIi
def OoO0oOOOO ( ) :
 iIIII = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oO0o0 , 3002 , 'http://www.solie.org/alibrary/' + o00O0O )
def o0oo00OOOo ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def oo0oOi1i1IIi ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 o0oo0Ooo0 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( iIIII )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , I1111i in o0oo0Ooo0 :
  IiIi1iIIi1 ( '[COLOR' + II + ']Season- ' + I1111i + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  IiIi1iIIi1 ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , o00O0O , I1111i in i1I :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + o00O0O )
def o0OOoO ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  I1iII1II1I1ii ( url )
def I1iII1II1I1ii ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
  if 54 - 54: ii + I1ii11iIi11i * IIi
def OOOOO0O00 ( ) :
 iIIII = iIi11i1 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oO0o0 , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def oOoO0O00o ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  ooo0O0OO ( url )
  if 25 - 25: o0o00Oo0O + iiII11i1I1IIi + IIi * Ii1I
def IiIiIi ( ) :
 iIIII = iIi11i1 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oO0o0 , 8065 , oOOOo00O00oOo + 'classictv.png' )
def OO0Iii1iIiI111Ii ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  if 'mp4' in url :
   OOOOo0o00OO0000 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 61 - 61: ii * OOooOOo
def o0OoOo0o0OOoO0 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oO0o0 , 8071 , oOOOo00O00oOo + 'streams.png' )
def i1I1IIIiii1 ( url ) :
 I1 = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for I1111i , url in IIIII11I1IiI :
  if '(Free Access)' in I1111i :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def oOO0 ( url ) :
 I1 = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for o00O0O , I1111i , url in IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , o00O0O , o0ooooO0o0O , '' )
  if 80 - 80: oo0oO00 . o0o00Oo0O
def oooO ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  OO0oooOO ( 'http://watchxxxfree.com/categories' )
 if i11I1II1I11i == 1 :
  III ( 'http://www.perfectgirls.net' )
 if i11I1II1I11i == 2 :
  i1iiIIiiiI ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 3 :
  I1IIiIi1iI ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 4 :
  i1iiIIiiiI ( 'http://www.xvideos.com/best' )
 if i11I1II1I11i == 5 :
  i1iiIIiiiI ( 'http://www.xvideos.com/verified/videos' )
 if i11I1II1I11i == 6 :
  oOo0Iiii11 ( 'http://www.xvideos.com/tags' )
 if i11I1II1I11i == 7 :
  o00000O ( 'http://www.xvideos.com/porn' )
 if i11I1II1I11i == 8 :
  iIiiiII11 ( )
  if 98 - 98: Ii1I
  if 25 - 25: IIi % IIi
  if 25 - 25: Ii + Ii1I - ii . o0o00Oo0O % O00OOo00oo0o
  if 53 - 53: ooOoO0O00
  if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
  if 9 - 9: ooOoO0O00 - OOooOOo
  if 57 - 57: iI11I1II1I1I * iIi1i1ii1 * OooOO000 / oo0oO00
  if 46 - 46: iIi1i1ii1
  if 61 - 61: I11i / IIiIi1iI - IIiIiII11i
def oOoO0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  if 'ch' in url :
   i1II ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def o0Ooo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 iIIIi11iIiIii = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for I1111i , url in iIIIi11iIiIii :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def Oo0Oo00O00o0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   IiII1 ( url )
def iI1I1I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def OO0oooOO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i , i1i1ii1111i1i in IIIII11I1IiI :
  if 'category' in url :
   i1II ( '[COLOR' + II + ']' + I1111i + '[COLORorange]   ' + i1i1ii1111i1i + '[/COLOR]' , url , 90006 , o00O0O , oOOOo00O00oOo + 'Jizbox.png' , '' )
def Oo0o0oOo0oO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 iIIIi11iIiIii = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , o00O0O , '' , '' )
 for url in iIIIi11iIiIii :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def i1iiiI1I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   IiII1 ( url )
def IiII1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( url )
def III ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , i1i1ii1111i1i in IIIII11I1IiI :
  if 'category' in url :
   i1II ( '[COLOR' + II + ']' + I1111i + '[COLORorange]' + i1i1ii1111i1i + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def o00OoOOoO ( url ) :
 I1 = O000oo ( url )
 IiIIIIIi = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 iIIIi11iIiIii = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , o00O0O , '' , '' )
 for url in iIIIi11iIiIii :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , IiIIIIIi + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def iii1i1Iiiiiii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOoo0 ( 'http://www.perfectgirls.net' + url )
def OOoo0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( 'http://' + url )
def o00000O ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , I1111i , i1i1ii1111i1i in IIIII11I1IiI :
  i1II ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + i1i1ii1111i1i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def oOo0Iiii11 ( url ) :
 I1 = O000oo ( url )
 iIIIi11iIiIii = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in iIIIi11iIiIii :
  i1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , I1111i , i1i1ii1111i1i in IIIII11I1IiI :
  i1II ( ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - No of Videos : [COLORorange]' + ( i1i1ii1111i1i + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 7 - 7: oOo0O0Ooo % O00OOo00oo0o * OOoOoo + OOooOOo / OOooOOo
def Ii1iiIIIiI ( url ) :
 I1 = O000oo ( url )
 iIIIi11iIiIii = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in iIIIi11iIiIii :
  i1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i , OooOo in IIIII11I1IiI :
  i1II ( I1111i + '--' + ( OooOo ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( o00O0O ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 92 - 92: oO0o . I11i . iIi1i1ii1 % OOooOOo
  if 58 - 58: Ii1I % iIi1i1ii1 * iIi1i1ii1 - OooOO000
def i1iiIIiiiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for o00O0O , url , I1111i , I1III111i , I111IiI11 in IIIII11I1IiI :
  i1II ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + I111IiI11 + ' - [COLORred]' + I1III111i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , o00O0O , o00O0O , I111IiI11 + ' - ' + I1III111i )
 oOO00OoOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in oOO00OoOo :
  i1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 83 - 83: ooOoO0O00
def I1IIiIi1iI ( url ) :
 I1 = O000oo ( url )
 ooo0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 iIIIi11iIiIii = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in iIIIi11iIiIii :
  i1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( ooo0 ) )
 for url , I1111i in IIIII11I1IiI :
  if '/c/' in url :
   i1II ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 43 - 43: IIi / oOo0O0Ooo
   if 46 - 46: Ii1I % OOoOoo + ii * iIi1i1ii1
def iIiiiII11 ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIO0oooooO = ( i1111IIiii1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 iIi = iIO0oooooO . lower ( )
 II1iI111iiIIiI1I = 'http://www.xvideos.com/?k=' + iIi
 print II1iI111iiIIiI1I + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O000oo ( II1iI111iiIIiI1I )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for o00O0O , oO0o0 , I1111i , I1III111i , I111IiI11 in IIIII11I1IiI :
  i1II ( '[COLOR' + II + ']' + I1111i + '[COLORgreen] - Porn Quality : [COLORorange]' + I111IiI11 + ' - [COLORred]' + I1III111i + '[/COLOR]' , 'http://www.xvideos.com' + oO0o0 , 10108 , o00O0O , o00O0O , I111IiI11 + ' - ' + I1III111i )
 oOO00OoOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for oO0o0 in oOO00OoOo :
  i1II ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oO0o0 , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
if 28 - 28: I1ii11iIi11i / OOoOoo . OooOO000 + oO0o + iiII11i1I1IIi % I1ii11iIi11i
if 45 - 45: I1ii11iIi11i / o0o00Oo0O % ii
if 92 - 92: iIi1i1ii1 . OOooOOo . iiII11i1I1IIi - ii / IIiIi1iI
if 80 - 80: iI11I1II1I1I / Ii + OooOO000
if 41 - 41: O00OOo00oo0o + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
if 25 - 25: ii . iIi1i1ii1 % OooOO000 . OOoOoo
if 67 - 67: ii + O00OOo00oo0o / IIiIi1iI
if 75 - 75: OOoOoo / ii . oOo0O0Ooo + O00OOo00oo0o - IIiIiII11i
if 33 - 33: OOoOoo / OOoOoo . Ii * Ii1I + I11i
if 16 - 16: OOoOoo
if 10 - 10: OOooOOo . OOoOoo * iI11I1II1I1I - oo0oO00 - OOooOOo / O00OOo00oo0o
if 13 - 13: oo0oO00 + OOooOOo % OOoOoo % ii
if 22 - 22: O00OOo00oo0o
if 23 - 23: o0o00Oo0O
if 41 - 41: ooOoO0O00 . IIi / IIiIi1iI / I11i % OOoOoo - iIi1i1ii1
if 14 - 14: Ii1I - Ii * O00OOo00oo0o
if 39 - 39: ii
if 19 - 19: Ii
if 80 - 80: oOo0O0Ooo
if 58 - 58: oo0oO00 + Ii1I % OOooOOo
if 22 - 22: iI11I1II1I1I - iIi1i1ii1 / oOo0O0Ooo * OOoOoo
if 26 - 26: I11i + IIi - I11i + I1ii11iIi11i . oo0oO00
if 97 - 97: ooOoO0O00
if 46 - 46: Ii1I
if 30 - 30: oO0o / o0o00Oo0O * I11i * O00OOo00oo0o + ii * OooOO000
if 23 - 23: iiII11i1I1IIi
if 36 - 36: OOoOoo . OooOO000 - ooOoO0O00 + O00OOo00oo0o
if 54 - 54: ii . oo0oO00 - OooOO000
if 76 - 76: O00OOo00oo0o
if 61 - 61: IIiIi1iI / IIiIiII11i * IIiIi1iI * OOooOOo * O00OOo00oo0o . Ii
if 26 - 26: O00OOo00oo0o / IIiIi1iI - oO0o . iI11I1II1I1I
if 83 - 83: IIiIi1iI % iIi1i1ii1 / I1ii11iIi11i - OooOO000 / o0o00Oo0O
if 97 - 97: iI11I1II1I1I * iiII11i1I1IIi
if 95 - 95: oO0o
def OoiIIii1Ii1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( I1 )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( I1 )
 ooOoO00 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'http' in url :
   O0OoO0ooOO0o ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   O0OoO0ooOO0o ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in ooOoO00 :
  if 'http' in url :
   O0OoO0ooOO0o ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
   if 92 - 92: IIiIi1iI / OOoOoo + iI11I1II1I1I
def I111ii1III1I ( url ) :
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 if 84 - 84: oo0oO00 + IIiIiII11i * IIiIiII11i % I11i / OooOO000 + IIiIi1iI
 if 9 - 9: OooOO000
def iIi11I1II ( ) :
 if 93 - 93: Ii1I - IIiIi1iI % Ii1I
 if 12 - 12: IIi + oO0o * iiII11i1I1IIi + iIi1i1ii1 + OOoOoo
 if 58 - 58: OooOO000 * iIi1i1ii1 - Ii % Ii1I
 if 3 - 3: O00OOo00oo0o . iiII11i1I1IIi % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * oO0o
 if 5 - 5: IIiIiII11i * ooOoO0O00 % iIi1i1ii1
 if 55 - 55: oOo0O0Ooo + OooOO000
 if 85 - 85: oo0oO00 + OooOO000 % OooOO000 / iiII11i1I1IIi . oOo0O0Ooo - OOooOOo
 if 19 - 19: iiII11i1I1IIi / OooOO000 + OOoOoo
 if 76 - 76: iI11I1II1I1I / O00OOo00oo0o - Ii1I % I11i % IIi + ii
 if 10 - 10: oO0o * iiII11i1I1IIi / I1ii11iIi11i - O00OOo00oo0o
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 8091 , oOOOo00O00oOo + 'gofish.png' )
def I1iIi1IiI1i ( url ) :
 I1 = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  IiIi1iIIi1 ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def IiiIiiiiI1III ( url ) :
 I1 = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 II111111 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for o00O0O in II111111 :
  o00O0O = o00O0O
 for url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 8092 , o00O0O )
 for url in next :
  IiIi1iIIi1 ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 27 - 27: O00OOo00oo0o * I1ii11iIi11i / IIiIi1iI
def IiIi11IIi1I11 ( url ) :
 I1 = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 65 - 65: OOooOOo * o0o00Oo0O - OOooOOo - oO0o
  if 96 - 96: Ii1I - o0o00Oo0O
  if 35 - 35: IIi . iiII11i1I1IIi . O00OOo00oo0o - iiII11i1I1IIi % iiII11i1I1IIi + O00OOo00oo0o
  if 99 - 99: I11i + IIi
I1iI1iiI1Ii1 = '{PQ},' ; O0oO0ooOOo = '{SC},' ; I1II1iIi = '{XG},' ; IIiIi1II1IiI = '{JP},' ; oo0OoO = '{HW},' ; I11iIiiI = '{RT},'
def iiIII1i ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 OO000oo0o = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 oO0o0 = 'http://onlinemovies.tube/?s=' + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 if 4 - 4: O00OOo00oo0o * oOo0O0Ooo % oOo0O0Ooo / ii
 O0Oooo = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 if 52 - 52: oo0oO00 + O00OOo00oo0o * O00OOo00oo0o * I1ii11iIi11i - iI11I1II1I1I + Ii1I
 i1iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 I1111iIIiIIII = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOo0Oii = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + i1111IIiii1
 O0000 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 ooO0OO0Oooo0o = ( i11 ( 'aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9tb3ZpZXNlYXJjaC5waHA=' ) )
 OOoO00o000 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 if 8 - 8: oo0oO00 / Ii
 if 93 - 93: O00OOo00oo0o % Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = OOoOO0oo0ooO ( oO0o0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 25 - 25: IIiIi1iI % OooOO000 * OooOO000 + iI11I1II1I1I . ooOoO0O00
 if 67 - 67: Ii1I + oo0oO00 * OOoOoo / IIiIiII11i % oO0o % oO0o
 Iiii = OOoOO0oo0ooO ( O0Oooo )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 if 28 - 28: OOooOOo % oo0oO00 - IIi + IIi + oo0oO00 / iI11I1II1I1I
 if 91 - 91: oOo0O0Ooo / IIiIiII11i * IIi
 ooOoo000 = OOoOO0oo0ooO ( i1iI )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 o0Oii11iIIiIi1 = OOoOO0oo0ooO ( oOo0Oii )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 ooO0IIiIIiiiiiII1 = OOoOO0oo0ooO ( O0000 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 iIi1i1II = OOoOO0oo0ooO ( ooO0OO0Oooo0o )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 oOoooOO00ooOO = OOoOO0oo0ooO ( OOoO00o000 )
 if 8 - 8: O00OOo00oo0o * IIiIiII11i - oO0o - iiII11i1I1IIi
 if 69 - 69: IIiIi1iI + O00OOo00oo0o + I11i . I1ii11iIi11i
 if 15 - 15: IIiIi1iI / OOoOoo * Ii + OooOO000
 if 15 - 15: I11i % oO0o / OooOO000
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( I1 )
  next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( I1 )
  for oO0o0 , o00O0O , I1111i , IIIiiiI in IIIII11I1IiI :
   if i1111IIiii1 in I1111i . lower ( ) :
    if 'movies' in IIIiiiI :
     IiIi1iIIi1 ( '[COLORred]*[COLOR' + II + ']' + IIIiiiI + '-' + I1111i + '-[COLORred] source MOVIE HUB[/COLOR]' , oO0o0 , 90044 , o00O0O )
  for oO0o0 in next :
   oO0oooooo ( oO0o0 )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 0 , "" , "Getting Source MOVIE HUB" )
   if 36 - 36: oO0o + oO0o % I1ii11iIi11i + I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
   if 20 - 20: IIi * oo0oO00
   if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . IIi
   if 31 - 31: oo0oO00 % ooOoO0O00 . ii - I11i + ii
   if 45 - 45: IIi + iiII11i1I1IIi / ii - iIi1i1ii1 + ii
   if 42 - 42: iI11I1II1I1I * oOo0O0Ooo * O00OOo00oo0o
   if 62 - 62: IIi * o0o00Oo0O % OOoOoo . OOoOoo . oOo0O0Ooo
 if Iiii != 'Failed' :
  ooOoO00 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for oo0 , I1111i in ooOoO00 :
   if i1111IIiii1 in I1111i . lower ( ) :
    IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( O0Oooo + oo0 ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
    if 37 - 37: OooOO000 - iiII11i1I1IIi + iI11I1II1I1I / O00OOo00oo0o - oO0o . I11i
    if 62 - 62: Ii1I
    if 47 - 47: O00OOo00oo0o % IIi * oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
    if 2 - 2: O00OOo00oo0o % ii - IIiIi1iI * Ii1I * OOoOoo
    if 99 - 99: iI11I1II1I1I . I1ii11iIi11i / IIiIi1iI . IIi % oOo0O0Ooo * iiII11i1I1IIi
    if 95 - 95: oo0oO00
    if 80 - 80: OOoOoo
    if 42 - 42: ii * IIiIiII11i
    if 53 - 53: O00OOo00oo0o + ooOoO0O00 . oO0o / Ii + iIi1i1ii1 % OOooOOo
 if ooOoo000 != 'Failed' :
  I1Io0Oo00 = [ ]
  O0O0o0o0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooOoo000 )
  for oO0o0 , I1ii1ii11i1I , iII1iii , o0iiiI1I1iIIIi1 , I1111i in O0O0o0o0o :
   if i1111IIiii1 in I1111i . lower ( ) :
    if I1111i in I1Io0Oo00 :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oO0o0 , 1016 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii )
     I1Io0Oo00 . append ( I1111i )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if o0Oii11iIIiIi1 != 'Failed' :
  I1II11IIi11i = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( o0Oii11iIIiIi1 )
  for oO0o0 , o00O0O , I1111i in I1II11IIi11i :
   if i1111IIiii1 in I1111i . lower ( ) :
    IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oO0o0 , 7067 , o00O0O )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 67 - 67: iI11I1II1I1I - OooOO000
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 81 - 81: o0o00Oo0O
    if 38 - 38: OooOO000
    if 78 - 78: Ii . OOoOoo % ii - OOoOoo - OOoOoo + iIi1i1ii1
    if 11 - 11: iiII11i1I1IIi
    if 20 - 20: o0o00Oo0O . Ii * ooOoO0O00 % o0o00Oo0O . oOo0O0Ooo
    if 53 - 53: IIiIi1iI / ii - IIiIiII11i
    if 68 - 68: ii . ii . iI11I1II1I1I / IIiIi1iI - iiII11i1I1IIi % o0o00Oo0O
    if 19 - 19: ii * oo0oO00
    if 60 - 60: IIiIiII11i - OooOO000 + I11i % IIi
 if iIi1i1II != 'Failed' :
  oooO0O0o00o = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( iIi1i1II )
  for I1111i , oO0o0 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii in oooO0O0o00o :
   if i1111IIiii1 in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Reaper[/COLOR]' ) , oO0o0 , 222 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 75 - 75: Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oOoooOO00ooOO != 'Failed' :
  o0oo0O0OO0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOoooOO00ooOO )
  for oO0o0 , I1ii1ii11i1I , iII1iii , o0iiiI1I1iIIIi1 , I1111i in o0oo0O0OO0 :
   if i1111IIiii1 in I1111i . lower ( ) :
    OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source APPRENTICE[/COLOR]' ) , oO0o0 , 222 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 32 - 32: Ii1I / I1ii11iIi11i . OOooOOo + OooOO000 * OOooOOo * OOoOoo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 46 - 46: iIi1i1ii1
    if 42 - 42: iI11I1II1I1I
    if 32 - 32: I1ii11iIi11i - iIi1i1ii1 . ii - ii - I1ii11iIi11i . iI11I1II1I1I
    if 34 - 34: I1ii11iIi11i
    if 31 - 31: ooOoO0O00 - iiII11i1I1IIi + O00OOo00oo0o + IIiIi1iI . IIiIi1iI . o0o00Oo0O
    if 33 - 33: ooOoO0O00 / OooOO000 * oO0o
    if 2 - 2: oo0oO00 . IIi
    if 43 - 43: iI11I1II1I1I
    if 29 - 29: OOoOoo % IIiIi1iI + oO0o . ooOoO0O00 + oOo0O0Ooo
    if 24 - 24: O00OOo00oo0o / iIi1i1ii1 * Ii1I - ii / oOo0O0Ooo . oo0oO00
 iiI1ii1Iii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 98 - 98: ooOoO0O00 - OooOO000
 for OOOoO in iiI1ii1Iii :
  oOooo = OOOO0OOoO0O0 + OOOoO + IIiiiiiiIi1I1
  iIIiII11iI1 = OOoOO0oo0ooO ( oOooo )
  if iIIiII11iI1 != 'Failed' :
   o0oI1Iii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIiII11iI1 )
   for oO0o0 , I1ii1ii11i1I , iII1iii , o0iiiI1I1iIIIi1 , I1111i in o0oI1Iii :
    if i1111IIiii1 in I1111i . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , oO0o0 , 222 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 33 - 33: I11i - oo0oO00 % Ii1I * iiII11i1I1IIi . ii % iIi1i1ii1
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 29 - 29: OooOO000 + IIiIiII11i . Ii . iIi1i1ii1 - o0o00Oo0O
 iiI1ii1Iii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 47 - 47: oo0oO00 . Ii1I - iI11I1II1I1I % IIiIiII11i / OOooOOo % ii
 if 13 - 13: OOoOoo . I1ii11iIi11i - iiII11i1I1IIi / oo0oO00 - I1ii11iIi11i - oOo0O0Ooo
 for OOOoO in iiI1ii1Iii :
  oOooo = OO000oo0o + OOOoO
  oOO0ooo = OOoOO0oo0ooO ( oOooo )
  if oOO0ooo != 'Failed' :
   Ii11II1IIIIIi = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oOO0ooo )
   for oo0 , I1111i in Ii11II1IIIIIi :
    if i1111IIiii1 in I1111i . lower ( ) :
     O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OO000oo0o + OOOoO + oo0 ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 83 - 83: iI11I1II1I1I + IIiIiII11i * oo0oO00 / o0o00Oo0O - OooOO000
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 23 - 23: ooOoO0O00
     if 24 - 24: OOoOoo
def iiiI ( ) :
 if 51 - 51: IIi % Ii
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
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - iIi1i1ii1 * iI11I1II1I1I
 oO0o0 = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllc2dvLnRvL3NlYXJjaC8=' ) ) + ( i1111IIiii1 ) . replace ( ' ' , '%20' )
 ii1oOOO0ooOO = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 IiIIIIIi = 'http://onlinemovies.tube/?s=' + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 O0Oooo = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 OO0ooo0OOO = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 i1iI = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iIi ) . replace ( ' ' , '+' )
 I1111iIIiIIII = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 oOo0Oii = ( i11 ( 'aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9zZXJpYWxzZWFyY2gucGhw' ) )
 O0000 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 69 - 69: O00OOo00oo0o + iI11I1II1I1I * oo0oO00 + OOoOoo % IIiIi1iI - iIi1i1ii1
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 83 - 83: OOoOoo % I11i * I11i
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = OOoOO0oo0ooO ( oO0o0 )
 o0oOoO00o . update ( 7 , "" , "Checking Source 2/9 Links" )
 o0000Oo0 = OOoOO0oo0ooO ( ii1oOOO0ooOO )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = OOoOO0oo0ooO ( IiIIIIIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = OOoOO0oo0ooO ( O0Oooo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = OOoOO0oo0ooO ( OO0ooo0OOO )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 ooOoo000 = cloudflare . source ( i1iI )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOO0ooo = OOoOO0oo0ooO ( I1111iIIiIIII )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 o0Oii11iIIiIi1 = OOoOO0oo0ooO ( oOo0Oii )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 ooO0IIiIIiiiiiII1 = OOoOO0oo0ooO ( O0000 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 38 - 38: OooOO000 - I1ii11iIi11i / iIi1i1ii1 + oo0oO00 . OooOO000 + OOoOoo
 if ooO0IIiIIiiiiiII1 != 'Failed' :
  iIiii1iI1Ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO0IIiIIiiiiiII1 )
  for oO0o0 , I1ii1ii11i1I , iII1iii , o0iiiI1I1iIIIi1 , I1111i in iIiii1iI1Ii :
   if iIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source HeroVision[/COLOR]' ) , oO0o0 , 1016 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 82 - 82: Ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 13 - 13: o0o00Oo0O % IIiIiII11i
 if o0Oii11iIIiIi1 != 'Failed' :
  I1II11IIi11i = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( o0Oii11iIIiIi1 )
  for I1111i , oO0o0 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii in I1II11IIi11i :
   if iIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] source Reaper[/COLOR]' ) , oO0o0 , 90037 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 96 - 96: oO0o + oOo0O0Ooo % I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 21 - 21: OOooOOo - Ii - OOooOOo
    if 4 - 4: iiII11i1I1IIi . OOoOoo
    if 39 - 39: IIi . I1ii11iIi11i - OOooOOo * Ii
    if 4 - 4: OOooOOo * o0o00Oo0O - iiII11i1I1IIi
    if 72 - 72: iiII11i1I1IIi + IIiIi1iI / oOo0O0Ooo . OOoOoo % oO0o / Ii
    if 13 - 13: O00OOo00oo0o % I11i + IIi + O00OOo00oo0o + Ii - Ii1I
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  iiIi1111iiI1 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for oO0o0 , o00O0O , I1111i , i11ii1Ii1 in i1I :
   if iIi in I1111i . lower ( ) :
    if 'season' in i11ii1Ii1 :
     IiIi1iIIi1 ( '[COLORred]*[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90054 , o00O0O , o00O0O , '' )
    if 'episodes' in i11ii1Ii1 :
     IiIi1iIIi1 ( '[COLORred]*[COLOR' + II + ']' + I1111i + ' - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90044 , o00O0O , o00O0O , '' )
  for oO0o0 in iiIi1111iiI1 :
   IiIi1iIIi1 ( '[COLORred]*[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oO0o0 , 90053 , oOOOo00O00oOo + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 85 - 85: iiII11i1I1IIi + O00OOo00oo0o
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if o0000Oo0 != 'Failed' :
  i1III1iI1I = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( o0000Oo0 )
  for oO0o0 , I1111i , o00O0O in i1III1iI1I :
   if iIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oO0o0 , 8022 , o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for o00O0O , oO0o0 , I1111i in IIIII11I1IiI :
   if iIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( I1111i ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - WatchSeries[/COLOR]' , 'http://www.watchseriesgo.to' + oO0o0 , 10044 , 'http://www.watchseriesgo.to/' + o00O0O , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Source WatchSeries Links" )
    if 95 - 95: O00OOo00oo0o + OOoOoo * iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  ooOoO00 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for I1111i in ooOoO00 :
   if iIi in I1111i . lower ( ) :
    IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( O0Oooo + I1111i ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / iIi1i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  Iii1I1111ii = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for I1111i in Iii1I1111ii :
   if iIi in I1111i . lower ( ) :
    IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( OO0ooo0OOO + I1111i ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 19 - 19: ooOoO0O00 - iI11I1II1I1I . iiII11i1I1IIi
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if ooOoo000 != 'Failed' :
  O0O0o0o0o = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( ooOoo000 )
  for oO0o0 , o00O0O , I1111i in O0O0o0o0o :
   if iIi in I1111i . lower ( ) :
    IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + ' -[COLORgold] Source - Dizi[/COLOR]' , oO0o0 , 8062 , o00O0O )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 2 - 2: iIi1i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oOO0ooo != 'Failed' :
  Ii11II1IIIIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOO0ooo )
  for oO0o0 , I1ii1ii11i1I , iII1iii , o0iiiI1I1iIIIi1 , I1111i in Ii11II1IIIIIi :
   if iIi in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '-[COLORgold] Source Scooby[/COLOR]' ) , oO0o0 , 1016 , I1ii1ii11i1I , o0iiiI1I1iIIIi1 , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 12 - 12: Ii - iI11I1II1I1I * OOoOoo * OooOO000
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 19 - 19: o0o00Oo0O + oo0oO00 + I11i
 oO0IIi11IiiiI11i = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for OOOoO in oO0IIi11IiiiI11i :
  oOooo = OOOO0OOoO0O0 + OOOoO + IIiiiiiiIi1I1
  oOoooOO00ooOO = OOoOO0oo0ooO ( oOooo )
  if oOoooOO00ooOO != 'Failed' :
   o0oo0O0OO0 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oOoooOO00ooOO )
   for I1111i , iII1iii , oO0o0 , o00O0O , o0ooooO0o0O , I1iii11 in o0oo0O0OO0 :
    if iIi in I1111i . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - Source Pandoras[/COLOR]' , oO0o0 , I1iii11 , o00O0O , o0ooooO0o0O , iII1iii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 68 - 68: oo0oO00 + iiII11i1I1IIi * oo0oO00 . OOoOoo % iIi1i1ii1 - ii
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 60 - 60: oO0o % Ii
     if 7 - 7: OOoOoo
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def III11i ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO0o0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( i1111IIiii1 ) . replace ( ' ' , '+' )
 if 54 - 54: O00OOo00oo0o / I11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = OOoOO0oo0ooO ( oO0o0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 39 - 39: IIi % oo0oO00 * Ii1I - o0o00Oo0O + oOo0O0Ooo + I11i
 if I1 != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for oO0o0 , I1111i in i1I :
   if i1111IIiii1 in I1111i . lower ( ) :
    O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oO0o0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 64 - 64: IIiIiII11i / IIiIiII11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
o0OOo0OOoOO0 = '{ZH},' ; oo0OOo0Oo00 = '{IX},' ; o0oOOoOoOOo = '{LM},'
if 61 - 61: OooOO000 * IIiIi1iI
def i1I1IiIiiI1II ( url ) :
 iI1ioo000o0O = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iI1ioo000o0O )
 for url , I1Iooooo , iI1i , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( ( I1Iooooo ) . replace ( 'Sezon' , ' Season ' ) + ( iI1i ) . replace ( 'Bölüm' , ' Episode ' ) + I1111i , url , 8063 , '' )
  if 1 - 1: IIiIiII11i - ooOoO0O00 + oo0oO00
  if 58 - 58: OooOO000 - ii
  if 56 - 56: OooOO000 / OooOO000
  if 21 - 21: o0o00Oo0O * IIiIi1iI % OOooOOo / o0o00Oo0O
def ooooooo ( url ) :
 iI1ioo000o0O = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iI1ioo000o0O )
 for url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( I1111i , url , 222 , '' )
  if 58 - 58: ooOoO0O00 + o0o00Oo0O . oO0o % iiII11i1I1IIi
  if 39 - 39: I11i + OOoOoo / iIi1i1ii1 + I11i
  if 33 - 33: OooOO000 - I1ii11iIi11i - iiII11i1I1IIi
  if 61 - 61: iIi1i1ii1 + oOo0O0Ooo / ooOoO0O00 + ooOoO0O00 / oo0oO00
def ii1I1IIII11ii ( ) :
 if 23 - 23: OOooOOo * OOoOoo / oo0oO00
 iI1ioo000o0O = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iI1ioo000o0O )
 for oO0o0 , o00O0O , I1111i , iI1i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i + '  -  ' + ( iI1i ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oO0o0 , 8063 , o00O0O )
  if 60 - 60: IIiIi1iI * iIi1i1ii1 + O00OOo00oo0o . IIi . o0o00Oo0O
def Ii1i1ii ( ) :
 iIIII = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i , o00O0O in IIIII11I1IiI :
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 8002 , o00O0O )
def ooO ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , time , url , I1111i , i1I111Ii in IIIII11I1IiI :
  iiOOooooO0Oo ( '%s %s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , time ) , url , 1015 , o00O0O , i1I111Ii )
  if 79 - 79: ii * O00OOo00oo0o - ooOoO0O00 * ii % o0o00Oo0O % iI11I1II1I1I
def oO0ooo00OoOooooo ( ) :
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . iIi1i1ii1 - I1ii11iIi11i . Ii
 IiIi1iIIi1 ( 'Coronation Street' , '' , 8001 , '' )
 IiIi1iIIi1 ( 'Eastenders' , '' , 8002 , '' )
 IiIi1iIIi1 ( 'Emmerdale' , '' , 8003 , '' )
 IiIi1iIIi1 ( 'Hollyoaks' , '' , 8004 , '' )
 IiIi1iIIi1 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 47 - 47: I1ii11iIi11i % oO0o - IIiIi1iI - I1ii11iIi11i * oo0oO00
 if 72 - 72: I11i % I11i + OooOO000 + Ii1I / I1ii11iIi11i
 if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
 if 64 - 64: OOoOoo
def OooooOOOO ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Holly' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oO0o0 :
    O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 89 - 89: o0o00Oo0O + OOoOoo * O00OOo00oo0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 30 - 30: OOooOOo
def IIIII11 ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'East' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oO0o0 :
    O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 48 - 48: O00OOo00oo0o / IIiIi1iI . iI11I1II1I1I
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 72 - 72: ooOoO0O00 . I11i
def iIIiiIiII1i ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Emmer' in I1111i :
   o00O0O = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oO0o0 :
    O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 78 - 78: o0o00Oo0O - O00OOo00oo0o * IIi + iiII11i1I1IIi + IIiIiII11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: I1ii11iIi11i . Ii + IIiIi1iI / Ii1I / OooOO000 + ii
def ooo0oOoO00Oo ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Coro' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oO0o0 :
    O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 46 - 46: IIiIi1iI - IIiIi1iI * Ii1I / OooOO000 * IIi / I11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 67 - 67: IIi - iIi1i1ii1 % OooOO000 / IIiIiII11i + oOo0O0Ooo * IIiIi1iI
def o0o0O0o0O ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Celeb' in I1111i :
   o00O0O = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oO0o0 :
    O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oO0o0 . replace ( '\\/' , '/' ) , 8006 , o00O0O )
   else :
    pass
    if 16 - 16: I11i
def IiiiI1i ( name , url ) :
 I1iIi1i = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if I1iIi1i :
  I1II1iI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  iIIII = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( iIIII ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  iIIII = open_url ( url )
  iIii1Ii11I1i = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( iIIII ) [ - 1 ]
  I1II1iI = iIii1Ii11I1i . replace ( '\\/' , '/' )
 i111iiI1ii = xbmcgui . ListItem ( name , '' , '' )
 i111iiI1ii . setPath ( I1II1iI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i111iiI1ii )
 if 18 - 18: IIiIi1iI
 if 37 - 37: I1ii11iIi11i % Ii - oOo0O0Ooo * Ii1I . IIiIi1iI
def OoO0 ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oO0o0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for oO0o0 , I1111i in i1I :
  IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oO0o0 , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 11 - 11: I11i - IIiIiII11i % oo0oO00 . IIiIiII11i
def OO0I11IIi1I1 ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Movies' in I1111i :
   IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( oO0o0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def Iiiii ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 for url in i1I :
  IiIi1iIIi1 ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + iIi1i1ii1 . IIi
  if 58 - 58: iI11I1II1I1I + O00OOo00oo0o - Ii1I - ooOoO0O00 * OOooOOo
def ooooO0oOoOOoO ( url ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , o00O0O )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
iii1iII1iii = '{UJ},' ; o0O0o = '{WE},' ; OO0o0o = '{WP},' ; O0O0O00OoO0O = '{PP},'
def i1II11III ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url , o00O0O in IIIII11I1IiI :
  if '{{' in I1111i :
   pass
  else :
   IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , o00O0O )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0OO0oo ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  II111IiiIIi ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def II111IiiIIi ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 66 - 66: ooOoO0O00
 if 91 - 91: I11i / Ii
 if 96 - 96: oO0o + OooOO000 * IIiIiII11i
def OO00OoO ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '(cooltvseries.com)' in I1111i :
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , I1111i in i1I :
  if '(cooltvseries.com)' in I1111i :
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def IIii ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  OOOOo0o00OO0000 ( ( url ) . replace ( ' ' , '%20' ) )
IiIi1iI1 = '{XX},' ; iiI1I1iii1 = '{UD},' ; Ii111ii1 = '{YT},' ; OoOo00Oo0oo0O = '{JS},' ; i11I111iII1i1 = '{PF},'
if 76 - 76: I1ii11iIi11i + iI11I1II1I1I % I11i
def oO00 ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i , o00O0O in IIIII11I1IiI :
  O0OoO0ooOO0o ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oO0o0 ) ) , 222 , o00O0O )
  if 7 - 7: IIi / OOooOOo * I1ii11iIi11i % ii - OOooOOo . Ii
def IiiI1iiI1III1i ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  if 'youtu' in url :
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + o00O0O )
 for url in next :
  IiIi1iIIi1 ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 36 - 36: oo0oO00 * OooOO000 + OOoOoo * OooOO000 . Ii1I - iI11I1II1I1I
def i1IIi1ii1i1ii ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 97 - 97: IIiIiII11i
def iIiIii ( url ) :
 iIIII = O000oo
 IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 222 , o00O0O )
  if 30 - 30: IIiIi1iI
  if 33 - 33: O00OOo00oo0o * OOoOoo - o0o00Oo0O + oOo0O0Ooo / OOoOoo
  if 19 - 19: ooOoO0O00 % IIiIiII11i
  if 85 - 85: OOoOoo - I11i % IIi - IIiIiII11i
  if 56 - 56: iIi1i1ii1 * Ii
def oooo0OoOO ( ) :
 if 37 - 37: Ii1I / iIi1i1ii1 - ii . oo0oO00
 IiIi1iIIi1 ( 'All Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Entertainment' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Movies' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Music' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'News' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Sports' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Documentary' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Kids' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Food' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Religious' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'USA Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 IiIi1iIIi1 ( 'Other' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 if 57 - 57: Ii - iiII11i1I1IIi / IIiIi1iI / I11i * Ii * I11i
 if 28 - 28: ii % o0o00Oo0O - IIi / I11i / oOo0O0Ooo
def Iii1iIII1Iii ( Cat_Name ) :
 if 13 - 13: iI11I1II1I1I - IIi
 i111ii1II11ii = False
 i11iII1IiI = '0'
 if Cat_Name == 'All Channels' : i111ii1II11ii = True
 if Cat_Name == 'Entertainment' : i11iII1IiI = '1'
 if Cat_Name == 'Movies' : i11iII1IiI = '2'
 if Cat_Name == 'Music' : i11iII1IiI = '3'
 if Cat_Name == 'News' : i11iII1IiI = '4'
 if Cat_Name == 'Sports' : i11iII1IiI = '5'
 if Cat_Name == 'Documentary' : i11iII1IiI = '6'
 if Cat_Name == 'Kids' : i11iII1IiI = '7'
 if Cat_Name == 'Food' : i11iII1IiI = '8'
 if Cat_Name == 'Religious' : i11iII1IiI = '9'
 if Cat_Name == 'USA Channels' : i11iII1IiI = '10'
 if Cat_Name == 'Other' : i11iII1IiI = '11'
 if 21 - 21: OOoOoo * OOooOOo - O00OOo00oo0o
 iIIII = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( iIIII )
 print 'Len Match: >>>' + str ( len ( IIIII11I1IiI ) )
 for I1111i , o00O0O , ii111Ii in IIIII11I1IiI :
  ii1I1 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  if ii111Ii == i11iII1IiI :
   IiIi1iIIi1 ( I1111i , '' , 7022 , ii1I1 )
  elif i111ii1II11ii == True :
   IiIi1iIIi1 ( I1111i , '' , 7022 , ii1I1 )
  else : pass
  if 7 - 7: ooOoO0O00 / OOoOoo / OooOO000
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 97 - 97: oO0o + iI11I1II1I1I
def O0OOoo ( Search_Name ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( iIIII )
 for o00O0O , oO0o0 , IiIIIIIi , O0Oooo in IIIII11I1IiI :
  ii1I1 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( o00O0O ) . replace ( '\\' , '' )
  O0OoO0ooOO0o ( Search_Name + ': Link 1' , ( oO0o0 ) . replace ( '\\' , '' ) , 222 , ii1I1 )
  O0OoO0ooOO0o ( Search_Name + ': Link 2' , ( IiIIIIIi ) . replace ( '\\' , '' ) , 222 , ii1I1 )
  O0OoO0ooOO0o ( Search_Name + ': Link 3' , ( O0Oooo ) . replace ( '\\' , '' ) , 222 , ii1I1 )
  if 38 - 38: OOoOoo . I11i
def i1Ii111 ( ) :
 iIIII = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  O0OoO0ooOO0o ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def OO0o0o0OOoooo ( ) :
 iIIII = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  O0OoO0ooOO0o ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def oOO00OOOO0o ( ) :
 iIIII = O000oo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( iIIII )
 for I1111i , oO0o0 in IIIII11I1IiI :
  O0OoO0ooOO0o ( I1111i , ( oO0o0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 86 - 86: I11i % oO0o + Ii1I
def oo0oO0o00Oo0 ( url ) :
 url
 i11I = xbmcgui . ListItem ( I1111i , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i11I )
 return
 if 22 - 22: IIiIiII11i
 if 92 - 92: oo0oO00 * OOoOoo * o0o00Oo0O
def OoOOOoo ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( iIIII )
 for url , iII1iii , o00O0O , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + o00O0O , '' , ( iII1iii ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  IiIi1iIIi1 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 76 - 76: OOooOOo * iIi1i1ii1 * iI11I1II1I1I * ooOoO0O00 - Ii1I
def I1Ii11I1i1iii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , iII1iii , o00O0O in IIIII11I1IiI :
  OOiIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + o00O0O , '' , iII1iii )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 O0OooOooO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for ooOOo in O0OooOooO :
  o000O0O = ( ooOOo ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiOOooooO0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + o00O0O , '' , o000O0O )
  if 73 - 73: iIi1i1ii1 + OooOO000 % IIi + ii * I1ii11iIi11i
def i1Ii ( INFO ) :
 OO0O000 ( 'info for workout' , INFO )
 if 16 - 16: oO0o
 if 44 - 44: iiII11i1I1IIi . OOoOoo % O00OOo00oo0o - IIiIi1iI - Ii1I
 if 34 - 34: Ii1I % ooOoO0O00 - oO0o
def IiI111i ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( ( I1111i ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def IiI1ii1 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def OOO00oo0 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   O0OoO0ooOO0o ( ( I1111i ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def o0ooOooO0o ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  if '=' in I1111i :
   pass
  else :
   O0OoO0ooOO0o ( I1111i , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 50 - 50: iIi1i1ii1 . o0o00Oo0O % oO0o . oo0oO00 + iIi1i1ii1 . OOooOOo
   if 69 - 69: Ii + Ii . Ii - Ii % iIi1i1ii1 / OooOO000
   if 59 - 59: ii
def oOO00O00o00 ( url ) :
 O0OoO0ooOO0o ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , oOOOo00O00oOo + 'bamf.png' , oOOOo00O00oOo + 'bamf.png' )
 O0OoO0ooOO0o ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , oOOOo00O00oOo + 'bamf.png' , oOOOo00O00oOo + 'bamf.png' )
 IiIi1iIIi1 ( '[COLOR' + II + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , oOOOo00O00oOo + 'bamf.png' )
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  if 'mp4' in url :
   pass
  else :
   O0OoO0ooOO0o ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'bamf.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOo0 ( url ) :
 O0OoO0ooOO0o ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 O0OoO0ooOO0o ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 IiIi1iIIi1 ( '[COLOR' + II + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , oOOOo00O00oOo + 'bamf.png' )
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  if 'mp4' in url :
   O0OoO0ooOO0o ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'bamf.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 55 - 55: iIi1i1ii1 - ii
 if 83 - 83: Ii - I1ii11iIi11i
 if 5 - 5: Ii1I . IIiIiII11i . ooOoO0O00
def iIIIIi ( ) :
 iIIII = O000oo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'Daily' in I1111i :
   IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , oO0o0 , 9008 , Oo00OOOOO )
def iiIIOo0Ooo ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  IiIi1iIIi1 ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def II1iII11 ( url ) :
 O0OoO0ooOO0o ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 O0OoO0ooOO0o ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 O0OoO0ooOO0o ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , Oo00OOOOO )
  if 19 - 19: IIiIiII11i
def i1iIIi ( ) :
 iIIII = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if '.m3u' in oO0o0 :
   IiIi1iIIi1 ( ( I1111i ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oO0o0 ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def oo0O0OO0Oooo ( url ) :
 iIIII = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( I1111i ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 7 - 7: IIiIiII11i - Ii1I / iiII11i1I1IIi % ii + ooOoO0O00
def oO00O0 ( ) :
 iIIII = O000oo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  if 'category' in oO0o0 :
   IiIi1iIIi1 ( I1111i , 'http://www.disclose.tv/' + oO0o0 , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 42 - 42: iiII11i1I1IIi + ooOoO0O00 - iIi1i1ii1 / OOoOoo . OooOO000
   if 30 - 30: I1ii11iIi11i + iIi1i1ii1 % Ii * ooOoO0O00 + oOo0O0Ooo % IIi
def IiiIIiiI1I11 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( iIIII )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( iIIII )
 for url , I1111i , o00O0O in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , 'http://www.disclose.tv/' + url , 7011 , o00O0O )
 for url in next :
  IiIi1iIIi1 ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 74 - 74: I11i - IIiIi1iI / oOo0O0Ooo
  if 98 - 98: o0o00Oo0O % Ii % IIi
def I1i1 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  if 'http' in url :
   O0OoO0ooOO0o ( 'video/flv' , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url , I1111i in i1I :
  O0OoO0ooOO0o ( I1111i , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url in ooOoO00 :
  O0OoO0ooOO0o ( 'YT Link' , url , 8043 , oOOOo00O00oOo + 'disclose.png' )
  if 36 - 36: oOo0O0Ooo / I1ii11iIi11i % iI11I1II1I1I / o0o00Oo0O . Ii1I
  if 53 - 53: I11i % ii - oo0oO00 - ooOoO0O00 / oO0o
def i1111II1iIII ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
  if 41 - 41: OOoOoo * ii . IIiIi1iI % Ii
def IiIoO0oo0 ( name , url , img ) :
 I1 = O000oo ( url )
 IiIiI1 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1 )
 iiiI1 = len ( IiIiI1 )
 if 29 - 29: I1ii11iIi11i / OooOO000 + iIi1i1ii1 - oO0o
 if 18 - 18: oo0oO00 * o0o00Oo0O - oOo0O0Ooo + o0o00Oo0O + O00OOo00oo0o
 if iiiI1 == 1 :
  for OOO00OOOO0o in IiIiI1 :
   OOO00OOOO0o = OOO00OOOO0o . replace ( 'player' , 'watch' )
   o0oiIiI1i1iiIi1i = OOO00OOOO0o + '&fv=&sou='
   iI1IiII1II1I = O000oo ( o0oiIiI1i1iiIi1i )
   O0ooO = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( iI1IiII1II1I )
   for o00OO00O0oOO in O0ooO :
    OOo000OOoOO = False
    Resolve ( o00OO00O0oOO )
    if 13 - 13: I1ii11iIi11i
 elif iiiI1 > 1 :
  if 70 - 70: OooOO000
  for OOO00OOOO0o in IiIiI1 :
   OooO00Oo = O000oo ( OOO00OOOO0o )
   oO0OO00O0 = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OooO00Oo )
   O000oOo0OO = oO0OO00O0
   O000oOo0OO = ( str ( O000oOo0OO ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + O000oOo0OO
   O0OoO0ooOO0o ( 'DOUBLE LINK' , O000oOo0OO , 424 , '' )
   if 57 - 57: Ii1I
   for url in oO0OO00O0 :
    IiIi1iIIi1 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     IiIIIIIi = Google . resolve ( url )
    except :
     pass
    try :
     II1111i11i11 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( IiIIIIIi ) )
     for IiIiIiIII1Iii , OOoOOOOOo0ooOOO0 in II1111i11i11 :
      if 91 - 91: Ii + iIi1i1ii1 % iIi1i1ii1 + I11i
      HD_URLS . append ( IiIiIiIII1Iii )
      SD_URLS . append ( OOoOOOOOo0ooOOO0 )
    except :
     pass
 else :
  pass
  if 15 - 15: Ii1I . oOo0O0Ooo - O00OOo00oo0o - ooOoO0O00
def O00OO0o0oO0 ( ) :
 if 85 - 85: OOoOoo * OooOO000
 if 17 - 17: IIi . oo0oO00 - I1ii11iIi11i * iI11I1II1I1I * IIiIi1iI
 IiIi1iIIi1 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 39 - 39: ii . oo0oO00
 IiIi1iIIi1 ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 83 - 83: O00OOo00oo0o . o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - iiII11i1I1IIi
 if 6 - 6: oo0oO00 / Ii1I / oO0o
def iiiiIIii1I ( ) :
 iIIII = O000oo ( 'http://cnfstudio.com/' )
 IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , 'http://cnfstudio.com/genre/' + oO0o0 , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 14 - 14: IIi * oOo0O0Ooo - Ii1I
OOooO0OOoo = xbmcgui . Dialog ( )
if 10 - 10: OooOO000 % O00OOo00oo0o * Ii1I * o0o00Oo0O * Ii % O00OOo00oo0o
ooOoo0O0o0OO0 = '{UN},' ; i11iiIiI11iII = '{IG},' ; oO0OIiIi1ii1Ii = '{PL},' ; i1II111II1 = '{LO},' ; I11I1iiI1 = '{LP},' ; II1IiI11I1 = '{HA},' ; oooo00o0O0 = '{XD},' ; II1I1iI1i1IiI = '{TA},' ; IIiiOoO000Ooo = '{DP},' ; OOiIiI1iI = '{JT},' ; ooo0oooO = '{JJ},' ; O0O0Ooo0 = '{MM},' ; IIIiIII1 = '{FQ},' ; OOo0OOo = '{HH},'
if 77 - 77: oo0oO00 . iIi1i1ii1 / o0o00Oo0O * oo0oO00
def oOoO0O0o ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( iIIII )
 oO00O0oO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( iIIII )
 for o00O0O , url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , o00O0O )
 oO00O0oO = oO00O0oO
 for url in oO00O0oO :
  IiIi1iIIi1 ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 69 - 69: IIi + IIi * iIi1i1ii1 * iiII11i1I1IIi + oOo0O0Ooo
def ii1i11iiII ( url ) :
 if 40 - 40: OooOO000
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  i1Oo00 = url + '&fv=&sou='
  i1Oo00 = i1Oo00 . replace ( 'player' , 'watch' )
  o000Oo0O0OoOo00 = I1i1I1i1i1 ( i1Oo00 )
  Ii11i1IiII = I1i1I1i1i1 ( url )
  if 96 - 96: Ii - OOooOOo / OooOO000 % ii / iI11I1II1I1I - IIi
  if 52 - 52: iI11I1II1I1I * OOooOOo + I11i . iiII11i1I1IIi
def I1i1I1i1i1 ( url ) :
 if 59 - 59: OooOO000 . ooOoO0O00
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  ooo0O0OO ( url )
  if 31 - 31: oOo0O0Ooo + oOo0O0Ooo
  if 11 - 11: OOoOoo + OOooOOo % I11i * oO0o / OOoOoo
def I11IiOO ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , O0o0Oo , '' )
 if 46 - 46: iI11I1II1I1I * OOooOOo - iiII11i1I1IIi . iI11I1II1I1I
def i1Iooo ( ) :
 if os . path . exists ( iiI1IiI ) :
  Ooo0O0O = open ( iiI1IiI , 'r' )
  for i11I in Ooo0O0O :
   iIII = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( i11I )
   for I1111i , oO0o0 in iIII :
    O0OoO0ooOO0o ( I1111i , oO0o0 , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 75 - 75: oOo0O0Ooo - IIiIi1iI - oOo0O0Ooo % oo0oO00 % ii
def I11Iii11i1Ii ( url ) :
 if os . path . exists ( Remote ) :
  I1 = iIi11i1 ( url )
  IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for I1111i , url in IIIII11I1IiI :
   url = ( url ) . strip ( )
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 65 - 65: iI11I1II1I1I * OOoOoo
  if 89 - 89: OOoOoo % Ii . Ii + oo0oO00 / Ii1I
def Iiii1i1 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for oO0o0 in IIIII11I1IiI :
  oO0o0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oO0o0
 I1111i = 'plugin.video.GenieTv'
 if 19 - 19: oOo0O0Ooo
 OO0OO0 ( oO0o0 , I1111i )
 if 100 - 100: oo0oO00 + oO0o
def II1I ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for oO0o0 in IIIII11I1IiI :
  oO0o0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oO0o0
 I1111i = 'repository.GenieTv'
 if 95 - 95: Ii . I11i + ii % I1ii11iIi11i
 OO0OO0 ( oO0o0 , I1111i )
 if 21 - 21: OooOO000 - I11i / iiII11i1I1IIi % o0o00Oo0O / iI11I1II1I1I / OooOO000
 if 1 - 1: I1ii11iIi11i . Ii
def iI1i11iII111 ( ) :
 i1Oo0oO00o = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i1Oo0oO00o )
 if i11I1II1I11i == 0 :
  ii1Ii ( )
 if i11I1II1I11i == 1 :
  iiI11Ii1 ( )
  if 37 - 37: I1ii11iIi11i + O00OOo00oo0o * oo0oO00 / I11i
  if 78 - 78: OOoOoo + iiII11i1I1IIi - I11i + oO0o / iI11I1II1I1I
  if 47 - 47: IIi
  if 20 - 20: O00OOo00oo0o % IIiIi1iI - O00OOo00oo0o * ii / Ii1I
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
O0000OOOoO = 'https://addons.tvaddons.ag/'
if 24 - 24: IIi
def iiI11Ii1 ( ) :
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 II1iI111iiIIiI1I = 'https://addons.tvaddons.ag/search/?keyword=' + iIi
 I1 = O000oo ( II1iI111iiIIiI1I )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for oO0o0 , ooo0O , I1111i in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , oO0o0 , 10054 , 'https://addons.tvaddons.ag/' + ooo0O , O0o0Oo , '' )
  if 71 - 71: OOoOoo - ooOoO0O00
  if 56 - 56: OOooOOo + oo0oO00
def ii1Ii ( ) :
 I1 = O000oo ( O0000OOOoO )
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
   if 74 - 74: OooOO000 / O00OOo00oo0o / IIiIiII11i - OooOO000 / oo0oO00 % iiII11i1I1IIi
   if 19 - 19: OOoOoo % ii + ii
def Addon ( url ) :
 I1 = O000oo ( url )
 i1IIi1iII1i = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  if 'Please' in I1111i :
   pass
  else :
   OOiIiIIi1 ( I1111i , url , 10054 , 'https://addons.tvaddons.ag/' + o00O0O , O0o0Oo , '' )
 for url in i1IIi1iII1i :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
  if 15 - 15: o0o00Oo0O % I1ii11iIi11i % OOoOoo % ii - OOoOoo
  if 27 - 27: O00OOo00oo0o - I11i * Ii1I - oOo0O0Ooo
def IIIiIIi111 ( url , name ) :
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
   if 77 - 77: oOo0O0Ooo / O00OOo00oo0o
def OO0OO0 ( url , name ) :
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
 if 65 - 65: Ii1I * o0o00Oo0O . ii * iiII11i1I1IIi / OOoOoo
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 87 - 87: iI11I1II1I1I
 if 58 - 58: Ii1I % Ii + OOooOOo / iiII11i1I1IIi - ii
def oOii1iiiiii ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , ooo0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , url , 1007 , ooo0O )
def OOOoO0o ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , ooo0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , ooo0O )
  if 12 - 12: ii . iiII11i1I1IIi . oO0o
  if 73 - 73: iIi1i1ii1 * ii * iiII11i1I1IIi - Ii
def Iiii1iI1i ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , iconimage , iII1iii , o0ooooO0o0O , name in IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    oo00OOoOoO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
    for i11I in oo00OOoOoO00 :
     if i11I == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    OoOoO00o00 ( name , url , 1016 , iconimage , o0ooooO0o0O , iII1iii )
   else :
    if 'youtube' in url :
     oo00OOoOoO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for i11I in oo00OOoOoO00 :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0o0oO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , o0ooooO0o0O , iII1iii )
    else :
     oo00OOoOoO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for i11I in oo00OOoOoO00 :
      if i11I == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0o0oO ( name , url , 222 , iconimage , o0ooooO0o0O , iII1iii )
     I1I11i ( 'tvshows' , 'Media Info 3' )
  else :
   oOOO00 ( url , iconimage , name )
   if 78 - 78: iIi1i1ii1
 else :
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
  for url , ooo0O , name in IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     IiIi1iIIi1 ( name , url , 1016 , ooo0O )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      O0OoO0ooOO0o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooo0O )
     else :
      oo00OOoOoO00 = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
      for i11I in oo00OOoOoO00 :
       if i11I == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      O0OoO0ooOO0o ( name , url , 222 , ooo0O )
      I1I11i ( 'tvshows' , 'Media Info 3' )
   else :
    oOOO00 ( url , ooo0O , name )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 29 - 29: IIiIiII11i
def oOOO00 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 OoOoO0ooo = ( url ) . replace ( oo0OOo0Oo00 , 'http' ) . replace ( iiI1I1iii1 , '.com' ) ;
 OO000o0O0o = ( OoOoO0ooo ) . replace ( o0oOOoOoOOo , 'a' ) . replace ( I1II1iIi , 'b' ) . replace ( IIiIi1II1IiI , 'c' ) . replace ( o0O0o , 'd' ) . replace ( oO0OIiIi1ii1Ii , 'e' ) . replace ( OOiIiI1iI , 'f' ) ;
 O0OiiiIIiIi1ii11 = ( OO000o0O0o ) . replace ( IiIi1iI1 , 'g' ) . replace ( II1IiI11I1 , 'h' ) . replace ( Ii111ii1 , 'i' ) . replace ( i11I111iII1i1 , 'j' ) . replace ( oo0OoO , 'k' ) . replace ( I11iIiiI , 'l' ) ;
 o0OOooOoOo00O = ( O0OiiiIIiIi1ii11 ) . replace ( oooOo000O , 'm' ) . replace ( IiiI1 , 'n' ) . replace ( iII1iiI11IIi , 'o' ) . replace ( i1ii11Iii11 , 'p' ) . replace ( o0ooOO , 'q' ) . replace ( OOoo000Ooo , 'r' ) ;
 iiii1II = ( o0OOooOoOo00O ) . replace ( ii1iIiIIIII , 's' ) . replace ( OO0o0o , 't' ) . replace ( iii , 'u' ) . replace ( OO00 , 'v' ) . replace ( iI1iII1 , 'w' ) . replace ( o0iiI11 , 'x' ) ;
 IiiiIII1i = ( iiii1II ) . replace ( OOooo0o0oOO0 , 'y' ) . replace ( I1II1IIiI11 , 'z' ) . replace ( ooOoo0O0o0OO0 , '.' ) . replace ( i11iiIiI11iII , '(' ) . replace ( i1II111II1 , ')' ) . replace ( I11I1iiI1 , '/' ) ;
 IIIiiiiiiii1 = ( IiiiIII1i ) . replace ( o0OOo0OOoOO0 , '1' ) . replace ( O0O0O00OoO0O , '2' ) . replace ( OO00Oo00o , '3' ) . replace ( II1I1iI1i1IiI , '4' ) . replace ( IIiiOoO000Ooo , '5' ) . replace ( OoOo00Oo0oo0O , '6' ) ;
 IiII1Iiii = ( IIIiiiiiiii1 ) . replace ( ooo0oooO , '7' ) . replace ( O0O0Ooo0 , '8' ) . replace ( IIIiIII1 , '9' ) . replace ( OOo0OOo , '0' ) . replace ( I1iI1iiI1Ii1 , ':' ) . replace ( O0oO0ooOOo , '%' ) ;
 url = ( IiII1Iiii ) . replace ( iii1iII1iii , '-' ) . replace ( oooo00o0O0 , '_' ) ;
 O0OoO0ooOO0o ( name , url , 222 , iconimage ) ;
 if 16 - 16: OooOO000 . o0o00Oo0O - O00OOo00oo0o * O00OOo00oo0o
 if 80 - 80: iIi1i1ii1 % Ii1I
def OOoo000OO00 ( ) :
 iIIII = iIi11i1 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for oO0o0 , ooo0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , oO0o0 , 1007 , ooo0O )
def O000oo0O0OO0 ( url ) :
 if 58 - 58: oO0o - ii . OooOO000
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , ooo0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , ooo0O )
  if 26 - 26: OOooOOo
def i1IiIiIii11I ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 O0oO0 = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 O0oO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0oO0 )
 if 80 - 80: O00OOo00oo0o + iiII11i1I1IIi . O00OOo00oo0o + IIi
 if 85 - 85: Ii . iiII11i1I1IIi + iIi1i1ii1 / iIi1i1ii1
def oooOo ( url ) :
 iIIII = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( iIIII )
 for url , o00O0O , I1111i in IIIII11I1IiI :
  if '-dir-' in I1111i :
   IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , o00O0O )
  else :
   IiIi1iIIi1 ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' , url , 1006 , o00O0O )
   if 43 - 43: OOoOoo . ii - IIiIiII11i
def OoOo0O0O ( url ) :
 iIIII = iIi11i1 ( url )
 o000oOOoo = ( 'http://afewbitsmore.com/' )
 IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '[To Parent Directory]' in I1111i :
   I1111i = 'HOME'
   pass
  elif 'HOME' in I1111i :
   pass
  elif '.m3u' in I1111i :
   IiIi1iIIi1 ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , o000oOOoo + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in I1111i :
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , o000oOOoo + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in I1111i :
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , o000oOOoo + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) , o000oOOoo + url , 1012 , oOOOo00O00oOo + 'music.png' )
def ooooOoo ( url ) :
 I1 = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for o00O0O , I1111i , url in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 99 - 99: OooOO000 % I11i + iI11I1II1I1I
def OoOOOO0ooO0 ( url ) :
 iIIII = iIi11i1 ( url )
 o000oOOoo = url
 IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  if '.mp3' in I1111i :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '/' , '' ) , o000oOOoo + url , 1011 , oOOOo00O00oOo + 'music.png' )
def oOOooo0O ( ) :
 iIIII = iIi11i1 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( iIIII )
 for oO0o0 , o00O0O , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , ( 'http://www.cyn.net/music/' + oO0o0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + o00O0O ) . replace ( ' ' , '%20' ) )
def O0O000 ( url , img ) :
 iIIII = iIi11i1 ( url )
 IiIIIIIi = url
 img = img
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( IiIIIIIi + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 72 - 72: ooOoO0O00
def iii1i11 ( url ) :
 iIIII = iIi11i1 ( url )
 IiIIIIIi = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( iIIII )
 for type , url , I1111i in IIIII11I1IiI :
  if '[VID]' in type :
   O0OoO0ooOO0o ( ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , IiIIIIIi + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   iii1i11 ( IiIIIIIi + url )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 72 - 72: IIiIi1iI + IIiIiII11i . o0o00Oo0O - OooOO000 / ii . O00OOo00oo0o
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
def oo0oo0O0 ( ) :
 OO000oo0o = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 i1111IIiii1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIi = i1111IIiii1 . lower ( )
 oO0o0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 ii1oOOO0ooOO = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 IiIIIIIi = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 32 - 32: ii
 I1 = OOoOO0oo0ooO ( oO0o0 )
 o0000Oo0 = OOoOO0oo0ooO ( ii1oOOO0ooOO )
 iii1i1iiiiIi = OOoOO0oo0ooO ( IiIIIIIi )
 if 29 - 29: Ii1I
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for oO0o0 , I1ii1ii11i1I , iII1iii , o0iiiI1I1iIIIi1 , I1111i in IIIII11I1IiI :
   if i1111IIiii1 in I1111i . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oO0o0 , 1016 , I1ii1ii11i1I , o0ooooO0o0O , iII1iii )
    if 41 - 41: iIi1i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if o0000Oo0 != 'Failed' :
  i1III1iI1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o0000Oo0 )
  for oO0o0 , I1111i in i1III1iI1I :
   if i1111IIiii1 in I1111i . lower ( ) :
    IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oO0o0 ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'Music.png' )
    if 49 - 49: iIi1i1ii1 % IIiIiII11i . iIi1i1ii1 - I11i - iiII11i1I1IIi * OOoOoo
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( iii1i1iiiiIi )
  for oO0o0 , I1111i in i1I :
   if i1111IIiii1 in I1111i . lower ( ) :
    IiIi1iIIi1 ( ( '[COLOR' + II + ']' + I1111i + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oO0o0 ) . replace ( ' ' , '%20' ) , 1006 , oOOOo00O00oOo + 'Music.png' )
    if 47 - 47: o0o00Oo0O . I11i / iIi1i1ii1 * OooOO000
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 63 - 63: O00OOo00oo0o - oo0oO00 - OooOO000 - IIiIi1iI / oo0oO00 + oO0o
    if 94 - 94: OOoOoo / oOo0O0Ooo . IIiIiII11i
    if 32 - 32: oo0oO00 . IIi % IIi . OOooOOo
    if 37 - 37: IIi + o0o00Oo0O + IIi . OooOO000 . I11i
    if 78 - 78: oOo0O0Ooo / iiII11i1I1IIi + I11i . I1ii11iIi11i / o0o00Oo0O
    if 49 - 49: Ii1I
oooOo000O = '{SF},' ; IiiI1 = '{IF},' ; iII1iiI11IIi = '{PW},' ; OO00Oo00o = '{AM},' ; i1ii11Iii11 = '{GF},' ; o0ooOO = '{DD},' ; OOoo000Ooo = '{UO},' ; ii1iIiIIIII = '{LE},' ; iii = '{ZY},' ; OO00 = '{UE},' ; iI1iII1 = '{PE},' ; o0iiI11 = '{JE},' ; OOooo0o0oOO0 = '{TH},' ; I1II1IIiI11 = '{LK},'
if 66 - 66: I11i . Ii1I
if 18 - 18: I1ii11iIi11i + OOoOoo
def IiIi1I1ii111 ( ) :
 iIIII = O000oo ( 'http://www.iwatchseries.me/tv-list/' )
 IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , oO0o0 , 8021 , oOOOo00O00oOo + 'iwatch.png' )
def OOOo0oo0 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( iIIII )
 for url , I1111i , OOOOOo in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i + OOOOOo , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def i1I1I1 ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  i11i ( url )
def i11i ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( iIIII )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( iIIII )
 ooOoO00 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( iIIII )
 Iii1I1111ii = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( 'VidSpot - ' + I1111i , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url in i1I :
  O0OoO0ooOO0o ( 'VodLocker' , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url , I1111i in Iii1I1111ii :
  O0OoO0ooOO0o ( 'VidUp' + I1111i , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for I1111i , url in ooOoO00 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   O0OoO0ooOO0o ( 'TheVideo - ' + I1111i , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
   if 14 - 14: iIi1i1ii1 + iIi1i1ii1 * ii * iiII11i1I1IIi + I1ii11iIi11i . oOo0O0Ooo
def o0ooo0 ( ) :
 iIIII = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , oO0o0 , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 80 - 80: IIi * oO0o + iIi1i1ii1
  if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
def OOOOo00oOOO00 ( ) :
 iIIII = O000oo ( 'http://www.animetoon.org/cartoon' )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( iIIII )
 for oO0o0 , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , oO0o0 , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 13 - 13: Ii1I / oO0o * Ii % oO0o % oO0o * IIiIiII11i
  if 17 - 17: iiII11i1I1IIi . o0o00Oo0O * ooOoO0O00 - OOooOOo % ooOoO0O00
  if 35 - 35: iIi1i1ii1 + Ii1I . oo0oO00 * I1ii11iIi11i
def IiI1I ( url ) :
 iIIII = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( iIIII )
 for o00O0O in i1I :
  O00O00 = o00O0O
 ooOoO00 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( iIIII )
 for url in ooOoO00 :
  IiIi1iIIi1 ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( iIIII )
 for url , I1111i in IIIII11I1IiI :
  IiIi1iIIi1 ( I1111i , url , 1003 , O00O00 )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0o0OoOOOoo ( url , IMAGE ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( iIIII )
 for I1111i , url in IIIII11I1IiI :
  print I1111i + '     ' + url
  if 'easy' in url :
   oo0O0O000O0oO ( url )
  elif 'playpanda' in url :
   oo0O0O000O0oO ( url )
   if 78 - 78: IIiIiII11i / iiII11i1I1IIi - Ii + Ii1I * I1ii11iIi11i
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo0O0O000O0oO ( url ) :
 iIIII = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( iIIII )
 for url in IIIII11I1IiI :
  O0OoO0ooOO0o ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 17 - 17: OOooOOo
  if 72 - 72: OooOO000 . I1ii11iIi11i - Ii / oOo0O0Ooo
def o0o0OoOo0 ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0o0O00Oo0o0 . add_header ( 'referer' , url )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 89 - 89: OOoOoo
def iIi11i1 ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 87 - 87: I11i % I1ii11iIi11i % IIiIiII11i + OooOO000 * oOo0O0Ooo
def i1iI1iIIiIi1I ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 IiiiIIiii = ( '%s%s' % ( OO0Oo00Oo , url ) )
 i1Oo00 = iIi11i1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , ooo0O , I1111i in IIIII11I1IiI :
  O0OoO0ooOO0o ( '%s' % ( '[COLOR' + II + ']' + I1111i + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , ooo0O )
  if 2 - 2: OooOO000 % ooOoO0O00 % iI11I1II1I1I - I11i + IIi
def OOOOOo00o0o ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  ooOoOoo ( url , I1111i )
 else :
  OOoo00OOoo ( url )
def OOoo00OOoo ( url ) :
 import urlresolver
 try :
  o0OOO00O0OOoO = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( o0OOO00O0OOoO , xbmcgui . ListItem ( I1111i ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( I1111i ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def ooo0O0OO ( url ) :
 if 93 - 93: OooOO000 . Ii
 I1iii = open ( oOOoo0Oo , "a" )
 I1iii . write ( 'url="' + url + '"\n' )
 I1iii . close
 if 24 - 24: IIi . oO0o + O00OOo00oo0o . oo0oO00 - Ii1I % OooOO000
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
def ooOoOoo ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  IiI = '.mp4'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   OOoo00OOoo ( url )
  if i11I1II1I11i == 1 :
   iiii1iI1IIiIi ( url , name , IiI )
 elif '.mkv' in url :
  IiI = '.mkv'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   OOoo00OOoo ( url )
  if i11I1II1I11i == 1 :
   iiii1iI1IIiIi ( url , name , IiI )
 elif '.mp3' in url :
  IiI = '.mp3'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   OOoo00OOoo ( url )
  if i11I1II1I11i == 1 :
   iiii1iI1IIiIi ( url , name , IiI )
 elif '.avi' in url :
  IiI = '.mp3'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   OOoo00OOoo ( url )
  if i11I1II1I11i == 1 :
   iiii1iI1IIiIi ( url , name , IiI )
 elif '.mov' in url :
  IiI = '.mp3'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   OOoo00OOoo ( url )
  if i11I1II1I11i == 1 :
   iiii1iI1IIiIi ( url , name , IiI )
 elif '.mpeg' in url :
  IiI = '.mp3'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   OOoo00OOoo ( url )
  if i11I1II1I11i == 1 :
   iiii1iI1IIiIi ( url , name , IiI )
 elif '.mpg' in url :
  IiI = '.mp3'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   OOoo00OOoo ( url )
  if i11I1II1I11i == 1 :
   iiii1iI1IIiIi ( url , name , IiI )
 elif '.flv' in url :
  IiI = '.mp3'
  i1Oo0oO00o = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  i11I1II1I11i = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i1Oo0oO00o )
  if i11I1II1I11i == 0 :
   OOoo00OOoo ( url )
  if i11I1II1I11i == 1 :
   iiii1iI1IIiIi ( url , name , IiI )
 else :
  OOoo00OOoo ( url )
def iiii1iI1IIiIi ( url , name , cat ) :
 i1Iii1I11ii ( )
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
def i1Iii1I11ii ( ) :
 o00O0 = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def oOoO000OOoo0 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 o0oOoO00o . update ( 100 , '%s' % I1111i )
 xbmc . sleep ( 1 )
 oO0O . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 44 - 44: oO0o % Ii . O00OOo00oo0o - o0o00Oo0O / OooOO000 . IIiIi1iI
def OOOOo0o00OO0000 ( url ) :
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0O . play ( url ) . strip ( )
 except : pass
 if 23 - 23: I11i % iI11I1II1I1I
def O0OOo00OO ( url ) :
 oO0O = xbmc . Player ( oOOiiiIIiIi ( ) )
 import urlresolver
 iIIiI1II = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 oO0O . play ( iIIiI1II )
 xbmc . sleep ( 1 )
 oO0O . play ( url )
 if 56 - 56: iI11I1II1I1I - IIi - iIi1i1ii1 - o0o00Oo0O
 if 4 - 4: I1ii11iIi11i + Ii1I * Ii * iI11I1II1I1I - O00OOo00oo0o
def oOOiiiIIiIi ( ) :
 try :
  II1II1ii1Ii = getSet ( "core-player" )
  if ( II1II1ii1Ii == 'DVDPLAYER' ) : OooOOo = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( II1II1ii1Ii == 'MPLAYER' ) : OooOOo = xbmc . PLAYER_CORE_MPLAYER
  elif ( II1II1ii1Ii == 'PAPLAYER' ) : OooOOo = xbmc . PLAYER_CORE_PAPLAYER
  else : OooOOo = xbmc . PLAYER_CORE_AUTO
 except : OooOOo = xbmc . PLAYER_CORE_AUTO
 return OooOOo
 return True
 if 96 - 96: iiII11i1I1IIi + iI11I1II1I1I % IIiIiII11i
def IiIi1iIIi1 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
 if 61 - 61: IIi . Ii1I * oo0oO00 / O00OOo00oo0o - oO0o
def i1II ( name , url , mode , iconimage , fanart , description ) :
 if 18 - 18: O00OOo00oo0o
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
 if 34 - 34: OooOO000 + O00OOo00oo0o * iiII11i1I1IIi / IIiIiII11i
def O0OoO0ooOO0o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIiii = [ ]
  IIiii . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = False )
 return ii1iiIi1
 if 14 - 14: IIiIiII11i + OooOO000 + iIi1i1ii1 / OooOO000 . iI11I1II1I1I
 if 85 - 85: iiII11i1I1IIi % iiII11i1I1IIi . o0o00Oo0O
 if 40 - 40: oO0o * OOooOOo * iI11I1II1I1I / OOooOOo * ii / Ii1I
 if 33 - 33: Ii % I11i . OooOO000 * IIi / iiII11i1I1IIi
 if 25 - 25: oO0o
 if 39 - 39: iIi1i1ii1 * OOooOOo + I1ii11iIi11i . IIi - o0o00Oo0O * Ii1I
def OO0O000 ( heading , announce ) :
 class O0o0ooo00o00 ( ) :
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
   try : oooOo0OOOoo0 = open ( announce ) ; ooOOo00oo0 = oooOo0OOOoo0 . read ( )
   except : ooOOo00oo0 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( ooOOo00oo0 ) )
   return
 O0o0ooo00o00 ( )
 O0o0ooo00o00 ( )
 if 6 - 6: Ii / oO0o . Ii / IIiIi1iI
def iI1Ii11iIiI1 ( ) :
 OO0O000 ( 'GenieTv Recomended Sources' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Reaper[/COLOR] [CR]  [COLORred]http://roguemedia.info/cerberus/repo/[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 26 - 26: o0o00Oo0O * iIi1i1ii1 - oOo0O0Ooo - OooOO000 / iI11I1II1I1I
 if 57 - 57: Ii1I - oO0o * iI11I1II1I1I
 if 26 - 26: oO0o % IIiIi1iI % I11i % OOooOOo . OooOO000 % o0o00Oo0O
 if 91 - 91: IIiIiII11i . I1ii11iIi11i . oo0oO00 - ii / OOooOOo
 if 30 - 30: iiII11i1I1IIi % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
def O0O0ooOOO ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 55 - 55: oO0o
 if 20 - 20: IIiIi1iI * O00OOo00oo0o * I11i - IIiIi1iI
 if 32 - 32: iIi1i1ii1 * oo0oO00
 if 85 - 85: Ii . oO0o + oO0o
 if 28 - 28: I1ii11iIi11i
 if 62 - 62: I1ii11iIi11i + ii / OooOO000
 if 60 - 60: iIi1i1ii1 / OOooOOo . iiII11i1I1IIi % IIi
 if 61 - 61: o0o00Oo0O . iIi1i1ii1 . o0o00Oo0O * Ii * IIiIiII11i / O00OOo00oo0o
 if 69 - 69: iiII11i1I1IIi
 if 17 - 17: iiII11i1I1IIi
 if 38 - 38: O00OOo00oo0o % IIi
 if 9 - 9: o0o00Oo0O . iI11I1II1I1I
 if 44 - 44: Ii1I % OOoOoo
 if 6 - 6: oO0o
 if 82 - 82: iI11I1II1I1I . iiII11i1I1IIi / OOoOoo / IIi * IIiIiII11i % oo0oO00
 if 62 - 62: IIiIiII11i
 if 96 - 96: iiII11i1I1IIi % OOooOOo * Ii1I
 if 94 - 94: I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % I1ii11iIi11i . IIiIi1iI
 if 63 - 63: Ii % Ii1I % oOo0O0Ooo . OOoOoo * I11i + IIi
 if 77 - 77: I11i
 if 63 - 63: IIiIi1iI * oo0oO00 + IIiIi1iI * iIi1i1ii1 + I1ii11iIi11i / Ii1I
 if 15 - 15: o0o00Oo0O . Ii1I * Ii1I
 if 65 - 65: O00OOo00oo0o + o0o00Oo0O % I11i
 if 72 - 72: IIi . OOooOOo / IIiIiII11i
def OOOoO0OooOO0o ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + i1iiIi1ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 54 - 54: ii . O00OOo00oo0o
def oo0o0oo0O0O ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + I1Iii1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 22 - 22: O00OOo00oo0o
def I1I11I1I11iII ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + i1I11iIIiIIiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 45 - 45: oOo0O0Ooo
def IiI1i11i ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + II111II1IiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 56 - 56: Ii1I
def II1iIii1Ii ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OoOO0OO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 28 - 28: o0o00Oo0O / I11i . iIi1i1ii1 / o0o00Oo0O . oo0oO00 - I11i
def OOooiii1I ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iIIiiiIiiii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 22 - 22: iiII11i1I1IIi
def I1ioooOooo00O0 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + II1iIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 3 - 3: Ii1I
def I1III1i1Ii ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o00oOoO0ooOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 37 - 37: OooOO000 + O00OOo00oo0o * iIi1i1ii1 + OOoOoo
def IiIIIii1iIII1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OoOooooo0oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 42 , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 15 - 15: iI11I1II1I1I + OooOO000
def OOOoo0OO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + Iii11I1II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for I1111i , url , I1ii1ii11i1I , o0ooooO0o0O , I11o0oO00oO0o0o0 in IIIII11I1IiI :
  iiOOooooO0Oo ( I1111i , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , I11o0oO00oO0o0o0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 96 - 96: O00OOo00oo0o % ooOoO0O00 . OooOO000 / o0o00Oo0O
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + IIiIi1iI . O00OOo00oo0o * IIiIi1iI
 if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
 if 82 - 82: o0o00Oo0O / OooOO000 * oO0o - iiII11i1I1IIi + I1ii11iIi11i
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + iIi1i1ii1 * IIiIiII11i
 if 78 - 78: O00OOo00oo0o - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
 if 97 - 97: ooOoO0O00
 if 29 - 29: oOo0O0Ooo
 if 37 - 37: Ii1I * O00OOo00oo0o * oOo0O0Ooo * o0o00Oo0O
def oOo0Oo0O0O ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for Ii1iiI1 , iiiI11iIIi1 , o00OoooooooOo in os . walk ( iIi1ii1I1 ) :
     Ii1II1i1i = 0
     Ii1II1i1i += len ( o00OoooooooOo )
     if Ii1II1i1i > 0 :
      for oooOo0OOOoo0 in o00OoooooooOo :
       os . unlink ( os . path . join ( Ii1iiI1 , oooOo0OOOoo0 ) )
  II1o0o00O = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( II1o0o00O )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 59 - 59: O00OOo00oo0o * OooOO000
 if 31 - 31: iiII11i1I1IIi / o0o00Oo0O
 if 57 - 57: ooOoO0O00 % IIiIi1iI
 if 69 - 69: I11i
 if 69 - 69: O00OOo00oo0o
 if 83 - 83: iI11I1II1I1I . I11i + O00OOo00oo0o . ii / IIiIi1iI + IIiIiII11i
 if 90 - 90: iIi1i1ii1 * OooOO000 / IIi
 if 68 - 68: OOooOOo
def i1I11ii ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 65 - 65: oo0oO00
def oooO0oOoo ( url ) :
 o000oOOO = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 iIi1 = [
 ( o000oOOO ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( o000oOOO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( o000oOOO , 'plugin.video.itv' , 'Images' ) ) ]
 if 65 - 65: iIi1i1ii1
 O0o0OOOooo0 = 0
 if 18 - 18: oOo0O0Ooo
 for i11I in iIi1 :
  if os . path . exists ( i11I ) and not i11I in [ oO0o0o0ooO0oO , o000oOOO ] :
   for Ii1iiI1 , iiiI11iIIi1 , o00OoooooooOo in os . walk ( i11I ) :
    Ii1II1i1i = 0
    Ii1II1i1i += len ( o00OoooooooOo )
    if Ii1II1i1i > 0 :
     for oooOo0OOOoo0 in o00OoooooooOo :
      if not oooOo0OOOoo0 in oooOOOOO :
       try :
        os . unlink ( os . path . join ( Ii1iiI1 , oooOo0OOOoo0 ) )
       except :
        pass
      else : iIiIi11 ( 'Ignore Log File: %s' % oooOo0OOOoo0 )
     for iii11i1 in iiiI11iIIi1 :
      try :
       shutil . rmtree ( os . path . join ( Ii1iiI1 , iii11i1 ) )
       O0o0OOOooo0 += 1
       iIiIi11 ( "[Success] cleared %s files from %s" % ( str ( Ii1II1i1i ) , os . path . join ( i11I , iii11i1 ) ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , iii11i1 ) )
  else :
   for Ii1iiI1 , iiiI11iIIi1 , o00OoooooooOo in os . walk ( i11I ) :
    for iii11i1 in iiiI11iIIi1 :
     if 'cache' in iii11i1 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( Ii1iiI1 , iii11i1 ) )
       O0o0OOOooo0 += 1
       iIiIi11 ( "[Success] wiped %s " % os . path . join ( i11I , iii11i1 ) )
      except :
       iIiIi11 ( "[Failed] to wipe cache in: %s" % os . path . join ( i11I , iii11i1 ) )
       if 32 - 32: iI11I1II1I1I * oOo0O0Ooo . IIi * iI11I1II1I1I
 i1I11ii ( oO , 'Clear Cache: Removed %s Files' % O0o0OOOooo0 )
 if 92 - 92: oo0oO00 - IIiIi1iI . ii * oo0oO00 / I1ii11iIi11i
 if 16 - 16: iiII11i1I1IIi / ii - OOoOoo % oOo0O0Ooo % iiII11i1I1IIi
 if 97 - 97: IIi * ooOoO0O00 / ii
 if 64 - 64: IIi + I11i / Ii - OOooOOo + IIi
 if 90 - 90: ooOoO0O00 % oO0o / IIiIi1iI - o0o00Oo0O + Ii
 if 98 - 98: ii
 if 61 - 61: I11i . OOoOoo . o0o00Oo0O + ii + o0o00Oo0O
def OoOOoO0O0oO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 Oo00Ooo0O0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Ii1iiI1 , iiiI11iIIi1 , o00OoooooooOo in os . walk ( Oo00Ooo0O0O0o ) :
   Ii1II1i1i = 0
   Ii1II1i1i += len ( o00OoooooooOo )
   if 86 - 86: oOo0O0Ooo + iI11I1II1I1I % IIiIi1iI / IIi / ii
   if 96 - 96: oo0oO00 - IIiIiII11i % oOo0O0Ooo * OOoOoo * iiII11i1I1IIi - IIi
   if Ii1II1i1i > 0 :
    if 69 - 69: IIiIi1iI / I1ii11iIi11i + oo0oO00 % ooOoO0O00 * O00OOo00oo0o - ooOoO0O00
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( Ii1II1i1i ) + " files found" , "Do you want to delete them?" ) :
     if 90 - 90: iIi1i1ii1 + oo0oO00 . IIiIiII11i - OOooOOo % iI11I1II1I1I
     for oooOo0OOOoo0 in o00OoooooooOo :
      os . unlink ( os . path . join ( Ii1iiI1 , oooOo0OOOoo0 ) )
     for iii11i1 in iiiI11iIIi1 :
      shutil . rmtree ( os . path . join ( Ii1iiI1 , iii11i1 ) )
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
 if 24 - 24: OOoOoo / iIi1i1ii1 * IIi
 if 33 - 33: IIi
 if 22 - 22: o0o00Oo0O + IIi % ooOoO0O00
 if 83 - 83: o0o00Oo0O + iIi1i1ii1 % Ii
 if 32 - 32: O00OOo00oo0o % I1ii11iIi11i - iiII11i1I1IIi + o0o00Oo0O
 if 57 - 57: oO0o + O00OOo00oo0o . iiII11i1I1IIi . ooOoO0O00 - I11i / I1ii11iIi11i
 if 19 - 19: iI11I1II1I1I . oO0o / ii
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % O00OOo00oo0o / Ii1I
 if 76 - 76: oO0o * oo0oO00 - oO0o
def I1iIIiiIIi1i ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 Oo00Ooo0O0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Ii1iiI1 , iiiI11iIIi1 , o00OoooooooOo in os . walk ( Oo00Ooo0O0O0o ) :
   Ii1II1i1i = 0
   Ii1II1i1i += len ( o00OoooooooOo )
   if 57 - 57: ii / OOooOOo + oo0oO00 . iIi1i1ii1
   if 14 - 14: Ii % IIi * I11i * OOooOOo
   if Ii1II1i1i > 0 :
    if 55 - 55: O00OOo00oo0o * IIi * O00OOo00oo0o
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( Ii1II1i1i ) + " files found" , "Do you want to delete them?" ) :
     if 70 - 70: o0o00Oo0O . iIi1i1ii1
     for oooOo0OOOoo0 in o00OoooooooOo :
      os . unlink ( os . path . join ( Ii1iiI1 , oooOo0OOOoo0 ) )
     for iii11i1 in iiiI11iIIi1 :
      shutil . rmtree ( os . path . join ( Ii1iiI1 , iii11i1 ) )
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
 oooO0oOoo ( url )
 return
 if 33 - 33: IIi * iIi1i1ii1
 if 64 - 64: Ii . iI11I1II1I1I
 if 7 - 7: OOooOOo % IIiIi1iI + OOooOOo - OOooOOo * Ii % oO0o
 if 57 - 57: IIi / oO0o + Ii1I
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % IIi + OOoOoo . oO0o . I1ii11iIi11i
 if 70 - 70: iiII11i1I1IIi . Ii1I * oo0oO00
 if 97 - 97: oo0oO00 . iI11I1II1I1I - IIi
 if 23 - 23: Ii1I % iiII11i1I1IIi
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
 if 99 - 99: O00OOo00oo0o - Ii1I - oOo0O0Ooo - O00OOo00oo0o + oO0o + IIiIiII11i
def i11iii1II1I1 ( url , name ) :
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IiIi11iI1IIi = os . path . join ( o00O0 , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 iII111I = os . path . join ( o00O0 , 'advancedsettings.xml.bak' )
 if os . path . exists ( iII111I ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   IiIi11iI1IIi = os . path . join ( o00O0 , 'advancedsettings.xml' )
   try :
    os . remove ( IiIi11iI1IIi )
    print '=== GenieTv - REMOVING    ' + str ( IiIi11iI1IIi ) + '    ==='
   except :
    pass
   i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
   oo0oO = open ( IiIi11iI1IIi , "w" )
   oo0oO . write ( i1Oo00 )
   oo0oO . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( IiIi11iI1IIi ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  IiIi11iI1IIi = os . path . join ( o00O0 , 'advancedsettings.xml' )
  try :
   os . remove ( IiIi11iI1IIi )
   print '=== GenieTv - REMOVING    ' + str ( IiIi11iI1IIi ) + '    ==='
  except :
   pass
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  oo0oO = open ( IiIi11iI1IIi , "w" )
  oo0oO . write ( i1Oo00 )
  oo0oO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IiIi11iI1IIi ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 78 - 78: IIiIiII11i * iI11I1II1I1I / OOoOoo . Ii1I
def IIiIiI1III1 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IiIi11iI1IIi = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  oo0oO = open ( IiIi11iI1IIi ) . read ( )
  if 'zero' in oo0oO :
   name = '0CACHE'
  elif 'tuxen' in oo0oO :
   name = 'TUXENS'
  elif 'muckys' in oo0oO :
   name = 'MUCKYS'
  elif 'p2p1' in oo0oO :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in oo0oO :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in oo0oO :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 13 - 13: IIiIiII11i . oO0o
def IIIoOoo0O00OO ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 o00O0 = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 IiIi11iI1IIi = os . path . join ( o00O0 , 'advancedsettings.xml' )
 try :
  os . remove ( IiIi11iI1IIi )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( IiIi11iI1IIi ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 20 - 20: OooOO000 - Ii1I * OooOO000 + O00OOo00oo0o
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - OOoOoo
 if 30 - 30: ii % IIi
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - IIi
 if 81 - 81: OooOO000 % iIi1i1ii1 . IIiIi1iI
 if 66 - 66: Ii1I * iIi1i1ii1 / ii * o0o00Oo0O % IIi
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * iIi1i1ii1 / O00OOo00oo0o * ii
 if 82 - 82: I1ii11iIi11i / iIi1i1ii1 / iIi1i1ii1 % iIi1i1ii1
 if 20 - 20: IIiIi1iI
 if 63 - 63: iI11I1II1I1I . oO0o
def oOOoO ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for ooooOo00OO0o , oO0o0oo , iiiI11iii11iI , I111iIii1i1 in IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ooooOo00OO0o , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iiiI11iii11iI , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % I111iIii1i1 )
  inc = inc + 1
  if 6 - 6: O00OOo00oo0o % OOoOoo / iIi1i1ii1 + O00OOo00oo0o . oo0oO00
  if 70 - 70: iI11I1II1I1I / iIi1i1ii1
  if 61 - 61: o0o00Oo0O * I11i + O00OOo00oo0o - IIi . oOo0O0Ooo - OOoOoo
  if 7 - 7: Ii1I
  if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / iiII11i1I1IIi
  if 95 - 95: OOooOOo - o0o00Oo0O % ii
  if 13 - 13: Ii
  if 54 - 54: IIi . Ii1I * iiII11i1I1IIi % O00OOo00oo0o . o0o00Oo0O * OOoOoo
  if 87 - 87: iIi1i1ii1 % Ii1I * I1ii11iIi11i
def OOO00i111 ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  IiIi11iI1IIi = os . path . join ( o00O0 , 'addons2.ini' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  oo0oO = open ( IiIi11iI1IIi , "w" )
  oo0oO . write ( i1Oo00 )
  oo0oO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IiIi11iI1IIi ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 25 - 25: Ii / iI11I1II1I1I * ii . IIi
def oO000oOo0oO0 ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  o00O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  IiIi11iI1IIi = os . path . join ( o00O0 , 'settings.xml' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  oo0oO = open ( IiIi11iI1IIi , "w" )
  oo0oO . write ( i1Oo00 )
  oo0oO . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( IiIi11iI1IIi ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 2 - 2: I11i - oOo0O0Ooo - Ii / ii
 if 87 - 87: I11i + oo0oO00 + ii * IIi
def IIIi1Iiii1I1 ( ) :
 try :
  iI1 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( iI1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    iiII1iii111 = os . path . join ( iI1 , "source.db" )
    os . unlink ( iiII1iii111 )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 22 - 22: oOo0O0Ooo
 if 76 - 76: oO0o + iiII11i1I1IIi + oO0o . iiII11i1I1IIi % IIi
 if 96 - 96: I1ii11iIi11i
 if 34 - 34: oo0oO00 - Ii1I
 if 10 - 10: IIi . iIi1i1ii1
def O000oo ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 5 - 5: OOoOoo - iiII11i1I1IIi
 if 16 - 16: OOoOoo . OooOO000 . I1ii11iIi11i % IIi / OOoOoo
 if 72 - 72: I11i * IIiIi1iI - Ii / iIi1i1ii1
 if 11 - 11: o0o00Oo0O - oOo0O0Ooo
 if 31 - 31: OooOO000
 if 1 - 1: O00OOo00oo0o / OOooOOo * OOooOOo - I11i % iIi1i1ii1
 if 96 - 96: OOoOoo / iIi1i1ii1 % oO0o . iI11I1II1I1I
def i11i1ii1I ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; i1Iiiiiii = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if i1Iiiiiii :
  Oo000O00o0O = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; Oo000O00o0O = xbmc . translatePath ( Oo000O00o0O ) ;
  o0o0oo0oO = os . path . join ( Oo000O00o0O , ".." , ".." ) ; o0o0oo0oO = os . path . abspath ( o0o0oo0oO ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + o0o0oo0oO ) ; Ii1iii1 = False
  try :
   for Ii1iiI1 , iiiI11iIIi1 , o00OoooooooOo in os . walk ( o0o0oo0oO , topdown = True ) :
    iiiI11iIIi1 [ : ] = [ iii11i1 for iii11i1 in iiiI11iIIi1 if iii11i1 not in o0oO0 ]
    for I1111i in o00OoooooooOo :
     try : os . remove ( os . path . join ( Ii1iiI1 , I1111i ) )
     except :
      if I1111i not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Ii1iii1 = True
      plugintools . log ( "Error removing " + Ii1iiI1 + " " + I1111i )
    for I1111i in iiiI11iIIi1 :
     try : os . rmdir ( os . path . join ( Ii1iiI1 , I1111i ) )
     except :
      if I1111i not in [ "Database" , "userdata" ] : Ii1iii1 = True
      plugintools . log ( "Error removing " + Ii1iiI1 + " " + I1111i )
   if not Ii1iii1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 i1iiI ( )
 if 75 - 75: I1ii11iIi11i / Ii * oOo0O0Ooo - ii
 if 25 - 25: iiII11i1I1IIi / Ii1I * oO0o . OooOO000
 if 18 - 18: o0o00Oo0O % I11i + OooOO000 + O00OOo00oo0o % OOoOoo
def I1I111i1I1II ( ) :
 O00oOoO0o0oO = [ ]
 oOoO = sys . argv [ 2 ]
 if len ( oOoO ) >= 2 :
  o0OO0o0o00o = sys . argv [ 2 ]
  Oo00oO = o0OO0o0o00o . replace ( '?' , '' )
  if ( o0OO0o0o00o [ len ( o0OO0o0o00o ) - 1 ] == '/' ) :
   o0OO0o0o00o = o0OO0o0o00o [ 0 : len ( o0OO0o0o00o ) - 2 ]
  Oo0OOOOOOOo0O = Oo00oO . split ( '&' )
  O00oOoO0o0oO = { }
  for OoOooOo00O in range ( len ( Oo0OOOOOOOo0O ) ) :
   I1III = { }
   I1III = Oo0OOOOOOOo0O [ OoOooOo00O ] . split ( '=' )
   if ( len ( I1III ) ) == 2 :
    O00oOoO0o0oO [ I1III [ 0 ] ] = I1III [ 1 ]
    if 41 - 41: iI11I1II1I1I - oO0o * OOoOoo
 return O00oOoO0o0oO
 if 65 - 65: IIi / IIi / OooOO000 * ii
iIIi1IiiiII1i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
Ooo000000 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
IIiIii1iiI = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
o0oOOOOOO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
OOo000OO000 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
IIIIII11iIiI1III = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
i1iiIi1ii = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
o0Ooo0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
I1Iii1iI = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
i1I11iIIiIIiIi = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
II111II1IiI = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OoOO0OO00 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
iIIiiiIiiii11 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
II1iIii = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
o00oOoO0ooOO = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
OoOooooo0oo = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
I1i11II11i = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
I1ii11iiIIi = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
i1I11 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oo000oOO00o0oOO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
i1IoOOoooO0O0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
OO0ooOoOO0OOo = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
Iii11I1II1 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OO0Oo00Oo = base64 . decodestring ( 'Q1VOVA==' )
def iiOOooooO0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = True )
 return ii1iiIi1
 if 61 - 61: OooOO000
def OOiIiIIi1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 oo0o0oooo = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ii1iiIi1 = True
 i111iiI1ii = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i111iiI1ii . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 i111iiI1ii . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIiii = [ ]
  if showcontext == 'fav' :
   IIiii . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIiii . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  i111iiI1ii . addContextMenuItems ( IIiii )
 ii1iiIi1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0o0oooo , listitem = i111iiI1ii , isFolder = False )
 return ii1iiIi1
 if 18 - 18: I11i / Ii % Ii1I * ii
 if 67 - 67: OOooOOo
o0OO0o0o00o = I1I111i1I1II ( )
oO0o0 = None
I1111i = None
I1iii11 = None
I1ii1ii11i1I = None
o0ooooO0o0O = None
I11o0oO00oO0o0o0 = None
OOO0 = None
o0oo00 = None
if 92 - 92: ooOoO0O00
if 68 - 68: oO0o % OOoOoo - oo0oO00 - IIiIi1iI . I1ii11iIi11i
try :
 o0oo00 = int ( o0OO0o0o00o [ "fav_mode" ] )
except :
 pass
 if 30 - 30: ii % I11i + IIiIi1iI * oO0o
try :
 oO0o0 = urllib . unquote_plus ( o0OO0o0o00o [ "url" ] )
except :
 pass
try :
 I1111i = urllib . unquote_plus ( o0OO0o0o00o [ "name" ] )
except :
 pass
try :
 I1ii1ii11i1I = urllib . unquote_plus ( o0OO0o0o00o [ "iconimage" ] )
except :
 pass
try :
 I1iii11 = int ( o0OO0o0o00o [ "mode" ] )
except :
 pass
try :
 o0ooooO0o0O = urllib . unquote_plus ( o0OO0o0o00o [ "fanart" ] )
except :
 pass
try :
 I11o0oO00oO0o0o0 = urllib . unquote_plus ( o0OO0o0o00o [ "description" ] )
except :
 pass
 if 57 - 57: iiII11i1I1IIi + iI11I1II1I1I . oO0o + oo0oO00
 if 4 - 4: iIi1i1ii1
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( I1iii11 )
print "URL: " + str ( oO0o0 )
print "Name: " + str ( I1111i )
print "IconImage: " + str ( I1ii1ii11i1I )
if 43 - 43: ooOoO0O00 . oOo0O0Ooo * iI11I1II1I1I * Ii - IIi + IIiIi1iI
if 56 - 56: I1ii11iIi11i % Ii / iIi1i1ii1 . O00OOo00oo0o . oO0o - OOooOOo
def I1I11i ( content , viewType ) :
 if 32 - 32: O00OOo00oo0o / oo0oO00 / oOo0O0Ooo
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 22 - 22: oO0o - OOooOOo . I1ii11iIi11i + I11i
if I1ii1ii11i1I == None : I1ii1ii11i1I = Oo00OOOOO
if o0ooooO0o0O == None : o0ooooO0o0O = O0o0Oo
if I1iii11 == None :
 o0o0o0oO0oOO ( )
 if 69 - 69: oo0oO00 - oOo0O0Ooo
elif I1iii11 == 1 :
 iiIIiiIi ( oO0o0 )
 if 10 - 10: ooOoO0O00 / OooOO000 . IIiIiII11i * ooOoO0O00 % ii
elif I1iii11 == 44 :
 oOo0 ( oO0o0 )
 if 83 - 83: iiII11i1I1IIi . IIi + O00OOo00oo0o * iiII11i1I1IIi . O00OOo00oo0o + oo0oO00
elif I1iii11 == 2 :
 oo0o0OoOO0o0 ( )
 if 64 - 64: iIi1i1ii1 . I11i - ooOoO0O00
elif I1iii11 == 3 :
 Ii11i1Ii1IIII ( )
 if 35 - 35: Ii1I % ii
elif I1iii11 == 21 :
 i1i1II ( )
 if 59 - 59: oOo0O0Ooo % iiII11i1I1IIi
elif I1iii11 == 4 :
 i1iIi1IIiIII1 ( )
 if 32 - 32: oOo0O0Ooo * o0o00Oo0O + o0o00Oo0O
elif I1iii11 == 5 :
 Ooo000O00 ( oO0o0 )
 if 34 - 34: OOoOoo
elif I1iii11 == 6 :
 OoOOoO0O0oO ( oO0o0 )
 if 5 - 5: oO0o . oOo0O0Ooo
elif I1iii11 == 7 :
 i11iii1II1I1 ( oO0o0 , I1111i )
 if 48 - 48: I1ii11iIi11i - oO0o . iiII11i1I1IIi - iI11I1II1I1I % iIi1i1ii1
elif I1iii11 == 8 :
 IIiIiI1III1 ( oO0o0 , I1111i )
 if 47 - 47: OooOO000 / ii - IIiIiII11i
elif I1iii11 == 9 :
 FIXREPOSADDONS ( oO0o0 )
 if 91 - 91: OOooOOo + I11i
elif I1iii11 == 10 :
 O0O0ooOOO ( )
 if 23 - 23: ooOoO0O00
elif I1iii11 == 11 :
 IIIoOoo0O00OO ( oO0o0 )
 if 9 - 9: ooOoO0O00 % O00OOo00oo0o - oO0o * OOooOOo . I11i
elif I1iii11 == 12 :
 oOOoO ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 18 - 18: iIi1i1ii1 . OOooOOo + OooOO000 . oOo0O0Ooo + ii . oO0o
elif I1iii11 == 13 :
 oOo0Oo0O0O ( )
 if 31 - 31: O00OOo00oo0o - iiII11i1I1IIi
elif I1iii11 == 14 :
 oooO0oOoo ( oO0o0 )
 if 49 - 49: iI11I1II1I1I - iI11I1II1I1I - OOooOOo + OOoOoo / OOooOOo
elif I1iii11 == 15 :
 oOOOoo0o ( )
 if 74 - 74: ii + Ii1I % o0o00Oo0O
elif I1iii11 == 16 :
 OOO00i111 ( oO0o0 , I1111i )
 if 32 - 32: Ii1I + Ii1I
elif I1iii11 == 17 :
 oO000oOo0oO0 ( oO0o0 , I1111i )
 if 89 - 89: IIiIi1iI + oo0oO00 + iIi1i1ii1 - IIi
elif I1iii11 == 18 :
 IIIi1Iiii1I1 ( )
 if 12 - 12: OOooOOo - I11i - O00OOo00oo0o / iiII11i1I1IIi
elif I1iii11 == 19 :
 Iiii1I ( oO0o0 )
 if 17 - 17: oO0o - O00OOo00oo0o - IIiIiII11i / O00OOo00oo0o / iIi1i1ii1
elif I1iii11 == 40 :
 oOO0o ( I1111i , oO0o0 , I11o0oO00oO0o0o0 )
 if 30 - 30: IIi * Ii1I % Ii1I + OooOO000 * OOoOoo
elif I1iii11 == 42 :
 I1II1 ( I1111i , oO0o0 , I11o0oO00oO0o0o0 )
 if 33 - 33: I11i + iiII11i1I1IIi * o0o00Oo0O * oO0o . Ii1I
elif I1iii11 == 43 :
 oooOoO ( oO0o0 )
 if 74 - 74: OooOO000 * OooOO000 * I11i / oo0oO00
elif I1iii11 == 20 :
 II1I1ii1ii11 ( oO0o0 )
 if 91 - 91: Ii . Ii1I / IIiIiII11i
elif I1iii11 == 22 :
 OOOoO0OooOO0o ( oO0o0 )
 if 97 - 97: iIi1i1ii1 % ooOoO0O00 % OOoOoo + I1ii11iIi11i - o0o00Oo0O - iiII11i1I1IIi
elif I1iii11 == 23 :
 oo0o0oo0O0O ( oO0o0 )
 if 64 - 64: iIi1i1ii1 - OooOO000
elif I1iii11 == 24 :
 I1I11I1I11iII ( oO0o0 )
 if 12 - 12: ooOoO0O00
elif I1iii11 == 25 :
 IiI1i11i ( oO0o0 )
 if 99 - 99: IIiIiII11i - Ii1I * OOoOoo
elif I1iii11 == 26 :
 II1iIii1Ii ( oO0o0 )
 if 3 - 3: OOoOoo - Ii1I * OooOO000 * Ii1I + I1ii11iIi11i
elif I1iii11 == 27 :
 OOooiii1I ( oO0o0 )
 if 15 - 15: Ii1I * iIi1i1ii1 / OooOO000 . I11i / iIi1i1ii1 % OOooOOo
elif I1iii11 == 28 :
 I1ioooOooo00O0 ( oO0o0 )
 if 75 - 75: ii % Ii % iI11I1II1I1I % Ii1I / Ii
elif I1iii11 == 29 :
 I1III1i1Ii ( oO0o0 )
 if 96 - 96: IIiIi1iI * oo0oO00 / iI11I1II1I1I / iiII11i1I1IIi
elif I1iii11 == 30 :
 iiiIi1II1III ( oO0o0 )
 if 5 - 5: I11i
elif I1iii11 == 31 :
 IiIIIii1iIII1 ( oO0o0 )
 if 83 - 83: iiII11i1I1IIi * oOo0O0Ooo . IIiIiII11i * ooOoO0O00 % o0o00Oo0O
elif I1iii11 == 32 :
 Iii1IIII11I ( )
 if 35 - 35: OOooOOo % oO0o + o0o00Oo0O * I11i % Ii1I
elif I1iii11 == 33 :
 O00O ( )
 if 57 - 57: oo0oO00 / iiII11i1I1IIi
elif I1iii11 == 35 :
 oOo00o ( oO0o0 )
 if 63 - 63: IIiIi1iI * oO0o * IIiIi1iI + OOooOOo
elif I1iii11 == 34 :
 II1 ( oO0o0 )
 if 25 - 25: OooOO000 * OOooOOo / oOo0O0Ooo / OOoOoo
elif I1iii11 == 36 :
 O0000oO0o00 ( oO0o0 )
 if 11 - 11: IIi + Ii
elif I1iii11 == 37 :
 oO0O0o0o00 ( oO0o0 )
 if 14 - 14: OOooOOo / OOoOoo + oO0o - iIi1i1ii1
elif I1iii11 == 38 :
 I111iiiii1 ( oO0o0 )
 if 38 - 38: O00OOo00oo0o
elif I1iii11 == 41 :
 i11i1ii1I ( o0OO0o0o00o )
 if 30 - 30: IIiIiII11i + iiII11i1I1IIi . Ii + iI11I1II1I1I
elif I1iii11 == 39 :
 OOOoo0OO ( oO0o0 )
 if 100 - 100: oo0oO00 * I11i / OooOO000
elif I1iii11 == 45 :
 TEXTS ( )
 if 92 - 92: IIiIi1iI / Ii * IIi
elif I1iii11 == 46 :
 iI1Ii11iIiI1 ( )
 if 55 - 55: IIiIi1iI
elif I1iii11 == 47 :
 GEVID ( )
 if 1 - 1: oO0o
elif I1iii11 == 48 :
 i11I1IIiiii ( I1111i , oO0o0 , I11o0oO00oO0o0o0 )
 if 43 - 43: iI11I1II1I1I - IIi - I11i + Ii1I - O00OOo00oo0o % Ii1I
elif I1iii11 == 49 :
 iI1i111I1Ii ( )
 if 58 - 58: OOooOOo
elif I1iii11 == 22222 :
 ooo0O0OO ( oO0o0 )
 if 27 - 27: OOoOoo * IIi - ii . iIi1i1ii1 - IIiIiII11i
elif I1iii11 == 222 :
 OOOOOo00o0o ( oO0o0 )
 if 62 - 62: oOo0O0Ooo / iI11I1II1I1I * iiII11i1I1IIi
elif I1iii11 == 2222222 :
 OOoo00OOoo ( oO0o0 )
 if 84 - 84: OOoOoo - OOooOOo . OOoOoo + IIiIi1iI . OooOO000
elif I1iii11 == 222222 :
 ooOoOoo ( oO0o0 , I1111i )
 if 96 - 96: iIi1i1ii1 % OooOO000 * iIi1i1ii1 % oOo0O0Ooo . I11i / I11i
elif I1iii11 == 333 :
 i1iI1iIIiIi1I ( oO0o0 )
 if 7 - 7: oO0o - IIiIi1iI % ooOoO0O00
 if 24 - 24: oO0o % o0o00Oo0O % iiII11i1I1IIi
elif I1iii11 == 1020 :
 o0ooo0 ( )
 if 61 - 61: IIiIi1iI . OooOO000 / IIiIi1iI * ii
elif I1iii11 == 1021 :
 ANIMEEP ( )
 if 13 - 13: IIiIiII11i
elif I1iii11 == 1022 :
 ANIMEPLAY ( oO0o0 )
 if 17 - 17: IIiIiII11i
elif I1iii11 == 1001 :
 OOOOo00oOOO00 ( )
 if 66 - 66: OOoOoo * oo0oO00
elif I1iii11 == 1005 :
 OOoo000OO00 ( )
 if 73 - 73: Ii + o0o00Oo0O % o0o00Oo0O
elif I1iii11 == 1007 :
 O000oo0O0OO0 ( oO0o0 )
 if 70 - 70: IIiIiII11i * ii - iIi1i1ii1 + oo0oO00 * o0o00Oo0O
elif I1iii11 == 1010 :
 oooOo ( oO0o0 )
 if 49 - 49: oo0oO00 . iIi1i1ii1 . OOooOOo - Ii1I
elif I1iii11 == 1011 :
 OoOOOO0ooO0 ( oO0o0 )
 if 74 - 74: IIiIi1iI % Ii1I * ooOoO0O00
elif I1iii11 == 1012 :
 OoOo0O0O ( oO0o0 )
 if 18 - 18: OOooOOo
elif I1iii11 == 1030 :
 oOOooo0O ( )
 if 30 - 30: IIiIiII11i
elif I1iii11 == 1031 :
 O0O000 ( oO0o0 , I1ii1ii11i1I )
 if 27 - 27: ooOoO0O00 - iI11I1II1I1I + o0o00Oo0O % I1ii11iIi11i / IIi + ooOoO0O00
elif I1iii11 == 1032 :
 iii1i11 ( oO0o0 )
 if 48 - 48: I1ii11iIi11i
elif I1iii11 == 1006 :
 Parse . ParseURL ( oO0o0 )
 if 70 - 70: ii * Ii
elif I1iii11 == 2030 :
 Parse . addonParseURL ( oO0o0 )
 if 60 - 60: OOoOoo / iI11I1II1I1I + ii - Ii1I * Ii
elif I1iii11 == 2031 :
 Parse . apkParseURL ( oO0o0 )
 if 47 - 47: o0o00Oo0O . oOo0O0Ooo / IIiIi1iI % Ii
elif I1iii11 == 1002 :
 IiI1I ( oO0o0 )
 if 47 - 47: iIi1i1ii1 . OOooOOo . iI11I1II1I1I . I11i
elif I1iii11 == 1003 :
 o0o0OoOOOoo ( oO0o0 , I1ii1ii11i1I )
 if 39 - 39: I11i
elif I1iii11 == 1004 :
 oo0O0O000O0oO ( oO0o0 )
 if 89 - 89: ii + OooOO000 . O00OOo00oo0o / iIi1i1ii1
elif I1iii11 == 1008 :
 oO00 ( )
 if 75 - 75: iI11I1II1I1I * OooOO000 / OOooOOo * IIiIiII11i . ooOoO0O00
elif I1iii11 == 1009 :
 I11Iii11i1Ii ( oO0o0 )
 if 6 - 6: iIi1i1ii1 % iIi1i1ii1 / ii * oo0oO00 . oOo0O0Ooo . ooOoO0O00
elif I1iii11 == 2001 :
 i1Iooo ( )
 if 59 - 59: iiII11i1I1IIi . iiII11i1I1IIi * oOo0O0Ooo - iIi1i1ii1 % OOooOOo
elif I1iii11 == 2002 :
 ooooOoo ( oO0o0 )
 if 19 - 19: ii / I1ii11iIi11i - O00OOo00oo0o . OOooOOo
elif I1iii11 == 1013 :
 OoO0oO ( )
elif I1iii11 == 10111113 :
 i111i1iIi1 ( oO0o0 )
 if 8 - 8: iiII11i1I1IIi % IIiIi1iI . iI11I1II1I1I
elif I1iii11 == 1014 :
 Ii1i1ii ( )
 if 95 - 95: I11i + Ii . Ii1I . IIiIi1iI . I11i
elif I1iii11 == 1015 :
 ooO ( oO0o0 )
 if 93 - 93: OooOO000
elif I1iii11 == 1016 :
 Iiii1iI1i ( oO0o0 , I1ii1ii11i1I , I1111i )
 if 55 - 55: IIiIiII11i % I11i - oO0o
elif I1iii11 == 1017 :
 O0OoOO0oo0 ( )
 if 48 - 48: IIiIi1iI * iI11I1II1I1I % OOooOOo
elif I1iii11 == 1018 :
 oOOO00o000o ( oO0o0 )
 if 100 - 100: IIiIiII11i - Ii + oO0o % IIiIi1iI - iI11I1II1I1I * Ii
elif I1iii11 == 1023 :
 oOO ( )
 if 30 - 30: oO0o . oO0o . iIi1i1ii1 % iIi1i1ii1 * ooOoO0O00 * oo0oO00
elif I1iii11 == 1024 :
 oOii1iiiiii ( oO0o0 )
 if 74 - 74: ii
elif I1iii11 == 1025 :
 OOOoO0o ( oO0o0 )
 if 33 - 33: I11i - IIiIiII11i
elif I1iii11 == 4001 :
 iiIi11iI1iii ( )
 if 95 - 95: ii
elif I1iii11 == 4002 :
 OOOooo ( )
 if 23 - 23: IIiIiII11i + iiII11i1I1IIi / o0o00Oo0O . iiII11i1I1IIi . O00OOo00oo0o + iI11I1II1I1I
elif I1iii11 == 4003 :
 i11I1I ( )
 if 2 - 2: ooOoO0O00 . o0o00Oo0O / I11i . IIiIiII11i / oO0o % ooOoO0O00
elif I1iii11 == 4004 :
 OO0 ( )
 if 12 - 12: I11i
elif I1iii11 == 4005 :
 o0Oooo ( )
 if 58 - 58: iI11I1II1I1I * iIi1i1ii1 . IIiIi1iI . I1ii11iIi11i * iIi1i1ii1
elif I1iii11 == 4006 :
 iIi1Ii1i1iI ( )
 if 63 - 63: OOooOOo . iiII11i1I1IIi * I11i - iiII11i1I1IIi % iiII11i1I1IIi
elif I1iii11 == 4007 :
 oOIIiIi ( )
 if 62 - 62: iiII11i1I1IIi - IIiIi1iI / IIiIi1iI
elif I1iii11 == 4008 :
 o0OoOO ( )
 if 95 - 95: OOooOOo - ooOoO0O00 / O00OOo00oo0o . IIiIi1iI % IIi - ooOoO0O00
elif I1iii11 == 4009 : Iii ( )
elif I1iii11 == 4010 : o00Ooo0 ( )
elif I1iii11 == 3000 :
 I11IiOO ( )
 if 12 - 12: OooOO000
elif I1iii11 == 3001 :
 OoO0oOOOO ( )
 if 96 - 96: o0o00Oo0O
elif I1iii11 == 3002 :
 o0oo00OOOo ( oO0o0 )
 if 89 - 89: Ii1I - I1ii11iIi11i
elif I1iii11 == 3003 :
 oo0oOi1i1IIi ( oO0o0 )
 if 26 - 26: IIiIi1iI % IIiIi1iI / IIiIiII11i / OooOO000
elif I1iii11 == 3004 :
 o0OOoO ( oO0o0 )
 if 2 - 2: ooOoO0O00 / Ii + oOo0O0Ooo
elif I1iii11 == 404 :
 i1IiIiIii11I ( I1111i , oO0o0 , I1ii1ii11i1I )
 if 95 - 95: Ii1I / OOoOoo % iI11I1II1I1I + o0o00Oo0O
elif I1iii11 == 405 :
 oOoO000OOoo0 ( oO0o0 )
 if 6 - 6: OOoOoo
elif I1iii11 == 7030 :
 oooo0OoOO ( )
 if 73 - 73: I11i % I11i . IIi * Ii1I - iIi1i1ii1
elif I1iii11 == 7021 :
 Iii1iIII1Iii ( I1111i )
 if 97 - 97: OOoOoo
elif I1iii11 == 7022 :
 O0OOoo ( I1111i )
 if 15 - 15: o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . O00OOo00oo0o
elif I1iii11 == 7000 :
 IiIoO0oo0 ( I1111i , oO0o0 , img )
 if 64 - 64: IIiIi1iI / ooOoO0O00
elif I1iii11 == 7050 :
 IiiI1iiI1III1i ( oO0o0 )
 if 100 - 100: IIiIiII11i
elif I1iii11 == 7051 :
 i1IIi1ii1i1ii ( oO0o0 )
 if 16 - 16: iIi1i1ii1
elif I1iii11 == 7052 :
 OO00OoO ( oO0o0 )
 if 96 - 96: I11i / O00OOo00oo0o % iIi1i1ii1 - IIiIi1iI
elif I1iii11 == 7053 :
 IIii ( oO0o0 )
 if 35 - 35: IIi
elif I1iii11 == 7054 :
 CoolPlay ( oO0o0 )
 if 90 - 90: Ii
elif I1iii11 == 7060 :
 OO0I11IIi1I1 ( )
 if 47 - 47: oO0o . Ii
elif I1iii11 == 7061 :
 ooooO0oOoOOoO ( oO0o0 )
 if 9 - 9: OOooOOo - iiII11i1I1IIi . ii % IIiIi1iI
elif I1iii11 == 7063 :
 Iiiii ( oO0o0 )
 if 13 - 13: oO0o * iI11I1II1I1I + IIiIiII11i - I1ii11iIi11i - OOooOOo
elif I1iii11 == 7062 :
 i1II11III ( oO0o0 )
 if 43 - 43: OooOO000 / O00OOo00oo0o * oOo0O0Ooo % IIiIi1iI % oOo0O0Ooo
elif I1iii11 == 7064 :
 NATatozcat ( )
 if 18 - 18: oO0o
elif I1iii11 == 7067 :
 O0OO0oo ( oO0o0 )
 if 99 - 99: OooOO000 / oo0oO00 . Ii / iiII11i1I1IIi + ooOoO0O00 - iiII11i1I1IIi
elif I1iii11 == 7066 :
 NATatozA ( oO0o0 )
 if 50 - 50: ooOoO0O00
elif I1iii11 == 7065 :
 II111IiiIIi ( oO0o0 )
 if 56 - 56: oO0o + O00OOo00oo0o / iIi1i1ii1
elif I1iii11 == 7070 :
 OoO0 ( )
 if 75 - 75: OOooOOo
elif I1iii11 == 7071 :
 DIZIlist ( oO0o0 )
 if 96 - 96: I11i * iiII11i1I1IIi * I1ii11iIi11i
elif I1iii11 == 7072 :
 DIZIpull ( oO0o0 )
 if 36 - 36: ii + IIiIi1iI . oo0oO00 * IIiIi1iI + OOoOoo
elif I1iii11 == 7073 :
 WATCHDIZI ( oO0o0 )
 if 45 - 45: oo0oO00 / OooOO000 + Ii1I - I1ii11iIi11i - IIiIi1iI . iI11I1II1I1I
elif I1iii11 == 7002 :
 iiiiIIii1I ( )
 if 52 - 52: oOo0O0Ooo + ooOoO0O00 . OooOO000 * oOo0O0Ooo
elif I1iii11 == 7003 :
 oOoO0O0o ( oO0o0 )
 if 31 - 31: I1ii11iIi11i % iI11I1II1I1I . o0o00Oo0O
elif I1iii11 == 7004 :
 ii1i11iiII ( oO0o0 )
 if 80 - 80: iiII11i1I1IIi / I1ii11iIi11i + Ii1I
elif I1iii11 == 7020 :
 I1i1I1i1i1 ( oO0o0 )
 if 18 - 18: IIiIiII11i - OooOO000 / iI11I1II1I1I % OOooOOo % Ii1I / I11i
elif I1iii11 == 7001 :
 oO00O0 ( )
 if 47 - 47: IIi
elif I1iii11 == 7010 :
 IiiIIiiI1I11 ( oO0o0 )
 if 24 - 24: iIi1i1ii1 % I11i
elif I1iii11 == 7011 :
 I1i1 ( oO0o0 )
 if 87 - 87: I11i % OooOO000 / IIiIi1iI - OOoOoo + Ii
elif I1iii11 == 7012 :
 i1111II1iIII ( oO0o0 )
 if 85 - 85: ii * OOoOoo . IIi / OooOO000 / ii
elif I1iii11 == 7013 :
 cnfTVPlay2 ( oO0o0 )
elif I1iii11 == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oO0o0 )
elif I1iii11 == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oO0o0 )
elif I1iii11 == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( I1111i , oO0o0 , I1ii1ii11i1I )
elif I1iii11 == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif I1iii11 == 7018 :
 O00OO0o0oO0 ( )
elif I1iii11 == 7019 :
 CNF_Studio_Indexer . List_Movies ( oO0o0 )
elif I1iii11 == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oO0o0 )
elif I1iii11 == 7024 :
 CNF_Studio_Indexer . Box_Office ( oO0o0 )
 if 87 - 87: oO0o
elif I1iii11 == 8000 :
 oO0ooo00OoOooooo ( )
elif I1iii11 == 8001 :
 ooo0oOoO00Oo ( )
elif I1iii11 == 8002 :
 IIIII11 ( )
elif I1iii11 == 8003 :
 iIIiiIiII1i ( )
elif I1iii11 == 8004 :
 OooooOOOO ( )
elif I1iii11 == 8005 :
 o0o0O0o0O ( )
elif I1iii11 == 8006 :
 IiiiI1i ( I1111i , oO0o0 )
elif I1iii11 == 8030 :
 oO0oo0o00o0O ( oO0o0 )
elif I1iii11 == 8045 :
 O00000OO00OO ( oO0o0 )
elif I1iii11 == 8046 :
 iI11iI ( oO0o0 )
elif I1iii11 == 8047 :
 OoiiI11111II ( oO0o0 )
elif I1iii11 == 8048 :
 OoooOOOOo ( oO0o0 )
elif I1iii11 == 8049 :
 I1i1Ii1i11ii ( oO0o0 )
elif I1iii11 == 804900 :
 oO0O0oo ( oO0o0 )
elif I1iii11 == 8020 :
 IiIi1I1ii111 ( )
elif I1iii11 == 8021 :
 OOOo0oo0 ( oO0o0 )
elif I1iii11 == 8022 :
 i1I1I1 ( oO0o0 )
elif I1iii11 == 8023 :
 i11i ( oO0o0 )
elif I1iii11 == 8040 :
 oOoO00o ( )
elif I1iii11 == 8041 :
 IiOOo0 ( oO0o0 )
elif I1iii11 == 8042 :
 oooOo00 ( oO0o0 )
elif I1iii11 == 8043 :
 yt . PlayVideo ( oO0o0 )
elif I1iii11 == 8044 :
 iII1II ( oO0o0 )
elif I1iii11 == 8060 :
 OOOOO0O00 ( )
elif I1iii11 == 8061 :
 oOoO0O00o ( oO0o0 )
elif I1iii11 == 8064 :
 IiIiIi ( )
elif I1iii11 == 8065 :
 OO0Iii1iIiI111Ii ( oO0o0 )
elif I1iii11 == 8070 :
 o0OoOo0o0OOoO0 ( )
elif I1iii11 == 8071 :
 i1I1IIIiii1 ( oO0o0 )
elif I1iii11 == 7080 :
 oOO0 ( oO0o0 )
elif I1iii11 == 8090 :
 iIi11I1II ( )
elif I1iii11 == 8091 :
 I1iIi1IiI1i ( oO0o0 )
elif I1iii11 == 8092 :
 IiIi11IIi1I11 ( oO0o0 )
elif I1iii11 == 8093 :
 IiiIiiiiI1III ( oO0o0 )
elif I1iii11 == 8081 :
 ii1I1IIII11ii ( )
elif I1iii11 == 8062 :
 i1I1IiIiiI1II ( oO0o0 )
elif I1iii11 == 8063 :
 ooooooo ( oO0o0 )
elif I1iii11 == 8050 :
 I1IIiiII ( )
elif I1iii11 == 8051 :
 oOOO0oOoo ( oO0o0 )
elif I1iii11 == 8052 :
 o0O0ooooooo00 ( oO0o0 )
elif I1iii11 == 8085 :
 OOoo ( )
elif I1iii11 == 8086 :
 OoOo0O0 ( oO0o0 )
elif I1iii11 == 8087 :
 iiI1i ( oO0o0 )
elif I1iii11 == 8088 :
 o0O00o0 ( oO0o0 , I1111i )
elif I1iii11 == 9000 :
 I1oOooo00O ( )
elif I1iii11 == 1111 :
 oo0oo0O0 ( )
elif I1iii11 == 9001 :
 iiIII1i ( )
elif I1iii11 == 9002 :
 iiiI ( )
elif I1iii11 == 9003 :
 III11i ( )
elif I1iii11 == 9004 :
 World1 ( )
elif I1iii11 == 9005 :
 World2 ( oO0o0 )
elif I1iii11 == 9006 :
 World3 ( oO0o0 )
elif I1iii11 == 9007 :
 iIIIIi ( )
elif I1iii11 == 9008 :
 iiIIOo0Ooo ( oO0o0 )
elif I1iii11 == 9009 :
 II1iII11 ( oO0o0 )
elif I1iii11 == 9010 :
 i1iIIi ( )
elif I1iii11 == 9011 :
 oo0O0OO0Oooo ( oO0o0 )
elif I1iii11 == 50 :
 i1i1iiIIiiiII ( oO0o0 )
elif I1iii11 == 9020 :
 champlist ( )
elif I1iii11 == 9021 :
 i1Ii111 ( )
elif I1iii11 == 9022 :
 OO0o0o0OOoooo ( )
elif I1iii11 == 9023 :
 oOO00OOOO0o ( )
elif I1iii11 == 9024 :
 oo0oO0o00Oo0 ( oO0o0 )
elif I1iii11 == 9030 :
 IiI111i ( oO0o0 )
elif I1iii11 == 9031 :
 IiI1ii1 ( oO0o0 )
elif I1iii11 == 9032 :
 OOO00oo0 ( oO0o0 )
elif I1iii11 == 9033 :
 o0ooOooO0o ( oO0o0 )
elif I1iii11 == 9034 :
 IIi1IIIi ( )
elif I1iii11 == 7085 :
 OoOOOoo ( oO0o0 )
elif I1iii11 == 7086 :
 I1Ii11I1i1iii ( oO0o0 )
elif I1iii11 == 7087 :
 i1Ii ( I11o0oO00oO0o0o0 )
elif I1iii11 == 9666 :
 I1iIIiiIIi1i ( oO0o0 )
elif I1iii11 == 10100 : oooO ( )
elif I1iii11 == 101001 : o00000O ( oO0o0 )
elif I1iii11 == 10105 : i1iiIIiiiI ( oO0o0 )
elif I1iii11 == 10106 : I1IIiIi1iI ( oO0o0 )
elif I1iii11 == 10104 : Ii1iiIIIiI ( oO0o0 )
elif I1iii11 == 10107 : iIiiiII11 ( )
elif I1iii11 == 10103 : oOo0Iiii11 ( oO0o0 )
elif I1iii11 == 10108 : OoiIIii1Ii1 ( oO0o0 )
elif I1iii11 == 10000 : Origin_Menu ( )
elif I1iii11 == 10001 : oO0o000OoOoO0 ( )
elif I1iii11 == 10002 : iiI ( )
elif I1iii11 == 10003 : O0O0Oo00 ( )
elif I1iii11 == 10004 : Ooo0o0oo ( oO0o0 )
elif I1iii11 == 10005 : o0oO0oOO ( )
elif I1iii11 == 10006 : ooo0OO0OOooO0 ( oO0o0 )
elif I1iii11 == 10007 : ooOO0OOO00o ( oO0o0 , I1ii1ii11i1I )
elif I1iii11 == 10008 : iii1IiII ( )
elif I1iii11 == 10009 : iII1i1 ( )
elif I1iii11 == 10010 : o0o000OOOO ( oO0o0 )
elif I1iii11 == 10011 : IiiII1I ( oO0o0 )
elif I1iii11 == 10012 : OOOOo0o00OO0000 ( oO0o0 )
elif I1iii11 == 10109 : O0OOo00OO ( oO0o0 )
elif I1iii11 == 10013 : oOiiI1i11I ( oO0o0 )
elif I1iii11 == 10014 : OOO00000o0 ( )
elif I1iii11 == 10015 : OO0o0OO0 ( )
elif I1iii11 == 10016 : II1Ii11Ii1i1I ( oO0o0 )
elif I1iii11 == 10017 : i1iiIo0o ( )
elif I1iii11 == 10018 : iIi11III ( )
elif I1iii11 == 10019 : IIi1II ( )
elif I1iii11 == 10020 : iIiII1iiiiI ( )
elif I1iii11 == 10021 : oo0OO0o0o0ooO0ooo ( )
elif I1iii11 == 10022 : I11iIiI1 ( oO0o0 )
elif I1iii11 == 10023 : o00iIiI1iI1Ii1 ( I1111i , oO0o0 )
elif I1iii11 == 10024 : iiI111i1 ( oO0o0 )
elif I1iii11 == 10025 : II1iiiiII ( )
elif I1iii11 == 10026 : O0o0 ( )
elif I1iii11 == 10027 : oooOoOoOO ( )
elif I1iii11 == 10028 : O00oO0O ( )
elif I1iii11 == 10029 : OOo0OOoo00 ( )
elif I1iii11 == 423 : oooO0o0oOoO ( oO0o0 )
elif I1iii11 == 426 : OooO00oo0O0 ( oO0o0 )
elif I1iii11 == 10030 : Izle_Films ( )
elif I1iii11 == 10031 : Latest_Izle_Movies ( )
elif I1iii11 == 10032 : Izle_Genres ( )
elif I1iii11 == 10033 : Izle_Pop_Movies ( )
elif I1iii11 == 10034 : Izle_Boxsets ( )
elif I1iii11 == 10035 : Izle_Search ( )
elif I1iii11 == 10036 : Izle_Genres_Movie ( oO0o0 )
elif I1iii11 == 10037 : Izle_Boxset_single ( oO0o0 )
elif I1iii11 == 10038 : Izle_IFRAME ( )
elif I1iii11 == 10039 : Izle_Boxsets_Next ( oO0o0 )
elif I1iii11 == 10040 : Oo0o0000OOoO ( )
elif I1iii11 == 10041 : O0OOOOoO00oo ( oO0o0 )
elif I1iii11 == 10042 : II1iOOoOooO0o ( oO0o0 )
elif I1iii11 == 10043 : O0o00ooo ( )
elif I1iii11 == 10044 : IiiII ( oO0o0 )
elif I1iii11 == 10045 : IIioo0 ( I1111i )
elif I1iii11 == 10046 : iIiI1111 ( oO0o0 )
elif I1iii11 == 10047 : i1i1i11iI11II ( oO0o0 )
elif I1iii11 == 10048 : I1I1ii1111 ( oO0o0 )
elif I1iii11 == 10049 : i1ii11I111Ii ( oO0o0 )
elif I1iii11 == 10050 : iI1i11iII111 ( )
elif I1iii11 == 10051 : ii1Ii ( )
elif I1iii11 == 10052 : iiI11Ii1 ( )
elif I1iii11 == 10053 : Addon ( oO0o0 )
elif I1iii11 == 10054 : IIIiIIi111 ( oO0o0 , I1111i )
elif I1iii11 == 10055 :
 O0o0O0O0O ( "addFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiiII1i1I ( I1111i , oO0o0 , I1ii1ii11i1I , o0ooooO0o0O , o0oo00 )
elif I1iii11 == 10056 :
 O0o0O0O0O ( "rmFavorite" )
 try :
  I1111i = I1111i . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  I1111i = I1111i . split ( '  - ' ) [ 0 ]
 except :
  pass
 O0OOOOOO0ooO ( I1111i )
elif I1iii11 == 10057 :
 O0o0O0O0O ( "getFavorites" )
 iI1Ii11 ( )
elif I1iii11 == 10058 : iIIiIiI1I1 ( )
elif I1iii11 == 10059 : Donators_Guide ( )
elif I1iii11 == 10060 : oo000o0000oO ( )
elif I1iii11 == 10061 : o0i1I11iI1iiI ( )
elif I1iii11 == 10062 : iiiiii1 ( I1111i , oO0o0 , I11o0oO00oO0o0o0 )
elif I1iii11 == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
elif I1iii11 == 10064 : Ii1iIi111I1i ( )
elif I1iii11 == 10065 : o000o0O0Oo00 ( oO0o0 )
elif I1iii11 == 10066 : I1Iiii ( oO0o0 )
elif I1iii11 == 10068 : IiIi ( oO0o0 )
elif I1iii11 == 10069 : IIIII1 ( oO0o0 )
elif I1iii11 == 10070 : O00OO0o0 ( oO0o0 )
elif I1iii11 == 10071 : Genie_Watch ( )
elif I1iii11 == 10072 : ooOoO ( )
elif I1iii11 == 10073 : Oo0o ( oO0o0 )
elif I1iii11 == 10074 : i1iiIIIi ( oO0o0 )
elif I1iii11 == 10075 : O00oOoo0OoO0 ( I1ii1ii11i1I , I1111i , oO0o0 )
elif I1iii11 == 10076 : Ii1 ( oO0o0 )
elif I1iii11 == 10077 : ooO0o0oO ( oO0o0 )
elif I1iii11 == 10078 : iIiiIiiIi ( )
elif I1iii11 == 10079 : Genie_Watch_Tv_Shows ( )
elif I1iii11 == 10080 : Genie_Watch_Tv_Genre ( oO0o0 )
elif I1iii11 == 10081 : Genie_Watch_TV_PlayRun ( oO0o0 )
elif I1iii11 == 10082 : Genie_Watch_TV_Episodes ( oO0o0 , I1ii1ii11i1I )
elif I1iii11 == 10083 : Genie_Watch_Tv_Recent ( oO0o0 )
elif I1iii11 == 10084 : OO0oOOoo ( )
elif I1iii11 == 10085 : Iiii1i1 ( )
elif I1iii11 == 10086 : II1I ( )
elif I1iii11 == 20000 : OO0ooOOO0O00o ( )
elif I1iii11 == 20001 : I11IIII1111II ( oO0o0 )
elif I1iii11 == 20002 : o0o00OOOO ( oO0o0 )
elif I1iii11 == 20003 : i1iIIiI1111 ( oO0o0 )
elif I1iii11 == 20004 : I1iIiIii ( oO0o0 )
elif I1iii11 == 20005 : i1iiI1i ( oO0o0 )
elif I1iii11 == 21004 : O000o0 ( )
elif I1iii11 == 21005 : O00oo0O00 ( oO0o0 )
elif I1iii11 == 21006 : OOO0OoO0oo0OO ( oO0o0 )
elif I1iii11 == 21007 : ii1III1iiIi ( oO0o0 )
elif I1iii11 == 30000 : IiIIiiI ( )
elif I1iii11 == 30001 : iI11II1i1I1 ( )
elif I1iii11 == 10012 : Resolve ( oO0o0 )
elif I1iii11 == 30003 : IIIiIi1iiI ( )
elif I1iii11 == 30004 : I1i1I ( oO0o0 )
elif I1iii11 == 30005 : i11Ii1iIIIIi ( oO0o0 )
elif I1iii11 == 30006 : ooO0 ( )
elif I1iii11 == 30007 : OoOoIiI1 ( )
elif I1iii11 == 30008 : I1i1I11111iI1 ( oO0o0 )
elif I1iii11 == 30009 : I1iI1I1ii1 ( oO0o0 )
elif I1iii11 == 30010 : oo00ooooOOo00 ( oO0o0 )
elif I1iii11 == 30011 : oo0o00OO ( )
elif I1iii11 == 30012 : ooOOO00oOOooO ( )
elif I1iii11 == 30013 : oOooOOo00ooO ( )
elif I1iii11 == 30014 : iiii1 ( )
elif I1iii11 == 30015 : o0oOoOo0 ( oO0o0 , I1ii1ii11i1I , o0ooooO0o0O )
elif I1iii11 == 30016 : o0OOOOOo0 ( oO0o0 )
elif I1iii11 == 30019 : IiI11I111 ( oO0o0 )
elif I1iii11 == 30017 : Iiii1Ii ( oO0o0 )
elif I1iii11 == 30018 : o0o000Oo ( oO0o0 )
elif I1iii11 == 30030 : iIi11iI1i ( )
elif I1iii11 == 30031 : OoOo ( )
elif I1iii11 == 30032 : OOoOooOoOOOoo ( )
elif I1iii11 == 30033 : Ii1iIi ( )
elif I1iii11 == 30034 : OOo0OOOoOOo ( )
elif I1iii11 == 30035 : oOo0I1Ii11i ( oO0o0 )
elif I1iii11 == 30036 : I1iIiiiI1 ( oO0o0 )
elif I1iii11 == 30037 : OOO0O00Oo ( oO0o0 )
elif I1iii11 == 30038 : III1III11II ( )
elif I1iii11 == 30039 : OooOoOO0 ( )
elif I1iii11 == 50000 : oOOo0O00o ( )
elif I1iii11 == 50001 : OO00o0O0O000o ( )
elif I1iii11 == 50002 : iI1I1ii11IIi1 ( oO0o0 )
elif I1iii11 == 50003 : IIiIi ( I11o0oO00oO0o0o0 )
elif I1iii11 == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif I1iii11 == 60001 : Oo0 ( )
elif I1iii11 == 60002 : Oo ( I1111i )
elif I1iii11 == 60003 : iI1II1I1I ( I1111i )
elif I1iii11 == 50004 : iiIiIIIiiI ( )
elif I1iii11 == 50005 : speedtest . runtest ( oO0o0 )
elif I1iii11 == 70001 : oo0ooooo00o ( )
elif I1iii11 == 70002 : oooo ( oO0o0 )
elif I1iii11 == 70003 : o0o0oo0Ooo ( oO0o0 )
elif I1iii11 == 70004 : iI1ii11I ( oO0o0 )
elif I1iii11 == 70005 : o0oO0o0oo0O0 ( oO0o0 )
elif I1iii11 == 70006 : O0oo00oOOO0o ( )
elif I1iii11 == 50006 : OO0O000 ( i1 , i1111 )
elif I1iii11 == 80000 : i1iiI ( )
elif I1iii11 == 80001 : resolvefilmon ( oO0o0 )
elif I1iii11 == 80002 : OOooOooo0OOo0 ( )
elif I1iii11 == 80003 : OOoOOOO00 ( I1111i , oO0o0 , "None" )
elif I1iii11 == 80004 : i11IiI1iiI11 ( I1111i , oO0o0 )
elif I1iii11 == 80005 : I1i11i ( )
elif I1iii11 == 80006 : iIi1IIi1ii ( oO0o0 )
elif I1iii11 == 80007 : I11Ii ( oO0o0 )
elif I1iii11 == 80008 : iIiII ( )
elif I1iii11 == 80009 : o000OO00OoO00 ( )
elif I1iii11 == 80010 : O00o ( oO0o0 )
elif I1iii11 == 80011 : ii1oOO0000 ( oO0o0 )
elif I1iii11 == 80012 : iI ( )
elif I1iii11 == 90000 : I11iIi1i1I1i1 ( I1111i , oO0o0 )
elif I1iii11 == 90001 : Ii1I1I1i1Ii ( )
elif I1iii11 == 90002 : o0O0oo0OO0O ( )
elif I1iii11 == 90003 : o00OoOOoO ( oO0o0 )
elif I1iii11 == 90004 : iii1i1Iiiiiii ( oO0o0 )
elif I1iii11 == 90005 : OOoo0 ( oO0o0 )
elif I1iii11 == 90006 : Oo0o0oOo0oO ( oO0o0 )
elif I1iii11 == 90007 : i1iiiI1I ( oO0o0 )
elif I1iii11 == 90008 : o0Ooo ( oO0o0 )
elif I1iii11 == 90009 : Oo0Oo00O00o0 ( oO0o0 )
elif I1iii11 == 90010 : iiIiI1i1 ( )
elif I1iii11 == 90020 : OoO0o0OO ( )
elif I1iii11 == 90021 : hellyeah2 ( oO0o0 )
elif I1iii11 == 90022 : hellyeah3 ( oO0o0 )
elif I1iii11 == 90023 : IiIIIII11I ( )
elif I1iii11 == 90024 : iiIii1I ( oO0o0 )
elif I1iii11 == 90025 : i1I11iIiII ( oO0o0 )
if 32 - 32: Ii - OOooOOo * iiII11i1I1IIi . I1ii11iIi11i * IIiIi1iI
elif I1iii11 == 90030 : I11iII ( )
elif I1iii11 == 90031 : I1i1i1iii ( )
elif I1iii11 == 90032 : iIIii ( oO0o0 )
elif I1iii11 == 90033 : ii1iii1i ( oO0o0 )
elif I1iii11 == 90034 : ooO0O00Oo0o ( oO0o0 )
elif I1iii11 == 90035 : I1i ( oO0o0 )
elif I1iii11 == 90036 : oOO00O00o00 ( oO0o0 )
elif I1iii11 == 90039 : ooOo0 ( oO0o0 )
elif I1iii11 == 90037 : oO0OoO00o ( oO0o0 )
elif I1iii11 == 90038 : OooOO0o0 ( )
if 21 - 21: IIi
elif I1iii11 == 10090 : O00 ( )
elif I1iii11 == 10091 : OO0oo ( oO0o0 )
elif I1iii11 == 10092 : i1oo ( oO0o0 )
elif I1iii11 == 10093 : OoIi11ii1 ( oO0o0 , I1ii1ii11i1I )
elif I1iii11 == 10094 : i1IiiI1 ( oO0o0 , I1ii1ii11i1I )
if 11 - 11: oo0oO00 % Ii * o0o00Oo0O
elif I1iii11 == 90040 : I1I ( )
elif I1iii11 == 90041 : I1iII11iIII1i1I ( oO0o0 )
elif I1iii11 == 90042 : i1iIIi1I1I11 ( oO0o0 )
elif I1iii11 == 90043 : oO0oooooo ( oO0o0 )
elif I1iii11 == 90044 : ooOo ( oO0o0 )
elif I1iii11 == 90045 : OoOO0OOoo ( )
elif I1iii11 == 90046 : o0oO0OoO0 ( oO0o0 )
elif I1iii11 == 90050 : I1ii1 ( )
elif I1iii11 == 90051 : o0OO000ooOo ( oO0o0 )
elif I1iii11 == 90052 : IIIiiI1 ( oO0o0 )
elif I1iii11 == 90053 : IiIiiiiI1 ( oO0o0 )
elif I1iii11 == 90054 : OoOOo ( oO0o0 )
elif I1iii11 == 90055 : i1I1iIi1IiI ( )
if 28 - 28: O00OOo00oo0o / iI11I1II1I1I + IIi . Ii1I % IIi + oO0o
elif I1iii11 == 100001 : Stand_up ( )
if 79 - 79: oo0oO00
elif I1iii11 == 100003 : II1Ii11Ii1i1I ( oO0o0 )
elif I1iii11 == 100004 : II1i ( oO0o0 )
elif I1iii11 == 100005 : Resolve ( oO0o0 )
elif I1iii11 == 100008 : Search ( )
elif I1iii11 == 100007 : i1iIi ( oO0o0 )
elif I1iii11 == 100009 : yt . PlayVideo ( oO0o0 )
elif I1iii11 == 100010 : oOi11iI11iIiIi ( oO0o0 )
elif I1iii11 == 100100 : ii1Oo0000oOo ( I1ii1ii11i1I , oO0o0 , OOO0 )
elif I1iii11 == 100101 : ii1iI ( oO0o0 , I1111i , o0ooooO0o0O , OOO0 , I1ii1ii11i1I )
elif I1iii11 == 100102 : oO0o00oOOooO0 ( I1111i , oO0o0 , I1ii1ii11i1I , o0ooooO0o0O )
elif I1iii11 == 100106 : ooO0o ( oO0o0 , I1111i )
elif I1iii11 == 100107 : Oo0oOooo000OO ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
