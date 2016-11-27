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
IiiIII111iI = "3.3.1"
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
 o00o0 ( iiOOooooO0Oo )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OOiIiIIi1 ( )
 else :
  I1IIII1i ( '[COLOR' + II + ']TOOLS[/COLOR]' , '' , 90001 , oOOOo00O00oOo + 'tools.png' , O0o0Oo , '' )
  I1I11i ( '[COLOR' + II + ']CONTACT US[/COLOR]' , '' , 50006 , oOOOo00O00oOo + 'Contact-Us.png' , O0o0Oo , '' )
  I1I11i ( '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , oOOOo00O00oOo + 'settings.png' , O0o0Oo , '' )
  I1I11i ( '[COLOR' + II + ']Force Genie Update Kodi 16+[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVwby9yZXBvc2l0b3J5LkdlbmllVHYtMC4xLjAuemlw' ) , 10085 , oOOOo00O00oOo + 'GenieUpdate.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'My Build' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']WIZARD[/COLOR]' , str ( ooOO0O0ooOooO ) , 4001 , oOOOo00O00oOo + 'Wizard.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Streams' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4002 , oOOOo00O00oOo + 'Streams.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Tommys Sports[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Music' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']Music[/COLOR]' , str ( ooOO0O0ooOooO ) , 4003 , oOOOo00O00oOo + 'Music.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Builders Toolbox' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']BUILDERS TOOLBOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 32 , oOOOo00O00oOo + 'BuildersToolbox.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Source List' ) == 'true' :
   I1I11i ( '[COLOR' + II + ']SOURCE LIST[/COLOR]' , str ( ooOO0O0ooOooO ) , 46 , oOOOo00O00oOo + 'SoruceList.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Maintainance' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']MAINTENANCE[/COLOR]' , str ( ooOO0O0ooOooO ) , 3 , oOOOo00O00oOo + 'Maintenance.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Addons' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']ADDONS[/COLOR]' , '' , 10050 , oOOOo00O00oOo + 'Addons.png' , O0o0Oo , '' )
  if Ii1I1I1i1Ii ( ) == 'android' :
   I1IIII1i ( '[COLOR' + II + ']APK TOOL[/COLOR]' , str ( ooOO0O0ooOooO ) , 30039 , oOOOo00O00oOo + 'APKTools.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Rss Feed' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']GenieTv RSS Feed[/COLOR]' , str ( ooOO0O0ooOooO ) , 39 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def OOiIiIIi1 ( ) :
 I1IIII1i ( '[COLOR' + II + ']TOOLS[/COLOR]' , '' , 90001 , oOOOo00O00oOo + 'tools.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'My Build' ) == 'true' :
  I1IIII1i ( '[COLOR' + II + ']WIZARD[/COLOR]' , str ( ooOO0O0ooOooO ) , 4001 , oOOOo00O00oOo + 'Wizard.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Streams' ) == 'true' :
  I1IIII1i ( '[COLOR' + II + ']STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4002 , oOOOo00O00oOo + 'Streams.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Music' ) == 'true' :
  I1IIII1i ( '[COLOR' + II + ']Music[/COLOR]' , str ( ooOO0O0ooOooO ) , 4003 , oOOOo00O00oOo + 'Music.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Tommys Sports[/COLOR]' , '' , 90010 , oOOOo00O00oOo + 'tommys.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Maintainance' ) == 'true' :
  I1IIII1i ( '[COLOR' + II + ']MAINTENANCE[/COLOR]' , str ( ooOO0O0ooOooO ) , 3 , oOOOo00O00oOo + 'Maintenance.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def i11I1II1I11i ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + II + ']APK TOOL[/COLOR]' , '[COLOR' + II + ']ADDONS[/COLOR]' , '[COLOR' + II + ']BUILDERS TOOLBOX[/COLOR]' , '[COLOR' + II + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + II + ']CONTACT US[/COLOR]' , '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + II + ']SOURCE LIST[/COLOR]' , '[COLOR' + II + ']GUIDE SKINS[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  Iiii1i1 ( )
 if iI1i11iII111 == 1 :
  Iii1IIII11I ( )
 if iI1i11iII111 == 2 :
  OOOoo0OO ( )
 if iI1i11iII111 == 3 :
  oO0o0 ( )
 if iI1i11iII111 == 4 :
  iI1Ii11iIiI1 ( iiOOooooO0Oo )
 if iI1i11iII111 == 5 :
  OOooO0OOoo . ok ( i1 , i1111 )
 if iI1i11iII111 == 6 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if iI1i11iII111 == 7 :
  OO0Oooo0oOO0O ( )
 if iI1i11iII111 == 8 :
  o00O0 ( )
def o00O0 ( ) :
 iiOOooooO0Oo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , 'GuideSkins' + '.zip' )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( iiOOooooO0Oo , ii1 , o0oOoO00o )
 I1iIIiiIIi1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1iIIiiIIi1i
 print '======================================='
 extract . all ( ii1 , I1iIIiiIIi1i , o0oOoO00o )
 O0O0ooOOO ( iiOOooooO0Oo )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oOOo0O00o ( )
def iIiIi11 ( ) :
 OOO = iiiiI ( )
 oooOo0OOOoo0 = OOO . replace ( OooO0 , "" )
 if os . path . exists ( OOO ) or not OOO == False :
  OOoO = open ( OOO , mode = 'r' ) ; OO0O000 = OOoO . read ( ) ; OOoO . close ( )
  iiIiI1i1 ( "%s - %s" % ( i1 , oooOo0OOOoo0 ) , OO0O000 )
 else :
  wiz . LogNotify ( 'View Log' , 'No Log File Found!' )
def o00O0 ( ) :
 iiOOooooO0Oo = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , 'GuideSkins' + '.zip' )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( iiOOooooO0Oo , ii1 , o0oOoO00o )
 I1iIIiiIIi1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1iIIiiIIi1i
 print '======================================='
 extract . all ( ii1 , I1iIIiiIIi1i , o0oOoO00o )
 O0O0ooOOO ( iiOOooooO0Oo )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oOOo0O00o ( )
def oO0O00oOOoooO ( ) :
 I1I11i ( '[COLOR' + II + ']Todays Games[/COLOR]' , str ( ooOO0O0ooOooO ) , 90030 , oOOOo00O00oOo + 'tgames.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Tommys Replays[/COLOR]' , str ( ooOO0O0ooOooO ) , 90031 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , O0o0Oo , '' )
 if 46 - 46: oOo0O0Ooo - ii - iiII11i1I1IIi * IIiIiII11i
def I1i1I11I ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 IIIII11I1IiI = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for Oo0o0oooo0O0 , OooooOOoo0 in IIIII11I1IiI :
  iiIiI1i1 ( '[COLOR' + II + ']Tommys List[/COLOR]  ' + Oo0o0oooo0O0 , OooooOOoo0 )
def i1I1IiiIi1i ( ) :
 I1IIII1i ( '[COLOR' + II + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 IIIII11I1IiI = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 90032 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
def Ooo0OOoOoO0 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , oOo0OOoO0 , O0o0Oo , '' )
 for url in next :
  I1IIII1i ( ( '[COLOR' + II + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , oOOOo00O00oOo + 'NEXT.png' , O0o0Oo , '' )
def IIo0Oo0oO0oOO00 ( url ) :
 OoO000O0Oo = O000oo ( url )
 oo00OO0000oO = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 IIIII11I1IiI = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 for iiI11ii1I1 , url in i1I :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 for iiI11ii1I1 , url in I1II1 :
  I1I11i ( ( '[COLOR' + II + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
 for url in oo00OO0000oO :
  I1I11i ( ( '[COLOR' + II + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , oOOOo00O00oOo + 'tommysreplays.png' , O0o0Oo , '' )
  if 86 - 86: iI11I1II1I1I / OOooOOo . IIiIiII11i
def II1i111Ii1i ( url ) :
 if 'drive' in url :
  iii1 ( url )
 else :
  OoO000O0Oo = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( OoO000O0Oo )
  for url in IIIII11I1IiI :
   iii1 ( url )
def ooO0oooOO0 ( url ) :
 o0ooo0 = liveresolver . resolve ( url )
 oOOOoo00 = xbmcgui . ListItem ( path = o0ooo0 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOOoo00 )
def iiIiIIIiiI ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 iiI1IIIi = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiI1IIIi )
def iiiiI ( ) :
 II11IiIi11 = False
 if os . path . exists ( os . path . join ( OooO0 , 'xbmc.log' ) ) :
  II11IiIi11 = os . path . join ( OooO0 , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'kodi.log' ) ) :
  II11IiIi11 = os . path . join ( OooO0 , 'kodi.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'spmc.log' ) ) :
  II11IiIi11 = os . path . join ( OooO0 , 'spmc.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'tvmc.log' ) ) :
  II11IiIi11 = os . path . join ( OooO0 , 'tvmc.log' )
 return II11IiIi11
 if 7 - 7: oO0o . iIi1i1ii1 % oo0oO00 * IIiIi1iI + OOoOoo + O00OOo00oo0o
def IIIIiII1i ( url ) :
 if url == 'http://' : return False
 try :
  O0o0O00Oo0o0 = urllib2 . Request ( url )
  O0o0O00Oo0o0 . add_header ( 'User-Agent' , I1i1iiI1 )
  O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
  O00O0oOO00O00 . close ( )
 except Exception , i1II1 :
  return i1II1
 return True
 if 25 - 25: O00OOo00oo0o / iI11I1II1I1I % OooOO000
def IiiiiI1i1Iii ( ) :
 i1Oo00 = O000oo ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( i1Oo00 )
 if len ( IIIII11I1IiI ) > 0 :
  for iiI11ii1I1 , iiOOooooO0Oo , oo00oO0o , iiii111II in IIIII11I1IiI :
   I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 50005 , oo00oO0o , iiii111II , '' )
def I11iIiI1I1i11 ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + II + ']WIPE GENIE[/COLOR]' , '[COLOR' + II + ']Genie BUILDS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Wizard[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   OOoooO00o0oo0 ( )
  if iI1i11iII111 == 1 :
   O00O ( )
  if iI1i11iII111 == 2 :
   I1i11 ( IiIi1I1 )
  if iI1i11iII111 == 3 :
   IiIIi1 ( iiOOooooO0Oo )
 else :
  I1IIII1i ( '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 10060 , oOOOo00O00oOo + 'BackupMyBuild.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 49 , oOOOo00O00oOo + 'RestoreMyBuild.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']WIPE GENIE[/COLOR]' , str ( ooOO0O0ooOooO ) , 41 , oOOOo00O00oOo + 'WipeGenie.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']WISHES PC[/COLOR]' , str ( ooOO0O0ooOooO ) , 1 , oOOOo00O00oOo + 'WISHESPC.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Genie BUILDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 44 , oOOOo00O00oOo + 'GenieBuilds.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 47 - 47: I1ii11iIi11i * Ii1I + iI11I1II1I1I / O00OOo00oo0o / oO0o - ii
def iII1i11IIi1i ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if Ooo == '5knuckleshuffle' :
   I1IIII1i ( '[COLOR' + II + ']XVID[/COLOR]' , str ( ooOO0O0ooOooO ) , 10100 , oOOOo00O00oOo + 'Jizbox.png' , O0o0Oo , '' )
   I1IIII1i ( '[COLOR' + II + ']ADULT CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30033 , oOOOo00O00oOo + 'adu.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']FAVOURITES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10057 , oOOOo00O00oOo + 'Favourites.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 9000 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']G-Tv Live List[/COLOR]' , '' , 4009 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   I1I11i ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']STREAM CATEGORIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 90002 , oOOOo00O00oOo + 'cats.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']STREAM TEAM[/COLOR]' , str ( ooOO0O0ooOooO ) , 4006 , oOOOo00O00oOo + 'StreamTeam.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , oOOOo00O00oOo + 'bamf.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , O0o0Oo , '' )
 else :
  if Ooo == '5knuckleshuffle' :
   I1IIII1i ( '[COLOR' + II + ']XVID[/COLOR]' , str ( ooOO0O0ooOooO ) , 10100 , oOOOo00O00oOo + 'Jizbox.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']ADULT CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30033 , oOOOo00O00oOo + 'adu.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Favourites' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']FAVOURITES[/COLOR]' , str ( ooOO0O0ooOooO ) , 10057 , oOOOo00O00oOo + 'Favourites.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Search' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 9000 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']G-Tv Live List[/COLOR]' , '' , 4009 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
   I1I11i ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']STREAM TEAM[/COLOR]' , str ( ooOO0O0ooOooO ) , 4006 , oOOOo00O00oOo + 'StreamTeam.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 4004 , oOOOo00O00oOo + 'Movies.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4005 , oOOOo00O00oOo + 'TVShows.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']BAMF IPTV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , oOOOo00O00oOo + 'bamf.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' , '' , 9034 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']FOOTBALL[/COLOR]' , '' , 10002 , oOOOo00O00oOo + 'Football.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']KIDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 4007 , oOOOo00O00oOo + 'Kids.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']NEWS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30032 , oOOOo00O00oOo + 'News.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'GenieTVTutorials.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']HOBBIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 4008 , oOOOo00O00oOo + 'Hobbies.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Stand Up' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']STAND UP[/COLOR]' , '' , 10003 , oOOOo00O00oOo + 'StandUp.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 8040 , oOOOo00O00oOo + 'documentaries.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 7001 , oOOOo00O00oOo + 'DiscloseTV.png' , O0o0Oo , '' )
   if 73 - 73: I11i * o0o00Oo0O - Ii
   if 85 - 85: iIi1i1ii1 % OooOO000 + iiII11i1I1IIi / I11i . oo0oO00 + IIi
  I1IIII1i ( '[COLOR' + II + ']24/7 STREAMS[/COLOR]' , '' , 30030 , oOOOo00O00oOo + '247Streams.png' , O0o0Oo , '' )
  if 62 - 62: Ii + Ii - I11i
  if 28 - 28: OooOO000 . OooOO000 % iI11I1II1I1I * iI11I1II1I1I . I11i / OooOO000
  if 27 - 27: oO0o + IIiIi1iI - ooOoO0O00
  if 69 - 69: OOoOoo - o0o00Oo0O % Ii1I + Ii . OOooOOo / oO0o
  if 79 - 79: o0o00Oo0O * Ii - OOoOoo / OOoOoo
  if 48 - 48: o0o00Oo0O
  if 93 - 93: Ii - oOo0O0Ooo * Ii1I * iiII11i1I1IIi % o0o00Oo0O + ii
  if 25 - 25: OOoOoo + iIi1i1ii1 / IIiIi1iI . I11i % o0o00Oo0O * oO0o
  I1IIII1i ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , O0o0Oo , '' )
  if 84 - 84: IIiIi1iI % iIi1i1ii1 + Ii
  if 28 - 28: I1ii11iIi11i + oO0o * IIi % oo0oO00 . iiII11i1I1IIi % o0o00Oo0O
  if 16 - 16: iiII11i1I1IIi - iI11I1II1I1I / oOo0O0Ooo . IIiIiII11i + iI11I1II1I1I
  if 19 - 19: oO0o - I1ii11iIi11i . o0o00Oo0O
  if 60 - 60: IIiIiII11i + I1ii11iIi11i
  if 9 - 9: IIiIi1iI * ii - iI11I1II1I1I + OOooOOo / oO0o . oO0o
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def iiIIi ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']MOVIES[/COLOR]' , '[COLOR' + II + ']TV SHOWS[/COLOR]' , '[COLOR' + II + ']FOOTBALL[/COLOR]' , '[COLOR' + II + ']KIDS[/COLOR]' , '[COLOR' + II + ']NEWS[/COLOR]' , '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + II + ']HOBBIES[/COLOR]' , '[COLOR' + II + ']STAND UP[/COLOR]' , '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']CATEGORIES[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  iiI1iI111ii1i ( )
 if iI1i11iII111 == 1 :
  Ii1IIiI1IiIII ( )
 if iI1i11iII111 == 2 :
  OO0Oo000OOOoO ( )
 if iI1i11iII111 == 3 :
  O0i11I1I1I ( )
 if iI1i11iII111 == 4 :
  oOOOo00O00O ( )
 if iI1i11iII111 == 5 :
  iIIIII1I ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , ooI1i , iiI11ii1I1 )
 if iI1i11iII111 == 6 :
  iIII ( )
 if iI1i11iII111 == 7 :
  o0o0O ( )
 if iI1i11iII111 == 8 :
  ooooO0oOoOOoO ( )
 if iI1i11iII111 == 9 :
  I1i11i ( )
 if iI1i11iII111 == 10 :
  IiIi ( )
  if 87 - 87: Ii1I - Ii1I - OooOO000 + oo0oO00
  if 82 - 82: oo0oO00 / iI11I1II1I1I . oOo0O0Ooo . IIi / I11i
def ii1Ii11I ( ) :
 if not os . path . exists ( IIIII ) :
  iiIiI1i1 ( 'Change Log 27/11/16 - v3.3.1' , 'NEW SECTIONS ADDED, BAMFtv (FREE IPTV), ROADRUNNER and Technica Streams, QUICKSILVER music section has a major revamp, REAPER section back with force, Download option added, Search series fixed, Watch series under maintenance but back up(STILL), Scooby streams back up and running' )
  os . makedirs ( IIIII )
  if 42 - 42: I1ii11iIi11i
  if 19 - 19: oo0oO00 % Ii1I * iI11I1II1I1I + oOo0O0Ooo
def iiI1iI111ii1i ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   iii11I ( )
  if iI1i11iII111 == 1 :
   I1Iii1 ( iiOOooooO0Oo )
  if iI1i11iII111 == 2 :
   iiI11Iii ( )
  if iI1i11iII111 == 3 :
   O0o0O0 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if iI1i11iII111 == 4 :
   Ii1II1I11i1 ( )
 else :
  I1IIII1i ( '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9001 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']POPCORN BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 7061 , oOOOo00O00oOo + 'PopcornBox.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Desi Flix[/COLOR]' , '' , 80005 , oOOOo00O00oOo + 'Desi.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , oOOOo00O00oOo + 'FilmTrailers.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOOo00O00oOo + 'ClassicMovies.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def oOoooooOoO ( ) :
 IIiiiI1iIII ( )
 Ii111 ( )
 if 10 - 10: O00OOo00oo0o % OOoOoo * OOoOoo . iiII11i1I1IIi / iIi1i1ii1 % IIi
 if 49 - 49: oO0o / oo0oO00 + o0o00Oo0O * I11i
 I1IIII1i ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  I1I11i ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
 I1I11i ( '[COLOR' + II + ']Link GTV to Guide[/COLOR]' , '' , 4010 , oOOOo00O00oOo + 'linkchannels.png' , O0o0Oo , '' )
def IiIi ( ) :
 I1IIII1i ( '[COLOR' + II + ']DAILY LISTS[/COLOR]' , '' , 9007 , Oo00OOOOO , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Oo00OOOOO , O0o0Oo , '' )
 if 28 - 28: IIiIi1iI + Ii / iiII11i1I1IIi % OOooOOo % I1ii11iIi11i - o0o00Oo0O
 if 54 - 54: ooOoO0O00 + IIiIiII11i
 if 83 - 83: Ii1I - oOo0O0Ooo + IIi
 if 5 - 5: iIi1i1ii1
 if 46 - 46: OOoOoo
def Ii1IIiI1IiIII ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   ii1iIi1iIiI1i ( )
  if iI1i11iII111 == 1 :
   iiI1iIii1i ( )
  if iI1i11iII111 == 2 :
   OOooO0oo0o00o ( )
  if iI1i11iII111 == 3 :
   ooOO0OoO ( )
  if iI1i11iII111 == 4 :
   Oo0 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1IIII1i ( '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9002 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '' , 10040 , oOOOo00O00oOo + 'WatchSeries.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '' , 8020 , oOOOo00O00oOo + 'iWatchSeries.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']CLASSIC TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 8064 , oOOOo00O00oOo + 'ClassicTV.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , oOOOo00O00oOo + 'TVShowTrailers.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def oooooOOO000Oo ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   Ooo00OoOOO = '[COLOR' + II + ']SILENT HUNTER[/COLOR]'
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   Oo0OO0000oooo = '[COLOR' + II + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   IIII1iII = '[COLOR' + II + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   ii1III11 = '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   I1iiIIIi11 = '[COLOR' + II + ']APPRENTICE[/COLOR]'
  OooOoOO0 = [ Ooo00OoOOO , Oo0OO0000oooo , IIII1iII , '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , I1iiIIIi11 , '[COLOR' + II + ']RAIZ TV[/COLOR]' , ii1III11 , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   Ii1I11ii1i ( ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvL2pkaC9ob21lLnR4dA==' ) ) )
  if iI1i11iII111 == 1 :
   Ii1I11ii1i ( ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvbWFpbm1lbnUucGhw' ) ) )
  if iI1i11iII111 == 2 :
   O0iIiIIIIIii ( )
  if iI1i11iII111 == 3 :
   iIIIII1I ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , ooI1i , iiI11ii1I1 )
  if iI1i11iII111 == 4 :
   OOo0 ( )
  if iI1i11iII111 == 5 :
   iIIIII1I ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , ooI1i , iiI11ii1I1 )
  if iI1i11iII111 == 6 :
   ii11I1 ( )
  if iI1i11iII111 == 7 :
   iIIIII1I ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , ooI1i , iiI11ii1I1 )
  if iI1i11iII111 == 8 :
   iIIIII1I ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9tYWluLnBocA==' ) ) , ooI1i , iiI11ii1I1 )
 else :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvbWFpbm1lbnUucGhw' ) ) , 90037 , oOOOo00O00oOo + 'TheReaper.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']PANDORAS BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 10025 , oOOOo00O00oOo + 'PandorasBox.png' , O0o0Oo , '' )
   if 75 - 75: oO0o / IIiIiII11i % o0o00Oo0O
   if 38 - 38: ii * IIiIi1iI % o0o00Oo0O * OOooOOo
  I1IIII1i ( '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'DojoStreams.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , '' , 1017 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'raiztv.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 1023 , oOOOo00O00oOo + 'ScoobyStreams.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'ITVStreams.png' , O0o0Oo , '' )
  if 29 - 29: Ii1I / ooOoO0O00 . oOo0O0Ooo - OOooOOo - OOooOOo - iIi1i1ii1
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 20 - 20: ooOoO0O00 % oO0o . oOo0O0Ooo / OOoOoo * Ii * IIi
def OOo ( ) :
 IIiiiI1iIII ( )
 I1I11i ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
def i1i11I1I1iii1 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 url = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( OoO000O0Oo )
 for ooo0O , iII1iii in IIIII11I1IiI :
  if '[DIR]' in ooo0O :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iII1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + iII1iii , 1018 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'mkv' in iII1iii :
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iII1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + iII1iii , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'avi' in iII1iii :
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iII1iii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + iII1iii , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
   if 83 - 83: oo0oO00 - IIiIiII11i - OooOO000
def OOo0 ( ) :
 I1IIII1i ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , oOOOo00O00oOo + 'scraped.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 if 3 - 3: O00OOo00oo0o
def i1iiIiI1Ii1i ( url ) :
 I1 = i1iIi ( url )
 IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( I1 )
 for iiI11ii1I1 , url , iiiii1II , O0OOO0OOooo00 , iiii111II , I111iIi1 in IIIII11I1IiI :
  if O0OOO0OOooo00 == '123' :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'appstreams.png'
  if iiii111II == '123' :
   iiii111II = oOOOo00O00oOo + 'appstreams.png'
  if 'php' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100010 , O0OOO0OOooo00 , iiii111II , I111iIi1 )
  elif 'playlist' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100007 , O0OOO0OOooo00 , iiii111II , I111iIi1 )
  elif 'watchseries' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100100 , O0OOO0OOooo00 , iiii111II , I111iIi1 )
  elif not 'http' in url :
   oo00O00oO000o ( iiI11ii1I1 , url , 100009 , O0OOO0OOooo00 , iiii111II , I111iIi1 , '' )
  else :
   oo00O00oO000o ( iiI11ii1I1 , url , 100005 , O0OOO0OOooo00 , iiii111II , I111iIi1 , '' )
   if 71 - 71: Ii1I - IIiIi1iI / OOooOOo * OOooOOo / ooOoO0O00 . ooOoO0O00
def ooo000ooO0000 ( url ) :
 I1 = i1iIi ( url )
 oOoooo000Oo00 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for url , oOo0OOoO0 , I111iIi1 , iiii111II , iiI11ii1I1 in oOoooo000Oo00 :
  if oOo0OOoO0 == '123' :
   oOo0OOoO0 = oOOOo00O00oOo + 'appstreams.png'
  if iiii111II == '123' :
   iiii111II = O0o0Oo
  if 'php' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100004 , oOo0OOoO0 , iiii111II , I111iIi1 )
  elif 'playlist' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100007 , oOo0OOoO0 , iiii111II , I111iIi1 )
  elif 'watchseries' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100100 , oOo0OOoO0 , iiii111II , I111iIi1 )
  elif not 'http' in url :
   oo00O00oO000o ( iiI11ii1I1 , url , 100009 , oOo0OOoO0 , iiii111II , I111iIi1 , '' )
  else :
   oo00O00oO000o ( iiI11ii1I1 , url , 100005 , oOo0OOoO0 , iiii111II , I111iIi1 , '' )
   if 93 - 93: Ii1I / oOo0O0Ooo / iI11I1II1I1I % O00OOo00oo0o % O00OOo00oo0o
def IiI11iI1i1i1i ( url ) :
 if 89 - 89: iiII11i1I1IIi
 I1 = i1iIi ( url )
 Ooooooo = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( I1 )
 for I1IIIiI1I1ii1 in Ooooooo :
  O0OOO0OOooo00 = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for O0OOO0OOooo00 in O0OOO0OOooo00 :
   O0OOO0OOooo00 = O0OOO0OOooo00
  iiI11ii1I1 = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for iiI11ii1I1 in iiI11ii1I1 :
   if 'elete' in iiI11ii1I1 :
    pass
   elif 'rivate Vid' in iiI11ii1I1 :
    pass
   else :
    iiI11ii1I1 = ( iiI11ii1I1 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  iiiI1I1iIIIi1 = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for iiiI1I1iIIIi1 in iiiI1I1iIIIi1 :
   iiiI1I1iIIIi1 = iiiI1I1iIIIi1
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for url in url :
   url = url
  oo00O00oO000o ( '[COLORred]' + str ( iiiI1I1iIIIi1 ) + '[/COLOR] : ' + str ( iiI11ii1I1 ) , str ( url ) , 100009 , str ( O0OOO0OOooo00 ) , O0o0Oo , '' , '' )
  i1Oo0oO00o ( 'movies' , '' )
  if 17 - 17: iI11I1II1I1I . ii / iiII11i1I1IIi % IIiIiII11i % ooOoO0O00 / Ii
  if 58 - 58: I1ii11iIi11i . IIiIiII11i + oo0oO00 - Ii / IIiIiII11i / o0o00Oo0O
  if 85 - 85: OOooOOo + IIi
  if 10 - 10: OOoOoo / oO0o + OOooOOo / ooOoO0O00
  if 27 - 27: iIi1i1ii1
def oO0OO0 ( iconimage , url , extra ) :
 O0OOO0OOooo00 = ' '
 o0O0Oo00 = ' '
 iiii111II = ' '
 O0Oo0o000oO = ' '
 oO0o00oOOooO0 = i1iIi ( url )
 O0OOO0OOooo00 = re . compile ( '<img src="(.+?)">' ) . findall ( oO0o00oOOooO0 )
 for O0OOO0OOooo00 in O0OOO0OOooo00 :
  O0OOO0OOooo00 = O0OOO0OOooo00
 OOOoO000 = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( oO0o00oOOooO0 )
 for iiii111II in OOOoO000 :
  iiii111II = iiii111II
 IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( oO0o00oOOooO0 )
 for url , O0Oo0o000oO in IIIII11I1IiI :
  O0Oo0o000oO = 'S' + ( O0Oo0o000oO ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = I11i1I1I + url
  oOOOO ( ( O0Oo0o000oO ) . replace ( '  ' , '' ) , url , 100101 , O0OOO0OOooo00 , iiii111II , o0O0Oo00 , '' )
  i1Oo0oO00o ( 'Movies' , 'info' )
  if 49 - 49: IIiIiII11i . oo0oO00 . Ii % OOoOoo
def i11i1iiI1i ( url , name , fanart , extra , iconimage ) :
 oO0oOOoo00000 = extra
 O0Oo0o000oO = name
 oO0o00oOOooO0 = i1iIi ( url )
 O0OOO0OOooo00 = iconimage
 IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( oO0o00oOOooO0 )
 for url , name , oOo00 in IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = I11i1I1I + url
  oOo00 = oOo00
  i1iI11i1IIi = name + ' - [COLORred]' + oOo00 + '[/COLOR]'
  oOOOO ( i1iI11i1IIi , url , 100102 , O0OOO0OOooo00 , fanart , 'Aired : ' + oOo00 , i1iI11i1IIi )
  if 4 - 4: ii - Ii1I * oOo0O0Ooo
def I1iIiI11I1 ( name , URL , iconimage , fanart ) :
 I1 = i1iIi ( URL )
 IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , name in IIIII11I1IiI :
  for oOOOoo00 in oO0Oo :
   if oOOOoo00 in iiOOooooO0Oo :
    URL = 'http://www.watchseriesgo.to/link/' + iiOOooooO0Oo
    oo00O00oO000o ( name , URL , 100106 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( IIIII11I1IiI ) <= 0 :
  oOOOO ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 27 - 27: iIi1i1ii1 . Ii % O00OOo00oo0o
  if 65 - 65: IIiIiII11i . oOo0O0Ooo % oo0oO00 * oO0o
def iI11I ( url , name ) :
 I1IIIiii1 = name
 I1 = i1iIi ( url )
 IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( I1 )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( I1 )
 I1II1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  O00oo ( url , I1IIIiii1 )
 for url in i1I :
  O00oo ( url , I1IIIiii1 )
 for url in I1II1 :
  O00oo ( url , I1IIIiii1 )
  if 77 - 77: OooOO000 % IIi - iiII11i1I1IIi % IIiIi1iI - oO0o / I1ii11iIi11i
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
  if 84 - 84: oo0oO00 % ooOoO0O00
def IioO0oOOO0Ooo ( url , season_name ) :
 I1 = i1iIi ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for oOO , iiI11ii1I1 in IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 89 - 89: O00OOo00oo0o + ii + O00OOo00oo0o * ooOoO0O00 + iI11I1II1I1I % iiII11i1I1IIi
  if 59 - 59: IIi + Ii
def I1iii ( url , season_name ) :
 I1 = i1iIi ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for oOO , iiI11ii1I1 in IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 88 - 88: Ii - IIiIi1iI
def oO0o0O0Ooo0o ( url , season_name ) :
 I1 = i1iIi ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I1 )
 for oOO , iiI11ii1I1 in IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 67 - 67: IIi . I1ii11iIi11i + OOooOOo - ii
def i1Ii11II ( url , season_name ) :
 I1 = i1iIi ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for oOO in IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 70 - 70: IIi / IIiIiII11i - iI11I1II1I1I - OooOO000
def Ii1iI111 ( url , season_name ) :
 I1 = i1iIi ( url )
 IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( I1 )
 for oOO in IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 11 - 11: iI11I1II1I1I . ii . IIiIiII11i / ooOoO0O00 - iiII11i1I1IIi
def O0oooo00o0Oo ( url , season_name ) :
 I1 = i1iIi ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for oOO in IIIII11I1IiI :
  Ii1II ( oOO , season_name )
  if 30 - 30: OOooOOo
def Ii1II ( Link , season_name ) :
 if 'http:/' in Link :
  Ii111oO0 ( Link )
  if 11 - 11: IIiIi1iI / IIiIiII11i
def iii1I1i ( url ) :
 I1 = OPEN_URL_1 ( url )
 OOOOooO0oO00O0o = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 for url in OOOOooO0oO00O0o :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 70 - 70: O00OOo00oo0o
def oOOOO ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 i11iIIi11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooOooo000OO00 = True
 IiIiI1I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIiI1I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiIiI1I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I11oo0ooOO = [ ]
  if 24 - 24: oO0o % oO0o * iI11I1II1I1I
  if showcontext == 'fav' :
   I11oo0ooOO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   I11oo0ooOO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IiIiI1I1I1 . addContextMenuItems ( I11oo0ooOO )
 ooOooo000OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iIIi11 , listitem = IiIiI1I1I1 , isFolder = True )
 return ooOooo000OO00
 if 50 - 50: oO0o . Ii - oo0oO00 . oo0oO00
 if 31 - 31: IIi / I1ii11iIi11i * ooOoO0O00 . OOooOOo
def oo00O00oO000o ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 i11iIIi11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooOooo000OO00 = True
 IiIiI1I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIiI1I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiIiI1I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I11oo0ooOO = [ ]
  I11oo0ooOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I11oo0ooOO . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   I11oo0ooOO . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IiIiI1I1I1 . addContextMenuItems ( I11oo0ooOO )
 ooOooo000OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iIIi11 , listitem = IiIiI1I1I1 , isFolder = False )
 return ooOooo000OO00
 if 57 - 57: IIi + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
def OO0oo ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 15 - 15: iI11I1II1I1I % ii - I1ii11iIi11i * iIi1i1ii1 + iiII11i1I1IIi
def i1I1II1iIIi11 ( url ) :
 IiI1iII1II111 = xbmc . Player ( IIiI11i1111Ii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : IiI1iII1II111 . play ( url ) . strip ( )
 except : pass
 if 63 - 63: IIi + IIiIi1iI
def Ii111oO0 ( url ) :
 IiI1iII1II111 = xbmc . Player ( )
 import urlresolver
 try : IiI1iII1II111 . play ( url )
 except : pass
 if 66 - 66: IIi - iI11I1II1I1I / OOooOOo + IIi - iiII11i1I1IIi + OooOO000
def i1iIi ( url ) :
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
  if 29 - 29: I11i % iI11I1II1I1I . ii % ii % IIiIiII11i / OooOO000
  if 70 - 70: Ii % OooOO000
  if 11 - 11: OOoOoo % Ii1I % iIi1i1ii1 / IIiIiII11i % O00OOo00oo0o - I1ii11iIi11i
def O0i11I1I1I ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   OOooO ( )
  if iI1i11iII111 == 1 :
   O00O0OO00oo ( )
  if iI1i11iII111 == 2 :
   oOOO ( )
  if iI1i11iII111 == 3 :
   ooo0oooo0 ( )
  if iI1i11iII111 == 4 :
   OOO0ooo ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
 else :
  I1IIII1i ( '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'SearchCartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'WCO' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , str ( ooOO0O0ooOooO ) , 21004 , oOOOo00O00oOo + 'watchcartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Cartoons' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']CARTOONS[/COLOR]' , '' , 10001 , oOOOo00O00oOo + 'Cartoons.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '' , 20000 , oOOOo00O00oOo + 'Cartoons.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Anime' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']AnimeLand[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) , 10004 , oOOOo00O00oOo + 'anime.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def iIII ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Football' ) == 'true' :
  I1IIII1i ( '[COLOR' + II + ']FOOTBALL[/COLOR]' , '' , 10002 , oOOOo00O00oOo + 'Football.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Fitness' ) == 'true' :
  I1IIII1i ( '[COLOR' + II + ']FITNESS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cuZml0bmVzc2JsZW5kZXIuY29tL3ZpZGVvcw==' ) ) , 7085 , oOOOo00O00oOo + 'Fitness.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'Go Fishing' ) == 'true' :
  I1IIII1i ( '[COLOR' + II + ']Go Fishing[/COLOR]' , str ( ooOO0O0ooOooO ) , 8090 , oOOOo00O00oOo + 'GoFishing.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'GenieTv Kitchen' ) == 'true' :
  I1IIII1i ( '[COLOR' + II + ']GenieTv Kitchen[/COLOR]' , ( i11 ( 'aHR0cDovL2Zvb2QubmR0di5jb20vdmlkZW9z' ) ) , 8045 , oOOOo00O00oOo + 'GenieTVKitchen.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 7 - 7: I11i + ooOoO0O00 . oOo0O0Ooo / I1ii11iIi11i
 if 22 - 22: IIiIi1iI - IIiIi1iI % IIi . O00OOo00oo0o + oo0oO00
 if 63 - 63: oOo0O0Ooo % O00OOo00oo0o * I11i + O00OOo00oo0o / I1ii11iIi11i % OooOO000
def OO ( ) :
 I1 = O000oo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiooOOoooooo in IIIII11I1IiI :
  IIiooOOoooooo = ( str ( IIiooOOoooooo ) )
  if os . path . exists ( xbmc . translatePath ( IIiooOOoooooo ) ) :
   iiI1i1Iii111 = ( IIiooOOoooooo ) . replace ( 'special://home/addons/' , '' )
   iiIiI1i1 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + iiI1i1Iii111 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iI1i11iII111 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iI1i11iII111 == 0 :
    i111I11i ( IIiooOOoooooo )
    oOOo0O00o ( )
   elif iI1i11iII111 == 1 :
    ii1OoOO ( IIiooOOoooooo )
  else :
   pass
   if 44 - 44: IIi
def ii1OoOO ( addon ) :
 iiI1i1Iii111 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 54 - 54: iIi1i1ii1 - iiII11i1I1IIi - O00OOo00oo0o . iI11I1II1I1I
def i111I11i ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 o0OIIiI1I1 = os . path . join ( I11II1i , 'default.py' )
 I11I1IIiiII1 = open ( o0OIIiI1I1 , "w+" )
 if 31 - 31: oOo0O0Ooo * oo0oO00 + ii - OooOO000 / ii
 I11I1IIiiII1 . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 I11I1IIiiII1 . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 I11I1IIiiII1 . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 19 - 19: OOoOoo * IIiIi1iI * I11i + o0o00Oo0O / o0o00Oo0O
 if 73 - 73: iI11I1II1I1I / iI11I1II1I1I - oo0oO00
 if 91 - 91: oo0oO00 + oOo0O0Ooo
 if 59 - 59: oOo0O0Ooo + Ii + ooOoO0O00 / iiII11i1I1IIi
def Ii1I11ii1i ( url ) :
 I1 = O000oo ( url )
 I11iIiI1 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 I1II1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 oo00OO0000oO = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 oo0oooOo = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url , oo00oO0o , iiii111II , I111iIi1 in I11iIiI1 :
  if 'php' in url :
   I1IIII1i ( iiI11ii1I1 , url , 90037 , oo00oO0o , iiii111II , I111iIi1 )
  elif iiI11ii1I1 == 'Search' :
   I1IIII1i ( 'Search' , url , 90038 , oo00oO0o , iiii111II , I111iIi1 )
  else :
   I1I11i ( iiI11ii1I1 , url , 222 , oo00oO0o , iiii111II , I111iIi1 )
 for iiI11ii1I1 , oOo0OOoO0 , url , o0OO0O0Oo in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 90037 , oOo0OOoO0 , o0OO0O0Oo , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , o0OO0O0Oo in i1I :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , o0OO0O0Oo , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , o0OO0O0Oo in I1II1 :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , o0OO0O0Oo , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , o0OO0O0Oo in oo00OO0000oO :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , o0OO0O0Oo , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 in oo0oooOo :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , '' , '' )
  i1Oo0oO00o ( 'movies' , 'MAIN' )
  if 78 - 78: OOooOOo / I1ii11iIi11i - IIi - OooOO000 * oo0oO00
def Ii1I11I ( ) :
 iiIii1I = [ 'serialsearch' , 'moviesearch' ]
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 if OO0OO0OO == '' :
  pass
 else :
  for OoooO0o in iiIii1I :
   IIIii1iiIi = I11 + OoooO0o + '.php'
   oO0o00oOOooO0 = O000oo ( IIIii1iiIi )
   if oO0o00oOOooO0 != 'Opened' :
    oOoooo000Oo00 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( oO0o00oOOooO0 )
    for iiI11ii1I1 , iiOOooooO0Oo , oo00oO0o , iiii111II , I111iIi1 in oOoooo000Oo00 :
     if OO0OO0OO in iiI11ii1I1 . lower ( ) :
      oooo0OOo = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( o00OO00OoO ) )
      for oOOOoo00 in oooo0OOo :
       if oOOOoo00 == iiOOooooO0Oo :
        iiI11ii1I1 = '[COLORred]* [/COLOR]' + ( iiI11ii1I1 ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        OoO00 = open ( oOOoo0Oo , "a" )
        OoO00 . write ( 'item="' + iiI11ii1I1 + '"\n' )
        OoO00 . close
      if 'php' in iiOOooooO0Oo :
       I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , 90037 , oo00oO0o , iiii111II , I111iIi1 )
      else :
       I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 222 , oo00oO0o , iiii111II , I111iIi1 )
       if 18 - 18: iIi1i1ii1 - ii % IIiIiII11i - oOo0O0Ooo % OOooOOo
   i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
   if 60 - 60: iI11I1II1I1I + ooOoO0O00
def OooOOo0 ( ) :
 I1 = O000oo ( 'http://www.tvcatchup.com/channels/' )
 iii1i1iiiiIi = O000oo ( 'http://www.djing.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for ooO000O , oOo0OOoO0 , iiOOooooO0Oo in IIIII11I1IiI :
  ooOO0oO0oo00o ( ooO000O , 'http://www.tvcatchup.com' + iiOOooooO0Oo , 90024 , 'http://www.tvcatchup.com' + oOo0OOoO0 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in i1I :
  if 'Submit' in iiI11ii1I1 :
   pass
  elif '&lt;' in iiI11ii1I1 :
   pass
  else :
   I1I11i ( 'DJing  ' + iiI11ii1I1 , iiOOooooO0Oo , 90025 , 'http://www.djing.com' + oOo0OOoO0 , O0o0Oo , '' )
  i1Oo0oO00o ( 'movies' , 'MAIN' )
def oOIII111iiIi1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'var url = "([^"]*)";' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( url )
def Ii11Ii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 1 - 1: oOo0O0Ooo % ii + IIiIiII11i - OOoOoo
def iiI11Iii ( ) :
 i11i1iiiII ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O000oo ( 'http://www.join4films.com/' )
 IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , iiOOooooO0Oo , 80006 , oOOOo00O00oOo + 'Desi.png' )
def i11I1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( iiI11ii1I1 , url , 80007 , oOo0OOoO0 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def iiiI111I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  iii1 ( url )
def oooOOO00o0 ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Iii = 'http://www.join4films.com/?s=' + ( i1I11iIiII ) . replace ( ' ' , '+' ) + '&search_type=1'
 OO0OO0OO = i1Iii . lower ( )
 i11I1 ( OO0OO0OO )
 if 39 - 39: I11i - Ii1I % OooOO000 * oO0o - IIi / OooOO000
 if 29 - 29: Ii1I
 if 52 - 52: Ii / ooOoO0O00
 if 1 - 1: IIiIi1iI
 if 78 - 78: Ii1I + iiII11i1I1IIi - o0o00Oo0O
 if 10 - 10: O00OOo00oo0o % oOo0O0Ooo
 if 97 - 97: ii - O00OOo00oo0o
 if 58 - 58: iI11I1II1I1I + o0o00Oo0O
 if 30 - 30: IIiIi1iI % OooOO000 * IIi - Ii1I * iIi1i1ii1 % IIiIi1iI
 if 46 - 46: Ii - o0o00Oo0O . oo0oO00
 if 100 - 100: oOo0O0Ooo / I11i * OooOO000 . o0o00Oo0O / IIi
 if 83 - 83: O00OOo00oo0o
 if 48 - 48: IIiIiII11i * IIi * O00OOo00oo0o
 if 50 - 50: OOoOoo % ooOoO0O00
 if 21 - 21: ii - iI11I1II1I1I
 if 93 - 93: oo0oO00 - I11i % OOooOOo . OOooOOo - IIiIi1iI
 if 90 - 90: IIiIi1iI + IIiIiII11i * Ii1I / iIi1i1ii1 . I11i + I11i
def I11I ( ) :
 I1IIII1i ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 I1IIII1i ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 I1IIII1i ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 I1IIII1i ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 if 69 - 69: ooOoO0O00
def ooOoOOOOo ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Iii = 'http://imoviemax.se/?s=' + ( i1I11iIiII ) . replace ( ' ' , '+' )
 OO0OO0OO = i1Iii . lower ( )
 ooooOooooOOo ( OO0OO0OO )
def ooO00O00oOO ( url ) :
 I1IIII1ii = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , iiI11ii1I1 , IiIIi1I1I11Ii in IIIII11I1IiI :
  if iiI11ii1I1 in I1IIII1ii :
   pass
  else :
   I1IIII1i ( iiI11ii1I1 + ' - ' + IiIIi1I1I11Ii + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
   I1IIII1ii . append ( iiI11ii1I1 )
   if 64 - 64: ii
def oO0oooooo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , o0OO0Oo in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 + ' - Views:' + o0OO0Oo , url , 10075 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
  if 3 - 3: O00OOo00oo0o - o0o00Oo0O % iI11I1II1I1I / OOoOoo . I11i
  if 3 - 3: o0o00Oo0O % ii / IIi
def ooooOooooOOo ( url ) :
 ooOo = [ ]
 I1 = O000oo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  I1IIII1i ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 10075 , oOo0OOoO0 , oOo0OOoO0 , '' )
  ooOo . append ( iiI11ii1I1 )
  if 84 - 84: IIi
def o0OoO00 ( img , name , url ) :
 img = img
 name = name
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for IIIIIiII1 , url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  iii11 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + iii11
  i1oO = ( IIIIIiII1 ) . replace ( 'play-' , 'Server ' )
  I1I11i ( i1oO , iii11 , 10076 , img , img , '' )
  if 30 - 30: I1ii11iIi11i . oO0o
def o0Oii1111i ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for iII1iii in IIIII11I1IiI :
  if '=m' in iII1iii :
   O0ooOO ( iII1iii )
  elif 'php' in iII1iii :
   o0Oii1111i ( url )
  else :
   I1 = O000oo ( iII1iii )
   IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for IiiI in IIIII11I1IiI :
    O0ooOO ( iII1iii )
    if 19 - 19: IIiIiII11i
    if 72 - 72: ii / oOo0O0Ooo + iIi1i1ii1 / OOooOOo * iIi1i1ii1
    if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + OooOO000 * iI11I1II1I1I % iIi1i1ii1
def I1iI1I1 ( url ) :
 I1 = O000oo ( url )
 IiIi1 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oOo00 , oo00ooOoo in IiIi1 :
  print 'there ><><><><><><><><><><><><'
  oOo00 = oOo00
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oo00ooOoo ) )
  for iiI11ii1I1 , iii1IIIiiiI in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + oOo00 + '[/COLOR] - ' + iiI11ii1I1 + ' - [COLOR' + II + ']' + iii1IIIiiiI + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
 I1IIIiI1I1ii1 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oOo00 , OoO00oo00 in I1IIIiI1I1ii1 :
  print 'there ><><><><><><><><><><><><'
  oOo00 = oOo00
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( OoO00oo00 ) )
  for iiI11ii1I1 , iii1IIIiiiI in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + oOo00 + '[/COLOR] - ' + iiI11ii1I1 + ' - [COLOR' + II + ']' + iii1IIIiiiI + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
   if 76 - 76: ii + I1ii11iIi11i % OOoOoo . oO0o + IIiIiII11i
   if 70 - 70: oOo0O0Ooo / iiII11i1I1IIi
   if 28 - 28: Ii1I * ii . IIiIiII11i / Ii + oo0oO00
def Oo0 ( url ) :
 I1 = O000oo ( url )
 I1IIIiI1I1ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
 for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
  iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for iiI11ii1I1 in iiI11ii1I1 :
   iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  O0OOO0OOooo00 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for O0OOO0OOooo00 in O0OOO0OOooo00 :
   O0OOO0OOooo00 = 'http:' + O0OOO0OOooo00
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O0OOO0OOooo00 , '' , '' )
  if 38 - 38: OOoOoo . iIi1i1ii1
  if 24 - 24: I11i - I11i + Ii1I + oOo0O0Ooo - oo0oO00
  if 12 - 12: OooOO000 . OOoOoo . OOooOOo / o0o00Oo0O
  if 58 - 58: I11i - IIiIiII11i % oo0oO00 + O00OOo00oo0o . OOooOOo / OOoOoo
def O0o0O0 ( url ) :
 if 8 - 8: Ii1I . oO0o * iiII11i1I1IIi + IIiIiII11i % Ii
 i1i1IiIiIi1Ii = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for iII1iii , oOo0OOoO0 , iiI11ii1I1 , oO0ooOO in IIIII11I1IiI :
  iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O000oo ( iII1iii )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for OOOOooO0oO00O0o , o0O0Oo00 in i1I :
   IIi1iI1 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( o0O0Oo00 ) )
   for I111iIi1 in IIi1iI1 :
    if iiI11ii1I1 in i1i1IiIiIi1Ii :
     pass
    else :
     I1I11i ( iiI11ii1I1 , OOOOooO0oO00O0o , 8043 , oOo0OOoO0 , oOo0OOoO0 , I111iIi1 )
     i1Oo0oO00o ( 'movies' , 'INFO' )
     i1i1IiIiIi1Ii . append ( iiI11ii1I1 )
     if 44 - 44: Ii1I - iIi1i1ii1 / IIiIiII11i * oO0o * I1ii11iIi11i
     if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * IIi % IIiIiII11i
def OooOoOOo0oO00 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , ooI1i , I111iIi1 , iiii111II , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 10065 , ooI1i , iiii111II , I111iIi1 )
 i1Oo0oO00o ( 'movies' , 'INFO' )
 if 73 - 73: OooOO000 / Ii1I % Ii1I * iiII11i1I1IIi / Ii1I
def iI1I11iIIi1 ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Iii = 'https://www.youtube.com/results?search_query=' + ( i1I11iIiII ) . replace ( ' ' , '+' )
 OO0OO0OO = i1Iii . lower ( )
 I1 = O000oo ( OO0OO0OO )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for iiOOooooO0Oo in next :
  iiOOooooO0Oo = 'https://www.youtube.com' + iiOOooooO0Oo
  I1IIII1i ( '[COLOR' + II + '] NEXT [/COLOR]' , iiOOooooO0Oo , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 , iI , o0O0Oo00 in IIIII11I1IiI :
  oOoOooOo0o0 . append ( iiI11ii1I1 )
  i1Oo0oO00o ( 'tvshows' , 'INFO' )
  O0OOO0OOooo00 = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + O0OOO0OOooo00
  iiOOooooO0Oo = 'http://www.youtube.com' + iiOOooooO0Oo
  I1I11i ( '[COLORred]' + iI + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O0OOO0OOooo00 , O0OOO0OOooo00 , o0O0Oo00 )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 , iI in IIIII11I1IiI :
   print 'im doing it'
   i1Oo0oO00o ( 'tvshows' , 'INFO' )
   O0OOO0OOooo00 = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
   iiOOooooO0Oo = 'http://www.youtube.com' + iiOOooooO0Oo
   if '&' in iiOOooooO0Oo :
    print ' i got here'
    I1 = O000oo ( iiOOooooO0Oo )
    I1IIIiI1I1ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
     iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for iiI11ii1I1 in iiI11ii1I1 :
      iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     iiOOooooO0Oo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for iiOOooooO0Oo in iiOOooooO0Oo :
      iiOOooooO0Oo = 'https://www.youtube.com/w' + iiOOooooO0Oo
     O0OOO0OOooo00 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for O0OOO0OOooo00 in O0OOO0OOooo00 :
      O0OOO0OOooo00 = 'http:' + O0OOO0OOooo00
     I1I11i ( '[COLORred]' + iI + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O0OOO0OOooo00 , O0o0Oo , '' )
   elif iiI11ii1I1 in oOoOooOo0o0 :
    pass
   elif 'user' in iiOOooooO0Oo or 'elete' in iiI11ii1I1 :
    pass
   elif 'hannel' in iiOOooooO0Oo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iiOOooooO0Oo
    I1 = O000oo ( iiOOooooO0Oo )
    Ii1IIiiIiiIi = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 in Ii1IIiiIiiIi :
     if 'outube' in iiOOooooO0Oo or 'list' in iiOOooooO0Oo :
      pass
     elif 'atch' in iiOOooooO0Oo :
      iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '/watch?v=' , '' )
      I1I11i ( '[COLORred]' + iI + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0OOoO0 , 'http:' + oOo0OOoO0 , '' )
     else :
      pass
   else :
    I1I11i ( '[COLORred]' + iI + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O0OOO0OOooo00 , O0OOO0OOooo00 , '' )
    if 40 - 40: I11i
def oOOo0oo0o0o0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IIII1i ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for oOo0OOoO0 , url , iiI11ii1I1 , iI , o0O0Oo00 in IIIII11I1IiI :
  oOoOooOo0o0 . append ( iiI11ii1I1 )
  i1Oo0oO00o ( 'tvshows' , 'INFO' )
  O0OOO0OOooo00 = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + O0OOO0OOooo00
  url = 'http://www.youtube.com' + url
  I1I11i ( '[COLORred]' + iI + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O0OOO0OOooo00 , O0OOO0OOooo00 , o0O0Oo00 )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for oOo0OOoO0 , url , iiI11ii1I1 , iI in IIIII11I1IiI :
   i1Oo0oO00o ( 'tvshows' , 'INFO' )
   O0OOO0OOooo00 = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    I1 = O000oo ( url )
    I1IIIiI1I1ii1 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
     iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for iiI11ii1I1 in iiI11ii1I1 :
      iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     O0OOO0OOooo00 = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I1IIIiI1I1ii1 ) )
     for O0OOO0OOooo00 in O0OOO0OOooo00 :
      O0OOO0OOooo00 = 'http:' + O0OOO0OOooo00
     I1I11i ( '[COLORred]' + iI + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O0OOO0OOooo00 , O0o0Oo , '' )
   elif iiI11ii1I1 in oOoOooOo0o0 :
    pass
   elif 'user' in url or 'elete' in iiI11ii1I1 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O000oo ( url )
    Ii1IIiiIiiIi = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for oOo0OOoO0 , url , iiI11ii1I1 in Ii1IIiiIiiIi :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      I1I11i ( '[COLORred]' + iI + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0OOoO0 , 'http:' + oOo0OOoO0 , '' )
     else :
      pass
   else :
    I1I11i ( '[COLORred]' + iI + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O0OOO0OOooo00 , O0OOO0OOooo00 , '' )
    if 43 - 43: Ii1I / oOo0O0Ooo . IIiIi1iI
    if 62 - 62: iI11I1II1I1I + OooOO000 . I1ii11iIi11i / OOoOoo % o0o00Oo0O . O00OOo00oo0o
def Ii111 ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  Oo0oOooOoOo = open ( IIIii1II1II )
  IIIII11I1IiI = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( Oo0oOooOoOo ) )
  for I1i , Oo in IIIII11I1IiI :
   if I1i == 'needs replacing' or Oo == 'needs replacing' :
    IiIiIi1I1 ( )
    if 2 - 2: ooOoO0O00 - IIiIi1iI + oOo0O0Ooo . I11i * I11i / OOooOOo
  I1IIII1i ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if 93 - 93: ooOoO0O00
def ooOOOo ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOOO + ")" )
 IiIiIi1I1 ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 98 - 98: oo0oO00 % OOoOoo * Ii % Ii1I
def iIiI1IIiii11 ( ) :
 I1IIII1i ( 'Full List' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'PPV' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'Entertainment' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'Factual' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'Movie Channels' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'US Movie Channels TEST' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'Kids' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'Music' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'UK Sports' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'International Sports' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'US Sports Live Event/Ticket/Pass' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'News UK & International' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'German' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'Arabic' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'TV Series Latest' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'VOD Latest' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 I1IIII1i ( 'VOD Bollywood' , '' , 60003 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
 if 33 - 33: iI11I1II1I1I / OooOO000 - oOo0O0Ooo * iiII11i1I1IIi
def o0o00oO0oo000 ( name ) :
 oO000o = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , oOo0OOoO0 , o0Oo , iiOOooooO0Oo in IIIII11I1IiI :
  if oO000o == 'Full List' :
   iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '.ts' , '.m3u8' )
   I1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiOOooooO0Oo ) . strip ( ) , 10012 , oOo0OOoO0 , oOo0OOoO0 , '' )
  else :
   oO000o = ( oO000o ) . replace ( 'World' , 'القنوات العربية' )
   if oO000o in o0Oo :
    iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '.ts' , '.m3u8' )
    print iiOOooooO0Oo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    I1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiOOooooO0Oo ) . strip ( ) , 10012 , oOo0OOoO0 , oOo0OOoO0 , '' )
   else :
    pass
    if 57 - 57: IIi / I1ii11iIi11i
def oO0O0Ooo ( name ) :
 oO000o = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , oOo0OOoO0 , iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '.ts' , '.m3u8' )
  I1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiOOooooO0Oo ) . strip ( ) , 10012 , oOo0OOoO0 , oOo0OOoO0 , '' )
 else :
  I1I11i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 4 - 4: IIiIiII11i . iiII11i1I1IIi + iIi1i1ii1 * O00OOo00oo0o . IIiIi1iI
  if 87 - 87: OOooOOo / oO0o / Ii
  if 74 - 74: oo0oO00 / Ii1I % I11i
  if 88 - 88: OOooOOo - Ii % I11i * iiII11i1I1IIi + Ii1I
  if 52 - 52: IIiIiII11i . oOo0O0Ooo + OOooOOo % oO0o
  if 62 - 62: I11i
  if 15 - 15: iiII11i1I1IIi + iIi1i1ii1 . IIi * oO0o . OOooOOo
  if 18 - 18: ooOoO0O00 % IIiIiII11i + O00OOo00oo0o % iIi1i1ii1
  if 72 - 72: iI11I1II1I1I
  if 45 - 45: I1ii11iIi11i - I11i % O00OOo00oo0o
  if 38 - 38: O00OOo00oo0o % IIi - ii
  if 87 - 87: oO0o % oOo0O0Ooo
def OOoooO00o0oo0 ( ) :
 I1IIII1i ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  I1IIII1i ( 'Backup Genie Favourites' , iiOOooooO0Oo , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( O0Oo000ooO00 ) :
  I1IIII1i ( 'Backup Ivue Config' , O0Oo000ooO00 , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( oO0 ) :
  I1IIII1i ( 'Backup Kodi Favourites' , oO0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 77 - 77: iI11I1II1I1I - ooOoO0O00 . oo0oO00
  if 26 - 26: I11i * OOoOoo . ooOoO0O00
  if 59 - 59: o0o00Oo0O + ooOoO0O00 - I11i
zip = oo00 . getSetting ( 'zip' )
OooOo000o0o = xbmc . translatePath ( os . path . join ( zip ) )
def iI1I1iII1i ( ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 30 - 30: o0o00Oo0O + Ii1I + IIiIiII11i
  if 14 - 14: I11i / IIi - iI11I1II1I1I - oo0oO00 % IIiIi1iI
  if 49 - 49: IIiIi1iI * oo0oO00 / I11i / I1ii11iIi11i * iI11I1II1I1I
def OOoO00ooO ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Ii1iIiII1ii1
  elif 'Ivue' in name :
   url = O0Oo000ooO00
  elif 'Kodi' in name :
   url = oO0
  iI1I1iII1i ( )
  I1IIIIiii1i = open ( url ) . read ( )
  o0IiiiI111I = os . path . join ( OooOo000o0o , description . split ( 'Your ' ) [ 1 ] )
  OOoO = open ( o0IiiiI111I , mode = 'w' )
  OOoO . write ( I1IIIIiii1i )
  OOoO . close ( )
 else :
  if 'guisettings.xml' in description :
   III1I11i1iIi = open ( os . path . join ( OooOo000o0o , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OO0oo0O0OOO0 = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIIII11I1IiI = re . compile ( OO0oo0O0OOO0 ) . findall ( III1I11i1iIi )
   for type , OoOOo , Iii1 in IIIII11I1IiI :
    Iii1 = Iii1 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , OoOOo , Iii1 ) )
  else :
   o0IiiiI111I = os . path . join ( url )
   I1IIIIiii1i = open ( os . path . join ( OooOo000o0o , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOoO = open ( o0IiiiI111I , mode = 'w' )
   OOoO . write ( I1IIIIiii1i )
   OOoO . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 78 - 78: Ii + I11i + O00OOo00oo0o / I11i % iI11I1II1I1I % OOoOoo
 if 83 - 83: iI11I1II1I1I % OOooOOo % I11i % O00OOo00oo0o . Ii1I % o0o00Oo0O
 if 47 - 47: I11i
 if 66 - 66: oOo0O0Ooo - OOoOoo
def iiIii ( ) :
 iIiIii1ii = 1
 iI1I1iII1i ( )
 IIiI1i = xbmc . translatePath ( os . path . join ( OooOo000o0o , 'Build Backup' , 'Full Backup' , '' ) )
 iII1 = xbmc . translatePath ( os . path . join ( OooOo000o0o , 'Build Backup' , 'my_full_backup.zip' ) )
 O000O = xbmc . translatePath ( os . path . join ( OooOo000o0o , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( IIiI1i ) :
  os . makedirs ( IIiI1i )
 Oo00OO0 = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not Oo00OO0 ) : return False , 0
 oo0O = Oo00OO0
 oO00OoOOOo = xbmc . translatePath ( os . path . join ( IIiI1i , oo0O + '.zip' ) )
 Oo0o0OOOOO0O = [ 'plugin.video.GenieTv' ]
 I1I1IiIi1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 oOO0o0oo0 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 oOo000O = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iII = "Creating full backup of existing build"
 ooO0o0O0Oo = "Creating Community Build"
 IiiIIi = "Archiving..."
 O00o0O = ""
 iIIIiI = "Please Wait"
 O00 ( Oo0o0000o0o0 , oO00OoOOOo , ooO0o0O0Oo , IiiIIi , O00o0O , iIIIiI , oOO0o0oo0 , oOo000O )
 time . sleep ( 1 )
 i1iiIII1IIiIIII = xbmc . translatePath ( os . path . join ( IIiI1i , oo0O + '_guisettings.zip' ) )
 I1iIIII1 = zipfile . ZipFile ( i1iiIII1IIiIIII , mode = 'w' )
 try :
  I1iIIII1 . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 I1iIIII1 . close ( )
 if iIiIii1ii == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + iII1 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + oO00OoOOOo + '[/COLOR]' )
  if 57 - 57: OOooOOo . iI11I1II1I1I % IIiIi1iI % iIi1i1ii1 * OOooOOo
def O00 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 II1 = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0ooO0OOO = len ( sourcefile )
 o0oo000OoOoo0 = [ ]
 OoO0o = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for iiiiIiI1i1I1 , oo0 , i1iIIi1II1iiI in os . walk ( sourcefile ) :
  for file in i1iIIi1II1iiI :
   OoO0o . append ( file )
 III1Ii1i1I1 = len ( OoO0o )
 for iiiiIiI1i1I1 , oo0 , i1iIIi1II1iiI in os . walk ( sourcefile ) :
  oo0 [ : ] = [ O0O00OooO for O0O00OooO in oo0 if O0O00OooO not in exclude_dirs ]
  i1iIIi1II1iiI [ : ] = [ OOoO for OOoO in i1iIIi1II1iiI if OOoO not in exclude_files ]
  for file in i1iIIi1II1iiI :
   o0oo000OoOoo0 . append ( file )
   I1IiI1iI11 = len ( o0oo000OoOoo0 ) / float ( III1Ii1i1I1 ) * 100
   o0oOoO00o . update ( int ( I1IiI1iI11 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iIi = os . path . join ( iiiiIiI1i1I1 , file )
   if not 'temp' in oo0 :
    if not 'plugin.program.originwizard' in oo0 :
     import time
     iiO0O0o0oO0O00 = '01/01/1980'
     o0O0oO0 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iIi ) ) )
     if o0O0oO0 > iiO0O0o0oO0O00 :
      II1 . write ( iIi , iIi [ o0ooO0OOO : ] )
 II1 . close ( )
 o0oOoO00o . close ( )
 if 77 - 77: o0o00Oo0O . iIi1i1ii1
 if 39 - 39: IIiIi1iI . IIiIiII11i
def ii11I1 ( ) :
 IIiiiI1iIII ( )
 I1IIII1i ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 if 45 - 45: oo0oO00 * OOooOOo / iI11I1II1I1I
 if 77 - 77: O00OOo00oo0o - iiII11i1I1IIi
def iiI1iI1I ( ) :
 IIiiiI1iIII ( )
 OooOoOO0 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  iii11I ( )
 if iI1i11iII111 == 1 :
  ii1iIi1iIiI1i ( )
 if iI1i11iII111 == 2 :
  OOooO ( )
 if iI1i11iII111 == 3 :
  iI1I11iIIi1 ( )
  if 27 - 27: Ii1I * O00OOo00oo0o - oO0o + iIi1i1ii1 * iIi1i1ii1
  if 55 - 55: IIiIi1iI
  if 82 - 82: O00OOo00oo0o - IIi + oO0o
  if 64 - 64: I11i . o0o00Oo0O * iIi1i1ii1 + ii - I1ii11iIi11i . ii
  if 70 - 70: I1ii11iIi11i - oo0oO00 . iI11I1II1I1I % iiII11i1I1IIi / OOooOOo - o0o00Oo0O
  if 55 - 55: OooOO000 - oO0o
  if 100 - 100: o0o00Oo0O
  if 79 - 79: iI11I1II1I1I
  if 81 - 81: IIi + iI11I1II1I1I * O00OOo00oo0o - iI11I1II1I1I . IIi
def I1ii ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   iIIIII1I ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , ooI1i , iiI11ii1I1 )
  if iI1i11iII111 == 1 :
   Ii1I11ii1i ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if iI1i11iII111 == 2 :
   oO0oI1I1 ( )
  if iI1i11iII111 == 3 :
   O0Oo0 ( )
  if iI1i11iII111 == 4 :
   OOooO0OO0 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if iI1i11iII111 == 5 :
   iI1iIiiiI1I1 ( )
  if iI1i11iII111 == 6 :
   OOOOOo ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if iI1i11iII111 == 7 :
   I1IiiiIiI ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if iI1i11iII111 == 8 :
   O0Oo ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if iI1i11iII111 == 9 :
   I1Ii1iIiII ( )
  if iI1i11iII111 == 10 :
   O0oOo00Ooo0o0 ( )
 else :
  I1IIII1i ( '[COLOR' + II + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , 1016 , oOOOo00O00oOo + 'Rays-Ravers.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']QuickSilver[/COLOR]' , ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) , 90037 , oOOOo00O00oOo + 'Quicksilver.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']RadioNomy[/COLOR]' , '' , 70001 , oOOOo00O00oOo + 'RadioNomy.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , str ( ooOO0O0ooOooO ) , 30031 , oOOOo00O00oOo + 'MusicChannels.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']UK RADIO[/COLOR]' , ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) , 10111113 , oOOOo00O00oOo + 'UKRadio.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']WORLD RADIO[/COLOR]' , str ( ooOO0O0ooOooO ) , 1013 , oOOOo00O00oOo + 'WorldRadio.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CONCERTS' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']CONCERTS[/COLOR]' , ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) , 7050 , oOOOo00O00oOo + 'Concerts.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']MUSIC[/COLOR]' , str ( ooOO0O0ooOooO ) , 1030 , oOOOo00O00oOo + 'MUSIC.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) , 1032 , oOOOo00O00oOo + 'MusicVideos.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']MUSIC[/COLOR]' , str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) , 1010 , oOOOo00O00oOo + 'Music.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , str ( ooOO0O0ooOooO ) , 1111 , oOOOo00O00oOo + 'MusicSearch.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' , 'http://doremisa.com/audiobooks/' , 30000 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , O0o0Oo , '' )
  if 33 - 33: iiII11i1I1IIi
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 87 - 87: OOooOOo / OOoOoo + iI11I1II1I1I
def oo0O0o ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   IioO0O ( )
  if iI1i11iII111 == 1 :
   IiiiiI1i1Iii ( )
  if iI1i11iII111 == 2 :
   iIiIi11 ( )
  if iI1i11iII111 == 3 :
   o00o0 ( iiOOooooO0Oo )
  if iI1i11iII111 == 4 :
   Oo00o0O0O ( iiOOooooO0Oo )
  if iI1i11iII111 == 5 :
   oOOo0O00o ( )
  if iI1i11iII111 == 6 :
   o0ooO0OoOo ( url = 'http://www.iplocation.net/' , inc = 1 )
  if iI1i11iII111 == 7 :
   o0oOO00 ( )
 else :
  I1I11i ( 'CLLEANUP' , 'url' , 9666 , oOOOo00O00oOo + 'MAIN5.png' , O0o0Oo , '' )
  I1I11i ( '[COLOR' + II + ']KILL KODI[/COLOR]' , '' , 80000 , oOOOo00O00oOo + 'KillKodi.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '' , 50004 , oOOOo00O00oOo + 'Speedtest.png' , O0o0Oo , '' )
  I1I11i ( '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '' , 50000 , oOOOo00O00oOo + 'View-Log-File.png' , O0o0Oo , '' )
  I1I11i ( 'DELETE CACHE' , 'url' , 14 , oOOOo00O00oOo + 'DeleteCache.png' , O0o0Oo , '' )
  I1I11i ( 'DELETE PACKAGES' , 'url' , 6 , oOOOo00O00oOo + 'DeletePackages.png' , O0o0Oo , '' )
  I1I11i ( 'FORCE REFRESH' , 'url' , 10 , oOOOo00O00oOo + 'ForceRefresh.png' , O0o0Oo , 'Force Refresh All Repos' )
  I1IIII1i ( 'LAST RESORT FIX EMPTY REPOS' , 'url' , 9 , oOOOo00O00oOo + '1.jpg' , O0o0Oo , 'Fix Corrupt Database' )
  I1I11i ( 'CHECK MY IP' , 'url' , 12 , oOOOo00O00oOo + 'CheckMyIP.png' , O0o0Oo , '' )
  I1I11i ( 'ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER' , 'url' , 13 , oOOOo00O00oOo + 'DeleteTextureAndThumbnailFolderAndroidOnly.png' , O0o0Oo , 'Only Works On Android On Windows It Deletes Your Thumnails Folder But Does Not Delete The Textures13.db' )
  if 46 - 46: Ii - iiII11i1I1IIi
  if 95 - 95: IIiIiII11i
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 65 - 65: OOooOOo
 if 31 - 31: iiII11i1I1IIi * OOooOOo . OOoOoo % iIi1i1ii1 + I1ii11iIi11i
def i1i1II ( ) :
 IIiiiI1iIII ( )
 I1IIII1i ( '[COLOR' + II + ']REPOS[/COLOR]' , ( i11 ( 'aHR0cDovL21pcnJvcnMua29kaS50di9hZGRvbnMv' ) ) , 2030 , oOOOo00O00oOo + 'repos.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']NEW[/COLOR]' , str ( ooOO0O0ooOooO ) , 22 , oOOOo00O00oOo + 'NEW.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']IPTV[/COLOR]' , str ( ooOO0O0ooOooO ) , 23 , oOOOo00O00oOo + 'IPTV.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']VIDEO[/COLOR]' , str ( ooOO0O0ooOooO ) , 24 , oOOOo00O00oOo + 'VIDEO.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SPORTS[/COLOR]' , str ( ooOO0O0ooOooO ) , 25 , oOOOo00O00oOo + 'SPORTS.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']KIDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 26 , oOOOo00O00oOo + 'KIDS.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']MUSIC[/COLOR]' , str ( ooOO0O0ooOooO ) , 27 , oOOOo00O00oOo + 'MUSIC.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']PROGRAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 28 , oOOOo00O00oOo + 'PROGRAMS.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']XXX[/COLOR]' , 'URL' , 29 , oOOOo00O00oOo + 'XXX.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 47 - 47: o0o00Oo0O * oOo0O0Ooo * oO0o . IIiIiII11i
 if 95 - 95: iIi1i1ii1 % OOoOoo . o0o00Oo0O % O00OOo00oo0o
def OOOii1i1iiI ( ) :
 IIiiiI1iIII ( )
 I1I11i ( 'CHECK ADVANCED XML' , str ( ooOO0O0ooOooO ) , 8 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 I1I11i ( 'MUCKYS XML' , str ( ooOO0O0ooOooO ) + '/wizard/muckys.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 I1I11i ( '0CACHE XML' , str ( ooOO0O0ooOooO ) + '/wizard/0cache.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 I1I11i ( 'MIKEY1234 XML' , str ( ooOO0O0ooOooO ) + '/wizard/mikey.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 I1I11i ( 'TUXENS XML' , str ( ooOO0O0ooOooO ) + '/wizard/tuxens.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 I1I11i ( 'P2P RECOMMENDED XML1' , str ( ooOO0O0ooOooO ) + '/wizard/p2p1.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 I1I11i ( 'P2P RECOMMENDED XML2' , str ( ooOO0O0ooOooO ) + '/wizard/p2p2.xml' , 7 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 I1I11i ( 'DELETE XML' , str ( ooOO0O0ooOooO ) , 11 , oOOOo00O00oOo + 'XML.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + IIi
def O00O ( ) :
 IIiiiI1iIII ( )
 I1I11i ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , O0o0Oo , '' )
 I1I11i ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 28 - 28: oOo0O0Ooo
def I11o0000o0Oo ( ) :
 IIiiiI1iIII ( )
 I1I11i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , O0o0Oo , '' )
 I1I11i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , O0o0Oo , '' )
 I1I11i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , O0o0Oo , '' )
 I1I11i ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , O0o0Oo , '' )
 if 90 - 90: iI11I1II1I1I * IIiIiII11i
 if 70 - 70: I11i * IIiIiII11i - IIiIi1iI
 if 55 - 55: oOo0O0Ooo
def oO0o0 ( ) :
 IIiiiI1iIII ( )
 OooOoOO0 = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  Ii1i1 ( )
 if iI1i11iII111 == 0 :
  oOoO00 ( iiOOooooO0Oo )
 if iI1i11iII111 == 0 :
  i1i ( iiOOooooO0Oo )
  if 27 - 27: iIi1i1ii1 * I1ii11iIi11i . OOooOOo
  if 17 - 17: IIiIiII11i % OooOO000 * IIi % ooOoO0O00 . oOo0O0Ooo . iI11I1II1I1I
  if 27 - 27: Ii - oOo0O0Ooo
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 35 - 35: ii - O00OOo00oo0o / oO0o
def iii11i1 ( ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1Oo00 )
 for oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , oOo0OOoO0 , oOo0OOoO0 , '' )
 i1Oo0oO00o ( 'tvshows' , 'INFO' )
 if 48 - 48: IIiIi1iI * Ii1I
def II111iIiI1Ii ( url ) :
 i1Oo00 = O000oo ( Ii1iiII1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 52 - 52: oo0oO00 / O00OOo00oo0o
def Ii1i1 ( ) :
 IIiiiI1iIII ( )
 I1IIII1i ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 91 - 91: OOoOoo . I1ii11iIi11i + IIiIiII11i
def Ii1I11i11I1i ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + oO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 7 - 7: o0o00Oo0O % O00OOo00oo0o + Ii1I + iIi1i1ii1 % ii . I1ii11iIi11i
def o0oOOooo00O ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OO0ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 7 - 7: Ii1I - oo0oO00 * IIi + I11i . Ii1I
def ooooO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + oO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 19 - 19: iIi1i1ii1
def O0o00oO0oOO ( url ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
def oOoO00 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OOOO0oOo00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 40 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 32 - 32: OOoOoo % iIi1i1ii1 - oOo0O0Ooo
def oo0ooooo00o ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OoOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 26 - 26: IIi
def Iii1IIII11I ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  Oo0oOo000OoO0 ( )
 if iI1i11iII111 == 1 :
  IIii1I1i ( )
 if iI1i11iII111 == 2 :
  IIII1iIIii ( )
  if 12 - 12: iI11I1II1I1I . iIi1i1ii1 . Ii1I % oOo0O0Ooo . IIiIiII11i . oo0oO00
  if 32 - 32: Ii1I + OOoOoo / o0o00Oo0O / OOooOOo * ii % IIiIi1iI
  if 50 - 50: oO0o
  if 66 - 66: iI11I1II1I1I
def IIii1I1i ( ) :
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , I11II1i11 in IIIII11I1IiI :
  i11i1iiiII ( 'Android Apps' + I11II1i11 , 'https://www.apkfiles.com' + iiOOooooO0Oo , 30035 , oOOOo00O00oOo + 'apps.png' )
 for iiOOooooO0Oo , I11II1i11 in i1I :
  i11i1iiiII ( 'Android Games' + I11II1i11 , 'https://www.apkfiles.com' + iiOOooooO0Oo , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def Ii1IIIII ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '/cat' in url :
   i11i1iiiII ( ( iiI11ii1I1 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def iiiIIiiii11 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '/app' in url :
   i11i1iiiII ( ( iiI11ii1I1 ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def IIiI1iIIiI1I1i ( url ) :
 OoO000O0Oo = O000oo ( url )
 IiIIiI = url
 if "page=" in str ( url ) :
  IiIIiI = url . split ( '?' ) [ 0 ]
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'apk' in url :
   I1I11i ( ( iiI11ii1I1 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + oOo0OOoO0 )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 I1I11i ( 'Next Page' , IiIIiI + str ( i1I ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def oOo0Oo0O0O ( name , url ) :
 OoO000O0Oo = I1iii11 ( url )
 name = name
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  III1II1i ( name , url , 'Brackets' )
def IIII1iIIii ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Iii = 'https://www.apkfiles.com/search?q=' + ( i1I11iIiII ) . replace ( ' ' , '+' ) + '&search_type=1'
 OO0OO0OO = i1Iii . lower ( )
 IIiI1iIIiI1I1i ( OO0OO0OO )
 if 3 - 3: OooOO000
def I1iIIIiI ( url ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( OoiI1I1 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , iiI11ii1I1 + '.apk' )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 27 - 27: IIiIi1iI - I1ii11iIi11i + OooOO000 - IIi . oOo0O0Ooo
def OOOOO0 ( url ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , iiI11ii1I1 + '.mp4' )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 79 - 79: IIiIiII11i - IIiIi1iI . ooOoO0O00 + o0o00Oo0O % o0o00Oo0O * oOo0O0Ooo
 if 7 - 7: ooOoO0O00 + IIi % OooOO000 / I11i + ooOoO0O00
def I1ii11I ( name , url , description ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , name )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 II1II1IIII = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print II1II1IIII
 print '======================================='
 extract . all ( ii1 , II1II1IIII , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 37 - 37: ii
 if 69 - 69: oOo0O0Ooo + OooOO000
 if 7 - 7: OooOO000 + oo0oO00
 if 26 - 26: iI11I1II1I1I + ooOoO0O00 / OOooOOo % Ii1I
 if 44 - 44: ii . IIiIiII11i . IIi % ii
def Oo0oOo000OoO0 ( ) :
 i1Oo00 = O000oo ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , iiOOooooO0Oo , oo00oO0o , iiii111II , Oo0oO00 in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 80003 , oo00oO0o , oOOOo00O00oOo + 'APKToolsB.png' , Oo0oO00 )
def ii11ii11I ( apk , ret = None ) :
 if apk == "kodi" :
  Oo0oo0oOO0oOo = "https://kodi.tv/download/"
  i1Oo00 = O000oo ( Oo0oo0oOO0oOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1Oo00 )
  if len ( IIIII11I1IiI ) == 1 :
   IiIII1i = IIIII11I1IiI [ 0 ] [ 0 ]
   oo0O = IIIII11I1IiI [ 0 ] [ 1 ]
   I11I11i1I1I11 = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( IiIII1i , oo0O )
  if ret == 'version' : return IiIII1i
  else : return I11I11i1I1I11
 elif apk == "spmc" :
  oo0O0o00 = 'https://github.com/koying/SPMC/releases/latest/'
  i1Oo00 = O000oo ( oo0O0o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1Oo00 )
  IiIII1i = re . sub ( '<[^<]+?>' , '' , IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  I11I11i1I1I11 = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( IiIII1i , IiIII1i )
  if ret == 'version' : return IiIII1i
  else : return I11I11i1I1I11
def III1II1i ( name , url ) :
 if Ii1I1I1i1Ii ( ) == 'android' :
  I1ii1i = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not I1ii1i : II11Ii111II1 ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  O00OOO00Ooo = name
  if I1ii1i :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not IIIIiII1i ( url ) == True : II11Ii111II1 ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % O00OOO00Ooo , '' , 'Please Wait' )
   ii1 = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( ii1 )
   except : pass
   downloader . download ( url , ii1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    I1iIIII1 = zipfile . ZipFile ( ii1 )
    for file in I1iIIII1 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as OOoO :
       OoOOoooO000 = file . split ( '/' ) [ 1 ]
       OOoO . write ( I1iIIII1 . read ( file ) )
       xbmc . sleep ( 500 )
       OOoO . close ( )
       try :
        os . remove ( ii1 )
       except :
        pass
       ii1 = os . path . join ( i1iiIII111ii , OoOOoooO000 )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ii1 + '")' )
  else : II11Ii111II1 ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : II11Ii111II1 ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 85 - 85: oOo0O0Ooo % iiII11i1I1IIi + IIi / iIi1i1ii1 % ii
 if 42 - 42: O00OOo00oo0o * OOoOoo
 if 23 - 23: oo0oO00 * O00OOo00oo0o - ii * ii % oO0o + IIiIiII11i
 if 9 - 9: iI11I1II1I1I * oO0o % O00OOo00oo0o
def I1iOOo0O ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1Oo00 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iiOOooooO0Oo = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + iiOOooooO0Oo )
  oOOoooO0O0 ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , iiOOooooO0Oo )
  if 46 - 46: iI11I1II1I1I
def oOOoooO0O0 ( name , url ) :
 if Ii1I1I1i1Ii ( ) == 'android' :
  I1ii1i = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not I1ii1i : II11Ii111II1 ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  O00OOO00Ooo = name
  if I1ii1i :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not IIIIiII1i ( url ) == True : II11Ii111II1 ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % O00OOO00Ooo , '' , 'Please Wait' )
   ii1 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( ii1 )
   except : pass
   downloader . download ( url , ii1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ii1 + '")' )
  else : II11Ii111II1 ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : II11Ii111II1 ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 33 - 33: iiII11i1I1IIi % iiII11i1I1IIi % o0o00Oo0O / oOo0O0Ooo . ooOoO0O00
 if 91 - 91: IIiIi1iI * iiII11i1I1IIi - IIiIiII11i . oOo0O0Ooo - I1ii11iIi11i + IIiIi1iI
def OO00o ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'INFO' )
 if 32 - 32: iI11I1II1I1I . iI11I1II1I1I . OooOO000 * iiII11i1I1IIi
 if 93 - 93: oo0oO00 * iIi1i1ii1
def IiIIi1 ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 30015 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 27 - 27: oOo0O0Ooo * IIiIi1iI
def oO0ooooo0O00 ( url , iconimage , fanart ) :
 i1Oo00 = O000oo ( url )
 iii11 = url
 oOo0OOoO0 = iconimage
 fanart = fanart
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for iII1iii , iiI11ii1I1 in IIIII11I1IiI :
  if '.mp4' in iiI11ii1I1 :
   I1I11i ( 'Watch VIDEO' , url + '/' + iII1iii , 222 , oOo0OOoO0 , fanart , '' )
  if 'description' in iiI11ii1I1 :
   I1I11i ( 'Read Description' , url + '/' + iII1iii , 30017 , oOo0OOoO0 , fanart , '' )
  if 'images' in iiI11ii1I1 :
   I1IIII1i ( 'View Images' , url + '/' + iII1iii , 30018 , oOo0OOoO0 , fanart , '' )
  if 'url' in iiI11ii1I1 :
   I1I11i ( 'Install Build On Android' , url + '/' + iII1iii , 30016 , oOo0OOoO0 , fanart , '' )
  if 'url' in iiI11ii1I1 :
   I1I11i ( 'Install Build On Pc' , url + '/' + iII1iii , 30019 , oOo0OOoO0 , fanart , '' )
 i1Oo0oO00o ( 'movies' , 'INFO' )
 if 5 - 5: OOooOOo % OooOO000 + OOoOoo
def iiiIi1II1III ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  I1i11II11i ( url )
  if 9 - 9: OOooOOo - Ii1I * IIiIi1iI . IIiIi1iI - oOo0O0Ooo
def OOooOooo0OOo0 ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  oo0o0OoOO0o0 ( url )
  if 14 - 14: I11i % OOoOoo + Ii1I + oO0o
def OOOoOOo0o ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1Oo00 )
 for IiI1Iii1 in IIIII11I1IiI :
  iiIiI1i1 ( 'Description:' , IiI1Iii1 )
  if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
def OooOo ( url ) :
 i1Oo00 = O000oo ( url )
 url = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for iII1iii , iiI11ii1I1 in IIIII11I1IiI :
  if 'png' in iiI11ii1I1 :
   I1I11i ( 'image' , '' , '' , url + '/' + iII1iii , url + '/' + iII1iii , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 67 - 67: I1ii11iIi11i / o0o00Oo0O
def oO0Oo00oo ( name , url , description ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , name + '.zip' )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 I1iIIiiIIi1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1iIIiiIIi1i
 print '======================================='
 extract . all ( ii1 , I1iIIiiIIi1i , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oOOo0O00o ( )
 if 75 - 75: iI11I1II1I1I * Ii - ii . OOooOOo
 if 70 - 70: oo0oO00 * oo0oO00 + I1ii11iIi11i * IIi % oOo0O0Ooo + iI11I1II1I1I
def oo0o0OoOO0o0 ( url ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 I1iIIiiIIi1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1iIIiiIIi1i
 print '======================================='
 extract . all ( ii1 , I1iIIiiIIi1i , o0oOoO00o )
 O0O0ooOOO ( url )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IioO0O ( )
 if 2 - 2: Ii
def I1i11II11i ( url ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 I1iIIiiIIi1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1iIIiiIIi1i
 print '======================================='
 extract . all ( ii1 , I1iIIiiIIi1i , o0oOoO00o )
 O0O0ooOOO ( url )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IioO0O ( )
 if 98 - 98: oo0oO00 / oO0o - iIi1i1ii1 - oOo0O0Ooo / OOooOOo + Ii
def i1I1IiI1ii ( name , url , description ) :
 I1iIIiiIIi1i = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 ii1 = os . path . join ( oOOoO0 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print I1iIIiiIIi1i
 print '======================================='
 extract . all ( ii1 , I1iIIiiIIi1i , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 IioO0O ( )
 if 64 - 64: OooOO000 * Ii1I % IIiIiII11i - OOooOOo + Ii1I
def Ii1I1I1i1Ii ( ) :
 if xbmc . getCondVisibility ( 'system.platform.android' ) : return 'android'
 elif xbmc . getCondVisibility ( 'system.platform.linux' ) : return 'linux'
 elif xbmc . getCondVisibility ( 'system.platform.windows' ) : return 'windows'
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) : return 'osx'
 elif xbmc . getCondVisibility ( 'system.platform.atv2' ) : return 'atv2'
 elif xbmc . getCondVisibility ( 'system.platform.ios' ) : return 'ios'
def OOO ( log ) :
 xbmc . log ( "[%s]: %s" % ( oO , log ) )
 if not os . path . exists ( oO0o0o0ooO0oO ) : os . makedirs ( oO0o0o0ooO0oO )
 if not os . path . exists ( oo0o0O00 ) : OOoO = open ( oo0o0O00 , 'w' ) ; OOoO . close ( )
 with open ( oo0o0O00 , 'a' ) as OOoO :
  OO0OOoo0OOO = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  OOoO . write ( OO0OOoo0OOO . rstrip ( '\r\n' ) + '\n' )
def IioO0O ( ) :
 iI1i11iII111 = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iI1i11iII111 == 0 : return
 elif iI1i11iII111 == 1 : pass
 ooooOoo0OO = Ii1I1I1i1Ii ( )
 OOO ( "Platform: " + str ( ooooOoo0OO ) )
 os . _exit ( 1 )
 OOO ( "Force close failed!  Trying alternate methods." )
 if ooooOoo0OO == 'osx' :
  OOO ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif ooooOoo0OO == 'linux' :
  OOO ( "############ try linux force close #################" )
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif ooooOoo0OO == 'android' :
  OOO ( "############ try android force close #################" )
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
 elif ooooOoo0OO == 'windows' :
  OOO ( "############ try windows force close #################" )
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
  OOO ( "############ try atv force close #################" )
  try : os . system ( 'killall AppleTV' )
  except : pass
  OOO ( "############ try raspbmc force close #################" )
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu." , "iOS detected. Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo." )
  if 85 - 85: IIiIiII11i . IIiIi1iI % IIi % iiII11i1I1IIi
  if 80 - 80: oo0oO00 * iiII11i1I1IIi / iI11I1II1I1I % oo0oO00 / iI11I1II1I1I
  if 42 - 42: ooOoO0O00 / Ii . I1ii11iIi11i * OooOO000 . Ii * o0o00Oo0O
def i1i ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for Iii , oo0 , i1iIIi1II1iiI in os . walk ( url ) :
  for file in i1iIIi1II1iiI :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    III1I11i1iIi = open ( ( os . path . join ( Iii , file ) ) ) . read ( )
    i1iI111II1ii = III1I11i1iIi . replace ( Oo0o0000o0o0 , 'special://home/' )
    OOoO = open ( ( os . path . join ( Iii , file ) ) , mode = 'w' )
    OOoO . write ( str ( i1iI111II1ii ) )
    OOoO . close ( )
 IioO0O ( )
 if 62 - 62: OooOO000 * iI11I1II1I1I . OOoOoo - ii * IIiIiII11i
def oO0oI1I1 ( ) :
 i11i1iiiII ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 i11i1iiiII ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 i11i1iiiII ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 45 - 45: o0o00Oo0O % oOo0O0Ooo - OooOO000 . oO0o
def I1II ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def iIIi1Ii1III ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def Oooo00 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1I :
  i11i1iiiII ( ( '[COLOR' + II + ']Filter - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( '[COLOR' + II + ']Stream - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oOo0OOoO0 )
def iii1II1iI1IIi ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( url )
def Ii11iiI1 ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII
 oO0O = 'https://www.radionomy.com/en/search/index?query=' + ( i1I11iIiII ) . replace ( ' ' , '+' )
 I1 = O000oo ( oO0O )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( '[COLOR' + II + ']Stream - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + iiOOooooO0Oo , 70005 , oOo0OOoO0 )
  if 70 - 70: oO0o % oOo0O0Ooo / oOo0O0Ooo . iiII11i1I1IIi % IIiIi1iI . IIiIiII11i
  if 10 - 10: iIi1i1ii1 - Ii . Ii1I % ooOoO0O00
def iI1iIiiiI1I1 ( ) :
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , 'http://www.listenlive.eu/' + iiOOooooO0Oo , 10111113 , oOOOo00O00oOo + 'radio.png' )
def OOooO0OO0 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  ooOO0oO0oo00o ( iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 78 - 78: iI11I1II1I1I * I1ii11iIi11i . I1ii11iIi11i - IIi . iI11I1II1I1I
def I111I1I ( ) :
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.toonjet.com/' + iiOOooooO0Oo , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0000 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 in IIIII11I1IiI :
  if 'ol.gif' in oOo0OOoO0 :
   pass
  elif 'link_block_' in oOo0OOoO0 :
   pass
  elif '.png' in oOo0OOoO0 :
   pass
  else :
   i11i1iiiII ( ( oOo0OOoO0 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOOo00O00oOo + 'vod.png' )
 for url in i1I :
  i11i1iiiII ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOOo00O00oOo + 'Next.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0OoOo ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  ooOO0oO0oo00o ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 89 - 89: I1ii11iIi11i + Ii1I - I11i
  if 40 - 40: oO0o + oO0o
def O0oOo00Ooo0o0 ( ) :
 o0oo0o00ooO00 ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 o0oo0o00ooO00 ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 37 - 37: oO0o - Ii1I . ii . IIiIi1iI + OOooOOo / iIi1i1ii1
def I1oOoO0OOO00O ( ) :
 o0oo0o00ooO00 ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 o0oo0o00ooO00 ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 o0oo0o00ooO00 ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 73 - 73: I11i % oO0o + OOoOoo + oOo0O0Ooo
def OoOO00 ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for iiI11ii1I1 , iiOOooooO0Oo , O0O00OoOoOOo in IIIII11I1IiI :
  if 'Parent' in iiI11ii1I1 :
   pass
  elif '2' in O0O00OoOoOOo :
   o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 58 - 58: OOoOoo + iI11I1II1I1I
def o0II1IIi1iII1i ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for iiI11ii1I1 , iiOOooooO0Oo , O0O00OoOoOOo in IIIII11I1IiI :
  if i1I11iIiII in iiI11ii1I1 . lower ( ) :
   if '1' in O0O00OoOoOOo :
    o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in O0O00OoOoOOo :
    o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in O0O00OoOoOOo :
    o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 26 - 26: o0o00Oo0O
    if 17 - 17: IIiIiII11i
def iiIiii ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for iiI11ii1I1 , iiOOooooO0Oo , O0O00OoOoOOo in IIIII11I1IiI :
  if '1' in O0O00OoOoOOo :
   o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in O0O00OoOoOOo :
   o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in O0O00OoOoOOo :
   o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 39 - 39: oOo0O0Ooo + I1ii11iIi11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 83 - 83: ooOoO0O00
def O0OooOO ( url ) :
 iII1iii = url
 I1 = O000oo ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
 for url , iiI11ii1I1 in i1I :
  if 'mp3' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iII1iii + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iII1iii + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , iII1iii + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in iiI11ii1I1 :
   o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iII1iii + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 49 - 49: OOoOoo / IIiIi1iI / IIi
   if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - IIiIi1iI
   if 38 - 38: I11i % O00OOo00oo0o + Ii + OooOO000 + IIiIi1iI / Ii
def o0OOOOOo0 ( url ) :
 I1 = O000oo ( url )
 iII1iii = url
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'Parent' in iiI11ii1I1 :
   pass
  elif '.db' in iiI11ii1I1 :
   pass
  elif '.jpg' in iiI11ii1I1 :
   pass
  elif '.html' in iiI11ii1I1 :
   pass
  elif '.doc' in iiI11ii1I1 :
   pass
  elif 'mp3' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iII1iii + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iII1iii + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , iII1iii + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 57 - 57: iI11I1II1I1I + iI11I1II1I1I
   if 56 - 56: oo0oO00 + IIiIi1iI
def Ii1Ii1 ( ) :
 o0oo0o00ooO00 ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 o0oo0o00ooO00 ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 o0oo0o00ooO00 ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 35 - 35: Ii - oo0oO00 % Ii
def II111I1Iii ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 in IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iiOOooooO0Oo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oOo0OOoO0 :
   pass
  else :
   o0oo0o00ooO00 ( oOo0OOoO0 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iiOOooooO0Oo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oOo0OOoO0 + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 84 - 84: I1ii11iIi11i % OooOO000 % ii + IIi % Ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * oo0oO00 . iiII11i1I1IIi / ooOoO0O00
 if 50 - 50: O00OOo00oo0o / ooOoO0O00 % ii
def oOOOOO0Ooooo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '</a>' in iiI11ii1I1 :
   pass
  elif '(' in iiI11ii1I1 :
   o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 57 - 57: iIi1i1ii1 - ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 68 - 68: I11i % Ii1I / O00OOo00oo0o + O00OOo00oo0o - O00OOo00oo0o . oO0o
def oOO00ooOOo ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if i1I11iIiII in iiI11ii1I1 . lower ( ) :
   if '</a>' in iiI11ii1I1 :
    pass
   elif '(' in iiI11ii1I1 :
    o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 20 - 20: Ii1I
    if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
def OOoooOoO0 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if '</a>' in iiI11ii1I1 :
   pass
  elif '(' in iiI11ii1I1 :
   o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 95 - 95: iIi1i1ii1 - Ii1I - o0o00Oo0O . oOo0O0Ooo . OooOO000
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: O00OOo00oo0o
 if 45 - 45: o0o00Oo0O - IIi
def oo0oOO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iII1iii = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( iII1iii )
  if 2 - 2: OOoOoo % oOo0O0Ooo - O00OOo00oo0o
def oooOo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '<p align' in iiI11ii1I1 :
   pass
  elif '&nbsp;' in iiI11ii1I1 :
   pass
  else :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 79 - 79: oo0oO00 - IIiIiII11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 43 - 43: ooOoO0O00 + o0o00Oo0O % oO0o / iIi1i1ii1 * oOo0O0Ooo
 if 89 - 89: oOo0O0Ooo . I1ii11iIi11i + Ii1I . o0o00Oo0O % I11i
def O00O0OO00oo ( ) :
 I1 = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'ongoing' in iiOOooooO0Oo :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 21005 , oOOOo00O00oOo + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in iiOOooooO0Oo :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 21005 , oOOOo00O00oOo + 'CartoonShows.png' , '' , '' )
  if 'disney' in iiOOooooO0Oo :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 21005 , oOOOo00O00oOo + 'Disney.png' , '' , '' )
  if 'genre' in iiOOooooO0Oo :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 21005 , oOOOo00O00oOo + 'Genre.png' , '' , '' )
  if 'years' in iiOOooooO0Oo :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 21005 , oOOOo00O00oOo + 'Years.png' , '' , '' )
def Ooo00O0 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 OoO0OOoO0 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , oOo0OOoO0 , oOo0OOoO0 , iiI11ii1I1 )
 for url , iiI11ii1I1 in OoO0OOoO0 :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IIII1i ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def iiI11i ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 IiI1iII1II111 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o0OoiiI1i = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 i11I = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in o0OoiiI1i :
  I1IIII1i ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , iiI11ii1I1 in IiI1iII1II111 :
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  I1IIII1i ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def o0oO0o0oo0O0 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 98 - 98: OOoOoo * iI11I1II1I1I . iIi1i1ii1 * I1ii11iIi11i / Ii1I + IIiIi1iI
def ooo0oooo0 ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if '9cart' in iiOOooooO0Oo :
   i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 25 - 25: oo0oO00
def Iii11111iiI ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( I1 )
 I1II1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if '9cart' in url :
   i11i1iiiII ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   i11i1iiiII ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url , iiI11ii1I1 in I1II1 :
  if '9cart' in url :
   i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 67 - 67: I11i
def OOOoO00O ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20003 , oOo0OOoO0 )
 for url , iiI11ii1I1 in i1I :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 27 - 27: Ii1I * ooOoO0O00 . ooOoO0O00
def o0O0O ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'Watch' in url :
   i11i1iiiII ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 56 - 56: o0o00Oo0O
def iIIIII1iI ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 18 - 18: I1ii11iIi11i - o0o00Oo0O
def O00oooooo ( url ) :
 url = cloudflare . source ( url )
 O0ooOO ( url )
 if 31 - 31: IIiIiII11i % IIiIi1iI % iIi1i1ii1 * O00OOo00oo0o % Ii
def IIIIIII1iIi ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in IIIII11I1IiI :
  O0ooOO ( url )
  if 75 - 75: iIi1i1ii1 - iiII11i1I1IIi % OOooOOo
  if 80 - 80: iIi1i1ii1 / IIi
def oOOO ( ) :
 if 21 - 21: I1ii11iIi11i - iI11I1II1I1I - O00OOo00oo0o
 I1IIII1i ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 1 - 1: oOo0O0Ooo * IIi + iIi1i1ii1 + oOo0O0Ooo - Ii
def OOooO ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 79 - 79: IIiIi1iI . oo0oO00 / oo0oO00 - IIiIi1iI * I1ii11iIi11i / I11i
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 19 - 19: Ii1I
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if i1I11iIiII in iiI11ii1I1 . lower ( ) :
   if 'Dad!' in iiI11ii1I1 :
    pass
   elif 'Family Guy' in iiI11ii1I1 :
    pass
   elif '2 Stupid' in iiI11ii1I1 :
    pass
   elif 'The Zelfs' in iiI11ii1I1 :
    pass
   elif 'A Clone' in iiI11ii1I1 :
    pass
   elif 'A.T.O.M' in iiI11ii1I1 :
    pass
   elif 'Almost Naked' in iiI11ii1I1 :
    pass
   elif 'Angry Kid' in iiI11ii1I1 :
    pass
   elif 'Annoying Orange' in iiI11ii1I1 :
    pass
   elif 'Aqua Teen' in iiI11ii1I1 :
    pass
   elif 'Assy Mcgee' in iiI11ii1I1 :
    pass
   elif 'Astroblast' in iiI11ii1I1 :
    pass
   elif 'Atomic Betty' in iiI11ii1I1 :
    pass
   elif 'Axe Cop' in iiI11ii1I1 :
    pass
   elif 'Baby Playpen' in iiI11ii1I1 :
    pass
   elif 'Beavis and Butt' in iiI11ii1I1 :
    pass
   elif 'Celebrity Deathmatch' in iiI11ii1I1 :
    pass
   elif 'Clerks The' in iiI11ii1I1 :
    pass
   elif 'Crapston Villas' in iiI11ii1I1 :
    pass
   elif 'Duckman:' in iiI11ii1I1 :
    pass
   elif 'Stripperella' in iiI11ii1I1 :
    pass
   elif 'Vixen' in iiI11ii1I1 :
    pass
   else :
    I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
    if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
    if 66 - 66: o0o00Oo0O
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 52 - 52: oO0o * ii
def OOO0ooo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'Dad!' in iiI11ii1I1 :
   pass
  elif 'Family Guy' in iiI11ii1I1 :
   pass
  elif '2 Stupid' in iiI11ii1I1 :
   pass
  elif 'The Zelfs' in iiI11ii1I1 :
   pass
  elif 'A Clone' in iiI11ii1I1 :
   pass
  elif 'A.T.O.M' in iiI11ii1I1 :
   pass
  elif 'Almost Naked' in iiI11ii1I1 :
   pass
  elif 'Angry Kid' in iiI11ii1I1 :
   pass
  elif 'Annoying Orange' in iiI11ii1I1 :
   pass
  elif 'Aqua Teen' in iiI11ii1I1 :
   pass
  elif 'Assy Mcgee' in iiI11ii1I1 :
   pass
  elif 'Astroblast' in iiI11ii1I1 :
   pass
  elif 'Atomic Betty' in iiI11ii1I1 :
   pass
  elif 'Axe Cop' in iiI11ii1I1 :
   pass
  elif 'Baby Playpen' in iiI11ii1I1 :
   pass
  elif 'Beavis and Butt' in iiI11ii1I1 :
   pass
  elif 'Celebrity Deathmatch' in iiI11ii1I1 :
   pass
  elif 'Clerks The' in iiI11ii1I1 :
   pass
  elif 'Crapston Villas' in iiI11ii1I1 :
   pass
  elif 'Duckman:' in iiI11ii1I1 :
   pass
  elif 'Stripperella' in iiI11ii1I1 :
   pass
  elif 'Vixen' in iiI11ii1I1 :
   pass
  else :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: o0o00Oo0O + OOoOoo * ooOoO0O00 . oO0o
def o0OO0oooo ( url ) :
 OoO000O0Oo = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 in i1I :
  I11II1i1 = oOo0OOoO0
 I1II1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1II1 :
  I1IIII1i ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10007 , I11II1i1 )
  if 46 - 46: IIiIiII11i % OooOO000 - ooOoO0O00 / iiII11i1I1IIi * OOooOOo
  if 92 - 92: I1ii11iIi11i - O00OOo00oo0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: oo0oO00 / O00OOo00oo0o / iiII11i1I1IIi % OOooOOo / Ii1I * IIiIi1iI
def iiIiIIi11I1 ( url , IMAGE ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  print iiI11ii1I1 + '     ' + url
  if 'easy' in url :
   oooOoOo0o00o ( url )
   if 2 - 2: IIiIiII11i
   if 54 - 54: iIi1i1ii1 . ii % I1ii11iIi11i
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 22 - 22: IIi
def oooOoOo0o00o ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( url )
  if 22 - 22: OooOO000 * iiII11i1I1IIi - I1ii11iIi11i * o0o00Oo0O / Ii
  if 78 - 78: I1ii11iIi11i * o0o00Oo0O / IIiIi1iI + ii + IIi
  if 23 - 23: OooOO000 % ii / iI11I1II1I1I + Ii1I / ooOoO0O00 / I11i
def o0o0O ( ) :
 if 94 - 94: ooOoO0O00
 I1IIII1i ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , O0o0Oo , '' )
 if 36 - 36: oOo0O0Ooo + I1ii11iIi11i
def iIIiiiI1iI1 ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'elete' in iiI11ii1I1 :
   pass
  else :
   ooOO0oO0oo00o ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 222 , oOo0OOoO0 )
   if 86 - 86: Ii1I * IIiIi1iI
def O0oO0o0OOOOOO ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiI1i11IiIiii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , I11iiI1I1 , i1iII1IiiIiI1 in IiI1i11IiIiii :
  for i1I11iIiII in I11iiI1I1 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   o0i1Ii11II = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for iiOOooooO0Oo , iiI11ii1I1 in o0i1Ii11II :
    if 'tube' in iiOOooooO0Oo :
     pass
    elif 'stage' in iiOOooooO0Oo :
     ooOO0oO0oo00o ( '[COLOR' + II + ']' + I11iiI1I1 + '   -   ' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0OOoO0 , )
    elif 'vee' in iiOOooooO0Oo :
     pass
     if 33 - 33: OOoOoo . ii . oo0oO00
def iI1 ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiI1i11IiIiii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , I11iiI1I1 , i1iII1IiiIiI1 in IiI1i11IiIiii :
  o0i1Ii11II = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for iiOOooooO0Oo , iiI11ii1I1 in o0i1Ii11II :
   if 'tube' in iiOOooooO0Oo :
    pass
   elif 'stage' in iiOOooooO0Oo :
    ooOO0oO0oo00o ( '[COLOR' + II + ']' + I11iiI1I1 + '   -   ' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0OOoO0 )
   elif 'vee' in iiOOooooO0Oo :
    pass
    if 94 - 94: iiII11i1I1IIi . oOo0O0Ooo
    if 73 - 73: ooOoO0O00 / IIiIiII11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: iIi1i1ii1 / IIiIi1iI . ii + oO0o
def iii1I1i ( url ) :
 I1 = O000oo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 OOOOooO0oO00O0o = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( OOOOooO0oO00O0o ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in OOOOooO0oO00O0o :
  iii1 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 51 - 51: OooOO000 % Ii % OOoOoo + O00OOo00oo0o % Ii1I
  if 16 - 16: OOooOOo / I1ii11iIi11i + o0o00Oo0O - OOooOOo . ii
  if 19 - 19: I11i
  if 73 - 73: O00OOo00oo0o * I1ii11iIi11i * OOooOOo
  if 65 - 65: Ii + I1ii11iIi11i * ii - oO0o
  if 26 - 26: I11i % IIi + IIi % iiII11i1I1IIi * Ii / OooOO000
  if 64 - 64: oo0oO00 % OOooOOo / IIiIiII11i % IIiIi1iI - OooOO000
def O0iIiIIIIIii ( ) :
 if 2 - 2: O00OOo00oo0o - Ii1I + I11i * oO0o / OooOO000
 iIIiI11iI1Ii1 ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 iIIiI11iI1Ii1 ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 94 - 94: IIiIi1iI / Ii % o0o00Oo0O
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 70 - 70: iiII11i1I1IIi - I1ii11iIi11i / ii % ii
def oooo0o0OOO0 ( ) :
 iIIiI11iI1Ii1 ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 iIIiI11iI1Ii1 ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 17 - 17: IIiIiII11i + oOo0O0Ooo
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def ooo0oO0oOo ( ) :
 if 61 - 61: O00OOo00oo0o % oOo0O0Ooo + I1ii11iIi11i + IIiIi1iI * O00OOo00oo0o % IIi
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 iiiI11 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 89 - 89: oo0oO00
 for OoooO0o in iiiI11 :
  IIIii1iiIi = OOOO0OOoO0O0 + OoooO0o + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( IIIii1iiIi )
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for iiOOooooO0Oo , ooI1i , I111iIi1 , iiii111II , iiI11ii1I1 in IIIII11I1IiI :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    o0OOOOOo00 ( iiI11ii1I1 , iiOOooooO0Oo , 222 , ooI1i , iiii111II , I111iIi1 )
    if 82 - 82: I1ii11iIi11i
    i1Oo0oO00o ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 5 - 5: oO0o / oO0o - o0o00Oo0O - O00OOo00oo0o + O00OOo00oo0o
    if 99 - 99: iiII11i1I1IIi * ii / I11i . OOoOoo - iI11I1II1I1I - iIi1i1ii1
def I1iIiIii ( ) :
 if 76 - 76: oO0o . ii % O00OOo00oo0o * iIi1i1ii1
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 iiiI11 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 23 - 23: OOoOoo + iI11I1II1I1I
 for OoooO0o in iiiI11 :
  Ii1111III1 = OOOO0OOoO0O0 + OoooO0o + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( Ii1111III1 )
  IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for iiI11ii1I1 , I111iIi1 , iiOOooooO0Oo , oOo0OOoO0 , iiii111II , iiiii1II in IIIII11I1IiI :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    iIIiI11iI1Ii1 ( iiI11ii1I1 , iiOOooooO0Oo , iiiii1II , oOo0OOoO0 , iiii111II , I111iIi1 )
    if 74 - 74: Ii1I - OooOO000 * ooOoO0O00
    i1Oo0oO00o ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 12 - 12: o0o00Oo0O
    if 75 - 75: iI11I1II1I1I % OOoOoo + Ii1I * o0o00Oo0O . OooOO000 - IIiIi1iI
def i1IIiIIIi1 ( ) :
 if 84 - 84: oo0oO00 + IIi . OooOO000
 OoO000O0Oo = O000oo ( OOOO0OOoO0O0 + 'spongemain.php' )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , I111iIi1 , iiOOooooO0Oo , oOo0OOoO0 , iiii111II , iiiii1II in IIIII11I1IiI :
  iIIiI11iI1Ii1 ( iiI11ii1I1 , iiOOooooO0Oo , iiiii1II , oOo0OOoO0 , iiii111II , I111iIi1 )
  i1Oo0oO00o ( 'movies' , 'MAIN' )
def O0o00 ( url ) :
 if 48 - 48: iiII11i1I1IIi + IIiIi1iI + OooOO000 / iiII11i1I1IIi / OooOO000
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOO0O00OO00 = ( '%s%s' % ( oo0o0Oo0 , url ) )
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , ooI1i , I111iIi1 , OOOoO000 , iiI11ii1I1 in IIIII11I1IiI :
  oooo0OOo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
  for oOOOoo00 in oooo0OOo :
   if oOOOoo00 == url :
    iiI11ii1I1 = ( '[COLORred]Watched - [/COLOR]' + iiI11ii1I1 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  o0OOOOOo00 ( iiI11ii1I1 , url , 222 , ooI1i , OOOoO000 , I111iIi1 )
  if 59 - 59: iiII11i1I1IIi * ii + IIi . iI11I1II1I1I / ooOoO0O00
  i1Oo0oO00o ( 'movies' , 'MAIN' )
  if 75 - 75: iiII11i1I1IIi . IIi - iI11I1II1I1I * oO0o * OooOO000
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 93 - 93: IIiIi1iI
  if 18 - 18: IIiIi1iI
def OOOooO00OO00O ( url ) :
 if 78 - 78: IIiIiII11i - I1ii11iIi11i - o0o00Oo0O . IIi + Ii - Ii1I
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , I111iIi1 , url , oOo0OOoO0 , iiii111II , iiiii1II in IIIII11I1IiI :
  iIIiI11iI1Ii1 ( iiI11ii1I1 , url , iiiii1II , oOo0OOoO0 , iiii111II , I111iIi1 )
  if 58 - 58: iIi1i1ii1 % ii
  i1Oo0oO00o ( 'movies' , 'MAIN' )
  if 49 - 49: Ii1I + o0o00Oo0O . iIi1i1ii1 * ii
  if 82 - 82: Ii1I
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 54 - 54: I11i + iiII11i1I1IIi - iI11I1II1I1I % IIiIi1iI % OOoOoo
def o0OOOOOo00 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 19 - 19: Ii1I / iI11I1II1I1I % ooOoO0O00 . ii
 i11iIIi11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooOooo000OO00 = True
 IiIiI1I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIiI1I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiIiI1I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I11oo0ooOO = [ ]
  I11oo0ooOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I11oo0ooOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   I11oo0ooOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiIiI1I1I1 . addContextMenuItems ( I11oo0ooOO )
 ooOooo000OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iIIi11 , listitem = IiIiI1I1I1 , isFolder = False )
 return ooOooo000OO00
 if 57 - 57: IIiIi1iI . I1ii11iIi11i - oO0o - Ii * O00OOo00oo0o / I11i
def iIIiI11iI1Ii1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 79 - 79: Ii1I + I11i % I1ii11iIi11i * I11i
 i11iIIi11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooOooo000OO00 = True
 IiIiI1I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIiI1I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiIiI1I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I11oo0ooOO = [ ]
  I11oo0ooOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I11oo0ooOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   I11oo0ooOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiIiI1I1I1 . addContextMenuItems ( I11oo0ooOO )
 ooOooo000OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iIIi11 , listitem = IiIiI1I1I1 , isFolder = True )
 return ooOooo000OO00
if 21 - 21: OooOO000
if 24 - 24: OooOO000 / IIiIi1iI
if 61 - 61: iI11I1II1I1I + oo0oO00
if 8 - 8: O00OOo00oo0o + oO0o
if 9 - 9: IIi + I11i
if 8 - 8: IIi * I1ii11iIi11i / OooOO000 - oO0o - ii
if 100 - 100: oo0oO00 . iI11I1II1I1I . iI11I1II1I1I
if 55 - 55: oo0oO00
if 37 - 37: OOoOoo / Ii / I1ii11iIi11i
if 97 - 97: O00OOo00oo0o . iiII11i1I1IIi / oOo0O0Ooo
if 83 - 83: iiII11i1I1IIi - Ii1I * oo0oO00
if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
if 75 - 75: Ii1I - OOooOOo * Ii . ii - I1ii11iIi11i . iiII11i1I1IIi
if 6 - 6: iiII11i1I1IIi * oo0oO00 / ii % iIi1i1ii1 * I11i
if 28 - 28: OOoOoo * oOo0O0Ooo % OOoOoo
def ooo00 ( string ) :
 if OOO00O == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 17 - 17: iiII11i1I1IIi
def o0OO0OO000OO ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 O00o0000OO = [ ]
 try :
  if 61 - 61: OOoOoo % ooOoO0O00 - OooOO000 . IIiIi1iI - I1ii11iIi11i + I1ii11iIi11i
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( OOOOi11i1 ) == False :
  ooo00 ( 'Making Favorites File' )
  O00o0000OO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  III1I11i1iIi = open ( OOOOi11i1 , "w" )
  III1I11i1iIi . write ( json . dumps ( O00o0000OO ) )
  III1I11i1iIi . close ( )
 else :
  ooo00 ( 'Appending Favorites' )
  III1I11i1iIi = open ( OOOOi11i1 ) . read ( )
  II1i = json . loads ( III1I11i1iIi )
  II1i . append ( ( name , url , iconimage , fanart , mode ) )
  i1iI111II1ii = open ( OOOOi11i1 , "w" )
  i1iI111II1ii . write ( json . dumps ( II1i ) )
  i1iI111II1ii . close ( )
  if 30 - 30: iiII11i1I1IIi / Ii1I
  if 22 - 22: oo0oO00 * OooOO000
def iIIIiIi1i ( ) :
 if os . path . exists ( OOOOi11i1 ) == False :
  O00o0000OO = [ ]
  ooo00 ( 'Making Favorites File' )
  O00o0000OO . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  III1I11i1iIi = open ( OOOOi11i1 , "w" )
  III1I11i1iIi . write ( json . dumps ( O00o0000OO ) )
  III1I11i1iIi . close ( )
 else :
  iiIiiIi = json . loads ( open ( OOOOi11i1 ) . read ( ) )
  ooOo0o = len ( iiIiiIi )
  for III in iiIiiIi :
   iiI11ii1I1 = III [ 0 ]
   iiOOooooO0Oo = III [ 1 ]
   ooI1i = III [ 2 ]
   try :
    IiiIOoO = III [ 3 ]
    if IiiIOoO == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     IiiIOoO = ooI1i
    else :
     IiiIOoO = iiii111II
   try : oO00o00 = III [ 5 ]
   except : oO00o00 = None
   try : OOooooO0o0O0 = III [ 6 ]
   except : OOooooO0o0O0 = None
   if 74 - 74: OOooOOo / ooOoO0O00 % ii
   if III [ 4 ] == 0 :
    I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , '' , ooI1i , iiii111II , '' , 'fav' )
   else :
    I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , III [ 4 ] , ooI1i , iiii111II , '' , 'fav' )
    if 52 - 52: OOoOoo % IIiIi1iI
def I111 ( name ) :
 II1i = json . loads ( open ( OOOOi11i1 ) . read ( ) )
 for oOOooo00OOooO in range ( len ( II1i ) ) :
  if II1i [ oOOooo00OOooO ] [ 0 ] == name :
   del II1i [ oOOooo00OOooO ]
   i1iI111II1ii = open ( OOOOi11i1 , "w" )
   i1iI111II1ii . write ( json . dumps ( II1i ) )
   i1iI111II1ii . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 31 - 31: oOo0O0Ooo / I11i + oOo0O0Ooo - IIiIiII11i
 if 29 - 29: oOo0O0Ooo + Ii . o0o00Oo0O
def IiIiIi1I1 ( ) :
 o0oo0Oo = os . path . join ( I11i1 , 'addons.ini' )
 i1i1I1II = open ( o0oo0Oo , "w+" )
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 i1i1I1II . write ( r'[' + IiII + ']' + '\n' )
 for iiI11ii1I1 , oOo0OOoO0 , o0Oo , iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = ( iiOOooooO0Oo + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  o0o0oO = ( iiI11ii1I1 + '=plugin://' + IiII + '/?url=' + iiOOooooO0Oo + '&mode=10012&name=' + ( iiI11ii1I1 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOo0OOoO0 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOo0OOoO0 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  i1i1I1II . write ( o0o0oO + '\n' )
  if 92 - 92: iiII11i1I1IIi / o0o00Oo0O * oOo0O0Ooo - iiII11i1I1IIi
  if 99 - 99: Ii % ii
def o0000O00oO0O ( ) :
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo in IIIII11I1IiI :
  i11i1iiiII ( '24/7' , iiOOooooO0Oo , 90021 , oOOOo00O00oOo + '247Streams.png' )
  if 3 - 3: iI11I1II1I1I % Ii1I . IIi % iiII11i1I1IIi
def I1i1I1Iiiii1 ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + '247Streams.png' , oOOOo00O00oOo + '247Streams.png' , '' )
def O0Oo0 ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def oOOOo00O00O ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def O0Ooo0O ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def iii1oOo0OoOOOo0 ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 55 - 55: oo0oO00 + o0o00Oo0O / OooOO000 % IIiIi1iI / ii
  if 98 - 98: iIi1i1ii1 * iI11I1II1I1I % I1ii11iIi11i % IIi
def O0ooO00o ( ) :
 if 24 - 24: O00OOo00oo0o + ii . OOoOoo / OOooOOo / iiII11i1I1IIi
 I1IIII1i ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 if 65 - 65: ii
def iiii11iI1 ( ) :
 if 81 - 81: Ii + iIi1i1ii1 % Ii - ooOoO0O00
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , iii1IIIiiiI in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 + '  -  ' + ( iii1IIIiiiI ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiOOooooO0Oo , 10023 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 9 - 9: oo0oO00
  if 2 - 2: iI11I1II1I1I * oOo0O0Ooo % ooOoO0O00 % Ii1I + ii + oOo0O0Ooo
  if 16 - 16: IIi
def oooO0o0oOoO ( ) :
 if 23 - 23: OOoOoo + iI11I1II1I1I % iI11I1II1I1I / IIiIi1iI . oo0oO00 + iI11I1II1I1I
 I1IIII1i ( '[COLOR' + II + ']Action[/COLOR]' , 'Aksiyon' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Adventure[/COLOR]' , 'Macera' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Animation[/COLOR]' , 'Animasyon' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Anime[/COLOR]' , 'Anime' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Biography[/COLOR]' , 'Biyografi' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Comedy[/COLOR]' , 'Komedi' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Crime[/COLOR]' , 'Su%C3%A7' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Documentary[/COLOR]' , 'Belgesel' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Drama[/COLOR]' , 'Dram' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Family[/COLOR]' , 'Aile' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Fantasy[/COLOR]' , 'Fantastik' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']History[/COLOR]' , 'Tarih' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Horror[/COLOR]' , 'Korku' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Mini-Series[/COLOR]' , 'Mini%20Dizi' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Musical[/COLOR]' , 'M%C3%BCzikal' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Mystery[/COLOR]' , 'Gizem' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Romance[/COLOR]' , 'Romantik' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Science Fiction[/COLOR]' , 'Bilim%20Kurgu' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Sport[/COLOR]' , 'Spor' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Thriller[/COLOR]' , 'Gerilim' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']War[/COLOR]' , 'Sava%C5%9F' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Western[/COLOR]' , 'Tarih' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Youth[/COLOR]' , 'Gen%C3%A7lik' , 10024 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 if 93 - 93: oo0oO00 * I11i / IIi - IIi . OooOO000 / oOo0O0Ooo
def I111ii1iI ( url ) :
 iii11 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( iii11 )
 IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 33 - 33: iIi1i1ii1 % o0o00Oo0O + Ii1I
  if 96 - 96: IIiIi1iI . ii
  if 39 - 39: IIi + oO0o
  if 80 - 80: IIi % oO0o / OOooOOo
def OOOOO000oo0 ( ) :
 if 2 - 2: O00OOo00oo0o * oOo0O0Ooo . OOoOoo * OooOO000
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( i1I11iIiII ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( iiOOooooO0Oo )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if i1I11iIiII in iiI11ii1I1 . lower ( ) :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 30 - 30: OOoOoo
   if 98 - 98: OooOO000 / iI11I1II1I1I . iiII11i1I1IIi * Ii + I1ii11iIi11i * iiII11i1I1IIi
   if 67 - 67: OooOO000
def oooO0o ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for iII1iii , O0Oo0o000oO , I1iII11ii1 , iiI11ii1I1 in IIIII11I1IiI :
  Ii111I11 = ( I1iII11ii1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  Oo0O0oo = ( O0Oo0o000oO ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0O0 = 'Season ' + Oo0O0oo + 'Episode ' + Ii111I11 + iiI11ii1I1
  oO0o0ooO ( o0O0 , iII1iii )
  if 85 - 85: IIiIiII11i
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 55 - 55: Ii1I
  if 76 - 76: oo0oO00 - Ii
def oO0o0ooO ( name , url ) :
 iII1iii = url
 II1ii1iI = name
 iii1i1iiiiIi = cloudflare . source ( iII1iii )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for OOOOooO0oO00O0o , i111 in i1I :
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + II1ii1iI + i111 + '[/COLOR]' , OOOOooO0oO00O0o , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 71 - 71: oO0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 75 - 75: OooOO000
 if 16 - 16: Ii1I + IIiIiII11i * OOooOOo . OOoOoo
def iiI1iIii1i ( ) :
 if 10 - 10: OooOO000 * iIi1i1ii1 - IIiIi1iI . iiII11i1I1IIi - IIi
 if 94 - 94: oOo0O0Ooo % OOoOoo + oO0o
 if 90 - 90: ooOoO0O00 + o0o00Oo0O - oo0oO00 . OooOO000 + iI11I1II1I1I
 if 88 - 88: iIi1i1ii1 * o0o00Oo0O . O00OOo00oo0o / ii
 if 29 - 29: ii . IIiIiII11i % OOooOOo
 if 26 - 26: iI11I1II1I1I - Ii1I . OOoOoo . OOoOoo + iI11I1II1I1I * I1ii11iIi11i
 if 85 - 85: IIi + IIiIiII11i - IIi * oo0oO00 - ooOoO0O00 % OooOO000
 if 1 - 1: ii / o0o00Oo0O + OOooOOo + OOooOOo . O00OOo00oo0o - OOooOOo
 if 9 - 9: O00OOo00oo0o * ii % oOo0O0Ooo / OOooOOo * iiII11i1I1IIi
 if 48 - 48: ii . OOooOOo
 if 65 - 65: oo0oO00 . I1ii11iIi11i
 if 94 - 94: OOooOOo + OOoOoo . IIiIi1iI
 if 69 - 69: o0o00Oo0O - o0o00Oo0O
 I1IIII1i ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 41 - 41: OOoOoo % I11i
 if 67 - 67: o0o00Oo0O % O00OOo00oo0o
def IIII1I ( url ) :
 I1 = O000oo ( url )
 I1IIIiI1I1ii1 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 70 - 70: iIi1i1ii1 . o0o00Oo0O - IIi
def o000ooOo0o0OO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 1 - 1: iI11I1II1I1I % IIiIi1iI + o0o00Oo0O
def IIiII11 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'episode' in url :
   I1IIII1i ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  else :
   I1IIII1i ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 58 - 58: OooOO000
  if 2 - 2: OOoOoo - oo0oO00 % oO0o + I11i + iIi1i1ii1 - iI11I1II1I1I
def iIIIOoO0000 ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 III11iIIi = 'http://www.watchseriesgo.to/search/' + i1I11iIiII . replace ( ' ' , '%20' )
 I1 = O000oo ( III11iIIi )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'watch online' in iiI11ii1I1 :
   pass
  else :
   print iiOOooooO0Oo
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + iiOOooooO0Oo , 10044 , oOo0OOoO0 , '' , '' )
   if 29 - 29: OOooOOo / ii + OOooOOo
   xbmcplugin . setContent ( I1IIiiIiii , 'movies' )
   if 13 - 13: oO0o * iiII11i1I1IIi % Ii % ooOoO0O00 + OOoOoo / IIiIiII11i
def Oo0Ooo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , I1iII11ii1 , I111iIi1 in IIIII11I1IiI :
  I1IIIiii1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( I1iII11ii1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + II + ']' + I1IIIiii1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOo0OOoO0 , '' , I111iIi1 )
  if 38 - 38: Ii1I % IIiIi1iI + ooOoO0O00 * ii * oo0oO00
def OoO0o0OO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIIiii1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + II + ']' + I1IIIiii1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 10 - 10: oo0oO00 - OooOO000 % IIiIiII11i - O00OOo00oo0o - ooOoO0O00
def iIi11iI1i ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOo0OOoO0 , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 46 - 46: ooOoO0O00 + IIiIiII11i * ooOoO0O00 - iIi1i1ii1
def Oo0OOOoOO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 I1IIIiI1I1ii1 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for O0Oo0o000oO , IiI1i11IiIiii in I1IIIiI1I1ii1 :
  IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( IiI1i11IiIiii ) )
  for url , iiI11ii1I1 in IIIII11I1IiI :
   I1IIIiii1 = ( O0Oo0o000oO ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IIII1i ( '[COLOR' + II + ']' + I1IIIiii1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 11 - 11: o0o00Oo0O * OOooOOo
class IIii1i ( ) :
 if 69 - 69: O00OOo00oo0o / ii % Ii
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 18 - 18: Ii - IIiIi1iI * oo0oO00 + I11i
  I1IIIiii1 = name
  self . Get_Sources ( iiOOooooO0Oo , I1IIIiii1 )
  if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
  if 33 - 33: O00OOo00oo0o % IIiIiII11i
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O000oo ( URL )
  IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
  for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + iiOOooooO0Oo
   self . Get_site_link ( URL , season_name )
   if 49 - 49: Ii1I + iiII11i1I1IIi / I11i + ii + IIi / OOoOoo
 def Get_site_link ( self , url , season_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="([^"]*)"' ) . findall ( I1 )
  i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( I1 )
  I1II1 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( I1 )
  for url in IIIII11I1IiI :
   self . main ( url , season_name )
  for url in i1I :
   self . main ( url , season_name )
  for url in I1II1 :
   self . main ( url , season_name )
   if 29 - 29: iIi1i1ii1 - iIi1i1ii1 / IIiIi1iI
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   I11IIII = 'DACLIPS'
   if I11IIII in IIii1i . source_list :
    pass
   else :
    self . daclips ( url , season_name , I11IIII )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    I11IIII = 'FILEHOOT'
    if I11IIII in IIii1i . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , I11IIII )
   else :
    if 'thevideo.me' in url :
     I11IIII = 'THEVIDEO'
     if I11IIII in IIii1i . source_list :
      pass
     else :
      self . thevideo ( url , season_name , I11IIII )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      I11IIII = 'ALLMYVIDEOS'
      if I11IIII in IIii1i . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , I11IIII )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       I11IIII = 'VIDSPOT'
       if I11IIII in IIii1i . source_list :
        pass
       else :
        self . vidspot ( url , season_name , I11IIII )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        I11IIII = 'VODLOCKER'
        if I11IIII in IIii1i . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , I11IIII )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 38 - 38: ii . I11i . IIiIiII11i - OooOO000
         if 65 - 65: Ii + oOo0O0Ooo / I1ii11iIi11i % IIi . iIi1i1ii1 + iI11I1II1I1I
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for oOO , iiI11ii1I1 in IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 32 - 32: oOo0O0Ooo
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for oOO , iiI11ii1I1 in IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 47 - 47: Ii1I * oo0oO00 + iI11I1II1I1I - oo0oO00 / OOoOoo
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( "{ label: '.+?', file: '(.+?)' }" ) . findall ( I1 )
  for oOO in IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 86 - 86: OOoOoo
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for oOO in IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 43 - 43: oOo0O0Ooo / OooOO000 / IIiIi1iI + iI11I1II1I1I + ii
 def daclips ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for oOO in IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 33 - 33: IIiIiII11i - OOoOoo - IIiIi1iI
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( I1 )
  for oOO in IIIII11I1IiI :
   self . Printer ( oOO , season_name , source_name )
   if 92 - 92: oO0o * OOoOoo
 def Printer ( self , Link , season_name , source_name ) :
  if 92 - 92: oo0oO00
  if Link in IIii1i . List :
   pass
  elif source_name in IIii1i . source_list :
   pass
  else :
   ooOO0oO0oo00o ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   IIii1i . List . append ( Link )
   IIii1i . source_list . append ( source_name )
   if 7 - 7: OooOO000
   xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 73 - 73: oO0o % Ii1I
   if 32 - 32: IIi + OooOO000 + iI11I1II1I1I * I1ii11iIi11i
   if 62 - 62: Ii
   if 2 - 2: oOo0O0Ooo
   if 69 - 69: ii / I1ii11iIi11i * O00OOo00oo0o
def OO0Oo000OOOoO ( ) :
 I1IIII1i ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , O0o0Oo , '' )
 if 99 - 99: IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oo0oO00 / IIiIiII11i % ii
def i11OOoOOO ( url ) :
 I1IIII1i ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oooooO0O0o , url , IiIiiI , OoOoO0oO00O , ooo0OIi1iiIIi1i , O0O00OooO , iIiiiI1I , OOoO , III1I11i1iIi , iIII1I1ii , iiIIi11ii1Ii in IIIII11I1IiI :
  IiIiiI = IiIiiI
  if 'Arsenal' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'arsenal-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                                  ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Bournemouth' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'afc-bournemouth.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                       ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Burnley' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'KEGnQWW.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                                   ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Chelsea' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'chelsea.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                                  ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Crystal' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'CrystalPalace.0.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                       ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Everton' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'Everton.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                                   ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Hull' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'hull-city-afc.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                                 ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Leicester' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                       ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Liverpool' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'liverpool-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                               ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Manchester City' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'city-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '               ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Manchester United' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + '91.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '          ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Middlesbrough' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                 ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Southampton' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'southampton-fc-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                   ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Stoke City' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'stoke-city.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                          ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Sunderland' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'sunderland-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                        ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Swansea' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'swansea-city-afc.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                    ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Tottenham' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '        ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Watford' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '                              ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'Bromwich' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '   ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  elif 'West Ham' in IiIiiI :
   O0OOO0OOooo00 = oOOOo00O00oOo + 'west-ham.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + oooooO0O0o + ' - ' + IiIiiI + '             ' + OoOoO0oO00O + '        ' + ooo0OIi1iiIIi1i + '        ' + O0O00OooO + '        ' + iIiiiI1I + '        ' + OOoO + '        ' + III1I11i1iIi + '        ' + iIII1I1ii + '[/COLOR]'
  I1IIII1i ( str ( iiI11ii1I1 ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , O0OOO0OOooo00 , O0OOO0OOooo00 , IiIiiI )
  if 60 - 60: I11i . OOooOOo % O00OOo00oo0o / oOo0O0Ooo / o0o00Oo0O
def IiI ( description ) :
 IiIiiI = description
 iiOOooooO0Oo = ( 'http://www.fullmatchesandshows.com/?s=' + IiIiiI ) . replace ( ' ' , '%20' )
 ii11I ( iiOOooooO0Oo )
 if 97 - 97: ooOoO0O00 + OooOO000 . IIiIi1iI - OooOO000
def ooo ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iiOOooooO0Oo , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOo0OOoO0 , O0o0Oo , '' )
  if 74 - 74: IIiIi1iI % OOooOOo / I1ii11iIi11i
def i1111Ii11i ( url ) :
 I1 = O000oo ( url )
 I1IIIiI1I1ii1 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for I1IIIiI1I1ii1 in I1IIIiI1I1ii1 :
  OoOo00O0o = re . compile ( '(.*?)</h2>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for O000O0Oo00OO0 in OoOo00O0o :
   O000O0Oo00OO0 = O000O0Oo00OO0
  iIIII11i = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I1IIIiI1I1ii1 ) )
  for oOo0OOoo0o , oOo0OOoO0 , time , iiiIIiiIi in iIIII11i :
   Ii1IIiiIiiIi = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( iiiIIiiIi )
   I1IIII1i ( '[COLOR' + II + ']' + O000O0Oo00OO0 + ' - ' + oOo0OOoo0o + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOo0OOoO0 , O0o0Oo , ( str ( Ii1IIiiIiiIi ) ) )
   if 86 - 86: ii % IIiIiII11i . ii * Ii1I
 i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if 9 - 9: I1ii11iIi11i + OooOO000
def oooooO0oO0ooO ( ) :
 I1IIII1i ( '[COLOR' + II + ']Latest[/COLOR]' , 'http://www.fullmatchesandshows.com' , 10011 , 'http://www.fancyicons.com/free-icons/125/miscellaneous/png/256/football_256.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']EURO 2016[/COLOR]' , 'http://www.fullmatchesandshows.com/euro-2016/' , 10011 , 'http://football.mywapblog.com/files/uefa-euro-2016-logo.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']Shows[/COLOR]' , 'http://www.fullmatchesandshows.com/category/show/' , 10011 , 'http://www.fm-base.co.uk/forum/attachments/club-competition-logos/3885-soccer-am-logo-socceram.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']Premier League[/COLOR]' , 'http://www.fullmatchesandshows.com/premier-league/' , 10011 , 'https://footballseasons.files.wordpress.com/2013/05/premier-league.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']La Liga[/COLOR]' , 'http://www.fullmatchesandshows.com/la-liga/' , 10011 , 'http://1.bp.blogspot.com/-c6kQ40ryhyo/U19cUlz25sI/AAAAAAAABak/qtn5chSFZm0/s1600/la-liga-logo_display_image.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']Bundesliga[/COLOR]' , 'http://www.fullmatchesandshows.com/bundesliga/' , 10011 , 'http://m.img.brothersoft.com/iphone/189/518670189_icon175x175.jpg' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']Champions League[/COLOR]' , 'http://www.fullmatchesandshows.com/champions-league/' , 10011 , 'http://www.ecursuri.ro/images/teste/test-champions-league.jpg' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']Serie A[/COLOR]' , 'http://www.fullmatchesandshows.com/category/serie-a/' , 10011 , 'http://files.jcriccione.it/200000223-2484526782/serie%20a.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']Ligue 1[/COLOR]' , 'http://www.fullmatchesandshows.com/category/ligue-1/' , 10011 , 'http://a1.mzstatic.com/us/r30/Purple5/v4/37/c7/44/37c744ae-5824-42b7-6ce0-5f471f52baab/icon180x180.jpeg' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']Copa America 2015[/COLOR]' , 'http://www.fullmatchesandshows.com/copa-america-2015/' , 10011 , 'https://pbs.twimg.com/profile_images/521966985907691520/Nq9OAPIo_400x400.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']CONCACAF[/COLOR]' , 'http://www.fullmatchesandshows.com/category/concacaf/' , 10011 , 'http://a3.mzstatic.com/us/r30/Purple3/v4/40/26/14/4026147c-7022-4ca3-504e-e78950cc3f1c/icon175x175.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 I1IIII1i ( '[COLOR' + II + ']Women World Cup[/COLOR]' , 'http://www.fullmatchesandshows.com/category/women-world-cup/' , 10011 , 'https://upload.wikimedia.org/wikipedia/en/thumb/7/76/2015_FIFA_Women\'s_World_Cup_logo.svg/967px-2015_FIFA_Women\'s_World_Cup_logo.svg.png' , oOOOo00O00oOo + 'fanart.jpg' , '' )
 if 31 - 31: Ii1I
def O0OoOo ( url ) :
 I1IIII1i ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  OOOOoO0 = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   OOOOoO0 = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   ooOO0oO0oo00o ( '[COLOR' + II + ']' + OOOOoO0 + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  OOOOoO0 = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   ooOO0oO0oo00o ( '[COLOR' + II + ']' + OOOOoO0 + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
def ii11I ( url ) :
 I1IIII1i ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 43 - 43: oOo0O0Ooo - I11i / I11i . IIiIiII11i - iIi1i1ii1
 if 40 - 40: OooOO000 . OOooOOo * o0o00Oo0O
 if 6 - 6: oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + iiII11i1I1IIi . IIi
 if 74 - 74: ooOoO0O00
 if 15 - 15: ooOoO0O00 + OOoOoo % oOo0O0Ooo / Ii * OOooOOo
 if 69 - 69: Ii
 if 61 - 61: o0o00Oo0O
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  OOOOoO0 = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   ooOO0oO0oo00o ( '[COLOR' + II + ']' + OOOOoO0 + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
   if 21 - 21: oO0o % iI11I1II1I1I . oO0o
def OO000OOOo0Oo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for OOOOooO0oO00O0o in IIIII11I1IiI :
  Oo00O0O = ( OOOOooO0oO00O0o ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  iii1 ( 'http:' + Oo00O0O )
  if 70 - 70: oO0o
  if 43 - 43: OOooOOo
  if 57 - 57: oOo0O0Ooo
  if 65 - 65: Ii - IIiIi1iI * iiII11i1I1IIi + IIiIi1iI / OOoOoo + I11i
def IiII1I ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  ooOO0oO0oo00o ( iiI11ii1I1 , url , 8046 , oOo0OOoO0 )
 for url in i1I :
  i11i1iiiII ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def O0oO0 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iii1 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 65 - 65: IIi + O00OOo00oo0o - iIi1i1ii1
def o0OOO ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 5 - 5: o0o00Oo0O . O00OOo00oo0o . iIi1i1ii1 + OooOO000 * ooOoO0O00 % OOoOoo
def ooooO0oOoOOoO ( ) :
 i11i1iiiII ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 i11i1iiiII ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 i11i1iiiII ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , iiOOooooO0Oo , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIiIi1i1I11 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + oOo0OOoO0 )
 for url in next :
  i11i1iiiII ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 33 - 33: IIiIi1iI + ii - oO0o / ooOoO0O00 / ii
  if 82 - 82: Ii1I / IIi - OooOO000 / I1ii11iIi11i * oO0o
def o00O ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   ooOO0oO0oo00o ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   i11i1iiiII ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def IIIIIiiI ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10012 , '' )
  if 38 - 38: o0o00Oo0O
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO ( name , url ) :
 i1i1i11iI11II = 0
 name = name
 url = url
 OooOoOO0 = [ '144' , '240' , '380' , '480' , '720' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  iii1 ( url )
  if 6 - 6: OOooOOo . IIiIiII11i * oOo0O0Ooo . oOo0O0Ooo / iIi1i1ii1
  if 14 - 14: O00OOo00oo0o % OOoOoo - o0o00Oo0O / O00OOo00oo0o
  if 91 - 91: Ii % O00OOo00oo0o * oo0oO00 - Ii1I . O00OOo00oo0o
  if 28 - 28: Ii
  if 51 - 51: oOo0O0Ooo + IIiIi1iI * o0o00Oo0O . iIi1i1ii1
  if 82 - 82: IIi * Ii1I % iIi1i1ii1 . IIi
  if 43 - 43: oO0o . IIiIi1iI * I1ii11iIi11i
  if 20 - 20: ooOoO0O00 . ooOoO0O00 - iiII11i1I1IIi
def O0o00ooo ( ) :
 OoO000O0Oo = I1iii11 ( 'http://documentarylovers.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  if 'genre' in iiOOooooO0Oo :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , iiOOooooO0Oo , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiiIIiiiI ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , oOo0OOoO0 )
 for url in next :
  i11i1iiiII ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 50 - 50: O00OOo00oo0o + iiII11i1I1IIi / iIi1i1ii1 * IIi / I11i
def Ii11Iiii ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  ooOO0oO0oo00o ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in i1I :
  IIIIIiiI ( url )
  if 98 - 98: ooOoO0O00 % I1ii11iIi11i
def o0OOoOooO0ooO ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1Iii = 'http://documentarylovers.com/?s=' + ( i1I11iIiII ) . replace ( ' ' , '+' )
 OO0OO0OO = i1Iii . lower ( )
 iiiIIiiiI ( OO0OO0OO )
 if 50 - 50: Ii + ii / o0o00Oo0O + I11i / Ii + oo0oO00
def O0O0O0OO00oo ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'films' in url :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def I11IIIIiI1 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  if 'films' in url :
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + oOo0OOoO0 )
 for url in i1I :
  i11i1iiiII ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def o0oOOO ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'rtd' in url :
   o00OoOooo ( url )
   if 47 - 47: IIiIi1iI + OooOO000 + ooOoO0O00
def o00OoOooo ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OoO000O0Oo )
 for i1Oo00 , file in IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1Oo00 + file )
  iii1 ( url )
  if 6 - 6: oo0oO00 / o0o00Oo0O / iIi1i1ii1 / OOoOoo / oo0oO00 . iI11I1II1I1I
  if 62 - 62: iI11I1II1I1I
def IIi1i1ii11I1 ( ) :
 I1 = I1iii11 ( 'http://www.stream2watch.co/live-tv' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , oOoO0OO in IIIII11I1IiI :
  i11i1iiiII ( ( iiI11ii1I1 + '[COLOR' + II + ']' + oOoO0OO + '[/COLOR]' ) , iiOOooooO0Oo , 8086 , oOo0OOoO0 )
  if 88 - 88: oOo0O0Ooo
def oOO0Oo ( url ) :
 I1 = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8087 , oOo0OOoO0 )
  if 5 - 5: Ii * OooOO000 - iIi1i1ii1 - Ii1I - ooOoO0O00 + OooOO000
def I1ii1iOO00OoOO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  iiii1II1ii11 ( url , iiI11ii1I1 )
  if 37 - 37: O00OOo00oo0o - oo0oO00 - oO0o
def iiii1II1ii11 ( url , name ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  print url
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 42 - 42: iI11I1II1I1I % iIi1i1ii1 - Ii1I + iI11I1II1I1I
def iiI1I ( ) :
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iiOOooooO0Oo , 3002 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def O0oooO00ooO0 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def o00OOO0o00OO ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 oOOOO0oOoo = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , iiI11ii1I1 in oOOOO0oOoo :
  i11i1iiiII ( '[COLOR' + II + ']Season- ' + iiI11ii1I1 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  i11i1iiiII ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def Oo0OOOOOOO0oo ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  II1Iiiii111i ( url )
def II1Iiiii111i ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( url )
  if 52 - 52: o0o00Oo0O - iI11I1II1I1I / oO0o / OOoOoo
def Ii1II1I11i1 ( ) :
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiOOooooO0Oo , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def I11Iii11i11I1 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  O0ooOO ( url )
  if 1 - 1: ooOoO0O00 . Ii1I * I11i % IIiIiII11i % iI11I1II1I1I
def ooOO0OoO ( ) :
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiOOooooO0Oo , 8065 , oOOOo00O00oOo + 'classictv.png' )
def OOo000o ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'mp4' in url :
   iii1 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 36 - 36: iIi1i1ii1
def ooOO00o0 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iiOOooooO0Oo , 8071 , oOOOo00O00oOo + 'streams.png' )
def Ii1I1iIiiI1 ( url ) :
 I1 = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '(Free Access)' in iiI11ii1I1 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def o00i111iiIiiIiI ( url ) :
 I1 = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOo0OOoO0 , iiii111II , '' )
  if 59 - 59: IIi + oOo0O0Ooo / IIiIiII11i / OOooOOo
def oOoo00 ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  IIiIi ( 'http://watchxxxfree.com/categories' )
 if iI1i11iII111 == 1 :
  I1I1IIiiI1 ( 'http://www.perfectgirls.net' )
 if iI1i11iII111 == 2 :
  oooOOO0o0O0 ( 'http://www.xvideos.com/best' )
 if iI1i11iII111 == 3 :
  iiiI1IiI ( 'http://www.xvideos.com/best' )
 if iI1i11iII111 == 4 :
  oooOOO0o0O0 ( 'http://www.xvideos.com/best' )
 if iI1i11iII111 == 5 :
  oooOOO0o0O0 ( 'http://www.xvideos.com/verified/videos' )
 if iI1i11iII111 == 6 :
  Ii111IIIIii ( 'http://www.xvideos.com/tags' )
 if iI1i11iII111 == 7 :
  O00o ( 'http://www.xvideos.com/porn' )
 if iI1i11iII111 == 8 :
  Iii1iIIiii1ii ( )
  if 13 - 13: iI11I1II1I1I - IIiIiII11i % o0o00Oo0O . iIi1i1ii1 % oO0o
  if 2 - 2: ii - iIi1i1ii1 % oo0oO00 / oOo0O0Ooo / I11i
  if 3 - 3: IIiIiII11i / IIi
  if 48 - 48: IIiIi1iI . Ii1I
  if 49 - 49: ooOoO0O00 - OOooOOo . I1ii11iIi11i + iI11I1II1I1I - IIiIi1iI / I1ii11iIi11i
  if 24 - 24: oo0oO00 - OooOO000 / IIiIi1iI
  if 10 - 10: OOooOOo * ooOoO0O00
  if 15 - 15: iiII11i1I1IIi + ooOoO0O00 - IIiIiII11i % oOo0O0Ooo
  if 34 - 34: oOo0O0Ooo
def o0OoOo0O00 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'ch' in url :
   o0oo0o00ooO00 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def iI1i1iI1iI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 I1IIiIi = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for iiI11ii1I1 , url in I1IIiIi :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def OOOOoOoO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   OO000 ( url )
def o0oOoo0o ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( url )
def IIiIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , IiIIi1I1I11Ii in IIIII11I1IiI :
  if 'category' in url :
   o0oo0o00ooO00 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]   ' + IiIIi1I1I11Ii + '[/COLOR]' , url , 90006 , oOo0OOoO0 , oOOOo00O00oOo + 'Jizbox.png' , '' )
def IiiIiIIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 I1IIiIi = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , oOo0OOoO0 , '' , '' )
 for url in I1IIiIi :
  I1IIII1i ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def O00Oo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   OO000 ( url )
def OO000 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( url )
def I1I1IIiiI1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , IiIIi1I1I11Ii in IIIII11I1IiI :
  if 'category' in url :
   o0oo0o00ooO00 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]' + IiIIi1I1I11Ii + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def oOOoo ( url ) :
 I1 = O000oo ( url )
 iII1iii = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 I1IIiIi = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , oOo0OOoO0 , '' , '' )
 for url in I1IIiIi :
  I1IIII1i ( '[COLORred]NEXT[/COLOR]' , iII1iii + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def oo0O0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  Ii111Ii11 ( 'http://www.perfectgirls.net' + url )
def Ii111Ii11 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( 'http://' + url )
def O00o ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , iiI11ii1I1 , IiIIi1I1I11Ii in IIIII11I1IiI :
  o0oo0o00ooO00 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - No of Videos : [COLORorange]' + IiIIi1I1I11Ii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def Ii111IIIIii ( url ) :
 I1 = O000oo ( url )
 I1IIiIi = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in I1IIiIi :
  o0oo0o00ooO00 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , iiI11ii1I1 , IiIIi1I1I11Ii in IIIII11I1IiI :
  o0oo0o00ooO00 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - No of Videos : [COLORorange]' + ( IiIIi1I1I11Ii + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 10 - 10: ii . oOo0O0Ooo * o0o00Oo0O * oO0o - IIi
def IIIiII11 ( url ) :
 I1 = O000oo ( url )
 I1IIiIi = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in I1IIiIi :
  o0oo0o00ooO00 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , I11II1i11 in IIIII11I1IiI :
  o0oo0o00ooO00 ( iiI11ii1I1 + '--' + ( I11II1i11 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOo0OOoO0 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 96 - 96: iiII11i1I1IIi * Ii1I * iIi1i1ii1 + Ii1I % oOo0O0Ooo + Ii
  if 37 - 37: iiII11i1I1IIi % Ii1I / IIiIi1iI
def oooOOO0o0O0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , iI , o0oO in IIIII11I1IiI :
  o0oo0o00ooO00 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - Porn Quality : [COLORorange]' + o0oO + ' - [COLORred]' + iI + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oOo0OOoO0 , oOo0OOoO0 , o0oO + ' - ' + iI )
 ooOo0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in ooOo0 :
  o0oo0o00ooO00 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 61 - 61: IIiIiII11i
def iiiI1IiI ( url ) :
 I1 = O000oo ( url )
 I1IIIiI1I1ii1 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 I1IIiIi = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in I1IIiIi :
  o0oo0o00ooO00 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I1IIIiI1I1ii1 ) )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '/c/' in url :
   o0oo0o00ooO00 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 48 - 48: IIi
   if 26 - 26: OooOO000 * O00OOo00oo0o * oo0oO00 * OOooOOo
def Iii1iIIiii1ii ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1ii1i11iI1 = ( i1I11iIiII ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 OO0OO0OO = I1ii1i11iI1 . lower ( )
 oO0O = 'http://www.xvideos.com/?k=' + OO0OO0OO
 print oO0O + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O000oo ( oO0O )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 , iI , o0oO in IIIII11I1IiI :
  o0oo0o00ooO00 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - Porn Quality : [COLORorange]' + o0oO + ' - [COLORred]' + iI + '[/COLOR]' , 'http://www.xvideos.com' + iiOOooooO0Oo , 10108 , oOo0OOoO0 , oOo0OOoO0 , o0oO + ' - ' + iI )
 ooOo0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for iiOOooooO0Oo in ooOo0 :
  o0oo0o00ooO00 ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iiOOooooO0Oo , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 6 - 6: o0o00Oo0O . IIiIi1iI - oo0oO00 / Ii
def O00O0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( I1 )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( I1 )
 I1II1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'http' in url :
   ooOO0oO0oo00o ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   ooOO0oO0oo00o ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in I1II1 :
  if 'http' in url :
   ooOO0oO0oo00o ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
   if 52 - 52: OooOO000 + o0o00Oo0O % I11i % o0o00Oo0O % IIiIiII11i + ii
def o0ooOOO0OO ( url ) :
 IiI1iII1II111 = xbmc . Player ( IIiI11i1111Ii ( ) )
 import urlresolver
 try : IiI1iII1II111 . play ( url )
 except : pass
 if 12 - 12: iiII11i1I1IIi
 if 19 - 19: iIi1i1ii1 * ooOoO0O00 % o0o00Oo0O + iiII11i1I1IIi
def I1i1ii1ii ( ) :
 if 32 - 32: OOoOoo / ii
 if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - OooOO000 - Ii
 if 84 - 84: ooOoO0O00 - oOo0O0Ooo % OooOO000
 if 80 - 80: I11i % OooOO000
 if 80 - 80: iIi1i1ii1
 if 26 - 26: iI11I1II1I1I . ii - iI11I1II1I1I
 if 59 - 59: Ii1I + iiII11i1I1IIi . oo0oO00
 if 87 - 87: oO0o
 if 34 - 34: O00OOo00oo0o . OOooOOo / Ii / OooOO000
 if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + IIi
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 8091 , oOOOo00O00oOo + 'gofish.png' )
def I11II11IiI11 ( url ) :
 I1 = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8092 , oOo0OOoO0 )
 for url in next :
  i11i1iiiII ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def O00oIi11Iiii1iiii ( url ) :
 I1 = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 i1IIII1111 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 in i1IIII1111 :
  oOo0OOoO0 = oOo0OOoO0
 for url , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8092 , oOo0OOoO0 )
 for url in next :
  i11i1iiiII ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 84 - 84: o0o00Oo0O % iIi1i1ii1 . iIi1i1ii1 . OooOO000 * iiII11i1I1IIi
def iIOO0O ( url ) :
 I1 = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 34 - 34: iIi1i1ii1 - oo0oO00 * ii . oO0o / oOo0O0Ooo
  if 66 - 66: I1ii11iIi11i / Ii % IIiIi1iI
  if 43 - 43: IIi
  if 84 - 84: IIi . OOoOoo . OooOO000
iIII1I1i = '{PQ},' ; I1IIIIII1 = '{SC},' ; O0oO0O = '{XG},' ; IIiiiII11i = '{JP},' ; iIiIiiIIIi1 = '{HW},' ; i1Ii1i111IIiIi1I = '{RT},'
def iii11I ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oo00Oo0oO00Oo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 iiOOooooO0Oo = ( i11 ( 'http://m3.doctor-movies.com/english/' ) )
 if 20 - 20: I11i / OOoOoo
 IiiI = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 II1I11 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 I11iIiIii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 Ooooo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 IIIiI1iIIII = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + i1I11iIiII
 o0oo00OOOo = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 oo0oO = ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvbW92aWVzZWFyY2gucGhw' ) )
 i1i1IIi = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 o0oo0Ooo0 = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 74 - 74: iIi1i1ii1 + Ii1I + oOo0O0Ooo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 37 - 37: OOoOoo
 if 97 - 97: I11i / OOoOoo + OOooOOo + oO0o % O00OOo00oo0o
 Iiii = OOoOO0oo0ooO ( IiiI )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OO0OoO0o00 = OOoOO0oo0ooO ( II1I11 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 iIIi1II1 = OOoOO0oo0ooO ( I11iIiIii )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IiI1I11ii = OOoOO0oo0ooO ( IIIiI1iIIII )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oO0O00oO0o0 = OOoOO0oo0ooO ( o0oo00OOOo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 o0oOo = OOoOO0oo0ooO ( oo0oO )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 O0OoOo0oO0o = OOoOO0oo0ooO ( i1i1IIi )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 I11iIi1i1IIi = OOoOO0oo0ooO ( o0oo0Ooo0 )
 if 49 - 49: I1ii11iIi11i / iIi1i1ii1 % iiII11i1I1IIi + oo0oO00 - oO0o
 if 13 - 13: IIiIiII11i
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
  for OoO , iiI11ii1I1 in IIIII11I1IiI :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiOOooooO0Oo + OoO ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 34 - 34: ooOoO0O00 % oo0oO00 . OOoOoo . ooOoO0O00 + IIiIiII11i / oO0o
    if 79 - 79: Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
    if 95 - 95: oo0oO00
    if 48 - 48: iiII11i1I1IIi / iI11I1II1I1I % IIiIiII11i
    if 39 - 39: ooOoO0O00 . Ii1I / iiII11i1I1IIi / iiII11i1I1IIi
    if 100 - 100: ii - ii + OOoOoo
    if 32 - 32: OOooOOo * I11i / ii
 if Iiii != 'Failed' :
  I1II1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for OoO , iiI11ii1I1 in I1II1 :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( IiiI + OoO ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OO0OoO0o00 != 'Failed' :
  oo00OO0000oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoO0o00 )
  for iiOOooooO0Oo , ooI1i , I111iIi1 , OOOoO000 , iiI11ii1I1 in oo00OO0000oO :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Silent Hunter[/COLOR]' ) , iiOOooooO0Oo , 222 , ooI1i , OOOoO000 , I111iIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 90 - 90: O00OOo00oo0o
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if iIIi1II1 != 'Failed' :
  ii11 = [ ]
  oo0oooOo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIi1II1 )
  for iiOOooooO0Oo , ooI1i , I111iIi1 , OOOoO000 , iiI11ii1I1 in oo0oooOo :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    if iiI11ii1I1 in ii11 :
     pass
    else :
     I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , iiOOooooO0Oo , 1016 , ooI1i , OOOoO000 , I111iIi1 )
     ii11 . append ( iiI11ii1I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if IiI1I11ii != 'Failed' :
  o00000O = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IiI1I11ii )
  for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in o00000O :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iiOOooooO0Oo , 7067 , oOo0OOoO0 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 23 - 23: I1ii11iIi11i - o0o00Oo0O
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 33 - 33: Ii1I
    if 54 - 54: IIiIi1iI * Ii1I . IIiIiII11i / IIi % IIi
    if 25 - 25: Ii + Ii1I - ii . o0o00Oo0O % O00OOo00oo0o
    if 53 - 53: ooOoO0O00
    if 59 - 59: I11i + oOo0O0Ooo % ii - iI11I1II1I1I
    if 9 - 9: ooOoO0O00 - OOooOOo
    if 57 - 57: iI11I1II1I1I * iIi1i1ii1 * OooOO000 / oo0oO00
    if 46 - 46: iIi1i1ii1
    if 61 - 61: I11i / IIiIi1iI - IIiIiII11i
 if o0oOo != 'Failed' :
  oOoO0 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( o0oOo )
  for iiI11ii1I1 , iiOOooooO0Oo , ooI1i , OOOoO000 , I111iIi1 in oOoO0 :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Reaper[/COLOR]' ) , iiOOooooO0Oo , 222 , ooI1i , OOOoO000 , I111iIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 95 - 95: IIiIi1iI / ii + o0o00Oo0O
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if O0OoOo0oO0o != 'Failed' :
  iIIIi11iIiIii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0OoOo0oO0o )
  for iiOOooooO0Oo , ooI1i , I111iIi1 , OOOoO000 , iiI11ii1I1 in iIIIi11iIiIii :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source APPRENTICE[/COLOR]' ) , iiOOooooO0Oo , 222 , ooI1i , OOOoO000 , I111iIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 61 - 61: ii . iIi1i1ii1 % oo0oO00 * ii
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 96 - 96: iIi1i1ii1 - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 if I11iIi1i1IIi != 'Failed' :
  oOO0O0O = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I11iIi1i1IIi )
  for iiOOooooO0Oo , ooI1i , iiI11ii1I1 in oOO0O0O :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Silent Hunter[/COLOR]' ) , iiOOooooO0Oo , 222 , ooI1i )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 81 - 81: Ii % ooOoO0O00 % IIiIiII11i % oOo0O0Ooo + oOo0O0Ooo % Ii1I
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 iiiI11 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 20 - 20: OOoOoo - iI11I1II1I1I
 for OoooO0o in iiiI11 :
  IIIii1iiIi = OOOO0OOoO0O0 + OoooO0o + IIiiiiiiIi1I1
  i1I1iI1 = OOoOO0oo0ooO ( IIIii1iiIi )
  if i1I1iI1 != 'Failed' :
   oOOoO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1I1iI1 )
   for iiOOooooO0Oo , ooI1i , I111iIi1 , OOOoO000 , iiI11ii1I1 in oOOoO :
    if i1I11iIiII in iiI11ii1I1 . lower ( ) :
     I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - Source Pandoras[/COLOR]' , iiOOooooO0Oo , 222 , ooI1i , OOOoO000 , I111iIi1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 28 - 28: iI11I1II1I1I * iiII11i1I1IIi . oOo0O0Ooo
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
     if 78 - 78: ii . ii / o0o00Oo0O
 iiiI11 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 25 - 25: IIiIiII11i % IIiIiII11i - iIi1i1ii1 . o0o00Oo0O
 if 79 - 79: OOoOoo / oO0o * ii * OOooOOo + oOo0O0Ooo
 for OoooO0o in iiiI11 :
  IIIii1iiIi = oo00Oo0oO00Oo + OoooO0o
  O0ooO = OOoOO0oo0ooO ( IIIii1iiIi )
  if O0ooO != 'Failed' :
   iIOO = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( O0ooO )
   for OoO , iiI11ii1I1 in iIOO :
    if i1I11iIiII in iiI11ii1I1 . lower ( ) :
     ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( oo00Oo0oO00Oo + OoooO0o + OoO ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 4 - 4: iIi1i1ii1 % Ii1I + iiII11i1I1IIi - Ii1I
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
     if 98 - 98: iIi1i1ii1 - o0o00Oo0O * oo0oO00 * iIi1i1ii1 * iIi1i1ii1
     if 44 - 44: OOoOoo + iiII11i1I1IIi
def ii1iIi1iIiI1i ( ) :
 if 66 - 66: oo0oO00
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 if 34 - 34: OooOO000 % Ii + Ii - OooOO000
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllc2dvLnRvL3NlYXJjaC8=' ) ) + ( i1I11iIiII ) . replace ( ' ' , '%20' )
 iII1iii = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 IiiI = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 II1I11 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 I11iIiIii = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( OO0OO0OO ) . replace ( ' ' , '+' )
 Ooooo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 IIIiI1iIIII = ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvc2VyaWFsc2VhcmNoLnBocA==' ) )
 o0oo00OOOo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 2 - 2: IIiIiII11i + ooOoO0O00
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 68 - 68: IIi + iIi1i1ii1
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = OOoOO0oo0ooO ( iII1iii )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = OOoOO0oo0ooO ( IiiI )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = OOoOO0oo0ooO ( II1I11 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iIIi1II1 = cloudflare . source ( I11iIiIii )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 O0ooO = OOoOO0oo0ooO ( Ooooo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 IiI1I11ii = OOoOO0oo0ooO ( IIIiI1iIIII )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 oO0O00oO0o0 = OOoOO0oo0ooO ( o0oo00OOOo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 58 - 58: OOoOoo * iIi1i1ii1 . ooOoO0O00
 if oO0O00oO0o0 != 'Failed' :
  i11I1iiii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0O00oO0o0 )
  for iiOOooooO0Oo , ooI1i , I111iIi1 , OOOoO000 , iiI11ii1I1 in i11I1iiii :
   if OO0OO0OO in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source HeroVision[/COLOR]' ) , iiOOooooO0Oo , 1016 , ooI1i , OOOoO000 , I111iIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 31 - 31: O00OOo00oo0o / I1ii11iIi11i / iI11I1II1I1I
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 90 - 90: I1ii11iIi11i * iiII11i1I1IIi + iiII11i1I1IIi
 if IiI1I11ii != 'Failed' :
  o00000O = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( IiI1I11ii )
  for iiI11ii1I1 , iiOOooooO0Oo , ooI1i , OOOoO000 , I111iIi1 in o00000O :
   if OO0OO0OO in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Reaper[/COLOR]' ) , iiOOooooO0Oo , 90037 , ooI1i , OOOoO000 , I111iIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 39 - 39: ooOoO0O00 + OooOO000 + o0o00Oo0O
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 18 - 18: iI11I1II1I1I % iI11I1II1I1I % oo0oO00 + oOo0O0Ooo % IIiIi1iI / iIi1i1ii1
    if 36 - 36: OOooOOo . Ii
    if 81 - 81: I1ii11iIi11i * OooOO000 * oO0o
    if 85 - 85: o0o00Oo0O * oo0oO00
    if 39 - 39: IIiIiII11i * oOo0O0Ooo - iI11I1II1I1I
    if 25 - 25: ii . iIi1i1ii1 % OooOO000 . OOoOoo
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 67 - 67: ii + O00OOo00oo0o / IIiIi1iI
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
   if OO0OO0OO in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - WatchSeries[/COLOR]' , 'http://www.watchseriesgo.to' + iiOOooooO0Oo , 10044 , oOo0OOoO0 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 75 - 75: OOoOoo / ii . oOo0O0Ooo + O00OOo00oo0o - IIiIiII11i
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
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
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iii1i1iiiiIi )
  for iiOOooooO0Oo , ooI1i , I111iIi1 , OOOoO000 , iiI11ii1I1 in i1I :
   if OO0OO0OO in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( iiI11ii1I1 + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , iiOOooooO0Oo , 1016 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Redemption Links" )
    if 80 - 80: oOo0O0Ooo
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  I1II1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for iiI11ii1I1 in I1II1 :
   if OO0OO0OO in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( iiI11ii1I1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiiI + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 58 - 58: oo0oO00 + Ii1I % OOooOOo
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  oo00OO0000oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for iiI11ii1I1 in oo00OO0000oO :
   if OO0OO0OO in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( iiI11ii1I1 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( II1I11 + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 22 - 22: iI11I1II1I1I - iIi1i1ii1 / oOo0O0Ooo * OOoOoo
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if iIIi1II1 != 'Failed' :
  oo0oooOo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iIIi1II1 )
  for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in oo0oooOo :
   if OO0OO0OO in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - Source - Dizi[/COLOR]' , iiOOooooO0Oo , 8062 , oOo0OOoO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 26 - 26: I11i + IIi - I11i + I1ii11iIi11i . oo0oO00
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if O0ooO != 'Failed' :
  iIOO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0ooO )
  for iiOOooooO0Oo , ooI1i , I111iIi1 , OOOoO000 , iiI11ii1I1 in iIOO :
   if OO0OO0OO in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- Source Scooby[/COLOR]' ) , iiOOooooO0Oo , 1016 , ooI1i , OOOoO000 , I111iIi1 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 97 - 97: ooOoO0O00
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 46 - 46: Ii1I
 II1i1 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for OoooO0o in II1i1 :
  IIIii1iiIi = OOOO0OOoO0O0 + OoooO0o + IIiiiiiiIi1I1
  O0OoOo0oO0o = OOoOO0oo0ooO ( IIIii1iiIi )
  if O0OoOo0oO0o != 'Failed' :
   iIIIi11iIiIii = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( O0OoOo0oO0o )
   for iiI11ii1I1 , I111iIi1 , iiOOooooO0Oo , oOo0OOoO0 , iiii111II , iiiii1II in iIIIi11iIiIii :
    if OO0OO0OO in iiI11ii1I1 . lower ( ) :
     I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - Source Pandoras[/COLOR]' , iiOOooooO0Oo , iiiii1II , oOo0OOoO0 , iiii111II , I111iIi1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 51 - 51: IIiIi1iI * OooOO000 / ooOoO0O00
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
     if 2 - 2: oo0oO00 + OOoOoo . OooOO000 - ooOoO0O00 + O00OOo00oo0o
     if 54 - 54: ii . oo0oO00 - OooOO000
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0o00o000Oo0 ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( i1I11iIiII ) . replace ( ' ' , '+' )
 if 1 - 1: oOo0O0Ooo - O00OOo00oo0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 62 - 62: oO0o . OooOO000 . OooOO000 % ooOoO0O00 * oo0oO00 % I1ii11iIi11i
 if I1 != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for iiOOooooO0Oo , iiI11ii1I1 in i1I :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    ooOO0oO0oo00o ( ( iiI11ii1I1 + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + iiOOooooO0Oo ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 20 - 20: IIiIi1iI . OOoOoo / iiII11i1I1IIi . ii * IIi + iIi1i1ii1
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
iiIII = '{ZH},' ; iIi11Ii1I1 = '{IX},' ; i1111ii1I = '{LM},'
if 60 - 60: IIi * IIiIi1iI * oO0o
def O0ooOIii1iIIIi11I1 ( url ) :
 IIII11Ii1I11I = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IIII11Ii1I11I )
 for url , O0Oo0o000oO , iii1IIIiiiI , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( O0Oo0o000oO ) . replace ( 'Sezon' , ' Season ' ) + ( iii1IIIiiiI ) . replace ( 'Bölüm' , ' Episode ' ) + iiI11ii1I1 , url , 8063 , '' )
  if 40 - 40: iIi1i1ii1 + Ii1I * O00OOo00oo0o - oo0oO00 % iIi1i1ii1
  if 67 - 67: Ii1I
  if 3 - 3: O00OOo00oo0o . iiII11i1I1IIi % IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * oO0o
  if 5 - 5: IIiIiII11i * ooOoO0O00 % iIi1i1ii1
def oO000O ( url ) :
 IIII11Ii1I11I = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( IIII11Ii1I11I )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( iiI11ii1I1 , url , 222 , '' )
  if 62 - 62: ooOoO0O00 * iI11I1II1I1I % oo0oO00 % OOooOOo / ii
  if 39 - 39: I1ii11iIi11i % OooOO000
  if 90 - 90: oOo0O0Ooo * Ii1I . iiII11i1I1IIi * iIi1i1ii1 - I11i
  if 40 - 40: o0o00Oo0O / OOoOoo - IIiIiII11i + I11i % I1ii11iIi11i
def o00oOo0OoO0oO ( ) :
 if 84 - 84: ooOoO0O00 / ooOoO0O00 - ooOoO0O00 . oo0oO00 . oO0o * Ii1I
 IIII11Ii1I11I = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIII11Ii1I11I )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , iii1IIIiiiI in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 + '  -  ' + ( iii1IIIiiiI ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiOOooooO0Oo , 8063 , oOo0OOoO0 )
  if 57 - 57: Ii1I * OOoOoo - IIiIi1iI
def O0oO00oO0o00o ( ) :
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 8002 , oOo0OOoO0 )
def o0OOo0O00OO0O ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , time , url , iiI11ii1I1 , Oo0oO00 in IIIII11I1IiI :
  I1IIII1i ( '%s %s' % ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , time ) , url , 1015 , oOo0OOoO0 , Oo0oO00 )
  if 58 - 58: oo0oO00
def iiIIiI1i1i1I1 ( ) :
 if 73 - 73: iiII11i1I1IIi + IIiIi1iI * OOooOOo / IIi - oOo0O0Ooo
 i11i1iiiII ( 'Coronation Street' , '' , 8001 , '' )
 i11i1iiiII ( 'Eastenders' , '' , 8002 , '' )
 i11i1iiiII ( 'Emmerdale' , '' , 8003 , '' )
 i11i1iiiII ( 'Hollyoaks' , '' , 8004 , '' )
 i11i1iiiII ( 'Im a Celebrity' , '' , 8005 , '' )
 if 57 - 57: iI11I1II1I1I * IIi - Ii / iiII11i1I1IIi - iI11I1II1I1I + IIiIi1iI
 if 62 - 62: iiII11i1I1IIi % oo0oO00 / ii % ii
 if 65 - 65: o0o00Oo0O . Ii1I * O00OOo00oo0o
 if 39 - 39: iI11I1II1I1I % o0o00Oo0O + I1ii11iIi11i
def OoOo0OO ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Holly' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iiOOooooO0Oo :
    ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 76 - 76: oo0oO00 . o0o00Oo0O * ii + IIiIi1iI
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 53 - 53: I1ii11iIi11i
def I11iIiiI ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'East' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iiOOooooO0Oo :
    ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 88 - 88: Ii1I - iiII11i1I1IIi * ii * OooOO000 . Ii . I11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 96 - 96: oOo0O0Ooo % oOo0O0Ooo / I11i / OOooOOo * IIiIi1iI - O00OOo00oo0o
def OOOoOOOo ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Emmer' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iiOOooooO0Oo :
    ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 82 - 82: I1ii11iIi11i + O00OOo00oo0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 93 - 93: iiII11i1I1IIi * o0o00Oo0O * IIi - I11i / Ii1I
def oooOo0OO ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Coro' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iiOOooooO0Oo :
    ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 9 - 9: iI11I1II1I1I
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 57 - 57: IIiIi1iI / iIi1i1ii1 % I11i % Ii
def o0OO0Oooo ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Celeb' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iiOOooooO0Oo :
    ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 97 - 97: OooOO000
def OoO00o00 ( name , url ) :
 ooOoo0oo00000O = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if ooOoo0oo00000O :
  oo0o0Oo00o0 = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OoO000O0Oo = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( OoO000O0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OoO000O0Oo = open_url ( url )
  i11II = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( OoO000O0Oo ) [ - 1 ]
  oo0o0Oo00o0 = i11II . replace ( '\\/' , '/' )
 IiIiI1I1I1 = xbmcgui . ListItem ( name , '' , '' )
 IiIiI1I1I1 . setPath ( oo0o0Oo00o0 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiIiI1I1I1 )
 if 63 - 63: oO0o % ooOoO0O00 - oo0oO00
 if 12 - 12: ii + O00OOo00oo0o / IIi / I1ii11iIi11i * IIiIiII11i - Ii1I
def i11IIi1Iii1 ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iiOOooooO0Oo , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for iiOOooooO0Oo , iiI11ii1I1 in i1I :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iiOOooooO0Oo , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 19 - 19: ooOoO0O00 % oO0o - Ii1I . O00OOo00oo0o . iIi1i1ii1
def iI1I1 ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Movies' in iiI11ii1I1 :
   i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( iiOOooooO0Oo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def oOOo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0OOoO0 )
 for url in i1I :
  i11i1iiiII ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 30 - 30: ii
  if 20 - 20: OOoOoo + ooOoO0O00 . Ii1I - iI11I1II1I1I
def I1Iii1 ( url ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url , oOo0OOoO0 in IIIII11I1IiI :
  if '{{' in iiI11ii1I1 :
   pass
  else :
   i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOo0OOoO0 )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
oOOOo0Oooo = '{UJ},' ; I1iiIIiI11I = '{WE},' ; I11II1I = '{WP},' ; oOoOo000 = '{PP},'
def iiI1IiI1I1I ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url , oOo0OOoO0 in IIIII11I1IiI :
  if '{{' in iiI11ii1I1 :
   pass
  else :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0OOoO0 )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIIiI1i ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  i1II ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1II ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . IIi
 if 31 - 31: oo0oO00 % ooOoO0O00 . ii - I11i + ii
 if 45 - 45: IIi + iiII11i1I1IIi / ii - iIi1i1ii1 + ii
def ii1i1I1111ii ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '(cooltvseries.com)' in iiI11ii1I1 :
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , iiI11ii1I1 in i1I :
  if '(cooltvseries.com)' in iiI11ii1I1 :
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def oo0ooo0O0O0O ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( ( url ) . replace ( ' ' , '%20' ) )
oO0iIiII111 = '{XX},' ; OO0 = '{UD},' ; iii111 = '{YT},' ; o00O000oooOo = '{JS},' ; O0o00oO0o0 = '{PF},'
if 42 - 42: ii * IIiIiII11i
def O0oooOO ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  ooOO0oO0oo00o ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( iiOOooooO0Oo ) ) , 222 , oOo0OOoO0 )
  if 5 - 5: OOooOOo % Ii1I . IIiIi1iI . iiII11i1I1IIi - Ii
def OOOOOo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  if 'youtu' in url :
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oOo0OOoO0 )
 for url in next :
  i11i1iiiII ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 39 - 39: Ii + IIi % OooOO000 + iIi1i1ii1 * oOo0O0Ooo + O00OOo00oo0o
def Oo00oOo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 51 - 51: OooOO000
def oOI1ii11IiI1I ( url ) :
 OoO000O0Oo = O000oo
 IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOo0OOoO0 )
  if 88 - 88: iI11I1II1I1I . ii % o0o00Oo0O % IIiIi1iI . Ii
  if 80 - 80: o0o00Oo0O . oOo0O0Ooo
  if 53 - 53: IIiIi1iI / ii - IIiIiII11i
  if 68 - 68: ii . ii . iI11I1II1I1I / IIiIi1iI - iiII11i1I1IIi % o0o00Oo0O
  if 19 - 19: ii * oo0oO00
def OoO00OO0 ( ) :
 if 26 - 26: o0o00Oo0O . iiII11i1I1IIi + OooOO000 - iIi1i1ii1 . iiII11i1I1IIi
 i11i1iiiII ( 'All Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'Entertainment' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'Movies' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'Music' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'News' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'Sports' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'Documentary' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'Kids' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'Food' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'Religious' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'USA Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 i11i1iiiII ( 'Other' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 if 2 - 2: Ii1I . I1ii11iIi11i * IIi % IIiIiII11i . OooOO000
 if 46 - 46: OOooOOo + oOo0O0Ooo % ii * Ii - I1ii11iIi11i
def i11I1Ii1Iiii1 ( Cat_Name ) :
 if 64 - 64: iIi1i1ii1 . ii - Ii1I
 iiIiIi = False
 OO0O = '0'
 if Cat_Name == 'All Channels' : iiIiIi = True
 if Cat_Name == 'Entertainment' : OO0O = '1'
 if Cat_Name == 'Movies' : OO0O = '2'
 if Cat_Name == 'Music' : OO0O = '3'
 if Cat_Name == 'News' : OO0O = '4'
 if Cat_Name == 'Sports' : OO0O = '5'
 if Cat_Name == 'Documentary' : OO0O = '6'
 if Cat_Name == 'Kids' : OO0O = '7'
 if Cat_Name == 'Food' : OO0O = '8'
 if Cat_Name == 'Religious' : OO0O = '9'
 if Cat_Name == 'USA Channels' : OO0O = '10'
 if Cat_Name == 'Other' : OO0O = '11'
 if 95 - 95: IIiIi1iI
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 print 'Len Match: >>>' + str ( len ( IIIII11I1IiI ) )
 for iiI11ii1I1 , oOo0OOoO0 , Iii11I in IIIII11I1IiI :
  iI1ii1 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0OOoO0 ) . replace ( '\\' , '' )
  if Iii11I == OO0O :
   i11i1iiiII ( iiI11ii1I1 , '' , 7022 , iI1ii1 )
  elif iiIiIi == True :
   i11i1iiiII ( iiI11ii1I1 , '' , 7022 , iI1ii1 )
  else : pass
  if 81 - 81: IIiIi1iI + oO0o . ooOoO0O00 + ooOoO0O00 / oOo0O0Ooo * O00OOo00oo0o
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 98 - 98: Ii1I - ii / oOo0O0Ooo . IIiIi1iI - ooOoO0O00
def oOOoOo0OoOO ( Search_Name ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , iiOOooooO0Oo , iII1iii , IiiI in IIIII11I1IiI :
  iI1ii1 = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0OOoO0 ) . replace ( '\\' , '' )
  ooOO0oO0oo00o ( Search_Name + ': Link 1' , ( iiOOooooO0Oo ) . replace ( '\\' , '' ) , 222 , iI1ii1 )
  ooOO0oO0oo00o ( Search_Name + ': Link 2' , ( iII1iii ) . replace ( '\\' , '' ) , 222 , iI1ii1 )
  ooOO0oO0oo00o ( Search_Name + ': Link 3' , ( IiiI ) . replace ( '\\' , '' ) , 222 , iI1ii1 )
  if 90 - 90: oO0o / iIi1i1ii1 % iI11I1II1I1I / o0o00Oo0O * oo0oO00 / oOo0O0Ooo
def oooO0O0Oo00 ( ) :
 OoO000O0Oo = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  ooOO0oO0oo00o ( iiI11ii1I1 , ( iiOOooooO0Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def I1I1i ( ) :
 OoO000O0Oo = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  ooOO0oO0oo00o ( iiI11ii1I1 , ( iiOOooooO0Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def iIo0oOOO0 ( ) :
 OoO000O0Oo = O000oo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  ooOO0oO0oo00o ( iiI11ii1I1 , ( iiOOooooO0Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 11 - 11: iiII11i1I1IIi / OOooOOo
def ii1IIi1IIIIi1 ( url ) :
 url
 oOOOoo00 = xbmcgui . ListItem ( iiI11ii1I1 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOOoo00 )
 return
 if 4 - 4: Ii1I - OOoOoo
 if 6 - 6: o0o00Oo0O . ii . O00OOo00oo0o - iIi1i1ii1 / IIiIi1iI
def iIIIIIi11Ii ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OoO000O0Oo )
 for url , I111iIi1 , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , ( I111iIi1 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  i11i1iiiII ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 92 - 92: oo0oO00 / Ii1I
def IiiiIi11i1I1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , I111iIi1 , oOo0OOoO0 in IIIII11I1IiI :
  I1I11i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , I111iIi1 )
  i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 IiI1i11IiIiii = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for OOI1 in IiI1i11IiIiii :
  OooooOOoo0 = ( OOI1 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IIII1i ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , OooooOOoo0 )
  if 59 - 59: ii * I11i / O00OOo00oo0o
def oOooOOoo ( INFO ) :
 iiIiI1i1 ( 'info for workout' , INFO )
 if 12 - 12: oo0oO00 . IIi
 if 52 - 52: Ii / iiII11i1I1IIi % OOoOoo
 if 21 - 21: OooOO000 % OOoOoo % I1ii11iIi11i % o0o00Oo0O
def OoOoooOO00OO ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( iiI11ii1I1 ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def OO000oo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def iii11iII1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '=' in iiI11ii1I1 :
   pass
  else :
   ooOO0oO0oo00o ( ( iiI11ii1I1 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def oOooo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '=' in iiI11ii1I1 :
   pass
  else :
   ooOO0oO0oo00o ( iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 15 - 15: IIiIi1iI * iI11I1II1I1I * oo0oO00
   if 96 - 96: O00OOo00oo0o * iI11I1II1I1I / OOooOOo % IIi * IIiIiII11i
   if 3 - 3: IIi . I1ii11iIi11i / Ii + oO0o
def i1O00oo00o000o ( url ) :
 ooOO0oO0oo00o ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 ooOO0oO0oo00o ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , Oo00OOOOO )
  if 57 - 57: iiII11i1I1IIi - iiII11i1I1IIi % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
  if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - iIi1i1ii1 * iI11I1II1I1I
  if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / oo0oO00 * I11i + IIi
def o0oOO00O000O0 ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Daily' in iiI11ii1I1 :
   i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 9008 , Oo00OOOOO )
def OOOoO000o0O0O ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def oO0oOO ( url ) :
 ooOO0oO0oo00o ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 ooOO0oO0oo00o ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 ooOO0oO0oo00o ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , Oo00OOOOO )
  if 84 - 84: Ii / I11i % iI11I1II1I1I . IIiIi1iI . oO0o / OooOO000
def ooooo0oo0OO ( ) :
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if '.m3u' in iiOOooooO0Oo :
   i11i1iiiII ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + iiOOooooO0Oo ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def IIiII ( url ) :
 OoO000O0Oo = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 48 - 48: OOooOOo . oOo0O0Ooo . iiII11i1I1IIi . OOoOoo
def I1i11i ( ) :
 OoO000O0Oo = O000oo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'category' in iiOOooooO0Oo :
   i11i1iiiII ( iiI11ii1I1 , 'http://www.disclose.tv/' + iiOOooooO0Oo , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 39 - 39: IIi . I1ii11iIi11i - OOooOOo * Ii
   if 4 - 4: OOooOOo * o0o00Oo0O - iiII11i1I1IIi
def O0o0oo0 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , 'http://www.disclose.tv/' + url , 7011 , oOo0OOoO0 )
 for url in next :
  i11i1iiiII ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 86 - 86: Ii + iI11I1II1I1I
  if 87 - 87: oO0o * OOooOOo - I1ii11iIi11i % IIi * Ii
def O0ooooo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'http' in url :
   ooOO0oO0oo00o ( 'video/flv' , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url , iiI11ii1I1 in i1I :
  ooOO0oO0oo00o ( iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url in I1II1 :
  ooOO0oO0oo00o ( 'YT Link' , url , 8043 , oOOOo00O00oOo + 'disclose.png' )
  if 16 - 16: OOooOOo / iIi1i1ii1 . O00OOo00oo0o % Ii % oOo0O0Ooo / IIi
  if 85 - 85: iiII11i1I1IIi + O00OOo00oo0o
def i1III1iI1I ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
  if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
def o000oo ( name , url , img ) :
 I1 = O000oo ( url )
 O0Ooo0o = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1 )
 Iii1iiIIi1i111i = len ( O0Ooo0o )
 if 48 - 48: I1ii11iIi11i . I11i - OooOO000
 if 15 - 15: I11i
 if Iii1iiIIi1i111i == 1 :
  for o0Oo00Oo in O0Ooo0o :
   o0Oo00Oo = o0Oo00Oo . replace ( 'player' , 'watch' )
   i11i11I = o0Oo00Oo + '&fv=&sou='
   OoO00O0oOo = O000oo ( i11i11I )
   ooIII = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( OoO00O0oOo )
   for oOO in ooIII :
    i1iIii1II11 = False
    Resolve ( oOO )
    if 70 - 70: IIi - OOooOOo - OOooOOo . I11i + IIiIiII11i - IIiIiII11i
 elif Iii1iiIIi1i111i > 1 :
  if 28 - 28: oOo0O0Ooo - O00OOo00oo0o
  for o0Oo00Oo in O0Ooo0o :
   Oo0OOo = O000oo ( o0Oo00Oo )
   I1i1i1IIi1I = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( Oo0OOo )
   IIi11iIIiIiI = I1i1i1IIi1I
   IIi11iIIiIiI = ( str ( IIi11iIIiIiI ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + IIi11iIIiIiI
   ooOO0oO0oo00o ( 'DOUBLE LINK' , IIi11iIIiIiI , 424 , '' )
   if 54 - 54: oo0oO00
   for url in I1i1i1IIi1I :
    i11i1iiiII ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     iII1iii = Google . resolve ( url )
    except :
     pass
    try :
     I1ii11I1IiI = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( iII1iii ) )
     for i1IIIii , I1I111i in I1ii11I1IiI :
      if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + oo0oO00
      HD_URLS . append ( i1IIIii )
      SD_URLS . append ( I1I111i )
    except :
     pass
 else :
  pass
  if 58 - 58: OooOO000 - ii
def o00o ( ) :
 if 62 - 62: iiII11i1I1IIi . IIiIiII11i * o0o00Oo0O + ooOoO0O00 * ii + ii
 if 23 - 23: ooOoO0O00
 i11i1iiiII ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 31 - 31: I1ii11iIi11i - iI11I1II1I1I / iiII11i1I1IIi . oO0o
 i11i1iiiII ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 74 - 74: I1ii11iIi11i - IIiIiII11i - OOoOoo
 if 50 - 50: oOo0O0Ooo - oo0oO00 + oo0oO00 * iiII11i1I1IIi + oo0oO00
def oooOoooOOo0 ( ) :
 OoO000O0Oo = O000oo ( 'http://cnfstudio.com/' )
 IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , 'http://cnfstudio.com/genre/' + iiOOooooO0Oo , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 25 - 25: OooOO000 + oOo0O0Ooo + OOooOOo + O00OOo00oo0o % o0o00Oo0O
OOooO0OOoo = xbmcgui . Dialog ( )
if 26 - 26: IIiIi1iI + OOooOOo
II111I1i1 = '{UN},' ; Iio0o0o = '{IG},' ; IiiIOoO00o0o0oo0o = '{PL},' ; i1i1ii11IiI = '{LO},' ; iiIIiiiiiI1iIi = '{LP},' ; IIIII11II1 = '{HA},' ; OOOO0oOO = '{XD},' ; IIIiii = '{TA},' ; I11OoooO = '{DP},' ; i1IIi11 = '{JT},' ; oOIIIII11 = '{JJ},' ; i1i1 = '{MM},' ; IiiIi = '{FQ},' ; IIiiIiI = '{HH},'
if 49 - 49: iIi1i1ii1 . Ii1I % IIiIi1iI . I1ii11iIi11i * IIi
def Ii1iI ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1iII = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOo0OOoO0 )
 i1iII = i1iII
 for url in i1iII :
  i11i1iiiII ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 83 - 83: I11i
def IiooO00Oo ( url ) :
 if 46 - 46: IIiIi1iI - IIiIi1iI * Ii1I / OooOO000 * IIi / I11i
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  i1Oo00 = url + '&fv=&sou='
  i1Oo00 = i1Oo00 . replace ( 'player' , 'watch' )
  O000o0Oo0 = IiI1i1I1i1Iii ( i1Oo00 )
  oOoooO0oo0 = IiI1i1I1i1Iii ( url )
  if 44 - 44: OOooOOo . O00OOo00oo0o . ooOoO0O00 . OOooOOo * IIiIi1iI
  if 59 - 59: IIiIiII11i * ii - ii
def IiI1i1I1i1Iii ( url ) :
 if 33 - 33: o0o00Oo0O . Ii % I11i
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  O0ooOO ( url )
  if 50 - 50: IIiIi1iI
  if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * IIi
def oo0ooO0O ( ) :
 I1IIII1i ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , O0o0Oo , '' )
 if 83 - 83: I1ii11iIi11i / IIiIi1iI
def II1iiIiI1 ( ) :
 if os . path . exists ( iiI1IiI ) :
  Ii1I11IIi1 = open ( iiI1IiI , 'r' )
  for oOOOoo00 in Ii1I11IIi1 :
   I1iiiiI = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oOOOoo00 )
   for iiI11ii1I1 , iiOOooooO0Oo in I1iiiiI :
    ooOO0oO0oo00o ( iiI11ii1I1 , iiOOooooO0Oo , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 12 - 12: oO0o
def i1I1IiI1II1 ( url ) :
 if os . path . exists ( Remote ) :
  I1 = I1iii11 ( url )
  IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for iiI11ii1I1 , url in IIIII11I1IiI :
   url = ( url ) . strip ( )
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 21 - 21: ii . o0o00Oo0O / Ii
  if 86 - 86: OOooOOo / IIi
def Iiii1i1 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + iiOOooooO0Oo
 iiI11ii1I1 = 'plugin.video.GenieTv'
 if 40 - 40: iI11I1II1I1I / IIiIi1iI / oOo0O0Ooo + Ii1I * IIi
 III1i1iI111I1 ( iiOOooooO0Oo , iiI11ii1I1 )
 if 64 - 64: I1ii11iIi11i % OOooOOo . I11i % oOo0O0Ooo / IIi
def II1I ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + iiOOooooO0Oo
 iiI11ii1I1 = 'repository.GenieTv'
 if 74 - 74: OOoOoo - oo0oO00 * oO0o - O00OOo00oo0o
 III1i1iI111I1 ( iiOOooooO0Oo , iiI11ii1I1 )
 if 81 - 81: I11i % iIi1i1ii1 - Ii
 if 34 - 34: iIi1i1ii1 - OOoOoo + O00OOo00oo0o
def OOOoo0OO ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  OoOOIi ( )
 if iI1i11iII111 == 1 :
  oOo0O ( )
  if 40 - 40: OooOO000 * OooOO000 / I11i
  if 42 - 42: iIi1i1ii1 * oOo0O0Ooo - o0o00Oo0O - IIiIi1iI
  if 22 - 22: iI11I1II1I1I / IIiIi1iI / oOo0O0Ooo - I11i
  if 21 - 21: oo0oO00 . Ii * iiII11i1I1IIi . IIi / IIi
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
Iii1Ii111ii1 = 'https://addons.tvaddons.ag/'
if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + iIi1i1ii1 % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def oOo0O ( ) :
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 oO0O = 'https://addons.tvaddons.ag/search/?keyword=' + OO0OO0OO
 I1 = O000oo ( oO0O )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , O0OOO0OOooo00 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , 10054 , 'https://addons.tvaddons.ag/' + O0OOO0OOooo00 , O0o0Oo , '' )
  if 79 - 79: ii + iiII11i1I1IIi * O00OOo00oo0o
  if 63 - 63: IIiIi1iI % oOo0O0Ooo . IIi - IIiIi1iI / I1ii11iIi11i % oOo0O0Ooo
def OoOOIi ( ) :
 I1 = O000oo ( Iii1Ii111ii1 )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'Repositories' in iiI11ii1I1 :
   pass
  elif 'Services' in iiI11ii1I1 :
   pass
  elif 'International' in iiI11ii1I1 :
   pass
  else :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 10053 , 'https://addons.tvaddons.ag/' + oOo0OOoO0 , O0o0Oo , '' )
   if 39 - 39: I11i . ooOoO0O00 % oo0oO00 / iiII11i1I1IIi % o0o00Oo0O
   if 100 - 100: O00OOo00oo0o - OOooOOo
def Addon ( url ) :
 I1 = O000oo ( url )
 oooOoO00O = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'Please' in iiI11ii1I1 :
   pass
  else :
   I1I11i ( iiI11ii1I1 , url , 10054 , 'https://addons.tvaddons.ag/' + oOo0OOoO0 , O0o0Oo , '' )
 for url in oooOoO00O :
  I1IIII1i ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
  if 42 - 42: OOoOoo * OooOO000 . Ii1I - iI11I1II1I1I . IIiIi1iI + iiII11i1I1IIi
  if 35 - 35: OooOO000 . oOo0O0Ooo / IIiIiII11i % OOoOoo
def iiiIiIIiIiiii ( url , name ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   ii1 = os . path . join ( oOO0O00Oo0O0o , name + '.zip' )
   try :
    os . remove ( ii1 )
   except :
    pass
   downloader . download ( url , ii1 , o0oOoO00o )
   I1iIIiiIIi1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print I1iIIiiIIi1i
   print '======================================='
   extract . all ( ii1 , I1iIIiiIIi1i , o0oOoO00o )
   oOOo0O00o ( )
   if 99 - 99: OOoOoo % O00OOo00oo0o
def III1i1iI111I1 ( url , name ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , name + '.zip' )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 I1iIIiiIIi1i = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print I1iIIiiIIi1i
 print '======================================='
 extract . all ( ii1 , I1iIIiiIIi1i , o0oOoO00o )
 oOOo0O00o ( )
 if 61 - 61: o0o00Oo0O + oOo0O0Ooo / ii * OooOO000 / IIiIiII11i / OooOO000
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 56 - 56: OooOO000 * Ii1I - IIiIiII11i % Ii1I
 if 30 - 30: Ii % oO0o * IIiIiII11i - o0o00Oo0O . Ii1I * iI11I1II1I1I
def iIiII1 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , O0OOO0OOooo00 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , url , 1007 , O0OOO0OOooo00 )
def iI1Iii1i1 ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , O0OOO0OOooo00 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , O0OOO0OOooo00 )
  if 87 - 87: Ii * IIiIiII11i - iIi1i1ii1 % ii
  if 55 - 55: ooOoO0O00
def iIIIII1I ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , iconimage , I111iIi1 , iiii111II , name in IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    oooo0OOo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
    for oOOOoo00 in oooo0OOo :
     if oOOOoo00 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    iIIiI11iI1Ii1 ( name , url , 1016 , iconimage , iiii111II , I111iIi1 )
   else :
    if 'youtube' in url :
     oooo0OOo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for oOOOoo00 in oooo0OOo :
      if oOOOoo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0OOOOOo00 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , iiii111II , I111iIi1 )
    else :
     oooo0OOo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for oOOOoo00 in oooo0OOo :
      if oOOOoo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o0OOOOOo00 ( name , url , 222 , iconimage , iiii111II , I111iIi1 )
     i1Oo0oO00o ( 'movies' , 'INFO' )
  else :
   oOOO0oo0 ( url , iconimage , name )
   if 13 - 13: OOooOOo - oO0o * ii
 else :
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
  for url , O0OOO0OOooo00 , name in IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     i11i1iiiII ( name , url , 1016 , O0OOO0OOooo00 )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      ooOO0oO0oo00o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , O0OOO0OOooo00 )
     else :
      oooo0OOo = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
      for oOOOoo00 in oooo0OOo :
       if oOOOoo00 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      ooOO0oO0oo00o ( name , url , 222 , O0OOO0OOooo00 )
      i1Oo0oO00o ( 'movies' , 'INFO' )
   else :
    oOOO0oo0 ( url , O0OOO0OOooo00 , name )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 26 - 26: ii
def oOOO0oo0 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 ooo0000oo0 = ( url ) . replace ( iIi11Ii1I1 , 'http' ) . replace ( OO0 , '.com' ) ;
 O0oooo000o = ( ooo0000oo0 ) . replace ( i1111ii1I , 'a' ) . replace ( O0oO0O , 'b' ) . replace ( IIiiiII11i , 'c' ) . replace ( I1iiIIiI11I , 'd' ) . replace ( IiiIOoO00o0o0oo0o , 'e' ) . replace ( i1IIi11 , 'f' ) ;
 IIiIiI11II = ( O0oooo000o ) . replace ( oO0iIiII111 , 'g' ) . replace ( IIIII11II1 , 'h' ) . replace ( iii111 , 'i' ) . replace ( O0o00oO0o0 , 'j' ) . replace ( iIiIiiIIIi1 , 'k' ) . replace ( i1Ii1i111IIiIi1I , 'l' ) ;
 oOo00Oooo = ( IIiIiI11II ) . replace ( I1iIiii , 'm' ) . replace ( OoOOo0OO0OOoo , 'n' ) . replace ( i1Ii1 , 'o' ) . replace ( Ii111OO0o0o0OOoooo , 'p' ) . replace ( oOO00OOOO0o , 'q' ) . replace ( oOOOO0o0o0o , 'r' ) ;
 I1o0o = ( oOo00Oooo ) . replace ( iI1I11i1IiiI1 , 's' ) . replace ( I11II1I , 't' ) . replace ( ooo000O , 'u' ) . replace ( OoOoOo000Oo0 , 'v' ) . replace ( Oo0ooo0ooo , 'w' ) . replace ( I1o00O00oOooo , 'x' ) ;
 oooii111I1I1I = ( I1o0o ) . replace ( iIIiIi1IiI1 , 'y' ) . replace ( Oo0O , 'z' ) . replace ( II111I1i1 , '.' ) . replace ( Iio0o0o , '(' ) . replace ( i1i1ii11IiI , ')' ) . replace ( iiIIiiiiiI1iIi , '/' ) ;
 Iii1I1III11 = ( oooii111I1I1I ) . replace ( iiIII , '1' ) . replace ( oOoOo000 , '2' ) . replace ( i1ii1IiIiIii , '3' ) . replace ( IIIiii , '4' ) . replace ( I11OoooO , '5' ) . replace ( o00O000oooOo , '6' ) ;
 OOo0ooOOOo0O0 = ( Iii1I1III11 ) . replace ( oOIIIII11 , '7' ) . replace ( i1i1 , '8' ) . replace ( IiiIi , '9' ) . replace ( IIiiIiI , '0' ) . replace ( iIII1I1i , ':' ) . replace ( I1IIIIII1 , '%' ) ;
 url = ( OOo0ooOOOo0O0 ) . replace ( oOOOo0Oooo , '-' ) . replace ( OOOO0oOO , '_' ) ;
 ooOO0oO0oo00o ( name , url , 222 , iconimage ) ;
 if 100 - 100: Ii . IIi . Ii
 if 81 - 81: oOo0O0Ooo
def Ooo0o0OO0 ( ) :
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , O0OOO0OOooo00 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , iiOOooooO0Oo , 1007 , O0OOO0OOooo00 )
def O0o00OoooO ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , O0OOO0OOooo00 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , O0OOO0OOooo00 )
  if 15 - 15: IIiIiII11i - iIi1i1ii1 - OooOO000 . oo0oO00 / Ii
def iiIiiiI ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iiI1IIIi = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iiI1IIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiI1IIIi )
 if 35 - 35: I11i - Ii1I + ooOoO0O00
 if 15 - 15: oOo0O0Ooo / IIi
def O0Oo ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if '-dir-' in iiI11ii1I1 :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , oOo0OOoO0 )
  else :
   i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , oOo0OOoO0 )
   if 37 - 37: I1ii11iIi11i % iiII11i1I1IIi . o0o00Oo0O - oO0o / OOoOoo
def OoOO00ooooo ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIII1i1I = ( 'http://afewbitsmore.com/' )
 IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '[To Parent Directory]' in iiI11ii1I1 :
   iiI11ii1I1 = 'HOME'
   pass
  elif 'HOME' in iiI11ii1I1 :
   pass
  elif '.m3u' in iiI11ii1I1 :
   i11i1iiiII ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , IIII1i1I + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in iiI11ii1I1 :
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , IIII1i1I + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in iiI11ii1I1 :
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , IIII1i1I + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , IIII1i1I + url , 1012 , oOOOo00O00oOo + 'music.png' )
def O0Oooo ( url ) :
 I1 = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 7 - 7: IIiIiII11i - Ii1I / iiII11i1I1IIi % ii + ooOoO0O00
def I1Iii1Ii1II111iIi ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 IIII1i1I = url
 IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '.mp3' in iiI11ii1I1 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '/' , '' ) , IIII1i1I + url , 1011 , oOOOo00O00oOo + 'music.png' )
def oo00ooOOoo ( ) :
 OoO000O0Oo = I1iii11 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , ( 'http://www.cyn.net/music/' + iiOOooooO0Oo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOo0OOoO0 ) . replace ( ' ' , '%20' ) )
def O000OOOo ( url , img ) :
 OoO000O0Oo = I1iii11 ( url )
 iII1iii = url
 img = img
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( iII1iii + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 99 - 99: OOooOOo * OooOO000
def I1IiiiIiI ( url ) :
 OoO000O0Oo = I1iii11 ( url )
 iII1iii = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for type , url , iiI11ii1I1 in IIIII11I1IiI :
  if '[VID]' in type :
   ooOO0oO0oo00o ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , iII1iii + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   I1IiiiIiI ( iII1iii + url )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 7 - 7: IIi . OOoOoo . O00OOo00oo0o / iIi1i1ii1 / I1ii11iIi11i
 if 83 - 83: iiII11i1I1IIi / I1ii11iIi11i
def I1Ii1iIiII ( ) :
 oo00Oo0oO00Oo = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 i1I11iIiII = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO0OO0OO = i1I11iIiII . lower ( )
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 iII1iii = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 IiiI = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 23 - 23: iI11I1II1I1I
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 iii1i1iiiiIi = OOoOO0oo0ooO ( iII1iii )
 Iiii = OOoOO0oo0ooO ( IiiI )
 if 10 - 10: iiII11i1I1IIi - I11i % ii - Ii1I
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for iiI11ii1I1 in IIIII11I1IiI :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( iiI11ii1I1 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiOOooooO0Oo + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 64 - 64: oO0o / oOo0O0Ooo
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for iiI11ii1I1 in i1I :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( iiI11ii1I1 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iII1iii + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 23 - 23: iiII11i1I1IIi * O00OOo00oo0o * I11i - oOo0O0Ooo % OOooOOo + I11i
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  I1II1 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii )
  for iiI11ii1I1 in I1II1 :
   if i1I11iIiII in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( iiI11ii1I1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiiI + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 41 - 41: OOoOoo * ii . IIiIi1iI % Ii
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 11 - 11: iI11I1II1I1I . O00OOo00oo0o - I1ii11iIi11i / iiII11i1I1IIi + IIiIiII11i
    if 29 - 29: iiII11i1I1IIi . Ii + ooOoO0O00 - iIi1i1ii1 + o0o00Oo0O . oOo0O0Ooo
    if 8 - 8: I11i
    if 78 - 78: ooOoO0O00 - I1ii11iIi11i
    if 48 - 48: iIi1i1ii1 - ii + O00OOo00oo0o % I11i - OOooOOo . oOo0O0Ooo
    if 42 - 42: O00OOo00oo0o
I1iIiii = '{SF},' ; OoOOo0OO0OOoo = '{IF},' ; i1Ii1 = '{PW},' ; i1ii1IiIiIii = '{AM},' ; Ii111OO0o0o0OOoooo = '{GF},' ; oOO00OOOO0o = '{DD},' ; oOOOO0o0o0o = '{UO},' ; iI1I11i1IiiI1 = '{LE},' ; ooo000O = '{ZY},' ; OoOoOo000Oo0 = '{UE},' ; Oo0ooo0ooo = '{PE},' ; I1o00O00oOooo = '{JE},' ; iIIiIi1IiI1 = '{TH},' ; Oo0O = '{LK},'
if 70 - 70: I11i / iiII11i1I1IIi + oo0oO00 % oOo0O0Ooo % I1ii11iIi11i + oO0o
if 80 - 80: IIi
def OOooO0oo0o00o ( ) :
 OoO000O0Oo = O000oo ( 'http://www.iwatchseries.me/tv-list/' )
 IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , iiOOooooO0Oo , 8021 , oOOOo00O00oOo + 'iwatch.png' )
def iiii1IiI1i1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oo0O in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 + oo0O , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def ii1iii1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  IiII1II1 ( url )
def IiII1II1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( 'VidSpot - ' + iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url in i1I :
  ooOO0oO0oo00o ( 'VodLocker' , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for iiI11ii1I1 , url in I1II1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   ooOO0oO0oo00o ( 'TheVideo - ' + iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
   if 63 - 63: IIiIiII11i % iI11I1II1I1I * Ii1I / IIiIi1iI % oOo0O0Ooo % ooOoO0O00
def OOOoOOooO0 ( ) :
 OoO000O0Oo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , iiOOooooO0Oo , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 2 - 2: IIiIi1iI - o0o00Oo0O - Ii1I / iiII11i1I1IIi * OOooOOo
  if 26 - 26: Ii1I + O00OOo00oo0o - oo0oO00 + OOoOoo % IIi
def O0000oOo0OO ( ) :
 OoO000O0Oo = O000oo ( 'http://www.animetoon.org/cartoon' )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , iiOOooooO0Oo , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 57 - 57: Ii1I
  if 30 - 30: Ii1I * OOoOoo % OOoOoo * OooOO000 . OooOO000
  if 23 - 23: oO0o % IIiIi1iI - oo0oO00 . Ii1I . ii
def o0OooO0 ( url ) :
 OoO000O0Oo = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 in i1I :
  I11II1i1 = oOo0OOoO0
 I1II1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1II1 :
  i11i1iiiII ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , url , 1003 , I11II1i1 )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def II1I1 ( url , IMAGE ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  print iiI11ii1I1 + '     ' + url
  if 'easy' in url :
   Oo0ooOOO ( url )
  elif 'playpanda' in url :
   Oo0ooOOO ( url )
   if 99 - 99: oO0o - OooOO000 . oO0o % I11i % IIi . o0o00Oo0O
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def Oo0ooOOO ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  ooOO0oO0oo00o ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 56 - 56: oo0oO00 + ooOoO0O00 * OooOO000 - o0o00Oo0O
  if 84 - 84: OooOO000 % oOo0O0Ooo / iI11I1II1I1I * iIi1i1ii1 * iI11I1II1I1I + Ii1I
def O000o ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0o0O00Oo0o0 . add_header ( 'referer' , url )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 76 - 76: IIi
def I1iii11 ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 52 - 52: I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
def i11i1IiIi ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 ooOO0O00OO00 = ( '%s%s' % ( oo0o0Oo0 , url ) )
 i1Oo00 = I1iii11 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , O0OOO0OOooo00 , iiI11ii1I1 in IIIII11I1IiI :
  ooOO0oO0oo00o ( '%s' % ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , O0OOO0OOooo00 )
  if 63 - 63: iiII11i1I1IIi
def O0ooOO ( url ) :
 if 6 - 6: oo0oO00 / Ii1I / oO0o
 OoO00 = open ( oOOoo0Oo , "a" )
 OoO00 . write ( 'url="' + url + '"\n' )
 OoO00 . close
 if 42 - 42: iiII11i1I1IIi
 IiI1iII1II111 = xbmc . Player ( IIiI11i1111Ii ( ) )
 import urlresolver
 try : IiI1iII1II111 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iiI11ii1I1 ) )
 IiI1iII1II111 = xbmc . Player ( IIiI11i1111Ii ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  OOooO0OOoo = xbmcgui . Dialog ( )
  if OOooO0OOoo . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   OOooO0OOoo . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : IiI1iII1II111 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def iIi1I ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  O0O00OoOoOOo = '.mp4'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0ooOO ( url )
  if iI1i11iII111 == 1 :
   i1IIIi111111 ( url , name , O0O00OoOoOOo )
 elif '.mkv' in url :
  O0O00OoOoOOo = '.mkv'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0ooOO ( url )
  if iI1i11iII111 == 1 :
   i1IIIi111111 ( url , name , O0O00OoOoOOo )
 elif '.mp3' in url :
  O0O00OoOoOOo = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0ooOO ( url )
  if iI1i11iII111 == 1 :
   i1IIIi111111 ( url , name , O0O00OoOoOOo )
 elif '.avi' in url :
  O0O00OoOoOOo = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0ooOO ( url )
  if iI1i11iII111 == 1 :
   i1IIIi111111 ( url , name , O0O00OoOoOOo )
 elif '.mov' in url :
  O0O00OoOoOOo = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0ooOO ( url )
  if iI1i11iII111 == 1 :
   i1IIIi111111 ( url , name , O0O00OoOoOOo )
 elif '.mpeg' in url :
  O0O00OoOoOOo = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0ooOO ( url )
  if iI1i11iII111 == 1 :
   i1IIIi111111 ( url , name , O0O00OoOoOOo )
 elif '.mpg' in url :
  O0O00OoOoOOo = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0ooOO ( url )
  if iI1i11iII111 == 1 :
   i1IIIi111111 ( url , name , O0O00OoOoOOo )
 elif '.flv' in url :
  O0O00OoOoOOo = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0ooOO ( url )
  if iI1i11iII111 == 1 :
   i1IIIi111111 ( url , name , O0O00OoOoOOo )
 else :
  O0ooOO ( url )
def i1IIIi111111 ( url , name , cat ) :
 O0Ii1iIii1I1 ( )
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , file )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def O0Ii1iIii1I1 ( ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def II1Ii1 ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iiI11ii1I1 )
 xbmc . sleep ( 1 )
 IiI1iII1II111 = xbmc . Player ( IIiI11i1111Ii ( ) )
 o0oOoO00o . update ( 100 , '%s' % iiI11ii1I1 )
 xbmc . sleep ( 1 )
 IiI1iII1II111 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 91 - 91: ii . ooOoO0O00 + OooOO000 + oOo0O0Ooo * OOooOOo
def iii1 ( url ) :
 IiI1iII1II111 = xbmc . Player ( IIiI11i1111Ii ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : IiI1iII1II111 . play ( url ) . strip ( )
 except : pass
 if 55 - 55: ii + OOoOoo + oOo0O0Ooo - iiII11i1I1IIi - Ii1I / Ii
def o0iI ( url ) :
 IiI1iII1II111 = xbmc . Player ( IIiI11i1111Ii ( ) )
 import urlresolver
 OO000O = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 IiI1iII1II111 . play ( OO000O )
 xbmc . sleep ( 1 )
 IiI1iII1II111 . play ( url )
 if 52 - 52: OooOO000 . OOoOoo - Ii1I * iI11I1II1I1I % I11i / IIiIi1iI
 if 18 - 18: OOooOOo % oo0oO00 % oO0o / OooOO000
def IIiI11i1111Ii ( ) :
 try :
  O0o0ooo00o0O = getSet ( "core-player" )
  if ( O0o0ooo00o0O == 'DVDPLAYER' ) : o0O0O0oO0o = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( O0o0ooo00o0O == 'MPLAYER' ) : o0O0O0oO0o = xbmc . PLAYER_CORE_MPLAYER
  elif ( O0o0ooo00o0O == 'PAPLAYER' ) : o0O0O0oO0o = xbmc . PLAYER_CORE_PAPLAYER
  else : o0O0O0oO0o = xbmc . PLAYER_CORE_AUTO
 except : o0O0O0oO0o = xbmc . PLAYER_CORE_AUTO
 return o0O0O0oO0o
 return True
 if 80 - 80: I11i . OooOO000 . ii
def i11i1iiiII ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i11iIIi11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ooOooo000OO00 = True
 IiIiI1I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIiI1I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I11oo0ooOO = [ ]
  I11oo0ooOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I11oo0ooOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   I11oo0ooOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiIiI1I1I1 . addContextMenuItems ( I11oo0ooOO )
 ooOooo000OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iIIi11 , listitem = IiIiI1I1I1 , isFolder = True )
 return ooOooo000OO00
 if 63 - 63: IIiIi1iI . IIi
def o0oo0o00ooO00 ( name , url , mode , iconimage , fanart , description ) :
 if 66 - 66: oOo0O0Ooo
 i11iIIi11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooOooo000OO00 = True
 IiIiI1I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIiI1I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiIiI1I1I1 . setProperty ( "Fanart_Image" , fanart )
 ooOooo000OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iIIi11 , listitem = IiIiI1I1I1 , isFolder = True )
 return ooOooo000OO00
 if 99 - 99: oO0o % o0o00Oo0O . O00OOo00oo0o - Ii1I . I1ii11iIi11i / OOooOOo
def ooOO0oO0oo00o ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 i11iIIi11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ooOooo000OO00 = True
 IiIiI1I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIiI1I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  I11oo0ooOO = [ ]
  I11oo0ooOO . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   I11oo0ooOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   I11oo0ooOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  IiIiI1I1I1 . addContextMenuItems ( I11oo0ooOO )
 ooOooo000OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iIIi11 , listitem = IiIiI1I1I1 , isFolder = False )
 return ooOooo000OO00
 if 60 - 60: Ii1I
 if 78 - 78: oo0oO00 + IIiIiII11i
 if 55 - 55: ii
 if 90 - 90: oOo0O0Ooo
 if 4 - 4: IIi % IIiIi1iI - IIi - I11i
 if 30 - 30: OOoOoo
def iiIiI1i1 ( heading , announce ) :
 class IIIiIII1 ( ) :
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
   try : OOoO = open ( announce ) ; IiI1Iii1 = OOoO . read ( )
   except : IiI1Iii1 = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiI1Iii1 ) )
   return
 IIIiIII1 ( )
 IIIiIII1 ( )
 if 92 - 92: I1ii11iIi11i + OOoOoo / I1ii11iIi11i + iIi1i1ii1 / IIi
def OO0Oooo0oOO0O ( ) :
 iiIiI1i1 ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 3 - 3: iIi1i1ii1 / o0o00Oo0O * IIiIi1iI - OOooOOo
 if 54 - 54: oo0oO00 . I11i * iiII11i1I1IIi
 if 16 - 16: Ii1I / iiII11i1I1IIi + I11i % Ii % IIi - iIi1i1ii1
 if 37 - 37: IIi * iIi1i1ii1 * iiII11i1I1IIi + OOooOOo / Ii
 if 68 - 68: ii * iiII11i1I1IIi
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 86 - 86: I11i / OOooOOo
 if 40 - 40: OooOO000
 if 62 - 62: IIiIi1iI / IIi
 if 74 - 74: OooOO000 % O00OOo00oo0o / O00OOo00oo0o - iI11I1II1I1I - IIiIiII11i + IIi
 if 92 - 92: iiII11i1I1IIi % O00OOo00oo0o
 if 18 - 18: IIiIi1iI + O00OOo00oo0o / IIi / oo0oO00 + iI11I1II1I1I % OOoOoo
 if 94 - 94: iiII11i1I1IIi
 if 37 - 37: oo0oO00
 if 52 - 52: Ii1I * oOo0O0Ooo . IIi + ooOoO0O00 % oo0oO00 / iI11I1II1I1I
 if 68 - 68: O00OOo00oo0o - OOooOOo . Ii + I11i
 if 71 - 71: Ii / ooOoO0O00 * oOo0O0Ooo / OOooOOo
 if 33 - 33: iiII11i1I1IIi . I1ii11iIi11i
 if 89 - 89: OooOO000 + ooOoO0O00 - OOoOoo + IIiIi1iI . IIiIiII11i
 if 85 - 85: iI11I1II1I1I - iIi1i1ii1 * I1ii11iIi11i . oo0oO00 + O00OOo00oo0o
 if 13 - 13: o0o00Oo0O + iI11I1II1I1I % IIiIiII11i + iI11I1II1I1I
 if 85 - 85: oOo0O0Ooo * iI11I1II1I1I . OooOO000 / OooOO000
 if 43 - 43: oOo0O0Ooo
 if 78 - 78: oO0o % IIiIiII11i + OOooOOo / oOo0O0Ooo
 if 34 - 34: I11i % Ii1I + iIi1i1ii1 * iiII11i1I1IIi / oo0oO00
 if 18 - 18: IIiIi1iI
 if 92 - 92: oO0o % iI11I1II1I1I / OOoOoo * OooOO000 . ooOoO0O00 + oo0oO00
 if 24 - 24: OOoOoo . OooOO000 * OOoOoo % Ii . Ii + ooOoO0O00
 if 64 - 64: iI11I1II1I1I / OOoOoo / I1ii11iIi11i - Ii1I
 if 100 - 100: OOoOoo + ooOoO0O00 * oO0o
def oOooOO0oOo0O0 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + I1iiii1iiiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 1 - 1: ooOoO0O00
def iIiiIIiI11 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iIIII11iII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 78 - 78: OOoOoo + iiII11i1I1IIi - I11i + oO0o / iI11I1II1I1I
def ii111I111i ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + II11111I ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 59 - 59: Ii1I / ii / iiII11i1I1IIi - ooOoO0O00
def OOoOI1i1i1Iii1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OoO00Ooooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 25 - 25: I11i + iI11I1II1I1I + OOoOoo + Ii1I / O00OOo00oo0o - ooOoO0O00
def Ii1I11Ii1iI ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OOOOOo00OOoO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 40 - 40: OooOO000
def Oooo0O00Ooo ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 3 - 3: Ii1I
def OOooOO0oO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iIiIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 15 - 15: ii
def i11iiI1iiIii ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + I1I111iOO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 44 - 44: IIi - OOoOoo + OooOO000
def oooo00OoOoO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + oo0O0I1i1I1i1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , ooI1i , iiii111II , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 70 - 70: o0o00Oo0O . iI11I1II1I1I * IIiIiII11i
def iI1Ii11iIiI1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iIi1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , ooI1i , iiii111II , o0O0Oo00 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , o0O0Oo00 )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 3 - 3: iIi1i1ii1 * IIiIi1iI . oO0o * ii + OOooOOo / o0o00Oo0O
 if 60 - 60: iiII11i1I1IIi
 if 97 - 97: Ii * iI11I1II1I1I / IIiIiII11i
 if 66 - 66: IIiIiII11i + OooOO000 * oo0oO00 % iiII11i1I1IIi / ooOoO0O00 / iI11I1II1I1I
 if 62 - 62: OOooOOo + oo0oO00 * OOoOoo + o0o00Oo0O / IIi + IIiIi1iI
 if 38 - 38: ooOoO0O00 / iI11I1II1I1I + OooOO000
 if 26 - 26: Ii1I . iIi1i1ii1 % I11i
 if 4 - 4: O00OOo00oo0o
 if 80 - 80: I1ii11iIi11i . o0o00Oo0O % I11i . I11i
def o0oOO00 ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for Iii , oo0 , i1iIIi1II1iiI in os . walk ( iIi1ii1I1 ) :
     OOoo000Ooo = 0
     OOoo000Ooo += len ( i1iIIi1II1iiI )
     if OOoo000Ooo > 0 :
      for OOoO in i1iIIi1II1iiI :
       os . unlink ( os . path . join ( Iii , OOoO ) )
  iiii1II = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( iiii1II )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 28 - 28: ii % iiII11i1I1IIi
 if 3 - 3: I11i / I1ii11iIi11i - oO0o + IIiIiII11i
 if 3 - 3: Ii
 if 20 - 20: ooOoO0O00 * OooOO000 + oO0o * oO0o / I1ii11iIi11i
 if 83 - 83: Ii1I
 if 53 - 53: OOooOOo % IIiIi1iI . oO0o + oOo0O0Ooo / Ii1I
 if 76 - 76: Ii1I . iI11I1II1I1I - Ii / Ii1I - I11i
 if 95 - 95: iiII11i1I1IIi
def II11Ii111II1 ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 76 - 76: IIiIiII11i - ooOoO0O00 . o0o00Oo0O * Ii % I11i - OooOO000
def o00o0 ( url ) :
 I1II1IIiI11 = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 IIIii = [
 ( I1II1IIiI11 ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( I1II1IIiI11 , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1II1IIiI11 , 'plugin.video.itv' , 'Images' ) ) ]
 if 29 - 29: OOooOOo
 iii1OO00Oo00o = 0
 if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . IIi
 for oOOOoo00 in IIIii :
  if os . path . exists ( oOOOoo00 ) and not oOOOoo00 in [ oO0o0o0ooO0oO , I1II1IIiI11 ] :
   for Iii , oo0 , i1iIIi1II1iiI in os . walk ( oOOOoo00 ) :
    OOoo000Ooo = 0
    OOoo000Ooo += len ( i1iIIi1II1iiI )
    if OOoo000Ooo > 0 :
     for OOoO in i1iIIi1II1iiI :
      if not OOoO in oooOOOOO :
       try :
        os . unlink ( os . path . join ( Iii , OOoO ) )
       except :
        pass
      else : OOO ( 'Ignore Log File: %s' % OOoO )
     for O0O00OooO in oo0 :
      try :
       shutil . rmtree ( os . path . join ( Iii , O0O00OooO ) )
       iii1OO00Oo00o += 1
       OOO ( "[Success] cleared %s files from %s" % ( str ( OOoo000Ooo ) , os . path . join ( oOOOoo00 , O0O00OooO ) ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( oOOOoo00 , O0O00OooO ) )
  else :
   for Iii , oo0 , i1iIIi1II1iiI in os . walk ( oOOOoo00 ) :
    for O0O00OooO in oo0 :
     if 'cache' in O0O00OooO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( Iii , O0O00OooO ) )
       iii1OO00Oo00o += 1
       OOO ( "[Success] wiped %s " % os . path . join ( oOOOoo00 , O0O00OooO ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( oOOOoo00 , O0O00OooO ) )
       if 3 - 3: o0o00Oo0O - O00OOo00oo0o * iIi1i1ii1 * IIi / iIi1i1ii1
 II11Ii111II1 ( oO , 'Clear Cache: Removed %s Files' % iii1OO00Oo00o )
 if 58 - 58: iIi1i1ii1 * iI11I1II1I1I + IIiIi1iI . IIiIi1iI
 if 74 - 74: IIiIi1iI - I11i * OOoOoo % IIiIi1iI
 if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * O00OOo00oo0o - oO0o - I11i
 if 44 - 44: ii
 if 82 - 82: OOooOOo . OOooOOo
 if 10 - 10: I1ii11iIi11i * Ii1I . oo0oO00 . ii . IIi * Ii1I
 if 80 - 80: O00OOo00oo0o + iiII11i1I1IIi . O00OOo00oo0o + IIi
def Oo00o0O0O ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 OoI11II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Iii , oo0 , i1iIIi1II1iiI in os . walk ( OoI11II ) :
   OOoo000Ooo = 0
   OOoo000Ooo += len ( i1iIIi1II1iiI )
   if 5 - 5: ii - OOoOoo / Ii1I % I1ii11iIi11i / O00OOo00oo0o . Ii1I
   if 86 - 86: ii - OOoOoo - iiII11i1I1IIi * IIiIiII11i
   if OOoo000Ooo > 0 :
    if 61 - 61: IIiIiII11i / Ii - OOooOOo
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( OOoo000Ooo ) + " files found" , "Do you want to delete them?" ) :
     if 32 - 32: Ii
     for OOoO in i1iIIi1II1iiI :
      os . unlink ( os . path . join ( Iii , OOoO ) )
     for O0O00OooO in oo0 :
      shutil . rmtree ( os . path . join ( Iii , O0O00OooO ) )
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
 if 57 - 57: iI11I1II1I1I
 if 99 - 99: OooOO000 % I11i + iI11I1II1I1I
 if 51 - 51: ooOoO0O00 % I11i - oo0oO00 - OOoOoo
 if 14 - 14: IIiIi1iI + iIi1i1ii1
 if 45 - 45: oo0oO00 + IIiIiII11i . OooOO000 / Ii1I
 if 76 - 76: iIi1i1ii1 + OooOO000 - OOoOoo * iI11I1II1I1I % ooOoO0O00
 if 72 - 72: IIiIi1iI + IIiIiII11i . o0o00Oo0O - OooOO000 / ii . O00OOo00oo0o
 if 28 - 28: iI11I1II1I1I . o0o00Oo0O
 if 32 - 32: ii
def O0O0ooOOO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 OoI11II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Iii , oo0 , i1iIIi1II1iiI in os . walk ( OoI11II ) :
   OOoo000Ooo = 0
   OOoo000Ooo += len ( i1iIIi1II1iiI )
   if 29 - 29: Ii1I
   if 41 - 41: iIi1i1ii1
   if OOoo000Ooo > 0 :
    if 49 - 49: iIi1i1ii1 % IIiIiII11i . iIi1i1ii1 - I11i - iiII11i1I1IIi * OOoOoo
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( OOoo000Ooo ) + " files found" , "Do you want to delete them?" ) :
     if 47 - 47: o0o00Oo0O . I11i / iIi1i1ii1 * OooOO000
     for OOoO in i1iIIi1II1iiI :
      os . unlink ( os . path . join ( Iii , OOoO ) )
     for O0O00OooO in oo0 :
      shutil . rmtree ( os . path . join ( Iii , O0O00OooO ) )
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
 o00o0 ( url )
 return
 if 63 - 63: O00OOo00oo0o - oo0oO00 - OooOO000 - IIiIi1iI / oo0oO00 + oO0o
 if 94 - 94: OOoOoo / oOo0O0Ooo . IIiIiII11i
 if 32 - 32: oo0oO00 . IIi % IIi . OOooOOo
 if 37 - 37: IIi + o0o00Oo0O + IIi . OooOO000 . I11i
 if 78 - 78: oOo0O0Ooo / iiII11i1I1IIi + I11i . I1ii11iIi11i / o0o00Oo0O
 if 49 - 49: Ii1I
 if 66 - 66: I11i . Ii1I
 if 18 - 18: I1ii11iIi11i + OOoOoo
 if 79 - 79: oO0o - o0o00Oo0O + IIiIiII11i % iIi1i1ii1 . oOo0O0Ooo
 if 43 - 43: oOo0O0Ooo % Ii1I * iIi1i1ii1
def i11i ( url , name ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1111i = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 IIIi11 = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml.bak' )
 if os . path . exists ( IIIi11 ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   I1111i = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
   try :
    os . remove ( I1111i )
    print '=== GenieTv - REMOVING    ' + str ( I1111i ) + '    ==='
   except :
    pass
   i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
   III1I11i1iIi = open ( I1111i , "w" )
   III1I11i1iIi . write ( i1Oo00 )
   III1I11i1iIi . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( I1111i ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  I1111i = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
  try :
   os . remove ( I1111i )
   print '=== GenieTv - REMOVING    ' + str ( I1111i ) + '    ==='
  except :
   pass
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  III1I11i1iIi = open ( I1111i , "w" )
  III1I11i1iIi . write ( i1Oo00 )
  III1I11i1iIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1111i ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 17 - 17: IIiIiII11i / IIiIi1iI
def o0OO0OOoo0oO ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1111i = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
 try :
  III1I11i1iIi = open ( I1111i ) . read ( )
  if 'zero' in III1I11i1iIi :
   name = '0CACHE'
  elif 'tuxen' in III1I11i1iIi :
   name = 'TUXENS'
  elif 'muckys' in III1I11i1iIi :
   name = 'MUCKYS'
  elif 'p2p1' in III1I11i1iIi :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in III1I11i1iIi :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in III1I11i1iIi :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 98 - 98: I11i * I1ii11iIi11i - iIi1i1ii1 . IIiIi1iI
def iI11i1iI ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1111i = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
 try :
  os . remove ( I1111i )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( I1111i ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 95 - 95: Ii % oO0o % IIiIi1iI
 if 41 - 41: OooOO000 . o0o00Oo0O
 if 74 - 74: I11i . iIi1i1ii1 / ooOoO0O00 + Ii1I + iIi1i1ii1 + Ii
 if 56 - 56: I1ii11iIi11i - I11i / iI11I1II1I1I / iIi1i1ii1 - OOoOoo - I1ii11iIi11i
 if 76 - 76: IIi . oOo0O0Ooo + IIi + iI11I1II1I1I + OOoOoo / iI11I1II1I1I
 if 95 - 95: iiII11i1I1IIi
 if 45 - 45: iiII11i1I1IIi - IIi * OooOO000 - oO0o . iIi1i1ii1
 if 77 - 77: oo0oO00 / iiII11i1I1IIi
 if 49 - 49: OOoOoo
 if 56 - 56: o0o00Oo0O / iiII11i1I1IIi + IIi
def o0ooO0OoOo ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for IIiiiIiI1 , IiIi11i1 , OO0OOo00Oo , IiI1iIIiIi1Ii in IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % IIiiiIiI1 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % OO0OOo00Oo , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % IiI1iIIiIi1Ii )
  inc = inc + 1
  if 69 - 69: IIi % Ii1I / OOooOOo . IIi - OOoOoo
  if 74 - 74: oO0o - I11i - OOoOoo . o0o00Oo0O % IIiIi1iI
  if 32 - 32: OOooOOo . oO0o / I1ii11iIi11i . Ii
  if 9 - 9: iiII11i1I1IIi - IIiIiII11i + O00OOo00oo0o / oo0oO00 % Ii1I
  if 17 - 17: iI11I1II1I1I - IIiIi1iI
  if 99 - 99: I1ii11iIi11i + O00OOo00oo0o % IIiIi1iI - I11i
  if 52 - 52: Ii1I
  if 93 - 93: OooOO000 . Ii
  if 24 - 24: IIi . oO0o + O00OOo00oo0o . oo0oO00 - Ii1I % OooOO000
def iiii1iI1IIiIi ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I1111i = os . path . join ( oOO0O00Oo0O0o , 'addons2.ini' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  III1I11i1iIi = open ( I1111i , "w" )
  III1I11i1iIi . write ( i1Oo00 )
  III1I11i1iIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1111i ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 49 - 49: OOoOoo % ii - oOo0O0Ooo
def O0oo0o0OoO0 ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I1111i = os . path . join ( oOO0O00Oo0O0o , 'settings.xml' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  III1I11i1iIi = open ( I1111i , "w" )
  III1I11i1iIi . write ( i1Oo00 )
  III1I11i1iIi . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1111i ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 95 - 95: oO0o - Ii . oO0o % IIi * o0o00Oo0O + Ii
 if 65 - 65: o0o00Oo0O / OooOO000 . ooOoO0O00 * OooOO000 / iI11I1II1I1I - oo0oO00
def OOOo00OOooO ( ) :
 try :
  OO0OOOoO0O0 = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( OO0OOOoO0O0 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    iII1I1iIi1i = os . path . join ( OO0OOOoO0O0 , "source.db" )
    os . unlink ( iII1I1iIi1i )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 89 - 89: OooOO000 + Ii1I - ii % IIiIi1iI . Ii1I
 if 1 - 1: I1ii11iIi11i * o0o00Oo0O . oOo0O0Ooo + IIiIi1iI / OOooOOo + iiII11i1I1IIi
 if 68 - 68: IIiIiII11i
 if 61 - 61: IIi . Ii1I * oo0oO00 / O00OOo00oo0o - oO0o
 if 18 - 18: O00OOo00oo0o
def O000oo ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 34 - 34: OooOO000 + O00OOo00oo0o * iiII11i1I1IIi / IIiIiII11i
 if 14 - 14: IIiIiII11i + OooOO000 + iIi1i1ii1 / OooOO000 . iI11I1II1I1I
 if 85 - 85: iiII11i1I1IIi % iiII11i1I1IIi . o0o00Oo0O
 if 40 - 40: oO0o * OOooOOo * iI11I1II1I1I / OOooOOo * ii / Ii1I
 if 33 - 33: Ii % I11i . OooOO000 * IIi / iiII11i1I1IIi
 if 25 - 25: oO0o
 if 39 - 39: iIi1i1ii1 * OOooOOo + I1ii11iIi11i . IIi - o0o00Oo0O * Ii1I
def I1i11 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; O0o0ooo00o00 = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if O0o0ooo00o00 :
  IiiIii11iI1Iii1iI = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; IiiIii11iI1Iii1iI = xbmc . translatePath ( IiiIii11iI1Iii1iI ) ;
  I1Iii11I = os . path . join ( IiiIii11iI1Iii1iI , ".." , ".." ) ; I1Iii11I = os . path . abspath ( I1Iii11I ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + I1Iii11I ) ; OOoO00o00oo = False
  try :
   for Iii , oo0 , i1iIIi1II1iiI in os . walk ( I1Iii11I , topdown = True ) :
    oo0 [ : ] = [ O0O00OooO for O0O00OooO in oo0 if O0O00OooO not in o0oO0 ]
    for iiI11ii1I1 in i1iIIi1II1iiI :
     try : os . remove ( os . path . join ( Iii , iiI11ii1I1 ) )
     except :
      if iiI11ii1I1 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : OOoO00o00oo = True
      plugintools . log ( "Error removing " + Iii + " " + iiI11ii1I1 )
    for iiI11ii1I1 in oo0 :
     try : os . rmdir ( os . path . join ( Iii , iiI11ii1I1 ) )
     except :
      if iiI11ii1I1 not in [ "Database" , "userdata" ] : OOoO00o00oo = True
      plugintools . log ( "Error removing " + Iii + " " + iiI11ii1I1 )
   if not OOoO00o00oo : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 IioO0O ( )
 if 5 - 5: oo0oO00 - ii / OOooOOo
 if 30 - 30: iiII11i1I1IIi % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
 if 55 - 55: oO0o
def I111II1ii11I1 ( ) :
 iIiiIII = [ ]
 ii1I = sys . argv [ 2 ]
 if len ( ii1I ) >= 2 :
  IiIi1I1 = sys . argv [ 2 ]
  ooO00OO0ooo = IiIi1I1 . replace ( '?' , '' )
  if ( IiIi1I1 [ len ( IiIi1I1 ) - 1 ] == '/' ) :
   IiIi1I1 = IiIi1I1 [ 0 : len ( IiIi1I1 ) - 2 ]
  O0o = ooO00OO0ooo . split ( '&' )
  iIiiIII = { }
  for III in range ( len ( O0o ) ) :
   i1i1ii1Ii111i = { }
   i1i1ii1Ii111i = O0o [ III ] . split ( '=' )
   if ( len ( i1i1ii1Ii111i ) ) == 2 :
    iIiiIII [ i1i1ii1Ii111i [ 0 ] ] = i1i1ii1Ii111i [ 1 ]
    if 18 - 18: o0o00Oo0O
 return iIiiIII
 if 14 - 14: iIi1i1ii1 / OOoOoo - o0o00Oo0O
i1iii1i11I1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
OoiI1I1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
Iii1I111I = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
OOOoo0ooO0 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
Ii1iiII1i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
Oo0OoO00OO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
I1iiii1iiiI = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
oO000OO0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
iIIII11iII = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
II11111I = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
OoO00Ooooo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OOOOOo00OOoO = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
o000 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
iIiIi1 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
I1I111iOO = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
oo0O0I1i1I1i1Ii = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
OoOo = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
ooOOoOoo0OO = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOOO0oOo00O = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
oO00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OO0ooo0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
oO0O0 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
iIi1i = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oo0o0Oo0 = base64 . decodestring ( 'Q1VOVA==' )
def I1IIII1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 i11iIIi11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooOooo000OO00 = True
 IiIiI1I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIiI1I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiIiI1I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I11oo0ooOO = [ ]
  if showcontext == 'fav' :
   I11oo0ooOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   I11oo0ooOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IiIiI1I1I1 . addContextMenuItems ( I11oo0ooOO )
 ooOooo000OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iIIi11 , listitem = IiIiI1I1I1 , isFolder = True )
 return ooOooo000OO00
 if 65 - 65: O00OOo00oo0o + o0o00Oo0O % I11i
def I1I11i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 i11iIIi11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 ooOooo000OO00 = True
 IiIiI1I1I1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IiIiI1I1I1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 IiIiI1I1I1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  I11oo0ooOO = [ ]
  if showcontext == 'fav' :
   I11oo0ooOO . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   I11oo0ooOO . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  IiIiI1I1I1 . addContextMenuItems ( I11oo0ooOO )
 ooOooo000OO00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iIIi11 , listitem = IiIiI1I1I1 , isFolder = False )
 return ooOooo000OO00
 if 72 - 72: IIi . OOooOOo / IIiIiII11i
 if 69 - 69: IIi * IIiIiII11i - IIiIi1iI - ooOoO0O00 + Ii
IiIi1I1 = I111II1ii11I1 ( )
iiOOooooO0Oo = None
iiI11ii1I1 = None
iiiii1II = None
ooI1i = None
iiii111II = None
o0O0Oo00 = None
iiiiI1iiIi1i = None
Iii1oo0o0oo0O0O = None
if 1 - 1: O00OOo00oo0o - ooOoO0O00 - O00OOo00oo0o . I1ii11iIi11i . ooOoO0O00
if 14 - 14: IIi / O00OOo00oo0o * iIi1i1ii1 + Ii1I * OOooOOo * OOoOoo
try :
 Iii1oo0o0oo0O0O = int ( IiIi1I1 [ "fav_mode" ] )
except :
 pass
 if 87 - 87: Ii1I
try :
 iiOOooooO0Oo = urllib . unquote_plus ( IiIi1I1 [ "url" ] )
except :
 pass
try :
 iiI11ii1I1 = urllib . unquote_plus ( IiIi1I1 [ "name" ] )
except :
 pass
try :
 ooI1i = urllib . unquote_plus ( IiIi1I1 [ "iconimage" ] )
except :
 pass
try :
 iiiii1II = int ( IiIi1I1 [ "mode" ] )
except :
 pass
try :
 iiii111II = urllib . unquote_plus ( IiIi1I1 [ "fanart" ] )
except :
 pass
try :
 o0O0Oo00 = urllib . unquote_plus ( IiIi1I1 [ "description" ] )
except :
 pass
 if 60 - 60: Ii / ooOoO0O00 * IIi
 if 89 - 89: iI11I1II1I1I * I11i + OOooOOo . Ii + Ii1I
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( iiiii1II )
print "URL: " + str ( iiOOooooO0Oo )
print "Name: " + str ( iiI11ii1I1 )
print "IconImage: " + str ( ooI1i )
if 1 - 1: oOo0O0Ooo . iiII11i1I1IIi . Ii1I
if 19 - 19: o0o00Oo0O * iiII11i1I1IIi % ii
def i1Oo0oO00o ( content , viewType ) :
 if 36 - 36: I11i % iiII11i1I1IIi * Ii1I % iIi1i1ii1 + ooOoO0O00 - I1ii11iIi11i
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 56 - 56: Ii1I
if ooI1i == None : ooI1i = Oo00OOOOO
if iiii111II == None : iiii111II = O0o0Oo
if iiiii1II == None :
 o0o0o0oO0oOO ( )
 if 32 - 32: OOooOOo % o0o00Oo0O % Ii - IIiIi1iI . oOo0O0Ooo
elif iiiii1II == 1 :
 OO00o ( iiOOooooO0Oo )
 if 24 - 24: oo0oO00 % I11i / O00OOo00oo0o + I11i
elif iiiii1II == 44 :
 IiIIi1 ( iiOOooooO0Oo )
 if 59 - 59: IIiIiII11i % oOo0O0Ooo * o0o00Oo0O . ii - ii % o0o00Oo0O
elif iiiii1II == 2 :
 IIii1I1i ( )
 if 56 - 56: oo0oO00 - ooOoO0O00 * ii - IIiIiII11i
elif iiiii1II == 3 :
 oo0O0o ( )
 if 28 - 28: ooOoO0O00 / iiII11i1I1IIi . I11i
elif iiiii1II == 21 :
 i1i1II ( )
 if 11 - 11: I1ii11iIi11i * ii - Ii
elif iiiii1II == 4 :
 OOOii1i1iiI ( )
 if 13 - 13: Ii . o0o00Oo0O / IIi * ooOoO0O00
elif iiiii1II == 5 :
 oo0o0OoOO0o0 ( iiOOooooO0Oo )
 if 14 - 14: OOoOoo + OOoOoo . iiII11i1I1IIi / iIi1i1ii1 . iI11I1II1I1I
elif iiiii1II == 6 :
 Oo00o0O0O ( iiOOooooO0Oo )
 if 10 - 10: IIiIiII11i . IIi / OooOO000
elif iiiii1II == 7 :
 i11i ( iiOOooooO0Oo , iiI11ii1I1 )
 if 35 - 35: OooOO000 / I1ii11iIi11i + o0o00Oo0O * iI11I1II1I1I - o0o00Oo0O
elif iiiii1II == 8 :
 o0OO0OOoo0oO ( iiOOooooO0Oo , iiI11ii1I1 )
 if 3 - 3: Ii1I
elif iiiii1II == 9 :
 FIXREPOSADDONS ( iiOOooooO0Oo )
 if 42 - 42: iiII11i1I1IIi % I1ii11iIi11i + OOoOoo - iiII11i1I1IIi . iI11I1II1I1I - iIi1i1ii1
elif iiiii1II == 10 :
 oOOo0O00o ( )
 if 27 - 27: OooOO000 % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
elif iiiii1II == 11 :
 iI11i1iI ( iiOOooooO0Oo )
 if 37 - 37: OooOO000 + O00OOo00oo0o * iIi1i1ii1 + OOoOoo
elif iiiii1II == 12 :
 o0ooO0OoOo ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + iIi1i1ii1 / IIiIiII11i
elif iiiii1II == 13 :
 o0oOO00 ( )
 if 66 - 66: IIiIi1iI + oo0oO00 % ii
elif iiiii1II == 14 :
 o00o0 ( iiOOooooO0Oo )
 if 23 - 23: oo0oO00 . OOooOOo + iI11I1II1I1I
elif iiiii1II == 15 :
 I11o0000o0Oo ( )
 if 17 - 17: OOoOoo
elif iiiii1II == 16 :
 iiii1iI1IIiIi ( iiOOooooO0Oo , iiI11ii1I1 )
 if 12 - 12: ooOoO0O00 . oO0o
elif iiiii1II == 17 :
 O0oo0o0OoO0 ( iiOOooooO0Oo , iiI11ii1I1 )
 if 14 - 14: IIi + IIiIiII11i % IIi . oo0oO00 * IIiIi1iI
elif iiiii1II == 18 :
 OOOo00OOooO ( )
 if 54 - 54: IIiIi1iI * iiII11i1I1IIi - O00OOo00oo0o
elif iiiii1II == 19 :
 I1iIIIiI ( iiOOooooO0Oo )
 if 15 - 15: OooOO000 / o0o00Oo0O
elif iiiii1II == 40 :
 I1ii11I ( iiI11ii1I1 , iiOOooooO0Oo , o0O0Oo00 )
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + IIiIi1iI . O00OOo00oo0o * IIiIi1iI
elif iiiii1II == 42 :
 oO0Oo00oo ( iiI11ii1I1 , iiOOooooO0Oo , o0O0Oo00 )
 if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
elif iiiii1II == 43 :
 I1i11II11i ( iiOOooooO0Oo )
 if 82 - 82: o0o00Oo0O / OooOO000 * oO0o - iiII11i1I1IIi + I1ii11iIi11i
elif iiiii1II == 20 :
 II111iIiI1Ii ( iiOOooooO0Oo )
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + iIi1i1ii1 * IIiIiII11i
elif iiiii1II == 22 :
 oOooOO0oOo0O0 ( iiOOooooO0Oo )
 if 78 - 78: O00OOo00oo0o - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
elif iiiii1II == 23 :
 iIiiIIiI11 ( iiOOooooO0Oo )
 if 97 - 97: ooOoO0O00
elif iiiii1II == 24 :
 ii111I111i ( iiOOooooO0Oo )
 if 29 - 29: oOo0O0Ooo
elif iiiii1II == 25 :
 OOoOI1i1i1Iii1 ( iiOOooooO0Oo )
 if 37 - 37: Ii1I * O00OOo00oo0o * oOo0O0Ooo * o0o00Oo0O
elif iiiii1II == 26 :
 Ii1I11Ii1iI ( iiOOooooO0Oo )
 if 35 - 35: oOo0O0Ooo - Ii1I * OooOO000 + OOoOoo / ooOoO0O00
elif iiiii1II == 27 :
 Oooo0O00Ooo ( iiOOooooO0Oo )
 if 46 - 46: I1ii11iIi11i . IIiIi1iI % I1ii11iIi11i / IIiIiII11i * IIiIi1iI * IIi
elif iiiii1II == 28 :
 OOooOO0oO ( iiOOooooO0Oo )
 if 59 - 59: O00OOo00oo0o * OooOO000
elif iiiii1II == 29 :
 i11iiI1iiIii ( iiOOooooO0Oo )
 if 31 - 31: iiII11i1I1IIi / o0o00Oo0O
elif iiiii1II == 30 :
 oo0ooooo00o ( iiOOooooO0Oo )
 if 57 - 57: ooOoO0O00 % IIiIi1iI
elif iiiii1II == 31 :
 oooo00OoOoO ( iiOOooooO0Oo )
 if 69 - 69: I11i
elif iiiii1II == 32 :
 oO0o0 ( )
 if 69 - 69: O00OOo00oo0o
elif iiiii1II == 33 :
 Ii1i1 ( )
 if 83 - 83: iI11I1II1I1I . I11i + O00OOo00oo0o . ii / IIiIi1iI + IIiIiII11i
elif iiiii1II == 35 :
 i1i ( iiOOooooO0Oo )
 if 90 - 90: iIi1i1ii1 * OooOO000 / IIi
elif iiiii1II == 34 :
 oOoO00 ( iiOOooooO0Oo )
 if 68 - 68: OOooOOo
elif iiiii1II == 36 :
 Ii1I11i11I1i ( iiOOooooO0Oo )
 if 65 - 65: oo0oO00
elif iiiii1II == 37 :
 o0oOOooo00O ( iiOOooooO0Oo )
 if 82 - 82: I11i
elif iiiii1II == 38 :
 ooooO ( iiOOooooO0Oo )
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + O00OOo00oo0o
elif iiiii1II == 41 :
 I1i11 ( IiIi1I1 )
 if 65 - 65: iIi1i1ii1
elif iiiii1II == 39 :
 iI1Ii11iIiI1 ( iiOOooooO0Oo )
 if 71 - 71: O00OOo00oo0o % O00OOo00oo0o . oo0oO00 + Ii - Ii
elif iiiii1II == 45 :
 TEXTS ( )
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / O00OOo00oo0o - Ii . IIiIi1iI / IIi
elif iiiii1II == 46 :
 OO0Oooo0oOO0O ( )
 if 13 - 13: I11i % o0o00Oo0O - O00OOo00oo0o * ii / I1ii11iIi11i - ii
elif iiiii1II == 47 :
 GEVID ( )
 if 78 - 78: oo0oO00 % ii
elif iiiii1II == 48 :
 i1I1IiI1ii ( iiI11ii1I1 , iiOOooooO0Oo , o0O0Oo00 )
 if 73 - 73: oOo0O0Ooo % IIiIi1iI % OOoOoo + ooOoO0O00 - ii / oo0oO00
elif iiiii1II == 49 :
 O00O ( )
 if 78 - 78: ii % oo0oO00 - Ii
elif iiiii1II == 22222 :
 O0ooOO ( iiOOooooO0Oo )
 if 37 - 37: OOoOoo % iIi1i1ii1 % ooOoO0O00
elif iiiii1II == 222 :
 iIi1I ( iiOOooooO0Oo , iiI11ii1I1 )
 if 23 - 23: IIiIi1iI - o0o00Oo0O + Ii
elif iiiii1II == 333 :
 i11i1IiIi ( iiOOooooO0Oo )
 if 98 - 98: ii
 if 61 - 61: I11i . OOoOoo . o0o00Oo0O + ii + o0o00Oo0O
elif iiiii1II == 1020 :
 OOOoOOooO0 ( )
 if 65 - 65: ooOoO0O00 * IIi * ii - OOoOoo . OooOO000 - oO0o
elif iiiii1II == 1021 :
 ANIMEEP ( )
 if 71 - 71: iIi1i1ii1 * OOooOOo
elif iiiii1II == 1022 :
 ANIMEPLAY ( iiOOooooO0Oo )
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % O00OOo00oo0o * I11i
elif iiiii1II == 1001 :
 O0000oOo0OO ( )
 if 64 - 64: IIiIi1iI / IIiIi1iI + Ii1I * IIi % IIi
elif iiiii1II == 1005 :
 Ooo0o0OO0 ( )
 if 87 - 87: oO0o * I1ii11iIi11i
elif iiiii1II == 1007 :
 O0o00OoooO ( iiOOooooO0Oo )
 if 83 - 83: ooOoO0O00 * O00OOo00oo0o - OOoOoo / iIi1i1ii1
elif iiiii1II == 1010 :
 O0Oo ( iiOOooooO0Oo )
 if 48 - 48: oo0oO00 . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
elif iiiii1II == 1011 :
 I1Iii1Ii1II111iIi ( iiOOooooO0Oo )
 if 32 - 32: iIi1i1ii1 * oOo0O0Ooo - IIi . I1ii11iIi11i / o0o00Oo0O + iIi1i1ii1
elif iiiii1II == 1012 :
 OoOO00ooooo ( iiOOooooO0Oo )
 if 67 - 67: OOooOOo % I1ii11iIi11i
elif iiiii1II == 1030 :
 oo00ooOOoo ( )
 if 7 - 7: Ii % Ii1I / O00OOo00oo0o % I1ii11iIi11i - oO0o
elif iiiii1II == 1031 :
 O000OOOo ( iiOOooooO0Oo , ooI1i )
 if 73 - 73: Ii1I
elif iiiii1II == 1032 :
 I1IiiiIiI ( iiOOooooO0Oo )
 if 92 - 92: Ii + o0o00Oo0O * iiII11i1I1IIi
elif iiiii1II == 1006 :
 Parse . ParseURL ( iiOOooooO0Oo )
 if 60 - 60: I11i / I1ii11iIi11i
elif iiiii1II == 2030 :
 Parse . addonParseURL ( iiOOooooO0Oo )
 if 19 - 19: iI11I1II1I1I . oO0o / ii
elif iiiii1II == 2031 :
 Parse . apkParseURL ( iiOOooooO0Oo )
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % O00OOo00oo0o / Ii1I
elif iiiii1II == 1002 :
 o0OooO0 ( iiOOooooO0Oo )
 if 76 - 76: oO0o * oo0oO00 - oO0o
elif iiiii1II == 1003 :
 II1I1 ( iiOOooooO0Oo , ooI1i )
 if 57 - 57: ii / OOooOOo + oo0oO00 . iIi1i1ii1
elif iiiii1II == 1004 :
 Oo0ooOOO ( iiOOooooO0Oo )
 if 14 - 14: Ii % IIi * I11i * OOooOOo
elif iiiii1II == 1008 :
 O0oooOO ( )
 if 55 - 55: O00OOo00oo0o * IIi * O00OOo00oo0o
elif iiiii1II == 1009 :
 i1I1IiI1II1 ( iiOOooooO0Oo )
 if 70 - 70: o0o00Oo0O . iIi1i1ii1
elif iiiii1II == 2001 :
 II1iiIiI1 ( )
 if 33 - 33: IIi * iIi1i1ii1
elif iiiii1II == 2002 :
 O0Oooo ( iiOOooooO0Oo )
 if 64 - 64: Ii . iI11I1II1I1I
elif iiiii1II == 1013 :
 iI1iIiiiI1I1 ( )
elif iiiii1II == 10111113 :
 OOooO0OO0 ( iiOOooooO0Oo )
 if 7 - 7: OOooOOo % IIiIi1iI + OOooOOo - OOooOOo * Ii % oO0o
elif iiiii1II == 1014 :
 O0oO00oO0o00o ( )
 if 57 - 57: IIi / oO0o + Ii1I
elif iiiii1II == 1015 :
 o0OOo0O00OO0O ( iiOOooooO0Oo )
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % IIi + OOoOoo . oO0o . I1ii11iIi11i
elif iiiii1II == 1016 :
 iIIIII1I ( iiOOooooO0Oo , ooI1i , iiI11ii1I1 )
 if 70 - 70: iiII11i1I1IIi . Ii1I * oo0oO00
elif iiiii1II == 1017 :
 OOo0 ( )
 if 97 - 97: oo0oO00 . iI11I1II1I1I - IIi
elif iiiii1II == 1018 :
 i1i11I1I1iii1 ( iiOOooooO0Oo )
 if 23 - 23: Ii1I % iiII11i1I1IIi
elif iiiii1II == 1023 :
 ii11I1 ( )
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
elif iiiii1II == 1024 :
 iIiII1 ( iiOOooooO0Oo )
 if 99 - 99: O00OOo00oo0o - Ii1I - oOo0O0Ooo - O00OOo00oo0o + oO0o + IIiIiII11i
elif iiiii1II == 1025 :
 iI1Iii1i1 ( iiOOooooO0Oo )
 if 34 - 34: O00OOo00oo0o * iiII11i1I1IIi
elif iiiii1II == 4001 :
 I11iIiI1I1i11 ( )
 if 31 - 31: OOoOoo . oo0oO00
elif iiiii1II == 4002 :
 iII1i11IIi1i ( )
 if 40 - 40: iIi1i1ii1 - iiII11i1I1IIi / IIiIiII11i * ooOoO0O00 + OOoOoo * IIiIiII11i
elif iiiii1II == 4003 :
 I1ii ( )
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - O00OOo00oo0o
elif iiiii1II == 4004 :
 iiI1iI111ii1i ( )
 if 99 - 99: iIi1i1ii1 - OOoOoo - ooOoO0O00 / Ii . OOoOoo
elif iiiii1II == 4005 :
 Ii1IIiI1IiIII ( )
 if 58 - 58: IIi
elif iiiii1II == 4006 :
 oooooOOO000Oo ( )
 if 12 - 12: oOo0O0Ooo . I11i * ii
elif iiiii1II == 4007 :
 O0i11I1I1I ( )
 if 64 - 64: OOooOOo + OOoOoo - ooOoO0O00 . IIiIiII11i . oO0o
elif iiiii1II == 4008 :
 iIII ( )
 if 31 - 31: oo0oO00 . OooOO000 - iiII11i1I1IIi . iI11I1II1I1I + iiII11i1I1IIi . OOooOOo
elif iiiii1II == 4009 : oOoooooOoO ( )
elif iiiii1II == 4010 : ooOOOo ( )
elif iiiii1II == 3000 :
 oo0ooO0O ( )
 if 86 - 86: Ii1I - Ii1I / OooOO000 - Ii1I * OooOO000 + O00OOo00oo0o
elif iiiii1II == 3001 :
 iiI1I ( )
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - OOoOoo
elif iiiii1II == 3002 :
 O0oooO00ooO0 ( iiOOooooO0Oo )
 if 30 - 30: ii % IIi
elif iiiii1II == 3003 :
 o00OOO0o00OO ( iiOOooooO0Oo )
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - IIi
elif iiiii1II == 3004 :
 Oo0OOOOOOO0oo ( iiOOooooO0Oo )
 if 81 - 81: OooOO000 % iIi1i1ii1 . IIiIi1iI
elif iiiii1II == 404 :
 iiIiiiI ( iiI11ii1I1 , iiOOooooO0Oo , ooI1i )
 if 66 - 66: Ii1I * iIi1i1ii1 / ii * o0o00Oo0O % IIi
elif iiiii1II == 405 :
 II1Ii1 ( iiOOooooO0Oo )
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * iIi1i1ii1 / O00OOo00oo0o * ii
elif iiiii1II == 7030 :
 OoO00OO0 ( )
 if 82 - 82: I1ii11iIi11i / iIi1i1ii1 / iIi1i1ii1 % iIi1i1ii1
elif iiiii1II == 7021 :
 i11I1Ii1Iiii1 ( iiI11ii1I1 )
 if 20 - 20: IIiIi1iI
elif iiiii1II == 7022 :
 oOOoOo0OoOO ( iiI11ii1I1 )
 if 63 - 63: iI11I1II1I1I . oO0o
elif iiiii1II == 7000 :
 o000oo ( iiI11ii1I1 , iiOOooooO0Oo , img )
 if 100 - 100: ooOoO0O00 * ooOoO0O00
elif iiiii1II == 7050 :
 OOOOOo ( iiOOooooO0Oo )
 if 26 - 26: IIi . oO0o % OOooOOo
elif iiiii1II == 7051 :
 Oo00oOo ( iiOOooooO0Oo )
 if 94 - 94: OOoOoo
elif iiiii1II == 7052 :
 ii1i1I1111ii ( iiOOooooO0Oo )
 if 15 - 15: iIi1i1ii1 - OOoOoo / o0o00Oo0O
elif iiiii1II == 7053 :
 oo0ooo0O0O0O ( iiOOooooO0Oo )
 if 28 - 28: O00OOo00oo0o . ooOoO0O00 / Ii1I
elif iiiii1II == 7054 :
 CoolPlay ( iiOOooooO0Oo )
 if 77 - 77: Ii / O00OOo00oo0o / Ii % OOooOOo - O00OOo00oo0o
elif iiiii1II == 7060 :
 iI1I1 ( )
 if 80 - 80: O00OOo00oo0o % OOooOOo . ii . IIiIiII11i % OOoOoo
elif iiiii1II == 7061 :
 I1Iii1 ( iiOOooooO0Oo )
 if 6 - 6: O00OOo00oo0o % OOoOoo / iIi1i1ii1 + O00OOo00oo0o . oo0oO00
elif iiiii1II == 7063 :
 oOOo ( iiOOooooO0Oo )
 if 70 - 70: iI11I1II1I1I / iIi1i1ii1
elif iiiii1II == 7062 :
 iiI1IiI1I1I ( iiOOooooO0Oo )
 if 61 - 61: o0o00Oo0O * I11i + O00OOo00oo0o - IIi . oOo0O0Ooo - OOoOoo
elif iiiii1II == 7064 :
 NATatozcat ( )
 if 7 - 7: Ii1I
elif iiiii1II == 7067 :
 IIIiI1i ( iiOOooooO0Oo )
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / iiII11i1I1IIi
elif iiiii1II == 7066 :
 NATatozA ( iiOOooooO0Oo )
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
elif iiiii1II == 7065 :
 i1II ( iiOOooooO0Oo )
 if 13 - 13: Ii
elif iiiii1II == 7070 :
 i11IIi1Iii1 ( )
 if 54 - 54: IIi . Ii1I * iiII11i1I1IIi % O00OOo00oo0o . o0o00Oo0O * OOoOoo
elif iiiii1II == 7071 :
 DIZIlist ( iiOOooooO0Oo )
 if 87 - 87: iIi1i1ii1 % Ii1I * I1ii11iIi11i
elif iiiii1II == 7072 :
 DIZIpull ( iiOOooooO0Oo )
 if 59 - 59: I1ii11iIi11i / iiII11i1I1IIi - iI11I1II1I1I * iI11I1II1I1I
elif iiiii1II == 7073 :
 WATCHDIZI ( iiOOooooO0Oo )
 if 18 - 18: iiII11i1I1IIi * Ii1I / Ii / iI11I1II1I1I * ii . IIi
elif iiiii1II == 7002 :
 oooOoooOOo0 ( )
 if 69 - 69: I1ii11iIi11i * IIiIi1iI
elif iiiii1II == 7003 :
 Ii1iI ( iiOOooooO0Oo )
 if 91 - 91: I11i . IIiIi1iI / oO0o / Ii * I11i
elif iiiii1II == 7004 :
 IiooO00Oo ( iiOOooooO0Oo )
 if 52 - 52: oOo0O0Ooo - Ii / OOoOoo . oo0oO00
elif iiiii1II == 7020 :
 IiI1i1I1i1Iii ( iiOOooooO0Oo )
 if 38 - 38: oo0oO00 + ii * OOooOOo % oo0oO00
elif iiiii1II == 7001 :
 I1i11i ( )
 if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
elif iiiii1II == 7010 :
 O0o0oo0 ( iiOOooooO0Oo )
 if 24 - 24: OOooOOo * iIi1i1ii1
elif iiiii1II == 7011 :
 O0ooooo ( iiOOooooO0Oo )
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
elif iiiii1II == 7012 :
 i1III1iI1I ( iiOOooooO0Oo )
 if 81 - 81: IIi
elif iiiii1II == 7013 :
 cnfTVPlay2 ( iiOOooooO0Oo )
elif iiiii1II == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iiOOooooO0Oo )
elif iiiii1II == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iiOOooooO0Oo )
elif iiiii1II == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iiI11ii1I1 , iiOOooooO0Oo , ooI1i )
elif iiiii1II == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iiiii1II == 7018 :
 o00o ( )
elif iiiii1II == 7019 :
 CNF_Studio_Indexer . List_Movies ( iiOOooooO0Oo )
elif iiiii1II == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iiOOooooO0Oo )
elif iiiii1II == 7024 :
 CNF_Studio_Indexer . Box_Office ( iiOOooooO0Oo )
 if 58 - 58: IIiIiII11i . O00OOo00oo0o . iIi1i1ii1 * ii / iIi1i1ii1 / iiII11i1I1IIi
elif iiiii1II == 8000 :
 iiIIiI1i1i1I1 ( )
elif iiiii1II == 8001 :
 oooOo0OO ( )
elif iiiii1II == 8002 :
 I11iIiiI ( )
elif iiiii1II == 8003 :
 OOOoOOOo ( )
elif iiiii1II == 8004 :
 OoOo0OO ( )
elif iiiii1II == 8005 :
 o0OO0Oooo ( )
elif iiiii1II == 8006 :
 OoO00o00 ( iiI11ii1I1 , iiOOooooO0Oo )
elif iiiii1II == 8030 :
 O0o00oO0oOO ( iiOOooooO0Oo )
elif iiiii1II == 8045 :
 IiII1I ( iiOOooooO0Oo )
elif iiiii1II == 8046 :
 O0oO0 ( iiOOooooO0Oo )
elif iiiii1II == 8047 :
 o0OOO ( iiOOooooO0Oo )
elif iiiii1II == 8048 :
 O0O0O0OO00oo ( iiOOooooO0Oo )
elif iiiii1II == 8049 :
 I11IIIIiI1 ( iiOOooooO0Oo )
elif iiiii1II == 804900 :
 o0oOOO ( iiOOooooO0Oo )
elif iiiii1II == 8020 :
 OOooO0oo0o00o ( )
elif iiiii1II == 8021 :
 iiii1IiI1i1 ( iiOOooooO0Oo )
elif iiiii1II == 8022 :
 ii1iii1 ( iiOOooooO0Oo )
elif iiiii1II == 8023 :
 IiII1II1 ( iiOOooooO0Oo )
elif iiiii1II == 8040 :
 ooooO0oOoOOoO ( )
elif iiiii1II == 8041 :
 IIiIi1i1I11 ( iiOOooooO0Oo )
elif iiiii1II == 8042 :
 o00O ( iiOOooooO0Oo )
elif iiiii1II == 8043 :
 yt . PlayVideo ( iiOOooooO0Oo )
elif iiiii1II == 8044 :
 IIIIIiiI ( iiOOooooO0Oo )
elif iiiii1II == 8060 :
 Ii1II1I11i1 ( )
elif iiiii1II == 8061 :
 I11Iii11i11I1 ( iiOOooooO0Oo )
elif iiiii1II == 8064 :
 ooOO0OoO ( )
elif iiiii1II == 8065 :
 OOo000o ( iiOOooooO0Oo )
elif iiiii1II == 8070 :
 ooOO00o0 ( )
elif iiiii1II == 8071 :
 Ii1I1iIiiI1 ( iiOOooooO0Oo )
elif iiiii1II == 7080 :
 o00i111iiIiiIiI ( iiOOooooO0Oo )
elif iiiii1II == 8090 :
 I1i1ii1ii ( )
elif iiiii1II == 8091 :
 I11II11IiI11 ( iiOOooooO0Oo )
elif iiiii1II == 8092 :
 iIOO0O ( iiOOooooO0Oo )
elif iiiii1II == 8093 :
 O00oIi11Iiii1iiii ( iiOOooooO0Oo )
elif iiiii1II == 8081 :
 o00oOo0OoO0oO ( )
elif iiiii1II == 8062 :
 O0ooOIii1iIIIi11I1 ( iiOOooooO0Oo )
elif iiiii1II == 8063 :
 oO000O ( iiOOooooO0Oo )
elif iiiii1II == 8050 :
 I111I1I ( )
elif iiiii1II == 8051 :
 Oo0000 ( iiOOooooO0Oo )
elif iiiii1II == 8052 :
 oO0OoOo ( iiOOooooO0Oo )
elif iiiii1II == 8085 :
 IIi1i1ii11I1 ( )
elif iiiii1II == 8086 :
 oOO0Oo ( iiOOooooO0Oo )
elif iiiii1II == 8087 :
 I1ii1iOO00OoOO ( iiOOooooO0Oo )
elif iiiii1II == 8088 :
 iiii1II1ii11 ( iiOOooooO0Oo , iiI11ii1I1 )
elif iiiii1II == 9000 :
 iiI1iI1I ( )
elif iiiii1II == 1111 :
 I1Ii1iIiII ( )
elif iiiii1II == 9001 :
 iii11I ( )
elif iiiii1II == 9002 :
 ii1iIi1iIiI1i ( )
elif iiiii1II == 9003 :
 oO0o00o000Oo0 ( )
elif iiiii1II == 9004 :
 World1 ( )
elif iiiii1II == 9005 :
 World2 ( iiOOooooO0Oo )
elif iiiii1II == 9006 :
 World3 ( iiOOooooO0Oo )
elif iiiii1II == 9007 :
 o0oOO00O000O0 ( )
elif iiiii1II == 9008 :
 OOOoO000o0O0O ( iiOOooooO0Oo )
elif iiiii1II == 9009 :
 oO0oOO ( iiOOooooO0Oo )
elif iiiii1II == 9010 :
 ooooo0oo0OO ( )
elif iiiii1II == 9011 :
 IIiII ( iiOOooooO0Oo )
elif iiiii1II == 50 :
 OOOOO0 ( iiOOooooO0Oo )
elif iiiii1II == 9020 :
 champlist ( )
elif iiiii1II == 9021 :
 oooO0O0Oo00 ( )
elif iiiii1II == 9022 :
 I1I1i ( )
elif iiiii1II == 9023 :
 iIo0oOOO0 ( )
elif iiiii1II == 9024 :
 ii1IIi1IIIIi1 ( iiOOooooO0Oo )
elif iiiii1II == 9030 :
 OoOoooOO00OO ( iiOOooooO0Oo )
elif iiiii1II == 9031 :
 OO000oo ( iiOOooooO0Oo )
elif iiiii1II == 9032 :
 iii11iII1 ( iiOOooooO0Oo )
elif iiiii1II == 9033 :
 oOooo ( iiOOooooO0Oo )
elif iiiii1II == 9034 :
 IiIi ( )
elif iiiii1II == 7085 :
 iIIIIIi11Ii ( iiOOooooO0Oo )
elif iiiii1II == 7086 :
 IiiiIi11i1I1 ( iiOOooooO0Oo )
elif iiiii1II == 7087 :
 oOooOOoo ( o0O0Oo00 )
elif iiiii1II == 9666 :
 O0O0ooOOO ( iiOOooooO0Oo )
elif iiiii1II == 10100 : oOoo00 ( )
elif iiiii1II == 101001 : O00o ( iiOOooooO0Oo )
elif iiiii1II == 10105 : oooOOO0o0O0 ( iiOOooooO0Oo )
elif iiiii1II == 10106 : iiiI1IiI ( iiOOooooO0Oo )
elif iiiii1II == 10104 : IIIiII11 ( iiOOooooO0Oo )
elif iiiii1II == 10107 : Iii1iIIiii1ii ( )
elif iiiii1II == 10103 : Ii111IIIIii ( iiOOooooO0Oo )
elif iiiii1II == 10108 : O00O0 ( iiOOooooO0Oo )
elif iiiii1II == 10000 : Origin_Menu ( )
elif iiiii1II == 10001 : oOOO ( )
elif iiiii1II == 10002 : OO0Oo000OOOoO ( )
elif iiiii1II == 10003 : o0o0O ( )
elif iiiii1II == 10004 : OOO0ooo ( iiOOooooO0Oo )
elif iiiii1II == 10005 : OOooO ( )
elif iiiii1II == 10006 : o0OO0oooo ( iiOOooooO0Oo )
elif iiiii1II == 10007 : iiIiIIi11I1 ( iiOOooooO0Oo , ooI1i )
elif iiiii1II == 10008 : oooooO0oO0ooO ( )
elif iiiii1II == 10009 : ooo ( )
elif iiiii1II == 10010 : i1111Ii11i ( iiOOooooO0Oo )
elif iiiii1II == 10011 : O0OoOo ( iiOOooooO0Oo )
elif iiiii1II == 10012 : iii1 ( iiOOooooO0Oo )
elif iiiii1II == 10109 : o0iI ( iiOOooooO0Oo )
elif iiiii1II == 10013 : OO000OOOo0Oo ( iiOOooooO0Oo )
elif iiiii1II == 10014 : iI1 ( )
elif iiiii1II == 10015 : O0oO0o0OOOOOO ( )
elif iiiii1II == 10016 : iii1I1i ( iiOOooooO0Oo )
elif iiiii1II == 10017 : iIIiiiI1iI1 ( )
elif iiiii1II == 10018 : O0ooO00o ( )
elif iiiii1II == 10019 : iiii11iI1 ( )
elif iiiii1II == 10020 : oooO0o0oOoO ( )
elif iiiii1II == 10021 : OOOOO000oo0 ( )
elif iiiii1II == 10022 : oooO0o ( iiOOooooO0Oo )
elif iiiii1II == 10023 : oO0o0ooO ( iiI11ii1I1 , iiOOooooO0Oo )
elif iiiii1II == 10024 : I111ii1iI ( iiOOooooO0Oo )
elif iiiii1II == 10025 : O0iIiIIIIIii ( )
elif iiiii1II == 10026 : oooo0o0OOO0 ( )
elif iiiii1II == 10027 : ooo0oO0oOo ( )
elif iiiii1II == 10028 : I1iIiIii ( )
elif iiiii1II == 10029 : i1IIiIIIi1 ( )
elif iiiii1II == 423 : OOOooO00OO00O ( iiOOooooO0Oo )
elif iiiii1II == 426 : O0o00 ( iiOOooooO0Oo )
elif iiiii1II == 10030 : Izle_Films ( )
elif iiiii1II == 10031 : Latest_Izle_Movies ( )
elif iiiii1II == 10032 : Izle_Genres ( )
elif iiiii1II == 10033 : Izle_Pop_Movies ( )
elif iiiii1II == 10034 : Izle_Boxsets ( )
elif iiiii1II == 10035 : Izle_Search ( )
elif iiiii1II == 10036 : Izle_Genres_Movie ( iiOOooooO0Oo )
elif iiiii1II == 10037 : Izle_Boxset_single ( iiOOooooO0Oo )
elif iiiii1II == 10038 : Izle_IFRAME ( )
elif iiiii1II == 10039 : Izle_Boxsets_Next ( iiOOooooO0Oo )
elif iiiii1II == 10040 : iiI1iIii1i ( )
elif iiiii1II == 10041 : iIi11iI1i ( iiOOooooO0Oo )
elif iiiii1II == 10042 : Oo0Ooo ( iiOOooooO0Oo )
elif iiiii1II == 10043 : iIIIOoO0000 ( )
elif iiiii1II == 10044 : Oo0OOOoOO ( iiOOooooO0Oo )
elif iiiii1II == 10045 : IIii1i ( iiI11ii1I1 )
elif iiiii1II == 10046 : OoO0o0OO ( iiOOooooO0Oo )
elif iiiii1II == 10047 : IIII1I ( iiOOooooO0Oo )
elif iiiii1II == 10048 : o000ooOo0o0OO ( iiOOooooO0Oo )
elif iiiii1II == 10049 : IIiII11 ( iiOOooooO0Oo )
elif iiiii1II == 10050 : OOOoo0OO ( )
elif iiiii1II == 10051 : OoOOIi ( )
elif iiiii1II == 10052 : oOo0O ( )
elif iiiii1II == 10053 : Addon ( iiOOooooO0Oo )
elif iiiii1II == 10054 : iiiIiIIiIiiii ( iiOOooooO0Oo , iiI11ii1I1 )
elif iiiii1II == 10055 :
 ooo00 ( "addFavorite" )
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 o0OO0OO000OO ( iiI11ii1I1 , iiOOooooO0Oo , ooI1i , iiii111II , Iii1oo0o0oo0O0O )
elif iiiii1II == 10056 :
 ooo00 ( "rmFavorite" )
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 I111 ( iiI11ii1I1 )
elif iiiii1II == 10057 :
 ooo00 ( "getFavorites" )
 iIIIiIi1i ( )
elif iiiii1II == 10058 : Ii111 ( )
elif iiiii1II == 10059 : Donators_Guide ( )
elif iiiii1II == 10060 : OOoooO00o0oo0 ( )
elif iiiii1II == 10061 : iiIii ( )
elif iiiii1II == 10062 : OOoO00ooO ( iiI11ii1I1 , iiOOooooO0Oo , o0O0Oo00 )
elif iiiii1II == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
elif iiiii1II == 10064 : iI1I11iIIi1 ( )
elif iiiii1II == 10065 : oOOo0oo0o0o0 ( iiOOooooO0Oo )
elif iiiii1II == 10066 : OooOoOOo0oO00 ( iiOOooooO0Oo )
elif iiiii1II == 10068 : O0o0O0 ( iiOOooooO0Oo )
elif iiiii1II == 10069 : Oo0 ( iiOOooooO0Oo )
elif iiiii1II == 10070 : I1iI1I1 ( iiOOooooO0Oo )
elif iiiii1II == 10071 : Genie_Watch ( )
elif iiiii1II == 10072 : I11I ( )
elif iiiii1II == 10073 : ooO00O00oOO ( iiOOooooO0Oo )
elif iiiii1II == 10074 : ooooOooooOOo ( iiOOooooO0Oo )
elif iiiii1II == 10075 : o0OoO00 ( ooI1i , iiI11ii1I1 , iiOOooooO0Oo )
elif iiiii1II == 10076 : o0Oii1111i ( iiOOooooO0Oo )
elif iiiii1II == 10077 : oO0oooooo ( iiOOooooO0Oo )
elif iiiii1II == 10078 : ooOoOOOOo ( )
elif iiiii1II == 10079 : Genie_Watch_Tv_Shows ( )
elif iiiii1II == 10080 : Genie_Watch_Tv_Genre ( iiOOooooO0Oo )
elif iiiii1II == 10081 : Genie_Watch_TV_PlayRun ( iiOOooooO0Oo )
elif iiiii1II == 10082 : Genie_Watch_TV_Episodes ( iiOOooooO0Oo , ooI1i )
elif iiiii1II == 10083 : Genie_Watch_Tv_Recent ( iiOOooooO0Oo )
elif iiiii1II == 10084 : OOo ( )
elif iiiii1II == 10085 : Iiii1i1 ( )
elif iiiii1II == 10086 : II1I ( )
elif iiiii1II == 20000 : ooo0oooo0 ( )
elif iiiii1II == 20001 : Iii11111iiI ( iiOOooooO0Oo )
elif iiiii1II == 20002 : OOOoO00O ( iiOOooooO0Oo )
elif iiiii1II == 20003 : o0O0O ( iiOOooooO0Oo )
elif iiiii1II == 20004 : iIIIII1iI ( iiOOooooO0Oo )
elif iiiii1II == 20005 : O00oooooo ( iiOOooooO0Oo )
elif iiiii1II == 21004 : O00O0OO00oo ( )
elif iiiii1II == 21005 : Ooo00O0 ( iiOOooooO0Oo )
elif iiiii1II == 21006 : iiI11i ( iiOOooooO0Oo )
elif iiiii1II == 21007 : o0oO0o0oo0O0 ( iiOOooooO0Oo )
elif iiiii1II == 30000 : O0oOo00Ooo0o0 ( )
elif iiiii1II == 30001 : iiIiii ( )
elif iiiii1II == 10012 : Resolve ( iiOOooooO0Oo )
elif iiiii1II == 30003 : OOoooOoO0 ( )
elif iiiii1II == 30004 : oo0oOO ( iiOOooooO0Oo )
elif iiiii1II == 30005 : oooOo ( iiOOooooO0Oo )
elif iiiii1II == 30006 : Ii1Ii1 ( )
elif iiiii1II == 30007 : II111I1Iii ( )
elif iiiii1II == 30008 : oOOOOO0Ooooo ( iiOOooooO0Oo )
elif iiiii1II == 30009 : O0OooOO ( iiOOooooO0Oo )
elif iiiii1II == 30010 : o0OOOOOo0 ( iiOOooooO0Oo )
elif iiiii1II == 30011 : I1oOoO0OOO00O ( )
elif iiiii1II == 30012 : OoOO00 ( )
elif iiiii1II == 30013 : o0II1IIi1iII1i ( )
elif iiiii1II == 30014 : oOO00ooOOo ( )
elif iiiii1II == 30015 : oO0ooooo0O00 ( iiOOooooO0Oo , ooI1i , iiii111II )
elif iiiii1II == 30016 : iiiIi1II1III ( iiOOooooO0Oo )
elif iiiii1II == 30019 : OOooOooo0OOo0 ( iiOOooooO0Oo )
elif iiiii1II == 30017 : OOOoOOo0o ( iiOOooooO0Oo )
elif iiiii1II == 30018 : OooOo ( iiOOooooO0Oo )
elif iiiii1II == 30030 : I1i1I1Iiiii1 ( )
elif iiiii1II == 30031 : O0Oo0 ( )
elif iiiii1II == 30032 : oOOOo00O00O ( )
elif iiiii1II == 30033 : O0Ooo0O ( )
elif iiiii1II == 30034 : iii1oOo0OoOOOo0 ( )
elif iiiii1II == 30035 : Ii1IIIII ( iiOOooooO0Oo )
elif iiiii1II == 30036 : iiiIIiiii11 ( iiOOooooO0Oo )
elif iiiii1II == 30037 : IIiI1iIIiI1I1i ( iiOOooooO0Oo )
elif iiiii1II == 30038 : IIII1iIIii ( )
elif iiiii1II == 30039 : Iii1IIII11I ( )
elif iiiii1II == 50000 : iIiIi11 ( )
elif iiiii1II == 50001 : iii11i1 ( )
elif iiiii1II == 50002 : i11OOoOOO ( iiOOooooO0Oo )
elif iiiii1II == 50003 : IiI ( o0O0Oo00 )
elif iiiii1II == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif iiiii1II == 60001 : iIiI1IIiii11 ( )
elif iiiii1II == 60002 : oO0O0Ooo ( iiI11ii1I1 )
elif iiiii1II == 60003 : o0o00oO0oo000 ( iiI11ii1I1 )
elif iiiii1II == 50004 : IiiiiI1i1Iii ( )
elif iiiii1II == 50005 : speedtest . runtest ( iiOOooooO0Oo )
elif iiiii1II == 70001 : oO0oI1I1 ( )
elif iiiii1II == 70002 : I1II ( iiOOooooO0Oo )
elif iiiii1II == 70003 : iIIi1Ii1III ( iiOOooooO0Oo )
elif iiiii1II == 70004 : Oooo00 ( iiOOooooO0Oo )
elif iiiii1II == 70005 : iii1II1iI1IIi ( iiOOooooO0Oo )
elif iiiii1II == 70006 : Ii11iiI1 ( )
elif iiiii1II == 50006 : iiIiI1i1 ( i1 , i1111 )
elif iiiii1II == 80000 : IioO0O ( )
elif iiiii1II == 80001 : resolvefilmon ( iiOOooooO0Oo )
elif iiiii1II == 80002 : Oo0oOo000OoO0 ( )
elif iiiii1II == 80003 : III1II1i ( iiI11ii1I1 , iiOOooooO0Oo )
elif iiiii1II == 80004 : oOo0Oo0O0O ( iiI11ii1I1 , iiOOooooO0Oo )
elif iiiii1II == 80005 : iiI11Iii ( )
elif iiiii1II == 80006 : i11I1 ( iiOOooooO0Oo )
elif iiiii1II == 80007 : iiiI111I ( iiOOooooO0Oo )
elif iiiii1II == 80008 : oooOOO00o0 ( )
elif iiiii1II == 80009 : O0o00ooo ( )
elif iiiii1II == 80010 : iiiIIiiiI ( iiOOooooO0Oo )
elif iiiii1II == 80011 : Ii11Iiii ( iiOOooooO0Oo )
elif iiiii1II == 80012 : o0OOoOooO0ooO ( )
elif iiiii1II == 90000 : ooO ( iiI11ii1I1 , iiOOooooO0Oo )
elif iiiii1II == 90001 : i11I1II1I11i ( )
elif iiiii1II == 90002 : iiIIi ( )
elif iiiii1II == 90003 : oOOoo ( iiOOooooO0Oo )
elif iiiii1II == 90004 : oo0O0 ( iiOOooooO0Oo )
elif iiiii1II == 90005 : Ii111Ii11 ( iiOOooooO0Oo )
elif iiiii1II == 90006 : IiiIiIIi ( iiOOooooO0Oo )
elif iiiii1II == 90007 : O00Oo ( iiOOooooO0Oo )
elif iiiii1II == 90008 : iI1i1iI1iI ( iiOOooooO0Oo )
elif iiiii1II == 90009 : OOOOoOoO ( iiOOooooO0Oo )
elif iiiii1II == 90010 : oO0O00oOOoooO ( )
elif iiiii1II == 90020 : o0000O00oO0O ( )
elif iiiii1II == 90021 : hellyeah2 ( iiOOooooO0Oo )
elif iiiii1II == 90022 : hellyeah3 ( iiOOooooO0Oo )
elif iiiii1II == 90023 : OooOOo0 ( )
elif iiiii1II == 90024 : oOIII111iiIi1 ( iiOOooooO0Oo )
elif iiiii1II == 90025 : Ii11Ii ( iiOOooooO0Oo )
if 41 - 41: iiII11i1I1IIi + oO0o . OooOO000
elif iiiii1II == 90030 : I1i1I11I ( )
elif iiiii1II == 90031 : i1I1IiiIi1i ( )
elif iiiii1II == 90032 : Ooo0OOoOoO0 ( iiOOooooO0Oo )
elif iiiii1II == 90033 : IIo0Oo0oO0oOO00 ( iiOOooooO0Oo )
elif iiiii1II == 90034 : II1i111Ii1i ( iiOOooooO0Oo )
elif iiiii1II == 90035 : ooO0oooOO0 ( iiOOooooO0Oo )
elif iiiii1II == 90036 : i1O00oo00o000o ( iiOOooooO0Oo )
elif iiiii1II == 90037 : Ii1I11ii1i ( iiOOooooO0Oo )
elif iiiii1II == 90038 : Ii1I11I ( )
if 73 - 73: Ii * oOo0O0Ooo + I11i / oo0oO00
if 56 - 56: ooOoO0O00
elif iiiii1II == 100001 : Stand_up ( )
if 11 - 11: Ii % I11i / iiII11i1I1IIi * ii
elif iiiii1II == 100003 : iii1I1i ( iiOOooooO0Oo )
elif iiiii1II == 100004 : ooo000ooO0000 ( iiOOooooO0Oo )
elif iiiii1II == 100005 : Resolve ( iiOOooooO0Oo )
elif iiiii1II == 100008 : Search ( )
elif iiiii1II == 100007 : IiI11iI1i1i1i ( iiOOooooO0Oo )
elif iiiii1II == 100009 : yt . PlayVideo ( iiOOooooO0Oo )
elif iiiii1II == 100010 : i1iiIiI1Ii1i ( iiOOooooO0Oo )
elif iiiii1II == 100100 : oO0OO0 ( ooI1i , iiOOooooO0Oo , iiiiI1iiIi1i )
elif iiiii1II == 100101 : i11i1iiI1i ( iiOOooooO0Oo , iiI11ii1I1 , iiii111II , iiiiI1iiIi1i , ooI1i )
elif iiiii1II == 100102 : I1iIiI11I1 ( iiI11ii1I1 , iiOOooooO0Oo , ooI1i , iiii111II )
elif iiiii1II == 100106 : iI11I ( iiOOooooO0Oo , iiI11ii1I1 )
elif iiiii1II == 100107 : OO0oo ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
