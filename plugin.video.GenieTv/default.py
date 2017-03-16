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
IiiIII111iI = "3.4.8"
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
 iiOOooooO0Oo ( '[COLOR' + II + ']Tommys Replays[/COLOR]' , str ( I1I1IiI1 ) , 900300 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 if 46 - 46: oOo0O0Ooo - ii - ooOOOoO * IIiIiII11i
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.sportinglife.com/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 34 - 34: ooOOOoO - O0OOOoOoo0 / Ii1IIIi1 + Ii1I * ii1ii11IIIiiI
def OOOO0OoOO0o0o ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']our match eng prem[/COLOR]' , 'http://ourmatch.net/videos/england/premier-league-highlights/' , 900301 , III1iII1I1ii + 'tommysreplays.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']our match la liga[/COLOR]' , 'http://ourmatch.net/videos/spain/la-liga-highlights/' , 900301 , III1iII1I1ii + 'tommysreplays.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']our match serie a[/COLOR]' , 'http://ourmatch.net/videos/italy/serie-a-highlights/' , 900301 , III1iII1I1ii + 'tommysreplays.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']our match bund[/COLOR]' , 'http://ourmatch.net/videos/germany/bundesliga-highlights/' , 900301 , III1iII1I1ii + 'tommysreplays.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']our match ligue 1[/COLOR]' , 'http://ourmatch.net/videos/france/ligue-1-highlights/' , 900301 , III1iII1I1ii + 'tommysreplays.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']our match uefa champ[/COLOR]' , 'http://ourmatch.net/videos/europe/uefa-champions-league-highlights/' , 900301 , III1iII1I1ii + 'tommysreplays.png' , '' , '' )
III1iII1I1ii + 'tommysreplays.png'
def ooI1111i ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']GOAL OF THE MONTH[/COLOR]' , 'http://ourmatch.net/goal-of-the-month/' , 900302 , III1iII1I1ii + 'tommysreplays.png' , III1iII1I1ii + 'tommysreplays.png' , '' )
 oO0OOoo0OO = OoOooO ( url )
 iIIii = re . compile ( 'href="([^"]*)".+?<img src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o00O0O = re . compile ( 'class=\'current\'>.+?</span><a class=.+? href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url , ii1iii1i , Iii1I1111ii in iIIii :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 900302 , ii1iii1i , III1iII1I1ii + 'tommysreplays.png' , '' )
 for ooOoO00 in o00O0O :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ooOoO00 , 900301 , III1iII1I1ii + 'NEXT.png' , '' , '' )
def Ii1IIiI1i ( url ) :
 o0O00Oo0 = OoOooO ( url )
 iIIii = re . compile ( "<source src=\"(.+?)\"></video>',.+?'type':'([^']*)'," , re . DOTALL ) . findall ( o0O00Oo0 )
 IiII111i1i11 = re . compile ( "embed:'<iframe src=\"(.+?)\" width=.+? 'type':'([^']*)'," , re . DOTALL ) . findall ( o0O00Oo0 )
 for url , Iii1I1111ii in iIIii :
  OOiIiIIi1 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 222 , III1iII1I1ii + 'tommysreplays.png' , III1iII1I1ii + 'tommysreplays.png' , '' )
 for url , Iii1I1111ii in IiII111i1i11 :
  OOiIiIIi1 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 222 , III1iII1I1ii + 'tommysreplays.png' , III1iII1I1ii + 'tommysreplays.png' , '' )
def i111iIi1i1II1 ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdG9tbXlzbGlzdC50eHQ=' ) )
 i1IIIII11I1IiI = re . compile ( 'date="([^"]*)".+?list="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 for i1I1i111Ii , ooo in i1IIIII11I1IiI :
  iiIiI1i1 ( '[COLOR' + II + ']Tommys List[/COLOR]  ' + i1I1i111Ii , ooo )
def i1i1iI1iiiI ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Last Highlight | Football Highlights[/COLOR]' , ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) ) , 90032 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 oooO = OoOooO ( i11 ( 'aHR0cDovL2xhc3RobC5jb20v' ) )
 i1IIIII11I1IiI = re . compile ( 'menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 90032 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
def Ooo0oOooo0 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="bookmark" title="([^"]*)"><img width=".+?" height=".+?" class="entry-thumb" src="([^"]*)" ' , re . DOTALL ) . findall ( oooO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oooO )
 for url , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) , url , 90033 , ii1iii1i , O0o0Oo , '' )
 for url in next :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']NEXT[/COLOR]' ) . replace ( '&#038;' , '&' ) , url , 90032 , III1iII1I1ii + 'NEXT.png' , O0o0Oo , '' )
def oOOOoo00 ( url ) :
 oooO = OoOooO ( url )
 iiIiIIIiiI = re . compile ( '"file":"([^"]*)"' , re . DOTALL ) . findall ( oooO )
 iiI1IIIi = re . compile ( '<!--(.+?)--><br />\n<iframe.+?src="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( '<strong>(.+?)</strong><br />\n<iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 i1IIIII11I1IiI = re . compile ( 'id="([^"]*)"><iframe style="border:0px #FFFFFF none;" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="400" width="100%" src="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for Iii1I1111ii , url in i1I :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for Iii1I1111ii , url in iiI1IIIi :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Full Show[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , 'http:' + url , 90034 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
 for url in iiIiIIIiiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']Play[/COLOR]' ) . replace ( 'pane-0-0' , 'HighLights' ) . replace ( 'pane-0-1' , 'First Half' ) . replace ( 'pane-0-2' , 'Second Half' ) , url , 222 , III1iII1I1ii + 'tommysreplays.png' , O0o0Oo , '' )
  if 47 - 47: I1ii11iIi11i % ooOOOoO % Ii - o0o00Oo0O + I11i1ii1
def ooO000OO0O00O ( url ) :
 if 'drive' in url :
  OOOoOO0o ( url )
 else :
  oooO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'sources:.+?file:"([^"]*)"' ) . findall ( oooO )
  for url in i1IIIII11I1IiI :
   OOOoOO0o ( url )
def i1II1 ( url ) :
 i11i1 = liveresolver . resolve ( url )
 IiiiiI1i1Iii = xbmcgui . ListItem ( path = i11i1 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiiiiI1i1Iii )
def oo00oO0o ( url ) :
 _log ( "play_resolved_url [" + url + "]" )
 iiii111II = xbmcgui . ListItem ( path = url )
 return xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiii111II )
def iiiiI ( ) :
 I11iIiI1I1i11 = False
 if os . path . exists ( os . path . join ( OooO0 , 'xbmc.log' ) ) :
  I11iIiI1I1i11 = os . path . join ( OooO0 , 'xbmc.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'kodi.log' ) ) :
  I11iIiI1I1i11 = os . path . join ( OooO0 , 'kodi.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'spmc.log' ) ) :
  I11iIiI1I1i11 = os . path . join ( OooO0 , 'spmc.log' )
 elif os . path . exists ( os . path . join ( OooO0 , 'tvmc.log' ) ) :
  I11iIiI1I1i11 = os . path . join ( OooO0 , 'tvmc.log' )
 return I11iIiI1I1i11
 if 92 - 92: Ii1I * ooOoO0O00 . o000O0o / iiiiiiii1
def ooo0O0o00O ( url ) :
 if url == 'http://' : return False
 try :
  O00O0oOO00O00 = urllib2 . Request ( url )
  O00O0oOO00O00 . add_header ( 'User-Agent' , I1i1iiI1 )
  i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
  i1Oo00 . close ( )
 except Exception , I1i11 :
  return I1i11
 return True
def IiIi1I1 ( ) :
 if 39 - 39: IIiIiII11i + OOooOOo - I11i1ii1 . OOooOOo
 if 84 - 84: oO0o + ooOoO0O00 - IIiIiII11i . Ii1I * ii + oOo0O0Ooo
 if 38 - 38: Ii1IIIi1 + IIiIiII11i % I11i1ii1 % OOooOOo - ii1ii11IIIiiI / ii
 if 73 - 73: I11i * o0o00Oo0O - Ii
 if 85 - 85: ii1ii11IIIiiI % O0OOOoOoo0 + ooOOOoO / I11i . o000O0o + Ii1IIIi1
 i1i = OoOooO ( oOOoo00O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?con="([^"]*)".+?anart="([^"]*)"' ) . findall ( i1i )
 if len ( i1IIIII11I1IiI ) > 0 :
  for Iii1I1111ii , oOooO0 , ooOoOo0 , I11iiiiI1i in i1IIIII11I1IiI :
   OOiIiIIi1 ( Iii1I1111ii , oOooO0 , 50005 , ooOoOo0 , I11iiiiI1i , '' )
def iI1i11 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , '[COLOR' + II + ']WIPE GENIE[/COLOR]' , '[COLOR' + II + ']Genie BUILDS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Wizard[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OoOOoooOO0O ( )
  if iI11iI1IiiIiI == 1 :
   ooo00Ooo ( )
  if iI11iI1IiiIiI == 2 :
   Oo0o0O00 ( ii1 )
  if iI11iI1IiiIiI == 3 :
   I1i11OO ( oOooO0 )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']BACKUP MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 10060 , III1iII1I1ii + 'BackupMyBuild.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RESTORE MY BUILD[/COLOR]' , str ( I1I1IiI1 ) , 49 , III1iII1I1ii + 'RestoreMyBuild.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']WIPE GENIE[/COLOR]' , str ( I1I1IiI1 ) , 41 , III1iII1I1ii + 'WipeGenie.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Genie BUILDS[/COLOR]' , str ( I1I1IiI1 ) , 44 , III1iII1I1ii + 'GenieBuilds.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 84 - 84: I11i1ii1 % ii1ii11IIIiiI + Ii
def II1I1Ii ( ) :
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
   if 62 - 62: o0o00Oo0O % ooOOOoO . ooOOOoO - iI11I1II1I1I / Ii
   if 31 - 31: iI11I1II1I1I / oO0o / Ii1I
   if 41 - 41: I1ii11iIi11i
   if 10 - 10: I1ii11iIi11i / I1ii11iIi11i / iiiiiiii1 . iiiiiiii1
   if 98 - 98: I1ii11iIi11i / oOo0O0Ooo . o0o00Oo0O + oO0o
   if 43 - 43: IIiIiII11i . o000O0o / Ii1I
   if 20 - 20: oOo0O0Ooo
   if 95 - 95: O0OOOoOoo0 - oOo0O0Ooo
   if 34 - 34: I11i1ii1 * oOo0O0Ooo . ooOoO0O00 * I11i1ii1 / I11i1ii1
   if 30 - 30: Ii1I + I1ii11iIi11i / I1ii11iIi11i % Ii1I . Ii1I
   if 55 - 55: I11i1ii1 - ooOOOoO + IIiIiII11i + O0OOOoOoo0 % ii1ii11IIIiiI
   if 41 - 41: ooOoO0O00 - ooOOOoO - ii1ii11IIIiiI
   if 8 - 8: oO0o + iiiiiiii1 - I11i % I1ii11iIi11i % I11i * o000O0o
   if 9 - 9: I1ii11iIi11i - Ii - Ii1IIIi1 * ii1ii11IIIiiI + I11i1ii1
   if 44 - 44: IIiIiII11i
   if 52 - 52: Ii1I - I1ii11iIi11i + Ii1I % I11i
   if 35 - 35: iI11I1II1I1I
   if 42 - 42: iiiiiiii1 . oOo0O0Ooo . ooOoO0O00 + OOooOOo + Ii1IIIi1 + oOo0O0Ooo
   if 31 - 31: O0OOOoOoo0 . Ii1IIIi1 - I11i1ii1 . ii / ii
 I1I11i ( 'movies' , 'MAIN' )
def OOoOiiII1i11i ( ) :
 i111I1 = [ '[COLOR' + II + ']FOOTBALL[/COLOR]' , '[COLOR' + II + ']KIDS[/COLOR]' , '[COLOR' + II + ']NEWS[/COLOR]' , '[COLOR' + II + ']HOBBIES[/COLOR]' , '[COLOR' + II + ']DOCUMENTARIES[/COLOR]' , '[COLOR' + II + ']DISCLOSE TV[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']CATEGORIES[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  IiIi ( )
 if iI11iI1IiiIiI == 1 :
  OOOOO0O00 ( )
 if iI11iI1IiiIiI == 2 :
  Iii ( )
 if iI11iI1IiiIiI == 3 :
  iIIiIiI1I1 ( )
 if iI11iI1IiiIiI == 4 :
  ooO ( )
 if iI11iI1IiiIiI == 5 :
  iiOO0O0Ooo ( )
  if 77 - 77: I11i / ii
  if 46 - 46: I11i % iI11I1II1I1I . O0OOOoOoo0 % O0OOOoOoo0 + Ii
  if 72 - 72: iI11I1II1I1I * ii1ii11IIIiiI % I11i1ii1 / oO0o
def ii1Ii11I ( ) :
 if not os . path . exists ( IIIII ) :
  iiIiI1i1 ( 'Change Log 16/3/17 - v3.4.8' , 'All Categories In GTV Live Lists Updated,[CR]BamfTv Added To StreamTeam,[CR] Pirate Movies Added To StreamTeam,[CR]GenieTv Now Krypton Compatible,[CR] G.O.D.S (GenieTv On Demand Soaps) Added To GenieTv,[CR] RaysRavers And RaizTv Updated,[CR] More Sections Now Available For Download Including Kids,[CR] Tv Guide Removed And Replaced By External App,[CR] Boss Documentaries A Masterpiece By Jason Cadd,[CR] Updates To All Searches,[CR] StreamTeam Cleaned Up,[CR] Addon Overall CleanUp,[CR] General Maintence' )
  os . makedirs ( IIIII )
  if 35 - 35: I11i1ii1 + ooOoO0O00 % Ii1I % ooOOOoO + o000O0o
  if 17 - 17: ooOoO0O00
def iiIi1i ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , '[COLOR' + II + ']POPCORN BOX[/COLOR]' , '[COLOR' + II + ']DESI FLIX[/COLOR]' , '[COLOR' + II + ']FILM TRAILERS[/COLOR]' , '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']MOVIES[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   I1i11111i1i11 ( )
  if iI11iI1IiiIiI == 1 :
   OOoOOO0 ( )
  if iI11iI1IiiIiI == 2 :
   I1I1i ( oOooO0 )
  if iI11iI1IiiIiI == 3 :
   I1IIIiIiIi ( )
  if iI11iI1IiiIiI == 4 :
   IIIII1 ( i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) )
  if iI11iI1IiiIiI == 5 :
   iIi1Ii1i1iI ( )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 9001 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TOP RATED MOVIES[/COLOR]' , str ( I1I1IiI1 ) , 10200 , III1iII1I1ii + 'rated.png' , O0o0Oo , '' )
  if 16 - 16: Ii1IIIi1 / I1ii11iIi11i / ii * oOo0O0Ooo + ooOoO0O00 % Ii1IIIi1
  if oo00 . getSetting ( 'Popcorn Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']POPCORN BOX[/COLOR]' , str ( I1I1IiI1 ) , 7061 , III1iII1I1ii + 'PopcornBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Desi Flix[/COLOR]' , '' , 80005 , III1iII1I1ii + 'Desi.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']Film Trailers[/COLOR]' , i11 ( 'aHR0cDovL3RoZW1vdmllYm94Lm5ldC9leHBsb3Jl' ) , 10068 , III1iII1I1ii + 'FilmTrailers.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC MOVIES' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC MOVIES[/COLOR]' , '' , 8060 , III1iII1I1ii + 'ClassicMovies.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def ooo0o00 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']DAILY LISTS[/COLOR]' , '' , 9007 , Oo00OOOOO , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']WEB LISTS[/COLOR]' , 'http://iptvsatlinks.blogspot.co.uk/' , 9030 , Oo00OOOOO , O0o0Oo , '' )
 if 99 - 99: o0o00Oo0O . ooOOOoO + iI11I1II1I1I
 if 32 - 32: ii1ii11IIIiiI . iI11I1II1I1I % iI11I1II1I1I * Ii - oO0o - ooOOOoO
 if 63 - 63: oO0o
 if 69 - 69: iI11I1II1I1I . Ii1I % I11i1ii1 + iI11I1II1I1I / o0o00Oo0O / Ii1I
 if 61 - 61: Ii1IIIi1 % Ii1IIIi1 * I11i / I11i
def o0oOO ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']THE SOURCE[/COLOR]' , '[COLOR' + II + ']WATCH SERIES[/COLOR]' , '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '[COLOR' + II + ']RETURN DATES[/COLOR]' , '[COLOR' + II + ']CLASSIC TV[/COLOR]' , '[COLOR' + II + ']TV SHOW TRAILERS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TV SHOWS[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   O0o0OO0000ooo ( )
  if iI11iI1IiiIiI == 1 :
   iIIII1iIIii ( )
  if iI11iI1IiiIiI == 2 :
   oOOO00o000o ( )
  if iI11iI1IiiIiI == 3 :
   iIi11i1 ( )
  if iI11iI1IiiIiI == 4 :
   oO00oo0o00o0o ( )
  if iI11iI1IiiIiI == 5 :
   IiIIIIIi ( )
  if iI11iI1IiiIiI == 6 :
   IiIi1iIIi1 ( i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , str ( I1I1IiI1 ) , 9002 , III1iII1I1ii + 'Search.png' , O0o0Oo , '' )
  if 86 - 86: ooOOOoO * oOo0O0Ooo + ooOOOoO + IIiIiII11i
  if 8 - 8: iiiiiiii1 - O0OOOoOoo0 / I11i1ii1
  if 96 - 96: OOooOOo
  iiOOooooO0Oo ( '[COLOR' + II + ']iWATCH SERIES[/COLOR]' , '' , 8020 , III1iII1I1ii + 'iWatchSeries.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RETURN DATES[/COLOR]' , str ( I1I1IiI1 ) , 10095 , III1iII1I1ii + 'RD.png' , O0o0Oo , '' )
  if oo00 . getSetting ( 'CLASSIC TV' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']CLASSIC TV[/COLOR]' , str ( I1I1IiI1 ) , 8064 , III1iII1I1ii + 'ClassicTV.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TV Show Trailers[/COLOR]' , i11 ( 'aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj03WkZJUzJBcUF6OCZsaXN0PVBMM2t4NWgyVHJZR3dwVzBWYk5lbnBqLUJLTUJUR2dKUEU=' ) , 10069 , III1iII1I1ii + 'TVShowTrailers.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
def IIiiI ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   III1i11 = '[COLOR' + II + ']PANDORAS BOX[/COLOR]'
   if 25 - 25: oO0o
   if 24 - 24: I1111IIi * Ii * Ii1IIIi1
   if 85 - 85: I11i . OOooOOo / I11i1ii1 . o0o00Oo0O % iiiiiiii1
   if 90 - 90: I1ii11iIi11i % o0o00Oo0O * iI11I1II1I1I . O0OOOoOoo0
  i111I1 = [ III1i11 , '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , '[COLOR' + II + ']RAIZ TV[/COLOR]' , '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , '[COLOR' + II + ']BAMF TV[/COLOR]' , '[COLOR' + II + ']PIRATE MOVIES[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']StreamTeam[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   I1iii11 ( )
  if iI11iI1IiiIiI == 1 :
   ooo0O ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , iII1iii , Iii1I1111ii )
  if iI11iI1IiiIiI == 2 :
   i11i1iiiII ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0' ) ) )
  if iI11iI1IiiIiI == 3 :
   ooo0O ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , iII1iii , Iii1I1111ii )
   if 68 - 68: Ii * oO0o
  if iI11iI1IiiIiI == 4 :
   II1i ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) )
  if iI11iI1IiiIiI == 5 :
   ooo0O ( ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , iII1iii , Iii1I1111ii )
 else :
  if 2 - 2: iI11I1II1I1I * I1ii11iIi11i % o000O0o - IIiIiII11i - O0OOOoOoo0
  if 3 - 3: iiiiiiii1
  if oo00 . getSetting ( 'Pandoras Box' ) == 'true' :
   iiOOooooO0Oo ( '[COLOR' + II + ']PANDORAS BOX[/COLOR]' , str ( I1I1IiI1 ) , 10025 , III1iII1I1ii + 'PandorasBox.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']TECHNICA STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9nYS90ZWMvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'Technica-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']ROADRUNNER STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9ST0FEUlVOTkVSL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'Roadrunner-Streams.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']RAIZ TV[/COLOR]' , ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL3JhaXp0di9yYWl6dHYudHh0' ) ) , 90037 , III1iII1I1ii + 'raiztv.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']BAMF TV[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL0JBTUYueG1s' ) ) , 1018 , III1iII1I1ii + 'bamftv.png' , O0o0Oo , '' )
  iiOOooooO0Oo ( '[COLOR' + II + ']PIRATE MOVIES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9waXJhdGUvbWFpbi5waHA=' ) ) , 1016 , III1iII1I1ii + 'pirate.png' , O0o0Oo , '' )
  if 45 - 45: iiiiiiii1
  if 83 - 83: OOooOOo . ii
  if 58 - 58: Ii + ii % ii / I1111IIi / Ii
  if 62 - 62: oO0o / Ii1I
  if 7 - 7: ii . I1111IIi
  if 53 - 53: ii1ii11IIIiiI % ii1ii11IIIiiI * I11i + OOooOOo
 I1I11i ( 'movies' , 'MAIN' )
 if 92 - 92: ii + ooOoO0O00 / ii1ii11IIIiiI * o0o00Oo0O
def O00oOo00o0o ( ) :
 Oo0oO ( )
 OOiIiIIi1 ( '[COLOR' + II + ']SILENT HUNTER[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1006 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 1[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni8=' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SERVER 2[/COLOR]' , ( i11 ( 'aHR0cDovL3NpbGVudGh1bnRlci5zcnZlLmlvLw==' ) ) , 1018 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovLzUuMTM1LjIwNy45Ni9TY3JhcGVzL21haW4ucGhw' ) ) , 1016 , III1iII1I1ii + 'SilentHunter.png' , O0o0Oo , '' )
def II1i ( url ) :
 oooO = OoOooO ( url )
 O00oO0 = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( oooO )
 i1IIIII11I1IiI = re . compile ( '<title>(.+?)</title>.+?<link>ignoreme</link>.+?<thumbnail>(.+?)</thumbnail>.+?<externallink>(.+?)</externallink>' , re . DOTALL ) . findall ( str ( O00oO0 ) )
 i1I = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<referer></referer>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O00oO0 ) )
 iiI1IIIi = re . compile ( '<title>(.+?)</title>.+?<utube>(.+?)</utube>.+?<thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( str ( O00oO0 ) )
 for Iii1I1111ii , ii1iii1i , url in i1IIIII11I1IiI :
  if '247ch' in url :
   O0Oo00OoOo ( Iii1I1111ii , url , 10190 , ii1iii1i )
  elif '.m3u' in url :
   O0Oo00OoOo ( Iii1I1111ii , url , 1019 , ii1iii1i )
  elif '.xml' in url :
   O0Oo00OoOo ( Iii1I1111ii , url , 1018 , ii1iii1i )
  else :
   ii1ii111 ( Iii1I1111ii , url , 222 , ii1iii1i )
 for Iii1I1111ii , url , ii1iii1i in i1I :
  if '.xml' in url :
   O0Oo00OoOo ( Iii1I1111ii , url , 1018 , ii1iii1i )
  elif '.m3u' in url :
   O0Oo00OoOo ( Iii1I1111ii , url , 1019 , ii1iii1i )
  else :
   ii1ii111 ( Iii1I1111ii , url , 222 , ii1iii1i )
 for Iii1I1111ii , url , ii1iii1i in iiI1IIIi :
  ii1ii111 ( Iii1I1111ii , url , 8043 , ii1iii1i )
def i11111I1I ( url ) :
 oO0OOoo0OO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 222 , III1iII1I1ii + 'BAMFTV.png' )
def I11o0oO00oO0o0o0 ( url ) :
 oO0OOoo0OO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<title>(.+?)</title>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<referer></referer>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , url , ii1iii1i in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 222 , ii1iii1i )
  if 17 - 17: ooOOOoO . I1111IIi - IIiIiII11i + o0o00Oo0O / iI11I1II1I1I / Ii
def I1IIIiI1I1ii1 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tYWluLnBocA==' ) ) , 1016 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']APPRENTICE SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9zY3JhcGVkL3NjcmFwZWQucGhw' ) ) , 1024 , III1iII1I1ii + 'scraped.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Where The Magics AT[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWMucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Magic[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYWJyYWNhZGFicmEvbWFnaWNuZXcucGhw' ) ) , 100004 , III1iII1I1ii + 'newaddmagic.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Sitcoms[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9UVl9TaG93cy5waHA=' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLORred]****[/COLOR][COLOR' + II + ']Newly Added Comedy[/COLOR][COLORred]****[/COLOR]' , ( i11 ( 'aHR0cDovL2hlcm92aXNpb24ueDEwaG9zdC5jb20vYnJpdGNvbS9uZXcucGhw' ) ) , 100010 , III1iII1I1ii + 'newaddsit.png' , O0o0Oo , '' )
 if 30 - 30: o0o00Oo0O * ii
def I1iIIIi1 ( url ) :
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 i1IIIII11I1IiI = re . compile ( '<NAME="(.+?)"<URL="(.+?)"<MODE="(.+?)"<IMAGE="(.+?)"<FANART="(.+?)"<DESC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , url , iIiiiii1i , iiIi1IIiI , I11iiiiI1i , i1oO0OO0 in i1IIIII11I1IiI :
  if iiIi1IIiI == '123' :
   iiIi1IIiI = III1iII1I1ii + 'appstreams.png'
  if I11iiiiI1i == '123' :
   I11iiiiI1i = III1iII1I1ii + 'appstreams.png'
  if 'php' in url :
   iiOOooooO0Oo ( Iii1I1111ii , url , 100010 , iiIi1IIiI , I11iiiiI1i , i1oO0OO0 )
  elif 'playlist' in url :
   iiOOooooO0Oo ( Iii1I1111ii , url , 100007 , iiIi1IIiI , I11iiiiI1i , i1oO0OO0 )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( Iii1I1111ii , url , 100100 , iiIi1IIiI , I11iiiiI1i , i1oO0OO0 )
  elif not 'http' in url :
   o0O0Oo00 ( Iii1I1111ii , url , 100009 , iiIi1IIiI , I11iiiiI1i , i1oO0OO0 , '' )
  else :
   o0O0Oo00 ( Iii1I1111ii , url , 100005 , iiIi1IIiI , I11iiiiI1i , i1oO0OO0 , '' )
   if 51 - 51: Ii1IIIi1 % iI11I1II1I1I - ii % I11i1ii1 * iI11I1II1I1I % oO0o
def oO0o00oOOooO0 ( url ) :
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 OOOoO000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , ii1iii1i , i1oO0OO0 , I11iiiiI1i , Iii1I1111ii in OOOoO000 :
  if ii1iii1i == '123' :
   ii1iii1i = III1iII1I1ii + 'appstreams.png'
  if I11iiiiI1i == '123' :
   I11iiiiI1i = O0o0Oo
  if 'php' in url :
   iiOOooooO0Oo ( Iii1I1111ii , url , 100004 , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
  elif 'playlist' in url :
   iiOOooooO0Oo ( Iii1I1111ii , url , 100007 , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
  elif 'watchseries' in url :
   iiOOooooO0Oo ( Iii1I1111ii , url , 100100 , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
  elif not 'http' in url :
   o0O0Oo00 ( Iii1I1111ii , url , 100009 , ii1iii1i , I11iiiiI1i , i1oO0OO0 , '' )
  else :
   o0O0Oo00 ( Iii1I1111ii , url , 100005 , ii1iii1i , I11iiiiI1i , i1oO0OO0 , '' )
   if 57 - 57: IIiIiII11i
def oOOOoo ( url ) :
 if 15 - 15: Ii % oOo0O0Ooo * ooOOOoO / iiiiiiii1
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 oooO0o0o0O0 = re . compile ( '<tr class="pl-video yt-uix-tile(.+?)</tr>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O00oO0 in oooO0o0o0O0 :
  iiIi1IIiI = re . compile ( 'data-thumb="(.+?)"' ) . findall ( str ( O00oO0 ) )
  for iiIi1IIiI in iiIi1IIiI :
   iiIi1IIiI = iiIi1IIiI
  Iii1I1111ii = re . compile ( 'data-title="(.+?)"' ) . findall ( str ( O00oO0 ) )
  for Iii1I1111ii in Iii1I1111ii :
   if 'elete' in Iii1I1111ii :
    pass
   elif 'rivate Vid' in Iii1I1111ii :
    pass
   else :
    Iii1I1111ii = ( Iii1I1111ii ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&amp;' , '&' )
  iii11111I = re . compile ( '<div class="timestamp"><span aria-label=".+?">(.+?)</span>' ) . findall ( str ( O00oO0 ) )
  for iii11111I in iii11111I :
   iii11111I = iii11111I
  url = re . compile ( 'data-video-ids="(.+?)"' ) . findall ( str ( O00oO0 ) )
  for url in url :
   url = url
  o0O0Oo00 ( '[COLORred]' + str ( iii11111I ) + '[/COLOR] : ' + str ( Iii1I1111ii ) , str ( url ) , 100009 , str ( iiIi1IIiI ) , O0o0Oo , '' , '' )
  I1I11i ( 'movies' , '' )
  if 16 - 16: iI11I1II1I1I - I1111IIi
  if 88 - 88: ii
  if 84 - 84: OOooOOo / ooOOOoO * O0OOOoOoo0 / o000O0o - Ii . I1ii11iIi11i
  if 60 - 60: Ii1I * oOo0O0Ooo
def I1iIiI11I1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 OOOoO000 = re . compile ( '<a href="(.+?)" target="_blank"><img src="(.+?)" style="max-width:200px;" /><description = "(.+?)" /><background = "(.+?)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for url , ii1iii1i , i1oO0OO0 , I11iiiiI1i , Iii1I1111ii in OOOoO000 :
  if '.php' in url :
   iiOOooooO0Oo ( Iii1I1111ii , url , 100210 , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
  else :
   OOiIiIIi1 ( Iii1I1111ii , url , 222 , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
   if 27 - 27: ii1ii11IIIiiI . Ii % iiiiiiii1
   if 65 - 65: IIiIiII11i . oOo0O0Ooo % o000O0o * oO0o
   if 38 - 38: OOooOOo / O0OOOoOoo0 % I1ii11iIi11i
def I1IIIiii1 ( iconimage , url , extra ) :
 iiIi1IIiI = ' '
 O00oo = ' '
 I11iiiiI1i = ' '
 O0OO00O0oOO = ' '
 Ii1iI111 = IiiI1iiiiI1iI ( url )
 iiIi1IIiI = re . compile ( '<img src="(.+?)">' ) . findall ( Ii1iI111 )
 for iiIi1IIiI in iiIi1IIiI :
  iiIi1IIiI = iiIi1IIiI
 O0oooo00o0Oo = re . compile ( 'style="background-image: url\((.+?)\)">' ) . findall ( Ii1iI111 )
 for I11iiiiI1i in O0oooo00o0Oo :
  I11iiiiI1i = I11iiiiI1i
 i1IIIII11I1IiI = re . compile ( 'itemprop="season".+?href=".+?" href="(.+?)".+?aria-hidden=".+?"></i>.+?S(.+?)</span>' , re . DOTALL ) . findall ( Ii1iI111 )
 for url , O0OO00O0oOO in i1IIIII11I1IiI :
  O0OO00O0oOO = 'S' + ( O0OO00O0oOO ) . replace ( '  ' , '' ) . replace ( '\n' , '' ) . replace ( '    ' , '' ) . replace ( '	' , '' )
  url = oO0Oo + url
  I1iii ( ( O0OO00O0oOO ) . replace ( '  ' , '' ) , url , 100101 , iiIi1IIiI , I11iiiiI1i , O00oo , '' )
  I1I11i ( 'Movies' , 'info' )
  if 86 - 86: Ii1I * o0o00Oo0O * I1111IIi
def Ooo0oo ( url , name , fanart , extra , iconimage ) :
 IIi11IIiIii1 = extra
 O0OO00O0oOO = name
 Ii1iI111 = IiiI1iiiiI1iI ( url )
 iiIi1IIiI = iconimage
 i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="(.+?)">.+?<span class="" itemprop="name">(.+?)</span>.+?<span itemprop="datepublished">(.+?)</span></span>.+?</li>' , re . DOTALL ) . findall ( Ii1iI111 )
 for url , name , I1iIII1 in i1IIIII11I1IiI :
  name = ( name ) . replace ( '&nbsp;' , '-' ) . replace ( '---' , ' - ' ) . replace ( '&#039;' , '\'' ) . replace ( '&amp;' , '&' ) . replace ( '&quot;' , '"' )
  url = oO0Oo + url
  I1iIII1 = I1iIII1
  iIii = name + ' - [COLORred]' + I1iIII1 + '[/COLOR]'
  I1iii ( iIii , url , 100102 , iiIi1IIiI , fanart , 'Aired : ' + I1iIII1 , iIii )
  if 84 - 84: o000O0o % ooOoO0O00
def oOO ( name , URL , iconimage , fanart ) :
 oO0OOoo0OO = IiiI1iiiiI1iI ( URL )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)".+?height="16px">(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , name in i1IIIII11I1IiI :
  for IiiiiI1i1Iii in oOOoo0Oo :
   if IiiiiI1i1Iii in oOooO0 :
    URL = 'http://www.watchseriesgo.to/link/' + oOooO0
    o0O0Oo00 ( name , URL , 100106 , III1iII1I1ii + 'appstreams.png' , O0o0Oo , '' , '' )
 if len ( i1IIIII11I1IiI ) <= 0 :
  I1iii ( '[COLORred]NO STREAMS AVAILABLE[/COLOR]' , '' , '' , '' , '' , '' , '' )
  if 17 - 17: IIiIiII11i / Ii1I % I1111IIi + oOo0O0Ooo * iiiiiiii1
  if 36 - 36: iiiiiiii1 * oO0o
def I1I ( url , name ) :
 ii1iIi1II = name
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe style=.+?" src="(.+?)"' ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<IFRAME SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 iiI1IIIi = re . compile ( '<IFRAME style=".+?" SRC="(.+?)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  IIIIi1I ( url , ii1iIi1II )
 for url in i1I :
  IIIIi1I ( url , ii1iIi1II )
 for url in iiI1IIIi :
  IIIIi1I ( url , ii1iIi1II )
  if 31 - 31: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I % ooOOOoO
def IIIIi1I ( url , season_name ) :
 if 'daclips.in' in url :
  iii ( url , season_name )
 elif 'filehoot.com' in url :
  I1ii ( url , season_name )
 elif 'allmyvideos.net' in url :
  iii1111iiI1ii ( url , season_name )
 elif 'vidspot.net' in url :
  IIiii ( url , season_name )
 elif 'vodlocker' in url :
  I1i1i ( url , season_name )
 elif 'vidto' in url :
  OOOOooO0oO00O0o ( url , season_name )
  if 70 - 70: iiiiiiii1
  if 16 - 16: O0OOOoOoo0 - ii % I1ii11iIi11i
def OOOOooO0oO00O0o ( url , season_name ) :
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i11i1iIiii , Iii1I1111ii in i1IIIII11I1IiI :
  OOO00OO0oOo ( i11i1iIiii , season_name )
  if 35 - 35: O0OOOoOoo0 + I11i1ii1 - o000O0o . O0OOOoOoo0 . I1111IIi
  if 87 - 87: OOooOOo
def iii1111iiI1ii ( url , season_name ) :
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i11i1iIiii , Iii1I1111ii in i1IIIII11I1IiI :
  OOO00OO0oOo ( i11i1iIiii , season_name )
  if 25 - 25: ooOoO0O00 . oO0o - OOooOOo / oO0o % oO0o * iI11I1II1I1I
def IIiii ( url , season_name ) :
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 i1IIIII11I1IiI = re . compile ( '"file" : "(.+?)",\n.+?"default" : .+?,\n.+?"label" : "(.+?)"' ) . findall ( oO0OOoo0OO )
 for i11i1iIiii , Iii1I1111ii in i1IIIII11I1IiI :
  OOO00OO0oOo ( i11i1iIiii , season_name )
  if 50 - 50: oO0o . Ii - o000O0o . o000O0o
def I1i1i ( url , season_name ) :
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i11i1iIiii in i1IIIII11I1IiI :
  OOO00OO0oOo ( i11i1iIiii , season_name )
  if 31 - 31: Ii1IIIi1 / I1ii11iIi11i * ooOoO0O00 . OOooOOo
def iii ( url , season_name ) :
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 i1IIIII11I1IiI = re . compile ( '{ file: "(.+?)", type:"video" }' ) . findall ( oO0OOoo0OO )
 for i11i1iIiii in i1IIIII11I1IiI :
  OOO00OO0oOo ( i11i1iIiii , season_name )
  if 57 - 57: Ii1IIIi1 + iI11I1II1I1I % ooOoO0O00 % oOo0O0Ooo
def I1ii ( url , season_name ) :
 oO0OOoo0OO = IiiI1iiiiI1iI ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "(.+?)",.+?skin' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i11i1iIiii in i1IIIII11I1IiI :
  OOO00OO0oOo ( i11i1iIiii , season_name )
  if 83 - 83: I11i / Ii % iI11I1II1I1I . ooOOOoO % o000O0o . ii
def OOO00OO0oOo ( Link , season_name ) :
 if 'http:/' in Link :
  o00oO00 ( Link )
  if 59 - 59: Ii1IIIi1 + iI11I1II1I1I * I11i + iiiiiiii1 . O0OOOoOoo0
def IiI1iII1II111 ( url ) :
 oO0OOoo0OO = OPEN_URL_1 ( url )
 IIiI11i1111Ii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 for url in IIiI11i1111Ii :
  Resolve_2 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 63 - 63: Ii1IIIi1 + I11i1ii1
def I1iii ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0ooOOO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii11Iii1i1ii = True
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1i1111 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o0oO0O00oOo = [ ]
  if 26 - 26: I1111IIi % iiiiiiii1 % o000O0o % ii1ii11IIIiiI
  if showcontext == 'fav' :
   o0oO0O00oOo . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o0oO0O00oOo . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ii1i1i1111 . addContextMenuItems ( o0oO0O00oOo )
 Ii11Iii1i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = True )
 return Ii11Iii1i1ii
 if 55 - 55: I11i1ii1 % ii / ii % ii
 if 52 - 52: Ii1I + Ii1I . IIiIiII11i
def o0O0Oo00 ( name , url , mode , iconimage , fanart , description , extra , showcontext = True , allinfo = { } ) :
 O0ooOOO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii11Iii1i1ii = True
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1i1111 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o0oO0O00oOo = [ ]
  o0oO0O00oOo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o0oO0O00oOo . append ( ( 'Remove from abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=105&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o0oO0O00oOo . append ( ( 'Add to abracadabra Favorites' , 'XBMC.RunPlugin(%s?mode=104&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ii1i1i1111 . addContextMenuItems ( o0oO0O00oOo )
 Ii11Iii1i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = False )
 return Ii11Iii1i1ii
 if 34 - 34: ii . o0o00Oo0O / o000O0o * OOooOOo - Ii1I
def IiiiI ( ) :
 return xbmc . executebuiltin ( 'Action(Queue)' )
 if 42 - 42: ooOoO0O00 . oOo0O0Ooo / ooOoO0O00 + ii1ii11IIIiiI
def O0o0O0OO00o ( url ) :
 OOo00O = xbmc . Player ( o0Ii1Iii111IiI1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : OOo00O . play ( url ) . strip ( )
 except : pass
 if 98 - 98: iiiiiiii1 - ii % oOo0O0Ooo + o0o00Oo0O . ii1ii11IIIiiI
def o00oO00 ( url ) :
 OOo00O = xbmc . Player ( )
 import urlresolver
 try : OOo00O . play ( url )
 except : pass
 if 56 - 56: IIiIiII11i / o000O0o + Ii + Ii1IIIi1
def IiiI1iiiiI1iI ( url ) :
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
  if 54 - 54: ii1ii11IIIiiI - ooOOOoO - iiiiiiii1 . iI11I1II1I1I
  if 79 - 79: ii1ii11IIIiiI . oO0o
  if 40 - 40: I11i + I1ii11iIi11i . I11i % I11i1ii1
def OOOOO0O00 ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']WATCH CARTOONS ONLINE[/COLOR]' , '[COLOR' + II + ']CARTOONS[/COLOR]' , '[COLOR' + II + ']MORE CARTOONS[/COLOR]' , '[COLOR' + II + ']ANIME LAND[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Kids[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   I11I1IIiiII1 ( )
  if iI11iI1IiiIiI == 1 :
   IIIIIii1ii11 ( )
  if iI11iI1IiiIiI == 2 :
   OOOooo0OooOoO ( )
  if iI11iI1IiiIiI == 3 :
   oOoOOOo ( )
  if iI11iI1IiiIiI == 4 :
   ii1I ( ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2R1YmJlZC1hbmltZQ==' ) ) )
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
def iIIiIiI1I1 ( ) :
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
 if 85 - 85: ooOOOoO
 if 88 - 88: oOo0O0Ooo + ii - o000O0o
 if 85 - 85: I11i . I1111IIi / o0o00Oo0O . I11i . Ii1I . oO0o
def OO ( ) :
 oO0OOoo0OO = OoOooO ( 'http://genietv.co.uk/genietv_art/testdelete.txt' )
 i1IIIII11I1IiI = re . compile ( '<unwanted_addon =(.+?)</unwanted_addon>' ) . findall ( oO0OOoo0OO )
 for IIiIi1iI in i1IIIII11I1IiI :
  IIiIi1iI = ( str ( IIiIi1iI ) )
  if os . path . exists ( xbmc . translatePath ( IIiIi1iI ) ) :
   OO0O0Oo0 = ( IIiIi1iI ) . replace ( 'special://home/addons/' , '' )
   iiIiI1i1 ( "Please remove any addons or repo's that may alter Genie Tv coding without your knowledge" , "It has been recognised you have \n[COLORred]" + OO0O0Oo0 + "[/COLOR]\n installed on your system. In order for genie to function this addon must be removed. \n\nThere have been 'creative differences' between ourselves and this addon. Initially we just stopped our addon from working if this addon was installed, but when private talks were undertaken the 'author' (we use this term very lightly) of this addon gave us a choice, either remove our block or they will tamper with our addon, they then saw fit to host our addon and begin pushing unwanted and unauthorised, potentially malicious updates (we've no idea what they altered and with there approach anything could be possible) so we took steps to remove this addon purely for your protection from alterations to code from, self confessed, unskilled individuals. \n\nHowever the approach we took i guess can be seen as malicious because we did not inform you of actions that altered your device without your knowledge (bar a popup telling you this was happening), for this we apologise, it was a major oversight on our part and made us no better than them. \n\nAll are free to continue to use genie tv at no cost but you must make a decision. A box will soon open and you will need to choose remove or close. If you choose remove you are accepting to remove these addons that we believe have the potential to maliciously alter your device from an unofficial source or if you press close it will close genie, it will not be useable until these addons are remove and you can chose to use whatever addon you see fit at your own risk. \n\nThis is not 'playing god' please dont see it that way but merely protecting our hard work and in the end your experience from this.  We hope this issue resolves itself and things return to normality as much as, if not more than, yourself. Please wait to decide what action you wish to take" )
   xbmc . sleep ( 40000 )
   iI11iI1IiiIiI = xbmcgui . Dialog ( ) . yesno ( 'Remove Potentially Harmful Addons' , 'Remove will remove addons known to alter genie tv' , 'Close will stop genie tv working to protect' , 'you from any potential unwanted updates' , nolabel = 'Close' , yeslabel = 'Remove' )
   if iI11iI1IiiIiI == 0 :
    oOOOO00 ( IIiIi1iI )
    oOOo0O00o ( )
   elif iI11iI1IiiIiI == 1 :
    oOo0O00O ( IIiIi1iI )
  else :
   pass
   if 36 - 36: o0o00Oo0O + I1ii11iIi11i
def oOo0O00O ( addon ) :
 OO0O0Oo0 = ( addon ) . replace ( 'special://home/addons/' , '' )
 o0oOoO00o . create ( "[COLOR=white]The addons are being removed as requested[/COLOR]" , 'Please enjoy Genie Tv and we thank you for your support' , '[COLORyellow]Hopefully this may end soon and peace is restored[/COLOR]' )
 xbmc . sleep ( 3000 )
 addon = xbmc . translatePath ( str ( addon ) )
 shutil . rmtree ( addon , ignore_errors = True )
 o0oOoO00o . update ( 100 , "" , "Your Device is now clean" )
 xbmc . sleep ( 1000 )
 o0oOoO00o . close ( )
 if 5 - 5: I1ii11iIi11i * OOooOOo
def oOOOO00 ( addon ) :
 OOooO0OOoo . ok ( "[COLOR=white]Incompatible[/COLOR]" , "Unfortunately GenieTv will not work with" , addon , 'please remove then reinstall genie' )
 ii1I11iIiIII1 = os . path . join ( I11II1i , 'default.py' )
 oOO0OOOOoooO = open ( ii1I11iIiIII1 , "w+" )
 if 22 - 22: ooOOOoO + iI11I1II1I1I
 oOO0OOOOoooO . write ( r'Genie Tv will not work with certain addons in an attempt to bring you original content from the best developers' )
 oOO0OOOOoooO . write ( r'and not those simply out to profit or make a name for themselves off others work' )
 oOO0OOOOoooO . write ( r'Please remove' + unwanted_addons + 'if you would like to use genie tv then uninstall and reinstall from official repo' )
 if 24 - 24: OOooOOo % ooOoO0O00 + O0OOOoOoo0 . Ii . Ii1I
 if 17 - 17: Ii1I . IIiIiII11i . I11i1ii1 / Ii1I
 if 57 - 57: ooOOOoO
 if 67 - 67: oO0o . I11i1ii1
def i11i1iiiII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 oO00oOo0OOO = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<name>(.+?)</name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 ii1ooO = re . compile ( '<name>(.+?)<name>\n<thumbnail>(.+?)</thumbnail>\n<externallink>(.+?)</externallink>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<title>(.+?)</title>\n<link>(.+?)</link>\n<thumbnail>(.+?)</thumbnail>\n<fanart>(.+?)</fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iiI1IIIi = re . compile ( '<title>(.+?)<title>\n<link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iiIiIIIiiI = re . compile ( '<title>(.+?)<title>\n<Link>(.+?)<link>\n<thumbnail>(.+?)<thumbnail>\n<fanart>(.+?)<fanart>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oOoOoO000OO = re . compile ( '<title>(.+?)</title><link>(.+?)</link><thumbnail>(.+?)</thumbnail>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , url , ooOoOo0 , I11iiiiI1i , i1oO0OO0 in oO00oOo0OOO :
  if 'php' in url :
   iiOOooooO0Oo ( Iii1I1111ii , url , 90037 , ooOoOo0 , I11iiiiI1i , i1oO0OO0 )
  elif Iii1I1111ii == 'Search' :
   iiOOooooO0Oo ( 'Search' , url , 90038 , ooOoOo0 , I11iiiiI1i , i1oO0OO0 )
  else :
   OOiIiIIi1 ( Iii1I1111ii , url , 222 , ooOoOo0 , I11iiiiI1i , i1oO0OO0 )
 for Iii1I1111ii , ii1iii1i , url , ii11II11 in ii1ooO :
  iiOOooooO0Oo ( Iii1I1111ii , url , 90037 , ii1iii1i , ii11II11 , '' )
 for Iii1I1111ii , ii1iii1i , url , ii11II11 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 90037 , ii1iii1i , ii11II11 , '' )
 for Iii1I1111ii , url , ii1iii1i , ii11II11 in i1I :
  OOiIiIIi1 ( Iii1I1111ii , url , 222 , ii1iii1i , ii11II11 , '' )
 for Iii1I1111ii , url , ii1iii1i , ii11II11 in iiI1IIIi :
  OOiIiIIi1 ( Iii1I1111ii , url , 222 , ii1iii1i , ii11II11 , '' )
 for Iii1I1111ii , url , ii1iii1i , ii11II11 in iiIiIIIiiI :
  OOiIiIIi1 ( Iii1I1111ii , url , 222 , ii1iii1i , ii11II11 , '' )
 for Iii1I1111ii , url , ii1iii1i in oOoOoO000OO :
  OOiIiIIi1 ( Iii1I1111ii , url , 222 , ii1iii1i , '' , '' )
  I1I11i ( 'tvshows' , 'Media Info 3' )
  if 70 - 70: iI11I1II1I1I
def ii1Ii11IiiI1 ( ) :
 iIi = [ 'serialsearch' , 'moviesearch' ]
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 if iiiI111I == '' :
  pass
 else :
  for oooOOO00o0 in iIi :
   i1Iii = I11 + oooOOO00o0 + '.php'
   Ii1iI111 = OoOooO ( i1Iii )
   if Ii1iI111 != 'Opened' :
    OOOoO000 = re . compile ( '<NAME>(.+?)</NAME><URL>(.+?)</URL><ICON>(.+?)</ICON><FANART>(.+?)</FANART><DESC>(.+?)</DESC>' ) . findall ( Ii1iI111 )
    for Iii1I1111ii , oOooO0 , ooOoOo0 , I11iiiiI1i , i1oO0OO0 in OOOoO000 :
     if iiiI111I in Iii1I1111ii . lower ( ) :
      II1I11IIi = re . compile ( 'item="(.+?)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for IiiiiI1i1Iii in II1I11IIi :
       if IiiiiI1i1Iii == oOooO0 :
        Iii1I1111ii = '[COLORred]* [/COLOR]' + ( Iii1I1111ii ) . replace ( '[COLORred]* [/COLOR][COLORred]* [/COLOR]' , '[COLORred]* [/COLOR]' )
        OoOOo = open ( o00OO00OoO , "a" )
        OoOOo . write ( 'item="' + Iii1I1111ii + '"\n' )
        OoOOo . close
      if 'php' in oOooO0 :
       iiOOooooO0Oo ( Iii1I1111ii , oOooO0 , 90037 , ooOoOo0 , I11iiiiI1i , i1oO0OO0 )
      else :
       OOiIiIIi1 ( Iii1I1111ii , oOooO0 , 222 , ooOoOo0 , I11iiiiI1i , i1oO0OO0 )
       if 17 - 17: ooOoO0O00
   I1I11i ( 'tvshows' , 'Media Info 3' )
   if 1 - 1: I11i1ii1
def oOO0oo ( ) :
 oO0OOoo0OO = OoOooO ( 'http://www.tvcatchup.com/channels/' )
 O0 = OoOooO ( 'http://www.djing.com/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img style="" src="([^"]*)" alt="([^"]*)"/>.+?<br/>(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 II1iIi1IiIii = re . compile ( 'title="([^"]*)".+?<a href="([^"]*)" >.+?<img style="" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( 'href="([^"]*)">.+?src="([^"]*)".+?pad pad-top-minus pad-bottom-minus">(.+?)</h2>' , re . DOTALL ) . findall ( O0 )
 for oOooO0 , ii1iii1i , I111I11I111 , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( ( '[COLORgold]' + I111I11I111 + '[/COLOR][COLORwhite] - [COLORsteelblue]' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#039;' , '' ) . replace ( '&amp;' , '&' ) , 'http://www.tvcatchup.com' + oOooO0 , 90024 , ii1iii1i )
 for IIiiiiiiIi1I1 , oOooO0 , ii1iii1i in II1iIi1IiIii :
  ii1ii111 ( IIiiiiiiIi1I1 , 'http://www.tvcatchup.com' + oOooO0 , 90024 , ii1iii1i )
 for oOooO0 , ii1iii1i , Iii1I1111ii in i1I :
  if 'Submit' in Iii1I1111ii :
   pass
  elif '&lt;' in Iii1I1111ii :
   pass
  else :
   OOiIiIIi1 ( '[COLORgold]DJing  [/COLOR][COLORwhite]- [COLORsteelblue]' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 90025 , 'http://www.djing.com' + ii1iii1i , O0o0Oo , '' )
  I1I11i ( 'movies' , 'MAIN' )
def iiiiI11ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 if 96 - 96: O0OOOoOoo0 . o0o00Oo0O / O0OOOoOoo0 % o0o00Oo0O
 i1IIIII11I1IiI = re . compile ( "file: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOoOO0o ( url )
def o0o000 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<iframe src='([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  i1iiiIii11 ( ( url ) . replace ( 'http://djing.com/embed/?url=' , '' ) )
  if 67 - 67: I11i % OOooOOo . OOooOOo - I11i1ii1
def OOoOOO0 ( ) :
 if 90 - 90: I11i1ii1 + IIiIiII11i * Ii1I / ii1ii11IIIiiI . I11i + I11i
 if 40 - 40: I11i1ii1 / OOooOOo % Ii % Ii1I / oOo0O0Ooo
 if 62 - 62: ooOoO0O00 - OOooOOo
 if 62 - 62: ooOoO0O00 + I1ii11iIi11i % I1111IIi
 if 28 - 28: Ii1I . ooOoO0O00
 if 10 - 10: oO0o / I1ii11iIi11i
 oO0OOoo0OO = cloudflare . source ( 'http://www.boxofficemojo.com/yearly/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'yr' in oOooO0 :
   O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.boxofficemojo.com/yearly/' + oOooO0 , 10201 , III1iII1I1ii + 'rated.png' )
   if 15 - 15: O0OOOoOoo0 . OOooOOo / O0OOOoOoo0 * ooOOOoO - oOo0O0Ooo % Ii1I
def oo0OOOOOO0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'bgcolor=".+?"><td align=".+?"><font size="2">(.+?)</.+?<a href="([^"]*)">(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for i11Ii1I1I11I , url , Iii1I1111ii in i1IIIII11I1IiI :
  if 'id' in url :
   O0Oo00OoOo ( ( '[COLORred]RANK [COLORblue]' + i11Ii1I1I11I + '[COLORred] - [COLORblue]' + Iii1I1111ii + '[/COLOR]' ) , Iii1I1111ii , 10202 , III1iII1I1ii + 'rated.png' )
   if 29 - 29: ii . oOo0O0Ooo % Ii1I - O0OOOoOoo0
def iiii ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0OO0Oo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oo00O0 = ( url )
 iiiI111I = oo00O0 . lower ( )
 url = 'http://onlinemovies.tube/?s=' + ( oo00O0 ) . replace ( ' ' , '+' )
 I11iiii1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 iiiiI1iiiIi = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 o0oO0OoO0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 oOOOOOoOO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oooo00 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1oO = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oo00O0
 iI = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 Ii1IIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 43 - 43: iiiiiiii1 % O0OOOoOoo0
 o0O0ooOOoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 iIi11ii = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 50 - 50: ii1ii11IIIiiI / OOooOOo * ii1ii11IIIiiI
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( url )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( I11iiii1I )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( iiiiI1iiiIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( o0oO0OoO0 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 Ii1iIi111i1i1 = O0o0O00Oo0o0 ( oOOOOOoOO )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IIOO0ooOo0OoOo0 = O0o0O00Oo0o0 ( i1oO )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOo = O0o0O00Oo0o0 ( iI )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 i1iIIIiiiI = O0o0O00Oo0o0 ( Ii1IIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 94 - 94: o0o00Oo0O - ooOOOoO - iI11I1II1I1I % I11i1ii1 / ii1ii11IIIiiI % O0OOOoOoo0
 if 44 - 44: I1ii11iIi11i % iI11I1II1I1I
 oo0ooO0 = O0o0O00Oo0o0 ( o0O0ooOOoO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 IIiiiiIiIIii = O0o0O00Oo0o0 ( iIi11ii )
 if 86 - 86: ooOOOoO / I11i - I11i + Ii1I + o000O0o
 if 33 - 33: I11i . O0OOOoOoo0 . I1111IIi . ooOoO0O00
 if 49 - 49: Ii1I
 if 84 - 84: ooOOOoO - I1ii11iIi11i / o0o00Oo0O - iiiiiiii1
 if 21 - 21: o0o00Oo0O * o0o00Oo0O % Ii1I
 if 94 - 94: ooOOOoO + IIiIiII11i % Ii
 if 8 - 8: I11i1ii1 * o0o00Oo0O
 if 73 - 73: I11i / o000O0o / ooOOOoO / oO0o
 if 11 - 11: OOooOOo + I1111IIi - ii / oO0o
 if 34 - 34: I11i1ii1
 if 45 - 45: I11i1ii1 / I1ii11iIi11i / ii1ii11IIIiiI
 if 44 - 44: Ii1I - ii1ii11IIIiiI / IIiIiII11i * oO0o * I1ii11iIi11i
 if 73 - 73: I11i - oOo0O0Ooo * ooOoO0O00 / Ii * Ii1IIIi1 % IIiIiII11i
 if i1iIIIiiiI != 'Failed' :
  OooOoOOo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iIIIiiiI )
  for url , Iii1I1111ii in OooOoOOo0oO00 :
   O00O = O0o0O00Oo0o0 ( url )
   O0Ooo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( O00O )
   for oO00oOOo0Oo , IIi in O0Ooo :
    IIi = ( IIi . replace ( '.' , ' ' ) )
    if iiiI111I in IIi . lower ( ) :
     if '.mkv' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , url + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.mp4' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , url + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.avi' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , url + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.wav' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , url + oO00oOOo0Oo , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , url + oO00oOOo0Oo , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 6 - 6: oO0o + I11i - IIiIiII11i / iI11I1II1I1I + o0o00Oo0O
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for url , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in i1I :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORred] source Technica[/COLOR]' ) , url , 222 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 58 - 58: I1ii11iIi11i
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 9 - 9: iI11I1II1I1I % Ii1I . Ii1IIIi1 + ii
 if ii1ii1ii != 'Failed' :
  iiI1IIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for Oo0o , Iii1I1111ii in iiI1IIIi :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiiiI1iiiIi + Oo0o ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  iiIiIIIiiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for url , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in iiIiIIIiiI :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORred] source RaizTv[/COLOR]' ) , url , 222 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 93 - 93: Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if Ii1iIi111i1i1 != 'Failed' :
  iIii1Ooo0oO0 = [ ]
  oOoOoO000OO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1iIi111i1i1 )
  for url , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in oOoOoO000OO :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    if Iii1I1111ii in iIii1Ooo0oO0 :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , url , 1016 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
     iIii1Ooo0oO0 . append ( Iii1I1111ii )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if IIOO0ooOo0OoOo0 != 'Failed' :
  o0Oo0oOooOoOo = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIOO0ooOo0OoOo0 )
  for url , ii1iii1i , Iii1I1111ii in o0Oo0oOooOoOo :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + url , 7067 , ii1iii1i )
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
 if oo0ooO0 != 'Failed' :
  oOoO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0ooO0 )
  for url , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in oOoO0o :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source APPRENTICE[/COLOR]' ) , url , 222 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
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
 for oooOOO00o0 in iiIIii :
  i1Iii = O0Oo000ooO00 + oooOOO00o0 + I1IIIii
  i1iIIIiiiI = O0o0O00Oo0o0 ( i1Iii )
  if i1iIIIiiiI != 'Failed' :
   OooOoOOo0oO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIIiiiI )
   for url , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in OooOoOOo0oO00 :
    if oo00O0 in Iii1I1111ii . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgold] - Source Pandoras[/COLOR]' , url , 222 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 62 - 62: ooOOOoO
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 63 - 63: Ii1IIIi1 + I11i1ii1 * o000O0o / I11i / I1ii11iIi11i * iI11I1II1I1I
 iiIIii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 57 - 57: OOooOOo - o000O0o / I11i1ii1 % Ii
 if 3 - 3: O0OOOoOoo0 . I11i1ii1 % oOo0O0Ooo + Ii1I
 for oooOOO00o0 in iiIIii :
  i1Iii = o0OO0Oo + oooOOO00o0
  oo0o = O0o0O00Oo0o0 ( i1Iii )
  if oo0o != 'Failed' :
   o0IiiiI111I = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0o )
   for Oo0o , Iii1I1111ii in o0IiiiI111I :
    if oo00O0 in Iii1I1111ii . lower ( ) :
     ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o0OO0Oo + oooOOO00o0 + Oo0o ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 49 - 49: I11i * ii1ii11IIIiiI + ooOOOoO + O0OOOoOoo0
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 30 - 30: I11i / Ii1IIIi1 / I1111IIi % I11i1ii1 + IIiIiII11i
def oO00oo0o00o0o ( ) :
 O0Oo00OoOo ( 'RUNNING' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3J1bm5pbmc9MQ==' ) , 10096 , III1iII1I1ii + 'running.png' )
 O0Oo00OoOo ( 'COUNTDOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NvdW50ZG93bj0x' ) , 10096 , III1iII1I1ii + 'countdown.png' )
 O0Oo00OoOo ( 'UNKNOWN' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP3Vua25vd249MQ==' ) , 10097 , III1iII1I1ii + 'unknown.png' )
 O0Oo00OoOo ( 'CANCELLED' , i11 ( 'aHR0cDovL3d3dy5yZXR1cm5kYXRlcy5jb20vaW5kZXgucGhwP2NhbmNlbGVkPTE=' ) , 10098 , III1iII1I1ii + 'cancelled.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 4 - 4: O0OOOoOoo0 - I1ii11iIi11i - I1111IIi - ooOOOoO % Ii / oO0o
def i1iii11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , O0OO00O0oOO , oOo0O0o0000o0O0 , I1iIII1 , o0OoOoOOoOo0o in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLORblue]' + Iii1I1111ii + '[/COLOR] [COLORred]Season[/COLOR]-' + O0OO00O0oOO + ' [COLORred]Returns [/COLOR]- ' + o0OoOoOOoOo0o + ' ' + I1iIII1 ) , Iii1I1111ii , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 20 - 20: oO0o / iI11I1II1I1I
def iIooo0oo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4></font></td><td></td><td><font size=4><a' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , O0OO00O0oOO , oOo0O0o0000o0O0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLORblue]' + Iii1I1111ii + '[/COLOR] [COLORred]Season[/COLOR]-' + O0OO00O0oOO + ' [COLORred] Status Unknown[/COLOR] ' ) , Iii1I1111ii , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 8 - 8: oO0o + OOooOOo . iI11I1II1I1I % o0o00Oo0O
def iI11Ii111 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '></td><td><font size=4>(.+?)</font.+?/td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td><font size=4>(.+?)</font></td><td></td><td><font size=4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , O0OO00O0oOO , oOo0O0o0000o0O0 , I1iIII1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLORblue]' + Iii1I1111ii + ' [COLORred] Cancelled On[/COLOR] ' + I1iIII1 ) , Iii1I1111ii , 10099 , III1iII1I1ii + 'seasons.png' )
  xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
  if 54 - 54: OOooOOo % O0OOOoOoo0 . OOooOOo * Ii1IIIi1 + OOooOOo % ooOoO0O00
def I1I1I11Ii ( url ) :
 oo00O0 = ( url )
 iiiI111I = oo00O0 . lower ( )
 if 48 - 48: ii + o000O0o % iI11I1II1I1I
 if 11 - 11: oOo0O0Ooo % ii1ii11IIIiiI - oO0o - o000O0o + I11i
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( oo00O0 ) . replace ( ' ' , '+' )
 I11iiii1I = 'http://onlinemovies.tube/?s=' + ( oo00O0 ) . replace ( ' ' , '+' )
 iiiiI1iiiIi = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 o0oO0OoO0 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oooo00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 98 - 98: O0OOOoOoo0 + ii1ii11IIIiiI - oO0o
 iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 Ii1IIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 OOo0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsdHYucGhw' ) )
 if 58 - 58: OOooOOo - O0OOOoOoo0 - ii
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 96 - 96: iI11I1II1I1I
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 82 - 82: OOooOOo + o0o00Oo0O - I1111IIi % o000O0o * Ii
 if 15 - 15: I11i
 o0O00Oo0 = O0o0O00Oo0o0 ( oO00oOOo0Oo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( I11iiii1I )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( iiiiI1iiiIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( o0oO0OoO0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 oo0o = O0o0O00Oo0o0 ( oooo00 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 39 - 39: Ii1IIIi1 / Ii1I / oOo0O0Ooo * iiiiiiii1
 if 44 - 44: o0o00Oo0O + I11i1ii1 . iI11I1II1I1I + I1ii11iIi11i / o0o00Oo0O - ooOOOoO
 oOo = O0o0O00Oo0o0 ( iI )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 i1iIIIiiiI = O0o0O00Oo0o0 ( Ii1IIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 o0o0OoOOOOOo = O0o0O00Oo0o0 ( OOo0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source 11/11 Links" )
 if 39 - 39: ii * Ii1IIIi1 * o0o00Oo0O . ooOOOoO . oO0o + I11i1ii1
 if i1iIIIiiiI != 'Failed' :
  OooOoOOo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iIIIiiiI )
  for url , Iii1I1111ii in OooOoOOo0oO00 :
   O00O = O0o0O00Oo0o0 ( url )
   O0Ooo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( O00O )
   for oO00oOOo0Oo , IIi in O0Ooo :
    if iiiI111I in IIi . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , url + oO00oOOo0Oo , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 9 - 9: OOooOOo + o000O0o % ii + I11i
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if oOo != 'Failed' :
  ooOO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo )
  for url , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in ooOO0o :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source HeroVision[/COLOR]' ) , url , 1016 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 51 - 51: I1ii11iIi11i - Ii1I * ooOOOoO
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 12 - 12: iI11I1II1I1I % I11i1ii1 % I11i1ii1
    if 78 - 78: I1111IIi . OOooOOo . ooOOOoO
    if 97 - 97: o000O0o
    if 80 - 80: oOo0O0Ooo . ii1ii11IIIiiI
    if 47 - 47: ooOOOoO + I11i1ii1 + IIiIiII11i % Ii
    if 93 - 93: Ii1I % OOooOOo . o0o00Oo0O / O0OOOoOoo0 * o000O0o
    if 29 - 29: I11i
    if 86 - 86: IIiIiII11i . I1111IIi
    if 2 - 2: ii
    if 60 - 60: oO0o
    if 81 - 81: OOooOOo % ii1ii11IIIiiI
 if o0o0OoOOOOOo != 'Failed' :
  oo0 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( o0o0OoOOOOOo )
  for url , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in oo0 :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORred] RaizTv[/COLOR]' , url , 1016 , iII1iii )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 30 , "" , "Getting RaizTv Links" )
    if 16 - 16: ii1ii11IIIiiI * oO0o / o000O0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  II1iiI = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for url , ii1iii1i , Iii1I1111ii , III1Ii1i1I1 in i1I :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    if 'season' in III1Ii1i1I1 :
     O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90054 , ii1iii1i , ii1iii1i , '' )
    if 'episodes' in III1Ii1i1I1 :
     O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + ' - [COLORred]Source - Tv HUB[/COLOR]' , url , 90044 , ii1iii1i , ii1iii1i , '' )
  for url in II1iiI :
   O0Oo00OoOo ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , url , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 97 - 97: iiiiiiii1 . I11i1ii1 - iiiiiiii1 + oOo0O0Ooo * IIiIiII11i
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if o0O00Oo0 != 'Failed' :
  ii1ooO = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( o0O00Oo0 )
  for url , Iii1I1111ii , ii1iii1i in ii1ooO :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( Iii1I1111ii ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , url , 8022 , ii1iii1i , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 10 - 10: ii1ii11IIIiiI + ooOOOoO % ii - oOo0O0Ooo
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 70 - 70: Ii1IIIi1 - O0OOOoOoo0
    if 2 - 2: iI11I1II1I1I
    if 45 - 45: ii / Ii
    if 10 - 10: O0OOOoOoo0 - o000O0o * iI11I1II1I1I % iI11I1II1I1I * I1111IIi - Ii1I
    if 97 - 97: IIiIiII11i % iiiiiiii1 + iiiiiiii1 - oO0o / ii1ii11IIIiiI * oOo0O0Ooo
    if 17 - 17: ii1ii11IIIiiI
    if 39 - 39: I11i1ii1 . IIiIiII11i
    if 45 - 45: o000O0o * OOooOOo / iI11I1II1I1I
    if 77 - 77: iiiiiiii1 - ooOOOoO
 if ii1ii1ii != 'Failed' :
  iiI1IIIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for Iii1I1111ii in iiI1IIIi :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iiiiI1iiiIi + Iii1I1111ii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 11 - 11: Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  iiIiIIIiiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for Iii1I1111ii in iiIiIIIiiI :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( o0oO0OoO0 + Iii1I1111ii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 26 - 26: iI11I1II1I1I * iiiiiiii1 - Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  o0IiiiI111I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0o )
  for url , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in o0IiiiI111I :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] Source Scooby[/COLOR]' ) , url , 1016 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 27 - 27: Ii1I * iiiiiiii1 - oO0o + ii1ii11IIIiiI * ii1ii11IIIiiI
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 55 - 55: I11i1ii1
 o0O0OO0o = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oooOOO00o0 in o0O0OO0o :
  i1Iii = O0Oo000ooO00 + oooOOO00o0 + I1IIIii
  oo0ooO0 = O0o0O00Oo0o0 ( i1Iii )
  if oo0ooO0 != 'Failed' :
   oOoO0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oo0ooO0 )
   for Iii1I1111ii , i1oO0OO0 , url , ii1iii1i , I11iiiiI1i , iIiiiii1i in oOoO0o :
    if iiiI111I in Iii1I1111ii . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgold] - Source Pandoras[/COLOR]' , url , iIiiiii1i , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 54 - 54: OOooOOo . o000O0o % Ii / ii + I1111IIi % o000O0o
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 36 - 36: o000O0o
     if 74 - 74: ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 72 - 72: o0o00Oo0O + oOo0O0Ooo - O0OOOoOoo0 - oO0o
def o0i1I11iI1iiI ( ) :
 oO0OOoo0OO = OoOooO ( 'http://genietv.co.uk/redo/GenieArt/NEW/' )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( Iii1I1111ii ) . replace ( '.png' , '' ) , 'http://genietv.co.uk/redo/GenieArt/NEW/' + oOooO0 , 100111 , 'http://genietv.co.uk/redo/GenieArt/NEW/' + oOooO0 )
def I1 ( url ) :
 iioO0o = "ShowPicture(" + url + ')'
 xbmc . executebuiltin ( iioO0o )
 sys . exit ( 1 )
 if 50 - 50: O0OOOoOoo0 / O0OOOoOoo0 + Ii1IIIi1 * I11i1ii1 / Ii1I
def I1IIiiI1II1 ( ) :
 if 5 - 5: O0OOOoOoo0
 if 62 - 62: OOooOOo . ii . Ii1IIIi1 . oO0o * O0OOOoOoo0
 if 78 - 78: o000O0o / oO0o - o000O0o * ii . OOooOOo
 if 96 - 96: oOo0O0Ooo % ooOoO0O00 . I11i . o0o00Oo0O
 if 37 - 37: ooOoO0O00 - Ii1IIIi1 % ii / Ii1IIIi1 % I11i1ii1
 if 48 - 48: Ii % o000O0o
 if 29 - 29: O0OOOoOoo0 + Ii % ooOOOoO
 if 93 - 93: OOooOOo % iI11I1II1I1I
 if 90 - 90: oOo0O0Ooo - Ii1IIIi1 / ii1ii11IIIiiI / o0o00Oo0O / ooOOOoO
 if 87 - 87: OOooOOo / I1111IIi + iI11I1II1I1I
 if 93 - 93: iI11I1II1I1I + o000O0o % I11i1ii1
 O0Oo00OoOo ( 'SEASONS' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3NlYXNvbi8=' ) , 90053 , III1iII1I1ii + 'seasons.png' )
 O0Oo00OoOo ( 'EPISODES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL2VwaXNvZGUv' ) , 90054 , III1iII1I1ii + 'episodes.png' )
 O0Oo00OoOo ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90055 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 21 - 21: Ii1IIIi1
def iIiI1I1IIi11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , I1I1i11 in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( Iii1I1111ii + ' - ' + I1I1i11 ) . replace ( '&amp;' , '&' ) , url , 90053 , III1iII1I1ii + 'seasons.png' )
  if 25 - 25: I1111IIi - Ii1I
def I1iiII11IiIi1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , url , 90054 , III1iII1I1ii + 'episodes.png' )
  if 95 - 95: IIiIiII11i
def oo000oO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for ii1iii1i , Iii1I1111ii , url in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , url , 90054 , ii1iii1i )
 for url in next :
  O0Oo00OoOo ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 78 - 78: ii1ii11IIIiiI + OOooOOo + I1111IIi - I1111IIi . Ii / oO0o
def I11i11i1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)"></a></div>.+?<div class="numerando">(.+?)</div>.+?<a href="([^"]*)">(.+?)</a>.+?<span class="date">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)">.+?a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for ii1iii1i , I1I1i11 , url , Iii1I1111ii , OOOii1i1iiI in i1IIIII11I1IiI :
  iiOOooooO0Oo ( I1I1i11 + ' - ' + Iii1I1111ii + ' - ' + OOOii1i1iiI , url , 90044 , ii1iii1i , ii1iii1i , '' )
 for ii1iii1i , Iii1I1111ii , url in i1I :
  O0Oo00OoOo ( Iii1I1111ii , url , 90044 , ii1iii1i , ii1iii1i , '' )
 for url in next :
  O0Oo00OoOo ( 'NEXT' , url , 90053 , III1iII1I1ii + 'Next.png' )
  if 94 - 94: ooOoO0O00 * ooOoO0O00 % IIiIiII11i + Ii1IIIi1
def iIIi11 ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0000o0Oo = 'http://onlinemovies.tube/?s=' + ( oo00O0 ) . replace ( ' ' , '+' )
 iiiI111I = o0000o0Oo . lower ( )
 oO0OOoo0OO = OoOooO ( iiiI111I )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , ii1iii1i , Iii1I1111ii , III1Ii1i1I1 in i1IIIII11I1IiI :
  if 'season' in III1Ii1i1I1 :
   O0Oo00OoOo ( Iii1I1111ii , oOooO0 , 90054 , ii1iii1i , ii1iii1i , '' )
  if 'episodes' in III1Ii1i1I1 :
   O0Oo00OoOo ( Iii1I1111ii , oOooO0 , 90044 , ii1iii1i , ii1iii1i , '' )
 for oOooO0 in next :
  O0Oo00OoOo ( 'NEXT' , oOooO0 , 90053 , III1iII1I1ii + 'Next.png' )
  if 90 - 90: iI11I1II1I1I * IIiIiII11i
def oOOo0OoOOOoo ( ) :
 if 88 - 88: o000O0o * oO0o
 if 35 - 35: Ii1I / O0OOOoOoo0 % oOo0O0Ooo + iI11I1II1I1I
 if 79 - 79: OOooOOo / I11i1ii1
 if 77 - 77: I1ii11iIi11i
 if 46 - 46: iiiiiiii1
 if 72 - 72: O0OOOoOoo0 * Ii1IIIi1
 if 67 - 67: ooOoO0O00
 if 5 - 5: IIiIiII11i . ii
 if 57 - 57: oOo0O0Ooo
 if 35 - 35: ii - iiiiiiii1 / oO0o
 O0Oo00OoOo ( 'ALL MOVIES' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlL3dhdGNoLw==' ) , 90043 , III1iII1I1ii + 'allmov.png' )
 O0Oo00OoOo ( 'GENRE' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90041 , III1iII1I1ii + 'Genre.png' )
 O0Oo00OoOo ( 'BY YEAR' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90042 , III1iII1I1ii + 'Years.png' )
 O0Oo00OoOo ( 'SEARCH' , i11 ( 'aHR0cDovL29ubGluZW1vdmllcy50dWJlLw==' ) , 90045 , III1iII1I1ii + 'Search.png' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 50 - 50: OOooOOo
def i1i1Ii11Ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a> <i>(.+?)</i>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , I1I1i11 in i1IIIII11I1IiI :
  if 'genre' in url :
   O0Oo00OoOo ( ( Iii1I1111ii + ' - ' + I1I1i11 ) . replace ( '&amp;' , '&' ) , url , 90043 , III1iII1I1ii + 'Genre.png' )
   if 57 - 57: Ii1IIIi1 + iiiiiiii1 % Ii1I . oO0o / oO0o * o0o00Oo0O
def Ii1iiII1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if 'release' in url :
   O0Oo00OoOo ( Iii1I1111ii , url , 90043 , III1iII1I1ii + 'Years.png' )
   if 52 - 52: o000O0o / iiiiiiii1
def o0Oi11i1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="item movies">.+?<img src="([^"]*)" alt="([^"]*)"></a>.+?<span class="quality">(.+?)</span>.+?<h3><a href="([^"]*)">.+?<div class="texto">(.+?)<div class="degradado"></div></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<img src="([^"]*)" alt="([^"]*)" />.+?class="([^"]*)">.+?<a href="([^"]*)".+?class="rating">(.+?)</.+?<p>(.+?)</p>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( "<link rel='next' href='([^']*)' />" ) . findall ( oO0OOoo0OO )
 for ii1iii1i , Iii1I1111ii , O00O0 , url , i1oO0OO0 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii + ' ' + O00O0 , url , 90044 , ii1iii1i , ii1iii1i , i1oO0OO0 )
 for ii1iii1i , Iii1I1111ii , III1Ii1i1I1 , url , IiI , i1oO0OO0 in i1I :
  if 'movies' in III1Ii1i1I1 :
   iiOOooooO0Oo ( Iii1I1111ii + ' - ' + IiI , url , 90044 , ii1iii1i , ii1iii1i , i1oO0OO0 )
 for url in next :
  O0Oo00OoOo ( 'NEXT' , url , 90043 , III1iII1I1ii + 'Next.png' )
  if 87 - 87: I11i1ii1 . o0o00Oo0O % iiiiiiii1 + Ii1I + ii1ii11IIIiiI % iI11I1II1I1I
def ii11iIIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="option-1".+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  i1II1II1iii1i ( 'http:' + url )
  if 75 - 75: I1111IIi - OOooOOo - iI11I1II1I1I % I11i
def i1II1II1iii1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{file: "([^"]*)",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( ( Iii1I1111ii ) . replace ( '360p' , 'SD' ) . replace ( '480p' , 'SD' ) . replace ( '720p' , 'HD' ) . replace ( '1080p' , 'HD' ) , url , 222 , III1iII1I1ii + 'movhub.png' )
def OooooO ( ) :
 if 92 - 92: I11i / I11i * ii1ii11IIIiiI
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
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0000o0Oo = 'http://onlinemovies.tube/?s=' + ( oo00O0 ) . replace ( ' ' , '+' )
 iiiI111I = o0000o0Oo . lower ( )
 oO0OOoo0OO = OoOooO ( iiiI111I )
 i1IIIII11I1IiI = re . compile ( '<div class="result-item">.+?<a href="(.+?)".+?<img src="(.+?)".+?alt="(.+?)".+?<span class="(.+?)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , ii1iii1i , Iii1I1111ii , i1IiiiiIi1I in i1IIIII11I1IiI :
  if 'movies' in i1IiiiiIi1I :
   O0Oo00OoOo ( i1IiiiiIi1I + '-' + Iii1I1111ii , oOooO0 , 90044 , ii1iii1i )
 for oOooO0 in next :
  o0Oi11i1I ( oOooO0 )
  if 56 - 56: ii * o0o00Oo0O
def I1IIIiIiIi ( ) :
 O0Oo00OoOo ( 'Search' , '' , 80008 , III1iII1I1ii + 'Search.png' )
 oO0OOoo0OO = OoOooO ( 'http://www.join4films.com/' )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-taxonomy menu-item-object-category menu-item-.+?"><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , oOooO0 , 80006 , III1iII1I1ii + 'Desi.png' )
def oo0OoOOooO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img width="138" height="173" src="([^"]*)" class="attachment-index-thumb size-index-thumb wp-post-image" alt="([^"]*)"' ) . findall ( oO0OOoo0OO )
 next = re . compile ( 'href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( Iii1I1111ii , url , 80007 , ii1iii1i )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( 'Next' , url , 80006 , III1iII1I1ii + 'Next.png' )
def o0o0OO0o00o0O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  url = ( url ) . replace ( ' ' , '%20' )
  OOOoOO0o ( url )
def IIIIIIi1i ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0000o0Oo = 'http://www.join4films.com/?s=' + ( oo00O0 ) . replace ( ' ' , '+' ) + '&search_type=1'
 iiiI111I = o0000o0Oo . lower ( )
 oo0OoOOooO ( iiiI111I )
 if 26 - 26: iI11I1II1I1I - o0o00Oo0O . o0o00Oo0O
 if 68 - 68: Ii1IIIi1 + o000O0o . o0o00Oo0O . ii1ii11IIIiiI % ooOoO0O00 % Ii1IIIi1
 if 50 - 50: I1111IIi + I11i
 if 96 - 96: oO0o
 if 92 - 92: I1ii11iIi11i / Ii + Ii1I
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
def Ooo0oO ( ) :
 iiOOooooO0Oo ( 'Genre' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10073 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Most Viewed' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9tb3ZpZXMv' ) , 10077 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Box Office' , i11 ( 'aHR0cDovL2ltb3ZpZW1heC5zZS9jYXRlZ29yeS9ib3gtb2ZmaWNlLw==' ) , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( 'Search' , '' , 10078 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
 if 32 - 32: ooOoO0O00 . O0OOOoOoo0 + IIiIiII11i - oO0o - iI11I1II1I1I
def iIIIIiiii1I ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0000o0Oo = 'http://imoviemax.se/?s=' + ( oo00O0 ) . replace ( ' ' , '+' )
 iiiI111I = o0000o0Oo . lower ( )
 IIi1iI11IIIi1 ( iiiI111I )
def o00O0o0oo0oOO0oO ( url ) :
 iIiIII1iI1111 = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="cat-item cat-item-.+? "><a href="([^"]*)">(.+?)</a><i>(.+?)</i></li>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , Ii1I1I111iI in i1IIIII11I1IiI :
  if Iii1I1111ii in iIiIII1iI1111 :
   pass
  else :
   iiOOooooO0Oo ( Iii1I1111ii + ' - ' + Ii1I1I111iI + ' Films' , url , 10074 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
   iIiIII1iI1111 . append ( Iii1I1111ii )
   if 31 - 31: O0OOOoOoo0 + I1111IIi . I1ii11iIi11i * I1ii11iIi11i * IIiIiII11i * o0o00Oo0O
def o00O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li>.+?<b>.+?</b>.+?<a href="([^"]*)">(.+?)</a>.+?<span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , Oo000O in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii + ' - Views:' + Oo000O , url , 10075 , III1iII1I1ii + 'genievision.png' , O0o0Oo , '' )
  if 42 - 42: I1111IIi % O0OOOoOoo0 % I11i % o000O0o + ooOOOoO % OOooOOo
  if 3 - 3: o000O0o
def IIi1iI11IIIi1 ( url ) :
 OOOiI1 = [ ]
 oO0OOoo0OO = OoOooO ( url )
 next = re . compile ( "<link rel='next' href='(.+?)' />" ) . findall ( oO0OOoo0OO )
 for next in next :
  iiOOooooO0Oo ( 'NEXT PAGE' , next , 10074 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<a href="([^"]*)"><span class="player"></span></a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , Iii1I1111ii , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 10075 , ii1iii1i , ii1iii1i , '' )
  OOOiI1 . append ( Iii1I1111ii )
  if 84 - 84: Ii1IIIi1 * oOo0O0Ooo % ooOOOoO + Ii1IIIi1 / O0OOOoOoo0
def oo000oOO00o0oOO ( img , name , url ) :
 img = img
 name = name
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="([^"]*)" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</iframe></div>' ) . findall ( oO0OOoo0OO )
 for i1i1I1 , url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>> before' + url
  I1i = ( url ) . replace ( 'player' , 'watch' ) + '&fv=&sou='
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<< after' + I1i
  OOo0O = ( i1i1I1 ) . replace ( 'play-' , 'Server ' )
  OOiIiIIi1 ( OOo0O , I1i , 10076 , img , img , '' )
  if 100 - 100: oO0o % oO0o
def iI1I1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source src="([^"]*)" type="video/mp4">' ) . findall ( oO0OOoo0OO )
 for I11iiii1I in i1IIIII11I1IiI :
  if '=m' in I11iiii1I :
   ii1O0ooooo000 ( I11iiii1I )
  elif 'php' in I11iiii1I :
   iI1I1 ( url )
  else :
   oO0OOoo0OO = OoOooO ( I11iiii1I )
   i1IIIII11I1IiI = re . compile ( 'content="([^"]*)">' ) . findall ( oO0OOoo0OO )
   for iiiiI1iiiIi in i1IIIII11I1IiI :
    ii1O0ooooo000 ( I11iiii1I )
    if 97 - 97: Ii % o000O0o / I1ii11iIi11i / I1ii11iIi11i
    if 97 - 97: IIiIiII11i - iiiiiiii1 - iI11I1II1I1I * oOo0O0Ooo
    if 54 - 54: iI11I1II1I1I
def i111i1I1ii1i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 O0Oooo = re . compile ( '<td id=".+?" class="today">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iIII1 , I11iI1I in O0Oooo :
  print 'there ><><><><><><><><><><><><'
  I1iIII1 = I1iIII1
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( I11iI1I ) )
  for Iii1I1111ii , Iii1iiIi1II1 in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + I1iIII1 + '[/COLOR] - ' + Iii1I1111ii + ' - [COLOR' + II + ']' + Iii1iiIi1II1 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
 O00oO0 = re . compile ( '<td id=".+?" class="day">.+?title="([^"]*)">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I1iIII1 , Oo000o in O00oO0 :
  print 'there ><><><><><><><><><><><><'
  I1iIII1 = I1iIII1
  i1IIIII11I1IiI = re . compile ( '<p><a href=".+?" rel=".+?">(.+?)</a>.+?<br /><a href=".+?">(.+?)</a>.+?</p>' , re . DOTALL ) . findall ( str ( Oo000o ) )
  for Iii1I1111ii , Iii1iiIi1II1 in i1IIIII11I1IiI :
   print 'here <><><><><><><><><><><><>'
   iiOOooooO0Oo ( '[COLORred]' + I1iIII1 + '[/COLOR] - ' + Iii1I1111ii + ' - [COLOR' + II + ']' + Iii1iiIi1II1 + '[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5wb2dkZXNpZ24uY28udWsvY2F0Lw==' ) , 10070 , III1iII1I1ii + 'loader.png' , O0o0Oo , '' )
   if 69 - 69: Ii1I + O0OOOoOoo0 * o0o00Oo0O . Ii1IIIi1 % OOooOOo
   if 96 - 96: I11i1ii1 . I11i1ii1 - ooOOOoO / ooOOOoO
   if 96 - 96: Ii / oOo0O0Ooo - o0o00Oo0O . I11i1ii1
def IiIi1iIIi1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 O00oO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O00oO0 in O00oO0 :
  Iii1I1111ii = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00oO0 ) )
  for Iii1I1111ii in Iii1I1111ii :
   Iii1I1111ii = ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
  url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00oO0 ) )
  for url in url :
   url = 'https://www.youtube.com/w' + url
  iiIi1IIiI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00oO0 ) )
  for iiIi1IIiI in iiIi1IIiI :
   iiIi1IIiI = 'http:' + iiIi1IIiI
  OOiIiIIi1 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIi1IIiI , '' , '' )
  if 39 - 39: I11i1ii1 / o0o00Oo0O * I1111IIi
  if 17 - 17: ii1ii11IIIiiI / iI11I1II1I1I - oO0o + oOo0O0Ooo % Ii1IIIi1
  if 14 - 14: I11i % I1111IIi + Ii1I + oO0o
  if 76 - 76: oO0o - Ii + OOooOOo + Ii1IIIi1 / ii
def IIIII1 ( url ) :
 if 50 - 50: IIiIiII11i - iiiiiiii1 + iI11I1II1I1I + iI11I1II1I1I
 OoooooOo = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="explore-list">.+?<div class="el-img"><a href="([^"]*)" class=".+?"><img src="([^"]*)" alt=".+?<h3>(.+?)</h3><p>(.+?)</p></div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I11iiii1I , ii1iii1i , Iii1I1111ii , OooOo in i1IIIII11I1IiI :
  Iii1I1111ii = ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#039;' , '\'' ) . replace ( '&' , '&' ) . replace ( '&quot;' , '"' )
  O0 = OoOooO ( I11iiii1I )
  i1I = re . compile ( '<!-- # player # -->.+?<iframe title=".+?".+?src="http://www.youtube.com/embed/(.+?)?autohide.+?<!-- detail box -->(.+?)</div>' , re . DOTALL ) . findall ( O0 )
  for IIiI11i1111Ii , O00oo in i1I :
   oOo0 = re . compile ( '<p>(.+?)</p>' , re . DOTALL ) . findall ( str ( O00oo ) )
   for i1oO0OO0 in oOo0 :
    if Iii1I1111ii in OoooooOo :
     pass
    else :
     OOiIiIIi1 ( Iii1I1111ii , IIiI11i1111Ii , 8043 , ii1iii1i , ii1iii1i , i1oO0OO0 )
     I1I11i ( 'movies' , 'INFO' )
     OoooooOo . append ( Iii1I1111ii )
     if 30 - 30: Ii1IIIi1 + IIiIiII11i - I1111IIi * ii
     if 19 - 19: I1111IIi - I11i . iI11I1II1I1I . OOooOOo / Ii1IIIi1
def OOO0O00Oo ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooO )
 for url , iII1iii , i1oO0OO0 , I11iiiiI1i , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 10065 , iII1iii , I11iiiiI1i , i1oO0OO0 )
 I1I11i ( 'movies' , 'INFO' )
 if 13 - 13: iI11I1II1I1I
def IiIIII1iiIIi ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0000o0Oo = 'https://www.youtube.com/results?search_query=' + ( oo00O0 ) . replace ( ' ' , '+' )
 iiiI111I = o0000o0Oo . lower ( )
 oO0OOoo0OO = OoOooO ( iiiI111I )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in next :
  oOooO0 = 'https://www.youtube.com' + oOooO0
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , oOooO0 , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for ii1iii1i , oOooO0 , Iii1I1111ii , i1I1IiI1ii , O00oo in i1IIIII11I1IiI :
  OOOO . append ( Iii1I1111ii )
  I1I11i ( 'tvshows' , 'INFO' )
  iiIi1IIiI = 'http:' + ( ii1iii1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiIi1IIiI
  oOooO0 = 'http://www.youtube.com' + oOooO0
  OOiIiIIi1 ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIi1IIiI , iiIi1IIiI , O00oo )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for ii1iii1i , oOooO0 , Iii1I1111ii , i1I1IiI1ii in i1IIIII11I1IiI :
   print 'im doing it'
   I1I11i ( 'tvshows' , 'INFO' )
   iiIi1IIiI = 'http:' + ( ii1iii1i ) . replace ( 'https:' , '' )
   oOooO0 = 'http://www.youtube.com' + oOooO0
   if '&' in oOooO0 :
    print ' i got here'
    oO0OOoo0OO = OoOooO ( oOooO0 )
    O00oO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for O00oO0 in O00oO0 :
     Iii1I1111ii = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00oO0 ) )
     for Iii1I1111ii in Iii1I1111ii :
      Iii1I1111ii = ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     oOooO0 = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00oO0 ) )
     for oOooO0 in oOooO0 :
      oOooO0 = 'https://www.youtube.com/w' + oOooO0
     iiIi1IIiI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00oO0 ) )
     for iiIi1IIiI in iiIi1IIiI :
      iiIi1IIiI = 'http:' + iiIi1IIiI
     OOiIiIIi1 ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIi1IIiI , O0o0Oo , '' )
   elif Iii1I1111ii in OOOO :
    pass
   elif 'user' in oOooO0 or 'elete' in Iii1I1111ii :
    pass
   elif 'hannel' in oOooO0 :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + oOooO0
    oO0OOoo0OO = OoOooO ( oOooO0 )
    O00OOoOOOO00O = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for ii1iii1i , oOooO0 , Iii1I1111ii in O00OOoOOOO00O :
     if 'outube' in oOooO0 or 'list' in oOooO0 :
      pass
     elif 'atch' in oOooO0 :
      oOooO0 = ( oOooO0 ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ii1iii1i , 'http:' + ii1iii1i , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , ( oOooO0 ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIi1IIiI , iiIi1IIiI , '' )
    if 72 - 72: oOo0O0Ooo + I1111IIi . OOooOOo + OOooOOo
def ooooOoo0OO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>.+?<div class="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2" dir="ltr">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<a href="([^"]*)" class="yt-uix-button.+?class="yt-uix-button-content">Next.+?</span></a>' ) . findall ( oO0OOoo0OO )
 for url in next :
  url = 'https://www.youtube.com' + url
  iiOOooooO0Oo ( '[COLOR' + II + '] NEXT [/COLOR]' , url , 10065 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 for ii1iii1i , url , Iii1I1111ii , i1I1IiI1ii , O00oo in i1IIIII11I1IiI :
  OOOO . append ( Iii1I1111ii )
  I1I11i ( 'tvshows' , 'INFO' )
  iiIi1IIiI = 'http:' + ( ii1iii1i ) . replace ( 'https:' , '' )
  print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + iiIi1IIiI
  url = 'http://www.youtube.com' + url
  OOiIiIIi1 ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIi1IIiI , iiIi1IIiI , O00oo )
 else :
  i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)" alt=.+?yt-lockup-title "><a href="([^"]*)".+?data-sessionlink=.+?" title="([^"]*)".+?<span class="accessible-description".+?>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for ii1iii1i , url , Iii1I1111ii , i1I1IiI1ii in i1IIIII11I1IiI :
   I1I11i ( 'tvshows' , 'INFO' )
   iiIi1IIiI = 'http:' + ( ii1iii1i ) . replace ( 'https:' , '' )
   url = 'http://www.youtube.com' + url
   if '&' in url :
    oO0OOoo0OO = OoOooO ( url )
    O00oO0 = re . compile ( '<li class="yt-uix-scroller-scroll-unit "(.+?)</li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for O00oO0 in O00oO0 :
     Iii1I1111ii = re . compile ( 'data-video-title="([^"]*)"' ) . findall ( str ( O00oO0 ) )
     for Iii1I1111ii in Iii1I1111ii :
      Iii1I1111ii = ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&quot;' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&' , '&' )
     url = re . compile ( '<a href="/w(.+?)&' ) . findall ( str ( O00oO0 ) )
     for url in url :
      url = 'https://www.youtube.com/w' + url
     iiIi1IIiI = re . compile ( '<img.+?="([^"]*)"' ) . findall ( str ( O00oO0 ) )
     for iiIi1IIiI in iiIi1IIiI :
      iiIi1IIiI = 'http:' + iiIi1IIiI
     OOiIiIIi1 ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIi1IIiI , O0o0Oo , '' )
   elif Iii1I1111ii in OOOO :
    pass
   elif 'user' in url or 'elete' in Iii1I1111ii :
    pass
   elif 'hannel' in url :
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + url
    oO0OOoo0OO = OoOooO ( url )
    O00OOoOOOO00O = re . compile ( 'data-thumb="([^"]*)".+?href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
    for ii1iii1i , url , Iii1I1111ii in O00OOoOOOO00O :
     if 'outube' in url or 'list' in url :
      pass
     elif 'atch' in url :
      url = ( url ) . replace ( '/watch?v=' , '' )
      OOiIiIIi1 ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , 'http:' + ii1iii1i , 'http:' + ii1iii1i , '' )
     else :
      pass
   else :
    OOiIiIIi1 ( '[COLORred]' + i1I1IiI1ii + '[/COLOR]' + '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIi1IIiI , iiIi1IIiI , '' )
    if 85 - 85: IIiIiII11i . I11i1ii1 % Ii1IIIi1 % ooOOOoO
def OOo00ooOoO0o ( ) :
 Oo0oO ( )
 i1i1iiIIiiiII ( )
 if 5 - 5: ii / I11i % ooOOOoO % oO0o * O0OOOoOoo0 + iI11I1II1I1I
 if 11 - 11: iiiiiiii1 % Ii % o000O0o . I1111IIi
 iiOOooooO0Oo ( '[COLOR' + II + ']My Account[/COLOR]' , 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o , 60004 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']G-Tv Channels[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvZ3VpZGUvdGhlbGlzdHVsdC5tM3U=' ) ) , 60001 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 oOO0o ( '[COLORsteelblue]VOD Lists[/COLOR]' , '' , 40000 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
 if 65 - 65: O0OOOoOoo0 . oO0o + ii1ii11IIIiiI
 if 25 - 25: I11i + I1ii11iIi11i . I1ii11iIi11i % ii - ii1ii11IIIiiI
 if 43 - 43: oO0o % oO0o
def IIiii11ii1i ( ) :
 oOO0o ( ( '[COLORsteelblue]All Vod[/COLOR]' ) . replace ( '\/' , ' - ' ) , II1iI1IIi + '&action=get_vod_streams' , 40001 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( Ii11iiI1 )
 i1IIIII11I1IiI = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLORsteelblue]' + Iii1I1111ii + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOooO0 , 40001 , III1iII1I1ii + 'Vod_Lists.png' , O0o0Oo , '' )
def oO0O ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( OOoooO00o0o + url )
 i1IIIII11I1IiI = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg .+?,"container_extension":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , type , I11iiii1I , ooOoOo0 , I1ii1Ii1 in i1IIIII11I1IiI :
  OOiIiIIi1 ( Iii1I1111ii , OoOoO + I11iiii1I + '.' + I1ii1Ii1 , 222 , ( ooOoOo0 ) . replace ( '\/' , '/' ) + 'jpg' , O0o0Oo , 'Type: ' + type )
  if 13 - 13: OOooOOo % I11i1ii1
def i1i1iiIIiiiII ( ) :
 if OO0o == 'insert_password' :
  OOooO0OOoo . ok ( '[COLOR' + II + ']G-Tv Login[/COLOR]' , 'You need to set username and password to access this' , 'These are unique and provided upon purchase' , 'from [COLOR' + II + ']http://GenieTv.co.uk[/COLOR]' )
  oo00 . openSettings ( sys . argv [ 0 ] )
 else :
  O0OOOOo0 ( )
  if 72 - 72: I11i % oOo0O0Ooo / O0OOOoOoo0 - o0o00Oo0O + ooOOOoO
  if 83 - 83: o0o00Oo0O
  if 89 - 89: I1ii11iIi11i + Ii1I - I11i
  if 40 - 40: oO0o + oO0o
  if 94 - 94: O0OOOoOoo0 * iI11I1II1I1I . ooOOOoO
  if 13 - 13: iI11I1II1I1I * OOooOOo / iiiiiiii1 % I11i1ii1 + o000O0o
  if 41 - 41: Ii1I
  if 5 - 5: I1ii11iIi11i
def O0OOOOo0 ( ) :
 i1i = OoOooO ( 'http://piesustv.net:8000/panel_api.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 for oOooO0 in i1IIIII11I1IiI :
  o0oOo00 = datetime . fromtimestamp ( float ( i1IIIII11I1IiI [ 0 ] ) )
  o0oOo00 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= o0oOo00 <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   OOooO0OOoo . ok ( '[COLORred]Your Account Expires Today[/COLOR]' , '[COLOR' + II + ']If You Wish To Continue With Your Subscription[/COLOR]' , '' , '[COLOR' + II + ']Please Visit [COLORred]GenieTv.co.uk[COLOR' + II + '] To Purchase A licence[/COLOR]' )
def IiI1III ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"username":"(.+?)"' ) . findall ( i1i )
 O0O0OOO = re . compile ( '"password":"(.+?)"' ) . findall ( i1i )
 ii1ooO = re . compile ( '"status":"(.+?)"' ) . findall ( i1i )
 i1I = re . compile ( '"exp_date":"(.+?)"' ) . findall ( i1i )
 iiI1IIIi = re . compile ( '"active_cons":"(.+?)"' ) . findall ( i1i )
 iiIiIIIiiI = re . compile ( '"created_at":"(.+?)"' ) . findall ( i1i )
 oOoOoO000OO = re . compile ( '"max_connections":"(.+?)"' ) . findall ( i1i )
 o0IiiiI111I = re . compile ( '"is_trial":"1"' ) . findall ( i1i )
 o0Oo0oOooOoOo = re . compile ( '"is_trial":"0"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']My GTV Account Information[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  ii1ii111 ( '[COLOR' + II + ']Username:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in O0O0OOO :
  ii1ii111 ( '[COLOR' + II + ']Password:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in ii1ooO :
  ii1ii111 ( '[COLOR' + II + ']Status:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in iiIiIIIiiI :
  o0oOo00 = datetime . fromtimestamp ( float ( iiIiIIIiiI [ 0 ] ) )
  o0oOo00 . strftime ( '%Y-%m-%d %H:%M:%S' )
  ii1ii111 ( '[COLOR' + II + ']Created:[/COLOR]  %s' % ( o0oOo00 ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in i1I :
  o0oOo00 = datetime . fromtimestamp ( float ( i1I [ 0 ] ) )
  o0oOo00 . strftime ( '%Y-%m-%d %H:%M:%S' )
  if IIiiiiiiIi1I1 <= o0oOo00 <= IIiiiiiiIi1I1 + timedelta ( hours = 24 ) :
   ii1ii111 ( '[COLORred]Expires Today[/COLOR]' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
  ii1ii111 ( '[COLOR' + II + ']Expires:[/COLOR]  %s' % ( o0oOo00 ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in iiI1IIIi :
  ii1ii111 ( '[COLOR' + II + ']Active Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in oOoOoO000OO :
  ii1ii111 ( '[COLOR' + II + ']Max Connection:[/COLOR]  %s' % ( url ) , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in o0IiiiI111I :
  ii1ii111 ( '[COLOR' + II + ']Trial:[/COLOR] Yes' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 for url in o0Oo0oOooOoOo :
  ii1ii111 ( '[COLOR' + II + ']Trial:[/COLOR] No' , '' , '' , III1iII1I1ii + 'MyAcc.png' )
 ii1ii111 ( '' , '' , '' , '' )
 ii1ii111 ( '' , '' , '' , '' )
 ii1ii111 ( '[COLOR' + II + ']Sign up[/COLOR]' , '' , 50006 , '' )
 if 45 - 45: ii1ii11IIIiiI / oO0o - I1ii11iIi11i / I11i1ii1 - ooOOOoO * o000O0o
def O00OoOoO ( ) :
 OOooO0OOoo . ok ( '[COLOR=white]ReCreate Addons.ini[/COLOR]' , 'If it doesnt work ensure login details are correct and retry' , '' , 'This will allow access to streams in guide without linking to favourites' )
 xbmc . executebuiltin ( "XBMC.RunScript(" + OOO00 + ")" )
 ooO0o0oo ( )
 OOooO0OOoo . ok ( '[COLOR=yellow]Done[/COLOR]' , 'Done' , 'Easy as that' , 'Now Go to guide and it should link your GTV streams' )
 if 79 - 79: I1111IIi % oO0o
def Oo0oOO ( data ) :
 ooooo = len ( data ) % 4
 if 26 - 26: oOo0O0Ooo
 if 41 - 41: oOo0O0Ooo - Ii
 if 6 - 6: oO0o / I1ii11iIi11i / O0OOOoOoo0
 if 13 - 13: Ii1I % OOooOOo
 if 76 - 76: o0o00Oo0O . oO0o + OOooOOo
 if 41 - 41: IIiIiII11i * I11i1ii1
 if ooooo != 0 :
  data += b'=' * ( 4 - ooooo )
 return base64 . decodestring ( data )
II1iI1IIi = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s' % ( II11iiii1Ii , OO0o )
OoOoO = 'http://piesustv.net:8000/movie/%s/%s/' % ( II11iiii1Ii , OO0o )
o0oOoOo0 = 'http://piesustv.net:8000/live/%s/%s/' % ( II11iiii1Ii , OO0o )
III1IiI1i1i = '&action=get_live_categories'
o0OOOOOo0 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_live_streams&category_id=' % ( II11iiii1Ii , OO0o )
Ii11iiI1 = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_categories' % ( II11iiii1Ii , OO0o )
OOoooO00o0o = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_vod_streams&category_id=' % ( II11iiii1Ii , OO0o )
oooOoO = 'http://piesustv.net:8000/player_api.php?username=%s&password=%s&action=get_short_epg&stream_id=' % ( II11iiii1Ii , OO0o )
O0Oo0 = "http://piesustv.net:8000/enigma2.php?username=%s&password=%s&type=get_live_streams&cat_id=" % ( II11iiii1Ii , OO0o )
if 46 - 46: oOo0O0Ooo * OOooOOo
def oOoO00O000 ( ) :
 iiOOooooO0Oo ( ( '[COLORsteelblue]Full List[/COLOR]' ) . replace ( '\/' , ' - ' ) , '0' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( ( '[COLORsteelblue]PPV Wrestling[/COLOR]' ) . replace ( '\/' , ' - ' ) , '23' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( ( '[COLORsteelblue]PPV Boxing[/COLOR]' ) . replace ( '\/' , ' - ' ) , '13' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( ( '[COLORsteelblue]IND/PAK[/COLOR]' ) . replace ( '\/' , ' - ' ) , '21' , 600033 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( ( '[COLORsteelblue]International[/COLOR]' ) . replace ( '\/' , ' - ' ) , '12' , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( II1iI1IIi + III1IiI1i1i )
 i1IIIII11I1IiI = re . compile ( '"category_id":"([^"]*)","category_name":"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if '12' in oOooO0 :
   pass
  elif '21' in oOooO0 :
   pass
  elif '23' in oOooO0 :
   pass
  elif '13' in oOooO0 :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLORsteelblue]' + Iii1I1111ii + '[/COLOR]' ) . replace ( '\/' , ' - ' ) , oOooO0 , 60003 , III1iII1I1ii + 'GTV.png' , O0o0Oo , '' )
   if 54 - 54: o0o00Oo0O - O0OOOoOoo0 . Ii1IIIi1 % O0OOOoOoo0 + O0OOOoOoo0
def i1iI1Iiii1I ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( O0Oo0 + url )
 O00oO0 = re . compile ( '<channel>(.+?)</channel>' ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<title>(.+?)</title><description>(.+?)/description><desc_image><!.+?http(.+?)".+?<stream_url><!.+?http(.+?).ts.+?></stream_url>' , re . DOTALL ) . findall ( str ( O00oO0 ) )
 i1I = re . compile ( '<title>(.+?)</title>.+?<description/><desc_image><!.+?http(.+?)".+?<stream_url><!.+?http(.+?).ts.+?></stream_url>' , re . DOTALL ) . findall ( str ( O00oO0 ) )
 for Iii1I1111ii , i1oO0OO0 , ii1iii1i , I11iiii1I in i1IIIII11I1IiI :
  if 'PPV' in Iii1I1111ii :
   pass
  else :
   try :
    I1iII = ( i11 ( Iii1I1111ii ) )
    O00oo = ( ( i11 ( i1oO0OO0 ) ) )
    Iii1I1IIII = '('
    OooooOoO = ')'
    OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1iII + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + I11iiii1I + '.m3u8' , 222 , 'http' + ii1iii1i , O0o0Oo , ( '[COLOR' + II + ']' + O00oo + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( OooooOoO , '[COLORsteelblue]' ) . replace ( Iii1I1IIII , '[COLORorangered]' ) )
   except :
    pass
    Iii1I1IIII = '('
    OooooOoO = ')'
    OOiIiIIi1 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + I11iiii1I + '.m3u8' , 222 , 'http' + ii1iii1i , O0o0Oo , ( '[COLOR' + II + ']' + i1oO0OO0 + '[/COLOR]' ) . replace ( '<' , '' ) . replace ( OooooOoO , '[COLORsteelblue]' ) . replace ( Iii1I1IIII , '[COLORorangered]' ) )
   I1I11i ( 'tvshows' , 'Media Info 3' )
 for Iii1I1111ii , ii1iii1i , I11iiii1I in i1I :
  if 'PPV' in Iii1I1111ii :
   pass
  I1iII = ( Oo0oOO ( Iii1I1111ii ) )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + I1iII + '[/COLOR]' ) . replace ( 'min' , 'min[COLORsteelblue]' ) . replace ( '+' , '[COLORorangered]+' ) , 'http' + I11iiii1I + '.m3u8' , 222 , 'http' + ii1iii1i , O0o0Oo , '' )
  if 79 - 79: I11i1ii1 % Ii1IIIi1
def oO0O0o0O ( url ) :
 url = url
 oO0OOoo0OO = OoOooO ( o0OOOOOo0 + url )
 i1IIIII11I1IiI = re . compile ( '"name":"([^"]*)","stream_type":"([^"]*)","stream_id":"([^"]*)","stream_icon":"(.+?)jpg' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , type , I11iiii1I , ooOoOo0 in i1IIIII11I1IiI :
  iiiiI1iiiIi = ( o0oOoOo0 + I11iiii1I + '.m3u8' ) . strip ( )
  OOiIiIIi1 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , iiiiI1iiiIi , 222 , ( ooOoOo0 ) . replace ( '\/' , '/' ) + 'jpg' , O0o0Oo , type )
  I1I11i ( 'tvshows' , 'Media Info 3' )
def oOO00ooOOo ( url , name , img ) :
 img = img
 name = name
 url = url
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/xmltv.php?username=' + II11iiii1Ii + '&password=' + OO0o )
 i1IIIII11I1IiI = re . compile ( 'channel="([^"]*)">.+?<title>(.+?)</title>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for IIi , ii11Iiii in i1IIIII11I1IiI :
  if name == IIi :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) + ii11Iiii , ( url ) . strip ( ) , 222 , img , img , '' )
  else :
   OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( url ) . strip ( ) , 222 , img , img , '' )
def II1 ( name ) :
 OoooOo = name
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="Live Events"",.+?\n(.+?)\n' ) . findall ( oO0OOoo0OO )
 for name , ii1iii1i , oOooO0 in i1IIIII11I1IiI :
  oOooO0 = ( oOooO0 ) . replace ( '.ts' , '.m3u8' )
  OOiIiIIi1 ( ( '' + name + '' ) . replace ( '_' , ' ' ) , ( oOooO0 ) . strip ( ) , 222 , ii1iii1i , ii1iii1i , '' )
 else :
  OOiIiIIi1 ( '[COLORred]Streams will appear here for live events when available[/COLOR]' , '' , 222 , '' , '' , '' )
  if 34 - 34: ii1ii11IIIiiI * ii1ii11IIIiiI - Ii1I - o0o00Oo0O . Ii
  if 32 - 32: iI11I1II1I1I . oO0o * o000O0o / Ii1IIIi1 . IIiIiII11i - I1ii11iIi11i
  if 10 - 10: Ii1I / Ii - ii1ii11IIIiiI + o000O0o * oOo0O0Ooo
  if 94 - 94: oOo0O0Ooo + iI11I1II1I1I / o0o00Oo0O - ii % Ii1I
  if 64 - 64: ooOOOoO + oO0o
  if 25 - 25: oOo0O0Ooo . I11i1ii1 + oOo0O0Ooo % ii1ii11IIIiiI * iI11I1II1I1I
  if 31 - 31: Ii + Ii1IIIi1 - o0o00Oo0O
  if 51 - 51: oO0o * ooOoO0O00 / ii1ii11IIIiiI * Ii1IIIi1 + I11i1ii1 % Ii1I
  if 34 - 34: o000O0o * ii + ii1ii11IIIiiI + Ii
  if 22 - 22: ooOoO0O00
  if 24 - 24: ooOOOoO / oOo0O0Ooo * ooOoO0O00 % ii
  if 99 - 99: Ii . IIiIiII11i . ii
def OoOOoooOO0O ( ) :
 iiOOooooO0Oo ( 'Full Backup' , '' , 10061 , III1iII1I1ii + 'FullBackUp.png' , O0o0Oo , 'Back Up Your Full System' )
 if os . path . exists ( ooOooo000oOO ) :
  iiOOooooO0Oo ( 'Backup Genie Favourites' , oOooO0 , 10062 , III1iII1I1ii + 'BackupGenieFavourites.png' , O0o0Oo , 'Back Up Your favourites' )
 if os . path . exists ( oO0 ) :
  iiOOooooO0Oo ( 'Backup Ivue Config' , oO0 , 10062 , III1iII1I1ii + 'BackUpIvueConfig.png' , O0o0Oo , 'Back Up Your master.db' )
 if os . path . exists ( Ii1iIiII1ii1 ) :
  iiOOooooO0Oo ( 'Backup Kodi Favourites' , Ii1iIiII1ii1 , 10062 , III1iII1I1ii + 'BackKodiFavourites.png' , O0o0Oo , 'Back Up Your favourites.xml' )
  if 59 - 59: Ii . ii / ooOOOoO * Ii1I + ii
  if 3 - 3: Ii * I1ii11iIi11i % iI11I1II1I1I % oOo0O0Ooo * O0OOOoOoo0 / Ii1IIIi1
  if 95 - 95: I1111IIi * o0o00Oo0O * iiiiiiii1 . ii % I1ii11iIi11i + Ii1I
zip = oo00 . getSetting ( 'zip' )
oOIii11111iiI = xbmc . translatePath ( os . path . join ( zip ) )
def o0OOOOoO ( ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if not os . path . exists ( zip ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 70 - 70: IIiIiII11i + iiiiiiii1 + Ii - ooOoO0O00 / I1111IIi
  if 40 - 40: Ii1I * iiiiiiii1
  if 38 - 38: o0o00Oo0O . I1ii11iIi11i + OOooOOo - o000O0o
def i1iIii ( name , url , description ) :
 if 'Backup' in name :
  if 'Genie' in name :
   url = ooOooo000oOO
  elif 'Ivue' in name :
   url = oO0
  elif 'Kodi' in name :
   url = Ii1iIiII1ii1
  o0OOOOoO ( )
  o0O0ooooooo00 = open ( url ) . read ( )
  I1111ii11IIII = os . path . join ( oOIii11111iiI , description . split ( 'Your ' ) [ 1 ] )
  OOoO = open ( I1111ii11IIII , mode = 'w' )
  OOoO . write ( o0O0ooooooo00 )
  OOoO . close ( )
 else :
  if 'guisettings.xml' in description :
   IiIi1II111I = open ( os . path . join ( oOIii11111iiI , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   o00o = '<setting type="([^"]*)" name="%s.(.+?)">(.+?)</setting>' % skin
   i1IIIII11I1IiI = re . compile ( o00o ) . findall ( IiIi1II111I )
   for type , IIi1i1 , o0O0Ooo in i1IIIII11I1IiI :
    o0O0Ooo = o0O0Ooo . replace ( '&quot;' , '' ) . replace ( '&' , '&' )
    xbmc . executebuiltin ( "Skin.Se	t%s(%s,%s)" % ( type . title ( ) , IIi1i1 , o0O0Ooo ) )
  else :
   I1111ii11IIII = os . path . join ( url )
   o0O0ooooooo00 = open ( os . path . join ( oOIii11111iiI , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   OOoO = open ( I1111ii11IIII , mode = 'w' )
   OOoO . write ( o0O0ooooooo00 )
   OOoO . close ( )
 OOooO0OOoo . ok ( "[COLOR=white]GenieTv[/COLOR]" , "" , 'All Done !' , '' )
 if 79 - 79: I11i1ii1 . o000O0o / o000O0o - I11i1ii1 * I1ii11iIi11i / I11i
 if 19 - 19: Ii1I
 if 46 - 46: iI11I1II1I1I . Ii - OOooOOo % o0o00Oo0O / IIiIiII11i * ooOoO0O00
 if 66 - 66: o0o00Oo0O
def oOooOOo00ooO ( ) :
 o0OO0oooo = 1
 o0OOOOoO ( )
 I11II1i1 = xbmc . translatePath ( os . path . join ( oOIii11111iiI , 'Build Backup' , 'Full Backup' , '' ) )
 IiI1ii11I1 = xbmc . translatePath ( os . path . join ( oOIii11111iiI , 'Build Backup' , 'my_full_backup.zip' ) )
 I1i1iI = xbmc . translatePath ( os . path . join ( oOIii11111iiI , 'Build Backup' , 'my_full_backup_GUI_Settings.zip' ) )
 if not os . path . exists ( I11II1i1 ) :
  os . makedirs ( I11II1i1 )
 I1iI1I1ii1 = OOooO0OOoo . input ( 'Enter a name for this backup' , type = xbmcgui . INPUT_ALPHANUM )
 if ( not I1iI1I1ii1 ) : return False , 0
 I1iII = I1iI1I1ii1
 iIIi1 = xbmc . translatePath ( os . path . join ( I11II1i1 , I1iII + '.zip' ) )
 o0Ooo0o0Oo = [ 'plugin.video.GenieTv' ]
 oo00ooooOOo00 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' ]
 ii1i = [ 'plugin.video.GenieTv' , 'repository.origin' , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OO00Oooo000 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' ]
 iI1 = "Creating full backup of existing build"
 ii111iiIii = "Creating Community Build"
 oO0oiIiI = "Archiving..."
 iIIiiiI1iI1 = ""
 oO00000oO0o0O = "Please Wait"
 IIIiI1iI1 ( Oo0o0000o0o0 , iIIi1 , ii111iiIii , oO0oiIiI , iIIiiiI1iI1 , oO00000oO0o0O , ii1i , OO00Oooo000 )
 time . sleep ( 1 )
 IIiIiiii1I1 = xbmc . translatePath ( os . path . join ( I11II1i1 , I1iII + '_guisettings.zip' ) )
 oO0O0 = zipfile . ZipFile ( IIiIiiii1I1 , mode = 'w' )
 try :
  oO0O0 . write ( xbmc . translatePath ( os . path . join ( Oo0o0000o0o0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 oO0O0 . close ( )
 if o0OO0oooo == 0 :
  OOooO0OOoo . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your' , 'system, please reboot and try again.' , '' )
 else :
  OOooO0OOoo . ok ( "SUCCESS!" , 'You Are Now Backed Up. If you\'d like to share this build with' , 'the community please post details on the forum at' , '[COLOR=blue][B]http://rh-project.info[/COLOR][/B]' )
  OOooO0OOoo . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=yellow]' + IiI1ii11I1 , '[/COLOR]Universal Backup (can be used on any device): [COLOR=yellow]' + iIIi1 + '[/COLOR]' )
  if 65 - 65: O0OOOoOoo0 . oOo0O0Ooo
def IIIiI1iI1 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 IIi11IIiIi1i = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 IiiOoo0o0ooooOOo = len ( sourcefile )
 oOoOO0000oO00 = [ ]
 O0oiIiiIi = [ ]
 o0oOoO00o . create ( message_header , message1 , message2 , message3 )
 for i1I111II , Oo0OOo , i1II11I11ii1 in os . walk ( sourcefile ) :
  for file in i1II11I11ii1 :
   O0oiIiiIi . append ( file )
 OOoO0oO00o = len ( O0oiIiiIi )
 for i1I111II , Oo0OOo , i1II11I11ii1 in os . walk ( sourcefile ) :
  Oo0OOo [ : ] = [ OOO0OoO0oo0OO for OOO0OoO0oo0OO in Oo0OOo if OOO0OoO0oo0OO not in exclude_dirs ]
  i1II11I11ii1 [ : ] = [ OOoO for OOoO in i1II11I11ii1 if OOoO not in exclude_files ]
  for file in i1II11I11ii1 :
   oOoOO0000oO00 . append ( file )
   i1iI1Ii11Ii1 = len ( oOoOO0000oO00 ) / float ( OOoO0oO00o ) * 100
   o0oOoO00o . update ( int ( i1iI1Ii11Ii1 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   o0OoO0oo0O0o = os . path . join ( i1I111II , file )
   if not 'temp' in Oo0OOo :
    if not 'plugin.program.originwizard' in Oo0OOo :
     import time
     ii1III1iiIi = '01/01/1980'
     I1ii1iI = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o0OoO0oo0O0o ) ) )
     if I1ii1iI > ii1III1iiIi :
      IIi11IIiIi1i . write ( o0OoO0oo0O0o , o0OoO0oo0O0o [ IiiOoo0o0ooooOOo : ] )
 IIi11IIiIi1i . close ( )
 o0oOoO00o . close ( )
 if 99 - 99: I11i
 if 1 - 1: ii1ii11IIIiiI * OOooOOo * oO0o + I1ii11iIi11i
def O0OOoOooO00 ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY STREAMS[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvdHZjYXRzLnBocA==' ) ) , 1016 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SCOOBY SCRAPES[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2NyYXBlZC9jYXRzLnBocA==' ) ) , 1024 , III1iII1I1ii + 'scoob.png' , O0o0Oo , '' )
 if 89 - 89: o000O0o
 if 87 - 87: O0OOOoOoo0 % I1ii11iIi11i
def OOo000o ( ) :
 Oo0oO ( )
 i111I1 = [ '[COLOR' + II + ']SEARCH MOVIES[/COLOR]' , '[COLOR' + II + ']SEARCH SERIES[/COLOR]' , '[COLOR' + II + ']SEARCH CARTOONS[/COLOR]' , '[COLOR' + II + ']SEARCH YOUTUBE[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Search Genie[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  I1i11111i1i11 ( )
 if iI11iI1IiiIiI == 1 :
  O0o0OO0000ooo ( )
 if iI11iI1IiiIiI == 2 :
  I11I1IIiiII1 ( )
 if iI11iI1IiiIiI == 3 :
  IiIIII1iiIIi ( )
  if 37 - 37: O0OOOoOoo0
  if 33 - 33: oO0o - o0o00Oo0O - oO0o
  if 94 - 94: I1111IIi * ooOOOoO * ii / I11i . I1111IIi - I11i
  if 13 - 13: Ii1IIIi1 / I1111IIi - oO0o / Ii1IIIi1 . ooOoO0O00
  if 22 - 22: o0o00Oo0O - ooOOOoO + iiiiiiii1 . ii1ii11IIIiiI * ooOoO0O00
  if 26 - 26: iI11I1II1I1I * I11i . ooOOOoO
  if 10 - 10: iiiiiiii1 * o000O0o % I1ii11iIi11i - ooOOOoO % I1ii11iIi11i
  if 65 - 65: O0OOOoOoo0 * iI11I1II1I1I / o0o00Oo0O . ooOOOoO
  if 94 - 94: I1ii11iIi11i . I11i1ii1 * Ii - I11i . O0OOOoOoo0
def o00OOo ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']RaysRavers[/COLOR]' , '[COLOR' + II + ']QuickSilver[/COLOR]' , '[COLOR' + II + ']RadioNomy[/COLOR]' , '[COLOR' + II + ']MUSIC CHANNELS[/COLOR]' , '[COLOR' + II + ']UK RADIO[/COLOR]' , '[COLOR' + II + ']WORLD RADIO[/COLOR]' , '[COLOR' + II + ']CONCERTS[/COLOR]' , '[COLOR' + II + ']MUSIC VIDEOS[/COLOR]' , '[COLOR' + II + ']MUSIC[/COLOR]' , '[COLOR' + II + ']MUSIC SEARCH[/COLOR]' , '[COLOR' + II + ']KODIBLE AUDIO BOOKS[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Music[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   i11i1iiiII ( ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QyL2Rpci50eHQ=' ) ) )
  if iI11iI1IiiIiI == 1 :
   i11i1iiiII ( ( i11 ( 'aHR0cDovL3F1aWNrc2lsdmVyLW11c2ljLmNvbS9hZGRvbmNvcmUvVGV4dHMvaG9tZS50eHQ=' ) ) )
  if iI11iI1IiiIiI == 2 :
   Ii11III ( )
  if iI11iI1IiiIiI == 3 :
   I1Ii1i11I1I ( )
  if iI11iI1IiiIiI == 4 :
   oo0o000o0oOO0 ( ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1L3VrLmh0bWw=' ) ) )
  if iI11iI1IiiIiI == 5 :
   OOO000OOo0o0O ( )
  if iI11iI1IiiIiI == 6 :
   I111Iii1 ( ( i11 ( 'aHR0cHM6Ly93d3cucmVkZGl0LmNvbS9yL2Z1bGxjb25jZXJ0cy8=' ) ) )
  if iI11iI1IiiIiI == 7 :
   i11i ( ( i11 ( 'aHR0cDovLzE3Ni45LjE5Mi4yMjEvbXA0Lw==' ) ) )
  if iI11iI1IiiIiI == 8 :
   O0o0O00o0o ( str ( I1I1IiI1 ) + ( i11 ( 'L3ZvZC91cmxzL211c2ljLnBocA==' ) ) )
  if iI11iI1IiiIiI == 9 :
   II1IIiiI1 ( )
  if iI11iI1IiiIiI == 10 :
   O00O00 ( )
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
  if 66 - 66: I1ii11iIi11i - iI11I1II1I1I
 I1I11i ( 'movies' , 'MAIN' )
 if 9 - 9: I11i % Ii1I . Ii1I
def IiIIIIii11i ( ) :
 Oo0oO ( )
 if oo00 . getSetting ( 'Simplify' ) == 'true' :
  i111I1 = [ '[COLOR' + II + ']KILL KODI[/COLOR]' , '[COLOR' + II + ']SPEEDTEST[/COLOR]' , '[COLOR' + II + ']VIEW LOG FILE[/COLOR]' , '[COLOR' + II + ']DELETE CACHE[/COLOR]' , '[COLOR' + II + ']DELETE PACKAGES[/COLOR]' , '[COLOR' + II + ']FORCE REFRESH[/COLOR]' , '[COLOR' + II + ']CHECK MY IP[/COLOR]' , '[COLOR' + II + ']ANDROID ONLY DELETE TEXTURE13.DB&THUBMNAIL FOLDER[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Maintenance[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   oO0OOO00 ( )
  if iI11iI1IiiIiI == 1 :
   IiIi1I1 ( )
  if iI11iI1IiiIiI == 2 :
   iIiIi11 ( )
  if iI11iI1IiiIiI == 3 :
   I1iIiI1iiiiI1 ( oOooO0 )
  if iI11iI1IiiIiI == 4 :
   IIII1ii1 ( oOooO0 )
  if iI11iI1IiiIiI == 5 :
   oOOo0O00o ( )
  if iI11iI1IiiIiI == 6 :
   OOO0O0OOo ( url = 'http://www.iplocation.net/' , inc = 1 )
  if iI11iI1IiiIiI == 7 :
   Iii1 ( )
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
  if 96 - 96: I1ii11iIi11i / o000O0o . IIiIiII11i . I1ii11iIi11i
  if 91 - 91: IIiIiII11i . Ii1IIIi1 + I11i
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
def ooo00Ooo ( ) :
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
def O00Ooo0O0OOOo ( ) :
 Oo0oO ( )
 i111I1 = [ '[COLOR' + II + ']SKINS[/COLOR]' , '[COLOR' + II + ']ARTWORK PACKS[/COLOR]' , '[COLOR' + II + ']CREATE UNIVERSAL PATHS[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  o0oooo0O ( )
 if iI11iI1IiiIiI == 0 :
  iI1iIIIIIiIi1 ( oOooO0 )
 if iI11iI1IiiIiI == 0 :
  iIioOo ( oOooO0 )
  if 66 - 66: IIiIiII11i + oO0o
  if 19 - 19: oO0o . ii * oO0o + I1111IIi + ii
  if 19 - 19: I1ii11iIi11i
 I1I11i ( 'movies' , 'MAIN' )
 if 75 - 75: ii . Ii1IIIi1 + oO0o / ii1ii11IIIiiI - oOo0O0Ooo % ii1ii11IIIiiI
def O0OooooO0o0O0 ( ) :
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXgucGhwL2d0di1pcHR2' ) )
 i1IIIII11I1IiI = re . compile ( ' src="([^"]*)".+?><br />(.+?)</span></li>' , re . DOTALL ) . findall ( i1i )
 for ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&amp;' , '&' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , ' ' ) . replace ( '</span><span style="margin: 0px; padding: 0px;">' , ' ' ) , '' , '' , ii1iii1i , ii1iii1i , '' )
 I1I11i ( 'tvshows' , 'INFO' )
 if 74 - 74: OOooOOo / ooOoO0O00 % ii
def o00o0o000Oo ( url ) :
 i1i = OoOooO ( Oooo00OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 5 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 6 - 6: o000O0o / oOo0O0Ooo / OOooOOo
def o0oooo0O ( ) :
 Oo0oO ( )
 iiOOooooO0Oo ( '[COLOR' + II + ']GOTHAM SKINS[/COLOR]' , str ( I1I1IiI1 ) , 36 , III1iII1I1ii + 'GothamSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']HELIX SKINS[/COLOR]' , str ( I1I1IiI1 ) , 37 , III1iII1I1ii + 'HelixSkins.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']ISENGAARD SKINS[/COLOR]' , Oo0o0000o0o0 , 38 , III1iII1I1ii + 'IsengaardSkins.png' , O0o0Oo , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 51 - 51: IIiIiII11i / I1ii11iIi11i / oOo0O0Ooo + Ii
def iiI1ii1Iii ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + Ii1I1IIIiI1i ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 75 - 75: Ii1I
def O00o ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o0o0ooOo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 91 - 91: oO0o * iiiiiiii1 % oO0o . I11i * Ii1I . Ii1IIIi1
def i111I111 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + I1Iiii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 22 - 22: ii1ii11IIIiiI * ooOOOoO + oOo0O0Ooo - ooOOOoO / Ii1I
def iii1 ( url ) :
 i1i = OoOooO ( i11 ( 'aHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3MvN2ZrMjhndDlwb3QxMjJhL0JVSUxEUy50eHQ/ZGw9MA==' ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 93 - 93: o000O0o % ooOoO0O00
def iI1iIIIIIiIi1 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + OOo0OOoo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 40 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 22 - 22: I11i1ii1 / I11i1ii1 - ii1ii11IIIiiI % ooOOOoO . Ii1IIIi1 + I1111IIi
def OooO00oo0O0 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + i1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 5 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 73 - 73: ii . I1ii11iIi11i / o0o00Oo0O - o0o00Oo0O
def Ii1I1i ( ) :
 i111I1 = [ '[COLOR' + II + ']GenieTv Apps[/COLOR]' , '[COLOR' + II + ']APK Factory[/COLOR]' , '[COLOR' + II + ']APK Search[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']APK TOOL[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  IiI11IIi11Iii ( )
 if iI11iI1IiiIiI == 1 :
  ii11i1I1i ( )
 if iI11iI1IiiIiI == 2 :
  Iiiii1I ( )
  if 13 - 13: IIiIiII11i . O0OOOoOoo0 - iiiiiiii1 . oO0o . iI11I1II1I1I
  if 66 - 66: I1ii11iIi11i * I1111IIi
  if 83 - 83: ii
  if 12 - 12: I11i1ii1
def ii11i1I1i ( ) :
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cHM6Ly93d3cuYXBrZmlsZXMuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">Applications(.+?)</a>' ) . findall ( oooO )
 i1I = re . compile ( 'href="([^"]*)">Games(.+?)</a>' ) . findall ( oooO )
 for oOooO0 , I11OOO0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( 'Android Apps' + I11OOO0 , 'https://www.apkfiles.com' + oOooO0 , 30035 , III1iII1I1ii + 'apps.png' )
 for oOooO0 , I11OOO0 in i1I :
  O0Oo00OoOo ( 'Android Games' + I11OOO0 , 'https://www.apkfiles.com' + oOooO0 , 30035 , III1iII1I1ii + 'GAMES.png' )
 I1I11i ( 'movies' , 'MAIN' )
def I1Ii1 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if '/cat' in url :
   O0Oo00OoOo ( ( Iii1I1111ii ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def O0oo0oOoO00 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" >(.+?)</a>' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if '/app' in url :
   O0Oo00OoOo ( ( Iii1I1111ii ) . replace ( '&amp;' , ' - ' ) , 'https://www.apkfiles.com' + url , 30037 , III1iII1I1ii + 'APK.png' )
def i1ii1iIi ( url ) :
 oooO = OoOooO ( url )
 oO00oOOo0Oo = url
 if "page=" in str ( url ) :
  oO00oOOo0Oo = url . split ( '?' ) [ 0 ]
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?<img src="([^"]*)" class="file_list_icon".+?alt="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( 'class="[^"]*".+?ref="([^"]*)".+?yle=.+?</a>' ) . findall ( oooO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  if 'apk' in url :
   OOiIiIIi1 ( ( Iii1I1111ii ) . replace ( '&#39;' , '' ) . replace ( '&amp;' , ' - ' ) . replace ( '&#174;:' , ': ' ) . replace ( '&#174;' , ' ' ) , 'https://www.apkfiles.com' + url , 80004 , 'http:' + ii1iii1i )
 if len ( i1I ) > 1 :
  i1I = str ( i1I [ len ( i1I ) - 1 ] )
 OOiIiIIi1 ( 'Next Page' , oO00oOOo0Oo + str ( i1I ) , 30037 , III1iII1I1ii + 'Next.png' )
def I1I1Ii ( name , url ) :
 oooO = ii1Oo0000oOo ( url )
 name = name
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" class="yellow_button"  title=' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  url = 'https://www.apkfiles.com' + url
  iI1IIII1 ( name , url , 'Brackets' )
def Iiiii1I ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0000o0Oo = 'https://www.apkfiles.com/search?q=' + ( oo00O0 ) . replace ( ' ' , '+' ) + '&search_type=1'
 iiiI111I = o0000o0Oo . lower ( )
 i1ii1iIi ( iiiI111I )
 if 75 - 75: Ii / Ii * I11i1ii1 - o0o00Oo0O * oOo0O0Ooo
def Ooo000o0oo0 ( url ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( o0Ii11iIiiI , 'Download' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your App Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oooooo0O000o = os . path . join ( O0O00Oo , Iii1I1111ii + '.apk' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, exit kodi and go to your downloads folder to install your app[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 82 - 82: ii
def OoOO00oo0o ( url ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons/plugin.video.GenieTv/resources/downloads' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your fILM Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oooooo0O000o = os . path . join ( O0O00Oo , Iii1I1111ii + '.mp4' )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Please press ok, Your download With Be Avaiilable Via The My Downloads Button[/COLOR]" , "[COLORblue]Tool Brought To You By GenieTv[/COLOR]" )
 if 76 - 76: O0OOOoOoo0 . I1111IIi % O0OOOoOoo0 - iiiiiiii1
 if 51 - 51: ii + I11i * iI11I1II1I1I * o000O0o / ooOoO0O00
def I11IiI1i ( name , url , description ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( "Your Art Pack Is Downloading" , "Why not check out our website" , '' , 'Http://GenieTv.co.uk' )
 oooooo0O000o = os . path . join ( O0O00Oo , name )
 try :
  os . remove ( oooooo0O000o )
 except :
  pass
 downloader . download ( url , oooooo0O000o , o0oOoO00o )
 OooO = xbmc . translatePath ( os . path . join ( o00 ) )
 time . sleep ( 2 )
 o0oOoO00o . update ( 0 , "" , "Placing Your Art Please Wait" )
 print '======================================='
 print OooO
 print '======================================='
 extract . all ( oooooo0O000o , OooO , o0oOoO00o )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , "[COLORred]Once complete your artwork will be stored in your Media folder, Accessible via the Homefolder, Enjoy[/COLOR]" )
 if 85 - 85: IIiIiII11i
 if 55 - 55: Ii1I
 if 76 - 76: o000O0o - Ii
 if 27 - 27: Ii1I - Ii % iiiiiiii1 / I1ii11iIi11i . I1ii11iIi11i / ii
 if 76 - 76: ooOOOoO * oO0o . iI11I1II1I1I % ii % Ii1I
def IiI11IIi11Iii ( ) :
 i1i = OoOooO ( ii11iIi1I ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i1i )
 for Iii1I1111ii , oOooO0 , ooOoOo0 , I11iiiiI1i , IiiI1i111I1i in i1IIIII11I1IiI :
  OOiIiIIi1 ( Iii1I1111ii , oOooO0 , 80003 , ooOoOo0 , III1iII1I1ii + 'APKToolsB.png' , IiiI1i111I1i )
def OO0O0OO0O0 ( apk , ret = None ) :
 if apk == "kodi" :
  oOoo = "https://kodi.tv/download/"
  i1i = OoOooO ( oOoo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( "<h2>Current release:.+?odi v(.+?) &#8220;(.+?)&#8221;</h2>" ) . findall ( i1i )
  if len ( i1IIIII11I1IiI ) == 1 :
   oo0O00ooo0o = i1IIIII11I1IiI [ 0 ] [ 0 ]
   I1iII = i1IIIII11I1IiI [ 0 ] [ 1 ]
   ii1i1Iii = "http://mirrors.kodi.tv/releases/android/arm/kodi-%s-%s-armeabi-v7a.apk" % ( oo0O00ooo0o , I1iII )
  if ret == 'version' : return oo0O00ooo0o
  else : return ii1i1Iii
 elif apk == "spmc" :
  oO00oO00O0Oo = 'https://github.com/koying/SPMC/releases/latest/'
  i1i = OoOooO ( oO00oO00O0Oo ) . replace ( '\n' , '' ) . replace ( '\r' , '' ) . replace ( '\t' , '' )
  i1IIIII11I1IiI = re . compile ( ".+?class=\"release-title\">(.+?)</h1>.+?" ) . findall ( i1i )
  oo0O00ooo0o = re . sub ( '<[^<]+?>' , '' , i1IIIII11I1IiI [ 0 ] ) . replace ( ' ' , '' )
  ii1i1Iii = 'https://github.com/koying/SPMC/releases/download/%s-spmc/SPMC-armeabi-v7a_%s.apk' % ( oo0O00ooo0o , oo0O00ooo0o )
  if ret == 'version' : return oo0O00ooo0o
  else : return ii1i1Iii
def iI1IIII1 ( name , url , Brackets ) :
 if I1IIII1i ( ) == 'android' :
  OO0o0o0oo = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not OO0o0o0oo : iIiII1 ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' ) ; return
  i111iii1I1 = name
  if OO0o0o0oo :
   if not os . path . exists ( i1iiIII111ii ) : os . makedirs ( i1iiIII111ii )
   if not ooo0O0o00O ( url ) == True : iIiII1 ( oO , 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % i111iii1I1 , '' , 'Please Wait' )
   oooooo0O000o = os . path . join ( i1iiIII111ii , "%s.apk" % name )
   try : os . remove ( oooooo0O000o )
   except : pass
   downloader . download ( url , oooooo0O000o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   if "Brackets" in Brackets :
    oO0O0 = zipfile . ZipFile ( oooooo0O000o )
    for file in oO0O0 . namelist ( ) :
     if file . endswith ( '.apk' ) :
      with open ( os . path . join ( i1iiIII111ii , os . path . basename ( file ) ) , 'wb' ) as OOoO :
       iiIiII1 = file . split ( '/' ) [ 1 ]
       OOoO . write ( oO0O0 . read ( file ) )
       xbmc . sleep ( 500 )
       OOoO . close ( )
       try :
        os . remove ( oooooo0O000o )
       except :
        pass
       oooooo0O000o = os . path . join ( i1iiIII111ii , iiIiII1 )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oooooo0O000o + '")' )
  else : iIiII1 ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIiII1 ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 37 - 37: o0o00Oo0O + I11i1ii1 * Ii1IIIi1
 if 27 - 27: o0o00Oo0O . IIiIiII11i + I1111IIi % I11i
 if 67 - 67: o0o00Oo0O % iiiiiiii1
 if 35 - 35: oOo0O0Ooo . OOooOOo + ii % I1ii11iIi11i % Ii1IIIi1
def iIi1Ii1111i ( ) :
 if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
 i1i = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?).apk</a></td>' ) . findall ( i1i )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  oOooO0 = ( ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvVGhlSHViLw==' ) ) + oOooO0 )
  i1iooO0oO0o ( ( Iii1I1111ii ) . replace ( '_' , ' ' ) , oOooO0 )
  if 22 - 22: I11i + I1ii11iIi11i . I11i1ii1 + Ii1I * O0OOOoOoo0 . Ii
def i1iooO0oO0o ( name , url ) :
 if I1IIII1i ( ) == 'android' :
  OO0o0o0oo = OOooO0OOoo . yesno ( oO , "Would you like to download and install:" , "%s" % name )
  if not OO0o0o0oo : iIiII1 ( oO , '[COLOR blue]OOOoooh:[/COLOR] Have A Nice Day' ) ; return
  i111iii1I1 = name
  if OO0o0o0oo :
   if not os . path . exists ( i1iIIi1 ) : os . makedirs ( i1iIIi1 )
   if not ooo0O0o00O ( url ) == True : iIiII1 ( oO , 'HUB Installer: [COLOR red]Invalid Apk Url![/COLOR]' ) ; return
   o0oOoO00o . create ( oO , 'Downloading %s' % i111iii1I1 , '' , 'Please Wait' )
   oooooo0O000o = os . path . join ( i1iIIi1 , "%s.apk" % name )
   try : os . remove ( oooooo0O000o )
   except : pass
   downloader . download ( url , oooooo0O000o , o0oOoO00o )
   xbmc . sleep ( 500 )
   o0oOoO00o . close ( )
   OOooO0OOoo . ok ( oO , "Launching the APK to be installed" , "Follow the install process to complete." )
   xbmc . executebuiltin ( 'StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:' + oooooo0O000o + '")' )
  else : iIiII1 ( oO , '[COLOR red]ERROR:[/COLOR] Install Cancelled' )
 else : iIiII1 ( oO , '[COLOR red]ERROR:[/COLOR] None Android Device' )
 if 90 - 90: Ii1IIIi1 * OOooOOo - I1ii11iIi11i + I11i
 if 53 - 53: ii . ii + I11i - O0OOOoOoo0 + Ii1IIIi1
def i1111iIII ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC50eHQ=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 5 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'INFO' )
 if 50 - 50: o0o00Oo0O * Ii1I + IIiIiII11i . ooOoO0O00 + OOooOOo
 if 39 - 39: iI11I1II1I1I + I11i1ii1
def I1i11OO ( url ) :
 i1i = OoOooO ( I1I1IiI1 + ( i11 ( 'L0dlbmllVHYvdGVzdC93aC54bWw=' ) ) ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 30015 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 92 - 92: ooOOOoO % Ii % I1ii11iIi11i
def ii11Ii1IiiI1 ( url , iconimage , fanart ) :
 i1i = OoOooO ( url )
 I1i = url
 ii1iii1i = iconimage
 fanart = fanart
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for I11iiii1I , Iii1I1111ii in i1IIIII11I1IiI :
  if '.mp4' in Iii1I1111ii :
   OOiIiIIi1 ( 'Watch VIDEO' , url + '/' + I11iiii1I , 222 , ii1iii1i , fanart , '' )
  if 'description' in Iii1I1111ii :
   OOiIiIIi1 ( 'Read Description' , url + '/' + I11iiii1I , 30017 , ii1iii1i , fanart , '' )
  if 'images' in Iii1I1111ii :
   iiOOooooO0Oo ( 'View Images' , url + '/' + I11iiii1I , 30018 , ii1iii1i , fanart , '' )
  if 'url' in Iii1I1111ii :
   OOiIiIIi1 ( 'Install Build On Android' , url + '/' + I11iiii1I , 30016 , ii1iii1i , fanart , '' )
  if 'url' in Iii1I1111ii :
   OOiIiIIi1 ( 'Install Build On Pc' , url + '/' + I11iiii1I , 30019 , ii1iii1i , fanart , '' )
 I1I11i ( 'movies' , 'INFO' )
 if 83 - 83: I11i1ii1 + ooOoO0O00 * ii * o000O0o
def OoO0o0OO ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  II11IiI1 ( url )
  if 21 - 21: oO0o
def O0o0oOOO ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url="([^"]*)"' ) . findall ( i1i )
 for url in i1IIIII11I1IiI :
  IIi11 ( url )
  if 78 - 78: iiiiiiii1 / o000O0o - iI11I1II1I1I - OOooOOo
def o0oOOooo0o0O ( url ) :
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'desc="([^"]*)"' ) . findall ( i1i )
 for IiiiIIi11II in i1IIIII11I1IiI :
  iiIiI1i1 ( 'Description:' , IiiiIIi11II )
  if 55 - 55: ooOOOoO
def ooooooo00oO0OO ( url ) :
 i1i = OoOooO ( url )
 url = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( i1i )
 for I11iiii1I , Iii1I1111ii in i1IIIII11I1IiI :
  if 'png' in Iii1I1111ii :
   OOiIiIIi1 ( 'image' , '' , '' , url + '/' + I11iiii1I , url + '/' + I11iiii1I , '' )
 I1I11i ( 'movies' , 'MAIN' )
 if 30 - 30: I11i + ii + Ii1IIIi1 / IIiIiII11i * I1ii11iIi11i
def O00O0IIIIIIIiiiI ( name , url , description ) :
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
 if 59 - 59: o000O0o % I11i1ii1
 if 36 - 36: ii
def IIi11 ( url ) :
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
 oO0OOO00 ( )
 if 33 - 33: o0o00Oo0O + I1ii11iIi11i - iI11I1II1I1I % Ii / oOo0O0Ooo
def II11IiI1 ( url ) :
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
 oO0OOO00 ( )
 if 47 - 47: Ii1I * o000O0o + iI11I1II1I1I - o000O0o / I1111IIi
def oO0ooo0O0Ooo ( name , url , description ) :
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
 oO0OOO00 ( )
 if 33 - 33: IIiIiII11i - I1111IIi - I11i1ii1
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
  oO00oOoo00o0 = "[%s %s] %s" % ( datetime . now ( ) . date ( ) , str ( datetime . now ( ) . time ( ) ) [ : 8 ] , log )
  OOoO . write ( oO00oOoo00o0 . rstrip ( '\r\n' ) + '\n' )
def oO0OOO00 ( ) :
 iI11iI1IiiIiI = OOooO0OOoo . yesno ( 'Force Close Kodi' , 'You are about to close Kodi' , 'Would you like to continue?' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Close' )
 if iI11iI1IiiIiI == 0 : return
 elif iI11iI1IiiIiI == 1 : pass
 III1I = I1IIII1i ( )
 OOO ( "Platform: " + str ( III1I ) )
 os . _exit ( 1 )
 OOO ( "Force close failed!  Trying alternate methods." )
 if III1I == 'osx' :
  OOO ( "############ try osx force close #################" )
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
  OOooO0OOoo . ok ( "[COLOR=red][B]WARNING !!![/COLOR][/B]" , "If you\'re seeing this message it means the force close" , "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu." , '' )
 elif III1I == 'linux' :
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
 elif III1I == 'android' :
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
 elif III1I == 'windows' :
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
  if 85 - 85: I1ii11iIi11i . Ii - Ii . oOo0O0Ooo . oO0o % ii
  if 20 - 20: iiiiiiii1 + iiiiiiii1 * IIiIiII11i * iI11I1II1I1I % o0o00Oo0O * oOo0O0Ooo
  if 62 - 62: ii / OOooOOo . I1111IIi . I1111IIi % I11i1ii1
def iIioOo ( url ) :
 o0oOoO00o . create ( "[COLOR=green]GenieTv[/COLOR]" , "Renaming paths..." , '' , 'Please Wait' )
 for iII , Oo0OOo , i1II11I11ii1 in os . walk ( url ) :
  for file in i1II11I11ii1 :
   if file . endswith ( ".xml" ) :
    o0oOoO00o . update ( 0 , "Fixing" , file , 'Please Wait' )
    IiIi1II111I = open ( ( os . path . join ( iII , file ) ) ) . read ( )
    O0ooo = IiIi1II111I . replace ( Oo0o0000o0o0 , 'special://home/' )
    OOoO = open ( ( os . path . join ( iII , file ) ) , mode = 'w' )
    OOoO . write ( str ( O0ooo ) )
    OOoO . close ( )
 oO0OOO00 ( )
 if 9 - 9: Ii1IIIi1 * ooOoO0O00 % I11i1ii1 . o0o00Oo0O
def Ii11III ( ) :
 O0Oo00OoOo ( ( '[COLOR' + II + ']GENRE[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70002 , III1iII1I1ii + 'RadioNomy.png' )
 O0Oo00OoOo ( ( '[COLOR' + II + ']SORT BY[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbS9lbi9zdHlsZQ==' ) ) , 70003 , III1iII1I1ii + 'RadioNomy.png' )
 O0Oo00OoOo ( ( '[COLOR' + II + ']SEARCH[/COLOR]' ) , '' , 70006 , III1iII1I1ii + 'RadioNomy.png' )
 if 2 - 2: ii % iI11I1II1I1I
def I11iIiI1 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a data-style-id=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def i1I1iiii1Ii11 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
def IiIIIIi ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( 'data-style-parentid=".+?" href="([^"]*)" rel="internal">(.+?)</a>' ) . findall ( oooO )
 for url , Iii1I1111ii in i1I :
  O0Oo00OoOo ( ( '[COLOR' + II + ']Filter - ' + Iii1I1111ii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70004 , III1iII1I1ii + 'RadioNomy.png' )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( ( '[COLOR' + II + ']Stream - ' + Iii1I1111ii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + url , 70005 , ii1iii1i )
def Oo ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a class="download" href="([^"]*)' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  OOOoOO0o ( url )
def IIiIIIII1I ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0
 ooiiI = 'https://www.radionomy.com/en/search/index?query=' + ( oo00O0 ) . replace ( ' ' , '+' )
 oO0OOoo0OO = OoOooO ( ooiiI )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" rel="internal"><img class=".+?" src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( ( '[COLOR' + II + ']Stream - ' + Iii1I1111ii + '[/COLOR]' ) , ( i11 ( 'aHR0cHM6Ly93d3cucmFkaW9ub215LmNvbQ==' ) ) + oOooO0 , 70005 , ii1iii1i )
  if 72 - 72: ooOOOoO . IIiIiII11i * ooOoO0O00
  if 79 - 79: Ii1I / o0o00Oo0O % I11i
def OOO000OOo0o0O ( ) :
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cDovL3d3dy5saXN0ZW5saXZlLmV1Lw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a></td></tr>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , 'http://www.listenlive.eu/' + oOooO0 , 10111113 , III1iII1I1ii + 'radio.png' )
def oo0o000o0oOO0 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<tr>.+?<td><a href=".+?"><b>(.+?)</b>.+?<td><a href="([^"]*)">' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  ii1ii111 ( Iii1I1111ii , url , 222 , III1iII1I1ii + 'radio.png' )
  if 71 - 71: iiiiiiii1 / oOo0O0Ooo / o0o00Oo0O
def IiIii11I ( ) :
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cDovL3d3dy50b29uamV0LmNvbS8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" style="font-size:.8em;">(.+?)</a>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.toonjet.com/' + oOooO0 , 8051 , III1iII1I1ii + 'classictoons.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ooo0O00 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><img src="([^"]*)"' ) . findall ( oooO )
 i1I = re . compile ( '<a href="([^"]*)">.+?</a></td></tr></table>' ) . findall ( oooO )
 for url , ii1iii1i in i1IIIII11I1IiI :
  if 'ol.gif' in ii1iii1i :
   pass
  elif 'link_block_' in ii1iii1i :
   pass
  elif '.png' in ii1iii1i :
   pass
  else :
   O0Oo00OoOo ( ( ii1iii1i ) . replace ( 'http://www.toonjet.com/images/icons/' , '' ) . replace ( 'images/icons/' , '' ) . replace ( '.jpg' , '' ) . replace ( '_icon' , '' ) . replace ( '_' , ' ' ) , 'http://www.toonjet.com/' + url , 8052 , III1iII1I1ii + 'vod.png' )
 for url in i1I :
  O0Oo00OoOo ( 'NEXT PAGE' , 'http://www.toonjet.com/' + url , 8051 , III1iII1I1ii + 'Next.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oooo0oOOoO000 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe width="640" height="480" src="([^"]*)" frameborder="0" allowfullscreen></iframe>' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']PLAY[/COLOR]' , ( url ) . replace ( 'http://www.youtube.com/embed/' , '' ) . replace ( '?autoplay=0' , '' ) , 8043 , III1iII1I1ii + 'classictoons.png' )
  if 86 - 86: iI11I1II1I1I - ooOOOoO % I11i1ii1 . Ii1IIIi1 * OOooOOo . ooOoO0O00
  if 75 - 75: ooOOOoO + I11i1ii1 / I11i1ii1 - Ii1IIIi1 * oO0o * I11i1ii1
def O00O00 ( ) :
 oOO0o ( 'Audio Books' , '' , 30011 , III1iII1I1ii + 'AudioBooks.png' , III1iII1I1ii + 'AudioBooks.png' , '' )
 oOO0o ( 'Kids Audio Books' , '' , 30006 , III1iII1I1ii + 'KidsAudioBooks.png' , III1iII1I1ii + 'KidsAudioBooks.png' , '' )
 if 53 - 53: I1111IIi % I1ii11iIi11i
def IiIII ( ) :
 oOO0o ( 'All' , '' , 30001 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 oOO0o ( 'Popular' , '' , 30012 , III1iII1I1ii + 'POPULARv.png' , III1iII1I1ii + 'POPULARv.png' , '' )
 oOO0o ( 'Search' , '' , 30013 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'Search.png' , '' )
 if 44 - 44: ii1ii11IIIiiI * I11i1ii1 / OOooOOo
def o0Oo0ooo ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , oOooO0 , oOOoo in i1IIIII11I1IiI :
  if 'Parent' in Iii1I1111ii :
   pass
  elif '2' in oOOoo :
   oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 36 - 36: Ii1IIIi1 * ii1ii11IIIiiI
def i1iIii1II1i ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , oOooO0 , oOOoo in i1IIIII11I1IiI :
  if oo00O0 in Iii1I1111ii . lower ( ) :
   if '1' in oOOoo :
    oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '2' in oOOoo :
    oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   elif '3' in oOOoo :
    oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 27 - 27: Ii1I / Ii1IIIi1
    if 33 - 33: ii % Ii1I . o0o00Oo0O / Ii1I
def O0OoOo ( ) :
 oO0OOoo0OO = OoOooO ( oOoOooOo0o0 + 'books' + I1IIIii )
 i1IIIII11I1IiI = re . compile ( '<NAME=>(.*?)</NAME><URL=>(.*?)</URL><CAT=>(.*?)</CAT>' ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , oOooO0 , oOOoo in i1IIIII11I1IiI :
  if '1' in oOOoo :
   oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 3010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '2' in oOOoo :
   oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '3' in oOOoo :
   oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '.mp3' , '' ) , oOooO0 , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 94 - 94: oO0o + oO0o + Ii1I . oO0o * ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 62 - 62: I11i / iI11I1II1I1I
def O0OOo ( url ) :
 I11iiii1I = url
 oO0OOoo0OO = OoOooO ( url )
 i1I = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1I :
  if 'mp3' in Iii1I1111ii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I11iiii1I + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'wma' in Iii1I1111ii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I11iiii1I + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  if 'm4b' in Iii1I1111ii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) , I11iiii1I + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif '/' in Iii1I1111ii :
   oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I11iiii1I + url , 30009 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 81 - 81: o0o00Oo0O + O0OOOoOoo0 . oOo0O0Ooo - IIiIiII11i . oOo0O0Ooo + o0o00Oo0O
   if 75 - 75: o0o00Oo0O % iI11I1II1I1I / OOooOOo % Ii1IIIi1 / I1111IIi
   if 31 - 31: Ii * OOooOOo
def oOiI1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I11iiii1I = url
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Parent' in Iii1I1111ii :
   pass
  elif '.db' in Iii1I1111ii :
   pass
  elif '.jpg' in Iii1I1111ii :
   pass
  elif '.html' in Iii1I1111ii :
   pass
  elif '.doc' in Iii1I1111ii :
   pass
  elif 'mp3' in Iii1I1111ii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I11iiii1I + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  elif 'm4a' in Iii1I1111ii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I11iiii1I + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '%20' , ' ' ) . replace ( '/' , '' ) . replace ( '.mp3' , '' ) , I11iiii1I + url , 30010 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 6 - 6: oO0o
   if 99 - 99: I11i * Ii1IIIi1 % o000O0o * o000O0o + ii
def O0OO ( ) :
 oOO0o ( 'A-Z' , '' , 30007 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 oOO0o ( 'All' , '' , 30003 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 oOO0o ( 'Search' , '' , 30014 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
 if 30 - 30: OOooOOo * I1ii11iIi11i % iI11I1II1I1I % oO0o + Ii
def IiOo00O0o0O ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9tcDNfZG93bmxvYWRzLmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?" align="center">.+?<a href="(.*?)">.+?<img border="0" src="images/Squeeze%20(.*?).gif" width="74" height=".*?"></a></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , ii1iii1i in i1IIIII11I1IiI :
  print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<' + oOooO0 + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
  if '-x' in ii1iii1i :
   pass
  else :
   oOO0o ( ii1iii1i , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) ) + ( oOooO0 ) . replace ( 'colour_it' , 'books_audio/audio_books_a' ) , 30008 , ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9pbWFnZXMvU3F1ZWV6ZSUyMA==' ) ) + ii1iii1i + '.gif' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 86 - 86: ooOOOoO + o0o00Oo0O + I1ii11iIi11i - ooOOOoO
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 34 - 34: IIiIiII11i % oOo0O0Ooo % iiiiiiii1 + I1ii11iIi11i - OOooOOo
 if 66 - 66: ii1ii11IIIiiI * iI11I1II1I1I - I11i1ii1 / oOo0O0Ooo
def o0i1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width=".*?" height=".*?"><b>.*?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if '</a>' in Iii1I1111ii :
   pass
  elif '(' in Iii1I1111ii :
   oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 76 - 76: ooOOOoO % I1111IIi / I1111IIi / oO0o % o000O0o . iI11I1II1I1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 85 - 85: ii1ii11IIIiiI
def Oo0O0OooOooo0 ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if oo00O0 in Iii1I1111ii . lower ( ) :
   if '</a>' in Iii1I1111ii :
    pass
   elif '(' in Iii1I1111ii :
    oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   else :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
    if 81 - 81: o000O0o - Ii1IIIi1
    if 21 - 21: I1ii11iIi11i * I11i + ii . iiiiiiii1 % o000O0o
def IIIIIiiI ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9jb21wbGV0ZV9saXN0Lmh0bQ==' ) )
 i1IIIII11I1IiI = re . compile ( '<td width=".+?">.*?<b>.+?<a href="(.*?)">(.*?)</a></b></td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if '</a>' in Iii1I1111ii :
   pass
  elif '(' in Iii1I1111ii :
   oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30005 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) . replace ( '  ' , '' ) . replace ( '+' , '' ) . replace ( '.mp3' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay8=' ) + oOooO0 , 30004 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 38 - 38: o0o00Oo0O
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 79 - 79: ooOoO0O00 . o000O0o
 if 34 - 34: iiiiiiii1 * IIiIiII11i
def o0oO00OOo0oO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">Download</a></b></td>' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  I11iiii1I = ( i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) ) + url
  Resolve ( I11iiii1I )
  if 92 - 92: oOo0O0Ooo . IIiIiII11i
def II1Ooo0000o00OO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td width="247">(.*?)</td>.*?<a href="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  if '<p align' in Iii1I1111ii :
   pass
  elif '&nbsp;' in Iii1I1111ii :
   pass
  else :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , '' ) , i11 ( 'aHR0cDovL3d3dy5raWRzYXVkaW9ib29rcy5jby51ay9ib29rc19hdWRpby8=' ) + url , 222 , III1iII1I1ii + 'KodibleAudioBooks.png' , III1iII1I1ii + 'KodibleAudioBooks.png' , '' )
   if 9 - 9: IIiIiII11i * Ii . Ii1IIIi1 - oO0o
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 31 - 31: Ii * ii1ii11IIIiiI . I11i % Ii1IIIi1 * Ii1I % o0o00Oo0O
 if 77 - 77: oO0o + oO0o . I11i1ii1 * ii + oO0o
def IIIIIii1ii11 ( ) :
 oO0OOoo0OO = cloudflare . source ( i11 ( 'aHR0cDovL3dhdGNoY2FydG9vbnNvbmxpbmUuZXUv' ) )
 i1IIIII11I1IiI = re . compile ( 'class="menu-item menu-item-type-.+?><a href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'ongoing' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'OnGoing.png' , '' , '' )
  if 'cartoon-series' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'CartoonShows.png' , '' , '' )
  if 'disney' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'Disney.png' , '' , '' )
  if 'genre' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'Genre.png' , '' , '' )
  if 'years' in oOooO0 :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 21005 , III1iII1I1ii + 'Years.png' , '' , '' )
def ii111I1i1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)" rel="nofollow" id="featured-thumbnail">.+?<div class="featured-thumbnail"><img width="140" height="200" src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 oooIiII = re . compile ( '<button type="button"><a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 21006 , ii1iii1i , ii1iii1i , Iii1I1111ii )
 for url , Iii1I1111ii in oooIiII :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in next :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 21005 , III1iII1I1ii + 'Next.png' , '' , '' )
def iII1I ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" target=_blank>(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 OOo00O = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o00oOOo0Oo = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oO0OOoo0OO )
 Oooo0o0oO = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#8217;' , '' ) , url , 21007 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url in o00oOOo0Oo :
  iiOOooooO0Oo ( '[COLOR' + II + ']PLAY[/COLOR]' , 'http:' + url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 for url , Iii1I1111ii in OOo00O :
  OOiIiIIi1 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
 else :
  iiOOooooO0Oo ( '[COLOR' + II + ']NO STREAMS AVAILABLE[/COLOR]' , url , 21005 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
def o0OOoOooO0ooO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file:"([^"]*)",type:"mp4",label:"([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 222 , III1iII1I1ii + 'watchcartoons.png' , '' , '' )
  if 50 - 50: Ii + ii / o0o00Oo0O + I11i / Ii + o000O0o
def oOoOOOo ( ) :
 oO0OOoo0OO = cloudflare . source ( 'http://9cartoon.me/CartoonList' )
 i1IIIII11I1IiI = re . compile ( '<a style="width:auto;padding: 4px 10px;" href="([^"]*)" rel="all".+?>(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if '9cart' in oOooO0 :
   O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 20001 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 90 - 90: O0OOOoOoo0 * ii1ii11IIIiiI - O0OOOoOoo0 + oO0o + ooOOOoO % o0o00Oo0O
def i111IIIIiI ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" rel="all" class="active">All</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)" rel="0" class="">#</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iiI1IIIi = re . compile ( '<li class="first-char"><a  href="([^"]*)">(.+?)</a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if '9cart' in url :
   O0Oo00OoOo ( '[COLOR' + II + ']ALL[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url in i1I :
  if '9cart' in url :
   O0Oo00OoOo ( '[COLOR' + II + ']123[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
 for url , Iii1I1111ii in iiI1IIIi :
  if '9cart' in url :
   O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 75 - 75: Ii . I11i1ii1 % ooOoO0O00 . oOo0O0Ooo - o000O0o + I1ii11iIi11i
def OOoOoooOOO0 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumnail_tool"><img src="([^"]*)".+?class="bigChar" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<a href="([^"]*)"><span>(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , url , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 20003 , ii1iii1i )
 for url , Iii1I1111ii in i1I :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&raquo;' , 'Next' ) , url , 20002 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 49 - 49: o0o00Oo0O / IIiIiII11i * oOo0O0Ooo - ii . IIiIiII11i % I1111IIi
def IIii1Ii1i1ii1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'Watch' in url :
   O0Oo00OoOo ( ( url ) . replace ( 'http://9cartoon.me/Watch/' , '' ) . replace ( '/' , ' ' ) . replace ( '-' , ' ' ) , url , 20004 , III1iII1I1ii + 'ORIGINCARTOON.png' )
   if 86 - 86: o000O0o % o0o00Oo0O + oO0o
def oO0OO ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" target="_blank" rel="nofollow">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 20005 , III1iII1I1ii + 'ORIGINCARTOON.png' )
  if 88 - 88: oOo0O0Ooo
def oOO0Oo ( url ) :
 url = cloudflare . source ( url )
 ii1O0ooooo000 ( url )
 if 5 - 5: Ii * O0OOOoOoo0 - ii1ii11IIIiiI - Ii1I - ooOoO0O00 + O0OOOoOoo0
def I1ii1i ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . recompile ( 'src="([^"]*)"' )
 for url in i1IIIII11I1IiI :
  ii1O0ooooo000 ( url )
  if 51 - 51: oO0o - O0OOOoOoo0 % o0o00Oo0O - OOooOOo
  if 53 - 53: O0OOOoOoo0 / ooOoO0O00 / ooOoO0O00
def OOOooo0OooOoO ( ) :
 if 77 - 77: ooOOOoO + ooOoO0O00 . ooOOOoO
 iiOOooooO0Oo ( '[COLOR' + II + ']Cartoons[/COLOR]' , i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) , 10004 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Cartoons[/COLOR]' , '' , 10005 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 if 89 - 89: I11i + Ii1IIIi1 * o000O0o
def I11I1IIiiII1 ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5hbmltZXRvb24ub3JnL2NhcnRvb24=' ) )
 if 45 - 45: O0OOOoOoo0 - I11i . ii1ii11IIIiiI
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oO0OOoo0OO )
 if 41 - 41: IIiIiII11i . oOo0O0Ooo / oO0o . I11i1ii1
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if oo00O0 in Iii1I1111ii . lower ( ) :
   if 'Dad!' in Iii1I1111ii :
    pass
   elif 'Family Guy' in Iii1I1111ii :
    pass
   elif '2 Stupid' in Iii1I1111ii :
    pass
   elif 'The Zelfs' in Iii1I1111ii :
    pass
   elif 'A Clone' in Iii1I1111ii :
    pass
   elif 'A.T.O.M' in Iii1I1111ii :
    pass
   elif 'Almost Naked' in Iii1I1111ii :
    pass
   elif 'Angry Kid' in Iii1I1111ii :
    pass
   elif 'Annoying Orange' in Iii1I1111ii :
    pass
   elif 'Aqua Teen' in Iii1I1111ii :
    pass
   elif 'Assy Mcgee' in Iii1I1111ii :
    pass
   elif 'Astroblast' in Iii1I1111ii :
    pass
   elif 'Atomic Betty' in Iii1I1111ii :
    pass
   elif 'Axe Cop' in Iii1I1111ii :
    pass
   elif 'Baby Playpen' in Iii1I1111ii :
    pass
   elif 'Beavis and Butt' in Iii1I1111ii :
    pass
   elif 'Celebrity Deathmatch' in Iii1I1111ii :
    pass
   elif 'Clerks The' in Iii1I1111ii :
    pass
   elif 'Crapston Villas' in Iii1I1111ii :
    pass
   elif 'Duckman:' in Iii1I1111ii :
    pass
   elif 'Stripperella' in Iii1I1111ii :
    pass
   elif 'Vixen' in Iii1I1111ii :
    pass
   else :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
    if 58 - 58: I1111IIi % Ii * IIiIiII11i . Ii1I
    if 94 - 94: Ii . Ii1IIIi1 + iI11I1II1I1I * iiiiiiii1 * iiiiiiii1
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 36 - 36: ooOOOoO - I1111IIi . I1111IIi
def ii1I ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Dad!' in Iii1I1111ii :
   pass
  elif 'Family Guy' in Iii1I1111ii :
   pass
  elif '2 Stupid' in Iii1I1111ii :
   pass
  elif 'The Zelfs' in Iii1I1111ii :
   pass
  elif 'A Clone' in Iii1I1111ii :
   pass
  elif 'A.T.O.M' in Iii1I1111ii :
   pass
  elif 'Almost Naked' in Iii1I1111ii :
   pass
  elif 'Angry Kid' in Iii1I1111ii :
   pass
  elif 'Annoying Orange' in Iii1I1111ii :
   pass
  elif 'Aqua Teen' in Iii1I1111ii :
   pass
  elif 'Assy Mcgee' in Iii1I1111ii :
   pass
  elif 'Astroblast' in Iii1I1111ii :
   pass
  elif 'Atomic Betty' in Iii1I1111ii :
   pass
  elif 'Axe Cop' in Iii1I1111ii :
   pass
  elif 'Baby Playpen' in Iii1I1111ii :
   pass
  elif 'Beavis and Butt' in Iii1I1111ii :
   pass
  elif 'Celebrity Deathmatch' in Iii1I1111ii :
   pass
  elif 'Clerks The' in Iii1I1111ii :
   pass
  elif 'Crapston Villas' in Iii1I1111ii :
   pass
  elif 'Duckman:' in Iii1I1111ii :
   pass
  elif 'Stripperella' in Iii1I1111ii :
   pass
  elif 'Vixen' in Iii1I1111ii :
   pass
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 10006 , III1iII1I1ii + 'ORIGINCARTOON.png' , O0o0Oo , '' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 60 - 60: Ii * I1ii11iIi11i % oO0o + oO0o
def ooo000o ( url ) :
 oooO = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oooO )
 for ii1iii1i in i1I :
  OOOOOO = ii1iii1i
 iiI1IIIi = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( oooO )
 for url in iiI1IIIi :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , url , 10006 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 10007 , OOOOOO )
  if 95 - 95: IIiIiII11i
  if 35 - 35: Ii1I * oO0o * oOo0O0Ooo / ii
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 15 - 15: I11i1ii1 % I11i / o000O0o - IIiIiII11i . iI11I1II1I1I
def ii1111Iii11i ( url , IMAGE ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  print Iii1I1111ii + '     ' + url
  if 'easy' in url :
   O0o0oo0O ( url )
   if 74 - 74: IIiIiII11i % ooOOOoO . oO0o * oO0o
   if 27 - 27: ooOOOoO * I1ii11iIi11i . ii1ii11IIIiiI . oOo0O0Ooo % IIiIiII11i - o000O0o
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 52 - 52: oOo0O0Ooo % oO0o * ii1ii11IIIiiI * O0OOOoOoo0 / Ii1IIIi1
def O0o0oo0O ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  OOOoOO0o ( url )
  if 88 - 88: o000O0o
  if 1 - 1: I1ii11iIi11i
  if 95 - 95: ii / ooOOOoO % ii / I11i1ii1 * I1111IIi
def oOiiIIIII ( ) :
 if 19 - 19: IIiIiII11i / OOooOOo
 iiOOooooO0Oo ( '[COLOR' + II + ']Stand Up[/COLOR]' , '' , 10014 , III1iII1I1ii + 'StandUp.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Comedian[/COLOR]' , '' , 10015 , III1iII1I1ii + 'SearchComedian.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Others[/COLOR]' , '' , 10017 , III1iII1I1ii + 'Others.png' , O0o0Oo , '' )
 if 80 - 80: OOooOOo + iI11I1II1I1I . I1111IIi
def ooOoOoo000O0O ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL2JhY2syYmFzaWNzYnVpbGQuY28udWsvdGVzdC9zdGFuZHVwbGlzdC5waHA=' ) ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  if 'elete' in Iii1I1111ii :
   pass
  else :
   ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 222 , ii1iii1i )
   if 42 - 42: I11i / I1111IIi
def oooOOO0o0O0 ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iiiI1IiI = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , Ii111IIIIii , i1iII1IiiIiI1 in iiiI1IiI :
  for oo00O0 in Ii111IIIIii :
   print '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< img >>>>>>>>>>>>>>>>>>>>>>>>>>'
   O00oIii1iIIiii1ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
   for oOooO0 , Iii1I1111ii in O00oIii1iIIiii1ii :
    if 'tube' in oOooO0 :
     pass
    elif 'stage' in oOooO0 :
     ii1ii111 ( '[COLOR' + II + ']' + Ii111IIIIii + '   -   ' + Iii1I1111ii + '[/COLOR]' , ( oOooO0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ii1iii1i , )
    elif 'vee' in oOooO0 :
     pass
     if 13 - 13: iI11I1II1I1I - IIiIiII11i % o0o00Oo0O . ii1ii11IIIiiI % oO0o
def Ii11iIiiI ( ) :
 oO0OOoo0OO = OoOooO ( ( i11 ( 'aHR0cDovL3d3dy5jb3VjaHRyaXBwZXIuY29tL2ZvcnVtMi9wYWdlLnBocD9wYWdlPTM=' ) ) )
 iiiI1IiI = re . compile ( '<tr>.+?<td width=".+?" align=".+?">.+?<img border=".+?" src="..(.+?)" width=".+?" height=".+?"></td>.+?<td width=".+?" valign=".+?" align=".+?"><font size=".+?">(.+?)</font></td>.+?<td width=".+?">(.+?)</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , Ii111IIIIii , i1iII1IiiIiI1 in iiiI1IiI :
  O00oIii1iIIiii1ii = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( i1iII1IiiIiI1 )
  for oOooO0 , Iii1I1111ii in O00oIii1iIIiii1ii :
   if 'tube' in oOooO0 :
    pass
   elif 'stage' in oOooO0 :
    ii1ii111 ( '[COLOR' + II + ']' + Ii111IIIIii + '   -   ' + Iii1I1111ii + '[/COLOR]' , ( oOooO0 ) . replace ( '" target="_blank' , '' ) , 10016 , 'http://couchtripper.com/' + ii1iii1i )
   elif 'vee' in oOooO0 :
    pass
    if 3 - 3: IIiIiII11i / Ii1IIIi1
    if 48 - 48: I11i1ii1 . Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 49 - 49: ooOoO0O00 - OOooOOo . I1ii11iIi11i + iI11I1II1I1I - I11i1ii1 / I1ii11iIi11i
def IiI1iII1II111 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 print '>>>>>>>>>>>>>>>>>>>>>>>>' + url + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 IIiI11i1111Ii = re . compile ( "url\[.+?\] = '(.+?)';" ) . findall ( oO0OOoo0OO )
 print '>>>>>>>>>>>>>>>>>>>>>>>' + ( str ( IIiI11i1111Ii ) ) + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
 for url in IIiI11i1111Ii :
  i1iiiIii11 ( ( url ) . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '\'' , '' ) )
  if 24 - 24: o000O0o - O0OOOoOoo0 / I11i1ii1
  if 10 - 10: OOooOOo * ooOoO0O00
  if 15 - 15: ooOOOoO + ooOoO0O00 - IIiIiII11i % oOo0O0Ooo
  if 34 - 34: oOo0O0Ooo
  if 57 - 57: Ii1IIIi1 . ii1ii11IIIiiI % I11i
  if 32 - 32: ooOOOoO / I1111IIi - o0o00Oo0O * iI11I1II1I1I
  if 70 - 70: ii % ii % oO0o
def I1iii11 ( ) :
 if 98 - 98: oO0o
 I1IIiIi ( '[COLOR darkgoldenrod]Open Pandora\'s Box[/COLOR]' , '' , 10029 , 'https://encrypted-tbn1.gstatic.com/images?q=tbn%3AANd9GcTQ9r4TA8yIw9ggxuwsHxWojo6tPVfgTe8QIOxOQwzNR2TavtCi6Q' , O0o0Oo , '' )
 I1IIiIi ( '[COLOR darkgoldenrod]Search[/COLOR]' , '' , 10026 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 93 - 93: o000O0o - Ii1IIIi1 + I11i . o000O0o / ooOOOoO
 I1I11i ( 'movies' , 'MAIN' )
 if 52 - 52: iiiiiiii1 + iiiiiiii1
def OO0 ( ) :
 I1IIiIi ( 'Search Pandoras Films' , '' , 10027 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 I1IIiIi ( 'Search Pandoras TV' , '' , 10028 , 'http://icons.iconarchive.com/icons/icontexto/search/256/search-red-dark-icon.png' , O0o0Oo , '' )
 if 1 - 1: o0o00Oo0O . oOo0O0Ooo * ii
 I1I11i ( 'movies' , 'MAIN' )
def OoOoOo0o00OoOO ( ) :
 if 26 - 26: o0o00Oo0O - ooOOOoO . IIiIiII11i / iI11I1II1I1I
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 iiIIii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 80 - 80: oOo0O0Ooo % Ii1I % O0OOOoOoo0 / I1111IIi
 for oooOOO00o0 in iiIIii :
  i1Iii = O0Oo000ooO00 + oooOOO00o0 + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( i1Iii )
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oOooO0 , iII1iii , i1oO0OO0 , I11iiiiI1i , Iii1I1111ii in i1IIIII11I1IiI :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    o00oo0o ( Iii1I1111ii , oOooO0 , 222 , iII1iii , I11iiiiI1i , i1oO0OO0 )
    if 90 - 90: I11i
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 44 - 44: I11i / Ii1I . I1ii11iIi11i + OOooOOo
    if 32 - 32: I1111IIi - I11i1ii1 * O0OOOoOoo0 * ooOOOoO
def O00OOOo ( ) :
 if 37 - 37: ooOOOoO % Ii1I / I11i1ii1
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 iiIIii = [ 'tvnum' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 if 94 - 94: ooOOOoO / oO0o . I11i
 for oooOOO00o0 in iiIIii :
  iIiOo = O0Oo000ooO00 + oooOOO00o0 + I1IIIii
  oO0OOoo0OO = O0o0O00Oo0o0 ( iIiOo )
  i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for Iii1I1111ii , i1oO0OO0 , oOooO0 , ii1iii1i , I11iiiiI1i , iIiiiii1i in i1IIIII11I1IiI :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    I1IIiIi ( Iii1I1111ii , oOooO0 , iIiiiii1i , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
    if 48 - 48: Ii1IIIi1
    I1I11i ( 'movies' , 'MAIN' )
    xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
    if 26 - 26: O0OOOoOoo0 * iiiiiiii1 * o000O0o * OOooOOo
    if 48 - 48: O0OOOoOoo0 % Ii . ii * I1111IIi % oO0o . O0OOOoOoo0
def IiOOo0 ( ) :
 if 85 - 85: iiiiiiii1 % Ii1I
 oooO = OoOooO ( O0Oo000ooO00 + 'spongemain.php' )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , i1oO0OO0 , oOooO0 , ii1iii1i , I11iiiiI1i , iIiiiii1i in i1IIIII11I1IiI :
  I1IIiIi ( Iii1I1111ii , oOooO0 , iIiiiii1i , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
  I1I11i ( 'movies' , 'MAIN' )
def OO00o0O0oOooO ( url ) :
 if 18 - 18: Ii * I1ii11iIi11i / Ii1I + Ii1I % OOooOOo
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiI111iIi1 = ( '%s%s' % ( I1i1ii1ii , url ) )
 i1i = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in i1IIIII11I1IiI :
  II1I11IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
  for IiiiiI1i1Iii in II1I11IIi :
   if IiiiiI1i1Iii == url :
    Iii1I1111ii = ( '[COLORred]Watched - [/COLOR]' + Iii1I1111ii ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
  o00oo0o ( Iii1I1111ii , url , 222 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
  if 32 - 32: I1111IIi / ii
  I1I11i ( 'movies' , 'MAIN' )
  if 30 - 30: OOooOOo / oOo0O0Ooo - oO0o - O0OOOoOoo0 - Ii
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 84 - 84: ooOoO0O00 - oOo0O0Ooo % O0OOOoOoo0
  if 80 - 80: I11i % O0OOOoOoo0
def ooOooOooOOO ( url ) :
 if 59 - 59: ooOOOoO
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , i1oO0OO0 , url , ii1iii1i , I11iiiiI1i , iIiiiii1i in i1IIIII11I1IiI :
  I1IIiIi ( Iii1I1111ii , url , iIiiiii1i , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
  if 63 - 63: oO0o . o000O0o + iiiiiiii1 . OOooOOo / Ii / O0OOOoOoo0
  I1I11i ( 'movies' , 'MAIN' )
  if 46 - 46: I1ii11iIi11i + IIiIiII11i * oOo0O0Ooo + Ii1IIIi1
  if 31 - 31: ii1ii11IIIiiI * I11i * ii1ii11IIIiiI + oO0o * I11i . iiiiiiii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 89 - 89: ii * ii1ii11IIIiiI * oOo0O0Ooo . I11i1ii1 * ii1ii11IIIiiI / O0OOOoOoo0
def o00oo0o ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 46 - 46: Ii
 O0ooOOO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii11Iii1i1ii = True
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1i1111 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o0oO0O00oOo = [ ]
  o0oO0O00oOo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o0oO0O00oOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o0oO0O00oOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ii1i1i1111 . addContextMenuItems ( o0oO0O00oOo )
 Ii11Iii1i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = False )
 return Ii11Iii1i1ii
 if 15 - 15: o0o00Oo0O / ooOoO0O00 / ooOoO0O00 . O0OOOoOoo0 % OOooOOo + oOo0O0Ooo
def I1IIiIi ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 if 48 - 48: iiiiiiii1 % O0OOOoOoo0 % ii1ii11IIIiiI % iI11I1II1I1I . ii1ii11IIIiiI
 O0ooOOO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii11Iii1i1ii = True
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1i1111 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o0oO0O00oOo = [ ]
  o0oO0O00oOo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o0oO0O00oOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o0oO0O00oOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ii1i1i1111 . addContextMenuItems ( o0oO0O00oOo )
 Ii11Iii1i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = True )
 return Ii11Iii1i1ii
if 14 - 14: O0OOOoOoo0 * oO0o % o0o00Oo0O + ooOOOoO + Ii1I
if 23 - 23: I1ii11iIi11i % O0OOOoOoo0 + ii1ii11IIIiiI - iiiiiiii1
if 65 - 65: ii
if 22 - 22: Ii1IIIi1 + IIiIiII11i + I1ii11iIi11i
if 83 - 83: I11i1ii1
if 43 - 43: Ii1IIIi1
if 84 - 84: Ii1IIIi1 . I1111IIi . O0OOOoOoo0
if 2 - 2: I1ii11iIi11i - OOooOOo
if 49 - 49: ii1ii11IIIiiI + IIiIiII11i / o000O0o - OOooOOo % OOooOOo + oOo0O0Ooo
if 54 - 54: I11i1ii1 % I1ii11iIi11i - Ii1IIIi1
if 16 - 16: Ii1I * O0OOOoOoo0 / ooOOOoO
if 46 - 46: IIiIiII11i
if 13 - 13: I1111IIi + IIiIiII11i % oOo0O0Ooo
if 30 - 30: ii - Ii + o000O0o / I1ii11iIi11i - Ii
if 74 - 74: o0o00Oo0O . ooOOOoO
def o00o0OOoOo0O0 ( string ) :
 if OOoOO0oo0ooO == 'true' :
  xbmc . log ( "[addon.live.GenieTV-%s]: %s" % ( addon_version , string ) )
  if 39 - 39: iiiiiiii1 . oO0o % I11i1ii1 . Ii1IIIi1 / O0OOOoOoo0 * oO0o
def iiI1i ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 o0O00o0 = [ ]
 try :
  if 61 - 61: IIiIiII11i % Ii + iI11I1II1I1I + Ii1I / oOo0O0Ooo * ooOoO0O00
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( IIIii1II1II ) == False :
  o00o0OOoOo0O0 ( 'Making Favorites File' )
  o0O00o0 . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  IiIi1II111I = open ( IIIii1II1II , "w" )
  IiIi1II111I . write ( json . dumps ( o0O00o0 ) )
  IiIi1II111I . close ( )
 else :
  o00o0OOoOo0O0 ( 'Appending Favorites' )
  IiIi1II111I = open ( IIIii1II1II ) . read ( )
  iiOOoO0oOOO = json . loads ( IiIi1II111I )
  iiOOoO0oOOO . append ( ( name , url , iconimage , fanart , mode ) )
  O0ooo = open ( IIIii1II1II , "w" )
  O0ooo . write ( json . dumps ( iiOOoO0oOOO ) )
  O0ooo . close ( )
  if 47 - 47: Ii1IIIi1 / IIiIiII11i % I1111IIi . o000O0o * Ii1I
  if 35 - 35: I1ii11iIi11i * IIiIiII11i
def IIi1i1IIi ( ) :
 if os . path . exists ( IIIii1II1II ) == False :
  o0O00o0 = [ ]
  o00o0OOoOo0O0 ( 'Making Favorites File' )
  o0O00o0 . append ( ( 'Genie Tv Favourites Section' , '' , '' , '' , '' , '' , '' ) )
  IiIi1II111I = open ( IIIii1II1II , "w" )
  IiIi1II111I . write ( json . dumps ( o0O00o0 ) )
  IiIi1II111I . close ( )
 else :
  o0oo0Ooo0 = json . loads ( open ( IIIii1II1II ) . read ( ) )
  o0OOoO = len ( o0oo0Ooo0 )
  for I1iII1II1I1ii in o0oo0Ooo0 :
   Iii1I1111ii = I1iII1II1I1ii [ 0 ]
   oOooO0 = I1iII1II1I1ii [ 1 ]
   iII1iii = I1iII1II1I1ii [ 2 ]
   try :
    oo0OO0O = I1iII1II1I1ii [ 3 ]
    if oo0OO0O == None :
     raise
   except :
    if oo00 . getSetting ( 'use_thumb' ) == "true" :
     oo0OO0O = iII1iii
    else :
     oo0OO0O = I11iiiiI1i
   try : OO0OooOOoO00OO00 = I1iII1II1I1ii [ 5 ]
   except : OO0OooOOoO00OO00 = None
   try : ii11ii1iIiI1 = I1iII1II1I1ii [ 6 ]
   except : ii11ii1iIiI1 = None
   if 80 - 80: iI11I1II1I1I - oOo0O0Ooo - ii * I11i1ii1 + Ii . Ii1IIIi1
   if I1iII1II1I1ii [ 4 ] == 0 :
    iiOOooooO0Oo ( Iii1I1111ii , oOooO0 , '' , iII1iii , I11iiiiI1i , '' , 'fav' )
   else :
    iiOOooooO0Oo ( Iii1I1111ii , oOooO0 , I1iII1II1I1ii [ 4 ] , iII1iii , I11iiiiI1i , '' , 'fav' )
    if 87 - 87: o0o00Oo0O * IIiIiII11i + iI11I1II1I1I % o000O0o % Ii - OOooOOo
def o00O0Oooo ( name ) :
 iiOOoO0oOOO = json . loads ( open ( IIIii1II1II ) . read ( ) )
 for OoOIiiIi1IiiiI in range ( len ( iiOOoO0oOOO ) ) :
  if iiOOoO0oOOO [ OoOIiiIi1IiiiI ] [ 0 ] == name :
   del iiOOoO0oOOO [ OoOIiiIi1IiiiI ]
   O0ooo = open ( IIIii1II1II , "w" )
   O0ooo . write ( json . dumps ( iiOOoO0oOOO ) )
   O0ooo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 79 - 79: Ii1I - iI11I1II1I1I % ooOoO0O00 / I1ii11iIi11i + IIiIiII11i
 if 95 - 95: o000O0o
def ooO0o0oo ( ) :
 i11ii = os . path . join ( I11i1 , 'addons.ini' )
 IiI111I = open ( i11ii , "w+" )
 oO0OOoo0OO = OoOooO ( 'http://piesustv.net:8000/get.php?username=' + II11iiii1Ii + '&password=' + OO0o + '&type=m3u_plus&output=mpegts' )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?tvg-name="([^"]*)" tvg-logo="([^"]*)" group-title="([^"]*)"",.+?\n(.+?).ts' ) . findall ( oO0OOoo0OO )
 IiI111I . write ( r'[' + IiII + ']' + '\n' )
 for Iii1I1111ii , ii1iii1i , oo0oO0 , oOooO0 in i1IIIII11I1IiI :
  oOooO0 = ( oOooO0 + '.m3u8' ) . replace ( ':' , '%3A' ) . replace ( '/' , '%2F' )
  ii1i1IiiIIII11111Ii = ( Iii1I1111ii + '=plugin://' + IiII + '/?url=' + oOooO0 + '&mode=10012&name=' + ( Iii1I1111ii ) . replace ( ' ' , '+' ) + '&amp;iconimage=' + ( ii1iii1i ) . replace ( ' ' , '' ) + '+&amp;fanart=' + ( ii1iii1i ) . replace ( ' ' , '' ) + '+&amp;description=' )
  IiI111I . write ( ii1i1IiiIIII11111Ii + '\n' )
  if 21 - 21: o0o00Oo0O + o0o00Oo0O / I11i - ooOOOoO
  if 88 - 88: Ii1I . IIiIiII11i / Ii1IIIi1 % ooOoO0O00 - OOooOOo % Ii
def Oo0 ( ) :
 oooO = cloudflare . source ( i11 ( 'aHR0cHM6Ly93d3cuYXJjb25haXR2Lm1lL2FjdGlvbi8=' ) )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" type="application/x-mpegurl"/></video>' , re . DOTALL ) . findall ( oooO )
 for oOooO0 in i1IIIII11I1IiI :
  O0Oo00OoOo ( '24/7' , oOooO0 , 90021 , III1iII1I1ii + '247Streams.png' )
  if 7 - 7: o0o00Oo0O - Ii1I / OOooOOo - ii1ii11IIIiiI - o000O0o / ii
def iIiI ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvMjQ3c3RyZWFtLm0zdQ==' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( Iii1I1111ii , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + '247Streams.png' , III1iII1I1ii + '247Streams.png' , '' )
def I1Ii1i11I1I ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbXVzaWMubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( Iii1I1111ii , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + 'musicch.png' , III1iII1I1ii + 'musicch.png' , '' )
def Iii ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvbmV3cy5tM3U=' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( Iii1I1111ii , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + 'NEWS.png' , III1iII1I1ii + 'NEWS.png' , '' )
def Oo00o0OOo0OO ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvYWR1bHQubTN1' ) )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , oOooO0 in i1IIIII11I1IiI :
  OOiIiIIi1 ( Iii1I1111ii , ( oOooO0 ) . strip ( ) , 222 , III1iII1I1ii + 'adult.png' , III1iII1I1ii + 'adult.png' , '' )
def I1i1iiIi ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9pVHZfU3RyZWFtcy9UVVRTL21haW4ucGhw' ) )
 i1IIIII11I1IiI = re . compile ( 'href="/watch?v=(.+?)">(.+?)</a>' , re . DOTALL ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  OOiIiIIi1 ( Iii1I1111ii , oOooO0 , 1016 , III1iII1I1ii + 'TUTS.png' , III1iII1I1ii + 'TUTS.png' , '' )
  if 45 - 45: OOooOOo * I11i1ii1 / ii + oO0o . iiiiiiii1 / oO0o
  if 64 - 64: ii1ii11IIIiiI / ooOoO0O00 % oOo0O0Ooo - I11i
def iIii111Ii ( ) :
 if 96 - 96: ii1ii11IIIiiI - IIiIiII11i % OOooOOo * oOo0O0Ooo * oOo0O0Ooo . I1ii11iIi11i
 iiOOooooO0Oo ( '[COLOR' + II + ']Recent Episodes[/COLOR]' , '' , 10019 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , '' , 10020 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search[/COLOR]' , '' , 10021 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
 if 75 - 75: I1ii11iIi11i + ii1ii11IIIiiI + oO0o
def o00o0o0oOo0 ( ) :
 if 33 - 33: ooOoO0O00 / I1111IIi - ooOoO0O00 . oOo0O0Ooo
 oooO = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( oooO )
 for oOooO0 , ii1iii1i , Iii1I1111ii , Iii1iiIi1II1 in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii + '  -  ' + ( Iii1iiIi1II1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOooO0 , 10023 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 48 - 48: I11i1ii1 + Ii1IIIi1 . iiiiiiii1 % IIiIiII11i + o000O0o
  if 38 - 38: o000O0o
  if 28 - 28: iI11I1II1I1I * ooOOOoO . oOo0O0Ooo
def oooiI1i ( ) :
 if 54 - 54: ii1ii11IIIiiI . o0o00Oo0O
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
 if 79 - 79: I1111IIi / oO0o * ii * OOooOOo + oOo0O0Ooo
def O0ooO ( url ) :
 I1i = 'http://dizilab.com/arsiv?limit=100&tur=' + url + '&orderby=&ulke=&order=&yil=&dizi_adi='
 oO0OOoo0OO = cloudflare . source ( I1i )
 i1IIIII11I1IiI = re . compile ( '<div class="tv-series-single">.+?<a href="([^"]*)" class="film-image">.+?<img src="([^"]*)" alt=""/>.+?<span class="position">.+?</span>\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 10022 , III1iII1I1ii + 'dtv.png' , O0o0Oo , '' )
  if 40 - 40: I11i . I11i * Ii
  if 44 - 44: I11i
  if 80 - 80: Ii1I + ooOOOoO - I11i1ii1 - I11i % ii1ii11IIIiiI
  if 85 - 85: iiiiiiii1
def O0OoO00OoOO ( ) :
 if 53 - 53: oO0o % Ii1I . O0OOOoOoo0 . ooOoO0O00 . oO0o
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 oOooO0 = ( i11 ( 'aHR0cDovL2RpemlsYWIuY29tL2Fyc2l2P2xpbWl0PSZ0dXI9Jm9yZGVyYnk9JnVsa2U9Jm9yZGVyPSZ5aWw9JmRpemlfYWRpPQ==' ) ) + ( oo00O0 ) . replace ( ' ' , '+' )
 oO0OOoo0OO = cloudflare . source ( oOooO0 )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="film-image">\n<img src="([^"]*)" alt=""/>\n</a>\n<div class="tss-detail">\n<a class="title" style="" href=".+?">\n<span class="position">.+?</span>\n(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  if oo00O0 in Iii1I1111ii . lower ( ) :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 10022 , III1iII1I1ii + 'dtv.png' )
   if 26 - 26: oOo0O0Ooo % OOooOOo
   if 67 - 67: I1ii11iIi11i - I1111IIi * ii1ii11IIIiiI . ii / Ii
   if 61 - 61: I11i % oOo0O0Ooo * ooOoO0O00 / oOo0O0Ooo / IIiIiII11i + iiiiiiii1
def i1Io00OOOo ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>.+?<a class="episode" href=".+?">\n(.+?)\n</a>.+?<a class="episode-name" href=".+?">\n(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I11iiii1I , O0OO00O0oOO , Ii1 , Iii1I1111ii in i1IIIII11I1IiI :
  ooOO0oo00Oo = ( Ii1 ) . replace ( 'Sezon' , '' ) . replace ( 'bölüm' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  i1I11I1i = ( O0OO00O0oOO ) . replace ( 'bölüm' , '' ) . replace ( 'Sezon' , '' ) . replace ( 'Bölüm' , '' ) . replace ( 'BÃ¶lÃ¼m' , '' ) . replace ( '.' , '' )
  oOO0oOooo = 'Season ' + i1I11I1i + 'Episode ' + ooOO0oo00Oo + Iii1I1111ii
  o00IIIIii1111i1 ( oOO0oOooo , I11iiii1I )
  if 11 - 11: OOooOOo
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 31 - 31: IIiIiII11i * ii1ii11IIIiiI / I1111IIi / Ii
  if 88 - 88: I1ii11iIi11i . I11i - Ii . o0o00Oo0O * iI11I1II1I1I * OOooOOo
def o00IIIIii1111i1 ( name , url ) :
 I11iiii1I = url
 OoOOoO0o = name
 O0 = cloudflare . source ( I11iiii1I )
 i1I = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0 )
 for IIiI11i1111Ii , o0O00ooo0 in i1I :
  ii1ii111 ( '[COLOR' + II + ']' + OoOOoO0o + o0O00ooo0 + '[/COLOR]' , IIiI11i1111Ii , 222 , III1iII1I1ii + 'dtv.png' )
  if 23 - 23: o0o00Oo0O
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 41 - 41: ooOoO0O00 . Ii1IIIi1 / I11i1ii1 / I11i % I1111IIi - ii1ii11IIIiiI
 if 14 - 14: Ii1I - Ii * iiiiiiii1
def iIIII1iIIii ( ) :
 if 39 - 39: ii
 if 19 - 19: Ii
 if 80 - 80: oOo0O0Ooo
 if 58 - 58: o000O0o + Ii1I % OOooOOo
 if 22 - 22: iI11I1II1I1I - ii1ii11IIIiiI / oOo0O0Ooo * I1111IIi
 if 26 - 26: I11i + Ii1IIIi1 - I11i + I1ii11iIi11i . o000O0o
 if 97 - 97: ooOoO0O00
 iiOOooooO0Oo ( '[COLOR' + II + ']LATEST EPISODES[/COLOR]' , 'http://watchepisodes.cc/' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']A-Z[/COLOR]' , 'http://watchepisodes.cc/series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']POPULAR[/COLOR]' , 'http://watchepisodes.cc/popular-series/' , 10092 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']SEARCH[/COLOR]' , '' , 10091 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 if 46 - 46: Ii1I
def II1i1 ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0o0oo0OOo0O0 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for ii1iii1i , url , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 10094 , 'http://watchepisodes.cc/' + ii1iii1i , '' , '' )
 for url in o0o0oo0OOo0O0 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10091 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 37 - 37: I11i * I1ii11iIi11i
def iI11i1I1i ( url ) :
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<h4 class="media-heading"><a href="([^"]*)">(.+?)</a></h4>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 o0o0oo0OOo0O0 = re . compile ( '([^"]*)" >&emsp; NEXT MOVIES</a></h4></li>' ) . findall ( oO0OOoo0OO )
 for ii1iii1i , url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1iii1i = 'http://watchepisodes.cc/' + ii1iii1i
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 10093 , ii1iii1i , ii1iii1i , '' )
 for url in o0o0oo0OOo0O0 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , url , 10092 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 96 - 96: iiiiiiii1 / I1111IIi * iI11I1II1I1I + Ii * Ii1I / oOo0O0Ooo
def OoOo0000o0OOo ( url , iconimage ) :
 ii1iii1i = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( "<td>(.+?)</td>.+?<td><a href='([^']*)'>(.+?)</a></td>" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Ii1 , url , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Ii1 + ' - ' + Iii1I1111ii + '[/COLOR]' , 'http://watchepisodes.cc/' + url , 10094 , ii1iii1i , '' , '' )
  if 84 - 84: I11i1ii1
def I11i1iiiiIIIi ( url , iconimage ) :
 ii1iii1i = iconimage
 oO0OOoo0OO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<td>(.+?)</td>.+?<a href="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  if 'player' in Iii1I1111ii :
   pass
  elif 'vod' in Iii1I1111ii :
   iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.' , '' ) . replace ( 'www' , '' ) . replace ( 'com' , '' ) . replace ( ' ' , '' ) , url , 10045 , ii1iii1i , '' , '' )
   if 13 - 13: o0o00Oo0O + iiiiiiii1 * IIiIiII11i + I1ii11iIi11i * I1111IIi
   if 12 - 12: I1111IIi - ii1ii11IIIiiI % ii1ii11IIIiiI
   if 23 - 23: I11i1ii1
   if 61 - 61: I1111IIi + O0OOOoOoo0 - oO0o * o000O0o
   if 87 - 87: IIiIiII11i % IIiIiII11i
   if 51 - 51: I11i1ii1 * iI11I1II1I1I . O0OOOoOoo0
def oOOO00o000o ( ) :
 if 25 - 25: Ii1IIIi1 - ii1ii11IIIiiI . ooOOOoO
 if 57 - 57: I11i + I1ii11iIi11i * Ii1I - I11i1ii1 % iI11I1II1I1I - ii1ii11IIIiiI
 if 37 - 37: oO0o * ooOOOoO + ii1ii11IIIiiI + Ii1I * I11i
 if 95 - 95: ii1ii11IIIiiI - Ii % Ii - o0o00Oo0O * iiiiiiii1
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
 iiOOooooO0Oo ( '[COLOR' + II + ']Newest Episodes Added[/COLOR]' , 'http://www.watchseriesgo.to/latest' , 10046 , III1iII1I1ii + 'latest.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']This Week\'s Popular Episodes[/COLOR]' , 'http://www.watchseriesgo.to/new' , 10042 , III1iII1I1ii + 'popular.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Genres[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10048 , III1iII1I1ii + 'Genre.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Series[/COLOR]' , 'http://www.watchseriesgo.to/series' , 10041 , III1iII1I1ii + 'series.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Search Program[/COLOR]' , '' , 10043 , III1iII1I1ii + 'Search.png' , III1iII1I1ii + 'WatchSeries.png' , '' )
 if 63 - 63: ooOOOoO * I11i1ii1 % IIiIiII11i % iiiiiiii1 + oOo0O0Ooo * I1ii11iIi11i
 if 96 - 96: I1111IIi
def oo00OOo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 O00oO0 = re . compile ( '<ul class="pagination">(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="/letters/(.+?)">(.+?)</a></li>' ) . findall ( str ( O00oO0 ) )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.watchseriesgo.to/letters/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 61 - 61: o000O0o % I11i1ii1 - Ii1I + o000O0o . OOooOOo
def IIIi ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class="sr-header">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.watchseriesgo.to/' + url , 10049 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  if 35 - 35: Ii1IIIi1 . ooOOOoO . iiiiiiii1 - ooOOOoO % ooOOOoO + iiiiiiii1
def oO0oO00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<ul class="pagination">.+?color:#000;">.+?</a></li>.+?<li><a href="([^"]*)".+?<div' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if 'episode' in url :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10049 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 15 - 15: oOo0O0Ooo % o000O0o . I1ii11iIi11i % iI11I1II1I1I
  if 98 - 98: ooOOOoO - ooOoO0O00 % ii1ii11IIIiiI - ii
def Iii1I1I ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 IIiIIiIi1II1IiI = 'http://www.watchseriesgo.to/search/' + oo00O0 . replace ( ' ' , '%20' )
 oO0OOoo0OO = OoOooO ( IIiIIiIi1II1IiI )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<a href="([^"]*)" title=".+?"><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'watch online' in Iii1I1111ii :
   pass
  else :
   print oOooO0
   iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.watchseriesgo.to' + oOooO0 , 10044 , ii1iii1i , '' , '' )
   if 99 - 99: I1ii11iIi11i
   xbmcplugin . setContent ( O000oo0O , 'movies' )
   if 17 - 17: Ii - Ii + Ii1I * I11i1ii1 * o000O0o / ii
def i1II111ii1ii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?<div class="block-left-home-inside-text">.+?<a href="([^"]*)" title=".+?"><b>(.+?)</b> <br>.+?<span class=".+?">(.+?)</span></a><br>(.+?)<br>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , url , Iii1I1111ii , Ii1 , i1oO0OO0 in i1IIIII11I1IiI :
  ii1iIi1II = ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + ' - ' + ( Ii1 ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ii1iIi1II + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , ii1iii1i , '' , i1oO0OO0 )
  if 54 - 54: O0OOOoOoo0 * IIiIiII11i / ii + iiiiiiii1 - o000O0o + I11i1ii1
def OOOOoOOOo0oOO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<li class="col-md-6 col-xs-12 list-movies-li"><a href="([^"]*)" title=".+?">(.+?)<span class="epnum">.+?</span></a></li>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1iIi1II = ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' )
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ii1iIi1II + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10046 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 92 - 92: iiiiiiii1 % O0OOOoOoo0 % I11i . oOo0O0Ooo - Ii1I - I11i
def IiIiooooOOo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="mask">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&' , '&' ) . replace ( '&#039;' , '\'' ) + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , ii1iii1i , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10041 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 100 - 100: Ii1IIIi1 % Ii - oOo0O0Ooo * iiiiiiii1 - I11i
def Oooo0o00 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<meta itemprop="url" content="([^"]*)">.+?<a href="([^"]*)" class="table-link">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 O00oO0 = re . compile ( '<div class="col-md-6 col-xs-12".+?<a href=".+?" itemprop="url"><span itemprop="name">(.+?)</span>(.+?)</ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O0OO00O0oOO , iiiI1IiI in O00oO0 :
  i1IIIII11I1IiI = re . compile ( '<li itemprop="episode".+?<meta itemprop="url" content="([^"]*)">.+?<span class="" itemprop="name">\n(.+?)\n' , re . DOTALL ) . findall ( str ( iiiI1IiI ) )
  for url , Iii1I1111ii in i1IIIII11I1IiI :
   ii1iIi1II = ( O0OO00O0oOO ) . replace ( '  ' , '' ) + ' ' + ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&nbsp;' , ' ' ) . replace ( '&#039;' , '\'' ) . replace ( '  ' , '' )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + ii1iIi1II + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 i1I = re . compile ( '&hellip;<li><a href=".+?">.+?</a></li><li><a href=".+?">.+?</a></li><li><a href="([^"]*)">Next</a></li></ul>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '/episode/' , '' ) . replace ( '_' , ' ' ) . replace ( '.html' , '' ) , 'http://www.watchseriesgo.to' + url , 10045 , III1iII1I1ii + 'WATCHSERIES.png' , '' , '' )
 for url in i1I :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + 'NEXT' + '[/COLOR]' , 'http://www.watchseriesgo.to' + url , 10044 , III1iII1I1ii + 'Next.png' , '' , '' )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 74 - 74: I1ii11iIi11i / iiiiiiii1 % iiiiiiii1 . I1111IIi
class ooOo ( ) :
 if 93 - 93: iiiiiiii1 % Ii
 List = [ ]
 source_list = [ ]
 def __init__ ( self , name ) :
  if 25 - 25: I11i1ii1 % O0OOOoOoo0 * O0OOOoOoo0 + iI11I1II1I1I . ooOoO0O00
  ii1iIi1II = name
  self . Get_Sources ( oOooO0 , ii1iIi1II )
  if 67 - 67: Ii1I + o000O0o * I1111IIi / IIiIiII11i % oO0o % oO0o
  if 28 - 28: OOooOOo % o000O0o - Ii1IIIi1 + Ii1IIIi1 + o000O0o / iI11I1II1I1I
 def Get_Sources ( self , URL , season_name ) :
  o0oOoO00o = xbmcgui . DialogProgress ( )
  oO0OOoo0OO = OoOooO ( URL )
  i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="/link/(.+?)" class="buttonlink" target="_blank" title="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
   URL = 'http://www.watchseriesgo.to/link/' + oOooO0
   self . Get_site_link ( URL , season_name )
   if 91 - 91: oOo0O0Ooo / IIiIiII11i * Ii1IIIi1
 def Get_site_link ( self , url , season_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe.+? src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  i1I = re . compile ( '<IFRAME SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  iiI1IIIi = re . compile ( '<IFRAME style=".+?" SRC="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for url in i1IIIII11I1IiI :
   self . main ( url , season_name )
  for url in i1I :
   self . main ( url , season_name )
  for url in iiI1IIIi :
   self . main ( url , season_name )
   if 94 - 94: IIiIiII11i - iI11I1II1I1I - iI11I1II1I1I
 def main ( self , url , season_name ) :
  o0oOoO00o . create ( "[COLORwhite]GenieTv[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
  if 'daclips.in' in url :
   OOOo0Ooo0o00o = 'DACLIPS'
   if OOOo0Ooo0o00o in ooOo . source_list :
    pass
   else :
    self . daclips ( url , season_name , OOOo0Ooo0o00o )
    o0oOoO00o . update ( 0 , "" , "Getting Daclips Links" )
  else :
   if 'thevideo.me' in url :
    OOOo0Ooo0o00o = 'THEVIDEO'
    if OOOo0Ooo0o00o in ooOo . source_list :
     pass
    else :
     self . thevideo ( url , season_name , OOOo0Ooo0o00o )
     o0oOoO00o . update ( 0 , "" , "Getting Thevideo Links" )
   else :
    if 'allmyvideos.net' in url :
     OOOo0Ooo0o00o = 'ALLMYVIDEOS'
     if OOOo0Ooo0o00o in ooOo . source_list :
      pass
     else :
      self . allmyvid ( url , season_name , OOOo0Ooo0o00o )
      o0oOoO00o . update ( 0 , "" , "Getting Allmyvideo Links" )
    else :
     if 'vidspot.net' in url :
      OOOo0Ooo0o00o = 'VIDSPOT'
      if OOOo0Ooo0o00o in ooOo . source_list :
       pass
      else :
       self . vidspot ( url , season_name , OOOo0Ooo0o00o )
       o0oOoO00o . update ( 0 , "" , "Getting Vidspot Links" )
     else :
      if 'vodlocker' in url :
       OOOo0Ooo0o00o = 'VODLOCKER'
       if OOOo0Ooo0o00o in ooOo . source_list :
        pass
       else :
        self . vodlocker ( url , season_name , OOOo0Ooo0o00o )
        o0oOoO00o . update ( 0 , "" , "Getting Vodlocker Links" )
      else :
       if 'vidto' in url :
        OOOo0Ooo0o00o = 'VIDTO'
        if OOOo0Ooo0o00o in ooOo . source_list :
         pass
        else :
         self . vidto ( url , season_name , OOOo0Ooo0o00o )
         o0oOoO00o . update ( 0 , "" , "Getting Vidto Links" )
         if 62 - 62: Ii1I . iiiiiiii1 . ii1ii11IIIiiI
       else :
        if 'youwatch' in url :
         OOOo0Ooo0o00o = 'YouWatch'
         if OOOo0Ooo0o00o in ooOo . source_list :
          pass
         else :
          self . youwatch ( url , season_name , OOOo0Ooo0o00o )
          o0oOoO00o . update ( 0 , "" , "Getting YouWatch Links" )
          if 19 - 19: Ii1I / iiiiiiii1
          if 35 - 35: I1ii11iIi11i * o000O0o / ii + o0o00Oo0O / ii / Ii1IIIi1
 def allmyvid ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for i11i1iIiii , Iii1I1111ii in i1IIIII11I1IiI :
   self . Printer ( i11i1iIiii , season_name , source_name )
   if 44 - 44: ooOoO0O00 . Ii1I - I11i1ii1 . Ii1IIIi1 . I11i + o000O0o
 def vidspot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '"file" : "([^"]*)",\n.+?"default" : .+?,\n.+?"label" : "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for i11i1iIiii , Iii1I1111ii in i1IIIII11I1IiI :
   self . Printer ( i11i1iIiii , season_name , source_name )
   if 17 - 17: iI11I1II1I1I + ooOoO0O00 . Ii1I + ii1ii11IIIiiI % ooOoO0O00 . o000O0o
 def thevideo ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{"file":"([^"]*)"' ) . findall ( oO0OOoo0OO )
  for i11i1iIiii in i1IIIII11I1IiI :
   self . Printer ( i11i1iIiii , season_name , source_name )
   if 57 - 57: o000O0o
 def vodlocker ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for i11i1iIiii in i1IIIII11I1IiI :
   self . Printer ( i11i1iIiii , season_name , source_name )
   if 92 - 92: IIiIiII11i - oO0o - Ii1IIIi1 % oOo0O0Ooo - OOooOOo * iiiiiiii1
 def daclips ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '{ file: "([^"]*)", type:"video" }' ) . findall ( oO0OOoo0OO )
  for i11i1iIiii in i1IIIII11I1IiI :
   self . Printer ( i11i1iIiii , season_name , source_name )
   if 16 - 16: iI11I1II1I1I + ii - I11i1ii1 * I1111IIi
 def filehoot ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for i11i1iIiii in i1IIIII11I1IiI :
   self . Printer ( i11i1iIiii , season_name , source_name )
 def vidto ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for i11i1iIiii in i1IIIII11I1IiI :
   self . Printer ( i11i1iIiii , season_name , source_name )
 def youwatch ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oO0OOoo0OO )
  for i11i1iIiii in i1IIIII11I1IiI :
   self . youplay ( i11i1iIiii , season_name , source_name )
 def youplay ( self , url , season_name , source_name ) :
  oO0OOoo0OO = OoOooO ( url )
  i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)"' ) . findall ( oO0OOoo0OO )
  for i11i1iIiii in i1IIIII11I1IiI :
   self . Printer ( i11i1iIiii , season_name , source_name )
   if 37 - 37: O0OOOoOoo0
 def Printer ( self , Link , season_name , source_name ) :
  if 15 - 15: I11i % oO0o / O0OOOoOoo0
  if Link in ooOo . List :
   pass
  elif source_name in ooOo . source_list :
   pass
  else :
   ii1ii111 ( '[COLOR' + II + ']' + source_name + '[/COLOR]' , Link , 222 , III1iII1I1ii + 'WATCHSERIES.png' )
   o0oOoO00o . update ( 100 , "" , "Got Source" )
   ooOo . List . append ( Link )
   ooOo . source_list . append ( source_name )
   if 36 - 36: oO0o + oO0o % I1ii11iIi11i + I1ii11iIi11i / ooOoO0O00 % ooOoO0O00
   xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
   if 20 - 20: Ii1IIIi1 * o000O0o
   if 91 - 91: oO0o % ooOoO0O00 - iI11I1II1I1I . Ii1IIIi1
   if 31 - 31: o000O0o % ooOoO0O00 . ii - I11i + ii
   if 45 - 45: Ii1IIIi1 + ooOOOoO / ii - ii1ii11IIIiiI + ii
   if 42 - 42: iI11I1II1I1I * oOo0O0Ooo * iiiiiiii1
def IiIi ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Highlights[/COLOR]' , '' , 10008 , III1iII1I1ii + 'Highlights.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Fixtures[/COLOR]' , '' , 10009 , III1iII1I1ii + 'Fixtures.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Live Sport On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'Sport.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Premier League Table[/COLOR]' , 'http://www.bbc.co.uk/sport/football/premier-league/table' , 50002 , III1iII1I1ii + 'PremiereLeague.png' , O0o0Oo , '' )
 if 62 - 62: Ii1IIIi1 * o0o00Oo0O % I1111IIi . I1111IIi . oOo0O0Ooo
def oo0I1I1iiI1i ( url ) :
 IiII1111I = '20'
 iiIIii111Ii = [ ]
 OO000oooOo000 = '                                                    '
 o0oO0o0Oo0 = '        '
 iiOOooooO0Oo ( OO000oooOo000 + 'pl' + o0oO0o0Oo0 + 'w' + o0oO0o0Oo0 + 'd' + o0oO0o0Oo0 + 'l' + o0oO0o0Oo0 + 'f' + o0oO0o0Oo0 + 'a' + o0oO0o0Oo0 + 'pts' , '' , '' , '' , '' , '' )
 oooO = IiiI1iiiiI1iI ( url )
 i1IIIII11I1IiI = re . compile ( '<td class="team-name"><a href=.+?>(.+?)</a>.+?<td class="played">(.+?)</td>.+?<td class="won"><span>(.+?)</span></td>.+?<td class="drawn">(.+?)</td>.+?<td class="lost">(.+?)</td>.+?<td class="for">(.+?)</td>.+?<td class="against">(.+?)</td>.+?<td class="goal-difference">(.+?)</td>.+?<td class="points">(.+?)</td>' , re . DOTALL ) . findall ( oooO )
 for i1I1iiiI , i1IiIi1I1i , Ii11I1 , OOO0OoO0oo0OO , OO00OO , OOoO , IiIi1II111I , IiIiIi11iiIi1 , OoOoO0O00oo in i1IIIII11I1IiI :
  ooo0o0oooo = o0Oo ( i1IiIi1I1i )
  IiiiiiiI111i = o0Oo ( Ii11I1 )
  iiIIIIiI11II1 = o0Oo ( OOO0OoO0oo0OO )
  IiI1i11i1iI = o0Oo ( OO00OO )
  o0oo0O0OO0 = o0Oo ( OOoO )
  IIiI = o0Oo ( IiIi1II111I )
  iiIIii111Ii . append ( i1I1iiiI [ 0 ] )
  i11I1Ii1Iiii1 = len ( iiIIii111Ii )
  o0oooOoOoOo = int ( len ( OO000oooOo000 ) - len ( i1I1iiiI ) - 2 )
  if len ( iiIIii111Ii ) >= 10 :
   o0oooOoOoOo = o0oooOoOoOo - 1
  if len ( iiIIii111Ii ) <= int ( IiII1111I ) :
   OOiIiIIi1 ( str ( i11I1Ii1Iiii1 ) + ' ' + i1I1iiiI + OO000oooOo000 [ 0 : o0oooOoOoOo ] + i1IiIi1I1i + ooo0o0oooo + Ii11I1 + IiiiiiiI111i + OOO0OoO0oo0OO + iiIIIIiI11II1 + OO00OO + IiI1i11i1iI + OOoO + o0oo0O0OO0 + IiIi1II111I + IIiI + ' ' + OoOoO0O00oo , '' , '' , '' , '' , '' )
   if 96 - 96: OOooOOo / oO0o % ii * I11i1ii1
   if 6 - 6: oOo0O0Ooo . IIiIiII11i + iiiiiiii1 / oO0o % oOo0O0Ooo . ii
def o0Oo ( space ) :
 if len ( space ) > 1 :
  Ii1I1I111iI = len ( '        ' ) - len ( space ) + 1
  space = int ( Ii1I1I111iI ) * ' '
 elif len ( space ) == 1 :
  space = '        '
 return space
 if 64 - 64: iI11I1II1I1I + IIiIiII11i . O0OOOoOoo0 % I1ii11iIi11i * I11i1ii1
def iiii1i1 ( ) :
 if 98 - 98: Ii1I - ii / oOo0O0Ooo . I11i1ii1 - ooOoO0O00
 if 60 - 60: OOooOOo % OOooOOo
 if 2 - 2: ii1ii11IIIiiI . o0o00Oo0O - o000O0o + I1111IIi
 if 96 - 96: ii1ii11IIIiiI + ii1ii11IIIiiI
 if 28 - 28: O0OOOoOoo0
 if 6 - 6: oOo0O0Ooo - O0OOOoOoo0
 if 49 - 49: IIiIiII11i
 if 33 - 33: I11i - o000O0o % Ii1I * ooOOOoO . ii % ii1ii11IIIiiI
 if 29 - 29: O0OOOoOoo0 + IIiIiII11i . Ii . ii1ii11IIIiiI - o0o00Oo0O
 if 47 - 47: o000O0o . Ii1I - iI11I1II1I1I % IIiIiII11i / OOooOOo % ii
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
 oooO = OoOooO ( i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20vcXVpY2tpbmRleC5odG1s' ) )
 i1IIIII11I1IiI = re . compile ( '<a target="_self" href="([^"]*)".+?src="([^"]*)" alt="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 for oOooO0 , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( 'amp;' , '' ) + '[/COLOR]' , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + oOooO0 , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20v' ) + ii1iii1i , O0o0Oo , '' )
  if 21 - 21: ii % OOooOOo - OOooOOo / Ii1I / I11i
def I111i ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 O00oO0 = re . compile ( 'AndClearL.+?><h2.+?head>(.*?)float' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for O00oO0 in O00oO0 :
  o0OoOoOOoOo0o = re . compile ( '(.*?)</h2>' ) . findall ( str ( O00oO0 ) )
  for II1IiIiiI1III in o0OoOoOOoOo0o :
   II1IiIiiI1III = II1IiIiiI1III
  i1i1iI = re . compile ( 'comp_head>(.*?)</span>.*?<div class = fLeft width = ".*?"><img src="(.*?)">.*?</div>.*?ST:(.*?)</div>(.+?)<!-- around all of channel types ENDS 2-->' , re . DOTALL ) . findall ( str ( O00oO0 ) )
  for I1i1IiIIiIiII , ii1iii1i , time , I111I11I111 in i1i1iI :
   O00OOoOOOO00O = re . compile ( ",CAPTION, '(.+?)&nbsp" ) . findall ( I111I11I111 )
   iiOOooooO0Oo ( '[COLOR' + II + ']' + II1IiIiiI1III + ' - ' + I1i1IiIIiIiII + ' - ' + time + '[/COLOR]' , '' , 10010 , i11 ( 'aHR0cDovL2xpdmVvbnNhdC5jb20=' ) + ii1iii1i , O0o0Oo , ( str ( O00OOoOOOO00O ) ) )
   if 27 - 27: ii * oOo0O0Ooo - O0OOOoOoo0 / O0OOOoOoo0
 I1I11i ( 'tvshows' , 'Media Info 3' )
 if 21 - 21: o0o00Oo0O * I11i1ii1 % OOooOOo / o0o00Oo0O
def ooooooo ( ) :
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
 if 58 - 58: ooOoO0O00 + o0o00Oo0O . oO0o % ooOOOoO
def IIi1I1 ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , url , Iii1I1111ii in i1IIIII11I1IiI :
  oO0OO0O = Iii1I1111ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Iii1I1111ii :
   pass
  else :
   oO0OO0O = Iii1I1111ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
   ii1ii111 ( '[COLOR' + II + ']' + oO0OO0O + '[/COLOR]' , url , 10013 , ii1iii1i )
 for url , ii1iii1i , Iii1I1111ii in i1I :
  oO0OO0O = Iii1I1111ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Iii1I1111ii :
   pass
  else :
   ii1ii111 ( '[COLOR' + II + ']' + oO0OO0O + '[/COLOR]' , url , 10013 , ii1iii1i )
def oooOoooOOo0 ( url ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Live On G-Tv[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9mb290eS9mb290eS5tM3U=' ) ) , 7080 , III1iII1I1ii + 'TodaysMacthes.png' , O0o0Oo , '' )
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'class="entry-thumb" src="([^"]*)" alt="".+?<h3 class="entry-title td-module-title"><a href="([^"]*)" rel="bookmark" title=".+?">([^>]*)</a></h3>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 i1I = re . compile ( '<div class="td-block-span6">.+?<div class="td_module_6 td_module_wrap td-animation-stack">.+?<div class="td-module-thumb"><a href="([^"]*)" rel="bookmark" title=".+?"><img width="100" height="70" class="entry-thumb" src="([^"]*)" alt=".+?" title="([^"]*)"/></a></div>.+?</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 if 25 - 25: O0OOOoOoo0 + oOo0O0Ooo + OOooOOo + iiiiiiii1 % o0o00Oo0O
 if 26 - 26: I11i1ii1 + OOooOOo
 if 17 - 17: Ii1I - O0OOOoOoo0 % I1ii11iIi11i * o0o00Oo0O % o0o00Oo0O * Ii1IIIi1
 if 6 - 6: iiiiiiii1
 if 46 - 46: IIiIiII11i * iiiiiiii1
 if 23 - 23: ooOoO0O00 - o0o00Oo0O
 if 6 - 6: I11i1ii1 % ii * iiiiiiii1 - I1111IIi
 for url , ii1iii1i , Iii1I1111ii in i1I :
  oO0OO0O = Iii1I1111ii . replace ( '&#8211;' , '-' ) . replace ( '&#038;' , '&' ) . replace ( '&#8217;' , '' )
  if 'Highlights &' in Iii1I1111ii :
   pass
  else :
   ii1ii111 ( '[COLOR' + II + ']' + oO0OO0O + '[/COLOR]' , url , 10013 , ii1iii1i )
   if 24 - 24: ooOOOoO / iI11I1II1I1I . ii % OOooOOo . ii1ii11IIIiiI
def ooo00OoOooooo ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<script data-config="([^"]*)" data-height' ) . findall ( oO0OOoo0OO )
 for IIiI11i1111Ii in i1IIIII11I1IiI :
  OoooooO0 = ( IIiI11i1111Ii ) . replace ( '/v2' , '' ) . replace ( 'zeus.json' , 'video-sd.mp4?hosting_id=21772' ) . replace ( 'config.playwire.com' , 'cdn.video.playwire.com' )
  i1iiiIii11 ( 'http:' + OoooooO0 )
  if 7 - 7: OOooOOo . Ii1IIIi1 % I1ii11iIi11i
  if 55 - 55: I11i1ii1 - I1ii11iIi11i * o000O0o
  if 72 - 72: I11i % I11i + O0OOOoOoo0 + Ii1I / I1ii11iIi11i
  if 30 - 30: I1ii11iIi11i + oOo0O0Ooo + Ii / oO0o
def o00OooooOOOO ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)"><img itemprop="image" content="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( "<a rel='next' href=([^=]*)=" , re . DOTALL ) . findall ( oooO )
 for url , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  ii1ii111 ( Iii1I1111ii , url , 8046 , ii1iii1i )
 for url in i1I :
  O0Oo00OoOo ( 'NEXT PAGE' , ( url ) . replace ( ' class' , '' ) , 8045 , III1iII1I1ii + 'Next.png' )
def oo000oiIIIII ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( "__filename='([^']*)',.+?__fullimage='([^']*)',.+?__title='([^']*)'," , re . DOTALL ) . findall ( oooO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  i1iiiIii11 ( 'http://bitcast-b.bitgravity.com/ndtvod/23372/ndtv/' + url )
  if 48 - 48: OOooOOo * ii + ii * iI11I1II1I1I * IIiIiII11i % Ii
def IIoooOoOO0o ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( "src='http://www.youtube.com/embed/(.+?)?version=3&#038;rel=1&#038;fs=1&#038;autohide=2&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;wmode=transparent' frameborder='0' allowfullscreen='true'></iframe>" ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 78 - 78: o0o00Oo0O - iiiiiiii1 * Ii1IIIi1 + ooOOOoO + IIiIiII11i
def ooO ( ) :
 O0Oo00OoOo ( '[COLOR' + II + ']Documentary Lovers[/COLOR]' , 'http://documentarylovers.com/' , 80009 , III1iII1I1ii + 'documentary.png' )
 O0Oo00OoOo ( '[COLOR' + II + ']RTD Documentaries[/COLOR]' , 'https://rtd.rt.com/' , 8048 , III1iII1I1ii + 'documentary.png' )
 O0Oo00OoOo ( '[COLOR' + II + ']Search Docs[/COLOR]' , '' , 80012 , III1iII1I1ii + 'Search.png' )
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cDovL2RvY3VyLmNvLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" class=.+? title="([^"]*)">' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , oOooO0 , 8041 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def III ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<img src="([^"]*)".+?class=itemTitle><a href="([^"]*)">(.+?)</a>' ) . findall ( oooO )
 next = re . compile ( '<a href="([^"]*)" rel=next>' , re . DOTALL ) . findall ( oooO )
 for ii1iii1i , url , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#039;s' , '' ) , 'http://docur.co' + url , 8042 , 'http://docur.co' + ii1iii1i )
 for url in next :
  O0Oo00OoOo ( 'NEXT PAGE' , url , 8041 , III1iII1I1ii + 'Next.png' )
  if 5 - 5: ii * Ii1I
  if 42 - 42: I11i . iiiiiiii1 / o0o00Oo0O . IIiIiII11i * OOooOOo
def i1IiI1I111iI1 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oooO )
 i1I = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  if 'youtube' in url :
   url = ( url ) . replace ( 'https://www.youtube.com/embed/' , '' )
   ii1ii111 ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
  else :
   O0Oo00OoOo ( '[COLOR' + II + ']doclist[/COLOR]' , 'http:' + url , 8044 , '' )
def oO00O000o ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '}],"([^"]*)":.+?,"url":"([^"]*)"' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  url = ( url ) . replace ( '\/' , '/' )
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 222 , '' )
  if 82 - 82: iiiiiiii1 / I11i1ii1 / I11i1ii1
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def Ii1I1i1IiiI ( name , url ) :
 IiiiI1i = 0
 name = name
 url = url
 i111I1 = [ '144' , '240' , '380' , '480' , '720' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Resolution[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  OOOoOO0o ( url )
  if 32 - 32: O0OOOoOoo0 + OOooOOo . iiiiiiii1 . ooOoO0O00 . OOooOOo * I11i1ii1
  if 59 - 59: IIiIiII11i * ii - ii
  if 33 - 33: o0o00Oo0O . Ii % I11i
  if 50 - 50: I11i1ii1
  if 81 - 81: Ii * iI11I1II1I1I / I1ii11iIi11i * Ii1IIIi1
  if 83 - 83: Ii - oOo0O0Ooo * Ii
  if 59 - 59: O0OOOoOoo0 - ii / I11i1ii1 + Ii1I . I11i - O0OOOoOoo0
  if 29 - 29: o000O0o
def IiI1i1I11I ( ) :
 oooO = ii1Oo0000oOo ( 'http://documentarylovers.com/' )
 i1IIIII11I1IiI = re . compile ( 'title="([^"]*)" href="([^"]*)"' ) . findall ( oooO )
 for Iii1I1111ii , oOooO0 in i1IIIII11I1IiI :
  if 'genre' in oOooO0 :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , oOooO0 , 80010 , III1iII1I1ii + 'documentary.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oO0o0ooooo ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)" title="([^"]*)" > <img.+?src="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 next = re . compile ( 'rel="next" href="([^"]*)"' ) . findall ( oooO )
 for url , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#8217;' , '' ) . replace ( '&#038;' , 'and' ) . replace ( '&amp;' , 'and' ) , url , 80011 , ii1iii1i )
 for url in next :
  O0Oo00OoOo ( 'NEXT PAGE' , url , 80010 , III1iII1I1ii + 'Next.png' )
  if 8 - 8: iI11I1II1I1I . iI11I1II1I1I + ii1ii11IIIiiI . Ii1IIIi1
def OoO0OO0 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( 'data-video="youtube" data-src="([^"]*)"><div' ) . findall ( oooO )
 i1I = re . compile ( 'itemprop="embedURL" content="([^"]*)"><meta' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']YouTube[/COLOR]' , url , 8043 , III1iII1I1ii + 'documentary.png' )
 for url in i1I :
  oO00O000o ( url )
  if 21 - 21: ii . o0o00Oo0O / Ii
def oOOO ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 o0000o0Oo = 'http://documentarylovers.com/?s=' + ( oo00O0 ) . replace ( ' ' , '+' )
 iiiI111I = o0000o0Oo . lower ( )
 oO0o0ooooo ( iiiI111I )
 if 71 - 71: oOo0O0Ooo . I11i1ii1
def iI1i11II1i1i ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if 'films' in url :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 8049 , III1iII1I1ii + 'documentary.png' )
def O0O0O00OoO0O ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<img alt="RTD" src="([^"]*)">.+?heading" href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( 'rel="next" href="([^"]*)">»</a>' ) . findall ( oooO )
 for ii1iii1i , url , Iii1I1111ii in i1IIIII11I1IiI :
  if 'films' in url :
   ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#038;' , 'and' ) . replace ( '&#8217;' , 'and' ) , 'https://rtd.rt.com' + url , 804900 , 'https://rtd.rt.com' + ii1iii1i )
 for url in i1I :
  O0Oo00OoOo ( 'NEXT' , url , 8049 , III1iII1I1ii + 'Next.png' )
def i1II11III ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)" frameborder=' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  if 'rtd' in url :
   O0OO0oo ( url )
   if 41 - 41: OOooOOo % iiiiiiii1 * o000O0o * ooOoO0O00
def O0OO0oo ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( "{file: '([^']*)' + '([^']*)'}" ) . findall ( oooO )
 for i1i , file in i1IIIII11I1IiI :
  url = ( 'https://rtd.rt.com' + i1i + file )
  OOOoOO0o ( url )
  if 32 - 32: oOo0O0Ooo + Ii - iiiiiiii1 / IIiIiII11i
  if 27 - 27: I11i1ii1 . I1ii11iIi11i + I11i1ii1 + O0OOOoOoo0
def III11IiI ( ) :
 oO0OOoo0OO = ii1Oo0000oOo ( 'http://www.stream2watch.co/live-tv' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt=".+?"/>.+?<span class="country_name">(.+?)<br />(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for oOooO0 , ii1iii1i , Iii1I1111ii , IIi in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( Iii1I1111ii + '[COLOR' + II + ']' + IIi + '[/COLOR]' ) , oOooO0 , 8086 , ii1iii1i )
  if 6 - 6: Ii1IIIi1 / iI11I1II1I1I / I11i1ii1 / oOo0O0Ooo - ooOoO0O00 - Ii1IIIi1
def Iii1iI1I1iii1 ( url ) :
 oO0OOoo0OO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="front_channel_href" href="([^"]*)" title=".+?">.+?<img class="front_channel_thumb" src="([^"]*)" alt=".+?"/>.+?<span class="front_channel_name">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 8087 , ii1iii1i )
  if 31 - 31: o0o00Oo0O - I1111IIi * Ii * ooOoO0O00
def O0oOo00Oo0oo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'a id="code_.+?data-f-href="([^"]*)" data-code-embed="">(.+?)</a>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  i111 ( url , Iii1I1111ii )
  if 63 - 63: I11i1ii1 % oOo0O0Ooo . Ii1IIIi1 - I11i1ii1 / I1ii11iIi11i % oOo0O0Ooo
def i111 ( url , name ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "playStream\('.+?', '(.+?)'\);" , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  print url
  ii1ii111 ( '[COLOR' + II + ']' + name + '[/COLOR]' , url , 222 , '' )
  if 39 - 39: I11i . ooOoO0O00 % o000O0o / ooOOOoO % o0o00Oo0O
def o0O0OOooO ( ) :
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cDovL3d3dy5zb2xpZS5vcmcvYWxpYnJhcnkvaW5kZXguaHRtbA==' ) )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oooO )
 for oOooO0 , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + oOooO0 , 3002 , 'http://www.solie.org/alibrary/' + ii1iii1i )
def i1II111i1IIii ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oooO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ii1iii1i )
def IIIi1ii1i1 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<br><a href="([^"]*)">(.+?)</a>' ) . findall ( oooO )
 iiiIiIIiIiiii = re . compile ( 'href="([^"]*)">Season(.+?)</a>' ) . findall ( oooO )
 next = re . compile ( '<a href="([^"]*)">Episodes</a>' ) . findall ( oooO )
 i1I = re . compile ( '<td align="center" valign="top">.+?<a href="([^"]*)">.+?<img src="([^"]*)".+?<H3>(.+?)</H3>' , re . DOTALL ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3004 , III1iII1I1ii + 'classicmovies.png' )
 for url , Iii1I1111ii in iiiIiIIiIiiii :
  O0Oo00OoOo ( '[COLOR' + II + ']Season- ' + Iii1I1111ii + '[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'classicmovies.png' )
 for url in next :
  O0Oo00OoOo ( '[COLOR' + II + ']NEXT[/COLOR]' , 'http://www.solie.org/alibrary/' + url , 3003 , III1iII1I1ii + 'Next.png' )
 for url , ii1iii1i , Iii1I1111ii in i1I :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '</TD>' , '' ) . replace ( '<BR>' , ' ' ) . replace ( '</H3>' , '' ) . replace ( '/<br>' , ' ' ) . replace ( '</a>' , '' ) . replace ( '<br>' , '' ) . replace ( '<H3>' , '' ) , 'http://www.solie.org/alibrary/' + url , 3003 , 'http://www.solie.org/alibrary/' + ii1iii1i )
def o00O0OooO0 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe.+?src="([^"]*)"' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  iii1II11II1 ( url )
def iii1II11II1 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<meta property="og:video" content="([^"]*)"/>' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  OOOoOO0o ( url )
  if 30 - 30: I1111IIi / Ii % oO0o * Ii1IIIi1
def iIi1Ii1i1iI ( ) :
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2FsbC8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOooO0 , 8065 , III1iII1I1ii + 'classicmovies.png' )
def i1oOOOoOO ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( "v.src = '([^']*)';" ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  ii1O0ooooo000 ( url )
  if 80 - 80: ii
def IiIIIIIi ( ) :
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cDovL3JldHJvdmlzaW9uLnR2L2NsYXNzaWMtdHYv' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"><h2><font color=".+?"><h2>(.+?)</font></h2></a>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#8211;' , ':' ) , oOooO0 , 8065 , III1iII1I1ii + 'classictv.png' )
def OOoo0o00O0oO ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)">' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( "videoId: '([^']*)'" , re . DOTALL ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  if 'mp4' in url :
   OOOoOO0o ( url )
 for url in i1I :
  yt . PlayVideo ( url )
  if 28 - 28: ii % o0o00Oo0O - Ii1IIIi1 / I11i / oOo0O0Ooo
def Iii1iIII1Iii ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcw==' ) )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"> (.+?).m3u</a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '-' , ' ' ) . replace ( '_' , ' ' ) , ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vbTN1c3RyZWFtcy8=' ) ) + oOooO0 , 8071 , III1iII1I1ii + 'streams.png' )
def ii1ii1111 ( url ) :
 oO0OOoo0OO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  if '(Free Access)' in Iii1I1111ii :
   url = ( url ) . strip ( )
  else :
   url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '_' , ' ' ) . replace ( '(Free Access)' , '[COLORwhite] - Free Access[/COLOR]' ) , url , 222 , III1iII1I1ii + 'streams.png' )
def iII11iiii111i ( url ) :
 oO0OOoo0OO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , Iii1I1111ii , url in i1IIIII11I1IiI :
  url = ( ( i11 ( 'aHR0cDovL3BpZXN1c3R2Lm5ldDo4MDAwL2xpdmUv' ) ) + II11iiii1Ii + '/' + OO0o + url ) . strip ( )
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , ii1iii1i , I11iiiiI1i , '' )
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
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if 'ch' in url :
   oOO0o ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORorange]   Videos[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Jizbox.png' , III1iII1I1ii + 'Jizbox.png' , '' )
def oooii111I1I1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "<a class=.+?href='([^']*)' rel=.+? title='([^']*)'" , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIIiIi1IiI1 = re . compile ( 'class="p-current">.+?</li> <li><a title="([^"]*)" href="([^"]*)">' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) . replace ( '&#039;' , '' ) , 'http://www.wetsextube.com' + url , 90009 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 for Iii1I1111ii , url in iIIiIi1IiI1 :
  iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.wetsextube.com' + url , 90008 , III1iII1I1ii + 'Next.png' , '' , '' )
def Oo0O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   Iii1I1III11 ( url )
def i1ii1IiIiIii ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOoOO0o ( url )
def Oooooo0O ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">.+?class="nb_cat border-radius-5">(.+?)</span>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , url , Iii1I1111ii , Ii1I1I111iI in i1IIIII11I1IiI :
  if 'category' in url :
   oOO0o ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORorange]   ' + Ii1I1I111iI + '[/COLOR]' , url , 90006 , ii1iii1i , III1iII1I1ii + 'Jizbox.png' , '' )
def OOo0ooOOOo0O0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" class="attachment-thumb_site size-thumb_site wp-post-image".+?<a href="([^"]*)" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIIiIi1IiI1 = re . compile ( '<link rel="next" href="([^"]*)"/>' ) . findall ( oO0OOoo0OO )
 for ii1iii1i , url , Iii1I1111ii in i1IIIII11I1IiI :
  OOiIiIIi1 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#8211;' , '-' ) , url , 90007 , ii1iii1i , '' , '' )
 for url in iIIiIi1IiI1 :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , url , 90006 , III1iII1I1ii + 'Next.png' , '' , '' )
def ooI1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-lazy-src="([^"]*)" frameborder=' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'jetload' in url :
   Iii1I1III11 ( url )
def Iii1I1III11 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  OOOoOO0o ( url )
def oooo000 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<td>.+?<a href="([^"]*)">(.+?)</a><br> \n(.+?)\n</td>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , Ii1I1I111iI in i1IIIII11I1IiI :
  if 'category' in url :
   oOO0o ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORorange]' + Ii1I1I111iI + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90003 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def i1Iii1i1II1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 I11iiii1I = url
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIIiIi1IiI1 = re . compile ( 'rel="next" href="([^"]*)">Next &raquo;</a>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  OOiIiIIi1 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.perfectgirls.net' + url , 90004 , ii1iii1i , '' , '' )
 for url in iIIiIi1IiI1 :
  iiOOooooO0Oo ( '[COLORred]NEXT[/COLOR]' , I11iiii1I + '/' + url , 90003 , III1iII1I1ii + 'Next.png' , '' , '' )
def O0o00OoooO ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'get\("(.*)", function' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  IiI1i1iI ( 'http://www.perfectgirls.net' + url )
def IiI1i1iI ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'http://(.+?)\n' ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  i1iiiIii11 ( 'http://' + url )
def I1I11I1i1i1II ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" title="([^"]*)">.+?"navbadge default">(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , Ii1I1I111iI in i1IIIII11I1IiI :
  oOO0o ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgreen] - No of Videos : [COLORorange]' + Ii1I1I111iI + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
def oo0o0o ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iIIiIi1IiI1 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in iIIiIi1IiI1 :
  oOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10103 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><b>(.+?)</b><span class="navbadge default"(.+?)</span>' ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , Ii1I1I111iI in i1IIIII11I1IiI :
  oOO0o ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgreen] - No of Videos : [COLORorange]' + ( Ii1I1I111iI + '[/COLOR]' ) ) . replace ( '"></span>' , ' ' ) . replace ( '<span class="flag-small flag-' , '' ) . replace ( '>' , '' ) , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
  if 5 - 5: oO0o . Ii1I . Ii
def iIIIII ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 iIIiIi1IiI1 = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in iIIiIi1IiI1 :
  oOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10104 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( ':"([^"]*)".+?;</script></a></div></div><p class="profile-name"><a href="([^"]*)">(.+?)</a></p><p class="profile-counts">\n(.+?)\n' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , url , Iii1I1111ii , I11OOO0 in i1IIIII11I1IiI :
  oOO0o ( Iii1I1111ii + '--' + ( I11OOO0 ) . replace ( '&nbsp;' , '' ) . replace ( '			' , '' ) , 'http://www.xvideos.com' + url + '#_tabVideos,videos-best' , 10105 , ( ii1iii1i ) . replace ( 'http:\/\/' , 'http://' ) , '' , '' )
  if 57 - 57: IIiIiII11i . ooOoO0O00
  if 33 - 33: O0OOOoOoo0 + I1ii11iIi11i % ooOOOoO . o000O0o
def ii1II1I ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , url , Iii1I1111ii , i1I1IiI1ii , i1II1i in i1IIIII11I1IiI :
  oOO0o ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgreen] - Porn Quality : [COLORorange]' + i1II1i + ' - [COLORred]' + i1I1IiI1ii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10108 , ii1iii1i , ii1iii1i , i1II1i + ' - ' + i1I1IiI1ii )
 O0oooooO0oOOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for url in O0oooooO0oOOo :
  oOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
  if 63 - 63: ii * iiiiiiii1
def oOoo0 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 O00oO0 = re . compile ( '<div class="main-categories">(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 iIIiIi1IiI1 = re . compile ( '<li><a class=".+?".+?href="([^"]*)">Next</a></li>' ) . findall ( oO0OOoo0OO )
 for url in iIIiIi1IiI1 :
  oOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + url , 10106 , III1iII1I1ii + 'Next.png' , '' , '' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)" class="btn btn-default">(.+?)</a>' ) . findall ( str ( O00oO0 ) )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if '/c/' in url :
   oOO0o ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.xvideos.com' + url , 10105 , III1iII1I1ii + 'Jizbox.png' , '' , '' )
   if 50 - 50: I1ii11iIi11i - I11i % IIiIiII11i . o0o00Oo0O . o000O0o % IIiIiII11i
   if 18 - 18: ooOOOoO % ii + oO0o / ooOOOoO
def ii1II11IIII1 ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 Iii1i11i = ( oo00O0 ) . replace ( ' ' , '+' ) . replace ( '&' , '&' )
 iiiI111I = Iii1i11i . lower ( )
 ooiiI = 'http://www.xvideos.com/?k=' + iiiI111I
 print ooiiI + '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'
 oO0OOoo0OO = OoOooO ( ooiiI )
 i1IIIII11I1IiI = re . compile ( '<div class="thumb"><script>.+?<img src="([^"]*)".+?<a href="([^"]*)" title="([^"]*)">.+?<strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , oOooO0 , Iii1I1111ii , i1I1IiI1ii , i1II1i in i1IIIII11I1IiI :
  oOO0o ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgreen] - Porn Quality : [COLORorange]' + i1II1i + ' - [COLORred]' + i1I1IiI1ii + '[/COLOR]' , 'http://www.xvideos.com' + oOooO0 , 10108 , ii1iii1i , ii1iii1i , i1II1i + ' - ' + i1I1IiI1ii )
 O0oooooO0oOOo = re . compile ( '<li><a href="([^"]*)" class="no-page">Next</a></li></ul></div>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in O0oooooO0oOOo :
  oOO0o ( '[COLORred]NEXT[/COLOR]' , 'http://www.xvideos.com' + oOooO0 , 10105 , III1iII1I1ii + 'Next.png' , '' , '' )
if 99 - 99: ii1ii11IIIiiI + I1111IIi % Ii
if 41 - 41: oOo0O0Ooo % Ii1IIIi1
if 30 - 30: Ii * I1ii11iIi11i . IIiIiII11i + Ii1I / I11i % iiiiiiii1
if 78 - 78: Ii1I + ii - oOo0O0Ooo * OOooOOo * O0OOOoOoo0
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
 iiI1IIIi = re . compile ( "setVideoHLS.+?'([^']*)'" ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   ii1ii111 ( '[COLOR' + II + ']Quality = [COLORred]SQUINT[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in i1I :
  if 'http' in url :
   ii1ii111 ( '[COLOR' + II + ']Quality = [COLORyellow]ENJOY[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
 for url in iiI1IIIi :
  if 'http' in url :
   ii1ii111 ( '[COLOR' + II + ']Quality = [COLORgreen]GO BLIND[/COLOR]' , url , 222 , III1iII1I1ii + 'Jizbox.png' )
   if 44 - 44: O0OOOoOoo0
def oOoOoOOOO0o ( url ) :
 OOo00O = xbmc . Player ( o0Ii1Iii111IiI1 ( ) )
 import urlresolver
 try : OOo00O . play ( url )
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
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 8091 , III1iII1I1ii + 'gofish.png' )
def i1II111II1 ( url ) :
 oO0OOoo0OO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="item-thumbnail">.+?<a href="([^"]*)" title="([^"]*)">.+?<img src="([^"]*)"' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 8092 , ii1iii1i )
 for url in next :
  O0Oo00OoOo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
def I11I1iiI1 ( url ) :
 oO0OOoo0OO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<h3><a href="([^"]*)" rel=".+?" title="([^"]*)">' , re . DOTALL ) . findall ( oO0OOoo0OO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' , re . DOTALL ) . findall ( oO0OOoo0OO )
 II1IiI11I1 = re . compile ( '<img width="520" height="293" src="([^"]*)" class="attachment' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i in II1IiI11I1 :
  ii1iii1i = ii1iii1i
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 8092 , ii1iii1i )
 for url in next :
  O0Oo00OoOo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 8093 , III1iII1I1ii + 'Next.png' )
  if 85 - 85: oOo0O0Ooo % Ii
def Ii1I1I11I1I1i ( url ) :
 oO0OOoo0OO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( "videoId: '([^']*)'," ) . findall ( oO0OOoo0OO )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( url )
  if 41 - 41: ii1ii11IIIiiI . Ii + o0o00Oo0O - ii * o000O0o
  if 33 - 33: I11i1ii1
  if 68 - 68: oOo0O0Ooo . iiiiiiii1 * oO0o % ii
  if 8 - 8: o0o00Oo0O * oOo0O0Ooo - OOooOOo + Ii1I
IiIIiIii1ii = '{PQ},' ; III1I1Iii1 = '{SC},' ; IIIiIII1 = '{XG},' ; OOo0OOo = '{JP},' ; OOIiI1IIIiI1I1i = '{HW},' ; oO00O0oO = '{RT},'
def I1i11111i1i11 ( ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0OO0Oo = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 oOooO0 = 'http://onlinemovies.tube/?s=' + ( oo00O0 ) . replace ( ' ' , '+' )
 I11iiii1I = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay90ZWNobmljYS9zZWFyY2htb3ZpZXMucGhw' ) )
 iiiiI1iiiIi = ( i11 ( 'aHR0cDovLzIxNy4yMTkuMTQzLjEwOC8xMzI3Lw==' ) )
 o0oO0OoO0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbW92aWVzLnBocA==' ) )
 oOOOOOoOO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvbW92L2FsbC5waHA=' ) )
 oooo00 = ( i11 ( 'aHR0cDovL2RsLnZpcG1heC1tb3ZpZS5pbi9Nb3ZpZS8=' ) )
 i1oO = ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL3NlYXJjaC8/cT0=' ) ) + oo00O0
 iI = ( i11 ( 'aHR0cDovL3JlZGVtcHRpb25zdHJlYW1zLmNvLnVrL1JlZGVtcHRpb24vbW92aWVzL2FsbG1vdmllLnBocA==' ) )
 Ii1IIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 69 - 69: Ii1IIIi1 + Ii1IIIi1 * ii1ii11IIIiiI * ooOOOoO + oOo0O0Ooo
 o0O0ooOOoO = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC9tb3ZmdWxsLnBocA==' ) )
 iIi11ii = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXhtb3YucGhw' ) )
 if 46 - 46: Ii1IIIi1
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oOooO0 )
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/9 Links" )
 O0 = O0o0O00Oo0o0 ( I11iiii1I )
 o0oOoO00o . update ( 14 , "" , "Checking Source 2/9 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( iiiiI1iiiIi )
 o0oOoO00o . update ( 28 , "" , "Checking Source 3/9 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( o0oO0OoO0 )
 o0oOoO00o . update ( 40 , "" , "Checking Source 4/9 Links" )
 Ii1iIi111i1i1 = O0o0O00Oo0o0 ( oOOOOOoOO )
 o0oOoO00o . update ( 52 , "" , "Checking Source 5/9 Links" )
 IIOO0ooOo0OoOo0 = O0o0O00Oo0o0 ( i1oO )
 o0oOoO00o . update ( 64 , "" , "Checking Source 6/9 Links" )
 oOo = O0o0O00Oo0o0 ( iI )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/9 Links" )
 i1iIIIiiiI = O0o0O00Oo0o0 ( Ii1IIi )
 o0oOoO00o . update ( 88 , "" , "Checking Source 8/9 Links" )
 if 17 - 17: ooOOOoO / IIiIiII11i * I11i / I1ii11iIi11i + O0OOOoOoo0 . o000O0o
 if 19 - 19: Ii1IIIi1 * ooOOOoO
 oo0ooO0 = O0o0O00Oo0o0 ( o0O0ooOOoO )
 o0oOoO00o . update ( 100 , "" , "Checking Source 9/9 Links" )
 IIiiiiIiIIii = O0o0O00Oo0o0 ( iIi11ii )
 if 85 - 85: ooOoO0O00 % I11i * Ii1I * oO0o . IIiIiII11i
 if i1iIIIiiiI != 'Failed' :
  OooOoOOo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iIIIiiiI )
  for oOooO0 , Iii1I1111ii in OooOoOOo0oO00 :
   O00O = O0o0O00Oo0o0 ( oOooO0 )
   O0Ooo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( O00O )
   for oO00oOOo0Oo , IIi in O0Ooo :
    IIi = ( IIi . replace ( '.' , ' ' ) )
    if iiiI111I in IIi . lower ( ) :
     if '.mkv' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.mp4' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.avi' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 222 , '' , '' , '' )
     elif '.wav' in oO00oOOo0Oo :
      OOiIiIIi1 ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 222 , '' , '' , '' )
     else :
      iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 1006 , '' , '' , '' )
      o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
      o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
      if 69 - 69: ii1ii11IIIiiI / iiiiiiii1 % iiiiiiii1 / I11i1ii1 + iiiiiiii1 / ooOoO0O00
      I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( O0 )
  for oOooO0 , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in i1I :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORred] source Technica[/COLOR]' ) , oOooO0 , 222 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting Technica Links" )
    if 70 - 70: Ii1IIIi1 - I1111IIi . iiiiiiii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 11 - 11: Ii + I11i - iiiiiiii1 * Ii - oOo0O0Ooo
 if ii1ii1ii != 'Failed' :
  iiI1IIIi = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( ii1ii1ii )
  for Oo0o , Iii1I1111ii in iiI1IIIi :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source 3[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( '.' , ' ' ) , ( iiiiI1iiiIi + Oo0o ) , 1006 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 18 , "" , "Getting Source 3 Links" )
 if oooooOoo0ooo != 'Failed' :
  iiIiIIIiiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooooOoo0ooo )
  for oOooO0 , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in iiIiIIIiiI :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORred] source RaizTv[/COLOR]' ) , oOooO0 , 222 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 53 , "" , "Getting RaizTv Links" )
    if 49 - 49: ooOoO0O00 % o000O0o / Ii1IIIi1 . Ii1I - iiiiiiii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if Ii1iIi111i1i1 != 'Failed' :
  iIii1Ooo0oO0 = [ ]
  oOoOoO000OO = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( Ii1iIi111i1i1 )
  for oOooO0 , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in oOoOoO000OO :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    if Iii1I1111ii in iIii1Ooo0oO0 :
     pass
    else :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source Scooby[/COLOR]' ) . replace ( '..&gt;' , '' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , oOooO0 , 1016 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
     iIii1Ooo0oO0 . append ( Iii1I1111ii )
     o0oOoO00o . create ( "[COLORred]*[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 36 , "" , "Getting Scooby Links" )
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if IIOO0ooOo0OoOo0 != 'Failed' :
  o0Oo0oOooOoOo = re . compile ( 'href="([^"]*)".+?src="([^"]*)" alt="Image of (.+?)"' , re . DOTALL ) . findall ( IIOO0ooOo0OoOo0 )
  for oOooO0 , ii1iii1i , Iii1I1111ii in o0Oo0oOooOoOo :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source Snag[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + oOooO0 , 7067 , ii1iii1i )
    o0oOoO00o . update ( 45 , "" , "Getting Snag Links" )
    if 12 - 12: Ii + ooOOOoO - Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0ooO0 != 'Failed' :
  oOoO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0ooO0 )
  for oOooO0 , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in oOoO0o :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    OOiIiIIi1 ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source APPRENTICE[/COLOR]' ) , oOooO0 , 222 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Herovision Links" )
    if 27 - 27: O0OOOoOoo0
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 22 - 22: OOooOOo / oOo0O0Ooo
    if 33 - 33: ooOOOoO
    if 37 - 37: OOooOOo % I11i * oO0o / Ii * IIiIiII11i * O0OOOoOoo0
    if 70 - 70: I11i1ii1 . Ii % OOooOOo + o000O0o
    if 95 - 95: Ii1I
    if 48 - 48: ooOOOoO
    if 14 - 14: iI11I1II1I1I / I11i * I1111IIi
    if 35 - 35: iI11I1II1I1I
    if 34 - 34: oO0o % oOo0O0Ooo . I11i % oO0o % oO0o
    if 30 - 30: oOo0O0Ooo + oOo0O0Ooo
 iiIIii = [ 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 75 - 75: oOo0O0Ooo - I11i1ii1 - oOo0O0Ooo % o000O0o % ii
 for oooOOO00o0 in iiIIii :
  i1Iii = O0Oo000ooO00 + oooOOO00o0 + I1IIIii
  i1iIIIiiiI = O0o0O00Oo0o0 ( i1Iii )
  if i1iIIIiiiI != 'Failed' :
   OooOoOOo0oO00 = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( i1iIIIiiiI )
   for oOooO0 , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in OooOoOOo0oO00 :
    if oo00O0 in Iii1I1111ii . lower ( ) :
     OOiIiIIi1 ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgold] - Source Pandoras[/COLOR]' , oOooO0 , 222 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 89 , "" , "Getting Pandoras Links" )
     if 13 - 13: I11i1ii1 * oO0o % iI11I1II1I1I / I1111IIi * O0OOOoOoo0 . I1ii11iIi11i
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 23 - 23: I11i1ii1 / I1111IIi . O0OOOoOoo0 * ii1ii11IIIiiI
 iiIIii = [ '4Kmovies' , 'hey1080p' , 'hey3D' , 'hey' , '480p' , '720p' , '1080p' , 'mova' , 'movb' , 'movc' , 'movd' , 'move' , 'movf' , 'movg' , 'movh' , 'movi' , 'movj' , 'movk' , 'movl' , 'movm' , 'movn' , 'movo' , 'movp' , 'movq' , 'movr' , 'movs' , 'movt' , 'movu' , 'movv' , 'movw' , 'movx' , 'movy' , 'movz' , '720paction' , '720padventure' , '720panimation' , '720pcomedy' , '720pcrime' , '720pdocumentary' , '720pdrama' , '720pfamily' , '720pfantasy' , '720phorror' , '720pmystery' , '720promance' , '720psci-Fi' , '720psport' , '720pthriller' , '720pwestern' , '1080paction' , '1080padventure' , '1080panimation' , '1080pcomedy' , '1080pcrime' , '1080pdocumentary' , '1080pdrama' , '1080pfamily' , '1080pfantasy' , '1080phorror' , '1080pmystery' , '1080promance' , '1080psci-Fi' , '1080psport' , '1080pthriller' , '1080pwestern' , 'top10action' , 'top10animation' , 'top10biography' , 'top10comedy' , 'top10crime' , 'top10documentary' , 'top10drama' , 'top10family' , 'top10fantasy' , 'top10horror' , 'top10music' , 'top10mystery' , 'top10romance' , 'top10sci-fi' , 'top10sport' , 'top10thriller' , 'top10western' ]
 if 87 - 87: Ii
 if 34 - 34: ooOoO0O00
 for oooOOO00o0 in iiIIii :
  i1Iii = o0OO0Oo + oooOOO00o0
  oo0o = O0o0O00Oo0o0 ( i1Iii )
  if oo0o != 'Failed' :
   o0IiiiI111I = re . compile ( '<li><a href="([^"]*)"> (.+?)</a></li>' ) . findall ( oo0o )
   for Oo0o , Iii1I1111ii in o0IiiiI111I :
    if oo00O0 in Iii1I1111ii . lower ( ) :
     ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + ' -[COLORgold] source 5[/COLOR]' ) . replace ( 'Ganool' , '' ) . replace ( 'ShAaNiG' , '' ) . replace ( 'YIFY' , '' ) . replace ( '[[ Max-Movie.In ]]' , '' ) . replace ( '.mkv' , '' ) . replace ( '.mp4' , '' ) . replace ( '.' , ' ' ) , ( o0OO0Oo + oooOOO00o0 + Oo0o ) , 222 , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Source 5 Links" )
     if 64 - 64: iI11I1II1I1I / I1111IIi / I1ii11iIi11i - Ii1I
     I1I11i ( 'tvshows' , 'Media Info 3' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 100 - 100: I1111IIi + ooOoO0O00 * oO0o
def O0o0OO0000ooo ( ) :
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
 if 24 - 24: Ii1IIIi1
 if 71 - 71: I1111IIi - ooOoO0O00
 if 56 - 56: OOooOOo + o000O0o
 if 74 - 74: O0OOOoOoo0 / iiiiiiii1 / IIiIiII11i - O0OOOoOoo0 / o000O0o % ooOOOoO
 if 19 - 19: I1111IIi % ii + ii
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 if 7 - 7: ooOoO0O00
 if 91 - 91: OOooOOo - OOooOOo . I1111IIi
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3d3dy5pd2F0Y2hzZXJpZXMuY2gvP3M9' ) ) + ( oo00O0 ) . replace ( ' ' , '+' )
 I11iiii1I = 'http://onlinemovies.tube/?s=' + ( oo00O0 ) . replace ( ' ' , '+' )
 iiiiI1iiiIi = ( i11 ( 'aHR0cDovL2RsLm15LWZpbG0ub3JnL3NlcmlhbC8=' ) )
 o0oO0OoO0 = ( i11 ( 'aHR0cDovL3MxLmJpYTJtLmJpei9TZXJpZXMv' ) )
 oooo00 = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9zY29vYnkvc2hvd3MvdHZhbGwucGhw' ) )
 if 33 - 33: iiiiiiii1 - iI11I1II1I1I / ii1ii11IIIiiI % o0o00Oo0O
 iI = ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9oZXJvdmlzaW9uL3ZvZC90dmZ1bGwucGhw' ) )
 Ii1IIi = ( i11 ( 'aHR0cDovL2dlbmlldHYuY28udWsvaW5kZXh0di5waHA=' ) )
 if 80 - 80: I1111IIi % ii - I1111IIi
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 if 27 - 27: iiiiiiii1 - I11i * Ii1I - oOo0O0Ooo
 o0oOoO00o . update ( 0 , "" , "Checking Source 1/11 Links" )
 if 22 - 22: I1ii11iIi11i % ii - I1ii11iIi11i - O0OOOoOoo0 . ii1ii11IIIiiI
 if 100 - 100: IIiIiII11i / iiiiiiii1 / O0OOOoOoo0 - Ii1I * iI11I1II1I1I
 o0O00Oo0 = O0o0O00Oo0o0 ( oO00oOOo0Oo )
 o0oOoO00o . update ( 14 , "" , "Checking Source 3/11 Links" )
 O0 = O0o0O00Oo0o0 ( I11iiii1I )
 o0oOoO00o . update ( 28 , "" , "Checking Source 4/11 Links" )
 ii1ii1ii = O0o0O00Oo0o0 ( iiiiI1iiiIi )
 o0oOoO00o . update ( 40 , "" , "Checking Source 5/11 Links" )
 oooooOoo0ooo = O0o0O00Oo0o0 ( o0oO0OoO0 )
 o0oOoO00o . update ( 52 , "" , "Checking Source 6/11 Links" )
 oo0o = O0o0O00Oo0o0 ( oooo00 )
 o0oOoO00o . update ( 76 , "" , "Checking Source 7/11 Links" )
 if 7 - 7: ooOoO0O00 . I1111IIi % Ii * Ii1I . ooOOOoO % Ii1I
 if 35 - 35: oOo0O0Ooo
 oOo = O0o0O00Oo0o0 ( iI )
 o0oOoO00o . update ( 95 , "" , "Checking Source 9/11 Links" )
 i1iIIIiiiI = O0o0O00Oo0o0 ( Ii1IIi )
 o0oOoO00o . update ( 97 , "" , "Checking Source 10/11 Links" )
 if 48 - 48: ii % ii - oO0o . OOooOOo
 if 22 - 22: I11i1ii1 . Ii . ii . ooOoO0O00
 if i1iIIIiiiI != 'Failed' :
  OooOoOOo0oO00 = re . compile ( '< url="([^"]*)"</url> < name="([^"]*)"</name>' ) . findall ( i1iIIIiiiI )
  for oOooO0 , Iii1I1111ii in OooOoOOo0oO00 :
   O00O = O0o0O00Oo0o0 ( oOooO0 )
   O0Ooo = re . compile ( '<a href="([^"]*)">(.*?)</a>' ) . findall ( O00O )
   for oO00oOOo0Oo , IIi in O0Ooo :
    if iiiI111I in IIi . lower ( ) :
     iiOOooooO0Oo ( ( '[COLOR' + II + ']*' + IIi + '-[COLORgold] source ' + Iii1I1111ii + '[/COLOR]' ) , oOooO0 + oO00oOOo0Oo , 1006 , '' , '' , '' )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 05 , "" , "Getting INDEXER Links" )
     if 12 - 12: OOooOOo % Ii1IIIi1 + o000O0o . o0o00Oo0O % iI11I1II1I1I
     I1I11i ( 'tvshows' , 'Media Info 3' )
 if oOo != 'Failed' :
  ooOO0o = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oOo )
  for oOooO0 , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in ooOO0o :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] source HeroVision[/COLOR]' ) , oOooO0 , 1016 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 10 , "" , "Getting Herovision Links" )
    if 41 - 41: ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
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
 if O0 != 'Failed' :
  i1I = re . compile ( '<a href="([^"]*)">.+?<img src="([^"]*)" alt="([^"]*)" />.+?<span class="([^"]*)">' , re . DOTALL ) . findall ( O0 )
  II1iiI = re . compile ( '<a href="([^"]*)" ><span class="icon-chevron-right">' , re . DOTALL ) . findall ( O0 )
  for oOooO0 , ii1iii1i , Iii1I1111ii , III1Ii1i1I1 in i1I :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    if 'season' in III1Ii1i1I1 :
     O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOooO0 , 90054 , ii1iii1i , ii1iii1i , '' )
    if 'episodes' in III1Ii1i1I1 :
     O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + ' - [COLORred]Source - Tv HUB[/COLOR]' , oOooO0 , 90044 , ii1iii1i , ii1iii1i , '' )
  for oOooO0 in II1iiI :
   O0Oo00OoOo ( '[COLOR' + II + ']' + 'NEXT - [COLORred]Source - Tv HUB[/COLOR]' , oOooO0 , 90053 , III1iII1I1ii + 'Next.png' )
   o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
   o0oOoO00o . update ( 40 , "" , "Getting Tv HUB Links" )
   if 7 - 7: oO0o * Ii * iI11I1II1I1I / Ii1IIIi1 / iiiiiiii1
   I1I11i ( 'tvshows' , 'Media Info 3' )
 if o0O00Oo0 != 'Failed' :
  ii1ooO = re . compile ( '<a href="([^"]*)">(.+?)</a></h2>.+?src="([^"]*)"' , re . DOTALL ) . findall ( o0O00Oo0 )
  for oOooO0 , Iii1I1111ii , ii1iii1i in ii1ooO :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    iiOOooooO0Oo ( '[COLOR' + II + ']' + ( Iii1I1111ii ) . replace ( '&#39;' , '' ) . replace ( '&039;' , '' ) . replace ( '.' , '' ) . replace ( '.' , '' ) . replace ( '#' , '' ) . replace ( 'hack//' , '' ) . replace ( '?' , '' ) + '[COLORgold] - iWatch[/COLOR]' , oOooO0 , 8022 , ii1iii1i , '' , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 45 , "" , "Getting Source iWatch Links" )
    if 35 - 35: O0OOOoOoo0 * Ii1IIIi1
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 65 - 65: IIiIiII11i % ooOoO0O00
    if 13 - 13: oO0o * iiiiiiii1 + I1ii11iIi11i - I1111IIi
    if 31 - 31: oO0o
    if 68 - 68: oO0o + ooOoO0O00 / iI11I1II1I1I + IIiIiII11i * iI11I1II1I1I + Ii1I
    if 77 - 77: Ii - iiiiiiii1 . Ii1I % I1ii11iIi11i . ii1ii11IIIiiI
    if 9 - 9: I11i
    if 55 - 55: Ii1IIIi1 % iI11I1II1I1I + ooOOOoO . I11i1ii1
    if 71 - 71: Ii / ooOoO0O00 + OOooOOo
    if 23 - 23: Ii
 if ii1ii1ii != 'Failed' :
  iiI1IIIi = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( ii1ii1ii )
  for Iii1I1111ii in iiI1IIIi :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 3[/COLOR]' , ( iiiiI1iiiIi + Iii1I1111ii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 60 , "" , "Getting Source 3 Links" )
    if 88 - 88: IIiIiII11i - O0OOOoOoo0 / ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oooooOoo0ooo != 'Failed' :
  iiIiIIIiiI = re . compile ( '<a .*?>(.*?)</a>' ) . findall ( oooooOoo0ooo )
  for Iii1I1111ii in iiIiIIIiiI :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[COLORgold] source 4[/COLOR]' , ( o0oO0OoO0 + Iii1I1111ii ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'TVShows.png' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 70 , "" , "Getting Source 4 Links" )
    if 71 - 71: Ii1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if oo0o != 'Failed' :
  o0IiiiI111I = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oo0o )
  for oOooO0 , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in o0IiiiI111I :
   if iiiI111I in Iii1I1111ii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLORred]*[COLOR' + II + ']' + Iii1I1111ii + '-[COLORgold] Source Scooby[/COLOR]' ) , oOooO0 , 1016 , iII1iii , O0oooo00o0Oo , i1oO0OO0 )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 90 , "" , "Getting Scooby Links" )
    if 19 - 19: I1ii11iIi11i - oO0o + Ii / iI11I1II1I1I
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 1 - 1: I1111IIi % ooOoO0O00
 o0O0OO0o = [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
 for oooOOO00o0 in o0O0OO0o :
  i1Iii = O0Oo000ooO00 + oooOOO00o0 + I1IIIii
  oo0ooO0 = O0o0O00Oo0o0 ( i1Iii )
  if oo0ooO0 != 'Failed' :
   oOoO0o = re . compile ( '<item>.+?<title>(.+?)</title>.+?<description>(.+?)</description>.+?<link>(.+?)</link>.+?<thumbnail>(.+?)</thumbnail>.+?<fanart>(.+?)</fanart>.+?<mode>(.+?)</mode>.+?</item>' , re . DOTALL ) . findall ( oo0ooO0 )
   for Iii1I1111ii , i1oO0OO0 , oOooO0 , ii1iii1i , I11iiiiI1i , iIiiiii1i in oOoO0o :
    if iiiI111I in Iii1I1111ii . lower ( ) :
     iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgold] - Source Pandoras[/COLOR]' , oOooO0 , iIiiiii1i , ii1iii1i , I11iiiiI1i , i1oO0OO0 )
     o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
     o0oOoO00o . update ( 100 , "" , "Getting Pandoras Links" )
     if 41 - 41: oO0o * oO0o / O0OOOoOoo0 + Ii1I . I11i
     I1I11i ( 'tvshows' , 'Media Info 3' )
     if 84 - 84: Ii + oO0o * oOo0O0Ooo + Ii1I / ii1ii11IIIiiI
     if 80 - 80: Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def ooOOO ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 oOooO0 = ( i11 ( 'aHR0cDovL3d3dy5pcHR2bTN1LmNvbS9zZWFyY2g/cT0=' ) ) + ( oo00O0 ) . replace ( ' ' , '+' )
 if 95 - 95: ooOOOoO
 o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Checking Sources" , '' , 'Please Wait' )
 o0oOoO00o . update ( 0 , "" , "Checking Source Links" )
 oO0OOoo0OO = O0o0O00Oo0o0 ( oOooO0 )
 o0oOoO00o . update ( 100 , "" , "Checking Source Links" )
 if 76 - 76: IIiIiII11i - ooOoO0O00 . o0o00Oo0O * Ii % I11i - O0OOOoOoo0
 if oO0OOoo0OO != 'Failed' :
  i1I = re . compile ( '#EXTINF:.+?,(.+?)</.+?="color: red;">http(.+?)</' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for oOooO0 , Iii1I1111ii in i1I :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgold] - source TvOnlineStreams[/COLOR]' ) . replace ( '..&gt;' , '' ) , ( 'http' + oOooO0 ) , 222 , '' )
    o0oOoO00o . create ( "[COLOR'+TEXTCOL+']Genie TV[/COLOR]" , "Getting Sources" , '' , 'Please Wait' )
    o0oOoO00o . update ( 100 , "" , "Getting TvOnlineStreams Links" )
    if 30 - 30: iiiiiiii1 % o000O0o + o000O0o * ii - Ii1I
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
OOoOOo = '{ZH},' ; iIiii1 = '{IX},' ; OO00Oo00o = '{LM},'
if 44 - 44: Ii - I11i + I11i % o0o00Oo0O / ii . Ii1IIIi1
def Ii1111i11 ( url ) :
 O0Ooo000OO00 = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="season" href="([^"]*)">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode" href=".+?">\n(.+?)\n</a>\n</span>\n<span>\n<a class="episode-name" href=".+?">\n(.+?)</a>' ) . findall ( O0Ooo000OO00 )
 for url , O0OO00O0oOO , Iii1iiIi1II1 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( O0OO00O0oOO ) . replace ( 'Sezon' , ' Season ' ) + ( Iii1iiIi1II1 ) . replace ( 'Bölüm' , ' Episode ' ) + Iii1I1111ii , url , 8063 , '' )
  if 51 - 51: I11i1ii1 * I1111IIi * iI11I1II1I1I / OOooOOo % I1111IIi
  if 36 - 36: Ii1I * I11i + Ii + ii
  if 82 - 82: OOooOOo . OOooOOo
  if 10 - 10: I1ii11iIi11i * Ii1I . o000O0o . ii . Ii1IIIi1 * Ii1I
def O0o0O00 ( url ) :
 O0Ooo000OO00 = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)",' , re . DOTALL ) . findall ( O0Ooo000OO00 )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( Iii1I1111ii , url , 222 , '' )
  if 85 - 85: Ii . ooOOOoO + ii1ii11IIIiiI / ii1ii11IIIiiI
  if 43 - 43: I1111IIi . ii - IIiIiII11i
  if 90 - 90: oOo0O0Ooo - iI11I1II1I1I + Ii1I * Ii1IIIi1 * o000O0o
  if 19 - 19: iiiiiiii1 * IIiIiII11i % I1ii11iIi11i - ooOoO0O00
def IIiIiI11IIiII1iII ( ) :
 if 51 - 51: iI11I1II1I1I * OOooOOo / ii1ii11IIIiiI * oO0o
 O0Ooo000OO00 = cloudflare . source ( i11 ( 'aHR0cDovL2RpemlsYWIuY29t' ) )
 i1IIIII11I1IiI = re . compile ( '<li id=".+?">.+?<a href="([^"]*)">.+?<img width="40" height="40" src="([^"]*)" alt=""/>.+?<span class="title">\n(.+?)</span>.+?<span class="alt-title">\n(.+?)</span>.+?</a>.+?</li>' , re . DOTALL ) . findall ( O0Ooo000OO00 )
 for oOooO0 , ii1iii1i , Iii1I1111ii , Iii1iiIi1II1 in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii + '  -  ' + ( Iii1iiIi1II1 ) . replace ( 'sezon' , 'Season' ) . replace ( 'bölüm' , 'Episode' ) , oOooO0 , 8063 , ii1iii1i )
  if 58 - 58: o0o00Oo0O - ooOoO0O00 / O0OOOoOoo0
def OO0O0000oo ( ) :
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cDovL3d3dy50dmd1aWRlLmNvLnVrLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)"  qt-title=".+?" qt-text=".+?<br> .+?" title="([^"]*)".+?class=".+? src="([^"]*)" alt=".+?" /></a>' , re . DOTALL ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 8002 , ii1iii1i )
def O0ooOo ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<table border="0".+?url((.+?));background-repeat: no-repeat;">.+?<tr>.+?<span class="season">(.+?)</span><br>.+?<a href="([^"]*)"+?>(.+?)</span><br>.+?<span class="programmetext">(.+?)</span></a><br>' , re . DOTALL ) . findall ( oooO )
 for ii1iii1i , time , url , Iii1I1111ii , IiiI1i111I1i in i1IIIII11I1IiI :
  iiOOooooO0Oo ( '%s %s' % ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , time ) , url , 1015 , ii1iii1i , IiiI1i111I1i )
  if 34 - 34: ii . IIiIiII11i * iI11I1II1I1I / o0o00Oo0O . oOo0O0Ooo
def iiIIi ( ) :
 if 76 - 76: ooOOOoO * iI11I1II1I1I % IIiIiII11i
 O0Oo00OoOo ( 'Coronation Street' , '' , 8001 , '' )
 O0Oo00OoOo ( 'Eastenders' , '' , 8002 , '' )
 O0Oo00OoOo ( 'Emmerdale' , '' , 8003 , '' )
 O0Oo00OoOo ( 'Hollyoaks' , '' , 8004 , '' )
 O0Oo00OoOo ( 'Im a Celebrity' , '' , 8005 , '' )
 if 54 - 54: I11i - ooOOOoO * OOooOOo * o0o00Oo0O - o0o00Oo0O
 if 28 - 28: ii1ii11IIIiiI * o000O0o * o000O0o * iiiiiiii1
 if 55 - 55: O0OOOoOoo0 - I11i1ii1 / o000O0o + oO0o
 if 94 - 94: I1111IIi / oOo0O0Ooo . IIiIiII11i
def II1oOO0O0Ooo0 ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Holly' in Iii1I1111ii :
   ii1iii1i = 'http://2.bp.blogspot.com/-9c7Sieh1RKs/UjD6TGAEEnI/AAAAAAAAAC8/84uwHfxcuYg/s1600/Hollyoaks.png'
   if 'huge' in oOooO0 :
    ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , ii1iii1i )
   else :
    pass
    if 7 - 7: ii1ii11IIIiiI - ooOoO0O00 % oO0o / iI11I1II1I1I % I11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE_IGNORE_THE ) ;
 if 26 - 26: OOooOOo . Ii1I . Ii1IIIi1
def iIiiII11 ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'East' in Iii1I1111ii :
   ii1iii1i = 'http://3.bp.blogspot.com/-KWHcNbNJU8Y/Vi1ousRl7fI/AAAAAAAAAT8/ksNE12LH0nE/s1600/eastenders.jpg'
   if 'huge' in oOooO0 :
    ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , ii1iii1i )
   else :
    pass
    if 75 - 75: OOooOOo + ii1ii11IIIiiI . Ii / ii1ii11IIIiiI
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 32 - 32: ii1ii11IIIiiI + I1111IIi + Ii1I
def oo00o ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Emmer' in Iii1I1111ii :
   ii1iii1i = 'http://2.bp.blogspot.com/-UfDcxisVV5c/UjH9vUicZ3I/AAAAAAAAADc/8Ozuiz1ojxw/s1600/Emmerdale.jpg'
   if 'huge' in oOooO0 :
    ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , ii1iii1i )
   else :
    pass
    if 14 - 14: ii1ii11IIIiiI + ii1ii11IIIiiI * ii * ooOOOoO + I1ii11iIi11i . oOo0O0Ooo
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 61 - 61: Ii1IIIi1 . Ii1IIIi1
def ii11 ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)".+?target=_blank>(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Coro' in Iii1I1111ii :
   ii1iii1i = 'http://3.bp.blogspot.com/-hofvfBQVexs/UjErIfNdS4I/AAAAAAAAADQ/Q-vVGu3apYU/s1600/corrie.jpg'
   if 'huge' in oOooO0 :
    ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , ii1iii1i )
   else :
    pass
    if 43 - 43: OOooOOo % ii1ii11IIIiiI + I1ii11iIi11i - ii . o0o00Oo0O % I1ii11iIi11i
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 98 - 98: I11i * I1ii11iIi11i - ii1ii11IIIiiI . I11i1ii1
def iI11i1iI ( ) :
 oO0OOoo0OO = OoOooO ( 'http://uksoapshare.blogspot.co.uk/' )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank">(.+?)</a>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Celeb' in Iii1I1111ii :
   ii1iii1i = 'http://3.bp.blogspot.com/-a_yDotWU_pY/VkotKWaG_gI/AAAAAAAAAUk/8Q5iNM6p37k/s1600/iacgoh.jpg'
   if 'huge' in oOooO0 :
    ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.HDTV.x264-SS.mp4' , '' ) . replace ( '_HDTV.x264' , '' ) . replace ( '-SS.mp4' , '' ) . replace ( '_720p.HDTV.x264.' , ' ' ) . replace ( '_720p' , '' ) , oOooO0 . replace ( '\\/' , '/' ) , 8006 , ii1iii1i )
   else :
    pass
    if 95 - 95: Ii % oO0o % I11i1ii1
def i1iOO ( name , url ) :
 IiIII1i = urlresolver . HostedMediaFile ( url ) . valid_url ( )
 if IiIII1i :
  OOoOooO0O = urlresolver . HostedMediaFile ( url ) . resolve ( )
 else :
  oooO = open_url ( url )
  url = re . compile ( 'src="([^"]*)"></iframe>' ) . findall ( oooO ) [ 0 ]
  url = url . split ( '?autoplay' ) [ 0 ]
  oooO = open_url ( url )
  o0o0OoOOOoo = re . compile ( 'mp4","url":"([^"]*)"' ) . findall ( oooO ) [ - 1 ]
  OOoOooO0O = o0o0OoOOOoo . replace ( '\\/' , '/' )
 Ii1i1i1111 = xbmcgui . ListItem ( name , '' , '' )
 Ii1i1i1111 . setPath ( OOoOooO0O )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii1i1i1111 )
 if 89 - 89: iiiiiiii1
 if 16 - 16: ii1ii11IIIiiI + ooOOOoO - Ii1IIIi1 * O0OOOoOoo0 - o0o00Oo0O
def IiiI1Ii1IIi ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5kaXppYm94aGQuY29tLw==' ) )
 i1IIIII11I1IiI = re . compile ( 'class="film menu-item menu-item-type-post_type menu-item-object-page menu-item-36980"><a href="([^"]*)"><i class="fa fa-film"></i><span>(.+?)</span></a></li>' ) . findall ( oooO )
 i1I = re . compile ( 'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-52949"><a href="([^"]*)"><i class="fa fa-"></i><span>(.+?)</span></a></li>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( 'Diziler' , 'Series' ) , oOooO0 , 7071 , III1iII1I1ii + 'popcorn.png' )
 for oOooO0 , Iii1I1111ii in i1I :
  O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( 'Filmler' , 'Movies' ) , oOooO0 , 7071 , III1iII1I1ii + 'popcorn.png' )
  if 8 - 8: Ii1IIIi1 % O0OOOoOoo0 . o000O0o
def iio0o0OoOo0 ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( '<a class="nav-item" href="([^"]*)">(.+?)</a>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Movies' in Iii1I1111ii :
   O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( oOooO0 ) . replace ( 'http://www.snagfilms.com' , '' ) , 7061 , III1iII1I1ii + 'popcorn.png' )
def o000O0OOo00O ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oooO )
 i1IIIII11I1IiI = re . compile ( '<a class="object-link size-poster".+?href="([^"]*)" data-type="category">.+?src="([^"]*)" alt="Image of (.+?)" />' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( "<li class='current'>.+?</li><li ><a href='(.+?)'>.+?</a></li><li" , re . DOTALL ) . findall ( oooO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ii1iii1i )
 for url in i1I :
  O0Oo00OoOo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , ( url ) . replace ( '&#038;' , '&' ) , 7063 , III1iII1I1ii + 'Next.png' )
  if 18 - 18: I11i1ii1 * IIiIiII11i
  if 43 - 43: I11i / o0o00Oo0O + ooOoO0O00 - Ii1I % Ii
def I1I1i ( url ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL3d3dy5zbmFnZmlsbXMuY29tL2NhdGVnb3JpZXMv' ) )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , url , ii1iii1i in i1IIIII11I1IiI :
  if '{{' in Iii1I1111ii :
   pass
  else :
   O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7062 , ii1iii1i )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
O0oOoOOO000 = '{UJ},' ; oOo00o0oO = '{WE},' ; iIiIi = '{WP},' ; I1Iii11II = '{PP},'
def ii11III1 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'data-title="([^"]*)".+?href="([^"]*)".+?src="([^"]*)" alt="Image' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , url , ii1iii1i in i1IIIII11I1IiI :
  if '{{' in Iii1I1111ii :
   pass
  else :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#x27;' , '' ) , 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) , 7067 , ii1iii1i )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOOoO0oo0oo0o ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="film-container">.+?<iframe src="([^"]*)"' , re . DOTALL ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  oo0OO0OooooO0 ( 'http://www.snagfilms.com' + ( url ) . replace ( 'http://www.snagfilms.com' , '' ) )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def oo0OO0OooooO0 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'file: "([^"]*)",.+?label: "([^"]*)"' , re . DOTALL ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 222 , III1iII1I1ii + 'popcorn.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 29 - 29: Ii1I / o000O0o * o0o00Oo0O - Ii - oO0o + ii1ii11IIIiiI
 if 86 - 86: oOo0O0Ooo / Ii1I * ii1ii11IIIiiI % Ii
 if 20 - 20: O0OOOoOoo0 . ii + O0OOOoOoo0 + I11i1ii1 * Ii1I
def i1IIiiI1iii1 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '</h4><p><ul><li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oooO )
 i1I = re . compile ( '<li><a href="([^"]*)">(.+?)<.+?class=' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if '(cooltvseries.com)' in Iii1I1111ii :
   ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + ' -(360)-[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
 for url , Iii1I1111ii in i1I :
  if '(cooltvseries.com)' in Iii1I1111ii :
   ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( ' - (cooltvseries.com).mp4' , '' ) , url , 7053 , III1iII1I1ii + 'CoolSeries.png' )
def o0OoO ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<source type="video/mp4" src="([^"]*)"/>' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  i1iiiIii11 ( ( url ) . replace ( ' ' , '%20' ) )
OOOo00OOooO = '{XX},' ; OO0OOOoO0O0 = '{UD},' ; iII1I1iIi1i = '{YT},' ; O0OO0o = '{JS},' ; Ii11IiiI = '{PF},'
if 34 - 34: OOooOOo * OOooOOo
def OoOo0OoOO0Ooo ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vc2VjcmV0L2Nsb3VkLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<li class="col-sm-2">.+?<a href="#" class="thumbnail" data-src="([^"]*)" data-toggle="modal".+?data-target="#infoModal" name="([^"]*)"> <img src="([^"]*)" alt=".+?" width="130px"' , re . DOTALL ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  ii1ii111 ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , 'http://stream.cloudtv.bz/stream/channel/20/' + ( i11 ( oOooO0 ) ) , 222 , ii1iii1i )
  if 95 - 95: oO0o - I1111IIi % iiiiiiii1
def I111Iii1 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'src="([^"]*)".+?alt=""></a><div class="entry unvoted"><p class="title"><a class="title may-blank " href="([^"]*)" tabindex=.+?>(.+?)</a>' , re . DOTALL ) . findall ( oooO )
 next = re . compile ( '<a href="([^"]*)" rel="nofollow next"' , re . DOTALL ) . findall ( oooO )
 for ii1iii1i , url , Iii1I1111ii in i1IIIII11I1IiI :
  if 'youtu' in url :
   ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&quot;' , '"' ) . replace ( '&' , ' & ' ) , url , 7051 , 'http:' + ii1iii1i )
 for url in next :
  O0Oo00OoOo ( '[COLOR' + II + ']NEXT[/COLOR]' , url , 7050 , III1iII1I1ii + 'Next.png' )
  if 27 - 27: iI11I1II1I1I / oOo0O0Ooo % OOooOOo / oOo0O0Ooo * ii1ii11IIIiiI
def I1IO0 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'rel="shortlink" href="([^"]*)">' , re . DOTALL ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  yt . PlayVideo ( ( url ) . replace ( 'https://youtu.be/' , '' ) )
  if 7 - 7: I1111IIi * I11i1ii1 + OOooOOo
def iIiiIi11iiI1 ( url ) :
 oooO = OoOooO
 i1IIIII11I1IiI = re . compile ( 'id:"([^"]*)",url:"([^"]*)"' , re . DOTALL ) . findall ( oooO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 222 , ii1iii1i )
  if 82 - 82: ooOOOoO % ooOoO0O00
  if 14 - 14: iiiiiiii1 + ii1ii11IIIiiI * I1ii11iIi11i
  if 49 - 49: I1ii11iIi11i
  if 57 - 57: o0o00Oo0O * I11i1ii1 - O0OOOoOoo0 - iI11I1II1I1I * O0OOOoOoo0
  if 9 - 9: I1111IIi . ooOOOoO
def IiIiiiIii1i ( ) :
 if 71 - 71: I11i . Ii1I % IIiIiII11i / iI11I1II1I1I % OOooOOo - Ii1I
 O0Oo00OoOo ( 'All Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'Entertainment' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'Movies' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'Music' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'News' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'Sports' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'Documentary' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'Kids' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'Food' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'Religious' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'USA Channels' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 O0Oo00OoOo ( 'Other' , '' , 7021 , III1iII1I1ii + 'livetv.png' )
 if 58 - 58: iI11I1II1I1I + I11i1ii1 / oO0o % I11i1ii1 % I11i % iI11I1II1I1I
 if 48 - 48: o0o00Oo0O % ooOOOoO * IIiIiII11i . I1ii11iIi11i . Ii1I
def oOo0OO0o0oO ( Cat_Name ) :
 if 41 - 41: Ii - oO0o
 I111II1ii11I1 = False
 iIiiIII = '0'
 if Cat_Name == 'All Channels' : I111II1ii11I1 = True
 if Cat_Name == 'Entertainment' : iIiiIII = '1'
 if Cat_Name == 'Movies' : iIiiIII = '2'
 if Cat_Name == 'Music' : iIiiIII = '3'
 if Cat_Name == 'News' : iIiiIII = '4'
 if Cat_Name == 'Sports' : iIiiIII = '5'
 if Cat_Name == 'Documentary' : iIiiIII = '6'
 if Cat_Name == 'Kids' : iIiiIII = '7'
 if Cat_Name == 'Food' : iIiiIII = '8'
 if Cat_Name == 'Religious' : iIiiIII = '9'
 if Cat_Name == 'USA Channels' : iIiiIII = '10'
 if Cat_Name == 'Other' : iIiiIII = '11'
 if 37 - 37: ii / Ii1I % I11i
 oooO = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"([^"]*)","img":"([^"]*)","stream_url3":".+?","cat_id":"([^"]*)","stream_url2":".+?","stream_url":".+?"}' , re . DOTALL ) . findall ( oooO )
 print 'Len Match: >>>' + str ( len ( i1IIIII11I1IiI ) )
 for Iii1I1111ii , ii1iii1i , II1O0ooo00o0 in i1IIIII11I1IiI :
  i11i1iIi111iiii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ii1iii1i ) . replace ( '\\' , '' )
  if II1O0ooo00o0 == iIiiIII :
   O0Oo00OoOo ( Iii1I1111ii , '' , 7022 , i11i1iIi111iiii )
  elif I111II1ii11I1 == True :
   O0Oo00OoOo ( Iii1I1111ii , '' , 7022 , i11i1iIi111iiii )
  else : pass
  if 14 - 14: ii1ii11IIIiiI / I1111IIi - o0o00Oo0O
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
  if 16 - 16: iiiiiiii1 % iI11I1II1I1I . ooOoO0O00
def o0O0oOOoo0O0 ( Search_Name ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYvRGVzaVN0cmVhbXMvaW5kZXgyMDIucGhwP3RhZz1nZXRfYWxsX2NoYW5uZWwmdXNlcm5hbWU9YnlwYXNz' ) )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oooO )
 i1IIIII11I1IiI = re . compile ( '"id":".+?","name":"' + Search_Name + '","img":"([^"]*)","stream_url3":"([^"]*)","cat_id":".+?","stream_url2":"([^"]*)","stream_url":"([^"]*)"}' , re . DOTALL ) . findall ( oooO )
 for ii1iii1i , oOooO0 , I11iiii1I , iiiiI1iiiIi in i1IIIII11I1IiI :
  i11i1iIi111iiii = i11 ( 'aHR0cDovL3VrdHZub3cuZGVzaXN0cmVhbXMudHYv' ) + ( ii1iii1i ) . replace ( '\\' , '' )
  ii1ii111 ( Search_Name + ': Link 1' , ( oOooO0 ) . replace ( '\\' , '' ) , 222 , i11i1iIi111iiii )
  ii1ii111 ( Search_Name + ': Link 2' , ( I11iiii1I ) . replace ( '\\' , '' ) , 222 , i11i1iIi111iiii )
  ii1ii111 ( Search_Name + ': Link 3' , ( iiiiI1iiiIi ) . replace ( '\\' , '' ) , 222 , i11i1iIi111iiii )
  if 71 - 71: Ii1I + ooOOOoO * I1ii11iIi11i - ooOoO0O00 . o0o00Oo0O % Ii
def I11i1IiI1 ( ) :
 oooO = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+)\s*(.+)\s*' ) . findall ( oooO )
 for Iii1I1111ii , oOooO0 in i1IIIII11I1IiI :
  ii1ii111 ( Iii1I1111ii , ( oOooO0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) + '|connection=keep-alive' , 222 , III1iII1I1ii + 'english.png' )
def o00oOO00 ( ) :
 oooO = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 ] , [ 221 , 72 , 245 , 82 , 68 , 48 , 242 , 99 , 143 , 68 , 9 , 111 , 24 , 118 , 180 , 76 , 29 , 51 , 14 , 100 , 187 , 51 , 105 , 100 , 106 , 121 , 52 , 53 , 240 , 114 , 26 , 98 , 252 , 50 , 197 , 82 , 218 , 112 , 19 , 99 , 94 , 71 , 54 , 120 , 104 , 108 , 174 , 101 , 107 , 72 , 168 , 82 , 191 , 50 , 88 , 76 , 90 , 109 , 138 , 78 , 24 , 118 , 89 , 76 , 218 , 110 , 231 , 86 , 105 , 114 , 252 , 76 , 37 , 50 , 36 , 82 , 96 , 118 , 27 , 100 , 120 , 50 , 160 , 53 , 72 , 115 , 200 , 98 , 80 , 50 , 201 , 70 , 114 , 107 , 9 , 99 , 113 , 121 , 127 , 57 , 155 , 106 , 213 , 97 , 194 , 71 , 192 , 70 , 162 , 116 , 27 , 99 , 46 , 71 , 191 , 108 , 4 , 118 , 24 , 98 , 27 , 109 , 105 , 108 , 89 , 119 , 164 , 100 , 88 , 72 , 237 , 89 , 93 , 117 , 40 , 98 , 211 , 84 , 75 , 78 , 216 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-2,(.+)\s*(.+)\s*' ) . findall ( oooO )
 for Iii1I1111ii , oOooO0 in i1IIIII11I1IiI :
  ii1ii111 ( Iii1I1111ii , ( oOooO0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'xxx.png' )
def o00O0oOOo ( ) :
 oooO = OoOooO ( i11 ( o0OO00 ( 0 , [ 97 , 129 , 72 , 149 , 82 , 100 , 48 , 63 , 99 , 170 , 68 , 159 , 111 , 42 , 118 , 83 , 76 , 128 , 51 , 61 , 100 , 44 , 51 , 201 , 100 , 148 , 121 , 134 , 53 ] , [ 159 , 114 , 70 , 98 , 144 , 50 , 37 , 82 , 253 , 112 , 184 , 99 , 50 , 71 , 154 , 120 , 110 , 108 , 179 , 101 , 250 , 72 , 65 , 82 , 125 , 50 , 52 , 76 , 28 , 109 , 124 , 78 , 191 , 118 , 193 , 76 , 193 , 110 , 145 , 86 , 92 , 114 , 193 , 76 , 41 , 50 , 82 , 82 , 206 , 118 , 32 , 100 , 163 , 50 , 209 , 53 , 191 , 115 , 42 , 98 , 30 , 50 , 237 , 70 , 26 , 107 , 70 , 99 , 64 , 121 , 115 , 57 , 230 , 116 , 32 , 97 , 39 , 88 , 58 , 104 , 38 , 50 , 77 , 98 , 185 , 50 , 86 , 81 , 80 , 117 , 111 , 98 , 226 , 84 , 75 , 78 , 210 , 49 ] ) ) )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+)\s*(.+)\s*' ) . findall ( oooO )
 for Iii1I1111ii , oOooO0 in i1IIIII11I1IiI :
  ii1ii111 ( Iii1I1111ii , ( oOooO0 ) . replace ( '"' , ' ' ) . replace ( '&' , '&' ) . strip ( ) , 222 , III1iII1I1ii + 'vod(1).png' )
  if 37 - 37: o0o00Oo0O
def OOOO00oO ( url ) :
 url
 IiiiiI1i1Iii = xbmcgui . ListItem ( Iii1I1111ii , path = url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiiiiI1i1Iii )
 return
 if 72 - 72: Ii1IIIi1 . OOooOOo / IIiIiII11i
 if 69 - 69: Ii1IIIi1 * IIiIiII11i - I11i1ii1 - ooOoO0O00 + Ii
def iiiiI1iiIi1i ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a class=.+?href="([^"]*)">.+?<div class="videothumboverlay hidden-xs" id=".+?">(.+?)</div>.+?<div class="videothumbbox"><img src="([^"]*)" class="videothumb" alt="([^"]*)"></div>' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( "<a href='(.+?)' class='paginationnext'>Next &raquo;</a></div>" ) . findall ( oooO )
 for url , i1oO0OO0 , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , 'https://www.fitnessblender.com' + url , 7086 , 'https://www.fitnessblender.com' + ii1iii1i , '' , ( i1oO0OO0 ) . replace ( '</p>' , ' ' ) . replace ( '<p>' , ' ' ) )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 for url in i1I :
  O0Oo00OoOo ( 'NEXT' , 'https://www.fitnessblender.com' + url , 7085 , III1iII1I1ii + 'Next.png' )
  if 11 - 11: o0o00Oo0O / iiiiiiii1 / iI11I1II1I1I % ii1ii11IIIiiI
def I1iI1Ii1I1Iii1 ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class=\'videowrapper\'>.+?src="//www.youtube.com/embed/(.+?)?rel=0&amp;wmode=transparent" frameborder="0"></iframe></div>.+?<h3 class="videodetailheader">(.+?)</h3>.+?<p class="videodetailvalue"><img src=\'(.+?)\'/></p>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for url , i1oO0OO0 , ii1iii1i in i1IIIII11I1IiI :
  OOiIiIIi1 ( 'PLAY' , url , 8043 , 'https://www.fitnessblender.com' + ii1iii1i , '' , i1oO0OO0 )
  I1I11i ( 'tvshows' , 'Media Info 3' )
 iiiI1IiI = re . compile ( '<h2 class="videodetailheader">Workout Details</h2>(.+?)</div>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iOO00O0O00oOOO in iiiI1IiI :
  ooo = ( ii1iOO00O0O00oOOO ) . replace ( '<p>' , '' ) . replace ( '</p>' , '' ) . replace ( '<br />' , '' ) . replace ( '&nbsp;' , '' ) . replace ( '<strong>' , '' ) . replace ( '</strong>' , '' ) . replace ( '"' , '' ) . replace ( '<' , '' ) . replace ( '>' , '' ) . replace ( 'a href' , '' ) . replace ( '&#39;' , '\'' ) . replace ( '&rsquo;t' , '' ) . replace ( '&' , '&' )
  iiOOooooO0Oo ( 'INFO' , '' , 7087 , 'https://www.fitnessblender.com' + ii1iii1i , '' , ooo )
  if 17 - 17: I11i1ii1
def I11iIIiIIiIi ( INFO ) :
 iiIiI1i1 ( 'info for workout' , INFO )
 if 45 - 45: oOo0O0Ooo
 if 17 - 17: ii - I11i1ii1 + ii1ii11IIIiiI . ii % I1ii11iIi11i
 if 92 - 92: iiiiiiii1 - Ii1IIIi1 % oO0o - I11i % ooOoO0O00
def IIII1iIii1Ii ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( "<a dir='ltr' href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( ( Iii1I1111ii ) . replace ( 'SlyNet' , '' ) , url , 9031 , III1iII1I1ii + 'Sport.png' )
def OoOO0OO00 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>" , re . DOTALL ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , url , 9032 , III1iII1I1ii + 'icon.png' )
def IiiIi ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:-1,(.+?)<br />(.+?)<br />' , re . DOTALL ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  if '=' in Iii1I1111ii :
   pass
  else :
   ii1ii111 ( ( Iii1I1111ii ) . replace ( '[PremiumSlyNet]' , '[Premium]' ) , url , 222 , III1iII1I1ii + 'icon.png' )
def oOO0oOoooOo ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:-.+?,(.+)</div></li><li class=".+?"><div class=".+?">(.+?)</div>).findall' ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  if '=' in Iii1I1111ii :
   pass
  else :
   ii1ii111 ( Iii1I1111ii , url , 222 , III1iII1I1ii + 'icon.png' )
   if 22 - 22: ooOOOoO
   if 53 - 53: oO0o
   if 96 - 96: ii - iI11I1II1I1I . o000O0o
def ii11iI1i1i1i1i ( url ) :
 ii1ii111 ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 ii1ii111 ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , III1iII1I1ii + 'bamf.png' , III1iII1I1ii + 'bamf.png' )
 O0Oo00OoOo ( '[COLOR' + II + ']SWITCH TO BAMF MOVIES [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90039 , III1iII1I1ii + 'bamf.png' )
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   pass
  else :
   ii1ii111 ( ( Iii1I1111ii ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def iiII1i1II1iIi ( url ) :
 ii1ii111 ( '[COLOR' + II + ']BROUGHT TO YOU BY ANDY BAMF[/COLOR]' , '' , '' , '' )
 ii1ii111 ( '[COLOR' + II + ']REQUIRES F4MTESTER INSTALLED	[/COLOR]' , '' , '' , '' )
 O0Oo00OoOo ( '[COLOR' + II + ']SWITCH TO BAMF CHANNELS [COLORred]CLICK HERE[/COLOR]' , ( i11 ( 'aHR0cDovL2dlbmlldHZjdW50cy5jby51ay9iYW1mZmZmL2JhbWYubTN1' ) ) , 90036 , III1iII1I1ii + 'bamf.png' )
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  if 'mp4' in url :
   ii1ii111 ( ( Iii1I1111ii ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'bamf.png' )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 8 - 8: ii
 if 60 - 60: Ii1IIIi1 * OOooOOo % I1ii11iIi11i
 if 61 - 61: ooOOOoO . iI11I1II1I1I - IIiIiII11i % ooOOOoO * o0o00Oo0O % I1ii11iIi11i
def IiiIIIII111 ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cDovL2lwdHZzYXRsaW5rcy5ibG9nc3BvdC5jby51ay8=' ) )
 i1IIIII11I1IiI = re . compile ( "<h3 class='post-title entry-title' itemprop='name'>.+?<a href='([^']*)'>(.+?)</a>.+?</h3>" , re . DOTALL ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Daily' in Iii1I1111ii :
   O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 9008 , Oo00OOOOO )
def II11iIIIii1i ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '>http(.+?)<br />' , re . DOTALL ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']NOT A GENIE LIST[/COLOR]' , ( 'http' + url ) . replace ( 'amp;' , '' ) , 9009 , Oo00OOOOO )
def o00OooO ( url ) :
 ii1ii111 ( '[COLOR' + II + ']SOME WILL, SOME WONT[/COLOR]' , '' , '' , '' )
 ii1ii111 ( '[COLOR' + II + ']SOME NEVER HAVE, SOME NEVER WILL[/COLOR]' , '' , '' , '' )
 ii1ii111 ( '[COLOR' + II + ']DONT BLAME US![/COLOR]' , '' , '' , '' )
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  ii1ii111 ( ( Iii1I1111ii ) . replace ( '_' , ' ' ) , url , 222 , Oo00OOOOO )
  if 1 - 1: OOooOOo + ii . I1111IIi . iI11I1II1I1I
def iIi1 ( ) :
 oooO = cloudflare . source ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if '.m3u' in oOooO0 :
   O0Oo00OoOo ( ( Iii1I1111ii ) . replace ( '_' , ' ' ) . replace ( '.m3u' , '' ) , ( ( i11 ( 'aHR0cDovL2tvZGkua2Fyb29tZWQubmV0L1BsYXlsaXN0cy8=' ) ) + oOooO0 ) , 9011 , III1iII1I1ii + 'disclose.png' )
def Iii11I1II1 ( url ) :
 oooO = cloudflare . source ( url )
 i1IIIII11I1IiI = re . compile ( '#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  ii1ii111 ( ( Iii1I1111ii ) . replace ( '_' , ' ' ) , url , 222 , '' )
  if 96 - 96: iiiiiiii1 % ooOoO0O00 . O0OOOoOoo0 / o0o00Oo0O
def iiOO0O0Ooo ( ) :
 oooO = OoOooO ( 'http://www.disclose.tv/action/videolist/aliens/page/1/all/channel/1/category/1/' )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)">(.+?)</a></li>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  if 'category' in oOooO0 :
   O0Oo00OoOo ( Iii1I1111ii , 'http://www.disclose.tv/' + oOooO0 , 7010 , III1iII1I1ii + 'disclose.png' )
   if 61 - 61: ooOoO0O00 / ooOoO0O00 + I11i1ii1 . iiiiiiii1 * I11i1ii1
   if 19 - 19: I11i . IIiIiII11i / ooOoO0O00
def Oo00 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'href="([^"]*)"><img width="135" height="76" alt="([^"]*)".+?src="([^"]*)" />' , re . DOTALL ) . findall ( oooO )
 next = re . compile ( '<link rel="next" href="([^"]*)" />' ) . findall ( oooO )
 for url , Iii1I1111ii , ii1iii1i in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , 'http://www.disclose.tv/' + url , 7011 , ii1iii1i )
 for url in next :
  O0Oo00OoOo ( 'NEXT' , url , 7010 , III1iII1I1ii + 'Next.png' )
  if 53 - 53: ooOOOoO + OOooOOo + ooOOOoO
  if 92 - 92: oOo0O0Ooo / Ii1I + ii1ii11IIIiiI * IIiIiII11i
def O0OoOO0O0 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( 'url: "([^"]*)",' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( "src='([^']*)' type='([^']*)' />" , re . DOTALL ) . findall ( oooO )
 iiI1IIIi = re . compile ( '<div class="youtube-player" data-id="([^"]*)">' , re . DOTALL ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  if 'http' in url :
   ii1ii111 ( 'video/flv' , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url , Iii1I1111ii in i1I :
  ii1ii111 ( Iii1I1111ii , url , 222 , III1iII1I1ii + 'disclose.png' )
 for url in iiI1IIIi :
  ii1ii111 ( 'YT Link' , url , 8043 , III1iII1I1ii + 'disclose.png' )
  if 60 - 60: o0o00Oo0O * IIiIiII11i / oOo0O0Ooo . I1ii11iIi11i
  if 54 - 54: iiiiiiii1 - iiiiiiii1 * o0o00Oo0O / ii1ii11IIIiiI + oOo0O0Ooo - iiiiiiii1
def oo0oO0oO00oO ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1".+?src="([^"]*)" scrolling="no".+?<li><a href="#play-1">(.+?)</a></li>' , re . DOTALL ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , ( url + '&fv=&sou=' ) . replace ( 'player' , 'watch' ) , 7000 , III1iII1I1ii + 'icon.png' )
  if 94 - 94: I11i1ii1 * Ii1IIIi1
def o00ooo0oOo0o ( name , url , img ) :
 oO0OOoo0OO = OoOooO ( url )
 OOo00ooOOo0ooO0 = re . compile ( '<iframe class="playerframe" src="([^"]*)" scrolling=".+?" marginwidth=".+?" marginheight=".+?" vspace=".+?" hspace=".+?" allowfullscreen=".+?" webkitallowfullscreen=".+?" mozallowfullscreen=".+?" width=".+?" height=".+?" frameborder=".+?"></iframe>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 I11i1I1 = len ( OOo00ooOOo0ooO0 )
 if 5 - 5: ii - O0OOOoOoo0 - Ii
 if 53 - 53: O0OOOoOoo0 * oO0o / Ii1I + oOo0O0Ooo + ii
 if I11i1I1 == 1 :
  for iIi11111i1II in OOo00ooOOo0ooO0 :
   iIi11111i1II = iIi11111i1II . replace ( 'player' , 'watch' )
   oooooOoo = iIi11111i1II + '&fv=&sou='
   O00 = OoOooO ( oooooOoo )
   O00iIi1i1Ii1 = re . compile ( '<source src="([^"]*)" type=".+?">' , re . DOTALL ) . findall ( O00 )
   for i11i1iIiii in O00iIi1i1Ii1 :
    O00O0O = False
    Resolve ( i11i1iIiii )
    if 22 - 22: o000O0o / ii1ii11IIIiiI
 elif I11i1I1 > 1 :
  if 45 - 45: I11i / Ii - OOooOOo + I1111IIi % O0OOOoOoo0
  for iIi11111i1II in OOo00ooOOo0ooO0 :
   oOO0 = OoOooO ( iIi11111i1II )
   i1i1iIi1IiI = re . compile ( '<iframe width=".*?" height=".*?" frameborder=".*?" src="(.*?)" scrolling=".*?" marginwidth=".*?" marginheight=".*?" vspace=".*?" hspace=".*?" allowfullscreen=".*?" webkitallowfullscreen=".*?" mozallowfullscreen=".*?"></iframe>' , re . DOTALL ) . findall ( oOO0 )
   i11i11Iii = i1i1iIi1IiI
   i11i11Iii = ( str ( i11i11Iii ) ) . replace ( '[\'' , '' ) . replace ( '\']' , '' ) ;
   print 'Stripped url : ' + i11i11Iii
   ii1ii111 ( 'DOUBLE LINK' , i11i11Iii , 424 , '' )
   if 86 - 86: oO0o * IIiIiII11i % ii1ii11IIIiiI * OOooOOo
   for url in i1i1iIi1IiI :
    O0Oo00OoOo ( 'DOUBLE LINK' , url , 424 , '' )
    try :
     I11iiii1I = Google . resolve ( url )
    except :
     pass
    try :
     Ii1I11 = re . findall ( r"{'url': u'(.*?)', 'quality': 'HD'}, {'url': u'(.*?)', 'quality': 'SD'}" , str ( I11iiii1I ) )
     for Oo0O00O0O00 , II1I1i in Ii1I11 :
      if 66 - 66: I1111IIi / OOooOOo % o0o00Oo0O % I11i - Ii1IIIi1 / OOooOOo
      HD_URLS . append ( Oo0O00O0O00 )
      SD_URLS . append ( II1I1i )
    except :
     pass
 else :
  pass
  if 11 - 11: oOo0O0Ooo + I1111IIi
def OooOoOOo0 ( ) :
 if 67 - 67: OOooOOo % I1ii11iIi11i
 if 7 - 7: Ii % Ii1I / iiiiiiii1 % I1ii11iIi11i - oO0o
 O0Oo00OoOo ( 'Genres' , 'http://cnfstudio.com/movies/' , 7002 , III1iII1I1ii + 'Movies.png' )
 if 73 - 73: Ii1I
 O0Oo00OoOo ( 'Search Movies' , '' , 7017 , III1iII1I1ii + 'Movies.png' )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 92 - 92: Ii + o0o00Oo0O * ooOOOoO
 if 60 - 60: I11i / I1ii11iIi11i
def iiiiIooo0O0O0OO ( ) :
 oooO = OoOooO ( 'http://cnfstudio.com/' )
 i1IIIII11I1IiI = re . compile ( '<a href="http://cnfstudio.com/genre/(.+?)">(.+?)</a>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , 'http://cnfstudio.com/genre/' + oOooO0 , 7003 , III1iII1I1ii + 'icon.png' )
  if 65 - 65: I11i - ii / OOooOOo
OOooO0OOoo = xbmcgui . Dialog ( )
if 49 - 49: o000O0o
o0o000OOO = '{UN},' ; I1111iii1ii11 = '{IG},' ; Oooo = '{PL},' ; III1II1I1iI = '{LO},' ; oOOOO = '{LP},' ; Oo0OO0o0oOO0 = '{HA},' ; i1II1IiIIi = '{XD},' ; o0O0 = '{TA},' ; iiI = '{DP},' ; i1I1IIIII1IIi = '{JT},' ; i11iii1II1I1 = '{JJ},' ; IiIi11iI1IIi = '{MM},' ; iII111I = '{FQ},' ; Ooooo0Oo0oOo = '{HH},'
if 33 - 33: ii - ii1ii11IIIiiI - OOooOOo + I1111IIi - ooOoO0O00 . Ii
def i1iII ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div class="movie">.+?<img src="([^"]*)" alt=".+?" />.+?<a href="([^"]*)"><span class="player"></span></a>.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( oooO )
 oOoo0O00OO = re . compile ( "<link rel='next' href='(.+?)'/>" ) . findall ( oooO )
 for ii1iii1i , url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '&#038;' , '' ) . replace ( '&#8216;' , '' ) . replace ( '&#8217;' , '' ) . replace ( '&#8211;' , '' ) , url , 7004 , ii1iii1i )
 oOoo0O00OO = oOoo0O00OO
 for url in oOoo0O00OO :
  O0Oo00OoOo ( 'Next Page' , url , 7003 , III1iII1I1ii + 'Next.png' )
  if 20 - 20: O0OOOoOoo0 - Ii1I * O0OOOoOoo0 + iiiiiiii1
def OOooo ( url ) :
 if 39 - 39: ooOoO0O00
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<div id="play-1" class="player-content"><iframe class="playerframe" src="([^"]*)" scrolling="no".+?</div>' , re . DOTALL ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  i1i = url + '&fv=&sou='
  i1i = i1i . replace ( 'player' , 'watch' )
  ooo0o0o0oOoO = oOOOO00o00 ( i1i )
  OOo00o0oOO0o = oOOOO00o00 ( url )
  if 27 - 27: O0OOOoOoo0 / ooOoO0O00 . O0OOOoOoo0 % ii * o000O0o % IIiIiII11i
  if 40 - 40: ooOOOoO % ii1ii11IIIiiI
def oOOOO00o00 ( url ) :
 if 76 - 76: I11i1ii1 . o000O0o
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<video id=".+?<source src="([^"]*)" type="video/mp4">' , re . DOTALL ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  ii1O0ooooo000 ( url )
  if 24 - 24: iI11I1II1I1I
  if 41 - 41: I1111IIi / ooOoO0O00 / OOooOOo / Ii1IIIi1 . oO0o % OOooOOo
def ooOO0o0ooOo0 ( ) :
 iiOOooooO0Oo ( '[COLOR' + II + ']Local M3u[/COLOR]' , iiI1IiI , 2001 , III1iII1I1ii + 'LocalM3U.png' , O0o0Oo , '' )
 iiOOooooO0Oo ( '[COLOR' + II + ']Remote M3u[/COLOR]' , O0OoO000O0OO , 7080 , III1iII1I1ii + 'RemoteM3U.png' , O0o0Oo , '' )
 if 18 - 18: ii1ii11IIIiiI - O0OOOoOoo0
def i11iI ( ) :
 if os . path . exists ( iiI1IiI ) :
  I111iIii1i1 = open ( iiI1IiI , 'r' )
  for IiiiiI1i1Iii in I111iIii1i1 :
   I1i1I1i1I1 = re . compile ( r'#EXTINF:.+?,(.+?)\n(.+?)\n#' ) . findall ( IiiiiI1i1Iii )
   for Iii1I1111ii , oOooO0 in I1i1I1i1I1 :
    ii1ii111 ( Iii1I1111ii , oOooO0 , 222 , III1iII1I1ii + 'streams.png' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 33 - 33: ii1ii11IIIiiI . o000O0o
def OOOo0OO0ooO0O0O ( url ) :
 if os . path . exists ( Remote ) :
  oO0OOoo0OO = ii1Oo0000oOo ( url )
  i1IIIII11I1IiI = re . compile ( 'EXTINF:.+?,(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
  for Iii1I1111ii , url in i1IIIII11I1IiI :
   url = ( url ) . strip ( )
   ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , '' )
 else :
  OOooO0OOoo . ok ( 'Set m3u path' , 'you need to set path to your m3u file' )
  oo00 . openSettings ( sys . argv [ 0 ] )
  if 76 - 76: I11i / ooOOOoO
  if 95 - 95: OOooOOo - o0o00Oo0O % ii
def Iiii1i1 ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcGx1Z2luLnZpZGVvLkdlbmllVHY=' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/plugin.video.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in i1IIIII11I1IiI :
  oOooO0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3BsdWdpbi52aWRlby5HZW5pZVR2Lw==' ) + oOooO0
 Iii1I1111ii = 'plugin.video.GenieTv'
 if 13 - 13: Ii
 O0O0o00o00O00 ( oOooO0 , Iii1I1111ii )
 if 94 - 94: Ii1I + IIiIiII11i - Ii1I + ooOOOoO
def i1IiiiI1iI ( ) :
 oO0OOoo0OO = OoOooO ( i11 ( 'aHR0cHM6Ly9naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvdHJlZS9tYXN0ZXIvX3JlcG8vcmVwb3NpdG9yeS5HZW5pZVR2' ) )
 i1IIIII11I1IiI = re . compile ( '<span class="css-truncate css-truncate-target"><a href="/GenieTv/Genie_Tv/blob/master/_repo/repository.GenieTv/(.+?)" class="js-navigation-open" id=".+?" title=".+?">.+?</a></span>' ) . findall ( oO0OOoo0OO )
 for oOooO0 in i1IIIII11I1IiI :
  oOooO0 = i11 ( 'aHR0cDovL3Jhdy5naXRodWIuY29tL0dlbmllVHYvR2VuaWVfVHYvbWFzdGVyL19yZXBvL3JlcG9zaXRvcnkuR2VuaWVUdi8=' ) + oOooO0
 Iii1I1111ii = 'repository.GenieTv'
 if 90 - 90: iI11I1II1I1I
 O0O0o00o00O00 ( oOooO0 , Iii1I1111ii )
 if 18 - 18: ooOOOoO * Ii1I / Ii / iI11I1II1I1I * ii . Ii1IIIi1
 if 69 - 69: I1ii11iIi11i * I11i1ii1
def OOI1iI1ii1II ( ) :
 i111I1 = [ '[COLOR' + II + ']CATAGORIES[/COLOR]' , '[COLOR' + II + ']SEARCH[/COLOR]' ]
 iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']TOOLS[/COLOR]' , i111I1 )
 if iI11iI1IiiIiI == 0 :
  OOII1iI ( )
 if iI11iI1IiiIiI == 1 :
  Ooooo0OO ( )
  if 51 - 51: I1111IIi - Ii1IIIi1 / OOooOOo
  if 63 - 63: o000O0o + iiiiiiii1 / oOo0O0Ooo - ii / OOooOOo * ii1ii11IIIiiI
  if 17 - 17: oO0o . oOo0O0Ooo * o0o00Oo0O
  if 81 - 81: Ii1IIIi1
oo00 = xbmcaddon . Addon ( id = 'plugin.video.GenieTv' )
OOooO0OOoo = xbmcgui . Dialog ( )
Oo0o0000o0o0 = xbmc . translatePath ( 'special://home/' )
o0oOoO00o = xbmcgui . DialogProgress ( )
OooOooo00OOO0o = 'https://addons.tvaddons.ag/'
if 41 - 41: Ii1IIIi1 % Ii * oOo0O0Ooo + I11i / o000O0o
def Ooooo0OO ( ) :
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 ooiiI = 'https://addons.tvaddons.ag/search/?keyword=' + iiiI111I
 oO0OOoo0OO = OoOooO ( ooiiI )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , iiIi1IIiI , Iii1I1111ii in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , oOooO0 , 10054 , 'https://addons.tvaddons.ag/' + iiIi1IIiI , O0o0Oo , '' )
  if 56 - 56: ooOoO0O00
  if 11 - 11: Ii % I11i / ooOOOoO * ii
def OOII1iI ( ) :
 oO0OOoo0OO = OoOooO ( OooOooo00OOO0o )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class="thumbnail"><img src="([^"]*)" class="pic" alt=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for oOooO0 , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Repositories' in Iii1I1111ii :
   pass
  elif 'Services' in Iii1I1111ii :
   pass
  elif 'International' in Iii1I1111ii :
   pass
  else :
   iiOOooooO0Oo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , oOooO0 , 10053 , 'https://addons.tvaddons.ag/' + ii1iii1i , O0o0Oo , '' )
   if 82 - 82: I1111IIi
   if 10 - 10: I1ii11iIi11i % Ii1IIIi1 / ooOOOoO * I1111IIi - I11i
def Addon ( url ) :
 oO0OOoo0OO = OoOooO ( url )
 ooOoO00 = re . compile ( '<li class="nextPage"><a class=".+?" href="([^"]*)"><dfn title="next Page">.+?</dfn></a></li>' ) . findall ( oO0OOoo0OO )
 i1IIIII11I1IiI = re . compile ( '<li><a href="([^"]*)"><span class=".+?"><img src="([^"]*)" width=".+?" alt=".+?" class=".+?" /></span><strong>(.+?)</strong></a></li>' ) . findall ( oO0OOoo0OO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  if 'Please' in Iii1I1111ii :
   pass
  else :
   OOiIiIIi1 ( Iii1I1111ii , url , 10054 , 'https://addons.tvaddons.ag/' + ii1iii1i , O0o0Oo , '' )
 for url in ooOoO00 :
  iiOOooooO0Oo ( '[COLOR' + II + ']NEXT PAGE[/COLOR]' , 'https://addons.tvaddons.ag' + url , 10053 , III1iII1I1ii + 'Next.png' , O0o0Oo , '' )
  if 54 - 54: Ii / iI11I1II1I1I % Ii1I / oOo0O0Ooo . iI11I1II1I1I / O0OOOoOoo0
  if 1 - 1: iiiiiiii1 / OOooOOo * OOooOOo - I11i % ii1ii11IIIiiI
def O000o ( url , name ) :
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
   if 44 - 44: IIiIiII11i
def O0O0o00o00O00 ( url , name ) :
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
 if 19 - 19: oO0o % o0o00Oo0O . oOo0O0Ooo / o0o00Oo0O
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "Origin + Genie TV" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Origin + Jaybox[/COLOR]" )
 return
 if 29 - 29: ii1ii11IIIiiI - ooOOOoO . iiiiiiii1 * Ii1I
 if 87 - 87: I1111IIi . O0OOOoOoo0 + o000O0o + IIiIiII11i * o0o00Oo0O % ii
def oo0Oo0oo ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oooO )
 for url , iiIi1IIiI , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , url , 1007 , iiIi1IIiI )
def IIiI1iIiii ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oooO )
 for url , iiIi1IIiI , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 1006 , iiIi1IIiI )
  if 53 - 53: iiiiiiii1 % Ii1I
def ii11iIII111 ( ) :
 oooO = OoOooO ( i11 ( 'aHR0cHM6Ly9nZW5pZXR2Y3VudHMuY28udWsvZ2EvdGVjL01vdmllcy9Nb3ZpZXMucGhw' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oooO )
 for oOooO0 , iII1iii , i1oO0OO0 , I11iiiiI1i , Iii1I1111ii in i1IIIII11I1IiI :
  o00O000o ( Iii1I1111ii , 100109 , oOooO0 , image = iII1iii , isFolder = True )
  if 82 - 82: I11i % I1111IIi - I11i1ii1
def OoOoO0o0oO0 ( url ) :
 import random
 iiII1Ii11 = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 iiII1Ii11 . clear ( )
 i11i1IIIII = [ ]
 I1oo0OOOOOO = [ ]
 oO0OO0O = [ ]
 oO0OOoo0OO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for I11iiii1I , iII1iii , i1oO0OO0 , I11iiiiI1i , Iii1I1111ii in i1IIIII11I1IiI :
  i11i1IIIII . append ( [ I11iiii1I , Iii1I1111ii ] )
  if len ( i11i1IIIII ) == len ( i1IIIII11I1IiI ) :
   for IiiiiI1i1Iii in i11i1IIIII :
    I1IIiIiOoOO0OOo0Oo = random . randint ( 1 , len ( i11i1IIIII ) )
    try :
     iI1iiI1Ii = i11i1IIIII [ int ( I1IIiIiOoOO0OOo0Oo ) ]
    except :
     pass
    if len ( I1oo0OOOOOO ) <= 20 :
     if iI1iiI1Ii [ 1 ] not in oO0OO0O :
      O0 = OoOooO ( iI1iiI1Ii [ 0 ] )
      iiI1IIIi = re . compile ( '&nbsp;<a href="(.+?)">(.+?)</a>' ) . findall ( O0 )
      for i1iiII1iIIIIII , IIIIII11iIiI1III in iiI1IIIi :
       oooooOoo0ooo = OoOooO ( i1iiII1iIIIIII )
       iiIiIIIiiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="(.+?)"' ) . findall ( oooooOoo0ooo )
       for o0Ooo0 , i1i in iiIiIIIiiI :
        if 'panda' in i1i :
         Ii1iIi111i1i1 = OoOooO ( i1i )
         oOoOoO000OO = re . compile ( "url: '(.+?)'" ) . findall ( Ii1iIi111i1i1 )
         for I1ii11iiIIi in oOoOoO000OO :
          if 'http' in I1ii11iiIIi :
           Ii1i1i1111 = xbmcgui . ListItem ( iI1iiI1Ii [ 1 ] , iconImage = IMAGES , thumbnailImage = IMAGES )
           Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : iI1iiI1Ii [ 1 ] } )
           Ii1i1i1111 . setProperty ( "IsPlayable" , "true" )
           iiII1Ii11 . add ( I1ii11iiIIi , Ii1i1i1111 )
           xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Ii1i1i1111 )
           if 61 - 61: O0OOOoOoo0
def o00O000o ( name , mode , url = '' , image = None , isFolder = True , page = 1 , keyword = None , infoLabels = None , contextMenu = None ) :
 if not image :
  image = Oo00OOOOO
 O0ooOOO0 = sys . argv [ 0 ]
 O0ooOOO0 += '?mode=' + str ( mode )
 O0ooOOO0 += '&title=' + urllib . quote_plus ( name )
 O0ooOOO0 += '&image=' + urllib . quote_plus ( image )
 O0ooOOO0 += '&page=' + str ( page )
 if url != '' :
  O0ooOOO0 += '&url=' + urllib . quote_plus ( url )
 if keyword :
  O0ooOOO0 += '&keyword=' + urllib . quote_plus ( keyword )
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = image , thumbnailImage = image )
 if contextMenu :
  Ii1i1i1111 . addContextMenuItems ( contextMenu )
 if infoLabels :
  Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = infoLabels )
 if not isFolder :
  Ii1i1i1111 . setProperty ( "IsPlayable" , "true" )
 Ii1i1i1111 . setProperty ( 'Fanart_Image' , O0o0Oo )
 xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = isFolder )
 if 18 - 18: I11i / Ii % Ii1I * ii
 if 67 - 67: OOooOOo
def ooo0O ( url , iconimage , name ) :
 from imports import cache
 cache = cache . get ( '' , 0 , url )
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oooO )
 for url , iconimage , i1oO0OO0 , I11iiiiI1i , name in i1IIIII11I1IiI :
  if 'http' in url :
   if '.php' in url :
    II1I11IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
    for IiiiiI1i1Iii in II1I11IIi :
     if IiiiiI1i1Iii == url :
      name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
    I1IIiIi ( name , url , 1016 , iconimage , I11iiiiI1i , i1oO0OO0 )
   else :
    if 'youtube' in url :
     II1I11IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for IiiiiI1i1Iii in II1I11IIi :
      if IiiiiI1i1Iii == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o00oo0o ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iconimage , I11iiiiI1i , i1oO0OO0 )
    else :
     II1I11IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
     for IiiiiI1i1Iii in II1I11IIi :
      if IiiiiI1i1Iii == url :
       name = ( '[COLORred]Watched - [/COLOR]' + name ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' ) . replace ( '[COLORred]Watched - [/COLOR][COLORred]Watched - [/COLOR]' , '[COLORred]Watched - [/COLOR]' )
     o00oo0o ( name , url , 222 , iconimage , I11iiiiI1i , i1oO0OO0 )
     I1I11i ( 'tvshows' , 'Media Info 3' )
  else :
   OOO0 ( url , iconimage , name )
   if 75 - 75: oOo0O0Ooo
 else :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oooO )
  for url , iiIi1IIiI , name in i1IIIII11I1IiI :
   if 'http' in url :
    if '.php' in url :
     O0Oo00OoOo ( name , url , 1016 , iiIi1IIiI )
    else :
     if 'youtube' in url :
      print '>>>>>>>>>>>>>>>>>>>>>>> youtube old way'
      ii1ii111 ( name , ( url ) . replace ( 'https://www.youtube.com/watch?v=' , '' ) . replace ( 'http://www.youtube.com/watch?v=' , '' ) , 8043 , iiIi1IIiI )
     else :
      II1I11IIi = re . compile ( 'url="([^"]*)"\n' ) . findall ( str ( OOOO0OOoO0O0 ) )
      for IiiiiI1i1Iii in II1I11IIi :
       if IiiiiI1i1Iii == url :
        name = '[COLORred]Watched - [/COLOR]' + name
      ii1ii111 ( name , url , 222 , iiIi1IIiI )
      I1I11i ( 'tvshows' , 'Media Info 3' )
   else :
    OOO0 ( url , iiIi1IIiI , name )
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 return cache
 if 99 - 99: I11i1ii1 . ii1ii11IIIiiI
def OOO0 ( url , iconimage , name ) :
 iconimage = iconimage
 name = name
 url = url
 o000 = ( url ) . replace ( iIiii1 , 'http' ) . replace ( OO0OOOoO0O0 , '.com' ) ;
 IIIi1IiI1iII = ( o000 ) . replace ( OO00Oo00o , 'a' ) . replace ( IIIiIII1 , 'b' ) . replace ( OOo0OOo , 'c' ) . replace ( oOo00o0oO , 'd' ) . replace ( Oooo , 'e' ) . replace ( i1I1IIIII1IIi , 'f' ) ;
 OOOO0oo = ( IIIi1IiI1iII ) . replace ( OOOo00OOooO , 'g' ) . replace ( Oo0OO0o0oOO0 , 'h' ) . replace ( iII1I1iIi1i , 'i' ) . replace ( Ii11IiiI , 'j' ) . replace ( OOIiI1IIIiI1I1i , 'k' ) . replace ( oO00O0oO , 'l' ) ;
 iii1I1ii1 = ( OOOO0oo ) . replace ( IIiII11Iiii1i1II , 'm' ) . replace ( ii1iIii , 'n' ) . replace ( OoOOOO0 , 'o' ) . replace ( Iii1iii11 , 'p' ) . replace ( Ii11 , 'q' ) . replace ( II11i1 , 'r' ) ;
 IIIi1IIiI = ( iii1I1ii1 ) . replace ( IiIi1I1i , 's' ) . replace ( iIiIi , 't' ) . replace ( IIiiIIi , 'u' ) . replace ( iI1II , 'v' ) . replace ( i11i1IIi , 'w' ) . replace ( Oo0oiiiii11i , 'x' ) ;
 OOoOOo0o0OOo0 = ( IIIi1IIiI ) . replace ( iiiI11I , 'y' ) . replace ( OOo , 'z' ) . replace ( o0o000OOO , '.' ) . replace ( I1111iii1ii11 , '(' ) . replace ( III1II1I1iI , ')' ) . replace ( oOOOO , '/' ) ;
 i1I1I = ( OOoOOo0o0OOo0 ) . replace ( OOoOOo , '1' ) . replace ( I1Iii11II , '2' ) . replace ( iIiiiIII1II , '3' ) . replace ( o0O0 , '4' ) . replace ( iiI , '5' ) . replace ( O0OO0o , '6' ) ;
 oO00oOOOO = ( i1I1I ) . replace ( i11iii1II1I1 , '7' ) . replace ( IiIi11iI1IIi , '8' ) . replace ( iII111I , '9' ) . replace ( Ooooo0Oo0oOo , '0' ) . replace ( IiIIiIii1ii , ':' ) . replace ( III1I1Iii1 , '%' ) ;
 url = ( oO00oOOOO ) . replace ( O0oOoOOO000 , '-' ) . replace ( i1II1IiIIi , '_' ) ;
 ii1ii111 ( name , url , 222 , iconimage ) ;
 if 54 - 54: ooOOOoO * ii
 if 71 - 71: I11i + ii * IIiIiII11i / iiiiiiii1
def o000OOO000o ( ) :
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3VybHMvdXJsLnBocA==' ) )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oooO )
 for oOooO0 , iiIi1IIiI , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , oOooO0 , 1007 , iiIi1IIiI )
def o000ooOO ( url ) :
 if 74 - 74: O0OOOoOoo0 * O0OOOoOoo0 * I11i / o000O0o
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oooO )
 for url , iiIi1IIiI , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 1006 , iiIi1IIiI )
  if 91 - 91: Ii . Ii1I / IIiIiII11i
def O00oO0OOOo0 ( name , url , iconimage = None ) :
 print '--- Playing "{0}". {1}' . format ( name , url )
 iiii111II = xbmcgui . ListItem ( path = url , thumbnailImage = iconimage )
 iiii111II . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiii111II )
 if 64 - 64: ii1ii11IIIiiI - O0OOOoOoo0
 if 12 - 12: ooOoO0O00
def O0o0O00o0o ( url ) :
 oooO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( oooO )
 for url , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  if '-dir-' in Iii1I1111ii :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '-dir-' , '' ) , url , 1012 , ii1iii1i )
  else :
   O0Oo00OoOo ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' , url , 1006 , ii1iii1i )
   if 99 - 99: IIiIiII11i - Ii1I * I1111IIi
def I11I11III ( url ) :
 oooO = ii1Oo0000oOo ( url )
 IIi1i1iI11I11 = ( 'http://afewbitsmore.com/' )
 i1IIIII11I1IiI = re . compile ( '<A HREF="([^"]*)">(.+?)</A><br>' , re . DOTALL ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if '[To Parent Directory]' in Iii1I1111ii :
   Iii1I1111ii = 'HOME'
   pass
  elif 'HOME' in Iii1I1111ii :
   pass
  elif '.m3u' in Iii1I1111ii :
   O0Oo00OoOo ( '[COLOR' + II + ']PLAY ALL[/COLOR]' , IIi1i1iI11I11 + url , 2002 , III1iII1I1ii + 'music.png' )
  elif '.mp3' in Iii1I1111ii :
   ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( 'amp;' , '' ) , IIi1i1iI11I11 + url , 222 , III1iII1I1ii + 'music.png' )
  elif '.m4a' in Iii1I1111ii :
   ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.m4a' , '' ) . replace ( 'amp;' , '' ) , IIi1i1iI11I11 + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) , IIi1i1iI11I11 + url , 1012 , III1iII1I1ii + 'music.png' )
def oo0ooOo0O0 ( url ) :
 oO0OOoo0OO = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( 'EXTINF:(.+?),(.+?)\n(.+?)\n#' , re . DOTALL ) . findall ( oO0OOoo0OO )
 for ii1iii1i , Iii1I1111ii , url in i1IIIII11I1IiI :
  ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '_' , ' ' ) , url , 222 , III1iII1I1ii + 'music.png' )
  if 99 - 99: oOo0O0Ooo - iI11I1II1I1I
def oOO0oo0o0ooO00 ( url ) :
 oooO = ii1Oo0000oOo ( url )
 IIi1i1iI11I11 = url
 i1IIIII11I1IiI = re . compile ( "<a href='(.+?)'>(.+?)</a>" ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  if '.mp3' in Iii1I1111ii :
   print '<<<<<<<<<<<<<<<<<<<' + url + '>>>>>>>>>>>>>>>>>>>>>>>>>>>'
   ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.mp3' , '' ) . replace ( '/' , '' ) , 'http://hypem.com' + url , 222 , III1iII1I1ii + 'music.png' )
  else :
   O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '/' , '' ) , IIi1i1iI11I11 + url , 1011 , III1iII1I1ii + 'music.png' )
def i1i1IIoO0O ( ) :
 oooO = ii1Oo0000oOo ( i11 ( 'aHR0cDovL3d3dy5jeW4ubmV0L211c2ljLw==' ) )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)"><img src="([^"]*)"><br>(.+?)</a></td>' , re . DOTALL ) . findall ( oooO )
 for oOooO0 , ii1iii1i , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , ( 'http://www.cyn.net/music/' + oOooO0 ) . replace ( ' ' , '%20' ) , 1031 , ( 'http://www.cyn.net/music/' + ii1iii1i ) . replace ( ' ' , '%20' ) )
def O0OO0OoO00oOo ( url , img ) :
 oooO = ii1Oo0000oOo ( url )
 I11iiii1I = url
 img = img
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.mp3' , '' ) , ( I11iiii1I + '/' + url ) . replace ( ' ' , '%20' ) , 222 , img )
  if 35 - 35: IIiIiII11i . Ii1IIIi1 + iI11I1II1I1I . ooOoO0O00 - OOooOOo + I1111IIi
def i11i ( url ) :
 oooO = ii1Oo0000oOo ( url )
 I11iiii1I = url
 i1IIIII11I1IiI = re . compile ( 'alt="([^"]*)"></td><td><a href="([^"]*)">(.+?)</a>' , re . DOTALL ) . findall ( oooO )
 for type , url , Iii1I1111ii in i1IIIII11I1IiI :
  if '[VID]' in type :
   ii1ii111 ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( '.mp4' , '' ) . replace ( '_H.264-AAC' , '' ) . replace ( '(' , ' (' ) . replace ( ')' , ') ' ) , I11iiii1I + url , 222 , III1iII1I1ii + 'music.png' )
  if '[DIR]' in type :
   i11i ( I11iiii1I + url )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
 if 55 - 55: I1ii11iIi11i % iiiiiiii1 . IIiIiII11i
 if 53 - 53: o0o00Oo0O / oO0o % Ii
def II1IIiiI1 ( ) :
 o0OO0Oo = ( i11 ( 'aHR0cDovL2h5cGVtLmNvbS9kb3dubG9hZC8=' ) )
 oo00O0 = OOooO0OOoo . input ( 'Search' , type = xbmcgui . INPUT_ALPHANUM )
 iiiI111I = oo00O0 . lower ( )
 oOooO0 = ( i11 ( 'aHR0cDovL3JhaXp0di5jby51ay9SYXlzUmF2ZXJzL2xpc3QvYWxsbXVzaWMucGhw' ) )
 oO00oOOo0Oo = ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) )
 I11iiii1I = ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) )
 if 11 - 11: iiiiiiii1 + ooOoO0O00 - O0OOOoOoo0 - oO0o * I11i1ii1 / I11i1ii1
 oO0OOoo0OO = O0o0O00Oo0o0 ( oOooO0 )
 o0O00Oo0 = O0o0O00Oo0o0 ( oO00oOOo0Oo )
 O0 = O0o0O00Oo0o0 ( I11iiii1I )
 if 4 - 4: iI11I1II1I1I - Ii * oO0o . iiiiiiii1 + I11i
 if oO0OOoo0OO != 'Failed' :
  i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /><description = "([^"]*)" /><background = "([^"]*)" </background></a><br><b>(.+?)</b>' ) . findall ( oO0OOoo0OO )
  for oOooO0 , iII1iii , i1oO0OO0 , O0oooo00o0Oo , Iii1I1111ii in i1IIIII11I1IiI :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    iiOOooooO0Oo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgold] source RaysRavers[/COLOR]' ) . replace ( '_' , ' ' ) , oOooO0 , 1016 , iII1iii , I11iiiiI1i , i1oO0OO0 )
    if 11 - 11: OOooOOo % Ii1I - ii1ii11IIIiiI - iiiiiiii1
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if o0O00Oo0 != 'Failed' :
  ii1ooO = re . compile ( '<a href="([^"]*)">(.+?)</a>' ) . findall ( o0O00Oo0 )
  for oOooO0 , Iii1I1111ii in ii1ooO :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgold] source 1' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL3Bhbmljc3RyZWFtLm5ldC9zdHJlYW1zLw==' ) ) + oOooO0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 58 - 58: OOooOOo . ii1ii11IIIiiI / I1111IIi * o000O0o
    I1I11i ( 'tvshows' , 'Media Info 3' )
 if O0 != 'Failed' :
  i1I = re . compile ( '<td><a href="([^"]*)">(.+?)</a></td>' ) . findall ( O0 )
  for oOooO0 , Iii1I1111ii in i1I :
   if oo00O0 in Iii1I1111ii . lower ( ) :
    O0Oo00OoOo ( ( '[COLOR' + II + ']' + Iii1I1111ii + '[COLORgold] source 2' ) . replace ( '..&gt;' , '' ) . replace ( '/' , '' ) + '[/COLOR]' , ( ( i11 ( 'aHR0cDovL21hc2xvdmQubm8taXAub3JnL3B1YmxpYy9tcDMv' ) ) + oOooO0 ) . replace ( ' ' , '%20' ) , 1006 , III1iII1I1ii + 'Music.png' )
    if 70 - 70: ii
    I1I11i ( 'tvshows' , 'Media Info 3' )
    if 51 - 51: o000O0o / IIiIiII11i + I11i1ii1 / ooOOOoO . O0OOOoOoo0
    if 77 - 77: iI11I1II1I1I * OOooOOo + Ii * I11i1ii1
    if 81 - 81: ii1ii11IIIiiI * O0OOOoOoo0 % ii1ii11IIIiiI % Ii % ooOoO0O00 / I11i
    if 53 - 53: OOooOOo
    if 55 - 55: I11i1ii1 % ooOoO0O00 / oO0o
    if 77 - 77: o0o00Oo0O % o000O0o % o000O0o
IIiII11Iiii1i1II = '{SF},' ; ii1iIii = '{IF},' ; OoOOOO0 = '{PW},' ; iIiiiIII1II = '{AM},' ; Iii1iii11 = '{GF},' ; Ii11 = '{DD},' ; II11i1 = '{UO},' ; IiIi1I1i = '{LE},' ; IIiiIIi = '{ZY},' ; iI1II = '{UE},' ; i11i1IIi = '{PE},' ; Oo0oiiiii11i = '{JE},' ; iiiI11I = '{TH},' ; OOo = '{LK},'
if 12 - 12: O0OOOoOoo0 / I11i1ii1 * iI11I1II1I1I / IIiIiII11i . Ii / IIiIiII11i
if 66 - 66: I1111IIi * o000O0o
def iIi11i1 ( ) :
 oooO = OoOooO ( 'http://www.iwatchseries.me/tv-list/' )
 i1IIIII11I1IiI = re . compile ( '<h5><a href="([^"]*)"><strong>(.+?)</strong></a></h5>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , oOooO0 , 8021 , III1iII1I1ii + 'iwatch.png' )
  I1I11i ( 'movies' , 'MAIN' )
def oo0oo00 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<h5><strong><a href="([^"]*)">(.+?)</a>(.+?)</strong></h5>' ) . findall ( oooO )
 for url , Iii1I1111ii , I1iII in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii + I1iII , url , 8022 , III1iII1I1ii + 'iwatch.png' )
def ooO00OoO ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '<iframe src="([^"]*)"' ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  print '>>>>>>>>>>>>>>>>>>>>' + url
  oo0OOO0O0 ( url )
def oo0OOO0O0 ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '{.+?"file" : "([^"]*)",.+?"default" : true.+?"label" : "([^"]*)"' , re . DOTALL ) . findall ( oooO )
 i1I = re . compile ( 'setup\(\{.+?file: "([^"]*)",.+?skin' , re . DOTALL ) . findall ( oooO )
 iiI1IIIi = re . compile ( "{ label: '([^']*)', file:.+?'([^']*)' }" ) . findall ( oooO )
 iiIiIIIiiI = re . compile ( '"file":"([^"]*)","label":"([^"]*)"' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( 'VidSpot - ' + Iii1I1111ii , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url in i1I :
  ii1ii111 ( 'VodLocker' , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for url , Iii1I1111ii in iiIiIIIiiI :
  ii1ii111 ( 'VidUp' + Iii1I1111ii , url , 222 , III1iII1I1ii + 'iwatch.png' )
 for Iii1I1111ii , url in iiI1IIIi :
  print '<><><><><><><><><><><> before   ' + url
  if 'hevideo' in url :
   print '>>>>>>>>>>>>>>>>>>>>>>>>>' + url
   ii1ii111 ( 'TheVideo - ' + Iii1I1111ii , url , 222 , III1iII1I1ii + 'iwatch.png' )
   if 99 - 99: ooOoO0O00 - o0o00Oo0O / IIiIiII11i + IIiIiII11i . I1111IIi / o000O0o
def i1ii1iIiI1 ( ) :
 oooO = cloudflare . source ( 'http://www.animeland.me/anime-list' )
 i1IIIII11I1IiI = re . compile ( 'letter-spacing:-1px;" href="([^"]*)">(.+?)</a></li>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , oOooO0 , 1021 , III1iII1I1ii + 'anime.png' )
  if 17 - 17: Ii . ii1ii11IIIiiI - I1111IIi / iI11I1II1I1I + ii - I11i1ii1
  if 59 - 59: OOooOOo
def ooOOOooOooOOoO0O ( ) :
 oooO = OoOooO ( 'http://www.animetoon.org/cartoon' )
 i1IIIII11I1IiI = re . compile ( '<td><a href="([^"]*)">(.+)</a></td>' ) . findall ( oooO )
 for oOooO0 , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , oOooO0 , 1002 , III1iII1I1ii + 'anime.png' )
  if 50 - 50: O0OOOoOoo0 . oOo0O0Ooo
  if 93 - 93: ii1ii11IIIiiI % iI11I1II1I1I * O0OOOoOoo0 / OOooOOo * Ii
  if 26 - 26: I11i1ii1 . O0OOOoOoo0
def o0ooOoOoO0o ( url ) :
 oooO = OoOooO ( url )
 i1I = re . compile ( '<img src="([^"]*)" id="series_image" width="250" height="370" alt=".+?" />' ) . findall ( oooO )
 for ii1iii1i in i1I :
  OOOOOO = ii1iii1i
 iiI1IIIi = re . compile ( '<li><a href="([^"]*)">Next</a></li>' ) . findall ( oooO )
 for url in iiI1IIIi :
  O0Oo00OoOo ( 'NEXT PAGE' , url , 1002 , III1iII1I1ii + 'Next.png' )
 i1IIIII11I1IiI = re . compile ( '&nbsp;<a href="([^"]*)">(.+?)</a>' ) . findall ( oooO )
 for url , Iii1I1111ii in i1IIIII11I1IiI :
  O0Oo00OoOo ( Iii1I1111ii , url , 1003 , OOOOOO )
 xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def OOo00OoOoo ( url , IMAGE ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( '"playlist">(.+?)</span></div><div><iframe src="([^"]*)"' ) . findall ( oooO )
 for Iii1I1111ii , url in i1IIIII11I1IiI :
  print Iii1I1111ii + '     ' + url
  if 'easy' in url :
   o0Oi1i1i11IIii ( url )
  elif 'playpanda' in url :
   o0Oi1i1i11IIii ( url )
   if 11 - 11: I11i1ii1 . iiiiiiii1 - O0OOOoOoo0 . I11i
  xbmcplugin . addSortMethod ( O000oo0O , xbmcplugin . SORT_METHOD_TITLE ) ;
def o0Oi1i1i11IIii ( url ) :
 oooO = OoOooO ( url )
 i1IIIII11I1IiI = re . compile ( "url: '(.+?)'," ) . findall ( oooO )
 for url in i1IIIII11I1IiI :
  ii1ii111 ( 'STREAM' , url , 222 , III1iII1I1ii + 'anime.png' )
  if 41 - 41: o000O0o / oO0o - oO0o + I11i1ii1 * Ii1IIIi1
  if 13 - 13: iiiiiiii1 * IIiIiII11i - OOooOOo
def II11iii ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 O00O0oOO00O00 . add_header ( 'referer' , url )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 85 - 85: oO0o
def ii1Oo0000oOo ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0" )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 5 - 5: ii1ii11IIIiiI % ii1ii11IIIiiI * iiiiiiii1
def IiiiiIIi1i ( url ) :
 xbmcplugin . addSortMethod ( handle = int ( sys . argv [ 1 ] ) , sortMethod = xbmcplugin . SORT_METHOD_TITLE )
 iiI111iIi1 = ( '%s%s' % ( I1i1ii1ii , url ) )
 i1i = ii1Oo0000oOo ( url )
 i1IIIII11I1IiI = re . compile ( '<a href="([^"]*)" target="_blank"><img src="([^"]*)" style="max-width:200px;" /></a><br><b>(.+?)</b>' ) . findall ( i1i )
 for url , iiIi1IIiI , Iii1I1111ii in i1IIIII11I1IiI :
  ii1ii111 ( '%s' % ( '[COLOR' + II + ']' + Iii1I1111ii + '[/COLOR]' ) . replace ( 'GenieTv' , '[COLOR green]GenieTV[/COLOR]' ) . replace ( '.' , ' ' ) . replace ( 'mp4' , '' ) . replace ( 'mkv' , '' ) . replace ( '_' , ' ' ) , '%s' % ( url ) , 222 , iiIi1IIiI )
  if 16 - 16: oO0o * IIiIiII11i
def IiI1ii1ii ( url ) :
 if oo00 . getSetting ( 'down' ) == 'true' :
  iIiIiiiII11i ( url , Iii1I1111ii )
 else :
  OOOoOO0o ( url )
def OOOoOO0o ( url ) :
 import urlresolver
 try :
  I1oO0oO00OO00 = urlresolver . resolve ( url ) . strip ( )
  xbmc . Player ( ) . play ( I1oO0oO00OO00 , xbmcgui . ListItem ( Iii1I1111ii ) )
 except :
  try :
   xbmc . Player ( ) . play ( url , xbmcgui . ListItem ( Iii1I1111ii ) )
  except :
   xbmcgui . Dialog ( ) . notification ( "GenieTv" , "unplayable stream" )
   sys . exit ( )
def ii1O0ooooo000 ( url ) :
 if 75 - 75: I11i + oOo0O0Ooo % I11i1ii1 * iiiiiiii1
 OoOOo = open ( o00OO00OoO , "a" )
 OoOOo . write ( 'url="' + url + '"\n' )
 OoOOo . close
 if 87 - 87: IIiIiII11i + o0o00Oo0O / O0OOOoOoo0 * I11i1ii1
 OOo00O = xbmc . Player ( o0Ii1Iii111IiI1 ( ) )
 import urlresolver
 try : OOo00O . play ( url )
 except : pass
 from urlresolver import common
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'LOADING' , 'Opening %s Now' % ( Iii1I1111ii ) )
 OOo00O = xbmc . Player ( o0Ii1Iii111IiI1 ( ) )
 url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 if o0oOoO00o . iscanceled ( ) :
  print "[COLORred]STREAM CANCELLED[/COLOR]"
  OOooO0OOoo = xbmcgui . Dialog ( )
  if OOooO0OOoo . yesno ( "[B]CANCELLED[/B]" , '[B]Was There A Problem[/B]' , '' , "" , 'Yes' , 'No' ) :
   OOooO0OOoo . ok ( "Message Send" , "Your Message Has Been Sent" )
  else :
   return
 else :
  try : OOo00O . play ( url )
  except : pass
  try : oo00 . resolve_url ( url )
  except : pass
  o0oOoO00o . close ( )
def iIiIiiiII11i ( url , name ) :
 url = url
 name = name
 if '.mp4' in url :
  oOOoo = '.mp4'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOoOO0o ( url )
  if iI11iI1IiiIiI == 1 :
   Ooo0 ( url , name , oOOoo )
 elif '.mkv' in url :
  oOOoo = '.mkv'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOoOO0o ( url )
  if iI11iI1IiiIiI == 1 :
   Ooo0 ( url , name , oOOoo )
 elif '.mp3' in url :
  oOOoo = '.mp3'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOoOO0o ( url )
  if iI11iI1IiiIiI == 1 :
   Ooo0 ( url , name , oOOoo )
 elif '.avi' in url :
  oOOoo = '.avi'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOoOO0o ( url )
  if iI11iI1IiiIiI == 1 :
   Ooo0 ( url , name , oOOoo )
 elif '.mov' in url :
  oOOoo = '.mov'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOoOO0o ( url )
  if iI11iI1IiiIiI == 1 :
   Ooo0 ( url , name , oOOoo )
 elif '.mpeg' in url :
  oOOoo = '.mpeg'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOoOO0o ( url )
  if iI11iI1IiiIiI == 1 :
   Ooo0 ( url , name , oOOoo )
 elif '.mpg' in url :
  oOOoo = '.mpg'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOoOO0o ( url )
  if iI11iI1IiiIiI == 1 :
   Ooo0 ( url , name , oOOoo )
 elif '.flv' in url :
  oOOoo = '.flv'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOoOO0o ( url )
  if iI11iI1IiiIiI == 1 :
   Ooo0 ( url , name , oOOoo )
 elif '.wmv' in url :
  oOOoo = '.wmv'
  i111I1 = [ '[COLOR' + II + ']PLAY[/COLOR]' , '[COLOR' + II + ']DOWNLOAD[/COLOR]' ]
  iI11iI1IiiIiI = xbmcgui . Dialog ( ) . select ( '[COLOR' + II + ']Play/Download[/COLOR]' , i111I1 )
  if iI11iI1IiiIiI == 0 :
   OOOoOO0o ( url )
  if iI11iI1IiiIiI == 1 :
   Ooo0 ( url , name , oOOoo )
 else :
  OOOoOO0o ( url )
def Ooo0 ( url , name , cat ) :
 o0oOoO00oo0oOo ( )
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
def o0oOoO00oo0oOo ( ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( ooOoOoo0O ) )
 if not os . path . exists ( ooOoOoo0O ) :
  OOooO0OOoo . ok ( '[COLOR=white]GenieTv[/COLOR]' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' , '' , '' )
  oo00 . openSettings ( sys . argv [ 0 ] )
def iiOO00O ( url ) :
 o0oOoO00o = xbmcgui . DialogProgress ( )
 o0oOoO00o . create ( 'Fetching Your Video' , 'Fetching Your Video' )
 o0oOoO00o . update ( 0 , '%s' % Iii1I1111ii )
 xbmc . sleep ( 1 )
 OOo00O = xbmc . Player ( o0Ii1Iii111IiI1 ( ) )
 o0oOoO00o . update ( 100 , '%s' % Iii1I1111ii )
 xbmc . sleep ( 1 )
 OOo00O . play ( url ) . strip ( )
 o0oOoO00o . close ( )
 if 15 - 15: o0o00Oo0O
def i1iiiIii11 ( url ) :
 OOo00O = xbmc . Player ( o0Ii1Iii111IiI1 ( ) )
 import urlresolver
 url = ( url ) . strip ( )
 try : OOo00O . play ( url ) . strip ( )
 except : pass
 if 14 - 14: O0OOOoOoo0 % I11i % I11i . Ii1IIIi1 * Ii1I - ii1ii11IIIiiI
def ooOOooooo0Oo ( url ) :
 OOo00O = xbmc . Player ( o0Ii1Iii111IiI1 ( ) )
 import urlresolver
 I1iii1IiI11I11I = 'http://genietv.co.uk/guide/intro.mp4'
 xbmc . sleep ( 10 )
 OOo00O . play ( I1iii1IiI11I11I )
 xbmc . sleep ( 1 )
 OOo00O . play ( url )
 if 2 - 2: iI11I1II1I1I * OOooOOo . o0o00Oo0O / oO0o
 if 3 - 3: Ii1I
def o0Ii1Iii111IiI1 ( ) :
 try :
  o0oo00OOoOoOOOO = getSet ( "core-player" )
  if ( o0oo00OOoOoOOOO == 'DVDPLAYER' ) : o000o00oooO = xbmc . PLAYER_CORE_DVDPLAYER
  elif ( o0oo00OOoOoOOOO == 'MPLAYER' ) : o000o00oooO = xbmc . PLAYER_CORE_MPLAYER
  elif ( o0oo00OOoOoOOOO == 'PAPLAYER' ) : o000o00oooO = xbmc . PLAYER_CORE_PAPLAYER
  else : o000o00oooO = xbmc . PLAYER_CORE_AUTO
 except : o000o00oooO = xbmc . PLAYER_CORE_AUTO
 return o000o00oooO
 return True
 if 99 - 99: O0OOOoOoo0 / o000O0o . Ii / ooOOOoO + ooOoO0O00 - ooOOOoO
def O0Oo00OoOo ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O0ooOOO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii11Iii1i1ii = True
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  o0oO0O00oOo = [ ]
  o0oO0O00oOo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o0oO0O00oOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o0oO0O00oOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ii1i1i1111 . addContextMenuItems ( o0oO0O00oOo )
 Ii11Iii1i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = True )
 return Ii11Iii1i1ii
 if 50 - 50: ooOoO0O00
def oOO0o ( name , url , mode , iconimage , fanart , description ) :
 if 56 - 56: oO0o + iiiiiiii1 / ii1ii11IIIiiI
 O0ooOOO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii11Iii1i1ii = True
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1i1111 . setProperty ( "Fanart_Image" , fanart )
 Ii11Iii1i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = True )
 return Ii11Iii1i1ii
 if 75 - 75: OOooOOo
def ii1ii111 ( name , url , mode , iconimage , showcontext = True , allinfo = { } ) :
 O0ooOOO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Ii11Iii1i1ii = True
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if showcontext :
  o0oO0O00oOo = [ ]
  o0oO0O00oOo . append ( ( 'Queue Item' , 'RunPlugin(%s?mode=100107)' % sys . argv [ 0 ] ) )
  if showcontext == 'fav' :
   o0oO0O00oOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o0oO0O00oOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , mode ) ) )
  Ii1i1i1111 . addContextMenuItems ( o0oO0O00oOo )
 Ii11Iii1i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = False )
 return Ii11Iii1i1ii
 if 96 - 96: I11i * ooOOOoO * I1ii11iIi11i
 if 36 - 36: ii + I11i1ii1 . o000O0o * I11i1ii1 + I1111IIi
 if 45 - 45: o000O0o / O0OOOoOoo0 + Ii1I - I1ii11iIi11i - I11i1ii1 . iI11I1II1I1I
 if 52 - 52: oOo0O0Ooo + ooOoO0O00 . O0OOOoOoo0 * oOo0O0Ooo
 if 31 - 31: I1ii11iIi11i % iI11I1II1I1I . o0o00Oo0O
 if 80 - 80: ooOOOoO / I1ii11iIi11i + Ii1I
def Iii11i1Ii ( url , heading , announce ) :
 class Oo0oo00 ( ) :
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
   try : OOoO = open ( announce ) ; IiiiIIi11II = OOoO . read ( )
   except : IiiiIIi11II = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiiiIIi11II ) )
   return
 Oo0oo00 ( )
 Oo0oo00 ( )
def iiIiI1i1 ( heading , announce ) :
 class Oo0oo00 ( ) :
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
   try : OOoO = open ( announce ) ; IiiiIIi11II = OOoO . read ( )
   except : IiiiIIi11II = announce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( IiiiIIi11II ) )
   return
 Oo0oo00 ( )
 Oo0oo00 ( )
def Ii1I1Ii ( ) :
 Iii11i1Ii ( III1iII1I1ii + 'genie.png' , 'GenieTv Recomended Sources' , '[COLORwhite]GenieTv[/COLOR] [CR]  [COLORred]http://genietv.com/repo[/COLOR] [CR][COLORwhite]RayRavers[/COLOR] [CR]  [COLORred]http://repo.raiztv.co.uk/[/COLOR] [CR][COLORwhite]Quick Silver Music[/COLOR] [CR]  [COLORred]http://quicksilver-music.com/addon[/COLOR] [CR][COLORwhite]Back2Basics[/COLOR] [CR]  [COLORred]http://archive.org/download/back2basicsrepo[/COLOR] [CR]' )
 if 51 - 51: ooOOOoO % IIiIiII11i - I11i % oO0o * Ii * O0OOOoOoo0
 if 82 - 82: ii / oOo0O0Ooo * IIiIiII11i - ii % iI11I1II1I1I * oO0o
 if 32 - 32: Ii - OOooOOo * ooOOOoO . I1ii11iIi11i * I11i1ii1
 if 21 - 21: Ii1IIIi1
 if 11 - 11: o000O0o % Ii * o0o00Oo0O
def oOOo0O00o ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( "GenieTv" , '' , '                                 REFRESH SUCCESSFUL :)' , "                          [COLOR gold]Brought To You By Kodi Support Group, GenieTv[/COLOR]" )
 return
 if 28 - 28: iiiiiiii1 / iI11I1II1I1I + Ii1IIIi1 . Ii1I % Ii1IIIi1 + oO0o
 if 79 - 79: o000O0o
 if 39 - 39: iiiiiiii1 % o000O0o % o0o00Oo0O % o0o00Oo0O - O0OOOoOoo0 - o000O0o
 if 83 - 83: Ii + iI11I1II1I1I
 if 21 - 21: I11i / Ii % iiiiiiii1
 if 56 - 56: I11i * iI11I1II1I1I . ii1ii11IIIiiI + OOooOOo % iiiiiiii1
 if 11 - 11: Ii1IIIi1
 if 12 - 12: ii * Ii1IIIi1 * Ii1I * I11i1ii1
 if 26 - 26: ii . ooOoO0O00 + oO0o
 if 42 - 42: Ii * I11i % ooOOOoO % I1ii11iIi11i + I11i * Ii
 if 66 - 66: ii1ii11IIIiiI / I1111IIi . ii * I1ii11iIi11i % Ii
 if 100 - 100: Ii1I % IIiIiII11i * Ii - O0OOOoOoo0
 if 69 - 69: Ii1IIIi1 + O0OOOoOoo0 / iiiiiiii1
 if 37 - 37: iI11I1II1I1I * ooOOOoO / I1111IIi * I1ii11iIi11i % Ii
 if 93 - 93: I11i1ii1 + I11i1ii1
 if 65 - 65: ii * ooOOOoO * o000O0o % Ii1I * IIiIiII11i
 if 86 - 86: Ii / ooOOOoO * O0OOOoOoo0 - O0OOOoOoo0
 if 32 - 32: I1ii11iIi11i . o0o00Oo0O
 if 48 - 48: Ii1I % IIiIiII11i + ooOOOoO
 if 25 - 25: I1111IIi * I11i / oOo0O0Ooo . I1111IIi % IIiIiII11i
 if 50 - 50: OOooOOo * O0OOOoOoo0
 if 59 - 59: oOo0O0Ooo * oOo0O0Ooo / ooOOOoO
 if 92 - 92: I11i
 if 8 - 8: O0OOOoOoo0 + Ii1I . ii1ii11IIIiiI
def ii1I11 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + ii1I11ooOOoo0 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 47 - 47: ii1ii11IIIiiI % I11i1ii1 + ii1ii11IIIiiI
def IIii ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + i11IiIi ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 5 - 5: ii1ii11IIIiiI / I11i + I1111IIi * ii
def oOiIiIi1iI1 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + ooOoO00ooo0OO0o00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 78 - 78: Ii + I11i
def OO00o0O ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + iIiIOOOoOo0o0Ooo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 22 - 22: OOooOOo * o0o00Oo0O / ii
def o00OO0oo0o ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o0OOo ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 18 - 18: oO0o
def ooooO0OOo0o0 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + IIo000o0O0000o ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 20 - 20: ii * iiiiiiii1
def i1ii1iiI11ii1II1 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + IIi1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 100 - 100: o0o00Oo0O - iI11I1II1I1I * I1ii11iIi11i
def iIIiIIIii1Ii1 ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + oOo0OOoo00 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 76 - 76: Ii . ooOOOoO . I11i1ii1 . Ii1I * ii1ii11IIIiiI . iiiiiiii1
def OoooOoo0Oooo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + i1O0o0oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 42 , iII1iii , I11iiiiI1i , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 33 - 33: ooOoO0O00 * I11i + Ii1I - ooOoO0O00 % ii
def O0O0OOOOoo ( url ) :
 i1i = OoOooO ( str ( I1I1IiI1 ) + o0OiI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 i1IIIII11I1IiI = re . compile ( 'name="([^"]*)".+?rl="([^"]*)".+?mg="([^"]*)".+?anart="([^"]*)".+?escription="([^"]*)"' ) . findall ( i1i )
 for Iii1I1111ii , url , iII1iii , I11iiiiI1i , O00oo in i1IIIII11I1IiI :
  iiOOooooO0Oo ( Iii1I1111ii , url , 5 , III1iII1I1ii + 'GenieTVRSSFeed.png' , III1iII1I1ii + 'GenieTVRSSFeed.png' , O00oo )
 I1I11i ( 'movies' , 'MAIN' )
 if 35 - 35: o000O0o - O0OOOoOoo0 . ii1ii11IIIiiI % I1111IIi . o0o00Oo0O
 if 79 - 79: iiiiiiii1 + o000O0o - iI11I1II1I1I * OOooOOo / ii
 if 49 - 49: ii + iiiiiiii1
 if 39 - 39: o000O0o * iiiiiiii1 - I11i1ii1 + o0o00Oo0O
 if 14 - 14: ooOoO0O00 . ooOoO0O00 + oO0o
 if 95 - 95: oOo0O0Ooo / I11i % IIiIiII11i * iiiiiiii1 . I1111IIi % oO0o
 if 45 - 45: Ii1I . ooOOOoO . IIiIiII11i - IIiIiII11i * ii
 if 71 - 71: Ii1IIIi1
 if 87 - 87: IIiIiII11i / iI11I1II1I1I % Ii1I
def Iii1 ( ) :
 try :
  if os . path . exists ( iIi1ii1I1 ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "Delete Thumbnails" , "[COLOR gold][B]##########WARNING ANDROID ONLY##########[/B][/COLOR]" , "This feature deletes your thumbnail folder and textures13.db" , "Are you sure you want to do proceed? This Can NOT Be Undone" ) :
    for iII , Oo0OOo , i1II11I11ii1 in os . walk ( iIi1ii1I1 ) :
     iII1IiI1I11i = 0
     iII1IiI1I11i += len ( i1II11I11ii1 )
     if iII1IiI1I11i > 0 :
      for OOoO in i1II11I11ii1 :
       os . unlink ( os . path . join ( iII , OOoO ) )
  Ii1i11I11i = os . path . join ( O00o0OO , "Textures13.db" )
  os . unlink ( Ii1i11I11i )
  OOooO0OOoo . ok ( "Restart KODI" , "Please restart KODI to rebuild thumbnail library" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "Error Deleting Thumbnails please visit The Support Group, GenieTv on facebook" )
 return
 if 55 - 55: o000O0o + ii % ooOoO0O00
 if 24 - 24: Ii1I - I1ii11iIi11i
 if 36 - 36: oOo0O0Ooo . Ii1IIIi1 % IIiIiII11i * I1111IIi
 if 34 - 34: ooOOOoO % O0OOOoOoo0 - I11i1ii1 - oOo0O0Ooo
 if 44 - 44: ii1ii11IIIiiI . I11i . iI11I1II1I1I + ii - oOo0O0Ooo
 if 22 - 22: ooOOOoO * Ii1I . ii / I1ii11iIi11i / ii1ii11IIIiiI
 if 54 - 54: iiiiiiii1 % ii1ii11IIIiiI + I11i1ii1
 if 45 - 45: ii1ii11IIIiiI / o000O0o * iiiiiiii1 . ii1ii11IIIiiI
def iIiII1 ( title , message , times = 2000 , icon = Oo00OOOOO ) :
 xbmc . executebuiltin ( 'XBMC.Notification(%s, %s, %s, %s)' % ( title , message , times , icon ) )
 if 25 - 25: Ii1I / Ii1I
def I1iIiI1iiiiI1 ( url ) :
 OO0OoOo0O = os . path . join ( i1iiIIiiI111 , 'addon_data' )
 Ooo0Oo = [
 ( OO0OoOo0O ) ,
 ( oO0o0o0ooO0oO ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'cache' ) ) ,
 ( os . path . join ( Oo0o0000o0o0 , 'temp' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' ) ) ,
 ( os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( oO0o0o0ooO0oO , 'plugin.video.itv' , 'Images' ) ) ,
 ( os . path . join ( OO0OoOo0O , 'script.module.simple.downloader' ) ) ,
 ( os . path . join ( OO0OoOo0O , 'plugin.video.itv' , 'Images' ) ) ]
 if 24 - 24: ooOOOoO
 iiIiiI = 0
 if 9 - 9: Ii + I11i1ii1 . iI11I1II1I1I * OOooOOo
 for IiiiiI1i1Iii in Ooo0Oo :
  if os . path . exists ( IiiiiI1i1Iii ) and not IiiiiI1i1Iii in [ oO0o0o0ooO0oO , OO0OoOo0O ] :
   for iII , Oo0OOo , i1II11I11ii1 in os . walk ( IiiiiI1i1Iii ) :
    iII1IiI1I11i = 0
    iII1IiI1I11i += len ( i1II11I11ii1 )
    if iII1IiI1I11i > 0 :
     for OOoO in i1II11I11ii1 :
      if not OOoO in oooOOOOO :
       try :
        os . unlink ( os . path . join ( iII , OOoO ) )
       except :
        pass
      else : OOO ( 'Ignore Log File: %s' % OOoO )
     for OOO0OoO0oo0OO in Oo0OOo :
      try :
       shutil . rmtree ( os . path . join ( iII , OOO0OoO0oo0OO ) )
       iiIiiI += 1
       OOO ( "[Success] cleared %s files from %s" % ( str ( iII1IiI1I11i ) , os . path . join ( IiiiiI1i1Iii , OOO0OoO0oo0OO ) ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( IiiiiI1i1Iii , OOO0OoO0oo0OO ) )
  else :
   for iII , Oo0OOo , i1II11I11ii1 in os . walk ( IiiiiI1i1Iii ) :
    for OOO0OoO0oo0OO in Oo0OOo :
     if 'cache' in OOO0OoO0oo0OO . lower ( ) :
      try :
       shutil . rmtree ( os . path . join ( iII , OOO0OoO0oo0OO ) )
       iiIiiI += 1
       OOO ( "[Success] wiped %s " % os . path . join ( IiiiiI1i1Iii , OOO0OoO0oo0OO ) )
      except :
       OOO ( "[Failed] to wipe cache in: %s" % os . path . join ( IiiiiI1i1Iii , OOO0OoO0oo0OO ) )
       if 4 - 4: iiiiiiii1 + O0OOOoOoo0 % o0o00Oo0O
 iIiII1 ( oO , 'Clear Cache: Removed %s Files' % iiIiiI )
 if 98 - 98: ooOoO0O00 + iiiiiiii1 - Ii1I . ii / o0o00Oo0O / O0OOOoOoo0
 if 66 - 66: ooOoO0O00 % ii * Ii + o000O0o * o0o00Oo0O / oO0o
 if 14 - 14: oOo0O0Ooo . I1111IIi
 if 29 - 29: ii / I1111IIi + OOooOOo - iiiiiiii1 + I1111IIi . ooOoO0O00
 if 26 - 26: Ii - IIiIiII11i
 if 43 - 43: oOo0O0Ooo
 if 35 - 35: I11i1ii1 + OOooOOo * ii - IIiIiII11i
def IIII1ii1 ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 Iii1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iII , Oo0OOo , i1II11I11ii1 in os . walk ( Iii1i ) :
   iII1IiI1I11i = 0
   iII1IiI1I11i += len ( i1II11I11ii1 )
   if 50 - 50: ii1ii11IIIiiI + ii1ii11IIIiiI
   if 51 - 51: Ii1I / ii * I1111IIi
   if iII1IiI1I11i > 0 :
    if 78 - 78: O0OOOoOoo0 / Ii1I . Ii
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( iII1IiI1I11i ) + " files found" , "Do you want to delete them?" ) :
     if 69 - 69: ooOOOoO - IIiIiII11i
     for OOoO in i1II11I11ii1 :
      os . unlink ( os . path . join ( iII , OOoO ) )
     for OOO0OoO0oo0OO in Oo0OOo :
      shutil . rmtree ( os . path . join ( iII , OOO0OoO0oo0OO ) )
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
 if 66 - 66: oOo0O0Ooo . oOo0O0Ooo - OOooOOo * ii * IIiIiII11i + oOo0O0Ooo
 if 59 - 59: ii1ii11IIIiiI
 if 59 - 59: IIiIiII11i - oO0o
 if 31 - 31: ooOOOoO - OOooOOo / I11i * OOooOOo / I1ii11iIi11i + I11i
 if 46 - 46: I1111IIi * oO0o / Ii1IIIi1 + I1ii11iIi11i
 if 24 - 24: I11i1ii1 % Ii1IIIi1 . o0o00Oo0O * I1ii11iIi11i
 if 52 - 52: o0o00Oo0O . iiiiiiii1 + O0OOOoOoo0 / Ii
 if 52 - 52: o000O0o % I1ii11iIi11i * IIiIiII11i
 if 24 - 24: Ii * ooOoO0O00 * ooOoO0O00
def ooO0O0O0ooOOO ( url ) :
 print '###' + i1 + ' - DELETING PACKAGES###'
 Iii1i = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 try :
  for iII , Oo0OOo , i1II11I11ii1 in os . walk ( Iii1i ) :
   iII1IiI1I11i = 0
   iII1IiI1I11i += len ( i1II11I11ii1 )
   if 27 - 27: ooOoO0O00 - o000O0o + Ii1IIIi1
   if 3 - 3: I1111IIi % iiiiiiii1 . ii
   if iII1IiI1I11i > 0 :
    if 19 - 19: iiiiiiii1 * ii1ii11IIIiiI - o000O0o
    OOooO0OOoo = xbmcgui . Dialog ( )
    if OOooO0OOoo . yesno ( "Delete Package Cache Files" , str ( iII1IiI1I11i ) + " files found" , "Do you want to delete them?" ) :
     if 78 - 78: oO0o - ii1ii11IIIiiI / Ii1IIIi1
     for OOoO in i1II11I11ii1 :
      os . unlink ( os . path . join ( iII , OOoO ) )
     for OOO0OoO0oo0OO in Oo0OOo :
      shutil . rmtree ( os . path . join ( iII , OOO0OoO0oo0OO ) )
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
 I1iIiI1iiiiI1 ( url )
 return
 if 81 - 81: OOooOOo
 if 21 - 21: O0OOOoOoo0 / Ii1IIIi1 % I1111IIi
 if 51 - 51: ooOOOoO + I11i1ii1 / oOo0O0Ooo
 if 3 - 3: iI11I1II1I1I / Ii1IIIi1 % o000O0o . ii1ii11IIIiiI - ii1ii11IIIiiI
 if 55 - 55: Ii % ii + o0o00Oo0O
 if 7 - 7: I11i1ii1 - Ii * O0OOOoOoo0 / ii1ii11IIIiiI - I11i
 if 62 - 62: I11i - iI11I1II1I1I . ooOOOoO . ii1ii11IIIiiI * ii1ii11IIIiiI
 if 24 - 24: ooOOOoO
 if 93 - 93: oOo0O0Ooo % oO0o / Ii / ooOOOoO
 if 60 - 60: I11i1ii1 - ii1ii11IIIiiI . oOo0O0Ooo * o000O0o * Ii
def IIiIiI1Ii ( url , name ) :
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1iO0000 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
 OOooO0OOoo = xbmcgui . Dialog ( )
 O0iiI1iii1I111 = os . path . join ( O0O00Oo , 'advancedsettings.xml.bak' )
 if os . path . exists ( O0iiI1iii1I111 ) == False :
  if OOooO0OOoo . yesno ( "Back Up Original" , 'Have You Backed Up Your Original?' , '' , "[B][COLOR red]     AS YOU CANNOT GO BACK !!![/B][/COLOR]" ) :
   print '###' + i1 + ' - ADVANCED XML###'
   O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
   I1iO0000 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
   try :
    os . remove ( I1iO0000 )
    print '=== GenieTv - REMOVING    ' + str ( I1iO0000 ) + '    ==='
   except :
    pass
   i1i = iI111I11I1I1 . http_GET ( url ) . content
   IiIi1II111I = open ( I1iO0000 , "w" )
   IiIi1II111I . write ( i1i )
   IiIi1II111I . close ( )
   print '=== GenieTv - WRITING NEW    ' + str ( I1iO0000 ) + '    ==='
   OOooO0OOoo = xbmcgui . Dialog ( )
   OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 else :
  print '###' + i1 + ' - ADVANCED XML###'
  O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
  I1iO0000 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
  try :
   os . remove ( I1iO0000 )
   print '=== GenieTv - REMOVING    ' + str ( I1iO0000 ) + '    ==='
  except :
   pass
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  IiIi1II111I = open ( I1iO0000 , "w" )
  IiIi1II111I . write ( i1i )
  IiIi1II111I . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1iO0000 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       Done Adding new Advanced XML" )
 return
 if 11 - 11: ii1ii11IIIiiI / Ii1IIIi1 * Ii1IIIi1 * o0o00Oo0O
def IiiIiIi1iII ( url , name ) :
 print '###' + i1 + ' - CHECK ADVANCE XML###'
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1iO0000 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
 try :
  IiIi1II111I = open ( I1iO0000 ) . read ( )
  if 'zero' in IiIi1II111I :
   name = '0CACHE'
  elif 'tuxen' in IiIi1II111I :
   name = 'TUXENS'
  elif 'muckys' in IiIi1II111I :
   name = 'MUCKYS'
  elif 'p2p1' in IiIi1II111I :
   name = '1st P2P RECOMMENDED'
  elif 'p2p2' in IiIi1II111I :
   name = '2nd P2P RECOMMENDED'
  elif 'mikey' in IiIi1II111I :
   name = 'MIKEY1234'
 except :
  name = "NO ADVANCED"
 OOooO0OOoo = xbmcgui . Dialog ( )
 OOooO0OOoo . ok ( i1 , "[COLOR yellow]YOU HAVE[/COLOR] " + name + "[COLOR yellow] XML SETTINGS SETUP[/COLOR]" )
 return
 if 52 - 52: o0o00Oo0O * ii . iiiiiiii1 . Ii1IIIi1 - O0OOOoOoo0 % O0OOOoOoo0
def IiiIIIIII ( url ) :
 print '###' + i1 + ' - DELETING ADVANCE XML###'
 O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
 I1iO0000 = os . path . join ( O0O00Oo , 'advancedsettings.xml' )
 try :
  os . remove ( I1iO0000 )
  OOooO0OOoo = xbmcgui . Dialog ( )
  print '=== GenieTv - DELETING    ' + str ( I1iO0000 ) + '    ==='
  OOooO0OOoo . ok ( i1 , "       Remove Advanced Settings Sucessfull" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "       No Advanced Settings To Remove" )
 return
 if 28 - 28: I11i
 if 43 - 43: Ii1I . I1111IIi * OOooOOo / I1ii11iIi11i
 if 2 - 2: iI11I1II1I1I
 if 2 - 2: o000O0o + I11i1ii1 % Ii1IIIi1 + I1111IIi
 if 29 - 29: I1ii11iIi11i % Ii1IIIi1
 if 65 - 65: O0OOOoOoo0 - Ii + ii
 if 74 - 74: Ii1IIIi1 - IIiIiII11i
 if 66 - 66: Ii + iiiiiiii1 . I11i1ii1
 if 46 - 46: iiiiiiii1 / Ii1I
 if 41 - 41: ooOoO0O00 % ii1ii11IIIiiI + iiiiiiii1 . I1ii11iIi11i / iI11I1II1I1I
def OOO0O0OOo ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 i1IIIII11I1IiI = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( iI111I11I1I1 . http_GET ( url ) . content )
 for OOooOOO000 , O0OoO , oOo0O00 , iI11II in i1IIIII11I1IiI :
  if inc < 2 : OOooO0OOoo = xbmcgui . Dialog ( ) ; OOooO0OOoo . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % OOooOOO000 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % oOo0O00 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % iI11II )
  inc = inc + 1
  if 13 - 13: OOooOOo - I1111IIi * iI11I1II1I1I * o0o00Oo0O
  if 26 - 26: ii + o000O0o + oO0o . o0o00Oo0O
  if 46 - 46: ii - I1ii11iIi11i * iiiiiiii1 * Ii1IIIi1 * iiiiiiii1 . o000O0o
  if 96 - 96: ii1ii11IIIiiI / I1111IIi % I11i + ooOOOoO
  if 46 - 46: oO0o * oOo0O0Ooo
  if 25 - 25: iiiiiiii1 . I1111IIi % o0o00Oo0O % ooOoO0O00
  if 53 - 53: o0o00Oo0O % I11i1ii1
  if 41 - 41: I1111IIi
  if 29 - 29: I11i1ii1
def OO0II111Iiii1 ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                                    Install Latest .ini File' ) :
  print '###' + i1 + ' - CUSTOM FTV INI###'
  O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I1iO0000 = os . path . join ( O0O00Oo , 'addons2.ini' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  IiIi1II111I = open ( I1iO0000 , "w" )
  IiIi1II111I . write ( i1i )
  IiIi1II111I . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1iO0000 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New .ini File" )
 return
 if 50 - 50: o000O0o
def oOO0Oo00o ( url , name ) :
 OOooO0OOoo = xbmcgui . Dialog ( )
 if OOooO0OOoo . yesno ( "GenieTv" , '                               Install Custom Settings' ) :
  print '###' + i1 + ' - CUSTOM FTV SETTINGS###'
  O0O00Oo = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  I1iO0000 = os . path . join ( O0O00Oo , 'settings.xml' )
  i1i = iI111I11I1I1 . http_GET ( url ) . content
  IiIi1II111I = open ( I1iO0000 , "w" )
  IiIi1II111I . write ( i1i )
  IiIi1II111I . close ( )
  print '=== GenieTv - WRITING NEW    ' + str ( I1iO0000 ) + '    ==='
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "                               Done Adding New Settings" )
 return
 if 91 - 91: o000O0o * o0o00Oo0O
 if 19 - 19: Ii1I / oO0o + o000O0o
def O0O0O ( ) :
 try :
  O0o0OO0oOo0OO = xbmc . translatePath ( os . path . join ( 'special://masterprofile/addon_data/plugin.video.GenieTv' , '' ) )
  if os . path . exists ( O0o0OO0oOo0OO ) == True :
   OOooO0OOoo = xbmcgui . Dialog ( )
   if OOooO0OOoo . yesno ( "GenieTv" , "                               Delete FTV Guide Database" ) :
    I1i11I11 = os . path . join ( O0o0OO0oOo0OO , "source.db" )
    os . unlink ( I1i11I11 )
  OOooO0OOoo . ok ( "GenieTv" , "                                     FTV Database Reset" )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( i1 , "               Error Deleting Database No Database To Delete" )
 return
 if 1 - 1: OOooOOo * iI11I1II1I1I
 if 17 - 17: ii . Ii1IIIi1
 if 32 - 32: OOooOOo . o000O0o + o0o00Oo0O
 if 100 - 100: o0o00Oo0O / Ii1IIIi1 - I11i1ii1
 if 15 - 15: O0OOOoOoo0 - o0o00Oo0O - ii
def OoOooO ( url ) :
 O00O0oOO00O00 = urllib2 . Request ( url )
 O00O0oOO00O00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 i1Oo00 = urllib2 . urlopen ( O00O0oOO00O00 )
 i1i = i1Oo00 . read ( )
 i1Oo00 . close ( )
 return i1i
 if 49 - 49: IIiIiII11i . ii
 if 30 - 30: oO0o / Ii - oO0o / I11i1ii1 + iI11I1II1I1I + ooOoO0O00
 if 99 - 99: Ii1IIIi1 * oOo0O0Ooo + o000O0o % o000O0o % Ii1IIIi1 * I1111IIi
 if 98 - 98: Ii1IIIi1
 if 97 - 97: I11i
 if 35 - 35: I11i1ii1 + Ii
 if 82 - 82: Ii + ooOOOoO + O0OOOoOoo0 % oOo0O0Ooo
def Oo0o0O00 ( params ) :
 plugintools . log ( "freshstart.main_list " + repr ( params ) ) ; oO0oO0oOOo = plugintools . message_yes_no ( i1 , "Do you wish to restore your" , "Kodi configuration to default settings?" )
 if oO0oO0oOOo :
  iii1iii1I1I = xbmcaddon . Addon ( id = Oo0oO0ooo ) . getAddonInfo ( 'path' ) ; iii1iii1I1I = xbmc . translatePath ( iii1iii1I1I ) ;
  IiI1iI1II1I1i = os . path . join ( iii1iii1I1I , ".." , ".." ) ; IiI1iI1II1I1i = os . path . abspath ( IiI1iI1II1I1i ) ; plugintools . log ( "freshstart.main_list xbmcPath=" + IiI1iI1II1I1i ) ; IiII11iii = False
  try :
   for iII , Oo0OOo , i1II11I11ii1 in os . walk ( IiI1iI1II1I1i , topdown = True ) :
    Oo0OOo [ : ] = [ OOO0OoO0oo0OO for OOO0OoO0oo0OO in Oo0OOo if OOO0OoO0oo0OO not in o0oO0 ]
    for Iii1I1111ii in i1II11I11ii1 :
     try : os . remove ( os . path . join ( iII , Iii1I1111ii ) )
     except :
      if Iii1I1111ii not in [ "Addons15.db" , "MyVideos75.db" , "Textures13.db" , "xbmc.log" ] : IiII11iii = True
      plugintools . log ( "Error removing " + iII + " " + Iii1I1111ii )
    for Iii1I1111ii in Oo0OOo :
     try : os . rmdir ( os . path . join ( iII , Iii1I1111ii ) )
     except :
      if Iii1I1111ii not in [ "Database" , "userdata" ] : IiII11iii = True
      plugintools . log ( "Error removing " + iII + " " + Iii1I1111ii )
   if not IiII11iii : plugintools . log ( "freshstart.main_list All user files removed, you now have a clean install" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv!" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
   else : plugintools . log ( "freshstart.main_list User files partially removed" ) ; plugintools . message ( i1 , "The process is complete, you're now back to a fresh Kodi configuration with GenieTv" , "Please reboot your system or restart Kodi in order for the changes to be applied." )
  except : plugintools . message ( i1 , "Problem found" , "Your settings has not been changed" ) ; import traceback ; plugintools . log ( traceback . format_exc ( ) ) ; plugintools . log ( "freshstart.main_list NOT removed" )
  plugintools . add_item ( action = "" , title = "Now Exit Kodi" , folder = False )
 else : plugintools . message ( i1 , "Your settings" , "has not been changed" ) ; plugintools . add_item ( action = "" , title = "Done" , folder = False )
 oO0OOO00 ( )
 if 73 - 73: o0o00Oo0O
 if 19 - 19: I1111IIi / I11i - ii1ii11IIIiiI . Ii + o000O0o % OOooOOo
 if 97 - 97: Ii1IIIi1 . Ii1IIIi1 . O0OOOoOoo0 . O0OOOoOoo0
def Ooo0oOoOoOoo ( ) :
 iIIi1iiIIiIi1 = [ ]
 IiI1111i1i11I = sys . argv [ 2 ]
 if len ( IiI1111i1i11I ) >= 2 :
  ii1 = sys . argv [ 2 ]
  O000oOo = ii1 . replace ( '?' , '' )
  if ( ii1 [ len ( ii1 ) - 1 ] == '/' ) :
   ii1 = ii1 [ 0 : len ( ii1 ) - 2 ]
  OO0oO0ooOOOoO = O000oOo . split ( '&' )
  iIIi1iiIIiIi1 = { }
  for I1iII1II1I1ii in range ( len ( OO0oO0ooOOOoO ) ) :
   iIiIIii11iI = { }
   iIiIIii11iI = OO0oO0ooOOOoO [ I1iII1II1I1ii ] . split ( '=' )
   if ( len ( iIiIIii11iI ) ) == 2 :
    iIIi1iiIIiIi1 [ iIiIIii11iI [ 0 ] ] = iIiIIii11iI [ 1 ]
    if 27 - 27: I11i
 return iIIi1iiIIiIi1
 if 13 - 13: Ii1I - o0o00Oo0O * o000O0o % iI11I1II1I1I . oOo0O0Ooo - Ii1IIIi1
oOOooO = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkbw==' )
o0Ii11iIiiI = base64 . decodestring ( 'L3N0b3JhZ2UvZW11bGF0ZWQvMA==' )
Iii1I1IIII = base64 . decodestring ( 'L2dlbmllLnR4dA==' )
i1iI1Iii11Iii11 = base64 . decodestring ( 'LmFyY2hpdGVjdHMueDEwaG9zdC5jb20vdGVzdC93aC50eHQ=' )
Oooo00OOo = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9maXhlcy9maXhlcy50eHQ=' )
iIiiI = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby9hcHBzL2FwcHMueG1s' )
ii1I11ooOOoo0 = base64 . decodestring ( 'L2FkZG9ucy9uZXcudHh0' )
OOo000 = base64 . decodestring ( 'aHR0cDovL2dlbmlldHYuY28udWsvcmVkby92b2Qvdm9kLnBocA==' )
i11IiIi = base64 . decodestring ( 'L2FkZG9ucy9pcHR2LnR4dA==' )
ooOoO00ooo0OO0o00 = base64 . decodestring ( 'L2FkZG9ucy92aWRlby50eHQ=' )
iIiIOOOoOo0o0Ooo = base64 . decodestring ( 'L2FkZG9ucy9zcG9ydHMudHh0' )
o0OOo = base64 . decodestring ( 'L2FkZG9ucy9raWRzLnR4dA==' )
IIo000o0O0000o = base64 . decodestring ( 'L2FkZG9ucy9tdXNpYy50eHQ=' )
IIi1 = base64 . decodestring ( 'L2FkZG9ucy9wcm9ncmFtcy50eHQ=' )
oOo0OOoo00 = base64 . decodestring ( 'L2FkZG9ucy94eHgudHh0' )
i1O0o0oO = base64 . decodestring ( 'L2FkZG9ucy9yZXBvLnR4dA==' )
i1iI = base64 . decodestring ( 'L2FkZG9ucy9wYWNrcy50eHQ=' )
iI1iIIiIi1I1 = base64 . decodestring ( 'L2FkZG9ucy9za2lucy50eHQ=' )
OOo0OOoo00 = base64 . decodestring ( 'L2FkZG9ucy9hcnQudHh0' )
Ii1I1IIIiI1i = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2dvdGhhbS50eHQ=' )
o0o0ooOo00 = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2hlbGl4LnR4dA==' )
I1Iiii = base64 . decodestring ( 'L2FkZG9ucy9Ta2luc2lzZW5nYXJkLnR4dA==' )
o0OiI = base64 . decodestring ( 'L2FkZG9ucy9SU1MudHh0' )
I1i1ii1ii = base64 . decodestring ( 'Q1VOVA==' )
def iiOOooooO0Oo ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O0ooOOO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii11Iii1i1ii = True
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1i1111 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o0oO0O00oOo = [ ]
  if showcontext == 'fav' :
   o0oO0O00oOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o0oO0O00oOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ii1i1i1111 . addContextMenuItems ( o0oO0O00oOo )
 Ii11Iii1i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = True )
 return Ii11Iii1i1ii
 if 85 - 85: oO0o + IIiIiII11i
def OOiIiIIi1 ( name , url , mode , iconimage , fanart , description , showcontext = True , allinfo = { } ) :
 O0ooOOO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&description=" + urllib . quote_plus ( description )
 Ii11Iii1i1ii = True
 Ii1i1i1111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ii1i1i1111 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 Ii1i1i1111 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  o0oO0O00oOo = [ ]
  if showcontext == 'fav' :
   o0oO0O00oOo . append ( ( 'Remove from Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10056&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if not name in OOO00O :
   o0oO0O00oOo . append ( ( 'Add to Genie TV Favorites' , 'XBMC.RunPlugin(%s?mode=10055&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  Ii1i1i1111 . addContextMenuItems ( o0oO0O00oOo )
 Ii11Iii1i1ii = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOOO0 , listitem = Ii1i1i1111 , isFolder = False )
 return Ii11Iii1i1ii
 if 87 - 87: oO0o
 if 93 - 93: ii
ii1 = Ooo0oOoOoOoo ( )
oOooO0 = None
Iii1I1111ii = None
iIiiiii1i = None
iII1iii = None
I11iiiiI1i = None
O00oo = None
ooOooO0O = None
iIIiii = None
if 25 - 25: IIiIiII11i + ooOOOoO
if 97 - 97: o0o00Oo0O + Ii1IIIi1 % OOooOOo * ooOOOoO . iI11I1II1I1I
try :
 iIIiii = int ( ii1 [ "fav_mode" ] )
except :
 pass
 if 94 - 94: o000O0o
try :
 oOooO0 = urllib . unquote_plus ( ii1 [ "url" ] )
except :
 pass
try :
 Iii1I1111ii = urllib . unquote_plus ( ii1 [ "name" ] )
except :
 pass
try :
 iII1iii = urllib . unquote_plus ( ii1 [ "iconimage" ] )
except :
 pass
try :
 iIiiiii1i = int ( ii1 [ "mode" ] )
except :
 pass
try :
 I11iiiiI1i = urllib . unquote_plus ( ii1 [ "fanart" ] )
except :
 pass
try :
 O00oo = urllib . unquote_plus ( ii1 [ "description" ] )
except :
 pass
 if 53 - 53: I11i1ii1 + O0OOOoOoo0 * ooOoO0O00 + oOo0O0Ooo
 if 89 - 89: oOo0O0Ooo / IIiIiII11i - OOooOOo % I11i
print str ( o0 ) + ': ' + str ( IiiIII111iI )
print "Mode: " + str ( iIiiiii1i )
print "URL: " + str ( oOooO0 )
print "Name: " + str ( Iii1I1111ii )
print "IconImage: " + str ( iII1iii )
if 1 - 1: ii . ooOOOoO / OOooOOo + I11i % ooOoO0O00
if 1 - 1: ii - oO0o - ii / O0OOOoOoo0
def I1I11i ( content , viewType ) :
 if 70 - 70: ii1ii11IIIiiI + Ii1I . IIiIiII11i * Ii
 if content :
  xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , content )
 if oo00 . getSetting ( 'auto-view' ) == 'true' :
  xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo00 . getSetting ( viewType ) )
  if 87 - 87: ii1ii11IIIiiI / iiiiiiii1 % OOooOOo * Ii1I - ii / OOooOOo
if iII1iii == None : iII1iii = Oo00OOOOO
if I11iiiiI1i == None : I11iiiiI1i = O0o0Oo
if iIiiiii1i == None :
 o0o0o0oO0oOO ( )
 if 24 - 24: ooOOOoO . Ii1IIIi1 * ooOoO0O00 . Ii1I / I11i1ii1 / o0o00Oo0O
elif iIiiiii1i == 1 :
 i1111iIII ( oOooO0 )
 if 62 - 62: I11i % IIiIiII11i
elif iIiiiii1i == 44 :
 I1i11OO ( oOooO0 )
 if 22 - 22: o000O0o - I11i
elif iIiiiii1i == 2 :
 ii11i1I1i ( )
 if 89 - 89: Ii1IIIi1
elif iIiiiii1i == 3 :
 IiIIIIii11i ( )
 if 34 - 34: O0OOOoOoo0 . Ii1IIIi1
elif iIiiiii1i == 21 :
 i1i1II ( )
 if 13 - 13: oO0o * Ii1IIIi1 + o000O0o
elif iIiiiii1i == 4 :
 o0ooOO00OO0o0O ( )
 if 21 - 21: Ii . ii1ii11IIIiiI % ooOoO0O00 * ii1ii11IIIiiI . o000O0o + ii1ii11IIIiiI
elif iIiiiii1i == 5 :
 IIi11 ( oOooO0 )
 if 92 - 92: ooOoO0O00 + oO0o * ooOOOoO
elif iIiiiii1i == 6 :
 IIII1ii1 ( oOooO0 )
 if 70 - 70: I1ii11iIi11i
elif iIiiiii1i == 7 :
 IIiIiI1Ii ( oOooO0 , Iii1I1111ii )
 if 93 - 93: O0OOOoOoo0 . Ii1I . I1ii11iIi11i . o000O0o . ii
elif iIiiiii1i == 8 :
 IiiIiIi1iII ( oOooO0 , Iii1I1111ii )
 if 51 - 51: o0o00Oo0O - O0OOOoOoo0
elif iIiiiii1i == 9 :
 FIXREPOSADDONS ( oOooO0 )
 if 65 - 65: o0o00Oo0O / IIiIiII11i * I1111IIi % ii1ii11IIIiiI + I11i
elif iIiiiii1i == 10 :
 oOOo0O00o ( )
 if 43 - 43: iiiiiiii1 + oO0o * ii
elif iIiiiii1i == 11 :
 IiiIIIIII ( oOooO0 )
 if 85 - 85: O0OOOoOoo0 + Ii1IIIi1
elif iIiiiii1i == 12 :
 OOO0O0OOo ( url = 'http://www.iplocation.net/' , inc = 1 )
 if 36 - 36: oO0o % IIiIiII11i * o0o00Oo0O + IIiIiII11i - o000O0o - ooOoO0O00
elif iIiiiii1i == 13 :
 Iii1 ( )
 if 53 - 53: ii1ii11IIIiiI - Ii1IIIi1
elif iIiiiii1i == 14 :
 I1iIiI1iiiiI1 ( oOooO0 )
 if 75 - 75: O0OOOoOoo0 % o0o00Oo0O - ooOOOoO - Ii1I + oOo0O0Ooo - oOo0O0Ooo
elif iIiiiii1i == 15 :
 Ii11IiI111 ( )
 if 87 - 87: ooOoO0O00 % ii1ii11IIIiiI % ooOoO0O00 + iI11I1II1I1I
elif iIiiiii1i == 16 :
 OO0II111Iiii1 ( oOooO0 , Iii1I1111ii )
 if 23 - 23: iI11I1II1I1I * ooOOOoO . iiiiiiii1 - I11i
elif iIiiiii1i == 17 :
 oOO0Oo00o ( oOooO0 , Iii1I1111ii )
 if 66 - 66: oOo0O0Ooo * iiiiiiii1 / Ii / Ii1IIIi1
elif iIiiiii1i == 18 :
 O0O0O ( )
 if 19 - 19: I11i1ii1 % iI11I1II1I1I * ii
elif iIiiiii1i == 19 :
 Ooo000o0oo0 ( oOooO0 )
 if 60 - 60: iiiiiiii1 * O0OOOoOoo0 / ii * I1ii11iIi11i
elif iIiiiii1i == 40 :
 I11IiI1i ( Iii1I1111ii , oOooO0 , O00oo )
 if 47 - 47: O0OOOoOoo0 + I11i % iI11I1II1I1I * OOooOOo
elif iIiiiii1i == 42 :
 O00O0IIIIIIIiiiI ( Iii1I1111ii , oOooO0 , O00oo )
 if 65 - 65: Ii1IIIi1 . IIiIiII11i * Ii + Ii1IIIi1
elif iIiiiii1i == 43 :
 II11IiI1 ( oOooO0 )
 if 99 - 99: Ii1I % I1ii11iIi11i
elif iIiiiii1i == 20 :
 o00o0o000Oo ( oOooO0 )
 if 31 - 31: I11i - IIiIiII11i * Ii1IIIi1 . Ii1IIIi1 - o000O0o
elif iIiiiii1i == 22 :
 ii1I11 ( oOooO0 )
 if 57 - 57: Ii1IIIi1 / Ii / iiiiiiii1 - I1ii11iIi11i . iI11I1II1I1I
elif iIiiiii1i == 23 :
 IIii ( oOooO0 )
 if 84 - 84: I1111IIi
elif iIiiiii1i == 24 :
 oOiIiIi1iI1 ( oOooO0 )
 if 42 - 42: o0o00Oo0O . iiiiiiii1 / ooOOOoO
elif iIiiiii1i == 25 :
 OO00o0O ( oOooO0 )
 if 69 - 69: OOooOOo / iiiiiiii1 * oOo0O0Ooo
elif iIiiiii1i == 26 :
 o00OO0oo0o ( oOooO0 )
 if 76 - 76: o0o00Oo0O + IIiIiII11i * oO0o
elif iIiiiii1i == 27 :
 ooooO0OOo0o0 ( oOooO0 )
 if 1 - 1: I11i
elif iIiiiii1i == 28 :
 i1ii1iiI11ii1II1 ( oOooO0 )
 if 34 - 34: I11i + Ii1IIIi1 . oO0o + oOo0O0Ooo + ii
elif iIiiiii1i == 29 :
 iIIiIIIii1Ii1 ( oOooO0 )
 if 90 - 90: ii1ii11IIIiiI / OOooOOo - iI11I1II1I1I / ooOoO0O00 * iiiiiiii1 - I11i1ii1
elif iIiiiii1i == 30 :
 OooO00oo0O0 ( oOooO0 )
 if 2 - 2: O0OOOoOoo0 * ooOOOoO * I11i1ii1 + Ii + o000O0o
elif iIiiiii1i == 31 :
 OoooOoo0Oooo ( oOooO0 )
 if 81 - 81: I11i * oO0o
elif iIiiiii1i == 32 :
 O00Ooo0O0OOOo ( )
 if 18 - 18: Ii / I11i - o000O0o . ooOOOoO * ooOoO0O00
elif iIiiiii1i == 33 :
 o0oooo0O ( )
 if 67 - 67: ii1ii11IIIiiI
elif iIiiiii1i == 35 :
 iIioOo ( oOooO0 )
 if 64 - 64: OOooOOo + O0OOOoOoo0 * OOooOOo - oOo0O0Ooo * ii
elif iIiiiii1i == 34 :
 iI1iIIIIIiIi1 ( oOooO0 )
 if 27 - 27: IIiIiII11i + Ii
elif iIiiiii1i == 36 :
 iiI1ii1Iii ( oOooO0 )
 if 32 - 32: ooOoO0O00
elif iIiiiii1i == 37 :
 O00o ( oOooO0 )
 if 76 - 76: IIiIiII11i % I11i1ii1 - Ii1I
elif iIiiiii1i == 38 :
 i111I111 ( oOooO0 )
 if 50 - 50: IIiIiII11i / oOo0O0Ooo . ii1ii11IIIiiI % Ii
elif iIiiiii1i == 41 :
 Oo0o0O00 ( ii1 )
 if 66 - 66: o000O0o / Ii1IIIi1 / O0OOOoOoo0
elif iIiiiii1i == 39 :
 O0O0OOOOoo ( oOooO0 )
 if 5 - 5: iiiiiiii1 . o000O0o
elif iIiiiii1i == 45 :
 TEXTS ( )
 if 77 - 77: O0OOOoOoo0 / Ii
elif iIiiiii1i == 46 :
 Ii1I1Ii ( )
 if 20 - 20: o0o00Oo0O . ooOOOoO
elif iIiiiii1i == 47 :
 GEVID ( )
 if 67 - 67: OOooOOo - I11i1ii1 - iI11I1II1I1I
elif iIiiiii1i == 48 :
 oO0ooo0O0Ooo ( Iii1I1111ii , oOooO0 , O00oo )
 if 31 - 31: IIiIiII11i + I11i * Ii . I11i
elif iIiiiii1i == 49 :
 ooo00Ooo ( )
 if 73 - 73: o000O0o / Ii1IIIi1 * IIiIiII11i % ii - ooOoO0O00 - I11i1ii1
elif iIiiiii1i == 22222 :
 ii1O0ooooo000 ( oOooO0 )
 if 43 - 43: I11i + ii1ii11IIIiiI % oO0o . iiiiiiii1 + ooOoO0O00
elif iIiiiii1i == 222 :
 IiI1ii1ii ( oOooO0 )
 if 85 - 85: I1ii11iIi11i % Ii1I / Ii1IIIi1
elif iIiiiii1i == 2222222 :
 OOOoOO0o ( oOooO0 )
 if 65 - 65: I11i1ii1 + I1111IIi - OOooOOo % IIiIiII11i - iI11I1II1I1I
elif iIiiiii1i == 222222 :
 iIiIiiiII11i ( oOooO0 , Iii1I1111ii )
 if 39 - 39: oOo0O0Ooo + Ii1I - Ii
elif iIiiiii1i == 333 :
 IiiiiIIi1i ( oOooO0 )
 if 43 - 43: iI11I1II1I1I
 if 73 - 73: OOooOOo + I11i
elif iIiiiii1i == 1020 :
 i1ii1iIiI1 ( )
 if 58 - 58: ooOoO0O00 * Ii1I % O0OOOoOoo0 . oO0o % I1111IIi % ooOOOoO
elif iIiiiii1i == 1021 :
 ANIMEEP ( )
 if 63 - 63: Ii1I % I11i1ii1 % Ii1I
elif iIiiiii1i == 1022 :
 ANIMEPLAY ( oOooO0 )
 if 71 - 71: ii1ii11IIIiiI
elif iIiiiii1i == 1001 :
 ooOOOooOooOOoO0O ( )
 if 43 - 43: I11i / I11i1ii1
elif iIiiiii1i == 1005 :
 o000OOO000o ( )
 if 88 - 88: Ii - ooOoO0O00 + I1ii11iIi11i - o0o00Oo0O
elif iIiiiii1i == 1007 :
 o000ooOO ( oOooO0 )
 if 50 - 50: Ii1I
elif iIiiiii1i == 1010 :
 O0o0O00o0o ( oOooO0 )
 if 37 - 37: o000O0o % O0OOOoOoo0 / IIiIiII11i / oO0o - I1111IIi - I11i1ii1
elif iIiiiii1i == 1011 :
 oOO0oo0o0ooO00 ( oOooO0 )
 if 69 - 69: Ii1I . ii % iiiiiiii1
elif iIiiiii1i == 1012 :
 I11I11III ( oOooO0 )
 if 79 - 79: oOo0O0Ooo - I1111IIi . ii - Ii1I
elif iIiiiii1i == 1030 :
 i1i1IIoO0O ( )
 if 79 - 79: Ii1IIIi1 + I11i % O0OOOoOoo0 . o000O0o
elif iIiiiii1i == 1031 :
 O0OO0OoO00oOo ( oOooO0 , iII1iii )
 if 49 - 49: ii1ii11IIIiiI + Ii * OOooOOo . OOooOOo . Ii1I . I1ii11iIi11i
elif iIiiiii1i == 1032 :
 i11i ( oOooO0 )
 if 61 - 61: ooOOOoO / Ii1IIIi1
elif iIiiiii1i == 1006 :
 Parse . ParseURL ( oOooO0 )
 if 85 - 85: OOooOOo - ooOOOoO . OOooOOo . OOooOOo
elif iIiiiii1i == 2030 :
 Parse . addonParseURL ( oOooO0 )
 if 62 - 62: I1111IIi % ii * oO0o + oO0o % ii1ii11IIIiiI % O0OOOoOoo0
elif iIiiiii1i == 2031 :
 Parse . apkParseURL ( oOooO0 )
 if 66 - 66: oOo0O0Ooo . Ii1IIIi1 - oO0o % I1ii11iIi11i * I11i - o000O0o
elif iIiiiii1i == 2032 :
 Parse . ParseBOSS ( oOooO0 )
 if 68 - 68: ooOOOoO - Ii / I11i + I11i1ii1 / oOo0O0Ooo
elif iIiiiii1i == 1002 :
 o0ooOoOoO0o ( oOooO0 )
 if 31 - 31: iiiiiiii1 . ii . ooOoO0O00
elif iIiiiii1i == 1003 :
 OOo00OoOoo ( oOooO0 , iII1iii )
 if 65 - 65: oO0o . I11i1ii1
elif iIiiiii1i == 1004 :
 o0Oi1i1i11IIii ( oOooO0 )
 if 12 - 12: iiiiiiii1 + o0o00Oo0O - o000O0o . I1111IIi
elif iIiiiii1i == 1008 :
 OoOo0OoOO0Ooo ( )
 if 46 - 46: I1111IIi . I11i1ii1 / O0OOOoOoo0
elif iIiiiii1i == 1009 :
 OOOo0OO0ooO0O0O ( oOooO0 )
 if 63 - 63: IIiIiII11i - Ii1I * IIiIiII11i
elif iIiiiii1i == 2001 :
 i11iI ( )
 if 92 - 92: oO0o % I11i1ii1 * o0o00Oo0O % iI11I1II1I1I / ooOoO0O00 / OOooOOo
elif iIiiiii1i == 2002 :
 oo0ooOo0O0 ( oOooO0 )
 if 67 - 67: iiiiiiii1 + ooOOOoO + iiiiiiii1 . Ii1IIIi1 % I11i / I11i1ii1
elif iIiiiii1i == 1013 :
 OOO000OOo0o0O ( )
elif iIiiiii1i == 10111113 :
 oo0o000o0oOO0 ( oOooO0 )
 if 78 - 78: Ii1I . o0o00Oo0O
elif iIiiiii1i == 1014 :
 OO0O0000oo ( )
 if 56 - 56: o000O0o - ooOoO0O00 * o0o00Oo0O / ooOOOoO * oOo0O0Ooo . ooOOOoO
elif iIiiiii1i == 1015 :
 O0ooOo ( oOooO0 )
 if 54 - 54: Ii % ooOoO0O00 + I1ii11iIi11i / OOooOOo
elif iIiiiii1i == 1016 :
 ooo0O ( oOooO0 , iII1iii , Iii1I1111ii )
 if 26 - 26: ooOOOoO . Ii1I
elif iIiiiii1i == 1017 :
 I1IIIiI1I1ii1 ( )
 if 55 - 55: OOooOOo * iiiiiiii1 % oO0o - oO0o
elif iIiiiii1i == 1018 :
 II1i ( oOooO0 )
 if 34 - 34: o0o00Oo0O * oO0o - o000O0o - I1111IIi * ii1ii11IIIiiI . IIiIiII11i
elif iIiiiii1i == 1019 :
 i11111I1I ( oOooO0 )
elif iIiiiii1i == 10190 :
 I11o0oO00oO0o0o0 ( oOooO0 )
 if 28 - 28: o0o00Oo0O % O0OOOoOoo0 - ooOoO0O00
elif iIiiiii1i == 1023 :
 O0OOoOooO00 ( )
 if 49 - 49: I11i1ii1 . ooOOOoO - iI11I1II1I1I
elif iIiiiii1i == 1024 :
 oo0Oo0oo ( oOooO0 )
 if 41 - 41: I11i1ii1 * Ii % I11i1ii1 . o000O0o
elif iIiiiii1i == 1025 :
 IIiI1iIiii ( oOooO0 )
 if 97 - 97: o000O0o - O0OOOoOoo0 + I1111IIi . OOooOOo + iI11I1II1I1I
elif iIiiiii1i == 4001 :
 iI1i11 ( )
 if 75 - 75: I11i1ii1 + I11i1ii1 . iiiiiiii1 % O0OOOoOoo0 / iI11I1II1I1I * O0OOOoOoo0
elif iIiiiii1i == 4002 :
 II1I1Ii ( )
 if 13 - 13: IIiIiII11i * Ii - ooOoO0O00 * oO0o + ooOoO0O00
elif iIiiiii1i == 4003 :
 o00OOo ( )
 if 43 - 43: o0o00Oo0O % o000O0o * oOo0O0Ooo
elif iIiiiii1i == 4004 :
 iiIi1i ( )
 if 64 - 64: IIiIiII11i + Ii
elif iIiiiii1i == 4005 :
 o0oOO ( )
 if 17 - 17: o0o00Oo0O * oOo0O0Ooo
elif iIiiiii1i == 4006 :
 IIiiI ( )
 if 40 - 40: iI11I1II1I1I * O0OOOoOoo0 % iI11I1II1I1I
elif iIiiiii1i == 4007 :
 OOOOO0O00 ( )
 if 39 - 39: ooOoO0O00 . ii1ii11IIIiiI - I1ii11iIi11i
elif iIiiiii1i == 4008 :
 iIIiIiI1I1 ( )
 if 91 - 91: oOo0O0Ooo - ii - ii
elif iIiiiii1i == 4009 : OOo00ooOoO0o ( )
elif iIiiiii1i == 4010 : O00OoOoO ( )
elif iIiiiii1i == 3000 :
 ooOO0o0ooOo0 ( )
 if 69 - 69: O0OOOoOoo0 * Ii / ooOoO0O00
elif iIiiiii1i == 3001 :
 o0O0OOooO ( )
 if 86 - 86: oOo0O0Ooo % ooOOOoO * o0o00Oo0O + ooOoO0O00 % iiiiiiii1
elif iIiiiii1i == 3002 :
 i1II111i1IIii ( oOooO0 )
 if 97 - 97: IIiIiII11i * OOooOOo - iiiiiiii1 / Ii / OOooOOo
elif iIiiiii1i == 3003 :
 IIIi1ii1i1 ( oOooO0 )
 if 25 - 25: I1ii11iIi11i / I1ii11iIi11i
elif iIiiiii1i == 3004 :
 o00O0OooO0 ( oOooO0 )
 if 74 - 74: Ii1IIIi1
elif iIiiiii1i == 404 :
 O00oO0OOOo0 ( Iii1I1111ii , oOooO0 , iII1iii )
 if 30 - 30: o0o00Oo0O . ii1ii11IIIiiI / I11i + oOo0O0Ooo - o0o00Oo0O
elif iIiiiii1i == 405 :
 iiOO00O ( oOooO0 )
 if 88 - 88: Ii
elif iIiiiii1i == 7030 :
 IiIiiiIii1i ( )
 if 33 - 33: oO0o + o0o00Oo0O
elif iIiiiii1i == 7021 :
 oOo0OO0o0oO ( Iii1I1111ii )
 if 20 - 20: I11i % ooOOOoO . I11i1ii1 - ooOoO0O00 . o0o00Oo0O
elif iIiiiii1i == 7022 :
 o0O0oOOoo0O0 ( Iii1I1111ii )
 if 10 - 10: ooOoO0O00
elif iIiiiii1i == 7000 :
 o00ooo0oOo0o ( Iii1I1111ii , oOooO0 , img )
 if 49 - 49: iiiiiiii1 - ii1ii11IIIiiI . o0o00Oo0O
elif iIiiiii1i == 7050 :
 I111Iii1 ( oOooO0 )
 if 46 - 46: Ii1IIIi1
elif iIiiiii1i == 7051 :
 I1IO0 ( oOooO0 )
 if 64 - 64: oOo0O0Ooo / OOooOOo
elif iIiiiii1i == 7052 :
 i1IIiiI1iii1 ( oOooO0 )
 if 6 - 6: Ii - O0OOOoOoo0 * ooOoO0O00 - O0OOOoOoo0
elif iIiiiii1i == 7053 :
 o0OoO ( oOooO0 )
 if 8 - 8: ooOOOoO / Ii . o0o00Oo0O / oO0o * o000O0o + iiiiiiii1
elif iIiiiii1i == 7054 :
 CoolPlay ( oOooO0 )
 if 91 - 91: oOo0O0Ooo
elif iIiiiii1i == 7060 :
 iio0o0OoOo0 ( )
 if 84 - 84: o0o00Oo0O % ii1ii11IIIiiI
elif iIiiiii1i == 7061 :
 I1I1i ( oOooO0 )
 if 3 - 3: oOo0O0Ooo . ooOOOoO / Ii1I
elif iIiiiii1i == 7063 :
 o000O0OOo00O ( oOooO0 )
 if 2 - 2: I1111IIi + ooOOOoO / iI11I1II1I1I . Ii . ooOoO0O00 * I11i1ii1
elif iIiiiii1i == 7062 :
 ii11III1 ( oOooO0 )
 if 14 - 14: I1ii11iIi11i . o0o00Oo0O - o000O0o - Ii
elif iIiiiii1i == 7064 :
 NATatozcat ( )
 if 8 - 8: oOo0O0Ooo / iI11I1II1I1I / ii / I1ii11iIi11i / I11i1ii1
elif iIiiiii1i == 7067 :
 OOOoO0oo0oo0o ( oOooO0 )
 if 80 - 80: ooOOOoO
elif iIiiiii1i == 7066 :
 NATatozA ( oOooO0 )
 if 26 - 26: IIiIiII11i + oOo0O0Ooo . IIiIiII11i - o000O0o % oO0o
elif iIiiiii1i == 7065 :
 oo0OO0OooooO0 ( oOooO0 )
 if 1 - 1: oO0o - IIiIiII11i
elif iIiiiii1i == 7070 :
 IiiI1Ii1IIi ( )
 if 75 - 75: I1ii11iIi11i - OOooOOo + o000O0o % ooOoO0O00 * Ii1IIIi1
elif iIiiiii1i == 7071 :
 DIZIlist ( oOooO0 )
 if 56 - 56: OOooOOo / oO0o / oOo0O0Ooo % ii
elif iIiiiii1i == 7072 :
 DIZIpull ( oOooO0 )
 if 39 - 39: oOo0O0Ooo + IIiIiII11i * I1ii11iIi11i % ii1ii11IIIiiI . I11i * o000O0o
elif iIiiiii1i == 7073 :
 WATCHDIZI ( oOooO0 )
 if 42 - 42: ii1ii11IIIiiI / I1ii11iIi11i
elif iIiiiii1i == 7002 :
 iiiiIooo0O0O0OO ( )
 if 25 - 25: ii % ii1ii11IIIiiI * iiiiiiii1 * ooOOOoO + oOo0O0Ooo % Ii1I
elif iIiiiii1i == 7003 :
 i1iII ( oOooO0 )
 if 70 - 70: ii1ii11IIIiiI + Ii1I * ooOOOoO * ooOoO0O00 . iiiiiiii1
elif iIiiiii1i == 7004 :
 OOooo ( oOooO0 )
 if 76 - 76: ii * OOooOOo . ii
elif iIiiiii1i == 7020 :
 oOOOO00o00 ( oOooO0 )
 if 46 - 46: I11i1ii1 * I11i % IIiIiII11i / iiiiiiii1
elif iIiiiii1i == 7001 :
 iiOO0O0Ooo ( )
 if 29 - 29: oO0o - Ii % I1ii11iIi11i % I11i
elif iIiiiii1i == 7010 :
 Oo00 ( oOooO0 )
 if 30 - 30: o000O0o - ii1ii11IIIiiI % ii1ii11IIIiiI
elif iIiiiii1i == 7011 :
 O0OoOO0O0 ( oOooO0 )
 if 8 - 8: I1111IIi
elif iIiiiii1i == 7012 :
 oo0oO0oO00oO ( oOooO0 )
 if 68 - 68: I1111IIi . ii - Ii + Ii
elif iIiiiii1i == 7013 :
 cnfTVPlay2 ( oOooO0 )
elif iIiiiii1i == 7014 :
 CNF_Studio_Indexer . MV_Movies ( oOooO0 )
elif iIiiiii1i == 7015 :
 CNF_Studio_Indexer . Movie_ByYear ( oOooO0 )
elif iIiiiii1i == 7016 :
 CNF_Studio_Indexer . Resolve_CNF_Link ( Iii1I1111ii , oOooO0 , iII1iii )
elif iIiiiii1i == 7017 :
 CNF_Studio_Indexer . Search_Movie ( )
elif iIiiiii1i == 7018 :
 OooOoOOo0 ( )
elif iIiiiii1i == 7019 :
 CNF_Studio_Indexer . List_Movies ( oOooO0 )
elif iIiiiii1i == 7020 :
 CNF_Studio_Indexer . Get_Movie_Page ( oOooO0 )
elif iIiiiii1i == 7024 :
 CNF_Studio_Indexer . Box_Office ( oOooO0 )
 if 81 - 81: OOooOOo + O0OOOoOoo0 . Ii
elif iIiiiii1i == 8000 :
 iiIIi ( )
elif iIiiiii1i == 8001 :
 ii11 ( )
elif iIiiiii1i == 8002 :
 iIiiII11 ( )
elif iIiiiii1i == 8003 :
 oo00o ( )
elif iIiiiii1i == 8004 :
 II1oOO0O0Ooo0 ( )
elif iIiiiii1i == 8005 :
 iI11i1iI ( )
elif iIiiiii1i == 8006 :
 i1iOO ( Iii1I1111ii , oOooO0 )
elif iIiiiii1i == 8030 :
 iii1 ( oOooO0 )
elif iIiiiii1i == 8045 :
 o00OooooOOOO ( oOooO0 )
elif iIiiiii1i == 8046 :
 oo000oiIIIII ( oOooO0 )
elif iIiiiii1i == 8047 :
 IIoooOoOO0o ( oOooO0 )
elif iIiiiii1i == 8048 :
 iI1i11II1i1i ( oOooO0 )
elif iIiiiii1i == 8049 :
 O0O0O00OoO0O ( oOooO0 )
elif iIiiiii1i == 804900 :
 i1II11III ( oOooO0 )
elif iIiiiii1i == 8020 :
 iIi11i1 ( )
elif iIiiiii1i == 8021 :
 oo0oo00 ( oOooO0 )
elif iIiiiii1i == 8022 :
 ooO00OoO ( oOooO0 )
elif iIiiiii1i == 8023 :
 oo0OOO0O0 ( oOooO0 )
elif iIiiiii1i == 8040 :
 ooO ( )
elif iIiiiii1i == 8041 :
 III ( oOooO0 )
elif iIiiiii1i == 8042 :
 i1IiI1I111iI1 ( oOooO0 )
elif iIiiiii1i == 8043 :
 yt . PlayVideo ( oOooO0 )
elif iIiiiii1i == 8044 :
 oO00O000o ( oOooO0 )
elif iIiiiii1i == 8060 :
 iIi1Ii1i1iI ( )
elif iIiiiii1i == 8061 :
 i1oOOOoOO ( oOooO0 )
elif iIiiiii1i == 8064 :
 IiIIIIIi ( )
elif iIiiiii1i == 8065 :
 OOoo0o00O0oO ( oOooO0 )
elif iIiiiii1i == 8070 :
 Iii1iIII1Iii ( )
elif iIiiiii1i == 8071 :
 ii1ii1111 ( oOooO0 )
elif iIiiiii1i == 7080 :
 iII11iiii111i ( oOooO0 )
elif iIiiiii1i == 8090 :
 I1OO0o0OoooO00 ( )
elif iIiiiii1i == 8091 :
 i1II111II1 ( oOooO0 )
elif iIiiiii1i == 8092 :
 Ii1I1I11I1I1i ( oOooO0 )
elif iIiiiii1i == 8093 :
 I11I1iiI1 ( oOooO0 )
elif iIiiiii1i == 8081 :
 IIiIiI11IIiII1iII ( )
elif iIiiiii1i == 8062 :
 Ii1111i11 ( oOooO0 )
elif iIiiiii1i == 8063 :
 O0o0O00 ( oOooO0 )
elif iIiiiii1i == 8050 :
 IiIii11I ( )
elif iIiiiii1i == 8051 :
 Ooo0O00 ( oOooO0 )
elif iIiiiii1i == 8052 :
 oooo0oOOoO000 ( oOooO0 )
elif iIiiiii1i == 8085 :
 III11IiI ( )
elif iIiiiii1i == 8086 :
 Iii1iI1I1iii1 ( oOooO0 )
elif iIiiiii1i == 8087 :
 O0oOo00Oo0oo0 ( oOooO0 )
elif iIiiiii1i == 8088 :
 i111 ( oOooO0 , Iii1I1111ii )
elif iIiiiii1i == 9000 :
 OOo000o ( )
elif iIiiiii1i == 1111 :
 II1IIiiI1 ( )
elif iIiiiii1i == 9001 :
 I1i11111i1i11 ( )
elif iIiiiii1i == 9002 :
 O0o0OO0000ooo ( )
elif iIiiiii1i == 9003 :
 ooOOO ( )
elif iIiiiii1i == 9004 :
 World1 ( )
elif iIiiiii1i == 9005 :
 World2 ( oOooO0 )
elif iIiiiii1i == 9006 :
 World3 ( oOooO0 )
elif iIiiiii1i == 9007 :
 IiiIIIII111 ( )
elif iIiiiii1i == 9008 :
 II11iIIIii1i ( oOooO0 )
elif iIiiiii1i == 9009 :
 o00OooO ( oOooO0 )
elif iIiiiii1i == 9010 :
 iIi1 ( )
elif iIiiiii1i == 9011 :
 Iii11I1II1 ( oOooO0 )
elif iIiiiii1i == 50 :
 OoOO00oo0o ( oOooO0 )
elif iIiiiii1i == 9020 :
 champlist ( )
elif iIiiiii1i == 9021 :
 I11i1IiI1 ( )
elif iIiiiii1i == 9022 :
 o00oOO00 ( )
elif iIiiiii1i == 9023 :
 o00O0oOOo ( )
elif iIiiiii1i == 9024 :
 OOOO00oO ( oOooO0 )
elif iIiiiii1i == 9030 :
 IIII1iIii1Ii ( oOooO0 )
elif iIiiiii1i == 9031 :
 OoOO0OO00 ( oOooO0 )
elif iIiiiii1i == 9032 :
 IiiIi ( oOooO0 )
elif iIiiiii1i == 9033 :
 oOO0oOoooOo ( oOooO0 )
elif iIiiiii1i == 9034 :
 ooo0o00 ( )
elif iIiiiii1i == 7085 :
 iiiiI1iiIi1i ( oOooO0 )
elif iIiiiii1i == 7086 :
 I1iI1Ii1I1Iii1 ( oOooO0 )
elif iIiiiii1i == 7087 :
 I11iIIiIIiIi ( O00oo )
elif iIiiiii1i == 9666 :
 ooO0O0O0ooOOO ( oOooO0 )
elif iIiiiii1i == 10100 : O0OoOo0 ( )
elif iIiiiii1i == 101001 : I1I11I1i1i1II ( oOooO0 )
elif iIiiiii1i == 10105 : ii1II1I ( oOooO0 )
elif iIiiiii1i == 10106 : oOoo0 ( oOooO0 )
elif iIiiiii1i == 10104 : iIIIII ( oOooO0 )
elif iIiiiii1i == 10107 : ii1II11IIII1 ( )
elif iIiiiii1i == 10103 : oo0o0o ( oOooO0 )
elif iIiiiii1i == 10108 : iII11I ( oOooO0 )
elif iIiiiii1i == 10000 : Origin_Menu ( )
elif iIiiiii1i == 10001 : OOOooo0OooOoO ( )
elif iIiiiii1i == 10002 : IiIi ( )
elif iIiiiii1i == 10003 : oOiiIIIII ( )
elif iIiiiii1i == 10004 : ii1I ( oOooO0 )
elif iIiiiii1i == 10005 : I11I1IIiiII1 ( )
elif iIiiiii1i == 10006 : ooo000o ( oOooO0 )
elif iIiiiii1i == 10007 : ii1111Iii11i ( oOooO0 , iII1iii )
elif iIiiiii1i == 10008 : ooooooo ( )
elif iIiiiii1i == 10009 : iiii1i1 ( )
elif iIiiiii1i == 10010 : I111i ( oOooO0 )
elif iIiiiii1i == 10011 : IIi1I1 ( oOooO0 )
elif iIiiiii1i == 10012 : OOOoOO0o ( oOooO0 )
elif iIiiiii1i == 10113 : GRABG ( oOooO0 , Iii1I1111ii )
elif iIiiiii1i == 10109 : ooOOooooo0Oo ( oOooO0 )
elif iIiiiii1i == 10013 : ooo00OoOooooo ( oOooO0 )
elif iIiiiii1i == 10014 : Ii11iIiiI ( )
elif iIiiiii1i == 10015 : oooOOO0o0O0 ( )
elif iIiiiii1i == 10016 : IiI1iII1II111 ( oOooO0 )
elif iIiiiii1i == 10017 : ooOoOoo000O0O ( )
elif iIiiiii1i == 10018 : iIii111Ii ( )
elif iIiiiii1i == 10019 : o00o0o0oOo0 ( )
elif iIiiiii1i == 10020 : oooiI1i ( )
elif iIiiiii1i == 10021 : O0OoO00OoOO ( )
elif iIiiiii1i == 10022 : i1Io00OOOo ( oOooO0 )
elif iIiiiii1i == 10023 : o00IIIIii1111i1 ( Iii1I1111ii , oOooO0 )
elif iIiiiii1i == 10024 : O0ooO ( oOooO0 )
elif iIiiiii1i == 10025 : I1iii11 ( )
elif iIiiiii1i == 10026 : OO0 ( )
elif iIiiiii1i == 10027 : OoOoOo0o00OoOO ( )
elif iIiiiii1i == 10028 : O00OOOo ( )
elif iIiiiii1i == 10029 : IiOOo0 ( )
elif iIiiiii1i == 423 : ooOooOooOOO ( oOooO0 )
elif iIiiiii1i == 426 : OO00o0O0oOooO ( oOooO0 )
elif iIiiiii1i == 10030 : Izle_Films ( )
elif iIiiiii1i == 10031 : Latest_Izle_Movies ( )
elif iIiiiii1i == 10032 : Izle_Genres ( )
elif iIiiiii1i == 10033 : Izle_Pop_Movies ( )
elif iIiiiii1i == 10034 : Izle_Boxsets ( )
elif iIiiiii1i == 10035 : Izle_Search ( )
elif iIiiiii1i == 10036 : Izle_Genres_Movie ( oOooO0 )
elif iIiiiii1i == 10037 : Izle_Boxset_single ( oOooO0 )
elif iIiiiii1i == 10038 : Izle_IFRAME ( )
elif iIiiiii1i == 10039 : Izle_Boxsets_Next ( oOooO0 )
elif iIiiiii1i == 10040 : oOOO00o000o ( )
elif iIiiiii1i == 10041 : IiIiooooOOo ( oOooO0 )
elif iIiiiii1i == 10042 : i1II111ii1ii ( oOooO0 )
elif iIiiiii1i == 10043 : Iii1I1I ( )
elif iIiiiii1i == 10044 : Oooo0o00 ( oOooO0 )
elif iIiiiii1i == 10045 : ooOo ( Iii1I1111ii )
elif iIiiiii1i == 10046 : OOOOoOOOo0oOO ( oOooO0 )
elif iIiiiii1i == 10047 : oo00OOo0 ( oOooO0 )
elif iIiiiii1i == 10048 : IIIi ( oOooO0 )
elif iIiiiii1i == 10049 : oO0oO00 ( oOooO0 )
elif iIiiiii1i == 10050 : OOI1iI1ii1II ( )
elif iIiiiii1i == 10051 : OOII1iI ( )
elif iIiiiii1i == 10052 : Ooooo0OO ( )
elif iIiiiii1i == 10053 : Addon ( oOooO0 )
elif iIiiiii1i == 10054 : O000o ( oOooO0 , Iii1I1111ii )
elif iIiiiii1i == 10055 :
 o00o0OOoOo0O0 ( "addFavorite" )
 try :
  Iii1I1111ii = Iii1I1111ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Iii1I1111ii = Iii1I1111ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 iiI1i ( Iii1I1111ii , oOooO0 , iII1iii , I11iiiiI1i , iIIiii )
elif iIiiiii1i == 10056 :
 o00o0OOoOo0O0 ( "rmFavorite" )
 try :
  Iii1I1111ii = Iii1I1111ii . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Iii1I1111ii = Iii1I1111ii . split ( '  - ' ) [ 0 ]
 except :
  pass
 o00O0Oooo ( Iii1I1111ii )
elif iIiiiii1i == 10057 :
 o00o0OOoOo0O0 ( "getFavorites" )
 IIi1i1IIi ( )
elif iIiiiii1i == 10058 : i1i1iiIIiiiII ( )
elif iIiiiii1i == 10059 : Donators_Guide ( )
elif iIiiiii1i == 10060 : OoOOoooOO0O ( )
elif iIiiiii1i == 10061 : oOooOOo00ooO ( )
elif iIiiiii1i == 10062 : i1iIii ( Iii1I1111ii , oOooO0 , O00oo )
elif iIiiiii1i == 10063 : xbmc . executebuiltin ( "XBMC.RunScript(" + iiiiiIIii + ")" )
elif iIiiiii1i == 10064 : IiIIII1iiIIi ( )
elif iIiiiii1i == 10065 : ooooOoo0OO ( oOooO0 )
elif iIiiiii1i == 10066 : OOO0O00Oo ( oOooO0 )
elif iIiiiii1i == 10068 : IIIII1 ( oOooO0 )
elif iIiiiii1i == 10069 : IiIi1iIIi1 ( oOooO0 )
elif iIiiiii1i == 10070 : i111i1I1ii1i ( oOooO0 )
elif iIiiiii1i == 10071 : Genie_Watch ( )
elif iIiiiii1i == 10072 : Ooo0oO ( )
elif iIiiiii1i == 10073 : o00O0o0oo0oOO0oO ( oOooO0 )
elif iIiiiii1i == 10074 : IIi1iI11IIIi1 ( oOooO0 )
elif iIiiiii1i == 10075 : oo000oOO00o0oOO ( iII1iii , Iii1I1111ii , oOooO0 )
elif iIiiiii1i == 10076 : iI1I1 ( oOooO0 )
elif iIiiiii1i == 10077 : o00O ( oOooO0 )
elif iIiiiii1i == 10078 : iIIIIiiii1I ( )
elif iIiiiii1i == 10079 : Genie_Watch_Tv_Shows ( )
elif iIiiiii1i == 10080 : Genie_Watch_Tv_Genre ( oOooO0 )
elif iIiiiii1i == 10081 : Genie_Watch_TV_PlayRun ( oOooO0 )
elif iIiiiii1i == 10082 : Genie_Watch_TV_Episodes ( oOooO0 , iII1iii )
elif iIiiiii1i == 10083 : Genie_Watch_Tv_Recent ( oOooO0 )
elif iIiiiii1i == 10084 : O00oOo00o0o ( )
elif iIiiiii1i == 10085 : Iiii1i1 ( )
elif iIiiiii1i == 10086 : i1IiiiI1iI ( )
elif iIiiiii1i == 20000 : oOoOOOo ( )
elif iIiiiii1i == 20001 : i111IIIIiI ( oOooO0 )
elif iIiiiii1i == 20002 : OOoOoooOOO0 ( oOooO0 )
elif iIiiiii1i == 20003 : IIii1Ii1i1ii1 ( oOooO0 )
elif iIiiiii1i == 20004 : oO0OO ( oOooO0 )
elif iIiiiii1i == 20005 : oOO0Oo ( oOooO0 )
elif iIiiiii1i == 21004 : IIIIIii1ii11 ( )
elif iIiiiii1i == 21005 : ii111I1i1 ( oOooO0 )
elif iIiiiii1i == 21006 : iII1I ( oOooO0 )
elif iIiiiii1i == 21007 : o0OOoOooO0ooO ( oOooO0 )
elif iIiiiii1i == 30000 : O00O00 ( )
elif iIiiiii1i == 30001 : O0OoOo ( )
elif iIiiiii1i == 100121 : Resolve ( oOooO0 )
elif iIiiiii1i == 30003 : IIIIIiiI ( )
elif iIiiiii1i == 30004 : o0oO00OOo0oO ( oOooO0 )
elif iIiiiii1i == 30005 : II1Ooo0000o00OO ( oOooO0 )
elif iIiiiii1i == 30006 : O0OO ( )
elif iIiiiii1i == 30007 : IiOo00O0o0O ( )
elif iIiiiii1i == 30008 : o0i1I ( oOooO0 )
elif iIiiiii1i == 30009 : O0OOo ( oOooO0 )
elif iIiiiii1i == 30010 : oOiI1I ( oOooO0 )
elif iIiiiii1i == 30011 : IiIII ( )
elif iIiiiii1i == 30012 : o0Oo0ooo ( )
elif iIiiiii1i == 30013 : i1iIii1II1i ( )
elif iIiiiii1i == 30014 : Oo0O0OooOooo0 ( )
elif iIiiiii1i == 30015 : ii11Ii1IiiI1 ( oOooO0 , iII1iii , I11iiiiI1i )
elif iIiiiii1i == 30016 : OoO0o0OO ( oOooO0 )
elif iIiiiii1i == 30019 : O0o0oOOO ( oOooO0 )
elif iIiiiii1i == 30017 : o0oOOooo0o0O ( oOooO0 )
elif iIiiiii1i == 30018 : ooooooo00oO0OO ( oOooO0 )
elif iIiiiii1i == 30030 : iIiI ( )
elif iIiiiii1i == 30031 : I1Ii1i11I1I ( )
elif iIiiiii1i == 30032 : Iii ( )
elif iIiiiii1i == 30033 : Oo00o0OOo0OO ( )
elif iIiiiii1i == 30034 : I1i1iiIi ( )
elif iIiiiii1i == 30035 : I1Ii1 ( oOooO0 )
elif iIiiiii1i == 30036 : O0oo0oOoO00 ( oOooO0 )
elif iIiiiii1i == 30037 : i1ii1iIi ( oOooO0 )
elif iIiiiii1i == 30038 : Iiiii1I ( )
elif iIiiiii1i == 30039 : Ii1I1i ( )
elif iIiiiii1i == 50000 : iIiIi11 ( )
elif iIiiiii1i == 50001 : O0OooooO0o0O0 ( )
elif iIiiiii1i == 50002 : oo0I1I1iiI1i ( oOooO0 )
elif iIiiiii1i == 50003 : Table_Menu ( O00oo )
elif iIiiiii1i == 60000 : oo00 . openSettings ( sys . argv [ 0 ] )
elif iIiiiii1i == 60001 : oOoO00O000 ( )
elif iIiiiii1i == 60002 : II1 ( Iii1I1111ii )
elif iIiiiii1i == 60003 : i1iI1Iiii1I ( oOooO0 )
elif iIiiiii1i == 600033 : oO0O0o0O ( oOooO0 )
elif iIiiiii1i == 60004 : IiI1III ( oOooO0 )
elif iIiiiii1i == 50004 : IiIi1I1 ( )
elif iIiiiii1i == 50005 : speedtest . runtest ( oOooO0 )
elif iIiiiii1i == 70001 : Ii11III ( )
elif iIiiiii1i == 70002 : I11iIiI1 ( oOooO0 )
elif iIiiiii1i == 70003 : i1I1iiii1Ii11 ( oOooO0 )
elif iIiiiii1i == 70004 : IiIIIIi ( oOooO0 )
elif iIiiiii1i == 70005 : Oo ( oOooO0 )
elif iIiiiii1i == 70006 : IIiIIIII1I ( )
elif iIiiiii1i == 50006 : iiIiI1i1 ( i1 , i1111 )
elif iIiiiii1i == 80000 : oO0OOO00 ( )
elif iIiiiii1i == 80001 : resolvefilmon ( oOooO0 )
elif iIiiiii1i == 80002 : IiI11IIi11Iii ( )
elif iIiiiii1i == 80003 : iI1IIII1 ( Iii1I1111ii , oOooO0 , "None" )
elif iIiiiii1i == 80004 : I1I1Ii ( Iii1I1111ii , oOooO0 )
elif iIiiiii1i == 80005 : I1IIIiIiIi ( )
elif iIiiiii1i == 80006 : oo0OoOOooO ( oOooO0 )
elif iIiiiii1i == 80007 : o0o0OO0o00o0O ( oOooO0 )
elif iIiiiii1i == 80008 : IIIIIIi1i ( )
elif iIiiiii1i == 80009 : IiI1i1I11I ( )
elif iIiiiii1i == 80010 : oO0o0ooooo ( oOooO0 )
elif iIiiiii1i == 80011 : OoO0OO0 ( oOooO0 )
elif iIiiiii1i == 80012 : oOOO ( )
elif iIiiiii1i == 90000 : Ii1I1i1IiiI ( Iii1I1111ii , oOooO0 )
elif iIiiiii1i == 90001 : II11 ( )
elif iIiiiii1i == 90002 : OOoOiiII1i11i ( )
elif iIiiiii1i == 90003 : i1Iii1i1II1 ( oOooO0 )
elif iIiiiii1i == 90004 : O0o00OoooO ( oOooO0 )
elif iIiiiii1i == 90005 : IiI1i1iI ( oOooO0 )
elif iIiiiii1i == 90006 : OOo0ooOOOo0O0 ( oOooO0 )
elif iIiiiii1i == 90007 : ooI1 ( oOooO0 )
elif iIiiiii1i == 90008 : oooii111I1I1I ( oOooO0 )
elif iIiiiii1i == 90009 : Oo0O ( oOooO0 )
elif iIiiiii1i == 90010 : oO0O00oOOoooO ( )
elif iIiiiii1i == 90020 : Oo0 ( )
elif iIiiiii1i == 90021 : hellyeah2 ( oOooO0 )
elif iIiiiii1i == 90022 : hellyeah3 ( oOooO0 )
elif iIiiiii1i == 90023 : oOO0oo ( )
elif iIiiiii1i == 90024 : iiiiI11ii ( oOooO0 )
elif iIiiiii1i == 90025 : o0o000 ( oOooO0 )
if 10 - 10: OOooOOo + ooOOOoO - iI11I1II1I1I - ooOOOoO
elif iIiiiii1i == 900300 : OOOO0OoOO0o0o ( )
elif iIiiiii1i == 900301 : ooI1111i ( oOooO0 )
elif iIiiiii1i == 900302 : Ii1IIiI1i ( oOooO0 )
elif iIiiiii1i == 90030 : i111iIi1i1II1 ( )
elif iIiiiii1i == 90031 : i1i1iI1iiiI ( )
elif iIiiiii1i == 90032 : Ooo0oOooo0 ( oOooO0 )
elif iIiiiii1i == 90033 : oOOOoo00 ( oOooO0 )
elif iIiiiii1i == 90034 : ooO000OO0O00O ( oOooO0 )
elif iIiiiii1i == 90035 : i1II1 ( oOooO0 )
elif iIiiiii1i == 90036 : ii11iI1i1i1i1i ( oOooO0 )
elif iIiiiii1i == 90039 : iiII1i1II1iIi ( oOooO0 )
elif iIiiiii1i == 90037 : i11i1iiiII ( oOooO0 )
elif iIiiiii1i == 90038 : ii1Ii11IiiI1 ( )
if 58 - 58: I11i1ii1
elif iIiiiii1i == 10090 : iIIII1iIIii ( )
elif iIiiiii1i == 10091 : II1i1 ( oOooO0 )
elif iIiiiii1i == 10092 : iI11i1I1i ( oOooO0 )
elif iIiiiii1i == 10093 : OoOo0000o0OOo ( oOooO0 , iII1iii )
elif iIiiiii1i == 10094 : I11i1iiiiIIIi ( oOooO0 , iII1iii )
if 98 - 98: ii1ii11IIIiiI / oO0o % ii
elif iIiiiii1i == 10095 : oO00oo0o00o0o ( )
elif iIiiiii1i == 10096 : i1iii11 ( oOooO0 )
elif iIiiiii1i == 10097 : iIooo0oo ( oOooO0 )
elif iIiiiii1i == 10098 : iI11Ii111 ( oOooO0 )
elif iIiiiii1i == 10099 : I1I1I11Ii ( oOooO0 )
if 65 - 65: I11i1ii1 % I1ii11iIi11i - oOo0O0Ooo % iiiiiiii1 + iI11I1II1I1I / iI11I1II1I1I
elif iIiiiii1i == 10200 : OOoOOO0 ( )
elif iIiiiii1i == 10201 : oo0OOOOOO0 ( oOooO0 )
elif iIiiiii1i == 10202 : iiii ( oOooO0 )
elif iIiiiii1i == 10203 : RT4 ( oOooO0 )
if 94 - 94: I1111IIi - I1ii11iIi11i . I11i - I11i1ii1 - o000O0o . ooOOOoO
elif iIiiiii1i == 90040 : oOOo0OoOOOoo ( )
elif iIiiiii1i == 90041 : i1i1Ii11Ii ( oOooO0 )
elif iIiiiii1i == 90042 : Ii1iiII1i ( oOooO0 )
elif iIiiiii1i == 90043 : o0Oi11i1I ( oOooO0 )
elif iIiiiii1i == 90044 : ii11iIIi ( oOooO0 )
elif iIiiiii1i == 90045 : OooooO ( )
elif iIiiiii1i == 90046 : i1II1II1iii1i ( oOooO0 )
elif iIiiiii1i == 90050 : I1IIiiI1II1 ( )
elif iIiiiii1i == 90051 : iIiI1I1IIi11 ( oOooO0 )
elif iIiiiii1i == 90052 : I1iiII11IiIi1 ( oOooO0 )
elif iIiiiii1i == 90053 : oo000oO ( oOooO0 )
elif iIiiiii1i == 90054 : I11i11i1 ( oOooO0 )
elif iIiiiii1i == 90055 : iIIi11 ( )
if 39 - 39: o000O0o + OOooOOo
elif iIiiiii1i == 100001 : Stand_up ( )
if 68 - 68: ooOoO0O00 * o000O0o / Ii
elif iIiiiii1i == 100003 : IiI1iII1II111 ( oOooO0 )
elif iIiiiii1i == 100004 : oO0o00oOOooO0 ( oOooO0 )
elif iIiiiii1i == 100005 : Resolve ( oOooO0 )
elif iIiiiii1i == 100008 : Search ( )
elif iIiiiii1i == 100007 : oOOOoo ( oOooO0 )
elif iIiiiii1i == 100009 : yt . PlayVideo ( oOooO0 )
elif iIiiiii1i == 100010 : I1iIIIi1 ( oOooO0 )
elif iIiiiii1i == 100100 : I1IIIiii1 ( iII1iii , oOooO0 , ooOooO0O )
elif iIiiiii1i == 100101 : Ooo0oo ( oOooO0 , Iii1I1111ii , I11iiiiI1i , ooOooO0O , iII1iii )
elif iIiiiii1i == 100102 : oOO ( Iii1I1111ii , oOooO0 , iII1iii , I11iiiiI1i )
elif iIiiiii1i == 100106 : I1I ( oOooO0 , Iii1I1111ii )
elif iIiiiii1i == 100107 : IiiiI ( )
elif iIiiiii1i == 100108 : ii11iIII111 ( )
elif iIiiiii1i == 100109 : OoOoO0o0oO0 ( oOooO0 )
elif iIiiiii1i == 40000 : IIiii11ii1i ( )
elif iIiiiii1i == 40001 : oO0O ( oOooO0 )
elif iIiiiii1i == 100110 : o0i1I11iI1iiI ( )
elif iIiiiii1i == 100111 : I1 ( oOooO0 )
elif iIiiiii1i == 100110 : o0i1I11iI1iiI ( )
elif iIiiiii1i == 100210 : I1iIiI11I1 ( oOooO0 )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
