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
IiiIII111iI = "3.3.2"
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
def i11i1 ( ) :
 if 42 - 42: Ii * iI11I1II1I1I / Ii1I . Ii % iiII11i1I1IIi
 if 41 - 41: OOoOoo / o0o00Oo0O
 if 51 - 51: iiII11i1I1IIi % oOo0O0Ooo
 if 60 - 60: oOo0O0Ooo / IIi . oOo0O0Ooo / O00OOo00oo0o . OOoOoo
 if 92 - 92: OOooOOo + O00OOo00oo0o * iIi1i1ii1 % oOo0O0Ooo
 i1Oo00 = O000oo ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( i1Oo00 )
 if len ( IIIII11I1IiI ) > 0 :
  for iiI11ii1I1 , iiOOooooO0Oo , i1I1i1 , O0OoooO0 in IIIII11I1IiI :
   I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 50005 , i1I1i1 , O0OoooO0 , '' )
def ooo0O0o00O ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + II + ']WIPE GENIE[/COLOR]' , '[COLOR' + II + ']Genie BUILDS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Wizard[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   I1i11 ( )
  if iI1i11iII111 == 1 :
   IiIi1I1 ( )
  if iI1i11iII111 == 2 :
   IiIIi1 ( IIIIiii1IIii )
  if iI1i11iII111 == 3 :
   II1i11I ( iiOOooooO0Oo )
 else :
  I1IIII1i ( '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 10060 , oOOOo00O00oOo + 'BackupMyBuild.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , str ( ooOO0O0ooOooO ) , 49 , oOOOo00O00oOo + 'RestoreMyBuild.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']WIPE GENIE[/COLOR]' , str ( ooOO0O0ooOooO ) , 41 , oOOOo00O00oOo + 'WipeGenie.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']WISHES PC[/COLOR]' , str ( ooOO0O0ooOooO ) , 1 , oOOOo00O00oOo + 'WISHESPC.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Genie BUILDS[/COLOR]' , str ( ooOO0O0ooOooO ) , 44 , oOOOo00O00oOo + 'GenieBuilds.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 50 - 50: ii % iiII11i1I1IIi
def IIii1111 ( ) :
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
   if 42 - 42: iiII11i1I1IIi / I11i . oo0oO00 + oo0oO00 % OOooOOo + Ii
   if 56 - 56: I11i
  I1IIII1i ( '[COLOR' + II + ']24/7 STREAMS[/COLOR]' , '' , 30030 , oOOOo00O00oOo + '247Streams.png' , O0o0Oo , '' )
  if 28 - 28: OooOO000 . OooOO000 % iI11I1II1I1I * iI11I1II1I1I . I11i / OooOO000
  if 27 - 27: oO0o + IIiIi1iI - ooOoO0O00
  if 69 - 69: OOoOoo - o0o00Oo0O % Ii1I + Ii . OOooOOo / oO0o
  if 79 - 79: o0o00Oo0O * Ii - OOoOoo / OOoOoo
  if 48 - 48: o0o00Oo0O
  if 93 - 93: Ii - oOo0O0Ooo * Ii1I * iiII11i1I1IIi % o0o00Oo0O + ii
  if 25 - 25: OOoOoo + iIi1i1ii1 / IIiIi1iI . I11i % o0o00Oo0O * oO0o
  if 84 - 84: IIiIi1iI % iIi1i1ii1 + Ii
  I1IIII1i ( '[COLOR' + II + ']FreeView[/COLOR]' , str ( ooOO0O0ooOooO ) , 90023 , oOOOo00O00oOo + 'freeview.png' , O0o0Oo , '' )
  if 28 - 28: I1ii11iIi11i + oO0o * IIi % oo0oO00 . iiII11i1I1IIi % o0o00Oo0O
  if 16 - 16: iiII11i1I1IIi - iI11I1II1I1I / oOo0O0Ooo . IIiIiII11i + iI11I1II1I1I
  if 19 - 19: oO0o - I1ii11iIi11i . o0o00Oo0O
  if 60 - 60: IIiIiII11i + I1ii11iIi11i
  if 9 - 9: IIiIi1iI * ii - iI11I1II1I1I + OOooOOo / oO0o . oO0o
  if 49 - 49: IIiIiII11i
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def Iiii1iI1i ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']MOVIES[/COLOR]' , '[COLOR' + II + ']TV SHOWS[/COLOR]' , '[COLOR' + II + ']FOOTBALL[/COLOR]' , '[COLOR' + II + ']KIDS[/COLOR]' , '[COLOR' + II + ']NEWS[/COLOR]' , '[COLOR' + II + ']GenieTv TUTORIALS[/COLOR]' , '[COLOR' + II + ']HOBBIES[/COLOR]' , '[COLOR' + II + ']STAND UP[/COLOR]' , '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , '[COLOR' + II + ']Dont Blame Us Tv[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']CATEGORIES[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  I1ii1ii11i1I ( )
 if iI1i11iII111 == 1 :
  o0OoOO ( )
 if iI1i11iII111 == 2 :
  O0O0Oo00 ( )
 if iI1i11iII111 == 3 :
  oOoO00o ( )
 if iI1i11iII111 == 4 :
  oO00O0 ( )
 if iI1i11iII111 == 5 :
  IIi1IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) ) , O00Ooo , iiI11ii1I1 )
 if iI1i11iII111 == 6 :
  OOOO0OOO ( )
 if iI1i11iII111 == 7 :
  i1i1ii ( )
 if iI1i11iII111 == 8 :
  iII1ii1 ( )
 if iI1i11iII111 == 9 :
  I1i1iiiI1 ( )
 if iI1i11iII111 == 10 :
  iIIi ( )
  if 62 - 62: I1ii11iIi11i - iiII11i1I1IIi
  if 21 - 21: o0o00Oo0O % OOoOoo . oOo0O0Ooo / IIiIiII11i + OOoOoo
def ii1Ii11I ( ) :
 if not os . path . exists ( IIIII ) :
  iiIiI1i1 ( 'Change Log 27/11/16 - v3.3.1' , 'NEW SECTIONS ADDED, BAMFtv (FREE IPTV), ROADRUNNER and Technica Streams, QUICKSILVER music section has a major revamp, REAPER section back with force, Download option added, Search series fixed, Watch series under maintenance but back up(STILL), Scooby streams back up and running' )
  os . makedirs ( IIIII )
  if 53 - 53: oo0oO00 - oOo0O0Ooo - oo0oO00 * OooOO000
  if 71 - 71: o0o00Oo0O - iI11I1II1I1I
def I1ii1ii11i1I ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   i1II ( )
  if iI1i11iII111 == 1 :
   iI1I ( iiOOooooO0Oo )
  if iI1i11iII111 == 2 :
   OooOoOo ( )
  if iI1i11iII111 == 3 :
   III1I1Iii1iiI ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if iI1i11iII111 == 4 :
   i1Iii11I1i ( )
 else :
  I1IIII1i ( '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9001 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']POPCORN BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 7061 , oOOOo00O00oOo + 'PopcornBox.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Desi Flix[/COLOR]' , '' , 80005 , oOOOo00O00oOo + 'Desi.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , oOOOo00O00oOo + 'FilmTrailers.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOOo00O00oOo + 'ClassicMovies.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def Oo00o0OO0O00o ( ) :
 IIiiiI1iIII ( )
 O0Oooo ( )
 if 21 - 21: I1ii11iIi11i
 if 29 - 29: iiII11i1I1IIi / IIiIiII11i / IIiIi1iI * IIi
 I1IIII1i ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  I1I11i ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
 I1I11i ( '[COLOR' + II + ']Link GTV to Guide[/COLOR]' , '' , 4010 , oOOOo00O00oOo + 'linkchannels.png' , O0o0Oo , '' )
def iIIi ( ) :
 I1IIII1i ( '[COLOR' + II + ']DAILY LISTS[/COLOR]' , '' , 9007 , Oo00OOOOO , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Oo00OOOOO , O0o0Oo , '' )
 if 10 - 10: O00OOo00oo0o % OOoOoo * OOoOoo . iiII11i1I1IIi / iIi1i1ii1 % IIi
 if 49 - 49: oO0o / oo0oO00 + o0o00Oo0O * I11i
 if 28 - 28: IIiIi1iI + Ii / iiII11i1I1IIi % OOooOOo % I1ii11iIi11i - o0o00Oo0O
 if 54 - 54: ooOoO0O00 + IIiIiII11i
 if 83 - 83: Ii1I - oOo0O0Ooo + IIi
def o0OoOO ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   iIi1Ii1i1iI ( )
  if iI1i11iII111 == 1 :
   IIiI1 ( )
  if iI1i11iII111 == 2 :
   i1iI1 ( )
  if iI1i11iII111 == 3 :
   ii1I1IiiI1ii1i ( )
  if iI1i11iII111 == 4 :
   O0o ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1IIII1i ( '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9002 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '' , 10040 , oOOOo00O00oOo + 'WatchSeries.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '' , 8020 , oOOOo00O00oOo + 'iWatchSeries.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']CLASSIC TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 8064 , oOOOo00O00oOo + 'ClassicTV.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , oOOOo00O00oOo + 'TVShowTrailers.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def oO0OoO00o ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   II1iiiiII = '[COLOR' + II + ']SILENT HUNTER[/COLOR]'
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   O0OoOO0oo0 = '[COLOR' + II + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   oOO = '[COLOR' + II + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   O0o0OO0000ooo = '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   iIIII1iIIii = '[COLOR' + II + ']APPRENTICE[/COLOR]'
  OooOoOO0 = [ II1iiiiII , O0OoOO0oo0 , oOO , '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , iIIII1iIIii , '[COLOR' + II + ']RAIZ TV[/COLOR]' , O0o0OO0000ooo , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   oOOO00o000o ( ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvL2pkaC9ob21lLnR4dA==' ) ) )
  if iI1i11iII111 == 1 :
   oOOO00o000o ( ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvbWFpbm1lbnUucGhw' ) ) )
  if iI1i11iII111 == 2 :
   iIi11i1 ( )
  if iI1i11iII111 == 3 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , O00Ooo , iiI11ii1I1 )
  if iI1i11iII111 == 4 :
   oO00oo0o00o0o ( )
  if iI1i11iII111 == 5 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , O00Ooo , iiI11ii1I1 )
  if iI1i11iII111 == 6 :
   IiIIIIIi ( )
  if iI1i11iII111 == 7 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , O00Ooo , iiI11ii1I1 )
  if iI1i11iII111 == 8 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9tYWluLnBocA==' ) ) , O00Ooo , iiI11ii1I1 )
 else :
  if oo00 . getSetting ( 'Silent Hunter' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']THE REAPER[/COLOR]' , ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvbWFpbm1lbnUucGhw' ) ) , 90037 , oOOOo00O00oOo + 'TheReaper.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']PANDORAS BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 10025 , oOOOo00O00oOo + 'PandorasBox.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'DojoStreams.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'Roadrunner-Streams.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'Technica-Streams.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , '' , 1017 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'raiztv.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , str ( ooOO0O0ooOooO ) , 1023 , oOOOo00O00oOo + 'ScoobyStreams.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']ITV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'ITVStreams.png' , O0o0Oo , '' )
  if 11 - 11: ooOoO0O00 % Ii - ooOoO0O00 * OOooOOo
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 39 - 39: O00OOo00oo0o
def O0OoO0ooOO0o ( ) :
 IIiiiI1iIII ( )
 I1I11i ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
def OoOo0oOooOoOO ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 url = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( OoO000O0Oo )
 for o00oOoOo0 , o0O0O0ooo0oOO in IIIII11I1IiI :
  if '[DIR]' in o00oOoOo0 :
   oo000ii ( ( '[COLOR' + II + ']' + o0O0O0ooo0oOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + o0O0O0ooo0oOO , 1018 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'mkv' in o0O0O0ooo0oOO :
   OoO ( ( '[COLOR' + II + ']' + o0O0O0ooo0oOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + o0O0O0ooo0oOO , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'avi' in o0O0O0ooo0oOO :
   OoO ( ( '[COLOR' + II + ']' + o0O0O0ooo0oOO + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + o0O0O0ooo0oOO , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
   if 41 - 41: ooOoO0O00 * IIiIiII11i / ii . IIi
def oO00oo0o00o0o ( ) :
 I1IIII1i ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , oOOOo00O00oOo + 'scraped.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 if 83 - 83: OooOO000 . o0o00Oo0O / I1ii11iIi11i / IIi - IIiIiII11i
def oO0oO0 ( url ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( I1 )
 for iiI11ii1I1 , url , Ii11iiI , IIi1iiii1iI , O0OoooO0 , iIiiii in IIIII11I1IiI :
  if IIi1iiii1iI == '123' :
   IIi1iiii1iI = oOOOo00O00oOo + 'appstreams.png'
  if O0OoooO0 == '123' :
   O0OoooO0 = oOOOo00O00oOo + 'appstreams.png'
  if 'php' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100010 , IIi1iiii1iI , O0OoooO0 , iIiiii )
  elif 'playlist' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100007 , IIi1iiii1iI , O0OoooO0 , iIiiii )
  elif 'watchseries' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100100 , IIi1iiii1iI , O0OoooO0 , iIiiii )
  elif not 'http' in url :
   O0000OOO0 ( iiI11ii1I1 , url , 100009 , IIi1iiii1iI , O0OoooO0 , iIiiii , '' )
  else :
   O0000OOO0 ( iiI11ii1I1 , url , 100005 , IIi1iiii1iI , O0OoooO0 , iIiiii , '' )
   if 51 - 51: oOo0O0Ooo / OOoOoo / iIi1i1ii1
def I111iIi1 ( url ) :
 I1 = i1i1IIIIi1i ( url )
 oo00O00oO000o = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for url , oOo0OOoO0 , iIiiii , O0OoooO0 , iiI11ii1I1 in oo00O00oO000o :
  if oOo0OOoO0 == '123' :
   oOo0OOoO0 = oOOOo00O00oOo + 'appstreams.png'
  if O0OoooO0 == '123' :
   O0OoooO0 = O0o0Oo
  if 'php' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100004 , oOo0OOoO0 , O0OoooO0 , iIiiii )
  elif 'playlist' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100007 , oOo0OOoO0 , O0OoooO0 , iIiiii )
  elif 'watchseries' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100100 , oOo0OOoO0 , O0OoooO0 , iIiiii )
  elif not 'http' in url :
   O0000OOO0 ( iiI11ii1I1 , url , 100009 , oOo0OOoO0 , O0OoooO0 , iIiiii , '' )
  else :
   O0000OOO0 ( iiI11ii1I1 , url , 100005 , oOo0OOoO0 , O0OoooO0 , iIiiii , '' )
   if 71 - 71: Ii1I - IIiIi1iI / OOooOOo * OOooOOo / ooOoO0O00 . ooOoO0O00
def ooo000ooO0000 ( url ) :
 if 97 - 97: I1ii11iIi11i * oOo0O0Ooo . iI11I1II1I1I
 I1 = i1i1IIIIi1i ( url )
 I1Ii1111iIi = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( I1 )
 for I11o0oO00oO0o0o0 in I1Ii1111iIi :
  IIi1iiii1iI = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for IIi1iiii1iI in IIi1iiii1iI :
   IIi1iiii1iI = IIi1iiii1iI
  iiI11ii1I1 = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for iiI11ii1I1 in iiI11ii1I1 :
   if 'elete' in iiI11ii1I1 :
    pass
   elif 'rivate Vid' in iiI11ii1I1 :
    pass
   else :
    iiI11ii1I1 = ( iiI11ii1I1 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  I1I = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for I1I in I1I :
   I1I = I1I
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for url in url :
   url = url
  O0000OOO0 ( '[COLORred]' + str ( I1I ) + '[/COLOR] : ' + str ( iiI11ii1I1 ) , str ( url ) , 100009 , str ( IIi1iiii1iI ) , O0o0Oo , '' , '' )
  i1Oo0oO00o ( 'movies' , '' )
  if 89 - 89: ooOoO0O00 / IIiIiII11i . iI11I1II1I1I
  if 1 - 1: IIiIi1iI % OOooOOo * I1ii11iIi11i
  if 55 - 55: OOooOOo
  if 87 - 87: ii % OooOO000 . oOo0O0Ooo / IIiIi1iI
  if 8 - 8: iiII11i1I1IIi + I11i
def oOOo0o0oo ( iconimage , url , extra ) :
 IIi1iiii1iI = ' '
 i11iiiiI1i = ' '
 O0OoooO0 = ' '
 iIIii = ' '
 i1iIiIi1I = i1i1IIIIi1i ( url )
 IIi1iiii1iI = re . compile ( '<img src="(.+?)">' ) . findall ( i1iIiIi1I )
 for IIi1iiii1iI in IIi1iiii1iI :
  IIi1iiii1iI = IIi1iiii1iI
 iiii11i = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( i1iIiIi1I )
 for O0OoooO0 in iiii11i :
  O0OoooO0 = O0OoooO0
 IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( i1iIiIi1I )
 for url , iIIii in IIIII11I1IiI :
  iIIii = 'S' + ( iIIii ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = I11i1I1I + url
  III11II1I1Ii1 ( ( iIIii ) . replace ( '  ' , '' ) , url , 100101 , IIi1iiii1iI , O0OoooO0 , i11iiiiI1i , '' )
  i1Oo0oO00o ( 'Movies' , 'info' )
  if 72 - 72: OooOO000 * oo0oO00 % iIi1i1ii1 . ii
def OoO0O0O0o00 ( url , name , fanart , extra , iconimage ) :
 iiiI11 = extra
 iIIii = name
 i1iIiIi1I = i1i1IIIIi1i ( url )
 IIi1iiii1iI = iconimage
 IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( i1iIiIi1I )
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
 for iiOOooooO0Oo , name in IIIII11I1IiI :
  for oOOOoo00 in oO0Oo :
   if oOOOoo00 in iiOOooooO0Oo :
    URL = 'http://www.watchseriesgo.to/link/' + iiOOooooO0Oo
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
 I1II1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  OoOo00o0OO ( url , oOoOOo000oOoO0 )
 for url in i1I :
  OoOo00o0OO ( url , oOoOOo000oOoO0 )
 for url in I1II1 :
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
 for Ooo0oo , iiI11ii1I1 in IIIII11I1IiI :
  IIi11IIiIii1 ( Ooo0oo , season_name )
  if 17 - 17: iIi1i1ii1 + oo0oO00 . oO0o - I1ii11iIi11i * Ii
  if 20 - 20: oOo0O0Ooo . ii % IIi
def I1i11ii11 ( url , season_name ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for Ooo0oo , iiI11ii1I1 in IIIII11I1IiI :
  IIi11IIiIii1 ( Ooo0oo , season_name )
  if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
def OO00O0oOO ( url , season_name ) :
 I1 = i1i1IIIIi1i ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I1 )
 for Ooo0oo , iiI11ii1I1 in IIIII11I1IiI :
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
 iii1I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOOOooO0oO00O0o = True
 ooOO00oOOo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO00oOOo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO00oOOo000 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIii11II11II1 = [ ]
  if 10 - 10: oOo0O0Ooo / I1ii11iIi11i % Ii1I * IIiIi1iI
  if showcontext == 'fav' :
   IIii11II11II1 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIii11II11II1 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooOO00oOOo000 . addContextMenuItems ( IIii11II11II1 )
 OOOOooO0oO00O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1I1i , listitem = ooOO00oOOo000 , isFolder = True )
 return OOOOooO0oO00O0o
 if 6 - 6: OooOO000 . OOoOoo * OOooOOo . ooOoO0O00
 if 98 - 98: ooOoO0O00
def O0000OOO0 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 iii1I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOOOooO0oO00O0o = True
 ooOO00oOOo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO00oOOo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO00oOOo000 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIii11II11II1 = [ ]
  IIii11II11II1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIii11II11II1 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIii11II11II1 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooOO00oOOo000 . addContextMenuItems ( IIii11II11II1 )
 OOOOooO0oO00O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1I1i , listitem = ooOO00oOOo000 , isFolder = False )
 return OOOOooO0oO00O0o
 if 65 - 65: OOooOOo / oO0o % OOoOoo
def iIiIIii ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 61 - 61: I11i / IIi / I1ii11iIi11i * o0o00Oo0O
def iIII1i1i ( url ) :
 IiI1iii11iIi1 = xbmc . Player ( i1iI11I1II1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : IiI1iii11iIi1 . play ( url ) . strip ( )
 except : pass
 if 14 - 14: Ii - OooOO000 * OOooOOo
def O0iIi1IiII ( url ) :
 IiI1iii11iIi1 = xbmc . Player ( )
 import urlresolver
 try : IiI1iii11iIi1 . play ( url )
 except : pass
 if 51 - 51: Ii1I / iI11I1II1I1I % oo0oO00 + I11i * IIiIi1iI + O00OOo00oo0o
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
  if 77 - 77: IIiIi1iI * OOooOOo
  if 14 - 14: iiII11i1I1IIi % iiII11i1I1IIi / OOoOoo
  if 72 - 72: ooOoO0O00 - IIiIiII11i - IIi + IIi * I11i * IIi
def oOoO00o ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   iII1I1 ( )
  if iI1i11iII111 == 1 :
   o0Ooo0o0ooo0 ( )
  if iI1i11iII111 == 2 :
   oo0o0000Oo0 ( )
  if iI1i11iII111 == 3 :
   o0O00oOoo ( )
  if iI1i11iII111 == 4 :
   O000O0OO00oo ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def OOOO0OOO ( ) :
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
 if 69 - 69: I11i / I1ii11iIi11i
 if 43 - 43: Ii1I . oOo0O0Ooo / ii % ii
 if 33 - 33: O00OOo00oo0o
def OO ( ) :
 I1 = O000oo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiooOOoooooo in IIIII11I1IiI :
  IIiooOOoooooo = ( str ( IIiooOOoooooo ) )
  if os . path . exists ( xbmc . translatePath ( IIiooOOoooooo ) ) :
   OOO0ooo = ( IIiooOOoooooo ) . replace ( 'special://home/addons/' , '' )
   iiIiI1i1 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + OOO0ooo + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iI1i11iII111 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iI1i11iII111 == 0 :
    IIiiii ( IIiooOOoooooo )
    oOOo0O00o ( )
   elif iI1i11iII111 == 1 :
    iI111i1I1II ( IIiooOOoooooo )
  else :
   pass
   if 96 - 96: O00OOo00oo0o / I1ii11iIi11i * IIiIiII11i - OooOO000 * I1ii11iIi11i
def iI111i1I1II ( addon ) :
 OOO0ooo = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 81 - 81: OOoOoo . I11i / O00OOo00oo0o
def IIiiii ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 Iii111Ii = os . path . join ( I11II1i , 'default.py' )
 O0O00oOooo0OO = open ( Iii111Ii , "w+" )
 if 23 - 23: oo0oO00 + oO0o
 O0O00oOooo0OO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 O0O00oOooo0OO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 O0O00oOooo0OO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 2 - 2: oo0oO00 - iIi1i1ii1 - iiII11i1I1IIi - O00OOo00oo0o . iI11I1II1I1I
 if 79 - 79: iIi1i1ii1 . oO0o
 if 40 - 40: I11i + I1ii11iIi11i . I11i % IIiIi1iI
 if 15 - 15: iIi1i1ii1 * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
def oOOO00o000o ( url ) :
 I1 = O000oo ( url )
 Oo00OOOOoo0oo = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 I1II1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 oo00OO0000oO = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 O00OOooo0Ooo = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url , i1I1i1 , O0OoooO0 , iIiiii in Oo00OOOOoo0oo :
  if 'php' in url :
   I1IIII1i ( iiI11ii1I1 , url , 90037 , i1I1i1 , O0OoooO0 , iIiiii )
  elif iiI11ii1I1 == 'Search' :
   I1IIII1i ( 'Search' , url , 90038 , i1I1i1 , O0OoooO0 , iIiiii )
  else :
   I1I11i ( iiI11ii1I1 , url , 222 , i1I1i1 , O0OoooO0 , iIiiii )
 for iiI11ii1I1 , oOo0OOoO0 , url , o0oOOoOOO in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 90037 , oOo0OOoO0 , o0oOOoOOO , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , o0oOOoOOO in i1I :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , o0oOOoOOO , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , o0oOOoOOO in I1II1 :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , o0oOOoOOO , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , o0oOOoOOO in oo00OO0000oO :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , o0oOOoOOO , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 in O00OOooo0Ooo :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , '' , '' )
  i1Oo0oO00o ( 'movies' , 'MAIN' )
  if 32 - 32: ooOoO0O00 . iiII11i1I1IIi / oO0o
def o0OOoOoO00 ( ) :
 I1iii = [ 'serialsearch' , 'moviesearch' ]
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 if o00o == '' :
  pass
 else :
  for III11I in I1iii :
   Ii1I11I = I11 + III11I + '.php'
   i1iIiIi1I = O000oo ( Ii1I11I )
   if i1iIiIi1I != 'Opened' :
    oo00O00oO000o = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( i1iIiIi1I )
    for iiI11ii1I1 , iiOOooooO0Oo , i1I1i1 , O0OoooO0 , iIiiii in oo00O00oO000o :
     if o00o in iiI11ii1I1 . lower ( ) :
      iiIii1I = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( o00OO00OoO ) )
      for oOOOoo00 in iiIii1I :
       if oOOOoo00 == iiOOooooO0Oo :
        iiI11ii1I1 = '[COLORred]* [/COLOR]' + ( iiI11ii1I1 ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        i1I11iIiII = open ( oOOoo0Oo , "a" )
        i1I11iIiII . write ( 'item="' + iiI11ii1I1 + '"\n' )
        i1I11iIiII . close
      if 'php' in iiOOooooO0Oo :
       I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , 90037 , i1I1i1 , O0OoooO0 , iIiiii )
      else :
       I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 222 , i1I1i1 , O0OoooO0 , iIiiii )
       if 66 - 66: I1ii11iIi11i - I11i * OOoOoo + OOooOOo + I11i - iI11I1II1I1I
   i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
   if 17 - 17: oo0oO00
def i1ii11 ( ) :
 I1 = O000oo ( 'http://www.tvcatchup.com/channels/' )
 iii1i1iiiiIi = O000oo ( 'http://www.djing.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for ii1i , oOo0OOoO0 , iiOOooooO0Oo in IIIII11I1IiI :
  OoO ( ii1i , 'http://www.tvcatchup.com' + iiOOooooO0Oo , 90024 , 'http://www.tvcatchup.com' + oOo0OOoO0 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in i1I :
  if 'Submit' in iiI11ii1I1 :
   pass
  elif '&lt;' in iiI11ii1I1 :
   pass
  else :
   I1I11i ( 'DJing  ' + iiI11ii1I1 , iiOOooooO0Oo , 90025 , 'http://www.djing.com' + oOo0OOoO0 , O0o0Oo , '' )
  i1Oo0oO00o ( 'movies' , 'MAIN' )
def IIioo0OO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'var url = "([^"]*)";' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( url )
def IiiI11i1I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 80 - 80: IIi / iiII11i1I1IIi / OOooOOo + ooOoO0O00 - I1ii11iIi11i
def OooOoOo ( ) :
 oo000ii ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O000oo ( 'http://www.join4films.com/' )
 IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , iiOOooooO0Oo , 80006 , oOOOo00O00oOo + 'Desi.png' )
def iIIiiIIi1IiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( iiI11ii1I1 , url , 80007 , oOo0OOoO0 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def I11IIIiIi11 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  iii1 ( url )
def I11iiIi1i1 ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = 'http://www.join4films.com/?s=' + ( oOO0OO0O ) . replace ( ' ' , '+' ) + '&search_type=1'
 o00o = i1IiiI1iIi . lower ( )
 iIIiiIIi1IiI ( o00o )
 if 66 - 66: oO0o * I1ii11iIi11i
 if 28 - 28: oO0o % OOooOOo % Ii1I + oOo0O0Ooo / oOo0O0Ooo
 if 71 - 71: IIi * oO0o % ii % oO0o / oOo0O0Ooo
 if 56 - 56: ii % Ii * iI11I1II1I1I . oO0o * o0o00Oo0O
 if 23 - 23: Ii
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
def ii111Ii11iii ( ) :
 I1IIII1i ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 I1IIII1i ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 I1IIII1i ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 I1IIII1i ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 if 62 - 62: iI11I1II1I1I
def OO0OoOOO0 ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = 'http://imoviemax.se/?s=' + ( oOO0OO0O ) . replace ( ' ' , '+' )
 o00o = i1IiiI1iIi . lower ( )
 O00ooOo ( o00o )
def oOO0o00O ( url ) :
 oOoO = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , iiI11ii1I1 , IIII in IIIII11I1IiI :
  if iiI11ii1I1 in oOoO :
   pass
  else :
   I1IIII1i ( iiI11ii1I1 + ' - ' + IIII + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
   oOoO . append ( iiI11ii1I1 )
   if 50 - 50: I1ii11iIi11i % OOoOoo
def iIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , iIIiooO00O00oOO in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 + ' - Views:' + iIIiooO00O00oOO , url , 10075 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
  if 40 - 40: OooOO000 . oo0oO00 + oOo0O0Ooo + Ii1I + O00OOo00oo0o
  if 26 - 26: iI11I1II1I1I
def O00ooOo ( url ) :
 OOOo = [ ]
 I1 = O000oo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  I1IIII1i ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 10075 , oOo0OOoO0 , oOo0OOoO0 , '' )
  OOOo . append ( iiI11ii1I1 )
  if 79 - 79: OOooOOo % OOoOoo % I1ii11iIi11i
def Ii1 ( img , name , url ) :
 img = img
 name = name
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for I1iiiiii , url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  o0OO0Oo = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + o0OO0Oo
  I11iiii1I = ( I1iiiiii ) . replace ( 'play-' , 'Server ' )
  I1I11i ( I11iiii1I , o0OO0Oo , 10076 , img , img , '' )
  if 3 - 3: o0o00Oo0O % ii / IIi
def ooOo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for o0O0O0ooo0oOO in IIIII11I1IiI :
  if '=m' in o0O0O0ooo0oOO :
   o0oO0OoO0 ( o0O0O0ooo0oOO )
  elif 'php' in o0O0O0ooo0oOO :
   ooOo ( url )
  else :
   I1 = O000oo ( o0O0O0ooo0oOO )
   IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for oOOOOOoOO in IIIII11I1IiI :
    o0oO0OoO0 ( o0O0O0ooo0oOO )
    if 81 - 81: IIiIiII11i + Ii / OooOO000
    if 85 - 85: Ii + O00OOo00oo0o * OOooOOo
    if 1 - 1: ooOoO0O00 / I1ii11iIi11i . oO0o
def o0Oii1111i ( url ) :
 I1 = O000oo ( url )
 O0ooOO = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for OOoO000 , IiiI in O0ooOO :
  print 'there ><><><><><><><><><><><><'
  OOoO000 = OOoO000
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IiiI ) )
  for iiI11ii1I1 , i11ii in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + OOoO000 + '[/COLOR] - ' + iiI11ii1I1 + ' - [COLOR' + II + ']' + i11ii + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
 I11o0oO00oO0o0o0 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for OOoO000 , i11I1 in I11o0oO00oO0o0o0 :
  print 'there ><><><><><><><><><><><><'
  OOoO000 = OOoO000
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( i11I1 ) )
  for iiI11ii1I1 , i11ii in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + OOoO000 + '[/COLOR] - ' + iiI11ii1I1 + ' - [COLOR' + II + ']' + i11ii + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
   if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + OooOO000 * iI11I1II1I1I % iIi1i1ii1
   if 25 - 25: iiII11i1I1IIi + OOooOOo . I11i % OOooOOo * IIi
   if 32 - 32: Ii - O00OOo00oo0o
def O0o ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
 for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
  iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for iiI11ii1I1 in iiI11ii1I1 :
   iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  IIi1iiii1iI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for IIi1iiii1iI in IIi1iiii1iI :
   IIi1iiii1iI = 'http:' + IIi1iiii1iI
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , '' , '' )
  if 53 - 53: ii - OOoOoo
  if 87 - 87: oo0oO00 . oOo0O0Ooo
  if 17 - 17: iIi1i1ii1 . Ii
  if 5 - 5: Ii1I + o0o00Oo0O + o0o00Oo0O . O00OOo00oo0o - IIiIi1iI
def III1I1Iii1iiI ( url ) :
 if 63 - 63: oo0oO00
 Oo0 = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for o0O0O0ooo0oOO , oOo0OOoO0 , iiI11ii1I1 , OOo0Oo0OOo0 in IIIII11I1IiI :
  iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O000oo ( o0O0O0ooo0oOO )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for i1ii , i11iiiiI1i in i1I :
   i1i11I = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( i11iiiiI1i ) )
   for iIiiii in i1i11I :
    if iiI11ii1I1 in Oo0 :
     pass
    else :
     I1I11i ( iiI11ii1I1 , i1ii , 8043 , oOo0OOoO0 , oOo0OOoO0 , iIiiii )
     i1Oo0oO00o ( 'movies' , 'INFO' )
     Oo0 . append ( iiI11ii1I1 )
     if 7 - 7: IIiIiII11i
     if 27 - 27: oo0oO00 . ii + Ii
def O0OO ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , O00Ooo , iIiiii , O0OoooO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 10065 , O00Ooo , O0OoooO0 , iIiiii )
 i1Oo0oO00o ( 'movies' , 'INFO' )
 if 39 - 39: Ii1I + oOo0O0Ooo - iI11I1II1I1I - I11i
def I1i ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = 'https://www.youtube.com/results?search_query=' + ( oOO0OO0O ) . replace ( ' ' , '+' )
 o00o = i1IiiI1iIi . lower ( )
 I1 = O000oo ( o00o )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for iiOOooooO0Oo in next :
  iiOOooooO0Oo = 'https://www.youtube.com' + iiOOooooO0Oo
  I1IIII1i ( '[COLOR' + II + '] NEXT [/COLOR]' , iiOOooooO0Oo , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 , i1II1iII , i11iiiiI1i in IIIII11I1IiI :
  oOoOooOo0o0 . append ( iiI11ii1I1 )
  i1Oo0oO00o ( 'tvshows' , 'INFO' )
  IIi1iiii1iI = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IIi1iiii1iI
  iiOOooooO0Oo = 'http://www.youtube.com' + iiOOooooO0Oo
  I1I11i ( '[COLORred]' + i1II1iII + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , IIi1iiii1iI , i11iiiiI1i )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 , i1II1iII in IIIII11I1IiI :
   print 'im doing it'
   i1Oo0oO00o ( 'tvshows' , 'INFO' )
   IIi1iiii1iI = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
   iiOOooooO0Oo = 'http://www.youtube.com' + iiOOooooO0Oo
   if '&' in iiOOooooO0Oo :
    print ' i got here'
    I1 = O000oo ( iiOOooooO0Oo )
    I11o0oO00oO0o0o0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
     iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for iiI11ii1I1 in iiI11ii1I1 :
      iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     iiOOooooO0Oo = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for iiOOooooO0Oo in iiOOooooO0Oo :
      iiOOooooO0Oo = 'https://www.youtube.com/w' + iiOOooooO0Oo
     IIi1iiii1iI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for IIi1iiii1iI in IIi1iiii1iI :
      IIi1iiii1iI = 'http:' + IIi1iiii1iI
     I1I11i ( '[COLORred]' + i1II1iII + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , O0o0Oo , '' )
   elif iiI11ii1I1 in oOoOooOo0o0 :
    pass
   elif 'user' in iiOOooooO0Oo or 'elete' in iiI11ii1I1 :
    pass
   elif 'hannel' in iiOOooooO0Oo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iiOOooooO0Oo
    I1 = O000oo ( iiOOooooO0Oo )
    II1i = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 in II1i :
     if 'outube' in iiOOooooO0Oo or 'list' in iiOOooooO0Oo :
      pass
     elif 'atch' in iiOOooooO0Oo :
      iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '/watch?v=' , '' )
      I1I11i ( '[COLORred]' + i1II1iII + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0OOoO0 , 'http:' + oOo0OOoO0 , '' )
     else :
      pass
   else :
    I1I11i ( '[COLORred]' + i1II1iII + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , IIi1iiii1iI , '' )
    if 81 - 81: Ii1I
def o00ooo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IIII1i ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for oOo0OOoO0 , url , iiI11ii1I1 , i1II1iII , i11iiiiI1i in IIIII11I1IiI :
  oOoOooOo0o0 . append ( iiI11ii1I1 )
  i1Oo0oO00o ( 'tvshows' , 'INFO' )
  IIi1iiii1iI = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + IIi1iiii1iI
  url = 'http://www.youtube.com' + url
  I1I11i ( '[COLORred]' + i1II1iII + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , IIi1iiii1iI , i11iiiiI1i )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for oOo0OOoO0 , url , iiI11ii1I1 , i1II1iII in IIIII11I1IiI :
   i1Oo0oO00o ( 'tvshows' , 'INFO' )
   IIi1iiii1iI = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    I1 = O000oo ( url )
    I11o0oO00oO0o0o0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
    for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
     iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for iiI11ii1I1 in iiI11ii1I1 :
      iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     IIi1iiii1iI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for IIi1iiii1iI in IIi1iiii1iI :
      IIi1iiii1iI = 'http:' + IIi1iiii1iI
     I1I11i ( '[COLORred]' + i1II1iII + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , O0o0Oo , '' )
   elif iiI11ii1I1 in oOoOooOo0o0 :
    pass
   elif 'user' in url or 'elete' in iiI11ii1I1 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O000oo ( url )
    II1i = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for oOo0OOoO0 , url , iiI11ii1I1 in II1i :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      I1I11i ( '[COLORred]' + i1II1iII + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0OOoO0 , 'http:' + oOo0OOoO0 , '' )
     else :
      pass
   else :
    I1I11i ( '[COLORred]' + i1II1iII + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI , IIi1iiii1iI , '' )
    if 31 - 31: o0o00Oo0O * I11i % I11i / oo0oO00 / iiII11i1I1IIi / oO0o
    if 11 - 11: OOooOOo + OOoOoo - ii / oO0o
def O0Oooo ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  iIIi1iI1I1IIi = open ( IIIii1II1II )
  IIIII11I1IiI = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( iIIi1iI1I1IIi ) )
  for O0OO0 , O0ooo0o0 in IIIII11I1IiI :
   if O0OO0 == 'needs replacing' or O0ooo0o0 == 'needs replacing' :
    oO0ooOoO ( )
    if 59 - 59: o0o00Oo0O % I1ii11iIi11i
  I1IIII1i ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if 92 - 92: iIi1i1ii1 % OooOO000 / Ii1I % Ii1I * oOo0O0Ooo
def Oo ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOOO + ")" )
 oO0ooOoO ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 78 - 78: oO0o % OOoOoo * ooOoO0O00
def O0iI ( ) :
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
 if 15 - 15: o0o00Oo0O / I1ii11iIi11i % Ii1I + I11i
def iiiIiI ( name ) :
 IiiIIIiI1ii = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , oOo0OOoO0 , oo0OOoOoo0O0O , iiOOooooO0Oo in IIIII11I1IiI :
  if IiiIIIiI1ii == 'Full List' :
   iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '.ts' , '.m3u8' )
   I1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiOOooooO0Oo ) . strip ( ) , 10012 , oOo0OOoO0 , oOo0OOoO0 , '' )
  else :
   IiiIIIiI1ii = ( IiiIIIiI1ii ) . replace ( 'World' , 'القنوات العربية' )
   if IiiIIIiI1ii in oo0OOoOoo0O0O :
    iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '.ts' , '.m3u8' )
    print iiOOooooO0Oo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    I1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiOOooooO0Oo ) . strip ( ) , 10012 , oOo0OOoO0 , oOo0OOoO0 , '' )
   else :
    pass
    if 15 - 15: OooOO000
def i1ii1111i1i ( name ) :
 IiiIIIiI1ii = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , oOo0OOoO0 , iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '.ts' , '.m3u8' )
  I1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiOOooooO0Oo ) . strip ( ) , 10012 , oOo0OOoO0 , oOo0OOoO0 , '' )
 else :
  I1I11i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 46 - 46: ooOoO0O00
  if 54 - 54: IIiIiII11i - OOooOOo
  if 73 - 73: IIi
  if 2 - 2: Ii - IIiIiII11i / oo0oO00 % o0o00Oo0O
  if 66 - 66: I1ii11iIi11i
  if 28 - 28: OOoOoo - OOoOoo . ooOoO0O00 - IIiIi1iI + oOo0O0Ooo . OOoOoo
  if 54 - 54: OOooOOo - O00OOo00oo0o
  if 3 - 3: oOo0O0Ooo - I1ii11iIi11i
  if 16 - 16: oo0oO00 + IIiIi1iI / I11i
  if 82 - 82: OOoOoo * Ii % IIiIiII11i - ii
  if 90 - 90: I1ii11iIi11i . oo0oO00 * ooOoO0O00 - ooOoO0O00
  if 16 - 16: oOo0O0Ooo * ooOoO0O00 - I11i . OOoOoo % iiII11i1I1IIi / I11i
def I1i11 ( ) :
 I1IIII1i ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  I1IIII1i ( 'Backup Genie Favourites' , iiOOooooO0Oo , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( O0Oo000ooO00 ) :
  I1IIII1i ( 'Backup Ivue Config' , O0Oo000ooO00 , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( oO0 ) :
  I1IIII1i ( 'Backup Kodi Favourites' , oO0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 14 - 14: iI11I1II1I1I * O00OOo00oo0o * Ii1I / iI11I1II1I1I * OOoOoo / iiII11i1I1IIi
  if 77 - 77: oO0o + O00OOo00oo0o + O00OOo00oo0o * iIi1i1ii1 / ii . iIi1i1ii1
  if 62 - 62: ooOoO0O00 - ooOoO0O00
zip = oo00 . getSetting ( 'zip' )
oOOO0O0Ooo = xbmc . translatePath ( os . path . join ( zip ) )
def IiI1i111IiIiIi1 ( ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 39 - 39: iiII11i1I1IIi - Ii1I
  if 53 - 53: I11i % OooOO000 + IIiIi1iI . I1ii11iIi11i - Ii1I % I11i
  if 64 - 64: IIiIiII11i
def iIIIiIi1I1i ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Ii1iIiII1ii1
  elif 'Ivue' in name :
   url = O0Oo000ooO00
  elif 'Kodi' in name :
   url = oO0
  IiI1i111IiIiIi1 ( )
  OoOOoO0oOo = open ( url ) . read ( )
  O0ooOOOO0O0 = os . path . join ( oOOO0O0Ooo , description . split ( 'Your ' ) [ 1 ] )
  OOoO = open ( O0ooOOOO0O0 , mode = 'w' )
  OOoO . write ( OoOOoO0oOo )
  OOoO . close ( )
 else :
  if 'guisettings.xml' in description :
   i1IIi1i1Ii1 = open ( os . path . join ( oOOO0O0Ooo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   Iii = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIIII11I1IiI = re . compile ( Iii ) . findall ( i1IIi1i1Ii1 )
   for type , o0Oo0oO , iI in IIIII11I1IiI :
    iI = iI . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , o0Oo0oO , iI ) )
  else :
   O0ooOOOO0O0 = os . path . join ( url )
   OoOOoO0oOo = open ( os . path . join ( oOOO0O0Ooo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOoO = open ( O0ooOOOO0O0 , mode = 'w' )
   OOoO . write ( OoOOoO0oOo )
   OOoO . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 25 - 25: Ii1I - Ii % IIi . Ii
 if 86 - 86: IIiIiII11i * Ii * ii + oo0oO00 % IIi
 if 60 - 60: OOooOOo / O00OOo00oo0o - IIiIiII11i . I1ii11iIi11i + o0o00Oo0O
 if 43 - 43: iI11I1II1I1I / IIiIiII11i % I11i - IIi
def oO0O000oOo ( ) :
 OoOOOO = 1
 IiI1i111IiIiIi1 ( )
 I1iiIi111I = xbmc . translatePath ( os . path . join ( oOOO0O0Ooo , 'Build Backup' , 'Full Backup' , '' ) )
 Iiii1iIii = xbmc . translatePath ( os . path . join ( oOOO0O0Ooo , 'Build Backup' , 'my_full_backup.zip' ) )
 oOoooO000O = xbmc . translatePath ( os . path . join ( oOOO0O0Ooo , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( I1iiIi111I ) :
  os . makedirs ( I1iiIi111I )
 III1I11i1iIi = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not III1I11i1iIi ) : return False , 0
 OO0oo0O0OOO0 = III1I11i1iIi
 OoOOo = xbmc . translatePath ( os . path . join ( I1iiIi111I , OO0oo0O0OOO0 + '.zip' ) )
 Iii1 = [ 'plugin.video.GenieTv' ]
 OoOOo00 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 O00 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 O0OO0OOo = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OOo0o = "Creating full backup of existing build"
 iIiii = "Creating Community Build"
 IiIii1ii = "Archiving..."
 IIiI1i = ""
 iII1 = "Please Wait"
 O000O ( Oo0o0000o0o0 , OoOOo , iIiii , IiIii1ii , IIiI1i , iII1 , O00 , O0OO0OOo )
 time . sleep ( 1 )
 Oo00OO0 = xbmc . translatePath ( os . path . join ( I1iiIi111I , OO0oo0O0OOO0 + '_guisettings.zip' ) )
 oo0O = zipfile . ZipFile ( Oo00OO0 , mode = 'w' )
 try :
  oo0O . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oo0O . close ( )
 if OoOOOO == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + Iiii1iIii , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + OoOOo + '[/COLOR]' )
  if 92 - 92: IIi % OOoOoo % OOooOOo
def O000O ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 iIi1Ii = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 IiI1IIIII1I = len ( sourcefile )
 I1I1IiIi1 = [ ]
 oOO0o0oo0 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for oOo000O , iII , ooO0o0O0Oo in os . walk ( sourcefile ) :
  for file in ooO0o0O0Oo :
   oOO0o0oo0 . append ( file )
 IiiIIi = len ( oOO0o0oo0 )
 for oOo000O , iII , ooO0o0O0Oo in os . walk ( sourcefile ) :
  iII [ : ] = [ O00o0O for O00o0O in iII if O00o0O not in exclude_dirs ]
  ooO0o0O0Oo [ : ] = [ OOoO for OOoO in ooO0o0O0Oo if OOoO not in exclude_files ]
  for file in ooO0o0O0Oo :
   I1I1IiIi1 . append ( file )
   iIIIiI = len ( I1I1IiIi1 ) / float ( IiiIIi ) * 100
   o0oOoO00o . update ( int ( iIIIiI ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   O00i1 = os . path . join ( oOo000O , file )
   if not 'temp' in iII :
    if not 'plugin.program.originwizard' in iII :
     import time
     iiIII1IIiIIII = '01/01/1980'
     I1iIIII1 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( O00i1 ) ) )
     if I1iIIII1 > iiIII1IIiIIII :
      iIi1Ii . write ( O00i1 , O00i1 [ IiI1IIIII1I : ] )
 iIi1Ii . close ( )
 o0oOoO00o . close ( )
 if 57 - 57: OOooOOo . iI11I1II1I1I % IIiIi1iI % iIi1i1ii1 * OOooOOo
 if 8 - 8: OOooOOo . IIiIi1iI % oo0oO00 . oOo0O0Ooo % oOo0O0Ooo . iIi1i1ii1
def IiIIIIIi ( ) :
 IIiiiI1iIII ( )
 I1IIII1i ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 if 47 - 47: iiII11i1I1IIi + IIiIi1iI + IIiIiII11i % Ii
 if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / OooOO000 * oo0oO00
def i1iii1ii ( ) :
 IIiiiI1iIII ( )
 OooOoOO0 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  i1II ( )
 if iI1i11iII111 == 1 :
  iIi1Ii1i1iI ( )
 if iI1i11iII111 == 2 :
  iII1I1 ( )
 if iI1i11iII111 == 3 :
  I1i ( )
  if 18 - 18: oO0o . IIiIiII11i % OOooOOo % iIi1i1ii1
  if 87 - 87: iI11I1II1I1I . ii * OOooOOo
  if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % iIi1i1ii1 - iI11I1II1I1I
  if 17 - 17: iiII11i1I1IIi / I11i % I1ii11iIi11i
  if 71 - 71: OOoOoo . O00OOo00oo0o . oO0o
  if 68 - 68: Ii % oo0oO00 * oO0o * OOoOoo * IIiIiII11i + o0o00Oo0O
  if 66 - 66: iiII11i1I1IIi % Ii1I % ii
  if 34 - 34: I11i / OooOO000 % o0o00Oo0O . oO0o . ooOoO0O00
  if 29 - 29: o0o00Oo0O . O00OOo00oo0o
def OO0o0oO0O000o ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , O00Ooo , iiI11ii1I1 )
  if iI1i11iII111 == 1 :
   oOOO00o000o ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if iI1i11iII111 == 2 :
   I1iI11iii ( )
  if iI1i11iII111 == 3 :
   oo0oO ( )
  if iI1i11iII111 == 4 :
   IiIi1iI11 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if iI1i11iII111 == 5 :
   iiI1iI1I ( )
  if iI1i11iII111 == 6 :
   III1II111Ii1 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if iI1i11iII111 == 7 :
   o0O0OO0o ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if iI1i11iII111 == 8 :
   OOOoOo ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if iI1i11iII111 == 9 :
   OOoO0oo0O ( )
  if iI1i11iII111 == 10 :
   iiI1I1ii ( )
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
  if 79 - 79: iI11I1II1I1I
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 81 - 81: IIi + iI11I1II1I1I * O00OOo00oo0o - iI11I1II1I1I . IIi
def I1ii ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   oO0oI1I1 ( )
  if iI1i11iII111 == 1 :
   i11i1 ( )
  if iI1i11iII111 == 2 :
   iIiIi11 ( )
  if iI1i11iII111 == 3 :
   o00o0 ( iiOOooooO0Oo )
  if iI1i11iII111 == 4 :
   O0Oo0 ( iiOOooooO0Oo )
  if iI1i11iII111 == 5 :
   oOOo0O00o ( )
  if iI1i11iII111 == 6 :
   OOooO0OO0 ( url = 'http://www.iplocation.net/' , inc = 1 )
  if iI1i11iII111 == 7 :
   iI1iIiiiI1I1 ( )
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
  if 78 - 78: oo0oO00 / oO0o - oo0oO00 * ii . OOooOOo
  if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 37 - 37: ooOoO0O00 - IIi % ii / IIi % IIiIi1iI
 if 48 - 48: Ii % oo0oO00
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
 if 29 - 29: OooOO000 + Ii % iiII11i1I1IIi
 if 93 - 93: OOooOOo % iI11I1II1I1I
def Ooo0o0oo0 ( ) :
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
 if 87 - 87: OOooOOo / OOoOoo + iI11I1II1I1I
def IiIi1I1 ( ) :
 IIiiiI1iIII ( )
 I1I11i ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , O0o0Oo , '' )
 I1I11i ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 93 - 93: iI11I1II1I1I + oo0oO00 % IIiIi1iI
def iii1IiI1I1 ( ) :
 IIiiiI1iIII ( )
 I1I11i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , O0o0Oo , '' )
 I1I11i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , O0o0Oo , '' )
 I1I11i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , O0o0Oo , '' )
 I1I11i ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , O0o0Oo , '' )
 if 64 - 64: IIiIi1iI / o0o00Oo0O * OOooOOo * IIiIi1iI
 if 60 - 60: iiII11i1I1IIi / ooOoO0O00 % Ii1I / Ii1I * Ii1I . Ii
 if 99 - 99: OOooOOo
def oO0o0 ( ) :
 IIiiiI1iIII ( )
 OooOoOO0 = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  oO00OoOo ( )
 if iI1i11iII111 == 0 :
  OoOi111i ( iiOOooooO0Oo )
 if iI1i11iII111 == 0 :
  II1III1i1iiI ( iiOOooooO0Oo )
  if 27 - 27: iIi1i1ii1 - o0o00Oo0O % iiII11i1I1IIi * O00OOo00oo0o . OOoOoo % iI11I1II1I1I
  if 37 - 37: ii + o0o00Oo0O - ooOoO0O00 % IIiIi1iI
  if 24 - 24: OOooOOo
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + IIi
def iIIi11 ( ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1Oo00 )
 for oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , oOo0OOoO0 , oOo0OOoO0 , '' )
 i1Oo0oO00o ( 'tvshows' , 'INFO' )
 if 54 - 54: iIi1i1ii1 - O00OOo00oo0o
def O0ii1ii1I1IIi1 ( url ) :
 i1Oo00 = O000oo ( oOOoo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 24 - 24: oO0o - oo0oO00 + Ii1I / OooOO000 % oOo0O0Ooo + iI11I1II1I1I
def oO00OoOo ( ) :
 IIiiiI1iIII ( )
 I1IIII1i ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 79 - 79: OOooOOo / IIiIi1iI
def oOo00o ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OOoooooooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 4 - 4: I1ii11iIi11i + I11i
def iIIiIii11i1Ii ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OoO0O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 14 - 14: oO0o / oO0o * o0o00Oo0O . oo0oO00
def oooOO0oOooO00 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iIIiI11i1I11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 29 - 29: oO0o * iI11I1II1I1I * o0o00Oo0O - OOooOOo / OOoOoo
def o0oO0OO00ooOO ( url ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 5 - 5: oOo0O0Ooo * OOooOOo - Ii . IIiIi1iI / OooOO000
def OoOi111i ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + III1iii1i1II ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 40 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 87 - 87: IIi + I11i . OooOO000 - ii
def iiiiI1IiI1I1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iI111i11iI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 2 - 2: OOooOOo + O00OOo00oo0o + ii . ooOoO0O00
def Iii1IIII11I ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  I1III1iIi ( )
 if iI1i11iII111 == 1 :
  OoO00O0 ( )
 if iI1i11iII111 == 2 :
  I1Iii ( )
  if 14 - 14: IIi
  if 79 - 79: iIi1i1ii1
  if 76 - 76: iI11I1II1I1I
  if 80 - 80: iI11I1II1I1I . o0o00Oo0O / iIi1i1ii1 % iIi1i1ii1
def OoO00O0 ( ) :
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , ooOo000OoO0o in IIIII11I1IiI :
  oo000ii ( 'Android Apps' + ooOo000OoO0o , 'https://www.apkfiles.com' + iiOOooooO0Oo , 30035 , oOOOo00O00oOo + 'apps.png' )
 for iiOOooooO0Oo , ooOo000OoO0o in i1I :
  oo000ii ( 'Android Games' + ooOo000OoO0o , 'https://www.apkfiles.com' + iiOOooooO0Oo , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def ooooo0O0 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '/cat' in url :
   oo000ii ( ( iiI11ii1I1 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def i1III1iI ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '/app' in url :
   oo000ii ( ( iiI11ii1I1 ) . replace ( '&amp;' , ' - ' ) , ( i11 ( 'aHR0cDovL2Fway5rb3BsYXllci5jb20=' ) ) + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def ii1ii1IiiiiIi1I ( url ) :
 OoO000O0Oo = O000oo ( url )
 ooo0O0o0OoOO = url
 if "page=" in str ( url ) :
  ooo0O0o0OoOO = url . split ( '?' ) [ 0 ]
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'apk' in url :
   I1I11i ( ( iiI11ii1I1 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + oOo0OOoO0 )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 I1I11i ( 'Next Page' , ooo0O0o0OoOO + str ( i1I ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def iIi11i ( name , url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 name = name
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  o0o00o0Oo ( name , url , 'Brackets' )
def I1Iii ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = 'https://www.apkfiles.com/search?q=' + ( oOO0OO0O ) . replace ( ' ' , '+' ) + '&search_type=1'
 o00o = i1IiiI1iIi . lower ( )
 ii1ii1IiiiiIi1I ( o00o )
 if 79 - 79: OOooOOo + oO0o - IIiIiII11i + iIi1i1ii1
def iIiiii1 ( url ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( ooOoo000oO , 'Download' ) )
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
 if 50 - 50: OOoOoo + I11i
def o0OoOOo ( url ) :
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
 if 56 - 56: iiII11i1I1IIi / iI11I1II1I1I + OOooOOo % IIi . IIi - Ii1I
 if 48 - 48: I1ii11iIi11i - IIiIi1iI + I1ii11iIi11i - oOo0O0Ooo * Ii . OooOO000
def I1iIIIiI ( name , url , description ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , name )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 OoiI1I1 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print OoiI1I1
 print '======================================='
 extract . all ( ii1 , OoiI1I1 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 27 - 27: IIiIi1iI - I1ii11iIi11i + OooOO000 - IIi . oOo0O0Ooo
 if 51 - 51: oo0oO00 + oO0o + OooOO000 + OooOO000 % I11i
 if 29 - 29: IIiIi1iI
 if 41 - 41: o0o00Oo0O % OooOO000
 if 10 - 10: OooOO000 . ooOoO0O00 + iIi1i1ii1
def I1III1iIi ( ) :
 i1Oo00 = O000oo ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , iiOOooooO0Oo , i1I1i1 , O0OoooO0 , oOOoOOO0oo0 in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 80003 , i1I1i1 , oOOOo00O00oOo + 'APKToolsB.png' , oOOoOOO0oo0 )
def O00O ( apk , ret = None ) :
 if apk == "kodi" :
  O0OOOOOoo = "https://kodi.tv/download/"
  i1Oo00 = O000oo ( O0OOOOOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1Oo00 )
  if len ( IIIII11I1IiI ) == 1 :
   oo0ooO0 = IIIII11I1IiI [ 0 ] [ 0 ]
   OO0oo0O0OOO0 = IIIII11I1IiI [ 0 ] [ 1 ]
   oOooo0OOO = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( oo0ooO0 , OO0oo0O0OOO0 )
  if ret == 'version' : return oo0ooO0
  else : return oOooo0OOO
 elif apk == "spmc" :
  ooo = 'https://github.com/koying/SPMC/releases/latest/'
  i1Oo00 = O000oo ( ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1Oo00 )
  oo0ooO0 = re . sub ( '<[^<]+?>' , '' , IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  oOooo0OOO = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( oo0ooO0 , oo0ooO0 )
  if ret == 'version' : return oo0ooO0
  else : return oOooo0OOO
def o0o00o0Oo ( name , url , Brackets ) :
 if Ii1I1I1i1Ii ( ) == 'android' :
  O00OII1 = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not O00OII1 : oOo00oII111i1ii1iII ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  ooo0OoO = name
  if O00OII1 :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not IIIIiII1i ( url ) == True : oOo00oII111i1ii1iII ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % ooo0OoO , '' , 'Please Wait' )
   ii1 = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( ii1 )
   except : pass
   downloader . download ( url , ii1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    oo0O = zipfile . ZipFile ( ii1 )
    for file in oo0O . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as OOoO :
       iiI1111I11i1I = file . split ( '/' ) [ 1 ]
       OOoO . write ( oo0O . read ( file ) )
       xbmc . sleep ( 500 )
       OOoO . close ( )
       try :
        os . remove ( ii1 )
       except :
        pass
       ii1 = os . path . join ( i1iiIII111ii , iiI1111I11i1I )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ii1 + '")' )
  else : oOo00oII111i1ii1iII ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oOo00oII111i1ii1iII ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 85 - 85: IIi * ooOoO0O00 % oOo0O0Ooo - IIiIi1iI
 if 37 - 37: OOoOoo . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
 if 83 - 83: OOoOoo / O00OOo00oo0o
 if 64 - 64: oO0o % OOoOoo . O00OOo00oo0o % oO0o + iiII11i1I1IIi * OOoOoo
def OOOO00OooO ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1Oo00 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iiOOooooO0Oo = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + iiOOooooO0Oo )
  OOOiI1 ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , iiOOooooO0Oo )
  if 84 - 84: IIi * oOo0O0Ooo % iiII11i1I1IIi + IIi / OooOO000
def OOOiI1 ( name , url ) :
 if Ii1I1I1i1Ii ( ) == 'android' :
  O00OII1 = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not O00OII1 : oOo00oII111i1ii1iII ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  ooo0OoO = name
  if O00OII1 :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not IIIIiII1i ( url ) == True : oOo00oII111i1ii1iII ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % ooo0OoO , '' , 'Please Wait' )
   ii1 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( ii1 )
   except : pass
   downloader . download ( url , ii1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ii1 + '")' )
  else : oOo00oII111i1ii1iII ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oOo00oII111i1ii1iII ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 80 - 80: ii + OOoOoo
 if 95 - 95: O00OOo00oo0o / oo0oO00 * O00OOo00oo0o - ii * ii % oO0o
def iI1 ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'INFO' )
 if 12 - 12: O00OOo00oo0o + IIi + iiII11i1I1IIi . OOoOoo / iIi1i1ii1
 if 29 - 29: OOoOoo . IIiIi1iI - IIiIiII11i
def II1i11I ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 30015 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 68 - 68: iI11I1II1I1I + IIiIiII11i / oo0oO00
def oOooo00000 ( url , iconimage , fanart ) :
 i1Oo00 = O000oo ( url )
 o0OO0Oo = url
 oOo0OOoO0 = iconimage
 fanart = fanart
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for o0O0O0ooo0oOO , iiI11ii1I1 in IIIII11I1IiI :
  if '.mp4' in iiI11ii1I1 :
   I1I11i ( 'Watch VIDEO' , url + '/' + o0O0O0ooo0oOO , 222 , oOo0OOoO0 , fanart , '' )
  if 'description' in iiI11ii1I1 :
   I1I11i ( 'Read Description' , url + '/' + o0O0O0ooo0oOO , 30017 , oOo0OOoO0 , fanart , '' )
  if 'images' in iiI11ii1I1 :
   I1IIII1i ( 'View Images' , url + '/' + o0O0O0ooo0oOO , 30018 , oOo0OOoO0 , fanart , '' )
  if 'url' in iiI11ii1I1 :
   I1I11i ( 'Install Build On Android' , url + '/' + o0O0O0ooo0oOO , 30016 , oOo0OOoO0 , fanart , '' )
  if 'url' in iiI11ii1I1 :
   I1I11i ( 'Install Build On Pc' , url + '/' + o0O0O0ooo0oOO , 30019 , oOo0OOoO0 , fanart , '' )
 i1Oo0oO00o ( 'movies' , 'INFO' )
 if 26 - 26: o0o00Oo0O
def i111I1iiIiII ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  OoO00ooO ( url )
  if 15 - 15: Ii
def I11i1I1ii1i1 ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  oO0ooooo0O00 ( url )
  if 5 - 5: OOooOOo % OooOO000 + OOoOoo
def iiiIi1II1III ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1Oo00 )
 for I1i11II11i in IIIII11I1IiI :
  iiIiI1i1 ( 'Description:' , I1i11II11i )
  if 9 - 9: OOooOOo - Ii1I * IIiIi1iI . IIiIi1iI - oOo0O0Ooo
def OOooOooo0OOo0 ( url ) :
 i1Oo00 = O000oo ( url )
 url = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for o0O0O0ooo0oOO , iiI11ii1I1 in IIIII11I1IiI :
  if 'png' in iiI11ii1I1 :
   I1I11i ( 'image' , '' , '' , url + '/' + o0O0O0ooo0oOO , url + '/' + o0O0O0ooo0oOO , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 87 - 87: OOoOoo
def I1IiI ( name , url , description ) :
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
 if 44 - 44: IIi / IIi . I11i % OOoOoo + OOooOOo
 if 57 - 57: OooOO000 % oO0o - oO0o
def oO0ooooo0O00 ( url ) :
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
 oO0oI1I1 ( )
 if 5 - 5: ooOoO0O00 + ii % OOooOOo
def OoO00ooO ( url ) :
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
 oO0oI1I1 ( )
 if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . O00OOo00oo0o
def Ooooo ( name , url , description ) :
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
 oO0oI1I1 ( )
 if 43 - 43: IIi
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
  ooOoO = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  OOoO . write ( ooOoO . rstrip ( '\r\n' ) + '\n' )
def oO0oI1I1 ( ) :
 iI1i11iII111 = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iI1i11iII111 == 0 : return
 elif iI1i11iII111 == 1 : pass
 ii1iII = Ii1I1I1i1Ii ( )
 OOO ( "Platform: " + str ( ii1iII ) )
 os . _exit ( 1 )
 OOO ( "Force close failed!  Trying alternate methods." )
 if ii1iII == 'osx' :
  OOO ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif ii1iII == 'linux' :
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
 elif ii1iII == 'android' :
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
 elif ii1iII == 'windows' :
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
  if 68 - 68: IIiIi1iI / ii * iiII11i1I1IIi / oo0oO00
  if 88 - 88: I11i
  if 1 - 1: ii
def II1III1i1iiI ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for I1III1I11Iii , iII , ooO0o0O0Oo in os . walk ( url ) :
  for file in ooO0o0O0Oo :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    i1IIi1i1Ii1 = open ( ( os . path . join ( I1III1I11Iii , file ) ) ) . read ( )
    i1oOOO0ooOO = i1IIi1i1Ii1 . replace ( Oo0o0000o0o0 , 'special://home/' )
    OOoO = open ( ( os . path . join ( I1III1I11Iii , file ) ) , mode = 'w' )
    OOoO . write ( str ( i1oOOO0ooOO ) )
    OOoO . close ( )
 oO0oI1I1 ( )
 if 3 - 3: ii
def I1iI11iii ( ) :
 oo000ii ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 oo000ii ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 oo000ii ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 71 - 71: OOoOoo + ooOoO0O00 - OooOO000 - Ii . iiII11i1I1IIi - IIiIi1iI
def OOoOOOO00 ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def IIii1III ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def ooooOoo0OO ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1I :
  oo000ii ( ( '[COLOR' + II + ']Filter - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']Stream - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oOo0OOoO0 )
def Oo0O0000Oo00o ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( url )
def II1 ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O
 iio00 = 'https://www.radionomy.com/en/search/index?query=' + ( oOO0OO0O ) . replace ( ' ' , '+' )
 I1 = O000oo ( iio00 )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']Stream - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + iiOOooooO0Oo , 70005 , oOo0OOoO0 )
  if 4 - 4: oO0o
  if 62 - 62: ooOoO0O00
def iiI1iI1I ( ) :
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , 'http://www.listenlive.eu/' + iiOOooooO0Oo , 10111113 , oOOOo00O00oOo + 'radio.png' )
def IiIi1iI11 ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  OoO ( iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 26 - 26: Ii + IIiIiII11i * ii
def O00OO0ooO0 ( ) :
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.toonjet.com/' + iiOOooooO0Oo , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoOooOO0oOOo0O ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
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
   oo000ii ( ( oOo0OOoO0 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOOo00O00oOo + 'vod.png' )
 for url in i1I :
  oo000ii ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOOo00O00oOo + 'Next.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1II ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 9 - 9: I1ii11iIi11i % ii - iIi1i1ii1
  if 43 - 43: oO0o % oO0o
def iiI1I1ii ( ) :
 IIiii11ii1i ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 IIiii11ii1i ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 7 - 7: oo0oO00 - o0o00Oo0O * iiII11i1I1IIi - I11i - IIiIiII11i
def Ii11iiI1 ( ) :
 IIiii11ii1i ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 IIiii11ii1i ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 IIiii11ii1i ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 71 - 71: I11i / IIi % IIi
def OoooO0 ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for iiI11ii1I1 , iiOOooooO0Oo , oooOO0oo0Oo00 in IIIII11I1IiI :
  if 'Parent' in iiI11ii1I1 :
   pass
  elif '2' in oooOO0oo0Oo00 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 99 - 99: o0o00Oo0O
def IiIii1 ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for iiI11ii1I1 , iiOOooooO0Oo , oooOO0oo0Oo00 in IIIII11I1IiI :
  if oOO0OO0O in iiI11ii1I1 . lower ( ) :
   if '1' in oooOO0oo0Oo00 :
    IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in oooOO0oo0Oo00 :
    IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in oooOO0oo0Oo00 :
    IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 46 - 46: IIiIi1iI % OOoOoo - I11i - I1ii11iIi11i - iIi1i1ii1 / iiII11i1I1IIi
    if 68 - 68: ooOoO0O00 - Ii1I / I1ii11iIi11i % iiII11i1I1IIi . OooOO000
def iIIIIIIIiIII ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for iiI11ii1I1 , iiOOooooO0Oo , oooOO0oo0Oo00 in IIIII11I1IiI :
  if '1' in oooOO0oo0Oo00 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in oooOO0oo0Oo00 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in oooOO0oo0Oo00 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 94 - 94: OooOO000 * iI11I1II1I1I . iiII11i1I1IIi
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 13 - 13: iI11I1II1I1I * OOooOOo / O00OOo00oo0o % IIiIi1iI + oo0oO00
def iiiI1iI1 ( url ) :
 o0O0O0ooo0oOO = url
 I1 = O000oo ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
 for url , iiI11ii1I1 in i1I :
  if 'mp3' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in iiI11ii1I1 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0O0O0ooo0oOO + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 15 - 15: OOoOoo . ooOoO0O00 * OOooOOo % iI11I1II1I1I
   if 35 - 35: Ii1I + O00OOo00oo0o - OOooOOo % oo0oO00 % I11i % OOooOOo
   if 45 - 45: oOo0O0Ooo * IIi % oO0o
def i111I11I ( url ) :
 I1 = O000oo ( url )
 o0O0O0ooo0oOO = url
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
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0O0O0ooo0oOO + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , o0O0O0ooo0oOO + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 80 - 80: iI11I1II1I1I - ii - Ii1I - Ii1I . ii
   if 48 - 48: O00OOo00oo0o . Ii / ooOoO0O00 % OOoOoo % OooOO000 + oo0oO00
def iiII1iiiiiii ( ) :
 IIiii11ii1i ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 IIiii11ii1i ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 IIiii11ii1i ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 9 - 9: ii + oo0oO00
def iIiI1ii ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 in IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iiOOooooO0Oo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oOo0OOoO0 :
   pass
  else :
   IIiii11ii1i ( oOo0OOoO0 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iiOOooooO0Oo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oOo0OOoO0 + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 76 - 76: iIi1i1ii1 + iI11I1II1I1I + OOooOOo . oO0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: OOoOoo / IIiIi1iI / IIi
 if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - IIiIi1iI
def III1IiI1i1i ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '</a>' in iiI11ii1I1 :
   pass
  elif '(' in iiI11ii1I1 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 94 - 94: OooOO000 - I1ii11iIi11i + oo0oO00
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 59 - 59: iiII11i1I1IIi . oOo0O0Ooo - iI11I1II1I1I + iI11I1II1I1I
def oO0o0Oo ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if oOO0OO0O in iiI11ii1I1 . lower ( ) :
   if '</a>' in iiI11ii1I1 :
    pass
   elif '(' in iiI11ii1I1 :
    IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 76 - 76: IIiIi1iI / OOooOOo + Ii1I
    if 2 - 2: Ii - O00OOo00oo0o + oO0o % iiII11i1I1IIi * iIi1i1ii1
def Ooo000O00 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if '</a>' in iiI11ii1I1 :
   pass
  elif '(' in iiI11ii1I1 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 36 - 36: IIi % Ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 47 - 47: ooOoO0O00 + IIiIiII11i . I1ii11iIi11i * oo0oO00 . iiII11i1I1IIi / ooOoO0O00
 if 50 - 50: O00OOo00oo0o / ooOoO0O00 % ii
def oOOOOO0Ooooo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  o0O0O0ooo0oOO = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( o0O0O0ooo0oOO )
  if 57 - 57: iIi1i1ii1 - ii
def OOoOO0O0o0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '<p align' in iiI11ii1I1 :
   pass
  elif '&nbsp;' in iiI11ii1I1 :
   pass
  else :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 44 - 44: IIi / I1ii11iIi11i + OOoOoo % IIiIiII11i / oO0o + Ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 20 - 20: Ii1I
 if 3 - 3: oO0o * ooOoO0O00 . oOo0O0Ooo . o0o00Oo0O - OOooOOo
def o0Ooo0o0ooo0 ( ) :
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
def OOoooOoO0 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 O0OOoooo0 = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , oOo0OOoO0 , oOo0OOoO0 , iiI11ii1I1 )
 for url , iiI11ii1I1 in O0OOoooo0 :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IIII1i ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def iIiIi1IiIi1iI ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 IiI1iii11iIi1 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 o00OO0 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 oooOo = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in o00OO0 :
  I1IIII1i ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , iiI11ii1I1 in IiI1iii11iIi1 :
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  I1IIII1i ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def oOoO0Oo0 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 7 - 7: IIiIi1iI + iIi1i1ii1
def o0O00oOoo ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if '9cart' in iiOOooooO0Oo :
   oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 32 - 32: iI11I1II1I1I % oOo0O0Ooo / Ii + IIi - I11i . OooOO000
def oo00I1IiI1IIiI ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( I1 )
 I1II1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if '9cart' in url :
   oo000ii ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   oo000ii ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url , iiI11ii1I1 in I1II1 :
  if '9cart' in url :
   oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 79 - 79: ooOoO0O00
def iIi1 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20003 , oOo0OOoO0 )
 for url , iiI11ii1I1 in i1I :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 96 - 96: ooOoO0O00 % ii
def ooiI1i ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'Watch' in url :
   oo000ii ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 3 - 3: OOoOoo / iiII11i1I1IIi
def Ii11 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 3 - 3: iIi1i1ii1 + O00OOo00oo0o . ooOoO0O00 / IIi % O00OOo00oo0o
def O0oo00oOOO0o ( url ) :
 url = cloudflare . source ( url )
 o0oO0OoO0 ( url )
 if 5 - 5: I11i / oOo0O0Ooo % iIi1i1ii1 . OOoOoo
def OooOOoO0OOOO ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in IIIII11I1IiI :
  o0oO0OoO0 ( url )
  if 33 - 33: iiII11i1I1IIi % IIiIiII11i + oO0o
  if 93 - 93: ooOoO0O00 . OOoOoo / oOo0O0Ooo + OOoOoo
def oo0o0000Oo0 ( ) :
 if 58 - 58: Ii1I + o0o00Oo0O . I1ii11iIi11i + OOooOOo - oO0o - OOooOOo
 I1IIII1i ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 41 - 41: I1ii11iIi11i / ooOoO0O00 / I1ii11iIi11i - OooOO000 . I11i
def iII1I1 ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 65 - 65: o0o00Oo0O * Ii . ii / oOo0O0Ooo / OooOO000
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 69 - 69: IIiIi1iI % IIiIi1iI
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if oOO0OO0O in iiI11ii1I1 . lower ( ) :
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
    if 76 - 76: Ii * OooOO000 / oO0o % Ii1I + IIi
    if 48 - 48: iI11I1II1I1I % ooOoO0O00 + OOooOOo % I11i
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 79 - 79: OOooOOo % oOo0O0Ooo % iIi1i1ii1 / ooOoO0O00 % oO0o
def O000O0OO00oo ( url ) :
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
 if 56 - 56: iI11I1II1I1I - Ii * OooOO000
def o0O0Ooo ( url ) :
 OoO000O0Oo = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 in i1I :
  O0oO00oOOooO = oOo0OOoO0
 I1II1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1II1 :
  I1IIII1i ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10007 , O0oO00oOOooO )
  if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
  if 66 - 66: o0o00Oo0O
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 52 - 52: oO0o * ii
def Ii11iiIo0OO0oooo ( url , IMAGE ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  print iiI11ii1I1 + '     ' + url
  if 'easy' in url :
   I11II1i1 ( url )
   if 46 - 46: IIiIiII11i % OooOO000 - ooOoO0O00 / iiII11i1I1IIi * OOooOOo
   if 92 - 92: I1ii11iIi11i - O00OOo00oo0o
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 24 - 24: oo0oO00 / O00OOo00oo0o / iiII11i1I1IIi % OOooOOo / Ii1I * IIiIi1iI
def I11II1i1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( url )
  if 8 - 8: iIi1i1ii1
  if 33 - 33: I11i / o0o00Oo0O + IIi
  if 75 - 75: OOoOoo % Ii + iI11I1II1I1I
def i1i1ii ( ) :
 if 92 - 92: OOooOOo % o0o00Oo0O
 I1IIII1i ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , O0o0Oo , '' )
 if 55 - 55: iI11I1II1I1I * OooOO000
def ooIi11iI ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'elete' in iiI11ii1I1 :
   pass
  else :
   OoO ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 222 , oOo0OOoO0 )
   if 22 - 22: IIi
def I1I11Iiii111 ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iI1ii111iiIii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , oO0oiIiI , i1iII1IiiIiI1 in iI1ii111iiIii :
  for oOO0OO0O in oO0oiIiI :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iIIiiiI1iI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for iiOOooooO0Oo , iiI11ii1I1 in iIIiiiI1iI1 :
    if 'tube' in iiOOooooO0Oo :
     pass
    elif 'stage' in iiOOooooO0Oo :
     OoO ( '[COLOR' + II + ']' + oO0oiIiI + '   -   ' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0OOoO0 , )
    elif 'vee' in iiOOooooO0Oo :
     pass
     if 86 - 86: Ii1I * IIiIi1iI
def O0oO0o0OOOOOO ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iI1ii111iiIii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , oO0oiIiI , i1iII1IiiIiI1 in iI1ii111iiIii :
  iIIiiiI1iI1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for iiOOooooO0Oo , iiI11ii1I1 in iIIiiiI1iI1 :
   if 'tube' in iiOOooooO0Oo :
    pass
   elif 'stage' in iiOOooooO0Oo :
    OoO ( '[COLOR' + II + ']' + oO0oiIiI + '   -   ' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0OOoO0 )
   elif 'vee' in iiOOooooO0Oo :
    pass
    if 24 - 24: ooOoO0O00 * OOoOoo - iiII11i1I1IIi / iIi1i1ii1
    if 62 - 62: I1ii11iIi11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: ooOoO0O00
def iIi1i ( url ) :
 I1 = O000oo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 i1ii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( i1ii ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in i1ii :
  iii1 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 4 - 4: O00OOo00oo0o - oOo0O0Ooo % oo0oO00 / I11i % oo0oO00 * IIiIiII11i
  if 3 - 3: ooOoO0O00 / O00OOo00oo0o - ooOoO0O00 - iiII11i1I1IIi % I1ii11iIi11i - oOo0O0Ooo
  if 45 - 45: OOoOoo
  if 7 - 7: iI11I1II1I1I - ooOoO0O00
  if 10 - 10: O00OOo00oo0o % o0o00Oo0O / oOo0O0Ooo % iiII11i1I1IIi
  if 25 - 25: IIiIiII11i / oO0o
  if 64 - 64: o0o00Oo0O % IIiIi1iI
def iIi11i1 ( ) :
 if 40 - 40: I11i + iiII11i1I1IIi
 OoO000Oo0oO ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 OoO000Oo0oO ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 46 - 46: o0o00Oo0O - OOooOOo . ii
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 19 - 19: I11i
def o00OOOOOo0OOo ( ) :
 OoO000Oo0oO ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 OoO000Oo0oO ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 44 - 44: iiII11i1I1IIi * I11i
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def II11ii1I11 ( ) :
 if 65 - 65: IIi + IIiIiII11i
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 Oo0O0OO0OoO0 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' , 'top10action' , 'top10music' ]
 if 26 - 26: IIi * I1ii11iIi11i
 for III11I in Oo0O0OO0OoO0 :
  Ii1I11I = OOOO0OOoO0O0 + III11I + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( Ii1I11I )
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for iiOOooooO0Oo , O00Ooo , iIiiii , O0OoooO0 , iiI11ii1I1 in IIIII11I1IiI :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    i1iI1Ii11Ii1 ( iiI11ii1I1 , iiOOooooO0Oo , 222 , O00Ooo , O0OoooO0 , iIiiii )
    if 82 - 82: o0o00Oo0O
    i1Oo0oO00o ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 70 - 70: iiII11i1I1IIi - I1ii11iIi11i / ii % ii
    if 95 - 95: ii % ii . iIi1i1ii1
def III1ii ( ) :
 if 38 - 38: Ii1I + OOooOOo
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 Oo0O0OO0OoO0 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 68 - 68: o0o00Oo0O
 for III11I in Oo0O0OO0OoO0 :
  o0oOoO00 = OOOO0OOoO0O0 + III11I + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( o0oOoO00 )
  IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for iiI11ii1I1 , iIiiii , iiOOooooO0Oo , oOo0OOoO0 , O0OoooO0 , Ii11iiI in IIIII11I1IiI :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    OoO000Oo0oO ( iiI11ii1I1 , iiOOooooO0Oo , Ii11iiI , oOo0OOoO0 , O0OoooO0 , iIiiii )
    if 94 - 94: oO0o + OOoOoo + IIiIi1iI
    i1Oo0oO00o ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 82 - 82: I1ii11iIi11i - I1ii11iIi11i . iI11I1II1I1I / IIi + OOoOoo % iI11I1II1I1I
    if 61 - 61: IIi / I1ii11iIi11i % IIi - oO0o + IIiIi1iI / IIiIi1iI
def oo0oOO ( ) :
 if 41 - 41: oO0o . O00OOo00oo0o * OOoOoo * O00OOo00oo0o
 OoO000O0Oo = O000oo ( OOOO0OOoO0O0 + 'spongemain.php' )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iIiiii , iiOOooooO0Oo , oOo0OOoO0 , O0OoooO0 , Ii11iiI in IIIII11I1IiI :
  OoO000Oo0oO ( iiI11ii1I1 , iiOOooooO0Oo , Ii11iiI , oOo0OOoO0 , O0OoooO0 , iIiiii )
  i1Oo0oO00o ( 'movies' , 'MAIN' )
def ooOO ( url ) :
 if 86 - 86: iIi1i1ii1 . IIi / OOoOoo - ii
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iii1IiI1i = ( '%s%s' % ( OooO0ooO0o0 , url ) )
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , O00Ooo , iIiiii , iiii11i , iiI11ii1I1 in IIIII11I1IiI :
  iiIii1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
  for oOOOoo00 in iiIii1I :
   if oOOOoo00 == url :
    iiI11ii1I1 = ( '[COLORred]Watched - [/COLOR]' + iiI11ii1I1 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  i1iI1Ii11Ii1 ( iiI11ii1I1 , url , 222 , O00Ooo , iiii11i , iIiiii )
  if 88 - 88: oo0oO00 % I1ii11iIi11i - iiII11i1I1IIi % oo0oO00 + OOoOoo - OooOO000
  i1Oo0oO00o ( 'movies' , 'MAIN' )
  if 23 - 23: o0o00Oo0O
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 9 - 9: iiII11i1I1IIi * I1ii11iIi11i . IIiIi1iI * Ii - o0o00Oo0O
  if 54 - 54: oOo0O0Ooo * IIi + I11i % ooOoO0O00 - I11i + OOooOOo
def IIIIiI11Ii1i ( url ) :
 if 100 - 100: OooOO000 + iiII11i1I1IIi + IIiIi1iI + OooOO000 / ooOoO0O00
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iIiiii , url , oOo0OOoO0 , O0OoooO0 , Ii11iiI in IIIII11I1IiI :
  OoO000Oo0oO ( iiI11ii1I1 , url , Ii11iiI , oOo0OOoO0 , O0OoooO0 , iIiiii )
  if 74 - 74: o0o00Oo0O % ii * I1ii11iIi11i + IIi * OooOO000
  i1Oo0oO00o ( 'movies' , 'MAIN' )
  if 100 - 100: IIi + iIi1i1ii1 * I11i + IIiIiII11i
  if 70 - 70: I1ii11iIi11i * iI11I1II1I1I
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 76 - 76: OooOO000 % OOooOOo % iI11I1II1I1I . IIi
def i1iI1Ii11Ii1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 30 - 30: ooOoO0O00
 iii1I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOOOooO0oO00O0o = True
 ooOO00oOOo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO00oOOo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO00oOOo000 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIii11II11II1 = [ ]
  IIii11II11II1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIii11II11II1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIii11II11II1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooOO00oOOo000 . addContextMenuItems ( IIii11II11II1 )
 OOOOooO0oO00O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1I1i , listitem = ooOO00oOOo000 , isFolder = False )
 return OOOOooO0oO00O0o
 if 75 - 75: iiII11i1I1IIi . IIi - iI11I1II1I1I * oO0o * OooOO000
def OoO000Oo0oO ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 93 - 93: IIiIi1iI
 iii1I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOOOooO0oO00O0o = True
 ooOO00oOOo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO00oOOo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO00oOOo000 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIii11II11II1 = [ ]
  IIii11II11II1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIii11II11II1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIii11II11II1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooOO00oOOo000 . addContextMenuItems ( IIii11II11II1 )
 OOOOooO0oO00O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1I1i , listitem = ooOO00oOOo000 , isFolder = True )
 return OOOOooO0oO00O0o
if 18 - 18: IIiIi1iI
if 66 - 66: oo0oO00 * Ii + OOooOOo / IIi
if 96 - 96: IIi + IIi % OOoOoo % IIi
if 28 - 28: iI11I1II1I1I + OOooOOo . I11i % Ii
if 58 - 58: iiII11i1I1IIi / ii % oo0oO00 + oO0o
if 58 - 58: o0o00Oo0O
if 91 - 91: OooOO000 / Ii1I . OooOO000 - I11i + Ii1I
if 72 - 72: iIi1i1ii1 . OOoOoo * Ii1I / Ii1I / OooOO000
if 13 - 13: ooOoO0O00
if 17 - 17: Ii * I11i * I11i + oO0o
if 95 - 95: oOo0O0Ooo
if 95 - 95: IIi % Ii1I + I11i % IIiIi1iI
if 36 - 36: o0o00Oo0O / ooOoO0O00 % IIiIiII11i / OooOO000
if 96 - 96: I1ii11iIi11i / oo0oO00 . IIiIiII11i . I1ii11iIi11i
if 91 - 91: IIiIiII11i . IIi + I11i
def I1iII1IIi1IiI ( string ) :
 if OOO00O == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 8 - 8: iI11I1II1I1I
def oOOo0ooO0 ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 ii1i1II11II1i = [ ]
 try :
  if 95 - 95: iiII11i1I1IIi + I11i * Ii1I
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( OOOOi11i1 ) == False :
  I1iII1IIi1IiI ( 'Making Favorites File' )
  ii1i1II11II1i . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  i1IIi1i1Ii1 = open ( OOOOi11i1 , "w" )
  i1IIi1i1Ii1 . write ( json . dumps ( ii1i1II11II1i ) )
  i1IIi1i1Ii1 . close ( )
 else :
  I1iII1IIi1IiI ( 'Appending Favorites' )
  i1IIi1i1Ii1 = open ( OOOOi11i1 ) . read ( )
  ooO = json . loads ( i1IIi1i1Ii1 )
  ooO . append ( ( name , url , iconimage , fanart , mode ) )
  i1oOOO0ooOO = open ( OOOOi11i1 , "w" )
  i1oOOO0ooOO . write ( json . dumps ( ooO ) )
  i1oOOO0ooOO . close ( )
  if 16 - 16: I1ii11iIi11i
  if 74 - 74: iiII11i1I1IIi
def OO0oOoO000o0 ( ) :
 if os . path . exists ( OOOOi11i1 ) == False :
  ii1i1II11II1i = [ ]
  I1iII1IIi1IiI ( 'Making Favorites File' )
  ii1i1II11II1i . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  i1IIi1i1Ii1 = open ( OOOOi11i1 , "w" )
  i1IIi1i1Ii1 . write ( json . dumps ( ii1i1II11II1i ) )
  i1IIi1i1Ii1 . close ( )
 else :
  ooo00 = json . loads ( open ( OOOOi11i1 ) . read ( ) )
  iII11II1II = len ( ooo00 )
  for OOO00000o0 in ooo00 :
   iiI11ii1I1 = OOO00000o0 [ 0 ]
   iiOOooooO0Oo = OOO00000o0 [ 1 ]
   O00Ooo = OOO00000o0 [ 2 ]
   try :
    OOOO000Ooo0O = OOO00000o0 [ 3 ]
    if OOOO000Ooo0O == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     OOOO000Ooo0O = O00Ooo
    else :
     OOOO000Ooo0O = O0OoooO0
   try : oOo0oO = OOO00000o0 [ 5 ]
   except : oOo0oO = None
   try : ooo0O = OOO00000o0 [ 6 ]
   except : ooo0O = None
   if 22 - 22: oo0oO00 * OooOO000
   if OOO00000o0 [ 4 ] == 0 :
    I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , '' , O00Ooo , O0OoooO0 , '' , 'fav' )
   else :
    I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , OOO00000o0 [ 4 ] , O00Ooo , O0OoooO0 , '' , 'fav' )
    if 4 - 4: OOooOOo - oo0oO00 + oOo0O0Ooo
def iiIiIiIiiIiI ( name ) :
 ooO = json . loads ( open ( OOOOi11i1 ) . read ( ) )
 for iIi1iIII in range ( len ( ooO ) ) :
  if ooO [ iIi1iIII ] [ 0 ] == name :
   del ooO [ iIi1iIII ]
   i1oOOO0ooOO = open ( OOOOi11i1 , "w" )
   i1oOOO0ooOO . write ( json . dumps ( ooO ) )
   i1oOOO0ooOO . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 36 - 36: ii / I1ii11iIi11i . O00OOo00oo0o % ii . IIi + IIiIiII11i
 if 43 - 43: iiII11i1I1IIi % iIi1i1ii1 / I11i * O00OOo00oo0o
def oO0ooOoO ( ) :
 oooIi1I11IiI1i = os . path . join ( I11i1 , 'addons.ini' )
 I111 = open ( oooIi1I11IiI1i , "w+" )
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 I111 . write ( r'[' + IiII + ']' + '\n' )
 for iiI11ii1I1 , oOo0OOoO0 , oo0OOoOoo0O0O , iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = ( iiOOooooO0Oo + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  I111oOOooo00OOooO = ( iiI11ii1I1 + '=plugin://' + IiII + '/?url=' + iiOOooooO0Oo + '&mode=10012&name=' + ( iiI11ii1I1 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOo0OOoO0 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOo0OOoO0 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  I111 . write ( I111oOOooo00OOooO + '\n' )
  if 31 - 31: oOo0O0Ooo / I11i + oOo0O0Ooo - IIiIiII11i
  if 29 - 29: oOo0O0Ooo + Ii . o0o00Oo0O
def o0oo0Oo ( ) :
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo in IIIII11I1IiI :
  oo000ii ( '24/7' , iiOOooooO0Oo , 90021 , oOOOo00O00oOo + '247Streams.png' )
  if 10 - 10: Ii1I
def oO0OOOoO0o ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + '247Streams.png' , oOOOo00O00oOo + '247Streams.png' , '' )
def oo0oO ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def oO00O0 ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def o0Oo00oOO ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def O0oo ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 56 - 56: OOoOoo * O00OOo00oo0o
  if 98 - 98: iiII11i1I1IIi + o0o00Oo0O * O00OOo00oo0o + Ii - IIi - iI11I1II1I1I
def I11I111i1I1 ( ) :
 if 41 - 41: ii / ooOoO0O00
 I1IIII1i ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 if 70 - 70: OOooOOo % I11i % ooOoO0O00 / Ii1I % Ii / ooOoO0O00
def i1i1Ii1IiIII ( ) :
 if 9 - 9: iiII11i1I1IIi - oo0oO00 + o0o00Oo0O / OooOO000 % ooOoO0O00
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , i11ii in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 + '  -  ' + ( i11ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiOOooooO0Oo , 10023 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 97 - 97: I11i * IIiIi1iI
  if 78 - 78: iiII11i1I1IIi . IIi + oo0oO00 * OooOO000 - ooOoO0O00
  if 27 - 27: iIi1i1ii1 % ooOoO0O00 . I1ii11iIi11i % O00OOo00oo0o
def i1iI ( ) :
 if 73 - 73: ii . I1ii11iIi11i / o0o00Oo0O - o0o00Oo0O
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
 if 25 - 25: iI11I1II1I1I * iiII11i1I1IIi - oo0oO00 % Ii + iIi1i1ii1 % oo0oO00
def iiI ( url ) :
 o0OO0Oo = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( o0OO0Oo )
 IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 2 - 2: iI11I1II1I1I * oOo0O0Ooo % ooOoO0O00 % Ii1I + ii + oOo0O0Ooo
  if 16 - 16: IIi
  if 63 - 63: OooOO000
  if 11 - 11: OooOO000 - iI11I1II1I1I
def ooOo0O0 ( ) :
 if 83 - 83: ii
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oOO0OO0O ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( iiOOooooO0Oo )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if oOO0OO0O in iiI11ii1I1 . lower ( ) :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 12 - 12: IIiIi1iI
   if 36 - 36: O00OOo00oo0o . OOoOoo * ii - I11i
   if 60 - 60: IIi . OooOO000 / iI11I1II1I1I + IIi * O00OOo00oo0o
def OoooO00OoO0 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for o0O0O0ooo0oOO , iIIii , iiIiI1I1I1IiI , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII11 = ( iiIiI1I1I1IiI ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o0I1iI111ii111i = ( iIIii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  o00iI1Ii11iIiiI1 = 'Season ' + o0I1iI111ii111i + 'Episode ' + I1IIII11 + iiI11ii1I1
  i11iII11ii ( o00iI1Ii11iIiiI1 , o0O0O0ooo0oOO )
  if 89 - 89: iIi1i1ii1
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 51 - 51: OooOO000
  if 68 - 68: OooOO000 - I11i * oO0o % IIiIi1iI . IIiIi1iI - iI11I1II1I1I
def i11iII11ii ( name , url ) :
 o0O0O0ooo0oOO = url
 Ii1IOoO0o0O = name
 iii1i1iiiiIi = cloudflare . source ( o0O0O0ooo0oOO )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for i1ii , iIoOoO0 in i1I :
  OoO ( '[COLOR' + II + ']' + Ii1IOoO0o0O + iIoOoO0 + '[/COLOR]' , i1ii , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 31 - 31: Ii - IIiIi1iI / Ii1I - iIi1i1ii1
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: Ii * I1ii11iIi11i
 if 29 - 29: iIi1i1ii1 / IIiIi1iI % iiII11i1I1IIi
def IIiI1 ( ) :
 if 10 - 10: iI11I1II1I1I % ii % Ii1I
 if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * iiII11i1I1IIi
 if 89 - 89: iIi1i1ii1 - IIiIi1iI . iiII11i1I1IIi - O00OOo00oo0o - oOo0O0Ooo
 if 79 - 79: OOoOoo + OOoOoo + iIi1i1ii1
 if 39 - 39: o0o00Oo0O - ii
 if 63 - 63: iI11I1II1I1I % I11i * IIiIi1iI
 if 79 - 79: o0o00Oo0O
 if 32 - 32: IIiIiII11i . o0o00Oo0O + iIi1i1ii1 / OOooOOo / OOoOoo / IIi
 if 15 - 15: Ii1I
 if 4 - 4: OOoOoo + iI11I1II1I1I * OooOO000 + I1ii11iIi11i * I11i % IIiIiII11i
 if 88 - 88: oo0oO00 - ooOoO0O00 % Ii % IIiIiII11i * ii
 if 40 - 40: I1ii11iIi11i
 if 47 - 47: OOooOOo
 I1IIII1i ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 65 - 65: o0o00Oo0O + O00OOo00oo0o % iIi1i1ii1 * oOo0O0Ooo / IIiIi1iI / OOooOOo
 if 71 - 71: Ii / OOooOOo . oo0oO00
def iI1IIIi11 ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 69 - 69: o0o00Oo0O - o0o00Oo0O
def i1I1i1i1I1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 17 - 17: OOooOOo + ii % IIi
def Ii1Ii1 ( url ) :
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
  if 62 - 62: O00OOo00oo0o * iiII11i1I1IIi
  if 74 - 74: OOooOOo . iI11I1II1I1I
def oOOoO0oO0oo0O ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oO00Oo = 'http://www.watchseriesgo.to/search/' + oOO0OO0O . replace ( ' ' , '%20' )
 I1 = O000oo ( oO00Oo )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'watch online' in iiI11ii1I1 :
   pass
  else :
   print iiOOooooO0Oo
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + iiOOooooO0Oo , 10044 , oOo0OOoO0 , '' , '' )
   if 82 - 82: OOoOoo
   xbmcplugin . setContent ( I1IIiiIiii , 'movies' )
   if 51 - 51: oo0oO00 % oO0o + I11i + iIi1i1ii1 - ii . oO0o
def II11IiI1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , iiIiI1I1I1IiI , iIiiii in IIIII11I1IiI :
  oOoOOo000oOoO0 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( iiIiI1I1I1IiI ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + II + ']' + oOoOOo000oOoO0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOo0OOoO0 , '' , iIiiii )
  if 86 - 86: iI11I1II1I1I % oo0oO00 - OOooOOo + O00OOo00oo0o % oO0o . Ii1I
def iiIIiIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  oOoOOo000oOoO0 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + II + ']' + oOoOOo000oOoO0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 97 - 97: OooOO000 + iiII11i1I1IIi % I1ii11iIi11i . IIiIiII11i / IIiIiII11i * OooOO000
def o0Oo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOo0OOoO0 , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 16 - 16: OooOO000 % oOo0O0Ooo - IIiIi1iI
def ooO00OoO0o0OO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 I11o0oO00oO0o0o0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for iIIii , iI1ii111iiIii in I11o0oO00oO0o0o0 :
  IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( iI1ii111iiIii ) )
  for url , iiI11ii1I1 in IIIII11I1IiI :
   oOoOOo000oOoO0 = ( iIIii ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IIII1i ( '[COLOR' + II + ']' + oOoOOo000oOoO0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 10 - 10: oo0oO00 - OooOO000 % IIiIiII11i - O00OOo00oo0o - ooOoO0O00
class iIi11iI1i ( ) :
 if 46 - 46: ooOoO0O00 + IIiIiII11i * ooOoO0O00 - iIi1i1ii1
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 79 - 79: IIiIiII11i - oo0oO00 * Ii1I - OOooOOo . Ii1I
  oOoOOo000oOoO0 = name
  self . Get_Sources ( iiOOooooO0Oo , oOoOOo000oOoO0 )
  if 11 - 11: o0o00Oo0O * OOooOOo
  if 37 - 37: OOooOOo + o0o00Oo0O . o0o00Oo0O * I1ii11iIi11i % O00OOo00oo0o / OooOO000
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O000oo ( URL )
  IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + iiOOooooO0Oo
   self . Get_site_link ( URL , season_name )
   if 18 - 18: ii
 def Get_site_link ( self , url , season_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
  i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( I1 )
  I1II1 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( I1 )
  for url in IIIII11I1IiI :
   self . main ( url , season_name )
  for url in i1I :
   self . main ( url , season_name )
  for url in I1II1 :
   self . main ( url , season_name )
   if 57 - 57: IIiIi1iI . OOooOOo * I11i - ii
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   OooO = 'DACLIPS'
   if OooO in iIi11iI1i . source_list :
    pass
   else :
    self . daclips ( url , season_name , OooO )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    OooO = 'FILEHOOT'
    if OooO in iIi11iI1i . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , OooO )
   else :
    if 'thevideo.me' in url :
     OooO = 'THEVIDEO'
     if OooO in iIi11iI1i . source_list :
      pass
     else :
      self . thevideo ( url , season_name , OooO )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      OooO = 'ALLMYVIDEOS'
      if OooO in iIi11iI1i . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , OooO )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       OooO = 'VIDSPOT'
       if OooO in iIi11iI1i . source_list :
        pass
       else :
        self . vidspot ( url , season_name , OooO )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        OooO = 'VODLOCKER'
        if OooO in iIi11iI1i . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , OooO )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 16 - 16: ooOoO0O00 . ooOoO0O00 / O00OOo00oo0o % OOooOOo / oOo0O0Ooo * Ii1I
         if 30 - 30: I11i + ii + IIi / IIiIiII11i * I1ii11iIi11i
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for Ooo0oo , iiI11ii1I1 in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 59 - 59: iIi1i1ii1 / OOooOOo * oO0o * OooOO000 % oo0oO00
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for Ooo0oo , iiI11ii1I1 in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 61 - 61: I1ii11iIi11i - o0o00Oo0O - ii
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 4 - 4: IIiIiII11i - oo0oO00 % I1ii11iIi11i * Ii
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 18 - 18: I1ii11iIi11i % o0o00Oo0O
 def daclips ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for Ooo0oo in IIIII11I1IiI :
   self . Printer ( Ooo0oo , season_name , source_name )
   if 47 - 47: Ii1I * oo0oO00 + iI11I1II1I1I - oo0oO00 / OOoOoo
 def Printer ( self , Link , season_name , source_name ) :
  if 86 - 86: OOoOoo
  if Link in iIi11iI1i . List :
   pass
  elif source_name in iIi11iI1i . source_list :
   pass
  else :
   OoO ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   iIi11iI1i . List . append ( Link )
   iIi11iI1i . source_list . append ( source_name )
   if 43 - 43: oOo0O0Ooo / OooOO000 / IIiIi1iI + iI11I1II1I1I + ii
   xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 33 - 33: IIiIiII11i - OOoOoo - IIiIi1iI
   if 92 - 92: oO0o * OOoOoo
   if 92 - 92: oo0oO00
   if 7 - 7: OooOO000
   if 73 - 73: oO0o % Ii1I
def O0O0Oo00 ( ) :
 I1IIII1i ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , O0o0Oo , '' )
 if 32 - 32: IIi + OooOO000 + iI11I1II1I1I * I1ii11iIi11i
def ooiIii1I1111 ( url ) :
 I1IIII1i ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for I1iIiiiIi1111I , url , iII1i1ii , i1I1ii1i , iiiiII11iIi , O00o0O , OO00 , OOoO , i1IIi1i1Ii1 , Oooo , O00IiII in IIIII11I1IiI :
  iII1i1ii = iII1i1ii
  if 'Arsenal' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'arsenal-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                                  ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Bournemouth' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'afc-bournemouth.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                       ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Burnley' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'KEGnQWW.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                                   ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Chelsea' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'chelsea.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                                  ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Crystal' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'CrystalPalace.0.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                       ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Everton' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'Everton.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                                   ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Hull' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'hull-city-afc.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                                 ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Leicester' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                       ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Liverpool' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'liverpool-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                               ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Manchester City' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'city-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '               ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Manchester United' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + '91.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '          ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Middlesbrough' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                 ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Southampton' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'southampton-fc-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                   ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Stoke City' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'stoke-city.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                          ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Sunderland' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'sunderland-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                        ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Swansea' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'swansea-city-afc.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                    ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Tottenham' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '        ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Watford' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '                              ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'Bromwich' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '   ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  elif 'West Ham' in iII1i1ii :
   IIi1iiii1iI = oOOOo00O00oOo + 'west-ham.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + I1iIiiiIi1111I + ' - ' + iII1i1ii + '             ' + i1I1ii1i + '        ' + iiiiII11iIi + '        ' + O00o0O + '        ' + OO00 + '        ' + OOoO + '        ' + i1IIi1i1Ii1 + '        ' + Oooo + '[/COLOR]'
  I1IIII1i ( str ( iiI11ii1I1 ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , IIi1iiii1iI , IIi1iiii1iI , iII1i1ii )
  if 27 - 27: oO0o . I11i . o0o00Oo0O - o0o00Oo0O / iiII11i1I1IIi - oO0o
def iIII1I1ii ( description ) :
 iII1i1ii = description
 iiOOooooO0Oo = ( 'http://www.fullmatchesandshows.com/?s=' + iII1i1ii ) . replace ( ' ' , '%20' )
 iiIIi11ii1Ii ( iiOOooooO0Oo )
 if 60 - 60: I11i . OOooOOo % O00OOo00oo0o / oOo0O0Ooo / o0o00Oo0O
def IiI ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iiOOooooO0Oo , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOo0OOoO0 , O0o0Oo , '' )
  if 34 - 34: o0o00Oo0O / IIi
def OOOoo0O00Oooo ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
  I11iIIi = re . compile ( '(.*?)</h2>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for I111Ii11i11I in I11iIIi :
   I111Ii11i11I = I111Ii11i11I
  i11I = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for oO0000O0Oo00O , oOo0OOoO0 , time , IiIII in i11I :
   II1i = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( IiIII )
   I1IIII1i ( '[COLOR' + II + ']' + I111Ii11i11I + ' - ' + oO0000O0Oo00O + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOo0OOoO0 , O0o0Oo , ( str ( II1i ) ) )
   if 44 - 44: iIi1i1ii1 * IIiIi1iI / OOooOOo
 i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if 69 - 69: IIiIi1iI . IIi - oOo0O0Ooo
def IiIi ( ) :
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
 if 44 - 44: IIiIiII11i . IIiIiII11i + IIi * iIi1i1ii1
def i1iIi ( url ) :
 I1IIII1i ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  i1II1i = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   i1II1i = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   OoO ( '[COLOR' + II + ']' + i1II1i + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  i1II1i = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   OoO ( '[COLOR' + II + ']' + i1II1i + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
def iiIIi11ii1Ii ( url ) :
 I1IIII1i ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 27 - 27: Ii1I / IIi
 if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
 if 63 - 63: OOoOoo + iI11I1II1I1I + oOo0O0Ooo + O00OOo00oo0o
 if 72 - 72: oO0o + Ii + Ii1I
 if 96 - 96: oo0oO00 % ooOoO0O00 / I11i
 if 13 - 13: IIiIiII11i - I1ii11iIi11i % Ii + OooOO000
 if 88 - 88: o0o00Oo0O . oo0oO00 % oOo0O0Ooo
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  i1II1i = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   OoO ( '[COLOR' + II + ']' + i1II1i + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
   if 10 - 10: oOo0O0Ooo + o0o00Oo0O
def Oooo0Oo00o ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for i1ii in IIIII11I1IiI :
  IIoO = ( i1ii ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  iii1 ( 'http:' + IIoO )
  if 13 - 13: ooOoO0O00
  if 48 - 48: o0o00Oo0O + oO0o . OooOO000 * I11i * OooOO000
  if 69 - 69: oO0o - ii - IIi % iiII11i1I1IIi / OOooOOo - IIiIiII11i
  if 67 - 67: IIi + IIi + oO0o . Ii + Ii1I + Ii
def IIi11I1i1I1I ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  OoO ( iiI11ii1I1 , url , 8046 , oOo0OOoO0 )
 for url in i1I :
  oo000ii ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def IiII1I ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iii1 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 72 - 72: iIi1i1ii1 / I1ii11iIi11i / oo0oO00 * OOooOOo + IIi
def OOoo0OOOo0o ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 10 - 10: O00OOo00oo0o
def iII1ii1 ( ) :
 oo000ii ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 oo000ii ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 oo000ii ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , iiOOooooO0Oo , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def I11i1i11IiIi1 ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + oOo0OOoO0 )
 for url in next :
  oo000ii ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 8 - 8: OooOO000 - oOo0O0Ooo * I1ii11iIi11i % Ii1I * ii
  if 26 - 26: ooOoO0O00 / OooOO000 . OooOO000
def I1i11IIIi ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   OoO ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   oo000ii ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def III1IIIIIiiI ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  OoO ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10012 , '' )
  if 38 - 38: o0o00Oo0O
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOi1i1i11iI11II ( name , url ) :
 II1iiI1iI = 0
 name = name
 url = url
 OooOoOO0 = [ '144' , '240' , '380' , '480' , '720' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  iii1 ( url )
  if 74 - 74: OOoOoo - o0o00Oo0O / O00OOo00oo0o * iIi1i1ii1 % IIiIi1iI . O00OOo00oo0o
  if 60 - 60: Ii1I . IIiIiII11i * Ii . I11i
  if 66 - 66: OooOO000 / Ii * o0o00Oo0O
  if 78 - 78: OOoOoo - iiII11i1I1IIi % o0o00Oo0O - IIi % oO0o
  if 43 - 43: oO0o
  if 90 - 90: ii + o0o00Oo0O + Ii1I / iiII11i1I1IIi / iIi1i1ii1 * Ii1I
  if 100 - 100: iiII11i1I1IIi
  if 82 - 82: iI11I1II1I1I
def iIiiII ( ) :
 OoO000O0Oo = oo00ooOoO00 ( 'http://documentarylovers.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  if 'genre' in iiOOooooO0Oo :
   oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , iiOOooooO0Oo , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def iII1I ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , oOo0OOoO0 )
 for url in next :
  oo000ii ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 92 - 92: O00OOo00oo0o % iIi1i1ii1
def Ii1Ii11I ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in i1I :
  III1IIIIIiiI ( url )
  if 28 - 28: IIiIi1iI . ooOoO0O00
def o0o00O ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = 'http://documentarylovers.com/?s=' + ( oOO0OO0O ) . replace ( ' ' , '+' )
 o00o = i1IiiI1iIi . lower ( )
 iII1I ( o00o )
 if 46 - 46: OOooOOo
def i1iiII ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'films' in url :
   oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def ooii ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  if 'films' in url :
   OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + oOo0OOoO0 )
 for url in i1I :
  oo000ii ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def oOO0O0O0OO00oo ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'rtd' in url :
   I11IIIIiI1 ( url )
   if 93 - 93: Ii
def I11IIIIiI1 ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OoO000O0Oo )
 for i1Oo00 , file in IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1Oo00 + file )
  iii1 ( url )
  if 80 - 80: ooOoO0O00 . oOo0O0Ooo - oo0oO00 + IIi + OooOO000 % oo0oO00
  if 13 - 13: IIiIiII11i / OOooOOo / OOooOOo + IIiIi1iI
def Ii1i ( ) :
 I1 = oo00ooOoO00 ( 'http://www.stream2watch.co/live-tv' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , ooooOoOooo00Oo in IIIII11I1IiI :
  oo000ii ( ( iiI11ii1I1 + '[COLOR' + II + ']' + ooooOoOooo00Oo + '[/COLOR]' ) , iiOOooooO0Oo , 8086 , oOo0OOoO0 )
  if 72 - 72: iiII11i1I1IIi
def i1I1IIiIIi ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8087 , oOo0OOoO0 )
  if 33 - 33: oO0o % OOoOoo - iI11I1II1I1I
def IIII1I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i1iI1I1IIIi1i ( url , iiI11ii1I1 )
  if 73 - 73: o0o00Oo0O * O00OOo00oo0o . ooOoO0O00
def i1iI1I1IIIi1i ( url , name ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  print url
  OoO ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 51 - 51: oO0o - OooOO000 % o0o00Oo0O - OOooOOo
def o0ooo ( ) :
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iiOOooooO0Oo , 3002 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def o0oo00O ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def IIIIII1iI1II ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 iiiI1 = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , iiI11ii1I1 in iiiI1 :
  oo000ii ( '[COLOR' + II + ']Season- ' + iiI11ii1I1 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  oo000ii ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def O00oooO00oo ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  Ii111III1i11I ( url )
def Ii111III1i11I ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( url )
  if 62 - 62: iiII11i1I1IIi . oO0o + oO0o + IIiIiII11i * iI11I1II1I1I + ii
def i1Iii11I1i ( ) :
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiOOooooO0Oo , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def Oo0OOOOOOO0oo ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  o0oO0OoO0 ( url )
  if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
def ii1I1IiiI1ii1i ( ) :
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiOOooooO0Oo , 8065 , oOOOo00O00oOo + 'classictv.png' )
def I1iIIIiiii ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'mp4' in url :
   iii1 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 44 - 44: O00OOo00oo0o / iIi1i1ii1 * IIi * ooOoO0O00 . iIi1i1ii1 * Ii
def O0o0oo0O ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iiOOooooO0Oo , 8071 , oOOOo00O00oOo + 'streams.png' )
def Ooo00OOo000 ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '(Free Access)' in iiI11ii1I1 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def i1ooOO00o0 ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOo0OOoO0 , O0OoooO0 , '' )
  if 44 - 44: oOo0O0Ooo % IIi * Ii * Ii - I1ii11iIi11i . O00OOo00oo0o
def o00i111iiIiiIiI ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  OOooooO ( 'http://watchxxxfree.com/categories' )
 if iI1i11iII111 == 1 :
  oOoo00 ( 'http://www.perfectgirls.net' )
 if iI1i11iII111 == 2 :
  IIiIi ( 'http://www.xvideos.com/best' )
 if iI1i11iII111 == 3 :
  I1I1IIiiI1 ( 'http://www.xvideos.com/best' )
 if iI1i11iII111 == 4 :
  IIiIi ( 'http://www.xvideos.com/best' )
 if iI1i11iII111 == 5 :
  IIiIi ( 'http://www.xvideos.com/verified/videos' )
 if iI1i11iII111 == 6 :
  oooOOO0o0O0 ( 'http://www.xvideos.com/tags' )
 if iI1i11iII111 == 7 :
  iiiI1IiI ( 'http://www.xvideos.com/porn' )
 if iI1i11iII111 == 8 :
  Ii111IIIIii ( )
  if 54 - 54: OooOO000 / oOo0O0Ooo * iiII11i1I1IIi / Ii * O00OOo00oo0o . iI11I1II1I1I
  if 40 - 40: oOo0O0Ooo . iIi1i1ii1 / ooOoO0O00
  if 28 - 28: iIi1i1ii1
  if 66 - 66: iiII11i1I1IIi
  if 27 - 27: o0o00Oo0O
  if 73 - 73: Ii + oo0oO00 % iiII11i1I1IIi . ii % oo0oO00
  if 32 - 32: Ii - IIiIiII11i
  if 21 - 21: OOooOOo - IIiIiII11i
  if 10 - 10: OOooOOo - I11i * Ii / I1ii11iIi11i + I11i + iI11I1II1I1I
def IiIIIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'ch' in url :
   IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def Oo0iII ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 O0ooiIIi1 = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for iiI11ii1I1 , url in O0ooiIIi1 :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def OoOo0O00 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   iI1i1iI1iI ( url )
def I1IIiIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( url )
def OOooooO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , IIII in IIIII11I1IiI :
  if 'category' in url :
   IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]   ' + IIII + '[/COLOR]' , url , 90006 , oOo0OOoO0 , oOOOo00O00oOo + 'Jizbox.png' , '' )
def OOOOoOoO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 O0ooiIIi1 = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , oOo0OOoO0 , '' , '' )
 for url in O0ooiIIi1 :
  I1IIII1i ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def OO000 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   iI1i1iI1iI ( url )
def iI1i1iI1iI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( url )
def oOoo00 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , IIII in IIIII11I1IiI :
  if 'category' in url :
   IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]' + IIII + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def o0oOoo0o ( url ) :
 I1 = O000oo ( url )
 o0O0O0ooo0oOO = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 O0ooiIIi1 = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , oOo0OOoO0 , '' , '' )
 for url in O0ooiIIi1 :
  I1IIII1i ( '[COLORred]NEXT[/COLOR]' , o0O0O0ooo0oOO + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def IiiIiIIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  O00Oo ( 'http://www.perfectgirls.net' + url )
def O00Oo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( 'http://' + url )
def iiiI1IiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , iiI11ii1I1 , IIII in IIIII11I1IiI :
  IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - No of Videos : [COLORorange]' + IIII + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def oooOOO0o0O0 ( url ) :
 I1 = O000oo ( url )
 O0ooiIIi1 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in O0ooiIIi1 :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , iiI11ii1I1 , IIII in IIIII11I1IiI :
  IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - No of Videos : [COLORorange]' + ( IIII + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 63 - 63: I11i / o0o00Oo0O - ii
def oo0O0 ( url ) :
 I1 = O000oo ( url )
 O0ooiIIi1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in O0ooiIIi1 :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , ooOo000OoO0o in IIIII11I1IiI :
  IIiii11ii1i ( iiI11ii1I1 + '--' + ( ooOo000OoO0o ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOo0OOoO0 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 34 - 34: IIiIiII11i - OOoOoo % OOooOOo % iIi1i1ii1 / IIiIi1iI
  if 10 - 10: ii . oOo0O0Ooo * o0o00Oo0O * oO0o - IIi
def IIiIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , i1II1iII , III in IIIII11I1IiI :
  IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - Porn Quality : [COLORorange]' + III + ' - [COLORred]' + i1II1iII + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oOo0OOoO0 , oOo0OOoO0 , III + ' - ' + i1II1iII )
 iII11 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in iII11 :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 96 - 96: iiII11i1I1IIi * Ii1I * iIi1i1ii1 + Ii1I % oOo0O0Ooo + Ii
def I1I1IIiiI1 ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 O0ooiIIi1 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in O0ooiIIi1 :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '/c/' in url :
   IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 37 - 37: iiII11i1I1IIi % Ii1I / IIiIi1iI
   if 94 - 94: iiII11i1I1IIi / oO0o . I11i
def Ii111IIIIii ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iIiOo = ( oOO0OO0O ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 o00o = iIiOo . lower ( )
 iio00 = 'http://www.xvideos.com/?k=' + o00o
 print iio00 + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O000oo ( iio00 )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 , i1II1iII , III in IIIII11I1IiI :
  IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - Porn Quality : [COLORorange]' + III + ' - [COLORred]' + i1II1iII + '[/COLOR]' , 'http://www.xvideos.com' + iiOOooooO0Oo , 10108 , oOo0OOoO0 , oOo0OOoO0 , III + ' - ' + i1II1iII )
 iII11 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for iiOOooooO0Oo in iII11 :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iiOOooooO0Oo , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
if 48 - 48: IIi
if 26 - 26: OooOO000 * O00OOo00oo0o * oo0oO00 * OOooOOo
if 48 - 48: OooOO000 % Ii . ii * OOoOoo % oO0o . OooOO000
if 6 - 6: o0o00Oo0O . IIiIi1iI - oo0oO00 / Ii
if 84 - 84: iiII11i1I1IIi / Ii1I * I11i * oO0o * IIi * o0o00Oo0O
if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
if 75 - 75: IIiIiII11i . oOo0O0Ooo + IIi - OOooOOo - o0o00Oo0O . iiII11i1I1IIi
if 19 - 19: iIi1i1ii1 * ooOoO0O00 % o0o00Oo0O + iiII11i1I1IIi
if 25 - 25: O00OOo00oo0o - iIi1i1ii1 / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + oo0oO00 + oo0oO00 + OooOO000
if 4 - 4: I11i + iiII11i1I1IIi / OooOO000 + ooOoO0O00 % I11i % OooOO000
if 80 - 80: iIi1i1ii1
if 26 - 26: iI11I1II1I1I . ii - iI11I1II1I1I
if 59 - 59: Ii1I + iiII11i1I1IIi . oo0oO00
if 87 - 87: oO0o
if 34 - 34: O00OOo00oo0o . OOooOOo / Ii / OooOO000
if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + IIi
if 31 - 31: iIi1i1ii1 * I11i * iIi1i1ii1 + oO0o * I11i . O00OOo00oo0o
if 89 - 89: ii * iIi1i1ii1 * oOo0O0Ooo . IIiIi1iI * iIi1i1ii1 / OooOO000
if 46 - 46: Ii
if 15 - 15: o0o00Oo0O / ooOoO0O00 / ooOoO0O00 . OooOO000 % OOooOOo + oOo0O0Ooo
if 48 - 48: O00OOo00oo0o % OooOO000 % iIi1i1ii1 % iI11I1II1I1I . iIi1i1ii1
if 14 - 14: OooOO000 * oO0o % o0o00Oo0O + iiII11i1I1IIi + Ii1I
if 23 - 23: I1ii11iIi11i % OooOO000 + iIi1i1ii1 - O00OOo00oo0o
if 65 - 65: ii
if 22 - 22: IIi + IIiIiII11i + I1ii11iIi11i
if 83 - 83: IIiIi1iI
if 43 - 43: IIi
if 84 - 84: IIi . OOoOoo . OooOO000
if 2 - 2: I1ii11iIi11i - OOooOOo
if 49 - 49: iIi1i1ii1 + IIiIiII11i / oo0oO00 - OOooOOo % OOooOOo + oOo0O0Ooo
if 54 - 54: IIiIi1iI % I1ii11iIi11i - IIi
if 16 - 16: Ii1I * OooOO000 / iiII11i1I1IIi
if 46 - 46: IIiIiII11i
if 13 - 13: OOoOoo + IIiIiII11i % oOo0O0Ooo
def IiIiiIII ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( I1 )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( I1 )
 I1II1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'http' in url :
   OoO ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   OoO ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in I1II1 :
  if 'http' in url :
   OoO ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
   if 4 - 4: o0o00Oo0O / iiII11i1I1IIi . oO0o - IIiIi1iI / IIi
def I1IIiIi1I1I1 ( url ) :
 IiI1iii11iIi1 = xbmc . Player ( i1iI11I1II1 ( ) )
 import urlresolver
 try : IiI1iii11iIi1 . play ( url )
 except : pass
 if 8 - 8: oO0o % IIiIi1iI . IIi / OooOO000 * iI11I1II1I1I + ii
 if 27 - 27: OOoOoo - ooOoO0O00
def o0O00o0 ( ) :
 if 61 - 61: IIiIiII11i % Ii + iI11I1II1I1I + Ii1I / oOo0O0Ooo * ooOoO0O00
 if 2 - 2: IIiIiII11i . iiII11i1I1IIi
 if 83 - 83: oOo0O0Ooo - O00OOo00oo0o + oOo0O0Ooo . oOo0O0Ooo
 if 45 - 45: ooOoO0O00 % IIi % IIiIiII11i
 if 4 - 4: oo0oO00 * oOo0O0Ooo - IIiIi1iI / IIiIiII11i + IIi / Ii
 if 63 - 63: oO0o + IIiIi1iI
 if 3 - 3: OOooOOo - O00OOo00oo0o / oo0oO00 . o0o00Oo0O * IIiIi1iI / Ii1I
 if 18 - 18: iIi1i1ii1
 if 74 - 74: iIi1i1ii1 + Ii1I + oOo0O0Ooo
 if 37 - 37: OOoOoo
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 8091 , oOOOo00O00oOo + 'gofish.png' )
def OOO0O ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8092 , oOo0OOoO0 )
 for url in next :
  oo000ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def I1iiIII ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 II1III = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 in II1III :
  oOo0OOoO0 = oOo0OOoO0
 for url , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8092 , oOo0OOoO0 )
 for url in next :
  oo000ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 14 - 14: Ii1I * O00OOo00oo0o % ooOoO0O00 / Ii1I
def i11II1 ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 86 - 86: I1ii11iIi11i
  if 88 - 88: O00OOo00oo0o * oOo0O0Ooo
  if 30 - 30: OOooOOo / oo0oO00 / iIi1i1ii1 * I11i * oo0oO00 . oOo0O0Ooo
  if 93 - 93: OOooOOo
o0OoOo0o0OOoO0 = '{PQ},' ; i1I1IIIiii1 = '{SC},' ; oOO0 = '{XG},' ; oOo = '{JP},' ; oooO = '{HW},' ; OO0oooOO = '{RT},'
def i1II ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 IIIi1iiIIiiiI = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 iiOOooooO0Oo = ( i11 ( 'http://m3.doctor-movies.com/english/' ) )
 if 26 - 26: IIiIi1iI % oo0oO00 + oOo0O0Ooo / OOoOoo . oOo0O0Ooo
 oOOOOOoOO = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 IiIi1i1 = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvc2lsZW50aHVudGVyL2xpc3RzL3NoLnBocA==' ) )
 ii11 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 o00000O = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 iIiiiII11 = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oOO0OO0O
 ooo00Oo0 = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 iIii1i1Ii = ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvbW92aWVzZWFyY2gucGhw' ) )
 III1iIii = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 iiIII1i1 = ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL1NILnBocA==' ) )
 if 78 - 78: oo0oO00 % OOooOOo
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 1 - 1: OOooOOo - I11i / IIiIi1iI - OOoOoo / ooOoO0O00
 if 28 - 28: oO0o / O00OOo00oo0o * oOo0O0Ooo + IIiIi1iI
 Iiii = OOoOO0oo0ooO ( oOOOOOoOO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 OO0OoO0o00 = OOoOO0oo0ooO ( IiIi1i1 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 iIIIIi11i = OOoOO0oo0ooO ( ii11 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 oooOOoo0 = OOoOO0oo0ooO ( iIiiiII11 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 Oo00O00o0 = OOoOO0oo0ooO ( ooo00Oo0 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 IiII1 = OOoOO0oo0ooO ( iIii1i1Ii )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 iI1I1I = OOoOO0oo0ooO ( III1iIii )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 Oo0o0oOo0oO = OOoOO0oo0ooO ( iiIII1i1 )
 if 20 - 20: OOoOoo - iI11I1II1I1I
 if 25 - 25: iiII11i1I1IIi + OOooOOo
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
  for o00OoOOoO , iiI11ii1I1 in IIIII11I1IiI :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source 1[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiOOooooO0Oo + o00OoOOoO ) , 222 , '' )
    o0oOoO00o . update ( 0 , "" , "Getting Source 1 Links" )
    if 28 - 28: iI11I1II1I1I * iiII11i1I1IIi . oOo0O0Ooo
    if 78 - 78: ii . ii / o0o00Oo0O
    if 25 - 25: IIiIiII11i % IIiIiII11i - iIi1i1ii1 . o0o00Oo0O
    if 79 - 79: OOoOoo / oO0o * ii * OOooOOo + oOo0O0Ooo
    if 68 - 68: iiII11i1I1IIi / iI11I1II1I1I . I1ii11iIi11i + Ii + I11i
    if 92 - 92: oO0o . I11i . iIi1i1ii1 % OOooOOo
    if 58 - 58: Ii1I % iIi1i1ii1 * iIi1i1ii1 - OooOO000
 if Iiii != 'Failed' :
  I1II1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for o00OoOOoO , iiI11ii1I1 in I1II1 :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( oOOOOOoOO + o00OoOOoO ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if OO0OoO0o00 != 'Failed' :
  oo00OO0000oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OO0OoO0o00 )
  for iiOOooooO0Oo , O00Ooo , iIiiii , iiii11i , iiI11ii1I1 in oo00OO0000oO :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Silent Hunter[/COLOR]' ) , iiOOooooO0Oo , 222 , O00Ooo , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Silent Hunter Links" )
    if 9 - 9: IIiIi1iI - iIi1i1ii1 % IIiIiII11i + OOoOoo + IIi % o0o00Oo0O
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if iIIIIi11i != 'Failed' :
  o00OoOo0 = [ ]
  O00OOooo0Ooo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iIIIIi11i )
  for iiOOooooO0Oo , O00Ooo , iIiiii , iiii11i , iiI11ii1I1 in O00OOooo0Ooo :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    if iiI11ii1I1 in o00OoOo0 :
     pass
    else :
     I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , iiOOooooO0Oo , 1016 , O00Ooo , iiii11i , iIiiii )
     o00OoOo0 . append ( iiI11ii1I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if oooOOoo0 != 'Failed' :
  iii1iII = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oooOOoo0 )
  for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in iii1iII :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iiOOooooO0Oo , 7067 , oOo0OOoO0 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 77 - 77: OOoOoo + ii * ooOoO0O00 % ii
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 3 - 3: iIi1i1ii1 * IIiIi1iI - oOo0O0Ooo / ooOoO0O00
    if 21 - 21: IIiIiII11i + O00OOo00oo0o
    if 22 - 22: OOoOoo . OooOO000 + I1ii11iIi11i
    if 45 - 45: I1ii11iIi11i % I1ii11iIi11i + I1ii11iIi11i / o0o00Oo0O % ii
    if 92 - 92: iIi1i1ii1 . OOooOOo . iiII11i1I1IIi - ii / IIiIi1iI
    if 80 - 80: iI11I1II1I1I / Ii + OooOO000
    if 41 - 41: O00OOo00oo0o + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
    if 96 - 96: oOo0O0Ooo - iI11I1II1I1I
    if 25 - 25: ii . iIi1i1ii1 % OooOO000 . OOoOoo
 if IiII1 != 'Failed' :
  ooo000 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( IiII1 )
  for iiI11ii1I1 , iiOOooooO0Oo , O00Ooo , iiii11i , iIiiii in ooo000 :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Reaper[/COLOR]' ) , iiOOooooO0Oo , 222 , O00Ooo , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 82 - 82: iI11I1II1I1I * ii
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if iI1I1I != 'Failed' :
  i1ii1i1i1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iI1I1I )
  for iiOOooooO0Oo , O00Ooo , iIiiii , iiii11i , iiI11ii1I1 in i1ii1i1i1 :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source APPRENTICE[/COLOR]' ) , iiOOooooO0Oo , 222 , O00Ooo , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 92 - 92: I1ii11iIi11i
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 60 - 60: Ii . o0o00Oo0O * iI11I1II1I1I * OOooOOo
 if Oo0o0oOo0oO != 'Failed' :
  OoOOoO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( Oo0o0oOo0oO )
  for iiOOooooO0Oo , O00Ooo , iiI11ii1I1 in OoOOoO0o :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Silent Hunter[/COLOR]' ) , iiOOooooO0Oo , 222 , O00Ooo )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 78 , "" , "Getting Silent Hunter Links" )
    if 66 - 66: iiII11i1I1IIi - iiII11i1I1IIi + OOoOoo
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 Oo0O0OO0OoO0 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 20 - 20: O00OOo00oo0o . ooOoO0O00
 for III11I in Oo0O0OO0OoO0 :
  Ii1I11I = OOOO0OOoO0O0 + III11I + IIiiiiiiIi1I1
  i1iiiI = OOoOO0oo0ooO ( Ii1I11I )
  if i1iiiI != 'Failed' :
   III11iIII1 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iiiI )
   for iiOOooooO0Oo , O00Ooo , iIiiii , iiii11i , iiI11ii1I1 in III11iIII1 :
    if oOO0OO0O in iiI11ii1I1 . lower ( ) :
     I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - Source Pandoras[/COLOR]' , iiOOooooO0Oo , 222 , O00Ooo , iiii11i , iIiiii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 4 - 4: Ii + ii / Ii . ii % Ii1I / OOooOOo
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
     if 35 - 35: Ii1I % ooOoO0O00 + I11i - iI11I1II1I1I
 Oo0O0OO0OoO0 = [ '0-9/' , 'A/' , 'B/' , 'C/' , 'D/' , 'E/' , 'F/' , 'G/' , 'H/' , 'I/' , 'J/' , 'K/' , 'L/' , 'M/' , 'N/' , 'O/' , 'P/' , 'R/' , 'S/' , 'T/' , 'U/' , 'V/' , 'W/' , 'X/' , 'Y/' , 'Z/' ]
 if 28 - 28: oOo0O0Ooo * IIiIiII11i * OOooOOo % IIi - IIi
 if 35 - 35: I1ii11iIi11i . IIiIi1iI - ooOoO0O00 . OOooOOo
 for III11I in Oo0O0OO0OoO0 :
  Ii1I11I = IIIi1iiIIiiiI + III11I
  I1iI1 = OOoOO0oo0ooO ( Ii1I11I )
  if I1iI1 != 'Failed' :
   II11i1ii = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( I1iI1 )
   for o00OoOOoO , iiI11ii1I1 in II11i1ii :
    if oOO0OO0O in iiI11ii1I1 . lower ( ) :
     OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + 'source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( IIIi1iiIIiiiI + III11I + o00OoOOoO ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 74 - 74: ii - I11i * OooOO000
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
     if 37 - 37: I11i * I1ii11iIi11i
     if 11 - 11: oo0oO00
def iIi1Ii1i1iI ( ) :
 if 62 - 62: ii % oo0oO00 * IIiIiII11i * O00OOo00oo0o * O00OOo00oo0o / IIiIi1iI
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 if 90 - 90: O00OOo00oo0o . IIiIiII11i . Ii1I
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllc2dvLnRvL3NlYXJjaC8=' ) ) + ( oOO0OO0O ) . replace ( ' ' , '%20' )
 o0O0O0ooo0oOO = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vdHZzaG93cy90dm1haW4ucGhw' ) )
 oOOOOOoOO = ( i11 ( 'aHR0cDovL3R2LmRsLXBhcnMuaW4v' ) )
 IiIi1i1 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 ii11 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o00o ) . replace ( ' ' , '+' )
 o00000O = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 iIiiiII11 = ( i11 ( 'aHR0cHM6Ly9sZXRvLmZlcmFsaG9zdGluZy5jb20vZ3JpbXcwMWYvdHIvc2VyaWFsc2VhcmNoLnBocA==' ) )
 ooo00Oo0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 32 - 32: IIiIi1iI - oO0o . OooOO000 . OooOO000 % ooOoO0O00 * iIi1i1ii1
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 65 - 65: OooOO000 / IIiIi1iI . IIiIiII11i
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = OOoOO0oo0ooO ( o0O0O0ooo0oOO )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = OOoOO0oo0ooO ( oOOOOOoOO )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = OOoOO0oo0ooO ( IiIi1i1 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 iIIIIi11i = cloudflare . source ( ii11 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 I1iI1 = OOoOO0oo0ooO ( o00000O )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 oooOOoo0 = OOoOO0oo0ooO ( iIiiiII11 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 Oo00O00o0 = OOoOO0oo0ooO ( ooo00Oo0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 90 - 90: iiII11i1I1IIi
 if Oo00O00o0 != 'Failed' :
  o00oooo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Oo00O00o0 )
  for iiOOooooO0Oo , O00Ooo , iIiiii , iiii11i , iiI11ii1I1 in o00oooo :
   if o00o in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source HeroVision[/COLOR]' ) , iiOOooooO0Oo , 1016 , O00Ooo , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 63 - 63: IIiIiII11i - iiII11i1I1IIi . OOooOOo
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 8 - 8: oOo0O0Ooo * IIiIi1iI / OOoOoo + OOooOOo . OOoOoo - IIi
 if oooOOoo0 != 'Failed' :
  iii1iII = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( oooOOoo0 )
  for iiI11ii1I1 , iiOOooooO0Oo , O00Ooo , iiii11i , iIiiii in iii1iII :
   if o00o in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- source Reaper[/COLOR]' ) , iiOOooooO0Oo , 90037 , O00Ooo , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 80 - 80: iI11I1II1I1I / oo0oO00 * I1ii11iIi11i - IIi * OooOO000
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 97 - 97: OOoOoo - iiII11i1I1IIi / IIiIiII11i
    if 26 - 26: OooOO000 + o0o00Oo0O * OooOO000 . ooOoO0O00
    if 50 - 50: iI11I1II1I1I - iiII11i1I1IIi % OooOO000 - I1ii11iIi11i
    if 52 - 52: oo0oO00 + iIi1i1ii1 - Ii1I * iIi1i1ii1 . IIi + O00OOo00oo0o
    if 43 - 43: oOo0O0Ooo % OOoOoo % Ii1I
    if 53 - 53: oo0oO00 % IIi % Ii1I . O00OOo00oo0o . O00OOo00oo0o . OooOO000
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 73 - 73: OooOO000 / IIiIi1iI + oO0o / OOooOOo . IIiIiII11i * iIi1i1ii1
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
   if o00o in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - WatchSeries[/COLOR]' , 'http://www.watchseriesgo.to' + iiOOooooO0Oo , 10044 , oOo0OOoO0 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 40 , "" , "Getting Source WatchSeries Links" )
    if 21 - 21: oOo0O0Ooo - oOo0O0Ooo + OooOO000 % oOo0O0Ooo * oo0oO00
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 74 - 74: OooOO000 / iiII11i1I1IIi . oOo0O0Ooo - ii + IIiIiII11i + iiII11i1I1IIi
    if 36 - 36: iIi1i1ii1 * oOo0O0Ooo * Ii1I . iiII11i1I1IIi * Ii1I
    if 76 - 76: IIi + o0o00Oo0O / OOoOoo - oO0o
    if 27 - 27: I1ii11iIi11i - iI11I1II1I1I * OooOO000 * IIiIiII11i * Ii1I
    if 9 - 9: Ii + IIi - OOooOOo / IIiIi1iI % ooOoO0O00 / oo0oO00
    if 22 - 22: ooOoO0O00
    if 3 - 3: oO0o * Ii1I - OooOO000 + Ii1I
    if 63 - 63: iiII11i1I1IIi * IIiIi1iI % IIiIiII11i % O00OOo00oo0o + oOo0O0Ooo * I1ii11iIi11i
    if 96 - 96: OOoOoo
    if 99 - 99: iI11I1II1I1I - IIiIi1iI
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iii1i1iiiiIi )
  for iiOOooooO0Oo , O00Ooo , iIiiii , iiii11i , iiI11ii1I1 in i1I :
   if o00o in iiI11ii1I1 . lower ( ) :
    oo000ii ( ( iiI11ii1I1 + '[COLORblue] - source Redemption[/COLOR]' ) . replace ( '..&gt;' , '' ) , iiOOooooO0Oo , 1016 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Redemption Links" )
    if 79 - 79: oOo0O0Ooo + oo0oO00 % iiII11i1I1IIi % oo0oO00
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  I1II1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for iiI11ii1I1 in I1II1 :
   if o00o in iiI11ii1I1 . lower ( ) :
    oo000ii ( ( iiI11ii1I1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOOOOOoOO + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 56 - 56: Ii1I + oo0oO00 . oO0o + ii * Ii1I - o0o00Oo0O
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  oo00OO0000oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for iiI11ii1I1 in oo00OO0000oO :
   if o00o in iiI11ii1I1 . lower ( ) :
    oo000ii ( ( iiI11ii1I1 + ' source 4' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( IiIi1i1 + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 35 - 35: IIi . iiII11i1I1IIi . O00OOo00oo0o - iiII11i1I1IIi % iiII11i1I1IIi + O00OOo00oo0o
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if iIIIIi11i != 'Failed' :
  O00OOooo0Ooo = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( iIIIIi11i )
  for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in O00OOooo0Ooo :
   if o00o in iiI11ii1I1 . lower ( ) :
    oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - Source - Dizi[/COLOR]' , iiOOooooO0Oo , 8062 , oOo0OOoO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 99 - 99: I11i + IIi
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if I1iI1 != 'Failed' :
  II11i1ii = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1iI1 )
  for iiOOooooO0Oo , O00Ooo , iIiiii , iiii11i , iiI11ii1I1 in II11i1ii :
   if o00o in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '- Source Scooby[/COLOR]' ) , iiOOooooO0Oo , 1016 , O00Ooo , iiii11i , iIiiii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 34 - 34: O00OOo00oo0o * I11i . oOo0O0Ooo % Ii
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 61 - 61: iI11I1II1I1I + oo0oO00 * iiII11i1I1IIi - ooOoO0O00 % oo0oO00
 oOOo = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for III11I in oOOo :
  Ii1I11I = OOOO0OOoO0O0 + III11I + IIiiiiiiIi1I1
  iI1I1I = OOoOO0oo0ooO ( Ii1I11I )
  if iI1I1I != 'Failed' :
   i1ii1i1i1 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( iI1I1I )
   for iiI11ii1I1 , iIiiii , iiOOooooO0Oo , oOo0OOoO0 , O0OoooO0 , Ii11iiI in i1ii1i1i1 :
    if o00o in iiI11ii1I1 . lower ( ) :
     I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - Source Pandoras[/COLOR]' , iiOOooooO0Oo , Ii11iiI , oOo0OOoO0 , O0OoooO0 , iIiiii )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 9 - 9: O00OOo00oo0o - oO0o + iI11I1II1I1I % o0o00Oo0O + iiII11i1I1IIi + OOoOoo
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
     if 50 - 50: ooOoO0O00 + IIiIi1iI
     if 64 - 64: I11i % oo0oO00 . IIiIi1iI
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1Ii ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( oOO0OO0O ) . replace ( ' ' , '+' )
 if 39 - 39: O00OOo00oo0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 57 - 57: ii * ii - oOo0O0Ooo / O00OOo00oo0o * Ii1I - OOoOoo
 if I1 != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for iiOOooooO0Oo , iiI11ii1I1 in i1I :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    OoO ( ( iiI11ii1I1 + '[COLORblue] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + iiOOooooO0Oo ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 71 - 71: iI11I1II1I1I / Ii % I11i . O00OOo00oo0o * oOo0O0Ooo % IIiIiII11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
i1II1111 = '{ZH},' ; ooOOOo0 = '{IX},' ; i11111 = '{LM},'
if 84 - 84: I11i
def oOOOOooO ( url ) :
 IIiiiII = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IIiiiII )
 for url , iIIii , i11ii , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( ( iIIii ) . replace ( 'Sezon' , ' Season ' ) + ( i11ii ) . replace ( 'Bölüm' , ' Episode ' ) + iiI11ii1I1 , url , 8063 , '' )
  if 31 - 31: iIi1i1ii1 % I11i % O00OOo00oo0o . Ii1I / I11i * oo0oO00
  if 74 - 74: oOo0O0Ooo . IIiIi1iI / OooOO000 . OOoOoo
  if 74 - 74: I1ii11iIi11i / O00OOo00oo0o % O00OOo00oo0o . OOoOoo
  if 72 - 72: ooOoO0O00
def I1Iii11111I1iii ( url ) :
 IIiiiII = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( IIiiiII )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( iiI11ii1I1 , url , 222 , '' )
  if 67 - 67: Ii1I + oo0oO00 * OOoOoo / IIiIiII11i % oO0o % oO0o
  if 28 - 28: OOooOOo % oo0oO00 - IIi + IIi + oo0oO00 / iI11I1II1I1I
  if 91 - 91: oOo0O0Ooo / IIiIiII11i * IIi
  if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
def OOOo0Ooo0o00o ( ) :
 if 62 - 62: Ii1I . O00OOo00oo0o . iIi1i1ii1
 IIiiiII = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IIiiiII )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , i11ii in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 + '  -  ' + ( i11ii ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiOOooooO0Oo , 8063 , oOo0OOoO0 )
  if 19 - 19: Ii1I / O00OOo00oo0o
def IIiIIiiiiiII1 ( ) :
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 8002 , oOo0OOoO0 )
def iIi1i1II ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , time , url , iiI11ii1I1 , oOOoOOO0oo0 in IIIII11I1IiI :
  I1IIII1i ( '%s %s' % ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , time ) , url , 1015 , oOo0OOoO0 , oOOoOOO0oo0 )
  if 62 - 62: I1ii11iIi11i * iI11I1II1I1I
def iI11ii ( ) :
 if 63 - 63: oo0oO00 . O00OOo00oo0o * IIiIiII11i - oo0oO00
 oo000ii ( 'Coronation Street' , '' , 8001 , '' )
 oo000ii ( 'Eastenders' , '' , 8002 , '' )
 oo000ii ( 'Emmerdale' , '' , 8003 , '' )
 oo000ii ( 'Hollyoaks' , '' , 8004 , '' )
 oo000ii ( 'Im a Celebrity' , '' , 8005 , '' )
 if 45 - 45: oo0oO00 % IIiIi1iI + O00OOo00oo0o + I11i . I1ii11iIi11i
 if 15 - 15: IIiIi1iI / OOoOoo * Ii + OooOO000
 if 15 - 15: I11i % oO0o / OooOO000
 if 36 - 36: oO0o + oO0o % I1ii11iIi11i + I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
def iII1I1IIiiiI ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Holly' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iiOOooooO0Oo :
    OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 31 - 31: oo0oO00 % ooOoO0O00 . ii - I11i + ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 45 - 45: IIi + iiII11i1I1IIi / ii - iIi1i1ii1 + ii
def ii1i1I1111ii ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'East' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iiOOooooO0Oo :
    OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 87 - 87: OOoOoo
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: ii / OooOO000 / O00OOo00oo0o + OooOO000 - iiII11i1I1IIi + IIiIiII11i
def IiIIIiII1111 ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Emmer' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iiOOooooO0Oo :
    OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 67 - 67: oO0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 76 - 76: I1ii11iIi11i
def i1Oo000O000 ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Coro' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iiOOooooO0Oo :
    OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 7 - 7: oOo0O0Ooo
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 40 - 40: IIiIi1iI
def Oo00oO0o0Oo0o ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Celeb' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iiOOooooO0Oo :
    OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 29 - 29: OOooOOo * o0o00Oo0O * oOo0O0Ooo / oO0o
def i1IiIi1I1i ( name , url ) :
 Ii11I1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if Ii11I1 :
  OO00OO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OoO000O0Oo = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( OoO000O0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OoO000O0Oo = open_url ( url )
  IiIiIi11iiIi1 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( OoO000O0Oo ) [ - 1 ]
  OO00OO = IiIiIi11iiIi1 . replace ( '\\/' , '/' )
 ooOO00oOOo000 = xbmcgui . ListItem ( name , '' , '' )
 ooOO00oOOo000 . setPath ( OO00OO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , ooOO00oOOo000 )
 if 78 - 78: Ii . OOoOoo % ii - OOoOoo - OOoOoo + iIi1i1ii1
 if 11 - 11: iiII11i1I1IIi
def IioooooOOo0Oo ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iiOOooooO0Oo , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for iiOOooooO0Oo , iiI11ii1I1 in i1I :
  oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iiOOooooO0Oo , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 29 - 29: o0o00Oo0O * Ii / ii / I11i . IIiIi1iI
def OoIII ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Movies' in iiI11ii1I1 :
   oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( iiOOooooO0Oo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def OO00O ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0OOoO0 )
 for url in i1I :
  oo000ii ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 66 - 66: iIi1i1ii1 / o0o00Oo0O . iiII11i1I1IIi + OooOO000 - iIi1i1ii1 . iiII11i1I1IIi
  if 2 - 2: Ii1I . I1ii11iIi11i * IIi % IIiIiII11i . OooOO000
def iI1I ( url ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url , oOo0OOoO0 in IIIII11I1IiI :
  if '{{' in iiI11ii1I1 :
   pass
  else :
   oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOo0OOoO0 )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
II1i1iI = '{UJ},' ; iI111I1 = '{WE},' ; iIiii1IIi1I = '{WP},' ; IiIiii1IiI = '{PP},'
def oo0o0ooOoo00O ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url , oOo0OOoO0 in IIIII11I1IiI :
  if '{{' in iiI11ii1I1 :
   pass
  else :
   oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0OOoO0 )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI1ii1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  O0oOOo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0oOOo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 33 - 33: oOo0O0Ooo * O00OOo00oo0o
 if 98 - 98: Ii1I - ii / oOo0O0Ooo . IIiIi1iI - ooOoO0O00
 if 60 - 60: OOooOOo % OOooOOo
def I1Ii11iI11ii ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '(cooltvseries.com)' in iiI11ii1I1 :
   OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , iiI11ii1I1 in i1I :
  if '(cooltvseries.com)' in iiI11ii1I1 :
   OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def oOo0 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( ( url ) . replace ( ' ' , '%20' ) )
ii1II = '{XX},' ; OOo00o0o0O0oo = '{UD},' ; i1iI1iIII = '{YT},' ; oo0Oo = '{JS},' ; I1IiIIIIi1iiI = '{PF},'
if 57 - 57: iiII11i1I1IIi . o0o00Oo0O . ii . O00OOo00oo0o - iIi1i1ii1 / IIiIi1iI
def iIIIIIi11Ii ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  OoO ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( iiOOooooO0Oo ) ) , 222 , oOo0OOoO0 )
  if 92 - 92: oo0oO00 / Ii1I
def III1II111Ii1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  if 'youtu' in url :
   OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oOo0OOoO0 )
 for url in next :
  oo000ii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 6 - 6: Ii / ooOoO0O00 / OOoOoo . oOo0O0Ooo - IIi % Ii
def o0OoOoOo0O ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 37 - 37: ooOoO0O00 . O00OOo00oo0o - IIiIiII11i % I11i - ooOoO0O00 . oo0oO00
def iiiiIOoo000 ( url ) :
 OoO000O0Oo = O000oo
 IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOo0OOoO0 )
  if 21 - 21: OooOO000 % OOoOoo % I1ii11iIi11i % o0o00Oo0O
  if 63 - 63: IIiIiII11i * oOo0O0Ooo - ii / oOo0O0Ooo
  if 50 - 50: OOooOOo % iIi1i1ii1 + OOooOOo * iIi1i1ii1 - IIi
  if 94 - 94: iI11I1II1I1I
  if 1 - 1: o0o00Oo0O
def iIOOO ( ) :
 if 98 - 98: IIiIiII11i + IIiIiII11i - iI11I1II1I1I . OOooOOo . O00OOo00oo0o
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
 if 99 - 99: oo0oO00 . iIi1i1ii1 * O00OOo00oo0o * iI11I1II1I1I / OOooOOo % OOoOoo
 if 70 - 70: Ii1I . o0o00Oo0O
def oOoOOo ( Cat_Name ) :
 if 2 - 2: IIiIi1iI - iiII11i1I1IIi * ooOoO0O00 % IIi / ii * IIi
 OOO000ooO0OO = False
 OoOOOO00 = '0'
 if Cat_Name == 'All Channels' : OOO000ooO0OO = True
 if Cat_Name == 'Entertainment' : OoOOOO00 = '1'
 if Cat_Name == 'Movies' : OoOOOO00 = '2'
 if Cat_Name == 'Music' : OoOOOO00 = '3'
 if Cat_Name == 'News' : OoOOOO00 = '4'
 if Cat_Name == 'Sports' : OoOOOO00 = '5'
 if Cat_Name == 'Documentary' : OoOOOO00 = '6'
 if Cat_Name == 'Kids' : OoOOOO00 = '7'
 if Cat_Name == 'Food' : OoOOOO00 = '8'
 if Cat_Name == 'Religious' : OoOOOO00 = '9'
 if Cat_Name == 'USA Channels' : OoOOOO00 = '10'
 if Cat_Name == 'Other' : OoOOOO00 = '11'
 if 15 - 15: IIi * IIiIi1iI + IIiIiII11i . O00OOo00oo0o . oo0oO00
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 print 'Len Match: >>>' + str ( len ( IIIII11I1IiI ) )
 for iiI11ii1I1 , oOo0OOoO0 , I1I11iII11 in IIIII11I1IiI :
  O0O000OOOoO = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0OOoO0 ) . replace ( '\\' , '' )
  if I1I11iII11 == OoOOOO00 :
   oo000ii ( iiI11ii1I1 , '' , 7022 , O0O000OOOoO )
  elif OOO000ooO0OO == True :
   oo000ii ( iiI11ii1I1 , '' , 7022 , O0O000OOOoO )
  else : pass
  if 95 - 95: iIi1i1ii1 % oOo0O0Ooo + I1ii11iIi11i * I11i * OooOO000
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 22 - 22: iIi1i1ii1 + oo0oO00 . OOooOOo
def Oo0O ( Search_Name ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , iiOOooooO0Oo , o0O0O0ooo0oOO , oOOOOOoOO in IIIII11I1IiI :
  O0O000OOOoO = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0OOoO0 ) . replace ( '\\' , '' )
  OoO ( Search_Name + ': Link 1' , ( iiOOooooO0Oo ) . replace ( '\\' , '' ) , 222 , O0O000OOOoO )
  OoO ( Search_Name + ': Link 2' , ( o0O0O0ooo0oOO ) . replace ( '\\' , '' ) , 222 , O0O000OOOoO )
  OoO ( Search_Name + ': Link 3' , ( oOOOOOoOO ) . replace ( '\\' , '' ) , 222 , O0O000OOOoO )
  if 11 - 11: o0o00Oo0O
def o0Oo0o ( ) :
 OoO000O0Oo = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  OoO ( iiI11ii1I1 , ( iiOOooooO0Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def i1iioO0oOo ( ) :
 OoO000O0Oo = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  OoO ( iiI11ii1I1 , ( iiOOooooO0Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def IIiIiii ( ) :
 OoO000O0Oo = O000oo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  OoO ( iiI11ii1I1 , ( iiOOooooO0Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 71 - 71: I11i + IIi . I1ii11iIi11i - OOooOOo * Ii . OOooOOo
def oo000O0o ( url ) :
 url
 oOOOoo00 = xbmcgui . ListItem ( iiI11ii1I1 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOOoo00 )
 return
 if 99 - 99: oOo0O0Ooo
 if 78 - 78: oO0o / iI11I1II1I1I . iIi1i1ii1 * oO0o * OOooOOo - IIi
def IiI1I1iii ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OoO000O0Oo )
 for url , iIiiii , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , ( iIiiii ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  oo000ii ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 34 - 34: ii
def oo0000o ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , iIiiii , oOo0OOoO0 in IIIII11I1IiI :
  I1I11i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , iIiiii )
  i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 iI1ii111iiIii = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for i1iI11ii11 in iI1ii111iiIii :
  OooooOOoo0 = ( i1iI11ii11 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IIII1i ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , OooooOOoo0 )
  if 57 - 57: IIi + I11i . IIi
def ooOOoo0 ( INFO ) :
 iiIiI1i1 ( 'info for workout' , INFO )
 if 36 - 36: O00OOo00oo0o * iI11I1II1I1I * ii
 if 58 - 58: IIiIi1iI + IIiIiII11i + iIi1i1ii1 . ii
 if 42 - 42: iI11I1II1I1I / iiII11i1I1IIi . o0o00Oo0O . iIi1i1ii1
def Ii1i111iI ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( ( iiI11ii1I1 ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def iII1ii ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def OOO00OiI ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '=' in iiI11ii1I1 :
   pass
  else :
   OoO ( ( iiI11ii1I1 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def O0o00oO00O0 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '=' in iiI11ii1I1 :
   pass
  else :
   OoO ( iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 16 - 16: iIi1i1ii1 / Ii + o0o00Oo0O . OOoOoo
   if 15 - 15: I1ii11iIi11i + OooOO000 + oOo0O0Ooo * I11i
   if 33 - 33: I11i * I1ii11iIi11i
def O0OOOOoOOO ( url ) :
 OoO ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 OoO ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  OoO ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'bamf.png' )
  if 64 - 64: IIiIiII11i / IIiIiII11i
  if 52 - 52: O00OOo00oo0o * Ii1I
  if 35 - 35: I11i % oO0o
def i11i1i1II ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Daily' in iiI11ii1I1 :
   oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 9008 , Oo00OOOOO )
def Ii11Ii11 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def IiIiIIi ( url ) :
 OoO ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 OoO ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 OoO ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  OoO ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , Oo00OOOOO )
  if 61 - 61: OooOO000 * IIiIi1iI
def i1I1IiIiiI1II ( ) :
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if '.m3u' in iiOOooooO0Oo :
   oo000ii ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + iiOOooooO0Oo ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def iI1i ( url ) :
 OoO000O0Oo = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  OoO ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 85 - 85: IIiIiII11i - iIi1i1ii1
def I1i1iiiI1 ( ) :
 OoO000O0Oo = O000oo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'category' in iiOOooooO0Oo :
   oo000ii ( iiI11ii1I1 , 'http://www.disclose.tv/' + iiOOooooO0Oo , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 93 - 93: OOoOoo / Ii - oo0oO00 + oO0o / ooOoO0O00
   if 62 - 62: Ii1I / ii * oOo0O0Ooo - ooOoO0O00
def OO0oOOo0o ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , 'http://www.disclose.tv/' + url , 7011 , oOo0OOoO0 )
 for url in next :
  oo000ii ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 46 - 46: ii
  if 23 - 23: ooOoO0O00
def IIiii1I1I ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'http' in url :
   OoO ( 'video/flv' , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url , iiI11ii1I1 in i1I :
  OoO ( iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url in I1II1 :
  OoO ( 'YT Link' , url , 8043 , oOOOo00O00oOo + 'disclose.png' )
  if 62 - 62: IIiIiII11i - OOooOOo * iIi1i1ii1
  if 53 - 53: oo0oO00 + OooOO000
def oO0O0ooOoo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
  if 24 - 24: Ii + ooOoO0O00 * OOooOOo % OooOO000
def iI11iiiIi1II111I1i1 ( name , url , img ) :
 I1 = O000oo ( url )
 Iio0o0o = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1 )
 IiiIOoO00o0o0oo0o = len ( Iio0o0o )
 if 13 - 13: iiII11i1I1IIi % O00OOo00oo0o . ooOoO0O00
 if 1 - 1: I11i % I11i . iI11I1II1I1I . ii . OOoOoo . OooOO000
 if IiiIOoO00o0o0oo0o == 1 :
  for oooo in Iio0o0o :
   oooo = oooo . replace ( 'player' , 'watch' )
   OOi1IIII11II1 = oooo + '&fv=&sou='
   OOOO0oOO = O000oo ( OOi1IIII11II1 )
   IIIiii = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( OOOO0oOO )
   for Ooo0oo in IIIiii :
    I11OoooO = False
    Resolve ( Ooo0oo )
    if 49 - 49: OOoOoo + oO0o + o0o00Oo0O
 elif IiiIOoO00o0o0oo0o > 1 :
  if 95 - 95: IIiIiII11i * OOooOOo . IIi + Ii1I + I11i + OOooOOo
  for oooo in Iio0o0o :
   OOo0o0o = O000oo ( oooo )
   ooo0OOoo = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( OOo0o0o )
   oO0o00O = ooo0OOoo
   oO0o00O = ( str ( oO0o00O ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + oO0o00O
   OoO ( 'DOUBLE LINK' , oO0o00O , 424 , '' )
   if 7 - 7: I1ii11iIi11i * oO0o - IIiIiII11i % O00OOo00oo0o . I1ii11iIi11i . I1ii11iIi11i
   for url in ooo0OOoo :
    oo000ii ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     o0O0O0ooo0oOO = Google . resolve ( url )
    except :
     pass
    try :
     iiII1iIi1ii1i = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( o0O0O0ooo0oOO ) )
     for i11IiI1 , O0oO00oOO00O in iiII1iIi1ii1i :
      if 69 - 69: ooOoO0O00 % oO0o % O00OOo00oo0o / IIiIi1iI / IIiIi1iI
      HD_URLS . append ( i11IiI1 )
      SD_URLS . append ( O0oO00oOO00O )
    except :
     pass
 else :
  pass
  if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * IIiIi1iI
def iIIoooO0 ( ) :
 if 7 - 7: oO0o * OooOO000
 if 16 - 16: O00OOo00oo0o . ooOoO0O00 . OOoOoo
 oo000ii ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 50 - 50: oO0o - IIiIiII11i * ii - oOo0O0Ooo . o0o00Oo0O + o0o00Oo0O
 oo000ii ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 80 - 80: I11i
 if 50 - 50: IIiIi1iI
def Oooo0O00OOo0o ( ) :
 OoO000O0Oo = O000oo ( 'http://cnfstudio.com/' )
 IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , 'http://cnfstudio.com/genre/' + iiOOooooO0Oo , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 4 - 4: oo0oO00 * ii % I1ii11iIi11i / IIiIi1iI
OOooO0OOoo = xbmcgui . Dialog ( )
if 11 - 11: I11i - IIiIiII11i % oo0oO00 . IIiIiII11i
OO0 = '{UN},' ; I11IIi1I1 = '{IG},' ; Iiiii = '{PL},' ; IiIi1I1IiI1II1 = '{LO},' ; iii1iII1iii = '{LP},' ; o0O0o = '{HA},' ; OO0o0o = '{XD},' ; O0O0O00OoO0O = '{TA},' ; i1II11III = '{DP},' ; O0OO0oo = '{JT},' ; II111IiiIIi = '{JJ},' ; o0oo = '{MM},' ; oOOO00o0OOO00 = '{FQ},' ; oo0oOooo0 = '{HH},'
if 57 - 57: ooOoO0O00 - IIi
def Iii1iI1I1iii1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OoO000O0Oo )
 Ii111ii1 = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOo0OOoO0 )
 Ii111ii1 = Ii111ii1
 for url in Ii111ii1 :
  oo000ii ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 80 - 80: iI11I1II1I1I * iI11I1II1I1I + iIi1i1ii1 % iI11I1II1I1I + IIiIiII11i % o0o00Oo0O
def oo000O ( url ) :
 if 97 - 97: ii * I11i + ii % iIi1i1ii1 * I1ii11iIi11i
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  i1Oo00 = url + '&fv=&sou='
  i1Oo00 = i1Oo00 . replace ( 'player' , 'watch' )
  iiI1iiI11i1 = II1IIiiIiI11 ( i1Oo00 )
  o00o0OOooO00 = II1IIiiIiI11 ( url )
  if 35 - 35: OooOO000 . oOo0O0Ooo / IIiIiII11i % OOoOoo
  if 6 - 6: iI11I1II1I1I * IIiIiII11i
def II1IIiiIiI11 ( url ) :
 if 38 - 38: oOo0O0Ooo
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  o0oO0OoO0 ( url )
  if 42 - 42: I11i
  if 8 - 8: Ii / IIiIi1iI
def I1I1IiiI1ii1 ( ) :
 I1IIII1i ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , O0o0Oo , '' )
 if 24 - 24: Ii1I * I11i
def OO0oOo00 ( ) :
 if os . path . exists ( iiI1IiI ) :
  IIiii1I = open ( iiI1IiI , 'r' )
  for oOOOoo00 in IIiii1I :
   iIIiII1 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oOOOoo00 )
   for iiI11ii1I1 , iiOOooooO0Oo in iIIiII1 :
    OoO ( iiI11ii1I1 , iiOOooooO0Oo , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 9 - 9: Ii1I - OOoOoo
def o0o0 ( url ) :
 if os . path . exists ( Remote ) :
  I1 = oo00ooOoO00 ( url )
  IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for iiI11ii1I1 , url in IIIII11I1IiI :
   url = ( url ) . strip ( )
   OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 87 - 87: Ii * IIiIiII11i - iIi1i1ii1 % ii
  if 55 - 55: ooOoO0O00
def Iiii1i1 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + iiOOooooO0Oo
 iiI11ii1I1 = 'plugin.video.GenieTv'
 if 67 - 67: oOo0O0Ooo - oO0o
 Oo0oO ( iiOOooooO0Oo , iiI11ii1I1 )
 if 65 - 65: oO0o * IIiIiII11i / iI11I1II1I1I
def II1I ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + iiOOooooO0Oo
 iiI11ii1I1 = 'repository.GenieTv'
 if 19 - 19: IIi . Ii . iiII11i1I1IIi * iiII11i1I1IIi
 Oo0oO ( iiOOooooO0Oo , iiI11ii1I1 )
 if 69 - 69: ooOoO0O00
 if 96 - 96: iiII11i1I1IIi - Ii % ooOoO0O00 . iI11I1II1I1I
def OOOoo0OO ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  OoOO0OoOoO00 ( )
 if iI1i11iII111 == 1 :
  oOoOo000Ooooo ( )
  if 18 - 18: iIi1i1ii1 + OOooOOo . ooOoO0O00 / OOoOoo / OooOO000
  if 97 - 97: oO0o + iI11I1II1I1I
  if 79 - 79: IIiIi1iI + oo0oO00 - IIiIiII11i . I1ii11iIi11i
  if 26 - 26: OOoOoo
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
oo0o0o = 'https://addons.tvaddons.ag/'
if 25 - 25: OOoOoo * O00OOo00oo0o - oo0oO00 * Ii * oOo0O0Ooo * IIi
def oOoOo000Ooooo ( ) :
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 iio00 = 'https://addons.tvaddons.ag/search/?keyword=' + o00o
 I1 = O000oo ( iio00 )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , IIi1iiii1iI , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , 10054 , 'https://addons.tvaddons.ag/' + IIi1iiii1iI , O0o0Oo , '' )
  if 56 - 56: ii . oOo0O0Ooo . IIiIiII11i % OooOO000
  if 59 - 59: IIiIi1iI % I1ii11iIi11i - oo0oO00 + OOoOoo
def OoOO0OoOoO00 ( ) :
 I1 = O000oo ( oo0o0o )
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
   if 33 - 33: iIi1i1ii1 + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * OOoOoo
   if 21 - 21: o0o00Oo0O * IIiIi1iI % oO0o
def Addon ( url ) :
 I1 = O000oo ( url )
 Iii1I11i1IiiI = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'Please' in iiI11ii1I1 :
   pass
  else :
   I1I11i ( iiI11ii1I1 , url , 10054 , 'https://addons.tvaddons.ag/' + oOo0OOoO0 , O0o0Oo , '' )
 for url in Iii1I11i1IiiI :
  I1IIII1i ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
  if 75 - 75: OOooOOo / ii / iiII11i1I1IIi % OOooOOo * iIi1i1ii1 * OOoOoo
  if 11 - 11: Ii1I / IIi . iIi1i1ii1 * Ii1I
def II1i1iii1iiiI ( url , name ) :
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
   if 62 - 62: iiII11i1I1IIi
def Oo0oO ( url , name ) :
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
 if 73 - 73: iIi1i1ii1 % oO0o * IIi
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 84 - 84: I1ii11iIi11i
 if 18 - 18: ii
def oooii111I1I1I ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , IIi1iiii1iI , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , url , 1007 , IIi1iiii1iI )
def iIIiIi1IiI1 ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , IIi1iiii1iI , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , IIi1iiii1iI )
  if 80 - 80: IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % iiII11i1I1IIi . I11i
  if 86 - 86: oo0oO00 + OooOO000 % ii . OOoOoo
def IIi1IIIi ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , iconimage , iIiiii , O0OoooO0 , name in IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    iiIii1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
    for oOOOoo00 in iiIii1I :
     if oOOOoo00 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    OoO000Oo0oO ( name , url , 1016 , iconimage , O0OoooO0 , iIiiii )
   else :
    if 'youtube' in url :
     iiIii1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for oOOOoo00 in iiIii1I :
      if oOOOoo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i1iI1Ii11Ii1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , O0OoooO0 , iIiiii )
    else :
     iiIii1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for oOOOoo00 in iiIii1I :
      if oOOOoo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     i1iI1Ii11Ii1 ( name , url , 222 , iconimage , O0OoooO0 , iIiiii )
     i1Oo0oO00o ( 'movies' , 'INFO' )
  else :
   o0ooOooO0o ( url , iconimage , name )
   if 50 - 50: iIi1i1ii1 . o0o00Oo0O % oO0o . oo0oO00 + iIi1i1ii1 . OOooOOo
 else :
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
  for url , IIi1iiii1iI , name in IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     oo000ii ( name , url , 1016 , IIi1iiii1iI )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      OoO ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , IIi1iiii1iI )
     else :
      iiIii1I = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
      for oOOOoo00 in iiIii1I :
       if oOOOoo00 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      OoO ( name , url , 222 , IIi1iiii1iI )
      i1Oo0oO00o ( 'movies' , 'INFO' )
   else :
    o0ooOooO0o ( url , IIi1iiii1iI , name )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 69 - 69: Ii + Ii . Ii - Ii % iIi1i1ii1 / OooOO000
def o0ooOooO0o ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 o0o0o0O00o00Ooo = ( url ) . replace ( ooOOOo0 , 'http' ) . replace ( OOo00o0o0O0oo , '.com' ) ;
 I1IIi1iIiIiIiI = ( o0o0o0O00o00Ooo ) . replace ( i11111 , 'a' ) . replace ( oOO0 , 'b' ) . replace ( oOo , 'c' ) . replace ( iI111I1 , 'd' ) . replace ( Iiiii , 'e' ) . replace ( O0OO0oo , 'f' ) ;
 iIII = ( I1IIi1iIiIiIiI ) . replace ( ii1II , 'g' ) . replace ( o0O0o , 'h' ) . replace ( i1iI1iIII , 'i' ) . replace ( I1IiIIIIi1iiI , 'j' ) . replace ( oooO , 'k' ) . replace ( OO0oooOO , 'l' ) ;
 OOoooo = ( iIII ) . replace ( I11Ii1 , 'm' ) . replace ( oO0O , 'n' ) . replace ( OOOoooooO0oOOoO , 'o' ) . replace ( I1I1 , 'p' ) . replace ( oOoooo0OooO , 'q' ) . replace ( OooO0O , 'r' ) ;
 Oo0o = ( OOoooo ) . replace ( O0OO0OO , 's' ) . replace ( iIiii1IIi1I , 't' ) . replace ( I1i11i , 'u' ) . replace ( iiiI1I , 'v' ) . replace ( OOOOo0o0O0 , 'w' ) . replace ( I1I1i1 , 'x' ) ;
 Ii1Ii = ( Oo0o ) . replace ( iIIOOoOOooO , 'y' ) . replace ( i1111II1iIII , 'z' ) . replace ( OO0 , '.' ) . replace ( I11IIi1I1 , '(' ) . replace ( IiIi1I1IiI1II1 , ')' ) . replace ( iii1iII1iii , '/' ) ;
 I1ii11ii1iiI = ( Ii1Ii ) . replace ( i1II1111 , '1' ) . replace ( IiIiii1IiI , '2' ) . replace ( oO0oo0 , '3' ) . replace ( O0O0O00OoO0O , '4' ) . replace ( i1II11III , '5' ) . replace ( oo0Oo , '6' ) ;
 IiIiI1 = ( I1ii11ii1iiI ) . replace ( II111IiiIIi , '7' ) . replace ( o0oo , '8' ) . replace ( oOOO00o0OOO00 , '9' ) . replace ( oo0oOooo0 , '0' ) . replace ( o0OoOo0o0OOoO0 , ':' ) . replace ( i1I1IIIiii1 , '%' ) ;
 url = ( IiIiI1 ) . replace ( II1i1iI , '-' ) . replace ( OO0o0o , '_' ) ;
 OoO ( name , url , 222 , iconimage ) ;
 if 14 - 14: oOo0O0Ooo
 if 8 - 8: I11i
def ooOO0O0O ( ) :
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , IIi1iiii1iI , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , iiOOooooO0Oo , 1007 , IIi1iiii1iI )
def IIIiIIIi111iI ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , IIi1iiii1iI , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , IIi1iiii1iI )
  if 41 - 41: oo0oO00 % oOo0O0Ooo % I1ii11iIi11i + iIi1i1ii1 + Ii
def o0oiIiI1i1iiIi1i ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iiI1IIIi = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iiI1IIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiI1IIIi )
 if 18 - 18: I1ii11iIi11i * OooOO000
 if 51 - 51: OOooOOo - OooOO000
def OOOoOo ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if '-dir-' in iiI11ii1I1 :
   oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , oOo0OOoO0 )
  else :
   oo000ii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , oOo0OOoO0 )
   if 43 - 43: oo0oO00 * OooOO000 * IIiIi1iI / iI11I1II1I1I
def I11Ii111IIi ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 OoOoO0OooO00Oo = ( 'http://afewbitsmore.com/' )
 IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '[To Parent Directory]' in iiI11ii1I1 :
   iiI11ii1I1 = 'HOME'
   pass
  elif 'HOME' in iiI11ii1I1 :
   pass
  elif '.m3u' in iiI11ii1I1 :
   oo000ii ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , OoOoO0OooO00Oo + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in iiI11ii1I1 :
   OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , OoOoO0OooO00Oo + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in iiI11ii1I1 :
   OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , OoOoO0OooO00Oo + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , OoOoO0OooO00Oo + url , 1012 , oOOOo00O00oOo + 'music.png' )
def oO0OO00O0 ( url ) :
 I1 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 65 - 65: IIi % OOoOoo % I11i . iIi1i1ii1 . Ii1I
def OOo ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 OoOoO0OooO00Oo = url
 IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '.mp3' in iiI11ii1I1 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   oo000ii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '/' , '' ) , OoOoO0OooO00Oo + url , 1011 , oOOOo00O00oOo + 'music.png' )
def O0000o00 ( ) :
 OoO000O0Oo = oo00ooOoO00 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , ( 'http://www.cyn.net/music/' + iiOOooooO0Oo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOo0OOoO0 ) . replace ( ' ' , '%20' ) )
def III1iIiIiII ( url , img ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 o0O0O0ooo0oOO = url
 img = img
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( o0O0O0ooo0oOO + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 42 - 42: ii - Ii1I / ooOoO0O00 * oOo0O0Ooo - O00OOo00oo0o - IIi
def o0O0OO0o ( url ) :
 OoO000O0Oo = oo00ooOoO00 ( url )
 o0O0O0ooo0oOO = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for type , url , iiI11ii1I1 in IIIII11I1IiI :
  if '[VID]' in type :
   OoO ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , o0O0O0ooo0oOO + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   o0O0OO0o ( o0O0O0ooo0oOO + url )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: Ii1I - OooOO000 . Ii / oOo0O0Ooo
 if 41 - 41: O00OOo00oo0o * oO0o - OooOO000 . iIi1i1ii1
def OOoO0oo0O ( ) :
 IIIi1iiIIiiiI = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oOO0OO0O = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o00o = oOO0OO0O . lower ( )
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 o0O0O0ooo0oOO = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 oOOOOOoOO = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 41 - 41: iI11I1II1I1I - o0o00Oo0O - Ii1I - oo0oO00 + O00OOo00oo0o
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 iii1i1iiiiIi = OOoOO0oo0ooO ( o0O0O0ooo0oOO )
 Iiii = OOoOO0oo0ooO ( oOOOOOoOO )
 if 22 - 22: o0o00Oo0O % OOoOoo % OooOO000 % oOo0O0Ooo
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for iiI11ii1I1 in IIIII11I1IiI :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    oo000ii ( ( iiI11ii1I1 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiOOooooO0Oo + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 34 - 34: OooOO000 . I1ii11iIi11i % Ii1I . OooOO000 % OOoOoo / OOoOoo
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for iiI11ii1I1 in i1I :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    oo000ii ( ( iiI11ii1I1 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( o0O0O0ooo0oOO + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 84 - 84: iIi1i1ii1
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  I1II1 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii )
  for iiI11ii1I1 in I1II1 :
   if oOO0OO0O in iiI11ii1I1 . lower ( ) :
    oo000ii ( ( iiI11ii1I1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( oOOOOOoOO + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 1 - 1: oo0oO00 - I1ii11iIi11i * iI11I1II1I1I * I1ii11iIi11i * ooOoO0O00
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 9 - 9: OooOO000 - OooOO000
    if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + oo0oO00
    if 20 - 20: oO0o + iiII11i1I1IIi . IIiIiII11i / Ii
    if 50 - 50: ii / oO0o % iI11I1II1I1I
    if 41 - 41: Ii1I % Ii1I + OOoOoo . OooOO000 % O00OOo00oo0o * IIiIi1iI
    if 57 - 57: iIi1i1ii1 . O00OOo00oo0o . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
I11Ii1 = '{SF},' ; oO0O = '{IF},' ; OOOoooooO0oOOoO = '{PW},' ; oO0oo0 = '{AM},' ; I1I1 = '{GF},' ; oOoooo0OooO = '{DD},' ; OooO0O = '{UO},' ; O0OO0OO = '{LE},' ; I1i11i = '{ZY},' ; iiiI1I = '{UE},' ; OOOOo0o0O0 = '{PE},' ; I1I1i1 = '{JE},' ; iIIOOoOOooO = '{TH},' ; i1111II1iIII = '{LK},'
if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
if 93 - 93: IIiIi1iI / IIi * o0o00Oo0O
def i1iI1 ( ) :
 OoO000O0Oo = O000oo ( 'http://www.iwatchseries.me/tv-list/' )
 IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , iiOOooooO0Oo , 8021 , oOOOo00O00oOo + 'iwatch.png' )
def iI11 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , OO0oo0O0OOO0 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 + OO0oo0O0OOO0 , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def i1IiI1Ii ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  OOo0 ( url )
def OOo0 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( 'VidSpot - ' + iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url in i1I :
  OoO ( 'VodLocker' , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for iiI11ii1I1 , url in I1II1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   OoO ( 'TheVideo - ' + iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
   if 30 - 30: OooOO000
def iIOO000O ( ) :
 OoO000O0Oo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , iiOOooooO0Oo , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 52 - 52: OooOO000 . OOoOoo - Ii1I * iI11I1II1I1I % I11i / IIiIi1iI
  if 18 - 18: OOooOOo % oo0oO00 % oO0o / OooOO000
def O0o0ooo00o0O ( ) :
 OoO000O0Oo = O000oo ( 'http://www.animetoon.org/cartoon' )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , iiOOooooO0Oo , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 72 - 72: IIiIi1iI % iiII11i1I1IIi + oO0o
  if 94 - 94: iIi1i1ii1 + iI11I1II1I1I
  if 80 - 80: I11i . OooOO000 . ii
def o00o000Oo ( url ) :
 OoO000O0Oo = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 in i1I :
  O0oO00oOOooO = oOo0OOoO0
 I1II1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1II1 :
  oo000ii ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  oo000ii ( iiI11ii1I1 , url , 1003 , O0oO00oOOooO )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIiIIIiI1iII ( url , IMAGE ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  print iiI11ii1I1 + '     ' + url
  if 'easy' in url :
   IiooO0O ( url )
  elif 'playpanda' in url :
   IiooO0O ( url )
   if 55 - 55: IIi - IIiIiII11i - OOoOoo . iiII11i1I1IIi + oo0oO00 - oo0oO00
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiooO0O ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  OoO ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 29 - 29: OOooOOo - O00OOo00oo0o % IIi
  if 45 - 45: OOoOoo / I1ii11iIi11i + ii
def OOIiI1IIIiI1I1i ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0o0O00Oo0o0 . add_header ( 'referer' , url )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 84 - 84: OOooOOo - iiII11i1I1IIi
def oo00ooOoO00 ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 80 - 80: Ii % IIi - I1ii11iIi11i % IIi
def O0O0oOo0o0o0 ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iii1IiI1i = ( '%s%s' % ( OooO0ooO0o0 , url ) )
 i1Oo00 = oo00ooOoO00 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , IIi1iiii1iI , iiI11ii1I1 in IIIII11I1IiI :
  OoO ( '%s' % ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , IIi1iiii1iI )
  if 86 - 86: I11i / OOooOOo
def o0oO0OoO0 ( url ) :
 if 40 - 40: OooOO000
 i1I11iIiII = open ( oOOoo0Oo , "a" )
 i1I11iIiII . write ( 'url="' + url + '"\n' )
 i1I11iIiII . close
 if 62 - 62: IIiIi1iI / IIi
 IiI1iii11iIi1 = xbmc . Player ( i1iI11I1II1 ( ) )
 import urlresolver
 try : IiI1iii11iIi1 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iiI11ii1I1 ) )
 IiI1iii11iIi1 = xbmc . Player ( i1iI11I1II1 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  OOooO0OOoo = xbmcgui . Dialog ( )
  if OOooO0OOoo . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   OOooO0OOoo . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : IiI1iii11iIi1 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def O0o0O0OoOo0 ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  oooOO0oo0Oo00 = '.mp4'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   o0oO0OoO0 ( url )
  if iI1i11iII111 == 1 :
   o00o0O0o0o0 ( url , name , oooOO0oo0Oo00 )
 elif '.mkv' in url :
  oooOO0oo0Oo00 = '.mkv'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   o0oO0OoO0 ( url )
  if iI1i11iII111 == 1 :
   o00o0O0o0o0 ( url , name , oooOO0oo0Oo00 )
 elif '.mp3' in url :
  oooOO0oo0Oo00 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   o0oO0OoO0 ( url )
  if iI1i11iII111 == 1 :
   o00o0O0o0o0 ( url , name , oooOO0oo0Oo00 )
 elif '.avi' in url :
  oooOO0oo0Oo00 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   o0oO0OoO0 ( url )
  if iI1i11iII111 == 1 :
   o00o0O0o0o0 ( url , name , oooOO0oo0Oo00 )
 elif '.mov' in url :
  oooOO0oo0Oo00 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   o0oO0OoO0 ( url )
  if iI1i11iII111 == 1 :
   o00o0O0o0o0 ( url , name , oooOO0oo0Oo00 )
 elif '.mpeg' in url :
  oooOO0oo0Oo00 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   o0oO0OoO0 ( url )
  if iI1i11iII111 == 1 :
   o00o0O0o0o0 ( url , name , oooOO0oo0Oo00 )
 elif '.mpg' in url :
  oooOO0oo0Oo00 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   o0oO0OoO0 ( url )
  if iI1i11iII111 == 1 :
   o00o0O0o0o0 ( url , name , oooOO0oo0Oo00 )
 elif '.flv' in url :
  oooOO0oo0Oo00 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   o0oO0OoO0 ( url )
  if iI1i11iII111 == 1 :
   o00o0O0o0o0 ( url , name , oooOO0oo0Oo00 )
 else :
  o0oO0OoO0 ( url )
def o00o0O0o0o0 ( url , name , cat ) :
 Ii11i1IiII ( )
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
def Ii11i1IiII ( ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def OooO00oo ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iiI11ii1I1 )
 xbmc . sleep ( 1 )
 IiI1iii11iIi1 = xbmc . Player ( i1iI11I1II1 ( ) )
 o0oOoO00o . update ( 100 , '%s' % iiI11ii1I1 )
 xbmc . sleep ( 1 )
 IiI1iii11iIi1 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 63 - 63: IIi
def iii1 ( url ) :
 IiI1iii11iIi1 = xbmc . Player ( i1iI11I1II1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : IiI1iii11iIi1 . play ( url ) . strip ( )
 except : pass
 if 52 - 52: iI11I1II1I1I * OOooOOo + I11i . iiII11i1I1IIi
def o0iIiii ( url ) :
 IiI1iii11iIi1 = xbmc . Player ( i1iI11I1II1 ( ) )
 import urlresolver
 o0O0OoO0o0o0 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 IiI1iii11iIi1 . play ( o0O0OoO0o0o0 )
 xbmc . sleep ( 1 )
 IiI1iii11iIi1 . play ( url )
 if 70 - 70: IIiIi1iI . Ii % OOooOOo + oo0oO00
 if 95 - 95: Ii1I
def i1iI11I1II1 ( ) :
 try :
  iiIii1I1Ii = getSet ( "core-player" )
  if ( iiIii1I1Ii == 'DVDPLAYER' ) : i1Iii1I1IIi = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( iiIii1I1Ii == 'MPLAYER' ) : i1Iii1I1IIi = xbmc . PLAYER_CORE_MPLAYER
  elif ( iiIii1I1Ii == 'PAPLAYER' ) : i1Iii1I1IIi = xbmc . PLAYER_CORE_PAPLAYER
  else : i1Iii1I1IIi = xbmc . PLAYER_CORE_AUTO
 except : i1Iii1I1IIi = xbmc . PLAYER_CORE_AUTO
 return i1Iii1I1IIi
 return True
 if 17 - 17: oOo0O0Ooo + IIi % I11i
def oo000ii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iii1I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOOOooO0oO00O0o = True
 ooOO00oOOo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO00oOOo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIii11II11II1 = [ ]
  IIii11II11II1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIii11II11II1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIii11II11II1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooOO00oOOo000 . addContextMenuItems ( IIii11II11II1 )
 OOOOooO0oO00O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1I1i , listitem = ooOO00oOOo000 , isFolder = True )
 return OOOOooO0oO00O0o
 if 34 - 34: iIi1i1ii1 * iiII11i1I1IIi / ii - iI11I1II1I1I
def IIiii11ii1i ( name , url , mode , iconimage , fanart , description ) :
 if 96 - 96: OooOO000 * oOo0O0Ooo + OOoOoo . Ii * I1ii11iIi11i % ooOoO0O00
 iii1I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOOOooO0oO00O0o = True
 ooOO00oOOo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO00oOOo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO00oOOo000 . setProperty ( "Fanart_Image" , fanart )
 OOOOooO0oO00O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1I1i , listitem = ooOO00oOOo000 , isFolder = True )
 return OOOOooO0oO00O0o
 if 65 - 65: iI11I1II1I1I * OOoOoo
def OoO ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 iii1I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOOOooO0oO00O0o = True
 ooOO00oOOo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO00oOOo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  IIii11II11II1 = [ ]
  IIii11II11II1 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   IIii11II11II1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIii11II11II1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  ooOO00oOOo000 . addContextMenuItems ( IIii11II11II1 )
 OOOOooO0oO00O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1I1i , listitem = ooOO00oOOo000 , isFolder = False )
 return OOOOooO0oO00O0o
 if 89 - 89: OOoOoo % Ii . Ii + oo0oO00 / Ii1I
 if 19 - 19: oOo0O0Ooo
 if 86 - 86: Ii1I + OOooOOo * OOoOoo + IIiIi1iI
 if 23 - 23: oO0o - oo0oO00 * iI11I1II1I1I
 if 1 - 1: iiII11i1I1IIi - I1ii11iIi11i / ooOoO0O00
 if 96 - 96: ii % OooOO000 - ii % o0o00Oo0O
def iiIiI1i1 ( heading , announce ) :
 class iiiiIiiiii1I ( ) :
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
   try : OOoO = open ( announce ) ; I1i11II11i = OOoO . read ( )
   except : I1i11II11i = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( I1i11II11i ) )
   return
 iiiiIiiiii1I ( )
 iiiiIiiiii1I ( )
 if 3 - 3: OOooOOo
def OO0Oooo0oOO0O ( ) :
 iiIiI1i1 ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 52 - 52: OOooOOo
 if 79 - 79: oOo0O0Ooo + I1ii11iIi11i % OOooOOo - OOoOoo + oOo0O0Ooo * oo0oO00
 if 52 - 52: OOooOOo % Ii1I * I1ii11iIi11i % ii - oO0o
 if 13 - 13: IIi . iIi1i1ii1 / iiII11i1I1IIi
 if 93 - 93: IIiIi1iI * oOo0O0Ooo * Ii1I / Ii1I
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 62 - 62: IIiIi1iI * iIi1i1ii1 % Ii1I - ooOoO0O00 - Ii1I
 if 24 - 24: IIi
 if 71 - 71: OOoOoo - ooOoO0O00
 if 56 - 56: OOooOOo + oo0oO00
 if 74 - 74: OooOO000 / O00OOo00oo0o / IIiIiII11i - OooOO000 / oo0oO00 % iiII11i1I1IIi
 if 19 - 19: OOoOoo % ii + ii
 if 7 - 7: ooOoO0O00
 if 91 - 91: OOooOOo - OOooOOo . OOoOoo
 if 33 - 33: O00OOo00oo0o - iI11I1II1I1I / iIi1i1ii1 % o0o00Oo0O
 if 80 - 80: OOoOoo % ii - OOoOoo
 if 27 - 27: O00OOo00oo0o - I11i * Ii1I - oOo0O0Ooo
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - OooOO000 . iIi1i1ii1
 if 100 - 100: IIiIiII11i / O00OOo00oo0o / OooOO000 - Ii1I * iI11I1II1I1I
 if 7 - 7: ooOoO0O00 . OOoOoo % Ii * Ii1I . iiII11i1I1IIi % Ii1I
 if 35 - 35: oOo0O0Ooo
 if 48 - 48: ii % ii - oO0o . OOooOOo
 if 22 - 22: IIiIi1iI . Ii . ii . ooOoO0O00
 if 12 - 12: OOooOOo % IIi + oo0oO00 . o0o00Oo0O % iI11I1II1I1I
 if 41 - 41: ii
 if 13 - 13: iiII11i1I1IIi + O00OOo00oo0o - O00OOo00oo0o % oo0oO00 / iiII11i1I1IIi
 if 4 - 4: oOo0O0Ooo + IIi - OOoOoo + OooOO000
 if 78 - 78: iIi1i1ii1
 if 29 - 29: IIiIiII11i
 if 79 - 79: iI11I1II1I1I - Ii + IIiIi1iI - IIiIiII11i . iI11I1II1I1I
def OO000o0O0o ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + O0OiiiIIiIi1ii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 78 - 78: IIiIi1iI
def oooOoO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + II1iiiiI1Ii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 69 - 69: iiII11i1I1IIi / ooOoO0O00 / oo0oO00 . O00OOo00oo0o
def iII1iiI11IIi ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + i1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 44 - 44: Ii1I
def Ooo00OoO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + oOOOOoo000Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 46 - 46: ooOoO0O00 + o0o00Oo0O
def IIii1i ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + ooOOOOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 3 - 3: Ii
def IiI11IiII1iI ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OOo0OOooO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 80 - 80: Ii1I
def ooOOO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o00Oooo0o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 5 - 5: OooOO000 - OooOO000 / O00OOo00oo0o % I1ii11iIi11i
def OOoO00OOo ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 5 - 5: ooOoO0O00 / oOo0O0Ooo / ii
def OOO00Oo00o ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + IiII1Iiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 16 - 16: OooOO000 . o0o00Oo0O - O00OOo00oo0o * O00OOo00oo0o
def iI1Ii11iIiI1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o0OO00Ooo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 97 - 97: oo0oO00 - O00OOo00oo0o * OooOO000 - IIiIi1iI * O00OOo00oo0o
 if 90 - 90: iIi1i1ii1 . OOooOOo
 if 89 - 89: O00OOo00oo0o - oO0o - I11i
 if 44 - 44: ii
 if 82 - 82: OOooOOo . OOooOOo
 if 10 - 10: I1ii11iIi11i * Ii1I . oo0oO00 . ii . IIi * Ii1I
 if 80 - 80: O00OOo00oo0o + iiII11i1I1IIi . O00OOo00oo0o + IIi
 if 85 - 85: Ii . iiII11i1I1IIi + iIi1i1ii1 / iIi1i1ii1
 if 43 - 43: OOoOoo . ii - IIiIiII11i
def iI1iIiiiI1I1 ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for I1III1I11Iii , iII , ooO0o0O0Oo in os . walk ( iIi1ii1I1 ) :
     OoOo0O0O = 0
     OoOo0O0O += len ( ooO0o0O0Oo )
     if OoOo0O0O > 0 :
      for OOoO in ooO0o0O0Oo :
       os . unlink ( os . path . join ( I1III1I11Iii , OOoO ) )
  o000oOOoo = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( o000oOOoo )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 62 - 62: OOooOOo
 if 32 - 32: Ii
 if 57 - 57: iI11I1II1I1I
 if 99 - 99: OooOO000 % I11i + iI11I1II1I1I
 if 51 - 51: ooOoO0O00 % I11i - oo0oO00 - OOoOoo
 if 14 - 14: IIiIi1iI + iIi1i1ii1
 if 45 - 45: oo0oO00 + IIiIiII11i . OooOO000 / Ii1I
 if 76 - 76: iIi1i1ii1 + OooOO000 - OOoOoo * iI11I1II1I1I % ooOoO0O00
def oOo00oII111i1ii1iII ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 72 - 72: IIiIi1iI + IIiIiII11i . o0o00Oo0O - OooOO000 / ii . O00OOo00oo0o
def o00o0 ( url ) :
 iiiiiiI = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 iI111iiI1II = [
 ( iiiiiiI ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( iiiiiiI , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( iiiiiiI , 'plugin.video.itv' , 'Images' ) ) ]
 if 96 - 96: OOooOOo * o0o00Oo0O - IIiIiII11i . IIiIi1iI - iIi1i1ii1
 OO0OOO0o0OOO0 = 0
 if 39 - 39: o0o00Oo0O * oOo0O0Ooo
 for oOOOoo00 in iI111iiI1II :
  if os . path . exists ( oOOOoo00 ) and not oOOOoo00 in [ oO0o0o0ooO0oO , iiiiiiI ] :
   for I1III1I11Iii , iII , ooO0o0O0Oo in os . walk ( oOOOoo00 ) :
    OoOo0O0O = 0
    OoOo0O0O += len ( ooO0o0O0Oo )
    if OoOo0O0O > 0 :
     for OOoO in ooO0o0O0Oo :
      if not OOoO in oooOOOOO :
       try :
        os . unlink ( os . path . join ( I1III1I11Iii , OOoO ) )
       except :
        pass
      else : OOO ( 'Ignore Log File: %s' % OOoO )
     for O00o0O in iII :
      try :
       shutil . rmtree ( os . path . join ( I1III1I11Iii , O00o0O ) )
       OO0OOO0o0OOO0 += 1
       OOO ( "[Success] cleared %s files from %s" % ( str ( OoOo0O0O ) , os . path . join ( oOOOoo00 , O00o0O ) ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( oOOOoo00 , O00o0O ) )
  else :
   for I1III1I11Iii , iII , ooO0o0O0Oo in os . walk ( oOOOoo00 ) :
    for O00o0O in iII :
     if 'cache' in O00o0O . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( I1III1I11Iii , O00o0O ) )
       OO0OOO0o0OOO0 += 1
       OOO ( "[Success] wiped %s " % os . path . join ( oOOOoo00 , O00o0O ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( oOOOoo00 , O00o0O ) )
       if 27 - 27: iI11I1II1I1I - oo0oO00
 oOo00oII111i1ii1iII ( oO , 'Clear Cache: Removed %s Files' % OO0OOO0o0OOO0 )
 if 73 - 73: IIi . I1ii11iIi11i + I1ii11iIi11i % I1ii11iIi11i % o0o00Oo0O
 if 8 - 8: OooOO000 . iIi1i1ii1 - ooOoO0O00 % oO0o / iiII11i1I1IIi
 if 13 - 13: I1ii11iIi11i / OOooOOo . Ii1I . IIi
 if 31 - 31: I11i
 if 59 - 59: I1ii11iIi11i / I1ii11iIi11i
 if 87 - 87: Ii1I % OOooOOo + iIi1i1ii1 . Ii / iIi1i1ii1
 if 32 - 32: iIi1i1ii1 + OOoOoo + Ii1I
def O0Oo0 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oo00o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1III1I11Iii , iII , ooO0o0O0Oo in os . walk ( oo00o ) :
   OoOo0O0O = 0
   OoOo0O0O += len ( ooO0o0O0Oo )
   if 14 - 14: iIi1i1ii1 + iIi1i1ii1 * ii * iiII11i1I1IIi + I1ii11iIi11i . oOo0O0Ooo
   if 61 - 61: IIi . IIi
   if OoOo0O0O > 0 :
    if 17 - 17: IIiIiII11i / IIiIi1iI
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( OoOo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 80 - 80: IIi * oO0o + iIi1i1ii1
     for OOoO in ooO0o0O0Oo :
      os . unlink ( os . path . join ( I1III1I11Iii , OOoO ) )
     for O00o0O in iII :
      shutil . rmtree ( os . path . join ( I1III1I11Iii , O00o0O ) )
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
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
 if 98 - 98: I11i * I1ii11iIi11i - iIi1i1ii1 . IIiIi1iI
 if 2 - 2: I1ii11iIi11i - IIiIi1iI % iI11I1II1I1I
 if 88 - 88: O00OOo00oo0o - oO0o
 if 79 - 79: OooOO000
 if 45 - 45: IIiIiII11i + OooOO000 . iiII11i1I1IIi . o0o00Oo0O * ooOoO0O00 - iIi1i1ii1
 if 48 - 48: Ii1I + I1ii11iIi11i
 if 76 - 76: Ii1I
 if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . iIi1i1ii1
def O0O0ooOOO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oo00o = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for I1III1I11Iii , iII , ooO0o0O0Oo in os . walk ( oo00o ) :
   OoOo0O0O = 0
   OoOo0O0O += len ( ooO0o0O0Oo )
   if 51 - 51: iIi1i1ii1 + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
   if 20 - 20: O00OOo00oo0o . iiII11i1I1IIi . iIi1i1ii1 + iiII11i1I1IIi - IIi * oo0oO00
   if OoOo0O0O > 0 :
    if 82 - 82: oO0o
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( OoOo0O0O ) + " files found" , "Do you want to delete them?" ) :
     if 78 - 78: IIiIiII11i / iiII11i1I1IIi - Ii + Ii1I * I1ii11iIi11i
     for OOoO in ooO0o0O0Oo :
      os . unlink ( os . path . join ( I1III1I11Iii , OOoO ) )
     for O00o0O in iII :
      shutil . rmtree ( os . path . join ( I1III1I11Iii , O00o0O ) )
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
 if 17 - 17: OOooOOo
 if 72 - 72: OooOO000 . I1ii11iIi11i - Ii / oOo0O0Ooo
 if 64 - 64: oo0oO00
 if 80 - 80: I11i % iI11I1II1I1I
 if 63 - 63: OOoOoo * Ii
 if 86 - 86: iiII11i1I1IIi % iiII11i1I1IIi - OOooOOo + O00OOo00oo0o / oOo0O0Ooo * ii
 if 26 - 26: IIiIiII11i * OooOO000 + I11i / o0o00Oo0O + ooOoO0O00 - iiII11i1I1IIi
 if 56 - 56: IIi
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + OOoOoo - iiII11i1I1IIi
 if 81 - 81: Ii1I + ii - IIi * o0o00Oo0O
def ooOoOoOo ( url , name ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1Iii11II = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 ii11III1 = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml.bak' )
 if os . path . exists ( ii11III1 ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   I1Iii11II = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
   try :
    os . remove ( I1Iii11II )
    print '=== GenieTv - REMOVING    ' + str ( I1Iii11II ) + '    ==='
   except :
    pass
   i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
   i1IIi1i1Ii1 = open ( I1Iii11II , "w" )
   i1IIi1i1Ii1 . write ( i1Oo00 )
   i1IIi1i1Ii1 . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( I1Iii11II ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  I1Iii11II = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
  try :
   os . remove ( I1Iii11II )
   print '=== GenieTv - REMOVING    ' + str ( I1Iii11II ) + '    ==='
  except :
   pass
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  i1IIi1i1Ii1 = open ( I1Iii11II , "w" )
  i1IIi1i1Ii1 . write ( i1Oo00 )
  i1IIi1i1Ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1Iii11II ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 95 - 95: I11i * Ii - O00OOo00oo0o - ii
def IioOOo0OO0O0 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1Iii11II = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
 try :
  i1IIi1i1Ii1 = open ( I1Iii11II ) . read ( )
  if 'zero' in i1IIi1i1Ii1 :
   name = '0CACHE'
  elif 'tuxen' in i1IIi1i1Ii1 :
   name = 'TUXENS'
  elif 'muckys' in i1IIi1i1Ii1 :
   name = 'MUCKYS'
  elif 'p2p1' in i1IIi1i1Ii1 :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in i1IIi1i1Ii1 :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in i1IIi1i1Ii1 :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 49 - 49: o0o00Oo0O . I1ii11iIi11i / iIi1i1ii1
def II1IooOO00Oo ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1Iii11II = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
 try :
  os . remove ( I1Iii11II )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( I1Iii11II ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 31 - 31: OooOO000 - Ii % iIi1i1ii1 / OooOO000 . ii + I1ii11iIi11i
 if 82 - 82: Ii1I * o0o00Oo0O + IIi . IIiIi1iI + oO0o % o0o00Oo0O
 if 2 - 2: IIiIiII11i * o0o00Oo0O . IIiIi1iI * ooOoO0O00
 if 29 - 29: iI11I1II1I1I - O00OOo00oo0o - iIi1i1ii1 - I11i + Ii
 if 78 - 78: I11i + iI11I1II1I1I / Ii1I - ii - oo0oO00
 if 79 - 79: Ii1I - oo0oO00 - I11i . IIi
 if 65 - 65: Ii . oO0o % OooOO000 + OOoOoo - Ii
 if 60 - 60: O00OOo00oo0o
 if 14 - 14: I1ii11iIi11i % oo0oO00 * OooOO000 - Ii / Ii1I * Ii
 if 95 - 95: iI11I1II1I1I + OOooOOo . oOo0O0Ooo + OOooOOo * iiII11i1I1IIi + IIi
def OOooO0OO0 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for i1i11IiII , oo0Oo00o0oo0OoO , oo0o0O00o0o , II1Iii1IiiIi in IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % i1i11IiII , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oo0o0O00o0o , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % II1Iii1IiiIi )
  inc = inc + 1
  if 73 - 73: o0o00Oo0O . O00OOo00oo0o - ii % iiII11i1I1IIi % ooOoO0O00
  if 14 - 14: O00OOo00oo0o + iIi1i1ii1 * I1ii11iIi11i
  if 49 - 49: I1ii11iIi11i
  if 57 - 57: o0o00Oo0O * IIiIi1iI - OooOO000 - iI11I1II1I1I * OooOO000
  if 9 - 9: OOoOoo . iiII11i1I1IIi
  if 23 - 23: o0o00Oo0O % ii - o0o00Oo0O . oOo0O0Ooo + Ii
  if 96 - 96: IIiIi1iI % o0o00Oo0O
  if 51 - 51: oOo0O0Ooo - OooOO000 / Ii1I . Ii1I + Ii1I
  if 87 - 87: IIiIiII11i . iIi1i1ii1 * oO0o
def OOoO00o00oo ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I1Iii11II = os . path . join ( oOO0O00Oo0O0o , 'addons2.ini' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  i1IIi1i1Ii1 = open ( I1Iii11II , "w" )
  i1IIi1i1Ii1 . write ( i1Oo00 )
  i1IIi1i1Ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1Iii11II ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 5 - 5: oo0oO00 - ii / OOooOOo
def I1II1i1iIIi ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I1Iii11II = os . path . join ( oOO0O00Oo0O0o , 'settings.xml' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  i1IIi1i1Ii1 = open ( I1Iii11II , "w" )
  i1IIi1i1Ii1 . write ( i1Oo00 )
  i1IIi1i1Ii1 . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1Iii11II ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 55 - 55: oO0o
 if 20 - 20: IIiIi1iI * O00OOo00oo0o * I11i - IIiIi1iI
def i1I1IiiIIIiiI ( ) :
 try :
  oOoo0O = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( oOoo0O ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    ooO00OO0ooo = os . path . join ( oOoo0O , "source.db" )
    os . unlink ( ooO00OO0ooo )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 78 - 78: IIiIi1iI . oOo0O0Ooo . O00OOo00oo0o / o0o00Oo0O % ii % Ii
 if 72 - 72: OooOO000 / IIi * o0o00Oo0O
 if 18 - 18: o0o00Oo0O
 if 14 - 14: iIi1i1ii1 / OOoOoo - o0o00Oo0O
 if 16 - 16: O00OOo00oo0o % iI11I1II1I1I . ooOoO0O00
def O000oo ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 72 - 72: IIiIi1iI * IIi
 if 69 - 69: oo0oO00 - Ii
 if 29 - 29: iIi1i1ii1 + OooOO000 % Ii1I + iiII11i1I1IIi * I1ii11iIi11i - Ii
 if 24 - 24: Ii . IIiIi1iI + IIiIi1iI - Ii % IIi
 if 58 - 58: oOo0O0Ooo
 if 94 - 94: I11i + iIi1i1ii1 % I11i . O00OOo00oo0o - IIiIi1iI * oOo0O0Ooo
 if 62 - 62: I1ii11iIi11i * ooOoO0O00 % Ii1I + I1ii11iIi11i . o0o00Oo0O . IIiIi1iI
def IiIIi1 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; OOO00oO0O = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if OOO00oO0O :
  IIi1 = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; IIi1 = xbmc . translatePath ( IIi1 ) ;
  OOoO0OooO = os . path . join ( IIi1 , ".." , ".." ) ; OOoO0OooO = os . path . abspath ( OOoO0OooO ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + OOoO0OooO ) ; IiiOo = False
  try :
   for I1III1I11Iii , iII , ooO0o0O0Oo in os . walk ( OOoO0OooO , topdown = True ) :
    iII [ : ] = [ O00o0O for O00o0O in iII if O00o0O not in o0oO0 ]
    for iiI11ii1I1 in ooO0o0O0Oo :
     try : os . remove ( os . path . join ( I1III1I11Iii , iiI11ii1I1 ) )
     except :
      if iiI11ii1I1 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IiiOo = True
      plugintools . log ( "Error removing " + I1III1I11Iii + " " + iiI11ii1I1 )
    for iiI11ii1I1 in iII :
     try : os . rmdir ( os . path . join ( I1III1I11Iii , iiI11ii1I1 ) )
     except :
      if iiI11ii1I1 not in [ "Database" , "userdata" ] : IiiOo = True
      plugintools . log ( "Error removing " + I1III1I11Iii + " " + iiI11ii1I1 )
   if not IiiOo : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oO0oI1I1 ( )
 if 38 - 38: ii * iI11I1II1I1I
 if 54 - 54: ii . O00OOo00oo0o
 if 71 - 71: iIi1i1ii1
def I1iI1Ii1I1Iii1 ( ) :
 ii1iOO00O0O00oOOO = [ ]
 ii1111iIIiIIi = sys . argv [ 2 ]
 if len ( ii1111iIIiIIi ) >= 2 :
  IIIIiii1IIii = sys . argv [ 2 ]
  ooOo0Oo = IIIIiii1IIii . replace ( '?' , '' )
  if ( IIIIiii1IIii [ len ( IIIIiii1IIii ) - 1 ] == '/' ) :
   IIIIiii1IIii = IIIIiii1IIii [ 0 : len ( IIIIiii1IIii ) - 2 ]
  I11i1I111II1IiI = ooOo0Oo . split ( '&' )
  ii1iOO00O0O00oOOO = { }
  for OOO00000o0 in range ( len ( I11i1I111II1IiI ) ) :
   oo00O0oOo = { }
   oo00O0oOo = I11i1I111II1IiI [ OOO00000o0 ] . split ( '=' )
   if ( len ( oo00O0oOo ) ) == 2 :
    ii1iOO00O0O00oOOO [ oo00O0oOo [ 0 ] ] = oo00O0oOo [ 1 ]
    if 6 - 6: ooOoO0O00 + OooOO000 - ooOoO0O00 - I1ii11iIi11i - I11i * Ii1I
 return ii1iOO00O0O00oOOO
 if 90 - 90: IIiIi1iI / o0o00Oo0O / I11i . iIi1i1ii1 / ii
III1iIiii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
ooOoo000oO = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
ii1I = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
iIIiiiIiiii11 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
oOOoo0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iI1i1i1i1i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
O0OiiiIIiIi1ii11 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
iiII1i1II1iIi = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
II1iiiiI1Ii11 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
i1i = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
oOOOOoo000Ooo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
ooOOOOOo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
OOo0OOooO0 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
o00Oooo0o0 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
iii = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
IiII1Iiii = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
iI111i11iI1 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iIIOOOO0o0Oo0 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
III1iii1i1II = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
OOoooooooO = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
OoO0O000 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
iIIiI11i1I11 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
o0OO00Ooo0 = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
OooO0ooO0o0 = base64 . decodestring ( 'Q1VOVA==' )
def I1IIII1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 iii1I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOOOooO0oO00O0o = True
 ooOO00oOOo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO00oOOo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO00oOOo000 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIii11II11II1 = [ ]
  if showcontext == 'fav' :
   IIii11II11II1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIii11II11II1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooOO00oOOo000 . addContextMenuItems ( IIii11II11II1 )
 OOOOooO0oO00O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1I1i , listitem = ooOO00oOOo000 , isFolder = True )
 return OOOOooO0oO00O0o
 if 27 - 27: OooOO000 % I1ii11iIi11i . Ii1I . ooOoO0O00 % OOooOOo . I11i
def I1I11i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 iii1I1i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOOOooO0oO00O0o = True
 ooOO00oOOo000 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 ooOO00oOOo000 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 ooOO00oOOo000 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIii11II11II1 = [ ]
  if showcontext == 'fav' :
   IIii11II11II1 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   IIii11II11II1 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  ooOO00oOOo000 . addContextMenuItems ( IIii11II11II1 )
 OOOOooO0oO00O0o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii1I1i , listitem = ooOO00oOOo000 , isFolder = False )
 return OOOOooO0oO00O0o
 if 37 - 37: OooOO000 + O00OOo00oo0o * iIi1i1ii1 + OOoOoo
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + iIi1i1ii1 / IIiIiII11i
IIIIiii1IIii = I1iI1Ii1I1Iii1 ( )
iiOOooooO0Oo = None
iiI11ii1I1 = None
Ii11iiI = None
O00Ooo = None
O0OoooO0 = None
i11iiiiI1i = None
o00OooO = None
IIiii1 = None
if 12 - 12: ooOoO0O00 . oO0o
if 14 - 14: IIi + IIiIiII11i % IIi . oo0oO00 * IIiIi1iI
try :
 IIiii1 = int ( IIIIiii1IIii [ "fav_mode" ] )
except :
 pass
 if 54 - 54: IIiIi1iI * iiII11i1I1IIi - O00OOo00oo0o
try :
 iiOOooooO0Oo = urllib . unquote_plus ( IIIIiii1IIii [ "url" ] )
except :
 pass
try :
 iiI11ii1I1 = urllib . unquote_plus ( IIIIiii1IIii [ "name" ] )
except :
 pass
try :
 O00Ooo = urllib . unquote_plus ( IIIIiii1IIii [ "iconimage" ] )
except :
 pass
try :
 Ii11iiI = int ( IIIIiii1IIii [ "mode" ] )
except :
 pass
try :
 O0OoooO0 = urllib . unquote_plus ( IIIIiii1IIii [ "fanart" ] )
except :
 pass
try :
 i11iiiiI1i = urllib . unquote_plus ( IIIIiii1IIii [ "description" ] )
except :
 pass
 if 15 - 15: OooOO000 / o0o00Oo0O
 if 61 - 61: ooOoO0O00 / ooOoO0O00 + IIiIi1iI . O00OOo00oo0o * IIiIi1iI
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( Ii11iiI )
print "URL: " + str ( iiOOooooO0Oo )
print "Name: " + str ( iiI11ii1I1 )
print "IconImage: " + str ( O00Ooo )
if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
if 82 - 82: o0o00Oo0O / OooOO000 * oO0o - iiII11i1I1IIi + I1ii11iIi11i
def i1Oo0oO00o ( content , viewType ) :
 if 47 - 47: Ii1I * oOo0O0Ooo / Ii1I + iIi1i1ii1 * IIiIiII11i
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 78 - 78: O00OOo00oo0o - ooOoO0O00 + OOooOOo + I1ii11iIi11i * Ii1I * I11i
if O00Ooo == None : O00Ooo = Oo00OOOOO
if O0OoooO0 == None : O0OoooO0 = O0o0Oo
if Ii11iiI == None :
 o0o0o0oO0oOO ( )
 if 97 - 97: ooOoO0O00
elif Ii11iiI == 1 :
 iI1 ( iiOOooooO0Oo )
 if 29 - 29: oOo0O0Ooo
elif Ii11iiI == 44 :
 II1i11I ( iiOOooooO0Oo )
 if 37 - 37: Ii1I * O00OOo00oo0o * oOo0O0Ooo * o0o00Oo0O
elif Ii11iiI == 2 :
 OoO00O0 ( )
 if 35 - 35: oOo0O0Ooo - Ii1I * OooOO000 + OOoOoo / ooOoO0O00
elif Ii11iiI == 3 :
 I1ii ( )
 if 46 - 46: I1ii11iIi11i . IIiIi1iI % I1ii11iIi11i / IIiIiII11i * IIiIi1iI * IIi
elif Ii11iiI == 21 :
 i1i1II ( )
 if 59 - 59: O00OOo00oo0o * OooOO000
elif Ii11iiI == 4 :
 Ooo0o0oo0 ( )
 if 31 - 31: iiII11i1I1IIi / o0o00Oo0O
elif Ii11iiI == 5 :
 oO0ooooo0O00 ( iiOOooooO0Oo )
 if 57 - 57: ooOoO0O00 % IIiIi1iI
elif Ii11iiI == 6 :
 O0Oo0 ( iiOOooooO0Oo )
 if 69 - 69: I11i
elif Ii11iiI == 7 :
 ooOoOoOo ( iiOOooooO0Oo , iiI11ii1I1 )
 if 69 - 69: O00OOo00oo0o
elif Ii11iiI == 8 :
 IioOOo0OO0O0 ( iiOOooooO0Oo , iiI11ii1I1 )
 if 83 - 83: iI11I1II1I1I . I11i + O00OOo00oo0o . ii / IIiIi1iI + IIiIiII11i
elif Ii11iiI == 9 :
 FIXREPOSADDONS ( iiOOooooO0Oo )
 if 90 - 90: iIi1i1ii1 * OooOO000 / IIi
elif Ii11iiI == 10 :
 oOOo0O00o ( )
 if 68 - 68: OOooOOo
elif Ii11iiI == 11 :
 II1IooOO00Oo ( iiOOooooO0Oo )
 if 65 - 65: oo0oO00
elif Ii11iiI == 12 :
 OOooO0OO0 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 82 - 82: I11i
elif Ii11iiI == 13 :
 iI1iIiiiI1I1 ( )
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + O00OOo00oo0o
elif Ii11iiI == 14 :
 o00o0 ( iiOOooooO0Oo )
 if 65 - 65: iIi1i1ii1
elif Ii11iiI == 15 :
 iii1IiI1I1 ( )
 if 71 - 71: O00OOo00oo0o % O00OOo00oo0o . oo0oO00 + Ii - Ii
elif Ii11iiI == 16 :
 OOoO00o00oo ( iiOOooooO0Oo , iiI11ii1I1 )
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / O00OOo00oo0o - Ii . IIiIi1iI / IIi
elif Ii11iiI == 17 :
 I1II1i1iIIi ( iiOOooooO0Oo , iiI11ii1I1 )
 if 13 - 13: I11i % o0o00Oo0O - O00OOo00oo0o * ii / I1ii11iIi11i - ii
elif Ii11iiI == 18 :
 i1I1IiiIIIiiI ( )
 if 78 - 78: oo0oO00 % ii
elif Ii11iiI == 19 :
 iIiiii1 ( iiOOooooO0Oo )
 if 73 - 73: oOo0O0Ooo % IIiIi1iI % OOoOoo + ooOoO0O00 - ii / oo0oO00
elif Ii11iiI == 40 :
 I1iIIIiI ( iiI11ii1I1 , iiOOooooO0Oo , i11iiiiI1i )
 if 78 - 78: ii % oo0oO00 - Ii
elif Ii11iiI == 42 :
 I1IiI ( iiI11ii1I1 , iiOOooooO0Oo , i11iiiiI1i )
 if 37 - 37: OOoOoo % iIi1i1ii1 % ooOoO0O00
elif Ii11iiI == 43 :
 OoO00ooO ( iiOOooooO0Oo )
 if 23 - 23: IIiIi1iI - o0o00Oo0O + Ii
elif Ii11iiI == 20 :
 O0ii1ii1I1IIi1 ( iiOOooooO0Oo )
 if 98 - 98: ii
elif Ii11iiI == 22 :
 OO000o0O0o ( iiOOooooO0Oo )
 if 61 - 61: I11i . OOoOoo . o0o00Oo0O + ii + o0o00Oo0O
elif Ii11iiI == 23 :
 oooOoO ( iiOOooooO0Oo )
 if 65 - 65: ooOoO0O00 * IIi * ii - OOoOoo . OooOO000 - oO0o
elif Ii11iiI == 24 :
 iII1iiI11IIi ( iiOOooooO0Oo )
 if 71 - 71: iIi1i1ii1 * OOooOOo
elif Ii11iiI == 25 :
 Ooo00OoO ( iiOOooooO0Oo )
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % O00OOo00oo0o * I11i
elif Ii11iiI == 26 :
 IIii1i ( iiOOooooO0Oo )
 if 64 - 64: IIiIi1iI / IIiIi1iI + Ii1I * IIi % IIi
elif Ii11iiI == 27 :
 IiI11IiII1iI ( iiOOooooO0Oo )
 if 87 - 87: oO0o * I1ii11iIi11i
elif Ii11iiI == 28 :
 ooOOO ( iiOOooooO0Oo )
 if 83 - 83: ooOoO0O00 * O00OOo00oo0o - OOoOoo / iIi1i1ii1
elif Ii11iiI == 29 :
 OOoO00OOo ( iiOOooooO0Oo )
 if 48 - 48: oo0oO00 . IIiIiII11i - OOooOOo % ooOoO0O00 . OOooOOo
elif Ii11iiI == 30 :
 iiiiI1IiI1I1 ( iiOOooooO0Oo )
 if 32 - 32: iIi1i1ii1 * oOo0O0Ooo - IIi . I1ii11iIi11i / o0o00Oo0O + iIi1i1ii1
elif Ii11iiI == 31 :
 OOO00Oo00o ( iiOOooooO0Oo )
 if 67 - 67: OOooOOo % I1ii11iIi11i
elif Ii11iiI == 32 :
 oO0o0 ( )
 if 7 - 7: Ii % Ii1I / O00OOo00oo0o % I1ii11iIi11i - oO0o
elif Ii11iiI == 33 :
 oO00OoOo ( )
 if 73 - 73: Ii1I
elif Ii11iiI == 35 :
 II1III1i1iiI ( iiOOooooO0Oo )
 if 92 - 92: Ii + o0o00Oo0O * iiII11i1I1IIi
elif Ii11iiI == 34 :
 OoOi111i ( iiOOooooO0Oo )
 if 60 - 60: I11i / I1ii11iIi11i
elif Ii11iiI == 36 :
 oOo00o ( iiOOooooO0Oo )
 if 19 - 19: iI11I1II1I1I . oO0o / ii
elif Ii11iiI == 37 :
 iIIiIii11i1Ii ( iiOOooooO0Oo )
 if 2 - 2: o0o00Oo0O - o0o00Oo0O % O00OOo00oo0o / Ii1I
elif Ii11iiI == 38 :
 oooOO0oOooO00 ( iiOOooooO0Oo )
 if 76 - 76: oO0o * oo0oO00 - oO0o
elif Ii11iiI == 41 :
 IiIIi1 ( IIIIiii1IIii )
 if 57 - 57: ii / OOooOOo + oo0oO00 . iIi1i1ii1
elif Ii11iiI == 39 :
 iI1Ii11iIiI1 ( iiOOooooO0Oo )
 if 14 - 14: Ii % IIi * I11i * OOooOOo
elif Ii11iiI == 45 :
 TEXTS ( )
 if 55 - 55: O00OOo00oo0o * IIi * O00OOo00oo0o
elif Ii11iiI == 46 :
 OO0Oooo0oOO0O ( )
 if 70 - 70: o0o00Oo0O . iIi1i1ii1
elif Ii11iiI == 47 :
 GEVID ( )
 if 33 - 33: IIi * iIi1i1ii1
elif Ii11iiI == 48 :
 Ooooo ( iiI11ii1I1 , iiOOooooO0Oo , i11iiiiI1i )
 if 64 - 64: Ii . iI11I1II1I1I
elif Ii11iiI == 49 :
 IiIi1I1 ( )
 if 7 - 7: OOooOOo % IIiIi1iI + OOooOOo - OOooOOo * Ii % oO0o
elif Ii11iiI == 22222 :
 o0oO0OoO0 ( iiOOooooO0Oo )
 if 57 - 57: IIi / oO0o + Ii1I
elif Ii11iiI == 222 :
 O0o0O0OoOo0 ( iiOOooooO0Oo , iiI11ii1I1 )
 if 60 - 60: o0o00Oo0O * I1ii11iIi11i % IIi + OOoOoo . oO0o . I1ii11iIi11i
elif Ii11iiI == 333 :
 O0O0oOo0o0o0 ( iiOOooooO0Oo )
 if 70 - 70: iiII11i1I1IIi . Ii1I * oo0oO00
 if 97 - 97: oo0oO00 . iI11I1II1I1I - IIi
elif Ii11iiI == 1020 :
 iIOO000O ( )
 if 23 - 23: Ii1I % iiII11i1I1IIi
elif Ii11iiI == 1021 :
 ANIMEEP ( )
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
elif Ii11iiI == 1022 :
 ANIMEPLAY ( iiOOooooO0Oo )
 if 99 - 99: O00OOo00oo0o - Ii1I - oOo0O0Ooo - O00OOo00oo0o + oO0o + IIiIiII11i
elif Ii11iiI == 1001 :
 O0o0ooo00o0O ( )
 if 34 - 34: O00OOo00oo0o * iiII11i1I1IIi
elif Ii11iiI == 1005 :
 ooOO0O0O ( )
 if 31 - 31: OOoOoo . oo0oO00
elif Ii11iiI == 1007 :
 IIIiIIIi111iI ( iiOOooooO0Oo )
 if 40 - 40: iIi1i1ii1 - iiII11i1I1IIi / IIiIiII11i * ooOoO0O00 + OOoOoo * IIiIiII11i
elif Ii11iiI == 1010 :
 OOOoOo ( iiOOooooO0Oo )
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - O00OOo00oo0o
elif Ii11iiI == 1011 :
 OOo ( iiOOooooO0Oo )
 if 99 - 99: iIi1i1ii1 - OOoOoo - ooOoO0O00 / Ii . OOoOoo
elif Ii11iiI == 1012 :
 I11Ii111IIi ( iiOOooooO0Oo )
 if 58 - 58: IIi
elif Ii11iiI == 1030 :
 O0000o00 ( )
 if 12 - 12: oOo0O0Ooo . I11i * ii
elif Ii11iiI == 1031 :
 III1iIiIiII ( iiOOooooO0Oo , O00Ooo )
 if 64 - 64: OOooOOo + OOoOoo - ooOoO0O00 . IIiIiII11i . oO0o
elif Ii11iiI == 1032 :
 o0O0OO0o ( iiOOooooO0Oo )
 if 31 - 31: oo0oO00 . OooOO000 - iiII11i1I1IIi . iI11I1II1I1I + iiII11i1I1IIi . OOooOOo
elif Ii11iiI == 1006 :
 Parse . ParseURL ( iiOOooooO0Oo )
 if 86 - 86: Ii1I - Ii1I / OooOO000 - Ii1I * OooOO000 + O00OOo00oo0o
elif Ii11iiI == 2030 :
 Parse . addonParseURL ( iiOOooooO0Oo )
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - OOoOoo
elif Ii11iiI == 2031 :
 Parse . apkParseURL ( iiOOooooO0Oo )
 if 30 - 30: ii % IIi
elif Ii11iiI == 1002 :
 o00o000Oo ( iiOOooooO0Oo )
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - IIi
elif Ii11iiI == 1003 :
 IiIiIIIiI1iII ( iiOOooooO0Oo , O00Ooo )
 if 81 - 81: OooOO000 % iIi1i1ii1 . IIiIi1iI
elif Ii11iiI == 1004 :
 IiooO0O ( iiOOooooO0Oo )
 if 66 - 66: Ii1I * iIi1i1ii1 / ii * o0o00Oo0O % IIi
elif Ii11iiI == 1008 :
 iIIIIIi11Ii ( )
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * iIi1i1ii1 / O00OOo00oo0o * ii
elif Ii11iiI == 1009 :
 o0o0 ( iiOOooooO0Oo )
 if 82 - 82: I1ii11iIi11i / iIi1i1ii1 / iIi1i1ii1 % iIi1i1ii1
elif Ii11iiI == 2001 :
 OO0oOo00 ( )
 if 20 - 20: IIiIi1iI
elif Ii11iiI == 2002 :
 oO0OO00O0 ( iiOOooooO0Oo )
 if 63 - 63: iI11I1II1I1I . oO0o
elif Ii11iiI == 1013 :
 iiI1iI1I ( )
elif Ii11iiI == 10111113 :
 IiIi1iI11 ( iiOOooooO0Oo )
 if 100 - 100: ooOoO0O00 * ooOoO0O00
elif Ii11iiI == 1014 :
 IIiIIiiiiiII1 ( )
 if 26 - 26: IIi . oO0o % OOooOOo
elif Ii11iiI == 1015 :
 iIi1i1II ( iiOOooooO0Oo )
 if 94 - 94: OOoOoo
elif Ii11iiI == 1016 :
 IIi1IIIi ( iiOOooooO0Oo , O00Ooo , iiI11ii1I1 )
 if 15 - 15: iIi1i1ii1 - OOoOoo / o0o00Oo0O
elif Ii11iiI == 1017 :
 oO00oo0o00o0o ( )
 if 28 - 28: O00OOo00oo0o . ooOoO0O00 / Ii1I
elif Ii11iiI == 1018 :
 OoOo0oOooOoOO ( iiOOooooO0Oo )
 if 77 - 77: Ii / O00OOo00oo0o / Ii % OOooOOo - O00OOo00oo0o
elif Ii11iiI == 1023 :
 IiIIIIIi ( )
 if 80 - 80: O00OOo00oo0o % OOooOOo . ii . IIiIiII11i % OOoOoo
elif Ii11iiI == 1024 :
 oooii111I1I1I ( iiOOooooO0Oo )
 if 6 - 6: O00OOo00oo0o % OOoOoo / iIi1i1ii1 + O00OOo00oo0o . oo0oO00
elif Ii11iiI == 1025 :
 iIIiIi1IiI1 ( iiOOooooO0Oo )
 if 70 - 70: iI11I1II1I1I / iIi1i1ii1
elif Ii11iiI == 4001 :
 ooo0O0o00O ( )
 if 61 - 61: o0o00Oo0O * I11i + O00OOo00oo0o - IIi . oOo0O0Ooo - OOoOoo
elif Ii11iiI == 4002 :
 IIii1111 ( )
 if 7 - 7: Ii1I
elif Ii11iiI == 4003 :
 OO0o0oO0O000o ( )
 if 81 - 81: I1ii11iIi11i % IIiIiII11i % I11i / iiII11i1I1IIi
elif Ii11iiI == 4004 :
 I1ii1ii11i1I ( )
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
elif Ii11iiI == 4005 :
 o0OoOO ( )
 if 13 - 13: Ii
elif Ii11iiI == 4006 :
 oO0OoO00o ( )
 if 54 - 54: IIi . Ii1I * iiII11i1I1IIi % O00OOo00oo0o . o0o00Oo0O * OOoOoo
elif Ii11iiI == 4007 :
 oOoO00o ( )
 if 87 - 87: iIi1i1ii1 % Ii1I * I1ii11iIi11i
elif Ii11iiI == 4008 :
 OOOO0OOO ( )
 if 59 - 59: I1ii11iIi11i / iiII11i1I1IIi - iI11I1II1I1I * iI11I1II1I1I
elif Ii11iiI == 4009 : Oo00o0OO0O00o ( )
elif Ii11iiI == 4010 : Oo ( )
elif Ii11iiI == 3000 :
 I1I1IiiI1ii1 ( )
 if 18 - 18: iiII11i1I1IIi * Ii1I / Ii / iI11I1II1I1I * ii . IIi
elif Ii11iiI == 3001 :
 o0ooo ( )
 if 69 - 69: I1ii11iIi11i * IIiIi1iI
elif Ii11iiI == 3002 :
 o0oo00O ( iiOOooooO0Oo )
 if 91 - 91: I11i . IIiIi1iI / oO0o / Ii * I11i
elif Ii11iiI == 3003 :
 IIIIII1iI1II ( iiOOooooO0Oo )
 if 52 - 52: oOo0O0Ooo - Ii / OOoOoo . oo0oO00
elif Ii11iiI == 3004 :
 O00oooO00oo ( iiOOooooO0Oo )
 if 38 - 38: oo0oO00 + ii * OOooOOo % oo0oO00
elif Ii11iiI == 404 :
 o0oiIiI1i1iiIi1i ( iiI11ii1I1 , iiOOooooO0Oo , O00Ooo )
 if 91 - 91: ooOoO0O00 - Ii1I * oOo0O0Ooo
elif Ii11iiI == 405 :
 OooO00oo ( iiOOooooO0Oo )
 if 24 - 24: OOooOOo * iIi1i1ii1
elif Ii11iiI == 7030 :
 iIOOO ( )
 if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
elif Ii11iiI == 7021 :
 oOoOOo ( iiI11ii1I1 )
 if 81 - 81: IIi
elif Ii11iiI == 7022 :
 Oo0O ( iiI11ii1I1 )
 if 58 - 58: IIiIiII11i . O00OOo00oo0o . iIi1i1ii1 * ii / iIi1i1ii1 / iiII11i1I1IIi
elif Ii11iiI == 7000 :
 iI11iiiIi1II111I1i1 ( iiI11ii1I1 , iiOOooooO0Oo , img )
 if 41 - 41: iiII11i1I1IIi + oO0o . OooOO000
elif Ii11iiI == 7050 :
 III1II111Ii1 ( iiOOooooO0Oo )
 if 73 - 73: Ii * oOo0O0Ooo + I11i / oo0oO00
elif Ii11iiI == 7051 :
 o0OoOoOo0O ( iiOOooooO0Oo )
 if 56 - 56: ooOoO0O00
elif Ii11iiI == 7052 :
 I1Ii11iI11ii ( iiOOooooO0Oo )
 if 11 - 11: Ii % I11i / iiII11i1I1IIi * ii
elif Ii11iiI == 7053 :
 oOo0 ( iiOOooooO0Oo )
 if 82 - 82: OOoOoo
elif Ii11iiI == 7054 :
 CoolPlay ( iiOOooooO0Oo )
 if 10 - 10: I1ii11iIi11i % IIi / iiII11i1I1IIi * OOoOoo - I11i
elif Ii11iiI == 7060 :
 OoIII ( )
 if 54 - 54: Ii / iI11I1II1I1I % Ii1I / oOo0O0Ooo . iI11I1II1I1I / OooOO000
elif Ii11iiI == 7061 :
 iI1I ( iiOOooooO0Oo )
 if 1 - 1: O00OOo00oo0o / OOooOOo * OOooOOo - I11i % iIi1i1ii1
elif Ii11iiI == 7063 :
 OO00O ( iiOOooooO0Oo )
 if 96 - 96: OOoOoo / iIi1i1ii1 % oO0o . iI11I1II1I1I
elif Ii11iiI == 7062 :
 oo0o0ooOoo00O ( iiOOooooO0Oo )
 if 30 - 30: iiII11i1I1IIi - oO0o
elif Ii11iiI == 7064 :
 NATatozcat ( )
 if 15 - 15: ii
elif Ii11iiI == 7067 :
 iI1ii1 ( iiOOooooO0Oo )
 if 31 - 31: IIiIiII11i
elif Ii11iiI == 7066 :
 NATatozA ( iiOOooooO0Oo )
 if 62 - 62: iI11I1II1I1I % O00OOo00oo0o % Ii1I * OOoOoo
elif Ii11iiI == 7065 :
 O0oOOo ( iiOOooooO0Oo )
 if 87 - 87: OOoOoo
elif Ii11iiI == 7070 :
 IioooooOOo0Oo ( )
 if 45 - 45: oo0oO00 + IIiIiII11i * o0o00Oo0O % IIi . iI11I1II1I1I
elif Ii11iiI == 7071 :
 DIZIlist ( iiOOooooO0Oo )
 if 55 - 55: OOoOoo
elif Ii11iiI == 7072 :
 DIZIpull ( iiOOooooO0Oo )
 if 43 - 43: IIi
elif Ii11iiI == 7073 :
 WATCHDIZI ( iiOOooooO0Oo )
 if 17 - 17: Ii
elif Ii11iiI == 7002 :
 Oooo0O00OOo0o ( )
 if 94 - 94: ii - OOoOoo + oo0oO00 . ii / ooOoO0O00
elif Ii11iiI == 7003 :
 Iii1iI1I1iii1 ( iiOOooooO0Oo )
 if 53 - 53: O00OOo00oo0o % Ii1I
elif Ii11iiI == 7004 :
 oo000O ( iiOOooooO0Oo )
 if 17 - 17: ii % iIi1i1ii1 % o0o00Oo0O
elif Ii11iiI == 7020 :
 II1IIiiIiI11 ( iiOOooooO0Oo )
 if 46 - 46: OooOO000 + O00OOo00oo0o % ii * Ii1I
elif Ii11iiI == 7001 :
 I1i1iiiI1 ( )
 if 89 - 89: OOoOoo - OOoOoo % OooOO000 / iiII11i1I1IIi + oo0oO00 - OOoOoo
elif Ii11iiI == 7010 :
 OO0oOOo0o ( iiOOooooO0Oo )
 if 97 - 97: iIi1i1ii1 % OOooOOo / Ii1I / iI11I1II1I1I * ii * IIi
elif Ii11iiI == 7011 :
 IIiii1I1I ( iiOOooooO0Oo )
 if 80 - 80: oo0oO00 / o0o00Oo0O
elif Ii11iiI == 7012 :
 oO0O0ooOoo ( iiOOooooO0Oo )
 if 55 - 55: oOo0O0Ooo * iiII11i1I1IIi / o0o00Oo0O % OOooOOo
elif Ii11iiI == 7013 :
 cnfTVPlay2 ( iiOOooooO0Oo )
elif Ii11iiI == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iiOOooooO0Oo )
elif Ii11iiI == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iiOOooooO0Oo )
elif Ii11iiI == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iiI11ii1I1 , iiOOooooO0Oo , O00Ooo )
elif Ii11iiI == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif Ii11iiI == 7018 :
 iIIoooO0 ( )
elif Ii11iiI == 7019 :
 CNF_Studio_Indexer . List_Movies ( iiOOooooO0Oo )
elif Ii11iiI == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iiOOooooO0Oo )
elif Ii11iiI == 7024 :
 CNF_Studio_Indexer . Box_Office ( iiOOooooO0Oo )
 if 71 - 71: Ii * OOooOOo * IIi + oo0oO00 + I1ii11iIi11i
elif Ii11iiI == 8000 :
 iI11ii ( )
elif Ii11iiI == 8001 :
 i1Oo000O000 ( )
elif Ii11iiI == 8002 :
 ii1i1I1111ii ( )
elif Ii11iiI == 8003 :
 IiIIIiII1111 ( )
elif Ii11iiI == 8004 :
 iII1I1IIiiiI ( )
elif Ii11iiI == 8005 :
 Oo00oO0o0Oo0o ( )
elif Ii11iiI == 8006 :
 i1IiIi1I1i ( iiI11ii1I1 , iiOOooooO0Oo )
elif Ii11iiI == 8030 :
 o0oO0OO00ooOO ( iiOOooooO0Oo )
elif Ii11iiI == 8045 :
 IIi11I1i1I1I ( iiOOooooO0Oo )
elif Ii11iiI == 8046 :
 IiII1I ( iiOOooooO0Oo )
elif Ii11iiI == 8047 :
 OOoo0OOOo0o ( iiOOooooO0Oo )
elif Ii11iiI == 8048 :
 i1iiII ( iiOOooooO0Oo )
elif Ii11iiI == 8049 :
 ooii ( iiOOooooO0Oo )
elif Ii11iiI == 804900 :
 oOO0O0O0OO00oo ( iiOOooooO0Oo )
elif Ii11iiI == 8020 :
 i1iI1 ( )
elif Ii11iiI == 8021 :
 iI11 ( iiOOooooO0Oo )
elif Ii11iiI == 8022 :
 i1IiI1Ii ( iiOOooooO0Oo )
elif Ii11iiI == 8023 :
 OOo0 ( iiOOooooO0Oo )
elif Ii11iiI == 8040 :
 iII1ii1 ( )
elif Ii11iiI == 8041 :
 I11i1i11IiIi1 ( iiOOooooO0Oo )
elif Ii11iiI == 8042 :
 I1i11IIIi ( iiOOooooO0Oo )
elif Ii11iiI == 8043 :
 yt . PlayVideo ( iiOOooooO0Oo )
elif Ii11iiI == 8044 :
 III1IIIIIiiI ( iiOOooooO0Oo )
elif Ii11iiI == 8060 :
 i1Iii11I1i ( )
elif Ii11iiI == 8061 :
 Oo0OOOOOOO0oo ( iiOOooooO0Oo )
elif Ii11iiI == 8064 :
 ii1I1IiiI1ii1i ( )
elif Ii11iiI == 8065 :
 I1iIIIiiii ( iiOOooooO0Oo )
elif Ii11iiI == 8070 :
 O0o0oo0O ( )
elif Ii11iiI == 8071 :
 Ooo00OOo000 ( iiOOooooO0Oo )
elif Ii11iiI == 7080 :
 i1ooOO00o0 ( iiOOooooO0Oo )
elif Ii11iiI == 8090 :
 o0O00o0 ( )
elif Ii11iiI == 8091 :
 OOO0O ( iiOOooooO0Oo )
elif Ii11iiI == 8092 :
 i11II1 ( iiOOooooO0Oo )
elif Ii11iiI == 8093 :
 I1iiIII ( iiOOooooO0Oo )
elif Ii11iiI == 8081 :
 OOOo0Ooo0o00o ( )
elif Ii11iiI == 8062 :
 oOOOOooO ( iiOOooooO0Oo )
elif Ii11iiI == 8063 :
 I1Iii11111I1iii ( iiOOooooO0Oo )
elif Ii11iiI == 8050 :
 O00OO0ooO0 ( )
elif Ii11iiI == 8051 :
 OoOooOO0oOOo0O ( iiOOooooO0Oo )
elif Ii11iiI == 8052 :
 I1II ( iiOOooooO0Oo )
elif Ii11iiI == 8085 :
 Ii1i ( )
elif Ii11iiI == 8086 :
 i1I1IIiIIi ( iiOOooooO0Oo )
elif Ii11iiI == 8087 :
 IIII1I ( iiOOooooO0Oo )
elif Ii11iiI == 8088 :
 i1iI1I1IIIi1i ( iiOOooooO0Oo , iiI11ii1I1 )
elif Ii11iiI == 9000 :
 i1iii1ii ( )
elif Ii11iiI == 1111 :
 OOoO0oo0O ( )
elif Ii11iiI == 9001 :
 i1II ( )
elif Ii11iiI == 9002 :
 iIi1Ii1i1iI ( )
elif Ii11iiI == 9003 :
 i1Ii ( )
elif Ii11iiI == 9004 :
 World1 ( )
elif Ii11iiI == 9005 :
 World2 ( iiOOooooO0Oo )
elif Ii11iiI == 9006 :
 World3 ( iiOOooooO0Oo )
elif Ii11iiI == 9007 :
 i11i1i1II ( )
elif Ii11iiI == 9008 :
 Ii11Ii11 ( iiOOooooO0Oo )
elif Ii11iiI == 9009 :
 IiIiIIi ( iiOOooooO0Oo )
elif Ii11iiI == 9010 :
 i1I1IiIiiI1II ( )
elif Ii11iiI == 9011 :
 iI1i ( iiOOooooO0Oo )
elif Ii11iiI == 50 :
 o0OoOOo ( iiOOooooO0Oo )
elif Ii11iiI == 9020 :
 champlist ( )
elif Ii11iiI == 9021 :
 o0Oo0o ( )
elif Ii11iiI == 9022 :
 i1iioO0oOo ( )
elif Ii11iiI == 9023 :
 IIiIiii ( )
elif Ii11iiI == 9024 :
 oo000O0o ( iiOOooooO0Oo )
elif Ii11iiI == 9030 :
 Ii1i111iI ( iiOOooooO0Oo )
elif Ii11iiI == 9031 :
 iII1ii ( iiOOooooO0Oo )
elif Ii11iiI == 9032 :
 OOO00OiI ( iiOOooooO0Oo )
elif Ii11iiI == 9033 :
 O0o00oO00O0 ( iiOOooooO0Oo )
elif Ii11iiI == 9034 :
 iIIi ( )
elif Ii11iiI == 7085 :
 IiI1I1iii ( iiOOooooO0Oo )
elif Ii11iiI == 7086 :
 oo0000o ( iiOOooooO0Oo )
elif Ii11iiI == 7087 :
 ooOOoo0 ( i11iiiiI1i )
elif Ii11iiI == 9666 :
 O0O0ooOOO ( iiOOooooO0Oo )
elif Ii11iiI == 10100 : o00i111iiIiiIiI ( )
elif Ii11iiI == 101001 : iiiI1IiI ( iiOOooooO0Oo )
elif Ii11iiI == 10105 : IIiIi ( iiOOooooO0Oo )
elif Ii11iiI == 10106 : I1I1IIiiI1 ( iiOOooooO0Oo )
elif Ii11iiI == 10104 : oo0O0 ( iiOOooooO0Oo )
elif Ii11iiI == 10107 : Ii111IIIIii ( )
elif Ii11iiI == 10103 : oooOOO0o0O0 ( iiOOooooO0Oo )
elif Ii11iiI == 10108 : IiIiiIII ( iiOOooooO0Oo )
elif Ii11iiI == 10000 : Origin_Menu ( )
elif Ii11iiI == 10001 : oo0o0000Oo0 ( )
elif Ii11iiI == 10002 : O0O0Oo00 ( )
elif Ii11iiI == 10003 : i1i1ii ( )
elif Ii11iiI == 10004 : O000O0OO00oo ( iiOOooooO0Oo )
elif Ii11iiI == 10005 : iII1I1 ( )
elif Ii11iiI == 10006 : o0O0Ooo ( iiOOooooO0Oo )
elif Ii11iiI == 10007 : Ii11iiIo0OO0oooo ( iiOOooooO0Oo , O00Ooo )
elif Ii11iiI == 10008 : IiIi ( )
elif Ii11iiI == 10009 : IiI ( )
elif Ii11iiI == 10010 : OOOoo0O00Oooo ( iiOOooooO0Oo )
elif Ii11iiI == 10011 : i1iIi ( iiOOooooO0Oo )
elif Ii11iiI == 10012 : iii1 ( iiOOooooO0Oo )
elif Ii11iiI == 10109 : o0iIiii ( iiOOooooO0Oo )
elif Ii11iiI == 10013 : Oooo0Oo00o ( iiOOooooO0Oo )
elif Ii11iiI == 10014 : O0oO0o0OOOOOO ( )
elif Ii11iiI == 10015 : I1I11Iiii111 ( )
elif Ii11iiI == 10016 : iIi1i ( iiOOooooO0Oo )
elif Ii11iiI == 10017 : ooIi11iI ( )
elif Ii11iiI == 10018 : I11I111i1I1 ( )
elif Ii11iiI == 10019 : i1i1Ii1IiIII ( )
elif Ii11iiI == 10020 : i1iI ( )
elif Ii11iiI == 10021 : ooOo0O0 ( )
elif Ii11iiI == 10022 : OoooO00OoO0 ( iiOOooooO0Oo )
elif Ii11iiI == 10023 : i11iII11ii ( iiI11ii1I1 , iiOOooooO0Oo )
elif Ii11iiI == 10024 : iiI ( iiOOooooO0Oo )
elif Ii11iiI == 10025 : iIi11i1 ( )
elif Ii11iiI == 10026 : o00OOOOOo0OOo ( )
elif Ii11iiI == 10027 : II11ii1I11 ( )
elif Ii11iiI == 10028 : III1ii ( )
elif Ii11iiI == 10029 : oo0oOO ( )
elif Ii11iiI == 423 : IIIIiI11Ii1i ( iiOOooooO0Oo )
elif Ii11iiI == 426 : ooOO ( iiOOooooO0Oo )
elif Ii11iiI == 10030 : Izle_Films ( )
elif Ii11iiI == 10031 : Latest_Izle_Movies ( )
elif Ii11iiI == 10032 : Izle_Genres ( )
elif Ii11iiI == 10033 : Izle_Pop_Movies ( )
elif Ii11iiI == 10034 : Izle_Boxsets ( )
elif Ii11iiI == 10035 : Izle_Search ( )
elif Ii11iiI == 10036 : Izle_Genres_Movie ( iiOOooooO0Oo )
elif Ii11iiI == 10037 : Izle_Boxset_single ( iiOOooooO0Oo )
elif Ii11iiI == 10038 : Izle_IFRAME ( )
elif Ii11iiI == 10039 : Izle_Boxsets_Next ( iiOOooooO0Oo )
elif Ii11iiI == 10040 : IIiI1 ( )
elif Ii11iiI == 10041 : o0Oo ( iiOOooooO0Oo )
elif Ii11iiI == 10042 : II11IiI1 ( iiOOooooO0Oo )
elif Ii11iiI == 10043 : oOOoO0oO0oo0O ( )
elif Ii11iiI == 10044 : ooO00OoO0o0OO ( iiOOooooO0Oo )
elif Ii11iiI == 10045 : iIi11iI1i ( iiI11ii1I1 )
elif Ii11iiI == 10046 : iiIIiIi ( iiOOooooO0Oo )
elif Ii11iiI == 10047 : iI1IIIi11 ( iiOOooooO0Oo )
elif Ii11iiI == 10048 : i1I1i1i1I1 ( iiOOooooO0Oo )
elif Ii11iiI == 10049 : Ii1Ii1 ( iiOOooooO0Oo )
elif Ii11iiI == 10050 : OOOoo0OO ( )
elif Ii11iiI == 10051 : OoOO0OoOoO00 ( )
elif Ii11iiI == 10052 : oOoOo000Ooooo ( )
elif Ii11iiI == 10053 : Addon ( iiOOooooO0Oo )
elif Ii11iiI == 10054 : II1i1iii1iiiI ( iiOOooooO0Oo , iiI11ii1I1 )
elif Ii11iiI == 10055 :
 I1iII1IIi1IiI ( "addFavorite" )
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 oOOo0ooO0 ( iiI11ii1I1 , iiOOooooO0Oo , O00Ooo , O0OoooO0 , IIiii1 )
elif Ii11iiI == 10056 :
 I1iII1IIi1IiI ( "rmFavorite" )
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiIiIiIiiIiI ( iiI11ii1I1 )
elif Ii11iiI == 10057 :
 I1iII1IIi1IiI ( "getFavorites" )
 OO0oOoO000o0 ( )
elif Ii11iiI == 10058 : O0Oooo ( )
elif Ii11iiI == 10059 : Donators_Guide ( )
elif Ii11iiI == 10060 : I1i11 ( )
elif Ii11iiI == 10061 : oO0O000oOo ( )
elif Ii11iiI == 10062 : iIIIiIi1I1i ( iiI11ii1I1 , iiOOooooO0Oo , i11iiiiI1i )
elif Ii11iiI == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
elif Ii11iiI == 10064 : I1i ( )
elif Ii11iiI == 10065 : o00ooo ( iiOOooooO0Oo )
elif Ii11iiI == 10066 : O0OO ( iiOOooooO0Oo )
elif Ii11iiI == 10068 : III1I1Iii1iiI ( iiOOooooO0Oo )
elif Ii11iiI == 10069 : O0o ( iiOOooooO0Oo )
elif Ii11iiI == 10070 : o0Oii1111i ( iiOOooooO0Oo )
elif Ii11iiI == 10071 : Genie_Watch ( )
elif Ii11iiI == 10072 : ii111Ii11iii ( )
elif Ii11iiI == 10073 : oOO0o00O ( iiOOooooO0Oo )
elif Ii11iiI == 10074 : O00ooOo ( iiOOooooO0Oo )
elif Ii11iiI == 10075 : Ii1 ( O00Ooo , iiI11ii1I1 , iiOOooooO0Oo )
elif Ii11iiI == 10076 : ooOo ( iiOOooooO0Oo )
elif Ii11iiI == 10077 : iIi ( iiOOooooO0Oo )
elif Ii11iiI == 10078 : OO0OoOOO0 ( )
elif Ii11iiI == 10079 : Genie_Watch_Tv_Shows ( )
elif Ii11iiI == 10080 : Genie_Watch_Tv_Genre ( iiOOooooO0Oo )
elif Ii11iiI == 10081 : Genie_Watch_TV_PlayRun ( iiOOooooO0Oo )
elif Ii11iiI == 10082 : Genie_Watch_TV_Episodes ( iiOOooooO0Oo , O00Ooo )
elif Ii11iiI == 10083 : Genie_Watch_Tv_Recent ( iiOOooooO0Oo )
elif Ii11iiI == 10084 : O0OoO0ooOO0o ( )
elif Ii11iiI == 10085 : Iiii1i1 ( )
elif Ii11iiI == 10086 : II1I ( )
elif Ii11iiI == 20000 : o0O00oOoo ( )
elif Ii11iiI == 20001 : oo00I1IiI1IIiI ( iiOOooooO0Oo )
elif Ii11iiI == 20002 : iIi1 ( iiOOooooO0Oo )
elif Ii11iiI == 20003 : ooiI1i ( iiOOooooO0Oo )
elif Ii11iiI == 20004 : Ii11 ( iiOOooooO0Oo )
elif Ii11iiI == 20005 : O0oo00oOOO0o ( iiOOooooO0Oo )
elif Ii11iiI == 21004 : o0Ooo0o0ooo0 ( )
elif Ii11iiI == 21005 : OOoooOoO0 ( iiOOooooO0Oo )
elif Ii11iiI == 21006 : iIiIi1IiIi1iI ( iiOOooooO0Oo )
elif Ii11iiI == 21007 : oOoO0Oo0 ( iiOOooooO0Oo )
elif Ii11iiI == 30000 : iiI1I1ii ( )
elif Ii11iiI == 30001 : iIIIIIIIiIII ( )
elif Ii11iiI == 10012 : Resolve ( iiOOooooO0Oo )
elif Ii11iiI == 30003 : Ooo000O00 ( )
elif Ii11iiI == 30004 : oOOOOO0Ooooo ( iiOOooooO0Oo )
elif Ii11iiI == 30005 : OOoOO0O0o0 ( iiOOooooO0Oo )
elif Ii11iiI == 30006 : iiII1iiiiiii ( )
elif Ii11iiI == 30007 : iIiI1ii ( )
elif Ii11iiI == 30008 : III1IiI1i1i ( iiOOooooO0Oo )
elif Ii11iiI == 30009 : iiiI1iI1 ( iiOOooooO0Oo )
elif Ii11iiI == 30010 : i111I11I ( iiOOooooO0Oo )
elif Ii11iiI == 30011 : Ii11iiI1 ( )
elif Ii11iiI == 30012 : OoooO0 ( )
elif Ii11iiI == 30013 : IiIii1 ( )
elif Ii11iiI == 30014 : oO0o0Oo ( )
elif Ii11iiI == 30015 : oOooo00000 ( iiOOooooO0Oo , O00Ooo , O0OoooO0 )
elif Ii11iiI == 30016 : i111I1iiIiII ( iiOOooooO0Oo )
elif Ii11iiI == 30019 : I11i1I1ii1i1 ( iiOOooooO0Oo )
elif Ii11iiI == 30017 : iiiIi1II1III ( iiOOooooO0Oo )
elif Ii11iiI == 30018 : OOooOooo0OOo0 ( iiOOooooO0Oo )
elif Ii11iiI == 30030 : oO0OOOoO0o ( )
elif Ii11iiI == 30031 : oo0oO ( )
elif Ii11iiI == 30032 : oO00O0 ( )
elif Ii11iiI == 30033 : o0Oo00oOO ( )
elif Ii11iiI == 30034 : O0oo ( )
elif Ii11iiI == 30035 : ooooo0O0 ( iiOOooooO0Oo )
elif Ii11iiI == 30036 : i1III1iI ( iiOOooooO0Oo )
elif Ii11iiI == 30037 : ii1ii1IiiiiIi1I ( iiOOooooO0Oo )
elif Ii11iiI == 30038 : I1Iii ( )
elif Ii11iiI == 30039 : Iii1IIII11I ( )
elif Ii11iiI == 50000 : iIiIi11 ( )
elif Ii11iiI == 50001 : iIIi11 ( )
elif Ii11iiI == 50002 : ooiIii1I1111 ( iiOOooooO0Oo )
elif Ii11iiI == 50003 : iIII1I1ii ( i11iiiiI1i )
elif Ii11iiI == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif Ii11iiI == 60001 : O0iI ( )
elif Ii11iiI == 60002 : i1ii1111i1i ( iiI11ii1I1 )
elif Ii11iiI == 60003 : iiiIiI ( iiI11ii1I1 )
elif Ii11iiI == 50004 : i11i1 ( )
elif Ii11iiI == 50005 : speedtest . runtest ( iiOOooooO0Oo )
elif Ii11iiI == 70001 : I1iI11iii ( )
elif Ii11iiI == 70002 : OOoOOOO00 ( iiOOooooO0Oo )
elif Ii11iiI == 70003 : IIii1III ( iiOOooooO0Oo )
elif Ii11iiI == 70004 : ooooOoo0OO ( iiOOooooO0Oo )
elif Ii11iiI == 70005 : Oo0O0000Oo00o ( iiOOooooO0Oo )
elif Ii11iiI == 70006 : II1 ( )
elif Ii11iiI == 50006 : iiIiI1i1 ( i1 , i1111 )
elif Ii11iiI == 80000 : oO0oI1I1 ( )
elif Ii11iiI == 80001 : resolvefilmon ( iiOOooooO0Oo )
elif Ii11iiI == 80002 : I1III1iIi ( )
elif Ii11iiI == 80003 : o0o00o0Oo ( iiI11ii1I1 , iiOOooooO0Oo , "None" )
elif Ii11iiI == 80004 : iIi11i ( iiI11ii1I1 , iiOOooooO0Oo )
elif Ii11iiI == 80005 : OooOoOo ( )
elif Ii11iiI == 80006 : iIIiiIIi1IiI ( iiOOooooO0Oo )
elif Ii11iiI == 80007 : I11IIIiIi11 ( iiOOooooO0Oo )
elif Ii11iiI == 80008 : I11iiIi1i1 ( )
elif Ii11iiI == 80009 : iIiiII ( )
elif Ii11iiI == 80010 : iII1I ( iiOOooooO0Oo )
elif Ii11iiI == 80011 : Ii1Ii11I ( iiOOooooO0Oo )
elif Ii11iiI == 80012 : o0o00O ( )
elif Ii11iiI == 90000 : ooOi1i1i11iI11II ( iiI11ii1I1 , iiOOooooO0Oo )
elif Ii11iiI == 90001 : i11I1II1I11i ( )
elif Ii11iiI == 90002 : Iiii1iI1i ( )
elif Ii11iiI == 90003 : o0oOoo0o ( iiOOooooO0Oo )
elif Ii11iiI == 90004 : IiiIiIIi ( iiOOooooO0Oo )
elif Ii11iiI == 90005 : O00Oo ( iiOOooooO0Oo )
elif Ii11iiI == 90006 : OOOOoOoO ( iiOOooooO0Oo )
elif Ii11iiI == 90007 : OO000 ( iiOOooooO0Oo )
elif Ii11iiI == 90008 : Oo0iII ( iiOOooooO0Oo )
elif Ii11iiI == 90009 : OoOo0O00 ( iiOOooooO0Oo )
elif Ii11iiI == 90010 : oO0O00oOOoooO ( )
elif Ii11iiI == 90020 : o0oo0Oo ( )
elif Ii11iiI == 90021 : hellyeah2 ( iiOOooooO0Oo )
elif Ii11iiI == 90022 : hellyeah3 ( iiOOooooO0Oo )
elif Ii11iiI == 90023 : i1ii11 ( )
elif Ii11iiI == 90024 : IIioo0OO ( iiOOooooO0Oo )
elif Ii11iiI == 90025 : IiiI11i1I ( iiOOooooO0Oo )
if 59 - 59: OOoOoo
elif Ii11iiI == 90030 : I1i1I11I ( )
elif Ii11iiI == 90031 : i1I1IiiIi1i ( )
elif Ii11iiI == 90032 : Ooo0OOoOoO0 ( iiOOooooO0Oo )
elif Ii11iiI == 90033 : IIo0Oo0oO0oOO00 ( iiOOooooO0Oo )
elif Ii11iiI == 90034 : II1i111Ii1i ( iiOOooooO0Oo )
elif Ii11iiI == 90035 : ooO0oooOO0 ( iiOOooooO0Oo )
elif Ii11iiI == 90036 : O0OOOOoOOO ( iiOOooooO0Oo )
elif Ii11iiI == 90037 : oOOO00o000o ( iiOOooooO0Oo )
elif Ii11iiI == 90038 : o0OOoOoO00 ( )
if 54 - 54: IIi
if 27 - 27: OOooOOo - oO0o + I11i + IIiIi1iI . oO0o
elif Ii11iiI == 100001 : Stand_up ( )
if 86 - 86: IIiIiII11i - ii - IIiIi1iI % OooOO000
elif Ii11iiI == 100003 : iIi1i ( iiOOooooO0Oo )
elif Ii11iiI == 100004 : I111iIi1 ( iiOOooooO0Oo )
elif Ii11iiI == 100005 : Resolve ( iiOOooooO0Oo )
elif Ii11iiI == 100008 : Search ( )
elif Ii11iiI == 100007 : ooo000ooO0000 ( iiOOooooO0Oo )
elif Ii11iiI == 100009 : yt . PlayVideo ( iiOOooooO0Oo )
elif Ii11iiI == 100010 : oO0oO0 ( iiOOooooO0Oo )
elif Ii11iiI == 100100 : oOOo0o0oo ( O00Ooo , iiOOooooO0Oo , o00OooO )
elif Ii11iiI == 100101 : OoO0O0O0o00 ( iiOOooooO0Oo , iiI11ii1I1 , O0OoooO0 , o00OooO , O00Ooo )
elif Ii11iiI == 100102 : i11i1iiI1i ( iiI11ii1I1 , iiOOooooO0Oo , O00Ooo , O0OoooO0 )
elif Ii11iiI == 100106 : OoOIii11iI11i1I ( iiOOooooO0Oo , iiI11ii1I1 )
elif Ii11iiI == 100107 : iIiIIii ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
