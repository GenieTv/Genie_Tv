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
IiiIII111iI = "3.4.6"
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
  OOiIiIIi1 ( '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '' , 60000 , III1iII1I1ii + 'settings.png' , O0o0Oo , '' )
  if I1IIII1i ( ) == 'android' :
   iiOOooooO0Oo ( '[COLOR' + II + ']APK TOOL[/COLOR]' , str ( I1I1IiI1 ) , 30039 , III1iII1I1ii + 'APKTools.png' , O0o0Oo , '' )
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
 i111I1 = [ '[COLOR' + II + ']Force Genie Update Kodi 16+[/COLOR]' , '[COLOR' + II + ']APK TOOL[/COLOR]' , '[COLOR' + II + ']ADDONS[/COLOR]' , '[COLOR' + II + ']GenieTv RSS Feed[/COLOR]' , '[COLOR' + II + ']CONTACT US[/COLOR]' , '[COLOR' + II + ']OPEN SETTINGS[/COLOR]' , '[COLOR' + II + ']SOURCE LIST[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  Iiii1i1 ( )
 if iI11iI1IiiIiI == 1 :
  Ii1I1i ( )
 if iI11iI1IiiIiI == 2 :
  OOI1iI1ii1II ( )
 if iI11iI1IiiIiI == 3 :
  O0O0OOOOoo ( oOooO0 )
 if iI11iI1IiiIiI == 4 :
  OOooO0OOoo . ok ( i1 , i1111 )
 if iI11iI1IiiIiI == 5 :
  oo00 . openSettings ( sys . argv [ 0 ] )
 if iI11iI1IiiIiI == 6 :
  Ii1I1Ii ( )
  if 69 - 69: oOo0O0Ooo / I11i . I1111IIi * iiiiiiii1 % ii1ii11IIIiiI - I11i
def i1ioOOoo00O00o ( ) :
 oOooO0 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 oooooo0O000o = os . path . join ( O0O00Oo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( oOooO0 , oooooo0O000o , o0oOoO00o )
 OoO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoO
 print '======================================='
 extract . all ( oooooo0O000o , OoO , o0oOoO00o )
 ooO0O0O0ooOOO ( oOooO0 )
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
def i1ioOOoo00O00o ( ) :
 oOooO0 = 'http://genietv.co.uk/guideskins/tvguideskins.zip'
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Awesomeness" , '' , 'Please Wait' )
 oooooo0O000o = os . path . join ( O0O00Oo , 'GuideSkins' + '.zip' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( oOooO0 , oooooo0O000o , o0oOoO00o )
 OoO = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/skins' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoO
 print '======================================='
 extract . all ( oooooo0O000o , OoO , o0oOoO00o )
 ooO0O0O0ooOOO ( oOooO0 )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Your skins are now downloaded, Enjoy" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oOOo0O00o ( )
def oO0O00oOOoooO ( ) :
 OOiIiIIi1 ( '[COLOR' + II + ']Todays Games[/COLOR]' , str ( I1I1IiI1 ) , 90030 , III1iII1I1ii + 'tgames.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Replays[/COLOR]' , str ( I1I1IiI1 ) , 90031 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 46 - 46: oOo0O0Ooo - ii - ooOOOoO * IIiIiII11i
def I1i1I11I ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 i1IIIII11I1IiI = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for Oo0o0oooo0O0 , OooooOOoo0 in i1IIIII11I1IiI :
  iiIiI1i1 ( '[COLOR' + II + ']Tommys List[/COLOR]  ' + Oo0o0oooo0O0 , OooooOOoo0 )
def i1I1IiiIi1i ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 i1IIIII11I1IiI = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 90032 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
def Ooo0OOoOoO0 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , oOo0OOoO0 , O0o0Oo , '' )
 for url in next :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , III1iII1I1ii + 'NEXT.png' , O0o0Oo , '' )
def IIo0Oo0oO0oOO00 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 oo00OO0000oO = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1IIIII11I1IiI = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for iiI11ii1I1 , url in i1I :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for iiI11ii1I1 , url in I1II1 :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for url in oo00OO0000oO :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
  if 86 - 86: iI11I1II1I1I / OOooOOo . IIiIiII11i
def II1i111Ii1i ( url ) :
 if 'drive' in url :
  iii1 ( url )
 else :
  OoO000O0Oo = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( OoO000O0Oo )
  for url in i1IIIII11I1IiI :
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
 if 7 - 7: oO0o . ii1ii11IIIiiI % o000O0o * I11i1ii1 + I1111IIi + iiiiiiii1
def IIIIiII1i ( url ) :
 if url == 'http://' : return False
 try :
  O00O0oOO00O00 = urllib2 . Request ( url )
  O00O0oOO00O00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
  i1Oo00 . close ( )
 except Exception , i1II1 :
  return i1II1
 return True
def i11i1 ( ) :
 if 42 - 42: Ii * iI11I1II1I1I / Ii1I . Ii % ooOOOoO
 if 41 - 41: I1111IIi / o0o00Oo0O
 if 51 - 51: ooOOOoO % oOo0O0Ooo
 if 60 - 60: oOo0O0Ooo / Ii1IIIi1 . oOo0O0Ooo / iiiiiiii1 . I1111IIi
 if 92 - 92: OOooOOo + iiiiiiii1 * ii1ii11IIIiiI % oOo0O0Ooo
 i1i = OoOooO ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( i1i )
 if len ( i1IIIII11I1IiI ) > 0 :
  for iiI11ii1I1 , oOooO0 , i1I1i1 , O0OoooO0 in i1IIIII11I1IiI :
   OOiIiIIi1 ( iiI11ii1I1 , oOooO0 , 50005 , i1I1i1 , O0OoooO0 , '' )
def ooo0O0o00O ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + II + ']WIPE GENIE[/COLOR]' , '[COLOR' + II + ']Genie BUILDS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Wizard[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   I1i11 ( )
  if iI11iI1IiiIiI == 1 :
   IiIi1I1 ( )
  if iI11iI1IiiIiI == 2 :
   IiIIi1 ( IIIIiii1IIii )
  if iI11iI1IiiIiI == 3 :
   II1i11I ( oOooO0 )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 10060 , III1iII1I1ii + 'BackupMyBuild.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 49 , III1iII1I1ii + 'RestoreMyBuild.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']WIPE GENIE[/COLOR]' , str ( I1I1IiI1 ) , 41 , III1iII1I1ii + 'WipeGenie.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Genie BUILDS[/COLOR]' , str ( I1I1IiI1 ) , 44 , III1iII1I1ii + 'GenieBuilds.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 50 - 50: ii % ooOOOoO
def IIii1111 ( ) :
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
  iiOOooooO0Oo ( '[COLOR' + II + ']FREEVIEW[/COLOR]' , str ( I1I1IiI1 ) , 90023 , III1iII1I1ii + 'freeview.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BOSS DOCS[/COLOR]' , i11 ( 'aHR0cHM6Ly9hdGxhbnRpYzI4MC5zdGFydGRlZGljYXRlZC5uZXQvYm9zcy9kb2NzLw==' ) , 2032 , III1iII1I1ii + 'boss.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , III1iII1I1ii + 'zone.png' , O0o0Oo , '' )
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
  iiOOooooO0Oo ( '[COLOR' + II + ']COMEDY ZONE[/COLOR]' , i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL2NvbS9ib3NzY29tLnBocA==' ) , 1016 , III1iII1I1ii + 'zone.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']FREEVIEW[/COLOR]' , str ( I1I1IiI1 ) , 90023 , III1iII1I1ii + 'freeview.png' , O0o0Oo , '' )
  if Ooo == '5knuckleshuffle' :
   iiOOooooO0Oo ( '[COLOR' + II + ']XVID[/COLOR]' , str ( I1I1IiI1 ) , 10100 , III1iII1I1ii + 'Jizbox.png' , O0o0Oo , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']ADULT CHANNELS[/COLOR]' , str ( I1I1IiI1 ) , 30033 , III1iII1I1ii + 'adu.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Football' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']FOOTBALL[/COLOR]' , '' , 10002 , III1iII1I1ii + 'Football.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']NEWS[/COLOR]' , str ( I1I1IiI1 ) , 30032 , III1iII1I1ii + 'News.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']HOBBIES[/COLOR]' , str ( I1I1IiI1 ) , 4008 , III1iII1I1ii + 'Hobbies.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Documentaries' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , str ( I1I1IiI1 ) , 8040 , III1iII1I1ii + 'documentaries.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'Disclose' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']DISCLOSE TV[/COLOR]' , str ( I1I1IiI1 ) , 7001 , III1iII1I1ii + 'DiscloseTV.png' , O0o0Oo , '' )
   if 42 - 42: ooOOOoO / I11i . o000O0o + o000O0o % OOooOOo + Ii
   if 56 - 56: I11i
   if 28 - 28: O0OOOoOoo0 . O0OOOoOoo0 % iI11I1II1I1I * iI11I1II1I1I . I11i / O0OOOoOoo0
   if 27 - 27: oO0o + I11i1ii1 - ooOoO0O00
   if 69 - 69: I1111IIi - o0o00Oo0O % Ii1I + Ii . OOooOOo / oO0o
   if 79 - 79: o0o00Oo0O * Ii - I1111IIi / I1111IIi
   if 48 - 48: o0o00Oo0O
   if 93 - 93: Ii - oOo0O0Ooo * Ii1I * ooOOOoO % o0o00Oo0O + ii
   if 25 - 25: I1111IIi + ii1ii11IIIiiI / I11i1ii1 . I11i % o0o00Oo0O * oO0o
   if 84 - 84: I11i1ii1 % ii1ii11IIIiiI + Ii
   if 28 - 28: I1ii11iIi11i + oO0o * Ii1IIIi1 % o000O0o . ooOOOoO % o0o00Oo0O
   if 16 - 16: ooOOOoO - iI11I1II1I1I / oOo0O0Ooo . IIiIiII11i + iI11I1II1I1I
   if 19 - 19: oO0o - I1ii11iIi11i . o0o00Oo0O
   if 60 - 60: IIiIiII11i + I1ii11iIi11i
   if 9 - 9: I11i1ii1 * ii - iI11I1II1I1I + OOooOOo / oO0o . oO0o
   if 49 - 49: IIiIiII11i
   if 25 - 25: ii - oOo0O0Ooo . oOo0O0Ooo * o000O0o
   if 81 - 81: O0OOOoOoo0 + I1111IIi
   if 98 - 98: oOo0O0Ooo
 I1I11i ( 'movies' , 'MAIN' )
def o00o0II1I ( ) :
 i111I1 = [ '[COLOR' + II + ']FOOTBALL[/COLOR]' , '[COLOR' + II + ']KIDS[/COLOR]' , '[COLOR' + II + ']NEWS[/COLOR]' , '[COLOR' + II + ']HOBBIES[/COLOR]' , '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II + ']DISCLOSE TV[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']CATEGORIES[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  II1I1I1Ii ( )
 if iI11iI1IiiIiI == 1 :
  OOOOoO00o0O ( )
 if iI11iI1IiiIiI == 2 :
  I1I1I1IIi1III ( )
 if iI11iI1IiiIiI == 3 :
  II11IiiIII ( )
 if iI11iI1IiiIiI == 4 :
  o0OOOo ( )
 if iI11iI1IiiIiI == 5 :
  ii1iiIiIII1ii ( )
  if 82 - 82: O0OOOoOoo0
  if 65 - 65: I11i1ii1 . ii / Ii1I . ooOoO0O00 * oO0o
  if 19 - 19: Ii + ii - I1ii11iIi11i - ooOOOoO
def ii1Ii11I ( ) :
 if not os . path . exists ( IIIII ) :
  iiIiI1i1 ( 'Change Log 25/2/17 - v3.4.4' , 'GenieTv Now Krypton Compatible,[CR] G.O.D.S (GenieTv On Demand Soaps) Added To GenieTv,[CR] RaysRavers And RaizTv Updated,[CR] More Sections Now Available For Download Including Kids,[CR] Tv Guide Removed And Replaced By External App,[CR] Boss Documentaries A Masterpiece By Jason Cadd,[CR] Updates To All Searches,[CR] StreamTeam Cleaned Up,[CR] Addon Overall CleanUp,[CR] General Maintence' )
  os . makedirs ( IIIII )
  if 21 - 21: o0o00Oo0O % I1111IIi . oOo0O0Ooo / IIiIiII11i + I1111IIi
  if 53 - 53: o000O0o - oOo0O0Ooo - o000O0o * O0OOOoOoo0
def oooooo0OO ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iI1I ( )
  if iI11iI1IiiIiI == 1 :
   OooOoOo ( )
  if iI11iI1IiiIiI == 2 :
   III1I1Iii1iiI ( oOooO0 )
  if iI11iI1IiiIiI == 3 :
   i1Iii11I1i ( )
  if iI11iI1IiiIiI == 4 :
   Oo00o0OO0O00o ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if iI11iI1IiiIiI == 5 :
   O0Oooo ( )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 10200 , III1iII1I1ii + 'rated.png' , O0o0Oo , '' )
  if 21 - 21: I1ii11iIi11i
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']POPCORN BOX[/COLOR]' , str ( I1I1IiI1 ) , 7061 , III1iII1I1ii + 'PopcornBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Desi Flix[/COLOR]' , '' , 80005 , III1iII1I1ii + 'Desi.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , III1iII1I1ii + 'FilmTrailers.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , III1iII1I1ii + 'ClassicMovies.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def I1ii1 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']DAILY LISTS[/COLOR]' , '' , 9007 , Oo00OOOOO , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Oo00OOOOO , O0o0Oo , '' )
 if 99 - 99: I11i1ii1 . iiiiiiii1 % I1111IIi * I1111IIi . ooOoO0O00
 if 72 - 72: Ii1IIIi1 % Ii1I + oO0o / o000O0o + I1111IIi
 if 10 - 10: iiiiiiii1 / I11i1ii1 + Ii / ii1ii11IIIiiI
 if 74 - 74: Ii1IIIi1 + o0o00Oo0O + ooOoO0O00 - ooOoO0O00 + IIiIiII11i
 if 83 - 83: Ii1I - oOo0O0Ooo + Ii1IIIi1
def iIi1Ii1i1iI ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']THE SOURCE[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']RETURN DATES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   IIiI1 ( )
  if iI11iI1IiiIiI == 1 :
   i1iI1 ( )
  if iI11iI1IiiIiI == 2 :
   ii1 ( )
  if iI11iI1IiiIiI == 3 :
   I1IiiI1ii1i ( )
  if iI11iI1IiiIiI == 4 :
   O0ooO0OoO00o ( )
  if iI11iI1IiiIiI == 5 :
   II1iiiiII ( )
  if iI11iI1IiiIiI == 6 :
   O0OoOO0oo0 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  if 96 - 96: OOooOOo . I11i - I11i1ii1
  if 99 - 99: I1111IIi . I1ii11iIi11i - ii1ii11IIIiiI % ii1ii11IIIiiI * o0o00Oo0O . IIiIiII11i
  if 4 - 4: ii1ii11IIIiiI
  iiOOooooO0Oo ( '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '' , 8020 , III1iII1I1ii + 'iWatchSeries.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RETURN DATES[/COLOR]' , str ( I1I1IiI1 ) , 10095 , III1iII1I1ii + 'RD.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC TV[/COLOR]' , str ( I1I1IiI1 ) , 8064 , III1iII1I1ii + 'ClassicTV.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , III1iII1I1ii + 'TVShowTrailers.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def OO0oOOoo ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   oOOO00o000o = '[COLOR' + II + ']PANDORAS BOX[/COLOR]'
   if 9 - 9: o000O0o + ooOOOoO / ooOOOoO
   if 12 - 12: ii % I11i * ooOOOoO % iI11I1II1I1I / ii1ii11IIIiiI
   if 27 - 27: Ii % IIiIiII11i % ooOOOoO . o0o00Oo0O - I1ii11iIi11i + OOooOOo
   if 57 - 57: iI11I1II1I1I / ooOOOoO - ooOoO0O00
  i111I1 = [ oOOO00o000o , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + II + ']RAIZ TV[/COLOR]' , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   ooOOo00O00Oo ( )
  if iI11iI1IiiIiI == 1 :
   IiII1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , I1iIi1iIiiIiI , iiI11ii1I1 )
  if iI11iI1IiiIiI == 2 :
   I1i11ii ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0' ) ) )
  if iI11iI1IiiIiI == 3 :
   IiII1 ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , I1iIi1iIiiIiI , iiI11ii1I1 )
   if 42 - 42: O0OOOoOoo0 + I1111IIi
   if 96 - 96: Ii1IIIi1
   if 85 - 85: I11i . OOooOOo / I11i1ii1 . o0o00Oo0O % iiiiiiii1
   if 90 - 90: I1ii11iIi11i % o0o00Oo0O * iI11I1II1I1I . O0OOOoOoo0
   if 8 - 8: I11i1ii1 + IIiIiII11i / O0OOOoOoo0 / ooOOOoO
 else :
  if 74 - 74: o0o00Oo0O / ooOoO0O00
  if 78 - 78: ii . oO0o + I11i1ii1 - ooOoO0O00
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']PANDORAS BOX[/COLOR]' , str ( I1I1IiI1 ) , 10025 , III1iII1I1ii + 'PandorasBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Technica-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'Roadrunner-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0' ) ) , 90037 , III1iII1I1ii + 'raiztv.png' , O0o0Oo , '' )
  if 31 - 31: ii . Ii1IIIi1
  if 83 - 83: O0OOOoOoo0 . o0o00Oo0O / I1ii11iIi11i / Ii1IIIi1 - IIiIiII11i
  if 100 - 100: oO0o
  if 46 - 46: OOooOOo / iI11I1II1I1I % O0OOOoOoo0 . iI11I1II1I1I * O0OOOoOoo0
  if 38 - 38: Ii1I - O0OOOoOoo0 / o0o00Oo0O . iiiiiiii1
  if 45 - 45: iiiiiiii1
 I1I11i ( 'movies' , 'MAIN' )
 if 83 - 83: OOooOOo . ii
def Oo0ooo ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
def IIiIiiii ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)".+?</td><td align=' ) . findall ( OoO000O0Oo )
 for ooo0 , oO000oOo00o0o in i1IIIII11I1IiI :
  if '[DIR]' in ooo0 :
   O00oO0 ( ( '[COLOR' + II + ']' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oO000oOo00o0o , 1018 , III1iII1I1ii + 'SilentHunter.png' )
  if 'mkv' in oO000oOo00o0o :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oO000oOo00o0o , 222 , III1iII1I1ii + 'SilentHunter.png' )
  if 'avi' in oO000oOo00o0o :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + oO000oOo00o0o + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mkv' , '' ) , url + oO000oOo00o0o , 222 , III1iII1I1ii + 'SilentHunter.png' )
   if 24 - 24: Ii - iiiiiiii1
def i11iiI1111 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , III1iII1I1ii + 'scraped.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 if 97 - 97: I1ii11iIi11i * oOo0O0Ooo . iI11I1II1I1I
def I1Ii1111iIi ( url ) :
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 i1IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , url , I1I , ooooo , O0OoooO0 , i11IIIiI1I in i1IIIII11I1IiI :
  if ooooo == '123' :
   ooooo = III1iII1I1ii + 'appstreams.png'
  if O0OoooO0 == '123' :
   O0OoooO0 = III1iII1I1ii + 'appstreams.png'
  if 'php' in url :
   iiOOooooO0Oo ( iiI11ii1I1 , url , 100010 , ooooo , O0OoooO0 , i11IIIiI1I )
  elif 'playlist' in url :
   iiOOooooO0Oo ( iiI11ii1I1 , url , 100007 , ooooo , O0OoooO0 , i11IIIiI1I )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( iiI11ii1I1 , url , 100100 , ooooo , O0OoooO0 , i11IIIiI1I )
  elif not 'http' in url :
   o0iiiI1I1iIIIi1 ( iiI11ii1I1 , url , 100009 , ooooo , O0OoooO0 , i11IIIiI1I , '' )
  else :
   o0iiiI1I1iIIIi1 ( iiI11ii1I1 , url , 100005 , ooooo , O0OoooO0 , i11IIIiI1I , '' )
   if 17 - 17: iI11I1II1I1I . ii / ooOOOoO % IIiIiII11i % ooOoO0O00 / Ii
def OOOIiiiii1iI ( url ) :
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 IIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , oOo0OOoO0 , i11IIIiI1I , O0OoooO0 , iiI11ii1I1 in IIi :
  if oOo0OOoO0 == '123' :
   oOo0OOoO0 = III1iII1I1ii + 'appstreams.png'
  if O0OoooO0 == '123' :
   O0OoooO0 = O0o0Oo
  if 'php' in url :
   iiOOooooO0Oo ( iiI11ii1I1 , url , 100004 , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
  elif 'playlist' in url :
   iiOOooooO0Oo ( iiI11ii1I1 , url , 100007 , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( iiI11ii1I1 , url , 100100 , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
  elif not 'http' in url :
   o0iiiI1I1iIIIi1 ( iiI11ii1I1 , url , 100009 , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I , '' )
  else :
   o0iiiI1I1iIIIi1 ( iiI11ii1I1 , url , 100005 , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I , '' )
   if 89 - 89: IIiIiII11i + ooOoO0O00 + IIiIiII11i
def IiII1II11I ( url ) :
 if 54 - 54: I1111IIi + o0o00Oo0O + ooOOOoO * iiiiiiii1 - Ii1IIIi1 % o000O0o
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 I111 = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iI1I1i11iIIii in I111 :
  ooooo = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( iI1I1i11iIIii ) )
  for ooooo in ooooo :
   ooooo = ooooo
  iiI11ii1I1 = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( iI1I1i11iIIii ) )
  for iiI11ii1I1 in iiI11ii1I1 :
   if 'elete' in iiI11ii1I1 :
    pass
   elif 'rivate Vid' in iiI11ii1I1 :
    pass
   else :
    iiI11ii1I1 = ( iiI11ii1I1 ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  IIIIIiI111I = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( iI1I1i11iIIii ) )
  for IIIIIiI111I in IIIIIiI111I :
   IIIIIiI111I = IIIIIiI111I
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( iI1I1i11iIIii ) )
  for url in url :
   url = url
  o0iiiI1I1iIIIi1 ( '[COLORred]' + str ( IIIIIiI111I ) + '[/COLOR] : ' + str ( iiI11ii1I1 ) , str ( url ) , 100009 , str ( ooooo ) , O0o0Oo , '' , '' )
  I1I11i ( 'movies' , '' )
  if 11 - 11: oOo0O0Ooo - oO0o
  if 39 - 39: Ii - iI11I1II1I1I / o000O0o
  if 70 - 70: I1111IIi
  if 34 - 34: iiiiiiii1 % I1111IIi
def IiI1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 IIi = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , oOo0OOoO0 , i11IIIiI1I , O0OoooO0 , iiI11ii1I1 in IIi :
  if '.php' in url :
   iiOOooooO0Oo ( iiI11ii1I1 , url , 100210 , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
  else :
   OOiIiIIi1 ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
   if 87 - 87: I11i1ii1
   if 45 - 45: oO0o / ii - O0OOOoOoo0 / ii1ii11IIIiiI % I1111IIi
   if 83 - 83: oOo0O0Ooo . iI11I1II1I1I - I1111IIi * Ii
def IiI11i1IIiiI ( iconimage , url , extra ) :
 ooooo = ' '
 oOOo000oOoO0 = ' '
 O0OoooO0 = ' '
 OoOo00o0OO = ' '
 ii1IIIIiI11 = I11o0oO00oO0o0o0 ( url )
 ooooo = re . compile ( '<img src="(.+?)">' ) . findall ( ii1IIIIiI11 )
 for ooooo in ooooo :
  ooooo = ooooo
 iI1IIIii = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( ii1IIIIiI11 )
 for O0OoooO0 in iI1IIIii :
  O0OoooO0 = O0OoooO0
 i1IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( ii1IIIIiI11 )
 for url , OoOo00o0OO in i1IIIII11I1IiI :
  OoOo00o0OO = 'S' + ( OoOo00o0OO ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oO0Oo + url
  I1i11ii11 ( ( OoOo00o0OO ) . replace ( '  ' , '' ) , url , 100101 , ooooo , O0OoooO0 , oOOo000oOoO0 , '' )
  I1I11i ( 'Movies' , 'info' )
  if 81 - 81: Ii1IIIi1 - ooOOOoO % I11i1ii1 - oO0o / I1ii11iIi11i
def Ii1iI111 ( url , name , fanart , extra , iconimage ) :
 O0oooo00o0Oo = extra
 OoOo00o0OO = name
 ii1IIIIiI11 = I11o0oO00oO0o0o0 ( url )
 ooooo = iconimage
 i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( ii1IIIIiI11 )
 for url , name , I1iii in i1IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oO0Oo + url
  I1iii = I1iii
  oO0o0O0Ooo0o = name + ' - [COLORred]' + I1iii + '[/COLOR]'
  I1i11ii11 ( oO0o0O0Ooo0o , url , 100102 , ooooo , fanart , 'Aired : ' + I1iii , oO0o0O0Ooo0o )
  if 21 - 21: iiiiiiii1 - oOo0O0Ooo + ooOOOoO
def ooOoo0o0O ( name , URL , iconimage , fanart ) :
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( URL )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , name in i1IIIII11I1IiI :
  for oOOOoo00 in oOOoo0Oo :
   if oOOOoo00 in oOooO0 :
    URL = 'http://www.watchseriesgo.to/link/' + oOooO0
    o0iiiI1I1iIIIi1 ( name , URL , 100106 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( i1IIIII11I1IiI ) <= 0 :
  I1i11ii11 ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 77 - 77: o000O0o
  if 64 - 64: I1ii11iIi11i * ii . I1ii11iIi11i
def ii1Ii1IiIIi ( url , name ) :
 o0OO0 = name
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 I1II1 = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  oOo00Oo0o0Oo ( url , o0OO0 )
 for url in i1I :
  oOo00Oo0o0Oo ( url , o0OO0 )
 for url in I1II1 :
  oOo00Oo0o0Oo ( url , o0OO0 )
  if 37 - 37: I1111IIi . I11i / I11i1ii1 . Ii1IIIi1
def oOo00Oo0o0Oo ( url , season_name ) :
 if 'daclips.in' in url :
  oOOOOo0OoO ( url , season_name )
 elif 'filehoot.com' in url :
  oo0o0oooo ( url , season_name )
 elif 'allmyvideos.net' in url :
  ii1iiIi1 ( url , season_name )
 elif 'vidspot.net' in url :
  i111iiI1ii ( url , season_name )
 elif 'vodlocker' in url :
  IIiii ( url , season_name )
 elif 'vidto' in url :
  I1i1i ( url , season_name )
  if 86 - 86: I1ii11iIi11i / o000O0o + o0o00Oo0O * O0OOOoOoo0
  if 19 - 19: IIiIiII11i * I1111IIi + ii1ii11IIIiiI
def I1i1i ( url , season_name ) :
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0ooO00oO , iiI11ii1I1 in i1IIIII11I1IiI :
  i11i1iIiii ( O0ooO00oO , season_name )
  if 71 - 71: Ii1I % I11i1ii1 - oOo0O0Ooo % ooOOOoO - o0o00Oo0O
  if 67 - 67: Ii1IIIi1 + I1ii11iIi11i
def ii1iiIi1 ( url , season_name ) :
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0ooO00oO , iiI11ii1I1 in i1IIIII11I1IiI :
  i11i1iIiii ( O0ooO00oO , season_name )
  if 84 - 84: o0o00Oo0O * ii - I1111IIi * I1111IIi
def i111iiI1ii ( url , season_name ) :
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0OOoo0OO )
 for O0ooO00oO , iiI11ii1I1 in i1IIIII11I1IiI :
  i11i1iIiii ( O0ooO00oO , season_name )
  if 8 - 8: I11i1ii1 / ooOoO0O00 . o000O0o
def IIiii ( url , season_name ) :
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0ooO00oO in i1IIIII11I1IiI :
  i11i1iIiii ( O0ooO00oO , season_name )
  if 41 - 41: O0OOOoOoo0 + oO0o
def oOOOOo0OoO ( url , season_name ) :
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 i1IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0OOoo0OO )
 for O0ooO00oO in i1IIIII11I1IiI :
  i11i1iIiii ( O0ooO00oO , season_name )
  if 86 - 86: OOooOOo . iI11I1II1I1I - oO0o
def oo0o0oooo ( url , season_name ) :
 oO0OOoo0OO = I11o0oO00oO0o0o0 ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0ooO00oO in i1IIIII11I1IiI :
  i11i1iIiii ( O0ooO00oO , season_name )
  if 56 - 56: o0o00Oo0O
def i11i1iIiii ( Link , season_name ) :
 if 'http:/' in Link :
  OOo00 ( Link )
  if 37 - 37: ooOoO0O00
def III1i1iI1 ( url ) :
 oO0OOoo0OO = OPEN_URL_1 ( url )
 o0ooo00o = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 for url in o0ooo00o :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 62 - 62: I1ii11iIi11i * OOooOOo
def I1i11ii11 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0oOOo00O = True
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OO0oIII111i11IiI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0000 = [ ]
  if 64 - 64: IIiIiII11i - oOo0O0Ooo
  if showcontext == 'fav' :
   O0000 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   O0000 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OO0oIII111i11IiI . addContextMenuItems ( O0000 )
 OOO0oOOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = True )
 return OOO0oOOo00O
 if 68 - 68: I11i1ii1 - Ii1IIIi1 - iI11I1II1I1I / OOooOOo + Ii1IIIi1 - oO0o
 if 75 - 75: O0OOOoOoo0 / I11i % iI11I1II1I1I . ii % ii % IIiIiII11i
def o0iiiI1I1iIIIi1 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0oOOo00O = True
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OO0oIII111i11IiI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0000 = [ ]
  O0000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0000 . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   O0000 . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OO0oIII111i11IiI . addContextMenuItems ( O0000 )
 OOO0oOOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = False )
 return OOO0oOOo00O
 if 26 - 26: IIiIiII11i % Ii % iI11I1II1I1I % ooOOOoO * ooOOOoO * Ii1I
def IiI1I11iIii ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 63 - 63: O0OOOoOoo0 * ooOOOoO * ii1ii11IIIiiI - o000O0o - ii1ii11IIIiiI
def o0oo ( url ) :
 oOoOoo0 = xbmc . Player ( ii1II ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oOoOoo0 . play ( url ) . strip ( )
 except : pass
 if 50 - 50: ii1ii11IIIiiI + ooOoO0O00 / o0o00Oo0O / I11i
def OOo00 ( url ) :
 oOoOoo0 = xbmc . Player ( )
 import urlresolver
 try : oOoOoo0 . play ( url )
 except : pass
 if 42 - 42: ooOoO0O00 . oOo0O0Ooo / ooOoO0O00 + ii1ii11IIIiiI
def I11o0oO00oO0o0o0 ( url ) :
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
  if 54 - 54: I11i1ii1 % Ii1IIIi1 . iiiiiiii1 + o000O0o - Ii1IIIi1 * oOo0O0Ooo
  if 92 - 92: I11i + iiiiiiii1 / I1ii11iIi11i % oO0o % I1111IIi . ii
  if 52 - 52: I11i1ii1 / Ii - Ii1IIIi1 . I1111IIi % iI11I1II1I1I + I11i
def OOOOoO00o0O ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OO00oOooo0O ( )
  if iI11iI1IiiIiI == 1 :
   oOOOo ( )
  if iI11iI1IiiIiI == 2 :
   OO0O0o0o0 ( )
  if iI11iI1IiiIiI == 3 :
   iIIIIIiI1I1 ( )
  if iI11iI1IiiIiI == 4 :
   I11I1IIiiII1 ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def II11IiiIII ( ) :
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
 if 31 - 31: oOo0O0Ooo * o000O0o + ii - O0OOOoOoo0 / ii
 if 19 - 19: I1111IIi * I11i1ii1 * I11i + o0o00Oo0O / o0o00Oo0O
 if 73 - 73: iI11I1II1I1I / iI11I1II1I1I - o000O0o
def OO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 i1IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0OOoo0OO )
 for IIiIi1iI in i1IIIII11I1IiI :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   oOoOOOo = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   iiIiI1i1 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + oOoOOOo + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iI11iI1IiiIiI = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iI11iI1IiiIiI == 0 :
    ii1I ( IIiIi1iI )
    oOOo0O00o ( )
   elif iI11iI1IiiIiI == 1 :
    o0OOoOoO00 ( IIiIi1iI )
  else :
   pass
   if 15 - 15: I1111IIi / o0o00Oo0O . I11i . Ii
def o0OOoOoO00 ( addon ) :
 oOoOOOo = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 59 - 59: iiiiiiii1 - I11i - I11i1ii1
def ii1I ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 Ii11iI = os . path . join ( I11II1i , 'default.py' )
 oO00OoOO = open ( Ii11iI , "w+" )
 if 18 - 18: I11i1ii1 - OOooOOo % ooOoO0O00 + o0o00Oo0O + Ii + ooOoO0O00
 oO00OoOO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 oO00OoOO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 oO00OoOO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 91 - 91: OOooOOo + I11i1ii1 . oOo0O0Ooo
 if 71 - 71: O0OOOoOoo0 % I11i / Ii1IIIi1 / I1ii11iIi11i
 if 66 - 66: I1ii11iIi11i - I11i * I1111IIi + OOooOOo + I11i - iI11I1II1I1I
 if 17 - 17: o000O0o
def I1i11ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1ii11 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii1i = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 I1II1 = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oo00OO0000oO = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 IIioo0OO = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , url , i1I1i1 , O0OoooO0 , i11IIIiI1I in i1ii11 :
  if 'php' in url :
   iiOOooooO0Oo ( iiI11ii1I1 , url , 90037 , i1I1i1 , O0OoooO0 , i11IIIiI1I )
  elif iiI11ii1I1 == 'Search' :
   iiOOooooO0Oo ( 'Search' , url , 90038 , i1I1i1 , O0OoooO0 , i11IIIiI1I )
  else :
   OOiIiIIi1 ( iiI11ii1I1 , url , 222 , i1I1i1 , O0OoooO0 , i11IIIiI1I )
 for iiI11ii1I1 , oOo0OOoO0 , url , IiiI11i1I in ii1i :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 90037 , oOo0OOoO0 , IiiI11i1I , '' )
 for iiI11ii1I1 , oOo0OOoO0 , url , IiiI11i1I in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 90037 , oOo0OOoO0 , IiiI11i1I , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , IiiI11i1I in i1I :
  OOiIiIIi1 ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , IiiI11i1I , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , IiiI11i1I in I1II1 :
  OOiIiIIi1 ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , IiiI11i1I , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 , IiiI11i1I in oo00OO0000oO :
  OOiIiIIi1 ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , IiiI11i1I , '' )
 for iiI11ii1I1 , url , oOo0OOoO0 in IIioo0OO :
  OOiIiIIi1 ( iiI11ii1I1 , url , 222 , oOo0OOoO0 , '' , '' )
  I1I11i ( 'tvshows' , 'Media Info 3' )
  if 80 - 80: Ii1IIIi1 / ooOOOoO / OOooOOo + ooOoO0O00 - I1ii11iIi11i
def iIIiiIIi1IiI ( ) :
 I11IIIiIi11 = [ 'serialsearch' , 'moviesearch' ]
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 if i1IiiI1iIi == '' :
  pass
 else :
  for oOOo00O0OOOo in I11IIIiIi11 :
   i11I1I1iiI = I11 + oOOo00O0OOOo + '.php'
   ii1IIIIiI11 = OoOooO ( i11I1I1iiI )
   if ii1IIIIiI11 != 'Opened' :
    IIi = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( ii1IIIIiI11 )
    for iiI11ii1I1 , oOooO0 , i1I1i1 , O0OoooO0 , i11IIIiI1I in IIi :
     if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
      I1i1iii1Ii = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for oOOOoo00 in I1i1iii1Ii :
       if oOOOoo00 == oOooO0 :
        iiI11ii1I1 = '[COLORred]* [/COLOR]' + ( iiI11ii1I1 ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        iI = open ( o00OO00OoO , "a" )
        iI . write ( 'item="' + iiI11ii1I1 + '"\n' )
        iI . close
      if 'php' in oOooO0 :
       iiOOooooO0Oo ( iiI11ii1I1 , oOooO0 , 90037 , i1I1i1 , O0OoooO0 , i11IIIiI1I )
      else :
       OOiIiIIi1 ( iiI11ii1I1 , oOooO0 , 222 , i1I1i1 , O0OoooO0 , i11IIIiI1I )
       if 99 - 99: ooOOOoO - iiiiiiii1 - o000O0o % oO0o
   I1I11i ( 'tvshows' , 'Media Info 3' )
   if 21 - 21: IIiIiII11i % Ii1I . ooOoO0O00 - ii
def iiOOOO0o ( ) :
 oO0OOoo0OO = OoOooO ( 'http://www.tvcatchup.com/channels/' )
 O0 = OoOooO ( 'http://www.djing.com/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img style="" src="([^"]*)" alt="([^"]*)"/>.+?<br/>(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I1iIi1IiI = re . compile ( 'title="([^"]*)".+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( O0 )
 for oOooO0 , oOo0OOoO0 , i1111O0O000OOOo , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLORgold]' + i1111O0O000OOOo + '[/COLOR][COLORwhite] - [COLORsteelblue]' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' ) , 'http://www.tvcatchup.com' + oOooO0 , 90024 , oOo0OOoO0 )
 for IIiiiiiiIi1I1 , oOooO0 , oOo0OOoO0 in i1I1iIi1IiI :
  O0Oo00OoOo ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + oOooO0 , 90024 , oOo0OOoO0 )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 in i1I :
  if 'Submit' in iiI11ii1I1 :
   pass
  elif '&lt;' in iiI11ii1I1 :
   pass
  else :
   OOiIiIIi1 ( '[COLORgold]DJing  [/COLOR][COLORwhite]- [COLORsteelblue]' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 90025 , 'http://www.djing.com' + oOo0OOoO0 , O0o0Oo , '' )
  I1I11i ( 'movies' , 'MAIN' )
def i11ii1Ii1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 if 25 - 25: Ii1IIIi1
 i1IIIII11I1IiI = re . compile ( "file: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  iii1 ( url )
def oOO0o000Oo00o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  iii11II1I ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 5 - 5: OOooOOo - I1111IIi * I1111IIi
def OooOoOo ( ) :
 if 50 - 50: IIiIiII11i * Ii1I / ii1ii11IIIiiI . I11i + I1ii11iIi11i - Ii1IIIi1
 if 18 - 18: OOooOOo % Ii % Ii1I / o000O0o / I11i / ooOoO0O00
 if 48 - 48: OOooOOo + ooOOOoO / I1111IIi + IIiIiII11i
 if 18 - 18: Ii1I
 if 23 - 23: IIiIiII11i
 if 24 - 24: iI11I1II1I1I + iI11I1II1I1I * O0OOOoOoo0
 oO0OOoo0OO = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'yr' in oOooO0 :
   O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + oOooO0 , 10201 , III1iII1I1ii + 'rated.png' )
   if 18 - 18: O0OOOoOoo0 * ooOOOoO - ii1ii11IIIiiI
def II1i1III ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i1iii11i , url , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'id' in url :
   O00oO0 ( ( '[COLORred]RANK [COLORblue]' + i1iii11i + '[COLORred] - [COLORblue]' + iiI11ii1I1 + '[/COLOR]' ) , iiI11ii1I1 , 10202 , III1iII1I1ii + 'rated.png' )
   if 58 - 58: ii1ii11IIIiiI / Ii1IIIi1 + ooOOOoO + I1111IIi
def iii1III1i ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iiiIi = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I11iiIi1i1 = ( url )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 oO000oOo00o0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 II1Iii = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 O0oooo0OoO0oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 IiiiIi1iI1iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 OO00o = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOOOoOO0O = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I11iiIi1i1
 ii11I = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 i1IiIiiiIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 74 - 74: IIiIiII11i + ooOoO0O00 + ii1ii11IIIiiI
 Oo00O0ooOO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 IiiI = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 19 - 19: IIiIiII11i
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( oO000oOo00o0o )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1Iii )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( O0oooo0OoO0oo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OoOOII1i11i1iIi11 = O0o0O00Oo0o0 ( IiiiIi1iI1iI )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 oo0O0oO0O0O = O0o0O00Oo0o0 ( OOOOoOO0O )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOo0O = O0o0O00Oo0o0 ( ii11I )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 I11iIiii1 = O0o0O00Oo0o0 ( i1IiIiiiIIIIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 1 - 1: ii1ii11IIIiiI
 if 48 - 48: o0o00Oo0O + o0o00Oo0O . iiiiiiii1 - I11i1ii1
 o00oo0000 = O0o0O00Oo0o0 ( Oo00O0ooOO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 iIi1IIi1ii = O0o0O00Oo0o0 ( IiiI )
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
 if I11iIiii1 != 'Failed' :
  OooOoOOo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( I11iIiii1 )
  for url , iiI11ii1I1 in OooOoOOo0oO00 :
   O00O = O0o0O00Oo0o0 ( url )
   O0Ooo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( O00O )
   for oO00oOOo0Oo , IIiIIIIii in O0Ooo :
    IIiIIIIii = ( IIiIIIIii . replace ( '.' , ' ' ) )
    if i1IiiI1iIi in IIiIIIIii . lower ( ) :
     if '.mkv' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , url + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.mp4' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , url + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.avi' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , url + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.wav' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , url + oO00oOOo0Oo , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , url + oO00oOOo0Oo , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 40 - 40: o0o00Oo0O
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for url , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in i1I :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 58 - 58: I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 9 - 9: iI11I1II1I1I % Ii1I . Ii1IIIi1 + ii
 if ii1ii1ii != 'Failed' :
  I1II1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for Oo0o , iiI11ii1I1 in I1II1 :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( II1Iii + Oo0o ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  oo00OO0000oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for url , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in oo00OO0000oO :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 93 - 93: Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if OoOOII1i11i1iIi11 != 'Failed' :
  iIii1Ooo0oO0 = [ ]
  IIioo0OO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOOII1i11i1iIi11 )
  for url , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in IIioo0OO :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    if iiI11ii1I1 in iIii1Ooo0oO0 :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
     iIii1Ooo0oO0 . append ( iiI11ii1I1 )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0O0oO0O0O != 'Failed' :
  o0Oo0oOooOoOo = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oo0O0oO0O0O )
  for url , oOo0OOoO0 , iiI11ii1I1 in o0Oo0oOooOoOo :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , oOo0OOoO0 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 49 - 49: Ii1IIIi1 . Ii1I . Ii - IIiIiII11i / ii1ii11IIIiiI
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 62 - 62: Ii1IIIi1
    if 1 - 1: I1111IIi / I1111IIi - Ii
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
    if 38 - 38: iI11I1II1I1I + Ii / Ii % oO0o / I11i1ii1 % ii1ii11IIIiiI
    if 7 - 7: I1111IIi * oOo0O0Ooo + ooOoO0O00 + Ii + I1ii11iIi11i % oOo0O0Ooo
    if 62 - 62: I11i - ii1ii11IIIiiI * OOooOOo - Ii % I11i1ii1
    if 52 - 52: Ii1I % o000O0o - Ii
    if 30 - 30: O0OOOoOoo0 / oO0o + o000O0o
    if 6 - 6: O0OOOoOoo0 . ooOOOoO + ii1ii11IIIiiI . iiiiiiii1
 if o00oo0000 != 'Failed' :
  oOoO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00oo0000 )
  for url , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in oOoO0o :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 46 - 46: iiiiiiii1 % ii1ii11IIIiiI
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 72 - 72: iI11I1II1I1I
    if 45 - 45: I1ii11iIi11i - I11i % iiiiiiii1
    if 38 - 38: iiiiiiii1 % Ii1IIIi1 - ii
    if 87 - 87: oO0o % oOo0O0Ooo
    if 77 - 77: iI11I1II1I1I - ooOoO0O00 . o000O0o
    if 26 - 26: I11i * I1111IIi . ooOoO0O00
    if 59 - 59: o0o00Oo0O + ooOoO0O00 - I11i
    if 62 - 62: Ii % Ii1IIIi1 . I1111IIi . Ii1IIIi1
    if 84 - 84: Ii * oO0o
    if 18 - 18: Ii1IIIi1 - ii1ii11IIIiiI - OOooOOo / iiiiiiii1 - o0o00Oo0O
 iiIIii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 70 - 70: I11i - Ii1IIIi1
 for oOOo00O0OOOo in iiIIii :
  i11I1I1iiI = O0Oo000ooO00 + oOOo00O0OOOo + I1IIIii
  I11iIiii1 = O0o0O00Oo0o0 ( i11I1I1iiI )
  if I11iIiii1 != 'Failed' :
   OooOoOOo0oO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11iIiii1 )
   for url , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in OooOoOOo0oO00 :
    if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 62 - 62: ooOOOoO
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 63 - 63: Ii1IIIi1 + I11i1ii1 * o000O0o / I11i / I1ii11iIi11i * iI11I1II1I1I
 iiIIii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 57 - 57: OOooOOo - o000O0o / I11i1ii1 % Ii
 if 3 - 3: O0OOOoOoo0 . I11i1ii1 % oOo0O0Ooo + Ii1I
 for oOOo00O0OOOo in iiIIii :
  i11I1I1iiI = iiiIi + oOOo00O0OOOo
  oo0o = O0o0O00Oo0o0 ( i11I1I1iiI )
  if oo0o != 'Failed' :
   o0IiiiI111I = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0o )
   for Oo0o , iiI11ii1I1 in o0IiiiI111I :
    if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
     O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iiiIi + oOOo00O0OOOo + Oo0o ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 49 - 49: I11i * ii1ii11IIIiiI + ooOOOoO + O0OOOoOoo0
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: I11i / Ii1IIIi1 / I1111IIi % I11i1ii1 + IIiIiII11i
def O0ooO0OoO00o ( ) :
 O00oO0 ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , III1iII1I1ii + 'running.png' )
 O00oO0 ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , III1iII1I1ii + 'countdown.png' )
 O00oO0 ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , III1iII1I1ii + 'unknown.png' )
 O00oO0 ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , III1iII1I1ii + 'cancelled.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 4 - 4: O0OOOoOoo0 - I1ii11iIi11i - I1111IIi - ooOOOoO % Ii / oO0o
def i1iii11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , OoOo00o0OO , oOo0O0o0000o0O0 , I1iii , o0OoOoOOoOo0o in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLORblue]' + iiI11ii1I1 + '[/COLOR] [COLORred]Season[/COLOR]-' + OoOo00o0OO + ' [COLORred]Returns [/COLOR]- ' + o0OoOoOOoOo0o + ' ' + I1iii ) , iiI11ii1I1 , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 20 - 20: oO0o / iI11I1II1I1I
def iIooo0oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , OoOo00o0OO , oOo0O0o0000o0O0 in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLORblue]' + iiI11ii1I1 + '[/COLOR] [COLORred]Season[/COLOR]-' + OoOo00o0OO + ' [COLORred] Status Unknown[/COLOR] ' ) , iiI11ii1I1 , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
def iI11Ii111 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , OoOo00o0OO , oOo0O0o0000o0O0 , I1iii in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLORblue]' + iiI11ii1I1 + ' [COLORred] Cancelled On[/COLOR] ' + I1iii ) , iiI11ii1I1 , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 54 - 54: OOooOOo % O0OOOoOoo0 . OOooOOo * Ii1IIIi1 + OOooOOo % ooOoO0O00
def I1I1I11Ii ( url ) :
 I11iiIi1i1 = ( url )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 if 48 - 48: ii + o000O0o % iI11I1II1I1I
 if 11 - 11: oOo0O0Ooo % ii1ii11IIIiiI - oO0o - o000O0o + I11i
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 oO000oOo00o0o = 'http://onlinemovies.tube/?s=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 II1Iii = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 O0oooo0OoO0oo = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 OO00o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 98 - 98: O0OOOoOoo0 + ii1ii11IIIiiI - oO0o
 ii11I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 i1IiIiiiIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 OOo0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 58 - 58: OOooOOo - O0OOOoOoo0 - ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 96 - 96: iI11I1II1I1I
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 82 - 82: OOooOOo + o0o00Oo0O - I1111IIi % o000O0o * Ii
 if 15 - 15: I11i
 I1iI = O0o0O00Oo0o0 ( oO00oOOo0Oo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( oO000oOo00o0o )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1Iii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( O0oooo0OoO0oo )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 oo0o = O0o0O00Oo0o0 ( OO00o )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 92 - 92: oO0o * I11i1ii1
 if 35 - 35: Ii
 oOo0O = O0o0O00Oo0o0 ( ii11I )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 I11iIiii1 = O0o0O00Oo0o0 ( i1IiIiiiIIIIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 ooO = O0o0O00Oo0o0 ( OOo0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 55 - 55: ooOOOoO
 if I11iIiii1 != 'Failed' :
  OooOoOOo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( I11iIiii1 )
  for url , iiI11ii1I1 in OooOoOOo0oO00 :
   O00O = O0o0O00Oo0o0 ( url )
   O0Ooo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( O00O )
   for oO00oOOo0Oo , IIiIIIIii in O0Ooo :
    if i1IiiI1iIi in IIiIIIIii . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , url + oO00oOOo0Oo , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 83 - 83: I1111IIi * ooOOOoO / I1ii11iIi11i
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if oOo0O != 'Failed' :
  iIIIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo0O )
  for url , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in iIIIiI :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 93 - 93: I11i1ii1 . iI11I1II1I1I % Ii . OOooOOo % I11i1ii1 + o0o00Oo0O
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 65 - 65: ii1ii11IIIiiI + oO0o - ii
    if 51 - 51: I1ii11iIi11i + o000O0o / O0OOOoOoo0 - ooOoO0O00
    if 51 - 51: I1ii11iIi11i - Ii1I * ooOOOoO
    if 12 - 12: iI11I1II1I1I % I11i1ii1 % I11i1ii1
    if 78 - 78: I1111IIi . OOooOOo . ooOOOoO
    if 97 - 97: o000O0o
    if 80 - 80: oOo0O0Ooo . ii1ii11IIIiiI
    if 47 - 47: ooOOOoO + I11i1ii1 + IIiIiII11i % Ii
    if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / O0OOOoOoo0 * o000O0o
    if 29 - 29: I11i
    if 86 - 86: IIiIiII11i . I1111IIi
 if ooO != 'Failed' :
  iIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO )
  for url , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in iIiI :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    O00oO0 ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , I1iIi1iIiiIiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 81 - 81: OOooOOo % ii1ii11IIIiiI
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  oo0 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for url , oOo0OOoO0 , iiI11ii1I1 , i1iIIi1II1iiI in i1I :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    if 'season' in i1iIIi1II1iiI :
     O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , oOo0OOoO0 , oOo0OOoO0 , '' )
    if 'episodes' in i1iIIi1II1iiI :
     O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , oOo0OOoO0 , oOo0OOoO0 , '' )
  for url in oo0 :
   O00oO0 ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 31 - 31: I11i % ooOOOoO + iI11I1II1I1I + Ii * iiiiiiii1
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if I1iI != 'Failed' :
  ii1i = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1iI )
  for url , iiI11ii1I1 , oOo0OOoO0 in ii1i :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( iiI11ii1I1 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , oOo0OOoO0 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 45 - 45: Ii1IIIi1 * iiiiiiii1 . I11i1ii1 - iiiiiiii1 + I1111IIi
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: Ii1IIIi1 . I1ii11iIi11i
    if 78 - 78: Ii1I % oOo0O0Ooo / ii % Ii1IIIi1 - O0OOOoOoo0
    if 2 - 2: iI11I1II1I1I
    if 45 - 45: ii / Ii
    if 10 - 10: O0OOOoOoo0 - o000O0o * iI11I1II1I1I % iI11I1II1I1I * I1111IIi - Ii1I
    if 97 - 97: IIiIiII11i % iiiiiiii1 + iiiiiiii1 - oO0o / ii1ii11IIIiiI * oOo0O0Ooo
    if 17 - 17: ii1ii11IIIiiI
    if 39 - 39: I11i1ii1 . IIiIiII11i
    if 45 - 45: o000O0o * OOooOOo / iI11I1II1I1I
 if ii1ii1ii != 'Failed' :
  I1II1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for iiI11ii1I1 in I1II1 :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( II1Iii + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 77 - 77: iiiiiiii1 - ooOOOoO
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  oo00OO0000oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for iiI11ii1I1 in oo00OO0000oO :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( O0oooo0OoO0oo + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 11 - 11: Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  o0IiiiI111I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0o )
  for url , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in o0IiiiI111I :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 26 - 26: iI11I1II1I1I * iiiiiiii1 - Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 27 - 27: Ii1I * iiiiiiii1 - oO0o + ii1ii11IIIiiI * ii1ii11IIIiiI
 o0OO0O0OO0oO0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oOOo00O0OOOo in o0OO0O0OO0oO0 :
  i11I1I1iiI = O0Oo000ooO00 + oOOo00O0OOOo + I1IIIii
  o00oo0000 = O0o0O00Oo0o0 ( i11I1I1iiI )
  if o00oo0000 != 'Failed' :
   oOoO0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00oo0000 )
   for iiI11ii1I1 , i11IIIiI1I , url , oOo0OOoO0 , O0OoooO0 , I1I in oOoO0o :
    if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] - Source Pandoras[/COLOR]' , url , I1I , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 9 - 9: o000O0o % Ii / I1ii11iIi11i
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 20 - 20: o000O0o * o0o00Oo0O + ooOOOoO - ii . ooOOOoO
     if 60 - 60: I11i . I11i / O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 45 - 45: o0o00Oo0O . Ii % O0OOOoOoo0 . OOooOOo % I1111IIi % iI11I1II1I1I
def Oo ( ) :
 oO0OOoo0OO = OoOooO ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( iiI11ii1I1 ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + oOooO0 , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + oOooO0 )
def oo0oooo0OoO0o ( url ) :
 I1I1 = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( I1I1 )
 sys . exit ( 1 )
 if 99 - 99: I11i1ii1 / iI11I1II1I1I - ii1ii11IIIiiI * Ii1I % oOo0O0Ooo
def i1II1i ( ) :
 if 10 - 10: ii1ii11IIIiiI - OOooOOo . ii . Ii1IIIi1 . oO0o * O0OOOoOoo0
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
 O00oO0 ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , III1iII1I1ii + 'seasons.png' )
 O00oO0 ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , III1iII1I1ii + 'episodes.png' )
 O00oO0 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 6 - 6: I1111IIi
def i1I1II ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , Ii1I1I1i11ii in i1IIIII11I1IiI :
  O00oO0 ( ( iiI11ii1I1 + ' - ' + Ii1I1I1i11ii ) . replace ( '&amp;' , '&' ) , url , 90053 , III1iII1I1ii + 'seasons.png' )
  if 58 - 58: iI11I1II1I1I - Ii - Ii * ii1ii11IIIiiI + I11i . OOooOOo
def OoOo00o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , url , 90054 , III1iII1I1ii + 'episodes.png' )
  if 30 - 30: OOooOOo . ooOOOoO / ooOOOoO * Ii
def II1III1i1iiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , iiI11ii1I1 , url in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , url , 90054 , oOo0OOoO0 )
 for url in next :
  O00oO0 ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 27 - 27: ii1ii11IIIiiI - o0o00Oo0O % ooOOOoO * iiiiiiii1 . I1111IIi % iI11I1II1I1I
def IiIi1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , Ii1I1I1i11ii , url , iiI11ii1I1 , oO0O0oO in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Ii1I1I1i11ii + ' - ' + iiI11ii1I1 + ' - ' + oO0O0oO , url , 90044 , oOo0OOoO0 , oOo0OOoO0 , '' )
 for oOo0OOoO0 , iiI11ii1I1 , url in i1I :
  O00oO0 ( iiI11ii1I1 , url , 90044 , oOo0OOoO0 , oOo0OOoO0 , '' )
 for url in next :
  O00oO0 ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 27 - 27: o0o00Oo0O / OOooOOo + iI11I1II1I1I - Ii1IIIi1 % I11i
def I111i1Ii1i1 ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI1IIi1IiI = 'http://onlinemovies.tube/?s=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 i1IiiI1iIi = iI1IIi1IiI . lower ( )
 oO0OOoo0OO = OoOooO ( i1IiiI1iIi )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 , i1iIIi1II1iiI in i1IIIII11I1IiI :
  if 'season' in i1iIIi1II1iiI :
   O00oO0 ( iiI11ii1I1 , oOooO0 , 90054 , oOo0OOoO0 , oOo0OOoO0 , '' )
  if 'episodes' in i1iIIi1II1iiI :
   O00oO0 ( iiI11ii1I1 , oOooO0 , 90044 , oOo0OOoO0 , oOo0OOoO0 , '' )
 for oOooO0 in next :
  O00oO0 ( 'NEXT' , oOooO0 , 90053 , III1iII1I1ii + 'Next.png' )
  if 45 - 45: o0o00Oo0O / ooOoO0O00 * o000O0o * oO0o
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
 O00oO0 ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , III1iII1I1ii + 'allmov.png' )
 O00oO0 ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , III1iII1I1ii + 'Genre.png' )
 O00oO0 ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , III1iII1I1ii + 'Years.png' )
 O00oO0 ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 20 - 20: iiiiiiii1 - iiiiiiii1
def iIIiI11i1I11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , Ii1I1I1i11ii in i1IIIII11I1IiI :
  if 'genre' in url :
   O00oO0 ( ( iiI11ii1I1 + ' - ' + Ii1I1I1i11ii ) . replace ( '&amp;' , '&' ) , url , 90043 , III1iII1I1ii + 'Genre.png' )
   if 29 - 29: oO0o * iI11I1II1I1I * o0o00Oo0O - OOooOOo / I1111IIi
def o0oO0OO00ooOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'release' in url :
   O00oO0 ( iiI11ii1I1 , url , 90043 , III1iII1I1ii + 'Years.png' )
   if 5 - 5: oOo0O0Ooo * OOooOOo - Ii . I11i1ii1 / O0OOOoOoo0
def III1iii1i1II ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , iiI11ii1I1 , O0oOO0o , url , i11IIIiI1I in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 + ' ' + O0oOO0o , url , 90044 , oOo0OOoO0 , oOo0OOoO0 , i11IIIiI1I )
 for oOo0OOoO0 , iiI11ii1I1 , i1iIIi1II1iiI , url , iiiiI1IiI1I1 , i11IIIiI1I in i1I :
  if 'movies' in i1iIIi1II1iiI :
   iiOOooooO0Oo ( iiI11ii1I1 + ' - ' + iiiiI1IiI1I1 , url , 90044 , oOo0OOoO0 , oOo0OOoO0 , i11IIIiI1I )
 for url in next :
  O00oO0 ( 'NEXT' , url , 90043 , III1iII1I1ii + 'Next.png' )
  if 19 - 19: ii1ii11IIIiiI
def O0o00oO0oOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  iiiii1I1III1 ( 'http:' + url )
  if 12 - 12: O0OOOoOoo0 . OOooOOo * oOo0O0Ooo
def iiiii1I1III1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( iiI11ii1I1 ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , III1iII1I1ii + 'movhub.png' )
def II1I1i1i1iii ( ) :
 if 14 - 14: Ii1IIIi1
 if 79 - 79: ii1ii11IIIiiI
 if 76 - 76: iI11I1II1I1I
 if 80 - 80: iI11I1II1I1I . o0o00Oo0O / ii1ii11IIIiiI % ii1ii11IIIiiI
 if 93 - 93: ii * I1ii11iIi11i
 if 10 - 10: iiiiiiii1 * ii + ooOOOoO - Ii1I / Ii1I . Ii
 if 22 - 22: iiiiiiii1 / I11i
 if 98 - 98: ooOoO0O00
 if 51 - 51: Ii1I + I11i1ii1 + I1ii11iIi11i / ooOoO0O00 + ooOoO0O00
 if 12 - 12: iI11I1II1I1I . ii1ii11IIIiiI . Ii1I % oOo0O0Ooo . IIiIiII11i . o000O0o
 if 32 - 32: Ii1I + I1111IIi / o0o00Oo0O / OOooOOo * ii % I11i1ii1
 if 50 - 50: oO0o
 if 66 - 66: iI11I1II1I1I
 if 41 - 41: iiiiiiii1 . o0o00Oo0O * oOo0O0Ooo * Ii1I
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI1IIi1IiI = 'http://onlinemovies.tube/?s=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 i1IiiI1iIi = iI1IIi1IiI . lower ( )
 oO0OOoo0OO = OoOooO ( i1IiiI1iIi )
 i1IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 , o0o0Oo0OOOOO in i1IIIII11I1IiI :
  if 'movies' in o0o0Oo0OOOOO :
   O00oO0 ( o0o0Oo0OOOOO + '-' + iiI11ii1I1 , oOooO0 , 90044 , oOo0OOoO0 )
 for oOooO0 in next :
  III1iii1i1II ( oOooO0 )
  if 49 - 49: iI11I1II1I1I % IIiIiII11i
def i1Iii11I1i ( ) :
 O00oO0 ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 oO0OOoo0OO = OoOooO ( 'http://www.join4films.com/' )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , oOooO0 , 80006 , III1iII1I1ii + 'Desi.png' )
def Iii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oO0OOoo0OO )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( iiI11ii1I1 , url , 80007 , oOo0OOoO0 )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def II1iIii111iII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  iii1 ( url )
def iI1iI1IiIIiI ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI1IIi1IiI = 'http://www.join4films.com/?s=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1IiiI1iIi = iI1IIi1IiI . lower ( )
 Iii ( i1IiiI1iIi )
 if 87 - 87: OOooOOo % iI11I1II1I1I
 if 72 - 72: Ii1IIIi1 . Ii1IIIi1 - Ii1I
 if 48 - 48: I1ii11iIi11i - I11i1ii1 + I1ii11iIi11i - oOo0O0Ooo * Ii . O0OOOoOoo0
 if 35 - 35: I1111IIi . o0o00Oo0O + I1ii11iIi11i + Ii1IIIi1 + ooOoO0O00
 if 65 - 65: o0o00Oo0O * oOo0O0Ooo / oOo0O0Ooo . OOooOOo
 if 87 - 87: IIiIiII11i * Ii1I % I1ii11iIi11i * I1ii11iIi11i
 if 58 - 58: Ii1IIIi1 . I11i + oOo0O0Ooo % I1ii11iIi11i - oO0o
 if 50 - 50: O0OOOoOoo0 % IIiIiII11i - I11i1ii1 . ooOoO0O00 + o0o00Oo0O % O0OOOoOoo0
 if 10 - 10: O0OOOoOoo0 . ooOoO0O00 + ii1ii11IIIiiI
 if 66 - 66: oO0o % I11i
 if 21 - 21: OOooOOo - ii % Ii
 if 71 - 71: ooOoO0O00 - ooOOOoO * iiiiiiii1 + o000O0o - oO0o % Ii1I
 if 63 - 63: iI11I1II1I1I + Ii1IIIi1 . oO0o / oOo0O0Ooo
 if 84 - 84: ooOoO0O00
 if 42 - 42: IIiIiII11i - oO0o - ii . O0OOOoOoo0 / OOooOOo
 if 56 - 56: Ii - iI11I1II1I1I . IIiIiII11i
 if 81 - 81: I1111IIi / OOooOOo * I1111IIi . o0o00Oo0O
def OOOOo00oo00O ( ) :
 iiOOooooO0Oo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 if 83 - 83: IIiIiII11i * ooOoO0O00 * O0OOOoOoo0 . Ii1I / ooOOOoO + ooOoO0O00
def i1Ii ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI1IIi1IiI = 'http://imoviemax.se/?s=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 i1IiiI1iIi = iI1IIi1IiI . lower ( )
 o0oO00 ( i1IiiI1iIi )
def O00o0O ( url ) :
 O00oOo0O0o00O = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , ooo0oo00O00Oo in i1IIIII11I1IiI :
  if iiI11ii1I1 in O00oOo0O0o00O :
   pass
  else :
   iiOOooooO0Oo ( iiI11ii1I1 + ' - ' + ooo0oo00O00Oo + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
   O00oOo0O0o00O . append ( iiI11ii1I1 )
   if 87 - 87: OOooOOo * O0OOOoOoo0 + I1111IIi % O0OOOoOoo0 % Ii1IIIi1
def o00OooOO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , iiiiI1111 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 + ' - Views:' + iiiiI1111 , url , 10075 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
  if 69 - 69: OOooOOo / IIiIiII11i % O0OOOoOoo0 % ii % oO0o
  if 19 - 19: I1111IIi * iiiiiiii1 / o000O0o * iiiiiiii1 - ii * ooOOOoO
def o0oO00 ( url ) :
 iiiI1i1 = [ ]
 oO0OOoo0OO = OoOooO ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0OOoo0OO )
 for next in next :
  iiOOooooO0Oo ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , iiI11ii1I1 , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 10075 , oOo0OOoO0 , oOo0OOoO0 , '' )
  iiiI1i1 . append ( iiI11ii1I1 )
  if 44 - 44: Ii1IIIi1 + ooOOOoO . I1111IIi / IIiIiII11i % iI11I1II1I1I + I1111IIi
def O0OOo ( img , name , url ) :
 img = img
 name = name
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oO0OOoo0OO )
 for i1I1Iiii1 , url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  O0ooooo000 = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + O0ooooo000
  OooOoOO0OO = ( i1I1Iiii1 ) . replace ( 'play-' , 'Server ' )
  OOiIiIIi1 ( OooOoOO0OO , O0ooooo000 , 10076 , img , img , '' )
  if 27 - 27: I1111IIi * oOo0O0Ooo . iI11I1II1I1I - iI11I1II1I1I
def i111i1I1ii1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oO0OOoo0OO )
 for oO000oOo00o0o in i1IIIII11I1IiI :
  if '=m' in oO000oOo00o0o :
   O0OoooI11iI1I ( oO000oOo00o0o )
  elif 'php' in oO000oOo00o0o :
   i111i1I1ii1i ( url )
  else :
   oO0OOoo0OO = OoOooO ( oO000oOo00o0o )
   i1IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( oO0OOoo0OO )
   for II1Iii in i1IIIII11I1IiI :
    O0OoooI11iI1I ( oO000oOo00o0o )
    if 50 - 50: iI11I1II1I1I * I1111IIi . ii / IIiIiII11i - Ii1I * Ii1I
    if 98 - 98: oO0o - ii1ii11IIIiiI . I1111IIi % Ii
    if 69 - 69: Ii1I + O0OOOoOoo0 * o0o00Oo0O . Ii1IIIi1 % OOooOOo
def O0O000O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iiii1IIi1 = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iii , oo0o0OoOO0o0 in iiii1IIi1 :
  print 'there ><><><><><><><><><><><><'
  I1iii = I1iii
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( oo0o0OoOO0o0 ) )
  for iiI11ii1I1 , III1III11II in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + I1iii + '[/COLOR] - ' + iiI11ii1I1 + ' - [COLOR' + II + ']' + III1III11II + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
 iI1I1i11iIIii = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iii , iIi1iI in iI1I1i11iIIii :
  print 'there ><><><><><><><><><><><><'
  I1iii = I1iii
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( iIi1iI ) )
  for iiI11ii1I1 , III1III11II in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + I1iii + '[/COLOR] - ' + iiI11ii1I1 + ' - [COLOR' + II + ']' + III1III11II + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
   if 63 - 63: oO0o / OOooOOo * iI11I1II1I1I . iiiiiiii1
   if 85 - 85: Ii / Ii . oO0o . o0o00Oo0O
   if 67 - 67: IIiIiII11i / I11i . Ii1IIIi1 . ii
def O0OoOO0oo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iI1I1i11iIIii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iI1I1i11iIIii in iI1I1i11iIIii :
  iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iI1I1i11iIIii ) )
  for iiI11ii1I1 in iiI11ii1I1 :
   iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iI1I1i11iIIii ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  ooooo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iI1I1i11iIIii ) )
  for ooooo in ooooo :
   ooooo = 'http:' + ooooo
  OOiIiIIi1 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooooo , '' , '' )
  if 19 - 19: I1111IIi . Ii1I / OOooOOo
  if 68 - 68: I11i1ii1 / ii * ooOOOoO / o000O0o
  if 88 - 88: I11i
  if 1 - 1: ii
def Oo00o0OO0O00o ( url ) :
 if 48 - 48: I11i1ii1 * OOooOOo - I11i1ii1 - Ii1IIIi1 + Ii1IIIi1
 iii = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO000oOo00o0o , oOo0OOoO0 , iiI11ii1I1 , IiIIII1iiIIi in i1IIIII11I1IiI :
  iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = OoOooO ( oO000oOo00o0o )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for o0ooo00o , oOOo000oOoO0 in i1I :
   i1I1IiI1ii = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( oOOo000oOoO0 ) )
   for i11IIIiI1I in i1I1IiI1ii :
    if iiI11ii1I1 in iii :
     pass
    else :
     OOiIiIIi1 ( iiI11ii1I1 , o0ooo00o , 8043 , oOo0OOoO0 , oOo0OOoO0 , i11IIIiI1I )
     I1I11i ( 'movies' , 'INFO' )
     iii . append ( iiI11ii1I1 )
     if 64 - 64: O0OOOoOoo0 * Ii1I % IIiIiII11i - OOooOOo + Ii1I
     if 62 - 62: OOooOOo % I11i % oOo0O0Ooo + I1111IIi . oO0o
def iI1iiiIii1II1 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , I1iIi1iIiiIiI , i11IIIiI1I , O0OoooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 10065 , I1iIi1iIiiIiI , O0OoooO0 , i11IIIiI1I )
 I1I11i ( 'movies' , 'INFO' )
 if 66 - 66: IIiIiII11i
def O00000Oo00o ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI1IIi1IiI = 'https://www.youtube.com/results?search_query=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 i1IiiI1iIi = iI1IIi1IiI . lower ( )
 oO0OOoo0OO = OoOooO ( i1IiiI1iIi )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in next :
  oOooO0 = 'https://www.youtube.com' + oOooO0
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , oOooO0 , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for oOo0OOoO0 , oOooO0 , iiI11ii1I1 , II1 , oOOo000oOoO0 in i1IIIII11I1IiI :
  OOOO . append ( iiI11ii1I1 )
  I1I11i ( 'tvshows' , 'INFO' )
  ooooo = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooooo
  oOooO0 = 'http://www.youtube.com' + oOooO0
  OOiIiIIi1 ( '[COLORred]' + II1 + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooooo , ooooo , oOOo000oOoO0 )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oOo0OOoO0 , oOooO0 , iiI11ii1I1 , II1 in i1IIIII11I1IiI :
   print 'im doing it'
   I1I11i ( 'tvshows' , 'INFO' )
   ooooo = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
   oOooO0 = 'http://www.youtube.com' + oOooO0
   if '&' in oOooO0 :
    print ' i got here'
    oO0OOoo0OO = OoOooO ( oOooO0 )
    iI1I1i11iIIii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for iI1I1i11iIIii in iI1I1i11iIIii :
     iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iI1I1i11iIIii ) )
     for iiI11ii1I1 in iiI11ii1I1 :
      iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oOooO0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iI1I1i11iIIii ) )
     for oOooO0 in oOooO0 :
      oOooO0 = 'https://www.youtube.com/w' + oOooO0
     ooooo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iI1I1i11iIIii ) )
     for ooooo in ooooo :
      ooooo = 'http:' + ooooo
     OOiIiIIi1 ( '[COLORred]' + II1 + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooooo , O0o0Oo , '' )
   elif iiI11ii1I1 in OOOO :
    pass
   elif 'user' in oOooO0 or 'elete' in iiI11ii1I1 :
    pass
   elif 'hannel' in oOooO0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oOooO0
    oO0OOoo0OO = OoOooO ( oOooO0 )
    iio00 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for oOo0OOoO0 , oOooO0 , iiI11ii1I1 in iio00 :
     if 'outube' in oOooO0 or 'list' in oOooO0 :
      pass
     elif 'atch' in oOooO0 :
      oOooO0 = ( oOooO0 ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + II1 + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0OOoO0 , 'http:' + oOo0OOoO0 , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + II1 + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooooo , ooooo , '' )
    if 4 - 4: oO0o
def ooOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for oOo0OOoO0 , url , iiI11ii1I1 , II1 , oOOo000oOoO0 in i1IIIII11I1IiI :
  OOOO . append ( iiI11ii1I1 )
  I1I11i ( 'tvshows' , 'INFO' )
  ooooo = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + ooooo
  url = 'http://www.youtube.com' + url
  OOiIiIIi1 ( '[COLORred]' + II1 + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooooo , ooooo , oOOo000oOoO0 )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oOo0OOoO0 , url , iiI11ii1I1 , II1 in i1IIIII11I1IiI :
   I1I11i ( 'tvshows' , 'INFO' )
   ooooo = 'http:' + ( oOo0OOoO0 ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oO0OOoo0OO = OoOooO ( url )
    iI1I1i11iIIii = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for iI1I1i11iIIii in iI1I1i11iIIii :
     iiI11ii1I1 = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( iI1I1i11iIIii ) )
     for iiI11ii1I1 in iiI11ii1I1 :
      iiI11ii1I1 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( iI1I1i11iIIii ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     ooooo = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( iI1I1i11iIIii ) )
     for ooooo in ooooo :
      ooooo = 'http:' + ooooo
     OOiIiIIi1 ( '[COLORred]' + II1 + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooooo , O0o0Oo , '' )
   elif iiI11ii1I1 in OOOO :
    pass
   elif 'user' in url or 'elete' in iiI11ii1I1 :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0OOoo0OO = OoOooO ( url )
    iio00 = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for oOo0OOoO0 , url , iiI11ii1I1 in iio00 :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + II1 + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + oOo0OOoO0 , 'http:' + oOo0OOoO0 , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + II1 + '[/COLOR]' + '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooooo , ooooo , '' )
    if 5 - 5: ii / I11i % ooOOOoO % oO0o * O0OOOoOoo0 + iI11I1II1I1I
def I11iiI11iiI ( ) :
 Oo0oO ( )
 OOOII1i1II ( )
 if 9 - 9: I1ii11iIi11i % ii - ii1ii11IIIiiI
 if 43 - 43: oO0o % oO0o
 iiOOooooO0Oo ( '[COLOR' + II + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o , 60004 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 IIiii11ii1i ( '[COLORsteelblue]VOD Lists[/COLOR]' , '' , 40000 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
 if 7 - 7: o000O0o - o0o00Oo0O * ooOOOoO - I11i - IIiIiII11i
 if 41 - 41: oOo0O0Ooo - iiiiiiii1 % IIiIiII11i . iiiiiiii1 - ooOOOoO
 if 45 - 45: ii1ii11IIIiiI - Ii1IIIi1
def OOoooO00o0o ( ) :
 IIiii11ii1i ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , I1ii1Ii1 + '&action=get_vod_streams' , 40001 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( OoOoO )
 i1IIIII11I1IiI = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLORsteelblue]' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOooO0 , 40001 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
def iI111I1III ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( i111IiiI1Ii + url )
 i1IIIII11I1IiI = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg .+?,"container_extension":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , type , oO000oOo00o0o , i1I1i1 , OooOOOOOo in i1IIIII11I1IiI :
  OOiIiIIi1 ( iiI11ii1I1 , i1I11ii + oO000oOo00o0o + '.' + OooOOOOOo , 222 , ( i1I1i1 ) . replace ( '\/' , '/' ) + 'jpg' , O0o0Oo , 'Type: ' + type )
  if 72 - 72: ooOOOoO
def OOOII1i1II ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  oO00 ( )
  if 37 - 37: oO0o - Ii1I . ii . I11i1ii1 + OOooOOo / ii1ii11IIIiiI
  if 15 - 15: I1111IIi . ooOoO0O00 * OOooOOo % iI11I1II1I1I
  if 35 - 35: Ii1I + iiiiiiii1 - OOooOOo % o000O0o % I11i % OOooOOo
  if 45 - 45: oOo0O0Ooo * Ii1IIIi1 % oO0o
  if 24 - 24: I11i1ii1 - ooOOOoO * o000O0o
  if 87 - 87: ii1ii11IIIiiI - Ii1I % Ii1I . o000O0o / Ii1I
  if 6 - 6: OOooOOo / iI11I1II1I1I * ii * Ii
  if 79 - 79: I1111IIi % oO0o
def oO00 ( ) :
 i1i = OoOooO ( 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 for oOooO0 in i1IIIII11I1IiI :
  Oo0oOO = datetime . fromtimestamp ( float ( i1IIIII11I1IiI [ 0 ] ) )
  Oo0oOO . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= Oo0oOO <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   OOooO0OOoo . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + II + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + II + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + II + '] To Purchase A licence[/COLOR]' )
def oooooiIiIi ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"username":"(.+?)"' ) . findall ( i1i )
 iiIiI1 = re . compile ( '"password":"(.+?)"' ) . findall ( i1i )
 ii1i = re . compile ( '"status":"(.+?)"' ) . findall ( i1i )
 i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 I1II1 = re . compile ( '"active_cons":"(.+?)"' ) . findall ( i1i )
 oo00OO0000oO = re . compile ( '"created_at":"(.+?)"' ) . findall ( i1i )
 IIioo0OO = re . compile ( '"max_connections":"(.+?)"' ) . findall ( i1i )
 o0IiiiI111I = re . compile ( '"is_trial":"1"' ) . findall ( i1i )
 o0Oo0oOooOoOo = re . compile ( '"is_trial":"0"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']My GTV Account Information[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  O0Oo00OoOo ( '[COLOR' + II + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in iiIiI1 :
  O0Oo00OoOo ( '[COLOR' + II + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in ii1i :
  O0Oo00OoOo ( '[COLOR' + II + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in oo00OO0000oO :
  Oo0oOO = datetime . fromtimestamp ( float ( oo00OO0000oO [ 0 ] ) )
  Oo0oOO . strftime ( '%Y-%m-%d %H:%M:%S' )
  O0Oo00OoOo ( '[COLOR' + II + ']Created:[/COLOR]  %s' % ( Oo0oOO ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in i1I :
  Oo0oOO = datetime . fromtimestamp ( float ( i1I [ 0 ] ) )
  Oo0oOO . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= Oo0oOO <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   O0Oo00OoOo ( '[COLORred]Expires Today[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  O0Oo00OoOo ( '[COLOR' + II + ']Expires:[/COLOR]  %s' % ( Oo0oOO ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in I1II1 :
  O0Oo00OoOo ( '[COLOR' + II + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in IIioo0OO :
  O0Oo00OoOo ( '[COLOR' + II + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in o0IiiiI111I :
  O0Oo00OoOo ( '[COLOR' + II + ']Trial:[/COLOR] Yes' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in o0Oo0oOooOoOo :
  O0Oo00OoOo ( '[COLOR' + II + ']Trial:[/COLOR] No' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 O0Oo00OoOo ( '' , '' , '' , '' )
 O0Oo00OoOo ( '' , '' , '' , '' )
 O0Oo00OoOo ( '[COLOR' + II + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 13 - 13: Ii1I % OOooOOo
def ooOii1i11 ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
 IiIiIi1I11I ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 43 - 43: Ii + O0OOOoOoo0 + I11i1ii1 / iiiiiiii1 . Ii1I + O0OOOoOoo0
I1ii1Ii1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( II11iiii1Ii , OO0o )
i1I11ii = 'http://piesustv.net:8000/movie/%s/%s/' % ( II11iiii1Ii , OO0o )
iIIi1IiIi = 'http://piesustv.net:8000/live/%s/%s/' % ( II11iiii1Ii , OO0o )
III1i = '&action=get_live_categories'
o0Oo0 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( II11iiii1Ii , OO0o )
OoOoO = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( II11iiii1Ii , OO0o )
i111IiiI1Ii = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_streams&category_id=' % ( II11iiii1Ii , OO0o )
ii1IiI11I = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( II11iiii1Ii , OO0o )
OO0Ooo000O0 = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( II11iiii1Ii , OO0o )
if 83 - 83: ii1ii11IIIiiI / Ii % OOooOOo
def ooo0ii1iIIi11 ( ) :
 iiOOooooO0Oo ( ( '[COLORsteelblue]Full List[/COLOR]' ) . replace ( '\/' , ' - ' ) , I1ii1Ii1 + '&action=get_live_streams' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( ( '[COLORsteelblue]PPV Wrestling[/COLOR]' ) . replace ( '\/' , ' - ' ) , '23' , 600033 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( ( '[COLORsteelblue]PPV Boxing[/COLOR]' ) . replace ( '\/' , ' - ' ) , '13' , 600033 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( ( '[COLORsteelblue]IND/PAK[/COLOR]' ) . replace ( '\/' , ' - ' ) , '21' , 600033 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( ( '[COLORsteelblue]International[/COLOR]' ) . replace ( '\/' , ' - ' ) , '12' , 600033 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( I1ii1Ii1 + III1i )
 i1IIIII11I1IiI = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if '12' in oOooO0 :
   pass
  elif '21' in oOooO0 :
   pass
  elif '23' in oOooO0 :
   pass
  elif '13' in oOooO0 :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLORsteelblue]' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOooO0 , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
   if 21 - 21: I1ii11iIi11i % I1111IIi
def oOO0Oooo ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( OO0Ooo000O0 + url )
 iI1I1i11iIIii = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<title>(.+?)</title><description>(.+?)/description><desc_image><!.+?http(.+?)".+?<stream_url><!.+?http(.+?).ts.+?></stream_url>' , re . DOTALL ) . findall ( str ( iI1I1i11iIIii ) )
 i1I = re . compile ( '<title>(.+?)</title><description/><desc_image><!.+?http(.+?)".+?<stream_url><!.+?http(.+?).ts.+?></stream_url>' , re . DOTALL ) . findall ( str ( iI1I1i11iIIii ) )
 for iiI11ii1I1 , i11IIIiI1I , oOo0OOoO0 , oO000oOo00o0o in i1IIIII11I1IiI :
  if 'PPV' in iiI11ii1I1 :
   pass
  else :
   try :
    II1i = ( ( i11 ( iiI11ii1I1 ) ) )
    oOOo000oOoO0 = ( ( i11 ( i11IIIiI1I ) ) )
    OOoOO0O0o0 = '('
    I1II1oOOoo = ')'
   except :
    pass
   OOiIiIIi1 ( ( '[COLOR' + II + ']' + II1i + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + oO000oOo00o0o + '.m3u8' , 222 , 'http' + oOo0OOoO0 , O0o0Oo , ( '[COLOR' + II + ']' + oOOo000oOoO0 + '[/COLOR]' ) . replace ( I1II1oOOoo , '[COLORsteelblue]' ) . replace ( OOoOO0O0o0 , '[COLORorangered]' ) )
   I1I11i ( 'tvshows' , 'Media Info 3' )
 for iiI11ii1I1 , oOo0OOoO0 , oO000oOo00o0o in i1I :
  if 'PPV' in iiI11ii1I1 :
   pass
  II1i = ( ( i11 ( iiI11ii1I1 ) ) )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + II1i + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + oO000oOo00o0o + '.m3u8' , 222 , 'http' + oOo0OOoO0 , O0o0Oo , '' )
  if 9 - 9: ooOOOoO . oO0o * ooOoO0O00 . ii
def II1OoooOo ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( o0Oo0 + url )
 i1IIIII11I1IiI = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , type , oO000oOo00o0o , i1I1i1 in i1IIIII11I1IiI :
  II1Iii = ( iIIi1IiIi + oO000oOo00o0o + '.m3u8' ) . strip ( )
  OOiIiIIi1 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , II1Iii , 222 , ( i1I1i1 ) . replace ( '\/' , '/' ) + 'jpg' , O0o0Oo , type )
  I1I11i ( 'tvshows' , 'Media Info 3' )
def I1I1IIiiii1ii ( url , name , img ) :
 img = img
 name = name
 url = url
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for IIiIIIIii , oOo0Oi1i in i1IIIII11I1IiI :
  if name == IIiIIIIii :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) + oOo0Oi1i , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def OOOO00OoooO ( name ) :
 IIIi = name
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , oOo0OOoO0 , oOooO0 in i1IIIII11I1IiI :
  oOooO0 = ( oOooO0 ) . replace ( '.ts' , '.m3u8' )
  OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oOooO0 ) . strip ( ) , 222 , oOo0OOoO0 , oOo0OOoO0 , '' )
 else :
  OOiIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 43 - 43: ooOoO0O00 + o0o00Oo0O % oO0o / ii1ii11IIIiiI * oOo0O0Ooo
  if 89 - 89: oOo0O0Ooo . I1ii11iIi11i + Ii1I . o0o00Oo0O % I11i
  if 84 - 84: ii + iiiiiiii1 / oOo0O0Ooo % Ii1IIIi1 % Ii1I * oOo0O0Ooo
  if 58 - 58: oO0o - OOooOOo . Ii % Ii / ooOoO0O00 / o000O0o
  if 24 - 24: oOo0O0Ooo * ooOoO0O00 % I11i1ii1 / o0o00Oo0O + Ii
  if 12 - 12: Ii1I / ii1ii11IIIiiI
  if 5 - 5: ii
  if 18 - 18: oOo0O0Ooo % ii - O0OOOoOoo0 . Ii * I1ii11iIi11i % ii1ii11IIIiiI
  if 12 - 12: ooOoO0O00 / Ii1IIIi1 % I11i1ii1 * I1111IIi * o0o00Oo0O * iI11I1II1I1I
  if 93 - 93: I1ii11iIi11i / Ii1I + ooOoO0O00 * o000O0o . ii
  if 54 - 54: o0o00Oo0O / I1111IIi % I11i1ii1 * ooOoO0O00 * o0o00Oo0O
  if 48 - 48: I11i . o000O0o % OOooOOo - OOooOOo
def I1i11 ( ) :
 iiOOooooO0Oo ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( ooOooo000oOO ) :
  iiOOooooO0Oo ( 'Backup Genie Favourites' , oOooO0 , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( oO0 ) :
  iiOOooooO0Oo ( 'Backup Ivue Config' , oO0 , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  iiOOooooO0Oo ( 'Backup Kodi Favourites' , Ii1iIiII1ii1 , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 33 - 33: ooOOOoO % IIiIiII11i + oO0o
  if 93 - 93: ooOoO0O00 . I1111IIi / oOo0O0Ooo + I1111IIi
  if 58 - 58: Ii1I + o0o00Oo0O . I1ii11iIi11i + OOooOOo - oO0o - OOooOOo
zip = oo00 . getSetting ( 'zip' )
IIiiI = xbmc . translatePath ( os . path . join ( zip ) )
def iII11iiiiiii ( ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 82 - 82: ooOOOoO / I11i1ii1 * ooOOOoO % Ii * IIiIiII11i
  if 83 - 83: oO0o + Ii1IIIi1 - I11i + iI11I1II1I1I % I1ii11iIi11i
  if 23 - 23: I11i + ii1ii11IIIiiI % OOooOOo % oOo0O0Ooo % ii
def OOOOoo00OO0O0Ooo0 ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = ooOooo000oOO
  elif 'Ivue' in name :
   url = oO0
  elif 'Kodi' in name :
   url = Ii1iIiII1ii1
  iII11iiiiiii ( )
  ooOOO00oOOooO = open ( url ) . read ( )
  IiI = os . path . join ( IIiiI , description . split ( 'Your ' ) [ 1 ] )
  OOoO = open ( IiI , mode = 'w' )
  OOoO . write ( ooOOO00oOOooO )
  OOoO . close ( )
 else :
  if 'guisettings.xml' in description :
   Iii1iiI = open ( os . path . join ( IIiiI , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ii1IiiII = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   i1IIIII11I1IiI = re . compile ( ii1IiiII ) . findall ( Iii1iiI )
   for type , IiiI1II1II1i , iIO0OO0o0O00oO in i1IIIII11I1IiI :
    iIO0OO0o0O00oO = iIO0OO0o0O00oO . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IiiI1II1II1i , iIO0OO0o0O00oO ) )
  else :
   IiI = os . path . join ( url )
   ooOOO00oOOooO = open ( os . path . join ( IIiiI , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOoO = open ( IiI , mode = 'w' )
   OOoO . write ( ooOOO00oOOooO )
   OOoO . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 81 - 81: I1111IIi / ooOOOoO
 if 46 - 46: Ii1I / iiiiiiii1 + I1111IIi / o000O0o / iiiiiiii1 / Ii1IIIi1
 if 73 - 73: I11i1ii1 + Ii1I
 if 100 - 100: iI11I1II1I1I
def ooOOo00 ( ) :
 IIii1i1IiIi1 = 1
 iII11iiiiiii ( )
 IiiiiIIi11iI = xbmc . translatePath ( os . path . join ( IIiiI , 'Build Backup' , 'Full Backup' , '' ) )
 ii111I11Ii = xbmc . translatePath ( os . path . join ( IIiiI , 'Build Backup' , 'my_full_backup.zip' ) )
 i11IiiI1Ii1 = xbmc . translatePath ( os . path . join ( IIiiI , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( IiiiiIIi11iI ) :
  os . makedirs ( IiiiiIIi11iI )
 I1iiIiiIiiI = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not I1iiIiiIiiI ) : return False , 0
 II1i = I1iiIiiIiiI
 oOoO = xbmc . translatePath ( os . path . join ( IiiiiIIi11iI , II1i + '.zip' ) )
 ii1IIii = [ 'plugin.video.GenieTv' ]
 IiI11i1I11111 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 Ii1IIIIIIiI1 = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 Ii11IiIiiii1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 OooO0O0Ooo = "Creating full backup of existing build"
 oO0O = "Creating Community Build"
 IIIiIi1iiI = "Archiving..."
 iI1 = ""
 o0Iiii = "Please Wait"
 I1i1I ( Oo0o0000o0o0 , oOoO , oO0O , IIIiIi1iiI , iI1 , o0Iiii , Ii1IIIIIIiI1 , Ii11IiIiiii1 )
 time . sleep ( 1 )
 i1111iI1 = xbmc . translatePath ( os . path . join ( IiiiiIIi11iI , II1i + '_guisettings.zip' ) )
 Oo0oOOOOo = zipfile . ZipFile ( i1111iI1 , mode = 'w' )
 try :
  Oo0oOOOOo . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 Oo0oOOOOo . close ( )
 if IIii1i1IiIi1 == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + ii111I11Ii , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + oOoO + '[/COLOR]' )
  if 14 - 14: ii . I11i . ooOOOoO
def I1i1I ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 I1IIIIIi1IIiI = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 III11I11ii = len ( sourcefile )
 O0OoO0oO00 = [ ]
 I1II1IiI1 = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for iIIiI11iI1Ii1 , o00oo , O0oO0oo0O in os . walk ( sourcefile ) :
  for file in O0oO0oo0O :
   I1II1IiI1 . append ( file )
 oooOOO0ooOoOOO = len ( I1II1IiI1 )
 for iIIiI11iI1Ii1 , o00oo , O0oO0oo0O in os . walk ( sourcefile ) :
  o00oo [ : ] = [ o0IiIiI111IIII1 for o0IiIiI111IIII1 in o00oo if o0IiIiI111IIII1 not in exclude_dirs ]
  O0oO0oo0O [ : ] = [ OOoO for OOoO in O0oO0oo0O if OOoO not in exclude_files ]
  for file in O0oO0oo0O :
   O0OoO0oO00 . append ( file )
   OOOoOooO000oO = len ( O0OoO0oO00 ) / float ( oooOOO0ooOoOOO ) * 100
   o0oOoO00o . update ( int ( OOOoOooO000oO ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   o0OOOOOo00 = os . path . join ( iIIiI11iI1Ii1 , file )
   if not 'temp' in o00oo :
    if not 'plugin.program.originwizard' in o00oo :
     import time
     oo0oOO = '01/01/1980'
     IIO000oooOO0Oo0 = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o0OOOOOo00 ) ) )
     if IIO000oooOO0Oo0 > oo0oOO :
      I1IIIIIi1IIiI . write ( o0OOOOOo00 , o0OOOOOo00 [ III11I11ii : ] )
 I1IIIIIi1IIiI . close ( )
 o0oOoO00o . close ( )
 if 31 - 31: I1111IIi - oO0o / Ii1IIIi1 . ooOoO0O00 / ii1ii11IIIiiI
 if 66 - 66: oO0o
def o00ooO0ooO0o0 ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 if 88 - 88: o000O0o % I1ii11iIi11i - ooOOOoO % o000O0o + I1111IIi - O0OOOoOoo0
 if 23 - 23: o0o00Oo0O
def I1iI11IiiI11i ( ) :
 Oo0oO ( )
 i111I1 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  iI1I ( )
 if iI11iI1IiiIiI == 1 :
  IIiI1 ( )
 if iI11iI1IiiIiI == 2 :
  OO00oOooo0O ( )
 if iI11iI1IiiIiI == 3 :
  O00000Oo00o ( )
  if 37 - 37: I11i % ooOoO0O00 - I11i + iI11I1II1I1I + iiiiiiii1
  if 84 - 84: o000O0o + Ii1IIIi1 . O0OOOoOoo0
  if 71 - 71: I11i1ii1 / I11i1ii1 . OOooOOo % O0OOOoOoo0
  if 50 - 50: I11i1ii1 + O0OOOoOoo0 / ooOOOoO / ooOOOoO % o0o00Oo0O
  if 87 - 87: I1ii11iIi11i + I11i1ii1
  if 66 - 66: I11i * Ii1IIIi1 + ii1ii11IIIiiI * I11i + Ii1IIIi1 / ii
  if 86 - 86: ii1ii11IIIiiI . O0OOOoOoo0 - O0OOOoOoo0
  if 71 - 71: iI11I1II1I1I . IIiIiII11i % iI11I1II1I1I
  if 22 - 22: Ii % Ii1I % I11i1ii1 % I11i1ii1 . oO0o
def O0oII1IIiiI1 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   I1i11ii ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if iI11iI1IiiIiI == 1 :
   I1i11ii ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if iI11iI1IiiIiI == 2 :
   O00O00 ( )
  if iI11iI1IiiIiI == 3 :
   oOooO0OoO ( )
  if iI11iI1IiiIiI == 4 :
   o0oOOOOoo0 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if iI11iI1IiiIiI == 5 :
   ooOO0OOO00o ( )
  if iI11iI1IiiIiI == 6 :
   OoOoO0ooooO0 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if iI11iI1IiiIiI == 7 :
   IIII1ii1 ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if iI11iI1IiiIiI == 8 :
   OOO0O0OOo ( str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if iI11iI1IiiIiI == 9 :
   Iii1 ( )
  if iI11iI1IiiIiI == 10 :
   OOoOi1IiiI ( )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']RaysRavers[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) , 90037 , III1iII1I1ii + 'Rays-Ravers.png' , O0o0Oo , '' )
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
  if 70 - 70: ooOOOoO . Ii1IIIi1 * I1ii11iIi11i / Ii1IIIi1
 I1I11i ( 'movies' , 'MAIN' )
 if 83 - 83: ii + oO0o * o000O0o . o0o00Oo0O
def iiIIIi1i ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iIi1i1i1II11I ( )
  if iI11iI1IiiIiI == 1 :
   i11i1 ( )
  if iI11iI1IiiIiI == 2 :
   iIiIi11 ( )
  if iI11iI1IiiIiI == 3 :
   O0OO ( oOooO0 )
  if iI11iI1IiiIiI == 4 :
   OO0OooOo ( oOooO0 )
  if iI11iI1IiiIiI == 5 :
   oOOo0O00o ( )
  if iI11iI1IiiIiI == 6 :
   ii111iI1i1 ( url = 'http://www.iplocation.net/' , inc = 1 )
  if iI11iI1IiiIiI == 7 :
   OO000 ( )
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
  if 31 - 31: oO0o * o0o00Oo0O / ooOOOoO . ii * ooOOOoO . Ii1I
  if 50 - 50: oO0o * ooOOOoO - I11i + I1111IIi * oO0o % o000O0o
 I1I11i ( 'movies' , 'MAIN' )
 if 92 - 92: ooOOOoO % ooOoO0O00 % I11i1ii1 % I1111IIi % I11i
 if 61 - 61: Ii1IIIi1 * I11i * o0o00Oo0O / O0OOOoOoo0
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
 if 52 - 52: I1ii11iIi11i + iI11I1II1I1I + ooOoO0O00 * ii1ii11IIIiiI - IIiIiII11i . IIiIiII11i
 if 22 - 22: ooOoO0O00 - iiiiiiii1 / O0OOOoOoo0 - OOooOOo . o000O0o
def iiIi1iIiI ( ) :
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
 if 9 - 9: iI11I1II1I1I . ii + ooOoO0O00 - I1ii11iIi11i
def IiIi1I1 ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']My Local Zip[/COLOR]' , oOOoO0 , 48 , III1iII1I1ii + 'MyLocalZIP.png' , O0o0Oo , '' )
 OOiIiIIi1 ( '[COLOR' + II + ']My Online Zip[/COLOR]' , iIii1 , 43 , III1iII1I1ii + 'MyOnlineZip.png' , O0o0Oo , '' )
 if 30 - 30: O0OOOoOoo0 / oO0o . O0OOOoOoo0
def iI1iiiI ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( 'INSTALL FTV GUIDE AND OTHER ADDONS REQUIRED' , str ( I1I1IiI1 ) + '/wizard/customftv/ftvguide-addons.zip' , 5 , III1iII1I1ii + 'FTV4.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE FIRST RUN SETTINGS' , str ( I1I1IiI1 ) + '/wizard/customftv/settings.xml' , 17 , III1iII1I1ii + 'FTV3.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'FTV GUIDE ADDONS2.INI UPDATE DAILY' , 'http://ren.byethost12.com/addons2.ini' , 16 , III1iII1I1ii + 'FTV1.png' , O0o0Oo , '' )
 OOiIiIIi1 ( 'RESET FTV DATABASE' , 'url' , 18 , III1iII1I1ii + 'FTV2.png' , O0o0Oo , '' )
 if 75 - 75: ii . Ii1IIIi1 + oO0o / ii1ii11IIIiiI - oOo0O0Ooo % ii1ii11IIIiiI
 if 89 - 89: O0OOOoOoo0 * iI11I1II1I1I + Ii . ii
 if 51 - 51: Ii1IIIi1 / I11i1ii1 + oO0o % OOooOOo / ii1ii11IIIiiI
def ii111i1i ( ) :
 Oo0oO ( )
 i111I1 = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  OOo0OOooo0 ( )
 if iI11iI1IiiIiI == 0 :
  oooOoOoOO ( oOooO0 )
 if iI11iI1IiiIiI == 0 :
  OooOO ( oOooO0 )
  if 32 - 32: Ii
  if 6 - 6: OOooOOo / iI11I1II1I1I * iiiiiiii1 / oOo0O0Ooo + o0o00Oo0O
  if 2 - 2: oOo0O0Ooo * I1ii11iIi11i % I11i % I1ii11iIi11i
 I1I11i ( 'movies' , 'MAIN' )
 if 66 - 66: I1111IIi + iI11I1II1I1I
def o0Oo00oOO ( ) :
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 i1IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1i )
 for oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , oOo0OOoO0 , oOo0OOoO0 , '' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 73 - 73: ooOOOoO / ii . IIiIiII11i - I1111IIi * I11i1ii1 * I1111IIi
def IiI1IiI1iiI1 ( url ) :
 i1i = OoOooO ( O000o0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 5 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 39 - 39: IIiIiII11i + ii / Ii1IIIi1 / ii1ii11IIIiiI * OOooOOo
def OOo0OOooo0 ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 71 - 71: ooOoO0O00 / Ii1I % Ii / ooOoO0O00
def i1i1Ii1IiIII ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + I1IIii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 22 - 22: I11i1ii1 / I11i1ii1 - ii1ii11IIIiiI % ooOOOoO . Ii1IIIi1 + I1111IIi
def OooO00oo0O0 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + i1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 73 - 73: ii . I1ii11iIi11i / o0o00Oo0O - o0o00Oo0O
def IiI11IIi11Iii ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + ii11i1I1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 49 - 49: ii + ii / Ii1IIIi1 . o000O0o
def IiIooOoOo0O00oo ( url ) :
 i1i = OoOooO ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 12 - 12: I11i1ii1
def oooOoOoOO ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + I11OOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 40 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 16 - 16: O0OOOoOoo0 / iI11I1II1I1I + Ii1IIIi1 * O0OOOoOoo0 * ooOOOoO
def iiIiI11IiI1ii ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + ooO0O0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 5 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 34 - 34: ooOoO0O00 - OOooOOo + I11i - I1ii11iIi11i % Ii1I
def Ii1I1i ( ) :
 i111I1 = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  I11ii1iI11 ( )
 if iI11iI1IiiIiI == 1 :
  i11ii111i1ii ( )
 if iI11iI1IiiIiI == 2 :
  Oo0O0O ( )
  if 8 - 8: Ii * o0o00Oo0O + Ii1I . iI11I1II1I1I % ooOOOoO / ooOOOoO
  if 70 - 70: oOo0O0Ooo + ii1ii11IIIiiI
  if 70 - 70: I1111IIi . Ii
  if 76 - 76: O0OOOoOoo0 . I1111IIi % O0OOOoOoo0 - iiiiiiii1
def i11ii111i1ii ( ) :
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( OoO000O0Oo )
 for oOooO0 , Oo0O0oo in i1IIIII11I1IiI :
  O00oO0 ( 'Android Apps' + Oo0O0oo , 'https://www.apkfiles.com' + oOooO0 , 30035 , III1iII1I1ii + 'apps.png' )
 for oOooO0 , Oo0O0oo in i1I :
  O00oO0 ( 'Android Games' + Oo0O0oo , 'https://www.apkfiles.com' + oOooO0 , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I11i ( 'movies' , 'MAIN' )
def o0O0 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if '/cat' in url :
   O00oO0 ( ( iiI11ii1I1 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def oO0o0 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if '/app' in url :
   O00oO0 ( ( iiI11ii1I1 ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def ooOoOoO0 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 oO00oOOo0Oo = url
 if "page=" in str ( url ) :
  oO00oOOo0Oo = url . split ( '?' ) [ 0 ]
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'apk' in url :
   OOiIiIIi1 ( ( iiI11ii1I1 ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + oOo0OOoO0 )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 OOiIiIIi1 ( 'Next Page' , oO00oOOo0Oo + str ( i1I ) , 30037 , III1iII1I1ii + 'Next.png' )
def Iii1II1ii ( name , url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 name = name
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  ooOo00 ( name , url , 'Brackets' )
def Oo0O0O ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI1IIi1IiI = 'https://www.apkfiles.com/search?q=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' ) + '&search_type=1'
 i1IiiI1iIi = iI1IIi1IiI . lower ( )
 ooOoOoO0 ( i1IiiI1iIi )
 if 98 - 98: oO0o . iI11I1II1I1I % ii % I1ii11iIi11i - Ii1I
def oO0I1I1i1I1I1I1 ( url ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( iI11IiIiiII1 , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oooooo0O000o = os . path . join ( O0O00Oo , iiI11ii1I1 + '.apk' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 15 - 15: I11i1ii1 - o0o00Oo0O % oOo0O0Ooo . ii * I1ii11iIi11i / o0o00Oo0O
def IIi1I ( url ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oooooo0O000o = os . path . join ( O0O00Oo , iiI11ii1I1 + '.mp4' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 15 - 15: Ii1I
 if 4 - 4: I1111IIi + iI11I1II1I1I * O0OOOoOoo0 + I1ii11iIi11i * I11i % IIiIiII11i
def OO0o0o0oo ( name , url , description ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oooooo0O000o = os . path . join ( O0O00Oo , name )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 iIiII1 = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print iIiII1
 print '======================================='
 extract . all ( oooooo0O000o , iIiII1 , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 47 - 47: ooOOOoO
 if 92 - 92: ii % oOo0O0Ooo / OOooOOo * OOooOOo % Ii / ii
 if 47 - 47: Ii / I1ii11iIi11i - I1ii11iIi11i * oO0o
 if 48 - 48: I1111IIi
 if 96 - 96: o000O0o / o0o00Oo0O . IIiIiII11i + I1111IIi % I11i
def I11ii1iI11 ( ) :
 i1i = OoOooO ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1i )
 for iiI11ii1I1 , oOooO0 , i1I1i1 , O0OoooO0 , oo0O0oOOO0o in i1IIIII11I1IiI :
  OOiIiIIi1 ( iiI11ii1I1 , oOooO0 , 80003 , i1I1i1 , III1iII1I1ii + 'APKToolsB.png' , oo0O0oOOO0o )
def oOo0Oo0Oo0 ( apk , ret = None ) :
 if apk == "kodi" :
  OooOo0o0OO = "https://kodi.tv/download/"
  i1i = OoOooO ( OooOo0o0OO ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1i )
  if len ( i1IIIII11I1IiI ) == 1 :
   iiI1ii1IIiI = i1IIIII11I1IiI [ 0 ] [ 0 ]
   II1i = i1IIIII11I1IiI [ 0 ] [ 1 ]
   IIi1i1I11IIII = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( iiI1ii1IIiI , II1i )
  if ret == 'version' : return iiI1ii1IIiI
  else : return IIi1i1I11IIII
 elif apk == "spmc" :
  OooOoOOO00O = 'https://github.com/koying/SPMC/releases/latest/'
  i1i = OoOooO ( OooOoOOO00O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1i )
  iiI1ii1IIiI = re . sub ( '<[^<]+?>' , '' , i1IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  IIi1i1I11IIII = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( iiI1ii1IIiI , iiI1ii1IIiI )
  if ret == 'version' : return iiI1ii1IIiI
  else : return IIi1i1I11IIII
def ooOo00 ( name , url , Brackets ) :
 if I1IIII1i ( ) == 'android' :
  I111iIIII11iI = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not I111iIIII11iI : oOoOO ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  i11I1iIii1i11 = name
  if I111iIIII11iI :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not IIIIiII1i ( url ) == True : oOoOO ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % i11I1iIii1i11 , '' , 'Please Wait' )
   oooooo0O000o = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( oooooo0O000o )
   except : pass
   downloader . download ( url , oooooo0O000o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    Oo0oOOOOo = zipfile . ZipFile ( oooooo0O000o )
    for file in Oo0oOOOOo . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as OOoO :
       iIiiI11II11i = file . split ( '/' ) [ 1 ]
       OOoO . write ( Oo0oOOOOo . read ( file ) )
       xbmc . sleep ( 500 )
       OOoO . close ( )
       try :
        os . remove ( oooooo0O000o )
       except :
        pass
       oooooo0O000o = os . path . join ( i1iiIII111ii , iIiiI11II11i )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oooooo0O000o + '")' )
  else : oOoOO ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oOoOO ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 98 - 98: O0OOOoOoo0 - O0OOOoOoo0
 if 58 - 58: o000O0o
 if 98 - 98: I11i * oO0o
 if 10 - 10: o000O0o - O0OOOoOoo0 % IIiIiII11i - iiiiiiii1 - ooOoO0O00
def iIi11iI1i ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1i )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  oOooO0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oOooO0 )
  Ii1iIi ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , oOooO0 )
  if 79 - 79: Ii1IIIi1 % iiiiiiii1 / o000O0o - iI11I1II1I1I - OOooOOo
def Ii1iIi ( name , url ) :
 if I1IIII1i ( ) == 'android' :
  I111iIIII11iI = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not I111iIIII11iI : oOoOO ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  i11I1iIii1i11 = name
  if I111iIIII11iI :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not IIIIiII1i ( url ) == True : oOoOO ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % i11I1iIii1i11 , '' , 'Please Wait' )
   oooooo0O000o = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( oooooo0O000o )
   except : pass
   downloader . download ( url , oooooo0O000o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oooooo0O000o + '")' )
  else : oOoOO ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : oOoOO ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 60 - 60: IIiIiII11i
 if 90 - 90: OOooOOo
def IIii1i ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 5 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'INFO' )
 if 69 - 69: iiiiiiii1 / ii % Ii
 if 18 - 18: Ii - I11i1ii1 * o000O0o + I11i
def II1i11I ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 30015 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 16 - 16: ii * Ii . ii - iI11I1II1I1I * ooOoO0O00
def i1iI1IIi1I ( url , iconimage , fanart ) :
 i1i = OoOooO ( url )
 O0ooooo000 = url
 oOo0OOoO0 = iconimage
 fanart = fanart
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for oO000oOo00o0o , iiI11ii1I1 in i1IIIII11I1IiI :
  if '.mp4' in iiI11ii1I1 :
   OOiIiIIi1 ( 'Watch VIDEO' , url + '/' + oO000oOo00o0o , 222 , oOo0OOoO0 , fanart , '' )
  if 'description' in iiI11ii1I1 :
   OOiIiIIi1 ( 'Read Description' , url + '/' + oO000oOo00o0o , 30017 , oOo0OOoO0 , fanart , '' )
  if 'images' in iiI11ii1I1 :
   iiOOooooO0Oo ( 'View Images' , url + '/' + oO000oOo00o0o , 30018 , oOo0OOoO0 , fanart , '' )
  if 'url' in iiI11ii1I1 :
   OOiIiIIi1 ( 'Install Build On Android' , url + '/' + oO000oOo00o0o , 30016 , oOo0OOoO0 , fanart , '' )
  if 'url' in iiI11ii1I1 :
   OOiIiIIi1 ( 'Install Build On Pc' , url + '/' + oO000oOo00o0o , 30019 , oOo0OOoO0 , fanart , '' )
 I1I11i ( 'movies' , 'INFO' )
 if 52 - 52: ii / I1111IIi % IIiIiII11i
def Ii11I1I11II ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  IIiiiI ( url )
  if 59 - 59: o000O0o % I11i1ii1
def ii1II1iiii ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  IIIIIiiI11i1 ( url )
  if 43 - 43: oOo0O0Ooo / O0OOOoOoo0 / I11i1ii1 + iI11I1II1I1I + ii
def iiI111i1 ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1i )
 for IiIii11i1IIiI in i1IIIII11I1IiI :
  iiIiI1i1 ( 'Description:' , IiIii11i1IIiI )
  if 40 - 40: O0OOOoOoo0 + iI11I1II1I1I * o000O0o + Ii . Ii
def iIii1I1111 ( url ) :
 i1i = OoOooO ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for oO000oOo00o0o , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'png' in iiI11ii1I1 :
   OOiIiIIi1 ( 'image' , '' , '' , url + '/' + oO000oOo00o0o , url + '/' + oO000oOo00o0o , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 26 - 26: iiiiiiii1 . oOo0O0Ooo . O0OOOoOoo0 - ii / iI11I1II1I1I
def i111IIiIII1i ( name , url , description ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oooooo0O000o = os . path . join ( O0O00Oo , name + '.zip' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OoO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoO
 print '======================================='
 extract . all ( oooooo0O000o , OoO , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to finish install" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 oOOo0O00o ( )
 if 74 - 74: IIiIiII11i / o0o00Oo0O
 if 56 - 56: ooOOOoO - o0o00Oo0O / o0o00Oo0O * ooOoO0O00 . ii % iI11I1II1I1I
def IIIIIiiI11i1 ( url ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oooooo0O000o = os . path . join ( O0O00Oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OoO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoO
 print '======================================='
 extract . all ( oooooo0O000o , OoO , o0oOoO00o )
 ooO0O0O0ooOOO ( url )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, if unsuccessful using windows Please kill kodi via taskmanager" , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIi1i1i1II11I ( )
 if 21 - 21: I1111IIi - oOo0O0Ooo % ii + I11i
def IIiiiI ( url ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading " , '' , 'Please Wait' )
 oooooo0O000o = os . path . join ( O0O00Oo , 'plugin.program.GenieTv.install' + '.zip' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OoO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoO
 print '======================================='
 extract . all ( oooooo0O000o , OoO , o0oOoO00o )
 ooO0O0O0ooOOO ( url )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIi1i1i1II11I ( )
 if 92 - 92: I11i1ii1 + I1111IIi
def Oooo ( name , url , description ) :
 OoO = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 oooooo0O000o = os . path . join ( oOOoO0 )
 time . sleep ( 2 )
 o0oOoO00o . create ( "GenieTv" , "Restoring" , '' , 'Please Wait' )
 print '======================================='
 print OoO
 print '======================================='
 extract . all ( oooooo0O000o , OoO , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "Press ok to force close kodi, If unsuccessful Please press home button got to settings/apps and force close kodi and clear cache. " , "[COLOR yellow]Brought To You By GenieTv[/COLOR]" )
 iIi1i1i1II11I ( )
 if 87 - 87: I1111IIi . ooOoO0O00 % ii * Ii
def I1IIII1i ( ) :
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
  o0oOo = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  OOoO . write ( o0oOo . rstrip ( '\r\n' ) + '\n' )
def iIi1i1i1II11I ( ) :
 iI11iI1IiiIiI = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iI11iI1IiiIiI == 0 : return
 elif iI11iI1IiiIiI == 1 : pass
 OoIIiIIIII1I = I1IIII1i ( )
 OOO ( "Platform: " + str ( OoIIiIIIII1I ) )
 os . _exit ( 1 )
 OOO ( "Force close failed!  Trying alternate methods." )
 if OoIIiIIIII1I == 'osx' :
  OOO ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif OoIIiIIIII1I == 'linux' :
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
 elif OoIIiIIIII1I == 'android' :
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
 elif OoIIiIIIII1I == 'windows' :
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
  if 96 - 96: Ii . IIiIiII11i
  if 7 - 7: ooOoO0O00
  if 63 - 63: iI11I1II1I1I + I1111IIi % ooOoO0O00 / oOo0O0Ooo % IIiIiII11i
def OooOO ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for OO0iiiii1iiIIii , o00oo , O0oO0oo0O in os . walk ( url ) :
  for file in O0oO0oo0O :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    Iii1iiI = open ( ( os . path . join ( OO0iiiii1iiIIii , file ) ) ) . read ( )
    II1IIii1I11I = Iii1iiI . replace ( Oo0o0000o0o0 , 'special://home/' )
    OOoO = open ( ( os . path . join ( OO0iiiii1iiIIii , file ) ) , mode = 'w' )
    OOoO . write ( str ( II1IIii1I11I ) )
    OOoO . close ( )
 iIi1i1i1II11I ( )
 if 17 - 17: o0o00Oo0O
def O00O00 ( ) :
 O00oO0 ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 O00oO0 ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 O00oO0 ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 31 - 31: ooOOOoO + IIiIiII11i * I1ii11iIi11i + I1ii11iIi11i . ooOOOoO
def O0Oo00o00OoO ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def II1i1I1111I1I ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def III1iiIIIII1 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1I :
  O00oO0 ( ( '[COLOR' + II + ']Filter - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']Stream - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , oOo0OOoO0 )
def oO0Oo0OOoo0oo ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  iii1 ( url )
def IiIi ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1
 iI1iii1iIiiI = 'https://www.radionomy.com/en/search/index?query=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 oO0OOoo0OO = OoOooO ( iI1iii1iIiiI )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']Stream - ' + iiI11ii1I1 + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oOooO0 , 70005 , oOo0OOoO0 )
  if 36 - 36: oO0o - o0o00Oo0O * oOo0O0Ooo / Ii1I / Ii1IIIi1
  if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
def ooOO0OOO00o ( ) :
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , 'http://www.listenlive.eu/' + oOooO0 , 10111113 , III1iII1I1ii + 'radio.png' )
def o0oOOOOoo0 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  O0Oo00OoOo ( iiI11ii1I1 , url , 222 , III1iII1I1ii + 'radio.png' )
  if 63 - 63: I1111IIi + iI11I1II1I1I + oOo0O0Ooo + iiiiiiii1
def oOOoO0O ( ) :
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.toonjet.com/' + oOooO0 , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OoOoOoOOo00Ooo0O ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 in i1IIIII11I1IiI :
  if 'ol.gif' in oOo0OOoO0 :
   pass
  elif 'link_block_' in oOo0OOoO0 :
   pass
  elif '.png' in oOo0OOoO0 :
   pass
  else :
   O00oO0 ( ( oOo0OOoO0 ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in i1I :
  O00oO0 ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIii1Oo ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 15 - 15: ooOoO0O00 + I1111IIi % oOo0O0Ooo / Ii * OOooOOo
  if 69 - 69: Ii
def OOoOi1IiiI ( ) :
 IIiii11ii1i ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 IIiii11ii1i ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 61 - 61: o0o00Oo0O
def iIiiI111I11 ( ) :
 IIiii11ii1i ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 IIiii11ii1i ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 IIiii11ii1i ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 86 - 86: o000O0o + O0OOOoOoo0 / ii - ooOOOoO
def o00O0 ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , oOooO0 , III in i1IIIII11I1IiI :
  if 'Parent' in iiI11ii1I1 :
   pass
  elif '2' in III :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 3 - 3: Ii - o000O0o / I1111IIi
def o0O0o0O0OO0O ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , oOooO0 , III in i1IIIII11I1IiI :
  if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
   if '1' in III :
    IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in III :
    IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in III :
    IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 7 - 7: ooOOOoO + ooOOOoO + IIiIiII11i % ii1ii11IIIiiI
    if 31 - 31: o000O0o * OOooOOo + Ii1IIIi1
def OOoo0OOOo0o ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , oOooO0 , III in i1IIIII11I1IiI :
  if '1' in III :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in III :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in III :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 10 - 10: iiiiiiii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 48 - 48: O0OOOoOoo0 * ooOoO0O00 % ii * ii1ii11IIIiiI * oO0o
def I1i ( url ) :
 oO000oOo00o0o = url
 oO0OOoo0OO = OoOooO ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1I :
  if 'mp3' in iiI11ii1I1 :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oO000oOo00o0o + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in iiI11ii1I1 :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oO000oOo00o0o + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in iiI11ii1I1 :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) , oO000oOo00o0o + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in iiI11ii1I1 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oO000oOo00o0o + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 77 - 77: iiiiiiii1 * Ii1IIIi1 / I11i1ii1 + Ii1I
   if 20 - 20: IIiIiII11i + ooOoO0O00
   if 17 - 17: ii % o000O0o - ooOoO0O00 % I1111IIi % I1ii11iIi11i
def IiOO0OOOOOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 oO000oOo00o0o = url
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
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
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oO000oOo00o0o + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in iiI11ii1I1 :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oO000oOo00o0o + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , oO000oOo00o0o + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 7 - 7: o0o00Oo0O + ii1ii11IIIiiI . IIiIiII11i
   if 12 - 12: oOo0O0Ooo - ooOoO0O00
def O0o00 ( ) :
 IIiii11ii1i ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 IIiii11ii1i ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 IIiii11ii1i ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 8 - 8: iiiiiiii1 * I1ii11iIi11i - Ii1IIIi1 . iI11I1II1I1I
def IiIiI ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , oOo0OOoO0 in i1IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oOooO0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in oOo0OOoO0 :
   pass
  else :
   IIiii11ii1i ( oOo0OOoO0 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oOooO0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + oOo0OOoO0 + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 77 - 77: I11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 74 - 74: I1111IIi - o0o00Oo0O / iiiiiiii1 * ii1ii11IIIiiI % I11i1ii1 . iiiiiiii1
 if 60 - 60: Ii1I . IIiIiII11i * Ii . I11i
def o00ooO000Oo00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if '</a>' in iiI11ii1I1 :
   pass
  elif '(' in iiI11ii1I1 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 43 - 43: oO0o . I11i1ii1 * I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 20 - 20: ooOoO0O00 . ooOoO0O00 - ooOOOoO
def O0o00ooo ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
   if '</a>' in iiI11ii1I1 :
    pass
   elif '(' in iiI11ii1I1 :
    IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 5 - 5: ooOoO0O00 - o000O0o / OOooOOo
    if 13 - 13: IIiIiII11i
def oO0o000oOO ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if '</a>' in iiI11ii1I1 :
   pass
  elif '(' in iiI11ii1I1 :
   IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 27 - 27: o0o00Oo0O - ooOOOoO * IIiIiII11i - iI11I1II1I1I / I11i1ii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 24 - 24: I1ii11iIi11i / iI11I1II1I1I % Ii1IIIi1 * OOooOOo - iI11I1II1I1I
 if 50 - 50: IIiIiII11i
def IiIIiiiIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  oO000oOo00o0o = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( oO000oOo00o0o )
  if 31 - 31: Ii + I1111IIi - iiiiiiii1 * O0OOOoOoo0
def O0OO00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  if '<p align' in iiI11ii1I1 :
   pass
  elif '&nbsp;' in iiI11ii1I1 :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 6 - 6: I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 73 - 73: iiiiiiii1 * Ii1I + I11i - I1ii11iIi11i . ooOOOoO
 if 93 - 93: Ii
def oOOOo ( ) :
 oO0OOoo0OO = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'ongoing' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'CartoonShows.png' , '' , '' )
  if 'disney' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'Disney.png' , '' , '' )
  if 'genre' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'Genre.png' , '' , '' )
  if 'years' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'Years.png' , '' , '' )
def OoOiII11IiIi ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iII1I1i = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , oOo0OOoO0 , oOo0OOoO0 , iiI11ii1I1 )
 for url , iiI11ii1I1 in iII1I1i :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def IIiiiooOoOooo00Oo ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oOoOoo0 = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ooo00O0OOo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0OOoo0OO )
 IiI1 = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in ooo00O0OOo :
  iiOOooooO0Oo ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , iiI11ii1I1 in oOoOoo0 :
  OOiIiIIi1 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def Iii1IIII1Iii ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 94 - 94: o000O0o . I11i % I11i % oOo0O0Ooo - O0OOOoOoo0 / Ii
def iIIIIIiI1I1 ( ) :
 oO0OOoo0OO = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 i1IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if '9cart' in oOooO0 :
   O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 73 - 73: o0o00Oo0O * iiiiiiii1 . ooOoO0O00
def OO00OoOO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 I1II1 = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if '9cart' in url :
   O00oO0 ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   O00oO0 ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url , iiI11ii1I1 in I1II1 :
  if '9cart' in url :
   O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 45 - 45: IIiIiII11i * ooOoO0O00
def II1ii1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20003 , oOo0OOoO0 )
 for url , iiI11ii1I1 in i1I :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 89 - 89: I11i + Ii1IIIi1 * o000O0o
def i1iI1IIi ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'Watch' in url :
   O00oO0 ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 27 - 27: o0o00Oo0O / oO0o
def O000oooO0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 20005 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 75 - 75: Ii
def Ii111III1i11I ( url ) :
 url = cloudflare . source ( url )
 O0OoooI11iI1I ( url )
 if 62 - 62: ooOOOoO . oO0o + oO0o + IIiIiII11i * iI11I1II1I1I + ii
def Oo0OOOOOOO0oo ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in i1IIIII11I1IiI :
  O0OoooI11iI1I ( url )
  if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
  if 15 - 15: I11i1ii1 % I11i / o000O0o - IIiIiII11i . iI11I1II1I1I
def OO0O0o0o0 ( ) :
 if 28 - 28: IIiIiII11i * I11i1ii1 * ii1ii11IIIiiI
 iiOOooooO0Oo ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 93 - 93: ooOoO0O00 . ii1ii11IIIiiI * iiiiiiii1 . I11i1ii1
def OO00oOooo0O ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 54 - 54: O0OOOoOoo0 . ooOoO0O00 . Ii1I * I11i % O0OOOoOoo0
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO0OOoo0OO )
 if 30 - 30: ooOOOoO
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
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
    iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
    if 85 - 85: IIiIiII11i + I11i1ii1 * ooOOOoO
    if 12 - 12: ii1ii11IIIiiI . oOo0O0Ooo % I11i
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 28 - 28: ii1ii11IIIiiI - oOo0O0Ooo % oO0o * iiiiiiii1
def I11I1IIiiII1 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
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
   iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 80 - 80: Ii1IIIi1 * I1111IIi
def IiIii11ii111 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 in i1I :
  oOiiIIIII = oOo0OOoO0
 I1II1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1II1 :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10007 , oOiiIIIII )
  if 19 - 19: IIiIiII11i / OOooOOo
  if 80 - 80: OOooOOo + iI11I1II1I1I . I1111IIi
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 76 - 76: oOo0O0Ooo * Ii1IIIi1
def ii111 ( url , IMAGE ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  print iiI11ii1I1 + '     ' + url
  if 'easy' in url :
   IIiiI11 ( url )
   if 7 - 7: oOo0O0Ooo / oO0o + iiiiiiii1 + ooOOOoO / oOo0O0Ooo
   if 82 - 82: Ii1I + ii
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 21 - 21: o000O0o * o000O0o / ooOOOoO . O0OOOoOoo0
def IIiiI11 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  iii1 ( url )
  if 10 - 10: ii1ii11IIIiiI * Ii1IIIi1 - I1ii11iIi11i - ii / I11i
  if 86 - 86: iiiiiiii1 % oOo0O0Ooo
  if 22 - 22: Ii * iiiiiiii1 . I1ii11iIi11i . ii + oOo0O0Ooo
def Iii1oooo00Oo0O ( ) :
 if 16 - 16: ii % oOo0O0Ooo - I11i / IIiIiII11i . ooOoO0O00
 iiOOooooO0Oo ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , O0o0Oo , '' )
 if 27 - 27: IIiIiII11i + I11i1ii1 . OOooOOo - iiiiiiii1
def oOiii1IiII ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'elete' in iiI11ii1I1 :
   pass
  else :
   O0Oo00OoOo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 222 , oOo0OOoO0 )
   if 65 - 65: I11i1ii1 % o0o00Oo0O
def IiiII1I ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiIii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , o0OoOo0O00 , i1iII1IiiIiI1 in IiIii :
  for I11iiIi1i1 in o0OoOo0O00 :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   iI1i1iI1iI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oOooO0 , iiI11ii1I1 in iI1i1iI1iI :
    if 'tube' in oOooO0 :
     pass
    elif 'stage' in oOooO0 :
     O0Oo00OoOo ( '[COLOR' + II + ']' + o0OoOo0O00 + '   -   ' + iiI11ii1I1 + '[/COLOR]' , ( oOooO0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0OOoO0 , )
    elif 'vee' in oOooO0 :
     pass
     if 18 - 18: ooOOOoO + I1ii11iIi11i - oO0o / iiiiiiii1 / Ii1IIIi1
def OOoOoO ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 IiIii = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , o0OoOo0O00 , i1iII1IiiIiI1 in IiIii :
  iI1i1iI1iI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oOooO0 , iiI11ii1I1 in iI1i1iI1iI :
   if 'tube' in oOooO0 :
    pass
   elif 'stage' in oOooO0 :
    O0Oo00OoOo ( '[COLOR' + II + ']' + o0OoOo0O00 + '   -   ' + iiI11ii1I1 + '[/COLOR]' , ( oOooO0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + oOo0OOoO0 )
   elif 'vee' in oOooO0 :
    pass
    if 72 - 72: OOooOOo / iiiiiiii1 * I1111IIi % iI11I1II1I1I
    if 53 - 53: oO0o . o0o00Oo0O . oOo0O0Ooo * Ii1IIIi1 / I11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: OOooOOo
def III1i1iI1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 o0ooo00o = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( o0ooo00o ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in o0ooo00o :
  iii11II1I ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 16 - 16: ooOoO0O00 - iiiiiiii1 - IIiIiII11i
  if 83 - 83: oOo0O0Ooo - oO0o - I11i / o0o00Oo0O - ooOOOoO . IIiIiII11i
  if 27 - 27: ii1ii11IIIiiI
  if 59 - 59: ii1ii11IIIiiI / IIiIiII11i - I1111IIi % OOooOOo % ii
  if 79 - 79: O0OOOoOoo0 . ii . oOo0O0Ooo * o0o00Oo0O * oO0o - Ii1IIIi1
  if 33 - 33: Ii1I . I1ii11iIi11i + oOo0O0Ooo + I11i
  if 54 - 54: I11i1ii1 * O0OOOoOoo0 * O0OOOoOoo0 % OOooOOo - Ii1IIIi1 % Ii1I
def ooOOo00O00Oo ( ) :
 if 44 - 44: I1ii11iIi11i . Ii1IIIi1 + ooOOOoO
 I1Ii1iIIiiiIi ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 I1Ii1iIIiiiIi ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 93 - 93: IIiIiII11i . Ii + IIiIiII11i % o000O0o
 I1I11i ( 'movies' , 'MAIN' )
 if 98 - 98: iiiiiiii1 * o000O0o * OOooOOo + ii1ii11IIIiiI * O0OOOoOoo0
def ii11iI1iIiiI ( ) :
 I1Ii1iIIiiiIi ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 I1Ii1iIIiiiIi ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 99 - 99: Ii - O0OOOoOoo0
 I1I11i ( 'movies' , 'MAIN' )
def o0O0O0O00o ( ) :
 if 83 - 83: o0o00Oo0O % IIiIiII11i + I11i / ii
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 iiIIii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 75 - 75: IIiIiII11i . oOo0O0Ooo + Ii1IIIi1 - OOooOOo - o0o00Oo0O . ooOOOoO
 for oOOo00O0OOOo in iiIIii :
  i11I1I1iiI = O0Oo000ooO00 + oOOo00O0OOOo + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( i11I1I1iiI )
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , O0OoooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    I11iIi1i1I1i1 ( iiI11ii1I1 , oOooO0 , 222 , I1iIi1iIiiIiI , O0OoooO0 , i11IIIiI1I )
    if 14 - 14: ooOOOoO
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 18 - 18: oOo0O0Ooo
    if 23 - 23: ii * IIiIiII11i
def oOOOOO0 ( ) :
 if 4 - 4: I11i + ooOOOoO / O0OOOoOoo0 + ooOoO0O00 % I11i % O0OOOoOoo0
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 iiIIii = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 80 - 80: ii1ii11IIIiiI
 for oOOo00O0OOOo in iiIIii :
  iioOO = O0Oo000ooO00 + oOOo00O0OOOo + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( iioOO )
  i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for iiI11ii1I1 , i11IIIiI1I , oOooO0 , oOo0OOoO0 , O0OoooO0 , I1I in i1IIIII11I1IiI :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    I1Ii1iIIiiiIi ( iiI11ii1I1 , oOooO0 , I1I , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
    if 38 - 38: ooOOOoO . I1111IIi - oO0o . oOo0O0Ooo
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 65 - 65: iiiiiiii1
    if 31 - 31: Ii / OOooOOo % Ii1I
def iiII1i1111II ( ) :
 if 78 - 78: Ii + iiiiiiii1 - I11i1ii1 * ii * ii1ii11IIIiiI * iI11I1II1I1I
 OoO000O0Oo = OoOooO ( O0Oo000ooO00 + 'spongemain.php' )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , i11IIIiI1I , oOooO0 , oOo0OOoO0 , O0OoooO0 , I1I in i1IIIII11I1IiI :
  I1Ii1iIIiiiIi ( iiI11ii1I1 , oOooO0 , I1I , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
  I1I11i ( 'movies' , 'MAIN' )
def Ii11Iiii1iiii ( url ) :
 if 10 - 10: O0OOOoOoo0 % I1ii11iIi11i
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i111111 = ( '%s%s' % ( o0oO0OOoO0OoO0 , url ) )
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in i1IIIII11I1IiI :
  I1i1iii1Ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
  for oOOOoo00 in I1i1iii1Ii :
   if oOOOoo00 == url :
    iiI11ii1I1 = ( '[COLORred]Watched - [/COLOR]' + iiI11ii1I1 ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  I11iIi1i1I1i1 ( iiI11ii1I1 , url , 222 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
  if 37 - 37: o000O0o % iiiiiiii1 % o000O0o
  I1I11i ( 'movies' , 'MAIN' )
  if 14 - 14: oO0o / oOo0O0Ooo
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 66 - 66: I1ii11iIi11i / Ii % I11i1ii1
  if 43 - 43: Ii1IIIi1
def o0IiiIIII1I1i ( url ) :
 if 26 - 26: O0OOOoOoo0 - I1ii11iIi11i + oOo0O0Ooo + I11i
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , i11IIIiI1I , url , oOo0OOoO0 , O0OoooO0 , I1I in i1IIIII11I1IiI :
  I1Ii1iIIiiiIi ( iiI11ii1I1 , url , I1I , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
  if 37 - 37: I11i * Ii1IIIi1 + oOo0O0Ooo . Ii1I * ii
  I1I11i ( 'movies' , 'MAIN' )
  if 82 - 82: Ii + iI11I1II1I1I / I1ii11iIi11i + Ii1IIIi1 * IIiIiII11i
  if 34 - 34: I11i % ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 36 - 36: oOo0O0Ooo
def I11iIi1i1I1i1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 64 - 64: Ii + ooOoO0O00 % o0o00Oo0O . ooOOOoO
 OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0oOOo00O = True
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OO0oIII111i11IiI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0000 = [ ]
  O0000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   O0000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OO0oIII111i11IiI . addContextMenuItems ( O0000 )
 OOO0oOOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = False )
 return OOO0oOOo00O
 if 64 - 64: I11i1ii1 / ooOoO0O00 % O0OOOoOoo0
def I1Ii1iIIiiiIi ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 84 - 84: OOooOOo - I1ii11iIi11i . I11i1ii1 . I1111IIi - I1ii11iIi11i
 OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0oOOo00O = True
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OO0oIII111i11IiI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0000 = [ ]
  O0000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   O0000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OO0oIII111i11IiI . addContextMenuItems ( O0000 )
 OOO0oOOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = True )
 return OOO0oOOo00O
if 99 - 99: iiiiiiii1
if 75 - 75: I11i1ii1 . Ii1IIIi1 / I1111IIi
if 84 - 84: ii . oOo0O0Ooo / I11i
if 86 - 86: I1ii11iIi11i % OOooOOo
if 77 - 77: ii1ii11IIIiiI % Ii1IIIi1 / o000O0o
if 91 - 91: oO0o / oO0o . IIiIiII11i . I11i1ii1 - oOo0O0Ooo
if 23 - 23: oOo0O0Ooo
if 7 - 7: O0OOOoOoo0 % Ii1I
if 64 - 64: iiiiiiii1 + Ii
if 35 - 35: OOooOOo + ooOoO0O00 % Ii1IIIi1
if 68 - 68: I1111IIi . I11i1ii1
if 64 - 64: ooOoO0O00 + I1ii11iIi11i * oOo0O0Ooo / Ii1IIIi1
if 3 - 3: I1ii11iIi11i / I11i1ii1 + I11i1ii1 . Ii1I
if 50 - 50: iI11I1II1I1I * o000O0o
if 85 - 85: ooOoO0O00
def Oo00 ( string ) :
 if OOoOO0oo0ooO == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 41 - 41: oO0o % oOo0O0Ooo - I1ii11iIi11i
def I1iII1II1I1ii ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 oo0OO0O = [ ]
 try :
  if 64 - 64: o000O0o . Ii1I * iiiiiiii1 % oOo0O0Ooo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( IIIii1II1II ) == False :
  Oo00 ( 'Making Favorites File' )
  oo0OO0O . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  Iii1iiI = open ( IIIii1II1II , "w" )
  Iii1iiI . write ( json . dumps ( oo0OO0O ) )
  Iii1iiI . close ( )
 else :
  Oo00 ( 'Appending Favorites' )
  Iii1iiI = open ( IIIii1II1II ) . read ( )
  IiI11II = json . loads ( Iii1iiI )
  IiI11II . append ( ( name , url , iconimage , fanart , mode ) )
  II1IIii1I11I = open ( IIIii1II1II , "w" )
  II1IIii1I11I . write ( json . dumps ( IiI11II ) )
  II1IIii1I11I . close ( )
  if 87 - 87: I1ii11iIi11i . ii * iiiiiiii1 * IIiIiII11i / ooOoO0O00 * OOooOOo
  if 25 - 25: ii1ii11IIIiiI * I11i * o000O0o . oOo0O0Ooo
def o0oo000 ( ) :
 if os . path . exists ( IIIii1II1II ) == False :
  oo0OO0O = [ ]
  Oo00 ( 'Making Favorites File' )
  oo0OO0O . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  Iii1iiI = open ( IIIii1II1II , "w" )
  Iii1iiI . write ( json . dumps ( oo0OO0O ) )
  Iii1iiI . close ( )
 else :
  oo0o0OO = json . loads ( open ( IIIii1II1II ) . read ( ) )
  iiI11I1III = len ( oo0o0OO )
  for i11ii in oo0o0OO :
   iiI11ii1I1 = i11ii [ 0 ]
   oOooO0 = i11ii [ 1 ]
   I1iIi1iIiiIiI = i11ii [ 2 ]
   try :
    i1iiIi1IiiiI = i11ii [ 3 ]
    if i1iiIi1IiiiI == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     i1iiIi1IiiiI = I1iIi1iIiiIiI
    else :
     i1iiIi1IiiiI = O0OoooO0
   try : OO0oooOO = i11ii [ 5 ]
   except : OO0oooOO = None
   try : IIIi1iiIIiiiI = i11ii [ 6 ]
   except : IIIi1iiIIiiiI = None
   if 26 - 26: I11i1ii1 % o000O0o + oOo0O0Ooo / I1111IIi . oOo0O0Ooo
   if i11ii [ 4 ] == 0 :
    iiOOooooO0Oo ( iiI11ii1I1 , oOooO0 , '' , I1iIi1iIiiIiI , O0OoooO0 , '' , 'fav' )
   else :
    iiOOooooO0Oo ( iiI11ii1I1 , oOooO0 , i11ii [ 4 ] , I1iIi1iIiiIiI , O0OoooO0 , '' , 'fav' )
    if 38 - 38: ii + ii - Ii * oOo0O0Ooo * ooOoO0O00 / IIiIiII11i
def OOO00000O ( name ) :
 IiI11II = json . loads ( open ( IIIii1II1II ) . read ( ) )
 for iIiiiII11 in range ( len ( IiI11II ) ) :
  if IiI11II [ iIiiiII11 ] [ 0 ] == name :
   del IiI11II [ iIiiiII11 ]
   II1IIii1I11I = open ( IIIii1II1II , "w" )
   II1IIii1I11I . write ( json . dumps ( IiI11II ) )
   II1IIii1I11I . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 98 - 98: Ii1I
 if 25 - 25: Ii1IIIi1 % Ii1IIIi1
def IiIiIi1I11I ( ) :
 IiIIii1 = os . path . join ( I11i1 , 'addons.ini' )
 IiiIIII1 = open ( IiIIii1 , "w+" )
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oO0OOoo0OO )
 IiiIIII1 . write ( r'[' + IiII + ']' + '\n' )
 for iiI11ii1I1 , oOo0OOoO0 , Iiii , oOooO0 in i1IIIII11I1IiI :
  oOooO0 = ( oOooO0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  oOO0o00 = ( iiI11ii1I1 + '=plugin://' + IiII + '/?url=' + oOooO0 + '&mode=10012&name=' + ( iiI11ii1I1 ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( oOo0OOoO0 ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( oOo0OOoO0 ) . replace ( ' ' , '' ) + '+&amp;description=' )
  IiiIIII1 . write ( oOO0o00 + '\n' )
  if 20 - 20: OOooOOo - ii1ii11IIIiiI . OOooOOo - I11i / I11i
  if 96 - 96: ooOoO0O00 * IIiIiII11i
def o00Oo0O ( ) :
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 in i1IIIII11I1IiI :
  O00oO0 ( '24/7' , oOooO0 , 90021 , III1iII1I1ii + '247Streams.png' )
  if 17 - 17: oO0o
def IIIi11i ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( iiI11ii1I1 , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + '247Streams.png' , III1iII1I1ii + '247Streams.png' , '' )
def oOooO0OoO ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( iiI11ii1I1 , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def I1I1I1IIi1III ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( iiI11ii1I1 , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def oooOOoo0 ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( iiI11ii1I1 , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def Oo00O00o0 ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 i1IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  OOiIiIIi1 ( iiI11ii1I1 , oOooO0 , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 48 - 48: iI11I1II1I1I / I1ii11iIi11i + oO0o % I1ii11iIi11i + ii1ii11IIIiiI + oO0o
  if 97 - 97: I11i1ii1 % Ii % ooOOOoO
def IIi1i ( ) :
 if 56 - 56: I11i / I1111IIi
 iiOOooooO0Oo ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 if 11 - 11: OOooOOo / ooOOOoO
def IIOoOOoOo ( ) :
 if 37 - 37: iI11I1II1I1I . oOo0O0Ooo % oO0o % ii . ii / o0o00Oo0O
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 , III1III11II in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 + '  -  ' + ( III1III11II ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOooO0 , 10023 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 25 - 25: IIiIiII11i % IIiIiII11i - ii1ii11IIIiiI . o0o00Oo0O
  if 79 - 79: I1111IIi / oO0o * ii * OOooOOo + oOo0O0Ooo
  if 68 - 68: ooOOOoO / iI11I1II1I1I . I1ii11iIi11i + Ii + I11i
def OOI1III1I11I1 ( ) :
 if 85 - 85: iiiiiiii1
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
 if 62 - 62: ii1ii11IIIiiI % IIiIiII11i + I1111IIi + Ii1IIIi1 % o000O0o . oOo0O0Ooo
def OOoOo0ooOoo ( url ) :
 O0ooooo000 = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0OOoo0OO = cloudflare . source ( O0ooooo000 )
 i1IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 68 - 68: Ii1IIIi1 + ii1ii11IIIiiI
  if 58 - 58: I1111IIi * ii1ii11IIIiiI . ooOoO0O00
  if 19 - 19: o000O0o
  if 85 - 85: I11i1ii1 - oOo0O0Ooo / ooOoO0O00 / oO0o / IIiIiII11i
def oo0O0O ( ) :
 if 45 - 45: I1ii11iIi11i % I1ii11iIi11i + I1ii11iIi11i / o0o00Oo0O % ii
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 oOooO0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 oO0OOoo0OO = cloudflare . source ( oOooO0 )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 10022 , III1iII1I1ii + 'dtv.png' )
   if 92 - 92: ii1ii11IIIiiI . OOooOOo . ooOOOoO - ii / I11i1ii1
   if 80 - 80: iI11I1II1I1I / Ii + O0OOOoOoo0
   if 41 - 41: iiiiiiii1 + oO0o * oOo0O0Ooo * o0o00Oo0O * I1ii11iIi11i - OOooOOo
def ooooOoo00 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO000oOo00o0o , OoOo00o0OO , IIIIii1111i1 , iiI11ii1I1 in i1IIIII11I1IiI :
  iiI1ii1 = ( IIIIii1111i1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  I1 = ( OoOo00o0OO ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOOoo0 = 'Season ' + I1 + 'Episode ' + iiI1ii1 + iiI11ii1I1
  II1OOO ( oOOoo0 , oO000oOo00o0o )
  if 32 - 32: iI11I1II1I1I * I1ii11iIi11i - o000O0o
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 72 - 72: I1111IIi % ooOoO0O00 / iI11I1II1I1I
  if 95 - 95: o0o00Oo0O . oO0o
def II1OOO ( name , url ) :
 oO000oOo00o0o = url
 ooOo = name
 O0 = cloudflare . source ( oO000oOo00o0o )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for o0ooo00o , OO00oOOO in i1I :
  O0Oo00OoOo ( '[COLOR' + II + ']' + ooOo + OO00oOOO + '[/COLOR]' , o0ooo00o , 222 , III1iII1I1ii + 'dtv.png' )
  if 94 - 94: iiiiiiii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 39 - 39: ii
 if 19 - 19: Ii
def i1iI1 ( ) :
 if 80 - 80: oOo0O0Ooo
 if 58 - 58: o000O0o + Ii1I % OOooOOo
 if 22 - 22: iI11I1II1I1I - ii1ii11IIIiiI / oOo0O0Ooo * I1111IIi
 if 26 - 26: I11i + Ii1IIIi1 - I11i + I1ii11iIi11i . o000O0o
 if 97 - 97: ooOoO0O00
 if 46 - 46: Ii1I
 if 30 - 30: oO0o / o0o00Oo0O * I11i * iiiiiiii1 + ii * O0OOOoOoo0
 iiOOooooO0Oo ( '[COLOR' + II + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , '' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 23 - 23: ooOOOoO
def I1Io0OO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iI11i1I1i = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + oOo0OOoO0 , '' , '' )
 for url in iI11i1I1i :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 96 - 96: iiiiiiii1 / I1111IIi * iI11I1II1I1I + Ii * Ii1I / oOo0O0Ooo
def OoOo0000o0OOo ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iI11i1I1i = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  oOo0OOoO0 = 'http://watchepisodes.cc/' + oOo0OOoO0
  iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 10093 , oOo0OOoO0 , oOo0OOoO0 , '' )
 for url in iI11i1I1i :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 84 - 84: I11i1ii1
def I11i1iiiiIIIi ( url , iconimage ) :
 oOo0OOoO0 = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for IIIIii1111i1 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + IIIIii1111i1 + ' - ' + iiI11ii1I1 + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , oOo0OOoO0 , '' , '' )
  if 13 - 13: o0o00Oo0O + iiiiiiii1 * IIiIiII11i + I1ii11iIi11i * I1111IIi
def i1111ii1I ( url , iconimage ) :
 oOo0OOoO0 = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  if 'player' in iiI11ii1I1 :
   pass
  elif 'vod' in iiI11ii1I1 :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , oOo0OOoO0 , '' , '' )
   if 60 - 60: Ii1IIIi1 * I11i1ii1 * oO0o
   if 64 - 64: ooOOOoO / IIiIiII11i / oO0o - I11i1ii1 * iI11I1II1I1I . O0OOOoOoo0
   if 25 - 25: Ii1IIIi1 - ii1ii11IIIiiI . ooOOOoO
   if 57 - 57: I11i + I1ii11iIi11i * Ii1I - I11i1ii1 % iI11I1II1I1I - ii1ii11IIIiiI
   if 37 - 37: oO0o * ooOOOoO + ii1ii11IIIiiI + Ii1I * I11i
   if 95 - 95: ii1ii11IIIiiI - Ii % Ii - o0o00Oo0O * iiiiiiii1
def ii1 ( ) :
 if 81 - 81: IIiIiII11i * oOo0O0Ooo % ooOoO0O00 * Ii + OOooOOo
 if 100 - 100: ooOoO0O00 % ii1ii11IIIiiI
 if 55 - 55: oOo0O0Ooo + O0OOOoOoo0
 if 85 - 85: o000O0o + O0OOOoOoo0 % O0OOOoOoo0 / ooOOOoO . oOo0O0Ooo - OOooOOo
 if 19 - 19: ooOOOoO / O0OOOoOoo0 + I1111IIi
 if 76 - 76: iI11I1II1I1I / iiiiiiii1 - Ii1I % I11i % Ii1IIIi1 + ii
 if 10 - 10: oO0o * ooOOOoO / I1ii11iIi11i - iiiiiiii1
 if 11 - 11: I1111IIi % Ii1I / I11i1ii1 . Ii + Ii1IIIi1 - IIiIiII11i
 if 50 - 50: ooOoO0O00 * o000O0o / Ii / Ii / o000O0o
 if 84 - 84: Ii1I - O0OOOoOoo0 + Ii1I
 if 63 - 63: ooOOOoO * I11i1ii1 % IIiIiII11i % iiiiiiii1 + oOo0O0Ooo * I1ii11iIi11i
 if 96 - 96: I1111IIi
 if 99 - 99: iI11I1II1I1I - I11i1ii1
 if 79 - 79: oOo0O0Ooo + o000O0o % ooOOOoO % o000O0o
 iiOOooooO0Oo ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , III1iII1I1ii + 'latest.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , III1iII1I1ii + 'popular.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , III1iII1I1ii + 'Genre.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , III1iII1I1ii + 'series.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 if 56 - 56: Ii1I + o000O0o . oO0o + ii * Ii1I - o0o00Oo0O
 if 35 - 35: Ii1IIIi1 . ooOOOoO . iiiiiiii1 - ooOOOoO % ooOOOoO + iiiiiiii1
def oO0oO00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iI1I1i11iIIii = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( iI1I1i11iIIii ) )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 15 - 15: oOo0O0Ooo % o000O0o . I1ii11iIi11i % iI11I1II1I1I
def O00oO0oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 65 - 65: o0o00Oo0O . Ii1I * iiiiiiii1
def iiIiI11IiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'episode' in url :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 23 - 23: oOo0O0Ooo - I11i % o000O0o . o0o00Oo0O * ii + I11i1ii1
  if 53 - 53: I1ii11iIi11i
def I11iIiiI ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 OO000oo0o = 'http://www.watchseriesgo.to/search/' + I11iiIi1i1 . replace ( ' ' , '%20' )
 oO0OOoo0OO = OoOooO ( OO000oo0o )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'watch online' in iiI11ii1I1 :
   pass
  else :
   print oOooO0
   iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.watchseriesgo.to' + oOooO0 , 10044 , oOo0OOoO0 , '' , '' )
   if 4 - 4: iiiiiiii1 * oOo0O0Ooo % oOo0O0Ooo / ii
   xbmcplugin . setContent ( O000oo0O , 'movies' )
   if 52 - 52: o000O0o + iiiiiiii1 * iiiiiiii1 * I1ii11iIi11i - iI11I1II1I1I + Ii1I
def i1iII1111iIIiIIII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , url , iiI11ii1I1 , IIIIii1111i1 , i11IIIiI1I in i1IIIII11I1IiI :
  o0OO0 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( IIIIii1111i1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + o0OO0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , oOo0OOoO0 , '' , i11IIIiI1I )
  if 55 - 55: oO0o / ii
def ooooOOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  o0OO0 = ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + o0OO0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 100 - 100: Ii1IIIi1 % Ii - oOo0O0Ooo * iiiiiiii1 - I11i
def Oooo0o00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , oOo0OOoO0 , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 74 - 74: I1ii11iIi11i / iiiiiiii1 % iiiiiiii1 . I1111IIi
def ooOoo0oo00000O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iI1I1i11iIIii = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for OoOo00o0OO , IiIii in iI1I1i11iIIii :
  i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( IiIii ) )
  for url , iiI11ii1I1 in i1IIIII11I1IiI :
   o0OO0 = ( OoOo00o0OO ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + o0OO0 + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 84 - 84: iI11I1II1I1I
class III1Ii11i1II ( ) :
 if 28 - 28: OOooOOo % o000O0o - Ii1IIIi1 + Ii1IIIi1 + o000O0o / iI11I1II1I1I
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 91 - 91: oOo0O0Ooo / IIiIiII11i * Ii1IIIi1
  o0OO0 = name
  self . Get_Sources ( oOooO0 , o0OO0 )
  if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
  if 83 - 83: Ii1I * iI11I1II1I1I + OOooOOo * ooOoO0O00 . ii % ii1ii11IIIiiI
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  oO0OOoo0OO = OoOooO ( URL )
  i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + oOooO0
   self . Get_site_link ( URL , season_name )
   if 81 - 81: oO0o - iI11I1II1I1I
 def Get_site_link ( self , url , season_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  I1II1 = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for url in i1IIIII11I1IiI :
   self . main ( url , season_name )
  for url in i1I :
   self . main ( url , season_name )
  for url in I1II1 :
   self . main ( url , season_name )
   if 60 - 60: iiiiiiii1
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   ooO0 = 'DACLIPS'
   if ooO0 in III1Ii11i1II . source_list :
    pass
   else :
    self . daclips ( url , season_name , ooO0 )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    ooO0 = 'THEVIDEO'
    if ooO0 in III1Ii11i1II . source_list :
     pass
    else :
     self . thevideo ( url , season_name , ooO0 )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     ooO0 = 'ALLMYVIDEOS'
     if ooO0 in III1Ii11i1II . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , ooO0 )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      ooO0 = 'VIDSPOT'
      if ooO0 in III1Ii11i1II . source_list :
       pass
      else :
       self . vidspot ( url , season_name , ooO0 )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       ooO0 = 'VODLOCKER'
       if ooO0 in III1Ii11i1II . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , ooO0 )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        ooO0 = 'VIDTO'
        if ooO0 in III1Ii11i1II . source_list :
         pass
        else :
         self . vidto ( url , season_name , ooO0 )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 35 - 35: I1ii11iIi11i * o000O0o / ii + o0o00Oo0O / ii / Ii1IIIi1
       else :
        if 'youwatch' in url :
         ooO0 = 'YouWatch'
         if ooO0 in III1Ii11i1II . source_list :
          pass
         else :
          self . youwatch ( url , season_name , ooO0 )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 44 - 44: ooOoO0O00 . Ii1I - I11i1ii1 . Ii1IIIi1 . I11i + o000O0o
          if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + ii1ii11IIIiiI % ooOoO0O00 . o000O0o
 def allmyvid ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for O0ooO00oO , iiI11ii1I1 in i1IIIII11I1IiI :
   self . Printer ( O0ooO00oO , season_name , source_name )
   if 57 - 57: o000O0o
 def vidspot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0ooO00oO , iiI11ii1I1 in i1IIIII11I1IiI :
   self . Printer ( O0ooO00oO , season_name , source_name )
   if 92 - 92: IIiIiII11i - oO0o - Ii1IIIi1 % oOo0O0Ooo - OOooOOo * iiiiiiii1
 def thevideo ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0ooO00oO in i1IIIII11I1IiI :
   self . Printer ( O0ooO00oO , season_name , source_name )
   if 16 - 16: iI11I1II1I1I + ii - I11i1ii1 * I1111IIi
 def vodlocker ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0ooO00oO in i1IIIII11I1IiI :
   self . Printer ( O0ooO00oO , season_name , source_name )
   if 37 - 37: O0OOOoOoo0
 def daclips ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oO0OOoo0OO )
  for O0ooO00oO in i1IIIII11I1IiI :
   self . Printer ( O0ooO00oO , season_name , source_name )
   if 15 - 15: I11i % oO0o / O0OOOoOoo0
 def filehoot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0ooO00oO in i1IIIII11I1IiI :
   self . Printer ( O0ooO00oO , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0ooO00oO in i1IIIII11I1IiI :
   self . Printer ( O0ooO00oO , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0ooO00oO in i1IIIII11I1IiI :
   self . youplay ( O0ooO00oO , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for O0ooO00oO in i1IIIII11I1IiI :
   self . Printer ( O0ooO00oO , season_name , source_name )
   if 36 - 36: oO0o + oO0o % I1ii11iIi11i + I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
 def Printer ( self , Link , season_name , source_name ) :
  if 20 - 20: Ii1IIIi1 * o000O0o
  if Link in III1Ii11i1II . List :
   pass
  elif source_name in III1Ii11i1II . source_list :
   pass
  else :
   O0Oo00OoOo ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 222 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   III1Ii11i1II . List . append ( Link )
   III1Ii11i1II . source_list . append ( source_name )
   if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . Ii1IIIi1
   xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 31 - 31: o000O0o % ooOoO0O00 . ii - I11i + ii
   if 45 - 45: Ii1IIIi1 + ooOOOoO / ii - ii1ii11IIIiiI + ii
   if 42 - 42: iI11I1II1I1I * oOo0O0Ooo * iiiiiiii1
   if 62 - 62: Ii1IIIi1 * o0o00Oo0O % I1111IIi . I1111IIi . oOo0O0Ooo
   if 91 - 91: ooOoO0O00 . O0OOOoOoo0
def II1I1I1Ii ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 37 - 37: O0OOOoOoo0 - ooOOOoO + iI11I1II1I1I / iiiiiiii1 - oO0o . I11i
def oO0000Oo ( url ) :
 IIIi11Ii111I1 = '20'
 Ooi11 = [ ]
 O00oOoOo0ooO0O0oo = '                                                    '
 ii11IiI = '        '
 iiOOooooO0Oo ( O00oOoOo0ooO0O0oo + 'pl' + ii11IiI + 'w' + ii11IiI + 'd' + ii11IiI + 'l' + ii11IiI + 'f' + ii11IiI + 'a' + ii11IiI + 'pts' , '' , '' , '' , '' , '' )
 OoO000O0Oo = I11o0oO00oO0o0o0 ( url )
 i1IIIII11I1IiI = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for I1iI1Ii11 , I1II11IIi11i , oo00ooOo , o0IiIiI111IIII1 , Ooo00OoO0O00 , OOoO , Iii1iiI , ii1ii1i1ii , iIi1Iii1 in i1IIIII11I1IiI :
  oooo = I11iii1iIIIIi ( I1II11IIi11i )
  III1i1iiI1 = I11iii1iIIIIi ( oo00ooOo )
  O0ooO0O00oo0 = I11iii1iIIIIi ( o0IiIiI111IIII1 )
  II1i1iI = I11iii1iIIIIi ( Ooo00OoO0O00 )
  iI111I1 = I11iii1iIIIIi ( OOoO )
  iIiii1IIi1I = I11iii1iIIIIi ( Iii1iiI )
  Ooi11 . append ( I1iI1Ii11 [ 0 ] )
  IiIiii1IiI = len ( Ooi11 )
  oo0o0ooOoo00O = int ( len ( O00oOoOo0ooO0O0oo ) - len ( I1iI1Ii11 ) - 2 )
  if len ( Ooi11 ) >= 10 :
   oo0o0ooOoo00O = oo0o0ooOoo00O - 1
  if len ( Ooi11 ) <= int ( IIIi11Ii111I1 ) :
   OOiIiIIi1 ( str ( IiIiii1IiI ) + ' ' + I1iI1Ii11 + O00oOoOo0ooO0O0oo [ 0 : oo0o0ooOoo00O ] + I1II11IIi11i + oooo + oo00ooOo + III1i1iiI1 + o0IiIiI111IIII1 + O0ooO0O00oo0 + Ooo00OoO0O00 + II1i1iI + OOoO + iI111I1 + Iii1iiI + iIiii1IIi1I + ' ' + iIi1Iii1 , '' , '' , '' , '' , '' )
   if 2 - 2: o000O0o . Ii1IIIi1
   if 43 - 43: iI11I1II1I1I
def I11iii1iIIIIi ( space ) :
 if len ( space ) > 1 :
  ooo0oo00O00Oo = len ( '        ' ) - len ( space ) + 1
  space = int ( ooo0oo00O00Oo ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 29 - 29: I1111IIi % I11i1ii1 + oO0o . ooOoO0O00 + oOo0O0Ooo
def I111I ( ) :
 if 58 - 58: iI11I1II1I1I / oOo0O0Ooo
 if 64 - 64: Ii1I / O0OOOoOoo0 / OOooOOo + I11i . ii1ii11IIIiiI . o000O0o
 if 9 - 9: I1111IIi - IIiIiII11i * oO0o
 if 78 - 78: iI11I1II1I1I / o0o00Oo0O * o000O0o / O0OOOoOoo0 / OOooOOo
 if 15 - 15: I11i1ii1 / o000O0o
 if 54 - 54: I11i1ii1 - iI11I1II1I1I - ooOOOoO % ii1ii11IIIiiI / IIiIiII11i
 if 80 - 80: Ii % iI11I1II1I1I / Ii
 if 66 - 66: OOooOOo . iI11I1II1I1I * Ii1I - ii1ii11IIIiiI - iI11I1II1I1I
 if 28 - 28: OOooOOo % ii
 if 13 - 13: I1111IIi . I1ii11iIi11i - ooOOOoO / o000O0o - I1ii11iIi11i - oOo0O0Ooo
 if 84 - 84: IIiIiII11i
 if 57 - 57: o0o00Oo0O * iI11I1II1I1I % o0o00Oo0O . ii
 if 53 - 53: ii1ii11IIIiiI / oOo0O0Ooo * ii1ii11IIIiiI + I11i + o000O0o - I1ii11iIi11i
 if 16 - 16: oO0o % iiiiiiii1 . ooOoO0O00 / Ii1I - o0o00Oo0O
 if 85 - 85: ooOoO0O00 . ooOoO0O00
 if 16 - 16: oOo0O0Ooo - Ii1IIIi1 % ii1ii11IIIiiI . Ii1IIIi1 + Ii1I % Ii
 if 59 - 59: Ii - ooOOOoO
 if 59 - 59: ii * I11i / iiiiiiii1
 if 75 - 75: I11i - ii
 if 21 - 21: oOo0O0Ooo + iI11I1II1I1I / Ii / o000O0o
 if 66 - 66: ii + O0OOOoOoo0 . I1111IIi % ooOoO0O00
 if 58 - 58: Ii1IIIi1 % O0OOOoOoo0 * o0o00Oo0O + Ii1I - I1111IIi
 if 26 - 26: ooOoO0O00 / oOo0O0Ooo / ooOOOoO + ooOOOoO
 if 46 - 46: iiiiiiii1 % Ii1I + ii1ii11IIIiiI
 if 67 - 67: iI11I1II1I1I . Ii . Ii . Ii / ooOOOoO + I11i1ii1
 if 10 - 10: I11i1ii1 - I1ii11iIi11i % IIiIiII11i
 if 66 - 66: iI11I1II1I1I . iI11I1II1I1I
 if 46 - 46: iiiiiiii1 * o000O0o . ii1ii11IIIiiI * iiiiiiii1 * iI11I1II1I1I / ooOOOoO
 if 46 - 46: IIiIiII11i % Ii1I . Ii1IIIi1 . I1ii11iIi11i / Ii + oO0o
 if 47 - 47: I1111IIi . Ii1IIIi1
 if 96 - 96: ooOOOoO % IIiIiII11i / I11i1ii1 % Ii1IIIi1 / I11i1ii1 % Ii
 if 57 - 57: ooOOOoO - ooOOOoO % IIiIiII11i % I1ii11iIi11i . I11i % I1ii11iIi11i
 if 91 - 91: oOo0O0Ooo - oO0o - I1ii11iIi11i - ii1ii11IIIiiI * iI11I1II1I1I
 if 68 - 68: oO0o % o0o00Oo0O * iI11I1II1I1I / o000O0o * I11i + Ii1IIIi1
 if 89 - 89: I11i1ii1 * oOo0O0Ooo . o000O0o
 if 75 - 75: I11i1ii1 - O0OOOoOoo0 % O0OOOoOoo0 + I11i1ii1 * I11i - Ii1I
 if 26 - 26: ooOOOoO * ii1ii11IIIiiI % oOo0O0Ooo + O0OOOoOoo0
 if 38 - 38: O0OOOoOoo0 - I1ii11iIi11i / ii1ii11IIIiiI + o000O0o . O0OOOoOoo0 + I1111IIi
 if 19 - 19: ii1ii11IIIiiI
 if 51 - 51: iI11I1II1I1I
 if 8 - 8: oO0o / I11i % O0OOOoOoo0 . Ii . ii . ii1ii11IIIiiI
 if 8 - 8: oO0o * I1ii11iIi11i
 if 41 - 41: I1ii11iIi11i / oO0o / OOooOOo - Ii - OOooOOo
 if 4 - 4: ooOOOoO . I1111IIi
 if 39 - 39: Ii1IIIi1 . I1ii11iIi11i - OOooOOo * Ii
 if 4 - 4: OOooOOo * o0o00Oo0O - ooOOOoO
 if 72 - 72: ooOOOoO + I11i1ii1 / oOo0O0Ooo . I1111IIi % oO0o / Ii
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
 if 59 - 59: I1111IIi % o000O0o
 if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 i1IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOooO0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOo0OOoO0 , O0o0Oo , '' )
  if 15 - 15: I11i1ii1 / I11i1ii1 % ii . iiiiiiii1
def oOoOooO0OOOoo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iI1I1i11iIIii = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iI1I1i11iIIii in iI1I1i11iIIii :
  o0OoOoOOoOo0o = re . compile ( '(.*?)</h2>' ) . findall ( str ( iI1I1i11iIIii ) )
  for I1I111i in o0OoOoOOoOo0o :
   I1I111i = I1I111i
  OOooOOoO0 = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( iI1I1i11iIIii ) )
  for Ii11i , oOo0OOoO0 , time , i1111O0O000OOOo in OOooOOoO0 :
   iio00 = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( i1111O0O000OOOo )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + I1I111i + ' - ' + Ii11i + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + oOo0OOoO0 , O0o0Oo , ( str ( iio00 ) ) )
   if 62 - 62: ooOOOoO . IIiIiII11i * o0o00Oo0O + ooOoO0O00 * ii + ii
 I1I11i ( 'tvshows' , 'Media Info 3' )
 if 23 - 23: ooOoO0O00
def IIiii1I1I ( ) :
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
 if 62 - 62: IIiIiII11i - OOooOOo * ii1ii11IIIiiI
def oO0OO0O ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  oooOoooOOo0 = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   oooOoooOOo0 = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   O0Oo00OoOo ( '[COLOR' + II + ']' + oooOoooOOo0 + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  oooOoooOOo0 = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   O0Oo00OoOo ( '[COLOR' + II + ']' + oooOoooOOo0 + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
def I1IIII1 ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 if 91 - 91: IIiIiII11i
 if 23 - 23: OOooOOo * I1111IIi / o000O0o
 if 60 - 60: I11i1ii1 * ii1ii11IIIiiI + iiiiiiii1 . Ii1IIIi1 . o0o00Oo0O
 if 8 - 8: IIiIiII11i + IIiIiII11i * ooOoO0O00 * I11i / o0o00Oo0O / o0o00Oo0O
 if 66 - 66: iiiiiiii1 * I11i / I1111IIi * O0OOOoOoo0 / ii
 if 72 - 72: iI11I1II1I1I
 if 82 - 82: OOooOOo . ii1ii11IIIiiI
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  oooOoooOOo0 = iiI11ii1I1 . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in iiI11ii1I1 :
   pass
  else :
   O0Oo00OoOo ( '[COLOR' + II + ']' + oooOoooOOo0 + '[/COLOR]' , url , 10013 , oOo0OOoO0 )
   if 73 - 73: iiiiiiii1
def i1IiIiiiii11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oO0OOoo0OO )
 for o0ooo00o in i1IIIII11I1IiI :
  ooooOO = ( o0ooo00o ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  iii11II1I ( 'http:' + ooooOO )
  if 1 - 1: Ii1IIIi1 % I11i + oO0o
  if 53 - 53: I1ii11iIi11i * ooOOOoO - ii1ii11IIIiiI % oO0o - OOooOOo - O0OOOoOoo0
  if 21 - 21: IIiIiII11i + oO0o - I1ii11iIi11i + oOo0O0Ooo
  if 20 - 20: oO0o
def o00OooooOOOO ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( iiI11ii1I1 , url , 8046 , oOo0OOoO0 )
 for url in i1I :
  O00oO0 ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def oo000oiIIIII ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  iii11II1I ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def IIoooOoOO0o ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 78 - 78: o0o00Oo0O - iiiiiiii1 * Ii1IIIi1 + ooOOOoO + IIiIiII11i
def o0OOOo ( ) :
 O00oO0 ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , III1iII1I1ii + 'documentary.png' )
 O00oO0 ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , III1iII1I1ii + 'documentary.png' )
 O00oO0 ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , III1iII1I1ii + 'Search.png' )
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , oOooO0 , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def IIIiiII1iIi1ii1i ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + oOo0OOoO0 )
 for url in next :
  O00oO0 ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 49 - 49: OOooOOo
  if 99 - 99: o0o00Oo0O + I1111IIi + I11i1ii1 - I11i1ii1 * Ii1I / I1111IIi
def oO00O000o ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   O0Oo00OoOo ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   O00oO0 ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def o0o00 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  O0Oo00OoOo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , '' )
  if 6 - 6: IIiIiII11i % Ii1I % ooOoO0O00 * I11i1ii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iII ( name , url ) :
 oooO0 = 0
 name = name
 url = url
 i111I1 = [ '144' , '240' , '380' , '480' , '720' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  iii1 ( url )
  if 7 - 7: oO0o * O0OOOoOoo0
  if 16 - 16: iiiiiiii1 . ooOoO0O00 . I1111IIi
  if 50 - 50: oO0o - IIiIiII11i * ii - oOo0O0Ooo . o0o00Oo0O + o0o00Oo0O
  if 80 - 80: I11i
  if 50 - 50: I11i1ii1
  if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * Ii1IIIi1
  if 83 - 83: Ii - oOo0O0Ooo * Ii
  if 59 - 59: O0OOOoOoo0 - ii / I11i1ii1 + Ii1I . I11i - O0OOOoOoo0
def iiI1iI1i1 ( ) :
 OoO000O0Oo = O0000OOO0 ( 'http://documentarylovers.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , oOooO0 in i1IIIII11I1IiI :
  if 'genre' in oOooO0 :
   O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oOooO0 , 80010 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOo0O0o0oo ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , oOo0OOoO0 )
 for url in next :
  O00oO0 ( 'NEXT PAGE' , url , 80010 , III1iII1I1ii + 'Next.png' )
  if 25 - 25: ii
def IiIi1I1IiI1II1 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
 for url in i1I :
  o0o00 ( url )
  if 21 - 21: ii . o0o00Oo0O / Ii
def oOOO ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iI1IIi1IiI = 'http://documentarylovers.com/?s=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 i1IiiI1iIi = iI1IIi1IiI . lower ( )
 OOOo0O0o0oo ( i1IiiI1iIi )
 if 71 - 71: oOo0O0Ooo . I11i1ii1
def iI1i11II1i1i ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'films' in url :
   O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , III1iII1I1ii + 'documentary.png' )
def O0O0O00OoO0O ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'films' in url :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + oOo0OOoO0 )
 for url in i1I :
  O00oO0 ( 'NEXT' , url , 8049 , III1iII1I1ii + 'Next.png' )
def i1II11III ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  if 'rtd' in url :
   O0OO0oo ( url )
   if 41 - 41: OOooOOo % iiiiiiii1 * o000O0o * ooOoO0O00
def O0OO0oo ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( OoO000O0Oo )
 for i1i , file in i1IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1i + file )
  iii1 ( url )
  if 32 - 32: oOo0O0Ooo + Ii - iiiiiiii1 / IIiIiII11i
  if 27 - 27: I11i1ii1 . I1ii11iIi11i + I11i1ii1 + O0OOOoOoo0
def III11IiI ( ) :
 oO0OOoo0OO = O0000OOO0 ( 'http://www.stream2watch.co/live-tv' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 , IIiIIIIii in i1IIIII11I1IiI :
  O00oO0 ( ( iiI11ii1I1 + '[COLOR' + II + ']' + IIiIIIIii + '[/COLOR]' ) , oOooO0 , 8086 , oOo0OOoO0 )
  if 6 - 6: Ii1IIIi1 / iI11I1II1I1I / I11i1ii1 / oOo0O0Ooo - ooOoO0O00 - Ii1IIIi1
def Iii1iI1I1iii1 ( url ) :
 oO0OOoo0OO = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8087 , oOo0OOoO0 )
  if 31 - 31: o0o00Oo0O - I1111IIi * Ii * ooOoO0O00
def O0oOo00Oo0oo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  i111 ( url , iiI11ii1I1 )
  if 63 - 63: I11i1ii1 % oOo0O0Ooo . Ii1IIIi1 - I11i1ii1 / I1ii11iIi11i % oOo0O0Ooo
def i111 ( url , name ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  print url
  O0Oo00OoOo ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 39 - 39: I11i . ooOoO0O00 % o000O0o / ooOOOoO % o0o00Oo0O
def o0O0OOooO ( ) :
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oOooO0 , 3002 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def i1II111i1IIii ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def IIIi1ii1i1 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 iiiIiIIiIiiii = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , iiI11ii1I1 in iiiIiIIiIiiii :
  O00oO0 ( '[COLOR' + II + ']Season- ' + iiI11ii1I1 + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  O00oO0 ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1I :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + oOo0OOoO0 )
def o00O0OooO0 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  iii1II11II1 ( url )
def iii1II11II1 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  iii1 ( url )
  if 30 - 30: I1111IIi / Ii % oO0o * Ii1IIIi1
def O0Oooo ( ) :
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOooO0 , 8065 , III1iII1I1ii + 'classicmovies.png' )
def i1oOOOoOO ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  O0OoooI11iI1I ( url )
  if 80 - 80: ii
def II1iiiiII ( ) :
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOooO0 , 8065 , III1iII1I1ii + 'classictv.png' )
def OOoo0o00O0oO ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  if 'mp4' in url :
   iii1 ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 28 - 28: ii % o0o00Oo0O - Ii1IIIi1 / I11i / oOo0O0Ooo
def Iii1iIII1Iii ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oOooO0 , 8071 , III1iII1I1ii + 'streams.png' )
def ii1ii1111 ( url ) :
 oO0OOoo0OO = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  if '(Free Access)' in iiI11ii1I1 :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def iII11iiii111i ( url ) :
 oO0OOoo0OO = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , iiI11ii1I1 , url in i1IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , oOo0OOoO0 , O0OoooO0 , '' )
  if 42 - 42: oO0o % o000O0o / I1ii11iIi11i / I1111IIi
def O0OoOo0 ( ) :
 i111I1 = [ '[COLOR' + II + ']XXX Vids[/COLOR]' , '[COLOR' + II + ']Perfect Girls[/COLOR]' , '[COLOR' + II + ']Best Videos[/COLOR]' , '[COLOR' + II + ']Genres[/COLOR]' , '[COLOR' + II + ']Recently Uploaded[/COLOR]' , '[COLOR' + II + ']100% Verified[/COLOR]' , '[COLOR' + II + ']Tags[/COLOR]' , '[COLOR' + II + ']In Your Language[/COLOR]' , '[COLOR' + II + ']Search[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  Oooooo0O ( 'http://watchxxxfree.com/categories' )
 if iI11iI1IiiIiI == 1 :
  oooo000 ( 'http://www.perfectgirls.net' )
 if iI11iI1IiiIiI == 2 :
  ii1II1I ( 'http://www.xvideos.com/best' )
 if iI11iI1IiiIiI == 3 :
  oOoo0 ( 'http://www.xvideos.com/best' )
 if iI11iI1IiiIiI == 4 :
  ii1II1I ( 'http://www.xvideos.com/best' )
 if iI11iI1IiiIiI == 5 :
  ii1II1I ( 'http://www.xvideos.com/verified/videos' )
 if iI11iI1IiiIiI == 6 :
  oo0o0o ( 'http://www.xvideos.com/tags' )
 if iI11iI1IiiIiI == 7 :
  I1I11I1i1i1II ( 'http://www.xvideos.com/porn' )
 if iI11iI1IiiIiI == 8 :
  ii1II11IIII1 ( )
  if 33 - 33: ii1ii11IIIiiI + OOooOOo - Ii1I + iI11I1II1I1I % ooOoO0O00 * I1111IIi
  if 21 - 21: o0o00Oo0O * I11i1ii1 % oO0o
  if 14 - 14: o0o00Oo0O / iiiiiiii1 / I11i1ii1 + I1111IIi - I1111IIi
  if 10 - 10: o0o00Oo0O - Ii1I / iiiiiiii1 % OOooOOo / ii / ii1ii11IIIiiI
  if 73 - 73: I11i1ii1 + I1111IIi % I11i . Ii1I / Ii1IIIi1 . iiiiiiii1
  if 76 - 76: ooOOOoO . Ii1I * ii % O0OOOoOoo0
  if 24 - 24: ii
  if 83 - 83: o0o00Oo0O / oO0o
  if 62 - 62: ooOOOoO
def o00O00oOooo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a target='_blank' href='([^']*)'><span>(.+?)</span>" ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'ch' in url :
   IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Jizbox.png' , III1iII1I1ii + 'Jizbox.png' , '' )
def ooo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii111I1I1I = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 for iiI11ii1I1 , url in ii111I1I1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Next.png' , '' , '' )
def iIIiIi1IiI1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   Oo0O ( url )
def Iii1I1III11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  iii1 ( url )
def Oooooo0O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , url , iiI11ii1I1 , ooo0oo00O00Oo in i1IIIII11I1IiI :
  if 'category' in url :
   IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]   ' + ooo0oo00O00Oo + '[/COLOR]' , url , 90006 , oOo0OOoO0 , III1iII1I1ii + 'Jizbox.png' , '' )
def i1ii1IiIiIii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii111I1I1I = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , oOo0OOoO0 , '' , '' )
 for url in ii111I1I1I :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , III1iII1I1ii + 'Next.png' , '' , '' )
def OOo0ooOOOo0O0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   Oo0O ( url )
def Oo0O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  iii1 ( url )
def oooo000 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , ooo0oo00O00Oo in i1IIIII11I1IiI :
  if 'category' in url :
   IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORorange]' + ooo0oo00O00Oo + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def ooI1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 oO000oOo00o0o = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii111I1I1I = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , oOo0OOoO0 , '' , '' )
 for url in ii111I1I1I :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , oO000oOo00o0o + '/' + url , 90003 , III1iII1I1ii + 'Next.png' , '' , '' )
def i1Iii1i1II1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  O0o00OoooO ( 'http://www.perfectgirls.net' + url )
def O0o00OoooO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  iii11II1I ( 'http://' + url )
def I1I11I1i1i1II ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , ooo0oo00O00Oo in i1IIIII11I1IiI :
  IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - No of Videos : [COLORorange]' + ooo0oo00O00Oo + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def oo0o0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 ii111I1I1I = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in ii111I1I1I :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , ooo0oo00O00Oo in i1IIIII11I1IiI :
  IIiii11ii1i ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - No of Videos : [COLORorange]' + ( ooo0oo00O00Oo + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 15 - 15: IIiIiII11i - ii1ii11IIIiiI - O0OOOoOoo0 . o000O0o / Ii
def iiIiiiI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 ii111I1I1I = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in ii111I1I1I :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , url , iiI11ii1I1 , Oo0O0oo in i1IIIII11I1IiI :
  IIiii11ii1i ( iiI11ii1I1 + '--' + ( Oo0O0oo ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( oOo0OOoO0 ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 35 - 35: I11i - Ii1I + ooOoO0O00
  if 15 - 15: oOo0O0Ooo / Ii1IIIi1
def ii1II1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , url , iiI11ii1I1 , II1 , IIi1IiiI1II in i1IIIII11I1IiI :
  IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - Porn Quality : [COLORorange]' + IIi1IiiI1II + ' - [COLORred]' + II1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , oOo0OOoO0 , oOo0OOoO0 , IIi1IiiI1II + ' - ' + II1 )
 oO00ooooo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in oO00ooooo :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 40 - 40: Ii1I . Ii - IIiIiII11i - ii * OOooOOo * iiiiiiii1
def oOoo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iI1I1i11iIIii = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii111I1I1I = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in ii111I1I1I :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( iI1I1i11iIIii ) )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if '/c/' in url :
   IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
   if 52 - 52: I11i % IIiIiII11i . ii
   if 7 - 7: IIiIiII11i - Ii1I / ooOOOoO % ii + ooOoO0O00
def ii1II11IIII1 ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 I1Iii1 = ( I11iiIi1i1 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 i1IiiI1iIi = I1Iii1 . lower ( )
 iI1iii1iIiiI = 'http://www.xvideos.com/?k=' + i1IiiI1iIi
 print iI1iii1iIiiI + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0OOoo0OO = OoOooO ( iI1iii1iIiiI )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , oOooO0 , iiI11ii1I1 , II1 , IIi1IiiI1II in i1IIIII11I1IiI :
  IIiii11ii1i ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgreen] - Porn Quality : [COLORorange]' + IIi1IiiI1II + ' - [COLORred]' + II1 + '[/COLOR]' , 'http://www.xvideos.com' + oOooO0 , 10108 , oOo0OOoO0 , oOo0OOoO0 , IIi1IiiI1II + ' - ' + II1 )
 oO00ooooo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in oO00ooooo :
  IIiii11ii1i ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oOooO0 , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
if 9 - 9: IIiIiII11i % I1ii11iIi11i * ii1ii11IIIiiI + I1111IIi % oO0o . ooOoO0O00
if 68 - 68: IIiIiII11i % iiiiiiii1 * Ii
if 9 - 9: IIiIiII11i + Ii1I / O0OOOoOoo0
if 51 - 51: ooOOOoO % Ii1I + ii - oOo0O0Ooo * OOooOOo * O0OOOoOoo0
if 7 - 7: Ii1IIIi1 . I1111IIi . iiiiiiii1 / ii1ii11IIIiiI / I1ii11iIi11i
if 83 - 83: ooOOOoO / I1ii11iIi11i
if 23 - 23: iI11I1II1I1I
if 10 - 10: ooOOOoO - I11i % ii - Ii1I
if 64 - 64: oO0o / oOo0O0Ooo
if 23 - 23: ooOOOoO * iiiiiiii1 * I11i - oOo0O0Ooo % OOooOOo + I11i
if 41 - 41: I1111IIi * ii . I11i1ii1 % Ii
if 11 - 11: iI11I1II1I1I . iiiiiiii1 - I1ii11iIi11i / ooOOOoO + IIiIiII11i
if 29 - 29: ooOOOoO . Ii + ooOoO0O00 - ii1ii11IIIiiI + o0o00Oo0O . oOo0O0Ooo
if 8 - 8: I11i
if 78 - 78: ooOoO0O00 - I1ii11iIi11i
if 48 - 48: ii1ii11IIIiiI - ii + iiiiiiii1 % I11i - OOooOOo . oOo0O0Ooo
if 42 - 42: iiiiiiii1
if 70 - 70: I11i / ooOOOoO + o000O0o % oOo0O0Ooo % I1ii11iIi11i + oO0o
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
def iII11I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "setVideoUrlLow.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( "setVideoUrlHigh.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 I1II1 = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   O0Oo00OoOo ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   O0Oo00OoOo ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in I1II1 :
  if 'http' in url :
   O0Oo00OoOo ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 44 - 44: O0OOOoOoo0
def oOoOoOOOO0o ( url ) :
 oOoOoo0 = xbmc . Player ( ii1II ( ) )
 import urlresolver
 try : oOoOoo0 . play ( url )
 except : pass
 if 57 - 57: O0OOOoOoo0 . ii1ii11IIIiiI * oOo0O0Ooo % iiiiiiii1 + iI11I1II1I1I
 if 85 - 85: iI11I1II1I1I + ii1ii11IIIiiI - IIiIiII11i * I1111IIi * O0OOOoOoo0
def I1OO0o0OoooO00 ( ) :
 if 3 - 3: o0o00Oo0O + o0o00Oo0O - o0o00Oo0O - o0o00Oo0O % ii + o000O0o
 if 20 - 20: oO0o + ooOOOoO . IIiIiII11i / Ii
 if 50 - 50: ii / oO0o % iI11I1II1I1I
 if 41 - 41: Ii1I % Ii1I + I1111IIi . O0OOOoOoo0 % iiiiiiii1 * I11i1ii1
 if 57 - 57: ii1ii11IIIiiI . iiiiiiii1 . IIiIiII11i % ii * o0o00Oo0O + iI11I1II1I1I
 if 94 - 94: ooOoO0O00 * oO0o * OOooOOo
 if 93 - 93: I11i1ii1 / Ii1IIIi1 * o0o00Oo0O
 if 17 - 17: oO0o / I11i1ii1 % oOo0O0Ooo
 if 47 - 47: I1ii11iIi11i * oO0o / I11i * oOo0O0Ooo
 if 60 - 60: Ii1I / I1111IIi . Ii / oO0o % IIiIiII11i
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmdsaW5nLnR2Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="menu-link  main-menu-link">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 8091 , III1iII1I1ii + 'gofish.png' )
def i1II111II1 ( url ) :
 oO0OOoo0OO = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8092 , oOo0OOoO0 )
 for url in next :
  O00oO0 ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
def I11I1iiI1 ( url ) :
 oO0OOoo0OO = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 II1IiI11I1 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 in II1IiI11I1 :
  oOo0OOoO0 = oOo0OOoO0
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 8092 , oOo0OOoO0 )
 for url in next :
  O00oO0 ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
  if 85 - 85: oOo0O0Ooo % Ii
def Ii1I1I11I1I1i ( url ) :
 oO0OOoo0OO = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 41 - 41: ii1ii11IIIiiI . Ii + o0o00Oo0O - ii * o000O0o
  if 33 - 33: I11i1ii1
  if 68 - 68: oOo0O0Ooo . iiiiiiii1 * oO0o % ii
  if 8 - 8: o0o00Oo0O * oOo0O0Ooo - OOooOOo + Ii1I
IiIIiIii1ii = '{PQ},' ; III1I1Iii1 = '{SC},' ; IIIiIII1 = '{XG},' ; OOo0OOo = '{JP},' ; OOIiI1IIIiI1I1i = '{HW},' ; oO00O0oO = '{RT},'
def iI1I ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 iiiIi = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 oOooO0 = 'http://onlinemovies.tube/?s=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 oO000oOo00o0o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 II1Iii = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 O0oooo0OoO0oo = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 IiiiIi1iI1iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 OO00o = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 OOOOoOO0O = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + I11iiIi1i1
 ii11I = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 i1IiIiiiIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 69 - 69: Ii1IIIi1 + Ii1IIIi1 * ii1ii11IIIiiI * ooOOOoO + oOo0O0Ooo
 Oo00O0ooOO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 IiiI = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 46 - 46: Ii1IIIi1
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oOooO0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( oO000oOo00o0o )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1Iii )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( O0oooo0OoO0oo )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 OoOOII1i11i1iIi11 = O0o0O00Oo0o0 ( IiiiIi1iI1iI )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 oo0O0oO0O0O = O0o0O00Oo0o0 ( OOOOoOO0O )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOo0O = O0o0O00Oo0o0 ( ii11I )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 I11iIiii1 = O0o0O00Oo0o0 ( i1IiIiiiIIIIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 17 - 17: ooOOOoO / IIiIiII11i * I11i / I1ii11iIi11i + O0OOOoOoo0 . o000O0o
 if 19 - 19: Ii1IIIi1 * ooOOOoO
 o00oo0000 = O0o0O00Oo0o0 ( Oo00O0ooOO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 iIi1IIi1ii = O0o0O00Oo0o0 ( IiiI )
 if 85 - 85: ooOoO0O00 % I11i * Ii1I * oO0o . IIiIiII11i
 if 69 - 69: ii1ii11IIIiiI / iiiiiiii1 % iiiiiiii1 / I11i1ii1 + iiiiiiii1 / ooOoO0O00
 if 70 - 70: Ii1IIIi1 - I1111IIi . iiiiiiii1
 if 11 - 11: Ii + I11i - iiiiiiii1 * Ii - oOo0O0Ooo
 if 49 - 49: ooOoO0O00 % o000O0o / Ii1IIIi1 . Ii1I - iiiiiiii1
 if 12 - 12: Ii + ooOOOoO - Ii1I
 if 27 - 27: O0OOOoOoo0
 if 22 - 22: OOooOOo / oOo0O0Ooo
 if 33 - 33: ooOOOoO
 if 37 - 37: OOooOOo % I11i * oO0o / Ii * IIiIiII11i * O0OOOoOoo0
 if 70 - 70: I11i1ii1 . Ii % OOooOOo + o000O0o
 if 95 - 95: Ii1I
 if 48 - 48: ooOOOoO
 if I11iIiii1 != 'Failed' :
  OooOoOOo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( I11iIiii1 )
  for oOooO0 , iiI11ii1I1 in OooOoOOo0oO00 :
   O00O = O0o0O00Oo0o0 ( oOooO0 )
   O0Ooo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( O00O )
   for oO00oOOo0Oo , IIiIIIIii in O0Ooo :
    IIiIIIIii = ( IIiIIIIii . replace ( '.' , ' ' ) )
    if i1IiiI1iIi in IIiIIIIii . lower ( ) :
     if '.mkv' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.mp4' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.avi' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.wav' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 14 - 14: iI11I1II1I1I / I11i * I1111IIi
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in i1I :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORred] source Technica[/COLOR]' ) , oOooO0 , 222 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 35 - 35: iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 34 - 34: oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
 if ii1ii1ii != 'Failed' :
  I1II1 = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for Oo0o , iiI11ii1I1 in I1II1 :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( II1Iii + Oo0o ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  oo00OO0000oO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in oo00OO0000oO :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORred] source RaizTv[/COLOR]' ) , oOooO0 , 222 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 30 - 30: oOo0O0Ooo + oOo0O0Ooo
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if OoOOII1i11i1iIi11 != 'Failed' :
  iIii1Ooo0oO0 = [ ]
  IIioo0OO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoOOII1i11i1iIi11 )
  for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in IIioo0OO :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    if iiI11ii1I1 in iIii1Ooo0oO0 :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oOooO0 , 1016 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
     iIii1Ooo0oO0 . append ( iiI11ii1I1 )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0O0oO0O0O != 'Failed' :
  o0Oo0oOooOoOo = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( oo0O0oO0O0O )
  for oOooO0 , oOo0OOoO0 , iiI11ii1I1 in o0Oo0oOooOoOo :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oOooO0 , 7067 , oOo0OOoO0 )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 75 - 75: oOo0O0Ooo - I11i1ii1 - oOo0O0Ooo % o000O0o % ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 13 - 13: I11i1ii1 * oO0o % iI11I1II1I1I / I1111IIi * O0OOOoOoo0 . I1ii11iIi11i
    if 23 - 23: I11i1ii1 / I1111IIi . O0OOOoOoo0 * ii1ii11IIIiiI
    if 87 - 87: Ii
    if 34 - 34: ooOoO0O00
    if 64 - 64: iI11I1II1I1I / I1111IIi / I1ii11iIi11i - Ii1I
    if 100 - 100: I1111IIi + ooOoO0O00 * oO0o
    if 64 - 64: o000O0o * Ii . I1ii11iIi11i
    if 52 - 52: I1ii11iIi11i / I11i1ii1 / O0OOOoOoo0 - I11i / O0OOOoOoo0
    if 74 - 74: ooOoO0O00 . iI11I1II1I1I
    if 85 - 85: oOo0O0Ooo
    if 10 - 10: o0o00Oo0O . IIiIiII11i / ii
    if 72 - 72: ii . I11i + o0o00Oo0O
    if 46 - 46: OOooOOo * ooOOOoO / o000O0o + I1ii11iIi11i + I1111IIi
    if 95 - 95: I11i - ii1ii11IIIiiI
    if 67 - 67: Ii1I * I1ii11iIi11i % I11i
    if 19 - 19: OOooOOo . Ii1IIIi1 . ii
    if 79 - 79: Ii1IIIi1 * I11i1ii1 * oOo0O0Ooo * Ii1I / Ii1I
    if 62 - 62: I11i1ii1 * ii1ii11IIIiiI % Ii1I - ooOoO0O00 - Ii1I
 if o00oo0000 != 'Failed' :
  oOoO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o00oo0000 )
  for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in oOoO0o :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source APPRENTICE[/COLOR]' ) , oOooO0 , 222 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 24 - 24: Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 71 - 71: I1111IIi - ooOoO0O00
    if 56 - 56: OOooOOo + o000O0o
    if 74 - 74: O0OOOoOoo0 / iiiiiiii1 / IIiIiII11i - O0OOOoOoo0 / o000O0o % ooOOOoO
    if 19 - 19: I1111IIi % ii + ii
    if 7 - 7: ooOoO0O00
    if 91 - 91: OOooOOo - OOooOOo . I1111IIi
    if 33 - 33: iiiiiiii1 - iI11I1II1I1I / ii1ii11IIIiiI % o0o00Oo0O
    if 80 - 80: I1111IIi % ii - I1111IIi
    if 27 - 27: iiiiiiii1 - I11i * Ii1I - oOo0O0Ooo
    if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - O0OOOoOoo0 . ii1ii11IIIiiI
 iiIIii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 100 - 100: IIiIiII11i / iiiiiiii1 / O0OOOoOoo0 - Ii1I * iI11I1II1I1I
 for oOOo00O0OOOo in iiIIii :
  i11I1I1iiI = O0Oo000ooO00 + oOOo00O0OOOo + I1IIIii
  I11iIiii1 = O0o0O00Oo0o0 ( i11I1I1iiI )
  if I11iIiii1 != 'Failed' :
   OooOoOOo0oO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( I11iIiii1 )
   for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in OooOoOOo0oO00 :
    if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] - Source Pandoras[/COLOR]' , oOooO0 , 222 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 7 - 7: ooOoO0O00 . I1111IIi % Ii * Ii1I . ooOOOoO % Ii1I
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 35 - 35: oOo0O0Ooo
 iiIIii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 48 - 48: ii % ii - oO0o . OOooOOo
 if 22 - 22: I11i1ii1 . Ii . ii . ooOoO0O00
 for oOOo00O0OOOo in iiIIii :
  i11I1I1iiI = iiiIi + oOOo00O0OOOo
  oo0o = O0o0O00Oo0o0 ( i11I1I1iiI )
  if oo0o != 'Failed' :
   o0IiiiI111I = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0o )
   for Oo0o , iiI11ii1I1 in o0IiiiI111I :
    if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
     O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( iiiIi + oOOo00O0OOOo + Oo0o ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 12 - 12: OOooOOo % Ii1IIIi1 + o000O0o . o0o00Oo0O % iI11I1II1I1I
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: ii
def IIiI1 ( ) :
 if 13 - 13: ooOOOoO + iiiiiiii1 - iiiiiiii1 % o000O0o / ooOOOoO
 if 4 - 4: oOo0O0Ooo + Ii1IIIi1 - I1111IIi + O0OOOoOoo0
 if 78 - 78: ii1ii11IIIiiI
 if 29 - 29: IIiIiII11i
 if 79 - 79: iI11I1II1I1I - Ii + I11i1ii1 - IIiIiII11i . iI11I1II1I1I
 if 84 - 84: I1ii11iIi11i % ooOOOoO * o0o00Oo0O * ooOOOoO
 if 66 - 66: Ii1IIIi1 / iI11I1II1I1I - OOooOOo % o0o00Oo0O . I11i1ii1
 if 12 - 12: I1ii11iIi11i + oOo0O0Ooo
 if 37 - 37: ooOoO0O00 * Ii
 if 95 - 95: Ii % iiiiiiii1 * I1ii11iIi11i + ooOoO0O00 . o0o00Oo0O + Ii1I
 if 7 - 7: oO0o * Ii * iI11I1II1I1I / Ii1IIIi1 / iiiiiiii1
 if 35 - 35: O0OOOoOoo0 * Ii1IIIi1
 if 65 - 65: IIiIiII11i % ooOoO0O00
 if 13 - 13: oO0o * iiiiiiii1 + I1ii11iIi11i - I1111IIi
 if 31 - 31: oO0o
 if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
 if 77 - 77: Ii - iiiiiiii1 . Ii1I % I1ii11iIi11i . ii1ii11IIIiiI
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 if 9 - 9: I11i
 if 55 - 55: Ii1IIIi1 % iI11I1II1I1I + ooOOOoO . I11i1ii1
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 oO000oOo00o0o = 'http://onlinemovies.tube/?s=' + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 II1Iii = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 O0oooo0OoO0oo = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 OO00o = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 71 - 71: Ii / ooOoO0O00 + OOooOOo
 ii11I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 i1IiIiiiIIIIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 OOo0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 23 - 23: Ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 88 - 88: IIiIiII11i - O0OOOoOoo0 / ii
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 71 - 71: Ii1I
 if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
 I1iI = O0o0O00Oo0o0 ( oO00oOOo0Oo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( oO000oOo00o0o )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( II1Iii )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( O0oooo0OoO0oo )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 oo0o = O0o0O00Oo0o0 ( OO00o )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 1 - 1: I1111IIi % ooOoO0O00
 if 41 - 41: oO0o * oO0o / O0OOOoOoo0 + Ii1I . I11i
 oOo0O = O0o0O00Oo0o0 ( ii11I )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 I11iIiii1 = O0o0O00Oo0o0 ( i1IiIiiiIIIIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 ooO = O0o0O00Oo0o0 ( OOo0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / ii1ii11IIIiiI
 if I11iIiii1 != 'Failed' :
  OooOoOOo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( I11iIiii1 )
  for oOooO0 , iiI11ii1I1 in OooOoOOo0oO00 :
   O00O = O0o0O00Oo0o0 ( oOooO0 )
   O0Ooo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( O00O )
   for oO00oOOo0Oo , IIiIIIIii in O0Ooo :
    if i1IiiI1iIi in IIiIIIIii . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + IIiIIIIii + '-[COLORgold] source ' + iiI11ii1I1 + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 80 - 80: Ii1I
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if oOo0O != 'Failed' :
  iIIIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo0O )
  for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in iIIIiI :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] source HeroVision[/COLOR]' ) , oOooO0 , 1016 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 67 - 67: IIiIiII11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 2 - 2: I11i - o0o00Oo0O * ii1ii11IIIiiI % I1111IIi
    if 64 - 64: ooOoO0O00 . I11i1ii1
    if 7 - 7: o000O0o . O0OOOoOoo0 - O0OOOoOoo0 / iiiiiiii1 % I1ii11iIi11i
    if 61 - 61: o000O0o - Ii1I / O0OOOoOoo0 % Ii1I + oO0o / I1ii11iIi11i
    if 10 - 10: Ii / OOooOOo
    if 27 - 27: oOo0O0Ooo / ii
    if 74 - 74: Ii1I % iiiiiiii1 - oO0o * ooOOOoO . ii * oO0o
    if 99 - 99: OOooOOo . O0OOOoOoo0 - ii - o0o00Oo0O
    if 6 - 6: Ii1IIIi1
    if 3 - 3: o0o00Oo0O - iiiiiiii1 * ii1ii11IIIiiI * Ii1IIIi1 / ii1ii11IIIiiI
    if 58 - 58: ii1ii11IIIiiI * iI11I1II1I1I + I11i1ii1 . I11i1ii1
 if ooO != 'Failed' :
  iIiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( ooO )
  for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in iIiI :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    O00oO0 ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORred] RaizTv[/COLOR]' , oOooO0 , 1016 , I1iIi1iIiiIiI )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 74 - 74: I11i1ii1 - I11i * I1111IIi % I11i1ii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  oo0 = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for oOooO0 , oOo0OOoO0 , iiI11ii1I1 , i1iIIi1II1iiI in i1I :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    if 'season' in i1iIIi1II1iiI :
     O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOooO0 , 90054 , oOo0OOoO0 , oOo0OOoO0 , '' )
    if 'episodes' in i1iIIi1II1iiI :
     O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOooO0 , 90044 , oOo0OOoO0 , oOo0OOoO0 , '' )
  for oOooO0 in oo0 :
   O00oO0 ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oOooO0 , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 93 - 93: iI11I1II1I1I / OOooOOo % I1ii11iIi11i * iiiiiiii1 - oO0o - I11i
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if I1iI != 'Failed' :
  ii1i = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( I1iI )
  for oOooO0 , iiI11ii1I1 , oOo0OOoO0 in ii1i :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( iiI11ii1I1 ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oOooO0 , 8022 , oOo0OOoO0 , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 44 - 44: ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 82 - 82: OOooOOo . OOooOOo
    if 10 - 10: I1ii11iIi11i * Ii1I . o000O0o . ii . Ii1IIIi1 * Ii1I
    if 80 - 80: iiiiiiii1 + ooOOOoO . iiiiiiii1 + Ii1IIIi1
    if 85 - 85: Ii . ooOOOoO + ii1ii11IIIiiI / ii1ii11IIIiiI
    if 43 - 43: I1111IIi . ii - IIiIiII11i
    if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * Ii1IIIi1 * o000O0o
    if 19 - 19: iiiiiiii1 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
    if 27 - 27: OOooOOo . o0o00Oo0O / Ii1I . iI11I1II1I1I
    if 15 - 15: ii1ii11IIIiiI + oO0o % iI11I1II1I1I - Ii1I - ooOoO0O00 % I11i
 if ii1ii1ii != 'Failed' :
  I1II1 = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for iiI11ii1I1 in I1II1 :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( II1Iii + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 54 - 54: I1111IIi - IIiIiII11i . I11i1ii1 + ii1ii11IIIiiI
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  oo00OO0000oO = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for iiI11ii1I1 in oo00OO0000oO :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( O0oooo0OoO0oo + iiI11ii1I1 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 45 - 45: o000O0o + IIiIiII11i . O0OOOoOoo0 / Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  o0IiiiI111I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0o )
  for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in o0IiiiI111I :
   if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + iiI11ii1I1 + '-[COLORgold] Source Scooby[/COLOR]' ) , oOooO0 , 1016 , I1iIi1iIiiIiI , iI1IIIii , i11IIIiI1I )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 76 - 76: ii1ii11IIIiiI + O0OOOoOoo0 - I1111IIi * iI11I1II1I1I % ooOoO0O00
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 72 - 72: I11i1ii1 + IIiIiII11i . o0o00Oo0O - O0OOOoOoo0 / ii . iiiiiiii1
 o0OO0O0OO0oO0 = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oOOo00O0OOOo in o0OO0O0OO0oO0 :
  i11I1I1iiI = O0Oo000ooO00 + oOOo00O0OOOo + I1IIIii
  o00oo0000 = O0o0O00Oo0o0 ( i11I1I1iiI )
  if o00oo0000 != 'Failed' :
   oOoO0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( o00oo0000 )
   for iiI11ii1I1 , i11IIIiI1I , oOooO0 , oOo0OOoO0 , O0OoooO0 , I1I in oOoO0o :
    if i1IiiI1iIi in iiI11ii1I1 . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] - Source Pandoras[/COLOR]' , oOooO0 , I1I , oOo0OOoO0 , O0OoooO0 , i11IIIiI1I )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 28 - 28: iI11I1II1I1I . o0o00Oo0O
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 32 - 32: ii
     if 29 - 29: Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iI111iiI1II ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOooO0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( I11iiIi1i1 ) . replace ( ' ' , '+' )
 if 96 - 96: OOooOOo * o0o00Oo0O - IIiIiII11i . I11i1ii1 - ii1ii11IIIiiI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oOooO0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 84 - 84: o000O0o * I11i * I11i - O0OOOoOoo0
 if oO0OOoo0OO != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oOooO0 , iiI11ii1I1 in i1I :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oOooO0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 25 - 25: o000O0o + iiiiiiii1 + oOo0O0Ooo + o0o00Oo0O * IIiIiII11i + oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
o00o0OO0O = '{ZH},' ; oooO00ooO0oOo = '{IX},' ; iiIIiiI = '{LM},'
if 59 - 59: I1ii11iIi11i / I1ii11iIi11i
def OOOOo0oo0o ( url ) :
 iI1I1iii11i = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( iI1I1iii11i )
 for url , OoOo00o0OO , III1III11II , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( OoOo00o0OO ) . replace ( 'Sezon' , ' Season ' ) + ( III1III11II ) . replace ( 'Bölüm' , ' Episode ' ) + iiI11ii1I1 , url , 8063 , '' )
  if 14 - 14: ii1ii11IIIiiI + ii1ii11IIIiiI * ii * ooOOOoO + I1ii11iIi11i . oOo0O0Ooo
  if 61 - 61: Ii1IIIi1 . Ii1IIIi1
  if 17 - 17: IIiIiII11i / I11i1ii1
  if 80 - 80: Ii1IIIi1 * oO0o + ii1ii11IIIiiI
def oo0iI1IIIi11iIII ( url ) :
 iI1I1iii11i = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( iI1I1iii11i )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( iiI11ii1I1 , url , 222 , '' )
  if 72 - 72: I1111IIi . Ii1I / oO0o * Ii % oO0o % I11i1ii1
  if 41 - 41: O0OOOoOoo0 . o0o00Oo0O
  if 74 - 74: I11i . ii1ii11IIIiiI / ooOoO0O00 + Ii1I + ii1ii11IIIiiI + Ii
  if 56 - 56: I1ii11iIi11i - I11i / iI11I1II1I1I / ii1ii11IIIiiI - I1111IIi - I1ii11iIi11i
def O0iIIii1 ( ) :
 if 12 - 12: ooOOOoO . ii1ii11IIIiiI + ooOOOoO - Ii1IIIi1 * O0OOOoOoo0 - o0o00Oo0O
 iI1I1iii11i = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( iI1I1iii11i )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 , III1III11II in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 + '  -  ' + ( III1III11II ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOooO0 , 8063 , oOo0OOoO0 )
  if 44 - 44: ooOoO0O00 % o000O0o / OOooOOo % I1111IIi . Ii1I
def iIO0 ( ) :
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 8002 , oOo0OOoO0 )
def oooO ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , time , url , iiI11ii1I1 , oo0O0oOOO0o in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '%s %s' % ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , time ) , url , 1015 , oOo0OOoO0 , oo0O0oOOO0o )
  if 4 - 4: ooOoO0O00 % I11i % o000O0o . ooOoO0O00
def O0OO0OOo00Oo ( ) :
 if 26 - 26: IIiIiII11i * O0OOOoOoo0 + I11i / o0o00Oo0O + ooOoO0O00 - ooOOOoO
 O00oO0 ( 'Coronation Street' , '' , 8001 , '' )
 O00oO0 ( 'Eastenders' , '' , 8002 , '' )
 O00oO0 ( 'Emmerdale' , '' , 8003 , '' )
 O00oO0 ( 'Hollyoaks' , '' , 8004 , '' )
 O00oO0 ( 'Im a Celebrity' , '' , 8005 , '' )
 if 56 - 56: Ii1IIIi1
 if 76 - 76: ooOoO0O00 % iI11I1II1I1I - I11i + I1111IIi - ooOOOoO
 if 81 - 81: Ii1I + ii - Ii1IIIi1 * o0o00Oo0O
 if 100 - 100: iI11I1II1I1I - OOooOOo
def iIi ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'Holly' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oOooO0 :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 9 - 9: ooOOOoO - IIiIiII11i + iiiiiiii1 / o000O0o % Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 17 - 17: iI11I1II1I1I - I11i1ii1
def OO00O0O ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'East' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oOooO0 :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 52 - 52: Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 93 - 93: O0OOOoOoo0 . Ii
def I1i1IO0OOoooO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'Emmer' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oOooO0 :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 80 - 80: ooOoO0O00 * Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 93 - 93: o0o00Oo0O - Ii - oO0o + ii1ii11IIIiiI
def Oo0OOo ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'Coro' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oOooO0 :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 78 - 78: O0OOOoOoo0
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: O0OOOoOoo0 + iiiiiiii1
def Ooo0O00 ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'Celeb' in iiI11ii1I1 :
   oOo0OOoO0 = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oOooO0 :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , oOo0OOoO0 )
   else :
    pass
    if 43 - 43: Ii
def Ooo00 ( name , url ) :
 iIiI1I1IIi1 = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if iIiI1I1IIi1 :
  oooOOOoO = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  OoO000O0Oo = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( OoO000O0Oo ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  OoO000O0Oo = open_url ( url )
  OOOOoO0O = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( OoO000O0Oo ) [ - 1 ]
  oooOOOoO = OOOOoO0O . replace ( '\\/' , '/' )
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , '' , '' )
 OO0oIII111i11IiI . setPath ( oooOOOoO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO0oIII111i11IiI )
 if 79 - 79: Ii
 if 81 - 81: O0OOOoOoo0 + I1111IIi - Ii
def oo00O0OO0oo0O ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oOooO0 , 7071 , III1iII1I1ii + 'popcorn.png' )
 for oOooO0 , iiI11ii1I1 in i1I :
  O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oOooO0 , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 1 - 1: I1ii11iIi11i * o0o00Oo0O . oOo0O0Ooo + I11i1ii1 / OOooOOo + ooOOOoO
def oO0o0OOO0O ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'Movies' in iiI11ii1I1 :
   O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( oOooO0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def iIII111i1ii1I ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0OOoO0 )
 for url in i1I :
  O00oO0 ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 30 - 30: oOo0O0Ooo * iI11I1II1I1I % O0OOOoOoo0
  if 15 - 15: O0OOOoOoo0 + Ii % o0o00Oo0O % iiiiiiii1 + oO0o * I11i1ii1
def III1I1Iii1iiI ( url ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url , oOo0OOoO0 in i1IIIII11I1IiI :
  if '{{' in iiI11ii1I1 :
   pass
  else :
   O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , oOo0OOoO0 )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
i1Iii11iiI1 = '{UJ},' ; o0ooOO000O = '{WE},' ; iI11iI = '{WP},' ; O0o0ooo00o00 = '{PP},'
def IiiIii11iI1Iii1iI ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url , oOo0OOoO0 in i1IIIII11I1IiI :
  if '{{' in iiI11ii1I1 :
   pass
  else :
   O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , oOo0OOoO0 )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def I1Iii11I ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  OOoO00o00oo ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOoO00o00oo ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 5 - 5: o000O0o - ii / OOooOOo
 if 30 - 30: ooOOOoO % I11i + ooOoO0O00 * ii * oO0o - IIiIiII11i
 if 55 - 55: oO0o
def I111II1ii11I1 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if '(cooltvseries.com)' in iiI11ii1I1 :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , iiI11ii1I1 in i1I :
  if '(cooltvseries.com)' in iiI11ii1I1 :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def iIiiIII ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  iii11II1I ( ( url ) . replace ( ' ' , '%20' ) )
ii1IooO00OO0ooo = '{XX},' ; O0oi1i1ii1Ii111i = '{UD},' ; iiiI1iiI11iii = '{YT},' ; o0O0oOOoo0O0 = '{JS},' ; OO00OOo = '{PF},'
if 24 - 24: Ii . I11i1ii1 + I11i1ii1 - Ii % Ii1IIIi1
def o00OO0 ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oOooO0 ) ) , 222 , oOo0OOoO0 )
  if 77 - 77: I11i
def OoOoO0ooooO0 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'youtu' in url :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + oOo0OOoO0 )
 for url in next :
  O00oO0 ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 63 - 63: I11i1ii1 * o000O0o + I11i1ii1 * ii1ii11IIIiiI + I1ii11iIi11i / Ii1I
def iiOOOO00oO ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 72 - 72: Ii1IIIi1 . OOooOOo / IIiIiII11i
def OOOoO0OooOO0o ( url ) :
 OoO000O0Oo = OoOooO
 i1IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 222 , oOo0OOoO0 )
  if 33 - 33: O0OOOoOoo0 - o0o00Oo0O
  if 22 - 22: I1111IIi / iI11I1II1I1I / I11i
  if 19 - 19: ii
  if 95 - 95: ii1ii11IIIiiI . I1111IIi / ooOOOoO . Ii . I1111IIi
  if 43 - 43: Ii + I11i % I11i * ii / iiiiiiii1
def ii1iOO00O0O00oOOO ( ) :
 if 17 - 17: I11i1ii1
 O00oO0 ( 'All Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'Entertainment' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'Movies' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'Music' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'News' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'Sports' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'Documentary' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'Kids' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'Food' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'Religious' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'USA Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O00oO0 ( 'Other' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 if 25 - 25: ii1ii11IIIiiI * iI11I1II1I1I * I11i + OOooOOo . OOooOOo
 if 3 - 3: oO0o . oOo0O0Ooo . ooOOOoO . Ii1I
def ii11iI11I111I ( Cat_Name ) :
 if 44 - 44: ooOoO0O00 - Ii1I + Ii1I . ooOOOoO / Ii1IIIi1
 IIiIiI1Ii = False
 oOO00o0oooOo0 = '0'
 if Cat_Name == 'All Channels' : IIiIiI1Ii = True
 if Cat_Name == 'Entertainment' : oOO00o0oooOo0 = '1'
 if Cat_Name == 'Movies' : oOO00o0oooOo0 = '2'
 if Cat_Name == 'Music' : oOO00o0oooOo0 = '3'
 if Cat_Name == 'News' : oOO00o0oooOo0 = '4'
 if Cat_Name == 'Sports' : oOO00o0oooOo0 = '5'
 if Cat_Name == 'Documentary' : oOO00o0oooOo0 = '6'
 if Cat_Name == 'Kids' : oOO00o0oooOo0 = '7'
 if Cat_Name == 'Food' : oOO00o0oooOo0 = '8'
 if Cat_Name == 'Religious' : oOO00o0oooOo0 = '9'
 if Cat_Name == 'USA Channels' : oOO00o0oooOo0 = '10'
 if Cat_Name == 'Other' : oOO00o0oooOo0 = '11'
 if 17 - 17: Ii1I
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 print 'Len Match: >>>' + str ( len ( i1IIIII11I1IiI ) )
 for iiI11ii1I1 , oOo0OOoO0 , O0oOoooOo in i1IIIII11I1IiI :
  iIiI1IIiii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0OOoO0 ) . replace ( '\\' , '' )
  if O0oOoooOo == oOO00o0oooOo0 :
   O00oO0 ( iiI11ii1I1 , '' , 7022 , iIiI1IIiii )
  elif IIiIiI1Ii == True :
   O00oO0 ( iiI11ii1I1 , '' , 7022 , iIiI1IIiii )
  else : pass
  if 63 - 63: Ii
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 21 - 21: iiiiiiii1
def o0Ooo0o0ooOooo0 ( Search_Name ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , oOooO0 , oO000oOo00o0o , II1Iii in i1IIIII11I1IiI :
  iIiI1IIiii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( oOo0OOoO0 ) . replace ( '\\' , '' )
  O0Oo00OoOo ( Search_Name + ': Link 1' , ( oOooO0 ) . replace ( '\\' , '' ) , 222 , iIiI1IIiii )
  O0Oo00OoOo ( Search_Name + ': Link 2' , ( oO000oOo00o0o ) . replace ( '\\' , '' ) , 222 , iIiI1IIiii )
  O0Oo00OoOo ( Search_Name + ': Link 3' , ( II1Iii ) . replace ( '\\' , '' ) , 222 , iIiI1IIiii )
  if 83 - 83: ooOoO0O00 % OOooOOo % I1ii11iIi11i
def oooooOO0 ( ) :
 OoO000O0Oo = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , oOooO0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( iiI11ii1I1 , ( oOooO0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def OOO0o0O ( ) :
 OoO000O0Oo = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , oOooO0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( iiI11ii1I1 , ( oOooO0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def I111i ( ) :
 OoO000O0Oo = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , oOooO0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( iiI11ii1I1 , ( oOooO0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 39 - 39: Ii1I
def oOO ( url ) :
 url
 oOOOoo00 = xbmcgui . ListItem ( iiI11ii1I1 , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOOoo00 )
 return
 if 37 - 37: O0OOOoOoo0 + iiiiiiii1 * ii1ii11IIIiiI + I1111IIi
 if 39 - 39: o0o00Oo0O * I1ii11iIi11i - oOo0O0Ooo + ii1ii11IIIiiI / IIiIiII11i
def o00OooO ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( OoO000O0Oo )
 for url , i11IIIiI1I , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , ( i11IIIiI1I ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  O00oO0 ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 1 - 1: OOooOOo + ii . I1111IIi . iI11I1II1I1I
def iIi1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i11IIIiI1I , oOo0OOoO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , i11IIIiI1I )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 IiIii = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii11I1II1 in IiIii :
  OooooOOoo0 = ( Iii11I1II1 ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiOOooooO0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + oOo0OOoO0 , '' , OooooOOoo0 )
  if 96 - 96: iiiiiiii1 % ooOoO0O00 . O0OOOoOoo0 / o0o00Oo0O
def OoOoo ( INFO ) :
 iiIiI1i1 ( 'info for workout' , INFO )
 if 97 - 97: I11i1ii1 * I1ii11iIi11i / I11i . IIiIiII11i / O0OOOoOoo0 / O0OOOoOoo0
 if 25 - 25: O0OOOoOoo0
 if 85 - 85: I1ii11iIi11i + I1ii11iIi11i % ooOOOoO + iiiiiiii1
def oOO00 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( ( iiI11ii1I1 ) . replace ( 'SlyNet' , '' ) , url , 9031 , III1iII1I1ii + 'Sport.png' )
def II1IiII1I1II ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , url , 9032 , III1iII1I1ii + 'icon.png' )
def oooOII111iiI1Ii1 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  if '=' in iiI11ii1I1 :
   pass
  else :
   O0Oo00OoOo ( ( iiI11ii1I1 ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , III1iII1I1ii + 'icon.png' )
def oo0oO0oO00oO ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  if '=' in iiI11ii1I1 :
   pass
  else :
   O0Oo00OoOo ( iiI11ii1I1 , url , 222 , III1iII1I1ii + 'icon.png' )
   if 94 - 94: I11i1ii1 * Ii1IIIi1
   if 59 - 59: iiiiiiii1 * O0OOOoOoo0
   if 31 - 31: ooOOOoO / o0o00Oo0O
def oo00oO0o000 ( url ) :
 O0Oo00OoOo ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 O0Oo00OoOo ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 O00oO0 ( '[COLOR' + II + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , III1iII1I1ii + 'bamf.png' )
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   pass
  else :
   O0Oo00OoOo ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iIi1ii ( url ) :
 O0Oo00OoOo ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 O0Oo00OoOo ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 O00oO0 ( '[COLOR' + II + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , III1iII1I1ii + 'bamf.png' )
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   O0Oo00OoOo ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 37 - 37: I1111IIi / iiiiiiii1 + IIiIiII11i % Ii1IIIi1 * Ii % OOooOOo
 if 65 - 65: o000O0o
 if 82 - 82: I11i
def OoOOOOooOo0 ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 i1IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'Daily' in iiI11ii1I1 :
   O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 9008 , Oo00OOOOO )
def o0000o0OOOo ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  O00oO0 ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def iiiiiI1iii11 ( url ) :
 O0Oo00OoOo ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 O0Oo00OoOo ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 O0Oo00OoOo ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 222 , Oo00OOOOO )
  if 13 - 13: I11i % o0o00Oo0O - iiiiiiii1 * ii / I1ii11iIi11i - ii
def oOo000O00O ( ) :
 OoO000O0Oo = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if '.m3u' in oOooO0 :
   O00oO0 ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oOooO0 ) , 9011 , III1iII1I1ii + 'disclose.png' )
def OooO ( url ) :
 OoO000O0Oo = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( iiI11ii1I1 ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 78 - 78: ii % o000O0o - Ii
def ii1iiIiIII1ii ( ) :
 OoO000O0Oo = OoOooO ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'category' in oOooO0 :
   O00oO0 ( iiI11ii1I1 , 'http://www.disclose.tv/' + oOooO0 , 7010 , III1iII1I1ii + 'disclose.png' )
   if 37 - 37: I1111IIi % ii1ii11IIIiiI % ooOoO0O00
   if 23 - 23: I11i1ii1 - o0o00Oo0O + Ii
def oO0ooOoOooO00o00 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( OoO000O0Oo )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , oOo0OOoO0 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , 'http://www.disclose.tv/' + url , 7011 , oOo0OOoO0 )
 for url in next :
  O00oO0 ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 64 - 64: I1111IIi . Ii1IIIi1
  if 85 - 85: IIiIiII11i % ii1ii11IIIiiI * OOooOOo
def Ii1 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   O0Oo00OoOo ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , iiI11ii1I1 in i1I :
  O0Oo00OoOo ( iiI11ii1I1 , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in I1II1 :
  O0Oo00OoOo ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 22 - 22: I11i1ii1 . I11i * ii1ii11IIIiiI - I11i1ii1 / oOo0O0Ooo
  if 100 - 100: ooOOOoO - Ii1IIIi1 - ii * oO0o * O0OOOoOoo0 + o000O0o
def o0o00O0oO ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 54 - 54: OOooOOo % iI11I1II1I1I
def i111I ( name , url , img ) :
 oO0OOoo0OO = OoOooO ( url )
 iiIIi1Ii1 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1oO00O = len ( iiIIi1Ii1 )
 if 37 - 37: o0o00Oo0O % iiiiiiii1 - oOo0O0Ooo
 if 43 - 43: iiiiiiii1
 if i1oO00O == 1 :
  for IiiIIiIii in iiIIi1Ii1 :
   IiiIIiIii = IiiIIiIii . replace ( 'player' , 'watch' )
   iiI = IiiIIiIii + '&fv=&sou='
   ooo0O0O0OO = OoOooO ( iiI )
   oOooOOoO = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( ooo0O0O0OO )
   for O0ooO00oO in oOooOOoO :
    o0o000OOO = False
    Resolve ( O0ooO00oO )
    if 36 - 36: iiiiiiii1 * iiiiiiii1 % oOo0O0Ooo % o0o00Oo0O . oOo0O0Ooo % ii
 elif i1oO00O > 1 :
  if 96 - 96: o000O0o % iI11I1II1I1I / iI11I1II1I1I . O0OOOoOoo0 . ii1ii11IIIiiI
  for IiiIIiIii in iiIIi1Ii1 :
   iII1I1iIIIiII = OoOooO ( IiiIIiIii )
   I11i1II1i = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( iII1I1iIIIiII )
   oO0Oo0 = I11i1II1i
   oO0Oo0 = ( str ( oO0Oo0 ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + oO0Oo0
   O0Oo00OoOo ( 'DOUBLE LINK' , oO0Oo0 , 424 , '' )
   if 98 - 98: I11i1ii1 - iI11I1II1I1I + Ii1IIIi1 - iI11I1II1I1I
   for url in I11i1II1i :
    O00oO0 ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     oO000oOo00o0o = Google . resolve ( url )
    except :
     pass
    try :
     o0O0iiI = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( oO000oOo00o0o ) )
     for i1I1IIIII1IIi , i11iii1II1I1 in o0O0iiI :
      if 25 - 25: IIiIiII11i * ooOoO0O00 + I1111IIi * I11i / Ii1IIIi1
      HD_URLS . append ( i1I1IIIII1IIi )
      SD_URLS . append ( i11iii1II1I1 )
    except :
     pass
 else :
  pass
  if 66 - 66: Ii . oO0o / OOooOOo - iiiiiiii1
def O0O0oooo ( ) :
 if 90 - 90: Ii1IIIi1 . OOooOOo . oOo0O0Ooo . I1111IIi
 if 52 - 52: ii1ii11IIIiiI - I1ii11iIi11i
 O00oO0 ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 48 - 48: iI11I1II1I1I * Ii / oO0o / oOo0O0Ooo
 O00oO0 ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 93 - 93: o000O0o
 if 57 - 57: ooOOOoO . iI11I1II1I1I + ooOOOoO . I1111IIi + I1111IIi
def OOO0 ( ) :
 OoO000O0Oo = OoOooO ( 'http://cnfstudio.com/' )
 i1IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , 'http://cnfstudio.com/genre/' + oOooO0 , 7003 , III1iII1I1ii + 'icon.png' )
  if 97 - 97: O0OOOoOoo0 + o000O0o * IIiIiII11i * I1ii11iIi11i
OOooO0OOoo = xbmcgui . Dialog ( )
if 30 - 30: I1ii11iIi11i / o0o00Oo0O
I1ii1i = '{UN},' ; ooOoOOooOOO0 = '{IG},' ; o0o00O00Oo0 = '{PL},' ; ooOO0oo0o0o = '{LO},' ; I1i1IiIi1111 = '{LP},' ; iIiiiI1i1iiiI = '{HA},' ; III1i1iII1 = '{XD},' ; IiiiiI11iii11iI = '{TA},' ; I111iIii1i1 = '{DP},' ; I1i1I1i1I1 = '{JT},' ; i1IOO = '{JJ},' ; Oo0OO0ooO0O0O = '{MM},' ; oO00O = '{FQ},' ; ooooooO0o00 = '{HH},'
if 56 - 56: Ii % I11i1ii1 * I1111IIi . OOooOOo * Ii1IIIi1
def OOOOoOO00 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( OoO000O0Oo )
 i111Ii1i = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 , url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , oOo0OOoO0 )
 i111Ii1i = i111Ii1i
 for url in i111Ii1i :
  O00oO0 ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 12 - 12: Ii1IIIi1 % IIiIiII11i
def o00oOo0oO0oOO ( url ) :
 if 51 - 51: IIiIiII11i / ii . o000O0o * I1ii11iIi11i
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  i1i = url + '&fv=&sou='
  i1i = i1i . replace ( 'player' , 'watch' )
  o0o0OO0OO = Iiii1I1iI ( i1i )
  iIi1iII1iii1 = Iiii1I1iI ( url )
  if 96 - 96: ii / ii1ii11IIIiiI / oO0o % OOooOOo + ooOOOoO
  if 16 - 16: ooOOOoO % I11i1ii1 - Ii
def Iiii1I1iI ( url ) :
 if 38 - 38: I11i / Ii1I - o0o00Oo0O
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  O0OoooI11iI1I ( url )
  if 21 - 21: Ii1IIIi1
  if 77 - 77: IIiIiII11i
def Oo0o0o00Oo ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , III1iII1I1ii + 'LocalM3U.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , III1iII1I1ii + 'RemoteM3U.png' , O0o0Oo , '' )
 if 67 - 67: I11i % I11i * I11i1ii1 - Ii / iI11I1II1I1I % oOo0O0Ooo
def ooo0o ( ) :
 if os . path . exists ( iiI1IiI ) :
  o0OOO0O00Oo00 = open ( iiI1IiI , 'r' )
  for oOOOoo00 in o0OOO0O00Oo00 :
   ooooO0O = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oOOOoo00 )
   for iiI11ii1I1 , oOooO0 in ooooO0O :
    O0Oo00OoOo ( iiI11ii1I1 , oOooO0 , 222 , III1iII1I1ii + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 15 - 15: ii
def iII1i ( url ) :
 if os . path . exists ( Remote ) :
  oO0OOoo0OO = O0000OOO0 ( url )
  i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for iiI11ii1I1 , url in i1IIIII11I1IiI :
   url = ( url ) . strip ( )
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 74 - 74: Ii1I * I1111IIi * I1111IIi . O0OOOoOoo0 + o000O0o + I11i1ii1
  if 28 - 28: ii . iI11I1II1I1I % o0o00Oo0O - oO0o * Ii
def Iiii1i1 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in i1IIIII11I1IiI :
  oOooO0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oOooO0
 iiI11ii1I1 = 'plugin.video.GenieTv'
 if 69 - 69: Ii . iiiiiiii1
 OO0oooOo ( oOooO0 , iiI11ii1I1 )
 if 71 - 71: ii - O0OOOoOoo0 + ii1ii11IIIiiI / o0o00Oo0O % I11i + oO0o
def i1IiiiI1iI ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in i1IIIII11I1IiI :
  oOooO0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oOooO0
 iiI11ii1I1 = 'repository.GenieTv'
 if 83 - 83: I1111IIi * Ii1I / I1111IIi * I1111IIi - Ii1IIIi1
 OO0oooOo ( oOooO0 , iiI11ii1I1 )
 if 89 - 89: oO0o % ooOOOoO
 if 51 - 51: I11i1ii1 * ii1ii11IIIiiI * ii % OOooOOo
def OOI1iI1ii1II ( ) :
 i111I1 = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  Ii1iI1iiIiII1 ( )
 if iI11iI1IiiIiI == 1 :
  i1iI111i1I ( )
  if 39 - 39: o000O0o + Ii1I + I1111IIi . I11i
  if 11 - 11: ii1ii11IIIiiI / OOooOOo - oO0o + OOooOOo
  if 51 - 51: I11i1ii1
  if 42 - 42: I11i - Ii1IIIi1 / Ii1IIIi1 / O0OOOoOoo0 * I1ii11iIi11i . I1ii11iIi11i
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
oo0Ooo = 'https://addons.tvaddons.ag/'
if 21 - 21: I1111IIi - oOo0O0Ooo . Ii1IIIi1 - o000O0o
def i1iI111i1I ( ) :
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 iI1iii1iIiiI = 'https://addons.tvaddons.ag/search/?keyword=' + i1IiiI1iIi
 oO0OOoo0OO = OoOooO ( iI1iii1iIiiI )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , ooooo , iiI11ii1I1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , oOooO0 , 10054 , 'https://addons.tvaddons.ag/' + ooooo , O0o0Oo , '' )
  if 1 - 1: iI11I1II1I1I / Ii * IIiIiII11i
  if 48 - 48: Ii1I + o0o00Oo0O * o000O0o + Ii1I + Ii1I
def Ii1iI1iiIiII1 ( ) :
 oO0OOoo0OO = OoOooO ( oo0Ooo )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'Repositories' in iiI11ii1I1 :
   pass
  elif 'Services' in iiI11ii1I1 :
   pass
  elif 'International' in iiI11ii1I1 :
   pass
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , oOooO0 , 10053 , 'https://addons.tvaddons.ag/' + oOo0OOoO0 , O0o0Oo , '' )
   if 60 - 60: IIiIiII11i % I1ii11iIi11i
   if 62 - 62: o0o00Oo0O + O0OOOoOoo0 - O0OOOoOoo0 % iI11I1II1I1I
def Addon ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1III1i = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if 'Please' in iiI11ii1I1 :
   pass
  else :
   OOiIiIIi1 ( iiI11ii1I1 , url , 10054 , 'https://addons.tvaddons.ag/' + oOo0OOoO0 , O0o0Oo , '' )
 for url in i1III1i :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
  if 39 - 39: IIiIiII11i - ii1ii11IIIiiI / o000O0o . I1111IIi % oOo0O0Ooo
  if 18 - 18: ii * OOooOOo . IIiIiII11i + o0o00Oo0O - ii * I11i
def Ii1IiIiI1Ii ( url , name ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'plugin' in url :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + url
   O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
   o0oOoO00o = xbmcgui . DialogProgress ( )
   o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
   oooooo0O000o = os . path . join ( O0O00Oo , name + '.zip' )
   try :
    os . remove ( oooooo0O000o )
   except :
    pass
   downloader . download ( url , oooooo0O000o , o0oOoO00o )
   OoO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
   time . sleep ( 2 )
   o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
   print '======================================='
   print OoO
   print '======================================='
   extract . all ( oooooo0O000o , OoO , o0oOoO00o )
   oOOo0O00o ( )
   if 60 - 60: ooOOOoO * oOo0O0Ooo . I11i1ii1
def OO0oooOo ( url , name ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "GenieTv" , "Downloading Content" , '' , 'Please Wait' )
 oooooo0O000o = os . path . join ( O0O00Oo , name + '.zip' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OoO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Extracting Zip Please Wait" )
 print '======================================='
 print OoO
 print '======================================='
 extract . all ( oooooo0O000o , OoO , o0oOoO00o )
 oOOo0O00o ( )
 if 24 - 24: I11i1ii1
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 79 - 79: ooOoO0O00 . ooOOOoO % oO0o % I1111IIi - o000O0o - Ii
 if 97 - 97: Ii1I / ii % oO0o
def OOOOO0ooOOOoo ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , ooooo , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , url , 1007 , ooooo )
def ooo0o0oOoOO0 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , ooooo , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , ooooo )
  if 56 - 56: I1ii11iIi11i % Ii / ii1ii11IIIiiI . iiiiiiii1 . oO0o - OOooOOo
def i1iIiIIiIIII1 ( ) :
 OoO000O0Oo = OoOooO ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , O0OoooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  Iii1iii11 ( iiI11ii1I1 , 100109 , oOooO0 , image = I1iIi1iIiiIiI , isFolder = True )
  if 29 - 29: ii / I1111IIi % ooOOOoO . Ii1IIIi1 + iiiiiiii1
def oO0OOOo0OO ( url ) :
 import random
 i1IiI = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 i1IiI . clear ( )
 I1iI1i = [ ]
 iIIi = [ ]
 oooOoooOOo0 = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oO000oOo00o0o , I1iIi1iIiiIiI , i11IIIiI1I , O0OoooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  I1iI1i . append ( [ oO000oOo00o0o , iiI11ii1I1 ] )
  if len ( I1iI1i ) == len ( i1IIIII11I1IiI ) :
   for oOOOoo00 in I1iI1i :
    iI1II = random . randint ( 1 , len ( I1iI1i ) )
    try :
     i11i1IIi = I1iI1i [ int ( iI1II ) ]
    except :
     pass
    if len ( iIIi ) <= 20 :
     if i11i1IIi [ 1 ] not in oooOoooOOo0 :
      O0 = OoOooO ( i11i1IIi [ 0 ] )
      I1II1 = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( O0 )
      for Oo0oiiiii11i , OOoOOo0o0OOo0 in I1II1 :
       oooooOoo0ooo = OoOooO ( Oo0oiiiii11i )
       oo00OO0000oO = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oooooOoo0ooo )
       for iiiI11I , i1i in oo00OO0000oO :
        if 'panda' in i1i :
         OoOOII1i11i1iIi11 = OoOooO ( i1i )
         IIioo0OO = re . compile ( "url: '(.+?)'" ) . findall ( OoOOII1i11i1iIi11 )
         for OOo in IIioo0OO :
          if 'http' in OOo :
           OO0oIII111i11IiI = xbmcgui . ListItem ( i11i1IIi [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : i11i1IIi [ 1 ] } )
           OO0oIII111i11IiI . setProperty ( "IsPlayable" , "true" )
           i1IiI . add ( OOo , OO0oIII111i11IiI )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OO0oIII111i11IiI )
           if 43 - 43: I1111IIi / ooOOOoO + oO0o
def Iii1iii11 ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = Oo00OOOOO
 OO0 = sys . argv [ 0 ]
 OO0 += '?mode=' + str ( mode )
 OO0 += '&title=' + urllib . quote_plus ( name )
 OO0 += '&image=' + urllib . quote_plus ( image )
 OO0 += '&page=' + str ( page )
 if url != '' :
  OO0 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  OO0 += '&keyword=' + urllib . quote_plus ( keyword )
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  OO0oIII111i11IiI . addContextMenuItems ( contextMenu )
 if infoLabels :
  OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  OO0oIII111i11IiI . setProperty ( "IsPlayable" , "true" )
 OO0oIII111i11IiI . setProperty ( 'Fanart_Image' , O0o0Oo )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = isFolder )
 if 38 - 38: O0OOOoOoo0
 if 59 - 59: oOo0O0Ooo
def IiII1 ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , iconimage , i11IIIiI1I , O0OoooO0 , name in i1IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    I1i1iii1Ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
    for oOOOoo00 in I1i1iii1Ii :
     if oOOOoo00 == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    I1Ii1iIIiiiIi ( name , url , 1016 , iconimage , O0OoooO0 , i11IIIiI1I )
   else :
    if 'youtube' in url :
     I1i1iii1Ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for oOOOoo00 in I1i1iii1Ii :
      if oOOOoo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I11iIi1i1I1i1 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , O0OoooO0 , i11IIIiI1I )
    else :
     I1i1iii1Ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for oOOOoo00 in I1i1iii1Ii :
      if oOOOoo00 == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     I11iIi1i1I1i1 ( name , url , 222 , iconimage , O0OoooO0 , i11IIIiI1I )
     I1I11i ( 'tvshows' , 'Media Info 3' )
  else :
   iI1II1III ( url , iconimage , name )
   if 80 - 80: I11i . OOooOOo - I11i - iiiiiiii1 / ooOOOoO
 else :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
  for url , ooooo , name in i1IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     O00oO0 ( name , url , 1016 , ooooo )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      O0Oo00OoOo ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , ooooo )
     else :
      I1i1iii1Ii = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for oOOOoo00 in I1i1iii1Ii :
       if oOOOoo00 == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      O0Oo00OoOo ( name , url , 222 , ooooo )
      I1I11i ( 'tvshows' , 'Media Info 3' )
   else :
    iI1II1III ( url , ooooo , name )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 17 - 17: oO0o - iiiiiiii1 - IIiIiII11i / iiiiiiii1 / ii1ii11IIIiiI
def iI1II1III ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 I11III111i1I = ( url ) . replace ( oooO00ooO0oOo , 'http' ) . replace ( O0oi1i1ii1Ii111i , '.com' ) ;
 O0ooOO0O00 = ( I11III111i1I ) . replace ( iiIIiiI , 'a' ) . replace ( IIIiIII1 , 'b' ) . replace ( OOo0OOo , 'c' ) . replace ( o0ooOO000O , 'd' ) . replace ( o0o00O00Oo0 , 'e' ) . replace ( I1i1I1i1I1 , 'f' ) ;
 OOO0O = ( O0ooOO0O00 ) . replace ( ii1IooO00OO0ooo , 'g' ) . replace ( iIiiiI1i1iiiI , 'h' ) . replace ( iiiI1iiI11iii , 'i' ) . replace ( OO00OOo , 'j' ) . replace ( OOIiI1IIIiI1I1i , 'k' ) . replace ( oO00O0oO , 'l' ) ;
 iIi11 = ( OOO0O ) . replace ( OoO0OOOo0Oo , 'm' ) . replace ( Oooo0OOo0O0o , 'n' ) . replace ( O0O00OOOo00O , 'o' ) . replace ( I1iOO000o0o0oo , 'p' ) . replace ( oO00oOoo0ooO0 , 'q' ) . replace ( Ooo0o0ooO0 , 'r' ) ;
 oO0o0O = ( iIi11 ) . replace ( OoO0 , 's' ) . replace ( iI11iI , 't' ) . replace ( O00OO0OoO00oO , 'u' ) . replace ( iiiI1iiIiII1 , 'v' ) . replace ( oOo0oOOoo0O , 'w' ) . replace ( iI1IiI11Ii11i , 'x' ) ;
 O0oi1IiI1I = ( oO0o0O ) . replace ( O00OOoOo0 , 'y' ) . replace ( O0ooO0oOO , 'z' ) . replace ( I1ii1i , '.' ) . replace ( ooOoOOooOOO0 , '(' ) . replace ( ooOO0oo0o0o , ')' ) . replace ( I1i1IiIi1111 , '/' ) ;
 ii111I1iII1i1 = ( O0oi1IiI1I ) . replace ( o00o0OO0O , '1' ) . replace ( O0o0ooo00o00 , '2' ) . replace ( O000000oooOOo , '3' ) . replace ( IiiiiI11iii11iI , '4' ) . replace ( I111iIii1i1 , '5' ) . replace ( o0O0oOOoo0O0 , '6' ) ;
 I11iiI1 = ( ii111I1iII1i1 ) . replace ( i1IOO , '7' ) . replace ( Oo0OO0ooO0O0O , '8' ) . replace ( oO00O , '9' ) . replace ( ooooooO0o00 , '0' ) . replace ( IiIIiIii1ii , ':' ) . replace ( III1I1Iii1 , '%' ) ;
 url = ( I11iiI1 ) . replace ( i1Iii11iiI1 , '-' ) . replace ( III1i1iII1 , '_' ) ;
 O0Oo00OoOo ( name , url , 222 , iconimage ) ;
 if 45 - 45: ooOOOoO . o000O0o - I11i1ii1 . O0OOOoOoo0 / I1111IIi
 if 97 - 97: iI11I1II1I1I . IIiIiII11i
def iIi11OOo0oo ( ) :
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for oOooO0 , ooooo , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , oOooO0 , 1007 , ooooo )
def OoOoO00OoOOo ( url ) :
 if 64 - 64: ii1ii11IIIiiI
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , ooooo , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , ooooo )
  if 55 - 55: ooOOOoO - ooOOOoO + I11i1ii1
def OooOii1Ii ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iiI1IIIi = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iiI1IIIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiI1IIIi )
 if 42 - 42: O0OOOoOoo0
 if 6 - 6: oO0o + Ii1IIIi1
def OOO0O0OOo ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( OoO000O0Oo )
 for url , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  if '-dir-' in iiI11ii1I1 :
   O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , oOo0OOoO0 )
  else :
   O00oO0 ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' , url , 1006 , oOo0OOoO0 )
   if 22 - 22: I1ii11iIi11i . ii % iiiiiiii1
def i1i1IiIi1 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 oOoooO0 = ( 'http://afewbitsmore.com/' )
 i1IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if '[To Parent Directory]' in iiI11ii1I1 :
   iiI11ii1I1 = 'HOME'
   pass
  elif 'HOME' in iiI11ii1I1 :
   pass
  elif '.m3u' in iiI11ii1I1 :
   O00oO0 ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , oOoooO0 + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in iiI11ii1I1 :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , oOoooO0 + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in iiI11ii1I1 :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , oOoooO0 + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) , oOoooO0 + url , 1012 , III1iII1I1ii + 'music.png' )
def oOo0oOo ( url ) :
 oO0OOoo0OO = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOo0OOoO0 , iiI11ii1I1 , url in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'music.png' )
  if 11 - 11: Ii + I1111IIi - OOooOOo - ii
def I1111 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 oOoooO0 = url
 i1IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  if '.mp3' in iiI11ii1I1 :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '/' , '' ) , oOoooO0 + url , 1011 , III1iII1I1ii + 'music.png' )
def o00O ( ) :
 OoO000O0Oo = O0000OOO0 ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for oOooO0 , oOo0OOoO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , ( 'http://www.cyn.net/music/' + oOooO0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + oOo0OOoO0 ) . replace ( ' ' , '%20' ) )
def ii11 ( url , img ) :
 OoO000O0Oo = O0000OOO0 ( url )
 oO000oOo00o0o = url
 img = img
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( oO000oOo00o0o + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 76 - 76: iiiiiiii1 % ii
def IIII1ii1 ( url ) :
 OoO000O0Oo = O0000OOO0 ( url )
 oO000oOo00o0o = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( OoO000O0Oo )
 for type , url , iiI11ii1I1 in i1IIIII11I1IiI :
  if '[VID]' in type :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , oO000oOo00o0o + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   IIII1ii1 ( oO000oOo00o0o + url )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: oOo0O0Ooo . Ii1I / iI11I1II1I1I % ooOOOoO
 if 94 - 94: oOo0O0Ooo - ii1ii11IIIiiI % ii + ooOoO0O00 - ii
def Iii1 ( ) :
 iiiIi = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 I11iiIi1i1 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 i1IiiI1iIi = I11iiIi1i1 . lower ( )
 oOooO0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 oO000oOo00o0o = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 65 - 65: iiiiiiii1 . o0o00Oo0O + OOooOOo
 oO0OOoo0OO = O0o0O00Oo0o0 ( oOooO0 )
 I1iI = O0o0O00Oo0o0 ( oO00oOOo0Oo )
 O0 = O0o0O00Oo0o0 ( oO000oOo00o0o )
 if 82 - 82: I11i1ii1 . iiiiiiii1 . I1ii11iIi11i % iI11I1II1I1I - Ii
 if oO0OOoo0OO != 'Failed' :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oOooO0 , I1iIi1iIiiIiI , i11IIIiI1I , iI1IIIii , iiI11ii1I1 in i1IIIII11I1IiI :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oOooO0 , 1016 , I1iIi1iIiiIiI , O0OoooO0 , i11IIIiI1I )
    if 11 - 11: I11i1ii1 . iiiiiiii1 - O0OOOoOoo0 . I11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if I1iI != 'Failed' :
  ii1i = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( I1iI )
  for oOooO0 , iiI11ii1I1 in ii1i :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oOooO0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 41 - 41: o000O0o / oO0o - oO0o + I11i1ii1 * Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( O0 )
  for oOooO0 , iiI11ii1I1 in i1I :
   if I11iiIi1i1 in iiI11ii1I1 . lower ( ) :
    O00oO0 ( ( '[COLOR' + II + ']' + iiI11ii1I1 + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oOooO0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 13 - 13: iiiiiiii1 * IIiIiII11i - OOooOOo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 3 - 3: Ii1IIIi1 + I11i1ii1 * Ii . O0OOOoOoo0 / iI11I1II1I1I
    if 44 - 44: oO0o
    if 74 - 74: ii1ii11IIIiiI * ooOoO0O00 * ooOOOoO - ii . oOo0O0Ooo
    if 24 - 24: IIiIiII11i - Ii * ooOoO0O00 . I11i1ii1
    if 42 - 42: ooOOOoO / Ii
    if 7 - 7: ooOOOoO
OoO0OOOo0Oo = '{SF},' ; Oooo0OOo0O0o = '{IF},' ; O0O00OOOo00O = '{PW},' ; O000000oooOOo = '{AM},' ; I1iOO000o0o0oo = '{GF},' ; oO00oOoo0ooO0 = '{DD},' ; Ooo0o0ooO0 = '{UO},' ; OoO0 = '{LE},' ; O00OO0OoO00oO = '{ZY},' ; iiiI1iiIiII1 = '{UE},' ; oOo0oOOoo0O = '{PE},' ; iI1IiI11Ii11i = '{JE},' ; O00OOoOo0 = '{TH},' ; O0ooO0oOO = '{LK},'
if 50 - 50: Ii . Ii * ooOoO0O00 / Ii . ooOoO0O00 - IIiIiII11i
if 72 - 72: iI11I1II1I1I / I11i . Ii1I
def I1IiiI1ii1i ( ) :
 OoO000O0Oo = OoOooO ( 'http://www.iwatchseries.me/tv-list/' )
 i1IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , oOooO0 , 8021 , III1iII1I1ii + 'iwatch.png' )
  I1I11i ( 'movies' , 'MAIN' )
def Oo0 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 , II1i in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 + II1i , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def II1I1iI11II1 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  OOO0o0000 ( url )
def OOO0o0000 ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( OoO000O0Oo )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( OoO000O0Oo )
 I1II1 = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( OoO000O0Oo )
 oo00OO0000oO = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( 'VidSpot - ' + iiI11ii1I1 , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in i1I :
  O0Oo00OoOo ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url , iiI11ii1I1 in oo00OO0000oO :
  O0Oo00OoOo ( 'VidUp' + iiI11ii1I1 , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for iiI11ii1I1 , url in I1II1 :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   O0Oo00OoOo ( 'TheVideo - ' + iiI11ii1I1 , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 55 - 55: ooOoO0O00 / iiiiiiii1 . O0OOOoOoo0
def Oooo00oo0o ( ) :
 OoO000O0Oo = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 i1IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , oOooO0 , 1021 , III1iII1I1ii + 'anime.png' )
  if 67 - 67: IIiIiII11i + ii1ii11IIIiiI - oOo0O0Ooo * I11i1ii1
  if 19 - 19: Ii * I1ii11iIi11i
def iii1Ii ( ) :
 OoO000O0Oo = OoOooO ( 'http://www.animetoon.org/cartoon' )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( OoO000O0Oo )
 for oOooO0 , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , oOooO0 , 1002 , III1iII1I1ii + 'anime.png' )
  if 59 - 59: oO0o * o0o00Oo0O . iI11I1II1I1I . ooOOOoO * O0OOOoOoo0
  if 71 - 71: I11i . Ii1IIIi1 * Ii1I - ii1ii11IIIiiI
  if 97 - 97: I1111IIi
def Iiiiii1I ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( OoO000O0Oo )
 for oOo0OOoO0 in i1I :
  oOiiIIIII = oOo0OOoO0
 I1II1 = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( OoO000O0Oo )
 for url in I1II1 :
  O00oO0 ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( OoO000O0Oo )
 for url , iiI11ii1I1 in i1IIIII11I1IiI :
  O00oO0 ( iiI11ii1I1 , url , 1003 , oOiiIIIII )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ii1iiii11IiI1 ( url , IMAGE ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( OoO000O0Oo )
 for iiI11ii1I1 , url in i1IIIII11I1IiI :
  print iiI11ii1I1 + '     ' + url
  if 'easy' in url :
   O0OoO0ooOoo ( url )
  elif 'playpanda' in url :
   O0OoO0ooOoo ( url )
   if 43 - 43: o0o00Oo0O
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def O0OoO0ooOoo ( url ) :
 OoO000O0Oo = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( OoO000O0Oo )
 for url in i1IIIII11I1IiI :
  O0Oo00OoOo ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 57 - 57: Ii + ooOOOoO % I11i1ii1 / iI11I1II1I1I
  if 74 - 74: I1ii11iIi11i + Ii1IIIi1 . I11i / OOooOOo + ii1ii11IIIiiI + ooOoO0O00
def O0o00oooO00o ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 . add_header ( 'referer' , url )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 83 - 83: o000O0o
def O0000OOO0 ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 34 - 34: OOooOOo
def O0Oo ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 i111111 = ( '%s%s' % ( o0oO0OOoO0OoO0 , url ) )
 i1i = O0000OOO0 ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , ooooo , iiI11ii1I1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( '%s' % ( '[COLOR' + II + ']' + iiI11ii1I1 + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , ooooo )
  if 24 - 24: OOooOOo + ii + ii1ii11IIIiiI * ooOOOoO
def iI1I11II1Iii1 ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  O00O0oO ( url , iiI11ii1I1 )
 else :
  iii1 ( url )
def iii1 ( url ) :
 import urlresolver
 try :
  IIIIi1iII = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( IIIIi1iII , xbmcgui . ListItem ( iiI11ii1I1 ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( iiI11ii1I1 ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def O0OoooI11iI1I ( url ) :
 if 49 - 49: ooOoO0O00 . I1111IIi
 iI = open ( o00OO00OoO , "a" )
 iI . write ( 'url="' + url + '"\n' )
 iI . close
 if 82 - 82: oO0o / ooOOOoO
 oOoOoo0 = xbmc . Player ( ii1II ( ) )
 import urlresolver
 try : oOoOoo0 . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( iiI11ii1I1 ) )
 oOoOoo0 = xbmc . Player ( ii1II ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  OOooO0OOoo = xbmcgui . Dialog ( )
  if OOooO0OOoo . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   OOooO0OOoo . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : oOoOoo0 . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def O00O0oO ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  III = '.mp4'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iii1 ( url )
  if iI11iI1IiiIiI == 1 :
   ii1iIIIi1Iii1 ( url , name , III )
 elif '.mkv' in url :
  III = '.mkv'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iii1 ( url )
  if iI11iI1IiiIiI == 1 :
   ii1iIIIi1Iii1 ( url , name , III )
 elif '.mp3' in url :
  III = '.mp3'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iii1 ( url )
  if iI11iI1IiiIiI == 1 :
   ii1iIIIi1Iii1 ( url , name , III )
 elif '.avi' in url :
  III = '.avi'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iii1 ( url )
  if iI11iI1IiiIiI == 1 :
   ii1iIIIi1Iii1 ( url , name , III )
 elif '.mov' in url :
  III = '.mov'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iii1 ( url )
  if iI11iI1IiiIiI == 1 :
   ii1iIIIi1Iii1 ( url , name , III )
 elif '.mpeg' in url :
  III = '.mpeg'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iii1 ( url )
  if iI11iI1IiiIiI == 1 :
   ii1iIIIi1Iii1 ( url , name , III )
 elif '.mpg' in url :
  III = '.mpg'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iii1 ( url )
  if iI11iI1IiiIiI == 1 :
   ii1iIIIi1Iii1 ( url , name , III )
 elif '.flv' in url :
  III = '.flv'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iii1 ( url )
  if iI11iI1IiiIiI == 1 :
   ii1iIIIi1Iii1 ( url , name , III )
 elif '.wmv' in url :
  III = '.wmv'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   iii1 ( url )
  if iI11iI1IiiIiI == 1 :
   ii1iIIIi1Iii1 ( url , name , III )
 else :
  iii1 ( url )
def ii1iIIIi1Iii1 ( url , name , cat ) :
 oOoOOOo0oo ( )
 O0O00Oo = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 name = ( name ) . replace ( 'blue' , '' ) . replace ( 'green' , '' ) . replace ( 'COLOR' , '' ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( ' ' , '_' ) . replace ( '/' , '' )
 file = name + cat
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Item Is Downloading" , "Why not check out our website" , '@' , 'Http://GenieTv.co.uk' )
 oooooo0O000o = os . path . join ( O0O00Oo , file )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]All Done, Your download With Be Avaiilable In Your Set Location[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
def oOoOOOo0oo ( ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def O000Oo0O ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % iiI11ii1I1 )
 xbmc . sleep ( 1 )
 oOoOoo0 = xbmc . Player ( ii1II ( ) )
 o0oOoO00o . update ( 100 , '%s' % iiI11ii1I1 )
 xbmc . sleep ( 1 )
 oOoOoo0 . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 100 - 100: Ii * O0OOOoOoo0 * I11i1ii1
def iii11II1I ( url ) :
 oOoOoo0 = xbmc . Player ( ii1II ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : oOoOoo0 . play ( url ) . strip ( )
 except : pass
 if 19 - 19: I1111IIi
def I1i1iiIi1Ii11I1 ( url ) :
 oOoOoo0 = xbmc . Player ( ii1II ( ) )
 import urlresolver
 iiI1I1iii1 = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 oOoOoo0 . play ( iiI1I1iii1 )
 xbmc . sleep ( 1 )
 oOoOoo0 . play ( url )
 if 21 - 21: iI11I1II1I1I + Ii1IIIi1 . Ii1I % Ii1IIIi1 + ii1ii11IIIiiI + iI11I1II1I1I
 if 64 - 64: ii1ii11IIIiiI * Ii1IIIi1 * o000O0o
def ii1II ( ) :
 try :
  ooO0O0oO = getSet ( "core-player" )
  if ( ooO0O0oO == 'DVDPLAYER' ) : iIiIoO00OooO00O0o = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( ooO0O0oO == 'MPLAYER' ) : iIiIoO00OooO00O0o = xbmc . PLAYER_CORE_MPLAYER
  elif ( ooO0O0oO == 'PAPLAYER' ) : iIiIoO00OooO00O0o = xbmc . PLAYER_CORE_PAPLAYER
  else : iIiIoO00OooO00O0o = xbmc . PLAYER_CORE_AUTO
 except : iIiIoO00OooO00O0o = xbmc . PLAYER_CORE_AUTO
 return iIiIoO00OooO00O0o
 return True
 if 3 - 3: o000O0o . ii * Ii1IIIi1 * Ii1I * I11i1ii1
def O00oO0 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOO0oOOo00O = True
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0000 = [ ]
  O0000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   O0000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OO0oIII111i11IiI . addContextMenuItems ( O0000 )
 OOO0oOOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = True )
 return OOO0oOOo00O
 if 26 - 26: ii . ooOoO0O00 + oO0o
def IIiii11ii1i ( name , url , mode , iconimage , fanart , description ) :
 if 42 - 42: Ii * I11i % ooOOOoO % I1ii11iIi11i + I11i * Ii
 OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0oOOo00O = True
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OO0oIII111i11IiI . setProperty ( "Fanart_Image" , fanart )
 OOO0oOOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = True )
 return OOO0oOOo00O
 if 66 - 66: ii1ii11IIIiiI / I1111IIi . ii * I1ii11iIi11i % Ii
def O0Oo00OoOo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOO0oOOo00O = True
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  O0000 = [ ]
  O0000 . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   O0000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   O0000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  OO0oIII111i11IiI . addContextMenuItems ( O0000 )
 OOO0oOOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = False )
 return OOO0oOOo00O
 if 100 - 100: Ii1I % IIiIiII11i * Ii - O0OOOoOoo0
 if 69 - 69: Ii1IIIi1 + O0OOOoOoo0 / iiiiiiii1
 if 37 - 37: iI11I1II1I1I * ooOOOoO / I1111IIi * I1ii11iIi11i % Ii
 if 93 - 93: I11i1ii1 + I11i1ii1
 if 65 - 65: ii * ooOOOoO * o000O0o % Ii1I * IIiIiII11i
 if 86 - 86: Ii / ooOOOoO * O0OOOoOoo0 - O0OOOoOoo0
def iIiiIIi1i111iI ( url , heading , announce ) :
 class i1iIi1I1II1 ( ) :
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
   try : OOoO = open ( announce ) ; IiIii11i1IIiI = OOoO . read ( )
   except : IiIii11i1IIiI = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiIii11i1IIiI ) )
   return
 i1iIi1I1II1 ( )
 i1iIi1I1II1 ( )
def iiIiI1i1 ( heading , announce ) :
 class i1iIi1I1II1 ( ) :
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
   try : OOoO = open ( announce ) ; IiIii11i1IIiI = OOoO . read ( )
   except : IiIii11i1IIiI = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiIii11i1IIiI ) )
   return
 i1iIi1I1II1 ( )
 i1iIi1I1II1 ( )
def Ii1I1Ii ( ) :
 iIiiIIi1i111iI ( III1iII1I1ii + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 33 - 33: ooOOOoO + iiiiiiii1
 if 12 - 12: oO0o . O0OOOoOoo0 + Ii1I . ii1ii11IIIiiI
 if 50 - 50: I1ii11iIi11i
 if 16 - 16: ii1ii11IIIiiI - OOooOOo % I1ii11iIi11i / ii1ii11IIIiiI . ooOOOoO + I11i1ii1
 if 78 - 78: iI11I1II1I1I + oO0o + Ii
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 21 - 21: I1ii11iIi11i + ii1ii11IIIiiI % I11i1ii1 + OOooOOo % ooOOOoO
 if 22 - 22: ooOoO0O00 / ii . oO0o
 if 83 - 83: oOo0O0Ooo - ii + Ii1I . ii1ii11IIIiiI / I11i + I11i1ii1
 if 90 - 90: oOo0O0Ooo - Ii
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
 if 78 - 78: I1111IIi
 if 38 - 38: oO0o * Ii1I
 if 4 - 4: oO0o . Ii1I
 if 21 - 21: Ii / oO0o / Ii1I * o0o00Oo0O - IIiIiII11i * Ii1IIIi1
 if 27 - 27: I11i . OOooOOo * ii1ii11IIIiiI * O0OOOoOoo0 * o0o00Oo0O
 if 93 - 93: I1111IIi % iiiiiiii1 % IIiIiII11i
 if 20 - 20: ii * iiiiiiii1
 if 38 - 38: O0OOOoOoo0 . ii
 if 28 - 28: iiiiiiii1 * ooOoO0O00 . Ii1I
 if 75 - 75: o0o00Oo0O / o000O0o * I11i1ii1 - Ii1IIIi1 / ooOoO0O00
def o0OOo0oOOo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + OoOOOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 87 - 87: I11i1ii1 / IIiIiII11i - Ii1I % Ii
def Ooo0000o ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + ii11Ii1111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 89 - 89: IIiIiII11i . Ii1I
def iIiiiiIi111I ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + ooOo00oOOOO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 21 - 21: ii % ii
def oOo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + oOOo000o0o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 79 - 79: iiiiiiii1 + o000O0o - iI11I1II1I1I * OOooOOo / ii
def ii1II1 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + OO0ooOooOoO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 86 - 86: Ii1IIIi1 / I11i
def o00o0oOo0O ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + Ii1i1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
def iII1IiI1I11i ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + Ii1i11I11i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 55 - 55: o000O0o + ii % ooOoO0O00
def iIIIIiI1I ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + oOO00O0O0oO0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 14 - 14: I11i . iI11I1II1I1I + ii - ooOoO0O00 / ii1ii11IIIiiI
def OOiI1I ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + II11IIi11Ii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 42 , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 25 - 25: Ii1I / Ii1I
def O0O0OOOOoo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + OO0OoOo0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for iiI11ii1I1 , url , I1iIi1iIiiIiI , O0OoooO0 , oOOo000oOoO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( iiI11ii1I1 , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , oOOo000oOoO0 )
 I1I11i ( 'movies' , 'MAIN' )
 if 84 - 84: ii + O0OOOoOoo0 . Ii - o0o00Oo0O / o0o00Oo0O % ooOoO0O00
 if 38 - 38: iI11I1II1I1I - IIiIiII11i
 if 47 - 47: Ii1I
 if 39 - 39: Ii
 if 97 - 97: OOooOOo . I1ii11iIi11i . iiiiiiii1 + O0OOOoOoo0 % I11i1ii1 . I1111IIi
 if 40 - 40: iiiiiiii1 - Ii
 if 58 - 58: IIiIiII11i / o0o00Oo0O
 if 83 - 83: Ii1IIIi1 * I1111IIi / oO0o / Ii
 if 94 - 94: o0o00Oo0O / iI11I1II1I1I + o0o00Oo0O / oOo0O0Ooo
def OO000 ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for OO0iiiii1iiIIii , o00oo , O0oO0oo0O in os . walk ( iIi1ii1I1 ) :
     oooO0OOO0o0o = 0
     oooO0OOO0o0o += len ( O0oO0oo0O )
     if oooO0OOO0o0o > 0 :
      for OOoO in O0oO0oo0O :
       os . unlink ( os . path . join ( OO0iiiii1iiIIii , OOoO ) )
  iiiIiiIII = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( iiiIiiIII )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 100 - 100: o000O0o + IIiIiII11i / I1111IIi / ooOoO0O00 / ii1ii11IIIiiI / o0o00Oo0O
 if 50 - 50: ii1ii11IIIiiI + ii1ii11IIIiiI
 if 51 - 51: Ii1I / ii * I1111IIi
 if 78 - 78: O0OOOoOoo0 / Ii1I . Ii
 if 69 - 69: ooOOOoO - IIiIiII11i
 if 66 - 66: oOo0O0Ooo . oOo0O0Ooo - OOooOOo * ii * IIiIiII11i + oOo0O0Ooo
 if 59 - 59: ii1ii11IIIiiI
 if 59 - 59: IIiIiII11i - oO0o
def oOoOO ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 31 - 31: ooOOOoO - OOooOOo / I11i * OOooOOo / I1ii11iIi11i + I11i
def O0OO ( url ) :
 I1iII1IiI11i = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 OOOoO = [
 ( I1iII1IiI11i ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( I1iII1IiI11i , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( I1iII1IiI11i , 'plugin.video.itv' , 'Images' ) ) ]
 if 93 - 93: Ii * I11i
 I1IiiI1i1 = 0
 if 23 - 23: oO0o / I11i
 for oOOOoo00 in OOOoO :
  if os . path . exists ( oOOOoo00 ) and not oOOOoo00 in [ oO0o0o0ooO0oO , I1iII1IiI11i ] :
   for OO0iiiii1iiIIii , o00oo , O0oO0oo0O in os . walk ( oOOOoo00 ) :
    oooO0OOO0o0o = 0
    oooO0OOO0o0o += len ( O0oO0oo0O )
    if oooO0OOO0o0o > 0 :
     for OOoO in O0oO0oo0O :
      if not OOoO in oooOOOOO :
       try :
        os . unlink ( os . path . join ( OO0iiiii1iiIIii , OOoO ) )
       except :
        pass
      else : OOO ( 'Ignore Log File: %s' % OOoO )
     for o0IiIiI111IIII1 in o00oo :
      try :
       shutil . rmtree ( os . path . join ( OO0iiiii1iiIIii , o0IiIiI111IIII1 ) )
       I1IiiI1i1 += 1
       OOO ( "[Success] cleared %s files from %s" % ( str ( oooO0OOO0o0o ) , os . path . join ( oOOOoo00 , o0IiIiI111IIII1 ) ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( oOOOoo00 , o0IiIiI111IIII1 ) )
  else :
   for OO0iiiii1iiIIii , o00oo , O0oO0oo0O in os . walk ( oOOOoo00 ) :
    for o0IiIiI111IIII1 in o00oo :
     if 'cache' in o0IiIiI111IIII1 . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( OO0iiiii1iiIIii , o0IiIiI111IIII1 ) )
       I1IiiI1i1 += 1
       OOO ( "[Success] wiped %s " % os . path . join ( oOOOoo00 , o0IiIiI111IIII1 ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( oOOOoo00 , o0IiIiI111IIII1 ) )
       if 22 - 22: Ii1IIIi1 - oO0o . ooOOOoO
 oOoOO ( oO , 'Clear Cache: Removed %s Files' % I1IiiI1i1 )
 if 89 - 89: iiiiiiii1
 if 19 - 19: I1111IIi + iiiiiiii1
 if 65 - 65: ii1ii11IIIiiI - o000O0o + ooOoO0O00 + Ii1IIIi1 % O0OOOoOoo0
 if 5 - 5: oO0o / O0OOOoOoo0 / Ii1IIIi1
 if 70 - 70: OOooOOo - ooOOOoO + I11i1ii1 / Ii / oOo0O0Ooo % iI11I1II1I1I
 if 83 - 83: o000O0o . ii1ii11IIIiiI - I11i % ooOOOoO + Ii
 if 40 - 40: o0o00Oo0O . ii1ii11IIIiiI
def OO0OooOo ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 Ooo0O0OO0OOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OO0iiiii1iiIIii , o00oo , O0oO0oo0O in os . walk ( Ooo0O0OO0OOo ) :
   oooO0OOO0o0o = 0
   oooO0OOO0o0o += len ( O0oO0oo0O )
   if 12 - 12: ooOOOoO
   if 97 - 97: ooOoO0O00 % ooOOOoO . I11i * oOo0O0Ooo % IIiIiII11i
   if oooO0OOO0o0o > 0 :
    if 41 - 41: ooOOOoO . Ii1I
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( oooO0OOO0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 69 - 69: o0o00Oo0O * I11i1ii1 % I11i1ii1 / o000O0o
     for OOoO in O0oO0oo0O :
      os . unlink ( os . path . join ( OO0iiiii1iiIIii , OOoO ) )
     for o0IiIiI111IIII1 in o00oo :
      shutil . rmtree ( os . path . join ( OO0iiiii1iiIIii , o0IiIiI111IIII1 ) )
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
 if 2 - 2: o000O0o % oO0o
 if 3 - 3: o000O0o / oO0o % Ii
 if 26 - 26: I11i1ii1 . iiiiiiii1 / IIiIiII11i % ii1ii11IIIiiI
 if 82 - 82: Ii1IIIi1 % o0o00Oo0O % iI11I1II1I1I % I1111IIi + Ii
 if 64 - 64: ooOoO0O00 / I1111IIi . I1111IIi - iiiiiiii1 % Ii1IIIi1 . IIiIiII11i
 if 78 - 78: iiiiiiii1 - o0o00Oo0O - iiiiiiii1 . iI11I1II1I1I % Ii1I . ii
 if 64 - 64: I1111IIi
 if 21 - 21: I11i - I11i1ii1 * ii . ii
 if 17 - 17: Ii1IIIi1 - O0OOOoOoo0 % oOo0O0Ooo * Ii1IIIi1 * iI11I1II1I1I . I11i
def ooO0O0O0ooOOO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 Ooo0O0OO0OOo = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for OO0iiiii1iiIIii , o00oo , O0oO0oo0O in os . walk ( Ooo0O0OO0OOo ) :
   oooO0OOO0o0o = 0
   oooO0OOO0o0o += len ( O0oO0oo0O )
   if 58 - 58: o000O0o - IIiIiII11i + o0o00Oo0O
   if 54 - 54: iI11I1II1I1I - I1111IIi - I1111IIi
   if oooO0OOO0o0o > 0 :
    if 18 - 18: Ii + iI11I1II1I1I . Ii
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( oooO0OOO0o0o ) + " files found" , "Do you want to delete them?" ) :
     if 63 - 63: O0OOOoOoo0 - oO0o * Ii1IIIi1
     for OOoO in O0oO0oo0O :
      os . unlink ( os . path . join ( OO0iiiii1iiIIii , OOoO ) )
     for o0IiIiI111IIII1 in o00oo :
      shutil . rmtree ( os . path . join ( OO0iiiii1iiIIii , o0IiIiI111IIII1 ) )
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
 O0OO ( url )
 return
 if 89 - 89: O0OOOoOoo0 / I1ii11iIi11i
 if 66 - 66: I11i + OOooOOo % ii . ooOOOoO
 if 30 - 30: IIiIiII11i - I1ii11iIi11i - Ii + o0o00Oo0O
 if 93 - 93: ooOoO0O00 + iiiiiiii1 / oO0o - ooOOOoO % I1ii11iIi11i / ii1ii11IIIiiI
 if 1 - 1: I1ii11iIi11i / ii1ii11IIIiiI . Ii % Ii1IIIi1 + I11i + o0o00Oo0O
 if 54 - 54: iiiiiiii1 + I11i1ii1 % I1111IIi
 if 83 - 83: I11i * iI11I1II1I1I
 if 36 - 36: OOooOOo + IIiIiII11i - oO0o % I11i1ii1 * ooOoO0O00
 if 4 - 4: ii1ii11IIIiiI + oO0o * Ii1I
 if 13 - 13: OOooOOo - I1111IIi * iI11I1II1I1I * o0o00Oo0O
def IiIIiI ( url , name ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iIi1I111Ii1I1 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 o00OO0Oo0Oo = os . path . join ( O0O00Oo , 'advancedsettings.xml.bak' )
 if os . path . exists ( o00OO0Oo0Oo ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   iIi1I111Ii1I1 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
   try :
    os . remove ( iIi1I111Ii1I1 )
    print '=== GenieTv - REMOVING    ' + str ( iIi1I111Ii1I1 ) + '    ==='
   except :
    pass
   i1i = iI111I11I1I1 . http_GET ( url ) . content
   Iii1iiI = open ( iIi1I111Ii1I1 , "w" )
   Iii1iiI . write ( i1i )
   Iii1iiI . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( iIi1I111Ii1I1 ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  iIi1I111Ii1I1 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
  try :
   os . remove ( iIi1I111Ii1I1 )
   print '=== GenieTv - REMOVING    ' + str ( iIi1I111Ii1I1 ) + '    ==='
  except :
   pass
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  Iii1iiI = open ( iIi1I111Ii1I1 , "w" )
  Iii1iiI . write ( i1i )
  Iii1iiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iIi1I111Ii1I1 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 25 - 25: iiiiiiii1 . I1111IIi % o0o00Oo0O % ooOoO0O00
def oo0Oo0oo000 ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iIi1I111Ii1I1 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
 try :
  Iii1iiI = open ( iIi1I111Ii1I1 ) . read ( )
  if 'zero' in Iii1iiI :
   name = '0CACHE'
  elif 'tuxen' in Iii1iiI :
   name = 'TUXENS'
  elif 'muckys' in Iii1iiI :
   name = 'MUCKYS'
  elif 'p2p1' in Iii1iiI :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in Iii1iiI :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in Iii1iiI :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 15 - 15: o0o00Oo0O % ooOOOoO % I1111IIi - I1111IIi
def Ooo0 ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 iIi1I111Ii1I1 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
 try :
  os . remove ( iIi1I111Ii1I1 )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( iIi1I111Ii1I1 ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 50 - 50: o000O0o
 if 55 - 55: Ii1I
 if 55 - 55: I1ii11iIi11i % ii1ii11IIIiiI . iI11I1II1I1I * iiiiiiii1
 if 33 - 33: o0o00Oo0O - oOo0O0Ooo / Ii1I / oO0o + O0OOOoOoo0 - o000O0o
 if 27 - 27: iiiiiiii1 + I11i1ii1 - iiiiiiii1 % Ii * I1ii11iIi11i * I11i
 if 88 - 88: Ii1IIIi1
 if 25 - 25: oO0o + I11i . I11i1ii1 - ii1ii11IIIiiI . o000O0o * ii1ii11IIIiiI
 if 85 - 85: ooOoO0O00
 if 94 - 94: ii . o0o00Oo0O / ii
 if 67 - 67: Ii + OOooOOo
def ii111iI1i1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 i1IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for I1iII , oO0Ooo , iiiiIIiiII1Iii1 , OOo0O0O000 in i1IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % I1iII , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % iiiiIIiiII1Iii1 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % OOo0O0O000 )
  inc = inc + 1
  if 98 - 98: Ii1IIIi1
  if 97 - 97: I11i
  if 35 - 35: I11i1ii1 + Ii
  if 82 - 82: Ii + ooOOOoO + O0OOOoOoo0 % oOo0O0Ooo
  if 84 - 84: o000O0o % Ii1IIIi1
  if 25 - 25: Ii * OOooOOo + Ii . ooOoO0O00
  if 83 - 83: oOo0O0Ooo
  if 90 - 90: IIiIiII11i
  if 2 - 2: ii1ii11IIIiiI - ii - Ii % I1ii11iIi11i / ii1ii11IIIiiI
def OOO0O0oO ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iIi1I111Ii1I1 = os . path . join ( O0O00Oo , 'addons2.ini' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  Iii1iiI = open ( iIi1I111Ii1I1 , "w" )
  Iii1iiI . write ( i1i )
  Iii1iiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iIi1I111Ii1I1 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 55 - 55: oOo0O0Ooo
def oO00ooo0ooo0o ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  iIi1I111Ii1I1 = os . path . join ( O0O00Oo , 'settings.xml' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  Iii1iiI = open ( iIi1I111Ii1I1 , "w" )
  Iii1iiI . write ( i1i )
  Iii1iiI . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( iIi1I111Ii1I1 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 86 - 86: o0o00Oo0O - oO0o % ooOOOoO . o000O0o
 if 49 - 49: Ii - iI11I1II1I1I % o0o00Oo0O % O0OOOoOoo0 * I11i1ii1 - I1111IIi
def iiIiIiIiiIii ( ) :
 try :
  oO00o = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( oO00o ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    IiIi1i1 = os . path . join ( oO00o , "source.db" )
    os . unlink ( IiIi1i1 )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 96 - 96: I11i
 if 90 - 90: I1111IIi * ii1ii11IIIiiI . ooOOOoO / Ii1I % ooOOOoO
 if 58 - 58: O0OOOoOoo0 % iI11I1II1I1I * oO0o
 if 25 - 25: iiiiiiii1 - I11i1ii1 + I1ii11iIi11i . oOo0O0Ooo % iI11I1II1I1I
 if 49 - 49: ooOoO0O00 + oO0o + O0OOOoOoo0 / I1ii11iIi11i
def OoOooO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 5 - 5: Ii + ooOOOoO . I1111IIi
 if 9 - 9: Ii / iI11I1II1I1I - Ii1I * Ii1I
 if 99 - 99: ooOOOoO
 if 64 - 64: iI11I1II1I1I
 if 61 - 61: ii1ii11IIIiiI % I1ii11iIi11i + OOooOOo
 if 60 - 60: o000O0o . ii
 if 40 - 40: ooOOOoO
def IiIIi1 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; iI1Iii11Iii11 = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if iI1Iii11Iii11 :
  iIiiI = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; iIiiI = xbmc . translatePath ( iIiiI ) ;
  OOo000 = os . path . join ( iIiiI , ".." , ".." ) ; OOo000 = os . path . abspath ( OOo000 ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + OOo000 ) ; iI1iIIiIi1I1 = False
  try :
   for OO0iiiii1iiIIii , o00oo , O0oO0oo0O in os . walk ( OOo000 , topdown = True ) :
    o00oo [ : ] = [ o0IiIiI111IIII1 for o0IiIiI111IIII1 in o00oo if o0IiIiI111IIII1 not in o0oO0 ]
    for iiI11ii1I1 in O0oO0oo0O :
     try : os . remove ( os . path . join ( OO0iiiii1iiIIii , iiI11ii1I1 ) )
     except :
      if iiI11ii1I1 not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : iI1iIIiIi1I1 = True
      plugintools . log ( "Error removing " + OO0iiiii1iiIIii + " " + iiI11ii1I1 )
    for iiI11ii1I1 in o00oo :
     try : os . rmdir ( os . path . join ( OO0iiiii1iiIIii , iiI11ii1I1 ) )
     except :
      if iiI11ii1I1 not in [ "Database" , "userdata" ] : iI1iIIiIi1I1 = True
      plugintools . log ( "Error removing " + OO0iiiii1iiIIii + " " + iiI11ii1I1 )
   if not iI1iIIiIi1I1 : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 iIi1i1i1II11I ( )
 if 85 - 85: oO0o + IIiIiII11i
 if 87 - 87: oO0o
 if 93 - 93: ii
def ooOooO0O ( ) :
 iIIiii = [ ]
 ii111Ii = sys . argv [ 2 ]
 if len ( ii111Ii ) >= 2 :
  IIIIiii1IIii = sys . argv [ 2 ]
  OOo0o0oOOOO00 = IIIIiii1IIii . replace ( '?' , '' )
  if ( IIIIiii1IIii [ len ( IIIIiii1IIii ) - 1 ] == '/' ) :
   IIIIiii1IIii = IIIIiii1IIii [ 0 : len ( IIIIiii1IIii ) - 2 ]
  oo0O = OOo0o0oOOOO00 . split ( '&' )
  iIIiii = { }
  for i11ii in range ( len ( oo0O ) ) :
   ii1IIi1ii = { }
   ii1IIi1ii = oo0O [ i11ii ] . split ( '=' )
   if ( len ( ii1IIi1ii ) ) == 2 :
    iIIiii [ ii1IIi1ii [ 0 ] ] = ii1IIi1ii [ 1 ]
    if 25 - 25: OOooOOo + I11i % Ii / Ii1I - ii
 return iIIiii
 if 61 - 61: ii / Ii1IIIi1 % o000O0o
II1i1i1111IIIii = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
iI11IiIiiII1 = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
OOoOO0O0o0 = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
ii11IiiiIi1iI = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
O000o0 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
IiiiIII1 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
OoOOOoo = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
Iii11 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
ii11Ii1111 = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
ooOo00oOOOO0 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
oOOo000o0o = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
OO0ooOooOoO0 = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
Ii1i1 = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
Ii1i11I11i = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
oOO00O0O0oO0 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
II11IIi11Ii11 = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
ooO0O0 = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iII1Ii1ii111 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
I11OOO0 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
I1IIii11 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
i1iI = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
ii11i1I1i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
OO0OoOo0O = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
o0oO0OOoO0OoO0 = base64 . decodestring ( 'Q1VOVA==' )
def iiOOooooO0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0oOOo00O = True
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OO0oIII111i11IiI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0000 = [ ]
  if showcontext == 'fav' :
   O0000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   O0000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OO0oIII111i11IiI . addContextMenuItems ( O0000 )
 OOO0oOOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = True )
 return OOO0oOOo00O
 if 22 - 22: ii1ii11IIIiiI
def OOiIiIIi1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 OO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 OOO0oOOo00O = True
 OO0oIII111i11IiI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OO0oIII111i11IiI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 OO0oIII111i11IiI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0000 = [ ]
  if showcontext == 'fav' :
   O0000 . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   O0000 . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  OO0oIII111i11IiI . addContextMenuItems ( O0000 )
 OOO0oOOo00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OO0 , listitem = OO0oIII111i11IiI , isFolder = False )
 return OOO0oOOo00O
 if 44 - 44: iiiiiiii1 % OOooOOo + iiiiiiii1 / oO0o
 if 73 - 73: I1ii11iIi11i . ooOOOoO * O0OOOoOoo0 . Ii1I . o0o00Oo0O
IIIIiii1IIii = ooOooO0O ( )
oOooO0 = None
iiI11ii1I1 = None
I1I = None
I1iIi1iIiiIiI = None
O0OoooO0 = None
oOOo000oOoO0 = None
iiIiIi1I1 = None
ii11I1IIII11 = None
if 43 - 43: O0OOOoOoo0
if 25 - 25: Ii1IIIi1 % O0OOOoOoo0 + O0OOOoOoo0
try :
 ii11I1IIII11 = int ( IIIIiii1IIii [ "fav_mode" ] )
except :
 pass
 if 41 - 41: oO0o / Ii1I . Ii1I / ooOoO0O00 - ooOoO0O00 - Ii1I
try :
 oOooO0 = urllib . unquote_plus ( IIIIiii1IIii [ "url" ] )
except :
 pass
try :
 iiI11ii1I1 = urllib . unquote_plus ( IIIIiii1IIii [ "name" ] )
except :
 pass
try :
 I1iIi1iIiiIiI = urllib . unquote_plus ( IIIIiii1IIii [ "iconimage" ] )
except :
 pass
try :
 I1I = int ( IIIIiii1IIii [ "mode" ] )
except :
 pass
try :
 O0OoooO0 = urllib . unquote_plus ( IIIIiii1IIii [ "fanart" ] )
except :
 pass
try :
 oOOo000oOoO0 = urllib . unquote_plus ( IIIIiii1IIii [ "description" ] )
except :
 pass
 if 78 - 78: O0OOOoOoo0 % O0OOOoOoo0 % o0o00Oo0O - ooOOOoO - oO0o
 if 59 - 59: oOo0O0Ooo / Ii1I * ooOoO0O00 % O0OOOoOoo0
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( I1I )
print "URL: " + str ( oOooO0 )
print "Name: " + str ( iiI11ii1I1 )
print "IconImage: " + str ( I1iIi1iIiiIiI )
if 78 - 78: iI11I1II1I1I / Ii1I / I1111IIi
if 11 - 11: ooOOOoO
def I1I11i ( content , viewType ) :
 if 59 - 59: Ii1IIIi1 - iiiiiiii1 - IIiIiII11i / ooOoO0O00 * Ii1IIIi1 . ii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 46 - 46: I1111IIi * ii . I11i - iiiiiiii1 * oOo0O0Ooo
if I1iIi1iIiiIiI == None : I1iIi1iIiiIiI = Oo00OOOOO
if O0OoooO0 == None : O0OoooO0 = O0o0Oo
if I1I == None :
 o0o0o0oO0oOO ( )
 if 83 - 83: I1ii11iIi11i . I11i + O0OOOoOoo0 + I11i % iI11I1II1I1I * OOooOOo
elif I1I == 1 :
 IIii1i ( oOooO0 )
 if 65 - 65: Ii1IIIi1 . IIiIiII11i * Ii + Ii1IIIi1
elif I1I == 44 :
 II1i11I ( oOooO0 )
 if 99 - 99: Ii1I % I1ii11iIi11i
elif I1I == 2 :
 i11ii111i1ii ( )
 if 31 - 31: I11i - IIiIiII11i * Ii1IIIi1 . Ii1IIIi1 - o000O0o
elif I1I == 3 :
 iiIIIi1i ( )
 if 57 - 57: Ii1IIIi1 / Ii / iiiiiiii1 - I1ii11iIi11i . iI11I1II1I1I
elif I1I == 21 :
 i1i1II ( )
 if 84 - 84: I1111IIi
elif I1I == 4 :
 iiIi1iIiI ( )
 if 42 - 42: o0o00Oo0O . iiiiiiii1 / ooOOOoO
elif I1I == 5 :
 IIIIIiiI11i1 ( oOooO0 )
 if 69 - 69: OOooOOo / iiiiiiii1 * oOo0O0Ooo
elif I1I == 6 :
 OO0OooOo ( oOooO0 )
 if 76 - 76: o0o00Oo0O + IIiIiII11i * oO0o
elif I1I == 7 :
 IiIIiI ( oOooO0 , iiI11ii1I1 )
 if 1 - 1: I11i
elif I1I == 8 :
 oo0Oo0oo000 ( oOooO0 , iiI11ii1I1 )
 if 34 - 34: I11i + Ii1IIIi1 . oO0o + oOo0O0Ooo + ii
elif I1I == 9 :
 FIXREPOSADDONS ( oOooO0 )
 if 90 - 90: ii1ii11IIIiiI / OOooOOo - iI11I1II1I1I / ooOoO0O00 * iiiiiiii1 - I11i1ii1
elif I1I == 10 :
 oOOo0O00o ( )
 if 2 - 2: O0OOOoOoo0 * ooOOOoO * I11i1ii1 + Ii + o000O0o
elif I1I == 11 :
 Ooo0 ( oOooO0 )
 if 81 - 81: I11i * oO0o
elif I1I == 12 :
 ii111iI1i1 ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 18 - 18: Ii / I11i - o000O0o . ooOOOoO * ooOoO0O00
elif I1I == 13 :
 OO000 ( )
 if 67 - 67: ii1ii11IIIiiI
elif I1I == 14 :
 O0OO ( oOooO0 )
 if 64 - 64: OOooOOo + O0OOOoOoo0 * OOooOOo - oOo0O0Ooo * ii
elif I1I == 15 :
 iI1iiiI ( )
 if 27 - 27: IIiIiII11i + Ii
elif I1I == 16 :
 OOO0O0oO ( oOooO0 , iiI11ii1I1 )
 if 32 - 32: ooOoO0O00
elif I1I == 17 :
 oO00ooo0ooo0o ( oOooO0 , iiI11ii1I1 )
 if 76 - 76: IIiIiII11i % I11i1ii1 - Ii1I
elif I1I == 18 :
 iiIiIiIiiIii ( )
 if 50 - 50: IIiIiII11i / oOo0O0Ooo . ii1ii11IIIiiI % Ii
elif I1I == 19 :
 oO0I1I1i1I1I1I1 ( oOooO0 )
 if 66 - 66: o000O0o / Ii1IIIi1 / O0OOOoOoo0
elif I1I == 40 :
 OO0o0o0oo ( iiI11ii1I1 , oOooO0 , oOOo000oOoO0 )
 if 5 - 5: iiiiiiii1 . o000O0o
elif I1I == 42 :
 i111IIiIII1i ( iiI11ii1I1 , oOooO0 , oOOo000oOoO0 )
 if 77 - 77: O0OOOoOoo0 / Ii
elif I1I == 43 :
 IIiiiI ( oOooO0 )
 if 20 - 20: o0o00Oo0O . ooOOOoO
elif I1I == 20 :
 IiI1IiI1iiI1 ( oOooO0 )
 if 67 - 67: OOooOOo - I11i1ii1 - iI11I1II1I1I
elif I1I == 22 :
 o0OOo0oOOo ( oOooO0 )
 if 31 - 31: IIiIiII11i + I11i * Ii . I11i
elif I1I == 23 :
 Ooo0000o ( oOooO0 )
 if 73 - 73: o000O0o / Ii1IIIi1 * IIiIiII11i % ii - ooOoO0O00 - I11i1ii1
elif I1I == 24 :
 iIiiiiIi111I ( oOooO0 )
 if 43 - 43: I11i + ii1ii11IIIiiI % oO0o . iiiiiiii1 + ooOoO0O00
elif I1I == 25 :
 oOo ( oOooO0 )
 if 85 - 85: I1ii11iIi11i % Ii1I / Ii1IIIi1
elif I1I == 26 :
 ii1II1 ( oOooO0 )
 if 65 - 65: I11i1ii1 + I1111IIi - OOooOOo % IIiIiII11i - iI11I1II1I1I
elif I1I == 27 :
 o00o0oOo0O ( oOooO0 )
 if 39 - 39: oOo0O0Ooo + Ii1I - Ii
elif I1I == 28 :
 iII1IiI1I11i ( oOooO0 )
 if 43 - 43: iI11I1II1I1I
elif I1I == 29 :
 iIIIIiI1I ( oOooO0 )
 if 73 - 73: OOooOOo + I11i
elif I1I == 30 :
 iiIiI11IiI1ii ( oOooO0 )
 if 58 - 58: ooOoO0O00 * Ii1I % O0OOOoOoo0 . oO0o % I1111IIi % ooOOOoO
elif I1I == 31 :
 OOiI1I ( oOooO0 )
 if 63 - 63: Ii1I % I11i1ii1 % Ii1I
elif I1I == 32 :
 ii111i1i ( )
 if 71 - 71: ii1ii11IIIiiI
elif I1I == 33 :
 OOo0OOooo0 ( )
 if 43 - 43: I11i / I11i1ii1
elif I1I == 35 :
 OooOO ( oOooO0 )
 if 88 - 88: Ii - ooOoO0O00 + I1ii11iIi11i - o0o00Oo0O
elif I1I == 34 :
 oooOoOoOO ( oOooO0 )
 if 50 - 50: Ii1I
elif I1I == 36 :
 i1i1Ii1IiIII ( oOooO0 )
 if 37 - 37: o000O0o % O0OOOoOoo0 / IIiIiII11i / oO0o - I1111IIi - I11i1ii1
elif I1I == 37 :
 OooO00oo0O0 ( oOooO0 )
 if 69 - 69: Ii1I . ii % iiiiiiii1
elif I1I == 38 :
 IiI11IIi11Iii ( oOooO0 )
 if 79 - 79: oOo0O0Ooo - I1111IIi . ii - Ii1I
elif I1I == 41 :
 IiIIi1 ( IIIIiii1IIii )
 if 79 - 79: Ii1IIIi1 + I11i % O0OOOoOoo0 . o000O0o
elif I1I == 39 :
 O0O0OOOOoo ( oOooO0 )
 if 49 - 49: ii1ii11IIIiiI + Ii * OOooOOo . OOooOOo . Ii1I . I1ii11iIi11i
elif I1I == 45 :
 TEXTS ( )
 if 61 - 61: ooOOOoO / Ii1IIIi1
elif I1I == 46 :
 Ii1I1Ii ( )
 if 85 - 85: OOooOOo - ooOOOoO . OOooOOo . OOooOOo
elif I1I == 47 :
 GEVID ( )
 if 62 - 62: I1111IIi % ii * oO0o + oO0o % ii1ii11IIIiiI % O0OOOoOoo0
elif I1I == 48 :
 Oooo ( iiI11ii1I1 , oOooO0 , oOOo000oOoO0 )
 if 66 - 66: oOo0O0Ooo . Ii1IIIi1 - oO0o % I1ii11iIi11i * I11i - o000O0o
elif I1I == 49 :
 IiIi1I1 ( )
 if 68 - 68: ooOOOoO - Ii / I11i + I11i1ii1 / oOo0O0Ooo
elif I1I == 22222 :
 O0OoooI11iI1I ( oOooO0 )
 if 31 - 31: iiiiiiii1 . ii . ooOoO0O00
elif I1I == 222 :
 iI1I11II1Iii1 ( oOooO0 )
 if 65 - 65: oO0o . I11i1ii1
elif I1I == 2222222 :
 iii1 ( oOooO0 )
 if 12 - 12: iiiiiiii1 + o0o00Oo0O - o000O0o . I1111IIi
elif I1I == 222222 :
 O00O0oO ( oOooO0 , iiI11ii1I1 )
 if 46 - 46: I1111IIi . I11i1ii1 / O0OOOoOoo0
elif I1I == 333 :
 O0Oo ( oOooO0 )
 if 63 - 63: IIiIiII11i - Ii1I * IIiIiII11i
 if 92 - 92: oO0o % I11i1ii1 * o0o00Oo0O % iI11I1II1I1I / ooOoO0O00 / OOooOOo
elif I1I == 1020 :
 Oooo00oo0o ( )
 if 67 - 67: iiiiiiii1 + ooOOOoO + iiiiiiii1 . Ii1IIIi1 % I11i / I11i1ii1
elif I1I == 1021 :
 ANIMEEP ( )
 if 78 - 78: Ii1I . o0o00Oo0O
elif I1I == 1022 :
 ANIMEPLAY ( oOooO0 )
 if 56 - 56: o000O0o - ooOoO0O00 * o0o00Oo0O / ooOOOoO * oOo0O0Ooo . ooOOOoO
elif I1I == 1001 :
 iii1Ii ( )
 if 54 - 54: Ii % ooOoO0O00 + I1ii11iIi11i / OOooOOo
elif I1I == 1005 :
 iIi11OOo0oo ( )
 if 26 - 26: ooOOOoO . Ii1I
elif I1I == 1007 :
 OoOoO00OoOOo ( oOooO0 )
 if 55 - 55: OOooOOo * iiiiiiii1 % oO0o - oO0o
elif I1I == 1010 :
 OOO0O0OOo ( oOooO0 )
 if 34 - 34: o0o00Oo0O * oO0o - o000O0o - I1111IIi * ii1ii11IIIiiI . IIiIiII11i
elif I1I == 1011 :
 I1111 ( oOooO0 )
 if 28 - 28: o0o00Oo0O % O0OOOoOoo0 - ooOoO0O00
elif I1I == 1012 :
 i1i1IiIi1 ( oOooO0 )
 if 49 - 49: I11i1ii1 . ooOOOoO - iI11I1II1I1I
elif I1I == 1030 :
 o00O ( )
 if 41 - 41: I11i1ii1 * Ii % I11i1ii1 . o000O0o
elif I1I == 1031 :
 ii11 ( oOooO0 , I1iIi1iIiiIiI )
 if 97 - 97: o000O0o - O0OOOoOoo0 + I1111IIi . OOooOOo + iI11I1II1I1I
elif I1I == 1032 :
 IIII1ii1 ( oOooO0 )
 if 75 - 75: I11i1ii1 + I11i1ii1 . iiiiiiii1 % O0OOOoOoo0 / iI11I1II1I1I * O0OOOoOoo0
elif I1I == 1006 :
 Parse . ParseURL ( oOooO0 )
 if 13 - 13: IIiIiII11i * Ii - ooOoO0O00 * oO0o + ooOoO0O00
elif I1I == 2030 :
 Parse . addonParseURL ( oOooO0 )
 if 43 - 43: o0o00Oo0O % o000O0o * oOo0O0Ooo
elif I1I == 2031 :
 Parse . apkParseURL ( oOooO0 )
 if 64 - 64: IIiIiII11i + Ii
elif I1I == 2032 :
 Parse . ParseBOSS ( oOooO0 )
 if 17 - 17: o0o00Oo0O * oOo0O0Ooo
elif I1I == 1002 :
 Iiiiii1I ( oOooO0 )
 if 40 - 40: iI11I1II1I1I * O0OOOoOoo0 % iI11I1II1I1I
elif I1I == 1003 :
 ii1iiii11IiI1 ( oOooO0 , I1iIi1iIiiIiI )
 if 39 - 39: ooOoO0O00 . ii1ii11IIIiiI - I1ii11iIi11i
elif I1I == 1004 :
 O0OoO0ooOoo ( oOooO0 )
 if 91 - 91: oOo0O0Ooo - ii - ii
elif I1I == 1008 :
 o00OO0 ( )
 if 69 - 69: O0OOOoOoo0 * Ii / ooOoO0O00
elif I1I == 1009 :
 iII1i ( oOooO0 )
 if 86 - 86: oOo0O0Ooo % ooOOOoO * o0o00Oo0O + ooOoO0O00 % iiiiiiii1
elif I1I == 2001 :
 ooo0o ( )
 if 97 - 97: IIiIiII11i * OOooOOo - iiiiiiii1 / Ii / OOooOOo
elif I1I == 2002 :
 oOo0oOo ( oOooO0 )
 if 25 - 25: I1ii11iIi11i / I1ii11iIi11i
elif I1I == 1013 :
 ooOO0OOO00o ( )
elif I1I == 10111113 :
 o0oOOOOoo0 ( oOooO0 )
 if 74 - 74: Ii1IIIi1
elif I1I == 1014 :
 iIO0 ( )
 if 30 - 30: o0o00Oo0O . ii1ii11IIIiiI / I11i + oOo0O0Ooo - o0o00Oo0O
elif I1I == 1015 :
 oooO ( oOooO0 )
 if 88 - 88: Ii
elif I1I == 1016 :
 IiII1 ( oOooO0 , I1iIi1iIiiIiI , iiI11ii1I1 )
 if 33 - 33: oO0o + o0o00Oo0O
elif I1I == 1017 :
 i11iiI1111 ( )
 if 20 - 20: I11i % ooOOOoO . I11i1ii1 - ooOoO0O00 . o0o00Oo0O
elif I1I == 1018 :
 IIiIiiii ( oOooO0 )
 if 10 - 10: ooOoO0O00
elif I1I == 1023 :
 o00ooO0ooO0o0 ( )
 if 49 - 49: iiiiiiii1 - ii1ii11IIIiiI . o0o00Oo0O
elif I1I == 1024 :
 OOOOO0ooOOOoo ( oOooO0 )
 if 46 - 46: Ii1IIIi1
elif I1I == 1025 :
 ooo0o0oOoOO0 ( oOooO0 )
 if 64 - 64: oOo0O0Ooo / OOooOOo
elif I1I == 4001 :
 ooo0O0o00O ( )
 if 6 - 6: Ii - O0OOOoOoo0 * ooOoO0O00 - O0OOOoOoo0
elif I1I == 4002 :
 IIii1111 ( )
 if 8 - 8: ooOOOoO / Ii . o0o00Oo0O / oO0o * o000O0o + iiiiiiii1
elif I1I == 4003 :
 O0oII1IIiiI1 ( )
 if 91 - 91: oOo0O0Ooo
elif I1I == 4004 :
 oooooo0OO ( )
 if 84 - 84: o0o00Oo0O % ii1ii11IIIiiI
elif I1I == 4005 :
 iIi1Ii1i1iI ( )
 if 3 - 3: oOo0O0Ooo . ooOOOoO / Ii1I
elif I1I == 4006 :
 OO0oOOoo ( )
 if 2 - 2: I1111IIi + ooOOOoO / iI11I1II1I1I . Ii . ooOoO0O00 * I11i1ii1
elif I1I == 4007 :
 OOOOoO00o0O ( )
 if 14 - 14: I1ii11iIi11i . o0o00Oo0O - o000O0o - Ii
elif I1I == 4008 :
 II11IiiIII ( )
 if 8 - 8: oOo0O0Ooo / iI11I1II1I1I / ii / I1ii11iIi11i / I11i1ii1
elif I1I == 4009 : I11iiI11iiI ( )
elif I1I == 4010 : ooOii1i11 ( )
elif I1I == 3000 :
 Oo0o0o00Oo ( )
 if 80 - 80: ooOOOoO
elif I1I == 3001 :
 o0O0OOooO ( )
 if 26 - 26: IIiIiII11i + oOo0O0Ooo . IIiIiII11i - o000O0o % oO0o
elif I1I == 3002 :
 i1II111i1IIii ( oOooO0 )
 if 1 - 1: oO0o - IIiIiII11i
elif I1I == 3003 :
 IIIi1ii1i1 ( oOooO0 )
 if 75 - 75: I1ii11iIi11i - OOooOOo + o000O0o % ooOoO0O00 * Ii1IIIi1
elif I1I == 3004 :
 o00O0OooO0 ( oOooO0 )
 if 56 - 56: OOooOOo / oO0o / oOo0O0Ooo % ii
elif I1I == 404 :
 OooOii1Ii ( iiI11ii1I1 , oOooO0 , I1iIi1iIiiIiI )
 if 39 - 39: oOo0O0Ooo + IIiIiII11i * I1ii11iIi11i % ii1ii11IIIiiI . I11i * o000O0o
elif I1I == 405 :
 O000Oo0O ( oOooO0 )
 if 42 - 42: ii1ii11IIIiiI / I1ii11iIi11i
elif I1I == 7030 :
 ii1iOO00O0O00oOOO ( )
 if 25 - 25: ii % ii1ii11IIIiiI * iiiiiiii1 * ooOOOoO + oOo0O0Ooo % Ii1I
elif I1I == 7021 :
 ii11iI11I111I ( iiI11ii1I1 )
 if 70 - 70: ii1ii11IIIiiI + Ii1I * ooOOOoO * ooOoO0O00 . iiiiiiii1
elif I1I == 7022 :
 o0Ooo0o0ooOooo0 ( iiI11ii1I1 )
 if 76 - 76: ii * OOooOOo . ii
elif I1I == 7000 :
 i111I ( iiI11ii1I1 , oOooO0 , img )
 if 46 - 46: I11i1ii1 * I11i % IIiIiII11i / iiiiiiii1
elif I1I == 7050 :
 OoOoO0ooooO0 ( oOooO0 )
 if 29 - 29: oO0o - Ii % I1ii11iIi11i % I11i
elif I1I == 7051 :
 iiOOOO00oO ( oOooO0 )
 if 30 - 30: o000O0o - ii1ii11IIIiiI % ii1ii11IIIiiI
elif I1I == 7052 :
 I111II1ii11I1 ( oOooO0 )
 if 8 - 8: I1111IIi
elif I1I == 7053 :
 iIiiIII ( oOooO0 )
 if 68 - 68: I1111IIi . ii - Ii + Ii
elif I1I == 7054 :
 CoolPlay ( oOooO0 )
 if 81 - 81: OOooOOo + O0OOOoOoo0 . Ii
elif I1I == 7060 :
 oO0o0OOO0O ( )
 if 10 - 10: OOooOOo + ooOOOoO - iI11I1II1I1I - ooOOOoO
elif I1I == 7061 :
 III1I1Iii1iiI ( oOooO0 )
 if 58 - 58: I11i1ii1
elif I1I == 7063 :
 iIII111i1ii1I ( oOooO0 )
 if 98 - 98: ii1ii11IIIiiI / oO0o % ii
elif I1I == 7062 :
 IiiIii11iI1Iii1iI ( oOooO0 )
 if 65 - 65: I11i1ii1 % I1ii11iIi11i - oOo0O0Ooo % iiiiiiii1 + iI11I1II1I1I / iI11I1II1I1I
elif I1I == 7064 :
 NATatozcat ( )
 if 94 - 94: I1111IIi - I1ii11iIi11i . I11i - I11i1ii1 - o000O0o . ooOOOoO
elif I1I == 7067 :
 I1Iii11I ( oOooO0 )
 if 39 - 39: o000O0o + OOooOOo
elif I1I == 7066 :
 NATatozA ( oOooO0 )
 if 68 - 68: ooOoO0O00 * o000O0o / Ii
elif I1I == 7065 :
 OOoO00o00oo ( oOooO0 )
 if 96 - 96: oOo0O0Ooo
elif I1I == 7070 :
 oo00O0OO0oo0O ( )
 if 78 - 78: oO0o
elif I1I == 7071 :
 DIZIlist ( oOooO0 )
 if 72 - 72: Ii1I / o0o00Oo0O % IIiIiII11i / IIiIiII11i
elif I1I == 7072 :
 DIZIpull ( oOooO0 )
 if 48 - 48: Ii1IIIi1 % Ii1IIIi1 / iI11I1II1I1I - Ii
elif I1I == 7073 :
 WATCHDIZI ( oOooO0 )
 if 57 - 57: ooOOOoO / I1111IIi * ooOoO0O00 + IIiIiII11i . I11i
elif I1I == 7002 :
 OOO0 ( )
 if 11 - 11: IIiIiII11i
elif I1I == 7003 :
 OOOOoOO00 ( oOooO0 )
 if 66 - 66: ii1ii11IIIiiI - oOo0O0Ooo . ii * iiiiiiii1
elif I1I == 7004 :
 o00oOo0oO0oOO ( oOooO0 )
 if 16 - 16: I1111IIi * oO0o * Ii - I11i1ii1
elif I1I == 7020 :
 Iiii1I1iI ( oOooO0 )
 if 88 - 88: iI11I1II1I1I / ii1ii11IIIiiI * I1111IIi / iiiiiiii1
elif I1I == 7001 :
 ii1iiIiIII1ii ( )
 if 31 - 31: o0o00Oo0O . oOo0O0Ooo
elif I1I == 7010 :
 oO0ooOoOooO00o00 ( oOooO0 )
 if 8 - 8: OOooOOo
elif I1I == 7011 :
 Ii1 ( oOooO0 )
 if 99 - 99: O0OOOoOoo0
elif I1I == 7012 :
 o0o00O0oO ( oOooO0 )
 if 93 - 93: iiiiiiii1
elif I1I == 7013 :
 cnfTVPlay2 ( oOooO0 )
elif I1I == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oOooO0 )
elif I1I == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oOooO0 )
elif I1I == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( iiI11ii1I1 , oOooO0 , I1iIi1iIiiIiI )
elif I1I == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif I1I == 7018 :
 O0O0oooo ( )
elif I1I == 7019 :
 CNF_Studio_Indexer . List_Movies ( oOooO0 )
elif I1I == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oOooO0 )
elif I1I == 7024 :
 CNF_Studio_Indexer . Box_Office ( oOooO0 )
 if 39 - 39: ii1ii11IIIiiI
elif I1I == 8000 :
 O0OO0OOo00Oo ( )
elif I1I == 8001 :
 Oo0OOo ( )
elif I1I == 8002 :
 OO00O0O ( )
elif I1I == 8003 :
 I1i1IO0OOoooO ( )
elif I1I == 8004 :
 iIi ( )
elif I1I == 8005 :
 Ooo0O00 ( )
elif I1I == 8006 :
 Ooo00 ( iiI11ii1I1 , oOooO0 )
elif I1I == 8030 :
 IiIooOoOo0O00oo ( oOooO0 )
elif I1I == 8045 :
 o00OooooOOOO ( oOooO0 )
elif I1I == 8046 :
 oo000oiIIIII ( oOooO0 )
elif I1I == 8047 :
 IIoooOoOO0o ( oOooO0 )
elif I1I == 8048 :
 iI1i11II1i1i ( oOooO0 )
elif I1I == 8049 :
 O0O0O00OoO0O ( oOooO0 )
elif I1I == 804900 :
 i1II11III ( oOooO0 )
elif I1I == 8020 :
 I1IiiI1ii1i ( )
elif I1I == 8021 :
 Oo0 ( oOooO0 )
elif I1I == 8022 :
 II1I1iI11II1 ( oOooO0 )
elif I1I == 8023 :
 OOO0o0000 ( oOooO0 )
elif I1I == 8040 :
 o0OOOo ( )
elif I1I == 8041 :
 IIIiiII1iIi1ii1i ( oOooO0 )
elif I1I == 8042 :
 oO00O000o ( oOooO0 )
elif I1I == 8043 :
 yt . PlayVideo ( oOooO0 )
elif I1I == 8044 :
 o0o00 ( oOooO0 )
elif I1I == 8060 :
 O0Oooo ( )
elif I1I == 8061 :
 i1oOOOoOO ( oOooO0 )
elif I1I == 8064 :
 II1iiiiII ( )
elif I1I == 8065 :
 OOoo0o00O0oO ( oOooO0 )
elif I1I == 8070 :
 Iii1iIII1Iii ( )
elif I1I == 8071 :
 ii1ii1111 ( oOooO0 )
elif I1I == 7080 :
 iII11iiii111i ( oOooO0 )
elif I1I == 8090 :
 I1OO0o0OoooO00 ( )
elif I1I == 8091 :
 i1II111II1 ( oOooO0 )
elif I1I == 8092 :
 Ii1I1I11I1I1i ( oOooO0 )
elif I1I == 8093 :
 I11I1iiI1 ( oOooO0 )
elif I1I == 8081 :
 O0iIIii1 ( )
elif I1I == 8062 :
 OOOOo0oo0o ( oOooO0 )
elif I1I == 8063 :
 oo0iI1IIIi11iIII ( oOooO0 )
elif I1I == 8050 :
 oOOoO0O ( )
elif I1I == 8051 :
 OoOoOoOOo00Ooo0O ( oOooO0 )
elif I1I == 8052 :
 iIii1Oo ( oOooO0 )
elif I1I == 8085 :
 III11IiI ( )
elif I1I == 8086 :
 Iii1iI1I1iii1 ( oOooO0 )
elif I1I == 8087 :
 O0oOo00Oo0oo0 ( oOooO0 )
elif I1I == 8088 :
 i111 ( oOooO0 , iiI11ii1I1 )
elif I1I == 9000 :
 I1iI11IiiI11i ( )
elif I1I == 1111 :
 Iii1 ( )
elif I1I == 9001 :
 iI1I ( )
elif I1I == 9002 :
 IIiI1 ( )
elif I1I == 9003 :
 iI111iiI1II ( )
elif I1I == 9004 :
 World1 ( )
elif I1I == 9005 :
 World2 ( oOooO0 )
elif I1I == 9006 :
 World3 ( oOooO0 )
elif I1I == 9007 :
 OoOOOOooOo0 ( )
elif I1I == 9008 :
 o0000o0OOOo ( oOooO0 )
elif I1I == 9009 :
 iiiiiI1iii11 ( oOooO0 )
elif I1I == 9010 :
 oOo000O00O ( )
elif I1I == 9011 :
 OooO ( oOooO0 )
elif I1I == 50 :
 IIi1I ( oOooO0 )
elif I1I == 9020 :
 champlist ( )
elif I1I == 9021 :
 oooooOO0 ( )
elif I1I == 9022 :
 OOO0o0O ( )
elif I1I == 9023 :
 I111i ( )
elif I1I == 9024 :
 oOO ( oOooO0 )
elif I1I == 9030 :
 oOO00 ( oOooO0 )
elif I1I == 9031 :
 II1IiII1I1II ( oOooO0 )
elif I1I == 9032 :
 oooOII111iiI1Ii1 ( oOooO0 )
elif I1I == 9033 :
 oo0oO0oO00oO ( oOooO0 )
elif I1I == 9034 :
 I1ii1 ( )
elif I1I == 7085 :
 o00OooO ( oOooO0 )
elif I1I == 7086 :
 iIi1 ( oOooO0 )
elif I1I == 7087 :
 OoOoo ( oOOo000oOoO0 )
elif I1I == 9666 :
 ooO0O0O0ooOOO ( oOooO0 )
elif I1I == 10100 : O0OoOo0 ( )
elif I1I == 101001 : I1I11I1i1i1II ( oOooO0 )
elif I1I == 10105 : ii1II1I ( oOooO0 )
elif I1I == 10106 : oOoo0 ( oOooO0 )
elif I1I == 10104 : iiIiiiI ( oOooO0 )
elif I1I == 10107 : ii1II11IIII1 ( )
elif I1I == 10103 : oo0o0o ( oOooO0 )
elif I1I == 10108 : iII11I ( oOooO0 )
elif I1I == 10000 : Origin_Menu ( )
elif I1I == 10001 : OO0O0o0o0 ( )
elif I1I == 10002 : II1I1I1Ii ( )
elif I1I == 10003 : Iii1oooo00Oo0O ( )
elif I1I == 10004 : I11I1IIiiII1 ( oOooO0 )
elif I1I == 10005 : OO00oOooo0O ( )
elif I1I == 10006 : IiIii11ii111 ( oOooO0 )
elif I1I == 10007 : ii111 ( oOooO0 , I1iIi1iIiiIiI )
elif I1I == 10008 : IIiii1I1I ( )
elif I1I == 10009 : I111I ( )
elif I1I == 10010 : oOoOooO0OOOoo ( oOooO0 )
elif I1I == 10011 : oO0OO0O ( oOooO0 )
elif I1I == 10012 : iii1 ( oOooO0 )
elif I1I == 10113 : GRABG ( oOooO0 , iiI11ii1I1 )
elif I1I == 10109 : I1i1iiIi1Ii11I1 ( oOooO0 )
elif I1I == 10013 : i1IiIiiiii11 ( oOooO0 )
elif I1I == 10014 : OOoOoO ( )
elif I1I == 10015 : IiiII1I ( )
elif I1I == 10016 : III1i1iI1 ( oOooO0 )
elif I1I == 10017 : oOiii1IiII ( )
elif I1I == 10018 : IIi1i ( )
elif I1I == 10019 : IIOoOOoOo ( )
elif I1I == 10020 : OOI1III1I11I1 ( )
elif I1I == 10021 : oo0O0O ( )
elif I1I == 10022 : ooooOoo00 ( oOooO0 )
elif I1I == 10023 : II1OOO ( iiI11ii1I1 , oOooO0 )
elif I1I == 10024 : OOoOo0ooOoo ( oOooO0 )
elif I1I == 10025 : ooOOo00O00Oo ( )
elif I1I == 10026 : ii11iI1iIiiI ( )
elif I1I == 10027 : o0O0O0O00o ( )
elif I1I == 10028 : oOOOOO0 ( )
elif I1I == 10029 : iiII1i1111II ( )
elif I1I == 423 : o0IiiIIII1I1i ( oOooO0 )
elif I1I == 426 : Ii11Iiii1iiii ( oOooO0 )
elif I1I == 10030 : Izle_Films ( )
elif I1I == 10031 : Latest_Izle_Movies ( )
elif I1I == 10032 : Izle_Genres ( )
elif I1I == 10033 : Izle_Pop_Movies ( )
elif I1I == 10034 : Izle_Boxsets ( )
elif I1I == 10035 : Izle_Search ( )
elif I1I == 10036 : Izle_Genres_Movie ( oOooO0 )
elif I1I == 10037 : Izle_Boxset_single ( oOooO0 )
elif I1I == 10038 : Izle_IFRAME ( )
elif I1I == 10039 : Izle_Boxsets_Next ( oOooO0 )
elif I1I == 10040 : ii1 ( )
elif I1I == 10041 : Oooo0o00 ( oOooO0 )
elif I1I == 10042 : i1iII1111iIIiIIII ( oOooO0 )
elif I1I == 10043 : I11iIiiI ( )
elif I1I == 10044 : ooOoo0oo00000O ( oOooO0 )
elif I1I == 10045 : III1Ii11i1II ( iiI11ii1I1 )
elif I1I == 10046 : ooooOOo ( oOooO0 )
elif I1I == 10047 : oO0oO00 ( oOooO0 )
elif I1I == 10048 : O00oO0oo ( oOooO0 )
elif I1I == 10049 : iiIiI11IiI ( oOooO0 )
elif I1I == 10050 : OOI1iI1ii1II ( )
elif I1I == 10051 : Ii1iI1iiIiII1 ( )
elif I1I == 10052 : i1iI111i1I ( )
elif I1I == 10053 : Addon ( oOooO0 )
elif I1I == 10054 : Ii1IiIiI1Ii ( oOooO0 , iiI11ii1I1 )
elif I1I == 10055 :
 Oo00 ( "addFavorite" )
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 I1iII1II1I1ii ( iiI11ii1I1 , oOooO0 , I1iIi1iIiiIiI , O0OoooO0 , ii11I1IIII11 )
elif I1I == 10056 :
 Oo00 ( "rmFavorite" )
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  iiI11ii1I1 = iiI11ii1I1 . split ( '  - ' ) [ 0 ]
 except :
  pass
 OOO00000O ( iiI11ii1I1 )
elif I1I == 10057 :
 Oo00 ( "getFavorites" )
 o0oo000 ( )
elif I1I == 10058 : OOOII1i1II ( )
elif I1I == 10059 : Donators_Guide ( )
elif I1I == 10060 : I1i11 ( )
elif I1I == 10061 : ooOOo00 ( )
elif I1I == 10062 : OOOOoo00OO0O0Ooo0 ( iiI11ii1I1 , oOooO0 , oOOo000oOoO0 )
elif I1I == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
elif I1I == 10064 : O00000Oo00o ( )
elif I1I == 10065 : ooOO ( oOooO0 )
elif I1I == 10066 : iI1iiiIii1II1 ( oOooO0 )
elif I1I == 10068 : Oo00o0OO0O00o ( oOooO0 )
elif I1I == 10069 : O0OoOO0oo0 ( oOooO0 )
elif I1I == 10070 : O0O000O ( oOooO0 )
elif I1I == 10071 : Genie_Watch ( )
elif I1I == 10072 : OOOOo00oo00O ( )
elif I1I == 10073 : O00o0O ( oOooO0 )
elif I1I == 10074 : o0oO00 ( oOooO0 )
elif I1I == 10075 : O0OOo ( I1iIi1iIiiIiI , iiI11ii1I1 , oOooO0 )
elif I1I == 10076 : i111i1I1ii1i ( oOooO0 )
elif I1I == 10077 : o00OooOO0 ( oOooO0 )
elif I1I == 10078 : i1Ii ( )
elif I1I == 10079 : Genie_Watch_Tv_Shows ( )
elif I1I == 10080 : Genie_Watch_Tv_Genre ( oOooO0 )
elif I1I == 10081 : Genie_Watch_TV_PlayRun ( oOooO0 )
elif I1I == 10082 : Genie_Watch_TV_Episodes ( oOooO0 , I1iIi1iIiiIiI )
elif I1I == 10083 : Genie_Watch_Tv_Recent ( oOooO0 )
elif I1I == 10084 : Oo0ooo ( )
elif I1I == 10085 : Iiii1i1 ( )
elif I1I == 10086 : i1IiiiI1iI ( )
elif I1I == 20000 : iIIIIIiI1I1 ( )
elif I1I == 20001 : OO00OoOO ( oOooO0 )
elif I1I == 20002 : II1ii1 ( oOooO0 )
elif I1I == 20003 : i1iI1IIi ( oOooO0 )
elif I1I == 20004 : O000oooO0 ( oOooO0 )
elif I1I == 20005 : Ii111III1i11I ( oOooO0 )
elif I1I == 21004 : oOOOo ( )
elif I1I == 21005 : OoOiII11IiIi ( oOooO0 )
elif I1I == 21006 : IIiiiooOoOooo00Oo ( oOooO0 )
elif I1I == 21007 : Iii1IIII1Iii ( oOooO0 )
elif I1I == 30000 : OOoOi1IiiI ( )
elif I1I == 30001 : OOoo0OOOo0o ( )
elif I1I == 100121 : Resolve ( oOooO0 )
elif I1I == 30003 : oO0o000oOO ( )
elif I1I == 30004 : IiIIiiiIi ( oOooO0 )
elif I1I == 30005 : O0OO00 ( oOooO0 )
elif I1I == 30006 : O0o00 ( )
elif I1I == 30007 : IiIiI ( )
elif I1I == 30008 : o00ooO000Oo00 ( oOooO0 )
elif I1I == 30009 : I1i ( oOooO0 )
elif I1I == 30010 : IiOO0OOOOOo ( oOooO0 )
elif I1I == 30011 : iIiiI111I11 ( )
elif I1I == 30012 : o00O0 ( )
elif I1I == 30013 : o0O0o0O0OO0O ( )
elif I1I == 30014 : O0o00ooo ( )
elif I1I == 30015 : i1iI1IIi1I ( oOooO0 , I1iIi1iIiiIiI , O0OoooO0 )
elif I1I == 30016 : Ii11I1I11II ( oOooO0 )
elif I1I == 30019 : ii1II1iiii ( oOooO0 )
elif I1I == 30017 : iiI111i1 ( oOooO0 )
elif I1I == 30018 : iIii1I1111 ( oOooO0 )
elif I1I == 30030 : IIIi11i ( )
elif I1I == 30031 : oOooO0OoO ( )
elif I1I == 30032 : I1I1I1IIi1III ( )
elif I1I == 30033 : oooOOoo0 ( )
elif I1I == 30034 : Oo00O00o0 ( )
elif I1I == 30035 : o0O0 ( oOooO0 )
elif I1I == 30036 : oO0o0 ( oOooO0 )
elif I1I == 30037 : ooOoOoO0 ( oOooO0 )
elif I1I == 30038 : Oo0O0O ( )
elif I1I == 30039 : Ii1I1i ( )
elif I1I == 50000 : iIiIi11 ( )
elif I1I == 50001 : o0Oo00oOO ( )
elif I1I == 50002 : oO0000Oo ( oOooO0 )
elif I1I == 50003 : Table_Menu ( oOOo000oOoO0 )
elif I1I == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif I1I == 60001 : ooo0ii1iIIi11 ( )
elif I1I == 60002 : OOOO00OoooO ( iiI11ii1I1 )
elif I1I == 60003 : oOO0Oooo ( oOooO0 )
elif I1I == 600033 : II1OoooOo ( oOooO0 )
elif I1I == 60004 : oooooiIiIi ( oOooO0 )
elif I1I == 50004 : i11i1 ( )
elif I1I == 50005 : speedtest . runtest ( oOooO0 )
elif I1I == 70001 : O00O00 ( )
elif I1I == 70002 : O0Oo00o00OoO ( oOooO0 )
elif I1I == 70003 : II1i1I1111I1I ( oOooO0 )
elif I1I == 70004 : III1iiIIIII1 ( oOooO0 )
elif I1I == 70005 : oO0Oo0OOoo0oo ( oOooO0 )
elif I1I == 70006 : IiIi ( )
elif I1I == 50006 : iiIiI1i1 ( i1 , i1111 )
elif I1I == 80000 : iIi1i1i1II11I ( )
elif I1I == 80001 : resolvefilmon ( oOooO0 )
elif I1I == 80002 : I11ii1iI11 ( )
elif I1I == 80003 : ooOo00 ( iiI11ii1I1 , oOooO0 , "None" )
elif I1I == 80004 : Iii1II1ii ( iiI11ii1I1 , oOooO0 )
elif I1I == 80005 : i1Iii11I1i ( )
elif I1I == 80006 : Iii ( oOooO0 )
elif I1I == 80007 : II1iIii111iII ( oOooO0 )
elif I1I == 80008 : iI1iI1IiIIiI ( )
elif I1I == 80009 : iiI1iI1i1 ( )
elif I1I == 80010 : OOOo0O0o0oo ( oOooO0 )
elif I1I == 80011 : IiIi1I1IiI1II1 ( oOooO0 )
elif I1I == 80012 : oOOO ( )
elif I1I == 90000 : iII ( iiI11ii1I1 , oOooO0 )
elif I1I == 90001 : II11 ( )
elif I1I == 90002 : o00o0II1I ( )
elif I1I == 90003 : ooI1 ( oOooO0 )
elif I1I == 90004 : i1Iii1i1II1 ( oOooO0 )
elif I1I == 90005 : O0o00OoooO ( oOooO0 )
elif I1I == 90006 : i1ii1IiIiIii ( oOooO0 )
elif I1I == 90007 : OOo0ooOOOo0O0 ( oOooO0 )
elif I1I == 90008 : ooo ( oOooO0 )
elif I1I == 90009 : iIIiIi1IiI1 ( oOooO0 )
elif I1I == 90010 : oO0O00oOOoooO ( )
elif I1I == 90020 : o00Oo0O ( )
elif I1I == 90021 : hellyeah2 ( oOooO0 )
elif I1I == 90022 : hellyeah3 ( oOooO0 )
elif I1I == 90023 : iiOOOO0o ( )
elif I1I == 90024 : i11ii1Ii1 ( oOooO0 )
elif I1I == 90025 : oOO0o000Oo00o ( oOooO0 )
if 10 - 10: OOooOOo . iI11I1II1I1I / Ii1I % O0OOOoOoo0 / Ii
elif I1I == 90030 : I1i1I11I ( )
elif I1I == 90031 : i1I1IiiIi1i ( )
elif I1I == 90032 : Ooo0OOoOoO0 ( oOooO0 )
elif I1I == 90033 : IIo0Oo0oO0oOO00 ( oOooO0 )
elif I1I == 90034 : II1i111Ii1i ( oOooO0 )
elif I1I == 90035 : ooO0oooOO0 ( oOooO0 )
elif I1I == 90036 : oo00oO0o000 ( oOooO0 )
elif I1I == 90039 : iIi1ii ( oOooO0 )
elif I1I == 90037 : I1i11ii ( oOooO0 )
elif I1I == 90038 : iIIiiIIi1IiI ( )
if 14 - 14: Ii % I11i * o0o00Oo0O % iI11I1II1I1I . I1111IIi - IIiIiII11i
elif I1I == 10090 : i1iI1 ( )
elif I1I == 10091 : I1Io0OO ( oOooO0 )
elif I1I == 10092 : OoOo0000o0OOo ( oOooO0 )
elif I1I == 10093 : I11i1iiiiIIIi ( oOooO0 , I1iIi1iIiiIiI )
elif I1I == 10094 : i1111ii1I ( oOooO0 , I1iIi1iIiiIiI )
if 14 - 14: ii1ii11IIIiiI % I11i1ii1 - OOooOOo
elif I1I == 10095 : O0ooO0OoO00o ( )
elif I1I == 10096 : i1iii11 ( oOooO0 )
elif I1I == 10097 : iIooo0oo ( oOooO0 )
elif I1I == 10098 : iI11Ii111 ( oOooO0 )
elif I1I == 10099 : I1I1I11Ii ( oOooO0 )
if 52 - 52: oO0o / ooOoO0O00 - ii1ii11IIIiiI
elif I1I == 10200 : OooOoOo ( )
elif I1I == 10201 : II1i1III ( oOooO0 )
elif I1I == 10202 : iii1III1i ( oOooO0 )
elif I1I == 10203 : RT4 ( oOooO0 )
if 8 - 8: o000O0o + I11i1ii1 . Ii1I . ooOoO0O00 / oOo0O0Ooo . I1111IIi
elif I1I == 90040 : II11I ( )
elif I1I == 90041 : iIIiI11i1I11 ( oOooO0 )
elif I1I == 90042 : o0oO0OO00ooOO ( oOooO0 )
elif I1I == 90043 : III1iii1i1II ( oOooO0 )
elif I1I == 90044 : O0o00oO0oOO ( oOooO0 )
elif I1I == 90045 : II1I1i1i1iii ( )
elif I1I == 90046 : iiiii1I1III1 ( oOooO0 )
elif I1I == 90050 : i1II1i ( )
elif I1I == 90051 : i1I1II ( oOooO0 )
elif I1I == 90052 : OoOo00o ( oOooO0 )
elif I1I == 90053 : II1III1i1iiI ( oOooO0 )
elif I1I == 90054 : IiIi1i ( oOooO0 )
elif I1I == 90055 : I111i1Ii1i1 ( )
if 8 - 8: ooOoO0O00 * o0o00Oo0O
elif I1I == 100001 : Stand_up ( )
if 60 - 60: I1ii11iIi11i - IIiIiII11i + oOo0O0Ooo
elif I1I == 100003 : III1i1iI1 ( oOooO0 )
elif I1I == 100004 : OOOIiiiii1iI ( oOooO0 )
elif I1I == 100005 : Resolve ( oOooO0 )
elif I1I == 100008 : Search ( )
elif I1I == 100007 : IiII1II11I ( oOooO0 )
elif I1I == 100009 : yt . PlayVideo ( oOooO0 )
elif I1I == 100010 : I1Ii1111iIi ( oOooO0 )
elif I1I == 100100 : IiI11i1IIiiI ( I1iIi1iIiiIiI , oOooO0 , iiIiIi1I1 )
elif I1I == 100101 : Ii1iI111 ( oOooO0 , iiI11ii1I1 , O0OoooO0 , iiIiIi1I1 , I1iIi1iIiiIiI )
elif I1I == 100102 : ooOoo0o0O ( iiI11ii1I1 , oOooO0 , I1iIi1iIiiIiI , O0OoooO0 )
elif I1I == 100106 : ii1Ii1IiIIi ( oOooO0 , iiI11ii1I1 )
elif I1I == 100107 : IiI1I11iIii ( )
elif I1I == 100108 : i1iIiIIiIIII1 ( )
elif I1I == 100109 : oO0OOOo0OO ( oOooO0 )
elif I1I == 40000 : OOoooO00o0o ( )
elif I1I == 40001 : iI111I1III ( oOooO0 )
elif I1I == 100110 : Oo ( )
elif I1I == 100111 : oo0oooo0OoO0o ( oOooO0 )
elif I1I == 100110 : Oo ( )
elif I1I == 100210 : IiI1i ( oOooO0 )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
