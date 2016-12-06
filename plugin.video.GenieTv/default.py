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
  iiIiI1i1 ( 'Change Log 06/12/16 - v3.3.5' , 'NEW SECTIONS ADDED, MOVIE HUB(streams>>stream categories>>movies), Tv HUB(streams>>stream categories>>tv shows), BAMF IPTV revamped, WATCH SERIES revamped, General Maintence' )
  os . makedirs ( IIIII )
  if 53 - 53: oo0oO00 - oOo0O0Ooo - oo0oO00 * OooOO000
  if 71 - 71: o0o00Oo0O - iI11I1II1I1I
def I1ii1ii11i1I ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']MOVIE HUB[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   i1II ( )
  if iI1i11iII111 == 1 :
   iI1I ( )
  if iI1i11iII111 == 2 :
   OooOoOo ( iiOOooooO0Oo )
  if iI1i11iII111 == 3 :
   III1I1Iii1iiI ( )
  if iI1i11iII111 == 4 :
   i1Iii11I1i ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if iI1i11iII111 == 5 :
   Oo00o0OO0O00o ( )
 else :
  I1IIII1i ( '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9001 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']MOVIE HUB[/COLOR]' , '' , 90040 , oOOOo00O00oOo + 'movhub.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']POPCORN BOX[/COLOR]' , str ( ooOO0O0ooOooO ) , 7061 , oOOOo00O00oOo + 'PopcornBox.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Desi Flix[/COLOR]' , '' , 80005 , oOOOo00O00oOo + 'Desi.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , oOOOo00O00oOo + 'FilmTrailers.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , oOOOo00O00oOo + 'ClassicMovies.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def O0Oooo ( ) :
 IIiiiI1iIII ( )
 iiIi1i ( )
 if 27 - 27: IIi * IIiIi1iI . O00OOo00oo0o % OOoOoo * OOoOoo . ooOoO0O00
 if 72 - 72: IIi % Ii1I + oO0o / oo0oO00 + OOoOoo
 I1IIII1i ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 if oo00 . getSetting ( 'TV GUIDE' ) == 'true' :
  I1I11i ( '[COLOR' + II + ']TV GUIDE[/COLOR]' , '' , 10063 , oOOOo00O00oOo + 'TvGuide.png' , O0o0Oo , '' )
 I1I11i ( '[COLOR' + II + ']Link GTV to Guide[/COLOR]' , '' , 4010 , oOOOo00O00oOo + 'linkchannels.png' , O0o0Oo , '' )
def iIIi ( ) :
 I1IIII1i ( '[COLOR' + II + ']DAILY LISTS[/COLOR]' , '' , 9007 , Oo00OOOOO , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Oo00OOOOO , O0o0Oo , '' )
 if 10 - 10: O00OOo00oo0o / IIiIi1iI + Ii / iIi1i1ii1
 if 74 - 74: IIi + o0o00Oo0O + ooOoO0O00 - ooOoO0O00 + IIiIiII11i
 if 83 - 83: Ii1I - oOo0O0Ooo + IIi
 if 5 - 5: iIi1i1ii1
 if 46 - 46: OOoOoo
def o0OoOO ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']Tv HUB[/COLOR]' , '[COLOR' + II + ']THE SOURCE[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
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
   Oo0 ( )
  if iI1i11iII111 == 5 :
   oooooOOO000Oo ( )
  if iI1i11iII111 == 6 :
   Ooo00OoOOO ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  I1IIII1i ( '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , str ( ooOO0O0ooOooO ) , 9002 , oOOOo00O00oOo + 'Search.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']Tv HUB[/COLOR]' , str ( ooOO0O0ooOooO ) , 90050 , oOOOo00O00oOo + 'Tv HUB.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Watch Series' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '' , 10040 , oOOOo00O00oOo + 'WatchSeries.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '' , 8020 , oOOOo00O00oOo + 'iWatchSeries.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   I1IIII1i ( '[COLOR' + II + ']CLASSIC TV[/COLOR]' , str ( ooOO0O0ooOooO ) , 8064 , oOOOo00O00oOo + 'ClassicTV.png' , O0o0Oo , '' )
  I1IIII1i ( '[COLOR' + II + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , oOOOo00O00oOo + 'TVShowTrailers.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def Oo0OO0000oooo ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'The Reaper' ) == 'true' :
   IIII1iII = '[COLOR' + II + ']THE REAPER[/COLOR]'
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   ii1III11 = '[COLOR' + II + ']PANDORAS BOX[/COLOR]'
  if oo00 . getSetting ( 'Scooby Streams' ) == 'true' :
   I1iiIIIi11 = '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]'
  if oo00 . getSetting ( 'HeroVision' ) == 'true' :
   Ii1I11ii1i = '[COLOR' + II + ']APPRENTICE[/COLOR]'
  OooOoOO0 = [ IIII1iII , ii1III11 , '[COLOR' + II + ']DoJo STREAMS[/COLOR]' , Ii1I11ii1i , '[COLOR' + II + ']RAIZ TV[/COLOR]' , I1iiIIIi11 , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0iIiIIIIIii ( ( i11 ( 'aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9tYWlubWVudS5waHA=' ) ) )
  if iI1i11iII111 == 1 :
   OOo0 ( )
  if iI1i11iII111 == 2 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9kb2pvc3RyZWFtcy9tYWluLnBocA==' ) ) , O00Ooo , iiI11ii1I1 )
  if iI1i11iII111 == 3 :
   ii11I1 ( )
  if iI1i11iII111 == 4 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvcmFpenBpY2t6LnBocA==' ) ) , O00Ooo , iiI11ii1I1 )
  if iI1i11iII111 == 5 :
   oO0oo ( )
  if iI1i11iII111 == 6 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , O00Ooo , iiI11ii1I1 )
  if iI1i11iII111 == 7 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9tYWluLnBocA==' ) ) , O00Ooo , iiI11ii1I1 )
 else :
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
  if 38 - 38: ii * IIiIi1iI % o0o00Oo0O * OOooOOo
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 29 - 29: Ii1I / ooOoO0O00 . oOo0O0Ooo - OOooOOo - OOooOOo - iIi1i1ii1
def IiiIiI111iI ( ) :
 IIiiiI1iIII ( )
 I1I11i ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , oOOOo00O00oOo + 'SilentHunter.png' , O0o0Oo , '' )
def OOo ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 url = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( OoO000O0Oo )
 for I1iii11 , ooo0O in IIIII11I1IiI :
  if '[DIR]' in I1iii11 :
   iII1iii ( ( '[COLOR' + II + ']' + ooo0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + ooo0O , 1018 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'mkv' in ooo0O :
   i11i1iiiII ( ( '[COLOR' + II + ']' + ooo0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + ooo0O , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
  if 'avi' in ooo0O :
   i11i1iiiII ( ( '[COLOR' + II + ']' + ooo0O + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + ooo0O , 222 , oOOOo00O00oOo + 'SilentHunter.png' )
   if 68 - 68: Ii * oO0o
def ii11I1 ( ) :
 I1IIII1i ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , oOOOo00O00oOo + 'scraped.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , oOOOo00O00oOo + 'newaddmagic.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , oOOOo00O00oOo + 'newaddsit.png' , O0o0Oo , '' )
 if 46 - 46: OOooOOo / iI11I1II1I1I % OooOO000 . iI11I1II1I1I * OooOO000
def IIi1ii1Ii ( url ) :
 I1 = OoOoO ( url )
 IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( I1 )
 for iiI11ii1I1 , url , o0ii1i , oOOoo , O0OoooO0 , iII1111III1I in IIIII11I1IiI :
  if oOOoo == '123' :
   oOOoo = oOOOo00O00oOo + 'appstreams.png'
  if O0OoooO0 == '123' :
   O0OoooO0 = oOOOo00O00oOo + 'appstreams.png'
  if 'php' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100010 , oOOoo , O0OoooO0 , iII1111III1I )
  elif 'playlist' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100007 , oOOoo , O0OoooO0 , iII1111III1I )
  elif 'watchseries' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100100 , oOOoo , O0OoooO0 , iII1111III1I )
  elif not 'http' in url :
   ii11i ( iiI11ii1I1 , url , 100009 , oOOoo , O0OoooO0 , iII1111III1I , '' )
  else :
   ii11i ( iiI11ii1I1 , url , 100005 , oOOoo , O0OoooO0 , iII1111III1I , '' )
   if 100 - 100: IIiIi1iI % iI11I1II1I1I * IIiIiII11i - OooOO000
def oo00O00oO000o ( url ) :
 I1 = OoOoO ( url )
 OOo00OoO = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for url , oOo0OOoO0 , iII1111III1I , O0OoooO0 , iiI11ii1I1 in OOo00OoO :
  if oOo0OOoO0 == '123' :
   oOo0OOoO0 = oOOOo00O00oOo + 'appstreams.png'
  if O0OoooO0 == '123' :
   O0OoooO0 = O0o0Oo
  if 'php' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100004 , oOo0OOoO0 , O0OoooO0 , iII1111III1I )
  elif 'playlist' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100007 , oOo0OOoO0 , O0OoooO0 , iII1111III1I )
  elif 'watchseries' in url :
   I1IIII1i ( iiI11ii1I1 , url , 100100 , oOo0OOoO0 , O0OoooO0 , iII1111III1I )
  elif not 'http' in url :
   ii11i ( iiI11ii1I1 , url , 100009 , oOo0OOoO0 , O0OoooO0 , iII1111III1I , '' )
  else :
   ii11i ( iiI11ii1I1 , url , 100005 , oOo0OOoO0 , O0OoooO0 , iII1111III1I , '' )
   if 10 - 10: I11i / Ii
def o00oO ( url ) :
 if 92 - 92: OOoOoo * I1ii11iIi11i * I1ii11iIi11i * oOo0O0Ooo . iI11I1II1I1I
 I1 = OoOoO ( url )
 I1Ii1111iIi = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( I1 )
 for I11o0oO00oO0o0o0 in I1Ii1111iIi :
  oOOoo = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for oOOoo in oOOoo :
   oOOoo = oOOoo
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
  ii11i ( '[COLORred]' + str ( I1I ) + '[/COLOR] : ' + str ( iiI11ii1I1 ) , str ( url ) , 100009 , str ( oOOoo ) , O0o0Oo , '' , '' )
  i1Oo0oO00o ( 'movies' , '' )
  if 89 - 89: ooOoO0O00 / IIiIiII11i . iI11I1II1I1I
  if 1 - 1: IIiIi1iI % OOooOOo * I1ii11iIi11i
  if 55 - 55: OOooOOo
  if 87 - 87: ii % OooOO000 . oOo0O0Ooo / IIiIi1iI
  if 8 - 8: iiII11i1I1IIi + I11i
def oOOo0o0oo ( iconimage , url , extra ) :
 oOOoo = ' '
 i11iiiiI1i = ' '
 O0OoooO0 = ' '
 iIIii = ' '
 i1iIiIi1I = OoOoO ( url )
 oOOoo = re . compile ( '<img src="(.+?)">' ) . findall ( i1iIiIi1I )
 for oOOoo in oOOoo :
  oOOoo = oOOoo
 iiii11i = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( i1iIiIi1I )
 for O0OoooO0 in iiii11i :
  O0OoooO0 = O0OoooO0
 IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( i1iIiIi1I )
 for url , iIIii in IIIII11I1IiI :
  iIIii = 'S' + ( iIIii ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = I11i1I1I + url
  III11II1I1Ii1 ( ( iIIii ) . replace ( '  ' , '' ) , url , 100101 , oOOoo , O0OoooO0 , i11iiiiI1i , '' )
  i1Oo0oO00o ( 'Movies' , 'info' )
  if 72 - 72: OooOO000 * oo0oO00 % iIi1i1ii1 . ii
def OoO0O0O0o00 ( url , name , fanart , extra , iconimage ) :
 iiiI11 = extra
 iIIii = name
 i1iIiIi1I = OoOoO ( url )
 oOOoo = iconimage
 IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( i1iIiIi1I )
 for url , name , OOoO000 in IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = I11i1I1I + url
  OOoO000 = OOoO000
  oOOOO = name + ' - [COLORred]' + OOoO000 + '[/COLOR]'
  III11II1I1Ii1 ( oOOOO , url , 100102 , oOOoo , fanart , 'Aired : ' + OOoO000 , oOOOO )
  if 49 - 49: IIiIiII11i . oo0oO00 . Ii % OOoOoo
def i11i1iiI1i ( name , URL , iconimage , fanart ) :
 I1 = OoOoO ( URL )
 IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , name in IIIII11I1IiI :
  for oOOOoo00 in oO0Oo :
   if oOOOoo00 in iiOOooooO0Oo :
    URL = 'http://www.watchseriesgo.to/link/' + iiOOooooO0Oo
    ii11i ( name , URL , 100106 , oOOOo00O00oOo + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( IIIII11I1IiI ) <= 0 :
  III11II1I1Ii1 ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 87 - 87: IIiIi1iI
  if 45 - 45: oO0o / ii - OooOO000 / iIi1i1ii1 % OOoOoo
def OoO ( url , name ) :
 Iii11iI11i1I = name
 I1 = OoOoO ( url )
 IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( I1 )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( I1 )
 I1II1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  oOoOOo000oOoO0 ( url , Iii11iI11i1I )
 for url in i1I :
  oOoOOo000oOoO0 ( url , Iii11iI11i1I )
 for url in I1II1 :
  oOoOOo000oOoO0 ( url , Iii11iI11i1I )
  if 86 - 86: IIiIiII11i % Ii + iIi1i1ii1 % Ii
def oOoOOo000oOoO0 ( url , season_name ) :
 if 'daclips.in' in url :
  Ooo0o0OOO ( url , season_name )
 elif 'filehoot.com' in url :
  i11IiII ( url , season_name )
 elif 'allmyvideos.net' in url :
  oOooo0O0o ( url , season_name )
 elif 'vidspot.net' in url :
  Oo000 ( url , season_name )
 elif 'vodlocker' in url :
  O00O0oOOo ( url , season_name )
 elif 'vidto' in url :
  O0oO ( url , season_name )
  if 79 - 79: I11i % OooOO000 * ii * iI11I1II1I1I . OooOO000 / iIi1i1ii1
  if 19 - 19: o0o00Oo0O + iiII11i1I1IIi + iIi1i1ii1 / IIiIiII11i / IIiIiII11i
def O0oO ( url , season_name ) :
 I1 = OoOoO ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for oO0o0O0Ooo0o , iiI11ii1I1 in IIIII11I1IiI :
  i1Ii11II ( oO0o0O0Ooo0o , season_name )
  if 18 - 18: IIiIiII11i . ii % OOooOOo % iIi1i1ii1
  if 9 - 9: oO0o - I1ii11iIi11i * ii . I1ii11iIi11i
def oOooo0O0o ( url , season_name ) :
 I1 = OoOoO ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( I1 )
 for oO0o0O0Ooo0o , iiI11ii1I1 in IIIII11I1IiI :
  i1Ii11II ( oO0o0O0Ooo0o , season_name )
  if 2 - 2: ii % IIi
def Oo000 ( url , season_name ) :
 I1 = OoOoO ( url )
 IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( I1 )
 for oO0o0O0Ooo0o , iiI11ii1I1 in IIIII11I1IiI :
  i1Ii11II ( oO0o0O0Ooo0o , season_name )
  if 63 - 63: oOo0O0Ooo % iI11I1II1I1I
def O00O0oOOo ( url , season_name ) :
 I1 = OoOoO ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for oO0o0O0Ooo0o in IIIII11I1IiI :
  i1Ii11II ( oO0o0O0Ooo0o , season_name )
  if 39 - 39: OooOO000 / IIiIiII11i / Ii1I % oOo0O0Ooo
def Ooo0o0OOO ( url , season_name ) :
 I1 = OoOoO ( url )
 IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( I1 )
 for oO0o0O0Ooo0o in IIIII11I1IiI :
  i1Ii11II ( oO0o0O0Ooo0o , season_name )
  if 89 - 89: O00OOo00oo0o + ii + O00OOo00oo0o * ooOoO0O00 + iI11I1II1I1I % iiII11i1I1IIi
def i11IiII ( url , season_name ) :
 I1 = OoOoO ( url )
 IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( I1 )
 for oO0o0O0Ooo0o in IIIII11I1IiI :
  i1Ii11II ( oO0o0O0Ooo0o , season_name )
  if 59 - 59: IIi + Ii
def i1Ii11II ( Link , season_name ) :
 if 'http:/' in Link :
  oo0OOo0O ( Link )
  if 39 - 39: ii + oo0oO00 % IIi / IIi
def I1i ( url ) :
 I1 = OPEN_URL_1 ( url )
 ooo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 for url in ooo :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 20 - 20: ooOoO0O00 - iiII11i1I1IIi
def III11II1I1Ii1 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 ii1ii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOoo0oO = True
 iioo0o0OoOOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iioo0o0OoOOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iioo0o0OoOOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooO0oO00O0o = [ ]
  if 70 - 70: O00OOo00oo0o
  if showcontext == 'fav' :
   ooO0oO00O0o . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooO0oO00O0o . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iioo0o0OoOOO . addContextMenuItems ( ooO0oO00O0o )
 OoOoo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1ii11 , listitem = iioo0o0OoOOO , isFolder = True )
 return OoOoo0oO
 if 16 - 16: OooOO000 - ii % I1ii11iIi11i
 if 36 - 36: IIi
def ii11i ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 ii1ii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOoo0oO = True
 iioo0o0OoOOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iioo0o0OoOOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iioo0o0OoOOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooO0oO00O0o = [ ]
  ooO0oO00O0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooO0oO00O0o . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooO0oO00O0o . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iioo0o0OoOOO . addContextMenuItems ( ooO0oO00O0o )
 OoOoo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1ii11 , listitem = iioo0o0OoOOO , isFolder = False )
 return OoOoo0oO
 if 84 - 84: O00OOo00oo0o . oO0o . IIiIiII11i . iiII11i1I1IIi / iIi1i1ii1 % Ii1I
def OOO0oOoO0O ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 84 - 84: o0o00Oo0O * ii - OOoOoo * OOoOoo
def i1ii ( url ) :
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0O . play ( url ) . strip ( )
 except : pass
 if 11 - 11: Ii - oo0oO00 . oo0oO00
def oo0OOo0O ( url ) :
 oO0O = xbmc . Player ( )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 if 31 - 31: IIi / I1ii11iIi11i * ooOoO0O00 . OOooOOo
def OoOoO ( url ) :
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
  if 57 - 57: IIi + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
  if 83 - 83: I11i / Ii % iI11I1II1I1I . iiII11i1I1IIi % oo0oO00 . ii
  if 94 - 94: iIi1i1ii1 + iI11I1II1I1I % oO0o
def oOoO00o ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   O0OO0oOOo ( )
  if iI1i11iII111 == 1 :
   OO0oO0o ( )
  if iI1i11iII111 == 2 :
   III111i11IiI ( )
  if iI1i11iII111 == 3 :
   O0000 ( )
  if iI1i11iII111 == 4 :
   ooO00O0O0 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
 if 33 - 33: I1ii11iIi11i
 if 49 - 49: oO0o % OooOO000 % OooOO000 / OooOO000
 if 53 - 53: iI11I1II1I1I
def OO ( ) :
 I1 = O000oo ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( I1 )
 for IIiooOOoooooo in IIIII11I1IiI :
  IIiooOOoooooo = ( str ( IIiooOOoooooo ) )
  if os . path . exists ( xbmc . translatePath ( IIiooOOoooooo ) ) :
   oooo00o0o0o = ( IIiooOOoooooo ) . replace ( 'special://home/addons/' , '' )
   iiIiI1i1 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + oooo00o0o0o + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iI1i11iII111 = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iI1i11iII111 == 0 :
    O0Oo00oO0O00 ( IIiooOOoooooo )
    oOOo0O00o ( )
   elif iI1i11iII111 == 1 :
    IiO000O0OO00oo ( IIiooOOoooooo )
  else :
   pass
   if 69 - 69: I11i / I1ii11iIi11i
def IiO000O0OO00oo ( addon ) :
 oooo00o0o0o = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 43 - 43: Ii1I . oOo0O0Ooo / ii % ii
def O0Oo00oO0O00 ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 iIIIII1iiiiII = os . path . join ( I11II1i , 'default.py' )
 oooO = open ( iIIIII1iiiiII , "w+" )
 if 22 - 22: IIiIi1iI - IIiIi1iI % IIi . O00OOo00oo0o + oo0oO00
 oooO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 oooO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 oooO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 63 - 63: oOo0O0Ooo % O00OOo00oo0o * I11i + O00OOo00oo0o / I1ii11iIi11i % OooOO000
 if 45 - 45: OOoOoo
 if 20 - 20: ii * I11i * o0o00Oo0O . IIi
 if 78 - 78: iI11I1II1I1I + iiII11i1I1IIi - iIi1i1ii1 * O00OOo00oo0o - ii % OOooOOo
def O0iIiIIIIIii ( url ) :
 I1 = O000oo ( url )
 i1OoOO = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( I1 )
 I1II1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 oo00OO0000oO = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( I1 )
 iIII1I1i1i = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url , i1I1i1 , O0OoooO0 , iII1111III1I in i1OoOO :
  if 'php' in url :
   I1IIII1i ( iiI11ii1I1 , url , 90037 , i1I1i1 , O0OoooO0 , iII1111III1I )
  elif iiI11ii1I1 == 'Search' :
   I1IIII1i ( 'Search' , url , 90038 , i1I1i1 , O0OoooO0 , iII1111III1I )
  else :
   I1I11i ( iiI11ii1I1 , url , 222 , i1I1i1 , O0OoooO0 , iII1111III1I )
 for iiI11ii1I1 , oOo0OOoO0 , url , o0OIIiI1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 90037 , oOo0OOoO0 , o0OIIiI1I1 , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , o0OIIiI1I1 in i1I :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , o0OIIiI1I1 , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , o0OIIiI1I1 in I1II1 :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , o0OIIiI1I1 , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , o0OIIiI1I1 in oo00OO0000oO :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , o0OIIiI1I1 , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 in iIII1I1i1i :
  I1I11i ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , '' , '' )
  i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
  if 15 - 15: iIi1i1ii1 * I1ii11iIi11i % Ii1I * iI11I1II1I1I - Ii
def Oo00OOOOoo0oo ( ) :
 O00OOooo0Ooo = [ 'serialsearch' , 'moviesearch' ]
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 if iiI1i11II == '' :
  pass
 else :
  for II11 in O00OOooo0Ooo :
   I1iii = I11 + II11 + '.php'
   i1iIiIi1I = O000oo ( I1iii )
   if i1iIiIi1I != 'Opened' :
    OOo00OoO = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( i1iIiIi1I )
    for iiI11ii1I1 , iiOOooooO0Oo , i1I1i1 , O0OoooO0 , iII1111III1I in OOo00OoO :
     if iiI1i11II in iiI11ii1I1 . lower ( ) :
      oOO0OO0O = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( o00OO00OoO ) )
      for oOOOoo00 in oOO0OO0O :
       if oOOOoo00 == iiOOooooO0Oo :
        iiI11ii1I1 = '[COLORred]* [/COLOR]' + ( iiI11ii1I1 ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        o00o = open ( oOOoo0Oo , "a" )
        o00o . write ( 'item="' + iiI11ii1I1 + '"\n' )
        o00o . close
      if 'php' in iiOOooooO0Oo :
       I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , 90037 , i1I1i1 , O0OoooO0 , iII1111III1I )
      else :
       I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 222 , i1I1i1 , O0OoooO0 , iII1111III1I )
       if 47 - 47: I11i + OooOO000 - oo0oO00 % ii
   i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
   if 52 - 52: O00OOo00oo0o / IIiIi1iI - iiII11i1I1IIi
def iIiI ( ) :
 I1 = O000oo ( 'http://www.tvcatchup.com/channels/' )
 iii1i1iiiiIi = O000oo ( 'http://www.djing.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)".+?src="([^"]*)"/>.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for iIIIi1i1I11i , oOo0OOoO0 , iiOOooooO0Oo in IIIII11I1IiI :
  i11i1iiiII ( iIIIi1i1I11i , 'http://www.tvcatchup.com' + iiOOooooO0Oo , 90024 , 'http://www.tvcatchup.com' + oOo0OOoO0 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in i1I :
  if 'Submit' in iiI11ii1I1 :
   pass
  elif '&lt;' in iiI11ii1I1 :
   pass
  else :
   I1I11i ( 'DJing  ' + iiI11ii1I1 , iiOOooooO0Oo , 90025 , 'http://www.djing.com' + oOo0OOoO0 , O0o0Oo , '' )
  i1Oo0oO00o ( 'movies' , 'MAIN' )
def oOO0OO0OO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'var url = "([^"]*)";' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( url )
def oOOoooO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 22 - 22: iiII11i1I1IIi + iI11I1II1I1I
def iiI1iIii1i ( ) :
 if 24 - 24: OOooOOo % ooOoO0O00 + OooOO000 . Ii . Ii1I
 if 17 - 17: Ii1I . IIiIiII11i . IIiIi1iI / Ii1I
 if 57 - 57: iiII11i1I1IIi
 if 67 - 67: oO0o . IIiIi1iI
 if 87 - 87: oo0oO00 % iIi1i1ii1
 if 83 - 83: IIiIiII11i - iiII11i1I1IIi
 if 35 - 35: ooOoO0O00 - iI11I1II1I1I + ooOoO0O00
 if 86 - 86: iI11I1II1I1I + OOooOOo . Ii - iIi1i1ii1
 if 51 - 51: OOooOOo
 if 14 - 14: OOoOoo % oo0oO00 % I1ii11iIi11i - Ii
 if 53 - 53: iIi1i1ii1 % I1ii11iIi11i
 iII1iii ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , oOOOo00O00oOo + 'seasons.png' )
 iII1iii ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , oOOOo00O00oOo + 'episodes.png' )
 iII1iii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , oOOOo00O00oOo + 'Search.png' )
 i1Oo0oO00o ( 'tvshows' , 'INFO' )
 if 59 - 59: IIi % iI11I1II1I1I . ooOoO0O00 + IIiIiII11i * OOoOoo
def i1IiiI1iIi ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( I1 )
 for url , iiI11ii1I1 , oOOo00O0OOOo in IIIII11I1IiI :
  iII1iii ( ( iiI11ii1I1 + ' - ' + oOOo00O0OOOo ) . replace ( '&amp;' , '&' ) , url , 90053 , oOOOo00O00oOo + 'seasons.png' )
  if 31 - 31: iiII11i1I1IIi % IIi * iiII11i1I1IIi
def IiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , url , 90054 , oOOOo00O00oOo + 'episodes.png' )
  if 34 - 34: iiII11i1I1IIi % IIiIi1iI . o0o00Oo0O . iI11I1II1I1I
def ooi1II1I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , url , 90054 , oOo0OOoO0 )
 for url in next :
  iII1iii ( 'NEXT' , url , 90053 , oOOOo00O00oOo + 'Next.png' )
  if 95 - 95: oO0o - IIi / IIiIiII11i % Ii1I . I11i
def iii1IIII1iii11I ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( I1 )
 for oOo0OOoO0 , oOOo00O0OOOo , url , iiI11ii1I1 , oo0OoOooo in IIIII11I1IiI :
  I1IIII1i ( oOOo00O0OOOo + ' - ' + iiI11ii1I1 + ' - ' + oo0OoOooo , url , 90044 , oOo0OOoO0 , oOo0OOoO0 , '' )
 for oOo0OOoO0 , iiI11ii1I1 , url in i1I :
  iII1iii ( iiI11ii1I1 , url , 90044 , oOo0OOoO0 , oOo0OOoO0 , '' )
 for url in next :
  iII1iii ( 'NEXT' , url , 90053 , oOOOo00O00oOo + 'Next.png' )
  if 95 - 95: OOoOoo * Ii1I % IIiIi1iI % iIi1i1ii1 - iIi1i1ii1
def oOoooO0 ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0 = 'http://onlinemovies.tube/?s=' + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 iiI1i11II = o0Oo0 . lower ( )
 I1 = O000oo ( iiI1i11II )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , i1i1II1i11 in IIIII11I1IiI :
  if 'season' in i1i1II1i11 :
   iII1iii ( iiI11ii1I1 , iiOOooooO0Oo , 90054 , oOo0OOoO0 , oOo0OOoO0 , '' )
  if 'episodes' in i1i1II1i11 :
   iII1iii ( iiI11ii1I1 , iiOOooooO0Oo , 90044 , oOo0OOoO0 , oOo0OOoO0 , '' )
 for iiOOooooO0Oo in next :
  iII1iii ( 'NEXT' , iiOOooooO0Oo , 90053 , oOOOo00O00oOo + 'Next.png' )
  if 91 - 91: iiII11i1I1IIi / ooOoO0O00 * ooOoO0O00
def iI1I ( ) :
 if 25 - 25: iI11I1II1I1I . IIi * oo0oO00 - iIi1i1ii1
 if 55 - 55: OOooOOo
 if 63 - 63: OOoOoo * OOooOOo * IIiIi1iI
 if 92 - 92: Ii1I / o0o00Oo0O
 if 80 - 80: I11i - IIi + ii
 if 98 - 98: IIi + ooOoO0O00 . oOo0O0Ooo - IIiIiII11i - I11i
 if 24 - 24: I1ii11iIi11i - ooOoO0O00 + iiII11i1I1IIi
 if 38 - 38: ii / Ii1I . o0o00Oo0O / ooOoO0O00 / I1ii11iIi11i + iI11I1II1I1I
 if 96 - 96: OooOO000
 if 18 - 18: OooOO000 * iiII11i1I1IIi - iIi1i1ii1
 iII1iii ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , oOOOo00O00oOo + 'allmov.png' )
 iII1iii ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , oOOOo00O00oOo + 'Genre.png' )
 iII1iii ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , oOOOo00O00oOo + 'Years.png' )
 iII1iii ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , oOOOo00O00oOo + 'Search.png' )
 i1Oo0oO00o ( 'tvshows' , 'INFO' )
 if 31 - 31: I1ii11iIi11i - o0o00Oo0O % OOooOOo % oo0oO00
def iI1iii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( I1 )
 for url , iiI11ii1I1 , oOOo00O0OOOo in IIIII11I1IiI :
  if 'genre' in url :
   iII1iii ( ( iiI11ii1I1 + ' - ' + oOOo00O0OOOo ) . replace ( '&amp;' , '&' ) , url , 90043 , oOOOo00O00oOo + 'Genre.png' )
   if 87 - 87: Ii1I / ii - I1ii11iIi11i % OOooOOo % OOoOoo % I1ii11iIi11i
def Ii1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'release' in url :
   iII1iii ( iiI11ii1I1 , url , 90043 , oOOOo00O00oOo + 'Years.png' )
   if 34 - 34: OooOO000 - ii . oOo0O0Ooo / IIiIiII11i
def II1II ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , oo0O , url , iII1111III1I in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 + ' ' + oo0O , url , 90044 , oOo0OOoO0 , oOo0OOoO0 , iII1111III1I )
 for oOo0OOoO0 , iiI11ii1I1 , i1i1II1i11 , url , Oo , iII1111III1I in i1I :
  if 'movies' in i1i1II1i11 :
   I1IIII1i ( iiI11ii1I1 + ' - ' + Oo , url , 90044 , oOo0OOoO0 , oOo0OOoO0 , iII1111III1I )
 for url in next :
  iII1iii ( 'NEXT' , url , 90043 , oOOOo00O00oOo + 'Next.png' )
  if 11 - 11: OOoOoo
def o0oooO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  ooOo ( url )
  if 84 - 84: IIi
def ooOo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( iiI11ii1I1 ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , oOOOo00O00oOo + 'movhub.png' )
def o0OoO00 ( ) :
 if 18 - 18: oo0oO00 - I11i - oOo0O0Ooo - oOo0O0Ooo
 if 54 - 54: I1ii11iIi11i + oOo0O0Ooo / OooOO000 . oOo0O0Ooo * OOooOOo
 if 1 - 1: OOooOOo * oO0o . ooOoO0O00 / I1ii11iIi11i . Ii1I + I1ii11iIi11i
 if 17 - 17: I1ii11iIi11i + oO0o / iIi1i1ii1 / OooOO000 * IIi
 if 29 - 29: oO0o % ii * oo0oO00 / IIiIiII11i - oo0oO00
 if 19 - 19: Ii
 if 54 - 54: IIiIiII11i . iiII11i1I1IIi
 if 73 - 73: OOooOOo . oOo0O0Ooo
 if 32 - 32: OOooOOo * oOo0O0Ooo % IIiIi1iI * iIi1i1ii1 . o0o00Oo0O
 if 48 - 48: OooOO000 * OooOO000
 if 13 - 13: iIi1i1ii1 / iiII11i1I1IIi + OOooOOo . I11i % IIiIi1iI
 if 48 - 48: oOo0O0Ooo / Ii - I11i * oo0oO00 / ii
 if 89 - 89: iI11I1II1I1I / oOo0O0Ooo - IIiIiII11i / iIi1i1ii1 . Ii . iIi1i1ii1
 if 48 - 48: o0o00Oo0O + o0o00Oo0O . O00OOo00oo0o - IIiIi1iI
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0 = 'http://onlinemovies.tube/?s=' + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 iiI1i11II = o0Oo0 . lower ( )
 I1 = O000oo ( iiI1i11II )
 IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , o00oo0000 in IIIII11I1IiI :
  if 'movies' in o00oo0000 :
   iII1iii ( o00oo0000 + '-' + iiI11ii1I1 , iiOOooooO0Oo , 90044 , oOo0OOoO0 )
 for iiOOooooO0Oo in next :
  II1II ( iiOOooooO0Oo )
  if 44 - 44: I1ii11iIi11i % iI11I1II1I1I
def III1I1Iii1iiI ( ) :
 iII1iii ( 'Search' , '' , 80008 , oOOOo00O00oOo + 'Search.png' )
 I1 = O000oo ( 'http://www.join4films.com/' )
 IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , iiOOooooO0Oo , 80006 , oOOOo00O00oOo + 'Desi.png' )
def oo0ooO0 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( I1 )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , url , 80007 , oOo0OOoO0 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( 'Next' , url , 80006 , oOOOo00O00oOo + 'Next.png' )
def IIiiiiIiIIii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  iii1 ( url )
def O0OO ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0 = 'http://www.join4films.com/?s=' + ( o0oOOoOOO ) . replace ( ' ' , '+' ) + '&search_type=1'
 iiI1i11II = o0Oo0 . lower ( )
 oo0ooO0 ( iiI1i11II )
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
 if 78 - 78: Ii / iI11I1II1I1I - I11i
 if 23 - 23: iiII11i1I1IIi
def iIiiIiiIi ( ) :
 I1IIII1i ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 I1IIII1i ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 I1IIII1i ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 I1IIII1i ( 'Search' , '' , 10078 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
 if 40 - 40: I11i
def oOOo0oo0o0o0 ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0 = 'http://imoviemax.se/?s=' + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 iiI1i11II = o0Oo0 . lower ( )
 iIii1Ooo0oO0 ( iiI1i11II )
def o0Oo0oOooOoOo ( url ) :
 I1iOo = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( I1 )
 for url , iiI11ii1I1 , IiIiIi1I1 in IIIII11I1IiI :
  if iiI11ii1I1 in I1iOo :
   pass
  else :
   I1IIII1i ( iiI11ii1I1 + ' - ' + IiIiIi1I1 + ' Films' , url , 10074 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
   I1iOo . append ( iiI11ii1I1 )
   if 2 - 2: ooOoO0O00 - IIiIi1iI + oOo0O0Ooo . I11i * I11i / OOooOOo
def oOOO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , iIi1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 + ' - Views:' + iIi1I1 , url , 10075 , oOOOo00O00oOo + 'genievision.png' , O0o0Oo , '' )
  if 63 - 63: OooOO000 * Ii1I . ii / IIi * I1ii11iIi11i . IIiIi1iI
  if 62 - 62: ooOoO0O00 / IIiIi1iI . oOo0O0Ooo * I11i
def iIii1Ooo0oO0 ( url ) :
 i11i1Ii1 = [ ]
 I1 = O000oo ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( I1 )
 for next in next :
  I1IIII1i ( 'NEXT PAGE' , next , 10074 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 10075 , oOo0OOoO0 , oOo0OOoO0 , '' )
  i11i1Ii1 . append ( iiI11ii1I1 )
  if 98 - 98: O00OOo00oo0o
def o0oo0000 ( img , name , url ) :
 img = img
 name = name
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( I1 )
 for i111i1i , url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  IiIii1I1I = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + IiIii1I1I
  OO0Oooo0oo = ( i111i1i ) . replace ( 'play-' , 'Server ' )
  I1I11i ( OO0Oooo0oo , IiIii1I1I , 10076 , img , img , '' )
  if 42 - 42: iIi1i1ii1 * O00OOo00oo0o . OOoOoo * oOo0O0Ooo + OOooOOo
def i1i1II11II1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( I1 )
 for ooo0O in IIIII11I1IiI :
  if '=m' in ooo0O :
   II1IIIii ( ooo0O )
  elif 'php' in ooo0O :
   i1i1II11II1 ( url )
  else :
   I1 = O000oo ( ooo0O )
   IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( I1 )
   for iIIIiIi1I1i in IIIII11I1IiI :
    II1IIIii ( ooo0O )
    if 78 - 78: iI11I1II1I1I % OOooOOo + Ii1I / ooOoO0O00 % IIiIiII11i + IIi
    if 91 - 91: iI11I1II1I1I % oO0o . I11i + iIi1i1ii1 + I11i
    if 95 - 95: iIi1i1ii1 + Ii1I * IIi
def I1Ii ( url ) :
 I1 = O000oo ( url )
 ooooOoO0O = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for OOoO000 , IIII in ooooOoO0O :
  print 'there ><><><><><><><><><><><><'
  OOoO000 = OOoO000
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( IIII ) )
  for iiI11ii1I1 , IIIIoOo in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + OOoO000 + '[/COLOR] - ' + iiI11ii1I1 + ' - [COLOR' + II + ']' + IIIIoOo + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
 I11o0oO00oO0o0o0 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for OOoO000 , Oo0oOo0O0O0o in I11o0oO00oO0o0o0 :
  print 'there ><><><><><><><><><><><><'
  OOoO000 = OOoO000
  IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Oo0oOo0O0O0o ) )
  for iiI11ii1I1 , IIIIoOo in IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   I1IIII1i ( '[COLORred]' + OOoO000 + '[/COLOR] - ' + iiI11ii1I1 + ' - [COLOR' + II + ']' + IIIIoOo + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , oOOOo00O00oOo + 'loader.png' , O0o0Oo , '' )
   if 46 - 46: o0o00Oo0O * I1ii11iIi11i / o0o00Oo0O + oO0o
   if 56 - 56: IIi . IIiIiII11i
   if 53 - 53: oo0oO00 % iiII11i1I1IIi . IIiIi1iI - OOooOOo
def Ooo00OoOOO ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( I1 )
 for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
  iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for iiI11ii1I1 in iiI11ii1I1 :
   iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  oOOoo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for oOOoo in oOOoo :
   oOOoo = 'http:' + oOOoo
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoo , '' , '' )
  if 69 - 69: IIiIiII11i * oOo0O0Ooo - IIiIi1iI - iI11I1II1I1I + I11i - oo0oO00
  if 50 - 50: iiII11i1I1IIi - IIiIi1iI
  if 1 - 1: oo0oO00
  if 12 - 12: IIiIi1iI % oOo0O0Ooo + oo0oO00 - ooOoO0O00 . iIi1i1ii1 / oOo0O0Ooo
def i1Iii11I1i ( url ) :
 if 51 - 51: IIi . oOo0O0Ooo
 Ooi11III1II1 = [ ]
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( I1 )
 for ooo0O , oOo0OOoO0 , iiI11ii1I1 , Ii1iIi111I1i in IIIII11I1IiI :
  iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  iii1i1iiiiIi = O000oo ( ooo0O )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for ooo , i11iiiiI1i in i1I :
   I1III111i = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( i11iiiiI1i ) )
   for iII1111III1I in I1III111i :
    if iiI11ii1I1 in Ooi11III1II1 :
     pass
    else :
     I1I11i ( iiI11ii1I1 , ooo , 8043 , oOo0OOoO0 , oOo0OOoO0 , iII1111III1I )
     i1Oo0oO00o ( 'movies' , 'INFO' )
     Ooi11III1II1 . append ( iiI11ii1I1 )
     if 4 - 4: ooOoO0O00 + IIiIi1iI + ooOoO0O00
     if 31 - 31: iIi1i1ii1
def OoOOo00 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , O00Ooo , iII1111III1I , O0OoooO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 10065 , O00Ooo , O0OoooO0 , iII1111III1I )
 i1Oo0oO00o ( 'movies' , 'INFO' )
 if 53 - 53: OOoOoo . O00OOo00oo0o % iI11I1II1I1I % OOooOOo % iiII11i1I1IIi
def o0OoOoOOoOo0o ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0 = 'https://www.youtube.com/results?search_query=' + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 iiI1i11II = o0Oo0 . lower ( )
 I1 = O000oo ( iiI1i11II )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for iiOOooooO0Oo in next :
  iiOOooooO0Oo = 'https://www.youtube.com' + iiOOooooO0Oo
  I1IIII1i ( '[COLOR' + II + '] NEXT [/COLOR]' , iiOOooooO0Oo , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 , iIiii , i11iiiiI1i in IIIII11I1IiI :
  oOoOooOo0o0 . append ( iiI11ii1I1 )
  i1Oo0oO00o ( 'tvshows' , 'INFO' )
  oOOoo = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOOoo
  iiOOooooO0Oo = 'http://www.youtube.com' + iiOOooooO0Oo
  I1I11i ( '[COLORred]' + iIiii + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoo , oOOoo , i11iiiiI1i )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 , iIiii in IIIII11I1IiI :
   print 'im doing it'
   i1Oo0oO00o ( 'tvshows' , 'INFO' )
   oOOoo = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
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
     oOOoo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for oOOoo in oOOoo :
      oOOoo = 'http:' + oOOoo
     I1I11i ( '[COLORred]' + iIiii + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoo , O0o0Oo , '' )
   elif iiI11ii1I1 in oOoOooOo0o0 :
    pass
   elif 'user' in iiOOooooO0Oo or 'elete' in iiI11ii1I1 :
    pass
   elif 'hannel' in iiOOooooO0Oo :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + iiOOooooO0Oo
    I1 = O000oo ( iiOOooooO0Oo )
    IiIii1ii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 in IiIii1ii :
     if 'outube' in iiOOooooO0Oo or 'list' in iiOOooooO0Oo :
      pass
     elif 'atch' in iiOOooooO0Oo :
      iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '/watch?v=' , '' )
      I1I11i ( '[COLORred]' + iIiii + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0OOoO0 , 'http:' + oOo0OOoO0 , '' )
     else :
      pass
   else :
    I1I11i ( '[COLORred]' + iIiii + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoo , oOOoo , '' )
    if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
def iI11Ii111 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( I1 )
 for url in next :
  url = 'https://www.youtube.com' + url
  I1IIII1i ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 for oOo0OOoO0 , url , iiI11ii1I1 , iIiii , i11iiiiI1i in IIIII11I1IiI :
  oOoOooOo0o0 . append ( iiI11ii1I1 )
  i1Oo0oO00o ( 'tvshows' , 'INFO' )
  oOOoo = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + oOOoo
  url = 'http://www.youtube.com' + url
  I1I11i ( '[COLORred]' + iIiii + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoo , oOOoo , i11iiiiI1i )
 else :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
  for oOo0OOoO0 , url , iiI11ii1I1 , iIiii in IIIII11I1IiI :
   i1Oo0oO00o ( 'tvshows' , 'INFO' )
   oOOoo = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
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
     oOOoo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
     for oOOoo in oOOoo :
      oOOoo = 'http:' + oOOoo
     I1I11i ( '[COLORred]' + iIiii + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoo , O0o0Oo , '' )
   elif iiI11ii1I1 in oOoOooOo0o0 :
    pass
   elif 'user' in url or 'elete' in iiI11ii1I1 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    I1 = O000oo ( url )
    IiIii1ii = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
    for oOo0OOoO0 , url , iiI11ii1I1 in IiIii1ii :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      I1I11i ( '[COLORred]' + iIiii + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0OOoO0 , 'http:' + oOo0OOoO0 , '' )
     else :
      pass
   else :
    I1I11i ( '[COLORred]' + iIiii + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoo , oOOoo , '' )
    if 54 - 54: OOooOOo % OooOO000 . OOooOOo * IIi + OOooOOo % ooOoO0O00
    if 23 - 23: O00OOo00oo0o - IIi + iIi1i1ii1 - OOooOOo * OOooOOo . I1ii11iIi11i
def iiIi1i ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  iIii11iI1II = open ( IIIii1II1II )
  IIIII11I1IiI = re . compile ( 'plugin.video.GenieTv.+?2Flive%2F(.+?)%2F(.+?)%2F' ) . findall ( str ( iIii11iI1II ) )
  for I1II1I1I , OOo0oOO0o0oo0 in IIIII11I1IiI :
   if I1II1I1I == 'needs replacing' or OOo0oOO0o0oo0 == 'needs replacing' :
    oOo000O ( )
    if 1 - 1: iI11I1II1I1I
  I1IIII1i ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , oOOOo00O00oOo + 'GTV.png' , O0o0Oo , '' )
  if 54 - 54: ii - oOo0O0Ooo % Ii1I
def oO0Ooo0OooOOo ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOOO + ")" )
 oOo000O ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 71 - 71: OOoOoo + ooOoO0O00 * I1ii11iIi11i % I1ii11iIi11i / I1ii11iIi11i
def OoO00o0 ( ) :
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
 if 68 - 68: o0o00Oo0O
def II1iIII ( name ) :
 OoOOOOo = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , oOo0OOoO0 , OoOOOO0O0oO0 , iiOOooooO0Oo in IIIII11I1IiI :
  if OoOOOOo == 'Full List' :
   iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '.ts' , '.m3u8' )
   I1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiOOooooO0Oo ) . strip ( ) , 10012 , oOo0OOoO0 , oOo0OOoO0 , '' )
  else :
   OoOOOOo = ( OoOOOOo ) . replace ( 'World' , 'القنوات العربية' )
   if OoOOOOo in OoOOOO0O0oO0 :
    iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '.ts' , '.m3u8' )
    print iiOOooooO0Oo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    I1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiOOooooO0Oo ) . strip ( ) , 10012 , oOo0OOoO0 , oOo0OOoO0 , '' )
   else :
    pass
    if 15 - 15: IIiIi1iI * OOooOOo % OOoOoo . OOooOOo . iiII11i1I1IIi
def o0ooO0OOO ( name ) :
 OoOOOOo = name
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( I1 )
 for name , oOo0OOoO0 , iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = ( iiOOooooO0Oo ) . replace ( '.ts' , '.m3u8' )
  I1I11i ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( iiOOooooO0Oo ) . strip ( ) , 10012 , oOo0OOoO0 , oOo0OOoO0 , '' )
 else :
  I1I11i ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 10012 , '' , '' , '' )
  if 74 - 74: iIi1i1ii1 * Ii / O00OOo00oo0o
  if 75 - 75: o0o00Oo0O - ii + IIiIi1iI . oo0oO00 % IIiIiII11i
  if 9 - 9: IIiIiII11i * IIiIiII11i . Ii * iI11I1II1I1I
  if 18 - 18: oO0o . IIiIiII11i % OOooOOo % iIi1i1ii1
  if 87 - 87: iI11I1II1I1I . ii * OOooOOo
  if 100 - 100: oO0o / ooOoO0O00 - oOo0O0Ooo % iIi1i1ii1 - iI11I1II1I1I
  if 17 - 17: iiII11i1I1IIi / I11i % I1ii11iIi11i
  if 71 - 71: OOoOoo . O00OOo00oo0o . oO0o
  if 68 - 68: Ii % oo0oO00 * oO0o * OOoOoo * IIiIiII11i + o0o00Oo0O
  if 66 - 66: iiII11i1I1IIi % Ii1I % ii
  if 34 - 34: I11i / OooOO000 % o0o00Oo0O . oO0o . ooOoO0O00
  if 29 - 29: o0o00Oo0O . O00OOo00oo0o
def I1i11 ( ) :
 I1IIII1i ( 'Full Backup' , '' , 10061 , oOOOo00O00oOo + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  I1IIII1i ( 'Backup Genie Favourites' , iiOOooooO0Oo , 10062 , oOOOo00O00oOo + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( O0Oo000ooO00 ) :
  I1IIII1i ( 'Backup Ivue Config' , O0Oo000ooO00 , 10062 , oOOOo00O00oOo + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( oO0 ) :
  I1IIII1i ( 'Backup Kodi Favourites' , oO0 , 10062 , oOOOo00O00oOo + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 66 - 66: oo0oO00 * iI11I1II1I1I % iI11I1II1I1I * OOoOoo - IIiIi1iI - OOoOoo
  if 70 - 70: O00OOo00oo0o + oo0oO00
  if 93 - 93: O00OOo00oo0o + iIi1i1ii1
zip = oo00 . getSetting ( 'zip' )
i1i1 = xbmc . translatePath ( os . path . join ( zip ) )
def i1IiIi1 ( ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 22 - 22: iiII11i1I1IIi * o0o00Oo0O . IIiIiII11i - oO0o
  if 90 - 90: oo0oO00
  if 94 - 94: iiII11i1I1IIi / Ii1I * O00OOo00oo0o - OOooOOo
def I1Ii11II1I1 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = Ii1iIiII1ii1
  elif 'Ivue' in name :
   url = O0Oo000ooO00
  elif 'Kodi' in name :
   url = oO0
  i1IiIi1 ( )
  IiI1iI1IiiIi1 = open ( url ) . read ( )
  OoO0oo = os . path . join ( i1i1 , description . split ( 'Your ' ) [ 1 ] )
  OOoO = open ( OoO0oo , mode = 'w' )
  OOoO . write ( IiI1iI1IiiIi1 )
  OOoO . close ( )
 else :
  if 'guisettings.xml' in description :
   OoOoO0O = open ( os . path . join ( i1i1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o0i1I11iI1iiI = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   IIIII11I1IiI = re . compile ( o0i1I11iI1iiI ) . findall ( OoOoO0O )
   for type , I1ii , oO0oI1I1 in IIIII11I1IiI :
    oO0oI1I1 = oO0oI1I1 . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , I1ii , oO0oI1I1 ) )
  else :
   OoO0oo = os . path . join ( url )
   IiI1iI1IiiIi1 = open ( os . path . join ( i1i1 , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOoO = open ( OoO0oo , mode = 'w' )
   OOoO . write ( IiI1iI1IiiIi1 )
   OOoO . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 99 - 99: IIiIi1iI / iI11I1II1I1I - iIi1i1ii1 * Ii1I % oOo0O0Ooo
 if 13 - 13: oO0o
 if 70 - 70: O00OOo00oo0o + o0o00Oo0O . oo0oO00 * iIi1i1ii1
 if 2 - 2: ii . IIi . OOoOoo
def I1iIII1IiiI ( ) :
 OOoooOoO0Oo = 1
 i1IiIi1 ( )
 Oo000iiIiII11i1 = xbmc . translatePath ( os . path . join ( i1i1 , 'Build Backup' , 'Full Backup' , '' ) )
 oOo00Ooo0o0 = xbmc . translatePath ( os . path . join ( i1i1 , 'Build Backup' , 'my_full_backup.zip' ) )
 i1IiII1i1I = xbmc . translatePath ( os . path . join ( i1i1 , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( Oo000iiIiII11i1 ) :
  os . makedirs ( Oo000iiIiII11i1 )
 iI1ii1ii1I = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not iI1ii1ii1I ) : return False , 0
 iI1IIi11i1I1 = iI1ii1ii1I
 O00oo = xbmc . translatePath ( os . path . join ( Oo000iiIiII11i1 , iI1IIi11i1I1 + '.zip' ) )
 OoOo0oO0o = [ 'plugin.video.GenieTv' ]
 o0OoOo00ooO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 i111i = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 II1III1i1iiI = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 I11i11i1 = "Creating full backup of existing build"
 OOOii1i1iiI = "Creating Community Build"
 Oo0oOo0ooOOOo = "Archiving..."
 OoO0000o = ""
 o0Ii1 = "Please Wait"
 IIi1IiII ( Oo0o0000o0o0 , O00oo , OOOii1i1iiI , Oo0oOo0ooOOOo , OoO0000o , o0Ii1 , i111i , II1III1i1iiI )
 time . sleep ( 1 )
 o0IIIIiI11I = xbmc . translatePath ( os . path . join ( Oo000iiIiII11i1 , iI1IIi11i1I1 + '_guisettings.zip' ) )
 iiiI11iIIi1 = zipfile . ZipFile ( o0IIIIiI11I , mode = 'w' )
 try :
  iiiI11iIIi1 . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 iiiI11iIIi1 . close ( )
 if OOoooOoO0Oo == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + oOo00Ooo0o0 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + O00oo + '[/COLOR]' )
  if 72 - 72: OooOO000 * IIi
def IIi1IiII ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 oooo = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 iiiIIIii = len ( sourcefile )
 ooOoo00 = [ ]
 Ii11IiI = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for o00oOoO0Oo , Ii1iiII1i , oO00O in os . walk ( sourcefile ) :
  for file in oO00O :
   Ii11IiI . append ( file )
 IIiI11 = len ( Ii11IiI )
 for o00oOoO0Oo , Ii1iiII1i , oO00O in os . walk ( sourcefile ) :
  Ii1iiII1i [ : ] = [ I11i11I for I11i11I in Ii1iiII1i if I11i11I not in exclude_dirs ]
  oO00O [ : ] = [ OOoO for OOoO in oO00O if OOoO not in exclude_files ]
  for file in oO00O :
   ooOoo00 . append ( file )
   oooO00o00 = len ( ooOoo00 ) / float ( IIiI11 ) * 100
   o0oOoO00o . update ( int ( oooO00o00 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   iII11iiIIi11 = os . path . join ( o00oOoO0Oo , file )
   if not 'temp' in Ii1iiII1i :
    if not 'plugin.program.originwizard' in Ii1iiII1i :
     import time
     Iiii11I = '01/01/1980'
     OO0ooo0 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( iII11iiIIi11 ) ) )
     if OO0ooo0 > Iiii11I :
      oooo . write ( iII11iiIIi11 , iII11iiIIi11 [ iiiIIIii : ] )
 oooo . close ( )
 o0oOoO00o . close ( )
 if 7 - 7: Ii1I - oo0oO00 * IIi + I11i . Ii1I
 if 85 - 85: o0o00Oo0O
def oO0oo ( ) :
 IIiiiI1iIII ( )
 I1IIII1i ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , oOOOo00O00oOo + 'scoob.png' , O0o0Oo , '' )
 if 32 - 32: ii . oO0o / I1ii11iIi11i * I11i / I11i * iIi1i1ii1
 if 19 - 19: iIi1i1ii1
def O0o00oO0oOO ( ) :
 IIiiiI1iIII ( )
 OooOoOO0 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  i1II ( )
 if iI1i11iII111 == 1 :
  ii1iIi1iIiI1i ( )
 if iI1i11iII111 == 2 :
  O0OO0oOOo ( )
 if iI1i11iII111 == 3 :
  o0OoOoOOoOo0o ( )
  if 49 - 49: iI11I1II1I1I * ooOoO0O00 . ii
  if 90 - 90: I11i % Ii1I - iI11I1II1I1I % OOooOOo
  if 8 - 8: OOooOOo * I1ii11iIi11i / OOoOoo % iIi1i1ii1 - oOo0O0Ooo
  if 71 - 71: OooOO000
  if 23 - 23: ooOoO0O00 . iI11I1II1I1I . IIi . o0o00Oo0O % iIi1i1ii1 % Ii
  if 11 - 11: o0o00Oo0O - IIiIiII11i . IIi . iIi1i1ii1 % O00OOo00oo0o
  if 21 - 21: I1ii11iIi11i / OooOO000 . O00OOo00oo0o * ii + iiII11i1I1IIi - ooOoO0O00
  if 58 - 58: Ii1I
  if 2 - 2: IIiIiII11i / O00OOo00oo0o
def OoOoO0oOOooo ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   IIi1IIIi ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvbWFpbi5waHA=' ) ) , O00Ooo , iiI11ii1I1 )
  if iI1i11iII111 == 1 :
   O0iIiIIIIIii ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if iI1i11iII111 == 2 :
   oo0 ( )
  if iI1i11iII111 == 3 :
   Ooii1IIi1ii ( )
  if iI1i11iII111 == 4 :
   oo0OoOOooO ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if iI1i11iII111 == 5 :
   o0o0OO0o00o0O ( )
  if iI1i11iII111 == 6 :
   IIIIIIi1i ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if iI1i11iII111 == 7 :
   iiiii11I1 ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if iI1i11iII111 == 8 :
   Ii1OOOo ( str ( ooOO0O0ooOooO ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if iI1i11iII111 == 9 :
   I1iI1IiI ( )
  if iI1i11iII111 == 10 :
   i1i1Ii1I ( )
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
  if 11 - 11: IIi - OOooOOo - I11i * OOooOOo + IIiIi1iI
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 62 - 62: oOo0O0Ooo * Ii . OooOO000
def I1iIIIiI ( ) :
 IIiiiI1iIII ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  OooOoOO0 = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   OoiI1I1 ( )
  if iI1i11iII111 == 1 :
   i11i1 ( )
  if iI1i11iII111 == 2 :
   iIiIi11 ( )
  if iI1i11iII111 == 3 :
   o00o0 ( iiOOooooO0Oo )
  if iI1i11iII111 == 4 :
   I1III1i1I ( iiOOooooO0Oo )
  if iI1i11iII111 == 5 :
   oOOo0O00o ( )
  if iI1i11iII111 == 6 :
   OOOOO0 ( url = 'http://www.iplocation.net/' , inc = 1 )
  if iI1i11iII111 == 7 :
   Ooo0Oo0o ( )
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
  if 85 - 85: oOo0O0Ooo
  if 7 - 7: ooOoO0O00 + IIi % OooOO000 / I11i + ooOoO0O00
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 41 - 41: iIi1i1ii1 + Ii / OOoOoo % Ii1I
 if 22 - 22: OOooOOo % I11i * iIi1i1ii1 - Ii1I + I11i - I1ii11iIi11i
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
 if 15 - 15: IIi
 if 31 - 31: OooOO000 / ooOoO0O00 . oO0o
def OOOoo ( ) :
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
 if 25 - 25: Ii1I + oo0oO00 + ii . IIiIiII11i . OooOO000
def IiIi1I1 ( ) :
 IIiiiI1iIII ( )
 I1I11i ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , oOOOo00O00oOo + 'MyLocalZIP.png' , O0o0Oo , '' )
 I1I11i ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , oOOOo00O00oOo + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 66 - 66: IIiIi1iI * OOooOOo
def II1 ( ) :
 IIiiiI1iIII ( )
 I1I11i ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , oOOOo00O00oOo + 'FTV4.png' , O0o0Oo , '' )
 I1I11i ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( ooOO0O0ooOooO ) + '/wizard/customftv/settings.xml' , 17 , oOOOo00O00oOo + 'FTV3.png' , O0o0Oo , '' )
 I1I11i ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , oOOOo00O00oOo + 'FTV1.png' , O0o0Oo , '' )
 I1I11i ( 'RESET FTV DATABASE' , 'url' , 18 , oOOOo00O00oOo + 'FTV2.png' , O0o0Oo , '' )
 if 91 - 91: IIi + O00OOo00oo0o . iiII11i1I1IIi
 if 15 - 15: iiII11i1I1IIi
 if 94 - 94: O00OOo00oo0o % IIiIiII11i * ooOoO0O00 * iI11I1II1I1I
def oO0o0 ( ) :
 IIiiiI1iIII ( )
 OooOoOO0 = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  oO0oOoo0O ( )
 if iI1i11iII111 == 0 :
  II1iI11 ( iiOOooooO0Oo )
 if iI1i11iII111 == 0 :
  O00o0O ( iiOOooooO0Oo )
  if 85 - 85: IIi * ooOoO0O00 % oOo0O0Ooo - IIiIi1iI
  if 37 - 37: OOoOoo . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
  if 83 - 83: OOoOoo / O00OOo00oo0o
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 64 - 64: oO0o % OOoOoo . O00OOo00oo0o % oO0o + iiII11i1I1IIi * OOoOoo
def OOOO00OooO ( ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1Oo00 )
 for oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , oOo0OOoO0 , oOo0OOoO0 , '' )
 i1Oo0oO00o ( 'tvshows' , 'INFO' )
 if 64 - 64: oO0o . oOo0O0Ooo - ii . IIiIi1iI - OooOO000
def O0oO0o000o ( url ) :
 i1Oo00 = O000oo ( i11i11II11i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 17 - 17: IIiIiII11i + I1ii11iIi11i . O00OOo00oo0o
def oO0oOoo0O ( ) :
 IIiiiI1iIII ( )
 I1IIII1i ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 36 , oOOOo00O00oOo + 'GothamSkins.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( ooOO0O0ooOooO ) , 37 , oOOOo00O00oOo + 'HelixSkins.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , oOOOo00O00oOo + 'IsengaardSkins.png' , O0o0Oo , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 12 - 12: O00OOo00oo0o + IIi + iiII11i1I1IIi . OOoOoo / iIi1i1ii1
def i1IoOOoooO0O0 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + ii1O0ooooo000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 97 - 97: Ii % oo0oO00 / I1ii11iIi11i / I1ii11iIi11i
def OoO00ooO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iiO0o0O0oo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 100 - 100: OOoOoo . iIi1i1ii1 - iI11I1II1I1I . Ii / IIiIiII11i
def o0oO0OO00oo0o ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + I1II1Oo000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 69 - 69: Ii1I + OooOO000 * o0o00Oo0O . IIi % OOooOOo
def O0O000O ( url ) :
 i1Oo00 = O000oo ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 22 - 22: oo0oO00
def II1iI11 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + i1i11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 40 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 86 - 86: iIi1i1ii1
def IiII1i1iI ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + O0OOO00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 62 - 62: Ii + OOooOOo + ooOoO0O00
def Iii1IIII11I ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  oOOoO0O ( )
 if iI1i11iII111 == 1 :
  i1IiiiiiIiII ( )
 if iI1i11iII111 == 2 :
  iI ( )
  if 12 - 12: ii / o0o00Oo0O + IIiIiII11i * Ii1I
  if 46 - 46: IIiIiII11i - OOoOoo * ii / oo0oO00 % OOoOoo
  if 11 - 11: iI11I1II1I1I . OOooOOo / OOoOoo % IIiIi1iI
  if 61 - 61: IIiIi1iI - IIi + IIi
def i1IiiiiiIiII ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iii in IIIII11I1IiI :
  iII1iii ( 'Android Apps' + iii , 'https://www.apkfiles.com' + iiOOooooO0Oo , 30035 , oOOOo00O00oOo + 'apps.png' )
 for iiOOooooO0Oo , iii in i1I :
  iII1iii ( 'Android Games' + iii , 'https://www.apkfiles.com' + iiOOooooO0Oo , 30035 , oOOOo00O00oOo + 'GAMES.png' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def IiIIII1iiIIi ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '/cat' in url :
   iII1iii ( ( iiI11ii1I1 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def i1I1IiI1ii ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '/app' in url :
   iII1iii ( ( iiI11ii1I1 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , oOOOo00O00oOo + 'APK.png' )
def O00OOoOOOO00O ( url ) :
 OoO000O0Oo = O000oo ( url )
 Ooo0OOO = url
 if "page=" in str ( url ) :
  Ooo0OOO = url . split ( '?' ) [ 0 ]
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'apk' in url :
   I1I11i ( ( iiI11ii1I1 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + oOo0OOoO0 )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 I1I11i ( 'Next Page' , Ooo0OOO + str ( i1I ) , 30037 , oOOOo00O00oOo + 'Next.png' )
def ooooOoo0OO ( name , url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 name = name
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  Oo0O0000Oo00o ( name , url , 'Brackets' )
def iI ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0 = 'https://www.apkfiles.com/search?q=' + ( o0oOOoOOO ) . replace ( ' ' , '+' ) + '&search_type=1'
 iiI1i11II = o0Oo0 . lower ( )
 O00OOoOOOO00O ( iiI1i11II )
 if 20 - 20: oO0o . oOo0O0Ooo * Ii / Ii
def o00iIiiiII ( url ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( Ii1I1 , 'Download' ) )
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
 if 71 - 71: OOooOOo + iI11I1II1I1I * oo0oO00 . O00OOo00oo0o % Ii % iI11I1II1I1I
def OooOO0oOOo0O ( url ) :
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
 if 42 - 42: OooOO000 / I11i + I1ii11iIi11i . I1ii11iIi11i % IIi
 if 16 - 16: ooOoO0O00 + oO0o % OOooOOo + iIi1i1ii1 * I1ii11iIi11i
def i1o0oo0 ( name , url , description ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 ii1 = os . path . join ( oOO0O00Oo0O0o , name )
 try :
  os . remove ( ii1 )
 except :
  pass
 downloader . download ( url , ii1 , o0oOoO00o )
 OoO0OOoO0Oo0 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print OoO0OOoO0Oo0
 print '======================================='
 extract . all ( ii1 , OoO0OOoO0Oo0 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 91 - 91: IIiIiII11i
 if 53 - 53: oO0o % I11i / IIi % OOoOoo % oO0o % ii
 if 31 - 31: oOo0O0Ooo
 if 73 - 73: IIiIi1iI . o0o00Oo0O / I11i - ii % Ii
 if 80 - 80: iIi1i1ii1 / IIiIi1iI % o0o00Oo0O . I1ii11iIi11i
def oOOoO0O ( ) :
 i1Oo00 = O000oo ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , iiOOooooO0Oo , i1I1i1 , O0OoooO0 , oOiI111I1III in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 80003 , i1I1i1 , oOOOo00O00oOo + 'APKToolsB.png' , oOiI111I1III )
def i111IiiI1Ii ( apk , ret = None ) :
 if apk == "kodi" :
  OooOOOOOo = "https://kodi.tv/download/"
  i1Oo00 = O000oo ( OooOOOOOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1Oo00 )
  if len ( IIIII11I1IiI ) == 1 :
   i1I11ii = IIIII11I1IiI [ 0 ] [ 0 ]
   iI1IIi11i1I1 = IIIII11I1IiI [ 0 ] [ 1 ]
   o0ooO00O0O = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( i1I11ii , iI1IIi11i1I1 )
  if ret == 'version' : return i1I11ii
  else : return o0ooO00O0O
 elif apk == "spmc" :
  iiiI1iI1 = 'https://github.com/koying/SPMC/releases/latest/'
  i1Oo00 = O000oo ( iiiI1iI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1Oo00 )
  i1I11ii = re . sub ( '<[^<]+?>' , '' , IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  o0ooO00O0O = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( i1I11ii , i1I11ii )
  if ret == 'version' : return i1I11ii
  else : return o0ooO00O0O
def Oo0O0000Oo00o ( name , url , Brackets ) :
 if Ii1I1I1i1Ii ( ) == 'android' :
  I1oOoO0OOO00O = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not I1oOoO0OOO00O : OOOOO0o0OOo ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  I11I11I11IiIi = name
  if I1oOoO0OOO00O :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not IIIIiII1i ( url ) == True : OOOOO0o0OOo ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % I11I11I11IiIi , '' , 'Please Wait' )
   ii1 = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( ii1 )
   except : pass
   downloader . download ( url , ii1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    iiiI11iIIi1 = zipfile . ZipFile ( ii1 )
    for file in iiiI11iIIi1 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as OOoO :
       OOii1ii1i11I1I = file . split ( '/' ) [ 1 ]
       OOoO . write ( iiiI11iIIi1 . read ( file ) )
       xbmc . sleep ( 500 )
       OOoO . close ( )
       try :
        os . remove ( ii1 )
       except :
        pass
       ii1 = os . path . join ( i1iiIII111ii , OOii1ii1i11I1I )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ii1 + '")' )
  else : OOOOO0o0OOo ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : OOOOO0o0OOo ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 41 - 41: OOoOoo
 if 3 - 3: OOoOoo + IIiIiII11i / iI11I1II1I1I
 if 10 - 10: IIiIiII11i . o0o00Oo0O
 if 31 - 31: oo0oO00 / Ii / o0o00Oo0O
def iiI1ii ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1Oo00 = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1Oo00 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iiOOooooO0Oo = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + iiOOooooO0Oo )
  O0OooOO ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , iiOOooooO0Oo )
  if 49 - 49: OOoOoo / IIiIi1iI / IIi
def O0OooOO ( name , url ) :
 if Ii1I1I1i1Ii ( ) == 'android' :
  I1oOoO0OOO00O = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not I1oOoO0OOO00O : OOOOO0o0OOo ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  I11I11I11IiIi = name
  if I1oOoO0OOO00O :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not IIIIiII1i ( url ) == True : OOOOO0o0OOo ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % I11I11I11IiIi , '' , 'Please Wait' )
   ii1 = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( ii1 )
   except : pass
   downloader . download ( url , ii1 , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + ii1 + '")' )
  else : OOOOO0o0OOo ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : OOOOO0o0OOo ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 25 - 25: oOo0O0Ooo % o0o00Oo0O + ooOoO0O00 - IIiIi1iI
 if 38 - 38: I11i % O00OOo00oo0o + Ii + OooOO000 + IIiIi1iI / Ii
def o0OOOOOo0 ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'INFO' )
 if 57 - 57: iI11I1II1I1I + iI11I1II1I1I
 if 56 - 56: oo0oO00 + IIiIi1iI
def II1i11I ( url ) :
 i1Oo00 = O000oo ( ooOO0O0ooOooO + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 30015 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 32 - 32: IIiIiII11i + OOooOOo % IIiIi1iI / OOooOOo + Ii1I
def IiI11I111 ( url , iconimage , fanart ) :
 i1Oo00 = O000oo ( url )
 IiIii1I1I = url
 oOo0OOoO0 = iconimage
 fanart = fanart
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for ooo0O , iiI11ii1I1 in IIIII11I1IiI :
  if '.mp4' in iiI11ii1I1 :
   I1I11i ( 'Watch VIDEO' , url + '/' + ooo0O , 222 , oOo0OOoO0 , fanart , '' )
  if 'description' in iiI11ii1I1 :
   I1I11i ( 'Read Description' , url + '/' + ooo0O , 30017 , oOo0OOoO0 , fanart , '' )
  if 'images' in iiI11ii1I1 :
   I1IIII1i ( 'View Images' , url + '/' + ooo0O , 30018 , oOo0OOoO0 , fanart , '' )
  if 'url' in iiI11ii1I1 :
   I1I11i ( 'Install Build On Android' , url + '/' + ooo0O , 30016 , oOo0OOoO0 , fanart , '' )
  if 'url' in iiI11ii1I1 :
   I1I11i ( 'Install Build On Pc' , url + '/' + ooo0O , 30019 , oOo0OOoO0 , fanart , '' )
 i1Oo0oO00o ( 'movies' , 'INFO' )
 if 54 - 54: o0o00Oo0O - OooOO000 . IIi % OooOO000 + OooOO000
def i1iI1Iiii1I ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  I1iII ( url )
  if 29 - 29: ooOoO0O00 % OooOO000 / OOoOoo + OOooOOo - IIi - Ii1I
def OoiiI1i111 ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1Oo00 )
 for url in IIIII11I1IiI :
  oO0O0o0O ( url )
  if 100 - 100: OOooOOo % I1ii11iIi11i
def OoOOiI ( url ) :
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1Oo00 )
 for IIiiiiIiI1III in IIIII11I1IiI :
  iiIiI1i1 ( 'Description:' , IIiiiiIiI1III )
  if 26 - 26: ooOoO0O00
def i111I1 ( url ) :
 i1Oo00 = O000oo ( url )
 url = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1Oo00 )
 for ooo0O , iiI11ii1I1 in IIIII11I1IiI :
  if 'png' in iiI11ii1I1 :
   I1I11i ( 'image' , '' , '' , url + '/' + ooo0O , url + '/' + ooo0O , '' )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 63 - 63: o0o00Oo0O . oOo0O0Ooo . o0o00Oo0O * iI11I1II1I1I
def oOo0O ( name , url , description ) :
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
 if 30 - 30: iIi1i1ii1 . Ii1I / IIi
 if 2 - 2: OOoOoo % oOo0O0Ooo - O00OOo00oo0o
def oO0O0o0O ( url ) :
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
 OoiI1I1 ( )
 if 79 - 79: ii / Ii1I . o0o00Oo0O
def I1iII ( url ) :
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
 OoiI1I1 ( )
 if 79 - 79: oo0oO00 - IIiIiII11i
def Ii1iiI1 ( name , url , description ) :
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
 OoiI1I1 ( )
 if 76 - 76: iIi1i1ii1 * iI11I1II1I1I
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
  iiI1iI = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  OOoO . write ( iiI1iI . rstrip ( '\r\n' ) + '\n' )
def OoiI1I1 ( ) :
 iI1i11iII111 = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iI1i11iII111 == 0 : return
 elif iI1i11iII111 == 1 : pass
 Ooo00O0 = Ii1I1I1i1Ii ( )
 OOO ( "Platform: " + str ( Ooo00O0 ) )
 os . _exit ( 1 )
 OOO ( "Force close failed!  Trying alternate methods." )
 if Ooo00O0 == 'osx' :
  OOO ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif Ooo00O0 == 'linux' :
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
 elif Ooo00O0 == 'android' :
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
 elif Ooo00O0 == 'windows' :
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
  if 70 - 70: oOo0O0Ooo - IIiIi1iI - oO0o - OOooOOo . Ii % ooOoO0O00
  if 1 - 1: oo0oO00 / ooOoO0O00
  if 74 - 74: iiII11i1I1IIi / ii / I1ii11iIi11i * Ii . IIiIiII11i . ii
def O00o0O ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for Ooi1IIii11i1I1 , Ii1iiII1i , oO00O in os . walk ( url ) :
  for file in oO00O :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    OoOoO0O = open ( ( os . path . join ( Ooi1IIii11i1I1 , file ) ) ) . read ( )
    Ii1I1O0oo00oOOO0o = OoOoO0O . replace ( Oo0o0000o0o0 , 'special://home/' )
    OOoO = open ( ( os . path . join ( Ooi1IIii11i1I1 , file ) ) , mode = 'w' )
    OOoO . write ( str ( Ii1I1O0oo00oOOO0o ) )
    OOoO . close ( )
 OoiI1I1 ( )
 if 5 - 5: I11i / oOo0O0Ooo % iIi1i1ii1 . OOoOoo
def oo0 ( ) :
 iII1iii ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , oOOOo00O00oOo + 'RadioNomy.png' )
 iII1iii ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , oOOOo00O00oOo + 'RadioNomy.png' )
 iII1iii ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , oOOOo00O00oOo + 'RadioNomy.png' )
 if 86 - 86: ooOoO0O00 * OOooOOo . o0o00Oo0O - iIi1i1ii1 - I11i - OOooOOo
def i11IiI ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def OoIi1I1I ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
def oOOoOOO0oOoo ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1I :
  iII1iii ( ( '[COLOR' + II + ']Filter - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , oOOOo00O00oOo + 'RadioNomy.png' )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']Stream - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oOo0OOoO0 )
def o0O0ooooooo00 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( url )
def I1111ii11IIII ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO
 IiIi1II111I = 'https://www.radionomy.com/en/search/index?query=' + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 I1 = O000oo ( IiIi1II111I )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']Stream - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + iiOOooooO0Oo , 70005 , oOo0OOoO0 )
  if 80 - 80: iIi1i1ii1 / IIi
  if 21 - 21: I1ii11iIi11i - iI11I1II1I1I - O00OOo00oo0o
def o0o0OO0o00o0O ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , 'http://www.listenlive.eu/' + iiOOooooO0Oo , 10111113 , oOOOo00O00oOo + 'radio.png' )
def oo0OoOOooO ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'radio.png' )
  if 1 - 1: oOo0O0Ooo * IIi + iIi1i1ii1 + oOo0O0Ooo - Ii
def O0o ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.toonjet.com/' + iiOOooooO0Oo , 8051 , oOOOo00O00oOo + 'classictoons.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def O00oOOooO ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
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
   iII1iii ( ( oOo0OOoO0 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , oOOOo00O00oOo + 'vod.png' )
 for url in i1I :
  iII1iii ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , oOOOo00O00oOo + 'Next.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def IiIIii1iiI ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , oOOOo00O00oOo + 'classictoons.png' )
  if 7 - 7: I11i
  if 18 - 18: ii + I11i . o0o00Oo0O + OOoOoo * ooOoO0O00 . oO0o
def i1i1Ii1I ( ) :
 o0OO0oooo ( 'Audio Books' , '' , 30011 , oOOOo00O00oOo + 'AudioBooks.png' , oOOOo00O00oOo + 'AudioBooks.png' , '' )
 o0OO0oooo ( 'Kids Audio Books' , '' , 30006 , oOOOo00O00oOo + 'KidsAudioBooks.png' , oOOOo00O00oOo + 'KidsAudioBooks.png' , '' )
 if 40 - 40: O00OOo00oo0o - OOooOOo * iiII11i1I1IIi - OOoOoo / OOooOOo
def OO0oo ( ) :
 o0OO0oooo ( 'All' , '' , 30001 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 o0OO0oooo ( 'Popular' , '' , 30012 , oOOOo00O00oOo + 'POPULARv.png' , oOOOo00O00oOo + 'POPULARv.png' , '' )
 o0OO0oooo ( 'Search' , '' , 30013 , oOOOo00O00oOo + 'Search.png' , oOOOo00O00oOo + 'Search.png' , '' )
 if 90 - 90: O00OOo00oo0o + Ii1I / O00OOo00oo0o + OOoOoo / IIiIiII11i
def o00oO0O0oo0o ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for iiI11ii1I1 , iiOOooooO0Oo , iIi11I11 in IIIII11I1IiI :
  if 'Parent' in iiI11ii1I1 :
   pass
  elif '2' in iIi11I11 :
   o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 40 - 40: iI11I1II1I1I
def oOoOo0o00o ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for iiI11ii1I1 , iiOOooooO0Oo , iIi11I11 in IIIII11I1IiI :
  if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
   if '1' in iIi11I11 :
    o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '2' in iIi11I11 :
    o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   elif '3' in iIi11I11 :
    o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 2 - 2: IIiIiII11i
    if 54 - 54: iIi1i1ii1 . ii % I1ii11iIi11i
def ii111I11Ii ( ) :
 I1 = O000oo ( I1IIIii + 'books' + IIiiiiiiIi1I1 )
 IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( I1 )
 for iiI11ii1I1 , iiOOooooO0Oo , iIi11I11 in IIIII11I1IiI :
  if '1' in iIi11I11 :
   o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 3010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '2' in iIi11I11 :
   o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '3' in iIi11I11 :
   o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , iiOOooooO0Oo , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 6 - 6: iIi1i1ii1
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 77 - 77: ooOoO0O00 + oO0o . oOo0O0Ooo * IIi / OOoOoo / iIi1i1ii1
def oOoo ( url ) :
 ooo0O = url
 I1 = O000oo ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1 )
 for url , iiI11ii1I1 in i1I :
  if 'mp3' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ooo0O + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ooo0O + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , ooo0O + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif '/' in iiI11ii1I1 :
   o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooo0O + url , 30009 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 57 - 57: I11i / O00OOo00oo0o
   if 13 - 13: ii + oO0o
   if 32 - 32: o0o00Oo0O + oo0oO00 % I1ii11iIi11i
def iI1iI ( url ) :
 I1 = O000oo ( url )
 ooo0O = url
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
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooo0O + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooo0O + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , ooo0O + url , 30010 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 100 - 100: IIiIi1iI / IIiIi1iI - IIi % IIi * oo0oO00 / OOoOoo
   if 32 - 32: oOo0O0Ooo + Ii1I - oo0oO00 + Ii1I / ooOoO0O00 * oo0oO00
def o0OoOoooo0 ( ) :
 o0OO0oooo ( 'A-Z' , '' , 30007 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 o0OO0oooo ( 'All' , '' , 30003 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 o0OO0oooo ( 'Search' , '' , 30014 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
 if 60 - 60: oOo0O0Ooo % oo0oO00 / I11i % oo0oO00 * Ii / OooOO000
def i1Ii11IIi1 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 in IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + iiOOooooO0Oo + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oOo0OOoO0 :
   pass
  else :
   o0OO0oooo ( oOo0OOoO0 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( iiOOooooO0Oo ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oOo0OOoO0 + '.gif' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 7 - 7: iI11I1II1I1I - ooOoO0O00
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 10 - 10: O00OOo00oo0o % o0o00Oo0O / oOo0O0Ooo % iiII11i1I1IIi
 if 25 - 25: IIiIiII11i / oO0o
def oo0OoOO0000 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '</a>' in iiI11ii1I1 :
   pass
  elif '(' in iiI11ii1I1 :
   o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 2 - 2: iIi1i1ii1 * Ii1I * ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 73 - 73: OOooOOo + I1ii11iIi11i
def oOo ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
   if '</a>' in iiI11ii1I1 :
    pass
   elif '(' in iiI11ii1I1 :
    o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   else :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
    if 19 - 19: I11i
    if 73 - 73: O00OOo00oo0o * I1ii11iIi11i * OOooOOo
def Oo0OOo ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if '</a>' in iiI11ii1I1 :
   pass
  elif '(' in iiI11ii1I1 :
   o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30005 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
  else :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + iiOOooooO0Oo , 30004 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 44 - 44: iiII11i1I1IIi * I11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: IIi % iiII11i1I1IIi * Ii / oo0oO00 % IIi
 if 70 - 70: OOooOOo / IIiIiII11i % IIiIi1iI - OooOO000
def I1II1IiI1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  ooo0O = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( ooo0O )
  if 26 - 26: IIi * I1ii11iIi11i
def i1iI1Ii11Ii1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '<p align' in iiI11ii1I1 :
   pass
  elif '&nbsp;' in iiI11ii1I1 :
   pass
  else :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 10012 , oOOOo00O00oOo + 'KodibleAudioBooks.png' , oOOOo00O00oOo + 'KodibleAudioBooks.png' , '' )
   if 82 - 82: o0o00Oo0O
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 70 - 70: iiII11i1I1IIi - I1ii11iIi11i / ii % ii
 if 95 - 95: ii % ii . iIi1i1ii1
def OO0oO0o ( ) :
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
def III1ii ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 iII1ii = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , oOo0OOoO0 , oOo0OOoO0 , iiI11ii1I1 )
 for url , iiI11ii1I1 in iII1ii :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in next :
  I1IIII1i ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def o0oOoO00 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 oO0O = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 oOO000 = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( I1 )
 OoOooO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url in oOO000 :
  I1IIII1i ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 for url , iiI11ii1I1 in oO0O :
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
 else :
  I1IIII1i ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
def OoO0o00OOOOO ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'watchcartoons.png' , '' , '' )
  if 19 - 19: OooOO000 * I1ii11iIi11i . OooOO000 . oO0o / oO0o - oo0oO00
def O0000 ( ) :
 I1 = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if '9cart' in iiOOooooO0Oo :
   iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 20001 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 9 - 9: O00OOo00oo0o * OOoOoo * O00OOo00oo0o
def ooOO ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( I1 )
 I1II1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if '9cart' in url :
   iII1iii ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   iII1iii ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
 for url , iiI11ii1I1 in I1II1 :
  if '9cart' in url :
   iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 86 - 86: iIi1i1ii1 . IIi / OOoOoo - ii
def iii1IiI1i ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20003 , oOo0OOoO0 )
 for url , iiI11ii1I1 in i1I :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 93 - 93: ooOoO0O00 % OOooOOo / iI11I1II1I1I * I11i . o0o00Oo0O % IIi
def OOOO00OOO00 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'Watch' in url :
   iII1iii ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
   if 23 - 23: o0o00Oo0O
def I1iI11IiiI11i ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' )
  if 37 - 37: I11i % ooOoO0O00 - I11i + iI11I1II1I1I + O00OOo00oo0o
def oOoO00O ( url ) :
 url = cloudflare . source ( url )
 II1IIIii ( url )
 if 31 - 31: IIiIi1iI . OOooOOo % OOooOOo % I1ii11iIi11i % oOo0O0Ooo * OooOO000
def I1i1iII1I11 ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in IIIII11I1IiI :
  II1IIIii ( url )
  if 55 - 55: IIiIi1iI % I1ii11iIi11i % I11i
  if 29 - 29: OOoOoo / iI11I1II1I1I + Ii1I % OooOO000 % iiII11i1I1IIi
def III111i11IiI ( ) :
 if 46 - 46: iI11I1II1I1I
 I1IIII1i ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , oOOOo00O00oOo + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 70 - 70: ooOoO0O00 . iiII11i1I1IIi
def O0OO0oOOo ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 74 - 74: iiII11i1I1IIi
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( I1 )
 if 58 - 58: iI11I1II1I1I * oO0o * O00OOo00oo0o * IIiIi1iI . ii
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
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
    if 6 - 6: Ii1I - oo0oO00 * Ii + OOooOOo / IIiIi1iI % IIi
    if 38 - 38: IIi % OOoOoo % IIiIiII11i - I1ii11iIi11i - iI11I1II1I1I
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 9 - 9: I11i % Ii1I . Ii1I
def ooO00O0O0 ( url ) :
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
 if 28 - 28: ii % oo0oO00 + Ii1I + o0o00Oo0O . O00OOo00oo0o
def ooOO0OOO00o ( url ) :
 OoO000O0Oo = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 in i1I :
  OoOoO0ooooO0 = oOo0OOoO0
 I1II1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1II1 :
  I1IIII1i ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10007 , OoOoO0ooooO0 )
  if 4 - 4: I1ii11iIi11i - oO0o - Ii * O00OOo00oo0o / iIi1i1ii1 - IIi
  if 45 - 45: I11i % I1ii11iIi11i * ooOoO0O00 - o0o00Oo0O
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 82 - 82: IIiIiII11i / OooOO000
def OOoOi1IiiI ( url , IMAGE ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  print iiI11ii1I1 + '     ' + url
  if 'easy' in url :
   O0OOO0 ( url )
   if 61 - 61: IIiIi1iI . Ii + oo0oO00
   if 8 - 8: iI11I1II1I1I
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 55 - 55: oo0oO00
def O0OOO0 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( url )
  if 37 - 37: OOoOoo / Ii / I1ii11iIi11i
  if 97 - 97: O00OOo00oo0o . iiII11i1I1IIi / oOo0O0Ooo
  if 83 - 83: iiII11i1I1IIi - Ii1I * oo0oO00
def i1i1ii ( ) :
 if 90 - 90: I1ii11iIi11i * oOo0O0Ooo
 I1IIII1i ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , oOOOo00O00oOo + 'StandUp.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , oOOOo00O00oOo + 'SearchComedian.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , oOOOo00O00oOo + 'Others.png' , O0o0Oo , '' )
 if 75 - 75: Ii1I - OOooOOo * Ii . ii - I1ii11iIi11i . iiII11i1I1IIi
def I1iI1i11IiI11 ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'elete' in iiI11ii1I1 :
   pass
  else :
   i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 222 , oOo0OOoO0 )
   if 82 - 82: O00OOo00oo0o * oO0o
def i1o0 ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0OO0OO000OO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , O00o0000OO , i1iII1IiiIiI1 in o0OO0OO000OO :
  for o0oOOoOOO in O00o0000OO :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   O0Ooo0O0OO = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for iiOOooooO0Oo , iiI11ii1I1 in O0Ooo0O0OO :
    if 'tube' in iiOOooooO0Oo :
     pass
    elif 'stage' in iiOOooooO0Oo :
     i11i1iiiII ( '[COLOR' + II + ']' + O00o0000OO + '   -   ' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0OOoO0 , )
    elif 'vee' in iiOOooooO0Oo :
     pass
     if 38 - 38: O00OOo00oo0o
def Iiiii1Iii1I ( ) :
 I1 = O000oo ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 o0OO0OO000OO = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , O00o0000OO , i1iII1IiiIiI1 in o0OO0OO000OO :
  O0Ooo0O0OO = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for iiOOooooO0Oo , iiI11ii1I1 in O0Ooo0O0OO :
   if 'tube' in iiOOooooO0Oo :
    pass
   elif 'stage' in iiOOooooO0Oo :
    i11i1iiiII ( '[COLOR' + II + ']' + O00o0000OO + '   -   ' + iiI11ii1I1 + '[/COLOR]' , ( iiOOooooO0Oo ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0OOoO0 )
   elif 'vee' in iiOOooooO0Oo :
    pass
    if 83 - 83: OOooOOo
    if 62 - 62: oo0oO00 + I1ii11iIi11i / Ii
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 90 - 90: iI11I1II1I1I + OOooOOo
def I1i ( url ) :
 I1 = O000oo ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 ooo = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( I1 )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( ooo ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in ooo :
  iii1 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 9 - 9: iI11I1II1I1I . ii + ooOoO0O00 - I1ii11iIi11i
  if 30 - 30: OooOO000 / oO0o . OooOO000
  if 17 - 17: I1ii11iIi11i + ii * ii
  if 5 - 5: O00OOo00oo0o % ii . OOooOOo
  if 67 - 67: Ii1I + iIi1i1ii1
  if 72 - 72: OOoOoo % I11i
  if 93 - 93: iI11I1II1I1I + Ii . I11i . ooOoO0O00 % oOo0O0Ooo % IIiIi1iI
def OOo0 ( ) :
 if 74 - 74: OOooOOo / ooOoO0O00 % ii
 o00o0o000Oo ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 o00o0o000Oo ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 100 - 100: ooOoO0O00 - Ii . O00OOo00oo0o * oO0o
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 62 - 62: o0o00Oo0O
def iiIIIIiii ( ) :
 o00o0o000Oo ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 o00o0o000Oo ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 36 - 36: Ii / o0o00Oo0O . iiII11i1I1IIi
 i1Oo0oO00o ( 'movies' , 'MAIN' )
def iii1IiiiI1i1 ( ) :
 if 37 - 37: I1ii11iIi11i - ooOoO0O00 - OOoOoo + iiII11i1I1IIi . iI11I1II1I1I
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 Oo00oOO00 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 21 - 21: ii . IIiIiII11i - OOoOoo * IIiIi1iI * OOoOoo
 for II11 in Oo00oOO00 :
  I1iii = OOOO0OOoO0O0 + II11 + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( I1iii )
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I1 )
  for iiOOooooO0Oo , O00Ooo , iII1111III1I , O0OoooO0 , iiI11ii1I1 in IIIII11I1IiI :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    IiI1IiI1iiI1 ( iiI11ii1I1 , iiOOooooO0Oo , 222 , O00Ooo , O0OoooO0 , iII1111III1I )
    if 70 - 70: IIi + IIiIi1iI * iIi1i1ii1 . iIi1i1ii1 + oO0o
    i1Oo0oO00o ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 28 - 28: ooOoO0O00 . IIi
    if 88 - 88: iiII11i1I1IIi + oOo0O0Ooo - iiII11i1I1IIi / ii - Ii
def i11Ii1IiIIIi ( ) :
 if 71 - 71: oO0o % oOo0O0Ooo - OooOO000 . OooOO000
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 Oo00oOO00 = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 22 - 22: IIiIi1iI / IIiIi1iI - iIi1i1ii1 % iiII11i1I1IIi . IIi + OOoOoo
 for II11 in Oo00oOO00 :
  OooO00oo0O0 = OOOO0OOoO0O0 + II11 + IIiiiiiiIi1I1
  I1 = OOoOO0oo0ooO ( OooO00oo0O0 )
  IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( I1 )
  for iiI11ii1I1 , iII1111III1I , iiOOooooO0Oo , oOo0OOoO0 , O0OoooO0 , o0ii1i in IIIII11I1IiI :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    o00o0o000Oo ( iiI11ii1I1 , iiOOooooO0Oo , o0ii1i , oOo0OOoO0 , O0OoooO0 , iII1111III1I )
    if 10 - 10: OOoOoo / ii
    i1Oo0oO00o ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 50 - 50: Ii - ii . oo0oO00 + o0o00Oo0O . ooOoO0O00
    if 91 - 91: I11i . OooOO000 % I1ii11iIi11i - OooOO000 . oo0oO00 % Ii
def iIi ( ) :
 if 97 - 97: iiII11i1I1IIi . iiII11i1I1IIi + OOooOOo / oO0o - oOo0O0Ooo . ii
 OoO000O0Oo = O000oo ( OOOO0OOoO0O0 + 'spongemain.php' )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iII1111III1I , iiOOooooO0Oo , oOo0OOoO0 , O0OoooO0 , o0ii1i in IIIII11I1IiI :
  o00o0o000Oo ( iiI11ii1I1 , iiOOooooO0Oo , o0ii1i , oOo0OOoO0 , O0OoooO0 , iII1111III1I )
  i1Oo0oO00o ( 'movies' , 'MAIN' )
def Ii1iiI1i1 ( url ) :
 if 3 - 3: IIi . OOoOoo / I1ii11iIi11i
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OooIIi111 = ( '%s%s' % ( oO0o0o0O , url ) )
 i1Oo00 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , O00Ooo , iII1111III1I , iiii11i , iiI11ii1I1 in IIIII11I1IiI :
  oOO0OO0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
  for oOOOoo00 in oOO0OO0O :
   if oOOOoo00 == url :
    iiI11ii1I1 = ( '[COLORred]Watched - [/COLOR]' + iiI11ii1I1 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  IiI1IiI1iiI1 ( iiI11ii1I1 , url , 222 , O00Ooo , iiii11i , iII1111III1I )
  if 11 - 11: O00OOo00oo0o - iiII11i1I1IIi % Ii . iI11I1II1I1I * oOo0O0Ooo - I1ii11iIi11i
  i1Oo0oO00o ( 'movies' , 'MAIN' )
  if 73 - 73: o0o00Oo0O + IIiIi1iI - o0o00Oo0O / ii * I1ii11iIi11i
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 32 - 32: oO0o % oOo0O0Ooo % OooOO000
  if 66 - 66: OOooOOo + I11i
def OOOO00 ( url ) :
 if 71 - 71: IIiIi1iI . Ii
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iII1111III1I , url , oOo0OOoO0 , O0OoooO0 , o0ii1i in IIIII11I1IiI :
  o00o0o000Oo ( iiI11ii1I1 , url , o0ii1i , oOo0OOoO0 , O0OoooO0 , iII1111III1I )
  if 56 - 56: o0o00Oo0O * OooOO000 + OooOO000 * iI11I1II1I1I / IIiIi1iI * O00OOo00oo0o
  i1Oo0oO00o ( 'movies' , 'MAIN' )
  if 25 - 25: iI11I1II1I1I . iiII11i1I1IIi * Ii + I1ii11iIi11i * iiII11i1I1IIi
  if 67 - 67: OooOO000
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 88 - 88: I1ii11iIi11i
def IiI1IiI1iiI1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 8 - 8: Ii1I
 ii1ii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOoo0oO = True
 iioo0o0OoOOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iioo0o0OoOOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iioo0o0OoOOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooO0oO00O0o = [ ]
  ooO0oO00O0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooO0oO00O0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooO0oO00O0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iioo0o0OoOOO . addContextMenuItems ( ooO0oO00O0o )
 OoOoo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1ii11 , listitem = iioo0o0OoOOO , isFolder = False )
 return OoOoo0oO
 if 82 - 82: ii
def o00o0o000Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 75 - 75: IIiIiII11i % oOo0O0Ooo + IIi % ii / OOoOoo
 ii1ii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOoo0oO = True
 iioo0o0OoOOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iioo0o0OoOOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iioo0o0OoOOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooO0oO00O0o = [ ]
  ooO0oO00O0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooO0oO00O0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooO0oO00O0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iioo0o0OoOOO . addContextMenuItems ( ooO0oO00O0o )
 OoOoo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1ii11 , listitem = iioo0o0OoOOO , isFolder = True )
 return OoOoo0oO
if 4 - 4: Ii - IIi % Ii1I * O00OOo00oo0o % I11i
if 71 - 71: IIiIi1iI . IIiIi1iI - iI11I1II1I1I
if 22 - 22: ii / Ii1I % OooOO000 * OOooOOo
if 32 - 32: ii % oo0oO00 % iI11I1II1I1I / o0o00Oo0O
if 61 - 61: IIiIiII11i . o0o00Oo0O - iIi1i1ii1 - Ii1I / Ii - IIiIiII11i
if 98 - 98: iIi1i1ii1 - oOo0O0Ooo . Ii * I1ii11iIi11i
if 29 - 29: iIi1i1ii1 / IIiIi1iI % iiII11i1I1IIi
if 10 - 10: iI11I1II1I1I % ii % Ii1I
if 39 - 39: IIiIiII11i * OOooOOo . o0o00Oo0O * iiII11i1I1IIi
if 89 - 89: iIi1i1ii1 - IIiIi1iI . iiII11i1I1IIi - O00OOo00oo0o - oOo0O0Ooo
if 79 - 79: OOoOoo + OOoOoo + iIi1i1ii1
if 39 - 39: o0o00Oo0O - ii
if 63 - 63: iI11I1II1I1I % I11i * IIiIi1iI
if 79 - 79: o0o00Oo0O
if 32 - 32: IIiIiII11i . o0o00Oo0O + iIi1i1ii1 / OOooOOo / OOoOoo / IIi
def ii1I11iI ( string ) :
 if OOO00O == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 85 - 85: IIi + IIiIiII11i - IIi * oo0oO00 - ooOoO0O00 % OooOO000
def IiIiI ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 iI1Ii11 = [ ]
 try :
  if 93 - 93: oOo0O0Ooo / IIiIi1iI / iiII11i1I1IIi + IIiIiII11i + Ii
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( OOOOi11i1 ) == False :
  ii1I11iI ( 'Making Favorites File' )
  iI1Ii11 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  OoOoO0O = open ( OOOOi11i1 , "w" )
  OoOoO0O . write ( json . dumps ( iI1Ii11 ) )
  OoOoO0O . close ( )
 else :
  ii1I11iI ( 'Appending Favorites' )
  OoOoO0O = open ( OOOOi11i1 ) . read ( )
  iiiII1III = json . loads ( OoOoO0O )
  iiiII1III . append ( ( name , url , iconimage , fanart , mode ) )
  Ii1I1O0oo00oOOO0o = open ( OOOOi11i1 , "w" )
  Ii1I1O0oo00oOOO0o . write ( json . dumps ( iiiII1III ) )
  Ii1I1O0oo00oOOO0o . close ( )
  if 6 - 6: IIi * oo0oO00 / o0o00Oo0O . IIiIiII11i + OOoOoo % I11i
  if 67 - 67: o0o00Oo0O % O00OOo00oo0o
def III ( ) :
 if os . path . exists ( OOOOi11i1 ) == False :
  iI1Ii11 = [ ]
  ii1I11iI ( 'Making Favorites File' )
  iI1Ii11 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  OoOoO0O = open ( OOOOi11i1 , "w" )
  OoOoO0O . write ( json . dumps ( iI1Ii11 ) )
  OoOoO0O . close ( )
 else :
  I1Io0 = json . loads ( open ( OOOOi11i1 ) . read ( ) )
  oOo0000ooO = len ( I1Io0 )
  for I1Io0oO0oo in I1Io0 :
   iiI11ii1I1 = I1Io0oO0oo [ 0 ]
   iiOOooooO0Oo = I1Io0oO0oo [ 1 ]
   O00Ooo = I1Io0oO0oo [ 2 ]
   try :
    ooOO00Oo = I1Io0oO0oo [ 3 ]
    if ooOO00Oo == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     ooOO00Oo = O00Ooo
    else :
     ooOO00Oo = O0OoooO0
   try : oO00OOOOOO0o = I1Io0oO0oo [ 5 ]
   except : oO00OOOOOO0o = None
   try : iIII = I1Io0oO0oo [ 6 ]
   except : iIII = None
   if 85 - 85: IIiIiII11i + O00OOo00oo0o - IIiIi1iI * iI11I1II1I1I % oo0oO00
   if I1Io0oO0oo [ 4 ] == 0 :
    I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , '' , O00Ooo , O0OoooO0 , '' , 'fav' )
   else :
    I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , I1Io0oO0oo [ 4 ] , O00Ooo , O0OoooO0 , '' , 'fav' )
    if 62 - 62: iIi1i1ii1 + o0o00Oo0O * oO0o
def oOoOO ( name ) :
 iiiII1III = json . loads ( open ( OOOOi11i1 ) . read ( ) )
 for i11I1iIii1i11 in range ( len ( iiiII1III ) ) :
  if iiiII1III [ i11I1iIii1i11 ] [ 0 ] == name :
   del iiiII1III [ i11I1iIii1i11 ]
   Ii1I1O0oo00oOOO0o = open ( OOOOi11i1 , "w" )
   Ii1I1O0oo00oOOO0o . write ( json . dumps ( iiiII1III ) )
   Ii1I1O0oo00oOOO0o . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 42 - 42: oO0o * Ii
 if 16 - 16: OooOO000 % oOo0O0Ooo - IIiIi1iI
def oOo000O ( ) :
 ooO00OoO0o0OO = os . path . join ( I11i1 , 'addons.ini' )
 II11IiI1 = open ( ooO00OoO0o0OO , "w+" )
 I1 = O000oo ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( I1 )
 II11IiI1 . write ( r'[' + IiII + ']' + '\n' )
 for iiI11ii1I1 , oOo0OOoO0 , OoOOOO0O0oO0 , iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = ( iiOOooooO0Oo + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  iIIi11i = ( iiI11ii1I1 + '=plugin://' + IiII + '/?url=' + iiOOooooO0Oo + '&mode=10012&name=' + ( iiI11ii1I1 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOo0OOoO0 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOo0OOoO0 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  II11IiI1 . write ( iIIi11i + '\n' )
  if 39 - 39: OOooOOo . I1ii11iIi11i - OOoOoo / I11i / ooOoO0O00
  if 79 - 79: IIi % O00OOo00oo0o / oo0oO00 - iI11I1II1I1I - OOooOOo
def o0oOO ( ) :
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo in IIIII11I1IiI :
  iII1iii ( '24/7' , iiOOooooO0Oo , 90021 , oOOOo00O00oOo + '247Streams.png' )
  if 84 - 84: Ii + IIiIi1iI . o0o00Oo0O
def o00oo ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + '247Streams.png' , oOOOo00O00oOo + '247Streams.png' , '' )
def Ooii1IIi1ii ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + 'musicch.png' , oOOOo00O00oOo + 'musicch.png' , '' )
def oO00O0 ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + 'NEWS.png' , oOOOo00O00oOo + 'NEWS.png' , '' )
def Ii11IIIi1 ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , ( iiOOooooO0Oo ) . strip ( ) , 222 , oOOOo00O00oOo + 'adult.png' , oOOOo00O00oOo + 'adult.png' , '' )
def ooooooo00oO0OO ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( iiI11ii1I1 , iiOOooooO0Oo , 1016 , oOOOo00O00oOo + 'TUTS.png' , oOOOo00O00oOo + 'TUTS.png' , '' )
  if 30 - 30: I11i + ii + IIi / IIiIiII11i * I1ii11iIi11i
  if 59 - 59: iIi1i1ii1 / OOooOOo * oO0o * OooOO000 % oo0oO00
def oOOoooOO ( ) :
 if 30 - 30: IIiIi1iI - Ii + oOo0O0Ooo / I1ii11iIi11i % o0o00Oo0O
 I1IIII1i ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
 if 66 - 66: iI11I1II1I1I % Ii / oOo0O0Ooo
def IIIIIiiI11i1 ( ) :
 if 43 - 43: oOo0O0Ooo / OooOO000 / IIiIi1iI + iI11I1II1I1I + ii
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , IIIIoOo in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 + '  -  ' + ( IIIIoOo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiOOooooO0Oo , 10023 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 33 - 33: IIiIiII11i - OOoOoo - IIiIi1iI
  if 92 - 92: oO0o * OOoOoo
  if 92 - 92: oo0oO00
def i1i1IIiII1I ( ) :
 if 85 - 85: I1ii11iIi11i . Ii - Ii . oOo0O0Ooo . oO0o % ii
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
 if 20 - 20: O00OOo00oo0o + O00OOo00oo0o * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
def OooOo ( url ) :
 IiIii1I1I = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 I1 = cloudflare . source ( IiIii1I1I )
 IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10022 , oOOOo00O00oOo + 'dtv.png' , O0o0Oo , '' )
  if 87 - 87: IIiIi1iI * oO0o + I11i . IIi - IIiIi1iI
  if 33 - 33: IIiIiII11i / o0o00Oo0O / OOoOoo - iiII11i1I1IIi - ooOoO0O00
  if 8 - 8: Ii . OooOO000 / iI11I1II1I1I / Ii1I / OOoOoo - iIi1i1ii1
  if 32 - 32: I11i . ooOoO0O00 * I1ii11iIi11i
def O0oooo0O ( ) :
 if 15 - 15: ooOoO0O00 % ii * IIi . IIiIiII11i + o0o00Oo0O * oO0o
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 I1 = cloudflare . source ( iiOOooooO0Oo )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 10022 , oOOOo00O00oOo + 'dtv.png' )
   if 16 - 16: o0o00Oo0O - o0o00Oo0O / iiII11i1I1IIi - oO0o
   if 30 - 30: I11i - oO0o + IIi
   if 65 - 65: o0o00Oo0O / IIiIiII11i . iI11I1II1I1I . oo0oO00 / I1ii11iIi11i % iI11I1II1I1I
def Oo0Oo ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for ooo0O , iIIii , OO0 , iiI11ii1I1 in IIIII11I1IiI :
  iiiii1iiIIii = ( OO0 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  II1IIii1I11I = ( iIIii ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  ii1IiIIiI11111Ii = 'Season ' + II1IIii1I11I + 'Episode ' + iiiii1iiIIii + iiI11ii1I1
  O0OOo ( ii1IiIIiI11111Ii , ooo0O )
  if 75 - 75: iiII11i1I1IIi + IIiIi1iI / IIiIi1iI - IIi * oO0o * IIiIi1iI
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 53 - 53: OOoOoo % I1ii11iIi11i
  if 42 - 42: Ii / oOo0O0Ooo - oO0o - IIiIi1iI + IIiIiII11i % IIiIi1iI
def O0OOo ( name , url ) :
 ooo0O = url
 Ii1IIii = name
 iii1i1iiiiIi = cloudflare . source ( ooo0O )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iii1i1iiiiIi )
 for ooo , oooOOoo in i1I :
  i11i1iiiII ( '[COLOR' + II + ']' + Ii1IIii + oooOOoo + '[/COLOR]' , ooo , 10012 , oOOOo00O00oOo + 'dtv.png' )
  if 36 - 36: IIi * iIi1i1ii1
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 16 - 16: IIiIiII11i
 if 100 - 100: o0o00Oo0O - ooOoO0O00
def OOooO0oo0o00o ( ) :
 if 48 - 48: oo0oO00 % IIiIi1iI + o0o00Oo0O
 if 27 - 27: Ii1I / IIi
 if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
 if 63 - 63: OOoOoo + iI11I1II1I1I + oOo0O0Ooo + O00OOo00oo0o
 if 72 - 72: oO0o + Ii + Ii1I
 if 96 - 96: oo0oO00 % ooOoO0O00 / I11i
 if 13 - 13: IIiIiII11i - I1ii11iIi11i % Ii + OooOO000
 I1IIII1i ( '[COLOR' + II + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']SEARCH[/COLOR]' , '' , 10091 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 88 - 88: o0o00Oo0O . oo0oO00 % oOo0O0Ooo
def iii111i ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( I1 )
 iIi11ii1iI = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + oOo0OOoO0 , '' , '' )
 for url in iIi11ii1iI :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 69 - 69: Ii
def ooO ( url ) :
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( I1 )
 iIi11ii1iI = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  oOo0OOoO0 = 'http://watchepisodes.cc/' + oOo0OOoO0
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10093 , oOo0OOoO0 , oOo0OOoO0 , '' )
 for url in iIi11ii1iI :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 84 - 84: iI11I1II1I1I . IIiIi1iI + OooOO000
def O00OOOo0Oo0 ( url , iconimage ) :
 oOo0OOoO0 = iconimage
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( I1 )
 for OO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + OO0 + ' - ' + iiI11ii1I1 + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , oOo0OOoO0 , '' , '' )
  if 55 - 55: IIi / OOooOOo * IIi
def IIIiiiI1Ii1 ( url , iconimage ) :
 oOo0OOoO0 = iconimage
 I1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if 'player' in iiI11ii1I1 :
   pass
  elif 'vod' in iiI11ii1I1 :
   I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , oOo0OOoO0 , '' , '' )
   if 97 - 97: IIiIiII11i % I1ii11iIi11i * OOoOoo
   if 51 - 51: I1ii11iIi11i % IIi . I1ii11iIi11i
   if 72 - 72: iIi1i1ii1 % iIi1i1ii1 / oOo0O0Ooo
   if 40 - 40: I1ii11iIi11i - IIi + O00OOo00oo0o - I11i % oOo0O0Ooo . IIiIi1iI
   if 35 - 35: Ii + ii * iI11I1II1I1I . O00OOo00oo0o
   if 48 - 48: OooOO000 * ooOoO0O00 % ii * iIi1i1ii1 * oO0o
def ooOO0OoO ( ) :
 if 7 - 7: OooOO000 . iIi1i1ii1 . OooOO000 - O00OOo00oo0o
 if 33 - 33: IIiIi1iI + ii - oO0o / ooOoO0O00 / ii
 if 82 - 82: Ii1I / IIi - OooOO000 / I1ii11iIi11i * oO0o
 if 55 - 55: ii
 if 73 - 73: OOooOOo - Ii1I % I1ii11iIi11i + Ii1I - o0o00Oo0O . oO0o
 if 38 - 38: o0o00Oo0O
 if 79 - 79: ooOoO0O00 . oo0oO00
 if 34 - 34: O00OOo00oo0o * IIiIiII11i
 if 71 - 71: OOoOoo
 if 97 - 97: Ii1I
 if 86 - 86: I1ii11iIi11i - IIi . OOooOOo . IIiIiII11i * oOo0O0Ooo . IIiIiII11i
 if 34 - 34: I11i . O00OOo00oo0o % OOoOoo - o0o00Oo0O / O00OOo00oo0o
 if 91 - 91: Ii % O00OOo00oo0o * oo0oO00 - Ii1I . O00OOo00oo0o
 I1IIII1i ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 I1IIII1i ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 if 28 - 28: Ii
 if 51 - 51: oOo0O0Ooo + IIiIi1iI * o0o00Oo0O . iIi1i1ii1
def O00Oo00OOoO0 ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 99 - 99: oO0o / ooOoO0O00 . Ii1I
def I1I1i11iiiiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
  if 66 - 66: oo0oO00 / OOooOOo
def iII1I ( url ) :
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
  if 92 - 92: O00OOo00oo0o % iIi1i1ii1
  if 30 - 30: IIiIiII11i - I11i % O00OOo00oo0o . iiII11i1I1IIi
def oo0o ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0o00O = 'http://www.watchseriesgo.to/search/' + o0oOOoOOO . replace ( ' ' , '%20' )
 I1 = O000oo ( o0o00O )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'watch online' in iiI11ii1I1 :
   pass
  else :
   print iiOOooooO0Oo
   I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + iiOOooooO0Oo , 10044 , oOo0OOoO0 , '' , '' )
   if 46 - 46: OOooOOo
   xbmcplugin . setContent ( I1IIiiIiii , 'movies' )
   if 4 - 4: OooOO000 + o0o00Oo0O
def I1IiiiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , OO0 , iII1111III1I in IIIII11I1IiI :
  Iii11iI11i1I = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( OO0 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + II + ']' + Iii11iI11i1I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOo0OOoO0 , '' , iII1111III1I )
  if 6 - 6: oOo0O0Ooo - Ii
def O00O0O0OO00oo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  Iii11iI11i1I = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  I1IIII1i ( '[COLOR' + II + ']' + Iii11iI11i1I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 39 - 39: OOoOoo % OOooOOo * Ii1I - ii - I1ii11iIi11i
def Oo0oOOO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOo0OOoO0 , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 62 - 62: iIi1i1ii1 - oo0oO00 % iI11I1II1I1I
def ooOOO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( I1 )
 I11o0oO00oO0o0o0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( I1 )
 for iIIii , o0OO0OO000OO in I11o0oO00oO0o0o0 :
  IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( o0OO0OO000OO ) )
  for url , iiI11ii1I1 in IIIII11I1IiI :
   Iii11iI11i1I = ( iIIii ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   I1IIII1i ( '[COLOR' + II + ']' + Iii11iI11i1I + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , oOOOo00O00oOo + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  I1IIII1i ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 97 - 97: ooOoO0O00 * O00OOo00oo0o . IIiIiII11i
class ooooOoOooo00Oo ( ) :
 if 72 - 72: iiII11i1I1IIi
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 26 - 26: OOoOoo % I1ii11iIi11i
  Iii11iI11i1I = name
  self . Get_Sources ( iiOOooooO0Oo , Iii11iI11i1I )
  if 72 - 72: o0o00Oo0O + I11i + oOo0O0Ooo / I1ii11iIi11i
  if 83 - 83: OOoOoo - oOo0O0Ooo . iIi1i1ii1
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  I1 = O000oo ( URL )
  IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + iiOOooooO0Oo
   self . Get_site_link ( URL , season_name )
   if 34 - 34: OOooOOo - oo0oO00 * ii
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
   if 5 - 5: Ii * OooOO000 - iIi1i1ii1 - Ii1I - ooOoO0O00 + OooOO000
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   I1ii1i = 'DACLIPS'
   if I1ii1i in ooooOoOooo00Oo . source_list :
    pass
   else :
    self . daclips ( url , season_name , I1ii1i )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'filehoot.com' in url :
    I1ii1i = 'FILEHOOT'
    if I1ii1i in ooooOoOooo00Oo . source_list :
     pass
    else :
     o0oOoO00o . update ( 0 , "" , "Getting Filehoot Links" )
     self . filehoot ( url , season_name , I1ii1i )
   else :
    if 'thevideo.me' in url :
     I1ii1i = 'THEVIDEO'
     if I1ii1i in ooooOoOooo00Oo . source_list :
      pass
     else :
      self . thevideo ( url , season_name , I1ii1i )
      o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
    else :
     if 'allmyvideos.net' in url :
      I1ii1i = 'ALLMYVIDEOS'
      if I1ii1i in ooooOoOooo00Oo . source_list :
       pass
      else :
       self . allmyvid ( url , season_name , I1ii1i )
       o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
     else :
      if 'vidspot.net' in url :
       I1ii1i = 'VIDSPOT'
       if I1ii1i in ooooOoOooo00Oo . source_list :
        pass
       else :
        self . vidspot ( url , season_name , I1ii1i )
        o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
      else :
       if 'vodlocker' in url :
        I1ii1i = 'VODLOCKER'
        if I1ii1i in ooooOoOooo00Oo . source_list :
         pass
        else :
         self . vodlocker ( url , season_name , I1ii1i )
         o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
         if 51 - 51: oO0o - OooOO000 % o0o00Oo0O - OOooOOo
         if 53 - 53: OooOO000 / ooOoO0O00 / ooOoO0O00
 def allmyvid ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( I1 )
  for oO0o0O0Ooo0o , iiI11ii1I1 in IIIII11I1IiI :
   self . Printer ( oO0o0O0Ooo0o , season_name , source_name )
   if 77 - 77: iiII11i1I1IIi + ooOoO0O00 . iiII11i1I1IIi
 def vidspot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( I1 )
  for oO0o0O0Ooo0o , iiI11ii1I1 in IIIII11I1IiI :
   self . Printer ( oO0o0O0Ooo0o , season_name , source_name )
   if 89 - 89: I11i + IIi * oo0oO00
 def thevideo ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( I1 )
  for oO0o0O0Ooo0o in IIIII11I1IiI :
   self . Printer ( oO0o0O0Ooo0o , season_name , source_name )
   if 45 - 45: OooOO000 - I11i . iIi1i1ii1
 def vodlocker ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for oO0o0O0Ooo0o in IIIII11I1IiI :
   self . Printer ( oO0o0O0Ooo0o , season_name , source_name )
   if 41 - 41: IIiIiII11i . oOo0O0Ooo / oO0o . IIiIi1iI
 def daclips ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( I1 )
  for oO0o0O0Ooo0o in IIIII11I1IiI :
   self . Printer ( oO0o0O0Ooo0o , season_name , source_name )
   if 58 - 58: OOoOoo % Ii * IIiIiII11i . Ii1I
 def filehoot ( self , url , season_name , source_name ) :
  I1 = O000oo ( url )
  IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( I1 )
  for oO0o0O0Ooo0o in IIIII11I1IiI :
   self . Printer ( oO0o0O0Ooo0o , season_name , source_name )
   if 94 - 94: Ii . IIi + iI11I1II1I1I * O00OOo00oo0o * O00OOo00oo0o
 def Printer ( self , Link , season_name , source_name ) :
  if 36 - 36: iiII11i1I1IIi - OOoOoo . OOoOoo
  if Link in ooooOoOooo00Oo . List :
   pass
  elif source_name in ooooOoOooo00Oo . source_list :
   pass
  else :
   i11i1iiiII ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 10012 , oOOOo00O00oOo + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   ooooOoOooo00Oo . List . append ( Link )
   ooooOoOooo00Oo . source_list . append ( source_name )
   if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
   xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 84 - 84: iI11I1II1I1I + ii
   if 77 - 77: o0o00Oo0O * Ii1I * oo0oO00 + oO0o + Ii1I - O00OOo00oo0o
   if 10 - 10: Ii1I + OOoOoo
   if 58 - 58: oOo0O0Ooo + ii / OooOO000 . IIiIi1iI % I11i / Ii1I
   if 62 - 62: IIiIiII11i
def O0O0Oo00 ( ) :
 I1IIII1i ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , oOOOo00O00oOo + 'Highlights.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , oOOOo00O00oOo + 'Fixtures.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'Sport.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , oOOOo00O00oOo + 'PremiereLeague.png' , O0o0Oo , '' )
 if 12 - 12: OOoOoo + IIiIiII11i
def O0Ooo00o00O ( url ) :
 I1IIII1i ( '[COLORwhite]                                                    pl        w        d        l        f        a        pts[/COLOR]' , '' , '' , '' , '' , '' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<td class="ixt div"><strong><a href="([^"]*)">([^>]*)</a></strong></td>.+?<td class="div">([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td>([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="mobile-hdn">([^>]*)</td>.+?<td class="div">([^>]*)</td>.+?<td class="div">([^>]*)</td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for ooo0O0O0oo0 , url , oo000oO , IiIiII11i1 , Ii1I1iIiiI1 , I11i11I , o00i111iiIiiIiI , OOoO , OoOoO0O , OOooooO , oOoo00 in IIIII11I1IiI :
  oo000oO = oo000oO
  if 'Arsenal' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'arsenal-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                                  ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Bournemouth' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'afc-bournemouth.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                       ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Burnley' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'KEGnQWW.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                                   ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Chelsea' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'chelsea.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                                  ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Crystal' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'CrystalPalace.0.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                       ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Everton' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'Everton.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                                   ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Hull' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'hull-city-afc.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                                 ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Leicester' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'leicester-city-fc-hd-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                       ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Liverpool' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'liverpool-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                               ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Manchester City' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'city-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '               ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Manchester United' in oo000oO :
   oOOoo = oOOOo00O00oOo + '91.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '          ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Middlesbrough' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'middlesbrough-fc-hd-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                 ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Southampton' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'southampton-fc-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                   ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Stoke City' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'stoke-city.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                          ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Sunderland' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'sunderland-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                        ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Swansea' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'swansea-city-afc.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                    ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Tottenham' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'tottenham-hotspur_zps4e3ed7c1.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '        ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Watford' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'watford-fc-hd-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '                              ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'Bromwich' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'west-bromwich-albion-logo.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '   ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  elif 'West Ham' in oo000oO :
   oOOoo = oOOOo00O00oOo + 'west-ham.png'
   iiI11ii1I1 = '[COLOR' + II + ']' + ooo0O0O0oo0 + ' - ' + oo000oO + '             ' + IiIiII11i1 + '        ' + Ii1I1iIiiI1 + '        ' + I11i11I + '        ' + o00i111iiIiiIiI + '        ' + OOoO + '        ' + OoOoO0O + '        ' + OOooooO + '[/COLOR]'
  I1IIII1i ( str ( iiI11ii1I1 ) , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 50003 , oOOoo , oOOoo , oo000oO )
  if 29 - 29: IIi / OOooOOo . iI11I1II1I1I / iiII11i1I1IIi % OOooOOo % OooOO000
def iiI1 ( description ) :
 oo000oO = description
 iiOOooooO0Oo = ( 'http://www.fullmatchesandshows.com/?s=' + oo000oO ) . replace ( ' ' , '%20' )
 oooOOO0o0O0 ( iiOOooooO0Oo )
 if 31 - 31: ii - oo0oO00 / O00OOo00oo0o
def oo00o000O ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + iiOOooooO0Oo , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOo0OOoO0 , O0o0Oo , '' )
  if 66 - 66: ii + I11i . ooOoO0O00 * OooOO000
def o00oIII ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( I1 )
 for I11o0oO00oO0o0o0 in I11o0oO00oO0o0o0 :
  i1iiIi1iii11I = re . compile ( '(.*?)</h2>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for Ii11iIiiI in i1iiIi1iii11I :
   Ii11iIiiI = Ii11iIiiI
  iiII = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( I11o0oO00oO0o0o0 ) )
  for iII1IiiIIIIii , oOo0OOoO0 , time , oOOOIii1IiiII1Ii1 in iiII :
   IiIii1ii = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( oOOOIii1IiiII1Ii1 )
   I1IIII1i ( '[COLOR' + II + ']' + Ii11iIiiI + ' - ' + iII1IiiIIIIii + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOo0OOoO0 , O0o0Oo , ( str ( IiIii1ii ) ) )
   if 26 - 26: ii + oOo0O0Ooo
 i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if 57 - 57: IIi . iIi1i1ii1 % I11i
def I1I11 ( ) :
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
 if 9 - 9: IIi
def I1iIII1IIiIi ( url ) :
 I1IIII1i ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  OOOOoOoO = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   OOOOoOoO = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   i11i1iiiII ( '[COLOR' + II + ']' + OOOOoOoO + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  OOOOoOoO = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   i11i1iiiII ( '[COLOR' + II + ']' + OOOOoOoO + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
def oooOOO0o0O0 ( url ) :
 I1IIII1i ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , oOOOo00O00oOo + 'TodaysMacthes.png' , O0o0Oo , '' )
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( I1 )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( I1 )
 if 72 - 72: OOooOOo / O00OOo00oo0o * OOoOoo % iI11I1II1I1I
 if 53 - 53: oO0o . o0o00Oo0O . oOo0O0Ooo * IIi / I11i
 if 34 - 34: OOooOOo
 if 16 - 16: ooOoO0O00 - O00OOo00oo0o - IIiIiII11i
 if 83 - 83: oOo0O0Ooo - oO0o - I11i / o0o00Oo0O - iiII11i1I1IIi . IIiIiII11i
 if 27 - 27: iIi1i1ii1
 if 59 - 59: iIi1i1ii1 / IIiIiII11i - OOoOoo % OOooOOo % ii
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  OOOOoOoO = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   i11i1iiiII ( '[COLOR' + II + ']' + OOOOoOoO + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
   if 79 - 79: OooOO000 . ii . oOo0O0Ooo * o0o00Oo0O * oO0o - IIi
def IIIiII11 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( I1 )
 for ooo in IIIII11I1IiI :
  O00OO00OOOoO = ( ooo ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  iii1 ( 'http:' + O00OO00OOOoO )
  if 47 - 47: ooOoO0O00 % IIiIi1iI - I1ii11iIi11i * iiII11i1I1IIi / Ii
  if 45 - 45: oOo0O0Ooo . I1ii11iIi11i . O00OOo00oo0o / oo0oO00
  if 4 - 4: Ii + IIi
  if 26 - 26: OooOO000 * O00OOo00oo0o * oo0oO00 * OOooOOo
def I1ii1i11iI1 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , url , 8046 , oOo0OOoO0 )
 for url in i1I :
  iII1iii ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , oOOOo00O00oOo + 'Next.png' )
def IiOOo0 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iii1 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 85 - 85: O00OOo00oo0o % Ii1I
def OO00o0O0oOooO ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 18 - 18: Ii * I1ii11iIi11i / Ii1I + Ii1I % OOooOOo
def iII1ii1 ( ) :
 iII1iii ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , oOOOo00O00oOo + 'documentary.png' )
 iII1iii ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , oOOOo00O00oOo + 'documentary.png' )
 iII1iii ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , oOOOo00O00oOo + 'Search.png' )
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , iiOOooooO0Oo , 8041 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiI111iIi1 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + oOo0OOoO0 )
 for url in next :
  iII1iii ( 'NEXT PAGE' , url , 8041 , oOOOo00O00oOo + 'Next.png' )
  if 25 - 25: O00OOo00oo0o - iIi1i1ii1 / o0o00Oo0O . ii % oOo0O0Ooo . ooOoO0O00
  if 19 - 19: IIiIiII11i / IIiIiII11i % Ii1I + oo0oO00 + oo0oO00 + OooOO000
def IIi1I1 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   i11i1iiiII ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
  else :
   iII1iii ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def oO00o0oOoo ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10012 , '' )
  if 66 - 66: Ii1I . I1ii11iIi11i
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1OO ( name , url ) :
 I1ii1 = 0
 name = name
 url = url
 OooOoOO0 = [ '144' , '240' , '380' , '480' , '720' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  iii1 ( url )
  if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + IIi
  if 31 - 31: iIi1i1ii1 * I11i * iIi1i1ii1 + oO0o * I11i . O00OOo00oo0o
  if 89 - 89: ii * iIi1i1ii1 * oOo0O0Ooo . IIiIi1iI * iIi1i1ii1 / OooOO000
  if 46 - 46: Ii
  if 15 - 15: o0o00Oo0O / ooOoO0O00 / ooOoO0O00 . OooOO000 % OOooOOo + oOo0O0Ooo
  if 48 - 48: O00OOo00oo0o % OooOO000 % iIi1i1ii1 % iI11I1II1I1I . iIi1i1ii1
  if 14 - 14: OooOO000 * oO0o % o0o00Oo0O + iiII11i1I1IIi + Ii1I
  if 23 - 23: I1ii11iIi11i % OooOO000 + iIi1i1ii1 - O00OOo00oo0o
def ooOOoO0o0 ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( 'http://documentarylovers.com/' )
 IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  if 'genre' in iiOOooooO0Oo :
   iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , iiOOooooO0Oo , 80010 , oOOOo00O00oOo + 'documentary.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1Ii1i11ii ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , oOo0OOoO0 )
 for url in next :
  iII1iii ( 'NEXT PAGE' , url , 80010 , oOOOo00O00oOo + 'Next.png' )
  if 58 - 58: OOooOOo + oO0o * iIi1i1ii1
def iI1IIIIII ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , oOOOo00O00oOo + 'documentary.png' )
 for url in i1I :
  oO00o0oOoo ( url )
  if 79 - 79: I1ii11iIi11i - ii % O00OOo00oo0o + ii - iiII11i1I1IIi % OOooOOo
def iII ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0Oo0 = 'http://documentarylovers.com/?s=' + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 iiI1i11II = o0Oo0 . lower ( )
 i1Ii1i11ii ( iiI1i11II )
 if 89 - 89: oOo0O0Ooo / OooOO000 / ii - Ii + oOo0O0Ooo
def Oo0ooo ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'films' in url :
   iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , oOOOo00O00oOo + 'documentary.png' )
def Oo00o00 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  if 'films' in url :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + oOo0OOoO0 )
 for url in i1I :
  iII1iii ( 'NEXT' , url , 8049 , oOOOo00O00oOo + 'Next.png' )
def OoOo0O0 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'rtd' in url :
   I1o0 ( url )
   if 26 - 26: OooOO000 * iI11I1II1I1I + IIiIiII11i / oOo0O0Ooo
def I1o0 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OoO000O0Oo )
 for i1Oo00 , file in IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1Oo00 + file )
  iii1 ( url )
  if 52 - 52: iIi1i1ii1 / OOooOOo + oO0o % iIi1i1ii1 % IIi / oo0oO00
  if 91 - 91: oO0o / oO0o . IIiIiII11i . IIiIi1iI - oOo0O0Ooo
def iii11 ( ) :
 I1 = i1i11I1I1iii1 ( 'http://www.stream2watch.co/live-tv' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , OO0oO in IIIII11I1IiI :
  iII1iii ( ( iiI11ii1I1 + '[COLOR' + II + ']' + OO0oO + '[/COLOR]' ) , iiOOooooO0Oo , 8086 , oOo0OOoO0 )
  if 35 - 35: iiII11i1I1IIi + IIi / IIi
def i1IIIi1Iii1i ( url ) :
 I1 = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8087 , oOo0OOoO0 )
  if 63 - 63: oO0o + IIiIi1iI
def IIi1iI1i ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  Iii11II1 ( url , iiI11ii1I1 )
  if 42 - 42: I1ii11iIi11i / OOoOoo . iIi1i1ii1 * oOo0O0Ooo
def Iii11II1 ( url , name ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  print url
  i11i1iiiII ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 54 - 54: OOooOOo * OooOO000 + oO0o
def oOOOo ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + iiOOooooO0Oo , 3002 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def o0OOOoO0O ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def OoOOo ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 III11iI1i11i = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , oOOOo00O00oOo + 'classicmovies.png' )
 for url , iiI11ii1I1 in III11iI1i11i :
  iII1iii ( '[COLOR' + II + ']Season- ' + iiI11ii1I1 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'classicmovies.png' )
 for url in next :
  iII1iii ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , oOOOo00O00oOo + 'Next.png' )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def IIiI ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  OOoOo0oO0oo00 ( url )
def OOoOo0oO0oo00 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( url )
  if 100 - 100: oO0o . iiII11i1I1IIi / iIi1i1ii1 . I11i - OOooOOo . iiII11i1I1IIi
def Oo00o0OO0O00o ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiOOooooO0Oo , 8065 , oOOOo00O00oOo + 'classicmovies.png' )
def i1I1IIIiii1 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  II1IIIii ( url )
  if 76 - 76: ii
def oooooOOO000Oo ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , iiOOooooO0Oo , 8065 , oOOOo00O00oOo + 'classictv.png' )
def i1iiIi1IiiiI ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'mp4' in url :
   iii1 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 79 - 79: Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
def oOOo00ooO ( ) :
 I1 = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + iiOOooooO0Oo , 8071 , oOOOo00O00oOo + 'streams.png' )
def ooOoOOOoOo0oO0OoO ( url ) :
 I1 = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '(Free Access)' in iiI11ii1I1 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , oOOOo00O00oOo + 'streams.png' )
def I1ii11 ( url ) :
 I1 = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOo0OOoO0 , O0OoooO0 , '' )
  if 65 - 65: O00OOo00oo0o + OooOO000 * OooOO000
def OoOOiIO0oOoo00Oo0O ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  Iii1i1Ii ( 'http://watchxxxfree.com/categories' )
 if iI1i11iII111 == 1 :
  III1iIii ( 'http://www.perfectgirls.net' )
 if iI1i11iII111 == 2 :
  iiIII1i1 ( 'http://www.xvideos.com/best' )
 if iI1i11iII111 == 3 :
  oOOo0OOoOO0 ( 'http://www.xvideos.com/best' )
 if iI1i11iII111 == 4 :
  iiIII1i1 ( 'http://www.xvideos.com/best' )
 if iI1i11iII111 == 5 :
  iiIII1i1 ( 'http://www.xvideos.com/verified/videos' )
 if iI1i11iII111 == 6 :
  IiIi ( 'http://www.xvideos.com/tags' )
 if iI1i11iII111 == 7 :
  IIi1IiiIi1III ( 'http://www.xvideos.com/porn' )
 if iI1i11iII111 == 8 :
  IiIiIiiIIii ( )
  if 77 - 77: oo0oO00 * IIiIi1iI . IIi * iIi1i1ii1 % IIiIiII11i
  if 94 - 94: oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
  if 75 - 75: I1ii11iIi11i + iIi1i1ii1 + oO0o
  if 97 - 97: IIiIi1iI % Ii % iiII11i1I1IIi
  if 21 - 21: I1ii11iIi11i / iIi1i1ii1 / Ii1I / ooOoO0O00 / I11i
  if 86 - 86: ooOoO0O00
  if 33 - 33: OOooOOo % Ii * IIi
  if 69 - 69: IIiIiII11i + I1ii11iIi11i - oo0oO00 . I1ii11iIi11i / iI11I1II1I1I * iI11I1II1I1I
  if 75 - 75: oO0o % ii
def iiiI ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if 'ch' in url :
   o0OO0oooo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Jizbox.png' , oOOOo00O00oOo + 'Jizbox.png' , '' )
def ooo0o00o ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( I1 )
 O0oOOo0 = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( I1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 for iiI11ii1I1 , url in O0oOOo0 :
  I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def oooOOOoO0O ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   iIOOO0O00 ( url )
def Oo0O000OoO00 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( url )
def Iii1i1Ii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , IiIiIi1I1 in IIIII11I1IiI :
  if 'category' in url :
   o0OO0oooo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]   ' + IiIiIi1I1 + '[/COLOR]' , url , 90006 , oOo0OOoO0 , oOOOo00O00oOo + 'Jizbox.png' , '' )
def oOO00OoOo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 O0oOOo0 = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , oOo0OOoO0 , '' , '' )
 for url in O0oOOo0 :
  I1IIII1i ( '[COLORred]NEXT[/COLOR]' , url , 90006 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def oOoooO0OO00 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'jetload' in url :
   iIOOO0O00 ( url )
def iIOOO0O00 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( url )
def III1iIii ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , IiIiIi1I1 in IIIII11I1IiI :
  if 'category' in url :
   o0OO0oooo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]' + IiIiIi1I1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def IiiI ( url ) :
 I1 = O000oo ( url )
 ooo0O = url
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 O0oOOo0 = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , oOo0OOoO0 , '' , '' )
 for url in O0oOOo0 :
  I1IIII1i ( '[COLORred]NEXT[/COLOR]' , ooo0O + '/' + url , 90003 , oOOOo00O00oOo + 'Next.png' , '' , '' )
def O0oooooO ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  IIi1 ( 'http://www.perfectgirls.net' + url )
def IIi1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( I1 )
 for url in IIIII11I1IiI :
  iii1 ( 'http://' + url )
def IIi1IiiIi1III ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( I1 )
 for url , iiI11ii1I1 , IiIiIi1I1 in IIIII11I1IiI :
  o0OO0oooo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - No of Videos : [COLORorange]' + IiIiIi1I1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
def IiIi ( url ) :
 I1 = O000oo ( url )
 O0oOOo0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in O0oOOo0 :
  o0OO0oooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( I1 )
 for url , iiI11ii1I1 , IiIiIi1I1 in IIIII11I1IiI :
  o0OO0oooo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - No of Videos : [COLORorange]' + ( IiIiIi1I1 + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
  if 44 - 44: oO0o + iiII11i1I1IIi % oO0o + ooOoO0O00 + OooOO000 + o0o00Oo0O
def Ii1iII1ii1 ( url ) :
 I1 = O000oo ( url )
 O0oOOo0 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in O0oOOo0 :
  o0OO0oooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , iii in IIIII11I1IiI :
  o0OO0oooo ( iiI11ii1I1 + '--' + ( iii ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOo0OOoO0 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 80 - 80: iI11I1II1I1I / Ii + OooOO000
  if 41 - 41: O00OOo00oo0o + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
def iiIII1i1 ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , url , iiI11ii1I1 , iIiii , ooooOoo00 in IIIII11I1IiI :
  o0OO0oooo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - Porn Quality : [COLORorange]' + ooooOoo00 + ' - [COLORred]' + iIiii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oOo0OOoO0 , oOo0OOoO0 , ooooOoo00 + ' - ' + iIiii )
 IIIIii1111i1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for url in IIIIii1111i1 :
  o0OO0oooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
  if 11 - 11: OOooOOo
def oOOo0OOoOO0 ( url ) :
 I1 = O000oo ( url )
 I11o0oO00oO0o0o0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 O0oOOo0 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( I1 )
 for url in O0oOOo0 :
  o0OO0oooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , oOOOo00O00oOo + 'Next.png' , '' , '' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( I11o0oO00oO0o0o0 ) )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '/c/' in url :
   o0OO0oooo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , oOOOo00O00oOo + 'Jizbox.png' , '' , '' )
   if 31 - 31: IIiIiII11i * iIi1i1ii1 / OOoOoo / Ii
   if 88 - 88: I1ii11iIi11i . I11i - Ii . o0o00Oo0O * iI11I1II1I1I * OOooOOo
def IiIiIiiIIii ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OoOOoO0o = ( o0oOOoOOO ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 iiI1i11II = OoOOoO0o . lower ( )
 IiIi1II111I = 'http://www.xvideos.com/?k=' + iiI1i11II
 print IiIi1II111I + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 I1 = O000oo ( IiIi1II111I )
 IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 , iIiii , ooooOoo00 in IIIII11I1IiI :
  o0OO0oooo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - Porn Quality : [COLORorange]' + ooooOoo00 + ' - [COLORred]' + iIiii + '[/COLOR]' , 'http://www.xvideos.com' + iiOOooooO0Oo , 10108 , oOo0OOoO0 , oOo0OOoO0 , ooooOoo00 + ' - ' + iIiii )
 IIIIii1111i1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( I1 )
 for iiOOooooO0Oo in IIIIii1111i1 :
  o0OO0oooo ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + iiOOooooO0Oo , 10105 , oOOOo00O00oOo + 'Next.png' , '' , '' )
if 66 - 66: iiII11i1I1IIi - iiII11i1I1IIi + OOoOoo
if 20 - 20: O00OOo00oo0o . ooOoO0O00
if 9 - 9: oO0o
if 89 - 89: ooOoO0O00
if 19 - 19: IIiIi1iI / I11i % OOoOoo - iIi1i1ii1
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
if 68 - 68: iI11I1II1I1I . iI11I1II1I1I / OOooOOo - IIiIiII11i - iI11I1II1I1I
if 75 - 75: IIiIi1iI . oOo0O0Ooo * IIiIiII11i
if 99 - 99: iI11I1II1I1I * Ii1I + OOoOoo
if 70 - 70: ooOoO0O00 % IIiIi1iI . Ii1I - OOoOoo + IIi
if 84 - 84: oo0oO00 + IIiIiII11i * IIiIiII11i % I11i / OooOO000 + IIiIi1iI
if 9 - 9: OooOO000
if 25 - 25: IIi - iIi1i1ii1 . iiII11i1I1IIi
if 57 - 57: I11i + I1ii11iIi11i * Ii1I - IIiIi1iI % iI11I1II1I1I - iIi1i1ii1
if 37 - 37: oO0o * iiII11i1I1IIi + iIi1i1ii1 + Ii1I * I11i
if 95 - 95: iIi1i1ii1 - Ii % Ii - o0o00Oo0O * O00OOo00oo0o
if 81 - 81: IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * Ii + OOooOOo
def oo0OoOO000O ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( I1 )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( I1 )
 I1II1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( I1 )
 for url in IIIII11I1IiI :
  if 'http' in url :
   i11i1iiiII ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   i11i1iiiII ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
 for url in I1II1 :
  if 'http' in url :
   i11i1iiiII ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , oOOOo00O00oOo + 'Jizbox.png' )
   if 62 - 62: ooOoO0O00 * iI11I1II1I1I % oo0oO00 % OOooOOo / ii
def iI1111iiI1 ( url ) :
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 if 71 - 71: I11i % IIi + o0o00Oo0O / Ii1I
 if 88 - 88: iiII11i1I1IIi / I1ii11iIi11i - O00OOo00oo0o
def I1iIi1IiI1i ( ) :
 if 50 - 50: ooOoO0O00 * oo0oO00 / Ii / Ii / oo0oO00
 if 84 - 84: Ii1I - OooOO000 + Ii1I
 if 63 - 63: iiII11i1I1IIi * IIiIi1iI % IIiIiII11i % O00OOo00oo0o + oOo0O0Ooo * I1ii11iIi11i
 if 96 - 96: OOoOoo
 if 99 - 99: iI11I1II1I1I - IIiIi1iI
 if 79 - 79: oOo0O0Ooo + oo0oO00 % iiII11i1I1IIi % oo0oO00
 if 56 - 56: Ii1I + oo0oO00 . oO0o + ii * Ii1I - o0o00Oo0O
 if 35 - 35: IIi . iiII11i1I1IIi . O00OOo00oo0o - iiII11i1I1IIi % iiII11i1I1IIi + O00OOo00oo0o
 if 99 - 99: I11i + IIi
 if 34 - 34: O00OOo00oo0o * I11i . oOo0O0Ooo % Ii
 I1 = O000oo ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 8091 , oOOOo00O00oOo + 'gofish.png' )
def Oo0OO0 ( url ) :
 I1 = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8092 , oOo0OOoO0 )
 for url in next :
  iII1iii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
def o0ooOOoo0 ( url ) :
 I1 = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( I1 )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( I1 )
 OO0oOo = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 in OO0oOo :
  oOo0OOoO0 = oOo0OOoO0
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8092 , oOo0OOoO0 )
 for url in next :
  iII1iii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , oOOOo00O00oOo + 'Next.png' )
  if 36 - 36: OOooOOo * oO0o / IIiIi1iI / oOo0O0Ooo - iIi1i1ii1
def o0oOo0OoO ( url ) :
 I1 = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( I1 )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 3 - 3: OOoOoo - ii * ii - oOo0O0Ooo / O00OOo00oo0o * Ii1I
  if 58 - 58: OOoOoo % iI11I1II1I1I / Ii % I11i . O00OOo00oo0o * OooOO000
  if 32 - 32: ii + I11i
  if 91 - 91: IIiIi1iI - O00OOo00oo0o * O00OOo00oo0o
ooOOOo0 = '{PQ},' ; i11111 = '{SC},' ; oOoOOOOO = '{XG},' ; ii1IIii = '{JP},' ; Ii1111Ii1 = '{HW},' ; III1Iiii1i11 = '{RT},'
def i1II ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 OO00 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 iiOOooooO0Oo = 'http://onlinemovies.tube/?s=' + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 if 10 - 10: iiII11i1I1IIi * ooOoO0O00 . oo0oO00 / O00OOo00oo0o . IIi / O00OOo00oo0o
 iIIIiIi1I1i = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 if 1 - 1: OooOO000 % IIiIi1iI
 O0ooo0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 o0Oo00o0 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i11II = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + o0oOOoOOO
 oOOoOo0Ooo = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 o0OOoOoo00 = ( i11 ( 'aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9tb3ZpZXNlYXJjaC5waHA=' ) )
 Oo0Ooo0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 if 19 - 19: ooOoO0O00 % oO0o - Ii1I . O00OOo00oo0o . iIi1i1ii1
 if 19 - 19: Ii1I / O00OOo00oo0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 if 35 - 35: I1ii11iIi11i * oo0oO00 / ii + o0o00Oo0O / ii / IIi
 if 44 - 44: ooOoO0O00 . Ii1I - IIiIi1iI . IIi . I11i + oo0oO00
 Iiii = OOoOO0oo0ooO ( iIIIiIi1I1i )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + iIi1i1ii1 % ooOoO0O00 . oo0oO00
 if 57 - 57: oo0oO00
 OoOO00OO0 = OOoOO0oo0ooO ( O0ooo0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IIII111 = OOoOO0oo0ooO ( i11II )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 iiI1IiI1I1I = OOoOO0oo0ooO ( oOOoOo0Ooo )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 IIIiI1i = OOoOO0oo0ooO ( o0OOoOoo00 )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 i1IIOOOoooOo00O = OOoOO0oo0ooO ( Oo0Ooo0 )
 if 6 - 6: ii - I1ii11iIi11i
 if 52 - 52: IIi + I1ii11iIi11i
 if 67 - 67: Ii1I % ii
 if 41 - 41: oO0o / OOoOoo + O00OOo00oo0o . O00OOo00oo0o / oo0oO00
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( I1 )
  next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( I1 )
  for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , o00oo0000 in IIIII11I1IiI :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    if 'movies' in o00oo0000 :
     iII1iii ( '[COLORred]*[COLOR' + II + ']' + o00oo0000 + '-' + iiI11ii1I1 + '-[COLORred] source MOVIE HUB[/COLOR]' , iiOOooooO0Oo , 90044 , oOo0OOoO0 )
  for iiOOooooO0Oo in next :
   II1II ( iiOOooooO0Oo )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 0 , "" , "Getting Source MOVIE HUB" )
   if 74 - 74: iIi1i1ii1 % Ii . o0o00Oo0O * oOo0O0Ooo * ooOoO0O00 * ii
   if 22 - 22: O00OOo00oo0o + OooOO000 - iiII11i1I1IIi + iI11I1II1I1I / O00OOo00oo0o - ii
   if 42 - 42: ii - OOooOOo - IIi * O00OOo00oo0o
   if 98 - 98: oO0o . iI11I1II1I1I % I1ii11iIi11i + ii
   if 2 - 2: O00OOo00oo0o % ii - IIiIi1iI * Ii1I * OOoOoo
   if 99 - 99: iI11I1II1I1I . I1ii11iIi11i / IIiIi1iI . IIi % oOo0O0Ooo * iiII11i1I1IIi
   if 95 - 95: oo0oO00
 if Iiii != 'Failed' :
  I1II1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( Iiii )
  for oOo0ooO0O0oo , iiI11ii1I1 in I1II1 :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iIIIiIi1I1i + oOo0ooO0O0oo ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
    if 31 - 31: Ii + iIi1i1ii1 % OOooOOo
    if 9 - 9: IIiIi1iI . iiII11i1I1IIi - I1ii11iIi11i . O00OOo00oo0o
    if 39 - 39: IIi
    if 70 - 70: OOoOoo % oO0o % oOo0O0Ooo
    if 95 - 95: OOooOOo - O00OOo00oo0o / o0o00Oo0O * oOo0O0Ooo - I11i
    if 12 - 12: iI11I1II1I1I % I1ii11iIi11i . OooOO000 . OOoOoo % Ii
    if 2 - 2: oo0oO00 * oo0oO00 . OOooOOo * iIi1i1ii1 * iI11I1II1I1I
    if 13 - 13: iiII11i1I1IIi / o0o00Oo0O . Ii * ooOoO0O00 % Ii
    if 8 - 8: OOooOOo - ii
 if OoOO00OO0 != 'Failed' :
  Oo00 = [ ]
  iIII1I1i1i = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOO00OO0 )
  for iiOOooooO0Oo , O00Ooo , iII1111III1I , iiii11i , iiI11ii1I1 in iIII1I1i1i :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    if iiI11ii1I1 in Oo00 :
     pass
    else :
     I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , iiOOooooO0Oo , 1016 , O00Ooo , iiii11i , iII1111III1I )
     Oo00 . append ( iiI11ii1I1 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if IIII111 != 'Failed' :
  iii111iii1 = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIII111 )
  for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in iii111iii1 :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + iiOOooooO0Oo , 7067 , oOo0OOoO0 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 17 - 17: oo0oO00 - IIiIiII11i - OooOO000 + iiII11i1I1IIi
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 54 - 54: IIiIiII11i * o0o00Oo0O % oOo0O0Ooo . iiII11i1I1IIi
    if 62 - 62: iIi1i1ii1 . Ii % o0o00Oo0O % O00OOo00oo0o - I1ii11iIi11i
    if 69 - 69: IIiIiII11i . OOooOOo * OOooOOo % iIi1i1ii1 + oOo0O0Ooo
    if 100 - 100: Ii - I1ii11iIi11i
    if 47 - 47: OooOO000 * OOooOOo * OOoOoo
    if 46 - 46: iIi1i1ii1
    if 42 - 42: iI11I1II1I1I
    if 32 - 32: I1ii11iIi11i - iIi1i1ii1 . ii - ii - I1ii11iIi11i . iI11I1II1I1I
    if 34 - 34: I1ii11iIi11i
 if IIIiI1i != 'Failed' :
  IiI1I1i1 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( IIIiI1i )
  for iiI11ii1I1 , iiOOooooO0Oo , O00Ooo , iiii11i , iII1111III1I in IiI1I1i1 :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source Reaper[/COLOR]' ) , iiOOooooO0Oo , 222 , O00Ooo , iiii11i , iII1111III1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 61 , "" , "Getting Reaper Links" )
    if 6 - 6: oOo0O0Ooo . IIiIiII11i + O00OOo00oo0o / oO0o % oOo0O0Ooo . ii
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if i1IIOOOoooOo00O != 'Failed' :
  Oooo000 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1IIOOOoooOo00O )
  for iiOOooooO0Oo , O00Ooo , iII1111III1I , iiii11i , iiI11ii1I1 in Oooo000 :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    I1I11i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , iiOOooooO0Oo , 222 , O00Ooo , iiii11i , iII1111III1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 37 - 37: oO0o . ooOoO0O00 + ooOoO0O00 / oOo0O0Ooo * IIiIi1iI * iIi1i1ii1
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 56 - 56: ii / oOo0O0Ooo . IIiIi1iI - ooOoO0O00
    if 60 - 60: OOooOOo % OOooOOo
    if 2 - 2: iIi1i1ii1 . o0o00Oo0O - oo0oO00 + OOoOoo
    if 96 - 96: iIi1i1ii1 + iIi1i1ii1
    if 28 - 28: OooOO000
    if 6 - 6: oOo0O0Ooo - OooOO000
    if 49 - 49: IIiIiII11i
    if 33 - 33: I11i - oo0oO00 % Ii1I * iiII11i1I1IIi . ii % iIi1i1ii1
    if 29 - 29: OooOO000 + IIiIiII11i . Ii . iIi1i1ii1 - o0o00Oo0O
    if 47 - 47: oo0oO00 . Ii1I - iI11I1II1I1I % IIiIiII11i / OOooOOo % ii
 Oo00oOO00 = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 13 - 13: OOoOoo . I1ii11iIi11i - iiII11i1I1IIi / oo0oO00 - I1ii11iIi11i - oOo0O0Ooo
 for II11 in Oo00oOO00 :
  I1iii = OOOO0OOoO0O0 + II11 + IIiiiiiiIi1I1
  oOO0o = OOoOO0oo0ooO ( I1iii )
  if oOO0o != 'Failed' :
   ooIi11II1IIIIIi = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOO0o )
   for iiOOooooO0Oo , O00Ooo , iII1111III1I , iiii11i , iiI11ii1I1 in ooIi11II1IIIIIi :
    if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
     I1I11i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] - Source Pandoras[/COLOR]' , iiOOooooO0Oo , 222 , O00Ooo , iiii11i , iII1111III1I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 83 - 83: iI11I1II1I1I + IIiIiII11i * oo0oO00 / o0o00Oo0O - OooOO000
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
     if 23 - 23: ooOoO0O00
 Oo00oOO00 = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 24 - 24: OOoOoo
 if 51 - 51: IIi % Ii
 for II11 in Oo00oOO00 :
  I1iii = OO00 + II11
  o0OoOoOo0O = OOoOO0oo0ooO ( I1iii )
  if o0OoOoOo0O != 'Failed' :
   IiIOOOoo = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( o0OoOoOo0O )
   for oOo0ooO0O0oo , iiI11ii1I1 in IiIOOOoo :
    if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
     i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( OO00 + II11 + oOo0ooO0O0oo ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 61 - 61: IIiIiII11i / IIiIiII11i . Ii
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
     if 61 - 61: oO0o - Ii / iiII11i1I1IIi % OOoOoo
     if 21 - 21: OooOO000 % OOoOoo % I1ii11iIi11i % o0o00Oo0O
def ii1iIi1iIiI1i ( ) :
 if 63 - 63: IIiIiII11i * oOo0O0Ooo - ii / oOo0O0Ooo
 if 50 - 50: OOooOOo % iIi1i1ii1 + OOooOOo * iIi1i1ii1 - IIi
 if 94 - 94: iI11I1II1I1I
 if 1 - 1: o0o00Oo0O
 if 2 - 2: oO0o . iiII11i1I1IIi
 if 97 - 97: I1ii11iIi11i
 if 65 - 65: I1ii11iIi11i % IIi / Ii / iI11I1II1I1I . O00OOo00oo0o + IIiIi1iI
 if 92 - 92: oo0oO00
 if 96 - 96: O00OOo00oo0o * iI11I1II1I1I / OOooOOo % IIi * IIiIiII11i
 if 3 - 3: IIi . I1ii11iIi11i / Ii + oO0o
 if 47 - 47: OOoOoo . IIi
 if 96 - 96: iiII11i1I1IIi % IIiIiII11i / IIiIi1iI % IIi / IIiIi1iI % Ii
 if 57 - 57: iiII11i1I1IIi - iiII11i1I1IIi % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
 if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - iIi1i1ii1 * iI11I1II1I1I
 if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / oo0oO00 * I11i + IIi
 if 89 - 89: IIiIi1iI * oOo0O0Ooo . oo0oO00
 if 75 - 75: IIiIi1iI - OooOO000 % OooOO000 + IIiIi1iI * I11i - Ii1I
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 if 26 - 26: iiII11i1I1IIi * iIi1i1ii1 % oOo0O0Ooo + OooOO000
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL3d3dy53YXRjaHNlcmllc2dvLnRvL3NlYXJjaC8=' ) ) + ( o0oOOoOOO ) . replace ( ' ' , '%20' )
 ooo0O = 'http://onlinemovies.tube/?s=' + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 iIIIiIi1I1i = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 I1iII1iI = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 O0ooo0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( iiI1i11II ) . replace ( ' ' , '+' )
 o0Oo00o0 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 i11II = ( i11 ( 'aHR0cDovL3JvZ3VlbWVkaWEueDEwLm14L3JlYXBlci9zZXJpYWxzZWFyY2gucGhw' ) )
 oOOoOo0Ooo = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 if 46 - 46: ii * iIi1i1ii1 . iI11I1II1I1I - o0o00Oo0O . ooOoO0O00 * oO0o
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 83 - 83: OooOO000 . Ii . ii . iIi1i1ii1
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 iii1i1iiiiIi = OOoOO0oo0ooO ( ooo0O )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 Iiii = OOoOO0oo0ooO ( iIIIiIi1I1i )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OO0OoO0o00 = OOoOO0oo0ooO ( I1iII1iI )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 OoOO00OO0 = cloudflare . source ( O0ooo0 )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 o0OoOoOo0O = OOoOO0oo0ooO ( o0Oo00o0 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 IIII111 = OOoOO0oo0ooO ( i11II )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 iiI1IiI1I1I = OOoOO0oo0ooO ( oOOoOo0Ooo )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 if 8 - 8: oO0o * I1ii11iIi11i
 if iiI1IiI1I1I != 'Failed' :
  IIiII = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( iiI1IiI1I1I )
  for iiOOooooO0Oo , O00Ooo , iII1111III1I , iiii11i , iiI11ii1I1 in IIiII :
   if iiI1i11II in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source HeroVision[/COLOR]' ) , iiOOooooO0Oo , 1016 , O00Ooo , iiii11i , iII1111III1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 48 - 48: OOooOOo . oOo0O0Ooo . iiII11i1I1IIi . OOoOoo
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 39 - 39: IIi . I1ii11iIi11i - OOooOOo * Ii
 if IIII111 != 'Failed' :
  iii111iii1 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( IIII111 )
  for iiI11ii1I1 , iiOOooooO0Oo , O00Ooo , iiii11i , iII1111III1I in iii111iii1 :
   if iiI1i11II in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source Reaper[/COLOR]' ) , iiOOooooO0Oo , 90037 , O00Ooo , iiii11i , iII1111III1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 20 , "" , "Getting Reaper Links" )
    if 4 - 4: OOooOOo * o0o00Oo0O - iiII11i1I1IIi
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 72 - 72: iiII11i1I1IIi + IIiIi1iI / oOo0O0Ooo . OOoOoo % oO0o / Ii
    if 13 - 13: O00OOo00oo0o % I11i + IIi + O00OOo00oo0o + Ii - Ii1I
    if 70 - 70: IIiIiII11i * IIiIiII11i . oOo0O0Ooo
    if 11 - 11: OooOO000
    if 20 - 20: iIi1i1ii1 . O00OOo00oo0o % iIi1i1ii1
    if 5 - 5: IIi + OooOO000
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting CoolSeries Links" )
    if 23 - 23: O00OOo00oo0o % iI11I1II1I1I . iiII11i1I1IIi
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  OO0oO0O = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( iii1i1iiiiIi )
  for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , i1i1II1i11 in i1I :
   if iiI1i11II in iiI11ii1I1 . lower ( ) :
    if 'season' in i1i1II1i11 :
     iII1iii ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + ' - [COLORred]Source - Tv HUB[/COLOR]' , iiOOooooO0Oo , 90054 , oOo0OOoO0 , oOo0OOoO0 , '' )
    if 'episodes' in i1i1II1i11 :
     iII1iii ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + ' - [COLORred]Source - Tv HUB[/COLOR]' , iiOOooooO0Oo , 90044 , oOo0OOoO0 , oOo0OOoO0 , '' )
  for iiOOooooO0Oo in OO0oO0O :
   iII1iii ( '[COLORred]*[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , iiOOooooO0Oo , 90053 , oOOOo00O00oOo + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 11 - 11: Ii1I / o0o00Oo0O + IIiIiII11i
   i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( I1 )
  for oOo0OOoO0 , iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
   if iiI1i11II in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( '[COLOR' + II + ']' + ( iiI11ii1I1 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - WatchSeries[/COLOR]' , 'http://www.watchseriesgo.to' + iiOOooooO0Oo , 10044 , oOo0OOoO0 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 50 , "" , "Getting Source WatchSeries Links" )
    if 95 - 95: O00OOo00oo0o + OOoOoo * iI11I1II1I1I
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 17 - 17: oO0o - I1ii11iIi11i * o0o00Oo0O / iIi1i1ii1
    if 19 - 19: ooOoO0O00 - iI11I1II1I1I . iiII11i1I1IIi
    if 2 - 2: iIi1i1ii1
    if 12 - 12: Ii - iI11I1II1I1I * OOoOoo * OooOO000
    if 19 - 19: o0o00Oo0O + oo0oO00 + I11i
    if 81 - 81: iI11I1II1I1I
    if 51 - 51: I11i . Ii1I * iIi1i1ii1 / I1ii11iIi11i * IIiIiII11i / o0o00Oo0O
    if 44 - 44: Ii % O00OOo00oo0o % oo0oO00 + iiII11i1I1IIi * oo0oO00 . iIi1i1ii1
    if 89 - 89: ii % IIiIiII11i - oO0o % Ii
    if 7 - 7: OOoOoo
 if Iiii != 'Failed' :
  I1II1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( Iiii )
  for iiI11ii1I1 in I1II1 :
   if iiI1i11II in iiI11ii1I1 . lower ( ) :
    iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iIIIiIi1I1i + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 15 - 15: I1ii11iIi11i + OooOO000 + oOo0O0Ooo * I11i
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if OO0OoO0o00 != 'Failed' :
  oo00OO0000oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( OO0OoO0o00 )
  for iiI11ii1I1 in oo00OO0000oO :
   if iiI1i11II in iiI11ii1I1 . lower ( ) :
    iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( I1iII1iI + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 33 - 33: I11i * I1ii11iIi11i
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if OoOO00OO0 != 'Failed' :
  iIII1I1i1i = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( OoOO00OO0 )
  for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in iIII1I1i1i :
   if iiI1i11II in iiI11ii1I1 . lower ( ) :
    iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + ' -[COLORgold] Source - Dizi[/COLOR]' , iiOOooooO0Oo , 8062 , oOo0OOoO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 80 , "" , "Getting Dizi Links" )
    if 88 - 88: O00OOo00oo0o % IIi - OOooOOo - OOooOOo . oOo0O0Ooo
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if o0OoOoOo0O != 'Failed' :
  IiIOOOoo = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0OoOoOo0O )
  for iiOOooooO0Oo , O00Ooo , iII1111III1I , iiii11i , iiI11ii1I1 in IiIOOOoo :
   if iiI1i11II in iiI11ii1I1 . lower ( ) :
    I1IIII1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] Source Scooby[/COLOR]' ) , iiOOooooO0Oo , 1016 , O00Ooo , iiii11i , iII1111III1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 52 - 52: IIiIiII11i / IIiIiII11i / oOo0O0Ooo - O00OOo00oo0o
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 91 - 91: oOo0O0Ooo + I11i % IIiIiII11i + oO0o
 Oo0o0OOo0Oo0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for II11 in Oo0o0OOo0Oo0 :
  I1iii = OOOO0OOoO0O0 + II11 + IIiiiiiiIi1I1
  i1IIOOOoooOo00O = OOoOO0oo0ooO ( I1iii )
  if i1IIOOOoooOo00O != 'Failed' :
   Oooo000 = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( i1IIOOOoooOo00O )
   for iiI11ii1I1 , iII1111III1I , iiOOooooO0Oo , oOo0OOoO0 , O0OoooO0 , o0ii1i in Oooo000 :
    if iiI1i11II in iiI11ii1I1 . lower ( ) :
     I1IIII1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] - Source Pandoras[/COLOR]' , iiOOooooO0Oo , o0ii1i , oOo0OOoO0 , O0OoooO0 , iII1111III1I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 88 - 88: iIi1i1ii1 / ii % OOooOOo - ooOoO0O00
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
     if 49 - 49: I11i - iI11I1II1I1I
     if 61 - 61: OooOO000 * IIiIi1iI
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1I1IiIiiI1II ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( o0oOOoOOO ) . replace ( ' ' , '+' )
 if 39 - 39: ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 37 - 37: OooOO000 . I11i / iIi1i1ii1 / IIi * ooOoO0O00
 if I1 != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( I1 )
  for iiOOooooO0Oo , iiI11ii1I1 in i1I :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + iiOOooooO0Oo ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 90 - 90: oOo0O0Ooo . IIiIiII11i - ooOoO0O00 + oo0oO00
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
o0oOoo00 = '{ZH},' ; Ii11iIi1iIiii = '{IX},' ; iIIIi = '{LM},'
if 11 - 11: iiII11i1I1IIi
def IIIIi1 ( url ) :
 IiII1II1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( IiII1II1 )
 for url , iIIii , IIIIoOo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( ( iIIii ) . replace ( 'Sezon' , ' Season ' ) + ( IIIIoOo ) . replace ( 'Bölüm' , ' Episode ' ) + iiI11ii1I1 , url , 8063 , '' )
  if 61 - 61: iIi1i1ii1 + oOo0O0Ooo / ooOoO0O00 + ooOoO0O00 / oo0oO00
  if 47 - 47: O00OOo00oo0o
  if 25 - 25: OooOO000 + oOo0O0Ooo + OOooOOo + O00OOo00oo0o % o0o00Oo0O
  if 26 - 26: IIiIi1iI + OOooOOo
def II111I1i1 ( url ) :
 IiII1II1 = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( IiII1II1 )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , url , 222 , '' )
  if 10 - 10: o0o00Oo0O . OOooOOo * OOoOoo / O00OOo00oo0o / ooOoO0O00
  if 32 - 32: o0o00Oo0O / IIi . IIiIi1iI % O00OOo00oo0o
  if 18 - 18: OOoOoo * OooOO000 / iiII11i1I1IIi / o0o00Oo0O
  if 11 - 11: iI11I1II1I1I / iIi1i1ii1 + ii % ooOoO0O00 * Ii
def OoOooooo ( ) :
 if 87 - 87: IIiIiII11i - ii / ooOoO0O00 . iIi1i1ii1 - I1ii11iIi11i . Ii
 IiII1II1 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( IiII1II1 )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 , IIIIoOo in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 + '  -  ' + ( IIIIoOo ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , iiOOooooO0Oo , 8063 , oOo0OOoO0 )
  if 47 - 47: I1ii11iIi11i % oO0o - IIiIi1iI - I1ii11iIi11i * oo0oO00
def OOOOO0oOOoO ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 8002 , oOo0OOoO0 )
def iiiiII ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , time , url , iiI11ii1I1 , oOiI111I1III in IIIII11I1IiI :
  I1IIII1i ( '%s %s' % ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , time ) , url , 1015 , oOo0OOoO0 , oOiI111I1III )
  if 15 - 15: iiII11i1I1IIi % oOo0O0Ooo - Ii / oO0o / OOooOOo + OOooOOo
def oo000oiIIIII ( ) :
 if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
 iII1iii ( 'Coronation Street' , '' , 8001 , '' )
 iII1iii ( 'Eastenders' , '' , 8002 , '' )
 iII1iii ( 'Emmerdale' , '' , 8003 , '' )
 iII1iii ( 'Hollyoaks' , '' , 8004 , '' )
 iII1iii ( 'Im a Celebrity' , '' , 8005 , '' )
 if 22 - 22: oO0o . OOooOOo % IIiIiII11i - o0o00Oo0O
 if 52 - 52: oO0o
 if 49 - 49: iIi1i1ii1 . Ii1I % IIiIi1iI . I1ii11iIi11i * IIi
 if 44 - 44: iI11I1II1I1I / o0o00Oo0O * I1ii11iIi11i + oOo0O0Ooo . IIiIi1iI
def I1iIi1i ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Holly' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in iiOOooooO0Oo :
    i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 7 - 7: OOooOOo / OOooOOo . O00OOo00oo0o * o0o00Oo0O + OOoOoo + oo0oO00
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 98 - 98: IIiIiII11i * OOoOoo - oOo0O0Ooo % I11i - OooOO000 % Ii1I
def Oo0Oo0o00oO ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'East' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in iiOOooooO0Oo :
    i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 81 - 81: Ii1I % OooOO000
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 22 - 22: ii + I11i . iiII11i1I1IIi + oOo0O0Ooo + ii . OOooOOo
def o0O0o ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Emmer' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in iiOOooooO0Oo :
    i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 48 - 48: O00OOo00oo0o
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 12 - 12: OOooOOo * IIiIi1iI
def ooOoooOoo0oO ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Coro' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in iiOOooooO0Oo :
    i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 50 - 50: IIiIi1iI
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * IIi
def oo0ooO0O ( ) :
 I1 = O000oo ( 'http://uksoapshare.blogspot.co.uk/' )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( I1 )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Celeb' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in iiOOooooO0Oo :
    i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , iiOOooooO0Oo . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 83 - 83: I1ii11iIi11i / IIiIi1iI
def II1iiIiI1 ( name , url ) :
 Ii1I11IIi1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if Ii1I11IIi1 :
  I1iiiiI = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OoO000O0Oo = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( OoO000O0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OoO000O0Oo = open_url ( url )
  iii11I1 = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( OoO000O0Oo ) [ - 1 ]
  I1iiiiI = iii11I1 . replace ( '\\/' , '/' )
 iioo0o0OoOOO = xbmcgui . ListItem ( name , '' , '' )
 iioo0o0OoOOO . setPath ( I1iiiiI )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iioo0o0OoOOO )
 if 44 - 44: oo0oO00
 if 95 - 95: O00OOo00oo0o - OOooOOo / ii . ii
def iiiIII1iii1I ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , iiOOooooO0Oo , 7071 , oOOOo00O00oOo + 'popcorn.png' )
 for iiOOooooO0Oo , iiI11ii1I1 in i1I :
  iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , iiOOooooO0Oo , 7071 , oOOOo00O00oOo + 'popcorn.png' )
  if 32 - 32: IIi - iIi1i1ii1 . oO0o * IIiIi1iI + OOoOoo . ooOoO0O00
def O0O0O00OoO0O ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Movies' in iiI11ii1I1 :
   iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( iiOOooooO0Oo ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , oOOOo00O00oOo + 'popcorn.png' )
def i1II11III ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0OOoO0 )
 for url in i1I :
  iII1iii ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , oOOOo00O00oOo + 'Next.png' )
  if 95 - 95: iiII11i1I1IIi + I11i - Ii % oO0o / oo0oO00
  if 80 - 80: O00OOo00oo0o * oo0oO00 * ooOoO0O00
def OooOoOo ( url ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url , oOo0OOoO0 in IIIII11I1IiI :
  if '{{' in iiI11ii1I1 :
   pass
  else :
   iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOo0OOoO0 )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
IiIii1i = '{UJ},' ; I1i11i1II = '{WE},' ; OOoOo0oOooo = '{WP},' ; OOo0o = '{PP},'
def Ooo0O0ooo0o ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url , oOo0OOoO0 in IIIII11I1IiI :
  if '{{' in iiI11ii1I1 :
   pass
  else :
   iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0OOoO0 )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0Oo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  O0oOo00Oo0oo0 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0oOo00Oo0oo0 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOOOo00O00oOo + 'popcorn.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: O00OOo00oo0o / O00OOo00oo0o % oo0oO00
 if 97 - 97: ii * I11i + ii % iIi1i1ii1 * I1ii11iIi11i
 if 35 - 35: iI11I1II1I1I % OooOO000 - ooOoO0O00
def I1i1iI1I1II ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '(cooltvseries.com)' in iiI11ii1I1 :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
 for url , iiI11ii1I1 in i1I :
  if '(cooltvseries.com)' in iiI11ii1I1 :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , oOOOo00O00oOo + 'CoolSeries.png' )
def iiI11II ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iii1 ( ( url ) . replace ( ' ' , '%20' ) )
Oo0OOooO00OO = '{XX},' ; Ii1i1 = '{UD},' ; iiiIiIIiIiiii = '{YT},' ; o00O0OooO0 = '{JS},' ; iii1II11II1 = '{PF},'
if 30 - 30: OOoOoo / Ii % oO0o * IIi
def i1oOOOoOO ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  i11i1iiiII ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( iiOOooooO0Oo ) ) , 222 , oOo0OOoO0 )
  if 80 - 80: ii
def IIIIIIi1i ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  if 'youtu' in url :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oOo0OOoO0 )
 for url in next :
  iII1iii ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , oOOOo00O00oOo + 'Next.png' )
  if 65 - 65: oo0oO00 * ooOoO0O00 . ii % IIiIi1iI
def OoOo00oOoo0oO ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 35 - 35: O00OOo00oo0o - ooOoO0O00 / OOoOoo
def iI1IiiiiI ( url ) :
 OoO000O0Oo = O000oo
 IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOo0OOoO0 )
  if 12 - 12: Ii . iiII11i1I1IIi * IIi % ooOoO0O00 . IIiIi1iI
  if 58 - 58: OooOO000 % iI11I1II1I1I . iI11I1II1I1I / iiII11i1I1IIi
  if 79 - 79: oO0o / IIi - ooOoO0O00 + ooOoO0O00 - OOoOoo + OOoOoo
  if 67 - 67: oO0o * oO0o / ii
  if 79 - 79: I11i % iI11I1II1I1I / IIiIiII11i / iIi1i1ii1 / iIi1i1ii1 + o0o00Oo0O
def ii11 ( ) :
 if 97 - 97: oO0o + iI11I1II1I1I
 iII1iii ( 'All Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'Entertainment' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'Movies' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'Music' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'News' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'Sports' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'Documentary' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'Kids' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'Food' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'Religious' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'USA Channels' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 iII1iii ( 'Other' , '' , 7021 , oOOOo00O00oOo + 'livetv.png' )
 if 79 - 79: IIiIi1iI + oo0oO00 - IIiIiII11i . I1ii11iIi11i
 if 26 - 26: OOoOoo
def oo0o0o ( Cat_Name ) :
 if 25 - 25: OOoOoo * O00OOo00oo0o - oo0oO00 * Ii * oOo0O0Ooo * IIi
 Ooii1II11IIII = False
 oO0OOOO0o0o0 = '0'
 if Cat_Name == 'All Channels' : Ooii1II11IIII = True
 if Cat_Name == 'Entertainment' : oO0OOOO0o0o0 = '1'
 if Cat_Name == 'Movies' : oO0OOOO0o0o0 = '2'
 if Cat_Name == 'Music' : oO0OOOO0o0o0 = '3'
 if Cat_Name == 'News' : oO0OOOO0o0o0 = '4'
 if Cat_Name == 'Sports' : oO0OOOO0o0o0 = '5'
 if Cat_Name == 'Documentary' : oO0OOOO0o0o0 = '6'
 if Cat_Name == 'Kids' : oO0OOOO0o0o0 = '7'
 if Cat_Name == 'Food' : oO0OOOO0o0o0 = '8'
 if Cat_Name == 'Religious' : oO0OOOO0o0o0 = '9'
 if Cat_Name == 'USA Channels' : oO0OOOO0o0o0 = '10'
 if Cat_Name == 'Other' : oO0OOOO0o0o0 = '11'
 if 21 - 21: o0o00Oo0O * IIiIi1iI % oO0o
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 print 'Len Match: >>>' + str ( len ( IIIII11I1IiI ) )
 for iiI11ii1I1 , oOo0OOoO0 , Iii1 in IIIII11I1IiI :
  I11i1IiiI = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0OOoO0 ) . replace ( '\\' , '' )
  if Iii1 == oO0OOOO0o0o0 :
   iII1iii ( iiI11ii1I1 , '' , 7022 , I11i1IiiI )
  elif Ooii1II11IIII == True :
   iII1iii ( iiI11ii1I1 , '' , 7022 , I11i1IiiI )
  else : pass
  if 75 - 75: OOooOOo / ii / iiII11i1I1IIi % OOooOOo * iIi1i1ii1 * OOoOoo
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 11 - 11: Ii1I / IIi . iIi1i1ii1 * Ii1I
def II1i1iii1iiiI ( Search_Name ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , iiOOooooO0Oo , ooo0O , iIIIiIi1I1i in IIIII11I1IiI :
  I11i1IiiI = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0OOoO0 ) . replace ( '\\' , '' )
  i11i1iiiII ( Search_Name + ': Link 1' , ( iiOOooooO0Oo ) . replace ( '\\' , '' ) , 222 , I11i1IiiI )
  i11i1iiiII ( Search_Name + ': Link 2' , ( ooo0O ) . replace ( '\\' , '' ) , 222 , I11i1IiiI )
  i11i1iiiII ( Search_Name + ': Link 3' , ( iIIIiIi1I1i ) . replace ( '\\' , '' ) , 222 , I11i1IiiI )
  if 62 - 62: iiII11i1I1IIi
def o00O00oOooo ( ) :
 OoO000O0Oo = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , ( iiOOooooO0Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , oOOOo00O00oOo + 'english.png' )
def oooii111I1I1I ( ) :
 OoO000O0Oo = O000oo ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , ( iiOOooooO0Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'xxx.png' )
def iIIiIi1IiI1 ( ) :
 OoO000O0Oo = O000oo ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , iiOOooooO0Oo in IIIII11I1IiI :
  i11i1iiiII ( iiI11ii1I1 , ( iiOOooooO0Oo ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , oOOOo00O00oOo + 'vod(1).png' )
  if 80 - 80: IIiIiII11i / OOooOOo % Ii1I . iI11I1II1I1I % iiII11i1I1IIi . I11i
def OO00oo ( url ) :
 url
 oOOOoo00 = xbmcgui . ListItem ( iiI11ii1I1 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOOoo00 )
 return
 if 88 - 88: o0o00Oo0O / I11i * I11i . I11i . o0o00Oo0O
 if 27 - 27: Ii % OooOO000 + iIi1i1ii1 . IIi
def iIIi1I1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OoO000O0Oo )
 for url , iII1111III1I , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , ( iII1111III1I ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  iII1iii ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , oOOOo00O00oOo + 'Next.png' )
  if 100 - 100: Ii . IIi . Ii
def o00Oo ( url ) :
 I1 = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( I1 )
 for url , iII1111III1I , oOo0OOoO0 in IIIII11I1IiI :
  I1I11i ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , iII1111III1I )
  i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 o0OO0OO000OO = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( I1 )
 for I1III11i11Iii in o0OO0OO000OO :
  OooooOOoo0 = ( I1III11i11Iii ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  I1IIII1i ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , OooooOOoo0 )
  if 16 - 16: IIi . IIiIiII11i - iIi1i1ii1 - ii
def ooOoOoOoo ( INFO ) :
 iiIiI1i1 ( 'info for workout' , INFO )
 if 25 - 25: I1ii11iIi11i + I11i - oO0o
 if 57 - 57: IIiIiII11i . ooOoO0O00
 if 33 - 33: OooOO000 + I1ii11iIi11i % iiII11i1I1IIi . oo0oO00
def i1II1i ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( ( iiI11ii1I1 ) . replace ( 'SlyNet' , '' ) , url , 9031 , oOOOo00O00oOo + 'Sport.png' )
def O0oooooO0oOOo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , url , 9032 , oOOOo00O00oOo + 'icon.png' )
def oo0O0OO0Oooo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '=' in iiI11ii1I1 :
   pass
  else :
   i11i1iiiII ( ( iiI11ii1I1 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 10012 , oOOOo00O00oOo + 'icon.png' )
def IiiI11Iii ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if '=' in iiI11ii1I1 :
   pass
  else :
   i11i1iiiII ( iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'icon.png' )
   if 42 - 42: iiII11i1I1IIi + ooOoO0O00 - iIi1i1ii1 / OOoOoo . OooOO000
   if 30 - 30: I1ii11iIi11i + iIi1i1ii1 % Ii * ooOoO0O00 + oOo0O0Ooo % IIi
   if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % O00OOo00oo0o
def OOOo0o ( url ) :
 i11i1iiiII ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , oOOOo00O00oOo + 'bamf.png' , oOOOo00O00oOo + 'bamf.png' )
 i11i1iiiII ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , oOOOo00O00oOo + 'bamf.png' , oOOOo00O00oOo + 'bamf.png' )
 iII1iii ( '[COLOR' + II + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , oOOOo00O00oOo + 'bamf.png' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if 'mp4' in url :
   pass
  else :
   i11i1iiiII ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'bamf.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo0o0o0o0o0 ( url ) :
 i11i1iiiII ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 i11i1iiiII ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 iII1iii ( '[COLOR' + II + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , oOOOo00O00oOo + 'bamf.png' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  if 'mp4' in url :
   i11i1iiiII ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'bamf.png' )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: oOo0O0Ooo / I1ii11iIi11i % iI11I1II1I1I / o0o00Oo0O . Ii1I
 if 53 - 53: I11i % ii - oo0oO00 - ooOoO0O00 / oO0o
 if 33 - 33: OOoOoo * iiII11i1I1IIi
def OO0oOOOOO ( ) :
 OoO000O0Oo = O000oo ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'Daily' in iiI11ii1I1 :
   iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , iiOOooooO0Oo , 9008 , Oo00OOOOO )
def OoOo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  iII1iii ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def oO0i1ii1i1 ( url ) :
 i11i1iiiII ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 i11i1iiiII ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 i11i1iiiII ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  i11i1iiiII ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , Oo00OOOOO )
  if 42 - 42: oo0oO00
def iiiiiiI1iIi ( ) :
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if '.m3u' in iiOOooooO0Oo :
   iII1iii ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + iiOOooooO0Oo ) , 9011 , oOOOo00O00oOo + 'disclose.png' )
def iI1Ii11IIiII ( url ) :
 OoO000O0Oo = cloudflare . source ( url )
 IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  i11i1iiiII ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 10012 , '' )
  if 42 - 42: O00OOo00oo0o
def I1i1iiiI1 ( ) :
 OoO000O0Oo = O000oo ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  if 'category' in iiOOooooO0Oo :
   iII1iii ( iiI11ii1I1 , 'http://www.disclose.tv/' + iiOOooooO0Oo , 7010 , oOOOo00O00oOo + 'disclose.png' )
   if 70 - 70: I11i / iiII11i1I1IIi + oo0oO00 % oOo0O0Ooo % I1ii11iIi11i + oO0o
   if 80 - 80: IIi
def iiii1IiI1i1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , 'http://www.disclose.tv/' + url , 7011 , oOo0OOoO0 )
 for url in next :
  iII1iii ( 'NEXT' , url , 7010 , oOOOo00O00oOo + 'Next.png' )
  if 3 - 3: OOooOOo
  if 33 - 33: ii . OOoOoo / OooOO000 + ii - Ii1I
def II1I11i ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  if 'http' in url :
   i11i1iiiII ( 'video/flv' , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url , iiI11ii1I1 in i1I :
  i11i1iiiII ( iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'disclose.png' )
 for url in I1II1 :
  i11i1iiiII ( 'YT Link' , url , 8043 , oOOOo00O00oOo + 'disclose.png' )
  if 97 - 97: oOo0O0Ooo
  if 56 - 56: iIi1i1ii1 * ooOoO0O00 + O00OOo00oo0o * I11i % oO0o
def IiiI1i1I1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , oOOOo00O00oOo + 'icon.png' )
  if 59 - 59: IIiIiII11i
def OOo0OOO0OO ( name , url , img ) :
 I1 = O000oo ( url )
 O0O00000o = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( I1 )
 oOOOoOo00O0 = len ( O0O00000o )
 if 86 - 86: iI11I1II1I1I * OooOO000 * iIi1i1ii1 / oO0o % IIiIi1iI - o0o00Oo0O
 if 63 - 63: Ii1I
 if oOOOoOo00O0 == 1 :
  for II1IiiI in O0O00000o :
   II1IiiI = II1IiiI . replace ( 'player' , 'watch' )
   ooO0O0OOO = II1IiiI + '&fv=&sou='
   IiIII = O000oo ( ooO0O0OOO )
   OOo00O0O = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( IiIII )
   for oO0o0O0Ooo0o in OOo00O0O :
    IIIIiI1i1111iI1i = False
    Resolve ( oO0o0O0Ooo0o )
    if 85 - 85: iI11I1II1I1I + iIi1i1ii1 - IIiIiII11i * OOoOoo * OooOO000
 elif oOOOoOo00O0 > 1 :
  if 17 - 17: IIi . oo0oO00 - I1ii11iIi11i * iI11I1II1I1I * IIiIi1iI
  for II1IiiI in O0O00000o :
   iiOo0OoOoOo0o = O000oo ( II1IiiI )
   iiIIIi1ii = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iiOo0OoOoOo0o )
   iii1IiI = iiIIIi1ii
   iii1IiI = ( str ( iii1IiI ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + iii1IiI
   i11i1iiiII ( 'DOUBLE LINK' , iii1IiI , 424 , '' )
   if 87 - 87: oOo0O0Ooo - o0o00Oo0O - iiII11i1I1IIi * O00OOo00oo0o % O00OOo00oo0o
   for url in iiIIIi1ii :
    iII1iii ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     ooo0O = Google . resolve ( url )
    except :
     pass
    try :
     Oo0o00o0oOoo0 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( ooo0O ) )
     for I1II , o000 in Oo0o00o0oOoo0 :
      if 8 - 8: I1ii11iIi11i
      HD_URLS . append ( I1II )
      SD_URLS . append ( o000 )
    except :
     pass
 else :
  pass
  if 22 - 22: IIiIi1iI % OOooOOo / I11i
def oO0OIiIi1ii1Ii ( ) :
 if 6 - 6: OooOO000 % I11i + O00OOo00oo0o
 if 91 - 91: I11i + o0o00Oo0O * oo0oO00 * OOoOoo * Ii1I
 iII1iii ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , oOOOo00O00oOo + 'Movies.png' )
 if 83 - 83: ii
 iII1iii ( 'Search Movies' , '' , 7017 , oOOOo00O00oOo + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 52 - 52: I11i / OOooOOo % oo0oO00 % oO0o / OOoOoo % I11i
 if 88 - 88: IIi / Ii / iIi1i1ii1 / Ii * Ii1I % iiII11i1I1IIi
def II1I1iI1i1IiI ( ) :
 OoO000O0Oo = O000oo ( 'http://cnfstudio.com/' )
 IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , 'http://cnfstudio.com/genre/' + iiOOooooO0Oo , 7003 , oOOOo00O00oOo + 'icon.png' )
  if 9 - 9: oo0oO00 / ii / IIi * Ii - IIiIi1iI + O00OOo00oo0o
OOooO0OOoo = xbmcgui . Dialog ( )
if 69 - 69: o0o00Oo0O . O00OOo00oo0o - o0o00Oo0O
oOOoO0iiIii1iii = '{UN},' ; OO0O0Ooo0 = '{IG},' ; IIIiIII1 = '{PL},' ; OOo0OOo = '{LO},' ; OOIiI1IIIiI1I1i = '{LP},' ; oO00O0oO = '{HA},' ; O00O00 = '{XD},' ; IIi1i = '{TA},' ; o0ooOOOo0O = '{DP},' ; i11111i1I1IiI = '{JT},' ; Ii111i1I1i1i = '{JJ},' ; o0o00o0Oo = '{MM},' ; O0OooO00ooOo0 = '{FQ},' ; OoOOoO0Ooo0oo = '{HH},'
if 33 - 33: oOo0O0Ooo / iiII11i1I1IIi . I1ii11iIi11i
def O0OoO0o ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OoO000O0Oo )
 o0Oo00oOOO0o = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOo0OOoO0 )
 o0Oo00oOOO0o = o0Oo00oOOO0o
 for url in o0Oo00oOOO0o :
  iII1iii ( 'Next Page' , url , 7003 , oOOOo00O00oOo + 'Next.png' )
  if 60 - 60: iiII11i1I1IIi . OOooOOo . IIiIiII11i
def I1Iiii11 ( url ) :
 if 43 - 43: oOo0O0Ooo
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  i1Oo00 = url + '&fv=&sou='
  i1Oo00 = i1Oo00 . replace ( 'player' , 'watch' )
  OOOooOOO00O = I1i1Iii1111Ii ( i1Oo00 )
  Ii1IiIi1i111 = I1i1Iii1111Ii ( url )
  if 80 - 80: Ii . Ii + oo0oO00 / ii - oOo0O0Ooo . OOoOoo
  if 53 - 53: IIiIi1iI - OOooOOo + OOoOoo
def I1i1Iii1111Ii ( url ) :
 if 100 - 100: oo0oO00 + oO0o
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  II1IIIii ( url )
  if 95 - 95: Ii . I11i + ii % I1ii11iIi11i
  if 21 - 21: OooOO000 - I11i / iiII11i1I1IIi % o0o00Oo0O / iI11I1II1I1I / OooOO000
def iIiii1Ii ( ) :
 I1IIII1i ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , oOOOo00O00oOo + 'LocalM3U.png' , O0o0Oo , '' )
 I1IIII1i ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , oOOOo00O00oOo + 'RemoteM3U.png' , O0o0Oo , '' )
 if 17 - 17: o0o00Oo0O - iIi1i1ii1 + OOoOoo
def iIIII11iII ( ) :
 if os . path . exists ( iiI1IiI ) :
  O0O0OOo = open ( iiI1IiI , 'r' )
  for oOOOoo00 in O0O0OOo :
   ii1i111 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oOOOoo00 )
   for iiI11ii1I1 , iiOOooooO0Oo in ii1i111 :
    i11i1iiiII ( iiI11ii1I1 , iiOOooooO0Oo , 222 , oOOOo00O00oOo + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 66 - 66: O00OOo00oo0o * ii / Ii1I - iiII11i1I1IIi - IIiIi1iI * iiII11i1I1IIi
def OOoOooO0o ( url ) :
 if os . path . exists ( Remote ) :
  I1 = i1i11I1I1iii1 ( url )
  IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
  for iiI11ii1I1 , url in IIIII11I1IiI :
   url = ( url ) . strip ( )
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 58 - 58: Ii1I / oO0o / oo0oO00 + OOoOoo % OooOO000 / IIiIiII11i
  if 95 - 95: IIiIiII11i / iIi1i1ii1 % iiII11i1I1IIi - ii
def Iiii1i1 ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + iiOOooooO0Oo
 iiI11ii1I1 = 'plugin.video.GenieTv'
 if 45 - 45: oO0o * ii / o0o00Oo0O . O00OOo00oo0o / OOooOOo
 oO0I1ii11i1 ( iiOOooooO0Oo , iiI11ii1I1 )
 if 40 - 40: I11i * OOoOoo / Ii1I / O00OOo00oo0o - OOoOoo
def II1I ( ) :
 I1 = O000oo ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( I1 )
 for iiOOooooO0Oo in IIIII11I1IiI :
  iiOOooooO0Oo = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + iiOOooooO0Oo
 iiI11ii1I1 = 'repository.GenieTv'
 if 52 - 52: oOo0O0Ooo - iiII11i1I1IIi / I1ii11iIi11i % I11i
 oO0I1ii11i1 ( iiOOooooO0Oo , iiI11ii1I1 )
 if 19 - 19: o0o00Oo0O + iIi1i1ii1 * iIi1i1ii1 * ooOoO0O00
 if 28 - 28: oo0oO00 * OooOO000
def OOOoo0OO ( ) :
 OooOoOO0 = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , OooOoOO0 )
 if iI1i11iII111 == 0 :
  Oo0i11iiI11II ( )
 if iI1i11iII111 == 1 :
  iI1iIii ( )
  if 42 - 42: Ii1I / IIiIi1iI . iI11I1II1I1I
  if 5 - 5: ii
  if 21 - 21: IIi
  if 71 - 71: IIi + oo0oO00 . iiII11i1I1IIi
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
iiii1I = 'https://addons.tvaddons.ag/'
if 73 - 73: iIi1i1ii1 * ii * iiII11i1I1IIi - Ii
def iI1iIii ( ) :
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 IiIi1II111I = 'https://addons.tvaddons.ag/search/?keyword=' + iiI1i11II
 I1 = O000oo ( IiIi1II111I )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for iiOOooooO0Oo , oOOoo , iiI11ii1I1 in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , iiOOooooO0Oo , 10054 , 'https://addons.tvaddons.ag/' + oOOoo , O0o0Oo , '' )
  if 58 - 58: I11i + OOooOOo - OOoOoo
  if 82 - 82: iIi1i1ii1 . iI11I1II1I1I / iIi1i1ii1 / oo0oO00 % iI11I1II1I1I
def Oo0i11iiI11II ( ) :
 I1 = O000oo ( iiii1I )
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
   if 34 - 34: IIi
   if 99 - 99: IIiIiII11i
def Addon ( url ) :
 I1 = O000oo ( url )
 I1I111i1I = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( I1 )
 IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( I1 )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if 'Please' in iiI11ii1I1 :
   pass
  else :
   I1I11i ( iiI11ii1I1 , url , 10054 , 'https://addons.tvaddons.ag/' + oOo0OOoO0 , O0o0Oo , '' )
 for url in I1I111i1I :
  I1IIII1i ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , oOOOo00O00oOo + 'Next.png' , O0o0Oo , '' )
  if 81 - 81: Ii1I % iI11I1II1I1I
  if 70 - 70: o0o00Oo0O . iI11I1II1I1I * IIiIiII11i
def iIi1i ( url , name ) :
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
   if 3 - 3: iIi1i1ii1 * IIiIi1iI . oO0o * ii + OOooOOo / o0o00Oo0O
def oO0I1ii11i1 ( url , name ) :
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
 if 60 - 60: iiII11i1I1IIi
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 97 - 97: Ii * iI11I1II1I1I / IIiIiII11i
 if 66 - 66: IIiIiII11i + OooOO000 * oo0oO00 % iiII11i1I1IIi / ooOoO0O00 / iI11I1II1I1I
def OO0OO0 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , oOOoo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , url , 1007 , oOOoo )
def i11IIii ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , oOOoo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , oOOoo )
  if 48 - 48: OooOO000
  if 26 - 26: Ii1I . iIi1i1ii1 % I11i
def IIi1IIIi ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , iconimage , iII1111III1I , O0OoooO0 , name in IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    oOO0OO0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
    for oOOOoo00 in oOO0OO0O :
     if oOOOoo00 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    o00o0o000Oo ( name , url , 1016 , iconimage , O0OoooO0 , iII1111III1I )
   else :
    if 'youtube' in url :
     oOO0OO0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for oOOOoo00 in oOO0OO0O :
      if oOOOoo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IiI1IiI1iiI1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , O0OoooO0 , iII1111III1I )
    else :
     oOO0OO0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
     for oOOOoo00 in oOO0OO0O :
      if oOOOoo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     IiI1IiI1iiI1 ( name , url , 222 , iconimage , O0OoooO0 , iII1111III1I )
     i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
  else :
   i1IiI1iiIII1 ( url , iconimage , name )
   if 68 - 68: Ii . IIiIi1iI % iiII11i1I1IIi
 else :
  IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
  for url , oOOoo , name in IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     iII1iii ( name , url , 1016 , oOOoo )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      i11i1iiiII ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , oOOoo )
     else :
      oOO0OO0O = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( o00OO00OoO ) )
      for oOOOoo00 in oOO0OO0O :
       if oOOOoo00 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      i11i1iiiII ( name , url , 222 , oOOoo )
      i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
   else :
    i1IiI1iiIII1 ( url , oOOoo , name )
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 47 - 47: OOooOOo . ooOoO0O00
def i1IiI1iiIII1 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 iiooo0o0oO = ( url ) . replace ( Ii11iIi1iIiii , 'http' ) . replace ( Ii1i1 , '.com' ) ;
 IIIIiiii = ( iiooo0o0oO ) . replace ( iIIIi , 'a' ) . replace ( oOoOOOOO , 'b' ) . replace ( ii1IIii , 'c' ) . replace ( I1i11i1II , 'd' ) . replace ( IIIiIII1 , 'e' ) . replace ( i11111i1I1IiI , 'f' ) ;
 IiI11IiII1iI = ( IIIIiiii ) . replace ( Oo0OOooO00OO , 'g' ) . replace ( oO00O0oO , 'h' ) . replace ( iiiIiIIiIiiii , 'i' ) . replace ( iii1II11II1 , 'j' ) . replace ( Ii1111Ii1 , 'k' ) . replace ( III1Iiii1i11 , 'l' ) ;
 OOo0OOooO0 = ( IiI11IiII1iI ) . replace ( oOoooOOO0 , 'm' ) . replace ( I1Iiii1i1iI , 'n' ) . replace ( O000O , 'o' ) . replace ( OOoO00OOo , 'p' ) . replace ( iiiiiiii , 'q' ) . replace ( OOO00Oo00o , 'r' ) ;
 IiII1Iiii = ( OOo0OOooO0 ) . replace ( I1o000o00OO00Oo , 's' ) . replace ( OOoOo0oOooo , 't' ) . replace ( I1II11I11111i , 'u' ) . replace ( I1II1II , 'v' ) . replace ( oooOi1IiIiIii11I , 'w' ) . replace ( O0o0O00 , 'x' ) ;
 OoI11II = ( IiII1Iiii ) . replace ( Iii11IiIi , 'y' ) . replace ( OOOoO000oOOo , 'z' ) . replace ( oOOoO0iiIii1iii , '.' ) . replace ( OO0O0Ooo0 , '(' ) . replace ( OOo0OOo , ')' ) . replace ( OOIiI1IIIiI1I1i , '/' ) ;
 IIiIiI11IIiII1iII = ( OoI11II ) . replace ( o0oOoo00 , '1' ) . replace ( OOo0o , '2' ) . replace ( OooO00OOOOoo , '3' ) . replace ( IIi1i , '4' ) . replace ( o0ooOOOo0O , '5' ) . replace ( o00O0OooO0 , '6' ) ;
 I11I1I111 = ( IIiIiI11IIiII1iII ) . replace ( Ii111i1I1i1i , '7' ) . replace ( o0o00o0Oo , '8' ) . replace ( O0OooO00ooOo0 , '9' ) . replace ( OoOOoO0Ooo0oo , '0' ) . replace ( ooOOOo0 , ':' ) . replace ( i11111 , '%' ) ;
 url = ( I11I1I111 ) . replace ( IiIii1i , '-' ) . replace ( O00O00 , '_' ) ;
 i11i1iiiII ( name , url , 222 , iconimage ) ;
 if 72 - 72: ooOoO0O00
 if 72 - 72: IIiIi1iI + IIiIiII11i . o0o00Oo0O - OooOO000 / ii . O00OOo00oo0o
def iiiiiiI ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOOoo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , iiOOooooO0Oo , 1007 , oOOoo )
def iI111iiI1II ( url ) :
 if 96 - 96: OOooOOo * o0o00Oo0O - IIiIiII11i . IIiIi1iI - iIi1i1ii1
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , oOOoo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , oOOoo )
  if 84 - 84: oo0oO00 * I11i * I11i - OooOO000
def III1Ii ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iiI1IIIi = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iiI1IIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiI1IIIi )
 if 90 - 90: oOo0O0Ooo
 if 27 - 27: iI11I1II1I1I - oo0oO00
def Ii1OOOo ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  if '-dir-' in iiI11ii1I1 :
   iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , oOo0OOoO0 )
  else :
   iII1iii ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , oOo0OOoO0 )
   if 73 - 73: IIi . I1ii11iIi11i + I1ii11iIi11i % I1ii11iIi11i % o0o00Oo0O
def I1OooO0oOoOoO ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IiiIIiiII = ( 'http://afewbitsmore.com/' )
 IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '[To Parent Directory]' in iiI11ii1I1 :
   iiI11ii1I1 = 'HOME'
   pass
  elif 'HOME' in iiI11ii1I1 :
   pass
  elif '.m3u' in iiI11ii1I1 :
   iII1iii ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , IiiIIiiII + url , 2002 , oOOOo00O00oOo + 'music.png' )
  elif '.mp3' in iiI11ii1I1 :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , IiiIIiiII + url , 222 , oOOOo00O00oOo + 'music.png' )
  elif '.m4a' in iiI11ii1I1 :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , IiiIIiiII + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , IiiIIiiII + url , 1012 , oOOOo00O00oOo + 'music.png' )
def OOOOo0oo0o ( url ) :
 I1 = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( I1 )
 for oOo0OOoO0 , iiI11ii1I1 , url in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 10012 , oOOOo00O00oOo + 'music.png' )
  if 43 - 43: oOo0O0Ooo % Ii1I * iIi1i1ii1
def i11i ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 IiiIIiiII = url
 IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  if '.mp3' in iiI11ii1I1 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , oOOOo00O00oOo + 'music.png' )
  else :
   iII1iii ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '/' , '' ) , IiiIIiiII + url , 1011 , oOOOo00O00oOo + 'music.png' )
def I1111i ( ) :
 OoO000O0Oo = i1i11I1I1iii1 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , oOo0OOoO0 , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , ( 'http://www.cyn.net/music/' + iiOOooooO0Oo ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOo0OOoO0 ) . replace ( ' ' , '%20' ) )
def IIIi11 ( url , img ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 ooo0O = url
 img = img
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( ooo0O + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 17 - 17: IIiIiII11i / IIiIi1iI
def iiiii11I1 ( url ) :
 OoO000O0Oo = i1i11I1I1iii1 ( url )
 ooo0O = url
 IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for type , url , iiI11ii1I1 in IIIII11I1IiI :
  if '[VID]' in type :
   i11i1iiiII ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , ooo0O + url , 222 , oOOOo00O00oOo + 'music.png' )
  if '[DIR]' in type :
   iiiii11I1 ( ooo0O + url )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: IIi * oO0o + iIi1i1ii1
 if 62 - 62: ii . o0o00Oo0O % I1ii11iIi11i
def I1iI1IiI ( ) :
 OO00 = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 o0oOOoOOO = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiI1i11II = o0oOOoOOO . lower ( )
 iiOOooooO0Oo = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 ooo0O = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 iIIIiIi1I1i = ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 if 98 - 98: I11i * I1ii11iIi11i - iIi1i1ii1 . IIiIi1iI
 I1 = OOoOO0oo0ooO ( iiOOooooO0Oo )
 iii1i1iiiiIi = OOoOO0oo0ooO ( ooo0O )
 Iiii = OOoOO0oo0ooO ( iIIIiIi1I1i )
 if 2 - 2: I1ii11iIi11i - IIiIi1iI % iI11I1II1I1I
 if I1 != 'Failed' :
  IIIII11I1IiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for iiI11ii1I1 in IIIII11I1IiI :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    iII1iii ( ( iiI11ii1I1 + ' source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iiOOooooO0Oo + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 88 - 88: O00OOo00oo0o - oO0o
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if iii1i1iiiiIi != 'Failed' :
  i1I = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( I1 )
  for iiI11ii1I1 in i1I :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    iII1iii ( ( iiI11ii1I1 + ' source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( ooo0O + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , '' )
    if 79 - 79: OooOO000
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
 if Iiii != 'Failed' :
  I1II1 = re . compile ( '<td><a href=".+?"><img src=".+?"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( Iiii )
  for iiI11ii1I1 in I1II1 :
   if o0oOOoOOO in iiI11ii1I1 . lower ( ) :
    iII1iii ( ( iiI11ii1I1 + ' source 3' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) , ( iIIIiIi1I1i + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1031 , '' )
    if 45 - 45: IIiIiII11i + OooOO000 . iiII11i1I1IIi . o0o00Oo0O * ooOoO0O00 - iIi1i1ii1
    i1Oo0oO00o ( 'tvshows' , 'Media Info 3' )
    if 48 - 48: Ii1I + I1ii11iIi11i
    if 76 - 76: Ii1I
    if 98 - 98: IIiIiII11i + oOo0O0Ooo - Ii1I . iIi1i1ii1
    if 51 - 51: iIi1i1ii1 + Ii * oO0o % I1ii11iIi11i / oOo0O0Ooo - iI11I1II1I1I
    if 20 - 20: O00OOo00oo0o . iiII11i1I1IIi . iIi1i1ii1 + iiII11i1I1IIi - IIi * oo0oO00
    if 82 - 82: oO0o
oOoooOOO0 = '{SF},' ; I1Iiii1i1iI = '{IF},' ; O000O = '{PW},' ; OooO00OOOOoo = '{AM},' ; OOoO00OOo = '{GF},' ; iiiiiiii = '{DD},' ; OOO00Oo00o = '{UO},' ; I1o000o00OO00Oo = '{LE},' ; I1II11I11111i = '{ZY},' ; I1II1II = '{UE},' ; oooOi1IiIiIii11I = '{PE},' ; O0o0O00 = '{JE},' ; Iii11IiIi = '{TH},' ; OOOoO000oOOo = '{LK},'
if 78 - 78: IIiIiII11i / iiII11i1I1IIi - Ii + Ii1I * I1ii11iIi11i
if 17 - 17: OOooOOo
def Oo0 ( ) :
 OoO000O0Oo = O000oo ( 'http://www.iwatchseries.me/tv-list/' )
 IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , iiOOooooO0Oo , 8021 , oOOOo00O00oOo + 'iwatch.png' )
def O0oooO ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , iI1IIi11i1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 + iI1IIi11i1I1 , url , 8022 , oOOOo00O00oOo + 'iwatch.png' )
def Ii1IiIi11i1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  OO0OOo00Oo ( url )
def OO0OOo00Oo ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( 'VidSpot - ' + iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for url in i1I :
  i11i1iiiII ( 'VodLocker' , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
 for iiI11ii1I1 , url in I1II1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   i11i1iiiII ( 'TheVideo - ' + iiI11ii1I1 , url , 222 , oOOOo00O00oOo + 'iwatch.png' )
   if 26 - 26: IIiIiII11i * OooOO000 + I11i / o0o00Oo0O + ooOoO0O00 - iiII11i1I1IIi
def o000oOoOOO ( ) :
 OoO000O0Oo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , iiOOooooO0Oo , 1021 , oOOOo00O00oOo + 'anime.png' )
  if 88 - 88: Ii1I % Ii1I + ii - IIi * o0o00Oo0O
  if 100 - 100: iI11I1II1I1I - OOooOOo
def iIiI1Iii11II ( ) :
 OoO000O0Oo = O000oo ( 'http://www.animetoon.org/cartoon' )
 IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for iiOOooooO0Oo , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , iiOOooooO0Oo , 1002 , oOOOo00O00oOo + 'anime.png' )
  if 17 - 17: iI11I1II1I1I - IIiIi1iI
  if 99 - 99: I1ii11iIi11i + O00OOo00oo0o % IIiIi1iI - I11i
  if 52 - 52: Ii1I
def o0oI1 ( url ) :
 OoO000O0Oo = O000oo ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 in i1I :
  OoOoO0ooooO0 = oOo0OOoO0
 I1II1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1II1 :
  iII1iii ( 'NEXT PAGE' , url , 1002 , oOOOo00O00oOo + 'Next.png' )
 IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in IIIII11I1IiI :
  iII1iii ( iiI11ii1I1 , url , 1003 , OoOoO0ooooO0 )
 xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def i1IO0OOoooO ( url , IMAGE ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in IIIII11I1IiI :
  print iiI11ii1I1 + '     ' + url
  if 'easy' in url :
   ooO0OOoOoOO00 ( url )
  elif 'playpanda' in url :
   ooO0OOoOoOO00 ( url )
   if 65 - 65: OOoOoo / Ii1I
  xbmcplugin . addSortMethod ( I1IIiiIiii , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooO0OOoOoOO00 ( url ) :
 OoO000O0Oo = O000oo ( url )
 IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in IIIII11I1IiI :
  i11i1iiiII ( 'STREAM' , url , 222 , oOOOo00O00oOo + 'anime.png' )
  if 84 - 84: ii . Ii % oO0o * I1ii11iIi11i / OooOO000
  if 95 - 95: oO0o - Ii . oO0o % IIi * o0o00Oo0O + Ii
def Ooo00 ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O0o0O00Oo0o0 . add_header ( 'referer' , url )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 23 - 23: I11i % iI11I1II1I1I
def i1i11I1I1iii1 ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 62 - 62: iIi1i1ii1 - I11i + iIi1i1ii1 . oO0o % IIiIiII11i - iI11I1II1I1I
def OoO0OOOOO ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 OooIIi111 = ( '%s%s' % ( oO0o0o0O , url ) )
 i1Oo00 = i1i11I1I1iii1 ( url )
 IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1Oo00 )
 for url , oOOoo , iiI11ii1I1 in IIIII11I1IiI :
  i11i1iiiII ( '%s' % ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , oOOoo )
  if 12 - 12: oo0oO00 % o0o00Oo0O % OooOO000 . oO0o
def I1iIi1i1 ( url ) :
 import urlresolver
 try :
  oOO0oo0Oo00O = urlresolver . resolve ( url )
  xbmc . Player ( ) . play ( oOO0oo0Oo00O , xbmcgui . ListItem ( iiI11ii1I1 ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( iiI11ii1I1 ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def II1IIIii ( url ) :
 if 14 - 14: OOooOOo
 o00o = open ( oOOoo0Oo , "a" )
 o00o . write ( 'url="' + url + '"\n' )
 o00o . close
 if 34 - 34: OOooOOo * OOooOOo
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 try : oO0O . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iiI11ii1I1 ) )
 oO0O = xbmc . Player ( oOO ( ) )
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
def OoOo0OoOO0Ooo ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  iIi11I11 = '.mp4'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   II1IIIii ( url )
  if iI1i11iII111 == 1 :
   oO000o0oo ( url , name , iIi11I11 )
 elif '.mkv' in url :
  iIi11I11 = '.mkv'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   II1IIIii ( url )
  if iI1i11iII111 == 1 :
   oO000o0oo ( url , name , iIi11I11 )
 elif '.mp3' in url :
  iIi11I11 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   II1IIIii ( url )
  if iI1i11iII111 == 1 :
   oO000o0oo ( url , name , iIi11I11 )
 elif '.avi' in url :
  iIi11I11 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   II1IIIii ( url )
  if iI1i11iII111 == 1 :
   oO000o0oo ( url , name , iIi11I11 )
 elif '.mov' in url :
  iIi11I11 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   II1IIIii ( url )
  if iI1i11iII111 == 1 :
   oO000o0oo ( url , name , iIi11I11 )
 elif '.mpeg' in url :
  iIi11I11 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   II1IIIii ( url )
  if iI1i11iII111 == 1 :
   oO000o0oo ( url , name , iIi11I11 )
 elif '.mpg' in url :
  iIi11I11 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   II1IIIii ( url )
  if iI1i11iII111 == 1 :
   oO000o0oo ( url , name , iIi11I11 )
 elif '.flv' in url :
  iIi11I11 = '.mp3'
  OooOoOO0 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI1i11iII111 = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , OooOoOO0 )
  if iI1i11iII111 == 0 :
   II1IIIii ( url )
  if iI1i11iII111 == 1 :
   oO000o0oo ( url , name , iIi11I11 )
 else :
  II1IIIii ( url )
def oO000o0oo ( url , name , cat ) :
 oO0o0I1I ( )
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
def oO0o0I1I ( ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def O0i1I1Iii1IiiIi ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iiI11ii1I1 )
 xbmc . sleep ( 1 )
 oO0O = xbmc . Player ( oOO ( ) )
 o0oOoO00o . update ( 100 , '%s' % iiI11ii1I1 )
 xbmc . sleep ( 1 )
 oO0O . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 73 - 73: o0o00Oo0O . O00OOo00oo0o - ii % iiII11i1I1IIi % ooOoO0O00
def iii1 ( url ) :
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oO0O . play ( url ) . strip ( )
 except : pass
 if 14 - 14: O00OOo00oo0o + iIi1i1ii1 * I1ii11iIi11i
def iI11iI ( url ) :
 oO0O = xbmc . Player ( oOO ( ) )
 import urlresolver
 O0o0ooo00o00 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 oO0O . play ( O0o0ooo00o00 )
 xbmc . sleep ( 1 )
 oO0O . play ( url )
 if 6 - 6: Ii / oO0o . Ii / IIiIi1iI
 if 26 - 26: o0o00Oo0O * iIi1i1ii1 - oOo0O0Ooo - OooOO000 / iI11I1II1I1I
def oOO ( ) :
 try :
  oO0Ooo00O = getSet ( "core-player" )
  if ( oO0Ooo00O == 'DVDPLAYER' ) : OOoO00o00oo = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( oO0Ooo00O == 'MPLAYER' ) : OOoO00o00oo = xbmc . PLAYER_CORE_MPLAYER
  elif ( oO0Ooo00O == 'PAPLAYER' ) : OOoO00o00oo = xbmc . PLAYER_CORE_PAPLAYER
  else : OOoO00o00oo = xbmc . PLAYER_CORE_AUTO
 except : OOoO00o00oo = xbmc . PLAYER_CORE_AUTO
 return OOoO00o00oo
 return True
 if 5 - 5: oo0oO00 - ii / OOooOOo
def iII1iii ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 ii1ii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OoOoo0oO = True
 iioo0o0OoOOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iioo0o0OoOOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooO0oO00O0o = [ ]
  ooO0oO00O0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooO0oO00O0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooO0oO00O0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iioo0o0OoOOO . addContextMenuItems ( ooO0oO00O0o )
 OoOoo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1ii11 , listitem = iioo0o0OoOOO , isFolder = True )
 return OoOoo0oO
 if 30 - 30: iiII11i1I1IIi % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
def o0OO0oooo ( name , url , mode , iconimage , fanart , description ) :
 if 55 - 55: oO0o
 ii1ii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOoo0oO = True
 iioo0o0OoOOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iioo0o0OoOOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iioo0o0OoOOO . setProperty ( "Fanart_Image" , fanart )
 OoOoo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1ii11 , listitem = iioo0o0OoOOO , isFolder = True )
 return OoOoo0oO
 if 20 - 20: IIiIi1iI * O00OOo00oo0o * I11i - IIiIi1iI
def i11i1iiiII ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 ii1ii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OoOoo0oO = True
 iioo0o0OoOOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iioo0o0OoOOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  ooO0oO00O0o = [ ]
  ooO0oO00O0o . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   ooO0oO00O0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooO0oO00O0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  iioo0o0OoOOO . addContextMenuItems ( ooO0oO00O0o )
 OoOoo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1ii11 , listitem = iioo0o0OoOOO , isFolder = False )
 return OoOoo0oO
 if 32 - 32: iIi1i1ii1 * oo0oO00
 if 85 - 85: Ii . oO0o + oO0o
 if 28 - 28: I1ii11iIi11i
 if 62 - 62: I1ii11iIi11i + ii / OooOO000
 if 60 - 60: iIi1i1ii1 / OOooOOo . iiII11i1I1IIi % IIi
 if 61 - 61: o0o00Oo0O . iIi1i1ii1 . o0o00Oo0O * Ii * IIiIiII11i / O00OOo00oo0o
def iiIiI1i1 ( heading , announce ) :
 class ooo0Oo000o ( ) :
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
   try : OOoO = open ( announce ) ; IIiiiiIiI1III = OOoO . read ( )
   except : IIiiiiIiI1III = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IIiiiiIiI1III ) )
   return
 ooo0Oo000o ( )
 ooo0Oo000o ( )
 if 18 - 18: o0o00Oo0O
def OO0Oooo0oOO0O ( ) :
 iiIiI1i1 ( 'GenieTv recomended sources for Kodi' , '[COLORwhite]http://genietv.com/repo[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR]' )
 if 14 - 14: iIi1i1ii1 / OOoOoo - o0o00Oo0O
 if 16 - 16: O00OOo00oo0o % iI11I1II1I1I . ooOoO0O00
 if 72 - 72: IIiIi1iI * IIi
 if 69 - 69: oo0oO00 - Ii
 if 29 - 29: iIi1i1ii1 + OooOO000 % Ii1I + iiII11i1I1IIi * I1ii11iIi11i - Ii
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 24 - 24: Ii . IIiIi1iI + IIiIi1iI - Ii % IIi
 if 58 - 58: oOo0O0Ooo
 if 94 - 94: I11i + iIi1i1ii1 % I11i . O00OOo00oo0o - IIiIi1iI * oOo0O0Ooo
 if 62 - 62: I1ii11iIi11i * ooOoO0O00 % Ii1I + I1ii11iIi11i . o0o00Oo0O . IIiIi1iI
 if 57 - 57: I1ii11iIi11i - O00OOo00oo0o + o0o00Oo0O % I11i
 if 72 - 72: IIi . OOooOOo / IIiIiII11i
 if 69 - 69: IIi * IIiIiII11i - IIiIi1iI - ooOoO0O00 + Ii
 if 50 - 50: ii * ooOoO0O00 / oo0oO00
 if 83 - 83: ooOoO0O00
 if 38 - 38: ii * iI11I1II1I1I
 if 54 - 54: ii . O00OOo00oo0o
 if 71 - 71: iIi1i1ii1
 if 31 - 31: iiII11i1I1IIi . Ii . oO0o * I1ii11iIi11i % iIi1i1ii1 . I11i
 if 92 - 92: ii / o0o00Oo0O * ooOoO0O00 + iI11I1II1I1I
 if 93 - 93: IIiIi1iI % O00OOo00oo0o
 if 46 - 46: Ii1I * OOooOOo * OOoOoo * Ii1I . Ii1I
 if 43 - 43: IIiIi1iI . ooOoO0O00
 if 68 - 68: OOoOoo % I1ii11iIi11i . o0o00Oo0O - OOooOOo + Ii1I . Ii
 if 45 - 45: oOo0O0Ooo
 if 17 - 17: ii - IIiIi1iI + iIi1i1ii1 . ii % I1ii11iIi11i
 if 92 - 92: O00OOo00oo0o - IIi % oO0o - I11i % ooOoO0O00
 if 38 - 38: Ii1I . iiII11i1I1IIi / OOooOOo % iiII11i1I1IIi
 if 10 - 10: o0o00Oo0O . oOo0O0Ooo * I11i / OooOO000
 if 61 - 61: I1ii11iIi11i - O00OOo00oo0o
def O0o0oooOo0oo ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + OO0oOooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 49 - 49: iI11I1II1I1I / iiII11i1I1IIi
def o0OOooo ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + ooIii1I1i1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 5 - 5: o0o00Oo0O . Ii + ii / OooOO000 % oOo0O0Ooo
def oOO0oOooooO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + I1III1i1Ii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 79 - 79: iiII11i1I1IIi * OooOO000
def iI1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + iIIII11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 91 - 91: OOoOoo % iiII11i1I1IIi + O00OOo00oo0o
def IIii1i ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o00OooO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 1 - 1: OOooOOo + ii . OOoOoo . iI11I1II1I1I
def iIi1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + Iii11I1II1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 96 - 96: O00OOo00oo0o % ooOoO0O00 . OooOO000 / o0o00Oo0O
def OoOoo ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + O0oOoOooo00oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 84 - 84: oO0o - iiII11i1I1IIi + OOooOOo + O00OOo00oo0o % IIiIiII11i - oOo0O0Ooo
def I1i11I1IiII1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + II1iiiiII ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 54 - 54: O00OOo00oo0o - O00OOo00oo0o * o0o00Oo0O / iIi1i1ii1 + oOo0O0Ooo - O00OOo00oo0o
def oo0oO0oO00oO ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o0OOo000ooo0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 42 , O00Ooo , O0OoooO0 , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 57 - 57: ooOoO0O00 % IIiIi1iI
def iI1Ii11iIiI1 ( url ) :
 i1Oo00 = O000oo ( str ( ooOO0O0ooOooO ) + o0o000oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1Oo00 )
 for iiI11ii1I1 , url , O00Ooo , O0OoooO0 , i11iiiiI1i in IIIII11I1IiI :
  I1IIII1i ( iiI11ii1I1 , url , 5 , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , oOOOo00O00oOo + 'GenieTVRSSFeed.png' , i11iiiiI1i )
 i1Oo0oO00o ( 'movies' , 'MAIN' )
 if 37 - 37: O00OOo00oo0o . ii / IIiIi1iI + IIiIiII11i
 if 90 - 90: iIi1i1ii1 * OooOO000 / IIi
 if 68 - 68: OOooOOo
 if 65 - 65: oo0oO00
 if 82 - 82: I11i
 if 80 - 80: ooOoO0O00 % OOooOOo + oO0o - ii / iI11I1II1I1I + O00OOo00oo0o
 if 65 - 65: iIi1i1ii1
 if 71 - 71: O00OOo00oo0o % O00OOo00oo0o . oo0oO00 + Ii - Ii
 if 16 - 16: iI11I1II1I1I / oOo0O0Ooo / O00OOo00oo0o - Ii . IIiIi1iI / IIi
def Ooo0Oo0o ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for Ooi1IIii11i1I1 , Ii1iiII1i , oO00O in os . walk ( iIi1ii1I1 ) :
     IIIi11iiIIi = 0
     IIIi11iiIIi += len ( oO00O )
     if IIIi11iiIIi > 0 :
      for OOoO in oO00O :
       os . unlink ( os . path . join ( Ooi1IIii11i1I1 , OOoO ) )
  oOo000O00O = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( oOo000O00O )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 90 - 90: ooOoO0O00 / oo0oO00 / oO0o % IIi
 if 20 - 20: Ii - OOooOOo + OOoOoo % OooOO000
 if 79 - 79: oO0o / I11i
 if 98 - 98: Ii . Ii * ii
 if 61 - 61: I11i . OOoOoo . o0o00Oo0O + ii + o0o00Oo0O
 if 65 - 65: ooOoO0O00 * IIi * ii - OOoOoo . OooOO000 - oO0o
 if 71 - 71: iIi1i1ii1 * OOooOOo
 if 33 - 33: ooOoO0O00 . ooOoO0O00 * ii % O00OOo00oo0o * I11i
def OOOOO0o0OOo ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 64 - 64: IIiIi1iI / IIiIi1iI + Ii1I * IIi % IIi
def o00o0 ( url ) :
 oOO0O0oO0o00O = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 oOo0OooOo = [
 ( oOO0O0oO0o00O ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( oOO0O0oO0o00O , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oOO0O0oO0o00O , 'plugin.video.itv' , 'Images' ) ) ]
 if 86 - 86: IIi % Ii / ooOoO0O00 - oO0o + iIi1i1ii1 . IIi
 IIi11ii = 0
 if 57 - 57: IIi * oO0o + o0o00Oo0O % O00OOo00oo0o - oOo0O0Ooo
 for oOOOoo00 in oOo0OooOo :
  if os . path . exists ( oOOOoo00 ) and not oOOOoo00 in [ oO0o0o0ooO0oO , oOO0O0oO0o00O ] :
   for Ooi1IIii11i1I1 , Ii1iiII1i , oO00O in os . walk ( oOOOoo00 ) :
    IIIi11iiIIi = 0
    IIIi11iiIIi += len ( oO00O )
    if IIIi11iiIIi > 0 :
     for OOoO in oO00O :
      if not OOoO in oooOOOOO :
       try :
        os . unlink ( os . path . join ( Ooi1IIii11i1I1 , OOoO ) )
       except :
        pass
      else : OOO ( 'Ignore Log File: %s' % OOoO )
     for I11i11I in Ii1iiII1i :
      try :
       shutil . rmtree ( os . path . join ( Ooi1IIii11i1I1 , I11i11I ) )
       IIi11ii += 1
       OOO ( "[Success] cleared %s files from %s" % ( str ( IIIi11iiIIi ) , os . path . join ( oOOOoo00 , I11i11I ) ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( oOOOoo00 , I11i11I ) )
  else :
   for Ooi1IIii11i1I1 , Ii1iiII1i , oO00O in os . walk ( oOOOoo00 ) :
    for I11i11I in Ii1iiII1i :
     if 'cache' in I11i11I . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( Ooi1IIii11i1I1 , I11i11I ) )
       IIi11ii += 1
       OOO ( "[Success] wiped %s " % os . path . join ( oOOOoo00 , I11i11I ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( oOOOoo00 , I11i11I ) )
       if 43 - 43: O00OOo00oo0o
 OOOOO0o0OOo ( oO , 'Clear Cache: Removed %s Files' % IIi11ii )
 if 10 - 10: ooOoO0O00 - I11i / ii + Ii + iI11I1II1I1I
 if 26 - 26: Ii . IIi - o0o00Oo0O
 if 73 - 73: oOo0O0Ooo
 if 95 - 95: oO0o % oO0o * oo0oO00 - oO0o
 if 57 - 57: ii / OOooOOo + oo0oO00 . iIi1i1ii1
 if 14 - 14: Ii % IIi * I11i * OOooOOo
 if 55 - 55: O00OOo00oo0o * IIi * O00OOo00oo0o
def I1III1i1I ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oo0i11Iiiiii11II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Ooi1IIii11i1I1 , Ii1iiII1i , oO00O in os . walk ( oo0i11Iiiiii11II ) :
   IIIi11iiIIi = 0
   IIIi11iiIIi += len ( oO00O )
   if 100 - 100: O00OOo00oo0o + iiII11i1I1IIi + oO0o . Ii1I
   if 40 - 40: oO0o - oO0o
   if IIIi11iiIIi > 0 :
    if 58 - 58: OOoOoo * OooOO000 . oOo0O0Ooo + IIi
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( IIIi11iiIIi ) + " files found" , "Do you want to delete them?" ) :
     if 4 - 4: oO0o . IIi + Ii + IIiIi1iI % oo0oO00 - IIiIi1iI
     for OOoO in oO00O :
      os . unlink ( os . path . join ( Ooi1IIii11i1I1 , OOoO ) )
     for I11i11I in Ii1iiII1i :
      shutil . rmtree ( os . path . join ( Ooi1IIii11i1I1 , I11i11I ) )
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
 if 45 - 45: oo0oO00
 if 66 - 66: IIi
 if 23 - 23: Ii1I % iiII11i1I1IIi
 if 18 - 18: ii . ooOoO0O00 + IIiIiII11i
 if 99 - 99: O00OOo00oo0o - Ii1I - oOo0O0Ooo - O00OOo00oo0o + oO0o + IIiIiII11i
 if 34 - 34: O00OOo00oo0o * iiII11i1I1IIi
 if 31 - 31: OOoOoo . oo0oO00
 if 40 - 40: iIi1i1ii1 - iiII11i1I1IIi / IIiIiII11i * ooOoO0O00 + OOoOoo * IIiIiII11i
 if 53 - 53: Ii1I - Ii . oO0o / OOooOOo - O00OOo00oo0o
def O0O0ooOOO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 oo0i11Iiiiii11II = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for Ooi1IIii11i1I1 , Ii1iiII1i , oO00O in os . walk ( oo0i11Iiiiii11II ) :
   IIIi11iiIIi = 0
   IIIi11iiIIi += len ( oO00O )
   if 99 - 99: iIi1i1ii1 - OOoOoo - ooOoO0O00 / Ii . OOoOoo
   if 58 - 58: IIi
   if IIIi11iiIIi > 0 :
    if 12 - 12: oOo0O0Ooo . I11i * ii
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( IIIi11iiIIi ) + " files found" , "Do you want to delete them?" ) :
     if 64 - 64: OOooOOo + OOoOoo - ooOoO0O00 . IIiIiII11i . oO0o
     for OOoO in oO00O :
      os . unlink ( os . path . join ( Ooi1IIii11i1I1 , OOoO ) )
     for I11i11I in Ii1iiII1i :
      shutil . rmtree ( os . path . join ( Ooi1IIii11i1I1 , I11i11I ) )
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
 if 31 - 31: oo0oO00 . OooOO000 - iiII11i1I1IIi . iI11I1II1I1I + iiII11i1I1IIi . OOooOOo
 if 86 - 86: Ii1I - Ii1I / OooOO000 - Ii1I * OooOO000 + O00OOo00oo0o
 if 61 - 61: I1ii11iIi11i / IIiIiII11i / I1ii11iIi11i / ooOoO0O00 . I1ii11iIi11i - OOoOoo
 if 30 - 30: ii % IIi
 if 14 - 14: OOooOOo / oO0o / Ii - OOooOOo / I11i - IIi
 if 81 - 81: OooOO000 % iIi1i1ii1 . IIiIi1iI
 if 66 - 66: Ii1I * iIi1i1ii1 / ii * o0o00Oo0O % IIi
 if 49 - 49: IIiIiII11i . oOo0O0Ooo * o0o00Oo0O * iIi1i1ii1 / O00OOo00oo0o * ii
 if 82 - 82: I1ii11iIi11i / iIi1i1ii1 / iIi1i1ii1 % iIi1i1ii1
 if 20 - 20: IIiIi1iI
def ooOooooOo00OO0o ( url , name ) :
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oO0o0oo = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 iiiI11iii11iI = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml.bak' )
 if os . path . exists ( iiiI11iii11iI ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   oO0o0oo = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
   try :
    os . remove ( oO0o0oo )
    print '=== GenieTv - REMOVING    ' + str ( oO0o0oo ) + '    ==='
   except :
    pass
   i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
   OoOoO0O = open ( oO0o0oo , "w" )
   OoOoO0O . write ( i1Oo00 )
   OoOoO0O . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( oO0o0oo ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  oO0o0oo = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
  try :
   os . remove ( oO0o0oo )
   print '=== GenieTv - REMOVING    ' + str ( oO0o0oo ) + '    ==='
  except :
   pass
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  OoOoO0O = open ( oO0o0oo , "w" )
  OoOoO0O . write ( i1Oo00 )
  OoOoO0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oO0o0oo ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 46 - 46: OooOO000 % O00OOo00oo0o % OOooOOo . ii . IIiIiII11i % OOoOoo
def I1i1I1i1I1 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oO0o0oo = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
 try :
  OoOoO0O = open ( oO0o0oo ) . read ( )
  if 'zero' in OoOoO0O :
   name = '0CACHE'
  elif 'tuxen' in OoOoO0O :
   name = 'TUXENS'
  elif 'muckys' in OoOoO0O :
   name = 'MUCKYS'
  elif 'p2p1' in OoOoO0O :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in OoOoO0O :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in OoOoO0O :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 33 - 33: iIi1i1ii1 . oo0oO00
def OOOo0OO0ooO0O0O ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 oO0o0oo = os . path . join ( oOO0O00Oo0O0o , 'advancedsettings.xml' )
 try :
  os . remove ( oO0o0oo )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( oO0o0oo ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 76 - 76: I11i / iiII11i1I1IIi
 if 95 - 95: OOooOOo - o0o00Oo0O % ii
 if 13 - 13: Ii
 if 54 - 54: IIi . Ii1I * iiII11i1I1IIi % O00OOo00oo0o . o0o00Oo0O * OOoOoo
 if 87 - 87: iIi1i1ii1 % Ii1I * I1ii11iIi11i
 if 59 - 59: I1ii11iIi11i / iiII11i1I1IIi - iI11I1II1I1I * iI11I1II1I1I
 if 18 - 18: iiII11i1I1IIi * Ii1I / Ii / iI11I1II1I1I * ii . IIi
 if 69 - 69: I1ii11iIi11i * IIiIi1iI
 if 91 - 91: I11i . IIiIi1iI / oO0o / Ii * I11i
 if 52 - 52: oOo0O0Ooo - Ii / OOoOoo . oo0oO00
def OOOOO0 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for II1i1I , OOo0Oo , iI1iIiI1Ii1iI , OooOooo00OOO0o in IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % II1i1I , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iI1iIiI1Ii1iI , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OooOooo00OOO0o )
  inc = inc + 1
  if 41 - 41: IIi % Ii * oOo0O0Ooo + I11i / oo0oO00
  if 56 - 56: ooOoO0O00
  if 11 - 11: Ii % I11i / iiII11i1I1IIi * ii
  if 82 - 82: OOoOoo
  if 10 - 10: I1ii11iIi11i % IIi / iiII11i1I1IIi * OOoOoo - I11i
  if 54 - 54: Ii / iI11I1II1I1I % Ii1I / oOo0O0Ooo . iI11I1II1I1I / OooOO000
  if 1 - 1: O00OOo00oo0o / OOooOOo * OOooOOo - I11i % iIi1i1ii1
  if 96 - 96: OOoOoo / iIi1i1ii1 % oO0o . iI11I1II1I1I
  if 30 - 30: iiII11i1I1IIi - oO0o
def iiii ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oO0o0oo = os . path . join ( oOO0O00Oo0O0o , 'addons2.ini' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  OoOoO0O = open ( oO0o0oo , "w" )
  OoOoO0O . write ( i1Oo00 )
  OoOoO0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oO0o0oo ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 62 - 62: iI11I1II1I1I % O00OOo00oo0o % Ii1I * OOoOoo
def oO0OO0o0oo0o ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  oOO0O00Oo0O0o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  oO0o0oo = os . path . join ( oOO0O00Oo0O0o , 'settings.xml' )
  i1Oo00 = iI111I11I1I1 . http_GET ( url ) . content
  OoOoO0O = open ( oO0o0oo , "w" )
  OoOoO0O . write ( i1Oo00 )
  OoOoO0O . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( oO0o0oo ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 55 - 55: OOoOoo
 if 43 - 43: IIi
def i1OO0o ( ) :
 try :
  ooOoOoO0o00o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( ooOoOoO0o00o ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    I1111iI = os . path . join ( ooOoOoO0o00o , "source.db" )
    os . unlink ( I1111iI )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 89 - 89: OOoOoo - OOoOoo % OooOO000 / iiII11i1I1IIi + oo0oO00 - OOoOoo
 if 97 - 97: iIi1i1ii1 % OOooOOo / Ii1I / iI11I1II1I1I * ii * IIi
 if 80 - 80: oo0oO00 / o0o00Oo0O
 if 55 - 55: oOo0O0Ooo * iiII11i1I1IIi / o0o00Oo0O % OOooOOo
 if 71 - 71: Ii * OOooOOo * IIi + oo0oO00 + I1ii11iIi11i
def O000oo ( url ) :
 O0o0O00Oo0o0 = urllib2 . Request ( url )
 O0o0O00Oo0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 O00O0oOO00O00 = urllib2 . urlopen ( O0o0O00Oo0o0 )
 i1Oo00 = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 return i1Oo00
 if 59 - 59: OOoOoo
 if 54 - 54: IIi
 if 27 - 27: OOooOOo - oO0o + I11i + IIiIi1iI . oO0o
 if 86 - 86: IIiIiII11i - ii - IIiIi1iI % OooOO000
 if 16 - 16: IIiIi1iI + I1ii11iIi11i + ii
 if 87 - 87: oOo0O0Ooo . oo0oO00 / OOoOoo - ii
 if 33 - 33: oo0oO00 % oO0o . iI11I1II1I1I / OOoOoo
def IiIIi1 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; i1II1iI = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if i1II1iI :
  oOOo0oOO = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; oOOo0oOO = xbmc . translatePath ( oOOo0oOO ) ;
  oOOoOoO0OOO0oO = os . path . join ( oOOo0oOO , ".." , ".." ) ; oOOoOoO0OOO0oO = os . path . abspath ( oOOoOoO0OOO0oO ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + oOOoOoO0OOO0oO ) ; Oo0oO = False
  try :
   for Ooi1IIii11i1I1 , Ii1iiII1i , oO00O in os . walk ( oOOoOoO0OOO0oO , topdown = True ) :
    Ii1iiII1i [ : ] = [ I11i11I for I11i11I in Ii1iiII1i if I11i11I not in o0oO0 ]
    for iiI11ii1I1 in oO00O :
     try : os . remove ( os . path . join ( Ooi1IIii11i1I1 , iiI11ii1I1 ) )
     except :
      if iiI11ii1I1 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : Oo0oO = True
      plugintools . log ( "Error removing " + Ooi1IIii11i1I1 + " " + iiI11ii1I1 )
    for iiI11ii1I1 in Ii1iiII1i :
     try : os . rmdir ( os . path . join ( Ooi1IIii11i1I1 , iiI11ii1I1 ) )
     except :
      if iiI11ii1I1 not in [ "Database" , "userdata" ] : Oo0oO = True
      plugintools . log ( "Error removing " + Ooi1IIii11i1I1 + " " + iiI11ii1I1 )
   if not Oo0oO : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 OoiI1I1 ( )
 if 81 - 81: ii / IIiIi1iI * iI11I1II1I1I . I1ii11iIi11i + oo0oO00 / o0o00Oo0O
 if 84 - 84: IIiIiII11i - I11i
 if 78 - 78: OOoOoo
def ooO0OoOO0 ( ) :
 o0oo00 = [ ]
 o000IIIi1IiI1iII = sys . argv [ 2 ]
 if len ( o000IIIi1IiI1iII ) >= 2 :
  IIIIiii1IIii = sys . argv [ 2 ]
  OOOO0oo = IIIIiii1IIii . replace ( '?' , '' )
  if ( IIIIiii1IIii [ len ( IIIIiii1IIii ) - 1 ] == '/' ) :
   IIIIiii1IIii = IIIIiii1IIii [ 0 : len ( IIIIiii1IIii ) - 2 ]
  iii1I1ii1 = OOOO0oo . split ( '&' )
  o0oo00 = { }
  for I1Io0oO0oo in range ( len ( iii1I1ii1 ) ) :
   IIiII11Iiii1i1II = { }
   IIiII11Iiii1i1II = iii1I1ii1 [ I1Io0oO0oo ] . split ( '=' )
   if ( len ( IIiII11Iiii1i1II ) ) == 2 :
    o0oo00 [ IIiII11Iiii1i1II [ 0 ] ] = IIiII11Iiii1i1II [ 1 ]
    if 48 - 48: ii + O00OOo00oo0o
 return o0oo00
 if 19 - 19: ooOoO0O00 / IIi - Ii + OOooOOo
i1iIIii1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
Ii1I1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
i1ooo00o0OO0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
oO0OOOo0OO = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
i11i11II11i1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
i1IiI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
OO0oOooo = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
I1iI1i = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
ooIii1I1i1i1 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
I1III1i1Ii = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iIIII11 = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
o00OooO = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Iii11I1II1 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
O0oOoOooo00oo = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
II1iiiiII = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
o0OOo000ooo0o = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
O0OOO00 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iIIiiI1II = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
i1i11i = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
ii1O0ooooo000 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
iiO0o0O0oo0o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
I1II1Oo000o = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
o0o000oo = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
oO0o0o0O = base64 . decodestring ( 'Q1VOVA==' )
def I1IIII1i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 ii1ii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOoo0oO = True
 iioo0o0OoOOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iioo0o0OoOOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iioo0o0OoOOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooO0oO00O0o = [ ]
  if showcontext == 'fav' :
   ooO0oO00O0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooO0oO00O0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iioo0o0OoOOO . addContextMenuItems ( ooO0oO00O0o )
 OoOoo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1ii11 , listitem = iioo0o0OoOOO , isFolder = True )
 return OoOoo0oO
 if 15 - 15: iiII11i1I1IIi - iI11I1II1I1I % iIi1i1ii1
def I1I11i ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 ii1ii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OoOoo0oO = True
 iioo0o0OoOOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iioo0o0OoOOO . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 iioo0o0OoOOO . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  ooO0oO00O0o = [ ]
  if showcontext == 'fav' :
   ooO0oO00O0o . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in Oo0OoO00oOO0o :
   ooO0oO00O0o . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iioo0o0OoOOO . addContextMenuItems ( ooO0oO00O0o )
 OoOoo0oO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1ii11 , listitem = iioo0o0OoOOO , isFolder = False )
 return OoOoo0oO
 if 47 - 47: OooOO000 / ii - IIiIiII11i
 if 91 - 91: OOooOOo + I11i
IIIIiii1IIii = ooO0OoOO0 ( )
iiOOooooO0Oo = None
iiI11ii1I1 = None
o0ii1i = None
O00Ooo = None
O0OoooO0 = None
i11iiiiI1i = None
ii11I1IiIIi1i1IIi = None
oooOo = None
if 33 - 33: iiII11i1I1IIi * OooOO000 + iI11I1II1I1I - Ii1I
if 11 - 11: IIiIiII11i + OOooOOo * iiII11i1I1IIi
try :
 oooOo = int ( IIIIiii1IIii [ "fav_mode" ] )
except :
 pass
 if 45 - 45: OooOO000 . o0o00Oo0O - oOo0O0Ooo
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
 o0ii1i = int ( IIIIiii1IIii [ "mode" ] )
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
 if 21 - 21: Ii1I - oo0oO00 * oO0o
 if 98 - 98: Ii1I - IIi % iI11I1II1I1I
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( o0ii1i )
print "URL: " + str ( iiOOooooO0Oo )
print "Name: " + str ( iiI11ii1I1 )
print "IconImage: " + str ( O00Ooo )
if 54 - 54: Ii1I + ooOoO0O00 - iiII11i1I1IIi * ii
if 71 - 71: I11i + ii * IIiIiII11i / O00OOo00oo0o
def i1Oo0oO00o ( content , viewType ) :
 if 78 - 78: O00OOo00oo0o % IIi
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 73 - 73: Ii1I + OooOO000 * oOo0O0Ooo * iiII11i1I1IIi
if O00Ooo == None : O00Ooo = Oo00OOOOO
if O0OoooO0 == None : O0OoooO0 = O0o0Oo
if o0ii1i == None :
 o0o0o0oO0oOO ( )
 if 35 - 35: iiII11i1I1IIi * o0o00Oo0O * oO0o . Ii1I
elif o0ii1i == 1 :
 o0OOOOOo0 ( iiOOooooO0Oo )
 if 74 - 74: OooOO000 * OooOO000 * I11i / oo0oO00
elif o0ii1i == 44 :
 II1i11I ( iiOOooooO0Oo )
 if 91 - 91: Ii . Ii1I / IIiIiII11i
elif o0ii1i == 2 :
 i1IiiiiiIiII ( )
 if 97 - 97: iIi1i1ii1 % ooOoO0O00 % OOoOoo + I1ii11iIi11i - o0o00Oo0O - iiII11i1I1IIi
elif o0ii1i == 3 :
 I1iIIIiI ( )
 if 64 - 64: iIi1i1ii1 - OooOO000
elif o0ii1i == 21 :
 i1i1II ( )
 if 12 - 12: ooOoO0O00
elif o0ii1i == 4 :
 OOOoo ( )
 if 99 - 99: IIiIiII11i - Ii1I * OOoOoo
elif o0ii1i == 5 :
 oO0O0o0O ( iiOOooooO0Oo )
 if 3 - 3: OOoOoo - Ii1I * OooOO000 * Ii1I + I1ii11iIi11i
elif o0ii1i == 6 :
 I1III1i1I ( iiOOooooO0Oo )
 if 15 - 15: Ii1I * iIi1i1ii1 / OooOO000 . I11i / iIi1i1ii1 % OOooOOo
elif o0ii1i == 7 :
 ooOooooOo00OO0o ( iiOOooooO0Oo , iiI11ii1I1 )
 if 75 - 75: ii % Ii % iI11I1II1I1I % Ii1I / Ii
elif o0ii1i == 8 :
 I1i1I1i1I1 ( iiOOooooO0Oo , iiI11ii1I1 )
 if 96 - 96: IIiIi1iI * oo0oO00 / iI11I1II1I1I / iiII11i1I1IIi
elif o0ii1i == 9 :
 FIXREPOSADDONS ( iiOOooooO0Oo )
 if 5 - 5: I11i
elif o0ii1i == 10 :
 oOOo0O00o ( )
 if 83 - 83: iiII11i1I1IIi * oOo0O0Ooo . IIiIiII11i * ooOoO0O00 % o0o00Oo0O
elif o0ii1i == 11 :
 OOOo0OO0ooO0O0O ( iiOOooooO0Oo )
 if 35 - 35: OOooOOo % oO0o + o0o00Oo0O * I11i % Ii1I
elif o0ii1i == 12 :
 OOOOO0 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 57 - 57: oo0oO00 / iiII11i1I1IIi
elif o0ii1i == 13 :
 Ooo0Oo0o ( )
 if 63 - 63: IIiIi1iI * oO0o * IIiIi1iI + OOooOOo
elif o0ii1i == 14 :
 o00o0 ( iiOOooooO0Oo )
 if 25 - 25: OooOO000 * OOooOOo / oOo0O0Ooo / OOoOoo
elif o0ii1i == 15 :
 II1 ( )
 if 11 - 11: IIi + Ii
elif o0ii1i == 16 :
 iiii ( iiOOooooO0Oo , iiI11ii1I1 )
 if 14 - 14: OOooOOo / OOoOoo + oO0o - iIi1i1ii1
elif o0ii1i == 17 :
 oO0OO0o0oo0o ( iiOOooooO0Oo , iiI11ii1I1 )
 if 38 - 38: O00OOo00oo0o
elif o0ii1i == 18 :
 i1OO0o ( )
 if 30 - 30: IIiIiII11i + iiII11i1I1IIi . Ii + iI11I1II1I1I
elif o0ii1i == 19 :
 o00iIiiiII ( iiOOooooO0Oo )
 if 100 - 100: oo0oO00 * I11i / OooOO000
elif o0ii1i == 40 :
 i1o0oo0 ( iiI11ii1I1 , iiOOooooO0Oo , i11iiiiI1i )
 if 92 - 92: IIiIi1iI / Ii * IIi
elif o0ii1i == 42 :
 oOo0O ( iiI11ii1I1 , iiOOooooO0Oo , i11iiiiI1i )
 if 55 - 55: IIiIi1iI
elif o0ii1i == 43 :
 I1iII ( iiOOooooO0Oo )
 if 1 - 1: oO0o
elif o0ii1i == 20 :
 O0oO0o000o ( iiOOooooO0Oo )
 if 43 - 43: iI11I1II1I1I - IIi - I11i + Ii1I - O00OOo00oo0o % Ii1I
elif o0ii1i == 22 :
 O0o0oooOo0oo ( iiOOooooO0Oo )
 if 58 - 58: OOooOOo
elif o0ii1i == 23 :
 o0OOooo ( iiOOooooO0Oo )
 if 27 - 27: OOoOoo * IIi - ii . iIi1i1ii1 - IIiIiII11i
elif o0ii1i == 24 :
 oOO0oOooooO ( iiOOooooO0Oo )
 if 62 - 62: oOo0O0Ooo / iI11I1II1I1I * iiII11i1I1IIi
elif o0ii1i == 25 :
 iI1 ( iiOOooooO0Oo )
 if 84 - 84: OOoOoo - OOooOOo . OOoOoo + IIiIi1iI . OooOO000
elif o0ii1i == 26 :
 IIii1i ( iiOOooooO0Oo )
 if 96 - 96: iIi1i1ii1 % OooOO000 * iIi1i1ii1 % oOo0O0Ooo . I11i / I11i
elif o0ii1i == 27 :
 iIi1 ( iiOOooooO0Oo )
 if 7 - 7: oO0o - IIiIi1iI % ooOoO0O00
elif o0ii1i == 28 :
 OoOoo ( iiOOooooO0Oo )
 if 24 - 24: oO0o % o0o00Oo0O % iiII11i1I1IIi
elif o0ii1i == 29 :
 I1i11I1IiII1 ( iiOOooooO0Oo )
 if 61 - 61: IIiIi1iI . OooOO000 / IIiIi1iI * ii
elif o0ii1i == 30 :
 IiII1i1iI ( iiOOooooO0Oo )
 if 13 - 13: IIiIiII11i
elif o0ii1i == 31 :
 oo0oO0oO00oO ( iiOOooooO0Oo )
 if 17 - 17: IIiIiII11i
elif o0ii1i == 32 :
 oO0o0 ( )
 if 66 - 66: OOoOoo * oo0oO00
elif o0ii1i == 33 :
 oO0oOoo0O ( )
 if 73 - 73: Ii + o0o00Oo0O % o0o00Oo0O
elif o0ii1i == 35 :
 O00o0O ( iiOOooooO0Oo )
 if 70 - 70: IIiIiII11i * ii - iIi1i1ii1 + oo0oO00 * o0o00Oo0O
elif o0ii1i == 34 :
 II1iI11 ( iiOOooooO0Oo )
 if 49 - 49: oo0oO00 . iIi1i1ii1 . OOooOOo - Ii1I
elif o0ii1i == 36 :
 i1IoOOoooO0O0 ( iiOOooooO0Oo )
 if 74 - 74: IIiIi1iI % Ii1I * ooOoO0O00
elif o0ii1i == 37 :
 OoO00ooO ( iiOOooooO0Oo )
 if 18 - 18: OOooOOo
elif o0ii1i == 38 :
 o0oO0OO00oo0o ( iiOOooooO0Oo )
 if 30 - 30: IIiIiII11i
elif o0ii1i == 41 :
 IiIIi1 ( IIIIiii1IIii )
 if 27 - 27: ooOoO0O00 - iI11I1II1I1I + o0o00Oo0O % I1ii11iIi11i / IIi + ooOoO0O00
elif o0ii1i == 39 :
 iI1Ii11iIiI1 ( iiOOooooO0Oo )
 if 48 - 48: I1ii11iIi11i
elif o0ii1i == 45 :
 TEXTS ( )
 if 70 - 70: ii * Ii
elif o0ii1i == 46 :
 OO0Oooo0oOO0O ( )
 if 60 - 60: OOoOoo / iI11I1II1I1I + ii - Ii1I * Ii
elif o0ii1i == 47 :
 GEVID ( )
 if 47 - 47: o0o00Oo0O . oOo0O0Ooo / IIiIi1iI % Ii
elif o0ii1i == 48 :
 Ii1iiI1 ( iiI11ii1I1 , iiOOooooO0Oo , i11iiiiI1i )
 if 47 - 47: iIi1i1ii1 . OOooOOo . iI11I1II1I1I . I11i
elif o0ii1i == 49 :
 IiIi1I1 ( )
 if 39 - 39: I11i
elif o0ii1i == 22222 :
 II1IIIii ( iiOOooooO0Oo )
 if 89 - 89: ii + OooOO000 . O00OOo00oo0o / iIi1i1ii1
elif o0ii1i == 222 :
 I1iIi1i1 ( iiOOooooO0Oo )
 if 75 - 75: iI11I1II1I1I * OooOO000 / OOooOOo * IIiIiII11i . ooOoO0O00
elif o0ii1i == 222222 :
 OoOo0OoOO0Ooo ( iiOOooooO0Oo , iiI11ii1I1 )
 if 6 - 6: iIi1i1ii1 % iIi1i1ii1 / ii * oo0oO00 . oOo0O0Ooo . ooOoO0O00
elif o0ii1i == 333 :
 OoO0OOOOO ( iiOOooooO0Oo )
 if 59 - 59: iiII11i1I1IIi . iiII11i1I1IIi * oOo0O0Ooo - iIi1i1ii1 % OOooOOo
 if 19 - 19: ii / I1ii11iIi11i - O00OOo00oo0o . OOooOOo
elif o0ii1i == 1020 :
 o000oOoOOO ( )
 if 8 - 8: iiII11i1I1IIi % IIiIi1iI . iI11I1II1I1I
elif o0ii1i == 1021 :
 ANIMEEP ( )
 if 95 - 95: I11i + Ii . Ii1I . IIiIi1iI . I11i
elif o0ii1i == 1022 :
 ANIMEPLAY ( iiOOooooO0Oo )
 if 93 - 93: OooOO000
elif o0ii1i == 1001 :
 iIiI1Iii11II ( )
 if 55 - 55: IIiIiII11i % I11i - oO0o
elif o0ii1i == 1005 :
 iiiiiiI ( )
 if 48 - 48: IIiIi1iI * iI11I1II1I1I % OOooOOo
elif o0ii1i == 1007 :
 iI111iiI1II ( iiOOooooO0Oo )
 if 100 - 100: IIiIiII11i - Ii + oO0o % IIiIi1iI - iI11I1II1I1I * Ii
elif o0ii1i == 1010 :
 Ii1OOOo ( iiOOooooO0Oo )
 if 30 - 30: oO0o . oO0o . iIi1i1ii1 % iIi1i1ii1 * ooOoO0O00 * oo0oO00
elif o0ii1i == 1011 :
 i11i ( iiOOooooO0Oo )
 if 74 - 74: ii
elif o0ii1i == 1012 :
 I1OooO0oOoOoO ( iiOOooooO0Oo )
 if 33 - 33: I11i - IIiIiII11i
elif o0ii1i == 1030 :
 I1111i ( )
 if 95 - 95: ii
elif o0ii1i == 1031 :
 IIIi11 ( iiOOooooO0Oo , O00Ooo )
 if 23 - 23: IIiIiII11i + iiII11i1I1IIi / o0o00Oo0O . iiII11i1I1IIi . O00OOo00oo0o + iI11I1II1I1I
elif o0ii1i == 1032 :
 iiiii11I1 ( iiOOooooO0Oo )
 if 2 - 2: ooOoO0O00 . o0o00Oo0O / I11i . IIiIiII11i / oO0o % ooOoO0O00
elif o0ii1i == 1006 :
 Parse . ParseURL ( iiOOooooO0Oo )
 if 12 - 12: I11i
elif o0ii1i == 2030 :
 Parse . addonParseURL ( iiOOooooO0Oo )
 if 58 - 58: iI11I1II1I1I * iIi1i1ii1 . IIiIi1iI . I1ii11iIi11i * iIi1i1ii1
elif o0ii1i == 2031 :
 Parse . apkParseURL ( iiOOooooO0Oo )
 if 63 - 63: OOooOOo . iiII11i1I1IIi * I11i - iiII11i1I1IIi % iiII11i1I1IIi
elif o0ii1i == 1002 :
 o0oI1 ( iiOOooooO0Oo )
 if 62 - 62: iiII11i1I1IIi - IIiIi1iI / IIiIi1iI
elif o0ii1i == 1003 :
 i1IO0OOoooO ( iiOOooooO0Oo , O00Ooo )
 if 95 - 95: OOooOOo - ooOoO0O00 / O00OOo00oo0o . IIiIi1iI % IIi - ooOoO0O00
elif o0ii1i == 1004 :
 ooO0OOoOoOO00 ( iiOOooooO0Oo )
 if 12 - 12: OooOO000
elif o0ii1i == 1008 :
 i1oOOOoOO ( )
 if 96 - 96: o0o00Oo0O
elif o0ii1i == 1009 :
 OOoOooO0o ( iiOOooooO0Oo )
 if 89 - 89: Ii1I - I1ii11iIi11i
elif o0ii1i == 2001 :
 iIIII11iII ( )
 if 26 - 26: IIiIi1iI % IIiIi1iI / IIiIiII11i / OooOO000
elif o0ii1i == 2002 :
 OOOOo0oo0o ( iiOOooooO0Oo )
 if 2 - 2: ooOoO0O00 / Ii + oOo0O0Ooo
elif o0ii1i == 1013 :
 o0o0OO0o00o0O ( )
elif o0ii1i == 10111113 :
 oo0OoOOooO ( iiOOooooO0Oo )
 if 95 - 95: Ii1I / OOoOoo % iI11I1II1I1I + o0o00Oo0O
elif o0ii1i == 1014 :
 OOOOO0oOOoO ( )
 if 6 - 6: OOoOoo
elif o0ii1i == 1015 :
 iiiiII ( iiOOooooO0Oo )
 if 73 - 73: I11i % I11i . IIi * Ii1I - iIi1i1ii1
elif o0ii1i == 1016 :
 IIi1IIIi ( iiOOooooO0Oo , O00Ooo , iiI11ii1I1 )
 if 97 - 97: OOoOoo
elif o0ii1i == 1017 :
 ii11I1 ( )
 if 15 - 15: o0o00Oo0O - oOo0O0Ooo / ooOoO0O00 . O00OOo00oo0o
elif o0ii1i == 1018 :
 OOo ( iiOOooooO0Oo )
 if 64 - 64: IIiIi1iI / ooOoO0O00
elif o0ii1i == 1023 :
 oO0oo ( )
 if 100 - 100: IIiIiII11i
elif o0ii1i == 1024 :
 OO0OO0 ( iiOOooooO0Oo )
 if 16 - 16: iIi1i1ii1
elif o0ii1i == 1025 :
 i11IIii ( iiOOooooO0Oo )
 if 96 - 96: I11i / O00OOo00oo0o % iIi1i1ii1 - IIiIi1iI
elif o0ii1i == 4001 :
 ooo0O0o00O ( )
 if 35 - 35: IIi
elif o0ii1i == 4002 :
 IIii1111 ( )
 if 90 - 90: Ii
elif o0ii1i == 4003 :
 OoOoO0oOOooo ( )
 if 47 - 47: oO0o . Ii
elif o0ii1i == 4004 :
 I1ii1ii11i1I ( )
 if 9 - 9: OOooOOo - iiII11i1I1IIi . ii % IIiIi1iI
elif o0ii1i == 4005 :
 o0OoOO ( )
 if 13 - 13: oO0o * iI11I1II1I1I + IIiIiII11i - I1ii11iIi11i - OOooOOo
elif o0ii1i == 4006 :
 Oo0OO0000oooo ( )
 if 43 - 43: OooOO000 / O00OOo00oo0o * oOo0O0Ooo % IIiIi1iI % oOo0O0Ooo
elif o0ii1i == 4007 :
 oOoO00o ( )
 if 18 - 18: oO0o
elif o0ii1i == 4008 :
 OOOO0OOO ( )
 if 99 - 99: OooOO000 / oo0oO00 . Ii / iiII11i1I1IIi + ooOoO0O00 - iiII11i1I1IIi
elif o0ii1i == 4009 : O0Oooo ( )
elif o0ii1i == 4010 : oO0Ooo0OooOOo ( )
elif o0ii1i == 3000 :
 iIiii1Ii ( )
 if 50 - 50: ooOoO0O00
elif o0ii1i == 3001 :
 oOOOo ( )
 if 56 - 56: oO0o + O00OOo00oo0o / iIi1i1ii1
elif o0ii1i == 3002 :
 o0OOOoO0O ( iiOOooooO0Oo )
 if 75 - 75: OOooOOo
elif o0ii1i == 3003 :
 OoOOo ( iiOOooooO0Oo )
 if 96 - 96: I11i * iiII11i1I1IIi * I1ii11iIi11i
elif o0ii1i == 3004 :
 IIiI ( iiOOooooO0Oo )
 if 36 - 36: ii + IIiIi1iI . oo0oO00 * IIiIi1iI + OOoOoo
elif o0ii1i == 404 :
 III1Ii ( iiI11ii1I1 , iiOOooooO0Oo , O00Ooo )
 if 45 - 45: oo0oO00 / OooOO000 + Ii1I - I1ii11iIi11i - IIiIi1iI . iI11I1II1I1I
elif o0ii1i == 405 :
 O0i1I1Iii1IiiIi ( iiOOooooO0Oo )
 if 52 - 52: oOo0O0Ooo + ooOoO0O00 . OooOO000 * oOo0O0Ooo
elif o0ii1i == 7030 :
 ii11 ( )
 if 31 - 31: I1ii11iIi11i % iI11I1II1I1I . o0o00Oo0O
elif o0ii1i == 7021 :
 oo0o0o ( iiI11ii1I1 )
 if 80 - 80: iiII11i1I1IIi / I1ii11iIi11i + Ii1I
elif o0ii1i == 7022 :
 II1i1iii1iiiI ( iiI11ii1I1 )
 if 18 - 18: IIiIiII11i - OooOO000 / iI11I1II1I1I % OOooOOo % Ii1I / I11i
elif o0ii1i == 7000 :
 OOo0OOO0OO ( iiI11ii1I1 , iiOOooooO0Oo , img )
 if 47 - 47: IIi
elif o0ii1i == 7050 :
 IIIIIIi1i ( iiOOooooO0Oo )
 if 24 - 24: iIi1i1ii1 % I11i
elif o0ii1i == 7051 :
 OoOo00oOoo0oO ( iiOOooooO0Oo )
 if 87 - 87: I11i % OooOO000 / IIiIi1iI - OOoOoo + Ii
elif o0ii1i == 7052 :
 I1i1iI1I1II ( iiOOooooO0Oo )
 if 85 - 85: ii * OOoOoo . IIi / OooOO000 / ii
elif o0ii1i == 7053 :
 iiI11II ( iiOOooooO0Oo )
 if 87 - 87: oO0o
elif o0ii1i == 7054 :
 CoolPlay ( iiOOooooO0Oo )
 if 32 - 32: Ii - OOooOOo * iiII11i1I1IIi . I1ii11iIi11i * IIiIi1iI
elif o0ii1i == 7060 :
 O0O0O00OoO0O ( )
 if 21 - 21: IIi
elif o0ii1i == 7061 :
 OooOoOo ( iiOOooooO0Oo )
 if 11 - 11: oo0oO00 % Ii * o0o00Oo0O
elif o0ii1i == 7063 :
 i1II11III ( iiOOooooO0Oo )
 if 28 - 28: O00OOo00oo0o / iI11I1II1I1I + IIi . Ii1I % IIi + oO0o
elif o0ii1i == 7062 :
 Ooo0O0ooo0o ( iiOOooooO0Oo )
 if 79 - 79: oo0oO00
elif o0ii1i == 7064 :
 NATatozcat ( )
 if 39 - 39: O00OOo00oo0o % oo0oO00 % o0o00Oo0O % o0o00Oo0O - OooOO000 - oo0oO00
elif o0ii1i == 7067 :
 O0Oo ( iiOOooooO0Oo )
 if 83 - 83: Ii + iI11I1II1I1I
elif o0ii1i == 7066 :
 NATatozA ( iiOOooooO0Oo )
 if 21 - 21: I11i / Ii % O00OOo00oo0o
elif o0ii1i == 7065 :
 O0oOo00Oo0oo0 ( iiOOooooO0Oo )
 if 56 - 56: I11i * iI11I1II1I1I . iIi1i1ii1 + OOooOOo % O00OOo00oo0o
elif o0ii1i == 7070 :
 iiiIII1iii1I ( )
 if 11 - 11: IIi
elif o0ii1i == 7071 :
 DIZIlist ( iiOOooooO0Oo )
 if 12 - 12: ii * IIi * Ii1I * IIiIi1iI
elif o0ii1i == 7072 :
 DIZIpull ( iiOOooooO0Oo )
 if 26 - 26: ii . ooOoO0O00 + oO0o
elif o0ii1i == 7073 :
 WATCHDIZI ( iiOOooooO0Oo )
 if 42 - 42: Ii * I11i % iiII11i1I1IIi % I1ii11iIi11i + I11i * Ii
elif o0ii1i == 7002 :
 II1I1iI1i1IiI ( )
 if 66 - 66: iIi1i1ii1 / OOoOoo . ii * I1ii11iIi11i % Ii
elif o0ii1i == 7003 :
 O0OoO0o ( iiOOooooO0Oo )
 if 100 - 100: Ii1I % IIiIiII11i * Ii - OooOO000
elif o0ii1i == 7004 :
 I1Iiii11 ( iiOOooooO0Oo )
 if 69 - 69: IIi + OooOO000 / O00OOo00oo0o
elif o0ii1i == 7020 :
 I1i1Iii1111Ii ( iiOOooooO0Oo )
 if 37 - 37: iI11I1II1I1I * iiII11i1I1IIi / OOoOoo * I1ii11iIi11i % Ii
elif o0ii1i == 7001 :
 I1i1iiiI1 ( )
 if 93 - 93: IIiIi1iI + IIiIi1iI
elif o0ii1i == 7010 :
 iiii1IiI1i1 ( iiOOooooO0Oo )
 if 65 - 65: ii * iiII11i1I1IIi * oo0oO00 % Ii1I * IIiIiII11i
elif o0ii1i == 7011 :
 II1I11i ( iiOOooooO0Oo )
 if 86 - 86: Ii / iiII11i1I1IIi * OooOO000 - OooOO000
elif o0ii1i == 7012 :
 IiiI1i1I1 ( iiOOooooO0Oo )
 if 32 - 32: I1ii11iIi11i . o0o00Oo0O
elif o0ii1i == 7013 :
 cnfTVPlay2 ( iiOOooooO0Oo )
elif o0ii1i == 7014 :
 CNF_Studio_Indexer . MV_Movies ( iiOOooooO0Oo )
elif o0ii1i == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( iiOOooooO0Oo )
elif o0ii1i == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iiI11ii1I1 , iiOOooooO0Oo , O00Ooo )
elif o0ii1i == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif o0ii1i == 7018 :
 oO0OIiIi1ii1Ii ( )
elif o0ii1i == 7019 :
 CNF_Studio_Indexer . List_Movies ( iiOOooooO0Oo )
elif o0ii1i == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( iiOOooooO0Oo )
elif o0ii1i == 7024 :
 CNF_Studio_Indexer . Box_Office ( iiOOooooO0Oo )
 if 48 - 48: Ii1I % IIiIiII11i + iiII11i1I1IIi
elif o0ii1i == 8000 :
 oo000oiIIIII ( )
elif o0ii1i == 8001 :
 ooOoooOoo0oO ( )
elif o0ii1i == 8002 :
 Oo0Oo0o00oO ( )
elif o0ii1i == 8003 :
 o0O0o ( )
elif o0ii1i == 8004 :
 I1iIi1i ( )
elif o0ii1i == 8005 :
 oo0ooO0O ( )
elif o0ii1i == 8006 :
 II1iiIiI1 ( iiI11ii1I1 , iiOOooooO0Oo )
elif o0ii1i == 8030 :
 O0O000O ( iiOOooooO0Oo )
elif o0ii1i == 8045 :
 I1ii1i11iI1 ( iiOOooooO0Oo )
elif o0ii1i == 8046 :
 IiOOo0 ( iiOOooooO0Oo )
elif o0ii1i == 8047 :
 OO00o0O0oOooO ( iiOOooooO0Oo )
elif o0ii1i == 8048 :
 Oo0ooo ( iiOOooooO0Oo )
elif o0ii1i == 8049 :
 Oo00o00 ( iiOOooooO0Oo )
elif o0ii1i == 804900 :
 OoOo0O0 ( iiOOooooO0Oo )
elif o0ii1i == 8020 :
 Oo0 ( )
elif o0ii1i == 8021 :
 O0oooO ( iiOOooooO0Oo )
elif o0ii1i == 8022 :
 Ii1IiIi11i1 ( iiOOooooO0Oo )
elif o0ii1i == 8023 :
 OO0OOo00Oo ( iiOOooooO0Oo )
elif o0ii1i == 8040 :
 iII1ii1 ( )
elif o0ii1i == 8041 :
 iiI111iIi1 ( iiOOooooO0Oo )
elif o0ii1i == 8042 :
 IIi1I1 ( iiOOooooO0Oo )
elif o0ii1i == 8043 :
 yt . PlayVideo ( iiOOooooO0Oo )
elif o0ii1i == 8044 :
 oO00o0oOoo ( iiOOooooO0Oo )
elif o0ii1i == 8060 :
 Oo00o0OO0O00o ( )
elif o0ii1i == 8061 :
 i1I1IIIiii1 ( iiOOooooO0Oo )
elif o0ii1i == 8064 :
 oooooOOO000Oo ( )
elif o0ii1i == 8065 :
 i1iiIi1IiiiI ( iiOOooooO0Oo )
elif o0ii1i == 8070 :
 oOOo00ooO ( )
elif o0ii1i == 8071 :
 ooOoOOOoOo0oO0OoO ( iiOOooooO0Oo )
elif o0ii1i == 7080 :
 I1ii11 ( iiOOooooO0Oo )
elif o0ii1i == 8090 :
 I1iIi1IiI1i ( )
elif o0ii1i == 8091 :
 Oo0OO0 ( iiOOooooO0Oo )
elif o0ii1i == 8092 :
 o0oOo0OoO ( iiOOooooO0Oo )
elif o0ii1i == 8093 :
 o0ooOOoo0 ( iiOOooooO0Oo )
elif o0ii1i == 8081 :
 OoOooooo ( )
elif o0ii1i == 8062 :
 IIIIi1 ( iiOOooooO0Oo )
elif o0ii1i == 8063 :
 II111I1i1 ( iiOOooooO0Oo )
elif o0ii1i == 8050 :
 O0o ( )
elif o0ii1i == 8051 :
 O00oOOooO ( iiOOooooO0Oo )
elif o0ii1i == 8052 :
 IiIIii1iiI ( iiOOooooO0Oo )
elif o0ii1i == 8085 :
 iii11 ( )
elif o0ii1i == 8086 :
 i1IIIi1Iii1i ( iiOOooooO0Oo )
elif o0ii1i == 8087 :
 IIi1iI1i ( iiOOooooO0Oo )
elif o0ii1i == 8088 :
 Iii11II1 ( iiOOooooO0Oo , iiI11ii1I1 )
elif o0ii1i == 9000 :
 O0o00oO0oOO ( )
elif o0ii1i == 1111 :
 I1iI1IiI ( )
elif o0ii1i == 9001 :
 i1II ( )
elif o0ii1i == 9002 :
 ii1iIi1iIiI1i ( )
elif o0ii1i == 9003 :
 i1I1IiIiiI1II ( )
elif o0ii1i == 9004 :
 World1 ( )
elif o0ii1i == 9005 :
 World2 ( iiOOooooO0Oo )
elif o0ii1i == 9006 :
 World3 ( iiOOooooO0Oo )
elif o0ii1i == 9007 :
 OO0oOOOOO ( )
elif o0ii1i == 9008 :
 OoOo ( iiOOooooO0Oo )
elif o0ii1i == 9009 :
 oO0i1ii1i1 ( iiOOooooO0Oo )
elif o0ii1i == 9010 :
 iiiiiiI1iIi ( )
elif o0ii1i == 9011 :
 iI1Ii11IIiII ( iiOOooooO0Oo )
elif o0ii1i == 50 :
 OooOO0oOOo0O ( iiOOooooO0Oo )
elif o0ii1i == 9020 :
 champlist ( )
elif o0ii1i == 9021 :
 o00O00oOooo ( )
elif o0ii1i == 9022 :
 oooii111I1I1I ( )
elif o0ii1i == 9023 :
 iIIiIi1IiI1 ( )
elif o0ii1i == 9024 :
 OO00oo ( iiOOooooO0Oo )
elif o0ii1i == 9030 :
 i1II1i ( iiOOooooO0Oo )
elif o0ii1i == 9031 :
 O0oooooO0oOOo ( iiOOooooO0Oo )
elif o0ii1i == 9032 :
 oo0O0OO0Oooo ( iiOOooooO0Oo )
elif o0ii1i == 9033 :
 IiiI11Iii ( iiOOooooO0Oo )
elif o0ii1i == 9034 :
 iIIi ( )
elif o0ii1i == 7085 :
 iIIi1I1 ( iiOOooooO0Oo )
elif o0ii1i == 7086 :
 o00Oo ( iiOOooooO0Oo )
elif o0ii1i == 7087 :
 ooOoOoOoo ( i11iiiiI1i )
elif o0ii1i == 9666 :
 O0O0ooOOO ( iiOOooooO0Oo )
elif o0ii1i == 10100 : OoOOiIO0oOoo00Oo0O ( )
elif o0ii1i == 101001 : IIi1IiiIi1III ( iiOOooooO0Oo )
elif o0ii1i == 10105 : iiIII1i1 ( iiOOooooO0Oo )
elif o0ii1i == 10106 : oOOo0OOoOO0 ( iiOOooooO0Oo )
elif o0ii1i == 10104 : Ii1iII1ii1 ( iiOOooooO0Oo )
elif o0ii1i == 10107 : IiIiIiiIIii ( )
elif o0ii1i == 10103 : IiIi ( iiOOooooO0Oo )
elif o0ii1i == 10108 : oo0OoOO000O ( iiOOooooO0Oo )
elif o0ii1i == 10000 : Origin_Menu ( )
elif o0ii1i == 10001 : III111i11IiI ( )
elif o0ii1i == 10002 : O0O0Oo00 ( )
elif o0ii1i == 10003 : i1i1ii ( )
elif o0ii1i == 10004 : ooO00O0O0 ( iiOOooooO0Oo )
elif o0ii1i == 10005 : O0OO0oOOo ( )
elif o0ii1i == 10006 : ooOO0OOO00o ( iiOOooooO0Oo )
elif o0ii1i == 10007 : OOoOi1IiiI ( iiOOooooO0Oo , O00Ooo )
elif o0ii1i == 10008 : I1I11 ( )
elif o0ii1i == 10009 : oo00o000O ( )
elif o0ii1i == 10010 : o00oIII ( iiOOooooO0Oo )
elif o0ii1i == 10011 : I1iIII1IIiIi ( iiOOooooO0Oo )
elif o0ii1i == 10012 : iii1 ( iiOOooooO0Oo )
elif o0ii1i == 10109 : iI11iI ( iiOOooooO0Oo )
elif o0ii1i == 10013 : IIIiII11 ( iiOOooooO0Oo )
elif o0ii1i == 10014 : Iiiii1Iii1I ( )
elif o0ii1i == 10015 : i1o0 ( )
elif o0ii1i == 10016 : I1i ( iiOOooooO0Oo )
elif o0ii1i == 10017 : I1iI1i11IiI11 ( )
elif o0ii1i == 10018 : oOOoooOO ( )
elif o0ii1i == 10019 : IIIIIiiI11i1 ( )
elif o0ii1i == 10020 : i1i1IIiII1I ( )
elif o0ii1i == 10021 : O0oooo0O ( )
elif o0ii1i == 10022 : Oo0Oo ( iiOOooooO0Oo )
elif o0ii1i == 10023 : O0OOo ( iiI11ii1I1 , iiOOooooO0Oo )
elif o0ii1i == 10024 : OooOo ( iiOOooooO0Oo )
elif o0ii1i == 10025 : OOo0 ( )
elif o0ii1i == 10026 : iiIIIIiii ( )
elif o0ii1i == 10027 : iii1IiiiI1i1 ( )
elif o0ii1i == 10028 : i11Ii1IiIIIi ( )
elif o0ii1i == 10029 : iIi ( )
elif o0ii1i == 423 : OOOO00 ( iiOOooooO0Oo )
elif o0ii1i == 426 : Ii1iiI1i1 ( iiOOooooO0Oo )
elif o0ii1i == 10030 : Izle_Films ( )
elif o0ii1i == 10031 : Latest_Izle_Movies ( )
elif o0ii1i == 10032 : Izle_Genres ( )
elif o0ii1i == 10033 : Izle_Pop_Movies ( )
elif o0ii1i == 10034 : Izle_Boxsets ( )
elif o0ii1i == 10035 : Izle_Search ( )
elif o0ii1i == 10036 : Izle_Genres_Movie ( iiOOooooO0Oo )
elif o0ii1i == 10037 : Izle_Boxset_single ( iiOOooooO0Oo )
elif o0ii1i == 10038 : Izle_IFRAME ( )
elif o0ii1i == 10039 : Izle_Boxsets_Next ( iiOOooooO0Oo )
elif o0ii1i == 10040 : ooOO0OoO ( )
elif o0ii1i == 10041 : Oo0oOOO ( iiOOooooO0Oo )
elif o0ii1i == 10042 : I1IiiiI ( iiOOooooO0Oo )
elif o0ii1i == 10043 : oo0o ( )
elif o0ii1i == 10044 : ooOOO ( iiOOooooO0Oo )
elif o0ii1i == 10045 : ooooOoOooo00Oo ( iiI11ii1I1 )
elif o0ii1i == 10046 : O00O0O0OO00oo ( iiOOooooO0Oo )
elif o0ii1i == 10047 : O00Oo00OOoO0 ( iiOOooooO0Oo )
elif o0ii1i == 10048 : I1I1i11iiiiI ( iiOOooooO0Oo )
elif o0ii1i == 10049 : iII1I ( iiOOooooO0Oo )
elif o0ii1i == 10050 : OOOoo0OO ( )
elif o0ii1i == 10051 : Oo0i11iiI11II ( )
elif o0ii1i == 10052 : iI1iIii ( )
elif o0ii1i == 10053 : Addon ( iiOOooooO0Oo )
elif o0ii1i == 10054 : iIi1i ( iiOOooooO0Oo , iiI11ii1I1 )
elif o0ii1i == 10055 :
 ii1I11iI ( "addFavorite" )
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 IiIiI ( iiI11ii1I1 , iiOOooooO0Oo , O00Ooo , O0OoooO0 , oooOo )
elif o0ii1i == 10056 :
 ii1I11iI ( "rmFavorite" )
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 oOoOO ( iiI11ii1I1 )
elif o0ii1i == 10057 :
 ii1I11iI ( "getFavorites" )
 III ( )
elif o0ii1i == 10058 : iiIi1i ( )
elif o0ii1i == 10059 : Donators_Guide ( )
elif o0ii1i == 10060 : I1i11 ( )
elif o0ii1i == 10061 : I1iIII1IiiI ( )
elif o0ii1i == 10062 : I1Ii11II1I1 ( iiI11ii1I1 , iiOOooooO0Oo , i11iiiiI1i )
elif o0ii1i == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
elif o0ii1i == 10064 : o0OoOoOOoOo0o ( )
elif o0ii1i == 10065 : iI11Ii111 ( iiOOooooO0Oo )
elif o0ii1i == 10066 : OoOOo00 ( iiOOooooO0Oo )
elif o0ii1i == 10068 : i1Iii11I1i ( iiOOooooO0Oo )
elif o0ii1i == 10069 : Ooo00OoOOO ( iiOOooooO0Oo )
elif o0ii1i == 10070 : I1Ii ( iiOOooooO0Oo )
elif o0ii1i == 10071 : Genie_Watch ( )
elif o0ii1i == 10072 : iIiiIiiIi ( )
elif o0ii1i == 10073 : o0Oo0oOooOoOo ( iiOOooooO0Oo )
elif o0ii1i == 10074 : iIii1Ooo0oO0 ( iiOOooooO0Oo )
elif o0ii1i == 10075 : o0oo0000 ( O00Ooo , iiI11ii1I1 , iiOOooooO0Oo )
elif o0ii1i == 10076 : i1i1II11II1 ( iiOOooooO0Oo )
elif o0ii1i == 10077 : oOOO ( iiOOooooO0Oo )
elif o0ii1i == 10078 : oOOo0oo0o0o0 ( )
elif o0ii1i == 10079 : Genie_Watch_Tv_Shows ( )
elif o0ii1i == 10080 : Genie_Watch_Tv_Genre ( iiOOooooO0Oo )
elif o0ii1i == 10081 : Genie_Watch_TV_PlayRun ( iiOOooooO0Oo )
elif o0ii1i == 10082 : Genie_Watch_TV_Episodes ( iiOOooooO0Oo , O00Ooo )
elif o0ii1i == 10083 : Genie_Watch_Tv_Recent ( iiOOooooO0Oo )
elif o0ii1i == 10084 : IiiIiI111iI ( )
elif o0ii1i == 10085 : Iiii1i1 ( )
elif o0ii1i == 10086 : II1I ( )
elif o0ii1i == 20000 : O0000 ( )
elif o0ii1i == 20001 : ooOO ( iiOOooooO0Oo )
elif o0ii1i == 20002 : iii1IiI1i ( iiOOooooO0Oo )
elif o0ii1i == 20003 : OOOO00OOO00 ( iiOOooooO0Oo )
elif o0ii1i == 20004 : I1iI11IiiI11i ( iiOOooooO0Oo )
elif o0ii1i == 20005 : oOoO00O ( iiOOooooO0Oo )
elif o0ii1i == 21004 : OO0oO0o ( )
elif o0ii1i == 21005 : III1ii ( iiOOooooO0Oo )
elif o0ii1i == 21006 : o0oOoO00 ( iiOOooooO0Oo )
elif o0ii1i == 21007 : OoO0o00OOOOO ( iiOOooooO0Oo )
elif o0ii1i == 30000 : i1i1Ii1I ( )
elif o0ii1i == 30001 : ii111I11Ii ( )
elif o0ii1i == 10012 : Resolve ( iiOOooooO0Oo )
elif o0ii1i == 30003 : Oo0OOo ( )
elif o0ii1i == 30004 : I1II1IiI1 ( iiOOooooO0Oo )
elif o0ii1i == 30005 : i1iI1Ii11Ii1 ( iiOOooooO0Oo )
elif o0ii1i == 30006 : o0OoOoooo0 ( )
elif o0ii1i == 30007 : i1Ii11IIi1 ( )
elif o0ii1i == 30008 : oo0OoOO0000 ( iiOOooooO0Oo )
elif o0ii1i == 30009 : oOoo ( iiOOooooO0Oo )
elif o0ii1i == 30010 : iI1iI ( iiOOooooO0Oo )
elif o0ii1i == 30011 : OO0oo ( )
elif o0ii1i == 30012 : o00oO0O0oo0o ( )
elif o0ii1i == 30013 : oOoOo0o00o ( )
elif o0ii1i == 30014 : oOo ( )
elif o0ii1i == 30015 : IiI11I111 ( iiOOooooO0Oo , O00Ooo , O0OoooO0 )
elif o0ii1i == 30016 : i1iI1Iiii1I ( iiOOooooO0Oo )
elif o0ii1i == 30019 : OoiiI1i111 ( iiOOooooO0Oo )
elif o0ii1i == 30017 : OoOOiI ( iiOOooooO0Oo )
elif o0ii1i == 30018 : i111I1 ( iiOOooooO0Oo )
elif o0ii1i == 30030 : o00oo ( )
elif o0ii1i == 30031 : Ooii1IIi1ii ( )
elif o0ii1i == 30032 : oO00O0 ( )
elif o0ii1i == 30033 : Ii11IIIi1 ( )
elif o0ii1i == 30034 : ooooooo00oO0OO ( )
elif o0ii1i == 30035 : IiIIII1iiIIi ( iiOOooooO0Oo )
elif o0ii1i == 30036 : i1I1IiI1ii ( iiOOooooO0Oo )
elif o0ii1i == 30037 : O00OOoOOOO00O ( iiOOooooO0Oo )
elif o0ii1i == 30038 : iI ( )
elif o0ii1i == 30039 : Iii1IIII11I ( )
elif o0ii1i == 50000 : iIiIi11 ( )
elif o0ii1i == 50001 : OOOO00OooO ( )
elif o0ii1i == 50002 : O0Ooo00o00O ( iiOOooooO0Oo )
elif o0ii1i == 50003 : iiI1 ( i11iiiiI1i )
elif o0ii1i == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif o0ii1i == 60001 : OoO00o0 ( )
elif o0ii1i == 60002 : o0ooO0OOO ( iiI11ii1I1 )
elif o0ii1i == 60003 : II1iIII ( iiI11ii1I1 )
elif o0ii1i == 50004 : i11i1 ( )
elif o0ii1i == 50005 : speedtest . runtest ( iiOOooooO0Oo )
elif o0ii1i == 70001 : oo0 ( )
elif o0ii1i == 70002 : i11IiI ( iiOOooooO0Oo )
elif o0ii1i == 70003 : OoIi1I1I ( iiOOooooO0Oo )
elif o0ii1i == 70004 : oOOoOOO0oOoo ( iiOOooooO0Oo )
elif o0ii1i == 70005 : o0O0ooooooo00 ( iiOOooooO0Oo )
elif o0ii1i == 70006 : I1111ii11IIII ( )
elif o0ii1i == 50006 : iiIiI1i1 ( i1 , i1111 )
elif o0ii1i == 80000 : OoiI1I1 ( )
elif o0ii1i == 80001 : resolvefilmon ( iiOOooooO0Oo )
elif o0ii1i == 80002 : oOOoO0O ( )
elif o0ii1i == 80003 : Oo0O0000Oo00o ( iiI11ii1I1 , iiOOooooO0Oo , "None" )
elif o0ii1i == 80004 : ooooOoo0OO ( iiI11ii1I1 , iiOOooooO0Oo )
elif o0ii1i == 80005 : III1I1Iii1iiI ( )
elif o0ii1i == 80006 : oo0ooO0 ( iiOOooooO0Oo )
elif o0ii1i == 80007 : IIiiiiIiIIii ( iiOOooooO0Oo )
elif o0ii1i == 80008 : O0OO ( )
elif o0ii1i == 80009 : ooOOoO0o0 ( )
elif o0ii1i == 80010 : i1Ii1i11ii ( iiOOooooO0Oo )
elif o0ii1i == 80011 : iI1IIIIII ( iiOOooooO0Oo )
elif o0ii1i == 80012 : iII ( )
elif o0ii1i == 90000 : I1OO ( iiI11ii1I1 , iiOOooooO0Oo )
elif o0ii1i == 90001 : i11I1II1I11i ( )
elif o0ii1i == 90002 : Iiii1iI1i ( )
elif o0ii1i == 90003 : IiiI ( iiOOooooO0Oo )
elif o0ii1i == 90004 : O0oooooO ( iiOOooooO0Oo )
elif o0ii1i == 90005 : IIi1 ( iiOOooooO0Oo )
elif o0ii1i == 90006 : oOO00OoOo ( iiOOooooO0Oo )
elif o0ii1i == 90007 : oOoooO0OO00 ( iiOOooooO0Oo )
elif o0ii1i == 90008 : ooo0o00o ( iiOOooooO0Oo )
elif o0ii1i == 90009 : oooOOOoO0O ( iiOOooooO0Oo )
elif o0ii1i == 90010 : oO0O00oOOoooO ( )
elif o0ii1i == 90020 : o0oOO ( )
elif o0ii1i == 90021 : hellyeah2 ( iiOOooooO0Oo )
elif o0ii1i == 90022 : hellyeah3 ( iiOOooooO0Oo )
elif o0ii1i == 90023 : iIiI ( )
elif o0ii1i == 90024 : oOO0OO0OO ( iiOOooooO0Oo )
elif o0ii1i == 90025 : oOOoooO ( iiOOooooO0Oo )
if 25 - 25: OOoOoo * I11i / oOo0O0Ooo . OOoOoo % IIiIiII11i
elif o0ii1i == 90030 : I1i1I11I ( )
elif o0ii1i == 90031 : i1I1IiiIi1i ( )
elif o0ii1i == 90032 : Ooo0OOoOoO0 ( iiOOooooO0Oo )
elif o0ii1i == 90033 : IIo0Oo0oO0oOO00 ( iiOOooooO0Oo )
elif o0ii1i == 90034 : II1i111Ii1i ( iiOOooooO0Oo )
elif o0ii1i == 90035 : ooO0oooOO0 ( iiOOooooO0Oo )
elif o0ii1i == 90036 : OOOo0o ( iiOOooooO0Oo )
elif o0ii1i == 90039 : oo0o0o0o0o0 ( iiOOooooO0Oo )
elif o0ii1i == 90037 : O0iIiIIIIIii ( iiOOooooO0Oo )
elif o0ii1i == 90038 : Oo00OOOOoo0oo ( )
if 50 - 50: OOooOOo * OooOO000
elif o0ii1i == 10090 : OOooO0oo0o00o ( )
elif o0ii1i == 10091 : iii111i ( iiOOooooO0Oo )
elif o0ii1i == 10092 : ooO ( iiOOooooO0Oo )
elif o0ii1i == 10093 : O00OOOo0Oo0 ( iiOOooooO0Oo , O00Ooo )
elif o0ii1i == 10094 : IIIiiiI1Ii1 ( iiOOooooO0Oo , O00Ooo )
if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / iiII11i1I1IIi
elif o0ii1i == 90040 : iI1I ( )
elif o0ii1i == 90041 : iI1iii ( iiOOooooO0Oo )
elif o0ii1i == 90042 : Ii1 ( iiOOooooO0Oo )
elif o0ii1i == 90043 : II1II ( iiOOooooO0Oo )
elif o0ii1i == 90044 : o0oooO ( iiOOooooO0Oo )
elif o0ii1i == 90045 : o0OoO00 ( )
elif o0ii1i == 90046 : ooOo ( iiOOooooO0Oo )
elif o0ii1i == 90050 : iiI1iIii1i ( )
elif o0ii1i == 90051 : i1IiiI1iIi ( iiOOooooO0Oo )
elif o0ii1i == 90052 : IiI ( iiOOooooO0Oo )
elif o0ii1i == 90053 : ooi1II1I ( iiOOooooO0Oo )
elif o0ii1i == 90054 : iii1IIII1iii11I ( iiOOooooO0Oo )
elif o0ii1i == 90055 : oOoooO0 ( )
if 92 - 92: I11i
elif o0ii1i == 100001 : Stand_up ( )
if 8 - 8: OooOO000 + Ii1I . iIi1i1ii1
elif o0ii1i == 100003 : I1i ( iiOOooooO0Oo )
elif o0ii1i == 100004 : oo00O00oO000o ( iiOOooooO0Oo )
elif o0ii1i == 100005 : Resolve ( iiOOooooO0Oo )
elif o0ii1i == 100008 : Search ( )
elif o0ii1i == 100007 : o00oO ( iiOOooooO0Oo )
elif o0ii1i == 100009 : yt . PlayVideo ( iiOOooooO0Oo )
elif o0ii1i == 100010 : IIi1ii1Ii ( iiOOooooO0Oo )
elif o0ii1i == 100100 : oOOo0o0oo ( O00Ooo , iiOOooooO0Oo , ii11I1IiIIi1i1IIi )
elif o0ii1i == 100101 : OoO0O0O0o00 ( iiOOooooO0Oo , iiI11ii1I1 , O0OoooO0 , ii11I1IiIIi1i1IIi , O00Ooo )
elif o0ii1i == 100102 : i11i1iiI1i ( iiI11ii1I1 , iiOOooooO0Oo , O00Ooo , O0OoooO0 )
elif o0ii1i == 100106 : OoO ( iiOOooooO0Oo , iiI11ii1I1 )
elif o0ii1i == 100107 : OOO0oOoO0O ( )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
